# BM-14: disler/claude-code-hooks-mastery

## D1 — Identidade e escopo

Framework que ensina a dominar hooks de Claude Code (CLI Anthropic) para controle determinístico sobre comportamento de agentes. Resolve o problema de imprevisibilidade: substitui decisão LLM por regras executáveis. Para engenheiros que querem sair de "vibe coding" para workflows auditáveis.

**Fonte:** https://raw.githubusercontent.com/disler/claude-code-hooks-mastery/HEAD/README.md

## D2 — Vitalidade

Stars: 3855 | Último push: 2026-03-04T18:16:25Z | Licença: NÃO ENCONTRADO (sem `license.spdx_id`) | Nº de contribuidores: NÃO ENCONTRADO. Fonte: `docs/benchmark/_CORPUS.md` linha 62.

## D3 — Ciclo de vida do trabalho

Workflow: User prompt → UserPromptSubmit hook (validação) → PreToolUse hook (aprovação/bloqueio) → Execução → PostToolUse hook (feedback) → Validação automática (ruff, type checking) → SubagentStart/Stop (orquestração) → SessionEnd (cleanup).

Artefatos: logs em JSON (pre_tool_use.json), validação em stdout.

**Fonte:** https://raw.githubusercontent.com/disler/claude-code-hooks-mastery/HEAD/ai_docs/claude_code_hooks_docs.md

## D4 — Papéis e modelo por fase

Papéis: Builder (executor focado, 1 tarefa por vez, sem spawnar agentes), Validator (checagem automática pós-execução), Meta-agent (gera agentes autonomamente).

Modelos por evento: diferem por lifecycle event type. Não há seleção explícita de modelo por fase confirmada.

**Fonte:** https://raw.githubusercontent.com/disler/claude-code-hooks-mastery/HEAD/.claude/agents/team/builder.md

## D5 — Unidade de trabalho e rastreabilidade

Unidade = uma tool call. Rastro: todos os invocações logadas em JSON (logs/pre_tool_use.json). Link explícito requisito→código não confirmado.

**Fonte:** https://raw.githubusercontent.com/disler/claude-code-hooks-mastery/HEAD/.claude/hooks/pre_tool_use.py

## D6 — Contexto e custo

NÃO ENCONTRADO

## D7 — Memória e estado persistente

logs/pre_tool_use.json (audit trail de todas as tool uses). Configuração em .claude/settings.json (global ou por projeto). Variáveis de ambiente via setup hook.

**Fonte:** https://raw.githubusercontent.com/disler/claude-code-hooks-mastery/HEAD/.claude/hooks/setup.py

## D8 — Qualidade e testes

Validação automática via PostToolUse: Ruff (linting), Type validator (type checking). TDD não confirmado. Piso de regressão não confirmado.

**Fonte:** https://raw.githubusercontent.com/disler/claude-code-hooks-mastery/HEAD/.claude/agents/team/builder.md

## D9 — Guardrails e enforcement

**Código executável (Python).** Duas regras em pre_tool_use.py:
1. Bloqueia `rm -rf` e variantes; rejeita caminhos perigosos (root, home, wildcards, parent refs).
2. Bloqueia acesso a `.env`; permite `.env.sample`.

Exit code 2 bloqueia tool call. Logging em JSON para auditoria.

**Fonte:** https://raw.githubusercontent.com/disler/claude-code-hooks-mastery/HEAD/.claude/hooks/pre_tool_use.py

## D10 — Distribuição e versionamento do próprio framework

Instalação via `.claude/` (estrutura padrão Claude Code). Configuração em settings.json. Sem versionamento semântico ou releases confirmados.

**Fonte:** https://raw.githubusercontent.com/disler/claude-code-hooks-mastery/HEAD/.claude/settings.json

## D11 — Extensibilidade

Hook system: adicionar matchers e commands em settings.json. Exemplos: 7 crypto agents (haiku/opus/sonnet), 8 output styles, 9 status lines. Sem SDK/plugin explícito confirmado.

**Fonte:** docs/benchmark/_trees/disler-claude-code-hooks-mastery.txt (131 arquivos)

## D12 — Observabilidade e métricas

JSON logging (pre_tool_use.json). Série histórica, dashboard ou métricas de qualidade não confirmados.

**Fonte:** https://raw.githubusercontent.com/disler/claude-code-hooks-mastery/HEAD/.claude/hooks/pre_tool_use.py

## D13 — Segurança e permissões

PreToolUse hook bloqueia: rm -rf, acesso .env. Sandbox não confirmado. Allowlist não confirmado.

**Fonte:** https://raw.githubusercontent.com/disler/claude-code-hooks-mastery/HEAD/.claude/hooks/pre_tool_use.py

## D14 — Onboarding humano e documentação

6 passos formais: settings → matchers → hook → save → verify → test. Documentação em ai_docs/: getting started, hooks docs, subagents docs.

**Fonte:** https://raw.githubusercontent.com/disler/claude-code-hooks-mastery/HEAD/ai_docs/claude_code_hooks_getting_started.md

## D15 — Multi-projeto, multi-repo e equipe

Builder/Validator pair pattern para team workflows. Meta-agent para geração autônoma. Mecanismo de compartilhamento cross-project não confirmado.

**Fonte:** https://raw.githubusercontent.com/disler/claude-code-hooks-mastery/HEAD/.claude/agents/team/builder.md

## D16 — Interação com o humano

SubagentStop hook valida conclusão antes de encerrar. PreToolUse requer aprovação implícita (exit 0/2). UserPromptSubmit permite injetar contexto. Workflow explícito de revisão humana não confirmado.

**Fonte:** https://raw.githubusercontent.com/disler/claude-code-hooks-mastery/HEAD/ai_docs/claude_code_hooks_docs.md

---

## Práticas transplantáveis

1. **Hook-based validation pipeline** — Bloqueia classes de erro antes de execução (ruff, type checking automáticos). *Custo estimado: ~2h setup + escrita de 1-2 scripts Python.*

2. **Builder/Validator agent pair** — Separa execução de oversight com papéis explícitos. *Custo: ~4h; requer definição clara de papéis.*

3. **Deterministic control via exit codes** — Substitui LLM decision making em pontos críticos (0 = permitir, 2 = bloquear). *Custo: trivial.*

## Anti-práticas

1. **Bloqueio baseado em string matching de comandos** (rm -rf). Frágil: bypass via `\rm`, aliases, ou splitting. Use allowlist + seccomp em produção.

2. **Múltiplas versões de status_line (9 no tree).** Fragmentação de manutenção. Versionamento semântico teria evitado.

3. **Crypto agents triplicados (haiku/opus/sonnet em paralelo).** DRY violation. Usar single agent com model selection logic interno.

## Dimensões fora da grade

- **Hook chaining e precedência:** ordem de execução de múltiplos hooks no mesmo evento não está clara.
- **Schema validation:** nenhuma validação de conformidade do próprio settings.json confirmada.
- **Rollback/recovery:** sem mecanismo de undo para hooks que bloquearam ações.
