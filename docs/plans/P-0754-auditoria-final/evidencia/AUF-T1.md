# Evidência de revisão — P-0754 AUF-T1

## Diff (`git diff --stat`)
```
.claude/tools/review_evidence.py                   | 14 +++++++++
 docs/DIARIO_DE_OBRAS.md                            |  4 +--
 docs/plans/P-0754-auditoria-final/estado.tsv       |  2 +-
 .../evidencia/P-0754-AUF-T1-medida.json            | 15 ++++++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_review_evidence.py                      | 35 ++++++++++++++++++++++
 6 files changed, 68 insertions(+), 3 deletions(-)
```

## Arquivos tocados
- `.claude/tools/review_evidence.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0754-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T1-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `e7a3d58c1f0c4930d3cdcea22a118b25d6672e3f`
- Arquivos-alvo declarados: `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`
- Arquivos tocados: `.claude/tools/review_evidence.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T1-medida.json`, `docs/telemetria.tsv`, `tests/test_review_evidence.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T1-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index d53607e..8d81a22 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -598,6 +598,20 @@ def _diff_para_arquivo(root: Path, caminho_rel: str, desde: str | None = None) -
                 lineterm="",
             )
             return "\n".join(diff_linhas) + "\n"
+        if _eh_nao_rastreado(root, caminho_rel):
+            # AUF-T1: não rastreado ausente de `<ref>` — criado depois do recorte do despacho —
+            # chega como diff unificado contra o vazio, no molde do bloco do TK-93a acima.
+            texto_atual = _texto_do_disco(root, caminho_rel)
+            if texto_atual is None:
+                return "(arquivo binário ou não-UTF-8 — trecho omitido)"
+            diff_linhas = difflib.unified_diff(
+                [],
+                texto_atual.splitlines(),
+                fromfile=f"{caminho_rel}@{desde}",
+                tofile=caminho_rel,
+                lineterm="",
+            )
+            return "\n".join(diff_linhas) + "\n"
         texto = _git(["diff", desde, "--", caminho_rel], root)
         if texto.strip():
             return texto

```

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index 4f4185c..7a78a9e 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -1398,3 +1398,38 @@ def test_tr_evidencia_sem_medida_diz_ausente(tmp_path):
 
     assert "## Medida do executor" in documento
     assert "ausente" in documento
+
+
+def test_tf_arquivo_novo_depois_do_recorte_sai_como_diferenca(tmp_path):
+    """TF da AUF-T1: arquivo novo (não rastreado, ausente do `<ref>` capturado antes dele existir)
+    chega ao revisor como diferença — diff unificado contra o vazio, com as linhas marcadas `+` —
+    e não como o conteúdo integral do arquivo."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+
+    ref = review_evidence.capturar_ref(repo)
+
+    (repo / "novo.md").write_text("linha-1\nlinha-2\n", encoding="utf-8")
+
+    trechos = review_evidence.montar_trechos(repo, ["novo.md"], 4000, desde=ref)
+    texto = trechos["novo.md"]["texto"]
+
+    assert "+linha-1" in texto
+    assert "+linha-2" in texto
+
+
+def test_tr_arquivo_novo_sem_desde_segue_com_conteudo_integral(tmp_path):
+    """Regressão: sem `ref`/`desde`, o mesmo arquivo novo continua chegando como conteúdo
+    integral (comportamento antigo, preservado no caminho sem recorte)."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+
+    (repo / "novo.md").write_text("linha-1\nlinha-2\n", encoding="utf-8")
+
+    trechos = review_evidence.montar_trechos(repo, ["novo.md"], 4000)
+    texto = trechos["novo.md"]["texto"]
+
+    assert "linha-1\nlinha-2\n" in texto
+    assert "+linha-1" not in texto

```

## Medida do executor
- Arquivo: docs\plans\P-0754-auditoria-final\evidencia\P-0754-AUF-T1-medida.json; mundo: depois; gerado em: 2026-09-28T13:47:02+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_review_evidence.py -q -k "arquivo_novo_depois_do_recorte or arquivo_novo_sem_desde"` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
