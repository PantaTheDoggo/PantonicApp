"""T7 (`docs/plans/P-0734-execucao-autonoma.md` `### T7`) — `docs/telemetria.tsv` deixa de ser
editado à mão. Cada linha nova passa por `python .claude/tools/telemetria.py append ...`: valida
tipo e domínio de cada coluna antes de tocar o arquivo, falha ruidosa (exit != 0) em qualquer
coluna inválida sem escrever nada, e faz a escrita em modo atômico (arquivo temporário no mesmo
diretório + `os.replace`) — nenhum leitor concorrente vê um arquivo parcialmente escrito, e o
conteúdo anterior nunca é tocado por conteúdo (só ganha uma linha no final).

A série histórica é insumo — nenhuma linha existente é reescrita, reordenada ou normalizada; o
script só apende. Colunas na ordem do header real do TSV: `data`, `projeto`, `tarefa`, `modelo`,
`tool_uses`, `tokens_k`, `duracao_s`, `fonte`. O mapeamento é sempre por nome de coluna (nunca por
posição), o que elimina o risco de "coluna trocada em silêncio" que a edição manual admitia.

A célula vazia é a sentinela de métrica não medida. `tool_uses`, `tokens_k` e `duracao_s` aceitam
célula vazia sempre que `fonte` é `contado` ou `nao_medido`. Com `fonte=usage` os três campos são
obrigatórios: o bloco de uso reportado sempre os carrega, e célula vazia ali é medida perdida, não
ausente.

CLI: ``python .claude/tools/telemetria.py append --data AAAA-MM-DD --projeto P --tarefa T
--modelo M --tool_uses N --tokens_k K --duracao_s S --fonte {usage,contado,nao_medido}
[--file caminho/para/telemetria.tsv]``. Sem `--file`, resolve `docs/telemetria.tsv` a partir da
raiz do repositório (mesmo desenho do `--root` de `.claude/checks/dead_code.py`: a raiz é
derivada da posição do próprio script, não do diretório de trabalho).
"""
from __future__ import annotations

import argparse
import datetime
import math
import os
import sys
import tempfile
from pathlib import Path

_COLUMNS = ("data", "projeto", "tarefa", "modelo", "tool_uses", "tokens_k", "duracao_s", "fonte")
_FONTE_VALIDOS = {"usage", "contado", "nao_medido"}
_FORBIDDEN_CHARS = ("\t", "\n", "\r")


class TelemetriaValidationError(ValueError):
    """Coluna inválida — tipo ou domínio (mensagem já traz o nome da coluna)."""


def _validar_texto(nome: str, valor: str) -> str:
    if not valor or not valor.strip():
        raise TelemetriaValidationError(f"{nome}: vazio")
    if any(ch in valor for ch in _FORBIDDEN_CHARS):
        raise TelemetriaValidationError(f"{nome}: contém tab/newline — corromperia o TSV")
    return valor


def _validar_data(valor: str) -> str:
    try:
        datetime.date.fromisoformat(valor)
    except ValueError as exc:
        raise TelemetriaValidationError(f"data: '{valor}' não é AAAA-MM-DD válido") from exc
    return valor


def _validar_inteiro_nao_negativo(nome: str, valor: str, permite_vazio: bool = False) -> str:
    if permite_vazio and valor == "":
        return valor
    try:
        numero = int(valor)
    except ValueError as exc:
        raise TelemetriaValidationError(f"{nome}: '{valor}' não é inteiro") from exc
    if numero < 0:
        raise TelemetriaValidationError(f"{nome}: '{valor}' é negativo")
    return str(numero)


def _validar_numero_nao_negativo(nome: str, valor: str, permite_vazio: bool = False) -> str:
    if permite_vazio and valor == "":
        return valor
    try:
        numero = float(valor)
    except ValueError as exc:
        raise TelemetriaValidationError(f"{nome}: '{valor}' não é numérico") from exc
    if not math.isfinite(numero):
        raise TelemetriaValidationError(f"{nome}: '{valor}' não é finito")
    if numero < 0:
        raise TelemetriaValidationError(f"{nome}: '{valor}' é negativo")
    # Preserva a forma original recebida (ex.: "44", não "44.0") — só a validação usa float().
    return valor


def _validar_fonte(valor: str) -> str:
    if valor not in _FONTE_VALIDOS:
        raise TelemetriaValidationError(
            f"fonte: '{valor}' fora do domínio {sorted(_FONTE_VALIDOS)}"
        )
    return valor


def build_row(args: argparse.Namespace) -> str:
    """Valida todas as colunas e devolve a linha TSV pronta (sem newline final). Lança
    `TelemetriaValidationError` na primeira coluna inválida — nada é escrito em disco a partir
    daqui; quem chama decide o que fazer com a exceção.

    `tool_uses`/`tokens_k`/`duracao_s` aceitam célula vazia quando `fonte` não é `usage` — a
    sentinela de métrica não medida. Com `fonte=usage` os três continuam obrigatórios."""
    fonte = _validar_fonte(args.fonte)
    permite_vazio = fonte != "usage"
    valores = {
        "data": _validar_data(args.data),
        "projeto": _validar_texto("projeto", args.projeto),
        "tarefa": _validar_texto("tarefa", args.tarefa),
        "modelo": _validar_texto("modelo", args.modelo),
        "tool_uses": _validar_inteiro_nao_negativo("tool_uses", args.tool_uses, permite_vazio),
        "tokens_k": _validar_numero_nao_negativo("tokens_k", args.tokens_k, permite_vazio),
        "duracao_s": _validar_numero_nao_negativo("duracao_s", args.duracao_s, permite_vazio),
        "fonte": fonte,
    }
    return "\t".join(valores[coluna] for coluna in _COLUMNS)


def append_row(path: Path, row: str) -> None:
    """Escrita atômica em modo append: lê o conteúdo atual (bytes, sem interpretar), monta
    conteúdo-anterior + linha-nova num arquivo temporário no mesmo diretório, e substitui via
    `os.replace` — o arquivo final nunca fica parcialmente escrito, e o conteúdo anterior nunca
    é alterado, só sucedido pela linha nova."""
    existing = path.read_bytes() if path.exists() else b""
    if existing and not existing.endswith(b"\n"):
        existing += b"\n"
    new_content = existing + row.encode("utf-8") + b"\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=str(path.parent), prefix=".telemetria-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as tmp_file:
            tmp_file.write(new_content)
        os.replace(tmp_path, path)
    except Exception:
        Path(tmp_path).unlink(missing_ok=True)
        raise


def _default_tsv_path() -> Path:
    root = Path(__file__).resolve().parent.parent.parent
    return root / "docs" / "telemetria.tsv"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Apêndice validado de docs/telemetria.tsv — a série deixa de ser editada à mão."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    append_parser = subparsers.add_parser("append", help="Adiciona uma linha validada ao TSV.")
    append_parser.add_argument("--data", required=True)
    append_parser.add_argument("--projeto", required=True)
    append_parser.add_argument("--tarefa", required=True)
    append_parser.add_argument("--modelo", required=True)
    append_parser.add_argument("--tool_uses", required=True)
    append_parser.add_argument("--tokens_k", required=True)
    append_parser.add_argument("--duracao_s", required=True)
    append_parser.add_argument("--fonte", required=True)
    append_parser.add_argument(
        "--file", type=Path, default=None, help="Caminho do TSV (default: docs/telemetria.tsv)."
    )

    args = parser.parse_args(argv)

    if args.command == "append":
        target = args.file if args.file is not None else _default_tsv_path()
        try:
            row = build_row(args)
        except TelemetriaValidationError as exc:
            print(f"telemetria: FALHOU - {exc}", file=sys.stderr)
            return 1
        append_row(target, row)
        print(f"telemetria: OK - linha adicionada a '{target}'.")
        return 0

    parser.error(f"comando desconhecido: {args.command}")
    return 2


if __name__ == "__main__":
    sys.exit(main())
