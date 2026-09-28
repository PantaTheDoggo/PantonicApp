# LT-0001 — Plano de exemplo sem lastro declarado
**Status:** `in-progress`
**Prefixo das tarefas no diário:** `LT-T<n>`

## 1. Modelo conceitual

**Estado do modelo:** versão 1 · 2026-09-22 · autor: planejador · 1 operações · 2 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem |
|---|---|---|---|---|
| insumo do teste | dado de entrada do fluxo sem lastro | status | um registro por rodada | externo |
| resultado do teste | o produto da operação | status | um registro validado | OP-1 |

### 1.2 Fluxo de operações

- **OP-1** — Primeira operação do fluxo sem lastro.
  - `precisa de: insumo do teste` · `altera: resultado do teste.status` · `tarefas: LT-T1`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final |
|---|---|---|
| insumo do teste.status | recebido | processado |
| resultado do teste.status | rascunho | validado |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 1 | 2026-09-22 | vigente | planejador |

## 4. Tarefas

### LT-T1 — Um [Sonnet · classe mecanica]
- **Status:** `done` · 2026-09-22
- **Operação do modelo:** `OP-1`
  - OP-1: Primeira operação do fluxo sem lastro.
  - precisa de: insumo do teste — um registro por rodada
