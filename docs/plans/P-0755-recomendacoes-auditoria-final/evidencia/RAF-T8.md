# Evidência de revisão — P-0755 RAF-T8

## Diff (`git diff --stat`)
```
.claude/tools/review_evidence.py                   | 16 +++--
 docs/DIARIO_DE_OBRAS.md                            |  4 +-
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T8-medida.json            | 22 +++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_review_evidence.py                      | 75 +++++++++++++++++++++-
 6 files changed, 111 insertions(+), 9 deletions(-)
```

## Arquivos tocados
- `.claude/tools/review_evidence.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T8-medida.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `3038b5060d1ad7736554652a0c5ecced1d57a1a2`
- Arquivos-alvo declarados: `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`
- Arquivos tocados: `.claude/tools/review_evidence.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T8-medida.json`, `docs/telemetria.tsv`, `tests/test_review_evidence.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T8-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index 91d109a..c0ceb1f 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -644,8 +644,9 @@ def _diff_para_arquivo(root: Path, caminho_rel: str, desde: str | None = None) -
             # AUF-T1: não rastreado ausente de `<ref>` — criado depois do recorte do despacho —
             # chega como diff unificado contra o vazio, no molde do bloco do TK-93a acima.
             texto_atual = _texto_do_disco(root, caminho_rel)
+            marca = f"(arquivo novo — ausente em `{desde}`)\n"
             if texto_atual is None:
-                return "(arquivo binário ou não-UTF-8 — trecho omitido)"
+                return marca + "(arquivo binário ou não-UTF-8 — trecho omitido)"
             diff_linhas = difflib.unified_diff(
                 [],
                 texto_atual.splitlines(),
@@ -653,7 +654,6 @@ def _diff_para_arquivo(root: Path, caminho_rel: str, desde: str | None = None) -
                 tofile=caminho_rel,
                 lineterm="",
             )
-            marca = f"(arquivo novo — ausente em `{desde}`)\n"
             return marca + "\n".join(diff_linhas) + "\n"
         texto = _git(["diff", desde, "--", caminho_rel], root)
         if texto.strip():
@@ -668,6 +668,8 @@ def _diff_para_arquivo(root: Path, caminho_rel: str, desde: str | None = None) -
         try:
             conteudo = caminho_abs.read_text(encoding="utf-8")
         except UnicodeDecodeError:
+            if _eh_nao_rastreado(root, caminho_rel):
+                return "(arquivo novo — ausente em `HEAD`)\n(arquivo binário ou não-UTF-8 — trecho omitido)"
             return "(arquivo binário ou não-UTF-8 — trecho omitido)"
         if _eh_nao_rastreado(root, caminho_rel):
             return "(arquivo novo — ausente em `HEAD`)\n" + conteudo
@@ -879,14 +881,20 @@ def _renderizar(
     linhas.append("## Arquivos tocados")
     if arquivos_tocados:
         estados = estado_git or {}
+        registro = set(escopo.get("registro_orquestracao", []))
         alheio = (
             set(escopo.get("fora_dos_alvos", []))
             | set(escopo.get("de_outra_tarefa", {}).keys())
-            | set(escopo.get("registro_orquestracao", []))
+            | registro
             | set(escopo.get("ato_do_dono", []))
         )
         for caminho in arquivos_tocados:
-            atribuicao = "alheio" if caminho in alheio else "da entrega"
+            if caminho in registro:
+                atribuicao = "registro da orquestração"
+            elif caminho in alheio:
+                atribuicao = "alheio"
+            else:
+                atribuicao = "da entrega"
             codigo = estados.get(caminho)
             estado_txt = f"`{codigo}`" if codigo is not None else "(sem entrada em `git status`)"
             linhas.append(f"- `{caminho}` — atribuição: {atribuicao}; estado git: {estado_txt}")

```

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index c56fc81..49bc925 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -833,7 +833,7 @@ def test_tr_atribuicao_de_arquivos_tocados_cobre_os_quatro_baldes_alheios_de_con
     `registro_orquestracao`, `ato_do_dono`) — não só `fora_dos_alvos`. Prova que a seção lê o
     dicionário que `confrontar_escopo` já calcula em vez de reimplementar uma segunda checagem de
     cobertura (`DM-19`): um arquivo do balde `registro_orquestracao`, que nunca aparece em
-    `fora_dos_alvos`, ainda assim sai marcado `alheio`."""
+    `fora_dos_alvos`, sai marcado com o nome do balde, `registro da orquestração` (`R-14`, RAF-T8)."""
     review_evidence = _load_review_evidence()
     repo = tmp_path / "repo"
     _init_repo_com_baseline(repo)
@@ -848,7 +848,7 @@ def test_tr_atribuicao_de_arquivos_tocados_cobre_os_quatro_baldes_alheios_de_con
         plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
     )
 
-    assert "- `docs/telemetria.tsv` — atribuição: alheio; estado git: `??`" in documento
+    assert "- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: `??`" in documento
 
 
 def test_tf_atribuir_classifica_nos_cinco_baldes(tmp_path, capsys):
@@ -1802,3 +1802,74 @@ def test_tr_quebra_out_com_medida_ao_lado_usa_a_do_lado(tmp_path, capsys):
     conteudo = destino_out.read_text(encoding="utf-8")
     assert '| 1 | `python -c "print(\'a\')"` | 3 | true |' in conteudo
     assert '| 1 | `python -c "print(\'a\')"` | 7 | true |' not in conteudo
+
+
+# --- RAF-T8 (R-14, AE-135 do P-0755): a marca de arquivo novo abre também o retorno binário, e o
+# registro da orquestração leva o mesmo nome na lista e no resumo
+
+
+def test_tf_marca_e_rotulo_binario_novo_abre_com_a_marca(tmp_path):
+    """TF do RAF-T8 (R-14): `img.bin` não rastreado, criado depois do `<ref>` — a marca `(arquivo
+    novo — ausente em ...)` que hoje só abre o diff de texto passa a abrir também o retorno do
+    arquivo que não se lê como texto, seguida de `(arquivo binário ou não-UTF-8 — trecho
+    omitido)` (hoje os dois retornos são só a linha do binário, sem marca)."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+
+    ref = review_evidence.capturar_ref(repo)
+
+    (repo / "img.bin").write_bytes(bytes([0xFF, 0xFE, 0x00, 0x81]))
+
+    assert review_evidence._diff_para_arquivo(repo, "img.bin", desde=ref) == (
+        f"(arquivo novo — ausente em `{ref}`)\n"
+        "(arquivo binário ou não-UTF-8 — trecho omitido)"
+    )
+    assert review_evidence._diff_para_arquivo(repo, "img.bin") == (
+        "(arquivo novo — ausente em `HEAD`)\n"
+        "(arquivo binário ou não-UTF-8 — trecho omitido)"
+    )
+
+
+def test_tr_marca_e_rotulo_binario_rastreado_alterado_sem_marca(tmp_path):
+    """Regressão do RAF-T8: `img.bin` rastreado (existe no `<ref>`) e alterado depois dele — o
+    retorno com `desde=ref` não ganha a marca de arquivo novo; ela é exclusiva do não rastreado."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    (repo / "img.bin").write_bytes(bytes([0xFF, 0xFE, 0x00, 0x81]))
+    _run_git(["add", "-A"], repo)
+    _run_git(["commit", "-m", "img.bin"], repo)
+
+    ref = review_evidence.capturar_ref(repo)
+
+    (repo / "img.bin").write_bytes(bytes([0xFF, 0xFE, 0x00, 0x82]))
+
+    assert "(arquivo novo" not in review_evidence._diff_para_arquivo(repo, "img.bin", desde=ref)
+
+
+def test_tf_marca_e_rotulo_registro_da_orquestracao_na_lista(tmp_path):
+    """TF do RAF-T8 (R-14, `F-17`): `docs/DIARIO_DE_OBRAS.md` (balde `registro_orquestracao`) e
+    `docs/nota.txt` (balde `fora_dos_alvos`) não rastreados, fora dos `Arquivos-alvo` — a seção
+    `## Arquivos tocados` passa a nomear o balde do primeiro em vez do genérico `alheio` que hoje
+    os dois recebem, igualando o rótulo ao da seção `## Esco
```
[truncado em 4000 caracteres]

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T8-medida.json; mundo: depois; gerado em: 2026-09-29T07:24:16+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_review_evidence.py -q -k marca_e_rotulo_binario` | 0 | true |
| 2 | `python -m pytest tests/test_review_evidence.py -q -k marca_e_rotulo_registro` | 0 | true |

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
