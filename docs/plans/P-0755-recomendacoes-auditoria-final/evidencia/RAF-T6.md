# Evidência de revisão — P-0755 RAF-T6

## Diff (`git diff --stat`)
```
.claude/global/hooks/pytest_filter.py              |  22 ++++-
 .claude/global/hooks/pytest_pretooluse.py          |  92 +++++++++++++++++-
 docs/DIARIO_DE_OBRAS.md                            |   4 +-
 .../estado.tsv                                     |   2 +-
 .../evidencia/P-0755-RAF-T6-medida.json            |  15 +++
 docs/telemetria.tsv                                |   1 +
 tests/test_pytest_pretooluse.py                    | 105 +++++++++++++++++++++
 7 files changed, 233 insertions(+), 8 deletions(-)
```

## Arquivos tocados
- `.claude/global/hooks/pytest_filter.py` — atribuição: da entrega; estado git: ` M`
- `.claude/global/hooks/pytest_pretooluse.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T6-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_pytest_pretooluse.py` — atribuição: da entrega; estado git: `??`

## Escopo
- Recorte: desde `c3456146706d9adc703bbce08421db2f5e24af3a`
- Arquivos-alvo declarados: `.claude/global/hooks/pytest_pretooluse.py`, `.claude/global/hooks/pytest_filter.py`, `tests/test_pytest_pretooluse.py`
- Arquivos tocados: `.claude/global/hooks/pytest_filter.py`, `.claude/global/hooks/pytest_pretooluse.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T6-medida.json`, `docs/telemetria.tsv`, `tests/test_pytest_pretooluse.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T6-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/global/hooks/pytest_pretooluse.py`
```
diff --git a/.claude/global/hooks/pytest_pretooluse.py b/.claude/global/hooks/pytest_pretooluse.py
index f098f03..b930e53 100644
--- a/.claude/global/hooks/pytest_pretooluse.py
+++ b/.claude/global/hooks/pytest_pretooluse.py
@@ -7,6 +7,11 @@ Regras de seguranca:
 - Nao reescreve --collect-only/--co (a listagem e o proprio resultado util).
 - Bypass explicito: incluir "#nofilter" no fim do comando.
 - A sintaxe gerada (`cmd 2>&1 | python filter`) funciona igual em bash e pwsh.
+- Comando encadeado (`&&`, `||`, `;`, quebra de linha): so o segmento que
+  invoca o pytest entra no bloco filtrado; o resto do comando fica como esta.
+  O bloco grava um marcador com o exit code real do pytest
+  (`__PYTEST_EXIT__=...`) antes do pipe, e o pytest_filter.py devolve esse
+  exit code no lugar do exit code do proprio pipe.
 """
 import json
 import re
@@ -20,12 +25,95 @@ PYTEST_RE = re.compile(
     r"(?:\S*[/\\])?pytest(?:\.exe)?(?:\s|$)"            # pytest / caminho/pytest
 )
 
+# Mesmo casamento de PYTEST_RE, mas ancorado no inicio do segmento (sem o
+# prefixo de inicio-de-comando ou separador): usado para testar se o texto de
+# UM segmento (ja dividido por dividir_segmentos) e uma invocacao do pytest.
+SEGMENTO_PYTEST_RE = re.compile(
+    r"^(?:\S*python(?:3)?(?:\.exe)?\s+-m\s+)?(?:\S*[/\\])?pytest(?:\.exe)?(?:\s|$)"
+)
+
 
 def passthrough() -> None:
     print("{}")
     sys.exit(0)
 
 
+def dividir_segmentos(cmd: str) -> list[str]:
+    """Divide `cmd` alternando segmento e separador (`&&`, `||`, `;` ou
+    quebra de linha), reconhecendo o separador so fora de aspas simples ou
+    duplas. A primeira e a ultima parte sao sempre segmentos; `"".join(...)`
+    do resultado reproduz `cmd`."""
+    partes: list[str] = []
+    atual: list[str] = []
+    aspas: str | None = None
+    i = 0
+    n = len(cmd)
+    while i < n:
+        ch = cmd[i]
+        if aspas is not None:
+            atual.append(ch)
+            if ch == aspas:
+                aspas = None
+            i += 1
+            continue
+        if ch in ("'", '"'):
+            aspas = ch
+            atual.append(ch)
+            i += 1
+            continue
+        if cmd[i : i + 2] in ("&&", "||"):
+            partes.append("".join(atual))
+            partes.append(cmd[i : i + 2])
+            atual = []
+            i += 2
+            continue
+        if ch in (";", "\n"):
+            partes.append("".join(atual))
+            partes.append(ch)
+            atual = []
+            i += 1
+            continue
+        atual.append(ch)
+        i += 1
+    partes.append("".join(atual))
+    return partes
+
+
+def reescrever(cmd: str, ferramenta: str) -> str | None:
+    """Reescreve so os segmentos de `cmd` que invocam o pytest, cada um no seu
+    bloco (Bash ou PowerShell conforme `ferramenta`) que grava o exit code
+    real em `__PYTEST_EXIT__` antes do pipe pelo pytest_filter.py. Segmento
+    sem pytest fica como esta. Devolve `None` se nenhum segmento casar."""
+    partes = dividir_segmentos(cmd)
+    houve = False
+    novas: list[str] = []
+    for indice, parte in enumerate(partes):
+        if indice % 2 == 1:
+            novas.append(parte)
+            continue
+        texto = parte.strip()
+        if not texto or not SEGMENTO_PYTEST_RE.match(texto):
+            novas.append(parte)
+            continue
+        prefixo = parte[: len(parte) - len(parte.lstrip())]
+        sufixo = parte[len(parte.rstrip()) :]
+        if ferramenta == "PowerShell":
+            bloco = (
+                '& { %s; "__PYTEST_EXIT__=$LASTEXITCODE" } 2>&1 | python "%s"'
+                % (texto, FILTER_PATH)
+            )
+        else:
+            bloco = (
+                '{ %s; echo "__PYTEST_EXIT__=$?"; } 2>&1 | python "%s"'
+                % (texto, FILTER_PATH)
+            )
+        novas.append(prefixo + bloco + sufixo)
+        houve = True
+    if not houve:
+        return None
+    return "".join(novas)
+
+
 def main() -> None:
     try:
  
```
[truncado em 4000 caracteres]

### `.claude/global/hooks/pytest_filter.py`
```
diff --git a/.claude/global/hooks/pytest_filter.py b/.claude/global/hooks/pytest_filter.py
index bf3cb5d..76c6fb7 100644
--- a/.claude/global/hooks/pytest_filter.py
+++ b/.claude/global/hooks/pytest_filter.py
@@ -4,9 +4,11 @@ Le a saida completa do pytest via stdin, grava o log integral em
 %TEMP%/claude/pytest_last_run.log e imprime apenas o que importa para o agente:
 secoes FAILURES/ERRORS, o short test summary e a linha de sumario final.
 
-Exit code: 0 se a suite passou; 1 se houve falha/erro/saida irreconhecivel
-(permite ao agente detectar falha mesmo com o pipe engolindo o exit code
-original do pytest).
+Exit code: se a entrada trouxer o marcador `__PYTEST_EXIT__=<n>` (gravado
+pelo pytest_pretooluse.py antes do pipe, no comando encadeado), o filtro sai
+com esse `<n>` - o exit code real do pytest. Sem marcador: 0 se a suite
+passou; 1 se houve falha/erro/saida irreconhecivel (permite ao agente
+detectar falha mesmo com o pipe engolindo o exit code original do pytest).
 """
 import os
 import re
@@ -27,6 +29,7 @@ PLAIN_SUMMARY_RE = re.compile(
     r"^(no tests ran|\d+ (passed|failed|errors?|skipped|xfailed|xpassed|deselected|warnings?)\b.*)"
     r" in \d+(\.\d+)?s"
 )
+MARCADOR_EXIT_RE = re.compile(r"^__PYTEST_EXIT__=(-?\d+)$")
 
 
 def main() -> None:
@@ -36,7 +39,15 @@ def main() -> None:
     except Exception:
         pass
 
-    lines = sys.stdin.read().splitlines()
+    lines_lidas = sys.stdin.read().splitlines()
+    marcador_exit = None
+    lines = []
+    for ln in lines_lidas:
+        m = MARCADOR_EXIT_RE.match(ln.strip())
+        if m:
+            marcador_exit = int(m.group(1))
+            continue
+        lines.append(ln)
 
     log_dir = os.path.join(tempfile.gettempdir(), "claude")
     log_path = os.path.join(log_dir, "pytest_last_run.log")
@@ -85,6 +96,9 @@ def main() -> None:
         note += " (saida filtrada acima foi truncada; use Grep no log)"
     print(note)
 
+    if marcador_exit is not None:
+        sys.exit(marcador_exit)
+
     summary = lines[summary_idx] if summary_idx is not None else ""
     failed = summary == "" or bool(FAILURE_HINT_RE.search(summary))
     sys.exit(1 if failed else 0)

```

### `tests/test_pytest_pretooluse.py`
```
(arquivo novo — ausente em `c3456146706d9adc703bbce08421db2f5e24af3a`)
--- tests/test_pytest_pretooluse.py@c3456146706d9adc703bbce08421db2f5e24af3a
+++ tests/test_pytest_pretooluse.py
@@ -0,0 +1,105 @@
+"""RAF-T6 (`docs/plans/P-0755-recomendacoes-auditoria-final/plano.md` `### RAF-T6`) — o filtro da
+saída dos testes devolve o código de saída dos próprios testes, mesmo quando o comando encadeia
+outros passos depois deles.
+
+Carrega o hook e o filtro por caminho (`.claude/global/hooks/` não é pacote importável) e roda
+cada um por subprocesso: o hook recebe o JSON do evento no stdin e devolve JSON no stdout; o
+filtro recebe o texto da saída do pytest no stdin, com `TMPDIR`/`TEMP`/`TMP` apontando para
+`tmp_path`, para o log não cair na pasta temporária do usuário."""
+from __future__ import annotations
+
+import importlib.util
+import json
+import os
+import subprocess
+import sys
+from pathlib import Path
+
+_ROOT = Path(__file__).resolve().parent.parent
+_HOOK_PATH = _ROOT / ".claude" / "global" / "hooks" / "pytest_pretooluse.py"
+_FILTER_PATH = _ROOT / ".claude" / "global" / "hooks" / "pytest_filter.py"
+
+
+def _load_hook_module():
+    spec = importlib.util.spec_from_file_location("pytest_pretooluse_raf_t6", _HOOK_PATH)
+    modulo = importlib.util.module_from_spec(spec)
+    spec.loader.exec_module(modulo)
+    return modulo
+
+
+def _filtro_path_esperado() -> str:
+    return _load_hook_module().FILTER_PATH
+
+
+def _rodar_hook(tool_name: str, command: str) -> str:
+    payload = json.dumps({"tool_name": tool_name, "tool_input": {"command": command}})
+    resultado = subprocess.run(
+        [sys.executable, str(_HOOK_PATH)],
+        input=payload,
+        capture_output=True,
+        text=True,
+        check=True,
+    )
+    return resultado.stdout
+
+
+def _rodar_filtro(texto: str, tmp_path: Path) -> subprocess.CompletedProcess:
+    env = dict(os.environ)
+    env["TMPDIR"] = str(tmp_path)
+    env["TEMP"] = str(tmp_path)
+    env["TMP"] = str(tmp_path)
+    return subprocess.run(
+        [sys.executable, str(_FILTER_PATH)],
+        input=texto,
+        capture_output=True,
+        text=True,
+        env=env,
+    )
+
+
+def test_tf_hook_reescreve_so_o_segmento_do_pytest_no_bash():
+    filtro = _filtro_path_esperado()
+    stdout = _rodar_hook("Bash", 'cd x && pytest -q; echo "exit=$?"')
+    saida = json.loads(stdout)
+
+    esperado = (
+        'cd x && { pytest -q; echo "__PYTEST_EXIT__=$?"; } 2>&1 | python "%s"; echo "exit=$?"'
+        % filtro
+    )
+    assert saida["hookSpecificOutput"]["updatedInput"]["command"] == esperado
+
+
+def test_tf_hook_reescreve_so_o_segmento_do_pytest_no_powershell():
+    filtro = _filtro_path_esperado()
+    stdout = _rodar_hook("PowerShell", 'python -m pytest -q; Write-Output "fim"')
+    saida = json.loads(stdout)
+
+    esperado = (
+        '& { python -m pytest -q; "__PYTEST_EXIT__=$LASTEXITCODE" } 2>&1 | python "%s"; '
+        'Write-Output "fim"' % filtro
+    )
+    assert saida["hookSpecificOutput"]["updatedInput"]["command"] == esperado
+
+
+def test_tr_hook_sem_pytest_segue_passthrough():
+    stdout = _rodar_hook("Bash", "git status")
+
+    assert stdout.strip() == "{}"
+
+
+def test_tf_filtro_sai_com_o_exit_do_marcador(tmp_path):
+    entrada = "3 passed in 0.10s\n__PYTEST_EXIT__=5\n"
+
+    resultado = _rodar_filtro(entrada, tmp_path)
+
+    assert resultado.returncode == 5
+    assert "__PYTEST_EXIT__" not in resultado.stdout
+    assert "3 passed in 0.10s" in resultado.stdout
+
+
+def test_tr_filtro_sem_marcador_segue_pelo_sumario(tmp_path):
+    falhou = _rodar_filtro("1 failed, 2 passed in 0.10s\n", tmp_path)
+    assert falhou.returncode == 1
+
+    passou = _rodar_filtro("3 passed in 0.10s\n", tmp_path)
+    assert passou.returncode == 0

```

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T6-medida.json; mundo: depois; gerado em: 2026-09-29T02:52:09+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_pytest_pretooluse.py -q` | 0 | true |

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
