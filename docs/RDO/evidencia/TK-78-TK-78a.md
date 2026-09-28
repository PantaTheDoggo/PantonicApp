# Evidência de revisão — DIARIO_DE_OBRAS TK-78a

## Diff (`git diff --stat`)
```
.claude/README.md                                  |    6 +-
 .claude/agents/pantonic-consultant.md              |   43 +-
 .claude/agents/pantonic-executor.md                |    8 +-
 .claude/agents/pantonic-fora-da-caixa.md           |    2 +-
 .claude/agents/pantonic-model-designer.md          |   56 +-
 .claude/agents/pantonic-planner.md                 |  139 +-
 .claude/agents/pantonic-reviewer.md                |    4 +-
 .claude/global/CLAUDE.md                           |   23 +-
 .../hooks/modelo_por_fase_userpromptsubmit.py      |    8 +-
 .claude/skills/bootstrap-pantonic/SKILL.md         |    2 +-
 .claude/skills/diario-de-obras/SKILL.md            |   71 +-
 .claude/skills/modelo-por-fase/SKILL.md            |   26 +-
 .claude/skills/passagem-de-bastao/SKILL.md         |   10 +-
 .claude/skills/scrum-master/SKILL.md               |   79 +-
 .claude/tools/modelo.py                            |   31 +-
 GOVERNANCA.md                                      |  227 +--
 README.md                                          |   91 +-
 docs/CUSTO_DO_PICKUP.md                            |  113 ++
 docs/DIARIO_DE_OBRAS.md                            | 1238 +++++++++++++--
 docs/DIARIO_HISTORICO.md                           |  154 ++
 docs/DOC_MAP.md                                    |  110 +-
 docs/RDO/INDEX.md                                  |   40 +
 docs/RESIDENCIA_DOUTRINA.md                        |    4 +-
 docs/consultant-spec.md                            |   75 +-
 docs/plans/P-0745-planejador-modelo-operacao.md    | 1584 ++++++++++++++++++--
 docs/plans/_INBOX.md                               |    3 +-
 docs/plans/_INBOX_HISTORICO.md                     |    4 +
 docs/telemetria.tsv                                |  145 ++
 tests/fixtures/modelo/fluxo-concluido.md           |   12 +-
 tests/fixtures/modelo/fluxo-pendente.md            |   20 +-
 tests/fixtures/modelo/fluxo-valido.md              |   12 +-
 tests/fixtures/modelo/plano-invalido-2.md          |   10 +-
 tests/fixtures/modelo/plano-invalido.md            |   12 +-
 tests/fixtures/modelo/plano-sem-cabecalho.md       |    8 +-
 tests/fixtures/modelo/plano-sem-estado.md          |    8 +-
 tests/test_modelo.py                               |  127 +-
 36 files changed, 3799 insertions(+), 706 deletions(-)
```

## Arquivos tocados
- `.claude/README.md` — atribuição: da entrega; estado git: ` M`
- `.claude/agents/pantonic-consultant.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-executor.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-fora-da-caixa.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-model-designer.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-planner.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-reviewer.md` — atribuição: alheio; estado git: ` M`
- `.claude/global/CLAUDE.md` — atribuição: alheio; estado git: ` M`
- `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` — atribuição: da entrega; estado git: ` M`
- `.claude/skills/bootstrap-pantonic/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/diario-de-obras/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/modelo-por-fase/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/skills/passagem-de-bastao/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/scrum-master/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/modelo.py` — atribuição: alheio; estado git: ` M`
- `GOVERNANCA.md` — atribuição: da entrega; estado git: ` M`
- `README.md` — atribuição: da entrega; estado git: ` M`
- `docs/ACIONAMENTOS_CONSULTOR.tsv` — atribuição: alheio; estado git: `??`
- `docs/CUSTO_DO_PICKUP.md` — atribuição: alheio; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/DIARIO_HISTORICO.md` — atribuição: alheio; estado git: ` M`
- `docs/DOC_MAP.md` — atribuição: alheio; estado git: ` M`
- `docs/OPERACOES_AS_IS.md` — atribuição: alheio; estado git: `??`
- `docs/OPERACOES_AS_IS_P-0745.md` — atribuição: alheio; estado git: `??`
- `docs/OPERACOES_AS_IS_P-0747.md` — atribuição: alheio; estado git: `??`
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
- `docs/RDO/P-0747-CON-T2b-corretivo-da-op-2-o-agente-nomeia-a-recusa-do-impedimento-im.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T3-o-loop-leva-toda-parada-ao-consultor.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T3a-corretivo-da-op-3-a-parada-e-a-mesma-em-todas-as-regras-que.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T3b-corretivo-da-op-3-com-estrategico-o-loop-para-sem-executar-a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T3c-corretivo-da-op-3-com-estrategico-a-rota-planejador-executa.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T3d-corretivo-da-op-3-o-loop-redespacha-sem-retentativa-o-card-c.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T4-a-forma-efemera-com-cenario-persistido.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T4a-corretivo-da-op-4-a-queda-de-uma-instancia-do-consultor-nao.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T5-o-outro-lado-da-fronteira-nas-definicoes-de-conduta.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T5a-corretivo-da-op-5-o-diario-e-a-regra-8-dizem-o-que-a-triagem.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T6-a-especificacao-vira-lastro-medido.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T6a-corretivo-da-op-6-a-spec-nao-prevalece-sobre-o-bloco-a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T7-a-medida-do-piloto-da-forma-efemera.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T7a-corretivo-da-op-7-o-veredito-declara-o-modelo-das-instancias.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T8-a-porta-de-entrada-e-a-descricao-do-agente.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0747-CON-T8a-corretivo-da-op-8-a-description-volta-ao-yaml-que-o-harness.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0748-TLG-T1-a-sonda-de-viabilidade-diante-do-dono.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0748-TLG-T2-o-repertorio-de-mensagens-na-skill-do-loop.md` — atribuição: alheio; estado git: `??`
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
- `docs/RDO/evidencia/P-0747-CON-T2b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T3.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T3a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T3b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T3c.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T3d.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T4.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T4a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T5.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T5a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T6.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T6a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T7.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T7a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T8.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0747-CON-T8a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0748-TLG-T1.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0748-TLG-T2.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-54-TK-54b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-76-TK-76a.md` — atribuição: alheio; estado git: `??`
- `docs/RESIDENCIA_DOUTRINA.md` — atribuição: alheio; estado git: ` M`
- `docs/consultant-spec.md` — atribuição: alheio; estado git: ` M`
- `docs/planner-spec.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0745-planejador-modelo-operacao.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0746-lastro-do-modelo.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0747-consultor-de-plano.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0748-tela-do-gerente.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CAMPANHA-P-0748.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-P-0747.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-P-0748.md` — atribuição: alheio; estado git: `??`
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
- Arquivos-alvo declarados: `.claude/skills/scrum-master/SKILL.md`, `.claude/skills/modelo-por-fase/SKILL.md`, `GOVERNANCA.md`, `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, `README.md`, `.claude/README.md`
- Arquivos tocados: `.claude/README.md`, `.claude/agents/pantonic-consultant.md`, `.claude/agents/pantonic-executor.md`, `.claude/agents/pantonic-fora-da-caixa.md`, `.claude/agents/pantonic-model-designer.md`, `.claude/agents/pantonic-planner.md`, `.claude/agents/pantonic-reviewer.md`, `.claude/global/CLAUDE.md`, `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, `.claude/skills/bootstrap-pantonic/SKILL.md`, `.claude/skills/diario-de-obras/SKILL.md`, `.claude/skills/modelo-por-fase/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/modelo.py`, `GOVERNANCA.md`, `README.md`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/DIARIO_HISTORICO.md`, `docs/DOC_MAP.md`, `docs/OPERACOES_AS_IS.md`, `docs/OPERACOES_AS_IS_P-0745.md`, `docs/OPERACOES_AS_IS_P-0747.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-76a-as-tabelas-do-modelo-em-frases-curtas-para-o-dono.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0745-PLN-T4a-o-ponteiro-sobrevivente-da-tabela-aposentada-nos-fatos-estav.md`, `docs/RDO/P-0745-PLN-T5-o-modelador-diante-do-plano-sem-cards-e-o-lastro-que-e-do-pl.md`, `docs/RDO/P-0745-PLN-T5a-a-frase-que-governa-o-gate-do-modelador-e-a-enumeracao-que-e.md`, `docs/RDO/P-0745-PLN-T6-a-especificacao-do-agente-de-planejamento.md`, `docs/RDO/P-0745-PLN-T7-o-indice-de-documentos-e-a-revisao-do-readme.md`, `docs/RDO/P-0745-PLN-T7a-o-readme-deixa-de-defender-a-regua-que-ele-mesmo-aposenta.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/P-0747-CON-T1-o-consultor-entra-na-doutrina-de-governanca.md`, `docs/RDO/P-0747-CON-T2-a-definicao-de-conduta-do-consultor-sem-estatuto-provisorio.md`, `docs/RDO/P-0747-CON-T2a-corretivo-da-op-2-o-agente-descreve-o-cenario-persistido-e-l.md`, `docs/RDO/P-0747-CON-T2b-corretivo-da-op-2-o-agente-nomeia-a-recusa-do-impedimento-im.md`, `docs/RDO/P-0747-CON-T3-o-loop-leva-toda-parada-ao-consultor.md`, `docs/RDO/P-0747-CON-T3a-corretivo-da-op-3-a-parada-e-a-mesma-em-todas-as-regras-que.md`, `docs/RDO/P-0747-CON-T3b-corretivo-da-op-3-com-estrategico-o-loop-para-sem-executar-a.md`, `docs/RDO/P-0747-CON-T3c-corretivo-da-op-3-com-estrategico-a-rota-planejador-executa.md`, `docs/RDO/P-0747-CON-T3d-corretivo-da-op-3-o-loop-redespacha-sem-retentativa-o-card-c.md`, `docs/RDO/P-0747-CON-T4-a-forma-efemera-com-cenario-persistido.md`, `docs/RDO/P-0747-CON-T4a-corretivo-da-op-4-a-queda-de-uma-instancia-do-consultor-nao.md`, `docs/RDO/P-0747-CON-T5-o-outro-lado-da-fronteira-nas-definicoes-de-conduta.md`, `docs/RDO/P-0747-CON-T5a-corretivo-da-op-5-o-diario-e-a-regra-8-dizem-o-que-a-triagem.md`, `docs/RDO/P-0747-CON-T6-a-especificacao-vira-lastro-medido.md`, `docs/RDO/P-0747-CON-T6a-corretivo-da-op-6-a-spec-nao-prevalece-sobre-o-bloco-a.md`, `docs/RDO/P-0747-CON-T7-a-medida-do-piloto-da-forma-efemera.md`, `docs/RDO/P-0747-CON-T7a-corretivo-da-op-7-o-veredito-declara-o-modelo-das-instancias.md`, `docs/RDO/P-0747-CON-T8-a-porta-de-entrada-e-a-descricao-do-agente.md`, `docs/RDO/P-0747-CON-T8a-corretivo-da-op-8-a-description-volta-ao-yaml-que-o-harness.md`, `docs/RDO/P-0748-TLG-T1-a-sonda-de-viabilidade-diante-do-dono.md`, `docs/RDO/P-0748-TLG-T2-o-repertorio-de-mensagens-na-skill-do-loop.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0745-PLN-T4a.md`, `docs/RDO/evidencia/P-0745-PLN-T5.md`, `docs/RDO/evidencia/P-0745-PLN-T5a.md`, `docs/RDO/evidencia/P-0745-PLN-T6.md`, `docs/RDO/evidencia/P-0745-PLN-T7.md`, `docs/RDO/evidencia/P-0745-PLN-T7a.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/P-0747-CON-T1.md`, `docs/RDO/evidencia/P-0747-CON-T2.md`, `docs/RDO/evidencia/P-0747-CON-T2a.md`, `docs/RDO/evidencia/P-0747-CON-T2b.md`, `docs/RDO/evidencia/P-0747-CON-T3.md`, `docs/RDO/evidencia/P-0747-CON-T3a.md`, `docs/RDO/evidencia/P-0747-CON-T3b.md`, `docs/RDO/evidencia/P-0747-CON-T3c.md`, `docs/RDO/evidencia/P-0747-CON-T3d.md`, `docs/RDO/evidencia/P-0747-CON-T4.md`, `docs/RDO/evidencia/P-0747-CON-T4a.md`, `docs/RDO/evidencia/P-0747-CON-T5.md`, `docs/RDO/evidencia/P-0747-CON-T5a.md`, `docs/RDO/evidencia/P-0747-CON-T6.md`, `docs/RDO/evidencia/P-0747-CON-T6a.md`, `docs/RDO/evidencia/P-0747-CON-T7.md`, `docs/RDO/evidencia/P-0747-CON-T7a.md`, `docs/RDO/evidencia/P-0747-CON-T8.md`, `docs/RDO/evidencia/P-0747-CON-T8a.md`, `docs/RDO/evidencia/P-0748-TLG-T1.md`, `docs/RDO/evidencia/P-0748-TLG-T2.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/RDO/evidencia/TK-76-TK-76a.md`, `docs/RESIDENCIA_DOUTRINA.md`, `docs/consultant-spec.md`, `docs/planner-spec.md`, `docs/plans/P-0745-planejador-modelo-operacao.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/P-0747-consultor-de-plano.md`, `docs/plans/P-0748-tela-do-gerente.md`, `docs/plans/_CAMPANHA-P-0748.md`, `docs/plans/_CENARIO-P-0747.md`, `docs/plans/_CENARIO-P-0748.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VEREDITO-procedimentos-2026-09-22.md`, `docs/telemetria.tsv`, `tests/fixtures/modelo/fluxo-concluido.md`, `tests/fixtures/modelo/fluxo-pendente.md`, `tests/fixtures/modelo/fluxo-valido.md`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/fixtures/modelo/plano-invalido.md`, `tests/fixtures/modelo/plano-sem-cabecalho.md`, `tests/fixtures/modelo/plano-sem-estado.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_doutrina_unidade.py`, `tests/test_modelo.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/agents/pantonic-model-designer.md` → `TK-76a`, `.claude/agents/pantonic-planner.md` → `TK-76a`, `docs/CUSTO_DO_PICKUP.md` → `TK-54b`, `docs/DIARIO_DE_OBRAS.md` → `TK-54b`, `docs/DOC_MAP.md` → `TK-54b`
- Registro da orquestração (não atribuível a tarefa): `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-76a-as-tabelas-do-modelo-em-frases-curtas-para-o-dono.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0745-PLN-T4a-o-ponteiro-sobrevivente-da-tabela-aposentada-nos-fatos-estav.md`, `docs/RDO/P-0745-PLN-T5-o-modelador-diante-do-plano-sem-cards-e-o-lastro-que-e-do-pl.md`, `docs/RDO/P-0745-PLN-T5a-a-frase-que-governa-o-gate-do-modelador-e-a-enumeracao-que-e.md`, `docs/RDO/P-0745-PLN-T6-a-especificacao-do-agente-de-planejamento.md`, `docs/RDO/P-0745-PLN-T7-o-indice-de-documentos-e-a-revisao-do-readme.md`, `docs/RDO/P-0745-PLN-T7a-o-readme-deixa-de-defender-a-regua-que-ele-mesmo-aposenta.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/P-0747-CON-T1-o-consultor-entra-na-doutrina-de-governanca.md`, `docs/RDO/P-0747-CON-T2-a-definicao-de-conduta-do-consultor-sem-estatuto-provisorio.md`, `docs/RDO/P-0747-CON-T2a-corretivo-da-op-2-o-agente-descreve-o-cenario-persistido-e-l.md`, `docs/RDO/P-0747-CON-T2b-corretivo-da-op-2-o-agente-nomeia-a-recusa-do-impedimento-im.md`, `docs/RDO/P-0747-CON-T3-o-loop-leva-toda-parada-ao-consultor.md`, `docs/RDO/P-0747-CON-T3a-corretivo-da-op-3-a-parada-e-a-mesma-em-todas-as-regras-que.md`, `docs/RDO/P-0747-CON-T3b-corretivo-da-op-3-com-estrategico-o-loop-para-sem-executar-a.md`, `docs/RDO/P-0747-CON-T3c-corretivo-da-op-3-com-estrategico-a-rota-planejador-executa.md`, `docs/RDO/P-0747-CON-T3d-corretivo-da-op-3-o-loop-redespacha-sem-retentativa-o-card-c.md`, `docs/RDO/P-0747-CON-T4-a-forma-efemera-com-cenario-persistido.md`, `docs/RDO/P-0747-CON-T4a-corretivo-da-op-4-a-queda-de-uma-instancia-do-consultor-nao.md`, `docs/RDO/P-0747-CON-T5-o-outro-lado-da-fronteira-nas-definicoes-de-conduta.md`, `docs/RDO/P-0747-CON-T5a-corretivo-da-op-5-o-diario-e-a-regra-8-dizem-o-que-a-triagem.md`, `docs/RDO/P-0747-CON-T6-a-especificacao-vira-lastro-medido.md`, `docs/RDO/P-0747-CON-T6a-corretivo-da-op-6-a-spec-nao-prevalece-sobre-o-bloco-a.md`, `docs/RDO/P-0747-CON-T7-a-medida-do-piloto-da-forma-efemera.md`, `docs/RDO/P-0747-CON-T7a-corretivo-da-op-7-o-veredito-declara-o-modelo-das-instancias.md`, `docs/RDO/P-0747-CON-T8-a-porta-de-entrada-e-a-descricao-do-agente.md`, `docs/RDO/P-0747-CON-T8a-corretivo-da-op-8-a-description-volta-ao-yaml-que-o-harness.md`, `docs/RDO/P-0748-TLG-T1-a-sonda-de-viabilidade-diante-do-dono.md`, `docs/RDO/P-0748-TLG-T2-o-repertorio-de-mensagens-na-skill-do-loop.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0745-PLN-T4a.md`, `docs/RDO/evidencia/P-0745-PLN-T5.md`, `docs/RDO/evidencia/P-0745-PLN-T5a.md`, `docs/RDO/evidencia/P-0745-PLN-T6.md`, `docs/RDO/evidencia/P-0745-PLN-T7.md`, `docs/RDO/evidencia/P-0745-PLN-T7a.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/P-0747-CON-T1.md`, `docs/RDO/evidencia/P-0747-CON-T2.md`, `docs/RDO/evidencia/P-0747-CON-T2a.md`, `docs/RDO/evidencia/P-0747-CON-T2b.md`, `docs/RDO/evidencia/P-0747-CON-T3.md`, `docs/RDO/evidencia/P-0747-CON-T3a.md`, `docs/RDO/evidencia/P-0747-CON-T3b.md`, `docs/RDO/evidencia/P-0747-CON-T3c.md`, `docs/RDO/evidencia/P-0747-CON-T3d.md`, `docs/RDO/evidencia/P-0747-CON-T4.md`, `docs/RDO/evidencia/P-0747-CON-T4a.md`, `docs/RDO/evidencia/P-0747-CON-T5.md`, `docs/RDO/evidencia/P-0747-CON-T5a.md`, `docs/RDO/evidencia/P-0747-CON-T6.md`, `docs/RDO/evidencia/P-0747-CON-T6a.md`, `docs/RDO/evidencia/P-0747-CON-T7.md`, `docs/RDO/evidencia/P-0747-CON-T7a.md`, `docs/RDO/evidencia/P-0747-CON-T8.md`, `docs/RDO/evidencia/P-0747-CON-T8a.md`, `docs/RDO/evidencia/P-0748-TLG-T1.md`, `docs/RDO/evidencia/P-0748-TLG-T2.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/RDO/evidencia/TK-76-TK-76a.md`, `docs/plans/P-0745-planejador-modelo-operacao.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/P-0747-consultor-de-plano.md`, `docs/plans/P-0748-tela-do-gerente.md`, `docs/plans/_CAMPANHA-P-0748.md`, `docs/plans/_CENARIO-P-0747.md`, `docs/plans/_CENARIO-P-0748.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VEREDITO-procedimentos-2026-09-22.md`, `docs/telemetria.tsv`
- Ato do dono, fora do ciclo de tarefa: `.claude/agents/pantonic-consultant.md`, `.claude/agents/pantonic-executor.md`, `.claude/agents/pantonic-fora-da-caixa.md`, `.claude/agents/pantonic-reviewer.md`
- Fato: 25 arquivo(s) fora dos alvos e sem atribuição: `.claude/global/CLAUDE.md`, `.claude/skills/bootstrap-pantonic/SKILL.md`, `.claude/skills/diario-de-obras/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/tools/modelo.py`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/DIARIO_HISTORICO.md`, `docs/OPERACOES_AS_IS.md`, `docs/OPERACOES_AS_IS_P-0745.md`, `docs/OPERACOES_AS_IS_P-0747.md`, `docs/RESIDENCIA_DOUTRINA.md`, `docs/consultant-spec.md`, `docs/planner-spec.md`, `tests/fixtures/modelo/fluxo-concluido.md`, `tests/fixtures/modelo/fluxo-pendente.md`, `tests/fixtures/modelo/fluxo-valido.md`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/fixtures/modelo/plano-invalido.md`, `tests/fixtures/modelo/plano-sem-cabecalho.md`, `tests/fixtures/modelo/plano-sem-estado.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_doutrina_unidade.py`, `tests/test_modelo.py`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/skills/scrum-master/SKILL.md`
```
diff --git a/.claude/skills/scrum-master/SKILL.md b/.claude/skills/scrum-master/SKILL.md
index 8cd7d64..68ad155 100644
--- a/.claude/skills/scrum-master/SKILL.md
+++ b/.claude/skills/scrum-master/SKILL.md
@@ -24,7 +24,7 @@ Três contadores, e só três.
 Além deles: **plano corrente**, **tarefa corrente** e **fila corrente** (ordem do plano,
 **reordenada em execução** por `A3a`). Nada mais entra. Fonte normativa:
 `docs/plans/P-0734-execucao-autonoma.md` `### DP-B` (retentativa/precedência do bloco A);
-`GOVERNANCA.md` §4.3 e `### DP-Q` (encerramento); `### DP-G` item 3 (reordenação da fila).
+`GOVERNANCA.md` §4.3 e `### DP-Q` (encerramento); `### DP-G` item 3 (reordenação da fila); `docs/plans/P-0747-consultor-de-plano.md` `DCS-3`..`DCS-6` (triagem de toda parada pelo consultor e rota devolvida).
 
 ## Fluxo
 
@@ -35,8 +35,13 @@ Dez passos, nesta ordem.
 - **Gatilho:** invocação da skill, antes de qualquer despacho.
 - **Entrada:** modelo ativo do contexto principal.
 - **Ação:** rodar `.claude/skills/modelo-por-fase/SKILL.md` (fase **orquestração**, matriz
-  `GOVERNANCA.md` §3). Modelo diferente do exigido: **PARA e pede `/model` ao dono**.
-- **Saída:** modelo conferido, ou parada com o `/model` pedido.
+  `GOVERNANCA.md` §3). Modelo ativo **acima** do exigido: **segue** nele — o contexto principal
+  só orquestra, e o modelo de cada tarefa viaja no despacho (passo 4) — e anota a divergência em
+  uma linha do relatório de encerramento. O loop nunca para para rebaixar o modelo. Modelo ativo
+  **abaixo** do exigido: **PARA e pede ao dono o `/model` do modelo melhor** — a única parada do
+  gate.
+- **Saída:** modelo conferido, com a divergência anotada quando houver, ou parada com o `/model`
+  do modelo melhor pedido.
 
 ### Passo 2 — Seleção da próxima tarefa do plano
 
@@ -151,6 +156,7 @@ Dez passos, nesta ordem.
 - **Entrada:** `status`, `veredito`, `bloqueante`, `recomendação`, contador de retentativas.
 - **Ação:** aplicar a tabela do bloco A **em ordem de precedência** — a primeira regra que casa
   vence.
+- **Triagem:** toda regra que escala ao consultor (`A3a`, `A3b`, `A3c`, `A6a`, `A7`, `B1` e o gate do modelo do passo 9) recebe de volta a linha `rota=<resolve|modelador|planejador>` — e, quando o consultor classificar o impedimento como estratégico, a linha `estrategico=<uma frase>` logo abaixo dela — e despacha por ela: `estrategico=` presente — **PARA** em qualquer rota, e nas rotas `resolve` e `modelador` **sem executar a ação da rota**: o reparo que o consultor já gravou fica no plano, o modelador **não** é despachado, e a frase, a rota e o dossiê de emenda, se houver, vão ao relatório de encerramento, para o dono decidir antes de qualquer ato sobre o modelo (`G-NOASK`; `P-0747` `DCS-28`); com `rota=planejador` a ação da rota já é a parada e se executa como está — o plano materializado `blocked`, a rodada de replanejamento enfileirada — e a frase vai junto ao relatório; `rota=resolve` sem `estrategico=` — o reparo já está gravado no plano, e a janela segue; quando o reparo é a recusa do impedimento como improcedente (`P-0747` `DCS-35`), a mesma tarefa volta a `ready` com ao menos uma linha nova gravada pelo consultor e é redespachada **sem** consumir retentativa; `rota=modelador` — despacha o `pantonic-model-designer` com o dossiê `Ato de modelo` de `emenda` que o consultor devolveu, sem parar a janela: a versão pendente coexiste com a vigente até o marco, onde o pedido de validar ou recusar o drift sobe ao dono (`GOVERNANCA.md` §3.2), e com a recusa o caso volta ao consultor para resolver preservando o modelo; `rota=planejador` — materializa o plano como `blocked`, e a rodada de replanejamento vira a próxima tarefa do plano (`G-REPLAN`, `GOVERNANCA.md` §7 item 17): **PARA**.
 - **Saída:** "segue" (vai ao passo 9) ou "PARA" (vai ao relatório de encerramento). Se a
   linha de retorno do reviewer trouxer um dossiê `Ato de modelo`, despache o
   `pantonic-model-designer` com esse dossiê **antes** de seguir ao pa
```
[truncado em 4000 caracteres]

### `.claude/skills/modelo-por-fase/SKILL.md`
```
diff --git a/.claude/skills/modelo-por-fase/SKILL.md b/.claude/skills/modelo-por-fase/SKILL.md
index 32df1d0..e070b57 100644
--- a/.claude/skills/modelo-por-fase/SKILL.md
+++ b/.claude/skills/modelo-por-fase/SKILL.md
@@ -1,6 +1,6 @@
 ---
 name: modelo-por-fase
-description: Gatilho operacional da regra "modelo por fase" (GOVERNANCA.md §3) — classifica a fase do trabalho (intelectual/execução/varredura), confere o modelo ativo contra a tabela vinculante e para para pedir o /model correto ao dono. Usar no início de qualquer tarefa/subagente, ao trocar de fase no meio de uma sessão, ou quando o hook global de nudge (UserPromptSubmit) disparar o aviso.
+description: Gatilho operacional da regra "modelo por fase" (GOVERNANCA.md §3) — classifica a fase do trabalho (intelectual/execução/varredura), confere o modelo ativo contra a tabela vinculante; acima do exigido segue e anota a divergência, e só abaixo do exigido para para pedir o /model melhor ao dono. Usar no início de qualquer tarefa/subagente, ao trocar de fase no meio de uma sessão, ou quando o hook global de nudge (UserPromptSubmit) disparar o aviso.
 ---
 
 # modelo-por-fase — gatilho operacional do modelo por fase
@@ -21,7 +21,7 @@ si.
 | Fase | Modelo | Sinal típico |
 |---|---|---|
 | Intelectual (planejar/arquitetar/auditar/decidir/especificar) | Opus (Fable só sob pedido explícito do dono) | PRD, arquitetura, spec, decomposição, auditoria, parecer |
-| Execução (implementar/editar/testar/corrigir) | Sonnet | Uma tarefa atômica do diário de obras, TDD |
+| Execução (implementar/editar/testar/corrigir) | Sonnet | Um card do diário de obras — a materialização de uma operação do modelo —, TDD |
 | Varredura (search/grep/leitura ampla) | Haiku (ou subagente de coleta) | Levantar contexto antes de planejar/executar |
 
 ## Os três gatilhos
@@ -32,20 +32,26 @@ si.
    implementar. Repita o gate; não herde o modelo da fase anterior por inércia.
 3. **Nudge do hook global** — quando `modelo_por_fase_userpromptsubmit.py` emitir o aviso
    (`systemMessage` + `additionalContext`), esta skill é o procedimento que traduz o aviso em
-   ação (passo "Gate de parada" abaixo). O hook é heurística de palavra-chave sobre o prompt do
+   ação (passo "Gate de subida" abaixo). O hook é heurística de palavra-chave sobre o prompt do
    dono; esta skill cobre também os casos que o hook não vê (ex.: subagente sem hook rodando,
    troca de fase decidida pelo próprio agente sem novo prompt do dono).
 
-## Gate de parada
+## Gate de subida
 
-Se o modelo ativo **não bate** com a fase:
+Se o modelo ativo **não bate** com a fase (ordem: Haiku < Sonnet < Opus):
 
-- **Pare** — não prossiga a fase com o modelo errado (não decida sozinho, não assuma que "dessa
-  vez tanto faz").
-- **Peça** ao dono, de forma explícita, o comando `/model <opus|sonnet|haiku>` correspondente.
+- **Acima do indicado** (ex.: Opus numa fase de Sonnet): **não pare** e não peça `/model` ao
+  dono — siga no modelo ativo. O contexto principal só orquestra: o modelo de cada tarefa
+  delegada viaja no despacho (`model` do cabeçalho do card), e rebaixar a tela principal nunca
+  justifica interromper o trabalho. **Anote** a divergência em uma linha, no fim da resposta —
+  uma vez por fase, não a cada turno; no loop de execução a nota vai ao relatório de
+  encerramento (`scrum-master`, passo 1).
+- **Abaixo do indicado** (ex.: Sonnet numa fase de Opus): **pare** e peça ao dono, de forma
+  explícita, o `/model <opus|sonnet>` do modelo melhor — a única parada do gate. Não prossiga a
+  fase com o modelo mais fraco nem assuma que "dessa vez tanto faz".
 - Só o dono decide inverter a tabela para um agente de **execução** (custo caro em execução
-  exige OK explícito e registrado — `GOVERNANCA.md` §3, penúltimo bullet). Para as demais fases
-  não há inversão silenciosa possível: preferência genérica de memória não decide isso.
+  exige OK explícito e registrado — `GOVERNANCA.md` §3, penúltimo bullet); a inversão se
+  materializ
```
[truncado em 4000 caracteres]

### `GOVERNANCA.md`
```
diff --git a/GOVERNANCA.md b/GOVERNANCA.md
index 8d1e39a..c8f4744 100644
--- a/GOVERNANCA.md
+++ b/GOVERNANCA.md
@@ -75,9 +75,9 @@ de regressão, contexto limpo e validação por sprint (§4.5) existem por isso
 processo, não inspeções do resultado. A **rota** vem em segundo: decidida no planejamento e mantida
 fiel na execução (§7 itens 9 e 12), porque processo bom com rota errada entrega, com esmero, o
 produto errado. O **custo** é o terceiro: **restrição de projeto**, não razão de ser. Modelo por
-fase, orçamento de turnos e economia de contexto tornam a qualidade **sustentável** — nunca a
-compram mais barata. Quando os três colidem, a ordem decide: nenhuma economia justifica abrir mão
-de um guardrail, e nenhuma rota se muda para caber no orçamento.
+fase, dimensionamento pela operação do modelo e economia de contexto tornam a qualidade
+**sustentável** — nunca a compram mais barata. Quando os três colidem, a ordem decide: nenhuma
+economia justifica abrir mão de um guardrail, e nenhuma rota se muda para caber no custo.
 
 **Matriz de responsabilidades — lugar canônico.** Quem responde pelo quê num projeto Pantonic* é
 declarado **aqui e só aqui**; qualquer outra seção deste documento, agente ou skill **aponta** para
@@ -88,9 +88,10 @@ adequado ao seu custo — a coluna *Modelo* é a tabela vinculante do **modelo p
 | Papel | Modelo | Responde por | Não faz |
 |---|---|---|---|
 | **Dono / gerente** | humano | Última instância e **fonte da doutrina de produto**: decide o quê e o porquê, ratifica decisões (`DR-`/`DP-`), valida cada sprint (§4.5), aceita release, autoriza saída do piso de regressão (§4.4) e comando destrutivo (§7 item 13) | Não desempata, no meio de uma execução, o que o plano deveria ter decidido — a pergunta que chega até ele em execução é sintoma de plano não-pronto (§7 itens 11 e 12) |
-| **Planejamento** | O mais poderoso disponível (Opus; Fable só sob solicitação explícita do dono) | PRD, arquitetura, specs, decisões de rota e decomposição em checklists de **tarefas atômicas fechadas** (G-PLANREADY, §7 item 11), cada uma com objetivo, arquivos-alvo, verificação e critério de pronto; **o dimensionamento de cada tarefa** sob a *Diretriz de dimensionamento de tarefa* desta seção — coesão, autossuficiência em contexto e ocupação estimada, exercidas no recorte, não publicadas no card; **a revisão de plano, com exclusividade** — indício de que o plano precisa mudar chega aqui e só aqui, e o planejador decide por si o que for **técnico ou tático**, escalando ao dono o que for **estratégico ou alterar escopo**; **a revisão do README ao encerrar cada sprint** — tarefa nomeada do próprio plano, com o guarda executável como instrumento e o veredito do dono como aceite (G-README dever 2, §7 item 14); sprint planejada sem essa tarefa é plano incompleto; **o risco de interrupção de cada card** — plano em que um executor frio pararia por dúvida sem contingência fechada não se libera (G-NOASK, §7 item 18); **o dossiê de ato de modelo** (§3.2): o planejador não escreve a seção do modelo — devolve o dossiê de autoria junto com o plano gravado, e o de emenda em rodada de replanejamento | Não executa: não implementa, não fecha tarefa, não transforma dúvida própria em pergunta ao executor |
-| **Orquestração** | Melhor custo-benefício (Sonnet); o loop roda no contexto principal, onde o dono interrompe sem derrubar a sessão, e **para para pedir `/model`** quando a fase exige outro modelo | Conduzir um plano do começo ao fim: despachar cada tarefa ao papel competente com o dossiê fechado, rotear a linha de retorno do executor e o laudo do `reviewer` (aprovado segue, reprovado volta ao mesmo escopo, escalado sobe ao dono), registrar a telemetria medida e arquivar o resultado; roda `modelo.py check` antes de despachar e antes de fechar cada tarefa, abre o relatório e cada marco com `modelo.py show` e **despacha o modelador** ao receber um dossiê de ato de modelo (§3.2) | Não implementa, não julga a entrega — o veredito é da revisão
```
[truncado em 4000 caracteres]

### `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`
```
diff --git a/.claude/global/hooks/modelo_por_fase_userpromptsubmit.py b/.claude/global/hooks/modelo_por_fase_userpromptsubmit.py
index 82a8713..48c285a 100644
--- a/.claude/global/hooks/modelo_por_fase_userpromptsubmit.py
+++ b/.claude/global/hooks/modelo_por_fase_userpromptsubmit.py
@@ -83,9 +83,11 @@ _NUDGE = {
     "execution": (
         "\U0001F7E1 Fase de execucao (implementar/editar/testar) — Sonnet basta. "
         "Rodar em Opus e desperdicio (Regra 7): considere `/model sonnet`.",
-        "Gate modelo-por-fase: este prompt e execucao mecanica (Regra 7). Se o modelo "
-        "ativo for Opus, recomende ao dono `/model sonnet` antes de implementar "
-        "(anuncie — Regra 5), salvo tarefa de alto risco com racional registrado.",
+        "Nota modelo-por-fase: este prompt e execucao mecanica (Regra 7); o modelo "
+        "indicado e Sonnet. Se o ativo for Opus, NAO pare e NAO peca `/model` ao dono "
+        "(rebaixar a tela principal nunca interrompe o trabalho): siga e anote a "
+        "divergencia em uma linha no fim da resposta. So pare para pedir "
+        "`/model sonnet` se o ativo for Haiku.",
     ),
     "reading": (
         "\U0001F7E1 Fase de leitura/varredura — Haiku basta, ou delegue ao "

```

### `README.md`
```
diff --git a/README.md b/README.md
index 4cf033f..b65ea8a 100644
--- a/README.md
+++ b/README.md
@@ -91,8 +91,9 @@ a leitura de quem adota (`G-README`, §10).
 - **Diário de obras** — `docs/DIARIO_DE_OBRAS.md`, o kanban central e a única fonte de verdade de
   status do projeto: diretiva, índice, uma seção por sprint ou tíquete e as notas de execução. Onde
   a regra mora: `.claude/skills/diario-de-obras/SKILL.md` (§7 desta página).
-- **Tarefa atômica** — a unidade de execução, definida por uma propriedade: executável por um agente
-  que não conhece o projeto, em contexto limpo, sem busca transversal. Onde
+- **Card** — a unidade de execução: a materialização de **uma operação do modelo** do plano,
+  executável por um agente que não conhece o projeto, em contexto limpo, sem busca transversal —
+  uma operação inteira, coesa e autossuficiente em contexto, sem percentual e sem teto. Onde
   a regra mora: `GOVERNANCA.md` §4.1 (§5 desta página).
 - **Passagem de bastão** — o procedimento fixo que fecha uma tarefa e abre a seguinte: gate verde,
   registro no RDO e no diário, achados fora de escopo, decisões e a herança de contexto para a
@@ -117,10 +118,11 @@ a leitura de quem adota (`G-README`, §10).
   reexecução se faz em contexto limpo. **Capacidade** é outra coisa: não é condição de execução e
   **nunca interrompe tarefa em curso** — dimensiona a tarefa *antes* de ela ser delegada. Onde a
   regra mora: `GOVERNANCA.md` §4.3 (coesão) e §3 (capacidade, §3 desta página).
-- **Orçamento de turnos** — o número de chamadas de ferramenta atribuído a uma tarefa **antes** da
-  delegação, escolhido pela classe do trabalho e calibrado pela série medida. É **referência de
-  dimensionamento de quem planeja**, nunca porteiro: cruzá-lo é alarme, não bloqueio, e quem executa
-  não se ocupa dele. Onde a regra mora: `GOVERNANCA.md` §3 (§3 desta página).
+- **Classe do card** — `mecanica|implementacao|comportamental|investigacao|redacao`: declara a
+  **natureza** do trabalho e calibra a profundidade de quem executa. **Não carrega teto**:
+  nenhum número de turnos ou de ocupação dimensiona uma tarefa — a unidade é a operação do
+  modelo que o card materializa. O consumo segue medido em `docs/telemetria.tsv` e se lê **na
+  série**, nunca como aceite. Onde a regra mora: `GOVERNANCA.md` §3 (§3 desta página).
 
 ### Metadados — como o próprio framework é distribuído
 
@@ -205,9 +207,9 @@ guardrail é uma coisa que **falha** sozinha, no instante em que a regra é viol
 segundo: quem decide arquitetura é o planejamento, no modelo caro e com o contexto de quem decidiu,
 porque processo bom com rota errada entrega, com esmero, o produto errado. **Custo** é o terceiro, e
 é **restrição de projeto**: um agente cobra por turno, reenviando o contexto inteiro a cada um, e o
-orçamento de turnos, o modelo por fase e a disciplina de coleta existem para tornar a qualidade
+dimensionamento pela operação do modelo, o modelo por fase e a disciplina de coleta existem para tornar a qualidade
 **sustentável** (§3). Quando os três colidem, a ordem decide:
-nenhuma economia justifica abrir mão de um guardrail, e nenhuma rota se muda para caber no orçamento.
+nenhuma economia justifica abrir mão de um guardrail, e nenhuma rota se muda para caber no custo.
 
 O que ele deliberadamente deixa de fora também é parte do desenho. Ele não governa produto —
 prioridade de negócio, escopo funcional e a decisão de fazer ou não fazer continuam sendo do dono. E
@@ -302,39 +304,20 @@ turnos. Ele protege o contexto do orquestrador, o que é valioso, e o consumo to
 mesmo. Tarefa pequena, abaixo de uns quinze turnos estimados, sai mais barata
 executada inline do que delegada.
 
-**Orçamento de turnos por classe de tarefa.** Cada tarefa atômica recebe um número de referência
-**antes** de ser delegada, escolhido pela classe do trabalho. Ele dimensiona e alimenta a série
-medida; não recusa entrega, não roteia e não encerra tarefa nem janela. A tabela é a **única**
-residência d
```
[truncado em 4000 caracteres]

### `.claude/README.md`
```
diff --git a/.claude/README.md b/.claude/README.md
index 86c08f0..c134651 100644
--- a/.claude/README.md
+++ b/.claude/README.md
@@ -13,11 +13,11 @@ blocos de "fatos estáveis" dos agentes. Fundamentos: `GOVERNANCA.md` e
 | `pantonic-auditor-arch` | Opus | Auditor de clean architecture e DDD Pantonic*. Invocado pelo usuário para ler a codebase e criar um checklist de desvios de clean architecture e DDD com ações de recuperação da qualidade arquitetural. Não altera código. |
 | `pantonic-auditor-cleancode` | Sonnet | Auditor de clean code Pantonic*. Invocado pelo usuário para inspecionar a codebase e identificar code smells — principalmente desvios de coesão e acoplamento — produzindo checklist de apontamentos com ações de correção. Não altera código. |
 | `pantonic-benchmarker` | Haiku | Agente coletor de benchmarking Pantonic* (somente leitura + escrita do próprio relatório, modelo barato). Usar para produzir, a partir de UM repositório público confirmado, um relatório de benchmarking no esquema fixo de 16 dimensões (D1..D16), sem juízo sobre o PantonicApp. |
-| `pantonic-consultant` | Opus | Consultor de plano Pantonic*, instanciado UMA vez por execução de plano e mantido de standby com o cenário inteiro no contexto. Acionado a cada escalonamento para desbloquear impedimento de executor e reparar o plano, devolvendo ao loop o dossiê Ato de modelo quando a decisão exigir emenda do modelo de domínio - quem escreve no modelo é o pantonic-model-designer. Figura ad-hoc, provisória, criada por decisão do dono em 2026-09-18. |
+| `pantonic-consultant` | Opus | Consultor de plano Pantonic*, papel de doutrina (GOVERNANCA.md §3, linha Consultoria). Ponto de triagem de toda parada de executor e de todo laudo com pendência substantiva - devolve ao loop a rota resolve, modelador ou planejador, fecha sozinho o técnico e o tático, inclusive o card corretivo da mesma operação, e devolve o dossiê Ato de modelo de emenda quando há drift do modelo - quem escreve no modelo é o pantonic-model-designer. Efêmero - cada acionamento é uma instância nova que lê o cenário persistido do plano. |
 | `pantonic-executor` | Sonnet | Agente de execução Pantonic*. Usar para implementar UM MÓDULO COESO do diário de obras por contexto — a disciplina inteira de um tema, não um fragmento —, com TDD (teste funcional + regressão) e guardrails de clean architecture. Não avalia, não decide, não trata ambiguidade — card que exija qualquer um dos três é devolvido como defeituoso. Não replaneja escopo e nunca busca a próxima tarefa. |
 | `pantonic-fora-da-caixa` | Opus | Agente fora-da-caixa Pantonic*. Invocado pelo usuário para varrer a codebase, identificar procedimentos que ficaram complexos por acúmulo de correções e extensões, e propor redesenhos "como se recomeçasse do zero hoje" — mais simples, robustos e diretos. Não altera código. |
 | `pantonic-model-designer` | Opus | Modelador de domínio de plano Pantonic*. Dono único de todo ato sobre a seção Modelo conceitual de um plano - escreve na autoria, emenda quando uma decisão muda o que o plano entrega, resolve conflito entre o texto e a entrega e explica o contexto do modelo. Não planeja, não executa, não julga entrega e não escreve nenhuma outra linha do plano. |
-| `pantonic-planner` | Opus | Agente de planejamento Pantonic*. Usar para produzir PRD, Architecture, Spec e Sprint Plan, e para decompor qualquer procedimento complexo em checklists de tarefas atômicas fechadas, autossuficientes para um executor frio. Não implementa código, não sonda codebase por conta própria e não publica plano com questão aberta. |
+| `pantonic-planner` | Opus | Agente de planejamento Pantonic*. Usar para produzir PRD, Architecture, Spec e Sprint Plan, e para decompor o modelo de domínio de um plano em cards fechados — um por operação do modelo, autossuficientes para um executor frio. Grava o esqueleto do plano, devolve o dossiê de autoria do modelo e só decompõe depois de a seção do modelo existir. Não implementa código, não sonda
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
