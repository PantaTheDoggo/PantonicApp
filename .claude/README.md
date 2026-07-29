# Kit agêntico Pantonic* — agentes e skills reusáveis

Este diretório é o **kit padrão** de todo projeto Pantonic*. Ao criar um projeto novo, copie
`agents/` e `skills/` para o `.claude/` do projeto e ajuste apenas os caminhos citados nos
blocos de "fatos estáveis" dos agentes. Fundamentos: `GOVERNANCA.md` e
`ARQUITETURA_PANTONICA.md` na raiz da pasta PantonicApp.

## Agentes (`agents/`)

| Agente | Modelo | Papel |
|---|---|---|
| `pantonic-planner` | Opus (Fable só sob solicitação explícita do dono) | PRD/Architecture/Spec/Sprint Plan; decomposição em tarefas atômicas |
| `pantonic-executor` | Sonnet | Uma tarefa do diário por contexto, com TDD e guardrails |
| `pantonic-scout` | Haiku | Coleta (search/grep/leitura) → dossiês compactos; somente leitura |
| `pantonic-auditor-arch` | Opus | Auditoria de clean architecture → checklist de desvios + ações de recuperação |
| `pantonic-auditor-cleancode` | Sonnet | Auditoria de code smells (coesão/acoplamento) → checklist + correções |
| `pantonic-fora-da-caixa` | Opus | Redesenho "do zero, hoje" de procedimentos inchados por remendos |
| `pantonic-auditor-pyside6` | Sonnet | Auditoria de melhores práticas Qt (threading, signals, ownership, perf) |
| `pantonic-benchmarker` | Haiku | Coletor de benchmarking de frameworks públicos → relatório D1..D16 em `docs/benchmark/` (um repositório por invocação) |

Os auditores são invocados pelo usuário, produzem relatórios em `docs/audits/` e **não alteram
código** — apontamentos aceitos viram tíquetes no diário de obras via `pantonic-planner`.
**Antes de invocar qualquer auditor, rode a skill `audit-sweep`** (contexto principal): ela
executa a fase mecânica (greps determinísticos) via `pantonic-scout` (Haiku) e grava
`docs/audits/SWEEP_<data>.md`; o auditor parte do sweep e gasta o modelo caro só na leitura
confirmatória.

**Manutenção dos scouts:** `pantonic-scout` = `context-scout` global
(`~/.claude/agents/context-scout.md`) + bloco de fatos estáveis do projeto. Toda melhoria em
um deve ser replicada no outro — edite sempre os dois juntos.
Bases de conhecimento dos auditores: `D:\Skillstore\Ready\skill\python_clean_architecture_skill.md`
(arch) e `D:\Skillstore\Ready\skill\pyside_skill.md` (pyside6) — ajustar os caminhos se o
Skillstore mudar de lugar.

## Skills (`skills/`)

| Skill | Quando usar |
|---|---|
| `bootstrap-pantonic` | Criar projeto novo (4 artefatos + esqueleto do core) |
| `diario-de-obras` | Registrar planos/tíquetes, mudar status, condensar histórico |
| `integrar-poc` | POC validada pelo cliente → plugin (pipeline de 5 passos) |
| `guardrails-check` | Gate de qualidade ao final de toda tarefa (piso completo só em Tier 3 — sprint/alto raio) |
| `handover` | Encerrar tarefa e preparar troca de contexto limpa (com trava de contexto) |
| `audit-sweep` | Pré-varredura mecânica antes de qualquer auditor (greps → `docs/audits/SWEEP_*.md`) |

## Ciclo típico

`bootstrap-pantonic` (planner) → tarefas no diário → para cada tarefa, em contexto limpo:
executor → `guardrails-check` → `handover` → usuário limpa contexto e invoca a próxima.
Novas funcionalidades entram por `integrar-poc`.
