"""FPU-T4 (`docs/plans/P-0752-fato-no-ponto-de-uso.md` `### FPU-T4`) — TFs/TR de
`.claude/tools/crenca_hook.py`: gancho `PreToolUse` (`Write|Edit`) que avisa, no ato de gravar
plano ou diário, todo número de aceite que chega sem comando (DFP-5).

Padrão de carga do módulo idêntico a `tests/test_progresso_hook.py:23-31`
(`.claude/` não é pacote importável).
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_CRENCA_HOOK_PATH = _ROOT / ".claude" / "tools" / "crenca_hook.py"


def _load_crenca_hook():
    spec = importlib.util.spec_from_file_location("crenca_hook", _CRENCA_HOOK_PATH)
    modulo = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = modulo
    spec.loader.exec_module(modulo)
    return modulo


crenca_hook = _load_crenca_hook()


def test_tf_numero_sem_comando_avisa(capsys):
    payload = {
        "hook_event_name": "PreToolUse",
        "tool_name": "Write",
        "tool_input": {
            "file_path": "docs/plans/P-0752-fato-no-ponto-de-uso.md",
            "content": "A suíte fechou com 410 passed nesta rodada.",
        },
    }

    assert crenca_hook.main(entrada=json.dumps(payload)) == 0

    saida = json.loads(capsys.readouterr().out)
    assert saida["systemMessage"] == (
        "1 número(s) de aceite sem comando no texto novo: número sem comando é crença — "
        "medir antes de gravar"
    )


def test_tf_numero_na_linha_do_comando_nao_avisa(capsys):
    payload = {
        "hook_event_name": "PreToolUse",
        "tool_name": "Edit",
        "tool_input": {
            "file_path": "docs/plans/P-0752-fato-no-ponto-de-uso.md",
            "new_string": "1. `python -m pytest -q` → verde — antes `397 passed`",
        },
    }

    assert crenca_hook.main(entrada=json.dumps(payload)) == 0

    assert capsys.readouterr().out == ""


def test_tf_fora_de_docs_plans_nao_avisa(capsys):
    payload = {
        "hook_event_name": "PreToolUse",
        "tool_name": "Write",
        "tool_input": {
            "file_path": "src/modulo.py",
            "content": "resultado: 410 passed",
        },
    }

    assert crenca_hook.main(entrada=json.dumps(payload)) == 0

    assert capsys.readouterr().out == ""


def test_tr_payload_invalido_sai_zero(capsys):
    assert crenca_hook.main(entrada="") == 0

    assert capsys.readouterr().out == ""


def test_tf_literais_sobrepostos_contam_uma_vez():
    texto = "antes `397 passed`, depois `401 passed`"
    assert crenca_hook.contar_crencas(texto) == 2
