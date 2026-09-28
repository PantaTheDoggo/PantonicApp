# Evidência de revisão — DIARIO_DE_OBRAS TK-85a

## Diff (`git diff --stat`)
```
.claude/README.md                                  |    8 +-
 .claude/agents/pantonic-consultant.md              |   49 +-
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
 .claude/skills/passagem-de-bastao/SKILL.md         |   54 +-
 .claude/skills/redacao-doc/SKILL.md                |    3 +-
 .claude/skills/scrum-master/SKILL.md               |  223 +-
 .claude/tools/backlog.py                           |  584 ++-
 .claude/tools/backlog_hook.py                      |   14 +-
 .claude/tools/card_check.py                        |  403 ++-
 .claude/tools/modelo.py                            |   39 +-
 .claude/tools/rdo.py                               |  322 +-
 .claude/tools/rdo_template.md                      |   12 +-
 .claude/tools/review_evidence.py                   |  170 +-
 .claude/tools/telemetria.py                        |   56 +-
 .claude/tools/telemetria_hook.py                   |   15 +-
 GOVERNANCA.md                                      |  413 ++-
 README.md                                          |  196 +-
 docs/CUSTO_DO_PICKUP.md                            |  171 +
 docs/DIARIO_DE_OBRAS.md                            | 3774 +++++++++++++++++++-
 docs/DIARIO_HISTORICO.md                           |  154 +
 docs/DOC_MAP.md                                    |  115 +-
 docs/RDO/INDEX.md                                  |  133 +
 docs/RESIDENCIA_DOUTRINA.md                        |    4 +-
 docs/RUBRICA_DE_REVISAO.md                         |   27 +-
 docs/consultant-spec.md                            |   75 +-
 docs/plans/P-0741-modelo-conceitual.md             |    8 +-
 docs/plans/P-0742-loop-fora-do-llm.md              |  976 ++++-
 docs/plans/P-0745-planejador-modelo-operacao.md    | 1584 +++++++-
 docs/plans/_INBOX.md                               |    3 +-
 docs/plans/_INBOX_HISTORICO.md                     |    9 +
 docs/telemetria.tsv                                |  406 +++
 .../backlog/vermelho/docs/DIARIO_DE_OBRAS.md       |    3 +
 tests/fixtures/modelo/fluxo-concluido.md           |   12 +-
 tests/fixtures/modelo/fluxo-pendente.md            |   20 +-
 tests/fixtures/modelo/fluxo-valido.md              |   12 +-
 tests/fixtures/modelo/plano-invalido-2.md          |   10 +-
 tests/fixtures/modelo/plano-invalido.md            |   12 +-
 tests/fixtures/modelo/plano-sem-cabecalho.md       |    8 +-
 tests/fixtures/modelo/plano-sem-estado.md          |    8 +-
 tests/test_backlog.py                              |  819 +++++
 tests/test_card_check.py                           |  208 ++
 tests/test_materializar.py                         |    2 +-
 tests/test_modelo.py                               |  143 +-
 tests/test_rdo.py                                  |  411 ++-
 tests/test_review_evidence.py                      |  286 +-
 tests/test_telemetria.py                           |   50 +
 tests/test_telemetria_hook.py                      |   35 +
 59 files changed, 11447 insertions(+), 1274 deletions(-)
```

## Arquivos tocados
- `.claude/README.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-consultant.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-executor.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-fora-da-caixa.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-model-designer.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-planner.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-reviewer.md` — atribuição: da entrega; estado git: ` M`
- `.claude/checks/frontmatter_yaml.py` — atribuição: alheio; estado git: `??`
- `.claude/checks/kit_check.ps1` — atribuição: alheio; estado git: ` M`
- `.claude/global/CLAUDE.md` — atribuição: alheio; estado git: ` M`
- `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` — atribuição: alheio; estado git: ` M`
- `.claude/projecoes.json` — atribuição: alheio; estado git: ` M`
- `.claude/skills/bootstrap-pantonic/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/diario-de-obras/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/entrega-de-encerramento/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/fatos-frescos/SKILL.md` — atribuição: alheio; estado git: `??`
- `.claude/skills/mensagem-ao-dono/SKILL.md` — atribuição: alheio; estado git: `??`
- `.claude/skills/modelo-por-fase/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/passagem-de-bastao/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/redacao-doc/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/scrum-master/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/tools/backlog.py` — atribuição: alheio; estado git: ` M`
- `.claude/tools/backlog_hook.py` — atribuição: alheio; estado git: ` M`
- `.claude/tools/caminhos.py` — atribuição: alheio; estado git: `??`
- `.claude/tools/card_check.py` — atribuição: alheio; estado git: ` M`
- `.claude/tools/crenca_hook.py` — atribuição: alheio; estado git: `??`
- `.claude/tools/encerrar.py` — atribuição: alheio; estado git: `??`
- `.claude/tools/modelo.py` — atribuição: alheio; estado git: ` M`
- `.claude/tools/progresso_hook.py` — atribuição: alheio; estado git: `??`
- `.claude/tools/rdo.py` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/rdo_template.md` — atribuição: alheio; estado git: ` M`
- `.claude/tools/review_evidence.py` — atribuição: alheio; estado git: ` M`
- `.claude/tools/telemetria.py` — atribuição: alheio; estado git: ` M`
- `.claude/tools/telemetria_hook.py` — atribuição: alheio; estado git: ` M`
- `GOVERNANCA.md` — atribuição: alheio; estado git: ` M`
- `README.md` — atribuição: alheio; estado git: ` M`
- `docs/ACIONAMENTOS_CONSULTOR.tsv` — atribuição: alheio; estado git: `??`
- `docs/ARMADILHAS_DE_FERRAMENTA.md` — atribuição: alheio; estado git: `??`
- `docs/CUSTO_DO_PICKUP.md` — atribuição: alheio; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/DIARIO_HISTORICO.md` — atribuição: alheio; estado git: ` M`
- `docs/DOC_MAP.md` — atribuição: alheio; estado git: ` M`
- `docs/FALHAS_COMUNICACAO.tsv` — atribuição: alheio; estado git: `??`
- `docs/OPERACOES_AS_IS.md` — atribuição: alheio; estado git: `??`
- `docs/OPERACOES_AS_IS_P-0745.md` — atribuição: alheio; estado git: `??`
- `docs/OPERACOES_AS_IS_P-0746.md` — atribuição: alheio; estado git: `??`
- `docs/OPERACOES_AS_IS_P-0747.md` — atribuição: alheio; estado git: `??`
- `docs/OPERACOES_AS_IS_P-0748.md` — atribuição: alheio; estado git: `??`
- `docs/OPERACOES_AS_IS_P-0749.md` — atribuição: alheio; estado git: `??`
- `docs/OPERACOES_AS_IS_P-0750.md` — atribuição: alheio; estado git: `??`
- `docs/OPERACOES_AS_IS_P-0751.md` — atribuição: alheio; estado git: `??`
- `docs/PISO_C11.tsv` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-65a-check-recusa-id-de-depende-de-que-nao-e-item.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-65b-o-ponto-de-carga-escreve-em-utf-8-antes-de-argparse-abrir-a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-65c-o-verbo-diretiva-nao-descarta-id-em-silencio.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-65d-os-dois-depende-de-do-diario-voltam-a-gramatica.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-65e-o-ramo-concatenado-do-aviso-de-diretiva-ganha-teste.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-66a-o-atribuidor-so-casa-tarefa-ja-despachada.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-68a-os-controles-1-1-e-1-2-da-regra-1-entram-na-copia-canonica-d.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-74a-o-alvo-diretorio-de-outra-tarefa-casa-por-prefixo.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-74b-modelo-py-recusa-limpo-o-alvo-que-nao-e-arquivo-de-plano.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-76a-as-tabelas-do-modelo-em-frases-curtas-para-o-dono.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-77a-o-validate-recusa-frontmatter-de-agente-ou-skill-que-o-yaml.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-78a-o-loop-nao-para-para-rebaixar-o-modelo.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-78b-a-regua-do-card-aprende-as-tres-licoes-da-janela.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-78c-a-evidencia-mede-so-o-que-mudou-desde-o-despacho.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-78d-a-doutrina-e-o-readme-deixam-de-mandar-parar-para-rebaixar-o.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-79a-a-prosa-depois-da-linha-de-retorno-e-descartada-por-regra-na.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-82a-rdo-py-escreve-em-utf-8-antes-de-argparse-abrir-a-boca.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-84a-com-desde-o-nao-rastreado-anterior-ao-ref-sai-dos-tocados.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-86a-o-piso-do-c-11-vem-de-docs-piso-c11-tsv-do-repositorio-checa.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-87a-o-item-do-backlog-py-termina-no-cabecalho-de-nivel-1-ou-2-se.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-88a-o-fechamento-de-tarefa-e-de-plano-e-um-comando-cada-com-rdo.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-88b-a-tarefa-sem-medida-fecha-declarando-a-ausencia-e-a-rodada-d.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-88c-o-painel-le-cada-argumento-da-propria-invocacao-e-o-rdo-publ.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-88d-o-fechamento-pergunta-ao-rdo-py-e-ao-backlog-py-se-pode-escr.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-89a-o-leitor-de-alvos-da-evidencia-corta-o-literal-da-ancora-ant.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-89b-a-doutrina-do-gate-do-card-conta-oito-itens-cita-o-card-chec.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-90a-o-p-0742-entra-no-indice-do-diario-como-blocked.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-90b-a-rodada-de-replanejamento-rp-1-do-p-0742-os-oito-cards-pass.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-91a-o-bullet-emenda-do-modelador-diz-o-que-fazer-no-marco.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/INDEX.md` — atribuição: alheio; estado git: ` M`
- `docs/RDO/P-0741-MC-T5-o-readme-explica-o-modelo-a-afericao-sobre-o-proprio-plano-e.md` — atribuição: alheio; estado git: `??`
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
- `docs/RDO/P-0748-TLG-T2a-o-repertorio-deixa-de-citar-o-comando-que-nao-vai-existir.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0748-TLG-T2b-o-repertorio-como-tabela-de-eventos-a-skill-diz-o-que-a-func.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0748-TLG-T3-o-gancho-que-grava-o-arquivo-de-progresso.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0748-TLG-T3a-a-captura-do-payload-dos-ganchos-o-que-a-funcao-vai-ler.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0748-TLG-T3b-a-funcao-que-gera-a-linha-do-stream-a-cada-evento-do-loop.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0748-TLG-T3c-o-painel-nao-perde-linha-e-nao-afirma-o-que-nao-aconteceu.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0748-TLG-T3d-o-painel-so-diz-que-a-janela-encerrou-quando-ela-encerrou.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0748-TLG-T3e-o-painel-diz-so-o-que-o-gancho-ve-o-modelo-mostrado-e-o-cons.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0748-TLG-T3f-o-estado-do-gancho-nao-guarda-chave-que-ninguem-le.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0748-TLG-T3g-o-painel-reconhece-o-retorno-do-agente-com-o-ou-o-colchete-a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0748-TLG-T3h-o-painel-da-uma-linha-a-cada-status-do-mesmo-comando-e-a-ski.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0748-TLG-T4-o-condutor-narra-uma-linha-do-repertorio-antes-de-cada-ato-n.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0748-TLG-T4a-a-skill-deixa-de-narrar-a-transicao-chega-ao-painel-pela-fun.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0748-TLG-T5-a-porta-de-entrada-diz-como-o-dono-acompanha-a-execucao-no-p.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0748-TLG-T5a-a-celula-da-scrum-master-na-tabela-de-skills-volta-a-dizer-q.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0749-SAN-T1-o-id-e-o-caminho-do-plano-num-lugar-so.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0749-SAN-T2-o-estado-sai-do-texto-e-vai-para-o-estado-tsv.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0749-SAN-T2a-projeto-novo-com-contador-em-p-0-e-nenhum-plano-passa-no-che.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0749-SAN-T3-relato-laudo-e-evidencia-nascem-na-pasta-do-plano.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0749-SAN-T3a-a-flag-vence-tambem-no-indice-e-a-cli-anuncia-os-dois-destin.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0749-SAN-T4-a-doutrina-ensina-a-pasta-o-estado-tsv-e-a-contagem-em-zero.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0749-SAN-T5-a-regra-do-artefato-de-humano-minimo-uma-vez-so.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0749-SAN-T6-a-porta-de-entrada-descreve-a-pasta-a-tabela-e-o-texto-minim.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0749-SAN-T6a-o-glossario-diz-o-contador-como-a-regra-o-diz.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0749-SAN-T6b-as-decisoes-estruturantes-dizem-o-contador-como-a-regra-o-di.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0750-CAH-T1-a-regra-da-mensagem-legivel-ao-dono-na-doutrina-e-no-regulam.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0750-CAH-T2-o-glossario-diz-o-que-cada-familia-de-sigla-nomeia.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0750-CAH-T3-a-tabela-de-falhas-de-comunicacao-com-as-falhas-ja-medidas.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0750-CAH-T4-a-skill-da-mensagem-ao-dono.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0750-CAH-T4a-o-titulo-de-tarefa-na-skill-da-mensagem-ao-dono-para-antes-d.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0750-CAH-T5-os-textos-que-mandavam-citar-sigla-ao-dono-passam-a-mandar-o.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0751-EBK-T1-o-check-acusa-tiquete-vivo-sem-card.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0751-EBK-T10-a-regua-de-autoria-do-card-segunda-leva.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0751-EBK-T11-o-planejador-publica-o-grep-da-superficie-e-ensaia-os-cards.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0751-EBK-T12-tres-ajustes-de-regra-existente-a-devolucao-do-modelador-o-e.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0751-EBK-T13-quanto-custa-retomar-o-planejador-por-mensagem.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0751-EBK-T13a-a-razao-da-regra-da-retomada-sai-do-custo-de-partida-nao-da.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0751-EBK-T14-a-rodada-de-revisao-de-guardrails-pendente-desde-2026-08-08.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0751-EBK-T2-o-check-confronta-o-card-com-o-rdo-py-e-o-piso-com-o-corpus.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0751-EBK-T3-o-next-projeta-o-colchete-do-cabecalho-inteiro.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0751-EBK-T4-rdo-py-close-recusa-tarefa-que-nao-esta-done.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0751-EBK-T5-o-kit-check-conta-defeito-nao-linha.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0751-EBK-T5a-o-kit-check-nao-conta-o-sumario-do-materializar-e-detalha-so.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0751-EBK-T6-nenhuma-fixture-carrega-nome-que-o-harness-descobre.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0751-EBK-T7-a-doutrina-do-teste-que-discrimina-e-da-medida-publicada.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0751-EBK-T8-a-vigencia-do-modelo-o-desfecho-do-drift-recusado-e-o-lastro.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0751-EBK-T9-uma-operacao-uma-oracao.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T1-o-gate-do-card-le-a-forma-do-corpus-e-deixa-de-produzir-item.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T10-a-tabela-de-acionamentos-ganha-a-coluna-de-causa-raiz.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T1a-um-teste-tranca-o-marcador-de-item-so-no-inicio-de-linha-com.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T2-o-gate-do-card-roda-no-ensaio-do-planejador-e-no-despacho-do.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T3-toda-ancora-de-arquivo-e-linha-do-card-leva-o-literal-e-o-ga.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T4-o-aviso-de-crenca-no-ato-de-gravar-plano-ou-diario.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T4a-o-aviso-de-crenca-conta-uma-vez-o-literal-que-casa-dois-padr.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T5-o-executor-devolve-a-medida-como-arquivo-e-a-evidencia-a-inc.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T5a-o-executor-o-revisor-e-o-loop-falam-do-arquivo-de-medida.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T5b-a-medida-guarda-a-cauda-da-saida-onde-esta-o-sumario.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T5c-a-medida-do-executor-mora-onde-o-revisor-a-procura-tambem-no.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T6-o-dossie-de-despacho-carrega-os-achados-roteados-ao-card.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T7-o-escritor-da-telemetria-recusa-a-linha-repetida-da-mesma-ro.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T8-as-armadilhas-de-ferramenta-medidas-ganham-um-arquivo-so.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T8a-a-regua-de-autoria-do-card-aponta-as-armadilhas-de-ferrament.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T9-a-skill-de-fatos-frescos.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T9a-a-skill-de-fatos-frescos-le-os-totais-em-instrumento-de-leit.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-68a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-84a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-86a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-87a-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-87a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88b-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88c-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88c.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88d-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88d.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-89a-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-89a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-89b-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-89b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-90a-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-90a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-90b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-91a-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-91a.md` — atribuição: alheio; estado git: `??`
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
- `docs/RDO/evidencia/P-0748-TLG-T2a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0748-TLG-T2b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0748-TLG-T3.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0748-TLG-T3a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0748-TLG-T3b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0748-TLG-T3c.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0748-TLG-T3d.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0748-TLG-T3e.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0748-TLG-T3f.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0748-TLG-T3g.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0748-TLG-T3h.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0748-TLG-T4.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0748-TLG-T4a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0748-TLG-T5.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0748-TLG-T5a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0749-SAN-T1.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0749-SAN-T2.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0749-SAN-T2a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0749-SAN-T3.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0749-SAN-T3a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0749-SAN-T4.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0749-SAN-T5.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0749-SAN-T6.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0749-SAN-T6a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0749-SAN-T6b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0750-CAH-T1.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0750-CAH-T2.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0750-CAH-T3.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0750-CAH-T4.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0750-CAH-T4a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0750-CAH-T5.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0751-EBK-T1.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0751-EBK-T10.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0751-EBK-T11.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0751-EBK-T12.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0751-EBK-T13.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0751-EBK-T13a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0751-EBK-T14.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0751-EBK-T2.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0751-EBK-T3.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0751-EBK-T4.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0751-EBK-T5.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0751-EBK-T5a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0751-EBK-T6.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0751-EBK-T7.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0751-EBK-T8.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0751-EBK-T9.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0751-TK-86a-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T1.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T10-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T10.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T1a-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T1a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T2.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T3.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T4-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T4.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T4a-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T4a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T5.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T5a-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T5a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T5b-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T5b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T5c-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T5c.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T6-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T6.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T7-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T7.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T8-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T8.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T8a-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T8a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T9-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T9.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T9a-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T9a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-54-TK-54b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-65-TK-65a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-65-TK-65b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-65-TK-65c.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-65-TK-65d.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-65-TK-65e.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-66-TK-66a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-74-TK-74a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-74-TK-74b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-76-TK-76a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-77-TK-77a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-78-TK-78a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-78-TK-78b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-78-TK-78c.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-78-TK-78d.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-79-TK-79a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-82-TK-82a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-84a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-86a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-87a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-88a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-88b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-88c.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-88d.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-89a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-89b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-90a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-90b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-91a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T1.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T10.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T1a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T2.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T3.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T4.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T4a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T5.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T5a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T5b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T5c.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T6.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T7.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T8.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T8a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T9.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T9a.md` — atribuição: alheio; estado git: `??`
- `docs/RESIDENCIA_DOUTRINA.md` — atribuição: alheio; estado git: ` M`
- `docs/RUBRICA_DE_REVISAO.md` — atribuição: alheio; estado git: ` M`
- `docs/consultant-spec.md` — atribuição: alheio; estado git: ` M`
- `docs/planner-spec.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0741-modelo-conceitual.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0742-loop-fora-do-llm.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0745-planejador-modelo-operacao.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0746-lastro-do-modelo.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0747-consultor-de-plano.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0748-tela-do-gerente.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0749-saneamento-artefatos.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0750-comunicacao-agente-humano.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0751-esgotar-backlog.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0752-fato-no-ponto-de-uso.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CAMPANHA-P-0748.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-P-0747.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-P-0748.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-P-0749.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-P-0750.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-P-0751.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-P-0752.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-TK-65.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-TK-78.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-TK-86.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-TK-88.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-TK-89.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_ENTREGA-P-0751.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_INBOX.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/_INBOX_HISTORICO.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/_VEREDITO-procedimentos-2026-09-22.md` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/backlog/pasta/docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/estado.tsv` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/plano.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/pasta/docs/plans/_INBOX.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/vermelho/docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/card_check/alvo.txt` — atribuição: alheio; estado git: `??`
- `tests/fixtures/card_check/plano-ancoras.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/card_check/plano-corpus.md` — atribuição: alheio; estado git: `??`
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
- `tests/test_backlog.py` — atribuição: alheio; estado git: ` M`
- `tests/test_caminhos.py` — atribuição: alheio; estado git: `??`
- `tests/test_card_check.py` — atribuição: alheio; estado git: ` M`
- `tests/test_crenca_hook.py` — atribuição: alheio; estado git: `??`
- `tests/test_doutrina_unidade.py` — atribuição: alheio; estado git: `??`
- `tests/test_encerrar.py` — atribuição: alheio; estado git: `??`
- `tests/test_fixtures_higiene.py` — atribuição: alheio; estado git: `??`
- `tests/test_frontmatter_yaml.py` — atribuição: alheio; estado git: `??`
- `tests/test_global_claude.py` — atribuição: alheio; estado git: `??`
- `tests/test_kit_check.py` — atribuição: alheio; estado git: `??`
- `tests/test_materializar.py` — atribuição: alheio; estado git: ` M`
- `tests/test_modelo.py` — atribuição: alheio; estado git: ` M`
- `tests/test_progresso_hook.py` — atribuição: alheio; estado git: `??`
- `tests/test_rdo.py` — atribuição: da entrega; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: alheio; estado git: ` M`
- `tests/test_telemetria.py` — atribuição: alheio; estado git: ` M`
- `tests/test_telemetria_hook.py` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: árvore de trabalho inteira (nenhum `--desde` informado)
- Arquivos-alvo declarados: `.claude/tools/rdo.py`, `tests/test_rdo.py`, `.claude/agents/pantonic-reviewer.md`
- Arquivos tocados: `.claude/README.md`, `.claude/agents/pantonic-consultant.md`, `.claude/agents/pantonic-executor.md`, `.claude/agents/pantonic-fora-da-caixa.md`, `.claude/agents/pantonic-model-designer.md`, `.claude/agents/pantonic-planner.md`, `.claude/agents/pantonic-reviewer.md`, `.claude/checks/frontmatter_yaml.py`, `.claude/checks/kit_check.ps1`, `.claude/global/CLAUDE.md`, `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, `.claude/projecoes.json`, `.claude/skills/bootstrap-pantonic/SKILL.md`, `.claude/skills/diario-de-obras/SKILL.md`, `.claude/skills/entrega-de-encerramento/SKILL.md`, `.claude/skills/fatos-frescos/SKILL.md`, `.claude/skills/mensagem-ao-dono/SKILL.md`, `.claude/skills/modelo-por-fase/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/redacao-doc/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/backlog.py`, `.claude/tools/backlog_hook.py`, `.claude/tools/caminhos.py`, `.claude/tools/card_check.py`, `.claude/tools/crenca_hook.py`, `.claude/tools/encerrar.py`, `.claude/tools/modelo.py`, `.claude/tools/progresso_hook.py`, `.claude/tools/rdo.py`, `.claude/tools/rdo_template.md`, `.claude/tools/review_evidence.py`, `.claude/tools/telemetria.py`, `.claude/tools/telemetria_hook.py`, `GOVERNANCA.md`, `README.md`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/ARMADILHAS_DE_FERRAMENTA.md`, `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/DIARIO_HISTORICO.md`, `docs/DOC_MAP.md`, `docs/FALHAS_COMUNICACAO.tsv`, `docs/OPERACOES_AS_IS.md`, `docs/OPERACOES_AS_IS_P-0745.md`, `docs/OPERACOES_AS_IS_P-0746.md`, `docs/OPERACOES_AS_IS_P-0747.md`, `docs/OPERACOES_AS_IS_P-0748.md`, `docs/OPERACOES_AS_IS_P-0749.md`, `docs/OPERACOES_AS_IS_P-0750.md`, `docs/OPERACOES_AS_IS_P-0751.md`, `docs/PISO_C11.tsv`, `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65a-check-recusa-id-de-depende-de-que-nao-e-item.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65b-o-ponto-de-carga-escreve-em-utf-8-antes-de-argparse-abrir-a.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65c-o-verbo-diretiva-nao-descarta-id-em-silencio.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65d-os-dois-depende-de-do-diario-voltam-a-gramatica.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65e-o-ramo-concatenado-do-aviso-de-diretiva-ganha-teste.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-66a-o-atribuidor-so-casa-tarefa-ja-despachada.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-68a-os-controles-1-1-e-1-2-da-regra-1-entram-na-copia-canonica-d.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-74a-o-alvo-diretorio-de-outra-tarefa-casa-por-prefixo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-74b-modelo-py-recusa-limpo-o-alvo-que-nao-e-arquivo-de-plano.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-76a-as-tabelas-do-modelo-em-frases-curtas-para-o-dono.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-77a-o-validate-recusa-frontmatter-de-agente-ou-skill-que-o-yaml.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78a-o-loop-nao-para-para-rebaixar-o-modelo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78b-a-regua-do-card-aprende-as-tres-licoes-da-janela.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78c-a-evidencia-mede-so-o-que-mudou-desde-o-despacho.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78d-a-doutrina-e-o-readme-deixam-de-mandar-parar-para-rebaixar-o.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-79a-a-prosa-depois-da-linha-de-retorno-e-descartada-por-regra-na.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-82a-rdo-py-escreve-em-utf-8-antes-de-argparse-abrir-a-boca.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-84a-com-desde-o-nao-rastreado-anterior-ao-ref-sai-dos-tocados.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-86a-o-piso-do-c-11-vem-de-docs-piso-c11-tsv-do-repositorio-checa.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-87a-o-item-do-backlog-py-termina-no-cabecalho-de-nivel-1-ou-2-se.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-88a-o-fechamento-de-tarefa-e-de-plano-e-um-comando-cada-com-rdo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-88b-a-tarefa-sem-medida-fecha-declarando-a-ausencia-e-a-rodada-d.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-88c-o-painel-le-cada-argumento-da-propria-invocacao-e-o-rdo-publ.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-88d-o-fechamento-pergunta-ao-rdo-py-e-ao-backlog-py-se-pode-escr.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-89a-o-leitor-de-alvos-da-evidencia-corta-o-literal-da-ancora-ant.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-89b-a-doutrina-do-gate-do-card-conta-oito-itens-cita-o-card-chec.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-90a-o-p-0742-entra-no-indice-do-diario-como-blocked.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-90b-a-rodada-de-replanejamento-rp-1-do-p-0742-os-oito-cards-pass.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-91a-o-bullet-emenda-do-modelador-diz-o-que-fazer-no-marco.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0741-MC-T5-o-readme-explica-o-modelo-a-afericao-sobre-o-proprio-plano-e.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0745-PLN-T4a-o-ponteiro-sobrevivente-da-tabela-aposentada-nos-fatos-estav.md`, `docs/RDO/P-0745-PLN-T5-o-modelador-diante-do-plano-sem-cards-e-o-lastro-que-e-do-pl.md`, `docs/RDO/P-0745-PLN-T5a-a-frase-que-governa-o-gate-do-modelador-e-a-enumeracao-que-e.md`, `docs/RDO/P-0745-PLN-T6-a-especificacao-do-agente-de-planejamento.md`, `docs/RDO/P-0745-PLN-T7-o-indice-de-documentos-e-a-revisao-do-readme.md`, `docs/RDO/P-0745-PLN-T7a-o-readme-deixa-de-defender-a-regua-que-ele-mesmo-aposenta.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/P-0747-CON-T1-o-consultor-entra-na-doutrina-de-governanca.md`, `docs/RDO/P-0747-CON-T2-a-definicao-de-conduta-do-consultor-sem-estatuto-provisorio.md`, `docs/RDO/P-0747-CON-T2a-corretivo-da-op-2-o-agente-descreve-o-cenario-persistido-e-l.md`, `docs/RDO/P-0747-CON-T2b-corretivo-da-op-2-o-agente-nomeia-a-recusa-do-impedimento-im.md`, `docs/RDO/P-0747-CON-T3-o-loop-leva-toda-parada-ao-consultor.md`, `docs/RDO/P-0747-CON-T3a-corretivo-da-op-3-a-parada-e-a-mesma-em-todas-as-regras-que.md`, `docs/RDO/P-0747-CON-T3b-corretivo-da-op-3-com-estrategico-o-loop-para-sem-executar-a.md`, `docs/RDO/P-0747-CON-T3c-corretivo-da-op-3-com-estrategico-a-rota-planejador-executa.md`, `docs/RDO/P-0747-CON-T3d-corretivo-da-op-3-o-loop-redespacha-sem-retentativa-o-card-c.md`, `docs/RDO/P-0747-CON-T4-a-forma-efemera-com-cenario-persistido.md`, `docs/RDO/P-0747-CON-T4a-corretivo-da-op-4-a-queda-de-uma-instancia-do-consultor-nao.md`, `docs/RDO/P-0747-CON-T5-o-outro-lado-da-fronteira-nas-definicoes-de-conduta.md`, `docs/RDO/P-0747-CON-T5a-corretivo-da-op-5-o-diario-e-a-regra-8-dizem-o-que-a-triagem.md`, `docs/RDO/P-0747-CON-T6-a-especificacao-vira-lastro-medido.md`, `docs/RDO/P-0747-CON-T6a-corretivo-da-op-6-a-spec-nao-prevalece-sobre-o-bloco-a.md`, `docs/RDO/P-0747-CON-T7-a-medida-do-piloto-da-forma-efemera.md`, `docs/RDO/P-0747-CON-T7a-corretivo-da-op-7-o-veredito-declara-o-modelo-das-instancias.md`, `docs/RDO/P-0747-CON-T8-a-porta-de-entrada-e-a-descricao-do-agente.md`, `docs/RDO/P-0747-CON-T8a-corretivo-da-op-8-a-description-volta-ao-yaml-que-o-harness.md`, `docs/RDO/P-0748-TLG-T1-a-sonda-de-viabilidade-diante-do-dono.md`, `docs/RDO/P-0748-TLG-T2-o-repertorio-de-mensagens-na-skill-do-loop.md`, `docs/RDO/P-0748-TLG-T2a-o-repertorio-deixa-de-citar-o-comando-que-nao-vai-existir.md`, `docs/RDO/P-0748-TLG-T2b-o-repertorio-como-tabela-de-eventos-a-skill-diz-o-que-a-func.md`, `docs/RDO/P-0748-TLG-T3-o-gancho-que-grava-o-arquivo-de-progresso.md`, `docs/RDO/P-0748-TLG-T3a-a-captura-do-payload-dos-ganchos-o-que-a-funcao-vai-ler.md`, `docs/RDO/P-0748-TLG-T3b-a-funcao-que-gera-a-linha-do-stream-a-cada-evento-do-loop.md`, `docs/RDO/P-0748-TLG-T3c-o-painel-nao-perde-linha-e-nao-afirma-o-que-nao-aconteceu.md`, `docs/RDO/P-0748-TLG-T3d-o-painel-so-diz-que-a-janela-encerrou-quando-ela-encerrou.md`, `docs/RDO/P-0748-TLG-T3e-o-painel-diz-so-o-que-o-gancho-ve-o-modelo-mostrado-e-o-cons.md`, `docs/RDO/P-0748-TLG-T3f-o-estado-do-gancho-nao-guarda-chave-que-ninguem-le.md`, `docs/RDO/P-0748-TLG-T3g-o-painel-reconhece-o-retorno-do-agente-com-o-ou-o-colchete-a.md`, `docs/RDO/P-0748-TLG-T3h-o-painel-da-uma-linha-a-cada-status-do-mesmo-comando-e-a-ski.md`, `docs/RDO/P-0748-TLG-T4-o-condutor-narra-uma-linha-do-repertorio-antes-de-cada-ato-n.md`, `docs/RDO/P-0748-TLG-T4a-a-skill-deixa-de-narrar-a-transicao-chega-ao-painel-pela-fun.md`, `docs/RDO/P-0748-TLG-T5-a-porta-de-entrada-diz-como-o-dono-acompanha-a-execucao-no-p.md`, `docs/RDO/P-0748-TLG-T5a-a-celula-da-scrum-master-na-tabela-de-skills-volta-a-dizer-q.md`, `docs/RDO/P-0749-SAN-T1-o-id-e-o-caminho-do-plano-num-lugar-so.md`, `docs/RDO/P-0749-SAN-T2-o-estado-sai-do-texto-e-vai-para-o-estado-tsv.md`, `docs/RDO/P-0749-SAN-T2a-projeto-novo-com-contador-em-p-0-e-nenhum-plano-passa-no-che.md`, `docs/RDO/P-0749-SAN-T3-relato-laudo-e-evidencia-nascem-na-pasta-do-plano.md`, `docs/RDO/P-0749-SAN-T3a-a-flag-vence-tambem-no-indice-e-a-cli-anuncia-os-dois-destin.md`, `docs/RDO/P-0749-SAN-T4-a-doutrina-ensina-a-pasta-o-estado-tsv-e-a-contagem-em-zero.md`, `docs/RDO/P-0749-SAN-T5-a-regra-do-artefato-de-humano-minimo-uma-vez-so.md`, `docs/RDO/P-0749-SAN-T6-a-porta-de-entrada-descreve-a-pasta-a-tabela-e-o-texto-minim.md`, `docs/RDO/P-0749-SAN-T6a-o-glossario-diz-o-contador-como-a-regra-o-diz.md`, `docs/RDO/P-0749-SAN-T6b-as-decisoes-estruturantes-dizem-o-contador-como-a-regra-o-di.md`, `docs/RDO/P-0750-CAH-T1-a-regra-da-mensagem-legivel-ao-dono-na-doutrina-e-no-regulam.md`, `docs/RDO/P-0750-CAH-T2-o-glossario-diz-o-que-cada-familia-de-sigla-nomeia.md`, `docs/RDO/P-0750-CAH-T3-a-tabela-de-falhas-de-comunicacao-com-as-falhas-ja-medidas.md`, `docs/RDO/P-0750-CAH-T4-a-skill-da-mensagem-ao-dono.md`, `docs/RDO/P-0750-CAH-T4a-o-titulo-de-tarefa-na-skill-da-mensagem-ao-dono-para-antes-d.md`, `docs/RDO/P-0750-CAH-T5-os-textos-que-mandavam-citar-sigla-ao-dono-passam-a-mandar-o.md`, `docs/RDO/P-0751-EBK-T1-o-check-acusa-tiquete-vivo-sem-card.md`, `docs/RDO/P-0751-EBK-T10-a-regua-de-autoria-do-card-segunda-leva.md`, `docs/RDO/P-0751-EBK-T11-o-planejador-publica-o-grep-da-superficie-e-ensaia-os-cards.md`, `docs/RDO/P-0751-EBK-T12-tres-ajustes-de-regra-existente-a-devolucao-do-modelador-o-e.md`, `docs/RDO/P-0751-EBK-T13-quanto-custa-retomar-o-planejador-por-mensagem.md`, `docs/RDO/P-0751-EBK-T13a-a-razao-da-regra-da-retomada-sai-do-custo-de-partida-nao-da.md`, `docs/RDO/P-0751-EBK-T14-a-rodada-de-revisao-de-guardrails-pendente-desde-2026-08-08.md`, `docs/RDO/P-0751-EBK-T2-o-check-confronta-o-card-com-o-rdo-py-e-o-piso-com-o-corpus.md`, `docs/RDO/P-0751-EBK-T3-o-next-projeta-o-colchete-do-cabecalho-inteiro.md`, `docs/RDO/P-0751-EBK-T4-rdo-py-close-recusa-tarefa-que-nao-esta-done.md`, `docs/RDO/P-0751-EBK-T5-o-kit-check-conta-defeito-nao-linha.md`, `docs/RDO/P-0751-EBK-T5a-o-kit-check-nao-conta-o-sumario-do-materializar-e-detalha-so.md`, `docs/RDO/P-0751-EBK-T6-nenhuma-fixture-carrega-nome-que-o-harness-descobre.md`, `docs/RDO/P-0751-EBK-T7-a-doutrina-do-teste-que-discrimina-e-da-medida-publicada.md`, `docs/RDO/P-0751-EBK-T8-a-vigencia-do-modelo-o-desfecho-do-drift-recusado-e-o-lastro.md`, `docs/RDO/P-0751-EBK-T9-uma-operacao-uma-oracao.md`, `docs/RDO/P-0752-FPU-T1-o-gate-do-card-le-a-forma-do-corpus-e-deixa-de-produzir-item.md`, `docs/RDO/P-0752-FPU-T10-a-tabela-de-acionamentos-ganha-a-coluna-de-causa-raiz.md`, `docs/RDO/P-0752-FPU-T1a-um-teste-tranca-o-marcador-de-item-so-no-inicio-de-linha-com.md`, `docs/RDO/P-0752-FPU-T2-o-gate-do-card-roda-no-ensaio-do-planejador-e-no-despacho-do.md`, `docs/RDO/P-0752-FPU-T3-toda-ancora-de-arquivo-e-linha-do-card-leva-o-literal-e-o-ga.md`, `docs/RDO/P-0752-FPU-T4-o-aviso-de-crenca-no-ato-de-gravar-plano-ou-diario.md`, `docs/RDO/P-0752-FPU-T4a-o-aviso-de-crenca-conta-uma-vez-o-literal-que-casa-dois-padr.md`, `docs/RDO/P-0752-FPU-T5-o-executor-devolve-a-medida-como-arquivo-e-a-evidencia-a-inc.md`, `docs/RDO/P-0752-FPU-T5a-o-executor-o-revisor-e-o-loop-falam-do-arquivo-de-medida.md`, `docs/RDO/P-0752-FPU-T5b-a-medida-guarda-a-cauda-da-saida-onde-esta-o-sumario.md`, `docs/RDO/P-0752-FPU-T5c-a-medida-do-executor-mora-onde-o-revisor-a-procura-tambem-no.md`, `docs/RDO/P-0752-FPU-T6-o-dossie-de-despacho-carrega-os-achados-roteados-ao-card.md`, `docs/RDO/P-0752-FPU-T7-o-escritor-da-telemetria-recusa-a-linha-repetida-da-mesma-ro.md`, `docs/RDO/P-0752-FPU-T8-as-armadilhas-de-ferramenta-medidas-ganham-um-arquivo-so.md`, `docs/RDO/P-0752-FPU-T8a-a-regua-de-autoria-do-card-aponta-as-armadilhas-de-ferrament.md`, `docs/RDO/P-0752-FPU-T9-a-skill-de-fatos-frescos.md`, `docs/RDO/P-0752-FPU-T9a-a-skill-de-fatos-frescos-le-os-totais-em-instrumento-de-leit.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-68a.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-84a.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-86a.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-87a-medida.json`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-87a.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88a.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88b-medida.json`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88b.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88c-medida.json`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88c.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88d-medida.json`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88d.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-89a-medida.json`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-89a.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-89b-medida.json`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-89b.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-90a-medida.json`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-90a.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-90b.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-91a-medida.json`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-91a.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0745-PLN-T4a.md`, `docs/RDO/evidencia/P-0745-PLN-T5.md`, `docs/RDO/evidencia/P-0745-PLN-T5a.md`, `docs/RDO/evidencia/P-0745-PLN-T6.md`, `docs/RDO/evidencia/P-0745-PLN-T7.md`, `docs/RDO/evidencia/P-0745-PLN-T7a.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/P-0747-CON-T1.md`, `docs/RDO/evidencia/P-0747-CON-T2.md`, `docs/RDO/evidencia/P-0747-CON-T2a.md`, `docs/RDO/evidencia/P-0747-CON-T2b.md`, `docs/RDO/evidencia/P-0747-CON-T3.md`, `docs/RDO/evidencia/P-0747-CON-T3a.md`, `docs/RDO/evidencia/P-0747-CON-T3b.md`, `docs/RDO/evidencia/P-0747-CON-T3c.md`, `docs/RDO/evidencia/P-0747-CON-T3d.md`, `docs/RDO/evidencia/P-0747-CON-T4.md`, `docs/RDO/evidencia/P-0747-CON-T4a.md`, `docs/RDO/evidencia/P-0747-CON-T5.md`, `docs/RDO/evidencia/P-0747-CON-T5a.md`, `docs/RDO/evidencia/P-0747-CON-T6.md`, `docs/RDO/evidencia/P-0747-CON-T6a.md`, `docs/RDO/evidencia/P-0747-CON-T7.md`, `docs/RDO/evidencia/P-0747-CON-T7a.md`, `docs/RDO/evidencia/P-0747-CON-T8.md`, `docs/RDO/evidencia/P-0747-CON-T8a.md`, `docs/RDO/evidencia/P-0748-TLG-T1.md`, `docs/RDO/evidencia/P-0748-TLG-T2.md`, `docs/RDO/evidencia/P-0748-TLG-T2a.md`, `docs/RDO/evidencia/P-0748-TLG-T2b.md`, `docs/RDO/evidencia/P-0748-TLG-T3.md`, `docs/RDO/evidencia/P-0748-TLG-T3a.md`, `docs/RDO/evidencia/P-0748-TLG-T3b.md`, `docs/RDO/evidencia/P-0748-TLG-T3c.md`, `docs/RDO/evidencia/P-0748-TLG-T3d.md`, `docs/RDO/evidencia/P-0748-TLG-T3e.md`, `docs/RDO/evidencia/P-0748-TLG-T3f.md`, `docs/RDO/evidencia/P-0748-TLG-T3g.md`, `docs/RDO/evidencia/P-0748-TLG-T3h.md`, `docs/RDO/evidencia/P-0748-TLG-T4.md`, `docs/RDO/evidencia/P-0748-TLG-T4a.md`, `docs/RDO/evidencia/P-0748-TLG-T5.md`, `docs/RDO/evidencia/P-0748-TLG-T5a.md`, `docs/RDO/evidencia/P-0749-SAN-T1.md`, `docs/RDO/evidencia/P-0749-SAN-T2.md`, `docs/RDO/evidencia/P-0749-SAN-T2a.md`, `docs/RDO/evidencia/P-0749-SAN-T3.md`, `docs/RDO/evidencia/P-0749-SAN-T3a.md`, `docs/RDO/evidencia/P-0749-SAN-T4.md`, `docs/RDO/evidencia/P-0749-SAN-T5.md`, `docs/RDO/evidencia/P-0749-SAN-T6.md`, `docs/RDO/evidencia/P-0749-SAN-T6a.md`, `docs/RDO/evidencia/P-0749-SAN-T6b.md`, `docs/RDO/evidencia/P-0750-CAH-T1.md`, `docs/RDO/evidencia/P-0750-CAH-T2.md`, `docs/RDO/evidencia/P-0750-CAH-T3.md`, `docs/RDO/evidencia/P-0750-CAH-T4.md`, `docs/RDO/evidencia/P-0750-CAH-T4a.md`, `docs/RDO/evidencia/P-0750-CAH-T5.md`, `docs/RDO/evidencia/P-0751-EBK-T1.md`, `docs/RDO/evidencia/P-0751-EBK-T10.md`, `docs/RDO/evidencia/P-0751-EBK-T11.md`, `docs/RDO/evidencia/P-0751-EBK-T12.md`, `docs/RDO/evidencia/P-0751-EBK-T13.md`, `docs/RDO/evidencia/P-0751-EBK-T13a.md`, `docs/RDO/evidencia/P-0751-EBK-T14.md`, `docs/RDO/evidencia/P-0751-EBK-T2.md`, `docs/RDO/evidencia/P-0751-EBK-T3.md`, `docs/RDO/evidencia/P-0751-EBK-T4.md`, `docs/RDO/evidencia/P-0751-EBK-T5.md`, `docs/RDO/evidencia/P-0751-EBK-T5a.md`, `docs/RDO/evidencia/P-0751-EBK-T6.md`, `docs/RDO/evidencia/P-0751-EBK-T7.md`, `docs/RDO/evidencia/P-0751-EBK-T8.md`, `docs/RDO/evidencia/P-0751-EBK-T9.md`, `docs/RDO/evidencia/P-0751-TK-86a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T1.md`, `docs/RDO/evidencia/P-0752-FPU-T10-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T10.md`, `docs/RDO/evidencia/P-0752-FPU-T1a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T1a.md`, `docs/RDO/evidencia/P-0752-FPU-T2.md`, `docs/RDO/evidencia/P-0752-FPU-T3.md`, `docs/RDO/evidencia/P-0752-FPU-T4-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T4.md`, `docs/RDO/evidencia/P-0752-FPU-T4a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T4a.md`, `docs/RDO/evidencia/P-0752-FPU-T5.md`, `docs/RDO/evidencia/P-0752-FPU-T5a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T5a.md`, `docs/RDO/evidencia/P-0752-FPU-T5b-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T5b.md`, `docs/RDO/evidencia/P-0752-FPU-T5c-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T5c.md`, `docs/RDO/evidencia/P-0752-FPU-T6-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T6.md`, `docs/RDO/evidencia/P-0752-FPU-T7-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T7.md`, `docs/RDO/evidencia/P-0752-FPU-T8-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T8.md`, `docs/RDO/evidencia/P-0752-FPU-T8a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T8a.md`, `docs/RDO/evidencia/P-0752-FPU-T9-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T9.md`, `docs/RDO/evidencia/P-0752-FPU-T9a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T9a.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/RDO/evidencia/TK-65-TK-65a.md`, `docs/RDO/evidencia/TK-65-TK-65b.md`, `docs/RDO/evidencia/TK-65-TK-65c.md`, `docs/RDO/evidencia/TK-65-TK-65d.md`, `docs/RDO/evidencia/TK-65-TK-65e.md`, `docs/RDO/evidencia/TK-66-TK-66a.md`, `docs/RDO/evidencia/TK-74-TK-74a.md`, `docs/RDO/evidencia/TK-74-TK-74b.md`, `docs/RDO/evidencia/TK-76-TK-76a.md`, `docs/RDO/evidencia/TK-77-TK-77a.md`, `docs/RDO/evidencia/TK-78-TK-78a.md`, `docs/RDO/evidencia/TK-78-TK-78b.md`, `docs/RDO/evidencia/TK-78-TK-78c.md`, `docs/RDO/evidencia/TK-78-TK-78d.md`, `docs/RDO/evidencia/TK-79-TK-79a.md`, `docs/RDO/evidencia/TK-82-TK-82a.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-84a.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-86a.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-87a.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-88a.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-88b.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-88c.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-88d.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-89a.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-89b.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-90a.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-90b.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-91a.md`, `docs/RDO/laudos/P-0752-FPU-T1.md`, `docs/RDO/laudos/P-0752-FPU-T10.md`, `docs/RDO/laudos/P-0752-FPU-T1a.md`, `docs/RDO/laudos/P-0752-FPU-T2.md`, `docs/RDO/laudos/P-0752-FPU-T3.md`, `docs/RDO/laudos/P-0752-FPU-T4.md`, `docs/RDO/laudos/P-0752-FPU-T4a.md`, `docs/RDO/laudos/P-0752-FPU-T5.md`, `docs/RDO/laudos/P-0752-FPU-T5a.md`, `docs/RDO/laudos/P-0752-FPU-T5b.md`, `docs/RDO/laudos/P-0752-FPU-T5c.md`, `docs/RDO/laudos/P-0752-FPU-T6.md`, `docs/RDO/laudos/P-0752-FPU-T7.md`, `docs/RDO/laudos/P-0752-FPU-T8.md`, `docs/RDO/laudos/P-0752-FPU-T8a.md`, `docs/RDO/laudos/P-0752-FPU-T9.md`, `docs/RDO/laudos/P-0752-FPU-T9a.md`, `docs/RESIDENCIA_DOUTRINA.md`, `docs/RUBRICA_DE_REVISAO.md`, `docs/consultant-spec.md`, `docs/planner-spec.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0742-loop-fora-do-llm.md`, `docs/plans/P-0745-planejador-modelo-operacao.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/P-0747-consultor-de-plano.md`, `docs/plans/P-0748-tela-do-gerente.md`, `docs/plans/P-0749-saneamento-artefatos.md`, `docs/plans/P-0750-comunicacao-agente-humano.md`, `docs/plans/P-0751-esgotar-backlog.md`, `docs/plans/P-0752-fato-no-ponto-de-uso.md`, `docs/plans/_CAMPANHA-P-0748.md`, `docs/plans/_CENARIO-P-0747.md`, `docs/plans/_CENARIO-P-0748.md`, `docs/plans/_CENARIO-P-0749.md`, `docs/plans/_CENARIO-P-0750.md`, `docs/plans/_CENARIO-P-0751.md`, `docs/plans/_CENARIO-P-0752.md`, `docs/plans/_CENARIO-TK-65.md`, `docs/plans/_CENARIO-TK-78.md`, `docs/plans/_CENARIO-TK-86.md`, `docs/plans/_CENARIO-TK-88.md`, `docs/plans/_CENARIO-TK-89.md`, `docs/plans/_ENTREGA-P-0751.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VEREDITO-procedimentos-2026-09-22.md`, `docs/telemetria.tsv`, `tests/fixtures/backlog/pasta/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/estado.tsv`, `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/plano.md`, `tests/fixtures/backlog/pasta/docs/plans/_INBOX.md`, `tests/fixtures/backlog/vermelho/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/card_check/alvo.txt`, `tests/fixtures/card_check/plano-ancoras.md`, `tests/fixtures/card_check/plano-corpus.md`, `tests/fixtures/modelo/fluxo-concluido.md`, `tests/fixtures/modelo/fluxo-pendente.md`, `tests/fixtures/modelo/fluxo-valido.md`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/fixtures/modelo/plano-invalido.md`, `tests/fixtures/modelo/plano-sem-cabecalho.md`, `tests/fixtures/modelo/plano-sem-estado.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_backlog.py`, `tests/test_caminhos.py`, `tests/test_card_check.py`, `tests/test_crenca_hook.py`, `tests/test_doutrina_unidade.py`, `tests/test_encerrar.py`, `tests/test_fixtures_higiene.py`, `tests/test_frontmatter_yaml.py`, `tests/test_global_claude.py`, `tests/test_kit_check.py`, `tests/test_materializar.py`, `tests/test_modelo.py`, `tests/test_progresso_hook.py`, `tests/test_rdo.py`, `tests/test_review_evidence.py`, `tests/test_telemetria.py`, `tests/test_telemetria_hook.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/README.md` → `TK-64a`, `.claude/agents/pantonic-executor.md` → `TK-79a`, `.claude/agents/pantonic-model-designer.md` → `TK-76a`, `.claude/agents/pantonic-planner.md` → `TK-76a`, `.claude/checks/frontmatter_yaml.py` → `TK-77a`, `.claude/checks/kit_check.ps1` → `TK-77a`, `.claude/global/CLAUDE.md` → `TK-68a`, `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` → `TK-56a`, `.claude/skills/diario-de-obras/SKILL.md` → `TK-88a`, `.claude/skills/modelo-por-fase/SKILL.md` → `TK-78a`, `.claude/skills/passagem-de-bastao/SKILL.md` → `TK-88a`, `.claude/skills/scrum-master/SKILL.md` → `TK-78a`, `.claude/tools/backlog.py` → `TK-59a`, `.claude/tools/caminhos.py` → `TK-88a`, `.claude/tools/encerrar.py` → `TK-86a`, `.claude/tools/modelo.py` → `TK-74b`, `.claude/tools/progresso_hook.py` → `TK-88a`, `.claude/tools/rdo_template.md` → `TK-88a`, `.claude/tools/review_evidence.py` → `TK-66a`, `.claude/tools/telemetria_hook.py` → `TK-56a`, `GOVERNANCA.md` → `TK-76a`, `README.md` → `TK-51a`, `docs/CUSTO_DO_PICKUP.md` → `TK-54b`, `docs/DIARIO_DE_OBRAS.md` → `TK-54b`, `docs/DOC_MAP.md` → `TK-54b`, `docs/PISO_C11.tsv` → `TK-86a`, `docs/RUBRICA_DE_REVISAO.md` → `TK-89b`, `docs/plans/P-0742-loop-fora-do-llm.md` → `TK-90b`, `docs/plans/_INBOX.md` → `TK-90a`, `docs/plans/_INBOX_HISTORICO.md` → `TK-90a`, `docs/telemetria.tsv` → `TK-88b`, `tests/fixtures/backlog/pasta/docs/DIARIO_DE_OBRAS.md` → `TK-61a`, `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/estado.tsv` → `TK-61a`, `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/plano.md` → `TK-61a`, `tests/fixtures/backlog/pasta/docs/plans/_INBOX.md` → `TK-61a`, `tests/fixtures/backlog/vermelho/docs/DIARIO_DE_OBRAS.md` → `TK-61a`, `tests/test_backlog.py` → `TK-57a`, `tests/test_encerrar.py` → `TK-88a`, `tests/test_frontmatter_yaml.py` → `TK-77a`, `tests/test_global_claude.py` → `TK-68a`, `tests/test_materializar.py` → `TK-56a`, `tests/test_modelo.py` → `TK-74b`, `tests/test_progresso_hook.py` → `TK-88a`, `tests/test_review_evidence.py` → `TK-62a`, `tests/test_telemetria_hook.py` → `TK-56a`
- Registro da orquestração (não atribuível a tarefa): `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65a-check-recusa-id-de-depende-de-que-nao-e-item.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65b-o-ponto-de-carga-escreve-em-utf-8-antes-de-argparse-abrir-a.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65c-o-verbo-diretiva-nao-descarta-id-em-silencio.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65d-os-dois-depende-de-do-diario-voltam-a-gramatica.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65e-o-ramo-concatenado-do-aviso-de-diretiva-ganha-teste.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-66a-o-atribuidor-so-casa-tarefa-ja-despachada.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-68a-os-controles-1-1-e-1-2-da-regra-1-entram-na-copia-canonica-d.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-74a-o-alvo-diretorio-de-outra-tarefa-casa-por-prefixo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-74b-modelo-py-recusa-limpo-o-alvo-que-nao-e-arquivo-de-plano.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-76a-as-tabelas-do-modelo-em-frases-curtas-para-o-dono.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-77a-o-validate-recusa-frontmatter-de-agente-ou-skill-que-o-yaml.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78a-o-loop-nao-para-para-rebaixar-o-modelo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78b-a-regua-do-card-aprende-as-tres-licoes-da-janela.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78c-a-evidencia-mede-so-o-que-mudou-desde-o-despacho.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78d-a-doutrina-e-o-readme-deixam-de-mandar-parar-para-rebaixar-o.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-79a-a-prosa-depois-da-linha-de-retorno-e-descartada-por-regra-na.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-82a-rdo-py-escreve-em-utf-8-antes-de-argparse-abrir-a-boca.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-84a-com-desde-o-nao-rastreado-anterior-ao-ref-sai-dos-tocados.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-86a-o-piso-do-c-11-vem-de-docs-piso-c11-tsv-do-repositorio-checa.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-87a-o-item-do-backlog-py-termina-no-cabecalho-de-nivel-1-ou-2-se.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-88a-o-fechamento-de-tarefa-e-de-plano-e-um-comando-cada-com-rdo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-88b-a-tarefa-sem-medida-fecha-declarando-a-ausencia-e-a-rodada-d.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-88c-o-painel-le-cada-argumento-da-propria-invocacao-e-o-rdo-publ.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-88d-o-fechamento-pergunta-ao-rdo-py-e-ao-backlog-py-se-pode-escr.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-89a-o-leitor-de-alvos-da-evidencia-corta-o-literal-da-ancora-ant.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-89b-a-doutrina-do-gate-do-card-conta-oito-itens-cita-o-card-chec.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-90a-o-p-0742-entra-no-indice-do-diario-como-blocked.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-90b-a-rodada-de-replanejamento-rp-1-do-p-0742-os-oito-cards-pass.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-91a-o-bullet-emenda-do-modelador-diz-o-que-fazer-no-marco.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0741-MC-T5-o-readme-explica-o-modelo-a-afericao-sobre-o-proprio-plano-e.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0745-PLN-T4a-o-ponteiro-sobrevivente-da-tabela-aposentada-nos-fatos-estav.md`, `docs/RDO/P-0745-PLN-T5-o-modelador-diante-do-plano-sem-cards-e-o-lastro-que-e-do-pl.md`, `docs/RDO/P-0745-PLN-T5a-a-frase-que-governa-o-gate-do-modelador-e-a-enumeracao-que-e.md`, `docs/RDO/P-0745-PLN-T6-a-especificacao-do-agente-de-planejamento.md`, `docs/RDO/P-0745-PLN-T7-o-indice-de-documentos-e-a-revisao-do-readme.md`, `docs/RDO/P-0745-PLN-T7a-o-readme-deixa-de-defender-a-regua-que-ele-mesmo-aposenta.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/P-0747-CON-T1-o-consultor-entra-na-doutrina-de-governanca.md`, `docs/RDO/P-0747-CON-T2-a-definicao-de-conduta-do-consultor-sem-estatuto-provisorio.md`, `docs/RDO/P-0747-CON-T2a-corretivo-da-op-2-o-agente-descreve-o-cenario-persistido-e-l.md`, `docs/RDO/P-0747-CON-T2b-corretivo-da-op-2-o-agente-nomeia-a-recusa-do-impedimento-im.md`, `docs/RDO/P-0747-CON-T3-o-loop-leva-toda-parada-ao-consultor.md`, `docs/RDO/P-0747-CON-T3a-corretivo-da-op-3-a-parada-e-a-mesma-em-todas-as-regras-que.md`, `docs/RDO/P-0747-CON-T3b-corretivo-da-op-3-com-estrategico-o-loop-para-sem-executar-a.md`, `docs/RDO/P-0747-CON-T3c-corretivo-da-op-3-com-estrategico-a-rota-planejador-executa.md`, `docs/RDO/P-0747-CON-T3d-corretivo-da-op-3-o-loop-redespacha-sem-retentativa-o-card-c.md`, `docs/RDO/P-0747-CON-T4-a-forma-efemera-com-cenario-persistido.md`, `docs/RDO/P-0747-CON-T4a-corretivo-da-op-4-a-queda-de-uma-instancia-do-consultor-nao.md`, `docs/RDO/P-0747-CON-T5-o-outro-lado-da-fronteira-nas-definicoes-de-conduta.md`, `docs/RDO/P-0747-CON-T5a-corretivo-da-op-5-o-diario-e-a-regra-8-dizem-o-que-a-triagem.md`, `docs/RDO/P-0747-CON-T6-a-especificacao-vira-lastro-medido.md`, `docs/RDO/P-0747-CON-T6a-corretivo-da-op-6-a-spec-nao-prevalece-sobre-o-bloco-a.md`, `docs/RDO/P-0747-CON-T7-a-medida-do-piloto-da-forma-efemera.md`, `docs/RDO/P-0747-CON-T7a-corretivo-da-op-7-o-veredito-declara-o-modelo-das-instancias.md`, `docs/RDO/P-0747-CON-T8-a-porta-de-entrada-e-a-descricao-do-agente.md`, `docs/RDO/P-0747-CON-T8a-corretivo-da-op-8-a-description-volta-ao-yaml-que-o-harness.md`, `docs/RDO/P-0748-TLG-T1-a-sonda-de-viabilidade-diante-do-dono.md`, `docs/RDO/P-0748-TLG-T2-o-repertorio-de-mensagens-na-skill-do-loop.md`, `docs/RDO/P-0748-TLG-T2a-o-repertorio-deixa-de-citar-o-comando-que-nao-vai-existir.md`, `docs/RDO/P-0748-TLG-T2b-o-repertorio-como-tabela-de-eventos-a-skill-diz-o-que-a-func.md`, `docs/RDO/P-0748-TLG-T3-o-gancho-que-grava-o-arquivo-de-progresso.md`, `docs/RDO/P-0748-TLG-T3a-a-captura-do-payload-dos-ganchos-o-que-a-funcao-vai-ler.md`, `docs/RDO/P-0748-TLG-T3b-a-funcao-que-gera-a-linha-do-stream-a-cada-evento-do-loop.md`, `docs/RDO/P-0748-TLG-T3c-o-painel-nao-perde-linha-e-nao-afirma-o-que-nao-aconteceu.md`, `docs/RDO/P-0748-TLG-T3d-o-painel-so-diz-que-a-janela-encerrou-quando-ela-encerrou.md`, `docs/RDO/P-0748-TLG-T3e-o-painel-diz-so-o-que-o-gancho-ve-o-modelo-mostrado-e-o-cons.md`, `docs/RDO/P-0748-TLG-T3f-o-estado-do-gancho-nao-guarda-chave-que-ninguem-le.md`, `docs/RDO/P-0748-TLG-T3g-o-painel-reconhece-o-retorno-do-agente-com-o-ou-o-colchete-a.md`, `docs/RDO/P-0748-TLG-T3h-o-painel-da-uma-linha-a-cada-status-do-mesmo-comando-e-a-ski.md`, `docs/RDO/P-0748-TLG-T4-o-condutor-narra-uma-linha-do-repertorio-antes-de-cada-ato-n.md`, `docs/RDO/P-0748-TLG-T4a-a-skill-deixa-de-narrar-a-transicao-chega-ao-painel-pela-fun.md`, `docs/RDO/P-0748-TLG-T5-a-porta-de-entrada-diz-como-o-dono-acompanha-a-execucao-no-p.md`, `docs/RDO/P-0748-TLG-T5a-a-celula-da-scrum-master-na-tabela-de-skills-volta-a-dizer-q.md`, `docs/RDO/P-0749-SAN-T1-o-id-e-o-caminho-do-plano-num-lugar-so.md`, `docs/RDO/P-0749-SAN-T2-o-estado-sai-do-texto-e-vai-para-o-estado-tsv.md`, `docs/RDO/P-0749-SAN-T2a-projeto-novo-com-contador-em-p-0-e-nenhum-plano-passa-no-che.md`, `docs/RDO/P-0749-SAN-T3-relato-laudo-e-evidencia-nascem-na-pasta-do-plano.md`, `docs/RDO/P-0749-SAN-T3a-a-flag-vence-tambem-no-indice-e-a-cli-anuncia-os-dois-destin.md`, `docs/RDO/P-0749-SAN-T4-a-doutrina-ensina-a-pasta-o-estado-tsv-e-a-contagem-em-zero.md`, `docs/RDO/P-0749-SAN-T5-a-regra-do-artefato-de-humano-minimo-uma-vez-so.md`, `docs/RDO/P-0749-SAN-T6-a-porta-de-entrada-descreve-a-pasta-a-tabela-e-o-texto-minim.md`, `docs/RDO/P-0749-SAN-T6a-o-glossario-diz-o-contador-como-a-regra-o-diz.md`, `docs/RDO/P-0749-SAN-T6b-as-decisoes-estruturantes-dizem-o-contador-como-a-regra-o-di.md`, `docs/RDO/P-0750-CAH-T1-a-regra-da-mensagem-legivel-ao-dono-na-doutrina-e-no-regulam.md`, `docs/RDO/P-0750-CAH-T2-o-glossario-diz-o-que-cada-familia-de-sigla-nomeia.md`, `docs/RDO/P-0750-CAH-T3-a-tabela-de-falhas-de-comunicacao-com-as-falhas-ja-medidas.md`, `docs/RDO/P-0750-CAH-T4-a-skill-da-mensagem-ao-dono.md`, `docs/RDO/P-0750-CAH-T4a-o-titulo-de-tarefa-na-skill-da-mensagem-ao-dono-para-antes-d.md`, `docs/RDO/P-0750-CAH-T5-os-textos-que-mandavam-citar-sigla-ao-dono-passam-a-mandar-o.md`, `docs/RDO/P-0751-EBK-T1-o-check-acusa-tiquete-vivo-sem-card.md`, `docs/RDO/P-0751-EBK-T10-a-regua-de-autoria-do-card-segunda-leva.md`, `docs/RDO/P-0751-EBK-T11-o-planejador-publica-o-grep-da-superficie-e-ensaia-os-cards.md`, `docs/RDO/P-0751-EBK-T12-tres-ajustes-de-regra-existente-a-devolucao-do-modelador-o-e.md`, `docs/RDO/P-0751-EBK-T13-quanto-custa-retomar-o-planejador-por-mensagem.md`, `docs/RDO/P-0751-EBK-T13a-a-razao-da-regra-da-retomada-sai-do-custo-de-partida-nao-da.md`, `docs/RDO/P-0751-EBK-T14-a-rodada-de-revisao-de-guardrails-pendente-desde-2026-08-08.md`, `docs/RDO/P-0751-EBK-T2-o-check-confronta-o-card-com-o-rdo-py-e-o-piso-com-o-corpus.md`, `docs/RDO/P-0751-EBK-T3-o-next-projeta-o-colchete-do-cabecalho-inteiro.md`, `docs/RDO/P-0751-EBK-T4-rdo-py-close-recusa-tarefa-que-nao-esta-done.md`, `docs/RDO/P-0751-EBK-T5-o-kit-check-conta-defeito-nao-linha.md`, `docs/RDO/P-0751-EBK-T5a-o-kit-check-nao-conta-o-sumario-do-materializar-e-detalha-so.md`, `docs/RDO/P-0751-EBK-T6-nenhuma-fixture-carrega-nome-que-o-harness-descobre.md`, `docs/RDO/P-0751-EBK-T7-a-doutrina-do-teste-que-discrimina-e-da-medida-publicada.md`, `docs/RDO/P-0751-EBK-T8-a-vigencia-do-modelo-o-desfecho-do-drift-recusado-e-o-lastro.md`, `docs/RDO/P-0751-EBK-T9-uma-operacao-uma-oracao.md`, `docs/RDO/P-0752-FPU-T1-o-gate-do-card-le-a-forma-do-corpus-e-deixa-de-produzir-item.md`, `docs/RDO/P-0752-FPU-T10-a-tabela-de-acionamentos-ganha-a-coluna-de-causa-raiz.md`, `docs/RDO/P-0752-FPU-T1a-um-teste-tranca-o-marcador-de-item-so-no-inicio-de-linha-com.md`, `docs/RDO/P-0752-FPU-T2-o-gate-do-card-roda-no-ensaio-do-planejador-e-no-despacho-do.md`, `docs/RDO/P-0752-FPU-T3-toda-ancora-de-arquivo-e-linha-do-card-leva-o-literal-e-o-ga.md`, `docs/RDO/P-0752-FPU-T4-o-aviso-de-crenca-no-ato-de-gravar-plano-ou-diario.md`, `docs/RDO/P-0752-FPU-T4a-o-aviso-de-crenca-conta-uma-vez-o-literal-que-casa-dois-padr.md`, `docs/RDO/P-0752-FPU-T5-o-executor-devolve-a-medida-como-arquivo-e-a-evidencia-a-inc.md`, `docs/RDO/P-0752-FPU-T5a-o-executor-o-revisor-e-o-loop-falam-do-arquivo-de-medida.md`, `docs/RDO/P-0752-FPU-T5b-a-medida-guarda-a-cauda-da-saida-onde-esta-o-sumario.md`, `docs/RDO/P-0752-FPU-T5c-a-medida-do-executor-mora-onde-o-revisor-a-procura-tambem-no.md`, `docs/RDO/P-0752-FPU-T6-o-dossie-de-despacho-carrega-os-achados-roteados-ao-card.md`, `docs/RDO/P-0752-FPU-T7-o-escritor-da-telemetria-recusa-a-linha-repetida-da-mesma-ro.md`, `docs/RDO/P-0752-FPU-T8-as-armadilhas-de-ferramenta-medidas-ganham-um-arquivo-so.md`, `docs/RDO/P-0752-FPU-T8a-a-regua-de-autoria-do-card-aponta-as-armadilhas-de-ferrament.md`, `docs/RDO/P-0752-FPU-T9-a-skill-de-fatos-frescos.md`, `docs/RDO/P-0752-FPU-T9a-a-skill-de-fatos-frescos-le-os-totais-em-instrumento-de-leit.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-68a.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-84a.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-86a.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-87a-medida.json`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-87a.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88a.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88b-medida.json`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88b.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88c-medida.json`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88c.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88d-medida.json`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88d.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-89a-medida.json`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-89a.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-89b-medida.json`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-89b.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-90a-medida.json`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-90a.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-90b.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-91a-medida.json`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-91a.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0745-PLN-T4a.md`, `docs/RDO/evidencia/P-0745-PLN-T5.md`, `docs/RDO/evidencia/P-0745-PLN-T5a.md`, `docs/RDO/evidencia/P-0745-PLN-T6.md`, `docs/RDO/evidencia/P-0745-PLN-T7.md`, `docs/RDO/evidencia/P-0745-PLN-T7a.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/P-0747-CON-T1.md`, `docs/RDO/evidencia/P-0747-CON-T2.md`, `docs/RDO/evidencia/P-0747-CON-T2a.md`, `docs/RDO/evidencia/P-0747-CON-T2b.md`, `docs/RDO/evidencia/P-0747-CON-T3.md`, `docs/RDO/evidencia/P-0747-CON-T3a.md`, `docs/RDO/evidencia/P-0747-CON-T3b.md`, `docs/RDO/evidencia/P-0747-CON-T3c.md`, `docs/RDO/evidencia/P-0747-CON-T3d.md`, `docs/RDO/evidencia/P-0747-CON-T4.md`, `docs/RDO/evidencia/P-0747-CON-T4a.md`, `docs/RDO/evidencia/P-0747-CON-T5.md`, `docs/RDO/evidencia/P-0747-CON-T5a.md`, `docs/RDO/evidencia/P-0747-CON-T6.md`, `docs/RDO/evidencia/P-0747-CON-T6a.md`, `docs/RDO/evidencia/P-0747-CON-T7.md`, `docs/RDO/evidencia/P-0747-CON-T7a.md`, `docs/RDO/evidencia/P-0747-CON-T8.md`, `docs/RDO/evidencia/P-0747-CON-T8a.md`, `docs/RDO/evidencia/P-0748-TLG-T1.md`, `docs/RDO/evidencia/P-0748-TLG-T2.md`, `docs/RDO/evidencia/P-0748-TLG-T2a.md`, `docs/RDO/evidencia/P-0748-TLG-T2b.md`, `docs/RDO/evidencia/P-0748-TLG-T3.md`, `docs/RDO/evidencia/P-0748-TLG-T3a.md`, `docs/RDO/evidencia/P-0748-TLG-T3b.md`, `docs/RDO/evidencia/P-0748-TLG-T3c.md`, `docs/RDO/evidencia/P-0748-TLG-T3d.md`, `docs/RDO/evidencia/P-0748-TLG-T3e.md`, `docs/RDO/evidencia/P-0748-TLG-T3f.md`, `docs/RDO/evidencia/P-0748-TLG-T3g.md`, `docs/RDO/evidencia/P-0748-TLG-T3h.md`, `docs/RDO/evidencia/P-0748-TLG-T4.md`, `docs/RDO/evidencia/P-0748-TLG-T4a.md`, `docs/RDO/evidencia/P-0748-TLG-T5.md`, `docs/RDO/evidencia/P-0748-TLG-T5a.md`, `docs/RDO/evidencia/P-0749-SAN-T1.md`, `docs/RDO/evidencia/P-0749-SAN-T2.md`, `docs/RDO/evidencia/P-0749-SAN-T2a.md`, `docs/RDO/evidencia/P-0749-SAN-T3.md`, `docs/RDO/evidencia/P-0749-SAN-T3a.md`, `docs/RDO/evidencia/P-0749-SAN-T4.md`, `docs/RDO/evidencia/P-0749-SAN-T5.md`, `docs/RDO/evidencia/P-0749-SAN-T6.md`, `docs/RDO/evidencia/P-0749-SAN-T6a.md`, `docs/RDO/evidencia/P-0749-SAN-T6b.md`, `docs/RDO/evidencia/P-0750-CAH-T1.md`, `docs/RDO/evidencia/P-0750-CAH-T2.md`, `docs/RDO/evidencia/P-0750-CAH-T3.md`, `docs/RDO/evidencia/P-0750-CAH-T4.md`, `docs/RDO/evidencia/P-0750-CAH-T4a.md`, `docs/RDO/evidencia/P-0750-CAH-T5.md`, `docs/RDO/evidencia/P-0751-EBK-T1.md`, `docs/RDO/evidencia/P-0751-EBK-T10.md`, `docs/RDO/evidencia/P-0751-EBK-T11.md`, `docs/RDO/evidencia/P-0751-EBK-T12.md`, `docs/RDO/evidencia/P-0751-EBK-T13.md`, `docs/RDO/evidencia/P-0751-EBK-T13a.md`, `docs/RDO/evidencia/P-0751-EBK-T14.md`, `docs/RDO/evidencia/P-0751-EBK-T2.md`, `docs/RDO/evidencia/P-0751-EBK-T3.md`, `docs/RDO/evidencia/P-0751-EBK-T4.md`, `docs/RDO/evidencia/P-0751-EBK-T5.md`, `docs/RDO/evidencia/P-0751-EBK-T5a.md`, `docs/RDO/evidencia/P-0751-EBK-T6.md`, `docs/RDO/evidencia/P-0751-EBK-T7.md`, `docs/RDO/evidencia/P-0751-EBK-T8.md`, `docs/RDO/evidencia/P-0751-EBK-T9.md`, `docs/RDO/evidencia/P-0751-TK-86a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T1.md`, `docs/RDO/evidencia/P-0752-FPU-T10-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T10.md`, `docs/RDO/evidencia/P-0752-FPU-T1a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T1a.md`, `docs/RDO/evidencia/P-0752-FPU-T2.md`, `docs/RDO/evidencia/P-0752-FPU-T3.md`, `docs/RDO/evidencia/P-0752-FPU-T4-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T4.md`, `docs/RDO/evidencia/P-0752-FPU-T4a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T4a.md`, `docs/RDO/evidencia/P-0752-FPU-T5.md`, `docs/RDO/evidencia/P-0752-FPU-T5a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T5a.md`, `docs/RDO/evidencia/P-0752-FPU-T5b-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T5b.md`, `docs/RDO/evidencia/P-0752-FPU-T5c-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T5c.md`, `docs/RDO/evidencia/P-0752-FPU-T6-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T6.md`, `docs/RDO/evidencia/P-0752-FPU-T7-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T7.md`, `docs/RDO/evidencia/P-0752-FPU-T8-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T8.md`, `docs/RDO/evidencia/P-0752-FPU-T8a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T8a.md`, `docs/RDO/evidencia/P-0752-FPU-T9-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T9.md`, `docs/RDO/evidencia/P-0752-FPU-T9a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T9a.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/RDO/evidencia/TK-65-TK-65a.md`, `docs/RDO/evidencia/TK-65-TK-65b.md`, `docs/RDO/evidencia/TK-65-TK-65c.md`, `docs/RDO/evidencia/TK-65-TK-65d.md`, `docs/RDO/evidencia/TK-65-TK-65e.md`, `docs/RDO/evidencia/TK-66-TK-66a.md`, `docs/RDO/evidencia/TK-74-TK-74a.md`, `docs/RDO/evidencia/TK-74-TK-74b.md`, `docs/RDO/evidencia/TK-76-TK-76a.md`, `docs/RDO/evidencia/TK-77-TK-77a.md`, `docs/RDO/evidencia/TK-78-TK-78a.md`, `docs/RDO/evidencia/TK-78-TK-78b.md`, `docs/RDO/evidencia/TK-78-TK-78c.md`, `docs/RDO/evidencia/TK-78-TK-78d.md`, `docs/RDO/evidencia/TK-79-TK-79a.md`, `docs/RDO/evidencia/TK-82-TK-82a.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-84a.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-86a.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-87a.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-88a.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-88b.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-88c.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-88d.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-89a.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-89b.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-90a.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-90b.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-91a.md`, `docs/RDO/laudos/P-0752-FPU-T1.md`, `docs/RDO/laudos/P-0752-FPU-T10.md`, `docs/RDO/laudos/P-0752-FPU-T1a.md`, `docs/RDO/laudos/P-0752-FPU-T2.md`, `docs/RDO/laudos/P-0752-FPU-T3.md`, `docs/RDO/laudos/P-0752-FPU-T4.md`, `docs/RDO/laudos/P-0752-FPU-T4a.md`, `docs/RDO/laudos/P-0752-FPU-T5.md`, `docs/RDO/laudos/P-0752-FPU-T5a.md`, `docs/RDO/laudos/P-0752-FPU-T5b.md`, `docs/RDO/laudos/P-0752-FPU-T5c.md`, `docs/RDO/laudos/P-0752-FPU-T6.md`, `docs/RDO/laudos/P-0752-FPU-T7.md`, `docs/RDO/laudos/P-0752-FPU-T8.md`, `docs/RDO/laudos/P-0752-FPU-T8a.md`, `docs/RDO/laudos/P-0752-FPU-T9.md`, `docs/RDO/laudos/P-0752-FPU-T9a.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0745-planejador-modelo-operacao.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/P-0747-consultor-de-plano.md`, `docs/plans/P-0748-tela-do-gerente.md`, `docs/plans/P-0749-saneamento-artefatos.md`, `docs/plans/P-0750-comunicacao-agente-humano.md`, `docs/plans/P-0751-esgotar-backlog.md`, `docs/plans/P-0752-fato-no-ponto-de-uso.md`, `docs/plans/_CAMPANHA-P-0748.md`, `docs/plans/_CENARIO-P-0747.md`, `docs/plans/_CENARIO-P-0748.md`, `docs/plans/_CENARIO-P-0749.md`, `docs/plans/_CENARIO-P-0750.md`, `docs/plans/_CENARIO-P-0751.md`, `docs/plans/_CENARIO-P-0752.md`, `docs/plans/_CENARIO-TK-65.md`, `docs/plans/_CENARIO-TK-78.md`, `docs/plans/_CENARIO-TK-86.md`, `docs/plans/_CENARIO-TK-88.md`, `docs/plans/_CENARIO-TK-89.md`, `docs/plans/_ENTREGA-P-0751.md`, `docs/plans/_VEREDITO-procedimentos-2026-09-22.md`
- Ato do dono, fora do ciclo de tarefa: `.claude/agents/pantonic-consultant.md`, `.claude/agents/pantonic-fora-da-caixa.md`
- Fato: 45 arquivo(s) fora dos alvos e sem atribuição: `.claude/projecoes.json`, `.claude/skills/bootstrap-pantonic/SKILL.md`, `.claude/skills/entrega-de-encerramento/SKILL.md`, `.claude/skills/fatos-frescos/SKILL.md`, `.claude/skills/mensagem-ao-dono/SKILL.md`, `.claude/skills/redacao-doc/SKILL.md`, `.claude/tools/backlog_hook.py`, `.claude/tools/card_check.py`, `.claude/tools/crenca_hook.py`, `.claude/tools/telemetria.py`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/ARMADILHAS_DE_FERRAMENTA.md`, `docs/DIARIO_HISTORICO.md`, `docs/FALHAS_COMUNICACAO.tsv`, `docs/OPERACOES_AS_IS.md`, `docs/OPERACOES_AS_IS_P-0745.md`, `docs/OPERACOES_AS_IS_P-0746.md`, `docs/OPERACOES_AS_IS_P-0747.md`, `docs/OPERACOES_AS_IS_P-0748.md`, `docs/OPERACOES_AS_IS_P-0749.md`, `docs/OPERACOES_AS_IS_P-0750.md`, `docs/OPERACOES_AS_IS_P-0751.md`, `docs/RESIDENCIA_DOUTRINA.md`, `docs/consultant-spec.md`, `docs/planner-spec.md`, `tests/fixtures/card_check/alvo.txt`, `tests/fixtures/card_check/plano-ancoras.md`, `tests/fixtures/card_check/plano-corpus.md`, `tests/fixtures/modelo/fluxo-concluido.md`, `tests/fixtures/modelo/fluxo-pendente.md`, `tests/fixtures/modelo/fluxo-valido.md`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/fixtures/modelo/plano-invalido.md`, `tests/fixtures/modelo/plano-sem-cabecalho.md`, `tests/fixtures/modelo/plano-sem-estado.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_caminhos.py`, `tests/test_card_check.py`, `tests/test_crenca_hook.py`, `tests/test_doutrina_unidade.py`, `tests/test_fixtures_higiene.py`, `tests/test_kit_check.py`, `tests/test_telemetria.py`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/rdo.py`
```
diff --git a/.claude/tools/rdo.py b/.claude/tools/rdo.py
index 7380315..9b376ed 100644
--- a/.claude/tools/rdo.py
+++ b/.claude/tools/rdo.py
@@ -9,12 +9,21 @@ gramática fixa da `DP-C` (`extrair_dossie`, reusada também por `review_evidenc
 pendência-do-laudo) e o consumo medido, **calcula** o desdobramento pela tabela de dois ramos de
 `calcular_desdobramento` e materializa o documento a partir de `.claude/tools/rdo_template.md`
 numa única escrita atômica — o formato do RDO vive no template, não em nenhum prompt de agente.
-
-O RDO é escrito por uma única transição (`review` → `done`, `DP-F`/`DP-E`): tarefa `cancelled` ou
-`blocked` não produz RDO, então `close` não tem `--status` e não lê `status` de lugar nenhum. O
-laudo é documento **consumido e descartado** pelo `scrum-master` (`DP-H`) — `close` não abre
-arquivo de laudo nenhum e não conhece `--laudos-dir`; o template não pendura ponteiro para um
-documento que já não existe.
+O RDO tem três seções de nível 1 (`TK-88`): `# Humano` (resumo em linguagem corrente, o que o
+dono lê — `--humano`), `# Máquina` (dossiê verbatim, pacote do laudo, consumo e desdobramento, o
+que o próximo agente lê) e `# Histórico` (as linhas do painel do gerente para a tarefa —
+`--historico`). Quem preenche as duas seções de fora é `.claude/tools/encerrar.py tarefa`, o
+instrumento de fechamento que chama `cmd_close` em processo; `close` chamado direto preenche o
+mínimo honesto e nunca inventa linha de painel.
+
+O RDO é escrito por uma única transição (`review` → `done`, `DP-F`/`DP-E`): `close` recusa (exit
+!= 0, nada escrito) a tarefa cujo status corrente não é `done` — lido na mesma fonte que
+`backlog.py status` escreve (bullet `- **Status:**` no plano legado e no diário, linha da tarefa em
+`estado.tsv` no plano em pasta), nunca aceito por flag (`close` não tem `--status`, `DEB-8`).
+Status ausente (card sem o bullet, tarefa sem linha no `estado.tsv`, `estado.tsv` inexistente)
+conta como não-`done`. O laudo é documento **consumido e descartado** pelo `scrum-master` (`DP-H`)
+— `close` não abre arquivo de laudo nenhum e não conhece `--laudos-dir`; o template não pendura
+ponteiro para um documento que já não existe.
 
 Plano legado (cabeçalho sem colchete algum — a gramática fixa da `DX-15` é `### <ID> — <título>
 [<modelo> · classe <classe>]`, com o segmento histórico ` · teto <N>` aceito e descartado sem
@@ -31,16 +40,19 @@ diretório se preciso. `--vermelho-mecanico <dimensao>` (repetível) declara o q
 já reportou vermelho; marcar `conforme` contra uma dimensão declarada vermelha é recusado (`DA-7`).
 `--escalar "<uma linha>"` força `recomendacao=escalar` independentemente da tabela, e a linha
 gravada é a pendência que a regra `B1` consome. `--achado-processo <alvo> "<uma linha>"`
-(repetível; alvo em `dossie`, `doutrina`, `rubrica` ou `modelo`) grava a seção `## Achado de processo` e
+(repetível; alvo em `dossie` — ou `dossiê` —, `doutrina`, `rubrica` ou `modelo`) grava a seção `## Achado de processo` e
 **não** altera percentual, veredito, bloqueante nem recomendação — invariante 1 de
 `docs/RUBRICA_DE_REVISAO.md` §6; `--escalar` fica reservado ao achado que invalida a rota (decisão
-de arquitetura ou de requisito).
+de arquitetura ou de requisito). `--motivo <dimensao> "<uma linha>"` (repetível, só para dimensão
+fora de `conforme`) grava a seção `## Motivo das dimensões fora de conforme`, entre a tabela de
+níveis e o achado de processo — é o lugar do motivo, não o card *Lições aprendidas na tarefa*.
 
 Escrita atômica (arquivo temporário no mesmo diretório de destino + `os.replace`) e falha ruidosa
 (exit != 0, mensagem em stderr, nada escrito) no mesmo padrão de `.claude/tools/telemetria.py`."""
 from __future__ import annotations
 
 import argparse
+import importlib.util
 import math
 import os
 import re
@@ -50,6 +62,18 @@ import unicodedata
 from fractions import Fraction
 from pathlib import Path
 
+
+def _carregar_caminhos():
+    caminho = Path(__file__).resolve().parent /
```
[truncado em 4000 caracteres]

### `tests/test_rdo.py`
```
diff --git a/tests/test_rdo.py b/tests/test_rdo.py
index fbcc7fc..bcb1290 100644
--- a/tests/test_rdo.py
+++ b/tests/test_rdo.py
@@ -26,6 +26,9 @@ autonoma.md` é lido, nunca escrito, por este módulo."""
 from __future__ import annotations
 
 import importlib.util
+import os
+import subprocess
+import sys
 from pathlib import Path
 
 import pytest
@@ -223,9 +226,27 @@ def test_tr_laudo_recusa_nao_se_aplica_em_dimensao_que_nao_admite(tmp_path, caps
 # --- close (EXA-T19) — o RDO nasce inteiro no fechamento ----------------------------------------
 
 
+def _plano_real_com_status_done(tmp_path: Path) -> Path:
+    """Cópia de `_PLANO_REAL` em `tmp_path / "plano-real"` (subpasta, porque vários testes contam
+    os `.md` de `tmp_path` como RDO), com a linha `` - **Status:** `done` · 2026-09-25 `` inserida
+    logo abaixo de cada linha que começa por `### T7 — ` e por `### T8a — ` (`DEB-8`) — o plano
+    real não é tocado."""
+    destino = tmp_path / "plano-real" / _PLANO_REAL.name
+    if not destino.exists():
+        destino.parent.mkdir(parents=True, exist_ok=True)
+        linhas = _PLANO_REAL.read_text(encoding="utf-8").splitlines()
+        saida: list[str] = []
+        for linha in linhas:
+            saida.append(linha)
+            if linha.startswith("### T7 — ") or linha.startswith("### T8a — "):
+                saida.append("- **Status:** `done` · 2026-09-25")
+        destino.write_text("\n".join(saida) + "\n", encoding="utf-8")
+    return destino
+
+
 def _argv_close(tmp_path, tarefa="T7", omit=(), **overrides: str) -> list[str]:
     campos = {
-        "--plano": str(_PLANO_REAL),
+        "--plano": str(_plano_real_com_status_done(tmp_path)),
         "--tarefa": tarefa,
         "--tool-uses": "12",
         "--tokens-k": "80",
@@ -246,6 +267,68 @@ def _argv_close(tmp_path, tarefa="T7", omit=(), **overrides: str) -> list[str]:
     return argv
 
 
+def test_tf_close_recusa_tarefa_nao_done_e_aceita_done_no_plano_legado(tmp_path):
+    """TF do `DEB-8`: `close` recusa (exit != 0, nada escrito) uma tarefa `in-progress` — status
+    lido do bullet `- **Status:**` do corpo do card, no plano legado — e aceita (exit 0, RDO
+    escrito) a mesma tarefa quando o status passa a `done`."""
+    rdo = _load_rdo()
+    plano = tmp_path / "plano.md"
+    _escrever_plano_sintetico(
+        plano, "### T1 — Tarefa sintética [Sonnet · classe implementacao]", status="in-progress",
+    )
+
+    exit_code = rdo.main(_argv_close(tmp_path, tarefa="T1", **{"--plano": str(plano)}))
+
+    assert exit_code != 0
+    assert [p for p in tmp_path.glob("*.md") if p.name not in ("plano.md", "INDEX.md")] == []
+
+    _escrever_plano_sintetico(
+        plano, "### T1 — Tarefa sintética [Sonnet · classe implementacao]", status="done",
+    )
+
+    exit_code_done = rdo.main(_argv_close(tmp_path, tarefa="T1", **{"--plano": str(plano)}))
+
+    assert exit_code_done == 0
+    gerados = [p for p in tmp_path.glob("*.md") if p.name not in ("plano.md", "INDEX.md")]
+    assert len(gerados) == 1
+
+
+def test_tf_close_recusa_tarefa_nao_done_e_aceita_done_no_plano_em_pasta(tmp_path):
+    """TF do `DEB-8`: mesmo par sobre plano em pasta — status lido da linha da tarefa em
+    `estado.tsv`, nunca do corpo do card."""
+    rdo = _load_rdo()
+    plano = tmp_path / "docs" / "plans" / "P-0-delta" / "plano.md"
+    plano.parent.mkdir(parents=True)
+    _escrever_plano_sintetico(plano, "### T1 — Tarefa sintética [Sonnet · classe implementacao]")
+    estado_path = plano.parent / "estado.tsv"
+    rdo_dir = tmp_path / "rdo-dir"
+    argv = [
+        "close", "--plano", str(plano), "--tarefa", "T1",
+        "--tool-uses", "5", "--tokens-k", "10", "--duracao-s", "60",
+        "--veredito", "aprovado", "--percentual", "100", "--bloqueante", "nenhuma",
+        "--recomendacao", "seguir", "--pendencia-laudo", "nenhuma",
+        "--rdo-dir", str(rdo_dir),
+    ]
+
+    estado_path.write_text(
+        rdo._caminhos.CABECALHO_ESTADO + "\n" + "T1\ttare
```
[truncado em 4000 caracteres]

### `.claude/agents/pantonic-reviewer.md`
```
diff --git a/.claude/agents/pantonic-reviewer.md b/.claude/agents/pantonic-reviewer.md
index fb8248a..f27207f 100644
--- a/.claude/agents/pantonic-reviewer.md
+++ b/.claude/agents/pantonic-reviewer.md
@@ -34,12 +34,14 @@ das faixas. Abra a régua durante a revisão; marcação feita de memória é ma
 - Três entradas de julgamento, e só elas: o dossiê da tarefa no plano, o dossiê de evidência
   produzido por `.claude/tools/review_evidence.py` antes do despacho e o diff da entrega. Nenhuma
   delas é narrativa de quem executou — a entrega se julga pelo que ficou no repositório.
+- a seção `## Medida do executor` do dossiê de evidência é a única afirmação de verde admitida;
+  `ausente` conta como verificação não feita.
 - O dossiê de evidência nasce desta chamada, gerada pelo `scrum-master` antes do despacho:
 
   ```
   python .claude/tools/review_evidence.py --plano <plano> --tarefa <ID> \
     --desde <ref capturada no passo 4> \
-    --out docs/RDO/evidencia/<plano>-<ID>.md
+    --out docs/RDO/evidencia/<plano>-<ID>.md   # só plano legado; plano em pasta: sem --out, grava docs/plans/P-<n>-<slug>/evidencia/<ID>.md
   ```
 
   O instrumento se executa; abrir o fonte para entender a chamada é sinal de documentação
@@ -50,7 +52,7 @@ das faixas. Abra a régua durante a revisão; marcação feita de memória é ma
   é do `pantonic-model-designer`, despachado por quem conduz a sessão.
 - Saída: as duas linhas de veredito ao chamador, o dossiê `Ato de modelo` de `conflito` quando o
   passo 7 o exigir, e o laudo em documento próprio, gravado pelo gerador
-  em `docs/RDO/laudos/<plano>-<tarefa>.md`.
+  em `docs/plans/P-<n>-<slug>/laudos/<tarefa>.md` (plano legado: `docs/RDO/laudos/<plano>-<tarefa>.md`).
 - O laudo carrega o **pacote**: veredito, percentual, dimensão bloqueante, recomendação e
   pendência. Com esses cinco campos o `scrum-master` fecha o registro da tarefa sem falha, e é essa
   suficiência que o laudo tem de entregar.
@@ -122,8 +124,8 @@ fazer.
    `--vermelho-mecanico` é repetível e recebe toda dimensão que a camada mecânica reportou vermelha.
    `--escalar` é o seu único canal de pendência: presente, a recomendação vira `escalar`, dominante
    sobre a tabela de veredito, e é por ele que pendência de arquitetura ou de requisito chega ao
-   loop — que a roteia ao **planejamento** (G-REPLAN/G-NOASK, `GOVERNANCA.md` §7 itens 17-18);
-   ao dono chega só o que o planejador classificar como estratégico, nunca a sua linha direto. Percentual, veredito, bloqueante e recomendação saem do cálculo, e marcação inconsistente
+   loop — que a roteia à **triagem do consultor** (G-REPLAN/G-NOASK, `GOVERNANCA.md` §7 itens 17-18);
+   ao dono chega só o que o consultor devolver como drift do modelo ou estratégico, nunca a sua linha direto. Percentual, veredito, bloqueante e recomendação saem do cálculo, e marcação inconsistente
    com a régua faz o gerador falhar.
 7. **Retorno ao chamador** — as duas linhas fixas e, quando houver, o dossiê:
 
@@ -138,8 +140,9 @@ fazer.
    conduz a sessão lê para despachar o `pantonic-model-designer`; sem ele, a divergência fica só
    no laudo e o texto do modelo nunca é acertado. Você **não aciona** o modelador — devolve o dossiê e para.
 
-   O motivo de cada dimensão fora de `conforme`, os achados de processo com alvo e rota e a
-   pendência ao dono ficam no laudo, que é onde eles têm leitor.
+   O motivo de cada dimensão fora de `conforme` vai na flag `--motivo <dimensao> "<uma linha>"` do
+   `rdo.py laudo` — não no card *Lições aprendidas na tarefa*; os achados de processo com alvo e
+   rota e a pendência ao dono também ficam no laudo, que é onde eles têm leitor.
 
 ## Proibições
 

```

## Medida do executor
- ausente: docs\RDO\evidencia\DIARIO_DE_OBRAS-TK-85a-medida.json não existe

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
