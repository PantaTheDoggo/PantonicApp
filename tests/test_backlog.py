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

import importlib.util
import shutil
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_BACKLOG_PATH = _ROOT / ".claude" / "tools" / "backlog.py"
_FIXTURES = Path(__file__).resolve().parent / "fixtures" / "backlog"
_FIXTURE_VERDE = _FIXTURES / "verde"
_FIXTURE_VERMELHO = _FIXTURES / "vermelho"


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
