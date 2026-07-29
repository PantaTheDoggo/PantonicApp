# BM-20 — PRPs (Product Requirement Prompts) — `Wirasm/prp`
**Dados:** 2226 stars | Push: 2026-07-27T13:48:33Z | MIT | Wirasm | Árvore: `_trees/wirasm-prp.txt` (269 arquivos)

## D1 — Identidade e escopo
Toolkit de engenharia ágil orquestrador: AI-assisted feature dev end-to-end com Claude Code. Combina PRD + codebase intelligence + validation loops. Resolve: requisitos tradicionais faltam detalhe técnico para AI gerar código 1ª pass. Para: equipes escalar AI-dev sem iteração manual. Escopo: planning (PRD→plan), implement (task×validation), PR+review auto, orchestration multiworkstream.
Fonte: https://raw.githubusercontent.com/Wirasm/PRPs-agentic-eng/HEAD/README.md

## D2 — Vitalidade
Stars: 2226 | Último push: 2026-07-27T13:48:33Z | Licença: MIT | Contribuidores: NÃO ENCONTRADO
Fonte: Corpus cached (`_CORPUS.md` linha 68)

## D3 — Ciclo de vida do trabalho
**prp-plan** (6 fases): DETECT→PARSE→EXPLORE→RESEARCH→DESIGN→ARCHITECT→GENERATE. Artifacts: `.plan.md` (file:line + validation cmds).
**prp-implement** (6 fases): DETECT→LOAD→PREPARE→EXECUTE→VALIDATE→REPORT. Artifacts: implementations + reports + updated PRD.
**prp-loop**: plan→implement→pr→review→fix (autonomous, max iterations bound). Artifacts: `.state.json` + run files.
**prp-orchestrate**: multi-agent, worktrees isolados, event-driven steering, run file + event log + standing decisions.
Gates: ambiguity, pattern not found, version mismatch, architecture conflict.
Fonte: https://raw.githubusercontent.com/Wirasm/PRPs-agentic-eng/HEAD/.claude/skills/prp-plan/SKILL.md

## D4 — Papéis e modelo por fase
Agentes: prp-code-reviewer (report), prp-codebase-explorer, prp-codebase-analyst, prp-meta-skill (workflow+gates), prp-orchestrate (Claude-only), prp-research-team (report, Claude-only).
Coordenação: shared lib `.claude/skills/` + unified store `~/.prp/<key>/`.
Modelo explícito: 5 workflows (`/prp-prd`, `/prp-plan`, `/prp-implement`, `/prp-loop`, `/prp-issue`) por tipo tarefa. Advisory agents = report-only; workflow agents = loop until green.
Fonte: https://raw.githubusercontent.com/Wirasm/PRPs-agentic-eng/HEAD/AGENTS.md

## D5 — Unidade de trabalho e rastreabilidade
Task = step do plano, executável atomicamente. Tem: file:line, descrição, validation cmd, artefato esperado. Rastreamento: plan → file:line → code → immediate type-check → full validation (types/lint/tests/build).
Fonte: https://raw.githubusercontent.com/Wirasm/PRPs-agentic-eng/HEAD/.claude/skills/prp-plan/SKILL.md (Phase 6)

## D6 — Contexto e custo
NÃO ENCONTRADO — sem orçamento/limite explícito de contexto (tokens), turnos ou dinheiro.

## D7 — Memória e estado persistente
**prp-loop**: estado em `~/.prp/<key>/state/prp-loop.state.json` (JSON); halts com state preservado se max iterations/cycles atingido ou sem commit novo após fix.
**prp-orchestrate**: run file em `$PRP_DIR/orchestration/<run-id>.md` (YYYY-MM-DD-<slug>); reload+reconcile vs git/gh em resume (`--resume`); nunca committed.
**Shared**: plans+reports em `~/.prp/<key>/`, cross-worktree. **Skill lib**: `.claude/skills/` canonical.
Fonte: https://raw.githubusercontent.com/Wirasm/PRPs-agentic-eng/HEAD/.claude/skills/prp-loop/SKILL.md

## D8 — Qualidade e testes
TDD: NÃO ENCONTRADO. Gates: prp-plan (6 checkpoints) + prp-meta-skill (checklist→reviewer→test). Regressão/piso: NÃO ENCONTRADO. prp-implement: per-task type-check (imediato) + full validation (types/lint/tests/build); fail-fast.
Fonte: https://raw.githubusercontent.com/Wirasm/PRPs-agentic-eng/HEAD/.claude/skills/prp-meta-skill/SKILL.md

## D9 — Guardrails e enforcement
Regras executáveis: ~60% código (`prp_loop.py`, `prp_runner.py`, `.claude/skills/prp-meta-skill/references/validation.md`), ~40% checklist. Meta-skill enforça: frontmatter compliance, progressive disclosure, no-duplication, behavior-preservation, mandatory-read. Sequência: checklist→reviewer agent→trigger test.
Fonte: https://raw.githubusercontent.com/Wirasm/PRPs-agentic-eng/HEAD/.claude/skills/prp-meta-skill/SKILL.md

## D10 — Distribuição e versionamento do próprio framework
Plugin marketplace: `/plugin marketplace add Wirasm/PRPs-agentic-eng` → `/plugin install prp-core@prp-marketplace`. Versioning: v0.1.0 (pyproject.toml). Updates: manual (uninstall+reinstall). Restart Claude Code obrigatório. Team: `.claude/settings.json` + enabledPlugins list.
Fonte: https://raw.githubusercontent.com/Wirasm/PRPs-agentic-eng/HEAD/plugins/prp-core/README.md

## D11 — Extensibilidade
Plugins: GitHub marketplace (`.claude-plugin/marketplace.json`). Skills: via prp-meta-skill (SKILL.md spine + references + templates). Hooks: `prp-research-team-stop.sh` (webhook). Agentes: 10 em `.claude/agents/` (editable Markdown). Modelo: fork+adapt, maintainer explicitamente picky (load-bearing deps).
Fonte: https://raw.githubusercontent.com/Wirasm/PRPs-agentic-eng/HEAD/CONTRIBUTING.md

## D12 — Observabilidade e métricas
State file: `prp-loop.state.json` (progresso inspecionável). Run files: event log + standing decisions (who/what/when). Sentinels: "VALIDATION: GREEN/RED" ou exit 0/non-zero. Série histórica, telemetria, métricas agregadas: NÃO ENCONTRADO.
Fonte: https://raw.githubusercontent.com/Wirasm/PRPs-agentic-eng/HEAD/.claude/skills/prp-loop/SKILL.md

## D13 — Segurança e permissões
Sandbox: NÃO ENCONTRADO. Allowlist: NÃO ENCONTRADO. Secrets: NÃO ENCONTRADO. Destrutivas: prp-orchestrate+prp-loop fazem merges; gate humano existe (pre-merge explicit approval), mas mecanismo de secret/permission NÃO ENCONTRADO.

## D14 — Onboarding humano e documentação
Mínimo leitura decidir: 2 min (README-for-DUMMIES: "what is PRP?"→Setup→"That's It" 5 patterns). Mínimo começar: install+pick 1 workflow+run 1 skill. Docs: layered (quickstart→conceptual→reference→advanced), "context is king". Estrutura: README, README-for-DUMMIES, CONTRIBUTING, AGENTS.md, skills em `.claude/skills/` com references+templates.
Fonte: https://raw.githubusercontent.com/Wirasm/PRPs-agentic-eng/HEAD/README-for-DUMMIES.md

## D15 — Multi-projeto, multi-repo e equipe
`~/.prp/` = shared artifact store cross-project (key=identifier). prp-orchestrate: multiworkstream com worktrees isolados; disjoint file sets rodam concurrent (limit 3). Standing Decisions: covered→auto (record `auto`); out-of-scope→escalate. Event-driven notifications (agents report; orchestrator verify vs authoritative signals antes avançar queue).
Fonte: https://raw.githubusercontent.com/Wirasm/PRPs-agentic-eng/HEAD/.claude/skills/prp-orchestrate/SKILL.md

## D16 — Interação com o humano
**Plan gate**: apresentar decomposição+standing decisions; aprovação batch. **PR/landing**: check Standing Decisions; covered→auto (record `auto`); uncovered→escalate (2-3 linhas). **Pre-merge**: nunca sem explicit approval naquele run. **Blocked agent**: escalação imediata. **Nunca auto**: merge sem approval; decisão fora scope.
Fonte: https://raw.githubusercontent.com/Wirasm/PRPs-agentic-eng/HEAD/.claude/skills/prp-orchestrate/SKILL.md

---
## Rodapé: Práticas Transplantáveis
1. **Plano como fonte + validation cmds (file:line + exit 0).** Custo: Médio (1-2 sem). Templates documentados; adotante serializa padrões+cmds por stack.
2. **Enforcement via meta-skill (checklist+reviewer+test).** Custo: Alto (1-2 mês). Requer validation criteria; skill refatora auditorias team.
3. **Multi-workstream orchestration + Standing Decisions (auto-decide covered, escalate out-of-scope).** Custo: Médio (2-3 sem). Run file+log simples; pesado é treinar "covered vs escalate".

## Rodapé: Anti-Práticas
1. **Lazy-load always-needed formats (references esquecidas).** Motivo: agent pode silenciosamente esquecer ler críticas. Meta-skill mitiga com "mandatory-read", mas tensão intrínseca.
2. **Commit run files por workstreams.** Motivo: live coordination quebra se committed; destroi idempotência+reconcile em resume. Framework proíbe, mas doc não destaca motivo com força.
3. **Sem série histórica validação/regressão.** Motivo: cada run recomeça zero; sucessos prévios não criam "piso" anti-regressão. Observabilidade p/ degradação first-pass success NÃO ENCONTRADO.

## Dimensões fora da grade
**Orçamento/contexto:** Framework não declara/enforça teto de contexto (tokens), turnos ou dinheiro. Cada skill roda "até completar" — relevante p/ orgs com limites LLM.
**Meta-rule de validação:** Cada skill tem gate logic próprio (prp-plan 6 checkpoints, prp-implement 6 fases). Sem agregação uniforme. Design choice p/ framework-de-frameworks, mas criou complexidade de auditoria cruzada.

---
**Coleta:** 12 requisições conteúdo. Relatório: 160 linhas.
