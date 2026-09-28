# Fixture de card_check — corpus na forma inline (`FPU-T1`)

Cinco cards sintéticos, congelados por esta fixture: nenhum é card vivo de plano nenhum. Todos
usam a forma inline de `Verificação` (`DFP-14`): comando entre crases, `→` e o par opcional
`antes …, depois …`. `CX-T1` fecha comparando `antes`; `CX-T2` fecha comparando `depois`; `CX-T3`
não declara `antes`; `CX-T4` isola um item real de uma prosa de outro campo que contém `N.` fora
do início de linha; `CX-T5` isola dois itens reais de uma prosa na linha de continuação do
próprio item que contém `N.` fora do início de linha.

### CX-T1 — Card inline que fecha em antes [Sonnet · classe mecanica]
- **Status:** `ready`
- **Objetivo:** fixture de `card_check` na forma inline (`DFP-14`) cujo comando imprime o valor
  declarado como `antes`.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Verificação:**
  1. `python -c "print('a')"` → `b` — antes `a`, depois `b`
- **Pronto quando:** fixture existe e `card_check.py --tarefa CX-T1` sai 0, comparando `antes`.

### CX-T2 — Card inline que fecha em depois [Sonnet · classe mecanica]
- **Status:** `done`
- **Objetivo:** fixture de `card_check` na forma inline (`DFP-14`) cujo comando imprime o valor
  declarado como `depois`.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Verificação:**
  1. `python -c "print('b')"` → `b` — antes `a`, depois `b`
- **Pronto quando:** fixture existe e `card_check.py --tarefa CX-T2` sai 0, comparando `depois`;
  com `--mundo antes` sai 1, nomeando a divergência.

### CX-T3 — Card inline sem antes [Sonnet · classe mecanica]
- **Status:** `ready`
- **Objetivo:** fixture de `card_check` na forma inline (`DFP-14`) sem o par `antes`/`depois`.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Verificação:**
  1. `python -c "print('a')"` → `a`
- **Pronto quando:** fixture existe e `card_check.py --tarefa CX-T3` sai 1, nomeando `sem valor
  antes`.

### CX-T4 — Card inline com prosa de outro campo contendo N. fora do início de linha [Sonnet · classe mecanica]
- **Status:** `ready`
- **Objetivo:** fixture de `card_check` cujo campo `Contingências` contém a prosa `acionamento 1.
  medido`, fora do início de linha — não pode virar item fantasma na `Verificação`, que tem um
  item só.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Verificação:**
  1. `python -c "print('a')"` → `b` — antes `a`, depois `b`
- **Contingências:** prosa de teste — acionamento 1. medido, sem item novo de Verificação.
- **Pronto quando:** fixture existe e `card_check.py --tarefa CX-T4` sai 0, reconhecendo
  exatamente um item.

### CX-T5 — Card inline com prosa N. na continuação do item de Verificação [Sonnet · classe mecanica]
- **Status:** `ready`
- **Objetivo:** fixture de `card_check` cuja `Verificação` tem dois itens, com a linha de
  continuação do item 1 trazendo prosa que contém `1.` e `2.` fora do início de linha — não pode
  virar item fantasma, discriminando o caso que `CX-T4` (prosa noutro campo) não cobre.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Verificação:**
  1. `python -c "print('a')"` → `b` — antes `a`, depois `b`; medido no
     acionamento 1. e conferido na revisão 2. da mesma janela
  2. `python -c "print('c')"` → `d` — antes `c`, depois `d`
- **Pronto quando:** fixture existe e `card_check.py --tarefa CX-T5` sai 0, reconhecendo
  exatamente dois itens.
