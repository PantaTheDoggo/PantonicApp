# Evidência de revisão — P-0753 AF-T3

## Diff (`git diff --stat`)
```
.claude/tools/progresso_hook.py                    | 10 +++++
 docs/ARMADILHAS_DE_FERRAMENTA.md                   |  1 +
 docs/DIARIO_DE_OBRAS.md                            |  2 +-
 docs/plans/P-0753-auditoria-estagio-1/estado.tsv   |  2 +-
 .../evidencia/P-0753-AF-T3-medida.json             | 43 ++++++++++++++++++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_progresso_hook.py                       | 42 +++++++++++++++++++++
 7 files changed, 99 insertions(+), 2 deletions(-)
```

## Arquivos tocados
- `.claude/tools/progresso_hook.py` — atribuição: da entrega; estado git: `??`
- `docs/ARMADILHAS_DE_FERRAMENTA.md` — atribuição: da entrega; estado git: `??`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T3-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_progresso_hook.py` — atribuição: da entrega; estado git: `??`

## Escopo
- Recorte: desde `3d0eef66df3758aa1da9aca1204da85c4c9a536f`
- Arquivos-alvo declarados: `.claude/tools/progresso_hook.py`, `tests/test_progresso_hook.py`, `docs/ARMADILHAS_DE_FERRAMENTA.md`
- Arquivos tocados: `.claude/tools/progresso_hook.py`, `docs/ARMADILHAS_DE_FERRAMENTA.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T3-medida.json`, `docs/telemetria.tsv`, `tests/test_progresso_hook.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T3-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/progresso_hook.py`
```
--- .claude/tools/progresso_hook.py@3d0eef66df3758aa1da9aca1204da85c4c9a536f
+++ .claude/tools/progresso_hook.py
@@ -302,6 +302,16 @@
         return None
     i = 1
     while i < len(tokens) and tokens[i].startswith("-"):
+        opcao = tokens[i]
+        if opcao == "-m":
+            if i + 1 >= len(tokens):
+                return None
+            return (tokens[i + 1], tokens[i + 2:])
+        if opcao == "-c":
+            return None
+        if opcao in ("-X", "-W"):
+            i += 2
+            continue
         i += 1
     if i >= len(tokens):
         return None

```

### `tests/test_progresso_hook.py`
```
--- tests/test_progresso_hook.py@3d0eef66df3758aa1da9aca1204da85c4c9a536f
+++ tests/test_progresso_hook.py
@@ -1354,3 +1354,45 @@
         'Tarefa "Um título de teste": vou reunir para o revisor o que mudou desde o despacho, '
         "os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.",
     ]
+
+
+# --- AF-T3: o painel reconhece o programa depois das opções do interpretador -----------
+
+
+def test_tf_opcao_do_interpretador_com_valor_gera_m2(estado, raiz):
+    rodar(payload_next(
+        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
+        "- **Objetivo:** Fazer x.\n"
+    ), estado, raiz)
+
+    p_in_progress = P(
+        hook_event_name="PreToolUse", tool_name="Bash",
+        tool_input={"command": "python -X utf8 .claude/tools/backlog.py status TLG-T9 in-progress"},
+    )
+    assert rodar(p_in_progress, estado, raiz) == 0
+    assert progresso(estado)[-1] == (
+        'Tarefa "Um título de teste": gates aprovados; vou materializar in-progress '
+        "e gravar o ponto de partida."
+    )
+
+
+def test_tr_opcao_do_interpretador_sem_valor_segue_gerando_m2(estado, raiz):
+    rodar(payload_next(
+        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
+        "- **Objetivo:** Fazer x.\n"
+    ), estado, raiz)
+
+    p_in_progress = P(
+        hook_event_name="PreToolUse", tool_name="Bash",
+        tool_input={"command": "python -u .claude/tools/backlog.py status TLG-T9 in-progress"},
+    )
+    assert rodar(p_in_progress, estado, raiz) == 0
+    assert progresso(estado)[-1] == (
+        'Tarefa "Um título de teste": gates aprovados; vou materializar in-progress '
+        "e gravar o ponto de partida."
+    )
+
+
+def test_tf_opcao_do_interpretador_m_e_c():
+    assert progresso_hook._programa(["python", "-m", "pytest", "-q"]) == ("pytest", ["-q"])
+    assert progresso_hook._programa(["python", "-c", "print(1)"]) is None

```

### `docs/ARMADILHAS_DE_FERRAMENTA.md`
```
--- docs/ARMADILHAS_DE_FERRAMENTA.md@3d0eef66df3758aa1da9aca1204da85c4c9a536f
+++ docs/ARMADILHAS_DE_FERRAMENTA.md
@@ -13,5 +13,6 @@
 | `markdown` | escape de markdown (`\*`) e soft-wrap vazando para literal de aceite | (`AE-19`, `AE-23` do `P-0740`) | o literal de aceite se copia da linha física do arquivo, nunca do texto renderizado nem através de quebra de linha, e se confirma antes de publicar com `python -c` que imprime a contagem dele no arquivo. |
 | `Python` | console cp1252 estoura `UnicodeEncodeError` ao imprimir `→` | (`TK-65b`, e de novo na autoria deste plano, 2026-09-26) | `python -X utf8`, ou `sys.stdout.reconfigure(encoding='utf-8')` antes do primeiro `print`. |
 | `Bash` (ferramenta do agente) | a ferramenta Bash reduz `\\` a `\` antes de o bash ler o comando — entre aspas simples, entre aspas duplas e em heredoc, com ou sem aspas no delimitador | (`P-0752`, 2026-09-26: `python -c "import sys;print(repr(sys.argv[1]))" 'a\\tb'` imprime `'a\\tb'` pela ferramenta Bash e `'a\\\\tb'` pela ferramenta PowerShell) | arquivo que leva barra invertida se grava com Write/Edit, nunca por heredoc; comando com `\\` literal vai pela ferramenta PowerShell com aspas simples, ou a barra entra por `chr(92)` dentro do `python -c`. |
+| `Python` (linha de comando) | opção do interpretador antes do script (`-X utf8`, `-W`, `-m`, `-c`) desloca o nome do programa: quem lê a linha pulando só o token iniciado por `-` toma o valor da opção (`utf8`) pelo script | (`R-06` da auditoria de encerramento do estágio 1, 2026-09-27: com `python -X utf8`, o painel do gerente calou `M-2`, `M-5`, `M-10`, `M-13` e `M-18`) | quem lê a linha de comando pula a opção junto com o valor dela (`-X`, `-W`), toma o módulo depois de `-m` como programa e não procura script depois de `-c` — é o que `progresso_hook._programa` faz. |
 
 Regra: linha de Verificação prefere `python -c` a shell; PowerShell só com `pwsh -Command` e aspas simples.

```

## Medida do executor
- Arquivo: docs\plans\P-0753-auditoria-estagio-1\evidencia\P-0753-AF-T3-medida.json; mundo: depois; gerado em: 2026-09-27T12:17:13+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_progresso_hook.py -q -k "opcao_do_interpretador"` | 0 | true |
| 2 | `python -c "import importlib.util as u;from pathlib import Path;s=u.spec_from_file_location('p',Path('.claude/tools/progresso_hook.py'));m=u.module_from_spec(s);s.loader.exec_module(m);print(m._programa(['python','-X','utf8','.claude/tools/backlog.py','status'])[0])"` | 0 | true |
| 3 | `python -c "from pathlib import Path;print(Path('docs/ARMADILHAS_DE_FERRAMENTA.md').read_text(encoding='utf-8').count('progresso_hook._programa'))"` | 0 | true |
| 4 | `python -m pytest -q` | 0 | true |
| 5 | `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
