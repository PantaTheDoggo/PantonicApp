# BM-05 — Benchmarking: anthropics/claude-code
**Repositório:** `anthropics/claude-code` | **Trilha:** B | **Corpus:** 21 repositórios

## D1 — Identidade e escopo
Claude Code: ferramenta agentic de codificação no terminal, automação de tarefas rotineiras (edição, Git, explicação). Para desenvolvedores em terminal/IDE/GitHub (MacOS, Linux, Windows).
**Ref:** https://raw.githubusercontent.com/anthropics/claude-code/HEAD/README.md

## D2 — Vitalidade
- Stars: 139455 | Push: 2026-07-25 | Contribuidores: NÃO ENCONTRADO | Licença: Anthropic Commercial Terms (proprietária)
**Ref:** https://raw.githubusercontent.com/anthropics/claude-code/HEAD/LICENSE.md

## D3 — Ciclo de vida do trabalho
7 fases (feature-dev): Discovery → Exploration (artefato: key files file:line) → Clarifying Qs (lista) → Architecture (2-3 abordagens, trade-offs) → Implementation → Quality Review (por severidade) → Summary.
Gates: 3→4 (aguarda respostas), 4→5 (aprova abordagem), 6→7 (decide fix).
**Ref:** https://raw.githubusercontent.com/anthropics/claude-code/HEAD/plugins/feature-dev/README.md

## D4 — Papéis e modelo por fase
Agentes: agent-sdk-verifier-py, agent-sdk-verifier-ts, code-reviewer, code-simplifier, comment-analyzer, pr-test-analyzer, silent-failure-hunter, type-design-analyzer, conversation-analyzer, agent-creator, plugin-validator, skill-reviewer.
Comandos: /new-sdk-app, /create-plugin, /feature-dev, /code-review, /review-pr.
Modelo explícito por agente/fase: NÃO ENCONTRADO
**Ref:** https://raw.githubusercontent.com/anthropics/claude-code/HEAD/plugins/agent-sdk-dev/README.md

## D5 — Unidade de trabalho e rastreabilidade
Unidades: Feature, PR, Comando. Rastreamento requisito→código→teste: NÃO ENCONTRADO (agentes analisam testes mas sem rastreamento bidirecional).
**Ref:** https://raw.githubusercontent.com/anthropics/claude-code/HEAD/plugins/pr-review-toolkit/agents/code-reviewer.md

## D6 — Contexto e custo
Orçamento/limite explícito: NÃO ENCONTRADO. Sem documentação de políticas de consumo, orçamento ou limites de contexto.

## D7 — Memória e estado persistente
Configuração em settings.json (permissões, sandbox, allowlist). Manifesto: .claude-plugin/plugin.json (metadata estática).
Estado entre invocações: NÃO ENCONTRADO (compartilhamento de contexto entre agentes não documentado).
**Ref:** https://raw.githubusercontent.com/anthropics/claude-code/HEAD/.claude-plugin/marketplace.json

## D8 — Qualidade e testes
TDD: NÃO ENCONTRADO | Gates de regressão: NÃO ENCONTRADO | Piso de regressão: NÃO ENCONTRADO.
Agentes usam confidence scores (0-100) sem série histórica ou gate automático.
**Ref:** https://raw.githubusercontent.com/anthropics/claude-code/HEAD/plugins/pr-review-toolkit/README.md

## D9 — Guardrails e enforcement
Tipo: Texto (Markdown) + permissões JSON. Enforcement: allow/ask/deny em settings.json, propriedades booleanas.
Proporção: Maioria texto (guias .md), enforcement via JSON (não runtime visível).
**Ref:** https://raw.githubusercontent.com/anthropics/claude-code/HEAD/examples/settings/README.md

## D10 — Distribuição e versionamento do próprio framework
Instalação: Homebrew, curl, PowerShell, WinGet. Atualização: auto-update (streaming) + /update.
Versão: sequencial (2.1.220), comando não documentado. Cadência: frequente (múltiplas versões/período).
**Ref:** https://raw.githubusercontent.com/anthropics/claude-code/HEAD/CHANGELOG.md

## D11 — Extensibilidade
Sistema de plugins (.claude-plugin/) com descoberta automática. Componentes: comandos, agentes, skills, hooks.
Publicação: Marketplace, local, npm. Sem fork: estrutura de descoberta permite estender sem alterar código-base.
**Ref:** https://raw.githubusercontent.com/anthropics/claude-code/HEAD/plugins/plugin-dev/skills/plugin-structure/SKILL.md

## D12 — Observabilidade e métricas
Telemetria de consumo: NÃO ENCONTRADO | Série histórica: NÃO ENCONTRADO.
Confidence scores (0-100) retornados sem agregação histórica.
**Ref:** https://raw.githubusercontent.com/anthropics/claude-code/HEAD/plugins/pr-review-toolkit/README.md

## D13 — Segurança e permissões
Sandbox: Bash apenas (não Read, Write, WebSearch, WebFetch, MCPs). Permissões: allow/ask/deny em settings.json.
Gestão de segredos: NÃO ENCONTRADO | Prevenção de ações destrutivas: NÃO ENCONTRADO.
Bug bounty via HackerOne.
**Ref:** https://raw.githubusercontent.com/anthropics/claude-code/HEAD/examples/settings/README.md, https://raw.githubusercontent.com/anthropics/claude-code/HEAD/SECURITY.md

## D14 — Onboarding humano e documentação
README detalhado. Cada plugin: README.md, SKILL.md, Agent .md, exemplos (gateway AWS/GCP, MDM, settings).
Fluxos interativos com approval gates. Plugins learning-output-style e explanatory-output-style.
**Ref:** https://raw.githubusercontent.com/anthropics/claude-code/HEAD/README.md

## D15 — Multi-projeto, multi-repo e equipe
Gateway (AWS, GCP) — mesmo plugin multi-cloud. MDM (MacOS, Windows) — mesmo padrão multi-OS.
Plugins independentes, descoberta automática, sem fork.
**Ref:** https://raw.githubusercontent.com/anthropics/claude-code/HEAD/plugins/

## D16 — Interação com o humano
Gates explícitos: create-plugin (confirm → approve plan → proceed), feature-dev (waits 3→4, which approach 4→5, fix 6→7).
Previne automático: "provide recommendations and get explicit confirmation" se usuário defere.
Decisões humanas: escopo, componentes, especificações, design, fix.
**Ref:** https://raw.githubusercontent.com/anthropics/claude-code/HEAD/plugins/plugin-dev/commands/create-plugin.md

---

## Rodapé obrigatório

### 3 práticas transplantáveis
1. **Feature-dev com 7 fases + gates** (~4h): estrutura sistemática, rastreamento, previne automatismo.
2. **Plugins com descoberta automática** (~6h): desacoplamento, reutilização, extensibilidade sem fork.
3. **Permissões em settings.json (allow/ask/deny)** (~2h): política centralizada, auditável.

### 3 anti-práticas
1. **Licença comercial proprietária**: reduz contribuição comunitária, inibe fork, incompatível com expectativa open-source.
2. **Agentes sem modelo explícito**: impossibilita otimização custo-qualidade (Opus trivial vs Haiku crítico).
3. **Guardrails apenas em texto**: conformidade silenciosa; precisa enforcement de código (hook, guard).

### Dimensões fora da grade
- **Custo por sessão/turno**: sem orçamento de contexto, limite de turnos ou custo. Crítico para agentic long-running.
- **Rastreamento requisito→código→teste**: sem traceability matrix. Essencial para auditoria e regressão.
- **Estado persistente entre invocações**: não documentado se agentes compartilham contexto ou são isolados. Crítico para multi-agent workflows.

---
**Coleta:** 10 buscas | Guardrail 2 respeitado (URLs de arquivos buscados).
