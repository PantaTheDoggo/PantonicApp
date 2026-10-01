# Evidência de revisão — P-0755 RAF-T12

## Diff (`git diff --stat`)
```
docs/DIARIO_DE_OBRAS.md                                   |  4 ++--
 docs/RUBRICA_DE_REVISAO.md                                | 10 ++++++----
 .../plans/P-0755-recomendacoes-auditoria-final/estado.tsv |  2 +-
 .../evidencia/P-0755-RAF-T12-medida.json                  | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 25 insertions(+), 7 deletions(-)
```

## Arquivos tocados
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/RUBRICA_DE_REVISAO.md` — atribuição: da entrega; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T12-medida.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`

## Escopo
- Recorte: desde `e98f412077ebbdc9f488b080b814299d211b8ead`
- Arquivos-alvo declarados: `docs/RUBRICA_DE_REVISAO.md`
- Arquivos tocados: `docs/DIARIO_DE_OBRAS.md`, `docs/RUBRICA_DE_REVISAO.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T12-medida.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T12-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `docs/RUBRICA_DE_REVISAO.md`
```
diff --git a/docs/RUBRICA_DE_REVISAO.md b/docs/RUBRICA_DE_REVISAO.md
index f93fbad..d9ed439 100644
--- a/docs/RUBRICA_DE_REVISAO.md
+++ b/docs/RUBRICA_DE_REVISAO.md
@@ -94,15 +94,17 @@ essa obrigação é **capacidade**, não card: atribuição por **hunk**.
 ### `testes`
 
 - **Pergunta:** os testes que o dossiê exige existem e passam?
-- **Fonte da evidência:** mecânica — presença dos arquivos de teste declarados e exit code da suíte
-  da área tocada.
+- **Fonte da evidência:** mecânica — presença dos arquivos de teste declarados, exit code da suíte
+  da área tocada e a seção `## Linhas removidas dos testes` da evidência.
 - **Bloqueante:** sim.
 - **`conforme`:** o teste funcional e o teste de regressão exigidos existem e a suíte fecha em
   exit 0.
 - **`parcial`:** os testes presentes passam, com cobertura menor que a declarada — teste funcional
   sem o de regressão que tranca o comportamento, por exemplo.
-- **`não conforme`:** teste exigido ausente, suíte em exit não-zero, ou teste cujo significado mudou
-  removido em vez de reescrito.
+- **`não conforme`:** teste exigido ausente, suíte em exit não-zero, teste cujo significado mudou
+  removido em vez de reescrito, ou asserção de teste existente removida sem que o card mande
+  removê-la — a linha aparece na seção `## Linhas removidas dos testes` da evidência (`R-12`,
+  `P-0755`).
 - **`não se aplica`:** dossiê de classe de redação, sem exigência de teste de código. A suíte
   continua medida pela dimensão `guardas`.
 

```

## Linhas removidas dos testes
- nenhum arquivo de teste entre os alvos

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T12-medida.json; mundo: depois; gerado em: 2026-09-29T09:22:58+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8');print('rubrica=%d-%d'%(t.count('removido em vez de reescrito.'),t.count('asserção de teste existente removida sem que o card mande')))"` | 0 | true |

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
