# BM-07: github/awesome-copilot

## D1 — Identidade e escopo

Catálogo comunitário open source de customizações para GitHub Copilot. Fornece agentes especializados, instruções de codificação, skills autossuficientes, plugins, hooks e workflows. Resolve: como estender Copilot sem forkar. Serve a desenvolvedores que querem reutilizar extensões ou compartilhar suas próprias.
- Fonte: https://raw.githubusercontent.com/github/awesome-copilot/HEAD/README.md

## D2 — Vitalidade

Stars: 37168 | pushed_at: 2026-07-29T05:28:56Z | Licença: MIT | Contribuidores: NÃO ENCONTRADO
- Fonte: docs/benchmark/_CORPUS.md (linha 53)

## D3 — Ciclo de vida do trabalho

Fases: **Contribuição** (autor prepara artefato em tipo específico) → **Validação** (checks automáticos: npm run skill:validate, plugin:validate, GitHub Actions) → **Revisão humana** (etiquetas, comandos /approve /reject) → **Publicação** (mercado Awesome Copilot).

Artefatos por tipo: `.instructions.md`, `.agent.md`, `SKILL.md` (pasta), `.md` (workflows), `plugin/` (pasta). Sem gates formalizados além de checks automáticos; re-review cíclico cada 6 meses para plugins externos.
- Fonte: https://raw.githubusercontent.com/github/awesome-copilot/HEAD/CONTRIBUTING.md

## D4 — Papéis e modelo por fase

Agentes nomeados para especialização: "Senior .NET architect", "TDD implementer", "Security reviewer", "UI/UX designer", "Gem Orchestrator" (coordenador). Orquestração via agente coordenador, não protocolo formal de handoff. Modelo **não é explícito por fase** — cada recurso segue tipo, não estágio.
- Fonte: https://raw.githubusercontent.com/github/awesome-copilot/HEAD/docs/README.agents.md

## D5 — Unidade de trabalho e rastreabilidade

Unidade: Pull Request ou Issue conforme tipo (instructions, agents, skills, plugins, workflows, hooks). Etiquetas de workflow automáticas: awaiting-review, ready-for-review, approved, rejected. Sem rastreamento explícito requisito→código→teste; rastreabilidade é por artefato versionado + PR/Issue link.
- Fonte: https://raw.githubusercontent.com/github/awesome-copilot/HEAD/CONTRIBUTING.md

## D6 — Contexto e custo

NÃO ENCONTRADO

## D7 — Memória e estado persistente

Marketplace.json (manifesto técnico de plugins): https://raw.githubusercontent.com/github/awesome-copilot/marketplace/.github/plugin/marketplace.json. Tabelas README regeneradas por `npm start` (derivadas de estrutura). Skills carregadas sob demanda ("loaded on-demand"), sem estado persistido explícito entre execuções.
- Fonte: https://raw.githubusercontent.com/github/awesome-copilot/HEAD/docs/README.plugins.md

## D8 — Qualidade e testes

TDD: NÃO ENCONTRADO. Gates executáveis: `npm run skill:validate`, `npm run plugin:validate`, GitHub Actions checks (conformidade, nomenclatura, campos obrigatórios). Regressão: re-review cíclico a cada 6 meses para plugins externos após aprovação. Sem "piso de regressão" de testes.
- Fonte: https://raw.githubusercontent.com/github/awesome-copilot/HEAD/CONTRIBUTING.md

## D9 — Guardrails e enforcement

Proporção: **executável** (npm scripts, GitHub Actions, compilação `.lock.yml` antes de exec) ~70%, **texto** (CONTRIBUTING.md, README.* diretrizes) ~30%. "Agent Workflow Firewall" mencionado com "validação rigorosa e sandboxing", mas detalhes técnicos não documentados.
- Fonte: https://raw.githubusercontent.com/github/awesome-copilot/HEAD/docs/README.workflows.md, CONTRIBUTING.md

## D10 — Distribuição e versionamento do próprio framework

Versão: 1.0.0 (SemVer). Distribuição: npm package, GitHub Copilot CLI (`copilot plugin install <plugin>@awesome-copilot`), VS Code (deep links). Sem changelog ou histórico explícito de releases no repositório.
- Fonte: https://raw.githubusercontent.com/github/awesome-copilot/HEAD/package.json

## D11 — Extensibilidade

Plugins (agrupam agentes + skills temáticos), Skills (self-contained com `SKILL.md` + assets), Agents (`.agent.md` com instruções), Instructions (`.instructions.md`), Workflows (`.md` + YAML frontmatter compilados para `.lock.yml`), Hooks (pastas). Mecanismo: contribuir via CONTRIBUTING.md + mercado automático. Sem API declarada; extensão é "puxar e editar".
- Fonte: https://raw.githubusercontent.com/github/awesome-copilot/HEAD/docs/README.plugins.md, README.skills.md

## D12 — Observabilidade e métricas

NÃO ENCONTRADO. Workflows mencionam "saídas estruturadas", sem série histórica ou telemetria de consumo/qualidade documentada.

## D13 — Segurança e permissões

Agent Workflow Firewall (para agentic workflows). Sandboxing: sim. Validação: sim (rigorosa, conforme doc). Allowlist: NÃO ENCONTRADO. Ações destrutivas: NÃO ENCONTRADO. Sem especificação técnica público do Firewall.
- Fonte: https://raw.githubusercontent.com/github/awesome-copilot/HEAD/docs/README.workflows.md

## D14 — Onboarding humano e documentação

Site com busca completa, filtragem por categoria (agentes, instructions, skills, plugins, hooks, workflows). Hub de Aprendizado com guias e tutoriais. Tabelas no README com links. Botões VS Code/Insiders para instalação direta (deep links). CONTRIBUTING.md com passos. Sem documentação de "por que escolher este recurso vs. aquele".
- Fonte: https://raw.githubusercontent.com/github/awesome-copilot/HEAD/README.md, https://raw.githubusercontent.com/github/awesome-copilot/HEAD/docs/README.agents.md, https://raw.githubusercontent.com/github/awesome-copilot/HEAD/docs/README.hooks.md, https://raw.githubusercontent.com/github/awesome-copilot/HEAD/docs/README.instructions.md, https://raw.githubusercontent.com/github/awesome-copilot/HEAD/docs/README.plugins.md, https://raw.githubusercontent.com/github/awesome-copilot/HEAD/docs/README.skills.md, https://raw.githubusercontent.com/github/awesome-copilot/HEAD/docs/README.workflows.md

## D15 — Multi-projeto, multi-repo e equipe

Marketplace.json sugere suporte a múltiplos plugins. Documentação de como compartilhar doutrina entre projetos: NÃO ENCONTRADO. Cada plugin agrupa agentes/skills, mas sem modelo explícito de sincronização ou propagação de padrão.
- Fonte: https://raw.githubusercontent.com/github/awesome-copilot/HEAD/docs/README.plugins.md

## D16 — Interação com o humano

Aprovação manual: etiquetas + comandos de barra (`/approve`, `/reject`, `/rerun-intake`). Re-review cíclico (6 meses). Slash commands em workflows. Comentários automáticos para decisões. Sem especificação de "nunca automático" em ações destrutivas ou sensíveis.
- Fonte: https://raw.githubusercontent.com/github/awesome-copilot/HEAD/CONTRIBUTING.md

---

## Práticas transplantáveis

1. **Marketplace como arquivo estruturado (marketplace.json)**: Curação comunitária com credenciais, versionamento, metadados. Custo de adoção: baixo (um JSON bem-formado). Alto valor para distribuição/descoberta.

2. **Validação executável de estrutura de artefatos (npm scripts)**: `npm run skill:validate`, `plugin:validate` para enforçar convenção sem discussão. Custo: médio (escrever checkers). Enforcement alto.

3. **Re-review cíclico de aprovações antigas**: Cada 6 meses, reavalia plugins já aprovados. Custo: baixo (trigger automático). Segurança a longo prazo contra artefatos envelhecidos.

## Anti-práticas

1. **Documentação de segurança vaga ("guardrails incorporados")**: Sem detalhe técnico de Firewall, allowlist ou sandbox impl. Leva a confiança falsa e erros de integração por parte de consumidores.

2. **Workflow Firewall mencionado mas não especificado publicamente**: Contrato implícito dificulta auditoria e confiabilidade. Consumidor não sabe o que é garantido.

3. **Nenhum orçamento explícito de contexto em workflows**: IA pode gastar tokens sem limite. Sem análise de custo de execução nem "turno máximo".

## Dimensões fora da grade

- **Marketplace como infraestrutura canônica**: Arquivo JSON como single source of truth para descoberta, decoupling de repositório. Ponte entre "o que existe" e "o que o consumidor vê".
- **Compilação de workflows markdown → lock.yml**: Validação estática antes de runtime. Padrão de conversão que captura semântica mas abre brecha de inconsistência entre fonte e compilado.
