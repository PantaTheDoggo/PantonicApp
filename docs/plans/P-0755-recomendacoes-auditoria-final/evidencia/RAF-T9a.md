# Evidência de revisão — P-0755 RAF-T9a

## Diff (`git diff --stat`)
```
docs/DIARIO_DE_OBRAS.md                                   |  6 +++---
 .../plans/P-0755-recomendacoes-auditoria-final/estado.tsv |  2 +-
 .../evidencia/P-0755-RAF-T9a-medida.json                  | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 tests/test_review_evidence.py                             |  6 +++---
 5 files changed, 23 insertions(+), 7 deletions(-)
```

## Arquivos tocados
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T9a-medida.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `8656ea1d1fe54c4f87d8e5fb9ed9bc0e0ea63f51`
- Arquivos-alvo declarados: `tests/test_review_evidence.py`
- Arquivos tocados: `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T9a-medida.json`, `docs/telemetria.tsv`, `tests/test_review_evidence.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T9a-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index d493fc6..65722f8 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -1456,9 +1456,9 @@ def test_tf_caminho_acentuado_do_status_entra_nos_tocados_pelo_ramo_de_caminho_a
 
 
 def test_tf_alvo_com_curinga_casa_os_tocados(tmp_path):
-    """AUF-T3: alvo com curinga (`relatorios/*.md`) casa, por `fnmatch`, cada tocado que bate com
-    o padrão — não a regra antiga, que descartava o literal e dava os dois arquivos como fora dos
-    alvos com uma entrada só sob a chave do padrão."""
+    """AUF-T3: alvo com curinga (`relatorios/*.md`) casa, por `_casa_curinga` (RAF-T9), cada
+    tocado que bate com o padrão — não a regra antiga, que descartava o literal e dava os dois
+    arquivos como fora dos alvos com uma entrada só sob a chave do padrão."""
     review_evidence = _load_review_evidence()
     repo = tmp_path / "repo"
     _init_repo_com_baseline(repo)

```

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T9a-medida.json; mundo: depois; gerado em: 2026-09-29T08:00:09+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "import pathlib,sys; t=pathlib.Path('tests/test_review_evidence.py').read_text(encoding='utf-8'); q=chr(96); a=t.count('por '+q+'fnmatch'+q); d=t.count('por '+q+'_casa_curinga'+q+' (RAF-T9)'); print('docstring=%d-%d'%(a,d)); sys.exit(0 if (a,d)==(0,1) else 1)"` | 0 | true |

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
