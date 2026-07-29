# BM-18: promptfoo/promptfoo

## D1 — Identidade e escopo
CLI e biblioteca para avaliar LLM apps e fazer red-teaming de segurança. Problema: eliminar tentativa-e-erro no desenvolvimento de IA. Público: desenvolvedores com apps LLM em produção que precisam aumentar confiabilidade e segurança antes de deploy.
https://raw.githubusercontent.com/promptfoo/promptfoo/HEAD/README.md

## D2 — Vitalidade
23.715 stars | pushed_at 2026-07-29T01:30:49Z | Licença MIT | Ativo.
https://docs/benchmark/_CORPUS.md (linha 66)

## D3 — Ciclo de vida do trabalho
Fases: feature-branch → lint/format → sync com main → push → PR → CI → code-review → merge. Não há gates explícitos nomeados; CI roda em paralelo com review.
https://raw.githubusercontent.com/promptfoo/promptfoo/HEAD/docs/agents/git-workflow.md

## D4 — Papéis e modelo por fase
Papéis implícitos em AGENTS.md: reviser (code review), committer (git), tester (CI), não há função nomeada de "product owner" ou "prioritizer". Modelo por fase: não explícito. Sincronização com main é responsabilidade de cada contributor, não centralizada.
https://raw.githubusercontent.com/promptfoo/promptfoo/HEAD/AGENTS.md

## D5 — Unidade de trabalho e rastreabilidade
NÃO ENCONTRADO

## D6 — Contexto e custo
NÃO ENCONTRADO

## D7 — Memória e estado persistente
NÃO ENCONTRADO

## D8 — Qualidade e testes
Vitest (framework moderno). Gates: Biome lint, TypeScript noEmit, test:coverage:ratchet (piso de cobertura), depcheck (deps não-usadas), test:smoke, test:integration. CI/CD valida em paralelo.
https://raw.githubusercontent.com/promptfoo/promptfoo/HEAD/package.json

## D9 — Guardrails e enforcement
NÃO ENCONTRADO

## D10 — Distribuição e versionamento do próprio framework
Semantic versioning (MAJOR.MINOR.PATCH, v0.121.19 em 2026-07-14). Cadência: 1-3 dias entre releases. Auto-gerado via changelog convencional; não há changelog manualmente editado.
https://raw.githubusercontent.com/promptfoo/promptfoo/HEAD/CHANGELOG.md

## D11 — Extensibilidade
Extension Hooks em 4 pontos: beforeAll, afterAll, beforeEach, afterEach. Configurados em promptfooconfig.yaml com referência a arquivo .js ou .py: `file://caminho:nomeFuncao`. Permite integração custom.
https://raw.githubusercontent.com/promptfoo/promptfoo/HEAD/examples/config-extension-api/README.md

## D12 — Observabilidade e métricas
Logging estruturado com sanitização de segredos (tokens, API keys → [REDACTED]). Não há métricas de consumo ou série histórica documentada.
https://raw.githubusercontent.com/promptfoo/promptfoo/HEAD/docs/agents/logging.md

## D13 — Segurança e permissões
SQL injection prevention via Drizzle parametrizadas e buildSafeJsonPath. Sanitização de segredos em logs. Não há documentação de sandbox, allowlist ou autenticação em camada de aplicação.
https://raw.githubusercontent.com/promptfoo/promptfoo/HEAD/docs/agents/database-security.md

## D14 — Onboarding humano e documentação
README único. Documentação distribuída em docs/agents/ (6 arquivos: AGENTS, git-workflow, pr-conventions, logging, database-security, dependency-management). Diretórios de exemplos: examples/. Planos e arquitetura em docs/plans/ e docs/architecture/.
https://raw.githubusercontent.com/promptfoo/promptfoo/HEAD/README.md

## D15 — Multi-projeto, multi-repo e equipe
NÃO ENCONTRADO

## D16 — Interação com o humano
Aprovação obrigatória em PR: "NEVER commit/merge/push directly to main". Code review síncronaé esperado. Convenções: Conventional Commits, escopo redteam obrigatório se mudança é redteam. Atribuição a Claude proibida.
https://raw.githubusercontent.com/promptfoo/promptfoo/HEAD/docs/agents/pr-conventions.md

---

## Práticas transplantáveis

1. **Extension Hooks em 4 pontos de ciclo** — beforeAll/afterAll/beforeEach/afterEach, configurável em YAML, suporta .js e .py. Custo: ~3-5 dias (design de hook points, handlers, testes).

2. **Ratchet de cobertura obrigatório** — test:coverage:ratchet em gate CI, não permite regressão. Custo: ~2 dias (setup, CI integration, documentação).

3. **Sanitização automática de segredos em logs** — campo-a-campo para tokens/keys/passwords → [REDACTED]. Custo: ~1-2 dias (lista de padrões, filtro, testes).

## Anti-práticas

1. **Changelog não editável — auto-gerado puro** — sem captura de contexto/decisão que mudança convencional não suporta. Risco: relatórios de releases sem narrativa.

2. **Papéis implícitos, nunca nomeados** — AGENTS.md lista diretrizes mas não nomeia "prioritizer", "architect", "secops". Risco: ambiguidade em delegação.

3. **Sem série histórica de métricas** — logging sanitiza mas não agrega cobertura/performance. Risco: regressão silenciosa, sem alerta automático.

## Dimensões fora da grade

- **Arquitetura em camadas com ratchet de DAG**: 11 camadas (facade, contracts, core, node, providers, redteam, view-server, cli, app) com grafo de dependência acíclico verificável via `npm run architecture:check`. Restrição forte: nenhum módulo interno importa src/index.ts. Não cabe em D3/D4 (é arquitetura física, não ciclo de trabalho).

- **Planos de refatoração explícitos** — docs/plans/2026-01-08-plugins-state-management-refactor.md documentam mudança planejada. Não é parte de D3 (ciclo corrente).
