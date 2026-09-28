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

import datetime
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
_FIXTURE_PASTA = _FIXTURES / "pasta"
_FIXTURE_ESQUELETO = _FIXTURES / "esqueleto"


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
    shutil.copy2(_BACKLOG_PATH.parent / "caminhos.py", tools_dir / "caminhos.py")
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


def test_scan_items_corta_no_nivel_2():
    backlog = _load_backlog()
    linhas = [
        "# P-0999 — Plano",
        "",
        "## 5. Tarefas",
        "",
        "### X-T1 — Um [Sonnet · esforço low · classe implementacao]",
        "",
        "- **Status:** `ready`",
        "",
        "~~~~",
        "## Dentro da cerca",
        "~~~~",
        "",
        "## 6. Ordem de execução",
        "",
        "`X-T1`",
        "",
        "## 8. Achados",
        "",
        "- achado",
    ]
    item = backlog._scan_items(linhas, "p.md")[0]
    assert item.linha_fim == 12
    assert "## Dentro da cerca" in item.texto
    assert "## 6. Ordem de execução" not in item.texto


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
# TF/TR C-15 (EBK-T1) — tíquete vivo (status fora de done/cancelled/superseded) sem
# subtarefa. Fixture `verde`: TK-1 tem TK-1a (sem C-15); removendo a subtarefa, TK-1 fica
# vivo e sem filho — acusa C-15 nomeando TK-1. Tíquete terminal sem subtarefa não é acusado.
# --------------------------------------------------------------------------- #


def _remover_tk1a_verde(repo: Path) -> None:
    diario_path = repo / "docs" / "DIARIO_DE_OBRAS.md"
    linhas = diario_path.read_text(encoding="utf-8").splitlines()
    idx = linhas.index("### TK-1a — Sub da base [Sonnet · classe mecanica]")
    fim = idx + 2  # header da subtarefa + linha de Status dela
    if idx > 0 and linhas[idx - 1] == "":
        idx -= 1
    del linhas[idx:fim]
    diario_path.write_text("\n".join(linhas) + "\n", encoding="utf-8")


def test_tf_c15_par_tiquete_vivo_sem_subtarefa(tmp_path):
    backlog = _load_backlog()

    repo_com = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo_com")
    violacoes_com = backlog.check(backlog.carregar(repo_com))
    assert not any(v.codigo == "C-15" for v in violacoes_com)

    repo_sem = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo_sem")
    _remover_tk1a_verde(repo_sem)
    violacoes_sem = backlog.check(backlog.carregar(repo_sem))
    c15 = [v for v in violacoes_sem if v.codigo == "C-15"]
    assert len(c15) == 1
    assert "TK-1" in c15[0].texto


def test_tf_c15_tiquete_cancelled_sem_subtarefa_nao_acusa(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
    _remover_tk1a_verde(repo)
    _mudar_linha_unica(
        repo,
        "docs/DIARIO_DE_OBRAS.md",
        "| TK-1 | Tiquete base | ready | docs/DIARIO_DE_OBRAS.md#tk-1 |",
        "| TK-1 | Tiquete base | cancelled | docs/DIARIO_DE_OBRAS.md#tk-1 |",
    )
    _mudar_linha_unica(
        repo,
        "docs/DIARIO_DE_OBRAS.md",
        "- **Status:** `ready` · 2026-01-01",
        "- **Status:** `cancelled` · 2026-01-01",
    )

    violacoes = backlog.check(backlog.carregar(repo))
    assert not any(v.codigo == "C-15" for v in violacoes)


# --------------------------------------------------------------------------- #
# TF C-16 (EBK-T2) — a leitura de dossiê do `rdo.py` (`extrair_dossie`, leitura estrita:
# esquema_legado=False, modelo_legado=None, classe_legado=None) confronta todo card vivo
# (ready/in-progress/review); recusa vira C-16 com a mensagem da própria leitura, sem
# reimplementar a gramática (propriedade 1). Card done/cancelled/blocked não é lido
# (propriedade 2). Fixture `verde`: TK-1a nasce sem campo nenhum — os quatro obrigatórios
# (Objetivo/Arquivos-alvo/Verificação/Pronto quando) entram na cópia, logo abaixo do Status.
# --------------------------------------------------------------------------- #


def _tk1a_com_dossie(
    repo: Path,
    *,
    remover_verificacao: bool = False,
    heading_antes_verificacao: bool = False,
    status: str = "ready",
) -> None:
    diario_path = repo / "docs" / "DIARIO_DE_OBRAS.md"
    linhas = diario_path.read_text(encoding="utf-8").splitlines()
    idx = linhas.index("### TK-1a — Sub da base [Sonnet · classe mecanica]")
    status_idx = idx + 1
    assert linhas[status_idx].startswith("- **Status:**")
    if status != "ready":
        linhas[status_idx] = linhas[status_idx].replace("`ready`", f"`{status}`")
    novas = [
        "- **Objetivo:** objetivo mínimo do card de teste.",
        "- **Arquivos-alvo:**",
        "  - `arquivo-de-teste.py`",
    ]
    if heading_antes_verificacao:
        novas.append("### X")
    if not remover_verificacao:
        novas.extend(["- **Verificação:**", "  1. passo único de verificação."])
    novas.append("- **Pronto quando:** critério mínimo de pronto.")
    linhas[status_idx + 1 : status_idx + 1] = novas
    diario_path.write_text("\n".join(linhas) + "\n", encoding="utf-8")


def test_tf_c16_par_card_com_e_sem_verificacao(tmp_path):
    backlog = _load_backlog()

    repo_integro = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo_integro")
    _tk1a_com_dossie(repo_integro)
    violacoes_integro = backlog.check(backlog.carregar(repo_integro), repo=repo_integro, dossie=True)
    assert violacoes_integro == []

    repo_sem_verificacao = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo_sem_verificacao")
    _tk1a_com_dossie(repo_sem_verificacao, remover_verificacao=True)
    violacoes_sem = backlog.check(backlog.carregar(repo_sem_verificacao), repo=repo_sem_verificacao, dossie=True)
    assert len(violacoes_sem) == 1
    assert violacoes_sem[0].codigo == "C-16"
    assert violacoes_sem[0].texto == "campo obrigatório ausente em 'TK-1a': 'verificacao'"

    repo_heading = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo_heading")
    _tk1a_com_dossie(repo_heading, heading_antes_verificacao=True)
    violacoes_heading = backlog.check(backlog.carregar(repo_heading), repo=repo_heading, dossie=True)
    assert len(violacoes_heading) == 1
    assert violacoes_heading[0].codigo == "C-16"
    assert violacoes_heading[0].texto == "campo obrigatório ausente em 'TK-1a': 'verificacao'"


def test_tf_c16_card_defeituoso_status_done_nao_acusa(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
    _tk1a_com_dossie(repo, remover_verificacao=True, status="done")

    violacoes = backlog.check(backlog.carregar(repo), repo=repo, dossie=True)
    assert violacoes == []


# --------------------------------------------------------------------------- #
# TF C-17 (EBK-T2, DEB-7 propriedade 5) — entrada de `piso_c11` que não casa nenhuma
# ocorrência de citação quebrada no corpus corrente. Nenhuma fixture traz citação de seção;
# a cópia da `verde` recebe `.claude/skills/diario-de-obras/SKILL.fixture.md` (sem heading
# numerado `2.5`, só em prosa) e uma linha no diário citando `§2.5` dele — a forma que o C-11
# colhe.
# --------------------------------------------------------------------------- #

_C17_ENTRADA_QUE_CASA = (".claude/skills/diario-de-obras/SKILL.fixture.md", "2.5")
_C17_ENTRADA_ORFA = (".claude/skills/diario-de-obras/SKILL.fixture.md", "9.9")


def _verde_com_citacao_quebrada(tmp_path: Path, nome: str) -> Path:
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / nome)
    fixture_path = repo / ".claude" / "skills" / "diario-de-obras" / "SKILL.fixture.md"
    fixture_path.parent.mkdir(parents=True, exist_ok=True)
    fixture_path.write_text(
        "# X\n\n## 1. Um\n\nTexto de prosa que menciona 2.5 sem heading numerado 2.5.\n",
        encoding="utf-8",
    )
    diario = repo / "docs" / "DIARIO_DE_OBRAS.md"
    texto = diario.read_text(encoding="utf-8")
    if not texto.endswith("\n"):
        texto += "\n"
    diario.write_text(
        texto + "\nVer `.claude/skills/diario-de-obras/SKILL.fixture.md` §2.5.\n",
        encoding="utf-8",
    )
    return repo


def test_tf_c17_par_piso_casa_e_entrada_orfa(tmp_path):
    backlog = _load_backlog()
    repo = _verde_com_citacao_quebrada(tmp_path, "repo")
    modelo = backlog.carregar(repo)

    violacoes_sem_piso = backlog.check(modelo, repo=repo)
    assert len(violacoes_sem_piso) == 1
    assert violacoes_sem_piso[0].codigo == "C-11"

    violacoes_piso_casa = backlog.check(modelo, repo=repo, piso_c11={_C17_ENTRADA_QUE_CASA})
    assert violacoes_piso_casa == []

    violacoes_com_orfa = backlog.check(
        modelo, repo=repo, piso_c11={_C17_ENTRADA_QUE_CASA, _C17_ENTRADA_ORFA}
    )
    c17 = [v for v in violacoes_com_orfa if v.codigo == "C-17"]
    assert len(c17) == 1
    assert _C17_ENTRADA_ORFA[0] in c17[0].texto and _C17_ENTRADA_ORFA[1] in c17[0].texto
    assert not any(v.codigo == "C-11" for v in violacoes_com_orfa)


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
# TF/TR AF-T8 — plano em esboço (fixture `esqueleto`): `estado.tsv` só com a linha do
# plano, `blocked`, e nenhuma linha do inbox citando o caminho dele. O contador do
# `_INBOX.md` aponta para o mesmo id do plano em esboço — `C-10` não acusa enquanto o
# plano segue nesse estado; volta a acusar assim que uma linha de tarefa entra no
# `estado.tsv` (o plano deixou de ser esboço).
# --------------------------------------------------------------------------- #


def test_tf_check_aceita_plano_em_esqueleto(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_ESQUELETO, tmp_path / "repo")

    modelo = backlog.carregar(repo)
    violacoes = backlog.check(modelo, inbox_planos=repo / "docs" / "plans" / "_INBOX.md", repo=repo)

    assert violacoes == []


def test_tr_check_esqueleto_com_linha_de_tarefa_segue_acusando_c10(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_ESQUELETO, tmp_path / "repo")
    estado_path = repo / "docs" / "plans" / "P-0-esboco" / "estado.tsv"
    with estado_path.open("a", encoding="utf-8", newline="\n") as f:
        f.write("ESB-T1\ttarefa\tblocked\tdependencia\t2026-09-27\t-\n")

    modelo = backlog.carregar(repo)
    violacoes = backlog.check(modelo, inbox_planos=repo / "docs" / "plans" / "_INBOX.md", repo=repo)

    assert any(v.codigo == "C-10" for v in violacoes)


def test_tr_check_plano_legado_blocked_no_contador_segue_acusando_c10(tmp_path):
    """AE-10: o esboço é só plano em pasta. Plano legado `blocked`, id igual ao contador e
    fora do inbox não é esboço — o `C-10` segue acusando."""
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_CONTADOR_INBOX, tmp_path / "repo")
    _mudar_linha_unica(
        repo,
        "docs/plans/P-0742-existe.md",
        "**Status:** `done` · **Prefixo das tarefas no diário:** `EXI-T<n>`",
        "**Status:** `blocked` · **Prefixo das tarefas no diário:** `EXI-T<n>`",
    )

    modelo = backlog.carregar(repo)
    violacoes = backlog.check(modelo, inbox_planos=repo / "docs" / "plans" / "_INBOX.md", repo=repo)

    c10 = [v for v in violacoes if v.codigo == "C-10"]
    assert len(c10) == 1 and "P-0742" in c10[0].texto


# --------------------------------------------------------------------------- #
# TF/TR C-12 (TK-65a) — `Depende de:` só com ids de item, na gramática publicada
# `` `ID`[, `ID`] ``. Caso medido: o `P-0741` com `Depende de` citando ids de decisão do
# modelo (`DMC-*`) passou no `check` e travou o `next` (`0 elegível(is) · blocked 0`). Mesmo
# plano nas duas leituras — só o valor do campo muda.
# --------------------------------------------------------------------------- #


def _verde_com_depende(tmp_path: Path, valor: str, continuacao: str | None = None) -> Path:
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
    plano = repo / "docs" / "plans" / "P-0001-alfa.md"
    card = [
        "",
        "### ALF-T2 — Segunda tarefa [Sonnet · classe implementacao]",
        "- **Status:** `ready` · 2026-01-02",
        f"- **Depende de:** {valor}",
    ]
    if continuacao is not None:
        card.append(continuacao)
    plano.write_text(plano.read_text(encoding="utf-8").rstrip("\n") + "\n" + "\n".join(card) + "\n", encoding="utf-8")
    return repo


def test_tf_c12_depende_de_cita_id_que_nao_e_item(tmp_path):
    backlog = _load_backlog()
    repo = _verde_com_depende(tmp_path, "`DMC-1`")

    modelo = backlog.carregar(repo)
    c12 = [v for v in backlog.check(modelo) if v.codigo == "C-12"]

    assert len(c12) == 1
    assert c12[0].arquivo == "docs/plans/P-0001-alfa.md" and "DMC-1" in c12[0].texto
    # a mesma árvore trava o seletor — é o defeito que o lint passa a acusar
    selecao = backlog.selecionar_next(modelo)
    assert selecao.vencedor is None or selecao.vencedor.item.id != "ALF-T2"


def test_tr_c12_depende_de_com_ids_de_tarefa_nao_dispara(tmp_path):
    backlog = _load_backlog()
    repo = _verde_com_depende(tmp_path, "`ALF-T1`")

    modelo = backlog.carregar(repo)

    assert backlog.check(modelo) == []


def test_tf_c12_depende_de_com_prosa_no_campo(tmp_path):
    backlog = _load_backlog()
    repo = _verde_com_depende(tmp_path, "`ALF-T1` (as duas editam o mesmo arquivo)")

    c12 = [v for v in backlog.check(backlog.carregar(repo)) if v.codigo == "C-12"]

    assert len(c12) == 1 and "prosa" in c12[0].texto


def test_tf_c12_depende_de_com_continuacao_recuada(tmp_path):
    """Id na linha de continuação some do seletor (`_extrair_depende` só lê a 1ª linha)."""
    backlog = _load_backlog()
    repo = _verde_com_depende(tmp_path, "`ALF-T1`", continuacao="  `TK-1a`")

    c12 = [v for v in backlog.check(backlog.carregar(repo)) if v.codigo == "C-12"]

    assert len(c12) == 1 and "prosa" in c12[0].texto


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
# FPU-T6 — o dossiê de despacho carrega os achados roteados ao card (DFP-19)
# --------------------------------------------------------------------------- #

_ACHADOS_EXTRA = (
    "\n## Achados da execução\n\n"
    "- **`AE-1`** (2026-01-05, fixture) — achado da fixture, roteado. **Rota:** ALF-T1.\n"
    "- **AE-7** (`ALF-T1`, fechamento, 2026-01-02) — …\n"
    "  **Rota:** ALF-T1 (continuação)\n"
    "- **AE-8** (2026-01-06) — cita ALF-T1 no corpo, sem rota formal.\n"
    "- **AE-9** (2026-01-07) — achado da fixture, não roteado. **Rota:** ALF-T1a.\n"
)


def _verde_com_achados(tmp_path: Path) -> Path:
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
    plano = repo / "docs" / "plans" / "P-0001-alfa.md"
    plano.write_text(plano.read_text(encoding="utf-8") + _ACHADOS_EXTRA, encoding="utf-8")
    return repo


def test_tf_show_lista_achado_roteado(tmp_path):
    backlog = _load_backlog()
    repo = _verde_com_achados(tmp_path)
    modelo = backlog.carregar(repo)

    saida = backlog.show(modelo, "ALF-T1")
    bloco = saida.split("\n\n**Achados roteados a este card:**\n", 1)[1]

    assert "AE-1" in bloco
    assert "AE-7" in bloco
    assert "  **Rota:** ALF-T1 (continuação)" in bloco
    assert "AE-8" not in bloco
    assert "AE-9" not in bloco


def test_tf_show_sem_achado_diz_nenhum(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
    modelo = backlog.carregar(repo)

    saida = backlog.show(modelo, "BET-T1")

    assert saida.endswith("\n\n**Achados roteados a este card:** nenhum")


def test_tr_show_de_tiquete_nao_muda(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
    modelo = backlog.carregar(repo)

    alvo = backlog._localizar(modelo, "TK-1a")
    assert backlog.show(modelo, "TK-1a") == alvo.texto

    selecao = backlog.selecionar_next(modelo)
    assert selecao.vencedor.item.id == "TK-1a"
    saida = backlog.renderizar_next(modelo, selecao)
    assert "Achados roteados" not in saida


def test_tf_next_de_tarefa_de_plano_traz_o_bloco(tmp_path, capsys):
    backlog = _load_backlog()
    repo = _verde_com_handover(tmp_path)

    assert backlog.main(["next", "--repo", str(repo)]) == 0
    saida = capsys.readouterr().out

    assert saida.startswith("=== PRÓXIMA TAREFA: ALF-T2")
    idx_dossie = saida.index("--- dossiê")
    idx_pendencias = saida.index("--- pendências mecânicas ---")
    bloco_achados = saida.index("**Achados roteados a este card:** nenhum")
    assert idx_dossie < bloco_achados < idx_pendencias


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
# AF-T9 — `next` e `show` entregam o card inteiro; só notas de execução e achados
# seguem truncados ao teto `DB-7`.
# --------------------------------------------------------------------------- #


def test_tf_card_inteiro_no_next_e_no_show(tmp_path):
    backlog = _load_backlog()
    linhas_card = [f"- linha {i:03d} do card" for i in range(1, 151)]
    texto = (
        "### T1 — Título de T1 [Sonnet · classe mecanica]\n"
        "- **Status:** `ready` · 2026-01-01\n" + "\n".join(linhas_card)
    )
    t1 = backlog.Item(
        id="T1",
        tipo="tarefa",
        titulo="Título de T1",
        arquivo="docs/plans/P-0001-x.md",
        linha_header=10,
        linha_fim=10 + len(texto.splitlines()) - 1,
        texto=texto,
        modelo="Sonnet",
        classe="mecanica",
        status="ready",
        status_linha=11,
        pai="P-0001",
    )
    p1 = backlog.Plano(
        id="P-0001",
        titulo="Título de P-0001",
        arquivo="docs/plans/P-0001-x.md",
        linha_header=1,
        linha_fim=200,
        texto="conteúdo qualquer",
        status="ready",
        tarefas=[t1],
    )
    indice = [
        backlog.LinhaIndice(
            id="P-0001",
            titulo="Título de P-0001",
            status_bruto="ready",
            arquivo="docs/DIARIO_DE_OBRAS.md",
            linha=10,
            ancora="docs/plans/P-0001-x.md",
        )
    ]
    modelo = backlog.Modelo(planos=[p1], tiquetes=[], indice=indice, diario_arquivo="docs/DIARIO_DE_OBRAS.md")

    selecao = backlog.selecionar_next(modelo)
    assert selecao.exit_code == 0
    saida_next = backlog.renderizar_next(modelo, selecao)
    assert "linha 150 do card" in saida_next
    assert "… truncado (" not in saida_next

    saida_show = backlog.show(modelo, "T1")
    assert "linha 150 do card" in saida_show
    assert "… truncado (" not in saida_show


def test_tf_card_inteiro_pela_cli_sobre_plano_em_arquivo(tmp_path, capsys):
    """TF (`AE-12` do `P-0753`): o mesmo contrato do TF acima, exercitado na camada da CLI —
    plano em pasta gravado em disco, lido pelo parser, e `main(["show", ...])` e
    `main(["next", ...])` sobre ele. O card de 150 linhas sai inteiro nos dois verbos, até a
    última linha, e o card seguinte não vaza para o `show`."""
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_PASTA, tmp_path / "repo")
    linhas_card = "\n".join(f"- linha {i:03d} do card" for i in range(1, 151))
    plano = repo / "docs" / "plans" / "P-0-gama" / "plano.md"
    plano.write_text(
        plano.read_text(encoding="utf-8").replace(
            "- **Objetivo:** fixture.\n\n### GAM-T2",
            f"- **Objetivo:** fixture.\n{linhas_card}\n\n### GAM-T2",
            1,
        ),
        encoding="utf-8",
    )

    assert backlog.main(["show", "GAM-T1", "--repo", str(repo)]) == 0
    saida_show = capsys.readouterr().out
    assert "- linha 150 do card" in saida_show
    assert "… truncado (" not in saida_show
    assert "Segunda tarefa" not in saida_show

    assert backlog.main(["next", "--repo", str(repo)]) == 0
    saida_next = capsys.readouterr().out
    assert "=== PRÓXIMA TAREFA: GAM-T1" in saida_next
    assert "- linha 150 do card" in saida_next
    assert "… truncado (" not in saida_next


def test_tr_show_achados_truncados_apontam_a_secao_de_achados(tmp_path, capsys):
    """TR (`AE-11` do `P-0753`): quando o bloco de achados roteados a um card passa do teto
    `DB-7`, o ponteiro do corte localiza a seção `## Achados da execução` no arquivo do plano
    (`arquivo:<linha do heading>-<última linha da seção>`), como a skill `passagem-de-bastao`
    promete — antes apontava a faixa do plano inteiro (`arquivo:1-<fim>`)."""
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_PASTA, tmp_path / "repo")
    plano = repo / "docs" / "plans" / "P-0-gama" / "plano.md"
    achados = "\n".join(
        f"- **AE-{n}** (`GAM-T1`, fechamento) — achado {n:03d}. **Rota:** GAM-T1" for n in range(1, 131)
    )
    texto = plano.read_text(encoding="utf-8").rstrip("\n") + "\n\n## 9. Achados da execução\n\n" + achados + "\n"
    plano.write_text(texto, encoding="utf-8")
    linhas = texto.splitlines()
    ini = next(i for i, l in enumerate(linhas) if l.startswith("## 9. Achados")) + 1
    fim = len(linhas)

    assert backlog.main(["show", "GAM-T1", "--repo", str(repo)]) == 0

    saida = capsys.readouterr().out
    assert f"… truncado (docs/plans/P-0-gama/plano.md:{ini}-{fim})" in saida


def test_tr_card_inteiro_notas_de_execucao_seguem_com_teto():
    backlog = _load_backlog()
    linhas_notas = [f"  - `in-progress` — nota {i:03d} de execução" for i in range(1, 201)]
    texto = (
        "### T1 — Título de T1 [Sonnet · classe mecanica]\n"
        "- **Status:** `ready` · 2026-01-01\n"
        "- **Notas de execução:**\n" + "\n".join(linhas_notas)
    )
    t1 = backlog.Item(
        id="T1",
        tipo="tarefa",
        titulo="Título de T1",
        arquivo="docs/plans/P-0001-x.md",
        linha_header=10,
        linha_fim=10 + len(texto.splitlines()) - 1,
        texto=texto,
        modelo="Sonnet",
        classe="mecanica",
        status="ready",
        status_linha=11,
        pai="P-0001",
    )
    p1 = backlog.Plano(
        id="P-0001",
        titulo="Título de P-0001",
        arquivo="docs/plans/P-0001-x.md",
        linha_header=1,
        linha_fim=250,
        texto="conteúdo qualquer",
        status="ready",
        tarefas=[t1],
    )
    modelo = backlog.Modelo(planos=[p1], tiquetes=[], indice=[], diario_arquivo="docs/DIARIO_DE_OBRAS.md")

    saida = backlog.show(modelo, "T1")
    assert "… truncado (" in saida


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
# EBK-T3 (`docs/plans/P-0751-esgotar-backlog.md` `### EBK-T3`) — a primeira linha de `next`
# reproduz o colchete do cabeçalho do card como ele está no plano, com ` + dono` e
# ` · esforço <e>` quando o cabeçalho os tem, sobre cópia da fixture `verde`.
# --------------------------------------------------------------------------- #


def test_tf_next_bracket_sem_dono_nem_esforco(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
    modelo = backlog.carregar(repo)

    selecao = backlog.selecionar_next(modelo)
    assert selecao.exit_code == 0
    assert selecao.vencedor.item.id == "TK-1a"

    saida = backlog.renderizar_next(modelo, selecao)
    linhas = saida.splitlines()
    assert linhas[0] == "=== PRÓXIMA TAREFA: TK-1a — Sub da base [Sonnet · classe mecanica]"


def test_tf_next_bracket_projeta_dono_e_esforco(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")

    diario_path = repo / "docs" / "DIARIO_DE_OBRAS.md"
    linhas_diario = diario_path.read_text(encoding="utf-8").splitlines()
    idx = linhas_diario.index("### TK-1a — Sub da base [Sonnet · classe mecanica]")
    linhas_diario[idx] = "### TK-1a — Sub da base [Opus + dono · esforço high · classe investigacao]"
    diario_path.write_text("\n".join(linhas_diario) + "\n", encoding="utf-8")

    modelo = backlog.carregar(repo)
    selecao = backlog.selecionar_next(modelo)
    assert selecao.exit_code == 0
    assert selecao.vencedor.item.id == "TK-1a"

    saida = backlog.renderizar_next(modelo, selecao)
    linhas = saida.splitlines()
    assert linhas[0] == (
        "=== PRÓXIMA TAREFA: TK-1a — Sub da base [Opus + dono · esforço high · classe investigacao]"
    )


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


def test_tf_diretiva_acusa_id_descartado_na_cauda(tmp_path):
    """TF da TK-65c: id de item entre crases na cauda (depois do ` — `) que `_parse_diretiva`
    não lê não é recusado — a escrita segue e o aviso nomeia cada id descartado e a contagem de
    reconhecidos. `TK-90b` e `FFO-T1` são ids de item da árvore da fixture; só `TK-90a` está
    antes do ` — ` e por isso é o único reconhecido."""
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    _inserir_bloco_gerado(repo)
    modelo = backlog.carregar(repo)
    texto = "Priorize `TK-90a` — e depois `TK-90b`, `FFO-T1`"

    resultado = backlog.transacionar_diretiva(repo, modelo, texto)

    assert resultado.exit_code == 0
    diario_depois = (repo / "docs" / "DIARIO_DE_OBRAS.md").read_text(encoding="utf-8")
    assert f"**Diretiva de priorização:** {texto}" in diario_depois
    assert resultado.mensagem is not None
    assert "TK-90b" in resultado.mensagem
    assert "FFO-T1" in resultado.mensagem
    assert "1 id" in resultado.mensagem


def test_tr_diretiva_sem_id_descartado_mensagem_igual_a_hoje(tmp_path):
    """TR da TK-65c: crase que não é id de item (`done`) não entra no aviso — mensagem segue
    idêntica à de antes do reparo (sem aviso de descarte) para a mesma árvore. Concorrente: se o
    reparo passasse a colher qualquer crase da cauda em vez de só ids de item, `done` apareceria
    no aviso."""
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    _inserir_bloco_gerado(repo)
    modelo = backlog.carregar(repo)
    texto = "Priorize `TK-90a` — texto com `done`"

    resultado = backlog.transacionar_diretiva(repo, modelo, texto)

    assert resultado.exit_code == 0
    assert resultado.mensagem is None


def test_tf_diretiva_concatena_aviso_descarte_e_aviso_fila(tmp_path):
    """TK-65e: sem `_inserir_bloco_gerado` (sem `<!-- fila:gerada -->`), `_regenerar_bloco_fila`
    avisa a falta do marcador; com id de item descartado na cauda, `transacionar_diretiva` une os
    dois avisos por quebra de linha na mesma `mensagem` — a 1ª linha nomeia os ids descartados, a
    2ª é o aviso do bloco gerado. Concorrente: se a concatenação deixasse cair um dos dois avisos,
    a mensagem teria só uma linha e faltaria o conteúdo do aviso descartado."""
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    modelo = backlog.carregar(repo)
    texto = "Priorize `TK-90a` — e depois `TK-90b`, `FFO-T1`"

    resultado = backlog.transacionar_diretiva(repo, modelo, texto)

    assert resultado.exit_code == 0
    assert resultado.mensagem is not None
    linhas_mensagem = resultado.mensagem.splitlines()
    assert len(linhas_mensagem) == 2
    assert "TK-90b" in linhas_mensagem[0]
    assert "FFO-T1" in linhas_mensagem[0]
    assert "bloco `Fila corrente` nao projetado" in linhas_mensagem[1]
    assert "<!-- fila:gerada -->" in linhas_mensagem[1]


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


# --------------------------------------------------------------------------- #
# TF/TR TK-65b — `main()` reconfigura utf-8 antes de `parse_args` abrir a boca.
# Caso medido (2026-09-20): `PYTHONIOENCODING= python -X utf8=0 backlog.py --help` →
# `UnicodeEncodeError: 'charmap' codec can't encode character '→' in position 611`
# (a listagem do subcomando `drain` traz `→` no `help=`). Ambiente hostil explícito, mesmo
# padrão de `env=` dos testes `test_tf_hook_executavel_*`: `PYTHONIOENCODING` vazio +
# `-X utf8=0`. Par presença-ausência: o produto real (reparado) sai limpo; uma cópia com o
# laço de `reconfigure` revertido para depois de `parse_args` (o defeito medido) falha —
# prova que o par discrimina.
# --------------------------------------------------------------------------- #

_BLOCO_RECONFIGURE_ANTES = (
    "    for fluxo in (sys.stdout, sys.stderr):\n"
    "        if hasattr(fluxo, \"reconfigure\"):\n"
    "            fluxo.reconfigure(encoding=\"utf-8\")\n"
    "\n"
    "    args = parser.parse_args(argv)\n"
)

_BLOCO_PARSE_ARGS_DEPOIS = (
    "    args = parser.parse_args(argv)\n"
    "\n"
    "    for fluxo in (sys.stdout, sys.stderr):\n"
    "        if hasattr(fluxo, \"reconfigure\"):\n"
    "            fluxo.reconfigure(encoding=\"utf-8\")\n"
)


def _ambiente_hostil() -> dict:
    return {
        "SYSTEMROOT": os.environ["SYSTEMROOT"],
        "PATH": os.environ["PATH"],
        "PYTHONIOENCODING": "",
    }


def test_tf_main_reconfigure_antes_de_parse_args_help_ambiente_hostil():
    fonte = _BACKLOG_PATH.read_text(encoding="utf-8")
    assert _BLOCO_RECONFIGURE_ANTES in fonte

    resultado = subprocess.run(
        [sys.executable, "-X", "utf8=0", str(_BACKLOG_PATH), "--help"],
        capture_output=True,
        env=_ambiente_hostil(),
    )

    assert resultado.returncode == 0
    assert b"usage" in resultado.stdout
    assert b"UnicodeEncodeError" not in resultado.stderr


def test_tf_san_17_parse_plano_em_pasta_sem_cabecalho(tmp_path):
    backlog = _load_backlog()
    pasta = tmp_path / "docs" / "plans" / "P-0-gama"
    pasta.mkdir(parents=True)
    caminho = pasta / "plano.md"
    caminho.write_text("sem cabecalho de plano aqui\n", encoding="utf-8")

    plano = backlog._parse_plano(caminho, tmp_path)

    assert plano.id == "P-0-gama"
    assert plano.titulo == "P-0-gama"


def test_tr_main_reconfigure_apos_parse_args_falha_no_ambiente_hostil(tmp_path):
    fonte = _BACKLOG_PATH.read_text(encoding="utf-8")
    assert _BLOCO_RECONFIGURE_ANTES in fonte
    fonte_revertida = fonte.replace(_BLOCO_RECONFIGURE_ANTES, _BLOCO_PARSE_ARGS_DEPOIS)
    assert fonte_revertida != fonte

    backlog_revertido = tmp_path / "backlog.py"
    backlog_revertido.write_text(fonte_revertida, encoding="utf-8")
    shutil.copy2(_BACKLOG_PATH.parent / "caminhos.py", tmp_path / "caminhos.py")

    resultado = subprocess.run(
        [sys.executable, "-X", "utf8=0", str(backlog_revertido), "--help"],
        capture_output=True,
        env=_ambiente_hostil(),
    )

    assert resultado.returncode != 0
    assert b"UnicodeEncodeError" in resultado.stderr


# --------------------------------------------------------------------------- #
# P-0749 SAN-T2 — o estado sai do texto e vai para o `estado.tsv`. Plano em pasta
# (`_caminhos.e_layout_pasta`) lê e escreve o estado numa tabela de máquina na pasta do
# plano; plano legado segue com o estado na linha `**Status:**`, sem mudança.
# --------------------------------------------------------------------------- #


def test_tf_san_7_pasta_check_verde(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_PASTA, tmp_path / "repo")

    violacoes = backlog.check(
        backlog.carregar(repo), inbox_planos=repo / "docs" / "plans" / "_INBOX.md", repo=repo
    )

    assert violacoes == []


def test_tf_san_8_status_escreve_estado_tsv(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_PASTA, tmp_path / "repo")
    hoje = datetime.date.today().isoformat()
    estado_path = repo / "docs" / "plans" / "P-0-gama" / "estado.tsv"
    plano_path = repo / "docs" / "plans" / "P-0-gama" / "plano.md"
    plano_original = plano_path.read_bytes()

    modelo = backlog.carregar(repo)
    resultado = backlog.transacionar_status(repo, modelo, "GAM-T1", "in-progress")

    assert resultado.exit_code == 0, resultado.mensagem
    linhas_estado = estado_path.read_text(encoding="utf-8").splitlines()
    assert linhas_estado[2] == f"GAM-T1\ttarefa\tin-progress\t-\t{hoje}\t-"
    assert plano_path.read_bytes() == plano_original
    assert "docs/plans/P-0-gama/estado.tsv" in resultado.arquivos
    assert "docs/plans/P-0-gama/plano.md" not in resultado.arquivos

    resultado2 = backlog.transacionar_status(
        repo, modelo, "GAM-T1", "blocked", razao="premissa", nota="contingência 2 acionada: x"
    )

    assert resultado2.exit_code == 0, resultado2.mensagem
    linhas_estado2 = estado_path.read_text(encoding="utf-8").splitlines()
    assert linhas_estado2[2] == f"GAM-T1\ttarefa\tblocked\tpremissa\t{hoje}\tcontingência 2 acionada: x"


def test_tf_san_9_c13_nos_tres_casos(tmp_path):
    backlog = _load_backlog()

    repo1 = _copiar_fixture(_FIXTURE_PASTA, tmp_path / "sem-linha")
    estado_path1 = repo1 / "docs" / "plans" / "P-0-gama" / "estado.tsv"
    linhas1 = [l for l in estado_path1.read_text(encoding="utf-8").splitlines() if not l.startswith("GAM-T2\t")]
    estado_path1.write_text("\n".join(linhas1) + "\n", encoding="utf-8")
    c13_1 = [v for v in backlog.check(backlog.carregar(repo1)) if v.codigo == "C-13"]
    assert any("GAM-T2 sem linha em estado.tsv" in v.texto for v in c13_1)

    repo2 = _copiar_fixture(_FIXTURE_PASTA, tmp_path / "linha-extra")
    estado_path2 = repo2 / "docs" / "plans" / "P-0-gama" / "estado.tsv"
    texto2 = estado_path2.read_text(encoding="utf-8").rstrip("\n")
    estado_path2.write_text(texto2 + "\nGAM-T9\ttarefa\tready\t-\t2026-01-01\t-\n", encoding="utf-8")
    c13_2 = [v for v in backlog.check(backlog.carregar(repo2)) if v.codigo == "C-13"]
    assert any("GAM-T9: linha de estado.tsv sem card em plano.md" in v.texto for v in c13_2)

    repo3 = _copiar_fixture(_FIXTURE_PASTA, tmp_path / "sem-arquivo")
    (repo3 / "docs" / "plans" / "P-0-gama" / "estado.tsv").unlink()
    c13_3 = [v for v in backlog.check(backlog.carregar(repo3)) if v.codigo == "C-13"]
    assert any("estado.tsv ausente" in v.texto for v in c13_3)


def test_tf_san_10_c14_status_no_texto(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_PASTA, tmp_path / "repo")
    plano_path = repo / "docs" / "plans" / "P-0-gama" / "plano.md"
    linhas = plano_path.read_text(encoding="utf-8").splitlines()
    linhas.insert(2, "**Status:** `ready`")
    plano_path.write_text("\n".join(linhas) + "\n", encoding="utf-8")

    violacoes = backlog.check(backlog.carregar(repo))

    c14 = [v for v in violacoes if v.codigo == "C-14"]
    assert len(c14) == 1
    assert c14[0].arquivo == "docs/plans/P-0-gama/plano.md"
    assert c14[0].linha == 3
    assert c14[0].texto == "P-0: linha **Status:** em plano de pasta"


def test_tf_san_11_drain_preserva_largura(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_PASTA, tmp_path / "repo")
    diario_path = repo / "docs" / "DIARIO_DE_OBRAS.md"
    diario_linhas = [
        l for l in diario_path.read_text(encoding="utf-8").splitlines() if not l.startswith("| P-0-GAM ")
    ]
    diario_path.write_text("\n".join(diario_linhas) + "\n", encoding="utf-8")
    inbox_path = repo / "docs" / "plans" / "_INBOX.md"
    inbox_path.write_text(
        "**Próximo id de plano: P-0.**\n- `docs/plans/P-0-gama/plano.md` — gama\n", encoding="utf-8"
    )
    historico_path = repo / "docs" / "plans" / "_INBOX_HISTORICO.md"

    modelo = backlog.carregar(repo)
    resultado = backlog.transacionar_drain(repo, modelo, inbox_path, historico_path, data="2026-09-20")

    assert resultado.exit_code == 0, resultado.mensagem
    assert "**Próximo id de plano: P-1.**" in inbox_path.read_text(encoding="utf-8")


def test_tf_san_12_c10_preserva_largura(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_PASTA, tmp_path / "repo")
    inbox_path = repo / "docs" / "plans" / "_INBOX.md"
    inbox_path.write_text("**Próximo id de plano: P-0.**\n", encoding="utf-8")

    violacoes = backlog.check(backlog.carregar(repo), inbox_planos=inbox_path, repo=repo)

    c10 = [v for v in violacoes if v.codigo == "C-10"]
    assert len(c10) == 1
    assert c10[0].texto == "contador aponta para P-0, já presente em docs/plans/"


def test_tf_san_20_c10_projeto_novo_sem_plano(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_PASTA, tmp_path / "repo")
    shutil.rmtree(repo / "docs" / "plans" / "P-0-gama")
    diario_path = repo / "docs" / "DIARIO_DE_OBRAS.md"
    diario_linhas = [
        l for l in diario_path.read_text(encoding="utf-8").splitlines() if not l.startswith("| P-0-GAM ")
    ]
    diario_path.write_text("\n".join(diario_linhas) + "\n", encoding="utf-8")
    inbox_path = repo / "docs" / "plans" / "_INBOX.md"
    inbox_path.write_text("**Próximo id de plano: P-0.**\n", encoding="utf-8")

    assert backlog.check(backlog.carregar(repo), inbox_planos=inbox_path, repo=repo) == []


# --- TK-88 — plano fecha como done pelo instrumento --------------------------------------------


def test_tf_tk88_plano_ready_para_done_quando_toda_tarefa_e_terminal(tmp_path):
    """TF do `TK-88`: plano não passa por `review`; `ready → done` de **plano** é aceito quando
    nenhuma tarefa está aberta e ao menos uma é `done` (fixture `verde`, `P-0001`: `ALF-T1`
    done), e projeta `done 1/1` no índice. Antes o instrumento recusava e o fechamento era
    escrito à mão (diário, 2026-09-25)."""
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
    modelo = backlog.carregar(repo)

    resultado = backlog.transacionar_status(repo, modelo, "P-0001", "done")

    assert resultado.exit_code == 0, resultado.mensagem
    assert "**Status:** `done`" in (repo / "docs" / "plans" / "P-0001-alfa.md").read_text(encoding="utf-8")
    assert "| P-0001 | Plano alfa | done 1/1 |" in (repo / "docs" / "DIARIO_DE_OBRAS.md").read_text(encoding="utf-8")


def test_tr_tk88_plano_com_tarefa_aberta_nao_fecha_e_tarefa_segue_a_tabela(tmp_path):
    """TR do `TK-88`: a regra de plano nomeia a tarefa aberta e não escreve; para **tarefa**
    `ready → done` continua fora da tabela de §2.7."""
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
    plano = repo / "docs" / "plans" / "P-0001-alfa.md"
    plano.write_text(plano.read_text(encoding="utf-8").replace("- **Status:** `done` · 2026-01-01", "- **Status:** `ready` · 2026-01-01"), encoding="utf-8")
    antes = plano.read_text(encoding="utf-8")
    modelo = backlog.carregar(repo)

    resultado_plano = backlog.transacionar_status(repo, modelo, "P-0001", "done")
    resultado_tarefa = backlog.transacionar_status(repo, modelo, "ALF-T1", "done")

    assert resultado_plano.exit_code == 1 and "ALF-T1" in resultado_plano.mensagem
    assert resultado_tarefa.exit_code == 1 and "fora da tabela" in resultado_tarefa.mensagem
    assert plano.read_text(encoding="utf-8") == antes


def test_tf_checar_transicao_sem_escrita(tmp_path):
    """TF (`TK-88d`): `checar_transicao` devolve, para o plano com tarefa aberta, o mesmo
    resultado que `transacionar_status` produz — sem tocar arquivo (a função não recebe
    `repo`); quem escreve continua sendo só `transacionar_status`."""
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
    plano = repo / "docs" / "plans" / "P-0001-alfa.md"
    plano.write_text(plano.read_text(encoding="utf-8").replace("- **Status:** `done` · 2026-01-01", "- **Status:** `ready` · 2026-01-01"), encoding="utf-8")
    antes = plano.read_text(encoding="utf-8")
    modelo = backlog.carregar(repo)

    resultado_checagem = backlog.checar_transicao(modelo, "P-0001", "done")
    resultado_transacao = backlog.transacionar_status(repo, modelo, "P-0001", "done")

    assert resultado_checagem is not None
    assert resultado_checagem.exit_code == 1 and "ALF-T1" in resultado_checagem.mensagem
    assert resultado_checagem.mensagem == resultado_transacao.mensagem
    assert plano.read_text(encoding="utf-8") == antes


# --- TK-88 — o next devolve o handover à sucessora -------------------------------------------


_HANDOVER_T1 = (
    "- **Handover:** 2026-01-02 · para quem vier depois\n"
    "  - **Entregue:** `alfa.py:1` pronto\n"
    "  - **Contrato:** função `alfa()` estável\n"
    "  - **Não refazer:** nada a declarar\n"
    "  - **Pendente:** nenhum\n"
)


def _verde_com_handover(tmp_path: Path, extra_t3: bool = False) -> Path:
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
    diario = repo / "docs" / "DIARIO_DE_OBRAS.md"
    diario.write_text(
        diario.read_text(encoding="utf-8").replace(
            "# Diário de Obras (fixture verde)\n", "# Diário de Obras (fixture verde)\n**Diretiva de priorização:** Priorize `P-0001`.\n"
        ).replace("| P-0001 | Plano alfa | ready |", "| P-0001 | Plano alfa | ready 1/2 |"),
        encoding="utf-8",
    )
    plano = repo / "docs" / "plans" / "P-0001-alfa.md"
    texto = plano.read_text(encoding="utf-8") + _HANDOVER_T1 + (
        "\n### ALF-T2 — Segunda tarefa [Sonnet · classe implementacao]\n- **Status:** `ready` · 2026-01-03\n"
    )
    if extra_t3:
        texto += (
            "\n### ALF-T3 — Terceira tarefa [Sonnet · classe implementacao]\n- **Status:** `done` · 2026-01-04\n"
            "- **Handover:** 2026-01-04 · para `ALF-T2`, `pantonic-reviewer`\n"
            "  - **Entregue:** `gama.py:9`\n  - **Contrato:** `gama()` idempotente\n"
            "  - **Não refazer:** nada a declarar\n  - **Pendente:** nenhum\n"
        )
    plano.write_text(texto, encoding="utf-8")
    return repo


def test_tf_tk88_next_devolve_o_handover_da_antecessora(tmp_path, capsys):
    """TF do `TK-88`: sem handover endereçado, o `next` imprime, sob `=== HANDOVER DE <ID>`, o
    campo verbatim da antecessora imediata, antes do dossiê da próxima tarefa."""
    backlog = _load_backlog()
    repo = _verde_com_handover(tmp_path)

    assert backlog.main(["next", "--repo", str(repo)]) == 0
    saida = capsys.readouterr().out
    assert saida.startswith("=== PRÓXIMA TAREFA: ALF-T2 — Segunda tarefa")
    assert "=== HANDOVER DE ALF-T1 — Primeira tarefa (done; docs/plans/P-0001-alfa.md)" in saida
    assert _HANDOVER_T1.rstrip("\n") in saida
    assert saida.index("=== HANDOVER DE") < saida.index("--- dossiê")

    modelo = backlog.carregar(repo)
    t1 = backlog._localizar(modelo, "ALF-T1")
    assert backlog.extrair_handover(t1) == _HANDOVER_T1.rstrip("\n")
    assert backlog.extrair_handover(backlog._localizar(modelo, "ALF-T2")) is None


def test_tf_tk88_handover_enderecado_vence_a_antecessora(tmp_path, capsys):
    """TF do `TK-88`: irmão cujo cabeçalho nomeia a sucessora em `para` é devolvido, e a
    antecessora sem endereço fica de fora — a nomenclatura decide, não a posição."""
    backlog = _load_backlog()
    repo = _verde_com_handover(tmp_path, extra_t3=True)

    assert backlog.main(["next", "--repo", str(repo)]) == 0
    saida = capsys.readouterr().out
    assert "=== HANDOVER DE ALF-T3 — Terceira tarefa" in saida
    assert "=== HANDOVER DE ALF-T1" not in saida
    assert "`gama()` idempotente" in saida


# --------------------------------------------------------------------------- #
# TK-86a — o piso do C-11 vem de `docs/PISO_C11.tsv` do repositório checado
# --------------------------------------------------------------------------- #


def test_piso_c11_tsv_ausente_nao_acusa_c17(tmp_path, capsys):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
    backlog.main(["check", "--repo", str(repo)])
    assert "C-17" not in capsys.readouterr().out


def test_piso_c11_tsv_entrada_orfa_e_linha_malformada(tmp_path, capsys):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
    (repo / "docs" / "PISO_C11.tsv").write_bytes(
        "arquivo\tsecao\torigem\nGOVERNANCA.md\t9.9\tteste\nlixo\n".encode("utf-8")
    )
    assert backlog.main(["check", "--repo", str(repo)]) == 1
    saida = capsys.readouterr().out
    assert any("piso_c11 nomeia entrada órfã" in l and "9.9" in l for l in saida.splitlines())
    assert "C-17 docs/PISO_C11.tsv:3 — linha fora do esquema" in saida


# --------------------------------------------------------------------------- #
# AF-T10 (`DAF-41`) — `despachar`: um comando roda as conferências do despacho e
# recusa pela primeira que falhar. Cópia isolada da fixture `pasta` em `tmp_path`,
# nunca sobre o repositório real.
# --------------------------------------------------------------------------- #

_GAM_PLANO_DESPACHAR_TEXTO = (
    "# P-0 — Plano gama\n"
    "\n"
    "**Prefixo das tarefas no diário:** `GAM-T<n>`\n"
    "\n"
    "### GAM-T1 — Primeira tarefa [Sonnet · classe implementacao]\n"
    "- **Objetivo:** fixture.\n"
    "- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.\n"
    "- **Verificação:**\n"
    "  1. `python -c \"print('a')\"` → `b` — antes `a`, depois `b`\n"
    "- **Pronto quando:** fixture existe.\n"
    "\n"
    "### GAM-T2 — Segunda tarefa [Sonnet · classe implementacao]\n"
    "- **Objetivo:** fixture.\n"
    "- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.\n"
    "- **Verificação:**\n"
    "  1. `python -c \"print('a')\"` → `b` — antes `z`, depois `b`\n"
    "- **Pronto quando:** fixture existe.\n"
)


def _run_git_despachar(args: list[str], cwd: Path) -> None:
    resultado = subprocess.run(["git", *args], cwd=str(cwd), capture_output=True, text=True)
    assert resultado.returncode == 0, f"git {args}: {resultado.stderr}"


def _montar_repo_despachar(tmp_path: Path, nome: str = "repo") -> Path:
    """`DAF-41` — cópia em quatro tempos, ensaiada pelo consultor no redespacho: (a) fixture
    `pasta`; (b) `rdo.py`/`caminhos.py` reais em `.claude/tools/` da cópia (`card_check` carrega
    `rdo.py` de `<root>/.claude/tools/`, e `rdo.py` carrega `caminhos.py` ao lado — sem eles o
    gate `card_check` recusa com `rdo.py: módulo não encontrado`); (c) `docs/plans/P-0-gama/plano.md`
    sobrescrito com os campos que `rdo.extrair_dossie` exige (`Objetivo`, `Verificação`, `Pronto
    quando` e exatamente um entre `Arquivos-alvo`/`Entregável`) — `GAM-T1` o `card_check` aceita,
    `GAM-T2` recusa (`antes` `z` contra a saída real `a`); (d) `git init` + commit inicial com
    tudo, para `review_evidence.py --capturar-ref` ter uma árvore para gravar. A fixture do
    repositório não muda — só a cópia."""
    repo = _copiar_fixture(_FIXTURE_PASTA, tmp_path / nome)
    ferramentas = repo / ".claude" / "tools"
    ferramentas.mkdir(parents=True, exist_ok=True)
    shutil.copy2(_ROOT / ".claude" / "tools" / "rdo.py", ferramentas / "rdo.py")
    shutil.copy2(_ROOT / ".claude" / "tools" / "caminhos.py", ferramentas / "caminhos.py")
    (repo / "docs" / "plans" / "P-0-gama" / "plano.md").write_text(
        _GAM_PLANO_DESPACHAR_TEXTO, encoding="utf-8"
    )
    _run_git_despachar(["init"], repo)
    _run_git_despachar(["config", "user.email", "teste@example.com"], repo)
    _run_git_despachar(["config", "user.name", "Teste"], repo)
    _run_git_despachar(["add", "-A"], repo)
    _run_git_despachar(["commit", "-m", "baseline"], repo)
    return repo


def test_tf_despachar_grava_estado_e_imprime_ref(tmp_path, capsys):
    """TF da AF-T10: `despachar GAM-T1` roda as conferências do despacho, materializa
    `in-progress` em `estado.tsv` e imprime o `<ref>` capturado, gravado em
    `tarefa-corrente.json`."""
    backlog = _load_backlog()
    repo = _montar_repo_despachar(tmp_path)

    assert backlog.main(["despachar", "GAM-T1", "--repo", str(repo)]) == 0

    saida = capsys.readouterr().out
    linha_ref = next(l for l in saida.splitlines() if l.startswith("ref="))
    ref = linha_ref[len("ref="):]
    assert ref

    estado_tsv = (repo / "docs" / "plans" / "P-0-gama" / "estado.tsv").read_text(encoding="utf-8")
    linha_gam_t1 = next(l for l in estado_tsv.splitlines() if l.startswith("GAM-T1\t"))
    assert linha_gam_t1.split("\t")[2] == "in-progress"

    estado_corrente = json.loads(
        (repo / ".claude" / "estado" / "tarefa-corrente.json").read_text(encoding="utf-8")
    )
    assert estado_corrente["tarefa"] == "GAM-T1"
    assert estado_corrente["ref"] == ref


def test_tr_despachar_recusa_no_primeiro_gate_sem_escrever(tmp_path, capsys):
    """TR da AF-T10: `GAM-T2` tem `Verificação` que o `card_check` recusa (`antes` `z` contra a
    saída real `a`) — a regra concorrente "materializa e depois confere" deixaria `in-progress`
    gravado em `estado.tsv`; a regra certa recusa antes de escrever qualquer coisa."""
    backlog = _load_backlog()
    repo = _montar_repo_despachar(tmp_path)
    estado_path = repo / "docs" / "plans" / "P-0-gama" / "estado.tsv"
    estado_antes = estado_path.read_bytes()
    tarefa_corrente = repo / ".claude" / "estado" / "tarefa-corrente.json"

    assert backlog.main(["despachar", "GAM-T2", "--repo", str(repo)]) == 1

    erro = capsys.readouterr().err
    assert "despachar: recusado — card_check:" in erro
    # `AE-14` (`DAF-42`): a razão atravessa a fronteira do subprocesso decodificada em UTF-8 —
    # com a codificação do locale (cp1252) sai `nÃ£o fecham`.
    assert "não fecham" in erro
    assert estado_path.read_bytes() == estado_antes
    assert not tarefa_corrente.exists()


def test_tf_despachar_redespacho_reaproveita_ref(tmp_path, capsys):
    """TF da AF-T10: redespacho — `tarefa-corrente.json` já é de `GAM-T1` com `ref` `abc`
    (tarefa de volta a `ready`) — a saída reaproveita esse `ref` em vez de capturar um novo."""
    backlog = _load_backlog()
    repo = _montar_repo_despachar(tmp_path)
    estado_dir = repo / ".claude" / "estado"
    estado_dir.mkdir(parents=True, exist_ok=True)
    (estado_dir / "tarefa-corrente.json").write_text(
        json.dumps({"tarefa": "GAM-T1", "ref": "abc"}), encoding="utf-8"
    )

    assert backlog.main(["despachar", "GAM-T1", "--repo", str(repo)]) == 0

    saida = capsys.readouterr().out
    assert "ref=abc" in saida.splitlines()


def test_tr_despachar_mundo_depois_redespacha_tarefa_ja_aplicada(tmp_path, capsys):
    """TR (`AE-26` do `P-0753`): tarefa cuja entrega já está na árvore (o `depois` do card casa e
    o `antes` não) — `despachar` sem `--mundo` recusa pelo `card_check`; com `--mundo depois`
    passa, materializa `in-progress` e reaproveita o `ref` do primeiro despacho. Antes não havia
    como: o redespacho só-verificações ia a mão (`card_check --mundo depois` e `status`)."""
    backlog = _load_backlog()
    repo = _montar_repo_despachar(tmp_path)
    plano = repo / "docs" / "plans" / "P-0-gama" / "plano.md"
    plano.write_text(
        plano.read_text(encoding="utf-8").replace(
            "→ `b` — antes `a`, depois `b`", "→ `a` — antes `z`, depois `a`", 1
        ),
        encoding="utf-8",
    )
    estado_dir = repo / ".claude" / "estado"
    estado_dir.mkdir(parents=True, exist_ok=True)
    (estado_dir / "tarefa-corrente.json").write_text(
        json.dumps({"tarefa": "GAM-T1", "ref": "abc"}), encoding="utf-8"
    )

    assert backlog.main(["despachar", "GAM-T1", "--repo", str(repo)]) == 1
    assert "despachar: recusado — card_check:" in capsys.readouterr().err

    assert backlog.main(["despachar", "GAM-T1", "--mundo", "depois", "--repo", str(repo)]) == 0

    assert "ref=abc" in capsys.readouterr().out.splitlines()
    estado_tsv = (repo / "docs" / "plans" / "P-0-gama" / "estado.tsv").read_text(encoding="utf-8")
    linha_gam_t1 = next(l for l in estado_tsv.splitlines() if l.startswith("GAM-T1\t"))
    assert linha_gam_t1.split("\t")[2] == "in-progress"
