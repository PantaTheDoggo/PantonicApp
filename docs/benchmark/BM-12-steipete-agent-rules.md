# BM-12: steipete/agent-rules

## D1 — Identidade e escopo

Framework declarativo em duas camadas: **global-rules** (MCPs, setup, sincronização) + **project-rules** (automação: commit, PR review, bug fix). Resolve: consistência de doutrina em equipes com Cursor/Claude Code. Para: times que reproduzem padrões multi-projeto. Status: descontinuado mid-2026 ("old stuff I used mid 2025"), redirecionado para `steipete/agent-scripts`.

**Fonte:** https://raw.githubusercontent.com/steipete/agent-rules/HEAD/README.md

---

## D2 — Vitalidade

Stars: 5692 | Último push: 2026-05-03T17:06:19Z (~2,5 meses sem atividade) | Licença: MIT | Nº de contribuidores: NÃO ENCONTRADO. Fonte: `docs/benchmark/_CORPUS.md` linha 59.

**Fonte:** docs/benchmark/_CORPUS.md linha 59

---

## D3 — Ciclo de vida do trabalho

5 fases lineares: (1) Estratégia inicial — requisito, componentes, dependências; (2) Avaliação de abordagens — desempenho, manutenibilidade, escalabilidade; (3) Análise de compensações — benefícios vs. simplicidade; (4) Implementação — subtarefas, teste incremental; (5) Práticas — TDD, funções focadas, tratamento de casos extremos. Artefatos: código, testes, docs. Sem gates formais.

**Fonte:** https://raw.githubusercontent.com/steipete/agent-rules/HEAD/project-rules/implement-task.mdc

---

## D4 — Papéis e modelo por fase

6 papéis em revisão: PM, Dev, QA, Segurança, DevOps, Designer. Sem modelo dinâmico por fase; genérico.

**Fonte:** https://raw.githubusercontent.com/steipete/agent-rules/HEAD/project-rules/pr-review.mdc

## D5 — Unidade de trabalho e rastreabilidade

Tarefa = 5 fases (D3). Rastreabilidade: requisito (natural language) → Git → `npm run check`. Sem matriz de cobertura requisito-teste-código.

**Fonte:** https://raw.githubusercontent.com/steipete/agent-rules/HEAD/project-rules/implement-task.mdc, check.mdc

## D6 — Contexto e custo

Orçamento: 200k tokens. Estratégia: priorização (README → CLAUDE.md → tree) para reduzir consultas. Sem rate limiting, turnos máximos, ou limite monetário.

**Fonte:** https://raw.githubusercontent.com/steipete/agent-rules/HEAD/project-rules/context-prime.mdc

## D7 — Memória e estado persistente

Global: `~/.claude/` (rules compartilhadas, MCPs). Local: `.claude/` (project-specific). Logs: `/tmp/[MCP_SERVER_NAME]_start_debug.log`. Sem cache persistente além do filesystem.

**Fonte:** https://raw.githubusercontent.com/steipete/agent-rules/HEAD/install-project-rules.sh, mcp-inspector-debugging.mdc

---

## D8 — Qualidade e testes

Gatting: linting, type-check, unit tests, security scan, formatting, build verify. Ciclo: executar → analisar → corrigir (críticos primeiro) → reexecutar. TDD recomendado. Sem piso histórico de regressão.

**Fonte:** https://raw.githubusercontent.com/steipete/agent-rules/HEAD/project-rules/check.mdc, implement-task.mdc

## D9 — Guardrails e enforcement

~80% texto (`.mdc` markdown referenciável) + ~20% código (bash scripts: install, setup-mcps, mcp-sync). Sem validação em commit/CI.

**Fonte:** https://raw.githubusercontent.com/steipete/agent-rules/HEAD/install-project-rules.sh, global-rules/setup-mcps.sh

## D10 — Distribuição e versionamento do próprio framework

Instalação: `install-project-rules.sh` cria ref `@$(pwd)/project-rules` em `~/.claude/CLAUDE.md`. Atualização: dinâmica (ref, não cópia). Versionamento: nenhum semântico, nenhum changelog.

**Fonte:** https://raw.githubusercontent.com/steipete/agent-rules/HEAD/install-project-rules.sh

---

## D11 — Extensibilidade

Duplo: (1) **MCPs** via `setup-mcps.sh` (Peekaboo, Playwright, GitHub); (2) **Project rules** como slash commands em `.claude/commands/`, padrão declarativo 5-passos. Sem restrição de fork.

**Fonte:** https://raw.githubusercontent.com/steipete/agent-rules/HEAD/global-rules/setup-mcps.sh, project-rules/create-command.mdc

## D12 — Observabilidade e métricas

3 camadas: UI (Playwright) + processos (iTerm) + logs (`/tmp/[MCP]_start_debug.log`, `LOG_FILE_PATH`, stderr). Sem série histórica, telemetria, ou alertas.

**Fonte:** https://raw.githubusercontent.com/steipete/agent-rules/HEAD/project-rules/mcp-inspector-debugging.mdc

---

## D13 — Segurança e permissões

Validação: `setup-mcps.sh` verifica chaves de API (OpenAI, GitHub, Firecrawl) antes de install. Sem sandbox, allowlist, ou gatting de ações destrutivas.

**Fonte:** https://raw.githubusercontent.com/steipete/agent-rules/HEAD/global-rules/setup-mcps.sh

## D14 — Onboarding humano e documentação

Docs: `appkit.md`, `swiftui.md`, `swift-testing-api.mdc`, `mcp-best-practices.mdc` + 10+. Guias: `cursor-rules-meta-guide.mdc`, `create-command.mdc`. **Risco:** README desatualizado, redireciona para `steipete/agent-scripts`.

**Fonte:** https://raw.githubusercontent.com/steipete/agent-rules/HEAD/README.md

## D15 — Multi-projeto, multi-repo e equipe

Compartilhamento via ref global `~/.claude/CLAUDE.md`. Sem sincronização explícita entre equipes, sem registro de consumidores, sem governança de versões.

**Fonte:** https://raw.githubusercontent.com/steipete/agent-rules/HEAD/install-project-rules.sh

---

## D16 — Interação com o humano

Humano obrigatório em: revisão (6 papéis, feedback antes de aprove), design (trade-offs explícitos), testes (análise manual). Sem aprovação mecânica (ex.: merge automático). Sempre revisão esperada.

**Fonte:** https://raw.githubusercontent.com/steipete/agent-rules/HEAD/project-rules/pr-review.mdc

---

## Rodapé

### 3 Práticas transplantáveis

1. **Camadas texto+código** (guardrails em markdown + validação bash) — Custo: **baixo (~1-2d)**. Acelera onboarding: regras em natural language sem lógica procedural obrigatória.

2. **Referência dinâmica `@$(pwd)/path`** — Custo: **muito baixo (~2h)**. Atualizações automáticas sem redeploy; consumidores sempre sincronizados.

3. **Matriz 6-papéis em revisão** — Custo: **médio (~3-5d)**. Trade-offs explícitos antes de merge; reduz regressões.

### 3 Anti-práticas

1. **README desatualizado + redirecionamento** — Confunde novo usuário sobre qual repo usar. Solução: consolidar ou marcar "archived/deprecated" com data.

2. **Sem versionamento semântico nem changelog** — Consumidores não sabem breaking changes. Refs dinâmicas (D10) = atualizações silenciosas. Solução: `CHANGELOG.md`, tags git, arquivo VERSION.

3. **Sem governança de consumidores** — Impossível medir adoção, coordenar breaking changes, suportar retrocompatibilidade. Solução: `docs/ADOPTION.md` com lista, versão, último sync.

### Dimensões fora da grade

**Portabilidade IDE:** Acoplado a Cursor/Claude Code (`.claude/`, CLAUDE.md). MCPs funcionam em VS Code/Windsurf via JSON específico, mas requer conversão manual — sem "compilador" automático. Risco em migração multi-IDE.

**Deprecação de rules:** Sem processo de sunsetting para project-rules. Mudanças de sintaxe (ex.: `/commit-v1` → `/commit-v2`) sem período de transição causam choque em bases grandes. Seria relevante "sunsetting policy": rules deprecated permanecem N versões menores antes de remoção.
