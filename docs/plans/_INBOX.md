# Inbox de planos — PantonicApp (hub de governança) — append-only

Cada linha aponta para um `docs/plans/P-<MMDD>-<slug>.md`. Uma vez promovido ao índice/heading do
diário de obras do PantonicApp (a ser criado na Fase 5 de P-0721-governanca-single-source), a linha
é marcada `[drenado]` e permanece aqui — nunca é apagada.

- 2026-07-21 — `P-0721-governanca-single-source` — PantonicApp como repositório de referência da
  governança comum Pantonic*: kit executável (7 skills + agentes) deixa de ser copiado em cada
  filho e passa a ser herdado do canônico via `~/.claude`; filhos guardam só o específico +
  ponteiros; docs comuns (`GOVERNANCA.md`/`ARQUITETURA_PANTONICA.md`) formalizados como ponteiro.
  DP-1..DP-6 owner-gated. **Enfileirado após o fechamento de `SPRINT-SUBSWAPLAG` do PantonicVideo**
  (prioridade do dono 2026-07-21: correção da aplicação primeiro). Não promovido — plano registrado,
  não iniciado.
- 2026-07-22 — `P-0722-governanca-guardrails-anti-saga` — guardrails de doutrina extraídos do
  episódio "saga de legendas" do PantonicVideo (auditoria 2026-07-22), para o radar de todo agente
  Pantonic\*: **G-DEADCODE** (proibição de código morto testado — ~300 linhas foram o gatilho),
  **G-PLANFIDELITY** (executor não troca a rota arquitetural do plano; escala ao dono),
  **G-PREMISE** (premissa que embasa abandono de rota exige spike, não asserção), e skill global
  **`modelo-por-fase`** (operacionaliza §3: intelectual→Opus, execução→Sonnet, leitura→Haiku).
  Concern distinto do SGSS (doutrina, não distribuição); ratificado, entra em `GOVERNANCA.md` e o
  SGSS distribui. Decisões DP-G1..DP-G4 resolvidas 2026-07-22 (todas conforme recomendação); hook de
  modelo-por-fase já prototipado; não iniciado (aguarda "go").
- 2026-07-25 — `P-0725-governanca-tres-camadas` — redefinição do conjunto governado por decisão do
  dono: `PantonicApp` (base, sempre), `PantonicContainer` (só se containerizado) e
  `PantonicContainerForAWS` (só se container na AWS) são **três camadas condicionais de
  governança**; os demais Pantonic\* são consumidores e saem do escopo. Prepara os dois filhos para
  subir ao GitHub (varredura de credenciais → `.gitattributes`/LF → snapshot fiel → publicação) e
  extrai o delta por camada. **Rebaseia o P-0721** (§5): Fase 4 `superseded`, DP-8 encerrado, Fase 3
  preservada. **DP-9 owner-gated e bloqueante**: medido que a camada 3 não tem conteúdo AWS próprio
  (13/17 artefatos byte-idênticos ao Container; os 4 restantes são só rebordo de linha).
  **SUPERSEDED no mesmo dia** por `P-0725-governanca-hub-unico` — ver linha abaixo.
- 2026-07-25 — `P-0725-governanca-hub-unico` — segunda simplificação do dono no mesmo dia:
  `ContainerForAWS` **abortado** (não tinha conteúdo próprio), `Container` **congelado como
  legado**, escopo restrito a **`PantonicApp` como hub único** com **`PantonicVideo` como prova de
  aceitação** (o projeto mais maduro: se a transição não quebrar nem causar perda nele, a
  governança nova está aceita). Medido: só 5 artefatos são compartilhados hub×Video — 3 skills
  quase sincronizadas (~15 linhas de deriva) e 2 overrides legítimos por desenho
  (`guardrails-check`, `pantonic-executor`). Inclui **regra nova**: `KIT_VERSION` + tag
  `kit-v<N>` no hub, checagem de divergência na criação de todo plano, **atualização só por
  comando do usuário**. **DP-12 fechada 2026-07-25** conforme recomendação (todos os 11 artefatos
  só-do-hub são aceitos, exceto `integrar-poc`, que colide com o pipeline de POC local).
  **Em execução:** Fases 1-3 `done` em 2026-07-25/26 (hub publicado, tag `kit-v1.0.0`). **Fase 3b
  aberta em 2026-07-26** pela avaliação do arquiteto: o `sync-kit.ps1` (T1 do P-0721) caiu no vão
  quando o §5 absorveu a Fase 3 daquele plano em bloco, e `kit-v1.0.0` saiu sem o materializador —
  a 3b autora o script conforme o T1, prova em sandbox e republica como `kit-v1.0.1`. Só então a
  Fase 4 (prova de aceitação no PantonicVideo) é delegável.
- **[drenado]** 2026-07-29 — `P-0729-v2-benchmarking` — **Estágio 1 da iniciativa `PANTONIC-V2`**
  (consolidação do framework, pedido do dono 2026-07-29). Benchmarking de **20 repositórios
  públicos** de governança/gestão de projetos com IA, em 6 trilhas, um relatório por repo em
  **esquema fixo de 16 dimensões (D1..D16)**, emitidos por subagentes **Haiku**
  (`pantonic-benchmarker`, criado no T2). Inclui a **infraestrutura de versão da iniciativa** (T1:
  `VERSION` + `.claude/KIT_VERSION` com o mesmo valor + `CHANGELOG.md`). Mecanismo de coleta
  decidido por sonda medida no mesmo dia (`gh` ausente; API do GitHub a 60 req/h ⇒ metadados em
  lote cacheado + conteúdo por `raw.githubusercontent.com`). `backlog` — único plano vivo da
  iniciativa.
- **[drenado]** 2026-07-29 — `P-0729-v2-confronto` — **Estágio 2**: auto-retrato do PantonicApp no
  mesmo esquema (`BM-00`), matriz de cobertura 16×21, **relatório consolidado em Opus** (forças,
  fraquezas, **dimensões novas D17+**, descartes justificados, vieses do corpus) e backlog de
  candidatos `C-NN` **ratificado pelo dono** antes do Estágio 3 existir. Só escreve em
  `docs/benchmark/`. `blocked` — depende do Estágio 1 `done`.
- **[drenado]** 2026-07-29 — `P-0729-v2-melhoria` — **Estágio 3**: implementa os candidatos
  ratificados e **absorve o `P-0722` tarefa a tarefa** (§1 — mapa completo das 4 fases + DP-G4/DP-G5,
  por decisão do dono 2026-07-29: *"faça a mescla dos planos, mantendo um só"*). Nasce
  parcialmente aberto por desenho: `T2..T6` (herdadas, decisões fechadas) são delegáveis já; `T7..Tn`
  são escritas pelo `T1` a partir do `CANDIDATOS.md`. `blocked` — depende do Estágio 2 `done`.
- **[drenado]** 2026-07-29 — `P-0729-v2-documentacao` — **Estágio 4 (fechamento)**: `README.md`
  espelho em PT-BR (13 seções, fonte da verdade declarada por seção), `docs/DOC_MAP.md` do hub,
  **guarda executável de drift** do espelho, bump para `2.0.0` + tag `kit-v2.0.0`, e teste de
  aceitação por leitura cega (6 perguntas de decisão respondidas só pelo README). `blocked` —
  depende do Estágio 3 `done`.
- 2026-07-29 — **correção de estado** (o inbox é append-only, a linha original acima permanece):
  `P-0722-governanca-guardrails-anti-saga` está **`superseded`** desde 2026-07-29 — mesclado em
  `P-0729-v2-melhoria` §1 por decisão do dono. Nenhuma tarefa sai mais dele; as 8 tarefas herdadas
  estão mapeadas uma a uma naquela seção.
- 2026-07-29 — **correção das linhas `P-0729-v2-melhoria` e `P-0729-v2-confronto` acima** (regra
  nova do dono, mesmo dia): *"planos não podem ser emitidos em aberto — podem ser revisados, mas não
  publicados com questões em aberto, pois o agente executor irá parar a execução e forçar o
  retrabalho de revisitar a questão"*. Vira doutrina em `GOVERNANCA.md` como **G-PLANREADY item 5 —
  gate de publicação** (tarefa `V2M-T1`). Aplicada de imediato à própria iniciativa: o
  `P-0729-v2-melhoria` **não tem mais** o bloco aberto `T7..Tn`; ele foi partido em **Estágio 3A**
  (este arquivo — doutrina herdada do `P-0722`, fechado, `T1..T5`) e **Estágio 3B**
  (`P-0729-v2-melhoria-candidatos.md`, **ainda inexistente**, autorado **já fechado** pela tarefa
  `T6` nova do `P-0729-v2-confronto`, depois da ratificação do dono). A Fase 4 do `P-0722`
  (distribuição) foi remapeada para `P-0729-v2-documentacao` T4 — propagação acontece uma vez, no
  fechamento da iniciativa. **Próximo id de plano da iniciativa: nenhum a criar agora.**
