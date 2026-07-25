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
  comando do usuário**. DP-12 aberta (o que fazer com os 11 artefatos que só existem no hub).
  Não iniciado.
