# Evidência de revisão — DIARIO_DE_OBRAS TK-76a

## Diff (`git diff --stat`)
```
.claude/README.md                               |    2 +-
 .claude/agents/pantonic-fora-da-caixa.md        |    2 +-
 .claude/agents/pantonic-model-designer.md       |   54 +-
 .claude/agents/pantonic-planner.md              |  135 +-
 .claude/global/CLAUDE.md                        |   21 +-
 .claude/skills/bootstrap-pantonic/SKILL.md      |    2 +-
 .claude/skills/diario-de-obras/SKILL.md         |   56 +-
 .claude/skills/modelo-por-fase/SKILL.md         |    2 +-
 .claude/tools/modelo.py                         |   31 +-
 GOVERNANCA.md                                   |  198 ++-
 README.md                                       |   85 +-
 docs/CUSTO_DO_PICKUP.md                         |  113 ++
 docs/DIARIO_DE_OBRAS.md                         |  900 ++++++++++---
 docs/DIARIO_HISTORICO.md                        |  154 +++
 docs/DOC_MAP.md                                 |   91 +-
 docs/RDO/INDEX.md                               |   18 +
 docs/RESIDENCIA_DOUTRINA.md                     |    4 +-
 docs/consultant-spec.md                         |   41 +-
 docs/plans/P-0745-planejador-modelo-operacao.md | 1584 ++++++++++++++++++++---
 docs/plans/_INBOX.md                            |    3 +-
 docs/plans/_INBOX_HISTORICO.md                  |    3 +
 docs/telemetria.tsv                             |   84 ++
 tests/fixtures/modelo/fluxo-concluido.md        |   12 +-
 tests/fixtures/modelo/fluxo-pendente.md         |   20 +-
 tests/fixtures/modelo/fluxo-valido.md           |   12 +-
 tests/fixtures/modelo/plano-invalido-2.md       |   10 +-
 tests/fixtures/modelo/plano-invalido.md         |   12 +-
 tests/fixtures/modelo/plano-sem-cabecalho.md    |    8 +-
 tests/fixtures/modelo/plano-sem-estado.md       |    8 +-
 tests/test_modelo.py                            |  127 +-
 30 files changed, 3214 insertions(+), 578 deletions(-)
```

## Arquivos tocados
- `.claude/README.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-fora-da-caixa.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-model-designer.md` — atribuição: da entrega; estado git: ` M`
- `.claude/agents/pantonic-planner.md` — atribuição: da entrega; estado git: ` M`
- `.claude/global/CLAUDE.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/bootstrap-pantonic/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/diario-de-obras/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/modelo-por-fase/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/tools/modelo.py` — atribuição: alheio; estado git: ` M`
- `GOVERNANCA.md` — atribuição: da entrega; estado git: ` M`
- `README.md` — atribuição: alheio; estado git: ` M`
- `docs/CUSTO_DO_PICKUP.md` — atribuição: alheio; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/DIARIO_HISTORICO.md` — atribuição: alheio; estado git: ` M`
- `docs/DOC_MAP.md` — atribuição: alheio; estado git: ` M`
- `docs/OPERACOES_AS_IS.md` — atribuição: alheio; estado git: `??`
- `docs/OPERACOES_AS_IS_P-0745.md` — atribuição: alheio; estado git: `??`
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
- `docs/RDO/P-0745-PLN-T7a-o-readme-deixa-de-defender-a-regua-que-ele-mesmo-aposenta.md` — atribuição: alheio; estado git: `??`
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
- `docs/RDO/evidencia/P-0745-PLN-T7a.md` — atribuição: alheio; estado git: `??`
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
- `docs/plans/P-0747-consultor-de-plano.md` — atribuição: alheio; estado git: `??`
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
- Arquivos-alvo declarados: `.claude/agents/pantonic-model-designer.md`, `GOVERNANCA.md`, `.claude/agents/pantonic-planner.md`
- Arquivos tocados: `.claude/README.md`, `.claude/agents/pantonic-fora-da-caixa.md`, `.claude/agents/pantonic-model-designer.md`, `.claude/agents/pantonic-planner.md`, `.claude/global/CLAUDE.md`, `.claude/skills/bootstrap-pantonic/SKILL.md`, `.claude/skills/diario-de-obras/SKILL.md`, `.claude/skills/modelo-por-fase/SKILL.md`, `.claude/tools/modelo.py`, `GOVERNANCA.md`, `README.md`, `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/DIARIO_HISTORICO.md`, `docs/DOC_MAP.md`, `docs/OPERACOES_AS_IS.md`, `docs/OPERACOES_AS_IS_P-0745.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0745-PLN-T4a-o-ponteiro-sobrevivente-da-tabela-aposentada-nos-fatos-estav.md`, `docs/RDO/P-0745-PLN-T5-o-modelador-diante-do-plano-sem-cards-e-o-lastro-que-e-do-pl.md`, `docs/RDO/P-0745-PLN-T5a-a-frase-que-governa-o-gate-do-modelador-e-a-enumeracao-que-e.md`, `docs/RDO/P-0745-PLN-T6-a-especificacao-do-agente-de-planejamento.md`, `docs/RDO/P-0745-PLN-T7-o-indice-de-documentos-e-a-revisao-do-readme.md`, `docs/RDO/P-0745-PLN-T7a-o-readme-deixa-de-defender-a-regua-que-ele-mesmo-aposenta.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0745-PLN-T4a.md`, `docs/RDO/evidencia/P-0745-PLN-T5.md`, `docs/RDO/evidencia/P-0745-PLN-T5a.md`, `docs/RDO/evidencia/P-0745-PLN-T6.md`, `docs/RDO/evidencia/P-0745-PLN-T7.md`, `docs/RDO/evidencia/P-0745-PLN-T7a.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/RESIDENCIA_DOUTRINA.md`, `docs/consultant-spec.md`, `docs/planner-spec.md`, `docs/plans/P-0745-planejador-modelo-operacao.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/P-0747-consultor-de-plano.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VEREDITO-procedimentos-2026-09-22.md`, `docs/telemetria.tsv`, `tests/fixtures/modelo/fluxo-concluido.md`, `tests/fixtures/modelo/fluxo-pendente.md`, `tests/fixtures/modelo/fluxo-valido.md`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/fixtures/modelo/plano-invalido.md`, `tests/fixtures/modelo/plano-sem-cabecalho.md`, `tests/fixtures/modelo/plano-sem-estado.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_doutrina_unidade.py`, `tests/test_modelo.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/README.md` → `TK-64a`, `README.md` → `TK-51a`, `docs/CUSTO_DO_PICKUP.md` → `TK-54b`, `docs/DIARIO_DE_OBRAS.md` → `TK-54b`, `docs/DOC_MAP.md` → `TK-54b`
- Registro da orquestração (não atribuível a tarefa): `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0745-PLN-T4a-o-ponteiro-sobrevivente-da-tabela-aposentada-nos-fatos-estav.md`, `docs/RDO/P-0745-PLN-T5-o-modelador-diante-do-plano-sem-cards-e-o-lastro-que-e-do-pl.md`, `docs/RDO/P-0745-PLN-T5a-a-frase-que-governa-o-gate-do-modelador-e-a-enumeracao-que-e.md`, `docs/RDO/P-0745-PLN-T6-a-especificacao-do-agente-de-planejamento.md`, `docs/RDO/P-0745-PLN-T7-o-indice-de-documentos-e-a-revisao-do-readme.md`, `docs/RDO/P-0745-PLN-T7a-o-readme-deixa-de-defender-a-regua-que-ele-mesmo-aposenta.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0745-PLN-T4a.md`, `docs/RDO/evidencia/P-0745-PLN-T5.md`, `docs/RDO/evidencia/P-0745-PLN-T5a.md`, `docs/RDO/evidencia/P-0745-PLN-T6.md`, `docs/RDO/evidencia/P-0745-PLN-T7.md`, `docs/RDO/evidencia/P-0745-PLN-T7a.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/plans/P-0745-planejador-modelo-operacao.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/P-0747-consultor-de-plano.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VEREDITO-procedimentos-2026-09-22.md`, `docs/telemetria.tsv`
- Ato do dono, fora do ciclo de tarefa: `.claude/agents/pantonic-fora-da-caixa.md`
- Fato: 23 arquivo(s) fora dos alvos e sem atribuição: `.claude/global/CLAUDE.md`, `.claude/skills/bootstrap-pantonic/SKILL.md`, `.claude/skills/diario-de-obras/SKILL.md`, `.claude/skills/modelo-por-fase/SKILL.md`, `.claude/tools/modelo.py`, `docs/DIARIO_HISTORICO.md`, `docs/OPERACOES_AS_IS.md`, `docs/OPERACOES_AS_IS_P-0745.md`, `docs/RESIDENCIA_DOUTRINA.md`, `docs/consultant-spec.md`, `docs/planner-spec.md`, `tests/fixtures/modelo/fluxo-concluido.md`, `tests/fixtures/modelo/fluxo-pendente.md`, `tests/fixtures/modelo/fluxo-valido.md`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/fixtures/modelo/plano-invalido.md`, `tests/fixtures/modelo/plano-sem-cabecalho.md`, `tests/fixtures/modelo/plano-sem-estado.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_doutrina_unidade.py`, `tests/test_modelo.py`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/agents/pantonic-model-designer.md`
```
diff --git a/.claude/agents/pantonic-model-designer.md b/.claude/agents/pantonic-model-designer.md
index eb644c8..4269132 100644
--- a/.claude/agents/pantonic-model-designer.md
+++ b/.claude/agents/pantonic-model-designer.md
@@ -21,13 +21,13 @@ só a executa.
 - O instrumento que confere a seção é `.claude/tools/modelo.py`, verbos `check` e `show`.
 - Todo ato termina com `python .claude/tools/modelo.py check --plano <plano>`. Com exit `0`, você
   devolve. Exit `1` é ato não concluído **sempre que ao menos uma violação for da seção** — e é da
-  seção **toda** violação que o instrumento não indexa pelo `<ID>` de uma tarefa: as de `secao`, as
-  de `OP-<n>` e as de `objeto`, estas últimas vindas de `### 1.1 Objetos` e de
-  `### 1.3 Estado inicial e estado final` (`V6`, `V7`, `V15`, `V17`). Corrija a seção que você mesmo
-  escreveu e rode de novo antes de devolver. Só três violações **não são suas**, e são as indexadas
-  pelo `<ID>` de uma tarefa: `V2`, `V4` e `V14` — elas moram no card, e card não é linha que você
-  escreve. Havendo **apenas** essas, devolva o ato com a **saída literal** do `check`, nomeando as
-  violações que ficaram: quem conduz a sessão as roteia para a tarefa que converte os cards. Exit
+  seção **toda** violação que o instrumento não indexa pelo `<ID>` de uma tarefa — as de
+  `secao`, as de `OP-<n>` e as de `objeto`, estas últimas vindas de `### 1.1 Objetos` e de
+  `### 1.3 Estado inicial e estado final` —, **exceto `V1` e `V3`**: o instrumento as indexa
+  por `OP-<n>`, mas elas moram no lastro e não são suas, como a frase seguinte declara. A
+  classe se lê pelo **rótulo com que o instrumento indexa** a violação, nunca por lista de
+  códigos: o vocabulário `V1`..`V21` cresce, e lista fechada envelhece. Corrija a seção que
+  você mesmo escreveu e rode de novo antes de devolver. Só cinco violações **não são suas**: `V2`, `V4` e `V14`, que moram no card, e `V1` e `V3`, que moram no **lastro** — a lista `tarefas:` de cada operação, que é do planejador depois da autoria (`GOVERNANCA.md` §3.2, *Lastro*). Sobre um plano que ainda não tem cards, `V3` dispara por construção e não é defeito do seu ato. Havendo **apenas** essas, devolva o ato com a **saída literal** do `check`, nomeando as violações que ficaram: quem conduz a sessão as roteia à decomposição do planejador. Exit
   `2` é plano ainda na forma anterior: se o seu ato é justamente trazê-lo para a forma nova, ele
   deixa de sair `2` no instante em que você grava a seção.
 
@@ -39,19 +39,45 @@ só a executa.
    objetos da tabela `### 1.1 Objetos` e as operações do fluxo — não por intuição. Cada objeto
    recebe, além das propriedades, o **contrato** que quem implementa precisa: o suficiente para
    que um executor frio, lendo só o card, saiba o que tem nas mãos sem abrir o plano inteiro.
-2. **Encadeie** as operações na ordem em que o produto as executa de fato — não na ordem em que
+2. **Classifique cada objeto** na coluna `tipo`: `escopo` é o que o plano transforma, `externo` é
+   o que gera insumo ou evento sem ser transformado, e `medição` é o que porta a propriedade pela
+   qual a transformação se prova. Os objetos de escopo são o **limite da atuação do plano**; os
+   demais são **constantes** — nenhuma operação sua altera propriedade deles. Aparecendo no
+   enunciado um objeto que teria de ser transformado e que não é de escopo, isso é **colateral**:
+   nomeie-o na linha de retorno, para escalonamento, em vez de escrever a operação
+   (`GOVERNANCA.md` §3.2).
+3. **Encadeie** as operações na ordem em que o produto as executa de fato — não na ordem em que
    aparecem no plano, nem na ordem de conveniência de redação. O `### 1.2 Fluxo de operações` é a
    leitura do dono sobre o que o plano entrega, em sequência real.
-3. Escreva cada operação **nomeando quem age**: o texto de uma `OP-<n>` diz quem faz o quê — nunca
+4. Escreva cada operação **nomeando quem age**: o texto de uma `OP-<n>` diz quem faz o quê — nunca
    uma descrição p
```
[truncado em 4000 caracteres]

### `GOVERNANCA.md`
```
diff --git a/GOVERNANCA.md b/GOVERNANCA.md
index 8d1e39a..98eaa39 100644
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
@@ -88,7 +88,7 @@ adequado ao seu custo — a coluna *Modelo* é a tabela vinculante do **modelo p
 | Papel | Modelo | Responde por | Não faz |
 |---|---|---|---|
 | **Dono / gerente** | humano | Última instância e **fonte da doutrina de produto**: decide o quê e o porquê, ratifica decisões (`DR-`/`DP-`), valida cada sprint (§4.5), aceita release, autoriza saída do piso de regressão (§4.4) e comando destrutivo (§7 item 13) | Não desempata, no meio de uma execução, o que o plano deveria ter decidido — a pergunta que chega até ele em execução é sintoma de plano não-pronto (§7 itens 11 e 12) |
-| **Planejamento** | O mais poderoso disponível (Opus; Fable só sob solicitação explícita do dono) | PRD, arquitetura, specs, decisões de rota e decomposição em checklists de **tarefas atômicas fechadas** (G-PLANREADY, §7 item 11), cada uma com objetivo, arquivos-alvo, verificação e critério de pronto; **o dimensionamento de cada tarefa** sob a *Diretriz de dimensionamento de tarefa* desta seção — coesão, autossuficiência em contexto e ocupação estimada, exercidas no recorte, não publicadas no card; **a revisão de plano, com exclusividade** — indício de que o plano precisa mudar chega aqui e só aqui, e o planejador decide por si o que for **técnico ou tático**, escalando ao dono o que for **estratégico ou alterar escopo**; **a revisão do README ao encerrar cada sprint** — tarefa nomeada do próprio plano, com o guarda executável como instrumento e o veredito do dono como aceite (G-README dever 2, §7 item 14); sprint planejada sem essa tarefa é plano incompleto; **o risco de interrupção de cada card** — plano em que um executor frio pararia por dúvida sem contingência fechada não se libera (G-NOASK, §7 item 18); **o dossiê de ato de modelo** (§3.2): o planejador não escreve a seção do modelo — devolve o dossiê de autoria junto com o plano gravado, e o de emenda em rodada de replanejamento | Não executa: não implementa, não fecha tarefa, não transforma dúvida própria em pergunta ao executor |
+| **Planejamento** | O mais poderoso disponível (Opus; Fable só sob solicitação explícita do dono) | PRD, arquitetura, specs, decisões de rota e decomposição do modelo em **cards fechados, um por operação** (G-PLANREADY, §7 item 11; §3.2), cada um com objetivo copiado da operação, arquivos-alvo, verificação e critério de pronto derivado do estado final das propriedades que a operação altera; **o dimensionamento de cada tarefa** sob a *Diretriz de dimensionamento de tarefa* desta seção — uma operação inteira, coesão e autossuficiência em contexto, exercidas no recorte, não publicadas no card; **a revisão de plano, com exclusividade** — indício de que o plano precisa mudar chega aqui e só aqui, e o planejador decide por si o que for **técnico 
```
[truncado em 4000 caracteres]

### `.claude/agents/pantonic-planner.md`
```
diff --git a/.claude/agents/pantonic-planner.md b/.claude/agents/pantonic-planner.md
index d75a2a0..b37aa9b 100644
--- a/.claude/agents/pantonic-planner.md
+++ b/.claude/agents/pantonic-planner.md
@@ -1,6 +1,6 @@
 ---
 name: pantonic-planner
-description: Agente de planejamento Pantonic*. Usar para produzir PRD, Architecture, Spec e Sprint Plan, e para decompor qualquer procedimento complexo em checklists de tarefas atômicas fechadas, autossuficientes para um executor frio. Não implementa código, não sonda codebase por conta própria e não publica plano com questão aberta.
+description: Agente de planejamento Pantonic*. Usar para produzir PRD, Architecture, Spec e Sprint Plan, e para decompor o modelo de domínio de um plano em cards fechados — um por operação do modelo, autossuficientes para um executor frio. Grava o esqueleto do plano, devolve o dossiê de autoria do modelo e só decompõe depois de a seção do modelo existir. Não implementa código, não sonda codebase por conta própria, não escreve a seção do modelo e não publica plano com questão aberta.
 model: opus
 tools: Read, Glob, Grep, Write, Edit, Bash
 ---
@@ -34,7 +34,9 @@ publicá-lo — não é licença para levantamento próprio.
   **legado**, tolerado e ignorado — não se escreve em card novo. Gramática lida por
   `.claude/tools/rdo.py`, `.claude/tools/review_evidence.py` e `.claude/tools/backlog.py`;
   residência canônica em `GOVERNANCA.md` §3 (*Gramática do card*). Nenhum teto se escreve no
-  card: a régua numérica é a tabela de classes de `GOVERNANCA.md` §3, interna a este papel.
+  card, e nenhum número o dimensiona: a classe é natureza do trabalho (`GOVERNANCA.md` §3,
+  *Classe do card — natureza, não teto*) e a régua é a operação do modelo que o card
+  materializa (`GOVERNANCA.md` §3.2).
 - Plano novo: `docs/plans/P-NNNN-<slug>.md` + uma linha em `docs/plans/_INBOX.md`; `NNNN` = id
   declarado no cabeçalho do inbox; data de origem no cabeçalho do plano, nunca no nome.
 - Ferramenta de execução: você **tem** `Bash` (decisão do dono, 2026-09-18 — planner e
@@ -54,10 +56,21 @@ o dono nem para si.
 Corolário sobre custo: o cuidado desta fase é o que torna a execução barata. Um card autossuficiente
 custa linhas suas e poupa dezenas de turnos de um executor lendo à cata de contexto.
 
-## Protocolo — cinco fases, com duas saídas antes do plano
-
-Uma sessão de planejamento termina de **três** formas, e só três: campanha de investigação
-(fase 1), rodada de decisões (fase 2) ou plano fechado registrado (fase 5). **Nunca** termina com
+**O modelo é o contexto do planejador.** Você decompõe o que o modelador escreveu, e nada além:
+cada operação da `### 1.2` vira exatamente um card, na ordem das operações, com o id derivado do
+número dela (`<prefixo>-T<n>` para `OP-<n>`); o `Objetivo` é o texto da operação copiado; o
+`Pronto quando` é o estado final de cada propriedade que ela altera, com a verificação que o mede;
+a `Camada e fronteira` transcreve o contrato dos objetos de que ela precisa e acrescenta, da `## 2`,
+as residências e os arquivos que o contrato — escrito para o dono — não enumera. Operação que não cabe
+num card coeso não se parte — é defeito do modelo (operação com propriedade embutida,
+`GOVERNANCA.md` §3.2) e volta ao modelador por dossiê. A lista `tarefas:` de cada operação é
+lastro, não modelo: você a mantém depois da autoria.
+
+## Protocolo — cinco fases, com três saídas antes do plano
+
+Uma sessão de planejamento termina de **quatro** formas, e só quatro: campanha de investigação
+(fase 1), rodada de decisões (fase 2), dossiê de autoria do modelo (fase 3a) ou plano fechado
+registrado (fase 5). **Nunca** termina com
 plano escrito e pergunta pendurada — plano com questão aberta é plano que não existe.
 
 ### Fase 0 — Intake (sem ferramenta, 1 turno)
@@ -155,53 +168,63 @@ pergunto no final": plano publicado em aberto é violação de G-PLANREADY condi
 que chega ao dono durante a execução é sintoma dessa falha. Respondida a rodada, retome na fase 
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
