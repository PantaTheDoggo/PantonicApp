"""BKL-T2 (`docs/plans/P-0739-backlog-instrumento.md` `### BKL-T2`) — núcleo somente-leitura do
instrumento de backlog: carrega o índice do diário, os planos vivos e o próprio diário; monta o
grafo item → tarefas; `check` acusa cada violação de gramática (`C-1..C-9`, vocabulário fechado
definido no card) com `arquivo:linha`; `show` emite o dossiê verbatim de um item, truncado ao teto
`DB-7` (8.000 chars / 120 linhas, com ponteiro `arquivo:l1-l2` quando corta).

Gramática implementada (residência canônica: skill `diario-de-obras`, seção "Gramática legível
por máquina" — replicada aqui igual, `DB-17`/`DB-18`):

- plano: linha 1 `# P-NNNN — <título>`; nas 20 primeiras linhas `**Status:** \\`<estado>\\`` e
  `**Prefixo das tarefas no diário:** \\`<PFX>-T<n>\\``; opcional `**Ordem de execução:** ID → ID`.
- tarefa de plano: `### <ID> — <título> [<modelo>[ + dono][ · esforço <esforço>] · classe <classe>[ · teto <n>]]`,
  `<ID>` = `(?:[A-Z0-9]+-)?T[0-9]+[a-z]?` (`DB-14`); ` + dono` e ` · teto <n>` são tolerados e
  ignorados, nunca violação (`DB-20`).
- tíquete: `## TK-<n> — <título>` (nível 2, sem bracket).
- subtarefa de tíquete: `### TK-<n><letra> — <título> [<modelo>[ · esforço <esforço>] · classe <classe>]`, dentro da
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
import datetime
import os
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
_ESFORCOS = "low|medium|high|xhigh|max"
_BRACKET = (
    rf"\[({_MODELOS})(?: \+ dono)?(?: · esforço (?:{_ESFORCOS}))?"
    rf" · classe ({_CLASSES})(?: · teto \d+)?\]"
)

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
TIPO_BULLET_RE = re.compile(r"^- \*\*Tipo:\*\* (.+)$")
NOTAS_BULLET_RE = re.compile(r"^- \*\*Notas de execução:\*\*\s*$")
DIRETIVA_RE = re.compile(r"^\*\*Diretiva de priorização:\*\* (.*)$")
NIVEL_1_OU_2_RE = re.compile(r"^#{1,2} ")

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
    campo_tipo: str | None = None
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
    ancora: str = ""


@dataclass
class Modelo:
    planos: list[Plano]
    tiquetes: list[Item]
    indice: list[LinhaIndice]
    diario_arquivo: str
    diario_linhas: list[str] = field(default_factory=list)
    diretiva_ids: list[str] = field(default_factory=list)


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


def _extrair_tipo(linhas: list[str], inicio_idx: int, fim_idx: int) -> str | None:
    for j in range(inicio_idx, fim_idx + 1):
        m = TIPO_BULLET_RE.match(linhas[j])
        if m:
            return m.group(1).strip()
    return None


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
        campo_tipo = _extrair_tipo(linhas, i + 1, fim_idx)

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
                campo_tipo=campo_tipo,
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
            LinhaIndice(
                id=id_, titulo=titulo, status_bruto=status_bruto, arquivo=arquivo_rel, linha=i, ancora=ancora
            )
        )
    return resultado


def _parse_diretiva(linhas: list[str]) -> list[str]:
    for linha in linhas:
        m = DIRETIVA_RE.match(linha)
        if m:
            parte_ids = m.group(1).split(" — ", 1)[0]
            return re.findall(r"`([^`]+)`", parte_ids)
    return []


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


def _parse_diario(caminho: Path, repo: Path) -> tuple[list[LinhaIndice], list[Item], list[str]]:
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
    return indice, tiquetes, linhas


def carregar(repo: Path) -> Modelo:
    """Carrega índice + planos vivos + diário. Só abre `docs/DIARIO_DE_OBRAS.md` e
    `docs/plans/P-*.md` — nunca `*_HISTORICO.md` nem `_INBOX.md` (fora de escopo desta tarefa)."""
    diario_path = repo / "docs" / "DIARIO_DE_OBRAS.md"
    planos_dir = repo / "docs" / "plans"

    planos = [_parse_plano(caminho, repo) for caminho in sorted(planos_dir.glob("P-*.md"))]
    indice, tiquetes, diario_linhas = _parse_diario(diario_path, repo)
    diretiva_ids = _parse_diretiva(diario_linhas)

    return Modelo(
        planos=planos,
        tiquetes=tiquetes,
        indice=indice,
        diario_arquivo=diario_path.relative_to(repo).as_posix(),
        diario_linhas=diario_linhas,
        diretiva_ids=diretiva_ids,
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
        for tarefa in plano.tarefas:
            if tarefa.id == id_:
                return tarefa.status
    for tiquete in modelo.tiquetes:
        if tiquete.id == id_:
            return tiquete.status
        for sub in tiquete.filhos:
            if sub.id == id_:
                return sub.status
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
# next — seleção determinística (BKL-T3, §2.5/§2.6 de
# docs/plans/P-0739-backlog-instrumento.md). Somente-leitura (DB-5): nenhuma função
# desta seção escreve em arquivo do repositório.
# --------------------------------------------------------------------------- #


@dataclass
class Candidato:
    item: Item
    pai: Plano | Item
    tipo_pai: str  # "plano" | "tiquete"


@dataclass
class SelecaoNext:
    exit_code: int
    vencedor: Candidato | None
    mensagem: str | None = None


def _candidatos(modelo: Modelo) -> list[Candidato]:
    resultado: list[Candidato] = []
    for plano in modelo.planos:
        for tarefa in plano.tarefas:
            resultado.append(Candidato(item=tarefa, pai=plano, tipo_pai="plano"))
    for tiquete in modelo.tiquetes:
        for sub in tiquete.filhos:
            resultado.append(Candidato(item=sub, pai=tiquete, tipo_pai="tiquete"))
    return resultado


def _aplicar_diretiva(modelo: Modelo, candidatos: list[Candidato]) -> list[Candidato]:
    if not modelo.diretiva_ids:
        return candidatos
    ids = set(modelo.diretiva_ids)
    return [c for c in candidatos if c.item.id in ids or c.pai.id in ids]


def _posicao_indice(modelo: Modelo, pai_id: str) -> int | None:
    for pos, linha in enumerate(modelo.indice):
        if linha.id == pai_id:
            return pos
    return None


def _irmaos_ordenados(pai: Plano | Item, tipo_pai: str) -> list[Item]:
    filhos = pai.tarefas if tipo_pai == "plano" else pai.filhos
    ordem = pai.ordem_execucao if tipo_pai == "plano" else []
    if not ordem:
        return list(filhos)
    posicao_original = {id(f): idx for idx, f in enumerate(filhos)}

    def chave(item: Item) -> tuple[int, int]:
        if item.id in ordem:
            return (0, ordem.index(item.id))
        return (1, posicao_original[id(item)])

    return sorted(filhos, key=chave)


def _ordem_interna(c: Candidato) -> int:
    irmaos = _irmaos_ordenados(c.pai, c.tipo_pai)
    for idx, irmao in enumerate(irmaos):
        if irmao is c.item:
            return idx
    return len(irmaos)


def _eh_bug(c: Candidato) -> bool:
    if c.item.campo_tipo == "bug":
        return True
    if c.tipo_pai == "tiquete" and c.pai.campo_tipo == "bug":
        return True
    return False


def _tier(c: Candidato) -> int:
    if c.tipo_pai == "plano" and c.item.tipo == "tarefa" and c.pai.status == "in-progress":
        return 0
    if _eh_bug(c):
        return 1
    return 2


def _mensagem_e2(pares: list[tuple["Plano | Item", "Plano | Item"]]) -> str | None:
    """E-2 (DB-37, DB-40) — item ou pai sem a linha de `Status` recusa a seleção/transição.

    `pares` é a lista de (item, pai) sob avaliação; a mensagem cobre a união dos dois
    papéis, um `<ID>` distinto por vez, em ordem alfabética crescente, separados por
    `, `. Residência única do cálculo de E-2 — `next`, `status` e `start` reusam esta
    função, nenhum a reescreve (`DB-40`)."""
    ids = sorted({obj.id for item, pai in pares for obj in (item, pai) if obj.status is None})
    if not ids:
        return None
    return ", ".join(f"linha de status ausente para {id_}" for id_ in ids)


def _eh_elegivel(modelo: Modelo, c: Candidato) -> bool:
    """§2.5 item 3 — elegibilidade de um candidato."""
    return (
        c.item.status == "ready"
        and c.pai.status in ("ready", "in-progress")
        and (not c.item.depende_de or all(_status_do_id(modelo, d) == "done" for d in c.item.depende_de))
    )


def selecionar_next(modelo: Modelo) -> SelecaoNext:
    """§2.5 — ordem total de seleção. Somente-leitura: só lê `modelo`."""
    candidatos = _aplicar_diretiva(modelo, _candidatos(modelo))

    mensagem_e2 = _mensagem_e2([(c.item, c.pai) for c in candidatos])
    if mensagem_e2 is not None:
        return SelecaoNext(3, None, mensagem_e2)

    em_progresso = [c for c in candidatos if c.item.status == "in-progress"]
    if len(em_progresso) == 1:
        vencedor = em_progresso[0]
        if _posicao_indice(modelo, vencedor.pai.id) is None:
            return SelecaoNext(3, None, f"linha de índice ausente para {vencedor.pai.id}")
        return SelecaoNext(0, vencedor, None)
    if len(em_progresso) >= 2:
        ids = ", ".join(sorted(c.item.id for c in em_progresso))
        return SelecaoNext(3, None, f"dois ou mais itens in-progress: {ids}")

    elegiveis = [c for c in candidatos if _eh_elegivel(modelo, c)]

    if not elegiveis:
        n_blocked = sum(1 for c in candidatos if c.item.status == "blocked")
        return SelecaoNext(2, None, f"nada delegável — 0 elegível(is) · blocked {n_blocked}")

    posicoes: dict[str, int] = {}
    for c in elegiveis:
        if c.pai.id not in posicoes:
            pos = _posicao_indice(modelo, c.pai.id)
            if pos is None:
                return SelecaoNext(3, None, f"linha de índice ausente para {c.pai.id}")
            posicoes[c.pai.id] = pos

    ordenados = sorted(elegiveis, key=lambda c: (_tier(c), posicoes[c.pai.id], _ordem_interna(c)))
    return SelecaoNext(0, ordenados[0], None)


def _done_total(filhos: list[Item]) -> tuple[int, int]:
    """DB-36 — <total> = filhos diretos não `cancelled`; <done> = destes, os `done`."""
    vivos = [f for f in filhos if f.status != "cancelled"]
    total = len(vivos)
    done = sum(1 for f in vivos if f.status == "done")
    return done, total


def _residencia_plano(plano: Plano) -> str:
    return f"{plano.arquivo}:1-{plano.linha_fim}"


def _residencia_tiquete(modelo: Modelo, tiquete: Item) -> str:
    linhas = modelo.diario_linhas
    fim = len(linhas)
    for idx in range(tiquete.linha_header, len(linhas)):
        if NIVEL_1_OU_2_RE.match(linhas[idx]):
            fim = idx
            break
    return f"{modelo.diario_arquivo}:{tiquete.linha_header}-{fim}"


def _indice_ancora(modelo: Modelo, pai_id: str) -> str:
    for linha in modelo.indice:
        if linha.id == pai_id:
            return linha.ancora
    return ""


def _antecessora(pai: Plano | Item, tipo_pai: str, vencedor_item: Item) -> Item | None:
    irmaos = _irmaos_ordenados(pai, tipo_pai)
    idx = next((i for i, x in enumerate(irmaos) if x is vencedor_item), None)
    if idx is None or idx == 0:
        return None
    return irmaos[idx - 1]


def _range_notas(item: Item) -> tuple[int, int] | None:
    linhas = item.texto.splitlines()
    inicio: int | None = None
    fim: int | None = None
    for idx, linha in enumerate(linhas):
        if inicio is None:
            if NOTAS_BULLET_RE.match(linha):
                inicio = idx
                fim = idx
            continue
        if linha.startswith("  -") or linha.startswith("\t-"):
            fim = idx
            continue
        break
    if inicio is None:
        return None
    return (item.linha_header + inicio, item.linha_header + (fim or inicio))


def _listar_blocked(modelo: Modelo) -> str:
    todos: list[Item] = []
    for plano in modelo.planos:
        todos.extend(plano.tarefas)
    for tiquete in modelo.tiquetes:
        todos.extend(tiquete.filhos)
    bloqueados = [it for it in todos if it.status == "blocked"]
    if not bloqueados:
        return "nenhum"
    partes = [f"{it.id} ({it.status_razao or 'sem razão'})" for it in bloqueados]
    return ", ".join(partes)


_CAMINHO_PLANO_INBOX_RE = re.compile(r"docs/plans/P-\d{4}-[^)\s`]+\.md")


def _contar_inbox_planos(caminho: Path) -> int:
    """DB-38 — conta as linhas de `docs/plans/_INBOX.md` que começam com `- `, contêm um
    caminho que casa `docs/plans/P-[0-9]{4}-<slug>.md` e não começam com `- [drenado `."""
    if not caminho.exists():
        return 0
    linhas = caminho.read_text(encoding="utf-8").splitlines()
    n = 0
    for linha in linhas:
        s = linha.strip()
        if not s.startswith("- "):
            continue
        if s.startswith("- [drenado "):
            continue
        if not _CAMINHO_PLANO_INBOX_RE.search(s):
            continue
        n += 1
    return n


def _contar_inbox_memoria(caminho: Path) -> int:
    """`GOVERNANCA_MEMORIAS.md` §8 — linha de candidato permanece até ser marcada
    `[promovido]` ou `[descartado — motivo]`; enquanto isso, é uma linha "não marcada"."""
    if not caminho.exists():
        return 0
    linhas = caminho.read_text(encoding="utf-8").splitlines()
    n = 0
    for linha in linhas:
        s = linha.strip()
        if not s.startswith("- "):
            continue
        if "[promovido]" in s or "[descartado" in s:
            continue
        n += 1
    return n


def renderizar_next(
    modelo: Modelo,
    selecao: SelecaoNext,
    memoria_inbox: Path | None = None,
    inbox_planos: Path | None = None,
) -> str:
    """§2.6 — forma fixa da saída de `next` para `selecao.exit_code == 0`."""
    candidato = selecao.vencedor
    assert candidato is not None
    item = candidato.item
    pai = candidato.pai
    tipo_pai = candidato.tipo_pai

    bracket = f"[{item.modelo} · classe {item.classe}]"
    linhas_saida = [f"=== PRÓXIMA TAREFA: {item.id} — {item.titulo} {bracket}"]

    if tipo_pai == "plano":
        done, total = _done_total(pai.tarefas)
        residencia = _residencia_plano(pai)
        ancora = _indice_ancora(modelo, pai.id)
        linhas_saida.append(
            f"plano: {pai.id} — {pai.titulo} ({done}/{total}) · residência: {residencia} · índice: {ancora}"
        )
    else:
        done, total = _done_total(pai.filhos)
        residencia = _residencia_tiquete(modelo, pai)
        ancora = _indice_ancora(modelo, pai.id)
        linhas_saida.append(
            f"tíquete: {pai.id} — {pai.titulo} ({done}/{total}) · residência: {residencia} · índice: {ancora}"
        )

    antecessora_item = _antecessora(pai, tipo_pai, item)
    if antecessora_item is not None:
        notas = _range_notas(antecessora_item)
        if notas is None:
            linhas_saida.append(f"antecessora: {antecessora_item.id} ({antecessora_item.status}; sem notas)")
        else:
            l1, l2 = notas
            linhas_saida.append(
                f"antecessora: {antecessora_item.id} "
                f"({antecessora_item.status}; notas em {antecessora_item.arquivo}:{l1}-{l2})"
            )

    linhas_saida.append("--- dossiê (verbatim, teto DB-7) ---")
    linhas_saida.append(_truncar(item.texto, item.arquivo, item.linha_header, item.linha_fim))
    linhas_saida.append("--- pendências mecânicas ---")

    n_inbox_planos = _contar_inbox_planos(inbox_planos) if inbox_planos is not None else 0
    n_memoria = _contar_inbox_memoria(memoria_inbox) if memoria_inbox is not None else 0
    blocked = _listar_blocked(modelo)
    linhas_saida.append(
        f"inbox de planos: {n_inbox_planos} por drenar · fila de memória: {n_memoria} candidato(s) · "
        f"blocked: {blocked}"
    )

    return "\n".join(linhas_saida)


# --------------------------------------------------------------------------- #
# status / start / diretiva — transição e projeções (BKL-T4, §2.7 e §3 de
# docs/plans/P-0739-backlog-instrumento.md). As funções recebem `repo`/`modelo` e
# caminhos já resolvidos por parâmetro e nunca leem `sys.argv` (DB-1).
# --------------------------------------------------------------------------- #

_TRANSICOES: dict[tuple[str, str], bool] = {
    ("triage", "ready"): True,
    ("triage", "cancelled"): True,
    ("ready", "in-progress"): True,
    ("ready", "blocked"): True,
    ("ready", "cancelled"): True,
    ("blocked", "ready"): True,
    ("blocked", "cancelled"): True,
    ("in-progress", "review"): True,
    ("in-progress", "blocked"): True,
    ("review", "done"): True,
    ("review", "in-progress"): True,
    ("review", "blocked"): True,
}


@dataclass
class ResultadoStatus:
    exit_code: int
    mensagem: str | None = None
    arquivos: list[str] = field(default_factory=list)


def _pai_do_alvo(modelo: Modelo, alvo: "Plano | Item") -> tuple["Plano | Item", str]:
    """Pai para as projeções de `<done>/<total>` e do bloco `Fila corrente` (DB-36,
    DB-33): plano e tiquete são pai de si mesmos; tarefa é filha do plano `alvo.pai`;
    subtarefa é filha do tiquete `alvo.pai`."""
    if isinstance(alvo, Plano):
        return alvo, "plano"
    if alvo.tipo == "tiquete":
        return alvo, "tiquete"
    if alvo.tipo == "tarefa":
        for plano in modelo.planos:
            if plano.id == alvo.pai:
                return plano, "plano"
    if alvo.tipo == "subtarefa":
        for tiquete in modelo.tiquetes:
            if tiquete.id == alvo.pai:
                return tiquete, "tiquete"
    raise ValueError(f"pai não localizado para {alvo.id}")


def _proxima_do_pai(modelo: Modelo, pai: "Plano | Item", tipo_pai: str) -> str | None:
    filhos = pai.tarefas if tipo_pai == "plano" else pai.filhos
    candidatos_pai = [Candidato(item=f, pai=pai, tipo_pai=tipo_pai) for f in filhos]
    elegiveis = [c for c in candidatos_pai if _eh_elegivel(modelo, c)]
    if not elegiveis:
        return None
    ordenados = sorted(elegiveis, key=lambda c: (_tier(c), _ordem_interna(c)))
    return ordenados[0].item.id


def _bloco_fila_corrente(modelo: Modelo) -> list[str]:
    """§2.3 (DB-33) — um bullet por pai vivo, na ordem das linhas do índice."""
    linhas: list[str] = []
    for linha_idx in modelo.indice:
        alvo: "Plano | Item | None" = None
        tipo = "plano"
        for plano in modelo.planos:
            if plano.id == linha_idx.id:
                alvo, tipo = plano, "plano"
                break
        if alvo is None:
            for tiquete in modelo.tiquetes:
                if tiquete.id == linha_idx.id:
                    alvo, tipo = tiquete, "tiquete"
                    break
        if alvo is None:
            continue
        filhos = alvo.tarefas if tipo == "plano" else alvo.filhos
        if not any(f.status not in ("done", "cancelled") for f in filhos):
            continue
        done, total = _done_total(filhos)
        proxima = _proxima_do_pai(modelo, alvo, tipo)
        proxima_txt = f"próxima `{proxima}`" if proxima else "próxima —"
        linhas.append(f"- `{alvo.id}` (`{alvo.status}`, {done}/{total}): {proxima_txt}")
    return linhas


def _escrever_atomico(caminho: Path, linhas: list[str]) -> None:
    """DB-1 — temp no mesmo diretório + `os.replace`, num ato só."""
    texto = "\n".join(linhas) + "\n"
    tmp = caminho.with_name(caminho.name + ".tmp")
    tmp.write_text(texto, encoding="utf-8")
    os.replace(tmp, caminho)


def _inserir_nota(linhas: list[str], alvo: Item, linha_nota: str) -> None:
    faixa = _range_notas(alvo)
    if faixa is not None:
        _, fim_linha = faixa
        linhas.insert(fim_linha, linha_nota)
        return
    pos_insercao = alvo.linha_fim
    while pos_insercao > alvo.linha_header and linhas[pos_insercao - 1].strip() == "":
        pos_insercao -= 1
    linhas[pos_insercao:pos_insercao] = ["- **Notas de execução:**", linha_nota]


def transacionar_status(
    repo: Path,
    modelo: Modelo,
    id_: str,
    estado: str,
    razao: str | None = None,
    nota: str | None = None,
) -> ResultadoStatus:
    """§2.7 + §3 — `status`/`start`: transição e escrita atômica das projeções, num ato
    só. Nenhuma escrita ocorre antes de todas as checagens (E-2, E-3, tabela de §2.7,
    `blocked` exige `--razao`) passarem."""
    alvo = _localizar(modelo, id_)
    if alvo is None:
        return ResultadoStatus(1, f"id não encontrado: {id_}")

    pai, tipo_pai = _pai_do_alvo(modelo, alvo)

    mensagem_e2 = _mensagem_e2([(alvo, pai)])
    if mensagem_e2 is not None:
        return ResultadoStatus(3, mensagem_e2)

    if _posicao_indice(modelo, pai.id) is None:
        return ResultadoStatus(3, f"linha de índice ausente para {pai.id}")

    atual = alvo.status
    if (atual, estado) not in _TRANSICOES:
        return ResultadoStatus(1, f"transição fora da tabela de §2.7: {atual} → {estado} para {id_}")

    if estado == "blocked" and not razao:
        return ResultadoStatus(1, "blocked exige --razao")

    if estado == "in-progress" and pai is not alvo:
        irmaos = pai.tarefas if tipo_pai == "plano" else pai.filhos
        if any(irmao is not alvo and irmao.status == "in-progress" for irmao in irmaos):
            return ResultadoStatus(1, f"já há item in-progress no mesmo pai: {pai.id}")

    # Checagens concluídas — nenhum arquivo tocado até aqui. Muta o modelo em memória
    # (mesmos objetos referenciados por `pai.tarefas`/`pai.filhos`) para que done/total,
    # "próxima" e o bloco `Fila corrente` já reflitam a transição.
    hoje = datetime.date.today().isoformat()
    alvo.status = estado
    alvo.status_razao = razao

    plano_arquivo = alvo.arquivo if (isinstance(alvo, Plano) or alvo.tipo == "tarefa") else None
    plano_linhas = (repo / plano_arquivo).read_text(encoding="utf-8").splitlines() if plano_arquivo else None
    diario_linhas = list(modelo.diario_linhas)

    if isinstance(alvo, Plano):
        idx = alvo.status_linha - 1
        plano_linhas[idx] = STATUS_CAMPO_RE.sub(f"**Status:** `{estado}`", plano_linhas[idx], count=1)
    else:
        sufixo = f" · {razao}" if razao else ""
        nova_linha = f"- **Status:** `{estado}` · {hoje}{sufixo}"
        if alvo.tipo == "tarefa":
            plano_linhas[alvo.status_linha - 1] = nova_linha
        else:
            diario_linhas[alvo.status_linha - 1] = nova_linha

    linha_indice_pai = next(l for l in modelo.indice if l.id == pai.id)
    done, total = _done_total(pai.tarefas if tipo_pai == "plano" else pai.filhos)
    novo_status_bruto = f"{pai.status} {done}/{total}" if total else pai.status
    diario_linhas[linha_indice_pai.linha - 1] = (
        f"| {linha_indice_pai.id} | {linha_indice_pai.titulo} | {novo_status_bruto} | {linha_indice_pai.ancora} |"
    )

    if nota is not None and isinstance(alvo, Item):
        linha_nota = f"  - {hoje} `{estado}` — {nota}"
        _inserir_nota(plano_linhas if alvo.tipo == "tarefa" else diario_linhas, alvo, linha_nota)

    ini = diario_linhas.index("<!-- fila:gerada -->")
    fim = diario_linhas.index("<!-- /fila:gerada -->", ini)
    diario_linhas[ini + 1 : fim] = _bloco_fila_corrente(modelo)

    arquivos_tocados = [modelo.diario_arquivo]
    _escrever_atomico(repo / modelo.diario_arquivo, diario_linhas)
    if plano_arquivo is not None:
        _escrever_atomico(repo / plano_arquivo, plano_linhas)
        arquivos_tocados.append(plano_arquivo)

    return ResultadoStatus(0, None, sorted(set(arquivos_tocados)))


def transacionar_diretiva(repo: Path, modelo: Modelo, texto: str) -> ResultadoStatus:
    """§3 — `diretiva`: reescreve a linha `**Diretiva de priorização:**`."""
    diario_linhas = list(modelo.diario_linhas)
    nova_linha = f"**Diretiva de priorização:** {texto}"
    for i, linha in enumerate(diario_linhas):
        if DIRETIVA_RE.match(linha):
            diario_linhas[i] = nova_linha
            break
    else:
        diario_linhas.insert(1, nova_linha)
    _escrever_atomico(repo / modelo.diario_arquivo, diario_linhas)
    return ResultadoStatus(0, None, [modelo.diario_arquivo])


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

    next_parser = subparsers.add_parser("next", help="Seleção determinística da próxima tarefa.")
    next_parser.add_argument("--repo", default=None)
    next_parser.add_argument("--memoria-inbox", default=None)
    next_parser.add_argument("--inbox-planos", default=None)

    status_parser = subparsers.add_parser("status", help="Transição de status + projeções atômicas.")
    status_parser.add_argument("id")
    status_parser.add_argument("estado")
    status_parser.add_argument("--razao", default=None)
    status_parser.add_argument("--nota", default=None)
    status_parser.add_argument("--repo", default=None)

    start_parser = subparsers.add_parser("start", help="= status <ID> in-progress.")
    start_parser.add_argument("id")
    start_parser.add_argument("--repo", default=None)

    diretiva_parser = subparsers.add_parser("diretiva", help="Reescreve a linha de diretiva de priorização.")
    diretiva_parser.add_argument("texto")
    diretiva_parser.add_argument("--repo", default=None)

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

    if args.comando == "next":
        selecao = selecionar_next(modelo)
        if selecao.exit_code == 0:
            memoria_inbox = Path(args.memoria_inbox).resolve() if args.memoria_inbox else None
            inbox_planos = (
                Path(args.inbox_planos).resolve() if args.inbox_planos else repo / "docs" / "plans" / "_INBOX.md"
            )
            print(renderizar_next(modelo, selecao, memoria_inbox=memoria_inbox, inbox_planos=inbox_planos))
            return 0
        print(selecao.mensagem, file=sys.stderr if selecao.exit_code == 3 else sys.stdout)
        return selecao.exit_code

    if args.comando in ("status", "start"):
        estado = args.estado if args.comando == "status" else "in-progress"
        razao = args.razao if args.comando == "status" else None
        nota = args.nota if args.comando == "status" else None
        resultado = transacionar_status(repo, modelo, args.id, estado, razao=razao, nota=nota)
        if resultado.exit_code == 0:
            print(f"{args.comando}: {args.id} → {estado}. arquivos tocados: {', '.join(resultado.arquivos)}")
            return 0
        print(resultado.mensagem, file=sys.stderr if resultado.exit_code == 3 else sys.stdout)
        return resultado.exit_code

    if args.comando == "diretiva":
        resultado = transacionar_diretiva(repo, modelo, args.texto)
        print(f"diretiva atualizada. arquivos tocados: {', '.join(resultado.arquivos)}")
        return 0

    parser.error(f"comando desconhecido: {args.comando}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
