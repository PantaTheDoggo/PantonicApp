# P-0747 — O consultor de plano: a figura, a triagem de toda parada e a fronteira com o planejador

**Data:** 2026-09-22 · **Origem:** pedido do dono em 2026-09-22 (transcrito na §0) · **Plano de
origem:** nenhum. Absorve o tíquete `TK-75`, anunciado em `docs/DIARIO_DE_OBRAS.md:20` e nunca aberto
(`DCS-1`). Consome como insumo a `docs/consultant-spec.md` e as seções `## 9` e `## 10` do `P-0740` ·
**Status:** `done` · 2026-09-23 · **Marco 1 aceito pelo dono em 2026-09-23** sobre a versão 1 do modelo, verbatim: *"A definição de objetos no modelo ficou bom"* e *"inicie o plano 747"*; a forma das tabelas do modelo foi ao `TK-76`, que roda antes deste plano e não o toca ·
**Ordem de execução:** CON-T1 → CON-T2 → CON-T3 → CON-T3a → CON-T4 → CON-T2a → CON-T3b → CON-T4a → CON-T3c → CON-T5 → CON-T6 → CON-T5a → CON-T6a → CON-T7 → CON-T7a → CON-T8 → CON-T8a → CON-T2b → CON-T3d · **Prefixo das tarefas no diário:** `CON-T<n>` (materializa `OP-<n>`) · **Prefixo das
decisões:** `DCS-<n>` · **Checagem de versão do kit:** modo hub, congelada em `0.0.0`
(`GOVERNANCA.md` §10) · **Branch de trabalho:** `plan/planner-modelo-escopo`, sem commit (`DCS-16`).

## 0. O problema, verbatim

**Pedido do dono, 2026-09-22:**

> Inicie o plano do consultor, avaliando a spec existente, e aplicando as novas roles do planner e do
> model designer. Durante o processo, colete impressões e adicione aos resultados o veredito dos
> procedimentos incluídos nos planos recentes

A segunda frase é dever de quem conduz a sessão, não escopo deste plano. "Aplicando as novas roles"
é instrução sobre como planejar (modelo primeiro, um card por operação), não entrega.

**Atos do dono que compõem o enunciado — lastro do modelo:**

1. `docs/DIARIO_DE_OBRAS.md:166` (2026-09-18): *"O dono declarou que vai **detalhar esta figura e as
   fronteiras dela com o `pantonic-planner` em plano próprio**; até lá o agente é provisório, não é
   doutrina de `GOVERNANCA.md` §3 e não se cita como fonte normativa. Nesta transição o
   `scrum-master` aciona o consultor no lugar de abrir rodada fria de planejador."*
2. `docs/DIARIO_DE_OBRAS.md:176` (2026-09-19, `DM-28`): *"sempre que a tarefa demandar uma técnica
   ainda a ser projetada, faça ad-hoc. Execução ad-hoc vira insights para planejamento da técnica a
   ser materializada em sequência"*.
3. `docs/DIARIO_DE_OBRAS.md:180` (2026-09-19, `DM-45` iii): *"**Ao perceber que se aproxima do
   próprio limite, o consultor promove handover** — estado do cenário, escalonamentos abertos, o que
   estava em curso — e o **`scrum-master` descomissiona a instância e provisiona outra**, repassando
   esse handover. A **forma de comunicação é ad-hoc** neste plano (`DM-28`) e entra na **spec do
   consultor** (`LM-T9`) para resolução no plano próprio"*.
4. `docs/DIARIO_DE_OBRAS.md:182` (2026-09-19, `DM-45` iv): *"registrar, a cada acionamento, **o que
   o motivou, que classe de impedimento era e o que ficou inconclusivo**, produzindo o **panorama dos
   pontos inconclusivos** que serve de insumo à **spec de robustez**."*
5. `docs/DIARIO_DE_OBRAS.md:192` (2026-09-19): *"**O consultor segue ad-hoc — a figura ainda não foi
   criada.** A `docs/consultant-spec.md` é insumo, não criação: enquanto o agente não for materializado
   por plano próprio, o `pantonic-consultant` permanece provisório"*.
6. `docs/DIARIO_DE_OBRAS.md:194` (2026-09-19): *"São duas, e não se confundem: a **spec do
   consultor** (`docs/consultant-spec.md`, que existe) e a **spec de robustez** (que ainda não tem
   arquivo; o `TK-55` é o acumulador dela)."*
7. `docs/consultant-spec.md:149-160` (2026-09-22, `DC-1`..`DC-4`): questão não correlata ao modelo
   conceitual é tática, e tática é da figura (`DC-1`). A guarda é o drift do modelo: havendo drift, a
   figura para e pede a decisão do dono (`DC-2`). Decisão técnica ou tática da figura não passa por
   validação do dono, verbatim *"Eu não vou validar a decisão dele para questões técnicas e
   táticas."* (`DC-3`). A figura é o ponto de triagem de toda parada de executor e decide entre model
   designer, planejador ou resolver ela mesma (`DC-4`). Precedência, `:169-171`: *"Enquanto o bloco A
   não for reescrito, **a spec prevalece**: toda parada de executor aciona a figura."*
8. `docs/DIARIO_DE_OBRAS.md:12-29` (2026-09-22): a decisão de abrir este planejamento, e as três
   residências que contradizem a spec — (a) a skill `scrum-master`, (b) `GOVERNANCA.md` §3 e §7
   itens 17-18, (c) `.claude/agents/pantonic-consultant.md`.
9. `docs/plans/P-0746-lastro-do-modelo.md:65-71` (2026-09-21, sobre o drift na execução autônoma):
   *"E mesmo a execução autônoma tem marcos de descanso e validação. Nesses pontos também é feita a
   revisão do modelo pelos drifts que porventura tenham surgido durante a execução. **O loop autônomo
   carrega o drift até o marco.** No marco, o drift é validado e o plano continua, ou recusado, e as
   tarefas retroagem onde ocorreu o drift."* — transcrito em 2026-09-23 por `DCS-24`, como lastro da
   `OP-3` e do estado final de `consultor.fronteira com o modelador`.

**O que o plano entrega quando termina:** o consultor deixa de ser figura ad-hoc e passa a papel
de doutrina, com a linha dele na matriz de `GOVERNANCA.md` §3. Toda parada de executor é triada por
ele em todas as residências do kit (`F-4`, 47 itens). A fronteira com o planejador e com o modelador fica
escrita nos três lados. As lacunas da §10 da spec ficam fechadas por norma ou com residência
nomeada. A forma efêmera com cenário persistido roda como piloto e sai medida.

## 1. Modelo conceitual

> **Como ler esta seção.** Versão 2, vigente desde o aceite do dono no marco de fechamento de
> 2026-09-23. O que ela mudou sobre a versão 1, e por quê, está em `### 1.4 Registro de versões`.
> O **consultor** é o único objeto de escopo: o plano o leva de figura ad-hoc a papel de doutrina,
> e as oito operações agem só sobre ele. O **planejador** e o **modelador** são externos: o que os
> cards escrevem neles é a fronteira do consultor, nada além. A **parada de executor** e o
> **acionamento do consultor** são medição. Cada um dos 50 itens de `F-4` é alcançado pelo texto
> de exatamente uma operação, e o contrato do consultor diz qual. Todo elemento tem lastro num dos
> nove atos do dono da `## 0` ou no pedido de 2026-09-22. O que não tem lastro mora em
> `## Requisitos secundários`.

**Estado do modelo:** versão 2 · 2026-09-23 · autor: modelador · 5 objetos · 8 operações · 12 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem | lastro na §0 | tipo |
|---|---|---|---|---|---|---|
| consultor | a figura que recebe toda parada de executor, decide se a resolve ou para onde ela vai, e devolve a rota ao loop — e o conjunto de residências que a governam, que é onde ela de fato existe | estatuto na doutrina, alcance da triagem das paradas, fronteira com o planejador, fronteira com o modelador, forma da figura, registro dos acionamentos, lacunas deixadas pela especificação, descrição pública da figura | residências: **a lista `F-4` da `## 2`, itens 1 a 50, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44, 45 e 48; `OP-5` itens 25 a 38 e 49; `OP-6` itens 42, 43 e 50; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`) | OP-1 | pedido: *"Inicie o plano do consultor"*; ato 1: *"detalhar esta figura e as fronteiras dela com o `pantonic-planner` em plano próprio"* | escopo |
| planejador | o papel que decompõe o plano em cards e mantém a lista de tarefas de cada operação — o lado da fronteira para onde vai o que o consultor não fecha | autoria da decomposição do plano | não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 13, 19, 20 e 25 — é a fronteira do consultor e nada além: a rodada de replanejamento chega pela rota `planejador` da triagem, só quando emenda aceita cria ou remove operação ou quando a premissa cai inteira (`superseded`), e o corretivo `T<n>a` da mesma operação, com o id apensado à lista `tarefas:`, passa a ser também ato do consultor (`DCS-4`). O que `DCS-18` deixa com o planejamento continua com ele. Alterar outra conduta do planejador é colateral e se escala | externo | ato 1: *"as fronteiras dela com o `pantonic-planner`"*; ato 7 (`DC-4`): *"decide entre model designer, planejador ou resolver ela mesma"* | externo |
| modelador | o papel único que escreve todo ato sobre a `## 1` de um plano — o lado da fronteira para onde vai o drift do modelo | autoria exclusiva do modelo | não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 26, 27 e 28 — é a fronteira do consultor e nada além: o consultor é nomeado como quem origina o dossiê de `emenda` e como quem apensa o id do corretivo à lista `tarefas:`; quem despacha continua sendo quem conduz a sessão (`I-2`). Os literais que a guarda executável prende no arquivo dele (`F-15`) ficam. O instrumento do modelo e seus testes não se tocam | externo | ato 7 (`DC-2`, `DC-4`): *"havendo drift, a figura para e pede a decisão do dono"*; *"decide entre model designer, planejador ou resolver ela mesma"* | externo |
| parada de executor | a devolução `blocked` de um executor, com o motivo `premissa`, `dependencia` ou `ferramenta`, e o laudo do revisor com pendência substantiva — não o plano não-pronto no gate nem o contexto acabando dentro da tarefa (`DCS-18`) | caminho até a resolução | nenhuma operação altera uma parada. O que se observa nela, antes e depois, é o caminho: quem a recebe, quem decide a rota e onde isso fica registrado. As paradas do `P-0745` e do `P-0746` (`F-8`) são o retrato do antes; o depois são as paradas da janela de execução deste plano, lidas no arquivo de estatística de `DCS-8` a partir do aceite da `OP-2` | externo | ato 7 (`DC-4`): *"ponto de triagem de toda parada de executor"*; `:169-171`: *"toda parada de executor aciona a figura"* | medição |
| acionamento do consultor | cada vez que o loop leva uma parada à figura e recebe a rota de volta | custo por acionamento | nenhuma operação altera um acionamento. O que se observa nele é o custo, apurado pelo método de `F-7`; a sonda é descartável e não vira artefato. Retrato do antes: as instâncias 1-4 da forma standby (`F-7`) e a série de `F-8`; o depois: os acionamentos da janela de execução deste plano a partir do aceite da `OP-4` | externo | pedido: *"avaliando a spec existente"*; ato 4: *"registrar, a cada acionamento"*; ato 3: *"Ao perceber que se aproxima do próprio limite"* | medição |

### 1.2 Fluxo de operações

**A. A figura entra na doutrina**

- **OP-1** — O redator da norma faz do consultor um papel de doutrina: dá a ele a linha própria na matriz de responsabilidades, tira das linhas de quem planeja, de quem orquestra e de quem executa a ideia de que toda parada sobe ao planejamento, e põe na triagem dele a escada de revisão, a reprovação depois da última tentativa e as regras de escalonamento e de não perguntar; escreve ainda o dever dele de validar no marco e de emitir a emenda, e a lista de tarefas de cada operação que ele passa a poder estender com o card corretivo.
  - `precisa de: parada de executor, planejador, modelador` · `altera: consultor.estatuto na doutrina, consultor.alcance da triagem das paradas, consultor.fronteira com o planejador, consultor.fronteira com o modelador` · `tarefas: CON-T1` · `lastro: ato 1, até lá o agente é provisório, não é doutrina de GOVERNANCA §3; ato 7, a figura é o ponto de triagem de toda parada de executor; ato 8, as três residências que contradizem a spec`
- **OP-2** — O autor de papéis reescreve a definição de conduta do consultor sobre a norma nova: tira dela o estatuto provisório, faz qualquer das três razões de parada acioná-lo, dá a ele a rota que devolve, os deveres de validar a emenda do modelo no marco e de emiti-la quando a resolução muda o que o plano entrega, a linha de estatística que ele apensa a cada acionamento e a saída curta por edição mínima.
  - `precisa de: consultor, parada de executor, planejador, modelador` · `altera: consultor.estatuto na doutrina, consultor.alcance da triagem das paradas, consultor.fronteira com o planejador, consultor.fronteira com o modelador, consultor.registro dos acionamentos, consultor.lacunas deixadas pela especificação` · `tarefas: CON-T2, CON-T2a, CON-T2b` · `lastro: ato 5, enquanto o agente não for materializado por plano próprio permanece provisório; ato 4, registrar a cada acionamento o que o motivou, que classe de impedimento era e o que ficou inconclusivo; ato 7, havendo drift a figura para e pede a decisão do dono`

**B. O loop tria e despacha pela figura**

- **OP-3** — O mantenedor do loop reescreve a condução das paradas: as duas fontes normativas da skill passam a citar as decisões deste plano, toda regra que roteia parada de executor ou laudo com pendência substantiva e o guardrail que manda a matéria ao planejador passam a levá-los ao consultor, o loop despacha a rota que ele devolve e, quando a rota é o modelador, despacha o modelador sem parar a janela e leva o pedido de validar o drift ao dono no marco; quando o consultor classifica o impedimento como estratégico, o loop para em qualquer rota e leva ao dono a classificação, a rota e o pedido de emenda, se houver; em resolver e em modelador para sem executar a ação e sem despachar o modelador, e em planejador executa a ação, que já é a parada. Quando o consultor recusa o impedimento como improcedente, o loop devolve a mesma tarefa à fila com a linha nova que ele gravou e a redespacha sem gastar a retentativa.
  - `precisa de: consultor, parada de executor, planejador, modelador` · `altera: consultor.alcance da triagem das paradas, consultor.fronteira com o planejador, consultor.fronteira com o modelador` · `tarefas: CON-T3, CON-T3a, CON-T3b, CON-T3c, CON-T3d` · `lastro: ato 7, enquanto o bloco A não for reescrito a spec prevalece, toda parada de executor aciona a figura; ato 8, a skill scrum-master contradiz a spec; ato 9, o loop autônomo carrega o drift até o marco`
- **OP-4** — O mantenedor do loop instala a forma efêmera do consultor com o cenário persistido, numa seção própria da skill e não num passo novo: cada acionamento nasce uma instância que lê o cenário do plano e o card em causa, decide, reescreve o cenário com edição mínima e se encerra; o cenário passa a ser o próprio handover, a retomada da instância de prontidão sai da nota de telemetria, o reprovisionamento por limite deixa de existir, e as linhas do corpo do agente e da regra do loop que o descrevem instanciado uma vez por plano passam a descrevê-lo efêmero.
  - `precisa de: consultor, acionamento do consultor` · `altera: consultor.forma da figura, consultor.lacunas deixadas pela especificação` · `tarefas: CON-T4, CON-T4a` · `lastro: ato 3, ao perceber que se aproxima do próprio limite o consultor promove handover, e a forma de comunicação entra na spec do consultor para resolução no plano próprio; pedido, avaliando a spec existente`

**C. O outro lado da fronteira e a especificação**

- **OP-5** — O autor de papéis escreve o outro lado da fronteira em toda definição de conduta que ainda manda a parada direto ao replanejamento: quem planeja passa a receber a rodada pela rota da triagem, quem escreve o modelo passa a nomear o consultor como origem da emenda e como quem estende a lista de tarefas, quem executa e quem revisa passam a devolver a parada e a pendência à triagem, e as regras do diário sobre revisão pedida e transição de estado, a passagem de bastão e a regra global de não decidir passam a dizer o mesmo.
  - `precisa de: consultor, planejador, modelador, parada de executor` · `altera: consultor.fronteira com o planejador, consultor.fronteira com o modelador, consultor.alcance da triagem das paradas` · `tarefas: CON-T5, CON-T5a` · `lastro: ato 1, detalhar esta figura e as fronteiras dela com o pantonic-planner; ato 7, decide entre model designer, planejador ou resolver ela mesma`
- **OP-6** — O redator da especificação a converte em lastro medido: o estatuto dela passa a apontar para a norma e para a definição de conduta, cada lacuna que ela deixava aberta ganha o ponteiro para a regra que a fecha ou para a residência que a recebe, e o índice de documentos deixa de descrevê-la como a única fonte da figura e passa a indexar o cenário e a estatística.
  - `precisa de: consultor` · `altera: consultor.estatuto na doutrina, consultor.lacunas deixadas pela especificação` · `tarefas: CON-T6, CON-T6a` · `lastro: ato 5, a spec é insumo, não criação; ato 6, a spec do consultor e a spec de robustez não se confundem; pedido, avaliando a spec existente`

**D. O piloto se mede e a porta de entrada se atualiza**

- **OP-7** — O medidor confronta o piloto da forma efêmera com a forma anterior: apura o custo de cada acionamento da janela pelo método já medido, conta as reprovações por perda de cenário e grava, na seção de custo da especificação, o veredito de adotar, recusar ou declarar a amostra insuficiente.
  - `precisa de: consultor, acionamento do consultor` · `altera: consultor.forma da figura` · `tarefas: CON-T7, CON-T7a` · `lastro: ato 2, execução ad-hoc vira insights para planejamento da técnica a ser materializada em sequência; pedido, avaliando a spec existente`
- **OP-8** — O mantenedor leva a figura nova à porta de entrada do repositório: a tabela de guardrails deixa de rotear o escalonamento ao planejador, a linha do consultor na tabela de agentes deixa de anunciá-lo instanciado uma vez e mantido de prontidão, e a descrição curta do agente é reescrita no mesmo ato em que o índice gerado do kit é regenerado, os quatro passando a descrever o papel de doutrina, a triagem de toda parada e a forma que o veredito do piloto deixou vigente.
  - `precisa de: consultor` · `altera: consultor.descrição pública da figura` · `tarefas: CON-T8, CON-T8a` · `lastro: ato 5, o consultor segue ad-hoc, a figura ainda não foi criada; ato 1, detalhar esta figura em plano próprio`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final | lastro na §0 |
|---|---|---|---|
| consultor.estatuto na doutrina | figura ad-hoc e provisória: a `description` diz *"Figura ad-hoc, provisória"* e o arquivo declara que não é doutrina, não está em `GOVERNANCA.md` §3 e não se cita como fonte normativa (`F-2`); a matriz não tem linha dele (`F-3`, `F-4` item 16); a spec é a única descrição da figura, e o índice de documentos a descreve assim (item 43). A spec afirmava prevalecer sobre o bloco A (item 50) | papel de doutrina em duas residências — a linha na matriz de `GOVERNANCA.md` §3 e a definição de conduta sem estatuto provisório —; a spec permanece como lastro medido e não normativo, com o estatuto apontando para as duas e o índice de documentos dizendo o mesmo | ato 1: *"até lá o agente é provisório, não é doutrina de `GOVERNANCA.md` §3"*; ato 5: *"permanece provisório"* |
| consultor.alcance da triagem das paradas | a parada vai aonde o motivo manda: 50 residências (`F-4`) roteiam parada de executor ou citam o consultor, e a maioria manda ao planejador — `A3b`, `A7`, `B1`, `G-REPLAN`, `G-NOASK`, as linhas de planejamento, orquestração e execução da matriz, a escada de revisão *"e só ele"*, o executor, o revisor, o diário, na revisão pedida por quem executa e na transição de estado, a passagem de bastão e a Regra 8 —; o agente só se aciona por `dependencia` ou `premissa`, sem citar `ferramenta`; a spec manda toda parada à figura e prevalece por precedência do dono | toda parada de executor — `premissa`, `dependencia` ou `ferramenta` — e todo laudo com pendência substantiva chegam ao consultor, que devolve uma rota entre resolver, modelador e planejador, e o loop a despacha; o motivo é evidência, não rota; nenhum dos 50 itens de `F-4` manda a parada direto ao planejador, e as duas fontes normativas da skill do loop citam as decisões deste plano; o que `DCS-18` deixa fora continua indo ao planejamento. Exceção: com a linha `estrategico=`, o loop para em qualquer rota e leva a classificação ao dono. Em `resolve` e `modelador`, para sem executar a ação e sem despachar o modelador. Em `planejador`, executa a ação, que já é a parada. Na rota resolver, o consultor pode recusar o impedimento como improcedente. Declara a razão no registro dos acionamentos. O card volta à fila com ao menos uma linha nova. O redespacho não gasta a retentativa. | ato 7 (`DC-3`, `DC-4`, `:169-171`); ato 8: *"as três residências que contradizem a spec"* |
| consultor.fronteira com o planejador | não escrita em lado nenhum: a rodada de replanejamento chega *"só a você"* ao planejador, o corretivo `T<n>a` é ato dele e a lista `tarefas:` é lastro só dele (`F-4` itens 19, 20, 25, 26 e 28); na prática o consultor já autorou três corretivos no `P-0745` sem escalar (`F-8`) e nunca reabriu o objetivo do plano em 37 acionamentos (`F-10`) | escrita nos três lados — norma, agente do consultor, agente do planejador —: o consultor fecha o técnico e o tático (reescreve card, reordena fila, repara instrumento, toma decisão nova com id, autora o corretivo da mesma operação e apensa o id à lista `tarefas:` dela); vai ao planejador só quando emenda aceita cria ou remove operação ou quando a premissa cai inteira; nunca reabre o objetivo do plano | ato 1: *"as fronteiras dela com o `pantonic-planner`"*; ato 7 (`DC-1`, `DC-3`, `DC-4`) |
| consultor.fronteira com o modelador | a doutrina já dá ao consultor validar a versão pendente no marco e emitir o dossiê de emenda (`F-3`, `F-4` itens 18 e 19), mas o agente não carrega nenhum dos dois deveres; o modelador recebe a emenda *"no dossiê de quem a tomou"*, sem nomear o consultor (item 27) | havendo drift — resolução que altera objeto, operação ou estado final da `## 1` —, o consultor devolve o dossiê `Ato de modelo` de `emenda` com o reparo e marca a rota `modelador`; o loop despacha o modelador sem parar a janela e a versão pendente coexiste com a vigente até o marco, onde o pedido de validar ou recusar o drift sobe ao dono; recusado, o consultor resolve preservando o modelo; o agente do consultor carrega os dois deveres e o do modelador o nomeia como origem da emenda | ato 7 (`DC-2`): *"havendo drift, a figura para e pede a decisão do dono"*; ato 9 |
| consultor.forma da figura | standby: *"instanciado uma vez"* por execução e retomado por `SendMessage`, sem passo de instanciação, handover nem reprovisionamento na skill do loop (`F-6`); a instância do `P-0745` cresceu de 70.3k a 368.5k em oito acionamentos (`F-8`); o handover por limite é ad-hoc (ato 3) | efêmera com cenário persistido, instalada pela seção `## Acionamento do consultor` da skill do loop: o cenário do plano, com teto de 15k tokens, é o handover, e o reprovisionamento por limite deixa de existir; o corpo do agente e a regra do loop deixam de descrevê-lo instanciado uma vez (`F-4` itens 44 e 45); ao fim do plano a forma leva o veredito medido do piloto, gravado na §11 da spec (item 46) — adotada; ou recusada, com achado em `## 9` e rota para plano novo de standby com aquecimento; ou em amostra insuficiente, com linha nova na §11 da spec e o piloto seguindo na próxima execução | ato 3: *"a forma de comunicação é ad-hoc neste plano … para resolução no plano próprio"*; ato 2: *"Execução ad-hoc vira insights"* |
| consultor.registro dos acionamentos | em prosa, sem residência estruturada: a tabela da §9 da spec reconstrói o histórico, e o panorama dos pontos inconclusivos não tem onde se acumular | residência estruturada, uma linha por acionamento apensada pelo consultor — o que o motivou, a classe do impedimento, a rota e o que ficou inconclusivo —, com o consumidor declarado no acumulador da spec de robustez; a prosa histórica não se migra | ato 4: *"o que o motivou, que classe de impedimento era e o que ficou inconclusivo"*; ato 6 |
| consultor.lacunas deixadas pela especificação | sete abertas (`F-9`): forma do handover, residência da estatística, norma de autoria de card novo, critério de não-acionamento na entrada, caminho de poluição, forma da figura, disciplina de saída | as sete fechadas: cinco por norma — handover e forma pelo cenário persistido, estatística pela residência estruturada, autoria de card novo pela fronteira com o planejador, disciplina de saída por regra do agente — e duas por residência nomeada — não-acionamento no `TK-55`, poluição pela regra geral do agente —; cada item da §10 da spec aponta para o que o fecha | pedido: *"avaliando a spec existente"*; ato 3: *"entra na spec do consultor … para resolução no plano próprio"* |
| consultor.descrição pública da figura | a porta de entrada anuncia o agente *"instanciado uma vez, mantido de standby"* e a tabela de guardrails roteia o escalonamento *"ao planejador"* (`F-4` itens 39 e 40); a `description` do agente o anuncia *"instanciado UMA vez"*, *"mantido de standby"* e *"Figura ad-hoc, provisória"* (item 47), e a região gerada do índice do kit a repete (item 41) | a porta de entrada, a `description` do agente e a região gerada, regenerada no mesmo ato, descrevem o papel de doutrina, a triagem de toda parada e a forma que o veredito do piloto deixou vigente; *"O kit são dez agentes"* fica igual | ato 5: *"O consultor segue ad-hoc — a figura ainda não foi criada"* |
| planejador.autoria da decomposição do plano | decompõe o plano em cards e mantém a lista de tarefas de cada operação | o mesmo, inalterado: este plano não o transforma; o que muda na definição de conduta dele é a fronteira do consultor, que é propriedade do consultor | ato 1; ato 7 (`DC-4`) |
| modelador.autoria exclusiva do modelo | todo ato sobre a `## 1` de um plano é dele, e só dele | o mesmo, inalterado: o consultor origina a emenda e nunca a escreve | ato 7 (`DC-2`, `DC-4`) |
| parada de executor.caminho até a resolução | segue o motivo: parte vai ao planejador pela `A3b`, parte ao consultor ad-hoc, e a rota não fica registrada em residência estruturada; no `P-0745` o consultor resolveu as sete como táticas enquanto a superfície ainda mandava ao planejador, e a `PLN-T2` subiu ao dono como três opções táticas (`F-8`) | passa sempre pela triagem do consultor, com a rota registrada numa linha por acionamento; sobe ao dono só o drift do modelo. Nenhuma operação a altera: a diferença entre as duas colunas é o que **prova** que a figura foi transformada | ato 7 (`DC-3`, `DC-4`): *"Eu não vou validar a decisão dele para questões técnicas e táticas."* |
| acionamento do consultor.custo por acionamento | forma standby: de $3,7 a $4,5 por acionamento nas instâncias 1-4, com a reescrita de cache entre 25% e 48% do custo porque o cache de subagente expira em 5 min, e zero reprovações (`F-7`) | medido sob a forma efêmera pelo mesmo método e lido pela regra pré-decidida: média abaixo de $3,7 com zero reprovações por perda de cenário adota a forma — a estimativa é de $1,2 a $1,5. Nenhuma operação o altera: é a medida que prova ou recusa a forma nova | pedido: *"avaliando a spec existente"*; ato 3: *"se aproxima do próprio limite"* |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 2 | 2026-09-23 | vigente | modelador — conflito apurado pelo revisor da `CON-T3b` (`DCS-28`). A `OP-3` e o estado final de `consultor.alcance da triagem das paradas` não cobriam a classificação estratégica. Com ela, o loop para em qualquer rota. Em `resolve` e `modelador`, para sem executar a ação. Em `planejador`, a ação já é a parada e se executa. Reescrita no lugar quatro vezes no mesmo dia, sem versão 3. Pelo segundo conflito (`AE-11` (i), `DCS-30`), a `F-4` passa a 48 itens e o item 48 cabe à `OP-4`. Pelo terceiro (laudo da `CON-T3c`, `DCS-30` (i), `AE-12`), a exceção de `planejador` é fixada e as contagens do estado passam a 48. Pelo quarto (`DCS-31`, `AE-16`), a `F-4` passa a 50 itens. O item 49 cabe à `OP-5`, que alarga o texto às regras do diário sobre revisão pedida e transição de estado. O item 50 cabe à `OP-6`. Dois estados iniciais ganham o fato novo. Pela emenda do dono (`DCS-35`, `AE-22`), o consultor pode recusar o impedimento como improcedente na rota resolver. O card volta à fila com linha nova, e o redespacho não gasta a retentativa. Muda o texto da `OP-3` e o estado final do alcance. Nenhum dos cinco atos muda objeto. Validada pelo consultor antes da emenda (`DCS-34`). Aceita pelo dono no marco de fechamento em 2026-09-23: *"pode fechar esse plano"* |
| 1 | 2026-09-22 | obsoleta | modelador — autoria sobre o dossiê do planejador, reescrita no lugar por quatro dossiês antes do Marco 1 e validada nele em 2026-09-23. Caiu pelo aceite da versão 2 no marco de fechamento de 2026-09-23 |

---

## Requisitos secundários

> Residência do elemento sem lastro nos atos do dono da `## 0` (`GOVERNANCA.md` §3.2; skill
> `diario-de-obras`, *Modelo de domínio (seção do plano)*). Nada aqui é contrato: são entregas que o
> agente julga necessárias para que o modelo não seja prejudicado, e a responsabilidade por elas é
> inteira dele.

| requisito | por que o agente o julga necessário | quem responde |
|---|---|---|
| a atualização de literal em `tests/test_doutrina_unidade.py` só quando o literal pertence à regra que o card reescreve (`F-15`, `I-5`, `## 8`) | a guarda executável prende literais das residências editadas; sem a atualização, a reescrita correta aparece como regressão | agente |
| `backlog.py check` e `modelo.py check` rodados com `docs/plans/_CENARIO-P-NNNN.md` presente (`## 8`) | o arquivo novo mora em `docs/plans/`, e os instrumentos que leem essa pasta não podem tomá-lo por plano | agente |

## 2. Fatos estabelecidos

- **F-1 — Não existe plano vivo sobre o consultor.** `_INBOX.md` está sem linha viva. O índice do
  diário não tem o tema (`docs/DIARIO_DE_OBRAS.md:221-258`). O `TK-75` não existe como cabeçalho:
  a única ocorrência é `docs/DIARIO_DE_OBRAS.md:20`. Fonte: dossiê do condutor e Q7, 2026-09-22.
- **F-2 — O agente hoje.** `.claude/agents/pantonic-consultant.md` tem 67 linhas. Frontmatter:
  `model: opus` e `tools: Read, Glob, Grep, Bash, Write, Edit`. A `description` diz *"Figura ad-hoc,
  provisória"*. O estatuto (`:14-18`) diz que o arquivo *"não é doutrina publicada, não está em
  `GOVERNANCA.md` §3 e não se cita como fonte normativa"*. Seções: `:20` *Por que você existe*,
  `:29` *O que você faz*, `:49` *O que você não faz*, `:62` *Coesão do seu contexto*. O `:35-37`
  aciona por `blocked` `dependencia` ou `premissa` e **não cita `ferramenta`**. O item 3 (`:37-47`)
  enumera *"decisão nova com id, cards reescritos, fila reordenada, achado absorvido com ponteiro"*.
  O arquivo não contém as `DC-*` nem o dever de validar no marco. Fonte: Q3.
- **F-3 — Deveres que a doutrina já dá ao consultor e o agente não carrega.** `GOVERNANCA.md:400`:
  *"primeiro o consultor; validando ele, o dono"*. `GOVERNANCA.md:424`: *"consultor | devolve o
  dossiê `Ato de modelo` de emenda junto com o reparo do escalonamento"*. A matriz de §3
  (`GOVERNANCA.md:85-97`) não tem linha do consultor. Fonte: dossiê do condutor e Q2.
- **F-4 — Superfície que roteia parada de executor ou cita o consultor. Esta é a residência única da
  lista: os cards e o contrato do objeto `consultor` a copiam ou citam pelo número do item e nunca a
  reenunciam.** Linhas medidas em 2026-09-22 pelo planejador (Grep `ao planejador|ao
  planejamento|só a você|e só ele|A3b|replanejamento|consultor` sobre `GOVERNANCA.md`, `README.md`,
  `.claude/agents`, `.claude/skills`, `.claude/global/CLAUDE.md`), somadas às linhas de Q1-Q7 e ao
  achado do modelador sobre o lastro.
  1. `.claude/skills/scrum-master/SKILL.md:18-27` — *Estado do loop*: fonte normativa = `P-0734`
     `### DP-B`, `### DP-Q`, `### DP-G` item 3.
  2. `.claude/skills/scrum-master/SKILL.md:148-159` — passo 8 (tabela do bloco A em ordem de
     precedência; despacho do modelador quando o reviewer traz dossiê `Ato de modelo`).
  3. `.claude/skills/scrum-master/SKILL.md:185` — o hook de telemetria não dispara na retomada por
     `SendMessage`, e a linha é apensada pelo loop.
  4. `.claude/skills/scrum-master/SKILL.md:196` — passo 9: *"o stderr vai ao consultor como
     escalonamento"*.
  5. `.claude/skills/scrum-master/SKILL.md:215-217` — fonte normativa das tabelas de roteamento =
     `P-0734` (`### DP-A`, `### DP-B`, `### DP-G` item 4, `### DP-K` §14.4), e *"Divergência entre
     esta tabela e essas seções resolve a favor da seção"*.
  6. `.claude/skills/scrum-master/SKILL.md:225-227` — `A3a`/`A3b`/`A3c`. A `A3b` diz *"A escalada é
     ao **planejador**"*, e a `A3c`, sem fallback, *"a recusa sobe como matéria de plano"*.
  7. `.claude/skills/scrum-master/SKILL.md:229` — `A6a`, que já escala ao consultor.
  8. `.claude/skills/scrum-master/SKILL.md:230` — `A7`: *"A escalada é a do `A3b`"*.
  9. `.claude/skills/scrum-master/SKILL.md:231` — `A8a`, que roteia a pendência ao consultor pelo
     `B1`.
  10. `.claude/skills/scrum-master/SKILL.md:253` — `B1`, que escala ao consultor. O parêntese
      `` (`pantonic-consultant`, instanciado uma vez por execução) `` não entra aqui: é o item 45.
  11. `.claude/skills/scrum-master/SKILL.md:258-268` — lista *O que obriga parada*.
  12. `.claude/skills/scrum-master/SKILL.md:323-324` — guardrail: *"a matéria ao planejador"*.
  13. `GOVERNANCA.md:91` — matriz, linha *Planejamento*: *"indício de que o plano precisa mudar chega
      aqui e só aqui"*.
  14. `GOVERNANCA.md:92` — matriz, linha *Orquestração*: *"obstáculo à rota e dossiê não fechado sobem
      ao **planejamento**"*.
  15. `GOVERNANCA.md:93` — matriz, linha *Execução*: *"a escalada é ao planejamento"*.
  16. `GOVERNANCA.md:85-97` — a matriz não tem linha do consultor.
  17. `GOVERNANCA.md:100-109` — *Escada de revisão de plano*: quem recebe é o planejador *"e só
      ele"*.
  18. `GOVERNANCA.md:400` — no marco, a validação é *"primeiro o consultor; validando ele, o dono"*.
  19. `GOVERNANCA.md:423-424` — tabela *Quem escreve*: a linha *planejador* dá a ele a lista
      `tarefas:` *"na decomposição e em toda rodada de replanejamento"*, e a linha *consultor* devolve
      o dossiê de emenda.
  20. `GOVERNANCA.md:435-441` — parágrafo *Lastro*: *"é do planejador, que a preenche na decomposição
      e a estende em rodada de replanejamento com o card corretivo"*.
  21. `GOVERNANCA.md:509-513` — `reprovado` depois da última retentativa: *"a matéria vai ao
      replanejamento"*.
  22. `GOVERNANCA.md:908-945` — `G-REPLAN`, item 17: escalada ao planejador, e o enforcement cita
      *"`A3b` da skill `scrum-master` (escala ao planejador, não ao dono)"*.
  23. `GOVERNANCA.md:946-972` — `G-NOASK`, item 18: *"O destino do bloqueio é o planejamento"* e
      *"`B1` roteia ao planejador"*.
  24. `.claude/agents/pantonic-consultant.md` — o corpo do arquivo (`F-2`): estatuto `:14-18`,
      `:20-28`, itens 2-4 de *O que você faz* `:35-47` e *O que você não faz* `:49-60`. Fora deste
      item: a `description` `:3`, que é o item 47, e as linhas de forma `:8-12`, `:31-34` e `:62-67`,
      que são o item 44.
  25. `.claude/agents/pantonic-planner.md:417-440` — *Rodada de replanejamento*: *"chega a você, só a
      você"*, e o card corretivo `T<n>a` com a lista `tarefas:` como *"lastro que é seu"*.
  26. `.claude/agents/pantonic-model-designer.md:30` — *"que é do planejador depois da autoria"*.
  27. `.claude/agents/pantonic-model-designer.md:66` — a emenda chega *"no dossiê de quem a tomou"*,
      sem nomear o consultor.
  28. `.claude/agents/pantonic-model-designer.md:110` — *"depois é lastro do planejador"*.
  29. `.claude/agents/pantonic-executor.md:30-39` — *"quem o conserta é o planejador"* e *"Quem recebe
      é o planejamento"*.
  30. `.claude/agents/pantonic-executor.md:50-51` — *"(roteamento `A3b` do `scrum-master`: para a
      janela e escala ao dono/planejador)"*.
  31. `.claude/agents/pantonic-executor.md:119` — *"quem recebe a escalada e decide é o
      planejador"*.
  32. `.claude/agents/pantonic-reviewer.md:125-126` — o loop roteia a pendência *"ao
      **planejamento**"*, e *"ao dono chega só o que o planejador classificar como estratégico"*.
  33. `.claude/skills/diario-de-obras/SKILL.md:89` e `:102` — a transição `blocked` → `review` é
      *"do **planejador**, na rodada de replanejamento"*.
  34. `.claude/skills/passagem-de-bastao/SKILL.md:136` — *"escala ao consultor com o stderr"*.
  35. `.claude/skills/passagem-de-bastao/SKILL.md:236-239` — obstáculo no meio da janela vira
      *"rodada de replanejamento como próxima tarefa"*.
  36. `.claude/skills/passagem-de-bastao/SKILL.md:260-265` — rodada *"delegada ao
      `pantonic-planner`"*.
  37. `.claude/skills/passagem-de-bastao/SKILL.md:285-286` — *"indício de que o plano precisa mudar vai
      ao planejador"*.
  38. `.claude/global/CLAUDE.md:163-166` — Regra 8: *"registra o achado e escala para
      replanejamento"*.
  39. `README.md:775` — tabela de guardrails, item 17: *"roteada ao planejador"*.
  40. `README.md:812` — linha do agente: *"instanciado uma vez, mantido de standby"*.
  41. `.claude/README.md:16` — região gerada `kit:agents`. Regenera-se por
      `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` e nunca se edita à mão.
  42. `docs/consultant-spec.md` — estatuto `:3-5` e §10 `:399-418`. A §11 é o item 46.
  43. `docs/DOC_MAP.md:162-184` — entrada da spec (*"~339 linhas"*, *"Não é doutrina"*, §10 com
      *"cinco matérias"*). Recebe as residências novas de `DCS-6` e `DCS-8`.

  44. `.claude/agents/pantonic-consultant.md:8-12` (*"você **não é efêmero**: é instanciado uma
      vez"*), `:31-34` (item 1, *"Absorve o cenário na instanciação"*) e `:62-67` (*Coesão do seu
      contexto*: *"Você atravessa **um plano**"*). São as linhas que descrevem a forma da figura.
  45. `.claude/skills/scrum-master/SKILL.md:253` — só o parêntese
      `` (`pantonic-consultant`, instanciado uma vez por execução) `` da `B1`, que descreve a forma.
  46. `docs/consultant-spec.md:422-479` — §11, *Custo por acionamento*: residência do veredito do
      piloto (`DCS-7`).
  47. `.claude/agents/pantonic-consultant.md:3` — `description:` do frontmatter, *"instanciado UMA vez
      por execução de plano e mantido de standby … Figura ad-hoc, provisória"*. É a fonte da região
      gerada do item 41 (`F-16`).
  48. `.claude/skills/scrum-master/SKILL.md:222` — a cláusula do consultor na linha `A1` do bloco A
      (*"Consultor: **nenhuma** retomada — a instância caída se descarta … Caiu de novo no mesmo
      acionamento: **PARA**"*), escrita pela `CON-T4a` (`DCS-29`) e medida em 2026-09-23 pelo consultor
      (acionamento 5). Descreve a forma da figura, como o item 44; entra na partição da `OP-4` pelo
      dossiê de conflito de `DCS-30` (`AE-11` i), na versão 2 pendente.
  49. `.claude/skills/diario-de-obras/SKILL.md:79-83` — parágrafo acima da *Máquina de transições*: *"Plano cuja
      revisão foi pedida por quem executa ou orquestra é caso de `blocked` **de plano**"* e *"abre uma **rodada de
      replanejamento**"*. Roteia toda revisão pedida por quem executa ao replanejamento, sem triagem, três linhas
      acima do item 33, que o censo enumerou (o Grep atingiu a `:81` por *replanejamento* e o item 33 não a absorveu).
      Achado pelo revisor da `CON-T5` (`AE-14` i); partição da `OP-5` pelo dossiê de conflito de `DCS-31`, na versão 2
      pendente.
  50. `docs/consultant-spec.md:167-169` — §3, subseção *Ato do dono de 2026-09-22*, parágrafo *Consequência sobre a
      §2*: *"Enquanto o bloco A não for reescrito, **a spec prevalece**: toda parada de executor aciona a figura"*.
      Escrito na spec pelo ato do dono, antes deste plano, e fora dos sete termos do censo (diz *figura*, não
      *consultor*); caduco desde a `CON-T3`. Achado pelo revisor da `CON-T6` (`AE-15`); partição da `OP-6` pelo dossiê
      de conflito de `DCS-31`, na versão 2 pendente.

  **Fora da lista, por `DCS-18`** (não são parada de executor): plano não-pronto no gate de
  delegação — `.claude/skills/passagem-de-bastao/SKILL.md:93` e `:129`, `README.md:472`,
  `.claude/global/CLAUDE.md:162` —; contexto acabando dentro da tarefa — `GOVERNANCA.md:633`,
  `.claude/skills/passagem-de-bastao/SKILL.md:223`, `README.md:710` —; e `README.md:476`, *"bloqueio
  que exija replanejamento"*, que continua verdadeiro sob a rota `planejador`. Sem linha de
  roteamento: as demais skills e agentes (Q1). As skills `proximo-passo` e `handover` não existem
  mais.
- **F-5 — Guardas que travam a superfície.** `.claude/checks/check-readme.ps1:143` casa
  `'^O kit são (.+?) agentes'`, e `:161` acusa divergência com o número de arquivos em
  `.claude/agents/`. `README.md:800` diz *"O kit são dez agentes"*. `tests/test_doutrina_unidade.py`
  prende literais de `GOVERNANCA.md`, `.claude/global/CLAUDE.md`, `pantonic-planner.md`, da skill
  `diario-de-obras` e de `README.md`. Nenhum teste prende a matriz, os itens 17-18 de §7, o bloco A
  da `scrum-master` nem o `pantonic-consultant.md`. Fonte: Q6.
- **F-6 — Mecanismo atual de acionamento.** A skill `scrum-master` não tem passo de instanciação,
  standby, handover nem reprovisionamento. A única frase é *"instanciado uma vez"* (`:253`), e o
  `SendMessage` aparece só na nota de telemetria (`:185`). Fonte: Q5.
- **F-7 — Custo medido por acionamento, forma standby** (`docs/consultant-spec.md:428-434`): de $3,7
  a $4,5 por acionamento nas instâncias 1-4. A reescrita de cache vai de 25% a 48% do custo porque o
  cache de subagente expira em 5 min. As instâncias 1-4 fecharam com zero reprovações. A forma
  efêmera foi estimada em $1,2–1,5 (`:452-462`). Método da medida (`:424-426`): transcripts
  deduplicados por `message.id`, preços Opus a $5/M de entrada, $25/M de saída, cache read a 10%
  e cache write a 125%. A sonda era descartável e não é artefato do repositório.
- **F-8 — Série de 2026-09-22.** `docs/telemetria.tsv`, linhas 550-599, tem 14 linhas
  `*-consultor-*`. A instância do `P-0745` cresceu de 70.3k para 368.5k em 8 acionamentos. A do
  `P-0746`, de 180.1k para 266.8k em 5. No `P-0745` o consultor resolveu as sete paradas como
  táticas e autorou `PLN-T4a`, `PLN-T5a` e `PLN-T7a` sob a `DC-4`, sem escalar. A `PLN-T2`,
  anterior à `DC-4`, subiu ao dono como três opções táticas (`docs/DIARIO_DE_OBRAS.md:30-35`).
- **F-9 — Lacunas que a spec deixa abertas** (`docs/consultant-spec.md:399-418`, residência da lista):
  forma do handover · residência estruturada da estatística · norma sobre autoria de card novo ·
  critério de não-acionamento na entrada · caminho de poluição · forma da figura · disciplina de
  saída.
- **F-10 — Fronteira medida com o planejador** (`docs/consultant-spec.md:211-214`): em 37
  acionamentos a figura *"nunca reabriu o objetivo do plano"*.
- **F-11 — Tíquetes vizinhos.** `TK-55` (`ready`, `docs/DIARIO_DE_OBRAS.md:1811`) é o acumulador da
  spec de robustez. `TK-70` (`ready`, `:3020`) trata *"A vigência bilateral do modelo e a conduta de
  drift do loop … na skill scrum-master e em GOVERNANCA.md §4.5"*. Fonte: Q7.
- **F-12 — Precedente de arquivo não-plano em `docs/plans/`.** Existem `_VIABILIDADE-agente-leitor.md`
  e `_CARD-revisao-critica-pickup-opus.md`, e `backlog.py check` saiu `0` no fechamento do `P-0745`
  com eles presentes (`docs/DIARIO_DE_OBRAS.md:9`).
- **F-14 — As duas residências novas não são ignoradas pelo git.** Medido em 2026-09-22:
  `git check-ignore -q docs/ACIONAMENTOS_CONSULTOR.tsv` e `git check-ignore -q
  docs/plans/_CENARIO-P-0747.md` saem os dois com exit `1` (não ignorado).
- **F-15 — Literais presos por `tests/test_doutrina_unidade.py`** (medido em 2026-09-22):
  - `GOVERNANCA.md` tem de conter `materialização de uma operação do modelo`, `**Lastro.**` e
    `**Rascunho antes do Marco 1.**`.
  - `.claude/agents/pantonic-model-designer.md` tem de conter `Só cinco violações`, `` `V1` e `V3` `` e
    `` exceto `V1` e `V3` ``.
  - `.claude/agents/pantonic-planner.md` tem de conter `SAÍDA 3`, `Fase 3b` e `Nenhum teto se escreve
    no`.
  - `.claude/global/CLAUDE.md` não pode conter `tarefa atômica`.
  - `README.md` tem de conter `71 turnos e ~189 mil tokens`.
- **F-16 — A região gerada acompanha a `description` e é gate.** Em 2026-09-22,
  `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` imprime
  `kit_check: check-drift OK - .claude/README.md == regenerado (10 agente(s), 11 skill(s))` e sai
  `0`. O check-drift compara a região `kit:agents` de `.claude/README.md` com as `description` dos
  agentes, e faz parte do gate da skill `guardrails-check` (`.claude/skills/guardrails-check/SKILL.md:34`).
  Mudar a `description` de um agente sem regenerar a região deixa o gate vermelho.
- **F-13 — Instrumentos.** `python .claude/tools/modelo.py check --plano <plano>` (exit 0/1/2);
  `python .claude/tools/backlog.py check`; `python -m pytest -q`, que deu `277 passed` no fechamento
  do `P-0745` (referência histórica datada, re-medir no despacho).

## 3. Decisões

| id | valor | razão |
|---|---|---|
| `DCS-1` | O plano absorve a matéria do `TK-75`, que não se abre. A linha 20 do diário passa a apontar para este plano (ato da orquestração). | Uma iniciativa, um plano vivo. A matéria do tíquete (as residências que contradizem a spec) é a superfície de `F-4`. |
| `DCS-2` | A figura vira doutrina em duas residências: uma linha na matriz de `GOVERNANCA.md` §3 e o arquivo do agente, sem estatuto provisório. A `docs/consultant-spec.md` fica como lastro medido e não normativo. O estatuto dela passa a apontar para as duas residências e cada item da §10 ganha ponteiro para o que o fecha. As três contagens defasadas (`:12-30`) não se corrigem. | Ato 1 da §0 ("em plano próprio") e G-SCOPE (papel declarado só na matriz). O não-reparo das contagens é ato do dono de 2026-09-19 (ato 6 da §0). |
| `DCS-3` | Toda parada de executor (`premissa`, `dependencia`, `ferramenta`) e todo laudo com pendência substantiva vão ao consultor. Ele devolve uma rota ∈ {`resolve`, `modelador`, `planejador`}, e o loop despacha. `A3a`/`A3b`/`A3c`, passo 8, lista *O que obriga parada*, `B1`, `G-REPLAN` e `G-NOASK` são reescritos nesse sentido. | `DC-4`. "Nenhum agente aciona outro" (`pantonic-model-designer.md:83-84`). O `motivo=` é evidência, não rota (`DP-G` item 1 do `P-0734`). |
| `DCS-4` | Fronteira com o planejador. O consultor fecha o técnico e o tático: reescrever card, reordenar fila, reparar instrumento, decisão nova com id e card corretivo `T<n>a` da mesma operação, cujo id ele apensa à lista `tarefas:` daquela operação. Vai ao planejador só quando uma emenda do modelo, já aceita, cria ou remove operação (Fase 3b das operações novas) ou quando a premissa cai por inteiro (`superseded`). Nunca reabre o objetivo do plano. | `DC-1`, `DC-3`, `DC-4`; `F-8` (três `T<n>a` medidos sob a `DC-4`); `F-10`. |
| `DCS-5` | Drift. Quando a resolução altera objeto, operação ou estado final da `## 1`, o consultor devolve o dossiê `Ato de modelo` de `emenda` (seis campos, forma vigente) e marca a rota `modelador`. O loop **para** e leva o dossiê ao dono. Com `go`, despacha o modelador. Com recusa, o consultor resolve preservando o modelo — a cláusula de parada da janela foi substituída por `DCS-24` em 2026-09-23. O dever de validar no marco (`GOVERNANCA.md:400`) e o de emitir a emenda (`:424`) entram no agente. O modelador passa a nomear o consultor como origem de `emenda`. | `DC-2`. A forma que o dono lê já existe (o dossiê), então há default e não há pergunta. `F-3`. |
| `DCS-6` | Forma da figura: **efêmera com cenário persistido**, em piloto. Cada acionamento nasce uma instância que lê o cenário e o card em causa, decide, reescreve o cenário com `Edit` mínimo e encerra. Residência do cenário: `docs/plans/_CENARIO-P-NNNN.md`, com teto de 15k tokens e conteúdo = decisões vivas, fila, achados abertos, matéria inconclusiva. O cenário tem autoridade sobre o plano para o que cobre. O handover da spec §8 passa a ser o próprio cenário, e o reprovisionamento por limite deixa de existir. A `scrum-master` ganha o passo de despacho efêmero. | `docs/consultant-spec.md:452-462` (decisão por piloto já tomada). Prefixo `_` pelo precedente `F-12`. Fecha dois itens de `F-9`: handover e forma. |
| `DCS-7` | O piloto roda na janela de execução deste plano, a partir do aceite da operação que instala o despacho efêmero. A medida é a penúltima operação, `classe investigacao`, pelo método de `F-7`. Regra de veredito: **adota** se a média de $/acionamento ficar abaixo de $3,7 e houver zero reprovações por perda de cenário. Caso contrário **recusa**: vira achado em `## 9` com rota "plano novo: standby + ping, spec §11 (ii)". Se houver menos de 3 acionamentos, o veredito é `amostra insuficiente`, grava-se como linha nova na spec §11 e o piloto segue na próxima execução de plano. | Spec §11 (i) e (ii). $3,7 é o piso medido da forma standby (`F-7`). |
| `DCS-8` | Estatística de acionamento em residência estruturada: `docs/ACIONAMENTOS_CONSULTOR.tsv`, colunas `data`, `plano`, `acionamento`, `tarefa`, `gatilho` (classe 1-4 da spec §2), `motivo`, `classe_impedimento`, `rota`, `inconclusivo`. O consultor apensa uma linha por acionamento. O consumidor declarado é o `TK-55`. Não se migra a prosa histórica. | `DM-45` iv (ato 4 da §0). As colunas vêm da tabela da spec §9 (`:372`) mais `rota` de `DCS-3`. A tabela da §9 já reconstrói o histórico. |
| `DCS-9` | Disciplina de saída vira regra do agente: `Edit` mínimo, nunca `Write` de seção, e resposta curta. | Spec §11 (iii): "vale para qualquer forma". |
| `DCS-10` | O critério de não-acionamento na entrada fica fora deste plano, com residência no `TK-55`, e se decide sobre a estatística de `DCS-8`. O caminho de poluição mantém a regra geral no agente, sem desenho novo. | Spec §11 (iv): *"não se decide por custo"*. Fecha, por residência nomeada, dois itens de `F-9`. |
| `DCS-11` | Fonte normativa das regras reescritas: `P-0747` `DCS-3`..`DCS-6`, citado ao lado do `P-0734` nos dois cabeçalhos de fonte da skill (`F-4` itens 1 e 5). A cláusula *"Divergência … resolve a favor da seção"* passa a valer também para as seções do `P-0747`. | Sem isso, a divergência entre a `A3b` reescrita e o `P-0734` se resolveria a favor do texto antigo (`F-4` item 5). |
| `DCS-12` | Fronteira com o `TK-70`: este plano não toca `GOVERNANCA.md` §4.5 nem a vigência do modelo. O `TK-70` mantém a conduta de drift do loop. Este plano cuida da triagem de drift **na parada**, feita pelo consultor. | `F-11`. Uma matéria, uma residência. |
| `DCS-13` | A Regra 8 (`.claude/global/CLAUDE.md:164`) passa a dizer que o executor para, registra e devolve `blocked`, e que a rota se decide na triagem. A propagação à cópia do dono em `~/.claude/CLAUDE.md` e aos derivados fica fora. | G-SURFACE (`F-4` item 18). A propagação é ato de outro instrumento (`checar-versao-kit`). |
| `DCS-14` | Todos os itens de `F-4` são regularizados neste plano, nenhum adiado. | G-SURFACE: decisão estruturante regulariza a superfície inteira no mesmo ato. |
| `DCS-15` | Nenhum agente novo nem removido: a frase *"O kit são dez agentes"* (`README.md:800`) fica igual. | `F-5`: o guarda compara a frase com a contagem de arquivos. |
| `DCS-16` | A execução corre em `plan/planner-modelo-escopo`, sem commit (o commit é ato do dono no marco). | Árvore com WIP do `P-0745` e do `P-0746` (`docs/DIARIO_DE_OBRAS.md:42-44`). |
| `DCS-18` | Plano não-pronto no gate de delegação e contexto acabando dentro da tarefa **não** são parada de executor: continuam indo ao planejamento, e as linhas deles ficam fora de `F-4`. | A `DC-4` fala de *"toda parada de executor"*, que é o retorno `blocked` com `motivo=`. Os dois casos não têm esse retorno: um é recusa do loop antes do despacho, o outro é queda sem linha de retorno. |
| `DCS-19` | O despacho efêmero entra na `scrum-master` como seção nova `## Acionamento do consultor`, logo antes de `## Relatório de encerramento`, e não como passo. | *"Dez passos, nesta ordem"* (`.claude/skills/scrum-master/SKILL.md:31`) enumera o fluxo. Um passo novo obrigaria a reescrever a contagem e a numeração dos passos seguintes, citados por outras residências. |
| `DCS-20` | A `description` do consultor (`F-4` item 47) muda na mesma operação que regenera a região gerada (item 41). As linhas de forma do agente e o parêntese da `B1` (itens 44 e 45) mudam na operação que instala a forma efêmera. O veredito do piloto grava-se na §11 da spec (item 46), pela operação que mede. | Três razões: `F-16` (a `description` trocada antes da regeneração deixa o gate de todas as tarefas intermediárias vermelho); propriedade alterada tem de ser declarada pela operação que edita (`consultor.forma da figura`); e cada item de `F-4` fica em exatamente uma operação. |
| `DCS-21` | O retorno do consultor abre com a linha `rota=<resolve|modelador|planejador>`, e a skill do loop a lê no passo 8. | `DCS-3` exige uma rota que o loop leia sem interpretar prosa. Loop que deriva a rota de prosa improvisa, e isso a `DP-G` proíbe. |
| `DCS-22` | A medida do piloto conta como reprovação toda revisão repetida das tarefas `CON-T5`, `CON-T6` e dos corretivos delas, e como retentativa toda execução repetida, lidas em `docs/telemetria.tsv`, sem atribuir causa. | A atribuição "por perda de cenário" de `DCS-7` não é mensurável depois que o laudo morre no consumo (`DP-K` §14.4). A contagem sem atribuição é mais estrita que a regra, e por isso não a relaxa. |
| `DCS-17` | A revisão do `README.md` é a última operação do plano. A medida do piloto (`DCS-7`) é a penúltima. | G-README dever 2. Nada depende da medida além do README, que descreve a forma vigente. |
| `DCS-23` | Ato do dono, 2026-09-23, verbatim: *"Gostaria que você pedisse ao consultor atuar no veredito da melhor forma, tomando as decisões mais corretas. Use o Fable para ele."* O veredito é `docs/plans/_VEREDITO-procedimentos-2026-09-22.md`; as decisões sobre ele são deste consultor, pela `DC-3`, e estão em `DCS-24`..`DCS-26` e no `AE-1` da `## 9`. | Delegação expressa do dono; o técnico e o tático fecham sem validação dele (`DC-3`, ato 7 da §0). |
| `DCS-24` | Drift na parada, lido com o ato do dono de 2026-09-21 (`docs/plans/P-0746-lastro-do-modelo.md` `## 0`: *"O loop autônomo carrega o drift até o marco. No marco, o drift é validado e o plano continua, ou recusado, e as tarefas retroagem onde ocorreu o drift."*): na rota `modelador` o loop **não para a janela** — despacha o `pantonic-model-designer` com o dossiê de `emenda` que o consultor devolveu junto com o reparo do card, a versão pendente nasce como bloco irmão e coexiste com a vigente até o marco, e é no marco que o pedido de validar ou recusar o drift sobe — primeiro ao consultor, validando ele, ao dono (`GOVERNANCA.md` §3.2). Recusado, o consultor resolve preservando o modelo; a retroação das tarefas desde o drift é conduta do loop no marco e fica com o `TK-70` (`DCS-12`). A janela continua parando na rota `planejador` e na classificação `estratégico`. Substitui só a cláusula *"o loop para e leva o dossiê ao dono"* de `DCS-5`; o resto de `DCS-5` fica. Efeito: o texto da `OP-3` e o estado final de `consultor.fronteira com o modelador` na `## 1` (dossiê de autoria, rascunho substituído no lugar) e os textos novos de `CON-T1` (3, 5, 7, 15 e Verificação 17), `CON-T2` (2, 5), `CON-T3` (objetivo, 2, 5, 6, 9, 10) e `CON-T5` (15). | A `DC-2` diz que a figura *para* — ela não resolve com drift — e *pede* a decisão do dono; não diz que o loop para. A spec §3 fixa que o pedido sobe *"nunca por interrupção"*, e o §3.2 vigente já faz a versão pendente coexistir com a vigente até o marco e a valida lá, primeiro pelo consultor. A parada imediata de `DCS-5` era a leitura que contradizia o ato de 2026-09-21, a norma publicada e a própria `DCS-12` (conduta de drift do loop é do `TK-70`). Veredito §4 item 1. |
| `DCS-25` | Destino de cada item do veredito. Roteado com texto pronto: `TK-72` §7 recebe §3.1 (censo de superfície por grep literal com padrão e contagem; exceção nomeada ao `Bash` do planejador), §3.4 (o contrato copiado no card se limita ao que o card precisa; lista de residências por ponteiro ao fato), §3.7 (medida retomada × invocação fria) e §3.8 (ensaio em árvore temporária como modo normal da Fase 4); `TK-67` recebe §3.5 (forma da devolução do modelador, com o campo *Achados fora da seção*), §3.6 (enunciado composto de atos datados, nomeado na norma) e §5 (hook `UserPromptSubmit` e gate `modelo-por-fase`). Registrado sem ação: §3.2, §3.3 e §4 itens 2 (`DCS-4` fica), 3 (`DCS-6`, `DCS-7` e `DCS-22` ficam) e 4 (`DCS-18` fica). O inchaço deste plano pelo contrato copiado (§3.4) **não se repara aqui**: a linha copiada tem 3.761 caracteres em sete cards (~7k tokens de leitura no total), e enxugá-la custa um ato do modelador (294k medidos nos dois dossiês de reautoria) mais sete re-cópias — capacidade, não término. | Teste capacidade × término (spec §2): nada do que os tíquetes recebem termina entrega aberta neste plano. `DCS-4` é a materialização de `DC-1`, `DC-3` e `DC-4` e de `F-8` (três corretivos autorados sob a `DC-4` sem objeção do dono). `DCS-18` é a definição de parada de executor — ampliá-la acrescentaria quatro residências a `F-4`. O critério do piloto é pré-decidido e a amostra curta já tem veredito próprio (`amostra insuficiente`). |
| `DCS-27` | A classificação `estratégico` tem forma mecânica: a linha `estrategico=<uma frase>`, logo abaixo de `rota=`, presente só quando o consultor classifica o impedimento como estratégico; com ela o loop **PARA** em qualquer rota e leva a frase ao relatório de encerramento. Sem ela, `resolve` e `modelador` seguem e `planejador` para (`DCS-24`). O corretivo `CON-T3a` da `OP-3`, autorado pelo consultor (`DCS-4`), leva a forma ao passo 8, a `A3a`/`A3b`/`A3c`/`A6a`/`A7`/`B1` e às duas listas de parada, e publica a linha de coerência do módulo (toda regra que devolve a rota nomeia a parada; nenhuma menção a `rota=resolve` sem a ressalva). | `AE-4`: a `A6a` seguia incondicionalmente e `estratégico` era prosa lida só em dois lugares — loop que deriva parada de prosa improvisa (`DP-G`), o mesmo motivo de `DCS-21`. A forma no agente do consultor (item 24, `OP-2`, já `done`) fica registrada em `AE-5` e vive provisoriamente no cenário. |
| `DCS-26` | O cenário que a `CON-T4` cria aponta para a `## 3` e a `## 9` do plano em vez de enumerar decisões e achados. A instância de prontidão deste plano — a que decidiu sobre o veredito — encerra no aceite da `CON-T4`; o cenário é o seu handover, e toda escalada seguinte nasce efêmera. | O cenário tem autoridade sobre o plano para o que cobre (`DCS-6`): um bloco literal escrito em 2026-09-22 dizendo *"nenhuma decisão de acionamento ainda"* já estaria falso hoje. A `## 6` já diz que todo acionamento após o aceite da `CON-T4` corre na forma nova. |
| `DCS-28` | `estrategico=` suspende a ação da rota. Com a linha presente, o loop **PARA** sem executar a ação própria da rota: o reparo que o consultor já gravou fica no plano (reparo não é rota), o modelador **não** é despachado, e a frase, a rota e o dossiê de emenda, se houver, vão ao relatório de encerramento — o destino nomeado do dossiê é o dono, que decide na retomada; o modelador só se despacha depois do ato dele. Com `rota=planejador` a ação da rota já é a parada, e nada muda ali. Corretivos autorados pelo consultor (`DCS-4`): `CON-T3b` da `OP-3` (passo 8 e lista *Obriga parada*) e `CON-T2a` da `OP-2` (a forma da linha `estrategico=` entra no agente, fechando o inconclusivo de `AE-5`, com a `:19` de `AE-7`). | `AE-6`. `estrategico=` é o que muda escopo ou objetivo do plano ou revoga decisão do dono (`G-NOASK`) — a única matéria que sobe ao dono na parada (`DC-3`); um ato sobre a `## 1` tomado sob essa classificação antes de o dono a ler poria no modelo uma versão pendente por decisão que não é técnica nem tática. Não altera objeto, operação nem estado final da `## 1`: a `OP-3` já diz que a janela para na classificação estratégica; o que faltava era a ordem entre parar e agir. |
| `DCS-29` | Queda de instância do consultor: nenhuma retomada por `SendMessage`. A instância caída se descarta, a telemetria dela registra `PARCIAL — trecho pré-queda não medido`, e o loop despacha uma instância nova com as mesmas três entradas, sobre o cenário como a caída o deixou; segunda queda no mesmo acionamento **PARA**. A `A1` passa a distinguir executor/`reviewer` (retomada) de consultor (descarte e despacho novo), e a seção *Acionamento do consultor* diz o mesmo. Corretivo `CON-T4a` da `OP-4`, autorado pelo consultor (`DCS-4`). Fila: `CON-T4 → CON-T2a → CON-T3b → CON-T4a → CON-T5`. | `AE-8`, `AE-7`. Duas regras para a mesma queda é o defeito de `AE-4` de novo — loop que escolhe entre regras improvisa (`DP-G`). Retomar uma instância efêmera contradiz `DCS-6` (o cenário é o handover); despachar outra é o que a forma já prescreve para todo acionamento. Coerência com a forma instalada, não drift: o estado final de `consultor.forma da figura` não muda. A `:19` do agente estava no item 24 (`OP-2`) e não no 44 (forma) — defeito de partição de `F-4`, reparado pelo corretivo da operação que possui o item. |
| `DCS-30` | Três matérias do acionamento 5, fechadas de uma vez. (i) Com `estrategico=` a suspensão da ação da rota vale para `resolve` e `modelador`; a rota `planejador` executa a sua ação, que já é a parada — plano `blocked`, rodada de replanejamento enfileirada —, e a frase vai junto ao relatório (`DCS-28`, *"nada muda ali"*). Corretivo `CON-T3c` da `OP-3`, autorado pelo consultor (`DCS-4`); fila `CON-T4a → CON-T3c → CON-T5`. (ii) A cláusula do consultor na `A1` da skill do loop entra em `F-4` como item 48, na partição da `OP-4`: dossiê `Ato de modelo` de `conflito` ao modelador, que reescreve a versão 2 pendente **no lugar** (`DLS-16` do `P-0746`), sem versão 3; o estado final de `consultor.forma da figura` não muda (`DCS-29`). (iii) O aposto *"a retomada do executor pela `A1`"* da nota de telemetria do passo 9 não abre card: a superfície da queda (`A1`, seção *Acionamento do consultor*, nota) está saturada — precondição mais rara (queda do `reviewer`) e a regra geral *"um subagente"* já cobre o caso —; acumula como pendência do relatório de encerramento e na coluna `inconclusivo` da estatística (`TK-55`). | `AE-10` (ii), `AE-11`. (i) é término de entrega aberta, não capacidade (spec §2): a `CON-T3b` contradisse a `DCS-28` numa rota, e sem a ação da rota o próximo pickup não encontra a rodada de replanejamento (`G-REPLAN`). (ii) é a própria regra da `OP-4` — residência que cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria —; a `F-4` é da `## 2` e o consultor a edita, a partição é da `## 1` e só o modelador a escreve (`I-3`). (iii) o reviewer mediu que não há contradição, e a quinta edição da skill por achado de revisão sobre a anterior é o sinal de saturação que a spec manda ler antes de abrir card. |
| `DCS-31` | Três matérias do acionamento 6, fechadas em dois corretivos, um por operação. (i) `.claude/skills/diario-de-obras/SKILL.md:79-83` entra em `F-4` como item 49, na partição da `OP-5` (mesmo arquivo do item 33), e o parágrafo passa a dizer o que a skill do loop e `G-REPLAN` dizem: a revisão pedida por quem executa leva a tarefa a `blocked premissa` e a parada à triagem; só a rota `planejador` leva o plano a `blocked` e abre a rodada; nas rotas `resolve` e `modelador` o plano segue. (ii) A Regra 8 de `.claude/global/CLAUDE.md` (item 38) deixa de usar "rota" para o que a triagem decide — a triagem decide *o destino da parada*; "rota aprovada" fica com o sentido do plano. (i) e (ii) no corretivo `CON-T5a` da `OP-5`. (iii) O parágrafo *Consequência sobre a §2* de `docs/consultant-spec.md:167-169` entra em `F-4` como item 50, na partição da `OP-6` (mesmo arquivo do item 42), e vira registro histórico datado: a spec prevaleceu enquanto o bloco A não foi reescrito, e não prevalece mais. Corretivo `CON-T6a` da `OP-6`. Ambos autorados pelo consultor (`DCS-4`); fila `CON-T6 → CON-T5a → CON-T6a → CON-T7`. Itens 49 e 50 vão ao modelador por dossiê `Ato de modelo` de `conflito`, para a versão 2 pendente **no lugar** (`DLS-16` do `P-0746`), com as contagens do estado a 50; nenhum estado final muda. | `AE-14`, `AE-15`. Dois cards e não um: um card materializa uma operação (`G-PLANREADY`, `GOVERNANCA.md` §7 item 11) e o corretivo `T<n>a` é da operação do card que corrige (`DCS-4`); as matérias caem em `OP-5` e `OP-6`, e apensar o reparo da spec à lista da `OP-5` falsificaria o andamento derivado das duas (`modelo.py`). Saturação: nenhuma das três superfícies (parágrafo do diário, Regra 8, spec §3) recebeu card antes deste — primeiro achado em cada uma; capacidade × término: três substituições literais, sem código, medidas na árvore real. Terceira residência fora da `F-4` em três laudos seguidos (`AE-11`, `AE-14`, `AE-15`): o censo da `F-4` foi Grep de sete termos, e falhou nos dois modos — hit não absorvido (a `:81` do diário) e sentido sem termo (a spec diz *figura*); o censo da superfície foi o elo fraco do planejamento, registrado para o `TK-55` e para a régua do `TK-72`. |
| `DCS-32` | O veredito `adotada` da `CON-T7` vale como medida da **forma**: a regra de `DCS-7` é aplicada como está (3 acionamentos, média $2,8 < $3,7, zero reprovações), porque o que a forma ataca — reescrita e releitura de contexto por acionamento — é contagem de tokens, e o método precifica tokens pela mesma tabela Opus nos dois lados. O que a amostra não mede é o consumo de tokens de um modelo distinto para a mesma decisão, e isso a subseção passa a declarar: modelo das instâncias (`claude-fable-5-1`, ato do dono `DCS-23`), $ como preço-Opus-equivalente e não custo real, e reexecução da sonda na primeira execução de plano com o consultor em Opus. Corretivo `CON-T7a` da `OP-7`, entre `CON-T7` e `CON-T8`; `CON-T8` depende dele e usa o par `adotada`. Não estratégico: nada de `DCS-7` é revogado — trocar o veredito para `amostra insuficiente` é que emendaria, depois de ver o resultado, o critério aceito no Marco 1, e o modelo das instâncias foi ato do próprio dono. | `AE-19`; laudo da `CON-T7`. Modelo conferido nos transcripts: todas as mensagens `assistant` das três instâncias em `claude-fable-5-1`. Saturação: primeiro achado na §11 da spec; capacidade × término: uma substituição literal ao fim do arquivo, medida na árvore real. Sem drift: `OP-7` e o estado final de `consultor.forma da figura` (vigente e pendente) dizem *veredito medido do piloto, gravado na §11 — adotada*, e é o que fica. |
| `DCS-33` | A `description` do consultor (item 47) volta ao Texto novo 3 da variante `adotada`, literal: `Efêmero - cada acionamento`. O `: ` que entrou no lugar do ` - ` faz `yaml.safe_load` recusar o frontmatter inteiro — o consultor é o único dos dez agentes que o harness não lê — e a região `kit:agents` de `.claude/README.md` reproduz o defeito porque foi regenerada a partir dele. Corretivo `CON-T8a` da `OP-8`, depois da `CON-T8` e último da fila: uma substituição literal na linha 3 do agente e a regeneração da região no mesmo ato, com a `Verificação` que faltou à `CON-T8` — o parse YAML estrito do frontmatter e a âncora do trecho divergente, não só o prefixo, medidos nos dois mundos. O item (iii) do `AE-20` (`kit_check.ps1 -Mode validate` sai 0 com frontmatter que parser YAML estrito recusa) é capacidade de instrumento: não abre card neste plano, vai a tíquete no encerramento. `README.md` não muda: o *"Efêmero: cada acionamento"* do Texto novo 2 é célula de tabela markdown, onde dois-pontos é legítimo. Não estratégico: nada de escopo, objetivo ou decisão do dono muda — é término da entrega que o estado final da `OP-8` já descreve. | `AE-20`; laudo da `CON-T8` (ressalva 93, `seguir com ressalva`). Medido na árvore real (acionamento 8), bloco aplicado e regenerado, revertidos por cópia: `yaml.safe_load` exit `1` → `0`; drift `0` → `1` (trocada, não regenerada) → `0`; `check-readme.ps1` `0`/`0`; `backlog.py check` e `modelo.py check` `0`/`0`; `277 passed` nos dois mundos; os outros nove frontmatters parseiam antes e depois. Saturação: primeiro achado no frontmatter do agente e na região gerada; capacidade × término: uma linha. Sem drift: `OP-8` e o estado final de `consultor.descrição pública da figura` são idênticos em `## 1` e `## 1A` e dizem *a `description` do agente e a região gerada, regenerada no mesmo ato, descrevem o papel de doutrina...* — é exatamente o que o corretivo termina. |
| `DCS-34` | Versão 2 pendente da `## 1A` **validada pelo consultor** no marco de fechamento (acionamento 9, gatilho 4): as três diferenças do drift (`OP-3`, `OP-5`, estado final de `consultor.alcance da triagem das paradas`) e as que o `--drift` não lista (partição da `F-4` a 50 itens, dois estados iniciais, lastro `DC-3`) conferem com a árvore entregue; `modelo.py check` exit 0, 17 tarefas `done`. Sobe ao dono para promover ou recusar; nada a re-copiar nos cards, porque não há card aberto. | `GOVERNANCA.md` §3.2: no marco, a validação da versão pendente se busca primeiro no consultor e, validando ele, no dono. Evidência por diferença em `AE-21`. Não estratégico: a versão 2 descreve o que o plano entregou sem mudar objeto, escopo ou objetivo. |
| `DCS-35` | Ato do dono de 2026-09-23, verbatim: *"Com relação à operação 3, foi considerado a hipótese que o consultor tem prerrogativa de recusar impedimento autonomamente? Emendar o modelo e ajustar agora"*. A recusa passa a ser desfecho nomeado da `rota=resolve`: **impedimento improcedente** — o executor parou sem razão e o card é executável como está. Três amarras: (1) o consultor declara a improcedência com a razão, registrada na coluna `motivo` da estatística; (2) o card volta a `ready` com ao menos uma linha nova — a contingência ou o fato que responde à dúvida do executor —, e recusar sem tocar o card não é permitido; (3) o redespacho não consome a retentativa. Alcance: as três paradas de executor (`A3a`, `A3b`, `A3c`), a triagem do passo 8 e a lista *Segue com registro*; `A6a`, `A7` e `B1` não mudam — a `A6a` já refaz sem gastar retentativa, `A7` e `B1` partem de laudo, e julgar entrega é do revisor, não do consultor. Dois corretivos, um por operação, depois da `CON-T8a`: `CON-T2b` (`OP-2`, item 24 — o agente) → `CON-T3d` (`OP-3`, itens 2, 6 e 11 — a skill). Emenda à versão 2 pendente, reescrita no lugar e sem versão 3: a `OP-3` e o estado final de `consultor.alcance da triagem das paradas` passam a nomear a recusa com as três amarras; a validação de `DCS-34` cobre a versão 2 como era e se refaz no marco sobre a versão emendada. Não estratégico: nada de escopo ou objetivo muda, e o ato é do próprio dono. | `AE-22`; ato do dono (gatilho 4). Vão medido pelo condutor: nem o item 2 do agente (`:25`) nem `A3a`/`A3b`/`A3c` (`:224-226`) nomeiam a parada sem razão; redespachar o mesmo card sem mudança a um executor frio reproduz a parada (laço); a spec mediu todas as paradas anteriores como conduta correta, sem caso improcedente. Dois cards e não um: um card materializa uma operação (`G-PLANREADY`, `DCS-31`) e o item 24 é da partição da `OP-2`. Rota `modelador`: a resolução altera a `OP-3` e um estado final — drift, dossiê de emenda na linha de retorno. Medido na árvore real (acionamento 10), blocos aplicados e revertidos por hash, nos dois mundos (só o agente; agente e skill): `improcedente` na skill `0` → `5` (linhas 154, 224, 225, 226, 260) e no agente `0` → `1`; `yaml.safe_load` do frontmatter `0`/`0`; `backlog.py check`, `modelo.py check` e `check-drift` `0`/`0`; `277 passed` em todos. |

## 4. Invariantes de execução

Todos os cards os repetem na parte que os vincula.

- **I-1.** Regra de dependência: `infracore ← contracts ← services ← plugins`, nunca no inverso. Este
  plano edita doutrina e skills, e nenhum card toca código de produto.
- **I-2.** Nenhum agente aciona outro. Todo despacho descrito na norma é ato do loop
  (`scrum-master`).
- **I-3.** O consultor nunca escreve a `## 1` de plano nenhum. Quem escreve no modelo é o
  `pantonic-model-designer`.
- **I-4.** `.claude/README.md:16` só muda por
  `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate`.
- **I-5.** Card que edita `GOVERNANCA.md`, `.claude/global/CLAUDE.md`, `pantonic-planner.md`, a skill
  `diario-de-obras` ou `README.md` roda `python -m pytest -q tests/test_doutrina_unidade.py`, que
  prende literais desses arquivos (`F-5`).
- **I-6.** Piso de regressão é relação, nunca constante: o total de `python -m pytest -q` medido no
  despacho não diminui.
- **I-7.** `README.md:800` fica igual (`DCS-15`) e `pwsh .claude/checks/check-readme.ps1` sai 0.
- **I-8.** Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 (`DCS-12`). Não corrigir as três
  contagens defasadas da spec (`DCS-2`).
- **I-9.** Lastro: o card `CON-T<n>` materializa `OP-<n>`. Card corretivo `CON-T<n>a` materializa a
  mesma operação, e o id entra na lista `tarefas:` dela.

## 5. Tarefas

### CON-T1 — O consultor entra na doutrina de GOVERNANCA [Sonnet · esforço medium · classe mecanica]
- **Status:** `done` · 2026-09-23
- **Objetivo:** O redator da norma faz do consultor um papel de doutrina: dá a ele a linha própria na matriz de responsabilidades, tira das linhas de quem planeja, de quem orquestra e de quem executa a ideia de que toda parada sobe ao planejamento, e põe na triagem dele a escada de revisão, a reprovação depois da última tentativa e as regras de escalonamento e de não perguntar; escreve ainda o dever dele de validar no marco e de emitir a emenda, e a lista de tarefas de cada operação que ele passa a poder estender com o card corretivo.
- **Fundamento:** `DCS-2`, `DCS-3`, `DCS-4`, `DCS-5`, `DCS-18`, `DCS-24`; fatos `F-3`, `F-4` itens 13 a 23, `F-15`; ato 7 da §0 (`DC-1`..`DC-4`).
- **Operação do modelo:** `OP-1`
  - OP-1: O redator da norma faz do consultor um papel de doutrina: dá a ele a linha própria na matriz de responsabilidades, tira das linhas de quem planeja, de quem orquestra e de quem executa a ideia de que toda parada sobe ao planejamento, e põe na triagem dele a escada de revisão, a reprovação depois da última tentativa e as regras de escalonamento e de não perguntar; escreve ainda o dever dele de validar no marco e de emitir a emenda, e a lista de tarefas de cada operação que ele passa a poder estender com o card corretivo.
  - precisa de: parada de executor — nenhuma operação altera uma parada. O que se observa nela, antes e depois, é o caminho: quem a recebe, quem decide a rota e onde isso fica registrado. As paradas do `P-0745` e do `P-0746` (`F-8`) são o retrato do antes; o depois são as paradas da janela de execução deste plano, lidas no arquivo de estatística de `DCS-8` a partir do aceite da `OP-2`; planejador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 13, 19, 20 e 25 — é a fronteira do consultor e nada além: a rodada de replanejamento chega pela rota `planejador` da triagem, só quando emenda aceita cria ou remove operação ou quando a premissa cai inteira (`superseded`), e o corretivo `T<n>a` da mesma operação, com o id apensado à lista `tarefas:`, passa a ser também ato do consultor (`DCS-4`). O que `DCS-18` deixa com o planejamento continua com ele. Alterar outra conduta do planejador é colateral e se escala; modelador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 26, 27 e 28 — é a fronteira do consultor e nada além: o consultor é nomeado como quem origina o dossiê de `emenda` e como quem apensa o id do corretivo à lista `tarefas:`; quem despacha continua sendo quem conduz a sessão (`I-2`). Os literais que a guarda executável prende no arquivo dele (`F-15`) ficam. O instrumento do modelo e seus testes não se tocam
- **Camada e fronteira:** documentação normativa — `GOVERNANCA.md` §3 (matriz, escada de revisão, *Quem escreve*, *Lastro*) e §7 itens 17-18; sem código, sem teste novo.
- **Domínio:** **parada de executor** — devolução `blocked` com motivo `premissa`, `dependencia` ou `ferramenta`, ou laudo com pendência substantiva; **triagem** — o consultor avalia o motivo (evidência, não rota) e devolve uma rota ∈ {`resolve`, `modelador`, `planejador`}; **drift** — resolução que altera objeto, operação ou estado final da `## 1`. Invariante: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa continuam indo ao planejamento (`DCS-18`).
- **Arquivos-alvo:**
  - `GOVERNANCA.md`
- **Contratos/classes:** nenhuma assinatura de código. A linha nova da matriz segue o cabeçalho `| Papel | Modelo | Responde por | Não faz |`.
- **Passos:**
  1. Em `GOVERNANCA.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**.
  2. Em `GOVERNANCA.md`, substitua o bloco **Texto atual 2** pelo bloco **Texto novo 2**.
  3. Em `GOVERNANCA.md`, substitua o bloco **Texto atual 3** pelo bloco **Texto novo 3**.
  4. Em `GOVERNANCA.md`, substitua o bloco **Texto atual 4** pelo bloco **Texto novo 4**.
  5. Em `GOVERNANCA.md`, substitua o bloco **Texto atual 5** pelo bloco **Texto novo 5**.
  6. Em `GOVERNANCA.md`, substitua o bloco **Texto atual 6** pelo bloco **Texto novo 6**.
  7. Em `GOVERNANCA.md`, substitua o bloco **Texto atual 7** pelo bloco **Texto novo 7**.
  8. Em `GOVERNANCA.md`, substitua o bloco **Texto atual 8** pelo bloco **Texto novo 8**.
  9. Em `GOVERNANCA.md`, substitua o bloco **Texto atual 9** pelo bloco **Texto novo 9**.
  10. Em `GOVERNANCA.md`, substitua o bloco **Texto atual 10** pelo bloco **Texto novo 10**.
  11. Em `GOVERNANCA.md`, substitua o bloco **Texto atual 11** pelo bloco **Texto novo 11**.
  12. Em `GOVERNANCA.md`, substitua o bloco **Texto atual 12** pelo bloco **Texto novo 12**.
  13. Em `GOVERNANCA.md`, substitua o bloco **Texto atual 13** pelo bloco **Texto novo 13**.
  14. Em `GOVERNANCA.md`, substitua o bloco **Texto atual 14** pelo bloco **Texto novo 14**.
  15. Em `GOVERNANCA.md`, substitua o bloco **Texto atual 15** pelo bloco **Texto novo 15**.
  16. Em `GOVERNANCA.md`, substitua o bloco **Texto atual 16** pelo bloco **Texto novo 16**.
- **Restrições desta tarefa:**
  - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação.
  - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`).
  - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`).
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:**
  - Não editar `GOVERNANCA.md:633` nem os trechos de G-PLANREADY: são os casos de `DCS-18`, que continuam indo ao planejamento.
  - Não alterar `GOVERNANCA.md:400` (o dever de validar no marco já está lá; a linha 18 da `Verificação` confirma que fica).
  - Não reescrever os literais `**Lastro.**`, `**Rascunho antes do Marco 1.**` e `materialização de uma operação do modelo`, que `tests/test_doutrina_unidade.py` prende (`F-15`).
- **Contingências:**
  - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco
  - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido
  - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa`
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`; quando o card toca arquivo preso por literal (`F-15`), também `tests/test_doutrina_unidade.py`.
- **Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-22 numa cópia da árvore com os cards anteriores aplicados em ensaio; o executor mede o **antes** antes da primeira edição.
  1. antes `0` · depois `1`

     ~~~~
     (Select-String -Path 'GOVERNANCA.md' -SimpleMatch -CaseSensitive -Pattern '| **Consultoria** |').Count
     ~~~~

  2. antes `1` · depois `0`

     ~~~~
     (Select-String -Path 'GOVERNANCA.md' -SimpleMatch -CaseSensitive -Pattern 'chega aqui e só aqui').Count
     ~~~~

  3. antes `1` · depois `0`

     ~~~~
     (Select-String -Path 'GOVERNANCA.md' -SimpleMatch -CaseSensitive -Pattern 'sobem ao **planejamento**').Count
     ~~~~

  4. antes `1` · depois `0`

     ~~~~
     (Select-String -Path 'GOVERNANCA.md' -SimpleMatch -CaseSensitive -Pattern 'a escalada é ao planejamento').Count
     ~~~~

  5. antes `1` · depois `0`

     ~~~~
     (Select-String -Path 'GOVERNANCA.md' -SimpleMatch -CaseSensitive -Pattern 'Quem **recebe** é o **planejador**').Count
     ~~~~

  6. antes `0` · depois `1`

     ~~~~
     (Select-String -Path 'GOVERNANCA.md' -SimpleMatch -CaseSensitive -Pattern 'Quem **recebe** é o **consultor**').Count
     ~~~~

  7. antes `1` · depois `0`

     ~~~~
     (Select-String -Path 'GOVERNANCA.md' -SimpleMatch -CaseSensitive -Pattern 'escalado sobe ao dono').Count
     ~~~~

  8. antes `1` · depois `0`

     ~~~~
     (Select-String -Path 'GOVERNANCA.md' -SimpleMatch -CaseSensitive -Pattern 'a matéria vai ao replanejamento').Count
     ~~~~

  9. antes `0` · depois `1`

     ~~~~
     (Select-String -Path 'GOVERNANCA.md' -SimpleMatch -CaseSensitive -Pattern 'vão primeiro ao **consultor** (`pantonic-consultant`)').Count
     ~~~~

  10. antes `1` · depois `0`

     ~~~~
     (Select-String -Path 'GOVERNANCA.md' -SimpleMatch -CaseSensitive -Pattern 'escala ao planejador, não ao dono').Count
     ~~~~

  11. antes `1` · depois `0`

     ~~~~
     (Select-String -Path 'GOVERNANCA.md' -SimpleMatch -CaseSensitive -Pattern 'destino do bloqueio é o planejamento').Count
     ~~~~

  12. antes `0` · depois `1`

     ~~~~
     (Select-String -Path 'GOVERNANCA.md' -SimpleMatch -CaseSensitive -Pattern 'destino do bloqueio é a triagem do consultor').Count
     ~~~~

  13. antes `1` · depois `0`

     ~~~~
     (Select-String -Path 'GOVERNANCA.md' -SimpleMatch -CaseSensitive -Pattern '`B1` roteia ao planejador').Count
     ~~~~

  14. antes `0` · depois `1`

     ~~~~
     (Select-String -Path 'GOVERNANCA.md' -SimpleMatch -CaseSensitive -Pattern 'na rota `planejador` da triagem').Count
     ~~~~

  15. antes `0` · depois `1`

     ~~~~
     (Select-String -Path 'GOVERNANCA.md' -SimpleMatch -CaseSensitive -Pattern 'e do consultor, que a estende com o card corretivo').Count
     ~~~~

  16. antes `0` · depois `1`

     ~~~~
     (Select-String -Path 'GOVERNANCA.md' -SimpleMatch -CaseSensitive -Pattern 'apensa à lista `tarefas:` da operação o id do card corretivo').Count
     ~~~~

  17. antes `0` · depois `1`

     ~~~~
     (Select-String -Path 'GOVERNANCA.md' -SimpleMatch -CaseSensitive -Pattern 'o loop despacha o modelador sem parar a janela').Count
     ~~~~

  18. antes `1` · depois `1`

     ~~~~
     (Select-String -Path 'GOVERNANCA.md' -SimpleMatch -CaseSensitive -Pattern 'primeiro o consultor; validando ele, o dono').Count
     ~~~~

  19. `8 passed` antes · `8 passed` depois

     ~~~~
     python -m pytest -q tests/test_doutrina_unidade.py
     ~~~~

  20. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes e `277 passed` depois, no ensaio)

     ~~~~
     python -m pytest -q
     ~~~~

- **Pronto quando:**
  - `consultor.estatuto na doutrina` — papel de doutrina em duas residências — a linha na matriz de `GOVERNANCA.md` §3 e a definição de conduta sem estatuto provisório —; a spec permanece como lastro medido e não normativo, com o estatuto apontando para as duas e o índice de documentos dizendo o mesmo — Verificação 1
  - `consultor.alcance da triagem das paradas` — toda parada de executor — `premissa`, `dependencia` ou `ferramenta` — e todo laudo com pendência substantiva chegam ao consultor, que devolve uma rota entre resolver, modelador e planejador, e o loop a despacha; o motivo é evidência, não rota; nenhum dos 47 itens de `F-4` manda a parada direto ao planejador, e as duas fontes normativas da skill do loop citam as decisões deste plano; o que `DCS-18` deixa fora continua indo ao planejamento — Verificação 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
  - `consultor.fronteira com o planejador` — escrita nos três lados — norma, agente do consultor, agente do planejador —: o consultor fecha o técnico e o tático (reescreve card, reordena fila, repara instrumento, toma decisão nova com id, autora o corretivo da mesma operação e apensa o id à lista `tarefas:` dela); vai ao planejador só quando emenda aceita cria ou remove operação ou quando a premissa cai inteira; nunca reabre o objetivo do plano — Verificação 14, 15
  - `consultor.fronteira com o modelador` — havendo drift — resolução que altera objeto, operação ou estado final da `## 1` —, o consultor devolve o dossiê `Ato de modelo` de `emenda` com o reparo e marca a rota `modelador`; o loop despacha o modelador sem parar a janela e a versão pendente coexiste com a vigente até o marco, onde o pedido de validar ou recusar o drift sobe ao dono; recusado, o consultor resolve preservando o modelo; o agente do consultor carrega os dois deveres e o do modelador o nomeia como origem da emenda — Verificação 16, 17, 18
- **Fora do escopo desta tarefa:** as definições de conduta dos agentes (`CON-T2`, `CON-T5`), a skill do loop (`CON-T3`, `CON-T4`) e o `README.md` (`CON-T8`).

**Texto atual 1** — `GOVERNANCA.md`:

~~~~
**a revisão de plano, com exclusividade** — indício de que o plano precisa mudar chega aqui e só aqui, e o planejador decide por si o que for **técnico ou tático**, escalando ao dono o que for **estratégico ou alterar escopo**;
~~~~

**Texto novo 1** — `GOVERNANCA.md`:

~~~~
**a revisão de plano na rota `planejador` da triagem** — indício de que o plano precisa mudar chega primeiro ao consultor (linha *Consultoria*) e aqui só quando a triagem devolve a rota `planejador`: emenda aceita do modelo que cria ou remove operação, ou premissa caída por inteiro; o planejador decide por si o que for **técnico ou tático**, escalando ao dono o que for **estratégico ou alterar escopo**;
~~~~

**Texto atual 2** — `GOVERNANCA.md`:

~~~~
A lista `tarefas:` de cada operação é lastro, não modelo, e é ele quem a mantém depois da autoria |
~~~~

**Texto novo 2** — `GOVERNANCA.md`:

~~~~
A lista `tarefas:` de cada operação é lastro, não modelo, e é ele quem a mantém depois da autoria, ao lado do consultor, que apensa o id do card corretivo `T<n>a` da mesma operação |
~~~~

**Texto atual 3** — `GOVERNANCA.md`:

~~~~
não transforma dúvida própria em pergunta ao executor |
~~~~

**Texto novo 3** — `GOVERNANCA.md`:

~~~~
não transforma dúvida própria em pergunta ao executor |
| **Consultoria** | O mais poderoso disponível (Opus) | **A triagem de toda parada de executor** — `blocked` com motivo `premissa`, `dependencia` ou `ferramenta` — e de todo laudo com pendência substantiva: avalia o motivo, que é evidência e não rota, e devolve ao loop **uma** rota entre `resolve`, `modelador` e `planejador` (`pantonic-consultant`). Na rota `resolve` fecha sozinho o técnico e o tático — reescreve card, reordena fila, repara instrumento, toma decisão nova com id, autora o card corretivo `T<n>a` da mesma operação e apensa o id à lista `tarefas:` dela —, sem validação do dono. Na rota `modelador`, quando a resolução altera objeto, operação ou estado final da `## 1`, devolve o dossiê `Ato de modelo` de `emenda` junto com o reparo, e o loop despacha o modelador sem parar a janela: a versão pendente coexiste com a vigente até o marco, onde o pedido de validar ou recusar o drift sobe ao dono (§3.2). Na rota `planejador`, quando emenda aceita cria ou remove operação ou a premissa caiu por inteiro. No marco, valida a versão pendente do modelo antes do dono (§3.2). Apensa uma linha por acionamento a `docs/ACIONAMENTOS_CONSULTOR.tsv` | Não reabre o objetivo do plano, não escreve a `## 1` de plano nenhum, não implementa a entrega do card, não julga entrega, não commita e não fala com o dono — ao dono sobe só, no marco, o pedido de validar o drift do modelo; não é acionado por outro agente — recebe despacho de quem conduz a sessão |
~~~~

**Texto atual 4** — `GOVERNANCA.md`:

~~~~
(aprovado segue, reprovado volta ao mesmo escopo, escalado sobe ao dono)
~~~~

**Texto novo 4** — `GOVERNANCA.md`:

~~~~
(aprovado segue, reprovado volta ao mesmo escopo, escalado vai à triagem do consultor)
~~~~

**Texto atual 5** — `GOVERNANCA.md`:

~~~~
obstáculo à rota e dossiê não fechado sobem ao **planejamento** (G-REPLAN e G-NOASK, §7 itens 17 e 18), nunca viram improviso do loop nem pergunta ao dono no meio da janela — ao dono chega, no relatório de encerramento, só o que o planejador classificar como estratégico. **Não revisa plano** — roteia a escalada ao planejamento, não replaneja
~~~~

**Texto novo 5** — `GOVERNANCA.md`:

~~~~
parada de executor e laudo com pendência substantiva vão à **triagem do consultor**, e dossiê não fechado volta ao **planejamento** (G-REPLAN e G-NOASK, §7 itens 17 e 18); o loop despacha a rota que o consultor devolve, e nada disso vira improviso do loop nem pergunta ao dono no meio da janela — ao dono chega só, no marco, o pedido de validar o drift do modelo e, no relatório de encerramento, o que for estratégico. **Não revisa plano** — roteia a parada à triagem, não replaneja
~~~~

**Texto atual 6** — `GOVERNANCA.md`:

~~~~
a escalada é ao planejamento, nunca direta ao dono.
~~~~

**Texto novo 6** — `GOVERNANCA.md`:

~~~~
a parada vai à triagem do consultor, nunca direta ao dono.
~~~~

**Texto atual 7** — `GOVERNANCA.md`:

~~~~

**Escada de revisão de plano.** Quem **suspeita** de que o plano precisa mudar é quem esbarra no
indício — quase sempre a execução, eventualmente a revisão ou a orquestração. Quem suspeita **não
revisa plano**: marca a tarefa como `blocked` com a razão tipada `premissa`, registra o indício
no corpo da tarefa e encerra. Quem **recebe** é o **planejador**, e só ele. Ele decide por si o que for
**técnico** (rota, decomposição, dimensionamento, arquivos-alvo, ordem das tarefas) e o que for
**tático** (fatiar, fundir, adiar ou reordenar tarefas dentro do plano vigente). Sobe ao **dono** o
que for **estratégico** — mudar o objetivo, a prioridade ou a doutrina — ou o que **altere o
escopo** acordado do plano. A orquestração roteia essa escalada; não a resolve. A forma da rodada que o planejador conduz —
entrada, saída e posição na fila — é o `G-REPLAN` (§7 item 17).
~~~~

**Texto novo 7** — `GOVERNANCA.md`:

~~~~
**Escada de revisão de plano.** Quem **suspeita** de que o plano precisa mudar é quem esbarra no indício — quase sempre a execução, eventualmente a revisão ou a orquestração. Quem suspeita **não revisa plano**: marca a tarefa como `blocked` com a razão tipada, registra o indício no corpo da tarefa e encerra. Quem **recebe** é o **consultor**, ponto de triagem de toda parada de executor (linha *Consultoria*). Ele decide por si o que for **técnico** (rota, decomposição, dimensionamento, arquivos-alvo, ordem das tarefas) e o que for **tático** (fatiar, fundir, adiar ou reordenar tarefas dentro do plano vigente), sem validação do dono. Havendo **drift** do modelo, devolve o dossiê de emenda com o reparo, e o pedido de validar ou recusar o drift sobe ao **dono** no marco (§3.2), sem parar a janela. Vai ao **planejador** só quando emenda aceita cria ou remove operação ou quando a premissa cai por inteiro. Sobe ao **dono** também o que for **estratégico** — mudar o objetivo, a prioridade ou a doutrina — ou o que **altere o escopo** acordado do plano. A orquestração roteia a parada à triagem e despacha a rota devolvida; não a resolve. A forma da rodada que o planejador conduz na rota `planejador` — entrada, saída e posição na fila — é o `G-REPLAN` (§7 item 17).
~~~~

**Texto atual 8** — `GOVERNANCA.md`:

~~~~
**mantém a lista `tarefas:` de cada operação** — lastro, não modelo — na decomposição e em toda rodada de replanejamento;
~~~~

**Texto novo 8** — `GOVERNANCA.md`:

~~~~
**mantém a lista `tarefas:` de cada operação** — lastro, não modelo — na decomposição e em toda rodada de replanejamento, ao lado do consultor, que a estende com o card corretivo `T<n>a` que autora;
~~~~

**Texto atual 9** — `GOVERNANCA.md`:

~~~~
| consultor | devolve o dossiê `Ato de modelo` de emenda junto com o reparo do escalonamento, quando a decisão muda o que o plano entrega |
~~~~

**Texto novo 9** — `GOVERNANCA.md`:

~~~~
| consultor | devolve o dossiê `Ato de modelo` de emenda junto com o reparo do escalonamento, quando a decisão muda o que o plano entrega; apensa à lista `tarefas:` da operação o id do card corretivo `T<n>a` que autora; no marco, valida a versão pendente antes do dono; não escreve outra linha da seção |
~~~~

**Texto atual 10** — `GOVERNANCA.md`:

~~~~
decomposição e a estende em rodada de replanejamento com o card corretivo. As violações `V1`
~~~~

**Texto novo 10** — `GOVERNANCA.md`:

~~~~
decomposição e a estende em rodada de replanejamento, e do consultor, que a estende com o card corretivo `T<n>a` que autora na rota `resolve`. As violações `V1`
~~~~

**Texto atual 11** — `GOVERNANCA.md`:

~~~~
é executável como está — e a matéria vai ao replanejamento (G-REPLAN, §7 item 17).
~~~~

**Texto novo 11** — `GOVERNANCA.md`:

~~~~
é executável como está — e a matéria vai à triagem do consultor (G-REPLAN, §7 item 17).
~~~~

**Texto atual 12** — `GOVERNANCA.md`:

~~~~
17. **G-REPLAN — bloqueio por premissa é gatilho de revisão do plano, não pendência do dono**
~~~~

**Texto novo 12** — `GOVERNANCA.md`:

~~~~
17. **G-REPLAN — parada de executor é gatilho de triagem, e de revisão do plano só na rota `planejador`; nunca pendência do dono**
~~~~

**Texto atual 13** — `GOVERNANCA.md`:

~~~~
   (dever do **planejador**; roteamento da **orquestração**). Tarefa devolvida `blocked` com razão
~~~~

**Texto novo 13** — `GOVERNANCA.md`:

~~~~
   (triagem do **consultor**; dever do **planejador** na rota `planejador`; roteamento da **orquestração**). Toda parada de executor — `blocked` com motivo `premissa`, `dependencia` ou `ferramenta` — e todo laudo com pendência substantiva vão primeiro ao **consultor** (`pantonic-consultant`), que devolve uma rota entre `resolve`, `modelador` e `planejador`; o motivo é evidência, não rota. Na rota `resolve` o consultor fecha a parada sozinho, com as saídas (a) a (d) abaixo, e o card corretivo `T<n>a` é ato dele. O que segue é a rota `planejador`, devolvida só quando emenda aceita do modelo cria ou remove operação ou quando a premissa caiu por inteiro: tarefa devolvida `blocked` com razão
~~~~

**Texto atual 14** — `GOVERNANCA.md`:

~~~~
`A3b` da skill `scrum-master` (escala ao planejador, não ao dono)
~~~~

**Texto novo 14** — `GOVERNANCA.md`:

~~~~
`A3b` da skill `scrum-master` (escala ao consultor, que devolve a rota; nunca ao dono)
~~~~

**Texto atual 15** — `GOVERNANCA.md`:

~~~~
destino do bloqueio é o planejamento** (G-REPLAN): a rodada decide o que é técnico ou tático e
~~~~

**Texto novo 15** — `GOVERNANCA.md`:

~~~~
destino do bloqueio é a triagem do consultor** (G-REPLAN): ele decide o que é técnico ou tático sem validação do dono, e ao dono sobe só, no marco, o pedido de validar o drift do modelo; na rota `planejador`, a rodada decide o que é técnico ou tático e
~~~~

**Texto atual 16** — `GOVERNANCA.md`:

~~~~
`B1` roteia ao planejador);
~~~~

**Texto novo 16** — `GOVERNANCA.md`:

~~~~
`B1` roteia ao consultor);
~~~~

### CON-T2 — A definição de conduta do consultor sem estatuto provisório [Sonnet · esforço medium · classe mecanica]
- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T1`
- **Objetivo:** O autor de papéis reescreve a definição de conduta do consultor sobre a norma nova: tira dela o estatuto provisório, faz qualquer das três razões de parada acioná-lo, dá a ele a rota que devolve, os deveres de validar a emenda do modelo no marco e de emiti-la quando a resolução muda o que o plano entrega, a linha de estatística que ele apensa a cada acionamento e a saída curta por edição mínima.
- **Fundamento:** `DCS-2`, `DCS-3`, `DCS-4`, `DCS-5`, `DCS-8`, `DCS-9`, `DCS-10`, `DCS-20`, `DCS-21`, `DCS-24`; fatos `F-2`, `F-4` item 24, `F-14`, `F-16`.
- **Operação do modelo:** `OP-2`
  - OP-2: O autor de papéis reescreve a definição de conduta do consultor sobre a norma nova: tira dela o estatuto provisório, faz qualquer das três razões de parada acioná-lo, dá a ele a rota que devolve, os deveres de validar a emenda do modelo no marco e de emiti-la quando a resolução muda o que o plano entrega, a linha de estatística que ele apensa a cada acionamento e a saída curta por edição mínima.
  - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`); parada de executor — nenhuma operação altera uma parada. O que se observa nela, antes e depois, é o caminho: quem a recebe, quem decide a rota e onde isso fica registrado. As paradas do `P-0745` e do `P-0746` (`F-8`) são o retrato do antes; o depois são as paradas da janela de execução deste plano, lidas no arquivo de estatística de `DCS-8` a partir do aceite da `OP-2`; planejador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 13, 19, 20 e 25 — é a fronteira do consultor e nada além: a rodada de replanejamento chega pela rota `planejador` da triagem, só quando emenda aceita cria ou remove operação ou quando a premissa cai inteira (`superseded`), e o corretivo `T<n>a` da mesma operação, com o id apensado à lista `tarefas:`, passa a ser também ato do consultor (`DCS-4`). O que `DCS-18` deixa com o planejamento continua com ele. Alterar outra conduta do planejador é colateral e se escala; modelador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 26, 27 e 28 — é a fronteira do consultor e nada além: o consultor é nomeado como quem origina o dossiê de `emenda` e como quem apensa o id do corretivo à lista `tarefas:`; quem despacha continua sendo quem conduz a sessão (`I-2`). Os literais que a guarda executável prende no arquivo dele (`F-15`) ficam. O instrumento do modelo e seus testes não se tocam
- **Camada e fronteira:** definição de agente — `.claude/agents/pantonic-consultant.md` (corpo, item 24 de `F-4`) e um arquivo de dados novo em `docs/`.
- **Domínio:** **rota** — a primeira linha do retorno do consultor, `rota=<resolve|modelador|planejador>` (`DCS-21`); **linha de estatística** — uma linha por acionamento em `docs/ACIONAMENTOS_CONSULTOR.tsv` (`DCS-8`).
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-consultant.md`
  - `docs/ACIONAMENTOS_CONSULTOR.tsv` (novo)
- **Contratos/classes:** arquivo novo `docs/ACIONAMENTOS_CONSULTOR.tsv`: UTF-8, separador tabulação, fim de linha `\n`, só a linha de cabeçalho `data`, `plano`, `acionamento`, `tarefa`, `gatilho`, `motivo`, `classe_impedimento`, `rota`, `inconclusivo`.
- **Passos:**
  1. Em `.claude/agents/pantonic-consultant.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**.
  2. Em `.claude/agents/pantonic-consultant.md`, substitua o bloco **Texto atual 2** pelo bloco **Texto novo 2**.
  3. Em `.claude/agents/pantonic-consultant.md`, substitua o bloco **Texto atual 3** pelo bloco **Texto novo 3**.
  4. Em `.claude/agents/pantonic-consultant.md`, substitua o bloco **Texto atual 4** pelo bloco **Texto novo 4**.
  5. Em `.claude/agents/pantonic-consultant.md`, substitua o bloco **Texto atual 5** pelo bloco **Texto novo 5**.
  6. Crie `docs/ACIONAMENTOS_CONSULTOR.tsv` com o conteúdo exato do bloco **Arquivo novo** (UTF-8, fim de linha LF).
- **Restrições desta tarefa:**
  - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação.
  - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`).
  - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`).
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:**
  - Não tocar a linha `description:` (`:3`): é o item 47, da `CON-T8`; trocá-la agora deixa o check-drift vermelho até a `CON-T8` (`F-16`). As linhas 9 e 14 da `Verificação` medem isso.
  - Não tocar `:8-12`, `:31-34` nem `:62-67`: são as linhas de forma (item 44), da `CON-T4`. A linha 10 da `Verificação` mede isso.
  - Não escrever linha de dado no `.tsv`: só o cabeçalho.
- **Contingências:**
  - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco
  - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido
  - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa`
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`; quando o card toca arquivo preso por literal (`F-15`), também `tests/test_doutrina_unidade.py`.
- **Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-22 numa cópia da árvore com os cards anteriores aplicados em ensaio; o executor mede o **antes** antes da primeira edição.
  1. antes `1` · depois `0`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'ad-hoc e provisória').Count
     ~~~~

  2. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'rota=<resolve|modelador|planejador>').Count
     ~~~~

  3. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'motivo `premissa`, `dependencia` ou `ferramenta`').Count
     ~~~~

  4. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'apense o id novo à lista `tarefas:`').Count
     ~~~~

  5. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'você valida a versão pendente do modelo antes do dono').Count
     ~~~~

  6. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'docs/ACIONAMENTOS_CONSULTOR.tsv').Count
     ~~~~

  7. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'nunca reescreva seção inteira com `Write`').Count
     ~~~~

  8. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'Não reabre o objetivo do plano').Count
     ~~~~

  9. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'Figura ad-hoc, provisória, criada por decisão do dono em 2026-09-18.').Count
     ~~~~

  10. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'você **não é efêmero**').Count
     ~~~~

  11. antes `False` · depois `True`

     ~~~~
     Test-Path docs/ACIONAMENTOS_CONSULTOR.tsv
     ~~~~

  12. antes `False` · depois `True`

     ~~~~
     (Get-Content docs/ACIONAMENTOS_CONSULTOR.tsv -TotalCount 1) -ceq "data`tplano`tacionamento`ttarefa`tgatilho`tmotivo`tclasse_impedimento`trota`tinconclusivo"
     ~~~~

  13. antes `1` · depois `1`

     ~~~~
     git check-ignore -q docs/ACIONAMENTOS_CONSULTOR.tsv; $LASTEXITCODE
     ~~~~

  14. antes `0` · depois `0`

     ~~~~
     pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift; $LASTEXITCODE
     ~~~~

  15. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes e `277 passed` depois, no ensaio)

     ~~~~
     python -m pytest -q
     ~~~~

- **Pronto quando:**
  - `consultor.estatuto na doutrina` — papel de doutrina em duas residências — a linha na matriz de `GOVERNANCA.md` §3 e a definição de conduta sem estatuto provisório —; a spec permanece como lastro medido e não normativo, com o estatuto apontando para as duas e o índice de documentos dizendo o mesmo — Verificação 1
  - `consultor.alcance da triagem das paradas` — toda parada de executor — `premissa`, `dependencia` ou `ferramenta` — e todo laudo com pendência substantiva chegam ao consultor, que devolve uma rota entre resolver, modelador e planejador, e o loop a despacha; o motivo é evidência, não rota; nenhum dos 47 itens de `F-4` manda a parada direto ao planejador, e as duas fontes normativas da skill do loop citam as decisões deste plano; o que `DCS-18` deixa fora continua indo ao planejamento — Verificação 2, 3
  - `consultor.fronteira com o planejador` — escrita nos três lados — norma, agente do consultor, agente do planejador —: o consultor fecha o técnico e o tático (reescreve card, reordena fila, repara instrumento, toma decisão nova com id, autora o corretivo da mesma operação e apensa o id à lista `tarefas:` dela); vai ao planejador só quando emenda aceita cria ou remove operação ou quando a premissa cai inteira; nunca reabre o objetivo do plano — Verificação 4, 8
  - `consultor.fronteira com o modelador` — havendo drift — resolução que altera objeto, operação ou estado final da `## 1` —, o consultor devolve o dossiê `Ato de modelo` de `emenda` com o reparo e marca a rota `modelador`; o loop despacha o modelador sem parar a janela e a versão pendente coexiste com a vigente até o marco, onde o pedido de validar ou recusar o drift sobe ao dono; recusado, o consultor resolve preservando o modelo; o agente do consultor carrega os dois deveres e o do modelador o nomeia como origem da emenda — Verificação 2, 5
  - `consultor.registro dos acionamentos` — residência estruturada, uma linha por acionamento apensada pelo consultor — o que o motivou, a classe do impedimento, a rota e o que ficou inconclusivo —, com o consumidor declarado no acumulador da spec de robustez; a prosa histórica não se migra — Verificação 6, 11, 12, 13
  - `consultor.lacunas deixadas pela especificação` — as sete fechadas: cinco por norma — handover e forma pelo cenário persistido, estatística pela residência estruturada, autoria de card novo pela fronteira com o planejador, disciplina de saída por regra do agente — e duas por residência nomeada — não-acionamento no `TK-55`, poluição pela regra geral do agente —; cada item da §10 da spec aponta para o que o fecha — Verificação 4, 7
- **Fora do escopo desta tarefa:** as linhas de forma do agente (`CON-T4`) e a `description` (`CON-T8`).

**Texto atual 1** — `.claude/agents/pantonic-consultant.md`:

~~~~
**Estatuto:** figura **ad-hoc e provisória**, criada por decisão do dono em 2026-09-18 para as
próximas tarefas do `P-0740`. O dono declarou que vai detalhar esta figura, e as suas fronteiras
com o `pantonic-planner`, em plano próprio. Até lá, este arquivo descreve o mínimo operacional —
ele **não** é doutrina publicada, não está em `GOVERNANCA.md` §3 e não se cita como fonte
normativa.
~~~~

**Texto novo 1** — `.claude/agents/pantonic-consultant.md`:

~~~~
**Estatuto:** papel de doutrina. A residência do papel é a linha *Consultoria* da matriz de responsabilidades de `GOVERNANCA.md` §3; este arquivo descreve a conduta. As regras de triagem têm fonte em `docs/plans/P-0747-consultor-de-plano.md`, `DCS-3`..`DCS-6`, e a `docs/consultant-spec.md` é lastro medido, não fonte normativa.
~~~~

**Texto atual 2** — `.claude/agents/pantonic-consultant.md`:

~~~~
2. **Desbloqueia impedimento de executor.** Quando um card volta `blocked` (`dependencia` ou
   `premissa`), ou quando um laudo recomenda `escalar`, o loop manda o caso a você. Você responde
   com **a decisão e o reparo**, não com opções: o executor não decide e o loop não improvisa.
~~~~

**Texto novo 2** — `.claude/agents/pantonic-consultant.md`:

~~~~
2. **Tria toda parada de executor.** Quando um card volta `blocked` — motivo `premissa`, `dependencia` ou `ferramenta` —, quando um laudo traz pendência substantiva ou quando um instrumento do loop recusa o fechamento, o loop manda o caso a você. O motivo é evidência, não rota. A primeira linha do seu retorno é `rota=<resolve|modelador|planejador>`, seguida da decisão e do reparo — nunca de opções:
   - `rota=resolve` — a questão é operacional, técnica ou tática: você a fecha sozinho, e o dono não valida (ato do dono de 2026-09-22: *"Eu não vou validar a decisão dele para questões técnicas e táticas."*).
   - `rota=modelador` — a resolução altera objeto, operação ou estado final da `## 1`: é drift do modelo, a sua guarda. Devolva o dossiê `Ato de modelo` de `emenda` junto com o reparo do card; o loop despacha o modelador sem parar a janela, a versão pendente coexiste com a vigente até o marco, e é lá que o pedido de validar ou recusar o drift sobe ao dono (`GOVERNANCA.md` §3.2) — recusado, o caso volta a você para resolver preservando o modelo.
   - `rota=planejador` — emenda já aceita cria ou remove operação, ou a premissa do plano caiu por inteiro.
~~~~

**Texto atual 3** — `.claude/agents/pantonic-consultant.md`:

~~~~
Você edita o plano: decisão nova com id, cards reescritos, fila reordenada, achado absorvido com ponteiro.
~~~~

**Texto novo 3** — `.claude/agents/pantonic-consultant.md`:

~~~~
Você edita o plano: decisão nova com id, cards reescritos, fila reordenada, achado absorvido com ponteiro. Card corretivo `T<n>a` da mesma operação do card que corrige é seu: copie o campo `Operação do modelo` do card corrigido e apense o id novo à lista `tarefas:` daquela operação — lastro, não modelo. No marco, você valida a versão pendente do modelo antes do dono (`GOVERNANCA.md` §3.2).
~~~~

**Texto atual 4** — `.claude/agents/pantonic-consultant.md`:

~~~~
4. **Responde curto.** O loop não quer ensaio: quer a decisão, o que mudou no plano e a rota.
~~~~

**Texto novo 4** — `.claude/agents/pantonic-consultant.md`:

~~~~
4. **Responde curto e edita pouco.** O loop não quer ensaio: quer a linha `rota=`, a decisão e o que mudou no plano. Edite o plano com `Edit` mínimo; nunca reescreva seção inteira com `Write`.
5. **Apensa uma linha de estatística por acionamento** a `docs/ACIONAMENTOS_CONSULTOR.tsv`, com os campos separados por tabulação, na ordem `data`, `plano`, `acionamento`, `tarefa`, `gatilho`, `motivo`, `classe_impedimento`, `rota`, `inconclusivo`. `gatilho` é a classe 1-4 da §2 de `docs/consultant-spec.md` (1 card `blocked`; 2 laudo com pendência substantiva; 3 impedimento de instrumento que nenhum card cobre; 4 ato do dono no marco); `acionamento` é o número de ordem no plano; `inconclusivo` é o que a decisão deliberadamente não fechou, ou `-`. O consumidor é o `TK-55`, acumulador da spec de robustez.
~~~~

**Texto atual 5** — `.claude/agents/pantonic-consultant.md`:

~~~~
- **Não fala com o dono.** Escalada ao dono sai pelo relatório de encerramento do `scrum-master`
  (`G-NOASK`, `GOVERNANCA.md` §7 item 18). Você decide o que é técnico e tático — que é quase
  tudo — e marca como estratégico só o que muda escopo ou rota do plano.
~~~~

**Texto novo 5** — `.claude/agents/pantonic-consultant.md`:

~~~~
- **Não fala com o dono.** Ao dono sobe só o que o loop leva: no marco, o pedido de validar o drift da rota `modelador` e, no relatório de encerramento do `scrum-master`, o que você marcar como estratégico — o que muda escopo ou objetivo do plano, ou revoga decisão do dono (`G-NOASK`, `GOVERNANCA.md` §7 item 18). O técnico e o tático você fecha sem validação do dono.
- **Não reabre o objetivo do plano** e não escreve a `## 1. Modelo conceitual` de plano nenhum.
~~~~

**Arquivo novo** — `docs/ACIONAMENTOS_CONSULTOR.tsv` (cada `<TAB>` é um caractere de tabulação; uma linha só, terminada em LF):

~~~~
data<TAB>plano<TAB>acionamento<TAB>tarefa<TAB>gatilho<TAB>motivo<TAB>classe_impedimento<TAB>rota<TAB>inconclusivo
~~~~

### CON-T3 — O loop leva toda parada ao consultor [Sonnet · esforço medium · classe mecanica]
- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T2`
- **Objetivo:** O mantenedor do loop reescreve a condução das paradas: as duas fontes normativas da skill passam a citar as decisões deste plano, toda regra que roteia parada de executor ou laudo com pendência substantiva e o guardrail que manda a matéria ao planejador passam a levá-los ao consultor, o loop despacha a rota que ele devolve e, quando a rota é o modelador, despacha o modelador sem parar a janela e leva o pedido de validar o drift ao dono no marco.
- **Fundamento:** `DCS-3`, `DCS-4`, `DCS-5`, `DCS-11`, `DCS-18`, `DCS-21`, `DCS-24`; fatos `F-4` itens 1, 2 e 4 a 12, `F-6`; ato 7 da §0 (precedência da spec até o bloco A ser reescrito).
- **Operação do modelo:** `OP-3`
  - OP-3: O mantenedor do loop reescreve a condução das paradas: as duas fontes normativas da skill passam a citar as decisões deste plano, toda regra que roteia parada de executor ou laudo com pendência substantiva e o guardrail que manda a matéria ao planejador passam a levá-los ao consultor, o loop despacha a rota que ele devolve e, quando a rota é o modelador, despacha o modelador sem parar a janela e leva o pedido de validar o drift ao dono no marco.
  - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`); parada de executor — nenhuma operação altera uma parada. O que se observa nela, antes e depois, é o caminho: quem a recebe, quem decide a rota e onde isso fica registrado. As paradas do `P-0745` e do `P-0746` (`F-8`) são o retrato do antes; o depois são as paradas da janela de execução deste plano, lidas no arquivo de estatística de `DCS-8` a partir do aceite da `OP-2`; planejador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 13, 19, 20 e 25 — é a fronteira do consultor e nada além: a rodada de replanejamento chega pela rota `planejador` da triagem, só quando emenda aceita cria ou remove operação ou quando a premissa cai inteira (`superseded`), e o corretivo `T<n>a` da mesma operação, com o id apensado à lista `tarefas:`, passa a ser também ato do consultor (`DCS-4`). O que `DCS-18` deixa com o planejamento continua com ele. Alterar outra conduta do planejador é colateral e se escala; modelador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 26, 27 e 28 — é a fronteira do consultor e nada além: o consultor é nomeado como quem origina o dossiê de `emenda` e como quem apensa o id do corretivo à lista `tarefas:`; quem despacha continua sendo quem conduz a sessão (`I-2`). Os literais que a guarda executável prende no arquivo dele (`F-15`) ficam. O instrumento do modelo e seus testes não se tocam
- **Camada e fronteira:** procedimento de orquestração — `.claude/skills/scrum-master/SKILL.md`; sem código.
- **Domínio:** **rota** devolvida pelo consultor, lida pelo passo 8 na linha `rota=<resolve|modelador|planejador>` (`DCS-21`). Invariante: o motivo do executor é evidência, não rota (`DP-G` item 1 do `P-0734`).
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
- **Contratos/classes:** nenhuma assinatura de código; as linhas `A3a`, `A3b` e `A3c` mantêm as três colunas `| # | condição | ação |`.
- **Passos:**
  1. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**.
  2. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 2** pelo bloco **Texto novo 2**.
  3. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 3** pelo bloco **Texto novo 3**.
  4. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 4** pelo bloco **Texto novo 4**.
  5. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 5** pelo bloco **Texto novo 5**.
  6. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 6** pelo bloco **Texto novo 6**.
  7. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 7** pelo bloco **Texto novo 7**.
  8. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 8** pelo bloco **Texto novo 8**.
  9. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 9** pelo bloco **Texto novo 9**.
  10. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 10** pelo bloco **Texto novo 10**.
  11. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 11** pelo bloco **Texto novo 11**.
- **Restrições desta tarefa:**
  - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação.
  - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`).
  - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`).
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:**
  - Não tocar o parêntese `` (`pantonic-consultant`, instanciado uma vez por execução) `` da `B1` nem a nota de `SendMessage` do passo 9: são os itens 45 e 3, da `CON-T4`. As linhas 9 e 10 da `Verificação` medem isso.
  - Não criar passo novo: *"Dez passos, nesta ordem"* fica igual (`DCS-19`).
  - Não tocar a `A8a` nem o passo 9 `:196`: já roteiam ao consultor (`F-4` itens 4 e 9).
- **Contingências:**
  - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco
  - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido
  - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa`
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`; quando o card toca arquivo preso por literal (`F-15`), também `tests/test_doutrina_unidade.py`.
- **Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-22 numa cópia da árvore com os cards anteriores aplicados em ensaio; o executor mede o **antes** antes da primeira edição.
  1. antes `1` · depois `0`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'A escalada é ao **planejador**').Count
     ~~~~

  2. antes `0` · depois `2`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'P-0747-consultor-de-plano.md` `DCS-3`..`DCS-6`').Count
     ~~~~

  3. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'rota=<resolve|modelador|planejador>').Count
     ~~~~

  4. antes `0` · depois `5`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'que devolve a rota (passo 8)').Count
     ~~~~

  5. antes `2` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'a rodada de replanejamento vira a próxima tarefa do plano').Count
     ~~~~

  6. antes `1` · depois `0`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'decide entre refazer com diretivas novas').Count
     ~~~~

  7. antes `1` · depois `0`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'encerra-a só a classificação `estratégico`').Count
     ~~~~

  8. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'revisão vai à triagem do consultor').Count
     ~~~~

  9. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'instanciado uma vez por execução').Count
     ~~~~

  10. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'retomado por `SendMessage`').Count
     ~~~~

  11. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes e `277 passed` depois, no ensaio)

     ~~~~
     python -m pytest -q
     ~~~~

- **Pronto quando:**
  - `consultor.alcance da triagem das paradas` — toda parada de executor — `premissa`, `dependencia` ou `ferramenta` — e todo laudo com pendência substantiva chegam ao consultor, que devolve uma rota entre resolver, modelador e planejador, e o loop a despacha; o motivo é evidência, não rota; nenhum dos 47 itens de `F-4` manda a parada direto ao planejador, e as duas fontes normativas da skill do loop citam as decisões deste plano; o que `DCS-18` deixa fora continua indo ao planejamento — Verificação 1, 2, 4, 6, 7, 8
  - `consultor.fronteira com o planejador` — escrita nos três lados — norma, agente do consultor, agente do planejador —: o consultor fecha o técnico e o tático (reescreve card, reordena fila, repara instrumento, toma decisão nova com id, autora o corretivo da mesma operação e apensa o id à lista `tarefas:` dela); vai ao planejador só quando emenda aceita cria ou remove operação ou quando a premissa cai inteira; nunca reabre o objetivo do plano — Verificação 5, 8
  - `consultor.fronteira com o modelador` — havendo drift — resolução que altera objeto, operação ou estado final da `## 1` —, o consultor devolve o dossiê `Ato de modelo` de `emenda` com o reparo e marca a rota `modelador`; o loop despacha o modelador sem parar a janela e a versão pendente coexiste com a vigente até o marco, onde o pedido de validar ou recusar o drift sobe ao dono; recusado, o consultor resolve preservando o modelo; o agente do consultor carrega os dois deveres e o do modelador o nomeia como origem da emenda — Verificação 3
- **Fora do escopo desta tarefa:** a seção `## Acionamento do consultor` e as linhas de forma (`CON-T4`).

**Texto atual 1** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
`GOVERNANCA.md` §4.3 e `### DP-Q` (encerramento); `### DP-G` item 3 (reordenação da fila).
~~~~

**Texto novo 1** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
`GOVERNANCA.md` §4.3 e `### DP-Q` (encerramento); `### DP-G` item 3 (reordenação da fila); `docs/plans/P-0747-consultor-de-plano.md` `DCS-3`..`DCS-6` (triagem de toda parada pelo consultor e rota devolvida).
~~~~

**Texto atual 2** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
- **Ação:** aplicar a tabela do bloco A **em ordem de precedência** — a primeira regra que casa
  vence.
~~~~

**Texto novo 2** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
- **Ação:** aplicar a tabela do bloco A **em ordem de precedência** — a primeira regra que casa
  vence.
- **Triagem:** toda regra que escala ao consultor (`A3a`, `A3b`, `A3c`, `A6a`, `A7`, `B1` e o gate do modelo do passo 9) recebe de volta a linha `rota=<resolve|modelador|planejador>` e despacha por ela: `rota=resolve` — o reparo já está gravado no plano, e a janela segue; `rota=modelador` — despacha o `pantonic-model-designer` com o dossiê `Ato de modelo` de `emenda` que o consultor devolveu, sem parar a janela: a versão pendente coexiste com a vigente até o marco, onde o pedido de validar ou recusar o drift sobe ao dono (`GOVERNANCA.md` §3.2), e com a recusa o caso volta ao consultor para resolver preservando o modelo; `rota=planejador` — materializa o plano como `blocked`, e a rodada de replanejamento vira a próxima tarefa do plano (`G-REPLAN`, `GOVERNANCA.md` §7 item 17): **PARA**.
~~~~

**Texto atual 3** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
Forma operacional das regras; fonte normativa em `docs/plans/P-0734-execucao-autonoma.md` —
`### DP-A`, `### DP-B` (com `### DP-Q`), `### DP-G` item 4, `### DP-K` §14.4. Divergência entre
esta tabela e essas seções resolve a favor da seção.
~~~~

**Texto novo 3** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
Forma operacional das regras; fonte normativa em `docs/plans/P-0734-execucao-autonoma.md` — `### DP-A`, `### DP-B` (com `### DP-Q`), `### DP-G` item 4, `### DP-K` §14.4 — e, para a triagem de toda parada pelo consultor, em `docs/plans/P-0747-consultor-de-plano.md` `DCS-3`..`DCS-6`, que prevalecem sobre o `P-0734` no que dispõem. Divergência entre esta tabela e essas seções resolve a favor da seção.
~~~~

**Texto atual 4** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
| `A3a` | `status=blocked` com `motivo=dependencia` | reordena a fila para que a bloqueada suceda a que a bloqueia e materializa `blocked` com a razão; **não** despacha o `reviewer`, **não** escreve RDO, **não** consome a retentativa e **não** incrementa o contador de tarefas fechadas: segue para a próxima elegível |
~~~~

**Texto novo 4** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
| `A3a` | `status=blocked` com `motivo=dependencia` | materializa `blocked` com a razão; **não** despacha o `reviewer`, **não** escreve RDO, **não** consome a retentativa e **não** incrementa o contador de tarefas fechadas; escala ao **consultor**, que devolve a rota (passo 8) — na rota `resolve`, a reordenação da fila que ele gravar, com a bloqueada depois da que a bloqueia: segue para a próxima elegível |
~~~~

**Texto atual 5** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
| `A3b` | `status=blocked` com `motivo=premissa` | materializa `blocked` com a razão na tarefa e no plano; **não** despacha o `reviewer` e **não** escreve RDO: **PARA**. A escalada é ao **planejador**: a rodada de replanejamento vira a próxima tarefa do plano (`G-REPLAN`, `GOVERNANCA.md` §7 item 17) e o relatório de janela a nomeia; ao dono só chega o que o planejador classificar como estratégico |
~~~~

**Texto novo 5** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
| `A3b` | `status=blocked` com `motivo=premissa` | materializa `blocked` com a razão na tarefa; **não** despacha o `reviewer` e **não** escreve RDO; escala ao **consultor**, que devolve a rota (passo 8): `resolve` segue com o reparo; `modelador` segue com o despacho do modelador; `planejador` **PARA**, como o passo 8 manda. O motivo é evidência, não rota (`DP-G` item 1 do `P-0734`) |
~~~~

**Texto atual 6** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
| `A3c` | `status=blocked` com `motivo=ferramenta` | materializa `blocked` com a razão, **sem** reclassificar o motivo; lê o **fallback declarado** da superfície no card e, havendo, **redespacha a mesma tarefa** por ele, **sem** consumir retentativa — a tarefa não falhou, a ferramenta foi negada; não havendo fallback declarado, **PARA** e a recusa sobe como matéria de plano, com a ferramenta, o caminho e a linha literal da recusa. **Não** despacha o `reviewer` e **não** escreve RDO |
~~~~

**Texto novo 6** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
| `A3c` | `status=blocked` com `motivo=ferramenta` | materializa `blocked` com a razão, **sem** reclassificar o motivo; escala ao **consultor** com a ferramenta, o caminho e a linha literal da recusa, e ele devolve a rota (passo 8): na rota `resolve`, havendo **fallback declarado** da superfície no card, **redespacha a mesma tarefa** por ele, **sem** consumir retentativa — a tarefa não falhou, a ferramenta foi negada —, e sem fallback aplica o reparo que o consultor gravar; `modelador` segue com o despacho do modelador; `planejador` **PARA**, como o passo 8 manda. **Não** despacha o `reviewer` e **não** escreve RDO |
~~~~

**Texto atual 7** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
escala ao **consultor de plano**, que decide entre refazer com diretivas novas, emendar o card ou mudar a rota; a janela **segue** com o que ele devolver (Diretiva de execução do `P-0740`, item 2).
~~~~

**Texto novo 7** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
escala ao **consultor de plano**, que devolve a rota (passo 8) — na rota `resolve`, refazer com diretivas novas ou emendar o card; a janela **segue** com o que ele devolver (Diretiva de execução do `P-0740`, item 2; `P-0747` `DCS-3`).
~~~~

**Texto atual 8** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
do plano: **PARA**. A escalada é a do `A3b`: a reprovação depois da última retentativa é nomeada no relatório de encerramento e a rodada de replanejamento vira a próxima tarefa do plano (`G-REPLAN`, `GOVERNANCA.md` §7 item 17).
~~~~

**Texto novo 8** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
do plano. A escalada é a do `A3b`: ao **consultor**, que devolve a rota (passo 8), e a reprovação depois da última retentativa é nomeada no relatório de encerramento.
~~~~

**Texto atual 9** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
que devolve decisão e reparo: a janela **segue** com o que ele devolver. **PARA** só se o consultor classificar o impedimento como **estratégico**; ao dono chega só isso
~~~~

**Texto novo 9** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
que devolve a rota (passo 8): na rota `resolve` a janela **segue** com o reparo e na rota `modelador` com o despacho do modelador; **PARA** na rota `planejador`, como o passo 8 manda, e quando o consultor classificar o impedimento como **estratégico**; ao dono chega só isso
~~~~

**Texto atual 10** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
- **Obriga parada:** decisão de arquitetura ou de requisito, que chega pelo `pendencia=`
  do retorno do executor ou pela recomendação `escalar` do laudo (`B1`), roteada ao **consultor de plano** —
  inclusive achado que invalida a rota do plano; executor `blocked` por `motivo=premissa` (`A3b`); o `blocked`
  por `motivo=ferramenta` como recusa de ferramenta sem fallback declarado (`A3c`); reprovação depois da
  última retentativa (`A7`); plano não-pronto (`B3`). Escalonamento ao consultor **não** encerra a janela: encerra-a só a classificação `estratégico` que ele devolver.
- **Segue com registro:** ressalva não bloqueante e achado fora de escopo com rota, pelo laudo
  (`A8`); o `blocked` por `motivo=dependencia` (`A3a`), que reordena a fila e segue para a
  próxima elegível; e o `blocked` por `motivo=ferramenta` como recusa de ferramenta com fallback
  declarado, que redespacha a mesma tarefa sem consumir retentativa (`A3c`).
~~~~

**Texto novo 10** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
- **Obriga parada:** a rota `planejador` que o consultor devolver a qualquer escalonamento (`A3a`, `A3b`, `A3c`, `A6a`, `A7`, `B1` e o gate do modelo do passo 9), e a classificação `estratégico` — inclusive achado que invalida a rota do plano; plano não-pronto (`B3`). Escalonamento ao consultor **não** encerra a janela por si: encerram-na a rota `planejador` e a classificação `estratégico` que ele devolver; a rota `modelador` despacha o modelador e segue, com a versão pendente até o marco.
- **Segue com registro:** ressalva não bloqueante e achado fora de escopo com rota, pelo laudo (`A8`); e toda parada ou pendência em que o consultor devolve `rota=resolve` (`A3a`, `A3b`, `A3c`, `A6a`, `A7`, `B1`), com o reparo que ele gravou — a reordenação da fila no `A3a`, o redespacho pelo fallback declarado no `A3c`; e a rota `modelador`, com o despacho do `pantonic-model-designer` sobre o dossiê devolvido e a versão pendente até o marco (`GOVERNANCA.md` §3.2).
~~~~

**Texto atual 11** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
  revisão leva o **plano** a `blocked`, com a razão registrada, e a matéria ao planejador.
~~~~

**Texto novo 11** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
  revisão vai à triagem do consultor, e só a rota `planejador` leva o **plano** a `blocked`, com a razão registrada, e a matéria ao planejador.
~~~~

### CON-T3a — Corretivo da OP-3: a parada é a mesma em todas as regras que escalam ao consultor [Sonnet · esforço medium · classe mecanica]
- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T3`
- **Objetivo:** Corretivo da `CON-T3` (`AE-4`, `DCS-27`): a skill do loop passa a dizer a mesma coisa sobre o destino da parada em todo lugar que escala ao consultor — a `A6a` deixa de seguir incondicionalmente, a classificação estratégica ganha forma mecânica (`estrategico=<uma frase>`, segunda linha do retorno) e entra na triagem do passo 8, nas regras `A3a`, `A3b`, `A3c`, `A6a`, `A7` e `B1` e nas duas listas de parada, e o gate do modelo do passo 9 entra na lista *Segue com registro*; o card publica a linha de coerência do módulo que faltou.
- **Fundamento:** `DCS-3`, `DCS-4`, `DCS-21`, `DCS-24`, `DCS-27`; achado `AE-4`; laudo da `CON-T3` (RUBRICA 8, critérios iv e xv).
- **Operação do modelo:** `OP-3`
  - OP-3: O mantenedor do loop reescreve a condução das paradas: as duas fontes normativas da skill passam a citar as decisões deste plano, toda regra que roteia parada de executor ou laudo com pendência substantiva e o guardrail que manda a matéria ao planejador passam a levá-los ao consultor, o loop despacha a rota que ele devolve e, quando a rota é o modelador, despacha o modelador sem parar a janela e leva o pedido de validar o drift ao dono no marco.
  - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`); parada de executor — nenhuma operação altera uma parada. O que se observa nela, antes e depois, é o caminho: quem a recebe, quem decide a rota e onde isso fica registrado. As paradas do `P-0745` e do `P-0746` (`F-8`) são o retrato do antes; o depois são as paradas da janela de execução deste plano, lidas no arquivo de estatística de `DCS-8` a partir do aceite da `OP-2`; planejador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 13, 19, 20 e 25 — é a fronteira do consultor e nada além: a rodada de replanejamento chega pela rota `planejador` da triagem, só quando emenda aceita cria ou remove operação ou quando a premissa cai inteira (`superseded`), e o corretivo `T<n>a` da mesma operação, com o id apensado à lista `tarefas:`, passa a ser também ato do consultor (`DCS-4`). O que `DCS-18` deixa com o planejamento continua com ele. Alterar outra conduta do planejador é colateral e se escala; modelador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 26, 27 e 28 — é a fronteira do consultor e nada além: o consultor é nomeado como quem origina o dossiê de `emenda` e como quem apensa o id do corretivo à lista `tarefas:`; quem despacha continua sendo quem conduz a sessão (`I-2`). Os literais que a guarda executável prende no arquivo dele (`F-15`) ficam. O instrumento do modelo e seus testes não se tocam
- **Camada e fronteira:** procedimento de orquestração — `.claude/skills/scrum-master/SKILL.md`, só as linhas que a `CON-T3` já reescreveu (`F-4` itens 2, 6, 7, 8, 10 e 11); sem código.
- **Domínio:** **linha `estrategico=`** — segunda linha do retorno do consultor, presente só quando ele classifica o impedimento como estratégico; com ela o loop **PARA** em qualquer rota e leva a frase ao relatório de encerramento (`DCS-27`). Invariante: sem `estrategico=`, `resolve` e `modelador` seguem e `planejador` para (`DCS-24`).
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
- **Contratos/classes:** nenhuma assinatura de código; as linhas do bloco A e a `B1` mantêm as três colunas `| # | condição | ação |`.
- **Passos:**
  1. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**.
  2. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 2** pelo bloco **Texto novo 2**.
  3. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 3** pelo bloco **Texto novo 3**.
  4. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 4** pelo bloco **Texto novo 4**.
  5. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 5** pelo bloco **Texto novo 5**.
  6. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 6** pelo bloco **Texto novo 6**.
  7. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 7** pelo bloco **Texto novo 7**.
  8. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 8** pelo bloco **Texto novo 8**.
  9. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 9** pelo bloco **Texto novo 9**.
  10. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 10** pelo bloco **Texto novo 10**.
- **Restrições desta tarefa:**
  - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação.
  - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`).
  - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`).
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:**
  - Não tocar o parêntese `` (`pantonic-consultant`, instanciado uma vez por execução) `` da `B1` nem a nota de `SendMessage` do passo 9: são da `CON-T4`. A linha 10 da `Verificação` mede isso.
  - Não criar passo novo nem seção nova (`DCS-19`); a seção `## Acionamento do consultor` é da `CON-T4`.
  - Não tocar `.claude/agents/pantonic-consultant.md`: a forma da linha `estrategico=` no agente é matéria registrada em `AE-5` (residência provisória: o cenário da `CON-T4`).
- **Contingências:**
  - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco
  - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido
  - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa`
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`.
- **Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-23 pelo consultor numa cópia de `.claude/skills/scrum-master/SKILL.md` **como está depois da `CON-T3`**; o executor mede o **antes** antes da primeira edição. As linhas 2 e 3 são a **coerência do módulo**: toda regra que devolve a rota nomeia a parada, e nenhuma menção a `rota=resolve` fica sem a ressalva de `estrategico=`.
  1. antes `0` · depois `9`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'estrategico=').Count
     ~~~~

  2. antes `3` · depois `0`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'que devolve a rota (passo 8)' | Where-Object { $_.Line -cnotmatch 'PARA' }).Count
     ~~~~

  3. antes `2` · depois `0`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'rota=resolve' | Where-Object { $_.Line -cnotmatch 'estrategico=' }).Count
     ~~~~

  4. antes `1` · depois `0`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'o card; a janela **segue** com o que ele devolver').Count
     ~~~~

  5. antes `1` · depois `0`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'classificar o impedimento como **estratégico**').Count
     ~~~~

  6. antes `0` · depois `5`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern '`planejador` e `estrategico=` **PARAM**').Count
     ~~~~

  7. antes `2` · depois `3`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'e o gate do modelo do passo 9').Count
     ~~~~

  8. antes `5` · depois `5`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'que devolve a rota (passo 8)').Count
     ~~~~

  9. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'rota=<resolve|modelador|planejador>').Count
     ~~~~

  10. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'instanciado uma vez por execução').Count
     ~~~~

  11. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes, na árvore com `CON-T1`..`CON-T3` aplicadas)

     ~~~~
     python -m pytest -q
     ~~~~
- **Pronto quando:**
  - `consultor.alcance da triagem das paradas` — fatia da `OP-3` (`F-4` itens 2, 6, 7, 8, 10 e 11): toda regra que escala ao consultor nomeia as mesmas três saídas — `resolve` e `modelador` seguem, `planejador` e `estrategico=` param —, o passo 8 lê a linha `estrategico=` e as duas listas de parada dizem o mesmo, com o gate do modelo do passo 9 nas duas — Verificação 1 a 9
- **Fora do escopo desta tarefa:** a seção `## Acionamento do consultor` e as linhas de forma (`CON-T4`); o agente do consultor (`AE-5`).

**Texto atual 1** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
recebe de volta a linha `rota=<resolve|modelador|planejador>` e despacha por ela: `rota=resolve` — o reparo já está gravado no plano, e a janela segue;
~~~~

**Texto novo 1** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
recebe de volta a linha `rota=<resolve|modelador|planejador>` — e, quando o consultor classificar o impedimento como estratégico, a linha `estrategico=<uma frase>` logo abaixo dela — e despacha por ela: `estrategico=` presente — **PARA** em qualquer rota, e a frase vai ao relatório de encerramento (`G-NOASK`); `rota=resolve` sem `estrategico=` — o reparo já está gravado no plano, e a janela segue;
~~~~

**Texto atual 2** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
com a bloqueada depois da que a bloqueia: segue para a próxima elegível |
~~~~

**Texto novo 2** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
com a bloqueada depois da que a bloqueia: segue para a próxima elegível; `modelador` segue com o despacho do modelador; `planejador` e `estrategico=` **PARAM**, como o passo 8 manda |
~~~~

**Texto atual 3** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
`modelador` segue com o despacho do modelador; `planejador` **PARA**, como o passo 8 manda. O motivo é evidência
~~~~

**Texto novo 3** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
`modelador` segue com o despacho do modelador; `planejador` e `estrategico=` **PARAM**, como o passo 8 manda. O motivo é evidência
~~~~

**Texto atual 4** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
`modelador` segue com o despacho do modelador; `planejador` **PARA**, como o passo 8 manda. **Não** despacha
~~~~

**Texto novo 4** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
`modelador` segue com o despacho do modelador; `planejador` e `estrategico=` **PARAM**, como o passo 8 manda. **Não** despacha
~~~~

**Texto atual 5** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
na rota `resolve`, refazer com diretivas novas ou emendar o card; a janela **segue** com o que ele devolver (Diretiva de execução do `P-0740`, item 2; `P-0747` `DCS-3`).
~~~~

**Texto novo 5** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
na rota `resolve`, refazer com diretivas novas ou emendar o card, e a janela **segue** com o que ele devolver (Diretiva de execução do `P-0740`, item 2; `P-0747` `DCS-3`); `modelador` segue com o despacho do modelador; `planejador` e `estrategico=` **PARAM**, como o passo 8 manda.
~~~~

**Texto atual 6** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
A escalada é a do `A3b`: ao **consultor**, que devolve a rota (passo 8), e a reprovação
~~~~

**Texto novo 6** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
A escalada é a do `A3b`: ao **consultor**, que devolve a rota (passo 8) — `resolve` segue, `modelador` segue com o despacho do modelador, `planejador` e `estrategico=` **PARAM** —, e a reprovação
~~~~

**Texto atual 7** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
**PARA** na rota `planejador`, como o passo 8 manda, e quando o consultor classificar o impedimento como **estratégico**; ao dono chega só isso
~~~~

**Texto novo 7** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
**PARA** na rota `planejador` e com `estrategico=`, como o passo 8 manda; ao dono chega só isso
~~~~

**Texto atual 8** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
e a classificação `estratégico` — inclusive achado que invalida a rota do plano; plano não-pronto (`B3`). Escalonamento ao consultor **não** encerra a janela por si: encerram-na a rota `planejador` e a classificação `estratégico` que ele devolver;
~~~~

**Texto novo 8** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
e a linha `estrategico=` que ele devolver com qualquer rota — inclusive achado que invalida a rota do plano; plano não-pronto (`B3`). Escalonamento ao consultor **não** encerra a janela por si: encerram-na a rota `planejador` e a linha `estrategico=`;
~~~~

**Texto atual 9** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
e toda parada ou pendência em que o consultor devolve `rota=resolve` (`A3a`, `A3b`, `A3c`, `A6a`, `A7`, `B1`), com o reparo
~~~~

**Texto novo 9** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
e toda parada ou pendência em que o consultor devolve `rota=resolve` sem `estrategico=` (`A3a`, `A3b`, `A3c`, `A6a`, `A7`, `B1` e o gate do modelo do passo 9), com o reparo
~~~~

**Texto atual 10** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
; e a rota `modelador`, com o despacho do `pantonic-model-designer`
~~~~

**Texto novo 10** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
; e a rota `modelador` sem `estrategico=`, com o despacho do `pantonic-model-designer`
~~~~

### CON-T4 — A forma efêmera com cenário persistido [Sonnet · esforço medium · classe mecanica]
- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T3a`
- **Objetivo:** O mantenedor do loop instala a forma efêmera do consultor com o cenário persistido, numa seção própria da skill e não num passo novo: cada acionamento nasce uma instância que lê o cenário do plano e o card em causa, decide, reescreve o cenário com edição mínima e se encerra; o cenário passa a ser o próprio handover, a retomada da instância de prontidão sai da nota de telemetria, o reprovisionamento por limite deixa de existir, e as linhas do corpo do agente e da regra do loop que o descrevem instanciado uma vez por plano passam a descrevê-lo efêmero.
- **Fundamento:** `DCS-6`, `DCS-7`, `DCS-19`, `DCS-20`, `DCS-21`, `DCS-26`; fatos `F-4` itens 3, 44 e 45, `F-6`, `F-12`, `F-14`; spec §11 (i).
- **Operação do modelo:** `OP-4`
  - OP-4: O mantenedor do loop instala a forma efêmera do consultor com o cenário persistido, numa seção própria da skill e não num passo novo: cada acionamento nasce uma instância que lê o cenário do plano e o card em causa, decide, reescreve o cenário com edição mínima e se encerra; o cenário passa a ser o próprio handover, a retomada da instância de prontidão sai da nota de telemetria, o reprovisionamento por limite deixa de existir, e as linhas do corpo do agente e da regra do loop que o descrevem instanciado uma vez por plano passam a descrevê-lo efêmero.
  - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`); acionamento do consultor — nenhuma operação altera um acionamento. O que se observa nele é o custo, apurado pelo método de `F-7`; a sonda é descartável e não vira artefato. Retrato do antes: as instâncias 1-4 da forma standby (`F-7`) e a série de `F-8`; o depois: os acionamentos da janela de execução deste plano a partir do aceite da `OP-4`
- **Camada e fronteira:** procedimento de orquestração e definição de agente — `.claude/skills/scrum-master/SKILL.md`, `.claude/agents/pantonic-consultant.md` (linhas de forma) e um arquivo novo em `docs/plans/`.
- **Domínio:** **cenário** — `docs/plans/_CENARIO-<plano>.md`, teto de 15k tokens, decisões vivas, fila, achados abertos e matéria inconclusiva, com autoridade sobre o plano para o que cobre; é o handover.
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
  - `.claude/agents/pantonic-consultant.md`
  - `docs/plans/_CENARIO-P-0747.md` (novo)
- **Contratos/classes:** arquivo novo `docs/plans/_CENARIO-P-0747.md`, UTF-8, conteúdo exatamente o do bloco **Arquivo novo** abaixo.
- **Passos:**
  1. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**.
  2. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 2** pelo bloco **Texto novo 2**.
  3. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 3** pelo bloco **Texto novo 3**.
  4. Em `.claude/agents/pantonic-consultant.md`, substitua o bloco **Texto atual 4** pelo bloco **Texto novo 4**.
  5. Em `.claude/agents/pantonic-consultant.md`, substitua o bloco **Texto atual 5** pelo bloco **Texto novo 5**.
  6. Em `.claude/agents/pantonic-consultant.md`, substitua o bloco **Texto atual 6** pelo bloco **Texto novo 6**.
  7. Crie `docs/plans/_CENARIO-P-0747.md` com o conteúdo exato do bloco **Arquivo novo** (UTF-8, fim de linha LF).
- **Restrições desta tarefa:**
  - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação.
  - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`).
  - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`).
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:**
  - Não tocar a linha `description:` (`:3`) do agente: é da `CON-T8` (`F-16`); a linha 12 da `Verificação` mede isso.
  - Não criar `## Passo 11`: a seção nova é `## Acionamento do consultor`, fora do fluxo (`DCS-19`).
- **Contingências:**
  - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco
  - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido
  - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa`
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
  - se `python .claude/tools/backlog.py check` ou `python .claude/tools/modelo.py check --plano docs/plans/P-0747-consultor-de-plano.md` sair diferente de `0` com `docs/plans/_CENARIO-P-0747.md` presente → parar e sinalizar `blocked` razão `premissa`, colando a saída (o arquivo fica na árvore)
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`; quando o card toca arquivo preso por literal (`F-15`), também `tests/test_doutrina_unidade.py`.
- **Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-22 numa cópia da árvore com os cards anteriores aplicados em ensaio; o executor mede o **antes** antes da primeira edição.
  1. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern '## Acionamento do consultor').Count
     ~~~~

  2. antes `1` · depois `0`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'instanciado uma vez por execução').Count
     ~~~~

  3. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'o consultor nunca é retomado').Count
     ~~~~

  4. antes `1` · depois `0`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'quando o subagente é retomado por `SendMessage`').Count
     ~~~~

  5. antes `1` · depois `2`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'rota=<resolve|modelador|planejador>').Count
     ~~~~

  6. antes `1` · depois `0`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'você **não é efêmero**').Count
     ~~~~

  7. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'você é **efêmero**').Count
     ~~~~

  8. antes `1` · depois `0`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'Absorve o cenário na instanciação').Count
     ~~~~

  9. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'Lê o cenário, não o plano.').Count
     ~~~~

  10. antes `1` · depois `0`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'Você atravessa **um plano**').Count
     ~~~~

  11. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'pare e declare a poluição').Count
     ~~~~

  12. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'Figura ad-hoc, provisória, criada por decisão do dono em 2026-09-18.').Count
     ~~~~

  13. antes `False` · depois `True`

     ~~~~
     Test-Path docs/plans/_CENARIO-P-0747.md
     ~~~~

  14. antes `1` · depois `1`

     ~~~~
     git check-ignore -q docs/plans/_CENARIO-P-0747.md; $LASTEXITCODE
     ~~~~

  15. antes `0` · depois `0`

     ~~~~
     python .claude/tools/backlog.py check; $LASTEXITCODE
     ~~~~

  16. antes `0` · depois `0`

     ~~~~
     python .claude/tools/modelo.py check --plano docs/plans/P-0747-consultor-de-plano.md; $LASTEXITCODE
     ~~~~

  17. antes `0` · depois `0`

     ~~~~
     pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift; $LASTEXITCODE
     ~~~~

  18. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes e `277 passed` depois, no ensaio)

     ~~~~
     python -m pytest -q
     ~~~~

- **Pronto quando:**
  - `consultor.forma da figura` — efêmera com cenário persistido, instalada pela seção `## Acionamento do consultor` da skill do loop: o cenário do plano, com teto de 15k tokens, é o handover, e o reprovisionamento por limite deixa de existir; o corpo do agente e a regra do loop deixam de descrevê-lo instanciado uma vez (`F-4` itens 44 e 45); ao fim do plano a forma leva o veredito medido do piloto, gravado na §11 da spec (item 46) — adotada; ou recusada, com achado em `## 9` e rota para plano novo de standby com aquecimento; ou em amostra insuficiente, com linha nova na §11 da spec e o piloto seguindo na próxima execução — Verificação 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14
  - `consultor.lacunas deixadas pela especificação` — as sete fechadas: cinco por norma — handover e forma pelo cenário persistido, estatística pela residência estruturada, autoria de card novo pela fronteira com o planejador, disciplina de saída por regra do agente — e duas por residência nomeada — não-acionamento no `TK-55`, poluição pela regra geral do agente —; cada item da §10 da spec aponta para o que o fecha — Verificação 1, 11, 15, 16
- **Fora do escopo desta tarefa:** a entrada do cenário no índice de documentos (`CON-T6`) e a medida do piloto (`CON-T7`).

**Texto atual 1** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
E o hook **não
  dispara** quando o subagente é retomado por `SendMessage` — nesse caso a linha é apensada pelo
  loop, como todas as outras.
~~~~

**Texto novo 1** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
E o hook **não
  dispara** quando um subagente é retomado por `SendMessage` — a retomada do executor pela `A1` — e nesse caso a linha é apensada pelo
  loop, como todas as outras; o consultor nunca é retomado (seção *Acionamento do consultor*).
~~~~

**Texto atual 2** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
(`pantonic-consultant`, instanciado uma vez por execução)
~~~~

**Texto novo 2** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
(`pantonic-consultant`, uma instância efêmera por acionamento — seção *Acionamento do consultor*)
~~~~

**Texto atual 3** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
## Relatório de encerramento
~~~~

**Texto novo 3** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
## Acionamento do consultor

Forma **efêmera com cenário persistido**, em piloto (`docs/plans/P-0747-consultor-de-plano.md` `DCS-6`, `DCS-7`). O consultor não fica de prontidão: a cada escalonamento das regras `A3a`, `A3b`, `A3c`, `A6a`, `A7` e `B1` e do gate do modelo do passo 9, o loop despacha **uma instância nova** do `pantonic-consultant`, com três entradas — o caminho do cenário do plano, `docs/plans/_CENARIO-<plano>.md`; o identificador do card em causa; e a evidência (a linha de retorno do executor, a pendência do laudo ou o stderr do instrumento). A instância lê o cenário e o card, decide, reescreve o cenário com `Edit` mínimo, apensa a linha dela a `docs/ACIONAMENTOS_CONSULTOR.tsv` e devolve `rota=<resolve|modelador|planejador>` — e, só quando classifica o impedimento como estratégico, a linha `estrategico=<uma frase>` logo abaixo (`DCS-27`) —, que o loop roteia pelo passo 8. Nenhuma instância é retomada por `SendMessage` e nenhuma é reprovisionada por limite: o cenário **é** o handover. Sem o arquivo de cenário na árvore, o primeiro acionamento do plano o cria, com as decisões vivas, a fila, os achados abertos e a matéria inconclusiva, em no máximo 15k tokens. A linha de telemetria de cada instância vem do bloco `<usage>` da notificação, como a de qualquer subagente, com a tarefa `<ID>-consultor-<n>`.

## Relatório de encerramento
~~~~

**Texto atual 4** — `.claude/agents/pantonic-consultant.md`:

~~~~
Você é o **consultor** de uma execução de plano Pantonic*. Diferente de todos os outros agentes
do kit, você **não é efêmero**: é instanciado uma vez, no começo da execução do plano, e
permanece vivo até a execução terminar. Quem conduz o loop (`scrum-master`) fala com você por
mensagem a cada escalonamento, e o seu contexto — o cenário inteiro do plano — atravessa todos
eles.
~~~~

**Texto novo 4** — `.claude/agents/pantonic-consultant.md`:

~~~~
Você é o **consultor** de uma execução de plano Pantonic*. Como todos os outros agentes do kit, você é **efêmero**: cada acionamento nasce uma instância sua, que lê o cenário do plano em `docs/plans/_CENARIO-<plano>.md` e o card em causa, decide, reescreve o cenário com `Edit` mínimo e se encerra. O cenário, e não o seu contexto, é o que atravessa os acionamentos: ele tem autoridade sobre o plano para o que cobre, e é o seu handover.
~~~~

**Texto atual 5** — `.claude/agents/pantonic-consultant.md`:

~~~~
1. **Absorve o cenário na instanciação.** No primeiro despacho você recebe o plano e lê, de uma
   vez: as decisões, a fila, os achados abertos e os instrumentos que o loop usa. A partir daí,
   **não releia o que já está no seu contexto** — o seu valor é justamente não repagar essa
   leitura.
~~~~

**Texto novo 5** — `.claude/agents/pantonic-consultant.md`:

~~~~
1. **Lê o cenário, não o plano.** A cada acionamento você lê `docs/plans/_CENARIO-<plano>.md` — decisões vivas, fila, achados abertos, matéria inconclusiva, no máximo 15k tokens — e o card em causa; do plano, só o trecho que o cenário aponta. Ao sair, reescreve no cenário o que a sua decisão mudou: o que você não escrever ali, o próximo acionamento não sabe. Cenário acima de 15k tokens: mova a matéria fechada para `## 9` do plano, com ponteiro, e registre isso na coluna `inconclusivo` da sua linha de estatística.
~~~~

**Texto atual 6** — `.claude/agents/pantonic-consultant.md`:

~~~~
## Coesão do seu contexto

Você atravessa **um plano**. Troca de plano é troca de cenário: você é encerrado e outro consultor
nasce para o plano seguinte (`CLAUDE.md` global, Regra 2). Se entrar no seu contexto material de
outro plano, ou um fato que derrube a premissa que você já usou para decidir, **pare e declare a
poluição** ao loop, em vez de seguir remendando.
~~~~

**Texto novo 6** — `.claude/agents/pantonic-consultant.md`:

~~~~
## Coesão do seu contexto

Cada instância sua atravessa **um acionamento** de **um plano**; o cenário de um plano nunca se lê no acionamento de outro (`CLAUDE.md` global, Regra 2). Se entrar no seu contexto material de outro plano, ou um fato que derrube a premissa que você já usou para decidir, **pare e declare a poluição** ao loop, em vez de seguir remendando.
~~~~

**Arquivo novo** — `docs/plans/_CENARIO-P-0747.md`:

~~~~
# Cenário do P-0747 — autoridade sobre o plano para o que cobre

Teto: 15k tokens. Escrito só pelo `pantonic-consultant`, com `Edit` mínimo, a cada acionamento.

## Decisões vivas

- `DCS-1`..`DCS-27` em `docs/plans/P-0747-consultor-de-plano.md` §3; as de acionamento são `DCS-23`..`DCS-27` (2026-09-23).
- Forma do retorno (`DCS-21`, `DCS-27`): primeira linha `rota=<resolve|modelador|planejador>`; segunda linha, só quando o impedimento é estratégico, `estrategico=<uma frase>` — com ela o loop para em qualquer rota.

## Fila

- a do plano, em `docs/plans/P-0747-consultor-de-plano.md` §6.

## Achados abertos

- os marcados `aberto` em `docs/plans/P-0747-consultor-de-plano.md` §9.

## Matéria inconclusiva

- o campo **Inconclusivo** de cada achado de `docs/plans/P-0747-consultor-de-plano.md` §9.
~~~~

### CON-T2a — Corretivo da OP-2: o agente descreve o cenário persistido e lê a linha estrategico= [Sonnet · esforço medium · classe mecanica]
- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T4`
- **Objetivo:** Corretivo da `CON-T2` (`AE-7`, inconclusivo de `AE-5`, `DCS-28`): a definição de conduta do consultor deixa de prescrever a forma de prontidão no fato que a motivou — a `:19` passa a dizer que o cenário fica num arquivo só, persistido, e não *"num contexto só, vivo"* — e o item 2 (*Tria toda parada de executor*) passa a enunciar a segunda linha do retorno, `estrategico=<uma frase>`, com o efeito que `DCS-28` fixa: o loop para em qualquer rota sem executar a ação da rota, e a frase, a rota e o dossiê de emenda, se houver, vão ao relatório de encerramento.
- **Fundamento:** `DCS-4`, `DCS-6`, `DCS-27`, `DCS-28`; achados `AE-5` (inconclusivo), `AE-7`; laudo da `CON-T4` (aprovado 100, `seguir`).
- **Operação do modelo:** `OP-2`
  - OP-2: O autor de papéis reescreve a definição de conduta do consultor sobre a norma nova: tira dela o estatuto provisório, faz qualquer das três razões de parada acioná-lo, dá a ele a rota que devolve, os deveres de validar a emenda do modelo no marco e de emiti-la quando a resolução muda o que o plano entrega, a linha de estatística que ele apensa a cada acionamento e a saída curta por edição mínima.
  - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`); parada de executor — nenhuma operação altera uma parada. O que se observa nela, antes e depois, é o caminho: quem a recebe, quem decide a rota e onde isso fica registrado. As paradas do `P-0745` e do `P-0746` (`F-8`) são o retrato do antes; o depois são as paradas da janela de execução deste plano, lidas no arquivo de estatística de `DCS-8` a partir do aceite da `OP-2`; planejador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 13, 19, 20 e 25 — é a fronteira do consultor e nada além: a rodada de replanejamento chega pela rota `planejador` da triagem, só quando emenda aceita cria ou remove operação ou quando a premissa cai inteira (`superseded`), e o corretivo `T<n>a` da mesma operação, com o id apensado à lista `tarefas:`, passa a ser também ato do consultor (`DCS-4`). O que `DCS-18` deixa com o planejamento continua com ele. Alterar outra conduta do planejador é colateral e se escala; modelador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 26, 27 e 28 — é a fronteira do consultor e nada além: o consultor é nomeado como quem origina o dossiê de `emenda` e como quem apensa o id do corretivo à lista `tarefas:`; quem despacha continua sendo quem conduz a sessão (`I-2`). Os literais que a guarda executável prende no arquivo dele (`F-15`) ficam. O instrumento do modelo e seus testes não se tocam
- **Camada e fronteira:** definição de agente — `.claude/agents/pantonic-consultant.md`, só a linha `:19` (*Por que você existe*) e a frase de abertura do item 2 (`:24`), ambas do item 24 de `F-4`; sem código.
- **Domínio:** **linha `estrategico=`** — segunda linha do retorno do consultor, presente só quando ele classifica o impedimento como estratégico; com ela o loop **PARA** em qualquer rota **sem executar a ação da rota** (`DCS-27`, `DCS-28`). **Cenário persistido** — `docs/plans/_CENARIO-<plano>.md`, o que atravessa os acionamentos no lugar do contexto vivo (`DCS-6`).
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-consultant.md`
- **Contratos/classes:** nenhuma assinatura de código; o front matter (`:1-6`) não muda.
- **Passos:**
  1. Em `.claude/agents/pantonic-consultant.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**.
  2. Em `.claude/agents/pantonic-consultant.md`, substitua o bloco **Texto atual 2** pelo bloco **Texto novo 2**.
- **Restrições desta tarefa:**
  - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação.
  - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`).
  - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`).
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:**
  - Não tocar a linha `description:` (`:3`) do agente: é da `CON-T8` (`F-16`); a linha 6 da `Verificação` mede isso.
  - Não tocar as linhas de forma que a `CON-T4` escreveu (`:8`, item 1, *Coesão do seu contexto*): são do item 44 (`OP-4`); a linha 5 da `Verificação` mede isso.
- **Contingências:**
  - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco
  - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido
  - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa`
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`.
- **Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-23 pelo consultor na árvore real, com os blocos aplicados e revertidos por hash, **como está depois da `CON-T4`**; o executor mede o **antes** antes da primeira edição.
  1. antes `1` · depois `0`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'num contexto só').Count
     ~~~~

  2. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'num arquivo só').Count
     ~~~~

  3. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'estrategico=').Count
     ~~~~

  4. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'sem executar a ação da rota').Count
     ~~~~

  5. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'você é **efêmero**').Count
     ~~~~

  6. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'Figura ad-hoc, provisória, criada por decisão do dono em 2026-09-18.').Count
     ~~~~

  7. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'rota=<resolve|modelador|planejador>').Count
     ~~~~

  8. antes `0` · depois `0`

     ~~~~
     python .claude/tools/backlog.py check; $LASTEXITCODE
     ~~~~

  9. antes `0` · depois `0`

     ~~~~
     python .claude/tools/modelo.py check --plano docs/plans/P-0747-consultor-de-plano.md; $LASTEXITCODE
     ~~~~

  10. antes `0` · depois `0`

     ~~~~
     pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift; $LASTEXITCODE
     ~~~~

  11. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes e `277 passed` depois, no ensaio de 2026-09-23 com os três corretivos aplicados)

     ~~~~
     python -m pytest -q
     ~~~~
- **Pronto quando:**
  - `consultor.alcance da triagem das paradas` — fatia da `OP-2` (`F-4` item 24): o retorno enunciado no agente tem as duas linhas, `rota=` e `estrategico=`, e a segunda diz que o loop para sem executar a ação da rota — Verificação 3, 4, 7
  - `consultor.estatuto na doutrina` — fatia da `OP-2` (`F-4` item 24): a definição de conduta não contradiz a própria forma — a `:19` descreve o cenário persistido, não o contexto vivo — Verificação 1, 2, 5
- **Fora do escopo desta tarefa:** a skill do loop (`CON-T3b`, `CON-T4a`); a `description` (`CON-T8`).

**Texto atual 1** — `.claude/agents/pantonic-consultant.md`:

~~~~
uma de cada vez, porque nenhuma delas tinha o contexto da anterior. Você é a correção disso: o
cenário fica **num contexto só**, vivo, e cada escalonamento chega a quem já sabe o que houve.
~~~~

**Texto novo 1** — `.claude/agents/pantonic-consultant.md`:

~~~~
uma de cada vez, porque nenhuma delas tinha o contexto da anterior. Você é a correção disso: o
cenário fica **num arquivo só**, persistido, e cada acionamento nasce lendo o que já houve em vez de redescobri-lo.
~~~~

**Texto atual 2** — `.claude/agents/pantonic-consultant.md`:

~~~~
A primeira linha do seu retorno é `rota=<resolve|modelador|planejador>`, seguida da decisão e do reparo — nunca de opções:
~~~~

**Texto novo 2** — `.claude/agents/pantonic-consultant.md`:

~~~~
A primeira linha do seu retorno é `rota=<resolve|modelador|planejador>`; a segunda, só quando o impedimento é estratégico — muda escopo ou objetivo do plano, ou revoga decisão do dono —, é `estrategico=<uma frase>`, e com ela o loop **para** em qualquer rota sem executar a ação da rota: o reparo já gravado fica no plano, e a frase, a rota e o dossiê de emenda, se houver, vão ao relatório de encerramento (`DCS-27`, `DCS-28`). Depois vêm a decisão e o reparo — nunca opções:
~~~~

### CON-T3b — Corretivo da OP-3: com estrategico= o loop para sem executar a ação da rota [Sonnet · esforço medium · classe mecanica]
- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T2a`
- **Objetivo:** Corretivo da `CON-T3a` (`AE-6`, `DCS-28`): a triagem do passo 8 e a lista *O que obriga parada* passam a fixar a ordem entre parar e agir — com `estrategico=` presente o loop **PARA** sem executar a ação da rota: o reparo que o consultor já gravou fica no plano, o modelador **não** é despachado, e a frase, a rota e o dossiê de emenda, se houver, vão ao relatório de encerramento, para o dono decidir antes de qualquer ato sobre o modelo. O dossiê ganha destino nomeado.
- **Fundamento:** `DCS-3`, `DCS-4`, `DCS-24`, `DCS-27`, `DCS-28`; achado `AE-6`; laudo da `CON-T3a` (aprovado 100, `seguir`).
- **Operação do modelo:** `OP-3`
  - OP-3: O mantenedor do loop reescreve a condução das paradas: as duas fontes normativas da skill passam a citar as decisões deste plano, toda regra que roteia parada de executor ou laudo com pendência substantiva e o guardrail que manda a matéria ao planejador passam a levá-los ao consultor, o loop despacha a rota que ele devolve e, quando a rota é o modelador, despacha o modelador sem parar a janela e leva o pedido de validar o drift ao dono no marco.
  - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`); parada de executor — nenhuma operação altera uma parada. O que se observa nela, antes e depois, é o caminho: quem a recebe, quem decide a rota e onde isso fica registrado. As paradas do `P-0745` e do `P-0746` (`F-8`) são o retrato do antes; o depois são as paradas da janela de execução deste plano, lidas no arquivo de estatística de `DCS-8` a partir do aceite da `OP-2`; planejador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 13, 19, 20 e 25 — é a fronteira do consultor e nada além: a rodada de replanejamento chega pela rota `planejador` da triagem, só quando emenda aceita cria ou remove operação ou quando a premissa cai inteira (`superseded`), e o corretivo `T<n>a` da mesma operação, com o id apensado à lista `tarefas:`, passa a ser também ato do consultor (`DCS-4`). O que `DCS-18` deixa com o planejamento continua com ele. Alterar outra conduta do planejador é colateral e se escala; modelador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 26, 27 e 28 — é a fronteira do consultor e nada além: o consultor é nomeado como quem origina o dossiê de `emenda` e como quem apensa o id do corretivo à lista `tarefas:`; quem despacha continua sendo quem conduz a sessão (`I-2`). Os literais que a guarda executável prende no arquivo dele (`F-15`) ficam. O instrumento do modelo e seus testes não se tocam
- **Camada e fronteira:** procedimento de orquestração — `.claude/skills/scrum-master/SKILL.md`, só a triagem do passo 8 e a lista *O que obriga parada* (`F-4` itens 2 e 8, já reescritos pela `CON-T3` e pela `CON-T3a`); sem código.
- **Domínio:** **linha `estrategico=`** — com ela o loop **PARA** em qualquer rota **sem executar a ação da rota** (`DCS-28`); as regras `A3a`..`B1` continuam remetendo ao passo 8 (*"como o passo 8 manda"*), por isso só a fonte muda. Invariante: sem `estrategico=`, `resolve` e `modelador` seguem e `planejador` para (`DCS-24`).
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
- **Contratos/classes:** nenhuma assinatura de código; nenhuma linha de tabela muda.
- **Passos:**
  1. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**.
  2. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 2** pelo bloco **Texto novo 2**.
- **Restrições desta tarefa:**
  - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação.
  - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`).
  - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`).
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:**
  - Não tocar a `A1` nem a seção `## Acionamento do consultor`: são da `CON-T4a`; a linha 7 da `Verificação` mede isso.
  - Não tocar as regras `A3a`, `A3b`, `A3c`, `A6a`, `A7` e `B1`: elas remetem ao passo 8, que é o que muda; as linhas 4 e 5 da `Verificação` medem isso.
- **Contingências:**
  - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco
  - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido
  - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa`
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`.
- **Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-23 pelo consultor na árvore real, com os blocos aplicados e revertidos por hash, **como está depois da `CON-T2a`** (que não toca a skill); o executor mede o **antes** antes da primeira edição. A linha 6 é a coerência do módulo herdada da `CON-T3a`.
  1. antes `0` · depois `2`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'sem executar a ação da rota').Count
     ~~~~

  2. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'o modelador **não** é despachado').Count
     ~~~~

  3. antes `10` · depois `10`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'estrategico=').Count
     ~~~~

  4. antes `5` · depois `5`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'que devolve a rota (passo 8)').Count
     ~~~~

  5. antes `5` · depois `5`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern '`planejador` e `estrategico=` **PARAM**').Count
     ~~~~

  6. antes `0` · depois `0`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'rota=resolve' | Where-Object { $_.Line -cnotmatch 'estrategico=' }).Count
     ~~~~

  7. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'uma retomada por `SendMessage` ao mesmo `agentId`').Count
     ~~~~

  8. antes `0` · depois `0`

     ~~~~
     python .claude/tools/backlog.py check; $LASTEXITCODE
     ~~~~

  9. antes `0` · depois `0`

     ~~~~
     python .claude/tools/modelo.py check --plano docs/plans/P-0747-consultor-de-plano.md; $LASTEXITCODE
     ~~~~

  10. antes `0` · depois `0`

     ~~~~
     pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift; $LASTEXITCODE
     ~~~~

  11. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes e `277 passed` depois, no ensaio de 2026-09-23 com os três corretivos aplicados)

     ~~~~
     python -m pytest -q
     ~~~~
- **Pronto quando:**
  - `consultor.alcance da triagem das paradas` — fatia da `OP-3` (`F-4` itens 2 e 8): com `estrategico=` o loop para sem executar a ação da rota, e o dossiê de emenda tem destino nomeado — o relatório de encerramento, para o dono —; as demais regras seguem remetendo ao passo 8 — Verificação 1 a 6
- **Fora do escopo desta tarefa:** a `A1` e a seção `## Acionamento do consultor` (`CON-T4a`); o agente do consultor (`CON-T2a`).

**Texto atual 1** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
`estrategico=` presente — **PARA** em qualquer rota, e a frase vai ao relatório de encerramento (`G-NOASK`);
~~~~

**Texto novo 1** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
`estrategico=` presente — **PARA** em qualquer rota **sem executar a ação da rota**: o reparo que o consultor já gravou fica no plano, o modelador **não** é despachado, e a frase, a rota e o dossiê de emenda, se houver, vão ao relatório de encerramento, para o dono decidir antes de qualquer ato sobre o modelo (`G-NOASK`; `P-0747` `DCS-28`);
~~~~

**Texto atual 2** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
encerram-na a rota `planejador` e a linha `estrategico=`; a rota `modelador` despacha o modelador e segue, com a versão pendente até o marco.
~~~~

**Texto novo 2** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
encerram-na a rota `planejador` e a linha `estrategico=` — esta sem executar a ação da rota, com o dossiê de emenda, se houver, no relatório de encerramento (`DCS-28`); a rota `modelador` sem `estrategico=` despacha o modelador e segue, com a versão pendente até o marco.
~~~~

### CON-T4a — Corretivo da OP-4: a queda de uma instância do consultor não se retoma [Sonnet · esforço medium · classe mecanica]
- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T3b`
- **Objetivo:** Corretivo da `CON-T4` (`AE-8`, `DCS-29`): a `A1` deixa de ser genérica — executor e `reviewer` se retomam por `SendMessage`; uma instância do consultor que cai se descarta, a telemetria dela registra `PARCIAL — trecho pré-queda não medido`, e o loop despacha uma instância nova com as mesmas três entradas, sobre o cenário como a caída o deixou; segunda queda no mesmo acionamento **PARA** —, e a seção *Acionamento do consultor* passa a dizer o mesmo. Uma regra para a queda, não duas.
- **Fundamento:** `DCS-4`, `DCS-6`, `DCS-19`, `DCS-29`; achado `AE-8`; laudo da `CON-T4` (aprovado 100, `seguir`).
- **Operação do modelo:** `OP-4`
  - OP-4: O mantenedor do loop instala a forma efêmera do consultor com o cenário persistido, numa seção própria da skill e não num passo novo: cada acionamento nasce uma instância que lê o cenário do plano e o card em causa, decide, reescreve o cenário com edição mínima e se encerra; o cenário passa a ser o próprio handover, a retomada da instância de prontidão sai da nota de telemetria, o reprovisionamento por limite deixa de existir, e as linhas do corpo do agente e da regra do loop que o descrevem instanciado uma vez por plano passam a descrevê-lo efêmero.
  - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`); acionamento do consultor — nenhuma operação altera um acionamento. O que se observa nele é o custo, apurado pelo método de `F-7`; a sonda é descartável e não vira artefato. Retrato do antes: as instâncias 1-4 da forma standby (`F-7`) e a série de `F-8`; o depois: os acionamentos da janela de execução deste plano a partir do aceite da `OP-4`
- **Camada e fronteira:** procedimento de orquestração — `.claude/skills/scrum-master/SKILL.md`, só a linha `A1` do bloco A e uma frase da seção `## Acionamento do consultor` (residência da `OP-4`); sem código.
- **Domínio:** **queda de instância** — notificação sem bloco `<usage>`; para o consultor, descarte e despacho novo em vez de retomada, porque o cenário é o handover (`DCS-6`, `DCS-29`).
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
- **Contratos/classes:** nenhuma assinatura de código; a linha `A1` mantém as três colunas `| # | condição | ação |`.
- **Passos:**
  1. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**.
  2. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 2** pelo bloco **Texto novo 2**.
- **Restrições desta tarefa:**
  - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação.
  - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`).
  - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`).
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:**
  - Não tocar o passo 8 nem a lista *O que obriga parada*: são da `CON-T3b`; a linha 6 da `Verificação` mede isso.
  - Não tocar a nota de telemetria do passo 9 (*"o consultor nunca é retomado"*): já diz o certo; a linha 4 da `Verificação` mede isso.
  - Não criar passo novo nem seção nova (`DCS-19`).
- **Contingências:**
  - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco
  - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido
  - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa`
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`.
- **Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-23 pelo consultor na árvore real, com os blocos aplicados e revertidos por hash, **como está depois da `CON-T3b`**; o executor mede o **antes** antes da primeira edição.
  1. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'Consultor: **nenhuma** retomada').Count
     ~~~~

  2. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'a instância que cai se descarta').Count
     ~~~~

  3. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'uma retomada por `SendMessage` ao mesmo `agentId`').Count
     ~~~~

  4. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'o consultor nunca é retomado').Count
     ~~~~

  5. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern '## Acionamento do consultor').Count
     ~~~~

  6. antes `2` · depois `2`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'sem executar a ação da rota').Count
     ~~~~

  7. antes `0` · depois `0`

     ~~~~
     python .claude/tools/backlog.py check; $LASTEXITCODE
     ~~~~

  8. antes `0` · depois `0`

     ~~~~
     python .claude/tools/modelo.py check --plano docs/plans/P-0747-consultor-de-plano.md; $LASTEXITCODE
     ~~~~

  9. antes `0` · depois `0`

     ~~~~
     pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift; $LASTEXITCODE
     ~~~~

  10. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes e `277 passed` depois, no ensaio de 2026-09-23 com os três corretivos aplicados)

     ~~~~
     python -m pytest -q
     ~~~~
- **Pronto quando:**
  - `consultor.forma da figura` — fatia da `OP-4` (seção `## Acionamento do consultor` e a `A1` que a contradizia): a queda de uma instância do consultor tem uma regra só — descarte e despacho de instância nova sobre o cenário, nunca retomada por `SendMessage` — Verificação 1 a 5
- **Fora do escopo desta tarefa:** o passo 8 e a lista de parada (`CON-T3b`); o agente do consultor (`CON-T2a`).

**Texto atual 1** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
| `A1` | queda do subagente (notificação sem bloco `<usage>`) | uma retomada por `SendMessage` ao mesmo `agentId` com "o que falta"; registra `PARCIAL — trecho pré-queda não medido`. Retomou: segue por `A2`..`A9`. Não retomou: **PARA** |
~~~~

**Texto novo 1** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
| `A1` | queda do subagente (notificação sem bloco `<usage>`) | executor ou `reviewer`: uma retomada por `SendMessage` ao mesmo `agentId` com "o que falta"; registra `PARCIAL — trecho pré-queda não medido`. Retomou: segue por `A2`..`A9`. Não retomou: **PARA**. Consultor: **nenhuma** retomada — a instância caída se descarta, a telemetria dela registra `PARCIAL — trecho pré-queda não medido`, e o loop despacha **uma instância nova** com as mesmas três entradas, sobre o cenário como a caída o deixou (seção *Acionamento do consultor*; `P-0747` `DCS-29`). Caiu de novo no mesmo acionamento: **PARA** |
~~~~

**Texto atual 2** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
Nenhuma instância é retomada por `SendMessage` e nenhuma é reprovisionada por limite: o cenário **é** o handover.
~~~~

**Texto novo 2** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
Nenhuma instância é retomada por `SendMessage` e nenhuma é reprovisionada por limite: o cenário **é** o handover, e a instância que cai se descarta — a `A1` despacha outra, com as mesmas três entradas, sobre o cenário como ficou.
~~~~

### CON-T3c — Corretivo da OP-3: com estrategico= a rota planejador executa a sua ação, que já é a parada [Sonnet · esforço medium · classe mecanica]
- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T4a`
- **Objetivo:** Corretivo da `CON-T3b` (`AE-10` ii, `DCS-30`): a triagem do passo 8 e a lista *O que obriga parada* deixam de suspender a ação da rota "em qualquer rota" — a suspensão com `estrategico=` vale para `resolve` e `modelador`; com `rota=planejador` a ação da rota já é a parada e se executa como está (`DCS-28`): o plano é materializado `blocked`, a rodada de replanejamento enfileirada, e a frase vai junto ao relatório de encerramento.
- **Fundamento:** `DCS-3`, `DCS-4`, `DCS-28`, `DCS-30`; achado `AE-10` (ii); laudo da `CON-T3b` (aprovado 100, `seguir`).
- **Operação do modelo:** `OP-3`
  - OP-3: O mantenedor do loop reescreve a condução das paradas: as duas fontes normativas da skill passam a citar as decisões deste plano, toda regra que roteia parada de executor ou laudo com pendência substantiva e o guardrail que manda a matéria ao planejador passam a levá-los ao consultor, o loop despacha a rota que ele devolve e, quando a rota é o modelador, despacha o modelador sem parar a janela e leva o pedido de validar o drift ao dono no marco.
  - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`); parada de executor — nenhuma operação altera uma parada. O que se observa nela, antes e depois, é o caminho: quem a recebe, quem decide a rota e onde isso fica registrado. As paradas do `P-0745` e do `P-0746` (`F-8`) são o retrato do antes; o depois são as paradas da janela de execução deste plano, lidas no arquivo de estatística de `DCS-8` a partir do aceite da `OP-2`; planejador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 13, 19, 20 e 25 — é a fronteira do consultor e nada além: a rodada de replanejamento chega pela rota `planejador` da triagem, só quando emenda aceita cria ou remove operação ou quando a premissa cai inteira (`superseded`), e o corretivo `T<n>a` da mesma operação, com o id apensado à lista `tarefas:`, passa a ser também ato do consultor (`DCS-4`). O que `DCS-18` deixa com o planejamento continua com ele. Alterar outra conduta do planejador é colateral e se escala; modelador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 26, 27 e 28 — é a fronteira do consultor e nada além: o consultor é nomeado como quem origina o dossiê de `emenda` e como quem apensa o id do corretivo à lista `tarefas:`; quem despacha continua sendo quem conduz a sessão (`I-2`). Os literais que a guarda executável prende no arquivo dele (`F-15`) ficam. O instrumento do modelo e seus testes não se tocam
- **Camada e fronteira:** procedimento de orquestração — `.claude/skills/scrum-master/SKILL.md`, só a triagem do passo 8 e a lista *O que obriga parada* (`F-4` itens 2 e 8, já reescritos pela `CON-T3`, pela `CON-T3a` e pela `CON-T3b`); sem código.
- **Domínio:** **linha `estrategico=` com `rota=planejador`** — a ação da rota é a própria parada (`DCS-28`), e suspendê-la deixaria o plano sem `blocked` materializado e sem rodada de replanejamento enfileirada (`G-REPLAN`); nas rotas `resolve` e `modelador` nada muda em relação à `CON-T3b`. Invariante: sem `estrategico=`, `resolve` e `modelador` seguem e `planejador` para (`DCS-24`).
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
- **Contratos/classes:** nenhuma assinatura de código; nenhuma linha de tabela muda.
- **Passos:**
  1. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**.
  2. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 2** pelo bloco **Texto novo 2**.
- **Restrições desta tarefa:**
  - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação.
  - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`).
  - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`).
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:**
  - Não tocar a `A1`, a seção `## Acionamento do consultor` nem a nota de telemetria do passo 9: são da `OP-4` (`CON-T4`, `CON-T4a`); a linha 7 da `Verificação` mede isso.
  - Não tocar as regras `A3a`, `A3b`, `A3c`, `A6a`, `A7` e `B1`: elas remetem ao passo 8, que é o que muda; a linha 5 da `Verificação` mede isso.
- **Contingências:**
  - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco
  - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido
  - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa`
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`.
- **Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-23 pelo consultor (acionamento 5) na árvore real, com os blocos aplicados e revertidos por hash, **como está depois da `CON-T4a`**; o executor mede o **antes** antes da primeira edição. A linha 4 é a coerência do módulo herdada da `CON-T3b`: as duas ocorrências ficam, qualificadas.
  1. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'a ação da rota já é a parada').Count
     ~~~~

  2. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'se executa com ou sem `estrategico=`').Count
     ~~~~

  3. antes `0` · depois `2`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'nas rotas `resolve` e `modelador`').Count
     ~~~~

  4. antes `2` · depois `2`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'sem executar a ação da rota').Count
     ~~~~

  5. antes `5` · depois `5`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern '`planejador` e `estrategico=` **PARAM**').Count
     ~~~~

  6. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'o modelador **não** é despachado').Count
     ~~~~

  7. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'Consultor: **nenhuma** retomada').Count
     ~~~~

  8. antes `0` · depois `0`

     ~~~~
     python .claude/tools/backlog.py check; $LASTEXITCODE
     ~~~~

  9. antes `0` · depois `0`

     ~~~~
     python .claude/tools/modelo.py check --plano docs/plans/P-0747-consultor-de-plano.md; $LASTEXITCODE
     ~~~~

  10. antes `0` · depois `0`

     ~~~~
     pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift; $LASTEXITCODE
     ~~~~

  11. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes — laudo da `CON-T4a`, mesma árvore — e `277 passed` depois, no ensaio de 2026-09-23 do acionamento 5)

     ~~~~
     python -m pytest -q
     ~~~~
- **Pronto quando:**
  - `consultor.alcance da triagem das paradas` — fatia da `OP-3` (`F-4` itens 2 e 8): com `estrategico=` a suspensão da ação da rota vale para `resolve` e `modelador`, e a rota `planejador` executa a sua ação, que já é a parada — plano `blocked`, replanejamento enfileirado, frase no relatório — Verificação 1 a 6
- **Fora do escopo desta tarefa:** a `A1`, a seção `## Acionamento do consultor` e a nota de telemetria do passo 9 (`OP-4`); o agente do consultor (item 24, `OP-2`), cuja frase *"em qualquer rota sem executar a ação da rota"* se lê com a `DCS-28` que cita (`AE-12`, inconclusivo).

**Texto atual 1** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
`estrategico=` presente — **PARA** em qualquer rota **sem executar a ação da rota**: o reparo que o consultor já gravou fica no plano, o modelador **não** é despachado, e a frase, a rota e o dossiê de emenda, se houver, vão ao relatório de encerramento, para o dono decidir antes de qualquer ato sobre o modelo (`G-NOASK`; `P-0747` `DCS-28`);
~~~~

**Texto novo 1** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
`estrategico=` presente — **PARA** em qualquer rota, e nas rotas `resolve` e `modelador` **sem executar a ação da rota**: o reparo que o consultor já gravou fica no plano, o modelador **não** é despachado, e a frase, a rota e o dossiê de emenda, se houver, vão ao relatório de encerramento, para o dono decidir antes de qualquer ato sobre o modelo (`G-NOASK`; `P-0747` `DCS-28`); com `rota=planejador` a ação da rota já é a parada e se executa como está — o plano materializado `blocked`, a rodada de replanejamento enfileirada — e a frase vai junto ao relatório;
~~~~

**Texto atual 2** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
encerram-na a rota `planejador` e a linha `estrategico=` — esta sem executar a ação da rota, com o dossiê de emenda, se houver, no relatório de encerramento (`DCS-28`);
~~~~

**Texto novo 2** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
encerram-na a rota `planejador` — cuja ação, materializar o plano `blocked` e enfileirar o replanejamento, se executa com ou sem `estrategico=` — e a linha `estrategico=` — esta, nas rotas `resolve` e `modelador`, sem executar a ação da rota, com o dossiê de emenda, se houver, no relatório de encerramento (`DCS-28`);
~~~~

### CON-T5 — O outro lado da fronteira nas definições de conduta [Sonnet · esforço medium · classe mecanica]
- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T3c`
- **Objetivo:** O autor de papéis escreve o outro lado da fronteira em toda definição de conduta que ainda manda a parada direto ao replanejamento: quem planeja passa a receber a rodada pela rota da triagem, quem escreve o modelo passa a nomear o consultor como origem da emenda e como quem estende a lista de tarefas, quem executa e quem revisa passam a devolver a parada e a pendência à triagem, e a regra de transição de estado do diário, a passagem de bastão e a regra global de não decidir passam a dizer o mesmo.
- **Fundamento:** `DCS-3`, `DCS-4`, `DCS-5`, `DCS-13`, `DCS-18`, `DCS-24`; fatos `F-4` itens 25 a 38, `F-15`; ato 1 da §0.
- **Operação do modelo:** `OP-5`
  - OP-5: O autor de papéis escreve o outro lado da fronteira em toda definição de conduta que ainda manda a parada direto ao replanejamento: quem planeja passa a receber a rodada pela rota da triagem, quem escreve o modelo passa a nomear o consultor como origem da emenda e como quem estende a lista de tarefas, quem executa e quem revisa passam a devolver a parada e a pendência à triagem, e a regra de transição de estado do diário, a passagem de bastão e a regra global de não decidir passam a dizer o mesmo.
  - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`); planejador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 13, 19, 20 e 25 — é a fronteira do consultor e nada além: a rodada de replanejamento chega pela rota `planejador` da triagem, só quando emenda aceita cria ou remove operação ou quando a premissa cai inteira (`superseded`), e o corretivo `T<n>a` da mesma operação, com o id apensado à lista `tarefas:`, passa a ser também ato do consultor (`DCS-4`). O que `DCS-18` deixa com o planejamento continua com ele. Alterar outra conduta do planejador é colateral e se escala; modelador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 26, 27 e 28 — é a fronteira do consultor e nada além: o consultor é nomeado como quem origina o dossiê de `emenda` e como quem apensa o id do corretivo à lista `tarefas:`; quem despacha continua sendo quem conduz a sessão (`I-2`). Os literais que a guarda executável prende no arquivo dele (`F-15`) ficam. O instrumento do modelo e seus testes não se tocam; parada de executor — nenhuma operação altera uma parada. O que se observa nela, antes e depois, é o caminho: quem a recebe, quem decide a rota e onde isso fica registrado. As paradas do `P-0745` e do `P-0746` (`F-8`) são o retrato do antes; o depois são as paradas da janela de execução deste plano, lidas no arquivo de estatística de `DCS-8` a partir do aceite da `OP-2`
- **Camada e fronteira:** definições de agente e skills — sete arquivos, só nas linhas dos itens 25 a 38 de `F-4`; sem código.
- **Domínio:** **rota `planejador`** — emenda aceita que cria ou remove operação, ou premissa caída por inteiro; **card corretivo `T<n>a`** — da mesma operação, autorado pelo consultor na rota `resolve`, com o id apensado à lista `tarefas:`.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md`
  - `.claude/agents/pantonic-model-designer.md`
  - `.claude/agents/pantonic-executor.md`
  - `.claude/agents/pantonic-reviewer.md`
  - `.claude/skills/diario-de-obras/SKILL.md`
  - `.claude/skills/passagem-de-bastao/SKILL.md`
  - `.claude/global/CLAUDE.md`
- **Contratos/classes:** nenhuma assinatura de código.
- **Passos:**
  1. Em `.claude/agents/pantonic-planner.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**.
  2. Em `.claude/agents/pantonic-planner.md`, substitua o bloco **Texto atual 2** pelo bloco **Texto novo 2**.
  3. Em `.claude/agents/pantonic-model-designer.md`, substitua o bloco **Texto atual 3** pelo bloco **Texto novo 3**.
  4. Em `.claude/agents/pantonic-model-designer.md`, substitua o bloco **Texto atual 4** pelo bloco **Texto novo 4**.
  5. Em `.claude/agents/pantonic-model-designer.md`, substitua o bloco **Texto atual 5** pelo bloco **Texto novo 5**.
  6. Em `.claude/agents/pantonic-executor.md`, substitua o bloco **Texto atual 6** pelo bloco **Texto novo 6**.
  7. Em `.claude/agents/pantonic-executor.md`, substitua o bloco **Texto atual 7** pelo bloco **Texto novo 7**.
  8. Em `.claude/agents/pantonic-executor.md`, substitua o bloco **Texto atual 8** pelo bloco **Texto novo 8**.
  9. Em `.claude/agents/pantonic-executor.md`, substitua o bloco **Texto atual 9** pelo bloco **Texto novo 9**.
  10. Em `.claude/agents/pantonic-reviewer.md`, substitua o bloco **Texto atual 10** pelo bloco **Texto novo 10**.
  11. Em `.claude/agents/pantonic-reviewer.md`, substitua o bloco **Texto atual 11** pelo bloco **Texto novo 11**.
  12. Em `.claude/skills/diario-de-obras/SKILL.md`, substitua o bloco **Texto atual 12** pelo bloco **Texto novo 12**.
  13. Em `.claude/skills/diario-de-obras/SKILL.md`, substitua o bloco **Texto atual 13** pelo bloco **Texto novo 13**.
  14. Em `.claude/skills/passagem-de-bastao/SKILL.md`, substitua o bloco **Texto atual 14** pelo bloco **Texto novo 14**.
  15. Em `.claude/skills/passagem-de-bastao/SKILL.md`, substitua o bloco **Texto atual 15** pelo bloco **Texto novo 15**.
  16. Em `.claude/skills/passagem-de-bastao/SKILL.md`, substitua o bloco **Texto atual 16** pelo bloco **Texto novo 16**.
  17. Em `.claude/global/CLAUDE.md`, substitua o bloco **Texto atual 17** pelo bloco **Texto novo 17**.
- **Restrições desta tarefa:**
  - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação.
  - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`).
  - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`).
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:**
  - Não tocar `.claude/skills/passagem-de-bastao/SKILL.md:93`, `:129`, `:223` nem `.claude/global/CLAUDE.md:162`: são os casos de `DCS-18`.
  - Não tocar `.claude/skills/passagem-de-bastao/SKILL.md:136` (item 34): já escala ao consultor.
  - Não propagar a Regra 8 para `~/.claude/CLAUDE.md` nem para projetos derivados (`DCS-13`).
  - Não reescrever os literais `Só cinco violações`, `` `V1` e `V3` ``, `` exceto `V1` e `V3` ``, `SAÍDA 3`, `Fase 3b`, `Nenhum teto se escreve no` (`F-15`).
- **Contingências:**
  - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco
  - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido
  - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa`
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`; quando o card toca arquivo preso por literal (`F-15`), também `tests/test_doutrina_unidade.py`.
- **Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-22 numa cópia da árvore com os cards anteriores aplicados em ensaio; o executor mede o **antes** antes da primeira edição.
  1. antes `1` · depois `0`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-planner.md' -SimpleMatch -CaseSensitive -Pattern 'só a você').Count
     ~~~~

  2. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-planner.md' -SimpleMatch -CaseSensitive -Pattern 'A você ele chega só pela rota `planejador` da triagem').Count
     ~~~~

  3. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-planner.md' -SimpleMatch -CaseSensitive -Pattern 'lastro que é seu e do consultor').Count
     ~~~~

  4. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-model-designer.md' -SimpleMatch -CaseSensitive -Pattern 'que é do planejador e do consultor depois da autoria').Count
     ~~~~

  5. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-model-designer.md' -SimpleMatch -CaseSensitive -Pattern 'quando a decisão nasce da triagem de uma parada').Count
     ~~~~

  6. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-model-designer.md' -SimpleMatch -CaseSensitive -Pattern 'depois é lastro do planejador e do consultor').Count
     ~~~~

  7. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-model-designer.md' -SimpleMatch -CaseSensitive -Pattern 'Só cinco violações').Count
     ~~~~

  8. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-model-designer.md' -SimpleMatch -CaseSensitive -Pattern 'exceto `V1` e `V3`').Count
     ~~~~

  9. antes `5` · depois `2`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-executor.md' -SimpleMatch -CaseSensitive -Pattern 'planejador').Count
     ~~~~

  10. antes `0` · depois `4`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-executor.md' -SimpleMatch -CaseSensitive -Pattern 'consultor').Count
     ~~~~

  11. antes `1` · depois `0`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-reviewer.md' -SimpleMatch -CaseSensitive -Pattern 'roteia ao **planejamento**').Count
     ~~~~

  12. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-reviewer.md' -SimpleMatch -CaseSensitive -Pattern 'triagem do consultor').Count
     ~~~~

  13. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/diario-de-obras/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'é do **consultor**, na rota `resolve` da triagem').Count
     ~~~~

  14. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/diario-de-obras/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'a triagem do consultor (rota `resolve`)').Count
     ~~~~

  15. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/passagem-de-bastao/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'delegada ao `pantonic-planner`').Count
     ~~~~

  16. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/passagem-de-bastao/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'Bloqueio de executor vai à triagem').Count
     ~~~~

  17. antes `1` · depois `0`

     ~~~~
     (Select-String -Path '.claude/skills/passagem-de-bastao/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'ao planejador (`GOVERNANCA.md` §3, escada').Count
     ~~~~

  18. antes `0` · depois `2`

     ~~~~
     (Select-String -Path '.claude/skills/passagem-de-bastao/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'triagem do consultor').Count
     ~~~~

  19. antes `1` · depois `0`

     ~~~~
     (Select-String -Path '.claude/global/CLAUDE.md' -SimpleMatch -CaseSensitive -Pattern 'escala para replanejamento').Count
     ~~~~

  20. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/global/CLAUDE.md' -SimpleMatch -CaseSensitive -Pattern 'devolve `blocked` à triagem do plano').Count
     ~~~~

  21. `8 passed` antes · `8 passed` depois

     ~~~~
     python -m pytest -q tests/test_doutrina_unidade.py
     ~~~~

  22. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes e `277 passed` depois, no ensaio)

     ~~~~
     python -m pytest -q
     ~~~~

- **Pronto quando:**
  - `consultor.fronteira com o planejador` — escrita nos três lados — norma, agente do consultor, agente do planejador —: o consultor fecha o técnico e o tático (reescreve card, reordena fila, repara instrumento, toma decisão nova com id, autora o corretivo da mesma operação e apensa o id à lista `tarefas:` dela); vai ao planejador só quando emenda aceita cria ou remove operação ou quando a premissa cai inteira; nunca reabre o objetivo do plano — Verificação 1, 2, 3, 13, 14, 15, 16
  - `consultor.fronteira com o modelador` — havendo drift — resolução que altera objeto, operação ou estado final da `## 1` —, o consultor devolve o dossiê `Ato de modelo` de `emenda` com o reparo e marca a rota `modelador`; o loop despacha o modelador sem parar a janela e a versão pendente coexiste com a vigente até o marco, onde o pedido de validar ou recusar o drift sobe ao dono; recusado, o consultor resolve preservando o modelo; o agente do consultor carrega os dois deveres e o do modelador o nomeia como origem da emenda — Verificação 4, 5, 6, 7, 8
  - `consultor.alcance da triagem das paradas` — toda parada de executor — `premissa`, `dependencia` ou `ferramenta` — e todo laudo com pendência substantiva chegam ao consultor, que devolve uma rota entre resolver, modelador e planejador, e o loop a despacha; o motivo é evidência, não rota; nenhum dos 47 itens de `F-4` manda a parada direto ao planejador, e as duas fontes normativas da skill do loop citam as decisões deste plano; o que `DCS-18` deixa fora continua indo ao planejamento — Verificação 9, 10, 11, 12, 17, 18, 19, 20
- **Fora do escopo desta tarefa:** `GOVERNANCA.md` (`CON-T1`), a skill do loop (`CON-T3`, `CON-T4`) e o `README.md` (`CON-T8`).

**Texto atual 1** — `.claude/agents/pantonic-planner.md`:

~~~~
Indício de que o plano precisa mudar chega como tarefa `blocked` razão `premissa`, registrado no
corpo dela e em `## Achados da execução` do plano — e chega a você, só a você.
~~~~

**Texto novo 1** — `.claude/agents/pantonic-planner.md`:

~~~~
Indício de que o plano precisa mudar chega primeiro ao `pantonic-consultant`, que tria toda parada de executor e fecha sozinho o técnico e o tático — inclusive o card corretivo `T<n>a` da mesma operação. A você ele chega só pela rota `planejador` da triagem: emenda aceita do modelo que cria ou remove operação, ou premissa caída por inteiro; registrado no
corpo da tarefa e em `## Achados da execução` do plano.
~~~~

**Texto atual 2** — `.claude/agents/pantonic-planner.md`:

~~~~
e o id dele entra na lista `tarefas:` daquela operação — lastro que é seu (`GOVERNANCA.md`
~~~~

**Texto novo 2** — `.claude/agents/pantonic-planner.md`:

~~~~
e o id dele entra na lista `tarefas:` daquela operação — lastro que é seu e do consultor (`GOVERNANCA.md`
~~~~

**Texto atual 3** — `.claude/agents/pantonic-model-designer.md`:

~~~~
que é do planejador depois da autoria
~~~~

**Texto novo 3** — `.claude/agents/pantonic-model-designer.md`:

~~~~
que é do planejador e do consultor depois da autoria
~~~~

**Texto atual 4** — `.claude/agents/pantonic-model-designer.md`:

~~~~
no dossiê de quem a tomou
~~~~

**Texto novo 4** — `.claude/agents/pantonic-model-designer.md`:

~~~~
no dossiê de quem a tomou — o `pantonic-consultant`, quando a decisão nasce da triagem de uma parada, ou o `pantonic-planner`, na rodada de replanejamento —
~~~~

**Texto atual 5** — `.claude/agents/pantonic-model-designer.md`:

~~~~
depois é lastro do planejador.
~~~~

**Texto novo 5** — `.claude/agents/pantonic-model-designer.md`:

~~~~
depois é lastro do planejador e do consultor, que apensa o id do card corretivo `T<n>a`.
~~~~

**Texto atual 6** — `.claude/agents/pantonic-executor.md`:

~~~~
está no plano, e quem o conserta é o planejador (G-EXECREADY
~~~~

**Texto novo 6** — `.claude/agents/pantonic-executor.md`:

~~~~
está no plano, e quem o tria é o consultor (G-EXECREADY
~~~~

**Texto atual 7** — `.claude/agents/pantonic-executor.md`:

~~~~
Quem recebe é o planejamento.
~~~~

**Texto novo 7** — `.claude/agents/pantonic-executor.md`:

~~~~
Quem recebe é a triagem do consultor.
~~~~

**Texto atual 8** — `.claude/agents/pantonic-executor.md`:

~~~~
`A3b` do `scrum-master`: para a janela e escala ao dono/planejador)
~~~~

**Texto novo 8** — `.claude/agents/pantonic-executor.md`:

~~~~
`A3b` do `scrum-master`: escala ao consultor, que devolve a rota)
~~~~

**Texto atual 9** — `.claude/agents/pantonic-executor.md`:

~~~~
quem recebe a escalada e decide é o planejador (escada em
~~~~

**Texto novo 9** — `.claude/agents/pantonic-executor.md`:

~~~~
quem recebe a parada e decide a rota é o consultor (escada em
~~~~

**Texto atual 10** — `.claude/agents/pantonic-reviewer.md`:

~~~~
loop — que a roteia ao **planejamento** (G-REPLAN/G-NOASK
~~~~

**Texto novo 10** — `.claude/agents/pantonic-reviewer.md`:

~~~~
loop — que a roteia à **triagem do consultor** (G-REPLAN/G-NOASK
~~~~

**Texto atual 11** — `.claude/agents/pantonic-reviewer.md`:

~~~~
ao dono chega só o que o planejador classificar como estratégico, nunca a sua linha direto.
~~~~

**Texto novo 11** — `.claude/agents/pantonic-reviewer.md`:

~~~~
ao dono chega só o que o consultor devolver como drift do modelo ou estratégico, nunca a sua linha direto.
~~~~

**Texto atual 12** — `.claude/skills/diario-de-obras/SKILL.md`:

~~~~
a de `blocked` → `review` é do **planejador**,
na rodada de replanejamento
~~~~

**Texto novo 12** — `.claude/skills/diario-de-obras/SKILL.md`:

~~~~
a de `blocked` → `review` é do **consultor**, na rota `resolve` da triagem, ou do **planejador**,
na rodada de replanejamento
~~~~

**Texto atual 13** — `.claude/skills/diario-de-obras/SKILL.md`:

~~~~
| `blocked` → `review` | a rodada de replanejamento corrigiu o **aceite**
~~~~

**Texto novo 13** — `.claude/skills/diario-de-obras/SKILL.md`:

~~~~
| `blocked` → `review` | a triagem do consultor (rota `resolve`) ou a rodada de replanejamento corrigiu o **aceite**
~~~~

**Texto atual 14** — `.claude/skills/passagem-de-bastao/SKILL.md`:

~~~~
`premissa` e rodada de replanejamento como próxima tarefa (`G-NOASK`, `GOVERNANCA.md` §7 item 18).
~~~~

**Texto novo 14** — `.claude/skills/passagem-de-bastao/SKILL.md`:

~~~~
`premissa` e triagem do consultor, que devolve a rota (`G-NOASK`, `GOVERNANCA.md` §7 item 18).
~~~~

**Texto atual 15** — `.claude/skills/passagem-de-bastao/SKILL.md`:

~~~~
- **Bloqueio por premissa abre rodada, não pula tarefa** (`G-REPLAN`, `GOVERNANCA.md` §7 item 17):
  tarefa `blocked` com razão `premissa` no plano priorizado torna a **rodada de replanejamento** a
  próxima tarefa — delegada ao `pantonic-planner`, com o achado do corpo da tarefa como dossiê, nunca
  ao executor; a tarefa seguinte do mesmo plano não é despachada enquanto a rodada não fechar. Só o
  que o planejador classificar como estratégico chega ao dono.
~~~~

**Texto novo 15** — `.claude/skills/passagem-de-bastao/SKILL.md`:

~~~~
- **Bloqueio de executor vai à triagem, não pula tarefa** (`G-REPLAN`, `GOVERNANCA.md` §7 item 17): tarefa `blocked` no plano priorizado vai ao `pantonic-consultant`, que devolve a rota; só a rota `planejador` torna a **rodada de replanejamento** a próxima tarefa — delegada ao `pantonic-planner`, com o achado do corpo da tarefa como dossiê, nunca ao executor —, e a tarefa seguinte do mesmo plano não é despachada enquanto a rodada não fechar. Ao dono chega só, no marco, o pedido de validar o drift do modelo, e o estratégico.
~~~~

**Texto atual 16** — `.claude/skills/passagem-de-bastao/SKILL.md`:

~~~~
indício de que o plano precisa mudar vai
  ao planejador (`GOVERNANCA.md` §3, escada de revisão de plano).
~~~~

**Texto novo 16** — `.claude/skills/passagem-de-bastao/SKILL.md`:

~~~~
indício de que o plano precisa mudar vai
  à triagem do consultor (`GOVERNANCA.md` §3, escada de revisão de plano).
~~~~

**Texto atual 17** — `.claude/global/CLAUDE.md`:

~~~~
registra o achado e escala para replanejamento — nunca substitui a arquitetura por uma
~~~~

**Texto novo 17** — `.claude/global/CLAUDE.md`:

~~~~
registra o achado e devolve `blocked` à triagem do plano, que decide a rota — nunca substitui a arquitetura por uma
~~~~

### CON-T6 — A especificação vira lastro medido [Sonnet · esforço medium · classe mecanica]
- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T5`
- **Objetivo:** O redator da especificação a converte em lastro medido: o estatuto dela passa a apontar para a norma e para a definição de conduta, cada lacuna que ela deixava aberta ganha o ponteiro para a regra que a fecha ou para a residência que a recebe, e o índice de documentos deixa de descrevê-la como a única fonte da figura e passa a indexar o cenário e a estatística.
- **Fundamento:** `DCS-2`, `DCS-4`, `DCS-6`..`DCS-10`; fatos `F-4` itens 42 e 43, `F-9`.
- **Operação do modelo:** `OP-6`
  - OP-6: O redator da especificação a converte em lastro medido: o estatuto dela passa a apontar para a norma e para a definição de conduta, cada lacuna que ela deixava aberta ganha o ponteiro para a regra que a fecha ou para a residência que a recebe, e o índice de documentos deixa de descrevê-la como a única fonte da figura e passa a indexar o cenário e a estatística.
  - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`)
- **Camada e fronteira:** documentação — `docs/consultant-spec.md` (estatuto e §10) e `docs/DOC_MAP.md`; sem código.
- **Domínio:** **lacunas** — as sete da §10 da spec (`F-9`), cada uma com o ponteiro para a regra ou residência que a fecha.
- **Arquivos-alvo:**
  - `docs/consultant-spec.md`
  - `docs/DOC_MAP.md`
- **Contratos/classes:** nenhuma assinatura de código.
- **Passos:**
  1. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**.
  2. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 2** pelo bloco **Texto novo 2**.
  3. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 3** pelo bloco **Texto novo 3**.
  4. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 4** pelo bloco **Texto novo 4**.
  5. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 5** pelo bloco **Texto novo 5**.
  6. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 6** pelo bloco **Texto novo 6**.
  7. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 7** pelo bloco **Texto novo 7**.
  8. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 8** pelo bloco **Texto novo 8**.
  9. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 9** pelo bloco **Texto novo 9**.
  10. Em `docs/DOC_MAP.md`, substitua o bloco **Texto atual 10** pelo bloco **Texto novo 10**.
  11. Em `docs/DOC_MAP.md`, substitua o bloco **Texto atual 11** pelo bloco **Texto novo 11**.
  12. Em `docs/DOC_MAP.md`, substitua o bloco **Texto atual 12** pelo bloco **Texto novo 12**.
  13. Em `docs/DOC_MAP.md`, substitua o bloco **Texto atual 13** pelo bloco **Texto novo 13**.
  14. Em `docs/DOC_MAP.md`, substitua o bloco **Texto atual 14** pelo bloco **Texto novo 14**.
- **Restrições desta tarefa:**
  - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação.
  - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`).
  - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`).
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:**
  - Não tocar a §11 da spec (`:422` em diante): é o item 46, da `CON-T7`.
  - Não corrigir as três contagens defasadas da nota de leitura (`:12-30`) nem as tabelas das §§1-9 (`DCS-2`).
- **Contingências:**
  - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco
  - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido
  - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa`
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`; quando o card toca arquivo preso por literal (`F-15`), também `tests/test_doutrina_unidade.py`.
- **Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-22 numa cópia da árvore com os cards anteriores aplicados em ensaio; o executor mede o **antes** antes da primeira edição.
  1. antes `1` · depois `0`

     ~~~~
     (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern 'Promovê-lo a doutrina é').Count
     ~~~~

  2. antes `0` · depois `1`

     ~~~~
     (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern 'Lastro medido, não fonte normativa.').Count
     ~~~~

  3. antes `1` · depois `0`

     ~~~~
     (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern '**sem rota decidida aqui**').Count
     ~~~~

  4. antes `0` · depois `7`

     ~~~~
     (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern '`P-0747` `DCS-').Count
     ~~~~

  5. antes `1` · depois `0`

     ~~~~
     (Select-String -Path 'docs/DOC_MAP.md' -SimpleMatch -CaseSensitive -Pattern '**Não é doutrina**').Count
     ~~~~

  6. antes `0` · depois `1`

     ~~~~
     (Select-String -Path 'docs/DOC_MAP.md' -SimpleMatch -CaseSensitive -Pattern '## docs/ACIONAMENTOS_CONSULTOR.tsv').Count
     ~~~~

  7. antes `0` · depois `1`

     ~~~~
     (Select-String -Path 'docs/DOC_MAP.md' -SimpleMatch -CaseSensitive -Pattern '## docs/plans/_CENARIO-<plano>.md').Count
     ~~~~

  8. antes `1` · depois `0`

     ~~~~
     (Select-String -Path 'docs/DOC_MAP.md' -SimpleMatch -CaseSensitive -Pattern 'as cinco matérias sem rota decidida').Count
     ~~~~

  9. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes e `277 passed` depois, no ensaio)

     ~~~~
     python -m pytest -q
     ~~~~

- **Pronto quando:**
  - `consultor.estatuto na doutrina` — papel de doutrina em duas residências — a linha na matriz de `GOVERNANCA.md` §3 e a definição de conduta sem estatuto provisório —; a spec permanece como lastro medido e não normativo, com o estatuto apontando para as duas e o índice de documentos dizendo o mesmo — Verificação 1, 2, 5
  - `consultor.lacunas deixadas pela especificação` — as sete fechadas: cinco por norma — handover e forma pelo cenário persistido, estatística pela residência estruturada, autoria de card novo pela fronteira com o planejador, disciplina de saída por regra do agente — e duas por residência nomeada — não-acionamento no `TK-55`, poluição pela regra geral do agente —; cada item da §10 da spec aponta para o que o fecha — Verificação 3, 4, 6, 7, 8
- **Fora do escopo desta tarefa:** o veredito do piloto na §11 (`CON-T7`).

**Texto atual 1** — `docs/consultant-spec.md`:

~~~~
**Estatuto.** Especificação de uma figura **provisória**. Este documento não é doutrina: não altera
`GOVERNANCA.md`, não cria guardrail `G-*` e não se declara fonte normativa. Promovê-lo a doutrina é
ato posterior, e até lá o consultor de plano permanece figura ad-hoc.
~~~~

**Texto novo 1** — `docs/consultant-spec.md`:

~~~~
**Estatuto.** Lastro medido, não fonte normativa. A figura virou papel de doutrina pelo `docs/plans/P-0747-consultor-de-plano.md`: o papel mora na linha *Consultoria* da matriz de `GOVERNANCA.md` §3 e a conduta em `.claude/agents/pantonic-consultant.md`. Este documento registra o comportamento medido que as fundamenta, e as contagens dele não se corrigem.
~~~~

**Texto atual 2** — `docs/consultant-spec.md`:

~~~~
Registrado para que o plano próprio não comece frio, e **sem rota decidida aqui**:
~~~~

**Texto novo 2** — `docs/consultant-spec.md`:

~~~~
Registrado para que o plano próprio não comece frio. O `P-0747` fechou as sete lacunas, uma a uma, e o ponteiro de cada uma segue o bullet:
~~~~

**Texto atual 3** — `docs/consultant-spec.md`:

~~~~
o conteúdo está fixado, a forma é ad-hoc.
~~~~

**Texto novo 3** — `docs/consultant-spec.md`:

~~~~
o conteúdo está fixado, a forma é ad-hoc. → fechado: o cenário persistido é o handover (`.claude/skills/scrum-master/SKILL.md`, seção *Acionamento do consultor*; `P-0747` `DCS-6`).
~~~~

**Texto atual 4** — `docs/consultant-spec.md`:

~~~~
  a estrutura, não.
~~~~

**Texto novo 4** — `docs/consultant-spec.md`:

~~~~
  a estrutura, não. → fechado: `docs/ACIONAMENTOS_CONSULTOR.tsv`, uma linha por acionamento (`P-0747` `DCS-8`).
~~~~

**Texto atual 5** — `docs/consultant-spec.md`:

~~~~
  continua sem regra que o autorize ou o proíba.
~~~~

**Texto novo 5** — `docs/consultant-spec.md`:

~~~~
  continua sem regra que o autorize ou o proíba. → fechado: o card corretivo `T<n>a` da mesma operação é do consultor, e operação nova vai ao modelador (`GOVERNANCA.md` §3, linha *Consultoria*; `P-0747` `DCS-4`).
~~~~

**Texto atual 6** — `docs/consultant-spec.md`:

~~~~
  saída; nenhum critério de entrada foi exercido.
~~~~

**Texto novo 6** — `docs/consultant-spec.md`:

~~~~
  saída; nenhum critério de entrada foi exercido. → residência nomeada: `TK-55`, decidido sobre a estatística de `docs/ACIONAMENTOS_CONSULTOR.tsv` (`P-0747` `DCS-10`).
~~~~

**Texto atual 7** — `docs/consultant-spec.md`:

~~~~
  exercitado.
~~~~

**Texto novo 7** — `docs/consultant-spec.md`:

~~~~
  exercitado. → residência nomeada: a regra geral, na seção *Coesão do seu contexto* de `.claude/agents/pantonic-consultant.md` (`P-0747` `DCS-10`).
~~~~

**Texto atual 8** — `docs/consultant-spec.md`:

~~~~
  decide a forma **por piloto medido**, não por argumento.
~~~~

**Texto novo 8** — `docs/consultant-spec.md`:

~~~~
  decide a forma **por piloto medido**, não por argumento. → fechado: efêmera com cenário persistido, em piloto medido na §11 (`P-0747` `DCS-6`, `DCS-7`).
~~~~

**Texto atual 9** — `docs/consultant-spec.md`:

~~~~
  hoje é recomendação, não regra.
~~~~

**Texto novo 9** — `docs/consultant-spec.md`:

~~~~
  hoje é recomendação, não regra. → fechado: regra do agente, item 4 de *O que você faz* (`P-0747` `DCS-9`).
~~~~

**Texto atual 10** — `docs/DOC_MAP.md`:

~~~~
## docs/consultant-spec.md (~339 linhas)
~~~~

**Texto novo 10** — `docs/DOC_MAP.md`:

~~~~
## docs/consultant-spec.md (~480 linhas)
~~~~

**Texto atual 11** — `docs/DOC_MAP.md`:

~~~~
**Propósito:** especificação da figura **provisória** do consultor de plano (`pantonic-consultant`)
~~~~

**Texto novo 11** — `docs/DOC_MAP.md`:

~~~~
**Propósito:** especificação da figura do consultor de plano (`pantonic-consultant`)
~~~~

**Texto atual 12** — `docs/DOC_MAP.md`:

~~~~
do próprio acionamento. **Não é doutrina** e não se cita como fonte normativa.
~~~~

**Texto novo 12** — `docs/DOC_MAP.md`:

~~~~
do próprio acionamento. É **lastro medido**: a doutrina do papel mora em `GOVERNANCA.md` §3 (linha *Consultoria*) e em `.claude/agents/pantonic-consultant.md`.
~~~~

**Texto atual 13** — `docs/DOC_MAP.md`:

~~~~
- `## 10. O que esta especificação não fecha` — as cinco matérias sem rota decidida
~~~~

**Texto novo 13** — `docs/DOC_MAP.md`:

~~~~
- `## 10. O que esta especificação não fecha` — as sete lacunas, cada uma com o ponteiro para o que a fechou no `P-0747`
- `## 11. (i) Custo por acionamento — a medida que reabre a forma da figura` — custo medido por acionamento e o veredito do piloto da forma efêmera
~~~~

**Texto atual 14** — `docs/DOC_MAP.md`:

~~~~
desejada; as perguntas (a)..(h) mapeiam nas seções 2..9).
~~~~

**Texto novo 14** — `docs/DOC_MAP.md`:

~~~~
desejada; as perguntas (a)..(h) mapeiam nas seções 2..9).

## docs/ACIONAMENTOS_CONSULTOR.tsv
**Propósito:** estatística do acionamento do consultor — uma linha por acionamento, apensada pelo `pantonic-consultant`, com as colunas `data`, `plano`, `acionamento`, `tarefa`, `gatilho`, `motivo`, `classe_impedimento`, `rota`, `inconclusivo`. Consumidor: `TK-55` (spec de robustez).
**Quando consultar:** para o panorama dos pontos inconclusivos e das rotas devolvidas; o custo do acionamento mora em `docs/telemetria.tsv`.
**Acesso:** `Grep pattern:"<plano>" path:docs/ACIONAMENTOS_CONSULTOR.tsv`.

## docs/plans/_CENARIO-<plano>.md
**Propósito:** cenário persistido do consultor efêmero de um plano em execução — decisões vivas, fila, achados abertos, matéria inconclusiva, no máximo 15k tokens; autoridade sobre o plano para o que cobre. Escrito só pelo `pantonic-consultant`.
**Quando consultar:** ao acionar o consultor; nunca como substituto do plano fora do acionamento.
**Acesso:** Read integral (teto de 15k tokens).
~~~~

### CON-T5a — Corretivo da OP-5: o diário e a Regra 8 dizem o que a triagem diz [Sonnet · esforço medium · classe mecanica]
- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T6`
- **Objetivo:** Corretivo da `CON-T5` (`AE-14`, `DCS-31`): (i) o parágrafo da skill `diario-de-obras` que ainda leva o **plano** a `blocked` e abre rodada de replanejamento em toda revisão pedida por quem executa (`F-4` item 49) passa a dizer o que a skill do loop e `G-REPLAN` dizem — a tarefa vai a `blocked premissa`, a parada vai à triagem do consultor, e só a rota `planejador` leva o plano a `blocked` e abre a rodada; (ii) a Regra 8 de `.claude/global/CLAUDE.md` (item 38) deixa de usar "rota" para o que a triagem decide — a triagem decide o *destino da parada*; "rota aprovada" fica com o sentido do plano, que é do dono.
- **Fundamento:** `DCS-3`, `DCS-4`, `DCS-31`; achado `AE-14`; laudo da `CON-T5` (aprovado 100, `seguir`).
- **Operação do modelo:** `OP-5`
  - OP-5: O autor de papéis escreve o outro lado da fronteira em toda definição de conduta que ainda manda a parada direto ao replanejamento: quem planeja passa a receber a rodada pela rota da triagem, quem escreve o modelo passa a nomear o consultor como origem da emenda e como quem estende a lista de tarefas, quem executa e quem revisa passam a devolver a parada e a pendência à triagem, e a regra de transição de estado do diário, a passagem de bastão e a regra global de não decidir passam a dizer o mesmo.
  - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`); planejador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 13, 19, 20 e 25 — é a fronteira do consultor e nada além: a rodada de replanejamento chega pela rota `planejador` da triagem, só quando emenda aceita cria ou remove operação ou quando a premissa cai inteira (`superseded`), e o corretivo `T<n>a` da mesma operação, com o id apensado à lista `tarefas:`, passa a ser também ato do consultor (`DCS-4`). O que `DCS-18` deixa com o planejamento continua com ele. Alterar outra conduta do planejador é colateral e se escala; modelador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 26, 27 e 28 — é a fronteira do consultor e nada além: o consultor é nomeado como quem origina o dossiê de `emenda` e como quem apensa o id do corretivo à lista `tarefas:`; quem despacha continua sendo quem conduz a sessão (`I-2`). Os literais que a guarda executável prende no arquivo dele (`F-15`) ficam. O instrumento do modelo e seus testes não se tocam; parada de executor — nenhuma operação altera uma parada. O que se observa nela, antes e depois, é o caminho: quem a recebe, quem decide a rota e onde isso fica registrado. As paradas do `P-0745` e do `P-0746` (`F-8`) são o retrato do antes; o depois são as paradas da janela de execução deste plano, lidas no arquivo de estatística de `DCS-8` a partir do aceite da `OP-2`
- **Camada e fronteira:** procedimento (skill `diario-de-obras`, só o parágrafo `:79-83`, item 49) e regra global do kit (`.claude/global/CLAUDE.md`, só a linha `:164` da Regra 8, item 38); sem código.
- **Domínio:** **revisão pedida por quem executa** — no diário, a tarefa vai a `blocked premissa`, a parada vai à triagem, e só a rota `planejador` leva o plano a `blocked` e abre a rodada (`G-REPLAN`, `GOVERNANCA.md` §7 item 17); nas rotas `resolve` e `modelador` o plano segue. **Homonímia** — na Regra 8, "rota aprovada" é do plano e a triagem decide o *destino da parada*; a palavra "rota" não nomeia a triagem no mesmo período. Invariantes: o item 33 (`:89` e `:102`), já reescrito pela `CON-T5`, não muda (linha 4 da `Verificação`); o literal `devolve `blocked` à triagem do plano` da `CON-T5` (Verificação 20 dela) permanece (linha 8).
- **Arquivos-alvo:**
  - `.claude/skills/diario-de-obras/SKILL.md`
  - `.claude/global/CLAUDE.md`
- **Contratos/classes:** nenhuma assinatura de código; nenhuma linha de tabela muda.
- **Passos:**
  1. Em `.claude/skills/diario-de-obras/SKILL.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**.
  2. Em `.claude/global/CLAUDE.md`, substitua o bloco **Texto atual 2** pelo bloco **Texto novo 2**.
- **Restrições desta tarefa:**
  - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação.
  - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`).
  - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`).
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:**
  - Não tocar `.claude/skills/diario-de-obras/SKILL.md:89` nem `:102` (item 33, `CON-T5`) nem a tabela *Máquina de transições*; a linha 4 da `Verificação` mede isso.
  - Não tocar `.claude/global/CLAUDE.md:162` (caso de `DCS-18`) e não propagar a Regra 8 para `~/.claude/CLAUDE.md` nem para projetos derivados (`DCS-13`).
  - Não reescrever o literal `materialização de uma operação do modelo` da skill do diário nem introduzir `tarefa atômica` em `.claude/global/CLAUDE.md` (`tests/test_doutrina_unidade.py`); as linhas 5 e 9 medem isso.
- **Contingências:**
  - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco
  - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido
  - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa`
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`, e, porque os dois arquivos são presos por literal (`F-15`), `tests/test_doutrina_unidade.py`.
- **Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-23 pelo consultor (acionamento 6) na árvore real, com os blocos aplicados e revertidos por cópia, **como está depois da `CON-T6`**; o executor mede o **antes** antes da primeira edição.
  1. antes `1` · depois `0`

     ~~~~
     (Select-String -Path '.claude/skills/diario-de-obras/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'orquestra é caso de `blocked` **de plano**').Count
     ~~~~

  2. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/diario-de-obras/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'Só a rota `planejador` é caso de `blocked` **de plano**').Count
     ~~~~

  3. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/diario-de-obras/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'Nas rotas `resolve` e `modelador` o plano segue').Count
     ~~~~

  4. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/diario-de-obras/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'é do **consultor**, na rota `resolve` da triagem').Count
     ~~~~

  5. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/diario-de-obras/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'materialização de uma operação do modelo').Count
     ~~~~

  6. antes `1` · depois `0`

     ~~~~
     (Select-String -Path '.claude/global/CLAUDE.md' -SimpleMatch -CaseSensitive -Pattern 'que decide a rota — nunca substitui').Count
     ~~~~

  7. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/global/CLAUDE.md' -SimpleMatch -CaseSensitive -Pattern 'que decide o destino da parada').Count
     ~~~~

  8. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/global/CLAUDE.md' -SimpleMatch -CaseSensitive -Pattern 'devolve `blocked` à triagem do plano').Count
     ~~~~

  9. `8 passed` antes · `8 passed` depois

     ~~~~
     python -m pytest -q tests/test_doutrina_unidade.py
     ~~~~

  10. antes `0` · depois `0`

     ~~~~
     python .claude/tools/backlog.py check; $LASTEXITCODE
     ~~~~

  11. antes `0` · depois `0`

     ~~~~
     python .claude/tools/modelo.py check --plano docs/plans/P-0747-consultor-de-plano.md; $LASTEXITCODE
     ~~~~

  12. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes — laudo da `CON-T6`, mesma árvore — e `277 passed` depois, no ensaio de 2026-09-23 do acionamento 6)

     ~~~~
     python -m pytest -q
     ~~~~
- **Pronto quando:**
  - `consultor.alcance da triagem das paradas` — fatia da `OP-5` (`F-4` itens 38 e 49): a revisão pedida por quem executa leva a tarefa a `blocked premissa` e a parada à triagem, e só a rota `planejador` leva o plano a `blocked` e abre a rodada; a Regra 8 devolve a parada à triagem sem chamar de "rota" o que a triagem decide — Verificação 1, 2, 3, 6, 7
- **Fora do escopo desta tarefa:** o item 33 e os demais itens 25 a 37 da `F-4` (`CON-T5`, fechada); a spec (`CON-T6a`, `OP-6`); a versão 2 pendente da `## 1A`, que recebe os itens 49 e 50 pelo dossiê de conflito de `DCS-31` (modelador).

**Texto atual 1** — `.claude/skills/diario-de-obras/SKILL.md`:

~~~~
Plano cuja revisão foi pedida por quem executa ou orquestra é caso de `blocked` **de plano**, com a
razão registrada; na **tarefa** correspondente, a razão tipada é `premissa`. Esse `blocked` de plano
abre uma **rodada de replanejamento** como próxima tarefa do plano (`G-REPLAN`, `GOVERNANCA.md` §7
item 17): o plano só sai de `blocked` quando a rodada fecha — a tarefa volta a `ready` ou
`cancelled`, e a entrada `RP-<n>` fica em `## Achados da execução` do plano.
~~~~

**Texto novo 1** — `.claude/skills/diario-de-obras/SKILL.md`:

~~~~
Plano cuja revisão foi pedida por quem executa ou orquestra não vai a `blocked` por isso: a **tarefa**
vai a `blocked` com a razão tipada `premissa`, e a parada vai à triagem do consultor, que devolve a
rota (`G-REPLAN`, `GOVERNANCA.md` §7 item 17). Só a rota `planejador` é caso de `blocked` **de plano**,
com a razão registrada, e abre uma **rodada de replanejamento** como próxima tarefa do plano: o plano
só sai de `blocked` quando a rodada fecha — a tarefa volta a `ready` ou `cancelled`, e a entrada
`RP-<n>` fica em `## Achados da execução` do plano. Nas rotas `resolve` e `modelador` o plano segue.
~~~~

**Texto atual 2** — `.claude/global/CLAUDE.md`:

~~~~
registra o achado e devolve `blocked` à triagem do plano, que decide a rota — nunca substitui a arquitetura por uma
~~~~

**Texto novo 2** — `.claude/global/CLAUDE.md`:

~~~~
registra o achado e devolve `blocked` à triagem do plano, que decide o destino da parada — nunca substitui a arquitetura por uma
~~~~

### CON-T6a — Corretivo da OP-6: a spec não prevalece sobre o bloco A [Sonnet · esforço medium · classe mecanica]
- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T5a`
- **Objetivo:** Corretivo da `CON-T6` (`AE-15`, `DCS-31`): o parágrafo *Consequência sobre a §2* da subseção *Ato do dono de 2026-09-22* (§3 da spec, `F-4` item 50) deixa de afirmar que a spec prevalece enquanto o bloco A não for reescrito — o bloco A foi reescrito pela `CON-T3` e pelos corretivos `CON-T3a`..`CON-T3c` — e vira registro histórico datado, apontando para a skill do loop e para `G-REPLAN`, onde a regra mora hoje.
- **Fundamento:** `DCS-4`, `DCS-31`; achado `AE-15`; laudo da `CON-T6` (aprovado 100, `seguir`).
- **Operação do modelo:** `OP-6`
  - OP-6: O redator da especificação a converte em lastro medido: o estatuto dela passa a apontar para a norma e para a definição de conduta, cada lacuna que ela deixava aberta ganha o ponteiro para a regra que a fecha ou para a residência que a recebe, e o índice de documentos deixa de descrevê-la como a única fonte da figura e passa a indexar o cenário e a estatística.
  - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`)
- **Camada e fronteira:** documento de lastro (`docs/consultant-spec.md`, só o parágrafo `:167-169`, item 50); sem código. `docs/DOC_MAP.md` não muda: a entrada da spec diz *"~480 linhas"* e o arquivo vai de 477 a 479 linhas.
- **Domínio:** **precedência da spec** — nenhuma: a spec é lastro medido, não fonte normativa (estatuto, `:3-5`); a frase que afirmava precedência sobre o bloco A é datada e apontada para onde a regra mora. Invariante: as quatro diretivas `DC-1`..`DC-4`, o parágrafo *Por que a lacuna existia* e os dois blocos de *Lastro* não mudam.
- **Arquivos-alvo:**
  - `docs/consultant-spec.md`
- **Contratos/classes:** nenhuma assinatura de código; nenhuma linha de tabela muda.
- **Passos:**
  1. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**.
- **Restrições desta tarefa:**
  - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação.
  - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`).
  - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`).
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:**
  - Não tocar `DC-1`..`DC-4`, o parágrafo *Por que a lacuna existia* nem os blocos de *Lastro* da subseção.
  - Não corrigir as três contagens defasadas da spec (`DCS-2`) e não tocar a §11 (item 46, `CON-T7`).
  - Não tocar `docs/DOC_MAP.md` (item 43, `CON-T6`, fechada).
- **Contingências:**
  - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco
  - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido
  - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa`
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita lastro e não código. A guarda é a suíte inteira, `python -m pytest -q`.
- **Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-23 pelo consultor (acionamento 6) na árvore real, com o bloco aplicado e revertido por cópia, **como está depois da `CON-T6`**; o executor mede o **antes** antes da primeira edição.
  1. antes `1` · depois `0`

     ~~~~
     (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern 'Enquanto o bloco A não for').Count
     ~~~~

  2. antes `1` · depois `0`

     ~~~~
     (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern '**a spec prevalece**').Count
     ~~~~

  3. antes `0` · depois `1`

     ~~~~
     (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern 'a spec prevaleceu por precedência do dono').Count
     ~~~~

  4. antes `0` · depois `1`

     ~~~~
     (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern 'Registro histórico: o bloco A foi reescrito pela').Count
     ~~~~

  5. antes `1` · depois `1`

     ~~~~
     (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern 'Lastro medido, não fonte normativa').Count
     ~~~~

  6. antes `0` · depois `0`

     ~~~~
     python .claude/tools/backlog.py check; $LASTEXITCODE
     ~~~~

  7. antes `0` · depois `0`

     ~~~~
     python .claude/tools/modelo.py check --plano docs/plans/P-0747-consultor-de-plano.md; $LASTEXITCODE
     ~~~~

  8. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes — laudo da `CON-T6`, mesma árvore — e `277 passed` depois, no ensaio de 2026-09-23 do acionamento 6)

     ~~~~
     python -m pytest -q
     ~~~~
- **Pronto quando:**
  - `consultor.estatuto na doutrina` — fatia da `OP-6` (`F-4` item 50): a spec permanece lastro medido e não normativo, e nenhum parágrafo dela afirma prevalecer sobre a norma — Verificação 1 a 5
- **Fora do escopo desta tarefa:** a §11 da spec (item 46, `CON-T7`); o índice de documentos (item 43, `CON-T6`); o diário e a Regra 8 (`CON-T5a`, `OP-5`).

**Texto atual 1** — `docs/consultant-spec.md`:

~~~~
**Consequência sobre a §2.** A classe 1 de gatilho já dizia que card devolvido `blocked` aciona a
figura. A `A3b` da skill dizia o contrário para o motivo `premissa`. Enquanto o bloco A não for
reescrito, **a spec prevalece**: toda parada de executor aciona a figura.
~~~~

**Texto novo 1** — `docs/consultant-spec.md`:

~~~~
**Consequência sobre a §2.** A classe 1 de gatilho já dizia que card devolvido `blocked` aciona a
figura. A `A3b` da skill dizia o contrário para o motivo `premissa`. Enquanto o bloco A não foi
reescrito, a spec prevaleceu por precedência do dono. Registro histórico: o bloco A foi reescrito pela
`CON-T3` do `P-0747` (2026-09-23; corretivos `CON-T3a`..`CON-T3c`), a regra mora hoje na skill
`scrum-master` e em `G-REPLAN` (`GOVERNANCA.md` §7 item 17), e a spec não prevalece (estatuto, `:3-5`).
~~~~

### CON-T7 — A medida do piloto da forma efêmera [Sonnet · esforço high · classe investigacao]
- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T6a`
- **Objetivo:** O medidor confronta o piloto da forma efêmera com a forma anterior: apura o custo de cada acionamento da janela pelo método já medido, conta as reprovações por perda de cenário e grava, na seção de custo da especificação, o veredito de adotar, recusar ou declarar a amostra insuficiente.
- **Fundamento:** `DCS-7`, `DCS-22`; fatos `F-7`, `F-4` item 46; spec §11 (i) e (ii).
- **Operação do modelo:** `OP-7`
  - OP-7: O medidor confronta o piloto da forma efêmera com a forma anterior: apura o custo de cada acionamento da janela pelo método já medido, conta as reprovações por perda de cenário e grava, na seção de custo da especificação, o veredito de adotar, recusar ou declarar a amostra insuficiente.
  - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`); acionamento do consultor — nenhuma operação altera um acionamento. O que se observa nele é o custo, apurado pelo método de `F-7`; a sonda é descartável e não vira artefato. Retrato do antes: as instâncias 1-4 da forma standby (`F-7`) e a série de `F-8`; o depois: os acionamentos da janela de execução deste plano a partir do aceite da `OP-4`
- **Camada e fronteira:** medição — leitura de transcripts fora do repositório e de `docs/telemetria.tsv`; escrita só no fim da §11 de `docs/consultant-spec.md`.
- **Domínio:** **acionamento** — uma instância efêmera do `pantonic-consultant` despachada com o caminho `docs/plans/_CENARIO-P-0747.md` na mensagem de entrada; **reprovação** — revisão repetida de uma mesma tarefa (`DCS-22`).
- **Arquivos-alvo:**
  - `docs/consultant-spec.md`
- **Contratos/classes:** nenhuma assinatura de código; a sonda é descartável e fica em `%TEMP%\claude\`.
- **Método de sondagem:**
  1. Grave o bloco **Sonda** abaixo em `%TEMP%\claude\sonda_p0747.py` e rode `python $env:TEMP\claude\sonda_p0747.py`. A sonda lê só os transcripts `~/.claude/projects/d--workspaces-PantonicApp/*/subagents/agent-*.jsonl` cujo `agent-*.meta.json` tem `agentType` igual a `pantonic-consultant` e cuja primeira linha cita `_CENARIO-P-0747.md`; cada arquivo é um acionamento. Saída: `acionamentos=<n>` e, com `n` > 0, `media=$<x> min=$<a> max=$<b>`. Medido em 2026-09-22 antes da janela: `acionamentos=0`.
  2. Grave o bloco **Contagem** abaixo em `%TEMP%\claude\retentativas_p0747.py` e rode `python $env:TEMP\claude\retentativas_p0747.py` na raiz do repositório. Saída: `retentativas=<r> reprovacoes=<p> tarefas=<t>`. Medido em 2026-09-22 antes da janela: `retentativas=0 reprovacoes=0 tarefas=0`.
  3. Tome o veredito da `Contingências` deste card que casa os valores medidos: as quatro linhas cobrem todos os valores possíveis.
  4. Apense ao fim de `docs/consultant-spec.md`, depois da última linha, uma linha em branco e o bloco **Subseção** abaixo, trocando `<acionamentos>`, `<media>`, `<min>`, `<max>`, `<reprovacoes>`, `<retentativas>` e `<veredito>` pelos valores medidos (custo com uma casa decimal e vírgula, como `$1,3`; com menos de 1 acionamento, `<media>` vira `—` e `<min>–<max>` vira `—`) e `<frase>` pela frase do veredito no bloco **Frases**.
  - **Agregado que volta** (≤ 4 linhas, na linha de retorno): as duas linhas de saída das sondas, o veredito e, quando acionada, a linha `contingência recusa acionada: veredito recusada`. Nenhum dado bruto de transcript entra no contexto nem no retorno.
- **Restrições desta tarefa:**
  - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação.
  - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`).
  - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`).
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:**
  - Não versionar a sonda nem nenhum arquivo em `.claude/tools/`.
  - Não editar a §11 fora do fim do arquivo, nem as §§1-10.
- **Contingências:**
  - se a sonda imprimir `acionamentos=0`, `acionamentos=1` ou `acionamentos=2` → seguir com o veredito `amostra insuficiente` e a coluna de custo com `—`
  - se `acionamentos` for 3 ou mais, a média ficar abaixo de `$3.7` e `reprovacoes=0` → seguir com o veredito `adotada`
  - se `acionamentos` for 3 ou mais e a média for `$3.7` ou mais, ou `reprovacoes` for maior que 0 → seguir com o veredito `recusada`, e devolver na linha de retorno `contingência recusa acionada: veredito recusada` para a orquestração registrar o `AE-<n>` com rota "plano novo: standby + ping, spec §11 (ii)"
  - se o diretório `~/.claude/projects/d--workspaces-PantonicApp` não existir → parar e sinalizar `blocked` razão `premissa`
- **Testes:** nenhum — tarefa de medição; as sondas são descartáveis e não se versionam.
- **Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-22 numa cópia da árvore com os cards anteriores aplicados em ensaio; o executor mede o **antes** antes da primeira edição.
  1. antes `0` · depois `1`

     ~~~~
     (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern '### Veredito do piloto da forma efêmera').Count
     ~~~~

  2. antes `0` · depois `1`

     ~~~~
     (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern '| acionamentos | $/acionamento, média |').Count
     ~~~~

  3. A linha de agregado devolvida traz `acionamentos=`, `retentativas=` e o veredito, e a linha de tabela da subseção tem os mesmos números.
- **Pronto quando:**
  - `consultor.forma da figura` — efêmera com cenário persistido, instalada pela seção `## Acionamento do consultor` da skill do loop: o cenário do plano, com teto de 15k tokens, é o handover, e o reprovisionamento por limite deixa de existir; o corpo do agente e a regra do loop deixam de descrevê-lo instanciado uma vez (`F-4` itens 44 e 45); ao fim do plano a forma leva o veredito medido do piloto, gravado na §11 da spec (item 46) — adotada; ou recusada, com achado em `## 9` e rota para plano novo de standby com aquecimento; ou em amostra insuficiente, com linha nova na §11 da spec e o piloto seguindo na próxima execução — Verificação 1, 2, 3
- **Fora do escopo desta tarefa:** a descrição pública da forma (`CON-T8`).

**Sonda** — `%TEMP%\claude\sonda_p0747.py`:

~~~~
import glob, json, os, sys
FILTRO = sys.argv[1] if len(sys.argv) > 1 else "_CENARIO-P-0747.md"
BASE = os.path.expanduser(r"~/.claude/projects/d--workspaces-PantonicApp")
custos = []
for meta in glob.glob(os.path.join(BASE, "*", "subagents", "agent-*.meta.json")):
    if json.load(open(meta, encoding="utf-8")).get("agentType") != "pantonic-consultant":
        continue
    jl = meta[: -len(".meta.json")] + ".jsonl"
    linhas = open(jl, encoding="utf-8").read().splitlines()
    if not linhas or FILTRO not in linhas[0]:
        continue
    uso = {}
    for l in linhas:
        e = json.loads(l)
        m = e.get("message") or {}
        if e.get("type") == "assistant" and m.get("id") and m.get("usage"):
            uso[m["id"]] = m["usage"]
    s = lambda k: sum(u.get(k, 0) or 0 for u in uso.values())
    custo = (s("input_tokens") * 5 + s("output_tokens") * 25 + s("cache_read_input_tokens") * 0.5
             + s("cache_creation_input_tokens") * 6.25) / 1e6
    custos.append(custo)
n = len(custos)
print(f"acionamentos={n}")
if n:
    print(f"media=${sum(custos)/n:.1f} min=${min(custos):.1f} max=${max(custos):.1f}")
~~~~

**Contagem** — `%TEMP%\claude\retentativas_p0747.py`:

~~~~
import csv, re, collections
exe, rev = collections.Counter(), collections.Counter()
for r in csv.DictReader(open("docs/telemetria.tsv", encoding="utf-8"), delimiter="\t"):
    t = r["tarefa"]
    if re.fullmatch(r"CON-T[56][a-z]?", t): exe[t] += 1
    m = re.fullmatch(r"(CON-T[56][a-z]?)-revisao", t)
    if m: rev[m.group(1)] += 1
print(f"retentativas={sum(max(v-1,0) for v in exe.values())} reprovacoes={sum(max(v-1,0) for v in rev.values())} tarefas={len(exe)}")
~~~~

**Subseção** — apensada ao fim de `docs/consultant-spec.md`:

~~~~
### Veredito do piloto da forma efêmera (`P-0747`, `CON-T7`)

Janela medida: do aceite da `CON-T4` ao despacho da `CON-T7`. Método da própria §11: transcripts do `pantonic-consultant` cuja mensagem de entrada cita `_CENARIO-P-0747.md`, deduplicados por `message.id`; Opus a $5/M de entrada, $25/M de saída, cache read a 10% e cache write a 125%. Reprovações e retentativas contam todas as revisões e execuções repetidas das tarefas `CON-T5` e `CON-T6` e dos seus corretivos (`DCS-22`).

| acionamentos | $/acionamento, média | $/acionamento, mín–máx | reprovações | retentativas | veredito |
|---|---|---|---|---|---|
| <acionamentos> | <media> | <min>–<max> | <reprovacoes> | <retentativas> | <veredito> |

<frase>
~~~~

**Frases** — uma, pelo veredito:

- `adotada`: A forma efêmera fica adotada: a média ficou abaixo de $3,7, o piso medido da forma standby, com zero reprovações.
- `recusada`: A forma efêmera fica recusada pela regra do `DCS-7`: a reversão ao standby com aquecimento (item (ii) desta seção) é matéria de plano novo, e a forma efêmera segue instalada até ele.
- `amostra insuficiente`: Amostra insuficiente (menos de 3 acionamentos): o piloto segue na próxima execução de plano, e o veredito fica devido a ela.

### CON-T7a — Corretivo da OP-7: o veredito declara o modelo das instâncias [Sonnet · esforço low · classe mecanica]
- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T7`
- **Objetivo:** Corretivo da `CON-T7` (`AE-19`, `DCS-32`): a subseção *Veredito do piloto da forma efêmera* da §11 da spec (`F-4` item 46) passa a declarar o modelo em que as três instâncias medidas rodaram (`claude-fable-5-1`, ato do dono `DCS-23`), que a coluna de custo é contagem de tokens precificada pela tabela Opus nos dois lados — preço-Opus-equivalente, não custo real — e que a sonda se reexecuta na primeira execução de plano com o consultor em Opus. O veredito `adotada`, a tabela e a frase do veredito não mudam.
- **Fundamento:** `DCS-4`, `DCS-7`, `DCS-23`, `DCS-32`; achado `AE-19`; laudo da `CON-T7` (aprovado 100, `escalar`).
- **Operação do modelo:** `OP-7`
  - OP-7: O medidor confronta o piloto da forma efêmera com a forma anterior: apura o custo de cada acionamento da janela pelo método já medido, conta as reprovações por perda de cenário e grava, na seção de custo da especificação, o veredito de adotar, recusar ou declarar a amostra insuficiente.
  - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`); acionamento do consultor — nenhuma operação altera um acionamento. O que se observa nele é o custo, apurado pelo método de `F-7`; a sonda é descartável e não vira artefato. Retrato do antes: as instâncias 1-4 da forma standby (`F-7`) e a série de `F-8`; o depois: os acionamentos da janela de execução deste plano a partir do aceite da `OP-4`
- **Camada e fronteira:** documento de lastro (`docs/consultant-spec.md`, só o fim da subseção do veredito, item 46); sem código. `docs/DOC_MAP.md` não muda: a entrada da spec diz *"~480 linhas"* e o arquivo vai de 489 a 491 linhas.
- **Domínio:** **preço-Opus-equivalente** — custo obtido precificando os tokens medidos de uma instância pela tabela Opus da §11, qualquer que seja o modelo em que ela rodou; é a unidade da comparação entre formas, não o custo real da instância. Invariante: a tabela da subseção e a frase do veredito não mudam — a `CON-T8` lê a última linha da tabela.
- **Arquivos-alvo:**
  - `docs/consultant-spec.md`
- **Contratos/classes:** nenhuma assinatura de código; nenhuma linha de tabela muda.
- **Passos:**
  1. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**. O arquivo termina em CRLF: a substituição literal preserva o final de linha do arquivo, e o parágrafo novo entra com o mesmo final de linha.
- **Restrições desta tarefa:**
  - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação.
  - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`).
  - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`).
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:**
  - Não tocar a tabela da subseção nem a frase do veredito; as linhas 3 e 4 da `Verificação` medem isso.
  - Não editar a §11 fora do fim do arquivo, nem as §§1-10.
  - Não corrigir as três contagens defasadas da spec (`DCS-2`) e não tocar `docs/DOC_MAP.md` (item 43, `CON-T6`, fechada).
- **Contingências:**
  - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco
  - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido
  - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa`
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita lastro e não código. A guarda é a suíte inteira, `python -m pytest -q`.
- **Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-23 pelo consultor (acionamento 7) na árvore real, com o bloco aplicado e revertido por cópia, **como está depois da `CON-T7`**; o executor mede o **antes** antes da primeira edição.
  1. antes `0` · depois `1`

     ~~~~
     (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern 'Modelo das instâncias medidas:').Count
     ~~~~

  2. antes `0` · depois `1`

     ~~~~
     (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern 'preço-Opus-equivalente, não custo real').Count
     ~~~~

  3. antes `1` · depois `1`

     ~~~~
     (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern '| 3 | $2,8 | $2,4–$3,0 | 0 | 0 | adotada |').Count
     ~~~~

  4. antes `1` · depois `1`

     ~~~~
     (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern 'A forma efêmera fica adotada: a média ficou abaixo de $3,7, o piso medido da forma standby, com zero reprovações.').Count
     ~~~~

  5. antes `0` · depois `0`

     ~~~~
     python .claude/tools/backlog.py check; $LASTEXITCODE
     ~~~~

  6. antes `0` · depois `0`

     ~~~~
     python .claude/tools/modelo.py check --plano docs/plans/P-0747-consultor-de-plano.md; $LASTEXITCODE
     ~~~~

  7. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes — árvore real, acionamento 7 — e `277 passed` depois, com o bloco aplicado)

     ~~~~
     python -m pytest -q
     ~~~~
- **Pronto quando:**
  - `consultor.forma da figura` — fatia da `OP-7` (`F-4` item 46): o veredito medido do piloto segue gravado na §11 da spec como `adotada`, e a subseção declara o modelo das instâncias e a unidade da comparação — Verificação 1 a 4
- **Fora do escopo desta tarefa:** a descrição pública da forma (`CON-T8`); a tabela e a frase do veredito (`CON-T7`, fechada).

**Texto atual 1** — `docs/consultant-spec.md`:

~~~~
A forma efêmera fica adotada: a média ficou abaixo de $3,7, o piso medido da forma standby, com zero reprovações.
~~~~

**Texto novo 1** — `docs/consultant-spec.md`:

~~~~
A forma efêmera fica adotada: a média ficou abaixo de $3,7, o piso medido da forma standby, com zero reprovações.

Modelo das instâncias medidas: as três rodaram `claude-fable-5-1`, por ato do dono (`P-0747` `DCS-23`); as instâncias 1-4 da tabela desta seção, que dão o piso de $3,7, rodaram Opus. A coluna de custo é contagem de tokens precificada pela tabela Opus nos dois lados — preço-Opus-equivalente, não custo real — e compara a forma da figura (contexto reescrito e relido por acionamento), não o modelo; quanto um modelo distinto consome de tokens para a mesma decisão não foi medido. A sonda recebe o filtro do cenário como argumento e se reexecuta sobre a primeira execução de plano com o consultor em Opus, para conferir o veredito (`P-0747` `DCS-32`, `AE-19`).
~~~~

### CON-T8 — A porta de entrada e a descrição do agente [Sonnet + dono · esforço medium · classe mecanica]
- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T7a`
- **Objetivo:** O mantenedor leva a figura nova à porta de entrada do repositório: a tabela de guardrails deixa de rotear o escalonamento ao planejador, a linha do consultor na tabela de agentes deixa de anunciá-lo instanciado uma vez e mantido de prontidão, e a descrição curta do agente é reescrita no mesmo ato em que o índice gerado do kit é regenerado, os quatro passando a descrever o papel de doutrina, a triagem de toda parada e a forma que o veredito do piloto deixou vigente.
- **Fundamento:** `DCS-15`, `DCS-17`, `DCS-20`; fatos `F-4` itens 39, 40, 41 e 47, `F-5`, `F-16`; G-README dever 2 (a tarefa de revisão do `README.md` que fecha a sprint).
- **Operação do modelo:** `OP-8`
  - OP-8: O mantenedor leva a figura nova à porta de entrada do repositório: a tabela de guardrails deixa de rotear o escalonamento ao planejador, a linha do consultor na tabela de agentes deixa de anunciá-lo instanciado uma vez e mantido de prontidão, e a descrição curta do agente é reescrita no mesmo ato em que o índice gerado do kit é regenerado, os quatro passando a descrever o papel de doutrina, a triagem de toda parada e a forma que o veredito do piloto deixou vigente.
  - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`)
- **Camada e fronteira:** porta de entrada — `README.md`, a `description` do agente e a região gerada `kit:agents` de `.claude/README.md`, esta só por instrumento (`I-4`).
- **Domínio:** **veredito do piloto** — `adotada`, `recusada` ou `amostra insuficiente`, lido na última linha da tabela da subseção *Veredito do piloto da forma efêmera* da §11 de `docs/consultant-spec.md`, gravada pela `CON-T7`.
- **Arquivos-alvo:**
  - `README.md`
  - `.claude/agents/pantonic-consultant.md`
  - `.claude/README.md` (só pelo passo de regeneração)
- **Contratos/classes:** frontmatter YAML do agente: a `description` é uma linha só, sem a sequência dois-pontos-espaço.
- **Passos:**
  1. Em `README.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**.
  2. Em `README.md`, substitua o bloco **Texto atual 2** pelo bloco **Texto novo 2**.
  3. Em `.claude/agents/pantonic-consultant.md`, substitua o bloco **Texto atual 3** pelo bloco **Texto novo 3**.
  4. Rode `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` (exit `0` no ensaio): ele reescreve a região `kit:agents` de `.claude/README.md` a partir da `description` nova.
- **Restrições desta tarefa:**
  - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação.
  - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`).
  - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`).
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:**
  - Não editar `.claude/README.md` à mão: só `kit_check.ps1 -Mode generate` (`I-4`).
  - Não alterar *"O kit são dez agentes"* (`DCS-15`); a linha 4 da `Verificação` mede isso.
  - Não corrigir a duplicação `` `scrum-master`/`scrum-master` `` na coluna da direita da linha 17 da tabela de guardrails: fora do escopo.
- **Contingências:**
  - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco
  - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido
  - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa`
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
  - se a subseção *Veredito do piloto da forma efêmera* não existir na §11 de `docs/consultant-spec.md` → parar e sinalizar `blocked` razão `dependencia`, citando `CON-T7`; se ela existir sem o parágrafo *Modelo das instâncias medidas* → o mesmo, citando `CON-T7a`
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`; quando o card toca arquivo preso por literal (`F-15`), também `tests/test_doutrina_unidade.py`.
- **Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-22 numa cópia da árvore com os cards anteriores aplicados em ensaio; o executor mede o **antes** antes da primeira edição.
  1. antes `1` · depois `0`

     ~~~~
     (Select-String -Path 'README.md' -SimpleMatch -CaseSensitive -Pattern 'roteada ao planejador').Count
     ~~~~

  2. antes `1` · depois `0`

     ~~~~
     (Select-String -Path 'README.md' -SimpleMatch -CaseSensitive -Pattern 'instanciado uma vez, mantido de standby').Count
     ~~~~

  3. antes `0` · depois `1`

     ~~~~
     (Select-String -Path 'README.md' -SimpleMatch -CaseSensitive -Pattern 'Ponto de triagem de **toda** parada de executor').Count
     ~~~~

  4. antes `1` · depois `1`

     ~~~~
     (Select-String -Path 'README.md' -SimpleMatch -CaseSensitive -Pattern 'O kit são dez agentes').Count
     ~~~~

  5. antes `1` · depois `0`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'instanciado UMA vez').Count
     ~~~~

  6. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'description: Consultor de plano Pantonic*, papel de doutrina').Count
     ~~~~

  7. antes `1` · depois `0`

     ~~~~
     (Select-String -Path '.claude/README.md' -SimpleMatch -CaseSensitive -Pattern 'instanciado UMA vez').Count
     ~~~~

  8. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/README.md' -SimpleMatch -CaseSensitive -Pattern 'papel de doutrina (GOVERNANCA.md §3, linha Consultoria)').Count
     ~~~~

  9. antes `0` · com a `description` trocada e a região ainda não regenerada `1` · depois do passo de regeneração `0`

     ~~~~
     (pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift | Select-String -SimpleMatch -Pattern 'README.md diverge do regenerado').Count
     ~~~~

  10. antes `0` · depois `0`

     ~~~~
     pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift; $LASTEXITCODE
     ~~~~

  11. antes `0` · depois `0`

     ~~~~
     pwsh -NoProfile -File .claude/checks/check-readme.ps1; $LASTEXITCODE
     ~~~~

  12. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes e `277 passed` depois, no ensaio)

     ~~~~
     python -m pytest -q
     ~~~~

  13. Veredito do dono sobre o `README.md` revisado (G-README dever 2): `go`, pedido pela orquestração no relatório de encerramento.
- **Pronto quando:**
  - `consultor.descrição pública da figura` — a porta de entrada, a `description` do agente e a região gerada, regenerada no mesmo ato, descrevem o papel de doutrina, a triagem de toda parada e a forma que o veredito do piloto deixou vigente; *"O kit são dez agentes"* fica igual — Verificação 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13
- **Fora do escopo desta tarefa:** nenhuma outra linha do `README.md`.

**Texto atual 1** — `README.md`:

~~~~
bloqueio de tarefa por `premissa` abre uma rodada de replanejamento como próxima tarefa do plano, roteada ao planejador — nunca
~~~~

**Texto novo 1** — `README.md`:

~~~~
parada de executor vai à triagem do consultor, que devolve a rota; só na rota `planejador` a rodada de replanejamento vira a próxima tarefa do plano — nunca
~~~~

**Texto atual 2** — `README.md`:

~~~~
| `pantonic-consultant` | Opus | Consultor de **um** plano em execução: instanciado uma vez, mantido de standby com o cenário inteiro e acionado a cada escalonamento para desbloquear impedimento de executor e reparar o modelo funcional do plano. Não implementa entrega, não julga e não commita. |
~~~~

**Texto novo 2** — `README.md`:

~~~~
| `pantonic-consultant` | Opus | Ponto de triagem de **toda** parada de executor e de todo laudo com pendência substantiva: devolve a rota `resolve`, `modelador` ou `planejador`, fecha sozinho o técnico e o tático e leva ao dono só o drift do modelo. Efêmero, em piloto: cada acionamento é uma instância nova que lê o cenário persistido do plano. Não implementa entrega, não julga e não commita. |
~~~~

**Texto atual 3** — `.claude/agents/pantonic-consultant.md`:

~~~~
description: Consultor de plano Pantonic*, instanciado UMA vez por execução de plano e mantido de standby com o cenário inteiro no contexto. Acionado a cada escalonamento para desbloquear impedimento de executor e reparar o plano, devolvendo ao loop o dossiê Ato de modelo quando a decisão exigir emenda do modelo de domínio - quem escreve no modelo é o pantonic-model-designer. Figura ad-hoc, provisória, criada por decisão do dono em 2026-09-18.
~~~~

**Texto novo 3** — `.claude/agents/pantonic-consultant.md`:

~~~~
description: Consultor de plano Pantonic*, papel de doutrina (GOVERNANCA.md §3, linha Consultoria). Ponto de triagem de toda parada de executor e de todo laudo com pendência substantiva - devolve ao loop a rota resolve, modelador ou planejador, fecha sozinho o técnico e o tático, inclusive o card corretivo da mesma operação, e devolve o dossiê Ato de modelo de emenda quando há drift do modelo - quem escreve no modelo é o pantonic-model-designer. Efêmero, em piloto - cada acionamento é uma instância nova que lê o cenário persistido do plano.
~~~~

**Variantes pelo veredito.** O **Texto novo 2** e o **Texto novo 3** acima estão na variante `amostra insuficiente`. Leia o veredito na última linha da tabela da subseção *Veredito do piloto da forma efêmera* de `docs/consultant-spec.md` e use o par da variante lida — veredito medido pela `CON-T7` em 2026-09-23 e mantido pelo acionamento 7 (`AE-19`, `DCS-32`): `adotada`; o parágrafo que a `CON-T7a` apensa depois da tabela não muda a última linha dela:

- `adotada` — Texto novo 2:

~~~~
| `pantonic-consultant` | Opus | Ponto de triagem de **toda** parada de executor e de todo laudo com pendência substantiva: devolve a rota `resolve`, `modelador` ou `planejador`, fecha sozinho o técnico e o tático e leva ao dono só o drift do modelo. Efêmero: cada acionamento é uma instância nova que lê o cenário persistido do plano. Não implementa entrega, não julga e não commita. |
~~~~

  Texto novo 3:

~~~~
description: Consultor de plano Pantonic*, papel de doutrina (GOVERNANCA.md §3, linha Consultoria). Ponto de triagem de toda parada de executor e de todo laudo com pendência substantiva - devolve ao loop a rota resolve, modelador ou planejador, fecha sozinho o técnico e o tático, inclusive o card corretivo da mesma operação, e devolve o dossiê Ato de modelo de emenda quando há drift do modelo - quem escreve no modelo é o pantonic-model-designer. Efêmero - cada acionamento é uma instância nova que lê o cenário persistido do plano.
~~~~

- `amostra insuficiente` — Texto novo 2:

~~~~
| `pantonic-consultant` | Opus | Ponto de triagem de **toda** parada de executor e de todo laudo com pendência substantiva: devolve a rota `resolve`, `modelador` ou `planejador`, fecha sozinho o técnico e o tático e leva ao dono só o drift do modelo. Efêmero, em piloto: cada acionamento é uma instância nova que lê o cenário persistido do plano. Não implementa entrega, não julga e não commita. |
~~~~

  Texto novo 3:

~~~~
description: Consultor de plano Pantonic*, papel de doutrina (GOVERNANCA.md §3, linha Consultoria). Ponto de triagem de toda parada de executor e de todo laudo com pendência substantiva - devolve ao loop a rota resolve, modelador ou planejador, fecha sozinho o técnico e o tático, inclusive o card corretivo da mesma operação, e devolve o dossiê Ato de modelo de emenda quando há drift do modelo - quem escreve no modelo é o pantonic-model-designer. Efêmero, em piloto - cada acionamento é uma instância nova que lê o cenário persistido do plano.
~~~~

- `recusada` — Texto novo 2:

~~~~
| `pantonic-consultant` | Opus | Ponto de triagem de **toda** parada de executor e de todo laudo com pendência substantiva: devolve a rota `resolve`, `modelador` ou `planejador`, fecha sozinho o técnico e o tático e leva ao dono só o drift do modelo. Efêmero até a execução do plano de reversão ao standby: cada acionamento é uma instância nova que lê o cenário persistido do plano. Não implementa entrega, não julga e não commita. |
~~~~

  Texto novo 3:

~~~~
description: Consultor de plano Pantonic*, papel de doutrina (GOVERNANCA.md §3, linha Consultoria). Ponto de triagem de toda parada de executor e de todo laudo com pendência substantiva - devolve ao loop a rota resolve, modelador ou planejador, fecha sozinho o técnico e o tático, inclusive o card corretivo da mesma operação, e devolve o dossiê Ato de modelo de emenda quando há drift do modelo - quem escreve no modelo é o pantonic-model-designer. Efêmero até a execução do plano de reversão ao standby - cada acionamento é uma instância nova que lê o cenário persistido do plano.
~~~~

### CON-T8a — Corretivo da OP-8: a description volta ao YAML que o harness lê [Sonnet · esforço low · classe mecanica]
- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T8`
- **Objetivo:** Corretivo da `CON-T8` (`AE-20`, `DCS-33`): a `description` de `.claude/agents/pantonic-consultant.md` (`F-4` item 47) volta ao **Texto novo 3** da variante `adotada`, literal — `Efêmero - cada acionamento` onde entrou `Efêmero: cada acionamento` —, porque a sequência dois-pontos-espaço num valor sem aspas faz o parser YAML recusar o frontmatter inteiro, e o consultor é hoje o único dos dez agentes que o harness não lê. A região gerada `kit:agents` de `.claude/README.md` (item 41), regenerada a partir do valor defeituoso, se regenera de novo no mesmo ato. `README.md` não muda: o *"Efêmero: cada acionamento"* do Texto novo 2 é célula de tabela markdown, onde dois-pontos é legítimo.
- **Fundamento:** `DCS-4`, `DCS-20`, `DCS-33`; achado `AE-20`; laudo da `CON-T8` (ressalva 93, `seguir com ressalva`); `F-16`; `I-4`.
- **Operação do modelo:** `OP-8`
  - OP-8: O mantenedor leva a figura nova à porta de entrada do repositório: a tabela de guardrails deixa de rotear o escalonamento ao planejador, a linha do consultor na tabela de agentes deixa de anunciá-lo instanciado uma vez e mantido de prontidão, e a descrição curta do agente é reescrita no mesmo ato em que o índice gerado do kit é regenerado, os quatro passando a descrever o papel de doutrina, a triagem de toda parada e a forma que o veredito do piloto deixou vigente.
  - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`)
- **Camada e fronteira:** porta de entrada — a `description` do agente (item 47) e a região gerada `kit:agents` de `.claude/README.md` (item 41), esta só por instrumento (`I-4`). `README.md` fica como a `CON-T8` deixou.
- **Domínio:** **frontmatter legível** — o bloco YAML entre os dois `---` do agente é o que o harness lê para registrar o agente; um valor escalar sem aspas que contenha a sequência dois-pontos-espaço torna o bloco inválido para um parser estrito, e o arquivo deixa de ser agente. Invariante: o corpo do agente (itens 24 e 44, `CON-T2`, `CON-T2a`, `CON-T4`) não muda.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-consultant.md`
  - `.claude/README.md` (só pelo passo de regeneração)
- **Contratos/classes:** frontmatter YAML do agente: a `description` é uma linha só, sem a sequência dois-pontos-espaço, e `yaml.safe_load` do bloco entre os `---` sai sem erro (linha 1 da `Verificação`).
- **Passos:**
  1. Em `.claude/agents/pantonic-consultant.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1** (é a linha 3 do arquivo, inteira).
  2. Rode `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` (exit `0` medido): ele reescreve a região `kit:agents` de `.claude/README.md` a partir da `description` corrigida.
- **Restrições desta tarefa:**
  - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação — o separador depois de *Efêmero* é hífen entre espaços.
  - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`).
  - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`).
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:**
  - Não editar `.claude/README.md` à mão: só `kit_check.ps1 -Mode generate` (`I-4`).
  - Não tocar `README.md`: a linha 8 da `Verificação` mede que o Texto novo 2 da `CON-T8` fica.
  - Não tocar o corpo do agente (abaixo do segundo `---`) nem as linhas `name:`, `model:` e `tools:` do frontmatter.
- **Contingências:**
  - se o bloco **Texto atual 1** não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco
  - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido
  - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo 1**, corrigir a cópia, rodar o passo 2 de novo e medir de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa`
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`.
- **Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-23 pelo consultor (acionamento 8) na árvore real, **como está depois da `CON-T8`**, com o bloco aplicado e a região regenerada, ambos revertidos por cópia; o executor mede o **antes** antes da primeira edição.
  1. antes: traceback e `1` · depois: `ok` e `0` — o parse YAML estrito do frontmatter

     ~~~~
     python -c "import yaml; yaml.safe_load(open('.claude/agents/pantonic-consultant.md',encoding='utf-8').read().split('---')[1]); print('ok')"; $LASTEXITCODE
     ~~~~

  2. antes `1` · depois `0`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'Efêmero: cada acionamento').Count
     ~~~~

  3. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'Efêmero - cada acionamento').Count
     ~~~~

  4. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/README.md' -SimpleMatch -CaseSensitive -Pattern 'Efêmero - cada acionamento').Count
     ~~~~

  5. antes `0` · com a `description` trocada e a região ainda não regenerada `1` · depois do passo 2 `0`

     ~~~~
     (pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift | Select-String -SimpleMatch -Pattern 'README.md diverge do regenerado').Count
     ~~~~

  6. antes `0` · depois `0`

     ~~~~
     pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift; $LASTEXITCODE
     ~~~~

  7. antes `0` · depois `0`

     ~~~~
     pwsh -NoProfile -File .claude/checks/check-readme.ps1; $LASTEXITCODE
     ~~~~

  8. antes `1` · depois `1` — o Texto novo 2 da `CON-T8` fica

     ~~~~
     (Select-String -Path 'README.md' -SimpleMatch -CaseSensitive -Pattern 'Efêmero: cada acionamento').Count
     ~~~~

  9. antes `0` · depois `0`

     ~~~~
     python .claude/tools/backlog.py check; $LASTEXITCODE
     ~~~~

  10. antes `0` · depois `0`

     ~~~~
     python .claude/tools/modelo.py check --plano docs/plans/P-0747-consultor-de-plano.md; $LASTEXITCODE
     ~~~~

  11. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes — árvore real, acionamento 8 — e `277 passed` depois, com o bloco aplicado e a região regenerada)

     ~~~~
     python -m pytest -q
     ~~~~
- **Pronto quando:**
  - `consultor.descrição pública da figura` — término da `OP-8` (`F-4` itens 41 e 47): a `description` do agente é o Texto novo 3 literal da variante `adotada`, o frontmatter passa no parser YAML estrito e a região gerada, regenerada no mesmo ato, o reproduz; `README.md` e *"O kit são dez agentes"* ficam iguais — Verificação 1 a 8
- **Fora do escopo desta tarefa:** `README.md` (`CON-T8`, fechada); o corpo do agente (`CON-T2`, `CON-T2a`, `CON-T4`, fechadas); `kit_check.ps1 -Mode validate` recusar frontmatter inválido (item (iii) do `AE-20`, tíquete de instrumento, fora deste plano).

**Texto atual 1** — `.claude/agents/pantonic-consultant.md`:

~~~~
description: Consultor de plano Pantonic*, papel de doutrina (GOVERNANCA.md §3, linha Consultoria). Ponto de triagem de toda parada de executor e de todo laudo com pendência substantiva - devolve ao loop a rota resolve, modelador ou planejador, fecha sozinho o técnico e o tático, inclusive o card corretivo da mesma operação, e devolve o dossiê Ato de modelo de emenda quando há drift do modelo - quem escreve no modelo é o pantonic-model-designer. Efêmero: cada acionamento é uma instância nova que lê o cenário persistido do plano.
~~~~

**Texto novo 1** — `.claude/agents/pantonic-consultant.md`:

~~~~
description: Consultor de plano Pantonic*, papel de doutrina (GOVERNANCA.md §3, linha Consultoria). Ponto de triagem de toda parada de executor e de todo laudo com pendência substantiva - devolve ao loop a rota resolve, modelador ou planejador, fecha sozinho o técnico e o tático, inclusive o card corretivo da mesma operação, e devolve o dossiê Ato de modelo de emenda quando há drift do modelo - quem escreve no modelo é o pantonic-model-designer. Efêmero - cada acionamento é uma instância nova que lê o cenário persistido do plano.
~~~~

### CON-T2b — Corretivo da OP-2: o agente nomeia a recusa do impedimento improcedente na rota resolve [Sonnet · esforço low · classe mecanica]
- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T8a`
- **Objetivo:** Corretivo da `CON-T2` e da `CON-T2a` (`DCS-35`, `AE-22`, ato do dono de 2026-09-23): o bullet `rota=resolve` do item 2 da definição de conduta do consultor passa a nomear o desfecho **impedimento improcedente** — o executor parou sem razão e o card é executável como está — com as três amarras: a razão vai à coluna `motivo` da estatística; o card volta a `ready` com ao menos uma linha nova (a contingência ou o fato que responde à dúvida do executor), porque recusar sem tocar o card só reproduz a parada num executor frio; o redespacho não consome a retentativa.
- **Fundamento:** `DCS-4`, `DCS-35`; achado `AE-22`; ato do dono transcrito em `DCS-35`.
- **Operação do modelo:** `OP-2`
  - OP-2: O autor de papéis reescreve a definição de conduta do consultor sobre a norma nova: tira dela o estatuto provisório, faz qualquer das três razões de parada acioná-lo, dá a ele a rota que devolve, os deveres de validar a emenda do modelo no marco e de emiti-la quando a resolução muda o que o plano entrega, a linha de estatística que ele apensa a cada acionamento e a saída curta por edição mínima.
  - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`); parada de executor — nenhuma operação altera uma parada. O que se observa nela, antes e depois, é o caminho: quem a recebe, quem decide a rota e onde isso fica registrado. As paradas do `P-0745` e do `P-0746` (`F-8`) são o retrato do antes; o depois são as paradas da janela de execução deste plano, lidas no arquivo de estatística de `DCS-8` a partir do aceite da `OP-2`; planejador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 13, 19, 20 e 25 — é a fronteira do consultor e nada além: a rodada de replanejamento chega pela rota `planejador` da triagem, só quando emenda aceita cria ou remove operação ou quando a premissa cai inteira (`superseded`), e o corretivo `T<n>a` da mesma operação, com o id apensado à lista `tarefas:`, passa a ser também ato do consultor (`DCS-4`). O que `DCS-18` deixa com o planejamento continua com ele. Alterar outra conduta do planejador é colateral e se escala; modelador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 26, 27 e 28 — é a fronteira do consultor e nada além: o consultor é nomeado como quem origina o dossiê de `emenda` e como quem apensa o id do corretivo à lista `tarefas:`; quem despacha continua sendo quem conduz a sessão (`I-2`). Os literais que a guarda executável prende no arquivo dele (`F-15`) ficam. O instrumento do modelo e seus testes não se tocam
- **Camada e fronteira:** definição de agente — `.claude/agents/pantonic-consultant.md`, só o bullet `rota=resolve` do item 2 (`:25`), do item 24 de `F-4`; sem código.
- **Domínio:** **impedimento improcedente** — desfecho da `rota=resolve` em que o consultor recusa a parada porque o card era executável como está (`DCS-35`). **Linha nova** — a contingência ou o fato que responde à dúvida do executor, gravada no card antes do redespacho; sem ela a recusa não é permitida. **Retentativa** — o redespacho por recusa não a consome.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-consultant.md`
- **Contratos/classes:** nenhuma assinatura de código; o front matter (`:1-6`) não muda, e a linha 3 da `Verificação` mede que ele continua a parsear (`AE-20`).
- **Passos:**
  1. Em `.claude/agents/pantonic-consultant.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**.
- **Restrições desta tarefa:**
  - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação.
  - Não commitar (`DCS-16`). Não tocar a `description` (item 47, `OP-8`) nem as linhas de forma (item 44, `OP-4`).
  - Nenhum agente aciona outro: o redespacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`).
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:**
  - Não tocar a skill do loop: é da `CON-T3d` (`OP-3`).
  - Não tocar os bullets `rota=modelador` e `rota=planejador` (`:26-27`) nem a frase de abertura do item 2 (`:24`).
- **Contingências:**
  - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco
  - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido
  - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa`
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`.
- **Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-23 pelo consultor (acionamento 10) na árvore real, com o bloco aplicado e revertido por hash, **como está depois da `CON-T8a`**; o executor mede o **antes** antes da primeira edição.
  1. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'recusar o impedimento como improcedente').Count
     ~~~~

  2. antes `0` · depois `1`

     ~~~~
     (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'não consome a retentativa').Count
     ~~~~

  3. antes `0` · depois `0`

     ~~~~
     python -c "import yaml; t=open('.claude/agents/pantonic-consultant.md',encoding='utf-8').read(); yaml.safe_load(t.split('---')[1])"; $LASTEXITCODE
     ~~~~

  4. antes `0` · depois `0`

     ~~~~
     python .claude/tools/backlog.py check; $LASTEXITCODE
     ~~~~

  5. antes `0` · depois `0`

     ~~~~
     python .claude/tools/modelo.py check --plano docs/plans/P-0747-consultor-de-plano.md; $LASTEXITCODE
     ~~~~

  6. antes `0` · depois `0`

     ~~~~
     pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift; $LASTEXITCODE
     ~~~~

  7. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes — laudo da `CON-T8a`, mesma árvore — e `277 passed` depois, no ensaio de 2026-09-23 do acionamento 10)

     ~~~~
     python -m pytest -q
     ~~~~
- **Pronto quando:**
  - `consultor.fronteira com o planejador` — fatia da `OP-2` (`F-4` item 24): o consultor fecha o técnico e o tático, e entre os desfechos da rota `resolve` está recusar o impedimento improcedente com as três amarras de `DCS-35` — Verificação 1, 2
- **Fora do escopo desta tarefa:** a skill do loop (`CON-T3d`); a `## 1A` (modelador, dossiê de emenda de `DCS-35`).

**Texto atual 1** — `.claude/agents/pantonic-consultant.md`:

~~~~
   - `rota=resolve` — a questão é operacional, técnica ou tática: você a fecha sozinho, e o dono não valida (ato do dono de 2026-09-22: *"Eu não vou validar a decisão dele para questões técnicas e táticas."*).
~~~~

**Texto novo 1** — `.claude/agents/pantonic-consultant.md`:

~~~~
   - `rota=resolve` — a questão é operacional, técnica ou tática: você a fecha sozinho, e o dono não valida (ato do dono de 2026-09-22: *"Eu não vou validar a decisão dele para questões técnicas e táticas."*). Um dos desfechos é **recusar o impedimento como improcedente** — o executor parou sem razão e o card é executável como está (`DCS-35` do `P-0747`), com três amarras: você declara a improcedência com a razão, que vai à coluna `motivo` da estatística; devolve o card a `ready` com **ao menos uma linha nova** — a contingência ou o fato que responde à dúvida do executor —, porque recusar sem tocar o card só reproduz a parada num executor frio; e o redespacho **não consome a retentativa**.
~~~~

### CON-T3d — Corretivo da OP-3: o loop redespacha sem retentativa o card cujo impedimento o consultor recusou [Sonnet · esforço low · classe mecanica]
- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T2b`
- **Objetivo:** Corretivo da `CON-T3`, `CON-T3a`, `CON-T3b` e `CON-T3c` (`DCS-35`, `AE-22`, ato do dono de 2026-09-23): as regras da skill do loop que recebem `rota=resolve` de uma parada de executor — a triagem do passo 8, `A3a`, `A3b`, `A3c` e a lista *Segue com registro* — passam a nomear o desfecho **impedimento improcedente**: a mesma tarefa volta a `ready` com ao menos uma linha nova gravada pelo consultor e é redespachada **sem** consumir retentativa. `A6a`, `A7` e `B1` não mudam: partem de laudo, não de parada, e a `A6a` já refaz sem gastar retentativa.
- **Fundamento:** `DCS-3`, `DCS-4`, `DCS-35`; achado `AE-22`; ato do dono transcrito em `DCS-35`.
- **Operação do modelo:** `OP-3`
  - OP-3: O mantenedor do loop reescreve a condução das paradas: as duas fontes normativas da skill passam a citar as decisões deste plano, toda regra que roteia parada de executor ou laudo com pendência substantiva e o guardrail que manda a matéria ao planejador passam a levá-los ao consultor, o loop despacha a rota que ele devolve e, quando a rota é o modelador, despacha o modelador sem parar a janela e leva o pedido de validar o drift ao dono no marco.
  - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`); parada de executor — nenhuma operação altera uma parada. O que se observa nela, antes e depois, é o caminho: quem a recebe, quem decide a rota e onde isso fica registrado. As paradas do `P-0745` e do `P-0746` (`F-8`) são o retrato do antes; o depois são as paradas da janela de execução deste plano, lidas no arquivo de estatística de `DCS-8` a partir do aceite da `OP-2`; planejador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 13, 19, 20 e 25 — é a fronteira do consultor e nada além: a rodada de replanejamento chega pela rota `planejador` da triagem, só quando emenda aceita cria ou remove operação ou quando a premissa cai inteira (`superseded`), e o corretivo `T<n>a` da mesma operação, com o id apensado à lista `tarefas:`, passa a ser também ato do consultor (`DCS-4`). O que `DCS-18` deixa com o planejamento continua com ele. Alterar outra conduta do planejador é colateral e se escala; modelador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 26, 27 e 28 — é a fronteira do consultor e nada além: o consultor é nomeado como quem origina o dossiê de `emenda` e como quem apensa o id do corretivo à lista `tarefas:`; quem despacha continua sendo quem conduz a sessão (`I-2`). Os literais que a guarda executável prende no arquivo dele (`F-15`) ficam. O instrumento do modelo e seus testes não se tocam
- **Camada e fronteira:** procedimento de orquestração — `.claude/skills/scrum-master/SKILL.md`, só a triagem do passo 8 (`F-4` item 2), `A3a`/`A3b`/`A3c` (item 6) e a lista *Segue com registro* (item 11); sem código.
- **Domínio:** **impedimento improcedente** — o consultor recusa a parada porque o card era executável como está (`DCS-35`); para o loop é reparo da rota `resolve`, não rota nova. **Redespacho por recusa** — a mesma tarefa, de volta a `ready` com a linha nova, ao executor seguinte, sem consumir retentativa — a tarefa não falhou, o executor parou sem razão; o mesmo tratamento que o `A3c` já dá ao fallback declarado. Invariante: sem `estrategico=`, `resolve` segue; `planejador` e `estrategico=` param (`DCS-24`, `DCS-28`).
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
- **Contratos/classes:** nenhuma assinatura de código; nenhuma linha de tabela nasce ou morre — três células mudam (`A3a`, `A3b`, `A3c`).
- **Passos:**
  1. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1** (passo 8, *Triagem*).
  2. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 2** pelo bloco **Texto novo 2** (`A3a`).
  3. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 3** pelo bloco **Texto novo 3** (`A3b`).
  4. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 4** pelo bloco **Texto novo 4** (`A3c`).
  5. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 5** pelo bloco **Texto novo 5** (lista *Segue com registro*).
- **Restrições desta tarefa:**
  - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação. O arquivo tem terminadores CRLF: preservar.
  - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`).
  - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`).
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:**
  - Não tocar `A6a`, `A7` e `B1`: laudo não é parada, e a recusa de `DCS-35` não os alcança; as linhas 5, 6 e 7 da `Verificação` medem isso.
  - Não tocar a lista *Obriga parada*, a `A1`, a seção `## Acionamento do consultor` nem a nota do passo 9.
  - Não tocar o agente do consultor: é da `CON-T2b` (`OP-2`).
- **Contingências:**
  - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco
  - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido
  - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa`
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`.
- **Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-23 pelo consultor (acionamento 10) na árvore real, com os blocos aplicados e revertidos por hash, **como está depois da `CON-T8a`** (a `CON-T2b` não toca este arquivo); o executor mede o **antes** antes da primeira edição. A linha 2 é a coerência do módulo: as cinco ocorrências caem exatamente nas cinco regras que recebem `rota=resolve` de parada de executor, e em nenhuma outra; o **antes** dela é vazio (nenhuma linha casa).
  1. antes `0` · depois `5`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'improcedente').Count
     ~~~~

  2. antes `` · depois `154,224,225,226,260`

     ~~~~
     ((Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'improcedente').LineNumber -join ',')
     ~~~~

  3. antes `0` · depois `5`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern '`DCS-35`').Count
     ~~~~

  4. antes `1` · depois `5`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'consumir retentativa').Count
     ~~~~

  5. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'refazer com diretivas novas ou emendar o card').Count
     ~~~~

  6. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'A escalada é a do `A3b`: ao **consultor**').Count
     ~~~~

  7. antes `1` · depois `1`

     ~~~~
     (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'descarta o laudo e escala ao **consultor de plano**').Count
     ~~~~

  8. antes `0` · depois `0`

     ~~~~
     python .claude/tools/backlog.py check; $LASTEXITCODE
     ~~~~

  9. antes `0` · depois `0`

     ~~~~
     python .claude/tools/modelo.py check --plano docs/plans/P-0747-consultor-de-plano.md; $LASTEXITCODE
     ~~~~

  10. antes `0` · depois `0`

     ~~~~
     pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift; $LASTEXITCODE
     ~~~~

  11. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes — laudo da `CON-T8a`, mesma árvore — e `277 passed` depois, no ensaio de 2026-09-23 do acionamento 10)

     ~~~~
     python -m pytest -q
     ~~~~
- **Pronto quando:**
  - `consultor.alcance da triagem das paradas` — fatia da `OP-3` (`F-4` itens 2, 6 e 11): na rota `resolve`, a recusa do impedimento improcedente devolve a mesma tarefa a `ready` com a linha nova e a redespacha sem consumir retentativa, nas três paradas de executor e na triagem do passo 8 — Verificação 1 a 4
- **Fora do escopo desta tarefa:** o agente do consultor (`CON-T2b`); a `## 1A` (modelador, dossiê de emenda de `DCS-35`); `A6a`, `A7`, `B1` e a lista *Obriga parada*.

**Texto atual 1** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
`rota=resolve` sem `estrategico=` — o reparo já está gravado no plano, e a janela segue;
~~~~

**Texto novo 1** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
`rota=resolve` sem `estrategico=` — o reparo já está gravado no plano, e a janela segue; quando o reparo é a recusa do impedimento como improcedente (`P-0747` `DCS-35`), a mesma tarefa volta a `ready` com ao menos uma linha nova gravada pelo consultor e é redespachada **sem** consumir retentativa;
~~~~

**Texto atual 2** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
na rota `resolve`, a reordenação da fila que ele gravar, com a bloqueada depois da que a bloqueia: segue para a próxima elegível;
~~~~

**Texto novo 2** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
na rota `resolve`, a reordenação da fila que ele gravar, com a bloqueada depois da que a bloqueia: segue para a próxima elegível — ou, recusado o impedimento como improcedente (`DCS-35`), o redespacho da mesma tarefa, de volta a `ready` com a linha nova que ele gravou, **sem** consumir retentativa;
~~~~

**Texto atual 3** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
`resolve` segue com o reparo; `modelador` segue com o despacho do modelador;
~~~~

**Texto novo 3** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
`resolve` segue com o reparo — inclusive a recusa do impedimento como improcedente (`DCS-35`): a mesma tarefa volta a `ready` com ao menos uma linha nova e é redespachada **sem** consumir retentativa; `modelador` segue com o despacho do modelador;
~~~~

**Texto atual 4** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
e sem fallback aplica o reparo que o consultor gravar;
~~~~

**Texto novo 4** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
e sem fallback aplica o reparo que o consultor gravar — inclusive a recusa do impedimento como improcedente (`DCS-35`), que redespacha a mesma tarefa, de volta a `ready` com a linha nova, **sem** consumir retentativa;
~~~~

**Texto atual 5** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
com o reparo que ele gravou — a reordenação da fila no `A3a`, o redespacho pelo fallback declarado no `A3c`;
~~~~

**Texto novo 5** — `.claude/skills/scrum-master/SKILL.md`:

~~~~
com o reparo que ele gravou — a reordenação da fila no `A3a`, o redespacho pelo fallback declarado no `A3c`, o redespacho da mesma tarefa com a linha nova quando ele recusa o impedimento como improcedente (`A3a`, `A3b`, `A3c`; `DCS-35`), sem consumir retentativa;
~~~~

## 6. Ordem de execução

Grafo linear, sem paralelismo: `CON-T1` → `CON-T2` → `CON-T3` → `CON-T3a` → `CON-T4` → `CON-T2a` → `CON-T3b` → `CON-T4a` → `CON-T3c` → `CON-T5` → `CON-T6` → `CON-T5a` → `CON-T6a` → `CON-T7` → `CON-T7a` → `CON-T8` → `CON-T8a` → `CON-T2b` → `CON-T3d`.

- A doutrina vem primeiro (`CON-T1`, `CON-T2`). Depois vem o loop (`CON-T3`, que lê a linha `rota=` definida na `CON-T2`).
- A forma efêmera (`CON-T4`) vem cedo para alargar a janela do piloto. Todo acionamento do consultor depois do aceite dela já corre na forma nova e conta na `CON-T7`.
- `CON-T3` e `CON-T4` editam a mesma linha da `B1` em trechos disjuntos, por isso são sequenciais. `CON-T2` e `CON-T4` editam o mesmo agente em linhas disjuntas, também em sequência.
- A medida do piloto é a penúltima (`CON-T7`) e a revisão do `README.md` é a última (`CON-T8`), porque lê o veredito (`DCS-17`).
- Os três corretivos do acionamento 4 (`AE-9`) entram logo depois da `CON-T4` e antes da `CON-T5`: `CON-T2a` edita o agente, `CON-T3b` e `CON-T4a` editam a skill em trechos disjuntos, por isso em sequência; a `CON-T5` não toca nenhum dos dois arquivos, mas passa a depender da `CON-T4a` para manter o grafo linear.
- O corretivo do acionamento 5 (`AE-12`, `DCS-30`) entra logo depois da `CON-T4a` e antes da `CON-T5`: `CON-T3c` edita a skill nos mesmos dois trechos da `CON-T3b` (passo 8 e lista *Obriga parada*); a `CON-T5` passa a depender da `CON-T3c`. Foi um card, não três: a `A1` entra em `F-4` por dossiê de conflito, e o aposto da nota do passo 9 não abre card por saturação (spec §2).
- Os dois corretivos do acionamento 6 (`AE-16`, `DCS-31`) entram logo depois da `CON-T6` e antes da `CON-T7`: `CON-T5a` edita o diário e a Regra 8 (`OP-5`), `CON-T6a` edita a spec (`OP-6`) — arquivos disjuntos, em sequência para manter o grafo linear; a `CON-T7` passa a depender da `CON-T6a`. Dois cards e não um: cada card materializa uma operação (`G-PLANREADY`) e o corretivo é da operação do card que corrige (`DCS-4`).
- O corretivo do acionamento 7 (`AE-19`, `DCS-32`) entra logo depois da `CON-T7` e antes da `CON-T8`: `CON-T7a` apensa à subseção do veredito na §11 da spec (`OP-7`) a declaração do modelo das instâncias e do preço-Opus-equivalente, sem mudar a linha da tabela que a `CON-T8` lê; a `CON-T8` passa a depender da `CON-T7a`.
- O corretivo do acionamento 8 (`AE-20`, `DCS-33`) entra depois da `CON-T8`, último da fila: `CON-T8a` devolve a `description` do agente ao Texto novo 3 literal (`OP-8`, item 47) e regenera a região gerada (item 41) no mesmo ato, com o parse YAML do frontmatter como linha de `Verificação`; depende da `CON-T8`. Um card, não dois: os dois itens são da mesma operação.
- Os dois corretivos do acionamento 10 (`AE-22`, `DCS-35`, ato do dono) entram depois da `CON-T8a`, últimos da fila: `CON-T2b` edita o agente (`OP-2`, item 24), `CON-T3d` edita a skill do loop (`OP-3`, itens 2, 6 e 11) — arquivos disjuntos, em sequência para manter o grafo linear; `CON-T2b` depende da `CON-T8a` e `CON-T3d` da `CON-T2b`. Dois cards e não um: o item 24 é da partição da `OP-2` (`DCS-31`).

## 7. Fora de escopo (explícito)

- Critério de não-acionamento na entrada. Mora no `TK-55` (`DCS-10`).
- Spec de robustez. O acumulador é o `TK-55`, e este plano só entrega a residência da estatística que
  a alimenta (`DCS-8`).
- Vigência bilateral do modelo e conduta de drift do loop em `GOVERNANCA.md` §4.5. Mora no `TK-70`
  (`DCS-12`).
- Propagação aos derivados e à cópia global do dono. Fica com a skill `checar-versao-kit` (`DCS-13`).
- Standby com ping de aquecimento (spec §11 ii). Só entra por plano novo se o piloto recusar a forma
  efêmera (`DCS-7`).
- Correção das três contagens defasadas da spec (`DCS-2`).
- Emendas à régua de autoria de card do `TK-72` e facetas de instrumento do `TK-66`/`TK-74`.

## 8. Riscos

| risco | resposta pré-decidida |
|---|---|
| Durante a execução deste plano o consultor é regido pelo arquivo que o próprio plano está reescrevendo. | Até o aceite da operação que o reescreve vale o arquivo vigente mais a spec (precedência do dono, ato 7 da §0). Depois do aceite, vale o arquivo novo. |
| Menos de 3 acionamentos na janela do piloto. | Veredito `amostra insuficiente` (`DCS-7`), gravado como linha nova na spec §11. O piloto segue na próxima execução de plano. |
| O cenário ultrapassa 15k tokens. | O consultor move matéria fechada para `## 9` do plano, com ponteiro, e registra a ocorrência na coluna `inconclusivo` da linha de `DCS-8`. |
| `backlog.py check` ou `modelo.py check` tratam `_CENARIO-P-NNNN.md` como plano. | O card que cria o cenário roda os dois instrumentos com o arquivo presente. Se algum sair diferente de 0 por causa dele → `blocked` razão `premissa`, e a rodada decide a residência. |
| `tests/test_doutrina_unidade.py` falha por literal que a reescrita alterou. | Medido no ensaio de 2026-09-22, com os oito cards aplicados numa cópia da árvore: `8 passed` depois de cada card e `277 passed` na suíte. Falha na execução real → `blocked` razão `premissa`. |
| A reescrita da `A3b` colide com texto do `TK-70` na mesma skill. | Este plano edita só o bloco A, o passo 8 e a lista de parada (`DCS-12`). Trecho sobre vigência do modelo fica intocado. |

## 9. Achados da execução

- **AE-1** — 2026-09-23 · acionamento 1 · forma de prontidão, instanciado por quem conduz a sessão, em Fable por pedido do dono · **Motivou:** o ato do dono `DCS-23`, delegando ao consultor as decisões sobre `docs/plans/_VEREDITO-procedimentos-2026-09-22.md` (§3.1-3.8, §4 itens 1-4, §5). · **Classe do impedimento:** decisão de planejamento pendente antes do Marco 1, por ato do dono (gatilho 4 da spec §2); nenhuma parada de executor. · **Decidido:** `DCS-24` (drift carregado até o marco, sem parar a janela), `DCS-25` (destino de cada item do veredito) e `DCS-26` (cenário por ponteiro; encerramento desta instância no aceite da `CON-T4`); textos apensados verbatim a `TK-72` §7 e a `TK-67` (*Insumo do veredito*) em `docs/DIARIO_DE_OBRAS.md`; `CON-T1` (Texto novo 3, 5, 7, 15; Verificação 17), `CON-T2` (Texto novo 2, 5), `CON-T3` (objetivo e cópia da `OP-3`; Texto novo 2, 5, 6, 9, 10), `CON-T4` (Arquivo novo) e `CON-T5` (Texto novo 15) reescritos, e o `Pronto quando` de `consultor.fronteira com o modelador` nos quatro cards que o carregam; as linhas de `Verificação` afetadas foram re-medidas em 2026-09-23 numa cópia da árvore com os cards aplicados em sequência. · **Inconclusivo:** (a) a `## 1` ainda diz que o loop para — texto da `OP-3` e estado final de `consultor.fronteira com o modelador` —; o dossiê de autoria foi devolvido na linha de retorno, e até o ato do modelador a cópia da `OP-3` em `CON-T3` e os `Pronto quando` divergem da `## 1` nesse ponto — após o ato, um acionamento confere se a cópia bate e corrige por `Edit`; (b) a retroação das tarefas quando o drift é recusado no marco é conduta do loop e fica com o `TK-70` (`DCS-12`); (c) a medida retomada × invocação fria (veredito §3.7) fica com o `TK-72`; (d) o inchaço dos cards pelo contrato copiado fica como está neste plano (`DCS-25`). · **Estratégico:** nenhum. · **Fechado** em 2026-09-23 (`AE-2`): (a) resolvida pela versão 1 reautorada no lugar pelo modelador (`### 1.4`, linha da versão 1, "e pelo quarto (`DCS-24`, 2026-09-23)"); (b), (c) e (d) seguem nas residências nomeadas.
- **AE-2** — 2026-09-23 · acionamento 2 · forma de prontidão, retomado por mensagem · **Motivou:** o ato do modelador sobre o dossiê `DCS-24` (versão 1 substituída no lugar: `OP-3`, estado final de `consultor.fronteira com o modelador`, nota *Como ler*, linha da versão), com o pedido de conferir as cópias nos cards. · **Classe do impedimento:** conferência de cópia card × modelo após ato de modelo (gatilho 2 da spec §2, por analogia — pendência de fechamento roteada pelo loop); nenhuma parada de executor. · **Decidido:** conferência por comparação literal, não por releitura: o `Pronto quando` de `consultor.fronteira com o modelador` em `CON-T1`, `CON-T2`, `CON-T3` e `CON-T5` é idêntico à célula de estado final da `### 1.3` (487 caracteres), e a oração final nova da `OP-3` ocorre exatamente 3 vezes no plano (`## 1`, objetivo e sub-bullet do `CON-T3`); nenhum card alterado; `AE-1` fechado. · **Inconclusivo:** nenhum. · **Estratégico:** nenhum. · fechado.
- **AE-3** — 2026-09-23 · laudo da `CON-T1` (aprovado 100, `seguir`), alvo `dossiê` · o `Pronto quando` de cada card enuncia a propriedade inteira, cuja fatia cabe a vários cards; só a fatia do card é verificável nele. Não bloqueia: as verificações do card medem a fatia dele. **Rota:** `TK-72` (recortar o `Pronto quando` à fatia da operação), sem reparo neste plano — vai reaparecer nos laudos das tarefas seguintes e se registra por ponteiro a este achado. Segundo achado do mesmo laudo (atribuição por hunk sobre árvore com WIP) → `TK-66`, sem ação nova.
- **AE-4** — 2026-09-23 · laudo da `CON-T3` (aprovado 100, recomendação `escalar`, fechado por `A8a`), pendência substantiva roteada pelo `B1` ao consultor · a skill do loop saiu incoerente sobre o destino da parada: (i) a `A6a` (Texto novo 7) diz que a janela segue com o que o consultor devolver, sem ressalvar a rota `planejador` que o passo 8, a lista *O que obriga parada* e o guardrail mandam parar — o `DCS-24` reautorou os blocos 2, 5, 6, 9 e 10 e não o 7; (ii) a classificação `estratégico` só aparece no `B1` e na lista de parada, não na triagem do passo 8 nem em `A3a`/`A3b`/`A3c`/`A6a`/`A7`, e `rota=resolve` + `estratégico` cai ao mesmo tempo em *Obriga parada* e *Segue com registro*; (iii) o card não tinha linha de coerência do módulo, e as divergências passaram nas onze verificações. Pedido do revisor: corretivo `CON-T3a` da `OP-3`, autorado pelo consultor (`DCS-4`). Laudo preservado em `%TEMP%\claude\laudo-CON-T3.md` até o reparo. · **Fechado** em 2026-09-23 (`AE-5`): corretivo `CON-T3a` autorado e enfileirado antes da `CON-T4`; `DCS-27`.
- **AE-5** — 2026-09-23 · acionamento 3 · forma de prontidão, retomado por mensagem · gatilho 2 (laudo com pendência substantiva, `B1`) · **Motivou:** `AE-4` — a `CON-T3` fechou aprovada 100 com recomendação `escalar`: `A6a` seguindo incondicionalmente, `estratégico` sem forma mecânica e fora da triagem, `Segue com registro` sem o gate do passo 9, e nenhuma linha de coerência no card. · **Classe do impedimento:** defeito de autoria de card (reautoria parcial pela `DCS-24`) sem aceite de coerência do módulo; nenhum drift. · **Decidido:** `rota=resolve`; `DCS-27`; corretivo `CON-T3a` da `OP-3` autorado pelo consultor com os dez blocos medidos contra a skill como está depois da `CON-T3`, `Depende de: CON-T3`, `CON-T4` passa a depender de `CON-T3a`, id apensado à lista `tarefas:` da `OP-3` (lastro, `DCS-4`); `CON-T4` emendada nos pontos que falam do retorno (Texto novo 3 e o cenário); `CON-T5` conferida — nenhum texto novo dela enuncia parada, só devolução à triagem — e não muda. · **Inconclusivo:** a forma da linha `estrategico=` não consta do agente do consultor (item 24, `OP-2`, já fechada) — vive provisoriamente no cenário da `CON-T4` e entra no agente no próximo ato sobre o item 24; a lacuna de autoria "aceite sem linha de coerência do módulo" já está no `TK-72` (Pacote 4, verificação com valor esperado) e ganha ali este caso. · **Estratégico:** nenhum. · fechado.
- **AE-6** — 2026-09-23 · laudo da `CON-T3a` (aprovado 100, `seguir`), alvo `dossiê`, não bloqueante · a `DCS-27`, a triagem do passo 8 e a forma do retorno no cenário da `CON-T4` dizem que com `estrategico=` o loop **para** em qualquer rota, mas não fecham se a ação própria da rota executa antes da parada — com `rota=modelador`, o dossiê de emenda fica sem destino nomeado. **Rota:** próximo acionamento do consultor; se não houver até o fechamento, entra nas pendências da entrega de encerramento. · **Fechado** em 2026-09-23 (`AE-9`): `DCS-28`; corretivos `CON-T3b` (passo 8 e lista de parada) e `CON-T2a` (forma da linha no agente).
- **AE-7** — 2026-09-23 · laudo da `CON-T4` (aprovado 100, `seguir`), alvo `dossiê` · `.claude/agents/pantonic-consultant.md:19` (*Por que você existe*) ainda prescreve a forma de prontidão — o cenário *"num contexto só, vivo"* — contra a `:8` (*"você é efêmero"*); a linha foi enumerada no item 24 da `F-4` (`OP-2`, fechada) e não no item 44 (forma). **Rota:** consultor. · **Fechado** em 2026-09-23 (`AE-9`): `DCS-29`; corretivo `CON-T2a` da `OP-2`, a operação que possui o item.
- **AE-8** — idem · a `A1` da skill do loop segue genérica (*"queda do subagente"* → retomada por `SendMessage` ao mesmo `agentId`) e a seção *Acionamento do consultor* diz que nenhuma instância é retomada por `SendMessage`: duas regras para a queda de uma instância do consultor. **Rota:** consultor. · **Fechado** em 2026-09-23 (`AE-9`): `DCS-29`; corretivo `CON-T4a` da `OP-4`.
- **AE-9** — 2026-09-23 · acionamento 4 · **primeira instância efêmera** (`DCS-6`, `DCS-26`), Fable por pedido do dono · gatilho 2 (laudos da `CON-T3a` e da `CON-T4`, aprovadas 100 `seguir`, com `AE-6`, `AE-7` e `AE-8` roteados ao consultor) · **Motivou:** três defeitos de coerência entre residências reescritas por operações já fechadas — a ordem entre parar e agir com `estrategico=` (`OP-3`), a `:19` do agente ainda na forma de prontidão (`OP-2`) e a `A1` contra a seção *Acionamento do consultor* (`OP-4`). · **Classe do impedimento:** coerência de residência, nenhuma parada de executor, nenhum drift (gatilho 2 da spec §2). · **Decidido:** `rota=resolve`; `DCS-28`, `DCS-29`; três corretivos autorados pelo consultor (`DCS-4`, `I-9`), com blocos e `Verificação` medidos em 2026-09-23 na árvore real — aplicados em sequência, checks e suíte rodados no estado final (`277 passed`), revertidos por hash —: `CON-T2a` (`OP-2`), `CON-T3b` (`OP-3`), `CON-T4a` (`OP-4`); fila `CON-T4 → CON-T2a → CON-T3b → CON-T4a → CON-T5`, `CON-T5` passa a depender de `CON-T4a`; ids apensados às listas `tarefas:`; `AE-6`, `AE-7` e `AE-8` fechados; o inconclusivo de `AE-5` (forma de `estrategico=` no agente) fechado pela `CON-T2a`. · **Inconclusivo:** (a) instância que cai no meio de um `Edit` deixa cenário ou plano meio-escritos, e a instância nova os lê como estão (`DCS-29`), sem verificação de integridade — fica para o `TK-55`, sobre a estatística; (b) a `Verificação` dos três cards mede a fatia (`AE-3`, `TK-72`). · **Estratégico:** nenhum. · fechado.
- **AE-10** — 2026-09-23 · laudo da `CON-T3b` (aprovado 100, `seguir`), dois achados · (i) alvo `modelo`: a `OP-3` não cobria a parada por `estrategico=` — **absorvido** pelo ato de conflito do modelador, versão 2 **pendente** em `## 1A` (só `OP-3` e o estado final de `consultor.alcance da triagem das paradas`), a adjudicar no marco de fechamento (`DCS-24`); (ii) alvo `dossiê`, não bloqueante: o Texto novo 1 da `CON-T3b` (passo 8) suprime a ação da rota "em qualquer rota", inclusive `planejador`, contra a `DCS-28` (*"com `rota=planejador` a ação da rota já é a parada, e nada muda ali"*) — com `estrategico=` + `planejador` a skill deixa de materializar o plano `blocked` e de enfileirar o replanejamento. **Rota:** próximo acionamento do consultor; sem acionamento até o fechamento, entra nas pendências da entrega de encerramento. · (ii) **fechado** pelo acionamento 5: `CON-T3c` (`AE-12`, `DCS-30`).
- **AE-11** — 2026-09-23 · laudo da `CON-T4a` (aprovado 100, `seguir`), dois achados, laudo preservado em `%TEMP%\claude\laudo-CON-T4a.md` · (i) alvo `modelo`, com dossiê `Ato de modelo` de `conflito` anexo: a linha `A1` da skill do loop passou a citar o consultor (`DCS-29`), mas não está na `F-4` nem na partição de residências da `OP-4` (itens 3, 44, 45, cenário e seção *Acionamento do consultor*), e a própria `OP-4` classifica residência assim como achado para o modelador; (ii) alvo `dossiê`: a nota de telemetria do passo 9 (item 3 da `F-4`) diz *"a retomada do executor pela `A1`"*, e a `A1` reescrita retoma executor **ou** reviewer. **Rota:** consultor (a `F-4` é seção do plano, não do modelo), junto com o `AE-10` (ii); o dossiê de conflito segue ao modelador depois do reparo da `F-4`. · **fechado** pelo acionamento 5: (i) item 48 de `F-4` e dossiê de conflito ao modelador; (ii) sem card, por saturação (`AE-12`, `DCS-30`).
- **AE-12** — 2026-09-23 · acionamento 5 · instância efêmera, Fable por pedido do dono · gatilho 2 (laudos da `CON-T3b` e da `CON-T4a`, aprovadas 100 `seguir`, com `AE-10` (ii) e `AE-11` roteados ao consultor) · **Motivou:** a triagem do passo 8 suprimindo a ação da rota `planejador` com `estrategico=` (`OP-3`); a `A1` citando o consultor fora de `F-4` e da partição da `OP-4`; o aposto da nota de telemetria do passo 9 nomeando só o executor. · **Classe do impedimento:** coerência de residência (`OP-3`) e partição de `F-4` (`OP-4`); nenhuma parada de executor; nenhum drift de estado final. · **Decidido:** `rota=modelador`; `DCS-30`; teste de saturação e capacidade × término aplicados antes de abrir card (spec §2): **um** corretivo, `CON-T3c` (`OP-3`), com blocos e `Verificação` medidos em 2026-09-23 na árvore real — aplicados, checks em 0 e `277 passed`, revertidos por hash —; fila `CON-T4a → CON-T3c → CON-T5`, `CON-T5` passa a depender de `CON-T3c`; id apensado à lista `tarefas:` da `OP-3`; `F-4` ganha o item 48 (cláusula do consultor na `A1`) e o dossiê de `conflito` segue ao modelador para reescrever a versão 2 pendente no lugar; `AE-10` (ii) e `AE-11` fechados. · **Inconclusivo:** (a) o aposto da nota do passo 9 (`AE-11` ii) fica como pendência do relatório de encerramento, sem card; (b) o item 2 do agente do consultor (`:24`, item 24 de `F-4`, `OP-2`) diz *"para em qualquer rota sem executar a ação da rota"* — a frase da `DCS-28`, que ele cita e que ela mesma qualifica para `planejador`; não se toca, pela mesma saturação; (c) as cópias de *precisa de* nos cards seguem a versão 1 vigente (*"itens 1 a 47"*) e só se re-copiam se a versão 2 vigorar no marco, como no acionamento 2. · **Estratégico:** nenhum. · fechado.
- **AE-13** — 2026-09-23 · laudo da `CON-T3c` (aprovado 100, `seguir`) · (i) alvo `modelo`: a versão 2 pendente dizia que com `estrategico=` nenhuma rota executa a ação, contra a `CON-T3c` — **absorvido** pelo terceiro ato de conflito do modelador, versão 2 reescrita no lugar (exceção de `planejador` fixada; contagens do estado a 48); (ii) alvo `dossiê`, achado de processo do consultor: o acionamento 5 (`AE-12`, `DCS-30`) declarou "nenhum drift de estado final" e mandou ao modelador só o item 48, sem confrontar a `DCS-30` (i) com o texto pendente da `OP-3` — o conflito só apareceu na revisão seguinte. **Rota:** estatística da spec do consultor (`TK-55`) — classe *decisão que muda o que a entrega faz, sem confronto com o modelo pendente*; sem ação no plano.
- **AE-14** — 2026-09-23 · laudo da `CON-T5` (aprovado 100, `seguir`), laudo preservado em `%TEMP%\claude\laudo-CON-T5.md` · (i) residência fora da `F-4` que ainda roteia parada: `.claude/skills/diario-de-obras/SKILL.md:79-83` diz que plano cuja revisão foi pedida por quem executa vai a `blocked` e abre rodada de replanejamento, enquanto a skill do loop só leva o plano a `blocked` na rota `planejador`; (ii) homonímia introduzida pelo Texto novo 17 na Regra 8 de `.claude/global/CLAUDE.md`: "rota" de triagem (`resolve|modelador|planejador`) e "rota aprovada do plano" no mesmo período, com donos diferentes. **Rota:** consultor, em acionamento único antes da `CON-T7`, junto com o que o laudo da `CON-T6` trouxer. · **Fechado** em 2026-09-23 (`AE-16`): `DCS-31`; item 49 de `F-4`; corretivo `CON-T5a` da `OP-5` (i e ii).
- **AE-15** — 2026-09-23 · laudo da `CON-T6` (aprovado 100, `seguir`), laudo preservado em `%TEMP%\claude\laudo-CON-T6.md` · residência fora da `F-4`: `docs/consultant-spec.md` §3, subseção *Ato do dono de 2026-09-22*, parágrafo *Consequência sobre a §2* — *"Enquanto o bloco A não for reescrito, a spec prevalece"* —, caduco desde que as `CON-T3`/`T3a`/`T3b`/`T3c` reescreveram o bloco A. Terceira residência fora da `F-4` achada na execução (com `AE-11` e `AE-14`). **Rota:** consultor, junto com o `AE-14`. · **Fechado** em 2026-09-23 (`AE-16`): `DCS-31`; item 50 de `F-4`; corretivo `CON-T6a` da `OP-6`.
- **AE-16** — 2026-09-23 · acionamento 6 · instância efêmera, Fable por pedido do dono · gatilho 2 (laudos da `CON-T5` e da `CON-T6`, aprovadas 100 `seguir`, com `AE-14` e `AE-15` roteados ao consultor) · **Motivou:** o parágrafo do diário que ainda leva o plano a `blocked` em toda revisão pedida por quem executa (fora da `F-4`); a homonímia "rota" na Regra 8 (item 38); o parágrafo da spec que afirma prevalecer sobre um bloco A já reescrito (fora da `F-4`). · **Classe do impedimento:** partição de `F-4` (`OP-5`, `OP-6`) e coerência de residência (`OP-5`); nenhuma parada de executor; nenhum estado final muda. · **Decidido:** `rota=modelador`; `DCS-31`; teste de saturação (primeiro achado em cada uma das três superfícies) e capacidade × término (três substituições literais) antes de abrir card; dois corretivos, um por operação — `CON-T5a` (`OP-5`: `AE-14` i e ii) e `CON-T6a` (`OP-6`: `AE-15`) —, porque um card materializa uma operação (`G-PLANREADY`, `DCS-4`); fila `CON-T6 → CON-T5a → CON-T6a → CON-T7`; itens 49 e 50 de `F-4` ao modelador por dossiê de conflito, versão 2 pendente reescrita no lugar, com o texto pendente da `OP-5`/`OP-6` e os estados iniciais confrontados antes de declarar que nenhum estado final muda (`AE-13` ii); `Verificação` dos dois cards medida na árvore real, blocos aplicados e revertidos (`8 passed`, `277 passed`). · **Achado de processo:** terceira residência fora da `F-4` em três laudos seguidos (`AE-11`, `AE-14`, `AE-15`). O censo da `F-4` foi Grep de sete termos e falhou nos dois modos possíveis — hit não absorvido (a `:81` do diário casa *replanejamento* e o item 33 enumerou só `:89` e `:102`) e sentido sem termo (a spec diz *figura*, não *consultor*): o censo da superfície foi o elo fraco do planejamento deste plano. Para o `TK-55` (estatística) e para a régua de autoria do `TK-72` (censo por sentido, com leitura do parágrafo vizinho de cada hit, não só por termo). · **Inconclusivo:** re-cópia de *precisa de* nos cards abertos só se a versão 2 vigorar no marco; a entrada da spec no índice (item 43, *"~480 linhas"*) não se re-mede por duas linhas.
- **AE-17** — 2026-09-23 · laudo da `CON-T5a` (aprovado 100, `seguir`), alvo `doutrina`, não bloqueante · o parágrafo novo do diário fecha *"Nas rotas resolve e modelador o plano segue"* sem a ressalva de `estrategico=`, com a qual a **janela** para também nessas rotas (`DCS-28`); quanto ao estado do **plano** não há divergência, medido pelo revisor. **Rota:** sem card — o parágrafo fala do estado do plano, não da janela, e a precondição (`estrategico=` em `resolve`/`modelador`) é mais rara que a do `AE-14`; vai às pendências da entrega de encerramento.
- **AE-18** — 2026-09-23 · laudo da `CON-T6a` (aprovado 100, `seguir`), alvo `dossiê`, não bloqueante · `docs/consultant-spec.md:164-165` (parágrafo *Por que a lacuna existia*, mesma subseção do item 50) afirma no presente que `A3a`/`A3b`/`A3c` "nunca foram revistas", caduco desde a `CON-T3`; e o ponteiro "(estatuto, :3-5)" envelheceu com a `CON-T6`. **Rota:** sem card — a spec é lastro medido, não fonte normativa, e a frase é narrativa de causa do registro histórico que a `CON-T6a` já datou; segunda frase na mesma subseção, precondição mais rara (saturação). Vai às pendências da entrega de encerramento.
- **AE-19** — 2026-09-23 · laudo da `CON-T7` (aprovado 100, recomendação `escalar`, fechado por `A8a`), pendência substantiva roteada pelo `B1` ao consultor · o veredito `adotada` (3 acionamentos, média $2,8, 0 reprovações) repousa em instâncias que rodaram `claude-fable-5-1` por pedido do dono (`DCS-23`), precificadas pelo método publicado (preços Opus) e comparadas ao piso de $3,7 da prontidão medido em Opus; a subseção apensada à §11 da spec não declara o modelo, e o número se lê como custo real da forma. Decidir, antes da `CON-T8` consumir o veredito, se ele vale como medida da forma ou se a subseção recebe a declaração e o veredito muda. Laudo em `%TEMP%\claude\laudo-CON-T7.md`. · **Decidido** (acionamento 7, instância efêmera, Fable por pedido do dono; gatilho 2): `rota=resolve`; `DCS-32` — o veredito `adotada` fica, como medida da forma em tokens, pela regra de `DCS-7` aplicada como está; a subseção recebe a declaração do modelo das instâncias (`claude-fable-5-1`, conferido em todas as mensagens `assistant` dos três transcripts), do $ como preço-Opus-equivalente e da reexecução da sonda na primeira execução com o consultor em Opus; corretivo `CON-T7a` (`OP-7`) entre `CON-T7` e `CON-T8`; `CON-T8` depende da `CON-T7a` e usa o par `adotada`, com a nota de que o parágrafo apensado não muda a última linha da tabela; `Verificação` medida na árvore real, bloco aplicado e revertido (`277 passed`). Sem drift: `OP-7` e o estado final de `consultor.forma da figura` (vigente e pendente) dizem *veredito medido do piloto, gravado na §11 — adotada*, e é o que fica. · **Inconclusivo:** a amostra da forma efêmera em Opus — quanto outro modelo consome de tokens para a mesma decisão — fica para a primeira execução de plano com o consultor em Opus, pela sonda com o filtro daquele cenário (`TK-55` acumula). · **Estratégico:** nenhum. · fechado.
- **AE-20** — 2026-09-23 · laudo da `CON-T8` (ressalva 93, `seguir com ressalva`, fechado por `A8`), laudo em `%TEMP%\claude\laudo-CON-T8.md` · (i) a `description` entregue em `.claude/agents/pantonic-consultant.md:3` diz `Efêmero: cada acionamento` onde o Texto novo 3 manda `Efêmero - cada acionamento`; o `: ` num valor sem aspas **quebra o YAML do frontmatter** — medido pela orquestração: `yaml.safe_load` falha com *"mapping values are not allowed here"* (o do planejador passa); (ii) a `Verificação` do card só casava o prefixo da `description` e não o parse do frontmatter, e saiu verde com o contrato violado; (iii) `kit_check.ps1 -Mode validate` sai 0 com frontmatter que não é YAML válido. **Rota:** (i) e (ii) → consultor, corretivo `CON-T8a` da `OP-8` (término de entrega; regenerar a região gerada no mesmo ato); (iii) → tíquete de instrumento (`kit_check` recusa frontmatter que parser YAML estrito recusa), a abrir no encerramento. · **Decidido** (acionamento 8, instância efêmera, Fable por pedido do dono; gatilho 2): `rota=resolve`; `DCS-33`; corretivo `CON-T8a` da `OP-8`, depois da `CON-T8`, com a `Verificação` medida nos dois mundos na árvore real (parse YAML exit `1` → `0`, drift `0` → `1` → `0`, `check-readme` `0`/`0`, `277 passed`). Só a `description` do consultor carrega o `: `: os outros nove frontmatters parseiam, e o *"Efêmero: cada acionamento"* do `README.md` é célula markdown, fora do YAML. · **Inconclusivo:** o item (iii) — `kit_check.ps1 -Mode validate` recusar frontmatter que parser YAML estrito recusa é capacidade de instrumento, tíquete a abrir pela orquestração no encerramento; sem card aqui. · **Estratégico:** nenhum. · fechado.
- **AE-21** — 2026-09-23 · acionamento 9 · instância efêmera, Fable por pedido do dono · gatilho 4 (marco de fechamento: validação da versão 2 pendente, `GOVERNANCA.md` §3.2) · **Ato:** `rota=resolve`; `DCS-34` — versão 2 **validada**. Diferença a diferença, medida na árvore: (i) `OP-3`, exceção `estrategico=` por rota — **confere**: `.claude/skills/scrum-master/SKILL.md:154` (passo 8, *Triagem*), `:224-226`/`:228`/`:252` (`A3a`..`A3c`, `A6a`, `B1`: *"`planejador` e `estrategico=` PARAM"*), `:259-260` (a ação de `planejador` se executa com ou sem `estrategico=`; `resolve`/`modelador` sem executar a ação e sem despachar o modelador); (ii) `OP-5`, *as regras do diário sobre revisão pedida e transição de estado* — **confere**: `.claude/skills/diario-de-obras/SKILL.md:79-84` (tarefa `blocked premissa`, triagem do consultor, só `planejador` é `blocked` de plano) e `:89`, `:103` (`blocked` → `review` pelo consultor na rota `resolve`); `.claude/global/CLAUDE.md:164-165` (Regra 8 sem a homonímia); `passagem-de-bastao/SKILL.md:239`, `:261`; agentes `pantonic-planner.md:420`, `pantonic-model-designer.md:82`, `pantonic-executor.md:33`/`:119`, `pantonic-reviewer.md:125-126`; (iii) estado final de `consultor.alcance da triagem das paradas`, 50 itens e a exceção — **confere**: `F-4` itens 48-50 no plano `:347-362`; item 48 `scrum-master/SKILL.md:222` (`A1`, cláusula do consultor); item 49 diário `:79-84`; item 50 `docs/consultant-spec.md:167-171` (registro histórico datado, *"a spec não prevalece"*); fontes normativas `scrum-master/SKILL.md:27` e `:216` citam `DCS-3`..`DCS-6`; (iv) partição do objeto `consultor` (`OP-4` +48, `OP-5` +49, `OP-6` +50) e listas `tarefas:` (`CON-T4a`, `CON-T5a`, `CON-T6a`) — **confere**: cards `:3028` (item 49, `OP-5`) e `:3169` (item 50, `OP-6`), `CON-T4a` na `OP-4`; (v) dois estados iniciais (`estatuto`: *"A spec afirmava prevalecer"*, item 50; `alcance`: o diário na revisão pedida e na transição) e lastro `DC-3` (`## 0` `:49`) — **confere** com o texto pré-plano citado nos itens 49 e 50; (vi) contagens `5 · 8 · 12` — **confere**: `modelo.py check` exit 0 (8 operações, 5 objetos, 12 propriedades, 17 tarefas). Sem `## 1`/`## 1A` tocadas, sem promoção: é do dono. · **Inconclusivo:** o parágrafo de leitura da `## 1A` abre com *"Muda só duas coisas"* e a linha 2 da `1.4` diz *"reescrita no lugar duas vezes"* enquanto ambos narram quatro atos — narrativa do bloco, que o modelador reescreve ao promover; `AE-17` (diário sem a ressalva de `estrategico=`) não contradiz a `OP-5` da versão 2, que não afirma isso do diário, e segue como pendência do encerramento.
- **AE-22** — 2026-09-23 · acionamento 10 · instância efêmera, Fable por pedido do dono · gatilho 4 (ato do dono depois do fechamento das 17 tarefas) · **Motivou:** o ato do dono sobre a `OP-3` — *"foi considerado a hipótese que o consultor tem prerrogativa de recusar impedimento autonomamente? Emendar o modelo e ajustar agora"* — e o vão medido pelo condutor: nem o bullet `rota=resolve` do agente (`:25`) nem `A3a`/`A3b`/`A3c` (`:224-226`) nomeiam o **impedimento improcedente**; redespachar o mesmo card sem mudança reproduz a parada num executor frio, e a spec não tem caso de parada improcedente. · **Classe do impedimento:** lacuna de desfecho na triagem (`OP-2`, `OP-3`), por ato do dono; nenhuma parada de executor; drift do estado final de `consultor.alcance da triagem das paradas`. · **Ato:** `rota=modelador`, sem `estrategico=`; `DCS-35` com o ato verbatim e as três amarras; corretivos `CON-T2b` (`OP-2`) → `CON-T3d` (`OP-3`) depois da `CON-T8a`, `Verificação` medida na árvore real nos dois mundos; dossiê `Ato de modelo` de `emenda` na linha de retorno, para a versão 2 pendente reescrita no lugar. · **Inconclusivo:** a versão 2 validada em `DCS-34` muda com a emenda e se valida de novo no marco; `A6a`, `A7` e `B1` ficam fora da recusa (partem de laudo) — parada improcedente vinda de laudo, se a prática a mostrar, é achado novo; a primeira recusa medida na prática é do `TK-55`.
- **AE-23** — 2026-09-23 · laudo da `CON-T2b` (aprovado 100, `seguir`), dois achados de `dossiê`, não bloqueantes · (i) a amarra 1 da `DCS-35` manda a razão da improcedência à coluna `motivo` da estatística, que o agente e o estado final de `consultor.registro dos acionamentos` reservam ao que motivou o acionamento — na recusa a coluna carrega dois fatos; (ii) o `Pronto quando` da `CON-T2b` pendura a fatia em `consultor.fronteira com o planejador`, e a `DCS-35` declara que a emenda muda `consultor.alcance da triagem das paradas`. **Rota:** sem card; (i) vai à residência estruturada da estatística no `TK-55`, (ii) ao `AE-3`/`TK-72`. Pendências da entrega de encerramento.
- **AE-24** — 2026-09-23 · laudo da `CON-T3d` (aprovado 100, `seguir`), alvo `doutrina`, não bloqueante · a saída do passo 8 da skill do loop — "segue (vai ao passo 9)" — não cobre o caminho de redespacho da mesma tarefa sem retentativa (a recusa da `DCS-35` em `A3a`/`A3b`/`A3c`, e o fallback da `A3c`, este anterior ao plano), porque o passo 9 só dispara com a tarefa em `done`. **Rota:** sem card nesta janela (vão pré-existente, janela no teto de ocupação); pendência da entrega de encerramento, candidato a corretivo da `OP-3` na próxima janela.
