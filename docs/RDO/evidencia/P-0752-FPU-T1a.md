# Evidência de revisão — P-0752 FPU-T1a

## Diff (`git diff --stat`)
```
.claude/README.md                                  |    7 +-
 .claude/agents/pantonic-consultant.md              |   43 +-
 .claude/agents/pantonic-executor.md                |   11 +-
 .claude/agents/pantonic-fora-da-caixa.md           |    2 +-
 .claude/agents/pantonic-model-designer.md          |   70 +-
 .claude/agents/pantonic-planner.md                 |  214 +-
 .claude/agents/pantonic-reviewer.md                |   10 +-
 .claude/checks/kit_check.ps1                       |   39 +-
 .claude/global/CLAUDE.md                           |   67 +-
 .../hooks/modelo_por_fase_userpromptsubmit.py      |   13 +-
 .claude/projecoes.json                             |   38 +
 .claude/skills/bootstrap-pantonic/SKILL.md         |    6 +-
 .claude/skills/diario-de-obras/SKILL.md            |  156 +-
 .claude/skills/entrega-de-encerramento/SKILL.md    |    2 +-
 .claude/skills/modelo-por-fase/SKILL.md            |   26 +-
 .claude/skills/passagem-de-bastao/SKILL.md         |   52 +-
 .claude/skills/redacao-doc/SKILL.md                |    3 +-
 .claude/skills/scrum-master/SKILL.md               |  214 +-
 .claude/tools/backlog.py                           |  423 ++-
 .claude/tools/backlog_hook.py                      |   14 +-
 .claude/tools/card_check.py                        |  403 ++-
 .claude/tools/modelo.py                            |   39 +-
 .claude/tools/rdo.py                               |  172 +-
 .claude/tools/rdo_template.md                      |   10 +
 .claude/tools/review_evidence.py                   |  151 +-
 GOVERNANCA.md                                      |  386 ++-
 README.md                                          |  195 +-
 docs/CUSTO_DO_PICKUP.md                            |  171 +
 docs/DIARIO_DE_OBRAS.md                            | 3340 ++++++++++++++++++--
 docs/DIARIO_HISTORICO.md                           |  154 +
 docs/DOC_MAP.md                                    |  110 +-
 docs/RDO/INDEX.md                                  |  109 +
 docs/RESIDENCIA_DOUTRINA.md                        |    4 +-
 docs/RUBRICA_DE_REVISAO.md                         |   25 +-
 docs/consultant-spec.md                            |   75 +-
 docs/plans/P-0741-modelo-conceitual.md             |    8 +-
 docs/plans/P-0745-planejador-modelo-operacao.md    | 1584 +++++++++-
 docs/plans/_INBOX.md                               |    3 +-
 docs/plans/_INBOX_HISTORICO.md                     |    8 +
 docs/telemetria.tsv                                |  343 ++
 .../backlog/vermelho/docs/DIARIO_DE_OBRAS.md       |    3 +
 tests/fixtures/modelo/fluxo-concluido.md           |   12 +-
 tests/fixtures/modelo/fluxo-pendente.md            |   20 +-
 tests/fixtures/modelo/fluxo-valido.md              |   12 +-
 tests/fixtures/modelo/plano-invalido-2.md          |   10 +-
 tests/fixtures/modelo/plano-invalido.md            |   12 +-
 tests/fixtures/modelo/plano-sem-cabecalho.md       |    8 +-
 tests/fixtures/modelo/plano-sem-estado.md          |    8 +-
 tests/test_backlog.py                              |  672 ++++
 tests/test_card_check.py                           |  168 +
 tests/test_materializar.py                         |    2 +-
 tests/test_modelo.py                               |  143 +-
 tests/test_rdo.py                                  |  284 +-
 tests/test_review_evidence.py                      |  237 +-
 54 files changed, 9262 insertions(+), 1029 deletions(-)
```

## Arquivos tocados
- `.claude/checks/frontmatter_yaml.py` — atribuição: alheio; estado git: `??`
- `.claude/skills/mensagem-ao-dono/SKILL.md` — atribuição: alheio; estado git: `??`
- `.claude/tools/caminhos.py` — atribuição: alheio; estado git: `??`
- `.claude/tools/encerrar.py` — atribuição: alheio; estado git: `??`
- `.claude/tools/progresso_hook.py` — atribuição: alheio; estado git: `??`
- `docs/ACIONAMENTOS_CONSULTOR.tsv` — atribuição: alheio; estado git: `??`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
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
- `docs/RDO/P-0752-FPU-T2-o-gate-do-card-roda-no-ensaio-do-planejador-e-no-despacho-do.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T3-toda-ancora-de-arquivo-e-linha-do-card-leva-o-literal-e-o-ga.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T5-o-executor-devolve-a-medida-como-arquivo-e-a-evidencia-a-inc.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T5a-o-executor-o-revisor-e-o-loop-falam-do-arquivo-de-medida.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-68a.md` — atribuição: alheio; estado git: `??`
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
- `docs/RDO/evidencia/P-0752-FPU-T2.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T3.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T5.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T5a-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0752-FPU-T5a.md` — atribuição: alheio; estado git: `??`
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
- `docs/RDO/laudos/P-0752-FPU-T1.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T2.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T3.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T5.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0752-FPU-T5a.md` — atribuição: alheio; estado git: `??`
- `docs/planner-spec.md` — atribuição: alheio; estado git: `??`
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
- `docs/plans/_VEREDITO-procedimentos-2026-09-22.md` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/backlog/pasta/docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/estado.tsv` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/plano.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/pasta/docs/plans/_INBOX.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/card_check/alvo.txt` — atribuição: alheio; estado git: `??`
- `tests/fixtures/card_check/plano-ancoras.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/card_check/plano-corpus.md` — atribuição: da entrega; estado git: `??`
- `tests/fixtures/modelo/plano-com-lastro.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-sem-lastro.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-terminal-sem-lastro.md` — atribuição: alheio; estado git: `??`
- `tests/test_caminhos.py` — atribuição: alheio; estado git: `??`
- `tests/test_card_check.py` — atribuição: da entrega; estado git: ` M`
- `tests/test_doutrina_unidade.py` — atribuição: alheio; estado git: `??`
- `tests/test_encerrar.py` — atribuição: alheio; estado git: `??`
- `tests/test_fixtures_higiene.py` — atribuição: alheio; estado git: `??`
- `tests/test_frontmatter_yaml.py` — atribuição: alheio; estado git: `??`
- `tests/test_global_claude.py` — atribuição: alheio; estado git: `??`
- `tests/test_kit_check.py` — atribuição: alheio; estado git: `??`
- `tests/test_progresso_hook.py` — atribuição: alheio; estado git: `??`

## Escopo
- Recorte: desde `1a1ec9dfd118e45164a7d768c78dee661722bc7d`
- Arquivos-alvo declarados: `tests/fixtures/card_check/plano-corpus.md`, `tests/test_card_check.py`
- Arquivos tocados: `.claude/checks/frontmatter_yaml.py`, `.claude/skills/mensagem-ao-dono/SKILL.md`, `.claude/tools/caminhos.py`, `.claude/tools/encerrar.py`, `.claude/tools/progresso_hook.py`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/DIARIO_DE_OBRAS.md`, `docs/FALHAS_COMUNICACAO.tsv`, `docs/OPERACOES_AS_IS.md`, `docs/OPERACOES_AS_IS_P-0745.md`, `docs/OPERACOES_AS_IS_P-0746.md`, `docs/OPERACOES_AS_IS_P-0747.md`, `docs/OPERACOES_AS_IS_P-0748.md`, `docs/OPERACOES_AS_IS_P-0749.md`, `docs/OPERACOES_AS_IS_P-0750.md`, `docs/OPERACOES_AS_IS_P-0751.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65a-check-recusa-id-de-depende-de-que-nao-e-item.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65b-o-ponto-de-carga-escreve-em-utf-8-antes-de-argparse-abrir-a.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65c-o-verbo-diretiva-nao-descarta-id-em-silencio.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65d-os-dois-depende-de-do-diario-voltam-a-gramatica.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65e-o-ramo-concatenado-do-aviso-de-diretiva-ganha-teste.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-66a-o-atribuidor-so-casa-tarefa-ja-despachada.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-68a-os-controles-1-1-e-1-2-da-regra-1-entram-na-copia-canonica-d.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-74a-o-alvo-diretorio-de-outra-tarefa-casa-por-prefixo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-74b-modelo-py-recusa-limpo-o-alvo-que-nao-e-arquivo-de-plano.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-76a-as-tabelas-do-modelo-em-frases-curtas-para-o-dono.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-77a-o-validate-recusa-frontmatter-de-agente-ou-skill-que-o-yaml.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78a-o-loop-nao-para-para-rebaixar-o-modelo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78b-a-regua-do-card-aprende-as-tres-licoes-da-janela.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78c-a-evidencia-mede-so-o-que-mudou-desde-o-despacho.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78d-a-doutrina-e-o-readme-deixam-de-mandar-parar-para-rebaixar-o.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-79a-a-prosa-depois-da-linha-de-retorno-e-descartada-por-regra-na.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-82a-rdo-py-escreve-em-utf-8-antes-de-argparse-abrir-a-boca.md`, `docs/RDO/P-0741-MC-T5-o-readme-explica-o-modelo-a-afericao-sobre-o-proprio-plano-e.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0745-PLN-T4a-o-ponteiro-sobrevivente-da-tabela-aposentada-nos-fatos-estav.md`, `docs/RDO/P-0745-PLN-T5-o-modelador-diante-do-plano-sem-cards-e-o-lastro-que-e-do-pl.md`, `docs/RDO/P-0745-PLN-T5a-a-frase-que-governa-o-gate-do-modelador-e-a-enumeracao-que-e.md`, `docs/RDO/P-0745-PLN-T6-a-especificacao-do-agente-de-planejamento.md`, `docs/RDO/P-0745-PLN-T7-o-indice-de-documentos-e-a-revisao-do-readme.md`, `docs/RDO/P-0745-PLN-T7a-o-readme-deixa-de-defender-a-regua-que-ele-mesmo-aposenta.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/P-0747-CON-T1-o-consultor-entra-na-doutrina-de-governanca.md`, `docs/RDO/P-0747-CON-T2-a-definicao-de-conduta-do-consultor-sem-estatuto-provisorio.md`, `docs/RDO/P-0747-CON-T2a-corretivo-da-op-2-o-agente-descreve-o-cenario-persistido-e-l.md`, `docs/RDO/P-0747-CON-T2b-corretivo-da-op-2-o-agente-nomeia-a-recusa-do-impedimento-im.md`, `docs/RDO/P-0747-CON-T3-o-loop-leva-toda-parada-ao-consultor.md`, `docs/RDO/P-0747-CON-T3a-corretivo-da-op-3-a-parada-e-a-mesma-em-todas-as-regras-que.md`, `docs/RDO/P-0747-CON-T3b-corretivo-da-op-3-com-estrategico-o-loop-para-sem-executar-a.md`, `docs/RDO/P-0747-CON-T3c-corretivo-da-op-3-com-estrategico-a-rota-planejador-executa.md`, `docs/RDO/P-0747-CON-T3d-corretivo-da-op-3-o-loop-redespacha-sem-retentativa-o-card-c.md`, `docs/RDO/P-0747-CON-T4-a-forma-efemera-com-cenario-persistido.md`, `docs/RDO/P-0747-CON-T4a-corretivo-da-op-4-a-queda-de-uma-instancia-do-consultor-nao.md`, `docs/RDO/P-0747-CON-T5-o-outro-lado-da-fronteira-nas-definicoes-de-conduta.md`, `docs/RDO/P-0747-CON-T5a-corretivo-da-op-5-o-diario-e-a-regra-8-dizem-o-que-a-triagem.md`, `docs/RDO/P-0747-CON-T6-a-especificacao-vira-lastro-medido.md`, `docs/RDO/P-0747-CON-T6a-corretivo-da-op-6-a-spec-nao-prevalece-sobre-o-bloco-a.md`, `docs/RDO/P-0747-CON-T7-a-medida-do-piloto-da-forma-efemera.md`, `docs/RDO/P-0747-CON-T7a-corretivo-da-op-7-o-veredito-declara-o-modelo-das-instancias.md`, `docs/RDO/P-0747-CON-T8-a-porta-de-entrada-e-a-descricao-do-agente.md`, `docs/RDO/P-0747-CON-T8a-corretivo-da-op-8-a-description-volta-ao-yaml-que-o-harness.md`, `docs/RDO/P-0748-TLG-T1-a-sonda-de-viabilidade-diante-do-dono.md`, `docs/RDO/P-0748-TLG-T2-o-repertorio-de-mensagens-na-skill-do-loop.md`, `docs/RDO/P-0748-TLG-T2a-o-repertorio-deixa-de-citar-o-comando-que-nao-vai-existir.md`, `docs/RDO/P-0748-TLG-T2b-o-repertorio-como-tabela-de-eventos-a-skill-diz-o-que-a-func.md`, `docs/RDO/P-0748-TLG-T3-o-gancho-que-grava-o-arquivo-de-progresso.md`, `docs/RDO/P-0748-TLG-T3a-a-captura-do-payload-dos-ganchos-o-que-a-funcao-vai-ler.md`, `docs/RDO/P-0748-TLG-T3b-a-funcao-que-gera-a-linha-do-stream-a-cada-evento-do-loop.md`, `docs/RDO/P-0748-TLG-T3c-o-painel-nao-perde-linha-e-nao-afirma-o-que-nao-aconteceu.md`, `docs/RDO/P-0748-TLG-T3d-o-painel-so-diz-que-a-janela-encerrou-quando-ela-encerrou.md`, `docs/RDO/P-0748-TLG-T3e-o-painel-diz-so-o-que-o-gancho-ve-o-modelo-mostrado-e-o-cons.md`, `docs/RDO/P-0748-TLG-T3f-o-estado-do-gancho-nao-guarda-chave-que-ninguem-le.md`, `docs/RDO/P-0748-TLG-T3g-o-painel-reconhece-o-retorno-do-agente-com-o-ou-o-colchete-a.md`, `docs/RDO/P-0748-TLG-T3h-o-painel-da-uma-linha-a-cada-status-do-mesmo-comando-e-a-ski.md`, `docs/RDO/P-0748-TLG-T4-o-condutor-narra-uma-linha-do-repertorio-antes-de-cada-ato-n.md`, `docs/RDO/P-0748-TLG-T4a-a-skill-deixa-de-narrar-a-transicao-chega-ao-painel-pela-fun.md`, `docs/RDO/P-0748-TLG-T5-a-porta-de-entrada-diz-como-o-dono-acompanha-a-execucao-no-p.md`, `docs/RDO/P-0748-TLG-T5a-a-celula-da-scrum-master-na-tabela-de-skills-volta-a-dizer-q.md`, `docs/RDO/P-0749-SAN-T1-o-id-e-o-caminho-do-plano-num-lugar-so.md`, `docs/RDO/P-0749-SAN-T2-o-estado-sai-do-texto-e-vai-para-o-estado-tsv.md`, `docs/RDO/P-0749-SAN-T2a-projeto-novo-com-contador-em-p-0-e-nenhum-plano-passa-no-che.md`, `docs/RDO/P-0749-SAN-T3-relato-laudo-e-evidencia-nascem-na-pasta-do-plano.md`, `docs/RDO/P-0749-SAN-T3a-a-flag-vence-tambem-no-indice-e-a-cli-anuncia-os-dois-destin.md`, `docs/RDO/P-0749-SAN-T4-a-doutrina-ensina-a-pasta-o-estado-tsv-e-a-contagem-em-zero.md`, `docs/RDO/P-0749-SAN-T5-a-regra-do-artefato-de-humano-minimo-uma-vez-so.md`, `docs/RDO/P-0749-SAN-T6-a-porta-de-entrada-descreve-a-pasta-a-tabela-e-o-texto-minim.md`, `docs/RDO/P-0749-SAN-T6a-o-glossario-diz-o-contador-como-a-regra-o-diz.md`, `docs/RDO/P-0749-SAN-T6b-as-decisoes-estruturantes-dizem-o-contador-como-a-regra-o-di.md`, `docs/RDO/P-0750-CAH-T1-a-regra-da-mensagem-legivel-ao-dono-na-doutrina-e-no-regulam.md`, `docs/RDO/P-0750-CAH-T2-o-glossario-diz-o-que-cada-familia-de-sigla-nomeia.md`, `docs/RDO/P-0750-CAH-T3-a-tabela-de-falhas-de-comunicacao-com-as-falhas-ja-medidas.md`, `docs/RDO/P-0750-CAH-T4-a-skill-da-mensagem-ao-dono.md`, `docs/RDO/P-0750-CAH-T4a-o-titulo-de-tarefa-na-skill-da-mensagem-ao-dono-para-antes-d.md`, `docs/RDO/P-0750-CAH-T5-os-textos-que-mandavam-citar-sigla-ao-dono-passam-a-mandar-o.md`, `docs/RDO/P-0751-EBK-T1-o-check-acusa-tiquete-vivo-sem-card.md`, `docs/RDO/P-0751-EBK-T10-a-regua-de-autoria-do-card-segunda-leva.md`, `docs/RDO/P-0751-EBK-T11-o-planejador-publica-o-grep-da-superficie-e-ensaia-os-cards.md`, `docs/RDO/P-0751-EBK-T12-tres-ajustes-de-regra-existente-a-devolucao-do-modelador-o-e.md`, `docs/RDO/P-0751-EBK-T13-quanto-custa-retomar-o-planejador-por-mensagem.md`, `docs/RDO/P-0751-EBK-T13a-a-razao-da-regra-da-retomada-sai-do-custo-de-partida-nao-da.md`, `docs/RDO/P-0751-EBK-T14-a-rodada-de-revisao-de-guardrails-pendente-desde-2026-08-08.md`, `docs/RDO/P-0751-EBK-T2-o-check-confronta-o-card-com-o-rdo-py-e-o-piso-com-o-corpus.md`, `docs/RDO/P-0751-EBK-T3-o-next-projeta-o-colchete-do-cabecalho-inteiro.md`, `docs/RDO/P-0751-EBK-T4-rdo-py-close-recusa-tarefa-que-nao-esta-done.md`, `docs/RDO/P-0751-EBK-T5-o-kit-check-conta-defeito-nao-linha.md`, `docs/RDO/P-0751-EBK-T5a-o-kit-check-nao-conta-o-sumario-do-materializar-e-detalha-so.md`, `docs/RDO/P-0751-EBK-T6-nenhuma-fixture-carrega-nome-que-o-harness-descobre.md`, `docs/RDO/P-0751-EBK-T7-a-doutrina-do-teste-que-discrimina-e-da-medida-publicada.md`, `docs/RDO/P-0751-EBK-T8-a-vigencia-do-modelo-o-desfecho-do-drift-recusado-e-o-lastro.md`, `docs/RDO/P-0751-EBK-T9-uma-operacao-uma-oracao.md`, `docs/RDO/P-0752-FPU-T1-o-gate-do-card-le-a-forma-do-corpus-e-deixa-de-produzir-item.md`, `docs/RDO/P-0752-FPU-T2-o-gate-do-card-roda-no-ensaio-do-planejador-e-no-despacho-do.md`, `docs/RDO/P-0752-FPU-T3-toda-ancora-de-arquivo-e-linha-do-card-leva-o-literal-e-o-ga.md`, `docs/RDO/P-0752-FPU-T5-o-executor-devolve-a-medida-como-arquivo-e-a-evidencia-a-inc.md`, `docs/RDO/P-0752-FPU-T5a-o-executor-o-revisor-e-o-loop-falam-do-arquivo-de-medida.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-68a.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0745-PLN-T4a.md`, `docs/RDO/evidencia/P-0745-PLN-T5.md`, `docs/RDO/evidencia/P-0745-PLN-T5a.md`, `docs/RDO/evidencia/P-0745-PLN-T6.md`, `docs/RDO/evidencia/P-0745-PLN-T7.md`, `docs/RDO/evidencia/P-0745-PLN-T7a.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/P-0747-CON-T1.md`, `docs/RDO/evidencia/P-0747-CON-T2.md`, `docs/RDO/evidencia/P-0747-CON-T2a.md`, `docs/RDO/evidencia/P-0747-CON-T2b.md`, `docs/RDO/evidencia/P-0747-CON-T3.md`, `docs/RDO/evidencia/P-0747-CON-T3a.md`, `docs/RDO/evidencia/P-0747-CON-T3b.md`, `docs/RDO/evidencia/P-0747-CON-T3c.md`, `docs/RDO/evidencia/P-0747-CON-T3d.md`, `docs/RDO/evidencia/P-0747-CON-T4.md`, `docs/RDO/evidencia/P-0747-CON-T4a.md`, `docs/RDO/evidencia/P-0747-CON-T5.md`, `docs/RDO/evidencia/P-0747-CON-T5a.md`, `docs/RDO/evidencia/P-0747-CON-T6.md`, `docs/RDO/evidencia/P-0747-CON-T6a.md`, `docs/RDO/evidencia/P-0747-CON-T7.md`, `docs/RDO/evidencia/P-0747-CON-T7a.md`, `docs/RDO/evidencia/P-0747-CON-T8.md`, `docs/RDO/evidencia/P-0747-CON-T8a.md`, `docs/RDO/evidencia/P-0748-TLG-T1.md`, `docs/RDO/evidencia/P-0748-TLG-T2.md`, `docs/RDO/evidencia/P-0748-TLG-T2a.md`, `docs/RDO/evidencia/P-0748-TLG-T2b.md`, `docs/RDO/evidencia/P-0748-TLG-T3.md`, `docs/RDO/evidencia/P-0748-TLG-T3a.md`, `docs/RDO/evidencia/P-0748-TLG-T3b.md`, `docs/RDO/evidencia/P-0748-TLG-T3c.md`, `docs/RDO/evidencia/P-0748-TLG-T3d.md`, `docs/RDO/evidencia/P-0748-TLG-T3e.md`, `docs/RDO/evidencia/P-0748-TLG-T3f.md`, `docs/RDO/evidencia/P-0748-TLG-T3g.md`, `docs/RDO/evidencia/P-0748-TLG-T3h.md`, `docs/RDO/evidencia/P-0748-TLG-T4.md`, `docs/RDO/evidencia/P-0748-TLG-T4a.md`, `docs/RDO/evidencia/P-0748-TLG-T5.md`, `docs/RDO/evidencia/P-0748-TLG-T5a.md`, `docs/RDO/evidencia/P-0749-SAN-T1.md`, `docs/RDO/evidencia/P-0749-SAN-T2.md`, `docs/RDO/evidencia/P-0749-SAN-T2a.md`, `docs/RDO/evidencia/P-0749-SAN-T3.md`, `docs/RDO/evidencia/P-0749-SAN-T3a.md`, `docs/RDO/evidencia/P-0749-SAN-T4.md`, `docs/RDO/evidencia/P-0749-SAN-T5.md`, `docs/RDO/evidencia/P-0749-SAN-T6.md`, `docs/RDO/evidencia/P-0749-SAN-T6a.md`, `docs/RDO/evidencia/P-0749-SAN-T6b.md`, `docs/RDO/evidencia/P-0750-CAH-T1.md`, `docs/RDO/evidencia/P-0750-CAH-T2.md`, `docs/RDO/evidencia/P-0750-CAH-T3.md`, `docs/RDO/evidencia/P-0750-CAH-T4.md`, `docs/RDO/evidencia/P-0750-CAH-T4a.md`, `docs/RDO/evidencia/P-0750-CAH-T5.md`, `docs/RDO/evidencia/P-0751-EBK-T1.md`, `docs/RDO/evidencia/P-0751-EBK-T10.md`, `docs/RDO/evidencia/P-0751-EBK-T11.md`, `docs/RDO/evidencia/P-0751-EBK-T12.md`, `docs/RDO/evidencia/P-0751-EBK-T13.md`, `docs/RDO/evidencia/P-0751-EBK-T13a.md`, `docs/RDO/evidencia/P-0751-EBK-T14.md`, `docs/RDO/evidencia/P-0751-EBK-T2.md`, `docs/RDO/evidencia/P-0751-EBK-T3.md`, `docs/RDO/evidencia/P-0751-EBK-T4.md`, `docs/RDO/evidencia/P-0751-EBK-T5.md`, `docs/RDO/evidencia/P-0751-EBK-T5a.md`, `docs/RDO/evidencia/P-0751-EBK-T6.md`, `docs/RDO/evidencia/P-0751-EBK-T7.md`, `docs/RDO/evidencia/P-0751-EBK-T8.md`, `docs/RDO/evidencia/P-0751-EBK-T9.md`, `docs/RDO/evidencia/P-0752-FPU-T1.md`, `docs/RDO/evidencia/P-0752-FPU-T1a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T2.md`, `docs/RDO/evidencia/P-0752-FPU-T3.md`, `docs/RDO/evidencia/P-0752-FPU-T5.md`, `docs/RDO/evidencia/P-0752-FPU-T5a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T5a.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/RDO/evidencia/TK-65-TK-65a.md`, `docs/RDO/evidencia/TK-65-TK-65b.md`, `docs/RDO/evidencia/TK-65-TK-65c.md`, `docs/RDO/evidencia/TK-65-TK-65d.md`, `docs/RDO/evidencia/TK-65-TK-65e.md`, `docs/RDO/evidencia/TK-66-TK-66a.md`, `docs/RDO/evidencia/TK-74-TK-74a.md`, `docs/RDO/evidencia/TK-74-TK-74b.md`, `docs/RDO/evidencia/TK-76-TK-76a.md`, `docs/RDO/evidencia/TK-77-TK-77a.md`, `docs/RDO/evidencia/TK-78-TK-78a.md`, `docs/RDO/evidencia/TK-78-TK-78b.md`, `docs/RDO/evidencia/TK-78-TK-78c.md`, `docs/RDO/evidencia/TK-78-TK-78d.md`, `docs/RDO/evidencia/TK-79-TK-79a.md`, `docs/RDO/evidencia/TK-82-TK-82a.md`, `docs/RDO/laudos/P-0752-FPU-T1.md`, `docs/RDO/laudos/P-0752-FPU-T2.md`, `docs/RDO/laudos/P-0752-FPU-T3.md`, `docs/RDO/laudos/P-0752-FPU-T5.md`, `docs/RDO/laudos/P-0752-FPU-T5a.md`, `docs/planner-spec.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/P-0747-consultor-de-plano.md`, `docs/plans/P-0748-tela-do-gerente.md`, `docs/plans/P-0749-saneamento-artefatos.md`, `docs/plans/P-0750-comunicacao-agente-humano.md`, `docs/plans/P-0751-esgotar-backlog.md`, `docs/plans/P-0752-fato-no-ponto-de-uso.md`, `docs/plans/_CAMPANHA-P-0748.md`, `docs/plans/_CENARIO-P-0747.md`, `docs/plans/_CENARIO-P-0748.md`, `docs/plans/_CENARIO-P-0749.md`, `docs/plans/_CENARIO-P-0750.md`, `docs/plans/_CENARIO-P-0751.md`, `docs/plans/_CENARIO-P-0752.md`, `docs/plans/_CENARIO-TK-65.md`, `docs/plans/_CENARIO-TK-78.md`, `docs/plans/_VEREDITO-procedimentos-2026-09-22.md`, `docs/telemetria.tsv`, `tests/fixtures/backlog/pasta/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/estado.tsv`, `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/plano.md`, `tests/fixtures/backlog/pasta/docs/plans/_INBOX.md`, `tests/fixtures/card_check/alvo.txt`, `tests/fixtures/card_check/plano-ancoras.md`, `tests/fixtures/card_check/plano-corpus.md`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_caminhos.py`, `tests/test_card_check.py`, `tests/test_doutrina_unidade.py`, `tests/test_encerrar.py`, `tests/test_fixtures_higiene.py`, `tests/test_frontmatter_yaml.py`, `tests/test_global_claude.py`, `tests/test_kit_check.py`, `tests/test_progresso_hook.py`
- Atribuídos a outra tarefa do mesmo plano: `tests/fixtures/card_check/alvo.txt` → `FPU-T3`, `tests/fixtures/card_check/plano-ancoras.md` → `FPU-T3`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65a-check-recusa-id-de-depende-de-que-nao-e-item.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65b-o-ponto-de-carga-escreve-em-utf-8-antes-de-argparse-abrir-a.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65c-o-verbo-diretiva-nao-descarta-id-em-silencio.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65d-os-dois-depende-de-do-diario-voltam-a-gramatica.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65e-o-ramo-concatenado-do-aviso-de-diretiva-ganha-teste.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-66a-o-atribuidor-so-casa-tarefa-ja-despachada.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-68a-os-controles-1-1-e-1-2-da-regra-1-entram-na-copia-canonica-d.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-74a-o-alvo-diretorio-de-outra-tarefa-casa-por-prefixo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-74b-modelo-py-recusa-limpo-o-alvo-que-nao-e-arquivo-de-plano.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-76a-as-tabelas-do-modelo-em-frases-curtas-para-o-dono.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-77a-o-validate-recusa-frontmatter-de-agente-ou-skill-que-o-yaml.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78a-o-loop-nao-para-para-rebaixar-o-modelo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78b-a-regua-do-card-aprende-as-tres-licoes-da-janela.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78c-a-evidencia-mede-so-o-que-mudou-desde-o-despacho.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78d-a-doutrina-e-o-readme-deixam-de-mandar-parar-para-rebaixar-o.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-79a-a-prosa-depois-da-linha-de-retorno-e-descartada-por-regra-na.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-82a-rdo-py-escreve-em-utf-8-antes-de-argparse-abrir-a-boca.md`, `docs/RDO/P-0741-MC-T5-o-readme-explica-o-modelo-a-afericao-sobre-o-proprio-plano-e.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0745-PLN-T4a-o-ponteiro-sobrevivente-da-tabela-aposentada-nos-fatos-estav.md`, `docs/RDO/P-0745-PLN-T5-o-modelador-diante-do-plano-sem-cards-e-o-lastro-que-e-do-pl.md`, `docs/RDO/P-0745-PLN-T5a-a-frase-que-governa-o-gate-do-modelador-e-a-enumeracao-que-e.md`, `docs/RDO/P-0745-PLN-T6-a-especificacao-do-agente-de-planejamento.md`, `docs/RDO/P-0745-PLN-T7-o-indice-de-documentos-e-a-revisao-do-readme.md`, `docs/RDO/P-0745-PLN-T7a-o-readme-deixa-de-defender-a-regua-que-ele-mesmo-aposenta.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/P-0747-CON-T1-o-consultor-entra-na-doutrina-de-governanca.md`, `docs/RDO/P-0747-CON-T2-a-definicao-de-conduta-do-consultor-sem-estatuto-provisorio.md`, `docs/RDO/P-0747-CON-T2a-corretivo-da-op-2-o-agente-descreve-o-cenario-persistido-e-l.md`, `docs/RDO/P-0747-CON-T2b-corretivo-da-op-2-o-agente-nomeia-a-recusa-do-impedimento-im.md`, `docs/RDO/P-0747-CON-T3-o-loop-leva-toda-parada-ao-consultor.md`, `docs/RDO/P-0747-CON-T3a-corretivo-da-op-3-a-parada-e-a-mesma-em-todas-as-regras-que.md`, `docs/RDO/P-0747-CON-T3b-corretivo-da-op-3-com-estrategico-o-loop-para-sem-executar-a.md`, `docs/RDO/P-0747-CON-T3c-corretivo-da-op-3-com-estrategico-a-rota-planejador-executa.md`, `docs/RDO/P-0747-CON-T3d-corretivo-da-op-3-o-loop-redespacha-sem-retentativa-o-card-c.md`, `docs/RDO/P-0747-CON-T4-a-forma-efemera-com-cenario-persistido.md`, `docs/RDO/P-0747-CON-T4a-corretivo-da-op-4-a-queda-de-uma-instancia-do-consultor-nao.md`, `docs/RDO/P-0747-CON-T5-o-outro-lado-da-fronteira-nas-definicoes-de-conduta.md`, `docs/RDO/P-0747-CON-T5a-corretivo-da-op-5-o-diario-e-a-regra-8-dizem-o-que-a-triagem.md`, `docs/RDO/P-0747-CON-T6-a-especificacao-vira-lastro-medido.md`, `docs/RDO/P-0747-CON-T6a-corretivo-da-op-6-a-spec-nao-prevalece-sobre-o-bloco-a.md`, `docs/RDO/P-0747-CON-T7-a-medida-do-piloto-da-forma-efemera.md`, `docs/RDO/P-0747-CON-T7a-corretivo-da-op-7-o-veredito-declara-o-modelo-das-instancias.md`, `docs/RDO/P-0747-CON-T8-a-porta-de-entrada-e-a-descricao-do-agente.md`, `docs/RDO/P-0747-CON-T8a-corretivo-da-op-8-a-description-volta-ao-yaml-que-o-harness.md`, `docs/RDO/P-0748-TLG-T1-a-sonda-de-viabilidade-diante-do-dono.md`, `docs/RDO/P-0748-TLG-T2-o-repertorio-de-mensagens-na-skill-do-loop.md`, `docs/RDO/P-0748-TLG-T2a-o-repertorio-deixa-de-citar-o-comando-que-nao-vai-existir.md`, `docs/RDO/P-0748-TLG-T2b-o-repertorio-como-tabela-de-eventos-a-skill-diz-o-que-a-func.md`, `docs/RDO/P-0748-TLG-T3-o-gancho-que-grava-o-arquivo-de-progresso.md`, `docs/RDO/P-0748-TLG-T3a-a-captura-do-payload-dos-ganchos-o-que-a-funcao-vai-ler.md`, `docs/RDO/P-0748-TLG-T3b-a-funcao-que-gera-a-linha-do-stream-a-cada-evento-do-loop.md`, `docs/RDO/P-0748-TLG-T3c-o-painel-nao-perde-linha-e-nao-afirma-o-que-nao-aconteceu.md`, `docs/RDO/P-0748-TLG-T3d-o-painel-so-diz-que-a-janela-encerrou-quando-ela-encerrou.md`, `docs/RDO/P-0748-TLG-T3e-o-painel-diz-so-o-que-o-gancho-ve-o-modelo-mostrado-e-o-cons.md`, `docs/RDO/P-0748-TLG-T3f-o-estado-do-gancho-nao-guarda-chave-que-ninguem-le.md`, `docs/RDO/P-0748-TLG-T3g-o-painel-reconhece-o-retorno-do-agente-com-o-ou-o-colchete-a.md`, `docs/RDO/P-0748-TLG-T3h-o-painel-da-uma-linha-a-cada-status-do-mesmo-comando-e-a-ski.md`, `docs/RDO/P-0748-TLG-T4-o-condutor-narra-uma-linha-do-repertorio-antes-de-cada-ato-n.md`, `docs/RDO/P-0748-TLG-T4a-a-skill-deixa-de-narrar-a-transicao-chega-ao-painel-pela-fun.md`, `docs/RDO/P-0748-TLG-T5-a-porta-de-entrada-diz-como-o-dono-acompanha-a-execucao-no-p.md`, `docs/RDO/P-0748-TLG-T5a-a-celula-da-scrum-master-na-tabela-de-skills-volta-a-dizer-q.md`, `docs/RDO/P-0749-SAN-T1-o-id-e-o-caminho-do-plano-num-lugar-so.md`, `docs/RDO/P-0749-SAN-T2-o-estado-sai-do-texto-e-vai-para-o-estado-tsv.md`, `docs/RDO/P-0749-SAN-T2a-projeto-novo-com-contador-em-p-0-e-nenhum-plano-passa-no-che.md`, `docs/RDO/P-0749-SAN-T3-relato-laudo-e-evidencia-nascem-na-pasta-do-plano.md`, `docs/RDO/P-0749-SAN-T3a-a-flag-vence-tambem-no-indice-e-a-cli-anuncia-os-dois-destin.md`, `docs/RDO/P-0749-SAN-T4-a-doutrina-ensina-a-pasta-o-estado-tsv-e-a-contagem-em-zero.md`, `docs/RDO/P-0749-SAN-T5-a-regra-do-artefato-de-humano-minimo-uma-vez-so.md`, `docs/RDO/P-0749-SAN-T6-a-porta-de-entrada-descreve-a-pasta-a-tabela-e-o-texto-minim.md`, `docs/RDO/P-0749-SAN-T6a-o-glossario-diz-o-contador-como-a-regra-o-diz.md`, `docs/RDO/P-0749-SAN-T6b-as-decisoes-estruturantes-dizem-o-contador-como-a-regra-o-di.md`, `docs/RDO/P-0750-CAH-T1-a-regra-da-mensagem-legivel-ao-dono-na-doutrina-e-no-regulam.md`, `docs/RDO/P-0750-CAH-T2-o-glossario-diz-o-que-cada-familia-de-sigla-nomeia.md`, `docs/RDO/P-0750-CAH-T3-a-tabela-de-falhas-de-comunicacao-com-as-falhas-ja-medidas.md`, `docs/RDO/P-0750-CAH-T4-a-skill-da-mensagem-ao-dono.md`, `docs/RDO/P-0750-CAH-T4a-o-titulo-de-tarefa-na-skill-da-mensagem-ao-dono-para-antes-d.md`, `docs/RDO/P-0750-CAH-T5-os-textos-que-mandavam-citar-sigla-ao-dono-passam-a-mandar-o.md`, `docs/RDO/P-0751-EBK-T1-o-check-acusa-tiquete-vivo-sem-card.md`, `docs/RDO/P-0751-EBK-T10-a-regua-de-autoria-do-card-segunda-leva.md`, `docs/RDO/P-0751-EBK-T11-o-planejador-publica-o-grep-da-superficie-e-ensaia-os-cards.md`, `docs/RDO/P-0751-EBK-T12-tres-ajustes-de-regra-existente-a-devolucao-do-modelador-o-e.md`, `docs/RDO/P-0751-EBK-T13-quanto-custa-retomar-o-planejador-por-mensagem.md`, `docs/RDO/P-0751-EBK-T13a-a-razao-da-regra-da-retomada-sai-do-custo-de-partida-nao-da.md`, `docs/RDO/P-0751-EBK-T14-a-rodada-de-revisao-de-guardrails-pendente-desde-2026-08-08.md`, `docs/RDO/P-0751-EBK-T2-o-check-confronta-o-card-com-o-rdo-py-e-o-piso-com-o-corpus.md`, `docs/RDO/P-0751-EBK-T3-o-next-projeta-o-colchete-do-cabecalho-inteiro.md`, `docs/RDO/P-0751-EBK-T4-rdo-py-close-recusa-tarefa-que-nao-esta-done.md`, `docs/RDO/P-0751-EBK-T5-o-kit-check-conta-defeito-nao-linha.md`, `docs/RDO/P-0751-EBK-T5a-o-kit-check-nao-conta-o-sumario-do-materializar-e-detalha-so.md`, `docs/RDO/P-0751-EBK-T6-nenhuma-fixture-carrega-nome-que-o-harness-descobre.md`, `docs/RDO/P-0751-EBK-T7-a-doutrina-do-teste-que-discrimina-e-da-medida-publicada.md`, `docs/RDO/P-0751-EBK-T8-a-vigencia-do-modelo-o-desfecho-do-drift-recusado-e-o-lastro.md`, `docs/RDO/P-0751-EBK-T9-uma-operacao-uma-oracao.md`, `docs/RDO/P-0752-FPU-T1-o-gate-do-card-le-a-forma-do-corpus-e-deixa-de-produzir-item.md`, `docs/RDO/P-0752-FPU-T2-o-gate-do-card-roda-no-ensaio-do-planejador-e-no-despacho-do.md`, `docs/RDO/P-0752-FPU-T3-toda-ancora-de-arquivo-e-linha-do-card-leva-o-literal-e-o-ga.md`, `docs/RDO/P-0752-FPU-T5-o-executor-devolve-a-medida-como-arquivo-e-a-evidencia-a-inc.md`, `docs/RDO/P-0752-FPU-T5a-o-executor-o-revisor-e-o-loop-falam-do-arquivo-de-medida.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-68a.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0745-PLN-T4a.md`, `docs/RDO/evidencia/P-0745-PLN-T5.md`, `docs/RDO/evidencia/P-0745-PLN-T5a.md`, `docs/RDO/evidencia/P-0745-PLN-T6.md`, `docs/RDO/evidencia/P-0745-PLN-T7.md`, `docs/RDO/evidencia/P-0745-PLN-T7a.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/P-0747-CON-T1.md`, `docs/RDO/evidencia/P-0747-CON-T2.md`, `docs/RDO/evidencia/P-0747-CON-T2a.md`, `docs/RDO/evidencia/P-0747-CON-T2b.md`, `docs/RDO/evidencia/P-0747-CON-T3.md`, `docs/RDO/evidencia/P-0747-CON-T3a.md`, `docs/RDO/evidencia/P-0747-CON-T3b.md`, `docs/RDO/evidencia/P-0747-CON-T3c.md`, `docs/RDO/evidencia/P-0747-CON-T3d.md`, `docs/RDO/evidencia/P-0747-CON-T4.md`, `docs/RDO/evidencia/P-0747-CON-T4a.md`, `docs/RDO/evidencia/P-0747-CON-T5.md`, `docs/RDO/evidencia/P-0747-CON-T5a.md`, `docs/RDO/evidencia/P-0747-CON-T6.md`, `docs/RDO/evidencia/P-0747-CON-T6a.md`, `docs/RDO/evidencia/P-0747-CON-T7.md`, `docs/RDO/evidencia/P-0747-CON-T7a.md`, `docs/RDO/evidencia/P-0747-CON-T8.md`, `docs/RDO/evidencia/P-0747-CON-T8a.md`, `docs/RDO/evidencia/P-0748-TLG-T1.md`, `docs/RDO/evidencia/P-0748-TLG-T2.md`, `docs/RDO/evidencia/P-0748-TLG-T2a.md`, `docs/RDO/evidencia/P-0748-TLG-T2b.md`, `docs/RDO/evidencia/P-0748-TLG-T3.md`, `docs/RDO/evidencia/P-0748-TLG-T3a.md`, `docs/RDO/evidencia/P-0748-TLG-T3b.md`, `docs/RDO/evidencia/P-0748-TLG-T3c.md`, `docs/RDO/evidencia/P-0748-TLG-T3d.md`, `docs/RDO/evidencia/P-0748-TLG-T3e.md`, `docs/RDO/evidencia/P-0748-TLG-T3f.md`, `docs/RDO/evidencia/P-0748-TLG-T3g.md`, `docs/RDO/evidencia/P-0748-TLG-T3h.md`, `docs/RDO/evidencia/P-0748-TLG-T4.md`, `docs/RDO/evidencia/P-0748-TLG-T4a.md`, `docs/RDO/evidencia/P-0748-TLG-T5.md`, `docs/RDO/evidencia/P-0748-TLG-T5a.md`, `docs/RDO/evidencia/P-0749-SAN-T1.md`, `docs/RDO/evidencia/P-0749-SAN-T2.md`, `docs/RDO/evidencia/P-0749-SAN-T2a.md`, `docs/RDO/evidencia/P-0749-SAN-T3.md`, `docs/RDO/evidencia/P-0749-SAN-T3a.md`, `docs/RDO/evidencia/P-0749-SAN-T4.md`, `docs/RDO/evidencia/P-0749-SAN-T5.md`, `docs/RDO/evidencia/P-0749-SAN-T6.md`, `docs/RDO/evidencia/P-0749-SAN-T6a.md`, `docs/RDO/evidencia/P-0749-SAN-T6b.md`, `docs/RDO/evidencia/P-0750-CAH-T1.md`, `docs/RDO/evidencia/P-0750-CAH-T2.md`, `docs/RDO/evidencia/P-0750-CAH-T3.md`, `docs/RDO/evidencia/P-0750-CAH-T4.md`, `docs/RDO/evidencia/P-0750-CAH-T4a.md`, `docs/RDO/evidencia/P-0750-CAH-T5.md`, `docs/RDO/evidencia/P-0751-EBK-T1.md`, `docs/RDO/evidencia/P-0751-EBK-T10.md`, `docs/RDO/evidencia/P-0751-EBK-T11.md`, `docs/RDO/evidencia/P-0751-EBK-T12.md`, `docs/RDO/evidencia/P-0751-EBK-T13.md`, `docs/RDO/evidencia/P-0751-EBK-T13a.md`, `docs/RDO/evidencia/P-0751-EBK-T14.md`, `docs/RDO/evidencia/P-0751-EBK-T2.md`, `docs/RDO/evidencia/P-0751-EBK-T3.md`, `docs/RDO/evidencia/P-0751-EBK-T4.md`, `docs/RDO/evidencia/P-0751-EBK-T5.md`, `docs/RDO/evidencia/P-0751-EBK-T5a.md`, `docs/RDO/evidencia/P-0751-EBK-T6.md`, `docs/RDO/evidencia/P-0751-EBK-T7.md`, `docs/RDO/evidencia/P-0751-EBK-T8.md`, `docs/RDO/evidencia/P-0751-EBK-T9.md`, `docs/RDO/evidencia/P-0752-FPU-T1.md`, `docs/RDO/evidencia/P-0752-FPU-T1a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T2.md`, `docs/RDO/evidencia/P-0752-FPU-T3.md`, `docs/RDO/evidencia/P-0752-FPU-T5.md`, `docs/RDO/evidencia/P-0752-FPU-T5a-medida.json`, `docs/RDO/evidencia/P-0752-FPU-T5a.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/RDO/evidencia/TK-65-TK-65a.md`, `docs/RDO/evidencia/TK-65-TK-65b.md`, `docs/RDO/evidencia/TK-65-TK-65c.md`, `docs/RDO/evidencia/TK-65-TK-65d.md`, `docs/RDO/evidencia/TK-65-TK-65e.md`, `docs/RDO/evidencia/TK-66-TK-66a.md`, `docs/RDO/evidencia/TK-74-TK-74a.md`, `docs/RDO/evidencia/TK-74-TK-74b.md`, `docs/RDO/evidencia/TK-76-TK-76a.md`, `docs/RDO/evidencia/TK-77-TK-77a.md`, `docs/RDO/evidencia/TK-78-TK-78a.md`, `docs/RDO/evidencia/TK-78-TK-78b.md`, `docs/RDO/evidencia/TK-78-TK-78c.md`, `docs/RDO/evidencia/TK-78-TK-78d.md`, `docs/RDO/evidencia/TK-79-TK-79a.md`, `docs/RDO/evidencia/TK-82-TK-82a.md`, `docs/RDO/laudos/P-0752-FPU-T1.md`, `docs/RDO/laudos/P-0752-FPU-T2.md`, `docs/RDO/laudos/P-0752-FPU-T3.md`, `docs/RDO/laudos/P-0752-FPU-T5.md`, `docs/RDO/laudos/P-0752-FPU-T5a.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/P-0747-consultor-de-plano.md`, `docs/plans/P-0748-tela-do-gerente.md`, `docs/plans/P-0749-saneamento-artefatos.md`, `docs/plans/P-0750-comunicacao-agente-humano.md`, `docs/plans/P-0751-esgotar-backlog.md`, `docs/plans/P-0752-fato-no-ponto-de-uso.md`, `docs/plans/_CAMPANHA-P-0748.md`, `docs/plans/_CENARIO-P-0747.md`, `docs/plans/_CENARIO-P-0748.md`, `docs/plans/_CENARIO-P-0749.md`, `docs/plans/_CENARIO-P-0750.md`, `docs/plans/_CENARIO-P-0751.md`, `docs/plans/_CENARIO-P-0752.md`, `docs/plans/_CENARIO-TK-65.md`, `docs/plans/_CENARIO-TK-78.md`, `docs/plans/_VEREDITO-procedimentos-2026-09-22.md`, `docs/telemetria.tsv`
- Fato: 31 arquivo(s) fora dos alvos e sem atribuição: `.claude/checks/frontmatter_yaml.py`, `.claude/skills/mensagem-ao-dono/SKILL.md`, `.claude/tools/caminhos.py`, `.claude/tools/encerrar.py`, `.claude/tools/progresso_hook.py`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/FALHAS_COMUNICACAO.tsv`, `docs/OPERACOES_AS_IS.md`, `docs/OPERACOES_AS_IS_P-0745.md`, `docs/OPERACOES_AS_IS_P-0746.md`, `docs/OPERACOES_AS_IS_P-0747.md`, `docs/OPERACOES_AS_IS_P-0748.md`, `docs/OPERACOES_AS_IS_P-0749.md`, `docs/OPERACOES_AS_IS_P-0750.md`, `docs/OPERACOES_AS_IS_P-0751.md`, `docs/planner-spec.md`, `tests/fixtures/backlog/pasta/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/estado.tsv`, `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/plano.md`, `tests/fixtures/backlog/pasta/docs/plans/_INBOX.md`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_caminhos.py`, `tests/test_doutrina_unidade.py`, `tests/test_encerrar.py`, `tests/test_fixtures_higiene.py`, `tests/test_frontmatter_yaml.py`, `tests/test_global_claude.py`, `tests/test_kit_check.py`, `tests/test_progresso_hook.py`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `tests/fixtures/card_check/plano-corpus.md`
```
# Fixture de card_check — corpus na forma inline (`FPU-T1`)

Cinco cards sintéticos, congelados por esta fixture: nenhum é card vivo de plano nenhum. Todos
usam a forma inline de `Verificação` (`DFP-14`): comando entre crases, `→` e o par opcional
`antes …, depois …`. `CX-T1` fecha comparando `antes`; `CX-T2` fecha comparando `depois`; `CX-T3`
não declara `antes`; `CX-T4` isola um item real de uma prosa de outro campo que contém `N.` fora
do início de linha; `CX-T5` isola dois itens reais de uma prosa na linha de continuação do
próprio item que contém `N.` fora do início de linha.

### CX-T1 — Card inline que fecha em antes [Sonnet · classe mecanica]
- **Status:** `ready`
- **Objetivo:** fixture de `card_check` na forma inline (`DFP-14`) cujo comando imprime o valor
  declarado como `antes`.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Verificação:**
  1. `python -c "print('a')"` → `b` — antes `a`, depois `b`
- **Pronto quando:** fixture existe e `card_check.py --tarefa CX-T1` sai 0, comparando `antes`.

### CX-T2 — Card inline que fecha em depois [Sonnet · classe mecanica]
- **Status:** `done`
- **Objetivo:** fixture de `card_check` na forma inline (`DFP-14`) cujo comando imprime o valor
  declarado como `depois`.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Verificação:**
  1. `python -c "print('b')"` → `b` — antes `a`, depois `b`
- **Pronto quando:** fixture existe e `card_check.py --tarefa CX-T2` sai 0, comparando `depois`;
  com `--mundo antes` sai 1, nomeando a divergência.

### CX-T3 — Card inline sem antes [Sonnet · classe mecanica]
- **Status:** `ready`
- **Objetivo:** fixture de `card_check` na forma inline (`DFP-14`) sem o par `antes`/`depois`.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Verificação:**
  1. `python -c "print('a')"` → `a`
- **Pronto quando:** fixture existe e `card_check.py --tarefa CX-T3` sai 1, nomeando `sem valor
  antes`.

### CX-T4 — Card inline com prosa de outro campo contendo N. fora do início de linha [Sonnet · classe mecanica]
- **Status:** `ready`
- **Objetivo:** fixture de `card_check` cujo campo `Contingências` contém a prosa `acionamento 1.
  medido`, fora do início de linha — não pode virar item fantasma na `Verificação`, que tem um
  item só.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Verificação:**
  1. `python -c "print('a')"` → `b` — antes `a`, depois `b`
- **Contingências:** prosa de teste — acionamento 1. medido, sem item novo de Verificação.
- **Pronto quando:** fixture existe e `card_check.py --tarefa CX-T4` sai 0, reconhecendo
  exatamente um item.

### CX-T5 — Card inline com prosa N. na continuação do item de Verificação [Sonnet · classe mecanica]
- **Status:** `ready`
- **Objetivo:** fixture de `card_check` cuja `Verificação` tem dois itens, com a linha de
  continuação do item 1 trazendo prosa que contém `1.` e `2.` fora do início de linha — não pode
  virar item fantasma, discriminando o caso que `CX-T4` (prosa noutro campo) não cobre.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Verificação:**
  1. `python -c "print('a')"` → `b` — antes `a`, depois `b`; medido no
     acionamento 1. e conferido na revisão 2. da mesma janela
  2. `python -c "print('c')"` → `d` — antes `c`, depois `d`
- **Pronto quando:** fixture existe e `card_check.py --tarefa CX-T5` sai 0, reconhecendo
  exatamente dois itens.

```

### `tests/test_card_check.py`
```
diff --git a/tests/test_card_check.py b/tests/test_card_check.py
index ce5a1f9..d824c33 100644
--- a/tests/test_card_check.py
+++ b/tests/test_card_check.py
@@ -203,6 +203,19 @@ def test_tf_marcador_so_no_inicio_de_linha(capsys):
     assert "card_check: OK" in saida.out
 
 
+def test_tf_prosa_na_continuacao_do_item_nao_vira_item():
+    """`CX-T5` tem a prosa `acionamento 1. e conferido na revisão 2.` na linha de continuação do
+    item 1 da `Verificação`, fora do início de linha — não pode virar item fantasma (`DFP-3`):
+    `card_check.verificar_tarefa` reconhece exatamente dois itens e fecha."""
+    card_check = _load_card_check()
+
+    ok, falhas, medida = card_check.verificar_tarefa(_PLANO_CORPUS, "CX-T5", _ROOT)
+
+    assert ok is True
+    assert falhas == []
+    assert len(medida["itens"]) == 2
+
+
 # --- FPU-T3 (DFP-4/DFP-16): toda âncora `<caminho>:<linha>` leva o literal, e o gate confere ----
 # a linha hoje.
 

```

## Medida do executor
- Arquivo: docs\RDO\evidencia\P-0752-FPU-T1a-medida.json; mundo: depois; gerado em: 2026-09-26T13:37:11+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_card_check.py -q -k prosa_na_continuacao` | 0 | true |
| 2 | `python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-corpus.md --tarefa CX-T5` | 0 | true |
| 3 | `python -m pytest -q` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
