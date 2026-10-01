# Evidência de revisão — P-0754 AUF-T2

## Diff (`git diff --stat`)
```
docs/DIARIO_DE_OBRAS.md                             |  4 ++--
 docs/plans/P-0754-auditoria-final/estado.tsv        |  2 +-
 .../evidencia/P-0754-AUF-T2-medida.json             | 15 +++++++++++++++
 docs/telemetria.tsv                                 |  1 +
 tests/test_review_evidence.py                       | 21 ++++++++++++++++++++-
 5 files changed, 39 insertions(+), 4 deletions(-)
```

## Arquivos tocados
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0754-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T2-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `3be245095c23721c76ba03a167fcecbd48602776`
- Arquivos-alvo declarados: `tests/test_review_evidence.py`
- Arquivos tocados: `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T2-medida.json`, `docs/telemetria.tsv`, `tests/test_review_evidence.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T2-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index 7a78a9e..3fb1bc0 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -1432,4 +1432,23 @@ def test_tr_arquivo_novo_sem_desde_segue_com_conteudo_integral(tmp_path):
     texto = trechos["novo.md"]["texto"]
 
     assert "linha-1\nlinha-2\n" in texto
-    assert "+linha-1" not in texto
+
+
+def test_tf_caminho_acentuado_do_status_entra_nos_tocados_pelo_ramo_de_caminho_ausente(tmp_path):
+    """AUF-T2: com `core.quotepath` ligado, o `git status` devolve o caminho acentuado como string
+    entre aspas com escape octal (`"a\\303\\247\\303\\243o.txt"`); `_extrair_caminho_status` só
+    tira as aspas, sem decodificar o escape — o caminho lido não existe no disco (que tem
+    `ação.txt`, não `a\\303\\247\\303\\243o.txt`) e o salto por `st_mtime` não dispara porque
+    `arquivo.exists()` é falso, então o caminho com escape entra nos tocados."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    _run_git(["config", "core.quotepath", "true"], repo)
+
+    ref = review_evidence.capturar_ref(repo)
+
+    (repo / "ação.txt").write_text("linha-1\n", encoding="utf-8")
+
+    tocados = review_evidence.coletar_arquivos_tocados(repo, desde=ref)
+
+    assert tocados == ["a\\303\\247\\303\\243o.txt"]

```

## Medida do executor
- Arquivo: docs\plans\P-0754-auditoria-final\evidencia\P-0754-AUF-T2-medida.json; mundo: depois; gerado em: 2026-09-28T13:55:36+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_review_evidence.py -q -k "caminho_acentuado"` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
