# LT-0002 — Plano de exemplo com lastro declarado
**Status:** `in-progress`
**Prefixo das tarefas no diário:** `LT2-T<n>`

## 1. Modelo conceitual

**Estado do modelo:** versão 1 · 2026-09-22 · autor: planejador · 1 operações · 2 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem | lastro na §0 |
|---|---|---|---|---|---|
| insumo com lastro | dado de entrada do fluxo com lastro | status | um registro por rodada | externo | citado na §0 como insumo do problema |
| resultado com lastro | o produto da operação | status | um registro validado | OP-1 | citado na §0 como resultado esperado |

### 1.2 Fluxo de operações

- **OP-1** — Primeira operação do fluxo com lastro.
  - `precisa de: insumo com lastro` · `altera: resultado com lastro.status` · `tarefas: LT2-T1` · `lastro: citado na §0 como a operação a executar`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final | lastro |
|---|---|---|---|
| insumo com lastro.status | recebido | processado | citado na §0 como estado inicial |
| resultado com lastro.status | rascunho | validado | citado na §0 como estado final |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 1 | 2026-09-22 | vigente | planejador |

## 4. Tarefas

### LT2-T1 — Um [Sonnet · classe mecanica]
- **Status:** `done` · 2026-09-22
- **Operação do modelo:** `OP-1`
  - OP-1: Primeira operação do fluxo com lastro.
  - precisa de: insumo com lastro — um registro por rodada
