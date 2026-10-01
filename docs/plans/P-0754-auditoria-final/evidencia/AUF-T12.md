# Evidência de revisão — P-0754 AUF-T12

## Diff (`git diff --stat`)
```
.claude/agents/pantonic-planner.md                        |  5 +++++
 docs/DIARIO_DE_OBRAS.md                                   |  4 ++--
 docs/plans/P-0754-auditoria-final/estado.tsv              |  2 +-
 .../evidencia/P-0754-AUF-T12-medida.json                  | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 24 insertions(+), 3 deletions(-)
```

## Arquivos tocados
- `.claude/agents/pantonic-planner.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0754-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T12-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `2f80def6bcc6383392e6a36df3f9fa7c2fa7f516`
- Arquivos-alvo declarados: `.claude/agents/pantonic-planner.md`
- Arquivos tocados: `.claude/agents/pantonic-planner.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T12-medida.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T12-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/agents/pantonic-planner.md`
```
diff --git a/.claude/agents/pantonic-planner.md b/.claude/agents/pantonic-planner.md
index 564e1bd..949905f 100644
--- a/.claude/agents/pantonic-planner.md
+++ b/.claude/agents/pantonic-planner.md
@@ -535,6 +535,11 @@ protocolo, encurtado, em seis passos:
    e o id dele entra na lista `tarefas:` daquela operação — lastro que é seu e do consultor (`GOVERNANCA.md`
    §3.2), não ato do modelador. Se a decisão nova muda o que o plano entrega, devolva também o
    dossiê `Ato de modelo` de `emenda`.
+
+   **Versão pendente reconfere a restrição que cita o estado do plano:** quando o modelador grava
+   uma versão pendente do modelo, toda `Restrição` de card que afirma estado do plano — seção que
+   existe ou não, versão vigente, operação presente — se reconfere contra o plano gravado, no mesmo
+   ato, e a que ficou falsa se reescreve (2026-09-27, `AE-20` do `P-0753`).
 5. **Fechar o estado** — tarefa de volta a `ready` (ou `cancelled`, se a rota mudou), plano de volta
    ao estado anterior, achado marcado como absorvido com ponteiro para a decisão, diretiva e
    `Fila corrente` do diário apontando a tarefa reaberta.

```

## Medida do executor
- Arquivo: docs\plans\P-0754-auditoria-final\evidencia\P-0754-AUF-T12-medida.json; mundo: depois; gerado em: 2026-09-28T15:09:11+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('[%d]'%t.count('Versão pendente reconfere a restrição que cita o estado do plano'))"` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
