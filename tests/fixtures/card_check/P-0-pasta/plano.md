# P-0 — Fixture de card_check em plano em pasta

**Prefixo das tarefas no diário:** `CP-T<n>`

### CP-T1 — Card concluído de plano em pasta [Sonnet · classe mecanica]
- **Objetivo:** fixture de `card_check`: o status `done` mora só em `estado.tsv`.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Verificação:**
  1. `python -c "print('b')"` → `b` — antes `a`, depois `b`
- **Pronto quando:** `card_check.py --tarefa CP-T1` sai 0, comparando `depois`.

### CP-T2 — Card pronto de plano em pasta [Sonnet · classe mecanica]
- **Objetivo:** fixture de `card_check`: o status `ready` mora só em `estado.tsv`.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Verificação:**
  1. `python -c "print('a')"` → `b` — antes `a`, depois `b`
- **Pronto quando:** `card_check.py --tarefa CP-T2` sai 0, comparando `antes`.
