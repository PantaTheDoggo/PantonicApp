# Evidência de revisão — P-0747 CON-T5a

## Diff (`git diff --stat`)
```
.claude/README.md                               |    2 +-
 .claude/agents/pantonic-consultant.md           |   41 +-
 .claude/agents/pantonic-executor.md             |    8 +-
 .claude/agents/pantonic-fora-da-caixa.md        |    2 +-
 .claude/agents/pantonic-model-designer.md       |   56 +-
 .claude/agents/pantonic-planner.md              |  139 +-
 .claude/agents/pantonic-reviewer.md             |    4 +-
 .claude/global/CLAUDE.md                        |   23 +-
 .claude/skills/bootstrap-pantonic/SKILL.md      |    2 +-
 .claude/skills/diario-de-obras/SKILL.md         |   71 +-
 .claude/skills/modelo-por-fase/SKILL.md         |    2 +-
 .claude/skills/passagem-de-bastao/SKILL.md      |   10 +-
 .claude/skills/scrum-master/SKILL.md            |   42 +-
 .claude/tools/modelo.py                         |   31 +-
 GOVERNANCA.md                                   |  227 ++--
 README.md                                       |   85 +-
 docs/CUSTO_DO_PICKUP.md                         |  113 ++
 docs/DIARIO_DE_OBRAS.md                         |  905 ++++++++++---
 docs/DIARIO_HISTORICO.md                        |  154 +++
 docs/DOC_MAP.md                                 |  110 +-
 docs/RDO/INDEX.md                               |   30 +
 docs/RESIDENCIA_DOUTRINA.md                     |    4 +-
 docs/consultant-spec.md                         |   61 +-
 docs/plans/P-0745-planejador-modelo-operacao.md | 1584 ++++++++++++++++++++---
 docs/plans/_INBOX.md                            |    3 +-
 docs/plans/_INBOX_HISTORICO.md                  |    3 +
 docs/telemetria.tsv                             |  116 ++
 tests/fixtures/modelo/fluxo-concluido.md        |   12 +-
 tests/fixtures/modelo/fluxo-pendente.md         |   20 +-
 tests/fixtures/modelo/fluxo-valido.md           |   12 +-
 tests/fixtures/modelo/plano-invalido-2.md       |   10 +-
 tests/fixtures/modelo/plano-invalido.md         |   12 +-
 tests/fixtures/modelo/plano-sem-cabecalho.md    |    8 +-
 tests/fixtures/modelo/plano-sem-estado.md       |    8 +-
 tests/test_modelo.py                            |  127 +-
 35 files changed, 3352 insertions(+), 685 deletions(-)
```

## Arquivos tocados
- `.claude/README.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-consultant.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-executor.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-fora-da-caixa.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-model-designer.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-planner.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-reviewer.md` — atribuição: alheio; estado git: ` M`
- `.claude/global/CLAUDE.md` — atribuição: da entrega; estado git: ` M`
- `.claude/skills/bootstrap-pantonic/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/diario-de-obras/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/skills/modelo-por-fase/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/passagem-de-bastao/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/scrum-master/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/tools/modelo.py` — atribuição: alheio; estado git: ` M`
- `GOVERNANCA.md` — atribuição: alheio; estado git: ` M`
- `README.md` — atribuição: alheio; estado git: ` M`
- `docs/ACIONAMENTOS_CONSULTOR.tsv` — atribuição: alheio; estado git: `??`
- `docs/CUSTO_DO_PICKUP.md` — atribuição: alheio; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/DIARIO_HISTORICO.md` — atribuição: alheio; estado git: ` M`
- `docs/DOC_MAP.md` — atribuição: alheio; estado git: ` M`
- `docs/OPERACOES_AS_IS.md` — atribuição: alheio; estado git: `??`
- `docs/OPERACOES_AS_IS_P-0745.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-76a-as-tabelas-do-modelo-em-frases-curtas-para-o-dono.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/INDEX.md` — atribuição: alheio; estado git: ` M`
- `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0745-PLN-T4a-o-ponteiro-sobrevivente-da-tabela-aposentada-nos-fatos-estav.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0745-PLN-T5-o-modelador-diante-do-plano-sem-cards-e-o-lastro-que-e-do-pl.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0745-PLN-T5a-a-frase-que-governa-o-gate-do-modelador-e-a-enumeracao-que-e.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0745-PLN-T6-a-especificacao-do-agente-de-planejamento.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0745-PLN-T7-o-indice-de-documentos-e-a-revisao-do-readme.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0745-PLN-T7a-o-readme-deixa-de-defender-a-regua-que-ele-mesmo-aposenta.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T1-o-consultor-entra-na-doutrina-de-governanca.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T2-a-definicao-de-conduta-do-consultor-sem-estatuto-provisorio.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T2a-corretivo-da-op-2-o-agente-descreve-o-cenario-persistido-e-l.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T3-o-loop-leva-toda-parada-ao-consultor.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T3a-corretivo-da-op-3-a-parada-e-a-mesma-em-todas-as-regras-que.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T3b-corretivo-da-op-3-com-estrategico-o-loop-para-sem-executar-a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T3c-corretivo-da-op-3-com-estrategico-a-rota-planejador-executa.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T4-a-forma-efemera-com-cenario-persistido.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T4a-corretivo-da-op-4-a-queda-de-uma-instancia-do-consultor-nao.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T5-o-outro-lado-da-fronteira-nas-definicoes-de-conduta.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T6-a-especificacao-vira-lastro-medido.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0745-PLN-T1.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0745-PLN-T2.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0745-PLN-T3.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0745-PLN-T4.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0745-PLN-T4a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0745-PLN-T5.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0745-PLN-T5a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0745-PLN-T6.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0745-PLN-T7.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0745-PLN-T7a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0746-LST-T1.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0746-LST-T3.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0746-LST-T5.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0746-LST-T6.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0746-LST-T7.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0746-LST-T8.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0746-LST-T9.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T1.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T2.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T2a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T3.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T3a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T3b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T3c.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T4.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T4a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T5.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T6.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-54-TK-54b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-76-TK-76a.md` — atribuição: alheio; estado git: `??`
- `docs/RESIDENCIA_DOUTRINA.md` — atribuição: alheio; estado git: ` M`
- `docs/consultant-spec.md` — atribuição: alheio; estado git: ` M`
- `docs/planner-spec.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0745-planejador-modelo-operacao.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0746-lastro-do-modelo.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0747-consultor-de-plano.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-P-0747.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_INBOX.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/_INBOX_HISTORICO.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/_VEREDITO-procedimentos-2026-09-22.md` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/modelo/fluxo-concluido.md` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/modelo/fluxo-pendente.md` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/modelo/fluxo-valido.md` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/modelo/plano-com-lastro.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-invalido-2.md` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/modelo/plano-invalido.md` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/modelo/plano-sem-cabecalho.md` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/modelo/plano-sem-estado.md` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/modelo/plano-sem-lastro.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-terminal-sem-lastro.md` — atribuição: alheio; estado git: `??`
- `tests/test_doutrina_unidade.py` — atribuição: alheio; estado git: `??`
- `tests/test_modelo.py` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `d75e7a656fe73d398263dde88dce8f29535d8dcb`
- Arquivos-alvo declarados: `.claude/skills/diario-de-obras/SKILL.md`, `.claude/global/CLAUDE.md`
- Arquivos tocados: `.claude/README.md`, `.claude/agents/pantonic-consultant.md`, `.claude/agents/pantonic-executor.md`, `.claude/agents/pantonic-fora-da-caixa.md`, `.claude/agents/pantonic-model-designer.md`, `.claude/agents/pantonic-planner.md`, `.claude/agents/pantonic-reviewer.md`, `.claude/global/CLAUDE.md`, `.claude/skills/bootstrap-pantonic/SKILL.md`, `.claude/skills/diario-de-obras/SKILL.md`, `.claude/skills/modelo-por-fase/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/modelo.py`, `GOVERNANCA.md`, `README.md`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/DIARIO_HISTORICO.md`, `docs/DOC_MAP.md`, `docs/OPERACOES_AS_IS.md`, `docs/OPERACOES_AS_IS_P-0745.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-76a-as-tabelas-do-modelo-em-frases-curtas-para-o-dono.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0745-PLN-T4a-o-ponteiro-sobrevivente-da-tabela-aposentada-nos-fatos-estav.md`, `docs/RDO/P-0745-PLN-T5-o-modelador-diante-do-plano-sem-cards-e-o-lastro-que-e-do-pl.md`, `docs/RDO/P-0745-PLN-T5a-a-frase-que-governa-o-gate-do-modelador-e-a-enumeracao-que-e.md`, `docs/RDO/P-0745-PLN-T6-a-especificacao-do-agente-de-planejamento.md`, `docs/RDO/P-0745-PLN-T7-o-indice-de-documentos-e-a-revisao-do-readme.md`, `docs/RDO/P-0745-PLN-T7a-o-readme-deixa-de-defender-a-regua-que-ele-mesmo-aposenta.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/P-0747-CON-T1-o-consultor-entra-na-doutrina-de-governanca.md`, `docs/RDO/P-0747-CON-T2-a-definicao-de-conduta-do-consultor-sem-estatuto-provisorio.md`, `docs/RDO/P-0747-CON-T2a-corretivo-da-op-2-o-agente-descreve-o-cenario-persistido-e-l.md`, `docs/RDO/P-0747-CON-T3-o-loop-leva-toda-parada-ao-consultor.md`, `docs/RDO/P-0747-CON-T3a-corretivo-da-op-3-a-parada-e-a-mesma-em-todas-as-regras-que.md`, `docs/RDO/P-0747-CON-T3b-corretivo-da-op-3-com-estrategico-o-loop-para-sem-executar-a.md`, `docs/RDO/P-0747-CON-T3c-corretivo-da-op-3-com-estrategico-a-rota-planejador-executa.md`, `docs/RDO/P-0747-CON-T4-a-forma-efemera-com-cenario-persistido.md`, `docs/RDO/P-0747-CON-T4a-corretivo-da-op-4-a-queda-de-uma-instancia-do-consultor-nao.md`, `docs/RDO/P-0747-CON-T5-o-outro-lado-da-fronteira-nas-definicoes-de-conduta.md`, `docs/RDO/P-0747-CON-T6-a-especificacao-vira-lastro-medido.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0745-PLN-T4a.md`, `docs/RDO/evidencia/P-0745-PLN-T5.md`, `docs/RDO/evidencia/P-0745-PLN-T5a.md`, `docs/RDO/evidencia/P-0745-PLN-T6.md`, `docs/RDO/evidencia/P-0745-PLN-T7.md`, `docs/RDO/evidencia/P-0745-PLN-T7a.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/P-0747-CON-T1.md`, `docs/RDO/evidencia/P-0747-CON-T2.md`, `docs/RDO/evidencia/P-0747-CON-T2a.md`, `docs/RDO/evidencia/P-0747-CON-T3.md`, `docs/RDO/evidencia/P-0747-CON-T3a.md`, `docs/RDO/evidencia/P-0747-CON-T3b.md`, `docs/RDO/evidencia/P-0747-CON-T3c.md`, `docs/RDO/evidencia/P-0747-CON-T4.md`, `docs/RDO/evidencia/P-0747-CON-T4a.md`, `docs/RDO/evidencia/P-0747-CON-T5.md`, `docs/RDO/evidencia/P-0747-CON-T6.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/RDO/evidencia/TK-76-TK-76a.md`, `docs/RESIDENCIA_DOUTRINA.md`, `docs/consultant-spec.md`, `docs/planner-spec.md`, `docs/plans/P-0745-planejador-modelo-operacao.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/P-0747-consultor-de-plano.md`, `docs/plans/_CENARIO-P-0747.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VEREDITO-procedimentos-2026-09-22.md`, `docs/telemetria.tsv`, `tests/fixtures/modelo/fluxo-concluido.md`, `tests/fixtures/modelo/fluxo-pendente.md`, `tests/fixtures/modelo/fluxo-valido.md`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/fixtures/modelo/plano-invalido.md`, `tests/fixtures/modelo/plano-sem-cabecalho.md`, `tests/fixtures/modelo/plano-sem-estado.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_doutrina_unidade.py`, `tests/test_modelo.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/README.md` → `CON-T8`, `.claude/agents/pantonic-consultant.md` → `CON-T2`, `.claude/agents/pantonic-executor.md` → `CON-T5`, `.claude/agents/pantonic-model-designer.md` → `CON-T5`, `.claude/agents/pantonic-planner.md` → `CON-T5`, `.claude/agents/pantonic-reviewer.md` → `CON-T5`, `.claude/skills/passagem-de-bastao/SKILL.md` → `CON-T5`, `.claude/skills/scrum-master/SKILL.md` → `CON-T3`, `GOVERNANCA.md` → `CON-T1`, `README.md` → `CON-T8`, `docs/ACIONAMENTOS_CONSULTOR.tsv` → `CON-T2`, `docs/DOC_MAP.md` → `CON-T6`, `docs/consultant-spec.md` → `CON-T6`, `docs/plans/_CENARIO-P-0747.md` → `CON-T4`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-76a-as-tabelas-do-modelo-em-frases-curtas-para-o-dono.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0745-PLN-T4a-o-ponteiro-sobrevivente-da-tabela-aposentada-nos-fatos-estav.md`, `docs/RDO/P-0745-PLN-T5-o-modelador-diante-do-plano-sem-cards-e-o-lastro-que-e-do-pl.md`, `docs/RDO/P-0745-PLN-T5a-a-frase-que-governa-o-gate-do-modelador-e-a-enumeracao-que-e.md`, `docs/RDO/P-0745-PLN-T6-a-especificacao-do-agente-de-planejamento.md`, `docs/RDO/P-0745-PLN-T7-o-indice-de-documentos-e-a-revisao-do-readme.md`, `docs/RDO/P-0745-PLN-T7a-o-readme-deixa-de-defender-a-regua-que-ele-mesmo-aposenta.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/P-0747-CON-T1-o-consultor-entra-na-doutrina-de-governanca.md`, `docs/RDO/P-0747-CON-T2-a-definicao-de-conduta-do-consultor-sem-estatuto-provisorio.md`, `docs/RDO/P-0747-CON-T2a-corretivo-da-op-2-o-agente-descreve-o-cenario-persistido-e-l.md`, `docs/RDO/P-0747-CON-T3-o-loop-leva-toda-parada-ao-consultor.md`, `docs/RDO/P-0747-CON-T3a-corretivo-da-op-3-a-parada-e-a-mesma-em-todas-as-regras-que.md`, `docs/RDO/P-0747-CON-T3b-corretivo-da-op-3-com-estrategico-o-loop-para-sem-executar-a.md`, `docs/RDO/P-0747-CON-T3c-corretivo-da-op-3-com-estrategico-a-rota-planejador-executa.md`, `docs/RDO/P-0747-CON-T4-a-forma-efemera-com-cenario-persistido.md`, `docs/RDO/P-0747-CON-T4a-corretivo-da-op-4-a-queda-de-uma-instancia-do-consultor-nao.md`, `docs/RDO/P-0747-CON-T5-o-outro-lado-da-fronteira-nas-definicoes-de-conduta.md`, `docs/RDO/P-0747-CON-T6-a-especificacao-vira-lastro-medido.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0745-PLN-T4a.md`, `docs/RDO/evidencia/P-0745-PLN-T5.md`, `docs/RDO/evidencia/P-0745-PLN-T5a.md`, `docs/RDO/evidencia/P-0745-PLN-T6.md`, `docs/RDO/evidencia/P-0745-PLN-T7.md`, `docs/RDO/evidencia/P-0745-PLN-T7a.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/P-0747-CON-T1.md`, `docs/RDO/evidencia/P-0747-CON-T2.md`, `docs/RDO/evidencia/P-0747-CON-T2a.md`, `docs/RDO/evidencia/P-0747-CON-T3.md`, `docs/RDO/evidencia/P-0747-CON-T3a.md`, `docs/RDO/evidencia/P-0747-CON-T3b.md`, `docs/RDO/evidencia/P-0747-CON-T3c.md`, `docs/RDO/evidencia/P-0747-CON-T4.md`, `docs/RDO/evidencia/P-0747-CON-T4a.md`, `docs/RDO/evidencia/P-0747-CON-T5.md`, `docs/RDO/evidencia/P-0747-CON-T6.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/RDO/evidencia/TK-76-TK-76a.md`, `docs/plans/P-0745-planejador-modelo-operacao.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/P-0747-consultor-de-plano.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VEREDITO-procedimentos-2026-09-22.md`, `docs/telemetria.tsv`
- Ato do dono, fora do ciclo de tarefa: `.claude/agents/pantonic-fora-da-caixa.md`
- Fato: 21 arquivo(s) fora dos alvos e sem atribuição: `.claude/skills/bootstrap-pantonic/SKILL.md`, `.claude/skills/modelo-por-fase/SKILL.md`, `.claude/tools/modelo.py`, `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_HISTORICO.md`, `docs/OPERACOES_AS_IS.md`, `docs/OPERACOES_AS_IS_P-0745.md`, `docs/RESIDENCIA_DOUTRINA.md`, `docs/planner-spec.md`, `tests/fixtures/modelo/fluxo-concluido.md`, `tests/fixtures/modelo/fluxo-pendente.md`, `tests/fixtures/modelo/fluxo-valido.md`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/fixtures/modelo/plano-invalido.md`, `tests/fixtures/modelo/plano-sem-cabecalho.md`, `tests/fixtures/modelo/plano-sem-estado.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_doutrina_unidade.py`, `tests/test_modelo.py`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/skills/diario-de-obras/SKILL.md`
```
diff --git a/.claude/skills/diario-de-obras/SKILL.md b/.claude/skills/diario-de-obras/SKILL.md
index 264e3a8..309d59c 100644
--- a/.claude/skills/diario-de-obras/SKILL.md
+++ b/.claude/skills/diario-de-obras/SKILL.md
@@ -76,16 +76,17 @@ os transcreve sem discricionariedade; nos demais estados, autoria e materializa
 | `done` | entregável aceito | laudo `seguir` ou `seguir com ressalva` acolhido e, onde o dono é o teste de sentido, o veredito dele |
 | `cancelled` | item que não será executado, por qualquer motivo | a triagem recusa; o escopo é descartado; o item é absorvido por outro |
 
-Plano cuja revisão foi pedida por quem executa ou orquestra é caso de `blocked` **de plano**, com a
-razão registrada; na **tarefa** correspondente, a razão tipada é `premissa`. Esse `blocked` de plano
-abre uma **rodada de replanejamento** como próxima tarefa do plano (`G-REPLAN`, `GOVERNANCA.md` §7
-item 17): o plano só sai de `blocked` quando a rodada fecha — a tarefa volta a `ready` ou
-`cancelled`, e a entrada `RP-<n>` fica em `## Achados da execução` do plano.
+Plano cuja revisão foi pedida por quem executa ou orquestra não vai a `blocked` por isso: a **tarefa**
+vai a `blocked` com a razão tipada `premissa`, e a parada vai à triagem do consultor, que devolve a
+rota (`G-REPLAN`, `GOVERNANCA.md` §7 item 17). Só a rota `planejador` é caso de `blocked` **de plano**,
+com a razão registrada, e abre uma **rodada de replanejamento** como próxima tarefa do plano: o plano
+só sai de `blocked` quando a rodada fecha — a tarefa volta a `ready` ou `cancelled`, e a entrada
+`RP-<n>` fica em `## Achados da execução` do plano. Nas rotas `resolve` e `modelador` o plano segue.
 
 ### Máquina de transições
 
 Toda transição é **materializada** pelo `scrum-master`; a **autoria** de `in-progress` → `review` e
-de `in-progress` → `blocked` é do executor (`DP-G`); a de `blocked` → `review` é do **planejador**,
+de `in-progress` → `blocked` é do executor (`DP-G`); a de `blocked` → `review` é do **consultor**, na rota `resolve` da triagem, ou do **planejador**,
 na rodada de replanejamento (`G-REPLAN`, `GOVERNANCA.md` §7 item 17), e nunca do executor. A coluna
 **gatilho** cita os dois — e só os dois — gatilhos que disparam ação automática.
 
@@ -99,7 +100,7 @@ na rodada de replanejamento (`G-REPLAN`, `GOVERNANCA.md` §7 item 17), e nunca d
 | `ready` → `cancelled` | escopo descartado ou absorvido por outro item | — |
 | `blocked` → `ready` | a razão registrada não se aplica mais | — |
 | `blocked` → `cancelled` | o bloqueio é permanente ou a rota mudou | — |
-| `blocked` → `review` | a rodada de replanejamento corrigiu o **aceite** de um `blocked premissa` cuja entrega material já está na árvore (`G-REPLAN`, saída (c)); nenhum retorno novo de executor é exigido | **gatilho 1** — o `scrum-master` invoca o `pantonic-reviewer` |
+| `blocked` → `review` | a triagem do consultor (rota `resolve`) ou a rodada de replanejamento corrigiu o **aceite** de um `blocked premissa` cuja entrega material já está na árvore (`G-REPLAN`, saída (c)); nenhum retorno novo de executor é exigido | **gatilho 1** — o `scrum-master` invoca o `pantonic-reviewer` |
 | `in-progress` → `review` | o executor devolve a linha de retorno da `DP-G` | **gatilho 1** — o `scrum-master` invoca o `pantonic-reviewer` |
 | `in-progress` → `blocked` | o executor para e escala | — |
 | `review` → `done` | laudo `seguir` ou `seguir com ressalva`, mais o aceite do dono onde ele é o teste de sentido | **gatilho 2** — o `scrum-master` escreve o RDO |
@@ -180,12 +181,51 @@ nível 2. Dentro dela, nesta ordem:
 | elemento | forma | regra |
 |---|---|---|
 | cabeçalho | `**Estado do modelo:** versão <n> · AAAA-MM-DD · autor: <papel> · <k> operações · <p> propriedades · situação: <vigente \| pendente>` | linha única; obrigatória (`V13`); `<n>` monotônico e `situação` é `vigente` na seção `## 1` |
-| objetos | `### 1.1 Objetos` + tabela `\| objeto \| o que é \| propriedades \| contrato \| origem \|`; `<objeto>` é u
```
[truncado em 4000 caracteres]

### `.claude/global/CLAUDE.md`
```
diff --git a/.claude/global/CLAUDE.md b/.claude/global/CLAUDE.md
index 35b23b9..75d537d 100644
--- a/.claude/global/CLAUDE.md
+++ b/.claude/global/CLAUDE.md
@@ -30,10 +30,11 @@ começar.
   **contexto limpo para a reexecução**.
 - **Capacidade** — mesmo coeso, o desempenho cai conforme o contexto enche. A capacidade não
   interrompe trabalho em curso: ela **dimensiona o trabalho antes de começar**. Quem planeja
-  delimita cada tarefa para caber num contexto coerente e coeso, autossuficiente em contexto para
-  a execução, dentro de uma estimativa de **50% de ocupação da janela, com tolerância até 60%**. O
-  número não é constante mágica: vem da literatura sobre decaimento de desempenho de agentes em
-  função do enchimento do contexto, e é revisto se a literatura indicar outro valor.
+  delimita cada tarefa como a **materialização de uma operação inteira do modelo do plano**,
+  coesa e autossuficiente em contexto para a execução; **nenhum percentual de ocupação entra
+  no dimensionamento** — a janela de 1M tokens deixou de limitar a granularidade, e o critério
+  de admissão de matéria numa tarefa é coesão, não custo. A ocupação é aviso da janela de
+  orquestração, entre tarefas, nunca critério de tarefa.
 
 **Sinais de poluição** (checagem obrigatória, lista não exaustiva): material de outra tarefa,
 outro plano ou outra iniciativa entrou no contexto; premissa que sustentava o trabalho foi
@@ -46,7 +47,7 @@ contradição é fatal quando atinge o **cenário** (premissa, rota, contrato),
 um **detalhe** que o próprio contexto já substituiu.
 
 **Consequências práticas:** para quem executa, vale **uma tarefa por contexto**, inalterado. Para
-quem orquestra, conduzir um plano **é** uma tarefa: o contexto atravessa várias tarefas atômicas
+quem orquestra, conduzir um plano **é** uma tarefa: o contexto atravessa várias tarefas
 sem violar nada, porque o cenário é o mesmo, e encerra na **troca de plano ou iniciativa** (troca
 de cenário) ou na capacidade, o que vier antes.
 
@@ -136,11 +137,11 @@ custo solta (caso medido: `GOVERNANCA.md` §3, kit Pantonic).
   corrigir) — nunca a cada micro-edição; tier superior só no fechamento.
 - **Sem re-leitura de verificação**: Edit/Write falham ruidosamente; reler o arquivo editado "para
   conferir" é um turno inteiro desperdiçado.
-- **Orçamento por tarefa atômica**: há um teto por classe de tarefa, calibrado pela série medida —
-  não um número único aqui; a tabela de tetos é autoridade do kit (`GOVERNANCA.md` §3, em projeto
-  Pantonic*). Estourar não é punição — é sinal de tarefa mal decomposta (replanejar) ou de método
-  ruim (thrashing editar-testar-editar sem plano interno); reportar no handover, não simplesmente
-  continuar.
+- **Classe do card é natureza, não teto**: nenhum número de turnos ou de ocupação dimensiona a
+  tarefa — a unidade é a operação do modelo do plano (`GOVERNANCA.md` §3, kit Pantonic).
+  Estourar não é punição — é sinal de operação mal recortada (volta ao modelador) ou de método
+  ruim (thrashing editar-testar-editar sem plano interno); reportar no handover, não
+  simplesmente continuar.
 - **Plano interno antes da primeira edição** — esboçar a sequência de mudanças reduz turnos de
   retrabalho.
 - **Fechamento enxuto**: um único registro canônico; relatório final ao orquestrador é ponteiro +
@@ -160,6 +161,6 @@ obstáculo técnico faz a fase intelectual vazar para a fase barata, sem o conte
   pendente, bloco a preencher, ramo condicional não resolvido, insumo que ainda não existe), o
   plano está incompleto — devolve ao planejamento e **não performa**.
 - **Rota é do dono:** ao bater num obstáculo que ameaça a rota aprovada, o executor **para**,
-  registra o achado e escala para replanejamento — nunca substitui a arquitetura por uma
+  registra o achado e devolve `blocked` à triagem do plano, que decide o destino da parada — nunca substitui a arquitetura por uma
   alternativa própria na mesma execução. Bifurcar rota exige decision record aprovado **ante
```
[truncado em 4000 caracteres]

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
