# EX-0009 — Plano de exemplo com versão pendente
**Status:** `in-progress`
**Prefixo das tarefas no diário:** `EX-T<n>`

## 1. Modelo conceitual

**Estado do modelo:** versão 1 · 2026-09-10 · autor: planejador · 1 operações · 2 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem |
|---|---|---|---|---|
| insumo externo | dado de entrada do fluxo pendente | status | um registro por rodada | externo |
| resultado alfa | o produto da primeira operação | status | um registro validado | OP-1 |
| objeto obsoleto | objeto que sai na versão pendente | nota | um registro descontinuado | externo |

### 1.2 Fluxo de operações

- **OP-1** — Primeira operação do fluxo pendente.
  - `precisa de: insumo externo` · `altera: resultado alfa.status` · `tarefas: EX-T1`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final |
|---|---|---|
| resultado alfa.status | rascunho | validado |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 1 | 2026-09-10 | vigente | planejador |
| 2 | 2026-09-21 | pendente | revisor |

## 1A. Modelo conceitual — versão pendente de validação

**Estado do modelo:** versão 2 · 2026-09-21 · autor: revisor · 2 operações · 3 propriedades · situação: pendente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem |
|---|---|---|---|---|
| insumo externo | dado de entrada do fluxo pendente | status | um registro por rodada | externo |
| resultado alfa | o produto da primeira operação | status, prazo | um registro validado | OP-1 |
| resultado beta | o produto da segunda operação, nova nesta versão | nível | um relatório derivado | OP-2 |

### 1.2 Fluxo de operações

- **OP-1** — Primeira operação do fluxo pendente.
  - `precisa de: insumo externo` · `altera: resultado alfa.status, resultado alfa.prazo` · `tarefas: EX-T1`
- **OP-2** — Segunda operação, nova nesta versão pendente.
  - `precisa de: resultado alfa` · `altera: resultado beta.nível` · `tarefas: EX-T2`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final |
|---|---|---|
| resultado alfa.status | rascunho | aprovado |
| resultado alfa.prazo | sem prazo | 30 dias |
| resultado beta.nível | inicial | alto |

## 4. Tarefas

### EX-T1 — Um [Sonnet · classe mecanica]
- **Status:** `done` · 2026-09-20
- **Operação do modelo:** `OP-1`
  - OP-1: Primeira operação do fluxo pendente.
  - precisa de: insumo externo — um registro por rodada

### EX-T2 — Dois [Sonnet · classe mecanica]
- **Status:** `ready` · 2026-09-20
- **Operação do modelo:** `OP-2`
  - OP-2: Segunda operação, nova nesta versão pendente.
  - precisa de: resultado alfa — um registro validado
