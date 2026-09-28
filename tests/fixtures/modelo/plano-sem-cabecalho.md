# EX-0003 — Plano de exemplo sem cabeçalho do modelo
**Status:** `in-progress`
**Prefixo das tarefas no diário:** `EX-T<n>`

## 1. Modelo conceitual

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem | lastro |
|---|---|---|---|---|---|
| insumo externo | dado de entrada do fluxo de exemplo | status | um registro por rodada | externo | lastro sintético da fixture |
| resultado um | o produto da primeira operação | status | um registro validado | OP-1 | lastro sintético da fixture |

### 1.2 Fluxo de operações

- **OP-1** — Primeira operação do fluxo de exemplo.
  - `precisa de: insumo externo` · `altera: resultado um.status` · `tarefas: EX-T1`
- **OP-2** — Segunda operação do fluxo de exemplo.
  - `precisa de: resultado um` · `altera: resultado um.status` · `tarefas: EX-T2`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final |
|---|---|---|
| insumo externo.status | recebido | processado |
| resultado um.status | rascunho | validado |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 1 | 2026-09-20 | vigente | planejador |

## 4. Tarefas

### EX-T1 — Um [Sonnet · classe mecanica]
- **Status:** `done` · 2026-09-20
- **Operação do modelo:** `OP-1`
  - OP-1: Primeira operação do fluxo de exemplo.
  - precisa de: insumo externo — um registro por rodada

### EX-T2 — Dois [Sonnet · classe mecanica]
- **Status:** `in-progress` · 2026-09-20
- **Operação do modelo:** `OP-2`
  - OP-2: Segunda operação do fluxo de exemplo.
  - precisa de: resultado um — um registro validado
