# Evidência de revisão — P-0754 AUF-T5

## Diff (`git diff --stat`)
```
.claude/tools/review_evidence.py                   | 61 +++++++++++++---------
 docs/DIARIO_DE_OBRAS.md                            |  4 +-
 docs/plans/P-0754-auditoria-final/estado.tsv       |  2 +-
 .../evidencia/P-0754-AUF-T5-medida.json            | 22 ++++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_review_evidence.py                      | 51 ++++++++++++++++++
 6 files changed, 112 insertions(+), 29 deletions(-)
```

## Arquivos tocados
- `.claude/tools/review_evidence.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0754-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T5-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `2ab46ca76ee5271a1f6b0ef9a545123f3e411b68`
- Arquivos-alvo declarados: `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`
- Arquivos tocados: `.claude/tools/review_evidence.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T5-medida.json`, `docs/telemetria.tsv`, `tests/test_review_evidence.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T5-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index a9dc620..56cfb1f 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -205,40 +205,58 @@ def _diff(args_sem_head: list[str], root: Path) -> str:
         return _git(["diff", *args_sem_head], root)
 
 
-def capturar_ref(root: Path) -> str:
-    """`<ref>` do despacho (`TK-93a`, flag `--capturar-ref`): commit cujo pai é `HEAD` (sem pai em
-    repositório sem commit ainda) e cuja árvore é a árvore de trabalho inteira — rastreados e não
-    rastreados não ignorados —, gravado por um índice temporário (`GIT_INDEX_FILE`); a árvore de
-    trabalho, o índice real e a lista de stash saem exatamente como entraram, porque nada aqui
-    escreve nele."""
+def _gravar_arvore_de_trabalho(root: Path) -> str:
+    """Grava a árvore de trabalho inteira — rastreados e não rastreados não ignorados, e também o
+    rastreado que o `.gitignore` cobre (`AUF-T5`, `DAU-18`, `DAU-25`) — num índice temporário
+    (`GIT_INDEX_FILE`) e devolve o hash de `git write-tree`. Chamada por `capturar_ref` e por
+    `coletar_diff_stat`. O índice temporário nasce como o arquivo de `tempfile.mkstemp`, apagado
+    antes do uso e no `finally`; quando `git rev-parse --verify HEAD` sai 0, roda `git read-tree
+    HEAD` nesse índice antes do `git add -A` — sem isso, `git add -A` num índice vazio respeita o
+    `.gitignore` e nunca vê um rastreado ignorado. Sem commit ainda, o índice parte vazio como
+    antes. A árvore de trabalho, o índice real e a lista de stash saem exatamente como entraram,
+    porque nada aqui escreve neles."""
     fd, indice_tmp = tempfile.mkstemp(prefix=".review-evidence-index-", suffix=".tmp")
     os.close(fd)
     Path(indice_tmp).unlink()
     env = dict(os.environ)
     env["GIT_INDEX_FILE"] = indice_tmp
     try:
-        _git(["add", "-A"], root, env=env)
-        arvore = _git(["write-tree"], root, env=env).strip()
         try:
-            pai = _git(["rev-parse", "--verify", "HEAD"], root).strip()
+            _git(["rev-parse", "--verify", "HEAD"], root)
         except ReviewEvidenceValidationError:
-            pai = None
-        args_commit = ["commit-tree", arvore, "-m", "review_evidence: captura de <ref> (TK-93a)"]
-        if pai is not None:
-            args_commit += ["-p", pai]
-        return _git(args_commit, root, env=env).strip()
+            pass
+        else:
+            _git(["read-tree", "HEAD"], root, env=env)
+        _git(["add", "-A"], root, env=env)
+        return _git(["write-tree"], root, env=env).strip()
     finally:
         Path(indice_tmp).unlink(missing_ok=True)
 
 
+def capturar_ref(root: Path) -> str:
+    """`<ref>` do despacho (`TK-93a`, flag `--capturar-ref`): commit cujo pai é `HEAD` (sem pai em
+    repositório sem commit ainda) e cuja árvore é a árvore de trabalho inteira — rastreados e não
+    rastreados não ignorados —, gravada por `_gravar_arvore_de_trabalho`; a árvore de trabalho, o
+    índice real e a lista de stash saem exatamente como entraram, porque nada aqui escreve nele."""
+    arvore = _gravar_arvore_de_trabalho(root)
+    try:
+        pai = _git(["rev-parse", "--verify", "HEAD"], root).strip()
+    except ReviewEvidenceValidationError:
+        pai = None
+    args_commit = ["commit-tree", arvore, "-m", "review_evidence: captura de <ref> (TK-93a)"]
+    if pai is not None:
+        args_commit += ["-p", pai]
+    return _git(args_commit, root).strip()
+
+
 def coletar_diff_stat(root: Path, desde: str | None = None) -> str:
     """Sem `desde`: `git diff HEAD --stat` (comportamento de sempre). Com `desde=<ref>` (`AF-T1`,
     `TK-94a`): recorta o resumo para o mesmo conjunto que `coletar_arquivos_tocados(root, desde)`
     devolve — rastreados e não rastreados da entrega, nunca o trabalho em andamento de outra
     tarefa na mesma árvore. Sem tocado nenhum, devolve string vazia (o chamador já renderiza
     `(sem diferenças)` para diff vazio); co
```
[truncado em 4000 caracteres]

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index 5bc83ee..2978566 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -1567,3 +1567,54 @@ def test_tr_alvo_de_outra_tarefa_fora_do_registro_segue_atribuido(tmp_path):
 
     assert escopo["de_outra_tarefa"] == {"src/c.py": "TK-1a"}
     assert escopo["registro_orquestracao"] == []
+
+
+def _repo_com_versionado_ignorado(tmp_path: Path) -> Path:
+    """Repositório de `_init_repo_com_baseline` com um arquivo já versionado que o `.gitignore`
+    também cobre (`AUF-T5`): `.gitignore` reescrito com `__pycache__/` e `versionado.log`,
+    `versionado.log` criado com `v1`, adicionado com `git add -f` e commitado junto do
+    `.gitignore`."""
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    (repo / ".gitignore").write_text("__pycache__/\nversionado.log\n", encoding="utf-8")
+    (repo / "versionado.log").write_text("v1", encoding="utf-8")
+    _run_git(["add", "-f", ".gitignore", "versionado.log"], repo)
+    _run_git(["commit", "-m", "versionado ignorado"], repo)
+    return repo
+
+
+def test_tf_capturar_ref_inclui_versionado_que_o_gitignore_cobre(tmp_path):
+    """AUF-T5 (`DAU-18`, `DAU-25`, `H-19` §2.1): arquivo já versionado que o `.gitignore` também
+    cobre entra na árvore de `<ref>` como qualquer outro rastreado — a regra antiga (`git add -A`
+    sozinho, num índice recém-criado vazio) deixava esse arquivo fora da árvore gravada, porque
+    `git add -A` respeita `.gitignore` e não vê um rastreado ignorado sem o índice já o conhecer."""
+    review_evidence = _load_review_evidence()
+    repo = _repo_com_versionado_ignorado(tmp_path)
+
+    (repo / "versionado.log").write_text("v2", encoding="utf-8")
+
+    ref = review_evidence.capturar_ref(repo)
+
+    resultado = subprocess.run(
+        ["git", "show", f"{ref}:versionado.log"], cwd=str(repo), capture_output=True, text=True
+    )
+    assert resultado.returncode == 0
+    assert resultado.stdout == "v2"
+
+
+def test_tf_versionado_ignorado_intocado_fica_fora_dos_tocados_e_alterado_entra(tmp_path):
+    """AUF-T5 (`DAU-18`, `DAU-25`, `F-13`, `F-14`): com `<ref>` gravando o versionado ignorado
+    (teste anterior), o arquivo intocado desde `<ref>` não aparece mais em
+    `coletar_arquivos_tocados` nem em `coletar_diff_stat` — a regra antiga, por não ter o arquivo
+    em `<ref>`, o enxergava sempre como apagado/tocado."""
+    review_evidence = _load_review_evidence()
+    repo = _repo_com_versionado_ignorado(tmp_path)
+
+    ref = review_evidence.capturar_ref(repo)
+
+    assert review_evidence.coletar_arquivos_tocados(repo, desde=ref) == []
+
+    (repo / "versionado.log").write_text("v3", encoding="utf-8")
+
+    assert review_evidence.coletar_arquivos_tocados(repo, desde=ref) == ["versionado.log"]
+    assert "versionado.log" in review_evidence.coletar_diff_stat(repo, desde=ref)

```

## Medida do executor
- Arquivo: docs\plans\P-0754-auditoria-final\evidencia\P-0754-AUF-T5-medida.json; mundo: depois; gerado em: 2026-09-28T14:25:25+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_review_evidence.py -q -k "versionado"` | 0 | true |
| 2 | `python -c "from pathlib import Path;t=Path('.claude/tools/review_evidence.py').read_text(encoding='utf-8');print('[%d-%d-%d]'%(t.count('def _gravar_arvore_de_trabalho'),t.count('_gravar_arvore_de_trabalho(root)'),t.count(chr(34)+'read-tree'+chr(34))))"` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
