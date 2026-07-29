# P-0729 — V2 / Estágio 3A: melhoria da governança e da execução (doutrina herdada do `P-0722`)

**Iniciativa:** `PANTONIC-V2` — Estágio 3 de 4, **parte A** (a parte B, derivada do benchmarking, é
autorada fechada pelo Estágio 2 — ver §2).
**Origem:** pedido do dono (2026-07-29): *"No terceiro estágio, elabore o plano de melhoramento da
governança e execução do PantonicApp atual."*

**Planejador:** Opus (2026-07-29). **Executor por tarefa:** redação de doutrina em Opus, mecânica
(skill, check, contador) em Sonnet.

**Estado:** `blocked` — razão: *depende de `P-0729-v2-confronto` `done`*. **Plano fechado:** todas as
tarefas têm objetivo, arquivos-alvo e critério de pronto; nenhuma questão em aberto, nenhum bloco a
preencher.

> **Antecipação autorizada (DM-4):** este plano **não depende do benchmarking** — suas decisões
> foram fechadas em 2026-07-22. Se o dono quiser, ele pode ser antecipado ao Estágio 2 sem
> replanejamento; a única consequência é que o auto-retrato (`BM-00`) passará a marcar as cinco
> guardrails como escritas, e não como `PARCIAL — decidido, não escrito`.

**Checagem de versão do kit:** modo hub; canônico. Sem divergência a reportar.

---

## 1. Mescla do `P-0722` (decisão do dono, 2026-07-29)

> Pergunta feita ao dono: como sequenciar o `P-0722-governanca-guardrails-anti-saga` (pronto,
> decisões DP-G1..DP-G5 fechadas, nunca iniciado), que disputa o mesmo alvo — `GOVERNANCA.md` —
> que este estágio. **Resposta:** *"Faça a mescla dos planos, mantendo um só, já que eles são
> complementares."*

`P-0722` passa a **`superseded`** e este plano é o único vivo da doutrina do hub. A absorção é
**tarefa a tarefa, não fase a fase** — a lição medida em `GOVERNANCA.md` §3 (uma tarefa do plano de
origem ficou sem dono quando uma fase foi absorvida em bloco, e só apareceu quando um passo
posterior tentou consumi-la). Mapa completo, sem sobra:

| Origem em `P-0722` | Absorvido em | Observação |
|---|---|---|
| Fase 1 — redigir G-DEADCODE, G-PLANFIDELITY, G-PREMISE, G-PLANREADY, G-EXECREADY em `GOVERNANCA.md` §7 (itens 9-13) | **T1** | Conteúdo integral, sem rediscussão: DP-G1..DP-G5 decididas em 2026-07-22 |
| Fase 1 — ponteiro em `GOVERNANCA.md` §3 para a skill `modelo-por-fase` | **T1** | Uma linha; fica junto da redação da doutrina |
| Fase 1 — materializar G-EXECREADY em `pantonic-executor` e na skill `proximo-passo` | **T1** | Regra só vale onde o agente a lê |
| Fase 1 — formalizar o contador sequencial de planos (`P-NNNN`, DP-G5) | **T4** | Tem mecânica própria (contador no `_INBOX.md`) e não bloqueia a doutrina |
| DP-G4 — promover G-PLANFIDELITY e G-EXECREADY a Regra do `~/.claude/CLAUDE.md` global | **T3** | Escopo global, fora do repo — tarefa separada por isso |
| Fase 2 — skill global `modelo-por-fase` + revisão do hook já instalado (DP-G2) | **T2** | O hook-protótipo existe desde 2026-07-22; a skill não |
| Fase 3 — check executável de símbolo de produção órfão (G-DEADCODE) | **T5** | Única tarefa do `P-0722` que produz código |
| Fase 4 — distribuição aos consumidores pelo mecanismo do hub | **`P-0729-v2-documentacao` T4** | O mecanismo mudou desde 2026-07-22: hoje é `git subtree` + `sync-kit.ps1` (`GOVERNANCA.md` §9/§10). Distribuição acontece **uma vez**, no fechamento da iniciativa, junto do bump e da nota de migração — não uma vez por estágio |

Nenhuma tarefa do `P-0722` fica sem destino. Nenhuma decisão dele é reaberta — o Estágio 2 pode
**acrescentar**, nunca revogar por conta própria: candidato do benchmarking que contradiga uma
guardrail já ratificada vai ao dono (coluna "sobreposição com o P-0722" exigida em
`P-0729-v2-confronto` T4).

## 2. Por que este plano contém só a parte herdada

A versão original deste plano, publicada mais cedo em 2026-07-29, tinha um bloco `T7..Tn` **em
aberto**, a ser preenchido por uma tarefa de planejamento depois do Estágio 2. O dono vetou o
padrão no mesmo dia:

> *"Planos não podem ser emitidos em aberto. Eles podem ser revisados, mas não podem ser publicados
> com questões em aberto, pois acabará que o agente executor irá parar a execução e forçar o
> retrabalho de revisitar a questão."*

A regra é acolhida como doutrina (T1, **G-PLANREADY item 5 — gate de publicação**) e aplicada
imediatamente a esta iniciativa. O efeito estrutural é o **split**:

- **Parte A (este plano):** o que já está decidido desde 2026-07-22 — as cinco guardrails, a skill,
  a promoção ao CLAUDE.md global, o contador de planos e o check de código morto. Fechado, publicado,
  executável.
- **Parte B (`P-0729-v2-melhoria-candidatos.md`):** o que depende do benchmarking. **Não existe
  ainda, e é correto que não exista.** Ele é autorado — já fechado — como a **última tarefa do
  Estágio 2** (`P-0729-v2-confronto` T6), quando o `CANDIDATOS.md` ratificado pelo dono já for
  insumo disponível. Só então entra no `_INBOX.md` e no diário.

O plano aberto e o plano inexistente parecem a mesma coisa do ponto de vista do backlog, mas não
são: o aberto é **escolhível** pela `proximo-passo` e para o executor no meio; o inexistente não é
escolhível e tem um dono explícito para nascer.

## 3. Tarefas

### T1 — Redigir a doutrina nova em `GOVERNANCA.md` [**Opus**] — *herdado de `P-0722` Fase 1*
- **Objetivo:** `GOVERNANCA.md` §7 passa de 8 para 13 guardrails, e as que dependem de comportamento
  de agente passam a viver também onde o agente as lê.
- **Arquivos-alvo:** `GOVERNANCA.md` §7 (itens 9-13) e §3 (uma linha apontando a skill
  `modelo-por-fase`); `.claude/agents/pantonic-executor.md`;
  `.claude/skills/proximo-passo/SKILL.md`; `.claude/skills/diario-de-obras/SKILL.md`;
  `VERSION` + `.claude/KIT_VERSION` + `CHANGELOG.md` (bump MINOR).
- **Conteúdo:** transcrever de `P-0722` §2 as regras e o enforcement de **G-DEADCODE**,
  **G-PLANFIDELITY**, **G-PREMISE**, **G-PLANREADY**, **G-EXECREADY**, sem reabrir a discussão e sem
  duplicar as 8 guardrails existentes. **Acrescentar a G-PLANREADY o item 5 (novo, decisão do dono
  2026-07-29):**

  > **5. Gate de publicação — plano não se publica em aberto.** Um plano só é registrado no
  > `_INBOX.md` e no diário quando está **fechado**: sem questão pendente, sem bloco a preencher,
  > sem tarefa cujo conteúdo dependa de artefato que ainda não existe. Plano aberto é escolhível
  > pela `proximo-passo` e **para o executor no meio**, forçando retrabalho de revisitar a questão
  > no pior momento — no modelo mais barato e sem o contexto de quem decidiu. Revisar um plano
  > publicado é legítimo e esperado; publicá-lo incompleto não é.
  > **Consequência operacional:** quando parte do trabalho depende de um insumo futuro, não se
  > publica um plano com um vão — **divide-se em dois**: o fechado agora, e o dependente, que é
  > autorado **já fechado** como a última tarefa do plano que produz o insumo. Um plano por nascer
  > não é backlog invisível: ele tem dono, é uma tarefa nomeada de outro plano.
  > **Enforcement:** checklist de fechamento de plano (as 5 condições de G-PLANREADY); a
  > `proximo-passo` recusa delegar tarefa de plano que viole qualquer uma; e o executor recusa
  > performar (G-EXECREADY).

- **Materializar também:** G-EXECREADY no `pantonic-executor` (recusa plano não-pronto; nunca
  pergunta nem decide); G-PLANREADY na `proximo-passo` (só delega tarefa de plano fechado) e na
  `diario-de-obras` (operação "Registrar plano" verifica o gate de publicação antes de apensar).
- **Pronto quando:** as 5 guardrails estão em §7 com regra + enforcement; G-PLANREADY tem os 5
  itens, incluindo o gate de publicação; §3 aponta a skill; os três artefatos do kit citam as regras
  que os governam; versão bumpada nos dois arquivos com o mesmo valor e tag criada.

### T2 — Skill global `modelo-por-fase` [Sonnet] — *herdado de `P-0722` Fase 2 (DP-G2/DP-G3)*
- **Objetivo:** dar gatilho operacional à regra de modelo por fase, hoje vinculante
  (`GOVERNANCA.md` §3) mas lembrada só por disciplina.
- **Arquivos-alvo:** `~/.claude/skills/modelo-por-fase/SKILL.md` (novo — home global, DP-G3);
  revisão de `~/.claude/hooks/modelo_por_fase_userpromptsubmit.py` (protótipo instalado em
  2026-07-22).
- **Conteúdo:** regra de decisão (intelectual→Opus / execução→Sonnet / varredura→Haiku), gate de
  parada e a convenção de anúncio da Regra 5. **Fato técnico já medido, não reinvestigar:** o agente
  não troca o próprio modelo — o schema de saída de hook não tem campo de modelo; a skill
  institucionaliza a parada e o pedido explícito de `/model`.
- **Pronto quando:** a skill existe e descreve os três gatilhos; o hook foi revisado (falsos
  positivos da heurística de palavra-chave corrigidos, ou registrados como aceitos com motivo);
  nada no repo do hub muda — registrar na nota de execução que skill global não bumpa `VERSION`.

### T3 — Promover G-PLANFIDELITY e G-EXECREADY ao CLAUDE.md global [Sonnet] — *herdado de `P-0722` DP-G4*
- **Objetivo:** as duas são conduta universal de executor, não doutrina específica de Pantonic.
- **Arquivos-alvo:** `~/.claude/CLAUDE.md`.
- **Guardrail de escopo:** promover **só** essas duas — G-DEADCODE e G-PREMISE ficam em
  `GOVERNANCA.md` (DP-G4). Forma condensada: o arquivo é lido em toda sessão de todo projeto, e cada
  linha custa em todos eles. A Regra 6 do CLAUDE.md global manda apagar a memória de origem quando
  um feedback vira regra — verificar se há memória a remover.
- **Pronto quando:** as duas regras estão no CLAUDE.md global em forma condensada; nenhuma memória
  redundante sobrou; `GOVERNANCA.md` aponta para elas em vez de duplicar o texto.

### T4 — Contador sequencial de planos [Sonnet] — *herdado de `P-0722` Fase 1/DP-G5*
- **Objetivo:** eliminar a colisão de nomenclatura por data — houve dois `P-0722` no mesmo dia, e
  esta iniciativa tem **quatro** planos `P-0729`, distinguidos só pelo slug.
- **Arquivos-alvo:** `GOVERNANCA.md` (G-PLANREADY item 1: `P-NNNN` monotônico, nunca reusado,
  próximo id = maior registrado no `_INBOX.md` + 1; a data vira campo de cabeçalho);
  `docs/plans/_INBOX.md` (linha de cabeçalho declarando o contador vigente).
- **Migração:** planos existentes ficam **grandfathered** (DP-G5, mantida) — renomear quebraria os
  ponteiros cruzados dos planos fechados sem ganho.
- **Pronto quando:** a regra está escrita; o `_INBOX.md` declara o próximo id; nenhum arquivo
  existente foi renomeado.

### T5 — Check executável de código morto testado [Sonnet] — *herdado de `P-0722` Fase 3*
- **Objetivo:** materializar G-DEADCODE como código, não como checklist — o episódio que a originou
  (~300 linhas de produção sem chamador, vivas só pela suíte verde) passou por revisões humanas.
- **Arquivos-alvo:** `.claude/checks/dead_code.py` (novo), entrada em
  `.claude/skills/guardrails-check/SKILL.md`, `VERSION` + `.claude/KIT_VERSION` + `CHANGELOG.md`.
- **Método:** alcançabilidade por AST a partir dos entry points reais (plugin registrado, superfície
  de serviço no contrato, bootstrap), com allowlist explícita e mínima para API de contrato ainda sem
  consumidor. Cobertura por teste **não** confere "vivo".
- **Verificação:** o check falha sob um símbolo de produção sem chamador (caso sintético) e passa no
  baseline atual do `PantonicVideo` após a limpeza registrada no `P-0722` daquele projeto.
- **Pronto quando:** as duas verificações passam; `guardrails-check` invoca o check; versão bumpada e
  tag criada.

## 4. Riscos

- **Doutrina crescer além do que se lê.** `GOVERNANCA.md` tem 268 linhas e passará de 300 com as 5
  guardrails novas; o CLAUDE.md global tem teto declarado de 200 linhas. Mitigação: T3 promove só o
  que é universal; toda regra nova nasce com enforcement declarado — regra sem enforcement é
  candidata a corte, não a adição.
- **Perder uma tarefa do `P-0722` na mescla** — exatamente o defeito que a lição de `GOVERNANCA.md`
  §3 registra. Mitigação: a tabela de §1 é o contrato da absorção, com "Absorvido em" preenchido em
  todas as linhas; o fechamento do estágio confere a tabela item a item.
- **O gate de publicação virar desculpa para não planejar.** "O plano depende de insumo futuro"
  pode ser usado para adiar indefinidamente. Mitigação: a regra exige que o plano por nascer seja
  **uma tarefa nomeada de outro plano**, com dono e critério de pronto — nunca uma intenção solta.
- **Check de código morto com falso-positivo** em API de contrato ainda sem consumidor. Mitigação:
  allowlist explícita e mínima, revisada (risco já registrado em `P-0722` §5).

## 5. Decisões (fechadas no planejamento)

| id | Decisão | Valor | Motivo |
|---|---|---|---|
| **DM-1** | Destino do `P-0722` | **Mesclado** neste plano; `P-0722` → `superseded`, com mapa tarefa a tarefa (§1) | Decisão do dono, 2026-07-29 ("mantendo um só, já que são complementares") |
| **DM-2** | Decisões DP-G1..DP-G5 do `P-0722` | Mantidas; não são reabertas pelo benchmarking | Nasceram de um incidente real medido — evidência pública não revoga evidência local |
| **DM-3** | Plano aberto | **Proibido.** O bloco `T7..Tn` da versão anterior foi removido e virou plano próprio, autorado fechado pelo Estágio 2 (§2) | Decisão do dono, 2026-07-29; vira G-PLANREADY item 5 no T1 |
| **DM-4** | Ordem de execução | Este plano pode ser **antecipado** ao Estágio 2 a critério do dono | Não depende do benchmarking; única consequência é o auto-retrato registrar as guardrails como escritas |
| **DM-5** | Home do gate de publicação | **Item 5 de G-PLANREADY**, não guardrail própria | G-PLANREADY já é a guardrail de prontidão de plano; uma 14ª entrada em §7 para a mesma preocupação fragmentaria a busca |
| **DM-6** | Distribuição aos consumidores | Uma vez só, no fechamento da iniciativa (`P-0729-v2-documentacao` T4) | Reportar divergência a cada estágio gastaria o turno do dono repetidamente pelo mesmo motivo (`GOVERNANCA.md` §10a: agente reporta, nunca atualiza) |
