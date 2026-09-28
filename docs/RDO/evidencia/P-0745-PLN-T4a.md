# Evidência de revisão — P-0745 PLN-T4a

## Diff (`git diff --stat`)
```
.claude/README.md                               |   2 +-
 .claude/agents/pantonic-fora-da-caixa.md        |   2 +-
 .claude/agents/pantonic-model-designer.md       |  15 +-
 .claude/agents/pantonic-planner.md              | 132 ++--
 .claude/global/CLAUDE.md                        |  21 +-
 .claude/skills/bootstrap-pantonic/SKILL.md      |   2 +-
 .claude/skills/diario-de-obras/SKILL.md         |  56 +-
 .claude/skills/modelo-por-fase/SKILL.md         |   2 +-
 .claude/tools/modelo.py                         |  31 +-
 GOVERNANCA.md                                   | 168 +++--
 README.md                                       |   3 +-
 docs/CUSTO_DO_PICKUP.md                         | 113 +++
 docs/DIARIO_DE_OBRAS.md                         | 668 ++++++++++++-----
 docs/DIARIO_HISTORICO.md                        | 154 ++++
 docs/DOC_MAP.md                                 |  53 +-
 docs/RDO/INDEX.md                               |  12 +
 docs/RESIDENCIA_DOUTRINA.md                     |   4 +-
 docs/consultant-spec.md                         |  41 +-
 docs/plans/P-0745-planejador-modelo-operacao.md | 916 ++++++++++++++++++++----
 docs/plans/_INBOX.md                            |   3 +-
 docs/plans/_INBOX_HISTORICO.md                  |   2 +
 docs/telemetria.tsv                             |  52 ++
 tests/fixtures/modelo/fluxo-concluido.md        |  12 +-
 tests/fixtures/modelo/fluxo-pendente.md         |  20 +-
 tests/fixtures/modelo/fluxo-valido.md           |  12 +-
 tests/fixtures/modelo/plano-invalido-2.md       |  10 +-
 tests/fixtures/modelo/plano-invalido.md         |  12 +-
 tests/fixtures/modelo/plano-sem-cabecalho.md    |   8 +-
 tests/fixtures/modelo/plano-sem-estado.md       |   8 +-
 tests/test_modelo.py                            | 127 +++-
 30 files changed, 2174 insertions(+), 487 deletions(-)
```

## Arquivos tocados
- `.claude/README.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-fora-da-caixa.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-model-designer.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-planner.md` — atribuição: da entrega; estado git: ` M`
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
- Arquivos-alvo declarados: `.claude/agents/pantonic-planner.md`, `tests/test_doutrina_unidade.py`
- Literais não reconhecidos como caminho (1): `## Fatos estáveis`
- Arquivos tocados: `.claude/README.md`, `.claude/agents/pantonic-fora-da-caixa.md`, `.claude/agents/pantonic-model-designer.md`, `.claude/agents/pantonic-planner.md`, `.claude/global/CLAUDE.md`, `.claude/skills/bootstrap-pantonic/SKILL.md`, `.claude/skills/diario-de-obras/SKILL.md`, `.claude/skills/modelo-por-fase/SKILL.md`, `.claude/tools/modelo.py`, `GOVERNANCA.md`, `README.md`, `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/DIARIO_HISTORICO.md`, `docs/DOC_MAP.md`, `docs/OPERACOES_AS_IS.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/RESIDENCIA_DOUTRINA.md`, `docs/consultant-spec.md`, `docs/plans/P-0745-planejador-modelo-operacao.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/telemetria.tsv`, `tests/fixtures/modelo/fluxo-concluido.md`, `tests/fixtures/modelo/fluxo-pendente.md`, `tests/fixtures/modelo/fluxo-valido.md`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/fixtures/modelo/plano-invalido.md`, `tests/fixtures/modelo/plano-sem-cabecalho.md`, `tests/fixtures/modelo/plano-sem-estado.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_doutrina_unidade.py`, `tests/test_modelo.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/README.md` → `PLN-T4`, `.claude/agents/pantonic-fora-da-caixa.md` → `PLN-T3`, `.claude/agents/pantonic-model-designer.md` → `PLN-T5`, `.claude/global/CLAUDE.md` → `PLN-T2`, `.claude/skills/bootstrap-pantonic/SKILL.md` → `PLN-T3`, `.claude/skills/diario-de-obras/SKILL.md` → `PLN-T3`, `.claude/skills/modelo-por-fase/SKILL.md` → `PLN-T3`, `GOVERNANCA.md` → `PLN-T2`, `README.md` → `PLN-T7`, `docs/DOC_MAP.md` → `PLN-T7`, `docs/RESIDENCIA_DOUTRINA.md` → `PLN-T2`, `docs/consultant-spec.md` → `PLN-T7`, `docs/plans/P-0745-planejador-modelo-operacao.md` → `PLN-T1`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-54b-a-fonte-da-bimodalidade.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0745-PLN-T1-o-agregado-medido-da-atuacao-do-planejador.md`, `docs/RDO/P-0745-PLN-T2-a-norma-da-unidade-de-trabalho-e-dos-limites.md`, `docs/RDO/P-0745-PLN-T3-a-gramatica-do-card-a-tarefa-e-a-materializacao-de-uma-opera.md`, `docs/RDO/P-0745-PLN-T4-o-protocolo-do-planejador-modelo-primeiro-um-card-por-operac.md`, `docs/RDO/P-0746-LST-T1-o-criterio-de-admissao-do-modelo-e-as-duas-vias-do-enunciado.md`, `docs/RDO/P-0746-LST-T3-a-residencia-do-requisito-secundario.md`, `docs/RDO/P-0746-LST-T5-o-instrumento-afere-lastro-declarado.md`, `docs/RDO/P-0746-LST-T6-a-reaplicacao-ao-p-0745.md`, `docs/RDO/P-0746-LST-T7-a-restricao-de-decomposicao-o-que-e-objeto-e-o-que-e-proprie.md`, `docs/RDO/P-0746-LST-T8-a-residencia-da-declaracao-de-lastro-na-gramatica.md`, `docs/RDO/P-0746-LST-T9-a-residencia-se-identifica-por-rotulo-e-o-caso-medido-se-des.md`, `docs/RDO/evidencia/P-0745-PLN-T1.md`, `docs/RDO/evidencia/P-0745-PLN-T2.md`, `docs/RDO/evidencia/P-0745-PLN-T3.md`, `docs/RDO/evidencia/P-0745-PLN-T4.md`, `docs/RDO/evidencia/P-0746-LST-T1.md`, `docs/RDO/evidencia/P-0746-LST-T3.md`, `docs/RDO/evidencia/P-0746-LST-T5.md`, `docs/RDO/evidencia/P-0746-LST-T6.md`, `docs/RDO/evidencia/P-0746-LST-T7.md`, `docs/RDO/evidencia/P-0746-LST-T8.md`, `docs/RDO/evidencia/P-0746-LST-T9.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/plans/P-0746-lastro-do-modelo.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/telemetria.tsv`
- Fato: 15 arquivo(s) fora dos alvos e sem atribuição: `.claude/tools/modelo.py`, `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_HISTORICO.md`, `docs/OPERACOES_AS_IS.md`, `tests/fixtures/modelo/fluxo-concluido.md`, `tests/fixtures/modelo/fluxo-pendente.md`, `tests/fixtures/modelo/fluxo-valido.md`, `tests/fixtures/modelo/plano-com-lastro.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/fixtures/modelo/plano-invalido.md`, `tests/fixtures/modelo/plano-sem-cabecalho.md`, `tests/fixtures/modelo/plano-sem-estado.md`, `tests/fixtures/modelo/plano-sem-lastro.md`, `tests/fixtures/modelo/plano-terminal-sem-lastro.md`, `tests/test_modelo.py`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/agents/pantonic-planner.md`
```
diff --git a/.claude/agents/pantonic-planner.md b/.claude/agents/pantonic-planner.md
index d75a2a0..1d8913c 100644
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
@@ -54,10 +56,20 @@ o dono nem para si.
 Corolário sobre custo: o cuidado desta fase é o que torna a execução barata. Um card autossuficiente
 custa linhas suas e poupa dezenas de turnos de um executor lendo à cata de contexto.
 
-## Protocolo — cinco fases, com duas saídas antes do plano
+**O modelo é o contexto do planejador.** Você decompõe o que o modelador escreveu, e nada além:
+cada operação da `### 1.2` vira exatamente um card, na ordem das operações, com o id derivado do
+número dela (`<prefixo>-T<n>` para `OP-<n>`); o `Objetivo` é o texto da operação copiado; o
+`Pronto quando` é o estado final de cada propriedade que ela altera, com a verificação que o mede;
+a `Camada e fronteira` transcreve o contrato dos objetos de que ela precisa. Operação que não cabe
+num card coeso não se parte — é defeito do modelo (operação com propriedade embutida,
+`GOVERNANCA.md` §3.2) e volta ao modelador por dossiê. A lista `tarefas:` de cada operação é
+lastro, não modelo: você a mantém depois da autoria.
 
-Uma sessão de planejamento termina de **três** formas, e só três: campanha de investigação
-(fase 1), rodada de decisões (fase 2) ou plano fechado registrado (fase 5). **Nunca** termina com
+## Protocolo — cinco fases, com três saídas antes do plano
+
+Uma sessão de planejamento termina de **quatro** formas, e só quatro: campanha de investigação
+(fase 1), rodada de decisões (fase 2), dossiê de autoria do modelo (fase 3a) ou plano fechado
+registrado (fase 5). **Nunca** termina com
 plano escrito e pergunta pendurada — plano com questão aberta é plano que não existe.
 
 ### Fase 0 — Intake (sem ferramenta, 1 turno)
@@ -155,53 +167,63 @@ pergunto no final": plano publicado em aberto é violação de G-PLANREADY condi
 que chega ao dono durante a execução é sintoma dessa falha. Respondida a rodada, retome na fase 3
 — no mesmo contexto se a resposta cabe no cenário; em contexto novo se ela o trocou.
 
-### Fase 3 — Auto
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
