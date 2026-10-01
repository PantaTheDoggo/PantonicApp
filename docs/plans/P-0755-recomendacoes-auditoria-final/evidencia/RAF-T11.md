# Evidência de revisão — P-0755 RAF-T11

## Diff (`git diff --stat`)
```
.claude/tools/review_evidence.py                   | 51 ++++++++++++++
 docs/DIARIO_DE_OBRAS.md                            |  4 +-
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T11-medida.json           | 15 ++++
 docs/telemetria.tsv                                |  1 +
 tests/test_review_evidence.py                      | 80 ++++++++++++++++++++++
 6 files changed, 150 insertions(+), 3 deletions(-)
```

## Arquivos tocados
- `.claude/tools/review_evidence.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T11-medida.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `2aea29d9575acfed89e92432b6b941ed75a43197`
- Arquivos-alvo declarados: `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`
- Arquivos tocados: `.claude/tools/review_evidence.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T11-medida.json`, `docs/telemetria.tsv`, `tests/test_review_evidence.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T11-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index 5a50558..a3a89c6 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -910,6 +910,52 @@ def secao_medida_do_executor(caminho_json: Path) -> list[str]:
     return linhas
 
 
+def _eh_alvo_de_teste(alvo: str) -> bool:
+    """RAF-T11 (`DRF-33`): verdadeiro quando o alvo, com separador normalizado, começa por
+    `tests/` e o nome do arquivo começa por `test_` e termina em `.py`."""
+    caminho = _normalizar_separador(alvo)
+    nome = caminho.rsplit("/", 1)[-1]
+    return caminho.startswith("tests/") and nome.startswith("test_") and nome.endswith(".py")
+
+
+def linhas_removidas_de_teste(
+    root: Path, arquivos_alvo: list[str], desde: str | None = None
+) -> dict[str, list[str]]:
+    """RAF-T11 (`DRF-33`; `F-17`, `F-18`; `R-12` do `P-0754`, `AE-97`/`AE-98`): para cada alvo,
+    na ordem, que não é curinga e é de arquivo de teste, a chave é o alvo como veio e o valor são
+    as linhas do diff que começam por `-` e não por `---`, na ordem — fato mecânico, sem julgar
+    se a remoção é legítima (isso é do revisor, `RAF-T12`)."""
+    removidas: dict[str, list[str]] = {}
+    for alvo in arquivos_alvo:
+        if _eh_alvo_curinga(alvo):
+            continue
+        if not _eh_alvo_de_teste(alvo):
+            continue
+        texto = _diff_para_arquivo(root, alvo, desde)
+        removidas[alvo] = [
+            linha
+            for linha in texto.splitlines()
+            if linha.startswith("-") and not linha.startswith("---")
+        ]
+    return removidas
+
+
+def _renderizar_removidas_de_teste(removidas: dict[str, list[str]]) -> list[str]:
+    linhas: list[str] = ["## Linhas removidas dos testes"]
+    if not removidas:
+        linhas.append("- nenhum arquivo de teste entre os alvos")
+        return linhas
+    for caminho, linhas_removidas in removidas.items():
+        if not linhas_removidas:
+            linhas.append(f"### `{caminho}` — nenhuma linha removida")
+            continue
+        linhas.append(f"### `{caminho}` — {len(linhas_removidas)} linha(s) removida(s)")
+        linhas.append("```")
+        linhas.extend(linhas_removidas)
+        linhas.append("```")
+    return linhas
+
+
 def _renderizar(
     *,
     plano_id: str,
@@ -928,6 +974,7 @@ def _renderizar(
     teto_guarda_chars: int,
     desde: str | None = None,
     linhas_medida: list[str] | None = None,
+    removidas_teste: dict[str, list[str]] | None = None,
 ) -> str:
     linhas: list[str] = []
     linhas.append(f"# Evidência de revisão — {plano_id} {tarefa_id}")
@@ -1012,6 +1059,9 @@ def _renderizar(
         if info["truncado"]:
             linhas.append(f"[truncado em {teto_diff_chars} caracteres]")
     linhas.append("")
+    if removidas_teste is not None:
+        linhas.extend(_renderizar_removidas_de_teste(removidas_teste))
+        linhas.append("")
     if linhas_medida is not None:
         linhas.extend(linhas_medida)
         linhas.append("")
@@ -1087,6 +1137,7 @@ def montar_documento(
         teto_guarda_chars=teto_guarda_chars,
         desde=desde,
         linhas_medida=secao_medida_do_executor(caminho_medida),
+        removidas_teste=linhas_removidas_de_teste(root, arquivos_alvo, desde),
     )
 
 

```

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index e0b0c2e..493fb19 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -2024,3 +2024,83 @@ def test_tr_acento_diff_renomeado_commitado_usa_o_caminho_novo(tmp_path):
         "src/c.py": f"R100 (commitado desde {ref})"
     }
     assert review_evidence.coletar_arquivos_tocados(repo, desde=ref) == ["src/c.py"]
+
+
+# --- RAF-T11 (DRF-33; F-17, F-18; R-12 do P-0754, AE-97/AE-98): a evidência mostra as linhas que
+# a entrega tirou dos testes -----------------------------------------------------------------
+
+
+def _repo_com_teste_versionado(tmp_path: Path) -> Path:
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    (repo / "tests").mkdir(parents=True, exist_ok=True)
+    (repo / "tests" / "test_a.py").write_text(
+        "def test_a():\n    assert 1 == 1\n    assert 2 == 2\n", encoding="utf-8"
+    )
+    _run_git(["add", "-A"], repo)
+    _run_git(["commit", "-m", "adiciona tests/test_a.py"], repo)
+    return repo
+
+
+def test_tf_removidas_de_teste_aparecem_na_evidencia(tmp_path):
+    """RAF-T11 (`DRF-33`; `F-17`, `F-18`; `R-12` do `P-0754`, `AE-97`/`AE-98`): a remoção de uma
+    asserção vizinha, que hoje passa verde sem aparecer em lugar nenhum do dossiê, chega como
+    seção própria mostrando a linha exata que saiu do teste."""
+    review_evidence = _load_review_evidence()
+    repo = _repo_com_teste_versionado(tmp_path)
+    ref = review_evidence.capturar_ref(repo)
+
+    (repo / "tests" / "test_a.py").write_text(
+        "def test_a():\n    assert 1 == 1\n", encoding="utf-8"
+    )
+
+    plano = tmp_path / "plano.md"
+    _escrever_plano(plano, "edita `tests/test_a.py`.")
+
+    documento = review_evidence.montar_documento(
+        plano, "T1", repo, desde=ref, comandos_guardas=_BATERIA_FAKE_VERDE
+    )
+
+    assert "## Linhas removidas dos testes" in documento
+    assert "### `tests/test_a.py` — 1 linha(s) removida(s)" in documento
+    assert "-    assert 2 == 2" in documento
+
+
+def test_tr_removidas_de_teste_so_acrescimo_diz_nenhuma(tmp_path):
+    """Regressão: arquivo de teste que só ganha linha (nenhuma remoção) diz 'nenhuma linha
+    removida' — e um alvo que não é arquivo de teste (`src/b.py`) não ganha entrada na seção; a
+    regra concorrente que listasse todo alvo daria uma entrada para ele também."""
+    review_evidence = _load_review_evidence()
+    repo = _repo_com_teste_versionado(tmp_path)
+    ref = review_evidence.capturar_ref(repo)
+
+    with (repo / "tests" / "test_a.py").open("a", encoding="utf-8") as arquivo:
+        arquivo.write("    assert 3 == 3\n")
+
+    plano = tmp_path / "plano.md"
+    _escrever_plano(plano, "edita `tests/test_a.py` e `src/b.py`.")
+
+    documento = review_evidence.montar_documento(
+        plano, "T1", repo, desde=ref, comandos_guardas=_BATERIA_FAKE_VERDE
+    )
+
+    secao = documento.split("## Linhas removidas dos testes", 1)[1]
+    secao = secao.split("## Medida do executor", 1)[0]
+    assert "### `tests/test_a.py` — nenhuma linha removida" in secao
+    assert "src/b.py" not in secao
+
+
+def test_tr_removidas_de_teste_sem_alvo_de_teste(tmp_path):
+    """Regressão: nenhum alvo de arquivo de teste na declaração — a seção diz o fato em vez de
+    ficar vazia ou listar arquivo que não é teste."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    plano = tmp_path / "plano.md"
+    _escrever_plano(plano, "edita `src/b.py`.")
+
+    documento = review_evidence.montar_documento(
+        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
+    )
+
+    assert "- nenhum arquivo de teste entre os alvos" in documento

```

## Linhas removidas dos testes
### `tests/test_review_evidence.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T11-medida.json; mundo: depois; gerado em: 2026-09-29T08:52:25+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_review_evidence.py -q -k removidas_de_teste` | 0 | true |

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
