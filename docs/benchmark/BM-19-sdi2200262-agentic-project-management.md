# BM-19: sdi2200262/agentic-project-management

## D1 — Identidade e escopo

Framework de código aberto que coordena múltiplos agentes de IA para gerenciar projetos complexos. Resolve o problema fundamental de degradação de contexto em conversas longas através de handoffs estruturados que transferem conhecimento acumulado entre instâncias. Para projetos ambiciosos de software que exigem coordenação sustentada e equipes que querem transparência e auditabilidade total.
- Fonte: https://raw.githubusercontent.com/sdi2200262/agentic-project-management/HEAD/README.md

## D2 — Vitalidade

2368 stars. Último push: 2026-06-08T13:30:29Z (21 dias). Licença: NOASSERTION. Número de contribuidores não encontrado em metadados.
- Fonte: Corpus cacheado (docs/benchmark/_CORPUS.md, linha 67)

## D3 — Ciclo de vida do trabalho

Duas fases principais. **Planning Phase**: Planner aplica "Context Gathering, then Work Breakdown" e produz 3 documentos de planejamento; após aprovação, inicializa Message Bus. **Implementation Phase**: Manager e Workers executam "continuous coordination loop of dispatching Tasks, reviewing results, and maintaining project state". Tarefa percorre 4 etapas: Task Assignment (Manager avalia prontidão) → Task Execution (Worker executa) → Task Logging (documenta) → Task Review (Manager examina logs, determina próximos passos). Tarefa transita por estados: Waiting → Ready → Active → Done.
- Fonte: https://raw.githubusercontent.com/sdi2200262/agentic-project-management/HEAD/templates/_standards/WORKFLOW.md

## D4 — Papéis e modelo por fase

Três papéis principais definidos no framework: **Planner** (transforma requisitos em 3 documentos de planejamento), **Manager** (coordena execução, dispatch de tarefas, revisão), **Worker** (executa instruções, valida resultados). Modelo explícito por fase via templates: "Templates (commands, guides, skills, agents)" orientam comportamentos em cada estágio. Aprovações humanas ocorrem no ciclo de revisão comunitária (Pull Requests com discussão), não em automação — "mention @sdi2200262 in relevant issues or PRs" para decisões arquiteturais.
- Fonte: https://raw.githubusercontent.com/sdi2200262/agentic-project-management/HEAD/CONTRIBUTING.md

## D5 — Unidade de trabalho e rastreabilidade

Uma tarefa é definida como: "Discrete work unit with objective, deliverables, validation criteria, and dependencies." Cada tarefa contém objetivo claro, entregas específicas, critérios de validação e dependências. Tarefas progridem através de estados no Tracker: Waiting → Ready → Active → Done, sendo conclusão uma decisão final do Manager. Não há documentação de rastro requisito → código → teste.
- Fonte: https://raw.githubusercontent.com/sdi2200262/agentic-project-management/HEAD/templates/_standards/TERMINOLOGY.md

## D6 — Contexto e custo

NÃO ENCONTRADO

## D7 — Memória e estado persistente

Message Bus (fila baseada em arquivo) com diretórios dedicados por agente contendo tarefas, relatórios de conclusão e handoff. Cada agente possui `.apm/bus/<agent-slug>/handoff.md` para transferência estruturada de contexto. Persistência centralizada em `.apm/metadata.json` armazena: versão de lançamento instalada, assistentes instalados, timestamps. Artefatos chave: Spec (manager lê direto), Plan (manager extrai para Task Prompts), Rules (todos leem), Tracker (estado vivo), Memory (índice + logs de tarefas/handoffs).
- Fonte: https://raw.githubusercontent.com/sdi2200262/agentic-project-management/HEAD/templates/_standards/WORKFLOW.md, https://raw.githubusercontent.com/sdi2200262/agentic-project-management/HEAD/templates/commands/apm-1-initiate-planner.md

## D8 — Qualidade e testes

NÃO ENCONTRADO

## D9 — Guardrails e enforcement

Validação de caminho é código (bloqueio de traversal, confinamento ao diretório raiz). Sem acesso externo é código. Regras em texto (CONTRIBUTING.md: conformidade com `templates/_standards/`). Limitações críticas: sem verificação de assinatura criptográfica, sem scanning de conteúdo, disclaimer de segurança pode ser permanentemente silenciado. Ações perigosas (injeção de instruções, sobrescrita de configuração) são templating em texto, não código executável.
- Fonte: https://raw.githubusercontent.com/sdi2200262/agentic-project-management/HEAD/SECURITY.md

## D10 — Distribuição e versionamento do próprio framework

CLI instalável via `npm install agentic-pm`; tag `latest` sempre aponta para versão estável. Templates via `apm init` (oficial) ou `apm custom` (personalizados). Atualização via `apm update`: repositórios oficiais buscam "versão mais compatível" com versão major instalada; repositórios personalizados buscam versões mais recentes do mesmo repo. Compatibilidade por major version: CLI v1.x busca apenas v1.x.x releases. Consumidor consulta versão via `.apm/metadata.json` contendo versão instalada, assistentes, timestamps.
- Fonte: https://raw.githubusercontent.com/sdi2200262/agentic-project-management/HEAD/VERSIONING.md

## D11 — Extensibilidade

Dois caminhos documentados: (1) skills standalone como `apm-assist` instaláveis sem clone do repo; (2) skill `apm-customization` "guia um agente de IA através da customização de templates APM, navegação da estrutura do repositório, realização de mudanças, construção e lançamento." Contribuição de novos skills via issue ou PR. Documentação não fornece detalhes técnicos de como implementar extensões personalizadas de skills ou comandos.
- Fonte: https://raw.githubusercontent.com/sdi2200262/agentic-project-management/HEAD/skills/README.md

## D12 — Observabilidade e métricas

NÃO ENCONTRADO

## D13 — Segurança e permissões

CLI não executa scripts durante instalação, apenas extrai ZIP. Validação de caminhos: arquivos confinados ao diretório do projeto; traversal bloqueado; impossível escrever fora da raiz. Riscos identificados: (1) injeção de instruções maliciosas em templates direcionando agentes, (2) sobrescrita de configurações por bundles maliciosos, (3) escrita arbitrária dentro do projeto (src/, package.json). Limitação crítica: nenhuma assinatura criptográfica ou scanning de conteúdo. Recomendação: auditar repositórios, especificar tags, revisar metadata.
- Fonte: https://raw.githubusercontent.com/sdi2200262/agentic-project-management/HEAD/SECURITY.md

## D14 — Onboarding humano e documentação

README explica problema, solução e tipo de projeto. CONTRIBUTING.md detalha papéis, fases, aprovações, como testar e mencionar o owner. Templates explícitos para commands, guides, skills, agents com estrutura prescrita. Documentação em `templates/_standards/` (WORKFLOW, TERMINOLOGY, STRUCTURE, WRITING, NOTES). Padrões em `src/_standards/CLI.md`. Consumidor percorre: README → CONTRIBUTING → templates → exemplos de command/skill.
- Fonte: https://raw.githubusercontent.com/sdi2200262/agentic-project-management/HEAD/CONTRIBUTING.md, https://raw.githubusercontent.com/sdi2200262/agentic-project-management/HEAD/README.md

## D15 — Multi-projeto, multi-repo e equipe

NÃO ENCONTRADO

## D16 — Interação com o humano

Aprovação explícita obrigatória: 3 documentos de planejamento devem ser aprovados antes de iniciar Implementation Phase. Manager examina logs de cada tarefa e determina próximos passos — decisão humana, não automática. Contribuições via Pull Requests com discussão colaborativa. Validação de padrões: conformidade obrigatória com `templates/_standards/`. Testes em projetos reais com reportes de problemas. Nenhum passo da doutrina é 100% automático.
- Fonte: https://raw.githubusercontent.com/sdi2200262/agentic-project-management/HEAD/CONTRIBUTING.md, https://raw.githubusercontent.com/sdi2200262/agentic-project-management/HEAD/templates/_standards/WORKFLOW.md

---

## Práticas transplantáveis

1. **Message Bus baseado em arquivo com handoff estruturado** (custo baixo). Usar diretórios de fila para comunicação entre agentes em vez de API; cada agente tem diretório dedicado com tarefas e handoff.md. Aplicável a qualquer framework de agentes que precise escalabilidade sem orquestração centralizada. Custo estimado: 1-2 dias de implementação.

2. **Aprovação explícita de 3 artefatos de planejamento antes de execução** (custo baixo). Separar fase de planejamento (Planner produz Spec, Plan, Rules) de implementação, exigindo aprovação humana entre elas. Reduz retrabalho e alinha equipe. Custo estimado: mudança de processo, < 1 dia.

3. **Versionamento por major version com compatibilidade pré-checada** (custo médio). CLI v1.x só busca v1.x.x templates, garantindo compatibilidade. Implementável via semver + verificação de compatibilidade no package.json. Custo estimado: 2-3 dias de implementação.

## Anti-práticas

1. **Sem assinatura criptográfica de templates** (risco alto). Qualquer template malicioso pode injetar instruções para exfiltrar dados ou destruir projeto. Framework reconhece o risco mas não implementa mitigação. Copiar sem primeiro estabelecer verificação de assinatura ou allowlist.

2. **Disclaimer de segurança pode ser silenciado permanentemente** (`skipDisclaimer`). Oferece falsa sensação de segurança; usuário "desativa" depois e volta a instalar sem auditar. Não copiar sem tornar disclaimer requerido a cada instalação.

3. **Três papéis fixos (Planner, Manager, Worker) sem modelo de escolha por projeto** (rigidez). Todos os projetos usam a mesma estrutura. Copiar apenas após avaliar se seu projeto se encaixa em 2 fases (Planning + Implementation) e 3 papéis especializados.

## Dimensões fora da grade

- **Continuação de sessão (session recovery):** APM detecta que conversas se encerrando significam perda de contexto; implementa `apm-9-recover` para recarregar estado. Mecanismo explícito de resumo ("summarize-session") antes de handoff. Não cabe em D7 (estado persistente) porque vai além de armazenamento — é orquestração de reconexão.
- **Integração de Message Bus com plataforma Claude:** Framework é agnóstico, mas templates explícitos mencionam "Bus Integration" em `templates/skills/apm-communication/bus-integration.md`. Não cabe em D11 (extensibilidade) porque é acoplamento de protocolos, não plugin.
