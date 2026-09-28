# Evidência de revisão — P-0753 AF-T2

## Diff (`git diff --stat`)
```
.claude/tools/review_evidence.py                   |  5 ++-
 docs/DIARIO_DE_OBRAS.md                            |  2 +-
 docs/plans/P-0753-auditoria-estagio-1/estado.tsv   |  2 +-
 .../evidencia/P-0753-AF-T2-medida.json             | 43 ++++++++++++++++++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_review_evidence.py                      | 43 ++++++++++++++++++++++
 6 files changed, 92 insertions(+), 4 deletions(-)
```

## Arquivos tocados
- `.claude/tools/review_evidence.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T2-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `297ff1e376417ca39cf6ecc093f049c3b9b2bbcb`
- Arquivos-alvo declarados: `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`
- Arquivos tocados: `.claude/tools/review_evidence.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T2-medida.json`, `docs/telemetria.tsv`, `tests/test_review_evidence.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T2-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index 86cecb8..c17aa2e 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -48,7 +48,7 @@ repositório. Ausência de `--desde` preserva o comportamento anterior integralm
 
 A seção `## Escopo` classifica o arquivo tocado em cinco baldes (`P-0739` `DB-25`): coberto
 pelos alvos do card; alvo declarado por outra tarefa do mesmo plano; registro da orquestração
-(`docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/plans/`, `docs/RDO/`); ato do dono fora
+(`docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/plans/`, `docs/RDO/`, `docs/audits/`); ato do dono fora
 do ciclo de tarefa (`.claude/agents/`); fora dos alvos
 sem atribuição. Só o último resolve o veredito — `git` não sabe qual tarefa tocou qual arquivo,
 e o plano sabe qual tarefa declarou qual alvo.
@@ -404,12 +404,13 @@ _REGISTRO_ORQUESTRACAO = (
     "docs/telemetria.tsv",
     "docs/plans/",
     "docs/RDO/",
+    "docs/audits/",
 )
 
 
 def _eh_registro_orquestracao(caminho: str) -> bool:
     """Balde (3) da `DB-25` (`P-0739`): arquivo que a orquestração escreve por ofício — kanban,
-    telemetria, plano, RDO. Não é atribuível a tarefa nenhuma e por isso não pesa no veredito;
+    telemetria, plano, RDO, relatório de auditoria. Não é atribuível a tarefa nenhuma e por isso não pesa no veredito;
     aparece nomeado na seção `## Escopo`. Item terminado em `/` casa por prefixo."""
     alvo = _normalizar_separador(caminho)
     for item in _REGISTRO_ORQUESTRACAO:

```

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index 0c52bdb..a9cee44 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -594,6 +594,49 @@ def test_tf_registro_da_orquestracao_sai_em_balde_proprio(tmp_path):
     assert "Veredito mecânico: conforme" in documento
 
 
+def test_tf_relatorio_de_auditoria_sai_como_registro_da_orquestracao(tmp_path):
+    """TF da AF-T2: `docs/audits/` entra no balde de registro da orquestração — o relatório de
+    auditoria de quem conduz, tocado fora dos alvos do card, não pesa no veredito mecânico."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    plano = tmp_path / "plano.md"
+    _escrever_plano(plano, "edita `src/b.py`.")
+
+    (repo / "src" / "b.py").write_text("def b():\n    return 9\n", encoding="utf-8")
+    (repo / "docs" / "audits").mkdir(parents=True, exist_ok=True)
+    (repo / "docs" / "audits" / "AUDITORIA_X.md").write_text("# Auditoria\n", encoding="utf-8")
+
+    documento = review_evidence.montar_documento(
+        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
+    )
+
+    assert "Registro da orquestração (não atribuível a tarefa)" in documento
+    assert "Veredito mecânico: conforme" in documento
+
+
+def test_tr_relatorio_de_auditoria_alvo_do_card_segue_coberto(tmp_path):
+    """Regressão: quando `docs/audits/AUDITORIA_X.md` é o próprio alvo declarado do card, a
+    cobertura pelos `Arquivos-alvo` tem precedência sobre o balde de registro da orquestração —
+    a atribuição sai `da entrega`, nunca `registro da orquestração` (a regra concorrente, 'tudo em
+    `docs/audits/` é registro', daria registro da orquestração)."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    plano = tmp_path / "plano.md"
+    _escrever_plano(plano, "cria `docs/audits/AUDITORIA_X.md`.")
+
+    (repo / "docs" / "audits").mkdir(parents=True, exist_ok=True)
+    (repo / "docs" / "audits" / "AUDITORIA_X.md").write_text("# Auditoria\n", encoding="utf-8")
+
+    documento = review_evidence.montar_documento(
+        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
+    )
+
+    assert "- `docs/audits/AUDITORIA_X.md` — atribuição: da entrega; estado git: `" in documento
+    assert "Registro da orquestração" not in documento
+
+
 def test_tr_arquivo_sem_atribuicao_continua_fora_dos_alvos_com_veredito_aberto(tmp_path):
     """Regressão: arquivo que não é alvo de T1, não é alvo de nenhuma outra tarefa do plano e não é
     registro da orquestração continua caindo em 'fora dos alvos', com veredito aberto."""

```

## Medida do executor
- Arquivo: docs\plans\P-0753-auditoria-estagio-1\evidencia\P-0753-AF-T2-medida.json; mundo: depois; gerado em: 2026-09-27T11:48:33+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "import importlib.util as u;from pathlib import Path;s=u.spec_from_file_location('r',Path('.claude/tools/review_evidence.py'));m=u.module_from_spec(s);s.loader.exec_module(m);print(m._eh_registro_orquestracao('docs/audits/AUDITORIA_X.md'))"` | 0 | true |
| 2 | `python -c "from pathlib import Path;c=chr(96);t=Path('.claude/tools/review_evidence.py').read_text(encoding='utf-8');print(t.count(c+'docs/RDO/'+c+')'),t.count(c+'docs/RDO/'+c+', '+c+'docs/audits/'+c+')'),t.count('plano, RDO, relatório de auditoria'))"` | 0 | true |
| 3 | `python -m pytest tests/test_review_evidence.py -q -k "auditoria"` | 0 | true |
| 4 | `python -m pytest -q` | 0 | true |
| 5 | `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
