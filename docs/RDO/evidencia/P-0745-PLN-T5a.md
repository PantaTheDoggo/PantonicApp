# Evidência de revisão — P-0745 PLN-T5a

## Diff (`git diff --stat`)
```
.claude/README.md                               |    2 +-
 .claude/agents/pantonic-fora-da-caixa.md        |    2 +-
 .claude/agents/pantonic-model-designer.md       |   38 +-
 .claude/agents/pantonic-planner.md              |  132 ++-
 .claude/global/CLAUDE.md                        |   21 +-
 .claude/skills/bootstrap-pantonic/SKILL.md      |    2 +-
 .claude/skills/diario-de-obras/SKILL.md         |   56 +-
 .claude/skills/modelo-por-fase/SKILL.md         |    2 +-
 .claude/tools/modelo.py                         |   31 +-
 GOVERNANCA.md                                   |  186 ++--
 README.md                                       |    3 +-
 docs/CUSTO_DO_PICKUP.md                         |  113 ++
 docs/DIARIO_DE_OBRAS.md                         |  693 ++++++++++---
 docs/DIARIO_HISTORICO.md                        |  154 +++
 docs/DOC_MAP.md                                 |   53 +-
 docs/RDO/INDEX.md                               |   14 +
 docs/RESIDENCIA_DOUTRINA.md                     |    4 +-
 docs/consultant-spec.md                         |   41 +-
 docs/plans/P-0745-planejador-modelo-operacao.md | 1244 ++++++++++++++++++++---
 docs/plans/_INBOX.md                            |    3 +-
 docs/plans/_INBOX_HISTORICO.md                  |    2 +
 docs/telemetria.tsv                             |   64 ++
 tests/fixtures/modelo/fluxo-concluido.md        |   12 +-
 tests/fixtures/modelo/fluxo-pendente.md         |   20 +-
 tests/fixtures/modelo/fluxo-valido.md           |   12 +-
 tests/fixtures/modelo/plano-invalido-2.md       |   10 +-
 tests/fixtures/modelo/plano-invalido.md         |   12 +-
 tests/fixtures/modelo/plano-sem-cabecalho.md    |    8 +-
 tests/fixtures/modelo/plano-sem-estado.md       |    8 +-
 tests/test_modelo.py                            |  127 ++-
 30 files changed, 2549 insertions(+), 520 deletions(-)
```

## Arquivos tocados
- `.claude/README.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-fora-da-caixa.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-model-designer.md` — atribuição: da entrega; estado git: ` M`
- `.claude/agents/pantonic-planner.md` — atribuição: alheio; estado git: ` M`
- `.claude/global/CLAUDE.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/bootstrap-pantonic/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/diario-de-obras/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/modelo-por-fase/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/tools/modelo.py` — atribuição: alheio; estado git: ` M`
- `GOVERNANCA.md` — atribuição: alheio; estado git: ` M`
- `README.md` — atribuição: alheio; estado git: ` M`
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
- Arquivos-alvo declarados: `.claude/agents/pantonic-model-designer.md`, `tests/test_doutrina_unidade.py`
- Literais não reconhecidos como caminho (4): `## Fatos estáveis`, `exit 1`, `seção`, `antes de devolver.`
- Arquivos tocados: `.claude/README.md`, `.claude/agents/pantonic-fora-da-caixa.md`, `.claude/agents/pantonic-model-designer.md`, `.claude/agents/pantonic-planner.md`, `.claude/global/CLAUDE.md`, `.claude/skills/bootstrap-pantonic/SKILL.md`, `.claude/skills/diario-de-obras/SKILL.md`, `.claude/skills/modelo-por-fase/SKILL.md`, `.claude/tools/modelo.py`, `GOVERNANCA.md`, `README.md`, `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/DIARIO_HISTORICO.md`, `docs/DOC_MAP.md`, `docs/OPERACOES_AS_IS.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0745-PLN-T4a-o-ponteiro-sobrevivente-da-tabela-aposentada-nos-fatos-estav.md`, `docs/RDO/P-0745-PLN-T5-o-modelador-diante-do-plano-sem-cards-e-o-lastro-que-e-do-pl.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0745-PLN-T4a.md`, `docs/RDO/evidencia/P-0745-PLN-T5.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/RESIDENCIA_DOUTRINA.md`, `docs/consultant-spec.md`, `docs/plans/P-0745-planejador-modelo-operacao.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/telemetria.tsv`, `tests/fixtures/modelo/fluxo-concluido.md`, `tests/fixtures/modelo/fluxo-pendente.md`, `tests/fixtures/modelo/fluxo-valido.md`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/fixtures/modelo/plano-invalido.md`, `tests/fixtures/modelo/plano-sem-cabecalho.md`, `tests/fixtures/modelo/plano-sem-estado.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_doutrina_unidade.py`, `tests/test_modelo.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/README.md` → `PLN-T4`, `.claude/agents/pantonic-fora-da-caixa.md` → `PLN-T3`, `.claude/agents/pantonic-planner.md` → `PLN-T4`, `.claude/global/CLAUDE.md` → `PLN-T2`, `.claude/skills/bootstrap-pantonic/SKILL.md` → `PLN-T3`, `.claude/skills/diario-de-obras/SKILL.md` → `PLN-T3`, `.claude/skills/modelo-por-fase/SKILL.md` → `PLN-T3`, `GOVERNANCA.md` → `PLN-T2`, `README.md` → `PLN-T7`, `docs/DOC_MAP.md` → `PLN-T7`, `docs/RESIDENCIA_DOUTRINA.md` → `PLN-T2`, `docs/consultant-spec.md` → `PLN-T7`, `docs/plans/P-0745-planejador-modelo-operacao.md` → `PLN-T1`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0745-PLN-T4a-o-ponteiro-sobrevivente-da-tabela-aposentada-nos-fatos-estav.md`, `docs/RDO/P-0745-PLN-T5-o-modelador-diante-do-plano-sem-cards-e-o-lastro-que-e-do-pl.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0745-PLN-T4a.md`, `docs/RDO/evidencia/P-0745-PLN-T5.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/telemetria.tsv`
- Fato: 15 arquivo(s) fora dos alvos e sem atribuição: `.claude/tools/modelo.py`, `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_HISTORICO.md`, `docs/OPERACOES_AS_IS.md`, `tests/fixtures/modelo/fluxo-concluido.md`, `tests/fixtures/modelo/fluxo-pendente.md`, `tests/fixtures/modelo/fluxo-valido.md`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/fixtures/modelo/plano-invalido.md`, `tests/fixtures/modelo/plano-sem-cabecalho.md`, `tests/fixtures/modelo/plano-sem-estado.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_modelo.py`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/agents/pantonic-model-designer.md`
```
diff --git a/.claude/agents/pantonic-model-designer.md b/.claude/agents/pantonic-model-designer.md
index eb644c8..28ea9e5 100644
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
 
@@ -39,19 +39,29 @@ só a executa.
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
