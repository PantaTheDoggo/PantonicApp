# RDO — P-0746 · LST-T1

**Plano:** `docs/plans/P-0746-lastro-do-modelo.md`
**Tarefa:** `LST-T1` — O critério de admissão do modelo e as duas vias do enunciado
**Modelo:** Opus · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `GOVERNANCA.md` §3.2 e a subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras` passam a exigir lastro declarado para todo objeto, operação e propriedade, e a distinguir as duas vias pelas quais o enunciado alimenta o modelo — estado e operação.

**Arquivos-alvo:** - `GOVERNANCA.md` §3.2 — parágrafo novo imediatamente depois de **Objeto, operação e propriedade** e antes de **Estado inicial, estado final e o aceite do plano** - `.claude/skills/diario-de-obras/SKILL.md` — subseção *Modelo de domínio (seção do plano)*

**Verificação:** 1. ``` grep -ci 'lastro' GOVERNANCA.md ``` → **≥ 3**. **Medido antes: 0** (`F-9`). 2. ``` grep -ci 'lastro' .claude/skills/diario-de-obras/SKILL.md ``` → **≥ 1**. **Medido antes: 0** (`F-9`). 3. ``` python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md ``` → exit **0** (`I-2`). 4. ``` python -m pytest tests -q ``` → **≥ 262 passed** (`I-3`).

**Pronto quando:** as quatro verificações imprimem os valores declarados e nenhum arquivo fora dos `Arquivos-alvo` foi editado. Por propriedade que a operação altera: - `restrições do modelo conceitual.leitura de lastro` — todo objeto, operação e propriedade tem âncora declarada num trecho do enunciado do problema ou do prompt de origem; elemento sem âncora não entra no modelo — Verificação 1 e 2. - `restrições do modelo conceitual.leitura de prompt` — o enunciado alimenta o modelo por duas vias declaradas: estado, que popula o inicial e o final, e operação, que é o que o plano faz diante do vão entre os dois — Verificação 1 e 2.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-21
- **Depende de:** —
- **Fundamento:** `DLS-1`, `DLS-2`; fatos `F-1`, `F-2`, `F-6`, `F-9`; invariantes `I-2`, `I-3`.
- **Operação do modelo:** `OP-1`, `OP-2` - OP-1: O redator da norma constrói a restrição de leitura de lastro: todo objeto, operação e propriedade do modelo tem âncora declarada num trecho do enunciado do problema ou do prompt que originou o plano, e elemento sem essa âncora não entra no modelo. - precisa de: — a `OP-1` constrói o objeto; não há objeto anterior a consumir - OP-2: O redator da norma constrói a restrição de leitura de prompt: o enunciado alimenta o modelo por duas vias declaradas — a via de estado, que popula o estado inicial e o estado final, e a via de operação, que é o que o plano faz diante do vão entre os dois. - precisa de: restrições do modelo conceitual — norma em `GOVERNANCA.md` §3.2; forma publicada na subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras`; aferição em `.claude/tools/modelo.py` (`check`), com `tests/test_modelo.py` e fixtures; autoria em `.claude/agents/pantonic-model-designer.md`
- **Camada e fronteira:** doutrina e gramática publicada. Nenhum instrumento, nenhum agente, nenhum teste novo — a aferição é da `LST-T5`.
- **Domínio:** *lastro* — a âncora de um elemento do modelo num trecho do enunciado (`## 0`) ou do prompt de origem. *Via de estado* — o trecho do enunciado que descreve como as coisas estão ou deverão estar; popula `### 1.3`. *Via de operação* — o trecho que pede ação; popula `### 1.2`.
- **Fora do escopo desta tarefa:** a restrição de decomposição (`LST-T7`), a residência do requisito secundário (`LST-T3`), o instrumento (`LST-T5`). A vigência bilateral e o drift saíram do plano na versão 3 do modelo e viraram o `TK-70` (`DLS-11`).

## Execução

**Consumo:** 6 tool uses, 49.2 k tokens, 108.2 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: a linha objetos da tabela da gramatica (SKILL.md) segue declarando cinco colunas enquanto a 1.1 do P-0746 ja usa seis com lastro na secao 0; o card nao prescreve alteracao de coluna e a afericao e da LST-T5.
laudo: A LST-T5 fica sem rota executavel: afere presenca de declaracao de lastro e proibe editar doutrina, mas nenhum card publica a residencia da declaracao na gramatica - decisao de forma (coluna nova em 1.1 e campo em 1.2/1.3) e do dono/planejamento, antes de despachar a LST-T5.

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

Duas observacoes. (1) O executor parou e devolveu pendencia autoral em vez de inventar a sexta coluna: e o comportamento correto sob G-NOASK, e o defeito e do card, que instituiu uma exigencia de declaracao sem prescrever onde ela se declara. Punir a execucao aqui ensinaria o loop a decidir calado. (2) Card de classe redacao cuja verificacao inteira e contagem de ocorrencia de palavra compra verde barato: o texto entregue e bom, mas a linha de aceite teria saido verde com tres mencoes decorativas de lastro. Para norma, o aceite discriminante e recorte do literal da forma publicada, nao contagem.

## Fechamento

**Desdobramento:** aprovado com ressalva
