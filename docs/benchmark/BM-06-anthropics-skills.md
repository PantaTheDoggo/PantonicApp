# BM-06 — anthropics/skills

## D1 — Identidade e escopo

**Skills** é um framework de Anthropic que encapsula instruções, scripts e recursos reutilizáveis para estender as capacidades de Claude em tarefas especializadas. Resolve o problema de ensinar AI agents a executar processos repetíveis (design, criação de documentos, testes, branding) com consistência, sem requerer instruções detalhadas a cada invocação.

**Fonte:** https://raw.githubusercontent.com/anthropics/skills/HEAD/README.md

## D2 — Vitalidade

Stars: **164915** | Último push: **2026-07-24T20:12:36Z** | Nº contribuidores: **NÃO ENCONTRADO** | Licença: *sem license.spdx_id*

**Fonte:** https://raw.githubusercontent.com/anthropics/skills/HEAD/.claude-plugin/marketplace.json (metadata via `docs/benchmark/_CORPUS.md`, linha 51)

## D3 — Ciclo de vida do trabalho

**MCP Builder skill** (4 fases):
1. Research & Planning: estudar princípios, specs, documentação
2. Implementation: infraestrutura, utilities, ferramentas com schemas
3. Review & Testing: validação via MCP Inspector e language-specific tools
4. Evaluation Creation: criar 10 questões de avaliação realistas

**Skill-creator skill** usa ciclo iterativo: define intent → write draft → test → evaluate → improve → repeat.

**Doc-coauthoring skill** (3 estágios): Context Gathering → Refinement & Structure → Reader Testing.

**Fonte:** https://raw.githubusercontent.com/anthropics/skills/HEAD/skills/mcp-builder/SKILL.md, skill-creator SKILL.md, doc-coauthoring SKILL.md

## D4 — Papéis e modelo por fase

**Skill-creator** coordena com agentes especializados:
- **Grader Agent**: avalia outputs vs. assertions e critica qualidade do evaluation framework
- **Analyzer Agent**: identifica padrões em benchmark data
- **Comparator Agent**: A/B comparisons blind entre versões

Não há indicação de escolha explícita de modelo (LLM) por fase — o framework é baseado em instruções, não em orchestração de modelos.

**Fonte:** https://raw.githubusercontent.com/anthropics/skills/HEAD/skills/skill-creator/SKILL.md, agents/grader.md

## D5 — Unidade de trabalho e rastreabilidade

Unidade: uma **skill** = pasta com `SKILL.md` (metadados + trigger conditions) + scripts + recursos. Template SKILL.md define nome, descrição, quando disparar.

**run_eval.py** testa discoverability via trigger rate (% de runs disparando skill para queries).

**Grader agent** avalia se outputs satisfazem assertions predefinidas. Não há rastro requisito → código → teste integrado.

**Fonte:** https://raw.githubusercontent.com/anthropics/skills/HEAD/template/SKILL.md, skills/skill-creator/scripts/run_eval.py, grader.md

## D6 — Contexto e custo

**NÃO ENCONTRADO** — nenhuma evidência de limite explícito de contexto, turnos, ou orçamento financeiro nas documentações lidas.

## D7 — Memória e estado persistente

**Doc-coauthoring skill** mantém estado entre estágios via artifacts ou files (documento único como single source of truth). **Internal-comms skill** usa guideline files como persistência de padrões corporativos. Além disso, não há mecanismo de memória entre sessões descrito.

**Fonte:** https://raw.githubusercontent.com/anthropics/skills/HEAD/skills/doc-coauthoring/SKILL.md, internal-comms/SKILL.md

## D8 — Qualidade e testes

**run_eval.py**: testa trigger rate (% de invocações que disparam skill). **Grader agent**: avalia assertions com rigor crítico ("A passing grade on a weak assertion is worse than useless"). **MCP Builder fase 3** inclui review + testing com MCP Inspector e validação language-specific. Não há TDD ou piso de regressão mencionado.

**Fonte:** https://raw.githubusercontent.com/anthropics/skills/HEAD/skills/skill-creator/scripts/run_eval.py, agents/grader.md, mcp-builder/SKILL.md

## D9 — Guardrails e enforcement

**DOCX skill**: valida via XSD checks, usa `<w:ins>`/`<w:del>` tags para tracked changes, recomenda output verification via renderização. Template SKILL.md + run_eval.py fornecem controle sobre trigger via descrição e threshold configurável. Não há guardrails executáveis — validação é manual ("render it and look at it").

**Fonte:** https://raw.githubusercontent.com/anthropics/skills/HEAD/skills/docx/SKILL.md, template/SKILL.md, run_eval.py

## D10 — Distribuição e versionamento do próprio framework

**marketplace.json** define "anthropic-agent-skills" versão 1.0.0 com três plugin groups (document-skills, example-skills, claude-api). Skills distribuem-se dentro deste repositório central via `.claude-plugin/marketplace.json`. Consumidor instala carregando skills via CLI. Sem CHANGELOG ou semantic versioning por skill.

**Fonte:** https://raw.githubusercontent.com/anthropics/skills/HEAD/.claude-plugin/marketplace.json, README.md

## D11 — Extensibilidade

Novos skills criados seguindo **template SKILL.md** (nome + descrição + trigger conditions + instruções). **Skill-creator skill** guia iteração de desenvolvimento de novos skills. Padrão aberto (pasta + SKILL.md + scripts) sem restrição de hook plugins.

**Fonte:** https://raw.githubusercontent.com/anthropics/skills/HEAD/template/SKILL.md, skills/skill-creator/SKILL.md

## D12 — Observabilidade e métricas

**run_eval.py** coleta trigger rate, pass/fail status por query. **skill-creator/scripts/aggregate_benchmark** agrupa timing + token data entre runs. Sem série histórica ou telemetria de produção mencionada.

**Fonte:** https://raw.githubusercontent.com/anthropics/skills/HEAD/skills/skill-creator/scripts/run_eval.py, SKILL.md

## D13 — Segurança e permissões

**.gitignore** minimal (IDE local, __pycache__); não ignora .env ou credentials explicitamente. **DOCX skill** valida via XSD; **internal-comms** mantém guidelines em files. Sem sandbox, allowlist ou ações destrutivas com aprovação explícita. Validação manual é responsabilidade do usuário.

**Fonte:** https://raw.githubusercontent.com/anthropics/skills/HEAD/.gitignore, docx/SKILL.md, internal-comms/SKILL.md

## D14 — Onboarding humano e documentação

**Template SKILL.md** é simples (nome, descrição, instruções). Cada SKILL.md inclui "trigger conditions" e seções organizadas por tarefa ("when you need X, read Y"). **Marketplace.json** e **README** explicam conceito. Spec técnica referencia https://agentskills.io/specification (fora do repositório, não verificável).

**Fonte:** https://raw.githubusercontent.com/anthropics/skills/HEAD/template/SKILL.md, skills/claude-api/SKILL.md, README.md, spec/agent-skills-spec.md

## D15 — Multi-projeto, multi-repo e equipe

**marketplace.json** agrupa skills em três plugin groups (document-skills, example-skills, claude-api). **Internal-comms skill** trata comunicações corporativas (newsletters, FAQs) com múltiplos stakeholders. Sem mecanismo de sincronização ou compartilhamento entre repositórios.

**Fonte:** https://raw.githubusercontent.com/anthropics/skills/HEAD/.claude-plugin/marketplace.json, skills/internal-comms/SKILL.md

## D16 — Interação com o humano

**Doc-coauthoring stage 1**: coleta contextual com feedback iterativo do usuário. **DOCX skill**: requer validação manual antes de finalizar. **Grader agent** fornece crítica de framework — humano revisa antes de aprovar. **Skill-creator**: "Your job is to figure out where the user is in this process and then jump in and help them progress" — design colaborativo.

**Fonte:** https://raw.githubusercontent.com/anthropics/skills/HEAD/skills/doc-coauthoring/SKILL.md, docx/SKILL.md, skill-creator/agents/grader.md, SKILL.md

---

## Práticas transplantáveis

1. **Template SKILL.md com trigger conditions** — estrutura clara e padronizada para descoberta de funcionalidades. Custo de adoção: **baixo** (~1–2 dias).

2. **Script run_eval.py para testar trigger rate** — validação automática de discoverability via runs paralelos. Custo de adoção: **médio** (~3–5 dias).

3. **Grader agent rigoroso para avaliação de assertions** — evita "false confidence" rejeitando expectations fracas. Custo de adoção: **médio** (~1 semana).

## Anti-práticas

1. **Validação manual de operações destrutivas** ("render it and look at it") — sem guardrails executáveis, é arriscado em automação de produção.

2. **Versionamento global único (1.0.0)** — sem semântica por skill, impossível rastrear quebras compatíveis em atualização.

3. **Especificação técnica em URL externa** (agentskills.io) — documentação frágil à mudanças externas não versionadas no repo.

## Dimensões fora da grade

- **Orquestração de múltiplas skills em sequência**: como um skill invoca outro? Não mencionado.
- **Controle de token window entre skills**: doc-coauthoring usa artifacts, mas limite é implícito.
- **Versionamento granular por skill**: apenas versão global do marketplace (1.0.0), sem changelog por skill.
