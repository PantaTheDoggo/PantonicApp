# Evidência de revisão — P-0755 RAF-T5

## Diff (`git diff --stat`)
```
.claude/tools/backlog_hook.py                      |  7 ++-
 docs/DIARIO_DE_OBRAS.md                            |  4 +-
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T5-medida.json            | 15 +++++
 docs/telemetria.tsv                                |  1 +
 tests/test_backlog_hook.py                         | 65 ++++++++++++++++++++++
 6 files changed, 90 insertions(+), 4 deletions(-)
```

## Arquivos tocados
- `.claude/tools/backlog_hook.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T5-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_backlog_hook.py` — atribuição: da entrega; estado git: `??`

## Escopo
- Recorte: desde `9f93ad422017a1d725df9b17556a2ed8a1bfc5e6`
- Arquivos-alvo declarados: `.claude/tools/backlog_hook.py`, `tests/test_backlog_hook.py`
- Arquivos tocados: `.claude/tools/backlog_hook.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T5-medida.json`, `docs/telemetria.tsv`, `tests/test_backlog_hook.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T5-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/backlog_hook.py`
```
diff --git a/.claude/tools/backlog_hook.py b/.claude/tools/backlog_hook.py
index c969246..8ebda4e 100644
--- a/.claude/tools/backlog_hook.py
+++ b/.claude/tools/backlog_hook.py
@@ -31,6 +31,7 @@ def _carregar_caminhos():
 _caminhos = _carregar_caminhos()
 
 _GATILHO = "proximo passo"
+_PREFIXOS_NAO_DONO = ("<agent-message", "[SYSTEM NOTIFICATION")
 
 
 def _norm(text: str) -> str:
@@ -52,7 +53,11 @@ def _carregar_backlog():
 
 
 def _casa_gatilho(prompt) -> bool:
-    return isinstance(prompt, str) and _GATILHO in _norm(prompt)
+    if not isinstance(prompt, str):
+        return False
+    if prompt.lstrip().startswith(_PREFIXOS_NAO_DONO):
+        return False
+    return _GATILHO in _norm(prompt)
 
 
 def _texto_next(modulo, repo: Path) -> str:

```

### `tests/test_backlog_hook.py`
```
(arquivo novo — ausente em `9f93ad422017a1d725df9b17556a2ed8a1bfc5e6`)
--- tests/test_backlog_hook.py@9f93ad422017a1d725df9b17556a2ed8a1bfc5e6
+++ tests/test_backlog_hook.py
@@ -0,0 +1,65 @@
+"""RAF-T5 (`docs/plans/P-0755-recomendacoes-auditoria-final/plano.md` `### RAF-T5`) — o gatilho
+do próximo passo em `.claude/tools/backlog_hook.py` responde só à mensagem do dono: relato de
+subagente (`<agent-message`) e aviso do sistema (`[SYSTEM NOTIFICATION`) não disparam, mesmo
+contendo a frase `próximo passo`.
+
+Carrega o hook por caminho (`.claude/tools/` não é pacote importável), fora da série de
+`tests/test_backlog.py` (que é de `backlog.py`, `DRF-9`)."""
+from __future__ import annotations
+
+import importlib.util
+from pathlib import Path
+
+_ROOT = Path(__file__).resolve().parent.parent
+_HOOK_PATH = _ROOT / ".claude" / "tools" / "backlog_hook.py"
+
+
+def _load_hook():
+    spec = importlib.util.spec_from_file_location("backlog_hook_raf_t5", _HOOK_PATH)
+    modulo = importlib.util.module_from_spec(spec)
+    spec.loader.exec_module(modulo)
+    return modulo
+
+
+class _BacklogFalso:
+    def carregar(self, repo):
+        raise RuntimeError("backlog falso")
+
+
+def test_tf_relato_de_subagente_com_proximo_passo_nao_injeta(tmp_path):
+    hook = _load_hook()
+    payload = {
+        "prompt": (
+            '<agent-message from="pantonic-planner">Próximo passo de quem conduz: '
+            "despachar.</agent-message>"
+        )
+    }
+
+    resultado = hook.processar(payload, repo=tmp_path, backlog_module=_BacklogFalso())
+
+    assert resultado is None
+
+
+def test_tf_aviso_do_sistema_com_proximo_passo_nao_injeta(tmp_path):
+    hook = _load_hook()
+    payload = {
+        "prompt": "  [SYSTEM NOTIFICATION] tarefa concluída; próximo passo do loop."
+    }
+
+    resultado = hook.processar(payload, repo=tmp_path, backlog_module=_BacklogFalso())
+
+    assert resultado is None
+
+
+def test_tr_mensagem_do_dono_com_proximo_passo_segue_injetando(tmp_path):
+    hook = _load_hook()
+    payload = {"prompt": "execute o próximo passo"}
+
+    resultado = hook.processar(payload, repo=tmp_path, backlog_module=_BacklogFalso())
+
+    assert resultado == {
+        "hookSpecificOutput": {
+            "hookEventName": "UserPromptSubmit",
+            "additionalContext": "backlog_hook: falha ao rodar next: backlog falso",
+        }
+    }

```

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T5-medida.json; mundo: depois; gerado em: 2026-09-29T02:42:51+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_backlog_hook.py -q` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 1
  ```
  docs\audits\sonda-2026-09-28\passos.py:13: docs.audits.sonda-2026-09-28.passos.passo (function) - sem chamador de producao alcancavel
  dead_code: FALHOU - 1 achado(s) de simbolo de producao sem chamador.
  ```
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): não conforme
- Veredito mecânico (`testes`): conforme
