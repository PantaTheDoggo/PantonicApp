"""BKL-T2 (`docs/plans/P-0739-backlog-instrumento.md` `### BKL-T2`) — núcleo somente-leitura do
instrumento de backlog: carrega o índice do diário, os planos vivos e o próprio diário; monta o
grafo item → tarefas; `check` acusa cada violação de gramática (`C-1..C-9`, vocabulário fechado
definido no card) com `arquivo:linha`; `show` emite o dossiê verbatim de um item, truncado ao teto
`DB-7` (8.000 chars / 120 linhas, com ponteiro `arquivo:l1-l2` quando corta).

Gramática implementada (residência canônica: skill `diario-de-obras`, seção "Gramática legível
por máquina" — replicada aqui igual, `DB-17`/`DB-18`):

- plano: linha 1 `# P-NNNN — <título>`; nas 20 primeiras linhas `**Status:** \\`<estado>\\`` e
  `**Prefixo das tarefas no diário:** \\`<PFX>-T<n>\\``; opcional `**Ordem de execução:** ID → ID`.
- tarefa de plano: `### <ID> — <título> [<modelo>[ + dono] · classe <classe>[ · teto <n>]]`,
  `<ID>` = `(?:[A-Z0-9]+-)?T[0-9]+[a-z]?` (`DB-14`); ` + dono` e ` · teto <n>` são tolerados e
  ignorados, nunca violação (`DB-20`).
- tíquete: `## TK-<n> — <título>` (nível 2, sem bracket).
- subtarefa de tíquete: `### TK-<n><letra> — <título> [<modelo> · classe <classe>]`, dentro da
  seção do tíquete-pai — mesma gramática de bracket da tarefa de plano (`DB-17`).
- campos: 1º bullet `- **Status:** \\`<estado>\\` · AAAA-MM-DD[ · <razão>]`; opcional
  `- **Depende de:** ...`.
- índice: `| <ID> | <título> | <estado>[ <done>/<total>] | <âncora> |`.

`carregar` só lê `docs/DIARIO_DE_OBRAS.md` e `docs/plans/P-*.md` — nunca abre `*_HISTORICO.md`
nem `_INBOX.md` (fora de escopo desta tarefa; a migração e o `drain` são tarefas futuras do
plano). Superfície testável: `carregar`/`check`/`show` recebem `repo`/`modelo` já resolvidos e
nunca leem `sys.argv` — mesmo desenho de `uow.py`/`telemetria.py` (`DB-1`).

CLI: ``python .claude/tools/backlog.py check [--repo <caminho>]`` (exit 0 sem violação, 1 com
violação) e ``python .claude/tools/backlog.py show <ID> [--repo <caminho>]``. A CLI só embrulha
`check`/`show` — nenhuma regra vive aqui (`DB-1`).
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# --------------------------------------------------------------------------- #
# Vocabulário fechado (DB-3) e gramática de ID (DB-14)
# --------------------------------------------------------------------------- #

_VOCAB_BASE = {"triage", "ready", "blocked", "in-progress", "review", "done", "cancelled"}
_VOCAB_PLANO = _VOCAB_BASE | {"superseded"}
_VOCAB_ITEM = _VOCAB_BASE

_MODELOS = "Opus|Sonnet|Haiku"
_CLASSES = "mecanica|implementacao|comportamental|investigacao|redacao"
_BRACKET = rf"\[({_MODELOS})(?: \+ dono)? · classe ({_CLASSES})(?: · teto \d+)?\]"

PLANO_HEADER_RE = re.compile(r"^# (P-\d{4}) — (.+)$")
STATUS_CAMPO_RE = re.compile(r"\*\*Status:\*\* `([a-z-]+)`")
PREFIXO_CAMPO_RE = re.compile(r"\*\*Prefixo das tarefas no diário:\*\* `([A-Za-z0-9]+)-T<n>`")
ORDEM_CAMPO_RE = re.compile(r"\*\*Ordem de execução:\*\* (.+)$")

HEADING_RE = re.compile(r"^(#{2,3}) (\S+) — (.*)$")
TICKET_ID_ONLY_RE = re.compile(r"^TK-\d+[a-z]?$")
TASK_ID_ONLY_RE = re.compile(r"^(?:[A-Z0-9]+-)?T\d+[a-z]?$")

TIQUETE_HEADER_RE = re.compile(r"^## (TK-\d+) — (.+)$")
SUBTAREFA_HEADER_RE = re.compile(rf"^### (TK-\d+[a-z]) — (.+?) {_BRACKET}$")
TAREFA_HEADER_RE = re.compile(rf"^### ((?:[A-Z0-9]+-)?T\d+[a-z]?) — (.+?) {_BRACKET}$")

STATUS_BULLET_RE = re.compile(r"^- \*\*Status:\*\* `([a-z-]+)` · \d{4}-\d{2}-\d{2}(?: · (.+))?$")
DEPENDE_BULLET_RE = re.compile(r"^- \*\*Depende de:\*\* (.+)$")

INDICE_LINHA_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|$")

_TETO_CHARS = 8000
_TETO_LINHAS = 120


# --------------------------------------------------------------------------- #
# Modelo de dados
# --------------------------------------------------------------------------- #


@dataclass
class Violacao:
    codigo: str
    arquivo: str
    linha: int
    texto: str

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.codigo} {self.arquivo}:{self.linha} — {self.texto}"


@dataclass
class Item:
    id: str
    tipo: str  # "tarefa" | "tiquete" | "subtarefa"
    titulo: str
    arquivo: str
    linha_header: int
    linha_fim: int
    texto: str
    modelo: str | None = None
    classe: str | None = None
    header_valido: bool = True
    status: str | None = None
    status_linha: int | None = None
    status_razao: str | None = None
    depende_de: list[str] = field(default_factory=list)
    pai: str | None = None
    filhos: list["Item"] = field(default_factory=list)


@dataclass
class Plano:
    id: str
    titulo: str
    arquivo: str
    linha_header: int
    linha_fim: int
    texto: str
    status: str | None = None
    status_linha: int | None = None
    prefixo: str | None = None
    ordem_execucao: list[str] = field(default_factory=list)
    tarefas: list[Item] = field(default_factory=list)


@dataclass
class LinhaIndice:
    id: str
    titulo: str
    status_bruto: str
    arquivo: str
    linha: int


@dataclass
class Modelo:
    planos: list[Plano]
    tiquetes: list[Item]
    indice: list[LinhaIndice]
    diario_arquivo: str


# --------------------------------------------------------------------------- #
# Parser
# --------------------------------------------------------------------------- #


def _classify_item_heading(linha: str) -> tuple[str, str, bool] | None:
    """Classifica uma linha de heading (## ou ###) cujo ID casa DB-14.

    Devolve (tipo, id, header_valido) — `None` se a linha não é heading de item
    (heading administrativo do doc, ou o token após `#`s não é um ID de DB-14).
    """
    m = HEADING_RE.match(linha)
    if not m:
        return None
    nivel, id_token, resto = m.group(1), m.group(2), m.group(3)
    if len(nivel) == 2:
        if TICKET_ID_ONLY_RE.match(id_token) and not re.search(r"[a-z]$", id_token):
            valido = bool(TIQUETE_HEADER_RE.match(linha)) and "[" not in resto
            return ("tiquete", id_token, valido)
        return None
    # nivel == 3
    if TICKET_ID_ONLY_RE.match(id_token):
        valido = bool(SUBTAREFA_HEADER_RE.match(linha))
        return ("subtarefa", id_token, valido)
    if TASK_ID_ONLY_RE.match(id_token):
        valido = bool(TAREFA_HEADER_RE.match(linha))
        return ("tarefa", id_token, valido)
    return None


def _extrair_status(
    linhas: list[str], inicio_idx: int, fim_idx: int
) -> tuple[str | None, int | None, str | None]:
    """1º bullet não-branco após o heading. Se não for `- **Status:** ...`, o item não tem
    status (`C-2`), qualquer que seja o conteúdo."""
    for j in range(inicio_idx, fim_idx + 1):
        bruta = linhas[j]
        if bruta.strip() == "":
            continue
        m = STATUS_BULLET_RE.match(bruta)
        if m:
            return m.group(1), j + 1, m.group(2)
        return None, None, None
    return None, None, None


def _extrair_depende(linhas: list[str], inicio_idx: int, fim_idx: int) -> list[str]:
    for j in range(inicio_idx, fim_idx + 1):
        m = DEPENDE_BULLET_RE.match(linhas[j])
        if m:
            return re.findall(r"`([^`]+)`", m.group(1))
    return []


def _scan_items(linhas: list[str], arquivo_rel: str) -> list[Item]:
    heading_idxs = [i for i, l in enumerate(linhas) if HEADING_RE.match(l)]
    itens: list[Item] = []
    for pos, i in enumerate(heading_idxs):
        linha = linhas[i]
        classificado = _classify_item_heading(linha)
        if classificado is None:
            continue
        tipo, id_, valido = classificado
        m_generic = HEADING_RE.match(linha)
        resto = m_generic.group(3)
        titulo = resto.split(" [", 1)[0].strip()
        modelo_tok = classe_tok = None
        if valido:
            if tipo == "tarefa":
                mm = TAREFA_HEADER_RE.match(linha)
                titulo, modelo_tok, classe_tok = mm.group(2), mm.group(3), mm.group(4)
            elif tipo == "subtarefa":
                mm = SUBTAREFA_HEADER_RE.match(linha)
                titulo, modelo_tok, classe_tok = mm.group(2), mm.group(3), mm.group(4)
            elif tipo == "tiquete":
                mm = TIQUETE_HEADER_RE.match(linha)
                titulo = mm.group(2)

        fim_idx = heading_idxs[pos + 1] - 1 if pos + 1 < len(heading_idxs) else len(linhas) - 1
        linha_header = i + 1
        linha_fim = fim_idx + 1
        texto_secao = "\n".join(linhas[i : fim_idx + 1])

        status, status_linha, status_razao = _extrair_status(linhas, i + 1, fim_idx)
        depende_de = _extrair_depende(linhas, i + 1, fim_idx)

        itens.append(
            Item(
                id=id_,
                tipo=tipo,
                titulo=titulo,
                arquivo=arquivo_rel,
                linha_header=linha_header,
                linha_fim=linha_fim,
                texto=texto_secao,
                modelo=modelo_tok,
                classe=classe_tok,
                header_valido=valido,
                status=status,
                status_linha=status_linha,
                status_razao=status_razao,
                depende_de=depende_de,
            )
        )
    return itens


def _parse_indice(linhas: list[str], arquivo_rel: str) -> list[LinhaIndice]:
    resultado: list[LinhaIndice] = []
    for i, linha in enumerate(linhas, start=1):
        m = INDICE_LINHA_RE.match(linha)
        if not m:
            continue
        id_, titulo, status_bruto, ancora = m.groups()
        if id_ == "ID" or set(id_) <= {"-"}:
            continue
        if set(status_bruto) <= {"-"}:
            continue
        resultado.append(
            LinhaIndice(id=id_, titulo=titulo, status_bruto=status_bruto, arquivo=arquivo_rel, linha=i)
        )
    return resultado


def _parse_plano(caminho: Path, repo: Path) -> Plano:
    texto = caminho.read_text(encoding="utf-8")
    linhas = texto.splitlines()
    rel = caminho.relative_to(repo).as_posix()

    m0 = PLANO_HEADER_RE.match(linhas[0]) if linhas else None
    plano_id = m0.group(1) if m0 else caminho.stem
    titulo = m0.group(2) if m0 else caminho.stem

    status: str | None = None
    status_linha: int | None = None
    prefixo: str | None = None
    ordem: list[str] = []
    for i, linha in enumerate(linhas[:20], start=1):
        if linha.lstrip().startswith("-"):
            # bullet de item (ex.: "- **Status:** `done` · ..." de uma tarefa) — os campos
            # do próprio plano vêm em linha de parágrafo, nunca em bullet.
            continue
        if status is None:
            ms = STATUS_CAMPO_RE.search(linha)
            if ms:
                status, status_linha = ms.group(1), i
        if prefixo is None:
            mp = PREFIXO_CAMPO_RE.search(linha)
            if mp:
                prefixo = mp.group(1)
        if not ordem:
            mo = ORDEM_CAMPO_RE.search(linha)
            if mo:
                ordem = [tok.strip() for tok in mo.group(1).split("→")]

    tarefas = [it for it in _scan_items(linhas, rel) if it.tipo == "tarefa"]
    for tarefa in tarefas:
        tarefa.pai = plano_id

    return Plano(
        id=plano_id,
        titulo=titulo,
        arquivo=rel,
        linha_header=1,
        linha_fim=len(linhas),
        texto=texto,
        status=status,
        status_linha=status_linha,
        prefixo=prefixo,
        ordem_execucao=ordem,
        tarefas=tarefas,
    )


def _parse_diario(caminho: Path, repo: Path) -> tuple[list[LinhaIndice], list[Item]]:
    texto = caminho.read_text(encoding="utf-8")
    linhas = texto.splitlines()
    rel = caminho.relative_to(repo).as_posix()

    indice = _parse_indice(linhas, rel)
    itens_flat = _scan_items(linhas, rel)

    tiquetes: list[Item] = []
    atual: Item | None = None
    for item in itens_flat:
        if item.tipo == "tiquete":
            atual = item
            tiquetes.append(item)
        elif item.tipo == "subtarefa":
            if atual is not None:
                item.pai = atual.id
                atual.filhos.append(item)
            else:
                tiquetes.append(item)
    return indice, tiquetes


def carregar(repo: Path) -> Modelo:
    """Carrega índice + planos vivos + diário. Só abre `docs/DIARIO_DE_OBRAS.md` e
    `docs/plans/P-*.md` — nunca `*_HISTORICO.md` nem `_INBOX.md` (fora de escopo desta tarefa)."""
    diario_path = repo / "docs" / "DIARIO_DE_OBRAS.md"
    planos_dir = repo / "docs" / "plans"

    planos = [_parse_plano(caminho, repo) for caminho in sorted(planos_dir.glob("P-*.md"))]
    indice, tiquetes = _parse_diario(diario_path, repo)

    return Modelo(
        planos=planos,
        tiquetes=tiquetes,
        indice=indice,
        diario_arquivo=diario_path.relative_to(repo).as_posix(),
    )


# --------------------------------------------------------------------------- #
# check — violações C-1..C-9
# --------------------------------------------------------------------------- #


def _celula_indice(bruto: str) -> tuple[str, bool, str | None]:
    """Núcleo do valor, se a célula carrega narrativa (prosa/parênteses extras), e o
    sufixo <done>/<total> quando presente."""
    m = re.match(r"^([a-z-]+)(?: (\d+/\d+))?$", bruto)
    if m:
        return m.group(1), False, m.group(2)
    m2 = re.match(r"^([a-z-]+)(?: \d+/\d+)? \*\(.*\)\*.*$", bruto)
    if m2:
        return m2.group(1), True, None
    primeiro = bruto.split(" ", 1)[0]
    return primeiro, True, None


def _status_do_id(modelo: Modelo, id_: str) -> str | None:
    for plano in modelo.planos:
        if plano.id == id_:
            return plano.status
    for tiquete in modelo.tiquetes:
        if tiquete.id == id_:
            return tiquete.status
    return None


def _item_checks(item: Item, violacoes: list[Violacao]) -> None:
    if not item.header_valido:
        violacoes.append(
            Violacao("C-1", item.arquivo, item.linha_header, f"cabeçalho fora da gramática: {item.id}")
        )
        return  # header inválido já é o defeito; status do bracket não se avalia
    if item.status is None:
        violacoes.append(Violacao("C-2", item.arquivo, item.linha_header, f"{item.id} sem linha de Status"))
    elif item.status not in _VOCAB_ITEM:
        violacoes.append(
            Violacao(
                "C-3",
                item.arquivo,
                item.status_linha or item.linha_header,
                f"{item.id}: status '{item.status}' fora do vocabulário",
            )
        )


def check(modelo: Modelo) -> list[Violacao]:
    violacoes: list[Violacao] = []

    for plano in modelo.planos:
        terminal = plano.status in {"done", "superseded", "cancelled"}
        if not terminal:
            if plano.prefixo is None:
                violacoes.append(
                    Violacao(
                        "C-7", plano.arquivo, plano.linha_header, f"{plano.id} vivo sem Prefixo das tarefas no diário"
                    )
                )
            if plano.status is None:
                violacoes.append(
                    Violacao("C-8", plano.arquivo, plano.linha_header, f"{plano.id} vivo sem Status")
                )
        if plano.status is not None and plano.status not in _VOCAB_PLANO:
            violacoes.append(
                Violacao(
                    "C-3",
                    plano.arquivo,
                    plano.status_linha or plano.linha_header,
                    f"{plano.id}: status '{plano.status}' fora do vocabulário",
                )
            )

        for tarefa in plano.tarefas:
            _item_checks(tarefa, violacoes)

        em_progresso = [t for t in plano.tarefas if t.status == "in-progress"]
        if len(em_progresso) > 1:
            segunda = em_progresso[1]
            violacoes.append(
                Violacao(
                    "C-6",
                    segunda.arquivo,
                    segunda.status_linha or segunda.linha_header,
                    f"duas tarefas in-progress em {plano.id}",
                )
            )

    for tiquete in modelo.tiquetes:
        _item_checks(tiquete, violacoes)
        for sub in tiquete.filhos:
            _item_checks(sub, violacoes)

        em_progresso = [x for x in [tiquete, *tiquete.filhos] if x.status == "in-progress"]
        if len(em_progresso) > 1:
            segunda = em_progresso[1]
            violacoes.append(
                Violacao(
                    "C-6",
                    segunda.arquivo,
                    segunda.status_linha or segunda.linha_header,
                    f"duas linhas in-progress em {tiquete.id}",
                )
            )

    ids_planos = {p.id for p in modelo.planos}
    ids_tiquetes = {t.id for t in modelo.tiquetes}
    for linha in modelo.indice:
        nucleo, tem_narrativa, _done_total = _celula_indice(linha.status_bruto)
        if nucleo not in _VOCAB_PLANO:
            violacoes.append(
                Violacao(
                    "C-3", linha.arquivo, linha.linha, f"{linha.id}: status de índice '{nucleo}' fora do vocabulário"
                )
            )
        elif tem_narrativa:
            violacoes.append(Violacao("C-4", linha.arquivo, linha.linha, f"{linha.id}: célula do índice com prosa"))
        else:
            item_status = _status_do_id(modelo, linha.id)
            if item_status is not None and item_status != nucleo:
                violacoes.append(
                    Violacao(
                        "C-5",
                        linha.arquivo,
                        linha.linha,
                        f"{linha.id}: índice '{nucleo}' diverge do campo '{item_status}'",
                    )
                )

        if nucleo not in {"done", "superseded"} and linha.id not in ids_planos and linha.id not in ids_tiquetes:
            violacoes.append(
                Violacao("C-9", linha.arquivo, linha.linha, f"{linha.id}: sem residência em plano vivo nem diário")
            )

    return violacoes


# --------------------------------------------------------------------------- #
# show — dossiê verbatim, teto DB-7
# --------------------------------------------------------------------------- #


def _localizar(modelo: Modelo, id_: str) -> Plano | Item | None:
    for plano in modelo.planos:
        if plano.id == id_:
            return plano
        for tarefa in plano.tarefas:
            if tarefa.id == id_:
                return tarefa
    for tiquete in modelo.tiquetes:
        if tiquete.id == id_:
            return tiquete
        for sub in tiquete.filhos:
            if sub.id == id_:
                return sub
    return None


def _truncar(texto: str, arquivo: str, linha_header: int, linha_fim: int) -> str:
    linhas = texto.splitlines()
    if len(texto) <= _TETO_CHARS and len(linhas) <= _TETO_LINHAS:
        return texto
    limite = min(len(linhas), _TETO_LINHAS)
    cortado = "\n".join(linhas[:limite])
    while len(cortado) > _TETO_CHARS and limite > 0:
        limite -= 1
        cortado = "\n".join(linhas[:limite])
    return cortado + f"\n… truncado ({arquivo}:{linha_header}-{linha_fim})"


def show(modelo: Modelo, id_: str) -> str:
    alvo = _localizar(modelo, id_)
    if alvo is None:
        return f"id não encontrado: {id_}"
    return _truncar(alvo.texto, alvo.arquivo, alvo.linha_header, alvo.linha_fim)


# --------------------------------------------------------------------------- #
# CLI — só embrulha (DB-1)
# --------------------------------------------------------------------------- #


def resolve_repo(repo_arg: str | None) -> Path:
    if repo_arg:
        return Path(repo_arg).resolve()
    return Path(__file__).resolve().parent.parent.parent


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="backlog.py", description="Núcleo somente-leitura do backlog: check e show."
    )
    subparsers = parser.add_subparsers(dest="comando", required=True)

    check_parser = subparsers.add_parser("check", help="Lint da gramática do diário/planos.")
    check_parser.add_argument("--repo", default=None)

    show_parser = subparsers.add_parser("show", help="Dossiê verbatim de um item.")
    show_parser.add_argument("id")
    show_parser.add_argument("--repo", default=None)

    args = parser.parse_args(argv)

    for fluxo in (sys.stdout, sys.stderr):
        if hasattr(fluxo, "reconfigure"):
            fluxo.reconfigure(encoding="utf-8")

    repo = resolve_repo(args.repo)
    modelo = carregar(repo)

    if args.comando == "check":
        violacoes = check(modelo)
        for violacao in violacoes:
            print(str(violacao))
        if violacoes:
            print(f"\n{len(violacoes)} violação(ões) encontrada(s).", file=sys.stderr)
            return 1
        print("check: OK — nenhuma violação.")
        return 0

    if args.comando == "show":
        print(show(modelo, args.id))
        return 0

    parser.error(f"comando desconhecido: {args.comando}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
