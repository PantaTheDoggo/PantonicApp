# P-0737 — O loop autônomo: a entrega do plano sem round-trip humano por tarefa

**Data:** 2026-08-22 · **Origem:** rodada de consolidação da iniciativa `EXECUCAO-AUTONOMA` (diretiva
do dono, 2026-08-22) · **Status:** `superseded` · **Prefixo das tarefas no diário:** `AUT-T<n>` ·
**Prefixo das decisões:** `DU-<n>` · **Checagem de versão do kit:** modo hub — **congelada em
`0.0.0`** (`DE-7`), comparação local × remoto suspensa, **nada a comparar**.

## 0. O objetivo herdado, verbatim

> "só existe um objetivo que tracei no começo, que era transformar o trabalho de `proximo-passo` em
> um agente autônomo, capaz de rodar sozinho todas as delegações e ajustes de modelo, e entregar ao
> cliente o entregável do plano, e não delegar ao humano uma tarefa rotineira e mecânica. Em algum
> momento parece que foram criadas várias tarefas e planos secundários, e parece que foi feito o
> drift do objetivo real inicial. É hora de coletar o que foi feito e o que está previsto, e focar em
> um plano mais eficiente para atingir o objetivo inicial."

O plano existe para servir esse enunciado e nada além dele. Tudo que não é caminho para ele — por
mais legítimo que seja — sai por decisão explícita (`DU-1`, `DU-2`, `DU-3`) e fica registrado com
rota, nunca apagado em silêncio.

## 1. O drift, medido

A iniciativa produziu instrumento, papel e doutrina em volume, e passou a se alimentar do próprio
registro: cada rodada de replanejamento abria decisões novas, cada decisão abria tarefas de
conformidade, e a conformidade abria tíquetes. O resultado medido em 2026-08-22:

- **`P-0734-execucao-autonoma` em 52/61**, com **9 tarefas abertas** — nenhuma delas o loop rodando.
- **`P-0733-divida-do-hub` em 1/13**, vivo desde então, disputando a mesma matéria de kit.
- **25 tíquetes vivos** no índice do diário, a maioria sem relação com o loop.
- **`P-0736-custo-do-pickup`** fechado como lições aprendidas, medindo que o custo fixo de entrada de
  um pickup é 33.932 chars (43,8%) **antes de tocar qualquer fonte do projeto** e que
  `.claude/skills/scrum-master/SKILL.md` (21.660 chars) é maior que a maior fonte do pickup medido.

**O que já está entregue e não se refaz** (as 52 tarefas do `P-0734` permanecem como registro):
instrumentos (`.claude/tools/telemetria.py`, `.claude/tools/rdo.py`,
`.claude/tools/review_evidence.py`), papéis (agente `pantonic-reviewer`, skill `scrum-master`) e
doutrina (rubrica de revisão, matriz de responsabilidades, `G-SCOPE`, `G-SURFACE`, `DP-A`..`DP-S`).

**O que falta para o objetivo:** o loop ainda depende de uma skill de pickup que o dono decidiu
descontinuar, o RDO ainda não se gera no fechamento, dois instrumentos falham no caminho comum, e a
doutrina ainda carrega texto de um mundo anterior às decisões já ratificadas.

## 2. Decisões

### 2.1 Do dono — fechadas no ato da rodada de 2026-08-22 (transcrição, não deliberação)

- **`DU-1` — Corte seco.** `P-0733-divida-do-hub` vira **`cancelled`** e os tíquetes são podados. A
  dívida que ele quitava não é caminho para o objetivo herdado; o que dela for defeito do loop
  reentra por absorção neste plano, e o resto morre com rota registrada.
- **`DU-2` — Critério de poda, fechado.** Um tíquete **sobrevive só se for defeito de artefato do
  loop ou erro factual no `README.md` canônico**. Todo o resto é cancelado. O critério é o mesmo
  para os 25, aplicado uma vez, sem reabertura caso a caso.
- **`DU-3` — Escopo estrito nos artefatos pedidos.** Saem deste plano, cada um como **plano à parte,
  emitido como recomendação ao término** (`AUT-T10`): (a) o **piloto** medido do loop; (b) a
  **otimização de contexto do `scrum-master`**; (c) a **otimização dos contextos dos agentes que ele
  instancia**. Nenhum dos três é tarefa daqui.
- **`DU-4` — `P-0734` vira `superseded`, classificação (B).** As 52 entregues ficam como registro,
  as **8** abertas restantes são absorvidas **uma a uma** (§4) e a **`T16` é cancelada por
  absorção** no plano recomendado do piloto. Nenhuma tarefa nova sai do `P-0734`.
- **`DU-5` — Forma (b) da reconciliação com `proximo-passo`, ratificada em 2026-08-22.** A skill
  `proximo-passo` é **descontinuada**; a responsabilidade é herdada pelo `scrum-master`, de contexto
  fixo, que orquestra mecanicamente os contextos dos agentes que instancia. Transcrever, não
  deliberar: a alternativa (a) — dois modos coexistindo com os gates extraídos — está **recusada**.

### 2.2 De planejamento — fechadas neste ato, sem decisão nova de arquitetura ou de requisito

- **`DU-6` — Dossiê herdado viaja por ponteiro, não por cópia.** Onde o dossiê técnico já existe
  verbatim no `P-0734`, este plano aponta por âncora exata (arquivo + `### T<n>` + faixa de linhas) e
  registra **só os deltas**. `superseded` não é apagado: o arquivo permanece legível e é a fonte do
  detalhe. Copiar 400 linhas de dossiê para cá criaria a duplicata que `GOVERNANCA.md` §3.1 proíbe.
- **`DU-7` — `DP-I` e `DP-J` preservam o identificador e trocam de residência.** As duas são citadas
  por nome em texto vigente (`T26`, `TK-30`, `DP-H`, `DP-K`); renomeá-las quebraria ponteiro sem
  ganho. Passam a morar em `## Dossiês fechados por decisão` **deste** plano, criado pela `AUT-T2`.
- **`DU-8` — O portador do checkpoint de contexto é a Orquestração; nenhum canal novo nasce.**
  Fecha o `TK-37` sem responsabilidade nova, por derivação do já ratificado: (i) a `DP-N` retirou do
  executor toda escrita — ele sinaliza `review` ou `blocked` com razão tipada e nada mais —, logo
  `handover/SKILL.md:96-100` e `GOVERNANCA.md:340-344`, que mandam a **Execução** escrever o
  checkpoint no diário, são **resíduo pré-`DP-N`**, não lacuna a preencher; (ii) escrever no registro
  do projeto já é ato da **Orquestração** na matriz de responsabilidades, então nada se cria; (iii)
  dentro do loop, o único contexto que **atravessa** tarefas é o do `scrum-master` — o do executor
  vive uma tarefa e morre com ela, sem herança a gravar. Tarefa que não cabe numa janela é **defeito
  de decomposição**, cuja rota já existe e é a partição do card pelo planejamento (precedentes
  medidos: `T6a`/`T6b`, `T21a`/`T21b`, `T7a`/`T7b`/`T7c` do `P-0735`).
- **`DU-9` — A skill única chama-se `passagem-de-bastao` e as duas antigas são apagadas.**
  `.claude/skills/proximo-passo/` e `.claude/skills/handover/` deixam de existir; nada é preservado
  "por ser comunicação com humano", porque essa comunicação já tem portador canônico — o **RDO**
  (`DP-K`: o RDO é a comunicação do projeto com o dono), gerado por função. O `TK-38` continua vivo e
  **não** é insumo da `AUT-T6`: ele trata da superfície do gerente com o humano, não do texto da
  skill aposentada. Material sem portador que apareça na transposição vira **linha de achado no
  `TK-38`**, nunca improviso na skill nova.
- **`DU-10` — A `T27` do `P-0734` dissolve em duas, sem vão.** A matéria de **doutrina** (incluindo
  as arestas e propriedades de `superseded` no vocabulário de plano/iniciativa, rota que o dono fixou
  para o `TK-30` em 2026-08-13) vai para a **`AUT-T8`**; a matéria de **kanban, planos vivos e
  varredura de fecho** vai para a **`AUT-T9`**, que mede o resultado da `T8`. A decisão do dono é
  preservada em substância — a matéria continua na herdeira da `T27`, e a `DP-F` não se reabre.
- **`DU-11` — Fronteira entre o que este ato de planejamento aplica e o que a `AUT-T1` aplica.**
  Aplicado **agora**, porque a reconciliação de planos derivados é imediata por regra da skill
  `diario-de-obras`: flip `P-0734` → `superseded` e `P-0733` → `cancelled` (célula do índice e linha
  *Próxima tarefa* das duas seções), drenagem da linha do `_INBOX.md`, contador de próximo id em
  `P-0738`, diretiva de priorização reescrita, e índice + seção do `P-0737` criados. Aplicado pela
  **`AUT-T1`**: a rota dos 25 tíquetes no índice e a seção de rebase dentro do `P-0734`. Nada
  aparece nas duas listas.
- **`DU-12` — Decide-e-para em lote: um round-trip do dono.** Três tarefas param para ratificação —
  `AUT-T2` (`DP-I`), `AUT-T3` (`DP-J`) e a frente (c) da `AUT-T5` (fronteira de ferramenta do
  `pantonic-reviewer`, cuja escolha o `TK-27` atribui ao dono). As três são ratificadas **juntas**, e
  o que a ratificação implicar materializar é **card autorado** pela rodada que a consumir — nunca
  improviso dentro da tarefa que decidiu.
- **`DU-13` — Sem bump, sem tag, hub primeiro.** `DE-7` mantida: nenhuma versão nova, nenhuma tag; a
  mudança canônica escreve linha no `CHANGELOG.md` sob `## [Não lançado]`. `DA-3` mantida: o alcance
  é o **hub**, e **nenhum consumidor é tocado** — a propagação é ato posterior, fora deste plano.
- **`DU-14` — Número não governa curso de ação. Regra temporária, decisão do dono, 2026-08-22.**
  Teto, orçamento e contagem de write-clusters são **instrumentação**: medem-se e registram-se, e não
  decidem nada. Dentro deste plano **deixam de acontecer**, por número: partir tarefa em fatias no
  gate de delegação (o precedente da própria `AUT-T5` → `T5a`/`T5b`/`T5c`, e o da `RPC-T7` antes
  dela), parar execução por teto atingido, reordenar fila e escalar ao dono. **As únicas duas
  restrições que governam** são a **coesão do contexto** (`.claude/global/CLAUDE.md` Regra 2 — uma
  tarefa por contexto; sinal de poluição encerra a janela) e o **volume da janela corrente**
  (`GOVERNANCA.md` §4.3 — a ocupação em uso encerra por capacidade, com checkpoint e handover).
  **Precedência:** onde texto herdado deste plano ou do kit mandar agir por número, esta regra vence
  dentro do `P-0737`; os cabeçalhos `[<modelo> · classe <slug> · teto <N>]` ficam como estão, e o
  número neles passa a ser leitura, nunca comando. **Temporária por desenho:** vale enquanto o
  `P-0737` estiver vivo e **morre com ele** — não vira doutrina, não sobe para `GOVERNANCA.md` e não
  entra em skill nem em agente, porque regra nova em artefato de doutrina é o volume que este plano
  existe para desfazer. **Não reabre nada:** o `orcamento_estourado` de `calcular_desdobramento` é
  parâmetro de instrumento dentro do dossiê fechado da `AUT-T4`, e esta regra não o toca — se a
  colisão importar, ela é ponto do dono na rodada daquela tarefa, não improviso dentro dela. O
  consumo continua medido e apendado a `docs/telemetria.tsv` sem exceção (`DP-Q`).

## 3. Invariante de execução (vale para todas as tarefas)

1. **Nenhuma tarefa deste plano executa o loop que ele projeta.** O plano se executa pelo fluxo
   vigente, uma tarefa por contexto. O loop rodando sobre trabalho real é o **piloto**, que saiu por
   `DU-3` e volta como recomendação.
2. **Instrumento nasce com teste.** Todo `.py` tocado entra com teste em `tests/`, e o piso de
   regressão da suíte nunca desce.
3. **Registro já escrito não se reescreve.** Bullets de fechamento, dossiês de decisão, RDO emitido e
   prosa que narra o ocorrido ficam como estão. Só **marcador vivo** — o que descreve estado atual —
   migra.
4. **Redação.** `.claude/skills/redacao-doc/SKILL.md` é normativa em todo texto publicado que este
   plano manda escrever. Plano e decision record são registro e são isentos.
5. **Número não governa curso de ação** (`DU-14`, temporária, vale só neste plano): teto, orçamento e
   contagem de write-clusters são instrumentação — não partem tarefa, não param execução, não
   reordenam fila e não escalam ao dono. Governam apenas a **coesão** (Regra 2) e o **volume da
   janela corrente** (`GOVERNANCA.md` §4.3). O consumo é medido e apendado a `docs/telemetria.tsv`
   sem exceção (`DP-Q`). **Promovida a permanente pela `CTX-T1` do `P-0738` e partida em duas pela
   `DX-13`:** poluição é regra final de execução, canônica em `.claude/global/CLAUDE.md` (Regra 2),
   com guardrail em `GOVERNANCA.md` §7 item 7; capacidade é diretriz de dimensionamento de quem
   planeja, canônica em `GOVERNANCA.md` §3.
6. **Bateria de fechamento de toda tarefa** — os quatro primeiros em exit 0:
   `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate`,
   `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift`,
   `pwsh -NoProfile -File .claude/checks/check-readme.ps1`,
   `python .claude/checks/dead_code.py`, e `python -m pytest` na raiz do hub.
7. **Contagens de linha medidas em rodadas anteriores são remedidas na entrada da tarefa** — nenhuma
   edição se apoia em número de linha herdado sem conferência por Grep.

## 4. Rebase do `P-0734-execucao-autonoma` — classificação (B)

**Efeito imediato:** `P-0734` inteiro vira **`superseded`**, com ponteiro `substituído por:
docs/plans/P-0737-loop-autonomo.md`. Fora do backlog, nenhuma tarefa nova sai dele, o entregue
permanece. A iniciativa `EXECUCAO-AUTONOMA` passa a ter **um** plano vivo — este (regra de
convergência da skill `diario-de-obras`).

**Destino das 9 tarefas abertas — uma a uma, nenhuma sem destino:**

| Tarefa do `P-0734` | Matéria | Destino |
|---|---|---|
| `T29` — artefato `tarefa`, fecha a `DP-I` | doutrina · decide-e-para | **absorvida** → `AUT-T2` |
| `T30` — utilidade do laudo, fecha a `DP-J` | doutrina · decide-e-para | **absorvida** → `AUT-T3` |
| `T19` — `rdo.py`: o RDO se gera no fechamento | implementação | **absorvida** → `AUT-T4` |
| `T12` — reconciliação com `proximo-passo` | kit executável | **absorvida** → `AUT-T6` (a decisão que ela deveria tomar já veio pronta pela `DU-5`: forma (b)) |
| `T23b` — `proximo-passo` aponta para a residência única | kit executável | **absorvida** → `AUT-T6` (a skill-alvo deixa de existir; a skill nova nasce já falando a lista final da `DP-F`, o que entrega o efeito sem a edição) |
| `T26` — conformidade: doutrina normativa | doutrina | **absorvida** → `AUT-T8` |
| `T27` — conformidade: kanban, planos vivos e varredura de fecho | doutrina + kanban | **absorvida, dissolvida em duas** (`DU-10`) → `AUT-T8` (doutrina, com o `TK-30`) + `AUT-T9` (kanban, planos vivos e varredura) |
| `T17` — `README.md`, `CHANGELOG.md` e veredito do dono | fecho | **absorvida** → `AUT-T10` |
| `T16` — piloto medido | validação | **cancelada por absorção** — a matéria migra integral para o **plano recomendado do piloto** (`DU-3`), emitido pela `AUT-T10`. O corpo do dossiê da `T16` (escopo, medidas, registro qualitativo por causa, gate de reprovação e o critério de aceitação do §19) é o material que aquele plano absorve, e **nada dele se perde**. |

**Item 4 da `T17` (desdobramento da matéria de consumo):** transferido para a `AUT-T10` junto do
resto da tarefa, e emitido como parte da recomendação (c) do §8 — a matéria de uso e teto (`TK-32`,
`T34` cancelada, a `DP-L` não formada) não se decide aqui.

## 5. Poda de tíquetes — os 25 vivos, nominalmente

Critério único, `DU-2`: sobrevive só o que é **defeito de artefato do loop** ou **erro factual no
`README.md` canônico**. Aplicação (execução no kanban é da `AUT-T1`):

**(a) Cancelados por poda — 10.** `TK-06`, `TK-07`, `TK-08`, `TK-15`, `TK-17`, `TK-20`, `TK-21`,
`TK-22`, `TK-24` (**sem objeto** — dependia do `P-0733`, cancelado pela `DU-1`), `TK-25`. Nenhum
passa no critério; cada célula recebe nota de poda com data e ponteiro para este parágrafo, e nenhum
texto do tíquete é apagado.

**(b) Absorvidos por este plano — 11**, cada um com a tarefa que o fecha:

| Tíquete | Matéria | Fecha em |
|---|---|---|
| `TK-26` | sentinela de "métrica não medida" em `telemetria.py` (decidido em 2026-08-11) | `AUT-T5` |
| `TK-50` | `telemetria.py append` não expressa `nao_medido`/`contado` — mesmo defeito, medido ao vivo em 2026-08-22 | `AUT-T5` |
| `TK-44` | `review_evidence.py` não discrimina escopo de tarefa | `AUT-T5` |
| `TK-27` | independência do `pantonic-reviewer` é parcial na lista de ferramentas | `AUT-T5` (mede e para; a escolha é do dono) |
| `TK-36` | reorganizar a passagem de bastão numa skill única | `AUT-T6` |
| `TK-37` | quem escreve o checkpoint de contexto (lacuna da matriz) | `AUT-T6`, pela `DU-8` |
| `TK-30` | arestas e propriedades de `superseded` sem residência | `AUT-T8` |
| `TK-04` | `pantonic-executor.md` hardcoda teto numérico | `AUT-T9` |
| `TK-42` | resíduo de entendimento derrubado fora dos universos da `DP-P` | `AUT-T9` |
| `TK-46` | `README.md:352-354` contradiz `GOVERNANCA.md` §3.1 sobre o hook | `AUT-T10` |
| `TK-18` | revisão final do espelho do `README.md` (14 seções) | `AUT-T10` |

**(c) Encaminhados ao plano recomendado de contexto — 2.** `TK-23` e `TK-32`. Nenhum mérito é
reaberto aqui; a `AUT-T1` registra o encaminhamento e a `AUT-T10` nomeia os dois na recomendação (b)
e (c) do §8.

**(d) Preservados vivos, sem toque — 2.** `TK-38` (nasceu de decisão do dono) e `TK-48` (owner-gated,
perda silenciosa de dados). Nenhum dos dois é podável pelo critério, e nenhuma tarefa deste plano os
edita.

## 6. Tarefas

### AUT-T1 — Registro da consolidação [Sonnet · classe mecanica · teto 20]
- **Objetivo:** o kanban passa a dizer a verdade do dia — um plano vivo na iniciativa, os 25 tíquetes
  com rota escrita, e o plano de origem carregando o mapa do rebase.
- **Já aplicado no ato do planejamento — não repetir, não conferir por reedição** (`DU-11`): flip
  `P-0734` → `superseded` e `P-0733` → `cancelled` (célula do índice e linha *Próxima tarefa* das
  duas seções), linha do `P-0737` no índice e seção `## P-0737` no diário, drenagem da linha do
  `_INBOX.md` com contador em `P-0738`, e a diretiva de priorização reescrita.
- **Arquivos-alvo:** `docs/DIARIO_DE_OBRAS.md` (índice — 25 células de tíquete);
  `docs/plans/P-0734-execucao-autonoma.md` (uma seção nova ao final, `## 24. Rebase pelo P-0737`);
  `docs/DOC_MAP.md` (uma entrada nova — frente (e)).
- **Conteúdo, em três frentes:**
  - **(a) Os 10 podados** (§5a) — coluna Status vira `cancelled`, com a nota
    `*(podado pelo critério do P-0737 §5, 2026-08-22)*`. O texto da coluna Título **não se toca**.
  - **(b) Os 11 absorvidos** (§5b) — o status **não muda**; cada célula ganha ao final da coluna
    Status a nota `*(absorvido pelo P-0737, fecha na AUT-T<n>)*`, com o `n` da tabela do §5b. Única
    exceção: `TK-18`, hoje `blocked — validação postergada`, tem a razão atualizada para
    `blocked — validação postergada até AUT-T9 done`.
  - **(c) Os 2 encaminhados** (§5c) — `TK-23` e `TK-32` ganham a nota
    `*(encaminhado ao plano de contexto recomendado pelo P-0737 §8)*`, status inalterado. `TK-38` e
    `TK-48` **não recebem edição nenhuma**.
  - **(d) A seção de rebase no `P-0734`** — `## 24. Rebase pelo P-0737`, transcrevendo a tabela do §4
    deste plano (as 8 absorvidas com a `AUT-T<n>` de destino e a `T16` cancelada por absorção) mais
    uma linha declarando o plano `superseded` por classificação (B). **Nenhum dossiê, bullet ou
    decision record do `P-0734` é editado** — a seção é acréscimo no fim do arquivo.
  - **(e) A entrada do `P-0737` no `docs/DOC_MAP.md`** — acréscimo autorizado pelo dono em
    2026-08-22, fora do escopo original desta tarefa: o plano nasceu com 574 linhas, acima do
    gatilho de 500 do mapa, e um plano desse porte fora do índice reintroduz o custo de navegação
    que o `P-0736` mediu. Uma entrada só, no formato já usado pelas três existentes (`P-0721`,
    `P-0725-HU`, `P-0729-V2K`): heading `## docs/plans/P-0737-loop-autonomo.md (~NNN linhas)` com o
    porte **re-derivado no ato** por `(Get-Content docs/plans/P-0737-loop-autonomo.md).Count` —
    nunca copiado deste dossiê —, seguido de **Propósito**, **Quando consultar**, a lista de âncoras
    `##` e a linha **Acesso:** com o padrão de Grep (`^### AUT-T5 `, trocando pela tarefa desejada).
- **Invariantes:** nenhuma linha do índice é reordenada; nenhum texto de tíquete é reescrito; nenhum
  dos 25 fica com duas rotas ou com nenhuma; as três entradas já existentes do `DOC_MAP` não são
  tocadas.
- **Verificação:** bateria do §3; Grep por cada um dos 25 IDs no índice, conferindo **exatamente uma**
  rota por ID; `Grep '^## 24\. Rebase' docs/plans/P-0734-execucao-autonoma.md` com 1 ocorrência;
  o padrão de Grep escrito na linha **Acesso:** da frente (e) executado uma vez, devolvendo match;
  `git diff --stat` restrito a três arquivos.
- **Pronto quando:** os 25 tíquetes têm rota escrita conforme o §5, o `P-0734` carrega a seção de
  rebase, o `DOC_MAP` indexa o `P-0737` com padrão de acesso que casa, e nenhum registro histórico
  foi reescrito.

### AUT-T5 — Os dois instrumentos que falham no caminho comum, e a fronteira do reviewer [Sonnet · classe implementacao · teto 40]
- **Absorve:** `TK-26`, `TK-50`, `TK-44`, `TK-27`.
- **Objetivo:** a série de consumo e o dossiê de evidência param de exigir escrita à mão e de mentir
  sobre escopo — são os dois instrumentos que o loop usa em toda tarefa, e os dois falharam medidos.
- **Arquivos-alvo:** `.claude/tools/telemetria.py`; `docs/telemetria.tsv` (uma célula);
  `.claude/tools/review_evidence.py`; `tests/test_telemetria.py`; `tests/test_review_evidence.py`;
  `docs/plans/P-0737-loop-autonomo.md` (só a frente (c), no §9 *Achados da execução*).
- **Conteúdo, em três frentes:**
  - **(a) Sentinela de métrica ausente — `TK-26` + `TK-50`, decisão já fechada em 2026-08-11.** A
    sentinela única é a **célula vazia**, e `append` a aceita nas três colunas numéricas
    (`tool_uses`, `tokens_k`, `duracao_s`) **sempre que `fonte` ≠ `usage`**. Com `fonte = usage` o
    vazio continua sendo falha ruidosa — o bloco `<usage>` carrega os três, e vazio ali é medida
    **perdida**, não ausente. Normalizar a **única** linha histórica com traço literal
    (`docs/telemetria.tsv:50`, `V2I-T3`, colunas `tokens_k` e `duracao_s`) para célula vazia — única
    exceção à regra "só apende", por ser correção de sentinela e não de número; **remedir a linha por
    Grep antes de editar**. Testes: aceitação por `fonte` ∈ {`contado`, `nao_medido`}, recusa por
    `fonte = usage`, e preservação byte a byte do restante do arquivo.
  - **(b) Escopo do dossiê de evidência — `TK-44`.** Duas correções, ambas dentro do instrumento:
    (i) **alvo declarado como diretório vira caso tratado** — hoje é comparado como caminho literal e
    produz "arquivo ausente na árvore de trabalho"; passa a casar por **prefixo de caminho**,
    normalizando separador, de modo que `.claude/tools/` case `.claude/tools/rdo.py`; (ii) o conjunto
    de arquivos atribuído à tarefa passa a ser recortado por um **ponto de referência**, e não pela
    árvore não commitada inteira: o `review_evidence.py` recebe o ponto por argumento
    (`--desde <ref>`), e na ausência dele mantém o comportamento atual **declarando no dossiê** que o
    recorte é a árvore inteira — o dossiê nunca afirma escopo que não mediu. Quem passa o argumento é
    o `scrum-master`, que já grava a tarefa corrente em `.claude/estado/tarefa-corrente.json` no ato
    do despacho (`DP-S` §23.3): a conciliação da skill entra nesta tarefa, no ponto onde ela invoca o
    instrumento. Testes: alvo-diretório casando por prefixo, `--desde` recortando, ausência de
    `--desde` produzindo a declaração explícita.
  - **(c) Fronteira de ferramenta do `pantonic-reviewer` — `TK-27`, mede e para.** Confirmar
    **empiricamente** se o campo `tools:` do frontmatter de agente aceita especificador de `Bash`
    (comando escopado), registrando o método e o resultado. **Nenhuma edição em
    `.claude/agents/pantonic-reviewer.md`**: a escolha entre (a) escopar no `tools:` e (b) impor o
    escopo por regra de permissão de projeto é **do dono** (`TK-27`), e vai à ratificação em lote da
    `DU-12`. O resultado é escrito como achado no §9 deste plano, com recomendação em uma linha.
- **Invariantes:** nenhum número da série é alterado (só a sentinela da linha 50); nenhuma coluna
  nova entra no TSV; a frente (c) não edita agente nem `settings`; o piso de regressão da suíte não
  desce.
- **Verificação:** bateria do §3; os testes novos falham antes da correção e passam depois; append de
  uma linha real com `fonte = contado` pelo instrumento, sem `Add-Content`.
- **Pronto quando:** uma linha de telemetria com métrica ausente é apendável **pelo instrumento**, o
  dossiê de evidência discrimina escopo ou declara que não discriminou, e a medição do `TK-27` está
  escrita com recomendação, parada para o dono.

### AUT-T4 — `rdo.py`: o RDO se gera no fechamento [Sonnet · classe implementacao · teto 40]
- **Dossiê herdado por ponteiro (`DU-6`):** `docs/plans/P-0734-execucao-autonoma.md` `### T19`
  (linhas 917-1045) — integral, incluindo a CLI final do `close`, as cinco frentes (a)..(e), as duas
  premissas de escopo (`DP-D`, `DP-H`) e a lista de argumentos que saem. Fechado por `DP-D`, `DP-F`,
  `DP-G` e `DP-H`; **nada nele se reabre**.
- **Deltas declarados, e são todos:** (i) a dependência da `T18` está **satisfeita** — a `T18` fechou,
  e os números de linha do dossiê valem para o estado atual de `.claude/tools/rdo.py`, a ser
  remedido por Grep na entrada (invariante 7); (ii) o teto rígido de 40 do dossiê original vale como
  **alarme**, não bloqueio (`DP-Q`, invariante 5); (iii) o dossiê fala em "achados do §9 do `P-0734`"
  — a residência de achado desta execução é o §9 **deste** plano.
- **Objetivo:** o RDO deixa de ser aberto no início e passa a ser **gerado no fechamento**, a partir
  do plano, do `pacote` recebido por argumento, do consumo medido e do desdobramento calculado —
  dissolvendo a circularidade `close` ↔ laudo.
- **Arquivos-alvo:** `.claude/tools/rdo.py`, `.claude/tools/rdo_template.md`, `tests/test_rdo.py`.
- **Invariantes:** o `close` **não lê arquivo de laudo** e o RDO **não carrega ponteiro** para ele; não
  existe `--status` em lugar nenhum; o que não estiver no `pacote` não entra no RDO por improviso — o
  critério de retenção é a `DP-J` (`AUT-T3`), e qualquer acréscimo é card autorado depois.
- **Verificação:** bateria do §3; os testes de `tests/test_rdo.py` cobrindo a CLI nova, o domínio
  fechado de `--veredito`, a faixa de `--percentual` e a recusa de campo multilinha.
- **Pronto quando:** um RDO é produzido por uma única invocação de `close` com o `pacote` completo, e
  nenhuma invocação abre documento no início.

### AUT-T2 — `DP-I`: o artefato `tarefa` — definição, autores e canal [Opus · classe redacao · teto 30]
- **Dossiê herdado por ponteiro (`DU-6`):** `P-0734` `### T29` (linhas 1234-1289) — as cinco
  perguntas, o insumo fechado da `DP-K` (hierarquia plano → tarefa → laudo → RDO) e os invariantes.
- **Deltas declarados:** (i) o **arquivo-alvo muda** — a seção `### DP-I` nasce em
  `docs/plans/P-0737-loop-autonomo.md`, sob `## Dossiês fechados por decisão` (a `AUT-T2` cria a
  seção-mãe se ela ainda não existir), e **não** no `P-0734`, que está `superseded` (`DU-7`); (ii) a
  dependência da `T21b` está satisfeita.
- **Objetivo:** fechar a `DP-I` — **três** das cinco perguntas são **transcrição** do já ratificado
  (definição, mapeamento sobre o material existente, ciclo de vida) e **duas** são decisão com
  recomendação explícita: **autores e escrita** (pergunta 2) e **conteúdo obrigatório, em particular
  onde o `status` da tarefa é materialmente gravado** (pergunta 3).
- **Invariantes:** decisão **incremental** sobre o ratificado — não revoga `DP-C`..`DP-K`, não move
  residência de artefato, não autora tarefa nova; proposta de mover residência é **achado tiquetado**;
  o termo único é `reviewer` (nem *inspetor*, nem *revisor*); `redacao-doc` não se aplica a decision
  record.
- **Verificação:** bateria do §3; a `### DP-I` responde às cinco perguntas sem bloco a preencher;
  Grep por `DP-I` neste plano com ≥1 ocorrência; nenhum arquivo fora deste plano no diff.
- **Pronto quando:** a `DP-I` está escrita como proposta completa e **para** para ratificação apenas
  das perguntas 2 e 3, em lote com a `DP-J` e a medição do `TK-27` (`DU-12`).

### AUT-T3 — `DP-J`: o que o `scrum-master` colhe do laudo e o que descarta [Opus · classe redacao · teto 30]
- **Dossiê herdado por ponteiro (`DU-6`):** `P-0734` `### T30` (linhas 1291-1333) — as quatro frentes
  (a) critério, (b) aplicação campo a campo, (c) o card "Lições aprendidas na tarefa", (d) efeito
  declarado; e o insumo fechado da `DP-K` (o laudo é efêmero nos três ramos).
- **Deltas declarados:** (i) a seção `### DP-J` nasce **neste** plano, sob `## Dossiês fechados por
  decisão` (`DU-7`); (ii) a dependência da `T19` é satisfeita pela **`AUT-T4`**, que precede esta
  tarefa na ordem do §7 — o `pacote` que o `close` consome é o piso sobre o qual o critério opera.
- **Objetivo:** fechar a `DP-J` — critério reexecutável de **utilidade**: a informação do laudo
  sobrevive se **decide** algo no desdobramento ou se o **RDO precisa dela** para ser registro
  suficiente; o resto morre com o laudo.
- **Invariantes:** o `pacote` da `DP-H` item 4 é **piso, não teto**; pesos, faixas e dimensões da
  rubrica não mudam; o RDO continua sem ponteiro para o laudo; o campo "Lições aprendidas na tarefa"
  **existe** por insumo do dono — a `DP-J` decide residência e autoria, não a existência; nenhuma
  materialização aqui (não edita `rdo.py`, não edita template, não reabre a `AUT-T4`).
- **Verificação:** bateria do §3; **todos** os campos do laudo vigente classificados, sem campo sem
  destino; a pergunta (c) com resposta e residência; diff restrito a este plano.
- **Pronto quando:** o critério está escrito, cada campo tem destino, e a decisão está **parada** para
  a ratificação em lote da `DU-12`.

### AUT-T6 — A skill única de passagem de bastão; `proximo-passo` e `handover` são aposentadas [Opus · classe redacao · teto 40]
- **Absorve:** `TK-36`, `TK-37`, e as tarefas `T12` e `T23b` do `P-0734`.
- **Forma já ratificada (`DU-5`) — transcrever, não deliberar:** forma **(b)**. `proximo-passo` é
  descontinuada; a responsabilidade é herdada pelo `scrum-master`, de contexto fixo, que orquestra
  mecanicamente os contextos dos agentes que instancia.
- **Objetivo:** o maquinário de transição entre tarefas passa a existir **uma vez só**, no ponto que o
  loop já usa, e o texto dos gates deixa de existir em duas cópias.
- **Arquivos-alvo:** `.claude/skills/passagem-de-bastao/SKILL.md` (**novo**);
  `.claude/skills/proximo-passo/SKILL.md` (**removido**); `.claude/skills/handover/SKILL.md`
  (**removido**); `.claude/skills/scrum-master/SKILL.md` (3 ocorrências medidas — conciliação do
  consumidor direto).
- **Natureza da skill nova, fixada pelo dono (`TK-36`, 2026-08-13):** maquinário **estrito** do
  `scrum-master`, na superfície **agente↔agente**, **transparente para o gerente do projeto** — ele
  não a invoca, não a lê e não a acompanha. Prima por eficiência e qualidade da transição, incluindo
  a **herança de contexto** entre tarefa predecessora e sucessora. **Não é skill de comunicação com
  humano** (essa superfície é do `TK-38`, e os dois eixos não se misturam).
- **Conteúdo:**
  - **Transposição, não reescrita.** O que sobrevive das duas skills viaja como está: heurística de
    priorização, leitura da diretiva do diário, drenagem dos inboxes, apuração da fila, montagem do
    dossiê de delegação e a herança de contexto entre tarefas. A reconciliação decide **onde** mora,
    não **se** sobrevive.
  - **Gate em um lugar só.** `G-PLANREADY` e o gate de delegação existem **uma vez** — a cópia
    perdedora é apagada no mesmo ato, e quem precisar dela aponta.
  - **Portador do checkpoint (`TK-37`, `DU-8`).** A skill nova declara a **Orquestração** como quem
    grava o checkpoint de contexto; o texto que atribuía o ato à Execução **sai** (é resíduo
    pré-`DP-N`). Nenhuma responsabilidade nova é criada; se a transposição exigir uma, **para e
    escala** (Regra 8) em vez de criá-la.
  - **Vocabulário final desde o nascimento (`T23b` absorvida).** A skill nova usa exclusivamente a
    lista final da `DP-F` (`ready`, `in-progress`, `review`, `done`, `blocked`, `cancelled`), aponta
    para a residência única em vez de reenunciar estados, e onde citar `superseded` nomeia que está
    no vocabulário de **plano/iniciativa**.
  - **Nenhuma regra de escolha de tarefa muda de efeito** — só de lugar e de termo.
- **Invariantes:** nada de `.claude/kit-exclude.txt`/`sync-kit.ps1` muda; nenhum consumidor é tocado
  (`DA-3`); material sem portador achado na transposição vira linha no `TK-38` (`DU-9`), nunca
  invenção na skill nova.
- **Verificação:** bateria do §3; `Grep -r 'proximo-passo|handover' .claude/skills/` devolvendo só o
  que a `AUT-T7` ainda vai tratar (nenhuma ocorrência normativa dentro das skills tocadas aqui);
  Grep pelo texto dos gates no kit → **uma** ocorrência normativa, demais são ponteiro; os dois
  diretórios antigos ausentes da árvore.
- **Pronto quando:** existe **uma** skill de passagem de bastão, invocada pelo `scrum-master`, com os
  gates definidos num lugar só, o portador do checkpoint declarado e nenhuma regra de escolha alterada
  em efeito.

### AUT-T7 — As superfícies que apontavam para a skill aposentada [Opus · classe redacao · teto 30]
- **Não delegável antes da `AUT-T6` `done`** — a varredura mede o resultado dela.
- **Objetivo:** `G-SURFACE` — a mudança estruturante regulariza a superfície de contato **inteira**, no
  ato. Nenhum artefato publicado continua mandando invocar uma skill que não existe.
- **Arquivos-alvo, com a contagem medida em 2026-08-22 (remedir na entrada):** `README.md` (3,
  inclusive o **§9 inteiro** — *Handover e uma tarefa por contexto*); `GOVERNANCA.md` (5 — §4 nas
  linhas `:333`/`:338`/`:341`/`:342`, cerimônias em `:240`, e o *enforcement* dos **itens 8 e 9 do
  §7**, "gate de review no handover"); `.claude/README.md` (1); `.claude/skills/diario-de-obras/SKILL.md`
  (2); `.claude/skills/bootstrap-pantonic/SKILL.md` (1);
  `.claude/global/docs/GOVERNANCA_MEMORIAS.md` (1); `docs/DOC_MAP.md` (1).
- **Fora do alvo, e é regra:** `CHANGELOG.md` (4), `docs/DIARIO_DE_OBRAS.md` (29), `docs/audits/*`,
  `docs/RDO/*` e todos os `docs/plans/P-*.md` — registro histórico não se reescreve (invariante 3). No
  diário, **só marcador vivo** migra, e isso é escopo da `AUT-T9`.
- **Conteúdo:** substituir a invocação da skill morta pela nova onde o texto é **normativo**; onde o
  texto descreve o **fluxo** (README §9, `GOVERNANCA.md` §4 e cerimônias), reescrever para o fluxo
  vigente — a transição é maquinário do `scrum-master`, transparente ao gerente. Os itens 8 e 9 do §7
  passam a cobrar o gate onde ele agora mora, sem criar guardrail novo.
- **Invariantes:** **nenhum guardrail novo** e nenhuma renumeração da lista do §7; nenhuma regra muda
  de efeito; `redacao-doc` normativa em tudo que é publicado.
- **Verificação:** bateria do §3; `Grep 'proximo-passo|skills/handover'` no repo, excluído o recorte
  histórico declarado acima, com resultado **vazio**; `check-readme.ps1` em exit 0.
- **Pronto quando:** nenhum artefato publicado invoca skill inexistente, e cada sobrevivente do Grep
  está dentro do recorte histórico declarado.

### AUT-T8 — Doutrina: `status` de tarefa × veredito de rubrica, e as arestas de `superseded` [Opus · classe redacao · teto 30]
- **Herda:** a `T26` do `P-0734` (`### T26`, linhas 847-877) e o `TK-30`. **Não delegável antes da
  ratificação da `DP-I`** — o lugar onde o `status` é materialmente gravado é o que a `DP-I` fixa, e
  esta tarefa **transcreve** esse lugar sem reinterpretá-lo.
- **Objetivo:** a doutrina passa a distinguir sem ambiguidade dois vocabulários que hoje compartilham
  palavras — `status` de tarefa e veredito de rubrica —, e o único estado terminal de plano deixa de
  existir sem gatilho de entrada nem aresta.
- **Arquivos-alvo, com a contagem medida em 2026-08-11 (remedir na entrada):** `GOVERNANCA.md` (12);
  `docs/RUBRICA_DE_REVISAO.md` (15); `ARQUITETURA_PANTONICA.md` (3);
  `.claude/skills/diario-de-obras/SKILL.md` (`## Status — residência única`); `README.md` §7 (espelho
  da residência única, por `G-SURFACE`).
- **Conteúdo:**
  - **`GOVERNANCA.md`** — o vocabulário de `status` segue a lista final; a matriz de responsabilidades
    registra a fronteira da `DP-G` (o `scrum-master` é o único que **materializa** o `status`, em
    qualquer estado; o executor é **autor** de `review` e `blocked`, e de mais nada) e que **o laudo é
    escrito só pelo `reviewer`**, sem recopiar a lista de estados.
  - **`docs/RUBRICA_DE_REVISAO.md`** — a expectativa medida é **quase nenhuma substituição**: as
    ocorrências são veredito (`conforme`/`parcial`/`não conforme`); o trabalho é tornar isso explícito
    onde o texto ficar ambíguo. Se a substituição for zero, **registrar "zero" como resultado**, não
    como omissão.
  - **`ARQUITETURA_PANTONICA.md`** — só o que for vocabulário de status de tarefa.
  - **`TK-30`, rota fixada pelo dono em 2026-08-13** — a residência única em
    `.claude/skills/diario-de-obras/SKILL.md` ganha, **no vocabulário de plano/iniciativa**, os três
    fatos hoje órfãos sobre `superseded`: é **terminal**, **condensa para o histórico** e **sai do
    backlog** (não é escolhível); e ele entra na **Lista final** e na **Máquina de transições** com
    gatilho de entrada e aresta. **A `DP-F` não se reabre** — as arestas são de plano, não de tarefa.
    O `README.md` §7 espelha o resultado no mesmo ato.
- **Invariantes:** pesos, faixas e dimensões da rubrica **não mudam**; o termo *inspetor* não entra em
  artefato nenhum; a doutrina não ganha regra nova aqui além das arestas que o `TK-30` já pedia.
- **Cuidado:** `GOVERNANCA.md` é doc grande — entrar por `docs/DOC_MAP.md` e Grep de âncora, nunca
  Read integral.
- **Verificação:** bateria do §3; Grep dos termos mortos nos arquivos-alvo, com resultado vazio ou com
  cada sobrevivente justificado por escrito como veredito/homônimo; `check-readme.ps1` em exit 0.
- **Pronto quando:** os dois vocabulários estão distinguíveis sem ambiguidade, `superseded` tem
  gatilho e aresta na fonte da verdade, e o espelho concorda com ela.

### AUT-T9 — Conformidade: kanban, planos vivos e varredura de fecho [Opus · classe redacao · teto 30]
- **Herda:** a `T27` do `P-0734` (`### T27`, linhas 879-915), na fatia que a `DU-10` lhe atribui.
  **Absorve** `TK-04` e `TK-42`. **Não delegável antes da `AUT-T6`, `AUT-T7` e `AUT-T8`** — a
  varredura mede o resultado das três.
- **Objetivo:** o registro material do `status` — kanban e planos vivos — passa à lista final, e o
  repositório é varrido para provar que não sobrou vocabulário morto vivo.
- **Arquivos-alvo, com a contagem medida em 2026-08-11 (remedir na entrada):**
  `docs/DIARIO_DE_OBRAS.md` (39, **só marcadores vivos**); `docs/plans/_INBOX.md` (12);
  `docs/plans/P-0734-execucao-autonoma.md` (46, **só os marcadores vivos**);
  `docs/plans/P-0733-divida-do-hub.md` (1); `docs/RDO/P-0734-T11-skill-scrum-master-o-loop.md` (1);
  mais `.claude/agents/pantonic-executor.md:20` (`TK-04`); `tests/test_review_evidence.py` (docstring
  de `test_escopo_violado_gera_fato_sem_inventar_parcial`) e `.claude/README.md` (nota dos auditores)
  (`TK-42`).
- **Conteúdo:**
  - **Só marcador vivo migra** — o que descreve o estado **atual** de tarefa, plano ou tíquete.
    Bullets de fechamento, dossiês de decisão, RDO emitido e prosa que narra o ocorrido ficam como
    estão; marca de revogação **não é** reescrita.
  - **Varredura de fecho** sobre o repo, excluído o recorte histórico: Grep de cada termo morto e do
    termo `inspetor`; cada sobrevivente classificado e justificado por escrito.
  - **`TK-04`** — `.claude/agents/pantonic-executor.md:20` deixa de hardcodar "orçamento esperado
    ~≤40 tool uses" e passa a **apontar** para a autoridade numérica única (`GOVERNANCA.md` §3, tabela
    de tetos por classe). Nenhum número novo entra no prompt.
  - **`TK-42`** — duas edições textuais, sem mudança de comportamento: a docstring que ainda cita
    *"pacote de retorno"* (objeto morto desde a `DP-H`) e a nota dos auditores de `.claude/README.md`
    que ainda manda apontamentos virarem tíquetes "via `pantonic-planner`".
  - **Resíduo em código vira tíquete, não edição** — exceto as duas edições nominais do `TK-42`,
    nenhum `.py` é renomeado aqui.
- **Invariantes:** nenhum bullet histórico reescrito; nenhuma edição de comportamento em `.py`; o
  diário é editado **por âncora**, nunca por reescrita de seção.
- **Verificação:** bateria do §3; a varredura registrada com a contagem final por termo e a
  justificativa de cada sobrevivente; `python -m pytest` sem regressão.
- **Pronto quando:** todo marcador vivo usa a lista final, todo sobrevivente está justificado por
  escrito, e `TK-04` e `TK-42` estão fechados.

### AUT-T10 — `README.md`, `CHANGELOG.md`, veredito do dono e as três recomendações [Opus + dono · classe redacao · teto 30]
- **Herda:** a `T17` do `P-0734` (`### T17`, linhas 624-660). **Absorve** `TK-46` e `TK-18`. É a
  **última** tarefa do plano e a que o fecha.
- **Objetivo:** dever 2 do `G-README` — a sprint encerra com a revisão do documento canônico, e o gate
  de sentido é do dono, único teste que o guarda não faz.
- **Arquivos-alvo:** `README.md` (papéis, fluxo de execução, anatomia do kit, contagens, e o
  `:352-354` do `TK-46`); `CHANGELOG.md` seção `## [Não lançado]`; `docs/plans/_INBOX.md` (as três
  linhas de recomendação); `docs/DIARIO_DE_OBRAS.md` (veredito).
- **Forma, nesta ordem:**
  1. **`CHANGELOG.md` `[Não lançado]`** — bloco consolidado: a skill única de passagem de bastão e a
     aposentadoria de `proximo-passo`/`handover`, o RDO gerado no fechamento, as correções de
     instrumento, a doutrina de `status` × veredito. **Proibido:** número de versão novo, tag,
     instrução de migração por número (`DE-7`).
  2. **`TK-46`** — `README.md:352-354` afirma que "o hook de aviso fica fora do kit"; contradiz
     `GOVERNANCA.md` §3.1, onde a **declaração** do hook é canônica e versionada e só o arquivo que o
     harness lê é ponto de carga. Corrigir a frase (remedir a linha por Grep).
  3. **`TK-18` — revisão final do espelho.** Varrer as **14 seções** com `> Fonte da verdade:`
     declarada contra as fontes correspondentes; o guarda verifica que a fonte existe, **não** que o
     texto concorda. Registrar o que fica sob guarda executável e o que permanece sob conferência
     humana.
  4. `pwsh -NoProfile -File .claude/checks/check-readme.ps1` — paridade estrutural. **Instrumento
     desta atividade, nunca gate automático de pronto.**
  5. **Leitura corrida do README pelo dono:** (a) o texto descreve o framework que ele governa? (b)
     alguma afirmação está equivocada, confusa ou desatualizada? (c) um cliente decidiria adotar — ou
     rejeitar — com base nisto, e a decisão seria justa?
  6. **Emitir as três recomendações do §8** como três linhas em `docs/plans/_INBOX.md`, cada uma com o
     que absorve. Autorar os planos é ato posterior, **fora desta tarefa**.
  7. **Veredito** registrado no diário, e o fechamento da iniciativa `EXECUCAO-AUTONOMA`.
- **Verificação:** veredito registrado; reprovação gera rodada nova de redação, **não segue adiante**;
  as três linhas existem no `_INBOX.md`, com o contador de próximo id atualizado.
- **Pronto quando:** aceite explícito do dono registrado no diário, `TK-46` e `TK-18` fechados, as
  três recomendações emitidas. **Fecha o plano e a iniciativa.**

## 7. Ordem de execução

`AUT-T1` → `AUT-T5` → `AUT-T4` → `AUT-T2` → `AUT-T3` → **[ratificação em lote do dono, `DU-12`]** →
`AUT-T6` → `AUT-T7` → `AUT-T8` → `AUT-T9` → `AUT-T10`.

**Por que esta ordem** (valor testável cedo, fatias verticais finas):

1. `T1` limpa o kanban — sem ela, toda escolha de tarefa seguinte lê um backlog que mente.
2. `T5` entrega valor no primeiro contexto: os dois instrumentos que **toda** tarefa usa param de
   exigir escrita à mão. É verificável pelo dono no ato (uma linha de telemetria apendada pelo
   instrumento).
3. `T4` fecha a mecânica do documental; `T3` depende dela (`DP-J` opera sobre o `pacote`), e `T2` é
   independente — as duas param juntas, com a medição do `TK-27`, num **único** round-trip.
4. `T6` é o coração do objetivo herdado e vem logo após a ratificação; `T7` regulariza a superfície no
   ato (`G-SURFACE`); `T8` depende da `DP-I` ratificada; `T9` mede o resultado das três.
5. `T10` fecha com o dono e emite as recomendações.

**A numeração não é a ordem** — os identificadores seguem o esqueleto registrado na rodada de
consolidação, e a ordem de execução é esta seção (mesmo padrão do `P-0735` §5).

## 8. Saída da `AUT-T10` — as três recomendações de plano

Não são tarefas deste plano. São **linhas de `docs/plans/_INBOX.md`** emitidas pela `AUT-T10`, para
autoria posterior, uma a uma, em contexto novo:

- **(a) Piloto medido do loop.** Absorve o corpo integral da `T16` do `P-0734` (cancelada por
  absorção, §4): escopo do piloto, medidas contra a série de `docs/telemetria.tsv`, registro
  qualitativo de cada acionamento do dono **pela causa**, gate explícito de reprovação e o critério de
  aceitação do §19 do `P-0734` (**uma só** ocorrência de acionamento em caminho feliz reprova). É a
  única prova de que o desenho entrega o que promete, e por decisão do dono (`DU-3`) roda em plano
  próprio, depois deste.
- **(b) Otimização do contexto do `scrum-master`.** Medida de entrada:
  `.claude/skills/scrum-master/SKILL.md` tem **21.660 chars** — maior que a maior fonte do pickup
  medido no `P-0736`; e o custo fixo de entrada de um pickup é 33.932 chars (43,8%) antes de tocar
  fonte do projeto. Absorve o `TK-23`. **Não** reabre o orçamento do `proximo-passo`: aquela questão
  está **abolida** (custo transitório de skill descontinuada).
- **(c) Otimização dos contextos dos agentes instanciados pelo `scrum-master`.** Absorve o `TK-32`
  (uso e teto como medida de **agregado**, com regime interino de teto não-bloqueante) e o
  desdobramento do item 4 da `T17` — a matéria de uso, teto, alarme e telemetria se revê **inteira e
  em plano próprio**, com a medição obrigatória dos três números sobre `docs/telemetria.tsv`: (i)
  quantas tarefas **por classe** cruzaram o teto e por quanto, (ii) em quantos cruzamentos a
  consequência prescrita de fato ocorreu, (iii) o custo do **próprio controle** em turnos.

## 9. Achados da execução

*(vazio na publicação; cada tarefa apende aqui o que achar fora do próprio escopo)*

- **2026-09-15 — `P-0739` registrado (enabler, não derivado A/B).** O plano `docs/plans/P-0739-backlog-instrumento.md` entrega `.claude/tools/backlog.py` (`next`/`status`/`drain`/`check`) e a gramática legível por máquina do kanban. Consequência para a `AUT-T6`: a skill `passagem-de-bastao` **embrulha** o instrumento em vez de transpor a heurística de priorização/drenagem em prosa; a `BKL-T8` edita transitoriamente `proximo-passo`/`handover`/`scrum-master` para invocar o instrumento — a `AUT-T6` encontra essas skills já apontando para ele. Status deste plano inalterado (`blocked` pela `TK-54`).

## 10. Fora de escopo (explícito)

- **O piloto**, a **otimização de contexto do `scrum-master`** e a **dos agentes instanciados** —
  `DU-3`, §8.
- **A matéria de uso e teto** (`TK-32`, `T34` cancelada, `DP-L` não formada) — recomendação (c).
- **O orçamento do `proximo-passo`** — questão **abolida** por decisão do dono: custo transitório de
  skill marcada para descontinuação, e atrasar a aposentadoria por defeito já mapeado é desperdício.
- **Canal novo para o executor** — `DU-8`: nenhuma razão tipada nova, nenhum campo novo de sinal.
- **Propagação aos consumidores** — `DA-3` mantida: hub primeiro, medir, depois propagar; nenhum dos
  derivados é tocado, e `sync-kit.ps1` fica inalterado.
- **Reabertura de decisão ratificada** — `DP-A`..`DP-S`, `DE-7`, `DA-3` e `DL-1`..`DL-10` são insumo,
  não matéria.
- **Bump e tag** — `DE-7`, versão congelada em `0.0.0`.

## 11. Riscos

| Risco | Sinal | Resposta |
|---|---|---|
| A `AUT-T6` esbarrar em responsabilidade que a matriz não declara | a transposição precisar atribuir ato a papel que a matriz não endossa | **para e escala** (`G-SCOPE`, guardrail 15; Regra 8) — não cria a responsabilidade no prompt |
| A `AUT-T5` estourar por acumular três frentes | gate de delegação medir mais write-clusters que o limite | **partição pelo planejamento** (`T5a`/`T5b`), sem mudança de rota nem de escopo — precedente medido no `P-0735` `T7` |
| A ratificação em lote (`DU-12`) devolver decisão diferente da recomendada | o dono recusar a proposta da `DP-I`, da `DP-J` ou a rota do `TK-27` | a materialização é **card autorado** depois da ratificação; nenhuma tarefa deste plano assume o resultado antecipadamente |
| A `DU-8` ser recusada pelo dono no veredito da `AUT-T10` | o dono discordar de que o portador do checkpoint é a Orquestração | a rota volta ao `TK-37`, reaberto como owner-gated; a skill nova é a única superfície a reconciliar |
| Drift de volta: a execução abrir tarefas novas de conformidade | card novo nascendo fora do §6 sem decision record | achado vira **tíquete**, nunca tarefa deste plano (`G-PLANFIDELITY`) |

## Dossiês fechados por decisão

*(`### DP-I` é criada pela `AUT-T2`; `### DP-J`, pela `AUT-T3` — `DU-7`)*
