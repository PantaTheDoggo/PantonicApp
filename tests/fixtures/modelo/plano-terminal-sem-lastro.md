# LT-0003 — Plano de exemplo terminal sem lastro declarado
**Status:** `done`
**Prefixo das tarefas no diário:** `LT3-T<n>`

## 1. Modelo conceitual

**Estado do modelo:** versão 1 · 2026-09-22 · autor: planejador · 1 operações · 2 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem |
|---|---|---|---|---|
| insumo terminal | dado de entrada do fluxo terminal | status | um registro por rodada | externo |
| resultado terminal | o produto da operação | status | um registro validado | OP-1 |

### 1.2 Fluxo de operações

- **OP-1** — Primeira operação do fluxo terminal.
  - `precisa de: insumo terminal` · `altera: resultado terminal.status` · `tarefas: LT3-T1`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final |
|---|---|---|
| insumo terminal.status | recebido | processado |
| resultado terminal.status | rascunho | validado |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 1 | 2026-09-22 | vigente | planejador |

## 4. Tarefas

### LT3-T1 — Um [Sonnet · classe mecanica]
- **Status:** `done` · 2026-09-22
- **Operação do modelo:** `OP-1`
  - OP-1: Primeira operação do fluxo terminal.
  - precisa de: insumo terminal — um registro por rodada
