# Evidência de revisão — P-0754 AUF-T3

## Diff (`git diff --stat`)
```
.claude/tools/review_evidence.py                   | 45 +++++++++++--
 docs/DIARIO_DE_OBRAS.md                            |  4 +-
 docs/plans/P-0754-auditoria-final/estado.tsv       |  2 +-
 .../evidencia/P-0754-AUF-T3-medida.json            | 15 +++++
 docs/telemetria.tsv                                |  1 +
 tests/test_review_evidence.py                      | 76 ++++++++++++++++++++++
 6 files changed, 136 insertions(+), 7 deletions(-)
```

## Arquivos tocados
- `.claude/tools/review_evidence.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0754-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T3-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `0170d3027b45aa7d9184f77e17292cfc3ccf7185`
- Arquivos-alvo declarados: `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`
- Arquivos tocados: `.claude/tools/review_evidence.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T3-medida.json`, `docs/telemetria.tsv`, `tests/test_review_evidence.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T3-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index 8d81a22..c3ed620 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -65,6 +65,7 @@ from __future__ import annotations
 
 import argparse
 import difflib
+import fnmatch
 import importlib.util
 import json
 import os
@@ -121,7 +122,7 @@ def _load_rdo(root: Path):
     return modulo
 
 
-_CAMINHO_RE = re.compile(r"^[A-Za-z0-9_.][A-Za-z0-9_./\\-]*$")
+_CAMINHO_RE = re.compile(r"^[A-Za-z0-9_.*][A-Za-z0-9_./\\*-]*$")
 _EXTENSAO_RE = re.compile(r"\.[A-Za-z0-9]+$")
 
 
@@ -400,6 +401,12 @@ def _eh_alvo_diretorio(root: Path, alvo: str) -> bool:
     return (root / alvo).is_dir()
 
 
+def _eh_alvo_curinga(alvo: str) -> bool:
+    """AUF-T3 (`DAU-22`): verdadeiro quando o alvo contém `*` — casa contra os tocados por
+    `fnmatch`, nunca por expansão contra a árvore inteira."""
+    return "*" in alvo
+
+
 _REGISTRO_ORQUESTRACAO = (
     "docs/DIARIO_DE_OBRAS.md",
     "docs/telemetria.tsv",
@@ -515,13 +522,18 @@ def confrontar_escopo(
         for alvo in arquivos_alvo
         if _eh_alvo_diretorio(root, alvo)
     ]
+    alvos_curinga = [
+        _normalizar_separador(alvo) for alvo in arquivos_alvo if _eh_alvo_curinga(alvo)
+    ]
     outros = alvos_de_outras_tarefas or {}
 
     def coberto(tocado: str) -> bool:
         if tocado in alvo_set:
             return True
         tocado_norm = _normalizar_separador(tocado)
-        return any(tocado_norm.startswith(prefixo) for prefixo in prefixos_dir)
+        if any(tocado_norm.startswith(prefixo) for prefixo in prefixos_dir):
+            return True
+        return any(fnmatch.fnmatchcase(tocado_norm, alvo) for alvo in alvos_curinga)
 
     de_outra_tarefa: dict[str, str] = {}
     registro: list[str] = []
@@ -611,7 +623,8 @@ def _diff_para_arquivo(root: Path, caminho_rel: str, desde: str | None = None) -
                 tofile=caminho_rel,
                 lineterm="",
             )
-            return "\n".join(diff_linhas) + "\n"
+            marca = f"(arquivo novo — ausente em `{desde}`)\n"
+            return marca + "\n".join(diff_linhas) + "\n"
         texto = _git(["diff", desde, "--", caminho_rel], root)
         if texto.strip():
             return texto
@@ -623,9 +636,12 @@ def _diff_para_arquivo(root: Path, caminho_rel: str, desde: str | None = None) -
     caminho_abs = root / caminho_rel
     if caminho_abs.is_file():
         try:
-            return caminho_abs.read_text(encoding="utf-8")
+            conteudo = caminho_abs.read_text(encoding="utf-8")
         except UnicodeDecodeError:
             return "(arquivo binário ou não-UTF-8 — trecho omitido)"
+        if _eh_nao_rastreado(root, caminho_rel):
+            return "(arquivo novo — ausente em `HEAD`)\n" + conteudo
+        return conteudo
     return "(sem diferença coletável — arquivo ausente na árvore de trabalho)"
 
 
@@ -646,6 +662,27 @@ def montar_trechos(
     algum item de `arquivos_alvo` é diretório; alvo-arquivo comum segue o caminho de sempre."""
     trechos: dict[str, dict] = {}
     for caminho in arquivos_alvo:
+        if _eh_alvo_curinga(caminho):
+            alvo_norm = _normalizar_separador(caminho)
+            casados = [
+                arquivo
+                for arquivo in (tocados or [])
+                if fnmatch.fnmatchcase(_normalizar_separador(arquivo), alvo_norm)
+            ]
+            if not casados:
+                trechos[caminho] = {
+                    "texto": "(nenhum arquivo tocado casa com o curinga)",
+                    "truncado": False,
+                }
+                continue
+            for arquivo in casados:
+                texto = _diff_para_arquivo(root, arquivo, desde)
+                truncado = len(texto) > teto_chars
+                trechos[arquivo] = {
+                    "texto": texto[:teto_chars] if truncado else texto,
+                    "truncado": truncado,
+                }
+            continue

```
[truncado em 4000 caracteres]

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index ffd59a0..87a6920 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -1453,3 +1453,79 @@ def test_tf_caminho_acentuado_do_status_entra_nos_tocados_pelo_ramo_de_caminho_a
     tocados = review_evidence.coletar_arquivos_tocados(repo, desde=ref)
 
     assert tocados == ["a\\303\\247\\303\\243o.txt"]
+
+
+def test_tf_alvo_com_curinga_casa_os_tocados(tmp_path):
+    """AUF-T3: alvo com curinga (`relatorios/*.md`) casa, por `fnmatch`, cada tocado que bate com
+    o padrão — não a regra antiga, que descartava o literal e dava os dois arquivos como fora dos
+    alvos com uma entrada só sob a chave do padrão."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    ref = review_evidence.capturar_ref(repo)
+
+    (repo / "relatorios").mkdir()
+    (repo / "relatorios" / "a.md").write_text("linha-a\n", encoding="utf-8")
+    (repo / "relatorios" / "b.md").write_text("linha-b\n", encoding="utf-8")
+
+    alvos = review_evidence.extrair_arquivos_alvo({"arquivos-alvo": "- `relatorios/*.md`"})
+    assert alvos == ["relatorios/*.md"]
+
+    tocados = review_evidence.coletar_arquivos_tocados(repo, desde=ref)
+    trechos = review_evidence.montar_trechos(repo, alvos, 4000, tocados, desde=ref)
+
+    assert set(trechos.keys()) == {"relatorios/a.md", "relatorios/b.md"}
+    assert review_evidence.confrontar_escopo(tocados, alvos, repo)["fora_dos_alvos"] == []
+
+
+def test_tr_alvo_com_curinga_sem_tocado_diz_que_nada_casa(tmp_path):
+    """Regressão: alvo com curinga sem nenhum tocado que case ganha uma entrada só, com a chave
+    igual ao próprio alvo, sem truncamento e com o texto fixo de aviso."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    ref = review_evidence.capturar_ref(repo)
+
+    trechos = review_evidence.montar_trechos(repo, ["relatorios/*.md"], 4000, [], desde=ref)
+
+    assert trechos == {
+        "relatorios/*.md": {
+            "texto": "(nenhum arquivo tocado casa com o curinga)",
+            "truncado": False,
+        }
+    }
+
+
+def test_tf_alvo_nao_rastreado_sem_antes_sai_marcado_como_novo(tmp_path):
+    """AUF-T3: arquivo não rastreado criado depois do `<ref>` abre com a linha de marca antes do
+    diff (com `desde`, marca de `<ref>`; sem `desde`, marca de `HEAD`)."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    ref = review_evidence.capturar_ref(repo)
+
+    (repo / "novo.md").write_text("linha-1\nlinha-2\n", encoding="utf-8")
+
+    texto_com_desde = review_evidence.montar_trechos(repo, ["novo.md"], 4000, desde=ref)["novo.md"][
+        "texto"
+    ]
+    texto_sem_desde = review_evidence.montar_trechos(repo, ["novo.md"], 4000)["novo.md"]["texto"]
+
+    assert texto_com_desde.startswith(f"(arquivo novo — ausente em `{ref}`)\n")
+    assert texto_sem_desde.startswith("(arquivo novo — ausente em `HEAD`)\n")
+
+
+def test_tr_alvo_rastreado_alterado_nao_leva_a_marca_de_novo(tmp_path):
+    """Regressão: arquivo rastreado alterado depois do `<ref>` continua trazendo a linha `+` de
+    sempre, sem a marca de arquivo novo."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    ref = review_evidence.capturar_ref(repo)
+
+    (repo / "src" / "b.py").write_text("def b():\n    return 2\n", encoding="utf-8")
+
+    texto = review_evidence.montar_trechos(repo, ["src/b.py"], 4000, desde=ref)["src/b.py"]["texto"]
+
+    assert "+    return 2" in texto
+    assert "(arquivo novo" not in texto

```

## Medida do executor
- Arquivo: docs\plans\P-0754-auditoria-final\evidencia\P-0754-AUF-T3-medida.json; mundo: depois; gerado em: 2026-09-28T14:10:22+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_review_evidence.py -q -k "curinga or marcado_como_novo or marca_de_novo"` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
