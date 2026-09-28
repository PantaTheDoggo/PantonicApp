# Evidência de revisão — DIARIO_DE_OBRAS TK-88a

## Diff (`git diff --stat`)
```
.claude/README.md                                  |    8 +-
 .claude/agents/pantonic-consultant.md              |   43 +-
 .claude/agents/pantonic-executor.md                |   11 +-
 .claude/agents/pantonic-fora-da-caixa.md           |    2 +-
 .claude/agents/pantonic-model-designer.md          |   81 +-
 .claude/agents/pantonic-planner.md                 |  217 +-
 .claude/agents/pantonic-reviewer.md                |   10 +-
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
 .claude/tools/backlog.py                           |  482 ++-
 .claude/tools/backlog_hook.py                      |   14 +-
 .claude/tools/card_check.py                        |  403 ++-
 .claude/tools/modelo.py                            |   39 +-
 .claude/tools/rdo.py                               |  172 +-
 .claude/tools/rdo_template.md                      |   10 +
 .claude/tools/review_evidence.py                   |  153 +-
 GOVERNANCA.md                                      |  389 ++-
 README.md                                          |  196 +-
 docs/CUSTO_DO_PICKUP.md                            |  171 +
 docs/DIARIO_DE_OBRAS.md                            | 3450 ++++++++++++++++++--
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
 docs/telemetria.tsv                                |  371 +++
 .../backlog/vermelho/docs/DIARIO_DE_OBRAS.md       |    3 +
 tests/fixtures/modelo/fluxo-concluido.md           |   12 +-
 tests/fixtures/modelo/fluxo-pendente.md            |   20 +-
 tests/fixtures/modelo/fluxo-valido.md              |   12 +-
 tests/fixtures/modelo/plano-invalido-2.md          |   10 +-
 tests/fixtures/modelo/plano-invalido.md            |   12 +-
 tests/fixtures/modelo/plano-sem-cabecalho.md       |    8 +-
 tests/fixtures/modelo/plano-sem-estado.md          |    8 +-
 tests/test_backlog.py                              |  746 +++++
 tests/test_card_check.py                           |  208 ++
 tests/test_materializar.py                         |    2 +-
 tests/test_modelo.py                               |  143 +-
 tests/test_rdo.py                                  |  284 +-
 tests/test_review_evidence.py                      |  237 +-
 54 files changed, 9618 insertions(+), 1036 deletions(-)
```

## Arquivos tocados
- `.claude/README.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-consultant.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-executor.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-fora-da-caixa.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-model-designer.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-planner.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-reviewer.md` — atribuição: alheio; estado git: ` M`
- `.claude/checks/frontmatter_yaml.py` — atribuição: alheio; estado git: `??`
- `.claude/checks/kit_check.ps1` — atribuição: alheio; estado git: ` M`
- `.claude/global/CLAUDE.md` — atribuição: alheio; estado git: ` M`
- `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` — atribuição: alheio; estado git: ` M`
- `.claude/projecoes.json` — atribuição: alheio; estado git: ` M`
- `.claude/skills/bootstrap-pantonic/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/diario-de-obras/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/skills/entrega-de-encerramento/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/fatos-frescos/SKILL.md` — atribuição: alheio; estado git: `??`
- `.claude/skills/mensagem-ao-dono/SKILL.md` — atribuição: alheio; estado git: `??`
- `.claude/skills/modelo-por-fase/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/passagem-de-bastao/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/skills/redacao-doc/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/scrum-master/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/backlog.py` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/backlog_hook.py` — atribuição: alheio; estado git: ` M`
- `.claude/tools/caminhos.py` — atribuição: da entrega; estado git: `??`
- `.claude/tools/card_check.py` — atribuição: alheio; estado git: ` M`
- `.claude/tools/crenca_hook.py` — atribuição: alheio; estado git: `??`
- `.claude/tools/encerrar.py` — atribuição: da entrega; estado git: `??`
- `.claude/tools/modelo.py` — atribuição: alheio; estado git: ` M`
- `.claude/tools/progresso_hook.py` — atribuição: da entrega; estado git: `??`
- `.claude/tools/rdo.py` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/rdo_template.md` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/review_evidence.py` — atribuição: alheio; estado git: ` M`
- `GOVERNANCA.md` — atribuição: da entrega; estado git: ` M`
- `README.md` — atribuição: da entrega; estado git: ` M`
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
- `docs/RDO/P-0752-FPU-T8-as-armadilhas-de-ferramenta-medidas-ganham-um-arquivo-so.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T8a-a-regua-de-autoria-do-card-aponta-as-armadilhas-de-ferrament.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T9-a-skill-de-fatos-frescos.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T9a-a-skill-de-fatos-frescos-le-os-totais-em-instrumento-de-leit.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-68a.md` — atribuição: alheio; estado git: `??`
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
- `docs/RDO/evidencia/P-0752-FPU-T1.md` — atribuição: alheio; estado git: `??`
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
- `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-91a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T1.md` — atribuição: alheio; estado git: `??`
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
- `docs/RDO/laudos/P-0752-FPU-T8.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T8a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T9.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T9a.md` — atribuição: alheio; estado git: `??`
- `docs/RESIDENCIA_DOUTRINA.md` — atribuição: alheio; estado git: ` M`
- `docs/RUBRICA_DE_REVISAO.md` — atribuição: alheio; estado git: ` M`
- `docs/consultant-spec.md` — atribuição: alheio; estado git: ` M`
- `docs/planner-spec.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0741-modelo-conceitual.md` — atribuição: alheio; estado git: ` M`
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
- `tests/test_backlog.py` — atribuição: da entrega; estado git: ` M`
- `tests/test_caminhos.py` — atribuição: alheio; estado git: `??`
- `tests/test_card_check.py` — atribuição: alheio; estado git: ` M`
- `tests/test_crenca_hook.py` — atribuição: alheio; estado git: `??`
- `tests/test_doutrina_unidade.py` — atribuição: alheio; estado git: `??`
- `tests/test_encerrar.py` — atribuição: da entrega; estado git: `??`
- `tests/test_fixtures_higiene.py` — atribuição: alheio; estado git: `??`
- `tests/test_frontmatter_yaml.py` — atribuição: alheio; estado git: `??`
- `tests/test_global_claude.py` — atribuição: alheio; estado git: `??`
- `tests/test_kit_check.py` — atribuição: alheio; estado git: `??`
- `tests/test_materializar.py` — atribuição: alheio; estado git: ` M`
- `tests/test_modelo.py` — atribuição: alheio; estado git: ` M`
- `tests/test_progresso_hook.py` — atribuição: da entrega; estado git: `??`
- `tests/test_rdo.py` — atribuição: da entrega; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: árvore de trabalho inteira (nenhum `--desde` informado)
- Arquivos-alvo declarados: `.claude/tools/encerrar.py`, `.claude/tools/rdo.py`, `.claude/tools/rdo_template.md`, `.claude/tools/backlog.py`, `.claude/tools/caminhos.py`, `.claude/tools/progresso_hook.py`, `GOVERNANCA.md`, `README.md`, `.claude/skills/diario-de-obras/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `tests/test_encerrar.py`, `tests/test_rdo.py`, `tests/test_backlog.py`, `tests/test_progresso_hook.py`
- Literais não reconhecidos como caminho (21): `cmd_close`, `HUMANO`, `HISTORICO`, `--humano`, `--historico`, `# Humano`, `# Máquina`, `# Histórico`, `transacionar_status`, `done`, `extrair_handover`, `handovers_para`, `=== HANDOVER DE`, `renderizar_next`, `destino_operacoes`, `destino_entrega`, `encerrar.py tarefa`, `M-10`, `M-18`, `M-10`, `M-18`
- Arquivos tocados: `.claude/README.md`, `.claude/agents/pantonic-consultant.md`, `.claude/agents/pantonic-executor.md`, `.claude/agents/pantonic-fora-da-caixa.md`, `.claude/agents/pantonic-model-designer.md`, `.claude/agents/pantonic-planner.md`, `.claude/agents/pantonic-reviewer.md`, `.claude/checks/frontmatter_yaml.py`, `.claude/checks/kit_check.ps1`, `.claude/global/CLAUDE.md`, `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, `.claude/projecoes.json`, `.claude/skills/bootstrap-pantonic/SKILL.md`, `.claude/skills/diario-de-obras/SKILL.md`, `.claude/skills/entrega-de-encerramento/SKILL.md`, `.claude/skills/fatos-frescos/SKILL.md`, `.claude/skills/mensagem-ao-dono/SKILL.md`, `.claude/skills/modelo-por-fase/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/redacao-doc/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/backlog.py`, `.claude/tools/backlog_hook.py`, `.claude/tools/caminhos.py`, `.claude/tools/card_check.py`, `.claude/tools/crenca_hook.py`, `.claude/tools/encerrar.py`, `.claude/tools/modelo.py`, `.claude/tools/progresso_hook.py`, `.claude/tools/rdo.py`, `.claude/tools/rdo_template.md`, `.claude/tools/review_evidence.py`, `GOVERNANCA.md`, `README.md`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/ARMADILHAS_DE_FERRAMENTA.md`, `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/DIARIO_HISTORICO.md`, `docs/DOC_MAP.md`, `docs/FALHAS_COMUNICACAO.tsv`, `docs/OPERACOES_AS_IS.md`, `docs/OPERACOES_AS_IS_P-0745.md`, `docs/OPERACOES_AS_IS_P-0746.md`, `docs/OPERACOES_AS_IS_P-0747.md`, `docs/OPERACOES_AS_IS_P-0748.md`, `docs/OPERACOES_AS_IS_P-0749.md`, `docs/OPERACOES_AS_IS_P-0750.md`, `docs/OPERACOES_AS_IS_P-0751.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65a-check-recusa-id-de-depende-de-que-nao-e-item.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65b-o-ponto-de-carga-escreve-em-utf-8-antes-de-argparse-abrir-a.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65c-o-verbo-diretiva-nao-descarta-id-em-silencio.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65d-os-dois-depende-de-do-diario-voltam-a-gramatica.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65e-o-ramo-concatenado-do-aviso-de-diretiva-ganha-teste.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-66a-o-atribuidor-so-casa-tarefa-ja-despachada.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-68a-os-controles-1-1-e-1-2-da-regra-1-entram-na-copia-canonica-d.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-74a-o-alvo-diretorio-de-outra-tarefa-casa-por-prefixo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-74b-modelo-py-recusa-limpo-o-alvo-que-nao-e-arquivo-de-plano.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-76a-as-tabelas-do-modelo-em-frases-curtas-para-o-dono.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-77a-o-validate-recusa-frontmatter-de-agente-ou-skill-que-o-yaml.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78a-o-loop-nao-para-para-rebaixar-o-modelo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78b-a-regua-do-card-aprende-as-tres-licoes-da-janela.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78c-a-evidencia-mede-so-o-que-mudou-desde-o-despacho.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78d-a-doutrina-e-o-readme-deixam-de-mandar-parar-para-rebaixar-o.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-79a-a-prosa-depois-da-linha-de-retorno-e-descartada-por-regra-na.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-82a-rdo-py-escreve-em-utf-8-antes-de-argparse-abrir-a-boca.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-91a-o-bullet-emenda-do-modelador-diz-o-que-fazer-no-marco.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0741-MC-T5-o-readme-explica-o-modelo-a-afericao-sobre-o-proprio-plano-e.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0745-PLN-T4a-o-ponteiro-sobrevivente-da-tabela-aposentada-nos-fatos-estav.md`, `docs/RDO/P-0745-PLN-T5-o-modelador-diante-do-plano-sem-cards-e-o-lastro-que-e-do-pl.md`, `docs/RDO/P-0745-PLN-T5a-a-frase-que-governa-o-gate-do-modelador-e-a-enumeracao-que-e.md`, `docs/RDO/P-0745-PLN-T6-a-especificacao-do-agente-de-planejamento.md`, `docs/RDO/P-0745-PLN-T7-o-indice-de-documentos-e-a-revisao-do-readme.md`, `docs/RDO/P-0745-PLN-T7a-o-readme-deixa-de-defender-a-regua-que-ele-mesmo-aposenta.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/P-0747-CON-T1-o-consultor-entra-na-doutrina-de-governanca.md`, `docs/RDO/P-0747-CON-T2-a-definicao-de-conduta-do-consultor-sem-estatuto-provisorio.md`, `docs/RDO/P-0747-CON-T2a-corretivo-da-op-2-o-agente-descreve-o-cenario-persistido-e-l.md`, `docs/RDO/P-0747-CON-T2b-corretivo-da-op-2-o-agente-nomeia-a-recusa-do-impedimento-im.md`, `docs/RDO/P-0747-CON-T3-o-loop-leva-toda-parada-ao-consultor.md`, `docs/RDO/P-0747-CON-T3a-corretivo-da-op-3-a-parada-e-a-mesma-em-todas-as-regras-que.md`, `docs/RDO/P-0747-CON-T3b-corretivo-da-op-3-com-estrategico-o-loop-para-sem-executar-a.md`, `docs/RDO/P-0747-CON-T3c-corretivo-da-op-3-com-estrategico-a-rota-planejador-executa.md`, `docs/RDO/P-0747-CON-T3d-corretivo-da-op-3-o-loop-redespacha-sem-retentativa-o-card-c.md`, `docs/RDO/P-0747-CON-T4-a-forma-efemera-com-cenario-persistido.md`, `docs/RDO/P-0747-CON-T4a-corretivo-da-op-4-a-queda-de-uma-instancia-do-consultor-nao.md`, `docs/RDO/P-0747-CON-T5-o-outro-lado-da-fronteira-nas-definicoes-de-conduta.md`, `docs/RDO/P-0747-CON-T5a-corretivo-da-op-5-o-diario-e-a-regra-8-dizem-o-que-a-triagem.md`, `docs/RDO/P-0747-CON-T6-a-especificacao-vira-lastro-medido.md`, `docs/RDO/P-0747-CON-T6a-corretivo-da-op-6-a-spec-nao-prevalece-sobre-o-bloco-a.md`, `docs/RDO/P-0747-CON-T7-a-medida-do-piloto-da-forma-efemera.md`, `docs/RDO/P-0747-CON-T7a-corretivo-da-op-7-o-veredito-declara-o-modelo-das-instancias.md`, `docs/RDO/P-0747-CON-T8-a-porta-de-entrada-e-a-descricao-do-agente.md`, `docs/RDO/P-0747-CON-T8a-corretivo-da-op-8-a-description-volta-ao-yaml-que-o-harness.md`, `docs/RDO/P-0748-TLG-T1-a-sonda-de-viabilidade-diante-do-dono.md`, `docs/RDO/P-0748-TLG-T2-o-repertorio-de-mensagens-na-skill-do-loop.md`, `docs/RDO/P-0748-TLG-T2a-o-repertorio-deixa-de-citar-o-comando-que-nao-vai-existir.md`, `docs/RDO/P-0748-TLG-T2b-o-repertorio-como-tabela-de-eventos-a-skill-diz-o-que-a-func.md`, `docs/RDO/P-0748-TLG-T3-o-gancho-que-grava-o-arquivo-de-progresso.md`, `docs/RDO/P-0748-TLG-T3a-a-captura-do-payload-dos-ganchos-o-que-a-funcao-vai-ler.md`, `docs/RDO/P-0748-TLG-T3b-a-funcao-que-gera-a-linha-do-stream-a-cada-evento-do-loop.md`, `docs/RDO/P-0748-TLG-T3c-o-painel-nao-perde-linha-e-nao-afirma-o-que-nao-aconteceu.md`, `docs/RDO/P-0748-TLG-T3d-o-painel-so-diz-que-a-janela-encerrou-quando-ela-encerrou.md`, `docs/RDO/P-0748-TLG-T3e-o-painel-diz-so-o-que-o-gancho-ve-o-modelo-mostrado-e-o-cons.md`, `docs/RDO/P-0748-TLG-T3f-o-estado-do-gancho-nao-guarda-chave-que-ninguem-le.md`, `docs/RDO/P-0748-TLG-T3g-o-painel-reconhece-o-retorno-do-agente-com-o-ou-o-colchete-a.md`, `docs/RDO/P-0748-TLG-T3h-o-painel-da-uma-linha-a-cada-status-do-mesmo-comando-e-a-ski.md`, `docs/RDO/P-0748-TLG-T4-o-condutor-narra-uma-linha-do-repertorio-antes-de-cada-ato-n.md`, `docs/RDO/P-0748-TLG-T4a-a-skill-deixa-de-narrar-a-transicao-chega-ao-painel-pela-fun.md`, `docs/RDO/P-0748-TLG-T5-a-porta-de-entrada-diz-como-o-dono-acompanha-a-execucao-no-p.md`, `docs/RDO/P-0748-TLG-T5a-a-celula-da-scrum-master-na-tabela-de-skills-volta-a-dizer-q.md`, `docs/RDO/P-0749-SAN-T1-o-id-e-o-caminho-do-plano-num-lugar-so.md`, `docs/RDO/P-0749-SAN-T2-o-estado-sai-do-texto-e-vai-para-o-estado-tsv.md`, `docs/RDO/P-0749-SAN-T2a-projeto-novo-com-contador-em-p-0-e-nenhum-plano-passa-no-che.md`, `docs/RDO/P-0749-SAN-T3-relato-laudo-e-evidencia-nascem-na-pasta-do-plano.md`, `docs/RDO/P-0749-SAN-T3a-a-flag-vence-tambem-no-indice-e-a-cli-anuncia-os-dois-destin.md`, `docs/RDO/P-0749-SAN-T4-a-doutrina-ensina-a-pasta-o-estado-tsv-e-a-contagem-em-zero.md`, `docs/RDO/P-0749-SAN-T5-a-regra-do-artefato-de-humano-minimo-uma-vez-so.md`, `docs/RDO/P-0749-SAN-T6-a-porta-de-entrada-descreve-a-pasta-a-tabela-e-o-texto-minim.md`, `docs/RDO/P-0749-SAN-T6a-o-glossario-diz-o-contador-como-a-regra-o-diz.md`, `docs/RDO/P-0749-SAN-T6b-as-decisoes-estruturantes-dizem-o-contador-como-a-regra-o-di.md`, `docs/RDO/P-0750-CAH-T1-a-regra-da-mensagem-legivel-ao-dono-na-doutrina-e-no-regulam.md`, `docs/RDO/P-0750-CAH-T2-o-glossario-diz-o-que-cada-familia-de-sigla-nomeia.md`, `docs/RDO/P-0750-CAH-T3-a-tabela-de-falhas-de-comunicacao-com-as-falhas-ja-medidas.md`, `docs/RDO/P-0750-CAH-T4-a-skill-da-mensagem-ao-dono.md`, `docs/RDO/P-0750-CAH-T4a-o-titulo-de-tarefa-na-skill-da-mensagem-ao-dono-para-antes-d.md`, `docs/RDO/P-0750-CAH-T5-os-textos-que-mandavam-citar-sigla-ao-dono-passam-a-mandar-o.md`, `docs/RDO/P-0751-EBK-T1-o-check-acusa-tiquete-vivo-sem-card.md`, `docs/RDO/P-0751-EBK-T10-a-regua-de-autoria-do-card-segunda-leva.md`, `docs/RDO/P-0751-EBK-T11-o-planejador-publica-o-grep-da-superficie-e-ensaia-os-cards.md`, `docs/RDO/P-0751-EBK-T12-tres-ajustes-de-regra-existente-a-devolucao-do-modelador-o-e.md`, `docs/RDO/P-0751-EBK-T13-quanto-custa-retomar-o-planejador-por-mensagem.md`, `docs/RDO/P-0751-EBK-T13a-a-razao-da-regra-da-retomada-sai-do-custo-de-partida-nao-da.md`, `docs/RDO/P-0751-EBK-T14-a-rodada-de-revisao-de-guardrails-pendente-desde-2026-08-08.md`, `docs/RDO/P-0751-EBK-T2-o-check-confronta-o-card-com-o-rdo-py-e-o-piso-com-o-corpus.md`, `docs/RDO/P-0751-EBK-T3-o-next-projeta-o-colchete-do-cabecalho-inteiro.md`, `docs/RDO/P-0751-EBK-T4-rdo-py-close-recusa-tarefa-que-nao-esta-done.md`, `docs/RDO/P-0751-EBK-T5-o-kit-check-conta-defeito-nao-linha.md`, `docs/RDO/P-0751-EBK-T5a-o-kit-check-nao-conta-o-sumario-do-materializar-e-detalha-so.md`, `docs/RDO/P-0751-EBK-T6-nenhuma-fixture-carrega-nome-que-o-harness-descobre.md`, `docs/RDO/P-0751-EBK-T7-a-doutrina-do-teste-que-discrimina-e-da-medida-publicada.md`, `docs/RDO/P-0751-EBK-T8-a-vigencia-do-modelo-o-desfecho-do-drift-recusado-e-o-lastro.md`, `docs/RDO/P-0751-EBK-T9-uma-operacao-uma-oracao.md`, `docs/RDO/P-0752-FPU-T1-o-gate-do-card-le-a-forma-do-corpus-e-deixa-de-produzir-item.md`, `docs/RDO/P-0752-FPU-T1a-um-teste-tranca-o-marcador-de-item-so-no-inicio-de-linha-com.md`, `docs/RDO/P-0752-FPU-T2-o-gate-do-card-roda-no-ensaio-do-planejador-e-no-despacho-do.md`, `docs/RDO/P-0752-FPU-T3-toda-ancora-de-arquivo-e-linha-do-card-leva-o-literal-e-o-ga.md`, `docs/RDO/P-0752-FPU-T4-o-aviso-de-crenca-no-ato-de-gravar-plano-ou-diario.md`, `docs/RDO/P-0752-FPU-T4a-o-aviso-de-crenca-conta-uma-vez-o-literal-que-casa-dois-padr.md`, `docs/RDO/P-0752-FPU-T5-o-executor-devolve-a-medida-como-arquivo-e-a-evidencia-a-inc.md`, `docs/RDO/P-0752-FPU-T5a-o-executor-o-revisor-e-o-loop-falam-do-arquivo-de-medida.md`, `docs/RDO/P-0752-FPU-T5b-a-medida-guarda-a-cauda-da-saida-onde-esta-o-sumario.md`, `docs/RDO/P-0752-FPU-T5c-a-medida-do-executor-mora-onde-o-revisor-a-procura-tambem-no.md`, `docs/RDO/P-0752-FPU-T6-o-dossie-de-despacho-carrega-os-achados-roteados-ao-card.md`, `docs/RDO/P-0752-FPU-T8-as-armadilhas-de-ferramenta-medidas-ganham-um-arquivo-so.md`, `docs/RDO/P-0752-FPU-T8a-a-regua-de-autoria-do-card-aponta-as-armadilhas-de-ferrament.md`, `docs/RDO/P-0752-FPU-T9-a-skill-de-fatos-frescos.md`, `docs/RDO/P-0752-FPU-T9a-a-skill-de-fatos-frescos-le-os-totais-em-instrumento-de-leit.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-68a.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-91a-medida.json`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-91a.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0745-PLN-T4a.md`, `docs/RDO/evidencia/P-0745-PLN-T5.md`, `docs/RDO/evidencia/P-0745-PLN-T5a.md`, `docs/RDO/evidencia/P-0745-PLN-T6.md`, `docs/RDO/evidencia/P-0745-PLN-T7.md`, `docs/RDO/evidencia/P-0745-PLN-T7a.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/P-0747-CON-T1.md`, `docs/RDO/evidencia/P-0747-CON-T2.md`, `docs/RDO/evidencia/P-0747-CON-T2a.md`, `docs/RDO/evidencia/P-0747-CON-T2b.md`, `docs/RDO/evidencia/P-0747-CON-T3.md`, `docs/RDO/evidencia/P-0747-CON-T3a.md`, `docs/RDO/evidencia/P-0747-CON-T3b.md`, `docs/RDO/evidencia/P-0747-CON-T3c.md`, `docs/RDO/evidencia/P-0747-CON-T3d.md`, `docs/RDO/evidencia/P-0747-CON-T4.md`, `docs/RDO/evidencia/P-0747-CON-T4a.md`, `docs/RDO/evidencia/P-0747-CON-T5.md`, `docs/RDO/evidencia/P-0747-CON-T5a.md`, `docs/RDO/evidencia/P-0747-CON-T6.md`, `docs/RDO/evidencia/P-0747-CON-T6a.md`, `docs/RDO/evidencia/P-0747-CON-T7.md`, `docs/RDO/evidencia/P-0747-CON-T7a.md`, `docs/RDO/evidencia/P-0747-CON-T8.md`, `docs/RDO/evidencia/P-0747-CON-T8a.md`, `docs/RDO/evidencia/P-0748-TLG-T1.md`, `docs/RDO/evidencia/P-0748-TLG-T2.md`, `docs/RDO/evidencia/P-0748-TLG-T2a.md`, `docs/RDO/evidencia/P-0748-TLG-T2b.md`, `docs/RDO/evidencia/P-0748-TLG-T3.md`, `docs/RDO/evidencia/P-0748-TLG-T3a.md`, `docs/RDO/evidencia/P-0748-TLG-T3b.md`, `docs/RDO/evidencia/P-0748-TLG-T3c.md`, `docs/RDO/evidencia/P-0748-TLG-T3d.md`, `docs/RDO/evidencia/P-0748-TLG-T3e.md`, `docs/RDO/evidencia/P-0748-TLG-T3f.md`, `docs/RDO/evidencia/P-0748-TLG-T3g.md`, `docs/RDO/evidencia/P-0748-TLG-T3h.md`, `docs/RDO/evidencia/P-0748-TLG-T4.md`, `docs/RDO/evidencia/P-0748-TLG-T4a.md`, `docs/RDO/evidencia/P-0748-TLG-T5.md`, `docs/RDO/evidencia/P-0748-TLG-T5a.md`, `docs/RDO/evidencia/P-0749-SAN-T1.md`, `docs/RDO/evidencia/P-0749-SAN-T2.md`, `docs/RDO/evidencia/P-0749-SAN-T2a.md`, `docs/RDO/evidencia/P-0749-SAN-T3.md`, `docs/RDO/evidencia/P-0749-SAN-T3a.md`, `docs/RDO/evidencia/P-0749-SAN-T4.md`, `docs/RDO/evidencia/P-0749-SAN-T5.md`, `docs/RDO/evidencia/P-0749-SAN-T6.md`, `docs/RDO/evidencia/P-0749-SAN-T6a.md`, `docs/RDO/evidencia/P-0749-SAN-T6b.md`, `docs/RDO/evidencia/P-0750-CAH-T1.md`, `docs/RDO/evidencia/P-0750-CAH-T2.md`, `docs/RDO/evidencia/P-0750-CAH-T3.md`, `docs/RDO/evidencia/P-0750-CAH-T4.md`, `docs/RDO/evidencia/P-0750-CAH-T4a.md`, `docs/RDO/evidencia/P-0750-CAH-T5.md`, `docs/RDO/evidencia/P-0751-EBK-T1.md`, `docs/RDO/evidencia/P-0751-EBK-T10.md`, `docs/RDO/evidencia/P-0751-EBK-T11.md`, `docs/RDO/evidencia/P-0751-EBK-T12.md`, `docs/RDO/evidencia/P-0751-EBK-T13.md`, `docs/RDO/evidencia/P-0751-EBK-T13a.md`, `docs/RDO/evidencia/P-0751-EBK-T14.md`, `docs/RDO/evidencia/P-0751-EBK-T2.md`, `docs/RDO/evidencia/P-0751-EBK-T3.md`, `docs/RDO/evidencia/P-0751-EBK-T4.md`, `docs/RDO/evidencia/P-0751-EBK-T5.md`, `docs/RDO/evidencia/P-0751-EBK-T5a.md`, `docs/RDO/evidencia/P-0751-EBK-T6.md`, `docs/RDO/evidencia/P-0751-EBK-T7.md`, `docs/RDO/evidencia/P-0751-EBK-T8.md`, `docs/RDO/evidencia/P-0751-EBK-T9.md`, `docs/RDO/evidencia/P-0752-FPU-T1.md`, `docs/RDO/evidencia/P-0752-FPU-T1a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T1a.md`, `docs/RDO/evidencia/P-0752-FPU-T2.md`, `docs/RDO/evidencia/P-0752-FPU-T3.md`, `docs/RDO/evidencia/P-0752-FPU-T4-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T4.md`, `docs/RDO/evidencia/P-0752-FPU-T4a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T4a.md`, `docs/RDO/evidencia/P-0752-FPU-T5.md`, `docs/RDO/evidencia/P-0752-FPU-T5a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T5a.md`, `docs/RDO/evidencia/P-0752-FPU-T5b-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T5b.md`, `docs/RDO/evidencia/P-0752-FPU-T5c-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T5c.md`, `docs/RDO/evidencia/P-0752-FPU-T6-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T6.md`, `docs/RDO/evidencia/P-0752-FPU-T8-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T8.md`, `docs/RDO/evidencia/P-0752-FPU-T8a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T8a.md`, `docs/RDO/evidencia/P-0752-FPU-T9-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T9.md`, `docs/RDO/evidencia/P-0752-FPU-T9a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T9a.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/RDO/evidencia/TK-65-TK-65a.md`, `docs/RDO/evidencia/TK-65-TK-65b.md`, `docs/RDO/evidencia/TK-65-TK-65c.md`, `docs/RDO/evidencia/TK-65-TK-65d.md`, `docs/RDO/evidencia/TK-65-TK-65e.md`, `docs/RDO/evidencia/TK-66-TK-66a.md`, `docs/RDO/evidencia/TK-74-TK-74a.md`, `docs/RDO/evidencia/TK-74-TK-74b.md`, `docs/RDO/evidencia/TK-76-TK-76a.md`, `docs/RDO/evidencia/TK-77-TK-77a.md`, `docs/RDO/evidencia/TK-78-TK-78a.md`, `docs/RDO/evidencia/TK-78-TK-78b.md`, `docs/RDO/evidencia/TK-78-TK-78c.md`, `docs/RDO/evidencia/TK-78-TK-78d.md`, `docs/RDO/evidencia/TK-79-TK-79a.md`, `docs/RDO/evidencia/TK-82-TK-82a.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-91a.md`, `docs/RDO/laudos/P-0752-FPU-T1.md`, `docs/RDO/laudos/P-0752-FPU-T1a.md`, `docs/RDO/laudos/P-0752-FPU-T2.md`, `docs/RDO/laudos/P-0752-FPU-T3.md`, `docs/RDO/laudos/P-0752-FPU-T4.md`, `docs/RDO/laudos/P-0752-FPU-T4a.md`, `docs/RDO/laudos/P-0752-FPU-T5.md`, `docs/RDO/laudos/P-0752-FPU-T5a.md`, `docs/RDO/laudos/P-0752-FPU-T5b.md`, `docs/RDO/laudos/P-0752-FPU-T5c.md`, `docs/RDO/laudos/P-0752-FPU-T6.md`, `docs/RDO/laudos/P-0752-FPU-T8.md`, `docs/RDO/laudos/P-0752-FPU-T8a.md`, `docs/RDO/laudos/P-0752-FPU-T9.md`, `docs/RDO/laudos/P-0752-FPU-T9a.md`, `docs/RESIDENCIA_DOUTRINA.md`, `docs/RUBRICA_DE_REVISAO.md`, `docs/consultant-spec.md`, `docs/planner-spec.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0745-planejador-modelo-operacao.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/P-0747-consultor-de-plano.md`, `docs/plans/P-0748-tela-do-gerente.md`, `docs/plans/P-0749-saneamento-artefatos.md`, `docs/plans/P-0750-comunicacao-agente-humano.md`, `docs/plans/P-0751-esgotar-backlog.md`, `docs/plans/P-0752-fato-no-ponto-de-uso.md`, `docs/plans/_CAMPANHA-P-0748.md`, `docs/plans/_CENARIO-P-0747.md`, `docs/plans/_CENARIO-P-0748.md`, `docs/plans/_CENARIO-P-0749.md`, `docs/plans/_CENARIO-P-0750.md`, `docs/plans/_CENARIO-P-0751.md`, `docs/plans/_CENARIO-P-0752.md`, `docs/plans/_CENARIO-TK-65.md`, `docs/plans/_CENARIO-TK-78.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VEREDITO-procedimentos-2026-09-22.md`, `docs/telemetria.tsv`, `tests/fixtures/backlog/pasta/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/estado.tsv`, `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/plano.md`, `tests/fixtures/backlog/pasta/docs/plans/_INBOX.md`, `tests/fixtures/backlog/vermelho/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/card_check/alvo.txt`, `tests/fixtures/card_check/plano-ancoras.md`, `tests/fixtures/card_check/plano-corpus.md`, `tests/fixtures/modelo/fluxo-concluido.md`, `tests/fixtures/modelo/fluxo-pendente.md`, `tests/fixtures/modelo/fluxo-valido.md`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/fixtures/modelo/plano-invalido.md`, `tests/fixtures/modelo/plano-sem-cabecalho.md`, `tests/fixtures/modelo/plano-sem-estado.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_backlog.py`, `tests/test_caminhos.py`, `tests/test_card_check.py`, `tests/test_crenca_hook.py`, `tests/test_doutrina_unidade.py`, `tests/test_encerrar.py`, `tests/test_fixtures_higiene.py`, `tests/test_frontmatter_yaml.py`, `tests/test_global_claude.py`, `tests/test_kit_check.py`, `tests/test_materializar.py`, `tests/test_modelo.py`, `tests/test_progresso_hook.py`, `tests/test_rdo.py`, `tests/test_review_evidence.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/README.md` → `TK-64a`, `.claude/agents/pantonic-executor.md` → `TK-79a`, `.claude/agents/pantonic-model-designer.md` → `TK-76a`, `.claude/agents/pantonic-planner.md` → `TK-76a`, `.claude/checks/frontmatter_yaml.py` → `TK-77a`, `.claude/checks/kit_check.ps1` → `TK-77a`, `.claude/global/CLAUDE.md` → `TK-68a`, `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` → `TK-56a`, `.claude/skills/modelo-por-fase/SKILL.md` → `TK-78a`, `.claude/tools/modelo.py` → `TK-74b`, `.claude/tools/review_evidence.py` → `TK-66a`, `docs/CUSTO_DO_PICKUP.md` → `TK-54b`, `docs/DIARIO_DE_OBRAS.md` → `TK-54b`, `docs/DOC_MAP.md` → `TK-54b`, `tests/fixtures/backlog/pasta/docs/DIARIO_DE_OBRAS.md` → `TK-61a`, `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/estado.tsv` → `TK-61a`, `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/plano.md` → `TK-61a`, `tests/fixtures/backlog/pasta/docs/plans/_INBOX.md` → `TK-61a`, `tests/fixtures/backlog/vermelho/docs/DIARIO_DE_OBRAS.md` → `TK-61a`, `tests/test_frontmatter_yaml.py` → `TK-77a`, `tests/test_global_claude.py` → `TK-68a`, `tests/test_materializar.py` → `TK-56a`, `tests/test_modelo.py` → `TK-74b`, `tests/test_review_evidence.py` → `TK-62a`
- Registro da orquestração (não atribuível a tarefa): `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65a-check-recusa-id-de-depende-de-que-nao-e-item.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65b-o-ponto-de-carga-escreve-em-utf-8-antes-de-argparse-abrir-a.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65c-o-verbo-diretiva-nao-descarta-id-em-silencio.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65d-os-dois-depende-de-do-diario-voltam-a-gramatica.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65e-o-ramo-concatenado-do-aviso-de-diretiva-ganha-teste.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-66a-o-atribuidor-so-casa-tarefa-ja-despachada.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-68a-os-controles-1-1-e-1-2-da-regra-1-entram-na-copia-canonica-d.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-74a-o-alvo-diretorio-de-outra-tarefa-casa-por-prefixo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-74b-modelo-py-recusa-limpo-o-alvo-que-nao-e-arquivo-de-plano.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-76a-as-tabelas-do-modelo-em-frases-curtas-para-o-dono.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-77a-o-validate-recusa-frontmatter-de-agente-ou-skill-que-o-yaml.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78a-o-loop-nao-para-para-rebaixar-o-modelo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78b-a-regua-do-card-aprende-as-tres-licoes-da-janela.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78c-a-evidencia-mede-so-o-que-mudou-desde-o-despacho.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78d-a-doutrina-e-o-readme-deixam-de-mandar-parar-para-rebaixar-o.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-79a-a-prosa-depois-da-linha-de-retorno-e-descartada-por-regra-na.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-82a-rdo-py-escreve-em-utf-8-antes-de-argparse-abrir-a-boca.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-91a-o-bullet-emenda-do-modelador-diz-o-que-fazer-no-marco.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0741-MC-T5-o-readme-explica-o-modelo-a-afericao-sobre-o-proprio-plano-e.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0745-PLN-T4a-o-ponteiro-sobrevivente-da-tabela-aposentada-nos-fatos-estav.md`, `docs/RDO/P-0745-PLN-T5-o-modelador-diante-do-plano-sem-cards-e-o-lastro-que-e-do-pl.md`, `docs/RDO/P-0745-PLN-T5a-a-frase-que-governa-o-gate-do-modelador-e-a-enumeracao-que-e.md`, `docs/RDO/P-0745-PLN-T6-a-especificacao-do-agente-de-planejamento.md`, `docs/RDO/P-0745-PLN-T7-o-indice-de-documentos-e-a-revisao-do-readme.md`, `docs/RDO/P-0745-PLN-T7a-o-readme-deixa-de-defender-a-regua-que-ele-mesmo-aposenta.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/P-0747-CON-T1-o-consultor-entra-na-doutrina-de-governanca.md`, `docs/RDO/P-0747-CON-T2-a-definicao-de-conduta-do-consultor-sem-estatuto-provisorio.md`, `docs/RDO/P-0747-CON-T2a-corretivo-da-op-2-o-agente-descreve-o-cenario-persistido-e-l.md`, `docs/RDO/P-0747-CON-T2b-corretivo-da-op-2-o-agente-nomeia-a-recusa-do-impedimento-im.md`, `docs/RDO/P-0747-CON-T3-o-loop-leva-toda-parada-ao-consultor.md`, `docs/RDO/P-0747-CON-T3a-corretivo-da-op-3-a-parada-e-a-mesma-em-todas-as-regras-que.md`, `docs/RDO/P-0747-CON-T3b-corretivo-da-op-3-com-estrategico-o-loop-para-sem-executar-a.md`, `docs/RDO/P-0747-CON-T3c-corretivo-da-op-3-com-estrategico-a-rota-planejador-executa.md`, `docs/RDO/P-0747-CON-T3d-corretivo-da-op-3-o-loop-redespacha-sem-retentativa-o-card-c.md`, `docs/RDO/P-0747-CON-T4-a-forma-efemera-com-cenario-persistido.md`, `docs/RDO/P-0747-CON-T4a-corretivo-da-op-4-a-queda-de-uma-instancia-do-consultor-nao.md`, `docs/RDO/P-0747-CON-T5-o-outro-lado-da-fronteira-nas-definicoes-de-conduta.md`, `docs/RDO/P-0747-CON-T5a-corretivo-da-op-5-o-diario-e-a-regra-8-dizem-o-que-a-triagem.md`, `docs/RDO/P-0747-CON-T6-a-especificacao-vira-lastro-medido.md`, `docs/RDO/P-0747-CON-T6a-corretivo-da-op-6-a-spec-nao-prevalece-sobre-o-bloco-a.md`, `docs/RDO/P-0747-CON-T7-a-medida-do-piloto-da-forma-efemera.md`, `docs/RDO/P-0747-CON-T7a-corretivo-da-op-7-o-veredito-declara-o-modelo-das-instancias.md`, `docs/RDO/P-0747-CON-T8-a-porta-de-entrada-e-a-descricao-do-agente.md`, `docs/RDO/P-0747-CON-T8a-corretivo-da-op-8-a-description-volta-ao-yaml-que-o-harness.md`, `docs/RDO/P-0748-TLG-T1-a-sonda-de-viabilidade-diante-do-dono.md`, `docs/RDO/P-0748-TLG-T2-o-repertorio-de-mensagens-na-skill-do-loop.md`, `docs/RDO/P-0748-TLG-T2a-o-repertorio-deixa-de-citar-o-comando-que-nao-vai-existir.md`, `docs/RDO/P-0748-TLG-T2b-o-repertorio-como-tabela-de-eventos-a-skill-diz-o-que-a-func.md`, `docs/RDO/P-0748-TLG-T3-o-gancho-que-grava-o-arquivo-de-progresso.md`, `docs/RDO/P-0748-TLG-T3a-a-captura-do-payload-dos-ganchos-o-que-a-funcao-vai-ler.md`, `docs/RDO/P-0748-TLG-T3b-a-funcao-que-gera-a-linha-do-stream-a-cada-evento-do-loop.md`, `docs/RDO/P-0748-TLG-T3c-o-painel-nao-perde-linha-e-nao-afirma-o-que-nao-aconteceu.md`, `docs/RDO/P-0748-TLG-T3d-o-painel-so-diz-que-a-janela-encerrou-quando-ela-encerrou.md`, `docs/RDO/P-0748-TLG-T3e-o-painel-diz-so-o-que-o-gancho-ve-o-modelo-mostrado-e-o-cons.md`, `docs/RDO/P-0748-TLG-T3f-o-estado-do-gancho-nao-guarda-chave-que-ninguem-le.md`, `docs/RDO/P-0748-TLG-T3g-o-painel-reconhece-o-retorno-do-agente-com-o-ou-o-colchete-a.md`, `docs/RDO/P-0748-TLG-T3h-o-painel-da-uma-linha-a-cada-status-do-mesmo-comando-e-a-ski.md`, `docs/RDO/P-0748-TLG-T4-o-condutor-narra-uma-linha-do-repertorio-antes-de-cada-ato-n.md`, `docs/RDO/P-0748-TLG-T4a-a-skill-deixa-de-narrar-a-transicao-chega-ao-painel-pela-fun.md`, `docs/RDO/P-0748-TLG-T5-a-porta-de-entrada-diz-como-o-dono-acompanha-a-execucao-no-p.md`, `docs/RDO/P-0748-TLG-T5a-a-celula-da-scrum-master-na-tabela-de-skills-volta-a-dizer-q.md`, `docs/RDO/P-0749-SAN-T1-o-id-e-o-caminho-do-plano-num-lugar-so.md`, `docs/RDO/P-0749-SAN-T2-o-estado-sai-do-texto-e-vai-para-o-estado-tsv.md`, `docs/RDO/P-0749-SAN-T2a-projeto-novo-com-contador-em-p-0-e-nenhum-plano-passa-no-che.md`, `docs/RDO/P-0749-SAN-T3-relato-laudo-e-evidencia-nascem-na-pasta-do-plano.md`, `docs/RDO/P-0749-SAN-T3a-a-flag-vence-tambem-no-indice-e-a-cli-anuncia-os-dois-destin.md`, `docs/RDO/P-0749-SAN-T4-a-doutrina-ensina-a-pasta-o-estado-tsv-e-a-contagem-em-zero.md`, `docs/RDO/P-0749-SAN-T5-a-regra-do-artefato-de-humano-minimo-uma-vez-so.md`, `docs/RDO/P-0749-SAN-T6-a-porta-de-entrada-descreve-a-pasta-a-tabela-e-o-texto-minim.md`, `docs/RDO/P-0749-SAN-T6a-o-glossario-diz-o-contador-como-a-regra-o-diz.md`, `docs/RDO/P-0749-SAN-T6b-as-decisoes-estruturantes-dizem-o-contador-como-a-regra-o-di.md`, `docs/RDO/P-0750-CAH-T1-a-regra-da-mensagem-legivel-ao-dono-na-doutrina-e-no-regulam.md`, `docs/RDO/P-0750-CAH-T2-o-glossario-diz-o-que-cada-familia-de-sigla-nomeia.md`, `docs/RDO/P-0750-CAH-T3-a-tabela-de-falhas-de-comunicacao-com-as-falhas-ja-medidas.md`, `docs/RDO/P-0750-CAH-T4-a-skill-da-mensagem-ao-dono.md`, `docs/RDO/P-0750-CAH-T4a-o-titulo-de-tarefa-na-skill-da-mensagem-ao-dono-para-antes-d.md`, `docs/RDO/P-0750-CAH-T5-os-textos-que-mandavam-citar-sigla-ao-dono-passam-a-mandar-o.md`, `docs/RDO/P-0751-EBK-T1-o-check-acusa-tiquete-vivo-sem-card.md`, `docs/RDO/P-0751-EBK-T10-a-regua-de-autoria-do-card-segunda-leva.md`, `docs/RDO/P-0751-EBK-T11-o-planejador-publica-o-grep-da-superficie-e-ensaia-os-cards.md`, `docs/RDO/P-0751-EBK-T12-tres-ajustes-de-regra-existente-a-devolucao-do-modelador-o-e.md`, `docs/RDO/P-0751-EBK-T13-quanto-custa-retomar-o-planejador-por-mensagem.md`, `docs/RDO/P-0751-EBK-T13a-a-razao-da-regra-da-retomada-sai-do-custo-de-partida-nao-da.md`, `docs/RDO/P-0751-EBK-T14-a-rodada-de-revisao-de-guardrails-pendente-desde-2026-08-08.md`, `docs/RDO/P-0751-EBK-T2-o-check-confronta-o-card-com-o-rdo-py-e-o-piso-com-o-corpus.md`, `docs/RDO/P-0751-EBK-T3-o-next-projeta-o-colchete-do-cabecalho-inteiro.md`, `docs/RDO/P-0751-EBK-T4-rdo-py-close-recusa-tarefa-que-nao-esta-done.md`, `docs/RDO/P-0751-EBK-T5-o-kit-check-conta-defeito-nao-linha.md`, `docs/RDO/P-0751-EBK-T5a-o-kit-check-nao-conta-o-sumario-do-materializar-e-detalha-so.md`, `docs/RDO/P-0751-EBK-T6-nenhuma-fixture-carrega-nome-que-o-harness-descobre.md`, `docs/RDO/P-0751-EBK-T7-a-doutrina-do-teste-que-discrimina-e-da-medida-publicada.md`, `docs/RDO/P-0751-EBK-T8-a-vigencia-do-modelo-o-desfecho-do-drift-recusado-e-o-lastro.md`, `docs/RDO/P-0751-EBK-T9-uma-operacao-uma-oracao.md`, `docs/RDO/P-0752-FPU-T1-o-gate-do-card-le-a-forma-do-corpus-e-deixa-de-produzir-item.md`, `docs/RDO/P-0752-FPU-T1a-um-teste-tranca-o-marcador-de-item-so-no-inicio-de-linha-com.md`, `docs/RDO/P-0752-FPU-T2-o-gate-do-card-roda-no-ensaio-do-planejador-e-no-despacho-do.md`, `docs/RDO/P-0752-FPU-T3-toda-ancora-de-arquivo-e-linha-do-card-leva-o-literal-e-o-ga.md`, `docs/RDO/P-0752-FPU-T4-o-aviso-de-crenca-no-ato-de-gravar-plano-ou-diario.md`, `docs/RDO/P-0752-FPU-T4a-o-aviso-de-crenca-conta-uma-vez-o-literal-que-casa-dois-padr.md`, `docs/RDO/P-0752-FPU-T5-o-executor-devolve-a-medida-como-arquivo-e-a-evidencia-a-inc.md`, `docs/RDO/P-0752-FPU-T5a-o-executor-o-revisor-e-o-loop-falam-do-arquivo-de-medida.md`, `docs/RDO/P-0752-FPU-T5b-a-medida-guarda-a-cauda-da-saida-onde-esta-o-sumario.md`, `docs/RDO/P-0752-FPU-T5c-a-medida-do-executor-mora-onde-o-revisor-a-procura-tambem-no.md`, `docs/RDO/P-0752-FPU-T6-o-dossie-de-despacho-carrega-os-achados-roteados-ao-card.md`, `docs/RDO/P-0752-FPU-T8-as-armadilhas-de-ferramenta-medidas-ganham-um-arquivo-so.md`, `docs/RDO/P-0752-FPU-T8a-a-regua-de-autoria-do-card-aponta-as-armadilhas-de-ferrament.md`, `docs/RDO/P-0752-FPU-T9-a-skill-de-fatos-frescos.md`, `docs/RDO/P-0752-FPU-T9a-a-skill-de-fatos-frescos-le-os-totais-em-instrumento-de-leit.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-68a.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-91a-medida.json`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-91a.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0745-PLN-T4a.md`, `docs/RDO/evidencia/P-0745-PLN-T5.md`, `docs/RDO/evidencia/P-0745-PLN-T5a.md`, `docs/RDO/evidencia/P-0745-PLN-T6.md`, `docs/RDO/evidencia/P-0745-PLN-T7.md`, `docs/RDO/evidencia/P-0745-PLN-T7a.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/P-0747-CON-T1.md`, `docs/RDO/evidencia/P-0747-CON-T2.md`, `docs/RDO/evidencia/P-0747-CON-T2a.md`, `docs/RDO/evidencia/P-0747-CON-T2b.md`, `docs/RDO/evidencia/P-0747-CON-T3.md`, `docs/RDO/evidencia/P-0747-CON-T3a.md`, `docs/RDO/evidencia/P-0747-CON-T3b.md`, `docs/RDO/evidencia/P-0747-CON-T3c.md`, `docs/RDO/evidencia/P-0747-CON-T3d.md`, `docs/RDO/evidencia/P-0747-CON-T4.md`, `docs/RDO/evidencia/P-0747-CON-T4a.md`, `docs/RDO/evidencia/P-0747-CON-T5.md`, `docs/RDO/evidencia/P-0747-CON-T5a.md`, `docs/RDO/evidencia/P-0747-CON-T6.md`, `docs/RDO/evidencia/P-0747-CON-T6a.md`, `docs/RDO/evidencia/P-0747-CON-T7.md`, `docs/RDO/evidencia/P-0747-CON-T7a.md`, `docs/RDO/evidencia/P-0747-CON-T8.md`, `docs/RDO/evidencia/P-0747-CON-T8a.md`, `docs/RDO/evidencia/P-0748-TLG-T1.md`, `docs/RDO/evidencia/P-0748-TLG-T2.md`, `docs/RDO/evidencia/P-0748-TLG-T2a.md`, `docs/RDO/evidencia/P-0748-TLG-T2b.md`, `docs/RDO/evidencia/P-0748-TLG-T3.md`, `docs/RDO/evidencia/P-0748-TLG-T3a.md`, `docs/RDO/evidencia/P-0748-TLG-T3b.md`, `docs/RDO/evidencia/P-0748-TLG-T3c.md`, `docs/RDO/evidencia/P-0748-TLG-T3d.md`, `docs/RDO/evidencia/P-0748-TLG-T3e.md`, `docs/RDO/evidencia/P-0748-TLG-T3f.md`, `docs/RDO/evidencia/P-0748-TLG-T3g.md`, `docs/RDO/evidencia/P-0748-TLG-T3h.md`, `docs/RDO/evidencia/P-0748-TLG-T4.md`, `docs/RDO/evidencia/P-0748-TLG-T4a.md`, `docs/RDO/evidencia/P-0748-TLG-T5.md`, `docs/RDO/evidencia/P-0748-TLG-T5a.md`, `docs/RDO/evidencia/P-0749-SAN-T1.md`, `docs/RDO/evidencia/P-0749-SAN-T2.md`, `docs/RDO/evidencia/P-0749-SAN-T2a.md`, `docs/RDO/evidencia/P-0749-SAN-T3.md`, `docs/RDO/evidencia/P-0749-SAN-T3a.md`, `docs/RDO/evidencia/P-0749-SAN-T4.md`, `docs/RDO/evidencia/P-0749-SAN-T5.md`, `docs/RDO/evidencia/P-0749-SAN-T6.md`, `docs/RDO/evidencia/P-0749-SAN-T6a.md`, `docs/RDO/evidencia/P-0749-SAN-T6b.md`, `docs/RDO/evidencia/P-0750-CAH-T1.md`, `docs/RDO/evidencia/P-0750-CAH-T2.md`, `docs/RDO/evidencia/P-0750-CAH-T3.md`, `docs/RDO/evidencia/P-0750-CAH-T4.md`, `docs/RDO/evidencia/P-0750-CAH-T4a.md`, `docs/RDO/evidencia/P-0750-CAH-T5.md`, `docs/RDO/evidencia/P-0751-EBK-T1.md`, `docs/RDO/evidencia/P-0751-EBK-T10.md`, `docs/RDO/evidencia/P-0751-EBK-T11.md`, `docs/RDO/evidencia/P-0751-EBK-T12.md`, `docs/RDO/evidencia/P-0751-EBK-T13.md`, `docs/RDO/evidencia/P-0751-EBK-T13a.md`, `docs/RDO/evidencia/P-0751-EBK-T14.md`, `docs/RDO/evidencia/P-0751-EBK-T2.md`, `docs/RDO/evidencia/P-0751-EBK-T3.md`, `docs/RDO/evidencia/P-0751-EBK-T4.md`, `docs/RDO/evidencia/P-0751-EBK-T5.md`, `docs/RDO/evidencia/P-0751-EBK-T5a.md`, `docs/RDO/evidencia/P-0751-EBK-T6.md`, `docs/RDO/evidencia/P-0751-EBK-T7.md`, `docs/RDO/evidencia/P-0751-EBK-T8.md`, `docs/RDO/evidencia/P-0751-EBK-T9.md`, `docs/RDO/evidencia/P-0752-FPU-T1.md`, `docs/RDO/evidencia/P-0752-FPU-T1a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T1a.md`, `docs/RDO/evidencia/P-0752-FPU-T2.md`, `docs/RDO/evidencia/P-0752-FPU-T3.md`, `docs/RDO/evidencia/P-0752-FPU-T4-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T4.md`, `docs/RDO/evidencia/P-0752-FPU-T4a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T4a.md`, `docs/RDO/evidencia/P-0752-FPU-T5.md`, `docs/RDO/evidencia/P-0752-FPU-T5a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T5a.md`, `docs/RDO/evidencia/P-0752-FPU-T5b-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T5b.md`, `docs/RDO/evidencia/P-0752-FPU-T5c-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T5c.md`, `docs/RDO/evidencia/P-0752-FPU-T6-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T6.md`, `docs/RDO/evidencia/P-0752-FPU-T8-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T8.md`, `docs/RDO/evidencia/P-0752-FPU-T8a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T8a.md`, `docs/RDO/evidencia/P-0752-FPU-T9-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T9.md`, `docs/RDO/evidencia/P-0752-FPU-T9a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T9a.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/RDO/evidencia/TK-65-TK-65a.md`, `docs/RDO/evidencia/TK-65-TK-65b.md`, `docs/RDO/evidencia/TK-65-TK-65c.md`, `docs/RDO/evidencia/TK-65-TK-65d.md`, `docs/RDO/evidencia/TK-65-TK-65e.md`, `docs/RDO/evidencia/TK-66-TK-66a.md`, `docs/RDO/evidencia/TK-74-TK-74a.md`, `docs/RDO/evidencia/TK-74-TK-74b.md`, `docs/RDO/evidencia/TK-76-TK-76a.md`, `docs/RDO/evidencia/TK-77-TK-77a.md`, `docs/RDO/evidencia/TK-78-TK-78a.md`, `docs/RDO/evidencia/TK-78-TK-78b.md`, `docs/RDO/evidencia/TK-78-TK-78c.md`, `docs/RDO/evidencia/TK-78-TK-78d.md`, `docs/RDO/evidencia/TK-79-TK-79a.md`, `docs/RDO/evidencia/TK-82-TK-82a.md`, `docs/RDO/laudos/DIARIO_DE_OBRAS-TK-91a.md`, `docs/RDO/laudos/P-0752-FPU-T1.md`, `docs/RDO/laudos/P-0752-FPU-T1a.md`, `docs/RDO/laudos/P-0752-FPU-T2.md`, `docs/RDO/laudos/P-0752-FPU-T3.md`, `docs/RDO/laudos/P-0752-FPU-T4.md`, `docs/RDO/laudos/P-0752-FPU-T4a.md`, `docs/RDO/laudos/P-0752-FPU-T5.md`, `docs/RDO/laudos/P-0752-FPU-T5a.md`, `docs/RDO/laudos/P-0752-FPU-T5b.md`, `docs/RDO/laudos/P-0752-FPU-T5c.md`, `docs/RDO/laudos/P-0752-FPU-T6.md`, `docs/RDO/laudos/P-0752-FPU-T8.md`, `docs/RDO/laudos/P-0752-FPU-T8a.md`, `docs/RDO/laudos/P-0752-FPU-T9.md`, `docs/RDO/laudos/P-0752-FPU-T9a.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0745-planejador-modelo-operacao.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/P-0747-consultor-de-plano.md`, `docs/plans/P-0748-tela-do-gerente.md`, `docs/plans/P-0749-saneamento-artefatos.md`, `docs/plans/P-0750-comunicacao-agente-humano.md`, `docs/plans/P-0751-esgotar-backlog.md`, `docs/plans/P-0752-fato-no-ponto-de-uso.md`, `docs/plans/_CAMPANHA-P-0748.md`, `docs/plans/_CENARIO-P-0747.md`, `docs/plans/_CENARIO-P-0748.md`, `docs/plans/_CENARIO-P-0749.md`, `docs/plans/_CENARIO-P-0750.md`, `docs/plans/_CENARIO-P-0751.md`, `docs/plans/_CENARIO-P-0752.md`, `docs/plans/_CENARIO-TK-65.md`, `docs/plans/_CENARIO-TK-78.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VEREDITO-procedimentos-2026-09-22.md`, `docs/telemetria.tsv`
- Ato do dono, fora do ciclo de tarefa: `.claude/agents/pantonic-consultant.md`, `.claude/agents/pantonic-fora-da-caixa.md`, `.claude/agents/pantonic-reviewer.md`
- Fato: 44 arquivo(s) fora dos alvos e sem atribuição: `.claude/projecoes.json`, `.claude/skills/bootstrap-pantonic/SKILL.md`, `.claude/skills/entrega-de-encerramento/SKILL.md`, `.claude/skills/fatos-frescos/SKILL.md`, `.claude/skills/mensagem-ao-dono/SKILL.md`, `.claude/skills/redacao-doc/SKILL.md`, `.claude/tools/backlog_hook.py`, `.claude/tools/card_check.py`, `.claude/tools/crenca_hook.py`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/ARMADILHAS_DE_FERRAMENTA.md`, `docs/DIARIO_HISTORICO.md`, `docs/FALHAS_COMUNICACAO.tsv`, `docs/OPERACOES_AS_IS.md`, `docs/OPERACOES_AS_IS_P-0745.md`, `docs/OPERACOES_AS_IS_P-0746.md`, `docs/OPERACOES_AS_IS_P-0747.md`, `docs/OPERACOES_AS_IS_P-0748.md`, `docs/OPERACOES_AS_IS_P-0749.md`, `docs/OPERACOES_AS_IS_P-0750.md`, `docs/OPERACOES_AS_IS_P-0751.md`, `docs/RESIDENCIA_DOUTRINA.md`, `docs/RUBRICA_DE_REVISAO.md`, `docs/consultant-spec.md`, `docs/planner-spec.md`, `tests/fixtures/card_check/alvo.txt`, `tests/fixtures/card_check/plano-ancoras.md`, `tests/fixtures/card_check/plano-corpus.md`, `tests/fixtures/modelo/fluxo-concluido.md`, `tests/fixtures/modelo/fluxo-pendente.md`, `tests/fixtures/modelo/fluxo-valido.md`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/fixtures/modelo/plano-invalido.md`, `tests/fixtures/modelo/plano-sem-cabecalho.md`, `tests/fixtures/modelo/plano-sem-estado.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_caminhos.py`, `tests/test_card_check.py`, `tests/test_crenca_hook.py`, `tests/test_doutrina_unidade.py`, `tests/test_fixtures_higiene.py`, `tests/test_kit_check.py`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

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

### `.claude/tools/rdo.py`
```
diff --git a/.claude/tools/rdo.py b/.claude/tools/rdo.py
index 7380315..b31254f 100644
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
@@ -41,6 +50,7 @@ Escrita atômica (arquivo temporário no mesmo diretório de destino + `os.repla
 from __future__ import annotations
 
 import argparse
+import importlib.util
 import math
 import os
 import re
@@ -50,6 +60,18 @@ import unicodedata
 from fractions import Fraction
 from pathlib import Path
 
+
+def _carregar_caminhos():
+    caminho = Path(__file__).resolve().parent / "caminhos.py"
+    spec = importlib.util.spec_from_file_location("caminhos", caminho)
+    modulo = importlib.util.module_from_spec(spec)
+    sys.modules[spec.name] = modulo
+    spec.loader.exec_module(modulo)
+    return modulo
+
+
+_caminhos = _carregar_caminhos()
+
 _MODELOS = {"Opus", "Sonnet", "Haiku"}
 
 # Conjunto normativo de classes (`DP-C`) — usado nas mensagens de erro (`sorted(...)`) para nomear
@@ -146,7 +168,7 @@ class DossieTarefa:
     de anotações adiadas (`from __future__ import annotations`) que `dataclasses` faz na
     definição da classe — evitado ficando fora do mecanismo de dataclass."""
 
-    def __init__(self, tarefa_id, titulo, modelo, classe, esquema, campos, extras):
+    def __init__(self, tarefa_id, titulo, modelo, classe, esquema, campos, extras, campos_linhas=None):
         self.tarefa_id = tarefa_id
         self.titulo = titulo
         self.modelo = modelo
@@ -154,6 +176,7 @@ class DossieTarefa:
         self.esquema = esquema  # "padrao" | "legado"
         self.campos = campos
         self.extras = extras
+        self.campos_linhas = campos_linhas
 
 
 def _remover_acentos(texto: str) -> str:
@@ -186,8 +209,14 @@ def _slugify(titulo: str) -> str:
     return texto[
```
[truncado em 4000 caracteres]

### `.claude/tools/rdo_template.md`
```
diff --git a/.claude/tools/rdo_template.md b/.claude/tools/rdo_template.md
index 3a1e6e1..a112207 100644
--- a/.claude/tools/rdo_template.md
+++ b/.claude/tools/rdo_template.md
@@ -1,5 +1,11 @@
 # RDO — {{PLANO_ID}} · {{TAREFA_ID}}
 
+# Humano
+
+{{HUMANO}}
+
+# Máquina
+
 **Plano:** `{{PLANO_PATH}}`
 **Tarefa:** `{{TAREFA_ID}}` — {{TITULO}}
 **Modelo:** {{MODELO}} · **Classe:** {{CLASSE}}
@@ -44,3 +50,7 @@
 ## Fechamento
 
 **Desdobramento:** {{DESDOBRAMENTO}}
+
+# Histórico
+
+{{HISTORICO}}

```

### `.claude/tools/backlog.py`
```
diff --git a/.claude/tools/backlog.py b/.claude/tools/backlog.py
index 04e4be1..f1152f6 100644
--- a/.claude/tools/backlog.py
+++ b/.claude/tools/backlog.py
@@ -1,9 +1,10 @@
 """BKL-T2 (`docs/plans/P-0739-backlog-instrumento.md` `### BKL-T2`) — núcleo somente-leitura do
 instrumento de backlog: carrega o índice do diário, os planos vivos e o próprio diário; monta o
-grafo item → tarefas; `check` acusa cada violação de gramática (`C-1..C-11`, vocabulário fechado
+grafo item → tarefas; `check` acusa cada violação de gramática (`C-1..C-17`, vocabulário fechado
 definido no card) com `arquivo:linha`; `resolver_citacao_secao` (`TK-60a`) resolve uma citação
 `` `<arquivo>.md` §<N>[.<N>]* `` contra o arquivo citado, acusando `C-11` quando a seção não
-existe — vocabulário do instrumento fechado em `C-1..C-11`; `show` emite o dossiê verbatim de um item,
+existe; `C-12` (`TK-65a`) acusa `Depende de:` fora da gramática ou citando id que não é item —
+vocabulário do instrumento fechado em `C-1..C-17`; `show` emite o dossiê verbatim de um item,
 truncado ao teto `DB-7` (8.000 chars / 120 linhas, com ponteiro `arquivo:l1-l2` quando corta).
 
 Gramática implementada (residência canônica: skill `diario-de-obras`, seção "Gramática legível
@@ -44,12 +45,42 @@ from __future__ import annotations
 
 import argparse
 import datetime
+import importlib.util
 import os
 import re
 import sys
 from dataclasses import dataclass, field
 from pathlib import Path
 
+
+def _carregar_caminhos():
+    caminho = Path(__file__).resolve().parent / "caminhos.py"
+    spec = importlib.util.spec_from_file_location("caminhos", caminho)
+    modulo = importlib.util.module_from_spec(spec)
+    sys.modules[spec.name] = modulo
+    spec.loader.exec_module(modulo)
+    return modulo
+
+
+_caminhos = _carregar_caminhos()
+
+
+_rdo_modulo = None
+
+
+def _carregar_rdo():
+    """Carregado sob demanda (não no import do módulo): ambientes de teste que copiam só
+    `backlog.py` + `caminhos.py` para uma raiz de teste isolada (sem `rdo.py`) continuam
+    funcionando para todo caminho que não liga `dossie=True` — só `_dossie_check` chama isto."""
+    global _rdo_modulo
+    if _rdo_modulo is None:
+        caminho = Path(__file__).resolve().parent / "rdo.py"
+        spec = importlib.util.spec_from_file_location("rdo", caminho)
+        modulo = importlib.util.module_from_spec(spec)
+        spec.loader.exec_module(modulo)
+        _rdo_modulo = modulo
+    return _rdo_modulo
+
 # --------------------------------------------------------------------------- #
 # Vocabulário fechado (DB-3) e gramática de ID (DB-14)
 # --------------------------------------------------------------------------- #
@@ -65,8 +96,16 @@ _BRACKET = (
     rf"\[({_MODELOS})(?: \+ dono)?(?: · esforço (?:{_ESFORCOS}))?"
     rf" · classe ({_CLASSES})(?: · teto \d+)?\]"
 )
+# EBK-T3 — regex independente (não usada por TAREFA_HEADER_RE/SUBTAREFA_HEADER_RE) só para
+# extrair `+ dono`/`esforço` do texto bruto do cabeçalho, sem tocar a numeração de grupos que
+# `test_tr_bkl_grupos_posicionais` (LM-T4a) trava: `_BRACKET` continua com dono/esforço não
+# capturantes ali.
+_BRACKET_DETALHE_RE = re.compile(
+    rf"\[(?:{_MODELOS})(?P<dono> \+ dono)?(?: · esforço (?P<esforco>{_ESFORCOS}))?"
+    rf" · classe (?:{_CLASSES})(?: · teto \d+)?\]"
+)
 
-PLANO_HEADER_RE = re.compile(r"^# (P-\d{4}) — (.+)$")
+PLANO_HEADER_RE = _caminhos.PLANO_HEADER_RE
 STATUS_CAMPO_RE = re.compile(r"\*\*Status:\*\* `([a-z-]+)`")
 PREFIXO_CAMPO_RE = re.compile(r"\*\*Prefixo das tarefas no diário:\*\* `([A-Za-z0-9]+)-T<n>`")
 ORDEM_CAMPO_RE = re.compile(r"\*\*Ordem de execução:\*\* (.+)$")
@@ -83,6 +122,9 @@ STATUS_BULLET_RE = re.compile(
     r"^- \*\*Status:\*\* `([a-z-]+)`(?: · \d{4}-\d{2}-\d{2}(?: · ([^—]+?))?|.*?)(?: — (.+))?$"
 )
 DEPENDE_BULLET_RE = re.compile(r"^- \*\*Depende de:\*\* (.+)$")
+# Gramática publicada do valor (skill `diario-de-obras`, *Item e residência*): `` `ID`[, `ID`] ``
+# e nada mais — `C-12` (TK-65a) acusa q
```
[truncado em 4000 caracteres]

### `.claude/tools/caminhos.py`
```
"""P-0749 SAN-T1 — residência única da forma do id e do caminho de plano (`DSA-8`).

Duas formas convivem, reconhecidas pelo caminho, sem chave de configuração (`DSA-7`): plano
legado `docs/plans/P-<dígitos>-<slug>.md` e plano em pasta `docs/plans/P-<n>-<slug>/plano.md`.
Nenhuma outra ferramenta guarda cópia destas regex (`I-3`); cada uma carrega este módulo por
caminho, via `importlib.util.spec_from_file_location`. Função entra aqui com o primeiro chamador
de produção (`DSA-18`); `main` é a CLI de listagem e o entry point do módulo (`DSA-19`).
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

PLANO_HEADER_RE = re.compile(r"^# (P-\d+) — (.+)$")
ID_PLANO_RE = re.compile(r"^P-(\d+)$")
CAMINHO_PLANO_INBOX_RE = re.compile(r"docs/plans/P-\d+-[^)\s`/]+(?:/plano)?\.md")
ID_PLANO_INBOX_RE = re.compile(r"docs/plans/P-(\d+)-")
CONTADOR_INBOX_RE = re.compile(r"\*\*Próximo id de plano: P-\d+\.\*\*")
CONTADOR_INBOX_ID_RE = re.compile(r"\*\*Próximo id de plano: P-(\d+)\.\*\*")

NOME_PLANO_PASTA = "plano.md"
_ID_NO_NOME_RE = re.compile(r"^(P-\d+)")
_PASTA_RE = re.compile(r"^P-\d+-")


def planos_dir(raiz: Path) -> Path:
    return Path(raiz) / "docs" / "plans"


def inbox_planos(raiz: Path) -> Path:
    return planos_dir(raiz) / "_INBOX.md"


def e_layout_pasta(plano_path: Path) -> bool:
    p = Path(plano_path)
    return p.name == NOME_PLANO_PASTA and _PASTA_RE.match(p.parent.name) is not None


def arquivos_de_plano(raiz: Path) -> list[Path]:
    base = planos_dir(raiz)
    legado = [p for p in base.glob("P-*.md") if p.is_file()]
    pasta = [p for p in base.glob("P-*/" + NOME_PLANO_PASTA) if p.is_file() and e_layout_pasta(p)]
    return sorted(legado + pasta)


def id_do_plano(plano_path: Path) -> str | None:
    p = Path(plano_path)
    nome = p.parent.name if e_layout_pasta(p) else p.stem
    m = _ID_NO_NOME_RE.match(nome)
    return m.group(1) if m else None


def pasta_do_plano(plano_path: Path) -> Path | None:
    p = Path(plano_path)
    return p.parent if e_layout_pasta(p) else None


NOME_ESTADO = "estado.tsv"
CABECALHO_ESTADO = "id\ttipo\tstatus\trazao\tdata\tnota"


def estado_tsv(plano_path: Path) -> Path:
    return Path(plano_path).parent / NOME_ESTADO


def formatar_id(numero: int, largura: int) -> str:
    return f"P-{numero:0{largura}d}"


def pasta_por_id(raiz: Path, plano_id: str) -> Path | None:
    achadas = [p.parent for p in planos_dir(raiz).glob(plano_id + "-*/" + NOME_PLANO_PASTA) if p.is_file()]
    return achadas[0] if len(achadas) == 1 else None


def destino_rdo(pasta: Path, tarefa: str) -> Path:
    return Path(pasta) / "rdo" / f"{tarefa}.md"


def destino_laudo(pasta: Path, tarefa: str) -> Path:
    return Path(pasta) / "laudos" / f"{tarefa}.md"


def destino_evidencia(pasta: Path, tarefa: str) -> Path:
    return Path(pasta) / "evidencia" / f"{tarefa}.md"


# Artefatos de fechamento de plano (`GOVERNANCA.md` §4.2, *Pasta do plano*; `TK-88`): o
# documento de validação (`operacoes.md`, skill `entrega-de-encerramento`) e a entrega aceita
# (`entrega.md`, escrita por `encerrar.py plano`). Plano legado: `docs/OPERACOES_AS_IS_<id>.md`
# e `docs/plans/_ENTREGA-<id>.md`, ao lado de `_CENARIO-<id>.md`.
def destino_operacoes(raiz: Path, plano_path: Path) -> Path:
    pasta = pasta_do_plano(plano_path)
    if pasta is not None:
        return pasta / "operacoes.md"
    return Path(raiz) / "docs" / f"OPERACOES_AS_IS_{id_do_plano(plano_path)}.md"


def destino_entrega(raiz: Path, plano_path: Path) -> Path:
    pasta = pasta_do_plano(plano_path)
    if pasta is not None:
        return pasta / "entrega.md"
    return planos_dir(raiz) / f"_ENTREGA-{id_do_plano(plano_path)}.md"


def main(argv: list[str] | None = None) -> int:
    """Lista os planos da raiz, um por linha: `<id><TAB><caminho relativo à raiz>`."""
    parser = argparse.ArgumentParser(description="Lista os planos, legado e em pasta.")
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[2]))
```
[truncado em 4000 caracteres]

### `.claude/tools/progresso_hook.py`
```
"""Ganchos `PreToolUse`, `PostToolUse`, `UserPromptSubmit` e `Stop` do `P-0748` (`OP-3`):
gera em `.claude/estado/progresso.txt` uma frase por evento de transição do loop, com o
título da tarefa no lugar da sigla. Falha aberta total: qualquer exceção em `main` é
silenciada e o script sempre sai `0`; nunca imprime. Captura de payload opcional (flag
`progresso-captura.on`).
"""
from __future__ import annotations

import importlib.util
import json
import os
import re
import sys
import time
from pathlib import Path


def _carregar_caminhos():
    caminho = Path(__file__).resolve().parent / "caminhos.py"
    spec = importlib.util.spec_from_file_location("caminhos", caminho)
    modulo = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = modulo
    spec.loader.exec_module(modulo)
    return modulo


_caminhos = _carregar_caminhos()

KIT = Path(__file__).resolve().parents[1]
REPO = KIT.parent

PAPEIS = {
    "pantonic-executor": "executor",
    "pantonic-reviewer": "revisor",
    "pantonic-consultant": "consultor",
    "pantonic-model-designer": "modelador",
    "pantonic-planner": "planejador",
}

ESTADO_ARQ = "progresso-estado.json"
CAPTURA_FLAG = "progresso-captura.on"
CAPTURA_ARQ = "progresso-captura.jsonl"
CAPTURA_TETO_BYTES = 1_000_000

FRASES = {
    'M-0': 'Abrindo a janela do plano "<título do plano>".',
    'M-1': 'Tarefa "<título>". Passo: conferir os gates e preparar o despacho.',
    'M-2': 'Tarefa "<título>": gates aprovados; vou materializar in-progress e gravar o ponto de partida.',
    'M-3': 'Agente executor recebe a tarefa "<título>" e vai executar: <objetivo>',
    'M-3b': 'Agente executor recebe a tarefa "<título>" e vai executar o card.',
    'M-4': 'Agente executor devolveu a tarefa "<título>": review — <pendência>.',
    'M-4b': 'Agente executor devolveu a tarefa "<título>": blocked — motivo <motivo>: <razão>.',
    'M-5': 'Tarefa "<título>": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.',
    'M-6': 'Agente revisor recebe a tarefa "<título>" e vai confrontar a entrega com o card.',
    'M-7': 'Agente revisor devolveu a tarefa "<título>": <veredito> <percentual>%, bloqueante <bloqueante>.',
    'M-8': 'Agente consultor recebe a tarefa "<título>" e vai triar.',
    'M-9': 'Agente consultor devolveu a tarefa "<título>": rota <rota>.',
    'M-9b': 'Agente consultor devolveu a tarefa "<título>": rota <rota>; estratégico: <frase>.',
    'M-10': 'Scrum master vai fechar a tarefa "<título>" como done: registrar estado, RDO e telemetria.',
    'M-10b': 'Scrum master vai marcar a tarefa "<título>" como <estado>, sem RDO.',
    'M-11': 'Scrum master concluiu a tarefa "<título fechada>" e vai pegar a tarefa "<título>".',
    'M-12': 'Scrum master concluiu a tarefa "<título fechada>"; nada delegável na fila. Encerrando a janela com o relatório.',
    'M-12b': 'Scrum master não encontrou tarefa delegável na fila. Encerrando a janela com o relatório.',
    'M-13': 'Tarefa "<título>": vou medir a que arquivo a pendência é atribuível.',
    'M-14': 'Agente modelador recebe a tarefa "<título>" e vai fazer <ato> no modelo.',
    'M-14b': 'Agente modelador recebe a tarefa "<título>" e vai atualizar o modelo.',
    'M-15': 'Agente planejador recebe a tarefa "<título>" e vai replanejar.',
    'M-16': 'Agente <papel> devolveu a tarefa "<título>": <primeira linha>.',
    'M-17': 'Scrum master mostrou o modelo do plano e aguarda; a resposta dele está na extensão.',
    'M-18': 'Scrum master vai fechar o plano "<título do plano>": registrar estado, relatório de entrega e a linha do diário.',
}


def titulo_do_plano(caminho: str, raiz: Path) -> str:
    """Título da linha 1 do plano (`# P-<n> — <título>`) apontado por `--plano` de
    `encerrar.py plano`; vazio quando o arquivo não existe ou a linha não casa."""
    for base in (Path(caminho), raiz / caminho):
        try:
            primeira = base.read_text(encoding="utf-8", err
```
[truncado em 4000 caracteres]

### `GOVERNANCA.md`
```
diff --git a/GOVERNANCA.md b/GOVERNANCA.md
index 8d1e39a..1513acd 100644
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
@@ -88,25 +88,18 @@ adequado ao seu custo — a coluna *Modelo* é a tabela vinculante do **modelo p
 | Papel | Modelo | Responde por | Não faz |
 |---|---|---|---|
 | **Dono / gerente** | humano | Última instância e **fonte da doutrina de produto**: decide o quê e o porquê, ratifica decisões (`DR-`/`DP-`), valida cada sprint (§4.5), aceita release, autoriza saída do piso de regressão (§4.4) e comando destrutivo (§7 item 13) | Não desempata, no meio de uma execução, o que o plano deveria ter decidido — a pergunta que chega até ele em execução é sintoma de plano não-pronto (§7 itens 11 e 12) |
-| **Planejamento** | O mais poderoso disponível (Opus; Fable só sob solicitação explícita do dono) | PRD, arquitetura, specs, decisões de rota e decomposição em checklists de **tarefas atômicas fechadas** (G-PLANREADY, §7 item 11), cada uma com objetivo, arquivos-alvo, verificação e critério de pronto; **o dimensionamento de cada tarefa** sob a *Diretriz de dimensionamento de tarefa* desta seção — coesão, autossuficiência em contexto e ocupação estimada, exercidas no recorte, não publicadas no card; **a revisão de plano, com exclusividade** — indício de que o plano precisa mudar chega aqui e só aqui, e o planejador decide por si o que for **técnico ou tático**, escalando ao dono o que for **estratégico ou alterar escopo**; **a revisão do README ao encerrar cada sprint** — tarefa nomeada do próprio plano, com o guarda executável como instrumento e o veredito do dono como aceite (G-README dever 2, §7 item 14); sprint planejada sem essa tarefa é plano incompleto; **o risco de interrupção de cada card** — plano em que um executor frio pararia por dúvida sem contingência fechada não se libera (G-NOASK, §7 item 18); **o dossiê de ato de modelo** (§3.2): o planejador não escreve a seção do modelo — devolve o dossiê de autoria junto com o plano gravado, e o de emenda em rodada de replanejamento | Não executa: não implementa, não fecha tarefa, não transforma dúvida própria em pergunta ao executor |
-| **Orquestração** | Melhor custo-benefício (Sonnet); o loop roda no contexto principal, onde o dono interrompe sem derrubar a sessão, e **para para pedir `/model`** quando a fase exige outro modelo | Conduzir um plano do começo ao fim: despachar cada tarefa ao papel competente com o dossiê fechado, rotear a linha de retorno do executor e o laudo do `reviewer` (aprovado segue, reprovado volta ao mesmo escopo, escalado sobe ao dono), registrar a telemetria medida e arquivar o resultado; roda `modelo.py check` antes de despachar e antes de fechar cada tarefa, abre o relatório e cada marco com `modelo.py show` e **despacha o modelador** ao receber um dossiê de ato de modelo (§3.2) | Não implementa, não julga a entrega — o veredito é da revisã
```
[truncado em 4000 caracteres]

### `README.md`
```
diff --git a/README.md b/README.md
index 4cf033f..59af694 100644
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
 
@@ -152,14 +154,17 @@ a leitura de quem adota (`G-README`, §10).
   história que os consumidores materializam; com a versão congelada, a criação de tag nova fica
   suspensa e as já existentes permanecem como histórico. Onde a regra mora: `GOVERNANCA.md` §10 (§13
   desta página).
-- **Plano `P-NNNN`** — o planejamento consolidado de uma rota de trabalho, em formato de checklist,
-  identificado por contador global monotônico e publicável só quando fechado. Onde a regra mora:
-  `GOVERNANCA.md` §7, item 11 (`G-PLANREADY`), e `docs/plans/_INBOX.md` como registro do contador
-  (§8 desta página).
+- **Plano `P-<n>`** — o planejamento consolidado de uma rota de trabalho, numa pasta própria
+  (`docs/plans/P-<n>-<slug>/`: `plano.md`, `estado.tsv` e os registros das tarefas), em formato de
+  checklist, identificado por contador monotônico do repositório e publicável só quando fechado. Onde a
+  regra mora: `GOVERNANCA.md` §7, item 11 (`G-PLANREADY`), e `docs/plans/_INBOX.md` como registro
+  do contador (§8 desta página).
+- **Artefato de humano mínimo** — o que o dono lê (plano, handover, diário) é o menor possível e
+  aponta para o dado de máquina em vez de repeti-lo. Onde a regra mora: `GOVERNANCA.md` §4.2.
 - **Iniciativa** — o corpo de trabalho ao qual um ou mais planos servem; tem no máximo **um** plano
   vivo por vez, sempre o mais recente cuja premissa não foi contradita. Onde a regra mora:
   `.claude/skills/diario-de-obras/SKILL.md`, regra de convergência (§7 desta página).
-- **Estágio** — a subdivisão de uma iniciativa longa, cada uma com o seu plano `P-NNNN`; é con
```
[truncado em 4000 caracteres]

### `.claude/skills/diario-de-obras/SKILL.md`
```
diff --git a/.claude/skills/diario-de-obras/SKILL.md b/.claude/skills/diario-de-obras/SKILL.md
index 264e3a8..6f1f613 100644
--- a/.claude/skills/diario-de-obras/SKILL.md
+++ b/.claude/skills/diario-de-obras/SKILL.md
@@ -36,7 +36,7 @@ e tíquete avulso é arquivado, com identificação imediata do trabalho e seu s
   própria (`### <ID>` no diário) ou, para sprint que vive inteiramente em `docs/plans/P-*.md`
   (linha única no índice, sem heading no diário), numa seção do próprio plano (`## Notas de
   execução` / `## Achados da execução`) — nunca de volta na linha do índice. A célula do índice
-  fica travada em ≤ ~1-2 frases + status + ponteiro, ponto final; se um handover for editá-la
+  fica travada em ≤ ~1-2 frases + status + ponteiro, ponto final (aplicação de *Artefato de humano mínimo*, `GOVERNANCA.md` §4.2); se um handover for editá-la
   para além disso, é sinal de que falta a seção/satélite de destino — criar a seção, não apensar
   ao índice (defeito medido: `TK-DIARIO-SANEAMENTO`, célula de `SPRINT-REVEALENV` cresceu de
   ~2.5k para ~5k chars por handovers sucessivos apensando parágrafos). Mesmo mecanismo do
@@ -69,23 +69,24 @@ os transcreve sem discricionariedade; nos demais estados, autoria e materializa
 | estado | significado | o que dispara a entrada |
 |---|---|---|
 | `triage` | item registrado, ainda não avaliado quanto a entrar no backlog | registro do item na fila de entrada (`docs/plans/_INBOX.md`) |
-| `ready` | item aceito e elegível para execução | a triagem aceita o item; ou o planejamento cria a tarefa dentro de plano aprovado; ou um `blocked` é destravado |
+| `ready` | item com o trabalho escrito e elegível para execução — em tíquete, só com ao menos um card `ready` | o tíquete é aberto já com o card (*Tíquete nasce executável*, abaixo); ou o planejamento cria a tarefa dentro de plano aprovado; ou um `blocked` é destravado |
 | `blocked` | item que existe e não pode ser executado agora, com razão registrada | fato novo derruba a premissa; dependência não satisfeita; validação postergada; escalada do executor ou do laudo |
 | `in-progress` | item em execução neste exato momento | o `scrum-master` delega o item a um contexto de execução |
 | `review` | o entregável existe e aguarda aceite ou feedback de correção | o executor devolve a linha de retorno da `DP-G` |
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
+de `in-progress` → `blocked` é do executor (`DP-G`); a de `blocked` → `rev
```
[truncado em 4000 caracteres]

### `.claude/skills/passagem-de-bastao/SKILL.md`
```
diff --git a/.claude/skills/passagem-de-bastao/SKILL.md b/.claude/skills/passagem-de-bastao/SKILL.md
index 63cfc92..7d372bc 100644
--- a/.claude/skills/passagem-de-bastao/SKILL.md
+++ b/.claude/skills/passagem-de-bastao/SKILL.md
@@ -8,8 +8,9 @@ description: Maquinário de transição entre tarefas de um plano Pantonic*, na
 Procedimento da **Orquestração** (`GOVERNANCA.md` §3). Ele é o maquinário que o
 `.claude/skills/scrum-master/SKILL.md` usa entre uma tarefa e a seguinte: **superfície
 agente↔agente**, transparente para o gerente do projeto — ele não a invoca, não a lê e não a
-acompanha. Não é skill de comunicação com humano; o que chega ao dono chega pelo **relatório de
-encerramento** do `scrum-master`, e só lá.
+acompanha. Não é skill de comunicação com humano; o que chega ao dono chega pelas linhas do
+**repertório de mensagens ao gerente**, que o gancho do kit gera a partir dos eventos do loop e grava no arquivo de progresso, e pelo
+**relatório de encerramento** do `scrum-master`, e só por eles.
 
 Esta skill não implementa, não julga entrega e não substitui decisão do dono
 (`.claude/global/CLAUDE.md` Regra 8). Os "fatos estáveis" da arquitetura de cada projeto ficam no
@@ -78,9 +79,12 @@ O orquestrador monta o prompt de delegação a partir só do dossiê compacto de
 **Fonte do contexto, em ordem de preferência:** (1) dossiê pré-autorado (`sprint_plan.md`, card de
 plano) copiado verbatim, **inclusive o campo `Oração do modelo` com os sub-bullets de texto** (é a única forma de o executor ler o
 modelo — `GOVERNANCA.md` §3.2) — exceto números de aceite, ver gate abaixo; (2) **herança de contexto** da
-tarefa predecessora: precedente já pago nesta janela (âncoras re-derivadas, rota confirmada, rota
-descartada, achado já medido) colado na delegação — custo marginal zero, e é o que impede a sucessora
-de redescobrir o que a antecessora já pagou; (3) `pantonic-scout`/`context-scout` (skill
+tarefa predecessora: o bloco `=== HANDOVER DE <ID>` que o `next` imprime antes do dossiê — o campo
+`- **Handover:**` que `encerrar.py handover` registrou no card da antecessora (`Entregue`,
+`Contrato`, `Não refazer`, `Pendente`), colado verbatim na delegação quando pertinente — mais o
+precedente já pago nesta janela (âncoras re-derivadas, rota confirmada, rota descartada, achado já
+medido) — custo marginal zero, e é o que impede a sucessora de redescobrir o que a antecessora já
+pagou; (3) `pantonic-scout`/`context-scout` (skill
 `context-prep`): DESCOBERTA quando não há dossiê; DETALHE (1 pergunta fechada por spawn, paralelos)
 quando o pré-autorado referencia shapes de módulos implementados depois dele; (4) leitura direta —
 exceção declarada no ato, motivo escrito — só para Read de âncora já conhecida ou Grep de string
@@ -125,6 +129,7 @@ decisão para o executor, no modelo mais barato e sem o contexto de quem decidiu
    `GOVERNANCA.md` §3, e não vira declaração no card.
 7. Build/verify com artefato existente (`dist/`, `.exe`): o dossiê declara "não deletar o artefato de
    saída" — deleção não autorizada é ação destrutiva, não limpeza.
+8. `card_check` exit 0 sobre o card.
 
 Recusa de qualquer item do gate: **não delega**, e o que falta fechar volta ao planejamento.
 
@@ -135,11 +140,20 @@ Recusa de qualquer item do gate: **não delega**, e o que falta fechar volta ao
    exigir). Sem gate verde, o destino é `blocked` ou permanece `in-progress`, nunca `done`. No mesmo gate, `python .claude/tools/modelo.py check --plano <plano>` sai `0` ou `2` (`GOVERNANCA.md` §3.2); exit `1` mantém
    `in-progress` e escala ao consultor com o stderr.
 
-2. **Materializar o status e registrar**: `python .claude/tools/backlog.py status <ID> <estado>`
-   materializa o `status`, em qualquer estado — ato exclusivo da **orquestração**: o executor é
-   **autor** de `review` e `blocked`, e de mais nada. O registro canônico da tarefa é o **RDO**; o
-   diário guarda a linha de status que aponta para lá (`GOVERNANCA.md` §4.2, "Fronteira de
-   registr
```
[truncado em 4000 caracteres]

### `.claude/skills/scrum-master/SKILL.md`
```
diff --git a/.claude/skills/scrum-master/SKILL.md b/.claude/skills/scrum-master/SKILL.md
index 8cd7d64..d48e2fa 100644
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
 
@@ -62,7 +67,11 @@ Dez passos, nesta ordem.
   `B3`. Exit `2`: plano anterior à doutrina do modelo; segue, com a nota "sem modelo" no
   relatório. Exit `0`: segue.
 
-  Aprovados os três, e **antes** de delegar, materializar `ready` → `in-progress` no kanban
+  Quarto gate, `card_check`: `python .claude/tools/card_check.py --plano <plano> --tarefa <ID>`
+  — exit `1`: **não delega**, o stderr vai à razão e a tarefa cai em `B3`, com a nota
+  `gate do card`.
+
+  Aprovados os quatro, e **antes** de delegar, materializar `ready` → `in-progress` no kanban
   (`DP-G` item 1, consequência 3) — ato exclusivo do `scrum-master`.
 - **Saída:** tarefa materializada em `in-progress` e liberada para despacho, ou parada com o que
   falta fechar.
@@ -75,15 +84,18 @@ Dez passos, nesta ordem.
   do `P-0740`; recriá-lo se tiver sido apagado nesta máquina) e gravar
   `.claude/estado/tarefa-corrente.json` (objeto único: `tarefa`, `projeto`,
   `modelo`, `plano`, `despachado_em` ISO 8601), insumo do hook `SubagentStop` (`T55`) para
-  `docs/telemetria.tsv`. Capturar `git rev-parse HEAD` como `<ref>` (schema `DP-S`), usada no
-  passo 6 (`AUT-T5b`).
+  `docs/telemetria.tsv`. Capturar como `<ref>` (schema `DP-S`) a saída de `git stash create` —
+  instantâneo dos arquivos rastreados no despacho, que não altera árvore, índice nem a lista de
+  stash —, ou `git rev-parse HEAD` quando ela vier vazia (árvore limpa); usada no passo 6
+  (`AUT-T5b`), onde o trecho de cada alvo passa a mostrar só o que mudou desde o despacho.
 
   Invocar `pantonic-executor` com `model` **igual ao do cabeçalho** (vence o `model:` do agente),
   com o dossiê da tarefa e a instrução de devolver **uma única linha**, domínio fechado (`DP-G`
   item 2):
 
   ```
-  <tarefa> review [pendencia=<uma linha>]
+  <tarefa> review
+  <tarefa> review pendencia=<uma linha>
   <tarefa> blocked motivo=<dependencia|premissa|ferramenta> <uma linha de razão>
   ```
 
@@ -101,9 +113,11 @@ Dez passos, nesta ordem.
 - **Ação:** ler a palavra devolvida — ela **é** o `status` da tarefa (`DP-G` item 2) — e, quando
   `blocked`, o `motivo=`. Materializa **sem discricionariedade** (`DP-G` item 1): não converte
   status nem re
```
[truncado em 4000 caracteres]

### `tests/test_encerrar.py`
```
"""TK-88 (`docs/DIARIO_DE_OBRAS.md` `## TK-88`) — TF/TR de `.claude/tools/encerrar.py`, o
instrumento de fechamento de tarefa e de plano. Repositório sintético em `tmp_path` com diário,
plano legado, laudo, série de telemetria e painel do gerente; nenhum teste toca a árvore real.
Padrão de carga por caminho igual ao de `tests/test_backlog.py` (`.claude/` não é pacote)."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
_ENCERRAR_PATH = _ROOT / ".claude" / "tools" / "encerrar.py"


def _load_encerrar():
    spec = importlib.util.spec_from_file_location("encerrar", _ENCERRAR_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


encerrar = _load_encerrar()

TITULO_T1 = "Primeira tarefa do plano"
TITULO_T2 = "Segunda tarefa, cancelada"
TITULO_PLANO = "Plano alfa"

DIARIO = (
    "# Diário de Obras — Teste\n"
    "**Diretiva de priorização:** Priorize `P-0001`.\n"
    "\n"
    "<!-- fila:gerada -->\n"
    "**Fila corrente:** —\n"
    "<!-- /fila:gerada -->\n"
    "\n"
    "## Índice\n"
    "\n"
    "| ID | Título | Status | Âncora |\n"
    "|---|---|---|---|\n"
    "| P-0001 | Plano alfa | ready 0/1 | docs/plans/P-0001-alfa.md |\n"
)

PLANO = (
    f"# P-0001 — {TITULO_PLANO}\n"
    "\n"
    "**Status:** `ready` · **Prefixo das tarefas no diário:** `ALF-T<n>`\n"
    "\n"
    "## 5. Tarefas\n"
    "\n"
    f"### ALF-T1 — {TITULO_T1} [Sonnet · classe implementacao]\n"
    "- **Status:** `{status_t1}` · 2026-09-20\n"
    "- **Objetivo:** entregar a primeira coisa.\n"
    "- **Arquivos-alvo:** `a.py`.\n"
    "- **Verificação:** `pytest -q`.\n"
    "- **Pronto quando:** o teste passa.\n"
    "\n"
    f"### ALF-T2 — {TITULO_T2} [Sonnet · classe implementacao]\n"
    "- **Status:** `cancelled` · 2026-09-20 · absorvida\n"
    "- **Objetivo:** nada.\n"
    "- **Arquivos-alvo:** `b.py`.\n"
    "- **Verificação:** nenhuma.\n"
    "- **Pronto quando:** nunca.\n"
    "\n"
    "## 8. Achados da execução\n"
    "\n"
    "- **AE-1** (`ALF-T1`, laudo, 2026-09-21) — achado antigo. **Rota:** registrado, sem ação.\n"
)

LAUDO = (
    "# Laudo — P-0001 · ALF-T1\n"
    "\n"
    "**Percentual:** 91%\n"
    "**Veredito:** ressalva\n"
    "**Dimensão bloqueante:** nenhuma\n"
    "**Recomendação:** seguir com ressalva\n"
    "**Pendência:** o teste novo não cobre o ramo vazio\n"
    "\n"
    "## Lições aprendidas na tarefa\n"
    "\n"
    "Observação qualitativa do revisor.\n"
)

TELEMETRIA = (
    "data\tprojeto\ttarefa\tmodelo\ttool_uses\ttokens_k\tduracao_s\tfonte\n"
    "2026-09-25\trepo\tALF-T1\tsonnet\t21\t77.5\t300.2\tusage\n"
    "2026-09-25\trepo\tALF-T1-revisao\topus\t9\t40.0\t120.0\tusage\n"
)

PAINEL = (
    f'Abrindo a janela do plano "{TITULO_PLANO}".\n'
    f'Tarefa "{TITULO_T1}". Passo: conferir os gates e preparar o despacho.\n'
    'Tarefa "Outra coisa de outro plano". Passo: conferir os gates e preparar o despacho.\n'
    f'Agente revisor devolveu a tarefa "{TITULO_T1}": ressalva 91%, bloqueante nenhuma.\n'
)


def _montar_repo(tmp_path: Path, status_t1: str = "review") -> Path:
    repo = tmp_path / "repo"
    (repo / "docs" / "plans").mkdir(parents=True)
    (repo / "docs" / "RDO" / "laudos").mkdir(parents=True)
    (repo / ".claude" / "estado").mkdir(parents=True)
    (repo / "docs" / "DIARIO_DE_OBRAS.md").write_text(DIARIO, encoding="utf-8")
    (repo / "docs" / "plans" / "P-0001-alfa.md").write_text(PLANO.format(status_t1=status_t1), encoding="utf-8")
    (repo / "docs" / "plans" / "_INBOX.md").write_text("**Próximo id de plano: P-0002.**\n", encoding="utf-8")
    (repo / "docs" / "RDO" / "laudos" / "P-0001-ALF-T1.md").write_text(LAUDO, encoding="utf-8")
    (repo / "docs" / "telemetria.tsv").write_text(TELEMETRIA, encoding="utf-8")
    (repo / ".claude" / "estado" / "progresso.txt").write_text(PAINEL, encoding="utf-8")
    return repo

```
[truncado em 4000 caracteres]

### `tests/test_rdo.py`
```
diff --git a/tests/test_rdo.py b/tests/test_rdo.py
index fbcc7fc..6dc4310 100644
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

### `tests/test_backlog.py`
```
diff --git a/tests/test_backlog.py b/tests/test_backlog.py
index efe187a..48b7964 100644
--- a/tests/test_backlog.py
+++ b/tests/test_backlog.py
@@ -11,6 +11,7 @@ para `tmp_path` — nunca contra o repositório real (`docs/DIARIO_DE_OBRAS.md`
 insumo, nunca alvo desta suíte)."""
 from __future__ import annotations
 
+import datetime
 import hashlib
 import importlib.util
 import io
@@ -35,6 +36,7 @@ _FIXTURE_CORPUS = _FIXTURES / "corpus"
 _FIXTURE_CONTADOR_INBOX = _FIXTURES / "contador_inbox"
 _FIXTURE_CITACAO_SECAO = _FIXTURES / "citacao_secao"
 _FIXTURE_CANDIDATO_A_FECHAMENTO = _FIXTURES / "candidato_a_fechamento"
+_FIXTURE_PASTA = _FIXTURES / "pasta"
 
 
 def _load_backlog():
@@ -74,6 +76,7 @@ def _montar_raiz_hook(base: Path, nome: str, fonte_hook: str) -> Path:
     tools_dir.mkdir(parents=True)
     (tools_dir / "backlog_hook.py").write_text(fonte_hook, encoding="utf-8")
     shutil.copy2(_BACKLOG_PATH, tools_dir / "backlog.py")
+    shutil.copy2(_BACKLOG_PATH.parent / "caminhos.py", tools_dir / "caminhos.py")
     return raiz
 
 
@@ -198,6 +201,182 @@ def test_tf_check_verde_sem_violacoes(tmp_path):
     assert violacoes == []
 
 
+# --------------------------------------------------------------------------- #
+# TF/TR C-15 (EBK-T1) — tíquete vivo (status fora de done/cancelled/superseded) sem
+# subtarefa. Fixture `verde`: TK-1 tem TK-1a (sem C-15); removendo a subtarefa, TK-1 fica
+# vivo e sem filho — acusa C-15 nomeando TK-1. Tíquete terminal sem subtarefa não é acusado.
+# --------------------------------------------------------------------------- #
+
+
+def _remover_tk1a_verde(repo: Path) -> None:
+    diario_path = repo / "docs" / "DIARIO_DE_OBRAS.md"
+    linhas = diario_path.read_text(encoding="utf-8").splitlines()
+    idx = linhas.index("### TK-1a — Sub da base [Sonnet · classe mecanica]")
+    fim = idx + 2  # header da subtarefa + linha de Status dela
+    if idx > 0 and linhas[idx - 1] == "":
+        idx -= 1
+    del linhas[idx:fim]
+    diario_path.write_text("\n".join(linhas) + "\n", encoding="utf-8")
+
+
+def test_tf_c15_par_tiquete_vivo_sem_subtarefa(tmp_path):
+    backlog = _load_backlog()
+
+    repo_com = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo_com")
+    violacoes_com = backlog.check(backlog.carregar(repo_com))
+    assert not any(v.codigo == "C-15" for v in violacoes_com)
+
+    repo_sem = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo_sem")
+    _remover_tk1a_verde(repo_sem)
+    violacoes_sem = backlog.check(backlog.carregar(repo_sem))
+    c15 = [v for v in violacoes_sem if v.codigo == "C-15"]
+    assert len(c15) == 1
+    assert "TK-1" in c15[0].texto
+
+
+def test_tf_c15_tiquete_cancelled_sem_subtarefa_nao_acusa(tmp_path):
+    backlog = _load_backlog()
+    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
+    _remover_tk1a_verde(repo)
+    _mudar_linha_unica(
+        repo,
+        "docs/DIARIO_DE_OBRAS.md",
+        "| TK-1 | Tiquete base | ready | docs/DIARIO_DE_OBRAS.md#tk-1 |",
+        "| TK-1 | Tiquete base | cancelled | docs/DIARIO_DE_OBRAS.md#tk-1 |",
+    )
+    _mudar_linha_unica(
+        repo,
+        "docs/DIARIO_DE_OBRAS.md",
+        "- **Status:** `ready` · 2026-01-01",
+        "- **Status:** `cancelled` · 2026-01-01",
+    )
+
+    violacoes = backlog.check(backlog.carregar(repo))
+    assert not any(v.codigo == "C-15" for v in violacoes)
+
+
+# --------------------------------------------------------------------------- #
+# TF C-16 (EBK-T2) — a leitura de dossiê do `rdo.py` (`extrair_dossie`, leitura estrita:
+# esquema_legado=False, modelo_legado=None, classe_legado=None) confronta todo card vivo
+# (ready/in-progress/review); recusa vira C-16 com a mensagem da própria leitura, sem
+# reimplementar a gramática (propriedade 1). Card done/cancelled/blocked não é lido
+# (propriedade 2). Fixture `verde`: TK-1a nasce sem campo nenhum — os quatro obrigatórios
+# (Objetivo/Arquivos-alvo/Verificação/Pronto quando) entram na cópia, logo abaixo do Status.
+
```
[truncado em 4000 caracteres]

### `tests/test_progresso_hook.py`
```
"""TLG-T3 (`docs/plans/P-0748-tela-do-gerente.md` `### TLG-T3b`) — TFs de
`.claude/tools/progresso_hook.py`: ganchos `PreToolUse`/`PostToolUse`/`UserPromptSubmit`/`Stop`
que geram, a cada evento de transição do loop, a frase do repertório `FRASES` e a gravam em
`.claude/estado/progresso.txt`, uma por linha, na ordem em que o loop as atravessa.

Padrão de carga do módulo idêntico a `tests/test_modelo.py:35,53-54` (`.claude/` não é pacote
importável).
"""
from __future__ import annotations

import importlib.util
import json
import os
import sys
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
_PROGRESSO_HOOK_PATH = _ROOT / ".claude" / "tools" / "progresso_hook.py"


def _load_progresso_hook():
    spec = importlib.util.spec_from_file_location("progresso_hook", _PROGRESSO_HOOK_PATH)
    modulo = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = modulo
    spec.loader.exec_module(modulo)
    return modulo


progresso_hook = _load_progresso_hook()


def P(**k):
    return {
        "session_id": "s1",
        "transcript_path": str(Path("t.jsonl")),
        **k,
    }


@pytest.fixture
def raiz(tmp_path):
    plans = tmp_path / "docs" / "plans"
    plans.mkdir(parents=True)
    (plans / "P-9999-teste.md").write_text(
        "# P-9999 — Plano de teste\n"
        "\n"
        "### TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
        "### TLG-T10 — Outro título [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer y.\n",
        encoding="utf-8",
    )
    (tmp_path / "docs" / "DIARIO_DE_OBRAS.md").write_text(
        "# Diário de Obras — Teste\n"
        "## TK-99 — Tíquete de teste\n"
        "### TK-99a — Card do tíquete [Sonnet · classe mecanica]\n"
        "- **Objetivo:** Fazer z.\n",
        encoding="utf-8",
    )
    return tmp_path


@pytest.fixture
def estado(tmp_path):
    return tmp_path / "estado"


def progresso(estado):
    arq = estado / "progresso.txt"
    if not arq.exists():
        return []
    return arq.read_text(encoding="utf-8").splitlines()


def payload_next(resp_texto, session_id="s1", transcript_path=None):
    p = P(
        hook_event_name="PostToolUse",
        tool_name="Bash",
        tool_input={"command": "python .claude/tools/backlog.py next"},
        tool_response={"stdout": resp_texto},
        session_id=session_id,
    )
    if transcript_path is not None:
        p["transcript_path"] = transcript_path
    return p


def rodar(payload, estado, raiz):
    return progresso_hook.main(entrada=json.dumps(payload), estado=estado, raiz=raiz)


# --- TF-GER-1 -----------------------------------------------------------------------


def test_tf_ger_1_texto_da_resposta():
    f = progresso_hook.texto_da_resposta
    assert f("a\nb") == "a\nb"
    assert f({"stdout": "a\nb"}) == "a\nb"
    assert f({"content": [{"type": "text", "text": "a"}, {"type": "text", "text": "b"}]}) == "a\nb"
    assert f([{"type": "text", "text": "a"}, {"type": "text", "text": "b"}]) == "a\nb"
    assert f(None) == ""
    assert f({"x": 1}) == '{"x": 1}'
    assert f({"content": []}) == ""
    assert f([]) == ""
    assert f({"content": [{"type": "image"}]}) == ""


# --- TF-GER-2 -------------------------------------------------------------------------


def test_tf_ger_2_tarefa_escolhida_primeira_da_sessao(estado, raiz):
    payload = payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    )
    assert rodar(payload, estado, raiz) == 0
    assert progresso(estado) == [
        'Abrindo a janela do plano "Plano de teste".',
        'Tarefa "Um título de teste". Passo: conferir os gates e preparar o despacho.',
    ]
    estado_loop = json.loads((estado / progresso_hook.ESTADO_ARQ).read_text(encoding="utf-8"))
    assert estado_loop["tarefa"] == "TLG-T9"
    assert estado_loop["titulo"] == "Um título de teste"
    assert estado_loop["obj
```
[truncado em 4000 caracteres]

## Medida do executor
- ausente: docs\RDO\evidencia\DIARIO_DE_OBRAS-TK-88a-medida.json não existe

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
