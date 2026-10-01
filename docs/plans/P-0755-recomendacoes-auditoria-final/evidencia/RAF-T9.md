# Evidência de revisão — P-0755 RAF-T9

## Diff (`git diff --stat`)
```
.claude/tools/review_evidence.py                   | 39 ++++++++++++++++--
 docs/DIARIO_DE_OBRAS.md                            |  4 +-
 .../estado.tsv                                     |  2 +-
 docs/telemetria.tsv                                |  1 +
 tests/test_review_evidence.py                      | 46 ++++++++++++++++++++++
 5 files changed, 85 insertions(+), 7 deletions(-)
```

## Arquivos tocados
- `.claude/tools/review_evidence.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `5e787d7d163bb075cba55f913d385220d1f1da11`
- Arquivos-alvo declarados: `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`
- Arquivos tocados: `.claude/tools/review_evidence.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/telemetria.tsv`, `tests/test_review_evidence.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index c0ceb1f..4517a57 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -65,7 +65,6 @@ from __future__ import annotations
 
 import argparse
 import difflib
-import fnmatch
 import importlib.util
 import json
 import os
@@ -431,10 +430,42 @@ def _eh_alvo_diretorio(root: Path, alvo: str) -> bool:
 
 def _eh_alvo_curinga(alvo: str) -> bool:
     """AUF-T3 (`DAU-22`): verdadeiro quando o alvo contém `*` — casa contra os tocados por
-    `fnmatch`, nunca por expansão contra a árvore inteira."""
+    `_casa_curinga`, nunca por expansão contra a árvore inteira."""
     return "*" in alvo
 
 
+def _curinga_para_regex(padrao: str) -> str:
+    """RAF-T9 (`DRF-31`): traduz o curinga do alvo para regex como a linha de comando o lê —
+    `**/` vira zero ou mais pastas, `**` sem `/` seguinte vira qualquer coisa, `*` fica preso a
+    uma pasta e `?` a um caractere dentro dela; o resto entra literal via `re.escape`."""
+    partes: list[str] = []
+    i = 0
+    n = len(padrao)
+    while i < n:
+        if padrao[i : i + 3] == "**/":
+            partes.append("(?:[^/]*/)*")
+            i += 3
+        elif padrao[i : i + 2] == "**":
+            partes.append(".*")
+            i += 2
+        elif padrao[i] == "*":
+            partes.append("[^/]*")
+            i += 1
+        elif padrao[i] == "?":
+            partes.append("[^/]")
+            i += 1
+        else:
+            partes.append(re.escape(padrao[i]))
+            i += 1
+    return "".join(partes)
+
+
+def _casa_curinga(caminho: str, padrao: str) -> bool:
+    """RAF-T9 (`DRF-31`): `caminho` casa com o curinga do alvo `padrao`, na tradução própria de
+    `_curinga_para_regex` (sem `fnmatch`, sem `glob`, sem `PurePath.full_match`)."""
+    return re.fullmatch(_curinga_para_regex(padrao), caminho) is not None
+
+
 _REGISTRO_ORQUESTRACAO = (
     "docs/DIARIO_DE_OBRAS.md",
     "docs/telemetria.tsv",
@@ -561,7 +592,7 @@ def confrontar_escopo(
         tocado_norm = _normalizar_separador(tocado)
         if any(tocado_norm.startswith(prefixo) for prefixo in prefixos_dir):
             return True
-        return any(fnmatch.fnmatchcase(tocado_norm, alvo) for alvo in alvos_curinga)
+        return any(_casa_curinga(tocado_norm, alvo) for alvo in alvos_curinga)
 
     de_outra_tarefa: dict[str, str] = {}
     registro: list[str] = []
@@ -699,7 +730,7 @@ def montar_trechos(
             casados = [
                 arquivo
                 for arquivo in (tocados or [])
-                if fnmatch.fnmatchcase(_normalizar_separador(arquivo), alvo_norm)
+                if _casa_curinga(_normalizar_separador(arquivo), alvo_norm)
             ]
             if not casados:
                 trechos[caminho] = {

```

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index 49bc925..d493fc6 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -1873,3 +1873,49 @@ def test_tf_marca_e_rotulo_registro_da_orquestracao_na_lista(tmp_path):
         in documento
     )
     assert "- `docs/nota.txt` — atribuição: alheio; estado git: `??`" in documento
+
+
+def test_tf_glob_estrela_nao_atravessa_pasta(tmp_path):
+    """RAF-T9 (`DRF-31`): a estrela simples do curinga do alvo casa como na linha de comando —
+    presa a uma pasta. `relatorios/*.md` cobre `relatorios/a.md`, mas não `relatorios/sub/x.md`
+    (hoje o `fnmatch` casa os dois, porque `*` também atravessa `/`)."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    ref = review_evidence.capturar_ref(repo)
+
+    (repo / "relatorios").mkdir()
+    (repo / "relatorios" / "sub").mkdir()
+    (repo / "relatorios" / "a.md").write_text("linha-a\n", encoding="utf-8")
+    (repo / "relatorios" / "sub" / "x.md").write_text("linha-x\n", encoding="utf-8")
+
+    alvos = ["relatorios/*.md"]
+    tocados = review_evidence.coletar_arquivos_tocados(repo, desde=ref)
+
+    assert review_evidence.confrontar_escopo(tocados, alvos, repo)["fora_dos_alvos"] == [
+        "relatorios/sub/x.md"
+    ]
+    trechos = review_evidence.montar_trechos(repo, alvos, 4000, tocados, desde=ref)
+    assert set(trechos.keys()) == {"relatorios/a.md"}
+
+
+def test_tf_glob_estrela_dupla_alcanca_subpastas(tmp_path):
+    """RAF-T9 (`DRF-31`): a estrela dupla do curinga do alvo alcança as subpastas, como na linha
+    de comando. `relatorios/**/*.md` cobre `relatorios/a.md` e `relatorios/sub/x.md` (hoje o
+    `fnmatch` deixa `relatorios/a.md` de fora, porque exige uma `/` depois de `relatorios/`)."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    ref = review_evidence.capturar_ref(repo)
+
+    (repo / "relatorios").mkdir()
+    (repo / "relatorios" / "sub").mkdir()
+    (repo / "relatorios" / "a.md").write_text("linha-a\n", encoding="utf-8")
+    (repo / "relatorios" / "sub" / "x.md").write_text("linha-x\n", encoding="utf-8")
+
+    alvos = ["relatorios/**/*.md"]
+    tocados = review_evidence.coletar_arquivos_tocados(repo, desde=ref)
+
+    assert review_evidence.confrontar_escopo(tocados, alvos, repo)["fora_dos_alvos"] == []
+    trechos = review_evidence.montar_trechos(repo, alvos, 4000, tocados, desde=ref)
+    assert set(trechos.keys()) == {"relatorios/a.md", "relatorios/sub/x.md"}

```

## Medida do executor
- ausente: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T9-medida.json não existe

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
