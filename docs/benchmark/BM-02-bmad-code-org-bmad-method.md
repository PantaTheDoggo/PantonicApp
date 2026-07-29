# BM-02: bmad-code-org/BMAD-METHOD

**Repositório:** `bmad-code-org/BMAD-METHOD`  
**URL:** https://github.com/bmad-code-org/BMAD-METHOD  
**Data de coleta:** 2026-07-29

---

## D1 — Identidade e escopo

Framework para software delivery assistido por agentes de IA. Resolve o problema da IA "fazer o pensamento por você" oferecendo "um colaborador especializado que o guia através de um processo estruturado". Cobre escala adaptativa (desde bugs até sistemas empresariais) com 6 agentes nomeados (Analyst, Product Manager, Architect, Developer, UX Designer, Technical Writer). Gratuito, código aberto.

**Fonte:** https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/HEAD/README.md

---

## D2 — Vitalidade

- **Stars:** 51221
- **Último push:** 2026-07-29T06:57:18Z
- **Nº de contribuidores:** NÃO ENCONTRADO
- **Licença:** NOASSERTION

---

## D3 — Ciclo de vida do trabalho

Quatro fases: (1) Análise — brainstorm, teste de ideias, pesquisa profunda; (2) Planejamento — PRD, design UX, especificações; (3) Solutioning — decisões técnicas, quebra em stories; (4) Implementação — execução com revisão e retrospectivas. Gate explícito: `bmad-check-implementation-readiness` (PASS/CONCERNS/FAIL) antes de Fase 4.

**Fonte:** https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/HEAD/docs/reference/workflow-map.md

---

## D4 — Papéis e modelo por fase

Seis agentes: Mary (Analyst), John (Product Manager), Winston (Architect), Amelia (Developer), Sally (UX Designer), Paige (Technical Writer). **Sem especificação visível de modelo (custo, capacidade) por agente ou fase.**

**Fonte:** https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/HEAD/docs/reference/agents.md

---

## D5 — Unidade de trabalho e rastreabilidade

Unidade mínima é a "skill" — artefato executável com ID, triggers, workflows. Estrutura de skills em `src/bmm-skills/<fase>/`. Não há evidência de rastro requisito→código→teste explícito documentado.

**Fonte:** docs/benchmark/_trees/bmad-code-org-bmad-method.txt (linhas 220+)

---

## D6 — Contexto e custo

NÃO ENCONTRADO. Sem menção a orçamento de contexto, limites de turnos ou custos explícitos na documentação.

---

## D7 — Memória e estado persistente

Estado compartilhado via `_bmad/_config/manifest.yaml` (versionamento de módulos) e `_bmad/custom/` (overrides TOML por escopo: team ou user). Memória de sessão do Party Mode é configurável ("keep memory across sessions" — yes/no).

**Fonte:** https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/HEAD/docs/how-to/install-bmad.md; https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/HEAD/docs/explanation/party-mode.md

---

## D8 — Qualidade e testes

Gates de teste via módulo TEA (Release Gate). Geração automática pós-implementação (workflow QA). Nenhuma menção explícita a "piso de testes" ou detecção de regressão contínua. Enforcement via código, não checklist.

**Fonte:** https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/HEAD/docs/reference/testing.md

---

## D9 — Guardrails e enforcement

Enforcement é baseado em código: validadores executáveis (`npm run validate:skills`, `npm run quality`). Regras de commit (Conventional Commits). Validação de skills determinística. **Proporção de código vs. texto: predominante em código.**

**Fonte:** https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/HEAD/AGENTS.md

---

## D10 — Distribuição e versionamento do próprio framework

Instalação: `npx bmad-method install` (unificado para first install, upgrades, channel switching). **Dois eixos de versionamento:** por módulo (stable/next/pinned) e do instalador (latest/next). Arquivo `manifest.yaml` documenta versão exata + hash de commit de cada módulo. Rastreabilidade completa.

**Fonte:** https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/HEAD/docs/how-to/install-bmad.md

---

## D11 — Extensibilidade

Customização via `bmad-customize` tool — overrides TOML sem fork. Suporta adicionar/remover/substituir lenses de review. Sem mencionar plugins de código externo ou hooks dinâmicos — apenas configuração declarativa.

**Fonte:** https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/HEAD/docs/reference/core-tools.md

---

## D12 — Observabilidade e métricas

NÃO ENCONTRADO. Nenhuma menção a telemetria de consumo, série histórica de performance ou dashboards. Única ferramenta de observabilidade é `bmad-help` (recomenda próximo passo, inspeciona projeto).

**Fonte:** https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/HEAD/docs/reference/commands.md

---

## D13 — Segurança e permissões

Postura reativa. Recomenda isolamento ("isolated environments"), limite de file access. Reconhece riscos críticos (injeção de prompt, travessia de diretórios, acesso ao filesystem). **Sem sandbox obrigatório, sem allowlist, sem tratamento automático de segredos.** Responsabilidade recai sobre o usuário.

**Fonte:** https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/HEAD/SECURITY.md

---

## D14 — Onboarding humano e documentação

Onboarding não-formal. Contribuidor lê essencial em 5-10 min (filosofia + Before Starting Work + PR Guidelines). Preferência por "talk first" — conversa no Discord antes de código substancial. Templates prontos (bug/feature). Documentação multilíngue (EN, ZH, FR, VI, CS).

**Fonte:** https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/HEAD/CONTRIBUTING.md

---

## D15 — Multi-projeto, multi-repo e equipe

Suporta equipes via git-based distribution. Team overrides (`.toml` sem `.user`) vivem em version control, herdados por todos. Personal overrides (`.*.user.toml`) gitignored. Suporta multi-org repos: *"use `.user.toml` to let individual teams point at their own templates."* Sem menção explícita a distribuição entre repositórios distintos.

**Fonte:** https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/HEAD/docs/how-to/expand-bmad-for-your-org.md

---

## D16 — Interação com o humano

Humano é sempre aprovador final. Modo interativo (padrão): "You steer the room" — conversa aberta até você encerrar. Modo não-interativo (`--non-interactive`): executa até conclusão natural, sem diálogo. Agentes propõem perspectivas conflitantes; humano escolhe. Nada é automático sem decisão explícita.

**Fonte:** https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/HEAD/docs/explanation/party-mode.md

---

## Práticas Transplantáveis

1. **Gate de prontidão antes de implementação** (`bmad-check-implementation-readiness`). Custo de adoção: ~3 linhas de checklist + 1 função de decisão. Bloqueia implementação débil de requisitos bem-definidos.

2. **Versionamento dual (módulo + instalador).** Manifesto YAML centraliza rastreabilidade. Custo: ~50 linhas de tooling no CI/release.

3. **Customização declarativa sem fork** (TOML overrides). Camada team vs. user automática. Custo: ~8h de design de superfícies customizáveis.

---

## Anti-Práticas

1. **Observabilidade ausente.** Nenhuma telemetria de consumo, série histórica ou métricas de qualidade por sprint. Decisões sobre performance ficam cegas.

2. **Segurança delegada ao usuário.** Sem sandbox técnico, allowlist ou tratamento automático de secrets — apenas recomendações. Alto risco em equipes grandes.

3. **Modelo de IA invisível.** Nenhuma escolha explícita de modelo por agente ou fase. Impossível otimizar custo vs. qualidade.

---

## Dimensões Fora da Grade

- **Integração IDE.** Framework menciona "ferramentas de IA/IDE a integrar" no fluxo de instalação, mas não há documentação de qual middleware (Claude Code, GitHub Copilot, etc.) é necessário ou como cada integração funciona. Representa lacuna de onboarding.

**Consumo de coleta:** 12 buscas de conteúdo
