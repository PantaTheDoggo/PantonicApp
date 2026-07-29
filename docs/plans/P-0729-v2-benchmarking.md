# P-0729 — V2 / Estágio 1: benchmarking de frameworks públicos de governança e gestão de projetos com IA

**Iniciativa:** `PANTONIC-V2` (consolidação do framework — 4 estágios encadeados).
**Origem:** pedido do dono (2026-07-29). Dor declarada: o framework PantonicApp cresceu por
acúmulo de decisões internas (skills, agentes, guardrails, procedimentos, golden rules) sem nunca
ter sido confrontado com o que existe publicamente. Meta deste estágio: **produzir evidência
comparável** — não opinião — sobre como os frameworks públicos mais conhecidos resolvem os mesmos
problemas, e **descobrir dimensões que o Pantonic não considerou**.

**Planejador:** Opus (2026-07-29). **Executor por tarefa:** declarado em cada `T*` — coleta em
Haiku (é o objetivo declarado do dono), mecânica em Sonnet, nenhuma tarefa deste estágio em Opus.

**Estado:** `backlog` — fechado e linear, pronto para execução. Nenhuma decisão pendente (§7).

**Checagem de versão do kit (GOVERNANCA §10b):** PantonicApp é o **hub** — resolve em modo hub
(`.claude/KIT_VERSION` = `1.0.1`, sem `.claude/kit/`). Não há consumidor a comparar; o hub é o
canônico. Sem divergência.

**Relação com os demais planos da iniciativa:** este é o **único plano vivo** da `PANTONIC-V2`
enquanto não fechar. Os estágios 2, 3 e 4 (`P-0729-v2-confronto`, `P-0729-v2-melhoria`,
`P-0729-v2-documentacao`) nascem `blocked` com razão *"depende do estágio anterior `done`"* e não
são escolhíveis pela `proximo-passo` até este fechar — convergência de iniciativa preservada
(skill `diario-de-obras`, "Planos derivados", caso C).

---

## 0. Escopo

**Em escopo:** validar um corpus de ~20 repositórios públicos; emitir um relatório por repositório
em **esquema fixo de 16 dimensões**; publicar índice e controle de qualidade do corpus. Instituir o
**controle de versão do framework** (infraestrutura de toda a iniciativa — T1).

**Fora de escopo:** qualquer juízo comparativo sobre o PantonicApp (é o Estágio 2), qualquer
alteração de doutrina, agente, skill ou guardrail (é o Estágio 3), e o README (Estágio 4). Um
relatório de benchmarking que opina sobre o Pantonic está **fora do esquema** e é reprovado no T8.

## 1. Sonda de viabilidade do mecanismo de coleta (medida 2026-07-29)

`GOVERNANCA.md` §3 exige que a decisão de mecanismo de plataforma venha com a sonda, não depois.
Medido nesta máquina, antes de escolher:

| Sonda | Resultado medido |
|---|---|
| `Get-Command gh` | **não instalado** — nada da coleta pode depender do GitHub CLI |
| `GET https://api.github.com/rate_limit` | HTTP 200; `limit: 60`, `remaining: 60` — **60 req/h por IP, sem autenticação** |

**Consequência dimensionada:** 20 repos × ~10 leituras = ~200 requisições — **estoura a cota 3×
numa hora**. Logo o mecanismo é obrigatoriamente híbrido:

- **`api.github.com` (cota escassa, 60/h):** só para o que não existe fora dela — metadados
  (`/repos/{o}/{r}`: stars, `pushed_at`, licença, descrição) e a árvore de arquivos
  (`/repos/{o}/{r}/git/trees/HEAD?recursive=1`). **2 chamadas por repositório, uma única vez**, no
  T3, gravadas em disco. Orçamento: 20 × 2 = **40 requisições**, dentro dos 60/h se feitas na mesma
  janela. Se o T3 receber HTTP 403/429, **para e reporta** — não continua meia-coleta.
- **`raw.githubusercontent.com` (sem cota de API):** todo conteúdo de arquivo, via
  `https://raw.githubusercontent.com/{o}/{r}/HEAD/{path}`. É onde ocorrem ~90% das leituras, e é
  por isso que a árvore é cacheada antes: o coletor escolhe o caminho exato em disco e busca direto,
  sem navegar.
- **Proibido:** `git clone` do corpus (custo de disco e tempo desproporcional ao que se lê) e
  qualquer coleta que dependa de raspar HTML do github.com (frágil).

## 2. Corpus candidato (6 trilhas, 24 candidatos → cortar para 20 no T3)

Os `owner/repo` abaixo são **candidatos**, escritos a partir do conhecimento do planejador e
portanto **suspeitos de estar desatualizados ou errados**. O T3 confirma cada um contra a API
(existe? é este o owner? stars? último push?) e **corta, corrige ou substitui** — um candidato que
não confirmar não entra no corpus e a substituição é registrada. Nenhum relatório é emitido sobre
repositório não confirmado.

| # | Trilha | Candidato | Por que está no corpus |
|---|---|---|---|
| 1 | A — dev agêntico spec-driven | `github/spec-kit` | Spec-Driven Development mantido pelo GitHub; concorrente direto dos "4 artefatos" |
| 2 | A | `bmad-code-org/BMAD-METHOD` | Papéis agênticos (PM/Arquiteto/Dev/QA) e handoff entre eles |
| 3 | A | `buildermethods/agent-os` | Camadas de padrões/produto/spec; instruções versionadas |
| 4 | A | `Fission-AI/OpenSpec` | Proposta de mudança como unidade de trabalho |
| 5 | A | `eyaltoledano/claude-task-master` | Decomposição em tarefas atômicas + dependências |
| 6 | A | `SuperClaude-Org/SuperClaude_Framework` | Comandos/personas/modos como framework instalável |
| 7 | B — doutrina de fornecedor | `anthropics/claude-code` (docs) | Subagentes, hooks, skills, CLAUDE.md — a plataforma que o Pantonic usa |
| 8 | B | `anthropics/skills` | Formato canônico de skill e progressive disclosure |
| 9 | B | padrão `AGENTS.md` (`openai/agents.md`) | Convenção multi-fornecedor de instrução de repo |
| 10 | B | `github/awesome-copilot` | `instructions`/`chatmodes`/`prompts` versionados por repo |
| 11 | B | `google-gemini/gemini-cli` | Mecanismo alternativo de instrução e extensões |
| 12 | C — regras, memória, contexto | `PatrickJS/awesome-cursorrules` | Volume e padrões de regra por stack |
| 13 | C | `cline/cline` (Memory Bank / `.clinerules`) | Memória persistente entre contextos — dimensão fraca no Pantonic |
| 14 | C | `coleam00/context-engineering-intro` | PRP: dossiê de tarefa autocontido |
| 15 | C | `davidkimai/Context-Engineering` | Teoria de orçamento e compressão de contexto |
| 16 | C | `steipete/agent-rules` | Regras portáveis entre ferramentas |
| 17 | D — princípios e arquitetura | `humanlayer/12-factor-agents` | Princípios de fatoração de agente; contraponto direto à doutrina |
| 18 | D | `hesreallyhim/awesome-claude-code` | Superfície do ecossistema (o que existe e o Pantonic ignora) |
| 19 | D | `disler/claude-code-hooks-mastery` | Hooks como enforcement executável de guardrail |
| 20 | D | `wshobson/agents` | Coleção madura de subagentes especializados |
| 21 | E — guardrails de runtime e avaliação | `guardrails-ai/guardrails` | Guardrail como validação executável, não como texto |
| 22 | E | `NVIDIA/NeMo-Guardrails` | Política declarativa de comportamento |
| 23 | E | `promptfoo/promptfoo` | Regressão/avaliação de prompt — análogo do piso de regressão |
| 24 | F — gestão de projeto com IA | `sdi2200262/agentic-project-management` | Gestão de projeto multi-agente com handover explícito |
| 25 | F | `Wirasm/PRPs-agentic-eng` | Pacote requisito→execução pronto para handoff |

**Critério de corte para 20:** manter no mínimo 3 por trilha; entre candidatos da mesma trilha,
preferir o de maior atividade recente (`pushed_at`) sobre o de mais stars — framework parado
documenta uma prática morta.

## 3. Esquema fixo do relatório (as 16 dimensões)

Todo relatório usa **exatamente** estas 16 dimensões, nesta ordem, com estes títulos. É o que torna
20 relatórios de Haiku confrontáveis em um único passe de Opus no Estágio 2 — e é a grade da matriz
de cobertura (`P-0729-v2-confronto` T2). Dimensão sem evidência recebe literalmente
`NÃO ENCONTRADO`, nunca inferência.

| id | Dimensão | O que responder |
|---|---|---|
| D1 | Identidade e escopo | O que é, que problema resolve, para que tipo de projeto |
| D2 | Vitalidade | Stars, último push, nº de contribuidores, licença (do cache do T3) |
| D3 | Ciclo de vida do trabalho | Fases, artefatos produzidos em cada uma, gates entre elas |
| D4 | Papéis e modelo por fase | Que agentes/papéis existem; há escolha explícita de modelo por fase? |
| D5 | Unidade de trabalho e rastreabilidade | O que é "uma tarefa"; existe rastro requisito → código → teste? |
| D6 | Contexto e custo | Há orçamento/limite explícito de contexto, turnos ou dinheiro? Como? |
| D7 | Memória e estado persistente | O que sobrevive entre sessões e onde vive |
| D8 | Qualidade e testes | TDD? Gates de teste? Noção de regressão/piso? |
| D9 | Guardrails e enforcement | As regras são texto, checklist, ou **código executável**? Qual proporção? |
| D10 | Distribuição e versionamento do próprio framework | Como o consumidor instala, atualiza e sabe a versão que tem |
| D11 | Extensibilidade | Plugins, skills, comandos, hooks — como se estende sem forkar |
| D12 | Observabilidade e métricas | Telemetria de consumo/qualidade; existe série histórica? |
| D13 | Segurança e permissões | Sandbox, allowlist, segredos, ações destrutivas |
| D14 | Onboarding humano e documentação | Quanto um humano precisa ler para decidir e para começar |
| D15 | Multi-projeto, multi-repo e equipe | Vários projetos/pessoas compartilham a doutrina? Como? |
| D16 | Interação com o humano | Onde o humano aprova, decide, é consultado; o que nunca é automático |

**Rodapé obrigatório de todo relatório**, além das 16 dimensões:
- **3 práticas transplantáveis** — cada uma com o custo estimado de adoção.
- **3 anti-práticas** — o que este framework faz que seria um erro copiar, com o motivo.
- **Dimensões fora da grade** — qualquer preocupação relevante deste framework que **não** cabe em
  D1..D16. Este campo é o principal instrumento de descoberta pedido pelo dono; "nenhuma" é
  resposta válida, mas nunca é resposta automática.

## 4. Guardrails do coletor (o Haiku é barato e crédulo — estas regras são o preço)

1. **Evidência ou `NÃO ENCONTRADO`.** Toda afirmação carrega a URL exata (arquivo, não repositório)
   de onde saiu. Sem URL, a linha não existe.
2. **Proibido responder de memória de treino.** Se a informação não estiver no que foi buscado
   nesta execução, é `NÃO ENCONTRADO` — inclusive para repositórios famosos.
3. **Teto de 12 buscas de conteúdo por repositório** e **relatório ≤ 160 linhas**. Estourar é sinal
   de repositório mal escolhido: para e reporta, não continua.
4. **Ordem de leitura prescrita** (evita vagar): `README` → árvore cacheada (escolher 3-6 caminhos
   de doutrina: `docs/`, `.github/`, `AGENTS.md`, `CLAUDE.md`, `*.instructions.md`, `commands/`,
   `agents/`) → `CHANGELOG`/releases se D10 ainda estiver vazia.
5. **Sem juízo sobre o Pantonic** (§0) e **sem prosa de recomendação** — o coletor descreve, o
   Estágio 2 julga.
6. **Um repositório por subagente.** Nunca dois no mesmo contexto (Regra 2 do CLAUDE.md aplicada à
   coleta: dois repos no mesmo contexto contaminam as descrições um do outro).

## 5. Tarefas

### T1 — Instituir o controle de versão do framework [Sonnet]
- **Objetivo:** dar à iniciativa o instrumento de versão que o dono pediu ("um V2 ao término"),
  antes de qualquer mudança que precise ser versionada.
- **Arquivos-alvo:** `VERSION` (novo, raiz), `.claude/KIT_VERSION`, `CHANGELOG.md` (novo, raiz),
  `GOVERNANCA.md` §10 (parágrafo novo ao final, sem reescrever o existente).
- **Regra a instituir (decidida em §7 / DV-1, apenas materializar):** `VERSION` (framework:
  doutrina + kit) e `.claude/KIT_VERSION` (o que o subtree publica) carregam **sempre o mesmo
  valor** — divergência entre eles é defeito, não estado válido. Semver com significado declarado:
  **MAJOR** = exige ação do consumidor (artefato removido/renomeado, doutrina invertida); **MINOR**
  = artefato ou guardrail novo compatível; **PATCH** = correção redacional. Toda tarefa que edite
  `.claude/` ou a doutrina bumpa os dois arquivos **e** escreve uma linha no `CHANGELOG.md`.
- **Valor inicial:** `1.1.0` nos dois arquivos (MINOR: o kit ganha o esquema de versão; `1.0.1`
  segue sendo a última tag publicada até o fim desta tarefa).
- **Testes:** N/A (não há suíte no hub). Verificação: `Get-Content VERSION` e
  `Get-Content .claude/KIT_VERSION` devolvem o mesmo valor.
- **Pronto quando:** os dois arquivos existem e coincidem em `1.1.0`; `CHANGELOG.md` tem a seção
  `1.1.0` com a linha desta mudança; `GOVERNANCA.md` §10 descreve a regra dos dois arquivos e o
  significado de MAJOR/MINOR/PATCH; tag anotada `kit-v1.1.0` criada (prática vigente das tags
  `kit-v1.0.0`/`kit-v1.0.1`).

### T2 — Agente `pantonic-benchmarker` e materialização do esquema [Sonnet]
- **Objetivo:** criar o coletor reusável de benchmarking (a campanha se repete; um prompt colado à
  mão não se repete) e fixar o esquema em disco.
- **Arquivos-alvo:** `.claude/agents/pantonic-benchmarker.md` (novo),
  `docs/benchmark/_ESQUEMA.md` (novo), `.claude/README.md` (linha na tabela de agentes),
  `VERSION` + `.claude/KIT_VERSION` + `CHANGELOG.md` (bump para `1.2.0`).
- **Conteúdo do agente:** frontmatter `model: haiku`, `tools: Read, Write, Glob, Grep, WebFetch`
  (sem Bash, sem Edit — coletor não altera o repositório além do próprio relatório); corpo = §3
  (esquema) + §4 (guardrails) + §1 (mecanismo: raw para conteúdo, nunca `api.github.com`, cuja cota
  já foi gasta no T3) deste plano, transcritos, mais o caminho de saída
  `docs/benchmark/BM-<NN>-<slug>.md`.
- **Pronto quando:** o agente existe e é invocável; `_ESQUEMA.md` contém D1..D16 e o rodapé
  obrigatório; `.claude/README.md` lista o agente novo; os dois arquivos de versão em `1.2.0` com
  linha no CHANGELOG e tag `kit-v1.2.0`.

### T3 — Curadoria e cache do corpus [Sonnet orquestrando; 1 janela de API]
- **Objetivo:** transformar os 25 candidatos de §2 em **20 repositórios confirmados**, com
  metadados e árvore de arquivos em disco, gastando a cota de 60 req/h uma única vez.
- **Arquivos-alvo:** `docs/benchmark/_CORPUS.md` (novo — tabela: `#`, trilha, `owner/repo`, stars,
  `pushed_at`, licença, status `confirmado`/`substituído`/`cortado`, motivo),
  `docs/benchmark/_trees/<slug>.txt` (20 arquivos, árvore recursiva).
- **Método:** 2 chamadas por candidato (`/repos/{o}/{r}` e `/git/trees/HEAD?recursive=1`), na mesma
  janela, **contando as requisições**; parar em 55 e reportar o restante. Candidato que devolva 404
  é corrigido por uma busca (`WebSearch`) e reconfirmado, ou cortado com motivo registrado.
- **Pronto quando:** `_CORPUS.md` tem exatamente 20 linhas `confirmado`, cada uma com stars e
  `pushed_at` datados de hoje, cobrindo as 6 trilhas com ≥3 cada; existem 20 arquivos em `_trees/`;
  toda substituição/corte tem motivo escrito.

### T4 — Relatórios do lote 1 (repos 1-5) [Haiku, 5 subagentes `pantonic-benchmarker` em paralelo]
- **Objetivo:** emitir `docs/benchmark/BM-01..BM-05` conforme o esquema.
- **Método:** um subagente por repositório, despachados na mesma mensagem; cada prompt carrega
  apenas `owner/repo`, o caminho da árvore cacheada e o caminho de saída — o esquema e os
  guardrails já vivem no arquivo do agente (dieta de prompt).
- **Pronto quando:** 5 arquivos existem, cada um com D1..D16 preenchidas (ou `NÃO ENCONTRADO`),
  rodapé completo, ≤160 linhas, e nenhuma afirmação sem URL de arquivo.

### T5 — Relatórios do lote 2 (repos 6-10) [Haiku] — idem T4
### T6 — Relatórios do lote 3 (repos 11-15) [Haiku] — idem T4
### T7 — Relatórios do lote 4 (repos 16-21) [Haiku] — idem T4, com **6** subagentes
O lote 4 carrega o `BM-21` acrescentado pela ampliação do corpus (ver "Achados da execução").

### T8 — Controle de qualidade e índice do corpus [Sonnet]
- **Objetivo:** garantir que o Estágio 2 receba 21 relatórios **comparáveis** — um relatório fora do
  esquema envenena a matriz e o consolidado.
- **Arquivos-alvo:** `docs/benchmark/INDICE.md` (novo), reemissão de relatórios reprovados.
- **Checklist de reprovação (qualquer item reprova):** dimensão ausente ou renomeada; afirmação sem
  URL; URL apontando para o repositório em vez do arquivo; relatório > 160 linhas; juízo sobre o
  PantonicApp; rodapé incompleto; "Dimensões fora da grade" ausente.
- **Pronto quando:** 21/21 aprovados; `INDICE.md` lista os 21 com trilha, `owner/repo`, veredito do
  QC e as "dimensões fora da grade" agregadas numa lista única (o insumo mais valioso do estágio);
  este plano fecha e o Estágio 2 é destravado no diário.

## 6. Riscos

- **Cota de 60 req/h estourada por retrabalho no T3** (candidatos errados forçando rebuscas).
  Mitigação: cortar em vez de insistir; o corte fica registrado e a trilha só precisa de 3 repos.
- **Haiku alucinando doutrina de repositório famoso** — o risco dominante deste estágio, porque a
  saída *parece* correta. Mitigação: §4.1/§4.2 (URL por afirmação, proibição explícita de memória)
  + o QC do T8, que é adversarial por desenho e reprova sem negociar.
- **Esquema virar leito de Procusto** — framework cuja preocupação central não cabe em D1..D16
  sendo descrito pobremente. Mitigação: o campo "Dimensões fora da grade" existe exatamente para
  isso e é obrigatório.
- **Repositório grande demais para 12 buscas** (ex.: `awesome-*` com centenas de arquivos).
  Mitigação: a árvore cacheada permite escolher os caminhos antes de buscar; para coleções, ler o
  README e 2-3 exemplares, não o acervo.

## 7. Decisões (fechadas no planejamento — G-PLANREADY)

| id | Decisão | Valor | Motivo |
|---|---|---|---|
| **DV-1** | Esquema de versão do framework | `VERSION` (raiz) + `.claude/KIT_VERSION` com **o mesmo valor**; semver com MAJOR/MINOR/PATCH definidos em T1 | O subtree só publica o prefixo `.claude/`, mas a doutrina vive fora dele — dois arquivos são inevitáveis; um número só elimina a ambiguidade de "qual é a versão" |
| **DV-2** | Onde a campanha começa a numeração | Framework em `1.0.1` hoje → `1.1.0` (T1) → `1.2.0` (T2); Estágios 1-2 não bumpam além disso | Relatório de benchmarking é evidência, não framework — não muda o que o consumidor consome |
| **DV-3** | Tamanho do corpus | ~~20~~ **21** repositórios, ≥3 por trilha (decisão do dono, 2026-07-29; **emendada no mesmo dia** de 20 para 21 pelo dono, para tornar o piso de 3 atingível na trilha F — ver "Achados da execução") | Cobertura suficiente para descoberta de dimensões sem inflar custo |
| **DV-4** | Mecanismo de coleta | Híbrido: `api.github.com` só para metadados/árvore em lote (T3); conteúdo por `raw.githubusercontent.com` | Medido: `gh` ausente e cota de 60 req/h (§1) |
| **DV-5** | Coletor é agente do kit, não prompt avulso | `pantonic-benchmarker` em `.claude/agents/` | A campanha se repete; e o esquema precisa estar fora do prompt para não derivar entre lotes |
| **DV-6** | Sequenciamento com o Estágio 3 | Estágios 1-2 correm agora (só escrevem em `docs/benchmark/`); o P-0722 foi **mesclado** ao Estágio 3 por decisão do dono | Nenhum conflito de arquivo com a doutrina; ver `P-0729-v2-melhoria` §1 |

## Achados da execução

- **`V2B-T3` (2026-07-29) — trilha F abaixo do piso de 3 (DV-3).** A tabela de 25 candidatos em
  §2 sempre teve só **2** candidatos para a trilha F (gestão de projeto com IA — `#24
  sdi2200262/agentic-project-management`, `#25 Wirasm/PRPs-agentic-eng`). O critério de corte de
  §2 (min. 3 por trilha) é estruturalmente impossível de cumprir para F com o pool dado — não há
  um 6º candidato de F para preferir por `pushed_at`, nem um substituto para um eventual 404
  (Fase B do T3 só autoriza WebSearch para reconfirmar 404, não para descobrir candidato novo).
  Resolução aplicada em `docs/benchmark/_CORPUS.md`: os 2 disponíveis de F foram mantidos
  `confirmado` (`BM-19`, `BM-20`); os 20 confirmados fecham com A=4, B=4, C=4, D=3, E=3, F=2.
  **RESOLVIDO no mesmo dia, antes do `V2B-T4`** (e não no `V2B-T8` como proposto acima: a
  numeração `BM-*` congela assim que o primeiro relatório é emitido, então mexer no corpus depois
  obrigaria a renumerar). **Decisão do dono, 2026-07-29:** ampliar o corpus de 20 para **21**
  repositórios — rota (c), que não estava entre as duas propostas: nenhuma trilha perde um
  confirmado e F sobe a 3. Terceiro candidato escolhido pelo orquestrador entre 4 sondados:
  `snarktank/ai-dev-tasks` (`BM-21`), com a tensão de estagnação declarada em `_CORPUS.md`.
  **Emenda à `DV-3`:** tamanho do corpus passa a **21**; o piso de ≥3 por trilha permanece e agora
  é cumprido em A–F. `V2B-T7` emite um relatório a mais (`BM-21`) e o `V2B-T8` valida **21/21**.
