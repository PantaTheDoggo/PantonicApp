# Evidência de revisão — P-0755 RAF-T10

## Diff (`git diff --stat`)
```
.claude/tools/review_evidence.py                   | 51 ++++++++++++++--------
 docs/DIARIO_DE_OBRAS.md                            |  4 +-
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T10-medida.json           | 15 +++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_review_evidence.py                      | 48 +++++++++++++++++---
 6 files changed, 93 insertions(+), 28 deletions(-)
```

## Arquivos tocados
- `.claude/tools/review_evidence.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T10-medida.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `8f1a6b8ceafd9ad6da2bb3765188643d28abc8c6`
- Arquivos-alvo declarados: `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`
- Arquivos tocados: `.claude/tools/review_evidence.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T10-medida.json`, `docs/telemetria.tsv`, `tests/test_review_evidence.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T10-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index 4517a57..1ad4cab 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -269,11 +269,29 @@ def coletar_diff_stat(root: Path, desde: str | None = None) -> str:
     return _git(["diff", "--stat", desde, arvore, "--", *tocados], root).strip()
 
 
-def _extrair_caminho_status(linha: str) -> str:
-    caminho = linha[3:]
-    if " -> " in caminho:
-        caminho = caminho.split(" -> ", 1)[1]
-    return caminho.strip().strip('"')
+def _entradas_status(root: Path) -> list[tuple[str, str]]:
+    """`git status --porcelain=v1 -z --untracked-files=all` (RAF-T10, `DRF-32`, `R-31`): com `-z`,
+    cada campo (separado por NUL) chega cru, sem aspas nem escape octal, qualquer que seja o
+    `core.quotepath` da máquina. Devolve, na ordem do `git`, `(código XY, caminho)` de cada campo
+    com 4 caracteres ou mais (`campo[:2]`, `campo[3:]`); quando o código contém `R` ou `C`, o
+    campo seguinte (o caminho de origem da renomeação/cópia) se consome sem virar entrada."""
+    saida = _git(["status", "--porcelain=v1", "-z", "--untracked-files=all"], root)
+    campos = saida.split("\0")
+    entradas: list[tuple[str, str]] = []
+    i = 0
+    while i < len(campos):
+        campo = campos[i]
+        if len(campo) < 4:
+            i += 1
+            continue
+        codigo = campo[:2]
+        caminho = campo[3:]
+        entradas.append((codigo, caminho))
+        if "R" in codigo or "C" in codigo:
+            i += 2
+        else:
+            i += 1
+    return entradas
 
 
 def _existe_no_ref(root: Path, ref: str, caminho: str) -> bool:
@@ -353,21 +371,18 @@ def coletar_arquivos_tocados(root: Path, desde: str | None = None) -> list[str]:
     que a data de commit de `<ref>` (`%ct`) fica de fora; a de data igual ou maior entra, e também
     a que não existe no disco como veio do `git status` (nome entre aspas com escape octal, por
     exemplo)."""
-    saida_status = _git(["status", "--porcelain=v1", "--untracked-files=all"], root)
+    entradas = _entradas_status(root)
     tocados: dict[str, None] = {}
     if desde is None:
-        for linha in saida_status.splitlines():
-            if not linha:
-                continue
-            tocados.setdefault(_extrair_caminho_status(linha), None)
+        for _codigo, caminho in entradas:
+            tocados.setdefault(caminho, None)
         return sorted(tocados.keys())
 
     corte = int(_git(["show", "-s", "--format=%ct", desde], root).strip())
     nao_rastreados: set[str] = set()
-    for linha in saida_status.splitlines():
-        if not linha.startswith("??"):
+    for codigo, caminho in entradas:
+        if codigo != "??":
             continue
-        caminho = _extrair_caminho_status(linha)
         nao_rastreados.add(caminho)
         if _existe_no_ref(root, desde, caminho):
             if _nao_rastreado_mudou_desde_ref(root, desde, caminho):
@@ -389,7 +404,7 @@ def coletar_arquivos_tocados(root: Path, desde: str | None = None) -> list[str]:
 
 def coletar_estado_git(root: Path, desde: str | None = None) -> dict[str, str]:
     """Código `XY` de `git status --porcelain=v1 --untracked-files=all` por caminho (mesma chave
-    que `coletar_arquivos_tocados` já extrai via `_extrair_caminho_status`) — a evidência `git`
+    que `coletar_arquivos_tocados` já extrai via `_entradas_status`) — a evidência `git`
     que comprova a atribuição de cada arquivo na seção `## Arquivos tocados` (`LM-T3`, `AE-13`).
     Não classifica nada: só devolve o estado bruto que o `git` já relata.
 
@@ -398,12 +413,10 @@ def coletar_estado_git(root: Path, desde: str | None = None) -> dict[str, str]:
     desde <ref>)`) via `setdefault` — é o `setdefault`, e não uma atribuição, que materializa essa
     precedência. Para renomeação (`R100\t<velho>\t<novo>`), a chave é o último campo da linha e a
     letra é o primeiro campo inteiro (`R100`)."""
-    saida_status = _git([
```
[truncado em 4000 caracteres]

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index 65722f8..7cbc6ad 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -1436,11 +1436,9 @@ def test_tr_arquivo_novo_sem_desde_segue_com_conteudo_integral(tmp_path):
 
 
 def test_tf_caminho_acentuado_do_status_entra_nos_tocados_pelo_ramo_de_caminho_ausente(tmp_path):
-    """AUF-T2: com `core.quotepath` ligado, o `git status` devolve o caminho acentuado como string
-    entre aspas com escape octal (`"a\\303\\247\\303\\243o.txt"`); `_extrair_caminho_status` só
-    tira as aspas, sem decodificar o escape — o caminho lido não existe no disco (que tem
-    `ação.txt`, não `a\\303\\247\\303\\243o.txt`) e o salto por `st_mtime` não dispara porque
-    `arquivo.exists()` é falso, então o caminho com escape entra nos tocados."""
+    """AUF-T2, reescrito pela RAF-T10 (`R-31`): com `core.quotepath` ligado, o `git status` sem `-z`
+    devolveria o caminho acentuado entre aspas com escape octal; com `-z` (`_entradas_status`) o
+    caminho chega cru, e o não rastreado criado depois do `ref` entra nos tocados como `ação.txt`."""
     review_evidence = _load_review_evidence()
     repo = tmp_path / "repo"
     _init_repo_com_baseline(repo)
@@ -1452,7 +1450,7 @@ def test_tf_caminho_acentuado_do_status_entra_nos_tocados_pelo_ramo_de_caminho_a
 
     tocados = review_evidence.coletar_arquivos_tocados(repo, desde=ref)
 
-    assert tocados == ["a\\303\\247\\303\\243o.txt"]
+    assert tocados == ["ação.txt"]
 
 
 def test_tf_alvo_com_curinga_casa_os_tocados(tmp_path):
@@ -1919,3 +1917,41 @@ def test_tf_glob_estrela_dupla_alcanca_subpastas(tmp_path):
     assert review_evidence.confrontar_escopo(tocados, alvos, repo)["fora_dos_alvos"] == []
     trechos = review_evidence.montar_trechos(repo, alvos, 4000, tocados, desde=ref)
     assert set(trechos.keys()) == {"relatorios/a.md", "relatorios/sub/x.md"}
+
+
+def test_tf_acento_z_nao_rastreado_chega_com_o_diff(tmp_path):
+    """RAF-T10 (`DRF-32`, `R-31`): com `core.quotepath` ligado, `_entradas_status` (via `-z`) lê o
+    caminho acentuado cru — hoje (sem `-z`) o caminho chega em escape octal e o trecho sai
+    `arquivo ausente`."""
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
+    assert tocados == ["ação.txt"]
+
+    trechos = review_evidence.montar_trechos(repo, ["ação.txt"], 4000, tocados, desde=ref)
+    assert "+linha-1" in trechos["ação.txt"]["texto"]
+
+    assert review_evidence.coletar_estado_git(repo)["ação.txt"] == "??"
+
+
+def test_tr_acento_z_renomeado_usa_o_caminho_novo(tmp_path):
+    """Regressão: renomeação (`git mv`) usa o caminho novo como chave — a origem, consumida como
+    o campo seguinte ao código `R` por `_entradas_status`, nunca vira entrada própria."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+
+    _run_git(["mv", "src/b.py", "src/c.py"], repo)
+
+    estados = review_evidence.coletar_estado_git(repo)
+    assert estados["src/c.py"] == "R "
+    assert "src/b.py" not in estados
+
+    assert review_evidence.coletar_arquivos_tocados(repo) == ["src/c.py"]

```

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T10-medida.json; mundo: depois; gerado em: 2026-09-29T08:11:43+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_review_evidence.py -q -k acento_z` | 0 | true |

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
