# BM-11: coleam00/context-engineering-intro

## D1 — Identidade e escopo
Framework de Context Engineering: estruturação de documentação, exemplos e validações para assistentes de IA executarem tarefas complexas. Princípio: "Context is King" (10x prompt engineering, 100x vibe coding). Resolve falhas por insuficiência de contexto estruturado. Fonte: https://raw.githubusercontent.com/coleam00/context-engineering-intro/HEAD/README.md

## D2 — Vitalidade
13750 stars; MIT. Último push 2026-03-16 (~4 meses). Confirmado BM-11, trilha C. Fonte: docs/benchmark/_CORPUS.md linha 57

## D3 — Ciclo de vida do trabalho
Artefato central: Product Requirements Plan (PRP). Fases: Definição → Exemplificação → Documentação → Considerações. PRP contém seções (Name/Goal/Why/What/Success Criteria/All Needed Context/Implementation Blueprint/Validation Loop/Anti-Patterns) com checkboxes e validação cascata (Level 1: sintaxe, Level 2: unit tests, Level 3: integração). Fonte: https://raw.githubusercontent.com/coleam00/context-engineering-intro/HEAD/PRPs/EXAMPLE_multi_agent_prp.md

## D4 — Papéis e modelo por fase
Agent Claude (executor), Desenvolvedor (inicia tarefas), Sistema (deps). Em use-cases: 6 subagentes especializados (planner, prompt-engineer, tool-integrator, dependency-manager, validator, main executor). Fases: Phase 0 (clarificação) → Phase 1 (requisitos) → Phase 2 (paralelo) → Phase 3 (impl) → Phase 4 (validação) → Phase 5 (docs). Fonte: https://raw.githubusercontent.com/coleam00/context-engineering-intro/HEAD/use-cases/agent-factory-with-subagents/CLAUDE.md

## D5 — Unidade de trabalho e rastreabilidade
PRP é unidade de trabalho. Rastreamento: requisito (seção "What"/"Success Criteria") → exemplos (pasta examples/, "All Needed Context") → teste (Validation Loop com pytest). Checkboxes marcam progresso. Transição "todo" → "doing" → "done" via Archon (optional). Fonte: https://raw.githubusercontent.com/coleam00/context-engineering-intro/HEAD/PRPs/EXAMPLE_multi_agent_prp.md

## D6 — Contexto e custo
NÃO ENCONTRADO

## D7 — Memória e estado persistente
NÃO ENCONTRADO

## D8 — Qualidade e testes
TDD obrigatório (Pytest, PEP8, type hints, black). Validação cascata (Level 1: linting, Level 2: unit, Level 3: integração). Cobertura ≥80% em use-cases. Sem série histórica regressão. Fonte: https://raw.githubusercontent.com/coleam00/context-engineering-intro/HEAD/CLAUDE.md

## D9 — Guardrails e enforcement
~60% checklist/workflow (PRP sections, Success Criteria), ~40% código (pytest, linting). Enforcement textual: "recognize agent factory request", "aguardar resposta explícita". Anti-patterns em texto: hardcodear API keys, ignorar testes. Allowlist técnico em settings.local.json (comandos: grep/ls/pytest/python; domínios: docs.anthropic.com, github.com). Fonte: https://raw.githubusercontent.com/coleam00/context-engineering-intro/HEAD/.claude/settings.local.json

## D10 — Distribuição e versionamento do próprio framework
Framework local sem pacote gerenciado. Instalação via "Open Claude Code in this directory". Sem SemVer, release tags, ou comando de versão. Update via pull git manual. Fonte: https://raw.githubusercontent.com/coleam00/context-engineering-intro/HEAD/use-cases/agent-factory-with-subagents/README.md

## D11 — Extensibilidade
PRPs reutilizáveis via templates (prp_base.md), copy_template.py gera novos PRPs. Modular (agent.py/tools.py/prompts.py/dependencies.py). Customização via novos .claude/commands/*.md. Sem hooks/plugins formais. Fonte: docs/benchmark/_trees/coleam00-context-engineering-intro.txt (linhas 1-2, 12, 30-31, 43-44, 236-242)

## D12 — Observabilidade e métricas
Archon project tracking (optional): "todo" → "doing" → "done". Métricas mencionadas ("Tempo <15 min", "100% requisitos testados") mas não rastreadas em série. Logging "informativo mas não verboso", sem estrutura. Fonte: https://raw.githubusercontent.com/coleam00/context-engineering-intro/HEAD/use-cases/agent-factory-with-subagents/CLAUDE.md

## D13 — Segurança e permissões
Allowlist em settings.local.json (comandos: grep/ls/source/find/mv/mkdir/tree/ruff/touch/cat/pytest/python; domínios: docs.anthropic.com, github.com). Sandbox via Claude Code. Anti-pattern "hardcodear chaves de API" mencionado mas não bloqueado. .env.example em use-cases, sem validação. Permissões iguais entre papéis. Fonte: https://raw.githubusercontent.com/coleam00/context-engineering-intro/HEAD/.claude/settings.local.json

## D14 — Onboarding humano e documentação
Estrutura: CLAUDE.md (~200 linhas), INITIAL.md, INITIAL_EXAMPLE.md, examples/, PRPs/templates/, .claude/commands/. Decidir: 5–10 min (README + CLAUDE.md). Começar: 15–30 min (copiar repo, preencher INITIAL.md, /execute-prp). Consistência em use-cases reduz fricção. Fonte: https://raw.githubusercontent.com/coleam00/context-engineering-intro/HEAD/README.md

## D15 — Multi-projeto, multi-repo e equipe
6 use-cases (agent-factory, mcp-server, pydantic-ai, ai-coding-wisc, ai-coding-workflows, template-generator). Doutrina compartilhada: .claude/, template PRP, validação 3-níveis. Sem sincronização explícita backlog — templates/docs são mecanismo de compartilhamento. Extensão a múltiplos repos via cópia .claude/ e adaptação templates. Fonte: https://raw.githubusercontent.com/coleam00/context-engineering-intro/HEAD/use-cases/agent-factory-with-subagents/README.md

## D16 — Interação com o humano
Phase 0: "aguardar respostas explícitas antes de prosseguir" (human-in-loop obrigatório). Validação: checkboxes em "Success Criteria"/"Final Validation Checklist" requerem revisão humana. Nunca automático: geração PRP, aprovação mudanças, transição fase. Fluxo: humano descreve requisito → /generate-prp → /execute-prp → valida → marca checkboxes. Fonte: https://raw.githubusercontent.com/coleam00/context-engineering-intro/HEAD/.claude/commands/execute-prp.md

---

## Práticas transplantáveis

**1. PRP como artefato de especificação estruturada** (Custo: médio ~10–20h). Seções prescritas (What/Why/Success/Validation/Anti-Patterns) reduzem falhas IA-humano, rastreiam requisito→teste.

**2. Validação em cascata (sintaxe → unit → integração)** (Custo: baixo ~5–10h). Reduz regressão, dá confiança incremental.

**3. Estrutura modular de subagentes (5–6 especializados)** (Custo: alto ~30–50h primeira aplicação). Reduz contexto/agente, facilita paralelização, isola erros.

## Anti-práticas

**1. PRP genérico sem templates especializados.** Redundância, mudanças não propagam. Melhor: herança hierárquica (markdown includes, sobreposição explícita).

**2. Enforcement apenas textual de regras críticas.** CLAUDE.md pode ser ignorado. Melhor: checklist permissões (settings.local.json) ou hook pré-execução validado em código.

**3. Falta de observabilidade/série histórica.** Métricas mencionadas mas não rastreadas. Melhor: PRP gera relatório automático duração/testes/checkpoints, agregação em dashboard.

## Dimensões fora da grade

Nenhuma. Framework atua em design de trabalho (especificação, validação, rastreamento, papéis). Escala (multi-tenancy, quotas API), compliance (auditoria), performance sob carga não abordados — apropriado para template local, não plataforma produção.
