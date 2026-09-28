# RDO — P-0746 · LST-T8

**Plano:** `docs/plans/P-0746-lastro-do-modelo.md`
**Tarefa:** `LST-T8` — A residência da declaração de lastro na gramática
**Modelo:** Opus · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** a gramática legível por máquina da subseção *Modelo de domínio (seção do plano)* passa a dizer **onde** o lastro se declara — sexta coluna na tabela de `### 1.1`, quarto campo na linha de máquina de `### 1.2`, quarta coluna na tabela de `### 1.3` —, a separar o que o instrumento afere do que o Marco guarda, e a declarar a retroatividade: plano em status terminal não se migra.

**Arquivos-alvo:** - `.claude/skills/diario-de-obras/SKILL.md` — subseção *Modelo de domínio (seção do plano)*: linhas `objetos`, `operações` e `estado` da tabela de gramática, mais o parágrafo **Lastro, por elemento** que a `LST-T1` acrescentou

**Verificação:** 1. ``` grep -cF '\| contrato \| origem \| lastro \|`' .claude/skills/diario-de-obras/SKILL.md ``` → **≥ 1**. **Medido antes: 0** (2026-09-21). 2. ``` grep -cF '\| contrato \| origem \|`' .claude/skills/diario-de-obras/SKILL.md ``` → **0** — a forma de cinco colunas **desaparece**. **Medido antes: 1**. Com a Verificação 1, é par presença-ausência: as duas leituras dão resultados diferentes sobre o mesmo arquivo. 3. ``` grep -cF '\| propriedade \| estado inicial \| estado final \| lastro \|`' .claude/skills/diario-de-obras/SKILL.md ``` → **≥ 1**. **Medido antes: 0** (2026-09-21). 4. ``` grep -cF '\| propriedade \| estado inicial \| estado final \|`' .claude/skills/diario-de-obras/SKILL.md ``` → **0** — a forma de três colunas desaparece. **Medido antes: 1**. Par com a Verificação 3. 5. ``` grep -cF '`lastro:' .claude/skills/diario-de-obras/SKILL.md ``` → **≥ 1** — o quarto campo da linha de máquina de `### 1.2` está publicado. **Medido antes: 0**. 6. ``` grep -cF 'plano em status terminal não se migra' .claude/skills/diario-de-obras/SKILL.md ``` → **≥ 1**. **Medido antes: 0** (2026-09-21). 7. ``` python .claude/tools/modelo.py check --plano docs/plans/P-0746-lastro-do-modelo.md ``` → exit **0** — publicar a forma não derruba o modelo deste plano, cuja `### 1.1` já usa a sexta coluna. **Medido antes: exit 0**, `modelo: OK — 6 operações, 1 objetos, 6 propriedades, 5 tarefas, versão 3` (2026-09-21; a contagem de tarefas sobe para 6 com este card). 8. ``` python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md ``` → exit **0** (`I-2`). 9. ``` python -m pytest tests -q ``` → **≥ 262 passed** (`I-3`).

**Pronto quando:** as nove verificações saem nos valores declarados, com os dois pares presença-ausência discriminando, e nenhum arquivo fora do alvo foi editado. Por propriedade que a operação altera: - `restrições do modelo conceitual.leitura de lastro` — a âncora deixa de ser exigência sem lugar: a forma publicada diz em que célula cada elemento declara a sua — Verificação 1, 2, 5 e 6. - `restrições do modelo conceitual.leitura de prompt` — as duas vias ganham residência na forma: a via de estado declara lastro na tabela de `### 1.3`, a via de operação no quarto campo de `### 1.2` — Verificação 3, 4 e 5.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-22
- **Depende de:** `LST-T3`
- **Fundamento:** `AE-1`, `DLS-12`, `DLS-14`; fatos `F-14`, `F-15`, `F-16`, `F-17`; invariantes `I-2`, `I-3`. Card autorado no reparo de escalonamento de 2026-09-21: a `LST-T1` instituiu a exigência de lastro sem publicar residência, e a `LST-T5` não tem campo cuja presença aferir enquanto a residência não existir.
- **Operação do modelo:** `OP-1`, `OP-2` - OP-1: O redator da norma constrói a restrição de leitura de lastro: todo objeto, operação e propriedade do modelo tem âncora declarada num trecho do enunciado do problema ou do prompt que originou o plano, e elemento sem essa âncora não entra no modelo. - precisa de: — a `OP-1` constrói o objeto; não há objeto anterior a consumir - OP-2: O redator da norma constrói a restrição de leitura de prompt: o enunciado alimenta o modelo por duas vias declaradas — a via de estado, que popula o estado inicial e o estado final, e a via de operação, que é o que o plano faz diante do vão entre os dois. - precisa de: restrições do modelo conceitual — norma em `GOVERNANCA.md` §3.2; forma publicada na subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras`; aferição em `.claude/tools/modelo.py` (`check`), com `tests/test_modelo.py` e fixtures; autoria em `.claude/agents/pantonic-model-designer.md` - **Afastamento declarado:** a linha `tarefas:` da `OP-1` e da `OP-2` no modelo **vigente** ainda lista só a `LST-T1`. A inclusão da `LST-T8` está no dossiê `Ato de modelo` de emenda devolvido em 2026-09-21 (`DLS-13`) e vigora com o aceite do Marco 2 — nenhuma tarefa escreve na `## 1` (`I-1`).
- **Camada e fronteira:** gramática publicada, **um arquivo**. Nenhuma edição de `GOVERNANCA.md` — a norma já diz que todo elemento tem lastro declarado (`LST-T1`) e que a gramática lida pelo instrumento mora na skill; esta tarefa publica a **forma**, não a regra. Nenhum instrumento e nenhum teste novo: ensinar o parser é da `LST-T5`, que vem em seguida e já encontra a forma publicada — a ordem é deliberada (`F-17`).
- **Domínio:** *residência da declaração* — a célula exata, na forma do plano, em que o autor do modelo escreve a âncora de um elemento. *Aferível* — o que o `check` mede é **presença de declaração não vazia**; a pertinência do trecho citado é juízo do Marco (`F-12`).
- **Forma prescrita (literal, não parafrasear):** - linha `objetos`: a tabela passa a `\| objeto \| o que é \| propriedades \| contrato \| origem \| lastro \|`, e `<lastro>` é o trecho do enunciado (`## 0`) ou do prompt de origem, citado ou apontado, não vazio - linha `operações`: a linha de máquina da operação admite um quarto campo, ` · ` + `` `lastro: <trecho>` ``, depois de `tarefas:` — **opcional na forma, obrigatório na doutrina** enquanto o acervo vivo não o declara (`F-14`) - linha `estado`: a tabela passa a `\| propriedade \| estado inicial \| estado final \| lastro \|` - o parágrafo de lastro ganha, verbatim, a frase `plano em status terminal não se migra`, e diz qual metade é de máquina: o `check` afere presença da coluna de `### 1.1`; o restante é guarda do Marco
- **Nota de aceite (`F-16`):** `grep -cF`, nunca `grep -ciF` — neste ambiente o segundo **aborta** com exit `134`. As Verificações 2 e 4 esperam `0` e **não** são erro de comando: o `grep` sai `1` quando não acha, e é isso que se quer.
- **Fora do escopo desta tarefa:** ensinar o parser a ler os campos novos e acusar ausência deles (`LST-T5`); reescrever `### 1.1`, `### 1.2` ou `### 1.3` **deste** plano (`I-1` — é ato do modelador sob dossiê); migrar plano algum à forma nova (`GOVERNANCA.md` §3.2, *Retroatividade*); a seção de requisitos secundários (`LST-T3`, já fechada).

## Execução

**Consumo:** 10 tool uses, 55.2 k tokens, 121.4 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: Antes de despachar a LST-T5: decidir como a coluna de lastro da 1.1 se identifica (literal 'lastro' da gramatica publicada contra o cabecalho 'lastro na secao 0' do unico plano vivo que a usa) e re-declarar a rota orfa do AE-9, que apontava para a LST-T8 e nao foi fechada por ela.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

Exercicio ponta a ponta do modulo: a gramatica agora publica o quarto campo lastro: como opcional na forma e obrigatorio na doutrina, enquanto _OPERACAO_LINHA_RE (.claude/tools/modelo.py:109) segue ancorada em fim de linha logo depois de tarefas: - acrescentar o campo faz a linha de maquina inteira deixar de casar, nao so o campo novo. O 1A deste plano ja se protege disso por decisao declarada (F-17, AE-6) e a ordem LST-T8 -> LST-T5 e deliberada; o ponto e que quem le apenas a skill nao recebe esse aviso. Acerto de autoria que vale repetir: o card publicou a forma verbatim, com a instrucao de nao parafrasear, e as quatro linhas literais chegaram identicas ao arquivo; o par presenca-ausencia (V1 contra V2, V3 contra V4) discriminou de fato - 1 e 0 sobre o mesmo arquivo.

## Fechamento

**Desdobramento:** aprovado
