# EX-0007 — Plano de exemplo inválido, parte dois
**Status:** `in-progress`
**Prefixo das tarefas no diário:** `EX2-T<n>`

## 1. Modelo conceitual

**Estado do modelo:** versão 1 · 2026-09-20 · autor: revisor · 5 operações · 3 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem |
|---|---|---|---|---|
| objeto zero | insumo externo usado pelas duas primeiras operações | estado | um registro de entrada | externo |
| objeto de OP-1 | produto legítimo da primeira operação | estado | um registro validado | OP-1 |
| objeto de OP-5 | produto legítimo da quinta operação, citado cedo demais | estado | um registro adiantado | OP-5 |

### 1.2 Fluxo de operações

- **OP-1** — Primeira operação, base do fluxo.
  - `precisa de: objeto zero` · `altera: objeto de OP-1.estado` · `tarefas: EX2-T1`
- **OP-2** — Segunda operação, sem nenhum objeto encadeado.
  - `precisa de: objeto zero` · `altera: objeto de OP-1.estado` · `tarefas: EX2-T2`
- **OP-3** — Terceira operação, citando objeto produzido depois dela.
  - `precisa de: objeto de OP-1, objeto de OP-5` · `altera: objeto de OP-1.estado` · `tarefas: EX2-T3`
- **OP-3** — Terceira operação repetida, mesmo identificador.
  - `precisa de: objeto de OP-1` · `altera: objeto de OP-1.estado` · `tarefas: EX2-T4`
- **OP-5** — Quinta operação, fora da sequência esperada.
  - `precisa de: objeto de OP-1` · `altera: objeto de OP-1.estado` · `tarefas: EX2-T5`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final |
|---|---|---|
| objeto zero.estado | inicial | final |
| objeto de OP-1.estado | inicial | final |
| objeto de OP-5.estado | inicial | final |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 1 | 2026-09-20 | vigente | revisor |

## 4. Tarefas

### EX2-T1 — Um [Sonnet · classe mecanica]
- **Status:** `done` · 2026-09-20
- **Operação do modelo:** `OP-1`
  - OP-1: Primeira operação, base do fluxo.
  - precisa de: objeto zero — um registro de entrada

### EX2-T2 — Dois [Sonnet · classe mecanica]
- **Status:** `in-progress` · 2026-09-20
- **Operação do modelo:** `OP-2`
  - OP-2: Segunda operação, sem nenhum objeto encadeado.
  - precisa de: objeto zero — um registro de entrada

### EX2-T3 — Três [Sonnet · classe mecanica]
- **Status:** `ready` · 2026-09-20
- **Operação do modelo:** `OP-3`
  - OP-3: Terceira operação, citando objeto produzido depois dela.
  - precisa de: objeto de OP-1 — um registro validado; objeto de OP-5 — um registro adiantado

### EX2-T4 — Quatro [Sonnet · classe mecanica]
- **Status:** `ready` · 2026-09-20
- **Operação do modelo:** `OP-3`
  - OP-3: Terceira operação repetida, mesmo identificador.
  - precisa de: objeto de OP-1 — um registro validado

### EX2-T5 — Cinco [Sonnet · classe mecanica]
- **Status:** `ready` · 2026-09-20
- **Operação do modelo:** `OP-5`
  - OP-5: Quinta operação, fora da sequência esperada.
  - precisa de: objeto de OP-1 — um registro validado
