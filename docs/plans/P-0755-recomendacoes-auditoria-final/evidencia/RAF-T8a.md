# Evidência de revisão — P-0755 RAF-T8a

## Diff (`git diff --stat`)
```
docs/DIARIO_DE_OBRAS.md                                   |  6 +++---
 docs/RUBRICA_DE_REVISAO.md                                |  3 ++-
 .../plans/P-0755-recomendacoes-auditoria-final/estado.tsv |  2 +-
 .../evidencia/P-0755-RAF-T8a-medida.json                  | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 22 insertions(+), 5 deletions(-)
```

## Arquivos tocados
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/RUBRICA_DE_REVISAO.md` — atribuição: da entrega; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T8a-medida.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`

## Escopo
- Recorte: desde `36ec915b0580a548d0c2cca717bd8001606f3215`
- Arquivos-alvo declarados: `docs/RUBRICA_DE_REVISAO.md`
- Arquivos tocados: `docs/DIARIO_DE_OBRAS.md`, `docs/RUBRICA_DE_REVISAO.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T8a-medida.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T8a-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `docs/RUBRICA_DE_REVISAO.md`
```
diff --git a/docs/RUBRICA_DE_REVISAO.md b/docs/RUBRICA_DE_REVISAO.md
index b6b2d3d..f93fbad 100644
--- a/docs/RUBRICA_DE_REVISAO.md
+++ b/docs/RUBRICA_DE_REVISAO.md
@@ -47,7 +47,8 @@ Dimensão de fonte mista tem a parte mecânica travada e a parte de juízo livre
 
 A seção `## Arquivos tocados` do dossiê de evidência (`.claude/tools/review_evidence.py`) carrega
 essa mesma autoridade por arquivo: cada arquivo tocado sai marcado `da entrega` (coberto pelos
-`Arquivos-alvo` da tarefa) ou `alheio` (fora deles), com o estado `git` que comprova a marcação —
+`Arquivos-alvo` da tarefa), `registro da orquestração` (arquivo que quem conduz escreve por ofício,
+sem peso no veredito) ou `alheio` (os demais), com o estado `git` que comprova a marcação —
 atribuição derivada da mesma `confrontar_escopo` que resolve a dimensão `escopo` abaixo, nunca uma
 segunda classificação. O reviewer lê a atribuição já calculada; não a julga de memória nem depende
 de injeção manual de contexto do orquestrador (`AE-13`).

```

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T8a-medida.json; mundo: depois; gerado em: 2026-09-29T07:34:40+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "import sys;from pathlib import Path;t=Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8');a=t.count('(fora deles), com o estado');b=t.count('(arquivo que quem conduz escreve por ofício,');print('arquivos=%d-%d'%(a,b));sys.exit(0 if (a,b)==(0,1) else 1)"` | 0 | true |

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
