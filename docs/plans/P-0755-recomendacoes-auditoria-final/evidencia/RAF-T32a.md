# Evidência de revisão — P-0755 RAF-T32a

## Diff (`git diff --stat`)
```
.claude/tools/progresso_hook.py                    | 10 ++++-
 docs/DIARIO_DE_OBRAS.md                            |  6 +--
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T32a-medida-depois.json   | 15 +++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_progresso_hook.py                       | 51 ++++++++++++++++++++++
 6 files changed, 80 insertions(+), 5 deletions(-)
```

## Arquivos tocados
- `.claude/tools/progresso_hook.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T32a-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_progresso_hook.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `ec60372cd5de78672834c9c235983476d443545d`
- Arquivos-alvo declarados: `.claude/tools/progresso_hook.py`, `tests/test_progresso_hook.py`
- Arquivos tocados: `.claude/tools/progresso_hook.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T32a-medida-depois.json`, `docs/telemetria.tsv`, `tests/test_progresso_hook.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T32a-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/progresso_hook.py`
```
diff --git a/.claude/tools/progresso_hook.py b/.claude/tools/progresso_hook.py
index 1b2c012..a475281 100644
--- a/.claude/tools/progresso_hook.py
+++ b/.claude/tools/progresso_hook.py
@@ -493,6 +493,10 @@ def evento(payload: dict, estado_loop: dict, estado: Path, raiz: Path) -> tuple[
         r = payload.get("tool_response")
         if isinstance(r, dict) and r.get("handback") == "send" and isinstance(r.get("agentId"), str):
             estado_loop.setdefault("pendentes", {})[r["agentId"]] = sub
+            despacho_pendente = tarefa_do_despacho(str(ti.get("prompt", "")), raiz)
+            if despacho_pendente:
+                _, titulo_pendente, _ = despacho_pendente
+                estado_loop.setdefault("titulos_pendentes", {})[r["agentId"]] = titulo_pendente
         else:
             despacho = tarefa_do_despacho(str(ti.get("prompt", "")), raiz)
             if despacho:
@@ -506,6 +510,7 @@ def evento(payload: dict, estado_loop: dict, estado: Path, raiz: Path) -> tuple[
         m = re.match(r'<agent-message from="([^"]+)">', p)
         if m:
             sub2 = estado_loop.get("pendentes", {}).pop(m.group(1), "")
+            titulo_pendente = estado_loop.get("titulos_pendentes", {}).pop(m.group(1), "")
             if sub2 in PAPEIS:
                 marca = "The report follows:"
                 idx = p.find(marca)
@@ -513,7 +518,10 @@ def evento(payload: dict, estado_loop: dict, estado: Path, raiz: Path) -> tuple[
                 fim = corpo.find("</agent-message>")
                 if fim != -1:
                     corpo = corpo[:fim]
-                _, titulo, _ = tarefa_corrente(estado_loop, estado, raiz)
+                if titulo_pendente:
+                    titulo = titulo_pendente
+                else:
+                    _, titulo, _ = tarefa_corrente(estado_loop, estado, raiz)
                 linhas = de_volta(sub2, corpo, titulo)
 
     elif ev == "Stop":

```

### `tests/test_progresso_hook.py`
```
diff --git a/tests/test_progresso_hook.py b/tests/test_progresso_hook.py
index 2dcaeb6..1d51628 100644
--- a/tests/test_progresso_hook.py
+++ b/tests/test_progresso_hook.py
@@ -1497,3 +1497,54 @@ def test_tr_tarefa_do_despacho_ausente_segue_a_corrente(estado, raiz):
     assert _despachar_agente(estado, raiz, "pantonic-planner", "despacho: P-9999\nPlaneje.") == (
         'Agente planejador recebe a tarefa "Um título de teste" e vai replanejar.'
     )
+
+
+def _devolver_agente(estado, raiz, sub, prompt, resposta, agent_id=None):
+    if agent_id is None:
+        r = {"content": [{"type": "text", "text": resposta}]}
+    else:
+        r = {"status": "completed", "agentId": agent_id, "handback": "send",
+             "content": [{"type": "text", "text": "ptr"}]}
+    rodar(P(hook_event_name="PostToolUse", tool_name="Agent",
+            tool_input={"subagent_type": sub, "prompt": prompt}, tool_response=r), estado, raiz)
+    if agent_id is not None:
+        rodar(P(hook_event_name="UserPromptSubmit", prompt=(
+            f'<agent-message from="{agent_id}">\n'
+            "[Subagent hand-back] The text below is the final report of a subagent this "
+            "session delegated to. The report follows:\n"
+            f"  {resposta}\n"
+            "</agent-message>"
+        )), estado, raiz)
+    return progresso(estado)[-1]
+
+
+def test_tf_retorno_do_despacho_assincrono_mostra_a_tarefa_despachada(estado, raiz):
+    rodar(payload_next(
+        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
+        "- **Objetivo:** Fazer x.\n"
+    ), estado, raiz)
+
+    ultima = _devolver_agente(
+        estado, raiz, "pantonic-consultant", "despacho: P-9999 TLG-T10\ncenario=x",
+        "rota=resolve", agent_id="c9",
+    )
+
+    assert ultima == 'Agente consultor devolveu a tarefa "Outro título": rota resolve.'
+    estado_loop = json.loads((estado / progresso_hook.ESTADO_ARQ).read_text(encoding="utf-8"))
+    assert estado_loop["tarefa"] == "TLG-T9"
+    assert estado_loop["pendentes"] == {}
+    assert estado_loop.get("titulos_pendentes", {}) == {}
+
+
+def test_tr_retorno_do_despacho_sincrono_mostra_a_tarefa_despachada(estado, raiz):
+    rodar(payload_next(
+        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
+        "- **Objetivo:** Fazer x.\n"
+    ), estado, raiz)
+
+    assert _devolver_agente(
+        estado, raiz, "pantonic-consultant", "despacho: P-9999 TLG-T10\ncenario=x", "rota=resolve",
+    ) == 'Agente consultor devolveu a tarefa "Outro título": rota resolve.'
+    assert _devolver_agente(
+        estado, raiz, "pantonic-consultant", "cenario=x", "rota=resolve",
+    ) == 'Agente consultor devolveu a tarefa "Um título de teste": rota resolve.'

```

## Linhas removidas dos testes
### `tests/test_progresso_hook.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T32a-medida-depois.json; mundo: depois; gerado em: 2026-09-30T02:41:41+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_progresso_hook.py -q -k retorno_do_despacho` | 0 | true |

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
