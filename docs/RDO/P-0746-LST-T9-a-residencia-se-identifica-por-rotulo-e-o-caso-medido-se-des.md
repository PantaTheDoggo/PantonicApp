# RDO — P-0746 · LST-T9

**Plano:** `docs/plans/P-0746-lastro-do-modelo.md`
**Tarefa:** `LST-T9` — A residência se identifica por rótulo, e o caso medido se desfaz em dois
**Modelo:** Opus · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** três frases já publicadas pela doutrina deste plano passam a bater com o corpus vivo: a coluna de lastro de `### 1.1` é reconhecida pelo cabeçalho que **começa com** `lastro`, a residência do requisito secundário é **seção nomeada**, em qualquer posição do plano, e o caso medido da promoção indevida em `GOVERNANCA.md` §3.2 deixa de comprimir duas recusas sobre modelos distintos numa recusa só.

**Arquivos-alvo:** - `.claude/skills/diario-de-obras/SKILL.md` — linha `objetos` da tabela de gramática e os parágrafos **Lastro, por elemento** e **Requisito secundário, a residência do elemento sem lastro** - `GOVERNANCA.md` §3.2 — a frase do caso medido no parágrafo da decomposição

**Verificação:** 1. ``` grep -cF 'cujo cabeçalho começa com' .claude/skills/diario-de-obras/SKILL.md ``` → **≥ 1**. **Medido antes: 0** (2026-09-22). 2. ``` grep -cF 'afere a presença da coluna `lastro` na tabela de' .claude/skills/diario-de-obras/SKILL.md ``` → **0** — a exigência de igualdade literal desaparece. **Medido antes: 1**. Par com a Verificação 1. 3. ``` grep -cF 'seção de nível 2 nomeada' .claude/skills/diario-de-obras/SKILL.md ``` → **≥ 1**. **Medido antes: 0** (2026-09-22). 4. ``` grep -cF 'seção `## 2. Requisitos secundários` do plano' .claude/skills/diario-de-obras/SKILL.md ``` → **0** — a prescrição por número desaparece. **Medido antes: 1**. Par com a Verificação 3. 5. ``` grep -cF 'dois modelos distintos' GOVERNANCA.md ``` → **≥ 1**. **Medido antes: 0** (2026-09-22). 6. ``` grep -cF 'o dono recusou duas vezes a versão 1 de um modelo' GOVERNANCA.md ``` → **0** — a frase comprimida desaparece. **Medido antes: 1**. Par com a Verificação 5. 7. **Não-regressão dos literais já aceitos** (as três tarefas de redação anteriores não se desfazem): `grep -cF` devolve **≥ 1** para cada um — `o que o plano constrói é objeto` (`GOVERNANCA.md`), `promoção indevida` (`GOVERNANCA.md`), `quatro propriedades` (`GOVERNANCA.md`), `descrição de estado não vira objeto próprio` (skill), `Requisitos secundários` (skill), `não entra no modelo e não é aferido por lastro` (skill), `plano em status terminal não se migra` (skill), `` \| contrato \| origem \| lastro \|` `` (skill) — e **0** para `` \| contrato \| origem \|` `` (skill). Todos medidos nos valores acima em 2026-09-22. 8. ``` python .claude/tools/modelo.py check --plano docs/plans/P-0746-lastro-do-modelo.md ``` → exit **0**. 9. ``` python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md ``` → exit **0** (`I-2`). 10. ``` python -m pytest tests -q ``` → **≥ 262 passed** (`I-3`).

**Pronto quando:** as dez verificações saem nos valores declarados, com os três pares presença-ausência discriminando e a não-regressão intacta, e nenhum arquivo fora dos `Arquivos-alvo` foi editado. Por propriedade que a operação altera: - `restrições do modelo conceitual.leitura de lastro` — a residência da âncora passa a ser reconhecível no corpus vivo: a coluna se identifica pelo rótulo, e o autor qualifica a âncora sem sair da forma — Verificação 1 e 2. - `restrições do modelo conceitual.leitura de prompt` — o caso medido da leitura pela via errada deixa de comprimir duas recusas sobre modelos distintos numa só — Verificação 5 e 6. - `restrições do modelo conceitual.decomposição de requisitos funcionais e não funcionais` — a residência do elemento sem lastro é seção nomeada, como a própria operação diz, e não um número de seção já ocupado no acervo — Verificação 3 e 4.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-22
- **Depende de:** `LST-T8`
- **Fundamento:** `DLS-15`; achados `AE-7`, `AE-9`, `AE-10`, `AE-11`; fatos `F-1`, `F-11`, `F-16`; invariantes `I-2`, `I-3`. Card autorado no segundo reparo de escalonamento, em 2026-09-22: as três frases nasceram corretas em intenção e erradas em confronto com o acervo — nenhuma entrega anterior é rebaixada por isto.
- **Operação do modelo:** `OP-1`, `OP-2`, `OP-4` - OP-1: O redator da norma constrói a restrição de leitura de lastro: todo objeto, operação e propriedade do modelo tem âncora declarada num trecho do enunciado do problema ou do prompt que originou o plano, e elemento sem essa âncora não entra no modelo. - precisa de: — a `OP-1` constrói o objeto; não há objeto anterior a consumir - OP-2: O redator da norma constrói a restrição de leitura de prompt: o enunciado alimenta o modelo por duas vias declaradas — a via de estado, que popula o estado inicial e o estado final, e a via de operação, que é o que o plano faz diante do vão entre os dois. - precisa de: restrições do modelo conceitual — norma em `GOVERNANCA.md` §3.2; forma publicada na subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras`; aferição em `.claude/tools/modelo.py` (`check`), com `tests/test_modelo.py` e fixtures; autoria em `.claude/agents/pantonic-model-designer.md` - OP-4: O redator da gramática constrói a restrição de decomposição de requisitos funcionais e não funcionais: o elemento com lastro é funcional e entra no modelo como contrato; o elemento sem lastro é não fundamental, reside em seção nomeada do plano fora do modelo, fica transparente para o dono e tem responsabilidade inteira do agente. - precisa de: restrições do modelo conceitual — norma em `GOVERNANCA.md` §3.2; forma publicada na subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras`; aferição em `.claude/tools/modelo.py` (`check`), com `tests/test_modelo.py` e fixtures; autoria em `.claude/agents/pantonic-model-designer.md` - **Nota de leitura:** o texto da `OP-4` já dizia **seção nomeada**; o que divergiu foi a gramática, que a publicou por número. Esta tarefa alinha a forma ao texto da operação — não o contrário.
- **Camada e fronteira:** doutrina e gramática publicada, dois arquivos, **três frases**. Nenhum instrumento, nenhum agente, nenhum teste novo, nenhuma seção nova: é correção cirúrgica de texto já publicado. **Nenhum ato sobre a `## 1` ou a `## 1A`** — a decisão do `DLS-15` é justamente que quem se ajusta é a gramática, não o modelo.
- **Domínio:** *rótulo* — o nome pelo qual a forma reconhece uma residência (cabeçalho de coluna, nome de seção), por oposição à *posição* (número da coluna, número da seção). *Casar por prefixo* — o cabeçalho conforme começa com o rótulo e pode qualificá-lo: `lastro`, `lastro na §0`, `lastro no prompt`.
- **Forma prescrita (literal, não parafrasear):** - a linha `objetos` e o parágrafo de lastro passam a dizer que a coluna se reconhece pelo cabeçalho **`cujo cabeçalho começa com`** `lastro`, admitindo qualificação da âncora; a forma canônica da tabela (`\| … \| origem \| lastro \|`) **não muda** - o parágrafo do requisito secundário passa a dizer `seção de nível 2 nomeada` `Requisitos secundários`, fora da `## 1`, **em qualquer posição do plano** — o número `## 2` sai da prescrição, porque `P-0743` e `P-0745` já o usam para *Fatos estabelecidos* e a retroatividade publicada proíbe migrá-los - a frase do caso medido em `GOVERNANCA.md` §3.2 passa a registrar que as duas recusas de 2026-09-21 foram sobre **`dois modelos distintos`** — uma sobre o modelo de um plano, outra sobre a versão 1 do próprio plano que instituía a regra, esta por quatro propriedades escritas como objetos — sem citar identificador de plano, no estilo do parágrafo
- **Nota de aceite (`F-16`):** `grep -cF`, nunca `grep -ciF` — o segundo **aborta** com exit `134` neste ambiente. As Verificações 2, 4 e 6 esperam `0`: o `grep` sai `1` quando não acha, e é isso que se quer.
- **Fora do escopo desta tarefa:** tocar a `## 1` ou a `## 1A` deste plano (`I-1`, `DLS-15` — não há dossiê nesta rodada); renumerar seção de plano algum; o instrumento (`LST-T5`, a tarefa seguinte, que implementa a leitura por prefixo); a `## 2` **deste** plano, cuja citação de operação o consultor já corrigiu no próprio ato de reparo (`AE-8`).

## Execução

**Consumo:** 15 tool uses, 54.5 k tokens, 105.9 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: Antes do Marco 2 adjudicar a versao 4: as linhas tarefas: do fluxo de operacoes nao contabilizam esta janela - OP-1 e OP-2 ganharam a LST-T8 pelo dossie de emenda de 2026-09-21 (DLS-13) e nenhuma delas, nem a OP-3 nem a OP-4, lista a LST-T9, que materializou as quatro. So o modelador escreve na secao 1 (I-1), entao isto morre em silencio se nao entrar no dossie do Marco 2.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

Exercicio ponta a ponta do modulo: a regra de prefixo fecha de fato o AE-10 - o cabecalho vivo e 'lastro na secao 0' na 1.1 da secao 1 (versao 3, vigente) e da 1A (versao 4, pendente) do P-0746, e o literal publicado admite-o sem tocar o modelo, que era a condicao do DLS-15. As duas ocorrencias do literal dizem a mesma coisa, sem divergencia interna. O vao que sobra e anterior a esta tarefa e ja tem rota: a gramatica afirma no presente que o check afere a presenca da coluna cujo cabecalho comeca com lastro, e .claude/tools/modelo.py nao contem nenhuma ocorrencia de lastro - zero, nem no instrumento nem em tests/test_modelo.py. A LST-T5 e quem o fecha. Acerto de autoria que vale repetir, pelo segundo laudo seguido: Forma prescrita verbatim com a instrucao de nao parafrasear, e tres pares presenca-ausencia medidos sobre o mesmo arquivo.

## Fechamento

**Desdobramento:** aprovado
