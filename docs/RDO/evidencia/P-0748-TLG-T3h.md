# Evidência de revisão — P-0748 TLG-T3h

## Diff (`git diff --stat`)
```
.claude/README.md                                  |    6 +-
 .claude/agents/pantonic-consultant.md              |   43 +-
 .claude/agents/pantonic-executor.md                |    8 +-
 .claude/agents/pantonic-fora-da-caixa.md           |    2 +-
 .claude/agents/pantonic-model-designer.md          |   56 +-
 .claude/agents/pantonic-planner.md                 |  160 +-
 .claude/agents/pantonic-reviewer.md                |    4 +-
 .claude/global/CLAUDE.md                           |   23 +-
 .../hooks/modelo_por_fase_userpromptsubmit.py      |    8 +-
 .claude/projecoes.json                             |   38 +
 .claude/skills/bootstrap-pantonic/SKILL.md         |    2 +-
 .claude/skills/diario-de-obras/SKILL.md            |   71 +-
 .claude/skills/modelo-por-fase/SKILL.md            |   26 +-
 .claude/skills/passagem-de-bastao/SKILL.md         |   15 +-
 .claude/skills/scrum-master/SKILL.md               |  101 +-
 .claude/tools/modelo.py                            |   31 +-
 .claude/tools/review_evidence.py                   |   31 +-
 GOVERNANCA.md                                      |  232 +--
 README.md                                          |  122 +-
 docs/CUSTO_DO_PICKUP.md                            |  113 ++
 docs/DIARIO_DE_OBRAS.md                            | 1333 ++++++++++++++--
 docs/DIARIO_HISTORICO.md                           |  154 ++
 docs/DOC_MAP.md                                    |  110 +-
 docs/RDO/INDEX.md                                  |   58 +
 docs/RESIDENCIA_DOUTRINA.md                        |    4 +-
 docs/consultant-spec.md                            |   75 +-
 docs/plans/P-0745-planejador-modelo-operacao.md    | 1584 ++++++++++++++++++--
 docs/plans/_INBOX.md                               |    3 +-
 docs/plans/_INBOX_HISTORICO.md                     |    4 +
 docs/telemetria.tsv                                |  205 +++
 tests/fixtures/modelo/fluxo-concluido.md           |   12 +-
 tests/fixtures/modelo/fluxo-pendente.md            |   20 +-
 tests/fixtures/modelo/fluxo-valido.md              |   12 +-
 tests/fixtures/modelo/plano-invalido-2.md          |   10 +-
 tests/fixtures/modelo/plano-invalido.md            |   12 +-
 tests/fixtures/modelo/plano-sem-cabecalho.md       |    8 +-
 tests/fixtures/modelo/plano-sem-estado.md          |    8 +-
 tests/test_modelo.py                               |  127 +-
 tests/test_review_evidence.py                      |   50 +
 39 files changed, 4153 insertions(+), 728 deletions(-)
```

## Arquivos tocados
- `.claude/skills/scrum-master/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/progresso_hook.py` — atribuição: da entrega; estado git: `??`
- `docs/ACIONAMENTOS_CONSULTOR.tsv` — atribuição: alheio; estado git: `??`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/OPERACOES_AS_IS.md` — atribuição: alheio; estado git: `??`
- `docs/OPERACOES_AS_IS_P-0745.md` — atribuição: alheio; estado git: `??`
- `docs/OPERACOES_AS_IS_P-0747.md` — atribuição: alheio; estado git: `??`
- `docs/OPERACOES_AS_IS_P-0748.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-76a-as-tabelas-do-modelo-em-frases-curtas-para-o-dono.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-78a-o-loop-nao-para-para-rebaixar-o-modelo.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-78b-a-regua-do-card-aprende-as-tres-licoes-da-janela.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-78c-a-evidencia-mede-so-o-que-mudou-desde-o-despacho.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-78d-a-doutrina-e-o-readme-deixam-de-mandar-parar-para-rebaixar-o.md` — atribuição: alheio; estado git: `??`
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
- `docs/RDO/P-0748-TLG-T4-o-condutor-narra-uma-linha-do-repertorio-antes-de-cada-ato-n.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0748-TLG-T4a-a-skill-deixa-de-narrar-a-transicao-chega-ao-painel-pela-fun.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0748-TLG-T5-a-porta-de-entrada-diz-como-o-dono-acompanha-a-execucao-no-p.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0748-TLG-T5a-a-celula-da-scrum-master-na-tabela-de-skills-volta-a-dizer-q.md` — atribuição: alheio; estado git: `??`
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
- `docs/RDO/evidencia/P-0748-TLG-T4.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0748-TLG-T4a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0748-TLG-T5.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0748-TLG-T5a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-54-TK-54b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-76-TK-76a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-78-TK-78a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-78-TK-78b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-78-TK-78c.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-78-TK-78d.md` — atribuição: alheio; estado git: `??`
- `docs/planner-spec.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0746-lastro-do-modelo.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0747-consultor-de-plano.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0748-tela-do-gerente.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CAMPANHA-P-0748.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-P-0747.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-P-0748.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_CENARIO-TK-78.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_VEREDITO-procedimentos-2026-09-22.md` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/modelo/plano-com-lastro.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-sem-lastro.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-terminal-sem-lastro.md` — atribuição: alheio; estado git: `??`
- `tests/test_doutrina_unidade.py` — atribuição: alheio; estado git: `??`
- `tests/test_progresso_hook.py` — atribuição: da entrega; estado git: `??`

## Escopo
- Recorte: desde `6801e0cc9fe89d37129c37a11a858a40783930cf`
- Arquivos-alvo declarados: `.claude/tools/progresso_hook.py`, `re.search`, `tests/test_progresso_hook.py`, `.claude/skills/scrum-master/SKILL.md`
- Literais não reconhecidos como caminho (8): `backlog\.py status`, `if m:`, `M-4`, `M-7`, `M-9`, `M-16`, `## Guardrails`, `- O gerente acompanha a execução num painel`
- Arquivos tocados: `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/progresso_hook.py`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/DIARIO_DE_OBRAS.md`, `docs/OPERACOES_AS_IS.md`, `docs/OPERACOES_AS_IS_P-0745.md`, `docs/OPERACOES_AS_IS_P-0747.md`, `docs/OPERACOES_AS_IS_P-0748.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-76a-as-tabelas-do-modelo-em-frases-curtas-para-o-dono.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78a-o-loop-nao-para-para-rebaixar-o-modelo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78b-a-regua-do-card-aprende-as-tres-licoes-da-janela.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78c-a-evidencia-mede-so-o-que-mudou-desde-o-despacho.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78d-a-doutrina-e-o-readme-deixam-de-mandar-parar-para-rebaixar-o.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0745-PLN-T4a-o-ponteiro-sobrevivente-da-tabela-aposentada-nos-fatos-estav.md`, `docs/RDO/P-0745-PLN-T5-o-modelador-diante-do-plano-sem-cards-e-o-lastro-que-e-do-pl.md`, `docs/RDO/P-0745-PLN-T5a-a-frase-que-governa-o-gate-do-modelador-e-a-enumeracao-que-e.md`, `docs/RDO/P-0745-PLN-T6-a-especificacao-do-agente-de-planejamento.md`, `docs/RDO/P-0745-PLN-T7-o-indice-de-documentos-e-a-revisao-do-readme.md`, `docs/RDO/P-0745-PLN-T7a-o-readme-deixa-de-defender-a-regua-que-ele-mesmo-aposenta.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/P-0747-CON-T1-o-consultor-entra-na-doutrina-de-governanca.md`, `docs/RDO/P-0747-CON-T2-a-definicao-de-conduta-do-consultor-sem-estatuto-provisorio.md`, `docs/RDO/P-0747-CON-T2a-corretivo-da-op-2-o-agente-descreve-o-cenario-persistido-e-l.md`, `docs/RDO/P-0747-CON-T2b-corretivo-da-op-2-o-agente-nomeia-a-recusa-do-impedimento-im.md`, `docs/RDO/P-0747-CON-T3-o-loop-leva-toda-parada-ao-consultor.md`, `docs/RDO/P-0747-CON-T3a-corretivo-da-op-3-a-parada-e-a-mesma-em-todas-as-regras-que.md`, `docs/RDO/P-0747-CON-T3b-corretivo-da-op-3-com-estrategico-o-loop-para-sem-executar-a.md`, `docs/RDO/P-0747-CON-T3c-corretivo-da-op-3-com-estrategico-a-rota-planejador-executa.md`, `docs/RDO/P-0747-CON-T3d-corretivo-da-op-3-o-loop-redespacha-sem-retentativa-o-card-c.md`, `docs/RDO/P-0747-CON-T4-a-forma-efemera-com-cenario-persistido.md`, `docs/RDO/P-0747-CON-T4a-corretivo-da-op-4-a-queda-de-uma-instancia-do-consultor-nao.md`, `docs/RDO/P-0747-CON-T5-o-outro-lado-da-fronteira-nas-definicoes-de-conduta.md`, `docs/RDO/P-0747-CON-T5a-corretivo-da-op-5-o-diario-e-a-regra-8-dizem-o-que-a-triagem.md`, `docs/RDO/P-0747-CON-T6-a-especificacao-vira-lastro-medido.md`, `docs/RDO/P-0747-CON-T6a-corretivo-da-op-6-a-spec-nao-prevalece-sobre-o-bloco-a.md`, `docs/RDO/P-0747-CON-T7-a-medida-do-piloto-da-forma-efemera.md`, `docs/RDO/P-0747-CON-T7a-corretivo-da-op-7-o-veredito-declara-o-modelo-das-instancias.md`, `docs/RDO/P-0747-CON-T8-a-porta-de-entrada-e-a-descricao-do-agente.md`, `docs/RDO/P-0747-CON-T8a-corretivo-da-op-8-a-description-volta-ao-yaml-que-o-harness.md`, `docs/RDO/P-0748-TLG-T1-a-sonda-de-viabilidade-diante-do-dono.md`, `docs/RDO/P-0748-TLG-T2-o-repertorio-de-mensagens-na-skill-do-loop.md`, `docs/RDO/P-0748-TLG-T2a-o-repertorio-deixa-de-citar-o-comando-que-nao-vai-existir.md`, `docs/RDO/P-0748-TLG-T2b-o-repertorio-como-tabela-de-eventos-a-skill-diz-o-que-a-func.md`, `docs/RDO/P-0748-TLG-T3-o-gancho-que-grava-o-arquivo-de-progresso.md`, `docs/RDO/P-0748-TLG-T3a-a-captura-do-payload-dos-ganchos-o-que-a-funcao-vai-ler.md`, `docs/RDO/P-0748-TLG-T3b-a-funcao-que-gera-a-linha-do-stream-a-cada-evento-do-loop.md`, `docs/RDO/P-0748-TLG-T3c-o-painel-nao-perde-linha-e-nao-afirma-o-que-nao-aconteceu.md`, `docs/RDO/P-0748-TLG-T3d-o-painel-so-diz-que-a-janela-encerrou-quando-ela-encerrou.md`, `docs/RDO/P-0748-TLG-T3e-o-painel-diz-so-o-que-o-gancho-ve-o-modelo-mostrado-e-o-cons.md`, `docs/RDO/P-0748-TLG-T3f-o-estado-do-gancho-nao-guarda-chave-que-ninguem-le.md`, `docs/RDO/P-0748-TLG-T3g-o-painel-reconhece-o-retorno-do-agente-com-o-ou-o-colchete-a.md`, `docs/RDO/P-0748-TLG-T4-o-condutor-narra-uma-linha-do-repertorio-antes-de-cada-ato-n.md`, `docs/RDO/P-0748-TLG-T4a-a-skill-deixa-de-narrar-a-transicao-chega-ao-painel-pela-fun.md`, `docs/RDO/P-0748-TLG-T5-a-porta-de-entrada-diz-como-o-dono-acompanha-a-execucao-no-p.md`, `docs/RDO/P-0748-TLG-T5a-a-celula-da-scrum-master-na-tabela-de-skills-volta-a-dizer-q.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0745-PLN-T4a.md`, `docs/RDO/evidencia/P-0745-PLN-T5.md`, `docs/RDO/evidencia/P-0745-PLN-T5a.md`, `docs/RDO/evidencia/P-0745-PLN-T6.md`, `docs/RDO/evidencia/P-0745-PLN-T7.md`, `docs/RDO/evidencia/P-0745-PLN-T7a.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/P-0747-CON-T1.md`, `docs/RDO/evidencia/P-0747-CON-T2.md`, `docs/RDO/evidencia/P-0747-CON-T2a.md`, `docs/RDO/evidencia/P-0747-CON-T2b.md`, `docs/RDO/evidencia/P-0747-CON-T3.md`, `docs/RDO/evidencia/P-0747-CON-T3a.md`, `docs/RDO/evidencia/P-0747-CON-T3b.md`, `docs/RDO/evidencia/P-0747-CON-T3c.md`, `docs/RDO/evidencia/P-0747-CON-T3d.md`, `docs/RDO/evidencia/P-0747-CON-T4.md`, `docs/RDO/evidencia/P-0747-CON-T4a.md`, `docs/RDO/evidencia/P-0747-CON-T5.md`, `docs/RDO/evidencia/P-0747-CON-T5a.md`, `docs/RDO/evidencia/P-0747-CON-T6.md`, `docs/RDO/evidencia/P-0747-CON-T6a.md`, `docs/RDO/evidencia/P-0747-CON-T7.md`, `docs/RDO/evidencia/P-0747-CON-T7a.md`, `docs/RDO/evidencia/P-0747-CON-T8.md`, `docs/RDO/evidencia/P-0747-CON-T8a.md`, `docs/RDO/evidencia/P-0748-TLG-T1.md`, `docs/RDO/evidencia/P-0748-TLG-T2.md`, `docs/RDO/evidencia/P-0748-TLG-T2a.md`, `docs/RDO/evidencia/P-0748-TLG-T2b.md`, `docs/RDO/evidencia/P-0748-TLG-T3.md`, `docs/RDO/evidencia/P-0748-TLG-T3a.md`, `docs/RDO/evidencia/P-0748-TLG-T3b.md`, `docs/RDO/evidencia/P-0748-TLG-T3c.md`, `docs/RDO/evidencia/P-0748-TLG-T3d.md`, `docs/RDO/evidencia/P-0748-TLG-T3e.md`, `docs/RDO/evidencia/P-0748-TLG-T3f.md`, `docs/RDO/evidencia/P-0748-TLG-T3g.md`, `docs/RDO/evidencia/P-0748-TLG-T4.md`, `docs/RDO/evidencia/P-0748-TLG-T4a.md`, `docs/RDO/evidencia/P-0748-TLG-T5.md`, `docs/RDO/evidencia/P-0748-TLG-T5a.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/RDO/evidencia/TK-76-TK-76a.md`, `docs/RDO/evidencia/TK-78-TK-78a.md`, `docs/RDO/evidencia/TK-78-TK-78b.md`, `docs/RDO/evidencia/TK-78-TK-78c.md`, `docs/RDO/evidencia/TK-78-TK-78d.md`, `docs/planner-spec.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/P-0747-consultor-de-plano.md`, `docs/plans/P-0748-tela-do-gerente.md`, `docs/plans/_CAMPANHA-P-0748.md`, `docs/plans/_CENARIO-P-0747.md`, `docs/plans/_CENARIO-P-0748.md`, `docs/plans/_CENARIO-TK-78.md`, `docs/plans/_VEREDITO-procedimentos-2026-09-22.md`, `docs/telemetria.tsv`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_doutrina_unidade.py`, `tests/test_progresso_hook.py`
- Atribuídos a outra tarefa do mesmo plano: `docs/plans/P-0748-tela-do-gerente.md` → `TLG-T1`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-76a-as-tabelas-do-modelo-em-frases-curtas-para-o-dono.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78a-o-loop-nao-para-para-rebaixar-o-modelo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78b-a-regua-do-card-aprende-as-tres-licoes-da-janela.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78c-a-evidencia-mede-so-o-que-mudou-desde-o-despacho.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-78d-a-doutrina-e-o-readme-deixam-de-mandar-parar-para-rebaixar-o.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0745-PLN-T4a-o-ponteiro-sobrevivente-da-tabela-aposentada-nos-fatos-estav.md`, `docs/RDO/P-0745-PLN-T5-o-modelador-diante-do-plano-sem-cards-e-o-lastro-que-e-do-pl.md`, `docs/RDO/P-0745-PLN-T5a-a-frase-que-governa-o-gate-do-modelador-e-a-enumeracao-que-e.md`, `docs/RDO/P-0745-PLN-T6-a-especificacao-do-agente-de-planejamento.md`, `docs/RDO/P-0745-PLN-T7-o-indice-de-documentos-e-a-revisao-do-readme.md`, `docs/RDO/P-0745-PLN-T7a-o-readme-deixa-de-defender-a-regua-que-ele-mesmo-aposenta.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/P-0747-CON-T1-o-consultor-entra-na-doutrina-de-governanca.md`, `docs/RDO/P-0747-CON-T2-a-definicao-de-conduta-do-consultor-sem-estatuto-provisorio.md`, `docs/RDO/P-0747-CON-T2a-corretivo-da-op-2-o-agente-descreve-o-cenario-persistido-e-l.md`, `docs/RDO/P-0747-CON-T2b-corretivo-da-op-2-o-agente-nomeia-a-recusa-do-impedimento-im.md`, `docs/RDO/P-0747-CON-T3-o-loop-leva-toda-parada-ao-consultor.md`, `docs/RDO/P-0747-CON-T3a-corretivo-da-op-3-a-parada-e-a-mesma-em-todas-as-regras-que.md`, `docs/RDO/P-0747-CON-T3b-corretivo-da-op-3-com-estrategico-o-loop-para-sem-executar-a.md`, `docs/RDO/P-0747-CON-T3c-corretivo-da-op-3-com-estrategico-a-rota-planejador-executa.md`, `docs/RDO/P-0747-CON-T3d-corretivo-da-op-3-o-loop-redespacha-sem-retentativa-o-card-c.md`, `docs/RDO/P-0747-CON-T4-a-forma-efemera-com-cenario-persistido.md`, `docs/RDO/P-0747-CON-T4a-corretivo-da-op-4-a-queda-de-uma-instancia-do-consultor-nao.md`, `docs/RDO/P-0747-CON-T5-o-outro-lado-da-fronteira-nas-definicoes-de-conduta.md`, `docs/RDO/P-0747-CON-T5a-corretivo-da-op-5-o-diario-e-a-regra-8-dizem-o-que-a-triagem.md`, `docs/RDO/P-0747-CON-T6-a-especificacao-vira-lastro-medido.md`, `docs/RDO/P-0747-CON-T6a-corretivo-da-op-6-a-spec-nao-prevalece-sobre-o-bloco-a.md`, `docs/RDO/P-0747-CON-T7-a-medida-do-piloto-da-forma-efemera.md`, `docs/RDO/P-0747-CON-T7a-corretivo-da-op-7-o-veredito-declara-o-modelo-das-instancias.md`, `docs/RDO/P-0747-CON-T8-a-porta-de-entrada-e-a-descricao-do-agente.md`, `docs/RDO/P-0747-CON-T8a-corretivo-da-op-8-a-description-volta-ao-yaml-que-o-harness.md`, `docs/RDO/P-0748-TLG-T1-a-sonda-de-viabilidade-diante-do-dono.md`, `docs/RDO/P-0748-TLG-T2-o-repertorio-de-mensagens-na-skill-do-loop.md`, `docs/RDO/P-0748-TLG-T2a-o-repertorio-deixa-de-citar-o-comando-que-nao-vai-existir.md`, `docs/RDO/P-0748-TLG-T2b-o-repertorio-como-tabela-de-eventos-a-skill-diz-o-que-a-func.md`, `docs/RDO/P-0748-TLG-T3-o-gancho-que-grava-o-arquivo-de-progresso.md`, `docs/RDO/P-0748-TLG-T3a-a-captura-do-payload-dos-ganchos-o-que-a-funcao-vai-ler.md`, `docs/RDO/P-0748-TLG-T3b-a-funcao-que-gera-a-linha-do-stream-a-cada-evento-do-loop.md`, `docs/RDO/P-0748-TLG-T3c-o-painel-nao-perde-linha-e-nao-afirma-o-que-nao-aconteceu.md`, `docs/RDO/P-0748-TLG-T3d-o-painel-so-diz-que-a-janela-encerrou-quando-ela-encerrou.md`, `docs/RDO/P-0748-TLG-T3e-o-painel-diz-so-o-que-o-gancho-ve-o-modelo-mostrado-e-o-cons.md`, `docs/RDO/P-0748-TLG-T3f-o-estado-do-gancho-nao-guarda-chave-que-ninguem-le.md`, `docs/RDO/P-0748-TLG-T3g-o-painel-reconhece-o-retorno-do-agente-com-o-ou-o-colchete-a.md`, `docs/RDO/P-0748-TLG-T4-o-condutor-narra-uma-linha-do-repertorio-antes-de-cada-ato-n.md`, `docs/RDO/P-0748-TLG-T4a-a-skill-deixa-de-narrar-a-transicao-chega-ao-painel-pela-fun.md`, `docs/RDO/P-0748-TLG-T5-a-porta-de-entrada-diz-como-o-dono-acompanha-a-execucao-no-p.md`, `docs/RDO/P-0748-TLG-T5a-a-celula-da-scrum-master-na-tabela-de-skills-volta-a-dizer-q.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0745-PLN-T4a.md`, `docs/RDO/evidencia/P-0745-PLN-T5.md`, `docs/RDO/evidencia/P-0745-PLN-T5a.md`, `docs/RDO/evidencia/P-0745-PLN-T6.md`, `docs/RDO/evidencia/P-0745-PLN-T7.md`, `docs/RDO/evidencia/P-0745-PLN-T7a.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/P-0747-CON-T1.md`, `docs/RDO/evidencia/P-0747-CON-T2.md`, `docs/RDO/evidencia/P-0747-CON-T2a.md`, `docs/RDO/evidencia/P-0747-CON-T2b.md`, `docs/RDO/evidencia/P-0747-CON-T3.md`, `docs/RDO/evidencia/P-0747-CON-T3a.md`, `docs/RDO/evidencia/P-0747-CON-T3b.md`, `docs/RDO/evidencia/P-0747-CON-T3c.md`, `docs/RDO/evidencia/P-0747-CON-T3d.md`, `docs/RDO/evidencia/P-0747-CON-T4.md`, `docs/RDO/evidencia/P-0747-CON-T4a.md`, `docs/RDO/evidencia/P-0747-CON-T5.md`, `docs/RDO/evidencia/P-0747-CON-T5a.md`, `docs/RDO/evidencia/P-0747-CON-T6.md`, `docs/RDO/evidencia/P-0747-CON-T6a.md`, `docs/RDO/evidencia/P-0747-CON-T7.md`, `docs/RDO/evidencia/P-0747-CON-T7a.md`, `docs/RDO/evidencia/P-0747-CON-T8.md`, `docs/RDO/evidencia/P-0747-CON-T8a.md`, `docs/RDO/evidencia/P-0748-TLG-T1.md`, `docs/RDO/evidencia/P-0748-TLG-T2.md`, `docs/RDO/evidencia/P-0748-TLG-T2a.md`, `docs/RDO/evidencia/P-0748-TLG-T2b.md`, `docs/RDO/evidencia/P-0748-TLG-T3.md`, `docs/RDO/evidencia/P-0748-TLG-T3a.md`, `docs/RDO/evidencia/P-0748-TLG-T3b.md`, `docs/RDO/evidencia/P-0748-TLG-T3c.md`, `docs/RDO/evidencia/P-0748-TLG-T3d.md`, `docs/RDO/evidencia/P-0748-TLG-T3e.md`, `docs/RDO/evidencia/P-0748-TLG-T3f.md`, `docs/RDO/evidencia/P-0748-TLG-T3g.md`, `docs/RDO/evidencia/P-0748-TLG-T4.md`, `docs/RDO/evidencia/P-0748-TLG-T4a.md`, `docs/RDO/evidencia/P-0748-TLG-T5.md`, `docs/RDO/evidencia/P-0748-TLG-T5a.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/RDO/evidencia/TK-76-TK-76a.md`, `docs/RDO/evidencia/TK-78-TK-78a.md`, `docs/RDO/evidencia/TK-78-TK-78b.md`, `docs/RDO/evidencia/TK-78-TK-78c.md`, `docs/RDO/evidencia/TK-78-TK-78d.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/P-0747-consultor-de-plano.md`, `docs/plans/_CAMPANHA-P-0748.md`, `docs/plans/_CENARIO-P-0747.md`, `docs/plans/_CENARIO-P-0748.md`, `docs/plans/_CENARIO-TK-78.md`, `docs/plans/_VEREDITO-procedimentos-2026-09-22.md`, `docs/telemetria.tsv`
- Fato: 10 arquivo(s) fora dos alvos e sem atribuição: `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/OPERACOES_AS_IS.md`, `docs/OPERACOES_AS_IS_P-0745.md`, `docs/OPERACOES_AS_IS_P-0747.md`, `docs/OPERACOES_AS_IS_P-0748.md`, `docs/planner-spec.md`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_doutrina_unidade.py`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/progresso_hook.py`
```
"""Ganchos `PreToolUse`, `PostToolUse`, `UserPromptSubmit` e `Stop` do `P-0748` (`OP-3`):
gera em `.claude/estado/progresso.txt` uma frase por evento de transição do loop, com o
título da tarefa no lugar da sigla. Falha aberta total: qualquer exceção em `main` é
silenciada e o script sempre sai `0`; nunca imprime. Captura de payload opcional (flag
`progresso-captura.on`).
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from pathlib import Path

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
}


def capturar(payload: dict, estado: Path) -> None:
    try:
        if not (estado / CAPTURA_FLAG).exists():
            return
        arq = estado / CAPTURA_ARQ
        if arq.exists() and arq.stat().st_size > CAPTURA_TETO_BYTES:
            return
        ti = payload.get("tool_input")
        resp = payload.get("tool_response")
        registro = {
            "evento": payload.get("hook_event_name"),
            "tool": payload.get("tool_name"),
            "input_chaves": sorted(ti.keys()) if isinstance(ti, dict) else type(ti).__name__,
            "command": str(ti.get("command", ""))[:120] if isinstance(ti, dict) else "",
            "subagent_type": ti.get("subagent_type") if isinstance(ti, dict) else None,
            "response_tipo": type(resp).__name__,
            "response_chaves": sorted(resp.keys()) i
```
[truncado em 4000 caracteres]

### `re.search`
```
(sem diferença coletável — arquivo ausente na árvore de trabalho)
```

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

### `.claude/skills/scrum-master/SKILL.md`
```
diff --git a/.claude/skills/scrum-master/SKILL.md b/.claude/skills/scrum-master/SKILL.md
index b588cdd..5069a51 100644
--- a/.claude/skills/scrum-master/SKILL.md
+++ b/.claude/skills/scrum-master/SKILL.md
@@ -329,13 +329,13 @@ ao gerente (`I-12`). Outras ferramentas, outros comandos e outros `subagent_type
 | `M-2` | estado mudado para in-progress — `PreToolUse` · `Bash` · `command` casa `backlog\.py status (\S+) in-progress` | `Tarefa "<título>": gates aprovados; vou materializar in-progress e gravar o ponto de partida.` | `<título>` ← estado se `<ID>` é a `tarefa` do estado, senão `localizar_card(<ID>)`. `status <ID> review` não gera linha |
 | `M-3` | agente despachado, executor — `PreToolUse` · `Agent` · `subagent_type` = `pantonic-executor` · objetivo não vazio | `Agente executor recebe a tarefa "<título>" e vai executar: <objetivo>` | `<título>`, `<objetivo>` ← tarefa corrente (`DTG-33` (iv)) e `localizar_card`; `<objetivo>` já termina em ponto, ou em `…` se truncado |
 | `M-3b` | o mesmo evento de `M-3`, objetivo vazio | `Agente executor recebe a tarefa "<título>" e vai executar o card.` | `<título>` como em `M-3` |
-| `M-4` | agente de volta, executor — `PostToolUse` · `Agent` · `pantonic-executor` · primeira linha não vazia da resposta casa `^(\S+) review(?:\s+\[?pendencia=(.*?)\]?)?$` | `Agente executor devolveu a tarefa "<título>": review — <pendência>.` | `<pendência>` ← grupo 2; ausente → `sem pendência` |
+| `M-4` | agente de volta, executor — `PostToolUse` · `Agent` · `pantonic-executor`; se o agente entregou em hand-back (`handback` = `send` na resposta, e o `PostToolUse` só grava `pendentes[agentId]`), `UserPromptSubmit` com `prompt` começando por `<agent-message from="<agentId>">` de agente em `pendentes`, e a resposta é o trecho depois de `The report follows:` (`DTG-39`) · primeira linha não vazia da resposta casa `^(\S+) review(?:\s+\[?pendencia=(.*?)\]?)?$` | `Agente executor devolveu a tarefa "<título>": review — <pendência>.` | `<pendência>` ← grupo 2; ausente → `sem pendência` |
 | `M-4b` | o mesmo evento, primeira linha casa `^(\S+) blocked motivo=(\S+)\s*(.*)$` | `Agente executor devolveu a tarefa "<título>": blocked — motivo <motivo>: <razão>.` | `<motivo>` ← grupo 2; `<razão>` ← grupo 3 |
 | `M-5` | evidência coletada — `PreToolUse` · `Bash` · `command` contém `review_evidence.py` e `--tarefa <ID>`, e não contém `--atribuir` | `Tarefa "<título>": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.` | `<ID>` ← `--tarefa (\S+)` no comando; `<título>` ← estado ou `localizar_card` |
 | `M-6` | agente despachado, revisor — `PreToolUse` · `Agent` · `pantonic-reviewer` | `Agente revisor recebe a tarefa "<título>" e vai confrontar a entrega com o card.` | `<título>` ← tarefa corrente |
-| `M-7` | agente de volta, revisor — `PostToolUse` · `Agent` · `pantonic-reviewer` · primeira linha casa `^(\S+) (\S+) (\d+)%? bloqueante=(.*)$` | `Agente revisor devolveu a tarefa "<título>": <veredito> <percentual>%, bloqueante <bloqueante>.` | `<veredito>` ← grupo 2; `<percentual>` ← grupo 3; `<bloqueante>` ← grupo 4 |
+| `M-7` | agente de volta, revisor — `PostToolUse` · `Agent` · `pantonic-reviewer`, ou o `UserPromptSubmit` da volta em hand-back, como em `M-4` · primeira linha casa `^(\S+) (\S+) (\d+)%? bloqueante=(.*)$` | `Agente revisor devolveu a tarefa "<título>": <veredito> <percentual>%, bloqueante <bloqueante>.` | `<veredito>` ← grupo 2; `<percentual>` ← grupo 3; `<bloqueante>` ← grupo 4 |
 | `M-8` | agente despachado, consultor — `PreToolUse` · `Agent` · `pantonic-consultant` | `Agente consultor recebe a tarefa "<título>" e vai triar.` | `<título>` ← tarefa corrente. A regra A-n/B-n saiu (`DTG-34`); "a parada" saiu (`DTG-48`): o consultor também é despachado por laudo, por instrumento e no marco, e o evento não diz por qual |
-| `M-9` | agente de volta, consultor — `PostToolUse` · `Agent` · `pantonic-consultant` · uma linha da re
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
