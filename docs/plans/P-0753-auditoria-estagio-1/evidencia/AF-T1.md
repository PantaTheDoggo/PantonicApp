# Evidência de revisão — P-0753 AF-T1

## Diff (`git diff --stat`)
```
.claude/tools/review_evidence.py                   | 32 +++++++++++--
 docs/DIARIO_DE_OBRAS.md                            |  2 +-
 docs/plans/P-0753-auditoria-estagio-1/estado.tsv   |  2 +-
 .../evidencia/P-0753-AF-T1-medida.json             | 29 ++++++++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_review_evidence.py                      | 54 ++++++++++++++++++++++
 6 files changed, 115 insertions(+), 5 deletions(-)
```

## Arquivos tocados
- `.claude/tools/review_evidence.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T1-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `47c30db1202798dcec255849e7a312d2162b3c44`
- Arquivos-alvo declarados: `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`
- Arquivos tocados: `.claude/tools/review_evidence.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T1-medida.json`, `docs/telemetria.tsv`, `tests/test_review_evidence.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T1-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index 012487a..86cecb8 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -229,8 +229,34 @@ def capturar_ref(root: Path) -> str:
         Path(indice_tmp).unlink(missing_ok=True)
 
 
-def coletar_diff_stat(root: Path) -> str:
-    return _diff(["--stat"], root).strip()
+def coletar_diff_stat(root: Path, desde: str | None = None) -> str:
+    """Sem `desde`: `git diff HEAD --stat` (comportamento de sempre). Com `desde=<ref>` (`AF-T1`,
+    `TK-94a`): recorta o resumo para o mesmo conjunto que `coletar_arquivos_tocados(root, desde)`
+    devolve — rastreados e não rastreados da entrega, nunca o trabalho em andamento de outra
+    tarefa na mesma árvore. Sem tocado nenhum, devolve string vazia (o chamador já renderiza
+    `(sem diferenças)` para diff vazio); com tocado, grava a árvore de trabalho num índice
+    temporário (`GIT_INDEX_FILE`, mesmo molde de `capturar_ref`) para obter o hash da árvore
+    inteira — rastreados e não rastreados —, e roda `git diff --stat <desde> <árvore> --
+    <tocados>` fora do índice temporário (comparação de dois tree-ish, não precisa mais dele).
+    Árvore de trabalho, índice real e lista de stash saem como entraram: nada aqui escreve
+    neles. Nunca roda `git diff --stat` sem caminho quando `tocados` é vazio — sem `--`, ele
+    devolveria a árvore inteira."""
+    if desde is None:
+        return _diff(["--stat"], root).strip()
+    tocados = coletar_arquivos_tocados(root, desde)
+    if not tocados:
+        return ""
+    fd, indice_tmp = tempfile.mkstemp(prefix=".review-evidence-index-", suffix=".tmp")
+    os.close(fd)
+    Path(indice_tmp).unlink()
+    env = dict(os.environ)
+    env["GIT_INDEX_FILE"] = indice_tmp
+    try:
+        _git(["add", "-A"], root, env=env)
+        arvore = _git(["write-tree"], root, env=env).strip()
+    finally:
+        Path(indice_tmp).unlink(missing_ok=True)
+    return _git(["diff", "--stat", desde, arvore, "--", *tocados], root).strip()
 
 
 def _extrair_caminho_status(linha: str) -> str:
@@ -875,7 +901,7 @@ def montar_documento(
 
     arquivos_alvo = extrair_arquivos_alvo(dossie.campos)
     literais_descartados = extrair_literais_nao_caminho(dossie.campos)
-    diff_stat = coletar_diff_stat(root)
+    diff_stat = coletar_diff_stat(root, desde)
     tocados = coletar_arquivos_tocados(root, desde)
     alvos_de_outras = mapear_alvos_de_outras_tarefas(plano_path, dossie.tarefa_id, root)
     escopo = confrontar_escopo(tocados, arquivos_alvo, root, alvos_de_outras)

```

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index 09dccf5..0c52bdb 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -1203,6 +1203,60 @@ def test_tf_trecho_desde_sem_alteracao_nao_despeja_o_arquivo(tmp_path):
     assert trechos["a.md"]["texto"] == f"(sem alteração desde `{snap}`)"
 
 
+def test_tf_diff_stat_desde_recorta_como_os_tocados(tmp_path):
+    """TF da AF-T1 (`TK-94a`): com `desde=<ref>`, o bloco `## Diff` de `montar_documento` resume
+    só o recorte que `coletar_arquivos_tocados(..., desde=ref)` já dá para a `## Arquivos
+    tocados` — a entrega, rastreada e não rastreada —, nunca o trabalho alheio já embutido na
+    árvore de `<ref>` (a regra antiga, `git diff HEAD --stat`, citaria o alheio e não citaria o
+    não rastreado)."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    plano = tmp_path / "plano.md"
+    _escrever_plano(plano, "edita `src/c.py` e cria `src/novo.py`.")
+
+    (repo / "src" / "c.py").write_text("def c():\n    return 1\n", encoding="utf-8")
+    _run_git(["add", "-A"], repo)
+    _run_git(["commit", "-m", "add c.py"], repo)
+
+    (repo / "src" / "b.py").write_text("def b():\n    return 2\n", encoding="utf-8")
+    ref = review_evidence.capturar_ref(repo)
+
+    (repo / "src" / "c.py").write_text("def c():\n    return 2\n", encoding="utf-8")
+    (repo / "src" / "novo.py").write_text("def novo():\n    return 3\n", encoding="utf-8")
+
+    documento = review_evidence.montar_documento(
+        plano, "T1", repo, desde=ref, comandos_guardas=_BATERIA_FAKE_VERDE
+    )
+
+    bloco = documento.split("## Diff (`git diff --stat`)")[1].split("## Arquivos tocados")[0]
+    assert "src/c.py" in bloco
+    assert "src/novo.py" in bloco
+    assert "src/b.py" not in bloco
+
+
+def test_tr_diff_stat_desde_sem_tocados_sai_sem_diferencas(tmp_path):
+    """TR da AF-T1: `<ref>` capturado e nada mudado depois — `coletar_diff_stat(repo, desde=ref)`
+    devolve string vazia (nunca roda `git diff --stat` sem caminho, que devolveria a árvore
+    inteira), e o bloco `## Diff` do documento traz `(sem diferenças)`, mesma convenção do diff
+    vazio sem `--desde`."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    plano = tmp_path / "plano.md"
+    _escrever_plano(plano, "edita `src/b.py`.")
+
+    ref = review_evidence.capturar_ref(repo)
+
+    assert review_evidence.coletar_diff_stat(repo, desde=ref) == ""
+
+    documento = review_evidence.montar_documento(
+        plano, "T1", repo, desde=ref, comandos_guardas=_BATERIA_FAKE_VERDE
+    )
+    bloco = documento.split("## Diff (`git diff --stat`)")[1].split("## Arquivos tocados")[0]
+    assert "(sem diferenças)" in bloco
+
+
 # --- FPU-T5 (DFP-17): o executor devolve a medida como arquivo, e a evidência a incorpora -------
 
 

```

## Medida do executor
- Arquivo: docs\plans\P-0753-auditoria-estagio-1\evidencia\P-0753-AF-T1-medida.json; mundo: depois; gerado em: 2026-09-27T11:30:04+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_review_evidence.py -q -k "diff_stat_desde"` | 0 | true |
| 2 | `python -m pytest -q` | 0 | true |
| 3 | `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
