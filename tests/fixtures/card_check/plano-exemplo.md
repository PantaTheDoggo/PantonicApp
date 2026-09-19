# Fixture de card_check (`LM-T5b`, `LM-T5c`)

Seis cards sintéticos, congelados por esta fixture (`DM-38` (ii)): nenhum é card vivo de plano
nenhum. `EX-T1` é conforme à forma normativa de `docs/RUBRICA_DE_REVISAO.md` `### 8.1`; `EX-T2` e
`EX-T3` são, cada um, a fixture de exatamente uma das duas falhas nomeadas que `card_check.py`
já pegava na `LM-T5b`. `EX-T4`, `EX-T5` e `EX-T6` são, cada um, a fixture de exatamente uma das
matérias que a `LM-T5c` fechou: prosa antes do bloco cercado (fora da forma da `### 8.1`), pipe
dentro de argumento citado (não é recusa) e `**Aferição: manual**` sobre comando executável (o
marcador é rejeitado).

### EX-T1 — Card conforme à forma normativa [Sonnet · classe mecanica]
- **Objetivo:** fixture de `card_check` com os três elementos completos em todo item, e o valor
  `Medido antes` batendo com a saída real do comando na árvore de teste.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Verificação:**
  1. ```
     python -c "print(2)"
     ```
     → imprime **2**. **Medido antes: 2**
- **Pronto quando:** fixture existe e `card_check.py --tarefa EX-T1` sai 0.

### EX-T2 — Card com item sem Medido antes [Sonnet · classe mecanica]
- **Objetivo:** fixture de `card_check` com um item de `Verificação` que tem comando e `→`, mas
  não declara `**Medido antes:**`.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Verificação:**
  1. ```
     python -c "print(2)"
     ```
     → imprime **2**.
- **Pronto quando:** fixture existe e `card_check.py --tarefa EX-T2` sai 1, nomeando o elemento
  `Medido antes` como ausente.

### EX-T3 — Card com Medido antes divergente [Sonnet · classe mecanica]
- **Objetivo:** fixture de `card_check` com os três elementos presentes, mas o valor de
  `**Medido antes:**` não bate com a saída real do comando na árvore de teste.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Verificação:**
  1. ```
     python -c "print(2)"
     ```
     → imprime **2**. **Medido antes: 3**
- **Pronto quando:** fixture existe e `card_check.py --tarefa EX-T3` sai 1, nomeando a
  divergência entre o valor declarado e o valor medido.

### EX-T4 — Card com prosa antes do bloco cercado [Sonnet · classe mecanica]
- **Objetivo:** fixture de `card_check` com um item cuja prosa abre o item, antes do bloco
  cercado — viola a forma normativa da `### 8.1`, que exige o bloco logo após `N.`.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Verificação:**
  1. Roda o comando abaixo e confere a saída.
     ```
     python -c "print(2)"
     ```
     → imprime **2**. **Medido antes: 2**
- **Pronto quando:** fixture existe e `card_check.py --tarefa EX-T4` sai 1, nomeando
  `item 1: fora da forma da 8.1`.

### EX-T5 — Card com pipe dentro de argumento citado [Sonnet · classe mecanica]
- **Objetivo:** fixture de `card_check` com a forma canônica de comando do kit — `pwsh` com um
  `-Command` citado contendo `|` — confirmando que o pipe dentro do argumento citado não é
  recusado.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command "(1,2,3,4 | Measure-Object).Count"
     ```
     → imprime **4**. **Medido antes: 4**
- **Pronto quando:** fixture existe e `card_check.py --tarefa EX-T5` sai 0.

### EX-T6 — Card com Aferição manual sobre comando executável [Sonnet · classe mecanica]
- **Objetivo:** fixture de `card_check` com `**Aferição: manual**` declarado sobre um item cujo
  comando é executável — o marcador só vale sobre comando recusado ou ausente.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Verificação:**
  1. ```
     python -c "print(2)"
     ```
     → imprime **2**. **Medido antes: 2**. **Aferição: manual**
- **Pronto quando:** fixture existe e `card_check.py --tarefa EX-T6` sai 1, nomeando o marcador
  `Aferição: manual` sobre comando executável.
