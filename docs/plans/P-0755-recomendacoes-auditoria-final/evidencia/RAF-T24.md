# Evidência de revisão — P-0755 RAF-T24

## Diff (`git diff --stat`)
```
.claude/skills/scrum-master/SKILL.md                      |  2 +-
 docs/DIARIO_DE_OBRAS.md                                   |  4 ++--
 .../plans/P-0755-recomendacoes-auditoria-final/estado.tsv |  2 +-
 .../evidencia/P-0755-RAF-T24-medida-depois.json           | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 20 insertions(+), 4 deletions(-)
```

## Arquivos tocados
- `.claude/skills/scrum-master/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T24-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`

## Escopo
- Recorte: desde `71a759157900a1f7b5520f2c567118818bbe7c5d`
- Arquivos-alvo declarados: `.claude/skills/scrum-master/SKILL.md`
- Arquivos tocados: `.claude/skills/scrum-master/SKILL.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T24-medida-depois.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T24-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/skills/scrum-master/SKILL.md`
```
diff --git a/.claude/skills/scrum-master/SKILL.md b/.claude/skills/scrum-master/SKILL.md
index e4ad929..841a40d 100644
--- a/.claude/skills/scrum-master/SKILL.md
+++ b/.claude/skills/scrum-master/SKILL.md
@@ -191,7 +191,7 @@ Dez passos, nesta ordem.
 - **Entrada:** `status`, `veredito`, `bloqueante`, `recomendação`, contador de retentativas.
 - **Ação:** aplicar a tabela do bloco A **em ordem de precedência** — a primeira regra que casa
   vence.
-- **Triagem:** toda regra que escala ao consultor (`A3a`, `A3b`, `A3c`, `A6a`, `A7`, `B1` e o gate do modelo do passo 9) recebe de volta a linha `rota=<resolve|modelador|planejador>` — e, quando o consultor classificar o impedimento como estratégico, a linha `estrategico=<uma frase>` logo abaixo dela — e despacha por ela: `estrategico=` presente — **PARA** em qualquer rota, e nas rotas `resolve` e `modelador` **sem executar a ação da rota**: o reparo que o consultor já gravou fica no plano, o modelador **não** é despachado, e a frase, a rota e o dossiê de emenda, se houver, vão ao relatório de encerramento, para o dono decidir antes de qualquer ato sobre o modelo (`G-NOASK`; `P-0747` `DCS-28`); com `rota=planejador` a ação da rota já é a parada e se executa como está — o plano materializado `blocked`, a rodada de replanejamento enfileirada — e a frase vai junto ao relatório; `rota=resolve` sem `estrategico=` — o reparo já está gravado no plano, e a janela segue; quando o reparo é a recusa do impedimento como improcedente (`P-0747` `DCS-35`), a mesma tarefa volta a `ready` com ao menos uma linha nova gravada pelo consultor e é redespachada **sem** consumir retentativa; `rota=modelador` — despacha o `pantonic-model-designer` com o dossiê `Ato de modelo` de `emenda` que o consultor devolveu, sem parar a janela: a versão pendente coexiste com a vigente até o marco, onde o pedido de validar ou recusar o drift sobe ao dono (`GOVERNANCA.md` §3.2), e com a recusa o caso volta ao consultor para resolver preservando o modelo; `rota=planejador` — materializa o plano como `blocked`, e a rodada de replanejamento vira a próxima tarefa do plano (`G-REPLAN`, `GOVERNANCA.md` §7 item 17): **PARA**.
+- **Triagem:** toda regra que escala ao consultor (`A3a`, `A3b`, `A3c`, `A6a`, `A7`, `B1` e o gate do modelo do passo 9) recebe de volta a linha `rota=<resolve|modelador|planejador>` — e, quando o consultor classificar o impedimento como estratégico, a linha `estrategico=<uma frase>` logo abaixo dela — e despacha por ela: `estrategico=` presente — **PARA** em qualquer rota, e nas rotas `resolve` e `modelador` **sem executar a ação da rota**: o reparo que o consultor já gravou fica no plano, o modelador **não** é despachado, e a frase, a rota e o dossiê de emenda, se houver, vão ao relatório de encerramento, para o dono decidir antes de qualquer ato sobre o modelo (`G-NOASK`; `P-0747` `DCS-28`); com `rota=planejador` a ação da rota já é a parada e se executa como está — o plano materializado `blocked`, a rodada de replanejamento enfileirada — e a frase vai junto ao relatório; `rota=resolve` sem `estrategico=` — o reparo já está gravado no plano, e a janela segue; quando o reparo é a recusa do impedimento como improcedente (`P-0747` `DCS-35`), a mesma tarefa volta a `ready` com ao menos uma linha nova gravada pelo consultor e é redespachada **sem** consumir retentativa; `rota=modelador` — despacha o `pantonic-model-designer` com o dossiê `Ato de modelo` de `emenda` que o consultor devolveu, sem parar a janela: a versão pendente coexiste com a vigente até o marco, onde o pedido de validar ou recusar o drift sobe ao dono (`GOVERNANCA.md` §3.2), e com a recusa o caso volta ao consultor para resolver preservando o modelo; quando, depois do modelador, `python .claude/tools/modelo.py check --plano <plano>` (sem `--so-vigente`) acusar `1A: V1 OP-<n> — operação sem tarefa`, a emenda criou operação nova, e o loop despacha em seguida o `pantonic-planner` para a rodada de replanejamento, que escreve o card dessa operaç
```
[truncado em 4000 caracteres]

## Linhas removidas dos testes
- nenhum arquivo de teste entre os alvos

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T24-medida-depois.json; mundo: depois; gerado em: 2026-09-29T21:42:50+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('rodada=%d'%t.count('o loop despacha em seguida o '))"` | 0 | true |

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
