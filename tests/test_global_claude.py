"""TR: `.claude/global/CLAUDE.md` carrega os Controles 1.1 e 1.2 da Regra 1."""

from pathlib import Path

CLAUDE_MD = Path(__file__).resolve().parent.parent / ".claude" / "global" / "CLAUDE.md"


def test_controles_1_1_e_1_2_entre_regra_1_e_regra_2():
    texto = CLAUDE_MD.read_text(encoding="utf-8")

    pos_regra1 = texto.index("## Regra 1 —")
    pos_regra2 = texto.index("## Regra 2 —")

    assert texto.count("### Controle 1.1 —") == 1
    assert texto.count("### Controle 1.2 —") == 1

    pos_controle_1_1 = texto.index("### Controle 1.1 —")
    pos_controle_1_2 = texto.index("### Controle 1.2 —")

    assert pos_regra1 < pos_controle_1_1 < pos_controle_1_2 < pos_regra2
