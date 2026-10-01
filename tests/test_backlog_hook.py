"""RAF-T5 (`docs/plans/P-0755-recomendacoes-auditoria-final/plano.md` `### RAF-T5`) — o gatilho
do próximo passo em `.claude/tools/backlog_hook.py` responde só à mensagem do dono: relato de
subagente (`<agent-message`) e aviso do sistema (`[SYSTEM NOTIFICATION`) não disparam, mesmo
contendo a frase `próximo passo`.

Carrega o hook por caminho (`.claude/tools/` não é pacote importável), fora da série de
`tests/test_backlog.py` (que é de `backlog.py`, `DRF-9`)."""
from __future__ import annotations

import importlib.util
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
_HOOK_PATH = _ROOT / ".claude" / "tools" / "backlog_hook.py"


def _load_hook():
    spec = importlib.util.spec_from_file_location("backlog_hook_raf_t5", _HOOK_PATH)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


class _BacklogFalso:
    def carregar(self, repo):
        raise RuntimeError("backlog falso")


def test_tf_relato_de_subagente_com_proximo_passo_nao_injeta(tmp_path):
    hook = _load_hook()
    payload = {
        "prompt": (
            '<agent-message from="pantonic-planner">Próximo passo de quem conduz: '
            "despachar.</agent-message>"
        )
    }

    resultado = hook.processar(payload, repo=tmp_path, backlog_module=_BacklogFalso())

    assert resultado is None


def test_tf_aviso_do_sistema_com_proximo_passo_nao_injeta(tmp_path):
    hook = _load_hook()
    payload = {
        "prompt": "  [SYSTEM NOTIFICATION] tarefa concluída; próximo passo do loop."
    }

    resultado = hook.processar(payload, repo=tmp_path, backlog_module=_BacklogFalso())

    assert resultado is None


def test_tr_mensagem_do_dono_com_proximo_passo_segue_injetando(tmp_path):
    hook = _load_hook()
    payload = {"prompt": "execute o próximo passo"}

    resultado = hook.processar(payload, repo=tmp_path, backlog_module=_BacklogFalso())

    assert resultado == {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": "backlog_hook: falha ao rodar next: backlog falso",
        }
    }
