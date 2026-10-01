# Evidência de revisão — P-0755 RAF-T6a

## Diff (`git diff --stat`)
```
.claude/global/hooks/pytest_pretooluse.py          | 12 +++++---
 docs/DIARIO_DE_OBRAS.md                            |  4 +--
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T6a-medida.json           | 29 ++++++++++++++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_pytest_pretooluse.py                    | 34 ++++++++++++++++++++++
 6 files changed, 75 insertions(+), 7 deletions(-)
```

## Arquivos tocados
- `.claude/global/hooks/pytest_pretooluse.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T6a-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_pytest_pretooluse.py` — atribuição: da entrega; estado git: `??`

## Escopo
- Recorte: desde `af627672777636a17d1f84aff13a04d0cc2f9781`
- Arquivos-alvo declarados: `.claude/global/hooks/pytest_pretooluse.py`, `tests/test_pytest_pretooluse.py`
- Arquivos tocados: `.claude/global/hooks/pytest_pretooluse.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T6a-medida.json`, `docs/telemetria.tsv`, `tests/test_pytest_pretooluse.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T6a-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/global/hooks/pytest_pretooluse.py`
```
diff --git a/.claude/global/hooks/pytest_pretooluse.py b/.claude/global/hooks/pytest_pretooluse.py
index b930e53..31aad7b 100644
--- a/.claude/global/hooks/pytest_pretooluse.py
+++ b/.claude/global/hooks/pytest_pretooluse.py
@@ -2,8 +2,10 @@
 canalizar a saida pelo pytest_filter.py, reduzindo a ingestao de contexto.
 
 Regras de seguranca:
-- So reescreve comandos que invocam pytest SEM pipe/redirecionamento proprio
-  (se o agente ja filtra ou redireciona, respeita a intencao original).
+- So reescreve comandos que invocam pytest SEM pipe simples ou redirecionamento
+  proprio (se o agente ja filtra ou redireciona, respeita a intencao original).
+  A recusa e do pipe simples (`|`) e do redirecionamento (`<`, `>`); o `||`
+  nao conta como pipe, e um separador de comando, como `&&`.
 - Nao reescreve --collect-only/--co (a listagem e o proprio resultado util).
 - Bypass explicito: incluir "#nofilter" no fim do comando.
 - A sintaxe gerada (`cmd 2>&1 | python filter`) funciona igual em bash e pwsh.
@@ -19,8 +21,10 @@ import sys
 
 FILTER_PATH = "C:/Users/panta/.claude/hooks/pytest_filter.py"
 
+PIPE_OU_REDIRECIONAMENTO_RE = re.compile(r"(?<!\|)\|(?!\|)|[<>]")
+
 PYTEST_RE = re.compile(
-    r"(?:^|[;&]\s*)"                                    # inicio ou apos ; / &&
+    r"(?:^|[;&|\n]\s*)"                                 # inicio ou apos ; / & / | / quebra de linha
     r"(?:\S*python(?:3)?(?:\.exe)?\s+-m\s+)?"           # opcional: python -m
     r"(?:\S*[/\\])?pytest(?:\.exe)?(?:\s|$)"            # pytest / caminho/pytest
 )
@@ -125,7 +129,7 @@ def main() -> None:
 
     cmd = (data.get("tool_input") or {}).get("command") or ""
 
-    if any(ch in cmd for ch in "|<>"):
+    if PIPE_OU_REDIRECIONAMENTO_RE.search(cmd):
         passthrough()
     if "#nofilter" in cmd or "pytest_filter" in cmd:
         passthrough()

```

### `tests/test_pytest_pretooluse.py`
```
--- tests/test_pytest_pretooluse.py@af627672777636a17d1f84aff13a04d0cc2f9781
+++ tests/test_pytest_pretooluse.py
@@ -87,6 +87,40 @@
     assert stdout.strip() == "{}"
 
 
+def test_tf_hook_reescreve_o_pytest_antes_do_ou_logico():
+    filtro = _filtro_path_esperado()
+    stdout = _rodar_hook("Bash", "pytest -q || echo falhou")
+    saida = json.loads(stdout)
+
+    esperado = (
+        '{ pytest -q; echo "__PYTEST_EXIT__=$?"; } 2>&1 | python "%s" || echo falhou'
+        % filtro
+    )
+    assert saida["hookSpecificOutput"]["updatedInput"]["command"] == esperado
+
+
+def test_tf_hook_reescreve_o_pytest_depois_do_ou_logico_e_da_quebra_de_linha():
+    filtro = _filtro_path_esperado()
+    bloco = '{ pytest -q; echo "__PYTEST_EXIT__=$?"; } 2>&1 | python "%s"' % filtro
+
+    stdout_ou_logico = _rodar_hook("Bash", "false || pytest -q")
+    saida_ou_logico = json.loads(stdout_ou_logico)
+    assert saida_ou_logico["hookSpecificOutput"]["updatedInput"]["command"] == (
+        "false || %s" % bloco
+    )
+
+    stdout_quebra_de_linha = _rodar_hook("Bash", "cd x\npytest -q")
+    saida_quebra_de_linha = json.loads(stdout_quebra_de_linha)
+    assert saida_quebra_de_linha["hookSpecificOutput"]["updatedInput"]["command"] == (
+        "cd x\n%s" % bloco
+    )
+
+
+def test_tr_hook_pipe_simples_e_redirecionamento_seguem_passthrough():
+    assert _rodar_hook("Bash", "pytest -q | tail -5").strip() == "{}"
+    assert _rodar_hook("Bash", "pytest -q > out.txt").strip() == "{}"
+
+
 def test_tf_filtro_sai_com_o_exit_do_marcador(tmp_path):
     entrada = "3 passed in 0.10s\n__PYTEST_EXIT__=5\n"
 

```

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T6a-medida.json; mundo: depois; gerado em: 2026-09-29T03:10:28+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_pytest_pretooluse.py::test_tf_hook_reescreve_o_pytest_antes_do_ou_logico -q` | 0 | true |
| 2 | `python -m pytest tests/test_pytest_pretooluse.py::test_tf_hook_reescreve_o_pytest_depois_do_ou_logico_e_da_quebra_de_linha -q` | 0 | true |
| 3 | `python -m pytest tests/test_pytest_pretooluse.py::test_tr_hook_pipe_simples_e_redirecionamento_seguem_passthrough -q` | 0 | true |

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
