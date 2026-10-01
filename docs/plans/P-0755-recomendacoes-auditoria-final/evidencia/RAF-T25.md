# Evidência de revisão — P-0755 RAF-T25

## Diff (`git diff --stat`)
```
.claude/agents/pantonic-planner.md                        |  9 +++++++++
 docs/DIARIO_DE_OBRAS.md                                   |  4 ++--
 .../plans/P-0755-recomendacoes-auditoria-final/estado.tsv |  2 +-
 .../evidencia/P-0755-RAF-T25-medida-depois.json           | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 28 insertions(+), 3 deletions(-)
```

## Arquivos tocados
- `.claude/agents/pantonic-planner.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T25-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`

## Escopo
- Recorte: desde `4774d67f73e811a802f631d21782eaedb0c23f56`
- Arquivos-alvo declarados: `.claude/agents/pantonic-planner.md`
- Arquivos tocados: `.claude/agents/pantonic-planner.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T25-medida-depois.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T25-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/agents/pantonic-planner.md`
```
diff --git a/.claude/agents/pantonic-planner.md b/.claude/agents/pantonic-planner.md
index 9f1ae60..c189117 100644
--- a/.claude/agents/pantonic-planner.md
+++ b/.claude/agents/pantonic-planner.md
@@ -562,6 +562,15 @@ protocolo, encurtado, em seis passos:
    uma versão pendente do modelo, toda `Restrição` de card que afirma estado do plano — seção que
    existe ou não, versão vigente, operação presente — se reconfere contra o plano gravado, no mesmo
    ato, e a que ficou falsa se reescreve (2026-09-27, `AE-20` do `P-0753`).
+
+   **Card da operação nova** (`R-04` da auditoria final, `P-0755`): na rodada que segue uma
+   emenda que cria operação sem card — o `modelo.py check` sem `--so-vigente` acusa
+   `1A: V1 OP-<n> — operação sem tarefa` —, o planejador escreve o card dessa operação, com o
+   campo `Operação do modelo` copiado da `## 1A` e o id da convenção de lastro sobre o número
+   da operação na `## 1A` (com sufixo `a`, `b`, … quando esse id já existe no plano); apensa o
+   id à lista `tarefas:` da operação na `## 1A`; e registra o card em `estado.tsv` `blocked`,
+   razão `dependencia`, nota `aguarda o aceite da versão <k> no marco`. A janela segue com as
+   tarefas da vigente, e a promoção do marco reescreve o campo dos cards.
 5. **Fechar o estado** — tarefa de volta a `ready` (ou `cancelled`, se a rota mudou), plano de volta
    ao estado anterior, achado marcado como absorvido com ponteiro para a decisão, diretiva e
    `Fila corrente` do diário apontando a tarefa reaberta.

```

## Linhas removidas dos testes
- nenhum arquivo de teste entre os alvos

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T25-medida-depois.json; mundo: depois; gerado em: 2026-09-29T21:51:28+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('nova=%d'%t.count('**Card da operação nova**'))"` | 0 | true |

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
