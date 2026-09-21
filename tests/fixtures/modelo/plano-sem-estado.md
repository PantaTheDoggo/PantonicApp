# EX-0008 — Plano de exemplo sem estado inicial e final
**Status:** `in-progress`
**Prefixo das tarefas no diário:** `EX-T<n>`

## 1. Modelo conceitual

**Estado do modelo:** versão 1 · 2026-09-20 · autor: planejador · 2 operações · 2 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem |
|---|---|---|---|---|
| insumo externo | dado de entrada do fluxo de exemplo | status | um registro por rodada | externo |
| resultado um | o produto da primeira operação | status, nota | um registro validado | OP-1 |

### 1.2 Fluxo de operações

- **OP-1** — Primeira operação do fluxo sem estado.
  - `precisa de: insumo externo` · `altera: resultado um.status` · `tarefas: EX-T1`
- **OP-2** — Segunda operação do fluxo sem estado.
  - `precisa de: resultado um` · `altera: resultado um.nota` · `tarefas: EX-T2`

### 1.3 Mudanças do modelo

| id | data | autor | operações | o que mudou e por quê |
|---|---|---|---|---|
| — | — | — | — | fixture na forma anterior — sem estado inicial e final (`MC-T2`) |

## 4. Tarefas

### EX-T1 — Um [Sonnet · classe mecanica]
- **Status:** `done` · 2026-09-20
- **Operação do modelo:** `OP-1`
  - OP-1: Primeira operação do fluxo sem estado.
  - precisa de: insumo externo — um registro por rodada

### EX-T2 — Dois [Sonnet · classe mecanica]
- **Status:** `ready` · 2026-09-20
- **Operação do modelo:** `OP-2`
  - OP-2: Segunda operação do fluxo sem estado.
  - precisa de: resultado um — um registro validado
