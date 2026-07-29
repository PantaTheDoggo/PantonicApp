# BM-03: Fission-AI/OpenSpec — Benchmarking Report

## D1 — Identidade e escopo

Framework de especificação leve que funciona como camada intermediária entre humanos e assistentes de IA durante o desenvolvimento. Resolve a imprecisão inerente ao trabalho com IA quando requisitos vivem apenas no histórico de chat. Público: desenvolvedores em projetos pessoais até empresas que trabalham com IA para geração de código.

https://raw.githubusercontent.com/Fission-AI/OpenSpec/HEAD/README.md

## D2 — Vitalidade

**Stars:** 62995  
**Último push:** 2026-07-29T01:31:26Z  
**Contribuidores:** NÃO ENCONTRADO  
**Licença:** MIT

Fonte dos metadados: cache do `V2B-T3` — `docs/benchmark/_CORPUS.md` (linha 47).

## D3 — Ciclo de vida do trabalho

5 fases sequenciais: Start Change (estrutura folder) → Create Artifacts (proposal, specs, design, tasks) → Implement Tasks (execução com refinamento) → Verify Work (validação) → Archive Change (merge de specs e arquivo). Artefatos são "enablers, not gates" — não há fase gates obrigatórias. Filosofia: "fluid not rigid", "iterative not waterfall".

https://raw.githubusercontent.com/Fission-AI/OpenSpec/HEAD/docs/concepts.md

## D4 — Papéis e modelo por fase

Papéis implícitos: Propositor (drafta), Revisor (valida), Integrador (merge). **Sem escolha explícita de modelo IA por fase.** OpenSpec é ferramenta, não agente — humano controla interações com IA.

https://raw.githubusercontent.com/Fission-AI/OpenSpec/HEAD/docs/team-workflow.md

## D5 — Unidade de trabalho e rastreabilidade

Unidade: uma **change** com um propósito claro ("one intent you can say in a sentence"). Rastro spec→teste existe via GIVEN/WHEN/THEN em specs. **Rastro spec→código não é rastreado explicitamente** — código fica em design.md ou versionado separadamente.

https://raw.githubusercontent.com/Fission-AI/OpenSpec/HEAD/docs/writing-specs.md

## D6 — Contexto e custo

NÃO ENCONTRADO. Sem limite explícito de contexto, turnos ou dinheiro. Design de "delta specs" sugere eficiência (descrever diff, não destino), mas sem quantificação.

## D7 — Memória e estado persistente

**Specs/ no openspec/** — "source of truth" versionado que sobrevive entre sessões. Specs descrevem "how your system behaves *right now*" e são compartilhadas entre humano e IA.

https://raw.githubusercontent.com/Fission-AI/OpenSpec/HEAD/docs/overview.md

## D8 — Qualidade e testes

TDD **não mencionado**. Artefatos (specs, design) funcionam como "enablers" de teste, não obrigatórios. Cenários GIVEN/WHEN/THEN em specs "*could become* an automated test" (aspiracional, não garantido). **Sem gates de teste** entre fases.

## D9 — Guardrails e enforcement

**~85% código executável**, ~10% configuração YAML, ~5% mensagens. CI com 9 jobs: testes em 3 plataformas (Linux/macOS/Windows), lint+tipagem, validação changeset, workflows de release. Regras são pipeline automatizado, não checklist manual.

https://raw.githubusercontent.com/Fission-AI/OpenSpec/HEAD/.github/workflows/ci.yml

## D10 — Distribuição e versionamento do próprio framework

**Semver** (v1.7.0 mais recente). Distribuição via npm. Consumidor: instala via `npm install`, verifica versão incorporada, atualiza com comando do CLI.

https://raw.githubusercontent.com/Fission-AI/OpenSpec/HEAD/CHANGELOG.md

## D11 — Extensibilidade

Três mecanismos: **(1) Project config** (openspec/config.yaml — injetar contexto/regras), **(2) Custom schemas** (openspec schema init — artefatos novos sem forkar), **(3) Community schemas** (repositórios mantidos externamente). **Sem plugins dinâmicos, skills customizadas ou hooks formais.**

https://raw.githubusercontent.com/Fission-AI/OpenSpec/HEAD/docs/customization.md

## D12 — Observabilidade e métricas

NÃO ENCONTRADO. Sem telemetria de consumo ou série histórica de qualidade. Telemetria geral do tool é desabilitável (OPENSPEC_TELEMETRY=0), sem captura de credenciais.

## D13 — Segurança e permissões

**Sem sandbox explícito** — ferramenta CLI local, opera com permissões do usuário (sem escalonamento). Ações destrutivas requerem consentimento. Telemetria desabilitável, nenhuma captura de IP/arquivo/hostname.

https://raw.githubusercontent.com/Fission-AI/OpenSpec/HEAD/SECURITY.md

## D14 — Onboarding humano e documentação

**2 min setup**, ~20 min primeira mudança, 30 min conhecimento funcional. "Your First Five Minutes" com 6 linhas de código. Documentação por tarefa (explore, review, write-specs), aprendizado incremental. Opcional: delegar setup à IA.

https://raw.githubusercontent.com/Fission-AI/OpenSpec/HEAD/docs/getting-started.md

## D15 — Multi-projeto, multi-repo e equipe

Specs/ no repositório principal (versionado). Convenções compartilhadas, não doutrina imposta. Cada projeto mantém suas convenções via arquivo, equipes sincronizam via git.

https://raw.githubusercontent.com/Fission-AI/OpenSpec/HEAD/docs/team-workflow.md

## D16 — Interação com o humano

**3 gates humanos obrigatórios:** validação de escopo (proposal), definição de "pronto" (delta specs), merge (código+specs juntos). Modelo deliberadamente humano-cêntrico — IA nunca decide, só acessa contexto.

---

## Práticas Transplantáveis

1. **Separação de specs (requisitos) de design (implementação)** — força clareza, permite iterar specs sem reeditar código. Custo: ~1 dia treinar equipe que não é waterfall.

2. **Artefatos versionados como "source of truth" persistente** — elimina inconsistência chat/código, cria série histórica. Custo: ~10 min de "archive" por mudança.

3. **Gates humanos explícitos em 3 pontos** (escopo, def de pronto, merge) — força revisão sem bloquear iteração. Custo: ~5 min por review.

## Anti-Práticas

1. **Ausência de TDD ou gates de teste obrigatórios** — nenhuma fase força testes automatizados. Risco: qualidade degradada com alta rotatividade de features.

2. **Sem limite explícito de contexto/custo** — delta specs é boa ideia, mas sem orçamento visível, conversas crescem indefinidamente. Risco: token waste.

3. **Zero suporte a IA automática em decisões críticas** — sem sugestão de specs por análise de código, sem sugestão de testes por specs. Limita IA ao acesso a contexto.

## Dimensões Fora da Grade

- **Governance de conflito em specs compartilhadas**: Como resolver merge conflicts quando múltiplos PRs modificam specs/ simultaneamente? Não abordado.
- **Tratamento de código legacy sem spec de origem**: OpenSpec assume specs "right now", mas código antigo provavelmente não tem origem spec. Não documentado.
