# Evidência de revisão — P-0755 RAF-T32

## Diff (`git diff --stat`)
```
.claude/tools/progresso_hook.py                    | 34 +++++++++++++++++--
 docs/ACIONAMENTOS_CONSULTOR.tsv                    |  1 +
 docs/DIARIO_DE_OBRAS.md                            |  4 +--
 .../cenario.md                                     | 11 ++++--
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T32-medida-depois.json    | 15 +++++++++
 .../P-0755-recomendacoes-auditoria-final/plano.md  |  5 +--
 docs/telemetria.tsv                                |  3 ++
 tests/test_progresso_hook.py                       | 39 ++++++++++++++++++++++
 9 files changed, 105 insertions(+), 9 deletions(-)
```

## Arquivos tocados
- `.claude/tools/progresso_hook.py` — atribuição: da entrega; estado git: ` M`
- `docs/ACIONAMENTOS_CONSULTOR.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/cenario.md` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T32-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_progresso_hook.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `b1b6481300943a9d4b63cb2fffc200a88306bc40`
- Arquivos-alvo declarados: `.claude/tools/progresso_hook.py`, `tests/test_progresso_hook.py`
- Arquivos tocados: `.claude/tools/progresso_hook.py`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/cenario.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T32-medida-depois.json`, `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`, `docs/telemetria.tsv`, `tests/test_progresso_hook.py`
- Registro da orquestração (não atribuível a tarefa): `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/cenario.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T32-medida-depois.json`, `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/progresso_hook.py`
```
diff --git a/.claude/tools/progresso_hook.py b/.claude/tools/progresso_hook.py
index cf4698d..1b2c012 100644
--- a/.claude/tools/progresso_hook.py
+++ b/.claude/tools/progresso_hook.py
@@ -190,6 +190,28 @@ def frase(id_frase: str, lacunas: dict[str, str]) -> str:
     return s
 
 
+# `R-16`, `DRF-18` do `P-0755`: o painel lê a linha de abertura do despacho (`despacho:
+# P-<n> <ID>`) antes de recorrer à tarefa corrente do loop; a gramática do `ID` é a do
+# `telemetria_hook.py`, sem import cruzado.
+_RE_LINHA_DESPACHO = re.compile(
+    r"^despacho: P-\d+ ([A-Z][A-Z0-9]*-T\d+[a-z]?|TK-\d+[a-z]?) *$",
+    re.MULTILINE,
+)
+
+
+def tarefa_do_despacho(prompt: str, raiz: Path) -> tuple[str, str, str] | None:
+    """`(ID, título, objetivo)` da linha de abertura do despacho no prompt do subagente
+    despachado, pelo `localizar_card`; sem a linha, `None` — o painel recorre então à tarefa
+    corrente do loop (`R-16`, `DRF-18` do `P-0755`). Não escreve em `estado_loop`: só escolhe
+    o título mostrado."""
+    encontrado = _RE_LINHA_DESPACHO.search(prompt)
+    if not encontrado:
+        return None
+    tid = encontrado.group(1)
+    titulo, objetivo, _ = localizar_card(tid, raiz)
+    return (tid, titulo, objetivo)
+
+
 def tarefa_corrente(estado_loop: dict, estado: Path, raiz: Path) -> tuple[str, str, str]:
     if estado_loop.get("tarefa"):
         return (estado_loop.get("tarefa"), estado_loop.get("titulo", ""), estado_loop.get("objetivo", ""))
@@ -444,7 +466,11 @@ def evento(payload: dict, estado_loop: dict, estado: Path, raiz: Path) -> tuple[
 
     elif ev == "PreToolUse" and tool == "Agent" and sub in PAPEIS:
         estado_loop.pop("relatorio", None)
-        _, titulo, objetivo = tarefa_corrente(estado_loop, estado, raiz)
+        despacho = tarefa_do_despacho(str(ti.get("prompt", "")), raiz)
+        if despacho:
+            _, titulo, objetivo = despacho
+        else:
+            _, titulo, objetivo = tarefa_corrente(estado_loop, estado, raiz)
         if sub == "pantonic-executor":
             if objetivo:
                 linhas.append(frase("M-3", {"<título>": titulo, "<objetivo>": objetivo}))
@@ -468,7 +494,11 @@ def evento(payload: dict, estado_loop: dict, estado: Path, raiz: Path) -> tuple[
         if isinstance(r, dict) and r.get("handback") == "send" and isinstance(r.get("agentId"), str):
             estado_loop.setdefault("pendentes", {})[r["agentId"]] = sub
         else:
-            _, titulo, _ = tarefa_corrente(estado_loop, estado, raiz)
+            despacho = tarefa_do_despacho(str(ti.get("prompt", "")), raiz)
+            if despacho:
+                _, titulo, _ = despacho
+            else:
+                _, titulo, _ = tarefa_corrente(estado_loop, estado, raiz)
             linhas = de_volta(sub, resp, titulo)
 
     elif ev == "UserPromptSubmit":

```

### `tests/test_progresso_hook.py`
```
diff --git a/tests/test_progresso_hook.py b/tests/test_progresso_hook.py
index 81f2327..2dcaeb6 100644
--- a/tests/test_progresso_hook.py
+++ b/tests/test_progresso_hook.py
@@ -1458,3 +1458,42 @@ def test_tr_card_de_tiquete_segue_com_o_titulo_do_card(tmp_path):
     assert progresso_hook.localizar_card("TK-9a", tmp_path) == (
         "O card do tíquete", "fixture.", "Um tíquete de teste",
     )
+
+
+# --- Testes -----------------------------------------------------------------------
+
+
+def _despachar_agente(estado, raiz, sub, prompt):
+    p = P(hook_event_name="PreToolUse", tool_name="Agent",
+          tool_input={"subagent_type": sub, "prompt": prompt})
+    rodar(p, estado, raiz)
+    return progresso(estado)[-1]
+
+
+def test_tf_tarefa_do_despacho_no_painel_vence_a_corrente(estado, raiz):
+    rodar(payload_next(
+        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
+        "- **Objetivo:** Fazer x.\n"
+    ), estado, raiz)
+
+    ultima = _despachar_agente(
+        estado, raiz, "pantonic-consultant", "despacho: P-9999 TLG-T10\ncenario=x"
+    )
+
+    assert ultima == 'Agente consultor recebe a tarefa "Outro título" e vai triar.'
+    estado_loop = json.loads((estado / progresso_hook.ESTADO_ARQ).read_text(encoding="utf-8"))
+    assert estado_loop["tarefa"] == "TLG-T9"
+
+
+def test_tr_tarefa_do_despacho_ausente_segue_a_corrente(estado, raiz):
+    rodar(payload_next(
+        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
+        "- **Objetivo:** Fazer x.\n"
+    ), estado, raiz)
+
+    assert _despachar_agente(estado, raiz, "pantonic-reviewer", "Revise.") == (
+        'Agente revisor recebe a tarefa "Um título de teste" e vai confrontar a entrega com o card.'
+    )
+    assert _despachar_agente(estado, raiz, "pantonic-planner", "despacho: P-9999\nPlaneje.") == (
+        'Agente planejador recebe a tarefa "Um título de teste" e vai replanejar.'
+    )

```

## Linhas removidas dos testes
### `tests/test_progresso_hook.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T32-medida-depois.json; mundo: depois; gerado em: 2026-09-30T02:26:24+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_progresso_hook.py -q -k tarefa_do_despacho` | 0 | true |

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
