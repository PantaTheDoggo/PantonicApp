# Fixture de card_check — âncoras de arquivo:linha (`FPU-T3`)

Quatro cards sintéticos, congelados por esta fixture: nenhum é card vivo de plano nenhum. Todos
são `ready` (mundo `antes`) e a `Verificação` de cada um fecha sozinha (`` 1. `python -c
"print('a')"` → `a` — antes `a`, depois `a` ``); o que varia é a âncora de arquivo:linha em
`Arquivos-alvo`/`Passos`, conferida contra `tests/fixtures/card_check/alvo.txt`.

### AN-T1 — Card com âncora e literal em Arquivos-alvo, repetida sem literal num Passo [Sonnet · classe mecanica]
- **Status:** `ready`
- **Objetivo:** fixture de `conferir_ancoras` com duas âncoras com literal em `Arquivos-alvo` e a
  repetição de uma delas, sem literal, em `Passos` — a repetição passa porque o mesmo texto de
  âncora já tem literal em outra ocorrência do card.
- **Arquivos-alvo:**
  - `tests/fixtures/card_check/alvo.txt:2` — `dois`
  - `tests/fixtures/card_check/alvo.txt:3` — `tres \`x\``
- **Passos:**
  1. Confere de novo `tests/fixtures/card_check/alvo.txt:2` sem repetir o literal, pois já está
     ancorado em Arquivos-alvo.
- **Verificação:**
  1. `python -c "print('a')"` → `a` — antes `a`, depois `a`
- **Pronto quando:** fixture existe e `card_check.py --tarefa AN-T1` sai 0.

### AN-T2 — Card com âncora sem literal só no Passo [Sonnet · classe mecanica]
- **Status:** `ready`
- **Objetivo:** fixture de `conferir_ancoras` cuja única ocorrência da âncora
  `tests/fixtures/card_check/alvo.txt:2` está em `Passos`, sem literal em nenhuma ocorrência do
  card — falha `âncora sem literal`.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Passos:**
  1. Confere `tests/fixtures/card_check/alvo.txt:2` sem literal.
- **Verificação:**
  1. `python -c "print('a')"` → `a` — antes `a`, depois `a`
- **Pronto quando:** fixture existe e `card_check.py --tarefa AN-T2` sai 1, nomeando `âncora sem
  literal`.

### AN-T3 — Card com literal que não está na linha ancorada [Sonnet · classe mecanica]
- **Status:** `ready`
- **Objetivo:** fixture de `conferir_ancoras` cujo literal declarado (`tres`) não está contido na
  linha 2 de `alvo.txt` (`dois`) — falha `literal fora da linha`.
- **Arquivos-alvo:**
  - `tests/fixtures/card_check/alvo.txt:2` — `tres`
- **Verificação:**
  1. `python -c "print('a')"` → `a` — antes `a`, depois `a`
- **Pronto quando:** fixture existe e `card_check.py --tarefa AN-T3` sai 1, nomeando `literal fora
  da linha`.

### AN-T4 — Card sem âncora [Sonnet · classe mecanica]
- **Status:** `ready`
- **Objetivo:** fixture de `conferir_ancoras` sem nenhuma âncora de arquivo:linha em
  `Arquivos-alvo` nem em `Passos` — a conferência não acusa nada e o card não muda de
  comportamento.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Verificação:**
  1. `python -c "print('a')"` → `a` — antes `a`, depois `a`
- **Pronto quando:** fixture existe e `card_check.py --tarefa AN-T4` sai 0.
