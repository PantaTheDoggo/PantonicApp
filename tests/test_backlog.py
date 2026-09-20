"""BKL-T2 (`docs/plans/P-0739-backlog-instrumento.md` `### BKL-T2`) — TF/TR do núcleo
somente-leitura de `.claude/tools/backlog.py`: parser, `check` (violações `C-1..C-9`) e `show`
(dossiê verbatim truncado ao teto `DB-7`).

`.claude/tools/` não é pacote importável (diretório com ponto no nome) — o módulo é carregado por
caminho via `importlib.util.spec_from_file_location`, mesmo padrão de `tests/test_telemetria.py`
para `.claude/tools/telemetria.py`.

Todas as asserções trabalham sobre fixtures em `tests/fixtures/backlog/{verde,vermelho}/` copiadas
para `tmp_path` — nunca contra o repositório real (`docs/DIARIO_DE_OBRAS.md` e `docs/plans/` são
insumo, nunca alvo desta suíte)."""
from __future__ import annotations

import hashlib
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_BACKLOG_PATH = _ROOT / ".claude" / "tools" / "backlog.py"
_HOOK_PATH = _ROOT / ".claude" / "tools" / "backlog_hook.py"
_FIXTURES = Path(__file__).resolve().parent / "fixtures" / "backlog"
_FIXTURE_VERDE = _FIXTURES / "verde"
_FIXTURE_VERMELHO = _FIXTURES / "vermelho"
_FIXTURE_NEXT_TK90 = _FIXTURES / "next_tk90"
_FIXTURE_NEXT_TK90_SEM_INDICE = _FIXTURES / "next_tk90_sem_indice"
_FIXTURE_INBOX_PLANOS = _FIXTURES / "inbox_planos" / "_INBOX.md"
_FIXTURE_CORPUS = _FIXTURES / "corpus"
_FIXTURE_CONTADOR_INBOX = _FIXTURES / "contador_inbox"
_FIXTURE_CITACAO_SECAO = _FIXTURES / "citacao_secao"
_FIXTURE_CANDIDATO_A_FECHAMENTO = _FIXTURES / "candidato_a_fechamento"


def _load_backlog():
    spec = importlib.util.spec_from_file_location("backlog", _BACKLOG_PATH)
    module = importlib.util.module_from_spec(spec)
    # Dataclasses com `from __future__ import annotations` resolvem anotações via
    # `sys.modules[cls.__module__]` — precisa estar registrado antes do exec_module.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _copiar_fixture(origem: Path, destino: Path) -> Path:
    shutil.copytree(origem, destino)
    return destino


def _load_hook():
    spec = importlib.util.spec_from_file_location("backlog_hook", _HOOK_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _montar_raiz_hook(base: Path, nome: str, fonte_hook: str) -> Path:
    """Raiz falsa em `base/nome` para relocar o acoplamento por `__file__` de `backlog_hook.py`
    (TK-63a — substitui o shim de `__file__` preservado, que a devolução anterior apontou como
    acoplamento ao diário e aos planos reais). Copiada de `_FIXTURE_NEXT_TK90` — fornece
    `docs/DIARIO_DE_OBRAS.md` e `docs/plans/_INBOX.md` para o `next` real ter o que ler — com
    `.claude/tools/backlog_hook.py` (fonte injetada, para poder trocar pelo produto revertido) e
    `.claude/tools/backlog.py` (cópia do arquivo real via `shutil.copy2`). Basta: `_carregar_backlog`
    resolve `backlog.py` como irmão de `__file__`, e `resolve_repo(None)` (em `backlog.py`) resolve
    a raiz a partir de onde o próprio `backlog.py` está — o acoplamento se fecha dentro da raiz
    falsa. Mesma técnica do `telemetria_hook` na `TK-56b` (aprovada 100%)."""
    raiz = _copiar_fixture(_FIXTURE_NEXT_TK90, base / nome)
    tools_dir = raiz / ".claude" / "tools"
    tools_dir.mkdir(parents=True)
    (tools_dir / "backlog_hook.py").write_text(fonte_hook, encoding="utf-8")
    shutil.copy2(_BACKLOG_PATH, tools_dir / "backlog.py")
    return raiz


def _hashes(repo: Path) -> dict[str, str]:
    return {
        str(caminho.relative_to(repo)): hashlib.sha256(caminho.read_bytes()).hexdigest()
        for caminho in repo.rglob("*")
        if caminho.is_file()
    }


def _mudar_linha_unica(repo: Path, relpath: str, velha: str, nova: str) -> None:
    """Troca uma linha por outra numa cópia de fixture em `tmp_path` — nunca na fixture do
    repositório. `velha` tem de ser única no arquivo (mesmo padrão de `_indice_com_sufixo`)."""
    caminho = repo / relpath
    texto = caminho.read_text(encoding="utf-8")
    assert texto.count(velha) == 1, f"linha não é única (ou ausente) em {relpath}: {velha!r}"
    caminho.write_text(texto.replace(velha, nova, 1), encoding="utf-8")


def _inserir_linhas_indice(repo: Path, linhas_novas: list[str]) -> None:
    """Acrescenta linhas à tabela do índice da fixture `corpus`, logo depois da linha do
    `TK-1` — sempre sobre a cópia em `tmp_path`, nunca na fixture do repositório."""
    ancora = "| TK-1 | Tiquete base | ready | docs/DIARIO_DE_OBRAS.md#tk-1 |\n"
    _mudar_linha_unica(
        repo, "docs/DIARIO_DE_OBRAS.md", ancora.rstrip("\n"), ancora.rstrip("\n") + "\n" + "\n".join(linhas_novas)
    )


def _inserir_bloco_gerado(repo: Path) -> None:
    """Prepara a cópia da fixture para os TF de escrita da `BKL-T4`: a fixture
    `next_tk90` não carrega os marcadores `<!-- fila:gerada -->`/`<!-- /fila:gerada -->`
    ainda — `status`/`start` são os primeiros verbos de escrita do instrumento (§2.3) —
    então o próprio TF os insere na cópia em `tmp_path`, nunca na fixture do repositório."""
    diario = repo / "docs" / "DIARIO_DE_OBRAS.md"
    linhas = diario.read_text(encoding="utf-8").splitlines()
    linhas[1:1] = ["<!-- fila:gerada -->", "<!-- /fila:gerada -->"]
    diario.write_text("\n".join(linhas) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- #
# TF parser — 3 formas de ID (DB-14), campo Status com/sem razão, heading legado
# --------------------------------------------------------------------------- #


def test_tf_parser_tres_formas_de_id_db14():
    backlog = _load_backlog()
    linhas = [
        "### T7 — Tarefa sem prefixo [Sonnet · classe mecanica]",
        "- **Status:** `done` · 2026-01-01",
        "",
        "### BKL-T2 — Tarefa com prefixo [Sonnet · classe implementacao]",
        "- **Status:** `ready` · 2026-01-01",
        "",
        "### TK-54a — Subtarefa de tíquete [Opus · classe investigacao]",
        "- **Status:** `ready` · 2026-01-01",
    ]
    itens = backlog._scan_items(linhas, "arquivo.md")
    ids_e_tipos = {(it.id, it.tipo) for it in itens}
    assert ("T7", "tarefa") in ids_e_tipos
    assert ("BKL-T2", "tarefa") in ids_e_tipos
    assert ("TK-54a", "subtarefa") in ids_e_tipos
    assert all(it.header_valido for it in itens)


def test_tf_status_com_e_sem_razao():
    backlog = _load_backlog()
    linhas_com_razao = [
        "### T1 — X [Sonnet · classe mecanica]",
        "- **Status:** `blocked` · 2026-02-02 · aguardando dono",
    ]
    linhas_sem_razao = [
        "### T1 — X [Sonnet · classe mecanica]",
        "- **Status:** `ready` · 2026-02-02",
    ]
    item_com = backlog._scan_items(linhas_com_razao, "a.md")[0]
    item_sem = backlog._scan_items(linhas_sem_razao, "a.md")[0]
    assert item_com.status == "blocked"
    assert item_com.status_razao == "aguardando dono"
    assert item_sem.status == "ready"
    assert item_sem.status_razao is None


def test_tf_heading_legado_sem_bracket_e_c1():
    backlog = _load_backlog()
    linhas = [
        "### TK-54a — O extrato [classe investigacao]",  # sem <modelo> · — forma real do repo
        "- **Status:** `ready` · 2026-01-01",
    ]
    item = backlog._scan_items(linhas, "arquivo.md")[0]
    assert item.tipo == "subtarefa"
    assert item.id == "TK-54a"
    assert item.header_valido is False


# --------------------------------------------------------------------------- #
# TF check — vermelho dispara C-1..C-9 uma vez cada; verde não dispara nada
# --------------------------------------------------------------------------- #


def test_tf_check_vermelho_dispara_cada_codigo_uma_vez(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERMELHO, tmp_path / "repo")

    modelo = backlog.carregar(repo)
    violacoes = backlog.check(modelo)

    codigos = [v.codigo for v in violacoes]
    esperados = [f"C-{n}" for n in range(1, 10)]
    assert sorted(codigos) == sorted(esperados)
    for v in violacoes:
        assert v.arquivo and v.linha > 0 and v.texto


def test_tf_check_verde_sem_violacoes(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")

    modelo = backlog.carregar(repo)
    violacoes = backlog.check(modelo)

    assert violacoes == []


# --------------------------------------------------------------------------- #
# TF/TR C-10 — contador do inbox (`docs/plans/_INBOX.md`) confrontado com o maior id
# presente em `docs/plans/P-*.md`. Caso medido: contador em `P-0742` com
# `docs/plans/P-0742-loop-fora-do-llm.md` já na árvore, sem nenhuma linha viva no inbox
# apontando para `P-0742` — a fixture `contador_inbox` reproduz exatamente essa forma
# (nenhum caminho `P-0742` mencionado no texto do inbox), para que a guarda C-10 só passe
# se ler `docs/plans/P-*.md`, nunca os ids do próprio texto do inbox.
# --------------------------------------------------------------------------- #


def test_tf_c10_contador_do_inbox_aponta_para_id_ja_usado(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_CONTADOR_INBOX, tmp_path / "repo")

    modelo = backlog.carregar(repo)
    violacoes = backlog.check(modelo, inbox_planos=repo / "docs" / "plans" / "_INBOX.md")

    c10 = [v for v in violacoes if v.codigo == "C-10"]
    assert len(c10) == 1
    assert c10[0].arquivo == "docs/plans/_INBOX.md" and c10[0].linha > 0 and "P-0742" in c10[0].texto


def test_tr_c10_contador_do_inbox_aponta_para_id_livre_nao_dispara(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_CONTADOR_INBOX, tmp_path / "repo")
    _mudar_linha_unica(
        repo,
        "docs/plans/_INBOX.md",
        "**Próximo id de plano: P-0742.**",
        "**Próximo id de plano: P-0743.**",
    )

    modelo = backlog.carregar(repo)
    violacoes = backlog.check(modelo, inbox_planos=repo / "docs" / "plans" / "_INBOX.md")

    assert not any(v.codigo == "C-10" for v in violacoes)


# --------------------------------------------------------------------------- #
# TK-60a — TF/TR de `resolver_citacao_secao`: terceiro resolvedor de referência do kit
# (caminho já tem Test-Path, identificador de tarefa tem review_evidence). Gramática real
# do kit: `` `<arquivo>.md` §<N>[.<N>]* `` (item 1). Fixture `citacao_secao` reproduz o
# caso real medido no `TK-60`: `.claude/skills/diario-de-obras/SKILL.fixture.md` (renomeada
# do nome real da skill, item 8 — o harness a listava como skill invocável) não tem heading
# numerado nenhum, mas carrega o literal `2.5` em prosa — a armadilha que um casamento por
# substring deixaria passar; `docs/plans/P-0900-exemplo.md` tem o heading real `### 2.5 ...`,
# caso positivo do par presença-ausência.
# --------------------------------------------------------------------------- #


def test_tf_resolver_citacao_secao_par_presenca_ausencia(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_CITACAO_SECAO, tmp_path / "repo")

    ausente = backlog.resolver_citacao_secao(
        "`.claude/skills/diario-de-obras/SKILL.fixture.md` §2.5", repo
    )
    presente = backlog.resolver_citacao_secao("`docs/plans/P-0900-exemplo.md` §2.5", repo)

    assert presente is None
    assert ausente is not None
    assert ausente.codigo == "C-11"
    assert "`.claude/skills/diario-de-obras/SKILL.fixture.md` §2.5" in ausente.texto


def test_tr_resolver_citacao_secao_nao_casa_por_substring(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_CITACAO_SECAO, tmp_path / "repo")
    caminho = repo / ".claude" / "skills" / "diario-de-obras" / "SKILL.fixture.md"
    texto = caminho.read_text(encoding="utf-8")

    # a armadilha: o literal existe no arquivo, fora de qualquer heading.
    assert "2.5" in texto
    assert not any(re.match(r"^#{1,6}\s+2\.5\b", linha) for linha in texto.splitlines())

    violacao = backlog.resolver_citacao_secao(
        "`.claude/skills/diario-de-obras/SKILL.fixture.md` §2.5", repo
    )

    assert violacao is not None
    assert violacao.codigo == "C-11"


def test_tr_resolver_citacao_secao_item5_arquivo_ausente_ou_ambiguo_devolve_none(tmp_path):
    """Item 5 (TK-60b): `_resolver_arquivo_citado` devolvendo `None` (arquivo que não existe
    nem por basename, ou basename ambíguo — mais de um arquivo com o mesmo nome no repo) faz
    `resolver_citacao_secao` devolver `None` em silêncio, não `C-11` — resolver caminho é do
    `Test-Path` (`DB-2`), não deste resolvedor. Citação a arquivo existente com seção ausente
    segue saindo `C-11` (terceiro braço do par presença-ausência)."""
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_CITACAO_SECAO, tmp_path / "repo")

    ausente = backlog.resolver_citacao_secao(
        "`docs/nao-existe-em-lugar-nenhum.md` §2", repo
    )
    assert ausente is None

    # basename ambíguo: duplica o arquivo citado em outro diretório da cópia (nunca na
    # fixture do repositório) para que a caminhada encontre dois achados.
    (repo / "docs" / "outra-pasta").mkdir(parents=True)
    (repo / "docs" / "outra-pasta" / "P-0900-exemplo.md").write_text(
        (repo / "docs" / "plans" / "P-0900-exemplo.md").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    ambiguo = backlog.resolver_citacao_secao("`P-0900-exemplo.md` §2.5", repo)
    assert ambiguo is None

    existente_secao_ausente = backlog.resolver_citacao_secao(
        "`.claude/skills/diario-de-obras/SKILL.fixture.md` §2.5", repo
    )
    assert existente_secao_ausente is not None
    assert existente_secao_ausente.codigo == "C-11"


def test_tr_resolver_citacao_secao_dominio_um_nivel():
    """Defeito medido nesta rodada (item 2, TK-60a): a gramática anterior exigia
    `\\d+(?:\\.\\d+)+` (dois níveis ou mais) e reprovava as 772 citações de um nível do
    corpus real. `§3` contra `GOVERNANCA.md`, `§8` contra `docs/RUBRICA_DE_REVISAO.md` e
    `§9` contra `docs/consultant-spec.md` resolvem (`None`); antes da correção os três
    saíam `C-11`."""
    backlog = _load_backlog()

    assert backlog.resolver_citacao_secao("`GOVERNANCA.md` §3", _ROOT) is None
    assert backlog.resolver_citacao_secao("`docs/RUBRICA_DE_REVISAO.md` §8", _ROOT) is None
    assert backlog.resolver_citacao_secao("`docs/consultant-spec.md` §9", _ROOT) is None


# --------------------------------------------------------------------------- #
# BKL-T10 (`docs/plans/P-0739-backlog-instrumento.md` `### BKL-T10`) — TF do corpus
# (`DB-43`) e da célula de item terminal (`DB-46`). Fixture `corpus`: `P-0900` (índice
# `ready`, cabeçalho sem `Status`/`Prefixo`), `P-0777-XYZ` (índice `done`, sufixo
# mnemônico, cabeçalho `ready` — diverge de propósito), `TK-1` (limpo) e uma tabela
# markdown ilustrativa fora de `## Índice`, dentro da prosa do `TK-1`.
# --------------------------------------------------------------------------- #


def test_tf_plano_terminal_no_indice_sai_do_corpus_do_check(tmp_path):
    backlog = _load_backlog()

    repo_vivo = _copiar_fixture(_FIXTURE_CORPUS, tmp_path / "repo_vivo")
    violacoes_vivo = backlog.check(backlog.carregar(repo_vivo))
    assert any(v.arquivo == "docs/plans/P-0900-legado.md" for v in violacoes_vivo)

    repo_terminal = _copiar_fixture(_FIXTURE_CORPUS, tmp_path / "repo_terminal")
    _mudar_linha_unica(
        repo_terminal,
        "docs/DIARIO_DE_OBRAS.md",
        "| P-0900 | Plano legado | ready | docs/plans/P-0900-legado.md |",
        "| P-0900 | Plano legado | done | docs/plans/P-0900-legado.md |",
    )
    violacoes_terminal = backlog.check(backlog.carregar(repo_terminal))
    assert not any(v.arquivo == "docs/plans/P-0900-legado.md" for v in violacoes_terminal)


def test_tf_plano_terminal_no_indice_nao_produz_candidato(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_CORPUS, tmp_path / "repo")
    _mudar_linha_unica(
        repo,
        "docs/DIARIO_DE_OBRAS.md",
        "| P-0900 | Plano legado | ready | docs/plans/P-0900-legado.md |",
        "| P-0900 | Plano legado | superseded | docs/plans/P-0900-legado.md |",
    )
    modelo = backlog.carregar(repo)

    candidatos = backlog._candidatos(modelo)
    assert all(c.item.id != "LEG-T1" for c in candidatos)

    selecao = backlog.selecionar_next(modelo)
    assert selecao.exit_code != 3


def test_tf_show_le_plano_fora_do_corpus(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_CORPUS, tmp_path / "repo")
    modelo = backlog.carregar(repo)

    dossie = backlog.show(modelo, "GAM-T1")

    assert "não encontrado" not in dossie
    assert "GAM-T1" in dossie


def test_tf_tabela_alheia_nao_vira_linha_de_indice(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_CORPUS, tmp_path / "repo")
    modelo = backlog.carregar(repo)

    ids_indice = {l.id for l in modelo.indice}
    assert "X-1" not in ids_indice
    assert {"P-0900", "P-0777-XYZ", "TK-1"} <= ids_indice

    violacoes = backlog.check(modelo)
    assert not any("X-1" in v.texto for v in violacoes)


def test_tf_c5_casa_plano_por_sufixo_do_indice(tmp_path):
    backlog = _load_backlog()

    repo_diverge = _copiar_fixture(_FIXTURE_CORPUS, tmp_path / "repo_diverge")
    violacoes = backlog.check(backlog.carregar(repo_diverge))
    assert len([v for v in violacoes if v.codigo == "C-5" and "P-0777-XYZ" in v.texto]) == 1

    repo_igual = _copiar_fixture(_FIXTURE_CORPUS, tmp_path / "repo_igual")
    _mudar_linha_unica(
        repo_igual,
        "docs/plans/P-0777-gama.md",
        "**Status:** `ready` · **Prefixo das tarefas no diário:** `GAM-T<n>`",
        "**Status:** `done` · **Prefixo das tarefas no diário:** `GAM-T<n>`",
    )
    violacoes2 = backlog.check(backlog.carregar(repo_igual))
    assert not any(v.codigo == "C-5" and "P-0777-XYZ" in v.texto for v in violacoes2)


def test_tf_c4_nao_vale_para_celula_de_item_terminal(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_CORPUS, tmp_path / "repo")
    _inserir_linhas_indice(
        repo,
        [
            "| X-2 | Nota terminal | done *(nota idêntica em ambas)* | docs/DIARIO_DE_OBRAS.md#x-2 |",
            "| X-3 | Nota viva | ready *(nota idêntica em ambas)* | docs/DIARIO_DE_OBRAS.md#x-3 |",
        ],
    )
    violacoes = backlog.check(backlog.carregar(repo))
    ids_com_c4 = {v.texto.split(":", 1)[0] for v in violacoes if v.codigo == "C-4"}

    assert "X-3" in ids_com_c4
    assert "X-2" not in ids_com_c4


def test_tf_c9_aceita_cancelled_como_terminal(tmp_path):
    backlog = _load_backlog()

    repo_cancelled = _copiar_fixture(_FIXTURE_CORPUS, tmp_path / "repo_cancelled")
    _inserir_linhas_indice(repo_cancelled, ["| X-9 | Fantasma cancelado | cancelled | docs/DIARIO_DE_OBRAS.md#x-9 |"])
    violacoes_cancelled = backlog.check(backlog.carregar(repo_cancelled))
    assert not any(v.codigo == "C-9" and v.texto.startswith("X-9") for v in violacoes_cancelled)

    repo_ready = _copiar_fixture(_FIXTURE_CORPUS, tmp_path / "repo_ready")
    _inserir_linhas_indice(repo_ready, ["| X-9 | Fantasma vivo | ready | docs/DIARIO_DE_OBRAS.md#x-9 |"])
    violacoes_ready = backlog.check(backlog.carregar(repo_ready))
    assert any(v.codigo == "C-9" and v.texto.startswith("X-9") for v in violacoes_ready)


# --------------------------------------------------------------------------- #
# TF show — trunca em 8.000 chars / 120 linhas com ponteiro arquivo:l1-l2
# --------------------------------------------------------------------------- #


def test_tf_show_trunca_em_8000_chars_120_linhas_com_ponteiro():
    backlog = _load_backlog()
    linhas_geradas = [f"linha {i:03d} de conteúdo qualquer para encher o dossiê de teste" for i in range(1, 201)]
    texto = "\n".join(linhas_geradas)
    plano = backlog.Plano(
        id="P-9000",
        titulo="Longo",
        arquivo="docs/plans/P-9000-longo.md",
        linha_header=1,
        linha_fim=200,
        texto=texto,
        status="ready",
        prefixo="LNG",
    )
    modelo = backlog.Modelo(planos=[plano], tiquetes=[], indice=[], diario_arquivo="docs/DIARIO_DE_OBRAS.md")

    saida = backlog.show(modelo, "P-9000")

    assert len(saida) < len(texto)
    assert "linha 001" in saida
    assert "linha 200" not in saida
    assert "docs/plans/P-9000-longo.md:1-200" in saida
    assert len(saida) <= 8000 + 200
    assert len(saida.splitlines()) <= 121


def test_tf_show_id_desconhecido():
    backlog = _load_backlog()
    modelo = backlog.Modelo(planos=[], tiquetes=[], indice=[], diario_arquivo="docs/DIARIO_DE_OBRAS.md")
    assert "não encontrado" in backlog.show(modelo, "P-0000")


# --------------------------------------------------------------------------- #
# TR — carregar nunca abre *_HISTORICO.md
# --------------------------------------------------------------------------- #


def test_tr_carregar_nunca_abre_historico(tmp_path, monkeypatch):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")

    # Decoys que carregar() jamais deveria tocar (histórico é append-only e nunca lido, DB-9).
    (repo / "docs" / "DIARIO_HISTORICO.md").write_text("PROIBIDO", encoding="utf-8")
    (repo / "docs" / "plans" / "_INBOX_HISTORICO.md").write_text("PROIBIDO", encoding="utf-8")

    original_open = Path.open

    def _open_guardado(self, *args, **kwargs):
        if "_HISTORICO" in str(self):
            raise AssertionError(f"carregar() abriu um histórico proibido: {self}")
        return original_open(self, *args, **kwargs)

    monkeypatch.setattr(Path, "open", _open_guardado)

    modelo = backlog.carregar(repo)

    assert len(modelo.planos) == 2


# --------------------------------------------------------------------------- #
# BKL-T3 (`docs/plans/P-0739-backlog-instrumento.md` `### BKL-T3`) — TF/TR do verbo
# somente-leitura `next`: seleção determinística (§2.5) e renderização (§2.6).
#
# Os oito TFs de ramo abaixo constroem `Modelo`/`Plano`/`Item` diretamente (mesmo padrão de
# `test_tf_show_trunca_em_8000_chars_120_linhas_com_ponteiro`), sem tocar disco — não há
# residência real a computar para exercitar a ordem de seleção em si. Os quatro TFs da RP-5
# (worked examples A/B de §2.6) usam as fixtures em disco `next_tk90` e
# `next_tk90_sem_indice`, que carregam `- **Tipo:** bug` no tíquete `TK-90` (nenhuma fixture
# pré-existente tinha esse campo — confirmado por grep antes desta tarefa).
# --------------------------------------------------------------------------- #


def _fabricas(backlog):
    """Fábricas de dataclasses do módulo `backlog` carregado por `_load_backlog()` — o módulo
    não é importável estaticamente (carregado via importlib), então as fábricas só podem
    referenciar `backlog.Item`/`backlog.Plano`/`backlog.LinhaIndice`/`backlog.Modelo` depois de
    `_load_backlog()` ter rodado."""

    def item(id_, status, depende_de=None, campo_tipo=None, linha_header=10):
        return backlog.Item(
            id=id_,
            tipo="tarefa",
            titulo=f"Título de {id_}",
            arquivo="docs/plans/PLANO-x.md",
            linha_header=linha_header,
            linha_fim=linha_header + 1,
            texto=(
                f"### {id_} — Título de {id_} [Sonnet · classe mecanica]\n"
                f"- **Status:** `{status}` · 2026-01-01"
            ),
            modelo="Sonnet",
            classe="mecanica",
            header_valido=True,
            status=status,
            status_linha=linha_header + 1,
            status_razao=None,
            depende_de=depende_de or [],
            campo_tipo=campo_tipo,
        )

    def plano(id_, status, tarefas, ordem_execucao=None, linha_fim=50):
        return backlog.Plano(
            id=id_,
            titulo=f"Título de {id_}",
            arquivo=f"docs/plans/{id_}-x.md",
            linha_header=1,
            linha_fim=linha_fim,
            texto="conteúdo qualquer",
            status=status,
            tarefas=tarefas,
            ordem_execucao=ordem_execucao or [],
        )

    def linha_indice(id_, status_bruto="ready", linha=10):
        return backlog.LinhaIndice(
            id=id_,
            titulo=f"Título de {id_}",
            status_bruto=status_bruto,
            arquivo="docs/DIARIO_DE_OBRAS.md",
            linha=linha,
            ancora=f"docs/plans/{id_}-x.md",
        )

    def modelo(planos, indice, diretiva_ids=None):
        return backlog.Modelo(
            planos=planos,
            tiquetes=[],
            indice=indice,
            diario_arquivo="docs/DIARIO_DE_OBRAS.md",
            diario_linhas=[],
            diretiva_ids=diretiva_ids or [],
        )

    return item, plano, linha_indice, modelo


def test_tf_retomada_de_in_progress():
    backlog = _load_backlog()
    item, plano, linha_indice, modelo = _fabricas(backlog)

    t1 = item("T1", "in-progress")
    t2 = item("T2", "ready")
    p1 = plano("P-0001", "ready", [t1, t2])
    m = modelo([p1], [linha_indice("P-0001")])

    selecao = backlog.selecionar_next(m)

    assert selecao.exit_code == 0
    assert selecao.vencedor.item.id == "T1"


def test_tf_diretiva_restringe_candidatos():
    backlog = _load_backlog()
    item, plano, linha_indice, modelo = _fabricas(backlog)

    t1 = item("T1", "ready")
    t2 = item("T2", "ready")
    p1 = plano("P-0001", "ready", [t1])
    p2 = plano("P-0002", "ready", [t2])
    indice = [linha_indice("P-0001", linha=10), linha_indice("P-0002", linha=11)]

    sem_diretiva = backlog.selecionar_next(modelo([p1, p2], indice))
    assert sem_diretiva.vencedor.item.id == "T1"  # P-0001 vence por FIFO (linha 10 < 11)

    com_diretiva = backlog.selecionar_next(modelo([p1, p2], indice, diretiva_ids=["P-0002"]))
    assert com_diretiva.exit_code == 0
    assert com_diretiva.vencedor.item.id == "T2"


def test_tf_depende_de_nao_done_segura_candidato():
    backlog = _load_backlog()
    item, plano, linha_indice, modelo = _fabricas(backlog)

    t9 = item("T9", "ready")  # dependência ainda não done
    t1 = item("T1", "ready", depende_de=["T9"])
    t2 = item("T2", "ready")
    p1 = plano("P-0001", "ready", [t9, t1, t2])
    m = modelo([p1], [linha_indice("P-0001")])

    selecao = backlog.selecionar_next(m)

    assert selecao.exit_code == 0
    assert selecao.vencedor.item.id == "T9"  # T1 fica preso por Depende de; T9 é elegível primeiro


def test_tf_plano_blocked_nao_contribui():
    backlog = _load_backlog()
    item, plano, linha_indice, modelo = _fabricas(backlog)

    t1 = item("T1", "ready")
    t2 = item("T2", "ready")
    p1 = plano("P-0001", "blocked", [t1])
    p2 = plano("P-0002", "ready", [t2])
    m = modelo([p1, p2], [linha_indice("P-0001", linha=10), linha_indice("P-0002", linha=11)])

    selecao = backlog.selecionar_next(m)

    assert selecao.exit_code == 0
    assert selecao.vencedor.item.id == "T2"


def test_tf_ordem_de_execucao_vence_ordem_dos_cabecalhos():
    backlog = _load_backlog()
    item, plano, linha_indice, modelo = _fabricas(backlog)

    t1 = item("T1", "ready")  # primeiro no cabeçalho
    t2 = item("T2", "ready")  # primeiro na Ordem de execução
    p1 = plano("P-0001", "ready", [t1, t2], ordem_execucao=["T2", "T1"])
    m = modelo([p1], [linha_indice("P-0001")])

    selecao = backlog.selecionar_next(m)

    assert selecao.exit_code == 0
    assert selecao.vencedor.item.id == "T2"


def test_tf_fila_vazia_exit2():
    backlog = _load_backlog()
    item, plano, linha_indice, modelo = _fabricas(backlog)

    t1 = item("T1", "blocked")
    p1 = plano("P-0001", "ready", [t1])
    m = modelo([p1], [linha_indice("P-0001")])

    selecao = backlog.selecionar_next(m)

    assert selecao.exit_code == 2


def test_tf_dois_in_progress_exit3():
    backlog = _load_backlog()
    item, plano, linha_indice, modelo = _fabricas(backlog)

    t1 = item("T1", "in-progress")
    t2 = item("T2", "in-progress")
    p1 = plano("P-0001", "ready", [t1, t2])
    m = modelo([p1], [linha_indice("P-0001")])

    selecao = backlog.selecionar_next(m)

    assert selecao.exit_code == 3
    assert "T1" in selecao.mensagem and "T2" in selecao.mensagem


def test_tf_rodape_lista_blocked_e_conta_memoria_inbox(tmp_path):
    backlog = _load_backlog()
    item, plano, linha_indice, modelo = _fabricas(backlog)

    t1 = item("T1", "ready")
    t_blocked = item("T2", "blocked")
    t_blocked.status_razao = "dependencia"
    p1 = plano("P-0001", "ready", [t1, t_blocked])
    m = modelo([p1], [linha_indice("P-0001")])

    inbox = tmp_path / "_INBOX.md"
    inbox.write_text(
        "\n".join(
            [
                "- 2026-01-01 — a — feedback — candidato 1 — **origem:** x",
                "- 2026-01-02 — b — feedback — candidato 2 — **origem:** y [promovido]",
                "- 2026-01-03 — c — feedback — candidato 3 — **origem:** z",
            ]
        ),
        encoding="utf-8",
    )

    selecao = backlog.selecionar_next(m)
    assert selecao.exit_code == 0
    saida = backlog.renderizar_next(m, selecao, memoria_inbox=inbox)

    assert "fila de memória: 2 candidato(s)" in saida
    assert "T2 (dependencia)" in saida


def test_tr_saida_do_next_cabe_no_teto(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    modelo = backlog.carregar(repo)

    selecao = backlog.selecionar_next(modelo)
    assert selecao.exit_code == 0
    saida = backlog.renderizar_next(modelo, selecao)

    assert len(saida) <= 8200


# --------------------------------------------------------------------------- #
# RP-5 — os quatro TFs fechados pela rodada de replanejamento: forma por tipo de pai
# (DB-33), faixa de bug sobre itens elegíveis (DB-35) e antecessora omitida no primeiro
# irmão (DB-34). Usam a fixture em disco `next_tk90` (com `TK-90` marcado `- **Tipo:** bug`)
# e `next_tk90_sem_indice` (mesmo `TK-90`, sem linha de índice).
# --------------------------------------------------------------------------- #


def test_tf_bug_antes_de_fifo(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    modelo = backlog.carregar(repo)

    selecao = backlog.selecionar_next(modelo)
    assert selecao.exit_code == 0
    assert selecao.vencedor.item.id == "TK-90a"

    saida = backlog.renderizar_next(modelo, selecao)
    linhas = saida.splitlines()
    assert (
        linhas[1]
        == "tíquete: TK-90 — Relatório diário sai com data trocada (0/2) · "
        "residência: docs/DIARIO_DE_OBRAS.md:10-18 · índice: docs/DIARIO_DE_OBRAS.md#tk-90"
    )
    assert "antecessora:" not in saida  # TK-90a é o primeiro irmão sob TK-90 (DB-34)


def test_tf_linha_do_pai_plano(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    modelo = backlog.carregar(repo)
    modelo.diretiva_ids = ["P-0090"]  # restringe a P-0090 (DB-1: campo já resolvido, sem parsear diretiva aqui)

    selecao = backlog.selecionar_next(modelo)
    assert selecao.exit_code == 0
    assert selecao.vencedor.item.id == "FFO-T2"

    num_linhas_plano = len((repo / "docs" / "plans" / "P-0090-fifo.md").read_text(encoding="utf-8").splitlines())
    saida = backlog.renderizar_next(modelo, selecao)
    linhas = saida.splitlines()

    assert linhas[1].startswith("plano: ")
    assert "P-0090" in linhas[1]
    assert "Plano fifo perdedor" in linhas[1]
    assert "(1/2)" in linhas[1]  # DB-36: FFO-T1 done, FFO-T2 ready — 1 done de 2 vivos
    assert f"residência: docs/plans/P-0090-fifo.md:1-{num_linhas_plano}" in linhas[1]
    assert "índice: docs/plans/P-0090-fifo.md" in linhas[1]


def test_tf_antecessora_omitida_no_primeiro_irmao(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")

    # sub-caso 1: vencedor (TK-90a) é o primeiro irmão sob TK-90 — sem linha `antecessora:`.
    modelo1 = backlog.carregar(repo)
    selecao1 = backlog.selecionar_next(modelo1)
    saida1 = backlog.renderizar_next(modelo1, selecao1)
    assert "antecessora:" not in saida1

    # sub-caso 2: vencedor (FFO-T2) não é o primeiro irmão — FFO-T1 é a antecessora, sem
    # bloco `Notas de execução`, então a linha 3 termina em "sem notas" (DB-34).
    modelo2 = backlog.carregar(repo)
    modelo2.diretiva_ids = ["P-0090"]
    selecao2 = backlog.selecionar_next(modelo2)
    saida2 = backlog.renderizar_next(modelo2, selecao2)
    linhas2 = saida2.splitlines()
    assert linhas2[2] == "antecessora: FFO-T1 (done; sem notas)"


def test_tf_pai_sem_linha_de_indice_sai_exit_3(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90_SEM_INDICE, tmp_path / "repo")
    modelo = backlog.carregar(repo)

    selecao = backlog.selecionar_next(modelo)

    assert selecao.exit_code == 3
    assert "linha de índice ausente para TK-90" in selecao.mensagem


# --------------------------------------------------------------------------- #
# BKL-T3a (`docs/plans/P-0739-backlog-instrumento.md` `### BKL-T3a`) — substrings
# obrigatórias das três condições de exit 3 de `next` (§2.5 item 6) e gramática por
# arquivo do contador de pendências do rodapé (§2.4 / DB-38).
# --------------------------------------------------------------------------- #


def test_tf_contador_do_inbox_de_planos_ignora_drenada_e_linha_sem_plano(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    modelo = backlog.carregar(repo)
    selecao = backlog.selecionar_next(modelo)
    assert selecao.exit_code == 0

    saida = backlog.renderizar_next(modelo, selecao, inbox_planos=_FIXTURE_INBOX_PLANOS)

    assert "inbox de planos: 1 por drenar" in saida
    assert "inbox de planos: 3 por drenar" not in saida


def test_tf_exit_3_dois_in_progress_nomeia_os_ids(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    diario = repo / "docs" / "DIARIO_DE_OBRAS.md"
    linhas = diario.read_text(encoding="utf-8").splitlines()
    alvo = "- **Status:** `ready` · 2026-01-01"
    secao_atual = None
    for i, linha in enumerate(linhas):
        if linha.startswith("### TK-90a"):
            secao_atual = "TK-90a"
            continue
        if linha.startswith("### TK-90b"):
            secao_atual = "TK-90b"
            continue
        if secao_atual in ("TK-90a", "TK-90b") and linha.strip() == alvo:
            linhas[i] = "- **Status:** `in-progress` · 2026-01-01"
            secao_atual = None
    diario.write_text("\n".join(linhas) + "\n", encoding="utf-8")

    modelo = backlog.carregar(repo)
    selecao = backlog.selecionar_next(modelo)

    assert selecao.exit_code == 3
    assert "dois ou mais itens in-progress: TK-90a, TK-90b" in selecao.mensagem


def test_tf_exit_3_item_sem_linha_de_status(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    diario = repo / "docs" / "DIARIO_DE_OBRAS.md"
    linhas = diario.read_text(encoding="utf-8").splitlines()
    alvo = "- **Status:** `ready` · 2026-01-01"
    secao_atual = None
    saida_linhas = []
    for linha in linhas:
        if linha.startswith("### TK-90a"):
            secao_atual = "TK-90a"
            saida_linhas.append(linha)
            continue
        if secao_atual == "TK-90a" and linha.strip() == alvo:
            secao_atual = None
            continue  # remove a linha de Status de TK-90a — vencedor da fixture intacta
        saida_linhas.append(linha)
    diario.write_text("\n".join(saida_linhas) + "\n", encoding="utf-8")

    modelo = backlog.carregar(repo)
    selecao = backlog.selecionar_next(modelo)

    assert selecao.exit_code == 3
    assert "linha de status ausente para TK-90a" in selecao.mensagem


# --------------------------------------------------------------------------- #
# BKL-T3b (`docs/plans/P-0739-backlog-instrumento.md` `### BKL-T3b`) — E-2 sobre o
# pai do candidato (`DB-37`/`DB-40`) e prefixo `- ` do contador de memória (`DB-41`).
# --------------------------------------------------------------------------- #


def test_tf_exit_3_pai_de_candidato_sem_linha_de_status(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")

    diario = repo / "docs" / "DIARIO_DE_OBRAS.md"
    linhas = diario.read_text(encoding="utf-8").splitlines()
    alvo = "- **Status:** `ready` · 2026-01-01"
    saida_linhas = []
    aguardando_status_tk90 = False
    for linha in linhas:
        if linha.startswith("## TK-90 —"):
            saida_linhas.append(linha)
            aguardando_status_tk90 = True
            continue
        if aguardando_status_tk90 and linha.strip() == alvo:
            aguardando_status_tk90 = False
            continue  # remove a linha de Status do pai TK-90
        saida_linhas.append(linha)
    diario.write_text("\n".join(saida_linhas) + "\n", encoding="utf-8")

    plano = repo / "docs" / "plans" / "P-0090-fifo.md"
    texto_plano = plano.read_text(encoding="utf-8")
    alvo_plano = "**Status:** `ready` · **Prefixo das tarefas no diário:** `FFO-T<n>`"
    substituto_plano = "**Prefixo das tarefas no diário:** `FFO-T<n>`"
    texto_plano = texto_plano.replace(alvo_plano, substituto_plano)
    plano.write_text(texto_plano, encoding="utf-8")

    modelo = backlog.carregar(repo)
    selecao = backlog.selecionar_next(modelo)

    assert selecao.exit_code == 3
    assert selecao.mensagem.count("linha de status ausente para TK-90") == 1
    assert "linha de status ausente para P-0090" in selecao.mensagem
    assert selecao.mensagem.index("P-0090") < selecao.mensagem.index("TK-90")


def test_tf_contador_de_memoria_ignora_regua_e_marcadas(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    modelo = backlog.carregar(repo)

    selecao = backlog.selecionar_next(modelo)
    assert selecao.exit_code == 0

    inbox = tmp_path / "_INBOX.md"
    inbox.write_text(
        "# Inbox de memória (fixture)\n"
        "\n"
        "- 2026-01-01 — a — feedback — candidato 1 — **origem:** x\n"
        "- 2026-01-02 — b — feedback — candidato 2 — **origem:** y [promovido]\n"
        "\n"
        "---\n"
        "\n"
        "- 2026-01-03 — c — feedback — candidato 3 — **origem:** z\n",
        encoding="utf-8",
    )

    saida = backlog.renderizar_next(modelo, selecao, memoria_inbox=inbox)

    assert "fila de memória: 2 candidato(s)" in saida
    assert "fila de memória: 3 candidato(s)" not in saida


# --------------------------------------------------------------------------- #
# TK-61a (`docs/DIARIO_DE_OBRAS.md` `### TK-61a`) — `DB-4`: rodapé de `next` projeta
# "candidato a fechamento", linha própria sob `--- pendências mecânicas ---`, sem tocar a
# linha dos três contadores (`DB-38`). Fixture `candidato_a_fechamento` traz os quatro casos
# num corpus só: TK-1 (todos terminais, aparece), TK-2 (filho vivo, não aparece), TK-3 (pai já
# terminal, não aparece), TK-4 (zero filhos, não aparece).
# --------------------------------------------------------------------------- #


def test_tf_rodape_lista_candidato_a_fechamento_quatro_casos(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_CANDIDATO_A_FECHAMENTO, tmp_path / "repo")
    modelo = backlog.carregar(repo)

    selecao = backlog.selecionar_next(modelo)
    assert selecao.exit_code == 0
    assert selecao.vencedor.item.id == "TK-2b"

    saida = backlog.renderizar_next(modelo, selecao)
    linhas = saida.splitlines()

    # (i) TK-1 — pai vivo, filhos TK-1a (done) e TK-1b (cancelled), todos terminais: aparece.
    #     DB-36: total = filhos não cancelled (só TK-1a) = 1; done = 1.
    # (ii) TK-2 — filho TK-2b ready: não aparece.
    # (iii) TK-3 — pai já `done`, filho TK-3a `done`: não aparece.
    # (iv) TK-4 — zero filhos: não aparece.
    assert linhas[-1] == "candidato a fechamento: TK-1 (1/1)"


def test_tr_linha_dos_tres_contadores_segue_identica(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_CANDIDATO_A_FECHAMENTO, tmp_path / "repo")
    modelo = backlog.carregar(repo)

    selecao = backlog.selecionar_next(modelo)
    assert selecao.exit_code == 0

    saida = backlog.renderizar_next(modelo, selecao)
    linhas = saida.splitlines()

    assert linhas[-2] == "inbox de planos: 0 por drenar · fila de memória: 0 candidato(s) · blocked: nenhum"
    assert linhas[-1] == "candidato a fechamento: TK-1 (1/1)"


# --------------------------------------------------------------------------- #
# BKL-T4 (`docs/plans/P-0739-backlog-instrumento.md` `### BKL-T4`) — `status`, `start`,
# `diretiva`: transição (§2.7) e escrita atômica das projeções (§3), reusando E-2/E-3
# de §2.5 item 6 (`DB-37`, `DB-40`) já entregues por `next`.
# --------------------------------------------------------------------------- #


def test_tf_status_transicao_valida_escreve_projecoes(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    _inserir_bloco_gerado(repo)
    modelo = backlog.carregar(repo)

    resultado = backlog.transacionar_status(repo, modelo, "TK-90a", "in-progress")

    assert resultado.exit_code == 0
    assert resultado.arquivos == ["docs/DIARIO_DE_OBRAS.md"]

    diario = (repo / "docs" / "DIARIO_DE_OBRAS.md").read_text(encoding="utf-8")
    assert "- **Status:** `in-progress` · " in diario
    linha_indice = next(l for l in diario.splitlines() if l.startswith("| TK-90 "))
    assert "ready 0/2" in linha_indice
    assert "<!-- fila:gerada -->" in diario
    assert "`TK-90`" in diario


def test_tf_status_transicao_em_tarefa_de_plano_escreve_os_dois_arquivos(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    _inserir_bloco_gerado(repo)
    modelo = backlog.carregar(repo)

    resultado = backlog.transacionar_status(repo, modelo, "FFO-T2", "in-progress")

    assert resultado.exit_code == 0
    assert resultado.arquivos == ["docs/DIARIO_DE_OBRAS.md", "docs/plans/P-0090-fifo.md"]

    plano_texto = (repo / "docs" / "plans" / "P-0090-fifo.md").read_text(encoding="utf-8")
    assert "### FFO-T2" in plano_texto
    assert "- **Status:** `in-progress` · " in plano_texto

    diario = (repo / "docs" / "DIARIO_DE_OBRAS.md").read_text(encoding="utf-8")
    linha_indice = next(l for l in diario.splitlines() if l.startswith("| P-0090 "))
    assert "ready 1/2" in linha_indice  # DB-36: FFO-T1 done, FFO-T2 (agora in-progress) — 1/2 inalterado


def test_tf_bloco_gerado_tem_bullet_por_pai(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    _inserir_bloco_gerado(repo)

    for estado in ("in-progress", "review", "done"):
        modelo = backlog.carregar(repo)
        resultado = backlog.transacionar_status(repo, modelo, "TK-90a", estado)
        assert resultado.exit_code == 0, resultado.mensagem

    diario_texto = (repo / "docs" / "DIARIO_DE_OBRAS.md").read_text(encoding="utf-8")
    ini = diario_texto.index("<!-- fila:gerada -->")
    fim = diario_texto.index("<!-- /fila:gerada -->")
    bloco = diario_texto[ini:fim]

    assert "- `P-0090` (`ready`, 1/2): próxima `FFO-T2`" in bloco
    assert "- `TK-90` (`ready`, 1/2): próxima `TK-90b`" in bloco
    # DB-33: ordem das linhas do índice — âncoras com o prefixo "- " porque a linha
    # `**Fila corrente:**` (BKL-T10b, metade 1) também carrega um token `` `TK-90` `` bare.
    assert bloco.index("- `P-0090`") < bloco.index("- `TK-90`")

    linha_indice = next(l for l in diario_texto.splitlines() if l.startswith("| TK-90 "))
    assert "ready 1/2" in linha_indice  # DB-36: TK-90a done, TK-90b ready — 1/2


# --------------------------------------------------------------------------- #
# BKL-T10b (`docs/plans/P-0739-backlog-instrumento.md` `### BKL-T10b`) — as três metades do
# bloco gerado: a linha `**Fila corrente:**` sobrevive à escrita (metade 1), o casamento de
# plano por sufixo também vale para o bloco (metade 2), e o bloco enxerga o corpus (metade 3).
# --------------------------------------------------------------------------- #


def test_tf_bloco_fila_preserva_linha_fila_corrente(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    diario = repo / "docs" / "DIARIO_DE_OBRAS.md"
    linhas = diario.read_text(encoding="utf-8").splitlines()
    linhas[1:1] = [
        "<!-- fila:gerada -->",
        "**Fila corrente:** `stale` — stale (`stale:0-0`) · fila: — · ready 0 · blocked 0 · in-progress 0",
        "- `stale` (`stale`, 0/0): próxima —",
        "<!-- /fila:gerada -->",
    ]
    diario.write_text("\n".join(linhas) + "\n", encoding="utf-8")
    modelo = backlog.carregar(repo)

    resultado = backlog.transacionar_status(repo, modelo, "TK-90a", "in-progress")

    assert resultado.exit_code == 0, resultado.mensagem
    diario_depois = diario.read_text(encoding="utf-8")
    ini = diario_depois.index("<!-- fila:gerada -->")
    fim = diario_depois.index("<!-- /fila:gerada -->")
    bloco = diario_depois[ini:fim]

    # Hoje a linha `**Fila corrente:**` desaparece (AE-27): o escritor substitui tudo entre
    # os marcadores só pelos bullets. Regenerada, ela continua presente e o `<ID>` nela
    # acompanha a transição (TK-90a in-progress → o pai TK-90 é o vencedor de `selecionar_next`).
    assert "**Fila corrente:**" in bloco
    assert "stale" not in bloco
    assert "`TK-90`" in bloco


def test_tf_bloco_fila_casa_plano_por_sufixo(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_CORPUS, tmp_path / "repo")
    # Índice publica `P-0777-XYZ` (sufixo mnemônico) e vivo; cabeçalho do plano declara só
    # `P-0777`. Filho `GAM-T1` vira não terminal para que o pai tenha bullet.
    _mudar_linha_unica(
        repo,
        "docs/DIARIO_DE_OBRAS.md",
        "| P-0777-XYZ | Plano gama | done | docs/plans/P-0777-gama.md |",
        "| P-0777-XYZ | Plano gama | ready | docs/plans/P-0777-gama.md |",
    )
    _mudar_linha_unica(
        repo,
        "docs/plans/P-0777-gama.md",
        "- **Status:** `done` · 2026-01-03",
        "- **Status:** `ready` · 2026-01-03",
    )
    modelo = backlog.carregar(repo)

    bloco = backlog._bloco_fila_corrente(modelo)
    texto = "\n".join(bloco)

    # A regra concorrente (igualdade exata `plano.id == linha_idx.id`) não emitiria bullet
    # nenhum para `P-0777`, porque `P-0777-XYZ` != `P-0777`.
    assert "- `P-0777`" in texto


def test_tf_bloco_fila_respeita_corpus(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_CORPUS, tmp_path / "repo")
    # `P-0900` (índice `ready`) já tem filho `LEG-T1` não terminal. `P-0777-XYZ` passa a
    # `superseded` no índice mas ganha filho não terminal também — só o corpus decide.
    _mudar_linha_unica(
        repo,
        "docs/DIARIO_DE_OBRAS.md",
        "| P-0777-XYZ | Plano gama | done | docs/plans/P-0777-gama.md |",
        "| P-0777-XYZ | Plano gama | superseded | docs/plans/P-0777-gama.md |",
    )
    _mudar_linha_unica(
        repo,
        "docs/plans/P-0777-gama.md",
        "- **Status:** `done` · 2026-01-03",
        "- **Status:** `ready` · 2026-01-03",
    )
    # `P-0900-legado.md` é fixture de plano fechado antigo, sem `Status`/`Prefixo` de propósito
    # (outros TF exercitam C-7/C-8 com isso). Aqui o campo é necessário para que `selecionar_next`
    # não recuse por E-2 e a linha da metade 1 chegue ao ramo com vencedor e contagens.
    p0900 = repo / "docs" / "plans" / "P-0900-legado.md"
    p0900.write_text(
        p0900.read_text(encoding="utf-8").replace(
            "# P-0900 — Plano legado\n",
            "# P-0900 — Plano legado\n\n**Status:** `ready` · **Prefixo das tarefas no diário:** `LEG-T<n>`\n",
            1,
        ),
        encoding="utf-8",
    )
    modelo = backlog.carregar(repo)

    bloco = backlog._bloco_fila_corrente(modelo)
    texto = "\n".join(bloco)

    # A regra concorrente (todo plano do diretório) emitiria os dois bullets.
    assert "- `P-0900`" in texto
    assert "- `P-0777`" not in texto
    # Só os filhos de `P-0900` (LEG-T1, ready) entram nas contagens da linha da metade 1 —
    # `GAM-T1`, fora do corpus, não conta.
    assert "ready 1 · blocked 0 · in-progress 0" in bloco[0]


def test_tr_bloco_fila_nao_cresce_com_plano_terminal(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_CORPUS, tmp_path / "repo")
    bloco_antes = backlog._bloco_fila_corrente(backlog.carregar(repo))

    _inserir_linhas_indice(repo, ["| P-0950 | Plano extra terminal | done | docs/plans/P-0950-extra.md |"])
    (repo / "docs" / "plans" / "P-0950-extra.md").write_text(
        "\n".join(
            [
                "# P-0950 — Plano extra terminal",
                "",
                "**Status:** `done` · **Prefixo das tarefas no diário:** `EXT-T<n>`",
                "",
                "### EXT-T1 — Única [Sonnet · classe implementacao]",
                "- **Status:** `done` · 2026-01-01",
                "",
            ]
        ),
        encoding="utf-8",
    )
    bloco_depois = backlog._bloco_fila_corrente(backlog.carregar(repo))

    assert bloco_depois == bloco_antes


def test_tf_status_blocked_sem_razao_recusa(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    _inserir_bloco_gerado(repo)
    antes = _hashes(repo)
    modelo = backlog.carregar(repo)

    resultado = backlog.transacionar_status(repo, modelo, "TK-90a", "blocked")

    assert resultado.exit_code == 1
    assert _hashes(repo) == antes


def test_tf_status_transicao_invalida_nao_escreve_nada(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    _inserir_bloco_gerado(repo)
    antes = _hashes(repo)
    modelo = backlog.carregar(repo)

    # `ready` → `done` não está em `_TRANSICOES` (§2.7 exige passar por in-progress/review).
    resultado = backlog.transacionar_status(repo, modelo, "TK-90a", "done")

    assert resultado.exit_code == 1
    assert _hashes(repo) == antes


def test_tf_status_nota_apensa_subbullet_e_nao_toca_indice(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    _inserir_bloco_gerado(repo)
    modelo = backlog.carregar(repo)

    resultado = backlog.transacionar_status(repo, modelo, "TK-90b", "in-progress", nota="anotação de execução")

    assert resultado.exit_code == 0
    diario = (repo / "docs" / "DIARIO_DE_OBRAS.md").read_text(encoding="utf-8")
    assert "- **Notas de execução:**" in diario
    assert "`in-progress` — anotação de execução" in diario

    linha_indice = next(l for l in diario.splitlines() if l.startswith("| TK-90 "))
    assert "anotação de execução" not in linha_indice


def test_tf_start_recusa_com_outro_in_progress_no_mesmo_pai(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    _inserir_bloco_gerado(repo)
    modelo = backlog.carregar(repo)
    primeiro = backlog.transacionar_status(repo, modelo, "TK-90a", "in-progress")
    assert primeiro.exit_code == 0

    antes = _hashes(repo)
    modelo2 = backlog.carregar(repo)
    resultado = backlog.transacionar_status(repo, modelo2, "TK-90b", "in-progress")

    assert resultado.exit_code == 1
    assert _hashes(repo) == antes


def test_tf_diretiva_preserva_texto_livre(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    diario = repo / "docs" / "DIARIO_DE_OBRAS.md"
    linhas = diario.read_text(encoding="utf-8").splitlines()
    linhas.insert(1, "**Diretiva de priorização:** nada por ora")
    diario.write_text("\n".join(linhas) + "\n", encoding="utf-8")

    modelo = backlog.carregar(repo)
    texto = "Priorize `P-0090` — motivo livre com **markdown** e crases `X`"
    resultado = backlog.transacionar_diretiva(repo, modelo, texto)

    assert resultado.exit_code == 0
    diario_depois = diario.read_text(encoding="utf-8")
    assert f"**Diretiva de priorização:** {texto}" in diario_depois
    assert "nada por ora" not in diario_depois


def test_tf_status_recusa_pai_sem_linha_de_indice(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90_SEM_INDICE, tmp_path / "repo")
    antes = _hashes(repo)

    modelo = backlog.carregar(repo)
    resultado = backlog.transacionar_status(repo, modelo, "TK-90a", "in-progress")

    assert resultado.exit_code == 3
    assert "linha de índice ausente para " in resultado.mensagem
    assert "TK-90" in resultado.mensagem
    assert _hashes(repo) == antes


def test_tf_bkl_3campos():
    """TF da LM-T4a: `TAREFA_HEADER_RE` aceita o cabeçalho de três campos (`DM-5`), com `esforço`
    opcional entre modelo e classe. Concorrente: hoje o match é `None`, e é isso que faz o `Item`
    nascer `header_valido=False`, sem modelo e sem classe (`F-6`)."""
    backlog = _load_backlog()

    match = backlog.TAREFA_HEADER_RE.match(
        "### XX-T1 — Título [Sonnet · esforço medium · classe implementacao]"
    )

    assert match is not None
    assert match.group(1) == "XX-T1"
    assert match.group(2) == "Título"
    assert match.group(3) == "Sonnet"
    assert match.group(4) == "implementacao"


def test_tr_bkl_grupos_posicionais():
    """TR da LM-T4a: o grupo novo de `esforço` é não capturante — `group(3)`/`group(4)` continuam
    lendo modelo/classe por posição. Concorrente: com um grupo capturante no `_BRACKET`,
    `group(3)`/`group(4)` devolveriam valores deslocados, exatamente a leitura que
    `backlog.py:229`/`:232` fazem."""
    backlog = _load_backlog()

    match = backlog.TAREFA_HEADER_RE.match(
        "### XX-T2 — Título [Opus + dono · classe investigacao · teto 3]"
    )

    assert match is not None
    assert match.group(3) == "Opus"
    assert match.group(4) == "investigacao"


def test_tf_bkl_esforco_fora_do_vocabulario():
    """TF da LM-T4a: `esforço` fora do vocabulário fechado (`low|medium|high|xhigh|max`) não casa.
    Concorrente: com o campo escrito como `.+?` em vez do vocabulário fechado, esta linha
    casaria — a gramática é fechada."""
    backlog = _load_backlog()

    match = backlog.TAREFA_HEADER_RE.match(
        "### XX-T3 — Título [Sonnet · esforço enorme · classe implementacao]"
    )

    assert match is None


# --------------------------------------------------------------------------- #
# LM-T4b (`docs/plans/P-0740-loop-de-modulos.md` `### LM-T4b`) — o bullet de `Status` em
# prosa: leitura aceita a forma canônica e a forma livre por igual, escrita preserva a
# cauda a partir de ` — `.
# --------------------------------------------------------------------------- #


def test_tf_status_em_prosa_e_lido():
    """Os cinco literais reais do card `LM-T4b` devolvem o estado certo — a forma em prosa
    deixa de dar `linha de status ausente`. As duas formas que o card lista como devendo
    continuar recusadas (sem estado entre crases; estado fora de minúsculas) continuam sem
    status."""
    backlog = _load_backlog()
    literais = [
        "- **Status:** `ready`",
        "- **Status:** `done` (2026-09-19) — **aprovado 100%**, bloqueante `nenhuma`",
        "- **Status:** `blocked` razão `premissa` (2026-09-19, `A3b`) — o executor parou antes de entregar",
        "- **Status:** `ready` · 2026-09-19",
        "- **Status:** `ready` · 2026-09-19 · destravada pelo dono",
    ]
    estados_esperados = ["ready", "done", "blocked", "ready", "ready"]
    for literal, esperado in zip(literais, estados_esperados):
        linhas = ["### T1 — X [Sonnet · classe mecanica]", literal]
        item = backlog._scan_items(linhas, "a.md")[0]
        assert item.status == esperado, literal

    for recusado in ("- **Status:** pendente", "- **Status:** `Ready`"):
        linhas = ["### T1 — X [Sonnet · classe mecanica]", recusado]
        item = backlog._scan_items(linhas, "a.md")[0]
        assert item.status is None, recusado


def test_tr_status_canonico_continua_lido():
    """Regressão: a forma estrita `· AAAA-MM-DD[ · razão]` não muda de leitura com o
    parser em prosa — mesmo caso de `test_tf_status_com_e_sem_razao`, conferido de novo
    aqui sob o nome de regressão do card `LM-T4b`."""
    backlog = _load_backlog()
    linhas_com_razao = [
        "### T1 — X [Sonnet · classe mecanica]",
        "- **Status:** `blocked` · 2026-02-02 · aguardando dono",
    ]
    linhas_sem_razao = [
        "### T1 — X [Sonnet · classe mecanica]",
        "- **Status:** `ready` · 2026-02-02",
    ]
    item_com = backlog._scan_items(linhas_com_razao, "a.md")[0]
    item_sem = backlog._scan_items(linhas_sem_razao, "a.md")[0]
    assert item_com.status == "blocked"
    assert item_com.status_razao == "aguardando dono"
    assert item_sem.status == "ready"
    assert item_sem.status_razao is None


def test_tf_escrita_preserva_a_cauda(tmp_path):
    """Aceite de escrita da `LM-T4b`, sobre a fixture `verde` (`AE-28`/`AE-29` — não sobre o
    plano real): troca o bullet de `ALF-T1` pela forma em prosa, transita `ready →
    in-progress` (está em `_TRANSICOES`) e exige exit 0 com a cauda preservada."""
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
    _inserir_bloco_gerado(repo)

    plano_path = repo / "docs" / "plans" / "P-0001-alfa.md"
    linhas = plano_path.read_text(encoding="utf-8").splitlines()
    idx = linhas.index("- **Status:** `done` · 2026-01-01")
    linhas[idx] = "- **Status:** `ready` (2026-01-01) — cauda em prosa que precisa sobreviver"
    plano_path.write_text("\n".join(linhas) + "\n", encoding="utf-8")

    modelo = backlog.carregar(repo)
    resultado = backlog.transacionar_status(repo, modelo, "ALF-T1", "in-progress")

    assert resultado.exit_code == 0, resultado.mensagem
    plano_depois = plano_path.read_text(encoding="utf-8").splitlines()
    linha_status = next(l for l in plano_depois if l.startswith("- **Status:** `in-progress`"))
    assert linha_status.endswith(" — cauda em prosa que precisa sobreviver")


# --------------------------------------------------------------------------- #
# LM-T4c (`docs/plans/P-0740-loop-de-modulos.md` `### LM-T4c`) — a fronteira entre razão e
# cauda no ramo canônico do bullet de `Status`: a razão não contém ` — `, e a cauda começa no
# primeiro ` — ` da linha.
# --------------------------------------------------------------------------- #


def test_tf_ramo_canonico_separa_razao_de_cauda():
    """TF da `LM-T4c`: caso medido por introspeção no `ESC-19` — a razão gulosa engolia a
    cauda inteira (`razao='premissa — cauda viva'`, `cauda=None`). Com a fronteira nova, a
    razão para no primeiro ` — ` e a cauda fica livre a partir dali."""
    backlog = _load_backlog()
    linha = "- **Status:** `blocked` · 2026-09-19 · premissa — cauda viva"

    match = backlog.STATUS_BULLET_RE.match(linha)

    assert match.group(2) == "premissa"
    assert match.group(3) == "cauda viva"


def test_tr_round_trip_blocked_ready_preserva_a_cauda(tmp_path):
    """Regressão da `LM-T4c`: sobre cópia da fixture `verde` em `tmp_path`, o round-trip
    `ready → blocked --razao premissa → ready` preserva a cauda em prosa no fim da linha nas
    duas transições. Concorrente: com a razão gulosa antiga, a segunda transição (`blocked →
    ready`) perde a prosa porque a primeira leitura já tinha engolido a cauda na razão."""
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
    _inserir_bloco_gerado(repo)

    plano_path = repo / "docs" / "plans" / "P-0001-alfa.md"
    linhas = plano_path.read_text(encoding="utf-8").splitlines()
    idx = linhas.index("- **Status:** `done` · 2026-01-01")
    linhas[idx] = "- **Status:** `ready` · 2026-01-01 — cauda viva"
    plano_path.write_text("\n".join(linhas) + "\n", encoding="utf-8")

    modelo = backlog.carregar(repo)
    resultado = backlog.transacionar_status(repo, modelo, "ALF-T1", "blocked", razao="premissa")
    assert resultado.exit_code == 0, resultado.mensagem

    modelo2 = backlog.carregar(repo)
    resultado2 = backlog.transacionar_status(repo, modelo2, "ALF-T1", "ready")
    assert resultado2.exit_code == 0, resultado2.mensagem

    plano_depois = plano_path.read_text(encoding="utf-8").splitlines()
    linha_status = next(l for l in plano_depois if l.startswith("- **Status:** `ready`"))
    assert linha_status.endswith(" — cauda viva")


# --------------------------------------------------------------------------- #
# LM-T13 (`docs/plans/P-0740-loop-de-modulos.md` `### LM-T13`) — o escritor de `razão`
# recusa o travessão que o leitor (`STATUS_BULLET_RE`, `LM-T4c`) trata como fronteira entre
# razão e cauda: sem a recusa a borda não é round-trippável (`ESC-30`).
# --------------------------------------------------------------------------- #


def test_tf_razao_com_travessao_recusada(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
    _inserir_bloco_gerado(repo)

    plano_path = repo / "docs" / "plans" / "P-0001-alfa.md"
    linhas = plano_path.read_text(encoding="utf-8").splitlines()
    idx = linhas.index("- **Status:** `done` · 2026-01-01")
    linhas[idx] = "- **Status:** `ready` · 2026-01-01"
    plano_path.write_text("\n".join(linhas) + "\n", encoding="utf-8")

    antes = _hashes(repo)
    modelo = backlog.carregar(repo)
    resultado = backlog.transacionar_status(repo, modelo, "ALF-T1", "blocked", razao="premissa — suja")

    assert resultado.exit_code == 1
    assert "travessão" in resultado.mensagem
    assert _hashes(repo) == antes


def test_tf_razao_legitima_faz_round_trip(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
    _inserir_bloco_gerado(repo)

    plano_path = repo / "docs" / "plans" / "P-0001-alfa.md"
    linhas = plano_path.read_text(encoding="utf-8").splitlines()
    idx = linhas.index("- **Status:** `done` · 2026-01-01")
    linhas[idx] = "- **Status:** `ready` · 2026-01-01 — cauda viva"
    plano_path.write_text("\n".join(linhas) + "\n", encoding="utf-8")

    modelo = backlog.carregar(repo)
    resultado = backlog.transacionar_status(repo, modelo, "ALF-T1", "blocked", razao="premissa")
    assert resultado.exit_code == 0, resultado.mensagem

    modelo2 = backlog.carregar(repo)
    alvo = backlog._localizar(modelo2, "ALF-T1")
    assert alvo.status_razao == "premissa"
    assert alvo.status_cauda == "cauda viva"


def _indice_com_sufixo(repo: Path, de: str, para: str) -> None:
    """Reescreve o id publicado na tabela de índice da cópia em `tmp_path` para a forma
    com sufixo mnemônico que o diário real usa (`P-0740-LM` para o plano `P-0740`).
    Nunca toca a fixture do repositório."""
    diario = repo / "docs" / "DIARIO_DE_OBRAS.md"
    linhas = diario.read_text(encoding="utf-8").splitlines()
    for i, linha in enumerate(linhas):
        if linha.startswith(f"| {de} |"):
            linhas[i] = linha.replace(f"| {de} |", f"| {para} |", 1)
            break
    else:  # pragma: no cover - fixture mudou
        raise AssertionError(f"linha de índice de {de} não encontrada na fixture")
    diario.write_text(chr(10).join(linhas) + chr(10), encoding="utf-8")


def _alf_t1_ready(repo: Path) -> Path:
    plano_path = repo / "docs" / "plans" / "P-0001-alfa.md"
    texto = plano_path.read_text(encoding="utf-8")
    plano_path.write_text(
        texto.replace("- **Status:** `done` · 2026-01-01", "- **Status:** `ready` · 2026-01-01"),
        encoding="utf-8",
    )
    return plano_path


def test_tf_indice_com_sufixo_mnemonico_casa_o_plano(tmp_path):
    """`ESC-27` do `P-0740`: o índice publica o id do plano com sufixo (`P-0001-ALF`), o
    cabeçalho do arquivo declara só `P-0001` (`PLANO_HEADER_RE`). Antes do reparo,
    `_posicao_indice` casava por igualdade exata e `status`/`start`/`next` saíam exit 3
    (`linha de índice ausente`) para **toda** tarefa de **todo** plano do repo real."""
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
    _inserir_bloco_gerado(repo)
    _indice_com_sufixo(repo, "P-0001", "P-0001-ALF")
    _alf_t1_ready(repo)

    modelo = backlog.carregar(repo)
    assert backlog._posicao_indice(modelo, "P-0001") is not None
    assert backlog._linha_indice(modelo, "P-0001").id == "P-0001-ALF"
    # sufixo é `-<alfanumérico>` fechado: prefixo parcial e id vizinho não casam
    assert backlog._posicao_indice(modelo, "P-000") is None
    assert backlog._posicao_indice(modelo, "P-0003") is None

    resultado = backlog.transacionar_status(repo, modelo, "ALF-T1", "in-progress")

    assert resultado.exit_code == 0, resultado.mensagem
    diario = (repo / "docs" / "DIARIO_DE_OBRAS.md").read_text(encoding="utf-8")
    assert "| P-0001-ALF | Plano alfa | ready 0/1 |" in diario


def test_tf_indice_exato_vence_o_sufixado(tmp_path):
    """Precedência da regra: havendo linha com o id nu, ela vence a sufixada, mesmo que a
    sufixada venha antes no documento (tíquete publica id nu e continua casando)."""
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
    modelo = backlog.carregar(repo)
    exata = backlog._linha_indice(modelo, "P-0001")
    sufixada = backlog.LinhaIndice(
        id="P-0001-ALF", titulo="x", status_bruto="ready", arquivo=exata.arquivo, linha=0
    )
    modelo.indice.insert(0, sufixada)

    assert backlog._linha_indice(modelo, "P-0001") is exata


def test_tf_status_sem_marcadores_do_bloco_gerado_projeta_e_avisa(tmp_path):
    """`AE-10` do `P-0739` medido no repo real em 2026-09-19 (`ESC-27`): os marcadores
    `<!-- fila:gerada -->` só entram no diário com a `BKL-T6`, e até lá `transacionar_status`
    estourava `ValueError` no `.index(...)`. A transação passa a projetar card + linha de
    índice e **declara** a omissão — pular em silêncio é a classe do `TK-55`."""
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")  # sem `_inserir_bloco_gerado`
    plano_path = _alf_t1_ready(repo)

    modelo = backlog.carregar(repo)
    resultado = backlog.transacionar_status(repo, modelo, "ALF-T1", "in-progress")

    assert resultado.exit_code == 0, resultado.mensagem
    assert "fila:gerada" in (resultado.mensagem or "")
    assert "- **Status:** `in-progress`" in plano_path.read_text(encoding="utf-8")
    assert "| P-0001 | Plano alfa | ready 0/1 |" in (repo / "docs" / "DIARIO_DE_OBRAS.md").read_text(
        encoding="utf-8"
    )


def test_tf_escrita_do_instrumento_preserva_lf(tmp_path):
    """`ESC-27` do `P-0740`: `.gitattributes` declara `* text=auto eol=lf` e o drift-guard
    `DP-5` depende disso. `_escrever_atomico` em modo texto no Windows gravava CRLF e virava o
    terminador de todo arquivo que o instrumento tocasse."""
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
    plano_path = _alf_t1_ready(repo)

    modelo = backlog.carregar(repo)
    resultado = backlog.transacionar_status(repo, modelo, "ALF-T1", "in-progress")

    assert resultado.exit_code == 0, resultado.mensagem
    for alvo in (plano_path, repo / "docs" / "DIARIO_DE_OBRAS.md"):
        assert b"\r" not in alvo.read_bytes(), alvo


# --------------------------------------------------------------------------- #
# BKL-T10a (`docs/plans/P-0739-backlog-instrumento.md` `### BKL-T10a`) — `drain`: cada linha
# viva de `docs/plans/_INBOX.md` vira linha de índice do diário e sai, verbatim, para
# `docs/plans/_INBOX_HISTORICO.md`. Nenhuma fixture de inbox com linha viva existe em
# `tests/fixtures/backlog/` — contingência do card: a fixture nasce na cópia em `tmp_path`,
# dentro do próprio teste, e não é entregável novo.
# --------------------------------------------------------------------------- #


def _escrever_plano(
    repo: Path, nome_arquivo: str, plano_id: str, titulo: str, prefixo: str | None, status: str | None
) -> Path:
    caminho = repo / "docs" / "plans" / nome_arquivo
    campos = []
    if status is not None:
        campos.append(f"**Status:** `{status}`")
    if prefixo is not None:
        campos.append(f"**Prefixo das tarefas no diário:** `{prefixo}-T<n>`")
    linhas = [f"# {plano_id} — {titulo}", ""]
    if campos:
        linhas.append(" · ".join(campos))
        linhas.append("")
    caminho.write_text("\n".join(linhas), encoding="utf-8")
    return caminho


def _inbox_com_linhas(repo: Path, linhas_extra: list[str]) -> Path:
    caminho = repo / "docs" / "plans" / "_INBOX.md"
    texto = caminho.read_text(encoding="utf-8")
    caminho.write_text(texto.rstrip("\n") + "\n" + "\n".join(linhas_extra) + "\n", encoding="utf-8")
    return caminho


def test_tf_drain_move_linha_viva(tmp_path):
    """Objetivo do card: a linha viva vira linha de índice (estado do `Status` do cabeçalho,
    título da linha 1, âncora = caminho) e sai, verbatim menos o prefixo, para o histórico.
    Exercita também a ressalva da revisão da `BKL-T10b`: o bloco `Fila corrente` é regenerado
    pela mesma `_regenerar_bloco_fila` que `status`/`diretiva` chamam — se `drain`
    reimplementasse a escrita do bloco em vez de chamá-la, o marcador continuaria vazio (como
    `_inserir_bloco_gerado` o deixa) em vez de ganhar a linha `**Fila corrente:**`."""
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    _escrever_plano(repo, "P-0800-alfa.md", "P-0800", "Plano alfa de teste", "ALF", "ready")
    _inbox_com_linhas(repo, ["- docs/plans/P-0800-alfa.md — plano alfa de teste, drenado pelo TF"])
    _inserir_bloco_gerado(repo)

    modelo = backlog.carregar(repo)
    inbox_path = repo / "docs" / "plans" / "_INBOX.md"
    historico_path = repo / "docs" / "plans" / "_INBOX_HISTORICO.md"

    resultado = backlog.transacionar_drain(repo, modelo, inbox_path, historico_path, data="2026-09-20")

    assert resultado.exit_code == 0, resultado.mensagem

    inbox_depois = inbox_path.read_text(encoding="utf-8")
    assert "P-0800-alfa" not in inbox_depois

    historico_depois = historico_path.read_text(encoding="utf-8")
    assert (
        "- [drenado 2026-09-20] docs/plans/P-0800-alfa.md — plano alfa de teste, drenado pelo TF"
        in historico_depois
    )

    diario_depois = (repo / "docs" / "DIARIO_DE_OBRAS.md").read_text(encoding="utf-8")
    assert "| P-0800-ALF | Plano alfa de teste | ready | docs/plans/P-0800-alfa.md |" in diario_depois

    ini = diario_depois.index("<!-- fila:gerada -->")
    fim = diario_depois.index("<!-- /fila:gerada -->")
    bloco = diario_depois[ini:fim]
    assert "**Fila corrente:**" in bloco


def test_tf_drain_ignora_linha_ja_drenada(tmp_path):
    """Inbox com uma linha viva, uma já prefixada `- [drenado AAAA-MM-DD] ` e uma sem caminho
    de plano: `drain` move só a viva. A gramática concorrente (a do inbox de memória, que só
    olha `[promovido]`/`[descartado`) moveria as duas outras também — nenhuma delas traz essas
    marcas — e é isso que esta fixture separa."""
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    _escrever_plano(repo, "P-0800-alfa.md", "P-0800", "Plano alfa de teste", "ALF", "ready")
    _inbox_com_linhas(
        repo,
        [
            "- docs/plans/P-0800-alfa.md — plano alfa de teste",
            "- [drenado 2026-09-01] docs/plans/P-0700-velho.md — já drenado antes, não é viva",
            "- nota qualquer sem caminho de plano nenhum",
        ],
    )

    modelo = backlog.carregar(repo)
    inbox_path = repo / "docs" / "plans" / "_INBOX.md"
    historico_path = repo / "docs" / "plans" / "_INBOX_HISTORICO.md"

    resultado = backlog.transacionar_drain(repo, modelo, inbox_path, historico_path, data="2026-09-20")

    assert resultado.exit_code == 0, resultado.mensagem

    historico_depois = historico_path.read_text(encoding="utf-8").splitlines()
    assert len(historico_depois) == 1
    assert "P-0800-alfa" in historico_depois[0]

    inbox_depois = inbox_path.read_text(encoding="utf-8")
    assert "[drenado 2026-09-01] docs/plans/P-0700-velho.md" in inbox_depois
    assert "nota qualquer sem caminho de plano nenhum" in inbox_depois
    assert "P-0800-alfa" not in inbox_depois


def test_tf_drain_inbox_vazio_e_no_op(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    modelo = backlog.carregar(repo)
    inbox_path = repo / "docs" / "plans" / "_INBOX.md"
    historico_path = repo / "docs" / "plans" / "_INBOX_HISTORICO.md"
    antes = _hashes(repo)

    resultado = backlog.transacionar_drain(repo, modelo, inbox_path, historico_path, data="2026-09-20")

    assert resultado.exit_code == 0
    assert resultado.arquivos == []
    assert _hashes(repo) == antes
    assert not historico_path.exists()


def test_tf_drain_plano_malformado_sai_exit_3(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    _escrever_plano(repo, "P-0800-alfa.md", "P-0800", "Plano alfa de teste", "ALF", "ready")
    _escrever_plano(repo, "P-0900-ruim.md", "P-0900", "Plano ruim", None, None)
    _inbox_com_linhas(
        repo,
        [
            "- docs/plans/P-0800-alfa.md — linha boa, vem antes",
            "- docs/plans/P-0900-ruim.md — linha malformada, sem Status nem Prefixo",
        ],
    )

    modelo = backlog.carregar(repo)
    inbox_path = repo / "docs" / "plans" / "_INBOX.md"
    historico_path = repo / "docs" / "plans" / "_INBOX_HISTORICO.md"
    antes = _hashes(repo)

    resultado = backlog.transacionar_drain(repo, modelo, inbox_path, historico_path, data="2026-09-20")

    assert resultado.exit_code == 3
    assert "P-0900-ruim.md" in resultado.mensagem
    assert _hashes(repo) == antes
    assert not historico_path.exists()


def test_tf_drain_recalcula_contador(tmp_path):
    """Corpus com um id maior que o do último drenado, para que a regra "último + 1" e a regra
    "max + 1" divirjam: a linha de id maior (`P-0743`) vem primeiro no inbox e a de id menor
    (`P-0741`) é a última processada. "último + 1" daria `P-0742`; "max + 1" dá `P-0744`."""
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    _escrever_plano(repo, "P-0743-alta.md", "P-0743", "Plano de id alto", "ALT", "ready")
    _escrever_plano(repo, "P-0741-baixa.md", "P-0741", "Plano de id baixo", "BAI", "ready")
    _inbox_com_linhas(
        repo,
        [
            "- docs/plans/P-0743-alta.md — processada primeiro",
            "- docs/plans/P-0741-baixa.md — processada por último",
        ],
    )

    modelo = backlog.carregar(repo)
    inbox_path = repo / "docs" / "plans" / "_INBOX.md"
    historico_path = repo / "docs" / "plans" / "_INBOX_HISTORICO.md"

    resultado = backlog.transacionar_drain(repo, modelo, inbox_path, historico_path, data="2026-09-20")

    assert resultado.exit_code == 0, resultado.mensagem
    inbox_depois = inbox_path.read_text(encoding="utf-8")
    assert "**Próximo id de plano: P-0744.**" in inbox_depois


def test_tr_historico_do_inbox_so_cresce(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    historico_path = repo / "docs" / "plans" / "_INBOX_HISTORICO.md"
    historico_path.write_text(
        "- [drenado 2026-01-01] docs/plans/P-0500-antigo.md — entrada histórica preexistente\n",
        encoding="utf-8",
    )
    _escrever_plano(repo, "P-0800-alfa.md", "P-0800", "Plano alfa de teste", "ALF", "ready")
    _inbox_com_linhas(repo, ["- docs/plans/P-0800-alfa.md — nova linha viva"])

    modelo = backlog.carregar(repo)
    inbox_path = repo / "docs" / "plans" / "_INBOX.md"

    linhas_antes = set(historico_path.read_text(encoding="utf-8").splitlines())
    resultado = backlog.transacionar_drain(repo, modelo, inbox_path, historico_path, data="2026-09-20")
    assert resultado.exit_code == 0, resultado.mensagem
    linhas_depois = set(historico_path.read_text(encoding="utf-8").splitlines())

    assert linhas_antes <= linhas_depois
    assert len(linhas_depois) == len(linhas_antes) + 1


# --------------------------------------------------------------------------- #
# TF hook — BKL-T11: `.claude/tools/backlog_hook.py`, gatilho e injeção via `next`
# --------------------------------------------------------------------------- #


def test_tf_hook_com_gatilho_devolve_additional_context(tmp_path, monkeypatch, capsys):
    hook = _load_hook()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    monkeypatch.setattr(sys, "stdin", io.StringIO(json.dumps({"prompt": "execute o próximo passo"})))

    exit_code = hook.main(repo=repo)

    assert exit_code == 0
    saida = json.loads(capsys.readouterr().out)
    assert saida["hookSpecificOutput"]["hookEventName"] == "UserPromptSubmit"
    assert saida["hookSpecificOutput"]["additionalContext"].strip() != ""


def test_tf_hook_sem_gatilho_e_silencio(tmp_path, monkeypatch, capsys):
    hook = _load_hook()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    monkeypatch.setattr(sys, "stdin", io.StringIO(json.dumps({"prompt": "bom dia"})))

    exit_code = hook.main(repo=repo)

    assert exit_code == 0
    assert capsys.readouterr().out == ""


def test_tf_hook_exit_3_de_next_vira_contexto(tmp_path, monkeypatch, capsys):
    hook = _load_hook()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    _mudar_linha_unica(
        repo,
        "docs/DIARIO_DE_OBRAS.md",
        "### TK-90a — Corrigir o parser de data do relatório [Sonnet · classe mecanica]\n"
        "- **Status:** `ready` · 2026-01-01",
        "### TK-90a — Corrigir o parser de data do relatório [Sonnet · classe mecanica]\n"
        "- **Status:** `in-progress` · 2026-01-01",
    )
    _mudar_linha_unica(
        repo,
        "docs/DIARIO_DE_OBRAS.md",
        "### TK-90b — Cobrir o parser com teste de regressão [Sonnet · classe mecanica]\n"
        "- **Status:** `ready` · 2026-01-01",
        "### TK-90b — Cobrir o parser com teste de regressão [Sonnet · classe mecanica]\n"
        "- **Status:** `in-progress` · 2026-01-01",
    )
    monkeypatch.setattr(sys, "stdin", io.StringIO(json.dumps({"prompt": "próximo passo"})))

    exit_code = hook.main(repo=repo)

    assert exit_code == 0
    saida = json.loads(capsys.readouterr().out)
    contexto = saida["hookSpecificOutput"]["additionalContext"]
    assert "TK-90a" in contexto and "TK-90b" in contexto


def test_tf_hook_gatilho_ignora_caixa(tmp_path, monkeypatch, capsys):
    hook = _load_hook()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    monkeypatch.setattr(sys, "stdin", io.StringIO(json.dumps({"prompt": "Execute o PRÓXIMO PASSO"})))

    exit_code = hook.main(repo=repo)

    assert exit_code == 0
    saida = json.loads(capsys.readouterr().out)
    assert saida["hookSpecificOutput"]["additionalContext"].strip() != ""


# --------------------------------------------------------------------------- #
# TF hook executável — BKL-T11a: `subprocess.run` do próprio
# `.claude/tools/backlog_hook.py`, bytes UTF-8 pela entrada padrão. Os TF acima entram por
# importação, com a string já decodificada em memória, e nunca tocam o `sys.stdin` de um
# processo — é exatamente esse ponto de carga que o `AE-35` mediu quebrado (0 bytes num host
# sem `PYTHONUTF8`, `sys.stdin.read()` decodificando em cp1252).
#
# TK-63a: o mundo hostil deixa de ser "host sem PYTHONUTF8" (mede o host — em host que já
# exporte a variável, para de discriminar) e passa a ser construído: `env` mínimo +
# `PYTHONIOENCODING=cp1252` (hostil; `PYTHONIOENCODING` prevalece sobre `PYTHONUTF8`, medido) e
# `env` mínimo + `PYTHONUTF8=1` (seguro). O par negativo deixa de ser um stub que só discriminava
# a si mesmo — passa a ser o produto revertido, extraído do arquivo real por substituição textual
# do bloco de reparo, montado na mesma raiz falsa que o produto correto. Mesma técnica do
# `telemetria_hook` na `TK-56b` (`tests/test_telemetria_hook.py`), aprovada 100%.
# --------------------------------------------------------------------------- #


def test_tf_hook_executavel_stdin_utf8_devolve_contexto(tmp_path):
    """TK-63a: raiz relocada em `tmp_path` (via `_montar_raiz_hook`, fixture `next_tk90`) —
    zero leitura do diário ou dos planos reais. Três asserções de relação, nenhuma de magnitude:
    (i) invariância — o hook reparado dá a mesma saída nos mundos hostil e seguro; (ii)
    divergência — o hook revertido (bloco de decode UTF-8 explícito trocado por `sys.stdin.read()`
    cru) dá saídas diferentes entre os dois mundos; (iii) não-vazio — a saída do reparado no
    mundo hostil não fica em branco. Reproduzido em 2026-09-20, em raiz relocada sobre
    `next_tk90`: reparado → 739 B idênticos em hostil e seguro; revertido → 0 B no hostil, 739 B
    no seguro."""
    fonte = _HOOK_PATH.read_text(encoding="utf-8")
    bloco_reparo = (
        "        try:\n"
        "            raw = sys.stdin.buffer.read().decode(\"utf-8\", errors=\"replace\")\n"
        "        except AttributeError:\n"
        "            raw = sys.stdin.read()\n"
    )
    assert bloco_reparo in fonte
    fonte_revertida = fonte.replace(bloco_reparo, "        raw = sys.stdin.read()\n")

    env_hostil = {
        "SYSTEMROOT": os.environ["SYSTEMROOT"],
        "PATH": os.environ["PATH"],
        "PYTHONIOENCODING": "cp1252",
    }
    env_seguro = {
        "SYSTEMROOT": os.environ["SYSTEMROOT"],
        "PATH": os.environ["PATH"],
        "PYTHONUTF8": "1",
    }
    payload = json.dumps(
        {"hookEventName": "UserPromptSubmit", "prompt": "execute o próximo passo"},
        ensure_ascii=False,
    ).encode("utf-8")

    def _rodar(nome: str, fonte_hook: str, env: dict):
        raiz = _montar_raiz_hook(tmp_path, nome, fonte_hook)
        hook_path = raiz / ".claude" / "tools" / "backlog_hook.py"
        return subprocess.run(
            [sys.executable, str(hook_path)], input=payload, capture_output=True, env=env,
        )

    reparado_hostil = _rodar("reparado_hostil", fonte, env_hostil)
    reparado_seguro = _rodar("reparado_seguro", fonte, env_seguro)
    revertido_hostil = _rodar("revertido_hostil", fonte_revertida, env_hostil)
    revertido_seguro = _rodar("revertido_seguro", fonte_revertida, env_seguro)

    for resultado in (reparado_hostil, reparado_seguro, revertido_hostil, revertido_seguro):
        assert resultado.returncode == 0

    # (i) invariância — o reparado dá a mesma saída nos dois mundos
    assert reparado_hostil.stdout == reparado_seguro.stdout
    # (iii) não-vazio — a saída do reparado no mundo hostil não fica em branco
    assert reparado_hostil.stdout != b""
    # (ii) divergência — o revertido dá saídas diferentes entre os dois mundos
    assert revertido_hostil.stdout != revertido_seguro.stdout


def test_tf_hook_executavel_sem_gatilho_e_silencio():
    payload = json.dumps(
        {"hookEventName": "UserPromptSubmit", "prompt": "bom dia"},
        ensure_ascii=False,
    ).encode("utf-8")
    env = {"SYSTEMROOT": os.environ["SYSTEMROOT"], "PATH": os.environ["PATH"]}

    resultado = subprocess.run(
        [sys.executable, str(_HOOK_PATH)],
        input=payload,
        capture_output=True,
        env=env,
    )

    assert resultado.returncode == 0
    assert resultado.stdout == b""
