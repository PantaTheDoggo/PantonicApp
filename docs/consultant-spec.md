# Especificação do consultor de plano

**Estatuto.** Especificação de uma figura **provisória**. Este documento não é doutrina: não altera
`GOVERNANCA.md`, não cria guardrail `G-*` e não se declara fonte normativa. Promovê-lo a doutrina é
ato posterior, e até lá o consultor de plano permanece figura ad-hoc.

**Método.** Toda afirmação abaixo descreve comportamento **medido** ao longo de quatro instanciações,
não comportamento desejado. Nenhuma recomendação entra sem lastro. Os identificadores do lastro
ficam nas linhas `Lastro` e nas tabelas, nunca no corpo do texto.


**Nota de leitura — três números de série deste documento estão defasados, por decisão registrada
(dono, 2026-09-19).** A série de acionamentos do consultor é incrementada **pelo próprio ato de
escalonar**, inclusive pelos escalonamentos que autoraram e corrigiram este documento. Todas as
contagens abaixo valem no recorte fechado **até o `ESC-36`**; três delas ficaram sem esse recorte e
**não se corrigem aqui**:

- **§10** diz que o empréstimo de autoria de card *"é fato medido **nove** vezes"* — a árvore mede
  **11**, porque a figura autorou mais dois cards depois do `ESC-36`.
- **§6** diz que o plano *"cresceu de 29 para **33** cards numa janela"* — fechou em **35**.
- **§1** atribui as **14** linhas `ESC-23-consultor`..`ESC-36-consultor` à instância do recorte
  `ESC-27`..`ESC-36`, que a tabela da mesma seção conta em **10** acionamentos: as 14 linhas cobrem
  **duas** instâncias, porque a marcação `-consultor` começa no `ESC-23`.

**Por que não se corrigem:** cada correção do censo descobriu uma superfície que o aceite anterior
não alcançava — foram quatro rodadas —, e o teto escrito no `P-0740` encerrou a série. Estas
imprecisões deixam de ser defeito a reparar aqui e passam a ser **estatística da spec de
robustez**, cujo acumulador é o tíquete `TK-55`. As afirmações que sustentam as decisões deste
documento — as quatro instâncias, o censo por recorte, o consumo por papel — estão corretas; o que
está defasado são três contagens de série.

---

## 1. A figura, em uma página

O consultor de plano é o único agente **não efêmero** do kit: é instanciado **uma vez** por
execução de plano, mantido de standby com o cenário inteiro no contexto, acionado a cada
escalonamento e encerrado com o plano. Ele responde com **a decisão e o reparo**, nunca com opções,
porque quem o aciona — o executor pela devolução de um card, o loop pelo roteamento de um laudo —
não decide.

O que o barateia é a **permanência**, não o modelo nem o prompt. Nenhuma das nove passagens da
primeira instância medida releu o plano: cada uma entrou apenas com o delta — o laudo e o retorno
do executor. É esse mecanismo, e não a instrução, que produz a economia da seção 6.

> **Lastro:** `I-1`, `I-2`; definição do agente (`.claude/agents/pantonic-consultant.md`, seções
> *O que você faz* e *Coesão do seu contexto*).

### As quatro instâncias medidas

| instância | acionamentos | consumo da figura | % da janela | recorte | como terminou |
|---|---|---|---|---|---|
| 1ª | 9 passagens | `2.639,1k` tk | **68,5%** de `3.850,3k` | — | decisão de janela, cenário coeso |
| 2ª | 14 acionamentos | `3.802,2k` tk | **63%** de `6.004,3k` | — | queda por limite de sessão, sem resposta |
| 3ª | 4 acionamentos | `857,7k` tk | não medido | `ESC-23`..`ESC-26` | sucessora provisionada após a queda; encerrada por ato do dono no fechamento do marco |
| 4ª | 10 acionamentos | `2.776,3k` tk | não medido | `ESC-27`..`ESC-36` | em curso na medida |

A `1ª` e a `2ª` recebem `—` na coluna `recorte`: precedem a marcação `-consultor` na telemetria (as
linhas `ESC-1`..`ESC-21` não a têm), então o recorte delas não é derivável da árvore, e o ordinal
vem do registro em prosa.

Na 2ª instância, os outros papéis da mesma janela consumiram execução `1.389,9k` (**23%**) e
revisão `812,2k` (**14%**). A instância do recorte `ESC-27`..`ESC-36` passou a ter linha de
telemetria por acionamento, apensada pelo `scrum-master`: são **`14 linhas de telemetria`**
(`ESC-23-consultor`..`ESC-36-consultor`) em `docs/telemetria.tsv`, uma por acionamento — contagem
até o `ESC-36`, recorte que a própria frase declara.

> **Lastro:** `I-1`, `I-9`, `I-10`, `DM-45` (i); `AE-60` (`ESC-27`..`ESC-33`), `AE-63` (`ESC-34`),
> `AE-65` (`ESC-35`), `AE-66` (`ESC-36`); seção `## 10` do plano de origem.

---

## 2. (a) Gatilho — o que aciona e o que não aciona

**O que aciona.** Quatro classes, todas medidas, e nenhuma outra apareceu em 37 acionamentos até o
`ESC-36`:

1. **Card devolvido `blocked` pelo executor** — motivo `premissa` ou `dependencia`. Medido duas
   vezes na mesma tarefa da instância do recorte `ESC-27`..`ESC-36`: nas duas o executor não tocou
   arquivo nenhum, enumerou as saídas possíveis em vez de escolher uma, e nas duas a recusa foi
   conduta correta. O consultor é quem decide; o executor não tinha a quem perguntar.
2. **Laudo com pendência substantiva**, roteada pelo loop. É o gatilho dominante: na 1ª instância
   **toda** pendência substantiva virou passagem.
3. **Impedimento de instrumento que nenhum card cobre.** Medido no primeiro acionamento da
   instância do recorte `ESC-27`..`ESC-36`: o verbo de materialização de status do instrumento de fila estava quebrado para toda
   tarefa de todo plano, por cinco defeitos encadeados, e o loop não conseguia executar o passo que
   a própria condução exige.
4. **Ato do dono no fechamento de marco.** Medido no `ESC-26` — não é despacho do loop nem laudo.

**O que não aciona.** Na 1ª instância, **nada**: nenhum critério de não-acionamento foi medido, e a
figura absorveu tudo que a fila lhe entregou. As duas regras de contenção que existem hoje foram
medidas na instância do recorte `ESC-27`..`ESC-36` e são **de saída, não de entrada** — elas não
impedem o acionamento, elas impedem que o achado vire card:

- **Teste de saturação.** *Uma superfície satura quando o achado seguinte exige precondição mais
  rara que o anterior e o veredito do instrumento se manteve correto em todos os mundos medidos.*
  Declarado sobre um guarda em que quatro de sete escalonamentos consecutivos terminaram; matéria
  nova sobre a superfície saturada acumula em tíquete posterior, e não abre card. Posteriormente
  estendido, pelo mesmo teste, a mais duas superfícies.
- **Capacidade × término.** Matéria que **acrescenta capacidade** não abre card no plano corrente;
  matéria que **termina entrega já aberta** abre. A distinção é verificável, não estilística: no
  segundo caso nada se acrescenta ao artefato e nenhum veredito sobre a árvore de hoje muda.

O diagnóstico que produziu as duas regras é do próprio papel: a figura vinha **convertendo cada
achado em card**, e isso é defeito de processo do consultor — não do loop e não da revisão.

> **Lastro:** `I-7`; `AE-47`/`ESC-27`, `AE-56`/`ESC-31`, `AE-58`/`ESC-32`, `AE-60`/`ESC-33`,
> `AE-62`/`AE-63`/`ESC-34`, `AE-64`/`AE-65`/`ESC-35`; definição do agente, item 2 de
> *O que você faz*.

---

## 3. (b) Domínio de decisão — o que ela fecha e o que sobe

**Fecha sozinha: técnico e tático — que é quase tudo.** Nas nove passagens da 1ª instância a
classificação saiu técnica ou tática em **todas**, e **nada** subiu como decisão. Nos dez
acionamentos da instância do recorte `ESC-27`..`ESC-36` cada decisão veio com a classificação
**declarada no próprio registro**,
e todas saíram não estratégicas.

**Sobe: o estratégico, e só ele.** O critério ficou fixado na instância do recorte
`ESC-27`..`ESC-36`, na primeira vez em que
a pergunta apareceu de verdade: *estratégico é o que muda escopo ou rota do plano, ou revoga/emenda
decisão do dono*. Dele decorre a distinção que evitou uma falsa escalada: **decidir sobre uma
diretiva não é emendá-la** — executar uma diretiva cuja condição de suspensão ainda não se cumpriu
é cumpri-la, não alterá-la. E a leitura é pela **substância** da condição, não pelo rótulo que a
diretiva usou para nomear o veículo esperado.

**Como sobe.** Nunca por interrupção. O que chega ao dono é **relatório de encerramento** — e,
quando há matéria diferida, a **oferta com o custo já medido**, para que a decisão dele não comece
fria. Ato do dono não é decisão da figura: na 1ª instância o que subiu foi relatório e um ato de
permissão, que é outra coisa.

**Onde a figura não decide.** Ela não julga entrega — o veredito é da revisão, pelo gerador — e não
commita: o commit acontece nos marcos de validação, por ato do loop.

> **Lastro:** `I-4`; `AE-56`/`ESC-31`, `AE-58`/`ESC-32`, `AE-60`/`ESC-33`, `AE-63`/`ESC-34`,
> `AE-65`/`ESC-35`; `G-NOASK` (`GOVERNANCA.md` §7 item 18); definição do agente, seção
> *O que você não faz*.

---

## 4. (c) Fronteira com o planejador — e o veredito sobre autoria de card

A definição da figura enumera o que ela faz com o plano: **decisão nova com identificador, cards
reescritos, fila reordenada, achado absorvido com ponteiro**. Medido, a prática ficou **fora** dessa
enumeração em um ponto, e dentro dela em todos os outros.

**O que ficou dentro, e é da figura:**

- **Reescrever card aberto.** Exercido repetidamente: reescrita de bloco de aceite, troca de campo,
  acréscimo de linha de verificação, mudança de esforço declarado, reordenação de fila. Inclui o
  caso mais forte medido — **trocar o produto de um card aberto** (de transcrição para decisão),
  devolvendo-o a `ready` por ato de replanejamento.
- **Reparar instrumento do loop com código.** Medido no primeiro acionamento da instância do recorte
  `ESC-27`..`ESC-36`: cinco defeitos encadeados corrigidos, quatro testes funcionais novos, suíte
  de `187` a `191`. A
  definição já reserva à figura exatamente essa escrita — *a que o próprio reparo exige e que
  nenhum card cobre, declarada no plano como tal* — e foi assim que ela saiu.
- **Recusar-se a editar o artefato que é alvo de um card aberto.** Medido: em vez de corrigir a
  norma diretamente, a figura **emendou o card** que já era dono do arquivo. Editá-la teria
  quebrado o card.

**O que ficou fora: autorar card novo.** A figura autorou cards novos em duas instâncias — quatro
na 1ª, mais as partições de dois cards em três; quatro na instância do recorte `ESC-27`..`ESC-36`,
que levou o plano de 29 a 33 entregas até o `ESC-36`. **Veredito: é empréstimo, não atribuição da figura.** Três fatos o sustentam, e nenhum
deles é preferência: a definição enumera *cards reescritos* e não *cards novos*; autorar card é ato
de planejamento; e nenhuma regra autoriza o empréstimo — a prática existe como fato medido, sem
norma. Este documento **registra o empréstimo e não o promove**: convertê-lo em atribuição da
figura é o ato posterior que a torna doutrina.

**A fronteira que se sustentou em 37 acionamentos até o `ESC-36`:** a figura **nunca reabriu o
objetivo do plano**.
É a única linha que nenhuma instância cruzou, e é ela — não a autoria de card — que separa a figura
do planejador na prática.

> **Lastro:** `I-3`, `I-5`; `AE-47`/`ESC-27` (reparo de instrumento), `AE-49`/`ESC-28` (emenda de
> card em vez de edição do artigo alheio), `AE-51`/`ESC-29`, `AE-54`/`ESC-30`, `AE-58`/`ESC-32`
> (cards novos), `AE-63`/`ESC-34` (partição), `AE-65`/`ESC-35` (troca de produto), `AE-69`
> (achado de divergência, fechado por veredito); definição do agente, item 3 de *O que você faz* e
> 1º bullet de *O que você não faz*.

---

## 5. (d) Instrumento — por que a figura nasce com execução de comando

A figura nasce com acesso a execução de comando (`Bash`), ao lado de leitura, busca e edição
(`Read`, `Glob`, `Grep`, `Write`, `Edit`). Não é conveniência: é a condição de exercício do papel.

A regra que a obriga é **comando de aceite não se deduz, se roda** — quem repara plano publica no
card o comando que **colou e rodou**, com o código de saída que viu, e não uma transcrição dele.
Papel de reparo de plano sem ferramenta de medida reproduz a classe de defeito em que o literal
publicado no card não é o literal executado.

Medido, o instrumento foi usado em quatro modos distintos, e cada um deles decidiu um escalonamento:

1. **Rodar o gate antes de publicar** — três fechamentos consecutivos da 1ª instância dependeram
   disso; em cada um, comandos extraídos do card e rodados verbatim pegaram literal corrompido ou
   piso vencido antes do despacho.
2. **Reparar código e provar o reparo** — suíte de `187` a `191`, verbo de fila de volta a exit 0.
3. **Provar que uma alternativa de desenho existe, antes de descartá-la** — uma fronteira de
   evidência por árvore foi construída e medida com o índice real intocado, o que dissolveu um
   falso dilema entre duas rotas caras.
4. **Confrontar o que o card prescreve com a árvore de hoje** — varredura de todos os caminhos
   citados pelos cards estacionados de outro plano: dois alvos mortos, exatamente, e três ausências
   que **não** eram alvo morto.

O modo 4 é o que sustenta a regra: sem execução de comando, a figura escreveria cards contra uma
árvore que ela supõe, e o custo cairia no executor como bloqueio.

> **Lastro:** `I-6`, `DM-12`, `DM-24`; `AE-7`, `AE-19`; `AE-47`/`ESC-27`, `AE-56`/`ESC-31`,
> `AE-65`/`ESC-35`; definição do agente, campo `tools` e item 3 de *O que você faz*.

---

## 6. (e) Custo e teto — a série, e quando não acionar

**O número é série, não constante.** Duas janelas medidas: **68,5%** e **63%** do consumo total
concentrados num papel só. A queda de 5,5 pontos não autoriza ler tendência — autoriza ler que o
valor se move e que publicar qualquer um dos dois como constante envelheceria.

**O que a figura economiza.** O regime que ela substituiu eram rodadas **frias** de planejador:
quatro delas custaram `423,7k` tk para fechar **uma** tarefa, redescobrindo o mesmo cenário a cada
vez, e três das quatro consertaram o mesmo defeito por manifestações diferentes. Com a figura, a
janela seguinte fechou **oito** tarefas a `481,3k`/tarefa contra `625k`/tarefa da anterior.

**O que ela custa.** Medido sobre 21 módulos de um piloto, na base executor + reviewer, o módulo
sai a `176,8k` tk / `52,3` tool uses / `8,8` min — **37,9% abaixo** da baseline de tarefa atômica em
tokens, **26,3% abaixo** em tool uses, **57,9% abaixo** em duração. Somando o papel que a baseline
não tinha, o mesmo módulo sai a `524,0k` — **84,1% acima** da baseline.

Os dois números são o mesmo fato visto de dois lados, e é assim que a figura tem de ser lida: **ela
barateia o módulo e encarece a janela.** Nenhum dos dois lados a condena ou a absolve sozinho.

**Contra o quê ela se paga.** A janela de 63% fechou 11 módulos com **zero reprovações e zero
retentativas**; a de 68,5%, oito módulos com zero reprovações e zero refações. O consumo do papel
compra ausência de retrabalho, e é contra isso que ele se mede.

**Quando não acionar.** Não existe critério de entrada medido: a 1ª instância roteou toda pendência
substantiva à figura, sem teto. Os dois tetos que existem agem na saída, estão descritos na seção 2
e foram declarados no registro do plano para não dependerem de ninguém lembrar. A leitura correta
da série de acionamentos que os motivou não é "o plano descobre escopo mais rápido do que fecha", e
sim "gasta-se profundidade de inspeção num artefato secundário" — três fatos a sustentam: o plano
cresceu de 29 para 33 cards numa janela, quatro dos cinco cards novos foram autorados pela figura
sob escalonamento, quatro dos sete escalonamentos do período terminaram no **mesmo** arquivo, e no
mesmo intervalo dez tarefas fecharam sem uma única reprovação.

> **Lastro:** `I-1`, `I-7`, `I-10`, `DM-23`, `DM-45` (i); `AE-21`, `AE-56`/`ESC-31`,
> `AE-58`/`ESC-32`, `AE-60`/`ESC-33`; seção `## 10` do plano de origem (baseline `BKL-T4`).

---

## 7. (f) Encerramento — decisão de janela × poluição

A figura atravessa **um plano**. Troca de plano é troca de cenário: a instância é encerrada e outra
nasce para o plano seguinte. O limite de formato é esse — **a troca de plano, não a duração**.

**Modo medido de encerramento: decisão de janela, com o cenário intacto.** As nove passagens da 1ª
instância couberam num contexto **coeso** do começo ao fim — um plano, um cenário. A última fechou o
cenário e o relatório subiu. Nenhuma instância medida encerrou por poluição de contexto.

**Poluição, o modo previsto e não exercido.** A regra vinculante existe e é a geral: entrando
material de outro plano, ou um fato que derrube a premissa já usada para decidir, a figura **para e
declara a poluição** ao loop, em vez de seguir remendando. Zero ocorrências medidas — o que
significa que este caminho de recuperação **não está exercitado**, e não que ele seja desnecessário.

**O modo que não é encerramento.** A queda por limite de sessão não encerra a figura: mata-a. É
matéria da seção 8, e a distinção importa porque o encerramento devolve o cenário e a queda o
perde.

> **Lastro:** `I-8`, `I-9`; `CLAUDE.md` global, Regra 2; seção `## 10` do plano de origem (regra de
> parada por janela); definição do agente, seção *Coesão do seu contexto*.

---

## 8. (g) Fim de vida por limite, e a sucessão

**O fato que define o problema.** A 2ª instância terminou por limite de sessão **sem devolver
resposta**: duas alocações pendentes e uma varredura final ficaram por fazer, a notificação veio sem
bloco de consumo, e nenhuma linha de telemetria foi apensada — porque telemetria é medida, não
estimativa. O que se perdeu **não foi trabalho entregue**: os achados estavam registrados e a tarefa
em curso seguiu por medida própria do gate. Perdeu-se o **contexto acumulado de 14 acionamentos**,
que é justamente o ativo que justifica a figura existir — ela não é efêmera por desenho.

Por isso: **a ausência de fim de vida é defeito estrutural da figura, não incidente.**

**A regra de sucessão, e ela é vinculante.** Ao perceber que se aproxima do próprio limite, o
consultor **promove handover**, entregando três coisas:

1. o **estado do cenário** acumulado;
2. os **escalonamentos abertos**;
3. **o que estava em curso** no momento.

O loop então **descomissiona a instância e provisiona outra**, repassando esse handover. A sucessão
é ato de quem conduz, não da figura: ela entrega o handover, não escolhe o sucessor.

**A forma de comunicação do handover.** Ela é, hoje, **ad-hoc** — a regra nomeia o *conteúdo* e não
a *forma*, e nenhuma instância a exerceu. Este documento fixa a forma no único estado em que ela foi
medida: **ad-hoc, não projetada e portanto não normativa**, até ser desenhada em plano próprio.
Enquanto isso durar, a forma praticada não se cita como precedente — é insumo, não doutrina.

> **Lastro:** `I-9`, `DM-45` (iii), `DM-28`; `ESC-22`; `GOVERNANCA.md` §4.2 (telemetria é medida).

---

## 9. (h) Estatística do próprio acionamento

**O fato que define o problema.** Duas janelas em que um papel só concentrou a maior parte do
consumo — 68,5% e 63% — **sem nenhum registro estruturado de causa**. O arquivo de telemetria
registra **quanto** cada acionamento custou e nada sobre **por que ele existiu**, que classe de
impedimento o motivou ou o que ficou em aberto ao fim dele. Sem isso, a especificação de robustez
da figura seria autorada sobre impressão.

**O que se coleta.** A cada acionamento, três campos:

1. **o que o motivou** — a pendência, o bloqueio ou o impedimento concreto;
2. **que classe de impedimento era** — a categoria, não a narrativa;
3. **o que ficou inconclusivo** — o que a decisão deliberadamente não fechou.

O produto acumulado dos três é o **panorama dos pontos inconclusivos**.

**Onde mora.** Hoje, ad-hoc: o registro vive em **prosa, no bloco de achados do plano**, um achado
por acionamento — forma que a tabela abaixo reconstrói inteira, o que prova que a informação existe e
que o que falta é **estrutura**, não matéria. O arquivo de telemetria segue sendo a residência do
**custo**, e a figura passa a apensar linha a ele. Uma residência projetada **não se fixa aqui**: é
matéria do plano próprio, pelo mesmo motivo da seção 8.

**Quem lê.** Destino declarado: **insumo direto da especificação de robustez** da figura. É o
consumidor nomeado, e é dele que vem a exigência de coletar a causa e não só o custo.

### Panorama medido dos dez acionamentos da instância do recorte `ESC-27`..`ESC-36`

| acionamento | o que motivou | classe do impedimento | o que ficou inconclusivo |
|---|---|---|---|
| `ESC-27` | verbo de materialização de status quebrado para toda tarefa de todo plano | instrumento do loop, nenhum card cobria | casamento por id no bloco de fila gerado e a definição de "pai vivo" (regra ingênua emitiria 12 bullets, 10 deles lixo); verbo de próxima tarefa em exit 3 por motivo pré-existente |
| `ESC-28` | linha de aceite reprovada três vezes pelo gate, sempre por baseline de corpus e nunca por defeito de entrega | contradição entre norma e instrumento | exigência **mecânica** no gate não implementada; dois arquivos com fim de linha divergente do declarado |
| `ESC-29` | duas frases de prosa falsas fora do alcance do guarda; regra ausente de três enumerações da própria skill | cobertura de instrumento | nenhum registrado |
| `ESC-30` | contrato de razão assimétrico entre leitor e escritor; classe da enumeração reproduzida no ato de fechá-la | contrato aberto pelo card anterior | a generalização *todo guarda que conta é ele próprio superfície contada*, roteada a tíquete; nenhum critério novo na norma |
| `ESC-31` | recorte do dossiê de evidência não discrimina autoria dentro do arquivo | divergência entre norma e prática | fronteira de evidência sem commit: **desenhada e medida, não construída** — diferida a tíquete posterior |
| `ESC-32` | terceira reincidência da classe de aceite por presença, em três cards consecutivos | técnica de autoria | exigência mecânica no gate (recusar bloco de aceite feito só de contagem de presença) diferida; item fantasma por decimal em prosa, reproduzível |
| `ESC-33` | acoplamento de escopo num guarda, com falha de diagnóstico e veredito correto | capacidade, não término | reparo **desenhado e verificado, não aplicado**; teto de saturação declarado sobre a superfície |
| `ESC-34` | card mandava executar uma partição que ele não decidira (1º bloqueio) | decisão de planejamento ausente | resíduo de contagem e citação por faixa de linha, sob o teto estendido a duas superfícies novas |
| `ESC-35` | matéria a reagrupar aponta para superfícies que o próprio plano destruiu (2º bloqueio) | interferência entre planos | transcrição dos três módulos diferida para a retomada do outro plano, com a árvore parada |
| `ESC-36` | colisão de identificador na nota da decisão; achado não reconciliado em plano estacionado | autoria em plano estacionado | **aberto no momento da medida** — sem achado de retorno registrado |

**Três leituras que a tabela sustenta, e nenhuma delas é visível na telemetria de custo.** Primeira:
**quatro dos dez acionamentos terminaram no mesmo arquivo periférico** — concentração invisível a
quem só vê o total. Segunda: **sete dos dez deixaram matéria inconclusiva diferida**, e o valor
delas está em já virem com desenho medido, para que quem as planeje não comece frio. Terceira: a
classe mais cara de acionamento não é a de defeito de redação de card — é a de **decisão ausente**,
em que o executor devolve o card sem tocar arquivo. A tarefa que voltou bloqueada duas vezes custou
três despachos, e **o que a destravou não foi refinar o card: foi trocar o produto dele.**

> **Lastro:** `I-10`, `DM-45` (iv), `DM-28`; `AE-47`/`ESC-27`, `AE-49`/`ESC-28`, `AE-51`/`ESC-29`,
> `AE-54`/`ESC-30`, `AE-56`/`ESC-31`, `AE-58`/`ESC-32`, `AE-60`/`ESC-33`, `AE-63`/`ESC-34`,
> `AE-65`/`ESC-35`, `AE-66`/`ESC-36`.

---

## 10. O que esta especificação não fecha

Registrado para que o plano próprio não comece frio, e **sem rota decidida aqui**:

- **A forma do handover de fim de vida** (seção 8) — o conteúdo está fixado, a forma é ad-hoc.
- **A residência estruturada da estatística de acionamento** (seção 9) — a matéria existe em prosa;
  a estrutura, não.
- **A norma sobre autoria de card novo** (seção 4) — o empréstimo é fato medido nove vezes, e
  continua sem regra que o autorize ou o proíba.
- **O critério de não-acionamento na entrada** (seções 2 e 6) — os dois tetos medidos agem na
  saída; nenhum critério de entrada foi exercido.
- **O caminho de poluição de contexto** (seção 7) — previsto, vinculante, zero ocorrências, não
  exercitado.
- **A forma da figura — standby ou efêmera com cenário persistido** (seção 11) — a medida de custo
  por acionamento reabre a premissa de que o standby entrega continuidade barata; o plano próprio
  decide a forma **por piloto medido**, não por argumento.
- **A disciplina de saída** (seção 11, item iii) — `Edit` mínimo em vez de `Write` de seção;
  hoje é recomendação, não regra.

> **Lastro:** `I-5`, `I-7`, `I-9`, `I-10`; `DM-28` (o ad-hoc é insumo, não precedente).

---

## 11. (i) Custo por acionamento — a medida que reabre a forma da figura

**O fato.** Medido em 2026-09-19 sobre os transcripts de cinco instâncias (deduplicados por
`message.id`; preços da skill `claude-api`: Opus $5/M entrada, $25/M saída, cache read 10%, cache
write 125%):

| instância | turnos | ctx final | duração | custo | reescrita de cache | releitura de cache | saída | acionamentos | $/acionamento |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 171 | 405k | 151 min | $39,5 | **$15,4 (39%)** | $17,9 | $6,2 (247k tk) | 9 | $4,4 |
| 2 | 188 | 452k | 252 min | $52,2 | **$25,3 (48%)** | $19,2 | $7,7 (307k) | 14 | $3,7 |
| 3 | 124 | 320k | 114 min | $22,6 | $7,3 (32%) | $10,7 | $4,6 | 5 | $4,5 |
| 4 | 114 | 280k | 115 min | $17,3 | $4,4 (25%) | $8,6 | $4,3 | 4 | $4,3 |
| 5 (morta por limite, seção 8) | 233 | — | 209 min | sem `usage` | 3,5M tk reescritos (~$22) | — | 268k tk | 15 | — |

**A causa da coluna "reescrita de cache".** O cache de prompt de um **subagente** expira em **5
minutos**; o da sessão principal, em **1 hora**. Todo pico de `cache_creation` acima de 30k tokens
nas cinco instâncias ocorre após pausa ≥ 5 min (gaps medidos: 5, 6, 7, 7, 8, 8, 8, 10, 11, 12, 13,
15, 16, 17, 18, 20, 21, 23, 35, 55 min); o maior gap **sem** pico é 4,3 min. Entre dois
acionamentos correm executor e reviewer (10–20 min). Logo **cada acionamento reescreve o contexto
inteiro a preço cheio** — a continuidade "no contexto", que é a razão de ser do standby (seção 1),
é paga integralmente a cada chamada, e cresce com a curva 258k → 451k.

**As três outras fatias.** Releitura de cache: `turnos × contexto × $0,50/M` — 36–45% do custo,
com 13–28 turnos por acionamento e 1,0–1,2 chamadas de ferramenta por turno (sem batching). Saída:
12–16%, e 16–65k tokens dela são payload de `Write` de seção inteira do plano. Leitura: 8%, e 57%
dela é o próprio plano (`P-0740`: 8.465 linhas, ~178k tokens) — a "absorção do cenário" da seção 1
é lida por faixas, várias vezes.

**O que a medida decide e o que deixa ao plano próprio.**

- **(i) Forma da figura.** A alternativa medida contra o standby é a **figura efêmera com cenário
  persistido**: a cada acionamento nasce uma instância que lê `docs/plans/<plano>-CENARIO.md` (≤ 15k
  tokens: decisões vivas, fila, achados abertos, matéria inconclusiva da seção 9), lê o card em
  causa, decide, **reescreve o cenário** e encerra. Custo estimado por acionamento: prefixo 17k +
  cenário 15k + leituras dirigidas 20k reescritos ($0,3) + ~15 turnos a ~70k ($0,5) + saída ($0,4)
  ≈ **$1,2–1,5**, contra $3,7–4,5 medidos — e sem fim de vida por limite (seção 8) nem curva de
  crescimento. O que se perde é o que a instância anterior não escreveu no cenário; o handover da
  seção 8 vira o modo normal, não o de fim de vida. **Decisão: por piloto de uma janela**, medindo
  `$/acionamento`, reprovações e retentativas contra as instâncias 1–4 (que fecharam com zero
  reprovações). Uma instância efêmera **não lê o plano**: lê o cenário e o card; o cenário é
  autoridade sobre o plano para o que ele cobre.
- **(ii) Manter o standby aquecido** (ping a cada ≤ 4 min via `SendMessage` enquanto executor e
  reviewer rodam; ping = releitura de 300k = $0,15, contra $1,9 de reescrita) é remendo: exige o
  loop acordado durante o despacho, põe turno e conteúdo no contexto da figura e não resolve a
  curva nem a morte por limite. **Só se (i) for recusada pelo piloto.**
- **(iii) Disciplina de saída.** `Edit` mínimo em vez de `Write` de seção; resposta curta como a
  definição já manda. Ganho ~12–16% do custo da instância, sem drawback. Vale para qualquer forma.
- **(iv) Critério de entrada do acionamento** (seções 2, 6, 10): continua aberto e **não se decide
  por custo** — decide-se pela estatística estruturada da seção 9, que ainda não existe. A medida
  só acrescenta o preço de cada acionamento (~$4) ao lado da causa.

**Onde a figura fica no custo do plano.** Consultor ≈ 35% de um plano de ~$500; sessões
principais ≈ 40%; executor + reviewer ≈ 18%. As alavancas fora da figura (loop em Sonnet, janela
curta, loop fora do LLM) estão em `docs/plans/_VIABILIDADE-agente-leitor.md` §7 e em tíquetes
próprios; **nada delas altera esta especificação** — o que altera é (i)–(iv).

> **Lastro:** `docs/plans/_VIABILIDADE-agente-leitor.md` §7.1–7.4 (medida e posição);
> sonda descartável `%TEMP%\claude\sonda_leituras.py`; seções 6, 8 e 9 desta especificação.
