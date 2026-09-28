# P-0748 — A tela do gerente: o fluxo da execução em linguagem humana

**Data:** 2026-09-23 · **Origem:** pedido do dono em 2026-09-23 (transcrito na §0), recebido via
orquestrador da sessão · **Plano de origem:** nenhum (plano novo; iniciativa *acompanhamento da
execução pelo gerente do projeto*) ·
**Status:** `done` · 2026-09-24 — **Marco 3 fechado com o aceite do dono** (17/17 tarefas `done`; versão 4 do modelo vigente; validação em `docs/OPERACOES_AS_IS_P-0748.md`). Antes: acionamento 16 do consultor (`DTG-52`) deixou a última tarefa, `TLG-T3h`
(corretivo da `OP-3`, `AE-25`/`AE-26`), depois o relatório de encerramento com o aceite de confiabilidade e a versão 4
pendente da `## 1A`, cuja promoção a `## 1` é ato do marco. Histórico: rodada de replanejamento 2 do planejador fechada
(`DTG-30`..`DTG-38`, `RP-2`) sobre a versão 3, então pendente (`DTG-29`, ato do dono sobre corpus real); rodada 1 (`DTG-20`..`DTG-28`); Marco 1 com `go` do dono em 2026-09-23 (juízo de viabilidade delegado ao
condutor da sessão: *"O marco é você me dizer se é viável ou não. Se for viavel, continue"*;
veredito: viável, defaults dos quatro pontos aplicados). `python .claude/tools/modelo.py check
--plano docs/plans/P-0748-tela-do-gerente.md` sai `0` ·
**Prefixo das tarefas no diário:** `TLG-T<n>` (para `OP-<n>`) ·
**Prefixo das decisões:** `DTG-<n>` · **Checagem de versão do kit:** modo hub — congelada em
`0.0.0` (`GOVERNANCA.md` §10), nada a comparar · **Branch de trabalho:** a que o dono indicar no
despacho; até lá, a corrente (`plan/planner-modelo-escopo`).
**Modelo de planejamento:** Fable 5.1 (modelo ativo da sessão de 2026-09-23).

*(Histórico da versão 1 — superado pela medida da `### 2.2` (veredito `não` na extensão), pela
decisão do dono em `DTG-12` e pela rodada do planejador de 2026-09-24 (`DTG-20`..`DTG-28`): a tela
passa a ser o painel fora da extensão, alimentado pelo arquivo de progresso.)*

**Veredito preliminar de viabilidade (a confirmar pela sonda `OP` de viabilidade, ver `DTG-3`):
sim, com uma restrição.** O que o dono pede — uma linha em linguagem humana por transição
(tarefa, passo, agente, veredito) — é texto escrito pelo agente que conduz o loop, e texto do
agente é o único canal que a extensão VS Code renderiza inteiro e sem recolher (`F-1`). O que o
dono quer **retirar** — resultados de `Grep`, avisos de leitura — não se apaga da tela por
configuração conhecida do harness (`H-2`, a apurar): o caminho viável é **deslocar** essas
chamadas para dentro dos subagentes, cujas chamadas internas a extensão recolhe sob a linha do
despacho (`H-3`, a apurar), e reduzir a zero as chamadas de ferramenta que o próprio orquestrador
faz no topo entre um despacho e outro. O `PantonicMonitor` não é tela: é uma ferramenta de
consumo de disco (`F-5`) e fica fora do escopo (`DTG-1`).

**Marcos de validação pelo dono:**

| marco | o que o dono lê | veredito |
|---|---|---|
| **Marco 1** | a `## 1. Modelo conceitual` deste plano, escrita pelo modelador: os objetos do pedido (stream de dados, tela do monitor, tarefa, mente do agente), o estado inicial e final de cada propriedade, e a lista de operações — em particular a operação de viabilidade, que é a primeira, e a de validação final, que é a última. **Quatro pontos a conferir no mesmo ato** (levantados na Fase 3b): (1) a **forma** do repertório de mensagens — worked example `A` contra alternativa `B` na `### 4.1`; o default aplicado nos cards é `A`; (2) a leitura de *"passo Y"* do exemplo do dono como **passo do loop** (despacho, revisão, fechamento), e não como passo interno do card — é o que o condutor tem em mãos (`I-3`); (3) `OP-5` (a porta de entrada do repositório como validação final) tem lastro fraco no enunciado: nasce da regra `G-README` dever 2 e de `DTG-6`, não de frase do dono — confirmar que a revisão do `README.md` é o corpus do Marco 3; (4) `OP-1` roda **no topo da sessão, com o dono presente e uma reabertura da sessão** (`DTG-14`) — confirmar disponibilidade | `go` 2026-09-23 — o dono delegou o marco ao condutor, verbatim: *"O marco é você me dizer se é viável ou não. Se for viavel, continue"*. Veredito do condutor: **viável** — as linhas do repertório são texto do agente, o único canal que a tela mostra inteiro; o ruído do topo cai pela fusão em `loop.py` (`DTG-11`), que não depende de a extensão recolher chamadas de subagente; resíduo conhecido: cada chamada que resta no topo deixa uma linha-resumo recolhida, que nenhuma configuração remove. `TLG-T1` segue como medição que confirma (Marco 2, `I-4`). Pontos: (1) forma `A`; (2) passo do loop; (3) `README.md` é o corpus do Marco 3; (4) dono presente no `TLG-T1` |
| **Marco 2** | o **agregado da sonda de viabilidade** (a tabela mecanismo → observado sim/não, `DTG-3`), com o veredito `sim`/`não` e, se `não`, a única alternativa fechada da `## 8` (`R-1`) | `go` 2026-09-24 — veredito de viabilidade `não` na extensão (`### 2.2`: (b) mostrou as quatro chamadas no topo); o dono escolheu a alternativa de `R-1`, verbatim: *"Registre 2. Eliminar esse resíduo é exatamente o objetivo deste plano"* (`DTG-12`); e aceitou a versão 2 da `## 1` (tela num painel fora da extensão, arquivo de progresso gravado por gancho do kit), verbatim, em 2026-09-24: *"Sim, é o que eu disse, então está aceito por default"* (`### 1.4`, validação do consultor em `DTG-19`). Rodada do planejador sobre a v2: `DTG-20`..`DTG-28` |
| **Marco 3** | o **painel fora da extensão** — o terminal integrado do VS Code mostrando `.claude/estado/progresso.txt` (`DTG-27`) — durante a execução da **última tarefa deste plano** (a revisão do `README.md`, `TLG-T5`), conduzida pelo loop já modificado: cada linha do painel é **gerada por `progresso_hook.py`** a partir do evento da transição (`DTG-30`), com o **título** da tarefa e do plano no lugar da sigla (`DTG-33`) e a frase da coleta de evidência dizendo o que se coleta (`DTG-35`); o dono lê o fluxo em linguagem humana e diz `go`/`no-go` — é a "validação final" do pedido, com corpus real e não fixture (`DTG-6`). Nenhuma reabertura de sessão é necessária: o gancho carrega na própria sessão (`AE-6`). No mesmo ato o dono valida a versão 3 da `## 1A` (promoção `## 1A` → `## 1`) | **antecipado sobre corpus real em 2026-09-24** (`DTG-29`): o dono leu no painel a janela que fechou `TLG-T3`, `TLG-T2a` e `TLG-T4` e deu o veredito *"convergindo"* com três correções — linha gerada por função, agregação do título, frase da evidência —, absorvidas pela versão 3 da `## 1A` e pela rodada 2 (`DTG-30`..`DTG-38`). O veredito final segue **pendente**, sobre a `TLG-T5` · **Versão 3 do modelo aceita pelo dono em 2026-09-24** (*"Aceito."*, sobre o modelo, `DTG-30`..`DTG-38` e o worked example da `### 4.1`) — promovida a vigente; o veredito final do Marco 3 segue pendente na `TLG-T5` · **Fechado em 2026-09-24.** Primeira leitura (`DTG-42`): forma aceita, confiabilidade não — *"Acho que a forma está ok, mas ainda precisa de uns ajustes na confiabilidade"*; os desvios mapeados foram corrigidos pelos corretivos `TLG-T3c`..`TLG-T3h` e `TLG-T5a` (`DTG-42`..`DTG-52`). Veredito final, verbatim: *"Vamos aprovar esse plano e ver ele ocorrendo na prática."* e *"Aceite os planos, revise os tiquetes para ver quais são pertinentes ainda para enfileira-los na sequencia"* — aceite da confiabilidade, do fechamento e da versão 4 do modelo (promovida a vigente pelo modelador). Documento de validação: `docs/OPERACOES_AS_IS_P-0748.md`. O plano fecha `done` 17/17 |

---

## 0. O problema, verbatim

Pedido do dono, 2026-09-23, nas palavras dele:

> eu queria um novo plano de melhoramento do framework.
> Qual é o meu problema: enquanto as tarefas do plano são executadas, a tela fica renderizando
> mensagens sem valor ao gerente do projeto. Por exemplo, resultados de grep. Avisos que está
> sendo lido algo.
> Nada disso importa, e faz o gerente de projeto se afastar do acompanhamento do plano pela
> quantidade de informação inutil sendo apresentada.
> O sucesso de uma iniciativa tem a ver com quão próximo o gerente de projeto acompanha cada
> passo, e tenha total consciencia do que está ocorrendo em real time para poder intervir e
> sanar problemas tempestivamente.
> Isso acima é o contexto do problema. Abaixo, o modelo que vou fornecer como v0 para o model
> designer melhorar (se necessário).
> Objetos de escopo:
> - stream de dados: fila onde são inseridas as mensagens que serão renderizadas.
> - Estado inicial: o stream parece ligado aos greps e outros comandos de saída. Estado final
>   será o stream de dados conectados à tarefa e ao pensamento do agente. Os demais fluxos de
>   dados podem ser descartados.
> Objetos de medição
> - tela do monitor: lugar onde são apresentados todas as mensagens renderizadas.
> - O estado inicial da tela são mensagems de grep e leitura. O estado final dela são mensagens
>   indicativas do progresso atual da tarefa e pensamentos sendo desenvolvidos pelos agentes.
> Objetos externos:
> - Tarefas: apresentam o cabeçalho e a sequencia de passos.
> - mente do agente: apresentam a forma como o agente compreende o passo atual.
> Exemplo de tela que eu espero receber ao término do plano:
> - Tarefa X, passo Y.
> - Agente executor receber passo Y e irá executar Z.
> - Agente consultor receber a execução Z e irá confrontar com Y.
> - Agente consultor aceitou a entrega.
> - Scrum master concluiu a tarefa X e irá pegar a tarefa X2.
> Veja a viabilidade desse plano.
> Espero as seguintes entregas:
> - Viabilidade (sim, não).
> - Bloqueio de saídas sem valor.
> - Template de mensagens possíveis de serem renderizadas
> - Modificação do stream de dados para renderização
> - Validação final onde eu poderei ver o desenvolvimento do plano em linguagem humana, e não
>   como saídas de comandos

**O que o plano entrega quando termina (critério de pronto do plano):** o dono acompanha a
execução de qualquer plano deste repositório lendo, na tela da extensão VS Code, uma linha em
linguagem humana por transição do loop (tarefa e passo; agente despachado e o que vai fazer;
veredito recebido; próxima tarefa), escrita pelo agente que conduz o loop a partir de um
template fechado, sem que resultado de `Grep`, aviso de leitura ou saída de comando do próprio
orquestrador se interponha entre duas dessas linhas — com a viabilidade medida antes, e não
suposta, e o veredito do dono sobre uma execução real como aceite final.

---

## 1. Modelo conceitual

> **Como ler esta versão.** Só a segunda operação muda. A versão anterior dizia que cada lacuna das frases se preenchia pelo que o condutor tem em mãos; desde que a linha passou a ser gerada pela função do kit, quem preenche a lacuna é a própria função — pelo campo do evento, pelo que a sessão já guarda ou por uma leitura que ela mesma faz —, e o texto da operação passa a dizer isso, como já diziam o estado final do repertório e a entrega. Objetos, propriedades, estados e as demais operações ficam como estavam.

**Estado do modelo:** versão 4 · 2026-09-24 · autor: modelador · 5 operações · 9 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem | lastro na §0 ou no ato do dono | tipo |
|---|---|---|---|---|---|---|
| stream de dados | a fila de mensagens que chega ao dono enquanto uma tarefa roda: o que o agente que conduz o loop escreve e as chamadas que ele mesmo faz, fora dos agentes que despacha, e o arquivo de progresso onde fica gravada, uma por linha, a mensagem que uma função do kit gera a cada transição do loop | viabilidade medida, repertório de mensagens, arquivo de progresso, o que as mensagens narram, agregação da linha, descrição pública | Quem implementa recebe o loop do condutor — as transições que ele atravessa a cada tarefa e o que ele tem em mãos em cada uma —, a função do kit que gera a linha a partir do evento de cada transição, e o arquivo de progresso onde essa função grava. A ferramenta que roda os agentes e o painel que mostra o arquivo ficam como estão. | OP-1 | *"stream de dados: fila onde são inseridas as mensagens que serão renderizadas"*; *"o stream parece ligado aos greps e outros comandos de saída"*; no segundo marco, *"Registre 2. Eliminar esse resíduo é exatamente o objetivo deste plano"*; no ato do dono sobre a execução real, *"Verifique se essas mensagens estão padronizadas por meio de funções, e não escritas agênticas. Isso padronizaria o stream de dados, e permitiria agregações sem custo em token"* | escopo |
| tela do monitor | o lugar onde o dono acompanha a execução: um painel fora da extensão do editor, que mostra o arquivo de progresso linha a linha. Não é a ferramenta de mapeamento de disco que também leva o nome de monitor | o que o dono lê durante a execução | Quem implementa não mexe nela: o dono abre o painel e só o observa, na validação do fim. A sonda do começo foi feita no painel da extensão, e foi o que ela viu que tirou a tela de lá. | externo | *"tela do monitor: lugar onde são apresentados todas as mensagens renderizadas"*; no segundo marco, *"Registre 2"* — a tela fora da extensão; no ato do dono sobre a execução real, *"Eu acho que está convergindo para o que eu desejo"* | medição |
| tarefa | o card que o loop executa, com o cabeçalho — onde está o título dela — e a sequência de passos | cabeçalho e sequência de passos | Quem implementa lê dela o que preenche as mensagens: qual tarefa, o título dela, qual passo e o que o passo pede. Nada nela muda. | externo | *"Tarefas: apresentam o cabeçalho e a sequencia de passos"*; no ato do dono sobre a execução real, *"fazer replace do código da tarefa por uma descrição resumida dela"* | externo |
| mente do agente | a forma como cada agente despachado entende o passo que recebe, dita numa frase de intenção — o que vai executar, o que vai confrontar, o que decidiu —, e não o raciocínio interno do modelo | compreensão do passo atual | Quem implementa usa a intenção que o condutor já tem em mãos — o que ele pediu ao agente e o que o agente devolveu — como campo do evento que a função recebe. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo. | externo | *"mente do agente: apresentam a forma como o agente compreende o passo atual"*; *"pensamentos sendo desenvolvidos pelos agentes"* | externo |

### 1.2 Fluxo de operações

- **OP-1** — O investigador encena, diante do dono, as quatro formas de uma saída chegar à tela — uma busca feita pelo próprio condutor, buscas e leituras feitas dentro de um agente despachado, a resposta de um gancho da ferramenta e a linha de status —; o dono anota o que cada uma mostra, e dessa tabela sai o veredito de viabilidade, sim ou não.
  - `precisa de: tela do monitor` · `altera: stream de dados.viabilidade medida` · `tarefas: TLG-T1` · `lastro: Veja a viabilidade desse plano; Viabilidade sim ou não`
- **OP-2** — O redator do loop escreve o repertório fechado de mensagens: uma frase-modelo para cada transição do loop — tarefa e passo, agente despachado e o que vai fazer, veredito recebido, próxima tarefa —, no molde do exemplo do dono, com cada lacuna preenchida pelo campo do evento, pelo que a sessão já guarda ou por uma leitura que a própria função faz no plano e no diário, e nunca pela mão do condutor: nenhuma lacuna pede ao condutor uma chamada nova nem gasto seu.
  - `precisa de: stream de dados, tarefa, mente do agente` · `altera: stream de dados.repertório de mensagens` · `tarefas: TLG-T2, TLG-T2a, TLG-T2b` · `lastro: Template de mensagens possíveis de serem renderizadas; Exemplo de tela que eu espero receber ao término do plano`
- **OP-3** — O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo.
  - `precisa de: stream de dados, tarefa, mente do agente` · `altera: stream de dados.arquivo de progresso, stream de dados.repertório de mensagens, stream de dados.agregação da linha` · `tarefas: TLG-T3, TLG-T3a, TLG-T3b, TLG-T3c, TLG-T3d, TLG-T3e, TLG-T3f, TLG-T3g, TLG-T3h` · `lastro: Verifique se essas mensagens estão padronizadas por meio de funções, e não escritas agênticas; uma agregação dessa função de stream out é fazer replace do código da tarefa por uma descrição resumida dela; minha única crítica é o termo evidência mecânica, que é vago; Bloqueio de saídas sem valor; Os demais fluxos de dados podem ser descartados; no ato do dono sobre a execução real, as linhas de duas tarefas não chegaram ao arquivo`
- **OP-4** — O mantenedor do loop liga cada transição à função: no instante em que o condutor escolhe a tarefa, muda o estado dela, despacha um agente, recebe o que ele devolveu, coleta a evidência ou fecha a tarefa, é a função que recebe o evento e leva a linha ao arquivo de progresso; o condutor deixa de escrever a linha como texto e deixa de precisar lembrar a forma dela, e o que chega ao dono é a transição narrada com o título da tarefa no lugar do identificador.
  - `precisa de: stream de dados, tarefa, mente do agente` · `altera: stream de dados.o que as mensagens narram` · `tarefas: TLG-T4, TLG-T4a` · `lastro: Isso padronizaria o stream de dados, e permitiria agregações sem custo em token; Só referenciando siglas não efetivamente agrega para a comunicação homem máquina; Estado final será o stream de dados conectados à tarefa e ao pensamento do agente; Modificação do stream de dados para renderização`
- **OP-5** — O mantenedor da porta de entrada do repositório reescreve a descrição pública de como o dono acompanha a execução — o painel fora da extensão e como se lê a linha de cada passo —, e essa própria tarefa corre pelo loop já modificado, com o dono lendo nesse painel o fluxo em linguagem humana e dando o aceite final.
  - `precisa de: stream de dados, tela do monitor` · `altera: stream de dados.descrição pública` · `tarefas: TLG-T5, TLG-T5a` · `lastro: Validação final onde eu poderei ver o desenvolvimento do plano em linguagem humana e não como saídas de comandos`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final | lastro na §0 ou no ato do dono |
|---|---|---|---|
| stream de dados.viabilidade medida | suposta: acredita-se que a extensão recolhe o que um agente despachado faz e que nenhuma configuração esconde uma saída da tela, mas nada disso foi visto | medida diante do dono, uma linha por mecanismo com o que ele viu, e o veredito sim ou não tirado dessa tabela; sendo não, a única alternativa já pensada sobe ao dono como decisão | *"Veja a viabilidade desse plano"*; *"Viabilidade (sim, não)"* |
| stream de dados.repertório de mensagens | não existe: o condutor escreve, quando escreve, frases soltas, sem forma combinada | fechado e embutido na função que gera a linha: uma frase por evento de transição do loop, no molde do exemplo do dono — "Tarefa X, passo Y.", "Agente executor recebe o passo Y e vai executar Z.", "Agente consultor aceitou a entrega." —, em que cada frase diz o que o ato faz, sem termo que o dono não consiga antecipar: a da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit —, e cada lacuna se preenche pelo campo do evento, não pela mão do condutor | *"Template de mensagens possíveis de serem renderizadas"*; *"Exemplo de tela que eu espero receber"*; no ato do dono sobre a execução real, *"minha única crítica é o termo 'evidência mecânica', que é vago. Eu precisaria de um detalhamento maior do que seria essa evidência mecânica, para intervir antes dela ser elaborada"* |
| stream de dados.arquivo de progresso | não existe: toda mensagem fica só no painel da extensão, misturada às chamadas de ferramenta, e nenhum gancho grava coisa alguma depois de uma ferramenta | existe e é alimentado pela função do kit a cada transição do loop: guarda uma linha do repertório por transição, na ordem em que o loop as atravessa, gerada a partir do evento e não da memória do agente — nenhuma linha se perde por o condutor ter esquecido a forma —, e nada mais: nenhuma busca, leitura ou saída de comando, e nenhuma chamada feita dentro dos agentes despachados | *"Bloqueio de saídas sem valor"*; *"Os demais fluxos de dados podem ser descartados"*; no segundo marco, *"Eliminar esse resíduo é exatamente o objetivo deste plano"*; no ato do dono sobre a execução real, *"padronizadas por meio de funções, e não escritas agênticas"* e o fato medido de que as linhas de duas tarefas não chegaram ao arquivo |
| stream de dados.o que as mensagens narram | parece ligado às buscas e às saídas de comando: o que chega à tela é o que as ferramentas devolvem | ligado à tarefa e à intenção dos agentes: uma linha em linguagem humana por transição, gerada pela função no instante em que o loop a atravessa — e não escrita pelo condutor antes de agir —, e é ela que chega ao arquivo de progresso, sem saída de comando entre duas delas | *"Estado final será o stream de dados conectados à tarefa e ao pensamento do agente"*; no ato do dono sobre a execução real, *"Isso padronizaria o stream de dados"* |
| stream de dados.agregação da linha | nenhuma: a linha cita a tarefa e o plano pela sigla — o identificador do card e o do plano —, e quem lê precisa saber de cor o que cada sigla nomeia | a função troca, ao gerar a linha, o identificador da tarefa pelo título dela e o do plano pelo título do plano, sem gastar nada do agente para isso; a sigla sozinha nunca chega ao dono | no ato do dono sobre a execução real, *"uma agregação dessa função de stream out é fazer replace do código da tarefa por uma descrição resumida dela. Só referenciando siglas não efetivamente agrega para a comunicação homem máquina"* |
| stream de dados.descrição pública | a porta de entrada do repositório apresenta o loop pelo que ele despacha e roteia, sem dizer o que o dono lê na tela enquanto ele roda | a porta de entrada diz ao leitor que a execução se acompanha num painel fora da extensão, que mostra o arquivo de progresso com uma linha em linguagem humana a cada passo; diz como abrir esse painel e mostra como a linha se lê | *"Validação final onde eu poderei ver o desenvolvimento do plano em linguagem humana"*; no prompt, a revisão da porta de entrada como última operação |
| tela do monitor.o que o dono lê durante a execução | no painel da extensão: resultados de busca e avisos de leitura entre os passos, em quantidade que afasta o dono do acompanhamento; a sonda viu ainda que as chamadas feitas dentro de cada agente despachado aparecem no topo — numa janela, cerca de noventa delas contra umas trinta e cinco do condutor —, e nenhum arranjo do condutor as tira de lá | num painel fora da extensão, só as linhas do repertório, em linguagem humana: tarefa e passo, agente e o que vai fazer, veredito recebido, próxima tarefa — a tarefa nomeada pelo título, e a coleta de evidência dizendo o que coleta. Nenhuma operação a altera: a diferença entre as duas colunas é o que prova que o stream mudou | *"O estado inicial da tela são mensagems de grep e leitura"*; *"O estado final dela são mensagens indicativas do progresso atual da tarefa"*; no segundo marco, *"Registre 2"*; no ato do dono sobre a execução real, *"Eu acho que está convergindo para o que eu desejo"* |
| tarefa.cabeçalho e sequência de passos | o card traz o cabeçalho e a sequência de passos | o mesmo, inalterado: o plano só lê a tarefa para preencher as mensagens | *"Tarefas: apresentam o cabeçalho e a sequencia de passos"* |
| mente do agente.compreensão do passo atual | cada agente entende à sua maneira o passo que recebe, e o raciocínio interno fica recolhido | o mesmo, inalterado: a tela mostra a intenção que o agente declara, nunca o raciocínio interno | *"apresentam a forma como o agente compreende o passo atual"* |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 4 | 2026-09-24 | vigente | modelador — conflito sobre o achado de processo de alvo `modelo` do laudo `P-0748-TLG-T2b`: a emenda sobre `DTG-29` reescreveu a `OP-3`, a `OP-4` e a `I-3`, mas deixou a cláusula final da `OP-2` dizendo que cada lacuna se preenche pelo que o condutor tem em mãos; a `OP-2` passa a dizer que a lacuna se preenche pelo campo do evento, pelo estado da sessão ou por leitura local da função, nunca pela mão do condutor, em linha com a `I-3` e com o estado final do repertório. Nada mais muda. Validada pelo consultor em `DTG-41` e aceita pelo dono no fechamento de 2026-09-24, verbatim: *"Vamos aprovar esse plano e ver ele ocorrendo na prática."* e *"Aceite os planos, revise os tiquetes para ver quais são pertinentes ainda para enfileira-los na sequencia"*; promovida a vigente nessa data |
| 3 | 2026-09-24 | obsoleta | modelador — emenda sobre `DTG-29` (ato do dono ao ler a execução real de `TLG-T3`, `TLG-T2a` e `TLG-T4`; fato medido `AE-7`): a linha do stream passa a ser gerada por função do kit a partir do evento de cada transição do loop, a função agrega o título da tarefa e o do plano no lugar do identificador, e a frase da coleta de evidência diz o que se coleta; muda a `OP-3` e a `OP-4`, nasce a propriedade `agregação da linha`, e mudam os estados finais do repertório, do arquivo de progresso e do que as mensagens narram. Aceita pelo dono em 2026-09-24, verbatim: *"Aceito."* — sobre o modelo emendado, as decisões `DTG-30`..`DTG-38` e o worked example da `### 4.1` (validação do consultor dispensada pela orquestração, com o dono presente). Caiu pelo aceite da versão 4 no fechamento de 2026-09-24 |
| 2 | 2026-09-24 | obsoleta | modelador — emenda sobre `DTG-12` (triagem `DTG-18`): a tela sai da extensão do editor para um painel à parte, alimentado pelo arquivo de progresso que um gancho do kit grava; muda a `OP-3`, e a `OP-4` e a `OP-5` passam a mirar o painel novo. Validada pelo consultor em `DTG-19` (acionamento 4) e aceita pelo dono no marco em 2026-09-24: *"Sim, é o que eu disse, então está aceito por default"*. Caiu pelo aceite da versão 3 em 2026-09-24 |
| 1 | 2026-09-23 | obsoleta | modelador — autoria sobre o dossiê do planejador. Caiu pelo aceite da versão 2 no marco de 2026-09-24 |

---

## 2. Fatos estabelecidos

Cada fato com a fonte. `F-<n>` é fato; `H-<n>` é **hipótese a apurar** — entra no plano como
insumo da sonda de viabilidade e **nunca** como premissa de card.

- **F-1** — O dono acompanha pela extensão VS Code do Claude Code (Windows). Ali, chamadas de
  ferramenta, resultados e raciocínio aparecem como linhas-resumo recolhíveis; o **texto que o
  agente escreve fica visível inteiro**. Fonte: contexto do ambiente entregue pelo orquestrador
  em 2026-09-23 (fato de ambiente, não decisão de rota).
- **F-2** — O loop de execução é conduzido pela skill `scrum-master`
  (`.claude/skills/scrum-master/SKILL.md`, passos 1–10: gate de modelo, seleção da tarefa,
  gates herdados, despacho do executor, recepção, despacho do reviewer, leitura do veredito,
  roteamento, arquivamento, continuar/encerrar) com a `passagem-de-bastao`, despachando
  `pantonic-executor`, `pantonic-reviewer` e `pantonic-consultant` como subagentes. Fonte:
  contexto do orquestrador; cabeçalhos da skill (`grep -n "^## \|^### "`, 2026-09-23).
- **F-3** — Um subagente devolve ao chamador **só** a mensagem final (`SubagentHandback`); as
  chamadas de ferramenta internas dele não entram no contexto do chamador. Fonte: contrato do
  harness em vigor nesta própria invocação (nota de sistema do agente: "Only a report delivered
  through SubagentHandback reaches your caller").
- **F-4** — Hooks `PreToolUse` do harness recebem a chamada e podem **reescrever o comando**
  antes da execução: um hook global já reescreve comandos `pytest` para filtrar a saída, com o
  log integral em `%TEMP%\claude\pytest_last_run.log`. Fonte: `~/.claude/CLAUDE.md`, Regra 3.
- **F-5** — `D:\workspaces\PantonicMonitor` é uma ferramenta de mapeamento e diff de consumo de
  disco (`Get-DiskState.ps1`, modos `Report`/`Diff`/`List`/`Prune`; árvore: o script, o README e
  `snapshots/`). Não tem relação com renderização de mensagens. Fonte:
  `D:\workspaces\PantonicMonitor\README.md:1-9`, lido em 2026-09-23.
- **F-6** — Existem dois arquivos de configuração do harness com efeito sobre esta sessão:
  `C:\Users\panta\.claude\settings.json` (global) e
  `D:\workspaces\PantonicApp\.claude\settings.json` (projeto). Fonte: `ls`, 2026-09-23. O
  conteúdo (quais hooks, matchers e comandos) é insumo a apurar (`Q-3`).
- **H-1** — *(a apurar)* Nenhuma configuração do harness (settings, hook, output style) suprime
  ou oculta a **renderização** de um resultado de ferramenta na extensão VS Code; hooks agem
  sobre a chamada (bloquear, reescrever, injetar contexto), não sobre o que a tela mostra.
- **H-2** — *(a apurar)* Um hook `PostToolUse` pode ler a resposta da ferramenta e escrevê-la
  em arquivo, mas **não** altera o que a extensão renderiza daquela chamada.
- **H-3** — *(a apurar, por observação do dono)* Na extensão VS Code, as chamadas de ferramenta
  feitas **dentro** de um subagente aparecem recolhidas sob a linha do despacho (`Agent`), e não
  como linhas do topo; só a chamada de despacho e o texto do orquestrador ficam no fluxo
  principal.
- **H-4** — *(a apurar)* A `statusline` do harness é um recurso da CLI; na extensão VS Code ou
  não renderiza ou renderiza uma única linha — em qualquer dos dois casos não serve como fluxo
  de progresso.
- **H-5** — *(apurada → `F-7`)* O orquestrador (`scrum-master`) faz hoje, no topo, entre um
  despacho e outro, doze atos de ferramenta por ciclo — contagem e lista por passo em `F-7`.

Fatos da campanha (`docs/plans/_CAMPANHA-P-0748.md`, scout, 2026-09-23) e das medições do
planejador na Fase 3b (2026-09-23), todos com fonte:

- **F-7** — *(Q-1 + leitura das âncoras)* Atos de ferramenta do condutor no topo, por ciclo de
  tarefa, em `.claude/skills/scrum-master/SKILL.md`: passo 2 `python .claude/tools/backlog.py
  next` (`:45`); passo 3 `python .claude/tools/modelo.py check --plano <plano>` (`:60`) e a
  materialização `ready` → `in-progress` (`:65-66`, "materializar `ready` → `in-progress` no
  kanban"); passo 4 garantir `.claude/estado/`, gravar `.claude/estado/tarefa-corrente.json`
  (chaves `tarefa`, `projeto`, `modelo`, `plano`, `despachado_em` ISO 8601) e "Capturar `git
  rev-parse HEAD` como `<ref>`" (`:74-79`); passo 6 `python .claude/tools/review_evidence.py
  --plano <plano> --tarefa <ID> --desde <ref> --out docs/RDO/evidencia/<plano>-<ID>.md`
  (`:120-124`); passo 9 `modelo.py check` de novo (`:194`), `python .claude/tools/backlog.py
  status <ID> <estado>` (`:168`), `python .claude/tools/rdo.py close …` (`:171-175`), "apagar o
  laudo" (`:178`), `python .claude/tools/telemetria.py append` (`:181`); passo 10 `python
  .claude/tools/review_evidence.py … --atribuir` (`:251`, só em `B0`). Doze atos, além dos dois
  despachos (executor, reviewer) e dos despachos condicionais (consultor, modelador).
- **F-8** — *(Q-2)* Nenhuma das duas skills prescreve texto ao dono entre passos; o único texto
  ao dono é o "Relatório de encerramento" (`scrum-master/SKILL.md:276-304`).
  `passagem-de-bastao/SKILL.md:10-13` diz, literal: "o que chega ao dono chega pelo **relatório
  de encerramento** do `scrum-master`, e só lá."
- **F-9** — *(Q-3)* Hooks vigentes — global `C:\Users\panta\.claude\settings.json`: `PreToolUse`
  `Bash|PowerShell` → `pytest_pretooluse.py`, `verbose_cmd_pretooluse.py` (`:250-264`);
  `PreToolUse` `Read` → `read_cap_pretooluse.py` (`:267-275`); `UserPromptSubmit` →
  `modelo_por_fase_userpromptsubmit.py` (`:277-287`); `statusLine` → `statusline.py`
  (`:291-295`), única chave que afeta renderização. Projeto `.claude/settings.json`: bloco
  `"hooks": {` (`:22`) com `PreToolUse` matcher `.*` → `python
  D:/workspaces/PantonicApp/.claude/tools/ocupacao.py` (`:23-32`), `SubagentStop` →
  `telemetria_hook.py` (`:34-42`), `UserPromptSubmit` → `backlog_hook.py` (`:44-53`). **Nenhum
  `PostToolUse`** em nenhum dos dois; nenhuma chave `verbose`, `collapse`, `hide`, `outputStyle`.
  O arquivo do projeto está limpo no git: `git diff --quiet -- .claude/settings.json` sai `0`
  (2026-09-23).
- **F-10** — *(Q-4)* O hook de `pytest` lê `tool_name` e `tool_input.command` e devolve
  `hookSpecificOutput.updatedInput` (`C:\Users\panta\.claude\hooks\pytest_pretooluse.py:35-60`).
  Confirma `F-4`: hook age sobre a chamada, não sobre a tela.
- **F-11** — *(Q-5)* Linhas de retorno fixas: executor (`pantonic-executor.md:87-88`) `<tarefa>
  review [pendencia=<uma linha>]` ou `<tarefa> blocked motivo=<dependencia|premissa|ferramenta>
  <uma linha de razão>`; reviewer (`pantonic-reviewer.md:128-139`) `<tarefa> <veredito>
  <percentual> bloqueante=<dimensão|nenhuma>` + `laudo=<caminho>` (+ dossiê `Ato de modelo` de
  `conflito`, opcional); consultor (`pantonic-consultant.md:24-25`)
  `rota=<resolve|modelador|planejador>` [+ `estrategico=<uma frase>`], seguidas da decisão e do
  reparo.
- **F-12** — `python .claude/tools/backlog.py next` é **só leitura**: `git status --porcelain`
  conta 126 linhas antes e depois da chamada (2026-09-23). Saída medida: primeira linha `===
  PRÓXIMA TAREFA: <ID> — <título> [<cabeçalho>]`, depois `tíquete: …`/plano, `--- dossiê
  (verbatim, teto DB-7) ---`, o card inteiro (inclusive a linha `- **Objetivo:**`), `---
  pendências mecânicas ---` e três linhas de contagem. Com fila vazia imprime `nada delegável — 0
  elegível(is) · blocked <n>` (forma registrada no card `TK-65a`, `docs/DIARIO_DE_OBRAS.md`).
- **F-13** — CLIs medidas por `--help` (2026-09-23): `backlog.py status id estado [--razao RAZAO]
  [--nota NOTA] [--repo REPO]`; `rdo.py close --plano --tarefa --tool-uses --tokens-k --duracao-s
  --veredito {aprovado,ressalva} --percentual {0..100} --bloqueante --recomendacao
  --pendencia-laudo [--pendencia] [--licoes-aprendidas] [--rdo-dir] [--template]
  [--esquema-legado] [--modelo] [--classe]`; `telemetria.py append --data --projeto --tarefa
  --modelo --tool_uses --tokens_k --duracao_s --fonte [--file]` (**sublinhado**, não hífen);
  `modelo.py check --plano PLANO [--root ROOT]`, exit `0`/`1`/`2` (`scrum-master/SKILL.md:60-63`).
- **F-14** — `python -m pytest tests/ -q` → `277 passed` (2026-09-23; referência histórica —
  o piso é relação, `I-7`). Os testes carregam os instrumentos por caminho:
  `importlib.util.spec_from_file_location("modelo", _MODELO_PATH)` (`tests/test_modelo.py:53-54`),
  `_ROOT = Path(__file__).resolve().parents[1]` (`:35`).
- **F-15** — `pwsh -NoProfile -File .claude/checks/check-readme.ps1` imprime, medido em
  2026-09-23, `check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s), versão '0.0.0', 14
  seção(ões) com Fonte da verdade válida; frases de contagem de 'Os guardrails' conferidas:
  'regras mínimas obrigatórias'=True, 'regras falham como teste executável'=True.` e sai `0`.
  Nem `README.md` nem `.claude/README.md` enumeram os instrumentos de `.claude/tools/` (busca por
  `rdo.py`, `review_evidence.py`, `backlog.py`: zero ocorrências).
- **F-16** — `git check-ignore -q .claude/tools/loop.py` e `git check-ignore -q
  tests/test_loop.py` saem `1` (não ignorados); `git check-ignore -q
  .claude/estado/tarefa-corrente.json` sai `0` (ignorado) e `.claude/estado/.gitkeep` existe.
- **F-17** — `.claude/agents/pantonic-scout.md` existe (dez agentes em `.claude/agents/`).
- **F-18** — `README.md:430` `## 6. O loop de execução`, `:432` `> Fonte da verdade:
  .claude/skills/scrum-master/SKILL.md`, `:436-437` a frase literal "o loop roteia pelo veredito
  calculado e o gerente não medeia tarefa a tarefa — ele lê um relatório no fim." (uma
  ocorrência de `ele lê um relatório no fim`); `:826` a linha da `scrum-master` na tabela de
  skills. O `README.md` já tem alterações não commitadas (`git diff --numstat` = `37 52`), logo
  `git diff` **não** discrimina o card do `README`. *(Re-medido em 2026-09-24, rodada do
  planejador: a `## 6` está em `:435`, o trecho `ele lê um relatório no fim` em `:442` (uma
  ocorrência), a linha da `scrum-master` na tabela de skills em `:831`; `numstat` = `49 59`.)*

Fatos da rodada do planejador sobre a versão 2 (2026-09-24), todos medidos, com fonte:

- **F-19** — *(tensão (2) e (1) da `### 1.3`, sonda de formato do transcript rodada pelo
  planejador com o script literal do passo 1 de `TLG-T3`)* O transcript da sessão principal
  (`C:\Users\panta\.claude\projects\d--workspaces-PantonicApp\<session_id>.jsonl`, o mais recente)
  grava o texto que o condutor escreve como entradas `"type": "assistant"` com bloco
  `"type": "text"` em `message.content`, uma linha JSON por bloco, separada da linha do
  `tool_use` (medido: `assistant 57 com_text 10 isSidechain_true 0 text_e_tool_use_juntos 0`). As
  entradas dos agentes despachados **não** estão nesse arquivo: moram em arquivos próprios em
  `<session_id>/` e todas levam `"isSidechain": true` (medido: `subagentes: arquivos 5 assistant 128
  isSidechain_true 128`). Chaves de uma entrada `assistant`: `isSidechain`, `message`,
  `parentUuid`, `sessionId`, `timestamp`, `type`, `uuid`.
- **F-20** — *(tensão (1) e (2))* Um gancho do harness recebe, no JSON de entrada, `transcript_path`
  apontando para o transcript da **sessão principal** mesmo quando dispara numa chamada feita
  **dentro** de um agente despachado, e nesse caso traz também `agent_id` e `agent_type` (payload
  literal de `PreToolUse` disparado dentro de `pantonic-executor`,
  `docs/audits/SPIKE_HARNESS_EXECUCAO_AUTONOMA.md:101-105`). O gancho vigente
  `.claude/tools/ocupacao.py:147-152` já usa as duas coisas: `if payload.get("agent_type"): return
  0` e `transcript_path = payload.get("transcript_path")`, com falha aberta (`:169-170`). Logo os
  ganchos **disparam** nas chamadas internas de subagente, e o payload as distingue.
- **F-21** — `.claude/projecoes.json` é a declaração canônica do que o harness lê; o
  `.claude/settings.json` é a materialização local, ignorada pelo git (`.gitignore:1-5`, texto
  literal do comentário das linhas 2-3: *"Declaração canônica do que o harness lê mora em
  .claude/projecoes.json (versionado); este arquivo é a materialização local, produzida por python
  .claude/tools/materializar.py apply."*, seguido de `.claude/settings.json` na linha 5). Bloco `hooks` do alvo `projeto` em
  `.claude/projecoes.json:7-38`, com `"SubagentStop": [` em `:19`; comando no formato `python
  {KIT_ROOT}/tools/<script>.py`. CLI medida: `materializar.py {apply,check,drift} [--alvo
  {projeto,usuario,todos}]`. Hoje: `check --alvo projeto` → `materializar: OK - manifesto valido.`
  exit `0`; `drift --alvo projeto` → `materializar: OK - sem drift.` exit `0`. O `check` exige que o
  arquivo citado no `command` exista (`materializar.py:343`). Ensaio numa cópia do kit
  (2026-09-24) com os eventos `PostToolUse` (matcher `.*`) e `Stop` acrescentados: `drift` antes
  do `apply` sai `1` com uma linha `evento 'PostToolUse': entrada canonica ausente do destino…` e
  uma `evento 'Stop': …`; `apply` → `materializar: OK - apply concluido.` exit `0`; `drift` depois →
  `materializar: OK - sem drift.` exit `0`; o `settings.json` gerado tem o nome do script duas vezes
  e passa em `json ok`.
- **F-22** — Residência contra o `.gitignore` (regra literal: `.claude/estado/*` e
  `!.claude/estado/.gitkeep`): `git check-ignore -q` sai `0` (ignorado) para
  `.claude/estado/progresso.txt`, `.claude/estado/progresso-cursor.json` e
  `.claude/estado/sonda_transcript.py`; sai `1` (versionável) para
  `.claude/tools/progresso_hook.py` e `tests/test_progresso_hook.py` (2026-09-24).
- **F-23** — Estado da `scrum-master` depois de `TLG-T2` (2026-09-24): cabeçalhos `### Passo 2`
  `:46` a `### Passo 10` `:211`, `## Repertório de mensagens ao gerente` `:313`, `## Proibições`
  `:339`, `## Guardrails` `:344` (última seção do arquivo). Todo passo 2..10 tem uma linha que
  começa por `- **Ação:**`. `loop.py` aparece em **sete** linhas, todas da tabela do repertório
  (`M-0` `:323`, `M-1` `:324`, `M-2` `:325`, `M-3` `:326`, `M-10` `:333`, `M-11` `:334`, `M-12`
  `:335`). Contagens `-SimpleMatch`: `**Narra:**` = `1` (a frase de abertura da seção do
  repertório cita o bullet), `[gerente] ` = `0`, `progresso.txt` = `0`. Na
  `passagem-de-bastao`, `:12-13` seguem com `e só lá` (`1` ocorrência).

*(Fatos da rodada de replanejamento 2, 2026-09-24 — `DTG-29`; medidos pelo condutor da janela
`TLG-T3`→`TLG-T4` e re-medidos pelo planejador no repositório no mesmo dia.)*

- **F-24** — *(o que existe e vai ser corrigido)* `.claude/tools/progresso_hook.py` (entregue por
  `TLG-T3`, `aprovado 100`): docstring de módulo nas linhas 1-5; `KIT = Path(__file__).resolve().parents[1]`
  `:14`; `MARCADOR` `:15`; `INICIOS` `:16`; `def linhas_do_repertorio` `:20`; `def ler_novas` `:37`;
  `def main(argv, entrada, estado, espera)` `:61`; dentro de `main`, a barreira `if payload.get("agent_type"): return 0`,
  depois `tp = payload.get("transcript_path")`, `estado = estado or KIT / "estado"`,
  `estado.mkdir(parents=True, exist_ok=True)` e, na linha seguinte, `trava = estado / "progresso.lock"`.
  Só biblioteca padrão (`json`, `os`, `sys`, `time`, `pathlib`); nunca imprime; sai `0`.
  `tests/test_progresso_hook.py`: `_ROOT = Path(__file__).resolve().parents[1]` `:19`, carga por
  `importlib.util.spec_from_file_location("progresso_hook", _PROGRESSO_HOOK_PATH)` `:24`, nove
  funções `def test_tf_prog_1_marcador` … `def test_tf_prog_9_trava` (`grep -c "^def test_"` → `9`).
- **F-25** — *(declaração dos ganchos, `.claude/projecoes.json`, alvo `projeto`)* `"PreToolUse": [`
  `:8` com **uma** entrada, matcher `.*`, comando `python {KIT_ROOT}/tools/ocupacao.py` (`:10-15`);
  `"PostToolUse": [` `:19`, matcher `.*` `:21`, comando `python {KIT_ROOT}/tools/progresso_hook.py`
  `:25`; `"Stop": [` `:30`, mesmo comando `:35`; `"SubagentStop": [` `:40`. Contagem `-SimpleMatch`
  de `progresso_hook.py` no arquivo: `2`. `materializar.py check --alvo projeto` e `drift --alvo
  projeto` saem `0` (condutor, 2026-09-24).
- **F-26** — *(estado da `scrum-master` depois de `TLG-T2a` e `TLG-T4`)* contagens `-SimpleMatch`:
  `**Narra:**` = `10` (nove bullets `- **Narra:**` nas linhas 50, 62, 81, 111, 130, 154, 165, 182,
  225 — um por passo 2..10, cada um imediatamente antes da linha `- **Ação:**` do passo — mais a
  frase *"é dito pelo bullet `**Narra:**` de cada passo"* no parágrafo de abertura da seção
  `## Repertório de mensagens ao gerente` `:322`); `[gerente] ` = `1` (o último bullet de
  `## Guardrails` — cabeçalho `:353`, bullet `:365` —, que começa por `- Toda linha do repertório (seção *Repertório de mensagens
  ao gerente*) é escrita como texto do agente`); `progresso.txt` = `1` (mesmo bullet);
  `progresso_hook.py` = `1` (mesmo bullet); `loop.py` = `0`; `backlog.py next` = `7`;
  `Repertório de mensagens ao gerente` = `2` (o cabeçalho `:322` e o bullet dos guardrails);
  `tarefa-corrente` = `1` (`:84`, passo 4); `backlog.py status` = `1` (`:183`, passo 9: *"materializar
  o status com `python .claude/tools/backlog.py status <ID> <estado>`"*, e só depois `rdo.py close`);
  `rdo.py close` = `5`; `review_evidence.py` = `6`. A tabela do repertório tem 15 linhas `M-0`..`M-14`
  (`:331-345`), quatro colunas: id, momento (passo), frase-modelo, lacunas ← o que o condutor já
  tem; a seção termina antes de `## Proibições` `:348`. O passo 3 (`:58-75`) manda *"materializar
  `ready` → `in-progress` no kanban"* sem escrever o comando; o instrumento que o faz é
  `backlog.py status <ID> in-progress` (CLI medida: `backlog.py status [--razao] [--nota] id estado`).
- **F-27** — `.claude/skills/passagem-de-bastao/SKILL.md:11-13` (texto vigente, entregue por
  `TLG-T4`): *"Não é skill de comunicação com humano; o que chega ao dono chega pelas linhas do
  **repertório de mensagens ao gerente**, que o gancho do kit grava no arquivo de progresso, e pelo
  **relatório de encerramento** do `scrum-master`, e só por eles."* Contagem `-SimpleMatch` de
  `arquivo de progresso` = `1`; de `a partir dos eventos` = `0`.
- **F-28** — `README.md` não foi tocado (`TLG-T5` é `ready`): `:442` contém `ele lê um relatório no
  fim` (única); `:831` contém `roteia pelo veredito calculado e encerra a janela` (única);
  `Repertório de mensagens ao gerente` = `0`; `progresso.txt` = `0`.
- **F-29** — *(eventos do loop que já são atos de ferramenta com entrada estruturada — o que uma
  função lê sem nenhum token do condutor)* `python .claude/tools/backlog.py next`: stdout começa por
  `=== PRÓXIMA TAREFA: <ID> — <título> [<cabeçalho>]` seguido do card inteiro (inclusive a linha
  `- **Objetivo:**`); fila vazia: `nada delegável`. `python .claude/tools/backlog.py status <ID>
  <estado>`, estados `in-progress`, `review`, `done`, `blocked`, `cancelled` (passo 3 e passo 9).
  `python .claude/tools/review_evidence.py --plano <plano> --tarefa <ID> --desde <ref> --out <arq>`
  (passo 6) e o mesmo comando com `--atribuir` (passo 10, `B0`). `python .claude/tools/rdo.py close
  --plano <plano> --tarefa <ID> …` (passo 9, depois do `status`). A chamada da ferramenta `Agent` com
  `subagent_type` ∈ {`pantonic-executor`, `pantonic-reviewer`, `pantonic-consultant`,
  `pantonic-model-designer`, `pantonic-planner`} e o retorno dela — primeira linha do executor
  `<ID> review[ pendencia=<uma linha>]` ou `<ID> blocked motivo=<dependencia|premissa|ferramenta>
  <razão>` (`scrum-master` passo 4, `DP-G` item 2); do revisor `<ID> <veredito> <percentual>
  bloqueante=<dimensão|nenhuma>` (`pantonic-reviewer.md:131`); do consultor `rota=<resolve|modelador|
  planejador>` e, opcional, `estrategico=<uma frase>` na segunda linha (`pantonic-consultant.md:24`).
  No passo 4 o loop grava `.claude/estado/tarefa-corrente.json` = `{"tarefa": "<ID>", "projeto":
  "PantonicApp", "modelo": "<modelo>", "plano": "P-0748", "despachado_em": "<ISO>"}` **antes** de
  invocar o executor (fonte do gancho `SubagentStop`); o campo `plano` é o id, não o caminho.
- **F-30** — *(payload dos ganchos, medido pelo kit em `ocupacao.py:147-163` e `progresso_hook.py`)*
  JSON no stdin com `session_id`, `transcript_path`, `cwd`, `hook_event_name` e, dentro de agente
  despachado, `agent_type`/`agent_id` (`F-20`); `PreToolUse` e `PostToolUse` trazem `tool_name` e
  `tool_input` (para `Bash`: `command`; para `Agent`: `subagent_type`, `description`, `prompt`,
  `model`), e `PostToolUse` traz também `tool_response`. Só o `Stop` roda sem `tool_*`. Comando
  que sai com erro **não** dispara `PostToolUse` (`AE-6`); `PreToolUse` dispara sempre. **Não
  medido:** a forma exata de `tool_response` para `Agent` e para `Bash` — se o texto de retorno do
  subagente e o stdout do comando chegam inteiros e em que chave. Não é medível de dentro de um
  executor: o `PostToolUse` de `Agent` só dispara na sessão principal, e um subagente não despacha
  agente. É o insumo de `TLG-T3a` (`DTG-32`).
- **F-31** — *(fontes da agregação)* título do card = cabeçalho `### <ID> — <título> [<modelo> · …]`
  (gramática de `GOVERNANCA.md` §3); objetivo = linha `- **Objetivo:**` do card; título do plano =
  linha 1, `# P-0748 — <título>`; cards de tíquete moram em `docs/DIARIO_DE_OBRAS.md` sob
  `## TK-<n> — <título>` (`backlog.py next` pode selecioná-los). `git check-ignore -q` sai `0`
  (ignorado) para `.claude/estado/progresso-estado.json`, `.claude/estado/progresso-captura.jsonl`
  e `.claude/estado/progresso-captura.on` (regra vigente `.claude/estado/*`, `F-22`; medido
  2026-09-24).
- **F-32** — *(o conteúdo da evidência, o que a frase `M-5` tem de dizer)* `review_evidence.py`
  produz cinco blocos: `git diff --stat` desde o ref do despacho; arquivos tocados; escopo (tocados
  × alvos do card, com atribuição a outra tarefa/orquestração e "fora dos alvos e sem atribuição");
  trechos do diff por alvo (teto 4000 chars); bateria de guardas (`pytest`, `dead_code`,
  `ratchet_piso`, `kit_check validate`/`check-drift`, `check-readme`) com exit e veredito mecânico.
  Frase aceita pelo dono nesta rodada: *"vou reunir para o revisor o que mudou desde o despacho, os
  arquivos tocados fora do previsto e o resultado dos testes e guardas do kit"*.
- **F-33** — Suíte em 2026-09-24 (condutor): `289 passed`. `python .claude/tools/modelo.py check
  --plano docs/plans/P-0748-tela-do-gerente.md` antes desta rodada: `modelo: OK — 5 operações, 4
  objetos, 8 propriedades, 6 tarefas, versão 2`, exit `0`. `AE-7` medido: as linhas narradas em
  `TLG-T3` e `TLG-T2a` não chegaram ao arquivo — o condutor as escreveu sem o marcador antes de a
  `TLG-T4` instituir a regra.

### 2.1 Insumos a apurar — campanha (perguntas fechadas)

Perguntas respondíveis por leitura vão ao `pantonic-scout` (≤ 40 linhas cada, `caminho:linha`);
as que exigem observar a tela são a matéria da operação de viabilidade (`DTG-3`). **`Q-1`..`Q-5`
respondidas em 2026-09-23** (`docs/plans/_CAMPANHA-P-0748.md`, absorvidas em `F-7`..`F-11`);
`Q-6` é o método de `TLG-T1`.

- **Q-1** (scout) — Em `.claude/skills/scrum-master/SKILL.md` e
  `.claude/skills/passagem-de-bastao/SKILL.md`: liste, por passo do fluxo, **cada chamada de
  ferramenta que o orquestrador faz no topo** (ferramenta, comando ou caminho, `SKILL.md:linha`).
  Devolver a sequência ordenada de um ciclo completo de tarefa.
- **Q-2** (scout) — Nas mesmas duas skills: que **texto** (não chamada de ferramenta) a skill
  manda o orquestrador escrever ao dono entre os passos hoje? `caminho:linha` e o texto literal
  prescrito, ou "nenhum".
- **Q-3** (scout) — `C:\Users\panta\.claude\settings.json` e
  `D:\workspaces\PantonicApp\.claude\settings.json`: quais hooks estão configurados (evento,
  matcher, comando, `arquivo:linha`)? Existe chave que afete renderização (`statusLine`,
  `outputStyle`, qualquer chave com `verbose`, `collapse`, `hide`)? Devolver a lista ou "nenhuma".
- **Q-4** (scout) — O script do hook global de `pytest` (`Q-3` dá o caminho): quais campos do
  JSON de entrada ele lê (`tool_name`, `tool_input.command`, outros) e como devolve a reescrita
  (`updatedInput`? exit code?). `caminho:linha`.
- **Q-5** (scout) — `.claude/agents/pantonic-executor.md`, `pantonic-reviewer.md`,
  `pantonic-consultant.md`: cada um tem linha de **retorno** com forma fixa (o que devolve ao
  orquestrador)? `caminho:linha` e a forma. É o insumo do template: a mensagem humana de cada
  transição se escreve a partir do que o orquestrador **já recebe**.
- **Q-6** (sonda, observada pelo dono — matéria da operação de viabilidade) — Na extensão VS
  Code, com o contexto de orquestração ativo: (a) um `Grep` no topo renderiza como? (b) um
  subagente que roda três `Grep` e um `Read` renderiza como no topo — só a linha do despacho,
  ou as quatro chamadas? (c) o stdout de um hook `PostToolUse` aparece na tela? (d) a
  `statusLine` configurada aparece na extensão? Devolver a tabela `mecanismo → observado`
  (sim/não), quatro linhas, sem dado bruto.

### 2.2 Agregado da sonda de viabilidade (TLG-T1)

Medido pelo dono na extensão VS Code em 2026-09-24, sessão reaberta com o hook (c) gravado.

| forma | mecanismo | observado pelo dono | o que apareceu na tela |
|---|---|---|---|
| (a) | `Grep` feito pelo condutor no topo | sim | uma linha recolhida: `Grep "TLG-T1" (in docs/plans/P-0748-tela-do-gerente.md)` · `14 lines of output` |
| (b) | 3 `Grep` + 1 `Read` dentro de um subagente despachado | sim | as quatro chamadas no topo — os três `Grep` e o `Read`, cada um em linha própria, mais o `SubagentHandback` com `IN`/`OUT`; e o relatório do subagente chegou de novo ao fluxo como mensagem própria (`Message from @af9…`, "Subagent hand-back") |
| (c) | stdout de um hook `PostToolUse` (`SONDA-HOOK-C`) | não | o texto `SONDA-HOOK-C` não aparece no fluxo transcrito pelo dono |
| (d) | `statusLine` configurada no settings global | não | nenhuma linha de status no fluxo transcrito pelo dono |

**Veredito de viabilidade (Marco 2):** não — regra: `sim` se e só se a linha (b) registra "só a linha do despacho".


---

## 3. Decisões

Todas técnicas ou táticas — nenhuma passou no teste de legitimidade para virar pergunta ao
dono. Toda decisão será consumida por ≥ 1 card na Fase 3b.

| id | valor | razão |
|---|---|---|
| `DTG-1` | **Revogada em parte por `DTG-12`/`DTG-18` (2026-09-24):** a tela deixa de ser o painel da extensão; segue viva só a exclusão do `PantonicMonitor`. Texto original: a "tela do monitor" do modelo é o **painel da extensão VS Code do Claude Code**; `PantonicMonitor` fica fora do escopo | `F-5`: é uma ferramenta de disco. O dono acompanha pela extensão (`F-1`) |
| `DTG-2` | O "stream de dados" que o plano modifica é a **saída do agente que conduz o loop** (`scrum-master`): o que ele escreve como texto e as chamadas que ele faz no topo. Não se tenta modificar o harness nem a extensão | Único canal cuja forma o kit controla; texto do agente renderiza inteiro (`F-1`); harness e extensão não são código deste repositório |
| `DTG-3` | A **primeira operação** do modelo é a sonda de viabilidade: tarefa `classe investigacao`, `+ dono` (ele observa a tela), método fechado = `Q-6`, agregado = tabela de quatro linhas `mecanismo → observado`. O veredito `sim`/`não` do dono é o Marco 2 e sai do agregado, nunca de suposição | O dono pediu "Viabilidade (sim, não)" como entrega; decisão que escolhe mecanismo de plataforma exige sonda antes da recomendação (`pantonic-planner`, Fase 1) |
| `DTG-4` | **Retirada por `DTG-26` (2026-09-24).** Texto original: a rota da entrega "bloqueio de saídas sem valor" é **deslocamento, não supressão**: (i) toda chamada de ferramenta do orquestrador no topo que não seja o despacho de subagente migra para dentro de um subagente ou para um único comando do kit; (ii) nenhuma chamada de `Grep`/`Read` do orquestrador entre dois despachos. Se a sonda medir `H-3 = não` (chamadas internas do subagente aparecem no topo), aplica-se `R-1` | Não há alavanca conhecida sobre a renderização (`H-1`, `H-2`); a alavanca que existe é onde a chamada acontece (`F-3`) |
| `DTG-5` | O **template de mensagens** é uma tabela fechada, residência única numa seção normativa deste plano (a ser escrita na Fase 3b como `## 4.1 Template de mensagens do loop`), uma linha por transição do loop da `scrum-master` (passos 2, 4, 5, 6, 7, 8, 10 — `F-2`), na forma do exemplo do dono na §0 (`Tarefa X, passo Y.` / `Agente executor recebe o passo Y e vai executar Z.` / ...). Cada linha é preenchida **só** com o que o orquestrador já tem em mãos naquele passo (id da tarefa, título, objetivo do card, linha de retorno do subagente — `Q-5`); nenhuma linha exige chamada de ferramenta nova para ser escrita | O template é a interface de leitura do dono; ele já deu a forma (cinco linhas de exemplo) — default derivado do pedido, sem pergunta. Ir ao Marco 1 como worked example preenchido com dado deste plano |
| `DTG-6` | A **validação final** roda sobre corpus real: a última tarefa deste plano (revisão do `README.md`, G-README dever 2) é executada pelo loop já modificado, e o Marco 3 é o dono lendo essa execução na tela. Não se cria fixture de "tarefa de mentira" | O dono pediu ver "o desenvolvimento do plano" — o próprio plano é o corpus; a tarefa de README é obrigatória de qualquer forma |
| `DTG-7` | O "pensamento do agente" na tela é a **frase de intenção** que cada agente devolve/escreve antes de agir (`o que vai executar`, `o que vai confrontar`), não o raciocínio interno do modelo: o loop não expõe raciocínio, e a extensão o recolhe (`F-1`) | Única forma controlável pelo kit; casa com as linhas 2 e 3 do exemplo do dono |
| `DTG-8` | Propagação das mudanças de skill/agente aos cinco kits derivados **fora deste plano** (§7); o plano altera só o hub | Regra do hub: propagação é ato de sincronização próprio, com divergências por linha a preservar |
| `DTG-9` | Hook novo (`PostToolUse` ou outro) **só** entra no plano se a sonda medir que ele altera o que a tela mostra (`Q-6` c); caso contrário, hooks ficam fora do escopo e nenhum card os toca. **Ativada por `DTG-12`/`DTG-18` (2026-09-24):** o `PostToolUse` entra por ato do dono, não pela linha (c) da `### 2.2` — (c) mediu `não` na extensão, e é por isso que a tela sai dela; o hook grava em arquivo, não em stdout | Evita entregar mecanismo que não muda o observável do dono |
| `DTG-10` | O template mora na `### 4.1` deste plano — residência normativa, autoria do planejador na Fase 3b, validada pelo dono no Marco 1 como worked example. `OP-2`/`TLG-T2` o **materializa** na `scrum-master` (seção nova `## Repertório de mensagens ao gerente`, tabela copiada da `### 4.1`), e a partir daí a seção da skill é a residência **vigente** para o condutor: `TLG-T4` e `TLG-T5` citam a seção da skill pelo nome e não recopiam o template | Concilia `DTG-5` com `OP-2` (tensão 2): o dono julga a forma antes de a skill existir (`R-4`), e o condutor lê a skill, não o plano. A relação é a de `Texto novo, literal` com o arquivo que o recebe |
| `DTG-11` | **Retirada por `DTG-26` (2026-09-24).** Texto original: a rota do deslocamento (`DTG-4`) é a **fusão** num instrumento novo do kit, `.claude/tools/loop.py`, com três verbos — `abrir`, `despachar`, `fechar` — que encapsulam por `subprocess` os doze atos de `F-7` dos passos 2, 3, 4 e 9 sobre os instrumentos existentes, sem reimplementar nenhum. O `review_evidence.py` dos passos 6 e `B0` fica como está (já é um único comando do kit). **Nenhuma chamada migra para dentro de agente** | O modelo declara `mente do agente` inalterada e a tensão 5 manda escalar alteração de agente, não absorvê-la; não existe subagente de fechamento a quem delegar `rdo.py close`. Entre dois despachos restam **um** `loop.py` por momento do loop (`fechar` entre a revisão e a próxima tarefa; `despachar` depois dos gates de julgamento; `abrir` só na abertura da janela) |
| `DTG-12` | Decisão do dono no Marco 2 sobre `R-1`, 2026-09-24: **opção 2 — tela fora da extensão** (arquivo de progresso alimentado por hook `PostToolUse`, lido em outro painel). Verbatim: *"Registre 2. Eliminar esse resíduo é exatamente o objetivo deste plano"* — dado depois de ver o resíduo medido na janela de 2026-09-24: cerca de 90 chamadas internas de subagente renderizadas no topo contra cerca de 35 chamadas do condutor, estas as únicas que `TLG-T3` corta. Consequências já mapeadas pelo consultor (acionamento 2): revoga `DTG-1` (a tela deixa de ser só o painel da extensão), retira o item correspondente da §7 e ativa `DTG-9`; exige emenda da `## 1` e operação nova. O plano retoma pela triagem do consultor sobre esta decisão (rotas `modelador` e `planejador`) antes de qualquer card; `TLG-T3` segue `blocked` até essa triagem, e a contingência 2 dela não se aplica enquanto a triagem não fechar | Ato do dono no Marco 2 (`G-NOASK`); a medida que o sustenta é a `### 2.2` e a contagem de chamadas por agente em `docs/telemetria.tsv` (2026-09-24) |
| `DTG-13` | Ordem **linear** `TLG-T1 → T2 → T3 → T4 → T5`, sem paralelismo. Substitui o item 2 da `## 6` original (template em paralelo com a sonda) | `OP-2` precisa do objeto que `OP-1` origina (§1, tensão 1); `T2`, `T3` e `T4` editam o mesmo `scrum-master/SKILL.md` — dois subagentes no mesmo arquivo em paralelo conflitam |
| `DTG-14` | `TLG-T1` é executada **no topo** pelo agente que conduz a sessão, modelo Sonnet, com o dono presente — nunca despachada a `pantonic-executor`: o objeto medido é a tela do topo, e o próprio despacho de um subagente é a forma (b) da sonda. A forma (c) exige um `PostToolUse` gravado em `.claude/settings.json` **antes** de a sessão de observação abrir (o harness lê os hooks na abertura — `F-9` mostra que hoje não há nenhum), e o bloco é removido ao fim da sonda | Medida de dentro de um subagente não vale: o que se mede é o fluxo principal. Único caso do plano em que um card roda sem `passagem-de-bastao` |
| `DTG-15` | `TLG-T4` reescreve também `passagem-de-bastao/SKILL.md:10-13` — a frase "o que chega ao dono chega pelo relatório de encerramento, e só lá" (`F-8`) deixa de ser verdadeira com o repertório — e nada mais nessa skill | Colateral nomeado no card, não absorvido em silêncio; a `passagem-de-bastao` continua sem chamada de topo (`F-7`) |
| `DTG-16` | Reparo do card `TLG-T1` em `review` (consultor, acionamento 1, 2026-09-24, `AE-1`): o rótulo `O que tem de existir ao final` vira `Pronto quando (o fato que tem de existir ao final)`, que `rdo.py` normaliza para `pronto-quando`; Verificação 1 e 2 ancoram em início de linha (o card cita os dois padrões, indentados, e a contagem literal dava 4 e 3); Verificação 4 e a contingência de `json` deixam o `git` e conferem o `settings.json` por conteúdo, porque ele é ignorado (`.gitignore:5`). Entrega não muda; o card segue `review` | `review_evidence.py` recusou o card (`campo obrigatório ausente … 'pronto-quando'`); os números novos e o `exit 0` do instrumento foram medidos, não deduzidos (`DM-12` do `P-0740`) |
| `DTG-17` | Triagem do Marco 2 (consultor, acionamento 2, 2026-09-24, `AE-2`): com o veredito `não` da `### 2.2`, a fila segue pela `## 6` item 1 como pré-decidida — `TLG-T2` roda (o repertório é independente da sonda, `R-1`); `TLG-T3` é materializado `blocked` razão `premissa` **já agora** (`backlog.py status`, exit `0`), em vez de despachado para parar na contingência 1, e `TLG-T4`/`TLG-T5` seguem atrás dele pela dependência. A janela fecha depois de `TLG-T2`, sem tarefa elegível, e a pergunta de `R-1` (com a confirmação de (d)) vai ao dono no relatório de encerramento. Preenchida `DTG-12`, `TLG-T3` volta a `ready` pelo mesmo instrumento; se o dono escolher a tela alternativa, o caso volta ao consultor antes (muda `DTG-1` e a `## 1` → `rota=modelador`, operação nova → `rota=planejador`) | Economiza um despacho de executor e um acionamento que só reproduziriam a parada; nada decidido sobre `R-1` — é do dono (`G-NOASK`) |
| `DTG-18` | Triagem de `DTG-12` (consultor, acionamento 3, 2026-09-24, gatilho 4): `rota=modelador`, sem `estrategico=` — a mudança de escopo é o próprio ato do dono, e a triagem não a alarga nem revoga decisão dele (`DTG-1` era do planejador, §3). Aplicado já: `DTG-1` revogada em parte, `DTG-9` ativada, a exclusão da tela alternativa sai da §7. O loop despacha o modelador com o dossiê `Ato de modelo` de `emenda` (versão 2 pendente: a tela do monitor passa a ser o arquivo de progresso lido em outro painel, operação nova para o hook, e OP-3/OP-4/OP-5 reavaliadas contra a tela nova). `TLG-T3`/`TLG-T4`/`TLG-T5` seguem `blocked`/atrás até a emenda ser aceita no marco (o consultor valida a pendente antes do dono); aceita, o caso vai à rodada do planejador (`rota=planejador`: card da operação nova, lastro `tarefas:`, destino de `TLG-T3`..`T5` e o defeito de Verificação do `AE-3` (i)) | Ato do dono no Marco 2; a `## 1` vigente define a tela como o painel da extensão (§1.1) e não tem operação que ligue hook — é drift de objeto e de operação, guarda do modelador (`GOVERNANCA.md` §3.2) |
| `DTG-19` | Validação da versão 2 pendente da `## 1` (consultor, acionamento 4, 2026-09-24, gatilho 4, primeira instância da `GOVERNANCA.md` §3.2): **conforme** — um objeto de escopo só (`stream de dados`), `tela do monitor` segue medição e constante, `tarefa` e `mente do agente` intactos; `OP-1`/`OP-2` idênticas à v1; `OP-3` nova casa com `DTG-12` (hook `PostToolUse`, arquivo de progresso, painel fora da extensão, chamadas internas de subagente fora do arquivo) e com as duas vias da §0; `OP-4`/`OP-5` reavaliadas contra o painel novo; exclusão do `PantonicMonitor` (`DTG-1`, parte viva) preservada. `V1 OP-3` (tarefa vazia) é lastro do planejador; `V13` é artefato da conferência isolada da `## 1A`. Tensão (1) não condiciona o aceite (o estado final do arquivo é o mesmo com ou sem disparo em subagente: o filtro do repertório exclui por construção); tensão (2) não condiciona o aceite do modelo, condiciona a execução: o card de `OP-3` abre por medida técnica curta do caminho da linha do condutor ao gancho, e caminho nenhum → para e sobe ao dono como estratégico. Sobe ao dono no marco; aceita → `rota=planejador` | Primeira instância da validação é do consultor; a segunda é do dono (`GOVERNANCA.md` §3.2). `modelo.py check` exit `0` (v1 vigente, 5 op); `backlog.py next` "nada delegável · blocked 1", exit `0` |
| `DTG-20` | Rodada do planejador (`G-REPLAN`, rota `planejador` de `DTG-19`, 2026-09-24) sobre a versão 2 aceita: `TLG-T3` é **reescrito** para a `OP-3` nova (gancho e arquivo de progresso) e recebe o lastro `tarefas: TLG-T3, TLG-T3a, TLG-T3b`; nasce o card corretivo `TLG-T2a` da `OP-2` (as colunas *momento* e *lacunas* de sete linhas do repertório citam `loop.py`, que deixa de existir por `DTG-26`; as frases-modelo, forma `A` do Marco 1, não mudam), com o lastro `tarefas: TLG-T2, TLG-T2a, TLG-T2b`; `TLG-T4` e `TLG-T5` são reescritos contra o painel. Ordem linear `TLG-T3 → TLG-T2a → TLG-T4 → TLG-T5` (substitui `DTG-13` a partir de `TLG-T3`): `TLG-T3` vai primeiro porque abre pela medida que pode derrubar a rota e mandar o caso ao dono, antes de gastar despacho no resto; `TLG-T2a` e `TLG-T4` editam a mesma skill e ficam em série. `I-10` revogada e `I-5` reescrita; `R-2` e `R-5` retirados (tratavam a fusão em `loop.py`); `R-6` e `R-7` novos | Insumo transcrito do consultor em `DTG-19` e na nota de acionamento 4 do cenário; a §3.2 de `GOVERNANCA.md` põe o lastro `tarefas:` e o card corretivo `T<n>a` com o planejador, não com o modelador |
| `DTG-21` | Tensão (2) da `### 1.3` — **rota do transcript**: o gancho lê o `transcript_path` do JSON de entrada (`F-20`) e extrai as linhas do repertório das entradas `"type": "assistant"` com bloco `"type": "text"` do transcript da sessão principal (`F-19`), a partir de um cursor de bytes por transcript. A linha **não** viaja dentro de um ato de ferramenta. `TLG-T3` abre re-medindo o formato do transcript com a sonda literal de `F-19`; com `com_text 0` na linha `principal:`, caminho nenhum leva a linha ao arquivo e o card para `blocked` razão `premissa` — a triagem sobe o caso ao dono como estratégico | `F-19` e `F-20` já medem o caminho; a alternativa (a linha dentro de um ato de ferramenta) poria um comando a mais no topo por transição e mudaria a forma do repertório aceita no Marco 1 |
| `DTG-22` | Tensão (1) da `### 1.3` — **exclusão dupla, por construção**: o gancho sai sem gravar nada quando o JSON de entrada traz `agent_type` não vazio (chamada de dentro de agente despachado, `F-20`, mesmo teste de `ocupacao.py:147`), e, ao ler o transcript, pula toda entrada com `isSidechain` verdadeiro (`F-19`) | Os ganchos disparam nas chamadas internas (`F-20`); cada uma das duas barreiras sozinha já basta nos dados medidos, e as duas juntas cobrem o caso de o harness mudar o `transcript_path` entregue ao subagente |
| `DTG-23` | **Forma da narração que o gancho leva ao arquivo** (a "forma" da `OP-4`): cada linha do repertório é escrita pelo condutor **sozinha numa linha** do texto dele, começando pelo marcador literal `[gerente] ` (colchete, a palavra `gerente`, colchete, um espaço) seguido da frase-modelo preenchida. O gancho grava uma linha de texto se e só se, sem espaços nas pontas, ela começa por `[gerente] ` **e** o resto começa por um dos sete inícios das frases da `### 4.1`: `Abrindo a janela do plano `, `Tarefa `, `Agente executor `, `Agente revisor `, `Agente consultor `, `Agente modelador `, `Scrum master `. No arquivo vai o resto, **sem** o marcador | Sem marcador, uma linha do relatório de encerramento que comece por `Tarefa ` entraria no arquivo; o marcador fica só na extensão, que o dono deixa de ler (`DTG-12`), e o arquivo guarda a frase pura. Consumida por `TLG-T3` (reconhecedor) e `TLG-T4` (regra da skill) |
| `DTG-24` | **Residência**: arquivo de progresso `.claude/estado/progresso.txt` (UTF-8, uma linha por transição, `\n`); cursor `.claude/estado/progresso-cursor.json` (objeto `{<transcript_path>: <offset em bytes>}`); ambos ignorados pelo git pela regra vigente `.claude/estado/*` — fato de uma sessão numa máquina, nunca versionado. Script `.claude/tools/progresso_hook.py` e teste `tests/test_progresso_hook.py`, versionáveis. A sonda do passo 1 de `TLG-T3` vive em `.claude/estado/sonda_transcript.py`, ignorado, e é apagada no mesmo card. `.gitignore` não muda | `F-22`, medido; o `.claude/estado/` já é o slot de estado de sessão do loop (comentário do `.gitignore`) |
| `DTG-25` | **Declaração do gancho**: em `.claude/projecoes.json`, alvo `projeto`, dois eventos com o mesmo comando `python {KIT_ROOT}/tools/progresso_hook.py` — `PostToolUse` com matcher `.*` e `Stop` sem matcher —, aplicados por `python .claude/tools/materializar.py apply --alvo projeto`; o `.claude/settings.json` não se edita à mão. O `Stop` existe para gravar as linhas escritas **depois** do último ato de ferramenta do turno (o `M-12` antes do relatório de encerramento), que nenhum `PostToolUse` alcança | `.claude/settings.json` é ignorado (`F-21`, `AE-2` do `P-0740`); sem o `Stop`, o `M-12` nunca chega ao arquivo e o estado final da `OP-3` ("as linhas do repertório, uma por transição") não se alcança. O `Stop` altera a mesma propriedade da mesma operação e não chama nada novo — registrado aqui como rota técnica, e levado ao modelador no retorno desta rodada para que ele diga se a letra da `OP-3` ("depois de cada ato de ferramenta") pede emenda |
| `DTG-26` | **`DTG-4` e `DTG-11` retiradas**: não há `loop.py`, nenhum ato do condutor migra nem se funde, e as chamadas que ele faz no topo ficam como estão | Sem operação na v2: a `OP-3` nova não enxuga o topo da extensão — o dono deixa de lê-la (`DTG-12`) e o arquivo exclui toda saída de ferramenta por construção (`DTG-21`, `DTG-23`) |
| `DTG-27` | **O painel**: o terminal integrado do VS Code, aberto na raiz do repositório, rodando `Get-Content -Path .claude/estado/progresso.txt -Wait -Tail 30 -Encoding utf8`. O arquivo nasce com a primeira linha narrada; o `README.md` diz como abrir o painel (`TLG-T5`) | É "outro painel" fora da extensão (`DTG-12`), sem instalar nada; `-Wait` segue o arquivo em tempo real, que é o que o dono pediu (*"real time"*, §0) |
| `DTG-28` | **Verificação por `numstat`** (`AE-3` (i)): nenhum card mede `git diff --numstat` contra `HEAD` em arquivo com alteração não commitada; a forma é o **delta** contra a base re-medida no despacho — base `<a> <r>`; depois, removidas `= <r>` e adicionadas `≥ <a> + <n>` para inserção pura. Onde o card substitui linhas que já são alteração não commitada (`TLG-T2a` troca linhas que `TLG-T2` inseriu), o `numstat` não muda nos dois mundos e **não** se usa: o aceite é por conteúdo, com antes e depois | `AE-3` (i), medido na `TLG-T2`; a régua de autoria já traz a forma (`TK-78b`) |
| `DTG-29` | **Ato do dono, 2026-09-24, ao ler o relatório da janela que fechou `TLG-T3`, `TLG-T2a` e `TLG-T4` — o Marco 3 antecipado sobre corpus real.** Verbatim: *"Eu acho que está convergindo para o que eu desejo. Verifique se essas mensagens estão padronizadas por meio de funções, e não escritas agênticas. Isso padronizaria o stream de dados, e permitiria agregações sem custo em token. E uma agregação dessa função de stream out é fazer replace do código da tarefa por uma descrição resumida dela. Só referenciando siglas não efetivamente agrega para a comunicação homem máquina. Com relação ao conteúdo apresentado, minha única crítica é o termo 'evidência mecânica', que é vago. Eu precisaria de um detalhamento maior do que seria essa evidência mecânica, para intervir antes dela ser elaborada caso eu entenda que não é o que se espera."* Três mudanças no que o plano entrega: **(1)** a linha do stream é **produzida por função do kit** a partir do evento de cada transição do loop, e não escrita pelo condutor como texto — o gancho deixa de filtrar o texto do agente pelo marcador e passa a gerar a linha; **(2)** a função **agrega**: o identificador da tarefa sai substituído pela descrição resumida dela (o título do card), e o do plano pelo título do plano — sigla sozinha não comunica; **(3)** a linha que anuncia a coleta de evidência **diz o que se coleta** (o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado da bateria de testes e guardas), em vez do termo vago "evidência mecânica", para que o dono possa intervir antes de ela ser elaborada. Resposta do condutor no mesmo ato, confirmada por leitura da skill e do gancho: hoje nenhuma função monta a frase — o repertório é tabela de frases-modelo e o condutor as escreve; o gancho só copia as linhas marcadas | Medido na própria janela (`AE-7`): as linhas narradas na `TLG-T3` e na `TLG-T2a` **não chegaram** ao arquivo de progresso — o condutor as escreveu sem o marcador antes de a `TLG-T4` instituir a regra. A narração agêntica é o ponto de falha que o ato elimina: linha gerada por função não depende da memória do agente, custa zero tokens de saída e é dado estruturado, agregável. A mudança altera a `OP-3` e a `OP-4` da `## 1` e o estado final de `stream de dados.repertório de mensagens` — vai ao modelador como emenda (versão 3 pendente) e daí à rodada do planejador |
| `DTG-30` | **Mecanismo (rodada 2, técnico):** a linha do stream é gerada por `progresso_hook.py` nos eventos `PreToolUse`, `PostToolUse` e `Stop` da sessão principal, que **derivam** a transição de `hook_event_name` + `tool_name` + `tool_input` + `tool_response` (`F-30`) e de um estado próprio da sessão (`DTG-31`), sem nenhum ato novo do condutor: `backlog.py next` (tarefa escolhida / fila vazia), `backlog.py status <ID> <estado>` (estado mudado / tarefa fechada), `Agent` com `subagent_type` (agente despachado no `PreToolUse`, agente de volta no `PostToolUse`), `review_evidence.py --tarefa` (evidência coletada) e `Stop` (janela encerrada). A tabela evento → frase é a `### 4.1` (versão 3). Alternativa rejeitada: instrumento `emitir` chamado pelo loop — ainda depende de o condutor lembrar, que é o ponto de falha medido em `AE-7` | Zero tokens e impossível de esquecer: cada transição do loop já é um ato de ferramenta com entrada estruturada (`F-29`). O `PreToolUse` é necessário porque a linha que anuncia um despacho tem de sair **antes** do retorno, e porque comando com erro não dispara `PostToolUse` (`AE-6`) |
| `DTG-31` | **Residência:** `progresso_hook.py` é **reescrito no lugar** (mesmo caminho, mesmo comando nos ganchos): perde a leitura do transcript, o marcador, os inícios e o cursor (`progresso-cursor.json` é apagado por `TLG-T3b`); ganha `FRASES` (os templates, cópia literal da coluna *frase gerada* da `### 4.1`), `texto_da_resposta`, `localizar_card`, `evento` e o estado próprio `.claude/estado/progresso-estado.json` (objeto `{"sessao", "aberta", "encerrada", "tarefa", "titulo", "objetivo", "titulo_plano", "tarefa_fechada", "titulo_fechada"}`, reiniciado quando `session_id` muda). A trava `progresso.lock` e as duas barreiras de `DTG-22` (`agent_type`) continuam; a de `isSidechain` deixa de existir com o transcript. `tests/test_progresso_hook.py` é reescrito: os nove `TF-PROG` saem, entram os `TF-CAP` (`TLG-T3a`) e os `TF-GER` (`TLG-T3b`). Em `.claude/projecoes.json` o `PreToolUse` do alvo `projeto` ganha uma **segunda entrada** (matcher `.*`, comando `progresso_hook.py`), ao lado da de `ocupacao.py`; `PostToolUse` e `Stop` ficam como estão (`DTG-25`), matcher `.*` mantido nos três porque é a forma medida (`F-21`) | Um script, um comando, um estado: o que `TLG-T3` instalou continua declarado e materializado do mesmo jeito (`F-25`); só o conteúdo do script muda. O estado próprio existe porque o evento `Agent` não traz o id da tarefa e o `next` seguinte precisa saber qual tarefa fechou (`M-11`) |
| `DTG-32` | **Medida antes da implementação:** `TLG-T3a` (`classe investigacao`) instala em `progresso_hook.py` uma **captura de payload** — função `capturar(payload, estado)`, ativa só quando existe o arquivo-flag `.claude/estado/progresso-captura.on`, que grava uma linha JSON por gancho em `.claude/estado/progresso-captura.jsonl` (evento, ferramenta, chaves de `tool_input`, comando ou `subagent_type`, tipo e chaves de `tool_response` e o JSON dela truncado em 2000 caracteres) — e cria o flag. O ciclo de `TLG-T3a` e o de `TLG-T2b` (retorno do executor e do revisor pela `Agent`, `backlog.py`, `review_evidence.py`, `rdo.py`) enchem a captura na sessão principal; `TLG-T3b` abre lendo esse arquivo e confirma que a resposta de `Agent` e de `Bash` cai numa das formas que `texto_da_resposta` normaliza (`DTG-33`), ou para em `premissa`. A captura fica como recurso permanente do gancho, desligada: `TLG-T3b` apaga o flag e o `.jsonl` | `F-30`: a forma de `tool_response` não está medida e não é medível de dentro de um executor; implementar a extração sobre forma suposta é escrever a saída "de memória" (`pantonic-planner`, Fase 4 item 11). O gancho carrega na própria sessão (`AE-6`), por isso a captura instalada por `TLG-T3a` já mede o retorno da própria `TLG-T3a` |
| `DTG-33` | **Agregação e normalização:** (i) `texto_da_resposta(resp)` devolve `resp` se `str`; se `dict`, o valor `str` da primeira chave presente entre `stdout`, `output`, `text`, `result`, `response`, ou, com `content` lista, os `text` dos blocos `dict` de `type` `text` unidos por `\n`; caso contrário `json.dumps(resp, ensure_ascii=False)`; `None` → `""`. (ii) `localizar_card(id, raiz)` varre `raiz/docs/plans/P-*.md` (ordem alfabética) e depois `raiz/docs/DIARIO_DE_OBRAS.md`; o card é a primeira linha que casa `^### <ID escapado> — (.+?) \[`; título = grupo 1; objetivo = primeira linha `- **Objetivo:** ` depois do cabeçalho e antes da próxima linha `### `, sem o rótulo, truncado em 240 caracteres com `…`; título do plano = em arquivo `P-*.md` a linha 1, em outro arquivo a última linha `## ` antes do card — em ambos sem os `#`, sem espaços nas pontas e sem o prefixo `<id> — ` (regex `^#+\s*(?:\S+\s+—\s+)?(.*)$`). Card não encontrado → título = o próprio `<ID>`, objetivo `""`, título do plano `""` (e `M-0` não sai). (iii) Nas frases, título da tarefa e do plano vão entre aspas duplas: `Tarefa "O gancho que grava o arquivo de progresso"`. (iv) O id da tarefa corrente vem, nesta ordem, do estado próprio (`tarefa`), de `.claude/estado/tarefa-corrente.json` (`tarefa`) ou, no `status`/`review_evidence.py`, do próprio comando; nenhum → `(tarefa não identificada)` | Ato do dono (`DTG-29` (2)): sigla sozinha não comunica; o título do card é a "descrição resumida". Corpus fechado e leitura local: nenhuma chamada de ferramenta, nenhum import de instrumento do kit. Fallback ao id mantém a linha no painel em vez de perdê-la |
| `DTG-34` | **Lacunas sem campo de evento** (decididas aqui, não pelo executor): `M-8` perde `(regra <A-n ou B-n>: <uma frase>)` — a regra que casou não é campo de nenhum evento; `M-12` perde `regra B1..B3` e ganha duas formas: com tarefa fechada na sessão e sem; `M-14` lê `<ato>` de `Ato:\s*`?(autoria|emenda|conflito)` no `prompt` do despacho e, sem casamento, usa a forma `M-14b` (*vai atualizar o modelo*); `M-3` sem objetivo usa `M-3b`; `M-4`/`M-7`/`M-9` fora da gramática de `F-29` caem em `M-16` (primeira linha da resposta, até 160 caracteres); `M-15` (planejador despachado) e `M-17` (`Stop`, uma vez por sessão aberta) são novas; `M-0` sai só na primeira tarefa escolhida da sessão. `M-1` deixa de repetir `<ID>`: `Tarefa "<título>". Passo: …`. As demais frases mudam só a sigla pelo título | `I-3` na versão 3: toda lacuna se preenche pelo campo do evento; lacuna sem campo é defeito de autoria, não do executor (`R-3`). O dono viu a forma `A` e disse *"convergindo"*: as frases mudam o mínimo que o ato pede |
| `DTG-35` | **A frase da evidência** (`M-5`), verbatim do aceite do dono nesta rodada: `Tarefa "<título>": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.` | Ato do dono (`DTG-29` (3)): o termo "evidência mecânica" era vago; a frase diz os três blocos que `review_evidence.py` produz (`F-32`) para que o dono intervenha antes |
| `DTG-36` | **Revogações e reescritas:** `DTG-21` (rota do transcript) e `DTG-23` (marcador e inícios) **revogadas** — o gancho não lê texto do condutor; `DTG-10` **reescrita**: a `### 4.1` segue residência normativa (o que o dono valida), `FRASES` em `progresso_hook.py` é a residência **vigente** (o que gera a linha) e a seção da `scrum-master` é cópia legível para o condutor, com igualdade verificada nos dois sentidos (`TLG-T2b` Verificação 3 contra a `### 4.1`; `TF-GER-18` de `TLG-T3b` contra a skill); `DTG-14` "reabrir a sessão" **caída** (`AE-6`: o gancho carregou na própria sessão) — a `## 6` deixa de pedir reabertura; `DTG-25` mantida e estendida ao `PreToolUse` (`DTG-31`); `DTG-27` mantida; `I-2`, `I-3`, `I-5` e `I-11` reescritas na `## 4`; `DTG-6`/Marco 3: a validação final continua sendo o dono lendo o painel durante `TLG-T5`, agora com linhas geradas, e no mesmo ato promove a `## 1A` | Consequência de `DTG-29` (1): tudo o que descrevia a narração pela mão do condutor deixa de ser verdadeiro; o que descrevia o arquivo, o painel e o comando de leitura continua |
| `DTG-37` | **Ordem:** `TLG-T3a → TLG-T2b → TLG-T3b → TLG-T4a → TLG-T5`, linear. `TLG-T3a` primeiro porque a captura precisa de ciclos reais para encher; `TLG-T2b` (texto, skill) roda em seguida e é o segundo ciclo capturado; `TLG-T3b` lê a captura e escreve a função, cujo `TF-GER-18` já encontra a tabela nova na skill; `TLG-T4a` depois, porque até a função existir o gancho antigo ainda copia as linhas marcadas e o painel não fica vazio; `TLG-T5` por último (Marco 3). `TLG-T2b` e `TLG-T4a` editam a mesma skill e ficam em série. Substitui `DTG-20` a partir de `TLG-T4` | Dois ciclos de captura antes da implementação; nenhuma janela com painel vazio; nenhum par de cards no mesmo arquivo |
| `DTG-38` | **Verificação da materialização** (`TLG-T3b`): depois do `apply`, `.claude/settings.json` contém `ocupacao.py` exatamente `1` vez e `progresso_hook.py` exatamente `3` vezes, e passa em `json ok`; contagem diferente → `blocked` razão `ferramenta`. A segunda entrada do `PreToolUse` entra no `projecoes.json` como novo objeto do array, imediatamente depois do objeto de `ocupacao.py` | `F-21` mediu só eventos novos, não entrada nova em evento existente; a contagem discrimina os dois mundos (apply que substitui o array inteiro deixaria `ocupacao.py` em `0`) |
| `DTG-39` | **Agente de volta em modo hand-back (consultor, acionamento 5, `AE-8`, técnico):** quando o `tool_response` do `PostToolUse` `Agent` é `dict` com `handback == "send"` e `agentId` `str`, o gancho **não** gera linha nesse evento: grava `pendentes[agentId] = subagent_type` no estado próprio. A linha de volta sai no `UserPromptSubmit` da sessão principal cujo `prompt` começa por `<agent-message from="<agentId>">`: o relatório é o texto depois de `The report follows:` e antes de `</agent-message>`, e a primeira linha não vazia dele passa pela mesma classificação da regra 5 (`M-4`/`M-4b`/`M-7`/`M-9`/`M-9b`/`M-16`); sem pendente com aquele id → nada. `tool_response` sem essa forma segue a regra 5 como antes. Declaração: o array `UserPromptSubmit` do alvo `projeto` ganha um segundo objeto com `progresso_hook.py`, depois do de `backlog_hook.py`; a contagem de `DTG-38` passa de `3` para `4` em `projecoes.json` e em `settings.json`, e `backlog_hook.py` fica em `1` nos dois. Emenda `DTG-25`, `DTG-30`, `DTG-31`, `DTG-33` (i) e `DTG-38` só nisso; nenhuma frase nova | Medido em 2026-09-24 pelo consultor no transcript da sessão principal (`toolUseResult` das seis chamadas `Agent` da janela): `content` é lista de um bloco `text` com o ponteiro *"This agent's report was delivered to you as a message from …"*, `handback` = `"send"`, `agentType` = o `subagent_type`; o relatório chega como `queued_command` com `prompt` `<agent-message from="<agentId>">\n[Subagent hand-back] … The report follows:\n  <relatório indentado>\n</agent-message>`, e o `UserPromptSubmit` global `modelo_por_fase` (que lê `data.get("prompt")`) disparou logo depois de três desses, e só neles e no prompt inicial. A forma (c) de `DTG-33` (i) casa, mas devolve o ponteiro: `M-4`/`M-7`/`M-9` nunca sairiam. A barreira `agent_type` (`DTG-22`) fica: o texto vem de evento da sessão principal |
| `DTG-40` | **Pendência espúria e gramática de retorno (consultor, acionamento 6, `AE-13`/`AE-14`, técnico):** a escalada `B1` da `TLG-T4a` é **improcedente** — o texto de `pendencia=` (`- **Ação:** antes=10 depois=10`) é o valor de aceite da Verificação 5, medido igual antes e depois, não pendência; a entrega fica `done` como o laudo deu (`aprovado 100`), sem redespacho, e a janela segue para `TLG-T5`. O `AE-14` degrada o Marco 3 (a volta do executor de `TLG-T5` é linha que o dono lê no painel), por isso fecha agora e não na rodada: ajuste de instrumento do loop, sem card, feito pelo consultor — o passo 4 da `scrum-master` deixa a meta-notação `[pendencia=<uma linha>]` e publica duas formas literais, `<tarefa> review` e `<tarefa> review pendencia=<uma linha>`, que a `M-4` (`^(\S+) review(?:\s+pendencia=(.*))?$`, `progresso_hook.py:186`) casa; a `M-4` fica como está. Medido: `review [pendencia` na skill `1 → 0`, `<tarefa> review pendencia=<uma linha>` `0 → 1`; `de_volta('pantonic-executor', …)` dá `M-4` para `TLG-T5 review` e `TLG-T5 review pendencia=x y` e `M-16` para a forma com colchete; `tests/test_progresso_hook.py tests/test_rdo.py` `75 passed`; `backlog.py next` → `TLG-T5`, `modelo.py check` exit `0` (v3). Nenhum card de `TLG-T5` manda colar valor de aceite na linha de retorno (conferido), logo o `AE-13` não recorre neste plano. `AE-9`, `AE-10`, `AE-12` (defeitos da `OP-3` entregue em `TLG-T3b`) não bloqueiam o Marco 3 — o fluxo normal da janela vê o `M-1` e o título sai (`progresso.txt:38`) — e vão, num **único** card corretivo `TLG-T3c` da `OP-3`, ao acionamento do consultor no Marco 3, junto com a retroação que a leitura do dono pedir (`TLG-T5`, *Fora do escopo*): não é replanejamento, não cria operação. |
| `DTG-41` | **Marco 3 — triagem do consultor (acionamento 7, gatilho 4, técnico/tático):** (a) a **versão 4 pendente da `## 1A` é conforme** e sobe ao dono no marco: só o texto da `OP-2` muda, e passa a dizer o que a `I-3`, o estado final de `stream de dados.repertório de mensagens` (idêntico nas versões 3 e 4) e as entregas de `TLG-T2b`/`TLG-T3b` já dizem — a lacuna se preenche pelo campo do evento, pelo estado da sessão ou por leitura local da função, nunca pela mão do condutor; nenhum objeto, propriedade, estado final ou outra operação muda, e nenhum lastro novo é exigido, porque o Ato é `conflito` (a letra que a versão 3 deixou para trás), não drift. (b) `AE-9`, `AE-10`, `AE-12` e `AE-16` → card corretivo **`TLG-T3c`** (`OP-3`): o título sobrevive ao `SubagentStop` (o fallback de `tarefa-corrente.json` e as regras 2 (`in-progress`) e 3 (`--tarefa`) gravam `tarefa`, `titulo` e `objetivo` no estado próprio); `texto_da_resposta` volta à semântica fechada de `TLG-T3b` (`content` sem texto → `""`); as regras 2 e 3 deixam de ser excludentes; o estado de `backlog.py status` passa a `([a-z-]+)`, para `done;` colado ao separador — a linha `M-10` da `### 4.1` mudou neste ato e a cópia da skill muda no card; nenhuma verificação roda o gancho contra o `.claude/estado/` vivo (`AE-10`). Medido pelo consultor numa cópia do gancho em pasta temporária: os 22 TF vigentes passam com a semântica nova, os cenários de `TF-GER-20`..`22` dão as linhas literais do card, e o gancho vigente dá `(tarefa não identificada)` ou nenhuma linha nos mesmos cenários. (c) `AE-15` → card corretivo **`TLG-T5a`** (`OP-5`): a célula da `scrum-master` volta a ter a cláusula `pelo fim do plano ou pela condição de contexto` colada a `encerra a janela`, e a cláusula do gancho vira o fim da frase. (d) Ordem: veredito do dono no Marco 3 → `TLG-T3c` → `TLG-T5a` — esta roda com o gancho corrigido e é a conferência dele no painel. Nenhum dos dois é rota `planejador`: nenhuma operação nasce ou cai | O `M-5` que faltou na `TLG-T5` (`AE-16`) é o caso que o `R-6` previu (linha faltando → `TLG-T3c`): a skill não proíbe encadear comandos, então a detecção tem de tolerar o encadeamento — o defeito é do gancho, não da condução. A versão 4 corrige a letra, não o que o plano entrega |
| `DTG-42` | **Ato do dono no Marco 3 (2026-09-24), verbatim:** *"Acho que a forma está ok, mas ainda precisa de uns ajustes na confiabilidade. Por exemplo, no ponto 1 você citou um ponto de perda de informação. Se já está identificado, esse ponto precisa ser corrigido. No ponto 3, você comentou que o scrum master escreve que encerrou a janela, mesmo que ele continue. Informações não confiáveis degradam a confiança de todo o framework. Se já está mapeado, corrija"*. Leitura: (a) a forma das frases está aceita — a palavra "parada" da `M-8` (`AE-17` (ii)) fica só registrada; (b) a confiabilidade **não** está aceita e o Marco 3 não fecha: todo ponto já mapeado de linha perdida (ponto 1: `AE-16`, e com ele `AE-9`) ou de linha que afirma o que não aconteceu (ponto 3: `AE-17` (i)) é corrigido antes do aceite; (c) o ponto 2 — aceitar a versão 4 da `## 1A`, só o texto da `OP-2` — ficou sem resposta: a versão 4 segue pendente | Ato do dono; o técnico e o tático do reparo são do consultor (`DTG-43`) |
| `DTG-43` | **Reparo do veredito do Marco 3 (consultor, acionamento 8, técnico/tático):** o `TLG-T3c` já cobria o ponto 1 inteiro (`AE-16`: `&&`, `;` e quebra de linha; `AE-9`: título depois do `SubagentStop`) e passa a cobrir também: (i) `AE-17` (i) — a `M-17` só sai no `Stop` que segue o relatório de encerramento, reconhecido pelo `modelo.py show` que o abre (`scrum-master/SKILL.md:286-287`, único uso no loop), e fecha `aberta`, de modo que a continuação na mesma sessão aparece como janela reaberta (`M-0`); `Stop` sem relatório não gera linha; (ii) `AE-18` — `rota=` e `estrategico=` só contam no início de linha, e prosa que cita `estrategico=` deixa de gerar a `M-9b`. Mudam neste ato as linhas `M-9`, `M-9b` e `M-17` da `### 4.1` (a coluna *frase gerada* não muda) e o estado próprio de `DTG-31` ganha a chave `relatorio`. Mantêm-se: `AE-6` fecha sem ação (o mecanismo que ele descrevia saiu com `DTG-30`/`DTG-36`); os demais pontos de perda previstos (`R-6` caminho absoluto, `R-7` concorrência) já têm resposta no código entregue. Nenhum card novo, nenhuma operação nova, nenhuma mudança na `## 1`: não é rota `modelador` nem `planejador` | Medido pelo consultor numa cópia do gancho em pasta temporária: com a semântica nova, os 22 TF vigentes passam menos o `TF-GER-12`, cuja asserção é a que o dono recusou, e os cenários de `TF-GER-12` reescrito, `TF-GER-23` e `TF-GER-24` dão as linhas literais do card; o gancho vigente dá a `M-17` no primeiro `Stop` e a `M-9b` com `` `.. `` para prosa — a mesma linha que o painel mostrou em `progresso.txt:54`. Uma linha falsa no painel é o que o dono recusou; uma linha omitida no fim de turno sem relatório não é perda, porque nesse ponto não houve transição |
| `DTG-45` | **A parada `premissa` da `TLG-T3d` é improcedente (consultor, acionamento 10, técnico/tático):** o executor leu a linha esperada do revisor na `TF-GER-25` como `M-7`, mas ela é a `M-16` (`Agente <papel> devolveu …: <primeira linha>.`), que o corpo sem id produz — medido no gancho da árvore, a lista do card sai igual. Para não reproduzir a dúvida, o corpo do `r1` passa à forma canônica `TLG-T9 aprovado 100 bloqueante=nenhuma` e a linha esperada à `M-7` (`aprovado 100%, bloqueante nenhuma.`), medida também. A edição parcial do gancho fica na árvore (Verificação 3 já `1 1 3 1`): o passo 2 passa a conferir, a contingência 2 e a "antes" da Verificação 3 passam a `1 1 3 1`. Redespacho sem consumir retentativa. |
| `DTG-44` | **O sinal da `M-17` é só o do encerramento real (consultor, acionamento 9, técnico/tático, sob `DTG-42`):** o `AE-19` é caso mapeado de linha que afirma o que não aconteceu, e o `DTG-42` manda corrigir o mapeado — vai a card, não a "inconclusivo". Três condições, cada uma fechando um caminho medido: (i) só grava `relatorio` o `modelo.py show` **sem** `--drift` nem `--pendente` — a forma exata que abre o relatório (`scrum-master/SKILL.md:286-287`); as outras duas são leituras do modelo, e o condutor roda `--drift` em pausa de marco; (ii) `relatorio` sai no despacho de agente seguinte e no `backlog.py next` — a janela que continua depois do `show` o desarma; (iii) `Stop` com agente despachado ainda sem volta (`pendentes` não vazio) não gera a `M-17` — é o fim de turno de quem espera o hand-back, e um `show` pedido pelo dono nesse intervalo não encerra nada; para (iii) não perder a `M-17` real por entrada órfã (agente caído, `A1`), o `backlog.py next` esvazia `pendentes` — o loop só pede a próxima sem agente em voo. Descartado: sinal novo que só o encerramento emita (comando, marcador ou flag do `modelo.py`) — violaria `I-3` (nenhuma linha exige chamada nem token do condutor) e `I-2`, e o `modelo.py` não é instrumento desta operação. Card `TLG-T3d` (`OP-3`); `TLG-T5a` passa a depender dele, para o painel dela ser a prova. Muda a linha `M-17` da `### 4.1` (frase intacta) | Medido pelo consultor numa cópia do gancho em pasta temporária: com as três condições, os 27 TF vigentes passam; na sequência do `TF-GER-25` o gancho vigente grava a `M-17` no primeiro `Stop` (depois do `--drift`) e **perde** a do encerramento real, o novo grava só esta; o `TF-GER-26` dá a `M-17` com `pendentes` órfão nos dois (guarda da condição (iii)) |
| `DTG-46` | *(premissa estratégica desfeita pelo dono em `DTG-47`; rota técnica em `DTG-48`)* **O sinal da `M-17` não fica confiável se for inferido de eventos compartilhados, e a escolha é do dono (consultor, acionamento 11, estratégico):** o `AE-20` é a terceira rodada sobre o mesmo sinal (`AE-17` (i) → `TLG-T3c`, `AE-19` → `TLG-T3d`, `AE-20`). Cada reparo fechou um caminho e abriu outro, porque a `M-17` afirma uma intenção do condutor (encerrou e deu o relatório), e os eventos que o gancho vê (`modelo.py show`, `Stop`, `pendentes`, `next`) também servem a outras leituras. O exercício (a) do revisor tem a mesma sequência de eventos de um encerramento `B3` real (gate recusa a tarefa escolhida → relatório → `Stop`) seguido de retomada pelo dono: nenhuma regra sobre esses eventos declara um falso sem declarar falso o outro. O (b) depende da forma da notificação de queda de agente, que só foi medida no regime antigo; no regime `<agent-message>` vigente não há medida. A confiabilidade exige um evento que só o encerramento emita, mas o único ato de ferramenta do relatório é o `show`, que é compartilhado. Toda saída confiável toca decisão do dono. **Opções:** (A) *sinal exclusivo* — o relatório abre com uma forma que só ele usa (argumento de encerramento no `show`, ou marcador de shell no mesmo comando): exceção nomeada à `I-3` (um argumento por janela); a `M-17` sai só nesse sinal; saem os guardas `--drift`, `pendentes` e o esvaziamento no `next`; o único residual é o condutor que esquece a forma, e aí a linha se perde (não sai falsa) num relatório que já nasce fora da doutrina — **recomendada**; (B) *a `M-17` diz só o que o gancho sabe* (ex.: o condutor parou sem nada em voo): revoga em parte a forma aceita em `DTG-42` (a); (a) fica verdadeira e a retomada reabre, mas (b) segue aberto até medir a queda no regime vigente; a mesma leitura serve à `M-8` "recebe a parada" (`AE-17` (ii)); (C) *manter `I-3` e a forma e declarar os dois residuais como limite*: revoga `DTG-42` para esses dois casos, custo zero. Nenhum quarto corretivo heurístico é gravado. `TLG-T5a` espera a escolha, para o painel dela provar o sinal escolhido | Medido: queda de agente = `<task-notification>` · `<task-id>` = `agentId` · `<status>failed</status>` (transcript `e2ed8a3b-…jsonl:458-460`, 2026-09-19); zero quedas nas 5 sessões de 2026-09-24, todas no regime `<agent-message>`; o gancho da árvore só reconhece `<agent-message from=` (`progresso_hook.py:326`). Exercícios (a) e (b) do revisor no `AE-20` |
| `DTG-47` | **Ato do dono sobre `DTG-46` (2026-09-24), verbatim, em duas mensagens.** O condutor apresentou (A), (B) e (C) e disse que *"nenhuma correção confiável é possível sem mudar uma decisão que você tomou"*. Mensagem 1: *"Qual é essa decisão minha? "nenhuma correção confiável é possível sem mudar uma decisão que você tomou.""*. O condutor respondeu que era `DTG-29`, endurecida na `I-3`; que (A) contraria só a redação da `I-3`, (B) o *"a forma está ok"* de `DTG-42` e (C) o *"se já está mapeado, corrija"*. Mensagem 2: *"A frase "encerrou a janela" e conteúdo. Eu expliquei sobre forma, então não existe essa contradição; A segunda afirmativa continua válida: se você viu algum desvio e já está mapeado, corrija"*. Leitura: (a) o aceite de `DTG-42` é de **forma**, não de conteúdo: o que uma frase do painel afirma pode mudar, e cai a leitura de `DTG-42` (a) que deixava a palavra "parada" da `M-8` só registrada; (b) corrigir todo desvio já mapeado segue de pé: os dois residuais do `AE-20` e o `AE-17` (ii); (c) o dono não escolheu entre (A) e (B) nem falou da `I-3`: a rota técnica volta ao consultor (`DTG-48`); (d) o ponto 2 (aceite da versão 4 da `## 1A`) segue sem resposta, e a v4 segue pendente | Ato do dono; o técnico e o tático do reparo são do consultor (`DTG-48`) |
| `DTG-48` | **Rota (B): a `M-17` e a `M-8` dizem só o que o gancho vê (consultor, acionamento 12, gatilho 4, técnico/tático, sob `DTG-47`):** desfeita a contradição, (B) corrige os dois residuais sem sinal novo e sem tocar decisão do dono; (A) pediria token do condutor a cada encerramento, contra a letra de `DTG-29` (*"sem custo em token"*), exceção que o dono não deu — descartada, e a `I-3` fica intacta. (i) A `M-17` passa a `Scrum master mostrou o modelo do plano e aguarda; a resposta dele está na extensão.`, no `Stop` com `aberta` e `relatorio` (o mesmo `show` sem `--drift` nem `--pendente`, o mesmo desarme no despacho e no `next`); saem a guarda `pendentes` do `Stop` e o esvaziamento de `pendentes` no `next`; o `Stop` deixa de fechar `aberta` e de gravar `encerrada` e só tira `relatorio`. A frase é verdadeira nos dois exercícios do `AE-20` e no encerramento real, e a janela que segue não ganha `M-0` falso nem perde a `M-17` seguinte. (ii) A `M-8` perde "a parada da" (`Agente consultor recebe a tarefa "<título>" e vai triar.`): o consultor também é despachado por laudo, instrumento e marco (este acionamento é gatilho 4), e o `AE-17` (ii) é desvio mapeado de conteúdo (`DTG-47` (a)). `M-12`/`M-12b` ficam: saem no `nada delegável`, que é parada. Mudam as linhas `M-8` e `M-17` da `### 4.1`, a coluna *frase gerada* inclusive (`DTG-47` suspende aí o "`FRASES` não muda" de `DTG-36`). Card `TLG-T3e` (`OP-3`); `TLG-T5a` depende dele e volta a `ready`. Nenhuma operação nasce ou cai, e nenhuma mudança na `## 1`: não é rota `modelador` nem `planejador` | Medido pelo consultor numa cópia do gancho em pasta temporária: no exercício (a) do `AE-20` o gancho da árvore grava a `M-17` falsa e **perde** a real (`aberta=False` desarma o `show` seguinte); no (b), nenhuma `M-17`, com `pendentes={a1}`; o novo grava a `M-17` nova nos dois pontos de (a) e no fim de (b), com `aberta=True`. Os 29 TF vigentes com as asserções de frase e estado do card, mais `TF-GER-27`/`28` → `31 passed`; o gancho da árvore falha 7 deles (`5`, `12`, `23`, `25`..`28`) |
| `DTG-49` | **A `M-10` diz só o que o loop faz em cada estado, e tarefa parada não sai como concluída (consultor, acionamento 13, gatilho 3, técnico/tático, sob `DTG-47`):** desvio mapeado e medido de conteúdo (`AE-21`), da mesma `OP-3`, emendado no `TLG-T3e` ainda não despachado. Varredura das 23 frases contra o que a `scrum-master` faz em cada evento: só a `M-10`, a `M-11` e a `M-12` afirmam o que pode não acontecer; as demais relatam o evento ou o campo lido. (i) `done`: o passo 9 materializa, escreve o RDO e apensa a telemetria; a seleção da próxima é do bloco B, que pode parar sem `next` (`B1` com `estrategico=`, `B2`) — medido em `progresso.txt:83` → `86` —, logo "e selecionar a próxima" sai, e a seleção, quando há, é a `M-11`/`M-12`. (ii) `blocked`/`cancelled`: nem RDO (`DP-F` item 3, fechamento c; passo 9), nem próxima (o `blocked` escala ao consultor, que pode redespachar a mesma tarefa ou parar) — medido em `progresso.txt:74` → `77`; forma nova `M-10b` `Scrum master vai marcar a tarefa "<título>" como <estado>, sem RDO.`, que não grava `tarefa_fechada`. (iii) Por isso a `M-11` e a `M-12` diziam "concluiu" de tarefa `blocked`/`cancelled` — medido numa cópia do gancho da árvore (sequência do `TF-GER-29`). A `### 4.1` já mudou (`M-10` e `M-10b` nova; worked example), 24 formas; card: `TF-GER-4`/`18`/`23`/`25`/`27` ajustados, `TF-GER-29` novo, `29 → 32`, suíte `309 → +3`; contagens `gancho 1 1 3 1 1 1 0 → 1 0 3 0 0 0 1`, `skill 1 1 0 1 0 → 0 0 1 0 1`, igualdade `iguais 12 de 23 24 → 24 de 24 24` (`powershell` 5.1 e `pwsh`); numa cópia com a semântica inteira do card, `32 passed`, e o gancho da árvore falha 10 dos 32 |
| `DTG-50` | **A chave `encerrada` sai do estado do gancho (consultor, acionamento 14, gatilho 2, técnico, sob `DTG-47`):** depois de `TLG-T3e` só a regra 1 a grava, sempre `False`, e nenhum código do kit a lê (`AE-22`); a linha `M-1` da skill e da `### 4.1` a documentava como se tivesse função. Desvio mapeado → corretivo `TLG-T3f` (`OP-3`, lastro `tarefas:` na `## 1` e na `## 1A`): sai a instrução da regra 1, a `M-1` perde "`, `encerrada` = false`" (a `### 4.1` já mudou: igualdade skill × plano `24 → 23 de 24` até `TLG-T3f`), `TF-GER-2` ganha `"encerrada" not in estado_loop`; `32 → 32`, suíte `312 → 312`. A chave `encerrada` de `DTG-31` (lista do objeto) fica revogada. `TLG-T5a` passa a depender de `TLG-T3f`, para o painel dela ser o corpus final com o gancho limpo. Nenhuma operação nasce ou cai; não é rota `modelador` nem `planejador` | Medido pelo consultor numa cópia temporária: a asserção nova com o gancho da árvore dá `1 failed, 31 passed` (`TF-GER-2`); com a instrução apagada e a `M-1` trocada, `32 passed`; `encerrada 1 1 → 0 0` (gancho, skill) em `powershell` 5.1 e `pwsh`; `grep` em `.claude` e `tests`: nenhum leitor da chave |
| `DTG-51` | **O gancho tolera o caractere a mais no retorno do agente (consultor, acionamento 15, gatilho 2, técnico, sob `DTG-47`):** o revisor da `TLG-T5a` devolveu `100%` (`AE-24`) e o executor da `TLG-T4a` tinha devolvido `[pendencia=…]` (`AE-14`); nos dois casos o painel caiu na `M-16` genérica. Quem lê tolera, quem escreve segue a forma exata: a `M-7` aceita `%` depois do percentual e a `M-4` aceita colchete em volta de `pendencia=`; a gramática dos agentes (`pantonic-reviewer.md:131`, passo 4 da `scrum-master`) não muda. A `M-4` e a `M-7` da `### 4.1` já mudaram (igualdade skill × plano `24 → 22 de 24` até o card). Corretivo `TLG-T3g` (`OP-3`, lastro `tarefas:` na `## 1` e na `## 1A`), depois de `TLG-T5a`: dois padrões de `de_volta`, `TF-GER-6`/`7` estendidos, `32 → 32`, suíte `312 → 312`. O `AE-23` (prosa depois da linha) fica no tíquete, porque o gancho já lê só a primeira linha. Nenhuma operação nasce ou cai; não é rota `modelador` nem `planejador` | Reforçar o texto dos agentes não fecha a classe: o `AE-23` mostrou que uma proibição escrita no despacho não segurou três executores seguidos. Medido pelo consultor numa cópia temporária: as asserções novas com o gancho da árvore dão `2 failed, 30 passed`; com os padrões novos e a skill trocada, `32 passed`; `tolera 0 0 0 0 → 1 1 1 1` em `powershell` 5.1 e `pwsh`; `100%%` continua na `M-16`, e prosa na mesma linha depois de `[pendencia=x]` entra no texto da pendência |
| `DTG-52` | **Cada `status` do comando dá a linha dele, e a skill cita o `UserPromptSubmit` da volta em hand-back (consultor, acionamento 16, gatilho 3, técnico, sob `DTG-47`):** dois desvios mapeados na redação do encerramento viram **um** corretivo da `OP-3`, `TLG-T3h`, antes do relatório. (a) `AE-25`: a regra 2 do gancho casa só o primeiro `backlog.py status` do comando (`re.search`) → `re.finditer`, corpo inalterado. (b) `AE-26`: as linhas `M-4`, `M-7`, `M-9` e `M-16` da `### 4.1` (já mudadas aqui) e da skill, e o bullet do painel em `## Guardrails` da skill, passam a nomear o `UserPromptSubmit` por onde a volta em hand-back chega (`DTG-39`). O cabeçalho do plano, que dizia "próxima `TLG-T3a`", foi corrigido aqui (`AE-27`). `DTG-30`, a linha do `TLG-T4a` e o card `TLG-T2b` ficam como registro de quando foram escritos | Medido 2026-09-24 numa cópia temporária: `TF-GER-30` sobre o gancho da árvore dá `1 failed, 32 passed` (a lista perde a linha do segundo `status`); com `re.finditer` e a skill trocada, `33 passed`; `conta 0 1 0 → 1 0 5` em `powershell` 5.1 e `pwsh`; igualdade skill × `### 4.1` `24 → 20 de 24 24` até o card, `24 de 24 24` na cópia. A regra 3 (`review_evidence.py`) fica com `re.search`: nenhum caso medido de dois `--tarefa` no mesmo comando |

---

## 4. Invariantes de execução

Valem para todos os cards; cada card repete inline a parte que o vincula.

- **I-1** — Nenhum card modifica o harness do Claude Code, a extensão VS Code ou qualquer
  arquivo fora deste repositório, salvo `C:\Users\panta\.claude\settings.json` **e só** se um
  card o nomear em `Arquivos-alvo` com o texto vigente transcrito como fato.
- **I-2** — *(reescrita por `DTG-36`, versão 3)* Toda linha do arquivo de progresso é **gerada por
  `progresso_hook.py`** a partir do evento de uma transição do loop (`DTG-30`); nenhuma é texto
  escrito pelo condutor, saída de comando ou eco de ferramenta. *(Texto da versão 2, revogado: toda
  linha do template é texto do agente, escrita antes da chamada de ferramenta que ela anuncia.)*
- **I-3** — *(reescrita por `DTG-36`)* Nenhuma linha exige chamada de ferramenta nova nem token do
  condutor: cada lacuna se preenche por campo do evento (`tool_input`, `tool_response`), pelo
  estado próprio da sessão ou por leitura local de `docs/plans/P-*.md`, `docs/DIARIO_DE_OBRAS.md` e
  `.claude/estado/tarefa-corrente.json` feita pela própria função (`DTG-33`). Lacuna sem campo é
  defeito de autoria (`DTG-34`), nunca decisão do executor.
- **I-4** — Nenhum card afirma sobre renderização o que a sonda (`DTG-3`) não mediu; card que
  dependa de `H-<n>` cita o valor medido, não a hipótese.
- **I-5** — *(reescrita por `DTG-36`, versão 3)* A linha que anuncia um ato — despacho de agente,
  `backlog.py status`, `review_evidence.py` — é gerada no `PreToolUse` desse ato; a que relata um
  retorno — resposta de agente, saída do `backlog.py next` — é gerada no `PostToolUse`; a de
  encerramento, no `Stop`. *(Texto da versão 2, revogado com `DTG-23`: a linha vem antes do ato,
  escrita pelo condutor com o marcador `[gerente] `.)*
- **I-6** — Critério de pronto de card só cita efeito em arquivo-alvo do card e comandos que o
  executor roda; a leitura da tela pelo dono é aceite de **marco**, não de card.
- **I-7** — Piso de regressão é relação, nunca constante: `pytest tests/` não reduz o total
  re-medido no despacho.
- **I-8** — Lastro do modelo: cada operação `OP-<n>` recebe exatamente um card `TLG-T<n>`;
  card corretivo `TLG-T<n>a` materializa a mesma operação; `python .claude/tools/modelo.py check
  --plano docs/plans/P-0748-tela-do-gerente.md` sai `0` antes de qualquer publicação da §5.
- **I-9** — Toda sprint termina com a tarefa nomeada de revisão do `README.md` (G-README dever
  2; dossiê inclui `pwsh .claude/checks/check-readme.ps1` e o veredito do dono como aceite) — e
  aqui ela é também o corpus do Marco 3 (`DTG-6`).
- **I-10** — *(revogada por `DTG-20`/`DTG-26`, 2026-09-24: a proibição dependia do `loop.py`,
  retirado; as chamadas do condutor no topo ficam como estão e o arquivo de progresso as exclui por
  construção.)*
- **I-11** — *(estendida por `DTG-36`)* O arquivo de progresso só recebe linhas pelo gancho
  `progresso_hook.py`: nenhum card faz o condutor, um agente ou um instrumento escrever nele
  diretamente, e o gancho nunca imprime nada nem bloqueia a ferramenta que o disparou (falha
  aberta, `exit 0` sempre) — vale igual para o `PreToolUse`, em que `exit 2` ou JSON no stdout
  mudariam o comportamento do harness. O gancho não importa instrumento nenhum do kit e não chama
  ferramenta nenhuma: só lê arquivos locais.
- **I-12** — *(versão 3)* A sigla da tarefa e a do plano nunca chegam ao painel sozinhas: toda
  frase que nomeia uma tarefa usa o título dela entre aspas duplas (`DTG-33`); só quando o card não
  é encontrado no corpus o título é o próprio id.

### 4.1 Template de mensagens do loop — versão 3 (evento → frase gerada)

**Esta seção é a residência normativa do repertório** (`DTG-5`, `DTG-10` reescrita por `DTG-36`):
é o que o dono valida. A residência **vigente** é o dicionário `FRASES` de
`.claude/tools/progresso_hook.py` (`TLG-T3b`), cópia literal da coluna *frase gerada*; a seção
`## Repertório de mensagens ao gerente` da `scrum-master` é a cópia legível para o condutor
(`TLG-T2b`), e a igualdade das três é verificada — skill × plano na Verificação 3 de `TLG-T2b`,
código × skill no `TF-GER-18` de `TLG-T3b`. Nenhuma outra seção do plano reenuncia a tabela.
Uma linha por **forma** de frase; o sufixo `b` marca a segunda forma do mesmo evento. Toda lacuna
`<…>` se preenche por campo do evento ou por leitura local da função (`I-3`, `DTG-33`); a linha
sai no gancho nomeado na coluna *evento* (`I-5`); o condutor não escreve nada (`I-2`). Nas frases,
`<título>` é o título do card entre aspas duplas e `<título do plano>` o do plano (`I-12`).
A versão 2 desta tabela (15 frases-modelo escritas pelo condutor, forma `A` do Marco 1) foi
substituída inteira em 2026-09-24 pela rodada 2 (`DTG-29`); as frases mudam só o que o ato do
dono pede (`DTG-34`, `DTG-35`).

| id | evento (gancho · ferramenta · detecção) | frase gerada | lacunas ← campo do evento ou leitura local |
|---|---|---|---|
| `M-0` | tarefa escolhida, primeira da sessão — `PostToolUse` · `Bash` · `command` contém `backlog.py next` · resposta contém `=== PRÓXIMA TAREFA: ` · estado sem `aberta` | `Abrindo a janela do plano "<título do plano>".` | `<título do plano>` ← `localizar_card(<ID>)`; vazio → linha omitida. Sai antes de `M-11` e de `M-1` |
| `M-1` | tarefa escolhida — o mesmo evento de `M-0`, sempre | `Tarefa "<título>". Passo: conferir os gates e preparar o despacho.` | `<ID>`, `<título>` ← linha `=== PRÓXIMA TAREFA: <ID> — <título> [` da resposta. Estado ← `tarefa`, `titulo`, `objetivo`, `titulo_plano` (de `localizar_card`), `aberta` = true |
| `M-2` | estado mudado para in-progress — `PreToolUse` · `Bash` · `command` casa `backlog\.py status (\S+) in-progress` | `Tarefa "<título>": gates aprovados; vou materializar in-progress e gravar o ponto de partida.` | `<título>` ← estado se `<ID>` é a `tarefa` do estado, senão `localizar_card(<ID>)`. `status <ID> review` não gera linha |
| `M-3` | agente despachado, executor — `PreToolUse` · `Agent` · `subagent_type` = `pantonic-executor` · objetivo não vazio | `Agente executor recebe a tarefa "<título>" e vai executar: <objetivo>` | `<título>`, `<objetivo>` ← tarefa corrente (`DTG-33` (iv)) e `localizar_card`; `<objetivo>` já termina em ponto, ou em `…` se truncado |
| `M-3b` | o mesmo evento de `M-3`, objetivo vazio | `Agente executor recebe a tarefa "<título>" e vai executar o card.` | `<título>` como em `M-3` |
| `M-4` | agente de volta, executor — `PostToolUse` · `Agent` · `pantonic-executor`; se o agente entregou em hand-back (`handback` = `send` na resposta, e o `PostToolUse` só grava `pendentes[agentId]`), `UserPromptSubmit` com `prompt` começando por `<agent-message from="<agentId>">` de agente em `pendentes`, e a resposta é o trecho depois de `The report follows:` (`DTG-39`) · primeira linha não vazia da resposta casa `^(\S+) review(?:\s+\[?pendencia=(.*?)\]?)?$` | `Agente executor devolveu a tarefa "<título>": review — <pendência>.` | `<pendência>` ← grupo 2; ausente → `sem pendência` |
| `M-4b` | o mesmo evento, primeira linha casa `^(\S+) blocked motivo=(\S+)\s*(.*)$` | `Agente executor devolveu a tarefa "<título>": blocked — motivo <motivo>: <razão>.` | `<motivo>` ← grupo 2; `<razão>` ← grupo 3 |
| `M-5` | evidência coletada — `PreToolUse` · `Bash` · `command` contém `review_evidence.py` e `--tarefa <ID>`, e não contém `--atribuir` | `Tarefa "<título>": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.` | `<ID>` ← `--tarefa (\S+)` no comando; `<título>` ← estado ou `localizar_card` |
| `M-6` | agente despachado, revisor — `PreToolUse` · `Agent` · `pantonic-reviewer` | `Agente revisor recebe a tarefa "<título>" e vai confrontar a entrega com o card.` | `<título>` ← tarefa corrente |
| `M-7` | agente de volta, revisor — `PostToolUse` · `Agent` · `pantonic-reviewer`, ou o `UserPromptSubmit` da volta em hand-back, como em `M-4` · primeira linha casa `^(\S+) (\S+) (\d+)%? bloqueante=(.*)$` | `Agente revisor devolveu a tarefa "<título>": <veredito> <percentual>%, bloqueante <bloqueante>.` | `<veredito>` ← grupo 2; `<percentual>` ← grupo 3; `<bloqueante>` ← grupo 4 |
| `M-8` | agente despachado, consultor — `PreToolUse` · `Agent` · `pantonic-consultant` | `Agente consultor recebe a tarefa "<título>" e vai triar.` | `<título>` ← tarefa corrente. A regra A-n/B-n saiu (`DTG-34`); "a parada" saiu (`DTG-48`): o consultor também é despachado por laudo, por instrumento e no marco, e o evento não diz por qual |
| `M-9` | agente de volta, consultor — `PostToolUse` · `Agent` · `pantonic-consultant`, ou o `UserPromptSubmit` da volta em hand-back, como em `M-4` · uma linha da resposta começa, depois de brancos, por `rota=(\S+)`, e nenhuma por `estrategico=` | `Agente consultor devolveu a tarefa "<título>": rota <rota>.` | `<rota>` ← grupo 1 da primeira linha que casa; `rota=` ou `estrategico=` no meio de uma linha não conta |
| `M-9b` | o mesmo evento, uma linha da resposta começa, depois de brancos, também por `estrategico=(.*)` | `Agente consultor devolveu a tarefa "<título>": rota <rota>; estratégico: <frase>.` | `<frase>` ← grupo 1 de `estrategico=`, até o fim da linha |
| `M-10` | tarefa fechada — `PreToolUse` · `Bash` · `command` casa `backlog\.py status (\S+) ([a-z-]+)` com `<estado>` igual a `done` | `Scrum master vai fechar a tarefa "<título>" como done: registrar estado, RDO e telemetria.` | Estado ← `tarefa_fechada` = `<ID>`, `titulo_fechada` = `<título>`. "e selecionar a próxima" saiu (`DTG-49`): depois do `done` o bloco B pode parar a janela sem `next` (`progresso.txt:83`, `86`); a seleção, quando há, sai na `M-11` ou na `M-12` |
| `M-10b` | o mesmo evento, `<estado>` igual a `blocked` ou `cancelled` | `Scrum master vai marcar a tarefa "<título>" como <estado>, sem RDO.` | `<estado>` ← grupo 2. Estado intocado, sem `tarefa_fechada`: a tarefa não foi concluída, e a `M-11` e a `M-12` diriam "concluiu". Sem RDO (`DP-F` item 3, fechamento c) e sem próxima: o `blocked` vai ao consultor, que pode parar a janela ou redespachar a mesma tarefa (`progresso.txt:74`, `77`; `DTG-49`) |
| `M-11` | tarefa escolhida com tarefa fechada na sessão — o evento de `M-1`, estado com `tarefa_fechada` | `Scrum master concluiu a tarefa "<título fechada>" e vai pegar a tarefa "<título>".` | `<título fechada>` ← `titulo_fechada` do estado; sai depois de `M-0` e antes de `M-1`, e limpa `tarefa_fechada` |
| `M-12` | fila vazia — `PostToolUse` · `Bash` · `backlog.py next` · resposta contém `nada delegável` · estado com `tarefa_fechada` | `Scrum master concluiu a tarefa "<título fechada>"; nada delegável na fila. Encerrando a janela com o relatório.` | `<título fechada>` ← estado; limpa `tarefa_fechada`. A regra B1..B3 saiu (`DTG-34`) |
| `M-12b` | o mesmo evento, estado sem `tarefa_fechada` | `Scrum master não encontrou tarefa delegável na fila. Encerrando a janela com o relatório.` | nenhuma lacuna |
| `M-13` | atribuição medida — `PreToolUse` · `Bash` · `command` contém `review_evidence.py`, `--tarefa <ID>` e `--atribuir` | `Tarefa "<título>": vou medir a que arquivo a pendência é atribuível.` | como `M-5` |
| `M-14` | agente despachado, modelador — `PreToolUse` · `Agent` · `pantonic-model-designer` · `prompt` casa `Ato:\s*` seguido, com ou sem crase, de `autoria`, `emenda` ou `conflito` | `Agente modelador recebe a tarefa "<título>" e vai fazer <ato> no modelo.` | `<ato>` ← a palavra casada |
| `M-14b` | o mesmo evento, sem casamento no `prompt` | `Agente modelador recebe a tarefa "<título>" e vai atualizar o modelo.` | `<título>` ← tarefa corrente |
| `M-15` | agente despachado, planejador — `PreToolUse` · `Agent` · `pantonic-planner` | `Agente planejador recebe a tarefa "<título>" e vai replanejar.` | `<título>` ← tarefa corrente |
| `M-16` | agente de volta, forma genérica — `PostToolUse` · `Agent`, ou o `UserPromptSubmit` da volta em hand-back, como em `M-4` · `pantonic-model-designer` ou `pantonic-planner`; ou `pantonic-executor`, `pantonic-reviewer`, `pantonic-consultant` cuja resposta não casa `M-4`, `M-4b`, `M-7`, `M-9` nem `M-9b` | `Agente <papel> devolveu a tarefa "<título>": <primeira linha>.` | `<papel>` ← `executor`, `revisor`, `consultor`, `modelador` ou `planejador` pelo `subagent_type`; `<primeira linha>` ← primeira linha não vazia da resposta, até 160 caracteres mais `…`; resposta vazia → `(sem texto)` |
| `M-17` | modelo do plano mostrado e turno acabado — `Stop` · estado com `aberta` e com `relatorio` | `Scrum master mostrou o modelo do plano e aguarda; a resposta dele está na extensão.` | nenhuma lacuna; estado ← sem `relatorio` (`aberta` fica). `relatorio` = true é gravado por `PreToolUse` · `Bash` · `command` contém `modelo.py show` sem `--drift` nem `--pendente`, com a janela aberta, sem gerar linha; sai no despacho de agente seguinte e no `backlog.py next`. `Stop` sem `relatorio` não gera linha. A frase diz só o que o gancho vê — o modelo mostrado e o turno acabado —, não se a janela encerrou nem o que se aguarda (`DTG-48`) |

Outros `subagent_type`, outras ferramentas (`Read`, `Grep`, `Edit`, …) e comandos `Bash` fora dos
três nomeados não geram linha nenhuma. Gancho disparado dentro de agente despachado (`agent_type`
no payload) sai sem ler nem gravar nada (`DTG-22`).

**Worked example (versão 3)** — o ciclo de `TLG-T2b` deste plano, aprovado sem escalada, como ele
aparece no painel (`DTG-27`): cada linha é gerada pelo gancho no evento nomeado, com o título da
tarefa e do plano no lugar da sigla (`DTG-33`), e nenhuma saída de ferramenta entre elas:

```
Abrindo a janela do plano "A tela do gerente: o fluxo da execução em linguagem humana".
Tarefa "O repertório como tabela de eventos: a skill diz o que a função gera". Passo: conferir os gates e preparar o despacho.
Tarefa "O repertório como tabela de eventos: a skill diz o que a função gera": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
Agente executor recebe a tarefa "O repertório como tabela de eventos: a skill diz o que a função gera" e vai executar: O redator do loop escreve o repertório fechado de mensagens: uma frase-modelo para cada transição do loop — tarefa e passo, agente despachado e o que vai fazer, veredito recebido, próxima tarefa —, no molde do exemplo do dono, com cada lacuna preenchida só pelo que o condutor já tem em mãos naquele passo.
Agente executor devolveu a tarefa "O repertório como tabela de eventos: a skill diz o que a função gera": review — sem pendência.
Tarefa "O repertório como tabela de eventos: a skill diz o que a função gera": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O repertório como tabela de eventos: a skill diz o que a função gera" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O repertório como tabela de eventos: a skill diz o que a função gera": aprovado 100%, bloqueante nenhuma.
Scrum master vai fechar a tarefa "O repertório como tabela de eventos: a skill diz o que a função gera" como done: registrar estado, RDO e telemetria.
Scrum master concluiu a tarefa "O repertório como tabela de eventos: a skill diz o que a função gera" e vai pegar a tarefa "A função que gera a linha do stream a cada evento do loop".
Tarefa "A função que gera a linha do stream a cada evento do loop". Passo: conferir os gates e preparar o despacho.
```

*(Histórico: o worked example `A` da versão 2 e a alternativa `B` do Marco 1 foram substituídos por
este; a forma `A` foi a escolhida no Marco 1 e é a base das frases acima.)*

---

## 5. Tarefas

Um card por operação da `### 1.2`, na ordem das operações; id `TLG-T<n>` para `OP-<n>`
(`I-8`). Todo card é lido por um executor frio que só tem o texto dele: restrições, contratos e
textos novos estão inline.

### TLG-T1 — A sonda de viabilidade diante do dono [Sonnet + dono · esforço medium · classe investigacao]
- **Status:** `done` · 2026-09-24
- **Objetivo:** O investigador encena, diante do dono, as quatro formas de uma saída chegar à tela — uma busca feita pelo próprio condutor, buscas e leituras feitas dentro de um agente despachado, a resposta de um gancho da ferramenta e a linha de status —; o dono anota o que cada uma mostra, e dessa tabela sai o veredito de viabilidade, sim ou não.
- **Fundamento:** `DTG-3` (sonda antes da recomendação), `DTG-9` (hook só entra se alterar a tela), `DTG-14` (execução no topo, hook gravado antes da sessão), `F-1`, `F-3`, `F-9` (nenhum `PostToolUse` vigente; settings do projeto limpo), `F-17` (`pantonic-scout` existe), hipóteses `H-1`..`H-4` que a sonda mede, `R-1`.
- **Operação do modelo:** `OP-1`
  - OP-1: O investigador encena, diante do dono, as quatro formas de uma saída chegar à tela — uma busca feita pelo próprio condutor, buscas e leituras feitas dentro de um agente despachado, a resposta de um gancho da ferramenta e a linha de status —; o dono anota o que cada uma mostra, e dessa tabela sai o veredito de viabilidade, sim ou não.
  - precisa de: tela do monitor — Quem implementa não mexe nela: só a observa, na sonda do começo e na validação do fim. É nela que se prova que o stream mudou.
- **Camada e fronteira:** kit (`.claude/`), sem código de produto. Toca `.claude/settings.json` **do projeto** (edição temporária, desfeita ao fim) e este plano (seção nova `### 2.2`). Não toca `C:\Users\panta\.claude\settings.json`, nenhum agente, nenhuma skill. **Esta tarefa não se delega:** é executada no topo da sessão pelo agente que a conduz, em modelo Sonnet, com o dono olhando a extensão VS Code; o despacho do passo (b) é a única chamada de subagente, e é ela mesma o objeto medido.
- **Domínio:** *tela do monitor* = painel da extensão VS Code do Claude Code (`DTG-1`); *forma de chegar à tela* = uma das quatro: (a) chamada de ferramenta do topo, (b) chamada de ferramenta dentro de subagente, (c) stdout de hook `PostToolUse`, (d) `statusLine`.
- **Arquivos-alvo:**
  - `.claude/settings.json:22` — âncora `"hooks": {` (bloco temporário inserido logo abaixo e removido no passo 7)
  - `docs/plans/P-0748-tela-do-gerente.md §2.1` — a seção nova `### 2.2 Agregado da sonda de viabilidade (TLG-T1)` entra **depois** do último bullet da `### 2.1` e **antes** do `---` que precede `## 3. Decisões`
- **Contratos/classes:** nenhum código. Forma do agregado (tabela de quatro linhas + uma linha de veredito), literal:

  ```
  ### 2.2 Agregado da sonda de viabilidade (TLG-T1)

  Medido pelo dono na extensão VS Code em <AAAA-MM-DD>, sessão reaberta com o hook (c) gravado.

  | forma | mecanismo | observado pelo dono | o que apareceu na tela |
  |---|---|---|---|
  | (a) | `Grep` feito pelo condutor no topo | sim / não | <uma frase> |
  | (b) | 3 `Grep` + 1 `Read` dentro de um subagente despachado | sim / não | <uma frase: "só a linha do despacho" ou "as quatro chamadas no topo"> |
  | (c) | stdout de um hook `PostToolUse` (`SONDA-HOOK-C`) | sim / não / não medida | <uma frase> |
  | (d) | `statusLine` configurada no settings global | sim / não | <uma frase> |

  **Veredito de viabilidade (Marco 2):** sim / não — regra: `sim` se e só se a linha (b) registra "só a linha do despacho".
  ```

  Na coluna `observado pelo dono`, `sim` significa "a saída dessa forma **aparece** no fluxo principal da extensão"; `não`, "não aparece".
- **Método de sondagem:** corpus = esta própria sessão; métrica = sim/não por forma, anotado pelo dono; agregado = a tabela acima, ≤ 12 linhas, sem dado bruto.
  1. **Preparar o hook (c), antes da sessão de observação.** Em `.claude/settings.json`, logo abaixo da linha `"hooks": {` (linha 22), inserir o bloco literal (vírgula final incluída, porque `"PreToolUse"` vem em seguida):

     ```
         "PostToolUse": [
           {
             "matcher": "Grep",
             "hooks": [
               {
                 "type": "command",
                 "command": "python -c \"print('SONDA-HOOK-C')\""
               }
             ]
           }
         ],
     ```

     Conferir `python -c "import json; json.load(open('.claude/settings.json', encoding='utf-8')); print('json ok')"` → `json ok`. Dizer ao dono, em uma linha: `Hook de sonda gravado; feche e reabra esta sessão da extensão para ele carregar, e me diga "pronto".` Encerrar o turno.
  2. **Forma (a)** — com a sessão reaberta: uma chamada `Grep` no topo, padrão `TLG-T1`, caminho `docs/plans/P-0748-tela-do-gerente.md`, `output_mode` `content`. Escrever ao dono: `Forma (a) feita: o Grep do topo. Anote o que apareceu.`
  3. **Forma (c)** — o mesmo `Grep` do passo 2 disparou o hook (matcher `Grep`). Escrever ao dono: `Forma (c): o texto SONDA-HOOK-C apareceu em algum lugar da tela? Anote sim ou não.`
  4. **Forma (b)** — uma chamada `Agent`, `subagent_type` `pantonic-scout`, prompt literal: `Sonda P-0748 forma (b). Rode, nesta ordem, três Grep — padrões OP-1, OP-2 e OP-3, cada um no arquivo docs/plans/P-0748-tela-do-gerente.md, output_mode content — e um Read de docs/plans/_CAMPANHA-P-0748.md com limit 5. Devolva uma única linha: "sonda-b: 3 grep + 1 read feitos".` Escrever ao dono: `Forma (b) feita: o subagente rodou quatro chamadas. Na tela apareceu só a linha do despacho, ou as quatro chamadas no topo? Anote.`
  5. **Forma (d)** — escrever ao dono: `Forma (d): a linha de status (statusLine do settings global) aparece na extensão? Anote sim ou não.`
  6. **Registrar o agregado:** o dono dita as quatro anotações; gravar a `### 2.2` no plano na forma literal de `Contratos/classes`, com a data e o veredito pela regra da última linha.
  7. **Remover o hook:** apagar do `.claude/settings.json` exatamente o bloco inserido no passo 1 (as doze linhas, de `"PostToolUse": [` à `],`), restaurando `"hooks": {` seguido diretamente de `"PreToolUse": [`. Conferir com a Verificação 3 e 4.
- **Restrições desta tarefa:** `I-1` — nenhum arquivo fora deste repositório é editado; o settings **global** fica intocado. `I-4` — a `### 2.2` registra só o que o dono viu, nunca hipótese. `I-6` — o veredito é aceite de **marco** (Marco 2), não desta tarefa: a tarefa fecha com a tabela gravada, seja o veredito `sim` ou `não`. Nenhum agente, skill ou instrumento é editado.
- **Não fazer:** não despachar `pantonic-executor` para esta tarefa; não editar `C:\Users\panta\.claude\settings.json`; não deixar o bloco `PostToolUse` no settings ao fim; não interpretar (c) ou (d) como veredito — só (b) decide; não repetir a sonda para "confirmar"; não iniciar `TLG-T2` neste contexto.
- **Contingências:**
  - se a chamada `Agent` não oferece `subagent_type` `pantonic-scout` → seguir com `general-purpose` e o mesmo prompt, anotando `(subagente general-purpose)` na coluna `mecanismo` da linha (b);
  - se o dono não reabre a sessão (passo 1) → seguir com os passos 2, 4, 5 e 6 assim mesmo, registrar (c) como `não medida` e a frase `sessão não reaberta`; o veredito segue só de (b);
  - se `python -c "import json; …"` do passo 1 falha → parar e sinalizar `blocked` razão `ferramenta`, devolvendo a linha de erro; restaurar o arquivo apagando à mão o bloco do passo 1 (o arquivo é ignorado pelo git, `.gitignore:5`: não há `git checkout` que o restaure, `DTG-16`) e conferir de novo o `json ok` antes de parar;
  - se (b) registra "as quatro chamadas no topo" → veredito `não`; gravar a tabela e fechar a tarefa normalmente — a rodada de decisões sobre `R-1` é ato da orquestração no Marco 2, não deste card.
- **Testes:** nenhum teste novo (tarefa de investigação); nenhuma suíte é tocada.
- **Verificação:**
  1. `(Select-String -Path docs/plans/P-0748-tela-do-gerente.md -Pattern "^### 2\.2 Agregado da sonda de viabilidade" | Measure-Object).Count` (âncora de início de linha: o próprio card cita o título indentado e dentro de crases, e essas linhas não contam, `DTG-16`) → antes `0`, depois `1` (medido 2026-09-24).
  2. `(Select-String -Path docs/plans/P-0748-tela-do-gerente.md -Pattern "^\*\*Veredito de viabilidade \(Marco 2\):\*\* (sim|não) " | Measure-Object).Count` (mesma âncora; exige `sim` ou `não` preenchido) → antes `0`, depois `1` (medido 2026-09-24).
  3. `(Select-String -SimpleMatch -Path .claude/settings.json -Pattern "SONDA-HOOK-C" | Measure-Object).Count` → antes `0` (medido 2026-09-23), **durante a sonda** `1`, depois do passo 7 `0`.
  4. `(Select-String -SimpleMatch -Path .claude/settings.json -Pattern '"PostToolUse"' | Measure-Object).Count` → antes `0`, depois do passo 7 `0` (medido 2026-09-24); e `python -c "import json; json.load(open('.claude/settings.json', encoding='utf-8')); print('json ok')"` → `json ok`. Conferência por conteúdo, não por `git diff`: o arquivo é ignorado pelo git (`.gitignore:5`), e `git diff --quiet` sobre ele sai `0` sempre (`DTG-16`).
- **Pronto quando (o fato que tem de existir ao final):** a tabela `### 2.2` com quatro linhas preenchidas com `sim`/`não` (ou `não medida` só na linha (c)) e a linha de veredito — é o **fato** que `stream de dados.viabilidade medida` exige: *medida diante do dono, uma linha por mecanismo com o que ele viu, e o veredito sim ou não tirado dessa tabela; sendo não, a única alternativa já pensada sobe ao dono como decisão* — Verificação 1 e 2.
- **Fora do escopo desta tarefa:** a resposta a `R-1` — é do dono, no Marco 2, e entra em `DTG-12`; qualquer edição no loop (`TLG-T3`, `TLG-T4`).

### TLG-T2 — O repertório de mensagens na skill do loop [Sonnet · esforço medium · classe redacao]
- **Status:** `done` · 2026-09-24
- **Objetivo:** O redator do loop escreve o repertório fechado de mensagens: uma frase-modelo para cada transição do loop — tarefa e passo, agente despachado e o que vai fazer, veredito recebido, próxima tarefa —, no molde do exemplo do dono, com cada lacuna preenchida só pelo que o condutor já tem em mãos naquele passo.
- **Fundamento:** `DTG-5`, `DTG-7` (intenção, não raciocínio), `DTG-10` (residência: `### 4.1` → seção da skill), `F-2`, `F-11` (linhas de retorno que preenchem as lacunas), `F-12` (saída do `backlog.py next`), `I-2`, `I-3`, `R-3`.
- **Depende de:** `TLG-T1`
- **Operação do modelo:** `OP-2`
  - OP-2: O redator do loop escreve o repertório fechado de mensagens: uma frase-modelo para cada transição do loop — tarefa e passo, agente despachado e o que vai fazer, veredito recebido, próxima tarefa —, no molde do exemplo do dono, com cada lacuna preenchida só pelo que o condutor já tem em mãos naquele passo.
  - precisa de: stream de dados — Quem implementa recebe o comportamento do condutor do loop: o que ele escreve ao dono e o que ele mesmo executa entre um despacho e outro. Só isso muda; a ferramenta que roda os agentes e a extensão que desenha a tela ficam como estão.; tarefa — Quem implementa lê dela o que preenche as mensagens: qual tarefa, qual passo e o que o passo pede. Nada nela muda.; mente do agente — Quem implementa usa a intenção que o condutor já tem em mãos: o que ele pediu ao agente e o que o agente devolveu. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo.
- **Camada e fronteira:** kit, skill `scrum-master`. Só inserção de uma seção nova; nenhuma linha existente da skill muda. Nenhum agente é editado.
- **Domínio:** *transição do loop* = mudança de passo da `scrum-master` (seleção, despacho, retorno, veredito, roteamento, fechamento, próxima); *lacuna* = `<…>` na frase-modelo, preenchida por dado que o condutor já recebeu (`I-3`).
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md:306` — âncora `## Proibições` (a seção nova entra imediatamente **antes** desta linha, separada por uma linha em branco)
- **Contratos/classes:** nenhum código.
- **Texto novo, literal** (inserir antes de `## Proibições`; a tabela é cópia da `### 4.1` deste plano, que é a residência única — as quinze linhas, sem alteração de uma palavra):

  ```
  ## Repertório de mensagens ao gerente

  O condutor narra a execução ao gerente do projeto com estas frases, e só com elas — uma por
  transição do loop, escrita como **texto do agente** antes do ato que ela anuncia, nunca como
  saída de comando (`P-0748`, `DTG-5`, `I-2`). Toda lacuna `<…>` se preenche com o que o condutor
  já tem em mãos naquele passo; nenhuma pede busca, leitura ou comando novo (`I-3`). Onde cada
  linha entra no fluxo é dito pelo bullet `**Narra:**` de cada passo.

  | id | momento (passo) | frase-modelo | lacunas ← o que o condutor já tem |
  |---|---|---|---|
  <as quinze linhas `M-0`..`M-14` da tabela da ### 4.1 do P-0748, copiadas verbatim>
  ```

  Onde está `<as quinze linhas …>`, colar as linhas `| \`M-0\` |` a `| \`M-14\` |` da `### 4.1` de `docs/plans/P-0748-tela-do-gerente.md` exatamente como estão lá (inclusive as crases nos ids e as referências `F-11`/`F-12`, que passam a apontar para o plano de origem).
- **Passos:**
  1. Abrir `.claude/skills/scrum-master/SKILL.md` e localizar a linha `## Proibições`.
  2. Inserir, antes dela, o texto de `Texto novo, literal`, com a tabela colada da `### 4.1` do plano.
  3. Rodar a Verificação 1–4.
- **Restrições desta tarefa:** `I-2` — nenhuma frase do repertório é saída de comando; `I-3` — nenhuma lacuna exige chamada nova; `DTG-10` — a tabela é cópia, não reescrita: divergência de uma palavra entre a `### 4.1` e a seção da skill é defeito. Inserção pura: `git diff --numstat` da skill tem `0` na coluna de linhas removidas.
- **Não fazer:** não editar nenhum passo da skill (é `TLG-T3` e `TLG-T4`); não acrescentar, remover ou reordenar linhas do repertório; não editar `passagem-de-bastao` (é `TLG-T4`); não editar agentes; não "melhorar" as frases.
- **Contingências:**
  - se a `### 4.1` do plano tiver mais ou menos de quinze linhas `M-<n>` → parar e sinalizar `blocked` razão `premissa` com a contagem encontrada;
  - se `## Proibições` não existir na skill → parar e sinalizar `blocked` razão `premissa` com as três primeiras linhas de `grep -n "^## " .claude/skills/scrum-master/SKILL.md`.
- **Testes:** nenhum TF (texto de skill); TR: `python -m pytest tests/ -q` não reduz o total re-medido no despacho (referência histórica `277 passed`, 2026-09-23, `F-14`).
- **Verificação:**
  1. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "## Repertório de mensagens ao gerente" | Measure-Object).Count` → antes `0` (medido 2026-09-23), depois `1`.
  2. `(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern "^\| ``M-\d+`` \|" | Measure-Object).Count` (regex deliberado: linha de tabela cujo id é `M-<n>` entre crases; em PowerShell a crase dobrada dentro de aspas duplas é uma crase literal) → antes `0` na skill (medido 2026-09-23), depois `15` — o mesmo padrão rodado sobre `docs/plans/P-0748-tela-do-gerente.md` devolve `15` (medido 2026-09-23), que é o valor de referência.
  3. `git diff --numstat -- .claude/skills/scrum-master/SKILL.md` → segunda coluna (linhas removidas) `0`; primeira coluna ≥ `24`.
  4. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` ≥ o total re-medido no despacho.
- **Pronto quando:** `stream de dados.repertório de mensagens` — *fechado: uma frase-modelo por transição do loop, no molde do exemplo do dono — "Tarefa X, passo Y.", "Agente executor recebe o passo Y e vai executar Z.", "Agente consultor aceitou a entrega." —; nenhuma lacuna pede ao condutor uma busca nova para ser preenchida* — Verificação 1, 2 e 3.
- **Fora do escopo desta tarefa:** ligar as frases aos passos (`TLG-T4`); qualquer comando do kit (`TLG-T3`).

### TLG-T3 — O gancho que grava o arquivo de progresso [Sonnet · esforço high · classe implementacao]
- **Status:** `done` · 2026-09-24
- **Objetivo:** O mantenedor do kit liga um gancho que roda depois de cada ato de ferramenta e grava num arquivo de progresso só as linhas do repertório, uma por transição e na ordem em que o condutor as escreve; toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — fica de fora do arquivo.
- **Fundamento:** `DTG-20` (destino do card), `DTG-21` (rota do transcript e medida de abertura), `DTG-22` (exclusão dupla), `DTG-23` (marcador e inícios), `DTG-24` (residência), `DTG-25` (declaração em `projecoes.json`, eventos `PostToolUse` e `Stop`), `DTG-26` (não há `loop.py`), `F-19`, `F-20`, `F-21`, `F-22`, `I-1`, `I-7`, `I-11`, `R-6`, `R-7`.
- **Depende de:** `TLG-T2`
- **Operação do modelo:** `OP-3`
  - OP-3: O mantenedor do kit liga um gancho que roda depois de cada ato de ferramenta e grava num arquivo de progresso só as linhas do repertório, uma por transição e na ordem em que o condutor as escreve; toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — fica de fora do arquivo.
  - precisa de: stream de dados — Quem implementa recebe o comportamento do condutor do loop, isto é, o que ele escreve ao dono a cada passo, e o arquivo de progresso que um gancho do próprio kit alimenta com essas linhas. A ferramenta que roda os agentes e a extensão que desenha a tela ficam como estão.
- **Camada e fronteira:** kit — script novo em `.claude/tools/`, teste novo em `tests/`, dois eventos novos no alvo `projeto` de `.claude/projecoes.json` e a materialização local em `.claude/settings.json`, feita **só** por `python .claude/tools/materializar.py apply --alvo projeto` (o `settings.json` é ignorado pelo git, `.gitignore:5`, e nunca se edita à mão). O script usa só a biblioteca padrão (`json`, `os`, `sys`, `time`, `pathlib`) e não importa nenhum instrumento do kit. Nenhuma skill, agente, `README.md`, `.gitignore`, `materializar.py` ou `ocupacao.py` muda; o settings global `C:\Users\panta\.claude\settings.json` fica intocado (`I-1`).
- **Domínio:** *arquivo de progresso* = `.claude/estado/progresso.txt`: uma linha do repertório por transição, UTF-8, terminada em `\n`, na ordem em que o condutor as escreveu, **sem** o marcador. *Linha do repertório* = linha do texto do condutor que, sem espaços nas pontas, começa pelo marcador literal `[gerente] ` (colchete, `gerente`, colchete, um espaço) e cujo resto começa por um destes sete inícios: `Abrindo a janela do plano `, `Tarefa `, `Agente executor `, `Agente revisor `, `Agente consultor `, `Agente modelador `, `Scrum master ` (`DTG-23`). *Transcript da sessão principal* = o `.jsonl` cujo caminho chega no campo `transcript_path` do JSON de entrada do gancho — medido: chega também quando o gancho dispara dentro de agente despachado, e nesse caso o JSON traz `agent_type` e `agent_id` (`F-20`); o texto do condutor fica nele como entradas `"type": "assistant"` com blocos `"type": "text"` em `message.content`, uma linha JSON por bloco, e as entradas dos agentes despachados moram em outros arquivos, com `"isSidechain": true` (`F-19`). *Cursor* = `.claude/estado/progresso-cursor.json`, objeto `{<transcript_path>: <offset em bytes já lido>}`. Os dois arquivos são ignorados pelo git pela regra vigente `.claude/estado/*` (`git check-ignore -q` sai `0`, `F-22`) — fato de sessão, nunca versionado.
- **Arquivos-alvo:**
  - `.claude/estado/sonda_transcript.py` — novo, temporário: criado no passo 1 e apagado no passo 2
  - `.claude/tools/progresso_hook.py` — novo
  - `tests/test_progresso_hook.py` — novo
  - `.claude/projecoes.json:19` — âncora: a linha que abre o evento SubagentStop do alvo projeto (única no arquivo); os dois eventos novos entram imediatamente antes dela
  - `.claude/settings.json` — materializado pelo passo 6, nunca editado à mão
- **Contratos/classes:** estrutura de `.claude/tools/progresso_hook.py` (assinaturas, não só nomes):

  ```python
  KIT = Path(__file__).resolve().parents[1]          # a pasta .claude/
  MARCADOR = "[gerente] "
  INICIOS = ("Abrindo a janela do plano ", "Tarefa ", "Agente executor ", "Agente revisor ",
             "Agente consultor ", "Agente modelador ", "Scrum master ")

  def linhas_do_repertorio(entrada: dict) -> list[str]: ...
  def ler_novas(transcript: Path, offset: int) -> tuple[list[str], int]: ...
  def main(argv: list[str] | None = None, entrada: str | None = None,
           estado: Path | None = None, espera: float = 2.0) -> int: ...

  if __name__ == "__main__":
      sys.exit(main())
  ```

  Semântica fechada:
  - `linhas_do_repertorio(entrada)`: devolve `[]` salvo quando `entrada.get("type") == "assistant"` **e** `entrada.get("isSidechain")` é falso. Com `content = entrada.get("message", {}).get("content")` que não é lista, `[]`. Para cada bloco `dict` com `bloco.get("type") == "text"`, para cada linha de `str(bloco.get("text", "")).splitlines()`: `l = linha.strip()`; se `l.startswith(MARCADOR)` e `l[len(MARCADOR):].startswith(INICIOS)`, acrescenta `l[len(MARCADOR):]`. Ordem preservada.
  - `ler_novas(transcript, offset)`: abre em binário; `tamanho = f.seek(0, 2)`; se `offset < 0` ou `offset > tamanho`, `offset = 0`; `f.seek(offset)`; `dados = f.read()`; `fim = dados.rfind(b"\n")`; com `fim == -1`, devolve `([], offset)`. Senão, para cada linha de `dados[:fim + 1].split(b"\n")` que não seja vazia: `json.loads(linha.decode("utf-8"))`, pulando a linha em `ValueError` ou `UnicodeDecodeError` e toda linha cujo resultado não é `dict`; acumula `linhas_do_repertorio`. Devolve `(linhas, offset + fim + 1)` — a linha final sem `\n` fica para a próxima chamada.
  - `main(...)`: tudo dentro de `try`/`except Exception: return 0` (falha aberta); **nunca imprime** e sai sempre `0` (`I-11`). (1) `raw = entrada` ou, se `None`, `sys.stdin.buffer.read().decode("utf-8", errors="replace")`; `payload = json.loads(raw)`; payload que não é `dict` → `0`. (2) `payload.get("agent_type")` não vazio → `0`, sem criar nada (`DTG-22`). (3) `tp = payload.get("transcript_path")` vazio → `0`, sem criar nada. (4) `estado = estado or KIT / "estado"`; `estado.mkdir(parents=True, exist_ok=True)`. (5) Trava `estado / "progresso.lock"`: repetir até `time.monotonic()` passar de início + `espera`: `os.open(trava, os.O_CREAT | os.O_EXCL | os.O_WRONLY)` e fechar o descritor → trava obtida; em `FileExistsError`, se `time.time() - trava.stat().st_mtime > 30`, `trava.unlink(missing_ok=True)` e tentar de novo; senão `time.sleep(0.05)`; `OSError` no `stat` → tentar de novo. Prazo vencido sem trava → `0`, sem ler nem gravar. Obtida a trava, os passos 6 a 8 rodam num `try` cujo `finally` faz `trava.unlink(missing_ok=True)`. (6) `cursor` = `json.loads` de `estado / "progresso-cursor.json"` lido em UTF-8; arquivo ausente, JSON inválido ou valor que não é `dict` → `{}`; `offset = cursor.get(tp, 0)`, e `0` se não for `int`. (7) `linhas, novo = ler_novas(Path(tp), offset)`; com `linhas` não vazia, abrir `estado / "progresso.txt"` em modo `"a"`, `encoding="utf-8"`, `newline="\n"`, e escrever cada linha seguida de `"\n"`. (8) `cursor[tp] = novo`; gravar o cursor com `json.dumps(cursor, ensure_ascii=False)` em UTF-8.
- **Texto novo, literal** — o script da sonda do passo 1, gravado em `.claude/estado/sonda_transcript.py` exatamente assim:

  ```python
  import json, pathlib, collections
  d = pathlib.Path.home() / ".claude" / "projects" / "d--workspaces-PantonicApp"
  t = max(d.glob("*.jsonl"), key=lambda p: p.stat().st_mtime)
  def contar(arq):
      n = collections.Counter()
      for linha in arq.open(encoding="utf-8"):
          try:
              e = json.loads(linha)
          except ValueError:
              continue
          if e.get("type") != "assistant":
              continue
          n["assistant"] += 1
          n["isSidechain_true"] += bool(e.get("isSidechain"))
          tipos = {b.get("type") for b in e.get("message", {}).get("content", []) if isinstance(b, dict)}
          n["com_text"] += "text" in tipos
          n["text_e_tool_use_juntos"] += {"text", "tool_use"} <= tipos
      return n
  p = contar(t)
  subs = list((d / t.stem).rglob("*.jsonl")) if (d / t.stem).exists() else []
  s = collections.Counter()
  for a in subs:
      s.update(contar(a))
  print("principal:", t.name, "assistant", p["assistant"], "com_text", p["com_text"], "isSidechain_true", p["isSidechain_true"], "text_e_tool_use_juntos", p["text_e_tool_use_juntos"])
  print("subagentes: arquivos", len(subs), "assistant", s["assistant"], "isSidechain_true", s["isSidechain_true"])
  ```

  Saída de referência, medida pelo planejador em 2026-09-24 (`F-19`): `principal: 2ce71b39-8c4f-476a-b609-3f58062db73d.jsonl assistant 57 com_text 10 isSidechain_true 0 text_e_tool_use_juntos 0` e `subagentes: arquivos 5 assistant 128 isSidechain_true 128`. Os números mudam com a sessão; o que decide são as contingências 1 a 3.

  O bloco a inserir em `.claude/projecoes.json`, imediatamente antes da linha `"SubagentStop": [` (dez espaços de recuo antes de cada chave de evento, como as vizinhas; vírgula final incluída):

  ```
            "PostToolUse": [
              {
                "matcher": ".*",
                "hooks": [
                  {
                    "type": "command",
                    "command": "python {KIT_ROOT}/tools/progresso_hook.py"
                  }
                ]
              }
            ],
            "Stop": [
              {
                "hooks": [
                  {
                    "type": "command",
                    "command": "python {KIT_ROOT}/tools/progresso_hook.py"
                  }
                ]
              }
            ],
  ```
- **Passos:**
  1. **Medida técnica de abertura (tensão (2), depois (1); `DTG-21`).** Criar `.claude/estado/sonda_transcript.py` com o script literal de `Texto novo, literal`; rodar `python .claude/estado/sonda_transcript.py`; guardar as duas linhas impressas para a linha de retorno da entrega. Aplicar as contingências 1 a 3 **antes** de qualquer outro passo.
  2. Apagar `.claude/estado/sonda_transcript.py`.
  3. Criar `.claude/tools/progresso_hook.py` com a estrutura e a semântica de `Contratos/classes`, e uma docstring de módulo de no máximo seis linhas dizendo: gancho `PostToolUse` e `Stop` do `P-0748` (`OP-3`); copia do transcript da sessão principal para `.claude/estado/progresso.txt` só as linhas do repertório marcadas com `[gerente] `; falha aberta, nunca imprime.
  4. Criar `tests/test_progresso_hook.py`: carregar o módulo por `importlib.util.spec_from_file_location("progresso_hook", _ROOT / ".claude" / "tools" / "progresso_hook.py")` com `_ROOT = Path(__file__).resolve().parents[1]` (o padrão de `tests/test_modelo.py:35,53-54`); montar cada transcript em `tmp_path` como `.jsonl` com uma entrada JSON por linha, terminada em `\n`; chamar `main(entrada=json.dumps(payload), estado=tmp_path / "estado")`; escrever os nove TFs de `Testes`.
  5. Inserir em `.claude/projecoes.json` o bloco literal de `Texto novo, literal`, imediatamente antes da linha `"SubagentStop": [`.
  6. Rodar, nesta ordem: `python .claude/tools/materializar.py check --alvo projeto`; `python .claude/tools/materializar.py drift --alvo projeto`; `python .claude/tools/materializar.py apply --alvo projeto`; `python .claude/tools/materializar.py drift --alvo projeto`.
  7. Rodar a Verificação 1 a 7.
- **Restrições desta tarefa:** `I-11` — o arquivo de progresso só recebe linhas por este gancho, que nunca imprime e sai sempre `0`. `DTG-22` — as **duas** barreiras existem: `agent_type` no JSON de entrada **e** `isSidechain` na entrada do transcript; uma não substitui a outra. `DTG-24` — os caminhos são exatamente os do `Domínio`; o `.gitignore` não muda. `DTG-25` — o `settings.json` muda só pelo `apply`. `I-7` — o total de `pytest tests/` não cai. Estrutural, sem teste: o script não importa `rdo`, `backlog`, `telemetria`, `modelo`, `ocupacao` nem `materializar` (Verificação 7).
- **Não fazer:** não editar `.claude/settings.json` à mão; não editar `.gitignore`, `materializar.py`, `ocupacao.py`, nenhuma skill (a regra de narração com o marcador é da `TLG-T4`), nenhum agente, o `README.md`; não tocar o alvo `usuario` do `projecoes.json`; não criar `loop.py` (`DTG-26`); não fazer o gancho imprimir, devolver JSON no stdout ou sair diferente de `0`; não gravar timestamp, marcador ou qualquer texto além da frase no arquivo de progresso; não pedir ao dono para reabrir a sessão (é ato da orquestração antes da `TLG-T5`); não deixar `.claude/estado/sonda_transcript.py` no disco.
- **Contingências:**
  1. se a linha `principal:` da sonda traz `com_text 0` → caminho nenhum leva a linha do condutor ao gancho (tensão (2) sem saída): apagar a sonda, parar e sinalizar `blocked` razão `premissa`, devolvendo as duas linhas da sonda — a triagem sobe o caso ao dono como estratégico (`DTG-21`);
  2. se a sonda termina com erro (por exemplo `ValueError` de `max()` sem nenhum `.jsonl` na pasta) → apagar a sonda, parar e sinalizar `blocked` razão `premissa`, devolvendo a última linha do erro;
  3. se a linha `principal:` traz `isSidechain_true` maior que `0`, ou a linha `subagentes:` traz `isSidechain_true` menor que `assistant` → seguir com este card como está (a barreira de `agent_type` e a de `isSidechain` continuam, `DTG-22`) e devolver `contingência 3 acionada: <as duas linhas da sonda>`;
  4. se `"SubagentStop": [` não aparece exatamente uma vez em `.claude/projecoes.json` → parar e sinalizar `blocked` razão `premissa`, devolvendo a saída de `grep -n "SubagentStop" .claude/projecoes.json`;
  5. se `materializar.py check --alvo projeto` sai diferente de `0`, ou o segundo `drift` sai diferente de `0` → parar e sinalizar `blocked` razão `ferramenta`, devolvendo a saída do comando;
  6. se o modo de permissão recusa o `materializar.py apply` → parar e sinalizar `blocked` razão `ferramenta` com a linha `apply recusado pelo modo de permissão; o dono roda: python .claude/tools/materializar.py apply --alvo projeto`; o agente não contorna a recusa nem edita o `settings.json` à mão;
  7. se `python -m pytest tests/ -q` reduz o total por teste **fora** de `tests/test_progresso_hook.py` → parar e sinalizar `blocked` razão `dependencia` com o nome do teste.
- **Testes:** `tests/test_progresso_hook.py`, todos com `estado = tmp_path / "estado"` e transcript em `tmp_path`. Para cada TF, o valor que a regra concorrente daria sobre a mesma fixture vem entre parênteses.
  - `TF-PROG-1` — marcador: uma entrada `assistant` com um bloco `text` de duas linhas, `[gerente] Tarefa TLG-T3 — O gancho. Passo: conferir os gates e preparar o despacho.` e `Tarefa solta sem marcador.`; o arquivo `progresso.txt` fica exatamente `Tarefa TLG-T3 — O gancho. Passo: conferir os gates e preparar o despacho.\n` (sem exigir o marcador: duas linhas).
  - `TF-PROG-2` — `isSidechain`: a mesma linha marcada numa entrada com `"isSidechain": true`; `progresso.txt` não existe (sem o filtro: uma linha).
  - `TF-PROG-3` — `agent_type`: payload com `"agent_type": "pantonic-executor"` sobre um transcript com uma linha marcada válida; nem `progresso.txt` nem `progresso-cursor.json` existem, e a pasta `estado` não foi criada (sem a barreira: uma linha).
  - `TF-PROG-4` — cursor: primeira chamada com uma entrada (linha `A`, `[gerente] Tarefa A. Passo: x.`); acrescentar ao transcript uma segunda entrada (linha `B`, `[gerente] Scrum master concluiu a tarefa A e vai pegar a tarefa B — y.`); segunda chamada; `progresso.txt` tem exatamente duas linhas, `A` e depois `B` (sem cursor: três linhas, `A`, `A`, `B`).
  - `TF-PROG-5` — só texto do condutor: uma entrada `"type": "user"` com bloco `tool_result` cujo conteúdo é `[gerente] Tarefa X. Passo: y.` e uma entrada `assistant` só com bloco `tool_use`; `progresso.txt` não existe (lendo todo texto do transcript: uma linha).
  - `TF-PROG-6` — inícios: bloco `text` com `[gerente] qualquer coisa fora do repertório` e `[gerente] Agente revisor devolveu a tarefa TLG-T3: aprovado 100%, bloqueante nenhuma.`; `progresso.txt` tem só a segunda frase, sem o marcador (só com o marcador: duas linhas).
  - `TF-PROG-7` — linha incompleta: transcript cuja última entrada, marcada, não termina em `\n`; depois da primeira chamada `progresso.txt` não existe e o cursor guarda o tamanho em bytes do trecho até o último `\n`; acrescentar `\n` e chamar de novo; `progresso.txt` tem a linha (consumindo a linha incompleta na primeira chamada: a linha se perde, zero linhas no fim).
  - `TF-PROG-8` — falha aberta, três casos, cada um com `main(...) == 0`, stdout vazio (`capsys`) e `progresso.txt` inexistente: entrada `"isto não é json"`; payload sem `transcript_path`; `transcript_path` apontando para arquivo que não existe (sem o `try`/`except`: exceção no terceiro caso).
  - `TF-PROG-9` — trava: com `estado / "progresso.lock"` recém-criado e `espera=0.2`, a chamada devolve `0`, `progresso.txt` e `progresso-cursor.json` não existem; com a mesma trava e `os.utime` pondo o `mtime` dela 60 segundos no passado, a chamada grava a linha e a trava não existe mais ao fim (sem trava: grava já no primeiro caso).

  Suítes: `python -m pytest tests/test_progresso_hook.py -q`; `python -m pytest tests/ -q`.
- **Verificação:**
  1. `python -m pytest tests/test_progresso_hook.py -q` → antes: arquivo inexistente (erro de coleta); depois `9 passed`.
  2. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` = total re-medido no despacho + `9` (referência histórica `277 passed`, 2026-09-23, `F-14`).
  3. `python .claude/tools/materializar.py check --alvo projeto` → `materializar: OK - manifesto valido.` e exit `0` (guarda; medido 2026-09-24 antes do card).
  4. `python .claude/tools/materializar.py drift --alvo projeto` → entre o passo 5 e o `apply`, exit `1` com uma linha contendo `evento 'PostToolUse'` e uma contendo `evento 'Stop'` (medido numa cópia do kit, 2026-09-24, `F-21`); depois do `apply`, `materializar: OK - sem drift.` e exit `0`.
  5. `(Select-String -SimpleMatch -Path .claude/projecoes.json -Pattern "progresso_hook.py" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `2`.
  6. `(Select-String -SimpleMatch -Path .claude/settings.json -Pattern "progresso_hook.py" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `2`; e `python -c "import json; json.load(open('.claude/settings.json', encoding='utf-8')); print('json ok')"` → `json ok`.
  7. Inspeção estrutural e limpeza, bloco cercado por conter barra invertida:

     ```
     (Select-String -Path .claude/tools/progresso_hook.py -Pattern "^(from|import) (rdo|backlog|telemetria|modelo|ocupacao|materializar)\b" | Measure-Object).Count
     (Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "print(" | Measure-Object).Count
     Test-Path .claude/estado/sonda_transcript.py
     ```

     → `0`, `0` e `False` (o primeiro padrão, rodado sobre `.claude/tools/ocupacao.py` em 2026-09-24, devolve `0`; o terceiro devolve `False` antes do card e `True` só entre os passos 1 e 2).
- **Pronto quando:** `stream de dados.arquivo de progresso` — *existe e é alimentado por um gancho do kit que roda depois de cada ato de ferramenta: guarda as linhas do repertório, uma por transição, na ordem em que o condutor as escreveu, e nada mais — nenhuma busca, leitura ou saída de comando, e nenhuma chamada feita dentro dos agentes despachados* — Verificação 1, 4, 5 e 6.
- **Fora do escopo desta tarefa:** a regra de narração com o marcador na `scrum-master` (`TLG-T4`); as colunas *momento* e *lacunas* do repertório (`TLG-T2a`); o painel e a descrição pública (`TLG-T5`); a leitura do painel com a sessão reaberta (Marco 3, aceite de marco, `I-6`); propagação aos kits derivados (`DTG-8`); a letra da `OP-3` diante do evento `Stop` (`DTG-25`, pergunta ao modelador, não ao executor).
- **Notas de execução:**
  - 2026-09-24 `blocked` — R-1 espera DTG-12 do dono no Marco 2 (DTG-17)
  - 2026-09-24 segue `blocked` (`DTG-18`) — `DTG-12` preenchida com a tela fora da extensão; a contingência 2 **não** se aplica: o card aguarda a emenda da `## 1` e a rodada do planejador, que o mantém, reescreve ou retira
  - 2026-09-24 reescrito pela rodada do planejador (`DTG-20`) para a `OP-3` da versão 2: o card do `loop.py` sai inteiro (`DTG-26`) e entra o gancho do arquivo de progresso

### TLG-T2a — O repertório deixa de citar o comando que não vai existir [Sonnet · esforço low · classe redacao]
- **Status:** `done` · 2026-09-24
- **Objetivo:** O redator do loop escreve o repertório fechado de mensagens: uma frase-modelo para cada transição do loop — tarefa e passo, agente despachado e o que vai fazer, veredito recebido, próxima tarefa —, no molde do exemplo do dono, com cada lacuna preenchida só pelo que o condutor já tem em mãos naquele passo.
- **Fundamento:** `DTG-20` (card corretivo da `OP-2`), `DTG-26` (não há `loop.py`: a próxima tarefa e o dossiê vêm do `backlog.py next`), `DTG-10` (a tabela da skill é cópia da `### 4.1`, que esta rodada corrigiu), `DTG-28` (aceite por conteúdo, não por `numstat`), `F-12`, `F-23`, `I-3`.
- **Depende de:** `TLG-T3`
- **Operação do modelo:** `OP-2`
  - OP-2: O redator do loop escreve o repertório fechado de mensagens: uma frase-modelo para cada transição do loop — tarefa e passo, agente despachado e o que vai fazer, veredito recebido, próxima tarefa —, no molde do exemplo do dono, com cada lacuna preenchida só pelo que o condutor já tem em mãos naquele passo.
  - precisa de: stream de dados — Quem implementa recebe o comportamento do condutor do loop, isto é, o que ele escreve ao dono a cada passo, e o arquivo de progresso que um gancho do próprio kit alimenta com essas linhas. A ferramenta que roda os agentes e a extensão que desenha a tela ficam como estão.; tarefa — Quem implementa lê dela o que preenche as mensagens: qual tarefa, qual passo e o que o passo pede. Nada nela muda.; mente do agente — Quem implementa usa a intenção que o condutor já tem em mãos: o que ele pediu ao agente e o que o agente devolveu. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo.
- **Camada e fronteira:** kit, skill `scrum-master`, seção `## Repertório de mensagens ao gerente`: só as sete linhas da tabela que citam `loop.py` (`M-0`, `M-1`, `M-2`, `M-3`, `M-10`, `M-11`, `M-12`), e nelas só as colunas *momento* e *lacunas*. A terceira coluna (a frase-modelo, forma `A` aceita pelo dono no Marco 1) fica idêntica. Nenhum passo, agente ou instrumento muda.
- **Domínio:** *lacuna* = `<…>` na frase-modelo, preenchida por dado que o condutor já recebeu (`I-3`); com `loop.py` fora do plano, a próxima tarefa, o título e o objetivo chegam pela saída do `python .claude/tools/backlog.py next` do passo 2 (`F-12`: primeira linha `=== PRÓXIMA TAREFA: <ID> — <título> [<cabeçalho>]`, depois o card inteiro, inclusive a linha `- **Objetivo:**`; fila vazia imprime `nada delegável`).
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md:323` — as linhas 323 a 326 e 333 a 335 de 2026-09-24, as sete da tabela do repertório que contêm loop.py (localizar pelo texto)
- **Contratos/classes:** nenhum código.
- **Texto novo, literal** — cada uma das sete linhas da tabela cujo id é `M-0`, `M-1`, `M-2`, `M-3`, `M-10`, `M-11` ou `M-12` é substituída **inteira** pela linha de mesmo id abaixo, que é cópia das linhas corrigidas da `### 4.1` do plano (residência única, `DTG-10`); as outras oito linhas da tabela não mudam:

  ```
  | `M-0` | abertura da janela, antes do `backlog.py next` | `Abrindo a janela do plano <plano>: vou selecionar a próxima tarefa e conferir o modelo.` | `<plano>` ← o plano nomeado no despacho da janela |
  | `M-1` | passo 2, tarefa selecionada | `Tarefa <ID> — <título>. Passo: conferir os gates e preparar o despacho.` | `<ID>`, `<título>` ← linha `=== PRÓXIMA TAREFA:` da saída do `backlog.py next` (`F-12`) |
  | `M-2` | passo 3, gates aprovados, antes de materializar `in-progress` | `Tarefa <ID>: gates aprovados; vou materializar in-progress e gravar o ponto de partida.` | `<ID>` |
  | `M-3` | passo 4, antes de invocar o executor | `Agente executor recebe a tarefa <ID> e vai executar: <objetivo>.` | `<objetivo>` ← linha `- **Objetivo:**` do card, no bloco do dossiê da saída do `backlog.py next` (`F-12`) |
  | `M-10` | passo 9, antes do `modelo.py check` que abre o fechamento | `Scrum master vai fechar a tarefa <ID> como <done, blocked ou cancelled>: registrar estado, RDO e telemetria, e selecionar a próxima.` | `<estado>` ← decisão do bloco A |
  | `M-11` | passo 2 da volta seguinte a um "segue" do bloco B (passo 10), logo depois do `backlog.py next` e antes do `M-1` | `Scrum master concluiu a tarefa <ID> e vai pegar a tarefa <ID2> — <título2>.` | `<ID>` ← a tarefa fechada no passo 9; `<ID2>`, `<título2>` ← linha `=== PRÓXIMA TAREFA:` dessa saída do `backlog.py next` (`F-12`) |
  | `M-12` | passo 10, encerramento; ou passo 2 da volta seguinte a um "segue", quando o `backlog.py next` devolve `nada delegável` | `Scrum master concluiu a tarefa <ID>; <fila vazia, ou regra B1..B3 em uma frase>. Encerrando a janela com o relatório.` | ← regra do bloco B que casou, ou a linha `nada delegável` na saída do `backlog.py next` (`F-12`) |
  ```

  Na skill, cada linha começa na coluna 1 (sem os dois espaços de recuo deste bloco).
- **Passos:**
  1. Em `.claude/skills/scrum-master/SKILL.md`, localizar as sete linhas da tabela que contêm `loop.py`.
  2. Substituir cada uma, inteira, pela linha de mesmo id de `Texto novo, literal`, sem recuo.
  3. Rodar a Verificação 1 a 4.
- **Restrições desta tarefa:** a terceira coluna de cada linha (a frase-modelo) fica idêntica à de antes — é a forma aceita no Marco 1; `DTG-10` — divergência de um caractere entre as quinze linhas da skill e as da `### 4.1` é defeito (Verificação 3); `DTG-28` — nada de `git diff --numstat` como aceite: as linhas trocadas já são alteração não commitada da `TLG-T2`, e o `numstat` dá o mesmo valor antes e depois. Só estas sete linhas mudam.
- **Não fazer:** não editar a terceira coluna de nenhuma linha; não mexer nas outras oito linhas (`M-4` a `M-9`, `M-13`, `M-14`); não editar passo nenhum da skill nem acrescentar bullet `**Narra:**` (é `TLG-T4`); não editar a `passagem-de-bastao`, agente ou instrumento; não editar o plano.
- **Contingências:**
  - se o número de linhas da skill que contêm `loop.py` for diferente de `7` antes da edição → parar e sinalizar `blocked` razão `premissa`, devolvendo a saída de `grep -n "loop.py" .claude/skills/scrum-master/SKILL.md`;
  - se alguma das sete linhas com `loop.py` não é linha da tabela `M-<n>` → parar e sinalizar `blocked` razão `premissa` com essa linha.
- **Testes:** nenhum TF (texto de skill); TR: `python -m pytest tests/ -q` não reduz o total re-medido no despacho (referência histórica `277 passed`, 2026-09-23).
- **Verificação:**
  1. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "loop.py" | Measure-Object).Count` → antes `7` (medido 2026-09-24), depois `0`.
  2. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "backlog.py next" | Measure-Object).Count` → antes `1` (medido 2026-09-24), depois `6`.
  3. Igualdade linha a linha com a `### 4.1` do plano, bloco cercado por conter barra invertida:

     ```
     python -c "import re;f=lambda p:[l.rstrip() for l in open(p,encoding='utf-8') if re.match(r'^\| .M-\d+. \|',l)];a=f('.claude/skills/scrum-master/SKILL.md');b=f('docs/plans/P-0748-tela-do-gerente.md');print('iguais',sum(x==y for x,y in zip(a,b)),'de',len(a),len(b))"
     ```

     → antes `iguais 8 de 15 15` (medido 2026-09-24, em `pwsh` e em `powershell`), depois `iguais 15 de 15 15`.
  4. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` ≥ o total re-medido no despacho.
- **Pronto quando:** `stream de dados.repertório de mensagens` — *fechado: uma frase-modelo por transição do loop, no molde do exemplo do dono — "Tarefa X, passo Y.", "Agente executor recebe o passo Y e vai executar Z.", "Agente consultor aceitou a entrega." —; nenhuma lacuna pede ao condutor uma busca nova para ser preenchida* — Verificação 1 e 3.
- **Fora do escopo desta tarefa:** onde cada linha entra no fluxo e a forma com o marcador (`TLG-T4`); o gancho (`TLG-T3`).

### TLG-T4 — O condutor narra: uma linha do repertório antes de cada ato, na forma que o gancho grava [Sonnet · esforço medium · classe redacao]
- **Status:** `done` · 2026-09-24
- **Objetivo:** O mantenedor do loop faz o condutor narrar a execução: a cada transição ele escreve, antes de agir, a linha do repertório que a descreve, na forma que o gancho leva ao arquivo de progresso, e é essa linha, e não a saída das ferramentas, que chega ao dono.
- **Fundamento:** `DTG-7` (intenção, não raciocínio), `DTG-10` (a residência vigente do repertório é a seção da skill), `DTG-15` (colateral na `passagem-de-bastao`), `DTG-20`, `DTG-23` (marcador `[gerente] ` e os sete inícios), `DTG-24` (caminho do arquivo), `DTG-26` (não há `loop.py`), `DTG-28` (`numstat` como delta), `F-8`, `F-23`, `I-2`, `I-5`, `I-11`.
- **Depende de:** `TLG-T2a`
- **Operação do modelo:** `OP-4`
  - OP-4: O mantenedor do loop faz o condutor narrar a execução: a cada transição ele escreve, antes de agir, a linha do repertório que a descreve, na forma que o gancho leva ao arquivo de progresso, e é essa linha, e não a saída das ferramentas, que chega ao dono.
  - precisa de: stream de dados — Quem implementa recebe o comportamento do condutor do loop, isto é, o que ele escreve ao dono a cada passo, e o arquivo de progresso que um gancho do próprio kit alimenta com essas linhas. A ferramenta que roda os agentes e a extensão que desenha a tela ficam como estão.; tarefa — Quem implementa lê dela o que preenche as mensagens: qual tarefa, qual passo e o que o passo pede. Nada nela muda.; mente do agente — Quem implementa usa a intenção que o condutor já tem em mãos: o que ele pediu ao agente e o que o agente devolveu. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo.
- **Camada e fronteira:** kit — skill `scrum-master` (um bullet `**Narra:**` por passo, do 2 ao 10, e um bullet em `## Guardrails`) e skill `passagem-de-bastao` (a frase das linhas 12-13). Nenhum agente, instrumento, teste ou arquivo de configuração. O gancho que lê a forma prescrita aqui é o `.claude/tools/progresso_hook.py` da `TLG-T3`, que este card não edita.
- **Domínio:** *narrar* = escrever, como texto do agente e **antes** do ato que ela anuncia, a linha `M-<n>` da seção `## Repertório de mensagens ao gerente` da própria skill, preenchida, **sozinha numa linha** e começando pelo marcador literal `[gerente] ` (`DTG-23`, `I-2`, `I-5`). *Forma que o gancho leva ao arquivo* = o gancho copia para `.claude/estado/progresso.txt` só as linhas que, sem espaços nas pontas, começam por `[gerente] ` e cujo resto começa por `Abrindo a janela do plano `, `Tarefa `, `Agente executor `, `Agente revisor `, `Agente consultor `, `Agente modelador ` ou `Scrum master `, e grava o resto, sem o marcador.
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md:50` — a linha que começa por - **Ação:** no Passo 2; os nove bullets entram um por passo, imediatamente antes da linha que começa por - **Ação:** de cada passo 2 a 10 (linhas 50, 61, 79, 108, 126, 149, 159, 175 e 217 em 2026-09-24; localizar pelo cabeçalho do passo)
  - `.claude/skills/scrum-master/SKILL.md:344` — cabeçalho ## Guardrails, última seção do arquivo; o bullet novo entra depois do último bullet dela
  - `.claude/skills/passagem-de-bastao/SKILL.md:12` — as linhas 12 e 13, que terminam em e só lá.
- **Contratos/classes:** nenhum código.
- **Texto novo, literal:** em cada passo, o bullet entra imediatamente **antes** da linha que começa por `- **Ação:**` daquele passo (a narração precede o ato). O rótulo à esquerda (`Passo 2:` e os seguintes) não entra na skill:

  ```
  Passo 2:  - **Narra:** na abertura da janela, `M-0` antes do `backlog.py next`; na volta seguinte a um "segue" do passo 10, `M-11` logo depois do `backlog.py next`, ou `M-12` se ele devolve `nada delegável`; com a tarefa selecionada, `M-1`. Na abertura com `nada delegável`, nenhuma linha além do `M-0`.
  Passo 3:  - **Narra:** aprovados os três gates, `M-2` antes de materializar `in-progress`.
  Passo 4:  - **Narra:** `M-3` antes de invocar o `pantonic-executor`, com o `<objetivo>` copiado da linha `- **Objetivo:**` do dossiê.
  Passo 5:  - **Narra:** `M-4` assim que a linha de retorno é lida, antes de qualquer ato do passo 6 ou 8.
  Passo 6:  - **Narra:** `M-5` antes do `review_evidence.py`; `M-6` antes de invocar o `pantonic-reviewer`.
  Passo 7:  - **Narra:** `M-7` assim que as duas linhas de retorno são lidas.
  Passo 8:  - **Narra:** `M-8` antes de invocar o `pantonic-consultant`; `M-9` assim que a rota é lida; `M-14` antes de invocar o `pantonic-model-designer`.
  Passo 9:  - **Narra:** `M-10` antes do `modelo.py check` que abre o fechamento.
  Passo 10: - **Narra:** em `B0`, `M-13` antes do `review_evidence.py --atribuir`; com encerramento, `M-12` antes do relatório; com "segue", nenhuma linha neste passo — o `M-11` sai no passo 2 seguinte.
  ```

  Em `## Guardrails`, acrescentar como último bullet, numa linha só:

  ```
  - Toda linha do repertório (seção *Repertório de mensagens ao gerente*) é escrita como texto do agente, **sozinha numa linha**, começando pelo marcador literal `[gerente] ` seguido da frase-modelo preenchida — por exemplo `[gerente] Agente revisor devolveu a tarefa TLG-T2: aprovado 100%, bloqueante nenhuma.` — e antes do ato que ela anuncia. O gancho `.claude/tools/progresso_hook.py` (eventos `PostToolUse` e `Stop`) copia para `.claude/estado/progresso.txt`, sem o marcador, só as linhas marcadas cujo resto começa por `Abrindo a janela do plano `, `Tarefa `, `Agente executor `, `Agente revisor `, `Agente consultor `, `Agente modelador ` ou `Scrum master `; é esse arquivo que o gerente lê, no painel fora da extensão, e nenhuma saída de ferramenta chega a ele. O loop nunca escreve no arquivo diretamente (`P-0748`, `DTG-23`, `I-2`, `I-5`, `I-11`).
  ```

  Em `passagem-de-bastao/SKILL.md`, substituir as duas linhas 12-13, hoje exatamente assim:

  ```
  acompanha. Não é skill de comunicação com humano; o que chega ao dono chega pelo **relatório de
  encerramento** do `scrum-master`, e só lá.
  ```

  por estas três linhas:

  ```
  acompanha. Não é skill de comunicação com humano; o que chega ao dono chega pelas linhas do
  **repertório de mensagens ao gerente**, que o gancho do kit grava no arquivo de progresso, e pelo
  **relatório de encerramento** do `scrum-master`, e só por eles.
  ```
- **Passos:**
  1. Medir a base: `git diff --numstat -- .claude/skills/scrum-master/SKILL.md` → anotar `<a> <r>` (linhas adicionadas e removidas) para a Verificação 6.
  2. Na `scrum-master`, inserir o bullet `**Narra:**` de cada passo, 2 a 10, imediatamente antes da linha `- **Ação:**` daquele passo — nove bullets, uma linha cada.
  3. Acrescentar o bullet de `## Guardrails` depois do último bullet da seção.
  4. Na `passagem-de-bastao`, substituir as linhas 12-13 pelas três linhas dadas.
  5. Rodar a Verificação 1 a 7.
- **Restrições desta tarefa:** `I-2` — a linha narrada é texto do agente, nunca saída de comando; `I-5` — a linha que anuncia um ato vem antes dele; `I-11` — a skill não manda o loop escrever no arquivo de progresso; `DTG-10` — o card cita `M-<n>` e **não** recopia frases do repertório; `DTG-23` — o marcador é exatamente `[gerente] ` e os sete inícios são exatamente os do `Domínio`. Na `scrum-master`, só inserções (dez linhas); na `passagem-de-bastao`, só a troca das duas linhas pelas três.
- **Não fazer:** não editar bullets `**Ação:**` nem nenhuma outra linha existente da `scrum-master`; não editar a tabela do repertório (é `TLG-T2a`); não acrescentar proibição de leitura no topo (a antiga `I-10` foi revogada, `DTG-26`); não citar `loop.py`; não editar agente, instrumento, `progresso_hook.py`, `projecoes.json` ou `README.md` (é `TLG-T5`); não acrescentar frase nova ao repertório (frase que faltar é a contingência 1).
- **Contingências:**
  - se algum passo precisar de uma frase que não existe entre `M-0` e `M-14` → parar e sinalizar `blocked` razão `premissa` com o passo e a transição sem frase;
  - se a skill ainda contém `loop.py` → parar e sinalizar `blocked` razão `dependencia` (`TLG-T2a` não entregou);
  - se algum dos passos 2 a 10 não tem exatamente uma linha que começa por `- **Ação:**` → parar e sinalizar `blocked` razão `premissa` com a lista das linhas da skill que começam por `- **Ação:**` (número e texto);
  - se as linhas 12-13 da `passagem-de-bastao` não contêm `e só lá` → parar e sinalizar `blocked` razão `premissa` com a saída de `grep -n "só lá" .claude/skills/passagem-de-bastao/SKILL.md`.
- **Testes:** nenhum TF (texto de skill); TR: `python -m pytest tests/ -q` não reduz o total re-medido no despacho.
- **Verificação:**
  1. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "**Narra:**" | Measure-Object).Count` → antes `1` (medido 2026-09-24: a frase de abertura da seção do repertório cita o bullet), depois `10`.
  2. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "[gerente] " | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`.
  3. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "progresso.txt" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`.
  4. `(Select-String -SimpleMatch -Path .claude/skills/passagem-de-bastao/SKILL.md -Pattern "e só lá" | Measure-Object).Count` → antes `1` (medido 2026-09-24), depois `0`.
  5. `(Select-String -SimpleMatch -Path .claude/skills/passagem-de-bastao/SKILL.md -Pattern "arquivo de progresso" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`.
  6. `git diff --numstat -- .claude/skills/scrum-master/SKILL.md` → com a base `<a> <r>` do passo 1: removidas `= <r>` e adicionadas `≥ <a> + 10` (delta contra a base re-medida no despacho, `DTG-28`; nunca o total contra `HEAD`).
  7. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` ≥ o total re-medido no despacho.
- **Pronto quando:** `stream de dados.o que as mensagens narram` — *ligado à tarefa e à intenção dos agentes: uma linha em linguagem humana por transição, escrita pelo condutor antes de agir, e é ela que chega ao arquivo de progresso, sem saída de comando entre duas delas* — Verificação 1, 2, 3, 4, 5 e 6.
- **Fora do escopo desta tarefa:** a descrição pública e o painel (`TLG-T5`); a leitura do painel pelo dono (Marco 3, aceite de marco e não de card, `I-6`).

### TLG-T3a — A captura do payload dos ganchos: o que a função vai ler [Sonnet · esforço low · classe investigacao]
- **Status:** `done` · 2026-09-24
- **Objetivo:** O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo. *(Este card é a sonda que a operação exige antes da função: mede a forma do payload que a função vai ler, `DTG-32`.)*
- **Fundamento:** `DTG-30` (mecanismo por evento), `DTG-31` (residência: o mesmo script), `DTG-32` (medida antes da implementação — este card), `F-24` (estrutura do script e dos testes), `F-25` (declaração dos ganchos, que não muda aqui), `F-30` (payload; a forma de `tool_response` é o não medido), `F-31` (o flag e a captura são ignorados pelo git), `I-1`, `I-7`, `I-11`.
- **Depende de:** `TLG-T4`
- **Operação do modelo:** `OP-3`
  - OP-3: O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo.
  - precisa de: stream de dados — Quem implementa recebe o loop do condutor — as transições que ele atravessa a cada tarefa e o que ele tem em mãos em cada uma —, a função do kit que gera a linha a partir do evento de cada transição, e o arquivo de progresso onde essa função grava. A ferramenta que roda os agentes e o painel que mostra o arquivo ficam como estão.; tarefa — Quem implementa lê dela o que preenche as mensagens: qual tarefa, o título dela, qual passo e o que o passo pede. Nada nela muda.; mente do agente — Quem implementa usa a intenção que o condutor já tem em mãos — o que ele pediu ao agente e o que o agente devolveu — como campo do evento que a função recebe. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo.
- **Camada e fronteira:** kit — só `.claude/tools/progresso_hook.py` (três constantes, uma função nova e **uma** chamada dentro de `main`) e `tests/test_progresso_hook.py` (três TFs acrescentados ao fim); cria o arquivo-flag `.claude/estado/progresso-captura.on`, ignorado pelo git pela regra vigente `.claude/estado/*` (`git check-ignore -q` sai `0`, `F-31`). O script continua só com biblioteca padrão e sem importar instrumento do kit. Nenhuma skill, agente, `README.md`, `.claude/projecoes.json`, `.claude/settings.json`, `.gitignore` muda; o comportamento existente do gancho (copiar as linhas marcadas do transcript) fica **intacto** até `TLG-T3b`.
- **Domínio:** *captura* = uma linha JSON por disparo do gancho na sessão principal, gravada em `.claude/estado/progresso-captura.jsonl`, com a forma de `tool_input` e de `tool_response` — é o dado que `F-30` diz não medido. *Flag* = `.claude/estado/progresso-captura.on`: a captura só roda se ele existe. *Payload* = o JSON do stdin do gancho (`F-30`): `hook_event_name`, `tool_name`, `tool_input`, `tool_response` (só no `PostToolUse`), `agent_type` (só dentro de agente despachado). *Sessão principal* = payload sem `agent_type` — a barreira de `DTG-22` já existe em `main` e a captura fica **depois** dela.
- **Arquivos-alvo:**
  - `.claude/tools/progresso_hook.py:16` — a linha que começa por INICIOS = (; as três constantes novas entram depois do fechamento dessa tupla e antes de def linhas_do_repertorio
  - `.claude/tools/progresso_hook.py:61` — a linha def main(; a chamada nova entra dentro de main, imediatamente depois da linha estado.mkdir(parents=True, exist_ok=True) e antes da linha trava = estado / "progresso.lock" (as duas únicas no arquivo)
  - `tests/test_progresso_hook.py:261` — a linha def test_tf_prog_9_trava(tmp_path):, último teste do arquivo; os três TFs novos entram depois do fim dessa função
  - `.claude/estado/progresso-captura.on (novo)` — arquivo vazio, criado no passo 4
- **Contratos/classes:**

  ```python
  CAPTURA_FLAG = "progresso-captura.on"
  CAPTURA_ARQ = "progresso-captura.jsonl"
  CAPTURA_TETO_BYTES = 1_000_000

  def capturar(payload: dict, estado: Path) -> None: ...
  ```

  Semântica fechada de `capturar`: tudo dentro de `try`/`except Exception: return` (falha aberta, nunca imprime). (1) Se `not (estado / CAPTURA_FLAG).exists()` → `return`. (2) `arq = estado / CAPTURA_ARQ`; se `arq.exists() and arq.stat().st_size > CAPTURA_TETO_BYTES` → `return`. (3) `ti = payload.get("tool_input")`; `resp = payload.get("tool_response")`; `registro = {"evento": payload.get("hook_event_name"), "tool": payload.get("tool_name"), "input_chaves": sorted(ti.keys()) if isinstance(ti, dict) else type(ti).__name__, "command": str(ti.get("command", ""))[:120] if isinstance(ti, dict) else "", "subagent_type": ti.get("subagent_type") if isinstance(ti, dict) else None, "response_tipo": type(resp).__name__, "response_chaves": sorted(resp.keys()) if isinstance(resp, dict) else None, "response": json.dumps(resp, ensure_ascii=False, default=str)[:2000]}`. (4) Abrir `arq` em modo `"a"`, `encoding="utf-8"`, `newline="\n"`, e escrever `json.dumps(registro, ensure_ascii=False) + "\n"`. A chamada em `main` é exatamente `capturar(payload, estado)`, uma linha, depois de `estado.mkdir(parents=True, exist_ok=True)` e antes de `trava = estado / "progresso.lock"` — portanto depois da barreira `if payload.get("agent_type"): return 0` e depois do `if not tp: return 0` (todo payload de `PreToolUse`, `PostToolUse` e `Stop` traz `transcript_path`, `F-30`).
- **Método de sondagem:** o corpus é a sessão principal que conduz este plano: a captura instalada aqui grava, sem nenhum ato do condutor, um registro por gancho disparado no ciclo deste próprio card (retorno do executor e do revisor pela ferramenta `Agent`, `backlog.py status`, `review_evidence.py`, `rdo.py close`, `backlog.py next`) e no ciclo de `TLG-T2b`. A métrica é a forma de `tool_response` por (`evento`, `tool`): tipo, chaves e os primeiros 2000 caracteres. O agregado **não volta a este contexto**: quem o lê é `TLG-T3b`, no passo 1, com teto de 1 MB no arquivo. Sequência de edição:
  1. Rodar `python -m pytest tests/test_progresso_hook.py -q` e anotar o total (contingência 2).
  2. Em `.claude/tools/progresso_hook.py`, acrescentar as três constantes e a função `capturar` de `Contratos/classes`, depois de `INICIOS` e antes de `def linhas_do_repertorio`.
  3. Em `main`, inserir a linha `        capturar(payload, estado)` (oito espaços de recuo, o mesmo das linhas vizinhas) imediatamente depois de `estado.mkdir(parents=True, exist_ok=True)`.
  4. Acrescentar ao fim de `tests/test_progresso_hook.py` os três TFs de `Testes`, no mesmo padrão dos existentes (`main(entrada=json.dumps(payload), estado=tmp_path / "estado")`, transcript vazio criado em `tmp_path`).
  5. Criar o flag: `python -c "open('.claude/estado/progresso-captura.on', 'w').close()"`.
  6. Rodar a Verificação 1 a 5.
- **Restrições desta tarefa:** `I-11` — o gancho continua sem imprimir e saindo `0`; a captura é falha aberta. `DTG-22` — a captura fica **depois** da barreira `agent_type`: nenhum registro de chamada feita dentro de agente despachado. Os nove `TF-PROG` existentes ficam intactos e verdes. Estrutural, sem teste: nenhum import novo além dos já presentes (`json`, `os`, `sys`, `time`, `pathlib`); `linhas_do_repertorio`, `ler_novas` e o bloco da trava não mudam.
- **Não fazer:** não escrever a função geradora nem mexer em `FRASES`, transcript, cursor ou trava (é `TLG-T3b`); não editar `.claude/projecoes.json` nem `.claude/settings.json`; não tocar skill, agente, `README.md`, `.gitignore`; não apagar nem renomear TF existente; não gravar na captura o `transcript_path` nem ler o transcript para ela; não criar a captura quando o flag não existe; não ler `.claude/estado/progresso-captura.jsonl` neste card (o dado só existe depois do retorno).
- **Contingências:**
  1. se `(Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "estado.mkdir(" | Measure-Object).Count` não for `1` antes da edição → parar e sinalizar `blocked` razão `premissa`, devolvendo a saída de `grep -n "mkdir" .claude/tools/progresso_hook.py`;
  2. se `python -m pytest tests/test_progresso_hook.py -q` antes da edição não sair `9 passed` → parar e sinalizar `blocked` razão `dependencia`, devolvendo a linha de sumário;
  3. se o modo de permissão recusar a criação do flag → parar e sinalizar `blocked` razão `ferramenta` com a linha `flag recusado pelo modo de permissão; o dono roda: python -c "open('.claude/estado/progresso-captura.on', 'w').close()"`; o agente não contorna a recusa;
  4. se `python -m pytest tests/ -q` reduzir o total por teste fora de `tests/test_progresso_hook.py` → parar e sinalizar `blocked` razão `dependencia` com o nome do teste.
- **Testes:** `tests/test_progresso_hook.py`, `estado = tmp_path / "estado"`, transcript = arquivo vazio `tmp_path / "t.jsonl"` cujo caminho vai em `transcript_path`. Para cada TF, o valor que a regra concorrente daria vem entre parênteses.
  - `TF-CAP-1` — flag ligado: criar `estado / "progresso-captura.on"`; payload `{"hook_event_name": "PostToolUse", "tool_name": "Bash", "tool_input": {"command": "python x.py"}, "tool_response": {"stdout": "x"}, "transcript_path": <t.jsonl>, "session_id": "s1"}`; `main(...)` devolve `0`; `estado / "progresso-captura.jsonl"` existe, tem exatamente uma linha, e `json.loads` dela tem `evento == "PostToolUse"`, `tool == "Bash"`, `input_chaves == ["command"]`, `command == "python x.py"`, `response_tipo == "dict"`, `response_chaves == ["stdout"]` e `response == '{"stdout": "x"}'` (sem a captura: arquivo inexistente).
  - `TF-CAP-2` — flag desligado: o mesmo payload sem o flag; `progresso-captura.jsonl` não existe e `main` devolve `0` (captura incondicional: uma linha).
  - `TF-CAP-3` — barreira: flag ligado e payload com `"agent_type": "pantonic-executor"`; `progresso-captura.jsonl` não existe e a pasta `estado` não foi criada (captura antes da barreira: uma linha).

  Suítes: `python -m pytest tests/test_progresso_hook.py -q`; `python -m pytest tests/ -q`.
- **Verificação:**
  1. `python -m pytest tests/test_progresso_hook.py -q` → antes `9 passed` (medido 2026-09-24, `F-24`), depois `12 passed`.
  2. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` = total re-medido no despacho + `3` (referência histórica `289 passed`, 2026-09-24, `F-33`).
  3. `(Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "def capturar(" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`; e `(Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "capturar(payload, estado)" | Measure-Object).Count` → antes `0`, depois `1`.
  4. `Test-Path .claude/estado/progresso-captura.on` → antes `False` (medido 2026-09-24: a pasta contém só `progresso-cursor.json`, `progresso.txt` e `.gitkeep`), depois `True`.
  5. `(Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "print(" | Measure-Object).Count` → antes `0`, depois `0`.
- **Pronto quando (o fato que tem de existir ao final):** o gancho grava um registro por disparo na sessão principal enquanto o flag existe (`TF-CAP-1`, Verificação 1 e 3) e o flag existe no disco (Verificação 4) — é o insumo de `TLG-T3b`, que é quem leva `stream de dados.arquivo de progresso`, `stream de dados.repertório de mensagens` e `stream de dados.agregação da linha` ao estado final da `### 1.3` (versão 3). A leitura do agregado é o passo 1 de `TLG-T3b`, nunca deste card.
- **Fora do escopo desta tarefa:** a função geradora, `FRASES`, o `PreToolUse` no `projecoes.json`, a remoção do transcript e do cursor (`TLG-T3b`); a tabela da skill (`TLG-T2b`); a skill deixar de narrar (`TLG-T4a`); o `README.md` (`TLG-T5`).

### TLG-T2b — O repertório como tabela de eventos: a skill diz o que a função gera [Sonnet · esforço low · classe redacao]
- **Status:** `done` · 2026-09-24
- **Objetivo:** O redator do loop escreve o repertório fechado de mensagens: uma frase-modelo para cada transição do loop — tarefa e passo, agente despachado e o que vai fazer, veredito recebido, próxima tarefa —, no molde do exemplo do dono, com cada lacuna preenchida só pelo que o condutor já tem em mãos naquele passo.
- **Fundamento:** `DTG-29` (ato do dono: função, agregação, frase da evidência), `DTG-33` (título entre aspas), `DTG-34` (lacunas sem campo), `DTG-35` (a frase da evidência), `DTG-36` (`DTG-10` reescrita: a seção da skill é cópia legível da `### 4.1`), `DTG-37` (ordem: roda antes de `TLG-T3b`, que confere o código contra esta tabela no `TF-GER-18`), `DTG-28` (aceite por conteúdo, não por `numstat`), `F-26`, `I-2`, `I-3`, `I-12`.
- **Depende de:** `TLG-T3a`
- **Operação do modelo:** `OP-2`
  - OP-2: O redator do loop escreve o repertório fechado de mensagens: uma frase-modelo para cada transição do loop — tarefa e passo, agente despachado e o que vai fazer, veredito recebido, próxima tarefa —, no molde do exemplo do dono, com cada lacuna preenchida só pelo que o condutor já tem em mãos naquele passo.
  - precisa de: stream de dados — Quem implementa recebe o loop do condutor — as transições que ele atravessa a cada tarefa e o que ele tem em mãos em cada uma —, a função do kit que gera a linha a partir do evento de cada transição, e o arquivo de progresso onde essa função grava. A ferramenta que roda os agentes e o painel que mostra o arquivo ficam como estão.; tarefa — Quem implementa lê dela o que preenche as mensagens: qual tarefa, o título dela, qual passo e o que o passo pede. Nada nela muda.; mente do agente — Quem implementa usa a intenção que o condutor já tem em mãos — o que ele pediu ao agente e o que o agente devolveu — como campo do evento que a função recebe. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo.
- **Camada e fronteira:** kit, skill `scrum-master`, **só** a seção `## Repertório de mensagens ao gerente` — do primeiro parágrafo depois do cabeçalho até a última linha da tabela, antes da linha em branco que precede `## Proibições`. Os bullets `- **Narra:**` dos passos, o bullet de `## Guardrails` com o marcador e a `passagem-de-bastao` são de `TLG-T4a`; o código é de `TLG-T3b`. Nenhum passo, agente, instrumento, teste ou configuração muda.
- **Domínio:** *frase gerada* = a linha que `progresso_hook.py` grava em `.claude/estado/progresso.txt` no evento nomeado, com as lacunas `<…>` preenchidas por campo do evento ou por leitura local da função (`I-3`); `<título>` = título do card entre aspas duplas, `<título do plano>` = título do plano (`I-12`). *Evento* = disparo de `PreToolUse`, `PostToolUse` ou `Stop` na sessão principal, com a ferramenta e a detecção da coluna 2. O condutor não escreve nenhuma dessas linhas (`I-2`).
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md:322` — cabeçalho ## Repertório de mensagens ao gerente (única linha que começa assim); a seção vai até a linha anterior à linha em branco que precede ## Proibições (linha 348 em 2026-09-24; localizar pelo texto)
- **Contratos/classes:** nenhum código.
- **Texto novo, literal** — tudo o que está entre o cabeçalho `## Repertório de mensagens ao gerente` (que fica) e a linha em branco antes de `## Proibições` (que fica) é substituído por este bloco, exatamente, sem recuo (as 23 linhas da tabela são cópia caractere a caractere da `### 4.1` do plano, versão 3 — residência normativa, `DTG-36`):

  ```
  As linhas que o gerente lê no painel são **geradas** pelo gancho `.claude/tools/progresso_hook.py`
  a partir do evento de cada transição do loop — o condutor não escreve nenhuma delas, não usa
  marcador e não escreve no arquivo de progresso (`P-0748`, `DTG-30`, `I-2`, `I-11`). Esta tabela é a
  cópia legível do que a função gera (a residência vigente é o dicionário `FRASES` do gancho; a
  normativa, a `### 4.1` do plano): uma linha por forma de frase, com o gancho, a ferramenta e a
  detecção que a disparam e o campo do evento que preenche cada lacuna `<…>`. `<título>` é o
  título do card entre aspas duplas e `<título do plano>` o do plano — a sigla nunca chega sozinha
  ao gerente (`I-12`). Outras ferramentas, outros comandos e outros `subagent_type` não geram linha.

  | id | evento (gancho · ferramenta · detecção) | frase gerada | lacunas ← campo do evento ou leitura local |
  |---|---|---|---|
  | `M-0` | tarefa escolhida, primeira da sessão — `PostToolUse` · `Bash` · `command` contém `backlog.py next` · resposta contém `=== PRÓXIMA TAREFA: ` · estado sem `aberta` | `Abrindo a janela do plano "<título do plano>".` | `<título do plano>` ← `localizar_card(<ID>)`; vazio → linha omitida. Sai antes de `M-11` e de `M-1` |
  | `M-1` | tarefa escolhida — o mesmo evento de `M-0`, sempre | `Tarefa "<título>". Passo: conferir os gates e preparar o despacho.` | `<ID>`, `<título>` ← linha `=== PRÓXIMA TAREFA: <ID> — <título> [` da resposta. Estado ← `tarefa`, `titulo`, `objetivo`, `titulo_plano` (de `localizar_card`), `aberta` = true, `encerrada` = false |
  | `M-2` | estado mudado para in-progress — `PreToolUse` · `Bash` · `command` casa `backlog\.py status (\S+) in-progress` | `Tarefa "<título>": gates aprovados; vou materializar in-progress e gravar o ponto de partida.` | `<título>` ← estado se `<ID>` é a `tarefa` do estado, senão `localizar_card(<ID>)`. `status <ID> review` não gera linha |
  | `M-3` | agente despachado, executor — `PreToolUse` · `Agent` · `subagent_type` = `pantonic-executor` · objetivo não vazio | `Agente executor recebe a tarefa "<título>" e vai executar: <objetivo>` | `<título>`, `<objetivo>` ← tarefa corrente (`DTG-33` (iv)) e `localizar_card`; `<objetivo>` já termina em ponto, ou em `…` se truncado |
  | `M-3b` | o mesmo evento de `M-3`, objetivo vazio | `Agente executor recebe a tarefa "<título>" e vai executar o card.` | `<título>` como em `M-3` |
  | `M-4` | agente de volta, executor — `PostToolUse` · `Agent` · `pantonic-executor` · primeira linha não vazia da resposta casa `^(\S+) review(?:\s+pendencia=(.*))?$` | `Agente executor devolveu a tarefa "<título>": review — <pendência>.` | `<pendência>` ← grupo 2; ausente → `sem pendência` |
  | `M-4b` | o mesmo evento, primeira linha casa `^(\S+) blocked motivo=(\S+)\s*(.*)$` | `Agente executor devolveu a tarefa "<título>": blocked — motivo <motivo>: <razão>.` | `<motivo>` ← grupo 2; `<razão>` ← grupo 3 |
  | `M-5` | evidência coletada — `PreToolUse` · `Bash` · `command` contém `review_evidence.py` e `--tarefa <ID>`, e não contém `--atribuir` | `Tarefa "<título>": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.` | `<ID>` ← `--tarefa (\S+)` no comando; `<título>` ← estado ou `localizar_card` |
  | `M-6` | agente despachado, revisor — `PreToolUse` · `Agent` · `pantonic-reviewer` | `Agente revisor recebe a tarefa "<título>" e vai confrontar a entrega com o card.` | `<título>` ← tarefa corrente |
  | `M-7` | agente de volta, revisor — `PostToolUse` · `Agent` · `pantonic-reviewer` · primeira linha casa `^(\S+) (\S+) (\d+) bloqueante=(.*)$` | `Agente revisor devolveu a tarefa "<título>": <veredito> <percentual>%, bloqueante <bloqueante>.` | `<veredito>` ← grupo 2; `<percentual>` ← grupo 3; `<bloqueante>` ← grupo 4 |
  | `M-8` | agente despachado, consultor — `PreToolUse` · `Agent` · `pantonic-consultant` | `Agente consultor recebe a parada da tarefa "<título>" e vai triar.` | `<título>` ← tarefa corrente. A regra A-n/B-n saiu (`DTG-34`) |
  | `M-9` | agente de volta, consultor — `PostToolUse` · `Agent` · `pantonic-consultant` · resposta contém `rota=(\S+)` e não contém `estrategico=` | `Agente consultor devolveu a tarefa "<título>": rota <rota>.` | `<rota>` ← grupo 1 |
  | `M-9b` | o mesmo evento, resposta contém também `estrategico=(.*)` | `Agente consultor devolveu a tarefa "<título>": rota <rota>; estratégico: <frase>.` | `<frase>` ← grupo 1 de `estrategico=`, até o fim da linha |
  | `M-10` | tarefa fechada — `PreToolUse` · `Bash` · `command` casa `backlog\.py status (\S+) (\S+)` com `<estado>` igual a `done`, `blocked` ou `cancelled` | `Scrum master vai fechar a tarefa "<título>" como <estado>: registrar estado, RDO e telemetria, e selecionar a próxima.` | `<estado>` ← grupo 2. Estado ← `tarefa_fechada` = `<ID>`, `titulo_fechada` = `<título>` |
  | `M-11` | tarefa escolhida com tarefa fechada na sessão — o evento de `M-1`, estado com `tarefa_fechada` | `Scrum master concluiu a tarefa "<título fechada>" e vai pegar a tarefa "<título>".` | `<título fechada>` ← `titulo_fechada` do estado; sai depois de `M-0` e antes de `M-1`, e limpa `tarefa_fechada` |
  | `M-12` | fila vazia — `PostToolUse` · `Bash` · `backlog.py next` · resposta contém `nada delegável` · estado com `tarefa_fechada` | `Scrum master concluiu a tarefa "<título fechada>"; nada delegável na fila. Encerrando a janela com o relatório.` | `<título fechada>` ← estado; limpa `tarefa_fechada`. A regra B1..B3 saiu (`DTG-34`) |
  | `M-12b` | o mesmo evento, estado sem `tarefa_fechada` | `Scrum master não encontrou tarefa delegável na fila. Encerrando a janela com o relatório.` | nenhuma lacuna |
  | `M-13` | atribuição medida — `PreToolUse` · `Bash` · `command` contém `review_evidence.py`, `--tarefa <ID>` e `--atribuir` | `Tarefa "<título>": vou medir a que arquivo a pendência é atribuível.` | como `M-5` |
  | `M-14` | agente despachado, modelador — `PreToolUse` · `Agent` · `pantonic-model-designer` · `prompt` casa `Ato:\s*` seguido, com ou sem crase, de `autoria`, `emenda` ou `conflito` | `Agente modelador recebe a tarefa "<título>" e vai fazer <ato> no modelo.` | `<ato>` ← a palavra casada |
  | `M-14b` | o mesmo evento, sem casamento no `prompt` | `Agente modelador recebe a tarefa "<título>" e vai atualizar o modelo.` | `<título>` ← tarefa corrente |
  | `M-15` | agente despachado, planejador — `PreToolUse` · `Agent` · `pantonic-planner` | `Agente planejador recebe a tarefa "<título>" e vai replanejar.` | `<título>` ← tarefa corrente |
  | `M-16` | agente de volta, forma genérica — `PostToolUse` · `Agent` · `pantonic-model-designer` ou `pantonic-planner`; ou `pantonic-executor`, `pantonic-reviewer`, `pantonic-consultant` cuja resposta não casa `M-4`, `M-4b`, `M-7`, `M-9` nem `M-9b` | `Agente <papel> devolveu a tarefa "<título>": <primeira linha>.` | `<papel>` ← `executor`, `revisor`, `consultor`, `modelador` ou `planejador` pelo `subagent_type`; `<primeira linha>` ← primeira linha não vazia da resposta, até 160 caracteres mais `…`; resposta vazia → `(sem texto)` |
  | `M-17` | janela encerrada — `Stop` · estado com `aberta` e sem `encerrada` | `Scrum master encerrou a janela; o relatório está na extensão.` | nenhuma lacuna; estado ← `encerrada` = true. Segundo `Stop` da mesma sessão não gera linha |
  ```

  Na skill, cada linha começa na coluna 1 (sem os dois espaços de recuo deste bloco).
- **Passos:**
  1. Em `.claude/skills/scrum-master/SKILL.md`, localizar o cabeçalho `## Repertório de mensagens ao gerente` e o cabeçalho `## Proibições`.
  2. Substituir tudo entre a linha em branco depois do primeiro e a linha em branco antes do segundo pelo bloco de `Texto novo, literal`, sem recuo, mantendo uma linha em branco antes e depois.
  3. Rodar a Verificação 1 a 6.
- **Restrições desta tarefa:** `DTG-36` — divergência de um caractere entre as 23 linhas da tabela na skill e as da `### 4.1` do plano é defeito (Verificação 3); o parágrafo não cita `**Narra:**`, `[gerente] ` nem `loop.py`; `DTG-28` — nada de `git diff --numstat` como aceite (a seção já é alteração não commitada de `TLG-T2`/`TLG-T2a`): o aceite é por conteúdo, antes e depois. Só esta seção muda.
- **Não fazer:** não editar nenhum bullet `- **Narra:**` nem o bullet de `## Guardrails` (é `TLG-T4a`); não editar passo, `## Proibições`, `## Guardrails`, `passagem-de-bastao`, agente, instrumento, teste, `README.md` ou o plano; não reescrever frase da tabela por conta própria — a tabela é cópia; não acrescentar nem remover linha da tabela.
- **Contingências:**
  1. se `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "## Repertório de mensagens ao gerente" | Measure-Object).Count` não for `1` → parar e sinalizar `blocked` razão `premissa`, devolvendo a saída de `grep -n "Repertório de mensagens ao gerente" .claude/skills/scrum-master/SKILL.md`;
  2. se `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "## Proibições" | Measure-Object).Count` não for `1` → parar e sinalizar `blocked` razão `premissa` com a saída de `grep -n "Proibições" .claude/skills/scrum-master/SKILL.md`;
  3. se a skill contém `loop.py` → parar e sinalizar `blocked` razão `dependencia` (`TLG-T2a` não entregou).
- **Testes:** nenhum TF (texto de skill); TR: `python -m pytest tests/ -q` não reduz o total re-medido no despacho.
- **Verificação:**
  1. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "**Narra:**" | Measure-Object).Count` → antes `10` (medido 2026-09-24, `F-26`), depois `9` (some a frase do parágrafo antigo; os nove bullets ficam para `TLG-T4a`).
  2. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "progresso_hook.py" | Measure-Object).Count` → antes `1` (medido 2026-09-24), depois `2`.
  3. Igualdade linha a linha com a `### 4.1` do plano, bloco cercado por conter barra invertida:

     ```
     python -c "import re;f=lambda p:[l.rstrip() for l in open(p,encoding='utf-8') if re.match(r'^\| .M-\d+b?. \|',l)];a=f('.claude/skills/scrum-master/SKILL.md');b=f('docs/plans/P-0748-tela-do-gerente.md');print('iguais',sum(x==y for x,y in zip(a,b)),'de',len(a),len(b))"
     ```

     → antes `iguais 0 de 15 23` (medido 2026-09-24, depois desta rodada gravar a `### 4.1`), depois `iguais 23 de 23 23`.
  4. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "evidência mecânica" | Measure-Object).Count` → antes `2` (medido 2026-09-24: a linha `M-5` e a `- **Ação:**` do passo 6, `:131`), depois `1` (só a do passo 6, que este card não toca).
  5. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "M-17" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`.
  6. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` ≥ o total re-medido no despacho.
- **Pronto quando:** `stream de dados.repertório de mensagens` — *fechado e embutido na função que gera a linha: uma frase por evento de transição do loop, no molde do exemplo do dono — "Tarefa X, passo Y.", "Agente executor recebe o passo Y e vai executar Z.", "Agente consultor aceitou a entrega." —, em que cada frase diz o que o ato faz, sem termo que o dono não consiga antecipar: a da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit —, e cada lacuna se preenche pelo campo do evento, não pela mão do condutor* — Verificação 3, 4 e 5 (a parte "embutido na função" é medida por `TLG-T3b`, `TF-GER-18`, contra esta tabela).
- **Fora do escopo desta tarefa:** o código que gera as frases (`TLG-T3b`); os bullets `**Narra:**`, o guardrail do marcador e a `passagem-de-bastao` (`TLG-T4a`); o `README.md` (`TLG-T5`).

### TLG-T3b — A função que gera a linha do stream a cada evento do loop [Sonnet · esforço high · classe implementacao]
- **Status:** `done` · 2026-09-24
- **Objetivo:** O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo.
- **Fundamento:** `DTG-30` (mecanismo: eventos derivados de `tool_name` + `tool_input` + `tool_response` + estado), `DTG-31` (residência e estado próprio), `DTG-32` (a captura de `TLG-T3a` é o insumo do passo 1), `DTG-33` (normalização da resposta, `localizar_card`, aspas, tarefa corrente), `DTG-34` (lacunas sem campo), `DTG-35` (frase da evidência), `DTG-36` (`FRASES` é a residência vigente; `TF-GER-18` confere contra a skill), `DTG-38` (materialização), `DTG-39` (agente de volta em modo hand-back: `pendentes` + `UserPromptSubmit`), `DTG-22` (barreira `agent_type`), `DTG-24` (caminhos), `DTG-25` (eventos declarados), `F-24`, `F-25`, `F-29`, `F-30`, `F-31`, `I-1`, `I-3`, `I-5`, `I-7`, `I-11`, `I-12`, `R-7`.
- **Depende de:** `TLG-T2b`
- **Operação do modelo:** `OP-3`
  - OP-3: O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo.
  - precisa de: stream de dados — Quem implementa recebe o loop do condutor — as transições que ele atravessa a cada tarefa e o que ele tem em mãos em cada uma —, a função do kit que gera a linha a partir do evento de cada transição, e o arquivo de progresso onde essa função grava. A ferramenta que roda os agentes e o painel que mostra o arquivo ficam como estão.; tarefa — Quem implementa lê dela o que preenche as mensagens: qual tarefa, o título dela, qual passo e o que o passo pede. Nada nela muda.; mente do agente — Quem implementa usa a intenção que o condutor já tem em mãos — o que ele pediu ao agente e o que o agente devolveu — como campo do evento que a função recebe. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo.
- **Camada e fronteira:** kit — `.claude/tools/progresso_hook.py` **reescrito** (mantém `capturar` e as três constantes de `TLG-T3a`, a trava e a barreira `agent_type`; perde transcript, marcador, inícios e cursor), `tests/test_progresso_hook.py` **reescrito** (os três `TF-CAP` ficam, os nove `TF-PROG` saem, entram dezenove `TF-GER`), uma entrada nova no `PreToolUse` e uma no `UserPromptSubmit` do alvo `projeto` de `.claude/projecoes.json` (`DTG-39`) e a materialização em `.claude/settings.json` **só** por `python .claude/tools/materializar.py apply --alvo projeto`. O script usa só biblioteca padrão (`json`, `os`, `re`, `sys`, `time`, `pathlib`), não importa instrumento do kit e não chama ferramenta nenhuma: lê `docs/plans/P-*.md`, `docs/DIARIO_DE_OBRAS.md` e `.claude/estado/tarefa-corrente.json` do disco. O `TF-GER-18` lê `.claude/skills/scrum-master/SKILL.md` (a cópia legível que `TLG-T2b` entregou) sem editá-la. Nenhuma skill, agente, `README.md`, `.gitignore`, `materializar.py`, `ocupacao.py` muda; o settings global fica intocado (`I-1`).
- **Domínio:** *evento de transição* = disparo de `PreToolUse`, `PostToolUse`, `UserPromptSubmit` ou `Stop` na sessão principal (payload sem `agent_type`) que casa uma linha da tabela `FRASES` abaixo; *frase gerada* = o template da tabela com as lacunas `<…>` substituídas; *arquivo de progresso* = `.claude/estado/progresso.txt`, uma frase por linha, UTF-8, `\n`; *estado próprio* = `.claude/estado/progresso-estado.json`, objeto com as chaves `sessao`, `aberta`, `encerrada`, `tarefa`, `titulo`, `objetivo`, `titulo_plano`, `tarefa_fechada`, `titulo_fechada`, `pendentes` (objeto `agentId → subagent_type`, `DTG-39`), reiniciado para `{"sessao": <session_id>}` quando `session_id` do payload difere de `sessao`; *tarefa corrente* = `tarefa` do estado próprio, senão `tarefa` de `.claude/estado/tarefa-corrente.json`, senão nenhuma (`DTG-33` (iv)); *corpus da agregação* = `docs/plans/P-*.md` em ordem alfabética e depois `docs/DIARIO_DE_OBRAS.md` (`DTG-33` (ii)); *captura* = `.claude/estado/progresso-captura.jsonl` de `TLG-T3a`, lida no passo 1 e apagada no passo 9. Todos os arquivos de `.claude/estado/` são ignorados pelo git (`F-22`, `F-31`).
- **Arquivos-alvo:**
  - `.claude/tools/progresso_hook.py:1` — reescrito inteiro; a docstring nova de no máximo seis linhas diz: ganchos PreToolUse, PostToolUse, UserPromptSubmit e Stop do P-0748 (OP-3); gera em .claude/estado/progresso.txt uma frase por evento de transição do loop, com o título da tarefa no lugar da sigla; falha aberta, nunca imprime; captura de payload opcional (flag progresso-captura.on)
  - `tests/test_progresso_hook.py:1` — reescrito inteiro; mantém a carga por importlib.util.spec_from_file_location("progresso_hook", ...) e _ROOT = Path(__file__).resolve().parents[1]
  - `.claude/projecoes.json:14` — a linha que contém tools/ocupacao.py (única no arquivo); o objeto novo entra depois do objeto que a contém, dentro do mesmo array PreToolUse
  - `.claude/projecoes.json:55` — a linha que contém tools/backlog_hook.py (única no arquivo); o objeto novo entra depois do objeto que a contém, dentro do mesmo array UserPromptSubmit (`DTG-39`)
  - `.claude/settings.json` — materializado pelo passo 8, nunca editado à mão
- **Contratos/classes:** estrutura de `.claude/tools/progresso_hook.py` (assinaturas, não só nomes):

  ```python
  KIT = Path(__file__).resolve().parents[1]          # a pasta .claude/
  REPO = KIT.parent
  PAPEIS = {"pantonic-executor": "executor", "pantonic-reviewer": "revisor",
            "pantonic-consultant": "consultor", "pantonic-model-designer": "modelador",
            "pantonic-planner": "planejador"}
  ESTADO_ARQ = "progresso-estado.json"
  CAPTURA_FLAG = "progresso-captura.on"              # de TLG-T3a, inalteradas
  CAPTURA_ARQ = "progresso-captura.jsonl"
  CAPTURA_TETO_BYTES = 1_000_000
  FRASES: dict[str, str]                              # literal em "Texto novo, literal", 23 chaves

  def capturar(payload: dict, estado: Path) -> None: ...          # de TLG-T3a, inalterada
  def texto_da_resposta(resp) -> str: ...
  def localizar_card(id_tarefa: str, raiz: Path) -> tuple[str, str, str]: ...   # (titulo, objetivo, titulo_plano)
  def frase(id_frase: str, lacunas: dict[str, str]) -> str: ...
  def tarefa_corrente(estado_loop: dict, estado: Path, raiz: Path) -> tuple[str, str, str]: ...  # (id, titulo, objetivo)
  def de_volta(sub: str, texto: str, titulo: str) -> list[str]: ...   # a classificação da regra 5, comum à 5b (DTG-39)
  def evento(payload: dict, estado_loop: dict, estado: Path, raiz: Path) -> tuple[list[str], dict]: ...
  def main(argv: list[str] | None = None, entrada: str | None = None,
           estado: Path | None = None, raiz: Path | None = None, espera: float = 2.0) -> int: ...

  if __name__ == "__main__":
      sys.exit(main())
  ```

  Semântica fechada:
  - `texto_da_resposta(resp)`: `None` → `""`; `str` → ele mesmo; `dict` → o valor da primeira chave presente, nesta ordem, entre `stdout`, `output`, `text`, `result`, `response`, se o valor for `str`; senão, com `content` lista, os `bloco["text"]` de cada `dict` com `bloco.get("type") == "text"`, unidos por `"\n"`; senão `json.dumps(resp, ensure_ascii=False, default=str)`; `list` → tratada como `content`; outro tipo → `str(resp)`.
  - `localizar_card(id_tarefa, raiz)`: `arquivos = sorted((raiz / "docs" / "plans").glob("P-*.md")) + [raiz / "docs" / "DIARIO_DE_OBRAS.md"]`, pulando os que não existem; para cada um, lê as linhas em UTF-8 (`errors="replace"`) e procura a primeira que casa `re.compile(r"^### " + re.escape(id_tarefa) + r" — (.+?) \[")`; achada: `titulo = m.group(1).strip()`; `objetivo` = a primeira linha seguinte que começa por `- **Objetivo:**`, antes da próxima que começa por `### `, sem o rótulo e sem espaços nas pontas, e, se passar de 240 caracteres, os 239 primeiros mais `…`; `titulo_plano` = se o nome do arquivo começa por `P-`, a linha 1; senão a última linha antes do cabeçalho que começa por `## `; em ambos, aplicar `re.match(r"^#+\s*(?:\S+\s+—\s+)?(.*)$", linha).group(1).strip()`. Não achado em nenhum arquivo → `(id_tarefa, "", "")`.
  - `frase(id_frase, lacunas)`: `s = FRASES[id_frase]`; para cada `(k, v)` em `lacunas.items()`, `s = s.replace(k, v)` — as chaves são os placeholders literais (`"<título>"`, `"<título do plano>"`, `"<objetivo>"`, `"<pendência>"`, `"<motivo>"`, `"<razão>"`, `"<veredito>"`, `"<percentual>"`, `"<bloqueante>"`, `"<rota>"`, `"<frase>"`, `"<estado>"`, `"<título fechada>"`, `"<ato>"`, `"<papel>"`, `"<primeira linha>"`); devolve `s`. Título de tarefa e de plano entram **sem** aspas no valor: as aspas estão no template.
  - `tarefa_corrente(estado_loop, estado, raiz)`: se `estado_loop.get("tarefa")` → `(tarefa, titulo, objetivo)` do estado; senão lê `estado / "tarefa-corrente.json"` (UTF-8; ausente, inválido ou sem `tarefa` `str` → nenhuma) e devolve `(id, *localizar_card(id, raiz)[:2])`; nenhuma → `("", "(tarefa não identificada)", "")`.
  - `evento(payload, estado_loop, estado, raiz)`: `sid = payload.get("session_id")`; se `estado_loop.get("sessao") != sid` → `estado_loop = {"sessao": sid}`. `ev = payload.get("hook_event_name")`; `tool = payload.get("tool_name")`; `ti = payload.get("tool_input") if isinstance(payload.get("tool_input"), dict) else {}`; `cmd = str(ti.get("command", ""))`; `sub = str(ti.get("subagent_type", ""))`; `resp = texto_da_resposta(payload.get("tool_response"))`; `linhas = []`. Aplicar **a primeira** regra que casa:
    1. `ev == "PostToolUse" and tool == "Bash" and "backlog.py next" in cmd`: `m = re.search(r"^=== PRÓXIMA TAREFA: (\S+) — (.+?) \[", resp, re.M)`. Com `m`: `tid, titulo = m.group(1), m.group(2).strip()`; `_, objetivo, titulo_plano = localizar_card(tid, raiz)`; se `not estado_loop.get("aberta")` e `titulo_plano` → `M-0`; se `estado_loop.get("tarefa_fechada")` → `M-11` com `<título fechada>` = `titulo_fechada` do estado, e apagar `tarefa_fechada` e `titulo_fechada`; sempre `M-1`; estado ← `tarefa=tid, titulo, objetivo, titulo_plano, aberta=True, encerrada=False`. Sem `m` e com `"nada delegável" in resp`: `M-12` se `tarefa_fechada` (e apagar as duas chaves), senão `M-12b`. Sem nenhum dos dois: nada.
    2. `ev == "PreToolUse" and tool == "Bash"` e `m = re.search(r"backlog\.py status (\S+) (\S+)", cmd)`: `tid, st = m.group(1), m.group(2)`; `titulo` = `titulo` do estado se `estado_loop.get("tarefa") == tid`, senão `localizar_card(tid, raiz)[0]`; `st == "in-progress"` → `M-2`; `st in ("done", "blocked", "cancelled")` → `M-10` com `<estado>` = `st`, e estado ← `tarefa_fechada=tid, titulo_fechada=titulo`; outro `st` → nada.
    3. `ev == "PreToolUse" and tool == "Bash" and "review_evidence.py" in cmd`: `m = re.search(r"--tarefa (\S+)", cmd)`; sem `m` → nada; `titulo` como na regra 2; `"--atribuir" in cmd` → `M-13`, senão `M-5`.
    4. `ev == "PreToolUse" and tool == "Agent" and sub in PAPEIS`: `_, titulo, objetivo = tarefa_corrente(...)`; `executor` → `M-3` com `<objetivo>` se `objetivo`, senão `M-3b`; `revisor` → `M-6`; `consultor` → `M-8`; `modelador` → `m = re.search(r"Ato:\s*`?(autoria|emenda|conflito)", str(ti.get("prompt", "")))` → `M-14` com `<ato>` = `m.group(1)`, senão `M-14b`; `planejador` → `M-15`.
    5. `ev == "PostToolUse" and tool == "Agent" and sub in PAPEIS`: `r = payload.get("tool_response")`; se `isinstance(r, dict) and r.get("handback") == "send" and isinstance(r.get("agentId"), str)` → `estado_loop.setdefault("pendentes", {})[r["agentId"]] = sub` e **nenhuma linha** (a volta sai na regra 5b, `DTG-39`); senão `_, titulo, _ = tarefa_corrente(...)`, e `linhas = de_volta(sub, resp, titulo)`.
    5b. `ev == "UserPromptSubmit"`: `p = str(payload.get("prompt") or "")`; `m = re.match(r'<agent-message from="([^"]+)">', p)`; sem `m` → nada; `sub = estado_loop.get("pendentes", {}).pop(m.group(1), "")`; `sub not in PAPEIS` → nada; `corpo` = o texto depois da primeira ocorrência de `The report follows:` (ausente → `""`), cortado antes da primeira `</agent-message>`; `_, titulo, _ = tarefa_corrente(...)`; `linhas = de_volta(sub, corpo, titulo)`.
    `de_volta(sub, texto, titulo)` (comum a 5 e 5b): `papel = PAPEIS[sub]`; `l1` = primeira linha não vazia de `texto`, sem espaços nas pontas (`""` se não houver); `executor`: `re.match(r"^(\S+) review(?:\s+pendencia=(.*))?$", l1)` → `M-4` com `<pendência>` = grupo 2 sem espaços nas pontas, ou `sem pendência` se `None` ou vazio; `re.match(r"^(\S+) blocked motivo=(\S+)\s*(.*)$", l1)` → `M-4b`; `revisor`: `re.match(r"^(\S+) (\S+) (\d+) bloqueante=(.*)$", l1)` → `M-7`; `consultor`: `mr = re.search(r"rota=(\S+)", texto)` e `me = re.search(r"estrategico=(.*)", texto)` → `M-9b` se `mr and me` (`<frase>` = `me.group(1).strip()`), `M-9` se só `mr`; tudo o que não casou acima (inclusive `modelador` e `planejador`) → `M-16` com `<papel>` = `papel` e `<primeira linha>` = `l1` cortada em 160 caracteres mais `…` quando maior, ou `(sem texto)` se vazia.
    6. `ev == "Stop"`: se `estado_loop.get("aberta") and not estado_loop.get("encerrada")` → `M-17`, estado ← `encerrada=True`; senão nada.
    7. Qualquer outro caso → nada. Devolve `(linhas, estado_loop)`.
  - `main(...)`: tudo dentro de `try`/`except Exception: return 0`; **nunca imprime**, sai sempre `0` (`I-11`). (1) `raw = entrada` ou `sys.stdin.buffer.read().decode("utf-8", errors="replace")`; `payload = json.loads(raw)`; não `dict` → `0`. (2) `payload.get("agent_type")` não vazio → `0`, sem criar nada (`DTG-22`). (3) `estado = estado or KIT / "estado"`; `raiz = raiz or REPO`; `estado.mkdir(parents=True, exist_ok=True)`. (4) `capturar(payload, estado)`. (5) Trava `estado / "progresso.lock"`, exatamente como hoje (`os.open` com `O_CREAT | O_EXCL`, prazo `espera`, trava velha de mais de 30 s removida; prazo vencido → `0`). (6) Sob a trava, num `try` cujo `finally` faz `trava.unlink(missing_ok=True)`: `estado_loop` = `json.loads` de `estado / ESTADO_ARQ` (ausente, inválido ou não `dict` → `{}`); `linhas, estado_loop = evento(payload, estado_loop, estado, raiz)`; com `linhas`, abrir `estado / "progresso.txt"` em modo `"a"`, `encoding="utf-8"`, `newline="\n"`, e escrever cada linha seguida de `"\n"`; gravar `estado_loop` com `json.dumps(estado_loop, ensure_ascii=False)` em UTF-8 em `estado / ESTADO_ARQ`.
- **Texto novo, literal** — (a) o dicionário `FRASES`, cópia caractere a caractere da coluna *frase gerada* da `### 4.1` do plano (versão 3; `TLG-T2b` levou a mesma tabela à skill, e o `TF-GER-18` confere os dois):

  ```python
  FRASES = {
      'M-0': 'Abrindo a janela do plano "<título do plano>".',
      'M-1': 'Tarefa "<título>". Passo: conferir os gates e preparar o despacho.',
      'M-2': 'Tarefa "<título>": gates aprovados; vou materializar in-progress e gravar o ponto de partida.',
      'M-3': 'Agente executor recebe a tarefa "<título>" e vai executar: <objetivo>',
      'M-3b': 'Agente executor recebe a tarefa "<título>" e vai executar o card.',
      'M-4': 'Agente executor devolveu a tarefa "<título>": review — <pendência>.',
      'M-4b': 'Agente executor devolveu a tarefa "<título>": blocked — motivo <motivo>: <razão>.',
      'M-5': 'Tarefa "<título>": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.',
      'M-6': 'Agente revisor recebe a tarefa "<título>" e vai confrontar a entrega com o card.',
      'M-7': 'Agente revisor devolveu a tarefa "<título>": <veredito> <percentual>%, bloqueante <bloqueante>.',
      'M-8': 'Agente consultor recebe a parada da tarefa "<título>" e vai triar.',
      'M-9': 'Agente consultor devolveu a tarefa "<título>": rota <rota>.',
      'M-9b': 'Agente consultor devolveu a tarefa "<título>": rota <rota>; estratégico: <frase>.',
      'M-10': 'Scrum master vai fechar a tarefa "<título>" como <estado>: registrar estado, RDO e telemetria, e selecionar a próxima.',
      'M-11': 'Scrum master concluiu a tarefa "<título fechada>" e vai pegar a tarefa "<título>".',
      'M-12': 'Scrum master concluiu a tarefa "<título fechada>"; nada delegável na fila. Encerrando a janela com o relatório.',
      'M-12b': 'Scrum master não encontrou tarefa delegável na fila. Encerrando a janela com o relatório.',
      'M-13': 'Tarefa "<título>": vou medir a que arquivo a pendência é atribuível.',
      'M-14': 'Agente modelador recebe a tarefa "<título>" e vai fazer <ato> no modelo.',
      'M-14b': 'Agente modelador recebe a tarefa "<título>" e vai atualizar o modelo.',
      'M-15': 'Agente planejador recebe a tarefa "<título>" e vai replanejar.',
      'M-16': 'Agente <papel> devolveu a tarefa "<título>": <primeira linha>.',
      'M-17': 'Scrum master encerrou a janela; o relatório está na extensão.',
  }
  ```

  (b) O objeto a inserir em `.claude/projecoes.json`, alvo `projeto`, dentro do array `"PreToolUse": [`, imediatamente depois do objeto que contém `tools/ocupacao.py` — na prática, as cinco linhas hoje exatamente assim (recuos de 18, 16, 14, 12 e 10 espaços):

  ```
                    "command": "python {KIT_ROOT}/tools/ocupacao.py"
                  }
                ]
              }
            ],
  ```

  passam a ser estas (o objeto novo entre a chave que fecha o de `ocupacao.py`, agora com vírgula, e o `],` que fecha o array):

  ```
                    "command": "python {KIT_ROOT}/tools/ocupacao.py"
                  }
                ]
              },
              {
                "matcher": ".*",
                "hooks": [
                  {
                    "type": "command",
                    "command": "python {KIT_ROOT}/tools/progresso_hook.py"
                  }
                ]
              }
            ],
  ```

  (Os dois blocos acima têm dois espaços de recuo a mais que o arquivo, por estarem neste card.)

  (c) O objeto a inserir em `.claude/projecoes.json`, alvo `projeto`, dentro do array `"UserPromptSubmit": [`, imediatamente depois do objeto que contém `tools/backlog_hook.py` (`DTG-39`) — as cinco linhas hoje exatamente assim (recuos de 18, 16, 14, 12 e 10 espaços no arquivo):

  ```
                    "command": "python {KIT_ROOT}/tools/backlog_hook.py"
                  }
                ]
              }
            ]
  ```

  passam a ser estas (sem `matcher`, como o objeto vizinho):

  ```
                    "command": "python {KIT_ROOT}/tools/backlog_hook.py"
                  }
                ]
              },
              {
                "hooks": [
                  {
                    "type": "command",
                    "command": "python {KIT_ROOT}/tools/progresso_hook.py"
                  }
                ]
              }
            ]
  ```

  (Mesma convenção: dois espaços de recuo a mais que o arquivo.)
- **Passos:**
  1. **Leitura da captura (`DTG-32`).** Rodar, em bloco cercado por conter aspas e barra invertida:

     ```
     python -c "import json;rs=[json.loads(l) for l in open('.claude/estado/progresso-captura.jsonl',encoding='utf-8') if l.strip()];print(sorted({(r['evento'],r['tool'],r['response_tipo'],tuple(r['response_chaves'] or [])) for r in rs}))"
     ```

     Guardar a saída para a linha de retorno. Aplicar as contingências 1 a 3. Conferir só as **chaves** das tuplas (o campo `response` da captura é cortado em 2000 caracteres e não passa em `json.loads` — não lê-lo): a tupla `('PostToolUse', 'Agent', 'dict', …)` contém `'agentId'`, `'agentType'`, `'content'` e `'handback'`; toda tupla `('PostToolUse', 'Bash', 'dict', …)` contém `'stdout'` (forma (b)). A forma do valor já foi medida pelo consultor no transcript (`DTG-39`) e está literal no `TF-GER-15`: nada da captura é copiado para fixture.
  2. Rodar `python -m pytest tests/test_progresso_hook.py -q` e anotar (contingência 7).
  3. Reescrever `.claude/tools/progresso_hook.py` com a estrutura e a semântica de `Contratos/classes` e o `FRASES` de `Texto novo, literal` (a), mantendo `capturar` e as três constantes de `TLG-T3a` sem mudança.
  4. Reescrever `tests/test_progresso_hook.py`: manter os três `TF-CAP`, remover os nove `TF-PROG`, escrever os dezenove `TF-GER` de `Testes`. Fixtures comuns: `estado = tmp_path / "estado"`; `raiz = tmp_path`, com `raiz / "docs" / "plans" / "P-9999-teste.md"` contendo as linhas `# P-9999 — Plano de teste`, uma linha em branco, `### TLG-T9 — Um título de teste [Sonnet · classe redacao]`, `- **Objetivo:** Fazer x.`, `### TLG-T10 — Outro título [Sonnet · classe redacao]`, `- **Objetivo:** Fazer y.`; e `raiz / "docs" / "DIARIO_DE_OBRAS.md"` contendo `# Diário de Obras — Teste`, `## TK-99 — Tíquete de teste`, `### TK-99a — Card do tíquete [Sonnet · classe mecanica]`, `- **Objetivo:** Fazer z.`. Chamada: `main(entrada=json.dumps(payload), estado=estado, raiz=raiz)`. Todo payload leva `"session_id": "s1"` e `"transcript_path": str(tmp_path / "t.jsonl")`, salvo onde o TF diz outra coisa. `progresso()` = conteúdo de `estado / "progresso.txt"` dividido em linhas.
  5. Inserir em `.claude/projecoes.json` o objeto de `Texto novo, literal` (b) e o de (c).
  6. Rodar `python .claude/tools/materializar.py check --alvo projeto`; depois `python .claude/tools/materializar.py drift --alvo projeto` (esperado: exit diferente de `0`); depois `python .claude/tools/materializar.py apply --alvo projeto`; depois `python .claude/tools/materializar.py drift --alvo projeto` (esperado: exit `0`).
  7. Rodar a Verificação 1 a 8.
  8. Apagar `.claude/estado/progresso-cursor.json` (obsoleto: `Remove-Item -Path .claude/estado/progresso-cursor.json -ErrorAction SilentlyContinue`).
  9. Apagar o flag e a captura: `Remove-Item -Path .claude/estado/progresso-captura.on, .claude/estado/progresso-captura.jsonl -ErrorAction SilentlyContinue`. Rodar a Verificação 9.
- **Restrições desta tarefa:** `I-11` — o gancho nunca imprime, sai sempre `0`, também no `PreToolUse` (stdout com JSON ou exit `2` mudariam o comportamento do harness); não importa `rdo`, `backlog`, `telemetria`, `modelo`, `ocupacao` nem `materializar` (Verificação 5). `DTG-22` — a barreira `agent_type` fica antes de qualquer leitura ou gravação. `DTG-33` — o corpus da agregação é só o do `Domínio`; título e título do plano entram nos templates entre aspas duplas já presentes no template, nunca acrescentadas pelo código. `DTG-36` — `FRASES` é cópia: o executor não reescreve frase nenhuma. `DTG-38` — `.claude/settings.json` muda só pelo `apply`. `I-7` — o total de `pytest tests/` não cai. `I-12` — nenhum template contém `<ID>` (`TF-GER-18`). Estrutural: `capturar` e as três constantes de `TLG-T3a` ficam idênticas.
- **Não fazer:** não editar `.claude/settings.json` à mão; não editar `.gitignore`, `materializar.py`, `ocupacao.py`, nenhuma skill (a remoção dos bullets `**Narra:**` é `TLG-T4a`; a tabela é `TLG-T2b`), nenhum agente, o `README.md`; não tocar o alvo `usuario` do `projecoes.json` nem os eventos `PostToolUse`, `Stop` e `SubagentStop`, nem o objeto de `backlog_hook.py` no `UserPromptSubmit` (só se acrescenta o de (c)); não mudar o matcher `.*` (`DTG-31`); não fazer o gancho imprimir, devolver JSON ou sair diferente de `0`; não ler o transcript nem manter cursor; não gravar timestamp, sigla entre parênteses ou qualquer texto além da frase no arquivo de progresso; não inventar frase para caso que não casa nenhuma regra (o caso é "nada", ou `M-16` quando a regra 5 o diz); não chamar `subprocess`, `git` ou instrumento do kit de dentro do gancho; não pedir ao dono para reabrir a sessão (`AE-6`); não deixar o flag nem a captura no disco ao fim.
- **Contingências:**
  1. se `.claude/estado/progresso-captura.jsonl` não existe, ou o comando do passo 1 termina com erro → parar e sinalizar `blocked` razão `premissa`, devolvendo `Test-Path .claude/estado/progresso-captura.jsonl` e `Test-Path .claude/estado/progresso-captura.on` (`TLG-T3a` não mediu: o flag não estava ligado na sessão principal);
  2. se a saída do passo 1 não contém nenhuma tupla que comece por `('PostToolUse', 'Agent'` → parar e sinalizar `blocked` razão `premissa`, devolvendo a saída inteira do passo 1;
  3. se a tupla `('PostToolUse', 'Agent', 'dict', …)` não contém as quatro chaves `agentId`, `agentType`, `content`, `handback`, ou alguma tupla `('PostToolUse', 'Bash', 'dict', …)` não contém `stdout` → parar e sinalizar `blocked` razão `premissa`, devolvendo a saída inteira do passo 1 (a forma do **valor** não é critério desta contingência: está medida em `DTG-39`);
  4. se `(Select-String -SimpleMatch -Path .claude/projecoes.json -Pattern "tools/ocupacao.py" | Measure-Object).Count` ou `(Select-String -SimpleMatch -Path .claude/projecoes.json -Pattern "tools/backlog_hook.py" | Measure-Object).Count` não for `1` → parar e sinalizar `blocked` razão `premissa`, devolvendo a saída de `grep -n "ocupacao.py\|backlog_hook.py" .claude/projecoes.json`;
  5. se `materializar.py check --alvo projeto` sai diferente de `0`, ou o `drift` **depois** do `apply` sai diferente de `0`, ou a Verificação 4 não dá `4`, `1`, `4` e `1` → parar e sinalizar `blocked` razão `ferramenta`, devolvendo a saída do comando (`DTG-38`);
  6. se o modo de permissão recusa o `materializar.py apply` → parar e sinalizar `blocked` razão `ferramenta` com a linha `apply recusado pelo modo de permissão; o dono roda: python .claude/tools/materializar.py apply --alvo projeto`; o agente não contorna a recusa nem edita o `settings.json` à mão;
  7. se `python -m pytest tests/test_progresso_hook.py -q` antes da edição não sai `12 passed`, ou o comando da Verificação 3 de `TLG-T2b` não imprime `iguais 23 de 23 23` → parar e sinalizar `blocked` razão `dependencia`, devolvendo a linha impressa;
  8. se `python -m pytest tests/ -q` reduz o total por teste **fora** de `tests/test_progresso_hook.py` → parar e sinalizar `blocked` razão `dependencia` com o nome do teste;
  9. se o `drift` **antes** do `apply` sai `0` (o materializador não vê a entrada nova) → seguir com o `apply` e o `drift` seguinte, e devolver `contingência 9 acionada: drift antes do apply saiu 0`; a Verificação 4 decide.
- **Testes:** `tests/test_progresso_hook.py`; fixtures do passo 4. Para cada TF, o valor que a regra concorrente daria sobre a mesma fixture vem entre parênteses. `P = lambda **k: {"session_id": "s1", "transcript_path": str(tmp_path / "t.jsonl"), **k}`.
  - `TF-GER-1` — `texto_da_resposta`: `"a\nb"`, `{"stdout": "a\nb"}`, `{"content": [{"type": "text", "text": "a"}, {"type": "text", "text": "b"}]}` e `[{"type": "text", "text": "a"}, {"type": "text", "text": "b"}]` devolvem todos `"a\nb"`; `None` devolve `""`; `{"x": 1}` devolve `'{"x": 1}'` (só `stdout`: `""` para a forma `content`).
  - `TF-GER-2` — tarefa escolhida, primeira da sessão: `P(hook_event_name="PostToolUse", tool_name="Bash", tool_input={"command": "python .claude/tools/backlog.py next"}, tool_response={"stdout": "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n- **Objetivo:** Fazer x.\n"})`; `progresso()` == `['Abrindo a janela do plano "Plano de teste".', 'Tarefa "Um título de teste". Passo: conferir os gates e preparar o despacho.']`; o estado tem `tarefa == "TLG-T9"`, `titulo == "Um título de teste"`, `objetivo == "Fazer x."`, `aberta is True`. Segunda chamada igual, na mesma sessão: `progresso()` tem 3 linhas e a terceira é a `M-1` (sem o flag `aberta`: 4 linhas).
  - `TF-GER-3` — fila vazia: `tool_response={"stdout": "nada delegável\n"}` sem estado → uma linha `Scrum master não encontrou tarefa delegável na fila. Encerrando a janela com o relatório.`; com o estado gravado previamente como `{"sessao": "s1", "aberta": true, "tarefa_fechada": "TLG-T9", "titulo_fechada": "Um título de teste"}` → `Scrum master concluiu a tarefa "Um título de teste"; nada delegável na fila. Encerrando a janela com o relatório.` e o estado não tem mais `tarefa_fechada` (sem a regra: nenhuma linha).
  - `TF-GER-4` — estado mudado: depois do `next` do `TF-GER-2`, `P(hook_event_name="PreToolUse", tool_name="Bash", tool_input={"command": "python .claude/tools/backlog.py status TLG-T9 in-progress"})` → última linha `Tarefa "Um título de teste": gates aprovados; vou materializar in-progress e gravar o ponto de partida.`; `… status TLG-T9 review` → nenhuma linha nova; `… status TLG-T9 done` → última linha `Scrum master vai fechar a tarefa "Um título de teste" como done: registrar estado, RDO e telemetria, e selecionar a próxima.` e o estado tem `tarefa_fechada == "TLG-T9"`; o mesmo comando `done` como `PostToolUse` → nenhuma linha nova (sem distinguir o gancho: linha duplicada).
  - `TF-GER-5` — agente despachado: depois do `next`, `P(hook_event_name="PreToolUse", tool_name="Agent", tool_input={"subagent_type": "pantonic-executor", "prompt": "…"})` → `Agente executor recebe a tarefa "Um título de teste" e vai executar: Fazer x.`; `pantonic-reviewer` → `Agente revisor recebe a tarefa "Um título de teste" e vai confrontar a entrega com o card.`; `pantonic-consultant` → `Agente consultor recebe a parada da tarefa "Um título de teste" e vai triar.`; `pantonic-model-designer` com `prompt` contendo `Ato: emenda` → `Agente modelador recebe a tarefa "Um título de teste" e vai fazer emenda no modelo.`; o mesmo sem `Ato:` → `Agente modelador recebe a tarefa "Um título de teste" e vai atualizar o modelo.`; `pantonic-planner` → `Agente planejador recebe a tarefa "Um título de teste" e vai replanejar.`; `pantonic-scout` → nenhuma linha (sem o filtro `PAPEIS`: uma linha).
  - `TF-GER-6` — agente de volta, executor: `P(hook_event_name="PostToolUse", tool_name="Agent", tool_input={"subagent_type": "pantonic-executor"}, tool_response={"content": [{"type": "text", "text": "TLG-T9 review pendencia=uma coisa\nresto"}]})` → `Agente executor devolveu a tarefa "Um título de teste": review — uma coisa.`; texto `TLG-T9 review` → `…: review — sem pendência.`; texto `TLG-T9 blocked motivo=premissa falta y` → `…: blocked — motivo premissa: falta y.` (sem a gramática: as três caem em `M-16`).
  - `TF-GER-7` — agente de volta, revisor: texto `TLG-T9 aprovado 100 bloqueante=nenhuma` → `Agente revisor devolveu a tarefa "Um título de teste": aprovado 100%, bloqueante nenhuma.`
  - `TF-GER-8` — agente de volta, consultor: texto `rota=resolve\nreparo…` → `Agente consultor devolveu a tarefa "Um título de teste": rota resolve.`; texto `rota=planejador\nestrategico=muda o escopo` → `…: rota planejador; estratégico: muda o escopo.` (sem `M-9b`: a segunda cai em `M-9` e perde a frase).
  - `TF-GER-9` — forma genérica: executor devolvendo `texto livre sem forma` → `Agente executor devolveu a tarefa "Um título de teste": texto livre sem forma.`; modelador devolvendo `Plano: docs/plans/x.md\nAto: emenda` → `Agente modelador devolveu a tarefa "Um título de teste": Plano: docs/plans/x.md.`; primeira linha de 200 caracteres `a` → a frase contém 160 `a` seguidos de `…`; resposta vazia → `…: (sem texto).` (sem o corte: 200 caracteres).
  - `TF-GER-10` — evidência: `P(hook_event_name="PreToolUse", tool_name="Bash", tool_input={"command": "python .claude/tools/review_evidence.py --plano docs/plans/P-9999-teste.md --tarefa TLG-T9 --desde abc --out x.md"})` → `Tarefa "Um título de teste": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.`; o mesmo comando com ` --atribuir` no fim → `Tarefa "Um título de teste": vou medir a que arquivo a pendência é atribuível.` (sem distinguir `--atribuir`: `M-5` duas vezes).
  - `TF-GER-11` — tarefa escolhida depois de uma fechada: estado `{"sessao": "s1", "aberta": true, "tarefa_fechada": "TLG-T9", "titulo_fechada": "Um título de teste"}`, depois o `next` devolvendo `TLG-T10 — Outro título` → exatamente duas linhas: `Scrum master concluiu a tarefa "Um título de teste" e vai pegar a tarefa "Outro título".` e `Tarefa "Outro título". Passo: conferir os gates e preparar o despacho.`; sem `M-0` (sem `aberta`: três linhas).
  - `TF-GER-12` — `Stop`: estado `{"sessao": "s1", "aberta": true}` e `P(hook_event_name="Stop")` → `Scrum master encerrou a janela; o relatório está na extensão.` e o estado tem `encerrada is True`; segundo `Stop` → nenhuma linha nova; `Stop` com estado vazio → `progresso.txt` não existe (sem o flag `aberta`: uma linha em sessão sem loop).
  - `TF-GER-13` — barreiras e falha aberta, cada caso com `main(...) == 0` e stdout vazio (`capsys`): `agent_type` = `pantonic-executor` num payload de `next` válido → nem `progresso.txt` nem `progresso-estado.json`, pasta `estado` não criada; entrada `"isto não é json"`; `tool_name` = `Read`; `Bash` com `command` = `git status` → `progresso.txt` não existe nos quatro (sem a barreira: uma linha no primeiro).
  - `TF-GER-14` — agregação: `status TLG-T77 in-progress` sem card no corpus e sem estado → `Tarefa "TLG-T77": gates aprovados; …` (sem o fallback: exceção ou linha vazia); estado vazio e `estado / "tarefa-corrente.json"` = `{"tarefa": "TLG-T9"}` com despacho do executor → `Agente executor recebe a tarefa "Um título de teste" e vai executar: Fazer x.`; `next` devolvendo `TK-99a — Card do tíquete` → `Abrindo a janela do plano "Tíquete de teste".` e `Tarefa "Card do tíquete". Passo: …`; card com objetivo de 300 caracteres → `<objetivo>` de 240 caracteres terminando em `…`.
  - `TF-GER-15` — amostra real em modo hand-back (`DTG-39`, formas medidas no transcript): depois do `next` do `TF-GER-2`, `P(hook_event_name="PostToolUse", tool_name="Agent", tool_input={"subagent_type": "pantonic-executor", "prompt": "…"}, tool_response={"status": "completed", "agentId": "ab2f2cd682dae49db", "agentType": "pantonic-executor", "handback": "send", "content": [{"type": "text", "text": "This agent's report was delivered to you as a message from \"ab2f2cd682dae49db\" (its SubagentHandback call). Read it there; it is not repeated here.\n"}]})` → nenhuma linha nova e o estado tem `pendentes == {"ab2f2cd682dae49db": "pantonic-executor"}`; em seguida `P(hook_event_name="UserPromptSubmit", prompt="<agent-message from=\"ab2f2cd682dae49db\">\n[Subagent hand-back] The text below is the final report of a subagent this session delegated to. The report follows:\n  TLG-T9 blocked motivo=premissa falta y\n  segunda linha\n</agent-message>")` → última linha `Agente executor devolveu a tarefa "Um título de teste": blocked — motivo premissa: falta y.` e `pendentes` vazio; o mesmo `UserPromptSubmit` repetido → nenhuma linha nova (sem o desvio: a primeira chamada grava `M-16` com o ponteiro *"This agent's report was delivered…"* e o relatório nunca vira linha).
  - `TF-GER-19` — `UserPromptSubmit` sem volta pendente: `prompt="rode o próximo passo"` → nenhuma linha; `<agent-message from="xyz">…The report follows:\n  TLG-T9 review\n</agent-message>` com `pendentes` vazio → nenhuma linha; revisor em hand-back (`pendentes = {"r1": "pantonic-reviewer"}`, relatório `TLG-T9 aprovado 100 bloqueante=nenhuma`) → `Agente revisor devolveu a tarefa "Um título de teste": aprovado 100%, bloqueante nenhuma.`; consultor em hand-back (`{"c1": "pantonic-consultant"}`, relatório `rota=planejador\n  estrategico=muda o escopo`) → `…: rota planejador; estratégico: muda o escopo.` (sem o filtro por id pendente: linha no prompt do dono ou de agente desconhecido).
  - `TF-GER-16` — sessão nova: estado `{"sessao": "s0", "aberta": true, "tarefa": "TLG-T9"}` e `next` com `session_id` `s1` → a primeira linha é `Abrindo a janela do plano "Plano de teste".` e o estado tem `sessao == "s1"` (sem reinício: sem `M-0`).
  - `TF-GER-17` — trava: com `estado / "progresso.lock"` recém-criado e `espera=0.2`, o `next` devolve `0` e não grava nada; com a trava 60 s no passado (`os.utime`), grava as duas linhas e a trava não existe ao fim (sem trava: grava no primeiro caso).
  - `TF-GER-18` — residência: `set(FRASES)` tem 23 chaves; nenhum valor contém `<ID>`; e, lendo `_ROOT / ".claude" / "skills" / "scrum-master" / "SKILL.md"`, para cada linha que casa `^\| `(M-\d+b?)` \| [^|]* \| `([^`]*)` \|`, `FRASES[grupo 1] == grupo 2` — 23 linhas casadas (template divergente ou faltando: falha).

  Suítes: `python -m pytest tests/test_progresso_hook.py -q`; `python -m pytest tests/ -q`.
- **Verificação:**
  1. `python -m pytest tests/test_progresso_hook.py -q` → antes `12 passed` (depois de `TLG-T3a`), depois `22 passed`.
  2. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` = total re-medido no despacho + `10` (referência histórica `289 passed` antes de `TLG-T3a`, `F-33`).
  3. `python .claude/tools/materializar.py check --alvo projeto` → `materializar: OK - manifesto valido.` e exit `0`; `python .claude/tools/materializar.py drift --alvo projeto` **depois** do `apply` → `materializar: OK - sem drift.` e exit `0` (formas medidas em `F-21`).
  4. `(Select-String -SimpleMatch -Path .claude/projecoes.json -Pattern "progresso_hook.py" | Measure-Object).Count` → antes `2` (medido 2026-09-24, `F-25`), depois `4` (`DTG-39`); `(Select-String -SimpleMatch -Path .claude/settings.json -Pattern "ocupacao.py" | Measure-Object).Count` → antes `1` (medido 2026-09-24), depois `1`; `(Select-String -SimpleMatch -Path .claude/settings.json -Pattern "progresso_hook.py" | Measure-Object).Count` → antes `2` (medido 2026-09-24), depois `4`; `(Select-String -SimpleMatch -Path .claude/settings.json -Pattern "backlog_hook.py" | Measure-Object).Count` → antes `1` (medido 2026-09-24 pelo consultor), depois `1`; e `python -c "import json; json.load(open('.claude/settings.json', encoding='utf-8')); print('json ok')"` → `json ok`.
  5. Inspeção estrutural, bloco cercado por conter barra invertida:

     ```
     (Select-String -Path .claude/tools/progresso_hook.py -Pattern "^(from|import) (rdo|backlog|telemetria|modelo|ocupacao|materializar|subprocess)\b" | Measure-Object).Count
     (Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "print(" | Measure-Object).Count
     (Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "MARCADOR" | Measure-Object).Count
     (Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "transcript_path" | Measure-Object).Count
     (Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "def evento(" | Measure-Object).Count
     (Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "def capturar(" | Measure-Object).Count
     ```

     → antes `0`, `0`, `3`, `1`, `0`, `1` (medidos 2026-09-24, com o `def capturar(` de `TLG-T3a`), depois `0`, `0`, `0`, `0`, `1`, `1`.
  6. Contagem das chaves de `FRASES`, bloco cercado por conter aspas:

     ```
     python -c "import importlib.util as u;s=u.spec_from_file_location('h','.claude/tools/progresso_hook.py');m=u.module_from_spec(s);s.loader.exec_module(m);print(len(m.FRASES), sum('<ID>' in v for v in m.FRASES.values()))"
     ```

     → antes termina em `AttributeError: module 'h' has no attribute 'FRASES'` (medido 2026-09-24), depois `23 0`.
  7. `Test-Path .claude/estado/progresso-cursor.json` → antes `True` (medido 2026-09-24), depois do passo 8 `False`.
  8. `Test-Path .claude/estado/progresso-estado.json` → depois de rodar `python .claude/tools/progresso_hook.py` com stdin `{"session_id": "x", "hook_event_name": "Stop"}` (por exemplo `'{"session_id": "x", "hook_event_name": "Stop"}' | python .claude/tools/progresso_hook.py; $LASTEXITCODE`) → `0` no exit, e `True` no `Test-Path`; `progresso.txt` não ganha linha (sessão sem `aberta`): `(Get-Content .claude/estado/progresso.txt | Measure-Object -Line).Lines` igual antes e depois.
  9. `Test-Path .claude/estado/progresso-captura.on` e `Test-Path .claude/estado/progresso-captura.jsonl` → depois do passo 9, `False` e `False`.
- **Pronto quando:**
  - `stream de dados.arquivo de progresso` — *existe e é alimentado pela função do kit a cada transição do loop: guarda uma linha do repertório por transição, na ordem em que o loop as atravessa, gerada a partir do evento e não da memória do agente — nenhuma linha se perde por o condutor ter esquecido a forma —, e nada mais: nenhuma busca, leitura ou saída de comando, e nenhuma chamada feita dentro dos agentes despachados* — Verificação 1, 3, 4 e 5.
  - `stream de dados.repertório de mensagens` — *fechado e embutido na função que gera a linha: uma frase por evento de transição do loop, no molde do exemplo do dono — "Tarefa X, passo Y.", "Agente executor recebe o passo Y e vai executar Z.", "Agente consultor aceitou a entrega." —, em que cada frase diz o que o ato faz, sem termo que o dono não consiga antecipar: a da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit —, e cada lacuna se preenche pelo campo do evento, não pela mão do condutor* — Verificação 1 (`TF-GER-10`, `TF-GER-18`) e 6.
  - `stream de dados.agregação da linha` — *a função troca, ao gerar a linha, o identificador da tarefa pelo título dela e o do plano pelo título do plano, sem gastar nada do agente para isso; a sigla sozinha nunca chega ao dono* — Verificação 1 (`TF-GER-2`, `TF-GER-14`, `TF-GER-18`) e 6.
- **Fora do escopo desta tarefa:** a skill deixar de narrar e a `passagem-de-bastao` (`TLG-T4a`); a tabela da skill (`TLG-T2b`, já entregue); o `README.md` e o painel (`TLG-T5`); a leitura do painel pelo dono (Marco 3, aceite de marco, `I-6`); propagação aos kits derivados (`DTG-8`).

### TLG-T4a — A skill deixa de narrar: a transição chega ao painel pela função [Sonnet · esforço low · classe redacao]
- **Status:** `done` · 2026-09-24
- **Objetivo:** O mantenedor do loop liga cada transição à função: no instante em que o condutor escolhe a tarefa, muda o estado dela, despacha um agente, recebe o que ele devolveu, coleta a evidência ou fecha a tarefa, é a função que recebe o evento e leva a linha ao arquivo de progresso; o condutor deixa de escrever a linha como texto e deixa de precisar lembrar a forma dela, e o que chega ao dono é a transição narrada com o título da tarefa no lugar do identificador.
- **Fundamento:** `DTG-30` (a função recebe o evento nos ganchos), `DTG-36` (`DTG-23` revogada, `I-2`/`I-5` reescritas; `DTG-15` — a `passagem-de-bastao` segue como colateral nomeado), `DTG-37` (roda depois de `TLG-T3b`: a função já gera as linhas), `DTG-28` (aceite por conteúdo), `F-26`, `F-27`, `I-2`, `I-5`, `I-11`.
- **Depende de:** `TLG-T3b`
- **Operação do modelo:** `OP-4`
  - OP-4: O mantenedor do loop liga cada transição à função: no instante em que o condutor escolhe a tarefa, muda o estado dela, despacha um agente, recebe o que ele devolveu, coleta a evidência ou fecha a tarefa, é a função que recebe o evento e leva a linha ao arquivo de progresso; o condutor deixa de escrever a linha como texto e deixa de precisar lembrar a forma dela, e o que chega ao dono é a transição narrada com o título da tarefa no lugar do identificador.
  - precisa de: stream de dados — Quem implementa recebe o loop do condutor — as transições que ele atravessa a cada tarefa e o que ele tem em mãos em cada uma —, a função do kit que gera a linha a partir do evento de cada transição, e o arquivo de progresso onde essa função grava. A ferramenta que roda os agentes e o painel que mostra o arquivo ficam como estão.; tarefa — Quem implementa lê dela o que preenche as mensagens: qual tarefa, o título dela, qual passo e o que o passo pede. Nada nela muda.; mente do agente — Quem implementa usa a intenção que o condutor já tem em mãos — o que ele pediu ao agente e o que o agente devolveu — como campo do evento que a função recebe. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo.
- **Camada e fronteira:** kit — skill `scrum-master` (remoção dos nove bullets `- **Narra:**` dos passos 2 a 10 e troca do último bullet de `## Guardrails`) e skill `passagem-de-bastao` (uma frase nas linhas 11-13). Nenhum agente, instrumento, teste, `README.md` ou configuração. A função que gera as linhas é o `progresso_hook.py` de `TLG-T3b`, já entregue; este card não o edita.
- **Domínio:** *ligar a transição à função* = a skill deixa de mandar o condutor escrever a linha e passa a dizer que a linha é gerada pelo gancho no evento (`I-2`, `I-5`); o condutor continua fazendo exatamente os mesmos atos (`backlog.py next`, `status`, despacho, `review_evidence.py`, `rdo.py close`) — são eles os eventos. *Marcador* = `[gerente] `, que deixa de existir na skill.
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md:50` — as nove linhas que começam por - **Narra:** (linhas 50, 62, 81, 111, 130, 154, 165, 182 e 225 em 2026-09-24, uma por passo 2 a 10, cada uma imediatamente antes da linha - **Ação:** do passo; localizar pelo texto)
  - `.claude/skills/scrum-master/SKILL.md:365` — o último bullet de ## Guardrails, a linha que começa por - Toda linha do repertório (seção *Repertório de mensagens ao gerente*) é escrita como texto do agente
  - `.claude/skills/passagem-de-bastao/SKILL.md:12` — a linha que contém que o gancho do kit grava no arquivo de progresso
- **Contratos/classes:** nenhum código.
- **Texto novo, literal:** (a) na `scrum-master`, cada uma das nove linhas que começam por `- **Narra:**` é **removida inteira** (a linha `- **Ação:**` que a seguia fica onde está, sem linha em branco nova). (b) O último bullet de `## Guardrails` (a linha inteira que começa por `- Toda linha do repertório (seção *Repertório de mensagens ao gerente*) é escrita como texto do agente`) é substituído por esta linha, uma só:

  ```
  - O gerente acompanha a execução num painel fora da extensão que mostra `.claude/estado/progresso.txt`; cada linha desse arquivo é **gerada** pelo gancho `.claude/tools/progresso_hook.py` (eventos `PreToolUse`, `PostToolUse` e `Stop`) a partir do evento da transição — `backlog.py next`, `backlog.py status`, o despacho e o retorno de cada agente, `review_evidence.py` e o encerramento —, com o título da tarefa no lugar da sigla (seção *Repertório de mensagens ao gerente*). O condutor **não escreve** linha de repertório, não usa marcador e não escreve no arquivo; nenhuma saída de ferramenta chega a ele (`P-0748`, `DTG-30`, `I-2`, `I-11`).
  ```

  (c) Na `passagem-de-bastao`, o trecho `que o gancho do kit grava no arquivo de progresso` (nas linhas 11-13, hoje: *"o que chega ao dono chega pelas linhas do **repertório de mensagens ao gerente**, que o gancho do kit grava no arquivo de progresso, e pelo **relatório de encerramento**"*) passa a `que o gancho do kit gera a partir dos eventos do loop e grava no arquivo de progresso`; o resto da frase fica.
- **Passos:**
  1. Na `scrum-master`, remover as nove linhas que começam por `- **Narra:**`.
  2. Substituir o último bullet de `## Guardrails` pela linha de `Texto novo, literal` (b).
  3. Na `passagem-de-bastao`, trocar o trecho de `Texto novo, literal` (c).
  4. Rodar a Verificação 1 a 6.
- **Restrições desta tarefa:** `I-2` — a skill não manda o condutor escrever linha nenhuma do repertório; `I-11` — a skill não manda o loop escrever no arquivo; `DTG-36` — nenhum marcador, nenhum início de frase, nenhuma frase do repertório recopiada (a tabela de `TLG-T2b` fica intacta); `DTG-28` — nada de `numstat`: aceite por conteúdo. Na `scrum-master`, só as nove remoções e a troca de um bullet; na `passagem-de-bastao`, só a troca do trecho.
- **Não fazer:** não editar bullets `**Ação:**`, `**Gatilho:**`, `**Entrada:**`, `**Saída:**` nem nenhuma outra linha dos passos; não editar a seção `## Repertório de mensagens ao gerente` (é `TLG-T2b`); não remover outros bullets de `## Guardrails`; não editar agente, instrumento, `progresso_hook.py`, `projecoes.json`, testes ou `README.md` (é `TLG-T5`); não acrescentar instrução nova de narração.
- **Contingências:**
  1. se `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "**Narra:**" | Measure-Object).Count` não for `9` antes da edição → parar e sinalizar `blocked` razão `dependencia` se for `10` (`TLG-T2b` não entregou o parágrafo), `premissa` para qualquer outro valor, devolvendo a saída de `grep -n "Narra:" .claude/skills/scrum-master/SKILL.md`;
  2. se `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "[gerente] " | Measure-Object).Count` não for `1` antes da edição → parar e sinalizar `blocked` razão `premissa` com a saída de `grep -n "gerente\]" .claude/skills/scrum-master/SKILL.md`;
  3. se a `passagem-de-bastao` não contém `que o gancho do kit grava no arquivo de progresso` exatamente uma vez → parar e sinalizar `blocked` razão `premissa` com a saída de `grep -n "arquivo de progresso" .claude/skills/passagem-de-bastao/SKILL.md`.
- **Testes:** nenhum TF (texto de skill); TR: `python -m pytest tests/ -q` não reduz o total re-medido no despacho.
- **Verificação:**
  1. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "**Narra:**" | Measure-Object).Count` → antes `9` (depois de `TLG-T2b`; `10` em 2026-09-24, `F-26`), depois `0`.
  2. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "[gerente] " | Measure-Object).Count` → antes `1` (medido 2026-09-24), depois `0`.
  3. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "gerada** pelo gancho" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`.
  4. `(Select-String -SimpleMatch -Path .claude/skills/passagem-de-bastao/SKILL.md -Pattern "a partir dos eventos do loop" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`; e `arquivo de progresso` → antes `1`, depois `1`.
  5. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "- **Ação:**" | Measure-Object).Count` → igual antes e depois (nenhuma linha de ação removida; medir antes e colar os dois valores na linha de retorno).
  6. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` ≥ o total re-medido no despacho.
- **Pronto quando:** `stream de dados.o que as mensagens narram` — *ligado à tarefa e à intenção dos agentes: uma linha em linguagem humana por transição, gerada pela função no instante em que o loop a atravessa — e não escrita pelo condutor antes de agir —, e é ela que chega ao arquivo de progresso, sem saída de comando entre duas delas* — Verificação 1, 2, 3 e 4.
- **Fora do escopo desta tarefa:** a descrição pública e o painel (`TLG-T5`); a leitura do painel pelo dono (Marco 3, aceite de marco e não de card, `I-6`).

### TLG-T5 — A porta de entrada diz como o dono acompanha a execução no painel [Sonnet + dono · esforço low · classe redacao]
- **Status:** `done` · 2026-09-24
- **Objetivo:** O mantenedor da porta de entrada do repositório reescreve a descrição pública de como o dono acompanha a execução — o painel fora da extensão e como se lê a linha de cada passo —, e essa própria tarefa corre pelo loop já modificado, com o dono lendo nesse painel o fluxo em linguagem humana e dando o aceite final.
- **Fundamento:** `DTG-6` (corpus real: esta tarefa é o Marco 3), `DTG-27` (o painel e o comando que o abre), `DTG-30` e `DTG-33` (linha gerada, com o título), `DTG-36` (`DTG-14` caída: nenhuma reabertura de sessão; o `README` cita a seção da skill e mostra duas linhas de exemplo, não recopia), `DTG-37` (última tarefa), `F-15` (saída do `check-readme.ps1`, re-medida em 2026-09-24), `F-28` (âncoras do `README`, re-medidas em 2026-09-24), `I-6`, `I-9`, `I-12`.
- **Depende de:** `TLG-T4a`
- **Operação do modelo:** `OP-5`
  - OP-5: O mantenedor da porta de entrada do repositório reescreve a descrição pública de como o dono acompanha a execução — o painel fora da extensão e como se lê a linha de cada passo —, e essa própria tarefa corre pelo loop já modificado, com o dono lendo nesse painel o fluxo em linguagem humana e dando o aceite final.
  - precisa de: stream de dados — Quem implementa recebe o loop do condutor — as transições que ele atravessa a cada tarefa e o que ele tem em mãos em cada uma —, a função do kit que gera a linha a partir do evento de cada transição, e o arquivo de progresso onde essa função grava. A ferramenta que roda os agentes e o painel que mostra o arquivo ficam como estão.; tela do monitor — Quem implementa não mexe nela: o dono abre o painel e só o observa, na validação do fim. A sonda do começo foi feita no painel da extensão, e foi o que ela viu que tirou a tela de lá.
- **Camada e fronteira:** documentação pública (`README.md`): um trecho do parágrafo **O que é.** da `## 6. O loop de execução` e um trecho da célula de descrição da linha `scrum-master` na tabela de skills. Nenhuma skill, agente, instrumento ou configuração. O dono abre o painel (`DTG-27`) **antes** do despacho deste card, na mesma sessão — nenhuma reabertura é necessária (`AE-6`, `DTG-36`).
- **Domínio:** *porta de entrada* = `README.md`; *descrição pública* = o que um leitor sem acesso às skills entende sobre como se acompanha a execução; *painel* = o terminal integrado do VS Code rodando `Get-Content -Path .claude/estado/progresso.txt -Wait -Tail 30 -Encoding utf8` na raiz do repositório (`DTG-27`); *linha gerada* = a frase que o gancho grava no evento da transição, com o título da tarefa entre aspas no lugar da sigla (`I-12`).
- **Arquivos-alvo:**
  - `README.md:442` — a linha que contém ele lê um relatório no fim (única no arquivo, re-medida 2026-09-24)
  - `README.md:831` — a linha da tabela de skills da scrum-master, que contém roteia pelo veredito calculado e encerra a janela (única no arquivo, re-medida 2026-09-24)
- **Contratos/classes:** nenhum código.
- **Texto novo, literal:** na linha `README.md:442`, substituir o trecho `o gerente não medeia tarefa a tarefa — ele lê um relatório no fim.` (o resto da linha, antes e depois do trecho, fica) por:

  ```
  o gerente não medeia tarefa a tarefa: acompanha a execução num painel fora da extensão do editor,
  que mostra o arquivo de progresso `.claude/estado/progresso.txt` com uma linha em linguagem humana
  por transição — por exemplo `Tarefa "A porta de entrada diz como o dono acompanha a execução no
  painel". Passo: conferir os gates e preparar o despacho.` e `Agente revisor devolveu a tarefa "A
  porta de entrada diz como o dono acompanha a execução no painel": aprovado 100%, bloqueante
  nenhuma.` —, gerada por um gancho do kit (`.claude/tools/progresso_hook.py`) a partir do evento de
  cada transição do loop, com o título da tarefa no lugar da sigla e sem nenhuma saída de
  ferramenta entre duas linhas; as frases estão na seção *Repertório de mensagens ao gerente* da
  `scrum-master`. Para abrir o painel, no terminal integrado do VS Code, na raiz do repositório:
  `Get-Content -Path .claude/estado/progresso.txt -Wait -Tail 30 -Encoding utf8` (o arquivo nasce
  com a primeira linha gerada). No fim da janela, o gerente lê um relatório.
  ```

  Na tabela de skills, na linha `README.md:831`, substituir o trecho `roteia pelo veredito calculado e encerra a janela` por `roteia pelo veredito calculado e encerra a janela; a cada transição, um gancho do kit gera a linha em linguagem humana que o gerente lê no painel do arquivo de progresso`.
- **Passos:**
  1. Substituir o trecho da linha `README.md:442` pelo texto dado.
  2. Substituir o trecho da linha `README.md:831` pelo texto dado.
  3. Rodar a Verificação 1 a 6.
- **Restrições desta tarefa:** `I-9` — o `check-readme.ps1` sai `0`; `DTG-36` — o `README` cita a seção da skill e mostra duas linhas de exemplo, não recopia o repertório; nenhuma contagem do `README` muda (nenhum agente, skill ou guardrail do kit é acrescentado — `F-15`). Só estas duas edições.
- **Não fazer:** não acrescentar seção nova ao `README`; não reescrever o resto da `## 6`; não editar `README.md:100` (a `passagem-de-bastao` continua transparente ao gerente); não editar `.claude/README.md`; não tocar skill, agente, instrumento, `projecoes.json` ou `settings.json`; não quebrar o comando `Get-Content` em duas linhas; não escrever "reabrir a sessão".
- **Contingências:**
  1. se `check-readme.ps1` sair diferente de `0` → parar e sinalizar `blocked` razão `premissa` com a linha impressa;
  2. se o trecho `ele lê um relatório no fim` não aparece exatamente uma vez no `README.md` → parar e sinalizar `blocked` razão `premissa` com a saída de `grep -n "relatório no fim" README.md`;
  3. se o trecho `roteia pelo veredito calculado e encerra a janela` não aparece exatamente uma vez no `README.md` → parar e sinalizar `blocked` razão `premissa` com a saída de `grep -n "roteia pelo veredito calculado" README.md`.
- **Testes:** nenhum TF; guarda: `pwsh -NoProfile -File .claude/checks/check-readme.ps1`.
- **Verificação:**
  1. `pwsh -NoProfile -File .claude/checks/check-readme.ps1; $LASTEXITCODE` → `check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida; frases de contagem de 'Os guardrails' conferidas: 'regras mínimas obrigatórias'=True, 'regras falham como teste executável'=True.` e `0` (re-medido em 2026-09-24 nesta rodada; as contagens não mudam).
  2. `(Select-String -SimpleMatch -Path README.md -Pattern "Repertório de mensagens ao gerente" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`.
  3. `(Select-String -SimpleMatch -Path README.md -Pattern "ele lê um relatório no fim" | Measure-Object).Count` → antes `1` (medido 2026-09-24), depois `0`.
  4. `(Select-String -SimpleMatch -Path README.md -Pattern "gera a linha em linguagem humana" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`.
  5. `(Select-String -SimpleMatch -Path README.md -Pattern "Get-Content -Path .claude/estado/progresso.txt -Wait -Tail 30 -Encoding utf8" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`.
  6. `(Select-String -SimpleMatch -Path README.md -Pattern "progresso_hook.py" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`.
- **Pronto quando:** `stream de dados.descrição pública` — *a porta de entrada diz ao leitor que a execução se acompanha num painel fora da extensão, que mostra o arquivo de progresso com uma linha em linguagem humana a cada passo; diz como abrir esse painel e mostra como a linha se lê* — Verificação 2, 3, 4, 5 e 6. O veredito do dono sobre o painel **durante** esta tarefa é o Marco 3 (aceite de marco, `+ dono`, registrado na tabela de marcos do plano pela orquestração — `I-6`), e no mesmo ato ele valida a versão 3 da `## 1A`.
- **Fora do escopo desta tarefa:** propagação aos kits derivados (`DTG-8`, tíquete próprio no fechamento do plano); qualquer retroação que o Marco 3 peça (rodada tática sobre `TLG-T3b`, `TLG-T2b` ou `TLG-T4a`, `R-4`, `R-6`).

### TLG-T3c — O painel não perde linha e não afirma o que não aconteceu [Sonnet · esforço medium · classe implementacao]
- **Status:** `done` · 2026-09-24
- **Objetivo:** O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo.
- **Fundamento:** `DTG-42` (ato do dono no Marco 3: corrigir o que já está mapeado), `DTG-43` (consultor, acionamento 8), `DTG-41` (consultor, Marco 3), `DTG-40`, `DTG-33` (iv) (tarefa corrente), `DTG-39`, `R-6`, `AE-9`, `AE-10`, `AE-12`, `AE-16`, `AE-17` (i), `AE-18`, `I-3`, `I-11`, `I-12`.
- **Depende de:** `TLG-T5`
- **Operação do modelo:** `OP-3`
  - OP-3: O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo.
  - precisa de: stream de dados — Quem implementa recebe o loop do condutor — as transições que ele atravessa a cada tarefa e o que ele tem em mãos em cada uma —, a função do kit que gera a linha a partir do evento de cada transição, e o arquivo de progresso onde essa função grava. A ferramenta que roda os agentes e o painel que mostra o arquivo ficam como estão.; tarefa — Quem implementa lê dela o que preenche as mensagens: qual tarefa, o título dela, qual passo e o que o passo pede. Nada nela muda.; mente do agente — Quem implementa usa a intenção que o condutor já tem em mãos — o que ele pediu ao agente e o que o agente devolveu — como campo do evento que a função recebe. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo.
- **Camada e fronteira:** kit — `.claude/tools/progresso_hook.py` (só `texto_da_resposta`, `tarefa_corrente`, as regras 2, 3 e 7 de `evento`, um bloco novo depois da cadeia de regras e as duas buscas do ramo `pantonic-consultant` de `de_volta`), `tests/test_progresso_hook.py` (duas funções estendidas, uma reescrita, cinco novas) e **quatro** linhas da seção *Repertório de mensagens ao gerente* da `scrum-master` (`M-9`, `M-9b`, `M-10` e `M-17`, cópias legíveis da `### 4.1`, que o consultor já mudou no plano em `DTG-41` e `DTG-43`). `FRASES`, `capturar`, as regras 1 e 4 a 6, o resto de `de_volta`, `main`, `projecoes.json` e `settings.json` ficam como estão.
- **Domínio:** *estado próprio* e *tarefa corrente* como em `TLG-T3b`; *comando encadeado* = um só `command` de `Bash` com mais de um instrumento, unidos por `&&`, `;` ou quebra de linha — por exemplo `backlog.py status <ID> review && … review_evidence.py … --tarefa <ID> …`, que na `TLG-T5` não gerou o `M-5` (`AE-16`); *título sobrevivente* = o título que o estado próprio guarda depois que o `telemetria_hook` apaga `tarefa-corrente.json` no `SubagentStop` do executor (`telemetria_hook.py:193`, `AE-9`); *janela encerrada* = a parada com relatório de encerramento, que a `scrum-master` escreve "uma vez por janela, na parada" e abre com a saída de `python .claude/tools/modelo.py show --plano <plano>` (`scrum-master/SKILL.md:286-287`; é o único uso de `modelo.py show` no loop) — um `Stop` sem esse comando antes é fim de turno em que a janela segue (`AE-17` (i)); *linha de rota do consultor* = linha do relatório do consultor que começa, depois de brancos, por `rota=` ou por `estrategico=` — o mesmo texto no meio de uma frase não é linha de rota (`AE-18`).
- **Arquivos-alvo:**
  - `.claude/tools/progresso_hook.py:84` — def texto_da_resposta; as duas guardas if partes (linhas 101 e 110 em 2026-09-24)
  - `.claude/tools/progresso_hook.py:162` — def tarefa_corrente; o ramo que lê tarefa-corrente.json
  - `.claude/tools/progresso_hook.py:203` — as duas buscas do ramo elif sub == "pantonic-consultant" de de_volta, re.search(r"rota=(\S+)", texto) e re.search(r"estrategico=(.*)", texto)
  - `.claude/tools/progresso_hook.py:257` — o elif da regra 2, que contém backlog\.py status (\S+) (\S+) (única no arquivo), e o elif da regra 3 logo abaixo, que contém "review_evidence.py" in cmd
  - `.claude/tools/progresso_hook.py:326` — o elif ev == "Stop" (regra 7) e o return (linhas, estado_loop) de evento, antes do qual entra o bloco novo
  - `tests/test_progresso_hook.py:97` — def test_tf_ger_1_texto_da_resposta (estendida); def test_tf_ger_9_forma_generica (linha 325, estendida); def test_tf_ger_12_stop (linha 407, reescrita); as cinco funções novas entram depois de def test_tf_ger_19_userpromptsubmit_sem_volta_pendente e antes de def test_tf_cap_1_flag_ligado
  - `.claude/skills/scrum-master/SKILL.md:338` — as linhas da tabela que começam por | `M-9` |, | `M-9b` |, | `M-10` | (340) e | `M-17` | (349) (cada uma única; localizar pelo texto)
- **Contratos/classes:** assinaturas inalteradas. Semântica que muda, e só ela:
  - `texto_da_resposta(resp)`: com `content` lista (em `dict`) ou com `resp` lista, devolve `"\n".join(partes)` **mesmo com `partes` vazia** — as duas guardas `if partes` saem, e o `json.dumps` do ramo `list` sai junto; o `json.dumps` fica só para `dict` sem chave de texto e sem `content` lista (semântica fechada de `TLG-T3b`, `AE-12`).
  - `tarefa_corrente(estado_loop, estado, raiz)`: quando o id vem de `tarefa-corrente.json`, antes de devolver, grava `estado_loop["tarefa"] = tid`, `estado_loop["titulo"] = titulo`, `estado_loop["objetivo"] = objetivo` (o dicionário recebido, o mesmo que `evento` devolve e `main` persiste) (`AE-9`).
  - Regra 2: casa `re.search(r"backlog\.py status (\S+) ([a-z-]+)", cmd)` (o estado para no primeiro caractere fora de `[a-z-]`, para `done;` colado ao separador); com `st == "in-progress"` e `estado_loop.get("tarefa") != tid`: `titulo, objetivo, _ = localizar_card(tid, raiz)` e o estado ← `tarefa = tid`, `titulo`, `objetivo`; o resto da regra fica.
  - Regra 3: com `--tarefa` casado e `estado_loop.get("tarefa") != tid`: `titulo, objetivo, _ = localizar_card(tid, raiz)` e o estado ← `tarefa = tid`, `titulo`, `objetivo`; o resto da regra fica.
  - Regras 2 e 3 **deixam de ser excludentes**: num `PreToolUse` de `Bash`, aplica-se a regra 2 (se casa) e, em seguida, sobre o mesmo comando e o estado já atualizado, a regra 3 (se `"review_evidence.py" in cmd`); as linhas saem nessa ordem. As demais regras seguem "a primeira que casa" (`AE-16`).
  - `de_volta`, ramo `pantonic-consultant`: `mr = re.search(r"^\s*rota=(\S+)", texto, re.M)` e `me = re.search(r"^\s*estrategico=(.*)$", texto, re.M)`; o resto do ramo fica (`AE-18`).
  - Regra 7 (`Stop`): com `estado_loop.get("aberta") and estado_loop.get("relatorio")` → `M-17` e o estado ← `aberta = False`, `encerrada = True`, e `relatorio` sai (`pop`); senão nada (`AE-17` (i)).
  - Bloco novo, **fora** da cadeia `if`/`elif` e depois dela, logo antes do `return` de `evento`: `if ev == "PreToolUse" and tool == "Bash" and "modelo.py show" in cmd and estado_loop.get("aberta"): estado_loop["relatorio"] = True` — não gera linha e vale também para comando encadeado. `relatorio` é a única chave nova do estado próprio (emenda `DTG-31`, `DTG-43`). Com `aberta` false depois da `M-17`, o próximo `backlog.py next` da mesma sessão gera `M-0` (a janela reabre no painel) pela regra 1 como ela está.
- **Texto novo, literal:** na `scrum-master`, na linha que começa por `` | `M-10` | ``, o trecho `` `backlog\.py status (\S+) (\S+)` `` passa a `` `backlog\.py status (\S+) ([a-z-]+)` ``; o resto da linha fica. As linhas que começam por `` | `M-9` | ``, `` | `M-9b` | `` e `` | `M-17` | `` passam a ser, inteiras, as linhas de mesmo início da `### 4.1` do plano (copiar do plano, não redigitar). As quatro passam a ser iguais, caractere a caractere, às da `### 4.1`; a coluna *frase gerada* não muda em nenhuma (`TF-GER-18`).
- **Passos:**
  1. Rodar `python -m pytest tests/test_progresso_hook.py -q`, a Verificação 3 e a Verificação 6, e anotar (contingências 1 e 2).
  2. Editar `progresso_hook.py` com a semântica de `Contratos/classes`.
  3. Estender `TF-GER-1` e `TF-GER-9`, reescrever `TF-GER-12` e escrever `TF-GER-20` a `TF-GER-24` de `Testes`, com as fixtures de `TLG-T3b` (passo 4 dele).
  4. Trocar as linhas `M-9`, `M-9b`, `M-10` e `M-17` da skill (`Texto novo, literal`).
  5. Rodar a Verificação 1 a 7.
- **Restrições desta tarefa:** `I-11` — o gancho segue sem imprimir e saindo sempre `0`; `DTG-36` — `FRASES` não muda (`TF-GER-18`); `AE-10` — **nenhum passo nem verificação roda `progresso_hook.py` contra o `.claude/estado/` real** (sem `estado=` de pasta temporária): o estado da sessão do loop é o que o painel certifica, e o `TF` com `tmp_path` é a única prova; `I-7` — o total de `pytest tests/` não cai. Na skill, só as linhas `M-9`, `M-9b`, `M-10` e `M-17`.
- **Não fazer:** não editar `FRASES`, `capturar`, `main`, as regras 1 e 4 a 6, `localizar_card` nem `frase`; em `de_volta`, só as duas buscas do ramo `pantonic-consultant`; não criar chave nova no estado próprio além de `relatorio`; não editar `.claude/projecoes.json`, `.claude/settings.json`, `telemetria_hook.py` nem outro instrumento; não editar outra linha da skill, a `### 4.1` do plano nem o `README.md` (é `TLG-T5a`); não apagar nem reescrever `.claude/estado/progresso.txt` ou `progresso-estado.json`; não alterar asserção existente dos `TF-GER` além das extensões de `TF-GER-1` e `TF-GER-9` e da reescrita de `TF-GER-12`.
- **Contingências:**
  1. se `python -m pytest tests/test_progresso_hook.py -q` antes da edição não sai `22 passed` → parar e sinalizar `blocked` razão `dependencia`, devolvendo a linha impressa;
  2. se a Verificação 3 antes da edição não dá `2`, ou `(Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "backlog\.py status (\S+) (\S+)" | Measure-Object).Count` não dá `1` → parar e sinalizar `blocked` razão `premissa`, devolvendo a saída de `grep -n "if partes\|py status" .claude/tools/progresso_hook.py`;
  3. se a Verificação 6 antes da edição não imprime `iguais 19 de 23 23` → parar e sinalizar `blocked` razão `premissa` com a linha impressa;
  4. se `python -m pytest tests/ -q` reduz o total por teste **fora** de `tests/test_progresso_hook.py` → parar e sinalizar `blocked` razão `dependencia` com o nome do teste.
- **Testes:** `tests/test_progresso_hook.py`, fixtures e `P` de `TLG-T3b`; o valor do gancho vigente sobre a mesma fixture vem entre parênteses (medido pelo consultor em 2026-09-24).
  - `TF-GER-1` (estendido) — `texto_da_resposta({"content": []})`, `texto_da_resposta([])` e `texto_da_resposta({"content": [{"type": "image"}]})` devolvem `""` (vigente: `'{"content": []}'`, `'[]'` e `'{"content": [{"type": "image"}]}'`); as asserções que já existem ficam, inclusive `{"x": 1}` → `'{"x": 1}'`.
  - `TF-GER-9` (estendido) — depois do `next` do `TF-GER-2`, `P(hook_event_name="PostToolUse", tool_name="Agent", tool_input={"subagent_type": "pantonic-executor"}, tool_response={"content": []})` → última linha `Agente executor devolveu a tarefa "Um título de teste": (sem texto).` (vigente: `…: {"content": []}.`).
  - `TF-GER-20` — o título sobrevive ao `SubagentStop`: estado vazio e `estado / "tarefa-corrente.json"` = `{"tarefa": "TLG-T9"}`; `P(hook_event_name="PreToolUse", tool_name="Agent", tool_input={"subagent_type": "pantonic-executor", "prompt": "…"})`; apagar `tarefa-corrente.json`; `PostToolUse` `Agent` do executor com `tool_response={"status": "completed", "agentId": "a1", "agentType": "pantonic-executor", "handback": "send", "content": [{"type": "text", "text": "ptr"}]}`; `P(hook_event_name="UserPromptSubmit", prompt="<agent-message from=\"a1\">\nx The report follows:\n  TLG-T9 review\n</agent-message>")`; `PreToolUse` `Agent` `pantonic-reviewer` → `progresso()` == `['Agente executor recebe a tarefa "Um título de teste" e vai executar: Fazer x.', 'Agente executor devolveu a tarefa "Um título de teste": review — sem pendência.', 'Agente revisor recebe a tarefa "Um título de teste" e vai confrontar a entrega com o card.']` e o estado tem `tarefa == "TLG-T9"` (vigente: a segunda e a terceira com `"(tarefa não identificada)"`).
  - `TF-GER-21` — a evidência e o `in-progress` alimentam o estado: estado vazio, sem `tarefa-corrente.json`; `PreToolUse` `Bash` com `command` = `python .claude/tools/review_evidence.py --plano docs/plans/P-9999-teste.md --tarefa TLG-T9 --desde abc --out x.md`; `PreToolUse` `Agent` `pantonic-reviewer`; `PreToolUse` `Bash` com `command` = `python .claude/tools/backlog.py status TLG-T10 in-progress`; `PreToolUse` `Agent` `pantonic-executor` com `prompt` `…` → `progresso()` == `['Tarefa "Um título de teste": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.', 'Agente revisor recebe a tarefa "Um título de teste" e vai confrontar a entrega com o card.', 'Tarefa "Outro título": gates aprovados; vou materializar in-progress e gravar o ponto de partida.', 'Agente executor recebe a tarefa "Outro título" e vai executar: Fazer y.']` (vigente: a segunda com `"(tarefa não identificada)"`, a quarta `Agente executor recebe a tarefa "(tarefa não identificada)" e vai executar o card.`).
  - `TF-GER-22` — comando encadeado: depois do `next` do `TF-GER-2`, `PreToolUse` `Bash` com `command` = `python .claude/tools/backlog.py status TLG-T9 review && python .claude/tools/review_evidence.py --plano docs/plans/P-9999-teste.md --tarefa TLG-T9 --desde abc --out x.md` → exatamente uma linha nova, `Tarefa "Um título de teste": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.`; em seguida `command` = `python .claude/tools/backlog.py status TLG-T9 in-progress; python .claude/tools/review_evidence.py --plano x --tarefa TLG-T9 --desde abc --atribuir` → exatamente duas linhas novas, `Tarefa "Um título de teste": gates aprovados; vou materializar in-progress e gravar o ponto de partida.` e `Tarefa "Um título de teste": vou medir a que arquivo a pendência é atribuível.` (vigente: nenhuma linha nos dois).
  - `TF-GER-12` (reescrito) — fim de turno não encerra a janela: estado `{"sessao": "s1", "aberta": True}`; `P(hook_event_name="Stop")` → `progresso()` == `[]` (vigente: a `M-17`); `PreToolUse` `Bash` com `command` = `python .claude/tools/modelo.py show --plano docs/plans/P-9999-teste.md` → `[]`; `Stop` → `["Scrum master encerrou a janela; o relatório está na extensão."]`, e o estado tem `encerrada is True`, `aberta is False` e não tem `relatorio`; segundo `Stop` → ainda uma linha; pasta de estado nova, só `Stop` → sem `progresso.txt`; outra pasta nova, `modelo.py show` e `Stop` → sem `progresso.txt` (janela nunca aberta).
  - `TF-GER-23` — a janela no painel: `next` de `TLG-T9` (`=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]`); `Stop`; `PreToolUse` `Bash` `python .claude/tools/backlog.py status TLG-T9 done`; `PreToolUse` `Bash` `python .claude/tools/modelo.py show --plano docs/plans/P-9999-teste.md`; `Stop`; `Stop`; `next` de `TLG-T10` (`… TLG-T10 — Outro título [Sonnet · classe redacao]`) → `progresso()` == `['Abrindo a janela do plano "Plano de teste".', 'Tarefa "Um título de teste". Passo: conferir os gates e preparar o despacho.', 'Scrum master vai fechar a tarefa "Um título de teste" como done: registrar estado, RDO e telemetria, e selecionar a próxima.', 'Scrum master encerrou a janela; o relatório está na extensão.', 'Abrindo a janela do plano "Plano de teste".', 'Scrum master concluiu a tarefa "Um título de teste" e vai pegar a tarefa "Outro título".', 'Tarefa "Outro título". Passo: conferir os gates e preparar o despacho.']` (vigente: a `M-17` sai no primeiro `Stop`, logo depois da `M-1`, e a reabertura não mostra a `M-0`).
  - `TF-GER-24` — `estrategico=` em prosa não é estratégico: `_volta_consultor(estado, raiz, "rota=resolve\nDecisão: sem `estrategico=`, o impedimento é tático.")` → `'Agente consultor devolveu a tarefa "Um título de teste": rota resolve.'`; e, com estado `{"sessao": "s1", "tarefa": "TLG-T9", "titulo": "Um título de teste", "pendentes": {"c1": "pantonic-consultant"}}`, `UserPromptSubmit` com `prompt` = `<agent-message from="c1">` + `\n[Subagent hand-back] The text below is the final report of a subagent this session delegated to. The report follows:\n  rota=resolve\n  - Decisão: sem `estrategico=`, o impedimento é tático.\n</agent-message>` → a mesma linha (vigente, nos dois: `…: rota resolve; estratégico: `, o impedimento é tático..`). O `TF-GER-8` e o `TF-GER-19`, que ficam, provam que `estrategico=` no início de linha, com ou sem brancos, segue dando a `M-9b`.

  Suítes: `python -m pytest tests/test_progresso_hook.py -q`; `python -m pytest tests/ -q`.
- **Verificação:**
  1. `python -m pytest tests/test_progresso_hook.py -q` → antes `22 passed` (medido 2026-09-24 pelo consultor), depois `27 passed`.
  2. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` = total re-medido no despacho + `5` (medido 2026-09-24: `302 passed`).
  3. `(Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "if partes" | Measure-Object).Count` → antes `2` (medido 2026-09-24), depois `0`.
  4. Semântica de `texto_da_resposta` e `FRASES` intacto, bloco cercado por conter aspas:

     ```
     python -c "import importlib.util as u;s=u.spec_from_file_location('h','.claude/tools/progresso_hook.py');m=u.module_from_spec(s);s.loader.exec_module(m);print(repr(m.texto_da_resposta({'content':[]})),repr(m.texto_da_resposta([])),len(m.FRASES))"
     ```

     → antes `'{"content": []}' '[]' 23` (medido 2026-09-24 em `powershell` 5.1 e `pwsh`), depois `'' '' 23`.
  5. `(Select-String -Path .claude/tools/progresso_hook.py -Pattern "^(from|import) (rdo|backlog|telemetria|modelo|ocupacao|materializar|subprocess)\b" | Measure-Object).Count` e `(Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "print(" | Measure-Object).Count` → antes `0` e `0` (medido 2026-09-24), depois `0` e `0`.
  6. Igualdade da tabela da skill com a `### 4.1`, bloco cercado por conter barra invertida:

     ```
     python -c "import re;f=lambda p:[l.rstrip() for l in open(p,encoding='utf-8') if re.match(r'^\| .M-\d+b?. \|',l)];a=f('.claude/skills/scrum-master/SKILL.md');b=f('docs/plans/P-0748-tela-do-gerente.md');print('iguais',sum(x==y for x,y in zip(a,b)),'de',len(a),len(b))"
     ```

     → antes `iguais 19 de 23 23` (medido 2026-09-24, depois de `DTG-41` mudar a `M-10` e `DTG-43` a `M-9`, a `M-9b` e a `M-17` da `### 4.1`), depois `iguais 23 de 23 23`.
  7. `(Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "modelo.py show" | Measure-Object).Count` e `(Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern 'r"estrategico=(.*)"' | Measure-Object).Count` → antes `0` e `1` (medido 2026-09-24), depois `1` e `0`.
- **Pronto quando:**
  - `stream de dados.agregação da linha` — *a função troca, ao gerar a linha, o identificador da tarefa pelo título dela e o do plano pelo título do plano, sem gastar nada do agente para isso; a sigla sozinha nunca chega ao dono* — Verificação 1 (`TF-GER-20`, `TF-GER-21`).
  - `stream de dados.arquivo de progresso` — *existe e é alimentado pela função do kit a cada transição do loop: guarda uma linha do repertório por transição, na ordem em que o loop as atravessa, gerada a partir do evento e não da memória do agente — nenhuma linha se perde por o condutor ter esquecido a forma —, e nada mais: nenhuma busca, leitura ou saída de comando, e nenhuma chamada feita dentro dos agentes despachados* — Verificação 1 (`TF-GER-1`, `TF-GER-9`, `TF-GER-12`, `TF-GER-22`, `TF-GER-23`, `TF-GER-24`), 3, 4, 6 e 7.
- **Fora do escopo desta tarefa:** a célula do `README.md` (`TLG-T5a`); a palavra "parada" da `M-8` (`AE-17` (ii): forma aceita pelo dono, `DTG-42`); o recorte `--desde` do dossiê (`AE-4`, `AE-5`, `AE-11`, `TK-55`); propagação aos kits derivados (`DTG-8`).

### TLG-T3d — O painel só diz que a janela encerrou quando ela encerrou [Sonnet · esforço low · classe implementacao]
- **Status:** `done` · 2026-09-24
- **Objetivo:** O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo.
- **Fundamento:** `DTG-44` (consultor, acionamento 9), `DTG-42` (ato do dono no Marco 3: corrigir o que já está mapeado), `DTG-43`, `AE-19`, `I-2`, `I-3`, `I-11`.
- **Depende de:** `TLG-T3c`
- **Operação do modelo:** `OP-3`
  - OP-3: O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo.
  - precisa de: stream de dados — Quem implementa recebe o loop do condutor — as transições que ele atravessa a cada tarefa e o que ele tem em mãos em cada uma —, a função do kit que gera a linha a partir do evento de cada transição, e o arquivo de progresso onde essa função grava. A ferramenta que roda os agentes e o painel que mostra o arquivo ficam como estão.; tarefa — Quem implementa lê dela o que preenche as mensagens: qual tarefa, o título dela, qual passo e o que o passo pede. Nada nela muda.; mente do agente — Quem implementa usa a intenção que o condutor já tem em mãos — o que ele pediu ao agente e o que o agente devolveu — como campo do evento que a função recebe. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo.
- **Camada e fronteira:** kit — `.claude/tools/progresso_hook.py` (quatro pontos de `evento`: o início da regra 1, o início do ramo `PreToolUse` · `Agent`, a condição da regra 7 e a condição do bloco `relatorio`), `tests/test_progresso_hook.py` (duas funções novas) e **uma** linha da seção *Repertório de mensagens ao gerente* da `scrum-master` (`M-17`, cópia legível da `### 4.1`, que o consultor já mudou em `DTG-44`). Todo o resto do gancho, `projecoes.json` e `settings.json` ficam como estão.
- **Domínio:** *relatório de encerramento* = o `python .claude/tools/modelo.py show --plano <plano>` que abre a parada (`scrum-master/SKILL.md:286-287`), **sem** `--drift` nem `--pendente` — essas duas são leituras do modelo, e o condutor roda `--drift` em pausa de marco (`AE-19`); *agente pendente* = entrada de `pendentes` no estado próprio, gravada no `PostToolUse` · `Agent` com `handback == "send"` e retirada na volta pelo `UserPromptSubmit` (`TLG-T3b`); um `Stop` com agente pendente é o fim de turno de quem espera o hand-back, nunca a parada; *entrada órfã* = agente que caiu sem volta (a `A1` despacha outro) — o `backlog.py next`, que o loop só roda sem agente em voo, esvazia `pendentes`.
- **Arquivos-alvo:**
  - `.claude/tools/progresso_hook.py:228` — o if da regra 1, que contém "backlog.py next" in cmd (único no arquivo)
  - `.claude/tools/progresso_hook.py:293` — o elif ev == "PreToolUse" and tool == "Agent" and sub in PAPEIS (único no arquivo)
  - `.claude/tools/progresso_hook.py:337` — a condição do elif ev == "Stop" (regra 7), if estado_loop.get("aberta") and estado_loop.get("relatorio"):
  - `.claude/tools/progresso_hook.py:343` — o bloco relatorio antes do return de evento, que contém "modelo.py show" in cmd
  - `tests/test_progresso_hook.py:864` — as duas funções novas entram depois de def test_tf_ger_24_estrategico_em_prosa_nao_e_estrategico e antes de def test_tf_cap_1_flag_ligado
  - `.claude/skills/scrum-master/SKILL.md:349` — a linha da tabela que começa por | `M-17` | (única; localizar pelo texto)
- **Contratos/classes:** assinaturas inalteradas. Semântica que muda, e só ela:
  - Regra 1: primeiras instruções do ramo, antes do `re.search` da `PRÓXIMA TAREFA`: `estado_loop.pop("relatorio", None)` e `estado_loop.pop("pendentes", None)` — valem para a tarefa escolhida e para "nada delegável"; o resto da regra fica.
  - Ramo `PreToolUse` · `Agent` · `sub in PAPEIS`: primeira instrução `estado_loop.pop("relatorio", None)`; o resto do ramo fica.
  - Regra 7 (`Stop`): a condição passa a `estado_loop.get("aberta") and estado_loop.get("relatorio") and not estado_loop.get("pendentes")`; o corpo fica.
  - Bloco `relatorio`: a condição passa a `ev == "PreToolUse" and tool == "Bash" and "modelo.py show" in cmd and "--drift" not in cmd and "--pendente" not in cmd and estado_loop.get("aberta")`; o corpo fica.
- **Texto novo, literal:** na `scrum-master`, a linha que começa por `` | `M-17` | `` passa a ser, inteira, a linha de mesmo início da `### 4.1` do plano (copiar do plano, não redigitar); a coluna *frase gerada* não muda (`TF-GER-18`).
- **Passos:**
  1. Rodar a Verificação 1, 3 e 5 e anotar (contingências 1 e 2).
  2. *(consultor, `DTG-45`)* A semântica de `Contratos/classes` já está em `progresso_hook.py` desde a primeira execução (Verificação 3 = `1 1 3 1`): conferir as quatro instruções contra `Contratos/classes` e **não** reeditar o gancho.
  3. Escrever `TF-GER-25` e `TF-GER-26` de `Testes`, com as fixtures e os ajudantes que o arquivo já tem (`P`, `payload_next`, `rodar`, `progresso`).
  4. Trocar a linha `M-17` da skill (`Texto novo, literal`).
  5. Rodar a Verificação 1 a 5.
- **Restrições desta tarefa:** `I-3` — nenhum comando, marcador ou flag novo do condutor: o sinal sai só de eventos que o loop já emite; `I-11` — o gancho segue sem imprimir e saindo sempre `0`; `DTG-36` — `FRASES` não muda; `AE-10` — nenhum passo nem verificação roda `progresso_hook.py` contra o `.claude/estado/` real; `I-7` — o total de `pytest tests/` não cai.
- **Não fazer:** não editar `FRASES`, `capturar`, `main`, `de_volta`, `texto_da_resposta`, `tarefa_corrente`, `localizar_card`, `frase` nem as regras 2 a 6 além do início do ramo `Agent` dito acima; não criar chave nova no estado próprio; não editar `modelo.py`, `.claude/projecoes.json`, `.claude/settings.json` nem outro instrumento; não editar outra linha da skill, a `### 4.1` do plano nem o `README.md` (é `TLG-T5a`); não apagar nem reescrever `.claude/estado/progresso.txt` ou `progresso-estado.json`; não alterar asserção existente dos `TF`.
- **Contingências:**
  1. se `python -m pytest tests/test_progresso_hook.py -q` antes da edição não sai `27 passed` → parar e sinalizar `blocked` razão `dependencia`, devolvendo a linha impressa;
  2. se a Verificação 3 antes da edição não dá `1 1 3 1` (`DTG-45`), ou a Verificação 5 antes não imprime `iguais 22 de 23 23` → parar e sinalizar `blocked` razão `premissa`, devolvendo a linha impressa e a saída de `grep -n "relatorio\|pendentes" .claude/tools/progresso_hook.py`;
  3. se `python -m pytest tests/ -q` reduz o total por teste **fora** de `tests/test_progresso_hook.py` → parar e sinalizar `blocked` razão `dependencia` com o nome do teste.
- **Testes:** `tests/test_progresso_hook.py`; `N9` abaixo = `"=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n- **Objetivo:** Fazer x.\n"`; `SHOW` = `"python .claude/tools/modelo.py show --plano docs/plans/P-9999-teste.md"`; despacho = `P(hook_event_name="PreToolUse", tool_name="Agent", tool_input={"subagent_type": <papel>, "prompt": "…"})`; volta pendente = `P(hook_event_name="PostToolUse", tool_name="Agent", tool_input={"subagent_type": <papel>}, tool_response={"status": "completed", "agentId": <id>, "agentType": <papel>, "handback": "send", "content": [{"type": "text", "text": "ptr"}]})`; hand-back = `P(hook_event_name="UserPromptSubmit", prompt=f'<agent-message from="{<id>}">\nx The report follows:\n  {<corpo>}\n</agent-message>')`. O valor do gancho vigente vem entre parênteses (medido pelo consultor em 2026-09-24).
  - `TF-GER-25` — `show` no meio da janela não a encerra, e o encerramento real não se perde. Sequência, numa só pasta de estado: `payload_next(N9)`; `PreToolUse` `Bash` `SHOW + " --drift"`; `Stop`; despacho `pantonic-executor`; volta pendente `pantonic-executor` id `a1`; `P(hook_event_name="UserPromptSubmit", prompt="mostre o modelo")`; `PreToolUse` `Bash` `SHOW`; `Stop`; hand-back `a1` corpo `TLG-T9 review`; despacho `pantonic-reviewer`; volta pendente `pantonic-reviewer` id `r1`; `Stop`; hand-back `r1` corpo `TLG-T9 aprovado 100 bloqueante=nenhuma`; `Stop`; `PreToolUse` `Bash` `python .claude/tools/backlog.py status TLG-T9 done`; `payload_next("nada delegável")`; `PreToolUse` `Bash` `SHOW`; `Stop` → `progresso()` == `['Abrindo a janela do plano "Plano de teste".', 'Tarefa "Um título de teste". Passo: conferir os gates e preparar o despacho.', 'Agente executor recebe a tarefa "Um título de teste" e vai executar: Fazer x.', 'Agente executor devolveu a tarefa "Um título de teste": review — sem pendência.', 'Agente revisor recebe a tarefa "Um título de teste" e vai confrontar a entrega com o card.', 'Agente revisor devolveu a tarefa "Um título de teste": aprovado 100%, bloqueante nenhuma.', 'Scrum master vai fechar a tarefa "Um título de teste" como done: registrar estado, RDO e telemetria, e selecionar a próxima.', 'Scrum master concluiu a tarefa "Um título de teste"; nada delegável na fila. Encerrando a janela com o relatório.', 'Scrum master encerrou a janela; o relatório está na extensão.']` (vigente: a `M-17` sai logo depois da `M-1`, no primeiro `Stop`, e falta a última linha). *(consultor, `DTG-45`)* O corpo do revisor leva o id da tarefa à frente, como `TF-GER-7` e `TF-GER-19` (`tests/test_progresso_hook.py:292,681`), e a linha esperada é a `M-7`; a forma sem id da primeira redação caía na `M-16` e também passava — medido os dois corpos no gancho da árvore, lista acima igual.
  - `TF-GER-26` — entrada órfã não apaga a `M-17` real: estado `{"sessao": "s1", "aberta": True, "tarefa": "TLG-T9", "titulo": "Um título de teste", "pendentes": {"x1": "pantonic-consultant"}}`; `payload_next("nada delegável")`; `PreToolUse` `Bash` `SHOW`; `Stop` → `progresso()` == `['Scrum master não encontrou tarefa delegável na fila. Encerrando a janela com o relatório.', 'Scrum master encerrou a janela; o relatório está na extensão.']` (vigente: igual — é a guarda da condição nova da regra 7, que sem o esvaziamento no `next` perderia a segunda linha).

  Suítes: `python -m pytest tests/test_progresso_hook.py -q`; `python -m pytest tests/ -q`.
- **Verificação:**
  1. `python -m pytest tests/test_progresso_hook.py -q` → antes `27 passed` (medido 2026-09-24 pelo consultor), depois `29 passed`.
  2. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` = total re-medido no despacho + `2` (medido 2026-09-24: `307 passed`).
  3. Contagens no gancho, quatro comandos PowerShell, bloco cercado por conter aspas:

     ```
     (Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern '"--drift" not in cmd' | Measure-Object).Count
     (Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern 'not estado_loop.get("pendentes")' | Measure-Object).Count
     (Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern 'estado_loop.pop("relatorio", None)' | Measure-Object).Count
     (Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern 'estado_loop.pop("pendentes", None)' | Measure-Object).Count
     ```

     → antes `1 1 3 1` (re-medido 2026-09-24 em `powershell` 5.1 e `pwsh` sobre a edição parcial da primeira execução, `DTG-45`; a árvore anterior dava `0 0 1 0`), depois `1 1 3 1`.
  4. `(Select-String -Path .claude/tools/progresso_hook.py -Pattern "^(from|import) (rdo|backlog|telemetria|modelo|ocupacao|materializar|subprocess)\b" | Measure-Object).Count` e `(Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "print(" | Measure-Object).Count` → antes `0` e `0` (medido 2026-09-24), depois `0` e `0`.
  5. Igualdade da tabela da skill com a `### 4.1`, bloco cercado por conter barra invertida:

     ```
     python -c "import re;f=lambda p:[l.rstrip() for l in open(p,encoding='utf-8') if re.match(r'^\| .M-\d+b?. \|',l)];a=f('.claude/skills/scrum-master/SKILL.md');b=f('docs/plans/P-0748-tela-do-gerente.md');print('iguais',sum(x==y for x,y in zip(a,b)),'de',len(a),len(b))"
     ```

     → antes `iguais 22 de 23 23` (medido 2026-09-24, depois de `DTG-44` mudar a `M-17` da `### 4.1`), depois `iguais 23 de 23 23`.
- **Pronto quando:**
  - `stream de dados.arquivo de progresso` — *existe e é alimentado pela função do kit a cada transição do loop: guarda uma linha do repertório por transição, na ordem em que o loop as atravessa, gerada a partir do evento e não da memória do agente — nenhuma linha se perde por o condutor ter esquecido a forma —, e nada mais: nenhuma busca, leitura ou saída de comando, e nenhuma chamada feita dentro dos agentes despachados* — Verificação 1 (`TF-GER-25`, `TF-GER-26`), 3, 4 e 5.
- **Fora do escopo desta tarefa:** a célula do `README.md` (`TLG-T5a`); o recorte `--desde` do dossiê (`AE-4`, `AE-5`, `AE-11`, `TK-55`); propagação aos kits derivados (`DTG-8`).

### TLG-T3e — O painel diz só o que o gancho vê: o modelo mostrado e o consultor despachado [Sonnet · esforço low · classe implementacao]
- **Status:** `done` · 2026-09-24
- **Objetivo:** O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo.
- **Fundamento:** `DTG-49` (consultor, acionamento 13: a `M-10` e o "concluiu" da `M-11`/`M-12` depois de `blocked`/`cancelled`, `AE-21`), `DTG-48` (consultor, acionamento 12), `DTG-47` (ato do dono: o aceite é de forma; corrigir todo desvio mapeado), `DTG-46`, `AE-20`, `AE-17` (ii), `I-2`, `I-3`, `I-11`.
- **Depende de:** `TLG-T3d`
- **Operação do modelo:** `OP-3`
  - OP-3: O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo.
  - precisa de: stream de dados — Quem implementa recebe o loop do condutor — as transições que ele atravessa a cada tarefa e o que ele tem em mãos em cada uma —, a função do kit que gera a linha a partir do evento de cada transição, e o arquivo de progresso onde essa função grava. A ferramenta que roda os agentes e o painel que mostra o arquivo ficam como estão.; tarefa — Quem implementa lê dela o que preenche as mensagens: qual tarefa, o título dela, qual passo e o que o passo pede. Nada nela muda.; mente do agente — Quem implementa usa a intenção que o condutor já tem em mãos — o que ele pediu ao agente e o que o agente devolveu — como campo do evento que a função recebe. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo.
- **Camada e fronteira:** kit — `.claude/tools/progresso_hook.py` (três entradas de `FRASES` e uma nova, uma instrução da regra 1, o ramo de fechamento da regra 2 e a regra 7 de `evento`), `tests/test_progresso_hook.py` (asserções de frase e de estado em `TF-GER-4`, `5`, `12`, `18`, `23`, `25`, `26` e três funções novas) e **quatro** linhas da seção *Repertório de mensagens ao gerente* da `scrum-master` (`M-8`, `M-10` e `M-17` trocadas, `M-10b` nova; cópia legível da `### 4.1`, que o consultor já mudou em `DTG-48` e `DTG-49`). Todo o resto do gancho, `projecoes.json` e `settings.json` ficam como estão.
- **Domínio:** *o que o gancho vê* = o evento e o estado próprio, nunca a intenção do condutor (`DTG-47`, `DTG-48`): no `Stop` depois de um `modelo.py show` sem `--drift` nem `--pendente`, o gancho vê que o modelo do plano foi mostrado e o turno acabou — não se a janela encerrou, nem se há agente caído; no despacho do `pantonic-consultant`, vê o despacho — não se houve parada; no `backlog.py status <ID> done`, vê o fechamento que o passo 9 faz (estado, RDO, telemetria) — não se o bloco B vai selecionar a próxima; no `status <ID> blocked|cancelled`, vê o estado pedido — não RDO, não próxima e não conclusão (`DTG-49`); *`relatorio`* = a chave do estado próprio que o `show` grava e que o despacho de agente, o `backlog.py next` e o `Stop` tiram (inalterado, salvo o `Stop`, que agora só a tira); *`pendentes`* segue servindo só ao casamento do hand-back (`UserPromptSubmit`).
- **Arquivos-alvo:**
  - `.claude/tools/progresso_hook.py:43` — a entrada 'M-8' de FRASES (única)
  - `.claude/tools/progresso_hook.py:55` — a entrada 'M-17' de FRASES (única)
  - `.claude/tools/progresso_hook.py:46` — a entrada 'M-10' de FRASES (única); a 'M-10b' entra logo depois dela
  - `.claude/tools/progresso_hook.py:230` — a instrução estado_loop.pop("pendentes", None) da regra 1 (única no arquivo)
  - `.claude/tools/progresso_hook.py:274` — o elif st in ("done", "blocked", "cancelled") da regra 2 e as três linhas do corpo dele
  - `.claude/tools/progresso_hook.py:339` — o elif ev == "Stop" (regra 7) e as quatro linhas do corpo dele
  - `tests/test_progresso_hook.py:199` — a asserção da M-10 em test_tf_ger_4_estado_mudado (197-200)
  - `tests/test_progresso_hook.py:236` — a asserção da M-8 em test_tf_ger_5_agente_despachado
  - `tests/test_progresso_hook.py:642` — as duas contagens == 23 de test_tf_ger_18_residencia (642, 648)
  - `tests/test_progresso_hook.py:438` — as asserções de test_tf_ger_12_stop (438, 440, 441)
  - `tests/test_progresso_hook.py:854` — a lista de test_tf_ger_23_janela_no_painel
  - `tests/test_progresso_hook.py:963` — a lista de test_tf_ger_25_show_no_meio_da_janela_nao_encerra
  - `tests/test_progresso_hook.py:991` — a lista de test_tf_ger_26_entrada_orfa_nao_apaga_a_m17_real
  - `tests/test_progresso_hook.py:995` — as três funções novas entram depois de def test_tf_ger_26_entrada_orfa_nao_apaga_a_m17_real e antes de # --- TF-CAP-1..3
  - `.claude/skills/scrum-master/SKILL.md:337` — as linhas da tabela que começam por | `M-8` |, | `M-10` | (340) e | `M-17` | (349) (cada uma única; localizar pelo texto); a | `M-10b` | entra logo depois da | `M-10` |
- **Contratos/classes:** assinaturas inalteradas. Semântica que muda, e só ela:
  - `FRASES['M-8']` = `Agente consultor recebe a tarefa "<título>" e vai triar.`; `FRASES['M-10']` = `Scrum master vai fechar a tarefa "<título>" como done: registrar estado, RDO e telemetria.`; `FRASES['M-10b']` (nova, logo depois da `M-10`) = `Scrum master vai marcar a tarefa "<título>" como <estado>, sem RDO.`; `FRASES['M-17']` = `Scrum master mostrou o modelo do plano e aguarda; a resposta dele está na extensão.` (as quatro iguais, letra a letra, à coluna *frase gerada* da `### 4.1`; `FRASES` passa de 23 a 24 entradas).
  - Regra 1: sai a linha `estado_loop.pop("pendentes", None)`; a `estado_loop.pop("relatorio", None)` antes dela fica.
  - Regra 2, ramo de fechamento: `elif st == "done":` com corpo `linhas.append(frase("M-10", {"<título>": titulo}))`, `estado_loop["tarefa_fechada"] = tid`, `estado_loop["titulo_fechada"] = titulo`; seguido de `elif st in ("blocked", "cancelled"):` com corpo único `linhas.append(frase("M-10b", {"<título>": titulo, "<estado>": st}))` — sem `tarefa_fechada`, para a `M-11` e a `M-12` não dizerem "concluiu" de tarefa parada (`DTG-49`).
  - Regra 7 (`Stop`): a condição passa a `estado_loop.get("aberta") and estado_loop.get("relatorio")`; o corpo passa a duas instruções, `linhas.append(frase("M-17", {}))` e `estado_loop.pop("relatorio", None)` — saem `estado_loop["aberta"] = False` e `estado_loop["encerrada"] = True`.
- **Texto novo, literal:** na `scrum-master`, as linhas que começam por `` | `M-8` | ``, `` | `M-10` | `` e `` | `M-17` | `` passam a ser, inteiras, as linhas de mesmo início da `### 4.1` do plano, e a linha `` | `M-10b` | `` da `### 4.1` entra logo depois da `` | `M-10` | `` (copiar do plano, não redigitar).
- **Passos:**
  1. Rodar a Verificação 1, 3, 4 e 6 e anotar (contingências 1 e 2).
  2. Editar o gancho (`Contratos/classes`).
  3. Ajustar as asserções existentes e escrever `TF-GER-27`, `TF-GER-28` e `TF-GER-29` de `Testes`, com as fixtures e os ajudantes que o arquivo já tem (`P`, `payload_next`, `rodar`, `progresso`).
  4. Trocar as linhas `M-8`, `M-10` e `M-17` da skill e inserir a `M-10b` (`Texto novo, literal`).
  5. Rodar a Verificação 1 a 6.
- **Restrições desta tarefa:** `I-3` — nenhum comando, marcador ou flag novo do condutor; `I-11` — o gancho segue sem imprimir e saindo sempre `0`; `DTG-36` — de `FRASES` só mudam `M-8`, `M-10` e `M-17`, e só entra `M-10b` (`DTG-47`, `DTG-48`, `DTG-49`); `AE-10` — nenhum passo nem verificação roda `progresso_hook.py` contra o `.claude/estado/` real; `I-7` — o total de `pytest tests/` não cai.
- **Não fazer:** não editar `capturar`, `main`, `de_volta`, `texto_da_resposta`, `tarefa_corrente`, `localizar_card`, `frase`, as regras 2 a 6 além do ramo de fechamento da regra 2, o bloco `relatorio` antes do `return` nem as instruções da regra 1 além da dita; não criar nem apagar chave do estado além do que `Contratos/classes` diz (`encerrada = False` da regra 1 fica); não editar `modelo.py`, `.claude/projecoes.json`, `.claude/settings.json` nem outro instrumento; não editar outra linha da skill, a `### 4.1` do plano nem o `README.md` (é `TLG-T5a`); não apagar nem reescrever `.claude/estado/progresso.txt` ou `progresso-estado.json`; não alterar asserção dos `TF` além das nomeadas em `Testes`.
- **Contingências:**
  1. se `python -m pytest tests/test_progresso_hook.py -q` antes da edição não sai `29 passed` → parar e sinalizar `blocked` razão `dependencia`, devolvendo a linha impressa;
  2. se a Verificação 3 antes da edição não imprime `gancho 1 1 3 1 1 1 0`, a 4 `skill 1 1 0 1 0`, ou a 6 `iguais 12 de 23 24` → parar e sinalizar `blocked` razão `premissa`, devolvendo a linha impressa e a saída de `grep -n "relatorio\|pendentes\|encerrada" .claude/tools/progresso_hook.py`;
  3. se `python -m pytest tests/ -q` reduz o total por teste **fora** de `tests/test_progresso_hook.py` → parar e sinalizar `blocked` razão `dependencia` com o nome do teste.
- **Testes:** `tests/test_progresso_hook.py`; `N17` abaixo = `"Scrum master mostrou o modelo do plano e aguarda; a resposta dele está na extensão."`; `N9`, `SHOW`, despacho, volta pendente e hand-back como no card de `TLG-T3d` (§5, `Testes`). Asserções existentes que mudam, e só elas:
  - `TF-GER-4` — a da `M-10` passa a `'Scrum master vai fechar a tarefa "Um título de teste" como done: registrar estado, RDO e telemetria.'` (o `tarefa_fechada` == `TLG-T9` fica).
  - `TF-GER-5` — a da `M-8` passa a `'Agente consultor recebe a tarefa "Um título de teste" e vai triar.'`.
  - `TF-GER-18` — as duas contagens `== 23` passam a `== 24`.
  - `M-10` nas listas de `TF-GER-23`, `TF-GER-25` e `TF-GER-27` — onde a lista traz `'Scrum master vai fechar a tarefa "Um título de teste" como done: registrar estado, RDO e telemetria, e selecionar a próxima.'`, ela passa a `'Scrum master vai fechar a tarefa "Um título de teste" como done: registrar estado, RDO e telemetria.'`; vale junto das mudanças abaixo.
  - `TF-GER-12` — a lista depois do segundo `Stop` passa a `[N17]`; as asserções `estado_loop["encerrada"] is True` e `estado_loop["aberta"] is False` saem, e entra `estado_loop["aberta"] is True`; o resto fica (o terceiro `Stop` segue dando uma linha só).
  - `TF-GER-23` — a `M-17` da lista passa a `N17`, e sai da lista o segundo `'Abrindo a janela do plano "Plano de teste".'`, o que vinha logo depois dela (a janela não fechou; lista de 6).
  - `TF-GER-25` — a última linha passa a `N17`, e entra `N17` logo depois de `'Agente executor recebe a tarefa "Um título de teste" e vai executar: Fazer x.'` (o `show` pedido com `a1` em voo, seguido de `Stop`; lista de 10).
  - `TF-GER-26` — a segunda linha passa a `N17`.
  Funções novas (o valor do gancho vigente vem entre parênteses, medido pelo consultor em 2026-09-24):
  - `TF-GER-27` — `show` puro no meio da janela (exercício (a) do `AE-20`): `payload_next(N9)`; `PreToolUse` `Bash` `SHOW`; `Stop`; despacho `pantonic-executor`; volta pendente `pantonic-executor` id `a1`; `Stop`; hand-back `a1` corpo `TLG-T9 review`; `PreToolUse` `Bash` `python .claude/tools/backlog.py status TLG-T9 done`; `payload_next("nada delegável")`; `PreToolUse` `Bash` `SHOW`; `Stop` → `progresso()` == `['Abrindo a janela do plano "Plano de teste".', 'Tarefa "Um título de teste". Passo: conferir os gates e preparar o despacho.', N17, 'Agente executor recebe a tarefa "Um título de teste" e vai executar: Fazer x.', 'Agente executor devolveu a tarefa "Um título de teste": review — sem pendência.', 'Scrum master vai fechar a tarefa "Um título de teste" como done: registrar estado, RDO e telemetria, e selecionar a próxima.', 'Scrum master concluiu a tarefa "Um título de teste"; nada delegável na fila. Encerrando a janela com o relatório.', N17]` e o estado com `aberta` `True` (vigente: `Scrum master encerrou a janela…` na terceira posição, falta a última linha, `aberta=False`).
  - `TF-GER-28` — agente caído e parada sem `next` (exercício (b) do `AE-20`): `payload_next(N9)`; despacho `pantonic-executor`; volta pendente id `a1`; `Stop`; despacho `pantonic-executor`; volta pendente id `a2`; `Stop`; hand-back `a2` corpo `TLG-T9 review`; despacho `pantonic-reviewer`; volta pendente id `r1`; `Stop`; hand-back `r1` corpo `TLG-T9 aprovado 100 bloqueante=nenhuma`; `PreToolUse` `Bash` `python .claude/tools/backlog.py status TLG-T9 done`; `PreToolUse` `Bash` `SHOW`; `Stop` → `len(progresso())` == `9`, `progresso()[-1]` == `N17` e `pendentes` do estado == `{"a1": "pantonic-executor"}` (vigente: 8 linhas, a última a `M-10`).
  - `TF-GER-29` — tarefa parada não é tarefa concluída (`AE-21`): `N10T` = `"=== PRÓXIMA TAREFA: TLG-T10 — Outro título [Sonnet · classe redacao]\n- **Objetivo:** Fazer y.\n"`; `payload_next(N9)`; `PreToolUse` `Bash` `python .claude/tools/backlog.py status TLG-T9 blocked`; `payload_next(N10T)`; `PreToolUse` `Bash` `python .claude/tools/backlog.py status TLG-T10 cancelled`; `payload_next("nada delegável")` → `progresso()` == `['Abrindo a janela do plano "Plano de teste".', 'Tarefa "Um título de teste". Passo: conferir os gates e preparar o despacho.', 'Scrum master vai marcar a tarefa "Um título de teste" como blocked, sem RDO.', 'Tarefa "Outro título". Passo: conferir os gates e preparar o despacho.', 'Scrum master vai marcar a tarefa "Outro título" como cancelled, sem RDO.', 'Scrum master não encontrou tarefa delegável na fila. Encerrando a janela com o relatório.']` e o estado sem `tarefa_fechada` (vigente: terceira e quinta linhas `… como blocked: registrar estado, RDO e telemetria, e selecionar a próxima.`, uma `Scrum master concluiu a tarefa "Um título de teste" e vai pegar a tarefa "Outro título".` antes da quarta e, no fim, `Scrum master concluiu a tarefa "Outro título"; nada delegável na fila. …` — 7 linhas).

  Medido pelo consultor em 2026-09-24 numa cópia temporária com a semântica inteira deste card: `32 passed`; o gancho da árvore contra os 32 falha 10 (`TF-GER-4`, `5`, `12`, `18`, `23`, `25`, `26`, `27`, `28`, `29`).

  Suítes: `python -m pytest tests/test_progresso_hook.py -q`; `python -m pytest tests/ -q`.
- **Verificação:**
  1. `python -m pytest tests/test_progresso_hook.py -q` → antes `29 passed` (medido 2026-09-24 pelo consultor), depois `32 passed`.
  2. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` = total re-medido no despacho + `3` (medido 2026-09-24, acionamento 13: `309 passed`).
  3. Contagens no gancho, bloco cercado por conter aspas (colar numa sessão PowerShell na raiz):

     ```
     $h='.claude/tools/progresso_hook.py'; "gancho " + ((@('"--drift" not in cmd','not estado_loop.get("pendentes")','estado_loop.pop("relatorio", None)','estado_loop.pop("pendentes", None)','estado_loop["encerrada"] = True','RDO e telemetria, e selecionar a pr',', sem RDO.') | ForEach-Object { (Select-String -SimpleMatch -Path $h -Pattern $_ | Measure-Object).Count }) -join ' ')
     ```

     → antes `gancho 1 1 3 1 1 1 0`, depois `gancho 1 0 3 0 0 0 1` (medido 2026-09-24 em `powershell` 5.1 e `pwsh`, na árvore e numa cópia com a semântica nova).
  4. Contagens na skill, bloco cercado:

     ```
     $s='.claude/skills/scrum-master/SKILL.md'; "skill " + ((@('recebe a parada da tarefa','Scrum master encerrou a janela; o relat','Scrum master mostrou o modelo do plano e aguarda','RDO e telemetria, e selecionar a pr',', sem RDO.') | ForEach-Object { (Select-String -SimpleMatch -Path $s -Pattern $_ | Measure-Object).Count }) -join ' ')
     ```

     → antes `skill 1 1 0 1 0`, depois `skill 0 0 1 0 1` (medido 2026-09-24, idem).
  5. `(Select-String -Path .claude/tools/progresso_hook.py -Pattern "^(from|import) (rdo|backlog|telemetria|modelo|ocupacao|materializar|subprocess)\b" | Measure-Object).Count` e `(Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "print(" | Measure-Object).Count` → antes `0` e `0` (medido 2026-09-24), depois `0` e `0`.
  6. Igualdade da tabela da skill com a `### 4.1`, bloco cercado por conter barra invertida:

     ```
     python -c "import re;f=lambda p:[l.rstrip() for l in open(p,encoding='utf-8') if re.match(r'^\| .M-\d+b?. \|',l)];a=f('.claude/skills/scrum-master/SKILL.md');b=f('docs/plans/P-0748-tela-do-gerente.md');print('iguais',sum(x==y for x,y in zip(a,b)),'de',len(a),len(b))"
     ```

     → antes `iguais 12 de 23 24` (medido 2026-09-24, depois de `DTG-48` mudar a `M-8` e a `M-17` e `DTG-49` mudar a `M-10` e inserir a `M-10b` na `### 4.1`; o `zip` desalinha a partir da `M-10b`), depois `iguais 24 de 24 24`.
- **Pronto quando:**
  - `stream de dados.arquivo de progresso` — *existe e é alimentado pela função do kit a cada transição do loop: guarda uma linha do repertório por transição, na ordem em que o loop as atravessa, gerada a partir do evento e não da memória do agente — nenhuma linha se perde por o condutor ter esquecido a forma —, e nada mais: nenhuma busca, leitura ou saída de comando, e nenhuma chamada feita dentro dos agentes despachados* — Verificação 1 (`TF-GER-27`, `TF-GER-28`, `TF-GER-29`), 3, 4, 5 e 6.
- **Fora do escopo desta tarefa:** a célula do `README.md` (`TLG-T5a`); a medida da notificação de queda de agente no regime `<agent-message>` (com a guarda `pendentes` fora do `Stop`, a entrada órfã não tira linha nenhuma); o recorte `--desde` do dossiê (`AE-4`, `AE-5`, `AE-11`, `TK-55`); propagação aos kits derivados (`DTG-8`).

### TLG-T3f — O estado do gancho não guarda chave que ninguém lê [Sonnet · esforço low · classe implementacao]
- **Status:** `done` · 2026-09-24
- **Objetivo:** O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo.
- **Fundamento:** `DTG-50` (consultor, acionamento 14), `AE-22`, `DTG-47`, `DTG-48`.
- **Depende de:** `TLG-T3e`
- **Operação do modelo:** `OP-3`
  - OP-3: O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo.
  - precisa de: stream de dados — Quem implementa recebe o loop do condutor — as transições que ele atravessa a cada tarefa e o que ele tem em mãos em cada uma —, a função do kit que gera a linha a partir do evento de cada transição, e o arquivo de progresso onde essa função grava. A ferramenta que roda os agentes e o painel que mostra o arquivo ficam como estão.; tarefa — Quem implementa lê dela o que preenche as mensagens: qual tarefa, o título dela, qual passo e o que o passo pede. Nada nela muda.; mente do agente — Quem implementa usa a intenção que o condutor já tem em mãos — o que ele pediu ao agente e o que o agente devolveu — como campo do evento que a função recebe. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo.
- **Camada e fronteira:** kit — `.claude/tools/progresso_hook.py` (uma instrução da regra 1 de `evento`), `tests/test_progresso_hook.py` (uma asserção nova em `TF-GER-2`) e **uma** linha da seção *Repertório de mensagens ao gerente* da `scrum-master` (`M-1`, cópia legível da `### 4.1`, que o consultor já mudou em `DTG-50`). Todo o resto fica como está.
- **Domínio:** *chave sem leitor* = chave do estado próprio (`.claude/estado/progresso-estado.json`) que o gancho grava e que nenhum código do kit lê; `encerrada` ficou assim com `TLG-T3e` (o `Stop` deixou de gravá-la `True` e de lê-la, `DTG-48`): só a regra 1 a grava, sempre `False` (`AE-22`). A chave que já está no `progresso-estado.json` da sessão corrente fica lá, inerte, até o `session_id` mudar (o estado se reinicia); ninguém a lê.
- **Arquivos-alvo:**
  - `.claude/tools/progresso_hook.py:250` — a instrução estado_loop["encerrada"] = False da regra 1 (única no arquivo)
  - `tests/test_progresso_hook.py:127` — a asserção estado_loop["aberta"] is True de test_tf_ger_2_tarefa_escolhida_primeira_da_sessao; a nova entra logo depois dela
  - `.claude/skills/scrum-master/SKILL.md:328` — a linha da tabela que começa por | `M-1` | (única; localizar pelo texto)
- **Contratos/classes:** assinaturas e `FRASES` inalteradas. Regra 1: sai a linha `estado_loop["encerrada"] = False`; a `estado_loop["aberta"] = True` antes dela fica.
- **Texto novo, literal:** na `scrum-master`, a linha que começa por `` | `M-1` | `` passa a ser, inteira, a linha de mesmo início da `### 4.1` do plano (copiar do plano, não redigitar).
- **Passos:**
  1. Rodar a Verificação 1, 3 e 4 e anotar (contingências 1 e 2).
  2. Apagar a instrução do gancho (`Contratos/classes`).
  3. Inserir a asserção de `Testes`.
  4. Trocar a linha `M-1` da skill (`Texto novo, literal`).
  5. Rodar a Verificação 1 a 5.
- **Restrições desta tarefa:** `I-3` — nenhum comando, marcador ou flag novo do condutor; `I-11` — o gancho segue sem imprimir e saindo sempre `0`; `DTG-36` — `FRASES` não muda; `AE-10` — nenhum passo nem verificação roda `progresso_hook.py` contra o `.claude/estado/` real; `I-7` — o total de `pytest tests/` não cai.
- **Não fazer:** não editar outra instrução do gancho; não apagar nem reescrever `.claude/estado/progresso.txt` ou `progresso-estado.json`; não editar outra linha da skill, a `### 4.1` do plano nem o `README.md` (é `TLG-T5a`); não editar `modelo.py`, `.claude/projecoes.json` nem `.claude/settings.json`; não alterar outra asserção dos `TF`.
- **Contingências:**
  1. se `python -m pytest tests/test_progresso_hook.py -q` antes da edição não sai `32 passed` → parar e sinalizar `blocked` razão `dependencia`, devolvendo a linha impressa;
  2. se a Verificação 3 antes da edição não imprime `encerrada 1 1`, ou a 4 `iguais 23 de 24 24` → parar e sinalizar `blocked` razão `premissa`, devolvendo a linha impressa e a saída de `grep -rn "encerrada" .claude/tools .claude/skills`;
  3. se `python -m pytest tests/ -q` reduz o total por teste **fora** de `tests/test_progresso_hook.py` → parar e sinalizar `blocked` razão `dependencia` com o nome do teste.
- **Testes:** `tests/test_progresso_hook.py`. Asserção nova, e só ela: `TF-GER-2` — logo depois de `assert estado_loop["aberta"] is True` (linha 127), `assert "encerrada" not in estado_loop`. Nenhuma função nova. Medido pelo consultor em 2026-09-24 numa cópia temporária: com a asserção e o gancho da árvore, `1 failed, 31 passed` (`TF-GER-2`); com a asserção, o gancho sem a instrução e a skill trocada, `32 passed`. Suítes: `python -m pytest tests/test_progresso_hook.py -q`; `python -m pytest tests/ -q`.
- **Verificação:**
  1. `python -m pytest tests/test_progresso_hook.py -q` → antes `32 passed` (medido 2026-09-24 pelo consultor), depois `32 passed`.
  2. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` = total re-medido no despacho (medido 2026-09-24, acionamento 14: `312 passed`); o total não muda.
  3. Contagens de `encerrada` no gancho e na skill, bloco cercado (colar numa sessão PowerShell na raiz):

     ```
     "encerrada " + ((@('.claude/tools/progresso_hook.py','.claude/skills/scrum-master/SKILL.md') | ForEach-Object { (Select-String -SimpleMatch -Path $_ -Pattern 'encerrada' | Measure-Object).Count }) -join ' ')
     ```

     → antes `encerrada 1 1`, depois `encerrada 0 0` (medido 2026-09-24 em `powershell` 5.1 e `pwsh`, na árvore e numa cópia com a mudança).
  4. Igualdade da tabela da skill com a `### 4.1`, bloco cercado por conter barra invertida:

     ```
     python -c "import re;f=lambda p:[l.rstrip() for l in open(p,encoding='utf-8') if re.match(r'^\| .M-\d+b?. \|',l)];a=f('.claude/skills/scrum-master/SKILL.md');b=f('docs/plans/P-0748-tela-do-gerente.md');print('iguais',sum(x==y for x,y in zip(a,b)),'de',len(a),len(b))"
     ```

     → antes `iguais 23 de 24 24` (medido 2026-09-24, depois de `DTG-50` mudar a `M-1` da `### 4.1`), depois `iguais 24 de 24 24`.
  5. `(Select-String -Path .claude/tools/progresso_hook.py -Pattern "^(from|import) (rdo|backlog|telemetria|modelo|ocupacao|materializar|subprocess)\b" | Measure-Object).Count` e `(Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "print(" | Measure-Object).Count` → antes `0` e `0`, depois `0` e `0`.
- **Pronto quando:**
  - `stream de dados.arquivo de progresso` — *existe e é alimentado pela função do kit a cada transição do loop: guarda uma linha do repertório por transição, na ordem em que o loop as atravessa, gerada a partir do evento e não da memória do agente — nenhuma linha se perde por o condutor ter esquecido a forma —, e nada mais: nenhuma busca, leitura ou saída de comando, e nenhuma chamada feita dentro dos agentes despachados* — Verificação 1 (`TF-GER-2`), 3 e 4.
- **Fora do escopo desta tarefa:** a chave já gravada no `progresso-estado.json` da sessão corrente (inerte; sai com o reinício por sessão); a célula do `README.md` (`TLG-T5a`); o recorte `--desde` do dossiê (`AE-4`, `AE-5`, `AE-11`, `TK-55`); propagação aos kits derivados (`DTG-8`).

### TLG-T5a — A célula da scrum-master na tabela de skills volta a dizer quando a janela encerra [Sonnet · esforço low · classe redacao]
- **Status:** `done` · 2026-09-24
- **Objetivo:** O mantenedor da porta de entrada do repositório reescreve a descrição pública de como o dono acompanha a execução — o painel fora da extensão e como se lê a linha de cada passo —, e essa própria tarefa corre pelo loop já modificado, com o dono lendo nesse painel o fluxo em linguagem humana e dando o aceite final.
- **Fundamento:** `DTG-41` (c), `DTG-44`, `DTG-48`, `AE-15`, `I-9`, `F-15`.
- **Depende de:** `TLG-T3f`
- **Operação do modelo:** `OP-5`
  - OP-5: O mantenedor da porta de entrada do repositório reescreve a descrição pública de como o dono acompanha a execução — o painel fora da extensão e como se lê a linha de cada passo —, e essa própria tarefa corre pelo loop já modificado, com o dono lendo nesse painel o fluxo em linguagem humana e dando o aceite final.
  - precisa de: stream de dados — Quem implementa recebe o loop do condutor — as transições que ele atravessa a cada tarefa e o que ele tem em mãos em cada uma —, a função do kit que gera a linha a partir do evento de cada transição, e o arquivo de progresso onde essa função grava. A ferramenta que roda os agentes e o painel que mostra o arquivo ficam como estão.; tela do monitor — Quem implementa não mexe nela: o dono abre o painel e só o observa, na validação do fim. A sonda do começo foi feita no painel da extensão, e foi o que ela viu que tirou a tela de lá.
- **Camada e fronteira:** documentação pública (`README.md`): um trecho da célula de descrição da linha `scrum-master` na tabela de skills. Nada mais.
- **Domínio:** *célula da `scrum-master`* = a linha da tabela de skills do `README.md` que começa por `` | `scrum-master` | Ponto de entrada da execução de backlog ``; o complemento `pelo fim do plano ou pela condição de contexto` rege `encerra a janela` (é o texto do `HEAD`), e a `TLG-T5` o deixou regendo `lê no painel` (`AE-15`).
- **Arquivos-alvo:**
  - `README.md:841` — a linha da tabela de skills da scrum-master, que contém encerra a janela; a cada transição (única no arquivo, medida 2026-09-24; localizar pelo texto)
- **Contratos/classes:** nenhum código.
- **Texto novo, literal:** na linha `README.md:841`, substituir o trecho `encerra a janela; a cada transição, um gancho do kit gera a linha em linguagem humana que o gerente lê no painel do arquivo de progresso pelo fim do plano ou pela condição de contexto.` por `encerra a janela pelo fim do plano ou pela condição de contexto; a cada transição, um gancho do kit gera a linha em linguagem humana que o gerente lê no painel do arquivo de progresso.` — o resto da linha, antes e depois do trecho, fica.
- **Passos:**
  1. Substituir o trecho pelo texto dado.
  2. Rodar a Verificação 1 a 4.
- **Restrições desta tarefa:** `I-9` — o `check-readme.ps1` sai `0` com as mesmas contagens; só esta edição.
- **Não fazer:** não editar outra linha do `README.md` nem outra célula da tabela; não reescrever a cláusula do gancho; não tocar skill, agente, instrumento ou configuração.
- **Contingências:**
  1. se `(Select-String -SimpleMatch -Path README.md -Pattern "progresso pelo fim do plano" | Measure-Object).Count` não for `1` antes da edição → parar e sinalizar `blocked` razão `premissa` com a saída de `grep -n "pelo fim do plano" README.md`;
  2. se `check-readme.ps1` sair diferente de `0` → parar e sinalizar `blocked` razão `premissa` com a linha impressa.
- **Testes:** nenhum TF; guarda: `pwsh -NoProfile -File .claude/checks/check-readme.ps1`.
- **Verificação:**
  1. `pwsh -NoProfile -File .claude/checks/check-readme.ps1; $LASTEXITCODE` → `check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida; frases de contagem de 'Os guardrails' conferidas: 'regras mínimas obrigatórias'=True, 'regras falham como teste executável'=True.` e `0` (medido 2026-09-24 antes da edição; a edição não muda contagem).
  2. `(Select-String -SimpleMatch -Path README.md -Pattern "progresso pelo fim do plano" | Measure-Object).Count` → antes `1` (medido 2026-09-24), depois `0`.
  3. `(Select-String -SimpleMatch -Path README.md -Pattern "encerra a janela pelo fim do plano ou pela condição de contexto; a cada transição" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`.
  4. `(Select-String -SimpleMatch -Path README.md -Pattern "gera a linha em linguagem humana" | Measure-Object).Count` → antes `1` (medido 2026-09-24), depois `1`.
- **Pronto quando:** `stream de dados.descrição pública` — *a porta de entrada diz ao leitor que a execução se acompanha num painel fora da extensão, que mostra o arquivo de progresso com uma linha em linguagem humana a cada passo; diz como abrir esse painel e mostra como a linha se lê* — Verificação 2, 3 e 4 (a célula deixa de dizer que o gerente lê o painel "pelo fim do plano").
- **Fora do escopo desta tarefa:** o parágrafo **O que é.** da `## 6` (entregue por `TLG-T5`); o gancho (`TLG-T3c`); propagação aos kits derivados (`DTG-8`).

### TLG-T3g — O painel reconhece o retorno do agente com o `%` ou o colchete a mais [Sonnet · esforço low · classe implementacao]
- **Status:** `done` · 2026-09-24
- **Objetivo:** O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo.
- **Fundamento:** `DTG-51` (consultor, acionamento 15), `AE-24`, `AE-14`, `DTG-40`, `DTG-47`.
- **Depende de:** `TLG-T5a`
- **Operação do modelo:** `OP-3`
  - OP-3: O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo.
  - precisa de: stream de dados — Quem implementa recebe o loop do condutor — as transições que ele atravessa a cada tarefa e o que ele tem em mãos em cada uma —, a função do kit que gera a linha a partir do evento de cada transição, e o arquivo de progresso onde essa função grava. A ferramenta que roda os agentes e o painel que mostra o arquivo ficam como estão.; tarefa — Quem implementa lê dela o que preenche as mensagens: qual tarefa, o título dela, qual passo e o que o passo pede. Nada nela muda.; mente do agente — Quem implementa usa a intenção que o condutor já tem em mãos — o que ele pediu ao agente e o que o agente devolveu — como campo do evento que a função recebe. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo.
- **Camada e fronteira:** kit — `.claude/tools/progresso_hook.py` (dois padrões de `de_volta`), `tests/test_progresso_hook.py` (duas asserções novas, em `TF-GER-6` e `TF-GER-7`) e **duas** linhas da seção *Repertório de mensagens ao gerente* da `scrum-master` (`M-4` e `M-7`, cópia legível da `### 4.1`, que o consultor já mudou em `DTG-51`). Todo o resto fica como está.
- **Domínio:** *variação inócua* = caractere a mais na primeira linha do retorno de agente que não muda o que ela diz: o `%` depois do percentual do revisor (`AE-24`: `TLG-T5a aprovado 100% bloqueante=nenhuma`, medido no painel) e o colchete de opcional em volta de `pendencia=` do executor (`AE-14`: `TLG-T4a review [pendencia=...]`, medido no painel). Hoje as duas formas caem na `M-16` genérica, com a linha crua e a sigla; depois, dão a `M-7` e a `M-4`. A gramática dos agentes (`pantonic-reviewer.md:131`, passo 4 da `scrum-master`) fica como está: quem lê tolera, quem escreve segue a forma exata. Prosa **depois** da primeira linha (`AE-23`) já não afeta o painel, porque `de_volta` lê só a primeira linha não vazia.
- **Arquivos-alvo:**
  - `.claude/tools/progresso_hook.py:187` — o padrão de `re.match` da `M-4` em `de_volta` (único no arquivo)
  - `.claude/tools/progresso_hook.py:195` — o padrão de `re.match` da `M-7` em `de_volta` (único no arquivo)
  - `tests/test_progresso_hook.py:269` — test_tf_ger_6_agente_de_volta_executor; a asserção nova entra depois da última
  - `tests/test_progresso_hook.py:286` — test_tf_ger_7_agente_de_volta_revisor; a asserção nova entra depois da única
  - `.claude/skills/scrum-master/SKILL.md:332` — a linha da tabela que começa por | `M-4` | (única; localizar pelo texto)
  - `.claude/skills/scrum-master/SKILL.md:336` — a linha da tabela que começa por | `M-7` | (única; localizar pelo texto)
- **Contratos/classes:** assinaturas e `FRASES` inalteradas. Em `de_volta`, dois padrões mudam, e só eles:
  - `M-4`: `r"^(\S+) review(?:\s+pendencia=(.*))?$"` → `r"^(\S+) review(?:\s+\[?pendencia=(.*?)\]?)?$"`
  - `M-7`: `r"^(\S+) (\S+) (\d+) bloqueante=(.*)$"` → `r"^(\S+) (\S+) (\d+)%? bloqueante=(.*)$"`

  Medido pelo consultor em 2026-09-24 com `de_volta` do gancho novo: `X review pendencia=a]b` → `review — a]b.`; `X review [pendencia=a b]` → `review — a b.`; `X review` → `review — sem pendência.`; `X aprovado 100% bloqueante=nenhuma` → `aprovado 100%, bloqueante nenhuma.`; `X aprovado 100%% bloqueante=nenhuma` → `M-16`.
- **Texto novo, literal:** na `scrum-master`, as linhas que começam por `` | `M-4` | `` e por `` | `M-7` | `` passam a ser, inteiras, as linhas de mesmo início da `### 4.1` do plano (copiar do plano, não redigitar).
- **Passos:**
  1. Rodar a Verificação 1, 3 e 4 e anotar (contingências 1 e 2).
  2. Trocar os dois padrões do gancho (`Contratos/classes`).
  3. Inserir as duas asserções de `Testes`.
  4. Trocar as linhas `M-4` e `M-7` da skill (`Texto novo, literal`).
  5. Rodar a Verificação 1 a 5.
- **Restrições desta tarefa:** `I-3` — nenhum comando, marcador ou flag novo do condutor; `I-11` — o gancho segue sem imprimir e saindo sempre `0`; `DTG-36` — `FRASES` não muda; `AE-10` — nenhum passo nem verificação roda `progresso_hook.py` contra o `.claude/estado/` real; `I-7` — o total de `pytest tests/` não cai.
- **Não fazer:** não editar outra instrução do gancho; não editar `.claude/agents/pantonic-reviewer.md`, `.claude/agents/pantonic-executor.md` nem o passo 4 da `scrum-master` (a gramática dos agentes não muda); não editar outra linha da skill, a `### 4.1` do plano nem o `README.md`; não apagar nem reescrever `.claude/estado/progresso.txt` ou `progresso-estado.json`; não alterar outra asserção dos `TF`.
- **Contingências:**
  1. se `python -m pytest tests/test_progresso_hook.py -q` antes da edição não sai `32 passed` → parar e sinalizar `blocked` razão `dependencia`, devolvendo a linha impressa;
  2. se a Verificação 3 antes da edição não imprime `tolera 0 0 0 0`, ou a 4 `iguais 22 de 24 24` → parar e sinalizar `blocked` razão `premissa`, devolvendo a linha impressa;
  3. se `python -m pytest tests/ -q` reduz o total por teste **fora** de `tests/test_progresso_hook.py` → parar e sinalizar `blocked` razão `dependencia` com o nome do teste.
- **Testes:** `tests/test_progresso_hook.py`. Asserções novas, e só elas; nenhuma função nova.
  - `TF-GER-6` — depois da asserção de `e3`:

    ```
        assert _volta_executor(tmp_path / "estado4", raiz, "TLG-T9 review [pendencia=uma coisa]") == (
            'Agente executor devolveu a tarefa "Um título de teste": review — uma coisa.'
        )
    ```

  - `TF-GER-7` — depois da asserção existente (a lista de duas linhas prova que o segundo retorno gerou linha própria):

    ```
        rodar(P(hook_event_name="PostToolUse", tool_name="Agent",
                tool_input={"subagent_type": "pantonic-reviewer"},
                tool_response={"content": [{"type": "text", "text": "TLG-T9 aprovado 100% bloqueante=nenhuma"}]}),
              estado, raiz)
        assert progresso(estado)[-2:] == [
            'Agente revisor devolveu a tarefa "Um título de teste": aprovado 100%, bloqueante nenhuma.'
        ] * 2
    ```

  Medido pelo consultor em 2026-09-24 numa cópia temporária: com as asserções e o gancho da árvore, `2 failed, 30 passed` (`TF-GER-6`, `TF-GER-7`); com as asserções, os dois padrões novos e a skill trocada, `32 passed`. Suítes: `python -m pytest tests/test_progresso_hook.py -q`; `python -m pytest tests/ -q`.
- **Verificação:**
  1. `python -m pytest tests/test_progresso_hook.py -q` → antes `32 passed` (medido 2026-09-24 pelo consultor), depois `32 passed`.
  2. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` = total re-medido no despacho (medido 2026-09-24, acionamento 15: `312 passed`); o total não muda.
  3. Contagens dos dois padrões tolerantes no gancho e na skill, bloco cercado (colar numa sessão PowerShell na raiz):

     ```
     "tolera " + ((@('.claude/tools/progresso_hook.py','.claude/skills/scrum-master/SKILL.md') | ForEach-Object { $f = $_; @('[?pendencia=', '(\d+)%? bloqueante') | ForEach-Object { (Select-String -SimpleMatch -Path $f -Pattern $_ | Measure-Object).Count } }) -join ' ')
     ```

     → antes `tolera 0 0 0 0`, depois `tolera 1 1 1 1` (medido 2026-09-24 em `powershell` 5.1 e `pwsh`, na árvore e numa cópia com a mudança).
  4. Igualdade da tabela da skill com a `### 4.1`, bloco cercado por conter barra invertida:

     ```
     python -c "import re;f=lambda p:[l.rstrip() for l in open(p,encoding='utf-8') if re.match(r'^\| .M-\d+b?. \|',l)];a=f('.claude/skills/scrum-master/SKILL.md');b=f('docs/plans/P-0748-tela-do-gerente.md');print('iguais',sum(x==y for x,y in zip(a,b)),'de',len(a),len(b))"
     ```

     → antes `iguais 22 de 24 24` (medido 2026-09-24, depois de `DTG-51` mudar a `M-4` e a `M-7` da `### 4.1`), depois `iguais 24 de 24 24`.
  5. `(Select-String -Path .claude/tools/progresso_hook.py -Pattern "^(from|import) (rdo|backlog|telemetria|modelo|ocupacao|materializar|subprocess)\b" | Measure-Object).Count` e `(Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "print(" | Measure-Object).Count` → antes `0` e `0`, depois `0` e `0`.
- **Pronto quando:**
  - `stream de dados.arquivo de progresso` — *existe e é alimentado pela função do kit a cada transição do loop: guarda uma linha do repertório por transição, na ordem em que o loop as atravessa, gerada a partir do evento e não da memória do agente — nenhuma linha se perde por o condutor ter esquecido a forma —, e nada mais: nenhuma busca, leitura ou saída de comando, e nenhuma chamada feita dentro dos agentes despachados* — Verificação 1 (`TF-GER-6`, `TF-GER-7`), 3 e 4.
- **Fora do escopo desta tarefa:** prosa depois da linha de retorno (`AE-23`, tíquete de disciplina do `pantonic-executor`); outras variações que nenhum painel mostrou; a gramática escrita dos agentes; propagação aos kits derivados (`DTG-8`).

### TLG-T3h — O painel dá uma linha a cada `status` do mesmo comando, e a skill cita o evento da volta em hand-back [Sonnet · esforço low · classe implementacao]
- **Status:** `done` · 2026-09-24
- **Objetivo:** O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo.
- **Fundamento:** `DTG-52` (consultor, acionamento 16), `AE-25`, `AE-26`, `AE-16`, `DTG-39`, `DTG-47`.
- **Depende de:** `TLG-T3g`
- **Operação do modelo:** `OP-3`
  - OP-3: O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo.
  - precisa de: stream de dados — Quem implementa recebe o loop do condutor — as transições que ele atravessa a cada tarefa e o que ele tem em mãos em cada uma —, a função do kit que gera a linha a partir do evento de cada transição, e o arquivo de progresso onde essa função grava. A ferramenta que roda os agentes e o painel que mostra o arquivo ficam como estão.; tarefa — Quem implementa lê dela o que preenche as mensagens: qual tarefa, o título dela, qual passo e o que o passo pede. Nada nela muda.; mente do agente — Quem implementa usa a intenção que o condutor já tem em mãos — o que ele pediu ao agente e o que o agente devolveu — como campo do evento que a função recebe. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo.
- **Camada e fronteira:** kit — `.claude/tools/progresso_hook.py` (a regra 2, `backlog.py status`), `tests/test_progresso_hook.py` (uma função nova, `TF-GER-30`) e **cinco** linhas da `scrum-master`: `M-4`, `M-7`, `M-9` e `M-16` da seção *Repertório de mensagens ao gerente* (cópia legível da `### 4.1`, que o consultor já mudou em `DTG-52`) e o bullet do painel em `## Guardrails`. Todo o resto fica como está.
- **Domínio:** (a) *status encadeado* = dois ou mais `backlog.py status <ID> <estado>` no mesmo comando `Bash` (`AE-25`). Hoje a regra 2 casa só o primeiro (`re.search`) e a linha do segundo se perde; depois, cada `status` do comando gera a linha dele, na ordem do comando. (b) *volta em hand-back* = o agente entrega com `handback` = `send`: o `PostToolUse` do `Agent` só grava `pendentes[agentId]`, e a linha de volta sai no `UserPromptSubmit` cujo `prompt` começa por `<agent-message from="<agentId>">` (`DTG-39`, regra 5b do gancho). O código já faz isso; a skill não o diz (`AE-26`).
- **Arquivos-alvo:**
  - `.claude/tools/progresso_hook.py:259` — o `re.search` de `backlog\.py status` na regra 2 e o `if m:` da linha seguinte (únicos no arquivo)
  - `tests/test_progresso_hook.py:1215` — fim do arquivo; a função nova entra depois da última
  - `.claude/skills/scrum-master/SKILL.md:332` — a linha da tabela que começa por | `M-4` | (única; localizar pelo texto)
  - `.claude/skills/scrum-master/SKILL.md:336` — a linha da tabela que começa por | `M-7` | (única; localizar pelo texto)
  - `.claude/skills/scrum-master/SKILL.md:338` — a linha da tabela que começa por | `M-9` | (única; localizar pelo texto)
  - `.claude/skills/scrum-master/SKILL.md:349` — a linha da tabela que começa por | `M-16` | (única; localizar pelo texto)
  - `.claude/skills/scrum-master/SKILL.md:369` — o bullet de `## Guardrails` que começa por `- O gerente acompanha a execução num painel` (único)
- **Contratos/classes:** assinaturas, `FRASES` e o corpo da regra 2 inalterados. Só a abertura da regra 2 muda — duas linhas viram uma, e o corpo, que já está no recuo do `for`, fica como está:

  ```
          m = re.search(r"backlog\.py status (\S+) ([a-z-]+)", cmd)
          if m:
  ```
  →
  ```
          for m in re.finditer(r"backlog\.py status (\S+) ([a-z-]+)", cmd):
  ```

  Medido pelo consultor em 2026-09-24 numa cópia temporária: o `diff` com a árvore dá só `259,260c259`.
- **Texto novo, literal:** na `scrum-master`, (1) as linhas que começam por `` | `M-4` | ``, `` | `M-7` | ``, `` | `M-9` | `` e `` | `M-16` | `` passam a ser, inteiras, as linhas de mesmo início da `### 4.1` do plano (copiar do plano, não redigitar); (2) no bullet de `## Guardrails` que começa por `- O gerente acompanha a execução num painel`, o trecho `` (eventos `PreToolUse`, `PostToolUse` e `Stop`) `` passa a ser `` (eventos `PreToolUse`, `PostToolUse`, `UserPromptSubmit` — a volta do agente que entrega em hand-back, `DTG-39` — e `Stop`) ``. Editar com `Edit`, preservando o fim de linha `CRLF` da cópia de trabalho.
- **Passos:**
  1. Rodar a Verificação 1, 3 e 4 e anotar (contingências 1 e 2).
  2. Trocar a abertura da regra 2 do gancho (`Contratos/classes`).
  3. Inserir o `TF-GER-30` de `Testes`.
  4. Trocar as cinco linhas da skill (`Texto novo, literal`).
  5. Rodar a Verificação 1 a 5.
- **Restrições desta tarefa:** `I-3` — nenhum comando, marcador ou flag novo do condutor; `I-11` — o gancho segue sem imprimir e saindo sempre `0`; `DTG-36` — `FRASES` não muda; `AE-10` — nenhum passo nem verificação roda `progresso_hook.py` contra o `.claude/estado/` real; `I-7` — o total de `pytest tests/` não cai.
- **Não fazer:** não editar outra instrução do gancho (a regra 3, `review_evidence.py`, segue com `re.search`: um só `--tarefa` por comando); não editar outra linha da skill, a `### 4.1` do plano nem o `README.md`; não apagar nem reescrever `.claude/estado/progresso.txt` ou `progresso-estado.json`; não alterar asserção de outro `TF`.
- **Contingências:**
  1. se `python -m pytest tests/test_progresso_hook.py -q` antes da edição não sai `32 passed` → parar e sinalizar `blocked` razão `dependencia`, devolvendo a linha impressa;
  2. se a Verificação 3 antes da edição não imprime `conta 0 1 0`, ou a 4 `iguais 20 de 24 24` → parar e sinalizar `blocked` razão `premissa`, devolvendo a linha impressa;
  3. se `python -m pytest tests/ -q` reduz o total por teste **fora** de `tests/test_progresso_hook.py` → parar e sinalizar `blocked` razão `dependencia` com o nome do teste.
- **Testes:** `tests/test_progresso_hook.py`. Uma função nova, no fim do arquivo, com o separador de comentário dos outros `TF`:

  ```
  # --- TF-GER-30 ----------------------------------------------------------------------


  def test_tf_ger_30_dois_status_no_mesmo_comando(estado, raiz):
      rodar(payload_next(
          "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
          "- **Objetivo:** Fazer x.\n"
      ), estado, raiz)

      antes = len(progresso(estado))
      p1 = P(hook_event_name="PreToolUse", tool_name="Bash", tool_input={"command": (
          "python .claude/tools/backlog.py status TLG-T9 done && "
          "python .claude/tools/backlog.py status TLG-T10 in-progress"
      )})
      rodar(p1, estado, raiz)
      assert progresso(estado)[antes:] == [
          'Scrum master vai fechar a tarefa "Um título de teste" como done: registrar estado, RDO e telemetria.',
          'Tarefa "Outro título": gates aprovados; vou materializar in-progress e gravar o ponto de partida.',
      ]
  ```

  Medido pelo consultor em 2026-09-24 numa cópia temporária: com o `TF-GER-30` e o gancho da árvore, `1 failed, 32 passed` (a lista sai só com a linha do primeiro `status`); com a abertura nova e a skill trocada, `33 passed`. Suítes: `python -m pytest tests/test_progresso_hook.py -q`; `python -m pytest tests/ -q`.
- **Verificação:**
  1. `python -m pytest tests/test_progresso_hook.py -q` → antes `32 passed` (medido 2026-09-24 pelo consultor), depois `33 passed`.
  2. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` = total re-medido no despacho (medido 2026-09-24, acionamento 16: `312 passed`); depois `<N>+1`.
  3. Contagens (linhas) de `re.finditer(r"backlog` e de `re.search(r"backlog\.py status` no gancho e de `UserPromptSubmit` na skill, bloco cercado (colar numa sessão PowerShell na raiz):

     ```
     "conta " + ((@(@('.claude/tools/progresso_hook.py','re.finditer(r"backlog'),@('.claude/tools/progresso_hook.py','re.search(r"backlog\.py status'),@('.claude/skills/scrum-master/SKILL.md','UserPromptSubmit')) | ForEach-Object { (Select-String -SimpleMatch -Path $_[0] -Pattern $_[1] | Measure-Object).Count }) -join ' ')
     ```

     → antes `conta 0 1 0`, depois `conta 1 0 5` (medido 2026-09-24 em `powershell` 5.1 e `pwsh`, na árvore e numa cópia com a mudança).
  4. Igualdade da tabela da skill com a `### 4.1`, bloco cercado por conter barra invertida:

     ```
     python -c "import re;f=lambda p:[l.rstrip() for l in open(p,encoding='utf-8') if re.match(r'^\| .M-\d+b?. \|',l)];a=f('.claude/skills/scrum-master/SKILL.md');b=f('docs/plans/P-0748-tela-do-gerente.md');print('iguais',sum(x==y for x,y in zip(a,b)),'de',len(a),len(b))"
     ```

     → antes `iguais 20 de 24 24` (medido 2026-09-24, depois de `DTG-52` mudar a `M-4`, a `M-7`, a `M-9` e a `M-16` da `### 4.1`), depois `iguais 24 de 24 24`.
  5. `(Select-String -Path .claude/tools/progresso_hook.py -Pattern "^(from|import) (rdo|backlog|telemetria|modelo|ocupacao|materializar|subprocess)\b" | Measure-Object).Count` e `(Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "print(" | Measure-Object).Count` → antes `0` e `0`, depois `0` e `0`.
- **Pronto quando:**
  - `stream de dados.arquivo de progresso` — *existe e é alimentado pela função do kit a cada transição do loop: guarda uma linha do repertório por transição, na ordem em que o loop as atravessa, gerada a partir do evento e não da memória do agente — nenhuma linha se perde por o condutor ter esquecido a forma —, e nada mais: nenhuma busca, leitura ou saída de comando, e nenhuma chamada feita dentro dos agentes despachados* — Verificação 1 (`TF-GER-30`), 3 e 4.
- **Fora do escopo desta tarefa:** `review_evidence.py` repetido no mesmo comando (nenhum caso medido); prosa depois da linha de retorno (`AE-23`); a docstring de `tests/test_progresso_hook.py`, que já cita os quatro eventos; propagação aos kits derivados (`DTG-8`).

---

## 6. Ordem de execução

Grafo linear, nada roda em paralelo. Até `TLG-T2`, a ordem das operações (`DTG-13`); de `TLG-T3` a
`TLG-T4`, a da rodada 1 (`DTG-20`); daí em diante, a da rodada 2 (`DTG-37`):

```
Marco 1 (go) → TLG-T1 → Marco 2 (go, v2 aceita) → TLG-T2 → TLG-T3 → TLG-T2a → TLG-T4 → [DTG-29: Marco 3 antecipado, v3 pendente] → TLG-T3a → TLG-T2b → TLG-T3b → TLG-T4a → TLG-T5 (= Marco 3, promove a v3) → [veredito do dono; v4 da ## 1A] → TLG-T3c → TLG-T3d → TLG-T5a
```

*(consultor, `DTG-48`)* O dono desfez a premissa estratégica de `DTG-46` (`DTG-47`: o aceite foi de forma; corrigir
todo desvio mapeado). Fila: `TLG-T3e` (`OP-3`, rota B: `M-17` e `M-8` dizem só o que o gancho vê) → `TLG-T5a` →
relatório de encerramento, com o aceite de confiabilidade e a versão 4 pendente da `## 1A`. *(consultor, `DTG-49`)* O
`TLG-T3e` absorve também a `M-10` (`AE-21`); fila inalterada. *(consultor, `DTG-50`)* `TLG-T3e` `done`; a chave
`encerrada` sem leitor (`AE-22`) vira o corretivo `TLG-T3f` (`OP-3`), antes de `TLG-T5a`: fila `TLG-T3f` → `TLG-T5a` → relatório. *(consultor, `DTG-51`)* `TLG-T3f` e `TLG-T5a` `done`; o `%` do revisor (`AE-24`) e o colchete do executor (`AE-14`) viram o corretivo `TLG-T3g` (`OP-3`): fila `TLG-T3g` → relatório. *(consultor, `DTG-52`)* `TLG-T3g` `done`; a linha que se perde com dois `status` no mesmo comando (`AE-25`) e o `UserPromptSubmit` que a skill não cita (`AE-26`) viram o corretivo `TLG-T3h` (`OP-3`): fila `TLG-T3h` → relatório.

*(consultor, `DTG-46`)* O laudo da `TLG-T3d` (`AE-20`) mostrou que o sinal da `M-17`, inferido de eventos
compartilhados, não fecha sem decisão do dono: o loop para, e a escolha entre A, B e C sobe no relatório de encerramento.
`TLG-T5a` roda depois do corretivo que a escolha pedir.

*(consultor, `DTG-44`)* O laudo da `TLG-T3c` mapeou mais um caso de `M-17` falsa (`AE-19`); sob `DTG-42` ele vira
o corretivo `TLG-T3d` (`OP-3`), antes de `TLG-T5a`, para que o painel dela já prove o sinal novo.

*(consultor, `DTG-43`)* O veredito veio em `DTG-42`: forma aceita, confiabilidade não — o Marco 3 não
fecha antes de `TLG-T3c` e `TLG-T5a`; `TLG-T3c` passa a cobrir também `AE-17` (i) e `AE-18`. O aceite
de confiabilidade e a versão 4 da `## 1A`, ainda sem resposta do dono, vão ao relatório de
encerramento do plano, depois de `TLG-T5a`, com o painel das duas tarefas como corpus.

1. `TLG-T1` (`OP-1`), `TLG-T2` (`OP-2`), `TLG-T3` (`OP-3`), `TLG-T2a` (`OP-2`) e `TLG-T4` (`OP-4`) —
   `done` em 2026-09-24. O dono leu o painel durante a janela `TLG-T3`→`TLG-T4` e deu o veredito de
   `DTG-29` (*"convergindo"*, três correções); a versão 3 da `## 1A` e a rodada 2 absorvem as três.
2. `TLG-T3a` (`OP-3`, investigação) vai primeiro: instala a captura do payload dos ganchos, que
   enche com o ciclo do próprio card — o gancho carrega na mesma sessão (`AE-6`) — e com o de
   `TLG-T2b`. Não toca skill, `projecoes.json` nem `settings.json`.
3. `TLG-T2b` (`OP-2`, corretivo) depende de `TLG-T3a` pela ordem, não por insumo: é o segundo ciclo
   capturado, e leva à skill a tabela versão 3 da `### 4.1`, que `TLG-T3b` confere no `TF-GER-18`.
4. `TLG-T3b` (`OP-3`, corretivo) depende de `TLG-T2b` por insumo duplo: a captura (passo 1,
   contingências 1 a 3 — caminho nenhum leva a resposta do agente à função → `blocked premissa`,
   caso ao planejador por rodada tática, `R-9`) e a tabela da skill (`TF-GER-18`). Escreve a função,
   declara o `PreToolUse` e materializa; a partir dela as linhas do painel são geradas.
5. `TLG-T4a` (`OP-4`, corretivo) depende de `TLG-T3b`: até a função existir, o gancho antigo ainda
   copia as linhas marcadas e o painel não fica vazio; `TLG-T2b` e `TLG-T4a` editam a mesma skill e
   ficam em série.
6. **Nenhuma reabertura de sessão** entre os cards (`DTG-36`; `DTG-14` caída por `AE-6`). O dono
   abre o painel (`DTG-27`) antes do despacho de `TLG-T5`, na sessão que estiver conduzindo.
7. `TLG-T5` (`OP-5`) é a última e é o corpus do Marco 3 (`DTG-6`): o dono lê no painel a execução
   dela, com as linhas geradas por `TLG-T3b`, e no mesmo ato valida a versão 3 (`## 1A` → `## 1`).
8. *(consultor, `DTG-41`)* Depois do veredito do dono no Marco 3 — que também valida a versão 4
   pendente da `## 1A`, só a `OP-2` —, os dois corretivos: `TLG-T3c` (`OP-3`: título que sobrevive
   ao `SubagentStop`, comando encadeado, `texto_da_resposta`) e `TLG-T5a` (`OP-5`: a célula da
   `scrum-master` no `README.md`). `TLG-T5a` roda depois de `TLG-T3c` para que o dono veja no painel
   o gancho corrigido. Retroação que o veredito pedir volta ao consultor antes de `TLG-T3c`.

---

## 7. Fora de escopo (explícito)

- `PantonicMonitor` (`F-5`, `DTG-1`) — não é tela nem será adaptado.
- Modificar o harness do Claude Code, a extensão VS Code ou a forma como eles renderizam
  ferramenta (`DTG-2`, `I-1`).
- Expor o raciocínio interno do modelo (`DTG-7`).
- Propagar as mudanças de skill/agente aos kits derivados (`DTG-8`) — mora na rotina de
  sincronização do kit, tíquete próprio a abrir no fechamento deste plano.
- Filtrar saída de `pytest` — já resolvido pelo hook global (`F-4`).
- ~~Uma "tela" alternativa fora da extensão~~ — **entrou no escopo por `DTG-12`** (dono, Marco 2,
  2026-09-24; triagem `DTG-18`): deixa de ser exclusão.
- Enxugar as chamadas que o condutor faz no topo da extensão (o antigo `loop.py`, `DTG-4`,
  `DTG-11`) — retirado por `DTG-26`: o dono deixa de ler a extensão, e o arquivo de progresso exclui
  essas chamadas por construção.
- *(rodada 2)* Um instrumento `emitir` chamado pelo loop para gerar a linha (`DTG-30`, alternativa
  rejeitada): ainda dependeria de o condutor lembrar, que é o defeito medido em `AE-7`.
- *(rodada 2)* Mudar a gramática das linhas de retorno dos agentes (`F-29`) para facilitar a
  extração: a função lê a gramática vigente e cai em `M-16` fora dela (`DTG-34`); nenhum agente é
  reescrito (`mente do agente` inalterada, `### 1.3`).
- *(rodada 2)* Mudar o matcher `.*` dos ganchos para `Bash|Agent` — forma não medida (`DTG-31`); o
  filtro é feito dentro do script.

---

## 8. Riscos

| id | risco | resposta pré-decidida |
|---|---|---|
| `R-1` | A sonda mede `H-3 = não`: chamadas internas do subagente aparecem no topo da extensão, e o deslocamento (`DTG-4`) não limpa a tela | Marco 2 recebe veredito **`não`** para "bloqueio de saídas sem valor" dentro da extensão; o template e a emissão (`DTG-5`, `I-2`) **seguem** — são independentes; a alternativa única, tela em arquivo de progresso alimentado por hook `PostToolUse` (viável por `F-4`) lido em outro painel, sobe ao dono como **rodada de decisões** (escopo), com "registrar e não agir" como opção. Nenhum executor decide isso |
| `R-2` | **Retirado por `DTG-20` (2026-09-24): tratava a fusão em `loop.py`, que saiu com `DTG-26`.** Texto original: `Q-1` revela que o orquestrador precisa de chamadas no topo que não cabem num único comando do kit (por exemplo, `backlog.py next` + `rdo.py` + leitura do card) | O card de modificação do loop funde as chamadas num único comando do kit que devolve o que o orquestrador precisa em ≤ 40 linhas (`I-5`); se a fusão exigir verbo novo no instrumento, é card do plano, nunca achado adiado |
| `R-3` | O template preenchido de memória diverge do que os subagentes de fato devolvem (`Q-5`) | `Q-5` entra na campanha antes da Fase 3b; cada linha do template cita o campo da linha de retorno que a preenche — linha sem campo é defeito de autoria, não do executor |
| `R-4` | O Marco 3 reprova de **forma** (o dono queria outra leitura) — precedente do `P-0741` | O template vai ao Marco 1 como worked example preenchido (`DTG-5`); reprovação no Marco 3 retroage só ao card do template, por rodada de replanejamento tática |
| `R-5` | **Retirado por `DTG-20` (2026-09-24): tratava a fusão em `loop.py`, que saiu com `DTG-26`.** Texto original: O executor frio, ao editar a `scrum-master`, remove chamadas de gate (passo 3) para "limpar" | `Não fazer` do card: nenhum gate sai; gate migra para dentro do comando único ou de subagente, e a saída dele deixa de ser lida no topo |
| `R-6` | *(reescrito na rodada 2)* No Marco 3, o painel mostra linha faltando: um evento do loop não casou nenhuma regra de `evento()` (comando escrito de forma que a detecção da `### 4.1` não reconhece, por exemplo `backlog.py` chamado por caminho absoluto sem `backlog.py next` literal) ou a regra 5 caiu em `M-16` | A detecção é por substring (`"backlog.py next" in cmd`), robusta a prefixo de caminho; linha faltando ou genérica no Marco 3 é card corretivo `TLG-T3c` da `OP-3` por rodada tática do planejador (regra nova ou detecção alargada) — nenhuma operação nova, nenhum executor decide. *(Texto da versão 2, superado: o texto do condutor ainda não estava no transcript quando o gancho rodou.)* |
| `R-7` | Chamadas de ferramenta em paralelo disparam o gancho em processos simultâneos e a mesma linha entra duas vezes, ou o estado próprio é gravado por dois processos | A trava `progresso.lock` serializa leitura do estado, gravação da linha e gravação do estado (`TF-GER-17`); linha repetida no Marco 3 é card corretivo `TLG-T3c`, pela mesma rota do `R-6` |
| `R-8` | *(retirado na rodada 2: a `OP-3` versão 3 fala em "evento de transição do loop", que cobre `PreToolUse`, `PostToolUse` e `Stop`.)* Texto original: o modelador julga que o evento `Stop` (`DTG-25`) pede emenda da letra da `OP-3` | — |
| `R-9` | *(rodada 2)* A captura de `TLG-T3a` mostra que `tool_response` de `Agent` não cai em nenhuma das quatro formas que `texto_da_resposta` normaliza (`DTG-33` (i)) — por exemplo, o texto do subagente não vem no payload | `TLG-T3b` para na contingência 3 (`blocked premissa`, com tipo, chaves e amostra); a triagem leva ao planejador por rodada tática, que estende `texto_da_resposta` (forma nova) ou, se o texto não vem no payload, autora a alternativa de `M-4`/`M-7`/`M-9` lerem o transcript da sessão principal (`F-19`, rota que `TLG-T3` já tinha) — decisão do planejador, nunca do executor |
| `R-10` | *(rodada 2)* O `materializar.py` não aceita uma segunda entrada no mesmo evento `PreToolUse` (só eventos novos foram ensaiados, `F-21`): `apply` substitui o array e `ocupacao.py` some do `settings.json`, ou o `drift` não vê a entrada | Contingência 5 de `TLG-T3b` (`DTG-38`: contagens `1` e `3` no `settings.json`) → `blocked ferramenta`; a triagem abre card de `materializar.py` (instrumento do kit, tíquete próprio) e o `PreToolUse` do gancho espera por ele; as linhas de `PostToolUse` e `Stop` (`M-0`, `M-1`, `M-4`, `M-7`, `M-9`, `M-11`, `M-12`, `M-16`, `M-17`) já saem sem ele |

---

## 9. Achados da execução

- **AE-1** — `fechado` (`DTG-16`) · 2026-09-24 · `TLG-T1`, gatilho 3 (instrumento). `review_evidence.py` recusou o card no passo 6: rótulo `O que tem de existir ao final` fora da gramática de `rdo.py` (`pronto-quando` obrigatório). Origem no kit: `pantonic-planner.md:414-416` manda a `classe investigacao` trocar "Pronto quando" por *"o número ou fato que tem de existir ao final"*, e o parser não conhece o rótulo — o mesmo defeito volta em todo card de investigação escrito ao pé da letra. Junto: Verificação 1 e 2 com número absoluto inalcançável (o card contém os padrões) e Verificação 4 vácua (`.claude/settings.json` ignorado pelo git). **Inconclusivo:** a divergência doutrina × parser é do kit, sem card neste plano — tíquete no relatório de encerramento (a doutrina passa a dizer `Pronto quando (o fato que tem de existir ao final)`, ou `rdo.py` aprende o alias); o `--desde d75e7a6` do passo 6 recolhe no diff a árvore suja inteira (outros planos), não só a entrega — matéria do loop, não deste card.

- **AE-2** — `fechado` (`DTG-17`; a decisão de `R-1` segue viva em `DTG-12`, reservada, e em `TLG-T3` `blocked`) · 2026-09-24 · `TLG-T1`, regra `A8a` → `B1` (laudo `aprovado 100`, recomendação `escalar`). Pendência do laudo, transcrita: Marco 2 — a `### 2.2` mediu veredito de viabilidade `não` ((b) = as quatro chamadas no topo, `H-3` = não); pela `## 6` item 1 e `R-1`, a rodada de decisões sobre `R-1` sobe ao dono e a resposta entra em `DTG-12` (hoje vazia) antes de `TLG-T3`, que para em premissa sem ela; o veredito "viável" do condutor no Marco 1 fica contrariado pela medida. Achados de processo do mesmo laudo, com a rota que ele deu: (i) a linha (d) foi registrada `não` pela ausência da `statusLine` no fluxo transcrito pelo dono, sem anotação explícita dele — `H-4` segue sem medida; rota: confirmação de (d) pelo dono no Marco 2, junto com `R-1`; (ii) o passo 1 manda o agente editar `.claude/settings.json` e não previu a recusa do modo automático (o dono colou o bloco); rota: tíquete para a doutrina de autoria de cards de sonda (`pantonic-planner`) — contingência "permissão recusada → o dono cola o bloco literal e o agente confere `json ok`"; (iii) `Arquivos-alvo` na forma `<arquivo> §2.1` não é reconhecido como caminho pelo `review_evidence.py` e o plano saiu "alheio" no dossiê de evidência; rota: o mesmo tíquete do `AE-1`.

- **AE-3** — `fechado` (item (i) absorvido por `DTG-28` na rodada do planejador de 2026-09-24; item (ii) segue no tíquete de encerramento do `AE-1`) · 2026-09-24 · `TLG-T2`, achados de processo do laudo (`aprovado 100`, `seguir`), com a rota que ele deu. (i) A Verificação 3 ("segunda coluna `0`; primeira ≥ `24`") mede o `numstat` da skill contra `HEAD`, total que outras entregas movem — a skill tinha `19/23` não commitados antes do despacho; só foi verificável porque o despacho a releu como delta sobre a base re-medida (entrega: `+26/-0`, inserção pura). Rota: replanejamento do `P-0748` — a forma certa é o delta contra a base re-medida no despacho, e `TLG-T3`/`TLG-T4`, que tocam a mesma skill, herdam o defeito. (ii) O dossiê de evidência com `--desde d75e7a6` recolhe a árvore suja inteira e o trecho do arquivo-alvo trunca em 4000 caracteres dentro de hunks de outros planos, sem chegar à seção inserida; rota: o mesmo tíquete de encerramento do `AE-1`.

- **AE-4** — `aberto`, rota `TK-55` (confiabilidade de instrumento) · 2026-09-24 · `TLG-T3` (recorreu na `TLG-T2a`, mesmo recorte), achado de processo do laudo (`aprovado 100`, `seguir`). O recorte `--desde <ref>` capturado por `git stash create` no passo 4 da `scrum-master` só guarda arquivos rastreados: os ~110 não rastreados que já existiam antes do despacho aparecem em *Arquivos tocados* do dossiê de evidência, e 9 saem como *fora dos alvos e sem atribuição* — o revisor reconciliou por data de modificação. Não afeta a entrega.

- **AE-5** — `aberto`, rota `TK-55` (confiabilidade de instrumento) · 2026-09-24 · `TLG-T4`, achado de processo do laudo (`aprovado 100`, `seguir`). O trecho de diff de `.claude/skills/scrum-master/SKILL.md` no dossiê de evidência truncou em 4000 caracteres no meio do bullet `**Narra:**` do Passo 8: três das dez inserções só foram lidas abrindo o repositório. Candidato: teto do trecho por arquivo-alvo em `review_evidence.py`, ou recorte só dos hunks do `--desde`. No mesmo laudo, âncora envelhecida (`passagem-de-bastao/SKILL.md` "12-13" estava em 11-12, texto idêntico): **sem ação**, coberta pela re-derivação de âncora do gate de delegação.

- **AE-6** — `fechado` (`DTG-43`, sem ação: a linha narrada que esperava o próximo ato saiu com `DTG-30`/`DTG-36`, e o veredito do Marco 3, `DTG-42`, não a cita) · era `aberto`, rota Marco 3 (leitura do painel pelo dono, `I-6`) · 2026-09-24 · observação do condutor na `TLG-T4`: o gancho da `TLG-T3` carregou **nesta mesma sessão**, sem reabrir, e gravou em `.claude/estado/progresso.txt` as linhas narradas, sem o marcador. Comando que sai com erro não dispara `PostToolUse` (o harness emite outro evento); a linha narrada antes dele espera o próximo ato bem-sucedido ou o `Stop` — nada se perde e a ordem se mantém, mas a chegada ao painel atrasa um ato.

- **AE-7** — `fechado` — absorvido por `DTG-30`..`DTG-32` (rodada de replanejamento 2, `RP-2`: a linha passa a ser gerada pelo gancho no evento, `TLG-T3a`/`TLG-T3b`) · 2026-09-24 · janela `TLG-T3`→`TLG-T4`, observação do condutor: as linhas do repertório escritas durante a `TLG-T3` e a `TLG-T2a` **não chegaram** a `.claude/estado/progresso.txt` — foram escritas sem o marcador `[gerente] `, porque a regra só entrou na skill com a `TLG-T4`; só as linhas posteriores à `TLG-T4` foram gravadas. Fato medido do defeito da narração agêntica: a chegada da linha ao painel dependia de o condutor lembrar a forma.

- **AE-8** — `fechado` (`DTG-39`, consultor, acionamento 5) · 2026-09-24 · `TLG-T3b` `blocked · premissa` pela contingência 3: o `response` do `PostToolUse` `Agent` na captura, cortado em 2000 caracteres por contrato de `TLG-T3a`, não passa em `json.loads`, e a forma do valor não era legível dali. **Procedente no mérito:** medido no transcript, o `tool_response` do `Agent` cai na forma (c), mas o texto é o ponteiro do hand-back — o relatório do agente chega ao condutor como `queued_command` e dispara `UserPromptSubmit` na sessão principal. `M-4`/`M-7`/`M-9` nunca sairiam. Reparo: regra 5 grava `pendentes`, regra 5b nova lê o relatório no `UserPromptSubmit`, `TF-GER-15` com as formas medidas literais, `TF-GER-19` novo, contagens `3 → 4`. **Inconclusivo:** o disparo do `UserPromptSubmit` no hand-back está medido por inferência (o `modelo_por_fase` global aparece logo depois de três das seis entregas, as que casam palavra-chave dele, e em nenhum outro ponto além do prompt inicial), não por captura do payload; a prova direta é a primeira linha `M-4` que o painel mostrar na volta do executor de `TLG-T4a` (Marco 3, `I-6`). **Verificação que teria evitado:** a `TLG-T3a` capturar o `tool_response` sem truncar o campo que a sonda existia para medir, ou a `DTG-32` pedir a forma do **valor** e não só as chaves.

- **AE-9** — `fechado` com o `done` de `TLG-T3c` (2026-09-24, `aprovado 100`), card escrito em `DTG-41` (consultor, acionamento 7) (`DTG-40`; a do laudo era replanejamento) · 2026-09-24 · `TLG-T3b`, achado de processo do laudo (`ressalva 94`, `seguir com ressalva`, dimensão `rota` parcial). O fallback de tarefa corrente de `DTG-33` (iv) lê `.claude/estado/tarefa-corrente.json`, que o `telemetria_hook` apaga no `SubagentStop` do executor (`telemetria_hook.py:193`) — antes dos eventos de volta (regras 5/5b) e do despacho do revisor —, e a regra 3 (`M-5`) identifica a tarefa pelo `--tarefa` do comando sem alimentar o estado. Toda tarefa cujo `M-1` o gancho não viu (instalação no meio do ciclo, `session_id` novo por `/clear`) degrada `M-4`/`M-6`/`M-7`/`M-9` para `"(tarefa não identificada)"`. Medido ao vivo em `.claude/estado/progresso.txt` nesta janela. Reparo indicado pelo laudo: fonte do título que sobreviva ao `SubagentStop`, e `M-5` gravando tarefa e título no estado.

- **AE-10** — `fechado` com o `done` de `TLG-T3c` (2026-09-24, `aprovado 100`) (restrição e verificações do card, `DTG-41`) · 2026-09-24 · `TLG-T3b`, achado de processo do laudo. A Verificação 8 do card roda o gancho real com `session_id` `x` contra o `.claude/estado/` vivo, o que reinicia o estado próprio da sessão do loop (apaga `tarefa`, `aberta` e `pendentes`): a verificação destrói o stream que certifica. Reparo indicado pelo laudo: a V8 passa a usar pasta de estado temporária, ou fica restrita ao `TF-GER-12`.

- **AE-11** — `aberto`, rota `TK-55` (confiabilidade de instrumento, como `AE-4`/`AE-5`) · 2026-09-24 · `TLG-T3b`, achado de processo do laudo. O dossiê de evidência com recorte `--desde <commit>` listou como "fora dos alvos e sem atribuição" nove arquivos não rastreados de outros planos (mtime 09-22/09-23) e o `docs/ACIONAMENTOS_CONSULTOR.tsv` da triagem do consultor; o revisor reconciliou por mtime. Reparo indicado: o `review_evidence.py` exclui não rastreados anteriores ao despacho.

- **AE-12** — `fechado` com o `done` de `TLG-T3c` (2026-09-24, `aprovado 100`) (`TF-GER-1` e `TF-GER-9` estendidos, `DTG-41`) · 2026-09-24 · `TLG-T3b`, motivo da dimensão `rota` parcial do laudo. `texto_da_resposta` ganhou uma guarda `if partes` fora da semântica fechada do card: `texto_da_resposta({'content': []})` devolve `'{"content": []}'` e `texto_da_resposta([])` devolve `'[]'` (card: `''`), e o stream mostraria JSON cru ao dono em vez de `(sem texto)`. Desvio contido no arquivo-alvo, sem TF que o discrimine (`TF-GER-1` não cobre lista sem texto).

- **AE-13** — `fechado` (`DTG-40`, consultor, acionamento 6: escalada improcedente; a emenda à rubrica de criação de tarefa vai ao tíquete de encerramento do `AE-1`) · 2026-09-24 · `TLG-T4a` (`aprovado 100`, `seguir`), `pendencia=` do executor: `- **Ação:** antes=10 depois=10`. Não atribuível a arquivo fora dos alvos pelo `B0` (é valor de aceite do próprio alvo, que a Verificação 5 do card manda colar na linha de retorno — cujo único campo livre é `pendencia=`). O laudo aponta a escalada como espúria por construção: valor medido de aceite viajando em `pendencia=`; rota do laudo: replanejamento do `P-0748` e emenda à rubrica de criação de tarefa (§8) — valor de aceite não viaja em `pendencia=`.

- **AE-14** — `fechado` (`DTG-40`, consultor, acionamento 6: passo 4 da `scrum-master` com duas formas literais sem colchete; a `M-4` não muda) · 2026-09-24 · `TLG-T4a`, achado de doutrina do laudo. O passo 4 da `scrum-master` publica a gramática de retorno como `<tarefa> review [pendencia=<uma linha>]`, com colchete de meta-notação de opcional, e a `M-4` da mesma skill casa `^(\S+) review(?:\s+pendencia=(.*))?$`, que recusa o colchete literal. O executor da `TLG-T4a` devolveu `TLG-T4a review [pendencia=...]` (o despacho do condutor repetiu a gramática com colchete) e o painel mostrou a `M-16` genérica, com a linha crua e a sigla, em vez da `M-4`. Reparo indicado: fechar a gramática do passo 4 sem meta-notação ambígua, ou a `M-4` tolerar o colchete, com Verificação que exercite a forma literal.

- **AE-15** — `fechado` com o `done` de `TLG-T5a` (2026-09-24, `aprovado 100`), card escrito em `DTG-41` (consultor, acionamento 7; a rota do laudo era o mesmo corretivo) · 2026-09-24 · `TLG-T5` (`aprovado 100`, `seguir`), achado de dossiê do laudo. O literal do card para `README.md:831` substitui um trecho que não fecha a frase: a cláusula nova entra entre `encerra a janela` e o complemento `pelo fim do plano ou pela condição de contexto`, que passa a reger `lê no painel do arquivo de progresso` — a célula da `scrum-master` na tabela de skills sai com o sentido trocado. A execução aplicou o literal fielmente; a causa é do card (rubrica §8, critério xii(a)). Reparo indicado: literal que desloca a cláusula para depois de `pela condição de contexto`, ou a reescreve como frase própria, com a mesma guarda `check-readme.ps1`. Recorrência do `AE-11` no mesmo laudo (nove não rastreados de outros planos listados como sem atribuição; rota `TK-55`).

- **AE-16** — `fechado` com o `done` de `TLG-T3c` (2026-09-24, `aprovado 100`) (`DTG-41`, consultor, acionamento 7) · 2026-09-24 · `TLG-T5`, observação do condutor no Marco 3: o `M-5` da `TLG-T5` não chegou ao painel porque o condutor encadeou `backlog.py status TLG-T5 review` e `review_evidence.py` no mesmo comando `Bash`; a regra 2 do gancho casou o `status … review`, que não gera linha, e, por ser "a primeira que casa", a regra 3 nunca foi avaliada. O condutor classificou o caso como defeito de condução; a triagem o classifica como **defeito do gancho** — a skill não proíbe encadear, e o `R-6` já previa este caso (linha faltando → `TLG-T3c`). Medido numa cópia do gancho: o vigente não gera linha nenhuma para o encadeado, nem para `status <ID> in-progress;` com o `;` colado ao estado.

- **AE-17** — (i) `aberto` até o `done` de `TLG-T3c` (`DTG-42`: o dono manda corrigir; `DTG-43`: `M-17` só depois do relatório de encerramento); (ii) **reaberto** até o `done` de `TLG-T3e` (`DTG-47`: o aceite foi de forma, e a palavra "parada" é conteúdo; `DTG-48`: a `M-8` perde "a parada da") · era `fechado` sem ação (`DTG-42`: forma aceita) · era `aberto`, rota leitura do dono no Marco 3 (`R-4`: forma) · 2026-09-24 · consultor, lido em `.claude/estado/progresso.txt` no acionamento 7. (i) A `M-17` (*"Scrum master encerrou a janela"*) sai no `Stop`, que dispara a cada fim de turno do condutor: na linha 44 ela aparece e a janela segue na linha 45 (`M-11`) — o dono lê "encerrou" quando o condutor só parou para esperá-lo. (ii) A `M-8` diz *"recebe a parada da tarefa"* também quando o consultor é acionado por marco ou por laudo (linhas 42 e 53), sem parada nenhuma. **Inconclusivo:** nenhum dos dois derruba estado final da `## 1` sem a leitura do dono — se ele pedir, é corretivo de `OP-3` (frase e detecção), triado de novo pelo consultor; se não, fica registrado.

- **AE-18** — `fechado` com o `done` de `TLG-T3c` (2026-09-24, `aprovado 100`) (`DTG-43`) · 2026-09-24 · consultor, lido em `.claude/estado/progresso.txt:54` no acionamento 8. A volta do consultor do acionamento 7, que **não** classificou nada como estratégico, saiu no painel como `…: rota resolve; estratégico: `..` — a `M-9b` casa `estrategico=(.*)` em qualquer ponto do relatório, e o relatório citava a linha em prosa (*sem `estrategico=`*). O loop roteou certo (lê a linha logo abaixo de `rota=`); só o painel mentiu. Mesma classe do `AE-17` (i), que o dono mandou corrigir em `DTG-42`: linha que afirma o que não aconteceu.

- **AE-19** — `fechado` com o `done` de `TLG-T3d` (2026-09-24; os residuais seguem no `AE-20`) (`DTG-44`, consultor, acionamento 9: caso mapeado sob `DTG-42`, vai a card) · 2026-09-24 · `TLG-T3c` (`aprovado 100`, `seguir`), achado do laudo sobre a semântica fechada da `M-17`: a chave `relatorio` é gravada por **qualquer** `modelo.py show` do condutor com a janela aberta e só é limpa pelo `Stop`; um `modelo.py show` pedido pelo dono (ou rodado pelo condutor) no meio da janela faz o fim de turno seguinte gravar `Scrum master encerrou a janela` sem a janela ter encerrado — a mesma classe de linha que o `DTG-42` manda eliminar. A entrega seguiu o contrato à letra (o card declarou o comando como único uso no loop); o caso já constava como "não resolvido" no acionamento 8. Recorrência do `AE-11` no mesmo laudo (não rastreados sem diff contra o despacho; rota `TK-55`).

- **AE-20** — `fechado` com o `done` de `TLG-T3e` (2026-09-24, `aprovado 100`) (`DTG-47`: o dono desfez a premissa estratégica; `DTG-48`, consultor, acionamento 12: rota B, os dois residuais corrigidos) · era estratégico ao dono no relatório de encerramento (`DTG-46`, consultor, acionamento 11: opções A/B/C na `§3`) · 2026-09-24 · `TLG-T3d` (`aprovado 100`, recomendação `escalar`), pendência do laudo, verbatim: *"DTG-42 fechada só com agente em voo: show puro no meio da janela sem agente pendente ainda grava M-17 falsa, e órfã + parada sem next perde a M-17 real; a heurística é do card (Domínio/Contratos), a decisão de rota sob I-3 vai à triagem do consultor"*. Exercícios do revisor em pasta temporária: (a) `next` → `modelo.py show --plano …` sem flag → `Stop` → despacho do executor: o painel grava `Scrum master encerrou a janela; …` antes de `Agente executor recebe a tarefa…`, e o estado fica `aberta=False`/`encerrada=True` com a janela seguindo; (b) executor `a1` que cai sem volta + outros agentes com volta + `show` + `Stop` sem `next` no meio: nenhuma `M-17`, estado `aberta=True`, `relatorio=True`, `pendentes={a1}`. São os dois residuais que o `DTG-44` deixou como `inconclusivo`; sob `DTG-42` são casos mapeados de linha que afirma o que não aconteceu ou que se perde.

- **AE-21** — `fechado` com o `done` de `TLG-T3e` (2026-09-24, `aprovado 100`) (`DTG-49`, consultor, acionamento 13) · 2026-09-24 · condutor, lido em `.claude/estado/progresso.txt:74` na volta da `TLG-T3d` `blocked` (regra `A3b`): *"Scrum master vai fechar a tarefa "O painel só diz que a janela encerrou quando ela encerrou" como blocked: registrar estado, RDO e telemetria, e selecionar a próxima."* — nem RDO nem próxima aconteceram (linhas 75-77: consultor e redespacho da mesma tarefa). Mesma classe em `done`: `progresso.txt:83` diz "selecionar a próxima" e a janela parou em `86` sem `next`. Mapeado por leitura do gancho e medido numa cópia: a `M-10` de `blocked`/`cancelled` grava `tarefa_fechada`, e a `M-11`/`M-12` seguintes dizem "concluiu".

- **AE-22** — `fechado` com o `done` de `TLG-T3f` (2026-09-24, `aprovado 100`) (`DTG-50`, consultor, acionamento 14: desvio mapeado sob `DTG-47`, corretivo da `OP-3`) · 2026-09-24 · `TLG-T3e` (`aprovado 100`, `seguir`), achado do laudo: a chave `encerrada` do `progresso-estado.json` virou escrita sem leitor — a regra 1 grava `False`, nada grava `True` e nada em `.claude` a lê; o card mandou mantê-la (*"`encerrada = False` da regra 1 fica"*) e a linha `M-1` da `scrum-master` (e da `### 4.1`) ainda a documenta. Rota do laudo: corretivo da `OP-3` que tira a chave do gancho e da linha `M-1`. Recorrência do `AE-11` no mesmo laudo (rota `TK-55`).

- **AE-23** — `aberto`, rota `TK-79` (aberto no fechamento, 2026-09-24) (disciplina de retorno do `pantonic-executor`; fora das operações deste plano; confirmado no acionamento 15, `DTG-51`: não entra no `TLG-T3g`, porque o painel já lê só a primeira linha) · 2026-09-24 · observação do condutor em três despachos seguidos: `TLG-T5`, `TLG-T3e` e `TLG-T3f` devolveram a linha de retorno válida **seguida de prosa de relatório**, e o `TLG-T3f` o fez mesmo com o despacho proibindo por escrito (*"sem nenhuma prosa depois da linha"*). O loop leu a primeira linha e seguiu; o painel não foi afetado, porque o gancho lê só a primeira linha não vazia do hand-back. Pela `A2`, prosa no lugar da linha é retorno inválido; prosa **depois** da linha não está tipificada.

- **AE-24** — `fechado` com o `done` de `TLG-T3g` (2026-09-24, `aprovado 100`) (`DTG-51`, consultor, acionamento 15: a `M-7` e a `M-4` toleram o `%` e o colchete; a gramática dos agentes não muda) · 2026-09-24 · `TLG-T5a` (`aprovado 100`, `seguir`), observação do condutor, medida no painel: o revisor devolveu `TLG-T5a aprovado 100% bloqueante=nenhuma` — com `%`, fora da gramática do papel (`.claude/agents/pantonic-reviewer.md:131`: `<tarefa> <veredito> <percentual> bloqueante=<dimensão|nenhuma>`) —, a `M-7` (`^(\S+) (\S+) (\d+) bloqueante=(.*)$`) não casou e o painel gravou a `M-16` genérica com a linha crua e a sigla: `Agente revisor devolveu a tarefa "A célula da scrum-master…": TLG-T5a aprovado 100% bloqueante=nenhuma.` Mesma classe do `AE-14` (colchete do executor): a `M-4`/`M-7` só casam a forma exata, e um desvio de um caractere do agente degrada a linha do dono. O loop leu o veredito sem ambiguidade e fechou; o laudo traz `Percentual: 100%`.

- **AE-25** — `fechado` com o `done` de `TLG-T3h` (2026-09-24, `ressalva 94`) (`DTG-52`, consultor, acionamento 16: desvio mapeado sob `DTG-47`, corretivo da `OP-3`) · 2026-09-24 · redação do encerramento (`docs/OPERACOES_AS_IS_P-0748.md`, pendência nº 7), medido pelo redator numa pasta temporária: dois `backlog.py status` no mesmo comando `Bash` geram só a linha do primeiro. A regra 2 do gancho usa `re.search` (`progresso_hook.py:259`); o `AE-16`/`TLG-T3c` fechou o encadeamento `status` + `review_evidence.py` (regras 2 e 3 não excludentes), não o de dois `status`. Mesma classe do `AE-16`: linha que se perde. Medido pelo consultor com o `TF-GER-30` numa cópia: a árvore perde a linha do segundo `status`.
- **AE-26** — `fechado` com o `done` de `TLG-T3h` (2026-09-24, `ressalva 94`) (`DTG-52`) · 2026-09-24 · redação do encerramento, pendência nº 6: a tabela `## Repertório de mensagens ao gerente` da `scrum-master`, a `### 4.1` e o bullet do painel em `## Guardrails` dizem que as linhas de volta de agente vêm do `PostToolUse`, e o bullet lista só `PreToolUse`, `PostToolUse` e `Stop`; nenhum cita o `UserPromptSubmit`, por onde chega a volta do agente que entrega em hand-back (`DTG-39`, regra 5b do gancho). O código está certo; o texto de doutrina descreve o mecanismo de forma incompleta (`DTG-42`: informação não confiável). Medido: `UserPromptSubmit` na skill `0` linhas.
- **AE-27** — `fechado` (`DTG-52`, consultor, acionamento 16: cabeçalho reescrito) · 2026-09-24 · redação do encerramento, pendência nº 9: o `**Status:**` do cabeçalho do plano dizia `ready` com "próxima `TLG-T3a`", texto da rodada 2 que nenhum fechamento de tarefa atualizou (o `backlog.py status` troca só o estado entre crases). Agora diz a próxima real (`TLG-T3h`) e o que vem depois dela.
- **AE-28** — `aberto`, rota registro (sem efeito funcional; recolocação é ato mecânico de 21 linhas, sem card) · 2026-09-24 · `TLG-T3h` (`ressalva 94`, `seguir com ressalva`, dimensão `rota` parcial): o card fechou a posição do `TF-GER-30` no fim de `tests/test_progresso_hook.py`, e a entrega o inseriu entre `test_tf_cap_2_flag_desligado` e `test_tf_cap_3_barreira_agent_type`, partindo o grupo sob o separador `# --- TF-CAP-1..3`; não declarado na linha de retorno. No mesmo laudo, dois achados de evidência: alvos não rastreados saem como arquivo inteiro truncado, sem diff (rota: versionar gancho e teste no commit de marco, ato do dono) e não rastreados preexistentes listados como tocados (rota `TK-55`).

- **RP-1** — 2026-09-24 · rodada de replanejamento do planejador (`G-REPLAN`, rota `planejador` de `DTG-19`) · classificação: **técnica/tática**, fechada no mesmo contexto (`DTG-20`..`DTG-28`); o escopo mudou antes, por ato do dono (`DTG-12`), e a rodada só o decompôs. Causa-raiz na autoria: a Fase 1 da versão 1 deu como fato a tela como painel da extensão (`DTG-1`) e decompôs o bloqueio de saída sobre essa premissa, com a sonda (`TLG-T1`) apenas confirmando — quando a premissa caiu, o `TLG-T3` inteiro caiu junto. Verificação que teria evitado: a própria doutrina da Fase 1 ("decisão que escolhe mecanismo de plataforma exige sonda antes da recomendação") — a sonda existia, mas o card dependente foi autorado antes do resultado, em vez de partir o plano; classe já coberta pelo `pantonic-planner` (Fase 1, investigação vira tarefa e o dependente é a última tarefa), logo só esta entrada. O defeito de Verificação do `AE-3` (i) (`numstat` contra `HEAD`) também é classe coberta (régua de autoria, `TK-78b`) e fica absorvido por `DTG-28`.

- **RP-2** — 2026-09-24 · rodada de replanejamento 2 do planejador (`G-REPLAN`, rota `planejador` sobre `DTG-29`, versão 3 pendente da `## 1A`) · classificação: **estratégica, já decidida pelo dono** em `DTG-29` (função, agregação, frase da evidência); o técnico e o tático fechados aqui (`DTG-30`..`DTG-38`), sem rodada de decisões. Cards: `TLG-T3a` (investigação: captura do payload), `TLG-T2b`, `TLG-T3b`, `TLG-T4a`, `TLG-T5` reescrito; ordem `DTG-37`. **Causa-raiz na autoria:** a versão 2 e a rodada 1 descreveram o mecanismo pela mão do condutor — *"escreve, antes de agir"* (`OP-4` v2, `DTG-21`, `DTG-23`, `I-2`, `I-5`) — quando o pedido do dono na §0 era um **stream padronizado** (*"Template de mensagens possíveis de serem renderizadas"*, *"Modificação do stream de dados para renderização"*). A escolha do texto do agente como canal foi `DTG-2`, decidida na Fase 2 da versão 1 com a razão `F-1` (*"texto do agente é o único canal que a extensão renderiza inteiro"*). Quando `DTG-12` tirou a tela da extensão, a razão de `DTG-2` caiu — mas a rodada 1 (passo 3 do protocolo, "repor o fato que faltou") **carregou `DTG-2` sem reler a razão** e só remendou o canal com um marcador (`DTG-23`): decisão viva com razão órfã. O primeiro corpus real (`AE-7`) mostrou o ponto de falha que a razão órfã escondia: linha que depende da memória do agente se perde. **Verificação que teria evitado:** na rodada de replanejamento, toda decisão mantida tem a coluna *razão* relida contra as decisões novas; razão que cita fato ou decisão revogada na mesma rodada é **razão órfã**, e a decisão se re-decide ou se revoga no mesmo ato — nunca se carrega. Classe **nova** no protocolo do planejador: entra em `.claude/agents/pantonic-planner.md`, passo 3 da *Rodada de replanejamento*, no mesmo ato desta entrada. Segunda lição, já coberta (Fase 1, "pergunta que exige medir vira tarefa de investigação"): a forma de `tool_response` não é medível de dentro de um executor, e por isso a sonda é card próprio (`TLG-T3a`), não passo de abertura do card de implementação.
- **Notas de execução:**
  - 2026-09-24 `blocked` — espera o ato do dono sobre DTG-46 (AE-20)
