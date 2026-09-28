# EX-0002 — Plano de exemplo inválido
**Status:** `in-progress`
**Prefixo das tarefas no diário:** `EX-T<n>`

## 1. Modelo conceitual

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem | lastro |
|---|---|---|---|---|---|
| objeto base | objeto usado normalmente pela primeira operação | estado | um registro simples | externo | lastro sintético da fixture |
| objeto sem uso | objeto externo que nenhuma operação cita | estado | um registro não usado | externo | lastro sintético da fixture |
| objeto orfão | objeto cuja origem aponta para uma operação inexistente | estado | um registro órfão | OP-9 | lastro sintético da fixture |
| objeto válido segundo | objeto produzido pela primeira operação | estado | um registro validado | OP-1 | lastro sintético da fixture |

### 1.2 Fluxo de operações

- **OP-1** — Primeira operação, com objeto inexistente citado.
  - `precisa de: objeto base, objeto fantasma` · `altera: objeto válido segundo.estado` · `tarefas: EX-T1`
- **OP-2** — Segunda operação, sem tarefa nenhuma.
  - `precisa de: objeto válido segundo` · `altera: objeto válido segundo.estado` · `tarefas: `
- **OP-3** — Terceira operação, citando tarefa inexistente.
  - `precisa de: objeto válido segundo` · `altera: objeto válido segundo.estado` · `tarefas: EX-T99`
- **OP-4** — Quarta operação, cujo texto usa o caminho docs/x.md.
  - `precisa de: objeto válido segundo` · `altera: objeto válido segundo.estado` · `tarefas: EX-T1`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final |
|---|---|---|
| objeto base.estado | inicial | final |
| objeto sem uso.estado | inicial | final |
| objeto orfão.estado | inicial | final |
| objeto válido segundo.estado | inicial | final |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 1 | 2026-09-20 | vigente | revisor |

## 4. Tarefas

### EX-T1 — Um [Sonnet · classe mecanica]
- **Status:** `done` · 2026-09-20
- **Operação do modelo:** `OP-1`, `OP-4`
  - OP-1: Primeira operação, com objeto inexistente citado.
  - precisa de: objeto base — um registro simples
  - OP-4: Quarta operação, cujo texto usa o caminho docs/x.md.
  - precisa de: objeto válido segundo — um registro validado

### EX-T2 — Dois [Sonnet · classe mecanica]
- **Status:** `in-progress` · 2026-09-20

### EX-T3 — Três [Sonnet · classe mecanica]
- **Status:** `ready` · 2026-09-20
- **Operação do modelo:** `OP-77`
  - OP-77: texto copiado para uma operação que não existe no fluxo.
  - precisa de: objeto inventado — contrato inventado

### EX-T4 — Quatro [Sonnet · classe mecanica]
- **Status:** `ready` · 2026-09-20
- **Operação do modelo:** `OP-2`
