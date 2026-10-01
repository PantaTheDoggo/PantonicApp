"""T7 (`docs/plans/P-0734-execucao-autonoma.md` `### T7`) — `docs/telemetria.tsv` deixa de ser
editado à mão. Cada linha nova passa por `python .claude/tools/telemetria.py append ...`: valida
tipo e domínio de cada coluna antes de tocar o arquivo, falha ruidosa (exit != 0) em qualquer
coluna inválida sem escrever nada, e faz a escrita em modo atômico (arquivo temporário no mesmo
diretório + `os.replace`) — nenhum leitor concorrente vê um arquivo parcialmente escrito, e,
sem `--agente`, o conteúdo anterior nunca é tocado por conteúdo (só ganha uma linha no final;
com `--agente`, ver o parágrafo seguinte).

A série histórica é insumo — sem `--agente`, nenhuma linha existente é reescrita, reordenada ou
normalizada, e o script só apende; com `--agente` (`DRF-18`, `DRF-39` do `P-0755`), a linha do
mesmo agente é substituída, e a série sem a coluna `agente` a ganha, com `-` nas linhas antigas.
Colunas na ordem do header real do TSV: `data`, `projeto`, `tarefa`, `modelo`, `tool_uses`,
`tokens_k`, `duracao_s`, `fonte` e, na série migrada, `agente`. O mapeamento é sempre por nome
de coluna (nunca por posição), o que elimina o risco de "coluna trocada em silêncio" que a
edição manual admitia.

A célula vazia é a sentinela de métrica não medida. `tool_uses`, `tokens_k` e `duracao_s` aceitam
célula vazia sempre que `fonte` é `contado` ou `nao_medido`. Com `fonte=usage` os três campos são
obrigatórios: o bloco de uso reportado sempre os carrega, e célula vazia ali é medida perdida, não
ausente.

CLI: ``python .claude/tools/telemetria.py append --data AAAA-MM-DD --projeto P --tarefa T
--modelo M --tool_uses N --tokens_k K --duracao_s S --fonte {usage,contado,nao_medido}
[--file caminho/para/telemetria.tsv] [--agente A]``. Sem `--file`, resolve `docs/telemetria.tsv`
a partir da raiz do repositório (mesmo desenho do `--root` de `.claude/checks/dead_code.py`: a
raiz é derivada da posição do próprio script, não do diretório de trabalho).
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


class TelemetriaRepetidaError(ValueError):
    """A última linha da mesma `tarefa` na série já tem `modelo`, `tool_uses` e `tokens_k`
    iguais (DFP-8) — mesma rodada, recusada antes de qualquer escrita."""


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


def ultima_linha_da_tarefa(path: Path, tarefa: str) -> dict[str, str] | None:
    """Última linha da série cuja coluna `tarefa` bate com `tarefa`, ou `None` se a série não
    existe ou não tem nenhuma. Cabeçalho: a primeira linha quando ela começa por `data\t`; sem
    cabeçalho (arquivo criado pelo próprio `append_row`, que não escreve header), as colunas
    seguem `_COLUMNS`."""
    if not path.exists():
        return None
    linhas = [linha for linha in path.read_text(encoding="utf-8").splitlines() if linha]
    if not linhas:
        return None
    colunas = _COLUMNS
    if linhas[0].startswith("data\t"):
        colunas = tuple(linhas[0].split("\t"))
        linhas = linhas[1:]
    ultima = None
    for linha in linhas:
        registro = dict(zip(colunas, linha.split("\t")))
        if registro.get("tarefa") == tarefa:
            ultima = registro
    return ultima


def eh_repetida(ultima: dict, nova: dict) -> bool:
    """`True` quando `modelo`, `tool_uses` e `tokens_k` são iguais como texto entre as duas
    linhas (DFP-8) — a comparação que define "mesma rodada"; `duracao_s` não entra."""
    return all(ultima.get(campo) == nova.get(campo) for campo in ("modelo", "tool_uses", "tokens_k"))


def checar_repetida(path: Path, row: str) -> None:
    """Lê `row` pelas colunas de `_COLUMNS` e lança `TelemetriaRepetidaError` quando a última
    linha da mesma `tarefa` na série de `path` já tem `modelo`, `tool_uses` e `tokens_k` iguais
    (DFP-8) — chamada antes de qualquer escrita sem agente (`append_row` e o `encerrar.py`),
    para que a recusa valha para todo escritor sem agente; o escritor por agente não a chama:
    nele a mesma rodada é a linha do mesmo agente, que `gravar_por_agente` substitui (`DRF-69`
    do `P-0755`)."""
    nova = dict(zip(_COLUMNS, row.split("\t")))
    ultima = ultima_linha_da_tarefa(path, nova.get("tarefa", ""))
    if ultima is not None and eh_repetida(ultima, nova):
        raise TelemetriaRepetidaError(
            f"linha repetida: {nova['tarefa']} já tem linha com modelo, tool_uses e tokens_k "
            f"iguais (data {ultima.get('data')})"
        )


def _tem_coluna_agente(path: Path) -> bool:
    """`True` quando a série em `path` já tem cabeçalho e a última coluna dele é `agente`
    (`R-16`, `DRF-18`/`DRF-39` do `P-0755`) — série já migrada pelo escritor de agente."""
    if not path.exists():
        return False
    linhas = path.read_text(encoding="utf-8").splitlines()
    if not linhas:
        return False
    primeira = linhas[0]
    if not primeira.startswith("data\t"):
        return False
    colunas = primeira.split("\t")
    return bool(colunas) and colunas[-1] == "agente"


def gravar_por_agente(path: Path, row: str, agente: str) -> None:
    """Escreve uma linha por agente na série (`DRF-18`, `DRF-39` do `P-0755`, `R-16`): a linha
    nova do mesmo `agente` substitui a linha antiga dele, em vez de apensar. Cabeçalho ausente
    ganha o de `_COLUMNS`; cabeçalho que não termina na coluna `agente` ganha `\tagente`, e cada
    linha de dado existente ganha `\t-` (a coluna nova nasce vazia para elas). Escrita atômica:
    arquivo temporário no mesmo diretório e `os.replace`, como `append_row`. Não chama
    `checar_repetida` (DFP-8): a linha do mesmo agente é a mesma rodada, e a troca a deixa
    idempotente (`DRF-69` do `P-0755`)."""
    linhas: list[str] = []
    if path.exists():
        linhas = [linha for linha in path.read_text(encoding="utf-8").splitlines() if linha]

    if not linhas or not linhas[0].startswith("data\t"):
        cabecalho = list(_COLUMNS)
        dados = linhas
    else:
        cabecalho = linhas[0].split("\t")
        dados = linhas[1:]

    if not cabecalho or cabecalho[-1] != "agente":
        cabecalho = cabecalho + ["agente"]
        dados = [linha + "\t-" for linha in dados]

    linha_nova = row + "\t" + agente
    indice_agente = len(cabecalho) - 1
    substituida = False
    novas_linhas_dado = []
    for linha in dados:
        valores = linha.split("\t")
        if len(valores) > indice_agente and valores[indice_agente] == agente:
            novas_linhas_dado.append(linha_nova)
            substituida = True
        else:
            novas_linhas_dado.append(linha)
    if not substituida:
        novas_linhas_dado.append(linha_nova)

    conteudo = ("\t".join(cabecalho) + "\n" + "\n".join(novas_linhas_dado) + "\n").encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=str(path.parent), prefix=".telemetria-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as tmp_file:
            tmp_file.write(conteudo)
        os.replace(tmp_path, path)
    except Exception:
        Path(tmp_path).unlink(missing_ok=True)
        raise


def append_row(path: Path, row: str) -> None:
    """Escrita atômica em modo append: lê o conteúdo atual (bytes, sem interpretar), monta
    conteúdo-anterior + linha-nova num arquivo temporário no mesmo diretório, e substitui via
    `os.replace` — o arquivo final nunca fica parcialmente escrito, e o conteúdo anterior nunca
    é alterado, só sucedido pela linha nova. Recusa a linha repetida da mesma rodada (DFP-8)
    antes de ler os bytes — a recusa vale para todo escritor sem agente, não só o CLI; a linha
    com agente vai a `gravar_por_agente`, que não recusa (`DRF-69` do `P-0755`)."""
    checar_repetida(path, row)
    # `DRF-39` do `P-0755`: série já migrada para a coluna `agente` (R-16) recebendo `append_row`
    # sem `--agente` (escritor que não passa por `gravar_por_agente`) — a linha ganha `-` na
    # coluna nova para não desalinhar contra o cabeçalho.
    if _tem_coluna_agente(path) and len(row.split("\t")) == len(_COLUMNS):
        row = row + "\t-"
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

    append_parser = subparsers.add_parser(
        "append", help="Adiciona uma linha validada ao TSV; com --agente, troca a do mesmo agente."
    )
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
    append_parser.add_argument(
        "--agente", default=None,
        help="Agente da linha (R-16): substitui a linha do mesmo agente em vez de apensar.",
    )

    args = parser.parse_args(argv)

    if args.command == "append":
        target = args.file if args.file is not None else _default_tsv_path()
        try:
            row = build_row(args)
        except TelemetriaValidationError as exc:
            print(f"telemetria: FALHOU - {exc}", file=sys.stderr)
            return 1
        if args.agente is not None:
            gravar_por_agente(target, row, args.agente)
            print(f"telemetria: OK - linha do agente '{args.agente}' gravada em '{target}'.")
            return 0
        try:
            append_row(target, row)
        except TelemetriaRepetidaError as exc:
            print(f"telemetria: FALHOU - {exc}", file=sys.stderr)
            return 3
        print(f"telemetria: OK - linha adicionada a '{target}'.")
        return 0

    parser.error(f"comando desconhecido: {args.command}")
    return 2


if __name__ == "__main__":
    sys.exit(main())
