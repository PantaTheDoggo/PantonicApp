# BM-10 — cline/cline

## D1 — Identidade e escopo

Cline é um assistente de IA para automação de desenvolvimento de código, integrado em IDE (VS Code, JetBrains) e CLI. Resolve automação de edição coordenada de arquivos, execução de comandos, correção de erros de compilação/linting, testes e deployment. Para qualquer projeto que use editor compatível e múltiplos modelos de IA (Claude, GPT, Gemini, etc.). Mantém aprovação humana em cada ação crítica.

*Fonte: https://raw.githubusercontent.com/cline/cline/HEAD/README.md*

## D2 — Vitalidade

Stars: 65159; `pushed_at`: 2026-07-29T07:23:35Z (ativo); Licença: Apache-2.0; Nº de contribuidores: NÃO ENCONTRADO.

*Fonte: docs/benchmark/_CORPUS.md linha 56*

## D3 — Ciclo de vida do trabalho

Três fases explícitas: (1) **Plan mode**: leitura de codebase, busca, discussão estratégica — sem modificação de arquivos nem execução de comandos. Produz sumários em Markdown, perguntas esclarecedoras, planos de implementação. (2) **Act mode**: execução de estratégia com retenção de contexto do planejamento — modifica arquivos, executa comandos, implementa. (3) **Completion/Resumption**: tarefas concluem ou retomam de checkpoints salvos. Ciclos podem iterar entre Plan e Act quando surgem problemas inesperados.

*Fonte: https://raw.githubusercontent.com/cline/cline/HEAD/docs/core-workflows/plan-and-act.mdx*

## D4 — Papéis e modelo por fase

Papéis: **Controller** (fonte única de verdade de estado), **Task** (orquestra loop principal), **McpHub** (gerencia conexões Model Context Protocol), **WebviewProvider** (comunicação UI). Por fase: Plan usa estratégia leitura-apenas; Act usa execução com aprovações discretas. Não há "escolha explícita de modelo por fase" — a documentação não explicita escalonamento de modelos (LLM ou agent type) por fase.

*Fonte: https://raw.githubusercontent.com/cline/cline/HEAD/.clinerules/cline-overview.md*

## D5 — Unidade de trabalho e rastreabilidade

Unidade: "Task" — iniciada pelo usuário via webview, encapsula ciclo completo (plan→act→completion). Rastreabilidade: histórico de conversas é persistido; checkpoints capturam estado de arquivos após cada ação de tool. Não há rastro explícito requisito → código → teste descrito na documentação consultada.

*Fonte: https://raw.githubusercontent.com/cline/cline/HEAD/.clinerules/cline-overview.md; docs/core-workflows/checkpoints.mdx*

## D6 — Contexto e custo

Contexto: janela gerenciada por tarefa; `getStateToPostToWebview()` serializa estado via proto para evitar desvio. Sem limite explícito de contexto documentado — comportamento é "reter contexto de planejamento ao passar para act" e depois "ciclar entre modos". Custo: suporta múltiplos provedores (Anthropic, OpenAI, Gemini, etc.) mas não há orçamento/cap documentado. Telemetria mede features usadas, taxa de conclusão, erros — sem captura de código.

*Fonte: https://raw.githubusercontent.com/cline/cline/HEAD/.clinerules/general.md; docs/enterprise-solutions/monitoring/telemetry.mdx; docs/getting-started/config.mdx*

## D7 — Memória e estado persistente

**Checkpoints**: shadowgit repository separado, snapshots automáticos após cada ação. Persiste entre sessões. Permite: comparar diffs, restaurar arquivos (sem touch na conversa), restaurar tarefa só, restaurar tudo. Não afeta `.git` principal. Limpa edições não rastreadas em `.git`. Configurável (desligável para repos grandes).

*Fonte: https://raw.githubusercontent.com/cline/cline/HEAD/docs/core-workflows/checkpoints.mdx*

## D8 — Qualidade e testes

NÃO ENCONTRADO. Documentação consultada não aborda TDD, gates de teste, ou regressão de piso.

## D9 — Guardrails e enforcement

**Regras em código executável**: (1) `bun` obrigatório para gerência de pacotes — verificado em tasks. (2) Evitar provider string-matching — usar catálogos compartilhados, normalização centralizada. (3) File handling: usar utilidades dedicadas (`stripUtf8Bom`) ao ler configs de usuário. (4) State routing: tudo via `StateManager` após init. (5) Proto: rodar `bun run protos` após mudanças `.proto`, mapear enums em `src/shared/proto-conversions/`. Proporção: ~70% regras em código, 30% em checklist/CLAUDE.md.

*Fonte: https://raw.githubusercontent.com/cline/cline/HEAD/.clinerules/general.md*

## D10 — Distribuição e versionamento do próprio framework

**Distribuição:** npm global (`npm i -g cline`), VS Code Marketplace, JetBrains Marketplace, SDK npm (`npm install @cline/sdk`), Kanban CLI (`npm i -g kanban`), integrações Slack/Telegram/Discord. **Versionamento:** Semantic Versioning (MAJOR.MINOR.PATCH); v4.0.0 recente (migração para SDK compartilhado, ClinePass, Customize marketplace). Cadência: lançamentos regulares (mensais/quinzenais). Usa **changesets** para automação de versionamento. Consumidor sabe versão via `package.json` ou `cline --version`.

*Fonte: https://raw.githubusercontent.com/cline/cline/HEAD/CHANGELOG.md; README.md*

## D11 — Extensibilidade

**Plugins**: 4 métodos de instalação (URLs arquivo, repos Git, pacotes npm, caminhos locais). Escopos: global (`~/.cline/plugins/`) ou por-projeto (`.cline/plugins/`). Estrutura: `package.json` deve incluir campo `cline` com pontos de entrada. **Skills/Hooks/Comandos slash**: documentação referencia escrita de plugins via SDK, mas não detalha construção. Sem necessidade de fork.

*Fonte: https://raw.githubusercontent.com/cline/cline/HEAD/docs/customization/plugins.mdx*

## D12 — Observabilidade e métricas

Telemetria: features usadas, taxa de conclusão de tarefas, erros, performance. Anônima, exclui código/conteúdo/caminhos/argumentos/conversas/credenciais. Desligável per-usuário em settings. Enterprise: prompt storage (backup de histórico conversacional), OpenTelemetry (exportar para Datadog/Grafana). Sem série histórica pública de métricas de consumo; relatórios é opt-in.

*Fonte: https://raw.githubusercontent.com/cline/cline/HEAD/docs/enterprise-solutions/monitoring/telemetry.mdx*

## D13 — Segurança e permissões

**Aprovações**: "não há lista fixa" — cada comando avaliado com flag `requires_approval`. Operações perigosas flagged: dependência mods (`npm install`), exclusão (`rm -rf`), move (`mv`), in-loco edits (`sed -i`). **YOLO mode**: desativa todos os safety checks (explícito, não padrão). **Recomendação**: usar ambientes throwaway/sandbox. **Proteção**: Git como safety net, checkpoints para reversão rápida. **Configuração**: `CLINE_COMMAND_PERMISSIONS` (allow/deny patterns) para restringir execução. **Sandbox**: regra/hook/skill/plugins devem vir de fonte confiável (executam código).

*Fonte: https://raw.githubusercontent.com/cline/cline/HEAD/docs/features/auto-approve.mdx; docs/getting-started/config.mdx*

## D14 — Onboarding humano e documentação

Documentação: site completo em docs/ (mdx), incluindo getting-started, core-workflows, customization, enterprise-solutions. README.md conciso (0 instalação por canal). Exemplos: multi-agent (README), desktop app (ARCHITECTURE.md), quickstart, vscode walkthrough (5 steps). `.clinerules/` inclui padrões específicos (bun-and-node, debug-harness, workflows). Onboarding: decidir exige ler README + 1-2 guias (30min); começar exige npm install + criar task (~5min). Documentação está distribuída mas navegável (docs/docs.json).

*Fonte: README.md; docs/ estrutura via árvore; docs/getting-started/config.mdx*

## D15 — Multi-projeto, multi-repo e equipe

**Múltiplos agentes:** modelo coordinator-specialist, um agente coordena e delega subtarefas. Sincronizam via task board persistente, inter-agent mailbox, mission log. Estado persiste em `~/.cline/data/teams/[team-name]/`. **Múltiplos projetos:** config global (`~/.cline/`) para defaults; config per-projeto (`.cline/`) para comportamento compartilhado com time (version-control enabled, sem secrets). Feature aplicável em CLI, SDK, Kanban; não em VSCode/JetBrains ainda.

*Fonte: https://raw.githubusercontent.com/cline/cline/HEAD/docs/cli/agent-teams.mdx; docs/getting-started/config.mdx*

## D16 — Interação com o humano

**Aprovação:** cada ação crítica (edição, comando, dependência) requer aprovação explícita antes de execução (exceto em YOLO mode, opt-in). **Plan mode**: modo "consulta" — estratégia é discutida, sem execução. **Checkpoints**: usuário pode comparar, escolher restauração, ou manter. **Telemetria:** usuário toggle on/off. **Tarefas:** iniciadas via webview → usuário digita prompts, Cline propõe ações em turno-a-turno. Sem automação silenciosa de operações destrutivas; YOLO é explícito.

*Fonte: docs/core-workflows/plan-and-act.mdx; docs/features/auto-approve.mdx; docs/core-workflows/checkpoints.mdx*

---

## Práticas Transplantáveis

1. **Checkpoints via shadowgit (low-overhead undo):** separar snapshots de arquivo de commits de trabalho permite reverter experimentação sem contaminar histórico de trabalho. Custo de adoção: ~40h (implementar commit hook pós-tool, comparação de diff, seleção de restore).

2. **Plan-Act modal workflow:** separar exploração (read-only, sem contexto loss) de execução (full capabilities) reduz erro de direção antes de modificação. Custo: ~30h (UI branching, state serialization entre modos).

3. **Eval-based command safety (não allowlist fixa):** avaliar `requires_approval` por comando em vez de lista estática permite novos padrões de risco sem refatoração. Custo: ~50h (heurística de eval, logging para auditoria).

## Anti-práticas

1. **Telemetria anônima sem histórico público:** coleta dados de feature-use/erros mas não publica série histórica de "qual feature foi mais usada em qual período" — impede discovery de padrões de adoção e regressão pública de qualidade.

2. **Multi-agente cordination com estado local em disco (~/.cline/data/teams/):** não há sincronização entre máquinas — teams só funcionam em single-machine; escalamento cross-machine (desktops diferentes, CI/CD remoto) fica fora.

3. **Falta de explicit context budget:** no act mode, histórico de conversa cresce sem cap explícito documentado — agentes podem derraparem em contexto sem sinal de aviso ou modo de "compact" automático.

## Dimensões Fora da Grade

- **Mode-locking (plan↔act transitions):** documentação não especifica se transições são implícitas (reconhecer quando act falha e sugerir plan) ou explícitas (usuário digita /plan, /act). Relevante para automação de recuperação.
- **Sub-agentes vs coordinated teams:** CLI/SDK tem duas formas de multi-agent (sub-agents paralelos leitura-only + coordinator-specialist com mailbox). Não há guia de "quando escolher qual."
- **Hooks vs rules vs plugins:** `.clinerules/`, `hooks/`, `skills/`, `plugins/` — cada um executável, mas guia de escopo ("use rules para X, hooks para Y") não está documentado.
