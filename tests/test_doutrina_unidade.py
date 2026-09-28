"""TR do P-0745 (PLN-T2..PLN-T5): a forma antiga da unidade de trabalho — percentual de
ocupação, tabela de tetos, tarefa atômica — não volta às residências que o plano editou."""
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


def _texto(rel: str) -> str:
    return (RAIZ / rel).read_text(encoding="utf-8")


def test_governanca_dimensiona_pela_operacao_sem_percentual():
    t = _texto("GOVERNANCA.md")
    assert "50% de ocupação" not in t
    assert "Orçamento de turnos por tarefa atômica" not in t
    assert "materialização de uma operação do modelo" in t


def test_global_claude_sem_percentual_nem_tarefa_atomica():
    t = _texto(".claude/global/CLAUDE.md")
    assert "50% de ocupação" not in t
    assert "tarefa atômica" not in t
    assert "tarefas atômicas" not in t


def test_skill_diario_formato_de_tarefa_pela_operacao():
    t = _texto(".claude/skills/diario-de-obras/SKILL.md")
    assert "## Formato de uma tarefa atômica" not in t
    assert "## Formato de uma tarefa\n" in t
    assert "materialização de uma operação do modelo" in t


def test_planner_decompoe_o_modelo_sem_percentual():
    t = _texto(".claude/agents/pantonic-planner.md")
    assert "atômic" not in t
    assert "50%" not in t
    assert "~80 linhas" not in t
    assert "SAÍDA 3" in t
    assert "Fase 3b" in t


def test_conduta_do_planejador_nao_remete_a_tabela_aposentada():
    t = _texto(".claude/agents/pantonic-planner.md")
    assert "tabela de classes" not in t
    assert "tabela de tetos" not in t
    assert "Nenhum teto se escreve no" in t


def test_modelador_devolve_lastro_como_saida_literal():
    t = _texto(".claude/agents/pantonic-model-designer.md")
    assert "Só cinco violações" in t
    assert "`V1` e `V3`" in t
    g = _texto("GOVERNANCA.md")
    assert "**Lastro.**" in g
    assert "**Rascunho antes do Marco 1.**" in g


def test_gate_do_modelador_nao_classifica_lastro_como_secao():
    t = _texto(".claude/agents/pantonic-model-designer.md")
    assert "exceto `V1` e `V3`" in t
    assert "(`V6`, `V7`, `V15`, `V17`)" not in t
    assert "Só cinco violações" in t


def test_readme_nao_defende_a_regua_aposentada():
    t = _texto("README.md")
    assert "Orçamento de turnos" not in t
    assert "Um teto único para tudo" not in t
    assert "Teto de turnos graduado por classe" not in t
    assert "calibrar tetos" not in t
    assert "calibração dos tetos" not in t
    assert "não cabe em ≤30" not in t
    assert "71 turnos e ~189 mil tokens" in t
