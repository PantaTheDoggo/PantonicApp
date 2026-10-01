# Evidência de revisão — P-0754 AUF-T7

## Diff (`git diff --stat`)
```
.claude/tools/progresso_hook.py                    |  4 +++
 docs/DIARIO_DE_OBRAS.md                            |  4 +--
 docs/plans/P-0754-auditoria-final/estado.tsv       |  2 +-
 .../evidencia/P-0754-AUF-T7-medida.json            | 15 +++++++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_progresso_hook.py                       | 31 ++++++++++++++++++++++
 6 files changed, 54 insertions(+), 3 deletions(-)
```

## Arquivos tocados
- `.claude/tools/progresso_hook.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0754-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T7-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_progresso_hook.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `eafa7609b6df860b2b3fc58ae472a1e5fba6e737`
- Arquivos-alvo declarados: `.claude/tools/progresso_hook.py`, `tests/test_progresso_hook.py`
- Arquivos tocados: `.claude/tools/progresso_hook.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T7-medida.json`, `docs/telemetria.tsv`, `tests/test_progresso_hook.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T7-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/progresso_hook.py`
```
diff --git a/.claude/tools/progresso_hook.py b/.claude/tools/progresso_hook.py
index 1f5c304..cf4698d 100644
--- a/.claude/tools/progresso_hook.py
+++ b/.claude/tools/progresso_hook.py
@@ -146,6 +146,7 @@ def localizar_card(id_tarefa: str, raiz: Path) -> tuple[str, str, str]:
     if diario.exists():
         arquivos.append(diario)
     padrao = re.compile(r"^### " + re.escape(id_tarefa) + r" — (.+?) \[")
+    padrao_tiquete = re.compile(r"^## " + re.escape(id_tarefa) + r" — (.+?)\s*$")
     padrao_rotulo = re.compile(r"^#+\s*(?:\S+\s+—\s+)?(.*)$")
     for arq in arquivos:
         try:
@@ -153,6 +154,9 @@ def localizar_card(id_tarefa: str, raiz: Path) -> tuple[str, str, str]:
         except OSError:
             continue
         for i, linha in enumerate(linhas):
+            mt = padrao_tiquete.match(linha)
+            if mt:
+                return (mt.group(1).strip(), "", "")
             m = padrao.match(linha)
             if not m:
                 continue

```

### `tests/test_progresso_hook.py`
```
diff --git a/tests/test_progresso_hook.py b/tests/test_progresso_hook.py
index acd4ac3..81f2327 100644
--- a/tests/test_progresso_hook.py
+++ b/tests/test_progresso_hook.py
@@ -1427,3 +1427,34 @@ def test_tr_opcao_do_interpretador_sem_valor_segue_gerando_m2(estado, raiz):
 def test_tf_opcao_do_interpretador_m_e_c():
     assert progresso_hook._programa(["python", "-m", "pytest", "-q"]) == ("pytest", ["-q"])
     assert progresso_hook._programa(["python", "-c", "print(1)"]) is None
+
+
+def test_tf_titulo_do_tiquete_em_curso(tmp_path):
+    diario = tmp_path / "docs" / "DIARIO_DE_OBRAS.md"
+    diario.parent.mkdir(parents=True)
+    diario.write_text(
+        "# Diário\n"
+        "\n"
+        "## TK-9 — Um tíquete de teste\n"
+        "\n"
+        "Corpo do tíquete.\n",
+        encoding="utf-8",
+    )
+
+    assert progresso_hook.localizar_card("TK-9", tmp_path) == ("Um tíquete de teste", "", "")
+
+
+def test_tr_card_de_tiquete_segue_com_o_titulo_do_card(tmp_path):
+    diario = tmp_path / "docs" / "DIARIO_DE_OBRAS.md"
+    diario.parent.mkdir(parents=True)
+    diario.write_text(
+        "## TK-9 — Um tíquete de teste\n"
+        "\n"
+        "### TK-9a — O card do tíquete [Sonnet · classe implementacao]\n"
+        "- **Objetivo:** fixture.\n",
+        encoding="utf-8",
+    )
+
+    assert progresso_hook.localizar_card("TK-9a", tmp_path) == (
+        "O card do tíquete", "fixture.", "Um tíquete de teste",
+    )

```

## Medida do executor
- Arquivo: docs\plans\P-0754-auditoria-final\evidencia\P-0754-AUF-T7-medida.json; mundo: depois; gerado em: 2026-09-28T14:42:22+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_progresso_hook.py -q -k "tiquete"` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
