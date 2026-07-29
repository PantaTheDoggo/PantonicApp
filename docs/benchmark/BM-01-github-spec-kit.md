# BM-01: github/spec-kit — Relatório de Benchmarking

**Repositório:** https://github.com/github/spec-kit  
**Metadados:** 124.381 stars | MIT | push 2026-07-28T22:29:28Z

---

## D1 — Identidade e escopo
Framework open-source que implementa Spec-Driven Development (SDD): inverte fluxo tradicional colocando especificação executável como artefato central. Resolve: geração automatizada de código a partir de specs antes da implementação. Aplicável a greenfield, brownfield, exploração criativa e conformidade empresarial. Agnóstico quanto a tecnologia/linguagem/stack.

**Fonte:** https://raw.githubusercontent.com/github/spec-kit/HEAD/README.md

---

## D2 — Vitalidade
**Stars:** 124.381 | **Licença:** MIT | **Último push:** 2026-07-28T22:29:28Z | **Contribuidores:** NÃO ENCONTRADO
**Fonte:** `docs/benchmark/_CORPUS.md` linha 44

---

## D3 — Ciclo de vida do trabalho
Fases: Especificação → Planejamento → Geração de Código → Feedback Operacional (cíclico). **Artefatos:** spec.md (requisitos + histórias + critérios), plan.md (decisões técnicas), data-model.md/contracts (specs executáveis), research.md (contexto), tasks.md (derivadas do plano). **Gates:** Simplicity (máx 3 iniciais), Anti-Abstraction (frameworks diretos), Integration-First (contratos antes de código). Validação contínua, não discreta.

**Fonte:** https://raw.githubusercontent.com/github/spec-kit/HEAD/spec-driven.md

---

## D4 — Papéis e modelo por fase
Suporta 30+ agentes de IA (Claude, Gemini, Kilocode, Copilot, Codex, Forge, Goose, etc). Seleção via `specify init --integration <key>` no setup, não por fase. Cada agente pode ter próprio contexto (CLAUDE.md, .github/copilot-instructions.md), gerenciado por extensão opcional agent-context.

**Fonte:** https://raw.githubusercontent.com/github/spec-kit/HEAD/AGENTS.md

---

## D5 — Unidade de trabalho e rastreabilidade
Unidade: feature com estrutura spec→plan→tasks documentada. Rastreabilidade bidirecional: requisito↔código via decisões técnicas, código↔testes via TDD obrigatório (testes antes da implementação). Feedback operacional fecha o rastro incluindo aprendizados. Cenários de teste "geram implementação e testes".

**Fonte:** https://raw.githubusercontent.com/github/spec-kit/HEAD/spec-driven.md

---

## D6 — Contexto e custo
NÃO ENCONTRADO (nenhum documento menciona limites explícitos de contexto, turnos ou orçamento de tokens).

---

## D7 — Memória e estado persistente
Estado sobrevive via artefatos Markdown (spec.md, plan.md, tasks.md, feature.json) em repositório Git. Coordenação entre equipes ocorre por **convenção**, não automático. Três modelos: Flow-back, Flow-forward, Living spec (definem evolução colaborativa de specs, não sincronização técnica).

**Fonte:** https://raw.githubusercontent.com/github/spec-kit/HEAD/docs/concepts/spec-persistence.md

---

## D8 — Qualidade e testes
TDD **NON-NEGOTIABLE**: testes automatizados antes da implementação. Matriz obrigatória: Linux/Windows × Python 3.11-3.13. Piso de regressão implícito (CI bloqueia regressão). Testes contínuos, não gate único.

**Fonte:** https://raw.githubusercontent.com/github/spec-kit/HEAD/.specify/memory/constitution.md

---

## D9 — Guardrails e enforcement
**Cinco princípios formalizados em constituição.md (2026-06-19), vinculantes para toda mudança.** Enforcement misto: (a) **código executável**: CI roda pytest, ruff, linting markdown, CodeQL; (b) **análise semântica**: `/speckit.analyze` trata violações "MUST" como CRITICAL; (c) **revisão obrigatória**: PR/merge verifica conformidade; desvios injustificados bloqueiam integração.

**Fonte:** https://raw.githubusercontent.com/github/spec-kit/HEAD/.specify/memory/constitution.md, https://raw.githubusercontent.com/github/spec-kit/HEAD/CONTRIBUTING.md

---

## D10 — Distribuição e versionamento do próprio framework
Semantic Versioning (MAJOR.MINOR.PATCH). Descoberta: `specify --version`. Atualização: `pip install --upgrade specify-cli` ou `specify self upgrade`. CLI detecta automaticamente novas versões e avisa. Lançamentos frequentes (múltiplos por semana em períodos ativos).

**Fonte:** https://raw.githubusercontent.com/github/spec-kit/HEAD/CHANGELOG.md

---

## D11 — Extensibilidade
Sistema de catálogos descentralizado (catalog.json, extension.yml). Extensões como repositórios independentes com versionamento semântico. Descoberta via `specify extension search`, instalação via `specify extension add <nome>` ou `--from <url>`. Sem necessidade de fork. Arquitetura: "add new functionality without bloating core".

**Fonte:** https://raw.githubusercontent.com/github/spec-kit/HEAD/extensions/README.md

---

## D12 — Observabilidade e métricas
NÃO ENCONTRADO (nenhuma série histórica de consumo, telemetria ou métricas de qualidade).

---

## D13 — Segurança e permissões
NÃO ENCONTRADO (apenas política de divulgação de vulnerabilidades; sem sandbox, allowlist, ou tratamento formal de segredos).

---

## D14 — Onboarding humano e documentação
Setup mínimo: 5-9 etapas. Conceitos críticos a compreender: (1) explicitação de objetivos, (2) separação spec/stack, (3) rastreamento via .specify/feature.json. Curva de aprendizado: rápida (fluxo curto para features menores). Resto é automatizado pelo agente.

**Fonte:** https://raw.githubusercontent.com/github/spec-kit/HEAD/docs/quickstart.md

---

## D15 — Multi-projeto, multi-repo e equipe
Monorepo suportado nativo: cada projeto membro tem próprio .specify/, specs/, constituição. **Nenhuma sincronização automática de doutrina.** Compartilhamento de regras requer manual (duplicação ou link explícito). Variável de env SPECIFY_INIT_DIR facilita CI/CD.

**Fonte:** https://raw.githubusercontent.com/github/spec-kit/HEAD/docs/guides/monorepo.md

---

## D16 — Interação com o humano
Testes de slash commands **exigem intervenção humana** com captura de resultado e documentação de conformidade em PR. Resto é automático (CI gates, análise semântica, geradores de código).

**Fonte:** https://raw.githubusercontent.com/github/spec-kit/HEAD/CONTRIBUTING.md

---

## Práticas Transplantáveis (com custo estimado)

1. **Constituição formalizada com enforcement misto (CI + análise semântica).**  
   Custo: ~40h (definir 3-5 princípios, integrar CI, criar analisador).

2. **SDD como linguagem de projeto (artefatos spec→plan→tasks com gates contínuos).**  
   Custo: ~30h (templates + treino de equipe).

3. **Sistema de catálogos descentralizado para extensibilidade (evita monolito).**  
   Custo: ~20h (esquema catalog.json + integração com descoberta).

---

## Anti-práticas (não copiar)

1. **Ausência de limites de contexto/custo explícitos em framework agnóstico de agentes.**  
   Motivo: Transfere para usuário a responsabilidade de descobrir cutoffs; risco de derrapagem em projetos grandes.

2. **Sincronização manual de doutrina em monorepo.**  
   Motivo: Quebra de contrato frequente; duplicação = divergência.

3. **Enforcement só via CI (sem guardrails em tempo de autoria).**  
   Motivo: Feedback tarde; dev descobre erro após push, não ao escrever.

---

## Dimensões Fora da Grade

- **Workflow engine (não é CLI simples):** Suporta orquestração com steps (command, shell, if_then, do_while, fan_out/in, gate, switch), overlays de composição, expressões. Complexidade significativa não capturada em D1..D16.
- **Integração profunda com 30+ agentes de IA:** Suporta diferentes "linguagens" de contexto (CLAUDE.md, TOML, YAML, Markdown, Skills). Pluralismo incomum.
- **Conceitos-chave de SDD:** Spec-of-specs (tipo system para specs), complex-features (decomposição), seleção de stack **após** spec (inversão de ordem).

---

**Relatório finalizado: 160 linhas | 12 buscas de conteúdo | Sem guardrails estourados.**
