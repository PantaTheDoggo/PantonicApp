# BM-04: SuperClaude Framework

## D1 — Identidade e escopo
Framework transforma Claude Code em plataforma estruturada por injeção de instruções comportamentais e orquestração de componentes. Resolve: fragmentação workflow (automação brainstorming→deploy), preservação orçamento tokens, falta especialização. Para: equipes/devs em projetos complexos full-stack conhecimento-intensivos.
Fonte: https://raw.githubusercontent.com/SuperClaude-Org/SuperClaude_Framework/HEAD/README.md

## D2 — Vitalidade
Stars: 23.613 | Push: 2026-07-22T06:02:09Z | Licença: MIT | Contribuidores: NÃO ENCONTRADO
Fonte: `docs/benchmark/_CORPUS.md` linha 49 (cache do `V2B-T3`)

## D3 — Ciclo de vida do trabalho
PDCA contínuo: Plan (hipóteses em docs/temp/hypothesis-*.md) → Do (checkpoints via TodoWrite em docs/temp/experiment-*.md) → Check (auto-avaliação, lições em docs/temp/lessons-*.md) → Act (sucesso→docs/patterns/, falha→docs/mistakes/, atualiza CLAUDE.md). Gates de qualidade entre fases.
Fonte: https://raw.githubusercontent.com/SuperClaude-Org/SuperClaude_Framework/HEAD/docs/Development/ARCHITECTURE.md

## D4 — Papéis e modelo por fase
20 agentes especializados. Modelo: ConfidenceChecker (pré-exec ≥90% prossegue, 70-89% alternativas, <70% questiona), SelfCheckProtocol (pós-impl), ReflexionPattern (aprendizado inter-sessão). PM Agent coordena.
Fonte: https://raw.githubusercontent.com/SuperClaude-Org/SuperClaude_Framework/HEAD/CLAUDE.md, AGENTS.md

## D5 — Unidade de trabalho e rastreabilidade
Tarefa = descrição + critérios + estimativa + prioridade. Rastreabilidade parcial: estados (TODO→IN PROGRESS→BLOCKED→REVIEW→DONE); requisito→código (linhas)→teste (cobertura 0% atual).
Fonte: https://raw.githubusercontent.com/SuperClaude-Org/SuperClaude_Framework/HEAD/TASK.md

## D6 — Contexto e custo
Orçamento: Simples 200, Médio 1.000, Complexo 2.500 tokens. ROI: 100-200 em confiança economiza 5.000-50.000. Modelo: humano define threshold; máquina questiona <70%, alternativas intermediária.
Fonte: https://raw.githubusercontent.com/SuperClaude-Org/SuperClaude_Framework/HEAD/CLAUDE.md

## D7 — Memória e estado persistente
Sobrevive: métricas (150+ campos), tarefas, feedback, workflows. Não: código, contexto conversacional. Armazenado: `docs/memory/workflow_metrics.jsonl` (append-only), rotação mensal, limpeza 6 meses.
Fonte: https://raw.githubusercontent.com/SuperClaude-Org/SuperClaude_Framework/HEAD/docs/memory/WORKFLOW_METRICS_SCHEMA.md

## D8 — Qualidade e testes
TDD: não mencionado. Gates: ausentes. Regressão/piso: não definido. Status: cobertura 0%, projeto 35% completo, testes planejados semanas 2-3 reativo.
Fonte: https://raw.githubusercontent.com/SuperClaude-Org/SuperClaude_Framework/HEAD/docs/Development/PROJECT_STATUS.md

## D9 — Guardrails e enforcement
~60% texto descritivo, ~30% checklists, ~10% código. Enforcement manual/interpretativo — instruções semânticas dependem interpretação agente, não scripts automáticos.
Fonte: https://raw.githubusercontent.com/SuperClaude-Org/SuperClaude_Framework/HEAD/src/superclaude/core/RULES.md

## D10 — Distribuição e versionamento do próprio framework
Semantic Versioning (4.3.0). Instalação: marketplace oficial ou dev mode. Consumidor identifica versão via arquivo `VERSION`. Distribuição: npm com package.json por módulo.
Fonte: https://raw.githubusercontent.com/SuperClaude-Org/SuperClaude_Framework/HEAD/PLUGIN_INSTALL.md, VERSION

## D11 — Extensibilidade
Plugins (Markdown slash commands em ~/.claude/plugins/), skills (confidence-check, deep-research, pm, token-efficiency, troubleshoot), hooks (SessionStart/Stop/PostToolUse/TaskCompleted), agentes TypeScript standalone. Sem fork.
Fonte: https://raw.githubusercontent.com/SuperClaude-Org/SuperClaude_Framework/HEAD/PLUGIN_INSTALL.md

## D12 — Observabilidade e métricas
Workflow Metrics Schema em docs/memory/workflow_metrics.jsonl (append-only JSONL ISO 8601). Campos: consumo (tokens/tempo/arquivos), qualidade (sucesso/feedback/alucinação), eficiência. Série histórica: análise semanal, testes A/B, tendências. Rotação mensal.
Fonte: https://raw.githubusercontent.com/SuperClaude-Org/SuperClaude_Framework/HEAD/docs/memory/WORKFLOW_METRICS_SCHEMA.md

## D13 — Segurança e permissões
Sandbox: project-specific workspace, MCP sandboxed. Allowlist: absolute path, directory traversal prevention, whitelist sensíveis. Segredos: nenhum armazenamento, API keys em credential stores, redação logs. Destrutivas: validação pré-exec, dry-run, backup, rollback.
Fonte: https://raw.githubusercontent.com/SuperClaude-Org/SuperClaude_Framework/HEAD/SECURITY.md

## D14 — Onboarding humano e documentação
Decisão: 5 min (Instant Start). Início: 4 níveis (S1: 3 comandos; S2: behavioral modes; S3: MCP; S4: avançado). Docs: beginner→intermediate→advanced.
Fonte: https://raw.githubusercontent.com/SuperClaude-Org/SuperClaude_Framework/HEAD/docs/getting-started/quick-start.md

## D15 — Multi-projeto, multi-repo e equipe
Sem sincronização multi-repo. Single-repo focused. Organizações devem implementar própria estratégia (submodules, monorepo, versioning, coordenação).
Fonte: https://raw.githubusercontent.com/SuperClaude-Org/SuperClaude_Framework/HEAD/docs/PR_STRATEGY.md

## D16 — Interação com o humano
Humano estabelece threshold confiança; máquina questiona <70%, alternativas intermediária. Reflexão multi-sessão requer interpretação humana. Feedback acumulado recalibra.
Fonte: https://raw.githubusercontent.com/SuperClaude-Org/SuperClaude_Framework/HEAD/CLAUDE.md

## Práticas Transplantáveis
1. **Confidence Checker** (baixo): limiares confiança pré-exec. Impacto: -30-40% retrabalho. Adoção: 2-3 dias.
2. **Workflow Metrics Schema** (médio): telemetria JSONL 150+ campos. Impacto: visibilidade tendências, detecção regressão. Adoção: 1-2 semanas.
3. **Behavioral Modes + Hooks** (médio): modos contextuais automação. Impacto: adaptação contexto. Adoção: 2-3 semanas.

## Anti-Práticas
1. **Guardrails textuais (~60% texto, 10% código):** impossível auditar; enforcement interpretativo. Anti-padrão: frameworks IA precisam validação programática.
2. **Testes 0% em framework:** ferramenta aumenta confiabilidade dev mas própria sem testes. Risco: propagação bugs.
3. **Sem sincronização multi-repo:** força reinvenção estratégia. Anti-padrão: reduz adoção, fragmenta.

## Dimensões Fora da Grade
- **Multilíngue nativo:** EN, JP, KR, ZH com guias traduzidos. Raro em frameworks.
- **Reflexão PDCA:** sucesso→docs/patterns/, falha→docs/mistakes/, atualiza CLAUDE.md. Evolução contínua.
- **MCP Orchestration (8):** Contexto, Tavily, Playwright, Sequential, Magic, Morphllm, Chrome, Serena. Coreografia rara.
