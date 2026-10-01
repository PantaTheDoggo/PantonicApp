# Evidência de revisão — P-0755 RAF-T1

## Diff (`git diff --stat`)
```
.claude/skills/scrum-master/SKILL.md                      |  5 +++++
 docs/DIARIO_DE_OBRAS.md                                   |  4 ++--
 .../plans/P-0755-recomendacoes-auditoria-final/estado.tsv |  2 +-
 .../evidencia/P-0755-RAF-T1-medida.json                   | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 24 insertions(+), 3 deletions(-)
```

## Arquivos tocados
- `.claude/skills/scrum-master/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T1-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `14f01618848483f88e5914b0c68ec8a5d6132767`
- Arquivos-alvo declarados: `.claude/skills/scrum-master/SKILL.md`
- Arquivos tocados: `.claude/skills/scrum-master/SKILL.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T1-medida.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T1-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/skills/scrum-master/SKILL.md`
```
diff --git a/.claude/skills/scrum-master/SKILL.md b/.claude/skills/scrum-master/SKILL.md
index fd226a0..6749e0a 100644
--- a/.claude/skills/scrum-master/SKILL.md
+++ b/.claude/skills/scrum-master/SKILL.md
@@ -40,6 +40,11 @@ Dez passos, nesta ordem.
   uma linha do relatório de encerramento. O loop nunca para para rebaixar o modelo. Modelo ativo
   **abaixo** do exigido: **PARA e pede ao dono o `/model` do modelo melhor** — a única parada do
   gate.
+   - **Janela:** o loop de um plano recém-planejado abre numa janela nova, separada da que o
+     planejou, com o plano gravado como único insumo; a janela do planejamento encerra no Marco 1
+     (`R-01` da auditoria final, `P-0755`). Quem conduz e planejou o plano na janela corrente não
+     despacha tarefa dele: encerra pelo relatório de janela, com a regra "loop de plano
+     recém-planejado abre em janela nova", e o dono abre a janela do loop.
 - **Saída:** modelo conferido, com a divergência anotada quando houver, ou parada com o `/model`
   do modelo melhor pedido.
 

```

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T1-medida.json; mundo: depois; gerado em: 2026-09-29T01:08:41+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('janela-nova=%d'%t.count('- **Janela:** o loop de um plano recém-planejado abre numa janela nova'))"` | 0 | true |

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
