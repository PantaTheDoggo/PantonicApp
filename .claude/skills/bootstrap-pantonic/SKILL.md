---
name: bootstrap-pantonic
description: Inicializa um novo projeto Pantonic* — os quatro artefatos (PRD, Architecture, Spec, Sprint Plan), a estrutura de docs ATIVO/HISTÓRICO e o esqueleto do core reusável. Usar ao criar um projeto novo da família Pantonic* ou ao auditar se um projeto existente segue o padrão.
---

# bootstrap-pantonic — nascimento de um projeto Pantonic*

Pré-requisito de leitura: `GOVERNANCA.md` e `ARQUITETURA_PANTONICA.md` (na pasta-mãe
PantonicApp ou copiados para o projeto). Este fluxo é conduzido pelo agente `pantonic-planner`;
a implementação (fase 5) é do `pantonic-executor`, uma tarefa por contexto.

## Fases

### 1. PRD (`docs/PRD.md`)
Coletar com o usuário: objetivos, casos de uso (UC-*), requisitos (RF-*/RNF-*), elementos de
domínio, estruturas de dados e **linguagem ubíqua**. Sem PRD aprovado, nada avança.

### 2. Architecture (`docs/ARCHITECTURE.md`)
Partir do core pantonico (não redesenhar infraestrutura): copiar o modelo de camadas, golden
rules e catálogos da ARQUITETURA_PANTONICA e **especializar só** `contracts/domain/`, serviços
de domínio e plugins. Cada responsabilidade de camada mapeada a UC/RF do PRD. Definir os
limites: o que é [REPLICAR] e o que é [ESPECIALIZAR] neste projeto.

### 3. Spec (`docs/SPEC.md`)
Materializar responsabilidades em classes Python: filesystem proposto, assinaturas, docstrings,
e técnicas de desacoplamento (inversão de dependência, strategy, unit of work). Todo Protocol
novo nasce em `contracts/`.

### 4. Sprint Plan (`docs/SPRINT_PLAN.md` → diário de obras)
Organizar o Spec em checklists de tarefas atômicas (skill `diario-de-obras`), ordenados para
entregáveis rapidamente testáveis pelo usuário. Definir os TF-* de cada tarefa. A ordem de
implementação do core segue ARQUITETURA_PANTONICA §15:

1. `contracts` instalável (portas genéricas) → 2. componentes de bootstrap → 3. injetor +
serviços de expressão → 4. UI shell mínima → 5. PluginRegistry + plugin "hello" →
6. suíte de conformance (vira gate) → 7. domínio/plugins do PRD.

### 5. Estrutura inicial do repositório
```
docs/            PRD, ARCHITECTURE, SPEC, DIARIO_DE_OBRAS, AS-IS (baseline), LICOES_APRENDIDAS
docs/plans/      P-<MMDD>-<slug>.md (planos completos) + _INBOX.md (append-only, drenado
                 para o diário pela skill diario-de-obras) — destino de planos de agentes
                 paralelos, nunca escritos direto no diário (GOVERNANCA §4.2)
infracore/  contracts/src/contracts/  services/  plugins/  tests/  tools/
CLAUDE.md        ≤ 200 linhas, só regras que mudam comportamento
.claude/agents/  copiar pantonic-planner, pantonic-executor, pantonic-scout do kit
.claude/skills/  copiar diario-de-obras, proximo-passo, integrar-poc, guardrails-check, handover
```

## Aceitação

- Os 4 artefatos existem, com rastreabilidade PRD → Architecture → Spec → Sprint Plan.
- Diário de obras criado com o primeiro sprint em `backlog`, diretiva de priorização vazia.
- `docs/plans/_INBOX.md` criado vazio.
- Docs separados ATIVO × HISTÓRICO; DOC_MAP planejado para quando um doc passar de 500 linhas.
- Kit agêntico copiado e ajustado (fatos estáveis apontando para os paths do projeto).
