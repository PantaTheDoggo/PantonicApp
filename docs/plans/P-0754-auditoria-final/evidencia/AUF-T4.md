# Evidência de revisão — P-0754 AUF-T4

## Diff (`git diff --stat`)
```
.claude/tools/review_evidence.py                   | 13 ++++----
 docs/DIARIO_DE_OBRAS.md                            |  4 +--
 docs/plans/P-0754-auditoria-final/estado.tsv       |  2 +-
 .../evidencia/P-0754-AUF-T4-medida.json            | 15 +++++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_review_evidence.py                      | 38 ++++++++++++++++++++++
 6 files changed, 63 insertions(+), 10 deletions(-)
```

## Arquivos tocados
- `.claude/tools/review_evidence.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0754-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T4-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `6f5a6d27d9ced395eb5c97bba80a6c7887ea783f`
- Arquivos-alvo declarados: `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`
- Arquivos tocados: `.claude/tools/review_evidence.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T4-medida.json`, `docs/telemetria.tsv`, `tests/test_review_evidence.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T4-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index c3ed620..a9dc620 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -507,9 +507,9 @@ def confrontar_escopo(
     alvos_de_outras_tarefas: dict[str, str] | None = None,
 ) -> dict:
     """Veredito mecânico da dimensão `escopo` (`docs/RUBRICA_DE_REVISAO.md:63-77`) com os cinco
-    baldes da `DB-25` e da `DB-32`, nesta precedência: coberto pelos alvos do card > alvo de outra
-    tarefa do mesmo plano > registro da orquestração > ato do dono fora do ciclo de tarefa > fora
-    dos alvos sem atribuição. Só o último resolve o
+    baldes da `DB-25` e da `DB-32`, nesta precedência: coberto pelos alvos do card > registro da
+    orquestração > alvo de outra tarefa do mesmo plano > ato do dono fora do ciclo de tarefa >
+    fora dos alvos sem atribuição. Só o último resolve o
     veredito: vazio → `conforme`; não vazio → `None` (aberto), porque a faixa `parcial` depende de
     desvio declarado na entrega, insumo que este script não recebe.
 
@@ -543,11 +543,10 @@ def confrontar_escopo(
         if coberto(tocado):
             continue
         tocado_norm = _normalizar_separador(tocado)
-        dona = _tarefa_dona(tocado_norm, outros, root)
-        if dona is not None:
-            de_outra_tarefa[tocado] = dona
-        elif _eh_registro_orquestracao(tocado):
+        if _eh_registro_orquestracao(tocado):
             registro.append(tocado)
+        elif (dona := _tarefa_dona(tocado_norm, outros, root)) is not None:
+            de_outra_tarefa[tocado] = dona
         elif _eh_ato_do_dono(tocado):
             ato_do_dono.append(tocado)
         else:

```

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index 87a6920..5bc83ee 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -1529,3 +1529,41 @@ def test_tr_alvo_rastreado_alterado_nao_leva_a_marca_de_novo(tmp_path):
 
     assert "+    return 2" in texto
     assert "(arquivo novo" not in texto
+
+
+def test_tf_escrita_da_conducao_vence_o_alvo_de_outra_tarefa(tmp_path):
+    """AUF-T4 (`DAU-17`, `H-18` §2.1, `F-9`, `F-13`): tocado que é registro da orquestração
+    (`docs/DIARIO_DE_OBRAS.md`) e também está mapeado como alvo de outra tarefa do mesmo plano
+    vai para `registro_orquestracao`, não para `de_outra_tarefa` — a nova precedência testa
+    `_eh_registro_orquestracao` antes de `_tarefa_dona`."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+
+    escopo = review_evidence.confrontar_escopo(
+        ["docs/DIARIO_DE_OBRAS.md"],
+        ["src/b.py"],
+        repo,
+        {"docs/DIARIO_DE_OBRAS.md": "TK-1a"},
+    )
+
+    assert escopo["registro_orquestracao"] == ["docs/DIARIO_DE_OBRAS.md"]
+    assert escopo["de_outra_tarefa"] == {}
+
+
+def test_tr_alvo_de_outra_tarefa_fora_do_registro_segue_atribuido(tmp_path):
+    """Regressão: tocado que não é registro da orquestração e está mapeado como alvo de outra
+    tarefa do mesmo plano continua saindo em `de_outra_tarefa`, sem cair em `registro_orquestracao`."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+
+    escopo = review_evidence.confrontar_escopo(
+        ["src/c.py"],
+        ["src/b.py"],
+        repo,
+        {"src/c.py": "TK-1a"},
+    )
+
+    assert escopo["de_outra_tarefa"] == {"src/c.py": "TK-1a"}
+    assert escopo["registro_orquestracao"] == []

```

## Medida do executor
- Arquivo: docs\plans\P-0754-auditoria-final\evidencia\P-0754-AUF-T4-medida.json; mundo: depois; gerado em: 2026-09-28T14:17:45+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_review_evidence.py -q -k "escrita_da_conducao or fora_do_registro_segue"` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
