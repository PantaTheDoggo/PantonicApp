# RDO — P-0746 · LST-T7

**Plano:** `docs/plans/P-0746-lastro-do-modelo.md`
**Tarefa:** `LST-T7` — A restrição de decomposição: o que é objeto e o que é propriedade
**Modelo:** Opus · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `GOVERNANCA.md` §3.2 e a subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras` passam a declarar como o enunciado se decompõe antes de virar modelo: o que o plano constrói é **objeto**; o que converge de um estado a outro é **propriedade** dele; descrição de estado não vira objeto próprio; e operação é o ato que altera propriedade.

**Arquivos-alvo:** - `GOVERNANCA.md` §3.2 — parágrafo novo imediatamente depois do que a `LST-T1` acrescentou - `.claude/skills/diario-de-obras/SKILL.md` — subseção *Modelo de domínio (seção do plano)*

**Verificação:** 1. ``` grep -cF 'o que o plano constrói é objeto' GOVERNANCA.md ``` → **≥ 1**. **Medido antes: 0** (2026-09-21). 2. ``` grep -cF 'promoção indevida' GOVERNANCA.md ``` → **≥ 1**. **Medido antes: 0** (2026-09-21). 3. ``` grep -cF 'descrição de estado não vira objeto próprio' .claude/skills/diario-de-obras/SKILL.md ``` → **≥ 1**. **Medido antes: 0** (2026-09-21). 4. Par presença-ausência sobre o texto: a norma dá, por literal, o teste que separa os dois — objeto é o que o plano constrói, propriedade é o que converge — e nomeia a promoção indevida como defeito, citando o caso medido do `F-11`. 5. ``` python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md ``` → exit **0** (`I-2`). 6. ``` python -m pytest tests -q ``` → **≥ 262 passed** (`I-3`).

**Pronto quando:** as seis verificações saem nos valores declarados e nenhum arquivo fora dos `Arquivos-alvo` foi editado. Por propriedade que a operação altera: - `restrições do modelo conceitual.decomposição em objeto e propriedade` — o enunciado se decompõe primeiro em objeto e propriedade: o que o plano constrói é objeto, o que converge de um estado a outro é propriedade dele, e descrição de estado não vira objeto próprio — Verificação 1, 2, 3 e 4.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-22
- **Depende de:** `LST-T1`
- **Fundamento:** `DLS-9`; fatos `F-11`, `F-12`. Card autorado na republicação: a versão 1 do modelo **deste** plano é o caso medido do defeito que a restrição proíbe.
- **Operação do modelo:** `OP-3` - OP-3: O redator da norma constrói a restrição de decomposição: o enunciado se decompõe primeiro em objeto e propriedade — o que o plano constrói é objeto, o que converge de um estado a outro é propriedade dele — e descrição de estado nunca vira objeto próprio. - precisa de: restrições do modelo conceitual — norma em `GOVERNANCA.md` §3.2; forma publicada na subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras`; aferição em `.claude/tools/modelo.py` (`check`), com `tests/test_modelo.py` e fixtures; autoria em `.claude/agents/pantonic-model-designer.md`
- **Camada e fronteira:** doutrina e gramática publicada. Nenhum instrumento, nenhum agente, nenhum teste novo — a restrição desta tarefa é de julgamento do autor do modelo, e a `LST-T5` **não** a torna aferível: não há como um `check` decidir se um substantivo do enunciado é objeto ou propriedade. A guarda dela é o Marco, não o instrumento.
- **Domínio:** *objeto* — o que o plano constrói ou torna conforme, e que não existia ou não estava conforme quando o plano começou. *Propriedade* — a dimensão do objeto que tem estado inicial e estado final distintos. *Promoção indevida* — propriedade escrita como objeto próprio, o defeito que infla a tabela `### 1.1` e que o dono recusou duas vezes em 2026-09-21 (`F-11`).
- **Literais obrigatórios (verbatim, não parafrasear):** o card fixa o recorte que a norma tem de conter, e a prosa em volta é autoria do executor (`DLS-14`). São três: em `GOVERNANCA.md`, `o que o plano constrói é objeto` e `promoção indevida`; na skill, `descrição de estado não vira objeto próprio`.
- **Nota de aceite (`F-16`):** use `grep -cF` (literal, sensível a maiúscula) — neste ambiente `grep -ciF` **aborta** com exit `134`. Contagem de ocorrência da palavra **não** é aceite: o defeito medido na `LST-T1` é que `grep -ci 'lastro'` sairia verde com três menções decorativas (`AE-2`, `DLS-14`).
- **Fora do escopo desta tarefa:** as leituras de lastro e de prompt (`LST-T1`, já fechadas); a residência do requisito secundário (`LST-T3`); o instrumento (`LST-T5`); reescrever o modelo do `P-0745` (`LST-T6`); a vigência e o drift, que saíram do plano no `TK-70` (`DLS-11`).

## Execução

**Consumo:** 5 tool uses, 46.8 k tokens, 80.6 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Tres observacoes. (1) O card corrigiu, um card depois, o defeito que a licao 2 do laudo da LST-T1 nomeou: o aceite saiu de contagem de ocorrencia de palavra para recorte verbatim de tres literais da forma publicada, com Medido antes: 0 por linha, e passou a discriminar de verdade. Feedback de laudo virando emenda de autoria dentro do mesmo plano e o ciclo funcionando. (2) O literal verbatim garante que a frase pousa, nao que o contexto ao redor dela esteja certo: a inexatidao do caso medido atravessou tres linhas de aceite verdes e so aparece confrontando o texto com F-1, F-11 e F-12. Para doutrina de kit, o aceite por literal precisa de par com conferencia do fato citado. (3) Exercicio ponta a ponta do modulo: os dois alvos ficaram coerentes entre si e com o resto da 3.2, e modelo.py check e show seguiram verdes sobre P-0743, P-0745 e P-0746.

## Fechamento

**Desdobramento:** aprovado
