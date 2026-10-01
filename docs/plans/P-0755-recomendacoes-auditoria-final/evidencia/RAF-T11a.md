# Evidência de revisão — P-0755 RAF-T11a

## Diff (`git diff --stat`)
```
.claude/tools/review_evidence.py                   |  60 ++++++++---
 docs/DIARIO_DE_OBRAS.md                            |   6 +-
 .../estado.tsv                                     |   2 +-
 .../evidencia/P-0755-RAF-T11a-medida.json          |  15 +++
 docs/telemetria.tsv                                |   1 +
 tests/test_review_evidence.py                      | 110 +++++++++++++++++++++
 6 files changed, 176 insertions(+), 18 deletions(-)
```

## Arquivos tocados
- `.claude/tools/review_evidence.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T11a-medida.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `37f8cdb4acff7dcb71c1dbde5ed7320bea085af9`
- Arquivos-alvo declarados: `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`
- Arquivos tocados: `.claude/tools/review_evidence.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T11a-medida.json`, `docs/telemetria.tsv`, `tests/test_review_evidence.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T11a-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index a3a89c6..171b488 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -918,25 +918,57 @@ def _eh_alvo_de_teste(alvo: str) -> bool:
     return caminho.startswith("tests/") and nome.startswith("test_") and nome.endswith(".py")
 
 
+def _linhas_removidas_do_diff(texto: str) -> list[str]:
+    """RAF-T11a (`DRF-53`; `AE-149`): as linhas de `texto` que começam por `-` e vêm depois da
+    primeira linha que começa por `@@` (o cabeçalho `--- a/...`/`+++ b/...` fica antes do `@@` e
+    sai; a linha removida cujo conteúdo começa por `--` fica). Texto sem linha `@@` dá lista
+    vazia."""
+    linhas = texto.splitlines()
+    inicio = next((i for i, linha in enumerate(linhas) if linha.startswith("@@")), None)
+    if inicio is None:
+        return []
+    return [linha for linha in linhas[inicio + 1 :] if linha.startswith("-")]
+
+
 def linhas_removidas_de_teste(
-    root: Path, arquivos_alvo: list[str], desde: str | None = None
+    root: Path,
+    arquivos_alvo: list[str],
+    desde: str | None = None,
+    tocados: list[str] | None = None,
 ) -> dict[str, list[str]]:
-    """RAF-T11 (`DRF-33`; `F-17`, `F-18`; `R-12` do `P-0754`, `AE-97`/`AE-98`): para cada alvo,
-    na ordem, que não é curinga e é de arquivo de teste, a chave é o alvo como veio e o valor são
-    as linhas do diff que começam por `-` e não por `---`, na ordem — fato mecânico, sem julgar
+    """RAF-T11a (`DRF-53`; `AE-149` da `RAF-T11`; `DRF-33`; `F-17`; `R-12`): para cada alvo, na
+    ordem, os caminhos que ele cobre, pela mesma expansão de `montar_trechos`: alvo curinga
+    (`_eh_alvo_curinga`) cobre os `tocados` que casam por `_casa_curinga`; alvo diretório
+    (`tocados` não vazio e `_eh_alvo_diretorio`) cobre os `tocados` sob o prefixo `<alvo>/`; outro
+    alvo cobre a si mesmo, como veio. Cada caminho coberto que é de teste (`_eh_alvo_de_teste`) e
+    cuja forma normalizada (`_normalizar_separador`) ainda não tem chave ganha a chave do caminho
+    como veio e o valor `_linhas_removidas_do_diff` do diff do caminho — fato mecânico, sem julgar
     se a remoção é legítima (isso é do revisor, `RAF-T12`)."""
     removidas: dict[str, list[str]] = {}
+    vistos: set[str] = set()
     for alvo in arquivos_alvo:
         if _eh_alvo_curinga(alvo):
-            continue
-        if not _eh_alvo_de_teste(alvo):
-            continue
-        texto = _diff_para_arquivo(root, alvo, desde)
-        removidas[alvo] = [
-            linha
-            for linha in texto.splitlines()
-            if linha.startswith("-") and not linha.startswith("---")
-        ]
+            alvo_norm = _normalizar_separador(alvo)
+            cobertos = [
+                arquivo
+                for arquivo in (tocados or [])
+                if _casa_curinga(_normalizar_separador(arquivo), alvo_norm)
+            ]
+        elif tocados and _eh_alvo_diretorio(root, alvo):
+            prefixo = _normalizar_separador(alvo).rstrip("/") + "/"
+            cobertos = [
+                arquivo for arquivo in tocados if _normalizar_separador(arquivo).startswith(prefixo)
+            ]
+        else:
+            cobertos = [alvo]
+        for caminho in cobertos:
+            if not _eh_alvo_de_teste(caminho):
+                continue
+            chave_norm = _normalizar_separador(caminho)
+            if chave_norm in vistos:
+                continue
+            vistos.add(chave_norm)
+            removidas[caminho] = _linhas_removidas_do_diff(_diff_para_arquivo(root, caminho, desde))
     return removidas
 
 
@@ -1137,7 +1169,7 @@ def montar_documento(
         teto_guarda_chars=teto_guarda_chars,
         desde=desde,
         linhas_medida=secao_medida_do_executor(caminho_medida),
-        removidas_teste=linhas_removidas_de_teste(root, arquivos_alvo, desde),
+        removidas_teste=linhas_removidas_de_teste(root, arquivos_alvo, desde, tocados),
    
```
[truncado em 4000 caracteres]

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index 493fb19..fc48831 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -2104,3 +2104,113 @@ def test_tr_removidas_de_teste_sem_alvo_de_teste(tmp_path):
     )
 
     assert "- nenhum arquivo de teste entre os alvos" in documento
+
+
+# --- RAF-T11a (DRF-53; AE-149 da RAF-T11): a seção cobre o teste sob curinga ou diretório e a
+# linha removida que começa por dois hífens --------------------------------------------------
+
+
+def _secao_removidas(documento: str) -> str:
+    secao = documento.split("## Linhas removidas dos testes", 1)[1]
+    return secao.split("## Medida do executor", 1)[0]
+
+
+def test_tf_removidas_de_teste_curinga_cobre_teste_tocado(tmp_path):
+    """RAF-T11a (`DRF-53`; `AE-149`): alvo curinga (`tests/test_*.py`) cobre o arquivo de teste
+    tocado que casa por `_casa_curinga` — hoje o curinga é pulado e a seção diz que nenhum arquivo
+    de teste está entre os alvos, apagando a remoção."""
+    review_evidence = _load_review_evidence()
+    repo = _repo_com_teste_versionado(tmp_path)
+    ref = review_evidence.capturar_ref(repo)
+
+    (repo / "tests" / "test_a.py").write_text(
+        "def test_a():\n    assert 1 == 1\n", encoding="utf-8"
+    )
+
+    plano = tmp_path / "plano.md"
+    _escrever_plano(plano, "edita `tests/test_*.py`.")
+
+    documento = review_evidence.montar_documento(
+        plano, "T1", repo, desde=ref, comandos_guardas=_BATERIA_FAKE_VERDE
+    )
+
+    secao = _secao_removidas(documento)
+    assert "### `tests/test_a.py` — 1 linha(s) removida(s)" in secao
+    assert "-    assert 2 == 2" in secao
+    assert "- nenhum arquivo de teste entre os alvos" not in secao
+
+
+def test_tf_removidas_de_teste_diretorio_cobre_teste_tocado(tmp_path):
+    """RAF-T11a (`DRF-53`; `AE-149`): alvo diretório (`tests/`) cobre o arquivo de teste tocado
+    sob o prefixo — hoje o diretório não é arquivo de teste e é pulado."""
+    review_evidence = _load_review_evidence()
+    repo = _repo_com_teste_versionado(tmp_path)
+    ref = review_evidence.capturar_ref(repo)
+
+    (repo / "tests" / "test_a.py").write_text(
+        "def test_a():\n    assert 1 == 1\n", encoding="utf-8"
+    )
+
+    plano = tmp_path / "plano.md"
+    _escrever_plano(plano, "edita `tests/`.")
+
+    documento = review_evidence.montar_documento(
+        plano, "T1", repo, desde=ref, comandos_guardas=_BATERIA_FAKE_VERDE
+    )
+
+    secao = _secao_removidas(documento)
+    assert "### `tests/test_a.py` — 1 linha(s) removida(s)" in secao
+    assert "-    assert 2 == 2" in secao
+    assert "- nenhum arquivo de teste entre os alvos" not in secao
+
+
+def test_tf_removidas_de_teste_linha_que_comeca_por_dois_hifens(tmp_path):
+    """RAF-T11a (`DRF-53`; `AE-149`): linha removida cujo conteúdo começa por `--` não pode sumir
+    atrás do filtro de cabeçalho `---` — hoje o filtro de `---` a apaga junto com o cabeçalho e a
+    seção diz 'nenhuma linha removida'."""
+    review_evidence = _load_review_evidence()
+    repo = _repo_com_teste_versionado(tmp_path)
+    with (repo / "tests" / "test_a.py").open("a", encoding="utf-8") as arquivo:
+        arquivo.write("--sep--\n")
+    _run_git(["add", "-A"], repo)
+    _run_git(["commit", "-m", "acrescenta linha de dois hifens"], repo)
+    ref = review_evidence.capturar_ref(repo)
+
+    conteudo = (repo / "tests" / "test_a.py").read_text(encoding="utf-8")
+    (repo / "tests" / "test_a.py").write_text(
+        conteudo.replace("--sep--\n", ""), encoding="utf-8"
+    )
+
+    plano = tmp_path / "plano.md"
+    _escrever_plano(plano, "edita `tests/test_a.py`.")
+
+    documento = review_evidence.montar_documento(
+        plano, "T1", repo, desde=ref, comandos_guardas=_BATERIA_FAKE_VERDE
+    )
+
+    secao = _secao_removidas(documento)
+    assert "### `tests/test_a.py` — 1 linha(s) removida(s)" in secao
+    assert "---sep--" in secao
+
+
+def test_tr_removidas_de_teste_a
```
[truncado em 4000 caracteres]

## Linhas removidas dos testes
### `tests/test_review_evidence.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T11a-medida.json; mundo: depois; gerado em: 2026-09-29T09:12:39+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_review_evidence.py -q -k "removidas_de_teste and (curinga or hifens or diretorio)"` | 0 | true |

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
