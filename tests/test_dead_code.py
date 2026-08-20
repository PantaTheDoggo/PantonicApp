"""T5a (docs/plans/P-0731-v2-extracao-modalidade.md ### T5a) — infraestrutura mínima
de suíte do hub e âncora do comportamento de `.claude/checks/dead_code.py` quanto às
virtuais despachadas por framework; estendida pela T5b, que trocou o mecanismo de uma
tabela embutida (Qt) para o ponto de extensão `<root>/.claude/framework-virtuals.txt`
declarado pelo projeto varrido.

`.claude/checks/` não é pacote importável (diretório com ponto no nome) — o módulo é
carregado por caminho via `importlib.util.spec_from_file_location`. A asserção é sobre
a lista de achados devolvida por `check()`, nunca sobre stdout/CLI (`main()` fica fora
do escopo destes testes).
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_DEAD_CODE_PATH = _ROOT / ".claude" / "checks" / "dead_code.py"
_FIXTURE_ROOT = Path(__file__).resolve().parent / "fixtures" / "qt_project"
_UNDECLARED_FIXTURE_ROOT = Path(__file__).resolve().parent / "fixtures" / "qt_project_undeclared"


def _load_dead_code():
    spec = importlib.util.spec_from_file_location("dead_code", _DEAD_CODE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_tf_qt_virtual_override_not_flagged():
    """Override de virtual (`paint`) em classe derivada de framework não aparece nos
    achados quando o projeto declara `QWidget`/`paint` em
    `qt_project/.claude/framework-virtuals.txt` (T5b) — mesmo resultado que a tabela
    embutida (`_QT_VIRTUAL_METHODS`/`_is_qt_derived`) produzia antes da troca de
    mecanismo, agora por declaração do projeto em vez de conhecimento do check."""
    dead_code = _load_dead_code()
    findings = dead_code.check(_FIXTURE_ROOT)
    assert not any("MyWidget.paint" in finding for finding in findings)


def test_tr_orphan_symbol_is_flagged():
    """Símbolo de produção órfão do mesmo fixture aparece nos achados — trava contra
    o falso-verde de "não varreu nada" (se o sweep não rodasse, este também sumiria)."""
    dead_code = _load_dead_code()
    findings = dead_code.check(_FIXTURE_ROOT)
    assert any("orphan_function" in finding for finding in findings)


def test_tr_undeclared_framework_virtual_is_flagged():
    """TR da T5b: mesma forma de classe/método de `qt_project/widget.py`, mas em
    `qt_project_undeclared/` — sem `.claude/framework-virtuals.txt`. Sem declaração,
    nenhuma exceção é concedida: `MyWidget.paint` MUST aparecer nos achados, provando
    que o ponto de extensão não vira exceção "de graça" (comportamento padrão do
    check, alheio a qualquer framework, é preservado quando o projeto não declara
    nada)."""
    dead_code = _load_dead_code()
    findings = dead_code.check(_UNDECLARED_FIXTURE_ROOT)
    assert any("MyWidget.paint" in finding for finding in findings)
