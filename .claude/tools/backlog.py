"""BKL-T2 (`docs/plans/P-0739-backlog-instrumento.md` `### BKL-T2`) — núcleo somente-leitura do
instrumento de backlog: carrega o índice do diário, os planos vivos e o próprio diário; monta o
grafo item → tarefas; `check` acusa cada violação de gramática (`C-1..C-17`, vocabulário fechado
definido no card) com `arquivo:linha`; `resolver_citacao_secao` (`TK-60a`) resolve uma citação
`` `<arquivo>.md` §<N>[.<N>]* `` contra o arquivo citado, acusando `C-11` quando a seção não
existe; `C-12` (`TK-65a`) acusa `Depende de:` fora da gramática ou citando id que não é item —
vocabulário do instrumento fechado em `C-1..C-17`; `show` emite o dossiê verbatim de um item,
inteiro no card de tarefa; o teto `DB-7` (8.000 chars / 120 linhas, com ponteiro `arquivo:l1-l2` quando corta) vale para plano, notas de execução e achados.

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
- campos: 1º bullet `- **Status:** \\`<estado>\\``, estado entre crases obrigatório (`LM-T4b`).
  Duas regras: (i) **leitura** — a forma canônica `· AAAA-MM-DD[ · <razão>]` continua aceita, e
  a forma em prosa também (qualquer texto livre depois do estado); tudo que vier depois de
  ` — ` é cauda livre, lida e preservada, nunca interpretada. No ramo canônico a fronteira é
  estrita (`LM-T4c`): a razão não contém ` — `; a cauda começa no primeiro ` — ` da linha e vai
  até o fim. Medido por introspeção no `ESC-19` sobre
  `` - **Status:** `blocked` · 2026-09-19 · premissa — cauda viva ``: antes desta regra
  razão='premissa — cauda viva' e cauda=None; depois, razão='premissa' e cauda='cauda viva'. O
  ramo em prosa não muda. Medido no despacho da `LM-T4b` (`P-0740-loop-de-modulos.md`): 25
  bullets de `Status`, 0 casavam com o regex estrito antes desta regra. (ii) **escrita** —
  `transacionar_status` reescreve só o prefixo de máquina (estado, data, razão) e preserva a
  cauda a partir de ` — `. Opcional `- **Depende de:** ...`.
- índice: `| <ID> | <título> | <estado>[ <done>/<total>] | <âncora> |`.

`carregar` só lê `docs/DIARIO_DE_OBRAS.md` e `docs/plans/P-*.md` — nunca abre `*_HISTORICO.md`
nem `_INBOX.md` (fora de escopo desta tarefa; a migração e o `drain` são tarefas futuras do
plano). Superfície testável: `carregar`/`check`/`show` recebem `repo`/`modelo` já resolvidos e
nunca leem `sys.argv` — mesmo desenho de `telemetria.py` (`DB-1`).

CLI: ``python .claude/tools/backlog.py check [--repo <caminho>]`` (exit 0 sem violação, 1 com
violação) e ``python .claude/tools/backlog.py show <ID> [--repo <caminho>]``. A CLI só embrulha
`check`/`show` — nenhuma regra vive aqui (`DB-1`).
"""
from __future__ import annotations

import argparse
import datetime
import importlib.util
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path


def _carregar_caminhos():
    caminho = Path(__file__).resolve().parent / "caminhos.py"
    spec = importlib.util.spec_from_file_location("caminhos", caminho)
    modulo = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = modulo
    spec.loader.exec_module(modulo)
    return modulo


_caminhos = _carregar_caminhos()


_rdo_modulo = None


def _carregar_rdo():
    """Carregado sob demanda (não no import do módulo): ambientes de teste que copiam só
    `backlog.py` + `caminhos.py` para uma raiz de teste isolada (sem `rdo.py`) continuam
    funcionando para todo caminho que não liga `dossie=True` — só `_dossie_check` chama isto."""
    global _rdo_modulo
    if _rdo_modulo is None:
        caminho = Path(__file__).resolve().parent / "rdo.py"
        spec = importlib.util.spec_from_file_location("rdo", caminho)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        _rdo_modulo = modulo
    return _rdo_modulo

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
# EBK-T3 — regex independente (não usada por TAREFA_HEADER_RE/SUBTAREFA_HEADER_RE) só para
# extrair `+ dono`/`esforço` do texto bruto do cabeçalho, sem tocar a numeração de grupos que
# `test_tr_bkl_grupos_posicionais` (LM-T4a) trava: `_BRACKET` continua com dono/esforço não
# capturantes ali.
_BRACKET_DETALHE_RE = re.compile(
    rf"\[(?:{_MODELOS})(?P<dono> \+ dono)?(?: · esforço (?P<esforco>{_ESFORCOS}))?"
    rf" · classe (?:{_CLASSES})(?: · teto \d+)?\]"
)

PLANO_HEADER_RE = _caminhos.PLANO_HEADER_RE
STATUS_CAMPO_RE = re.compile(r"\*\*Status:\*\* `([a-z-]+)`")
PREFIXO_CAMPO_RE = re.compile(r"\*\*Prefixo das tarefas no diário:\*\* `([A-Za-z0-9]+)-T<n>`")
ORDEM_CAMPO_RE = re.compile(r"\*\*Ordem de execução:\*\* (.+)$")

HEADING_RE = re.compile(r"^(#{2,3}) (\S+) — (.*)$")
TICKET_ID_ONLY_RE = re.compile(r"^TK-\d+[a-z]?$")
TASK_ID_ONLY_RE = re.compile(r"^(?:[A-Z0-9]+-)?T\d+[a-z]?$")

TIQUETE_HEADER_RE = re.compile(r"^## (TK-\d+) — (.+)$")
SUBTAREFA_HEADER_RE = re.compile(rf"^### (TK-\d+[a-z]) — (.+?) {_BRACKET}$")
TAREFA_HEADER_RE = re.compile(rf"^### ((?:[A-Z0-9]+-)?T\d+[a-z]?) — (.+?) {_BRACKET}$")

STATUS_BULLET_RE = re.compile(
    r"^- \*\*Status:\*\* `([a-z-]+)`(?: · \d{4}-\d{2}-\d{2}(?: · ([^—]+?))?|.*?)(?: — (.+))?$"
)
DEPENDE_BULLET_RE = re.compile(r"^- \*\*Depende de:\*\* (.+)$")
# Gramática publicada do valor (skill `diario-de-obras`, *Item e residência*): `` `ID`[, `ID`] ``
# e nada mais — `C-12` (TK-65a) acusa quem desvia.
DEPENDE_VALOR_RE = re.compile(r"^`[^`\s]+`(?:, `[^`\s]+`)*$")
TIPO_BULLET_RE = re.compile(r"^- \*\*Tipo:\*\* (.+)$")
NOTAS_BULLET_RE = re.compile(r"^- \*\*Notas de execução:\*\*\s*$")
DIRETIVA_RE = re.compile(r"^\*\*Diretiva de priorização:\*\* (.*)$")
NIVEL_1_OU_2_RE = re.compile(r"^#{1,2} ")

INDICE_LINHA_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|$")
INDICE_HEADING_RE = re.compile(r"^## Índice\s*$")

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
    dono: bool = False
    esforco: str | None = None
    header_valido: bool = True
    status: str | None = None
    status_linha: int | None = None
    status_razao: str | None = None
    status_cauda: str | None = None
    depende_de: list[str] = field(default_factory=list)
    depende_linha: int | None = None
    depende_na_gramatica: bool = True
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
    fora_do_corpus: bool = False
    estado_arquivo: str | None = None
    estado_ids: list[tuple[str, int]] = field(default_factory=list)
    estado_defeitos: list[tuple[int, str]] = field(default_factory=list)
    status_no_texto: int | None = None


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
) -> tuple[str | None, int | None, str | None, str | None]:
    """1º bullet não-branco após o heading. Se não for `- **Status:** ...`, o item não tem
    status (`C-2`), qualquer que seja o conteúdo.

    Aceita a forma canônica (`· AAAA-MM-DD[ · <razão>]`) e a forma em prosa por igual — só o
    estado entre crases é obrigatório (`LM-T4b`). O 4º valor é a cauda livre (tudo depois de
    ` — `), devolvida verbatim e nunca interpretada."""
    for j in range(inicio_idx, fim_idx + 1):
        bruta = linhas[j]
        if bruta.strip() == "":
            continue
        m = STATUS_BULLET_RE.match(bruta)
        if m:
            razao = m.group(2).strip() if m.group(2) is not None else None
            return m.group(1), j + 1, razao, m.group(3)
        return None, None, None, None
    return None, None, None, None


def _extrair_depende(linhas: list[str], inicio_idx: int, fim_idx: int) -> list[str]:
    for j in range(inicio_idx, fim_idx + 1):
        m = DEPENDE_BULLET_RE.match(linhas[j])
        if m:
            return re.findall(r"`([^`]+)`", m.group(1))
    return []


def _extrair_depende_forma(linhas: list[str], inicio_idx: int, fim_idx: int) -> tuple[int | None, bool]:
    """Linha (1-based) do bullet `Depende de:` e se o valor está na gramática publicada. Linha
    recuada logo depois do bullet é continuação do campo — `_extrair_depende` só lê a 1ª linha,
    então id na continuação some do seletor: fora da gramática, igual a prosa (`C-12`)."""
    for j in range(inicio_idx, fim_idx + 1):
        m = DEPENDE_BULLET_RE.match(linhas[j])
        if m:
            na_gramatica = bool(DEPENDE_VALOR_RE.match(m.group(1).rstrip()))
            if j + 1 <= fim_idx and linhas[j + 1][:1] in (" ", "\t") and linhas[j + 1].strip():
                na_gramatica = False
            return j + 1, na_gramatica
    return None, True


def _extrair_tipo(linhas: list[str], inicio_idx: int, fim_idx: int) -> str | None:
    for j in range(inicio_idx, fim_idx + 1):
        m = TIPO_BULLET_RE.match(linhas[j])
        if m:
            return m.group(1).strip()
    return None


def _fim_na_secao(linhas: list[str], inicio_idx: int, fim_idx: int) -> int:
    """TK-87a — fim do item também corta na primeira linha, entre `inicio_idx + 1` e `fim_idx`,
    que casa `NIVEL_1_OU_2_RE` fora de cerca de código (```` ``` ```` ou `~~~` abre/fecha).
    Devolve `fim_idx` sem alteração se nenhuma linha assim existir fora de cerca."""
    em_cerca = False
    for j in range(inicio_idx + 1, fim_idx + 1):
        linha = linhas[j]
        if linha.startswith("```") or linha.startswith("~~~"):
            em_cerca = not em_cerca
            continue
        if not em_cerca and NIVEL_1_OU_2_RE.match(linha):
            return j - 1
    return fim_idx


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
        dono_tok = False
        esforco_tok = None
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
            if tipo in ("tarefa", "subtarefa"):
                det = _BRACKET_DETALHE_RE.search(linha)
                if det is not None:
                    dono_tok = det.group("dono") is not None
                    esforco_tok = det.group("esforco")

        fim_idx = heading_idxs[pos + 1] - 1 if pos + 1 < len(heading_idxs) else len(linhas) - 1
        fim_idx = _fim_na_secao(linhas, i, fim_idx)
        linha_header = i + 1
        linha_fim = fim_idx + 1
        texto_secao = "\n".join(linhas[i : fim_idx + 1])

        status, status_linha, status_razao, status_cauda = _extrair_status(linhas, i + 1, fim_idx)
        depende_de = _extrair_depende(linhas, i + 1, fim_idx)
        depende_linha, depende_na_gramatica = _extrair_depende_forma(linhas, i + 1, fim_idx)
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
                dono=dono_tok,
                esforco=esforco_tok,
                header_valido=valido,
                status=status,
                status_linha=status_linha,
                status_razao=status_razao,
                status_cauda=status_cauda,
                depende_de=depende_de,
                depende_linha=depende_linha,
                depende_na_gramatica=depende_na_gramatica,
                campo_tipo=campo_tipo,
            )
        )
    return itens


def _parse_indice(linhas: list[str], arquivo_rel: str) -> list[LinhaIndice]:
    """Âncora do índice (§2.2, DB-43): a tabela que segue o cabeçalho `## Índice`, e só ela —
    começa na primeira linha iniciada por `|` depois desse cabeçalho e termina na primeira linha
    em branco. Nenhuma outra tabela markdown do diário produz linha de índice."""
    resultado: list[LinhaIndice] = []
    inicio_secao = next((i for i, l in enumerate(linhas) if INDICE_HEADING_RE.match(l)), None)
    if inicio_secao is None:
        return resultado
    inicio_tabela = next(
        (i for i in range(inicio_secao + 1, len(linhas)) if linhas[i].startswith("|")), None
    )
    if inicio_tabela is None:
        return resultado
    for i in range(inicio_tabela, len(linhas)):
        linha = linhas[i]
        if linha.strip() == "":
            break
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
                id=id_, titulo=titulo, status_bruto=status_bruto, arquivo=arquivo_rel, linha=i + 1, ancora=ancora
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


def _aplicar_estado_tsv(caminho: Path, repo: Path, plano: Plano, linhas_plano: list[str]) -> None:
    """P-0749 SAN-T2 (`DSA-5`): plano em pasta tem o estado em `estado.tsv`, nunca no texto."""
    plano.status, plano.status_linha = None, None
    plano.status_no_texto = next(
        (i for i, linha in enumerate(linhas_plano, start=1) if STATUS_CAMPO_RE.search(linha)), None
    )
    por_id = {t.id: t for t in plano.tarefas}
    for tarefa in plano.tarefas:
        tarefa.status = tarefa.status_linha = tarefa.status_razao = tarefa.status_cauda = None
    estado_path = _caminhos.estado_tsv(caminho)
    plano.estado_arquivo = estado_path.relative_to(repo).as_posix()
    if not estado_path.is_file():
        plano.estado_defeitos.append((1, "estado.tsv ausente"))
        return
    linhas = estado_path.read_text(encoding="utf-8").splitlines()
    if not linhas or linhas[0] != _caminhos.CABECALHO_ESTADO:
        plano.estado_defeitos.append((1, "cabeçalho fora do esquema"))
        return
    for n, linha in enumerate(linhas[1:], start=2):
        if not linha.strip():
            continue
        campos = linha.split("\t")
        if len(campos) != 6:
            plano.estado_defeitos.append((n, "linha fora do esquema"))
            continue
        id_, tipo, status, razao, _data, nota = campos
        if tipo == "plano" and id_ == plano.id:
            plano.status = status
        elif tipo == "tarefa":
            plano.estado_ids.append((id_, n))
            tarefa = por_id.get(id_)
            if tarefa is not None:
                tarefa.status = status
                tarefa.status_razao = None if razao == "-" else razao
                tarefa.status_cauda = None if nota == "-" else nota
        else:
            plano.estado_defeitos.append((n, f"{id_}: tipo '{tipo}' fora do esquema"))


def _parse_plano(caminho: Path, repo: Path) -> Plano:
    texto = caminho.read_text(encoding="utf-8")
    linhas = texto.splitlines()
    rel = caminho.relative_to(repo).as_posix()

    m0 = PLANO_HEADER_RE.match(linhas[0]) if linhas else None
    pasta = _caminhos.pasta_do_plano(caminho)
    nome = pasta.name if pasta is not None else caminho.stem
    plano_id = m0.group(1) if m0 else nome
    titulo = m0.group(2) if m0 else nome

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

    plano = Plano(
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
    if _caminhos.e_layout_pasta(caminho):
        _aplicar_estado_tsv(caminho, repo, plano, linhas)
    return plano


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

    planos = [_parse_plano(caminho, repo) for caminho in _caminhos.arquivos_de_plano(repo)]
    indice, tiquetes, diario_linhas = _parse_diario(diario_path, repo)
    diretiva_ids = _parse_diretiva(diario_linhas)

    modelo = Modelo(
        planos=planos,
        tiquetes=tiquetes,
        indice=indice,
        diario_arquivo=diario_path.relative_to(repo).as_posix(),
        diario_linhas=diario_linhas,
        diretiva_ids=diretiva_ids,
    )

    # §2.0 (DB-43) — a autoridade sobre a vida de um plano é a célula de estado da linha dele no
    # índice do diário, casada pela regra de sufixo de `_posicao_indice` (residência única do
    # casamento). Núcleo em done/superseded/cancelled → plano fora do corpus.
    for plano in planos:
        pos = _posicao_indice(modelo, plano.id)
        if pos is not None:
            nucleo, _, _ = _celula_indice(modelo.indice[pos].status_bruto)
            plano.fora_do_corpus = nucleo in {"done", "superseded", "cancelled"}

    return modelo


# --------------------------------------------------------------------------- #
# check — violações C-1..C-17 (C-11 via resolver_citacao_secao, definido abaixo — TK-60a:
# check é o chamador de produção, nenhum subcomando novo; C-12 via _depende_checks — TK-65a;
# C-15 acusa tíquete vivo sem subtarefa — EBK-T1; C-16 confronta card vivo com a leitura de
# dossiê do rdo.py e C-17 acusa entrada órfã de piso_c11 — EBK-T2)
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


def _plano_em_esboco(plano: Plano, texto_inbox: str) -> bool:
    """Domínio (`AF-T8`): plano em pasta cujo `estado.tsv` tem, depois do cabeçalho, uma linha
    só — a do plano, `blocked` — e nenhuma linha de `docs/plans/_INBOX.md` cita o caminho dele.
    É o estado entre a Fase 3a e a Fase 5 do planejador. `estado_arquivo` só existe em plano em
    pasta: plano legado `blocked` segue acusado no `C-10` (`AE-10`, reparo do consultor)."""
    return (
        plano.estado_arquivo is not None
        and plano.status == "blocked"
        and not plano.estado_ids
        and plano.arquivo not in texto_inbox
    )


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


def _ids_da_arvore(modelo: Modelo) -> set[str]:
    """Todo id que `_status_do_id` resolve — o espaço em que o seletor percorre `Depende de`."""
    ids: set[str] = set()
    for plano in modelo.planos:
        ids.add(plano.id)
        ids.update(t.id for t in plano.tarefas)
    for tiquete in modelo.tiquetes:
        ids.add(tiquete.id)
        ids.update(s.id for s in tiquete.filhos)
    return ids


def _depende_checks(item: Item, ids_arvore: set[str], violacoes: list[Violacao]) -> None:
    """C-12 (TK-65a) — `Depende de:` é lista de ids de item por gramática publicada. Prosa no
    campo, ou id que não resolve na árvore, deixa o item inselecionável por `next` sem que o
    lint avise: o seletor exige `done` de cada id e id inexistente nunca fica `done`."""
    if item.depende_linha is None:
        return
    if not item.depende_na_gramatica:
        violacoes.append(
            Violacao("C-12", item.arquivo, item.depende_linha, f"{item.id}: Depende de fora da gramática (prosa)")
        )
    for id_ in item.depende_de:
        if id_ not in ids_arvore:
            violacoes.append(
                Violacao("C-12", item.arquivo, item.depende_linha, f"{item.id}: Depende de cita '{id_}', que não é item")
            )


_ITEM_VIVO_DOSSIE = {"ready", "in-progress", "review"}


def _dossie_check(item: Item, repo: Path | None, dossie: bool, violacoes: list[Violacao]) -> None:
    """C-16 (EBK-T2) — confronta o card com a mesma leitura de dossiê que `rdo.py close` usa
    (`extrair_dossie`, leitura estrita: `esquema_legado=False, modelo_legado=None,
    classe_legado=None`), sem reimplementar a gramática (propriedade 1). Só corre com
    `dossie=True` e `repo` dado (propriedade 5); card `done`, `cancelled` ou `blocked` (fora de
    `_ITEM_VIVO_DOSSIE`) não é lido (propriedade 2)."""
    if not dossie or repo is None:
        return
    if item.status not in _ITEM_VIVO_DOSSIE:
        return
    rdo = _carregar_rdo()
    try:
        rdo.extrair_dossie(
            repo / item.arquivo,
            item.id,
            esquema_legado=False,
            modelo_legado=None,
            classe_legado=None,
        )
    except rdo.RdoValidationError as exc:
        violacoes.append(Violacao("C-16", item.arquivo, item.linha_header, str(exc)))


def check(
    modelo: Modelo,
    inbox_planos: Path | None = None,
    repo: Path | None = None,
    piso_c11: set[tuple[str, str]] | None = None,
    dossie: bool = False,
) -> list[Violacao]:
    violacoes: list[Violacao] = []
    ids_arvore = _ids_da_arvore(modelo)

    for plano in modelo.planos:
        if plano.fora_do_corpus:
            # §2.0 (DB-43) — plano fora do corpus: check não o linta, nem o cabeçalho (C-7,
            # C-8) nem as tarefas dele (C-1, C-2). C-5, index-line-based, não é lint do plano
            # e continua avaliado no laço sobre `modelo.indice` abaixo.
            continue
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

        if plano.estado_arquivo is not None:
            for linha_n, mensagem in plano.estado_defeitos:
                violacoes.append(Violacao("C-13", plano.estado_arquivo, linha_n, mensagem))
            ids_estado = {id_ for id_, _ in plano.estado_ids}
            ids_cards = {t.id for t in plano.tarefas}
            for tarefa in plano.tarefas:
                if tarefa.id not in ids_estado:
                    violacoes.append(
                        Violacao("C-13", plano.arquivo, tarefa.linha_header, f"{tarefa.id} sem linha em estado.tsv")
                    )
            for id_, linha_n in plano.estado_ids:
                if id_ not in ids_cards:
                    violacoes.append(
                        Violacao("C-13", plano.estado_arquivo, linha_n, f"{id_}: linha de estado.tsv sem card em plano.md")
                    )
            if plano.status_no_texto is not None:
                violacoes.append(
                    Violacao("C-14", plano.arquivo, plano.status_no_texto, f"{plano.id}: linha **Status:** em plano de pasta")
                )

        for tarefa in plano.tarefas:
            _item_checks(tarefa, violacoes)
            _depende_checks(tarefa, ids_arvore, violacoes)
            _dossie_check(tarefa, repo, dossie, violacoes)

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
        _depende_checks(tiquete, ids_arvore, violacoes)
        if tiquete.status not in {"done", "cancelled", "superseded"} and not tiquete.filhos:
            violacoes.append(
                Violacao("C-15", tiquete.arquivo, tiquete.linha_header, f"{tiquete.id} vivo sem subtarefa")
            )
        for sub in tiquete.filhos:
            _item_checks(sub, violacoes)
            _depende_checks(sub, ids_arvore, violacoes)
            _dossie_check(sub, repo, dossie, violacoes)

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

    ids_tiquetes = {t.id for t in modelo.tiquetes}
    for pos, linha in enumerate(modelo.indice):
        nucleo, tem_narrativa, _done_total = _celula_indice(linha.status_bruto)
        # DB-46: núcleo terminal (done/superseded/cancelled) é projeção final — C-4 não vale
        # para ele. C-3 (vocabulário do núcleo) vale para toda linha, terminal ou não.
        terminal = nucleo in {"done", "superseded", "cancelled"}
        # DB-43/DB-15: casamento de id de plano pela mesma regra de sufixo de `_posicao_indice`
        # (residência única) — nenhuma outra reimplementação desse casamento.
        plano_da_linha = None
        for plano in modelo.planos:
            if _posicao_indice(modelo, plano.id) == pos:
                plano_da_linha = plano
                break

        if nucleo not in _VOCAB_PLANO:
            violacoes.append(
                Violacao(
                    "C-3", linha.arquivo, linha.linha, f"{linha.id}: status de índice '{nucleo}' fora do vocabulário"
                )
            )
        elif tem_narrativa and not terminal:
            violacoes.append(Violacao("C-4", linha.arquivo, linha.linha, f"{linha.id}: célula do índice com prosa"))
        else:
            item_status = plano_da_linha.status if plano_da_linha is not None else _status_do_id(modelo, linha.id)
            if item_status is not None and item_status != nucleo:
                violacoes.append(
                    Violacao(
                        "C-5",
                        linha.arquivo,
                        linha.linha,
                        f"{linha.id}: índice '{nucleo}' diverge do campo '{item_status}'",
                    )
                )

        if not terminal and plano_da_linha is None and linha.id not in ids_tiquetes:
            violacoes.append(
                Violacao("C-9", linha.arquivo, linha.linha, f"{linha.id}: sem residência em plano vivo nem diário")
            )

    if inbox_planos is not None and inbox_planos.exists():
        # C-10 — o contador `**Próximo id de plano: P-NNNN.**` de `docs/plans/_INBOX.md`
        # confrontado com o maior id realmente presente em `docs/plans/P-*.md` (`modelo.planos`,
        # todo arquivo do glob, vivo ou não — DB-38). Nunca contra os ids mencionados no
        # próprio texto do inbox: plano criado sem linha de inbox não aparece lá, e é
        # exatamente esse o caso medido que motivou a violação.
        # AF-T8: o plano em esboço cujo id é o do contador não entra em `ids_planos` — ele
        # ainda não tem linha no inbox nem tarefa registrada (Domínio, `_plano_em_esboco`).
        texto_inbox = inbox_planos.read_text(encoding="utf-8")
        for i, linha_inbox in enumerate(texto_inbox.splitlines(), start=1):
            m = _CONTADOR_INBOX_ID_RE.search(linha_inbox)
            if m is None:
                continue
            contador = int(m.group(1))
            ids_planos: list[int] = []
            for p in modelo.planos:
                mid = _ID_PLANO_RE.match(p.id)
                if mid and not (int(mid.group(1)) == contador and _plano_em_esboco(p, texto_inbox)):
                    ids_planos.append(int(mid.group(1)))
            # Sem plano presente (projeto novo, `DSA-14`), todo contador vale, `P-0` inclusive.
            if ids_planos and contador <= max(ids_planos):
                violacoes.append(
                    Violacao(
                        "C-10",
                        "docs/plans/_INBOX.md",
                        i,
                        f"contador aponta para {_caminhos.formatar_id(contador, len(m.group(1)))}, já presente em docs/plans/",
                    )
                )
            break

    if repo is not None:
        # C-11 — citações de seção do corpus (item 6, TK-60a: chamador de produção é
        # `check`, nenhum subcomando novo). Corpus = `docs/DIARIO_DE_OBRAS.md` +
        # `docs/plans/P-*.md` (via modelo, DB-38: todo arquivo do glob, vivo ou não) +
        # `docs/DIARIO_HISTORICO.md` (carregar() nunca abre esse arquivo — leitura direta,
        # só para este lint).
        fontes: list[tuple[str, str]] = [(modelo.diario_arquivo, "\n".join(modelo.diario_linhas))]
        for plano in modelo.planos:
            fontes.append((plano.arquivo, plano.texto))
        historico = repo / "docs" / "DIARIO_HISTORICO.md"
        if historico.exists():
            fontes.append((historico.relative_to(repo).as_posix(), historico.read_text(encoding="utf-8")))

        chaves_quebradas: set[tuple[str, str]] = set()
        for arquivo_fonte, texto_fonte in fontes:
            for linha_num, referencia in _citacoes_do_texto(texto_fonte):
                violacao = resolver_citacao_secao(referencia, repo)
                if violacao is None:
                    continue
                m = _REF_SECAO_RE.match(referencia.strip())
                chave = (m.group("arquivo"), m.group("secao")) if m is not None else None
                if chave is not None:
                    chaves_quebradas.add(chave)
                if piso_c11 is not None and chave in piso_c11:
                    continue
                violacoes.append(
                    Violacao("C-11", arquivo_fonte, linha_num, f"referência não resolvida: {referencia}")
                )

        # C-17 (EBK-T2, DEB-7 propriedade 5) — `piso_c11` é o único que decide o silêncio de
        # C-11 e a existência deste lint: `None` = sem piso, nenhuma entrada a checar. O piso
        # vem de `docs/PISO_C11.tsv` do repositório checado (`ler_piso_c11`, TK-86a). Entrada
        # que não casa nenhuma citação quebrada do corpus corrente é órfã (propriedade 3).
        if piso_c11 is not None:
            for entry_arquivo, entry_secao in sorted(piso_c11):
                if (entry_arquivo, entry_secao) not in chaves_quebradas:
                    violacoes.append(
                        Violacao(
                            "C-17",
                            entry_arquivo,
                            1,
                            f"piso_c11 nomeia entrada órfã: `{entry_arquivo}` §{entry_secao}",
                        )
                    )

    return violacoes


# --------------------------------------------------------------------------- #
# resolver_citacao_secao — terceiro resolvedor de referência do kit (TK-60): caminho de
# arquivo já tem Test-Path, identificador de tarefa tem review_evidence, citação de seção
# tem este. C-11. Chamador de produção é `check`, acima (item 6, TK-60a) — nenhum
# subcomando novo.
# --------------------------------------------------------------------------- #

# Gramática observada, não a inventada (item 1, TK-60a): `` `<arquivo>.md` §<N>[.<N>]* ``
# — 1.017 ocorrências medidas no corpus contra 1 só da forma antiga `§X.Y publicada em
# <arquivo>` (o próprio texto do tíquete anterior).
_REF_SECAO_RE = re.compile(r"^`(?P<arquivo>[^`]+\.md)`\s+§(?P<secao>\d+(?:\.\d+)*)$")
_CITACAO_SECAO_HARVEST_RE = re.compile(r"`(?P<arquivo>[^`]+\.md)`\s+§(?P<secao>\d+(?:\.\d+)*)")
_HEADING_NUMERADO_RE = re.compile(r"^#{1,6}\s+(?P<num>\d+(?:\.\d+)*)\b")

# Piso de C-11 (TK-86a) — lido de `docs/PISO_C11.tsv` do repositório checado, não mais
# constante do código: o piso é dívida de um corpus, e cada repositório tem o seu.
_PISO_C11_ARQUIVO = "docs/PISO_C11.tsv"
_PISO_C11_CABECALHO = "arquivo\tsecao\torigem"
_PISO_C11_SECAO_RE = re.compile(r"^\d+(?:\.\d+)*$")


def ler_piso_c11(repo: Path) -> tuple[set[tuple[str, str]] | None, list[Violacao]]:
    """Lê o piso de C-11 de `docs/PISO_C11.tsv` do repositório checado.

    Piso de C-11 (item 7, TK-60a) — dívida já presente no corpus vivo, contabilizada para o
    lint não nascer vermelho; mesma trava do `.claude/checks/ratchet_piso.py` (falha só no
    PRÓXIMO ponteiro quebrado, não nos já conhecidos). Quitar o piso é tíquete próprio. Origem
    da entrada do hub: medido em 2026-09-20 (TK-60a, card), 15 ocorrências
    (`docs/plans/P-0741-modelo-conceitual.md` 6, `docs/DIARIO_HISTORICO.md` 6,
    `docs/DIARIO_DE_OBRAS.md` 1, `docs/plans/P-0730-v2-identidade.md` 1,
    `docs/plans/P-0731-v2-extracao-modalidade.md` 1).

    Arquivo ausente → `(None, [])` (sem piso, e o C-17 não tem o que checar). Cabeçalho fora do
    esquema → piso vazio e um C-17 na linha 1. Linha não vazia fora do esquema → C-17 com o
    número dela, e a linha não entra no piso.
    """
    caminho = repo / _PISO_C11_ARQUIVO
    if not caminho.is_file():
        return None, []
    linhas = caminho.read_text(encoding="utf-8").splitlines()
    if not linhas or linhas[0] != _PISO_C11_CABECALHO:
        return set(), [Violacao("C-17", _PISO_C11_ARQUIVO, 1, "cabeçalho fora do esquema")]
    piso: set[tuple[str, str]] = set()
    violacoes: list[Violacao] = []
    for numero, linha in enumerate(linhas[1:], start=2):
        if not linha.strip():
            continue
        campos = linha.split("\t")
        if len(campos) != 3 or not campos[0] or not _PISO_C11_SECAO_RE.match(campos[1]):
            violacoes.append(Violacao("C-17", _PISO_C11_ARQUIVO, numero, "linha fora do esquema"))
            continue
        piso.add((campos[0], campos[1]))
    return piso, violacoes


def _resolver_arquivo_citado(arquivo: str, repo: Path) -> Path | None:
    """Raiz do repo primeiro; queda para basename único no corpus (item 4, TK-60a) — 56
    ocorrências/20 distintas citam só o nome-base (`` `RUBRICA_DE_REVISAO.md` §8 ``, 9
    delas) com o arquivo em `docs/`. Ambíguo (mais de um arquivo com o mesmo nome no repo)
    ou ausente devolve `None` — quem acusa arquivo inexistente é `Test-Path` (`DB-2`, uma
    residência por regra), não este resolvedor (item 5)."""
    direto = repo / arquivo
    if direto.exists():
        return direto
    basename = Path(arquivo).name
    achados: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(repo):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        if basename in filenames:
            achados.append(Path(dirpath) / basename)
    if len(achados) == 1:
        return achados[0]
    return None


def resolver_citacao_secao(referencia: str, repo: Path) -> Violacao | None:
    """Resolve uma citação `` `<arquivo>.md` §<N>[.<N>]* `` contra o arquivo citado.
    Casamento por **heading** numerado (`^#{1,6} X.Y`), nunca substring — o caso que
    motivou o `TK-60`, `` `.claude/skills/diario-de-obras/SKILL.md` §2.5 ``, tem o literal
    `2.5` só em prosa (nenhum heading `2.5`) e por isso tem de sair `C-11` apesar do literal
    existir no arquivo.

    Domínio (item 2): um nível (`§3`) e dois níveis (`§3.2`) são seção; três ou mais
    componentes numéricos (`§3.0.0`) são versão, não seção — devolve `None` em silêncio
    (item 5), sem checar arquivo algum. Caminho: raiz do repo primeiro, com queda para
    basename único no corpus (item 4, `_resolver_arquivo_citado`); arquivo que não existe
    nem por basename também devolve `None` em silêncio — resolver caminho é do `Test-Path`
    (`DB-2`), não deste resolvedor (item 5).

    Devolve `None` quando a seção existe no arquivo citado, ou nos dois silêncios acima;
    `Violacao("C-11", ...)`, com o literal da referência recebida na mensagem, quando a
    seção não existe no arquivo citado, ou quando `referencia` não casa a gramática."""
    m = _REF_SECAO_RE.match(referencia.strip())
    if m is None:
        return Violacao("C-11", referencia, 1, f"referência não resolvida: {referencia}")
    arquivo = m.group("arquivo")
    secao = m.group("secao")
    if secao.count(".") >= 2:
        return None  # três ou mais componentes numéricos = versão, não seção (item 5)
    caminho = _resolver_arquivo_citado(arquivo, repo)
    if caminho is None:
        return None
    for linha in caminho.read_text(encoding="utf-8").splitlines():
        hm = _HEADING_NUMERADO_RE.match(linha)
        if hm is not None and hm.group("num") == secao:
            return None
    return Violacao("C-11", arquivo, 1, f"referência não resolvida: {referencia}")


def _citacoes_do_texto(texto: str) -> list[tuple[int, str]]:
    """Todas as citações `` `<arquivo>.md` §<N>[.<N>]* `` de um texto, pareadas com a linha
    (1-based) onde cada uma começa — usado por `check` para varrer o corpus (item 6,
    TK-60a)."""
    resultado: list[tuple[int, str]] = []
    for m in _CITACAO_SECAO_HARVEST_RE.finditer(texto):
        linha = texto.count("\n", 0, m.start()) + 1
        resultado.append((linha, m.group(0)))
    return resultado


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


_ACHADOS_HEADING_RE = re.compile(r"^## .*Achados da execução")
_AE_ID_RE = re.compile(r"\bAE-(\d+)\b")


def achados_roteados(texto_plano: str, tarefa_id: str) -> list[str]:
    """Entradas `AE-<n>` da seção `## Achados da execução` do plano cuja `**Rota:**` cita
    `tarefa_id` como palavra inteira (DFP-7/DFP-19). Leitura duplicada de
    `encerrar.achados_do_plano`/`_secao_achados`, sem import cruzado entre os dois módulos."""
    linhas = texto_plano.splitlines()
    ini = next((i for i, l in enumerate(linhas) if _ACHADOS_HEADING_RE.match(l)), None)
    if ini is None:
        return []
    fim = next((j for j in range(ini + 1, len(linhas)) if re.match(r"^#{1,2} ", linhas[j])), len(linhas))

    entradas_linhas: list[list[str]] = []
    atual: list[str] | None = None
    for linha in linhas[ini + 1 : fim]:
        if linha.startswith("- "):
            if atual is not None:
                entradas_linhas.append(atual)
            atual = [linha]
        elif atual is not None:
            atual.append(linha)
    if atual is not None:
        entradas_linhas.append(atual)

    resultado: list[str] = []
    for bruta in entradas_linhas:
        aparada = list(bruta)
        while aparada and aparada[-1].strip() == "":
            aparada.pop()
        if not aparada or not _AE_ID_RE.search(aparada[0]):
            continue
        texto_entrada = "\n".join(aparada)
        marcador = "**Rota:**"
        pos_rota = texto_entrada.find(marcador)
        if pos_rota == -1:
            continue
        rota = texto_entrada[pos_rota + len(marcador) :]
        if re.search(rf"(?<![\w-]){re.escape(tarefa_id)}(?![\w-])", rota):
            resultado.append(texto_entrada)
    return resultado


def _bloco_achados(texto_plano: str, tarefa_id: str) -> str:
    entradas = achados_roteados(texto_plano, tarefa_id)
    if not entradas:
        return "**Achados roteados a este card:** nenhum"
    return "\n".join(["**Achados roteados a este card:**", *entradas])


def _achados_truncados(plano: "Plano", tarefa_id: str) -> str:
    """Bloco de achados roteados a `tarefa_id` sob o teto `DB-7`. O ponteiro do corte (`AE-11`
    do `P-0753`) é a seção `## Achados da execução` no arquivo do plano — de onde o bloco foi
    cortado —, não a faixa do plano inteiro; sem a seção, cai na faixa do plano."""
    linhas = plano.texto.splitlines()
    ini = next((i for i, l in enumerate(linhas) if _ACHADOS_HEADING_RE.match(l)), None)
    if ini is None:
        l1, l2 = plano.linha_header, plano.linha_fim
    else:
        fim = next((j for j in range(ini + 1, len(linhas)) if re.match(r"^#{1,2} ", linhas[j])), len(linhas))
        l1, l2 = plano.linha_header + ini, plano.linha_header + fim - 1
    return _truncar(_bloco_achados(plano.texto, tarefa_id), plano.arquivo, l1, l2)


def _card_inteiro(item: Item) -> str:
    """AF-T9 — o card de um `Item` sai inteiro até a linha anterior a
    `- **Notas de execução:**`; o trecho que começa nessa linha (quando existe) passa por
    `_truncar` (teto `DB-7`)."""
    linhas = item.texto.splitlines()
    idx = next((i for i, l in enumerate(linhas) if NOTAS_BULLET_RE.match(l)), None)
    if idx is None:
        return item.texto
    antes = "\n".join(linhas[:idx])
    notas = "\n".join(linhas[idx:])
    notas_truncadas = _truncar(notas, item.arquivo, item.linha_header + idx, item.linha_fim)
    if antes:
        return antes + "\n" + notas_truncadas
    return notas_truncadas


def show(modelo: Modelo, id_: str) -> str:
    alvo = _localizar(modelo, id_)
    if alvo is None:
        return f"id não encontrado: {id_}"
    if isinstance(alvo, Item):
        texto = _card_inteiro(alvo)
        if alvo.tipo == "tarefa":
            plano = next(p for p in modelo.planos if p.id == alvo.pai)
            bloco = _achados_truncados(plano, alvo.id)
            return texto + "\n\n" + bloco
        return texto
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
        if plano.fora_do_corpus:
            # §2.0/§2.5 item 3 (DB-43) — a exclusão por corpus precede a elegibilidade e,
            # por tabela, precede também a avaliação de E-2 (que corre sobre `_candidatos`).
            continue
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
    """Residencia unica do casamento pai -> linha de indice.

    O indice do diario publica o id de um plano com **sufixo mnemonico**
    (`P-0740-LM`, `P-0739-BKL`), enquanto o cabecalho do arquivo de plano declara so
    `P-NNNN` (`PLANO_HEADER_RE`). Igualdade exata nunca casa nenhum plano vivo — o
    guarda "linha de indice ausente" disparava para **toda** tarefa de **todo** plano
    (medido em 2026-09-19 no `ESC-27` do `P-0740`).

    Regra: id exato vence; na falta dele, a primeira linha — em ordem de documento —
    cujo id seja `<pai_id>-<SUFIXO>` com `SUFIXO` em `[A-Za-z0-9]+`. O sufixo fechado
    impede que celula de tabela ilustrativa (o lixo que o `AE-1` mede no parser de
    indice) case por acidente. Tiquete publica o id nu e cai no ramo exato."""
    padrao = re.compile(rf"^{re.escape(pai_id)}-[A-Za-z0-9]+$")
    sufixado: int | None = None
    for pos, linha in enumerate(modelo.indice):
        if linha.id == pai_id:
            return pos
        if sufixado is None and padrao.match(linha.id):
            sufixado = pos
    return sufixado


def _linha_indice(modelo: Modelo, pai_id: str) -> LinhaIndice | None:
    """A linha de indice do pai, pela mesma regra de `_posicao_indice` — nenhum ponto
    do instrumento reescreve o casamento."""
    pos = _posicao_indice(modelo, pai_id)
    return modelo.indice[pos] if pos is not None else None


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
    linha = _linha_indice(modelo, pai_id)
    return linha.ancora if linha is not None else ""


def _antecessora(pai: Plano | Item, tipo_pai: str, vencedor_item: Item) -> Item | None:
    irmaos = _irmaos_ordenados(pai, tipo_pai)
    idx = next((i for i, x in enumerate(irmaos) if x is vencedor_item), None)
    if idx is None or idx == 0:
        return None
    return irmaos[idx - 1]


HANDOVER_BULLET_RE = re.compile(r"^- \*\*Handover:\*\*(?P<cabecalho>.*)$")


def extrair_handover(item: Item) -> str | None:
    """TK-88 — o campo `- **Handover:**` do card, verbatim: o bullet de topo e as linhas
    indentadas que o seguem (sub-bullets `Entregue`, `Contrato`, `Não refazer`, `Pendente`).
    Escrito por `encerrar.py handover`; lido aqui para o `next` devolvê-lo à sucessora. Ausente
    devolve None — o campo é opcional no card."""
    linhas = item.texto.splitlines()
    inicio = next((i for i, l in enumerate(linhas) if HANDOVER_BULLET_RE.match(l)), None)
    if inicio is None:
        return None
    fim = inicio
    for idx in range(inicio + 1, len(linhas)):
        if linhas[idx][:1] in (" ", "\t") and linhas[idx].strip():
            fim = idx
            continue
        break
    return "\n".join(linhas[inicio:fim + 1])


def handovers_para(pai: Plano | Item, tipo_pai: str, vencedor_item: Item) -> list[tuple[Item, str]]:
    """TK-88 — os handovers que o `next` entrega junto com a próxima tarefa, por nomenclatura,
    sem julgamento: (a) todo irmão cujo cabeçalho do handover nomeia a sucessora entre crases
    depois de `para` (`- **Handover:** <data> · para \\`<ID>\\``); (b) sem nenhum endereçado, o
    handover da antecessora imediata (`_antecessora`), quando ela o tem. A pertinência do que
    entra no dossiê da sucessora é do orquestrador; o instrumento só devolve o registro."""
    resultado: list[tuple[Item, str]] = []
    for irmao in _irmaos_ordenados(pai, tipo_pai):
        if irmao is vencedor_item:
            continue
        texto = extrair_handover(irmao)
        if texto is None:
            continue
        m = HANDOVER_BULLET_RE.match(texto.splitlines()[0])
        cabecalho = m.group("cabecalho") if m else ""
        destinatarios = cabecalho.split("para", 1)[1] if "para" in cabecalho else ""
        if f"`{vencedor_item.id}`" in destinatarios:
            resultado.append((irmao, texto))
    if resultado:
        return resultado
    antecessora_item = _antecessora(pai, tipo_pai, vencedor_item)
    if antecessora_item is not None:
        texto = extrair_handover(antecessora_item)
        if texto is not None:
            return [(antecessora_item, texto)]
    return []


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


def _listar_candidatos_a_fechamento(modelo: Modelo) -> str:
    """TK-61a, `DB-4` — candidato a fechamento: pai (plano ou tíquete) que (a) está no corpus
    da §2.0 (`DB-43` — plano `fora_do_corpus` já exclui o terminal; para tíquete, corpus não
    exclui por status, então (d) faz esse papel), (b) tem >= 1 filho direto, (c) tem todos os
    filhos diretos terminais (`done`/`cancelled` — `superseded` não entra: só plano o tem e
    plano não é filho) e (d) não é ele próprio terminal (`done`/`cancelled`/`superseded`). IDs
    em ordem alfabética crescente (`DB-37` E-1); `<done>/<total>` pela fórmula da `DB-36`
    (`_done_total`)."""
    candidatos: list[tuple[str, int, int]] = []
    for plano in modelo.planos:
        if plano.fora_do_corpus:
            continue
        filhos = plano.tarefas
        if not filhos:
            continue
        if not all(f.status in ("done", "cancelled") for f in filhos):
            continue
        done, total = _done_total(filhos)
        candidatos.append((plano.id, done, total))
    for tiquete in modelo.tiquetes:
        if tiquete.status in ("done", "cancelled", "superseded"):
            continue
        filhos = tiquete.filhos
        if not filhos:
            continue
        if not all(f.status in ("done", "cancelled") for f in filhos):
            continue
        done, total = _done_total(filhos)
        candidatos.append((tiquete.id, done, total))
    if not candidatos:
        return "nenhum"
    candidatos.sort(key=lambda c: c[0])
    return ", ".join(f"{id_} ({done}/{total})" for id_, done, total in candidatos)


_CAMINHO_PLANO_INBOX_RE = _caminhos.CAMINHO_PLANO_INBOX_RE
_ID_PLANO_INBOX_RE = _caminhos.ID_PLANO_INBOX_RE
_CONTADOR_INBOX_RE = _caminhos.CONTADOR_INBOX_RE
_CONTADOR_INBOX_ID_RE = _caminhos.CONTADOR_INBOX_ID_RE
_ID_PLANO_RE = _caminhos.ID_PLANO_RE


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

    sufixo_dono = " + dono" if item.dono else ""
    sufixo_esforco = f" · esforço {item.esforco}" if item.esforco else ""
    bracket = f"[{item.modelo}{sufixo_dono}{sufixo_esforco} · classe {item.classe}]"
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

    # TK-88 — o handover da(s) tarefa(s) que entregaram para esta chega junto com o dossiê,
    # verbatim, sob âncora própria: o orquestrador o cola na delegação quando pertinente.
    for autor, texto_handover in handovers_para(pai, tipo_pai, item):
        linhas_saida.append(f"=== HANDOVER DE {autor.id} — {autor.titulo} ({autor.status}; {autor.arquivo})")
        linhas_saida.append(texto_handover)

    linhas_saida.append("--- dossiê (verbatim, card inteiro) ---")
    linhas_saida.append(_card_inteiro(item))
    if tipo_pai == "plano":
        linhas_saida.append(_achados_truncados(pai, item.id))
    linhas_saida.append("--- pendências mecânicas ---")

    n_inbox_planos = _contar_inbox_planos(inbox_planos) if inbox_planos is not None else 0
    n_memoria = _contar_inbox_memoria(memoria_inbox) if memoria_inbox is not None else 0
    blocked = _listar_blocked(modelo)
    linhas_saida.append(
        f"inbox de planos: {n_inbox_planos} por drenar · fila de memória: {n_memoria} candidato(s) · "
        f"blocked: {blocked}"
    )
    linhas_saida.append(f"candidato a fechamento: {_listar_candidatos_a_fechamento(modelo)}")

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


def _fila_corrente_linha_topo(modelo: Modelo) -> str:
    """Metade 1 (`BKL-T10b`, DB-33) — primeira linha do bloco: `` `<ID>` `` — <título>
    (`` `<arquivo>:<l1>-<l2>` ``) do **pai** do vencedor de `selecionar_next`, residência dele
    por `_residencia_plano`/`_residencia_tiquete`, e as contagens ready/blocked/in-progress do
    corpus (`_candidatos`, já filtrado por `fora_do_corpus`, DB-43 — mesma exclusão da metade
    3). Sem vencedor, a linha declara o motivo (`selecao.mensagem`) em vez de sumir. `fila: —`
    — nenhuma função existente devolve a fila de candidatos além do vencedor; contingência do
    card: usar o que existe e declarar o campo omitido, sem inventar função nova de coleta."""
    selecao = selecionar_next(modelo)
    if selecao.vencedor is None:
        return f"**Fila corrente:** {selecao.mensagem}"

    pai = selecao.vencedor.pai
    tipo_pai = selecao.vencedor.tipo_pai
    residencia = _residencia_plano(pai) if tipo_pai == "plano" else _residencia_tiquete(modelo, pai)

    candidatos_corpus = _candidatos(modelo)
    n_ready = sum(1 for c in candidatos_corpus if c.item.status == "ready")
    n_blocked = sum(1 for c in candidatos_corpus if c.item.status == "blocked")
    n_in_progress = sum(1 for c in candidatos_corpus if c.item.status == "in-progress")

    return (
        f"**Fila corrente:** `{pai.id}` — {pai.titulo} (`{residencia}`) · fila: — · "
        f"ready {n_ready} · blocked {n_blocked} · in-progress {n_in_progress}"
    )


def _bloco_fila_corrente(modelo: Modelo) -> list[str]:
    """§2.3 (DB-33) — bloco inteiro: a linha `**Fila corrente:**` (metade 1) como primeiro
    elemento, mais um bullet por pai **em corpus** (§2.0, DB-43) com filho não terminal, na
    ordem das linhas do índice. Casamento de plano pela residência única de `_posicao_indice`
    (metade 2) — id exato vence, e na falta dele o sufixo mnemônico; nenhum outro ponto
    reimplementa esse casamento (DB-2)."""
    linhas: list[str] = [_fila_corrente_linha_topo(modelo)]
    for pos, linha_idx in enumerate(modelo.indice):
        alvo: "Plano | Item | None" = None
        tipo = "plano"
        for plano in modelo.planos:
            if plano.fora_do_corpus:
                continue
            if _posicao_indice(modelo, plano.id) == pos:
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
    # newline="\n": o canone do repo e LF em toda parte (`.gitattributes`: `* text=auto
    # eol=lf`, motivo declarado - sem isso o drift-guard `DP-5` entre hub e filho marca toda
    # linha como divergente). Sem o parametro, o modo texto do Windows grava CRLF e todo ato de
    # escrita do instrumento vira o terminador do arquivo tocado (`ESC-27` do `P-0740`).
    tmp.write_text(texto, encoding="utf-8", newline="\n")
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


def _regenerar_bloco_fila(modelo: Modelo, diario_linhas: list[str]) -> str | None:
    """Residência única (`BKL-T10b`, DB-2) da regeneração de `<!-- fila:gerada -->`..
    `<!-- /fila:gerada -->` — chamada por `transacionar_status` e por `transacionar_diretiva`
    (metade 4). Marcador ausente ou fechamento ausente não é erro do chamador: devolve o aviso
    em vez de recusar a transação (`AE-10`/`ESC-27` do `P-0740`); o comportamento não muda."""
    if "<!-- fila:gerada -->" not in diario_linhas:
        return (
            f"bloco `Fila corrente` nao projetado: marcadores `<!-- fila:gerada -->` ausentes em "
            f"{modelo.diario_arquivo} (`AE-10`; chegam com a `BKL-T6` do `P-0739`)"
        )
    ini = diario_linhas.index("<!-- fila:gerada -->")
    fim = next(
        (i for i in range(ini + 1, len(diario_linhas)) if diario_linhas[i] == "<!-- /fila:gerada -->"),
        None,
    )
    if fim is None:
        return f"bloco `Fila corrente` nao projetado: marcador de fechamento ausente em {modelo.diario_arquivo}"
    diario_linhas[ini + 1 : fim] = _bloco_fila_corrente(modelo)
    return None


def checar_transicao(
    modelo: Modelo,
    id_: str,
    estado: str,
    razao: str | None = None,
) -> ResultadoStatus | None:
    """As checagens de `transacionar_status` que não dependem do repositório (`TK-88d`): id,
    E-2, posição de índice do pai, a tabela de §2.7 — com o ramo especial de plano `done` — ,
    `blocked` exige `--razao` e o travessão na razão. `None` quando a transição pode passar;
    quem chama ainda decide a escrita. As checagens de `estado.tsv` (dependem de `repo`)
    continuam só em `transacionar_status`."""
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
    if isinstance(alvo, Plano) and estado == "done":
        # Fechamento de plano (`TK-88`; skill `diario-de-obras`, *Máquina de transições*,
        # gatilho 3): plano não passa por `review` — o aceite é das tarefas —, então o `done`
        # dele sai de `ready`, `in-progress` ou `blocked`, e só quando nenhuma tarefa está
        # aberta e ao menos uma foi entregue. Antes desta regra o instrumento recusava
        # `ready → done` e o fechamento era escrito à mão (medido: `P-0749`, 2026-09-25).
        if atual not in ("ready", "in-progress", "blocked"):
            return ResultadoStatus(1, f"plano {id_} em `{atual}` não fecha como done")
        abertas = [t.id for t in alvo.tarefas if t.status not in ("done", "cancelled")]
        if abertas:
            return ResultadoStatus(
                1, f"plano {id_} tem tarefa(s) não terminal(is): {', '.join(abertas)}"
            )
        if not any(t.status == "done" for t in alvo.tarefas):
            return ResultadoStatus(1, f"plano {id_} sem tarefa done não fecha como done")
    elif (atual, estado) not in _TRANSICOES:
        return ResultadoStatus(1, f"transição fora da tabela de §2.7: {atual} → {estado} para {id_}")

    if estado == "blocked" and not razao:
        return ResultadoStatus(1, "blocked exige --razao")

    if razao and "—" in razao:
        return ResultadoStatus(
            1,
            "razão contém travessão (—, U+2014): o leitor (STATUS_BULLET_RE) usa o "
            "travessão como fronteira entre razão e cauda — escreva --razao sem travessão",
        )

    if estado == "in-progress" and pai is not alvo:
        irmaos = pai.tarefas if tipo_pai == "plano" else pai.filhos
        if any(irmao is not alvo and irmao.status == "in-progress" for irmao in irmaos):
            return ResultadoStatus(1, f"já há item in-progress no mesmo pai: {pai.id}")

    return None


def transacionar_status(
    repo: Path,
    modelo: Modelo,
    id_: str,
    estado: str,
    razao: str | None = None,
    nota: str | None = None,
) -> ResultadoStatus:
    """§2.7 + §3 — `status`/`start`: transição e escrita atômica das projeções, num ato
    só. Nenhuma escrita ocorre antes de todas as checagens (`checar_transicao`, mais a
    consistência de `estado.tsv`, que depende de `repo`) passarem."""
    resultado = checar_transicao(modelo, id_, estado, razao)
    if resultado is not None:
        return resultado

    alvo = _localizar(modelo, id_)
    pai, tipo_pai = _pai_do_alvo(modelo, alvo)

    plano_pasta = alvo if isinstance(alvo, Plano) else next(
        (p for p in modelo.planos if alvo.tipo == "tarefa" and p.arquivo == alvo.arquivo), None
    )
    estado_rel = plano_pasta.estado_arquivo if plano_pasta is not None else None
    if estado_rel is not None:
        if "\t" in (razao or "") or "\t" in (nota or ""):
            return ResultadoStatus(1, "razão ou nota contém TAB: estado.tsv usa TAB como separador")
        estado_path = repo / estado_rel
        estado_linhas = estado_path.read_text(encoding="utf-8").splitlines() if estado_path.is_file() else []
        idx_estado = next(
            (k for k, l in enumerate(estado_linhas) if k > 0 and l.split("\t")[0] == id_), None
        )
        if idx_estado is None:
            return ResultadoStatus(3, f"{id_} sem linha em {estado_rel}")

    # Checagens concluídas — nenhum arquivo tocado até aqui. Muta o modelo em memória
    # (mesmos objetos referenciados por `pai.tarefas`/`pai.filhos`) para que done/total,
    # "próxima" e o bloco `Fila corrente` já reflitam a transição.
    hoje = datetime.date.today().isoformat()
    alvo.status = estado
    alvo.status_razao = razao

    plano_arquivo = alvo.arquivo if (estado_rel is None and (isinstance(alvo, Plano) or alvo.tipo == "tarefa")) else None
    plano_linhas = (repo / plano_arquivo).read_text(encoding="utf-8").splitlines() if plano_arquivo else None
    diario_linhas = list(modelo.diario_linhas)

    if estado_rel is not None:
        estado_linhas[idx_estado] = "\t".join([id_, "plano" if isinstance(alvo, Plano) else "tarefa", estado, razao or "-", hoje, nota if nota is not None else (getattr(alvo, "status_cauda", None) or "-")])
    elif isinstance(alvo, Plano):
        idx = alvo.status_linha - 1
        plano_linhas[idx] = STATUS_CAMPO_RE.sub(f"**Status:** `{estado}`", plano_linhas[idx], count=1)
    else:
        sufixo = f" · {razao}" if razao else ""
        cauda_sufixo = f" — {alvo.status_cauda}" if alvo.status_cauda else ""
        nova_linha = f"- **Status:** `{estado}` · {hoje}{sufixo}{cauda_sufixo}"
        if alvo.tipo == "tarefa":
            plano_linhas[alvo.status_linha - 1] = nova_linha
        else:
            diario_linhas[alvo.status_linha - 1] = nova_linha

    # Nao pode ser None: o guarda de `_posicao_indice` acima ja recusou o caso.
    linha_indice_pai = _linha_indice(modelo, pai.id)
    done, total = _done_total(pai.tarefas if tipo_pai == "plano" else pai.filhos)
    novo_status_bruto = f"{pai.status} {done}/{total}" if total else pai.status
    diario_linhas[linha_indice_pai.linha - 1] = (
        f"| {linha_indice_pai.id} | {linha_indice_pai.titulo} | {novo_status_bruto} | {linha_indice_pai.ancora} |"
    )

    if nota is not None and isinstance(alvo, Item) and estado_rel is None:
        linha_nota = f"  - {hoje} `{estado}` — {nota}"
        _inserir_nota(plano_linhas if alvo.tipo == "tarefa" else diario_linhas, alvo, linha_nota)

    # `AE-10` do `P-0739` / `ESC-27` do `P-0740`: os marcadores do bloco gerado so entram
    # no diario com a `BKL-T6` item (a), e o `P-0739` esta parado (`DM-9`). Projetar o que
    # ainda nao existe nao e erro do chamador — sem os dois marcadores a transacao segue e
    # projeta card + linha de indice, declarando a omissao em `mensagem` (skip silencioso
    # e a classe de defeito que o `TK-55` acumula). Com eles, o bloco e regenerado — residência
    # única em `_regenerar_bloco_fila` (`BKL-T10b`, DB-2).
    aviso = _regenerar_bloco_fila(modelo, diario_linhas)

    arquivos_tocados = [modelo.diario_arquivo]
    _escrever_atomico(repo / modelo.diario_arquivo, diario_linhas)
    if plano_arquivo is not None:
        _escrever_atomico(repo / plano_arquivo, plano_linhas)
        arquivos_tocados.append(plano_arquivo)
    if estado_rel is not None:
        _escrever_atomico(repo / estado_rel, estado_linhas)
        arquivos_tocados.append(estado_rel)

    return ResultadoStatus(0, aviso, sorted(set(arquivos_tocados)))


def _ids_descartados_diretiva(texto: str, ids_reconhecidos: list[str], ids_arvore: set[str]) -> list[str]:
    """TK-65c — id descartado, definição única: texto entre crases na cauda (depois do primeiro
    ` — `) que está em `ids_arvore` e não está entre `ids_reconhecidos` (o que `_parse_diretiva`
    devolveu). Sem repetição, na ordem em que aparece. Crase que não é id de item (`done`,
    `next`, nome de arquivo) não está em `ids_arvore` e não entra."""
    partes = texto.split(" — ", 1)
    cauda = partes[1] if len(partes) > 1 else ""
    descartados: list[str] = []
    for candidato in re.findall(r"`([^`]+)`", cauda):
        if candidato in ids_arvore and candidato not in ids_reconhecidos and candidato not in descartados:
            descartados.append(candidato)
    return descartados


def transacionar_diretiva(repo: Path, modelo: Modelo, texto: str) -> ResultadoStatus:
    """§3 — `diretiva`: reescreve a linha `**Diretiva de priorização:**` e regenera o bloco
    `Fila corrente` na mesma escrita atômica, pela residência única `_regenerar_bloco_fila`
    (`BKL-T10b`, metade 4, DB-2) — a mesma que `transacionar_status` chama. `modelo.diretiva_ids`
    é reconstruído a partir da linha recém-escrita antes da regeneração, para que o vencedor de
    `selecionar_next` usado na linha `Fila corrente` reflita a diretiva nova, não a antiga.

    TK-65c — `diretiva` acusa em vez de recusar: id de item entre crases na cauda (depois do
    primeiro ` — `) que `_parse_diretiva` não leu vira aviso nomeando cada id descartado e a
    contagem de ids reconhecidos antes do ` — `, concatenado por quebra de linha ao aviso de
    `_regenerar_bloco_fila` quando os dois existem. A escrita nunca é recusada por isso."""
    diario_linhas = list(modelo.diario_linhas)
    nova_linha = f"**Diretiva de priorização:** {texto}"
    for i, linha in enumerate(diario_linhas):
        if DIRETIVA_RE.match(linha):
            diario_linhas[i] = nova_linha
            break
    else:
        diario_linhas.insert(1, nova_linha)

    modelo.diretiva_ids = _parse_diretiva(diario_linhas)
    aviso_fila = _regenerar_bloco_fila(modelo, diario_linhas)

    descartados = _ids_descartados_diretiva(texto, modelo.diretiva_ids, _ids_da_arvore(modelo))
    aviso_descarte = None
    if descartados:
        nomes = ", ".join(f"`{id_}`" for id_ in descartados)
        aviso_descarte = (
            f"diretiva: {len(modelo.diretiva_ids)} id(s) reconhecido(s) antes de ' — '; "
            f"id(s) de item descartado(s) na cauda (não lido(s) por `next`): {nomes}"
        )
    avisos = [a for a in (aviso_descarte, aviso_fila) if a]
    aviso = "\n".join(avisos) if avisos else None

    _escrever_atomico(repo / modelo.diario_arquivo, diario_linhas)
    return ResultadoStatus(0, aviso, [modelo.diario_arquivo])


def transacionar_drain(
    repo: Path,
    modelo: Modelo,
    inbox_planos: Path,
    historico: Path,
    data: str | None = None,
) -> ResultadoStatus:
    """BKL-T10a, §2.4 — cada linha viva do inbox de planos vira linha de índice do diário e é
    movida verbatim (prefixada `- [drenado AAAA-MM-DD] `) para o histórico, que só recebe
    apenso e nunca é lido (`DB-9`). Contador do inbox recalculado como `max(id visto) + 1` sobre
    os ids `P-NNNN` referenciados no próprio inbox — o histórico nunca é lido, então não entra
    na conta. Checagem antes de qualquer escrita (`DB-1`/`DB-37`): inbox sem linha viva é no-op
    exit 0; plano referido sem `Status` ou sem `Prefixo` é exit 3, nomeando o arquivo, e nada é
    tocado — nem a linha boa que vinha antes dele no mesmo inbox. A regeneração do bloco `Fila
    corrente` reusa `_regenerar_bloco_fila`, a mesma residência única que `transacionar_status`
    e `transacionar_diretiva` chamam (`DB-2`) — `drain` é mais um chamador dela, não uma segunda
    implementação da escrita do bloco."""
    if not inbox_planos.exists():
        return ResultadoStatus(0, None, [])

    texto_inbox = inbox_planos.read_text(encoding="utf-8")
    linhas_inbox = texto_inbox.splitlines()

    vivas: list[tuple[int, str, str]] = []
    for i, linha in enumerate(linhas_inbox):
        s = linha.strip()
        if not s.startswith("- ") or s.startswith("- [drenado "):
            continue
        m = _CAMINHO_PLANO_INBOX_RE.search(s)
        if m:
            vivas.append((i, s, m.group(0)))

    if not vivas:
        return ResultadoStatus(0, None, [])

    # Checagem antes de qualquer escrita (DB-37/DB-1): todo plano referido tem de trazer
    # Status e Prefixo antes que a primeira linha seja movida.
    drenos: list[tuple[int, str, Plano]] = []
    for i, linha, caminho in vivas:
        plano = next((p for p in modelo.planos if p.arquivo == caminho), None)
        if plano is None or plano.status is None or plano.prefixo is None:
            return ResultadoStatus(3, f"plano sem Prefixo ou sem Status para linha de índice: {caminho}")
        drenos.append((i, linha, plano))

    hoje = data if data else datetime.date.today().isoformat()
    ids_vistos = [int(m.group(1)) for m in _ID_PLANO_INBOX_RE.finditer(texto_inbox)]
    novo_id = max(ids_vistos) + 1
    m_contador = _CONTADOR_INBOX_ID_RE.search(texto_inbox)
    largura = len(m_contador.group(1)) if m_contador else 1

    # Diário: uma linha de índice nova por plano drenado, na ordem do inbox. O modelo em
    # memória (`modelo.indice`, `plano.fora_do_corpus`) é atualizado junto, para que
    # `_bloco_fila_corrente` (chamado por `_regenerar_bloco_fila` abaixo) já enxergue os
    # planos recém-drenados — mesmo casamento por sufixo de `_posicao_indice` (DB-2).
    diario_linhas = list(modelo.diario_linhas)
    inicio_secao = next(k for k, l in enumerate(diario_linhas) if INDICE_HEADING_RE.match(l))
    inicio_tabela = next(k for k in range(inicio_secao + 1, len(diario_linhas)) if diario_linhas[k].startswith("|"))
    fim_tabela = next(
        (k for k in range(inicio_tabela, len(diario_linhas)) if diario_linhas[k].strip() == ""),
        len(diario_linhas),
    )

    novas_linhas_indice = []
    for _, _, plano in drenos:
        id_indice = f"{plano.id}-{plano.prefixo}"
        novas_linhas_indice.append(f"| {id_indice} | {plano.titulo} | {plano.status} | {plano.arquivo} |")
        nucleo, _, _ = _celula_indice(plano.status)
        plano.fora_do_corpus = nucleo in {"done", "superseded", "cancelled"}
        modelo.indice.append(
            LinhaIndice(
                id=id_indice,
                titulo=plano.titulo,
                status_bruto=plano.status,
                arquivo=modelo.diario_arquivo,
                linha=fim_tabela + 1,
                ancora=plano.arquivo,
            )
        )
    diario_linhas[fim_tabela:fim_tabela] = novas_linhas_indice

    aviso = _regenerar_bloco_fila(modelo, diario_linhas)

    # Inbox: remove as linhas drenadas e recalcula o contador.
    indices_remover = {i for i, _, _ in drenos}
    linhas_novo_inbox = [l for k, l in enumerate(linhas_inbox) if k not in indices_remover]
    linhas_novo_inbox = [
        _CONTADOR_INBOX_RE.sub(f"**Próximo id de plano: {_caminhos.formatar_id(novo_id, largura)}.**", l)
        if _CONTADOR_INBOX_RE.search(l)
        else l
        for l in linhas_novo_inbox
    ]

    # Histórico: apenso verbatim (só o prefixo `- ` vira `- [drenado AAAA-MM-DD] `), na ordem
    # do inbox; o arquivo nunca é lido pelo instrumento (DB-9), só apensado.
    linhas_historico = historico.read_text(encoding="utf-8").splitlines() if historico.exists() else []
    for _, linha, _ in drenos:
        linhas_historico.append(f"- [drenado {hoje}] " + linha[2:])

    _escrever_atomico(repo / modelo.diario_arquivo, diario_linhas)
    _escrever_atomico(inbox_planos, linhas_novo_inbox)
    _escrever_atomico(historico, linhas_historico)

    arquivos = sorted(
        {
            modelo.diario_arquivo,
            inbox_planos.relative_to(repo).as_posix(),
            historico.relative_to(repo).as_posix(),
        }
    )
    return ResultadoStatus(0, aviso, arquivos)


def _ultima_linha_stderr(texto: str) -> str:
    linhas = texto.splitlines()
    return linhas[-1] if linhas else ""


def despachar(repo: Path, id_: str, mundo: str | None = None) -> ResultadoStatus:
    """AF-T10 (`DAF-41`) — um comando roda as conferências do despacho do passo 3/4 de
    `.claude/skills/scrum-master/SKILL.md` (tarefa, `modelo.py check`, `card_check.py`,
    `pytest --co`, captura do `<ref>`, materialização em `in-progress`), nesta ordem, recusando
    pela primeira que falhar e sem escrever nada até a última checagem passar. `modelo.py`,
    `card_check.py` e `review_evidence.py` rodam como subprocessos do irmão em
    `Path(__file__).parent` (`sys.executable`), nunca por `import`.

    `mundo` (`AE-26` do `P-0753`) repassa `--mundo` ao `card_check`: `depois` é o redespacho de
    tarefa cuja entrega já está na árvore (só-verificações); ausente, o `card_check` deriva."""

    def _recusar(gate: str, razao: str) -> ResultadoStatus:
        print(f"despachar: recusado — {gate}: {razao}", file=sys.stderr)
        return ResultadoStatus(1, razao)

    modelo = carregar(repo)
    alvo = _localizar(modelo, id_)
    if not isinstance(alvo, Item) or alvo.tipo != "tarefa":
        return _recusar("tarefa", f"{id_} não é tarefa de plano")
    if alvo.status != "ready":
        return _recusar("tarefa", f"{id_} está {alvo.status}, não ready")

    pai, tipo_pai = _pai_do_alvo(modelo, alvo)
    irmao = Path(__file__).resolve().parent
    # `--plano` absoluto (`repo / pai.arquivo`): `card_check.verificar_tarefa` usa `Path(plano)`
    # direto, sem juntar com `--root` — relativo dependeria do cwd do subprocesso, que este
    # comando não fixa (`modelo.py` aceita os dois por `_resolver_plano`, mas o absoluto serve
    # aos dois irmãos sem depender de onde o processo-pai foi invocado).
    plano_abs = str(repo / pai.arquivo)

    # `DAF-42` (`AE-14`): os irmãos escrevem o stderr em UTF-8; sem `encoding` explícito o
    # texto sai na codificação do locale (cp1252 no Windows) — razão com mojibake, ou stderr
    # `None` quando um byte UTF-8 não existe em cp1252. Vale para os quatro `subprocess.run`.
    resultado_modelo = subprocess.run(
        [sys.executable, str(irmao / "modelo.py"), "check", "--plano", plano_abs, "--root", str(repo)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if resultado_modelo.returncode not in (0, 2):
        return _recusar("modelo", _ultima_linha_stderr(resultado_modelo.stderr))

    resultado_cc = subprocess.run(
        [
            sys.executable,
            str(irmao / "card_check.py"),
            "--plano",
            plano_abs,
            "--tarefa",
            id_,
            "--root",
            str(repo),
            *(["--mundo", mundo] if mundo else []),
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if resultado_cc.returncode != 0:
        return _recusar("card_check", _ultima_linha_stderr(resultado_cc.stderr))

    resultado_pytest = subprocess.run(
        [sys.executable, "-m", "pytest", "--co", "-q"],
        cwd=str(repo),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if resultado_pytest.returncode not in (0, 5):
        return _recusar("pytest --co", f"exit {resultado_pytest.returncode}")

    estado_path = repo / ".claude" / "estado" / "tarefa-corrente.json"
    ref: str | None = None
    if estado_path.is_file():
        try:
            dados_existentes = json.loads(estado_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            dados_existentes = {}
        if dados_existentes.get("tarefa") == id_ and dados_existentes.get("ref"):
            ref = dados_existentes["ref"]
    if ref is None:
        resultado_ref = subprocess.run(
            [sys.executable, str(irmao / "review_evidence.py"), "--capturar-ref", "--root", str(repo)],
            capture_output=True,
            text=True,
        encoding="utf-8",
        errors="replace",
        )
        if resultado_ref.returncode != 0:
            return _recusar("ref", _ultima_linha_stderr(resultado_ref.stderr))
        linhas_stdout = [linha for linha in resultado_ref.stdout.splitlines() if linha.strip()]
        ref = linhas_stdout[-1]

    resultado_status = transacionar_status(
        repo, modelo, id_, "in-progress", nota="despachada por backlog.py despachar"
    )
    if resultado_status.exit_code != 0:
        return _recusar("status", resultado_status.mensagem or "")

    estado_path.parent.mkdir(parents=True, exist_ok=True)
    dados = {
        "tarefa": id_,
        "projeto": repo.name,
        "modelo": alvo.modelo,
        "plano": pai.arquivo,
        "despachado_em": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "ref": ref,
    }
    estado_path.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"=== DESPACHO: {id_} — {alvo.titulo}")
    for autor, texto_handover in handovers_para(pai, tipo_pai, alvo):
        print(f"=== HANDOVER DE {autor.id} — {autor.titulo} ({autor.status}; {autor.arquivo})")
        print(texto_handover)
    print(show(modelo, id_))
    print(f"ref={ref}")

    return ResultadoStatus(0)


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

    drain_parser = subparsers.add_parser("drain", help="Inbox de planos → índice do diário + histórico.")
    drain_parser.add_argument("--data", default=None)
    drain_parser.add_argument("--repo", default=None)

    despachar_parser = subparsers.add_parser(
        "despachar", help="Roda as conferências do despacho e recusa pela primeira que falhar."
    )
    despachar_parser.add_argument("id")
    despachar_parser.add_argument(
        "--mundo",
        choices=["antes", "depois"],
        default=None,
        help="Repassado ao card_check; 'depois' redespacha tarefa cuja entrega já está na árvore.",
    )
    despachar_parser.add_argument("--repo", default=None)

    for fluxo in (sys.stdout, sys.stderr):
        if hasattr(fluxo, "reconfigure"):
            fluxo.reconfigure(encoding="utf-8")

    args = parser.parse_args(argv)

    repo = resolve_repo(args.repo)
    modelo = carregar(repo)

    if args.comando == "check":
        inbox_planos = _caminhos.inbox_planos(repo)
        piso_c11, violacoes = ler_piso_c11(repo)
        violacoes += check(modelo, inbox_planos=inbox_planos, repo=repo, piso_c11=piso_c11, dossie=True)
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
                Path(args.inbox_planos).resolve() if args.inbox_planos else _caminhos.inbox_planos(repo)
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
            if resultado.mensagem:
                print(resultado.mensagem)
            return 0
        print(resultado.mensagem, file=sys.stderr if resultado.exit_code == 3 else sys.stdout)
        return resultado.exit_code

    if args.comando == "diretiva":
        resultado = transacionar_diretiva(repo, modelo, args.texto)
        print(f"diretiva atualizada. arquivos tocados: {', '.join(resultado.arquivos)}")
        if resultado.mensagem:
            print(resultado.mensagem)
        return 0

    if args.comando == "drain":
        inbox_planos = _caminhos.inbox_planos(repo)
        historico = repo / "docs" / "plans" / "_INBOX_HISTORICO.md"
        resultado = transacionar_drain(repo, modelo, inbox_planos, historico, data=args.data)
        if resultado.exit_code == 0:
            if resultado.arquivos:
                print(f"drain: arquivos tocados: {', '.join(resultado.arquivos)}")
            else:
                print("drain: nada por drenar (no-op).")
            if resultado.mensagem:
                print(resultado.mensagem)
            return 0
        print(resultado.mensagem, file=sys.stderr if resultado.exit_code == 3 else sys.stdout)
        return resultado.exit_code

    if args.comando == "despachar":
        resultado = despachar(repo, args.id, mundo=args.mundo)
        return resultado.exit_code

    parser.error(f"comando desconhecido: {args.comando}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
