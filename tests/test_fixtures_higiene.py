"""EBK-T6 (`docs/plans/P-0751-esgotar-backlog.md` `### EBK-T6`) — nenhuma fixture sob
`tests/fixtures/` pode carregar um nome que o harness descobre como skill/config real
(`SKILL.md`, `CLAUDE.md`, `AGENTS.md`, `settings.json`, `settings.local.json`). Caso medido
(2026-09-20): uma fixture do `TK-60a` continha `SKILL.md` e o harness passou a listá-la como
skill invocável real."""
from __future__ import annotations

from pathlib import Path

_RAIZ = Path(__file__).resolve().parent / "fixtures"

_NOMES_DE_DESCOBERTA = {
    "SKILL.md",
    "CLAUDE.md",
    "AGENTS.md",
    "settings.json",
    "settings.local.json",
}


def nomes_de_descoberta(raiz: Path) -> list[Path]:
    """Lista, sob `raiz`, todo arquivo cujo nome é um dos nomes que o harness descobre."""
    return sorted(
        caminho
        for caminho in raiz.rglob("*")
        if caminho.is_file() and caminho.name in _NOMES_DE_DESCOBERTA
    )


def test_tf_ebk_6_acusa_arquivo_de_descoberta(tmp_path):
    (tmp_path / "a").mkdir()
    (tmp_path / "a" / "SKILL.md").write_text("x", encoding="utf-8")

    assert nomes_de_descoberta(tmp_path) == [tmp_path / "a" / "SKILL.md"]


def test_tf_ebk_6_sem_arquivo_de_descoberta(tmp_path):
    (tmp_path / "a").mkdir()
    (tmp_path / "a" / "outro.md").write_text("x", encoding="utf-8")

    assert nomes_de_descoberta(tmp_path) == []


def test_tr_ebk_6_fixtures_reais_nao_carregam_nome_de_descoberta():
    encontrados = nomes_de_descoberta(_RAIZ)

    assert encontrados == [], (
        "fixture(s) sob tests/fixtures/ com nome que o harness descobre: "
        f"{[str(p) for p in encontrados]}"
    )
