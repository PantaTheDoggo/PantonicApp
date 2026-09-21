# Inbox de planos — histórico (PantonicApp) — arquivamento, nunca reescrita

Este arquivo guarda, verbatim e na ordem original, as linhas já drenadas de `docs/plans/_INBOX.md`
(bullets marcados como drenados e as correções associadas a eles). É destino de arquivamento:
nunca editar, reindentar ou reescrever entradas aqui — só apensar futuras migrações do arquivo
vivo, se e quando o pickup precisar aliviá-lo de novo. O pickup do backlog lê só
`docs/plans/_INBOX.md`.

- **[drenado]** 2026-07-21 — `P-0721-governanca-single-source` — PantonicApp como repositório de referência da
  governança comum Pantonic*: kit executável (7 skills + agentes) deixa de ser copiado em cada
  filho e passa a ser herdado do canônico via `~/.claude`; filhos guardam só o específico +
  ponteiros; docs comuns (`GOVERNANCA.md`/`ARQUITETURA_PANTONICA.md`) formalizados como ponteiro.
  DP-1..DP-6 owner-gated. **Enfileirado após o fechamento de `SPRINT-SUBSWAPLAG` do PantonicVideo**
  (prioridade do dono 2026-07-21: correção da aplicação primeiro). Não promovido — plano registrado,
  não iniciado.
- **[drenado]** 2026-07-22 — `P-0722-governanca-guardrails-anti-saga` — guardrails de doutrina extraídos do
  episódio "saga de legendas" do PantonicVideo (auditoria 2026-07-22), para o radar de todo agente
  Pantonic\*: **G-DEADCODE** (proibição de código morto testado — ~300 linhas foram o gatilho),
  **G-PLANFIDELITY** (executor não troca a rota arquitetural do plano; escala ao dono),
  **G-PREMISE** (premissa que embasa abandono de rota exige spike, não asserção), e skill global
  **`modelo-por-fase`** (operacionaliza §3: intelectual→Opus, execução→Sonnet, leitura→Haiku).
  Concern distinto do SGSS (doutrina, não distribuição); ratificado, entra em `GOVERNANCA.md` e o
  SGSS distribui. Decisões DP-G1..DP-G4 resolvidas 2026-07-22 (todas conforme recomendação); hook de
  modelo-por-fase já prototipado; não iniciado (aguarda "go").
- **[drenado]** 2026-07-25 — `P-0725-governanca-tres-camadas` — redefinição do conjunto governado por decisão do
  dono: `PantonicApp` (base, sempre), `PantonicContainer` (só se containerizado) e
  `PantonicContainerForAWS` (só se container na AWS) são **três camadas condicionais de
  governança**; os demais Pantonic\* são consumidores e saem do escopo. Prepara os dois filhos para
  subir ao GitHub (varredura de credenciais → `.gitattributes`/LF → snapshot fiel → publicação) e
  extrai o delta por camada. **Rebaseia o P-0721** (§5): Fase 4 `superseded`, DP-8 encerrado, Fase 3
  preservada. **DP-9 owner-gated e bloqueante**: medido que a camada 3 não tem conteúdo AWS próprio
  (13/17 artefatos byte-idênticos ao Container; os 4 restantes são só rebordo de linha).
  **SUPERSEDED no mesmo dia** por `P-0725-governanca-hub-unico` — ver linha abaixo.
- **[drenado]** 2026-07-25 — `P-0725-governanca-hub-unico` — segunda simplificação do dono no mesmo dia:
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
- **[drenado]** 2026-07-29 — `P-0729-v2-melhoria-candidatos` — **Estágio 3B**: as mudanças que só o
  benchmarking podia revelar. Autorado **já fechado** pela `V2C-T6` (última tarefa do Estágio 2),
  conforme o gate de publicação — a linha só existe aqui porque o plano nasceu completo. **19
  tarefas** (`V2K-T1..T19`) cobrindo os **14 candidatos ratificados** em
  `docs/benchmark/CANDIDATOS.md` (12 `adotar` + 2 `adaptar`); `C-15` `adiar` não gera tarefa, com
  motivo em §4. Ordem parcial normativa (DK-1): Bloco A = `V2K-T1..T4` (enforcement executável do
  kit + régua de residência da doutrina) → Bloco B = Estágio 3A inteiro → Bloco C = `V2K-T5..T19`
  → Estágio 4. Dois bumps MINOR (`1.3.0` no fim do Bloco A, `1.4.0` no fim do Bloco C); a
  distribuição continua única, no `P-0729-v2-documentacao` T4. `backlog` — desbloqueado pelo
  fechamento do Estágio 2. **Checagem de versão do kit:** modo hub, `1.2.0`, paridade OK, sem
  divergência.
- **[drenado]** 2026-08-05 — `P-0730-v2-identidade` — **Estágio 5 (corretivo)**: o teste de aceitação
  do Estágio 4 reprovou o README e expôs que o desvio está na **fonte da verdade** —
  `GOVERNANCA.md` §1 define o framework como "desktop, stack fixo PySide6" quando o entendimento
  canônico do dono é **agnóstico a tecnologia e plataforma**, atuando nos níveis de arquitetura e de
  projeto, sobre **clean architecture + DDD**, estendidos pelo **infracore** e por **plugins (um
  plugin = um caso de uso)**. 11 desvios medidos (§2), 15 tarefas `V2I-T1..T15`, decisões
  `DR-1..DR-7` ratificadas no ato do planejamento. `DR-7` eleva o **README a documento canônico — o
  contrato entre o framework e o cliente** — com guardrail novo **G-README** e aceite do dono como
  gate de release. **Rebaseia o Estágio 4** (§6): `P-0729-v2-documentacao` vira `superseded`
  (classificação B), `V2D-T5` reprovada, `V2D-T6` cancelada por absorção. Fecha em `2.1.0` (`DR-6`);
  a abstração do infracore (`DR-5`) não entra aqui — nasce como `P-0731`, autorado já fechado pela
  `T15`. **Checagem de versão do kit:** modo hub, local `2.0.0` (VERSION == KIT_VERSION), maior tag
  publicada `kit-v1.3.0` ⇒ **republicação pendente** (decisão do dono, `T13`); achado `TK-05` — o
  gatilho de revisão de doutrina da skill compara só o MINOR e fica cego ao atravessar um MAJOR.
- **[drenado]** 2026-08-06 — `P-0731-v2-extracao-modalidade` — **Estágio 6 (corretivo)**: a 2ª rodada
  de aceite do README reprovou por identidade, e o veredito derruba a `DR-2` do Estágio 5. Perfil não
  é abstração do núcleo — é o nome que o núcleo dava para o próprio vazamento: um framework de
  aplicação desktop contém todo o conhecimento do PantonicApp e o estende, e a camada de baixo não
  sabe nada sobre quem a usa. **O conceito de perfil sai do hub inteiro** (`DE-1`), o conhecimento
  desktop/PySide6/MVVM/Qt migra para `PantonicForDesktop/` e o de container para
  `PantonicForContainer/` — ambas no `.gitignore`, embriões dos repositórios próprios dessas
  ramificações (`DE-2`, `DE-3`). Inclui o único caso que não é prosa: `dead_code.py` troca a tabela
  de virtuais de Qt por um ponto de extensão declarativo do projeto (`DE-5`). **11 tarefas**,
  decisões `DE-1..DE-6` fechadas no ato. **Rebaseia o Estágio 5** (§7): `P-0730-v2-identidade` vira
  `superseded` (classificação B), com as 5 tarefas não iniciadas absorvidas. Fecha em **`3.0.0`** —
  MAJOR, porque remover o conceito de perfil e um guardrail quebra compatibilidade de doutrina com
  os consumidores (`DE-4`). A abstração do infracore, que a `V2I-T15` reservava para `P-0731`, passa
  a **`P-0732`** com escopo corrigido (`DE-6`). **Checagem de versão do kit:** modo hub, `2.0.0`
  (`VERSION` == `KIT_VERSION` == maior tag `kit-v2.0.0`), paridade OK, sem divergência.
- **[drenado]** 2026-08-07 — `P-0732-v2-portas-do-core` — **Estágio 7**: o core é descrito pela implementação, não
  pelo contrato, e a auditoria da implementação de referência mediu as duas metades do vão —
  as portas do infracore existem só como **nomes** (nenhuma operação, invariante ou modo de falha
  escrito no hub, de modo que outra stack precisaria ler o código do case) e a **camada de casos de
  uso não tem artefato** (0 classes `UseCase`; orquestração dispersa em 14 ViewModels/5.216 linhas e
  numa fachada de 781 linhas). Autorado **já fechado** pela `V2E-T11`, última tarefa do Estágio 6,
  conforme o gate de publicação. **10 tarefas** (`V2P-T1..T10`), decisões `DI-1..DI-8` fechadas no
  ato — todas de planejamento: nenhuma questão owner-gated pendente. Entrega o esquema fixo de
  contrato de porta para as 8 portas de runtime + superfície de entrada + execução assíncrona
  (`DI-2`: contrato, nunca implementação — nenhum código de `infracore` nasce no hub), a residência
  do caso de uso em `plugins/<nome>/use_case.py` com campo `use_case` no manifesto (`DI-4`: nenhuma
  regra nova — é a forma que o bloco `DDD-usecase` do `audit-sweep` já procura), e fecha as duas
  declarações de aderência "não auditado" com o estado medido. **Sem guardrail novo** (`DI-5`) e
  **sem verificador executável novo** (`DI-6`: verificador sem alvo é o caso que `G-DEADCODE`
  proíbe — 0/6 consumidores com kit instalado). Inclui a **primeira rodada de revisão de guardrails
  do regime da `DE-8`** (`T7`), aberta pelo fechamento do `P-0731`, e encerra na revisão do
  `README.md` com veredito do dono (`T10`, `G-README` dever 2). **Checagem de versão do kit:** modo
  hub — **congelada em `0.0.0`** (`DE-7`), comparação local × remoto suspensa, nada a comparar.
- **[drenado]** 2026-08-08 — `P-0733-divida-do-hub` — **plano único, sem estágios**, aberto pelo
  encerramento da `SPRINT-PANTONICV2`: com os sete estágios terminais, o backlog vivo do hub passou a
  ser inteiramente tíquete avulso. Quita os **12 tíquetes vivos** do índice em **13 tarefas**
  (`DHB-T1..T13`), agrupados em três dívidas: doutrina decidida e não executada (`TK-15`, `TK-17`,
  `TK-21`, `TK-22`), resíduo de vocabulário do kit (`TK-04`, `TK-12`, `TK-20`) e guarda/navegação
  desalinhadas do que guardam (`TK-06`, `TK-07`, `TK-10`), fechando na revisão final do espelho
  (`TK-18`), que era o único postergado por decisão. Decisões `DH-1..DH-7` fechadas no ato: as duas
  questões que faltavam (`TK-07` — o guarda passa a cobrir seção não numerada; `TK-08` — "estágio"
  permanece convenção, sem promoção a conceito normativo) foram levadas ao dono **antes** da
  publicação, conforme o gate `G-PLANREADY` item 5, e as três restantes eram de planejamento
  (residência da invocação do ratchet, ausência de guarda de fidelidade do espelho, corte do `TK-17`
  em duas fatias por orçamento). Inclui a **segunda rodada de revisão de guardrails do regime da
  `DE-8`** (`T2`), armada pelo fechamento do `P-0732`. Sem bump e sem tag (`DE-7`). **Checagem de
  versão do kit:** modo hub — **congelada em `0.0.0`**, comparação local × remoto suspensa, nada a
  comparar.
- **[drenado]** 2026-08-08 — `P-0734-execucao-autonoma` — **iniciativa nova `EXECUCAO-AUTONOMA`**, aberta a pedido
  do dono: a execução do backlog deixa de custar um round-trip humano por tarefa atômica e passa a
  ser um **loop conduzido pelo próprio agente**. Cria três coisas que hoje não existem — o papel de
  **orquestração** (`scrum-master`, materializado como **skill** e não como agente, porque subagente
  não invoca subagente: `DA-1`), o papel de **revisão** (`pantonic-reviewer`, agente sem ferramenta
  de edição, que emite laudo por tarefa contra a rubrica) e o **documental gerado por função**
  (`telemetria.py`, `rdo.py`, `review_evidence.py`), tirando o formato dos prompts, onde ele é pago
  em todo turno de todo subagente. O registro canônico da tarefa migra do diário para
  `docs/RDO/` (`DA-5`); o diário fica kanban e `docs/telemetria.tsv` continua fonte única do número.
  **17 tarefas** (`EXA-T1..T17`), decisões `DA-1..DA-10` fechadas no ato. Três decisões de desenho
  foram **postergadas por decisão do dono** e viram tarefas próprias (`T2` transporte do pacote de
  retorno, `T3` política de autonomia e tetos, `T4` formato estruturado da tarefa no plano); cada uma
  **fecha o dossiê das tarefas dependentes** no próprio escopo, para que o plano não publique tarefa
  aberta (`G-PLANREADY` item 5). Alcance: **hub primeiro, medir, depois propagar** (`DA-3`, decisão
  do dono) — nenhum derivado é tocado, e a promoção a kit distribuído tem gatilho registrado no §7,
  condicionado ao piloto medido da `T16`. Sem bump e sem tag (`DE-7`). **Checagem de versão do kit:**
  modo hub — **congelada em `0.0.0`**, comparação local × remoto suspensa, nada a comparar; a rodada
  de revisão de guardrails armada pelo fechamento do `P-0732` já está atribuída à `DHB-T2` do
  `P-0733` e **não** é herdada por este plano.
- **[drenado]** 2026-08-15 — `P-0735-residencia-e-ponto-de-carga` — **iniciativa nova `RESIDENCIA`**, aberta pela
  decisão do dono sobre o `TK-45`: **o pacote passa a materializar também o `~/.claude`**. Diagnóstico
  medido no mesmo dia — 13 artefatos de conteúdo do framework (4 hooks registrados, 6 skills, 1 agente,
  2 docs de doutrina) vivem só em `~/.claude/`, mais o `CLAUDE.md` global de 156 linhas, e a doutrina
  versionada os invoca; pelo próprio critério publicado eles não são doutrina, e a doutrina depende
  deles. 5ª ocorrência medida da classe (`TK-01`, `DR-B`, `TK-21`, `TK-43`, `permissions.deny` do
  guardrail 13). **Raiz:** o teste de residência fundia dois eixos independentes — **autoridade** e
  **ponto de carga**. A régua nova (publicada em `GOVERNANCA.md` §3.1 no ato do planejamento) separa
  os dois em **três classes** (canônico · ponto de carga · local de máquina), acrescenta a **pergunta
  zero** antes das quatro e promove o `Prec-2` de critério de desempate a **invariante** — *nada
  canônico mora só num ponto de carga*; a precedência 2 passa a ser *canônico vence projeção* e a
  afirmação de que hook não viaja sai. **9 tarefas** (`RPC-T1..T9`), decisões `DL-1..DL-9` fechadas no
  ato, todas de planejamento: manifesto único `.claude/projecoes.json`, materializador
  `.claude/tools/materializar.py` (`apply`/`check`/`drift`, alvos `projeto` e `usuario`), canônico do
  ponto de carga do usuário em `.claude/global/`, `kit_check` cobrando o canônico no `-Mode validate`
  e a materialização do alvo `projeto` no `-Mode check-drift`. **Rebaseia o `P-0734`** (§6.1):
  classificação **(A)**, plano de origem para `blocked` em 49/60, `T53` e `T54` **canceladas por
  absorção** — o desenho da `T53` sobrevive integralmente na `T2`/`T3` e só a residência particular
  `.claude/hooks/hooks.json` desaparece (generalizar, não duplicar). Absorve `TK-45`, `TK-43`, o
  `permissions.deny` do `DP-R` §22.5 (`DL-7`) e destrava o `DR-B`; **`TK-21` não é absorvido** — rota
  já decidida na `DH-4` e executável no `P-0733` `T10`. Alcance: **hub primeiro, medir, depois
  propagar** (`DA-3` mantida; `docs/CONSUMIDORES.md` mede 0/6 com `.claude/kit/`), com o alvo
  `usuario` **opt-in** e `sync-kit.ps1` inalterado. Sem bump e sem tag (`DE-7`). **Checagem de versão
  do kit:** modo hub — **congelada em `0.0.0`**, comparação local × remoto suspensa, nada a comparar.
- **[drenado]** 2026-08-21 — `P-0736-custo-do-pickup` — **prioridade zero do dono**, declarada na diretiva do
  diário: *o custo de saber onde o trabalho parou esgota a janela antes da primeira delegação*. Fato
  medido, não hipótese: **4 pickups consecutivos** (2026-08-20 e 2026-08-21 ×3) encerrados por
  capacidade (`GOVERNANCA.md` §4.3) **sem executar tarefa nenhuma**; o 4º cruzou o teto ainda no
  levantamento. O dono classificou como **distorção que inviabiliza o framework**. Autorado sob o
  **nível 2** da regra escalonada do mesmo dia — **a investigação medida é a primeira tarefa e o
  plano termina antes da decisão de correção**; nenhuma rota de conserto se ratifica antes da
  medida. **Hipóteses a confirmar, cada uma com instrumento e número:** (H1) a coluna *Título* do
  índice do `docs/DIARIO_DE_OBRAS.md` acumula a narrativa inteira do plano — a célula do `P-0734` é
  uma única linha da ordem de dezenas de milhares de caracteres, lida em todo pickup para extrair
  apenas *status* e *âncora*; (H2) `docs/plans/_INBOX.md` é append-only, já em 205+ linhas, lido
  integralmente a cada pickup para drenar **zero** linhas novas — esta própria linha agrava o caso
  medido; (H3) a fila corrente não tem ponteiro estável e se reconstrói varrendo `Próxima tarefa`
  em 2.400+ linhas, devolvendo ~200 linhas de matches históricos das quais **uma** é a vigente;
  (H4) o custo fixo de entrada (skill `proximo-passo`, `CLAUDE.md` global, `MEMORY.md`) consumido
  antes de qualquer leitura de projeto; (H5) seção de plano terminal (`P-0735`, 13/13 `done`)
  permanece no diário ativo em vez de condensada no histórico. **Entregável da investigação:**
  orçamento medido por fonte lida num pickup típico, ranqueado do maior ao menor, e para cada fonte
  a rota candidata (condensar · substituir por ponteiro · gerar por instrumento · mover ao
  histórico) — **sem** implementar nenhuma. **Critério de aceitação do plano (a aferir depois da
  correção, não antes):** um pickup completo — dois inboxes drenados, diretiva lida, fila apurada e
  dossiê da tarefa em mãos — cabendo num orçamento **declarado em número e medido**, deixando a
  janela com folga para a execução que é o propósito dela. Alcance: **hub primeiro, medir, depois
  propagar** (`DA-3`); o defeito é do fluxo de pickup, que é kit distribuído, então a correção
  candidata atinge `.claude/skills/proximo-passo/` e `.claude/skills/diario-de-obras/`. Sem bump e
  sem tag (`DE-7`). **Checagem de versão do kit:** modo hub — **congelada em `0.0.0`**, nada a
  comparar. **Próximo id após este: `P-0737`.**
- **[drenado]** 2026-08-22 — `P-0737-loop-autonomo` — **rodada de consolidação da `EXECUCAO-AUTONOMA` executada
  nesta data**; a linha carrega o inventário e as decisões do dono, e o plano ainda **não foi
  autorado** (a janela da rodada cruzou o teto de ocupação depois do inventário). Objetivo herdado
  verbatim da diretiva: *transformar o trabalho de `proximo-passo` num agente autônomo, capaz de
  rodar sozinho todas as delegações e ajustes de modelo e entregar ao cliente o entregável do
  plano*. **Inventário medido:** `P-0734` em 52/61 — instrumentos (`telemetria.py`, `rdo.py`,
  `review_evidence.py`), papéis (`pantonic-reviewer`, skill `scrum-master`) e doutrina (rubrica,
  matriz, `G-SCOPE`, `G-SURFACE`, `DP-A`..`DP-S`) entregues; **9 tarefas abertas** — `T29` (`DP-I`,
  artefato `tarefa`), `T30` (`DP-J`, utilidade do laudo), `T19` (RDO gerado no fechamento), `T12` +
  `T23b` (reconciliação com `proximo-passo`), `T26` + `T27` (conformidade `status` × veredito),
  `T16` (piloto) e `T17` (README + veredito). **Três decisões do dono no ato da rodada:** (1)
  **corte seco** — `P-0733` vira `cancelled` e os tíquetes são podados; (2) **escopo estrito nos
  artefatos pedidos** — o **piloto sai** (plano à parte, emitido como *recomendação ao término*),
  otimização de contexto do `scrum-master` é **outro plano**, otimização dos contextos dos agentes
  que ele instancia é **outro plano**; (3) `P-0734` vira **`superseded`, classificação B** — as 52
  entregues ficam como registro, as 8 abertas restantes são absorvidas uma a uma e a `T16` é
  **cancelada por absorção** no plano recomendado do piloto. **Critério fechado de poda:** tíquete
  sobrevive só se for defeito de artefato do loop ou erro factual no `README.md` canônico.
  **Disposição dos 25 tíquetes vivos** — *cancelados por poda (10)*: `TK-06`, `TK-07`, `TK-08`,
  `TK-15`, `TK-17`, `TK-20`, `TK-21`, `TK-22`, `TK-24` (sem objeto com o `P-0733` cancelado),
  `TK-25`; *absorvidos pelo `P-0737` (11)*: `TK-04`, `TK-18`, `TK-26`, `TK-27`, `TK-30`, `TK-36`,
  `TK-37`, `TK-42`, `TK-44`, `TK-46`, `TK-50`; *encaminhados ao plano recomendado de contexto (2)*:
  `TK-23`, `TK-32`; *preservados vivos (2)*: `TK-38` (nasceu de decisão do dono) e `TK-48`
  (owner-gated sobre perda silenciosa de dados) — nenhum dos dois é podável pelo critério acima.
  **Esqueleto proposto, 10 tarefas** (`AUT-T1..T10`): `T1` registro da consolidação (mecânica);
  `T2` `DP-I`; `T3` `DP-J`; `T4` RDO no fechamento; `T5` instrumentos + fronteira do revisor
  (`TK-26`/`TK-50`/`TK-44`/`TK-27`); `T6` aposentadoria do `proximo-passo` na skill única de
  passagem de bastão (`TK-36`/`TK-37`, forma (b) já ratificada em 2026-08-22 — transcrever, não
  deliberar); `T7` superfícies que apontavam para a skill aposentada; `T8` doutrina `status` ×
  veredito (`TK-30`); `T9` conformidade de kanban, planos vivos e varredura de fecho
  (`TK-04`/`TK-42`); `T10` `README.md` + `CHANGELOG.md` + veredito do dono (`TK-46`/`TK-18`), que
  **emite as três recomendações de plano** e fecha a iniciativa. Sem bump e sem tag (`DE-7`).
  **Checagem de versão do kit:** modo hub — **congelada em `0.0.0`**, nada a comparar. **Próximo id
  após este: `P-0738`.**
- **[drenado]** 2026-08-22 — `P-0738-contexto-esgotado` — **plano emergencial, prioridade zero do dono**, declarado
  no mesmo dia: *contextos iniciam já esgotados; custos fixos recorrentes são repagos em cada tarefa,
  gerando desperdício massivo*. **Paralisa o `P-0737`** (`blocked` em 3/12) — nenhuma tarefa sai dele
  até este fechar. O plano **ainda não foi autorado**; esta linha carrega a evidência e o escopo
  mandatados. **Evidência medida que originou a decisão:** a `AUT-T5b` consumiu **três janelas de
  orquestração** para uma tarefa atômica cujo trabalho real coube num único subagente em background —
  janela A pagou o pickup e cruzou o teto no gate de delegação sem delegar; janela B pagou o pickup,
  delegou e cruzou o teto **antes do retorno**, deixando o ato de fechamento órfão; janela C pagou o
  pickup inteiro para verificar entrega pronta e escrever 2 edits, e ainda assim deixou a linha de
  telemetria pendente. Cada uma repagou o pickup que a `CPK-T2` mediu em **77.457 chars (~19.364
  tokens)**, dos quais **43,8% são custo fixo de entrada** antes de tocar qualquer fonte do projeto.
  **Diagnóstico preliminar, a confirmar pela investigação (não é rota ratificada):** (i) o gate de
  delegação orça o teto do **executor** e não orça o **saldo restante do orquestrador**, de modo que
  delegar com janela curta garante uma janela fria pagando pickup completo por um fechamento que vale
  ~5 tool uses; (ii) o custo fixo de entrada não é amortizado entre tarefas — todo contexto novo
  reconstrói do zero o mesmo estado; (iii) a verificação de entrega foi feita à mão, no contexto mais
  caro, existindo instrumento (`review_evidence.py`) e papel (`pantonic-reviewer`) construídos para
  isso. **Escopo mandatado pelo dono, nesta ordem:** investigação medida → avaliação de causas raízes
  → ações que atacam as causas raízes → **execução** (o plano não termina no diagnóstico, ao contrário
  do `P-0736`). **Invariante que o plano deve publicar como permanente**, hoje vigente só como regra
  temporária do `P-0737` (`DP-Q`, invariante 5): **só a capacidade de janela (Regra 2) e a poluição de
  contexto interrompem o curso de uma tarefa — teto e orçamento são alarme, nunca bloqueio.** **A
  autoria deve resolver:** se este plano **absorve** as duas recomendações que o `P-0737` §8 reservava
  como planos à parte (otimização de contexto do `scrum-master` e dos agentes que ele instancia) e os
  tíquetes `TK-23`/`TK-32`, encaminhados àquele plano de contexto — são a mesma matéria. Sem bump e
  sem tag (`DE-7`). **Checagem de versão do kit:** modo hub — **congelada em `0.0.0`**, nada a
  comparar. **Próximo id após este: `P-0739`.**
- [drenado 2026-09-16] `2026-09-15` — `P-0739` — `docs/plans/P-0739-backlog-instrumento.md` — O pickup vira instrumento: `backlog.py` (`next`/`status`/`drain`/`check`) decide a próxima tarefa, fecha a tarefa e mantém o kanban; gramática legível por máquina no diário/inbox; hook `UserPromptSubmit` injeta o dossiê. 9 tarefas `BKL-T1..T9`, decisões `DB-1..DB-16`. Aprovado pelo dono em 2026-09-15. **Próximo id após este: `P-0740`.**
- [drenado 2026-09-18] `2026-09-18` — `P-0740` — `docs/plans/P-0740-loop-de-modulos.md` — **P-0740 — O loop de módulos: a convergência da `EXECUCAO-AUTONOMA` sob a janela real.** Merge das três iniciativas (`P-0734` superseded, `P-0737` blocked 3/10, `P-0738` done 17/17) sob a premissa corrigida de janela de 1M. 6 tarefas (`LM-T1..T6`), decisões `DM-1..DM-8`. Sucede o `P-0737`, que passa a `superseded` (`DM-1`). Matéria: os seis defeitos medidos no run de aferição do `scrum-master` (`BKL-T4`, 2026-09-18) e a troca da tarefa atômica pelo módulo coeso. **Próximo id após este: `P-0741`.**
- [drenado 2026-09-20] docs/plans/P-0741-modelo-conceitual.md — modelo conceitual do plano (interface dono↔loop); 5 tarefas MC-T1..MC-T5; Marco 1 = go do dono sobre a §1, dado em 2026-09-19 pela aprovação do plano
- [drenado 2026-09-20] `2026-09-20` — `P-0743` — `docs/plans/P-0743-modelo-de-dominio.md` — **O modelo conceitual vira modelo de domínio.** Rodada de replanejamento sobre o `AE-18` do `P-0741` (diretiva do dono no Marco 2, apontamentos 1, 2 e 4): a forma passa a ser objetos com contrato e operações encadeadas, o estado vira estágio derivado do andamento das tarefas, o card ganha o campo `Operação do modelo` com o contrato copiado, e nasce o agente `pantonic-model-designer`, dono único de todo ato sobre o modelo. 6 tarefas (`DOM-T1..DOM-T6`), decisões `D-1..D-15`. Continuação do `P-0741` (classe B): o entregue fica de pé e a rota se estende. Marco 1 = `go` do dono sobre a §1 mais a §7 (a leitura nova, preenchida com dados reais). **Próximo id após este: `P-0744`.**
- [drenado 2026-09-20] `2026-09-20` — `P-0744` — `docs/plans/P-0744-spec-do-planejador.md` — **A especificação do agente de planejamento.** Mesma rodada, apontamento 3 do `AE-18`: a operacionalização do plano em tarefas é atribuição do planejamento e ganha spec própria, no precedente de `docs/consultant-spec.md`, escrita sobre agregado medido do corpus fechado de rodadas e achados. 3 tarefas (`PLS-T1..PLS-T3`), decisões `DPL-1..DPL-7`. **Primeiro plano escrito na forma nova do modelo**, e por isso `blocked` até o `P-0743` fechar. Fronteira com o `P-0743` declarada e disjunta na §6. **Próximo id após este: `P-0745`.**
