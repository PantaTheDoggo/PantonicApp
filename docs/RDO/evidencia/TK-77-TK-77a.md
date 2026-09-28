# Evidência de revisão — DIARIO_DE_OBRAS TK-77a

## Diff (`git diff --stat`)
```
.claude/README.md                                  |    7 +-
 .claude/agents/pantonic-consultant.md              |   43 +-
 .claude/agents/pantonic-executor.md                |    8 +-
 .claude/agents/pantonic-fora-da-caixa.md           |    2 +-
 .claude/agents/pantonic-model-designer.md          |   56 +-
 .claude/agents/pantonic-planner.md                 |  168 +-
 .claude/agents/pantonic-reviewer.md                |    8 +-
 .claude/checks/kit_check.ps1                       |   22 +
 .claude/global/CLAUDE.md                           |   39 +-
 .../hooks/modelo_por_fase_userpromptsubmit.py      |    8 +-
 .claude/projecoes.json                             |   38 +
 .claude/skills/bootstrap-pantonic/SKILL.md         |    6 +-
 .claude/skills/diario-de-obras/SKILL.md            |   99 +-
 .claude/skills/entrega-de-encerramento/SKILL.md    |    2 +-
 .claude/skills/modelo-por-fase/SKILL.md            |   26 +-
 .claude/skills/passagem-de-bastao/SKILL.md         |   15 +-
 .claude/skills/redacao-doc/SKILL.md                |    3 +-
 .claude/skills/scrum-master/SKILL.md               |  107 +-
 .claude/tools/backlog.py                           |  246 ++-
 .claude/tools/backlog_hook.py                      |   14 +-
 .claude/tools/modelo.py                            |   39 +-
 .claude/tools/rdo.py                               |   50 +-
 .claude/tools/review_evidence.py                   |   97 +-
 GOVERNANCA.md                                      |  279 +--
 README.md                                          |  174 +-
 docs/CUSTO_DO_PICKUP.md                            |  113 ++
 docs/DIARIO_DE_OBRAS.md                            | 1839 ++++++++++++++++++--
 docs/DIARIO_HISTORICO.md                           |  154 ++
 docs/DOC_MAP.md                                    |  110 +-
 docs/RDO/INDEX.md                                  |   84 +
 docs/RESIDENCIA_DOUTRINA.md                        |    4 +-
 docs/consultant-spec.md                            |   75 +-
 docs/plans/P-0741-modelo-conceitual.md             |    8 +-
 docs/plans/P-0745-planejador-modelo-operacao.md    | 1584 +++++++++++++++--
 docs/plans/_INBOX.md                               |    3 +-
 docs/plans/_INBOX_HISTORICO.md                     |    6 +
 docs/telemetria.tsv                                |  268 +++
 tests/fixtures/modelo/fluxo-concluido.md           |   12 +-
 tests/fixtures/modelo/fluxo-pendente.md            |   20 +-
 tests/fixtures/modelo/fluxo-valido.md              |   12 +-
 tests/fixtures/modelo/plano-invalido-2.md          |   10 +-
 tests/fixtures/modelo/plano-invalido.md            |   12 +-
 tests/fixtures/modelo/plano-sem-cabecalho.md       |    8 +-
 tests/fixtures/modelo/plano-sem-estado.md          |    8 +-
 tests/test_backlog.py                              |  348 ++++
 tests/test_modelo.py                               |  143 +-
 tests/test_rdo.py                                  |   84 +
 tests/test_review_evidence.py                      |  176 +-
 48 files changed, 5791 insertions(+), 846 deletions(-)
```

## Arquivos tocados
- `.claude/checks/frontmatter_yaml.py` — atribuição: da entrega; estado git: `??`
- `.claude/checks/kit_check.ps1` — atribuição: da entrega; estado git: ` M`
- `.claude/skills/mensagem-ao-dono/SKILL.md` — atribuição: alheio; estado git: `??`
- `.claude/tools/caminhos.py` — atribuição: alheio; estado git: `??`
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
- `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-65a-check-recusa-id-de-depende-de-que-nao-e-item.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-65b-o-ponto-de-carga-escreve-em-utf-8-antes-de-argparse-abrir-a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-65c-o-verbo-diretiva-nao-descarta-id-em-silencio.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-65d-os-dois-depende-de-do-diario-voltam-a-gramatica.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-65e-o-ramo-concatenado-do-aviso-de-diretiva-ganha-teste.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-66a-o-atribuidor-so-casa-tarefa-ja-despachada.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-74a-o-alvo-diretorio-de-outra-tarefa-casa-por-prefixo.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-74b-modelo-py-recusa-limpo-o-alvo-que-nao-e-arquivo-de-plano.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-76a-as-tabelas-do-modelo-em-frases-curtas-para-o-dono.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-78a-o-loop-nao-para-para-rebaixar-o-modelo.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-78b-a-regua-do-card-aprende-as-tres-licoes-da-janela.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-78c-a-evidencia-mede-so-o-que-mudou-desde-o-despacho.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-78d-a-doutrina-e-o-readme-deixam-de-mandar-parar-para-rebaixar-o.md` — atribuição: alheio; estado git: `??`
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
- `docs/RDO/evidencia/TK-78-TK-78a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-78-TK-78b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-78-TK-78c.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-78-TK-78d.md` — atribuição: alheio; estado git: `??`
- `docs/planner-spec.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0746-lastro-do-modelo.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0747-consultor-de-plano.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0748-tela-do-gerente.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0749-saneamento-artefatos.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0750-comunicacao-agente-humano.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CAMPANHA-P-0748.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-P-0747.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-P-0748.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-P-0749.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-P-0750.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-TK-65.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-TK-78.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_VEREDITO-procedimentos-2026-09-22.md` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/backlog/pasta/docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/estado.tsv` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/plano.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/pasta/docs/plans/_INBOX.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-com-lastro.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-sem-lastro.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-terminal-sem-lastro.md` — atribuição: alheio; estado git: `??`
- `tests/test_caminhos.py` — atribuição: alheio; estado git: `??`
- `tests/test_doutrina_unidade.py` — atribuição: alheio; estado git: `??`
- `tests/test_frontmatter_yaml.py` — atribuição: da entrega; estado git: `??`
- `tests/test_progresso_hook.py` — atribuição: alheio; estado git: `??`

## Escopo
- Recorte: desde `3808e1faaa777b9f95273e1289e0e1d28a5efb5e`
- Arquivos-alvo declarados: `.claude/checks/frontmatter_yaml.py`, `.claude/checks/kit_check.ps1`, `tests/test_frontmatter_yaml.py`
- Arquivos tocados: `.claude/checks/frontmatter_yaml.py`, `.claude/checks/kit_check.ps1`, `.claude/skills/mensagem-ao-dono/SKILL.md`, `.claude/tools/caminhos.py`, `.claude/tools/progresso_hook.py`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/DIARIO_DE_OBRAS.md`, `docs/FALHAS_COMUNICACAO.tsv`, `docs/OPERACOES_AS_IS.md`, `docs/OPERACOES_AS_IS_P-0745.md`, `docs/OPERACOES_AS_IS_P-0746.md`, `docs/OPERACOES_AS_IS_P-0747.md`, `docs/OPERACOES_AS_IS_P-0748.md`, `docs/OPERACOES_AS_IS_P-0749.md`, `docs/OPERACOES_AS_IS_P-0750.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65a-check-recusa-id-de-depende-de-que-nao-e-item.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65b-o-ponto-de-carga-escreve-em-utf-8-antes-de-argparse-abrir-a.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65c-o-verbo-diretiva-nao-descarta-id-em-silencio.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65d-os-dois-depende-de-do-diario-voltam-a-gramatica.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65e-o-ramo-concatenado-do-aviso-de-diretiva-ganha-teste.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-66a-o-atribuidor-so-casa-tarefa-ja-despachada.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-74a-o-alvo-diretorio-de-outra-tarefa-casa-por-prefixo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-74b-modelo-py-recusa-limpo-o-alvo-que-nao-e-arquivo-de-plano.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-76a-as-tabelas-do-modelo-em-frases-curtas-para-o-dono.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78a-o-loop-nao-para-para-rebaixar-o-modelo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78b-a-regua-do-card-aprende-as-tres-licoes-da-janela.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78c-a-evidencia-mede-so-o-que-mudou-desde-o-despacho.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78d-a-doutrina-e-o-readme-deixam-de-mandar-parar-para-rebaixar-o.md`, `docs/RDO/P-0741-MC-T5-o-readme-explica-o-modelo-a-afericao-sobre-o-proprio-plano-e.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0745-PLN-T4a-o-ponteiro-sobrevivente-da-tabela-aposentada-nos-fatos-estav.md`, `docs/RDO/P-0745-PLN-T5-o-modelador-diante-do-plano-sem-cards-e-o-lastro-que-e-do-pl.md`, `docs/RDO/P-0745-PLN-T5a-a-frase-que-governa-o-gate-do-modelador-e-a-enumeracao-que-e.md`, `docs/RDO/P-0745-PLN-T6-a-especificacao-do-agente-de-planejamento.md`, `docs/RDO/P-0745-PLN-T7-o-indice-de-documentos-e-a-revisao-do-readme.md`, `docs/RDO/P-0745-PLN-T7a-o-readme-deixa-de-defender-a-regua-que-ele-mesmo-aposenta.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/P-0747-CON-T1-o-consultor-entra-na-doutrina-de-governanca.md`, `docs/RDO/P-0747-CON-T2-a-definicao-de-conduta-do-consultor-sem-estatuto-provisorio.md`, `docs/RDO/P-0747-CON-T2a-corretivo-da-op-2-o-agente-descreve-o-cenario-persistido-e-l.md`, `docs/RDO/P-0747-CON-T2b-corretivo-da-op-2-o-agente-nomeia-a-recusa-do-impedimento-im.md`, `docs/RDO/P-0747-CON-T3-o-loop-leva-toda-parada-ao-consultor.md`, `docs/RDO/P-0747-CON-T3a-corretivo-da-op-3-a-parada-e-a-mesma-em-todas-as-regras-que.md`, `docs/RDO/P-0747-CON-T3b-corretivo-da-op-3-com-estrategico-o-loop-para-sem-executar-a.md`, `docs/RDO/P-0747-CON-T3c-corretivo-da-op-3-com-estrategico-a-rota-planejador-executa.md`, `docs/RDO/P-0747-CON-T3d-corretivo-da-op-3-o-loop-redespacha-sem-retentativa-o-card-c.md`, `docs/RDO/P-0747-CON-T4-a-forma-efemera-com-cenario-persistido.md`, `docs/RDO/P-0747-CON-T4a-corretivo-da-op-4-a-queda-de-uma-instancia-do-consultor-nao.md`, `docs/RDO/P-0747-CON-T5-o-outro-lado-da-fronteira-nas-definicoes-de-conduta.md`, `docs/RDO/P-0747-CON-T5a-corretivo-da-op-5-o-diario-e-a-regra-8-dizem-o-que-a-triagem.md`, `docs/RDO/P-0747-CON-T6-a-especificacao-vira-lastro-medido.md`, `docs/RDO/P-0747-CON-T6a-corretivo-da-op-6-a-spec-nao-prevalece-sobre-o-bloco-a.md`, `docs/RDO/P-0747-CON-T7-a-medida-do-piloto-da-forma-efemera.md`, `docs/RDO/P-0747-CON-T7a-corretivo-da-op-7-o-veredito-declara-o-modelo-das-instancias.md`, `docs/RDO/P-0747-CON-T8-a-porta-de-entrada-e-a-descricao-do-agente.md`, `docs/RDO/P-0747-CON-T8a-corretivo-da-op-8-a-description-volta-ao-yaml-que-o-harness.md`, `docs/RDO/P-0748-TLG-T1-a-sonda-de-viabilidade-diante-do-dono.md`, `docs/RDO/P-0748-TLG-T2-o-repertorio-de-mensagens-na-skill-do-loop.md`, `docs/RDO/P-0748-TLG-T2a-o-repertorio-deixa-de-citar-o-comando-que-nao-vai-existir.md`, `docs/RDO/P-0748-TLG-T2b-o-repertorio-como-tabela-de-eventos-a-skill-diz-o-que-a-func.md`, `docs/RDO/P-0748-TLG-T3-o-gancho-que-grava-o-arquivo-de-progresso.md`, `docs/RDO/P-0748-TLG-T3a-a-captura-do-payload-dos-ganchos-o-que-a-funcao-vai-ler.md`, `docs/RDO/P-0748-TLG-T3b-a-funcao-que-gera-a-linha-do-stream-a-cada-evento-do-loop.md`, `docs/RDO/P-0748-TLG-T3c-o-painel-nao-perde-linha-e-nao-afirma-o-que-nao-aconteceu.md`, `docs/RDO/P-0748-TLG-T3d-o-painel-so-diz-que-a-janela-encerrou-quando-ela-encerrou.md`, `docs/RDO/P-0748-TLG-T3e-o-painel-diz-so-o-que-o-gancho-ve-o-modelo-mostrado-e-o-cons.md`, `docs/RDO/P-0748-TLG-T3f-o-estado-do-gancho-nao-guarda-chave-que-ninguem-le.md`, `docs/RDO/P-0748-TLG-T3g-o-painel-reconhece-o-retorno-do-agente-com-o-ou-o-colchete-a.md`, `docs/RDO/P-0748-TLG-T3h-o-painel-da-uma-linha-a-cada-status-do-mesmo-comando-e-a-ski.md`, `docs/RDO/P-0748-TLG-T4-o-condutor-narra-uma-linha-do-repertorio-antes-de-cada-ato-n.md`, `docs/RDO/P-0748-TLG-T4a-a-skill-deixa-de-narrar-a-transicao-chega-ao-painel-pela-fun.md`, `docs/RDO/P-0748-TLG-T5-a-porta-de-entrada-diz-como-o-dono-acompanha-a-execucao-no-p.md`, `docs/RDO/P-0748-TLG-T5a-a-celula-da-scrum-master-na-tabela-de-skills-volta-a-dizer-q.md`, `docs/RDO/P-0749-SAN-T1-o-id-e-o-caminho-do-plano-num-lugar-so.md`, `docs/RDO/P-0749-SAN-T2-o-estado-sai-do-texto-e-vai-para-o-estado-tsv.md`, `docs/RDO/P-0749-SAN-T2a-projeto-novo-com-contador-em-p-0-e-nenhum-plano-passa-no-che.md`, `docs/RDO/P-0749-SAN-T3-relato-laudo-e-evidencia-nascem-na-pasta-do-plano.md`, `docs/RDO/P-0749-SAN-T3a-a-flag-vence-tambem-no-indice-e-a-cli-anuncia-os-dois-destin.md`, `docs/RDO/P-0749-SAN-T4-a-doutrina-ensina-a-pasta-o-estado-tsv-e-a-contagem-em-zero.md`, `docs/RDO/P-0749-SAN-T5-a-regra-do-artefato-de-humano-minimo-uma-vez-so.md`, `docs/RDO/P-0749-SAN-T6-a-porta-de-entrada-descreve-a-pasta-a-tabela-e-o-texto-minim.md`, `docs/RDO/P-0749-SAN-T6a-o-glossario-diz-o-contador-como-a-regra-o-diz.md`, `docs/RDO/P-0749-SAN-T6b-as-decisoes-estruturantes-dizem-o-contador-como-a-regra-o-di.md`, `docs/RDO/P-0750-CAH-T1-a-regra-da-mensagem-legivel-ao-dono-na-doutrina-e-no-regulam.md`, `docs/RDO/P-0750-CAH-T2-o-glossario-diz-o-que-cada-familia-de-sigla-nomeia.md`, `docs/RDO/P-0750-CAH-T3-a-tabela-de-falhas-de-comunicacao-com-as-falhas-ja-medidas.md`, `docs/RDO/P-0750-CAH-T4-a-skill-da-mensagem-ao-dono.md`, `docs/RDO/P-0750-CAH-T4a-o-titulo-de-tarefa-na-skill-da-mensagem-ao-dono-para-antes-d.md`, `docs/RDO/P-0750-CAH-T5-os-textos-que-mandavam-citar-sigla-ao-dono-passam-a-mandar-o.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0745-PLN-T4a.md`, `docs/RDO/evidencia/P-0745-PLN-T5.md`, `docs/RDO/evidencia/P-0745-PLN-T5a.md`, `docs/RDO/evidencia/P-0745-PLN-T6.md`, `docs/RDO/evidencia/P-0745-PLN-T7.md`, `docs/RDO/evidencia/P-0745-PLN-T7a.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/P-0747-CON-T1.md`, `docs/RDO/evidencia/P-0747-CON-T2.md`, `docs/RDO/evidencia/P-0747-CON-T2a.md`, `docs/RDO/evidencia/P-0747-CON-T2b.md`, `docs/RDO/evidencia/P-0747-CON-T3.md`, `docs/RDO/evidencia/P-0747-CON-T3a.md`, `docs/RDO/evidencia/P-0747-CON-T3b.md`, `docs/RDO/evidencia/P-0747-CON-T3c.md`, `docs/RDO/evidencia/P-0747-CON-T3d.md`, `docs/RDO/evidencia/P-0747-CON-T4.md`, `docs/RDO/evidencia/P-0747-CON-T4a.md`, `docs/RDO/evidencia/P-0747-CON-T5.md`, `docs/RDO/evidencia/P-0747-CON-T5a.md`, `docs/RDO/evidencia/P-0747-CON-T6.md`, `docs/RDO/evidencia/P-0747-CON-T6a.md`, `docs/RDO/evidencia/P-0747-CON-T7.md`, `docs/RDO/evidencia/P-0747-CON-T7a.md`, `docs/RDO/evidencia/P-0747-CON-T8.md`, `docs/RDO/evidencia/P-0747-CON-T8a.md`, `docs/RDO/evidencia/P-0748-TLG-T1.md`, `docs/RDO/evidencia/P-0748-TLG-T2.md`, `docs/RDO/evidencia/P-0748-TLG-T2a.md`, `docs/RDO/evidencia/P-0748-TLG-T2b.md`, `docs/RDO/evidencia/P-0748-TLG-T3.md`, `docs/RDO/evidencia/P-0748-TLG-T3a.md`, `docs/RDO/evidencia/P-0748-TLG-T3b.md`, `docs/RDO/evidencia/P-0748-TLG-T3c.md`, `docs/RDO/evidencia/P-0748-TLG-T3d.md`, `docs/RDO/evidencia/P-0748-TLG-T3e.md`, `docs/RDO/evidencia/P-0748-TLG-T3f.md`, `docs/RDO/evidencia/P-0748-TLG-T3g.md`, `docs/RDO/evidencia/P-0748-TLG-T3h.md`, `docs/RDO/evidencia/P-0748-TLG-T4.md`, `docs/RDO/evidencia/P-0748-TLG-T4a.md`, `docs/RDO/evidencia/P-0748-TLG-T5.md`, `docs/RDO/evidencia/P-0748-TLG-T5a.md`, `docs/RDO/evidencia/P-0749-SAN-T1.md`, `docs/RDO/evidencia/P-0749-SAN-T2.md`, `docs/RDO/evidencia/P-0749-SAN-T2a.md`, `docs/RDO/evidencia/P-0749-SAN-T3.md`, `docs/RDO/evidencia/P-0749-SAN-T3a.md`, `docs/RDO/evidencia/P-0749-SAN-T4.md`, `docs/RDO/evidencia/P-0749-SAN-T5.md`, `docs/RDO/evidencia/P-0749-SAN-T6.md`, `docs/RDO/evidencia/P-0749-SAN-T6a.md`, `docs/RDO/evidencia/P-0749-SAN-T6b.md`, `docs/RDO/evidencia/P-0750-CAH-T1.md`, `docs/RDO/evidencia/P-0750-CAH-T2.md`, `docs/RDO/evidencia/P-0750-CAH-T3.md`, `docs/RDO/evidencia/P-0750-CAH-T4.md`, `docs/RDO/evidencia/P-0750-CAH-T4a.md`, `docs/RDO/evidencia/P-0750-CAH-T5.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/RDO/evidencia/TK-65-TK-65a.md`, `docs/RDO/evidencia/TK-65-TK-65b.md`, `docs/RDO/evidencia/TK-65-TK-65c.md`, `docs/RDO/evidencia/TK-65-TK-65d.md`, `docs/RDO/evidencia/TK-65-TK-65e.md`, `docs/RDO/evidencia/TK-66-TK-66a.md`, `docs/RDO/evidencia/TK-74-TK-74a.md`, `docs/RDO/evidencia/TK-74-TK-74b.md`, `docs/RDO/evidencia/TK-76-TK-76a.md`, `docs/RDO/evidencia/TK-78-TK-78a.md`, `docs/RDO/evidencia/TK-78-TK-78b.md`, `docs/RDO/evidencia/TK-78-TK-78c.md`, `docs/RDO/evidencia/TK-78-TK-78d.md`, `docs/planner-spec.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/P-0747-consultor-de-plano.md`, `docs/plans/P-0748-tela-do-gerente.md`, `docs/plans/P-0749-saneamento-artefatos.md`, `docs/plans/P-0750-comunicacao-agente-humano.md`, `docs/plans/_CAMPANHA-P-0748.md`, `docs/plans/_CENARIO-P-0747.md`, `docs/plans/_CENARIO-P-0748.md`, `docs/plans/_CENARIO-P-0749.md`, `docs/plans/_CENARIO-P-0750.md`, `docs/plans/_CENARIO-TK-65.md`, `docs/plans/_CENARIO-TK-78.md`, `docs/plans/_VEREDITO-procedimentos-2026-09-22.md`, `docs/telemetria.tsv`, `tests/fixtures/backlog/pasta/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/estado.tsv`, `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/plano.md`, `tests/fixtures/backlog/pasta/docs/plans/_INBOX.md`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_caminhos.py`, `tests/test_doutrina_unidade.py`, `tests/test_frontmatter_yaml.py`, `tests/test_progresso_hook.py`
- Atribuídos a outra tarefa do mesmo plano: `docs/DIARIO_DE_OBRAS.md` → `TK-54b`, `tests/fixtures/backlog/pasta/docs/DIARIO_DE_OBRAS.md` → `TK-61a`, `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/estado.tsv` → `TK-61a`, `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/plano.md` → `TK-61a`, `tests/fixtures/backlog/pasta/docs/plans/_INBOX.md` → `TK-61a`
- Registro da orquestração (não atribuível a tarefa): `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65a-check-recusa-id-de-depende-de-que-nao-e-item.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65b-o-ponto-de-carga-escreve-em-utf-8-antes-de-argparse-abrir-a.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65c-o-verbo-diretiva-nao-descarta-id-em-silencio.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65d-os-dois-depende-de-do-diario-voltam-a-gramatica.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-65e-o-ramo-concatenado-do-aviso-de-diretiva-ganha-teste.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-66a-o-atribuidor-so-casa-tarefa-ja-despachada.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-74a-o-alvo-diretorio-de-outra-tarefa-casa-por-prefixo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-74b-modelo-py-recusa-limpo-o-alvo-que-nao-e-arquivo-de-plano.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-76a-as-tabelas-do-modelo-em-frases-curtas-para-o-dono.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78a-o-loop-nao-para-para-rebaixar-o-modelo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78b-a-regua-do-card-aprende-as-tres-licoes-da-janela.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78c-a-evidencia-mede-so-o-que-mudou-desde-o-despacho.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78d-a-doutrina-e-o-readme-deixam-de-mandar-parar-para-rebaixar-o.md`, `docs/RDO/P-0741-MC-T5-o-readme-explica-o-modelo-a-afericao-sobre-o-proprio-plano-e.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0745-PLN-T4a-o-ponteiro-sobrevivente-da-tabela-aposentada-nos-fatos-estav.md`, `docs/RDO/P-0745-PLN-T5-o-modelador-diante-do-plano-sem-cards-e-o-lastro-que-e-do-pl.md`, `docs/RDO/P-0745-PLN-T5a-a-frase-que-governa-o-gate-do-modelador-e-a-enumeracao-que-e.md`, `docs/RDO/P-0745-PLN-T6-a-especificacao-do-agente-de-planejamento.md`, `docs/RDO/P-0745-PLN-T7-o-indice-de-documentos-e-a-revisao-do-readme.md`, `docs/RDO/P-0745-PLN-T7a-o-readme-deixa-de-defender-a-regua-que-ele-mesmo-aposenta.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/P-0747-CON-T1-o-consultor-entra-na-doutrina-de-governanca.md`, `docs/RDO/P-0747-CON-T2-a-definicao-de-conduta-do-consultor-sem-estatuto-provisorio.md`, `docs/RDO/P-0747-CON-T2a-corretivo-da-op-2-o-agente-descreve-o-cenario-persistido-e-l.md`, `docs/RDO/P-0747-CON-T2b-corretivo-da-op-2-o-agente-nomeia-a-recusa-do-impedimento-im.md`, `docs/RDO/P-0747-CON-T3-o-loop-leva-toda-parada-ao-consultor.md`, `docs/RDO/P-0747-CON-T3a-corretivo-da-op-3-a-parada-e-a-mesma-em-todas-as-regras-que.md`, `docs/RDO/P-0747-CON-T3b-corretivo-da-op-3-com-estrategico-o-loop-para-sem-executar-a.md`, `docs/RDO/P-0747-CON-T3c-corretivo-da-op-3-com-estrategico-a-rota-planejador-executa.md`, `docs/RDO/P-0747-CON-T3d-corretivo-da-op-3-o-loop-redespacha-sem-retentativa-o-card-c.md`, `docs/RDO/P-0747-CON-T4-a-forma-efemera-com-cenario-persistido.md`, `docs/RDO/P-0747-CON-T4a-corretivo-da-op-4-a-queda-de-uma-instancia-do-consultor-nao.md`, `docs/RDO/P-0747-CON-T5-o-outro-lado-da-fronteira-nas-definicoes-de-conduta.md`, `docs/RDO/P-0747-CON-T5a-corretivo-da-op-5-o-diario-e-a-regra-8-dizem-o-que-a-triagem.md`, `docs/RDO/P-0747-CON-T6-a-especificacao-vira-lastro-medido.md`, `docs/RDO/P-0747-CON-T6a-corretivo-da-op-6-a-spec-nao-prevalece-sobre-o-bloco-a.md`, `docs/RDO/P-0747-CON-T7-a-medida-do-piloto-da-forma-efemera.md`, `docs/RDO/P-0747-CON-T7a-corretivo-da-op-7-o-veredito-declara-o-modelo-das-instancias.md`, `docs/RDO/P-0747-CON-T8-a-porta-de-entrada-e-a-descricao-do-agente.md`, `docs/RDO/P-0747-CON-T8a-corretivo-da-op-8-a-description-volta-ao-yaml-que-o-harness.md`, `docs/RDO/P-0748-TLG-T1-a-sonda-de-viabilidade-diante-do-dono.md`, `docs/RDO/P-0748-TLG-T2-o-repertorio-de-mensagens-na-skill-do-loop.md`, `docs/RDO/P-0748-TLG-T2a-o-repertorio-deixa-de-citar-o-comando-que-nao-vai-existir.md`, `docs/RDO/P-0748-TLG-T2b-o-repertorio-como-tabela-de-eventos-a-skill-diz-o-que-a-func.md`, `docs/RDO/P-0748-TLG-T3-o-gancho-que-grava-o-arquivo-de-progresso.md`, `docs/RDO/P-0748-TLG-T3a-a-captura-do-payload-dos-ganchos-o-que-a-funcao-vai-ler.md`, `docs/RDO/P-0748-TLG-T3b-a-funcao-que-gera-a-linha-do-stream-a-cada-evento-do-loop.md`, `docs/RDO/P-0748-TLG-T3c-o-painel-nao-perde-linha-e-nao-afirma-o-que-nao-aconteceu.md`, `docs/RDO/P-0748-TLG-T3d-o-painel-so-diz-que-a-janela-encerrou-quando-ela-encerrou.md`, `docs/RDO/P-0748-TLG-T3e-o-painel-diz-so-o-que-o-gancho-ve-o-modelo-mostrado-e-o-cons.md`, `docs/RDO/P-0748-TLG-T3f-o-estado-do-gancho-nao-guarda-chave-que-ninguem-le.md`, `docs/RDO/P-0748-TLG-T3g-o-painel-reconhece-o-retorno-do-agente-com-o-ou-o-colchete-a.md`, `docs/RDO/P-0748-TLG-T3h-o-painel-da-uma-linha-a-cada-status-do-mesmo-comando-e-a-ski.md`, `docs/RDO/P-0748-TLG-T4-o-condutor-narra-uma-linha-do-repertorio-antes-de-cada-ato-n.md`, `docs/RDO/P-0748-TLG-T4a-a-skill-deixa-de-narrar-a-transicao-chega-ao-painel-pela-fun.md`, `docs/RDO/P-0748-TLG-T5-a-porta-de-entrada-diz-como-o-dono-acompanha-a-execucao-no-p.md`, `docs/RDO/P-0748-TLG-T5a-a-celula-da-scrum-master-na-tabela-de-skills-volta-a-dizer-q.md`, `docs/RDO/P-0749-SAN-T1-o-id-e-o-caminho-do-plano-num-lugar-so.md`, `docs/RDO/P-0749-SAN-T2-o-estado-sai-do-texto-e-vai-para-o-estado-tsv.md`, `docs/RDO/P-0749-SAN-T2a-projeto-novo-com-contador-em-p-0-e-nenhum-plano-passa-no-che.md`, `docs/RDO/P-0749-SAN-T3-relato-laudo-e-evidencia-nascem-na-pasta-do-plano.md`, `docs/RDO/P-0749-SAN-T3a-a-flag-vence-tambem-no-indice-e-a-cli-anuncia-os-dois-destin.md`, `docs/RDO/P-0749-SAN-T4-a-doutrina-ensina-a-pasta-o-estado-tsv-e-a-contagem-em-zero.md`, `docs/RDO/P-0749-SAN-T5-a-regra-do-artefato-de-humano-minimo-uma-vez-so.md`, `docs/RDO/P-0749-SAN-T6-a-porta-de-entrada-descreve-a-pasta-a-tabela-e-o-texto-minim.md`, `docs/RDO/P-0749-SAN-T6a-o-glossario-diz-o-contador-como-a-regra-o-diz.md`, `docs/RDO/P-0749-SAN-T6b-as-decisoes-estruturantes-dizem-o-contador-como-a-regra-o-di.md`, `docs/RDO/P-0750-CAH-T1-a-regra-da-mensagem-legivel-ao-dono-na-doutrina-e-no-regulam.md`, `docs/RDO/P-0750-CAH-T2-o-glossario-diz-o-que-cada-familia-de-sigla-nomeia.md`, `docs/RDO/P-0750-CAH-T3-a-tabela-de-falhas-de-comunicacao-com-as-falhas-ja-medidas.md`, `docs/RDO/P-0750-CAH-T4-a-skill-da-mensagem-ao-dono.md`, `docs/RDO/P-0750-CAH-T4a-o-titulo-de-tarefa-na-skill-da-mensagem-ao-dono-para-antes-d.md`, `docs/RDO/P-0750-CAH-T5-os-textos-que-mandavam-citar-sigla-ao-dono-passam-a-mandar-o.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0745-PLN-T4a.md`, `docs/RDO/evidencia/P-0745-PLN-T5.md`, `docs/RDO/evidencia/P-0745-PLN-T5a.md`, `docs/RDO/evidencia/P-0745-PLN-T6.md`, `docs/RDO/evidencia/P-0745-PLN-T7.md`, `docs/RDO/evidencia/P-0745-PLN-T7a.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/P-0747-CON-T1.md`, `docs/RDO/evidencia/P-0747-CON-T2.md`, `docs/RDO/evidencia/P-0747-CON-T2a.md`, `docs/RDO/evidencia/P-0747-CON-T2b.md`, `docs/RDO/evidencia/P-0747-CON-T3.md`, `docs/RDO/evidencia/P-0747-CON-T3a.md`, `docs/RDO/evidencia/P-0747-CON-T3b.md`, `docs/RDO/evidencia/P-0747-CON-T3c.md`, `docs/RDO/evidencia/P-0747-CON-T3d.md`, `docs/RDO/evidencia/P-0747-CON-T4.md`, `docs/RDO/evidencia/P-0747-CON-T4a.md`, `docs/RDO/evidencia/P-0747-CON-T5.md`, `docs/RDO/evidencia/P-0747-CON-T5a.md`, `docs/RDO/evidencia/P-0747-CON-T6.md`, `docs/RDO/evidencia/P-0747-CON-T6a.md`, `docs/RDO/evidencia/P-0747-CON-T7.md`, `docs/RDO/evidencia/P-0747-CON-T7a.md`, `docs/RDO/evidencia/P-0747-CON-T8.md`, `docs/RDO/evidencia/P-0747-CON-T8a.md`, `docs/RDO/evidencia/P-0748-TLG-T1.md`, `docs/RDO/evidencia/P-0748-TLG-T2.md`, `docs/RDO/evidencia/P-0748-TLG-T2a.md`, `docs/RDO/evidencia/P-0748-TLG-T2b.md`, `docs/RDO/evidencia/P-0748-TLG-T3.md`, `docs/RDO/evidencia/P-0748-TLG-T3a.md`, `docs/RDO/evidencia/P-0748-TLG-T3b.md`, `docs/RDO/evidencia/P-0748-TLG-T3c.md`, `docs/RDO/evidencia/P-0748-TLG-T3d.md`, `docs/RDO/evidencia/P-0748-TLG-T3e.md`, `docs/RDO/evidencia/P-0748-TLG-T3f.md`, `docs/RDO/evidencia/P-0748-TLG-T3g.md`, `docs/RDO/evidencia/P-0748-TLG-T3h.md`, `docs/RDO/evidencia/P-0748-TLG-T4.md`, `docs/RDO/evidencia/P-0748-TLG-T4a.md`, `docs/RDO/evidencia/P-0748-TLG-T5.md`, `docs/RDO/evidencia/P-0748-TLG-T5a.md`, `docs/RDO/evidencia/P-0749-SAN-T1.md`, `docs/RDO/evidencia/P-0749-SAN-T2.md`, `docs/RDO/evidencia/P-0749-SAN-T2a.md`, `docs/RDO/evidencia/P-0749-SAN-T3.md`, `docs/RDO/evidencia/P-0749-SAN-T3a.md`, `docs/RDO/evidencia/P-0749-SAN-T4.md`, `docs/RDO/evidencia/P-0749-SAN-T5.md`, `docs/RDO/evidencia/P-0749-SAN-T6.md`, `docs/RDO/evidencia/P-0749-SAN-T6a.md`, `docs/RDO/evidencia/P-0749-SAN-T6b.md`, `docs/RDO/evidencia/P-0750-CAH-T1.md`, `docs/RDO/evidencia/P-0750-CAH-T2.md`, `docs/RDO/evidencia/P-0750-CAH-T3.md`, `docs/RDO/evidencia/P-0750-CAH-T4.md`, `docs/RDO/evidencia/P-0750-CAH-T4a.md`, `docs/RDO/evidencia/P-0750-CAH-T5.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/RDO/evidencia/TK-65-TK-65a.md`, `docs/RDO/evidencia/TK-65-TK-65b.md`, `docs/RDO/evidencia/TK-65-TK-65c.md`, `docs/RDO/evidencia/TK-65-TK-65d.md`, `docs/RDO/evidencia/TK-65-TK-65e.md`, `docs/RDO/evidencia/TK-66-TK-66a.md`, `docs/RDO/evidencia/TK-74-TK-74a.md`, `docs/RDO/evidencia/TK-74-TK-74b.md`, `docs/RDO/evidencia/TK-76-TK-76a.md`, `docs/RDO/evidencia/TK-78-TK-78a.md`, `docs/RDO/evidencia/TK-78-TK-78b.md`, `docs/RDO/evidencia/TK-78-TK-78c.md`, `docs/RDO/evidencia/TK-78-TK-78d.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/P-0747-consultor-de-plano.md`, `docs/plans/P-0748-tela-do-gerente.md`, `docs/plans/P-0749-saneamento-artefatos.md`, `docs/plans/P-0750-comunicacao-agente-humano.md`, `docs/plans/_CAMPANHA-P-0748.md`, `docs/plans/_CENARIO-P-0747.md`, `docs/plans/_CENARIO-P-0748.md`, `docs/plans/_CENARIO-P-0749.md`, `docs/plans/_CENARIO-P-0750.md`, `docs/plans/_CENARIO-TK-65.md`, `docs/plans/_CENARIO-TK-78.md`, `docs/plans/_VEREDITO-procedimentos-2026-09-22.md`, `docs/telemetria.tsv`
- Fato: 19 arquivo(s) fora dos alvos e sem atribuição: `.claude/skills/mensagem-ao-dono/SKILL.md`, `.claude/tools/caminhos.py`, `.claude/tools/progresso_hook.py`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/FALHAS_COMUNICACAO.tsv`, `docs/OPERACOES_AS_IS.md`, `docs/OPERACOES_AS_IS_P-0745.md`, `docs/OPERACOES_AS_IS_P-0746.md`, `docs/OPERACOES_AS_IS_P-0747.md`, `docs/OPERACOES_AS_IS_P-0748.md`, `docs/OPERACOES_AS_IS_P-0749.md`, `docs/OPERACOES_AS_IS_P-0750.md`, `docs/planner-spec.md`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_caminhos.py`, `tests/test_doutrina_unidade.py`, `tests/test_progresso_hook.py`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/checks/frontmatter_yaml.py`
```
"""TK-77a (`docs/DIARIO_DE_OBRAS.md` `### TK-77a`) — o `validate` recusa frontmatter de agente ou
skill que o YAML estrito recusa. Função pura `problemas(caminhos)`: para cada arquivo, recorta o
bloco entre a primeira linha `---` e a seguinte `---` (arquivo sem o bloco não é problema deste
script — o `validate` já o acusa via `Get-Frontmatter`), aplica `yaml.safe_load` e devolve
`"<caminho>: <primeira linha do erro>"` quando o parser levanta, ou `"<caminho>: frontmatter não
é mapeamento"` quando o resultado não é `dict`.

CLI: `python .claude/checks/frontmatter_yaml.py <arquivo>...` imprime um problema por linha e sai
`1` se houver algum, `0` se nenhum; sem PyYAML importável imprime `frontmatter_yaml: PyYAML
ausente` e sai `2`.
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


def _extrair_frontmatter(texto: str) -> str | None:
    """Bloco entre a primeira linha `---` e a linha `---` seguinte, sem os marcadores. `None`
    quando o arquivo não tem o bloco (início ausente ou não fechado) — não é problema deste
    script."""
    linhas = texto.splitlines()
    inicio = None
    for i, linha in enumerate(linhas):
        if linha.strip() == "---":
            inicio = i
            break
    if inicio is None:
        return None
    fim = None
    for i in range(inicio + 1, len(linhas)):
        if linhas[i].strip() == "---":
            fim = i
            break
    if fim is None:
        return None
    return "\n".join(linhas[inicio + 1 : fim])


def problemas(caminhos: list[Path]) -> list[str]:
    """Um problema por arquivo cujo frontmatter não é YAML válido para `yaml.safe_load` ou não
    carrega um mapeamento. Arquivo sem bloco de frontmatter não entra na lista."""
    resultado: list[str] = []
    for caminho in caminhos:
        texto = caminho.read_text(encoding="utf-8")
        bloco = _extrair_frontmatter(texto)
        if bloco is None:
            continue
        try:
            valor = yaml.safe_load(bloco)
        except yaml.YAMLError as exc:
            mensagem = str(exc)
            primeira_linha = mensagem.splitlines()[0] if mensagem else mensagem
            resultado.append(f"{caminho}: {primeira_linha}")
            continue
        if not isinstance(valor, dict):
            resultado.append(f"{caminho}: frontmatter não é mapeamento")
    return resultado


def _forcar_utf8(stream) -> None:
    """Console cp1252 do Windows estoura `UnicodeEncodeError` ao imprimir caminho/mensagem com
    acentos; mesma forma de `.claude/tools/review_evidence.py:156-161` (`_forcar_utf8`)."""
    reconfigure = getattr(stream, "reconfigure", None)
    if reconfigure is not None:
        reconfigure(encoding="utf-8", errors="replace")


def main(argv: list[str]) -> int:
    _forcar_utf8(sys.stdout)
    _forcar_utf8(sys.stderr)
    if yaml is None:
        print("frontmatter_yaml: PyYAML ausente")
        return 2
    lista = problemas([Path(a) for a in argv])
    for linha in lista:
        print(linha)
    return 1 if lista else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

```

### `.claude/checks/kit_check.ps1`
```
diff --git a/.claude/checks/kit_check.ps1 b/.claude/checks/kit_check.ps1
index 5ff5bc5..6de6503 100644
--- a/.claude/checks/kit_check.ps1
+++ b/.claude/checks/kit_check.ps1
@@ -195,6 +195,28 @@ foreach ($d in $skillDirs) {
     }
 }
 
+# --- 2b. Frontmatter é YAML válido --------------------------------------
+# TK-77a (`docs/DIARIO_DE_OBRAS.md` `### TK-77a`) — o frontmatter de agente ou skill que o YAML
+# estrito (`yaml.safe_load`) recusa também é motivo de falha aqui, mesma classe nas duas
+# famílias (o leitor de frontmatter acima, `Get-Frontmatter`, é um só para as duas).
+$frontmatterYamlScript = Join-Path $KitRoot 'checks/frontmatter_yaml.py'
+$frontmatterYamlTargets = [System.Collections.Generic.List[string]]::new()
+foreach ($f in $agentFiles) { $frontmatterYamlTargets.Add($f.FullName) }
+foreach ($d in $skillDirs) {
+    $skillMd = Join-Path $d.FullName 'SKILL.md'
+    if (Test-Path -LiteralPath $skillMd) { $frontmatterYamlTargets.Add($skillMd) }
+}
+$frontmatterYamlOutput = @(& python $frontmatterYamlScript @frontmatterYamlTargets 2>&1)
+$frontmatterYamlExit = $LASTEXITCODE
+if ($frontmatterYamlExit -eq 1) {
+    foreach ($line in $frontmatterYamlOutput) {
+        $errors.Add("frontmatter YAML: $line")
+    }
+}
+elseif ($frontmatterYamlExit -ne 0) {
+    $errors.Add("frontmatter YAML: saida nao interpretavel (exit $frontmatterYamlExit): $($frontmatterYamlOutput -join ' | ')")
+}
+
 # --- 3. Paridade de versão: VERSION (raiz) == .claude/KIT_VERSION --------
 $repoRoot = Split-Path -Parent $KitRoot
 $versionFile = Join-Path $repoRoot 'VERSION'

```

### `tests/test_frontmatter_yaml.py`
```
"""TK-77a (`docs/DIARIO_DE_OBRAS.md` `### TK-77a`) — TF/TR de `.claude/checks/frontmatter_yaml.py`
e da seção `2b` de `.claude/checks/kit_check.ps1`: o `validate` recusa frontmatter de agente ou
skill que o YAML estrito recusa. Padrão de carga do módulo idêntico a `tests/test_rdo.py`/
`tests/test_review_evidence.py` (`.claude/` não é pacote importável)."""
from __future__ import annotations

import importlib.util
import shutil
import subprocess
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
_FRONTMATTER_YAML_PATH = _ROOT / ".claude" / "checks" / "frontmatter_yaml.py"
_KIT_CHECK_PATH = _ROOT / ".claude" / "checks" / "kit_check.ps1"


def _load_frontmatter_yaml():
    spec = importlib.util.spec_from_file_location("frontmatter_yaml", _FRONTMATTER_YAML_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _pwsh_disponivel() -> bool:
    return shutil.which("pwsh") is not None


def test_frontmatter_com_dois_pontos_extra_gera_um_problema_nomeando_o_arquivo(tmp_path):
    modulo = _load_frontmatter_yaml()
    caminho = tmp_path / "agente.md"
    caminho.write_text("---\ndescription: A: b\n---\ncorpo\n", encoding="utf-8")

    resultado = modulo.problemas([caminho])

    assert len(resultado) == 1
    assert str(caminho) in resultado[0]


def test_frontmatter_com_hifen_no_lugar_dos_dois_pontos_nao_gera_problema(tmp_path):
    modulo = _load_frontmatter_yaml()
    caminho = tmp_path / "agente.md"
    caminho.write_text("---\ndescription: A - b\n---\ncorpo\n", encoding="utf-8")

    resultado = modulo.problemas([caminho])

    assert resultado == []


def test_frontmatter_que_carrega_lista_gera_um_problema(tmp_path):
    modulo = _load_frontmatter_yaml()
    caminho = tmp_path / "agente.md"
    caminho.write_text("---\n- um\n- dois\n---\ncorpo\n", encoding="utf-8")

    resultado = modulo.problemas([caminho])

    assert len(resultado) == 1
    assert "não é mapeamento" in resultado[0]


def test_frontmatter_que_carrega_escalar_gera_um_problema(tmp_path):
    modulo = _load_frontmatter_yaml()
    caminho = tmp_path / "agente.md"
    caminho.write_text("---\napenas um texto solto\n---\ncorpo\n", encoding="utf-8")

    resultado = modulo.problemas([caminho])

    assert len(resultado) == 1
    assert "não é mapeamento" in resultado[0]


def _copiar_kit(tmp_path: Path) -> Path:
    """Cópia de `.claude/` + `VERSION` sob `tmp_path`, ignorando `__pycache__` (mesmo padrão do
    card: `shutil.copytree`)."""
    destino = tmp_path / "cópia"
    shutil.copytree(
        _ROOT / ".claude",
        destino / ".claude",
        ignore=shutil.ignore_patterns("__pycache__"),
    )
    shutil.copy2(_ROOT / "VERSION", destino / "VERSION")
    return destino


def test_kit_check_valida_frontmatter_ponta_a_ponta(tmp_path):
    if not _pwsh_disponivel():
        pytest.skip("pwsh não está no PATH")

    copia = _copiar_kit(tmp_path)

    resultado_ok = subprocess.run(
        [
            "pwsh",
            "-NoProfile",
            "-File",
            str(copia / ".claude" / "checks" / "kit_check.ps1"),
            "-Mode",
            "validate",
            "-KitRoot",
            str(copia / ".claude"),
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    assert resultado_ok.returncode == 0, resultado_ok.stdout + resultado_ok.stderr

    consultor = copia / ".claude" / "agents" / "pantonic-consultant.md"
    conteudo = consultor.read_text(encoding="utf-8")
    conteudo_quebrado = conteudo.replace(
        "Efêmero - cada acionamento", "Efêmero: cada acionamento"
    )
    assert conteudo_quebrado != conteudo
    consultor.write_text(conteudo_quebrado, encoding="utf-8")

    resultado_falho = subprocess.run(
        [
            "pwsh",
            "-NoProfile",
            "-File",
            str(copia / ".claude" / "checks" / "kit_check.ps1"),
            "-Mode",
            "validate",
            "-K
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
