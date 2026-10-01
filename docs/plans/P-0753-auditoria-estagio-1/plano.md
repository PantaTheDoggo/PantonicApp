# P-0753 — Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor

**Data de origem:** 2026-09-27 · **Origem:** pedido do dono em dois atos de 2026-09-27 (transcritos na §0) ·
**Dossiê:** `docs/audits/AUDITORIA_ENCERRAMENTO_ESTAGIO1_2026-09-27.md` (363 linhas; §5 nas linhas 149-263
e Apêndice A nas linhas 289-363) — todo fato da §2 aponta `relatório:<linha>` · **Plano de origem:**
nenhum (o plano fictício que ocupou o id `P-0753` durante a auditoria foi descartado; relatório:283) ·
**Prefixo das tarefas no diário:** `AF-T<n>` · **Prefixo das decisões:** `DAF-<n>` ·
**Checagem de versão do kit:** modo hub — congelada em `0.0.0` (`GOVERNANCA.md` §10) ·
**Branch de trabalho:** `plan/planner-modelo-escopo` (HEAD `d75e7a6`, com WIP não commitado) ·
**Estado:** linha `plano` de `estado.tsv`, nesta pasta.

**Marcos de validação pelo dono:**

| marco | o que o dono lê | veredito |
|---|---|---|
| **Marco 1** | `python .claude/tools/modelo.py show --plano docs/plans/P-0753-auditoria-estagio-1/plano.md` (a §1 escrita pelo modelador) e, na mesma mensagem, as três escolhas de `DAF-5` (rota da campanha do planejador, destino de `uow.py`, classe do plano), cada uma com a recomendação desta §3 | go · 2026-09-27 — "Considere validado o marco 1 do plano atual, e inicie o loop" |
| **Marco 2** | o `README.md` revisado, a entrega do plano e a série de telemetria com os papéis gravados pelo hook | go · 2026-09-28 — "Conclua o que estiver pendente, e me entregue o plano concluído" |

## 0. O problema, verbatim

**Primeiro ato (2026-09-27), como transmitido por quem conduz:**

> Estamos em fase final da publicação da primeira versão do kit. [...] Elabore recomendações em
> tíquetes individuais para cada registro de inadequado e oportunidade de melhoria que se perceba
> viável. Entregue ao final o relatório com a avaliação e tíquetes para execução.

(A redação do mesmo ato registrada no relatório está em relatório:9.)

**Segundo ato (2026-09-27), sobre o relatório entregue:**

> Não ficou claro para mim se o plano já foi criado com as recomendações. E inserir os tíquetes
> descartados dentro do plano gerado.

**O que o plano entrega quando termina:** as dezoito recomendações `R-01`..`R-18` e os dois cards
descartados `TK-94a` e `TK-95a` do relatório de auditoria de encerramento do estágio 1 aplicados ao
kit — cada um na rota decidida na §3 —, com o `README.md` revisado ao fim.

Terceiro ato (dono, 2026-09-27, comentando o bloco das três operações bloqueadas), verbatim: *"OP19 - Acho um risco grande deixar o batedor, que seria um modelo Haiku, uma tarefa de decisão. Falha na ingestão de dados já condena todo o trabalho, e potencialmente todo o plano. Garantir que o batedor não precise fazer escolhas, não precise pensar, apenas executar. Aparenta que o problema das ferramentas é mais um problema de ajuste, e não pode um problema de ajuste alterar responsabilidades. Responsabilidades são decididas em nivel estratégico. Falhas de uso de ferramentas são resolvidos no nível operacional. Misturar os dois é falta grave. OP20 - Eu estou muito confuso sobre essa "unidade de trabalho" que insiste em reaparecer. Vou precisar de uma descrição melhor sobre isso. OP21 - Ok"*. Efeito: `AF-T21` passa a `ready`; `AF-T19` segue `blocked` à espera da rodada de replanejamento na rota operacional (instrumento, sem mudar responsabilidade do batedor); `AF-T20` segue `blocked` até a descrição do `uow.py` chegar ao dono.

Quarto ato (dono, 2026-09-27, sobre a `OP-20`), verbatim: *"Remover o uow, pois está obsoleto"*. Efeito: veredito na rota recomendada (`DAF-7`); `AF-T20` passa a `ready`.

**Marco 1, 2026-09-27 — veredito do dono (go):**

> Considere validado o marco 1 do plano atual, e inicie o loop

Efeito: plano `blocked` → `ready`; `AF-T19` segue `blocked` à espera da rodada de replanejamento na rota operacional (terceiro ato).

Quinto ato (dono, 2026-09-27, sobre o relatório da janela de execução), verbatim: *"Marque como aceitas as recomendações"*. Efeito, recomendação a recomendação: (1) `AF-T19` — rodada de planejamento em contexto novo para o card corretivo `AF-T19a` da `OP-19`, na rota operacional do terceiro ato; `AF-T19` segue `blocked` até ela; (2) a versão 2 pendente do modelo (texto da `OP-7`: em plano em pasta, a situação vem sempre do estado do plano) é aceita — ato de emenda despachado ao modelador; (3) Marco 2 segue pendente, depois da pendência (1); (4) a linha de `.claude/settings.json` com o diretório de cópias de `uow` sai.

Sexto ato (dono, 2026-09-27, na rodada de replanejamento da `AF-T19`, depois da avaliação medida do batedor, `F-36`), verbatim: *"Prosseguir com a recomendação A, e ajustar o desvio da ferramenta inacessível ao batedor"*. Efeito: `DAF-46` reescrita (o batedor roda no Opus, com a ferramenta de comando; leitura pontual direto; varredura ampla com o batedor); `AF-T19` `cancelled`; card corretivo `AF-T19a`; versão 3 do modelo emendada pelo modelador.

Sétimo ato (dono, 2026-09-27, sobre a versão 3 do modelo validada pelo consultor), verbatim: *"Aceito a versão 3"*. Efeito: versão 3 vigente e versão 2 obsoleta (ato de emenda do modelador); `AF-T19a` `ready`, próxima da fila.

**Marco 2, 2026-09-28 — veredito do dono (go):**

> Conclua o que estiver pendente, e me entregue o plano concluído

## 1. Modelo conceitual

**Estado do modelo:** versão 3 · 2026-09-27 · autor: modelador · 21 operações · 30 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem | lastro na §0 ou no relatório | tipo |
|---|---|---|---|---|---|---|
| dossiê de evidência | o documento que o revisor recebe com o que a entrega mudou na árvore, para julgar a tarefa | recorte do resumo de diferenças, atribuição do relatório de auditoria | Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo. | OP-1 | §0, segundo ato: *"inserir os tíquetes descartados dentro do plano gerado"* · relatório:291-363 | escopo |
| painel do gerente | a tela de progresso que acompanha, chamada a chamada, o que o loop faz | leitura de chamada com opção do interpretador | Quem implementa faz o painel reconhecer o programa chamado mesmo quando a chamada traz opções do interpretador antes dele. | OP-3 | relatório:183-187 | escopo |
| fechamento de tarefa | o comando único que encerra uma tarefa revisada e registra o que o laudo disse | achado de processo do laudo | Quem implementa faz o fechamento copiar cada achado de processo do laudo para os achados do plano, com a rota, sem repetir achado igual. | OP-4 | relatório:189-193 | escopo |
| série de telemetria | o registro do consumo de cada rodada de agente, somado por plano no encerramento | papéis gravados, consumo do plano | Quem implementa faz o gancho gravar toda rodada de agente do kit, com o papel no identificador, e a soma do plano contar todas elas. | OP-5 | relatório:201-205 | escopo |
| linha de retorno do revisor | a primeira linha que o revisor devolve ao loop ao fim de cada revisão | recomendação do laudo | Quem implementa acrescenta a recomendação à linha e faz todos os que a leem aceitarem a forma nova no mesmo ato. | OP-6 | relatório:231-235 | escopo |
| conferência do card | a conferência que roda, antes do despacho, os comandos de verificação do card no mundo em que ele está | situação do card em plano em pasta | Quem implementa faz a conferência ler a situação da tarefa sempre no estado do plano, mesmo quando o card declara a sua. Tarefa sem situação no estado é comparada contra o mundo de antes, com aviso. | OP-7 | relatório:225-229 | escopo |
| conferência do backlog | a conferência que valida os planos e o índice do backlog | aceite do plano em esboço | Quem implementa faz a conferência aceitar o plano recém-esboçado que já tem o estado registrado e ainda não entrou na fila. | OP-8 | relatório:171-175 | escopo |
| planejador | o agente que transforma o pedido do dono em plano, da campanha de perguntas à decomposição em cards | registro do plano em esboço, conferência do pedido, profundidade da auto-auditoria | Quem implementa recebe o roteiro de fases do agente e muda só a fase que a recomendação aponta, deixando as demais como estão. | OP-8 | relatório:171-175 · relatório:207-217 | escopo |
| despacho de tarefa | o ato de quem conduz de mandar um card pronto ao executor | card entregue inteiro, conferências do despacho | Quem implementa faz o despacho entregar o card sem corte e rodar num comando só as conferências que hoje se repetem à mão, recusando pela primeira que falhar. | OP-9 | relatório:177-181 · relatório:237-241 | escopo |
| consultor | o agente que tria cada parada do loop e decide o destino dela | leitura por acionamento, avaliação estratégica | Quem implementa fixa no agente o que ele lê em cada acionamento e a forma curta da avaliação estratégica, e dá a quem conduz o molde do despacho com as três entradas. | OP-11 | relatório:219-223 | escopo |
| marco de validação | o ponto em que o dono dá o sim ou o não sobre o plano | registro do veredito | Quem implementa faz um comando receber o resultado do dono como escolha explícita e gravá-lo em todos os lugares onde o marco aparece, sem interpretar a frase do dono. | OP-12 | relatório:195-199 | escopo |
| relatório de operações | o relato de encerramento que conta, tarefa a tarefa, como o plano foi executado | esqueleto | Quem implementa faz um comando gerar o esqueleto do relato a partir das tarefas do plano e conferir a cobertura dele. | OP-13 | relatório:249-253 | escopo |
| conferência do modelo | a conferência da seção de modelo de um plano e a comparação entre a versão vigente e a pendente | versão pendente conferida, comparação de contratos | Quem implementa faz a conferência julgar a versão pendente pelas mesmas regras da vigente, e a comparação mostrar o contrato e a propriedade que mudaram. | OP-14 | relatório:243-247 | escopo |
| bateria de testes do kit | os testes que guardam o kit, inclusive a verificação que a doutrina chama de obrigatória | piso e conformidade | Quem implementa cria o piso dos comportamentos já trancados e o teste de camadas do kit, sem mudar a skill que os exige. | OP-15 | relatório:153-157 | escopo |
| verificadores do console | os verificadores do kit escritos para o terminal do Windows | acentos na saída | Quem implementa faz os verificadores escreverem em UTF-8, sem mudar o texto das mensagens. | OP-16 | relatório:255-259 | escopo |
| guia de entrada do kit | o documento que apresenta o kit a quem chega | aderência ao kit entregue | Quem implementa revisa o guia contra o kit como ele fica depois das mudanças deste plano. | OP-18 | §0, o que o plano entrega quando termina: *"com o README.md revisado ao fim"* | escopo |
| batedor | o agente de leitura a quem o kit manda a coleta de dados, para poupar o contexto de quem pede | modelo em que roda, ferramenta de comando, coleta que recebe | Quem implementa troca o modelo e as ferramentas do batedor, tanto no do projeto quanto no modelo global de onde ele é copiado, e acerta as instruções do kit que mandam a coleta ao modelo barato. A campanha que o planejador manda a ele fica como está. | OP-19 | §0, terceiro ato: *"Acho um risco grande deixar o batedor, que seria um modelo Haiku, uma tarefa de decisão"* e *"Aparenta que o problema das ferramentas é mais um problema de ajuste"* · §0, sexto ato: *"Prosseguir com a recomendação A, e ajustar o desvio da ferramenta inacessível ao batedor"* · relatório:159-163 | escopo |
| instrumento de unidade de trabalho | uma ferramenta do kit que nada cita e nenhum teste cobre, com a documentação apontando uma regra que já mudou | presença no kit | Quem implementa retira a ferramenta do kit; não há teste dela a retirar junto. | OP-20 | relatório:165-169 | escopo |
| relatório de auditoria | o relatório do encerramento do primeiro estágio, com as dezoito recomendações e os dois tíquetes descartados | itens recomendados | Ninguém altera: é a fonte de cada item que o plano aplica. | externo | §0, primeiro ato: *"Elabore recomendações em tíquetes individuais para cada registro de inadequado e oportunidade de melhoria que se perceba viável"* · relatório:149-151 | externo |
| escolha do dono no primeiro marco | as três escolhas de rota que o relatório deixa ao dono: a campanha do planejador, o destino da ferramenta sem uso e a classe do plano | escolhas de rota | Ninguém altera: o dono as dá no primeiro marco, e a operação que depende de cada uma espera por ela. | externo | relatório:161 · relatório:167 · relatório:215 | externo |
| tarefa do loop | cada card que o loop despacha, revisa e fecha | atos manuais do condutor por tarefa | Ninguém altera: é nela que se vê, antes e depois, quanto de cada ciclo ainda depende da mão e da memória de quem conduz. | externo | relatório:99 · relatório:101 · relatório:106 | medição |

### 1.2 Fluxo de operações

**A. Os instrumentos que o próprio loop usa**

- **OP-1** — O instrumento de evidência passa a resumir as diferenças da entrega pelo mesmo recorte da lista de arquivos tocados, sem o trabalho em andamento de fora da tarefa.
  - `precisa de: relatório de auditoria` · `altera: dossiê de evidência.recorte do resumo de diferenças` · `tarefas: AF-T1` · `lastro: relatório:291-321`
- **OP-2** — O instrumento de evidência passa a contar o relatório de auditoria de quem conduz como registro da condução, e não como entrega fora do alvo da tarefa.
  - `precisa de: dossiê de evidência` · `altera: dossiê de evidência.atribuição do relatório de auditoria` · `tarefas: AF-T2` · `lastro: relatório:322-363`
- **OP-3** — O painel do gerente passa a reconhecer o programa chamado quando a chamada traz opções do interpretador antes dele.
  - `precisa de: dossiê de evidência` · `altera: painel do gerente.leitura de chamada com opção do interpretador` · `tarefas: AF-T3` · `lastro: relatório:183-187`
- **OP-4** — O fechamento de tarefa passa a copiar para os achados do plano cada achado de processo que o laudo traz, com a rota dele.
  - `precisa de: dossiê de evidência` · `altera: fechamento de tarefa.achado de processo do laudo` · `tarefas: AF-T4` · `lastro: relatório:189-193`
- **OP-5** — O gancho de telemetria passa a gravar o consumo de todo papel do kit, que a soma do plano conta por inteiro.
  - `precisa de: dossiê de evidência, fechamento de tarefa` · `altera: série de telemetria.papéis gravados, série de telemetria.consumo do plano` · `tarefas: AF-T5` · `lastro: relatório:201-205`

**B. As recomendações que nascem prontas**

- **OP-6** — O revisor passa a devolver a recomendação do laudo na primeira linha, na forma que o painel, o fechamento e as instruções do gerente leem no mesmo ato.
  - `precisa de: dossiê de evidência, painel do gerente, fechamento de tarefa` · `altera: linha de retorno do revisor.recomendação do laudo` · `tarefas: AF-T6` · `lastro: relatório:231-235`
- **OP-7** — A conferência do card passa a ler a situação da tarefa sempre no estado do plano em pasta, sem consultar a que o card declara.
  - `precisa de: dossiê de evidência` · `altera: conferência do card.situação do card em plano em pasta` · `tarefas: AF-T7` · `lastro: relatório:225-229`
- **OP-8** — A conferência do backlog passa a aceitar o plano que o planejador registra já no esboço, antes de ele entrar na fila.
  - `precisa de: dossiê de evidência` · `altera: conferência do backlog.aceite do plano em esboço, planejador.registro do plano em esboço` · `tarefas: AF-T8` · `lastro: relatório:171-175`
- **OP-9** — O backlog passa a entregar a quem conduz o card inteiro no despacho, sem corte no meio.
  - `precisa de: dossiê de evidência, conferência do backlog` · `altera: despacho de tarefa.card entregue inteiro` · `tarefas: AF-T9` · `lastro: relatório:177-181`
- **OP-10** — Quem conduz passa a despachar a tarefa por um comando único, que roda as conferências do despacho e recusa pela primeira que falhar.
  - `precisa de: dossiê de evidência, despacho de tarefa, conferência do card, tarefa do loop` · `altera: despacho de tarefa.conferências do despacho` · `tarefas: AF-T10` · `lastro: relatório:237-241`
- **OP-11** — O consultor passa a responder cada acionamento lendo só as três entradas do despacho, com a avaliação estratégica numa frase.
  - `precisa de: dossiê de evidência, despacho de tarefa` · `altera: consultor.leitura por acionamento, consultor.avaliação estratégica` · `tarefas: AF-T11` · `lastro: relatório:219-223`
- **OP-12** — Quem conduz passa a gravar o veredito do dono no marco por um comando único, que o escreve em todos os lugares onde o marco aparece.
  - `precisa de: dossiê de evidência, fechamento de tarefa` · `altera: marco de validação.registro do veredito` · `tarefas: AF-T12` · `lastro: relatório:195-199`
- **OP-13** — Quem conduz passa a gerar por comando o esqueleto do relatório de operações, em vez de reescrevê-lo de memória a cada plano.
  - `precisa de: dossiê de evidência, fechamento de tarefa` · `altera: relatório de operações.esqueleto` · `tarefas: AF-T13` · `lastro: relatório:249-253`
- **OP-14** — A conferência do modelo passa a julgar a versão pendente pelas mesmas regras da vigente e a mostrar, na comparação entre as duas, o contrato que mudou.
  - `precisa de: dossiê de evidência` · `altera: conferência do modelo.versão pendente conferida, conferência do modelo.comparação de contratos` · `tarefas: AF-T14` · `lastro: relatório:243-247`
- **OP-15** — Quem executa cria o piso dos comportamentos trancados e o teste de camadas que a verificação obrigatória do kit exige.
  - `precisa de: dossiê de evidência` · `altera: bateria de testes do kit.piso e conformidade` · `tarefas: AF-T15` · `lastro: relatório:153-157`
- **OP-16** — Os verificadores do kit passam a escrever os acentos corretamente no console do Windows.
  - `precisa de: dossiê de evidência` · `altera: verificadores do console.acentos na saída` · `tarefas: AF-T16` · `lastro: relatório:255-259`
- **OP-17** — O planejador passa a conferir, antes de abrir a campanha, a existência de cada caminho, nome e opção que o pedido do dono cita.
  - `precisa de: dossiê de evidência, planejador` · `altera: planejador.conferência do pedido` · `tarefas: AF-T17` · `lastro: relatório:207-211`

**C. O guia do kit, revisado ao fim da parte pronta**

- **OP-18** — Quem executa revisa o guia de entrada do kit para que ele descreva o kit como fica depois das mudanças deste plano.
  - `precisa de: dossiê de evidência, série de telemetria, linha de retorno do revisor, despacho de tarefa, marco de validação, relatório de operações, conferência do modelo, planejador` · `altera: guia de entrada do kit.aderência ao kit entregue` · `tarefas: AF-T18` · `lastro: §0, o que o plano entrega quando termina — com o README revisado ao fim`

**D. As recomendações que esperam a escolha do dono**

- **OP-19** — O batedor passa a rodar no Opus, com a ferramenta de comando, e a receber do kit só a varredura ampla, a pergunta de comando da campanha do planejador inclusive.
  - `precisa de: dossiê de evidência, planejador, escolha do dono no primeiro marco` · `altera: batedor.modelo em que roda, batedor.ferramenta de comando, batedor.coleta que recebe` · `tarefas: AF-T19, AF-T19a` · `lastro: relatório:159-163; §0, terceiro ato; §0, sexto ato, "Prosseguir com a recomendação A, e ajustar o desvio da ferramenta inacessível ao batedor"`
- **OP-20** — Quem executa retira do kit o instrumento de unidade de trabalho, que nada cita e nenhum teste cobre.
  - `precisa de: dossiê de evidência, escolha do dono no primeiro marco` · `altera: instrumento de unidade de trabalho.presença no kit` · `tarefas: AF-T20` · `lastro: relatório:165-169`
- **OP-21** — O planejador passa a dosar a própria auto-auditoria pela classe do plano, declarada no cabeçalho dele.
  - `precisa de: dossiê de evidência, planejador, escolha do dono no primeiro marco` · `altera: planejador.profundidade da auto-auditoria` · `tarefas: AF-T21` · `lastro: relatório:213-217`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final | lastro na §0 ou no relatório |
|---|---|---|---|
| dossiê de evidência.recorte do resumo de diferenças | com recorte informado, o resumo lista o trabalho em andamento da árvore inteira e deixa de fora os arquivos novos da entrega | com recorte informado, o resumo lista exatamente os arquivos tocados desde o recorte, os novos inclusive; sem recorte, nada muda | relatório:291-301 |
| dossiê de evidência.atribuição do relatório de auditoria | o relatório que quem conduz escreve durante a janela cai como arquivo fora do alvo e deixa o veredito mecânico aberto | cai como registro da condução e não pesa no veredito; quando é alvo do card, segue coberto | relatório:322-332 |
| painel do gerente.leitura de chamada com opção do interpretador | com a opção de UTF-8 do interpretador, o painel toma a opção pelo programa e cala cinco das linhas que deveria mostrar | com qualquer opção do interpretador, o painel reconhece o programa e mostra as mesmas linhas da chamada sem opção | relatório:183-187 |
| fechamento de tarefa.achado de processo do laudo | só chega aos achados do plano se quem conduz o redigitar, e na janela medida foi esquecido | cada achado de processo do laudo chega aos achados do plano com a rota, uma vez só | relatório:189-193 |
| série de telemetria.papéis gravados | só o executor grava sozinho; os demais papéis entram à mão ou não entram | toda rodada de agente do kit grava sozinha, com o papel no identificador | relatório:201-205 |
| série de telemetria.consumo do plano | o total mostrado ao dono ficou cerca de dois terços abaixo do consumo real | o total soma todas as rodadas do plano, de todos os papéis | relatório:201-205 |
| linha de retorno do revisor.recomendação do laudo | ausente; quem conduz abre o laudo a cada tarefa para saber o que fazer | presente na primeira linha e lida, na mesma forma, pelo painel, pelo fechamento e pelas instruções do gerente | relatório:231-235 |
| conferência do card.situação do card em plano em pasta | lida só no próprio card, que no plano em pasta não a traz; a conferência compara sempre contra o mundo de antes | lida sempre do estado do plano, nunca do card; tarefa concluída no estado é comparada contra o mundo de depois, e tarefa sem situação no estado, contra o mundo de antes, com aviso | relatório:225-229 |
| conferência do backlog.aceite do plano em esboço | recusa o plano entre o esboço e a publicação, com três violações | aceita o plano esboçado que tem o estado registrado e ainda não está na fila | relatório:171-175 |
| planejador.registro do plano em esboço | o roteiro não diz quando gravar o estado do plano, e o planejador improvisou | o roteiro manda gravar o estado do plano junto do esboço | relatório:171-175 |
| planejador.conferência do pedido | nenhuma; uma premissa falsa do pedido custou uma instância inteira do planejador | antes da campanha, cada caminho, nome e opção citados no pedido é conferido, e o que não existe volta ao dono | relatório:207-211 |
| planejador.profundidade da auto-auditoria | a mesma para todo plano; um plano trivial de três operações custou 319 mil tokens de planejamento | proporcional à classe do plano declarada no cabeçalho; rota recomendada, sujeita à escolha do dono | relatório:213-217 |
| despacho de tarefa.card entregue inteiro | o card chega cortado no meio, e quem conduz relê o trecho do plano | o card chega inteiro; só os achados e as notas de execução têm teto | relatório:177-181 |
| despacho de tarefa.conferências do despacho | seis atos iguais, feitos à mão a cada tarefa | um comando roda as conferências, marca a tarefa em curso e recusa pela primeira que falhar | relatório:237-241 |
| consultor.leitura por acionamento | lê além das três entradas; o acionamento que leu o relatório de auditoria custou 131 mil tokens | lê só o cenário, o card, a evidência e a doutrina que o cenário aponta | relatório:219-223 |
| consultor.avaliação estratégica | veio em três frases | vem em uma frase | relatório:219-223 |
| marco de validação.registro do veredito | não tem quem o escreva; os lugares onde o marco aparece ficam defasados entre si | um comando grava o resultado dado pelo dono em todos os lugares do marco, sem interpretar a frase dele | relatório:195-199 |
| relatório de operações.esqueleto | reescrito de memória a cada plano | gerado por comando a partir das tarefas do plano, com a cobertura conferida | relatório:249-253 |
| conferência do modelo.versão pendente conferida | a versão pendente não passa por regra nenhuma | a versão pendente passa pelas mesmas regras da vigente, com as violações marcadas como dela | relatório:243-247 |
| conferência do modelo.comparação de contratos | a comparação entre versões mostra só operações e estado final | a comparação mostra também o contrato e a propriedade de objeto que mudaram | relatório:243-247 |
| bateria de testes do kit.piso e conformidade | a verificação obrigatória sai verde porque nem o piso nem a conformidade existem | o piso lista os comportamentos trancados e o teste de camadas roda na suíte | relatório:153-157 |
| verificadores do console.acentos na saída | letra acentuada sai corrompida no console | letra acentuada sai correta | relatório:255-259 |
| guia de entrada do kit.aderência ao kit entregue | descreve o kit de antes deste plano | descreve o kit com as mudanças deste plano | §0, o que o plano entrega quando termina: *"com o README.md revisado ao fim"* |
| batedor.modelo em que roda | roda no modelo barato, o Haiku, tanto no do projeto quanto no global; na avaliação medida acertou as duas coletas pequenas e errou em silêncio as contagens das duas grandes | roda no Opus, nos dois lugares, o que acertou as quatro coletas da mesma avaliação | §0, terceiro ato: *"o batedor, que seria um modelo Haiku"* · §0, sexto ato: *"Prosseguir com a recomendação A, e ajustar o desvio da ferramenta inacessível ao batedor"* · relatório:159-163 |
| batedor.ferramenta de comando | só lê e procura; a pergunta de comando que a campanha do planejador lhe manda fica sem resposta, e quem conduz a roda à mão | tem a ferramenta de comando e responde também à pergunta de comando; não roda nada que escreva no projeto e conta e filtra pela própria ferramenta, nunca somando lista à mão; ninguém mais roda comando à mão para o planejador | §0, terceiro ato: *"o problema das ferramentas é mais um problema de ajuste"* · §0, sexto ato: *"Prosseguir com a recomendação A, e ajustar o desvio da ferramenta inacessível ao batedor"* · relatório:159-163 |
| batedor.coleta que recebe | as instruções do kit mandam ao modelo barato toda coleta, da leitura de duas linhas à varredura de centenas de arquivos | a leitura de um trecho já localizado quem precisa do dado faz direto; a varredura ampla segue com o batedor, para poupar o contexto de quem pede; nenhuma instrução do kit manda a coleta ao modelo barato | §0, terceiro ato: *"Garantir que o batedor não precise fazer escolhas, não precise pensar, apenas executar"* · §0, sexto ato: *"Prosseguir com a recomendação A, e ajustar o desvio da ferramenta inacessível ao batedor"* · relatório:159-163 |
| instrumento de unidade de trabalho.presença no kit | presente, sem quem o use nem teste, e sai sem erro quando falha | fora do kit; rota recomendada, sujeita à escolha do dono | relatório:165-169 |
| relatório de auditoria.itens recomendados | dezoito recomendações e dois tíquetes descartados, nenhum aberto | os mesmos vinte itens; o relatório não muda | §0, primeiro ato · relatório:149-151 |
| escolha do dono no primeiro marco.escolhas de rota | três escolhas em aberto | três escolhas dadas pelo dono: as três no primeiro marco, e a da campanha do planejador refeita por ele depois, na rodada de replanejamento | relatório:161 · relatório:167 · relatório:215 · §0, sexto ato: *"Prosseguir com a recomendação A, e ajustar o desvio da ferramenta inacessível ao batedor"* |
| tarefa do loop.atos manuais do condutor por tarefa | cada ciclo depende de quem conduz para reler o card, redigitar o achado, abrir o laudo, copiar a telemetria e repetir seis atos de despacho | nenhum desses atos depende da mão nem da memória de quem conduz | relatório:99 · relatório:101 · relatório:106 |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 1 | 2026-09-27 | obsoleta | modelador — autoria sobre o dossiê do planejador na Fase 3a; pedido do dono em dois atos de 2026-09-27. Caiu pelo aceite da versão 2 em 2026-09-27 |
| 2 | 2026-09-27 | obsoleta | modelador — conflito sobre o achado de processo de alvo modelo no laudo de AF-T7: OP-7 passa a dizer que a situação vem sempre do estado do plano em pasta. Aceita pelo dono em 2026-09-27, fora de marco, no quinto ato da §0, verbatim: *"Marque como aceitas as recomendações"*. Caiu pelo aceite da versão 3 em 2026-09-27 |
| 3 | 2026-09-27 | vigente | modelador — emenda pela DAF-46 reescrita, do planejador na rodada de replanejamento da AF-T19 (revoga a DAF-6): o batedor entra como objeto do plano, e a OP-19 passa a dizer que ele roda no Opus, com a ferramenta de comando, e recebe do kit só a varredura ampla, a pergunta de comando da campanha do planejador inclusive; a propriedade da campanha sai do planejador, cuja campanha não muda. Substitui, no lugar, o conteúdo anterior desta versão (a rota do instrumento novo, descartada pelo dono). Rota escolhida pelo dono em 2026-09-27, depois de ver a avaliação medida do batedor, verbatim: *"Prosseguir com a recomendação A, e ajustar o desvio da ferramenta inacessível ao batedor"*. Lastro corrigido depois da primeira leitura do consultor, que não validou por lastro: o sexto ato da §0 entra como âncora do batedor, das três propriedades dele e da OP-19, e a escolha da campanha refeita depois do primeiro marco entra no estado final da escolha do dono; nenhum texto de operação nem contrato mudou. Validada pelo consultor em 2026-09-27, e aceita pelo dono em 2026-09-27, fora de marco, verbatim: *"Aceito a versão 3"* |

## 2. Fatos estabelecidos

Fonte padrão: o relatório de auditoria, medido na árvore em 2026-09-27 (relatório:3-5). Fato
re-medido por quem planeja nesta sessão traz **re-medido 2026-09-27** e o comando ou padrão.

| id | fato | fonte |
|---|---|---|
| F-1 | O relatório é o dossiê do plano: 58 registros (relatório:73-130), conclusão por dimensão (relatório:132-147), 18 recomendações com origem, causa, ação, verificação e cabeçalho de card (relatório:153-259) e dois tíquetes do consultor com cards medidos (relatório:289-363). Nenhuma recomendação foi aberta no diário | relatório:151 |
| F-2 | O relatório não está rastreado pelo git: `git ls-files --error-unmatch` sobre o caminho dele sai com erro. **re-medido 2026-09-27** | Bash |
| F-3 | Diretiva do dono de 2026-09-26: "nenhum card nem tíquete novo por ajuste"; por ela as recomendações não foram abertas e `TK-94`/`TK-95` saíram do diário na limpeza | relatório:151, 263 |
| F-4 | `tests/conformance/` e `tests/piso_comportamental.txt` não existem no hub; `ratchet_piso` sai 0 por "nenhum piso declarado"; a skill `guardrails-check` chama o Tier 2 de obrigatório (`.claude/skills/guardrails-check/SKILL.md:16`). **re-medido 2026-09-27** (`ls` dos dois caminhos: ausentes) | relatório:75, 153-157 |
| F-5 | A Fase 1 do planejador manda pôr na campanha "rode `<comando exato>` no repositório e devolva o stdout literal" (`.claude/agents/pantonic-planner.md:125`); o `pantonic-scout` tem só `Read, Glob, Grep`; 5 de 10 perguntas da campanha medida pediam comando e foram rodadas à mão pelo orquestrador em 2 chamadas. O literal ``rode `<comando`` ocorre em 2 arquivos sob `.claude`, `GOVERNANCA.md` e `docs` (`grep -rlF`, `*.md`): o arquivo do planejador e o relatório. **re-medido 2026-09-27** | relatório:79, 159-163 |
| F-6 | O planejador tem `Bash` desde a decisão do dono de 2026-09-18, para rodar o aceite que publica e re-rodar grep de verificação de superfície | `.claude/agents/pantonic-planner.md`, *Fatos estáveis* |
| F-7 | `uow.py`: 0 citações em `.claude/skills`, `.claude/agents`, `GOVERNANCA.md`, `README.md`, `docs/RUBRICA_DE_REVISAO.md`; 0 arquivos `tests/*.py` citam `uow`; 0 citações em `.claude/checks/*.ps1` e em `.claude/projecoes.json`; a docstring (`.claude/tools/uow.py:3`) cita "Regra 9 da doutrina global", hoje outra regra; `uow.py status` sem UoW aberta sai 0 com `erro:` no stdout. **re-medido 2026-09-27** (três greps, 0 linhas cada) | relatório:76, 116, 165-169 |
| F-8 | Entre a Fase 3a e a Fase 5, `backlog.py check` recusou o esqueleto de plano em pasta só com `plano.md` (`C-8`, `C-13`, `C-10`), e o planejador improvisou o registro antecipado. A skill `diario-de-obras` diz "O planejador grava o arquivo ao registrar o plano" (`.claude/skills/diario-de-obras/SKILL.md:206`). O estado com `estado.tsv` só com a linha do plano está medido na F-22 | relatório:84, 171-175 |
| F-9 | `backlog.py next` e `show` cortam o dossiê no teto `DB-7` (8.000 chars / 120 linhas; `.claude/tools/backlog.py:8`, `:1022`, `:1051`, `:1531`) no meio de `Camada`, `Passos`, `Restrições`; o condutor relê o range | relatório:91, 177-181 |
| F-10 | `.claude/tools/progresso_hook.py:293` (`_programa`) pula todo token iniciado por `-` e toma o seguinte como script; com `python -X utf8 <script>` o "script" vira `utf8` e `M-2`, `M-5`, `M-10`, `M-13`, `M-18` não saem; sem `-X utf8` saem (controle pareado). `docs/ARMADILHAS_DE_FERRAMENTA.md:14` recomenda `-X utf8` | relatório:97, 104, 109, 183-187 |
| F-11 | `encerrar.py tarefa` lê o pacote de cinco campos do laudo e ignora a tabela `## Achado de processo` (colunas `alvo` e `achado`); o achado depende de `--achado` digitado pelo condutor, que o esqueceu na janela medida | relatório:101, 189-193 |
| F-12 | O veredito do marco não tem escritor: tabela *Marcos de validação*, `## 0`, decisão de emenda, `cenario.md` e `estado.tsv` ficam defasados entre si a cada marco | relatório:120, 125, 195-199 |
| F-13 | `.claude/tools/telemetria_hook.py:51` fixa `_AGENT_TYPE_EXECUTOR = "pantonic-executor"`: só o executor grava; a linha do revisor entrou à mão na forma `SF-T1-revisao opus 11 70.4 112.3 usage`; o "consumo do plano" impresso subestimou ~66% (399,6k contra ≈ 1.168k). **re-medido 2026-09-27** (linha 51) | relatório:77, 103, 127, 201-205 |
| F-14 | Uma premissa falsa no pedido (`ler_texto_utf8`) custou uma instância do planejador (41,4k) mais a campanha; um grep a revelaria. As skills citam o despacho do planejador só na rodada de replanejamento (`.claude/skills/passagem-de-bastao/SKILL.md:277`) e no painel (`.claude/skills/scrum-master/SKILL.md:391`): não há residência de condução de sessão de planejamento fora do arquivo do planejador. **re-medido 2026-09-27** (`grep -n pantonic-planner` nas skills) | relatório:78, 82, 207-211 |
| F-15 | O planejamento de 3 operações custou 319k em três instâncias; a Fase 4 de 14 itens e o ensaio em cópia foram aplicados inteiros; a Fase 3b-5 com ensaio custou 169,5k para 3 cards | relatório:83, 87, 213-217, 269 |
| F-16 | O consultor leu o relatório fora das três entradas no acionamento 1 (131,2k) e custou 67,4k no acionamento 2 com a instrução de não ler fora do cenário; `estrategico=` veio em três frases | relatório:117, 120, 219-223 |
| F-17 | `card_check.py` sobre card de plano em pasta imprime `status ausente: comparando antes`: não lê `estado.tsv` | relatório:92, 225-229 |
| F-18 | A linha de retorno do revisor traz veredito, percentual e `bloqueante=`, não a recomendação; o bloco A roteia pela recomendação e o condutor abre o laudo. O literal `bloqueante=` ocorre em 5 arquivos: `.claude/agents/pantonic-reviewer.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/encerrar.py`, `.claude/tools/progresso_hook.py`, `.claude/tools/rdo.py` (`grep -rlF "bloqueante="` sobre `.claude`, `GOVERNANCA.md`, `docs/RUBRICA_DE_REVISAO.md`, `README.md`, arquivos `*.md` e `*.py`: 5). **re-medido 2026-09-27** | relatório:99, 231-235 |
| F-19 | Por despacho o condutor roda seis atos mecânicos idênticos: `modelo.py check`, `card_check`, `pytest --co`, `status in-progress`, `tarefa-corrente.json` escrito à mão, captura do `<ref>` | relatório:106, 237-241 |
| F-20 | `modelo.py check` afere só a `## 1`; a `## 1A` pendente não passa por `V1..V21`; `show --drift` compara só operações e estado final, não contrato | relatório:121-122, 243-247 |
| F-21 | `operacoes.md` é reescrito de memória a cada plano a partir da estrutura da skill `entrega-de-encerramento` | relatório:123, 249-253 |
| F-22 | Estado intermediário da Fase 3a medido sobre este plano (`estado.tsv` só com a linha do plano, `blocked` `dependencia`; sem linha no inbox; contador em `P-0753`): `python .claude/tools/backlog.py check` sai 1 com uma só violação, `C-10 docs/plans/_INBOX.md:5 — contador aponta para P-0753, já presente em docs/plans/`; `C-8` e `C-13` não disparam. **re-medido 2026-09-27** | Bash |
| F-23 | `check-readme.ps1` imprime acentos corrompidos em console cp1252 (`vers�o`) | relatório:74, 255-259 |
| F-24 | `TK-94a` (com `--desde`, o `--stat` do dossiê de evidência recorta como os tocados) e `TK-95a` (`docs/audits/` no balde de registro da orquestração) são cards completos com Verificação medida pelo consultor; `TK-95a` depende de `TK-94a` (os dois tocam `.claude/tools/review_evidence.py` e `tests/test_review_evidence.py`). Âncoras hoje: `coletar_diff_stat` em `.claude/tools/review_evidence.py:232`, `_REGISTRO_ORQUESTRACAO` em `:376`, `_eh_registro_orquestracao` em `:384`. **re-medido 2026-09-27** | relatório:303-363 |
| F-25 | Linha de base: `python -m pytest --co -q` → `452 tests collected`; `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `kit_check: check-drift OK - .claude/README.md == regenerado (10 agente(s), 13 skill(s)); materializacao do alvo 'projeto' == canonico.`, exit 0; `python .claude/tools/backlog.py check` antes deste plano → `check: OK — nenhuma violação.` Referência histórica datada, nunca piso. **re-medido 2026-09-27** | Bash |
| F-26 | Há 59 arquivos de WIP não commitado na árvore; o `--stat` do dossiê de evidência os lista contra `HEAD` até o `TK-94a` fechar | relatório:293 |
| F-27 | Fora das recomendações: revisão da doutrina pendente — `P-0751` ("Esgotar o backlog") e `P-0752` ("Fato no ponto de uso") fecharam `done` sem rodada de revisão registrada (`GOVERNANCA.md` §7.1) | relatório:261-263 |
| F-28 | A forma da linha do revisor (`bloqueante=` na primeira linha) mora em três arquivos: `.claude/agents/pantonic-reviewer.md` (passo 7), `.claude/skills/scrum-master/SKILL.md` (Passo 7 e linha `M-7` da tabela de frases) e `.claude/tools/progresso_hook.py` (`FRASES['M-7']` e o regex da volta do revisor). Em `encerrar.py` e `rdo.py` o literal `bloqueante=` é argumento nomeado de função, e o fechamento já lê `**Recomendação:**` do laudo (`_LAUDO_RES`). `test_tf_ger_18_residencia` confere `FRASES` contra a tabela da skill. **re-medido 2026-09-27** (`grep -rnF "bloqueante="`) | Bash |
| F-29 | `rdo._status_atual(plano, id, dossie, pasta_plano)` já lê a linha da tarefa em `estado.tsv` quando `pasta_plano` não é `None`; `card_check.verificar_tarefa` passa `None`. **re-medido 2026-09-27** | Bash |
| F-30 | `telemetria_hook.processar` sai `False` para todo `agent_type` diferente de `pantonic-executor` e apaga `tarefa-corrente.json` depois de gravar; `test_tr_hook_so_executor_consome_estado` e a asserção `not estado_path.exists()` de `test_tf_processar_payload_de_fixture_grava_linha_esperada_no_tsv` trancam isso. `encerrar._consumo_do_plano` já conta as linhas de prefixo `<P-n>-`, no grupo `outros`. A skill `scrum-master` (*Acionamento do consultor*) fixa a tarefa `<ID>-consultor-<n>`; `GOVERNANCA.md` §4.2 diz que o hook só grava o executor. **re-medido 2026-09-27** | Bash |
| F-31 | `modelo.py show --drift` já tem a seção `## Objetos`, mas `_diff_objetos` compara só propriedades; `validar` sobre a versão pendente de `tests/fixtures/modelo/fluxo-pendente.md` daria `V13` e `V19` (a versão pendente não tem registro de versões) e `V17`, e nenhum teste roda `check` sobre essa fixture; `tests/fixtures/modelo/fluxo-valido.md` sai `check` 0. **re-medido 2026-09-27** | Bash |
| F-32 | `progresso_hook._programa(['python','-X','utf8','.claude/tools/backlog.py','status'])[0]` devolve `utf8`. **re-medido 2026-09-27** | Bash |
| F-33 | `uow.py` é citado em `.claude/tools/backlog.py` (docstring: "mesmo desenho de `uow.py`/`telemetria.py`") e em `.claude/settings.json` (diretório adicional das cópias de `uow`: configuração do harness, `I-6`). **re-medido 2026-09-27** (`grep -rln uow`, fora de `docs/plans`, `docs/audits`, `docs/RDO` e do diário) | Bash |
| F-34 | `check-readme.ps1` imprime o caractere de substituição no lugar dos acentos quando a saída é capturada (8 ocorrências em 2026-09-27); a saída de `kit_check.ps1 -Mode check-drift` não tem acento; nos dois arquivos, `param(...)` é a primeira instrução, e `$ErrorActionPreference = 'Stop'` vem logo depois. **re-medido 2026-09-27** | Bash |
| F-35 | `ratchet_piso.py` lê `<nodeid> — <frase>` por linha; `python -m pytest --co -q` coleta 107 nodeids `::test_tr_`; nenhum `import`/`from` de `tests` ou de `caminhos` em `.claude/tools/*.py` e `.claude/checks/*.py`; não há `conftest.py` em `tests/`; `pytest.ini` tem `testpaths = tests`. **re-medido 2026-09-27** | Bash |
| F-36 | Avaliação do batedor, 2026-09-27, pedida pelo dono: quatro demandas deste repositório (achar 2 linhas num arquivo; ler 2 campos de 10 arquivos; contar 325 cabeçalhos de card por classe em 113 planos e listar 20; contar quem cita cada uma de 16 ferramentas em 79 arquivos), cada uma no `pantonic-scout` com o modelo trocado, gabarito por script. Haiku: 100% nas duas pequenas (12,5 mil e 23,5 mil tokens); nas grandes, listas literais certas e contagens erradas sem aviso (246 em vez de 325; 3 de 16 contagens certas), a 67,0 mil e 85,6 mil tokens. Sonnet: 100%, 100%, 100%, 11 de 16 (erro declarado), a 14,9 mil, 16,1 mil, 87,8 mil e 149,5 mil. Opus: 100% nas quatro, a 14,0 mil, 15,8 mil, 33,4 mil e 88,9 mil. Preço por milhão de tokens de entrada: Haiku 4.5 US$ 1, Sonnet 5 US$ 2, Opus 5.5 US$ 4. O `pantonic-scout` e o `context-scout` têm `tools: Read, Glob, Grep` e `model: haiku` no frontmatter; a Fase 1 do planejador manda ao scout "rode `<comando exato>`" (`.claude/agents/pantonic-planner.md:132-136`). A palavra `haiku` ocorre 27 vezes nos doze arquivos-alvo da `AF-T19a`. **medido 2026-09-27** | Bash |

## 3. Decisões

Fechadas neste ato; o executor não as reabre. Toda decisão é consumida por ≥ 1 card da §5.

| id | decisão | razão |
|---|---|---|
| DAF-1 | Plano em pasta `docs/plans/P-0753-auditoria-estagio-1/`, prefixo `AF-T<n>`, decisões `DAF-<n>`; `estado.tsv` gravado já na Fase 3a com a linha do plano `blocked` `dependencia` | parâmetro de quem conduz; é a correção que a `R-04` recomenda (F-8) |
| DAF-2 | Escopo: `R-01`..`R-18`, `TK-94a` e `TK-95a` — vinte itens — mais a revisão do `README.md` ao fim (G-README dever 2). Fora: a revisão da doutrina pendente (F-27) e os registros sem recomendação (§7) | segundo ato do dono |
| DAF-3 | `TK-94a` e `TK-95a` entram como tarefas `AF-T<n>` deste plano, não como tíquetes do diário; o texto do Apêndice A é a fonte, e os valores `antes` da Verificação se re-medem na Fase 3b | segundo ato do dono ("inserir os tíquetes descartados dentro do plano"); a diretiva de 2026-09-26 (F-3) veta tíquete novo por ajuste, e o plano pedido pelo dono é a residência que ela não barra |
| DAF-4 | Ensaio dos cards em cópia da árvore (Fase 4 item 14) **dispensado** neste plano: cada `Verificação` publica o valor `antes` medido na autoria (`card_check --mundo antes` exit 0 obrigatório por card) e o valor `depois` marcado `(esperado, não ensaiado)` | registros 11 e 15 do relatório (F-15): o ensaio custou 169,5k para 3 cards, e este plano tem 21; decisão de quem conduz |
| DAF-5 | Três itens dependem de escolha do dono e seus cards nascem `blocked` razão `dependencia`: rota da `R-02`, destino de `uow.py` (`R-03`), classe do plano (`R-11`). Cada card é escrito **na rota recomendada** (`DAF-6`, `DAF-7`, `DAF-8`), com as opções no `Fundamento`; veredito do dono na rota recomendada → `ready`; veredito na outra rota → rodada de replanejamento, card corretivo `T<n>a` da mesma operação | decisão de quem conduz; card com um só caminho mantém o plano linear (G-PLANREADY condição 4) |
| DAF-6 | **Revogada pela `DAF-46` (2026-09-27).** `R-02`, rota recomendada (a): a campanha do planejador se parte em dois blocos fixados no arquivo do agente — *perguntas de leitura* (vão ao `pantonic-scout`) e *perguntas de comando* (quem conduz a sessão roda e cola stdout e exit code) —, e a frase de F-5 sai do arquivo. Alternativa registrada: rota (b), `.claude/tools/sondar.py` | sem instrumento novo a manter; o custo medido da rota manual foi 2 chamadas do orquestrador (F-5) |
| DAF-7 | `R-03`, rota recomendada: `uow.py` sai do kit (o arquivo é apagado; não há teste a apagar, F-7). Alternativa registrada: o arquivo do executor passa a citá-lo e o exit de erro vira 1 | 0 consumidores, 0 testes, ponteiro de regra envelhecido (F-7); kit na publicação da primeira versão |
| DAF-8 | `R-11`, rota recomendada: o cabeçalho do plano ganha `classe do plano` ∈ {`ferramentaria`, `doutrina`, `produto`} e a Fase 4 do planejador ganha a tabela item × classe (itens 7 e 13 só com gramática ou tabela normativa; item 14 só com arquivo compartilhado tocado). A medida de tokens por classe na série não é aceite de card e vai à §7. Alternativa registrada: protocolo inalterado | F-15; aceite de card é só o que o revisor roda |
| DAF-9 | `R-01`: cria-se `tests/piso_comportamental.txt` com uma linha por `test_tr_*` do kit e cria-se `tests/conformance/` com o teste de camadas do kit (nenhum `.claude/tools/*.py` importa de `tests`); a skill `guardrails-check` não muda | o gate prescrito deixa de ser verde por ausência no hub (F-4) e a skill segue igual nos derivados |
| DAF-10 | `R-04`: o texto da Fase 3a do planejador e a frase de F-8 na skill `diario-de-obras` passam a mandar gravar `estado.tsv` com a linha do plano na Fase 3a; `backlog.py check` aceita plano em pasta cujo `estado.tsv` tem só a linha do plano, `blocked`, sem linha no inbox — o `C-10` da F-22 deixa de disparar quando o id apontado pelo contador é um plano nesse estado; fixture nova com esse estado | F-8, F-22 |
| DAF-11 | `R-05`: `next` e `show` imprimem o card inteiro; o teto `DB-7` passa a valer só para `## Achados` e para as notas de execução; a skill `passagem-de-bastao` (Parte 2, fonte 1) registra a forma | F-9: a alternativa (só cabeçalho e range) mantém a leitura dupla medida |
| DAF-12 | `R-06`: `_programa` pula o valor de `-X` e de `-W`; com `-m <módulo>` o programa é o módulo; com `-c` não há script; a armadilha entra em `docs/ARMADILHAS_DE_FERRAMENTA.md` | F-10 |
| DAF-13 | `R-07`: `encerrar.fechar_tarefa` lê a tabela de achado de processo do laudo (colunas `alvo`, `achado`) e grava um `AE-<n>` com `**Rota:**` por linha, sem duplicar achado de texto idêntico já presente; `--achado` continua | F-11 |
| DAF-14 | `R-08`: verbo `encerrar.py marco` com `--plano <p>`, `--marco <n>`, `--resultado` ∈ {`go`, `no-go`}, `--veredito "<frase>"` e, exclusivos entre si, `--aceita-versao <k>` ou `--recusa-versao <k>`; o resultado é argumento explícito, nunca interpretado da frase | F-12; a máquina não interpreta a frase do dono |
| DAF-15 | `R-09`: o hook grava toda notificação de `subagent_type` `pantonic-*`; `tarefa` = id de `.claude/estado/tarefa-corrente.json` para executor (sem sufixo), revisor (`-revisao`) e consultor (`-consultor`); para planejador, modelador e scout, o primeiro `P-<n>` da primeira mensagem do transcript do subagente, com sufixo `-planejador`, `-modelador`, `-scout`; sem id derivável, `sem-id-<papel>`; `encerrar.py plano` soma as linhas com o prefixo das tarefas e as com o id do plano | F-13; `-revisao` já é a forma da série |
| DAF-16 | `R-10`: `.claude/tools/prevoo.py "<pedido>"` imprime `citado | existe | onde` para todo caminho, símbolo `nome(` e flag do texto; o dever mora na Fase 0 do arquivo do planejador: a §0 recebe a tabela; sem ela, o planejador roda o instrumento como primeiro ato, e linha `não` devolve ao dono antes da campanha | F-14: não há outra residência de condução de sessão de planejamento |
| DAF-17 | `R-12`: o arquivo do `pantonic-consultant` fixa a regra de leitura (cenário, card, evidência e a doutrina que o cenário aponta; nada mais) e `estrategico=` em uma frase; a skill `scrum-master` (*Acionamento do consultor*) traz o molde do despacho com as três entradas | F-16 |
| DAF-18 | `R-13`: `card_check.py` resolve o status pela linha da tarefa em `estado.tsv` (via `caminhos.estado_tsv`) quando o card não tem bullet `Status` | F-17 |
| DAF-19 | `R-14`: a linha do revisor passa a `<tarefa> <veredito> <percentual> bloqueante=<d> recomendacao=<r>`, com `<r>` ∈ {`seguir`, `seguir com ressalva`, `refazer`, `escalar`}, regularizada nas cinco residências de F-18 no mesmo card (G-SURFACE) | F-18 |
| DAF-20 | `R-15`: verbo `backlog.py despachar <ID>` roda os gates mecânicos de F-19, materializa `in-progress`, grava `tarefa-corrente.json`, captura o `<ref>` e imprime card inteiro, `HANDOVER` e `ref=<sha>`; recusa com a razão do primeiro gate que falhar; a skill `scrum-master` (Passos 3 e 4) cita o verbo | F-19 |
| DAF-21 | `R-16`: `modelo.py check` roda o vocabulário sobre a `## 1A` quando ela existe, com rótulo `1A:` nas violações; `show --drift` ganha a seção `## Objetos` com `[~]` por contrato ou propriedade alterada | F-20 |
| DAF-22 | `R-17`: verbo `encerrar.py operacoes --plano <p>` gera o esqueleto de `operacoes.md`; a checagem de cobertura vira opção `--checar` do mesmo verbo | F-21 |
| DAF-23 | `R-18`: `[Console]::OutputEncoding = [Text.Encoding]::UTF8` no topo de `check-readme.ps1` e de `kit_check.ps1` | F-23; mantém os acentos das mensagens |
| DAF-24 | Ordem: os instrumentos que o próprio loop usa primeiro (`TK-94a`, `TK-95a`, `R-06`, `R-07`, `R-09`); itens que editam o mesmo arquivo em série; os três `blocked` por último; a revisão do `README.md` fecha a parte `ready` (§6) | parâmetro de quem conduz; cada instrumento corrigido julga as tarefas seguintes |
| DAF-25 | `R-09`, detalhe (Fase 3b): tarefa do consultor `<ID>-consultor-<n>` (`<n>` = 1 + linhas da série com esse prefixo), como a skill `scrum-master` já fixa; modelo dos papéis não executores = `message.model` da última entrada `assistant` do transcript, normalizado (`opus`, `sonnet`, `haiku`; ausente → `nao-informado`); o `tarefa-corrente.json` não se apaga mais — vale até o despacho seguinte, e é dele que o revisor e o consultor tiram o id; papel fora do mapa usa o nome do agente sem `pantonic-`; `encerrar.py plano` separa `planejador`, `modelador` e `scout` em grupos próprios | F-30: a `DAF-15` não fixava modelo nem numeração, e o estado apagado no fim do executor deixaria o revisor sem id |
| DAF-26 | `R-14`, detalhe: `recomendacao=` no fim da linha; regex da volta do revisor `^(\S+) (\S+) (\d+)%? bloqueante=(\S+)(?: recomendacao=(.+))?$`; frase `M-7` ganha `, recomendação <recomendação>`, com `não informada` quando a linha vem sem o campo; `encerrar.py` e `rdo.py` não mudam | F-28: as cinco residências de F-18 são três, e o fechamento já lê a recomendação do laudo |
| DAF-27 | `R-08`, detalhe: lugares do marco = a célula da tabela *Marcos de validação*, o ato apensado ao fim da `## 0` e o status do plano (Marco 1 `go` com plano `blocked` → `ready`); o cenário do consultor fica fora (insumo que o consultor reescreve); o dossiê de versão sai com `Ato: emenda` | F-12; `GOVERNANCA.md` §3.2 nomeia quatro atos (autoria, emenda, conflito, leitura) |
| DAF-28 | `R-16`, detalhe: sobre a versão pendente, o vocabulário roda sem `V2`, `V4` e `V14` (os cards citam a vigente), sem `V19` e `V20`, e o `V13` sem exigir registro de versões; linha de contrato `[~] <objeto> — contrato: <vigente> => <pendente>`; fixture nova `tests/fixtures/modelo/fluxo-pendente-contrato.md` | F-31 |
| DAF-29 | `R-11`, tabela item × classe: `produto` aplica todos os itens; `ferramentaria` e `doutrina` aplicam os itens 7 e 13 só com gramática ou tabela normativa no plano, e o item 14 só com arquivo compartilhado tocado por dois cards | `DAF-8`; a classe `produto` guarda o protocolo inteiro onde o dano chega ao cliente |
| DAF-30 | `R-15`, detalhe: só tarefa de plano em `ready`; ordem `modelo.py check` (0 ou 2), `card_check` (0), `pytest --co -q` (0 ou 5), captura do `<ref>` (reaproveitado no redespacho da mesma tarefa), `status`; nada escrito na recusa; `tarefa-corrente.json` ganha `ref`; card de tíquete segue pelos passos à mão | F-19; skill `scrum-master` Passos 3 e 4 (exit 2 do modelo segue; o `<ref>` não se recaptura no redespacho) |
| DAF-31 | `R-10`, detalhe: `prevoo.py` extrai caminho (extensão fechada ou `/` final), símbolo (`nome(` ou identificador com `_`; existe se há `def`/`class` num `.py`) e flag (existe se aparece entre aspas num `.py` de `.claude/`); exit 0, 1 ou 2 | F-14: o caso medido (`ler_texto_utf8`, sem parênteses no pedido) exige o identificador com `_` |
| DAF-32 | `R-07`, detalhe: texto do `AE-<n>` = `achado de processo (<alvo>): ` + o trecho antes de `Rota:`; rota = o trecho depois, ou `não declarada no laudo`; texto já presente não se repete | F-11; o fechamento do plano recusa achado sem `**Rota:**` |
| DAF-33 | `R-05`, detalhe: o `show` de plano mantém o teto; no card, o teto vale a partir de `- **Notas de execução:**` e no bloco de achados | `DAF-11`; o plano inteiro no `show` não é despacho |
| DAF-34 | `R-17`, detalhe: destino `caminhos.destino_operacoes`; o verbo não sobrescreve; `--checar` confere a cobertura e os quatro blocos; a skill `entrega-de-encerramento` troca o bloco de código da cobertura pelo verbo | F-21; G-SURFACE |
| DAF-35 | `R-01`, detalhe: frase do piso = nome do TR sem o prefixo, com `_` trocado por espaço (regra mecânica); o teste de camadas cobre `.claude/tools` e `.claude/checks` contra `import` de `tests` e de `caminhos` | `DAF-9`; F-35 |
| DAF-36 | `R-03`, detalhe: a citação na docstring de `backlog.py` sai no mesmo card; a linha de `.claude/settings.json` fica para o dono (§7) | F-33; `I-6` |
| DAF-37 | `R-09`, reparo do consultor (acionamento 1, 2026-09-27): o terceiro teste que afirma o apagamento do estado, `test_tf_hook_executavel_stdin_utf8_nao_falha_e_preserva_invariancia`, entra no passo 2 da `AF-T5`; as asserções de estado seguem o contrato novo (o estado sobrevive em todo mundo) e o par negativo segue discriminando pela série (`tsv_vh is None` contra a linha em `tsv_vs`) | o passo 2 enumerou dois dos três testes que afirmam o apagamento (`tests/test_telemetria_hook.py:288`, `:426-437`); o executor parou pela contingência do card, com razão |
| DAF-38 | `R-09`, reparo do consultor (acionamento 2, 2026-09-27): `test_tf_ger_19_userpromptsubmit_sem_volta_pendente` e `test_tf_ger_25_show_no_meio_da_janela_nao_encerra` entram na contingência da `AF-T6` ao lado de `test_tf_ger_7_agente_de_volta_revisor` — os três afirmam a frase `M-7` antiga e caem só pelo sufixo `, recomendação não informada`. O trabalho parcial do primeiro despacho foi revertido pelo consultor aos quatro `Arquivos-alvo` da ref do despacho (`543229b`), porque o quarto gate (`card_check`, mundo `antes` para tarefa não `done`) o recusava (4 itens divergentes, exit 1); o redespacho parte da árvore limpa | a contingência nomeou um dos três testes que embutem a frase antiga (`tests/test_progresso_hook.py:724`, `:997`); medido: suíte com o trabalho parcial `2 failed, 466 passed`, só esses dois; com o literal trocado numa cópia do arquivo, `43 passed`; `tests/test_encerrar.py:107` traz a frase antiga como entrada de fixture do painel e não cai; revertida a árvore: `card_check` exit 0, suíte `466 passed` |
| DAF-39 | `R-13`, reparo do consultor (acionamento 3, 2026-09-27): a fixture `tests/fixtures/card_check/P-0-pasta/plano.md` do passo 2 da `AF-T7` ganha em `CP-T1` e `CP-T2` o bullet `- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.` (a forma de `plano-exemplo.md`), e as quatro Verificações passam de esperadas a medidas. O trabalho parcial do primeiro despacho foi revertido pelo consultor à ref do despacho (`2f63d41`) em `card_check.py` e `test_card_check.py`, e a pasta `P-0-pasta/` apagada, porque o quarto gate (`card_check`, mundo `antes`) o recusava; o redespacho parte da árvore limpa | o conteúdo literal da fixture não declarava `Arquivos-alvo` nem `Entregável`, e `rdo.extrair_dossie` (`rdo.py:348-355`) recusa o card (`tem nenhum`); a Verificação 1 saiu publicada sem ensaio. Medido com a fixture reparada: produto novo `CP-T1` exit 0 e `CP-T2` exit 0; código da ref `CP-T1` exit 1 (divergência `a` contra `b`) e `CP-T2` exit 0 — o TF discrimina; `-k estado_tsv` `2 passed`; `test_card_check.py` inteiro com a troca `20 passed` (a contingência não dispara). Revertida a árvore: V1 exit 1, V2 exit 5, suíte `468 passed`, `check-drift` exit 0 |
| DAF-40 | `R-12`, reparo do consultor (acionamento 4, 2026-09-27, `AE-10`, regra `A8`): o predicado `_plano_em_esboco` de `.claude/tools/backlog.py` passa a exigir `plano.estado_arquivo is not None` — só plano em pasta é esboço, como diz o `Domínio` da `AF-T8` — e `tests/test_backlog.py` ganha o TR `test_tr_check_plano_legado_blocked_no_contador_segue_acusando_c10` (fixture `contador_inbox`, plano legado com `Status` `blocked`, id = contador, fora do inbox → `C-10`). Escrita de código do consultor em instrumento do loop, declarada aqui: nenhum card cobre o reparo (`AF-T8` `done`) e a diretiva do dono de 2026-09-26 veda card novo por ajuste | laudo da `AF-T8` (ressalva 91%): o predicado omitia a cláusula *plano em pasta* e silenciava o `C-10` do plano legado `blocked`. Medido: defeito reproduzido em cópia da fixture (`C-10` ausente); com o reparo, `C-10` volta; o TR novo cai com a cláusula removida e passa com ela; `check --repo tests/fixtures/backlog/esqueleto` exit 0; `backlog.py check` real exit 0; suíte `473 passed`; `check-drift` exit 0; `card_check` `AF-T8` e `AF-T9` exit 0 |
| DAF-41 | `R-15`, reparo do consultor (acionamento 5, 2026-09-27): o passo 2 da `AF-T10` passa a montar a cópia temporária em quatro tempos — fixture, `rdo.py` e `caminhos.py` do repositório em `.claude/tools/` da cópia, `plano.md` da cópia sobrescrito com `GAM-T1` e `GAM-T2` literais (cada um com `Objetivo`, `Entregável` nenhum, `Verificação` e `Pronto quando`; `GAM-T2` com `antes` `z`), `git init` e commit — e o piso da suíte passa a `475` medido (`478` com os três testes). Impedimento procedente; nenhuma edição do executor a reverter (árvore dos três alvos igual à ref `9f6bf68`). O `AE-11` não entra neste card: o ponteiro do bloco de achados é do `show` (operação da `AF-T9`), não do despacho (`OP-10`), e a diretiva do dono veda card novo — segue auditoria final | o passo 2 dava só a `Verificação` de `GAM-T1`, e `rdo.extrair_dossie` (`rdo.py:345-351`) exige também `Pronto quando` e um entre `Arquivos-alvo`/`Entregável`; ensaiada a cadeia numa cópia, apareceu o segundo defeito que o executor ainda não tinha alcançado: `card_check.py:54` carrega `rdo.py` de `<root>/.claude/tools/` (e `rdo.py` carrega `caminhos.py`), ausentes na fixture. Medido na cópia montada como o passo 2 manda: `modelo.py check` exit 2, `card_check` `GAM-T1` exit 0 e `GAM-T2` exit 1, `pytest --co -q` exit 5, `--capturar-ref` exit 0. Na árvore: V1 exit 2, V2 exit 5, V3 `0 0`, suíte `475 passed`, `check-drift` exit 0 |
| DAF-42 | `R-15`, reparo do consultor (acionamento 6, 2026-09-27, `AE-14`, regra `A8`): os quatro `subprocess.run` de `despachar` (`.claude/tools/backlog.py`, `modelo.py`, `card_check.py`, `pytest --co`, `review_evidence.py --capturar-ref`) passam a decodificar com `encoding="utf-8", errors="replace"` — os irmãos escrevem o stderr em UTF-8, e a codificação do locale (cp1252 no Windows) punha mojibake na razão ou devolvia stderr `None` (traceback em `_ultima_linha_stderr`) —, e o TR `test_tr_despachar_recusa_no_primeiro_gate_sem_escrever` ganha o assert `"não fecham" in erro` sobre o texto da razão. Escrita de código do consultor em instrumento do loop, declarada aqui: nenhum card cobre o reparo (`AF-T10` `done`) e a diretiva do dono de 2026-09-26 veda card novo por ajuste | laudo da `AF-T10` (ressalva 91%), dimensão `criterio-de-pronto` parcial: contrato *a razão é a última linha do stderr* violado pela decodificação. Medido: com o assert novo e o produto da ref, o TR cai (`'não fecham'` ausente; a razão chega `nÃ£o fecham`); com o reparo, `-k despachar` `3 passed`; suíte `478 passed`; `backlog.py check`, `modelo.py check` e `check-drift` exit 0 |
| DAF-43 | `R-15`, reparo do consultor (acionamento 7, 2026-09-27, `AE-17`/`AE-18`, regra `A8`): dois defeitos do verbo `marco` (`.claude/tools/encerrar.py`, `gravar_marco`) — (a) a célula se reescrevia partindo a linha em toda barra vertical, cego à barra escapada que o próprio verbo emite, e regravar marco cuja frase tinha barra vertical deixava resto do veredito velho: agora o corte é pela regex `_MARCO_COLUNA_RE`, que só parte na barra não precedida de contrabarra; (b) Marco 1 `go` com transição recusada gravava o plano antes de sair exit 1: agora `backlog.checar_transicao` roda antes da escrita (1). Um TR por caminho em `tests/test_encerrar.py` (`test_tr_marco_regravar_celula_com_pipe_escapado_nao_deixa_resto`, `test_tr_marco_go_com_transicao_recusada_nao_escreve`). Escrita de código do consultor em instrumento do loop, declarada aqui: nenhum card cobre o reparo (`AF-T12` `done`) e a diretiva do dono de 2026-09-26 veda card novo por ajuste (sem `AF-T12a`). Linha apensada pelo acionamento 8, que achou a decisão só no cenário e nos `AE-17`/`AE-18` | laudo da `AF-T12` (ressalva 91%). Medido: os dois TRs vermelhos antes do reparo, verdes depois; `test_encerrar` `31 passed`; suíte `484 passed`; `backlog.py check`, `modelo.py check` e `check-drift` exit 0 |
| DAF-44 | `R-15`, reparo do consultor (acionamento 8, 2026-09-27, `AE-19`, regra `A8`): o `--checar` de `encerrar.py operacoes` (`checar_esqueleto_operacoes`) ganha a lista `sem seção` — toda tarefa não `cancelled` sem o cabeçalho `` ## `<ID>` — `` — e a CLI passa a imprimir três linhas, `nao citados`, `sem seção` e `sem os quatro blocos`, exit `0` só com as três em `nenhum`. Sem ela, seção apagada inteira passava: `nao citados` conta o ID em qualquer lugar e a tabela do arco que o esqueleto gera já cita toda tarefa; `sem os quatro blocos` só itera seções existentes. A skill `entrega-de-encerramento` (Procedimento, item 6) e o `--help` descrevem a linha nova. TR novo `test_tr_esqueleto_de_operacoes_checar_secao_apagada` (apaga a seção de `ALF-T1` inteira) e o TF `test_tf_esqueleto_de_operacoes_checar_cobertura` passa a exigir `sem seção: nenhum`. Escrita de código do consultor em instrumento do loop, declarada aqui: nenhum card cobre o reparo (`AF-T13` `done`) e a diretiva do dono de 2026-09-26 veda card novo por ajuste (sem `AF-T13a`) | laudo da `AF-T13` (aprovado 100%, achado de processo): contrato do `--checar` sem poder discriminante para seção ausente, contra o item 6 da skill. Medido: o TR novo cai no produto da `AF-T13` (exit 0 com `nenhum`/`nenhum`) e passa com o reparo; `test_encerrar` `35 passed`; suíte `488 passed`; `backlog.py check`, `modelo.py check --plano` e `check-drift` exit 0; Verificação 3 da `AF-T13` segue `2 0` |
| DAF-45 | `R-15`, reparo do consultor (acionamento 9, 2026-09-27, `AE-25`, regra `A8`): o `prevoo.py` (`AF-T17`) passa a normalizar cada token antes de classificá-lo (`_normalizar`) — tira à esquerda crase, aspas, `*` e abre-parêntese/colchete/chave; à direita crase, aspas, `*`, pontuação de frase (`,` `.` `;` `:` `!` `?`) e fecha-parêntese/colchete/chave; de flag, o `=<valor>` — e símbolo passa a ser o nome antes do primeiro `(` com ou sem argumentos até o `)`. O ponto inicial de `.claude/` fica. Três TRs novos em `tests/test_prevoo.py`, um por forma de citação (`test_tr_prevoo_citacao_em_crase_e_pontuada`, `test_tr_prevoo_chamada_com_parenteses_fechados`, `test_tr_prevoo_flag_com_pontuacao`), apensados a `tests/piso_comportamental.txt`; nenhum traz `def <nome>(` literal (armadilha da Verificação 1). Escrita de código do consultor em instrumento do kit, declarada aqui: nenhum card cobre o reparo (`AF-T17` `done`) e a diretiva do dono de 2026-09-26 veda card novo por ajuste (sem `AF-T17a`) | laudo da `AF-T17` (ressalva 91%, `criterio-de-pronto` parcial): o pré-voo silenciava citação em crase, com pontuação e chamada com parênteses fechados — o caso medido que motivou o card passava sem alarme. Medido antes do reparo, contra o repositório: os três textos do laudo saíam tabela vazia exit 0, tabela vazia exit 0 e `--plano; \| não` exit 1; depois, `ler_texto_utf8 \| não` exit 1, `funcao_inexistente \| não` exit 1 e `--plano \| sim` exit 0. `test_prevoo` `6 passed`; suíte `498 passed`; `dead_code`, `ratchet_piso`, `backlog.py check`, `modelo.py check --plano` e `check-drift` exit 0; Verificação 1 da `AF-T17` segue `ler_texto_utf8 \| não \| —` |
| DAF-46 | `R-02`, rodada de replanejamento (2026-09-27), revoga a `DAF-6`, na rota que o dono decidiu (opção A da avaliação da F-36): o batedor deixa de rodar no modelo barato e passa a rodar em Opus, com a ferramenta de comando (`Bash`), para responder também a pergunta "rode `<comando exato>`" da campanha do planejador, que fica como está; leitura pontual (âncora conhecida, grep de string exata) quem precisa do dado faz direto; varredura ampla segue delegada ao batedor, para proteger o contexto de quem pede. O batedor não roda comando que escreva na árvore e conta e filtra pela própria ferramenta, nunca somando lista à mão. A mudança alcança o agente do projeto e o canônico global (`.claude/global/agents/context-scout.md`) e toda residência do kit que manda a coleta ao modelo barato. Card corretivo `AF-T19a` da `OP-19`; `AF-T19` `cancelled`. Fora: o `pantonic-benchmarker` (Haiku), que não é batedor, e o `apply` da projeção global em `~/.claude` (ato do dono) | ato do dono, verbatim: *"Prosseguir com a recomendação A, e ajustar o desvio da ferramenta inacessível ao batedor"*; F-36: nas demandas pequenas o modelo barato economiza centavos, e nas grandes errou em silêncio a custo de token próximo ao do Opus; a regra "contar pela ferramenta" responde ao único erro medido fora do Haiku (filtro manual do Sonnet) |
| DAF-47 | reparo do consultor (acionamento 12, 2026-09-27, `AF-T19a` `blocked` `premissa` no passo 13): a contingência que parava se o `generate` mudasse de `.claude/README.md` qualquer linha além da do `pantonic-scout` contradizia a restrição `check-drift` exit 0 — com a árvore já fora de sincronia com o frontmatter, só o `generate` inteiro a satisfaz. Nova contingência: parar só se o `generate` mudar fora das duas regiões geradas ou se o `check-drift` não sair 0; a ressincronia de `pantonic-consultant`, `pantonic-planner`, `modelo-por-fase`, `fatos-frescos` e `mensagem-ao-dono` fica (todas em arquivo-alvo, todas cópia do frontmatter da árvore). Trabalho do executor mantido; o card volta `ready` com o estado de partida (passos 1-13 aplicados) e as Verificações medidas. Impedimento procedente | medido pelo consultor na árvore: Verificações 1 e 2 `True True True`, Verificação 3 `8`, `frontmatter_yaml` exit 0, suíte `498 passed`, `check-drift` exit 0 (`10 agente(s), 13 skill(s)`); cada trecho `novo:` dos passos 4 a 12 presente (grep); `fatos-frescos/` e `mensagem-ao-dono/` estão fora do git (`??`) e nenhum card do plano as cria |

## 4. Invariantes de execução

Valem para todos os cards; cada card repete, inline, a parte que o vincula.

- **I-1 Suíte:** `python -m pytest -q` sem falha ao fim de todo card; o piso é o total re-medido no
  despacho mais os testes novos do card; `452 tests collected` (2026-09-27) é referência histórica,
  nunca aceite.
- **I-2 Drift do kit:** `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0
  com a linha iniciada por `kit_check: check-drift OK` ao fim de todo card.
- **I-3 Fronteira de arquivo:** o card só edita os seus `Arquivos-alvo`; o WIP não commitado da árvore
  (F-26) não se toca, não se reverte e não se commita; nenhum card commita.
- **I-4 Instrumento do kit:** `.claude/tools/*.py` não importa de `tests/` e carrega `caminhos.py` por
  caminho (relatório:155).
- **I-5 Sem tíquete novo:** nenhum card abre tíquete no diário (F-3); achado vai à linha de retorno.
- **I-6 Configuração do harness:** nenhum card edita `.claude/settings*.json` nem `.claude/projecoes.json`.
- **I-7 Literal de aceite:** comando com crase, asterisco ou barra invertida vai em bloco cercado;
  `Select-String` leva `-SimpleMatch`; cada linha de `Verificação` publica o `antes` medido e o
  `depois` marcado `(esperado, não ensaiado)` (DAF-4).
- **I-8 Invocação do condutor:** até o card da `R-06` fechar, quem conduz invoca os instrumentos com
  `python <script>`, sem `-X utf8`, para o painel não cegar (F-10).

## 5. Tarefas

Um card por operação da `### 1.2`, na ordem das operações: `AF-T<n>` materializa `OP-<n>`. Plano em
pasta: o estado de cada card é a linha dele em `estado.tsv`. Em toda `Verificação`, o valor `antes`
foi **medido na autoria** (2026-09-27, `card_check --mundo antes` exit 0) e o valor `depois` é o
**esperado, não ensaiado** (`DAF-4`): a marca `(esperado, não ensaiado)` segue cada linha.

### AF-T1 — Com `--desde`, o resumo de diferenças do dossiê sai do recorte dos tocados [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** O instrumento de evidência passa a resumir as diferenças da entrega pelo mesmo recorte da lista de arquivos tocados, sem o trabalho em andamento de fora da tarefa.
- **Fundamento:** `DAF-3` (o card do Apêndice A do relatório, `TK-94a`, é a fonte; `antes` re-medidos), `F-24`, `F-26`; `DAF-24` (primeiro item: o instrumento corrigido julga as tarefas seguintes).
- **Operação do modelo:** `OP-1`
  - OP-1: O instrumento de evidência passa a resumir as diferenças da entrega pelo mesmo recorte da lista de arquivos tocados, sem o trabalho em andamento de fora da tarefa.
  - precisa de: relatório de auditoria — Ninguém altera: é a fonte de cada item que o plano aplica.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/` (ferramentaria do hub). Carrega módulo irmão por caminho (`importlib.util.spec_from_file_location`), nunca por `import`; não importa de `tests/`.
- **Caso medido que motivou:** no dossiê de evidência de duas tarefas do plano fictício da auditoria (2026-09-27), o bloco `## Diff (git diff --stat)` listou os 59 arquivos do trabalho não commitado da árvore contra `HEAD`, nenhum da entrega, e deixou fora os alvos entregues não rastreados; só `## Arquivos tocados` respeitou o `--desde`. Causa: `coletar_diff_stat(root)` roda `git diff HEAD --stat` e não recebe o `desde` que `montar_documento` já tem. O protótipo do consultor (fora da árvore) gravou a árvore de trabalho num índice temporário, como `capturar_ref` faz, e rodou `git diff --stat <ref> <árvore> -- <tocados>`: deu os mesmos 10 arquivos de `## Arquivos tocados`, o não rastreado incluído.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Contratos/classes:** `coletar_diff_stat(root: Path, desde: str | None = None) -> str`; `montar_documento` repassa o `desde` que já recebe. Com `desde`, o bloco `## Diff (git diff --stat)` lista exatamente os arquivos da seção `## Arquivos tocados` do mesmo recorte — rastreados e não rastreados —, cada um com as linhas mudadas desde `<ref>`; sem arquivo tocado, o bloco traz `(sem diferenças)`. Com lista de tocados vazia, o `git diff` não roda sem caminho (sem caminho ele devolveria a árvore inteira). Árvore de trabalho, índice real e lista de stash saem como entraram. O cabeçalho do bloco não muda. Sem `desde`, o bloco é o de hoje (`git diff HEAD --stat`).
- **Passos:**
  1. Em `coletar_diff_stat`, acrescentar o parâmetro `desde`; com `desde`, gravar a árvore de trabalho num índice temporário (variável `GIT_INDEX_FILE` apontando para arquivo em diretório temporário, como `capturar_ref` faz) e rodar `git diff --stat <desde> <árvore> -- <tocados>`, com `<tocados>` = a lista que `coletar_arquivos_tocados` devolve para o mesmo `desde`.
  2. Em `montar_documento`, passar `desde` a `coletar_diff_stat`.
  3. Escrever os dois testes da seção `Testes`.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 2 testes novos (referência datada: `452 passed`, 2026-09-27).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; o trabalho não commitado da árvore fora deles não se toca, não se reverte e não se commita; nenhum commit.
  - Nenhum tíquete novo no diário; achado vai à linha de retorno.
- **Não fazer:** não mudar `coletar_arquivos_tocados` nem `capturar_ref`; não tocar `_REGISTRO_ORQUESTRACAO` (é da `AF-T2`); não mudar o cabeçalho do bloco nem o teto de caracteres dos trechos; não usar `git stash push` nem nada que escreva na árvore, no índice real ou na lista de stash.
- **Contingências:**
  - se um teste existente de `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_diff_stat_desde_recorta_como_os_tocados` — repositório temporário com baseline commitado; um rastreado alterado antes da captura (trabalho alheio); `<ref>` por `capturar_ref`; depois, um rastreado alterado e um não rastreado criado: o bloco `## Diff` de `montar_documento(..., desde=<ref>)` cita os dois arquivos da entrega e não cita o trabalho alheio (a regra antiga, `git diff HEAD --stat`, citaria o alheio e não citaria o não rastreado). TR `test_tr_diff_stat_desde_sem_tocados_sai_sem_diferencas` — `<ref>` capturado e nada mudado depois: o bloco traz `(sem diferenças)`. Suítes: `tests/test_review_evidence.py`, depois a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_review_evidence.py -q -k "diff_stat_desde"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado)
  2. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
  3. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
- **Pronto quando:**
  - dossiê de evidência.recorte do resumo de diferenças — com recorte informado, o resumo lista exatamente os arquivos tocados desde o recorte, os novos inclusive; sem recorte, nada muda — Verificação 1 (e a suíte segue verde, Verificação 2)
- **Fora do escopo desta tarefa:** o balde de registro da orquestração para `docs/audits/` (`AF-T2`).
- **Handover:** 2026-09-27 · para `AF-T2`
  - **Entregue:** coletar_diff_stat(root, desde=None) em .claude/tools/review_evidence.py:232 recorta o bloco ## Diff pelos tocados desde <ref> (indice temporario, rastreados e nao rastreados); montar_documento repassa desde; testes em tests/test_review_evidence.py:1206 e :1238
  - **Contrato:** com --desde, o bloco ## Diff do dossie de evidencia lista exatamente os arquivos de ## Arquivos tocados; sem tocados sai (sem diferencas); sem --desde nada muda
  - **Não refazer:** o recorte do resumo de diferencas; a guarda de tocados vazio ja existe por inspecao
  - **Pendente:** nenhum

### AF-T2 — O relatório de auditoria de quem conduz entra no balde de registro da orquestração [Sonnet · esforço low · classe implementacao]
- **Objetivo:** O instrumento de evidência passa a contar o relatório de auditoria de quem conduz como registro da condução, e não como entrega fora do alvo da tarefa.
- **Fundamento:** `DAF-3` (o card do Apêndice A do relatório, `TK-95a`, é a fonte; `antes` re-medidos), `F-24`.
- **Depende de:** `AF-T1`
- **Operação do modelo:** `OP-2`
  - OP-2: O instrumento de evidência passa a contar o relatório de auditoria de quem conduz como registro da condução, e não como entrega fora do alvo da tarefa.
  - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/`; carrega módulo irmão por caminho; não importa de `tests/`.
- **Caso medido que motivou:** a evidência de uma tarefa do plano fictício da auditoria (`--desde a1bea86`, 2026-09-27) deu `docs/audits/AUDITORIA_ENCERRAMENTO_ESTAGIO1_2026-09-27.md` como "fora dos alvos e sem atribuição" e deixou o veredito mecânico aberto: o arquivo era o relatório que quem conduz escrevia na janela, não entrega do card. `_REGISTRO_ORQUESTRACAO` tem `docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/plans/` e `docs/RDO/`, e não `docs/audits/`, onde a orquestração grava auditoria. Com `docs/audits/` no balde, a mesma evidência sai `conforme`.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Contratos/classes:** `_eh_registro_orquestracao(caminho: str) -> bool` devolve `True` para caminho sob `docs/audits/`; a precedência de `confrontar_escopo` não muda: arquivo de `docs/audits/` que é alvo do card segue coberto (`da entrega`). O balde vale no dossiê, em `confrontar_escopo` e no `--atribuir`.
- **Passos:**
  1. Acrescentar `docs/audits/` à tupla `_REGISTRO_ORQUESTRACAO`.
  2. Na docstring do módulo, o trecho depois de `antigo:` vira o trecho depois de `novo:` (sem quebra nova e sem refluxo; o rótulo não entra no arquivo):

     ```text
     antigo: `docs/plans/`, `docs/RDO/`); ato do dono fora
     novo: `docs/plans/`, `docs/RDO/`, `docs/audits/`); ato do dono fora
     ```
  3. Na docstring de `_eh_registro_orquestracao`, o trecho depois de `antigo:` vira o trecho depois de `novo:` (sem quebra nova e sem refluxo; o rótulo não entra no arquivo):

     ```text
     antigo: telemetria, plano, RDO. Não é atribuível
     novo: telemetria, plano, RDO, relatório de auditoria. Não é atribuível
     ```
  4. Escrever os dois testes da seção `Testes`.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 2 testes novos (referência datada: `452 passed`, 2026-09-27).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Nenhum tíquete novo no diário.
- **Não fazer:** não mudar a precedência de `confrontar_escopo`; não criar declaração de trabalho em andamento da orquestração no despacho (rota descartada pelo consultor: ainda dependeria de quem conduz lembrar); não tocar `coletar_diff_stat` (é da `AF-T1`).
- **Contingências:**
  - se um teste existente de `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_relatorio_de_auditoria_sai_como_registro_da_orquestracao` — `docs/audits/AUDITORIA_X.md` tocado fora dos alvos de `T1`: o documento traz `Registro da orquestração (não atribuível a tarefa)` e `Veredito mecânico: conforme`. TR `test_tr_relatorio_de_auditoria_alvo_do_card_segue_coberto` — card cujo alvo é `docs/audits/AUDITORIA_X.md`: a atribuição do arquivo é `da entrega` (a regra concorrente, "tudo em `docs/audits/` é registro", daria registro da orquestração).
- **Verificação:**
  1. `python -c "import importlib.util as u;from pathlib import Path;s=u.spec_from_file_location('r',Path('.claude/tools/review_evidence.py'));m=u.module_from_spec(s);s.loader.exec_module(m);print(m._eh_registro_orquestracao('docs/audits/AUDITORIA_X.md'))"` → `True` — antes `False`, depois `True` (esperado, não ensaiado)
  2. `python -c "from pathlib import Path;c=chr(96);t=Path('.claude/tools/review_evidence.py').read_text(encoding='utf-8');print(t.count(c+'docs/RDO/'+c+')'),t.count(c+'docs/RDO/'+c+', '+c+'docs/audits/'+c+')'),t.count('plano, RDO, relatório de auditoria'))"` → `0 1 1` — antes `1 0 0`, depois `0 1 1` (esperado, não ensaiado)
  3. `python -m pytest tests/test_review_evidence.py -q -k "auditoria"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado)
  4. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
  5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
- **Pronto quando:**
  - dossiê de evidência.atribuição do relatório de auditoria — cai como registro da condução e não pesa no veredito; quando é alvo do card, segue coberto — Verificações 1 e 3 (as duas docstrings nomeiam a pasta, Verificação 2)
- **Fora do escopo desta tarefa:** edição de quem conduz fora de `docs/audits/` na janela segue para a reconciliação do revisor, como hoje.
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** docs/audits/ na tupla _REGISTRO_ORQUESTRACAO (.claude/tools/review_evidence.py:407); docstrings do modulo (:51) e de _eh_registro_orquestracao atualizadas; testes em tests/test_review_evidence.py:597 e :618
  - **Contrato:** arquivo tocado sob docs/audits/ fora dos alvos sai como 'Registro da orquestracao' e nao pesa no veredito mecanico; alvo do card em docs/audits/ segue 'da entrega'
  - **Não refazer:** o balde de docs/audits/; o recorte do ## Diff (AF-T1)
  - **Pendente:** nenhum

### AF-T3 — O painel do gerente reconhece o programa depois das opções do interpretador [Sonnet · esforço low · classe implementacao]
- **Objetivo:** O painel do gerente passa a reconhecer o programa chamado quando a chamada traz opções do interpretador antes dele.
- **Fundamento:** `DAF-12`, `F-10`, `F-32`.
- **Operação do modelo:** `OP-3`
  - OP-3: O painel do gerente passa a reconhecer o programa chamado quando a chamada traz opções do interpretador antes dele.
  - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.
- **Camada e fronteira:** gancho do kit em `.claude/tools/progresso_hook.py` (roda em `PreToolUse`, `PostToolUse` e `Stop`); falha aberta, sem bloquear a chamada; não importa de `tests/`.
- **Arquivos-alvo:**
  - `.claude/tools/progresso_hook.py`
  - `tests/test_progresso_hook.py`
  - `docs/ARMADILHAS_DE_FERRAMENTA.md`
- **Contratos/classes:** `_programa(tokens: list[str]) -> tuple[str, list[str]] | None` — assinatura inalterada. Regra nova, sobre os tokens depois do interpretador: `-X` e `-W` consomem também o token seguinte (o valor) — e, na forma colada (`-Xutf8`, `-Wignore`), só o próprio token; `-m <módulo>` devolve `(<módulo>, tokens depois do módulo)`; `-c` devolve `None` (não há script); qualquer outro token iniciado por `-` consome só a si mesmo, como hoje; o primeiro token que não começa por `-` é o script, como hoje.
- **Passos:**
  1. Reescrever o laço de `_programa` com a regra de `Contratos/classes`.
  2. Escrever os três testes da seção `Testes`, no molde de `test_tf_ger_4_estado_mudado` (fixture `estado`, `raiz`; `payload_next` com `=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]`).
  3. Apensar ao fim da tabela de `docs/ARMADILHAS_DE_FERRAMENTA.md` a linha abaixo (as quebras são as do bloco: uma linha só):

     ```text
     | `Python` (linha de comando) | opção do interpretador antes do script (`-X utf8`, `-W`, `-m`, `-c`) desloca o nome do programa: quem lê a linha pulando só o token iniciado por `-` toma o valor da opção (`utf8`) pelo script | (`R-06` da auditoria de encerramento do estágio 1, 2026-09-27: com `python -X utf8`, o painel do gerente calou `M-2`, `M-5`, `M-10`, `M-13` e `M-18`) | quem lê a linha de comando pula a opção junto com o valor dela (`-X`, `-W`), toma o módulo depois de `-m` como programa e não procura script depois de `-c` — é o que `progresso_hook._programa` faz. |
     ```
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 3 testes novos (referência datada: `452 passed`, 2026-09-27).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - O gancho segue em falha aberta: exceção dentro dele nunca bloqueia a chamada.
- **Não fazer:** não mudar `FRASES` nem as frases do painel; não mudar a linha da armadilha do console cp1252 já existente na tabela; não mudar o `.claude/settings.json` nem o `.claude/projecoes.json`.
- **Contingências:**
  - se um teste existente de `tests/test_progresso_hook.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_opcao_do_interpretador_com_valor_gera_m2` — `python -X utf8 .claude/tools/backlog.py status TLG-T9 in-progress` gera a frase `M-2` (`Tarefa "Um título de teste": gates aprovados; vou materializar in-progress e gravar o ponto de partida.`); a regra antiga toma `utf8` pelo script e não gera. TR `test_tr_opcao_do_interpretador_sem_valor_segue_gerando_m2` — `python -u .claude/tools/backlog.py status TLG-T9 in-progress` gera `M-2` (a regra concorrente "toda opção consome o token seguinte" tomaria `status` pelo script e não geraria). TF `test_tf_opcao_do_interpretador_m_e_c` — `_programa(['python','-m','pytest','-q'])` devolve `('pytest', ['-q'])` e `_programa(['python','-c','print(1)'])` devolve `None`.
- **Verificação:**
  1. `python -m pytest tests/test_progresso_hook.py -q -k "opcao_do_interpretador"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado)
  2. `python -c "import importlib.util as u;from pathlib import Path;s=u.spec_from_file_location('p',Path('.claude/tools/progresso_hook.py'));m=u.module_from_spec(s);s.loader.exec_module(m);print(m._programa(['python','-X','utf8','.claude/tools/backlog.py','status'])[0])"` → `backlog.py` — antes `utf8`, depois `backlog.py` (esperado, não ensaiado)
  3. `python -c "from pathlib import Path;print(Path('docs/ARMADILHAS_DE_FERRAMENTA.md').read_text(encoding='utf-8').count('progresso_hook._programa'))"` → `1` — antes `0`, depois `1` (esperado, não ensaiado)
  4. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
  5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
- **Pronto quando:**
  - painel do gerente.leitura de chamada com opção do interpretador — com qualquer opção do interpretador, o painel reconhece o programa e mostra as mesmas linhas da chamada sem opção — Verificações 1 e 2 (a armadilha registrada, Verificação 3)
- **Fora do escopo desta tarefa:** a recomendação do laudo na linha do revisor (`AF-T6`, que também edita `progresso_hook.py`).
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** _programa em .claude/tools/progresso_hook.py:293 pula -X/-W com valor (separado ou colado), devolve o modulo apos -m, None para -c; testes em tests/test_progresso_hook.py:1362, :1379, :1396; armadilha nova em docs/ARMADILHAS_DE_FERRAMENTA.md:16
  - **Contrato:** o painel gera as mesmas linhas para 'python -X utf8 <script>' e 'python <script>'; assinatura de _programa inalterada
  - **Não refazer:** a leitura das opcoes do interpretador no painel
  - **Pendente:** nenhum

### AF-T4 — O fechamento transcreve o achado de processo do laudo para os achados do plano [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** O fechamento de tarefa passa a copiar para os achados do plano cada achado de processo que o laudo traz, com a rota dele.
- **Fundamento:** `DAF-13`, `DAF-32`, `F-11`.
- **Operação do modelo:** `OP-4`
  - OP-4: O fechamento de tarefa passa a copiar para os achados do plano cada achado de processo que o laudo traz, com a rota dele.
  - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/encerrar.py`; carrega `backlog.py`, `rdo.py` e `telemetria.py` por caminho, como hoje; não importa de `tests/`.
- **Domínio:** *achado de processo* — linha da seção `## Achado de processo` do laudo que `rdo.py laudo` grava, na tabela `| alvo | achado |` (`alvo` ∈ `dossiê`, `doutrina`, `rubrica`, `modelo`), ou o corpo `nenhum` quando não há achado. Invariante: todo `AE-<n>` de `## Achados da execução` traz `**Rota:**` (o fechamento do plano recusa achado sem rota).
- **Arquivos-alvo:**
  - `.claude/tools/encerrar.py`
  - `tests/test_encerrar.py`
  - `.claude/skills/scrum-master/SKILL.md`
- **Contratos/classes:** função nova `achados_do_laudo(texto_laudo: str) -> list[tuple[str, str]]` — `(texto, rota)` por linha da tabela; `texto` = `achado de processo (<alvo>): ` + o trecho do achado antes da primeira ocorrência de `Rota:`, com `strip()`; `rota` = o trecho depois de `Rota:`, com `strip()`, ou `não declarada no laudo` quando o achado não traz `Rota:` ou o trecho sai vazio. `fechar_tarefa` grava, depois dos `--achado` de hoje, um `AE-<n>` por par de `achados_do_laudo`, pela `apensar_achado` existente, **pulando** o par cujo `texto` já ocorre em alguma entrada de `achados_do_plano(plano_path)` ou foi gravado antes no mesmo fechamento. `--achado` continua como está.
- **Passos:**
  1. Escrever `achados_do_laudo` e chamá-la em `fechar_tarefa` sobre o texto do mesmo arquivo de laudo que o fechamento já passa a `ler_laudo` (lido com `encoding="utf-8"`); gravar os pares depois do laço dos `--achado`, pela `apensar_achado`, com a regra de não repetir de `Contratos/classes`; somar os ids gravados à linha `Achados:` do texto humano.
  2. Em `.claude/skills/scrum-master/SKILL.md`, Passo 9, a linha abaixo depois de `antigo:` vira as duas linhas depois de `novo:` (as quebras são as do bloco; os rótulos não entram no arquivo):

     ```text
     antigo:
       (5) cada `--achado` vira `AE-<n>` com `**Rota:**` em `## Achados da execução` do plano. O
     novo:
       (5) cada linha da tabela `## Achado de processo` do laudo e cada `--achado` viram `AE-<n>` com
       `**Rota:**` em `## Achados da execução` do plano, sem repetir achado do laudo já registrado. O
     ```
  3. Escrever os três testes da seção `Testes`, com laudo de fixture igual à constante `LAUDO` de `tests/test_encerrar.py` acrescida, antes de `## Lições aprendidas na tarefa`, da seção `## Achado de processo` com a tabela `| alvo | achado |`.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 3 testes novos (referência datada: `452 passed`, 2026-09-27).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - O fechamento continua recusando sem escrever quando falta insumo; a leitura do achado do laudo nunca é motivo de recusa.
- **Não fazer:** não mudar `rdo.py` nem a forma da tabela que `rdo.py laudo` grava; não mudar `apensar_achado` nem a forma da entrada `AE-<n>`; não remover `--achado`.
- **Contingências:**
  - se o laudo não tiver a seção `## Achado de processo`, ou ela trouxer `nenhum` → nenhum achado do laudo; seguir.
  - se um teste existente de `tests/test_encerrar.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_achado_do_laudo_vira_ae_com_rota` — laudo com a linha `| dossiê | o card não citava o arquivo de teste. Rota: card corretivo ALF-T1a |`: o plano ganha `- **AE-2** (`ALF-T1`, fechamento, 2026-09-26) — achado de processo (dossiê): o card não citava o arquivo de teste. **Rota:** card corretivo ALF-T1a` (a regra de hoje não grava nada). TR `test_tr_achado_do_laudo_repetido_nao_duplica` — plano que já tem uma entrada com `achado de processo (dossiê): o card não citava o arquivo de teste.`: nenhum `AE-<n>` novo (a regra concorrente, "grava toda linha do laudo", duplicaria). TF `test_tf_achado_do_laudo_sem_rota_declarada` — linha `| doutrina | a skill não nomeia o gate. |`: o `AE-<n>` traz `**Rota:** não declarada no laudo`.
- **Verificação:**
  1. `python -m pytest tests/test_encerrar.py -q -k "achado_do_laudo"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado)
  2. `python -c "from pathlib import Path;print(Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8').count('cada linha da tabela'))"` → `1` — antes `0`, depois `1` (esperado, não ensaiado)
  3. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
  4. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
- **Pronto quando:**
  - fechamento de tarefa.achado de processo do laudo — cada achado de processo do laudo chega aos achados do plano com a rota, uma vez só — Verificações 1 e 2
- **Fora do escopo desta tarefa:** a soma do consumo do plano por papel (`AF-T5`, que também edita `encerrar.py`).
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** achados_do_laudo em .claude/tools/encerrar.py:238, chamada no fechamento (:555) apos os --achado, sem repetir texto ja registrado; Passo 9 item (5) do scrum-master (.claude/skills/scrum-master/SKILL.md:228); testes em tests/test_encerrar.py:188, :208, :231
  - **Contrato:** encerrar.py tarefa transcreve cada linha de '## Achado de processo' do laudo como AE-<n> com Rota (ou 'nao declarada no laudo'); o condutor nao precisa repassar esses achados por --achado
  - **Não refazer:** a transcricao do achado do laudo
  - **Pendente:** nenhum

### AF-T5 — O gancho de telemetria grava todo papel do kit, e a soma do plano os separa [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** O gancho de telemetria passa a gravar o consumo de todo papel do kit, que a soma do plano conta por inteiro.
- **Fundamento:** `DAF-15`, `DAF-25`, `F-13`, `F-30`.
- **Depende de:** `AF-T4`
- **Operação do modelo:** `OP-5`
  - OP-5: O gancho de telemetria passa a gravar o consumo de todo papel do kit, que a soma do plano conta por inteiro.
  - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; fechamento de tarefa — Quem implementa faz o fechamento copiar cada achado de processo do laudo para os achados do plano, com a rota, sem repetir achado igual.
- **Camada e fronteira:** gancho `SubagentStop` em `.claude/tools/telemetria_hook.py` (cliente do CLI `.claude/tools/telemetria.py append`, por subprocesso; nunca reimplementa validação de coluna); falha aberta total; `encerrar.py` carrega irmãos por caminho; nada importa de `tests/`.
- **Arquivos-alvo:**
  - `.claude/tools/telemetria_hook.py`
  - `tests/test_telemetria_hook.py`
  - `.claude/tools/encerrar.py`
  - `tests/test_encerrar.py`
  - `GOVERNANCA.md`
  - `.claude/skills/scrum-master/SKILL.md`
- **Contratos/classes:**
  - `processar(payload, estado_path, telemetria_cli, tsv_path=None, data=None) -> bool` — assinatura inalterada. Age para todo `agent_type` iniciado por `pantonic-`; outro `agent_type` (ou vazio) é silêncio, sem escrever e sem apagar nada. Sem `agent_transcript_path` legível, silêncio. O estado `tarefa-corrente.json` **não se apaga mais**: vale até o despacho seguinte do executor, que o sobrescreve.
  - Tarefa da linha, por papel: `pantonic-executor` → `estado["tarefa"]` (sem estado: silêncio, como hoje); `pantonic-reviewer` → `<tarefa>-revisao`; `pantonic-consultant` → `<tarefa>-consultor-<n>`, `<n>` = 1 + número de linhas da série cuja coluna `tarefa` começa por `<tarefa>-consultor-`; `pantonic-planner` → `<P-n>-planejador`; `pantonic-model-designer` → `<P-n>-modelador`; `pantonic-scout` → `<P-n>-scout`; outro `pantonic-<nome>` → `<P-n>-<nome>`. `<tarefa>` = `estado["tarefa"]`; `<P-n>` = a primeira ocorrência de `P-` seguido de dígitos no texto da primeira entrada `type == "user"` do transcript (conteúdo em texto ou lista de blocos `text`). Sem o id que o papel pede: `sem-id-<sufixo>` (`sem-id-revisao`, `sem-id-consultor`, `sem-id-planejador`, `sem-id-modelador`, `sem-id-scout`, `sem-id-<nome>`).
  - Modelo da linha: executor → `estado["modelo"]` em minúsculas (como hoje); demais papéis → o campo `message.model` da última entrada `assistant` do transcript, normalizado: contém `opus` → `opus`, `sonnet` → `sonnet`, `haiku` → `haiku`, outro texto → ele mesmo em minúsculas, ausente → `nao-informado`.
  - Projeto da linha: `estado["projeto"]` quando há estado; senão o nome da pasta `estado_path.parents[2]`. A série lida para contar `<n>` é `tsv_path` quando dado; senão `estado_path.parents[2] / "docs" / "telemetria.tsv"`.
  - `encerrar._consumo_do_plano(tsv, plano_id, ids)` ganha os grupos `planejador`, `modelador` e `scout` (linha cuja `tarefa` termina em `-planejador`, `-modelador`, `-scout`), na ordem `executor`, `revisor`, `consultor`, `planejador`, `modelador`, `scout`, `outros`; a regra de pertença ao plano não muda (id de tarefa do plano, ou prefixo `<plano_id>-`).
- **Passos:**
  1. Reescrever `processar` e a docstring do módulo (parágrafo **Filtro**) pela regra de `Contratos/classes`; apagar `_AGENT_TYPE_EXECUTOR` se ficar sem uso.
  2. Em `tests/test_telemetria_hook.py`: renomear `test_tr_hook_so_executor_consome_estado` para `test_tf_hook_grava_revisor_com_papel` e trocar as asserções para a linha `EXA-T55-revisao` gravada e o estado preservado; em `test_tf_processar_payload_de_fixture_grava_linha_esperada_no_tsv`, a asserção `assert not estado_path.exists()` passa a `assert estado_path.exists()`; em `test_tf_hook_executavel_stdin_utf8_nao_falha_e_preserva_invariancia` (`DAF-37`), as asserções `assert estado_rh is False`, `assert estado_rs is False` e `assert estado_vs is False` passam a `is True` (`assert estado_vh is True` fica), e na docstring o trecho ``main` apagaria o `.claude/estado/tarefa-corrente.json` real` passa a ``main` gravaria na `docs/telemetria.tsv` real` e o trecho `o transcript não é encontrado, o estado sobrevive e o TSV não é criado` passa a `o transcript não é encontrado e o TSV não é criado`; `test_tr_processar_agent_type_fora_do_filtro_e_silencio_e_preserva_o_estado` e `test_tr_processar_sem_estado_e_silencio_sem_escrita` ficam como estão.
  3. Escrever os testes novos da seção `Testes`.
  4. Em `encerrar._consumo_do_plano`, os três grupos novos.
  5. Em `GOVERNANCA.md` §4.2, as quatro linhas depois de `antigo:` viram as seis depois de `novo:` (as quebras são as do bloco; os rótulos não entram no arquivo):

     ```text
     antigo:
       revisor sair com `--desde`. O `.claude/estado/tarefa-corrente.json` se grava só no despacho do
       executor, e o hook `SubagentStop` só grava a linha do `pantonic-executor`; a rodada de outro
       papel gravada sob o id da tarefa (caso medido, 2026-09-26: a do revisor da `TK-88a`) sai da
       série por card corretivo que a cita.
     novo:
       revisor sair com `--desde`. O `.claude/estado/tarefa-corrente.json` se grava só no despacho do
       executor e vale até o despacho seguinte; o hook `SubagentStop` grava a rodada de todo papel
       `pantonic-*`, com o papel no identificador da tarefa: `<ID>` do executor, `<ID>-revisao` do
       revisor, `<ID>-consultor-<n>` do consultor, `<P-n>-planejador`, `<P-n>-modelador` e
       `<P-n>-scout` pelo primeiro id de plano da primeira mensagem do subagente, e
       `sem-id-<papel>` quando não há id a derivar.
     ```
  6. Em `.claude/skills/scrum-master/SKILL.md`, seção *Acionamento do consultor*, a frase depois de `antigo:` vira a frase depois de `novo:` (sem quebra nova e sem refluxo; os rótulos não entram no arquivo):

     ```text
     antigo: A linha de telemetria de cada instância vem do bloco `<usage>` da notificação, como a de qualquer subagente, com a tarefa `<ID>-consultor-<n>`.
     novo: A linha de telemetria de cada instância é gravada pelo hook `SubagentStop`, com a tarefa `<ID>-consultor-<n>`.
     ```
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os testes novos (referência datada: `452 passed`, 2026-09-27); a renomeação do passo 2 não reduz o total.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - O gancho sai sempre 0 e nunca bloqueia; nenhum `print` no gancho.
- **Não fazer:** não mudar `calcular_consumo` nem `montar_args_append` além do modelo e da tarefa; não editar `.claude/settings.json` nem `.claude/projecoes.json` (o gancho já está registrado em `SubagentStop`); não reescrever linhas antigas de `docs/telemetria.tsv`.
- **Contingências:**
  - se um teste existente de `tests/test_telemetria_hook.py` ou de `tests/test_encerrar.py` cair, fora dos três que o passo 2 altera → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_hook_grava_revisor_com_papel` (passo 2) — payload `pantonic-reviewer` com estado de `EXA-T55` e transcript cujo `message.model` é `claude-opus-4`: a série ganha a linha com tarefa `EXA-T55-revisao` e modelo `opus`, e o estado continua no disco (a regra de hoje não grava). TF `test_tf_hook_grava_consultor_numerado_por_papel` — série que já tem `EXA-T55-consultor-1`: o consultor grava `EXA-T55-consultor-2`. TF `test_tf_hook_grava_planejador_pelo_id_do_plano_papel` — transcript cuja primeira mensagem de usuário cita `docs/plans/P-0753-auditoria-estagio-1/plano.md`: tarefa `P-0753-planejador`. TR `test_tr_hook_sem_id_derivavel_grava_sem_id_papel` — `pantonic-scout` sem `P-<n>` na primeira mensagem: tarefa `sem-id-scout`. TF `test_tf_consumo_por_papel_separa_planejador_modelador_scout` (em `tests/test_encerrar.py`) — série com `P-0001-planejador` e `P-0001-scout`: a tabela de consumo da entrega traz as linhas `| planejador | 1 |` e `| scout | 1 |` (a regra de hoje as somaria em `outros`).
- **Verificação:**
  1. `python -m pytest tests/test_telemetria_hook.py -q -k "papel"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado)
  2. `python -m pytest tests/test_encerrar.py -q -k "consumo_por_papel"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado)
  3. `python -c "from pathlib import Path;c=chr(96);t=Path('GOVERNANCA.md').read_text(encoding='utf-8');print(t.count('só grava a linha do '+c+'pantonic-executor'+c),t.count('grava a rodada de todo papel'))"` → `0 1` — antes `1 0`, depois `0 1` (esperado, não ensaiado)
  4. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print(t.count('da notificação, como a de qualquer subagente'))"` → `0` — antes `1`, depois `0` (esperado, não ensaiado)
  5. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
  6. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
- **Pronto quando:**
  - série de telemetria.papéis gravados — toda rodada de agente do kit grava sozinha, com o papel no identificador — Verificações 1, 3 e 4
  - série de telemetria.consumo do plano — o total soma todas as rodadas do plano, de todos os papéis — Verificação 2
- **Fora do escopo desta tarefa:** a primeira linha do revisor (`AF-T6`); o arquivo `tarefa-corrente.json` gravado por comando (`AF-T10`); a revisão do `README.md` (`AF-T18`).
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** processar em .claude/tools/telemetria_hook.py:294 grava a rodada de todo pantonic-* com o papel no id (<ID>, <ID>-revisao, <ID>-consultor-<n>, <P-n>-planejador/-modelador/-scout, sem-id-<papel>) e nao apaga mais tarefa-corrente.json; _consumo_do_plano (.claude/tools/encerrar.py:676) separa planejador, modelador e scout; GOVERNANCA.md §4.2 e scrum-master (Acionamento do consultor) atualizados
  - **Contrato:** a serie docs/telemetria.tsv recebe a linha de revisor, consultor e demais papeis pelo hook SubagentStop, sem --tool-uses do condutor; tarefa-corrente.json vale ate o proximo despacho do executor
  - **Não refazer:** a gravacao por papel no hook; os grupos novos da soma do plano
  - **Pendente:** nenhum

### AF-T6 — A recomendação do laudo viaja na primeira linha do revisor [Sonnet · esforço low · classe implementacao]
- **Objetivo:** O revisor passa a devolver a recomendação do laudo na primeira linha, na forma que o painel, o fechamento e as instruções do gerente leem no mesmo ato.
- **Fundamento:** `DAF-19`, `DAF-26`, `DAF-38`, `F-18`, `F-28`.
- **Depende de:** `AF-T3`, `AF-T5`
- **Operação do modelo:** `OP-6`
  - OP-6: O revisor passa a devolver a recomendação do laudo na primeira linha, na forma que o painel, o fechamento e as instruções do gerente leem no mesmo ato.
  - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; painel do gerente — Quem implementa faz o painel reconhecer o programa chamado mesmo quando a chamada traz opções do interpretador antes dele.; fechamento de tarefa — Quem implementa faz o fechamento copiar cada achado de processo do laudo para os achados do plano, com a rota, sem repetir achado igual.
- **Camada e fronteira:** texto do agente revisor, instruções do gerente (skill `scrum-master`) e gancho do painel (`.claude/tools/progresso_hook.py`, falha aberta). O fechamento (`encerrar.py`) já lê a recomendação do laudo (`**Recomendação:**`) e não muda (`F-28`): os literais `bloqueante=` em `encerrar.py` e `rdo.py` são argumentos nomeados de função, não a linha do revisor.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-reviewer.md`
  - `.claude/skills/scrum-master/SKILL.md`
  - `.claude/tools/progresso_hook.py`
  - `tests/test_progresso_hook.py`
- **Contratos/classes:** linha nova do revisor: `<tarefa> <veredito> <percentual> bloqueante=<dimensão|nenhuma> recomendacao=<seguir|seguir com ressalva|refazer|escalar>`. Regex da volta do revisor no painel: `^(\S+) (\S+) (\d+)%? bloqueante=(\S+)(?: recomendacao=(.+))?$`. Frase `M-7`: `Agente revisor devolveu a tarefa "<título>": <veredito> <percentual>%, bloqueante <bloqueante>, recomendação <recomendação>.`, com `<recomendação>` ← grupo 5, e `não informada` quando a linha vem sem o campo. `test_tf_ger_18_residencia` confere `FRASES` contra a tabela de frases da skill: as duas mudam juntas.
- **Passos:**
  1. Em `.claude/agents/pantonic-reviewer.md`, passo 7 (*Retorno ao chamador*), a primeira linha do bloco das duas linhas fixas vira a linha nova de `Contratos/classes` (mesmo recuo de três espaços).
  2. Em `.claude/skills/scrum-master/SKILL.md`, Passo 7: a linha de entrada `` `<tarefa> <veredito> <percentual> bloqueante=<dimensão|nenhuma>` `` vira a linha nova de `Contratos/classes`, entre crases; e as três linhas depois de `antigo:` viram as quatro depois de `novo:` (as quebras são as do bloco; os rótulos não entram no arquivo):

     ```text
     antigo:
     - **Ação:** ler `veredito` ∈ {`aprovado`, `ressalva`, `reprovado`}, `bloqueante` e o caminho do
       laudo — calculados pelo gerador, não recalculados pelo loop. Colher a `recomendação` **do
       laudo**, campo fechado (`seguir`, `seguir com ressalva`, `refazer`, `escalar`), lido por `A6`,
     novo:
     - **Ação:** ler `veredito` ∈ {`aprovado`, `ressalva`, `reprovado`}, `bloqueante`, `recomendacao` e o
       caminho do laudo — calculados pelo gerador e transcritos pelo revisor, não recalculados pelo
       loop. A `recomendação` vem **da primeira linha**, campo fechado (`seguir`, `seguir com
       ressalva`, `refazer`, `escalar`), lido por `A6`,
     ```
  3. Na tabela de frases da skill, linha `M-7`: o regex vira o de `Contratos/classes`, a frase vira a de `Contratos/classes` e a última célula passa a `` `<veredito>` ← grupo 2; `<percentual>` ← grupo 3; `<bloqueante>` ← grupo 4; `<recomendação>` ← grupo 5, ou `não informada` sem o campo ``.
  4. Em `progresso_hook.py`: `FRASES['M-7']` vira a frase nova; o `re.match` da volta do `pantonic-reviewer` vira o regex novo, e o dicionário da frase ganha `"<recomendação>"`.
  5. Escrever os dois testes da seção `Testes`.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 2 testes novos (referência datada: `452 passed`, 2026-09-27).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0 (o texto do agente muda no corpo, não no frontmatter).
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não tocar `encerrar.py` nem `rdo.py`; não mudar o frontmatter do agente; não mudar outra frase do painel; não renomear o campo para `recomendação` com acento na linha (a linha é de máquina, ASCII).
- **Contingências:**
  - se `test_tf_ger_7_agente_de_volta_revisor` cair só porque a frase ganhou `, recomendação não informada` → atualizar as duas asserções dele para a frase nova com `não informada` e seguir.
  - se `test_tf_ger_19_userpromptsubmit_sem_volta_pendente` e `test_tf_ger_25_show_no_meio_da_janela_nao_encerra` caírem pelo mesmo motivo (`DAF-38`) → em `tests/test_progresso_hook.py`, o literal `aprovado 100%, bloqueante nenhuma.'` (2 ocorrências no arquivo, uma em cada teste) passa a `aprovado 100%, bloqueante nenhuma, recomendação não informada.'` e seguir.
  - se outro teste existente cair, fora desses três → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_m7_revisor_com_recomendacao` — volta `TLG-T9 ressalva 91 bloqueante=nenhuma recomendacao=seguir com ressalva` gera `Agente revisor devolveu a tarefa "Um título de teste": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.` (com o regex antigo o grupo 4 engoliria `nenhuma recomendacao=seguir com ressalva`). TR `test_tr_m7_revisor_sem_recomendacao_diz_nao_informada` — volta `TLG-T9 aprovado 100 bloqueante=nenhuma` gera a frase com `recomendação não informada`.
- **Verificação:**
  1. `python -m pytest tests/test_progresso_hook.py -q -k "recomendacao"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado)
  2. `python -c "from pathlib import Path;print(sum(Path(p).read_text(encoding='utf-8').count('recomendacao=<') for p in ['.claude/agents/pantonic-reviewer.md','.claude/skills/scrum-master/SKILL.md']))"` → `2` — antes `0`, depois `2` (esperado, não ensaiado)
  3. `python -c "from pathlib import Path;t=sum(Path(p).read_text(encoding='utf-8').count('recomendação <recomendação>') for p in ['.claude/tools/progresso_hook.py','.claude/skills/scrum-master/SKILL.md']);print(t)"` → `2` — antes `0`, depois `2` (esperado, não ensaiado)
  4. `python -m pytest tests/test_encerrar.py -q -k "tarefa_fecha_num_ato"` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava: o fechamento já transcreve `**Recomendação:**` do laudo)
  5. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
  6. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
- **Pronto quando:**
  - linha de retorno do revisor.recomendação do laudo — presente na primeira linha e lida, na mesma forma, pelo painel, pelo fechamento e pelas instruções do gerente — Verificações 1 a 4
- **Fora do escopo desta tarefa:** o verbo que despacha a tarefa (`AF-T10`).
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** linha do revisor com recomendacao= (.claude/agents/pantonic-reviewer.md passo 7); scrum-master Passo 7 le a recomendacao da primeira linha e a linha M-7 da tabela; progresso_hook.py:224 casa o campo e a frase M-7 o mostra ('nao informada' sem ele); testes em tests/test_progresso_hook.py:310 e :326
  - **Contrato:** o revisor devolve '<tarefa> <veredito> <percentual> bloqueante=<...> recomendacao=<...>'; o loop le a recomendacao dali, sem abrir o laudo
  - **Não refazer:** o campo recomendacao na primeira linha do revisor e no painel
  - **Pendente:** nenhum

### AF-T7 — A conferência do card lê a situação da tarefa no estado do plano em pasta [Sonnet · esforço low · classe implementacao]
- **Objetivo:** A conferência do card passa a ler a situação da tarefa sempre no estado do plano em pasta, sem consultar a que o card declara.
- **Fundamento:** `DAF-18`, `DAF-39`, `F-17`, `F-29`.
- **Operação do modelo:** `OP-7`
  - OP-7: A conferência do card passa a ler a situação da tarefa sempre no estado do plano em pasta, sem consultar a que o card declara.
  - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.
- **Camada e fronteira:** instrumento do kit `.claude/tools/card_check.py`; reusa `rdo._status_atual` (carregado por caminho) e `caminhos.pasta_do_plano`; não importa de `tests/`.
- **Arquivos-alvo:**
  - `.claude/tools/card_check.py`
  - `tests/test_card_check.py`
  - `tests/fixtures/card_check/P-0-pasta/plano.md`
  - `tests/fixtures/card_check/P-0-pasta/estado.tsv`
- **Contratos/classes:** em `verificar_tarefa`, a chamada `rdo._status_atual(plano_path, dossie.tarefa_id, dossie, None)` passa a `rdo._status_atual(plano_path, dossie.tarefa_id, dossie, _caminhos.pasta_do_plano(plano_path))`. `_status_atual` já lê a linha da tarefa em `estado.tsv` quando recebe a pasta (`F-29`). Status ausente continua imprimindo `status ausente: comparando antes`.
- **Passos:**
  1. Trocar o quarto argumento da chamada de `_status_atual`, como em `Contratos/classes`.
  2. Criar a fixture `tests/fixtures/card_check/P-0-pasta/plano.md` com o conteúdo abaixo (as quebras são as do bloco; o recuo de dois espaços não entra no arquivo). O bullet `Entregável` de cada card é exigido por `rdo.extrair_dossie`: todo card tem exatamente um entre `Arquivos-alvo` e `Entregável` (`DAF-39`):

     ```text
       # P-0 — Fixture de card_check em plano em pasta

       **Prefixo das tarefas no diário:** `CP-T<n>`

       ### CP-T1 — Card concluído de plano em pasta [Sonnet · classe mecanica]
       - **Objetivo:** fixture de `card_check`: o status `done` mora só em `estado.tsv`.
       - **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
       - **Verificação:**
         1. `python -c "print('b')"` → `b` — antes `a`, depois `b`
       - **Pronto quando:** `card_check.py --tarefa CP-T1` sai 0, comparando `depois`.

       ### CP-T2 — Card pronto de plano em pasta [Sonnet · classe mecanica]
       - **Objetivo:** fixture de `card_check`: o status `ready` mora só em `estado.tsv`.
       - **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
       - **Verificação:**
         1. `python -c "print('a')"` → `b` — antes `a`, depois `b`
       - **Pronto quando:** `card_check.py --tarefa CP-T2` sai 0, comparando `antes`.
     ```
  3. Criar `tests/fixtures/card_check/P-0-pasta/estado.tsv` com as quatro linhas abaixo, campos separados por TAB (cada `<TAB>` é um caractere de tabulação):

     ```text
     id<TAB>tipo<TAB>status<TAB>razao<TAB>data<TAB>nota
     P-0<TAB>plano<TAB>in-progress<TAB>-<TAB>2026-09-27<TAB>-
     CP-T1<TAB>tarefa<TAB>done<TAB>-<TAB>2026-09-27<TAB>-
     CP-T2<TAB>tarefa<TAB>ready<TAB>-<TAB>2026-09-27<TAB>-
     ```
  4. Escrever os dois testes da seção `Testes`.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 2 testes novos (referência datada: `468 passed`, 2026-09-27, `DAF-39`).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não mudar `rdo._status_atual`; não mudar a regra de mundo por status (`done` → `depois`; demais → `antes`); não mudar `--mundo`.
- **Contingências:**
  - se um teste existente de `tests/test_card_check.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_estado_tsv_done_compara_depois` — `CP-T1` sai 0 (a regra de hoje compara `antes`, `a` contra a saída `b`, e sai 1). TR `test_tr_estado_tsv_ready_compara_antes` — `CP-T2` sai 0 comparando `antes`.
- **Verificação:**
  1. `python .claude/tools/card_check.py --plano tests/fixtures/card_check/P-0-pasta/plano.md --tarefa CP-T1` → `exit 0` — antes `exit 1`, depois `exit 0` (medido pelo consultor, `DAF-39`)
  2. `python -m pytest tests/test_card_check.py -q -k "estado_tsv"` → `exit 0` — antes `exit 5`, depois `exit 0` (medido pelo consultor, `DAF-39`)
  3. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (medido pelo consultor, `DAF-39`; trava)
  4. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (medido pelo consultor, `DAF-39`; trava)
- **Pronto quando:**
  - conferência do card.situação do card em plano em pasta — lida do estado do plano; card concluído é comparado contra o mundo de depois — Verificações 1 e 2
- **Fora do escopo desta tarefa:** o verbo `despachar`, que chama esta conferência (`AF-T10`).
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** verificar_tarefa (.claude/tools/card_check.py:363) passa _caminhos.pasta_do_plano(plano_path) a rdo._status_atual; fixture tests/fixtures/card_check/P-0-pasta/ (plano.md + estado.tsv); testes test_tf_estado_tsv_done_compara_depois e test_tr_estado_tsv_ready_compara_antes em tests/test_card_check.py
  - **Contrato:** em plano em pasta, card_check le a situacao da tarefa em estado.tsv (done compara 'depois'); versao 2 do modelo, vigente desde o aceite do dono em 2026-09-27 (quinto ato da §0), diz que a fonte e incondicional em plano em pasta
  - **Não refazer:** a leitura de estado.tsv pelo card_check
  - **Pendente:** copias do texto de OP-7 no card AF-T7 (plano.md:726 e :729) defasadas em relacao a versao 2 pendente do modelo; atualizam-se se o dono aceitar a versao 2 no marco — sanado: versao 2 aceita pelo dono em 2026-09-27 e as copias do card (Objetivo e Operacao do modelo) sincronizadas

### AF-T8 — A conferência do backlog aceita o plano em esboço, e o planejador o registra no esboço [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** A conferência do backlog passa a aceitar o plano que o planejador registra já no esboço, antes de ele entrar na fila.
- **Fundamento:** `DAF-1`, `DAF-10`, `F-8`, `F-22`.
- **Operação do modelo:** `OP-8`
  - OP-8: A conferência do backlog passa a aceitar o plano que o planejador registra já no esboço, antes de ele entrar na fila.
  - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.
- **Camada e fronteira:** instrumento do kit `.claude/tools/backlog.py` (lint `check`) e o texto de dois papéis do kit: o agente planejador e a skill `diario-de-obras`; não importa de `tests/`.
- **Domínio:** *plano em esboço* — plano em pasta (`docs/plans/P-<n>-<slug>/plano.md`) cujo `estado.tsv` existe e tem, depois do cabeçalho, uma linha só: a do plano, com status `blocked`; e nenhuma linha de `docs/plans/_INBOX.md` cita o caminho dele. É o estado entre a Fase 3a e a Fase 5 do planejador.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
  - `tests/fixtures/backlog/esqueleto/docs/plans/P-0-esboco/plano.md`
  - `tests/fixtures/backlog/esqueleto/docs/plans/P-0-esboco/estado.tsv`
  - `tests/fixtures/backlog/esqueleto/docs/plans/_INBOX.md`
  - `tests/fixtures/backlog/esqueleto/docs/DIARIO_DE_OBRAS.md`
  - `.claude/agents/pantonic-planner.md`
  - `.claude/skills/diario-de-obras/SKILL.md`
- **Contratos/classes:** no bloco `C-10` de `check`, o conjunto de ids comparado com o contador deixa de fora o plano em esboço cujo id é igual ao do contador; o resto do `C-10` não muda (contador menor que o id de um plano que não está em esboço segue acusado). `C-8` e `C-13` não mudam (medido na `F-22`: não disparam nesse estado).
- **Passos:**
  1. Em `backlog.py`, no bloco `C-10`, excluir de `ids_planos` o plano em esboço (predicado de `Domínio`) cujo id é o do contador.
  2. Criar a fixture `tests/fixtures/backlog/esqueleto/`: `docs/plans/P-0-esboco/plano.md` com as três linhas `# P-0 — Plano em esboço`, linha vazia, `**Prefixo das tarefas no diário:** `` `ESB-T<n>` ``; `docs/plans/P-0-esboco/estado.tsv` com o cabeçalho `id<TAB>tipo<TAB>status<TAB>razao<TAB>data<TAB>nota` e a linha `P-0<TAB>plano<TAB>blocked<TAB>dependencia<TAB>2026-09-27<TAB>aguarda o modelo` (cada `<TAB>` é uma tabulação); `docs/plans/_INBOX.md` com a linha `**Próximo id de plano: P-0.**`; `docs/DIARIO_DE_OBRAS.md` igual a `tests/fixtures/backlog/pasta/docs/DIARIO_DE_OBRAS.md` sem a linha de índice `| P-0-GAM | Plano gama | ready | docs/plans/P-0-gama/plano.md |`.
  3. Escrever os dois testes da seção `Testes`.
  4. Em `.claude/agents/pantonic-planner.md`, Fase 3a, a linha depois de `antigo:` vira as três depois de `novo:` (as quebras são as do bloco; os rótulos não entram no arquivo):

     ```text
     antigo:
     Grave `docs/plans/P-<n>-<slug>/plano.md` **sem a §1 e sem a §5**, com o esqueleto fixo, nesta ordem:
     novo:
     Grave `docs/plans/P-<n>-<slug>/plano.md` **sem a §1 e sem a §5**, com o esqueleto fixo abaixo, e,
     no mesmo ato, `estado.tsv` na mesma pasta com o cabeçalho e só a linha do plano, `blocked`, razão
     `dependencia` — a linha do `_INBOX.md` e o contador ficam para a Fase 5. O esqueleto, nesta ordem:
     ```
  5. No mesmo arquivo, Fase 5, o trecho depois de `antigo:` vira o trecho depois de `novo:` (sem quebra nova e sem refluxo; os rótulos não entram no arquivo):

     ```text
     antigo: grave `estado.tsv` na pasta do plano (linha do plano e uma linha por card, esquema da skill `diario-de-obras`)
     novo: complete o `estado.tsv` da pasta do plano com uma linha por card (esquema da skill `diario-de-obras`; a linha do plano já está lá desde a Fase 3a)
     ```
  6. Em `.claude/skills/diario-de-obras/SKILL.md`, seção *Estado do plano em pasta*, as duas linhas depois de `antigo:` viram as quatro depois de `novo:` (as quebras são as do bloco; os rótulos não entram no arquivo):

     ```text
     antigo:
     `data` `AAAA-MM-DD`; `nota` uma linha sem TAB, ou `-`. O planejador grava o arquivo ao registrar
     o plano; depois só `backlog.py status` o reescreve. `check` acusa `C-13` (card sem linha, linha
     novo:
     `data` `AAAA-MM-DD`; `nota` uma linha sem TAB, ou `-`. O planejador grava o arquivo na Fase 3a,
     junto do esqueleto, só com a linha do plano (`blocked`, razão `dependencia`), e acrescenta uma
     linha por card ao registrar o plano; depois só `backlog.py status` o reescreve. `check` acusa
     `C-13` (card sem linha, linha
     ```
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 2 testes novos (referência datada: `452 passed`, 2026-09-27).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0 (o texto do agente muda no corpo, não no frontmatter).
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - `python .claude/tools/backlog.py check` sobre o repositório real segue saindo 0.
- **Não fazer:** não mudar `C-8`, `C-13` nem outro código de violação; não mudar o formato do contador; não tocar outra fase do arquivo do planejador; não mudar o frontmatter do agente.
- **Contingências:**
  - se, antes da mudança do passo 1, `python .claude/tools/backlog.py check --repo tests/fixtures/backlog/esqueleto` acusar violação além do `C-10` → parar e sinalizar `blocked` razão `premissa`, colando a saída.
  - se um teste existente de `tests/test_backlog.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_check_aceita_plano_em_esqueleto` — `check` sobre cópia da fixture `esqueleto` sai 0 (a regra de hoje sai 1 com `C-10`). TR `test_tr_check_esqueleto_com_linha_de_tarefa_segue_acusando_c10` — a mesma cópia com uma linha de tarefa acrescentada ao `estado.tsv` (o plano deixou de ser esboço) sai 1 com `C-10`.
- **Verificação:**
  1. `python .claude/tools/backlog.py check --repo tests/fixtures/backlog/esqueleto` → `exit 0` — antes `exit 1`, depois `exit 0` (esperado, não ensaiado)
  2. `python -m pytest tests/test_backlog.py -q -k "esqueleto"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado)
  3. `python -c "from pathlib import Path;c=chr(96);t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print(t.count('no mesmo ato, '+c+'estado.tsv'+c),t.count('a linha do plano já está lá desde a Fase 3a'))"` → `1 1` — antes `0 0`, depois `1 1` (esperado, não ensaiado)
  4. `python -c "from pathlib import Path;t=Path('.claude/skills/diario-de-obras/SKILL.md').read_text(encoding='utf-8');print(t.count('O planejador grava o arquivo ao registrar'),t.count('O planejador grava o arquivo na Fase 3a'))"` → `0 1` — antes `1 0`, depois `0 1` (esperado, não ensaiado)
  5. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
  6. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
- **Pronto quando:**
  - conferência do backlog.aceite do plano em esboço — aceita o plano esboçado que tem o estado registrado e ainda não está na fila — Verificações 1 e 2
  - planejador.registro do plano em esboço — o roteiro manda gravar o estado do plano junto do esboço — Verificações 3 e 4
- **Fora do escopo desta tarefa:** o card inteiro no `next` e no `show` (`AF-T9`); o pré-voo do pedido na Fase 0 (`AF-T17`).
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** _plano_em_esboco em .claude/tools/backlog.py:597 e o C-10 (:838-849) deixam de fora o plano em esboço cujo id é o do contador; fixture tests/fixtures/backlog/esqueleto/; planner Fases 3a e 5 e skill diario-de-obras (Estado do plano em pasta) mandam gravar estado.tsv com a linha do plano na Fase 3a
  - **Contrato:** backlog.py check aceita o plano em pasta em esboço (estado.tsv só com a linha do plano, blocked, fora do inbox); o predicado ainda não exige plano em pasta (ressalva do laudo, com o consultor)
  - **Não refazer:** nada a declarar
  - **Pendente:** predicado _plano_em_esboco omite a cláusula 'plano em pasta': plano legado blocked com id = contador fora do inbox é silenciado no C-10 (ressalva do laudo) — sanado pelo consultor no `DAF-40`

### AF-T9 — O `next` e o `show` entregam o card inteiro [Sonnet · esforço low · classe implementacao]
- **Objetivo:** O backlog passa a entregar a quem conduz o card inteiro no despacho, sem corte no meio.
- **Fundamento:** `DAF-11`, `DAF-33`, `F-9`.
- **Depende de:** `AF-T8`
- **Operação do modelo:** `OP-9`
  - OP-9: O backlog passa a entregar a quem conduz o card inteiro no despacho, sem corte no meio.
  - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; conferência do backlog — Quem implementa faz a conferência aceitar o plano recém-esboçado que já tem o estado registrado e ainda não entrou na fila.
- **Camada e fronteira:** instrumento do kit `.claude/tools/backlog.py` (verbos `next` e `show`, somente leitura) e a skill `passagem-de-bastao`; não importa de `tests/`.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
  - `.claude/skills/passagem-de-bastao/SKILL.md`
- **Contratos/classes:** `_truncar(texto, arquivo, linha_header, linha_fim) -> str` não muda. Regra nova: no `next` (`renderizar_next`) e no `show` de tarefa ou de card de tíquete (`Item`), o texto do card sai inteiro até a linha anterior a `- **Notas de execução:**`; o trecho que começa nessa linha (quando existe) e o bloco `_bloco_achados` passam por `_truncar`. O `show` de um plano (`Plano`) continua inteiro por `_truncar`, como hoje. O rótulo `--- dossiê (verbatim, teto DB-7) ---` do `next` vira `--- dossiê (verbatim, card inteiro) ---`.
- **Passos:**
  1. Escrever a função `_card_inteiro(item: Item) -> str` com a regra de `Contratos/classes` e usá-la no `next` e no `show` de `Item`.
  2. Trocar o rótulo do dossiê no `next`; na docstring do módulo, a linha depois de `antigo:` vira a linha depois de `novo:` (sem quebra nova e sem refluxo das linhas vizinhas; os rótulos não entram no arquivo):

     ```text
     antigo: truncado ao teto `DB-7` (8.000 chars / 120 linhas, com ponteiro `arquivo:l1-l2` quando corta).
     novo: inteiro no card de tarefa; o teto `DB-7` (8.000 chars / 120 linhas, com ponteiro `arquivo:l1-l2` quando corta) vale para plano, notas de execução e achados.
     ```
  3. Escrever os dois testes da seção `Testes`.
  4. Em `.claude/skills/passagem-de-bastao/SKILL.md`, Parte 2, inserir antes da linha que começa por `**Fonte do contexto, em ordem de preferência:**` o parágrafo abaixo, seguido de uma linha vazia (as quebras são as do bloco; o recuo de dois espaços não entra no arquivo):

     ```text
       **O card chega inteiro.** `backlog.py next` e `backlog.py show <ID>` imprimem o card inteiro, sem
       corte; o teto `DB-7` (8.000 caracteres ou 120 linhas, com o ponteiro `arquivo:l1-l2` de onde
       cortou) vale só para o bloco de achados roteados ao card e para as notas de execução do plano
       legado. O dossiê se copia da saída do instrumento, sem reler o plano.
     ```
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 2 testes novos (referência datada: `452 passed`, 2026-09-27).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - `next` e `show` seguem somente leitura: nenhuma escrita em arquivo.
- **Não fazer:** não mudar `_TETO_CHARS` nem `_TETO_LINHAS`; não mudar a seleção do `next`; não mudar o `show` de plano (`test_tf_show_trunca_em_8000_chars_120_linhas_com_ponteiro` segue verde).
- **Contingências:**
  - se `test_tr_saida_do_next_cabe_no_teto` cair porque o card da fixture `next_tk90` passou do teto → parar e sinalizar `blocked` razão `premissa`, colando o tamanho medido da saída.
  - se outro teste existente de `tests/test_backlog.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_card_inteiro_no_next_e_no_show` — plano temporário com um card de 150 linhas: a saída do `next` e a do `show <ID>` contêm a linha 150 do card e não contêm `… truncado (` (a regra de hoje corta na linha 120). TR `test_tr_card_inteiro_notas_de_execucao_seguem_com_teto` — card de plano legado com 200 linhas de notas de execução: a saída do `show` contém `… truncado (`.
- **Verificação:**
  1. `python -m pytest tests/test_backlog.py -q -k "card_inteiro"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado)
  2. `python -c "from pathlib import Path;print(Path('.claude/skills/passagem-de-bastao/SKILL.md').read_text(encoding='utf-8').count('O card chega inteiro.'))"` → `1` — antes `0`, depois `1` (esperado, não ensaiado)
  3. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
  4. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
- **Pronto quando:**
  - despacho de tarefa.card entregue inteiro — o card chega inteiro; só os achados e as notas de execução têm teto — Verificações 1 e 2
- **Fora do escopo desta tarefa:** o verbo `despachar`, que imprime o card pelo mesmo caminho (`AF-T10`).
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** _card_inteiro em .claude/tools/backlog.py:1121, usada por renderizar_next e pelo show de Item: card inteiro ate '- **Notas de execucao:**', notas e achados com teto; rotulo '--- dossiê (verbatim, card inteiro) ---'; paragrafo 'O card chega inteiro.' na skill passagem-de-bastao; testes tests/test_backlog.py:1142 e :1196
  - **Contrato:** o next e o show de tarefa entregam o card inteiro; show de plano segue truncado
  - **Não refazer:** o card inteiro no next/show
  - **Pendente:** nenhum

### AF-T10 — Um verbo `despachar` roda as conferências do despacho e recusa pela primeira que falhar [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** Quem conduz passa a despachar a tarefa por um comando único, que roda as conferências do despacho e recusa pela primeira que falhar.
- **Fundamento:** `DAF-20`, `DAF-30`, `F-19`.
- **Depende de:** `AF-T6`, `AF-T7`, `AF-T9`
- **Operação do modelo:** `OP-10`
  - OP-10: Quem conduz passa a despachar a tarefa por um comando único, que roda as conferências do despacho e recusa pela primeira que falhar.
  - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; despacho de tarefa — Quem implementa faz o despacho entregar o card sem corte e rodar num comando só as conferências que hoje se repetem à mão, recusando pela primeira que falhar.; conferência do card — Quem implementa faz a conferência ler a situação da tarefa no estado do plano quando o card não a traz.; tarefa do loop — Ninguém altera: é nela que se vê, antes e depois, quanto de cada ciclo ainda depende da mão e da memória de quem conduz.
- **Camada e fronteira:** instrumento do kit `.claude/tools/backlog.py`; roda `modelo.py`, `card_check.py` e `review_evidence.py` como subprocessos (`sys.executable` + caminho do irmão em `Path(__file__).parent`), nunca por `import`; não importa de `tests/`.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
  - `.claude/skills/scrum-master/SKILL.md`
- **Contratos/classes:** subcomando `despachar <ID> [--repo <caminho>]` (raiz padrão: a do próprio `backlog.py`, como os demais verbos). Ordem, parando na primeira recusa, com a linha `despachar: recusado — <gate>: <razão>` no stderr, exit `1` e **nada escrito**:
  - `tarefa` — `<ID>` é tarefa de plano (`Item` com `tipo == "tarefa"`) com status `ready`; senão a razão é `<ID> não é tarefa de plano` ou `<ID> está <status>, não ready`.
  - `modelo` — `python .claude/tools/modelo.py check --plano <plano> --root <repo>` sai `0` ou `2`; senão a razão é a última linha do stderr.
  - `card_check` — `python .claude/tools/card_check.py --plano <plano> --tarefa <ID> --root <repo>` sai `0`; senão a razão é a última linha do stderr.
  - `pytest --co` — `python -m pytest --co -q`, com `cwd = <repo>`, sai `0` ou `5`; senão a razão é `exit <n>`.
  - `ref` — se `<repo>/.claude/estado/tarefa-corrente.json` existe, é da mesma `tarefa` e tem `ref` não vazio, reaproveita esse `ref` (redespacho); senão `python .claude/tools/review_evidence.py --capturar-ref --root <repo>` sai `0` e o `ref` é a última linha não vazia do stdout; senão a razão é a última linha do stderr.
  - `status` — `transacionar_status(repo, modelo, <ID>, "in-progress", nota="despachada por backlog.py despachar")` com `exit_code == 0`; senão a razão é a `mensagem`.
  Depois do `status`: grava `<repo>/.claude/estado/tarefa-corrente.json` (criando o diretório) com `tarefa`, `projeto` (nome da pasta de `<repo>`), `modelo` (o do cabeçalho do card), `plano` (caminho do plano relativo a `<repo>`, com `/`), `despachado_em` (ISO 8601, UTC) e `ref`; e imprime, nesta ordem: `=== DESPACHO: <ID> — <título>`, os blocos `=== HANDOVER DE ...` que `handovers_para` devolve, o card como o `show <ID>` o imprime e a linha `ref=<sha>`. Exit `0`.
- **Passos:**
  1. Escrever a função `despachar(repo: Path, id_: str) -> ResultadoStatus` com a ordem de `Contratos/classes` e o subcomando no `main`.
  2. Escrever os três testes da seção `Testes`, sobre cópia temporária (`tmp_path`) de `tests/fixtures/backlog/pasta/` montada nesta ordem (`DAF-41`): (a) copiar a fixture; (b) copiar do repositório `.claude/tools/rdo.py` e `.claude/tools/caminhos.py` para `.claude/tools/` da cópia — o `card_check` carrega `rdo.py` de `<root>/.claude/tools/` e `rdo.py` carrega `caminhos.py` ao lado; sem eles o gate `card_check` recusa com `rdo.py: módulo não encontrado`; (c) sobrescrever `docs/plans/P-0-gama/plano.md` da cópia com o conteúdo abaixo (as quebras são as do bloco; o recuo de dois espaços não entra no arquivo) — `rdo.extrair_dossie` exige em todo card `Objetivo`, `Verificação`, `Pronto quando` e exatamente um entre `Arquivos-alvo` e `Entregável`; `GAM-T1` o `card_check` aceita e `GAM-T2` recusa (`antes` `z` contra a saída `a`); (d) `git init` e um commit inicial com tudo. A fixture do repositório não muda. Ensaiado pelo consultor na cópia assim montada: `modelo.py check` exit 2 (`ausente`), `card_check` `GAM-T1` exit 0 e `GAM-T2` exit 1, `pytest --co -q` exit 5, `review_evidence.py --capturar-ref` exit 0.

     ```text
       # P-0 — Plano gama

       **Prefixo das tarefas no diário:** `GAM-T<n>`

       ### GAM-T1 — Primeira tarefa [Sonnet · classe implementacao]
       - **Objetivo:** fixture.
       - **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
       - **Verificação:**
         1. `python -c "print('a')"` → `b` — antes `a`, depois `b`
       - **Pronto quando:** fixture existe.

       ### GAM-T2 — Segunda tarefa [Sonnet · classe implementacao]
       - **Objetivo:** fixture.
       - **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
       - **Verificação:**
         1. `python -c "print('a')"` → `b` — antes `z`, depois `b`
       - **Pronto quando:** fixture existe.
     ```
  3. Em `.claude/skills/scrum-master/SKILL.md`, Passo 3, inserir depois do parágrafo que começa por `Aprovados os quatro,` (e antes de `- **Saída:**`) o parágrafo abaixo, precedido de uma linha vazia (as quebras são as do bloco; o recuo de dois espaços entra no arquivo, como o dos parágrafos vizinhos do passo):

     ```text
       **Por comando** (`R-15`): `python .claude/tools/backlog.py despachar <ID>` roda, nesta ordem, o
       terceiro gate, o quarto e a coleta da suíte (`python -m pytest --co -q`), materializa
       `in-progress`, grava `.claude/estado/tarefa-corrente.json` com o `<ref>` e imprime o card
       inteiro, o bloco `HANDOVER` e a linha `ref=<sha>`. Recusa pelo primeiro gate que falhar, sem
       escrever nada: exit `1` **não delega**, e a linha de recusa vai à razão de `B3`. `G-PLANREADY` e o
       Gate de delegação continuam com quem conduz, antes do verbo; card de tíquete segue pelos passos
       à mão.
     ```
  4. No Passo 4, inserir antes do parágrafo que começa por `Invocar ` + `` `pantonic-executor` `` o parágrafo abaixo, seguido de uma linha vazia (as quebras são as do bloco; o recuo de dois espaços entra no arquivo, como o dos parágrafos vizinhos do passo):

     ```text
       Despachada pelo verbo `despachar` do passo 3, a tarefa já tem o arquivo gravado e o `<ref>` na
       linha `ref=<sha>` da saída: este passo só invoca o executor.
     ```
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 3 testes novos (referência datada: `475 passed`, medido pelo consultor em 2026-09-27, `DAF-41`; piso `478`).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Os testes rodam o verbo só sobre cópia temporária (`tmp_path`), nunca sobre o repositório real; o `pytest --co` do teste roda com `cwd` na cópia.
- **Não fazer:** não mudar `next`, `status` nem `start`; não mudar `card_check.py`, `modelo.py` nem `review_evidence.py`; não rodar o verbo sobre o repositório real para testar.
- **Contingências:**
  - se o `pytest --co` dentro do teste, com `cwd` na cópia temporária, sair com código fora de `0` e `5` → parar e sinalizar `blocked` razão `premissa`, colando a saída.
  - se um teste existente de `tests/test_backlog.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_despachar_grava_estado_e_imprime_ref` — `despachar GAM-T1` na cópia sai 0, a saída tem a linha que começa por `ref=`, o `estado.tsv` da cópia tem `GAM-T1` em `in-progress` e `tarefa-corrente.json` tem `tarefa == "GAM-T1"` e `ref` igual ao da saída. TR `test_tr_despachar_recusa_no_primeiro_gate_sem_escrever` — `GAM-T2` com `Verificação` que o `card_check` recusa: exit 1, stderr com `despachar: recusado — card_check:`, `estado.tsv` e `tarefa-corrente.json` intocados (a regra concorrente, "materializa e depois confere", deixaria `in-progress`). TF `test_tf_despachar_redespacho_reaproveita_ref` — `tarefa-corrente.json` já de `GAM-T1` com `ref` `abc`, tarefa de volta a `ready`: a saída traz `ref=abc`.
- **Verificação:**
  1. `python .claude/tools/backlog.py despachar --help` → `exit 0` — antes `exit 2`, depois `exit 0` (antes medido pelo consultor, `DAF-41`; depois esperado)
  2. `python -m pytest tests/test_backlog.py -q -k "despachar"` → `exit 0` — antes `exit 5`, depois `exit 0` (antes medido pelo consultor, `DAF-41`; depois esperado)
  3. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print(t.count('backlog.py despachar'),t.count('Despachada pelo verbo'))"` → `1 1` — antes `0 0`, depois `1 1` (antes medido pelo consultor, `DAF-41`; âncoras do passo 3 e do passo 4 conferidas, uma ocorrência cada)
  4. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (antes medido pelo consultor, `475 passed`, `DAF-41`; trava)
  5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (antes medido pelo consultor, `DAF-41`; trava)
- **Pronto quando:**
  - despacho de tarefa.conferências do despacho — um comando roda as conferências, marca a tarefa em curso e recusa pela primeira que falhar — Verificações 1 a 3
- **Fora do escopo desta tarefa:** o molde do despacho do consultor (`AF-T11`, que também edita a skill `scrum-master`).
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** verbo 'backlog.py despachar <ID>' roda modelo check, card_check, materializa in-progress, grava tarefa-corrente.json, captura o ref e imprime DESPACHO/HANDOVER/card/ref=; recusa pela primeira conferência que falhar, sem escrever; Passos 3 e 4 do scrum-master citam o verbo
  - **Contrato:** o condutor despacha com um comando; redespacho reaproveita o ref; a decodificação do stderr dos irmãos ainda não é UTF-8 (ressalva do laudo, com o consultor)
  - **Não refazer:** nada a declarar
  - **Pendente:** subprocess.run do despachar sem encoding='utf-8': razão com mojibake e traceback em byte indefinido (ressalva do laudo) — sanado pelo consultor no `DAF-42`

### AF-T11 — O consultor lê só as três entradas, e `estrategico=` é uma frase [Opus · esforço low · classe redacao]
- **Objetivo:** O consultor passa a responder cada acionamento lendo só as três entradas do despacho, com a avaliação estratégica numa frase.
- **Fundamento:** `DAF-17`, `F-16`.
- **Depende de:** `AF-T10`
- **Operação do modelo:** `OP-11`
  - OP-11: O consultor passa a responder cada acionamento lendo só as três entradas do despacho, com a avaliação estratégica numa frase.
  - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; despacho de tarefa — Quem implementa faz o despacho entregar o card sem corte e rodar num comando só as conferências que hoje se repetem à mão, recusando pela primeira que falhar.
- **Camada e fronteira:** texto de doutrina: o arquivo do agente `pantonic-consultant` (corpo, não o frontmatter) e a skill `scrum-master`, seção *Acionamento do consultor*.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-consultant.md`
  - `.claude/skills/scrum-master/SKILL.md`
- **Passos:**
  1. Em `.claude/agents/pantonic-consultant.md`, seção *O que você faz*, inserir depois da linha do item `1. **Lê o cenário, não o plano.**` a linha abaixo, recuada três espaços, como continuação do item 1 (uma linha só):

     ```text
        **Lê só as três entradas.** O despacho traz três entradas — o caminho do cenário, o id do card e a evidência (a linha de retorno do executor, a pendência do laudo ou o stderr do instrumento) —, e você lê só elas e, da doutrina, só a seção que o cenário aponta: relatório de auditoria, diário, RDO de outra tarefa e plano inteiro ficam fora, e fato que só eles teriam vai ao cenário como matéria inconclusiva. Caso medido (2026-09-27): o acionamento que leu o relatório de auditoria fora do cenário custou 131,2k tokens; o seguinte, com a instrução de não ler fora dele, 67,4k.
     ```
  2. No mesmo arquivo, inserir depois do terceiro sub-bullet do item 2 (a linha que começa por `   - ` + `` `rota=planejador` ``) e antes do item `3.` a linha abaixo, recuada três espaços, como continuação do item 2 (uma linha só):

     ```text
        A linha `estrategico=` tem **uma frase**, sem ponto no meio: o que o impedimento muda no escopo ou no objetivo do plano, ou qual decisão do dono ele revoga; o detalhe vai ao cenário, nunca à linha (caso medido, 2026-09-27: três frases num acionamento do plano fictício da auditoria).
     ```
  3. Em `.claude/skills/scrum-master/SKILL.md`, seção *Acionamento do consultor*, inserir depois do parágrafo que começa por `Forma **efêmera com cenário persistido**` o bloco abaixo, precedido e seguido de uma linha vazia (as quebras são as do bloco; o recuo de dois espaços não entra no arquivo, e as quatro linhas do molde ficam com quatro espaços, bloco de código por recuo):

     ```text
       Molde do despacho — as três entradas, e nada além delas:

           cenario=docs/plans/P-<n>-<slug>/cenario.md
           card=<ID>
           evidencia=<a linha de retorno do executor, a pendência do laudo ou o stderr do instrumento, verbatim>
           Leia só o cenário, o card e a evidência acima e, da doutrina, só o que o cenário aponta.
     ```
- **Restrições desta tarefa:**
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0 (o frontmatter do agente não muda).
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho).
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não mudar o frontmatter do agente; não mudar as regras de rota nem a tabela de estatística de acionamentos; não tocar a linha de telemetria da seção *Acionamento do consultor* (é da `AF-T5`).
- **Contingências:**
  - se o frontmatter do agente sair recusado por `python .claude/checks/frontmatter_yaml.py .claude/agents/pantonic-consultant.md` → a edição tocou o frontmatter: parar e sinalizar `blocked` razão `premissa`, colando o erro.
- **Testes:** nenhum teste novo (texto de doutrina); suítes a rodar: a inteira, como trava.
- **Verificação:**
  1. `python -c "from pathlib import Path;c=chr(96);t=Path('.claude/agents/pantonic-consultant.md').read_text(encoding='utf-8');print(t.count('Lê só as três entradas.'),t.count('A linha '+c+'estrategico='+c+' tem **uma frase**'))"` → `1 1` — antes `0 0`, depois `1 1` (esperado, não ensaiado)
  2. `python -c "from pathlib import Path;print(Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8').count('cenario=docs/plans/P-<n>-<slug>/cenario.md'))"` → `1` — antes `0`, depois `1` (esperado, não ensaiado)
  3. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
  4. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
- **Pronto quando:**
  - consultor.leitura por acionamento — lê só o cenário, o card, a evidência e a doutrina que o cenário aponta — Verificações 1 e 2
  - consultor.avaliação estratégica — vem em uma frase — Verificação 1
- **Fora do escopo desta tarefa:** a medida de tokens do consultor depois da mudança (lê-se na série `docs/telemetria.tsv`, com a gravação da `AF-T5`).
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** pantonic-consultant.md: item 1 ganha 'Lê só as três entradas' (:24) e o item 2 a regra de uma frase para estrategico= (:29); scrum-master seção Acionamento do consultor ganha o bloco do card
  - **Contrato:** o consultor lê só o cenário, o card e a evidência; estrategico= é uma frase sem ponto no meio
  - **Não refazer:** as duas regras do consultor
  - **Pendente:** nenhum

### AF-T12 — O veredito do marco é um comando [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** Quem conduz passa a gravar o veredito do dono no marco por um comando único, que o escreve em todos os lugares onde o marco aparece.
- **Fundamento:** `DAF-14`, `DAF-27`, `F-12`.
- **Depende de:** `AF-T6`
- **Operação do modelo:** `OP-12`
  - OP-12: Quem conduz passa a gravar o veredito do dono no marco por um comando único, que o escreve em todos os lugares onde o marco aparece.
  - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; fechamento de tarefa — Quem implementa faz o fechamento copiar cada achado de processo do laudo para os achados do plano, com a rota, sem repetir achado igual.
- **Camada e fronteira:** instrumento do kit `.claude/tools/encerrar.py`; carrega `backlog.py` por caminho, como hoje; não importa de `tests/`. A máquina não interpreta a frase do dono: o resultado entra por argumento.
- **Domínio:** *lugares do marco* (`DAF-27`) — (1) a célula `veredito` (última) da linha `| **Marco <n>** |` da tabela *Marcos de validação* do cabeçalho do plano; (2) o fim da seção `## 0.` do plano; (3) o status do plano no Marco 1. O cenário do consultor não é lugar do marco.
- **Arquivos-alvo:**
  - `.claude/tools/encerrar.py`
  - `tests/test_encerrar.py`
- **Contratos/classes:** subcomando `marco`, com `parents=[comuns]` (o analisador comum de hoje, que já traz `--plano`, `--repo` e `--data`) e mais: `--marco <n>` (inteiro), `--resultado {go,no-go}`, `--veredito "<frase>"` e, exclusivos entre si e opcionais, `--aceita-versao <k>` ou `--recusa-versao <k>`. Recusa com `marco: <razão>` no stderr, exit `1` e nada escrito, quando: o plano não existe; a linha `| **Marco <n>** |` não existe (`linha do Marco <n> ausente na tabela de marcos`); a seção `## 0.` não existe (`seção ## 0 ausente`); veio `--aceita-versao` ou `--recusa-versao` e o plano não tem a linha `## 1A. Modelo conceitual — versão pendente de validação` (`plano sem versão pendente (## 1A)`). Escritas, nesta ordem: (1) a última célula da linha do marco vira `<resultado> · <data> — "<frase>"`, com `|` da frase escrito `\|`; (2) antes do primeiro heading `## ` que vem depois de `## 0.`, entram as linhas `**Marco <n>, <data> — veredito do dono (<resultado>):**`, uma linha vazia, `> <frase>` e uma linha vazia; (3) com `--marco 1`, `--resultado go` e o plano em `blocked`, `_backlog.transacionar_status(repo, modelo, <id do plano>, "ready", nota="Marco 1 go em <data>")`. Com versão, imprime no stdout o dossiê abaixo; sempre imprime por último `marco: Marco <n> gravado — <resultado>`.
- **Passos:**
  1. Escrever a função `gravar_marco(...)` e o subcomando `marco` no `main`, pela regra de `Contratos/classes`.
  2. Com `--aceita-versao <k>` ou `--recusa-versao <k>`, imprimir o dossiê com as seis linhas abaixo (as quebras são as do bloco; o recuo de dois espaços não entra na saída; `<frase>`, `<n>`, `<k>` e `<plano>` se substituem):

     ```text
       Plano: <plano>
       Ato: emenda
       Motivo: Marco <n>, veredito do dono: "<frase>"
       Fato novo: o dono aceitou a versão <k> do modelo no Marco <n>.
       Restrição: a versão <k> passa a vigente e a anterior a obsoleta; o conteúdo da obsoleta sai do plano e o registro de versões guarda a linha (GOVERNANCA.md §3.2).
       Devolver: a seção ## 1 depois do ato e a linha nova do registro de versões.
     ```
     Com `--recusa-versao`, a linha `Fato novo` é `Fato novo: o dono recusou a versão <k> do modelo no Marco <n>.` e a `Restrição` é `Restrição: a versão <k> é eliminada e a vigente permanece, sem marca; o que foi entregue sob a versão recusada se refaz por card corretivo da operação afetada (GOVERNANCA.md §3.2).`
  3. Escrever os quatro testes da seção `Testes`, sobre plano temporário legado no molde de `PLANO` de `tests/test_encerrar.py`, com a linha `**Status:** `` `blocked` ``, a tabela de marcos `| marco | o que o dono lê | veredito |` com `| **Marco 1** | a seção 1 | pendente |` e uma seção `## 0. O problema, verbatim` antes de `## 5. Tarefas`.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 4 testes novos (referência datada: `452 passed`, 2026-09-27).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Nenhuma verificação de recusa escreve arquivo; todas as checagens rodam antes da primeira escrita.
- **Não fazer:** não escrever na `## 1` nem na `## 1A` (o ato de versão é do modelador); não tirar o resultado da frase do dono (ele vem só de `--resultado`); não mudar os verbos `tarefa`, `handover` e `plano`.
- **Contingências:**
  - se um teste existente de `tests/test_encerrar.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_marco_go_grava_celula_zero_e_tira_de_blocked` — `marco --marco 1 --resultado go --veredito "Pode seguir"`: a célula vira `go · 2026-09-26 — "Pode seguir"`, a `## 0` ganha a linha `> Pode seguir` e o plano sai de `blocked` para `ready`. TR `test_tr_marco_no_go_nao_muda_status` — o mesmo com `--resultado no-go`: células e `## 0` gravadas, plano segue `blocked` (a regra concorrente, "todo marco 1 libera o plano", o tiraria). TF `test_tf_marco_recusa_versao_imprime_dossie_de_emenda` — plano com a linha `## 1A. Modelo conceitual — versão pendente de validação` e `--recusa-versao 2 --veredito "Não aceito"`: o stdout tem `Ato: emenda` e `Motivo: Marco 1, veredito do dono: "Não aceito"`. TR `test_tr_marco_recusa_sem_linha_do_marco_sem_escrever` — `--marco 2` num plano só com o Marco 1: exit 1, stderr com `linha do Marco 2 ausente`, plano igual byte a byte.
- **Verificação:**
  1. `python .claude/tools/encerrar.py marco --help` → `exit 0` — antes `exit 2`, depois `exit 0` (esperado, não ensaiado)
  2. `python -m pytest tests/test_encerrar.py -q -k "marco"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado)
  3. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
  4. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
- **Pronto quando:**
  - marco de validação.registro do veredito — um comando grava o resultado dado pelo dono em todos os lugares do marco, sem interpretar a frase dele — Verificações 1 e 2
- **Fora do escopo desta tarefa:** o esqueleto do relatório de operações (`AF-T13`, que também edita `encerrar.py`); a promoção ou a eliminação da versão pendente (ato do modelador, com o dossiê que este verbo imprime).
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** subcomando 'encerrar.py marco' (gravar_marco) grava a célula do marco, o ato na ## 0 e, no Marco 1 go com plano blocked, a transição para ready; com --aceita/--recusa-versao imprime o dossiê de emenda; 4 testes em tests/test_encerrar.py
  - **Contrato:** o veredito do marco se grava por um comando; dois caminhos de borda com defeito (ressalva do laudo, com o consultor)
  - **Não refazer:** nada a declarar
  - **Pendente:** (a) regravar marco com frase que tinha pipe escapado deixa resto na célula; (b) Marco 1 go com transição recusada grava o plano antes de sair exit 1 (ressalva do laudo) — sanado pelo consultor no `DAF-43`

### AF-T13 — O esqueleto do relatório de operações sai por comando [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem conduz passa a gerar por comando o esqueleto do relatório de operações, em vez de reescrevê-lo de memória a cada plano.
- **Fundamento:** `DAF-22`, `DAF-34`, `F-21`.
- **Depende de:** `AF-T12`
- **Operação do modelo:** `OP-13`
  - OP-13: Quem conduz passa a gerar por comando o esqueleto do relatório de operações, em vez de reescrevê-lo de memória a cada plano.
  - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; fechamento de tarefa — Quem implementa faz o fechamento copiar cada achado de processo do laudo para os achados do plano, com a rota, sem repetir achado igual.
- **Camada e fronteira:** instrumento do kit `.claude/tools/encerrar.py` e a skill `entrega-de-encerramento`; `encerrar.py` carrega `backlog.py` e `caminhos.py` por caminho; não importa de `tests/`.
- **Arquivos-alvo:**
  - `.claude/tools/encerrar.py`
  - `tests/test_encerrar.py`
  - `.claude/skills/entrega-de-encerramento/SKILL.md`
- **Contratos/classes:** subcomando `operacoes`, com `parents=[comuns]` (o analisador comum de hoje, que já traz `--plano` e `--repo`) e mais a opção `--checar`. Sem `--checar`: grava em `caminhos.destino_operacoes(repo, plano)` o esqueleto abaixo; arquivo já existente é recusa (`operacoes: já existe <caminho>`, exit `1`, nada escrito). Com `--checar`: não escreve; lê o arquivo de `destino_operacoes` e imprime duas linhas, `nao citados: <ids separados por vírgula e espaço, ou nenhum>` (todo `### <ID> ` de card do plano que não aparece no documento como `` `<ID>` ``) e `sem os quatro blocos: <ids, ou nenhum>` (toda seção `## `` `<ID>` `` sem uma das quatro linhas de bloco); exit `0` quando as duas dizem `nenhum`, senão `1`; arquivo ausente é recusa (`operacoes: arquivo ausente <caminho>`, exit `1`). Tarefas lidas de `_backlog._parse_plano(plano, repo).tarefas` (`id`, `titulo`, `status`); tarefa `cancelled` entra na tabela do arco e não ganha seção.
- **Passos:**
  1. Escrever o subcomando com a regra de `Contratos/classes`. O esqueleto é, nesta ordem (as quebras são as do bloco; o recuo de dois espaços não entra no arquivo; `<título do plano>`, e em cada linha de tarefa `<ID>`, `<título>` e `<status>`, se substituem; a seção `## `` `<ID>` `` se repete por tarefa não `cancelled`, na ordem do plano):

     ```text
       # Operações — <título do plano>

       ## Abertura

       **O problema:**

       **A solução, em uma frase:**

       | termo | o que é |
       |---|---|

       ## O arco

       | estrato | pergunta que responde | tarefas |
       |---|---|---|

       | tarefa | título | status |
       |---|---|---|
       | `<ID>` | <título> | <status> |

       ## `<ID>` — <título>

       **Contexto que a motivou:**

       **O que é o artefato:**

       **Como funciona na prática:**

       **Protege contra:**

       ## O que vale além deste plano

       | regra | o que resolve | residência |
       |---|---|---|

       ## Os ganhos, medidos

       | medida | antes | depois |
       |---|---|---|

       ## O padrão que a execução revelou

       ## Pendências abertas ao fim do plano

       | pendência | por que ficou aberta | o que a fecha | bloqueia algo? |
       |---|---|---|---|
     ```
  2. Escrever os três testes da seção `Testes`, sobre o repositório temporário de `_montar_repo` (plano legado `P-0001-alfa.md`, destino `docs/OPERACOES_AS_IS_P-0001.md`).
  3. Em `.claude/skills/entrega-de-encerramento/SKILL.md`, seção *Procedimento*: o item `4.` passa a ser a linha `4. **Escreva as seções por tarefa** sobre o esqueleto que `` `python .claude/tools/encerrar.py operacoes --plano <plano>` `` gera (uma seção por tarefa viva, com os quatro blocos vazios), aplicando os três testes da regra de leitura.`; o item `6.` inteiro, com o bloco de código dele, e o item `7.` saem, e entra no lugar deles o item abaixo; o item `8.` passa a `7.` (as quebras são as do bloco; o recuo de dois espaços não entra no arquivo):

     ```text
       6. **Verifique a cobertura e a estrutura por comando**, não por leitura — todo card do plano citado
          no documento e toda seção de tarefa com os quatro blocos obrigatórios:
          `python .claude/tools/encerrar.py operacoes --plano <plano> --checar`, exit `0` com as linhas
          `nao citados: nenhum` e `sem os quatro blocos: nenhum`.
     ```
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 3 testes novos (referência datada: `452 passed`, 2026-09-27).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0 (a skill muda no corpo, não no frontmatter).
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não preencher os blocos do esqueleto (a redação é do relato, pela skill); não mudar `caminhos.destino_operacoes`; não mudar os demais verbos de `encerrar.py`.
- **Contingências:**
  - se um teste existente de `tests/test_encerrar.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_esqueleto_de_operacoes_uma_secao_por_card` — `operacoes --plano P-0001-alfa.md` grava o arquivo com exatamente uma linha que começa por `` ## `ALF-T1` `` e nenhuma de `ALF-T2` (`cancelled`), e a tabela do arco cita as duas. TR `test_tr_esqueleto_de_operacoes_nao_sobrescreve` — arquivo já existente: exit 1 e conteúdo intocado. TF `test_tf_esqueleto_de_operacoes_checar_cobertura` — sobre o esqueleto recém-gerado, `--checar` sai 0 com `nao citados: nenhum` e `sem os quatro blocos: nenhum`; com a linha `**Protege contra:**` apagada, sai 1 com `sem os quatro blocos: ALF-T1`.
- **Verificação:**
  1. `python .claude/tools/encerrar.py operacoes --help` → `exit 0` — antes `exit 2`, depois `exit 0` (esperado, não ensaiado)
  2. `python -m pytest tests/test_encerrar.py -q -k "esqueleto_de_operacoes"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado)
  3. `python -c "from pathlib import Path;t=Path('.claude/skills/entrega-de-encerramento/SKILL.md').read_text(encoding='utf-8');print(t.count('encerrar.py operacoes --plano'),t.count('citados = set(re.findall'))"` → `2 0` — antes `0 1`, depois `2 0` (esperado, não ensaiado)
  4. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
  5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
- **Pronto quando:**
  - relatório de operações.esqueleto — gerado por comando a partir das tarefas do plano, com a cobertura conferida — Verificações 1 a 3
- **Fora do escopo desta tarefa:** a redação do relatório de operações deste plano (ato de encerramento).
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** subcomando 'encerrar.py operacoes' grava o esqueleto do relatório de operações em caminhos.destino_operacoes (recusa se já existe) e, com --checar, lista 'nao citados' e 'sem os quatro blocos'; skill entrega-de-encerramento (Procedimento itens 4 e 6) cita o comando; 3 testes em tests/test_encerrar.py
  - **Contrato:** o relato do fechamento parte do esqueleto por comando e confere a cobertura com --checar; seção inteira ausente acusada na linha `sem seção:` desde o `DAF-44` (reparo do consultor, `AE-19`)
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum

### AF-T14 — A conferência do modelo julga a versão pendente, e a comparação mostra o contrato [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** A conferência do modelo passa a julgar a versão pendente pelas mesmas regras da vigente e a mostrar, na comparação entre as duas, o contrato que mudou.
- **Fundamento:** `DAF-21`, `DAF-28`, `F-20`, `F-31`.
- **Operação do modelo:** `OP-14`
  - OP-14: A conferência do modelo passa a julgar a versão pendente pelas mesmas regras da vigente e a mostrar, na comparação entre as duas, o contrato que mudou.
  - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.
- **Camada e fronteira:** instrumento do kit `.claude/tools/modelo.py` (verbos `check` e `show`); carrega `backlog.py` por caminho, como hoje; não importa de `tests/`.
- **Arquivos-alvo:**
  - `.claude/tools/modelo.py`
  - `tests/test_modelo.py`
  - `tests/fixtures/modelo/fluxo-pendente-contrato.md`
- **Contratos/classes:**
  - `validar(modelo, plano, modelo_pendente=None, *, pendente=False) -> list[str]` — com `pendente=True`, pula `V2`, `V4` e `V14` (os cards citam a vigente), `V19` e `V20`, e o `V13` só exige cabeçalho, tabela de objetos e tabela de estado (a `## 1A` não tem registro de versões). `verbo_check`, quando a `## 1A` existe, roda também `validar(modelo_pendente, plano, pendente=True)` e soma as violações dela com o prefixo `1A: ` (ex.: `1A: V5 OP-3 — objeto inexistente objeto fantasma`); exit e mensagem final como hoje, contando as duas.
  - `_diff_objetos(vigente, pendente)` acrescenta, para objeto presente nas duas versões com `contrato` diferente, a linha `[~] <objeto> — contrato: <contrato vigente> => <contrato pendente>`, depois das linhas de propriedade de hoje.
- **Passos:**
  1. Acrescentar o parâmetro `pendente` a `validar` e a chamada sobre a `## 1A` em `verbo_check`, pela regra de `Contratos/classes`.
  2. Acrescentar a comparação de contrato em `_diff_objetos`.
  3. Criar `tests/fixtures/modelo/fluxo-pendente-contrato.md`: cópia de `tests/fixtures/modelo/fluxo-valido.md` com, entre a tabela de `### 1.4 Registro de versões` e o heading seguinte, o bloco `## 1A. Modelo conceitual — versão pendente de validação` com o cabeçalho `**Estado do modelo:** versão 2 · 2026-09-27 · autor: modelador · 3 operações · 4 propriedades · situação: pendente` e cópias de `### 1.1`, `### 1.2` e `### 1.3` da vigente, com duas diferenças: na tabela de objetos, o contrato de `resultado um` é `um registro validado e datado`; na `OP-3`, o `precisa de:` é `resultado dois, registro auxiliar, objeto fantasma`.
  4. Escrever os dois testes da seção `Testes`.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 2 testes novos (referência datada: `452 passed`, 2026-09-27).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - `python .claude/tools/modelo.py check --plano docs/plans/P-0753-auditoria-estagio-1/plano.md` segue saindo 0 (o plano não tem `## 1A`).
- **Não fazer:** não mudar a gramática lida (`_localizar_secao`, `extrair_modelo`); não mudar `V1`..`V21` sobre a vigente; não editar `tests/fixtures/modelo/fluxo-pendente.md` (os testes de `show` o usam).
- **Contingências:**
  - se `check` sobre a fixture nova acusar, além de `1A: V5 OP-3 — objeto inexistente objeto fantasma`, outra violação → a cópia da vigente divergiu de `fluxo-valido.md`: refazer a cópia pelo passo 3 e seguir; se persistir, parar e sinalizar `blocked` razão `premissa`, colando a saída.
  - se um teste existente de `tests/test_modelo.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_check_pendente_roda_o_vocabulario` — `check` sobre a fixture nova sai 1 e o stderr tem a linha `1A: V5 OP-3 — objeto inexistente objeto fantasma` (a regra de hoje sai 0). TF `test_tf_drift_mostra_contrato_alterado` — `show --drift` sobre a fixture nova tem a linha `[~] resultado um — contrato: um registro validado => um registro validado e datado` (a regra de hoje não imprime linha de objeto, porque as propriedades não mudaram).
- **Verificação:**
  1. `python -m pytest tests/test_modelo.py -q -k "pendente_roda_o_vocabulario or drift_mostra_contrato"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado)
  2. `python .claude/tools/modelo.py check --plano tests/fixtures/modelo/fluxo-pendente-contrato.md` → `exit 1` — antes `exit 2`, depois `exit 1` (esperado, não ensaiado)
  3. `python .claude/tools/modelo.py show --plano tests/fixtures/modelo/fluxo-pendente-contrato.md --drift` → `[~] resultado um — contrato: um registro validado => um registro validado e datado` — antes `exit 2`, depois `[~] resultado um — contrato: um registro validado => um registro validado e datado` (esperado, não ensaiado)
  4. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
  5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
- **Pronto quando:**
  - conferência do modelo.versão pendente conferida — a versão pendente passa pelas mesmas regras da vigente, com as violações marcadas como dela — Verificações 1 e 2
  - conferência do modelo.comparação de contratos — a comparação mostra também o contrato e a propriedade de objeto que mudaram — Verificações 1 e 3
- **Fora do escopo desta tarefa:** o dossiê de versão no marco (`AF-T12`).
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** modelo.py: validar(pendente=True) roda o vocabulário sobre o bloco ## 1A e verbo_check soma as violações com prefixo '1A: '; _diff_objetos mostra '[~] <objeto> — contrato: <v> => <p>'; fixture tests/fixtures/modelo/fluxo-pendente-contrato.md; 2 TF em tests/test_modelo.py
  - **Contrato:** modelo.py check julga também a versão pendente; show --drift mostra contrato alterado; check sobre o P-0753 (com ## 1A v2) sai 0
  - **Não refazer:** o check da versão pendente e o drift de contrato
  - **Pendente:** nenhum

### AF-T15 — O piso comportamental e o teste de camadas passam a existir no hub [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** Quem executa cria o piso dos comportamentos trancados e o teste de camadas que a verificação obrigatória do kit exige.
- **Fundamento:** `DAF-9`, `DAF-35`, `F-4`, `F-35`.
- **Operação do modelo:** `OP-15`
  - OP-15: Quem executa cria o piso dos comportamentos trancados e o teste de camadas que a verificação obrigatória do kit exige.
  - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.
- **Camada e fronteira:** bateria de testes do hub (`tests/`); a regra de camadas do kit é: nenhum `.claude/tools/*.py` nem `.claude/checks/*.py` importa de `tests` e nenhum importa `caminhos` por `import` (carrega por `importlib.util.spec_from_file_location`). A skill `guardrails-check` não muda.
- **Arquivos-alvo:**
  - `tests/piso_comportamental.txt`
  - `tests/conformance/test_camadas_do_kit.py`
- **Contratos/classes:** `tests/piso_comportamental.txt` — lido por `.claude/checks/ratchet_piso.py`: uma linha por comportamento, `<pytest nodeid> — <frase>` (separador espaço, travessão, espaço); linhas vazias e iniciadas por `#` ignoradas. `tests/conformance/test_camadas_do_kit.py` — função `violacoes_de_camada(arquivos: list[Path]) -> list[str]`, que faz `ast.parse` de cada arquivo e devolve `<arquivo>:<linha> importa <módulo>` para todo `Import`/`ImportFrom` cujo primeiro componente do módulo é `tests` ou `caminhos`.
- **Passos:**
  1. Escrever `tests/conformance/test_camadas_do_kit.py` com `violacoes_de_camada` e os dois testes da seção `Testes`.
  2. Gerar `tests/piso_comportamental.txt` **depois** do passo 1: a primeira linha é `# Piso comportamental do hub — um comportamento trancado por linha (GOVERNANCA.md §4.4); gerado pela AF-T15 do P-0753.`; depois, uma linha por nodeid da saída de `python -m pytest --co -q` que contém `::test_tr_`, na ordem da coleta, na forma `<nodeid> — <frase>`, com `<frase>` = o nome da função sem o prefixo `test_tr_` e sem o sufixo de parâmetro entre colchetes, com `_` trocado por espaço.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 2 testes novos (referência datada: `452 passed`, 2026-09-27; `107` nodeids `::test_tr_` coletados na mesma data).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se criam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não mudar `.claude/skills/guardrails-check/SKILL.md`; não mudar `ratchet_piso.py`; não escrever frase à mão fora da regra do passo 2; não criar `conftest.py` nem `__init__.py`.
- **Contingências:**
  - se o teste de camadas acusar violação real num arquivo de `.claude/tools/` ou `.claude/checks/` → parar e sinalizar `blocked` razão `premissa`, colando a lista (medido na autoria: nenhuma).
  - se `python .claude/checks/ratchet_piso.py` sair diferente de 0 com o piso recém-gerado → a lista divergiu da coleta: gerar de novo pelo passo 2 e seguir; se persistir, parar e sinalizar `blocked` razão `premissa`, colando a saída.
- **Testes:** TF `test_tf_instrumentos_do_kit_nao_importam_tests_nem_caminhos` — `violacoes_de_camada` sobre todo `.claude/tools/*.py` e `.claude/checks/*.py` devolve lista vazia. TR `test_tr_camada_acusa_import_de_tests_e_de_caminhos` — arquivo temporário com `from tests import x` e `import caminhos` dá exatamente 2 violações (a regra concorrente, "só `tests`", daria 1).
- **Verificação:**
  1. `python .claude/checks/ratchet_piso.py` → `piso intacto` — antes `nenhum piso declarado`, depois `piso intacto` (esperado, não ensaiado)
  2. `python -m pytest tests/conformance -q` → `exit 0` — antes `exit 4`, depois `exit 0` (esperado, não ensaiado)
  3. `python -c "import subprocess,sys;from pathlib import Path;p=Path('tests/piso_comportamental.txt');c=subprocess.run([sys.executable,'-m','pytest','--co','-q'],capture_output=True,text=True).stdout.splitlines();tr=sorted(x.strip() for x in c if '::test_tr_' in x);print('ausente' if not p.exists() else ('iguais' if sorted(l.split(' — ')[0].strip() for l in p.read_text(encoding='utf-8').splitlines() if l.strip() and not l.startswith('#'))==tr else 'diferentes'))"` → `iguais` — antes `ausente`, depois `iguais` (esperado, não ensaiado)
  4. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
  5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
- **Pronto quando:**
  - bateria de testes do kit.piso e conformidade — o piso lista os comportamentos trancados e o teste de camadas roda na suíte — Verificações 1 a 3
- **Fora do escopo desta tarefa:** teste de TR acrescentado depois desta tarefa entra no piso por quem o cria, não por esta tarefa.
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** tests/piso_comportamental.txt com 124 nodeids de TR gerados da coleta (ratchet_piso.py sai 0); tests/conformance/test_camadas_do_kit.py com violacoes_de_camada e o par TF/TR
  - **Contrato:** o hub tem piso comportamental trancado e teste de camadas: instrumento do kit que importe tests ou caminhos por import quebra a suíte
  - **Não refazer:** o piso e o teste de camadas
  - **Pendente:** nenhum

### AF-T16 — Os verificadores em PowerShell escrevem UTF-8 no console [Sonnet · esforço low · classe mecanica]
- **Objetivo:** Os verificadores do kit passam a escrever os acentos corretamente no console do Windows.
- **Fundamento:** `DAF-23`, `F-23`, `F-34`.
- **Operação do modelo:** `OP-16`
  - OP-16: Os verificadores do kit passam a escrever os acentos corretamente no console do Windows.
  - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.
- **Camada e fronteira:** verificadores do kit em `.claude/checks/` (PowerShell 7); o texto das mensagens não muda.
- **Arquivos-alvo:**
  - `.claude/checks/check-readme.ps1`
  - `.claude/checks/kit_check.ps1`
- **Passos:**
  1. Em cada um dos dois arquivos, inserir logo depois da linha `$ErrorActionPreference = 'Stop'` a linha abaixo (uma linha só; `param(...)` segue sendo a primeira instrução do script):

     ```text
     [Console]::OutputEncoding = [Text.Encoding]::UTF8
     ```
- **Restrições desta tarefa:**
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0 e `pwsh -NoProfile -File .claude/checks/check-readme.ps1` sai 0.
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho).
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não mudar o texto de mensagem nenhuma; não trocar acento por ASCII; não mexer no bloco `param(...)`.
- **Contingências:**
  - se `tests/test_kit_check.py` cair por causa da saída em UTF-8 → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** nenhum teste novo; `tests/test_kit_check.py` e a suíte inteira como trava.
- **Verificação:**
  1. `python -c "import subprocess;r=subprocess.run(['pwsh','-NoProfile','-File','.claude/checks/check-readme.ps1'],capture_output=True);print(r.stdout.decode('utf-8','replace').count(chr(65533))>0)"` → `False` — antes `True`, depois `False` (esperado, não ensaiado)
  2. `python -c "from pathlib import Path;s='[Console]::OutputEncoding = [Text.Encoding]::UTF8';print(Path('.claude/checks/kit_check.ps1').read_text(encoding='utf-8').count(s),Path('.claude/checks/check-readme.ps1').read_text(encoding='utf-8').count(s))"` → `1 1` — antes `0 0`, depois `1 1` (esperado, não ensaiado)
  3. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
  4. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
- **Pronto quando:**
  - verificadores do console.acentos na saída — letra acentuada sai correta — Verificações 1 e 2
- **Fora do escopo desta tarefa:** os demais `.ps1` de `.claude/checks/` (a recomendação e a decisão nomeiam os dois).
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** [Console]::OutputEncoding = [Text.Encoding]::UTF8 logo depois de $ErrorActionPreference em .claude/checks/check-readme.ps1:45 e .claude/checks/kit_check.ps1:35
  - **Contrato:** os dois verificadores em PowerShell escrevem UTF-8 no console, sem caractere de substituição para quem lê a saída
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum

### AF-T17 — O pré-voo do pedido confere o que o dono cita antes da campanha [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** O planejador passa a conferir, antes de abrir a campanha, a existência de cada caminho, nome e opção que o pedido do dono cita.
- **Fundamento:** `DAF-16`, `DAF-31`, `F-14`.
- **Depende de:** `AF-T8`
- **Operação do modelo:** `OP-17`
  - OP-17: O planejador passa a conferir, antes de abrir a campanha, a existência de cada caminho, nome e opção que o pedido do dono cita.
  - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; planejador — Quem implementa recebe o roteiro de fases do agente e muda só a fase que a recomendação aponta, deixando as demais como estão.
- **Camada e fronteira:** instrumento novo do kit `.claude/tools/prevoo.py` (somente leitura; não importa de `tests/` nem de irmão) e a Fase 0 do arquivo do agente planejador (corpo, não o frontmatter).
- **Arquivos-alvo:**
  - `.claude/tools/prevoo.py` (novo)
  - `tests/test_prevoo.py` (novo)
  - `.claude/agents/pantonic-planner.md`
- **Contratos/classes:** `python .claude/tools/prevoo.py "<texto>" [--root <caminho>]` (raiz padrão: a do repositório, três níveis acima do arquivo). Força `sys.stdout.reconfigure(encoding="utf-8")` antes do primeiro `print`. Extrai do texto, na ordem da primeira aparição e sem repetir: **caminhos** — token terminado em `.py`, `.md`, `.ps1`, `.json`, `.tsv`, `.txt`, `.yml`, `.yaml` ou `.toml`, ou terminado em `/`; existe quando `(<root> / <token>)` existe; `onde` = o próprio caminho. **Símbolos** — nome seguido de `(`, ou identificador com `_` que não é parte de caminho nem de flag; existe quando algum `.py` sob `<root>` (fora de `.git` e `__pycache__`) tem a linha `def <nome>(` ou `class <nome>`; `onde` = `<arquivo>:<linha>` da primeira, com `/`. **Flags** — token que começa por `-` seguido de letra; existe quando algum `.py` sob `<root>/.claude` contém a flag entre aspas (`"<flag>"` ou `'<flag>'`); `onde` = `<arquivo>:<linha>` da primeira. Imprime a linha `citado | existe | onde` e uma linha `<citado> | <sim ou não> | <onde ou —>` por item. Exit `0` quando todo item existe (ou não há item), `1` quando algum não existe, `2` sem argumento (argparse).
- **Passos:**
  1. Escrever `.claude/tools/prevoo.py` pela regra de `Contratos/classes`, com `main(argv=None) -> int` e `if __name__ == "__main__": sys.exit(main())`.
  2. Escrever `tests/test_prevoo.py` com os testes da seção `Testes`, sobre árvore temporária (`--root <tmp_path>`), carregando o módulo por `importlib.util.spec_from_file_location`.
  3. Em `.claude/agents/pantonic-planner.md`: o título `### Fase 0 — Intake (sem ferramenta, 1 turno)` vira `### Fase 0 — Intake (uma ferramenta, o pré-voo; 1 turno)`; e, depois da linha do item `1. Transcreva o pedido do dono **verbatim**`, entra o parágrafo abaixo, recuado três espaços, como continuação do item 1 (as quebras são as do bloco; o recuo de dois espaços do bloco não entra no arquivo):

     ```text
          **Pré-voo do pedido.** A `## 0` recebe a tabela `citado | existe | onde` que
          `python .claude/tools/prevoo.py "<pedido>"` imprime para todo caminho, símbolo e flag do texto
          do dono, colada por quem conduz a sessão; sem ela, rode o instrumento como primeiro ato e cole a
          tabela. Linha com `não` volta ao dono antes da campanha, pela SAÍDA 2, com o citado e o `onde`
          vazio: premissa do pedido que não existe na árvore não vira pergunta ao scout (caso medido,
          2026-09-27: um nome de função citado no pedido e ausente da árvore custou uma instância inteira
          do planejador, 41,4k tokens).
     ```
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os testes novos (referência datada: `452 passed`, 2026-09-27).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0 (o frontmatter do agente não muda).
  - `python .claude/checks/dead_code.py` sai 0 (toda função nova é chamada a partir de `main`).
  - Só os `Arquivos-alvo` se editam ou se criam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não escrever em arquivo nenhum a partir do `prevoo.py`; não chamar rede; não mudar outra fase do arquivo do planejador; não registrar o instrumento em `.claude/settings.json` nem em `.claude/projecoes.json`.
- **Contingências:**
  - se `python .claude/checks/dead_code.py` acusar função do `prevoo.py` → a função não é chamada por `main`: ligá-la a `main` ou apagá-la, e seguir.
  - se `tests/piso_comportamental.txt` existir (entregue pela `AF-T15`) → acrescentar ao fim dele uma linha por TR novo desta tarefa, na forma `<nodeid> — <frase>` da `AF-T15`.
- **Testes:** TF `test_tf_prevoo_simbolo_ausente_diz_nao` — árvore temporária com `.claude/tools/caminhos.py` sem `ler_texto_utf8`: o texto `reutilizando a função ler_texto_utf8 de .claude/tools/caminhos.py` dá as linhas `.claude/tools/caminhos.py | sim | .claude/tools/caminhos.py` e `ler_texto_utf8 | não | —`, exit 1. TR `test_tr_prevoo_simbolo_definido_diz_onde` — com `def ler_texto_utf8(` na linha 3 do mesmo arquivo: `ler_texto_utf8 | sim | .claude/tools/caminhos.py:3`, exit 0 (a regra concorrente, "existe se aparece em qualquer lugar", aceitaria menção em `.md`; a fixture põe a menção num `.md` e a função ausente, e o TF acima tem de dar `não`). TF `test_tf_prevoo_flag_existente` — `.claude/tools/x.py` com `"--desde"`: o texto `rode com --desde` dá `--desde | sim | .claude/tools/x.py:<linha>`.
- **Verificação:**
  1. `python .claude/tools/prevoo.py "reutilizando a função ler_texto_utf8 de .claude/tools/caminhos.py"` → `ler_texto_utf8 | não | —` — antes `exit 2`, depois `ler_texto_utf8 | não | —` (esperado, não ensaiado)
  2. `python -m pytest tests/test_prevoo.py -q` → `exit 0` — antes `exit 4`, depois `exit 0` (esperado, não ensaiado)
  3. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print(t.count('sem ferramenta, 1 turno'),t.count('prevoo.py'))"` → `0 1` — antes `1 0`, depois `0 1` (esperado, não ensaiado)
  4. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
  5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
- **Pronto quando:**
  - planejador.conferência do pedido — antes da campanha, cada caminho, nome e opção citados no pedido é conferido, e o que não existe volta ao dono — Verificações 1 a 3
- **Fora do escopo desta tarefa:** a separação da campanha em blocos de leitura e de comando (`AF-T19`).
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** instrumento novo .claude/tools/prevoo.py (citado | existe | onde; exit 0/1/2), tests/test_prevoo.py com 3 testes, Fase 0 do pantonic-planner.md (:79-89) manda rodar o pré-voo; linha do TR em tests/piso_comportamental.txt
  - **Contrato:** o planejador confere caminhos, símbolos e flags citados pelo dono antes da campanha; a leitura de token ainda não normaliza crase e pontuação (ressalva do laudo, com o consultor; sanada no `DAF-45`)
  - **Não refazer:** nada a declarar
  - **Pendente:** prevoo.py usa str.split() sem tirar crase, vírgula, ponto, ponto-e-vírgula nem parênteses: citação em crase e 'nome()' saem sem item (ressalva do laudo; sanada no `DAF-45`)

### AF-T18 — O guia de entrada descreve o kit como ele fica [Sonnet · esforço medium · classe redacao]
- **Objetivo:** Quem executa revisa o guia de entrada do kit para que ele descreva o kit como fica depois das mudanças deste plano.
- **Fundamento:** `DAF-2` (revisão do `README.md` ao fim, G-README dever 2), `DAF-24`; as mudanças descritas vêm das `AF-T5`, `AF-T8`, `AF-T9`, `AF-T10`, `AF-T12`, `AF-T13`, `AF-T14` e `AF-T17`.
- **Depende de:** `AF-T1`, `AF-T2`, `AF-T3`, `AF-T4`, `AF-T5`, `AF-T6`, `AF-T7`, `AF-T8`, `AF-T9`, `AF-T10`, `AF-T11`, `AF-T12`, `AF-T13`, `AF-T14`, `AF-T15`, `AF-T16`, `AF-T17`
- **Operação do modelo:** `OP-18`
  - OP-18: Quem executa revisa o guia de entrada do kit para que ele descreva o kit como fica depois das mudanças deste plano.
  - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; série de telemetria — Quem implementa faz o gancho gravar toda rodada de agente do kit, com o papel no identificador, e a soma do plano contar todas elas.; linha de retorno do revisor — Quem implementa acrescenta a recomendação à linha e faz todos os que a leem aceitarem a forma nova no mesmo ato.; despacho de tarefa — Quem implementa faz o despacho entregar o card sem corte e rodar num comando só as conferências que hoje se repetem à mão, recusando pela primeira que falhar.; marco de validação — Quem implementa faz um comando receber o resultado do dono como escolha explícita e gravá-lo em todos os lugares onde o marco aparece, sem interpretar a frase do dono.; relatório de operações — Quem implementa faz um comando gerar o esqueleto do relato a partir das tarefas do plano e conferir a cobertura dele.; conferência do modelo — Quem implementa faz a conferência julgar a versão pendente pelas mesmas regras da vigente, e a comparação mostrar o contrato e a propriedade que mudaram.; planejador — Quem implementa recebe o roteiro de fases do agente e muda só a fase que a recomendação aponta, deixando as demais como estão.
- **Camada e fronteira:** documentação pública do hub (`README.md`); `.claude/README.md` é derivado e não se edita à mão.
- **Arquivos-alvo:**
  - `README.md`
- **Passos:**
  1. Seção *Anatomia do kit*, o bullet de `.claude/tools/backlog.py` (cinco linhas, de `- `` `.claude/tools/backlog.py` `` — o instrumento do diário de obras, em sete verbos` até `a linha de priorização.`) vira o bloco abaixo (as quebras são as do bloco; o recuo de dois espaços não entra no arquivo):

     ```text
       - `.claude/tools/backlog.py` — o instrumento do diário de obras, em oito verbos: `next` seleciona a
         próxima tarefa de forma determinística e imprime o card inteiro, `show` devolve o card inteiro de
         um item, `check` faz o lint da gramática do diário e dos planos — o plano recém-esboçado, com o
         estado registrado e ainda fora da fila, inclusive —, `status` e `start` transicionam uma tarefa e
         projetam a mudança nos registros derivados, `despachar` roda os gates do despacho, materializa
         `in-progress`, grava a tarefa corrente com o ponto de partida e imprime o card, `drain` leva o
         inbox de planos ao índice, e `diretiva` reescreve a linha de priorização.
     ```
  2. Mesma seção, o bullet de `.claude/tools/encerrar.py` (sete linhas, de `- `` `.claude/tools/encerrar.py` `` — o instrumento de fechamento, em três verbos` até `Os três recusam sem escrever quando falta insumo.`) vira o bloco abaixo, seguido do bullet novo do `prevoo.py` (as quebras são as do bloco; o recuo de dois espaços não entra no arquivo):

     ```text
       - `.claude/tools/encerrar.py` — o instrumento de fechamento, em cinco verbos: `handover` registra no
         próprio card, de máquina, o que quem vem depois espera da tarefa (o que foi entregue, com o que se
         pode contar, o que não refazer, o que fica pendente), e é esse campo que a seleção da próxima tarefa
         devolve à sucessora; `tarefa` leva a tarefa em revisão a concluída num ato só — confere o modelo do
         plano, projeta o estado, escreve o registro da tarefa em três seções (humano, máquina, histórico)
         com o pacote transcrito do laudo, garante a linha de telemetria e registra com rota os achados,
         inclusive cada achado de processo do laudo; `marco` grava o resultado que o dono deu num marco em
         todos os lugares onde o marco aparece; `operacoes` gera o esqueleto do relatório de operações e
         confere a cobertura dele; `plano` fecha o plano sem tarefa aberta — estado, relatório de entrega
         nas mesmas três seções e uma linha no diário. Os cinco recusam sem escrever quando falta insumo.
       - `.claude/tools/prevoo.py` — o pré-voo do pedido: confere cada caminho, símbolo e flag que o texto
         do dono cita e imprime a tabela `citado | existe | onde`, que abre o plano antes de qualquer
         campanha.
     ```
  3. Seção *O modelo de domínio do plano*, as duas linhas depois de `antigo:` viram as três depois de `novo:` (as quebras são as do bloco; os rótulos não entram no arquivo):

     ```text
     antigo:
     a sessão o despacha. O instrumento `.claude/tools/modelo.py` confere a seção (`check`) e gera a
     leitura do dono (`show`), que abre pelo estágio atual. Planos escritos antes desta doutrina não são
     novo:
     a sessão o despacha. O instrumento `.claude/tools/modelo.py` confere a seção vigente e a versão
     pendente (`check`) e gera a leitura do dono (`show`), que abre pelo estágio atual e, com `--drift`,
     mostra o que muda entre as duas versões, contratos inclusive. Planos escritos antes desta doutrina não são
     ```
  4. Seção *Memória e telemetria*, as duas linhas depois de `antigo:` viram as quatro depois de `novo:` (as quebras são as do bloco; os rótulos não entram no arquivo):

     ```text
     antigo:
     com a sessão). Quem escreve a linha é **o orquestrador**, nos dois pontos de fechamento — ao fechar
     cada tarefa e ao encerrar a janela. O valor registrado sai do dado medido da
     novo:
     com a sessão). Quem escreve a linha é o hook `SubagentStop`, a cada rodada de agente do kit, com o
     papel no identificador da tarefa (`<ID>`, `<ID>-revisao`, `<ID>-consultor-<n>`, `<P-n>-planejador`,
     `<P-n>-modelador`, `<P-n>-scout`); **o orquestrador** só a escreve no fechamento, quando o hook não
     disparou. O valor registrado sai do dado medido da
     ```
  5. Rodar `pwsh -NoProfile -File .claude/checks/check-readme.ps1` e conferir exit 0.
- **Restrições desta tarefa:**
  - `pwsh -NoProfile -File .claude/checks/check-readme.ps1` sai 0 e `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho).
  - Só o `README.md` se edita; nada fora dele se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não editar `.claude/README.md` (derivado); não reescrever seção fora das quatro dos passos; não acrescentar descrição das `AF-T19`, `AF-T20` e `AF-T21`, que esperam o veredito do dono.
- **Contingências:**
  - se o trecho `antigo:` de um passo não existir verbatim no `README.md` → parar e sinalizar `blocked` razão `premissa`, nomeando o passo.
  - se `check-readme.ps1` sair diferente de 0 → parar e sinalizar `blocked` razão `premissa`, colando a saída.
- **Testes:** nenhum teste novo; `pwsh -NoProfile -File .claude/checks/check-readme.ps1` e a suíte inteira.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('README.md').read_text(encoding='utf-8');print(t.count('em sete verbos'),t.count('em oito verbos'),t.count('em cinco verbos'),t.count('prevoo.py'),t.count('Quem escreve a linha é o hook'))"` → `0 1 1 1 1` — antes `1 0 0 0 0`, depois `0 1 1 1 1` (esperado, não ensaiado)
  2. `pwsh -NoProfile -File .claude/checks/check-readme.ps1` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
  3. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
  4. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
- **Pronto quando:**
  - guia de entrada do kit.aderência ao kit entregue — descreve o kit com as mudanças deste plano — Verificações 1 e 2
- **Fora do escopo desta tarefa:** o veredito do dono sobre o `README.md` revisado — gate do Marco 2, não critério de pronto deste card.
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** README.md: backlog.py em oito verbos com despachar (:906), encerrar.py em cinco verbos com marco e operacoes (:916), bullet novo de prevoo.py (:926), modelo.py check/show --drift sobre a versão pendente (~:695), telemetria gravada pelo hook SubagentStop (~:989)
  - **Contrato:** o guia de entrada descreve os instrumentos como a janela os deixou; check-readme.ps1 sai 0
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum

### AF-T19 — A campanha do planejador separa as perguntas de leitura das de comando [Opus · esforço low · classe redacao]
- **Objetivo:** O planejador passa a mandar ao batedor só as perguntas de leitura, deixando as de comando para quem conduz a sessão.
- **Fundamento:** `DAF-5`, `DAF-6`, `F-5`, `F-6`. **Espera o veredito do dono no Marco 1** (card nasce `blocked` razão `dependencia`). Opções registradas: rota (a), recomendada e escrita neste card — a campanha em dois blocos fixados no arquivo do agente; rota (b) — nasce `.claude/tools/sondar.py`, que recebe um arquivo com um comando por linha e devolve stdout, stderr e exit de cada um, e a campanha cita o instrumento (`[Sonnet · esforço medium · classe implementacao]`). Veredito na rota (b) → rodada de replanejamento, card corretivo `AF-T19a` da `OP-19`.
- **Depende de:** `AF-T17`
- **Operação do modelo:** `OP-19`
  - OP-19: O planejador passa a mandar ao batedor só as perguntas de leitura, deixando as de comando para quem conduz a sessão.
  - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; planejador — Quem implementa recebe o roteiro de fases do agente e muda só a fase que a recomendação aponta, deixando as demais como estão.; escolha do dono no primeiro marco — Ninguém altera: o dono as dá no primeiro marco, e a operação que depende de cada uma espera por ela.
- **Camada e fronteira:** texto de doutrina: a Fase 1 do arquivo do agente planejador (corpo, não o frontmatter).
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md`
- **Passos:**
  1. Fase 1, o trecho depois de `antigo:` vira o trecho depois de `novo:` (sem quebra nova e sem refluxo; os rótulos não entram no arquivo):

     ```text
     antigo: fechadas, no formato que o scout consome, e **encerre sem escrever plano**.
     novo: fechadas, nos dois blocos da *Forma da campanha*, abaixo, e **encerre sem escrever plano**.
     ```
  2. Fase 1, o bullet de cinco linhas que começa por `- **Todo comando que vai aparecer numa linha de` vira o bloco abaixo (as quebras são as do bloco; o recuo de dois espaços não entra no arquivo):

     ```text
       - **Todo comando que vai aparecer numa linha de `Verificação` com literal esperado entra na campanha
         como pergunta de comando**, no bloco *Perguntas de comando*, nunca no bloco do scout: o
         `pantonic-scout` só lê (`Read`, `Glob`, `Grep`) e não roda comando. Vale para ferramenta externa
         do dia a dia — `git`, `pytest`, `pwsh` —, não só para instrumento do kit: o erro que custou a
         `LM-T1` do `P-0740` foi escrever a saída de `git check-ignore -v` e de `git status --porcelain`
         de memória (2026-09-18, `RP-2`).
     ```
  3. Fase 1, inserir antes da linha que começa por `Orçamento: no máximo **duas** rodadas` o bloco abaixo, seguido de uma linha vazia (as quebras são as do bloco; o recuo de dois espaços não entra no arquivo):

     ```text
       **Forma da campanha (SAÍDA 1).** A campanha tem dois blocos, nesta ordem, e toda pergunta mora em
       exatamente um deles. *Perguntas de leitura* vão ao `pantonic-scout`, uma por item:
       `L<n>. <pergunta fechada> · área: <caminhos> · volta: <caminho:linha, assinatura ou condição> ·
       teto: 40 linhas`. *Perguntas de comando* quem conduz a sessão roda e cola, uma por item:
       `C<n>. <comando exato, como vai à linha de Verificação> · volta: stdout literal e exit code`.
     ```
- **Restrições desta tarefa:**
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0 (o frontmatter do agente não muda).
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo).
  - Só o `Arquivos-alvo` se edita; nada fora dele se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não tocar as outras fases do arquivo (a Fase 0 é da `AF-T17`, a Fase 4 da `AF-T21`); não criar `.claude/tools/sondar.py` (rota b, fora deste card); não mudar o frontmatter do agente.
- **Contingências:**
  - se o trecho `antigo:` do passo 1 ou o bullet do passo 2 não existir verbatim → parar e sinalizar `blocked` razão `premissa`, nomeando o passo.
- **Testes:** nenhum teste novo; a suíte inteira como trava.
- **Verificação:**
  1. `python -c "from pathlib import Path;c=chr(96);t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print(t.count('rode '+c+'<comando exato>'),t.count('Perguntas de comando'),t.count('no formato que o scout consome'))"` → `0 2 0` — antes `1 0 1`, depois `0 2 0` (esperado, não ensaiado)
  2. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
  3. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
- **Pronto quando:**
  - planejador.campanha ao batedor — perguntas de leitura vão ao batedor e perguntas de comando a quem conduz, cada bloco na forma fixada — Verificação 1
- **Fora do escopo desta tarefa:** `.claude/tools/sondar.py` (rota b).

### AF-T19a — O batedor roda no Opus, com a ferramenta de comando, e o kit deixa de mandar a coleta ao modelo barato [Sonnet · esforço medium · classe redacao]
- **Objetivo:** O batedor passa a rodar no Opus, com a ferramenta de comando, e a receber do kit só a varredura ampla, a pergunta de comando da campanha do planejador inclusive.
- **Fundamento:** `DAF-46` (revoga a `DAF-6`), `F-36`, `RP-1`, sexto ato da §0. Card corretivo da `AF-T19` (`cancelled`), mesma operação.
- **Depende de:** `AF-T21`
- **Operação do modelo:** `OP-19`
  - OP-19: O batedor passa a rodar no Opus, com a ferramenta de comando, e a receber do kit só a varredura ampla, a pergunta de comando da campanha do planejador inclusive.
  - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; planejador — Quem implementa recebe o roteiro de fases do agente e muda só a fase que a recomendação aponta, deixando as demais como estão.; escolha do dono no primeiro marco — Ninguém altera: o dono as dá no primeiro marco, e a operação que depende de cada uma espera por ela.
  - altera: batedor — Quem implementa troca o modelo e as ferramentas do batedor, tanto no do projeto quanto no modelo global de onde ele é copiado, e acerta as instruções do kit que mandam a coleta ao modelo barato. A campanha que o planejador manda a ele fica como está.
- **Camada e fronteira:** texto de doutrina e frontmatter de agente — os dois batedores (`.claude/agents/pantonic-scout.md` e o canônico global `.claude/global/agents/context-scout.md`), a matriz de papéis de `GOVERNANCA.md` §3, os dois guias README, três skills do projeto, duas skills e um documento da camada global, e as duas mensagens da fase de leitura do gancho global de modelo por fase (só o texto das mensagens; a lógica do gancho não muda).
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-scout.md`
  - `.claude/global/agents/context-scout.md`
  - `GOVERNANCA.md`
  - `README.md`
  - `.claude/README.md`
  - `.claude/skills/modelo-por-fase/SKILL.md`
  - `.claude/skills/audit-sweep/SKILL.md`
  - `.claude/skills/passagem-de-bastao/SKILL.md`
  - `.claude/global/skills/context-prep/SKILL.md`
  - `.claude/global/skills/onboard/SKILL.md`
  - `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`
  - `.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md`
- **Passos:** em cada troca, o trecho depois de `antigo:` vira o trecho depois de `novo:` (sem quebra nova e sem refluxo; os rótulos não entram no arquivo); em cada inserção, as quebras são as do bloco e o recuo de cinco espaços do bloco não entra no arquivo.
  1. `.claude/agents/pantonic-scout.md`, frontmatter, três trocas:

     ```text
     antigo: description: Agente de coleta Pantonic* (somente leitura, modelo barato). Usar para search, grep e leitura de codebase/documentos, devolvendo
     novo: description: Agente de coleta Pantonic* (não edita arquivo). Usar para search, grep, leitura de codebase/documentos e comando de consulta que a pergunta traz pronto, devolvendo
     antigo: model: haiku
     novo: model: opus
     antigo: tools: Read, Glob, Grep
     novo: tools: Read, Glob, Grep, Bash
     ```
  2. No mesmo arquivo, `## Regras`: depois da linha `- Prefira Grep dirigido a leituras; Read sempre com offset/limit na faixa relevante.`, entra o bloco:

     ```text
     - **Comando de consulta:** pergunta que traz um comando exato você roda com `Bash`, verbatim, e
       devolve o stdout literal e o exit code (≤ 40 linhas; passou disso, as 40 primeiras e o número de
       linhas omitidas). Não roda comando que escreva, mova ou apague arquivo, nem `git` que altere a
       árvore ou o histórico: pergunta assim não se roda e vai a *Lacunas*, com o comando.
     - **Contagem e filtro:** conte e filtre pela própria ferramenta (modo de contagem, glob, exclusão
       de pasta, comando de consulta), nunca somando uma lista à mão; o número do dossiê é o que a
       ferramenta imprimiu.
     ```
  3. `.claude/global/agents/context-scout.md`, frontmatter e corpo, cinco trocas:

     ```text
     antigo: description: Batedor de contexto barato (Haiku). Recebe
     novo: description: Batedor de contexto. Recebe
     antigo: no modelo principal. Somente leitura.
     novo: no modelo principal. Não edita arquivo.
     antigo: tools: Read, Glob, Grep
     novo: tools: Read, Glob, Grep, Bash
     antigo: model: haiku
     novo: model: opus
     antigo: explora o repositório de forma barata e devolve um dossiê
     novo: explora o repositório e devolve um dossiê
     ```
  4. No mesmo arquivo, `## Regras de exploração`: depois da linha `- Pare quando a pergunta estiver respondida — não explore "por completude".`, entra o mesmo bloco do passo 2.
  5. `GOVERNANCA.md` §3, a linha da tabela que começa por `| **Coleta** |` inteira vira:

     ```text
     | **Coleta** | O mais poderoso disponível (Opus) — a coleta alimenta toda decisão seguinte, e erro de contagem ou de escopo nela passa em silêncio | Search, grep, leitura de codebase/documentos/prompts e comando de consulta que a pergunta traz pronto; filtra e devolve só o pertinente, protegendo o contexto de quem pediu. Read de âncora já conhecida ou Grep de string exata, quem precisa do dado faz direto | Não edita, não conclui tarefa, não emite juízo sobre o que coletou; não roda comando que escreva na árvore |
     ```
  6. `README.md`, duas trocas de linha de tabela:

     ```text
     antigo: | Coleta / varredura | O mais barato — Haiku | Search, grep, leitura de codebase e documentos; devolve dossiê compacto |
     novo: | Coleta / varredura | O mais poderoso disponível — Opus, em subagente | Search, grep, leitura de codebase e documentos e comando de consulta; devolve dossiê compacto. Leitura pontual, quem precisa do dado faz direto |
     antigo: | `pantonic-scout` | Haiku | Buscas, greps e leitura de codebase e documentos; devolve dossiê compacto para preservar o contexto dos caros. |
     novo: | `pantonic-scout` | Opus | Buscas, greps, leitura de codebase e documentos e comando de consulta; devolve dossiê compacto para preservar o contexto de quem pediu. |
     ```
  7. `.claude/README.md`, fora da região gerada:

     ```text
     antigo: via `pantonic-scout` (Haiku) e grava
     novo: via `pantonic-scout` e grava
     ```
  8. `.claude/skills/modelo-por-fase/SKILL.md`, a linha da tabela que começa por `| Varredura (search/grep/leitura ampla) |` inteira vira:

     ```text
     | Varredura (search/grep/leitura ampla) | Opus, em subagente de coleta (`pantonic-scout` ou `context-scout`); leitura pontual, direto no modelo ativo | Levantar contexto antes de planejar/executar |
     ```
  9. `.claude/skills/audit-sweep/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md` e `.claude/global/skills/onboard/SKILL.md`, uma troca em cada, nessa ordem:

     ```text
     antigo: `pantonic-scout`, Haiku, pelos critérios
     novo: `pantonic-scout`, pelos critérios
     antigo: vai para o papel barato —
     novo: vai para o papel de coleta —
     antigo: `context-scout` (roda em Haiku; critérios de corte na skill
     novo: `context-scout` (critérios de corte na skill
     ```
  10. `.claude/global/skills/context-prep/SKILL.md`, quatro trocas:

     ```text
     antigo: ao subagente context-scout (Haiku) e entrega ao modelo principal só um dossiê compacto.
     novo: ao subagente context-scout e entrega ao modelo principal só um dossiê compacto, protegendo o contexto dele.
     antigo: # context-prep — exploração no Haiku, inteligência no modelo principal
     novo: # context-prep — exploração em subagente, inteligência no modelo principal
     antigo: fase para o subagente [[context-scout]] (`model: haiku`), preservando o contexto e o custo do
     novo: fase para o subagente [[context-scout]], preservando o contexto do
     antigo: (o agente já fixa `model: haiku`)
     novo: (o agente já fixa o modelo)
     ```
  11. `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, entrada `"reading"`: as quatro linhas de texto do bloco `antigo` viram as cinco do bloco `novo` (recuo de oito espaços no arquivo, como as vizinhas):

     ```text
     antigo:
             "\U0001F7E1 Fase de leitura/varredura — Haiku basta, ou delegue ao "
             "context-scout. Considere `/model haiku`.",
             "Gate modelo-por-fase: este prompt e leitura/varredura (Regra 7). Prefira "
             "delegar ao subagente context-scout (Haiku) a ler tudo no modelo caro.",
     novo:
             "\U0001F7E1 Fase de leitura/varredura — leitura pontual, faça direto; "
             "varredura ampla, delegue ao context-scout.",
             "Gate modelo-por-fase: este prompt e leitura/varredura (Regra 7). Leitura "
             "pontual (ancora conhecida, grep exato): faca direto. Varredura ampla: delegue "
             "ao subagente context-scout, para proteger o contexto.",
     ```
  12. `.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md`:

     ```text
     antigo: - Exploração/varredura → modelo barato (Haiku, ex.: context-scout).
     novo: - Exploração/varredura ampla → subagente de coleta (context-scout, Opus), para proteger o contexto; leitura pontual, direto no modelo ativo.
     ```
  13. Regenerar a tabela de agentes de `.claude/README.md` com `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` (a linha do `pantonic-scout` passa a `Opus` e à descrição nova).
  - **Estado de partida do redespacho (`DAF-47`):** os passos 1 a 13 já estão aplicados na árvore pelo primeiro despacho, conferidos pelo consultor em 2026-09-27 (cada trecho `novo:` presente; Verificações 1 a 6 medidas). Não os reaplique: trecho `antigo:` ausente aqui não é parada. O redespacho roda as Verificações e fecha.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho (nenhum teste novo; referência datada: `498 tests collected`, 2026-09-27).
  - `python .claude/checks/frontmatter_yaml.py .claude/agents/pantonic-scout.md .claude/global/agents/context-scout.md` sai 0.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0 depois do passo 13.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não mudar a Fase 1 nem outra parte do arquivo do planejador (a campanha fica como está); não tocar o `pantonic-benchmarker` nem as linhas de `GOVERNANCA.md` e dos README que falam dele; não mudar a lógica do gancho de modelo por fase, só as duas mensagens da entrada `"reading"`; não rodar `materializar.py apply` nem escrever em `~/.claude` (a projeção global é ato do dono); não editar `.claude/settings*.json` nem `.claude/projecoes.json` (I-6).
- **Contingências:**
  - se um trecho `antigo:`, uma linha de âncora de inserção ou uma linha de tabela citada não existir verbatim → parar e sinalizar `blocked` razão `premissa`, nomeando o passo — salvo no redespacho do `DAF-47`, em que o trecho `novo:` do passo já está na árvore.
  - se `kit_check.ps1 -Mode generate` mudar `.claude/README.md` fora das duas regiões geradas (`<!-- kit:agents:begin -->`..`end` e `<!-- kit:skills:begin -->`..`end`), ou se o `check-drift` não sair 0 depois dele → parar e sinalizar `blocked` razão `premissa`, colando o diff. Dentro das regiões, o `generate` também ressincroniza linhas que a árvore já trazia fora de sincronia com o frontmatter (`DAF-47`, medido: `pantonic-consultant`, `pantonic-planner`, `modelo-por-fase`, e as linhas novas de `fatos-frescos` e `mensagem-ao-dono`) — é o efeito esperado, não parada.
  - se um teste existente cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** nenhum teste novo; a suíte inteira como trava.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-scout.md').read_text(encoding='utf-8');print('model: opus' in t,'tools: Read, Glob, Grep, Bash' in t,'Contagem e filtro' in t)"` → `True True True` — antes `False False False`, depois `True True True` (medido pelo consultor em 2026-09-27 com os passos 1-13 aplicados, `DAF-47`)
  2. `python -c "from pathlib import Path;t=Path('.claude/global/agents/context-scout.md').read_text(encoding='utf-8');print('model: opus' in t,'tools: Read, Glob, Grep, Bash' in t,'Contagem e filtro' in t)"` → `True True True` — antes `False False False`, depois `True True True` (medido pelo consultor em 2026-09-27 com os passos 1-13 aplicados, `DAF-47`)
  3. `python -c "from pathlib import Path;fs=['.claude/agents/pantonic-scout.md','.claude/global/agents/context-scout.md','GOVERNANCA.md','README.md','.claude/README.md','.claude/skills/modelo-por-fase/SKILL.md','.claude/skills/audit-sweep/SKILL.md','.claude/skills/passagem-de-bastao/SKILL.md','.claude/global/skills/context-prep/SKILL.md','.claude/global/skills/onboard/SKILL.md','.claude/global/hooks/modelo_por_fase_userpromptsubmit.py','.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md'];print(sum(Path(f).read_text(encoding='utf-8').lower().count('haiku') for f in fs))"` → `8` — antes `27`, depois `8` (medido pelo consultor em 2026-09-27 com os passos 1-13 aplicados, `DAF-47`; as 8 que ficam: a ordem de modelos e o benchmarker, fora do batedor)
  4. `python .claude/checks/frontmatter_yaml.py .claude/agents/pantonic-scout.md .claude/global/agents/context-scout.md` → `exit 0` — antes `exit 0`, depois `exit 0` (medido pelo consultor em 2026-09-27 com os passos 1-13 aplicados, `DAF-47`; trava)
  5. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (medido pelo consultor em 2026-09-27 com os passos 1-13 aplicados, `DAF-47`; trava)
  6. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (medido pelo consultor em 2026-09-27 com os passos 1-13 aplicados, `DAF-47`; trava)
- **Pronto quando:**
  - batedor.modelo em que roda — roda no Opus, nos dois lugares, o que acertou as quatro coletas da mesma avaliação — Verificações 1 e 2
  - batedor.ferramenta de comando — tem a ferramenta de comando e responde também à pergunta de comando; não roda nada que escreva no projeto e conta e filtra pela própria ferramenta, nunca somando lista à mão; ninguém mais roda comando à mão para o planejador — Verificações 1 e 2
  - batedor.coleta que recebe — a leitura de um trecho já localizado quem precisa do dado faz direto; a varredura ampla segue com o batedor, para poupar o contexto de quem pede; nenhuma instrução do kit manda a coleta ao modelo barato — Verificação 3
- **Fora do escopo desta tarefa:** o `pantonic-benchmarker`; a projeção global em `~/.claude` (ato do dono); a propagação aos projetos derivados (plano próprio); a verificação "impedimento de papel é configuração do kit?" na Fase 1 do planejador (`RP-1`, auditoria final).
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** batedor em Opus com Bash nos dois lugares (.claude/agents/pantonic-scout.md frontmatter e ## Regras; .claude/global/agents/context-scout.md); GOVERNANCA.md §3 linha Coleta; README.md e .claude/README.md (tabela regenerada, check-drift 0); modelo-por-fase, audit-sweep, passagem-de-bastao, context-prep, onboard, gancho modelo_por_fase (entrada reading) e RECOMENDACOES_CONSUMO_GLOBAL sem mandar coleta ao modelo barato; haiku residual = 8 (ordem de modelos e benchmarker)
  - **Contrato:** o kit manda varredura ampla ao batedor em Opus, que roda comando de consulta pronto e nao escreve na arvore; leitura pontual quem precisa faz direto; projecao em ~/.claude e ato do dono (materializar.py apply nao rodado)
  - **Não refazer:** nada a declarar
  - **Pendente:** projecao global em ~/.claude e propagacao aos derivados, fora do escopo

### AF-T20 — `uow.py` sai do kit [Sonnet · esforço low · classe mecanica]
- **Objetivo:** Quem executa retira do kit o instrumento de unidade de trabalho, que nada cita e nenhum teste cobre.
- **Fundamento:** `DAF-5`, `DAF-7`, `DAF-36`, `F-7`, `F-33`. **Espera o veredito do dono no Marco 1** (card nasce `blocked` razão `dependencia`). Opções registradas: sair do kit, recomendada e escrita neste card; ou o arquivo do executor passa a citá-lo e o exit de erro vira 1. Veredito na segunda → rodada de replanejamento, card corretivo `AF-T20a` da `OP-20`.
- **Depende de:** `AF-T10`
- **Operação do modelo:** `OP-20`
  - OP-20: Quem executa retira do kit o instrumento de unidade de trabalho, que nada cita e nenhum teste cobre.
  - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; escolha do dono no primeiro marco — Ninguém altera: o dono as dá no primeiro marco, e a operação que depende de cada uma espera por ela.
- **Camada e fronteira:** instrumentos do kit em `.claude/tools/`; nenhuma configuração do harness.
- **Arquivos-alvo:**
  - `.claude/tools/uow.py`
  - `.claude/tools/backlog.py`
- **Passos:**
  1. Apagar `.claude/tools/uow.py`.
  2. Na docstring de `.claude/tools/backlog.py`, o trecho depois de `antigo:` vira o trecho depois de `novo:` (sem quebra nova e sem refluxo; os rótulos não entram no arquivo):

     ```text
     antigo: mesmo desenho de `uow.py`/`telemetria.py`
     novo: mesmo desenho de `telemetria.py`
     ```
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste de `uow.py` existe; o total não muda).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0; `python .claude/checks/dead_code.py` sai 0.
  - Só os `Arquivos-alvo` se editam ou se apagam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não editar `.claude/settings.json` (a linha de diretório adicional das cópias de `uow` fica para o dono, `F-33`); não apagar teste nenhum; não tocar `.claude/projecoes.json`.
- **Contingências:**
  - se `python -m pytest -q` ou `kit_check` citar `uow` numa falha → parar e sinalizar `blocked` razão `premissa`, colando a linha.
- **Testes:** nenhum teste novo; a suíte inteira como trava.
- **Verificação:**
  1. `python -c "from pathlib import Path;print(Path('.claude/tools/uow.py').exists())"` → `False` — antes `True`, depois `False` (esperado, não ensaiado)
  2. `python -c "from pathlib import Path;print(Path('.claude/tools/backlog.py').read_text(encoding='utf-8').count('uow.py'))"` → `0` — antes `1`, depois `0` (esperado, não ensaiado)
  3. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
  4. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
- **Pronto quando:**
  - instrumento de unidade de trabalho.presença no kit — fora do kit — Verificações 1 e 2
- **Fora do escopo desta tarefa:** a linha de `.claude/settings.json` com o diretório de cópias de `uow` (configuração de quem opera a máquina; ato do dono).
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** .claude/tools/uow.py apagado; docstring de .claude/tools/backlog.py:38 cita só telemetria.py
  - **Contrato:** uow.py não existe mais no kit; nenhum instrumento nem teste o cita
  - **Não refazer:** nada a declarar
  - **Pendente:** linha de .claude/settings.json:19 com o diretório de cópias de uow — ato do dono, fora do card

### AF-T21 — A auto-auditoria do planejador se dosa pela classe do plano [Opus · esforço medium · classe redacao]
- **Objetivo:** O planejador passa a dosar a própria auto-auditoria pela classe do plano, declarada no cabeçalho dele.
- **Fundamento:** `DAF-5`, `DAF-8`, `DAF-29`, `F-15`. **Espera o veredito do dono no Marco 1** (card nasce `blocked` razão `dependencia`). Opções registradas: classe do plano no cabeçalho e tabela item × classe, recomendada e escrita neste card; ou protocolo inalterado. Veredito na segunda → rodada de replanejamento, card corretivo `AF-T21a` da `OP-21` (que cancela esta).
- **Depende de:** `AF-T19`
- **Operação do modelo:** `OP-21`
  - OP-21: O planejador passa a dosar a própria auto-auditoria pela classe do plano, declarada no cabeçalho dele.
  - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; planejador — Quem implementa recebe o roteiro de fases do agente e muda só a fase que a recomendação aponta, deixando as demais como estão.; escolha do dono no primeiro marco — Ninguém altera: o dono as dá no primeiro marco, e a operação que depende de cada uma espera por ela.
- **Camada e fronteira:** texto de doutrina: o esqueleto da Fase 3a e a abertura da Fase 4 do arquivo do agente planejador (corpo, não o frontmatter).
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md`
- **Passos:**
  1. Fase 3a, no bloco do esqueleto, o trecho depois de `antigo:` vira o trecho depois de `novo:` (sem quebra nova e sem refluxo; os rótulos não entram no arquivo):

     ```text
     antigo: (cabeçalho: data de origem, iniciativa, plano de origem se derivado)
     novo: (cabeçalho: data de origem, iniciativa, plano de origem se derivado, classe do plano)
     ```
  2. Fase 4, inserir entre a linha `### Fase 4 — Auto-auditoria (antes de gravar, uma passada)` e o item `1.` o bloco abaixo, com uma linha vazia antes e depois (as quebras são as do bloco; o recuo de dois espaços não entra no arquivo):

     ```text
       **Profundidade pela classe do plano.** O cabeçalho do plano declara `**Classe do plano:**` com um
       de três valores: `ferramentaria` (o produto é instrumento do kit — código, teste, fixture),
       `doutrina` (o produto é texto normativo — agente, skill, `GOVERNANCA.md`, rubrica) ou `produto`
       (o produto é código do projeto consumidor). A passada aplica os itens pela tabela; item que a
       tabela dispensa não se aplica, e a razão é a própria classe.

       | itens | ferramentaria | doutrina | produto |
       |---|---|---|---|
       | 1 a 6 e 8 a 12 | aplicam | aplicam | aplicam |
       | 7 (parser frio) e 13 (segunda leva) | só com gramática ou tabela normativa no plano | só com gramática ou tabela normativa no plano | aplicam |
       | 14 (ensaio em cópia) | só com arquivo compartilhado tocado por dois cards | só com arquivo compartilhado tocado por dois cards | aplica |
     ```
- **Restrições desta tarefa:**
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0 (o frontmatter do agente não muda).
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo).
  - Só o `Arquivos-alvo` se edita; nada fora dele se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não mudar o texto dos itens 1 a 14 da Fase 4; não tocar a Fase 1 (é da `AF-T19`); não escrever a classe no cabeçalho de plano nenhum.
- **Contingências:**
  - se o trecho `antigo:` do passo 1 não existir verbatim → parar e sinalizar `blocked` razão `premissa`.
- **Testes:** nenhum teste novo; a suíte inteira como trava.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print(t.count('Profundidade pela classe do plano'),t.count('plano de origem se derivado, classe do plano)'))"` → `1 1` — antes `0 0`, depois `1 1` (esperado, não ensaiado)
  2. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
  3. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)
- **Pronto quando:**
  - planejador.profundidade da auto-auditoria — proporcional à classe do plano declarada no cabeçalho — Verificação 1
- **Fora do escopo desta tarefa:** a medida de tokens do planejador por classe na série (`§7`).
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** pantonic-planner.md: esqueleto da Fase 3a declara a classe do plano no cabeçalho (:189); Fase 4 abre com 'Profundidade pela classe do plano' e a tabela item × classe (:238)
  - **Contrato:** a auto-auditoria do planejador se dosa pela classe declarada no cabeçalho do plano
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum


## 6. Ordem de execução

Ordem linear por item; o id `AF-T<n>` de cada item é o da operação da §1 que o materializa, fixado na
Fase 3b: o `#` da tabela é o `<n>` do card. Itens do mesmo arquivo em série, na ordem abaixo; o campo
`Depende de` de cada card carrega essas arestas (a `AF-T20` depende também da `AF-T10`, porque edita a
docstring de `backlog.py`, F-33).

| # | item | arquivo que o prende à posição |
|---|---|---|
| 1 | `TK-94a` | `.claude/tools/review_evidence.py` |
| 2 | `TK-95a` (depois de 1) | `.claude/tools/review_evidence.py` |
| 3 | `R-06` | `.claude/tools/progresso_hook.py` |
| 4 | `R-07` | `.claude/tools/encerrar.py` |
| 5 | `R-09` (depois de 4) | `.claude/tools/telemetria_hook.py`, `.claude/tools/encerrar.py` |
| 6 | `R-14` (depois de 3 e 5) | `.claude/tools/progresso_hook.py`, `.claude/tools/encerrar.py`, `.claude/skills/scrum-master/SKILL.md` |
| 7 | `R-13` | `.claude/tools/card_check.py` |
| 8 | `R-04` | `.claude/tools/backlog.py`, `.claude/agents/pantonic-planner.md` |
| 9 | `R-05` (depois de 8) | `.claude/tools/backlog.py` |
| 10 | `R-15` (depois de 6, 7 e 9) | `.claude/tools/backlog.py`, `.claude/skills/scrum-master/SKILL.md` |
| 11 | `R-12` (depois de 10) | `.claude/skills/scrum-master/SKILL.md` |
| 12 | `R-08` (depois de 6) | `.claude/tools/encerrar.py` |
| 13 | `R-17` (depois de 12) | `.claude/tools/encerrar.py` |
| 14 | `R-16` | `.claude/tools/modelo.py` |
| 15 | `R-01` | `tests/` |
| 16 | `R-18` | `.claude/checks/check-readme.ps1`, `.claude/checks/kit_check.ps1` |
| 17 | `R-10` (depois de 8) | `.claude/agents/pantonic-planner.md` |
| 18 | revisão do `README.md` (depois de 1..17) | `README.md` |
| 19 | `R-02` — `cancelled` na rodada de replanejamento de 2026-09-27 (`DAF-46`); segue pela `19a` | `.claude/agents/pantonic-planner.md` |
| 19a | `R-02`, card corretivo `AF-T19a` (depois de 21) | `.claude/agents/pantonic-scout.md`, `.claude/global/agents/context-scout.md`, `GOVERNANCA.md`, `README.md` e as residências que mandam a coleta ao modelo barato |
| 20 | `R-03` — `blocked` até o veredito do Marco 1 | `.claude/tools/uow.py` |
| 21 | `R-11` — `blocked` até o veredito do Marco 1 (depois de 19) | `.claude/agents/pantonic-planner.md` |

## 7. Fora de escopo (explícito)

- Revisão da doutrina pendente (F-27): ato do dono, residência `GOVERNANCA.md` §7.1.
- Registros do relatório sem recomendação: 8 (custo do scout), 9 (plano em pasta nunca rodado fora de
  fixture), 24 (prefixo redundante no nome do arquivo de medida), 30 (histórico do RDO — resolvido
  pela `R-06`), 41 (declaração de WIP — resolvido pelo `TK-95a`), 56 (gancho de crença de formas
  fechadas), 57 (ocupação não medida).
- A medida de tokens do planejador por classe de plano (`DAF-8`): lê-se na série `docs/telemetria.tsv`
  em planos futuros, não em card deste plano.
- Propagação das mudanças aos projetos derivados do kit: plano próprio de propagação.
- Reabrir `TK-94`/`TK-95` no diário (`DAF-3`).
- Commitar o relatório de auditoria (F-2): ato de quem conduz, antes do primeiro despacho.
- A linha de `.claude/settings.json` com o diretório adicional das cópias de `uow` (F-33): configuração do
  harness (`I-6`), ato do dono se a `AF-T20` fechar.

## 8. Riscos

| risco | resposta pré-decidida |
|---|---|
| O relatório (não rastreado, F-2) some ou muda | nenhum card o lê: a §2 e os cards carregam os fatos inline; o card segue |
| O WIP de 59 arquivos (F-26) polui a evidência antes de o `TK-94a` fechar | o `TK-94a` é o primeiro item; até ele fechar, o revisor reconcilia pelo passo 3a |
| O dono escolhe, no Marco 1, a rota não recomendada da `R-02`, da `R-03` ou da `R-11` | o card fica `blocked`; a rodada de replanejamento (rota `planejador` do consultor) escreve o card corretivo `T<n>a` da mesma operação (`DAF-5`) |
| `card_check` recusa a marca `(esperado, não ensaiado)` (`DAF-4`) | a Fase 3b mede antes de publicar; recusa → a marca sai da linha de `Verificação` e vai ao `Fundamento` do card |
| Card que altera um gancho (`progresso_hook.py`, `telemetria_hook.py`) quebra o painel ou a telemetria da janela | os TF do gancho rodam antes da linha de retorno; teste existente do gancho que cair → `blocked` razão `premissa` |
| O total da suíte muda entre despachos | piso relacional (I-1) |
| Card encontra o arquivo-alvo com a alteração não commitada do card anterior do mesmo arquivo | segue sobre ela; a evidência recorta pelo `--desde` |

## 9. Achados da execução
- **AE-3** (`AF-T1`, fechamento, 2026-09-27) — AF-T1, secao Testes: o TR test_tr_diff_stat_desde_sem_tocados_sai_sem_diferencas nao discrimina a guarda 'com tocados vazio o git diff nao roda sem caminho' (sem a guarda, git diff --stat <ref> <arvore> tambem sai vazio no cenario); o caso que diverge (arvore difere de <ref> com tocados vazio) ficou fora do card, criterio (ix) da RUBRICA §8. Implementacao honra a guarda por inspecao (laudo do revisor). **Rota:** corrigido no ato, por ordem do dono (2026-09-28): TR `test_tr_diff_stat_desde_tocados_vazio_com_arvore_diferente_nao_resume_a_arvore` (árvore difere de `<ref>`, tocados vazio) — passa com a guarda, cai sem ela (medido removendo a guarda e restaurando); no piso.
- **AE-4** (`AF-T5`, fechamento, 2026-09-27) — achado de processo (dossiê): docs/ACIONAMENTOS_CONSULTOR.tsv, escrito pelo consultor na triagem do blocked desta tarefa, sai no dossie de evidencia como fora dos alvos e sem atribuicao: o review_evidence.py nao reconhece o registro do consultor como registro da conducao, e o escopo so fechou pela declaracao de desvio da orquestracao. **Rota:** auditoria final — diretiva do dono de 2026-09-26: nenhum card nem tiquete novo por ajuste (rota do laudo: item de replanejamento do P-0753 na operacao do dossie de evidencia). **Corrigido no ato, por ordem do dono (2026-09-28):** `docs/ACIONAMENTOS_CONSULTOR.tsv` entra em `_REGISTRO_ORQUESTRACAO` (`.claude/tools/review_evidence.py`); TR `test_tr_acionamentos_do_consultor_sai_como_registro_da_orquestracao` (vermelho antes, verde depois), no piso. Fecha também as reincidências `AE-6`, `AE-9`, `AE-15` e `AE-28`.
- **AE-5** (`AF-T5`, fechamento, 2026-09-27) — achado de processo (doutrina): O exercicio ponta a ponta do revisor (passo 3b) sobre telemetria_hook.processar sem tsv_path grava na docs/telemetria.tsv real, porque o CLI telemetria.py append cai no default do repositorio: nesta revisao, 8 linhas de fixture entraram na serie real e foram removidas byte a byte, com a serie de volta ao estado do dossie de evidencia (2 linhas desde c0a8e22). A definicao do revisor manda executar em leitura e nao avisa que instrumento com destino default na serie real precisa de destino explicito. **Rota:** auditoria final — diretiva do dono de 2026-09-26: nenhum card nem tiquete novo por ajuste (rota do laudo: tiquete de emenda ao passo 3b de .claude/agents/pantonic-reviewer.md). **Corrigido no ato, por ordem do dono (2026-09-28), na causa e não no aviso:** `telemetria_hook.processar` passa sempre `--file` explícito, a série do repositório do estado (`_tsv_para_contagem`, a mesma de onde a contagem do consultor lê), nunca o default do CLI; TR `test_tr_processar_sem_tsv_path_grava_na_serie_do_repo_do_estado` — no vermelho, a linha de sonda vazou para a série real (removida byte a byte); verde depois, série real intacta sob a suíte inteira. No piso.
- **AE-6** (`AF-T6`, fechamento, 2026-09-27) — achado de processo (dossiê): review_evidence.py marca docs/ACIONAMENTOS_CONSULTOR.tsv (escrito pelo consultor na triagem desta tarefa) como fora dos alvos e sem atribuicao, em vez de registro da orquestracao; reconciliado pela declaracao de desvio do despacho, escopo da entrega = os 4 alvos; rota: AE-4 ja registrado **Rota:** sem ação — reincidência do AE-4, já roteado à auditoria final
- **AE-7** (`AF-T7`, fechamento, 2026-09-27) — achado de processo (modelo): OP-7 diz que a conferencia le a situacao no estado do plano em pasta 'quando o card nao a declara'; a entrega (fiel ao Contratos/classes do card) le estado.tsv incondicionalmente em plano em pasta e nunca consulta o bullet '- **Status:**' do card - medido em copia temporaria: card com Status done + estado.tsv ready compara 'antes'; card com Status done sem estado.tsv imprime 'status ausente: comparando antes'. **Rota:** dossie Ato de modelo de conflito devolvido com este laudo, despacho ao pantonic-model-designer por quem conduz a sessao
- **AE-8** (`AF-T7`, fechamento, 2026-09-27) — achado de processo (dossiê): AF-T7: o Objetivo repete a clausula condicional 'quando o card nao a declara' enquanto Contratos/classes prescreve leitura incondicional de estado.tsv, e nenhuma Verificacao nem teste discrimina o caso de card que declara Status em plano em pasta. **Rota:** item de replanejamento do P-0753 na auditoria final (diretiva do dono de 2026-09-26), junto com a resolucao do conflito de OP-7
- **AE-9** (`AF-T7`, fechamento, 2026-09-27) — achado de processo (dossiê): docs/ACIONAMENTOS_CONSULTOR.tsv, escrito pelo consultor na triagem do blocked desta tarefa, sai no dossie de evidencia como fora dos alvos e sem atribuicao; reconciliado pela declaracao de desvio do despacho, escopo da entrega = os 4 alvos. **Rota:** sem acao - reincidencia do AE-4, ja roteado a auditoria final
- **AE-10** (`AF-T8`, fechamento, 2026-09-27) — achado de processo (dossiê): A Verificação e o par TF/TR do AF-T8 só discriminam a transição 'linha de tarefa entra no estado.tsv'; nenhuma linha exercita a cláusula 'plano em pasta' do Domínio, e por isso a perda de C-10 para plano legado blocked passou verde. Rota proposta pelo laudo: item de replanejamento do P-0753 — card corretivo que estreita o predicado ao plano em pasta e acrescenta TR com plano legado blocked, id = contador, fora do inbox (deve sair 1 com C-10). **Rota:** corrigido no ato pelo consultor (`DAF-40`, regra `A8`; sem card novo, diretiva do dono de 2026-09-26) — predicado estreitado ao plano em pasta e TR `test_tr_check_plano_legado_blocked_no_contador_segue_acusando_c10`; suíte `473 passed`. Fechado.
- **AE-11** (`AF-T9`, fechamento, 2026-09-27) — achado de processo (dossiê): Decisão que o card não fechou: o Contratos/classes manda o bloco _bloco_achados passar por _truncar sem fixar o ponteiro; a entrega usou a faixa inteira do plano (show BKL-T10a sai com '… truncado (docs/plans/P-0739-backlog-instrumento.md:1-5515)'), que não localiza a seção de achados nem o ponto de corte que a frase nova da passagem-de-bastao promete ('ponteiro arquivo:l1-l2 de onde cortou'). **Rota:** auditoria final — diretiva do dono de 2026-09-26: nenhum card nem tiquete novo por ajuste (rota do laudo: item de replanejamento do P-0753 — fixar o ponteiro do bloco de achados no card AF-T10). **Corrigido no ato, por ordem do dono (2026-09-28):** `_achados_truncados` (`.claude/tools/backlog.py`), usada pelo `show` e pelo `next`, aponta o corte para a seção `## Achados da execução` (`show BKL-T10a` passa de `P-0739-backlog-instrumento.md:1-5515` a `:3196-5515`); TR `test_tr_show_achados_truncados_apontam_a_secao_de_achados` (vermelho antes, `:1-142` contra `:11-142`; verde depois), no piso.
- **AE-12** (`AF-T9`, fechamento, 2026-09-27) — achado de processo (dossiê): Ambiguidade do campo Testes: 'plano temporário com um card de 150 linhas' não diz se o plano é arquivo parseado ou Modelo em memória; a entrega montou Item/Plano/Modelo em memória (tmp_path fica sem uso), e o TF não exercita o parser até renderizar_next/show. O reviewer exercitou a CLI em plano real (show AF-T9, show BKL-T10a, next, show P-0753: card inteiro, notas e achados com teto, plano truncado, árvore inalterada). **Rota:** auditoria final — diretiva do dono de 2026-09-26: nenhum card nem tiquete novo por ajuste (rota do laudo: item de replanejamento do P-0753 — autoria de TF de verbo de CLI nomeia a camada exercitada). **Corrigido no ato, por ordem do dono (2026-09-28):** TF `test_tf_card_inteiro_pela_cli_sobre_plano_em_arquivo` — plano em pasta gravado em disco, `main(["show", ...])` e `main(["next", ...])` entregam o card de 150 linhas inteiro, e o card seguinte não vaza para o `show`.
- **AE-13** (`AF-T10`, fechamento, 2026-09-27) — achado de processo (dossiê): Decisao que o card nao fechou (G-NOASK): 'Contratos/classes' manda '--plano <plano>' sem dizer se relativo ou absoluto; a entrega escolheu caminho absoluto (repo / pai.arquivo) porque card_check.verificar_tarefa usa Path(plano) sem juntar --root. Escolha correta e declarada em comentario no alvo; rota: item de replanejamento do P-0753 na operacao do despacho, para o card fixar a forma do argumento. **Rota:** auditoria final — diretiva do dono de 2026-09-26: nenhum card nem tiquete novo por ajuste (rota do laudo: item de replanejamento do P-0753 na operacao do despacho, para o card fixar a forma do argumento)
- **AE-14** (`AF-T10`, fechamento, 2026-09-27) — achado de processo (dossiê): Contratos/classes fixou 'a razao e a ultima linha do stderr' sem fixar a decodificacao do stderr dos irmaos (que escrevem UTF-8), e o TR so afere o prefixo 'despachar: recusado — card_check:' - nenhuma linha de Verificacao nem de Testes discrimina o texto da razao, e a mojibake passou verde. **Rota:** corrigido no ato pelo consultor (`DAF-42`, regra `A8`; sem card novo, diretiva do dono de 2026-09-26) — `encoding="utf-8", errors="replace"` nos quatro `subprocess.run` de `despachar` e assert `"não fecham" in erro` no TR `test_tr_despachar_recusa_no_primeiro_gate_sem_escrever` (cai sem o reparo, passa com ele); suíte `478 passed`. Fechado. (rota do laudo: item de replanejamento do P-0753 na operação do despacho, `OP-10`, na auditoria final)
- **AE-15** (`AF-T10`, fechamento, 2026-09-27) — achado de processo (dossiê): docs/ACIONAMENTOS_CONSULTOR.tsv, escrito pelo consultor na triagem do blocked desta tarefa, sai no dossie de evidencia como fora dos alvos e sem atribuicao; reconciliado pela declaracao de desvio da orquestracao, escopo da entrega = os 3 alvos. **Rota:** sem acao - reincidencia do AE-4, ja roteado a auditoria final.
- **AE-16** (`AF-T11`, fechamento, 2026-09-27) — achado de processo (dossiê): a linha nova do item 1 do pantonic-consultant ('le so as tres entradas e, da doutrina, so a secao que o cenario aponta') nao ressalva as leituras que os itens 3 e 5 do mesmo agente exigem fora do cenario (Fase 4 itens 11-13 do pantonic-planner, rdo.py/review_evidence.py/backlog.py antes de mudar gramatica de card, .gitignore, GOVERNANCA 3.3 para causa_raiz); texto prescrito verbatim pelo card, entregue fiel; rota: item de replanejamento do P-0753 - o consultor/planejador emenda o item 1 com a excecao das leituras que a propria doutrina do agente manda **Rota:** auditoria final — diretiva do dono de 2026-09-26: nenhum card nem tiquete novo por ajuste (rota do laudo: item de replanejamento do P-0753 — emendar o item 1 do consultor com a exceção das leituras que a doutrina dele manda). **Corrigido no ato, por ordem do dono (2026-09-28):** o item 1 de `.claude/agents/pantonic-consultant.md` ressalva as leituras que os itens 3 e 5 mandam (itens 11-13 da Fase 4 do planejador, `GOVERNANCA.md` §3.2, parser antes de mudar gramática, `.gitignore`, fontes da classificação), só no trecho que o reparo usa.
- **AE-17** (`AF-T12`, fechamento, 2026-09-27) — achado de processo (dossiê): AF-T12: o card nao traz aceite de coerencia do modulo (rubrica §8 (iv) e (xvii)). Nenhuma verificacao exercita a forma que o verbo emite (pipe escapado na celula) numa segunda gravacao, nem a recusa da transicao de status depois das escritas (1) e (2); por isso os dois defeitos do motivo passaram com a verificacao verde. **Rota:** sanado pelo consultor no `DAF-43`, sem `AF-T12a` (diretiva do dono veda card novo por ajuste): os dois defeitos corrigidos no ato em `.claude/tools/encerrar.py` e um TR por caminho em `tests/test_encerrar.py` (`test_tr_marco_regravar_celula_com_pipe_escapado_nao_deixa_resto`, `test_tr_marco_go_com_transicao_recusada_nao_escreve`), ambos vermelhos antes do reparo
- **AE-18** (`AF-T12`, fechamento, 2026-09-27) — achado de processo (dossiê): AF-T12: o card prescreve _backlog.transacionar_status como escrita (3), que faz checagens proprias, e exige ao mesmo tempo 'todas as checagens antes da primeira escrita' sem dizer como conciliar (ex.: chamar checar_transicao antes da escrita (1)). Tambem ficaram sem fechamento: a forma de <plano> no dossie (a entrega usou caminho relativo ao repo), o strip() da frase e duas recusas a mais (plano sem id no nome; plano fora do backlog). **Rota:** a conciliação sanada no `DAF-43` (`checar_transicao` roda antes da escrita (1)); o resto — forma de `<plano>` no dossiê, `strip()` da frase, as duas recusas a mais — não é erro (entrega coerente com o contrato, lacuna de autoria do card): auditoria final
- **AE-19** (`AF-T13`, fechamento, 2026-09-27) — achado de processo (dossiê): AF-T13: o contrato do --checar não tem poder discriminante para seção ausente — 'nao citados' conta o ID em crase em qualquer lugar do documento e a tabela do arco que o próprio esqueleto gera já cita toda tarefa, e 'sem os quatro blocos' só itera seções existentes; medido em cópia do P-0753: seção inteira de AF-T1 apagada, --checar sai 0 com 'nenhum'/'nenhum', enquanto o item 6 da skill promete 'toda seção de tarefa com os quatro blocos'. **Rota:** corrigido no ato pelo consultor (`DAF-44`, regra `A8`; sem `AF-T13a`, diretiva do dono de 2026-09-26) — linha `sem seção: <ids>` no `--checar` (tarefa não `cancelled` sem `` ## `<ID>` — ``), exit `1` quando não vazia; TR `test_tr_esqueleto_de_operacoes_checar_secao_apagada` apaga a seção inteira (vermelho antes do reparo, verde depois); skill `entrega-de-encerramento` item 6 atualizada; suíte `488 passed`. Fechado. (rota do laudo: card de replanejamento do P-0753)
- **AE-20** (`AF-T14`, fechamento, 2026-09-27) — achado de processo (dossiê): Restrição do AF-T14 justifica 'modelo.py check sobre o P-0753 sai 0' com '(o plano não tem ## 1A)', fato falso desde a versão 2 pendente gravada pelo modelador após a AF-T7 (plano.md:173); a restrição segue verdadeira (exit 0 re-medido, agora exercitando o caminho pendente sobre plano real). **Rota:** auditoria final — diretiva do dono de 2026-09-26: nenhum card nem tiquete novo por ajuste (rota do laudo: sem ação sobre a entrega; item de replanejamento do P-0753 — restrição que cita estado do plano re-confere o parêntese quando o modelador grava versão pendente)
- **AE-21** (`AF-T14`, fechamento, 2026-09-27) — achado de processo (dossiê): O dossiê de evidência truncou o diff de modelo.py em 4000 caracteres antes da linha que materializa o Passo 2 (_diff_objetos, contrato); a leitura exigiu abrir o repositório. **Rota:** sem ação — teto conhecido do instrumento; registrado para o agregado. · **Desfecho (P-0754, AUF-T14, 2026-09-28):** encerrado sem mudança no kit — o teto de 4000 caracteres do trecho é conhecido do instrumento e sai marcado na evidência, como o laudo da `AF-T14` registrou.
- **AE-22** (`AF-T16`, fechamento, 2026-09-27) — achado de processo (dossiê): AF-T16: as quatro linhas de Verificação saíram 'esperado, não ensaiado' (RUBRICA §8 xii-b) e a única linha comportamental exercita só o check-readme; o kit_check só emite acento em caminho de falha, sem linha que o discrimine (xvii). A revisão mediu os dois mundos: check-readme antes True/depois False; kit_check check-drift com -KitRoot vazio sai 1 com 'não' íntegro e 0 U+FFFD. **Rota:** auditoria final — diretiva do dono de 2026-09-26: nenhum card nem tiquete novo por ajuste (rota do laudo: item de replanejamento do P-0753 — autoria de Verificação com o valor antes ensaiado no ato). · **Desfecho (P-0754, AUF-T14, 2026-09-28):** encerrado sem mudança no kit — a regra já existe: o ensaio dos cards em cópia, item 14 da Fase 4 de `.claude/agents/pantonic-planner.md`, e o critério (xii)(b) de `docs/RUBRICA_DE_REVISAO.md`.
- **AE-23** (`AF-T17`, fechamento, 2026-09-27) — achado de processo (dossiê): Contrato diz 'na ordem da primeira aparicao', mas o TF do proprio card lista o caminho antes do simbolo que aparece primeiro no texto; a entrega decidiu 'ordem por categoria (caminhos, simbolos, flags)' e declarou no docstring. Decisao que o card nao fechou (G-NOASK). **Rota:** auditoria final — diretiva do dono de 2026-09-26: nenhum card nem tiquete novo por ajuste (rota do laudo: item de replanejamento do P-0753 — fixar a ordem por categoria no Contratos/classes). **Fechado por decisão do dono (2026-09-28), na recomendação:** a ordem por categoria (caminhos, símbolos, flags; cada uma na ordem da primeira aparição) é o contrato vigente — já declarado na docstring de `.claude/tools/prevoo.py` e travado pelo TF do card; nenhum texto vivo diz outra coisa (README e Fase 0 do planejador conferidos). A divergência ficou só no texto do card fechado.
- **AE-24** (`AF-T17`, fechamento, 2026-09-27) — achado de processo (dossiê): A contingencia do card manda apensar linha a tests/piso_comportamental.txt, arquivo fora dos Arquivos-alvo e contra a Restricao 'so os Arquivos-alvo se editam'; o dossie de evidencia marcou o arquivo como alheio sem atribuicao. A entrega apensou exatamente uma linha (o TR novo, forma '<nodeid> - <frase>'), escopo conforme. **Rota:** auditoria final — diretiva do dono de 2026-09-26: nenhum card nem tiquete novo por ajuste (rota do laudo: item de replanejamento do P-0753 — contingência que escreve em arquivo o lista em Arquivos-alvo como condicional)
- **AE-25** (`AF-T17`, fechamento, 2026-09-27) — achado de processo (dossiê): Contrato do AF-T17 nao define 'token': a entrega escolheu str.split() sem remover crase, virgula, ponto, ponto-e-virgula nem parenteses, e nenhuma linha de Testes/Verificacao traz citacao em crase ou pontuada (criterio (xvii)/(ix) da §8: o aceite nao exercita a forma que o pedido real usa). **Rota:** corrigido no ato pelo consultor no `DAF-45` (acionamento 9, regra `A8`) — normalização do token no `prevoo.py` e três TRs, um por forma de citação; sem card novo (diretiva do dono de 2026-09-26). Fechado.
- **RP-1** (`AF-T19`, rodada de replanejamento, 2026-09-27) — classificação: estratégica na origem, técnica no fim. A rodada começou decidindo "o planejador mede o comando por um instrumento novo e o batedor só lê" e parou quando o dono derrubou a premissa, verbatim: *"Tudo isso começou com uma afirmação "o batedor não pode usar X ferramenta". Isso é absurdo. Por que ele não consuegue usar a ferramenta? Era a pergunta que deveria ser respondida ao invés de se tentar entortar todo o processo só para que o batedor tenha algo para fazer. E, se no final das contas, não valer a pena ter o batedor, se ele não trouxer ganhos reais ao processo, melhor que ele seja descartado"*. Resposta: o batedor não usava a ferramenta porque o frontmatter não a listava — configuração, não limite. A avaliação medida (F-36) e o ato do dono fecharam a `DAF-46`. Causa-raiz na autoria: a auditoria e a `DAF-6` trataram a lista de ferramentas de um agente como fato fixo e desenharam o processo em volta dela. Verificação que teria evitado: diante de "o papel X não consegue Y", perguntar primeiro se o impedimento é configuração do próprio kit; se for, a primeira rota avaliada é ajustar a configuração. Classe nova: a verificação entra na Fase 1 do planejador fora deste plano (auditoria final, diretiva do dono de 2026-09-26). **Rota:** absorvido pela `DAF-46` e pela `AF-T19a`.
- **AE-26** (`AF-T19a`, fechamento, 2026-09-27) — Ressalva de registro do laudo AF-T19a: redespacho so-verificacoes (DAF-47) nao gravou a medida do executor (card_check --mundo depois --gravar), e o verbo backlog.py despachar confere o card so no mundo antes - redespacho de tarefa ja aplicada tem de passar por card_check --mundo depois e status in-progress a mao **Rota:** corrigido no ato, por ordem do dono (2026-09-28): `backlog.py despachar <ID> --mundo depois` repassa o mundo ao `card_check` e reaproveita o `<ref>`; Passo 3 do `scrum-master` e `README.md` citam a opção; TR `test_tr_despachar_mundo_depois_redespacha_tarefa_ja_aplicada` (vermelho antes, verde depois), no piso. A medida do executor não gravada no redespacho foi falha de condução (o despacho não mandou gravar), não do instrumento.
- **AE-27** (`AF-T19a`, fechamento, 2026-09-27) — achado de processo (dossiê): contingencia do passo 13 (generate so podia mudar a linha do pantonic-scout) contradizia a restricao check-drift exit 0 e parou o segundo despacho em blocked premissa - parada correta da execucao, defeito do card. **Rota:** sem acao - ja fechado como item de replanejamento pela DAF-47 (contingencia reescrita e linha Estado de partida do redespacho)
- **AE-28** (`AF-T19a`, fechamento, 2026-09-27) — achado de processo (dossiê): docs/ACIONAMENTOS_CONSULTOR.tsv (acionamentos 10-12 do consultor sobre esta tarefa, untracked) sai no dossie de evidencia como fora dos alvos e sem atribuicao; reconciliado como registro da conducao, escopo da entrega = os 12 alvos. **Rota:** sem acao - reincidencia do AE-4, ja roteado a auditoria final
- **AE-29** (fechamento do plano, 2026-09-27) — `python .claude/tools/encerrar.py operacoes --plano docs/plans/P-0753-auditoria-estagio-1/plano.md` (caminho relativo, como a skill `entrega-de-encerramento` o escreve) sai exit 1 com `ValueError: 'docs\\plans\\P-0753-auditoria-estagio-1\\plano.md' is not in the subpath of 'D:\\workspaces\\PantonicApp'` (`caminho.relative_to(repo)` sobre caminho não resolvido); com o caminho absoluto grava o esqueleto. Nenhum teste de `tests/test_encerrar.py` passa `--plano` relativo. **Rota:** corrigido no ato, por ordem do dono (2026-09-28): `escrever_esqueleto_operacoes` e `checar_esqueleto_operacoes` resolvem `plano_path` e `repo` antes do parser; TR `test_tr_esqueleto_de_operacoes_plano_relativo` (vermelho medido antes, verde depois), apensado ao `tests/piso_comportamental.txt`; suíte `499 passed`.
