# BM-15: wshobson/agents

## D1 — Identidade e escopo
Marketplace de 94 plugins (90 local + 4 externos), 203 agentes, 175 skills, 109 comandos reutilizáveis para workflows com IA. Evita reimplementação de arquitetura, segurança, testes, infraestrutura. Projetos: full-stack, ops, ML/IA, testes, documentação, incidentes.
https://raw.githubusercontent.com/wshobson/agents/HEAD/README.md

## D2 — Vitalidade
38344 stars. Último push: 2026-07-22T15:32:23Z (7 dias). Licença: MIT. Corpus: `docs/benchmark/_CORPUS.md` linha 63, "atividade recente alta".

## D3 — Ciclo de vida do trabalho
Três fases: Planning (Sonnet agents, raciocínio complexo) → Execution (Haiku agents, tarefas determinísticas) → Review (Sonnet, validação). Artefatos: scaffolding, endpoints, testes, código, Terraform, K8s, audit reports, C4 diagrams, API specs, observabilidade.
https://raw.githubusercontent.com/wshobson/agents/HEAD/docs/architecture.md

## D4 — Papéis e modelo por fase
Papéis: Plugin (unidade modular), Skill (capacidade reutilizável), Agent (subagent definido), Command (prompt com frontmatter). Modelo **por harness, não por fase**: 5 plataformas (Claude Code, Codex, Cursor, OpenCode, Gemini CLI), cada uma com constraints diferentes. Adapter automático mapeia arquitetura canônica para cada target.
https://raw.githubusercontent.com/wshobson/agents/HEAD/AGENTS.md (genérico), https://raw.githubusercontent.com/wshobson/agents/HEAD/docs/harnesses.md

## D5 — Unidade de trabalho e rastreabilidade
Skill = `SKILL.md` (≤8 KB) + `references/` opcional. Agent = `agents/<name>.md`. Command = `commands/<name>.md`. Frontmatter obrigatório (name, description, triggers "Use when…"). Marketplace.json cataloga tudo. **Sem rastro requisito→código→teste** documentado; eval valida artefatos gerados, não trace.
https://raw.githubusercontent.com/wshobson/agents/HEAD/docs/authoring.md

## D6 — Contexto e custo
**NÃO ENCONTRADO**. Nenhuma documentação sobre limites de contexto, turnos, ou orçamento.

## D7 — Memória e estado persistente
Marketplace registries (marketplace.json) vivem em raiz do repo, referenciam plugins locais via `./plugins/` ou git-subdir remoto. Estado do framework registrado em JSON; artefatos gerados (.claude-plugin/, harness-specific outputs) são gitignored. Makefile regenera registries via `make generate-all` antes de commit.
https://raw.githubusercontent.com/wshobson/agents/HEAD/.github/workflows/validate.yml

## D8 — Qualidade e testes
Framework **plugin-eval** com 3 camadas: (1) Static Analysis (~2s, determinístico), (2) LLM Judge (~30s, rubric ancorado), (3) Monte Carlo (~2-5min, 50-100 runs). Regressão via bootstrap confidence intervals (1000 resample). Anti-pattern detection (11 categorias, penalidade por severidade). Exit code 1 se < threshold. Pytest com pytest-asyncio. Unit + integration + E2E contra corpora reais.
https://raw.githubusercontent.com/wshobson/agents/HEAD/docs/plugin-eval.md

## D9 — Guardrails e enforcement
**Executable rules-as-code**: JSON struct validation, agent name collision detection, artifact drift check (regenera, falha se diferente). Author_association gate (só owners/members/collaborators). Tool allowlist (gh + git restritos a subcomandos seguros; sem push --force, reset --hard, branch -D). Validação automática bloqueia merge.
https://raw.githubusercontent.com/wshobson/agents/HEAD/.github/workflows/claude.yml, https://raw.githubusercontent.com/wshobson/agents/HEAD/.github/workflows/validate.yml

## D10 — Distribuição e versionamento do próprio framework
Instalação: via Marketplace registries; consumidor aponta para local ou remoto. Atualização: pull repo, `make generate-all`, symlink artefatos via `make install-<harness>`. **Sem discovery explícita de versão** — consumidor segue raiz do repo. Versioning implícito em Git tags (não documentado em Makefile).
https://raw.githubusercontent.com/wshobson/agents/HEAD/Makefile, https://raw.githubusercontent.com/wshobson/agents/HEAD/docs/usage.md

## D11 — Extensibilidade
Plugins sem fork: (1) Skill novo em `plugins/<name>/skills/` com SKILL.md ≤8KB + references/. (2) Agent em `agents/<name>.md`. (3) Command em `commands/<name>.md`. (4) Assets em `skills/<name>/assets/` (templates, configs). Adapter auto-porta. Validação: `uv run plugin-eval score --depth quick` + `make generate-all` antes de commit.
https://raw.githubusercontent.com/wshobson/agents/HEAD/docs/authoring.md

## D12 — Observabilidade e métricas
**NÃO ENCONTRADO**. Nenhuma telemetria de consumo, série histórica, ou dashboard de qualidade documentado.

## D13 — Segurança e permissões
Sandbox: tool allowlist (git/gh subcomandos whitelisted). Permissões: author_association gate (só membros podem triggerar workflows). Sem ações destrutivas (push --force, reset, rm bloqueado). Secrets: não mencionado em workflows.
https://raw.githubusercontent.com/wshobson/agents/HEAD/.github/workflows/claude.yml

## D14 — Onboarding humano e documentação
Docs estruturados: architecture.md, authoring.md, plugin-eval.md, harnesses.md, usage.md. README breve ("map, not encyclopedia"). Usage.md cobre comandos e invocação post-instalação. **Instalação inicial (setup, prerequisitos) não documentada**.
https://raw.githubusercontent.com/wshobson/agents/HEAD/README.md, https://raw.githubusercontent.com/wshobson/agents/HEAD/docs/

## D15 — Multi-projeto, multi-repo e equipe
94 plugins em 1 repo (local) + 4 externos (git-subdir). 203 agentes, 175 skills compartilham marketplace registry. Orquestrações pré-configuradas multi-agent. Git-subdir permite equipes externas contribiurem plugins sem forking.
https://raw.githubusercontent.com/wshobson/agents/HEAD/docs/harnesses.md, https://raw.githubusercontent.com/wshobson/agents/HEAD/.github/workflows/validate.yml

## D16 — Interação com o humano
Code review gates (contrib via PR, templates: bug_report, feature_request, new_subagent, moderation_report). Validação automática + human approval (merge gate). Marketplace.json editável manualmente. Skill body e agent prompts revisáveis. Sem aprovação inline durante execução de agente.
https://raw.githubusercontent.com/wshobson/agents/HEAD/.github/CONTRIBUTING.md, https://raw.githubusercontent.com/wshobson/agents/HEAD/.github/ISSUE_TEMPLATE/

---

## Práticas transplantáveis

1. **Three-layer plugin evaluation** (static + LLM Judge + Monte Carlo bootstrap)  
   Custo: ~5 min CI; detecta regressão com rigor estatístico. Transplantável a qualquer corpus de agentes/skills.

2. **Executable rules-as-code in CI** (drift detection, name collisions, struct validation bloqueiam merge)  
   Custo: ~30s validação; previne inconsistência entre source + generated artifacts. Modelo reutilizável em marketplaces.

3. **Source-of-truth + platform adapter pattern** (1 canonical markdown → 5 harnesses via Makefile)  
   Custo: setup initial adapter; depois manutenção baixa. Escala a novos CLIs/IDEs sem duplicação.

## Anti-práticas

1. **Monte Carlo evals obrigatório em todo commit** — overhead ~5min por PR. Usar tier 1 (static) em CI fast-path, tier 3 (Monte Carlo) só em releases/nightly.

2. **make generate-all como gate obrigatório** — frágil se generated artifacts divergem. Melhor: versionar gerados no Git ou usar versionamento semântico explícito em Makefile.

3. **Pouca documentação de instalação/atualização consumidor** — marketplace.json é fonte de verdade interna; consumidor não tem guia "clone + instalar em [IDE/CLI]". Risco: onboarding friction para novos usuários.

## Dimensões fora da grade

**Marketplace como federação**: plugins externos via git-subdir (não monolítico), mas sem governance de versioning/SLA entre contrib. locais e remotas. Impacto: quebra de compatibilidade cruzada não detectada automaticamente.

**Adapter harness como único mecanismo de portabilidade**: sem fallback manual se adapter falha (ex.: nova feature em Claude Code que Codex não suporta). Risco: margem de degradação silenciosa.

