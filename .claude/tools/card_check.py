"""LM-T5b (`docs/plans/P-0740-loop-de-modulos.md` `### LM-T5b`) — a régua de autoria que roda:
`python .claude/tools/card_check.py --plano <plano> --tarefa <ID>` recorta o bloco `Verificação`
do card pela forma normativa de `docs/RUBRICA_DE_REVISAO.md` `### 8.1` (comando em bloco cercado,
linha `→` com o esperado, literal `**Medido antes: <valor>**`), exige os três elementos em cada
item e **roda** cada comando publicado, comparando a saída medida agora com o `Medido antes`
declarado — divergência é falha nomeada, porque significa que o card descreve um mundo que não é
o que está na árvore.

Reusa `rdo.extrair_dossie` (que por sua vez usa `rdo._parsear_campos`, `.claude/tools/rdo.py:187`,
para localizar o cabeçalho da tarefa e recortar o bloco de campos) — o parser de campos é
**importado, nunca reescrito**. Carregado por caminho via `importlib.util.spec_from_file_location`,
mesmo padrão de `review_evidence.py` (`.claude/` não é pacote importável).

Contrato de segurança: a decisão é **por token**, depois de `shlex.split` — só executa comando
cujo primeiro token esteja na lista fechada (`python`, `pwsh`) e recusa — reportado, nunca
executado — qualquer comando com um **token isolado** que seja operador de shell (`;`, `&&`,
`||`, `|`, `>`, `>>`, `<`, `<<`) ou comece por substituição de comando (`` ` ``, `$(`). O conteúdo
de um argumento citado não é varrido por metacaractere: a justificativa é o próprio modo de
execução — `subprocess.run` roda os tokens **sem `shell=True`**, então um `|` dentro de um
argumento citado é texto do argumento, nunca operador.

Só afere e reporta o bloco `Verificação`: não corrige card, não julga objetivo/passos/restrições e
não substitui o `pantonic-reviewer` — roda **antes** do despacho, não depois da entrega. `rdo.py`,
`backlog.py` e `review_evidence.py` ficam intocados."""
from __future__ import annotations

import argparse
import importlib.util
import re
import shlex
import subprocess
import sys
from pathlib import Path


class CardCheckValidationError(ValueError):
    """Plano, tarefa ou dossiê inválidos (mensagem já nomeia o problema)."""


def _default_root() -> Path:
    return Path(__file__).resolve().parent.parent.parent


def _exigir_plano(plano_path: Path) -> None:
    if not plano_path.is_file():
        raise CardCheckValidationError(f"plano: arquivo não encontrado '{plano_path}'")


def _load_rdo(root: Path):
    caminho = root / ".claude" / "tools" / "rdo.py"
    if not caminho.is_file():
        raise CardCheckValidationError(f"rdo.py: módulo não encontrado em '{caminho}'")
    spec = importlib.util.spec_from_file_location("rdo", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def _forcar_utf8(stream) -> None:
    """Console cp1252 do Windows estoura `UnicodeEncodeError` ao imprimir `→` — duplicado do
    mesmo utilitário de `review_evidence.py` (`DM-11`, sem import cruzado entre módulos)."""
    reconfigure = getattr(stream, "reconfigure", None)
    if reconfigure is not None:
        reconfigure(encoding="utf-8", errors="replace")


# --- forma normativa (`docs/RUBRICA_DE_REVISAO.md` `### 8.1`): recortada do texto já achatado
# por `rdo._parsear_campos` (linhas do campo juntadas com espaço, sem quebra de linha) ---

# Marcador de início de item: "N." precedido do início do texto ou de espaço (equivalente, no
# texto já achatado em uma linha só, ao `^\s*\d+\.` da forma da 8.1 sobre o markdown original —
# cada quebra de linha da fonte virou um único espaço no join de `rdo._parsear_campos`).
_ITEM_MARKER_RE = re.compile(r"(?:^|(?<=\s))(?P<num>\d+)\.")
_ABERTURA_BLOCO_RE = re.compile(r"\s*```")
_MEDIDO_ANTES_RE = re.compile(r"\*\*Medido antes:\s*(?P<valor>[^*]+?)\*\*")
_SETA_RE = re.compile(r"→\s*(?P<esperado>.+?)(?=\*\*Medido antes:|$)")
_AFERICAO_MANUAL_RE = re.compile(r"\*\*Aferição:\s*manual\*\*")

_COMANDOS_PERMITIDOS = ("python", "pwsh")
_TOKENS_SHELL_RECUSADOS = frozenset({";", "&&", "||", "|", ">", ">>", "<", "<<"})
_EXIT_RE = re.compile(r"^exit\s+(-?\d+)$", re.IGNORECASE)


class ItemVerificacao:
    """Um item do bloco `Verificação` na forma normativa da `### 8.1`. Classe simples (não
    `@dataclass`), mesmo motivo de `DossieTarefa`/`LaudoResultado` em `rdo.py`: módulo carregado
    por caminho via `importlib` nos testes e nas ferramentas irmãs."""

    def __init__(
        self,
        indice: int,
        comando: str | None,
        esperado: str | None,
        medido_antes: str | None,
        afericao_manual: bool,
    ):
        self.indice = indice
        self.comando = comando
        self.esperado = esperado
        self.medido_antes = medido_antes
        self.afericao_manual = afericao_manual


def _parsear_itens(texto: str) -> tuple[list[ItemVerificacao], list[str]]:
    """`(itens, falhas_forma)`. Varre **todo** marcador `N.` de início de item (`_ITEM_MARKER_RE`)
    — não só os que já vêm com bloco cercado logo em seguida. Marcador cujo bloco cercado não vem
    **imediatamente** depois vira uma linha em `falhas_forma` (`item N: fora da forma da 8.1`) e
    **não** entra em `itens`: descartar em silêncio é o falso verde que esta função existe para
    fechar. Para os marcadores que casam a forma, cada item vai até o próximo marcador casado ou o
    fim do texto; dentro dele, o primeiro `` ``` `` fechado é o comando, e o resto é vasculhado por
    `→`, `**Medido antes:**` e `**Aferição: manual**`. Elemento ausente vira `None` — a nomeação da
    falha é responsabilidade de quem chama."""
    falhas_forma: list[str] = []
    # (posição do marcador "N.", posição logo após a abertura ``` do bloco)
    heads: list[tuple[int, int]] = []
    for marcador in _ITEM_MARKER_RE.finditer(texto):
        num = marcador.group("num")
        abertura = _ABERTURA_BLOCO_RE.match(texto, marcador.end())
        if abertura is None:
            falhas_forma.append(
                f'item {num}: fora da forma da 8.1 (bloco cercado não vem logo após "{num}.")'
            )
            continue
        heads.append((marcador.start(), abertura.end()))

    itens: list[ItemVerificacao] = []
    for i, (_inicio, fim_abertura) in enumerate(heads):
        fim = heads[i + 1][0] if i + 1 < len(heads) else len(texto)
        bloco = texto[fim_abertura:fim]
        fechamento = bloco.find("```")
        if fechamento == -1:
            comando = None
            resto = ""
        else:
            comando = bloco[:fechamento].strip() or None
            resto = bloco[fechamento + 3 :]
        m_medido = _MEDIDO_ANTES_RE.search(resto)
        medido_antes = m_medido.group("valor").strip() if m_medido else None
        m_seta = _SETA_RE.search(resto)
        esperado = m_seta.group("esperado").strip() if m_seta else None
        afericao_manual = bool(_AFERICAO_MANUAL_RE.search(resto))
        itens.append(ItemVerificacao(i + 1, comando, esperado, medido_antes, afericao_manual))
    return itens, falhas_forma


def _validar_comando(comando: str) -> str | None:
    """`None` quando o comando é seguro para execução; senão, a razão da recusa. A recusa é
    **reportada, nunca executada** — chamado sempre antes de `_rodar_comando`. A decisão é por
    **token**, depois de `shlex.split`: recusa só quando um token **isolado** é operador de shell
    ou substituição de comando; o conteúdo de um argumento citado (ex.: `pwsh -Command "(… |
    Measure-Object).Count"`) não é varrido por metacaractere, porque `_rodar_comando` executa sem
    `shell=True` — o token citado inteiro nunca é interpretado por um shell."""
    try:
        tokens = shlex.split(comando)
    except ValueError as exc:
        return f"comando ilegível: {exc}"
    for tok in tokens:
        if tok in _TOKENS_SHELL_RECUSADOS or tok.startswith("$(") or tok.startswith("`"):
            return (
                f"token de shell isolado recusado ('{tok}') - operador de shell ou substituição "
                "de comando fora de argumento citado"
            )
    if not tokens or tokens[0] not in _COMANDOS_PERMITIDOS:
        return f"primeiro token fora da lista fechada {_COMANDOS_PERMITIDOS}"
    return None


def _rodar_comando(comando: str, root: Path) -> tuple[int, str]:
    tokens = shlex.split(comando)
    resultado = subprocess.run(
        tokens,
        cwd=str(root),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return resultado.returncode, (resultado.stdout or "") + (resultado.stderr or "")


def _bate_com_medido(valor_declarado: str, returncode: int, saida: str) -> bool:
    """`Medido antes: exit N` compara com o código de saída; qualquer outro valor é conferido
    como substring literal da saída (stdout + stderr) do comando rodado agora."""
    valor = valor_declarado.strip()
    m = _EXIT_RE.match(valor)
    if m:
        return returncode == int(m.group(1))
    return valor in saida


def verificar_tarefa(plano: Path, tarefa_id: str, root: Path) -> tuple[bool, list[str]]:
    """Verbo único da `LM-T5b`: `(ok, falhas)` — `ok` é `True` só quando todo item do bloco
    `Verificação` da tarefa tem os três elementos da forma normativa e o comando publicado, rodado
    agora, bate com o `Medido antes` declarado. `falhas` tem uma linha por item que não fechou,
    nomeando o elemento ausente ou o valor divergente."""
    plano_path = Path(plano)
    _exigir_plano(plano_path)

    rdo = _load_rdo(root)
    try:
        dossie = rdo.extrair_dossie(
            plano_path,
            tarefa_id,
            esquema_legado=False,
            modelo_legado=None,
            classe_legado=None,
        )
    except rdo.RdoValidationError as exc:
        raise CardCheckValidationError(str(exc)) from exc

    texto = dossie.campos.get("verificacao", "")
    itens, falhas_forma = _parsear_itens(texto)
    falhas: list[str] = list(falhas_forma)
    if not itens and not falhas_forma:
        falhas.append("verificacao: nenhum item reconhecido (comando em bloco cercado ausente)")

    for item in itens:
        motivo_recusa = _validar_comando(item.comando) if item.comando else None
        comando_executavel = item.comando is not None and motivo_recusa is None

        if item.afericao_manual and comando_executavel:
            falhas.append(
                f"item {item.indice}: marcador 'Aferição: manual' rejeitado - comando é "
                "executável (o marcador só vale sobre comando recusado ou ausente)"
            )
            continue

        if item.comando is None and not item.afericao_manual:
            falhas.append(f"item {item.indice}: elemento ausente - comando em bloco cercado")
            continue

        if item.esperado is None:
            falhas.append(f"item {item.indice}: elemento ausente - → (valor esperado)")
        if item.medido_antes is None:
            falhas.append(f"item {item.indice}: elemento ausente - Medido antes")
        if item.esperado is None or item.medido_antes is None:
            continue

        if item.afericao_manual:
            # aceito por (d): comando ausente ou recusado por (c) — reportado como manual, não
            # executado; os elementos 2 e 3 já foram conferidos acima.
            continue

        if motivo_recusa is not None:
            falhas.append(f"item {item.indice}: comando recusado - {motivo_recusa}")
            continue

        returncode, saida = _rodar_comando(item.comando, root)
        if not _bate_com_medido(item.medido_antes, returncode, saida):
            falhas.append(
                f"item {item.indice}: divergencia - Medido antes declara "
                f"'{item.medido_antes}', execução mediu exit {returncode} saída "
                f"'{saida.strip()[:200]}'"
            )

    return (not falhas, falhas)


def main(argv: list[str] | None = None) -> int:
    _forcar_utf8(sys.stdout)
    _forcar_utf8(sys.stderr)
    parser = argparse.ArgumentParser(
        description=(
            "Régua de autoria (LM-T5b): afere o bloco Verificação de um card contra a forma "
            "normativa de docs/RUBRICA_DE_REVISAO.md #8.1 e roda cada comando publicado contra "
            "a árvore de teste."
        )
    )
    parser.add_argument("--plano", required=True, type=Path, help="Caminho do .md do plano.")
    parser.add_argument("--tarefa", required=True, help="Identificador da tarefa (ex.: EX-T1).")
    parser.add_argument(
        "--root",
        type=Path,
        default=_default_root(),
        help="Raiz do repositório (onde os comandos publicados rodam).",
    )
    args = parser.parse_args(argv)

    try:
        ok, falhas = verificar_tarefa(args.plano, args.tarefa, args.root)
    except CardCheckValidationError as exc:
        print(f"card_check: FALHOU - {exc}", file=sys.stderr)
        return 1

    if not ok:
        for linha in falhas:
            print(linha, file=sys.stderr)
        print(
            f"card_check: FALHOU - {len(falhas)} item(ns) da tarefa '{args.tarefa}' não fecham.",
            file=sys.stderr,
        )
        return 1

    print(f"card_check: OK - tarefa '{args.tarefa}' fecha.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
