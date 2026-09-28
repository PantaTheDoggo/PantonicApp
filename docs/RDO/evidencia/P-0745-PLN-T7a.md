# Evidência de revisão — P-0745 PLN-T7a

## Diff (`git diff --stat`)
```
.claude/README.md                               |    2 +-
 .claude/agents/pantonic-fora-da-caixa.md        |    2 +-
 .claude/agents/pantonic-model-designer.md       |   38 +-
 .claude/agents/pantonic-planner.md              |  132 +-
 .claude/global/CLAUDE.md                        |   21 +-
 .claude/skills/bootstrap-pantonic/SKILL.md      |    2 +-
 .claude/skills/diario-de-obras/SKILL.md         |   56 +-
 .claude/skills/modelo-por-fase/SKILL.md         |    2 +-
 .claude/tools/modelo.py                         |   31 +-
 GOVERNANCA.md                                   |  192 +--
 README.md                                       |   85 +-
 docs/CUSTO_DO_PICKUP.md                         |  113 ++
 docs/DIARIO_DE_OBRAS.md                         |  693 +++++++---
 docs/DIARIO_HISTORICO.md                        |  154 +++
 docs/DOC_MAP.md                                 |   91 +-
 docs/RDO/INDEX.md                               |   17 +
 docs/RESIDENCIA_DOUTRINA.md                     |    4 +-
 docs/consultant-spec.md                         |   41 +-
 docs/plans/P-0745-planejador-modelo-operacao.md | 1537 ++++++++++++++++++++---
 docs/plans/_INBOX.md                            |    3 +-
 docs/plans/_INBOX_HISTORICO.md                  |    2 +
 docs/telemetria.tsv                             |   75 ++
 tests/fixtures/modelo/fluxo-concluido.md        |   12 +-
 tests/fixtures/modelo/fluxo-pendente.md         |   20 +-
 tests/fixtures/modelo/fluxo-valido.md           |   12 +-
 tests/fixtures/modelo/plano-invalido-2.md       |   10 +-
 tests/fixtures/modelo/plano-invalido.md         |   12 +-
 tests/fixtures/modelo/plano-sem-cabecalho.md    |    8 +-
 tests/fixtures/modelo/plano-sem-estado.md       |    8 +-
 tests/test_modelo.py                            |  127 +-
 30 files changed, 2927 insertions(+), 575 deletions(-)
```

## Arquivos tocados
- `.claude/README.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-fora-da-caixa.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-model-designer.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-planner.md` — atribuição: alheio; estado git: ` M`
- `.claude/global/CLAUDE.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/bootstrap-pantonic/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/diario-de-obras/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/modelo-por-fase/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/tools/modelo.py` — atribuição: alheio; estado git: ` M`
- `GOVERNANCA.md` — atribuição: alheio; estado git: ` M`
- `README.md` — atribuição: da entrega; estado git: ` M`
- `docs/CUSTO_DO_PICKUP.md` — atribuição: alheio; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/DIARIO_HISTORICO.md` — atribuição: alheio; estado git: ` M`
- `docs/DOC_MAP.md` — atribuição: alheio; estado git: ` M`
- `docs/OPERACOES_AS_IS.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md` — atribuição: alheio; estado git: `??`
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
- `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0745-PLN-T1.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0745-PLN-T2.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0745-PLN-T3.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0745-PLN-T4.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0745-PLN-T4a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0745-PLN-T5.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0745-PLN-T5a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0745-PLN-T6.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0745-PLN-T7.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0746-LST-T1.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0746-LST-T3.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0746-LST-T5.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0746-LST-T6.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0746-LST-T7.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0746-LST-T8.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0746-LST-T9.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-54-TK-54b.md` — atribuição: alheio; estado git: `??`
- `docs/RESIDENCIA_DOUTRINA.md` — atribuição: alheio; estado git: ` M`
- `docs/consultant-spec.md` — atribuição: alheio; estado git: ` M`
- `docs/planner-spec.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0745-planejador-modelo-operacao.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0746-lastro-do-modelo.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_INBOX.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/_INBOX_HISTORICO.md` — atribuição: alheio; estado git: ` M`
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
- `tests/test_doutrina_unidade.py` — atribuição: da entrega; estado git: `??`
- `tests/test_modelo.py` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `d75e7a6`
- Arquivos-alvo declarados: `README.md`, `tests/test_doutrina_unidade.py`
- Literais não reconhecidos como caminho (6): `- **Orçamento de turnos**`, `README.md:209,211`, `GOVERNANCA.md:78,80`, `≤30`, `**Por quê.**`, `**Onde o gerente intervém.**`
- Arquivos tocados: `.claude/README.md`, `.claude/agents/pantonic-fora-da-caixa.md`, `.claude/agents/pantonic-model-designer.md`, `.claude/agents/pantonic-planner.md`, `.claude/global/CLAUDE.md`, `.claude/skills/bootstrap-pantonic/SKILL.md`, `.claude/skills/diario-de-obras/SKILL.md`, `.claude/skills/modelo-por-fase/SKILL.md`, `.claude/tools/modelo.py`, `GOVERNANCA.md`, `README.md`, `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/DIARIO_HISTORICO.md`, `docs/DOC_MAP.md`, `docs/OPERACOES_AS_IS.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0745-PLN-T4a-o-ponteiro-sobrevivente-da-tabela-aposentada-nos-fatos-estav.md`, `docs/RDO/P-0745-PLN-T5-o-modelador-diante-do-plano-sem-cards-e-o-lastro-que-e-do-pl.md`, `docs/RDO/P-0745-PLN-T5a-a-frase-que-governa-o-gate-do-modelador-e-a-enumeracao-que-e.md`, `docs/RDO/P-0745-PLN-T6-a-especificacao-do-agente-de-planejamento.md`, `docs/RDO/P-0745-PLN-T7-o-indice-de-documentos-e-a-revisao-do-readme.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0745-PLN-T4a.md`, `docs/RDO/evidencia/P-0745-PLN-T5.md`, `docs/RDO/evidencia/P-0745-PLN-T5a.md`, `docs/RDO/evidencia/P-0745-PLN-T6.md`, `docs/RDO/evidencia/P-0745-PLN-T7.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/RESIDENCIA_DOUTRINA.md`, `docs/consultant-spec.md`, `docs/planner-spec.md`, `docs/plans/P-0745-planejador-modelo-operacao.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/telemetria.tsv`, `tests/fixtures/modelo/fluxo-concluido.md`, `tests/fixtures/modelo/fluxo-pendente.md`, `tests/fixtures/modelo/fluxo-valido.md`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/fixtures/modelo/plano-invalido.md`, `tests/fixtures/modelo/plano-sem-cabecalho.md`, `tests/fixtures/modelo/plano-sem-estado.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_doutrina_unidade.py`, `tests/test_modelo.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/README.md` → `PLN-T4`, `.claude/agents/pantonic-fora-da-caixa.md` → `PLN-T3`, `.claude/agents/pantonic-model-designer.md` → `PLN-T5`, `.claude/agents/pantonic-planner.md` → `PLN-T4`, `.claude/global/CLAUDE.md` → `PLN-T2`, `.claude/skills/bootstrap-pantonic/SKILL.md` → `PLN-T3`, `.claude/skills/diario-de-obras/SKILL.md` → `PLN-T3`, `.claude/skills/modelo-por-fase/SKILL.md` → `PLN-T3`, `GOVERNANCA.md` → `PLN-T2`, `docs/DOC_MAP.md` → `PLN-T7`, `docs/RESIDENCIA_DOUTRINA.md` → `PLN-T2`, `docs/consultant-spec.md` → `PLN-T7`, `docs/planner-spec.md` → `PLN-T6`, `docs/plans/P-0745-planejador-modelo-operacao.md` → `PLN-T1`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0745-PLN-T4a-o-ponteiro-sobrevivente-da-tabela-aposentada-nos-fatos-estav.md`, `docs/RDO/P-0745-PLN-T5-o-modelador-diante-do-plano-sem-cards-e-o-lastro-que-e-do-pl.md`, `docs/RDO/P-0745-PLN-T5a-a-frase-que-governa-o-gate-do-modelador-e-a-enumeracao-que-e.md`, `docs/RDO/P-0745-PLN-T6-a-especificacao-do-agente-de-planejamento.md`, `docs/RDO/P-0745-PLN-T7-o-indice-de-documentos-e-a-revisao-do-readme.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0745-PLN-T4a.md`, `docs/RDO/evidencia/P-0745-PLN-T5.md`, `docs/RDO/evidencia/P-0745-PLN-T5a.md`, `docs/RDO/evidencia/P-0745-PLN-T6.md`, `docs/RDO/evidencia/P-0745-PLN-T7.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/telemetria.tsv`
- Fato: 15 arquivo(s) fora dos alvos e sem atribuição: `.claude/tools/modelo.py`, `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_HISTORICO.md`, `docs/OPERACOES_AS_IS.md`, `tests/fixtures/modelo/fluxo-concluido.md`, `tests/fixtures/modelo/fluxo-pendente.md`, `tests/fixtures/modelo/fluxo-valido.md`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/fixtures/modelo/plano-invalido.md`, `tests/fixtures/modelo/plano-sem-cabecalho.md`, `tests/fixtures/modelo/plano-sem-estado.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_modelo.py`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `README.md`
```
diff --git a/README.md b/README.md
index 4cf033f..649f356 100644
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

### `tests/test_doutrina_unidade.py`
```
"""TR do P-0745 (PLN-T2..PLN-T5): a forma antiga da unidade de trabalho — percentual de
ocupação, tabela de tetos, tarefa atômica — não volta às residências que o plano editou."""
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


def _texto(rel: str) -> str:
    return (RAIZ / rel).read_text(encoding="utf-8")


def test_governanca_dimensiona_pela_operacao_sem_percentual():
    t = _texto("GOVERNANCA.md")
    assert "50% de ocupação" not in t
    assert "Orçamento de turnos por tarefa atômica" not in t
    assert "materialização de uma operação do modelo" in t


def test_global_claude_sem_percentual_nem_tarefa_atomica():
    t = _texto(".claude/global/CLAUDE.md")
    assert "50% de ocupação" not in t
    assert "tarefa atômica" not in t
    assert "tarefas atômicas" not in t


def test_skill_diario_formato_de_tarefa_pela_operacao():
    t = _texto(".claude/skills/diario-de-obras/SKILL.md")
    assert "## Formato de uma tarefa atômica" not in t
    assert "## Formato de uma tarefa\n" in t
    assert "materialização de uma operação do modelo" in t


def test_planner_decompoe_o_modelo_sem_percentual():
    t = _texto(".claude/agents/pantonic-planner.md")
    assert "atômic" not in t
    assert "50%" not in t
    assert "~80 linhas" not in t
    assert "SAÍDA 3" in t
    assert "Fase 3b" in t


def test_conduta_do_planejador_nao_remete_a_tabela_aposentada():
    t = _texto(".claude/agents/pantonic-planner.md")
    assert "tabela de classes" not in t
    assert "tabela de tetos" not in t
    assert "Nenhum teto se escreve no" in t


def test_modelador_devolve_lastro_como_saida_literal():
    t = _texto(".claude/agents/pantonic-model-designer.md")
    assert "Só cinco violações" in t
    assert "`V1` e `V3`" in t
    g = _texto("GOVERNANCA.md")
    assert "**Lastro.**" in g
    assert "**Rascunho antes do Marco 1.**" in g


def test_gate_do_modelador_nao_classifica_lastro_como_secao():
    t = _texto(".claude/agents/pantonic-model-designer.md")
    assert "exceto `V1` e `V3`" in t
    assert "(`V6`, `V7`, `V15`, `V17`)" not in t
    assert "Só cinco violações" in t


def test_readme_nao_defende_a_regua_aposentada():
    t = _texto("README.md")
    assert "Orçamento de turnos" not in t
    assert "Um teto único para tudo" not in t
    assert "Teto de turnos graduado por classe" not in t
    assert "calibrar tetos" not in t
    assert "calibração dos tetos" not in t
    assert "não cabe em ≤30" not in t
    assert "71 turnos e ~189 mil tokens" in t

```

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
