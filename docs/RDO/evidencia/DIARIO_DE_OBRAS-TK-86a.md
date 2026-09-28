# Evidência de revisão — DIARIO_DE_OBRAS TK-86a

## Diff (`git diff --stat`)
```
.claude/README.md                                  |    8 +-
 .claude/agents/pantonic-consultant.md              |   43 +-
 .claude/agents/pantonic-executor.md                |   11 +-
 .claude/agents/pantonic-fora-da-caixa.md           |    2 +-
 .claude/agents/pantonic-model-designer.md          |   81 +-
 .claude/agents/pantonic-planner.md                 |  217 +-
 .claude/agents/pantonic-reviewer.md                |   15 +-
 .claude/checks/kit_check.ps1                       |   39 +-
 .claude/global/CLAUDE.md                           |   67 +-
 .../hooks/modelo_por_fase_userpromptsubmit.py      |   13 +-
 .claude/projecoes.json                             |   47 +
 .claude/skills/bootstrap-pantonic/SKILL.md         |    6 +-
 .claude/skills/diario-de-obras/SKILL.md            |  156 +-
 .claude/skills/entrega-de-encerramento/SKILL.md    |    2 +-
 .claude/skills/modelo-por-fase/SKILL.md            |   26 +-
 .claude/skills/passagem-de-bastao/SKILL.md         |   53 +-
 .claude/skills/redacao-doc/SKILL.md                |    3 +-
 .claude/skills/scrum-master/SKILL.md               |  217 +-
 .claude/tools/backlog.py                           |  533 ++-
 .claude/tools/backlog_hook.py                      |   14 +-
 .claude/tools/card_check.py                        |  403 ++-
 .claude/tools/modelo.py                            |   39 +-
 .claude/tools/rdo.py                               |  228 +-
 .claude/tools/rdo_template.md                      |   10 +
 .claude/tools/review_evidence.py                   |  166 +-
 GOVERNANCA.md                                      |  389 ++-
 README.md                                          |  196 +-
 docs/CUSTO_DO_PICKUP.md                            |  171 +
 docs/DIARIO_DE_OBRAS.md                            | 3572 ++++++++++++++++++--
 docs/DIARIO_HISTORICO.md                           |  154 +
 docs/DOC_MAP.md                                    |  115 +-
 docs/RDO/INDEX.md                                  |  120 +
 docs/RESIDENCIA_DOUTRINA.md                        |    4 +-
 docs/RUBRICA_DE_REVISAO.md                         |   27 +-
 docs/consultant-spec.md                            |   75 +-
 docs/plans/P-0741-modelo-conceitual.md             |    8 +-
 docs/plans/P-0745-planejador-modelo-operacao.md    | 1584 ++++++++-
 docs/plans/_INBOX.md                               |    3 +-
 docs/plans/_INBOX_HISTORICO.md                     |    8 +
 docs/telemetria.tsv                                |  375 ++
 .../backlog/vermelho/docs/DIARIO_DE_OBRAS.md       |    3 +
 tests/fixtures/modelo/fluxo-concluido.md           |   12 +-
 tests/fixtures/modelo/fluxo-pendente.md            |   20 +-
 tests/fixtures/modelo/fluxo-valido.md              |   12 +-
 tests/fixtures/modelo/plano-invalido-2.md          |   10 +-
 tests/fixtures/modelo/plano-invalido.md            |   12 +-
 tests/fixtures/modelo/plano-sem-cabecalho.md       |    8 +-
 tests/fixtures/modelo/plano-sem-estado.md          |    8 +-
 tests/test_backlog.py                              |  770 +++++
 tests/test_card_check.py                           |  208 ++
 tests/test_materializar.py                         |    2 +-
 tests/test_modelo.py                               |  143 +-
 tests/test_rdo.py                                  |  357 +-
 tests/test_review_evidence.py                      |  265 +-
 54 files changed, 9973 insertions(+), 1057 deletions(-)
```

## Arquivos tocados
- `.claude/tools/encerrar.py` — atribuição: da entrega; estado git: `??`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/RDO/evidencia/P-0751-TK-86a-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `04a5ae0c55c963576c408c547522afbaf2618ec7`
- Arquivos-alvo declarados: `.claude/tools/backlog.py`, `tests/test_backlog.py`, `docs/PISO_C11.tsv`, `.claude/tools/encerrar.py`
- Literais não reconhecidos como caminho (5): `git check-ignore`, `1`, `TK-88`, `TK-88b`, `TK-88d`
- Arquivos tocados: `.claude/tools/encerrar.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/evidencia/P-0751-TK-86a-medida.json`, `docs/telemetria.tsv`
- Atribuídos a outra tarefa do mesmo plano: `docs/DIARIO_DE_OBRAS.md` → `TK-54b`
- Registro da orquestração (não atribuível a tarefa): `docs/RDO/evidencia/P-0751-TK-86a-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/backlog.py`
```
(sem alteração desde `04a5ae0c55c963576c408c547522afbaf2618ec7`)
```

### `tests/test_backlog.py`
```
(sem alteração desde `04a5ae0c55c963576c408c547522afbaf2618ec7`)
```

### `docs/PISO_C11.tsv`
```
arquivo	secao	origem
GOVERNANCA.md	1.1	TK-60a, medido em 2026-09-20

```

### `.claude/tools/encerrar.py`
```
"""TK-88 (`docs/DIARIO_DE_OBRAS.md` `## TK-88`) — o fechamento de tarefa e o de plano deixam de
ser uma sequência de comandos e prosa escrita à mão e passam a ser **um comando cada**, que recebe
a informação da tarefa realizada, escreve os artefatos de fechamento que o kit já tinha e faz os
registros nos documentos de backlog no mesmo ato.

Lugar comum medido (2026-09-26, sobre os fechamentos de `P-0745`..`P-0751`): fechar uma tarefa
eram quatro comandos em turnos separados — `modelo.py check`, `backlog.py status <ID> done`,
`rdo.py close` com o pacote do laudo **redigitado** a partir do arquivo que `rdo.py laudo` já
tinha gravado, e `telemetria.py append` conferindo a linha do hook —, mais o achado `AE-<n>`
editado no plano; fechar um plano era inteiramente manual, porque o instrumento recusava
`ready → done` para plano (registrado no diário em 2026-09-25) e o parágrafo de fechamento, a
linha do índice e a triagem dos achados eram escritos à mão.

Três verbos, todos com as checagens **antes** de qualquer escrita. `tarefa` e `plano` **reportam**
resultado e histórico; `handover` **entrega** — é o que quem vem depois espera da tarefa, de forma
inequívoca, direta e objetiva, inteiramente de máquina, registrado **na própria tarefa**:

``python .claude/tools/encerrar.py handover --plano <caminho.md> --tarefa <ID> --entregue "<o que
existe, com caminho:linha>" --contrato "<com o que a sucessora conta>" [--nao-refazer "<o que já
está pago>"] [--pendente "<o que fica de propósito>"] [--para <ID|papel>]... [--repo] [--data]``

Escreve (ou substitui) o campo `- **Handover:** <data> · para \\`<ID>\\`...` com os sub-bullets
`Entregue`, `Contrato`, `Não refazer` e `Pendente` no card, antes de `- **Notas de execução:**`;
exige entrega na árvore (`in-progress`, `review`, `done` ou `blocked`). A nomenclatura é a
âncora da recuperação: `backlog.py next` (`handovers_para`) devolve, sob `=== HANDOVER DE <ID>`,
junto com a próxima tarefa, o handover de todo irmão que a nomeia em `para` e, na falta, o da
antecessora imediata — o orquestrador cola na delegação o que for pertinente. O `rdo.py close`
transcreve o campo no RDO como extra do card, e `show <ID>` o imprime verbatim.

Os outros dois:

``python .claude/tools/encerrar.py tarefa --plano <caminho.md> --tarefa <ID> [--resumo "<frase>"]
[--pendencia "<uma linha>"] [--achado "<texto>" "<rota>"]... [--laudo <caminho>]
[--tool-uses N --tokens-k K --duracao-s S [--modelo-agente <nome>]] [--progresso <caminho>]
[--rdo-dir <dir>] [--repo <raiz>] [--data AAAA-MM-DD]``

1. a tarefa está em `review` (única transição que produz RDO — skill `diario-de-obras`,
   *Máquina de transições*, gatilho 2); 2. o laudo existe (`<pasta>/laudos/<ID>.md` ou
   `docs/RDO/laudos/<plano>-<ID>.md`) e o pacote é **transcrito** dele — veredito, percentual,
   bloqueante, recomendação, pendência e lições —, nunca redigitado; `reprovado` é recusado
   (`GOVERNANCA.md` §4.2: não é desfecho de RDO); 3. o consumo vem da **fonte única**
   `docs/telemetria.tsv` (última linha da tarefa, gravada pelo hook `SubagentStop`) ou, quando o
   chamador traz o bloco `<usage>` em `--tool-uses/--tokens-k/--duracao-s`, é apensado à série no
   mesmo ato; sem nenhum dos dois o fechamento é recusado — número inventado não fecha tarefa;
   4. `modelo.py check` sai `0` ou `2` (exit `1` mantém a tarefa em `review`, `DMC-30`).
   Passadas as checagens, e nesta ordem: `backlog.transacionar_status(<ID>, done)` com a nota de
   fechamento (bullet do card, índice `done/total`, bloco `Fila corrente`, `estado.tsv`);
   `rdo.cmd_close` em processo, com as seções `# Humano` e `# Histórico` preenchidas — o humano em
   linguagem corrente, com o título da tarefa no lugar da sigla (`GOVERNANCA.md` §4.2, *Mensagem
   legível ao dono*), e o histórico com as linhas que o painel do gerente (`progresso_hook.py`)
   gerou para a tarefa; a linha de telemetria, se o consumo veio por argumento; e cada `--achado`
   como entrada `AE-<n>` com `**Rota:**` em `## Achados
```
[truncado em 4000 caracteres]

## Medida do executor
- ausente: docs\RDO\evidencia\DIARIO_DE_OBRAS-TK-86a-medida.json não existe

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
