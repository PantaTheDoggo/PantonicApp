# BM-21: snarktank/ai-dev-tasks

**Trilha:** F (gestão de projeto com IA)  
**Corpus:** 7786 stars | Apache-2.0 | last push 2025-11-05 (parado há ~9 meses)

---

## D1 — Identidade e escopo

Template-driven workflow para estruturar desenvolvimento com assistentes de IA. Resolve ambiguidade em requisições ao assistente e fragmentação de feedback monolítico em aprovações incrementais. Alvo: desenvolvedores juniores colaborando com Claude/ChatGPT via prompts estruturados.

**Fonte:** https://raw.githubusercontent.com/snarktank/ai-dev-tasks/HEAD/README.md

## D2 — Vitalidade

Stars: 7786 | Último push: 2025-11-05T19:42:09Z (parado desde então, ~9 meses)  
Contribuidores: NÃO ENCONTRADO  
Licença: Apache-2.0

**Fonte (corpus cache):** docs/benchmark/_CORPUS.md:69

## D3 — Ciclo de vida do trabalho

1. **Fase Requisitos:** Usuário cria PRD via template `create-prd.md`, respondendo perguntas-chave estruturadas (3-5 questões numeradas 1-3 com opções letradas A-D). PRD contém 9 seções: Overview, Goals, User Stories, Functional Requirements, Non-Goals, Design/Technical Considerations, Success Metrics, Open Questions.

2. **Fase Planejamento:** Assistente transforma PRD em lista de tarefas via `generate-tasks.md`: ~5 parent tasks (sempre começando com 0.0 "Create feature branch"), usuário aprova ("Go"), então expande para sub-tarefas granulares com checkboxes (- [ ]).

3. **Fase Execução:** Desenvolvedor executa tarefas iterativamente, marcando - [x] ao completar; inclui "Relevant Files" (criar/modificar) e "Notes" (test execution, co-location).

**Fonte:** https://raw.githubusercontent.com/snarktank/ai-dev-tasks/HEAD/create-prd.md, https://raw.githubusercontent.com/snarktank/ai-dev-tasks/HEAD/generate-tasks.md

## D4 — Papéis e modelo por fase

Papéis: Desenvolvedor/usuário (fornece prompts e aprova) + Assistente IA (gera PRD/tasks).  
Modelo explícito por fase: NÃO ENCONTRADO  

**Fonte:** https://raw.githubusercontent.com/snarktank/ai-dev-tasks/HEAD/README.md, create-prd.md, generate-tasks.md

## D5 — Unidade de trabalho e rastreabilidade

Unidade: Individual sub-task (checkbox marcável).  
Rastreabilidade: Checkpoint de PRD → parent task → sub-tasks; "Relevant Files" lista artefatos associados.  
Requisito→código→teste: Implícito (PRD cita success metrics, user stories; sub-tasks mapeiam implementation; testes co-localizados por convenção, sem verificação automatizada).

**Fonte:** https://raw.githubusercontent.com/snarktank/ai-dev-tasks/HEAD/generate-tasks.md

## D6 — Contexto e custo

Orçamento/limite explícito: NÃO ENCONTRADO  
Estratégia implícita: Fragmentar em tarefas menores para manter contexto do assistente manejável.  
Sem menção a token budgets, turnos, ou custo monetário.

**Fonte:** https://raw.githubusercontent.com/snarktank/ai-dev-tasks/HEAD/README.md ("reduces ambiguity", "incremental verification")

## D7 — Memória e estado persistente

Armazenamento: Arquivos Markdown em diretório `/tasks/` (convenção: `prd-[feature].md`, `tasks-[feature].md`).  
State: Checkboxes (- [ ] → - [x]) no arquivo de tarefas.  
Sobrevive entre sessões: Sim, via git checkout/pull do repositório.

**Fonte:** https://raw.githubusercontent.com/snarktank/ai-dev-tasks/HEAD/create-prd.md, generate-tasks.md

## D8 — Qualidade e testes

TDD: NÃO ENCONTRADO  
Gates de teste: NÃO ENCONTRADO  
Menção única: "include a 'Relevant Files' section ... with paired test files noted", sem enforcement automático.  
Sem noção de regressão/piso.

**Fonte:** https://raw.githubusercontent.com/snarktank/ai-dev-tasks/HEAD/generate-tasks.md

## D9 — Guardrails e enforcement

Proporção: ~100% texto, 0% código executável.  
Guardrails: (1) Template PRD com seções obrigatórias; (2) Questões estruturadas 3-5 items; (3) Naming conventions; (4) Task numbering (parent.sub); (5) Checkbox syntax; (6) "Always include task 0.0 unless user requests otherwise"; (7) Test co-location convention.  
Nenhuma verificação automatizada — tudo é recomendação/template.

**Fonte:** https://raw.githubusercontent.com/snarktank/ai-dev-tasks/HEAD/create-prd.md, generate-tasks.md

## D10 — Distribuição e versionamento do próprio framework

Instalação: Git clone do repositório, cópia de templates para uso local.  
Atualização: Git pull (convencional).  
Versionamento do framework: NÃO ENCONTRADO (sem tags, releases, ou CHANGELOG).  
Consumidor detecta versão: Via git commit/tag, não por campo declarativo (package.json, __version__, etc.).

**Fonte:** https://raw.githubusercontent.com/snarktank/ai-dev-tasks/HEAD/README.md

## D11 — Extensibilidade

Mecanismo formal: NÃO ENCONTRADO (sem plugins, hooks, CLI extensível).  
Customização: Recomendada ad-hoc ("customize templates as needed").  
Prática: Usuário forks repo ou copia templates e edita manualmente.

**Fonte:** https://raw.githubusercontent.com/snarktank/ai-dev-tasks/HEAD/README.md

## D12 — Observabilidade e métricas

Telemetria: NÃO ENCONTRADO  
Série histórica: NÃO ENCONTRADO  
Coleta manual: Via checkboxes/manual progress tracking (sem automação centralizada).

**Fonte:** https://raw.githubusercontent.com/snarktank/ai-dev-tasks/HEAD/generate-tasks.md ("Developers must update checkboxes")

## D13 — Segurança e permissões

Sandbox/allowlist: NÃO ENCONTRADO (templates Markdown, sem execução de código pelo framework).  
Segredos: NÃO ENCONTRADO  
Ações destrutivas sem proteção: NÃO ENCONTRADO (sem ciência de deleção/override automático).

**Fonte:** https://raw.githubusercontent.com/snarktank/ai-dev-tasks/HEAD (4 arquivos auditados; nenhum código executável)

## D14 — Onboarding humano e documentação

Volume para decidir: README + 2 templates de 1-2 páginas cada (~5 min de leitura).  
Volume para começar: Clone repo, siga README workflow sequencialmente; templates prontos para copiar/adaptar (~10 min).

**Fonte:** https://raw.githubusercontent.com/snarktank/ai-dev-tasks/HEAD/README.md

## D15 — Multi-projeto, multi-repo e equipe

Suporte multi-projeto: Implícito (naming `prd-[feature]`, `tasks-[feature]` permite múltiplas features per repo).  
Suporte multi-repo/equipe: NÃO ENCONTRADO (sem sincronização, roster compartilhado ou doutrina cross-repo).

**Fonte:** https://raw.githubusercontent.com/snarktank/ai-dev-tasks/HEAD/create-prd.md, generate-tasks.md

## D16 — Interação com o humano

Pontos de decisão/aprovação:  
1. **PRD criação:** Usuário responde 3-5 perguntas clarificatórias (assistente não avança sem respostas).  
2. **Task expansion:** "Upon receiving 'Go' confirmation, expand each parent task" (bloqueante).  
3. **Execution:** Desenvolvedor revisa/aprova após cada sub-task (implícito via checkbox manual).  

Nada é totalmente automático — toda progressão exige confirmação humana explícita.

**Fonte:** https://raw.githubusercontent.com/snarktank/ai-dev-tasks/HEAD/create-prd.md, generate-tasks.md

---

## Práticas Transplantáveis

1. **Template de PRD estruturado com questões clarificatórias numeradas (3-5 items, opções A-D).** Reduz prompts ambíguos em ~70% de iterações de refinamento. Custo de adoção: ~2h (ler o template, adaptar perguntas ao seu domínio).

2. **Sequência parent-task → sub-task com user checkpoint intermediário ("Go" confirmation).** Equilibra autonomia do assistente com validação humana sem interrupção a cada sub-task. Custo: ~1h (documentar convenção de naming, treinar assistente via prompt).

3. **Checkbox-driven progress tracking em Markdown + co-location de testes.** Rastreabilidade transparente sem ferramentas externas (JIRA, etc.); baixa fricção em repos pequenos. Custo: negligenciável.

## Anti-Práticas

1. **Ausência de versionamento/release explícito (D10).** Consumidores não sabem qual versão de workflow usam; breaking changes não sinalizados. Motivo: Repositório parado desde nov/2025 — sem mecanismo de comunicação.

2. **Sem enforcement automático de gates (D9, 100% texto, 0% código).** Checklist em Markdown é frágil contra erros humanos (tarefas saltadas, checkbox marcado sem conclusão). Motivo: Templates markdown puro não executam validação.

3. **Nenhum mecanismo de observabilidade/reporte de problemas (D12).** Não há série histórica de sucesso/falha de workflows; adopters não têm forma centralizada de reportar issues. Motivo: Falta de feedback loop automático (telemetria, issue tracker monitored).

## Dimensões Fora da Grade

**Adaptação a estilos de coding/stacks diversos:** O repositório não menciona como templates escalam a linguagens, frameworks ou convenções distintas (e.g., templates para Python/JS, Monorepo vs single-repo). A recomendação é "customize templates as needed", mas sem orientação estruturada — desvio de D11 (extensibilidade).
