# BM-08 — google-gemini/gemini-cli

## D1 — Identidade e escopo

Gemini CLI é um agente de IA de código aberto que integra o modelo Gemini do Google diretamente no terminal. Projecta-se como "ferramenta terminal-first designed for developers who live in the command line", democratizando acesso a IA avançada para fluxos de desenvolvimento. Resolve: análise de código, geração de aplicações multimodal (imagens/PDFs), debugging, automação operacional (PRs, rebase), revisão automatizada de código, e integração com GitHub. Trilha B (plataforma de IA com framework): modelagem de trabalho, composição de tarefas, integração com backends empresariais (Vertex AI) e padrões de extensibilidade.

Fonte: https://raw.githubusercontent.com/google-gemini/gemini-cli/HEAD/README.md

## D2 — Vitalidade

- **Stars:** 106.231
- **Último push:** 2026-07-29T01:29:18Z
- **Nº de contribuidores:** NÃO ENCONTRADO
- **Licença:** Apache-2.0

Fonte: docs/benchmark/_CORPUS.md (linha 54)

## D3 — Ciclo de vida do trabalho

Não há documentação explícita de fases de trabalho canônicas em D1..D16. O framework suporta: (1) **Plan mode** — planejamento estruturado com checkpoints de decisão; (2) **Session execution** — sessões persistidas localmente como transcritos; (3) **Memory inbox review** — aprovação manual de artefatos candidatos (skills, memory patches); (4) **Artifact promotion** — habilidades promovidas a `~/.gemini/skills/` (usuário) ou `.gemini/skills/` (projeto); (5) **Release cycle** — versionamento semântico com sufixos `-nightly` e `-preview`. Gates: aprovação obrigatória para memória/skills antes de persistência.

Fonte: https://raw.githubusercontent.com/google-gemini/gemini-cli/HEAD/docs/cli/auto-memory.md; docs/changelogs/latest.md

## D4 — Papéis e modelo por fase

**Agentes remotos (A2A):** Gemini CLI conecta a agentes remotos conformes via protocolo Agent-to-Agent; configuração via `.gemini/agents/*.md` em projeto ou `~/.gemini/agents/` global. Comandos: `/agents list`, `/agents enable`, `/agents disable`. Não há documentação de **orquestração explícita de papéis** entre agentes ou de atribuição de fases por tipo de agente. **Sub-agentes:** documentado em `docs/core/subagents.md` (árvore); mecanismo não detalhado em buscas. Modelo por fase: não explícito — configuração hierárquica global (`.gemini/config.yaml`) controla comportamentos por contexto (ex.: `pull_request_opened` com flags booleanas `help`, `summary`, `code_review`).

Fonte: https://raw.githubusercontent.com/google-gemini/gemini-cli/HEAD/docs/core/remote-agents.md; https://raw.githubusercontent.com/google-gemini/gemini-cli/HEAD/.gemini/config.yaml

## D5 — Unidade de trabalho e rastreabilidade

**Unidade de trabalho:** Não explícita. O sistema organiza trabalho em torno de **skills** (procedimentos reutilizáveis em `SKILL.md`), **commands** (invocações customizadas em `.gemini/commands/*.toml`), e **sessions** (transcritos persistidos localmente). Cada sessão gera transcrições—não há rastro requisito → código → teste documentado. **Skills** podem ser promovidas com `gemini skills` após aprovação via `/memory inbox`, sugerindo rastreamento de origem (draft → promoted), mas sem cadeia requisito-código explícita.

Fonte: https://raw.githubusercontent.com/google-gemini/gemini-cli/HEAD/docs/cli/auto-memory.md; docs/benchmark/_trees/google-gemini-gemini-cli.txt (`.gemini/skills/`, `.gemini/commands/`)

## D6 — Contexto e custo

**Limite de contexto:** Documentação menciona "context" via arquivo `docs/mermaid/context.mmd` (sem detalhes em busca). **Token caching:** `docs/cli/token-caching.md` existe (não buscado no orçamento). **Generation settings:** `docs/cli/generation-settings.md` existe — provavelmente controla limites de custo/contexto por modelo. **Quota público:** README menciona "60 requisições por minuto, 1.000 diárias para contas Google pessoais". Não há evidência de orçamento explícito em turnos ou em dinars no código; limites aplicam-se ao modelo (Gemini via API Google) e ao protocolo, não internamente ao framework.

Fonte: https://raw.githubusercontent.com/google-gemini/gemini-cli/HEAD/README.md; docs/benchmark/_trees/google-gemini-gemini-cli.txt (refs a docs/cli/generation-settings.md, docs/cli/token-caching.md)

## D7 — Memória e estado persistente

**Auto Memory:** Sistema de fundo analisa transcrições de sessões passadas, identifica padrões duráveis. Tipos de artefatos persistidos:
1. **Atualizações de memória** — patches que modificam arquivos de memória existentes
2. **Habilidades (Skills)** — procedimentos reutilizáveis em `SKILL.md`
3. **Contexto do projeto** — verificações, restrições, notas técnicas

**Local de persistência:** Habilidades promovidas → `~/.gemini/skills/` (usuário) ou `.gemini/skills/` (projeto). Patches de memória atualizam arquivos subjacentes. Drafts vivem em inbox do diretório de memória até revisão (`/memory inbox`) — nada aplicado automaticamente. **Sessions:** Transcritos persistem localmente (local filesystem), sobrevivem entre invocações.

Fonte: https://raw.githubusercontent.com/google-gemini/gemini-cli/HEAD/docs/cli/auto-memory.md

## D8 — Qualidade e testes

**Estratégia de testes:** Três níveis:
1. **Testes de integração** — validam funcionalidade end-to-end, binário compilado em ambiente controlado
2. **Testes de memória** — detectam vazamento de heap, snapshots com tolerância ≤10%
3. **Testes de performance** — latência, CPU, event loop delay com tolerância ≤15%

**Deflaking obrigatório:** Novos testes devem passar em ≥5 execuções antes de aprovação. **Ambientes múltiplos:** Execução em nenhum, Docker, Podman. **Linting automático:** CI/CD via GitHub Actions. **TDD:** Não mencionado — testes como validação pós-desenvolvimento. Arquivo: `docs/integration-tests.md`.

Fonte: https://raw.githubusercontent.com/google-gemini/gemini-cli/HEAD/docs/integration-tests.md

## D9 — Guardrails e enforcement

**Código executável:** CI/CD automático via `.github/workflows/` (ci.yml, test-build-binary.yml, etc.). **Regras textuais:** `.gemini/commands/strict-development-rules.md` (arquivo existente, conteúdo não buscado). **Strict mode:** Modo "yolo" pode ser desabilitado por políticos de admin. **Sandbox:** Sistema suporta múltiplos sandboxes (nenhum, Docker, Podman) conforme `docs/cli/sandbox.md`. **MCP allowlist (Model Context Protocol):** Administrador pode fazer override global que **não pode ser contornado localmente** — lista vazia usa config local, lista ativa ignora servidores não presentes, fusão garante servidor só funciona se **ambos** allowlist e config local o incluem. Campos de execução local (`command`, `args`, `env`, `cwd`) são automaticamente limpos para prevenir contorno.

Fonte: https://raw.githubusercontent.com/google-gemini/gemini-cli/HEAD/docs/admin/enterprise-controls.md; docs/benchmark/_trees/google-gemini-gemini-cli.txt (refs a `.gemini/commands/strict-development-rules.md`, `.github/workflows/`)

## D10 — Distribuição e versionamento do próprio framework

**Versão atual:** v0.52.0 (lançado 2026-07-22). **Versionamento semântico:** MAJOR.MINOR.PATCH com sufixos `-nightly` (compilações intermediárias) e `-preview` (pré-lançamentos). **Distribuição:** `package.json` indica instalação via npm. **Changelog:** `docs/changelogs/latest.md` (13 mudanças principais em v0.52.0), histórico em `docs/changelogs/preview.md`. Ciclo de release com PRs rastreados no GitHub. Não há evidência de auto-update ou mecanismo de verificação de versão in-band.

Fonte: https://raw.githubusercontent.com/google-gemini/gemini-cli/HEAD/docs/changelogs/latest.md; docs/benchmark/_trees/google-gemini-gemini-cli.txt (package.json linha 453)

## D11 — Extensibilidade

**Sistema de extensões:** Package prompts, MCP servers, custom commands, themes, hooks, sub-agents, agent skills em formato reutilizável. Instalação via: `gemini extensions install https://github.com/[repositorio]` ou caminho local. Descoberta via [Gemini CLI extension gallery](https://geminicli.com/extensions/browse/). **Sem fork necessário:** Composição de funcionalidades via pacotes independentes compartilháveis. **Criação própria:** Seguir templates em `docs/extensions/writing-extensions.md`. **Skills:** Sistema modular em `.gemini/skills/*.md` (projeto) ou `~/.gemini/skills/` (usuário), documentado em `docs/cli/creating-skills.md`, `docs/cli/skills-best-practices.md`. **Hooks:** Customização via `docs/hooks/writing-hooks.md`.

Fonte: https://raw.githubusercontent.com/google-gemini/gemini-cli/HEAD/docs/extensions/index.md; docs/benchmark/_trees/google-gemini-gemini-cli.txt (refs a docs/extensions/, docs/cli/creating-skills.md, docs/hooks/)

## D12 — Observabilidade e métricas

**Telemetria:** Baseada em OpenTelemetry (padrão neutro industria). Três pilares: **logs, métricas, traces**. **Métricas customizadas:** Contagem de sessões, requisições de API, latência de ferramentas (ms), uso de tokens (entrada, saída, cache), operações de arquivo, eventos de compressão. **Métricas de performance:** Duração de startup (por fase), heap/RSS, CPU, profundidade de fila. **Exportação:** Para backends como Google Cloud, Jaeger, Prometheus. **Série histórica:** Documentação não menciona retenção histórica integrada — responsabilidade do backend de destino. Arquivo: `docs/cli/telemetry.md`.

Fonte: https://raw.githubusercontent.com/google-gemini/gemini-cli/HEAD/docs/cli/telemetry.md

## D13 — Segurança e permissões

**Management Console:** Administrador aplica políticas globalmente, não controláveis localmente. **Strict mode:** Desabilita modo "yolo". **Extensions:** Pode desabilitar uso/instalação. **Unmanaged capabilities:** Desativa agent skills. **MCP (Model Context Protocol):** Allowlist em camadas — lista vazia → config local; lista ativa → ignora servidores fora dela. Fusão: servidor funciona só se **ambos** allowlist + config local o incluem. **Campos limpos:** `command`, `args`, `env`, `cwd` automaticamente removidos para prevenir contorno (execução local desabilitada). **Required servers:** Injetados automaticamente mesmo sem config local, garantindo conformidade. **Sandbox:** Suporte a Docker, Podman.

Fonte: https://raw.githubusercontent.com/google-gemini/gemini-cli/HEAD/docs/admin/enterprise-controls.md; docs/benchmark/_trees/google-gemini-gemini-cli.txt (refs a docs/cli/sandbox.md)

## D14 — Onboarding humano e documentação

**Estrutura doc:** Documentação extensa em `docs/` com seções dedicas:
- `docs/get-started/` (installation.mdx, authentication.mdx, index.md, gemini-3.md)
- `docs/cli/` (32+ guias incluindo cli-reference.md, model.md, session-management.md)
- `docs/core/` (index.md, remote-agents.md, subagents.md, local-model-routing.md)
- `docs/extensions/`, `docs/hooks/` (com best-practices.md)
- `docs/tutorials/` (automation.md, mcp-setup.md, skill-getting-started.md, etc.)

**README.md:** Propósito, plano gratuito, casos de uso, integração. **CONTRIBUTING.md:** Processo de contribuição (conteúdo não buscado). Não há métricas sobre quanto um humano precisa ler — estimativa via volume: >50 arquivos .md, estrutura progressiva (get-started → cli → core).

Fonte: docs/benchmark/_trees/google-gemini-gemini-cli.txt (docs/get-started/, docs/cli/, docs/core/); https://raw.githubusercontent.com/google-gemini/gemini-cli/HEAD/README.md

## D15 — Multi-projeto, multi-repo e equipe

**Compartilhamento de doutrina:** Configuração de projeto em `.gemini/config.yaml` (local); agentes em `.gemini/agents/` (projeto) ou `~/.gemini/agents/` (usuário/global). Skills em `.gemini/skills/` (projeto) ou `~/.gemini/skills/` (usuário). **Multi-repo:** Suporte a git worktrees (docs/cli/git-worktrees.md) e session management (docs/cli/session-management.md) sugere contexto por workspace. **Equipe:** Não há evidência de modelo colaborativo multi-usuário ou sincronização de estado entre usuários. Governo é **por máquina local** (config, skills, agents) ou **global por admin** (enterprise controls, MCP allowlist). Não há SLA de sincronização ou modelo de permissões por usuário.

Fonte: docs/benchmark/_trees/google-gemini-gemini-cli.txt (.gemini/config.yaml, .gemini/agents/, .gemini/skills/); https://raw.githubusercontent.com/google-gemini/gemini-cli/HEAD/docs/admin/enterprise-controls.md

## D16 — Interação com o humano

**Aprovações obrigatórias:** Memory inbox (`/memory inbox`) — skills e memory patches submetem-se a revisão manual antes de aplicação. Nada automático. **Decisões humanas:** Plan mode oferece checkpoints estruturados (não detalhado em busca), fluxo explícito de planejamento antes de execução. **Consultas:** Workflows de PR review mencionam flags booleanas (`help`, `summary`, `code_review`, `include_drafts`) que controlam que informação é consultada ao humano. **Automático nunca:** Prompts são sugestões (ex.: memory patches, skills) — nunca executadas sem `/memory inbox` review. Enterprise mode pode forçar behaviors via admin override, mas input local do usuário é sempre aceitável (lista local sobrescreve ou complementa allowlist).

Fonte: https://raw.githubusercontent.com/google-gemini/gemini-cli/HEAD/docs/cli/auto-memory.md; https://raw.githubusercontent.com/google-gemini/gemini-cli/HEAD/.gemini/config.yaml; https://raw.githubusercontent.com/google-gemini/gemini-cli/HEAD/docs/admin/enterprise-controls.md

---

## Rodapé

### 3 Práticas transplantáveis

1. **Auto Memory com inbox review (custo: baixo):** Framework detecta padrões duráveis de sessões passadas (facts, skills, procedures) e submete candidatos a revisão manual antes de persistência. Separa **descoberta automática** de **aprovação humana explícita**, reduzindo risco de poluição de memória com falsas generalizações. Implementável em qualquer CLI que registre transcrições: parse → candidate extractor → inbox file → manual `/memory apply`.

2. **OpenTelemetry integrado (custo: médio):** Telemetria customizada sobre atividade do agente (contagem de sessões, latência por ferramenta, tokens, operações de arquivo, heap, CPU) exportada para backends agnósticos (Google Cloud, Jaeger, Prometheus). Permite diagnosticar gargalos reais sem logs verbosos; série histórica fica a cargo do backend. Transplantável: adicionar instrumentação OTel a qualquer agente + middleware de export.

3. **Multi-sandbox CI com deflaking obrigatório (custo: médio-alto):** Testes em ≥5 execuções antes de merge, ambiente múltiplos (nenhum, Docker, Podman), snapshots de memória/performance com tolerância. Reduz flakiness e regressão silenciosa. Alto custo de implementação (plumbing CI/CD), mas pagável em projeto ativo; ROI em confiabilidade de testes.

### 3 Anti-práticas

1. **Allowlist global sem bypass local (anti-padrão):** MCP allowlist de admin limpa campos de execução (`command`, `args`, `env`, `cwd`) e ignora config local se fora da lista. Resolve conformidade corporativa, mas impede troubleshooting e torna difícil auditoria de por-quê-uma-coisa-não-funciona. Produz `"erro silencioso"` para usuário (config aplicada mas ignorada). **Por quê não copiar:** Enterprise security é legítimo, mas assimetria de visibilidade (admin vê allowlist, usuário não vê pq falhou) viola princípio de least surprise; melhor: audit log transparente + denied message.

2. **Skill promotion como único mecanismo de reutilização (anti-padrão):** Skills (`.gemini/skills/`) devem passar por inbox review antes de serem aplicadas. Para desenvolvimento iterativo rápido, isso é atrito; para framework legado, é garantia de que você não tem velhas skills poluindo o contexto sem rastreamento. **Por quê não copiar:** A taxa de promoção de skill reflete enviesamento do author — frameworks que deixam user rodar skill experimental sem promover descobrem mais rápido edge cases (falha rápida, iteração rápida). Aqui, feedback é lento; melhor: draft skills com auto-cleanup + deprecation warnings.

3. **Sem rastro requisito → código → teste explícito (anti-padrão):** Unidade de trabalho é nebulosa (command? skill? session?). Não há mecanismo natural para rastrear de requisito de usuário até código até teste específico. Adequado para exploração/prototipagem; inad em regime de produção com múltiplas features em voo. **Por quê não copiar:** Sem rastro, regressão é invisível; cherry-pick de fixes é frágil; onboarding de novo dev é adivinhação.

### Dimensões fora da grade (D1..D16)

**Routing de modelo**: Documentação extensa em `docs/cli/model-routing.md`, `docs/cli/model-steering.md`, `docs/cli/local-model-routing.md` sugere que framework permite flexibilidade em qual modelo processa que tarefa — relevante para custo/latência, mas não encaixa em D6 (contexto/custo é orçamento, não routing). **Artifact versioning within session**: Sessions são transcritos persistidos; não há evidência de branches/checkpoints intra-sessão além de `/rewind` (documentado em `docs/cli/rewind.md`, não buscado). **Checkpointing and git integration**: `docs/cli/checkpointing.md` existe; integração com git worktrees (`docs/cli/git-worktrees.md`). Ambas sugerem "snapshots de estado do projeto", não cobertas bem em D7 (memória é doutrina, não estado de código).
