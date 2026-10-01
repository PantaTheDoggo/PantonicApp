# Evidência de revisão — P-0755 RAF-T10a

## Diff (`git diff --stat`)
```
.claude/tools/review_evidence.py                   | 59 +++++++++++-------
 docs/DIARIO_DE_OBRAS.md                            |  6 +-
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T10a-medida.json          | 22 +++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_review_evidence.py                      | 69 ++++++++++++++++++++++
 6 files changed, 133 insertions(+), 26 deletions(-)
```

## Arquivos tocados
- `.claude/tools/review_evidence.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T10a-medida.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `c427f90188f12e3ae3180a47f8b5ff7a0cde57e9`
- Arquivos-alvo declarados: `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`
- Arquivos tocados: `.claude/tools/review_evidence.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T10a-medida.json`, `docs/telemetria.tsv`, `tests/test_review_evidence.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T10a-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index 1ad4cab..5a50558 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -121,7 +121,7 @@ def _load_rdo(root: Path):
     return modulo
 
 
-_CAMINHO_RE = re.compile(r"^[A-Za-z0-9_.*][A-Za-z0-9_./\\*-]*$")
+_CAMINHO_RE = re.compile(r"^[A-Za-z0-9_.*À-ÖØ-öø-ÿ][A-Za-z0-9_./\\*À-ÖØ-öø-ÿ-]*$")
 _EXTENSAO_RE = re.compile(r"\.[A-Za-z0-9]+$")
 
 
@@ -179,7 +179,7 @@ def _forcar_utf8(stream) -> None:
 def _git(args: list[str], root: Path, env: dict[str, str] | None = None) -> str:
     try:
         resultado = subprocess.run(
-            ["git", *args],
+            ["git", "-c", "core.quotepath=false", *args],
             cwd=str(root),
             capture_output=True,
             text=True,
@@ -294,6 +294,31 @@ def _entradas_status(root: Path) -> list[tuple[str, str]]:
     return entradas
 
 
+def _entradas_diff(root: Path, ref: str) -> list[tuple[str, str]]:
+    """`git diff <ref> --name-status -z` (RAF-T10a, `DRF-52`): com `-z`, cada campo (separado por
+    NUL) chega cru, sem aspas nem escape octal, qualquer que seja o `core.quotepath` da máquina.
+    Devolve, na ordem do `git`, `(letra, caminho)` de cada arquivo; quando a letra começa por `R`
+    ou `C`, vêm dois caminhos (origem e destino) e o caminho da entrada é o segundo (o novo) — a
+    origem não vira entrada."""
+    saida = _git(["diff", ref, "--name-status", "-z"], root)
+    campos = saida.split("\0")
+    entradas: list[tuple[str, str]] = []
+    i = 0
+    while i < len(campos):
+        letra = campos[i]
+        if not letra:
+            i += 1
+            continue
+        if letra[0] in ("R", "C"):
+            caminho = campos[i + 2]
+            i += 3
+        else:
+            caminho = campos[i + 1]
+            i += 2
+        entradas.append((letra, caminho))
+    return entradas
+
+
 def _existe_no_ref(root: Path, ref: str, caminho: str) -> bool:
     """`git cat-file -e <ref>:<caminho>` — existe como blob na árvore do commit `<ref>`."""
     return (
@@ -361,16 +386,15 @@ def coletar_arquivos_tocados(root: Path, desde: str | None = None) -> list[str]:
     arquivo dentro dele.
 
     Com `desde=<ref>` (AUT-T5b): recorta o conjunto de rastreados para só os alterados **desde**
-    `<ref>` (`git diff <ref> --name-only`), em vez da árvore de trabalho inteira — necessário
+    `<ref>` (`_entradas_diff`), em vez da árvore de trabalho inteira — necessário
     quando outras tarefas têm mudanças soltas, não commitadas, no mesmo repositório. Untracked
     presente na árvore de `<ref>` (`TK-93a`: `<ref>` de `--capturar-ref` grava não rastreados
     também) é julgado por conteúdo (`_nao_rastreado_mudou_desde_ref`), não por data — ele não
-    aparece em `git diff <ref> --name-only` (que o dá como apagado, já que está fora do índice
+    aparece como tocado de `_entradas_diff` (que o dá como apagado, já que está fora do índice
     atual). Untracked ausente de `<ref>` (ex.: `<ref>` de `git stash create`, que não grava
     não rastreados) segue pelo recorte por data: a entrada `??` cujo arquivo tem `st_mtime` menor
     que a data de commit de `<ref>` (`%ct`) fica de fora; a de data igual ou maior entra, e também
-    a que não existe no disco como veio do `git status` (nome entre aspas com escape octal, por
-    exemplo)."""
+    a que não existe no disco como veio do `git status`."""
     entradas = _entradas_status(root)
     tocados: dict[str, None] = {}
     if desde is None:
@@ -392,39 +416,30 @@ def coletar_arquivos_tocados(root: Path, desde: str | None = None) -> list[str]:
         if arquivo.exists() and arquivo.stat().st_mtime < corte:
             continue
         tocados.setdefault(caminho, None)
-    saida_diff = _git(["diff", desde, "--name-only"], root)
-    for linha in saida_diff.splitlines():
-        linha = linha.strip()
+    for _letra, caminho in _entradas_diff(root, desde):
         # não rastreado presente e
```
[truncado em 4000 caracteres]

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index 7cbc6ad..e0b0c2e 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -1955,3 +1955,72 @@ def test_tr_acento_z_renomeado_usa_o_caminho_novo(tmp_path):
     assert "src/b.py" not in estados
 
     assert review_evidence.coletar_arquivos_tocados(repo) == ["src/c.py"]
+
+
+def test_tf_acento_diff_commitado_chega_com_um_nome_so(tmp_path):
+    """RAF-T10a (`DRF-52`; `AE-142`-`AE-145` da `RAF-T10`): com `core.quotepath` ligado, o arquivo
+    acentuado já rastreado e alterado **depois** do `ref` (só `git diff` o vê, árvore de trabalho
+    limpa) chega com um nome só nos tocados, no estado, no resumo e no cabeçalho do trecho — hoje
+    (`git diff <ref> --name-only`/`--name-status` sem `-z`, `--stat` e diff unificado sem
+    `-c core.quotepath=false`) ele chega em escape octal."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    _run_git(["config", "core.quotepath", "true"], repo)
+
+    (repo / "ação.md").write_text("linha-1\n", encoding="utf-8")
+    _run_git(["add", "-A"], repo)
+    _run_git(["commit", "-m", "adiciona ação.md"], repo)
+
+    ref = review_evidence.capturar_ref(repo)
+
+    (repo / "ação.md").write_text("linha-1\nlinha-2\n", encoding="utf-8")
+    _run_git(["add", "-A"], repo)
+    _run_git(["commit", "-m", "altera ação.md"], repo)
+
+    tocados = review_evidence.coletar_arquivos_tocados(repo, desde=ref)
+    assert tocados == ["ação.md"]
+
+    assert review_evidence.coletar_estado_git(repo, desde=ref) == {
+        "ação.md": f"M (commitado desde {ref})"
+    }
+
+    trecho = review_evidence.montar_trechos(repo, ["ação.md"], 4000, tocados, desde=ref)["ação.md"][
+        "texto"
+    ]
+    resumo = review_evidence.coletar_diff_stat(repo, desde=ref)
+
+    assert "+linha-2" in trecho
+    assert r"\303" not in trecho
+    assert r"\303" not in resumo
+    assert "ação.md" in resumo
+
+
+def test_tf_acento_alvo_acentuado_e_caminho(tmp_path):
+    """RAF-T10a (`DRF-52`; `AE-144` da `RAF-T10`): `_CAMINHO_RE` aceita letra acentuada —
+    `docs/ação.md` declarado em `Arquivos-alvo` vira alvo reconhecido, não literal descartado
+    (hoje `_CAMINHO_RE` é ASCII-only e o descarta)."""
+    review_evidence = _load_review_evidence()
+    campos = {"arquivos-alvo": "- `docs/ação.md`"}
+
+    assert review_evidence.extrair_arquivos_alvo(campos) == ["docs/ação.md"]
+    assert review_evidence.extrair_literais_nao_caminho(campos) == []
+
+
+def test_tr_acento_diff_renomeado_commitado_usa_o_caminho_novo(tmp_path):
+    """Regressão: renomeação commitada depois do `ref` usa o caminho novo como chave em
+    `coletar_estado_git` e em `coletar_arquivos_tocados` — a origem, consumida como o segundo
+    campo da letra `R`/`C` por `_entradas_diff`, nunca vira entrada própria (a regra concorrente
+    que tratasse a origem como entrada daria `src/b.py` também)."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    ref = review_evidence.capturar_ref(repo)
+
+    _run_git(["mv", "src/b.py", "src/c.py"], repo)
+    _run_git(["commit", "-m", "renomeia src/b.py"], repo)
+
+    assert review_evidence.coletar_estado_git(repo, desde=ref) == {
+        "src/c.py": f"R100 (commitado desde {ref})"
+    }
+    assert review_evidence.coletar_arquivos_tocados(repo, desde=ref) == ["src/c.py"]

```

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T10a-medida.json; mundo: depois; gerado em: 2026-09-29T08:42:25+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_review_evidence.py -q -k "acento_diff or acento_alvo"` | 0 | true |
| 2 | `python -c "import pathlib,sys; t=pathlib.Path('.claude/tools/review_evidence.py').read_text(encoding='utf-8'); q=chr(96); p=chr(34); a=t.count(p+'--name-only'+p); b=t.count('escape octal, por')+t.count('o último campo da linha'); c=t.count(p+'--name-status'+p+', '+p+'-z'+p); d=t.count('-z --untracked-files=all'+q+' por caminho'); e=t.count(p+'-c'+p+', '+p+'core.quotepath=false'+p); print('diff=%d-%d-%d-%d-%d'%(a,b,c,d,e)); sys.exit(0 if (a,b,c,d,e)==(0,0,1,1,1) else 1)"` | 0 | true |

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
