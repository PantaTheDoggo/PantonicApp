# P-0755 — Aplicação das recomendações da auditoria final do kit

**Data de origem:** 2026-09-28 · **Origem:** pedido do dono de 2026-09-28 em dois atos (transcritos na §0) ·
**Plano de origem:** `P-0754` (este plano nasce pela `DAU-1` daquele: aplicar as `R-n` do relatório novo fica
para plano sucessor; classificação de derivado, feita na Fase 5: nenhuma de A, B e C — é o sucessor que a `DAU-1`
prevê, e o `P-0754` segue como está, no Marco 3, com 16/16 tarefas `done`) · **Classe do plano:** ferramentaria ·
**Prefixo das tarefas no diário:** `RAF-T<n>` (lastro `tarefas: RAF-T<n>` para `OP-<n>`) ·
**Prefixo das decisões:** `DRF-<n>` · **Prefixo dos fatos:** `F-<n>` ·
**Checagem de versão do kit:** modo hub — congelada em `0.0.0` (`GOVERNANCA.md` §10), feita pela condução
antes do despacho do planejador · **Branch de trabalho:** `plan/planner-modelo-escopo` (HEAD `2513964`, com o
WIP não commitado do `P-0754`, do roteiro e da sonda) · **Estado:** linha `plano` de `estado.tsv`, nesta pasta.

**Marcos de validação pelo dono** (`DRF-5`):

| marco | o que o dono lê | veredito |
|---|---|---|
| **Marco 1** | `python .claude/tools/modelo.py show --plano docs/plans/P-0755-recomendacoes-auditoria-final/plano.md` (a §1 escrita pelo modelador) e a §3 deste plano | go · 2026-09-28 — "Marcar como aceito, e colocar o plano no topo da fila para próxima janela" |
| **Marco 2** | etapa A, custo da orquestração: `R-01`, `R-02`, `R-03`, `R-15`, `R-24` aplicadas | go · 2026-09-29 — "Aceitar, e pode continuar neste contexto" |
| **Marco 3** | etapa B, instrumentos de revisão e medida: `R-13`, `R-14`, `R-30`, `R-31`, `R-12`, `R-09`, `R-10`, `R-11`, `R-05`, `R-26`, `R-27` aplicadas | go · 2026-09-29 — "aceito" |
| **Marco 4** | etapa C, modelo × card × versão: `R-04`, `R-06`, `R-07`, `R-08` aplicadas | go · 2026-09-29 — "Aceitar" · consultor: "valido a versão 3: a diferença para a vigente é só o contrato de conferência do modelo e a linha versões julgadas da §1.3, que é a DRF-37 dentro da OP-19, já entregue na árvore sem escopo novo" |
| **Marco 5** | etapa D, backlog, fechamento e telemetria: `R-17`, `R-18`, `R-28`, `R-19`, `R-20`, `R-16` aplicadas | go · 2026-09-30 — "marcar como aceito o veredito vigente e continuar plano" · consultor: "valido a versão 4: a diferença para a vigente é só a propriedade e o contrato da rubrica de revisão, o precisa de e o altera da OP-30 e a linha nova alvo do achado de instrumento da §1.3, que é a DRF-68 já entregue na árvore pela RAF-T30a sem escopo novo" |
| **Marco 6** | etapa E, doutrina do planejador e comunicação: `R-21`, `R-22`, `R-23`, `R-25` aplicadas, o `README.md` revisado e a entrega do plano | pendente |

**Critério de pronto do plano:** o kit passa a ter aplicadas as recomendações `R-01`..`R-31` do relatório
`docs/audits/AUDITORIA_FINAL_KIT.md`, exceto a `R-29` (fica registrada sem ação, `DRF-3`). São cinco etapas,
A..E, na ordem do roteiro, validadas nos Marcos 2..6. Cada recomendação chega com seu instrumento, teste e
doutrina, e o plano fecha com o `README.md` revisado.

## 0. O problema, verbatim

Ato 1 do dono (2026-09-28):

> Leia o docs/audits/HANDOVER_AUDITORIA_FINAL_2026-09-28.md, faça double check dos achados, e elabore um plano de atuação. Continue com Fable no papel intelectual

Ato 2 do dono (2026-09-28), depois de ler o roteiro `docs/audits/ROTEIRO_PLANO_SUCESSOR_2026-09-28.md`, que a
condução produziu com quatro decisões recomendadas (D1..D4, na §3 como `DRF-1`..`DRF-4`):

> Aceito recomendações. Libere o plano assim que possíveç

(sic.)

Pré-voo do pedido (`python .claude/tools/prevoo.py "<ato 1>"`, exit 0):

```
citado | existe | onde
docs/audits/HANDOVER_AUDITORIA_FINAL_2026-09-28.md | sim | docs/audits/HANDOVER_AUDITORIA_FINAL_2026-09-28.md
docs/audits/ROTEIRO_PLANO_SUCESSOR_2026-09-28.md | sim | docs/audits/ROTEIRO_PLANO_SUCESSOR_2026-09-28.md
docs/audits/AUDITORIA_FINAL_KIT.md | sim | docs/audits/AUDITORIA_FINAL_KIT.md
```

**Marco 1, 2026-09-28 — veredito do dono (go):**

> Marcar como aceito, e colocar o plano no topo da fila para próxima janela

**Marco 2, 2026-09-29 — veredito do dono (go):**

> Aceitar, e pode continuar neste contexto

**Marco 3, 2026-09-29 — veredito do dono (go):**

> aceito

**Marco 4, 2026-09-29 — veredito do dono (go):**

> Aceitar

**Marco 5, 2026-09-30 — veredito do dono (go):**

> marcar como aceito o veredito vigente e continuar plano

## 1. Modelo conceitual

**Estado do modelo:** versão 4 · 2026-09-29 · autor: modelador · 40 operações · 62 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem | lastro na §0 ou no relatório | tipo |
|---|---|---|---|---|---|---|
| gerente do loop | a rotina de quem conduz a sessão, que despacha cada tarefa ao executor, recebe a revisão e fecha a tarefa | janela em que o loop abre, entrega do despacho ao executor, conferência das âncoras, rota do modelador com operação nova, falha de instrumento levada ao consultor, card entregue ao consultor, abertura da mensagem de marco | Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só. | OP-1 | §0, ato 2: *"Aceito recomendações"* · relatório R-01, R-02, R-03, R-04, R-16, R-20, R-25 | escopo |
| medidor de custo da sessão | um comando novo que lê a conversa gravada de uma sessão e diz quanto contexto cada turno reenviou | medida por turno, medida por passo e por tarefa | Quem implementa parte dos dois rascunhos da auditoria, sem mexer neles, e entrega um comando com teste que serve a tarefa de qualquer plano. | OP-2 | §0, ato 2: *"Aceito recomendações"* · relatório R-01 | escopo |
| despacho de tarefa | o comando que confere se uma tarefa pode começar e entrega ao executor o que ele precisa para fazê-la | lugar do card despachado, texto pronto ao executor, âncoras conferidas, versão do modelo julgada | Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor. | OP-3 | §0, ato 2: *"Aceito recomendações"* · relatório R-02, R-03, R-04 | escopo |
| gatilho do próximo passo | o aviso automático que, quando o dono pede o próximo passo, injeta na conversa o estado do backlog | mensagens que o disparam | Quem implementa faz o gatilho reconhecer quem escreveu a mensagem antes de procurar a frase, com testes próprios. | OP-5 | §0, ato 2: *"Aceito recomendações"* · relatório R-15 | escopo |
| filtro da saída dos testes | o atalho que encurta a saída dos testes para só as falhas e o resumo | código de saída devolvido | Quem implementa corrige o filtro na cópia que o kit guarda; levá-lo à máquina do dono é ato do próprio dono. | OP-6 | §0, ato 2: *"Aceito recomendações"* · relatório R-24 | escopo |
| dossiê de evidência | o que o revisor recebe mostrando o que a entrega mudou, para julgar cada tarefa | casos em que hoje quebra, marca do arquivo novo que não é texto, rótulo do registro da orquestração, curinga do alvo, caminho acentuado, linhas removidas dos testes | Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável. | OP-7 | §0, ato 2: *"Aceito recomendações"* · relatório R-12, R-13, R-14, R-30, R-31 | escopo |
| rubrica de revisão | a régua pela qual o revisor julga cada entrega | critério da asserção removida, alvo do achado de instrumento | Quem implementa acrescenta um critério à régua de testes, apoiado no que a evidência passa a mostrar, e faz a régua e o laudo aceitarem um quinto alvo de achado, o de instrumento, além dos quatro de hoje. | OP-12 | §0, ato 2: *"Aceito recomendações"* · relatório R-12, R-20 | escopo |
| conferência de verificação do card | o comando que roda a linha de verificação de um card e diz se o resultado bate com o que o card escreveu | resultado esperado no bloco cercado, literal com pontuação, comandos de leitura do versionador, recorte do despacho no comando, linha de invariância | Quem implementa amplia o que a conferência aceita sem deixar de ler os cards já escritos na forma antiga. | OP-13 | §0, ato 2: *"Aceito recomendações"* · relatório R-09, R-10, R-11 | escopo |
| medida gravada do card | o arquivo em que a conferência guarda o que mediu, e que o revisor lê ao julgar | pasta em que é gravada, momento no nome, leitura pelo revisor | Quem implementa muda onde e com que nome a medida se grava, e faz o revisor achar tanto a nova quanto as vinte já gravadas com o nome antigo. | OP-15 | §0, ato 2: *"Aceito recomendações"* · relatório R-05 | escopo |
| planejador | o agente que transforma o pedido do dono em plano e escreve os cards | árvore em que se mede o antes, card que deixa o alvo igual, medida gravada na rodada, card da operação nova, profundidade do planejamento, pedido ao modelador, checagem de versão registrada | Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão. | OP-16 | §0, ato 2: *"Aceito recomendações"* · relatório R-04, R-05, R-21, R-22, R-23, R-26, R-27 | escopo |
| conferência do modelo | o comando que confere a seção do modelo do plano e mostra ao dono o estágio e a diferença entre versões | versões julgadas, fidelidade do texto copiado no card, diferença entre versões | Quem implementa acrescenta à conferência o que cada operação pede e mantém o que ela já julga quando chamada como hoje, com uma só mudança: enquanto houver versão pendente, o card que cita uma operação que só ela tem deixa de ser recusado. | OP-19 | §0, ato 2: *"Aceito recomendações"* · relatório R-04, R-06, R-07 | escopo |
| fechamento | o comando que encerra uma tarefa revisada e grava o veredito de cada marco | promoção da versão aceita, validação do consultor, origem do achado registrado, aviso de falha de instrumento | Quem implementa recebe o comando que hoje só grava o veredito do marco e confere achados por semelhança de texto, e acrescenta o que a operação pede. | OP-23 | §0, ato 2: *"Aceito recomendações"* · relatório R-06, R-08, R-19, R-20 | escopo |
| modelador | o agente dono da seção do modelo em todo plano | papel na promoção de versão | Quem implementa troca a regra da promoção da versão aceita, que deixa de ser ato do modelador salvo no conflito. | OP-26 | §0, ato 2: *"Aceito recomendações"* · relatório R-08 | escopo |
| consultor | o agente que tria cada parada do loop e valida a versão pendente do modelo antes do dono | forma da validação da versão pendente, origem citada no achado | Quem implementa acrescenta à definição do agente as duas formas de linha que as operações pedem, sem mudar a triagem. | OP-26 | §0, ato 2: *"Aceito recomendações"* · relatório R-08, R-19 | escopo |
| pré-voo do pedido | a conferência que, antes de planejar, verifica se cada caminho que o pedido cita existe | o que conta como caminho, caminho a criar | Quem implementa muda só a leitura do que é caminho e a classificação do que falta, com os testes que a provam. | OP-27 | §0, ato 2: *"Aceito recomendações"* · relatório R-17 | escopo |
| controle do backlog | os comandos que conferem os planos e tiram da fila o plano encerrado | aviso de diretiva desatualizada, prefixo de decisão repetido | Quem implementa acrescenta um aviso ao tirar o plano da fila e uma recusa ao conferir, sem mudar o resultado do primeiro. | OP-28 | §0, ato 2: *"Aceito recomendações"* · relatório R-18, R-28 | escopo |
| série de telemetria | a tabela em que o kit registra, por agente, quanto cada tarefa consumiu | plano e tarefa atribuídos, linhas por agente | Quem implementa faz o registro ler o plano e a tarefa na primeira linha do despacho e ganhar uma coluna que identifica o agente, completando as linhas antigas. | OP-31 | §0, ato 2: *"Aceito recomendações"* · relatório R-16 | escopo |
| painel do gerente | a tela de progresso que acompanha o que o loop está fazendo | tarefa mostrada | Quem implementa faz o painel ler a mesma linha de abertura do despacho antes de recorrer à tarefa corrente. | OP-32 | §0, ato 2: *"Aceito recomendações"* · relatório R-16 | escopo |
| norma de consumo do kit | a regra da governança sobre como se mede e se atribui o consumo de cada agente | linha de abertura do despacho | Quem implementa escreve a regra num lugar só, e os demais textos apontam para ela. | OP-33 | §0, ato 2: *"Aceito recomendações"* · relatório R-16 | escopo |
| checagem de versão do kit | a rotina que confere se o projeto está na versão vigente do kit | momento em que roda | Quem implementa escreve na própria rotina que quem conduz a roda antes de despachar o planejador e passa o resultado no pedido. | OP-38 | §0, ato 2: *"Aceito recomendações"* · relatório R-23 | escopo |
| guia de entrada do kit | o documento que apresenta o kit a quem chega | aderência ao kit entregue | Quem implementa revisa o guia contra o kit como ele fica depois das cinco etapas, incluindo os dois comandos que ele ainda não cita. | OP-40 | §0, ato 2: *"Libere o plano"* · prompt do planejador: o plano fecha com o guia revisado | escopo |
| relatório da auditoria final | o relatório da auditoria que mediu o kit num loop real e num plano fictício, com trinta e uma recomendações, cada uma com origem, ação e verificação | recomendações | Ninguém altera: é a fonte do que cada operação faz e de como ela se prova. | externo | §0, ato 1: *"faça double check dos achados, e elabore um plano de atuação"* | externo |
| escolhas do dono sobre o roteiro | as quatro escolhas que o dono aceitou ao ler o roteiro deste plano: como a versão pendente convive com o despacho, a régua de profundidade do planejamento, a recomendação que fica sem ação e a ordem das cinco etapas | quatro escolhas aceitas | Ninguém altera: fixam a rota das operações que dependem delas. | externo | §0, ato 2: *"Aceito recomendações"* | externo |
| rascunhos de medição da auditoria | os dois pequenos programas que a auditoria usou para medir o custo da sessão, guardados como registro dela | registro da auditoria | Ninguém altera: são o ponto de partida do medidor novo e ficam como estão. | externo | §0, ato 1: *"faça double check dos achados"* · relatório R-01 | externo |
| casos registrados pela auditoria | os incidentes que a auditoria mediu no loop real e no plano fictício, cada um reproduzível numa montagem descartável | resposta do kit a cada caso | Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança. | externo | §0, ato 1: *"faça double check dos achados"* · relatório §5, a verificação de cada recomendação | medição |

### 1.2 Fluxo de operações

**A. Custo da orquestração**

- **OP-1** — Quem executa ensina o gerente do loop a abrir a execução de um plano recém-planejado numa janela nova, separada da que o planejou, com o plano gravado como único insumo.
  - `precisa de: relatório da auditoria final` · `altera: gerente do loop.janela em que o loop abre` · `tarefas: RAF-T1, RAF-T1a` · `lastro: §0, ato 2, Aceito recomendações; relatório R-01`
- **OP-2** — Quem executa cria o medidor de custo da sessão, que lê uma conversa gravada e reparte o contexto reenviado por turno, por passo do loop e por tarefa despachada.
  - `precisa de: relatório da auditoria final, rascunhos de medição da auditoria, gerente do loop` · `altera: medidor de custo da sessão.medida por turno, medidor de custo da sessão.medida por passo e por tarefa` · `tarefas: RAF-T2` · `lastro: §0, ato 2, Aceito recomendações; relatório R-01`
- **OP-3** — Quem executa faz o despacho de tarefa entregar ao executor, num arquivo próprio, o card com as âncoras já conferidas, deixando na tela de quem conduz só o texto pronto do despacho.
  - `precisa de: relatório da auditoria final, gerente do loop, casos registrados pela auditoria` · `altera: despacho de tarefa.lugar do card despachado, despacho de tarefa.texto pronto ao executor, despacho de tarefa.âncoras conferidas` · `tarefas: RAF-T3, RAF-T3a` · `lastro: §0, ato 2, Aceito recomendações; relatório R-02, R-03`
- **OP-4** — Quem executa ensina o gerente do loop a repassar ao executor o texto pronto do despacho, sem reconferir à mão as âncoras do card.
  - `precisa de: despacho de tarefa, gerente do loop` · `altera: gerente do loop.entrega do despacho ao executor, gerente do loop.conferência das âncoras` · `tarefas: RAF-T4, RAF-T4a` · `lastro: §0, ato 2, Aceito recomendações; relatório R-02, R-03`
- **OP-5** — Quem executa faz o gatilho do próximo passo responder só à mensagem do dono, sem reagir ao relato de subagente nem ao aviso do sistema.
  - `precisa de: relatório da auditoria final, gerente do loop, casos registrados pela auditoria` · `altera: gatilho do próximo passo.mensagens que o disparam` · `tarefas: RAF-T5` · `lastro: §0, ato 2, Aceito recomendações; relatório R-15`
- **OP-6** — Quem executa faz o filtro da saída dos testes devolver o código de saída dos próprios testes, mesmo quando o comando encadeia outros passos depois deles.
  - `precisa de: relatório da auditoria final, gerente do loop, casos registrados pela auditoria` · `altera: filtro da saída dos testes.código de saída devolvido` · `tarefas: RAF-T6, RAF-T6a` · `lastro: §0, ato 2, Aceito recomendações; relatório R-24`

**B. Instrumentos de revisão e medida**

- **OP-7** — Quem executa faz o dossiê de evidência chegar ao fim nos três casos em que hoje quebra: conteúdo antigo que não se lê como texto, módulo de apoio ausente e medida guardada em outra pasta.
  - `precisa de: relatório da auditoria final, despacho de tarefa, casos registrados pela auditoria` · `altera: dossiê de evidência.casos em que hoje quebra` · `tarefas: RAF-T7, RAF-T7a` · `lastro: §0, ato 2, Aceito recomendações; relatório R-13`
- **OP-8** — Quem executa acerta duas marcas do dossiê de evidência: a de arquivo novo, que passa a valer também para o que não é texto, e a do registro da orquestração, que passa a ter o mesmo nome na lista e no resumo.
  - `precisa de: dossiê de evidência, casos registrados pela auditoria` · `altera: dossiê de evidência.marca do arquivo novo que não é texto, dossiê de evidência.rótulo do registro da orquestração` · `tarefas: RAF-T8, RAF-T8a` · `lastro: §0, ato 2, Aceito recomendações; relatório R-14`
- **OP-9** — Quem executa faz o dossiê de evidência ler o curinga do alvo como a linha de comando o lê, com a estrela presa a uma pasta e a estrela dupla alcançando as subpastas.
  - `precisa de: dossiê de evidência, casos registrados pela auditoria` · `altera: dossiê de evidência.curinga do alvo` · `tarefas: RAF-T9, RAF-T9a` · `lastro: §0, ato 2, Aceito recomendações; relatório R-30`
- **OP-10** — Quem executa faz o dossiê de evidência receber inteiro o nome de arquivo acentuado que o versionador lista, em vez de dá-lo por ausente.
  - `precisa de: dossiê de evidência, casos registrados pela auditoria` · `altera: dossiê de evidência.caminho acentuado` · `tarefas: RAF-T10, RAF-T10a` · `lastro: §0, ato 2, Aceito recomendações; relatório R-31`
- **OP-11** — Quem executa faz o dossiê de evidência mostrar, para cada arquivo de teste entre os alvos do card, as linhas que a entrega removeu.
  - `precisa de: dossiê de evidência, casos registrados pela auditoria` · `altera: dossiê de evidência.linhas removidas dos testes` · `tarefas: RAF-T11, RAF-T11a` · `lastro: §0, ato 2, Aceito recomendações; relatório R-12`
- **OP-12** — Quem executa acrescenta à rubrica de revisão o critério que reprova a asserção de teste removida sem que o card mande removê-la.
  - `precisa de: relatório da auditoria final, dossiê de evidência` · `altera: rubrica de revisão.critério da asserção removida` · `tarefas: RAF-T12, RAF-T12a` · `lastro: §0, ato 2, Aceito recomendações; relatório R-12`
- **OP-13** — Quem executa faz a conferência de verificação do card comparar com o resultado que o card escreve, também no bloco cercado medido depois da entrega e no literal com pontuação.
  - `precisa de: relatório da auditoria final, gerente do loop, casos registrados pela auditoria` · `altera: conferência de verificação do card.resultado esperado no bloco cercado, conferência de verificação do card.literal com pontuação` · `tarefas: RAF-T13, RAF-T13a` · `lastro: §0, ato 2, Aceito recomendações; relatório R-09, R-10`
- **OP-14** — Quem executa faz a conferência de verificação do card rodar a leitura do versionador contra o recorte do despacho, inclusive a linha que prova que o alvo ficou igual.
  - `precisa de: conferência de verificação do card, despacho de tarefa, casos registrados pela auditoria` · `altera: conferência de verificação do card.comandos de leitura do versionador, conferência de verificação do card.recorte do despacho no comando, conferência de verificação do card.linha de invariância` · `tarefas: RAF-T14` · `lastro: §0, ato 2, Aceito recomendações; relatório R-11`
- **OP-15** — Quem executa faz a medida gravada do card ficar na pasta do plano da árvore medida, com o momento da medida no nome, onde o dossiê de evidência a encontra.
  - `precisa de: conferência de verificação do card, dossiê de evidência, casos registrados pela auditoria` · `altera: medida gravada do card.pasta em que é gravada, medida gravada do card.momento no nome, medida gravada do card.leitura pelo revisor` · `tarefas: RAF-T15` · `lastro: §0, ato 2, Aceito recomendações; relatório R-05`
- **OP-16** — Quem executa ensina o planejador a medir o antes do card que depende de outro na cópia de ensaio com os anteriores aplicados, declarando em que árvore mediu.
  - `precisa de: relatório da auditoria final, conferência de verificação do card, medida gravada do card` · `altera: planejador.árvore em que se mede o antes` · `tarefas: RAF-T16` · `lastro: §0, ato 2, Aceito recomendações; relatório R-26`
- **OP-17** — Quem executa ensina o planejador a discriminar o card cujo alvo deve ficar igual pela prova de que nada nele mudou desde o recorte do despacho.
  - `precisa de: planejador, conferência de verificação do card` · `altera: planejador.card que deixa o alvo igual` · `tarefas: RAF-T17` · `lastro: §0, ato 2, Aceito recomendações; relatório R-27`
- **OP-18** — Quem executa ensina o planejador a gravar, na rodada de replanejamento, a medida de antes e a de depois de cada card que ela reescreve.
  - `precisa de: planejador, medida gravada do card` · `altera: planejador.medida gravada na rodada` · `tarefas: RAF-T18` · `lastro: §0, ato 2, Aceito recomendações; relatório R-05`

**C. Modelo, card e versão**

- **OP-19** — Quem executa faz a conferência do modelo julgar só a versão vigente quando pedida assim, deixando a versão pendente para o marco.
  - `precisa de: escolhas do dono sobre o roteiro, despacho de tarefa, casos registrados pela auditoria` · `altera: conferência do modelo.versões julgadas` · `tarefas: RAF-T19, RAF-T19a` · `lastro: §0, ato 2, Aceito recomendações; relatório R-04`
- **OP-20** — Quem executa faz o despacho de tarefa pedir à conferência do modelo só o julgamento da versão vigente.
  - `precisa de: conferência do modelo, despacho de tarefa, casos registrados pela auditoria` · `altera: despacho de tarefa.versão do modelo julgada` · `tarefas: RAF-T20` · `lastro: §0, ato 2, Aceito recomendações; relatório R-04`
- **OP-21** — Quem executa faz a conferência do modelo recusar o card cujo texto copiado da operação difere do texto da versão que ele cita.
  - `precisa de: conferência do modelo, casos registrados pela auditoria` · `altera: conferência do modelo.fidelidade do texto copiado no card` · `tarefas: RAF-T21` · `lastro: §0, ato 2, Aceito recomendações; relatório R-06`
- **OP-22** — Quem executa faz a conferência do modelo mostrar, entre duas versões, a operação inserida, a renumerada e a propriedade que só uma delas tem.
  - `precisa de: conferência do modelo, casos registrados pela auditoria` · `altera: conferência do modelo.diferença entre versões` · `tarefas: RAF-T22, RAF-T22a` · `lastro: §0, ato 2, Aceito recomendações; relatório R-07`
- **OP-23** — Quem executa faz o fechamento do marco promover sozinho a versão aceita, cobrando a linha de validação do consultor e acertando o texto da operação em cada card.
  - `precisa de: conferência do modelo, casos registrados pela auditoria` · `altera: fechamento.promoção da versão aceita, fechamento.validação do consultor` · `tarefas: RAF-T23, RAF-T23a, RAF-T23b` · `lastro: §0, ato 2, Aceito recomendações; relatório R-06, R-08`
- **OP-24** — Quem executa ensina o gerente do loop a seguir a janela quando o modelador cria operação nova, enfileirando a rodada de replanejamento.
  - `precisa de: escolhas do dono sobre o roteiro, conferência do modelo, despacho de tarefa, gerente do loop` · `altera: gerente do loop.rota do modelador com operação nova` · `tarefas: RAF-T24, RAF-T24a` · `lastro: §0, ato 2, Aceito recomendações; relatório R-04`
- **OP-25** — Quem executa ensina o planejador a escrever, na rodada que segue a emenda, o card da operação nova bloqueado até o aceite da versão no marco.
  - `precisa de: escolhas do dono sobre o roteiro, planejador, conferência do modelo` · `altera: planejador.card da operação nova` · `tarefas: RAF-T25` · `lastro: §0, ato 2, Aceito recomendações; relatório R-04`
- **OP-26** — Quem executa reescreve no modelador e no consultor a doutrina da promoção de versão, que passa ao comando do marco e só chama o modelador no conflito.
  - `precisa de: fechamento` · `altera: modelador.papel na promoção de versão, consultor.forma da validação da versão pendente` · `tarefas: RAF-T26, RAF-T26a` · `lastro: §0, ato 2, Aceito recomendações; relatório R-08`

**D. Backlog, fechamento e telemetria**

- **OP-27** — Quem executa faz o pré-voo do pedido separar o caminho que o pedido manda criar do caminho que já devia existir, sem tomar extensão solta por caminho.
  - `precisa de: relatório da auditoria final, planejador, casos registrados pela auditoria` · `altera: pré-voo do pedido.o que conta como caminho, pré-voo do pedido.caminho a criar` · `tarefas: RAF-T27, RAF-T27a` · `lastro: §0, ato 2, Aceito recomendações; relatório R-17`
- **OP-28** — Quem executa faz o controle do backlog avisar, ao tirar um plano da fila, que a diretiva de priorização não cita nada vivo nem o plano que saiu.
  - `precisa de: relatório da auditoria final, gerente do loop, casos registrados pela auditoria` · `altera: controle do backlog.aviso de diretiva desatualizada` · `tarefas: RAF-T28` · `lastro: §0, ato 2, Aceito recomendações; relatório R-18`
- **OP-29** — Quem executa faz o controle do backlog recusar o plano que declara o mesmo prefixo de decisão que outro já declarou, nomeando o plano dono do prefixo.
  - `precisa de: controle do backlog, casos registrados pela auditoria` · `altera: controle do backlog.prefixo de decisão repetido` · `tarefas: RAF-T29, RAF-T29a` · `lastro: §0, ato 2, Aceito recomendações; relatório R-28`
- **OP-30** — Quem executa faz o fechamento de tarefa tratar cada achado do laudo pela linha de origem, pulando o já registrado e avisando a falha de instrumento.
  - `precisa de: fechamento, rubrica de revisão, casos registrados pela auditoria` · `altera: fechamento.origem do achado registrado, fechamento.aviso de falha de instrumento, rubrica de revisão.alvo do achado de instrumento` · `tarefas: RAF-T30, RAF-T30a` · `lastro: §0, ato 2, Aceito recomendações; relatório R-19, R-20`
- **OP-31** — Quem executa faz a série de telemetria guardar uma linha por agente, atribuída ao plano e à tarefa que a abertura do despacho declara.
  - `precisa de: despacho de tarefa, casos registrados pela auditoria` · `altera: série de telemetria.plano e tarefa atribuídos, série de telemetria.linhas por agente` · `tarefas: RAF-T31, RAF-T31a, RAF-T31b` · `lastro: §0, ato 2, Aceito recomendações; relatório R-16`
- **OP-32** — Quem executa faz o painel do gerente mostrar a tarefa que a abertura do despacho declara, e não a tarefa corrente do loop.
  - `precisa de: série de telemetria, despacho de tarefa, casos registrados pela auditoria` · `altera: painel do gerente.tarefa mostrada` · `tarefas: RAF-T32, RAF-T32a` · `lastro: §0, ato 2, Aceito recomendações; relatório R-16`
- **OP-33** — Quem executa escreve na norma de consumo do kit a regra de que todo despacho de subagente abre com a linha que declara o plano e a tarefa.
  - `precisa de: série de telemetria, painel do gerente` · `altera: norma de consumo do kit.linha de abertura do despacho` · `tarefas: RAF-T33` · `lastro: §0, ato 2, Aceito recomendações; relatório R-16`
- **OP-34** — Quem executa ensina o gerente do loop a levar ao consultor a falha de instrumento que o fechamento avisa e a linha do card que ele vai triar.
  - `precisa de: fechamento, norma de consumo do kit, gerente do loop` · `altera: gerente do loop.falha de instrumento levada ao consultor, gerente do loop.card entregue ao consultor` · `tarefas: RAF-T34` · `lastro: §0, ato 2, Aceito recomendações; relatório R-20, R-16`
- **OP-35** — Quem executa ensina o consultor a citar a origem no laudo de todo achado que ele registra ou reescreve a partir dele.
  - `precisa de: fechamento, consultor` · `altera: consultor.origem citada no achado` · `tarefas: RAF-T35` · `lastro: §0, ato 2, Aceito recomendações; relatório R-19`

**E. Doutrina do planejador e comunicação**

- **OP-36** — Quem executa dá ao planejador uma régua de profundidade pelo tamanho do plano, que dispensa no plano de até cinco operações os itens que não mudam o resultado.
  - `precisa de: escolhas do dono sobre o roteiro, relatório da auditoria final, planejador` · `altera: planejador.profundidade do planejamento` · `tarefas: RAF-T36` · `lastro: §0, ato 2, Aceito recomendações; relatório R-21`
- **OP-37** — Quem executa tira do pedido do planejador ao modelador a exigência de caminho, linha e nome de comando nas células descritivas do modelo.
  - `precisa de: planejador, modelador` · `altera: planejador.pedido ao modelador` · `tarefas: RAF-T37` · `lastro: §0, ato 2, Aceito recomendações; relatório R-22`
- **OP-38** — Quem executa passa a quem conduz, antes do despacho do planejador, a checagem de versão do kit que o planejador hoje é mandado invocar.
  - `precisa de: relatório da auditoria final, planejador` · `altera: checagem de versão do kit.momento em que roda, planejador.checagem de versão registrada` · `tarefas: RAF-T38` · `lastro: §0, ato 2, Aceito recomendações; relatório R-23`
- **OP-39** — Quem executa ensina o gerente do loop a abrir a mensagem de marco nomeando a entrega e o pedido do dono que a originou.
  - `precisa de: relatório da auditoria final, gerente do loop, casos registrados pela auditoria` · `altera: gerente do loop.abertura da mensagem de marco` · `tarefas: RAF-T39, RAF-T39a` · `lastro: §0, ato 2, Aceito recomendações; relatório R-25`

**Fecho do plano**

- **OP-40** — Quem executa revisa o guia de entrada do kit para que ele descreva o kit como fica depois das cinco etapas.
  - `precisa de: medidor de custo da sessão, despacho de tarefa, gatilho do próximo passo, filtro da saída dos testes, dossiê de evidência, conferência de verificação do card, medida gravada do card, conferência do modelo, fechamento, pré-voo do pedido, controle do backlog, série de telemetria, painel do gerente` · `altera: guia de entrada do kit.aderência ao kit entregue` · `tarefas: RAF-T40` · `lastro: §0, ato 2, Libere o plano; prompt do planejador, o plano fecha com o guia revisado`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final | lastro na §0 ou no relatório |
|---|---|---|---|
| gerente do loop.janela em que o loop abre | o loop de um plano pode começar na mesma janela que o planejou, que já chega carregada; nada liga o começo do loop ao fim do planejamento | o planejamento encerra a sua janela no primeiro marco, e o loop de um plano recém-planejado abre numa janela nova, com o plano gravado como único insumo | relatório R-01 |
| gerente do loop.entrega do despacho ao executor | quem conduz copia na conversa o card inteiro e o handover, perto de três mil tokens por tarefa | quem conduz repassa ao executor o texto pronto do despacho, que aponta o arquivo do pacote: perto de mil tokens por tarefa, ou menos | relatório R-02 |
| gerente do loop.conferência das âncoras | quem conduz reconfere à mão, a cada despacho, as linhas que o card cita; foram vinte e três turnos no loop medido | nenhum passo manda reconferir: as âncoras chegam conferidas no pacote | relatório R-03 |
| gerente do loop.rota do modelador com operação nova | quando a emenda do modelo cria uma operação ainda sem card, o despacho seguinte é recusado e o loop trava | o loop despacha o modelador e em seguida o planejador para a rodada, e a janela segue com as tarefas da versão vigente | relatório R-04 |
| gerente do loop.falha de instrumento levada ao consultor | a falha de instrumento só sobe ao consultor pela leitura de quem conduz, e um laudo que recomenda seguir a deixa passar | o aviso de falha que o fechamento imprime também leva a tarefa ao consultor | relatório R-20 |
| gerente do loop.card entregue ao consultor | o consultor recebe o card da tarefa corrente, que pode não ser a que parou | o consultor é despachado com a linha que declara o card em triagem | relatório R-16 |
| gerente do loop.abertura da mensagem de marco | a mensagem de marco não diz o que o dono pediu, e o dono já respondeu perguntando se lhe pediam mais uma auditoria | a mensagem de marco abre nomeando a entrega e citando, com a data e poucas palavras do dono, o pedido que a originou | relatório R-25 |
| medidor de custo da sessão.medida por turno | só existe como rascunho da auditoria, sem teste | um comando do kit, com teste, grava o contexto reenviado em cada turno de uma conversa gravada | relatório R-01 |
| medidor de custo da sessão.medida por passo e por tarefa | o rascunho reconhece só as tarefas do plano auditado e quebra numa janela sem despacho | os turnos se repartem por passo do loop e por tarefa de qualquer plano ou tíquete; numa janela sem despacho o comando informa zero e termina bem | relatório R-01 |
| despacho de tarefa.lugar do card despachado | o card, o handover e a leitura do modelo saem inteiros na tela de quem conduz | o pacote da tarefa é gravado num arquivo da pasta do plano, fora do versionamento, que se regenera a cada despacho | relatório R-02 |
| despacho de tarefa.texto pronto ao executor | quem conduz monta à mão o recado ao executor | o despacho imprime o recado pronto: a linha que declara plano e tarefa, o caminho do pacote e a forma da resposta esperada | relatório R-02 |
| despacho de tarefa.âncoras conferidas | as linhas que o card cita chegam como o planejador as viu, às vezes já deslocadas | o pacote traz cada linha citada com o número atual e o texto dela, e marca como ausente o texto que não está mais no arquivo | relatório R-03 |
| despacho de tarefa.versão do modelo julgada | o despacho julga também a versão pendente do modelo e recusa a tarefa quando a pendente tem operação sem card | o despacho julga só a versão vigente; a pendente fica para o marco | relatório R-04 |
| gatilho do próximo passo.mensagens que o disparam | qualquer mensagem com a frase dispara, inclusive o relato de um subagente; já injetou o backlog três vezes numa mesma sessão | só a mensagem do dono dispara; o relato de subagente e o aviso do sistema não injetam nada | relatório R-15 |
| filtro da saída dos testes.código de saída devolvido | num comando encadeado, o código que volta é o do filtro, e um teste que falhou parece ter passado | volta o código de saída dos testes, também no comando encadeado, nas duas linhas de comando que o kit usa | relatório R-24 |
| dossiê de evidência.casos em que hoje quebra | quebra diante de conteúdo antigo que não se lê como texto, diante da falta do módulo de apoio e quando a medida foi guardada em outra pasta | compara o conteúdo bruto, falha com mensagem que nomeia o módulo ausente e acha a medida também na pasta do plano | relatório R-13 |
| dossiê de evidência.marca do arquivo novo que não é texto | o arquivo novo que não é texto chega sem a marca de novo que o arquivo de texto recebe | os dois chegam com a mesma marca de arquivo novo | relatório R-14 |
| dossiê de evidência.rótulo do registro da orquestração | a lista por arquivo chama de alheio o que o resumo chama de registro da orquestração | a lista e o resumo usam o mesmo nome | relatório R-14 |
| dossiê de evidência.curinga do alvo | a estrela do alvo casa também arquivos de subpastas | a estrela fica numa pasta só, e a estrela dupla alcança as subpastas, como na linha de comando | relatório R-30 |
| dossiê de evidência.caminho acentuado | o arquivo novo com acento no nome chega como ausente; o já rastreado, editado depois do ponto de partida da revisão, chega com o nome entre aspas e as letras acentuadas trocadas por códigos, é tido por alheio à entrega e aparece duas vezes, com dois nomes, no estado do versionador que o revisor lê | o arquivo acentuado, novo ou já rastreado, chega com a sua diferença e com um nome só, como qualquer outro | relatório R-31 · §0, ato 2 |
| dossiê de evidência.linhas removidas dos testes | uma asserção de teste removida passa despercebida; a auditoria viu uma passar com a revisão aprovada | para cada arquivo de teste entre os alvos, a evidência mostra as linhas que saíram | relatório R-12 |
| rubrica de revisão.critério da asserção removida | a régua de testes reprova teste exigido ausente e suíte vermelha, mas não a asserção existente removida | a régua reprova a asserção de teste removida sem que o card mande removê-la | relatório R-12 |
| rubrica de revisão.alvo do achado de instrumento | a rubrica e o gerador do laudo fecham quatro alvos, e nenhum laudo escreve o achado de instrumento que o fechamento lê | o quinto alvo, instrumento, é aceito, e o achado escrito com ele chega ao aviso do fechamento | relatório R-20 |
| conferência de verificação do card.resultado esperado no bloco cercado | no bloco cercado, a medida de depois da entrega é comparada com o valor de antes | é comparada com o resultado que o card escreve para depois da entrega | relatório R-09 |
| conferência de verificação do card.literal com pontuação | um valor com ponto, vírgula ou ponto e vírgula é cortado, e o par pode ser lido dentro do próprio comando | o valor entre crases é lido inteiro, só depois do comando; o card antigo continua lido como antes | relatório R-10 |
| conferência de verificação do card.comandos de leitura do versionador | só dois programas rodam, e a verificação que consulta o versionador é recusada | o versionador roda nos subcomandos de leitura, e outro subcomando é recusado com mensagem que o nomeia | relatório R-11 |
| conferência de verificação do card.recorte do despacho no comando | o comando não tem como saber contra que recorte comparar | a marca do recorte no comando é trocada pelo recorte que o despacho gravou para a tarefa | relatório R-11 |
| conferência de verificação do card.linha de invariância | não há como declarar uma linha que prova que o alvo ficou igual | a linha declarada de invariância não é medida antes da entrega e é medida depois dela | relatório R-11, R-27 |
| medida gravada do card.pasta em que é gravada | a pasta vem do plano indicado, não da árvore medida, e a medida feita na cópia de ensaio vai parar fora dela | a medida fica na pasta do plano dentro da árvore que foi medida | relatório R-05 |
| medida gravada do card.momento no nome | o nome não diz se a medida é de antes ou de depois, e a segunda apaga a primeira | o nome diz o momento, e as duas convivem | relatório R-05 |
| medida gravada do card.leitura pelo revisor | o revisor procura só o nome sem momento | o revisor lê a de depois, na falta dela a de antes, e por último as vinte já gravadas com o nome antigo | relatório R-05 |
| planejador.árvore em que se mede o antes | o card que depende de outro mede o antes na árvore real, onde o anterior ainda não está aplicado | ele mede na cópia de ensaio com os anteriores aplicados, só o primeiro de cada cadeia mede na árvore real, e o valor publicado diz em que árvore foi medido | relatório R-26 |
| planejador.card que deixa o alvo igual | o card de revisão sem texto novo não tem linha que o discrimine | a linha que o discrimina é a prova de que o alvo não mudou desde o recorte, declarada como invariância e medida depois da entrega | relatório R-27 |
| planejador.medida gravada na rodada | a rodada de replanejamento reescreve cards sem gravar a medida deles | a rodada grava a medida de antes na árvore real e a de depois na cópia de ensaio, para cada card que reescreve | relatório R-05 |
| planejador.card da operação nova | nada diz quem escreve o card da operação que uma emenda do modelo cria no meio do loop | na rodada que segue a emenda, o planejador escreve esse card e o registra bloqueado até o aceite da versão no marco | relatório R-04 · §0, ato 2 |
| planejador.profundidade do planejamento | todo plano passa pelo mesmo roteiro completo, e o planejamento custou mais de um quarto do gasto dos subagentes no plano medido | uma régua pelo tamanho do plano dispensa, no plano de até cinco operações, os itens que não mudam o resultado | relatório R-21 · §0, ato 2 |
| planejador.pedido ao modelador | o roteiro deixa o pedido ao modelador exigir caminho no contrato, o que a norma do modelador recusa | o roteiro diz que o pedido não exige caminho, linha nem nome de comando nas células descritivas, e que esses dados vão aos fatos do plano e ao card | relatório R-22 |
| planejador.checagem de versão registrada | o roteiro manda o planejador invocar uma rotina que ele, como subagente, pode não conseguir chamar | o planejador registra no cabeçalho a checagem que recebe pronta no pedido, e nenhuma fase manda invocar rotina | relatório R-23 |
| conferência do modelo.versões julgadas | julga sempre as duas versões juntas e recusa o card que cita uma operação que só a versão pendente tem | pode julgar só a vigente quando pedida assim; sem o pedido, continua julgando as duas; e aceita o card que cita uma operação de qualquer das duas | relatório R-04 · §0, ato 2 |
| conferência do modelo.fidelidade do texto copiado no card | aprova card cujo texto copiado da operação diverge do modelo | recusa o card cujo texto copiado diverge da versão que ele cita | relatório R-06 |
| conferência do modelo.diferença entre versões | casa as operações só pelo número: uma inserção aparece como alterações em cascata, e propriedade nova não aparece | casa primeiro pelo texto, mostra operação nova, renumerada e alterada, e lista a propriedade que só uma das versões tem | relatório R-07 |
| fechamento.promoção da versão aceita | o aceite no marco só grava o veredito, e a promoção custa uma instância inteira do modelador | o próprio comando do marco promove a versão aceita, registra a anterior como obsoleta e acerta o texto da operação em cada card; havendo conflito, recusa e prepara o pedido ao modelador | relatório R-06, R-08 |
| fechamento.validação do consultor | a validação do consultor antes do dono não fica gravada em lugar nenhum | o aceite exige a linha de validação do consultor, gravada ao lado do veredito do dono | relatório R-08 |
| fechamento.origem do achado registrado | o achado do laudo é conferido contra os já registrados só por semelhança de texto, e o que o consultor reescreveu entra de novo, em duplicata | cada achado registrado cita a linha do laudo de onde veio, e o fechamento pula o que já foi registrado com essa origem | relatório R-19 |
| fechamento.aviso de falha de instrumento | a falha de instrumento num laudo que recomenda seguir não chega ao consultor | o fechamento avisa, numa linha própria, cada achado de instrumento que relata queda ou erro | relatório R-20 |
| modelador.papel na promoção de versão | o modelador é chamado a cada aceite para promover a versão | o modelador só é chamado quando o comando do marco encontra conflito | relatório R-08 |
| consultor.forma da validação da versão pendente | a validação do consultor antes do dono não tem forma escrita | a definição do consultor dá a forma da linha de validação que o comando do marco cobra | relatório R-08 |
| consultor.origem citada no achado | o achado que o consultor reescreve a partir de um laudo não diz de onde veio | o achado cita a mesma origem no laudo que o fechamento usa | relatório R-19 |
| pré-voo do pedido.o que conta como caminho | uma extensão solta conta como caminho, e um arquivo com extensão fora de uma lista curta não conta | conta o que termina em barra, o que tem pasta e extensão curta, e o nome solto com uma das extensões conhecidas | relatório R-17 |
| pré-voo do pedido.caminho a criar | o caminho que o pedido manda criar sai como faltante e o pré-voo falha; foram seis linhas assim no pedido medido | ele sai como a criar, sem derrubar o resultado; o pedido medido passa com seis linhas a criar | relatório R-17 |
| controle do backlog.aviso de diretiva desatualizada | tirar um plano da fila deixa a diretiva de priorização apontando para o que já saiu, sem aviso | um aviso diz que a diretiva não cita nada vivo nem o plano que saiu; o resultado do comando não muda | relatório R-18 |
| controle do backlog.prefixo de decisão repetido | dois planos podem declarar o mesmo prefixo de decisão sem recusa | a conferência recusa o segundo, nomeando o plano dono; citar o prefixo de outro plano continua permitido | relatório R-28 |
| série de telemetria.plano e tarefa atribuídos | linhas vão para o plano errado quando o despacho cita outro plano antes do seu | a atribuição sai da linha de abertura do despacho, antes de qualquer outra pista | relatório R-16 |
| série de telemetria.linhas por agente | o mesmo agente pode deixar mais de uma linha | uma linha por agente, a última e acumulada; as linhas antigas ganham a coluna nova vazia | relatório R-16 |
| painel do gerente.tarefa mostrada | mostra a tarefa corrente do loop, mesmo quando o agente em curso foi despachado para outra | mostra a tarefa que a linha de abertura do despacho declara | relatório R-16 |
| norma de consumo do kit.linha de abertura do despacho | a regra não existe | todo despacho de subagente abre com uma linha que declara o plano e, quando houver, a tarefa ou o tíquete; a regra mora num lugar só | relatório R-16 |
| checagem de versão do kit.momento em que roda | a rotina roda quando o planejador a invoca na última fase | a rotina diz que quem conduz a roda antes de despachar o planejador e passa o resultado no pedido | relatório R-23 |
| guia de entrada do kit.aderência ao kit entregue | o guia não cita dois comandos do kit e descreve os demais como estão antes das cinco etapas | o guia cita todos os comandos do kit, inclusive o medidor novo, descreve o que as cinco etapas mudaram, e a conferência do guia passa | §0, ato 2 · prompt do planejador |
| relatório da auditoria final.recomendações | trinta e uma recomendações, escritas e não aplicadas | as mesmas trinta e uma, intactas no relatório; trinta aplicadas pelo plano e uma registrada sem ação | §0, ato 1 · §0, ato 2 |
| escolhas do dono sobre o roteiro.quatro escolhas aceitas | aceitas pelo dono em 2026-09-28 | as mesmas, intactas | §0, ato 2 |
| rascunhos de medição da auditoria.registro da auditoria | dois programas de uso único, com os defeitos que a auditoria viu | intactos, como registro da auditoria | relatório R-01 |
| casos registrados pela auditoria.resposta do kit a cada caso | cada caso reproduzido repete o defeito que a auditoria registrou | cada caso reproduzido dá o resultado que a verificação da sua recomendação pede | §0, ato 1 · relatório §5 |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 1 | 2026-09-28 | obsoleta | modelador, autoria sobre o dossiê do planejador. Caiu pelo aceite da versão 2 em 2026-09-29 |
| 2 | 2026-09-29 | obsoleta | modelador, conflito sobre o achado de modelo do laudo RAF-T10, que toca OP-10. Validada pelo consultor em DRF-58 e aceita pelo dono no Marco 3 em 2026-09-29: *"aceito"*; Caiu pelo aceite da versão 3 em 2026-09-29 |
| 3 | 2026-09-29 | obsoleta | modelador, conflito sobre o achado de modelo do laudo RAF-T19, pela decisão DRF-37, que toca OP-19; Caiu pelo aceite da versão 4 em 2026-09-30 |
| 4 | 2026-09-29 | vigente | modelador, emenda pela decisão DRF-68 do consultor, sobre o achado AE-186 do laudo RAF-T30, que toca OP-30 |

## 2. Fatos estabelecidos

Fonte de cada fato entre parênteses. "Qn" é o dossiê n da campanha de 2026-09-28 (16 dossiês de batedor,
até 40 linhas cada); o dossiê em si é volátil, e o fato carrega a âncora que o re-deriva.

### 2.1 Estado do repositório e do plano de origem

- **F-1** (condução, 2026-09-28) — Próximo id `P-0755` (`docs/plans/_INBOX.md:5`). Branch
  `plan/planner-modelo-escopo`, HEAD `2513964`; WIP não commitado do `P-0754` (90 linhas no `git status`), mais o
  roteiro e `docs/audits/sonda-2026-09-28/`. O `P-0754` está `ready` com 16/16 tarefas `done` e o Marco 3
  pendente. A diretiva de priorização (`docs/DIARIO_DE_OBRAS.md:4`) aponta o `P-0754`; a condução a reescreve com
  `backlog.py diretiva` depois do registro deste plano. Suíte: 521 testes coletados. Python 3.12 (Q11:
  `tests/__pycache__/test_materializar.cpython-312-pytest-9.0.3.pyc`).
- **F-2** (condução) — Tamanhos em linhas: `card_check.py` 584, `modelo.py` 733, `encerrar.py` 1298,
  `backlog.py` 2347, `review_evidence.py` 1137, `backlog_hook.py` 109, `telemetria_hook.py` 389, `prevoo.py` 180,
  `caminhos.py` 131 (todos em `.claude/tools/`), skill `scrum-master` 435, `pantonic-planner.md` 578.
- **F-3** (Q16) — Testes coletados por arquivo (`python -m pytest --co -q tests/<arquivo>`, exit 0 em todos):
  `test_card_check.py` 22, `test_modelo.py` 34, `test_encerrar.py` 37, `test_backlog.py` 127,
  `test_review_evidence.py` 78, `test_telemetria_hook.py` 15, `test_progresso_hook.py` 45, `test_prevoo.py` 6.
  Não existem `tests/test_backlog_hook.py`, `tests/test_pytest_pretooluse.py` nem `tests/test_pytest_filter.py`;
  o `backlog_hook.py` é testado dentro de `tests/test_backlog.py` (`:28`
  `_HOOK_PATH = _ROOT / ".claude" / "tools" / "backlog_hook.py"`).
- **F-4** (Q16) — `pwsh .claude/checks/check-readme.ps1`, exit 0, stdout:
  `check-readme: OK - 10 agente(s), 13 skill(s), 20 guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida; frases de contagem de 'Os guardrails' conferidas: 'regras mínimas obrigatórias'=True, 'regras falham como teste executável'=True.`
  O `README.md` cita os instrumentos em 12 linhas reais (`:697` `modelo.py`; `:721`, `:724`, `:725`, `:919`
  `encerrar.py`; `:770`, `:908` `backlog.py`; `:929` `review_evidence.py`; `:916` `backlog_hook.py`; `:471`
  `progresso_hook.py`; `:935` `prevoo.py`; `:940` `materializar.py`); `card_check.py` e `telemetria_hook.py` não
  têm menção.
- **F-5** (roteiro §1; handover §5) — O plano fictício `P-0755` da auditoria foi descartado; a cópia em
  `%TEMP%\claude\auditoria\p0754_artefatos\` é volátil e já tem a versão promovida. Nenhum caso da auditoria se
  reproduz a partir dela: todo caso vira fixture construída.
- **F-6** (auditoria §8) — Contexto reenviado por turno na sessão principal: 285,6k no loop real, 485,6k no
  fictício (planejamento, loop e auditoria numa janela só). Saída da sessão principal no Passo 4: 3,06k por
  despacho no loop real, 0,72k na variante com o card por arquivo. Âncoras re-derivadas à mão: 23 turnos no loop
  real. Planejamento = 352,2k de 1.250,0k do custo de subagentes do plano fictício.
- **F-7** (roteiro §1, divergências) — A fonte do hook do pytest é `.claude/global/hooks/pytest_pretooluse.py`,
  idêntica à projeção em `~/.claude/hooks/` (`diff -q`); a projeção é ato do dono (`materializar.py apply`). Os
  registros 18 e 42 da auditoria são o mesmo incidente (a `R-15` fecha a causa da `R-29`). As `R-26`..`R-31`
  foram escritas pelo consultor na `DAU-33`, sem revisão própria, e conferidas no roteiro.

### 2.2 Loop, despacho e âncoras (etapa A)

- **F-8** (Q1) — Skill `.claude/skills/scrum-master/SKILL.md` (435 linhas): `:9-10` "ponto de entrada único da
  execução de backlog"; `:35` Passo 1, gatilho "invocação da skill, antes de qualquer despacho"; `:48` Passo 2;
  Passo 3 em `:57-87` (`:61-63` `G-PLANREADY` e Gate de delegação; `:65-66` terceiro gate `modelo.py check`; `:70`
  quarto gate `card_check`; `:77-80` despacho por comando, que "imprime o card inteiro, o bloco `HANDOVER` e a
  linha `ref=<sha>`"); Passo 4 em `:89-122` (`:104-105` "este passo só invoca o executor"; `:107-109` invocação do
  executor; `:112-114` gramática da linha de retorno: `<tarefa> review`, `<tarefa> review pendencia=<uma linha>`,
  `<tarefa> blocked motivo=<dependencia|premissa|ferramenta> <uma linha de razão>`; `:119-121` o despacho cola as
  âncoras re-derivadas no ato). `grep "Marco 1"` na skill = 0: o loop começa na invocação, sem relação com o fim
  do planejamento.
- **F-9** (Q3) — `.claude/tools/backlog.py`: `despachar` em `:2083`
  (`def despachar(repo: Path, id_: str, mundo: str | None = None) -> ResultadoStatus:`), CLI `:2255` e `:2338`;
  `:2111` `plano_abs = str(repo / pai.arquivo)` (não deriva pasta; `caminhos.pasta_do_plano` não é chamado);
  `:2116-2124` roda `modelo.py check --plano <plano> --root <repo>` por subprocess e aceita rc 0 ou 2; `:2190`
  grava `"plano": pai.arquivo` em `.claude/estado/tarefa-corrente.json`; impressão só depois de todas as
  conferências, nesta ordem: `:2196` `=== DESPACHO: {id_} — {alvo.titulo}`, `:2198` `=== HANDOVER DE …` com o
  texto, `:2200` `print(show(modelo, id_))`, `:2201` `ref={ref}`; recusa em stderr
  `despachar: recusado — {gate}: {razao}` (`:2095`). `despachar --help`:
  `usage: backlog.py despachar [-h] [--mundo {antes,depois}] [--repo REPO] id`.
- **F-10** (Q4) — `git check-ignore -q docs/plans/P-0754-auditoria-final/despacho/AUF-T1.md` sai 1 (não
  ignorado); nenhuma regra de `.gitignore` cita `despacho`. Nenhum instrumento enumera `despacho/*.md` a ponto de
  acusar: `backlog.py:985` (`_resolver_arquivo_citado`, `C-11`) resolve citação por basename só com achado único,
  e o basename `AUF-T1.md` já tem três homônimos por pasta de plano (`rdo/`, `laudos/`, `evidencia/`).
- **F-11** (Q10) — `.claude/tools/backlog_hook.py:33` `_GATILHO = "proximo passo"`; `:73` lê o prompt de
  `payload["prompt"]`; `:54-55` `_casa_gatilho` testa `_GATILHO in _norm(prompt)`. Auditoria reg. 42: o gatilho
  casou em relatórios de subagente ("Próximo passo de quem conduz") e injetou 15,3 KB três vezes.
- **F-12** (Q11) — `.claude/global/hooks/pytest_pretooluse.py` (64 linhas): `:15` `FILTER_PATH` absoluto;
  `:17-21` `PYTEST_RE`; passthrough em `:35` (ferramenta diferente de Bash e PowerShell), `:40` (`|`, `<` ou `>`
  no comando), `:42` (`#nofilter` ou `pytest_filter`), `:44` (`--collect-only` ou `--co`), `:46` (sem pytest);
  `:49` `new_cmd = f'{cmd} 2>&1 | python "{FILTER_PATH}"'` (o pipe vai ao fim do comando inteiro). Projeção
  declarada em `.claude/projecoes.json:147`. Nenhum teste dedicado. Auditoria reg. 45: `cd … && pytest …; echo
  "exit=$?"` sai com o exit do filtro.
- **F-13** (Q14) — `docs/audits/sonda-2026-09-28/medir.py` (26 linhas) e `passos.py` (40 linhas): biblioteca
  padrão, `sys.argv` posicional, sem argparse. `medir.py <transcript.jsonl> <saida.tsv>` grava, por mensagem
  `assistant` com `message.usage`, `ctx = input + cache_read + cache_creation` (exit 0 no transcript real).
  `passos.py <tsv> <regex_inicio> <regex_fim>` classifica passos P2..P9 por substring; `:31` tarefa fixa em
  `despachar (AUF-T\d+)`; `:40` divide por `len(ts)` sem guarda: `ZeroDivisionError`, exit 1, em janela sem
  despacho `AUF-T`.

### 2.3 Instrumentos de revisão e medida (etapa B)

- **F-14** (Q5) — `.claude/tools/card_check.py`: `:97-98` `_ANTES_DEPOIS_RE` (literal de `antes` não aceita
  crase, `,` nem `;`; o de `depois` não aceita crase, `.` nem quebra); `:105`
  `_COMANDOS_PERMITIDOS = ("python", "pwsh")`; `:106` tokens recusados `; && || | > >> < <<` (mais `$(` e crase
  inicial, `:231`); `:242-250` `shlex.split` e `subprocess.run(tokens, cwd=root, …)` sem `shell=True`, saída =
  stdout+stderr; a forma de bloco cercado (`:388-430`) compara sempre com `Medido antes` (`:419-420`; docstring
  `:343-344`), qualquer que seja `--mundo`; `:257-261` `exit N` compara o returncode, senão substring; o
  `→ esperado` só é checado como presente (`:403-404`); `--gravar` sem caminho usa
  `caminhos.destino_medida(args.root, args.plano, args.tarefa)` (`:546`). Seleção de forma: `:168` bloco cercado,
  `:189` inline, `:211-214` falha `fora da forma da 8.1`.
- **F-15** (Q5; Q4) — `.claude/tools/caminhos.py:110-116` `destino_medida(raiz, plano_path, tarefa)`: plano em
  pasta → `pasta_do_plano(plano_path) / "evidencia" / f"{id}-{tarefa}-medida.json"` (a pasta vem do `--plano`,
  não da raiz); legado → `raiz / "docs" / "RDO" / "evidencia" / f"{id}-{tarefa}-medida.json"`. `pasta_do_plano`
  (`:54`) devolve `None` para plano legado. Há 20 arquivos de medida versionados, todos em
  `docs/plans/P-0753-auditoria-estagio-1/evidencia/` com o nome `<P-id>-<tarefa>-medida.json`.
- **F-16** (Q6) — Corpus de `Verificação` em `docs/plans/**/*.md`: 416 itens em bloco cercado, 665 inline, 244
  inline com par `antes`/`depois` lido pela regex atual. Um único par tem pontuação no literal:
  `docs/plans/P-0753-auditoria-estagio-1/plano.md:434` (depois = `backlog.py`, que a regex corta em `backlog`). Em
  `docs/plans/P-0752-fato-no-ponto-de-uso.md:530` a regex casa dentro do comando, antes do par real. Rubrica §8.1
  (`docs/RUBRICA_DE_REVISAO.md:314-338`): Forma A (bloco cercado, `**Medido antes: <valor>**`) e Forma B
  (inline).
- **F-17** (Q9) — `.claude/tools/review_evidence.py`: `:351` e `:396`
  `_git(["status", "--porcelain=v1", "--untracked-files=all"], root)` sem `-z`; `:558` e `:691`
  `fnmatch.fnmatchcase` para alvo com curinga; `:639` e `:662`
  `"(arquivo binário ou não-UTF-8 — trecho omitido)"` sem a marca de arquivo novo; `:992`
  `Path(dir_evidencia) / f"{plano_id}-{dossie.tarefa_id}-medida.json"` (com `--out`), `:994` `destino_medida` sem
  ele; no `--atribuir` (`main` `:1016`), `_load_rdo` em `:1079` e, via `mapear_alvos_de_outras_tarefas`
  (`:1094`), em `:486` ficam fora do `try` (`:1080-1091`): `rdo.py` ausente sai em traceback em vez de
  `review_evidence: FALHOU - rdo.py: módulo não encontrado em '<caminho>'` (`:118`); a lista por arquivo rotula
  `atribuição: alheio` (`:880`, `:883`) o que o resumo chama `Registro da orquestração` (`:910`; tupla
  `_REGISTRO_ORQUESTRACAO` `:432`); nenhuma lógica usa `numstat` nem reconhece arquivo de teste. Planos vivos têm
  0 alvos com `*`.
- **F-18** (Q9) — Rubrica, dimensão `testes` (`docs/RUBRICA_DE_REVISAO.md:93-106`, peso na `:183`): `não
  conforme` = "teste exigido ausente, suíte em exit não-zero, ou teste cujo significado mudou removido em vez de
  reescrito" (`:103-104`). Auditoria reg. 30: a remoção de asserção vizinha (`AE-97`) passou verde.

### 2.4 Modelo, versão e marco (etapa C)

- **F-19** (Q7; roteiro §1) — `.claude/tools/modelo.py`: vocabulário `V1`..`V21`, todos em `validar`
  (`:319-424`); com `pendente=True`, `V2`, `V4`, `V14`, `V19` e `V20` ficam fora; `:356-357` `V1` (operação sem
  tarefa) vale em qualquer bloco; `:586-589` o `check` valida a `## 1A` com `pendente=True` e prefixa as
  violações com `1A: `; `:420-422` `V4` e `V14`; `:482` `_diff_fluxo` casa por número e emite `[+]`, `[-]`,
  `[~]`; `:499` `_diff_estado` só mostra chave presente nas duas versões. Nenhum plano de `docs/plans/` tem
  `## 1A`; os testes usam fixtures em arquivo (`tests/test_modelo.py:46-47`, `fluxo-pendente.md` e
  `fluxo-pendente-contrato.md`); helpers `:53` `_load_modelo`, `:64` `_plano_stub`, `:70` `_tarefa_stub`.
  Consequência (roteiro §1): emenda que cria operação sem card recusa o despacho por construção
  (`backlog.py:2117`).
- **F-20** (Q8) — `.claude/tools/encerrar.py`: `marco --aceita-versao K` (`gravar_marco`, `:915`) recusa sem
  `## 1A` (`:946-949`, `plano sem versão pendente (## 1A)`), grava o veredito e imprime o dossiê `Ato: emenda`
  (`:1000-1024`) antes de `marco: Marco <n> gravado — <resultado>` (`:1239-1247`); não promove nem cobra a
  validação do consultor. Uso:
  `encerrar.py marco --plano PLANO … --marco MARCO --resultado {go,no-go} --veredito VEREDITO [--aceita-versao ACEITA_VERSAO | --recusa-versao RECUSA_VERSAO]`.
- **F-21** (Q2) — A promoção da `## 1A` hoje é do modelador (`.claude/agents/pantonic-model-designer.md:89-92`:
  aceita, o conteúdo da `## 1A` passa à `## 1`; a anterior vira `obsoleta` com a frase
  `Caiu pelo aceite da versão <N> em <data>`). A validação prévia do consultor está em `GOVERNANCA.md:413-415` e
  `:443` e em `.claude/agents/pantonic-consultant.md:30`, sem forma de linha em arquivo nenhum. A rota
  `modelador` segue sem parar a janela (`GOVERNANCA.md:92`, `:102`; `pantonic-consultant.md:27`;
  `scrum-master/SKILL.md:184`, `:307-308`). O card corretivo `T<n>a` é do consultor
  (`pantonic-consultant.md:30`; `GOVERNANCA.md:457`). Nenhum desses textos manda a rodada gravar medida.
- **F-31** (ensaio da Fase 4, 2026-09-28) — Com a `V22` da `RAF-T21` aplicada na cópia, o `modelo.py check`
  sai 1 sobre quatro planos encerrados, com texto de operação divergente no card — `P-0746` (1 linha `V22`,
  `LST-T5`), `P-0747` (7, `CON-T3`..`CON-T5a`), `P-0748` (5, `TLG-T2`..`TLG-T4`) e `P-0753` (1, `AF-T19`) — e 0
  sobre os demais planos com modelo, o `P-0754` inclusive. Nenhum instrumento roda o `check` sobre plano
  encerrado. No mesmo ensaio, o `encerrar.py` fecha tarefa pelo `check` completo (`_gate_modelo`), e o
  `_ler_tsv` do `encerrar.py` lê a série pelo cabeçalho e descarta linha com outro número de colunas.

### 2.5 Backlog, fechamento e telemetria (etapa D)

- **F-22** (Q12) — `.claude/tools/prevoo.py`: `:33` nove extensões (`.py`, `.md`, `.ps1`, `.json`, `.tsv`,
  `.txt`, `.yml`, `.yaml`, `.toml`); `:57-58` `_e_caminho(token)` = termina numa extensão ou em `/`; `:155-176`
  saída `citado | existe | onde`, `sim` ou `não`, exit 0 só sem `não`. Sobre o pedido do plano fictício o
  instrumento imprime 6 linhas `não` (`scratch_sonda/`, `scratch_sonda/amostras/a.txt`,
  `scratch_sonda/amostras/b.txt`, `scratch_sonda/contar.py`, `.txt`, `tests/test_sonda_auditoria_final.py`) e sai
  1; `scratch_sonda/amostras/c.bin` não aparece. O pedido, verbatim: "Crie em scratch_sonda/ duas coisas: (1) as
  amostras scratch_sonda/amostras/a.txt, scratch_sonda/amostras/b.txt e o binário scratch_sonda/amostras/c.bin;
  (2) o utilitário scratch_sonda/contar.py, que recebe caminhos de arquivo e imprime, por arquivo .txt, o número
  de linhas, recusando com mensagem o caminho que não existe, com os testes em
  tests/test_sonda_auditoria_final.py. Tudo só com biblioteca padrão."
- **F-23** (Q3; Q1) — `backlog.py`: `:112` `PREFIXO_CAMPO_RE` lê só `**Prefixo das tarefas no diário:**`; `:132`
  `DIRETIVA_RE`; `:422` `_parse_diretiva` pega ids entre crases antes de ` — `; `:1966` `transacionar_drain`
  (CLI `:2250` e `:2323`). `drain` e `diretiva` são chamados pelas skills `passagem-de-bastao` (`:28`) e
  `diario-de-obras` (`:345-346`, `:351`), não pela `scrum-master`.
- **F-24** (Q15) — 34 planos; 17 declaram `**Prefixo das decisões:**`, sem colisão de declaração; o `P-0749`
  declara `DSA-<n>`; o `P-0743` declara `D-<n>`. Citação de prefixo de outro plano é comum e legítima (9 de 13
  prefixos aparecem em mais de um plano, sempre com dono único). Colisão de prefixo próprio só nos legados sem
  declaração (`DC`, `DM`, `DP`).
- **F-25** (Q8) — `encerrar.py`: `:238` `achados_do_laudo` lê a tabela `| alvo | achado |` de
  `## Achado de processo`; `:284-294` `apensar_achado` grava
  `- **{ae_id}** (`{tarefa_id}`, fechamento, {data}) — {texto} **Rota:** {rota}`; `:555-556` dedupe por
  substring do texto contra as `AE-` do plano e os `--achado` do mesmo fechamento. Nenhuma `AE-` do `P-0754`
  registra origem `laudo:<n>`. A regra `B1` mora só em `scrum-master/SKILL.md:300`; `grep -c escalar encerrar.py`
  = 0.
- **F-26** (Q10) — `.claude/tools/telemetria_hook.py`: `:71` papéis por tarefa do estado (revisor, consultor);
  `:199-206` `_id_plano_da_primeira_mensagem`; `:309-316` lê `agent_transcript_path` e o estado; `:319-324`
  executor → `tarefa`; `:327-336` revisor → `<tarefa>-<sufixo>`, consultor → `<tarefa>-consultor-<n>`;
  `:337-339` demais papéis → `<P-id da primeira mensagem>-<sufixo>`; `:365` caminho de `tarefa-corrente.json`.
  `agent_id` e `agentId` têm 0 ocorrências; se o payload do `SubagentStop` traz `agent_id` não foi confirmado.
  Cabeçalho de `docs/telemetria.tsv`: `data`, `projeto`, `tarefa`, `modelo`, `tool_uses`, `tokens_k`,
  `duracao_s`, `fonte`. `.claude/tools/progresso_hook.py`: `:193-207` `tarefa_corrente` (cache do loop, depois
  `tarefa-corrente.json` → `localizar_card`); `:143-183` `localizar_card`. O consultor recebe o card só pelo texto
  de `scrum-master/SKILL.md:322`. Auditoria reg. 41 e 54: linhas atribuídas ao plano errado, duplicata por
  agente, consultor e painel com a tarefa corrente em vez da despachada.

### 2.6 Doutrina do planejador e comunicação (etapa E)

- **F-27** (Q13) — `.claude/agents/pantonic-planner.md:5` `tools: Read, Glob, Grep, Write, Edit, Bash`; nenhum dos
  11 agentes lista `Skill`; `.claude/settings.json` não trata de `Skill`; se a plataforma bloqueia skill em
  subagente não se verifica pelo repositório. `pantonic-planner.md:464` (Fase 5) manda invocar
  `checar-versao-kit`. Nenhuma skill descreve o despacho do planejador pela condução.
- **F-28** (Q13) — A Fase 3a do planejador (`pantonic-planner.md:187-216`) não traz literalmente o pedido de
  caminho no contrato; o dossiê de autoria do fictício o pediu por conta própria, e o modelador o recusou pela
  norma `TK-76` (`.claude/agents/pantonic-model-designer.md:63-67`: célula descritiva sem caminho, linha,
  identificador nem nome de instrumento). Tabela de profundidade por classe: `pantonic-planner.md:249-252`; item
  14: `:449-458`; Fase 5: `:460-467`.
- **F-29** (Q1) — O repertório de mensagens da skill `scrum-master` (`:379-416`, ids `M-0`..`M-18`) é gerado pelo
  `progresso_hook.py`; não há frase de marco. A forma do relatório de encerramento de janela está em
  `:333-339`. Auditoria reg. 46: a mensagem do Marco 2 do `P-0754` levou o dono a perguntar "Você está pedindo
  mais uma auditoria?".
- **F-30** (Q2) — `docs/DOC_MAP.md:7` põe o `GOVERNANCA.md` entre os docs abaixo de 500 linhas; ele tem 1388.
  Fora deste plano (§7).

## 3. Decisões

| id | valor | razão |
|---|---|---|
| DRF-1 | (dono, D1) `R-04` pela opção (a): o `modelo.py check` do despacho julga só a `## 1`; a `## 1A` é cobrada no marco (`encerrar.py marco --aceita-versao` exige `V1` fechado na pendente); a rota `modelador` com operação nova enfileira a rodada de replanejamento sem parar a janela. Mecânica em `DRF-14`. | Ato 2 do dono (§0) sobre o roteiro §2; preserva "rota modelador segue" (F-21). |
| DRF-2 | (dono, D2) `R-21` adotada: régua de profundidade da Fase 4 por classe e tamanho do plano; conteúdo em `DRF-23`. | Ato 2 do dono; F-6 (planejamento = 28% do custo de subagentes do fictício). |
| DRF-3 | (dono, D3) `R-29` registrada e sem ação: nenhuma operação, nenhum card. | Ato 2 do dono; F-7 (a `R-15` fecha a causa; registros 18 e 42 são o mesmo incidente). |
| DRF-4 | (dono, D4) Plano único, cinco etapas na ordem do roteiro §3: A (`R-01`, `R-02`, `R-03`, `R-15`, `R-24`); B (`R-13`, `R-14`, `R-30`, `R-31`, `R-12`, `R-09`, `R-10`, `R-11`, `R-05`, `R-26`, `R-27`); C (`R-04`, `R-06`, `R-07`, `R-08`); D (`R-17`, `R-18`, `R-28`, `R-19`, `R-20`, `R-16`); E (`R-21`, `R-22`, `R-23`, `R-25`), e a revisão do `README.md` por último. | Ato 2 do dono; uma iniciativa, um contexto de orquestração. |
| DRF-5 | Marcos numerados: Marco 1 = modelo; Marcos 2..6 = fim das etapas A..E. A primeira tarefa de cada etapa B..E nasce em `estado.tsv` `blocked`, razão `dependencia`, nota `Marco <m>: aguarda o veredito do dono sobre a etapa <X>`; só a condução a passa a `ready`, depois de `encerrar.py marco` gravar `go`. | F-20 (`--marco` e a tabela de marcos usam número); precedente `DAU-3` do `P-0754` (`blocked` filtra o `next`). |
| DRF-6 | `R-01`: o instrumento de medida é `.claude/tools/custo_sessao.py`, com dois verbos argparse — `medir <transcript.jsonl> <saida.tsv>` e `passos <saida.tsv> <regex_inicio> <regex_fim>` —, só biblioteca padrão; a tarefa se lê por `despachar ([A-Z]+-T\d+[a-z]?\|TK-\d+)`; janela sem despacho imprime `por tarefa: n=0` e sai 0. Teste em `tests/test_custo_sessao.py`, com transcript sintético em `tmp_path`. `docs/audits/sonda-2026-09-28/` fica intocada, como registro da auditoria. A doutrina (o loop de plano recém-planejado abre em janela nova, com o plano gravado como único insumo; a janela de planejamento encerra no Marco 1) mora no Passo 1 da skill `scrum-master`. | F-13 (o protótipo quebra e fixa `AUF-T`); F-8 (a skill não liga o loop ao fim do planejamento); F-6. |
| DRF-7 | `R-02`: `despachar <ID>` grava o card, os handovers, o `show` do modelo e as âncoras (`DRF-8`) em `<pasta-do-plano>/despacho/<ID>.md` (plano em pasta) ou `docs/RDO/despacho/<ID>.md` (plano legado ou tíquete), e grava `ref` em `.claude/estado/tarefa-corrente.json`; o stdout passa a ser a linha `=== DESPACHO: <ID> — <título>`, o texto pronto do despacho ao executor (primeira linha `despacho: <P-id> <ID>` da `DRF-18`, o caminho do arquivo, a gramática da linha de retorno de F-8) e a linha `ref=<sha>`. `.gitignore` ganha `docs/plans/*/despacho/` e `docs/RDO/despacho/`. O Passo 4 da skill passa a invocar o executor com esse texto. | F-9; F-10 (o arquivo de despacho é projeção regenerável do card: versioná-lo duplicaria o card); F-6 (0,72k por despacho, medido). |
| DRF-8 | `R-03`: para cada `caminho:linha` citado em `Passos` ou `Contratos/classes` e para cada texto entre crases desses campos que é substring de uma linha de um arquivo dos `Arquivos-alvo`, o arquivo de despacho traz `caminho:linha-atual — <texto da linha>`; texto sem linha que o contenha sai `âncora ausente: <texto>`. O Passo 3 da skill deixa de mandar re-derivar âncoras à mão. | F-6 (23 turnos de âncora); F-8 (`:119-121`). |
| DRF-9 | `R-15`: `backlog_hook.py` não injeta nada quando o prompt, depois de `lstrip()`, começa por `<agent-message` ou por `[SYSTEM NOTIFICATION`. Testes em `tests/test_backlog_hook.py` (novo). | F-11; `tests/test_backlog.py` está na série de `backlog.py` (`DRF-7`, `DRF-8`, `DRF-20`, `DRF-29`), e o arquivo novo tira o hook dessa série. |
| DRF-10 | `R-24`: o hook reescreve só o segmento do pytest, envolvendo-o para emitir, depois da saída, a linha-marcador `__PYTEST_EXIT__=<exit>` (Bash: `{ <segmento>; echo "__PYTEST_EXIT__=$?"; } 2>&1 \| python "<filtro>"`; PowerShell: `& { <segmento>; "__PYTEST_EXIT__=$LASTEXITCODE" } 2>&1 \| python "<filtro>"`); `.claude/global/hooks/pytest_filter.py` consome o marcador, não o imprime e sai com esse exit. Testes em `tests/test_pytest_pretooluse.py` (novo): reescrita por texto e exit do filtro por subprocesso com stdin. A projeção a `~/.claude/hooks/` é ato do dono. | F-12 (o pipe só no segmento ainda devolveria o exit do filtro; só o filtro propagando o exit fecha a `R-24` nas duas ferramentas). |
| DRF-11 | `R-13`: no ramo texto, quando o conteúdo em `<ref>` não decodifica, `review_evidence.py` compara bytes em vez de cair; os dois `_load_rdo` do `--atribuir` (`:1079` e o de `:486`, alcançado por `:1094`) passam para dentro do `try`, e a ausência sai `review_evidence: FALHOU - rdo.py: módulo não encontrado em '<caminho>'`, exit 1; com `--out`, a medida ausente ao lado do `--out` é procurada em `caminhos.destino_medida`. | F-17. |
| DRF-12 | `R-14`: binário novo abre com a mesma marca `(arquivo novo — ausente em <ref>)` do texto novo; a lista por arquivo rotula `atribuição: registro da orquestração` os arquivos que o resumo põe em `Registro da orquestração`. | F-17 (dois rótulos para o mesmo fato). |
| DRF-13 | `R-09`, `R-10`, `R-11` em `card_check.py`: (i) bloco cercado com `--mundo depois` compara com o literal da linha `→` (`exit N` ou substring); `antes` segue com `Medido antes`. (ii) O par inline é procurado só depois do `→`, primeiro na forma delimitada por crase (`antes` seguido de literal entre crases, `,` ou `;` opcional, `depois` seguido de literal entre crases), que aceita `,`, `;` e `.` no literal; sem par com crase, vale a regex atual (legado). (iii) `git` entra nos programas aceitos só com o primeiro argumento em {`status`, `diff`, `show`, `ls-files`, `check-ignore`}; outro subcomando é recusado com mensagem que o nomeia. (iv) O token literal `<ref>` do comando é trocado pelo `ref` de `.claude/estado/tarefa-corrente.json` quando o `tarefa` do arquivo é o `--tarefa`; linha de `Verificação` marcada `(invariância)` sai `não medida (invariância)` em `--mundo antes`, sem falhar, e roda em `--mundo depois`. | F-14; F-16 (1 literal real com pontuação; 1 captura dentro do comando); a `R-27` depende de (iii) e (iv) (roteiro §1, divergência 4). |
| DRF-14 | `R-04` (mecânica da `DRF-1`): `modelo.py check` ganha `--so-vigente`, que julga só a `## 1` e não conta violação de card cuja operação citada só existe na `## 1A`; `despachar` passa a chamar o `check` com `--so-vigente`; o `check` sem a flag continua julgando as duas. Rota `modelador` com operação nova: o loop despacha o modelador e, em seguida, o planejador para a rodada, que escreve o card da operação nova, apensa o id à lista `tarefas:` dela na `## 1A` e o registra `blocked`, razão `dependencia`, nota `aguarda o aceite da versão <k> no marco`; a janela segue. | F-19; F-21; `DRF-1`. |
| DRF-15 | `R-06`: `modelo.py check` ganha a violação `V22 <ID> — texto de OP-<n> diverge da versão <v>`, comparando (espaços colapsados, pontas limpas) o texto copiado no campo `Operação do modelo` com o da operação na versão que o card cita (vigente; ou pendente, para operação que só existe na `## 1A`). A reescrita dos cards na promoção é da `DRF-17`. | F-19; auditoria reg. 36 e 37 (o `check` aprovou texto divergente). |
| DRF-16 | `R-07`: `_diff_fluxo` casa operações primeiro por texto idêntico, depois por número: `[+] OP-k` nova, `[=] OP-k (era OP-j)` renumerada, `[~] OP-k — textoV => textoP` alterada; `_diff_estado` lista `[+] <chave> — <final>` e `[-] <chave> — <final>` para chave de uma só versão. | F-19; auditoria reg. 34. |
| DRF-17 | `R-08` (e a parte de promoção da `R-06`): `encerrar.py marco --aceita-versao <k>` exige `--consultor "<linha de validação>"`, gravada verbatim na célula do marco ao lado do veredito do dono; roda o `modelo.py check` completo e recusa se houver violação `1A:`; promove mecanicamente — o conteúdo da `## 1A` passa à `## 1` com `situação: vigente`, a `## 1A` sai, o registro de versões ganha a linha da obsoleta com `Caiu pelo aceite da versão <k> em <data>`, e o campo `Operação do modelo` de cada card listado em `tarefas:` é reescrito com o número, o texto e o `precisa de:` da versão promovida; não imprime dossiê. Conflito (cabeçalho da `## 1A` com versão diferente de `k`, ou registro de versões sem vigente único) recusa com mensagem e imprime o dossiê `Ato: emenda` de hoje, para o modelador. A doutrina da promoção muda em `pantonic-model-designer.md` (promoção por comando; modelador só no conflito) e a forma da validação em `pantonic-consultant.md`. | F-20; F-21 (hoje a promoção custa uma instância de modelador, 55,0k, reg. 37). |
| DRF-18 | `R-16`: todo despacho de subagente abre com a linha `despacho: <P-id>[ <ID>]` (`<ID>` = tarefa `<PFX>-T<n>[a-z]` ou tíquete `TK-<n>`); `telemetria_hook.py` e `progresso_hook.py` a leem na primeira mensagem, antes de `tarefa-corrente.json` e antes do primeiro `P-<n>` citado; a formação do id da série não muda, só a fonte. `docs/telemetria.tsv` ganha a última coluna `agente` = nome do arquivo de `agent_transcript_path` sem extensão (`-` sem ele); o hook substitui a linha de mesmo `agente` em vez de apensar, e acrescenta `-` às linhas antigas na primeira escrita com o cabeçalho novo. O consultor é despachado com a linha do card em triagem. A regra da linha mora em `GOVERNANCA.md` §4.2 (residência da doutrina de telemetria). | F-26 (`agent_id` não confirmado no payload; `agent_transcript_path` já é lido e é único por agente). |
| DRF-19 | `R-17`: `prevoo.py` toma por caminho o token que termina em `/`; ou que contém `/` e cujo último segmento termina em `.<ext>` de 1 a 5 caracteres alfanuméricos; ou que, sem `/`, termina numa das nove extensões e não começa por `.`. Caminho inexistente sai `criar` (em vez de `não`) quando a mesma frase — texto entre fins de frase (`. ` ou quebra de linha) — traz antes dele um verbo de {`crie`, `criar`, `grave`, `gravar`, `escreva`, `escrever`, `gere`, `gerar`}, sem distinção de caixa; `criar` não derruba o exit 0. Sobre o pedido de F-22: 6 linhas `criar`, exit 0. | F-22 (o `.txt` solto e o `c.bin` fora da lista). |
| DRF-20 | `R-18`: `backlog.py drain` imprime em stderr `drain: aviso — a diretiva de priorização não cita nenhum id vivo nem <P-id>` quando, depois da drenagem, a diretiva não cita id vivo e não cita o plano drenado; o exit não muda. | F-23; auditoria reg. 16. |
| DRF-21 | `R-19`: `apensar_achado` acrescenta à linha da `AE-` a origem ` **Origem:** ` seguida de `laudo:<TAREFA>#<n>` entre crases (`<n>` = ordinal da linha na tabela `## Achado de processo` do laudo); o fechamento pula o achado cuja origem já aparece em alguma `AE-` do plano; a dedupe por texto continua como segundo teste. O consultor, ao registrar ou reescrever `AE-` a partir de achado de laudo, cita a mesma origem (`pantonic-consultant.md`). | F-25 (nenhuma `AE-` traz origem; a reescrita do consultor escapa da dedupe por texto). |
| DRF-22 | `R-20`: `encerrar.py tarefa` imprime, antes da linha final, `encerrar: B1 — achado de instrumento com falha: <texto>` para cada achado de laudo de alvo `instrumento` cujo texto contém, sem distinção de caixa, um de {`queda`, `traceback`, `exceção`, `excecao`, `exception`, `error`}; a condição da `B1` em `scrum-master/SKILL.md:300` ganha "ou linha `encerrar: B1 —` na saída do fechamento". | F-25 (a `B1` só na skill; o código não lê `escalar`). |
| DRF-23 | `R-21` (conteúdo da `DRF-2`): a tabela de profundidade da Fase 4 do `pantonic-planner.md` ganha a coluna "plano de até 5 operações, qualquer classe": itens 1 a 6 e 8 a 12 aplicam; 7 e 13 só com gramática ou tabela normativa no plano; 14 só com arquivo compartilhado tocado por dois cards, e o ensaio da contingência só quando a contingência escreve arquivo. | F-6; F-28 (tabela em `:249-252`). |
| DRF-24 | `R-22`: a Fase 3a do `pantonic-planner.md` passa a dizer que a `Restrição` do dossiê de autoria não pede caminho, número de linha nem nome de instrumento em célula descritiva do modelo (norma `TK-76` do modelador), e que residência vai à `## 2` e à `Camada e fronteira` do card. | F-28. |
| DRF-25 | `R-23`: a condução roda a `checar-versao-kit` antes de despachar o planejador e põe o resultado no dossiê; a Fase 5 do `pantonic-planner.md` deixa de mandar invocar skill e registra no cabeçalho a checagem que o dossiê traz. `Skill` não entra no `tools:` do planejador. O quando rodar mora na própria skill `checar-versao-kit`. | F-27 (o limite da plataforma para skill em subagente não se verifica pelo repositório; a condução já fez a checagem no `P-0754` e neste plano). |
| DRF-26 | `R-25`: o relatório de encerramento de janela no marco (`scrum-master/SKILL.md:333-339`) abre nomeando o que se entrega e o ato do dono que o pediu, na forma `"<entrega>", que você pediu em <data> ("<trecho verbatim do pedido, até 15 palavras>")`. | F-29; a forma da mensagem de marco é decisão técnica com default registrado (Fase 2 desta autoria). |
| DRF-27 | `R-26`: a Fase 5 do `pantonic-planner.md` fixa que o card cujo `antes` depende de antecessor mede o `antes` na cópia do ensaio com os antecessores aplicados (`card_check --root <cópia>`), e só o primeiro card de cada cadeia mede contra a árvore real; o valor publicado diz a árvore (`real` ou `cópia com <IDs> aplicados`). | Auditoria reg. 13. |
| DRF-28 | `R-27`: o item 14 da Fase 4 admite a operação de estado final igual: a linha discriminante é `git diff <ref> --numstat -- <alvo>` com saída vazia, marcada `(invariância)`, medida em `--mundo depois` (suporte na `DRF-13`, (iii) e (iv)). A mesma seção manda a rodada de replanejamento gravar a medida dos dois mundos de cada card reescrito (`R-05`, `DRF-30`). | Auditoria reg. 14 e 35; F-21. |
| DRF-29 | `R-28`: `backlog.py check` recusa plano cujo `**Prefixo das decisões:**` declarado é o mesmo declarado por outro plano de `docs/plans/`, com o código de violação `C-<n>` seguinte ao maior do vocabulário do `check` e a mensagem nomeando o plano dono (o de menor id); citação de prefixo alheio não é colisão. | F-24. |
| DRF-30 | `R-05`: `destino_medida` resolve a pasta do plano sob a raiz dada (`<raiz>/docs/plans/<nome da pasta do plano>/evidencia/`), e o nome do arquivo ganha o mundo: `<P-id>-<ID>-medida-<mundo>.json` (legado: `<raiz>/docs/RDO/evidencia/<id>-<ID>-medida-<mundo>.json`); `card_check --gravar` sem caminho grava com o mundo efetivo; `review_evidence` lê `-depois`, depois `-antes`, depois o nome sem mundo (os 20 arquivos de F-15). A rodada grava o `antes` na árvore real e o `depois` na cópia do ensaio, copiando o arquivo para a `evidencia/` real. | F-15; auditoria reg. 35. |
| DRF-31 | `R-30`: o curinga do alvo em `review_evidence.py` (`:558`, `:691`) passa a ter a semântica do glob de shell — `*` não atravessa `/`, `**/` casa zero ou mais pastas — por tradução própria para regex. | F-1 (Python 3.12: `PurePath.full_match` só existe no 3.13); F-17 (0 alvos com `*` vivos). |
| DRF-32 | `R-31`: as duas leituras do porcelain (`:351`, `:396`) passam a `-z`, com parse por `\0`. | F-17. |
| DRF-33 | `R-12`: para cada arquivo dos `Arquivos-alvo` sob `tests/` com nome `test_*.py`, a evidência traz as linhas removidas desde o `<ref>`; a dimensão `testes` da rubrica ganha, em `não conforme`, "asserção de teste existente removida sem que o card mande removê-la". | F-17; F-18. |
| DRF-34 | Revisão do `README.md` (G-README dever 2) como última tarefa: o `README.md` passa a citar `.claude/tools/custo_sessao.py` e `.claude/tools/card_check.py` na lista de instrumentos, e reflete as mudanças de comportamento das etapas A..E nas seções que já descrevem os instrumentos; `pwsh .claude/checks/check-readme.ps1` sai 0. | F-4. |
| DRF-35 | `R-03` (refino da `DRF-8`, na decomposição): a conferência de âncoras do `despachar` lê os campos `Passos` e `Contratos/classes` pelos bullets `- **<Rótulo>:**` de coluna 0; pula o trecho entre crases com menos de 4 caracteres, o já visto e o que é um dos `Arquivos-alvo`; o trecho `<caminho>:<n>` sai com a linha `n` de hoje; o outro trecho sai com a primeira linha que o contém no primeiro alvo, na ordem do card; sem linha, `âncora ausente: <trecho>`. | Trecho curto (`-z`, `*`) casa quase toda linha e afogaria o pacote; a primeira ocorrência basta para o executor achar o ponto sem grep (F-6: 23 turnos de âncora à mão). Consumida pela `RAF-T3`. |
| DRF-36 | `R-27` e `R-11` (forma mecânica da linha de invariância da `DRF-28`, na decomposição): a linha publicada é `git diff --exit-code <ref> --numstat -- <alvo>` → `exit 0`, marcada `(invariância)`; o `--exit-code` faz o `git diff` sair 1 quando o alvo mudou desde o recorte, e o `card_check` compara o exit. | Saída vazia não é literal comparável: o `card_check` compara `exit N` ou substring, e a substring vazia casa qualquer saída. Medido no ensaio da `RAF-T14`: com o alvo intacto a linha sai `exit 0`; com uma linha a mais no alvo, `exit 1` e a saída `1 0 <alvo>`. Consumida pela `RAF-T14` e pela `RAF-T17`. |
| DRF-37 | `R-04` e `R-06` (na decomposição): o card é julgado contra a versão que cita. Com a `## 1A` presente, a operação citada existe se existe na vigente ou na pendente (`V4`, com e sem `--so-vigente`), e o texto copiado vale se é o da operação de mesmo número em qualquer das duas (`V22`); o `--so-vigente` deixa de acrescentar as violações `1A: ` e a `V20`, e julga o resto da `## 1` como o `check` completo. | O card da operação nova (`DRF-14`) cita operação que só existe na `## 1A`, e o card antigo de uma operação renumerada copia o texto da vigente; sem a regra, o `check` completo que o fechamento de tarefa roda (`F-31`) recusaria toda tarefa da janela até o marco, e a `V22` recusaria o despacho. Consumida pelas `RAF-T19`, `RAF-T21` e `RAF-T23`. |
| DRF-38 | `R-08` (mecânica da `DRF-17`, na decomposição): a promoção roda em processo (`encerrar.py` carrega `modelo.py` por `_carregar`); é também conflito o registro de versões sem a linha `pendente` da versão aceita; a célula `por` da linha que cai ganha `; Caiu pelo aceite da versão <k> em <data>`; a `## 1` nova é o conteúdo da `## 1A` (sem `### 1.4` próprio) seguido do registro de versões da `## 1`; o campo `Operação do modelo` de cada card das listas `tarefas:` da pendente se reescreve com o número, o texto e o `precisa de:` (contratos da pendente) de cada operação que o lista; a linha do consultor entra na célula como `· consultor: "<linha>"`, com `|` escapado, e a forma dela é `valido a versão <k>: <razão em uma frase>` ou `não valido a versão <k>: <razão em uma frase>`. | O `modelo.py check` carrega o `backlog.py` da raiz dada, e a raiz dos testes não o tem; a forma do registro segue a do modelador (`pantonic-model-designer.md`, ato **Emenda**). Medido no ensaio da `RAF-T23`: o plano promovido sai `modelo: OK — 2 operações, 3 objetos, 3 propriedades, 2 tarefas, versão 2`. Consumida pelas `RAF-T23` e `RAF-T26`. |
| DRF-39 | `R-16` (na decomposição): a coluna `agente` e a migração da série moram no escritor `.claude/tools/telemetria.py`, que o hook chama com `--agente`: `gravar_por_agente` põe `agente` no cabeçalho e `-` nas linhas antigas e substitui a linha do mesmo agente; `append_row` sem agente põe `-` na série já migrada; a série sem a coluna segue de oito colunas. | O `encerrar.py` também grava na série pelo `telemetria.py` (trio por argumento e `--nao-medido`); migrar só no hook deixaria linhas de oito colunas numa série de nove, que o `_ler_tsv` do `encerrar.py` descarta (`F-31`). Medido no ensaio da `RAF-T31`: `tests/test_encerrar.py` passa sem mudança; três asserções de `tests/test_telemetria_hook.py` se reescrevem. Consumida pelas `RAF-T31` e `RAF-T33`. |
| DRF-40 | Revisão do `README.md` (refino da `DRF-34`, na decomposição): os comandos do kit que o guia cita são onze — os dez que `F-4` conferiu (`card_check.py`, `modelo.py`, `encerrar.py`, `backlog.py`, `review_evidence.py`, `backlog_hook.py`, `telemetria_hook.py`, `progresso_hook.py`, `prevoo.py`, `materializar.py`) e o `custo_sessao.py`; o `telemetria_hook.py` entra na seção de telemetria do guia; o que as etapas mudaram entra por troca de trecho nas seções que já descrevem cada instrumento (§6, §8.1, §9, §11 e §12 do guia); a série `docs/telemetria.tsv` deixa de ser descrita como append-only. | O estado inicial da propriedade na `### 1.3` conta dois comandos sem menção, que são os dois de `F-4` (`card_check.py` e `telemetria_hook.py`), e a `DRF-34` nomeava só o primeiro; a série passa a substituir a linha do mesmo agente (`DRF-18`), o que desmente o append-only. Os demais módulos de `.claude/tools/` ficam fora (§7). Consumida pela `RAF-T40`. |
| DRF-41 | `R-25` (na decomposição): a linha de abertura de marco mora numa subseção nova, `### Quando a janela para num marco`, do `## Relatório de encerramento` da skill `scrum-master`, e vem antes da saída do `modelo.py show`; a parada de marco se reconhece pela próxima tarefa `blocked` à espera do veredito de um marco (nota `Marco <m>: …`, `DRF-5`); a entrega é a célula *o que o dono lê* da linha do marco na tabela de marcos do plano (plano sem essa tabela: o título do plano; refinada pela `DRF-75`: o trecho da célula antes dos dois-pontos, e o título do plano quando a célula não nomeia etapa), e o pedido é a data e um trecho verbatim do ato do dono na §0. | O relatório já abre pela saída do `show`, exceção declarada; a linha nova vem antes para o dono ler primeiro o que recebe e de onde veio, e a tabela de marcos é onde o plano já nomeia cada entrega. Consumida pela `RAF-T39`. |
| DRF-42 | `R-23` (na decomposição): o planejador registra a checagem no campo `**Checagem de versão do kit:**` do cabeçalho, com `não recebida no pedido` quando o pedido não a traz; o `description` do frontmatter da skill `checar-versao-kit` e a skill `diario-de-obras` não mudam, e a própria `checar-versao-kit` diz que o plano registrado sem planejador roda a checagem no registro. | O cabeçalho deste plano já usa o campo; o `description` é espelhado no índice derivado `.claude/README.md`, que o `kit_check.ps1 -Mode check-drift` compara; a regra do momento mora só na skill (`DRF-25`). Consumida pela `RAF-T38`. |
| DRF-43 | (consultor, acionamento 1, `AE-122`) O campo `- **Janela:**` que a `RAF-T1` gravou no Passo 1 da skill `scrum-master` sobe à coluna 0, campo irmão de `Gatilho`/`Entrada`/`Ação`/`Saída`, pelo card corretivo `RAF-T1a` (mesma `OP-1`); a `RAF-T1` fica `done` e o texto do card fica como executado. O planejador não ganha regra nova de recuo: os demais cards de bloco já dizem "perde o recuo deste card", e o que falhou foi a `Verificação 1` da `RAF-T1`, que contou o literal sem a linha anterior e por isso não discriminou a coluna — critério já escrito no item 13(iii) da Fase 4 do planejador. | Laudo da `RAF-T1` (ressalva 88); medida: `.claude/skills/scrum-master/SKILL.md:43-47` com recuo 3/5; as outras instruções de bloco da §5 dizem "perde o recuo deste card" (18 ocorrências medidas; só a `RAF-T1` fixava "os dois espaços"). |
| DRF-44 | (consultor, acionamento 1, `AE-121`) O vermelho do `dead_code.py` sobre `docs/audits/sonda-2026-09-28/passos.py` não ganha card nem tíquete neste plano: a sonda fica como registro da auditoria (§7), a §8 item 5 já prevê o gate vermelho por arquivo que o plano não toca, e a restrição de cada card de código admite esse achado nominalmente, de modo que o revisor o reconcilia pela linha do card. A pergunta de fundo — se `.py` sob `docs/` entra na varredura "de produção" do `dead_code.py` — segue com rota "auditoria final". | Diretiva do dono de 2026-09-26, item (2), no cabeçalho do diário: "nenhum card nem tíquete novo por ajuste", achado novo vira `AE-<n>` com rota "auditoria final"; mudar o escopo de um gate do kit está fora das operações da §1. |
| DRF-45 | (consultor, acionamento 2, `AE-125`) A conferência de âncoras do `despachar` (refino da `DRF-35`, que refina a `DRF-8`) lê o trecho entre crases como *code span* do Markdown (N crases abrem, N fecham); o trecho `<caminho>:<n>` aceita arquivo sem extensão e caminho que só termina um dos `Arquivos-alvo`; e marca `âncora ausente` só a linha citada que não existe e o texto citado logo depois dela (separado por `—` ou `:`, a convenção do `card_check`) que não está no arquivo. O outro trecho sem linha nos alvos não entra no pacote: não é citação de linha. Card corretivo `RAF-T3a` (mesma `OP-3`); `RAF-T4` passa a depender dele, porque a doutrina manda não reconferir o que o pacote traz. | Laudo da `RAF-T3` (ressalva 91); medida em cópia sobre os 41 cards do `P-0755`: regra da `DRF-35`, 1066 linhas e 573 `âncora ausente`; regra nova, 501 e 0. O estado final da §1.3 ("marca como ausente o texto que não está mais no arquivo") pede exatamente isto: o comando e o nome novo nunca estiveram no arquivo; a mudança é de mecânica, sem drift do modelo. |
| DRF-46 | (consultor, acionamento 3, `AE-126`) A regra da `RAF-T4` (âncora conferida no pacote, texto pronto repassado sem copiar o card) fecha nos dois pontos que o card não alcançou: o item 3 do Gate de delegação da skill `passagem-de-bastao`, residência única do gate que o Passo 3 da `scrum-master` manda rodar antes do `despachar`, passa a mandar re-derivar âncora só no card de tíquete (despachado à mão, sem pacote); e a `Entrada` do Passo 4 passa a ser o texto pronto do `despachar`. No mesmo ato, a `scrum-master` volta ao fim de linha LF que o `.gitattributes` declara. Card corretivo `RAF-T4a` (mesma `OP-4`). Sem drift: a `OP-4` já diz "sem reconferir à mão as âncoras do card". | Laudo da `RAF-T4` (ressalva 88): a Camada da `RAF-T4` afirmou "nenhum outro arquivo a repete" sem varredura; varredura do consultor (2026-09-28) de "re-derivad" e "copiado do plano" em `.claude/`, `README.md`, `GOVERNANCA.md` e `docs/*.md` acha só os dois pontos vivos (o resto é diário e histórico, e a herança de contexto da `passagem-de-bastao`, que cita precedente sem mandar re-derivar). Ensaio em cópia: Verificações 1-3 antes `gate=1-0`, `entrada=1-0`, `linhas=306-445 cr=0-445`; depois `gate=0-1`, `entrada=0-1`, `linhas=306-445 cr=0-0`. |
| DRF-47 | (consultor, acionamento 4, `AE-130`) O hook do filtro do pytest recusa por pipe só o pipe simples (`|` que não é metade de `||`) e o redirecionamento, e o pré-filtro `PYTEST_RE` acha o pytest também depois de `||` e de quebra de linha: sem isso o separador `||` e a quebra de linha que a `RAF-T6` pôs em `dividir_segmentos()` nunca chegam a `reescrever()`. A `RAF-T6` fica `done` e o texto do card fica como executado. Card corretivo `RAF-T6a` (mesma `OP-6`), dentro da etapa A, antes do Marco 2. Sem drift: a `OP-6` já diz "mesmo quando o comando encadeia outros passos depois deles". | Laudo da `RAF-T6` (ressalva 91): o card manteve "as cinco condições de passthrough de `main()` inalterados" e mandou reconhecer `||` como separador. Medida do consultor (2026-09-28, hook da árvore): `pytest -q || echo falhou`, `false || pytest -q` e `cd x`+quebra+`pytest -q` devolvem `{}`; `cd x && pytest -q` é reescrito. Ensaio em cópia: os dois TF novos falham antes (`2 failed, 6 passed`) e passam depois (`8 passed`); nós da Verificação antes `exit 4` (árvore real), depois `exit 0`; no Bash, o `||` depois do bloco filtrado dispara com o exit 1 de um teste que falha. |
| DRF-48 | (consultor, acionamento 5, `AE-132`, `AE-133`) Edição de arquivo-alvo que o sistema de permissão nega não se refaz por outra ferramenta nem por outro canal: o executor faz as demais edições do card, para e sinaliza `blocked` razão `ferramenta` com o caminho e o texto exato da edição negada na linha de retorno, e quem conduz junta as negadas num comando PowerShell único que entrega ao dono no fim da sessão. Invariante 13 da §4 e contingência inline de `RAF-T7` a `RAF-T40`. A emenda da `GOVERNANCA.md` §7 (`AE-133`) não vira card nem tíquete: rota auditoria final. Sem drift. | Ato do dono de 2026-09-29 ("O que você conseguir editar, edite. O que não conseguir, junte tudo e me passe no final o comando powershell"); a `RAF-T6a` refez por `Edit` a mudança negada por `python -c` no hook; diretiva de 2026-09-26 item (2) para a doutrina do kit. |
| DRF-49 | (consultor, acionamento 6, `AE-135`) No ramo em que o conteúdo do `ref` não se lê como texto e o de hoje se lê, os bytes nunca são iguais (os de hoje decodificam em UTF-8, os do `ref` não): o retorno de bytes iguais da regra 3 da `RAF-T7` é inalcançável e a comparação da regra 2 é sempre verdadeira. As duas comparações saem pelo card corretivo `RAF-T7a` (`OP-7`), sem teste novo (inspeção mecânica, item 12(ii) da Fase 4 do planejador); `RAF-T8` passa a depender dele (mesma função). A decisão não fica com a `RAF-T8`, para onde o laudo a roteou: o ramo é matéria da `OP-7`, e erro conhecido não se adia. Sem drift. | Laudo da `RAF-T7` (ressalva 91); ensaio do consultor em cópia (2026-09-29): ocorrências de `_bytes_do_ref(` 5 antes e 3 depois, `tests/test_review_evidence.py` `83 passed` antes e depois. |
| DRF-50 | (consultor, acionamento 7, `AE-137`) A frase da `docs/RUBRICA_DE_REVISAO.md` §3 que conta os rótulos da seção `## Arquivos tocados` (`da entrega` ou `alheio`) passa a nomear o terceiro, `registro da orquestração`, que a `RAF-T8` criou: a `RAF-T8` não pôs a frase nos `Arquivos-alvo` (item 12(i) da Fase 4 do planejador, a frase que conta o conjunto fecha no mesmo ato). Card corretivo `RAF-T8a` (`OP-8`), só redação; `RAF-T12` passa a depender dele (mesmo arquivo). Erro inequívoco: não se adia à auditoria final (o corretivo `T<n>a` é reparo do plano aprovado, §3 do cenário). Sem drift: a `OP-8` já diz que a lista e o resumo usam o mesmo nome. | Laudo da `RAF-T8` (ressalva 91); ensaio do consultor em cópia (2026-09-29): Verificação 1 `exit 1` (`arquivos=1-0`) antes e `exit 0` (`arquivos=0-1`) depois, linha mais longa 99 caracteres. |
| DRF-51 | (consultor, acionamento 8, `AE-140`) O docstring de `test_tf_alvo_com_curinga_casa_os_tocados` (`tests/test_review_evidence.py`) passa a nomear `_casa_curinga`: a `RAF-T9` tirou o `fnmatch` e congelou as linhas existentes do arquivo, e o docstring ficou dizendo que o curinga casa "por `fnmatch`". Card corretivo `RAF-T9a` (`OP-9`), só redação; `RAF-T10` passa a depender dele (mesmo arquivo). A rota do laudo (o próximo card que já edita o arquivo) não se segue: o texto é matéria da `OP-9`, e erro inequívoco não se adia a card de outra operação. Os "hoje o `fnmatch`" dos dois testes `glob_estrela` ficam: nomeiam a regra concorrente na data da autoria, convenção dos docstrings de teste do kit. Sem drift. | Laudo da `RAF-T9` (ressalva 91); ensaio do consultor em cópia (2026-09-29): Verificação 1 `exit 1` (`docstring=1-0`) antes e `exit 0` (`docstring=0-1`) depois, linha mais longa 94 caracteres, `tests/test_review_evidence.py` `88 passed` depois. |
| DRF-52 | (consultor, acionamento 9, `AE-142`..`AE-145`) A `DRF-32` se estende às duas leituras do `git diff <ref>` (`--name-only` e `--name-status`) em `review_evidence.py`, que passam a uma só, `git diff <ref> --name-status -z`, com parse por NUL e o caminho novo como chave da renomeação; a gramática de caminho do alvo (`_CAMINHO_RE`) aceita letra acentuada; os `_git` passa `-c core.quotepath=false` a todo `git` (o resumo `--stat` e o cabeçalho do trecho mostravam o nome em escape octal); os docstrings de `coletar_arquivos_tocados` e `coletar_estado_git` deixam de descrever o nome em escape octal e a leitura sem `-z`. Card corretivo `RAF-T10a` (`OP-10`, `tarefas:` da §1 e da §1A atualizadas); `RAF-T11` passa a depender dele (mesmo arquivo). `-z` e não `core.quotepath=false`: é o que a `DRF-32` já fixou, e cobre também aspas e tabulação no nome. O texto da `RAF-T10` (`done`, `Não fazer` e `Fora do escopo` que excluíam o `git diff`) fica como executado. O drift já tem a versão 2 pendente do modelador (estado final da propriedade `dossiê de evidência.caminho acentuado`); a `F-17` fica como foi medida na autoria, e a medida nova mora nesta linha. | Laudo da `RAF-T10` (ressalva 91) e o seu dossiê `Ato de modelo` de `conflito`; ensaio do consultor em cópia (2026-09-29): com `core.quotepath` ligado, o rastreado `ação.md` commitado depois do `ref` sai `"a\303\247\303\243o.md"` em `coletar_arquivos_tocados`, e `extrair_arquivos_alvo` descarta `docs/ação.md`, e o resumo `--stat` e o cabeçalho do trecho saem com o nome em escape octal; os dois TF falham e o TR passa antes (`2 failed, 1 passed`); depois, Verificação 1 `exit 5` → `exit 0`, Verificação 2 `exit 1` (`diff=1-2-0-0-0`) → `exit 0` (`diff=0-0-1-1-1`), `tests/test_review_evidence.py` `93 passed`; sem o item do `_git`, o TF do arquivo rastreado cai no cabeçalho do trecho. |
| DRF-53 | (consultor, acionamento 10, `AE-149`) A seção `## Linhas removidas dos testes` (`RAF-T11`) tem duas lacunas de uma regra entregue como escrita: alvo curinga ou diretório que cobre arquivo de teste é pulado, e a seção diz que não há arquivo de teste entre os alvos; e o filtro de `---` apaga, junto com o cabeçalho, a linha removida cujo conteúdo começa por `--`. Corretivo `RAF-T11a` (`OP-11`): expansão de `montar_trechos` contra os tocados, uma chave por arquivo, e só contam as linhas depois do primeiro `@@` (o que também tira da contagem o conteúdo integral de arquivo novo sem `ref`). `RAF-T12` e `RAF-T15` passam a depender dele. Sem drift: a `OP-11` já diz "cada arquivo de teste entre os alvos". Não é o caso vivo que conta (`F-17`: zero alvo curinga no corpus); é erro inequívoco, e erro não se adia. |
| DRF-54 | (consultor, acionamento 11, `AE-151`) O critério da `RAF-T12` (asserção removida sem ordem do card) é juízo — cada linha da seção `## Linhas removidas dos testes` confrontada com o card —, mas o bullet `Fonte da evidência` da dimensão `testes` seguiu "mecânica", contra a §3 da rubrica, que manda declarar a fonte mista. Corretivo `RAF-T12a` (`OP-12`): a dimensão passa a mista (presença dos testes e exit da suíte mecânicos e travados; juízo sobre as linhas removidas). A trava não muda: `veredito_testes` lê o exit e o `rdo.py` só recusa `conforme` contra vermelho (`DA-7`), então o juízo já é livre. No mesmo card, as sete citações da rubrica por número de linha em `review_evidence.py` e as três dos docstrings do seu teste, que apontavam a dimensão errada, passam a citar `§4` (erro inequívoco achado na triagem; não se adia). `RAF-T15` passa a depender dele (mesmo arquivo). Sem drift: a `OP-12` já diz o critério. A rota do laudo (triar junto da `RAF-T17`) não se seguiu: a `RAF-T17` é do planejador e não toca a rubrica. |
| DRF-55 | (consultor, acionamento 12, `AE-155`) A `RAF-T13` entregou a regra 1 (no mundo `depois` a forma 8.1 compara com o literal do esperado) e trocou só o docstring de `verificar_tarefa`, o único texto que a regra 3 do card nomeava; o docstring do módulo de `card_check.py` (linhas 5-7) e o `help` de `--mundo` seguiram dizendo que a conferência compara com o `Medido antes` e que o mundo só vale na forma inline. Corretivo `RAF-T13a` (`OP-13`, redação): os dois textos passam a dizer a regra 1; `RAF-T14` passa a depender dele (mesmo arquivo). `AE-156` (valor de item de teste que o card não fixou) e `AE-157` (restrição de `card_check` sobre `RAF-T1`..`RAF-T18` inalcançável para o próprio card no mundo `antes`) são defeitos de autoria da `RAF-T13`, que fica como executada: nenhum card aberto repete a restrição, e o valor escolhido não muda o mundo que o teste exercita. `AE-154` reincide a `DRF-44`. | Erro inequívoco no texto de um instrumento que o plano entregou, matéria da `OP-13`; não se adia para a `RAF-T14`, que é de outra recomendação. Sem drift: a `OP-13` já diz a regra. |
| DRF-56 | (consultor, acionamento 12, `AE-158`) Na execução, nenhum comando `git` que escreve no índice, na árvore ou nas referências roda na árvore do repositório (§4 invariante 14): a prova do mundo `antes` sai da ordem dos Passos (teste vermelho antes da regra) ou de cópia fora do repositório, e teste que precisa de `git` que escreve monta o próprio repositório em `tmp_path`. A restrição de escopo dos 27 cards abertos (`RAF-T14`..`RAF-T40`) e a do `RAF-T13a` passam a nomear a regra. A guarda mecânica (hook `PreToolUse` que recusa `git stash`, `reset`, `checkout --`, `restore` na execução) fica com rota auditoria final, pela diretiva de 2026-09-26. | A `RAF-T13` rodou `git stash` e `git stash pop` na árvore que carrega trabalho não commitado de vários planos; a restrição "nada fora deles se reverte" não foi lida como cobrindo o `stash`, e só os cards do `review_evidence.py` nomeavam o comando. Sem drift. |
| DRF-57 | (consultor, acionamento 13, `AE-160`..`AE-162`) O Passo 2 da `RAF-T14` ("os quatro TF falham e o TR passa") era inalcançável: o TR `test_tr_ref_do_despacho_de_outra_tarefa_falha` confere a mensagem que só a regra 4 cria. Defeito de autoria da `RAF-T14` (`done`, fica como executada); nenhum card aberto o repete: os dez cards abertos cujo Passo manda o TR passar antes (`RAF-T15`, `RAF-T20`..`RAF-T22`, `RAF-T27`..`RAF-T32`) conferem literal que o código de hoje já produz (medido). Autoria futura: TR que o Passo manda passar antes da regra só confere saída que o código de hoje já produz; TR que confere mensagem nova entra entre os que falham. O `AE-162` (a checagem do vermelho, prova do `antes` da `DRF-56`, não deixa rastro mecânico no dossiê) é lacuna de doutrina e de instrumento, não erro do plano: rota auditoria final, pela diretiva de 2026-09-26. O `AE-160` reincide a `DRF-44`. | Laudo da `RAF-T14` (ressalva 91): o revisor reproduziu fora da árvore `5 failed` com o `card_check.py` do `ref`. Medida do consultor (2026-09-29): `modelo.py` já tem `[~] OP-<n> — <texto> => <texto>`, `backlog.py` já tem `despachar: recusado — {gate}: {razao}`, `progresso_hook.py` já tem as frases do revisor e do planejador; o `prevoo.py` de hoje dá `notas.md \| sim \| notas.md` com `exit 0` e `docs/x.md \| não \| —` com `exit 1` (os dois TR da `RAF-T27`). A `RAF-T23` manda os cinco falharem. Sem drift. |
| DRF-58 | (consultor, acionamento 14, Marco 3) O consultor valida a versão 2 pendente do modelo (§1A, ato de `conflito` do modelador sobre a `OP-10`): a diferença para a versão 1 é só a linha `dossiê de evidência.caminho acentuado` da §1.3 (estado inicial passa a descrever também o arquivo já rastreado; estado final passa a "o arquivo acentuado, novo ou já rastreado, chega com a sua diferença e com um nome só, como qualquer outro"); objetos, fluxo, texto da `OP-10` e contagens (40 operações, 61 propriedades) iguais. O estado final novo cabe no texto da `OP-10` ("o nome de arquivo acentuado que o versionador lista") e no lastro `R-31`, não muda escopo nem objetivo do plano, e está entregue pela `RAF-T10a` (`done`). A v2 sobe ao dono para aceitar ou recusar no Marco 3. | Medida do consultor (2026-09-29, árvore no Marco 3): `modelo.py check --plano` exit 0 com a §1A julgada (nenhuma violação `1A:`); Verificações 1 e 2 da `RAF-T10a` `exit 0` (`3 passed`; `diff=0-0-1-1-1`); `-k acento` `5 passed`; `tests/test_review_evidence.py` `102 passed`. O `modelo.py show --drift` só lista o estado final: a mudança do estado inicial não aparece nele. |
| DRF-59 | (consultor, acionamento 15, `AE-169`) A regra 3 da `RAF-T19` (`validar` com `so_vigente=True` não emite a `V20`) ganha o caso que a distingue: pendente em versão 3 contra a vigente 1, o `check --so-vigente` sai 0 sem a `V20` e o `check` sem a flag sai 1 com ela. Card `RAF-T19a` (`OP-19`; `tarefas:` da §1 e da §1A; §6 linha C); `RAF-T21` passa a depender dele (mesmo arquivo de teste). A rota alternativa do laudo ("ou na `RAF-T20`") não se seguiu: a `RAF-T20` é da `OP-20` e não toca `tests/test_modelo.py`. O `AE-168` reincide a `DRF-44`. Sem drift. Autoria futura: card que põe guarda condicional numa violação dita o caso de teste em que a violação dispara. | Laudo da `RAF-T19` (ressalva 91). Medida do consultor em cópia (2026-09-29): `-k "so_vigente and fora_de_sequencia"` sai `exit 5` na árvore real e `exit 0` (`2 passed`) com os testes; sem a linha `and not so_vigente` de `validar`, o TF sai `1 failed`; `tests/test_modelo.py` `40 passed`. |
| DRF-60 | (consultor, acionamento 15, `AE-170`) O consultor valida a versão 3 pendente do modelo (§1A, ato de `conflito` do modelador sobre a `OP-19`): a diferença para a versão 2 é só o contrato do objeto `conferência do modelo` (mantém o que já julga, com uma só mudança: enquanto houver versão pendente, o card que cita operação que só ela tem deixa de ser recusado) e a linha `conferência do modelo.versões julgadas` da §1.3 (inicial e final); objetos, fluxo, textos das operações e contagens (40 operações, 61 propriedades) iguais. A mudança é a `DRF-37`, decidida na decomposição e entregue pela regra 4 da `RAF-T19`; cabe no texto da `OP-19`, sem mudança de escopo. Os cards que copiam o contrato da versão 2 (`precisa de:` das `RAF-T20`..`RAF-T25` e da `RAF-T40`; `Camada e fronteira` das `RAF-T21` e `RAF-T22`) ficam: copiam a vigente, válida até o Marco 4 (`DRF-37`); a promoção reescreve o `Operação do modelo` dos cards das listas `tarefas:` (`DRF-38`, `RAF-T23`), e as duas `Camada e fronteira` executam antes do marco, sob a vigente, sem que a mudança da versão 3 pese nelas (acrescentam violação ou saída sem tirar nada do que o `check` já julga). O texto da `RAF-T19` (`done`) fica como executado. Recusada pelo dono, o plano retroage ao ponto do drift (`GOVERNANCA.md` §3.2): o corretivo da `OP-19` que tira a regra 4 da `RAF-T19` (`numeros_pendente`), com a `DRF-37`, volta a este consultor. | Laudo da `RAF-T19` (ressalva 91) e o ato do modelador. Medida do consultor (2026-09-29): a diferença entre a §1 e a §1A é o cabeçalho, a linha do estado do modelo, a linha do objeto e a linha da §1.3 (e o registro de versões, só na §1); `modelo.py check --plano` e `check --so-vigente --plano` saem `exit 0` (`versão 2`, 51 tarefas antes do `RAF-T19a`). |
| DRF-61 | (consultor, acionamento 16, `RAF-T21` `blocked` razão `premissa`) A regra 2 da `RAF-T21` julga o texto copiado contra **todos** os textos de mesmo número na vigente e, havendo, na pendente: número duplicado numa versão, que já sai `V11`, conta cada um dos textos. O dicionário de um texto por número (o último vence) acusava `V22 EX2-T3` em `tests/fixtures/modelo/plano-invalido-2.md`, cujo `EX2-T3` copia fielmente o primeiro dos dois `OP-3`, e derrubava `test_tf_check_invalido_lista_catorze_violacoes_na_ordem` (5 violações onde o teste espera 4). Defeito de autoria do card: a regra não fixava o identificador duplicado, e o ensaio não rodou a suíte contra as fixtures. O teste existente fica intocado e passa a ser o TR do caso; o redespacho não consome a retentativa. Sem drift: a `OP-21` pede recusar só o texto que diverge da versão citada. | Evidência do executor (`1 failed`, `592 passed`; `-k texto_divergente` `3 passed`; `check` sobre o `P-0754` `exit 0`). Medida do consultor (2026-09-29, cópia em `%TEMP%`): com a regra por conjunto, `tests/test_modelo.py` `43 passed` (árvore real `1 failed, 42 passed`); `check` sobre o `P-0754` e o `P-0755` `exit 0`; linhas `V22` dos quatro planos encerrados iguais às da restrição (1, 7, 5, 1). |
| DRF-62 | (consultor, acionamento 17, `AE-176`) O comando do marco reconhece a `## 1A` por uma regra só, a do `modelo.py` (`_localizar_secao`: linha igual a `_HEADING_PENDENTE`): a pré-checagem de `gravar_marco` troca o prefixo de `_MARCO_VERSAO_PENDENTE_RE` pela igualdade exata, e a constante sai. O cabeçalho com texto a mais passa a sair com `marco: plano sem versão pendente (## 1A)` (exit 1, plano igual), em `--aceita-versao` e em `--recusa-versao`, em vez de `AttributeError` em `_checar_promocao`. A alternativa do laudo (nova razão de conflito em `_checar_promocao`) não se seguiu: deixaria duas regras para o mesmo cabeçalho no arquivo e pediria o dossiê ao modelador por um cabeçalho que o `modelo.py` nem lê. Card `RAF-T23a` (`OP-23`; `tarefas:` da §1 e da §1A; §6 linha C); `RAF-T30` depende dele (mesmo arquivo). A `RAF-T23` (`done`) fica como executada. Sem drift: a §1.3 já pede que o conflito recuse antes de escrever. Autoria futura: card que acrescenta leitura de seção a um instrumento confere a regra que as checagens já existentes do mesmo verbo usam para a mesma seção. | Laudo da `RAF-T23` (ressalva 91). Medida do consultor (2026-09-29, cópia em `%TEMP%`): com o teste do card e sem a regra, `1 failed` (`AttributeError: 'NoneType' object has no attribute 'versao'`); com a regra, `1 passed` e `tests/test_encerrar.py` `43 passed`; árvore real `-k cabecalho_1a` `exit 5`. O cabeçalho da `## 1A` do `P-0755` é o exato (o Marco 4 não muda). |
| DRF-63 | (consultor, acionamento 18, `AE-178`) O card da operação nova que a rodada registra `blocked`, nota `aguarda o aceite da versão <k> no marco` (`DRF-14`, `RAF-T25`), ganha destino no marco pela doutrina de quem conduz, no trecho da skill `scrum-master` que a `RAF-T24` escreveu: com `--aceita-versao <k>`, passa a `ready` (`backlog.py status <ID> ready`); com `--recusa-versao <k>`, o consultor, a quem o caso já volta, o tira do plano com a linha do `estado.tsv` (`cancelled` não basta: o `V4` julga o card com qualquer status). Card `RAF-T24a` (`OP-24`; `tarefas:` da §1 e da §1A; §6 linhas C e D); `RAF-T27` depende dele. A saída automática pelo `encerrar.py marco` não se seguiu: mudaria o estado final de `fechamento.promoção da versão aceita` (drift) e o desenho da `DRF-5`, em que só a condução passa a `ready` a primeira tarefa da etapa depois do `go`; o que a condução fez à mão nos Marcos 2 e 3 (`RAF-T7`, `RAF-T19`) é a `DRF-5` como escrita, não defeito. A mecanização das duas saídas fica com rota auditoria final (diretiva de 2026-09-26). Sem drift. | Laudo da `RAF-T25` (ressalva 90). Lido: `gravar_marco` só transita a linha do plano, no Marco 1 `go`; o `validar` do `modelo.py` emite o `V4` sem olhar o status do card. Medido: a Verificação 1 do `RAF-T24a` sai `destino=0-0 cr=0` na árvore e `destino=1-1 cr=0` na cópia com a troca. |
| DRF-64 | (consultor, acionamento 19, `AE-180`) O campo `Devolver` do dossiê `Ato: emenda` que o comando do marco imprime passa a vir de quem chama `_dossie_emenda`: no conflito da promoção, `a ## 1 e a ## 1A acertadas, com o registro de versões, para o comando do marco rodar de novo.`; na recusa, `a seção ## 1 depois do ato, com o registro de versões sem a linha da versão recusada, e o plano sem a ## 1A.` O texto único de hoje (`a seção ## 1 depois do ato e a linha nova do registro de versões`) pede no conflito o que o próprio comando faz na promoção e, na recusa, uma linha que não entra (a `## 1A` e a linha dela saem, `GOVERNANCA.md` §3.2): erro nos dois ramos, e o da recusa, achado na triagem, vem do `AF-T12` e sai no mesmo card, porque é a mesma linha. O lado que se alinha é o comando, não a doutrina: no conflito o ato não aconteceu, e o modelador acerta o que está para o comando rodar de novo (`R-08`). No modelador, a frase do conflito passa a nomear o quarto conflito que `_checar_promocao` já tem (`o plano não tem a ## 1`) e a devolver o que o dossiê pede. Cards `RAF-T23b` (`OP-23`) e `RAF-T26a` (`OP-26`, depois da `RAF-T23b`); `tarefas:` da §1 e da §1A; §6 linhas C e D; `RAF-T27` depende de `RAF-T26a`. A `RAF-T26` (`done`) fica como executada. Sem drift: a §1.3 pede, no conflito, que o comando recuse e prepare o pedido ao modelador, e que o modelador só seja chamado nele. Autoria futura: doutrina que descreve a saída de um instrumento confere cada frase contra o código que a imprime, inclusive a enumeração dos casos. | Laudo da `RAF-T26` (ressalva 90). Medida do consultor (2026-09-29, cópia em `%TEMP%`): árvore real `-k devolver` `exit 5`; com os dois testes e sem a regra `2 failed`; com a regra `2 passed`, `tests/test_encerrar.py` `45 passed`; modelador `conflito=1-0` → `conflito=0-1`, `tests/test_doutrina_unidade.py` `8 passed`. |
| DRF-65 | (consultor, acionamento 20, Marco 4) A linha de validação da versão 3 para `encerrar.py marco --consultor` (a `DRF-60` validou sem a forma da linha): versão 3 validada contra a árvore de então — diferença só no contrato de `conferência do modelo` e na linha `versões julgadas` da §1.3 (`DRF-37`, `OP-19`), `numeros_pendente` no `modelo.py`, `test_modelo.py` `46 passed`, `modelo.py check --plano` e `--so-vigente` `exit 0`; a linha está gravada na célula do Marco 4. Linha restaurada no acionamento 28: o cenário a dava por escrita nesta seção e ela faltava. | `DRF-60`; `DRF-37`; `R-08`. |
| DRF-66 | (consultor, acionamento 21, `AE-183`) O item `caminhos` do docstring do módulo de `.claude/tools/prevoo.py` (linhas 13-15) passa a dizer as três regras da `RAF-T27`: caminho é o token terminado em `/`, o que tem `/` e extensão curta no último segmento, ou o nome solto com uma das nove extensões que não começa por `.`; o que não existe sai `criar` quando a mesma frase o traz depois de um verbo de criação, e `criar` não derruba o exit 0; o `não` faz o exit ser 1. A `RAF-T27` (`done`, fica como executada) nomeou só os docstrings das funções; defeito de autoria, que o laudo não deixou o executor decidir. Card `RAF-T27a` (`OP-27`, redação; `tarefas:` da §1; §6 linha D; fecha a etapa com `RAF-T29`, `RAF-T34` e `RAF-T35`); nenhum card aberto edita o `prevoo.py`. O `AE-182` reincide a `DRF-44`. Sem drift: a `OP-27` já diz o que o texto passa a descrever. Autoria futura: card que muda regra de instrumento cujo docstring do módulo a descreve põe o docstring do módulo entre os passos (a mesma da `DRF-55`). | Laudo da `RAF-T27` (ressalva 91). Medida do consultor (2026-09-29, cópia em `%TEMP%`): o texto antigo existe verbatim, em CRLF, na árvore; Verificação 1 real `docstring=1-0-0 linhas=222`, cópia com a troca `docstring=0-1-1 linhas=227`; linha nova mais longa 98; o módulo compila e o pré-voo da cópia segue `criar` e `não` como antes. |
| DRF-67 | (consultor, acionamento 22, `AE-184`) As três frases de `.claude/tools/backlog.py` que contam o vocabulário do `check` (docstring do módulo, linhas 3 e 7; comentário da seção do `check`, linhas 592-595) passam de `C-1..C-17` a `C-1..C-18`, e o comentário nomeia a `C-18` e a função que a acusa. A `RAF-T29` (`done`, fica como executada) acrescentou a violação sem pôr as frases que a contam entre os passos (item 12(i) da Fase 4); a execução seguiu o card. Card `RAF-T29a` (`OP-29`, redação; `tarefas:` da §1; §6 linha D; fecha a etapa com `RAF-T34` e `RAF-T35`; `RAF-T36` passa a depender dele). Fora do módulo nada muda: `tests/test_backlog.py` linha 2 é o docstring atribuído à `BKL-T2` (o que aquele card testou) e `docs/OPERACOES_AS_IS_P-0751.md` linha 412 é medida datada. Nenhum card aberto edita o `backlog.py`. Sem drift. Autoria futura: card que acrescenta código ao vocabulário fechado de um instrumento põe entre os passos cada frase que conta o vocabulário (a mesma família da `DRF-55` e da `DRF-66`; reincidiu). | Laudo da `RAF-T29` (ressalva 91). Medida do consultor (2026-09-29, cópia em `%TEMP%`): os três textos antigos existem verbatim, arquivo LF (0 CR); Verificação 1 real `vocabulario=3-0-0 linhas=2612`, cópia com a troca `vocabulario=0-3-1 linhas=2613`; linha nova mais longa 92; o módulo compila. |
| DRF-68 | (consultor, acionamento 23, `AE-186`) O aviso `B1` da `RAF-T30` (`DRF-22`) segue chaveado no alvo `instrumento`, que passa a ser o quinto alvo de achado de processo: `.claude/tools/rdo.py` (`_ALVOS_ACHADO`, o docstring do módulo, o de `_formatar_achados_processo` e o `help` de `--achado-processo`), `docs/RUBRICA_DE_REVISAO.md` §6 (linha nova da tabela) e `.claude/agents/pantonic-reviewer.md`. A alternativa de chavear o `B1` num dos quatro alvos de hoje não se seguiu: nenhum deles denuncia instrumento, e o TR da `RAF-T30` exige que termo de falha em outro alvo cale. Card `RAF-T30a` (`OP-30`; `tarefas:` da §1; §6 linha D); `RAF-T34` passa a depender dele. Drift: a rubrica de revisão ganha propriedade que o modelo não tem — dossiê `Ato de modelo` de `emenda` ao modelador (versão 4 pendente, sobe no Marco 5; recusada, o corretivo da `OP-30` que tira o quinto alvo e a decisão do `B1` voltam a este consultor). A asserção `"linha nova do registro" not in saida`, que a `RAF-T30` deslocou do teste do marco para o fim do TR novo, volta ao lugar no redespacho da própria `RAF-T30` (Passo 0 e Verificação 3), que consome a retentativa: o deslocamento é defeito de execução, contra a restrição do card. O item 3 do `AE-186` (a seção *Linhas removidas* do `review_evidence.py` não vê asserção migrada de função) fica com rota auditoria final (diretiva de 2026-09-26). Autoria futura: card cujo instrumento lê a saída de outro instrumento prova o caminho com a saída real do produtor, não com a entrada montada à mão; card que acrescenta ao fim de arquivo de teste nomeia a última linha que fica. | Laudo da `RAF-T30` (reprovado 74). Medida do consultor (2026-09-29, cópia em `%TEMP%`): árvore real `-k alvo_instrumento` `exit 5`; com o TF e sem a regra `1 failed`; depois `1 passed`; Verificação 2 `alvos=3-0-0 rdo=0-0-0` → `alvos=0-1-1 rdo=1-1-1`; `test_rdo.py`, `test_encerrar.py` e `test_doutrina_unidade.py` na cópia com as mesmas falhas de infraestrutura antes e depois e um `passed` a mais; árvore real `127 passed` nos três. Redespacho da `RAF-T30` na cópia: `marco=1 total=2` → `marco=2 total=2`, as 1211 primeiras linhas de `tests/test_encerrar.py` iguais às do ref `9e5bf2e`. |
| DRF-69 | (consultor, acionamento 24, `AE-190`) A `DFP-8` do `P-0752` (recusa da linha repetida) não se aposenta nem se estende a `gravar_por_agente`: segue no escritor sem agente (`append_row` e a pré-checagem do `encerrar.py tarefa`), e no escritor por agente a identidade da rodada é o agente, cuja linha a nova troca — a mesma parada gravada de novo fica idempotente, e estender a recusa descartaria a linha de outro agente da mesma tarefa com os mesmos números. O cruzamento hook → fechamento segue coberto: o `checar_repetida` do `encerrar.py` lê a última linha da tarefa pelo cabeçalho, a do agente inclusive. O erro que a `RAF-T31` deixou é de texto: os docstrings de `checar_repetida` e `append_row` ("todo escritor") e o do módulo ("só apende", colunas e CLI sem `--agente`). Card `RAF-T31a` (`OP-31`, redação; `tarefas:` da §1 e da §1A; §6 linha D; fecha a etapa D); nenhum card aberto edita o `telemetria.py`. `RAF-T31` fica como executada. Sem drift: o estado `linhas por agente` já diz a troca. `AE-189` reincide a `DRF-44`. Autoria futura: a da `DRF-55` (card que muda comportamento de instrumento varre o docstring do módulo e os das funções que afirmam o comportamento antigo); reincidiu. | Laudo da `RAF-T31` (ressalva 91), achado 2 (`laudo:RAF-T31#2`). Medida do consultor (2026-09-29, cópia em `%TEMP%`): Verificação 1 real `docstring=1-1-1-0-0 linhas=305`, cópia `docstring=0-0-0-3-1 linhas=314`; linhas novas até 99, compila; `test_telemetria.py` e `test_telemetria_hook.py` `33 passed` na cópia depois; nenhum teste lê os docstrings. |
| DRF-70 | (consultor, acionamento 25, `AE-191`) O primeiro parágrafo do docstring do módulo de `.claude/tools/telemetria.py` (linhas 5-6, "o conteúdo anterior nunca é tocado por conteúdo (só ganha uma linha no final)") ganha a ressalva "sem `--agente`", e o `help` do subcomando `append` ("Adiciona uma linha validada ao TSV.") ganha "com --agente, troca a do mesmo agente": são as duas frases do arquivo que ainda afirmam só o apêndice, e a primeira contradiz o segundo parágrafo que a `RAF-T31a` reescreveu. O `help` entra pela varredura do consultor (o laudo nomeou só o docstring), para a família da `DRF-55` fechar num card só. O docstring de `append_row` fica (afirma o apêndice só dele, o que é verdade), e a `description` do parser também (nomeia o verbo). Card `RAF-T31b` (`OP-31`, redação; `tarefas:` da §1 e da §1A; §6 linha D; fecha a etapa D no lugar da `RAF-T31a`). `RAF-T31a` fica como executada. Sem drift. Defeito de autoria do consultor no acionamento 24, que varreu os parágrafos que o laudo da `RAF-T31` nomeou e não o arquivo (reincide a lição da `DRF-55`). Autoria futura: card que troca a afirmação de um comportamento varre o arquivo inteiro pelas frases que a afirmam (docstrings, `help`, `description`), não só os trechos que o laudo nomeia. | Laudo da `RAF-T31a` (ressalva 91), achado 1 (`laudo:RAF-T31a#1`). Medida do consultor (2026-09-29, cópia em `%TEMP%`): Verificação 1 real `texto=1-0-0-0 linhas=314`, cópia `texto=0-1-1-1 linhas=317`; compila; `--help` mostra o texto novo; `test_telemetria.py` e `test_telemetria_hook.py` `33 passed` na cópia; nenhum teste lê o docstring nem o `help`. |
| DRF-71 | (consultor, acionamento 26, `RAF-T32` `blocked` premissa) O card da `RAF-T32` nomeava `processar` como a função dos ramos `PreToolUse` · `Agent` e `PostToolUse` · `Agent` de `.claude/tools/progresso_hook.py`, que não a define (medido: `processar` só existe em `backlog_hook.py` e `telemetria_hook.py`); os ramos vivem em `evento` (linhas 334-497). O referente é inequívoco (as atribuições `tarefa_corrente` das linhas 447 e 471 são as únicas dos dois ramos; a da linha 486 é do `UserPromptSubmit`, que o `Não fazer` já exclui): o card troca `processar` por `evento` em `Camada e fronteira` e na regra 3 de `Contratos/classes`, com as duas atribuições nomeadas. Procedente (defeito de autoria do card, não parada sem razão). Sem drift. Autoria futura: função citada no card se mede por `grep` no arquivo-alvo antes de publicar (Fase 4 item 13 (ii)). |
| DRF-72 | (consultor, acionamento 27, `AE-193`) A `RAF-T32` levou a linha de abertura do despacho aos ramos `PreToolUse` e `PostToolUse` síncrono · `Agent` de `evento` e excluiu o `UserPromptSubmit`, onde mora a frase de volta do subagente que devolve por hand-back (`PostToolUse` com `handback` `send` só grava `pendentes[agentId]`; a volta chega em `<agent-message>`) — o caminho real quando o subagente devolve por `SubagentHandback`: o painel diz que o consultor recebe "Outro título" e devolve "Um título de teste" (medido). O estado final da `OP-32` (`painel do gerente.tarefa mostrada`) não vale no caminho real: corretivo `RAF-T32a` (`OP-32`; `tarefas:` §1 e §1A; §6 D; fecha a etapa D), que grava o título despachado numa chave nova `titulos_pendentes[agentId]` no `PostToolUse` do hand-back e o tira na volta, e testa o `PostToolUse` síncrono que a `RAF-T32` mudou sem teste. `pendentes` segue string (os testes de hoje o comparam inteiro). O terceiro item do achado (ID casado sem card mostra o ID) não é defeito: a regra 2 da `RAF-T32` manda o trio pelo `localizar_card`, que devolve o ID sem card, como a `tarefa_corrente`; cair na tarefa corrente nomearia uma tarefa que não foi despachada, o defeito da `R-16`. `RAF-T32` fica como executada. Sem drift. `AE-192` reincide a `DRF-44`. Autoria futura: card que troca a fonte de uma frase do painel cobre todo ramo que a emite (despacho, volta síncrona e volta por hand-back); o `Não fazer` da `RAF-T32`, reforçado pela `DRF-71`, excluiu o ramo por nome sem medir o que ele emite. | Laudo da `RAF-T32` (ressalva 91, achado 2). Ensaio do consultor (2026-09-29, cópia em `%TEMP%` pasta `raf_t32a`): `-k retorno_do_despacho` real `exit 5`; com os testes e sem as regras `1 failed, 1 passed`; depois `2 passed`; `tests/test_progresso_hook.py` real `47 passed`, cópia `48 passed` e a falha de infraestrutura `test_tf_ger_18_residencia` (lê a skill fora da cópia). |
| DRF-73 | (consultor, acionamento 28, Marco 5, `AE-187`) `_diff_fluxo` de `.claude/tools/modelo.py` compara o par só pelo texto (o card da `RAF-T22` mandava "com par de mesmo texto e mesmo número, nenhuma linha"), e a operação que muda `precisa de:` ou `altera:` sem mudar o texto sai do drift que o dono lê no marco — contra o estado final de `conferência do modelo.diferença entre versões` ("mostra operação [...] alterada"). Corretivo `RAF-T22a` (`OP-22`; `tarefas:` §1 e §1A; §6 E, depende do gate `RAF-T36`; `RAF-T40` depende dele): todo par emite `[~] OP-<k> — precisa de: <vigente> => <pendente>` e `[~] OP-<k> — altera: <vigente> => <pendente>` quando a lista difere; `tarefas:` é lastro e não entra. Ensaiado em cópia: `show --drift` do `P-0755` passa a mostrar as duas linhas da `OP-30`. Não bloqueia o Marco 5: a mensagem ao dono carrega a mudança da `OP-30` à mão. Sem drift. Autoria futura: card de instrumento que declara "nenhuma linha" para um caso mede os campos que o caso deixa de comparar. | `AE-187`; `DRF-16`; `R-07`. |
| DRF-74 | (consultor, acionamento 28, Marco 5) O consultor valida a versão 4 pendente do modelo (§1A, emenda do modelador pela `DRF-68`): o `diff` §1 × §1A, medido, muda só a propriedade e o contrato de `rubrica de revisão`, o `precisa de:` e o `altera:` da `OP-30`, a linha nova `rubrica de revisão.alvo do achado de instrumento` da §1.3 e a contagem do cabeçalho (62 propriedades); a mudança já está na árvore pela `RAF-T30a` (`_ALVOS_ACHADO` de `rdo.py` com `instrumento`), e `modelo.py check --plano` sai `exit 0`. Linha: "valido a versão 4: a diferença para a vigente é só a propriedade e o contrato da rubrica de revisão, o precisa de e o altera da OP-30 e a linha nova alvo do achado de instrumento da §1.3, que é a DRF-68 já entregue na árvore pela RAF-T30a sem escopo novo". O `show --drift` não mostra a mudança da `OP-30` (`AE-187`, corrigido pela `DRF-73` na etapa E): a mensagem do marco a carrega à mão. | `DRF-68`; `AE-186`; `AE-187`; `R-20`. |
| DRF-75 | (consultor, acionamento 29, `AE-204`) A subseção `### Quando a janela para num marco` da skill `scrum-master`, escrita pela `RAF-T39`, manda a entrega ser a célula *o que o dono lê* inteira, e o exemplo do Marco 2 usa só o trecho antes dos dois-pontos; a célula do Marco 1 é um comando; e o primeiro parágrafo do `## Relatório de encerramento` segue dizendo que o relatório abre com a saída do `modelo.py show`. A entrega passa a ser o nome da etapa, o trecho da célula antes dos dois-pontos, sem a lista que os segue; célula que não nomeia etapa (o marco do modelo) ou plano sem tabela de marcos: o título do plano. O primeiro parágrafo ganha a remissão à linha que vem antes do `show`, sem repetir a regra e sem o nome literal da subseção (a Verificação da `RAF-T39` conta `marco=1`). Corretivo `RAF-T39a` (`OP-39`; `tarefas:` §1; §6 E); `RAF-T40` depende dele. | Erro inequívoco não se adia: a rota do laudo (a `RAF-T40` ou o Marco 6 fixarem) punha a correção num card que não edita a skill ou no dono, que não valida questão técnica. A célula inteira levaria ao dono a lista de recomendações e, no Marco 1, um comando, contra o fim da `R-25` (o dono entender de relance o que recebe). Sem drift: o estado final da `OP-39` não muda. |

## 4. Invariantes de execução

Valem para todos os cards; cada card repete, inline, a parte que o vincula.

1. **O loop abre em janela nova** (`R-01` aplicada a este plano): a janela que planejou encerra no Marco 1; a
   execução começa em outra janela, com este plano como único insumo.
2. **Arquivo compartilhado em série:** dois cards que editam o mesmo arquivo rodam na ordem da §6, nunca em
   paralelo. Um arquivo de instrumento por card sempre que a operação permitir.
3. **Instrumento tem teste:** toda mudança em `.claude/tools/`, `.claude/global/hooks/` ou `.claude/checks/`
   vem com teste em `tests/`. Piso de regressão é relação: o total é re-medido no despacho (referência
   histórica: 521 coletados em 2026-09-28); a entrega soma os testes novos e não reduz esse total.
4. **Fixture construída:** todo caso da auditoria que um teste reproduz é fixture montada em `tmp_path`; nenhuma
   `Verificação` lê `%TEMP%`, o plano fictício descartado ou os artefatos de `docs/audits/`.
5. **Doutrina em card próprio, residência única:** mudança de texto normativo (agente, skill, `GOVERNANCA.md`,
   rubrica) é card distinto do card de instrumento, e cada regra nova é enunciada num lugar só.
6. **Só biblioteca padrão**, Python 3.12, e `pytest` nos testes.
7. **Fora do alcance de qualquer card:** `docs/audits/**`; `docs/plans/P-0753-auditoria-estagio-1/**`;
   `docs/plans/P-0754-auditoria-final/**`; `docs/telemetria.tsv` (só o hook o escreve); `~/.claude/**`;
   `.claude/KIT_VERSION` (versão congelada em `0.0.0`, modo hub).
8. **Atos do dono, fora do plano:** commit; `materializar.py apply` (leva o hook do pytest corrigido a
   `~/.claude/hooks/`).
9. **Marcos:** a primeira tarefa das etapas B..E nasce `blocked`, razão `dependencia` (`DRF-5`); só a condução a
   passa a `ready`, depois do `go` do dono gravado por `encerrar.py marco`.
10. **O plano fecha com a revisão do `README.md`** (G-README dever 2), com `pwsh .claude/checks/check-readme.ps1`
    em exit 0; o veredito do dono sobre ela é gate do Marco 6, não critério de pronto do card.
11. **`R-29` não tem operação** (`DRF-3`).
12. **Restrição ao modelo** (para o `pantonic-model-designer`): as operações seguem a ordem das etapas A..E da
    `DRF-4`, e a última é a revisão do `README.md`; cada operação corresponde a uma recomendação ou a um grupo
    coeso de recomendações que alteram o mesmo arquivo — a decisão de agrupar é do modelo, não do card; mudança
    de doutrina e mudança de instrumento são operações distintas; nenhuma célula descritiva do modelo leva
    caminho, linha, id de decisão ou nome de instrumento (norma `TK-76`) — residências ficam na §2 e nos cards.
13. **Permissão negada não se contorna** (`DRF-48`): se o sistema de permissão negar a edição de um arquivo-alvo, quem executa não refaz a mesma mudança por outra ferramenta nem por outro canal; faz as demais edições do card, para e sinaliza `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno. Quem conduz junta as edições negadas num comando PowerShell único e o entrega ao dono no fim da sessão (ato do dono de 2026-09-29); o card volta a `ready` depois que o dono o roda.
14. **A árvore compartilhada só se lê pelo `git`** (`DRF-56`): quem executa não roda na árvore do repositório comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`, `commit`), porque ela carrega trabalho não commitado de outros planos. A prova do mundo `antes` sai da ordem dos Passos (teste vermelho antes da regra) ou de cópia fora do repositório; teste que precisa de `git` que escreve monta o próprio repositório em `tmp_path`.

## 5. Tarefas

Um card por operação da §1, na ordem das operações; `RAF-T<n>` materializa `OP-<n>`. Os valores `antes` e `depois`
das Verificações foram medidos no ensaio da Fase 4 (cópia da árvore de 2026-09-28, HEAD `2513964` com o WIP, fora do
repositório): o `antes` de cada card na cópia com os cards anteriores aplicados, e também na árvore real quando o card
abre a sua série; o `depois`, na cópia com o próprio card aplicado.

### RAF-T1 — O loop de plano recém-planejado abre em janela nova [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa ensina o gerente do loop a abrir a execução de um plano recém-planejado numa janela nova, separada da que o planejou, com o plano gravado como único insumo.
- **Fundamento:** `DRF-4`, `DRF-6` (a doutrina mora no Passo 1 da skill `scrum-master`); `F-6`, `F-8`; relatório `R-01`.
- **Operação do modelo:** `OP-1`
  - OP-1: Quem executa ensina o gerente do loop a abrir a execução de um plano recém-planejado numa janela nova, separada da que o planejou, com o plano gravado como único insumo.
  - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.
- **Camada e fronteira:** doutrina do kit — a skill `scrum-master`, rotina de quem conduz o loop; nenhum código muda. O contrato do objeto é: "Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só." A regra nova mora só no Passo 1 da skill (residência única, `DRF-6`); nenhum outro arquivo a repete.
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
- **Passos:**
  1. Em `.claude/skills/scrum-master/SKILL.md`, no `### Passo 1 — Gate de modelo do contexto principal`, logo depois da linha `  gate.` (a última linha do bullet `- **Ação:**`) e antes da linha que começa por `- **Saída:** modelo conferido`, inserir o bloco abaixo (as quebras são as do bloco; cada linha perde os dois espaços do recuo deste card):

     ```text
     - **Janela:** o loop de um plano recém-planejado abre numa janela nova, separada da que o
       planejou, com o plano gravado como único insumo; a janela do planejamento encerra no Marco 1
       (`R-01` da auditoria final, `P-0755`). Quem conduz e planejou o plano na janela corrente não
       despacha tarefa dele: encerra pelo relatório de janela, com a regra "loop de plano
       recém-planejado abre em janela nova", e o dono abre a janela do loop.
     ```
  2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_progresso_hook.py` lê esta skill (tabela do repertório `M-0`..`M-18`), que o bloco não toca.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer no texto do `- **Ação:**` nem do `- **Saída:**` do Passo 1; não acrescentar a regra a `GOVERNANCA.md`, a outra skill ou a agente (a regra mora num lugar só); não criar o medidor de custo (é da `RAF-T2`).
- **Contingências:**
  - se a linha `  gate.` seguida da linha que começa por `- **Saída:** modelo conferido` não existir em `.claude/skills/scrum-master/SKILL.md` → parar e sinalizar `blocked` razão `premissa`, colando as linhas 32 a 45 do arquivo.
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_progresso_hook.py` lê a skill.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('janela-nova=%d'%t.count('- **Janela:** o loop de um plano recém-planejado abre numa janela nova'))"` → `janela-nova=1` — antes `janela-nova=0`, depois `janela-nova=1`
- **Pronto quando:**
  - gerente do loop.janela em que o loop abre — o planejamento encerra a sua janela no primeiro marco, e o loop de um plano recém-planejado abre numa janela nova, com o plano gravado como único insumo — Verificação 1
- **Fora do escopo desta tarefa:** o instrumento que mede o custo por turno (`RAF-T2`); a medida do ganho sobre o transcript do loop, que é da condução no relatório do Marco 6 (§7).
- **Handover:** 2026-09-28 · para quem vier depois
  - **Entregue:** campo '- **Janela:**' no Passo 1 da skill scrum-master, .claude/skills/scrum-master/SKILL.md:43-47 (hoje recuado 3 espaços, aninhado sob '- **Ação:**')
  - **Contrato:** a regra 'loop de plano recém-planejado abre em janela nova' mora só no Passo 1 da skill scrum-master; nenhum outro arquivo a repete
  - **Não refazer:** o texto do bloco; suíte 521 passed e check-drift 0 já medidos
  - **Pendente:** o recuo do campo (sub-item em vez de campo irmão de Gatilho/Entrada/Ação/Saída) vai à triagem do consultor

### RAF-T1a — O campo Janela do Passo 1 fica irmão dos outros campos do passo [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa sobe à coluna 0 o campo `- **Janela:**` que a `RAF-T1` gravou no Passo 1 da skill `scrum-master`, para ele ser campo do passo como `Gatilho`, `Entrada`, `Ação` e `Saída`, e não sub-item do `- **Ação:**`.
- **Fundamento:** `DRF-43`; `AE-122` (laudo da `RAF-T1`, ressalva 88); `DRF-4`, `DRF-6`.
- **Depende de:** `RAF-T1`
- **Operação do modelo:** `OP-1`
  - OP-1: Quem executa ensina o gerente do loop a abrir a execução de um plano recém-planejado numa janela nova, separada da que o planejou, com o plano gravado como único insumo.
  - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.
- **Camada e fronteira:** doutrina do kit — a skill `scrum-master`, rotina de quem conduz o loop; nenhum código muda. Muda só o recuo das cinco linhas do campo; o texto delas fica como a `RAF-T1` o gravou.
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
- **Passos:**
  1. Em `.claude/skills/scrum-master/SKILL.md`, no `### Passo 1 — Gate de modelo do contexto principal`, o campo `- **Janela:**` (hoje as linhas 43 a 47: a primeira começa por três espaços e `- **Janela:**`, as quatro de continuação por cinco espaços) perde três espaços de recuo em cada linha: a primeira passa a começar na coluna 0 por `- **Janela:**`, logo depois da linha `  gate.`, e as quatro de continuação por dois espaços, como as do `- **Ação:**`. O texto e as quebras não mudam; o número de linhas do arquivo não muda.
  2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho). `tests/test_progresso_hook.py` lê esta skill (tabela do repertório `M-0`..`M-18`), que a edição não toca.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0 (medido 0 antes, 2026-09-28).
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar palavra do campo `- **Janela:**`, do `- **Ação:**` nem do `- **Saída:**`; não mexer em outro passo da skill (os Passos 3 e 4 são da `RAF-T4`).
- **Contingências:**
  - se a Verificação 1 não imprimir `coluna0=0 aninhado=1 continua=0` antes da edição → parar e sinalizar `blocked` razão `premissa`, colando a saída e as linhas 36 a 50 do arquivo.
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_progresso_hook.py` lê a skill.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('coluna0=%d aninhado=%d continua=%d'%(t.count('  gate.\n- **Janela:** o loop de um plano recém-planejado abre numa janela nova'),t.count('   - **Janela:**'),sum(t.count('\n  '+s) for s in ('planejou, com o plano gravado','despacha tarefa dele: encerra','recém-planejado abre em janela nova'))))"` → `coluna0=1 aninhado=0 continua=3` — antes `coluna0=0 aninhado=1 continua=0`, depois `coluna0=1 aninhado=0 continua=3`
  2. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('janela-nova=%d'%t.count('- **Janela:** o loop de um plano recém-planejado abre numa janela nova'))"` → `janela-nova=1` — antes `janela-nova=1`, depois `janela-nova=1` (invariância: o texto do campo não muda)
- **Pronto quando:**
  - gerente do loop.janela em que o loop abre — a regra da janela nova é campo próprio do Passo 1, irmão de `Gatilho`, `Entrada`, `Ação` e `Saída` — Verificação 1
- **Fora do escopo desta tarefa:** regra nova de recuo no planejador (`DRF-43`); o vermelho do `dead_code.py` sobre a sonda (`DRF-44`).
- **Handover:** 2026-09-28 · para `RAF-T4`
  - **Entregue:** campo '- **Janela:**' do Passo 1 na coluna 0, continuações com 2 espaços, .claude/skills/scrum-master/SKILL.md:43-47
  - **Contrato:** Passo 1 da skill scrum-master tem cinco campos irmãos: Gatilho, Entrada, Ação, Janela, Saída; a regra da janela nova mora só ali
  - **Não refazer:** recuo e texto do campo Janela; suíte 521 passed e check-drift 0
  - **Pendente:** nenhum

### RAF-T2 — O medidor de custo da sessão vira comando do kit [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** Quem executa cria o medidor de custo da sessão, que lê uma conversa gravada e reparte o contexto reenviado por turno, por passo do loop e por tarefa despachada.
- **Fundamento:** `DRF-6`; `F-6` (285,6k por turno no loop real), `F-13` (os rascunhos quebram e fixam `AUF-T`); relatório `R-01`.
- **Depende de:** `RAF-T1`
- **Operação do modelo:** `OP-2`
  - OP-2: Quem executa cria o medidor de custo da sessão, que lê uma conversa gravada e reparte o contexto reenviado por turno, por passo do loop e por tarefa despachada.
  - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; rascunhos de medição da auditoria — Ninguém altera: são o ponto de partida do medidor novo e ficam como estão.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/`, só biblioteca padrão (Python 3.12); não importa de `tests/`, de outro módulo do kit nem de projeto consumidor; lê o transcript e escreve só o TSV que recebe por argumento. Os rascunhos `docs/audits/sonda-2026-09-28/medir.py` e `docs/audits/sonda-2026-09-28/passos.py` são o ponto de partida lido e ficam intocados (contrato do objeto: "Ninguém altera: são o ponto de partida do medidor novo e ficam como estão.").
- **Arquivos-alvo:**
  - `.claude/tools/custo_sessao.py`
  - `tests/test_custo_sessao.py`
- **Contratos/classes:** módulo novo `.claude/tools/custo_sessao.py`, com guarda `if __name__ == "__main__": sys.exit(main())` e toda função alcançável a partir de `main` (o `dead_code.py` julga alcançabilidade). Funções e saídas, exatas:
  1. `medir(transcript: Path, saida: Path) -> int` — para cada linha do transcript que é JSON (linha que não é JSON se pula) com `type == "assistant"` e `message.usage` não vazio, grava no TSV uma linha com cinco campos separados por tabulação: `timestamp` do evento, `message.id`, o contexto reenviado `input_tokens + cache_read_input_tokens + cache_creation_input_tokens` (ausente conta 0), `output_tokens` e as ferramentas do turno unidas por ` | `; devolve o número de linhas. Ferramentas, por bloco de `message.content`, na ordem: `tool_use` de nome `Agent` → `Agent:<subagent_type>:<description>`; `tool_use` de nome `Bash` ou `PowerShell` → `Bash:` seguido do `command` com todo espaço em branco colapsado num espaço, cortado em 220 caracteres; outro `tool_use` → `<name>:` seguido de `file_path` (na falta, `pattern`), cortado em 120; bloco `text` com texto não vazio → `TEXT`.
  2. `classificar_passo(ferramentas: str) -> str` — tira `TEXT | ` e ` | TEXT` do texto e devolve o primeiro que casa, nesta ordem: contém `pantonic-executor` → `P4`; `pantonic-reviewer` → `P6`; `pantonic-consultant` → `P8`; `encerrar.py` → `P9`; casa a regex `backlog\.py status \S+ review` → `P5`; contém `despachar` → `P3`; contém `backlog.py next` → `P2`; casa a regex `grep -n|--co -q|wc -l` e não contém `laudo` → `P3`; contém `laudos/` ou `Achado de processo` → `P7`; texto vazio ou só `TEXT` → `texto`; senão `outro`.
  3. `passos(tsv: Path, regex_inicio: str, regex_fim: str) -> list[str]` — agrupa as linhas do TSV por `message.id` (a primeira linha do id dá `timestamp`, contexto e saída; as ferramentas de todas as linhas do id se juntam por ` | `); a janela vai da primeira mensagem cujas ferramentas casam `regex_inicio` (`re.search`) até a última que casa `regex_fim`. Sem mensagem que case uma das duas, ou com a última do fim antes da primeira do início, devolve exatamente `["janela: vazia", "por tarefa: n=0"]`. Com janela, devolve, nesta ordem: `janela: <ts0> -> <ts1> turnos <N> ctx_k <x> out_k <y>`; uma linha `<passo> turnos=<n> ctx_k=<x> out_k=<y>` por passo, em ordem alfabética do passo; e, se nenhuma mensagem da janela casou a regex de tarefa `despachar ([A-Z]+-T\d+[a-z]?|TK-\d+)`, a linha `por tarefa: n=0`; senão `por tarefa: n=<k> turnos medio=<m> ctx_k medio=<c> min_turnos=<a> max_turnos=<b>` e uma linha `<tarefa> turnos=<n> ctx_k=<x> out_k=<y>` por tarefa, na ordem do primeiro despacho. A tarefa corrente é a do último `despachar` casado até a mensagem (inclusive); mensagem anterior ao primeiro despacho não entra em tarefa nenhuma. Todo valor `_k` é o total dividido por 1000 com uma casa (`f"{v / 1000:.1f}"`); `turnos medio` também com uma casa.
  4. `main(argv: list[str] | None = None) -> int` — `argparse` com subcomandos obrigatórios `medir <transcript> <saida>` e `passos <tsv> <regex_inicio> <regex_fim>`; reconfigura stdout e stderr para UTF-8; `medir` imprime `<n> linhas` e sai 0; `passos` imprime as linhas de `passos()` e sai 0. Os caminhos vêm como dados na linha de comando (relativos ao diretório corrente ou absolutos) e não se normalizam. Recusas fechadas, cada uma com stderr e exit 1, sem gravar nada: transcript que não é arquivo → `custo_sessao: FALHOU - transcript não encontrado '<caminho>'`; TSV que não é arquivo → `custo_sessao: FALHOU - tsv não encontrado '<caminho>'`; `regex_inicio` ou `regex_fim` que não compila → `custo_sessao: FALHOU - regex inválida '<padrão>': <erro do re>`. Sem subcomando, a recusa é a do `argparse` (exit 2).
- **Passos:**
  1. Criar `tests/test_custo_sessao.py` com os quatro testes da seção `Testes`, carregando o módulo por `importlib.util.spec_from_file_location` a partir de `.claude/tools/custo_sessao.py`, com o transcript sintético escrito em `tmp_path` (uma linha `user`, os turnos `assistant` do teste e uma linha que não é JSON).
  2. Rodar `python -m pytest tests/test_custo_sessao.py -q` e conferir que falha (o módulo não existe).
  3. Criar `.claude/tools/custo_sessao.py` com o contrato de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 4 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A).
  - Só biblioteca padrão; Python 3.12.
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Os testes usam só transcript sintético em `tmp_path`; nenhum teste lê `%TEMP%`, a pasta do usuário ou `docs/audits/`.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não editar nem apagar `docs/audits/sonda-2026-09-28/medir.py` e `docs/audits/sonda-2026-09-28/passos.py`; não localizar o transcript sozinho (o caminho vem por argumento); não registrar o comando em `.claude/projecoes.json` (não é hook); não citar o comando no `README.md` (é da `RAF-T40`).
- **Contingências:**
  - se `python .claude/checks/dead_code.py` acusar símbolo de `.claude/tools/custo_sessao.py` → seguir com a chamada do símbolo a partir de `main` ou com a remoção do símbolo, até o achado sumir, sem mudar a saída de `Contratos/classes`.
  - se um teste que já existia na suíte cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_medir_grava_uma_linha_por_turno_com_contexto_reenviado` — transcript com dois turnos: `m1` (`input_tokens` 10, `cache_read_input_tokens` 1000, `cache_creation_input_tokens` 200, `output_tokens` 30, um `Bash` com `python .claude/tools/backlog.py next`) e `m2` (5, 2000, 0, 40, um bloco `text`); `main(["medir", ...])` sai 0, imprime `2 linhas`, e o TSV é exatamente `t1\tm1\t1210\t30\tBash:python .claude/tools/backlog.py next` e `t2\tm2\t2005\t40\tTEXT` (a regra concorrente que somasse só `cache_read_input_tokens` daria 1000). TF `test_tf_passos_reparte_por_passo_e_por_tarefa_de_qualquer_plano` — quatro turnos de contexto 1000, 2000, 3000 e 4000: `despachar RAF-T3`, `Agent` `pantonic-executor`, `despachar TK-12`, `Agent` `pantonic-reviewer`; `passos` com início `despachar` e fim `pantonic-reviewer` sai 0 e imprime `janela: t1 -> t4 turnos 4 ctx_k 10.0 out_k 0.0`, `P3 turnos=2 ctx_k=4.0 out_k=0.0`, `P4 turnos=1 ctx_k=2.0 out_k=0.0`, `P6 turnos=1 ctx_k=4.0 out_k=0.0`, `por tarefa: n=2 turnos medio=2.0 ctx_k medio=5.0 min_turnos=2 max_turnos=2`, `RAF-T3 turnos=2 ctx_k=3.0 out_k=0.0` e `TK-12 turnos=2 ctx_k=7.0 out_k=0.0` (o rascunho, preso a `AUF-T`, não conta tarefa nenhuma). TR `test_tr_passos_sem_despacho_informa_zero_e_sai_0` — janela sem `despachar`: a última linha é `por tarefa: n=0` e o exit é 0 (o rascunho sai 1 com `ZeroDivisionError`); regex de início que nada casa: saída exatamente `janela: vazia` e `por tarefa: n=0`, exit 0. TR `test_tr_medir_e_passos_recusam_com_mensagem` — `medir` com transcript inexistente sai 1 com `custo_sessao: FALHOU - transcript não encontrado` no stderr; `passos` com início `(` sai 1 com `custo_sessao: FALHOU - regex inválida '('` (a regra concorrente sem recusa sai com exceção do `re`). Suíte `tests/test_custo_sessao.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_custo_sessao.py -q -k medir` → `exit 0` — antes `exit 4`, depois `exit 0`
  2. `python -m pytest tests/test_custo_sessao.py -q -k passos` → `exit 0` — antes `exit 4`, depois `exit 0`
- **Pronto quando:**
  - medidor de custo da sessão.medida por turno — um comando do kit, com teste, grava o contexto reenviado em cada turno de uma conversa gravada — Verificação 1
  - medidor de custo da sessão.medida por passo e por tarefa — os turnos se repartem por passo do loop e por tarefa de qualquer plano ou tíquete; numa janela sem despacho o comando informa zero e termina bem — Verificação 2
- **Fora do escopo desta tarefa:** a medida do ganho sobre o transcript real do loop (ato da condução no relatório do Marco 6, §7); a doutrina da janela nova (`RAF-T1`); a citação no `README.md` (`RAF-T40`).
- **Handover:** 2026-09-28 · para quem vier depois
  - **Entregue:** comando novo .claude/tools/custo_sessao.py (subcomandos medir <transcript> <saida> e passos <tsv> <regex_inicio> <regex_fim>) com 4 testes em tests/test_custo_sessao.py; suíte 525 passed
  - **Contrato:** medir grava TSV timestamp/message.id/contexto reenviado/output/ferramentas por turno; passos reparte por passo P2..P9 e por tarefa de qualquer plano ou tíquete (regex despachar <ID>); recusas fechadas com exit 1
  - **Não refazer:** o medidor e os testes; os rascunhos de docs/audits/sonda-2026-09-28/ ficam intocados
  - **Pendente:** a medida do ganho sobre o transcript real do loop é da condução no relatório do Marco 6

### RAF-T3 — O despacho grava o pacote da tarefa e imprime só o recado ao executor [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** Quem executa faz o despacho de tarefa entregar ao executor, num arquivo próprio, o card com as âncoras já conferidas, deixando na tela de quem conduz só o texto pronto do despacho.
- **Fundamento:** `DRF-7`, `DRF-8`, `DRF-35`; `F-6` (3,06k por despacho na tela de quem conduz; 0,72k com o card por arquivo; 23 turnos de âncora à mão), `F-9`, `F-10`; relatório `R-02`, `R-03`.
- **Depende de:** `RAF-T1`
- **Operação do modelo:** `OP-3`
  - OP-3: Quem executa faz o despacho de tarefa entregar ao executor, num arquivo próprio, o card com as âncoras já conferidas, deixando na tela de quem conduz só o texto pronto do despacho.
  - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit — `.claude/tools/backlog.py` (verbo `despachar`) e a residência dos caminhos `.claude/tools/caminhos.py`, só biblioteca padrão; `backlog.py` carrega `caminhos.py` por caminho (`_caminhos`), nunca por `import` de pacote; `modelo.py`, `card_check.py` e `review_evidence.py` seguem chamados por subprocesso, sem mudança. O pacote gravado é projeção regenerável do card: fica fora do versionamento pelo `.gitignore`. O contrato do objeto é: "Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor."
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `.claude/tools/caminhos.py`
  - `.gitignore`
  - `tests/test_backlog.py`
- **Contratos/classes:**
  1. `caminhos.py`, função nova antes de `def main(argv: list[str] | None = None) -> int:` — `destino_despacho(raiz: Path, plano_path: Path, tarefa: str) -> Path`: plano em pasta (`pasta_do_plano(plano_path)` não `None`) → `<pasta>/despacho/<tarefa>.md`; senão → `<raiz>/docs/RDO/despacho/<tarefa>.md`.
  2. `backlog.py`, funções novas antes de `def despachar(`: `_campos_do_card(texto: str) -> dict[str, str]` — cada linha que casa `^- \*\*(?P<rotulo>[^*]+):\*\*` abre o campo `<rotulo>` (sem espaços nas pontas), cujo texto vai do resto da linha até a linha anterior ao próximo campo; e `conferir_ancoras_do_card(repo: Path, texto_card: str) -> list[str]`, com esta regra fechada (`DRF-8`, `DRF-35`): (a) alvos = cada trecho entre crases do campo `Arquivos-alvo` que, sem espaços nas pontas, é arquivo existente sob `repo`, na ordem do card e sem repetição; (b) para cada trecho entre crases (`` `[^`\n]+` ``) dos campos `Passos` e, depois, `Contratos/classes`, sem espaços nas pontas, pula o trecho com menos de 4 caracteres, o já visto e o que é um dos alvos; (c) trecho na forma `<caminho>:<n>` ou `<caminho>:<n>-<m>` (regex `^(?P<caminho>[^:\s]+\.[A-Za-z0-9]+):(?P<linha>\d+)(?:-\d+)?$`) com `<caminho>` arquivo existente e `1 <= n <= número de linhas` → `- <caminho>:<n> — <linha n sem espaços nas pontas>`; (d) outro trecho → a primeira linha, do primeiro alvo em ordem, que contém o trecho → `- <caminho>:<linha> — <texto da linha sem espaços nas pontas>`; (e) sem linha → `- âncora ausente: <trecho>`; (f) item repetido não se repete; lista vazia → `["- nenhuma âncora citada"]`. Arquivos se leem em UTF-8 com `errors="replace"`.
  3. `despachar(repo: Path, id_: str, mundo: str | None = None) -> ResultadoStatus` — assinatura, gates, ordem das conferências, recusa e gravação de `.claude/estado/tarefa-corrente.json` (com `ref`) inalterados. No lugar das quatro impressões de hoje (o bloco que começa em `print(f"=== DESPACHO: {id_} — {alvo.titulo}")` e termina em `print(f"ref={ref}")`), grava o pacote em `_caminhos.destino_despacho(repo, repo / pai.arquivo, id_)` (cria a pasta; sobrescreve o que houver; UTF-8, quebra `\n`), com estas partes, nesta ordem, unidas por quebra de linha: `# Despacho <ID> — <título>`, linha vazia, `despacho: <P-id> <ID>` (o `<P-id>` é `pai.id`), `ref=<ref>`, linha vazia, `## Card`, linha vazia, o texto de `show(modelo, id_)`, linha vazia, `## Handovers`, linha vazia, cada handover de `handovers_para(pai, tipo_pai, alvo)` como hoje (`=== HANDOVER DE {autor.id} — {autor.titulo} ({autor.status}; {autor.arquivo})`, o texto, linha vazia) ou `- nenhum` e linha vazia quando não há, `## Âncoras conferidas`, linha vazia, as linhas de `conferir_ancoras_do_card(repo, alvo.texto)` e uma linha vazia. Depois imprime no stdout exatamente estas linhas, nesta ordem (as quebras são as do bloco; `<rel>` é o caminho do pacote relativo a `repo`, com `/`):

     ```text
     === DESPACHO: <ID> — <título>
     despacho: <P-id> <ID>
     Execute a tarefa <ID>: o card, os handovers e as âncoras conferidas estão em <rel>.
     Devolva uma única linha, numa destas formas:
     <ID> review
     <ID> review pendencia=<uma linha>
     <ID> blocked motivo=<dependencia|premissa|ferramenta> <uma linha de razão>
     ref=<ref>
     ```
  4. `.gitignore`: logo depois da linha `!.claude/estado/.gitkeep`, uma linha vazia e o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card):

     ```text
     # Pacote do despacho (`R-02`, `P-0755`): projeção regenerável do card, gravada por
     # `backlog.py despachar` a cada despacho — nunca se versiona.
     docs/plans/*/despacho/
     docs/RDO/despacho/
     ```
- **Passos:**
  1. Acrescentar ao fim de `tests/test_backlog.py` os cinco testes da seção `Testes`, no molde de `test_tf_despachar_grava_estado_e_imprime_ref` (fixture `_montar_repo_despachar`, `backlog.main(["despachar", ...])`).
  2. Rodar `python -m pytest tests/test_backlog.py -q -k "pacote or texto_pronto or confere_as_ancoras"` e conferir que os testes falham.
  3. Aplicar os itens 1 a 4 de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 5 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5); `destino_despacho` e as duas funções novas de `backlog.py` têm chamador de produção em `despachar`.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Os testes montam o repositório em `tmp_path` com `_montar_repo_despachar`; o único teste que lê a árvore real é o do `.gitignore`, por `git check-ignore -q`, sem escrever nada.
  - Nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar os gates de `despachar` nem a ordem deles; não mudar `next` nem `show`; não mudar o `modelo.py check` chamado pelo despacho (o `--so-vigente` é da `RAF-T20`); não editar a skill `scrum-master` (a doutrina dos Passos 3 e 4 é da `RAF-T4`); não criar pasta `despacho/` versionada nem `.gitkeep` nela.
- **Contingências:**
  - se um teste de `despachar` que já existia em `tests/test_backlog.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se `git check-ignore -q docs/plans/P-0755-recomendacoes-auditoria-final/despacho/RAF-T1.md` sair 1 depois do item 4 → parar e sinalizar `blocked` razão `premissa`, colando a saída de `git check-ignore -v` para o mesmo caminho.
- **Testes:** TF `test_tf_despachar_grava_o_pacote_na_pasta_do_plano` — `despachar GAM-T1` sai 0 e `docs/plans/P-0-gama/despacho/GAM-T1.md` tem as linhas `### GAM-T1 — Primeira tarefa [Sonnet · classe implementacao]`, `despacho: P-0 GAM-T1` e `## Âncoras conferidas` (a regra de hoje não grava arquivo). TR `test_tr_despachar_recusado_nao_grava_o_pacote` — `despachar GAM-T2` sai 1 e a pasta `docs/plans/P-0-gama/despacho` não existe. TF `test_tf_gitignore_ignora_o_pacote_do_despacho` — na raiz real, `git check-ignore -q` sai 0 para `docs/plans/P-0755-recomendacoes-auditoria-final/despacho/RAF-T1.md` e para `docs/RDO/despacho/TK-1.md` (hoje sai 1). TF `test_tf_despachar_imprime_o_texto_pronto_ao_executor` — a primeira linha do stdout é `=== DESPACHO: GAM-T1 — Primeira tarefa`, a segunda é `despacho: P-0 GAM-T1`, a terceira contém `docs/plans/P-0-gama/despacho/GAM-T1.md`, o stdout tem as três linhas da gramática de retorno com `GAM-T1`, a última começa por `ref=`, e o stdout não contém `- **Objetivo:** fixture.` (hoje o card inteiro sai na tela). TF `test_tf_despachar_confere_as_ancoras_do_card` — o card `GAM-T1` da fixture ganha `- **Arquivos-alvo:**` com `src/alvo.py` (no lugar do `Entregável`) e `- **Passos:**` com `` 1. Editar `src/alvo.py:1` — `x = 1`. `` e `` 2. Trocar `return 1` e `texto que sumiu`. ``; `src/alvo.py` tem as linhas `x = 1`, `def alvo():` e `    return 1`; o pacote tem as linhas `- src/alvo.py:1 — x = 1`, `- src/alvo.py:3 — return 1` e `- âncora ausente: texto que sumiu` (a regra de hoje não confere âncora). Suíte `tests/test_backlog.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_backlog.py -q -k pacote` → `exit 0` — antes `exit 5`, depois `exit 0`
  2. `python -m pytest tests/test_backlog.py -q -k texto_pronto` → `exit 0` — antes `exit 5`, depois `exit 0`
  3. `python -m pytest tests/test_backlog.py -q -k confere_as_ancoras` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - despacho de tarefa.lugar do card despachado — o pacote da tarefa é gravado num arquivo da pasta do plano, fora do versionamento, que se regenera a cada despacho — Verificação 1
  - despacho de tarefa.texto pronto ao executor — o despacho imprime o recado pronto: a linha que declara plano e tarefa, o caminho do pacote e a forma da resposta esperada — Verificação 2
  - despacho de tarefa.âncoras conferidas — o pacote traz cada linha citada com o número atual e o texto dela, e marca como ausente o texto que não está mais no arquivo — Verificação 3
- **Fora do escopo desta tarefa:** a doutrina do Passo 3 e do Passo 4 da skill `scrum-master` (`RAF-T4`); o despacho com `--so-vigente` (`RAF-T20`); a linha `despacho:` lida pelos hooks de telemetria e de progresso (`RAF-T31`, `RAF-T32`).
- **Handover:** 2026-09-28 · para `RAF-T4`
  - **Entregue:** backlog.py despachar grava o pacote (card, handovers, âncoras conferidas) em <pasta do plano>/despacho/<ID>.md via caminhos.destino_despacho e imprime só o recado de 8 linhas (=== DESPACHO, despacho: <P-id> <ID>, caminho do pacote, gramática de retorno, ref=); .gitignore ignora docs/plans/*/despacho/ e docs/RDO/despacho/; 5 testes novos, suíte 530 passed
  - **Contrato:** a linha 'despacho: <P-id> <ID>' sai na 2ª linha do stdout e no pacote; o pacote se regenera a cada despacho e nunca se versiona; gates e ordem de despachar inalterados
  - **Não refazer:** destino_despacho, _campos_do_card, conferir_ancoras_do_card e os 5 testes
  - **Pendente:** a regra de conferir_ancoras_do_card gera âncora ausente falsa (AE do laudo), em triagem do consultor antes da RAF-T4

### RAF-T3a — O pacote do despacho marca ausente só a linha citada que sumiu [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** Quem executa faz a conferência de âncoras do despacho marcar como ausente só o texto que o card cita como linha de um arquivo e que não está mais nele, lendo o trecho entre crases como o Markdown o lê, sem tomar comando, nome novo ou rótulo de campo por âncora que sumiu.
- **Fundamento:** `DRF-45`; `AE-125` (laudo da `RAF-T3`, ressalva 91); `DRF-8`, `DRF-35`; relatório `R-03`.
- **Depende de:** `RAF-T3`
- **Operação do modelo:** `OP-3`
  - OP-3: Quem executa faz o despacho de tarefa entregar ao executor, num arquivo próprio, o card com as âncoras já conferidas, deixando na tela de quem conduz só o texto pronto do despacho.
  - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit — só a função `conferir_ancoras_do_card` de `.claude/tools/backlog.py`, só biblioteca padrão; `despachar`, `_campos_do_card`, o pacote e o texto pronto ficam como a `RAF-T3` os gravou. A regra que o `card_check` já aplica a `Arquivos-alvo` e `Passos` (âncora `<caminho>:<n>` seguida do literal, separado por `—` ou `:`) é a mesma que esta regra usa para saber que um trecho é o texto de uma linha citada. Medida do consultor (2026-09-28) sobre os 41 cards do `P-0755`: a regra de hoje dá 1066 linhas de âncora, 573 delas `âncora ausente`; a regra desta tarefa, ensaiada em cópia, dá 501 linhas e nenhuma ausente.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
- **Contratos/classes:**
  1. `backlog.py`, `conferir_ancoras_do_card(repo: Path, texto_card: str) -> list[str]` — assinatura, os campos lidos (`Arquivos-alvo` para os alvos; `Passos` e, depois, `Contratos/classes` para os trechos), a ordem dos alvos, o pulo do trecho com menos de 4 caracteres, do já visto e do que é um dos alvos, o item repetido que não se repete, o `["- nenhuma âncora citada"]` e a leitura UTF-8 com `errors="replace"` ficam como estão. Muda esta regra fechada (`DRF-45`), que a docstring passa a descrever, citando `DRF-45`:
     (g) trecho entre crases é o *code span* do Markdown, lido linha a linha do campo: uma sequência de N crases abre, a próxima sequência de exatamente N crases fecha, e o trecho é o que fica entre elas, sem espaços nas pontas; vale também para os alvos de `Arquivos-alvo`. A regex ensaiada, com o trecho no grupo 2 (as quebras são as do bloco):

     ```text
     (?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)
     ```
     (h) trecho de linha citada é o que casa a regex do bloco abaixo; o caminho resolve para ele mesmo quando é arquivo sob `repo` e, se não for, para o primeiro alvo, na ordem do card, cujo caminho termina em `/` mais o caminho citado; resolvido e com `1 <= n <= número de linhas` → `- <caminho resolvido>:<n> — <linha n sem espaços nas pontas>`; senão → `- âncora ausente: <trecho>`.

     ```text
     ^(?P<caminho>[^:\s`]+):(?P<linha>\d+)(?:-\d+)?$
     ```
     (i) trecho que, na mesma linha do card, vem logo depois de um trecho da forma (h), com só espaços e um `—` ou um `:` entre os dois, é o texto daquela linha citada: a primeira linha do arquivo resolvido que o contém → `- <caminho resolvido>:<k> — <texto da linha sem espaços nas pontas>`; caminho não resolvido ou nenhuma linha que o contenha → `- âncora ausente: <trecho>`. Um trecho da forma (h) pulado por já visto continua abrindo o (i) do trecho seguinte.
     (j) outro trecho → a primeira linha, do primeiro alvo em ordem, que o contém, como hoje; sem linha, o trecho **não entra** no pacote: não cita linha (comando, nome que a tarefa cria, rótulo de campo).
  2. `tests/test_backlog.py`, em `test_tf_despachar_confere_as_ancoras_do_card`: a ausência passa a vir de uma linha citada. A linha do texto antigo vira as três do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os oito espaços que já tem no arquivo); as asserções do teste não mudam.

     Texto antigo:

     ```text
             "  2. Trocar `return 1` e `texto que sumiu`.\n"
     ```

     Texto novo:

     ```text
             "  2. Trocar `return 1`.\n"
             "- **Contratos/classes:**\n"
             "  1. `src/alvo.py:2` — `texto que sumiu`.\n"
     ```
- **Passos:**
  1. Acrescentar ao fim de `tests/test_backlog.py` os três testes da seção `Testes`, no molde de `test_tf_despachar_confere_as_ancoras_do_card` (fixture `_montar_repo_despachar`, o card `GAM-T1` com o bullet do `Entregável` trocado pelos campos do teste, `backlog.main(["despachar", "GAM-T1", "--repo", str(repo)])` saindo 0, o pacote lido de `docs/plans/P-0-gama/despacho/GAM-T1.md`).
  2. Rodar `python -m pytest tests/test_backlog.py -q -k "nao_marcam_ausente or sem_extensao"` e conferir que os dois testes TF falham.
  3. Aplicar os itens 1 e 2 de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 3 testes novos (referência datada: `530 passed`, 2026-09-28, entrega da `RAF-T3`).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5, `DRF-44`).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `despachar`, `_campos_do_card`, `destino_despacho`, o pacote nem o texto pronto; não mudar o `card_check.py` (a regra dele fica como está); não tirar asserção de teste existente.
- **Contingências:**
  - se um teste de `despachar` que já existia em `tests/test_backlog.py`, além do do item 2 de `Contratos/classes`, cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_ancoras_nao_marcam_ausente_o_trecho_que_nao_cita_linha` — alvo `src/alvo.py` com as linhas `x = 1`, `def alvo():` e `    return 1`; `Passos` com `` 1. Rodar `python -m pytest -q` e preencher o campo `Testes`. `` e ``` 2. Conferir ``campo `Testes` do card`` e trocar `return 1`. ```; o pacote tem `- src/alvo.py:3 — return 1` e não tem `- âncora ausente` (a regra de hoje marca ausentes o comando, o rótulo e o fragmento da crase dupla). TF `test_tf_ancoras_leem_arquivo_sem_extensao_e_caminho_pelo_alvo` — alvos `src/alvo.py` (as mesmas linhas) e `.alvorc` (linhas `chave = 1` e `outra = 2`); `Contratos/classes` com `` 1. Editar `.alvorc:2` e `alvo.py:3`. ``; `Passos` com `1. Aplicar Contratos/classes.`; o pacote tem `- .alvorc:2 — outra = 2` e `- src/alvo.py:3 — return 1` e não tem `- âncora ausente` (a regra de hoje marca os dois ausentes). TR `test_tr_ancoras_marcam_ausente_a_linha_citada_que_sumiu` — alvo `src/alvo.py` (as mesmas linhas); `Contratos/classes` com `` 1. `src/alvo.py:2` — `texto que sumiu`; `src/alvo.py:9`. ``; `Passos` com `1. Aplicar Contratos/classes.`; o pacote tem `- src/alvo.py:2 — def alvo():`, `- âncora ausente: texto que sumiu` e `- âncora ausente: src/alvo.py:9` (a regra concorrente, que não marcasse ausente trecho nenhum, falharia; a de hoje passa). A âncora com linha fica em `Contratos/classes` porque o `card_check` do despacho recusa, em `Passos`, a âncora cujo literal não está na linha. Suíte `tests/test_backlog.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_backlog.py -q -k nao_marcam_ausente` → `exit 0` — antes `exit 5`, depois `exit 0`
  2. `python -m pytest tests/test_backlog.py -q -k sem_extensao` → `exit 0` — antes `exit 5`, depois `exit 0`
  3. `python -m pytest tests/test_backlog.py -q -k linha_citada_que_sumiu` → `exit 0` — antes `exit 5`, depois `exit 0`
  4. `python -m pytest tests/test_backlog.py -q -k confere_as_ancoras` → `exit 0` — antes `exit 0`, depois `exit 0` (invariância: o teste da `RAF-T3`, com a linha do item 2, segue verde)
- **Pronto quando:**
  - despacho de tarefa.âncoras conferidas — o pacote traz cada linha citada com o número atual e o texto dela, e marca como ausente o texto que não está mais no arquivo — Verificações 1, 2 e 3
- **Fora do escopo desta tarefa:** a regra de âncora do `card_check.py`; as linhas de âncora achadas que não são ponto de edição (o pacote segue trazendo a primeira linha que contém o trecho); a doutrina dos Passos 3 e 4 da skill `scrum-master` (`RAF-T4`).
- **Handover:** 2026-09-28 · para `RAF-T4`
  - **Entregue:** conferir_ancoras_do_card (.claude/tools/backlog.py) lê crases como o Markdown, aceita <caminho>:<n> sem extensão e por sufixo de alvo, e marca ausente só linha citada que sumiu ou texto citado depois dela; 3 testes novos, suíte 533 passed
  - **Contrato:** o pacote do despacho não traz mais âncora ausente falsa: comando, nome novo e rótulo de campo saem do pacote
  - **Não refazer:** a regra nova de âncoras e os testes
  - **Pendente:** o pacote ainda traz, por trecho, a primeira linha dos alvos que o contém mesmo quando não é ponto de edição (matéria inconclusiva no cenário)

### RAF-T4 — Quem conduz repassa o texto pronto do despacho e não reconfere âncora [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa ensina o gerente do loop a repassar ao executor o texto pronto do despacho, sem reconferir à mão as âncoras do card.
- **Fundamento:** `DRF-7`, `DRF-8`, `DRF-45`; `F-6`, `F-8` (Passo 3 e Passo 4 da skill `scrum-master`); relatório `R-02`, `R-03`.
- **Depende de:** `RAF-T1a`, `RAF-T3`, `RAF-T3a`
- **Operação do modelo:** `OP-4`
  - OP-4: Quem executa ensina o gerente do loop a repassar ao executor o texto pronto do despacho, sem reconferir à mão as âncoras do card.
  - precisa de: despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.
- **Camada e fronteira:** doutrina do kit — a skill `scrum-master`, rotina de quem conduz o loop; nenhum código muda. O comportamento que a doutrina descreve já está no `despachar` desde a `RAF-T3`: grava o pacote em `<pasta-do-plano>/despacho/<ID>.md` (card, handovers e âncoras conferidas) e imprime, entre a linha `=== DESPACHO:` e a linha `ref=<sha>`, o texto pronto ao executor (a linha `despacho: <P-id> <ID>`, o caminho do pacote e a gramática da linha de retorno). A regra muda só nos Passos 3 e 4; nenhum outro arquivo a repete.
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
- **Passos:**
  1. No `### Passo 3 — Gates herdados`, no parágrafo que começa por `**Por comando** (`, trocar as duas linhas do texto antigo pelas quatro do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os dois espaços iniciais que já tem no arquivo).

     Texto antigo:

     ```text
       `in-progress`, grava `.claude/estado/tarefa-corrente.json` com o `<ref>` e imprime o card
       inteiro, o bloco `HANDOVER` e a linha `ref=<sha>`. Recusa pelo primeiro gate que falhar, sem
     ```

     Texto novo:

     ```text
       `in-progress`, grava `.claude/estado/tarefa-corrente.json` com o `<ref>`, grava o pacote da
       tarefa em `<pasta-do-plano>/despacho/<ID>.md` (fora do versionamento: o card, os handovers e as
       âncoras conferidas contra a árvore de agora) e imprime só o texto pronto do despacho ao
       executor e a linha `ref=<sha>`. Recusa pelo primeiro gate que falhar, sem
     ```
  2. No `### Passo 4 — Despacho do executor`, trocar as cinco linhas do texto antigo pelas sete do texto novo (mesma regra de quebra e recuo).

     Texto antigo:

     ```text
       Despachada pelo verbo `despachar` do passo 3, a tarefa já tem o arquivo gravado e o `<ref>` na
       linha `ref=<sha>` da saída: este passo só invoca o executor.

       Invocar `pantonic-executor` com `model` **igual ao do cabeçalho** (vence o `model:` do agente),
       com o dossiê da tarefa e a instrução de devolver **uma única linha**, domínio fechado (`DP-G`
     ```

     Texto novo:

     ```text
       Despachada pelo verbo `despachar` do passo 3, a tarefa já tem o arquivo gravado, o pacote em
       `<pasta-do-plano>/despacho/<ID>.md` e o `<ref>` na linha `ref=<sha>` da saída: este passo só
       invoca o executor.

       Invocar `pantonic-executor` com `model` **igual ao do cabeçalho** (vence o `model:` do agente),
       com o texto pronto que o `despachar` imprimiu entre a linha `=== DESPACHO:` e a linha
       `ref=<sha>`, repassado como está — sem copiar o card nem o handover na conversa —, que já traz
       a instrução de devolver **uma única linha**, domínio fechado (`DP-G`
     ```
  3. No mesmo Passo 4, trocar as três linhas do texto antigo pelas três do texto novo (mesma regra de quebra e recuo).

     Texto antigo:

     ```text
       O despacho cola, junto do dossiê, as **âncoras** (arquivo, linha e texto do ponto a editar)
       re-derivadas no ato e o **range de linhas do bullet de fechamento anterior** quando a tarefa
       fecha em plano em andamento.
     ```

     Texto novo:

     ```text
       As **âncoras** (arquivo, linha e texto do ponto a editar) chegam conferidas no pacote do
       despacho; nenhum passo as reconfere à mão. Quando a tarefa fecha em plano em andamento, o
       despacho acrescenta ao texto pronto o **range de linhas do bullet de fechamento anterior**.
     ```
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_progresso_hook.py` lê esta skill (tabela do repertório `M-0`..`M-18`), que os passos não tocam.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer nos gates do Passo 3 nem no caminho à mão do card de tíquete; não mexer na gramática da linha de retorno (o bloco cercado com `<tarefa> review`); não mexer no bloco `- **Janela:**` do Passo 1 (`RAF-T1`); não editar `.claude/tools/backlog.py` (a mecânica é da `RAF-T3`).
- **Contingências:**
  - se o texto antigo de um dos passos 1 a 3 não existir verbatim em `.claude/skills/scrum-master/SKILL.md` → parar e sinalizar `blocked` razão `premissa`, nomeando o passo.
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_progresso_hook.py` lê a skill.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('entrega=%d-%d'%(t.count('com o dossiê da tarefa e a instrução de devolver'),t.count('repassado como está — sem copiar o card nem o handover na conversa')))"` → `entrega=0-1` — antes `entrega=1-0`, depois `entrega=0-1`
  2. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('ancoras=%d-%d'%(t.count('re-derivadas no ato'),t.count('nenhum passo as reconfere à mão')))"` → `ancoras=0-1` — antes `ancoras=1-0`, depois `ancoras=0-1`
- **Pronto quando:**
  - gerente do loop.entrega do despacho ao executor — quem conduz repassa ao executor o texto pronto do despacho, que aponta o arquivo do pacote: perto de mil tokens por tarefa, ou menos — Verificação 1
  - gerente do loop.conferência das âncoras — nenhum passo manda reconferir: as âncoras chegam conferidas no pacote — Verificação 2
- **Fora do escopo desta tarefa:** a mecânica do pacote e das âncoras (`RAF-T3`); a rota do modelador com operação nova (`RAF-T24`); o despacho do consultor com a linha do card em triagem (`RAF-T34`).
- **Handover:** 2026-09-28 · para quem vier depois
  - **Entregue:** Passos 3 e 4 da skill scrum-master (.claude/skills/scrum-master/SKILL.md) mandam repassar ao executor o texto pronto do despachar, com o pacote em <pasta do plano>/despacho/<ID>.md, sem copiar o card nem reconferir âncora
  - **Contrato:** quem conduz repassa o recado impresso pelo despachar; as âncoras vêm conferidas no pacote
  - **Não refazer:** as três trocas de prosa nos Passos 3 e 4
  - **Pendente:** passagem-de-bastao Gate de delegação item 3 e o campo Entrada do Passo 4 ainda mandam re-derivar/copiar (em triagem do consultor)

### RAF-T4a — O gate de delegação e a entrada do Passo 4 deixam de mandar re-derivar e copiar [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa fecha a regra da `RAF-T4` nos dois pontos que ela não alcançou: o item 3 do Gate de delegação da skill `passagem-de-bastao`, que o Passo 3 da `scrum-master` manda rodar antes do `despachar`, deixa de mandar colar âncoras re-derivadas na tarefa de plano; e a `Entrada` do Passo 4 da `scrum-master` deixa de ser o dossiê copiado do plano.
- **Fundamento:** `DRF-46`; `AE-126` (laudo da `RAF-T4`, ressalva 88); `DRF-7`, `DRF-8`, `DRF-45`; relatório `R-02`, `R-03`.
- **Depende de:** `RAF-T4`
- **Operação do modelo:** `OP-4`
  - OP-4: Quem executa ensina o gerente do loop a repassar ao executor o texto pronto do despacho, sem reconferir à mão as âncoras do card.
  - precisa de: despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.
- **Camada e fronteira:** doutrina do kit — o item 3 do Gate de delegação da skill `passagem-de-bastao` (residência única do gate) e o campo `Entrada` do Passo 4 da skill `scrum-master`; nenhum código muda. A `RAF-T4` trocou os Passos 3 e 4 da `scrum-master`, mas o gate que o Passo 3 manda rodar antes do `despachar` seguia mandando colar as âncoras "re-derivadas no ato", e a `Entrada` do Passo 4 seguia "dossiê da tarefa copiado do plano". O card de tíquete segue pelos passos à mão (Passo 3 da `scrum-master`) e não tem pacote: para ele o gate conserva a re-derivação. O número de linhas dos dois arquivos não muda. A árvore tem a `scrum-master` com fim de linha CRLF nas 445 linhas, contra o `eol=lf` que o `.gitattributes` declara e o índice guarda em LF (medido pelo consultor, 2026-09-28, `git ls-files --eol`: `i/lf w/crlf`); o arquivo volta a LF no mesmo ato, sem mudar conteúdo.
- **Arquivos-alvo:**
  - `.claude/skills/passagem-de-bastao/SKILL.md`
  - `.claude/skills/scrum-master/SKILL.md`
- **Passos:**
  1. Em `.claude/skills/passagem-de-bastao/SKILL.md`, na seção `**Gate de delegação — residência única, roda ANTES de despachar o executor:**`, item 3, trocar as quatro linhas do texto antigo pelas quatro do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os três espaços iniciais que já tem no arquivo).

     Texto antigo:

     ```text
        silêncio. Junto dos números vão as **âncoras** (arquivo, linha e texto do ponto a editar)
        re-derivadas no ato e, quando a tarefa fecha em plano em andamento, o **range de linhas do bullet
        de fechamento anterior**: sem isso o dossiê não é autossuficiente e quem executa precisa
        redescobrir a localização — trabalho que a tarefa não pediu.
     ```

     Texto novo:

     ```text
        silêncio. As **âncoras** (arquivo, linha e texto do ponto a editar) da tarefa de plano chegam
        conferidas no pacote do `despachar` (`scrum-master`, passo 3) e não se re-derivam à mão; só o
        card de tíquete, despachado à mão, as leva re-derivadas no ato. Tarefa que fecha em plano em
        andamento leva ainda o **range de linhas do bullet de fechamento anterior** (`scrum-master`, passo 4).
     ```
  2. Em `.claude/skills/scrum-master/SKILL.md`, no `### Passo 4 — Despacho do executor`, trocar a linha do texto antigo pela do texto novo (sem quebra nova e sem refluxo; a linha começa na coluna 0).

     Texto antigo:

     ```text
     - **Entrada:** dossiê da tarefa copiado do plano; modelo declarado no cabeçalho.
     ```

     Texto novo:

     ```text
     - **Entrada:** texto pronto impresso pelo `despachar` (tíquete: dossiê à mão); modelo do cabeçalho.
     ```
  3. Gravar `.claude/skills/scrum-master/SKILL.md` com fim de linha LF em todas as linhas, sem mudar outro byte além dos do passo 2.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `533 passed`, 2026-09-28, entrega da `RAF-T3a`). `tests/test_progresso_hook.py` lê a skill `scrum-master` (tabela do repertório `M-0`..`M-18`), que os passos não tocam.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0 (medido 0 antes, 2026-09-28).
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar os itens 1, 2 e 4 a 8 do Gate de delegação nem o começo do item 3 (números de aceite e string de assert); não mexer nos Passos 3 e 4 da `scrum-master` além do campo `Entrada` do Passo 4 (o resto é da `RAF-T4`); não mexer no Passo 1 (`RAF-T1`, `RAF-T1a`).
- **Contingências:**
  - se o texto antigo do passo 1 ou do passo 2 não existir verbatim → parar e sinalizar `blocked` razão `premissa`, nomeando o passo.
  - se a Verificação 3 já imprimir `cr=0-0` antes da edição → o passo 3 não tem efeito e a tarefa segue.
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_progresso_hook.py` lê a skill `scrum-master`.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/skills/passagem-de-bastao/SKILL.md').read_text(encoding='utf-8');print('gate=%d-%d'%(t.count('Junto dos números vão as'),t.count('e não se re-derivam à mão; só o')))"` → `gate=0-1` — antes `gate=1-0`, depois `gate=0-1`
  2. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('entrada=%d-%d'%(t.count('dossiê da tarefa copiado do plano'),t.count('(tíquete: dossiê à mão); modelo do cabeçalho')))"` → `entrada=0-1` — antes `entrada=1-0`, depois `entrada=0-1`
  3. `python -c "from pathlib import Path;a=Path('.claude/skills/passagem-de-bastao/SKILL.md');b=Path('.claude/skills/scrum-master/SKILL.md');print('linhas=%d-%d cr=%d-%d'%(len(a.read_text(encoding='utf-8').splitlines()),len(b.read_text(encoding='utf-8').splitlines()),a.read_bytes().count(bytes([13])),b.read_bytes().count(bytes([13]))))"` → `linhas=306-445 cr=0-0` — antes `linhas=306-445 cr=0-445`, depois `linhas=306-445 cr=0-0`
- **Pronto quando:**
  - gerente do loop.conferência das âncoras — o gate que roda antes do despacho não manda re-derivar a âncora da tarefa de plano: ela chega conferida no pacote — Verificação 1
  - gerente do loop.entrega do despacho ao executor — a entrada do Passo 4 é o texto pronto do `despachar`, não o dossiê copiado do plano — Verificação 2
- **Fora do escopo desta tarefa:** a linha do `README.md` que ainda descreve o despacho imprimindo o card (`RAF-T40`); a menção a âncoras re-derivadas como precedente já pago, na herança de contexto da mesma skill `passagem-de-bastao` (não manda re-derivar); o parágrafo das âncoras do Passo 4 da `scrum-master` (`RAF-T4`).
- **Handover:** 2026-09-28 · para quem vier depois
  - **Entregue:** passagem-de-bastao Gate de delegação item 3 dispensa re-derivar âncora na tarefa de plano (tíquete segue à mão); Entrada do Passo 4 da scrum-master = texto pronto impresso pelo despachar; scrum-master/SKILL.md de volta a LF
  - **Contrato:** a regra 'repassar o texto pronto, sem copiar card nem reconferir âncora' vale nos Passos 3 e 4 e no gate de delegação
  - **Não refazer:** as três trocas de prosa e a normalização LF
  - **Pendente:** nenhum

### RAF-T5 — O gatilho do próximo passo responde só ao dono [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa faz o gatilho do próximo passo responder só à mensagem do dono, sem reagir ao relato de subagente nem ao aviso do sistema.
- **Fundamento:** `DRF-9`; `F-11` (o gatilho casou em relato de subagente e injetou 15,3 KB três vezes); relatório `R-15` (que também fecha a causa da `R-29`, `DRF-3`).
- **Depende de:** `RAF-T1`
- **Operação do modelo:** `OP-5`
  - OP-5: Quem executa faz o gatilho do próximo passo responder só à mensagem do dono, sem reagir ao relato de subagente nem ao aviso do sistema.
  - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit — o hook `UserPromptSubmit` `.claude/tools/backlog_hook.py`, só biblioteca padrão; a mudança é só na decisão de disparar; a saída quando dispara (`additionalContext` com a saída de `next`) não muda. Os testes novos moram em arquivo próprio, `tests/test_backlog_hook.py`, fora da série de `tests/test_backlog.py` (que é de `backlog.py`, `DRF-9`).
- **Arquivos-alvo:**
  - `.claude/tools/backlog_hook.py`
  - `tests/test_backlog_hook.py`
- **Contratos/classes:** `processar(payload: dict, repo: Path | None = None, backlog_module=None) -> dict | None` — assinatura inalterada. Regra nova em `_casa_gatilho(prompt) -> bool`: devolve verdadeiro só quando `prompt` é `str`, o prompt depois de `lstrip()` **não** começa por `<agent-message` nem por `[SYSTEM NOTIFICATION` (prefixos exatos, com distinção de caixa, numa tupla de módulo) e a frase `proximo passo` está em `_norm(prompt)` como hoje. Prompt fora do dono → `processar` devolve `None`, sem carregar `backlog.py`.
- **Passos:**
  1. Criar `tests/test_backlog_hook.py` com os três testes da seção `Testes`, carregando o hook por `importlib.util.spec_from_file_location` a partir de `.claude/tools/backlog_hook.py` e passando a `processar` `repo=tmp_path` e um `backlog_module` falso cujo `carregar(repo)` levanta `RuntimeError("backlog falso")`.
  2. Rodar `python -m pytest tests/test_backlog_hook.py -q` e conferir que os dois TF falham.
  3. Aplicar a regra de `Contratos/classes` em `_casa_gatilho`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 3 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A); os testes do hook que já moram em `tests/test_backlog.py` (`test_tf_hook_*`) seguem verdes.
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Os testes não leem o repositório real: o `backlog_module` é falso e `repo` é `tmp_path`.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mover para `tests/test_backlog_hook.py` os testes do hook que já existem em `tests/test_backlog.py`; não mudar `_GATILHO` nem `_norm`; não mudar `.claude/projecoes.json` (o registro do hook não muda).
- **Contingências:**
  - se um teste `test_tf_hook_*` de `tests/test_backlog.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_relato_de_subagente_com_proximo_passo_nao_injeta` — prompt `<agent-message from="pantonic-planner">Próximo passo de quem conduz: despachar.</agent-message>`: `processar` devolve `None` (hoje devolve o dicionário com o contexto da falha do backlog falso). TF `test_tf_aviso_do_sistema_com_proximo_passo_nao_injeta` — prompt com dois espaços iniciais, `  [SYSTEM NOTIFICATION] tarefa concluída; próximo passo do loop.`: devolve `None` (hoje, o dicionário). TR `test_tr_mensagem_do_dono_com_proximo_passo_segue_injetando` — prompt `execute o próximo passo`: devolve o dicionário com `hookEventName` `UserPromptSubmit` e `additionalContext` exatamente `backlog_hook: falha ao rodar next: backlog falso`. Suíte `tests/test_backlog_hook.py`, `tests/test_backlog.py -k hook` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_backlog_hook.py -q` → `exit 0` — antes `exit 4`, depois `exit 0`
- **Pronto quando:**
  - gatilho do próximo passo.mensagens que o disparam — só a mensagem do dono dispara; o relato de subagente e o aviso do sistema não injetam nada — Verificação 1
- **Fora do escopo desta tarefa:** o `next` limitado ao plano corrente (`R-29`, registrada sem ação, `DRF-3`); o hook do pytest (`RAF-T6`).
- **Handover:** 2026-09-28 · para quem vier depois
  - **Entregue:** _casa_gatilho em .claude/tools/backlog_hook.py só casa prompt do dono: recusa relato de subagente (<agent-message) e aviso do sistema; 3 testes novos em tests/test_backlog_hook.py, suíte 536
  - **Contrato:** processar() com assinatura inalterada; o gatilho do próximo passo não injeta o dossiê em relato de subagente
  - **Não refazer:** a regra nova de _casa_gatilho e os testes
  - **Pendente:** nenhum

### RAF-T6 — O filtro do pytest devolve o exit dos testes no comando encadeado [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** Quem executa faz o filtro da saída dos testes devolver o código de saída dos próprios testes, mesmo quando o comando encadeia outros passos depois deles.
- **Fundamento:** `DRF-10`; `F-7` (a fonte é `.claude/global/hooks/`; a projeção em `~/.claude/hooks/` é ato do dono), `F-12`; relatório `R-24`.
- **Depende de:** `RAF-T1`
- **Operação do modelo:** `OP-6`
  - OP-6: Quem executa faz o filtro da saída dos testes devolver o código de saída dos próprios testes, mesmo quando o comando encadeia outros passos depois deles.
  - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** fonte canônica dos hooks globais do kit, em `.claude/global/hooks/`, só biblioteca padrão; o hook e o filtro não importam um ao outro. A projeção para a pasta do usuário (`~/.claude/hooks/`, declarada em `.claude/projecoes.json`) é ato do dono (`python .claude/tools/materializar.py apply`) e fica fora do card: a sessão segue com a projeção antiga até o dono aplicar (§8 risco 6). O contrato do objeto é: "Quem implementa corrige o filtro na cópia que o kit guarda; levá-lo à máquina do dono é ato do próprio dono."
- **Arquivos-alvo:**
  - `.claude/global/hooks/pytest_pretooluse.py`
  - `.claude/global/hooks/pytest_filter.py`
  - `tests/test_pytest_pretooluse.py`
- **Contratos/classes:**
  1. `pytest_pretooluse.py` — `FILTER_PATH`, `PYTEST_RE`, `passthrough()` e as cinco condições de passthrough de `main()` inalterados. Três nomes novos de módulo: `SEGMENTO_PYTEST_RE` = `PYTEST_RE` sem o prefixo de início ou separador, ancorado no começo (`^(?:\S*python(?:3)?(?:\.exe)?\s+-m\s+)?(?:\S*[/\\])?pytest(?:\.exe)?(?:\s|$)`); `dividir_segmentos(cmd: str) -> list[str]` — as partes do comando alternando segmento e separador, com separador `&&`, `||`, `;` ou quebra de linha, reconhecido só fora de aspas simples ou duplas (a primeira e a última parte são segmentos; `"".join(partes) == cmd`); `reescrever(cmd: str, ferramenta: str) -> str | None` — cada segmento cujo texto sem espaços nas pontas casa `SEGMENTO_PYTEST_RE` troca o texto (espaços das pontas preservados) pelo bloco abaixo, conforme a ferramenta, e o resto do comando fica como está; nenhum segmento do pytest → `None`. Em `main()`, a linha `new_cmd = f'{cmd} 2>&1 | python "{FILTER_PATH}"'` vira `new_cmd = reescrever(cmd, data.get("tool_name"))`, e `None` cai em `passthrough()`. Blocos exatos (as quebras são as do bloco; `<segmento>` é o texto do segmento sem espaços nas pontas; `<filtro>` é o valor de `FILTER_PATH`):

     ```text
     Bash:       { <segmento>; echo "__PYTEST_EXIT__=$?"; } 2>&1 | python "<filtro>"
     PowerShell: & { <segmento>; "__PYTEST_EXIT__=$LASTEXITCODE" } 2>&1 | python "<filtro>"
     ```
  2. `pytest_filter.py` — constante nova `MARCADOR_EXIT_RE = re.compile(r"^__PYTEST_EXIT__=(-?\d+)$")`; a leitura do stdin tira de `lines` toda linha que, sem espaços nas pontas, casa o marcador (guardando o último exit lido); o log e o que se imprime não trazem o marcador; com marcador lido, o filtro sai com esse exit (`sys.exit(<exit>)`) no lugar da regra do sumário; sem marcador, a regra de hoje (0 se passou; 1 com falha, erro ou saída irreconhecível) não muda. Os docstrings dos dois arquivos passam a descrever a regra nova.
- **Passos:**
  1. Criar `tests/test_pytest_pretooluse.py` com os cinco testes da seção `Testes`: o hook roda por subprocesso (`sys.executable` e o caminho do hook, o JSON no stdin, o stdout lido como JSON); o `FILTER_PATH` esperado se lê carregando o hook por `importlib.util.spec_from_file_location`; o filtro roda por subprocesso com o texto no stdin e com `TMPDIR`, `TEMP` e `TMP` apontando para `tmp_path`, para o log não cair na pasta temporária do usuário.
  2. Rodar `python -m pytest tests/test_pytest_pretooluse.py -q` e conferir que os três TF falham.
  3. Aplicar os itens 1 e 2 de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 5 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Nenhum teste lê nem escreve a pasta do usuário: o filtro grava o log em `tmp_path`.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não rodar `python .claude/tools/materializar.py apply` nem copiar os arquivos para `~/.claude/hooks/` (ato do dono); não mudar `FILTER_PATH`; não mudar `.claude/projecoes.json`; não mudar as condições de passthrough (pipe ou redirecionamento no comando, `#nofilter`, `--collect-only`).
- **Contingências:**
  - se um teste de `tests/test_materializar.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_hook_reescreve_so_o_segmento_do_pytest_no_bash` — ferramenta `Bash`, comando `cd x && pytest -q; echo "exit=$?"`: o comando reescrito é exatamente `cd x && { pytest -q; echo "__PYTEST_EXIT__=$?"; } 2>&1 | python "<filtro>"; echo "exit=$?"` (hoje o pipe vai ao fim do comando inteiro e o `echo` final lê o exit do filtro). TF `test_tf_hook_reescreve_so_o_segmento_do_pytest_no_powershell` — ferramenta `PowerShell`, comando `python -m pytest -q; Write-Output "fim"`: reescrito exatamente `& { python -m pytest -q; "__PYTEST_EXIT__=$LASTEXITCODE" } 2>&1 | python "<filtro>"; Write-Output "fim"`. TR `test_tr_hook_sem_pytest_segue_passthrough` — ferramenta `Bash`, comando `git status`: stdout é `{}`. TF `test_tf_filtro_sai_com_o_exit_do_marcador` — stdin `3 passed in 0.10s` e `__PYTEST_EXIT__=5`, uma por linha: exit 5, stdout sem `__PYTEST_EXIT__` e com `3 passed in 0.10s` (hoje o filtro sai 0, pelo sumário). TR `test_tr_filtro_sem_marcador_segue_pelo_sumario` — stdin `1 failed, 2 passed in 0.10s`: exit 1; stdin `3 passed in 0.10s`: exit 0. Suíte `tests/test_pytest_pretooluse.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_pytest_pretooluse.py -q` → `exit 0` — antes `exit 4`, depois `exit 0`
- **Pronto quando:**
  - filtro da saída dos testes.código de saída devolvido — volta o código de saída dos testes, também no comando encadeado, nas duas linhas de comando que o kit usa — Verificação 1
- **Fora do escopo desta tarefa:** levar o hook e o filtro corrigidos a `~/.claude/hooks/` (ato do dono, §4 invariante 8); o gatilho do próximo passo (`RAF-T5`).
- **Handover:** 2026-09-28 · para quem vier depois
  - **Entregue:** filtro do pytest (.claude/global/hooks/pytest_pretooluse.py e pytest_filter.py) devolve o exit dos testes quando o comando encadeia passos depois deles; 5 testes novos em tests/test_pytest_pretooluse.py, suíte 541
  - **Contrato:** o exit do comando reescrito é o dos testes; a projeção em ~/.claude/hooks é ato do dono (materializar.py apply)
  - **Não refazer:** dividir_segmentos e a reescrita do exit, com os testes
  - **Pendente:** comando encadeado por || não chega a reescrever(): o passthrough de main() recusa qualquer pipe (em triagem do consultor)

### RAF-T6a — O filtro do pytest alcança o comando encadeado por OU lógico e por quebra de linha [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa faz o hook do filtro da saída dos testes alcançar também o comando encadeado por `||` ou por quebra de linha: a `RAF-T6` já divide esses segmentos, mas o `main()` do hook ainda devolve o comando sem filtro, porque lê o `||` como pipe e porque o pré-filtro não acha o pytest depois de `||` nem de quebra de linha.
- **Fundamento:** `DRF-47`; `AE-130` (laudo da `RAF-T6`, ressalva 91); `DRF-10`; `F-7`; relatório `R-24`.
- **Depende de:** `RAF-T6`
- **Operação do modelo:** `OP-6`
  - OP-6: Quem executa faz o filtro da saída dos testes devolver o código de saída dos próprios testes, mesmo quando o comando encadeia outros passos depois deles.
  - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** fonte canônica dos hooks globais do kit, em `.claude/global/hooks/`, só biblioteca padrão; o hook e o filtro não importam um ao outro. A projeção para a pasta do usuário (`~/.claude/hooks/`, declarada em `.claude/projecoes.json`) é ato do dono (`python .claude/tools/materializar.py apply`) e fica fora do card: a sessão segue com a projeção antiga até o dono aplicar (§8 risco 6). O contrato do objeto é: "Quem implementa corrige o filtro na cópia que o kit guarda; levá-lo à máquina do dono é ato do próprio dono."
- **Arquivos-alvo:**
  - `.claude/global/hooks/pytest_pretooluse.py`
  - `tests/test_pytest_pretooluse.py`
- **Contratos/classes:**
  1. `pytest_pretooluse.py` — o que fica verdade: `main()` segue devolvendo `{}` (`passthrough()`) para o comando com pipe simples (`|` que não é metade de `||`) ou com redirecionamento (`<`, `>`); o `||` deixa de contar como pipe; e o pré-filtro `PYTEST_RE` acha o pytest também no começo do segmento que vem depois de `||` ou de quebra de linha. `FILTER_PATH`, `SEGMENTO_PYTEST_RE`, `dividir_segmentos()`, `reescrever()`, `passthrough()` e as demais condições de passthrough (`#nofilter`, `pytest_filter`, `--collect-only`/`--co`) ficam inalterados. O docstring do módulo passa a dizer que a recusa é do pipe simples e do redirecionamento. A técnica é do executor; a ensaiada pelo consultor em cópia (2026-09-28) foi uma constante nova de módulo, usada no lugar do `any(...)` da primeira condição de passthrough de `main()`, e o prefixo de `PYTEST_RE` com `|` e quebra de linha na classe de separadores (as quebras são as do bloco):

     ```text
     PIPE_OU_REDIRECIONAMENTO_RE = re.compile(r"(?<!\|)\|(?!\|)|[<>]")
     PYTEST_RE, primeira linha:  r"(?:^|[;&|\n]\s*)"
     ```
- **Passos:**
  1. Acrescentar a `tests/test_pytest_pretooluse.py` os três testes da seção `Testes`, com os auxiliares que o arquivo já tem (`_rodar_hook`, `_filtro_path_esperado`).
  2. Rodar `python -m pytest tests/test_pytest_pretooluse.py -q` e conferir que os dois TF falham e os cinco testes da `RAF-T6` passam.
  3. Aplicar o item 1 de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 3 testes novos (referência datada: `541 passed`, 2026-09-28, handover da `RAF-T6`).
  - Os cinco testes da `RAF-T6` em `tests/test_pytest_pretooluse.py` seguem verdes e sem mudança.
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - `.claude/global/hooks/pytest_pretooluse.py` segue com fim de linha LF (`git ls-files --eol` mostra `w/lf` antes e depois).
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não rodar `python .claude/tools/materializar.py apply` nem copiar os arquivos para `~/.claude/hooks/` (ato do dono); não mudar `FILTER_PATH`, `.claude/projecoes.json` nem `.claude/global/hooks/pytest_filter.py`; não mudar `dividir_segmentos()` nem `reescrever()`; não deixar de recusar o pipe simples e o redirecionamento.
- **Contingências:**
  - se um dos cinco testes da `RAF-T6` cair depois do passo 3 → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se um teste de `tests/test_materializar.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_hook_reescreve_o_pytest_antes_do_ou_logico` — ferramenta `Bash`, comando `pytest -q || echo falhou`: o comando reescrito é exatamente `{ pytest -q; echo "__PYTEST_EXIT__=$?"; } 2>&1 | python "<filtro>" || echo falhou` (hoje o hook devolve `{}`). TF `test_tf_hook_reescreve_o_pytest_depois_do_ou_logico_e_da_quebra_de_linha` — ferramenta `Bash`: `false || pytest -q` reescrito exatamente `false || <bloco>`, e `cd x`, quebra de linha, `pytest -q` reescrito exatamente `cd x`, quebra de linha, `<bloco>`, sendo `<bloco>` o `{ pytest -q; echo "__PYTEST_EXIT__=$?"; } 2>&1 | python "<filtro>"` (hoje os dois devolvem `{}`). TR `test_tr_hook_pipe_simples_e_redirecionamento_seguem_passthrough` — ferramenta `Bash`: `pytest -q | tail -5` e `pytest -q > out.txt` devolvem `{}`. `<filtro>` é o `FILTER_PATH` lido do hook, como nos testes da `RAF-T6`. Suíte `tests/test_pytest_pretooluse.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_pytest_pretooluse.py::test_tf_hook_reescreve_o_pytest_antes_do_ou_logico -q` → `exit 0` — antes `exit 4`, depois `exit 0`
  2. `python -m pytest tests/test_pytest_pretooluse.py::test_tf_hook_reescreve_o_pytest_depois_do_ou_logico_e_da_quebra_de_linha -q` → `exit 0` — antes `exit 4`, depois `exit 0`
  3. `python -m pytest tests/test_pytest_pretooluse.py::test_tr_hook_pipe_simples_e_redirecionamento_seguem_passthrough -q` → `exit 0` — antes `exit 4`, depois `exit 0`
- **Pronto quando:**
  - filtro da saída dos testes.código de saída devolvido — o pytest antes do `||` entra no bloco filtrado, e o `||` lê o exit dos testes — Verificação 1
  - filtro da saída dos testes.código de saída devolvido — o pytest depois do `||` e depois da quebra de linha entra no bloco filtrado — Verificação 2
  - filtro da saída dos testes.código de saída devolvido — o pipe simples e o redirecionamento seguem sem filtro — Verificação 3
- **Fora do escopo desta tarefa:** levar o hook corrigido a `~/.claude/hooks/` (ato do dono, §4 invariante 8); pipe ou redirecionamento dentro de aspas (segue recusado, como na `RAF-T6`); o filtro `pytest_filter.py` (`RAF-T6`, entregue).
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** pytest_pretooluse.py recusa só pipe simples e redirecionamento (PIPE_OU_REDIRECIONAMENTO_RE) e PYTEST_RE acha o pytest depois de ||, | e quebra de linha; 3 testes novos, suíte 544
  - **Contrato:** comando encadeado por || ou quebra de linha com pytest é filtrado e devolve o exit dos testes; projeção em ~/.claude/hooks é ato do dono (materializar.py apply)
  - **Não refazer:** a regex nova e os 3 testes
  - **Pendente:** pipe ou redirecionamento dentro de aspas ainda recusa o filtro (matéria inconclusiva no cenário); contorno de ferramenta negada em triagem do consultor

### RAF-T7 — O dossiê de evidência chega ao fim nos três casos em que quebrava [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** Quem executa faz o dossiê de evidência chegar ao fim nos três casos em que hoje quebra: conteúdo antigo que não se lê como texto, módulo de apoio ausente e medida guardada em outra pasta.
- **Fundamento:** `DRF-11`; `F-17`; relatório `R-13` (auditoria reg. 25 e 26: `AE-105` e `AE-106` do `P-0754`).
- **Depende de:** `RAF-T3`
- **Operação do modelo:** `OP-7`
  - OP-7: Quem executa faz o dossiê de evidência chegar ao fim nos três casos em que hoje quebra: conteúdo antigo que não se lê como texto, módulo de apoio ausente e medida guardada em outra pasta.
  - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; carrega `rdo.py` e `caminhos.py` por caminho; roda `git` por subprocesso sem escrever no índice real, na lista de stash nem na árvore de trabalho. Primeira tarefa da etapa B: nasce `blocked` até o `go` do Marco 2 (`DRF-5`). O contrato do objeto é: "Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável."
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Contratos/classes:** assinaturas públicas inalteradas. Cinco regras:
  1. `_texto_do_ref(root: Path, ref: str, caminho: str) -> str` sai (os dois chamadores dela são os das regras 2 e 3) e, no lugar dela, entra `_texto_do_ref_ou_none(root: Path, ref: str, caminho: str) -> str | None`: os bytes de `_bytes_do_ref(root, ref, caminho)` decodificados em UTF-8; `None` quando não decodificam.
  2. `_nao_rastreado_mudou_desde_ref`: no ramo em que o arquivo de hoje se lê como texto, a linha `return _texto_do_ref(root, ref, caminho).splitlines() != texto_atual.splitlines()` passa a usar `_texto_do_ref_ou_none`; com `None`, devolve `_bytes_do_ref(root, ref, caminho) != (root / caminho).read_bytes()`; com texto, a comparação por linha de hoje.
  3. `_diff_para_arquivo`, no bloco do `TK-93a` (o que começa por `if _eh_nao_rastreado(root, caminho_rel) and _existe_no_ref(root, desde, caminho_rel):`): a linha `linhas_ref = _texto_do_ref(root, desde, caminho_rel).splitlines()` passa a usar `_texto_do_ref_ou_none`; com `None`, bytes iguais aos do disco devolvem `` (sem alteração desde `<ref>`) `` (a mesma linha que o bloco já usa, com o valor de `desde`) e bytes diferentes devolvem `(arquivo binário ou não-UTF-8 — trecho omitido)`; com texto, o diff de hoje.
  4. `main`, verbo `--atribuir`: a linha `rdo = _load_rdo(args.root)` entra num `try` próprio, antes do `try` que já existe; `ReviewEvidenceValidationError` imprime em stderr `review_evidence: FALHOU - <mensagem>` e devolve 1 — a mensagem é a de `_load_rdo`, `rdo.py: módulo não encontrado em '<caminho>'`. Com `rdo.py` presente, o segundo carregamento (dentro de `mapear_alvos_de_outras_tarefas`) acha o mesmo arquivo e não muda.
  5. `montar_documento`, com `dir_evidencia` dado: quando `Path(dir_evidencia) / f"{plano_id}-{dossie.tarefa_id}-medida.json"` não é arquivo, `caminho_medida` passa a ser `_caminhos.destino_medida(root, plano_path, dossie.tarefa_id)`; a medida ao lado do `--out` continua vencendo quando existe.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_review_evidence.py` o helper `_plano_em_pasta_com_medida(repo: Path, exit_medido: int) -> Path` e os cinco testes da seção `Testes`, no molde de `test_tf_nao_rastreado_binario_intocado_fica_fora_dos_tocados` e de `test_tf_evidencia_incorpora_medida` (fixture `_init_repo_com_baseline`, `review_evidence.capturar_ref`, `review_evidence.main`).
  2. Rodar `python -m pytest tests/test_review_evidence.py -q -k quebra` e conferir que os três TF falham e os dois TR passam.
  3. Aplicar as cinco regras de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 5 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5); `_texto_do_ref` sai por inteiro, sem sobrar sem chamador.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Os testes montam o próprio repositório em `tmp_path` com `_init_repo_com_baseline`; nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`.
  - Nenhuma linha que já existia em `tests/test_review_evidence.py` sai ou muda: o card só acrescenta ao fim do arquivo.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `_git` (os outros chamadores dependem da leitura em texto); não mudar o nome do arquivo de medida nem `caminhos.destino_medida` (é da `RAF-T15`); não mexer na marca de arquivo novo nem nos rótulos da lista (é da `RAF-T8`).
- **Contingências:**
  - se um teste que já existia em `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_quebra_ref_binario_hoje_texto_compara_bytes` — `dados.txt` não rastreado com os bytes `FF FE 00 81` no `ref`, regravado depois como texto `ola`: `coletar_arquivos_tocados(repo, desde=ref)` devolve `["dados.txt"]` e o trecho de `montar_trechos(repo, ["dados.txt"], 4000, tocados, desde=ref)` é exatamente `(arquivo binário ou não-UTF-8 — trecho omitido)` (hoje a leitura do `ref` em texto cai com exceção). TR `test_tr_quebra_ref_texto_segue_por_linha` — `dados.txt` com `ola` e quebra `\n` no `ref`, regravado com `\r\n`: `coletar_arquivos_tocados` devolve `[]` (a regra concorrente que comparasse sempre os bytes daria `["dados.txt"]`). TF `test_tf_quebra_atribuir_sem_rdo_falha_nomeado` — `--root` numa pasta sem `.claude/tools/rdo.py`, com `--atribuir`: `main` devolve 1 e o stderr contém `review_evidence: FALHOU - rdo.py: módulo não encontrado em` (hoje a exceção escapa sem essa linha). TF `test_tf_quebra_out_fora_acha_medida_na_pasta_do_plano` — plano em `docs/plans/P-0999-teste/plano.md` dentro do repositório, medida `P-0999-T1-medida.json` na `evidencia/` dele com `exit` 7, `--out` em `tmp_path/fora/T1.md`: exit 0 e o documento gravado contém `` | 1 | `python -c "print('a')"` | 7 | true | `` (hoje a seção diz `ausente`). TR `test_tr_quebra_out_com_medida_ao_lado_usa_a_do_lado` — o mesmo, com outra `P-0999-T1-medida.json` ao lado do `--out` com `exit` 3: o documento contém a linha com `3`, não a com `7`. Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_review_evidence.py -q -k quebra` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - dossiê de evidência.casos em que hoje quebra — compara o conteúdo bruto, falha com mensagem que nomeia o módulo ausente e acha a medida também na pasta do plano — Verificação 1
- **Fora do escopo desta tarefa:** o diff de arquivo rastreado cujo conteúdo não é UTF-8 (não pedido pela `R-13`; se a revisão o julgar defeito, vira `AE-<n>` na §9); a marca do binário novo e o rótulo único (`RAF-T8`); o nome da medida com o mundo (`RAF-T15`).
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** review_evidence.py: _texto_do_ref_ou_none substitui _texto_do_ref (chamadores _nao_rastreado_mudou_desde_ref e _diff_para_arquivo); main --atribuir isola _load_rdo no próprio try; montar_documento cai para caminhos.destino_medida quando a medida ao lado de dir_evidencia não existe; 5 testes novos, suíte 549
  - **Contrato:** o dossiê de evidência chega ao fim nos três casos que quebravam
  - **Não refazer:** as cinco regras e os 5 testes
  - **Pendente:** nenhum

### RAF-T7a — O ramo que o conteúdo antigo não texto nunca alcança sai do dossiê de evidência [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa tira de `.claude/tools/review_evidence.py` as duas comparações de bytes que a `RAF-T7` pôs no ramo em que o conteúdo do `ref` não se lê como texto e o de hoje se lê: os bytes de hoje decodificam em UTF-8 e os do `ref` não, logo nunca são iguais; a comparação de `_diff_para_arquivo` guarda um retorno inalcançável e a de `_nao_rastreado_mudou_desde_ref` é sempre verdadeira.
- **Fundamento:** `DRF-49`; `AE-135` (laudo da `RAF-T7`, ressalva 91); `DRF-11`; relatório `R-13`.
- **Depende de:** `RAF-T7`
- **Operação do modelo:** `OP-7`
  - OP-7: Quem executa faz o dossiê de evidência chegar ao fim nos três casos em que hoje quebra: conteúdo antigo que não se lê como texto, módulo de apoio ausente e medida guardada em outra pasta.
  - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; roda `git` por subprocesso sem escrever no índice real, na lista de stash nem na árvore de trabalho. O comportamento observável não muda: em todo caso alcançável, os dois ramos já devolvem o que passam a devolver sem a comparação. O contrato do objeto é: "Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável."
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
- **Contratos/classes:** assinaturas inalteradas. Duas regras, as duas no ramo `if texto_ref is None:`, que só se alcança com o arquivo de hoje decodificado em UTF-8 (`_texto_do_disco` não devolveu `None`) e o conteúdo do `ref` não decodificável:
  1. `_diff_para_arquivo`, bloco do `TK-93a`: o ramo devolve direto `(arquivo binário ou não-UTF-8 — trecho omitido)`; saem a linha `if _bytes_do_ref(root, desde, caminho_rel) == (root / caminho_rel).read_bytes():` e o `return` que ela guardava.
  2. `_nao_rastreado_mudou_desde_ref`: o ramo devolve `True` no lugar de `return _bytes_do_ref(root, ref, caminho) != (root / caminho).read_bytes()`.
  `_bytes_do_ref` segue com dois chamadores: `_texto_do_ref_ou_none` e o ramo de `_nao_rastreado_mudou_desde_ref` em que o arquivo de hoje não se lê como texto.
- **Passos:**
  1. Rodar a Verificação 1 e conferir que imprime `5` e sai 1.
  2. Aplicar as duas regras de `Contratos/classes`.
  3. Rodar a Verificação, `python -m pytest tests/test_review_evidence.py -q -k quebra` e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e não soma teste novo (referência datada: `83 passed` em `tests/test_review_evidence.py`, 2026-09-29, depois da `RAF-T7`).
  - Os cinco testes `quebra` da `RAF-T7` seguem verdes; `test_tf_quebra_ref_binario_hoje_texto_compara_bytes` passa pelos dois ramos.
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `_texto_do_ref_ou_none`, `_bytes_do_ref`, `_texto_do_disco` nem o ramo em que o arquivo de hoje não se lê como texto; não mexer na marca de arquivo novo nem nos rótulos da lista (é da `RAF-T8`); não acrescentar nem mudar teste.
- **Contingências:**
  - se um teste de `tests/test_review_evidence.py` cair depois do passo 2 → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo: o retorno que sai é inalcançável por construção e nenhum teste o exercita; a prova é a inspeção mecânica da Verificação 1 (item 12(ii) da Fase 4 do planejador). Regressão: os cinco testes `quebra` da `RAF-T7`, a suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Verificação:**
  1. `python -c "import pathlib,sys; t=pathlib.Path('.claude/tools/review_evidence.py').read_text(encoding='utf-8'); n=t.count('_bytes_do_ref('); print(n); sys.exit(0 if n==3 else 1)"` → `exit 0` — antes `exit 1`, depois `exit 0` (imprime `5` antes e `3` depois)
- **Pronto quando:**
  - dossiê de evidência.casos em que hoje quebra — o conteúdo antigo que não se lê como texto sai como binário, sem a comparação de bytes que nunca iguala — Verificação 1
- **Fora do escopo desta tarefa:** a marca do binário novo e o rótulo único (`RAF-T8`); o fim de linha da árvore de trabalho (medido em 2026-09-29: mais de cem arquivos rastreados `w/crlf` contra `eol=lf`, este entre eles).
- **Handover:** 2026-09-29 · para `RAF-T8`
  - **Entregue:** review_evidence.py: ramos texto_ref None de _diff_para_arquivo e _nao_rastreado_mudou_desde_ref sem a comparação de bytes inalcançável (_bytes_do_ref( conta 3); suíte 549
  - **Contrato:** conteúdo antigo não texto: trecho omitido e arquivo tratado como mudado, sem git show a mais
  - **Não refazer:** a remoção dos dois ramos
  - **Pendente:** nenhum

### RAF-T8 — O binário novo leva a marca de novo e o registro da orquestração tem um nome só [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa acerta duas marcas do dossiê de evidência: a de arquivo novo, que passa a valer também para o que não é texto, e a do registro da orquestração, que passa a ter o mesmo nome na lista e no resumo.
- **Fundamento:** `DRF-12`; `F-17` (dois rótulos para o mesmo fato: `atribuição: alheio` na lista, `Registro da orquestração` no resumo); relatório `R-14` (auditoria reg. 23 e 24).
- **Depende de:** `RAF-T7a`
- **Operação do modelo:** `OP-8`
  - OP-8: Quem executa acerta duas marcas do dossiê de evidência: a de arquivo novo, que passa a valer também para o que não é texto, e a do registro da orquestração, que passa a ter o mesmo nome na lista e no resumo.
  - precisa de: dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; roda `git` por subprocesso sem escrever no índice real, na lista de stash nem na árvore de trabalho. A mudança é de texto do dossiê de evidência; os baldes de `confrontar_escopo` e o veredito mecânico não mudam.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Contratos/classes:** assinaturas inalteradas. Três regras:
  1. `_diff_para_arquivo`, ramo da `AUF-T1` (com `desde`, não rastreado ausente de `<ref>`): a marca `` (arquivo novo — ausente em `<ref>`) `` e a quebra dela, que hoje só abrem o diff do texto, abrem também o retorno do arquivo que não se lê como texto, seguida de `(arquivo binário ou não-UTF-8 — trecho omitido)`.
  2. `_diff_para_arquivo`, ramo final sem `desde` (o `except UnicodeDecodeError:` da leitura do arquivo que existe na árvore): não rastreado devolve `` (arquivo novo — ausente em `HEAD`) ``, a quebra e `(arquivo binário ou não-UTF-8 — trecho omitido)`; rastreado segue com a linha de hoje, sem marca.
  3. `_renderizar`, seção `## Arquivos tocados`: arquivo que está em `escopo["registro_orquestracao"]` sai `atribuição: registro da orquestração`; os outros baldes alheios seguem `atribuição: alheio`; o coberto pelos alvos segue `atribuição: da entrega`.
  Os dois retornos das regras 1 e 2, exatos (as quebras são as do bloco; `<ref>` é o valor de `desde`):

  ```text
  (arquivo novo — ausente em `<ref>`)
  (arquivo binário ou não-UTF-8 — trecho omitido)
  ```

  ```text
  (arquivo novo — ausente em `HEAD`)
  (arquivo binário ou não-UTF-8 — trecho omitido)
  ```
- **Passos:**
  1. Em `tests/test_review_evidence.py`, no teste `test_tr_atribuicao_de_arquivos_tocados_cobre_os_quatro_baldes_alheios_de_confrontar_escopo`, trocar a asserção `` assert "- `docs/telemetria.tsv` — atribuição: alheio; estado git: `??`" in documento `` por `` assert "- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: `??`" in documento `` e, no docstring dele, o fim `ainda assim sai marcado` seguido de `` `alheio`. `` por `sai marcado com o nome do balde,` seguido de `` `registro da orquestração` (`R-14`, RAF-T8). `` — o significado da asserção mudou pela `R-14`, e ela se reescreve, não se remove.
  2. Acrescentar ao fim de `tests/test_review_evidence.py` os três testes da seção `Testes`.
  3. Rodar `python -m pytest tests/test_review_evidence.py -q -k "marca_e_rotulo or quatro_baldes_alheios"` e conferir que os dois TF e o teste reescrito falham.
  4. Aplicar as três regras de `Contratos/classes`.
  5. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 3 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Em `tests/test_review_evidence.py`, as únicas linhas que já existiam e mudam são a asserção e as duas linhas do docstring do passo 1; o resto só se acrescenta ao fim.
  - Os testes montam o próprio repositório em `tmp_path` com `_init_repo_com_baseline`; nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `confrontar_escopo`, `formatar_atribuicoes` (o `--atribuir` já usa `registro-da-orquestracao`) nem a linha `- Registro da orquestração (não atribuível a tarefa):` do resumo; não marcar como novo o arquivo rastreado; não mudar o curinga (é da `RAF-T9`).
- **Contingências:**
  - se um teste que já existia em `tests/test_review_evidence.py`, fora o reescrito no passo 1, cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_marca_e_rotulo_binario_novo_abre_com_a_marca` — `img.bin` com os bytes `FF FE 00 81` criado depois do `ref`: `_diff_para_arquivo(repo, "img.bin", desde=ref)` é exatamente o primeiro bloco de `Contratos/classes` com o valor do `ref`, e `_diff_para_arquivo(repo, "img.bin")` é exatamente o segundo (hoje os dois devolvem só a linha do binário, sem marca). TR `test_tr_marca_e_rotulo_binario_rastreado_alterado_sem_marca` — `img.bin` versionado e alterado depois do `ref`: o retorno com `desde=ref` não contém `(arquivo novo`. TF `test_tf_marca_e_rotulo_registro_da_orquestracao_na_lista` — `docs/DIARIO_DE_OBRAS.md` e `docs/nota.txt` não rastreados, fora dos alvos: o documento de `montar_documento` contém `` - `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: `??` `` e `` - `docs/nota.txt` — atribuição: alheio; estado git: `??` `` (hoje o primeiro sai `alheio`). Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_review_evidence.py -q -k marca_e_rotulo_binario` → `exit 0` — antes `exit 5`, depois `exit 0`
  2. `python -m pytest tests/test_review_evidence.py -q -k marca_e_rotulo_registro` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - dossiê de evidência.marca do arquivo novo que não é texto — os dois chegam com a mesma marca de arquivo novo — Verificação 1
  - dossiê de evidência.rótulo do registro da orquestração — a lista e o resumo usam o mesmo nome — Verificação 2
- **Fora do escopo desta tarefa:** o curinga do alvo (`RAF-T9`); o caminho acentuado (`RAF-T10`); as linhas removidas dos testes (`RAF-T11`).
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** review_evidence.py: binário novo abre com a marca (arquivo novo — ausente em <ref>/HEAD) antes do rótulo binário; arquivo do registro da orquestração sai 'atribuição: registro da orquestração' em Arquivos tocados; 3 testes novos, suíte 552
  - **Contrato:** rastreado alterado binário segue sem marca; demais baldes alheios seguem 'alheio'
  - **Não refazer:** as três regras e os testes
  - **Pendente:** nenhum

### RAF-T8a — A rubrica nomeia o rótulo do registro da orquestração [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa faz a frase da rubrica de revisão que conta os rótulos da seção `## Arquivos tocados` do dossiê de evidência nomear também `registro da orquestração`, o rótulo que a `RAF-T8` criou.
- **Fundamento:** `DRF-50`; `AE-137` (laudo da `RAF-T8`, ressalva 91); `DRF-12`; relatório `R-14`.
- **Depende de:** `RAF-T8`
- **Operação do modelo:** `OP-8`
  - OP-8: Quem executa acerta duas marcas do dossiê de evidência: a de arquivo novo, que passa a valer também para o que não é texto, e a do registro da orquestração, que passa a ter o mesmo nome na lista e no resumo.
  - precisa de: dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** doutrina do kit — a régua do revisor, `docs/RUBRICA_DE_REVISAO.md`, o parágrafo que abre com a seção `## Arquivos tocados` do dossiê de evidência, antes da nota de 2026-09-19; nenhum código muda. A frase segue dizendo que a atribuição vem da `confrontar_escopo`, que é onde o balde do registro da orquestração nasce.
- **Arquivos-alvo:**
  - `docs/RUBRICA_DE_REVISAO.md`
- **Passos:**
  1. Trocar a linha do texto antigo pelas duas do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card; as linhas vizinhas não mudam e não refluem).

     Texto antigo:

     ```text
     `Arquivos-alvo` da tarefa) ou `alheio` (fora deles), com o estado `git` que comprova a marcação —
     ```

     Texto novo:

     ```text
     `Arquivos-alvo` da tarefa), `registro da orquestração` (arquivo que quem conduz escreve por ofício,
     sem peso no veredito) ou `alheio` (os demais), com o estado `git` que comprova a marcação —
     ```
  2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `552 passed`, 2026-09-29, depois da `RAF-T8`).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - O arquivo segue com fim de linha LF (medido 2026-09-29: nenhum CR).
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar a nota de 2026-09-19 nem a dimensão `escopo`; não mexer na dimensão `testes` (é da `RAF-T12`); não editar `.claude/tools/review_evidence.py` nem `.claude/agents/pantonic-reviewer.md`.
- **Contingências:**
  - se o texto antigo do passo 1 não existir verbatim em `docs/RUBRICA_DE_REVISAO.md` → parar e sinalizar `blocked` razão `premissa`.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo: a mudança é de redação e a prova é o recorte do literal na Verificação 1. Regressão: a suíte inteira.
- **Verificação:**
  1. `python -c "import sys;from pathlib import Path;t=Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8');a=t.count('(fora deles), com o estado');b=t.count('(arquivo que quem conduz escreve por ofício,');print('arquivos=%d-%d'%(a,b));sys.exit(0 if (a,b)==(0,1) else 1)"` → `exit 0` — antes `exit 1`, depois `exit 0` (imprime `arquivos=1-0` antes e `arquivos=0-1` depois)
- **Pronto quando:**
  - dossiê de evidência.rótulo do registro da orquestração — a rubrica nomeia o rótulo que a lista do dossiê usa — Verificação 1
- **Fora do escopo desta tarefa:** o critério da asserção removida (`RAF-T12`); o curinga do alvo (`RAF-T9`).
- **Handover:** 2026-09-29 · para `RAF-T12`
  - **Entregue:** docs/RUBRICA_DE_REVISAO.md §3 nomeia os três rótulos de '## Arquivos tocados': da entrega, alheio e registro da orquestração (arquivo que quem conduz escreve por ofício, sem peso no veredito)
  - **Contrato:** a rubrica e o review_evidence.py usam o mesmo nome para o registro da orquestração
  - **Não refazer:** a troca da frase da rubrica
  - **Pendente:** nenhum

### RAF-T9 — O curinga do alvo casa como na linha de comando [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa faz o dossiê de evidência ler o curinga do alvo como a linha de comando o lê, com a estrela presa a uma pasta e a estrela dupla alcançando as subpastas.
- **Fundamento:** `DRF-31`; `F-1` (Python 3.12: `PurePath.full_match` só existe no 3.13), `F-17` (0 alvos com `*` nos planos vivos); relatório `R-30` (`AE-104` do `P-0754`).
- **Depende de:** `RAF-T8`
- **Operação do modelo:** `OP-9`
  - OP-9: Quem executa faz o dossiê de evidência ler o curinga do alvo como a linha de comando o lê, com a estrela presa a uma pasta e a estrela dupla alcançando as subpastas.
  - precisa de: dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; a tradução do curinga é própria, para regex (sem `fnmatch`, sem `glob`, sem `PurePath.full_match`); o curinga casa só contra os arquivos tocados, nunca contra a árvore inteira (`DAU-22` do `P-0754`, inalterada).
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Contratos/classes:** duas funções novas, logo depois de `_eh_alvo_curinga`:
  1. `_curinga_para_regex(padrao: str) -> str` — percorre o padrão da esquerda para a direita: `**/` vira `(?:[^/]*/)*` (zero ou mais pastas); `**` que não é seguido de `/` vira `.*`; `*` vira `[^/]*`; `?` vira `[^/]`; qualquer outro caractere entra com `re.escape`.
  2. `_casa_curinga(caminho: str, padrao: str) -> bool` — `re.fullmatch(_curinga_para_regex(padrao), caminho) is not None`.
  As duas chamadas de `fnmatch.fnmatchcase` (em `confrontar_escopo`, função interna `coberto`, e em `montar_trechos`, no ramo do alvo com curinga) passam a `_casa_curinga`, com os mesmos argumentos, na mesma ordem (caminho normalizado, padrão normalizado); `import fnmatch` sai da lista de imports; o docstring de `_eh_alvo_curinga` troca `fnmatch` por `_casa_curinga`.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_review_evidence.py` os dois testes da seção `Testes`.
  2. Rodar `python -m pytest tests/test_review_evidence.py -q -k glob_estrela` e conferir que os dois falham.
  3. Aplicar `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A); os testes do curinga da `AUF-T3` (`test_tf_alvo_com_curinga_casa_os_tocados`, `test_tr_alvo_com_curinga_sem_tocado_diz_que_nada_casa`) seguem verdes sem mudança.
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Nenhuma linha que já existia em `tests/test_review_evidence.py` sai ou muda: o card só acrescenta ao fim do arquivo.
  - Os testes montam o próprio repositório em `tmp_path` com `_init_repo_com_baseline`; nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não expandir o curinga contra a árvore inteira; não mudar `_eh_alvo_curinga`, `_CAMINHO_RE` nem `_tarefa_dona`; não aceitar `[`, `]` ou `{` como curinga (entram como literal).
- **Contingências:**
  - se um teste que já existia em `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_glob_estrela_nao_atravessa_pasta` — `relatorios/a.md` e `relatorios/sub/x.md` criados depois do `ref`, alvo `relatorios/*.md`: `confrontar_escopo(tocados, ["relatorios/*.md"], repo)["fora_dos_alvos"]` é `["relatorios/sub/x.md"]` e as chaves de `montar_trechos(repo, ["relatorios/*.md"], 4000, tocados, desde=ref)` são só `relatorios/a.md` (hoje o `fnmatch` casa os dois). TF `test_tf_glob_estrela_dupla_alcanca_subpastas` — os mesmos arquivos, alvo `relatorios/**/*.md`: `fora_dos_alvos` é `[]` e as chaves são `relatorios/a.md` e `relatorios/sub/x.md` (hoje o `fnmatch` deixa `relatorios/a.md` de fora, porque exige uma `/` depois de `relatorios/`). Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_review_evidence.py -q -k glob_estrela` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - dossiê de evidência.curinga do alvo — a estrela fica numa pasta só, e a estrela dupla alcança as subpastas, como na linha de comando — Verificação 1
- **Fora do escopo desta tarefa:** o curinga no alvo de outra tarefa do mesmo plano (`_tarefa_dona`, não pedido pela `R-30`); o caminho acentuado (`RAF-T10`).
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** review_evidence.py: _curinga_para_regex e _casa_curinga substituem fnmatch.fnmatchcase em confrontar_escopo e montar_trechos (* não atravessa pasta, ** alcança subpastas); 2 testes novos, suíte 554
  - **Contrato:** curinga de Arquivos-alvo casa como na linha de comando
  - **Não refazer:** _casa_curinga e os 2 testes
  - **Pendente:** nenhum

### RAF-T9a — O teste do curinga da AUF-T3 nomeia o mecanismo que casa o alvo [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa faz o docstring de `test_tf_alvo_com_curinga_casa_os_tocados`, em `tests/test_review_evidence.py`, nomear `_casa_curinga`, que a `RAF-T9` pôs no lugar do `fnmatch`, em vez de dizer que o curinga casa por `fnmatch`.
- **Fundamento:** `DRF-51`; `AE-140` (laudo da `RAF-T9`, ressalva 91); `DRF-31`; relatório `R-30`.
- **Depende de:** `RAF-T9`
- **Operação do modelo:** `OP-9`
  - OP-9: Quem executa faz o dossiê de evidência ler o curinga do alvo como a linha de comando o lê, com a estrela presa a uma pasta e a estrela dupla alcançando as subpastas.
  - precisa de: dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** teste do instrumento do kit, `tests/test_review_evidence.py`, só o docstring do teste da `AUF-T3`; nenhum código nem asserção muda. A `RAF-T9` congelou as linhas que já existiam no arquivo e mandou trocar só o docstring de `_eh_alvo_curinga`; este é o outro texto que a entrega dela tornou falso.
- **Arquivos-alvo:**
  - `tests/test_review_evidence.py`
- **Passos:**
  1. No teste `test_tf_alvo_com_curinga_casa_os_tocados`, trocar as três linhas do docstring pelas três do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os quatro espaços do corpo da função; o resto do teste não muda).

     Texto antigo:

     ```text
         """AUF-T3: alvo com curinga (`relatorios/*.md`) casa, por `fnmatch`, cada tocado que bate com
         o padrão — não a regra antiga, que descartava o literal e dava os dois arquivos como fora dos
         alvos com uma entrada só sob a chave do padrão."""
     ```

     Texto novo:

     ```text
         """AUF-T3: alvo com curinga (`relatorios/*.md`) casa, por `_casa_curinga` (RAF-T9), cada
         tocado que bate com o padrão — não a regra antiga, que descartava o literal e dava os dois
         arquivos como fora dos alvos com uma entrada só sob a chave do padrão."""
     ```
  2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `88 passed` em `tests/test_review_evidence.py`, 2026-09-29, depois da `RAF-T9`).
  - `test_tf_alvo_com_curinga_casa_os_tocados` e `test_tr_alvo_com_curinga_sem_tocado_diz_que_nada_casa` seguem verdes.
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Em `tests/test_review_evidence.py`, as únicas linhas que mudam são as três do docstring do passo 1.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não editar `.claude/tools/review_evidence.py`; não mudar os docstrings dos dois testes `glob_estrela` da `RAF-T9` (o "hoje" deles nomeia a regra concorrente na data da autoria, convenção dos docstrings de teste do kit).
- **Contingências:**
  - se o texto antigo do passo 1 não existir verbatim em `tests/test_review_evidence.py` → parar e sinalizar `blocked` razão `premissa`.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo: a mudança é de redação e a prova é o recorte do literal na Verificação 1. Regressão: o teste da `AUF-T3`, a suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Verificação:**
  1. `python -c "import pathlib,sys; t=pathlib.Path('tests/test_review_evidence.py').read_text(encoding='utf-8'); q=chr(96); a=t.count('por '+q+'fnmatch'+q); d=t.count('por '+q+'_casa_curinga'+q+' (RAF-T9)'); print('docstring=%d-%d'%(a,d)); sys.exit(0 if (a,d)==(0,1) else 1)"` → `exit 0` — antes `exit 1`, depois `exit 0` (imprime `docstring=1-0` antes e `docstring=0-1` depois)
- **Pronto quando:**
  - dossiê de evidência.curinga do alvo — o teste do curinga da `AUF-T3` nomeia o mecanismo que casa o alvo, `_casa_curinga` — Verificação 1
- **Fora do escopo desta tarefa:** o caminho acentuado (`RAF-T10`); o fim de linha do arquivo (medido 2026-09-29: `w/crlf` contra `eol=lf`, fora do P-0755).
- **Handover:** 2026-09-29 · para `RAF-T10`
  - **Entregue:** docstring de test_tf_alvo_com_curinga_casa_os_tocados (tests/test_review_evidence.py:1459-1461) cita _casa_curinga (RAF-T9) no lugar de fnmatch
  - **Contrato:** nenhum docstring de teste-alvo nomeia o fnmatch como mecanismo vigente
  - **Não refazer:** a troca do docstring
  - **Pendente:** nenhum

### RAF-T10 — O caminho acentuado chega inteiro ao dossiê de evidência [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa faz o dossiê de evidência receber inteiro o nome de arquivo acentuado que o versionador lista, em vez de dá-lo por ausente.
- **Fundamento:** `DRF-32`; `F-17` (as duas leituras do porcelain sem `-z`); relatório `R-31` (`AE-99` do `P-0754`).
- **Depende de:** `RAF-T9a`
- **Operação do modelo:** `OP-10`
  - OP-10: Quem executa faz o dossiê de evidência receber inteiro o nome de arquivo acentuado que o versionador lista, em vez de dá-lo por ausente.
  - precisa de: dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; roda `git` por subprocesso sem escrever no índice real, na lista de stash nem na árvore de trabalho. Com `-z`, o `git status` entrega o caminho cru (sem aspas nem escape octal), qualquer que seja o `core.quotepath` da máquina.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Contratos/classes:**
  1. `_extrair_caminho_status(linha: str) -> str` sai e, no lugar dela, entra `_entradas_status(root: Path) -> list[tuple[str, str]]`: roda `_git(["status", "--porcelain=v1", "-z", "--untracked-files=all"], root)`, separa a saída por NUL e devolve, na ordem do `git`, `(código XY, caminho)` de cada campo com 4 caracteres ou mais (`campo[:2]`, `campo[3:]`); quando o código contém `R` ou `C`, o campo seguinte (o caminho de origem) se consome sem virar entrada.
  2. `coletar_arquivos_tocados(root: Path, desde: str | None = None) -> list[str]` e `coletar_estado_git(root: Path, desde: str | None = None) -> dict[str, str]` — assinaturas inalteradas — trocam a leitura por linha da saída de `git status --porcelain=v1 --untracked-files=all` por `_entradas_status(root)`: sem `desde`, todo caminho entra nos tocados; com `desde`, o filtro dos não rastreados passa a ser `código == "??"`; em `coletar_estado_git`, a chave é o caminho e o valor é o código. O resto das duas funções (recorte por `<ref>`, `git diff <ref> --name-only`, `git diff <ref> --name-status`) não muda; o docstring de `coletar_estado_git` troca `_extrair_caminho_status` por `_entradas_status`.
- **Passos:**
  1. Em `tests/test_review_evidence.py`, no teste `test_tf_caminho_acentuado_do_status_entra_nos_tocados_pelo_ramo_de_caminho_ausente` (o nome fica), trocar a única asserção do teste (a que compara `tocados` com a lista do caminho em escape octal) por `assert tocados == ["ação.txt"]` e o docstring pelas três linhas do bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os quatro espaços do corpo da função): o significado do teste mudou pela `R-31`, e ele se reescreve, não se remove.

     ```text
         """AUF-T2, reescrito pela RAF-T10 (`R-31`): com `core.quotepath` ligado, o `git status` sem `-z`
         devolveria o caminho acentuado entre aspas com escape octal; com `-z` (`_entradas_status`) o
         caminho chega cru, e o não rastreado criado depois do `ref` entra nos tocados como `ação.txt`."""
     ```
  2. Acrescentar ao fim de `tests/test_review_evidence.py` os dois testes da seção `Testes`.
  3. Rodar `python -m pytest tests/test_review_evidence.py -q -k "acento_z or caminho_acentuado"` e conferir que o TF novo e o teste reescrito falham e o TR passa.
  4. Aplicar os itens 1 e 2 de `Contratos/classes`.
  5. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5); `_extrair_caminho_status` sai por inteiro, sem sobrar sem chamador.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Em `tests/test_review_evidence.py`, as únicas linhas que já existiam e mudam são a asserção e o docstring do passo 1; o resto só se acrescenta ao fim.
  - Os testes montam o próprio repositório em `tmp_path` com `_init_repo_com_baseline` e ligam `core.quotepath` só nele; nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `_eh_nao_rastreado` (ele só lê o código `??` do caminho que recebe); não mudar as leituras de `git diff <ref> --name-only` e `git diff <ref> --name-status`; não depender do `core.quotepath` global da máquina.
- **Contingências:**
  - se um teste que já existia em `tests/test_review_evidence.py`, fora o reescrito no passo 1, cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_acento_z_nao_rastreado_chega_com_o_diff` — `core.quotepath` ligado no repositório do teste, `ação.txt` com a linha `linha-1` criado depois do `ref`: `coletar_arquivos_tocados(repo, desde=ref)` é `["ação.txt"]`, o trecho de `montar_trechos(repo, ["ação.txt"], 4000, tocados, desde=ref)` contém `+linha-1`, e `coletar_estado_git(repo)["ação.txt"]` é `??` (hoje o caminho chega em escape octal e o trecho sai `arquivo ausente`). TR `test_tr_acento_z_renomeado_usa_o_caminho_novo` — `git mv src/b.py src/c.py` no repositório do teste: `coletar_estado_git(repo)["src/c.py"]` é `R ` (R e espaço), `src/b.py` não é chave, e `coletar_arquivos_tocados(repo)` é `["src/c.py"]` (a regra concorrente que tratasse a origem da renomeação como entrada daria `src/b.py` também). Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_review_evidence.py -q -k acento_z` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - dossiê de evidência.caminho acentuado — chega com a sua diferença, como qualquer outro — Verificação 1
- **Fora do escopo desta tarefa:** o caminho acentuado de arquivo rastreado nas saídas de `git diff <ref> --name-only` e `--name-status` (não pedido pela `R-31`; se a revisão o julgar defeito, vira `AE-<n>` na §9); as linhas removidas dos testes (`RAF-T11`).
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** review_evidence.py: _entradas_status(root) lê git status --porcelain=v1 -z (substitui _extrair_caminho_status) em coletar_arquivos_tocados e coletar_estado_git; 2 testes novos, suíte 556
  - **Contrato:** arquivo acentuado não rastreado ou alterado na árvore chega com o nome inteiro pelo git status
  - **Não refazer:** _entradas_status e os testes
  - **Pendente:** as leituras git diff <ref> --name-only/--name-status (review_evidence.py:395, :421) e _CAMINHO_RE ASCII (:124) ainda não cobrem acento; modelo v2 pendente da OP-10; em triagem do consultor

### RAF-T10a — O arquivo acentuado já rastreado chega com um nome só ao dossiê de evidência [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa faz o dossiê de evidência receber inteiro, e com um nome só, o arquivo acentuado já rastreado que a entrega alterou ou commitou depois do `ref` — na lista dos tocados, no estado do versionador, no resumo e no cabeçalho do trecho —, e reconhecer como caminho o alvo acentuado declarado no card — o que a `RAF-T10` deixou de fora ao corrigir só a leitura do `git status`.
- **Fundamento:** `DRF-52`; `AE-142`, `AE-143`, `AE-144`, `AE-145` (laudo da `RAF-T10`, ressalva 91); `DRF-32`; relatório `R-31`; versão 2 pendente do modelo (§1A, propriedade `dossiê de evidência.caminho acentuado`).
- **Depende de:** `RAF-T10`
- **Operação do modelo:** `OP-10`
  - OP-10: Quem executa faz o dossiê de evidência receber inteiro o nome de arquivo acentuado que o versionador lista, em vez de dá-lo por ausente.
  - precisa de: dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; roda `git` por subprocesso sem escrever no índice real, na lista de stash nem na árvore de trabalho. Sem `-z`, o `git diff` põe o caminho acentuado entre aspas com escape octal quando o `core.quotepath` está ligado (medido no laudo da `RAF-T10` e no ensaio do consultor); com `-z`, o caminho chega cru.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Contratos/classes:**
  1. Entra `_entradas_diff(root: Path, ref: str) -> list[tuple[str, str]]`, ao lado de `_entradas_status`: roda `git diff <ref> --name-status -z` e devolve, na ordem do `git`, `(letra, caminho)` de cada arquivo; quando a letra começa por `R` ou `C`, vêm dois caminhos, o caminho é o segundo (o novo) e a origem não vira entrada.
  2. `coletar_arquivos_tocados(root: Path, desde: str | None = None) -> list[str]` e `coletar_estado_git(root: Path, desde: str | None = None) -> dict[str, str]` — assinaturas inalteradas — trocam as leituras por linha de `git diff <ref> --name-only` e de `git diff <ref> --name-status` por `_entradas_diff(root, desde)`; ficam o filtro dos não rastreados já julgados por conteúdo (`nao_rastreados`) e o `setdefault` com o valor `<letra> (commitado desde <ref>)`.
  3. `_CAMINHO_RE` aceita letra acentuada onde hoje aceita letra ASCII; o resto da gramática da `DB-27` fica (sem espaço, e com extensão, barra ou barra final).
  4. `_git` roda o `git` com `-c core.quotepath=false` antes dos argumentos: o texto do `git` que o dossiê cola (o resumo `--stat` e o cabeçalho do diff unificado de cada trecho) mostra o nome acentuado cru; as leituras que a revisão confronta seguem por `-z` (`_entradas_status` e o item 1).
  5. Nos docstrings das duas funções do item 2, cada trecho antigo do bloco abaixo sai e o novo entra no lugar (o trecho antigo pode atravessar uma quebra de linha do docstring; o novo entra no lugar dele sem quebra nova, e o resto do parágrafo não reflui):

     ```text
     coletar_arquivos_tocados:
       antigo: `<ref>` (`git diff <ref> --name-only`), em vez
       novo:   `<ref>` (`_entradas_diff`), em vez
       antigo: aparece em `git diff <ref> --name-only` (que o dá
       novo:   aparece como tocado de `_entradas_diff` (que o dá
       antigo: a que não existe no disco como veio do `git status` (nome entre aspas com escape octal, por exemplo).
       novo:   a que não existe no disco como veio do `git status`.
     coletar_estado_git:
       antigo: Código `XY` de `git status --porcelain=v1 --untracked-files=all` por caminho
       novo:   Código `XY` de `git status --porcelain=v1 -z --untracked-files=all` por caminho
       antigo: entra a letra de `git diff <ref> --name-status`, marcada
       novo:   entra a letra de `_entradas_diff`, marcada
       antigo: Para renomeação (`R100\t<velho>\t<novo>`), a chave é o último campo da linha e a letra é o primeiro campo inteiro (`R100`).
       novo:   Para renomeação, a chave é o caminho novo e a letra é o campo inteiro (`R100`).
     ```
- **Passos:**
  1. Acrescentar ao fim de `tests/test_review_evidence.py` os três testes da seção `Testes`.
  2. Rodar `python -m pytest tests/test_review_evidence.py -q -k "acento_diff or acento_alvo"` e conferir que os dois TF falham e o TR passa.
  3. Aplicar os itens 1 a 5 de `Contratos/classes`.
  4. Rodar as Verificações e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 3 testes novos (referência datada: `90 passed` em `tests/test_review_evidence.py`, 2026-09-29, depois da `RAF-T10`).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Em `tests/test_review_evidence.py`, nenhuma linha que já existia muda; os testes novos só se acrescentam ao fim.
  - Os testes montam o próprio repositório em `tmp_path` com `_init_repo_com_baseline` e ligam `core.quotepath` só nele; nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `_entradas_status` nem `_eh_nao_rastreado`; não mudar `_EXTENSAO_RE`; não depender do `core.quotepath` global da máquina.
- **Contingências:**
  - se um teste que já existia em `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_acento_diff_commitado_chega_com_um_nome_so` — `ação.md` (linha `linha-1`) commitado sobre o repositório de `_init_repo_com_baseline`, `core.quotepath` ligado, `ref` capturado, depois `ação.md` ganha `linha-2` e se commita (árvore limpa, só o `git diff` o vê): `coletar_arquivos_tocados(repo, desde=ref)` é `["ação.md"]`, `coletar_estado_git(repo, desde=ref)` é `{"ação.md": f"M (commitado desde {ref})"}` e o trecho de `montar_trechos(repo, ["ação.md"], 4000, tocados, desde=ref)` contém `+linha-2`; nem esse trecho nem `coletar_diff_stat(repo, desde=ref)` trazem o escape octal `\303`, e o resumo contém `ação.md` (hoje o tocado, o cabeçalho do trecho e o resumo chegam entre aspas com escape octal). TF `test_tf_acento_alvo_acentuado_e_caminho` — com o campo `arquivos-alvo` igual a `` - `docs/ação.md` `` (o caminho entre crases): `extrair_arquivos_alvo(campos)` é `["docs/ação.md"]` e `extrair_literais_nao_caminho(campos)` é `[]` (hoje `[]` e o literal descartado). TR `test_tr_acento_diff_renomeado_commitado_usa_o_caminho_novo` — `ref` capturado, `git mv src/b.py src/c.py` e commit: `coletar_estado_git(repo, desde=ref)` é `{"src/c.py": f"R100 (commitado desde {ref})"}` e `coletar_arquivos_tocados(repo, desde=ref)` é `["src/c.py"]` (a regra concorrente que tratasse a origem como entrada daria `src/b.py` também). Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_review_evidence.py -q -k "acento_diff or acento_alvo"` → `exit 0` — antes `exit 5`, depois `exit 0`
  2. `python -c "import pathlib,sys; t=pathlib.Path('.claude/tools/review_evidence.py').read_text(encoding='utf-8'); q=chr(96); p=chr(34); a=t.count(p+'--name-only'+p); b=t.count('escape octal, por')+t.count('o último campo da linha'); c=t.count(p+'--name-status'+p+', '+p+'-z'+p); d=t.count('-z --untracked-files=all'+q+' por caminho'); e=t.count(p+'-c'+p+', '+p+'core.quotepath=false'+p); print('diff=%d-%d-%d-%d-%d'%(a,b,c,d,e)); sys.exit(0 if (a,b,c,d,e)==(0,0,1,1,1) else 1)"` → `exit 0` — antes `exit 1`, depois `exit 0` (imprime `diff=1-2-0-0-0` antes e `diff=0-0-1-1-1` depois)
- **Pronto quando:**
  - dossiê de evidência.caminho acentuado — o arquivo acentuado, novo ou já rastreado, chega com a sua diferença e com um nome só, como qualquer outro — Verificações 1 e 2
- **Fora do escopo desta tarefa:** a extensão acentuada (`_EXTENSAO_RE`); as linhas removidas dos testes (`RAF-T11`).
- **Handover:** 2026-09-29 · para `RAF-T11`
  - **Entregue:** review_evidence.py: _entradas_diff(root, ref) lê git diff <ref> --name-status -z (chave = caminho novo na renomeação); _git roda com -c core.quotepath=false; _CAMINHO_RE aceita letra acentuada; docstrings acertados; 3 testes novos, suíte 559
  - **Contrato:** arquivo acentuado, novo ou já rastreado, chega com a sua diferença e com um nome só (estado final da v2 pendente da OP-10)
  - **Não refazer:** _entradas_diff, o quotepath no _git, o _CAMINHO_RE e os testes
  - **Pendente:** nenhum

### RAF-T11 — A evidência mostra as linhas que a entrega tirou dos testes [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** Quem executa faz o dossiê de evidência mostrar, para cada arquivo de teste entre os alvos do card, as linhas que a entrega removeu.
- **Fundamento:** `DRF-33`; `F-17` (nenhuma lógica reconhece arquivo de teste), `F-18`; relatório `R-12` (`AE-97` e `AE-98` do `P-0754`: a remoção de uma asserção vizinha passou verde).
- **Depende de:** `RAF-T10a`
- **Operação do modelo:** `OP-11`
  - OP-11: Quem executa faz o dossiê de evidência mostrar, para cada arquivo de teste entre os alvos do card, as linhas que a entrega removeu.
  - precisa de: dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; roda `git` por subprocesso sem escrever no índice real, na lista de stash nem na árvore de trabalho. A seção nova informa, não julga: o veredito sobre a asserção removida é do revisor pela rubrica (`RAF-T12`), e o dossiê não ganha veredito mecânico novo.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Contratos/classes:** quatro regras, com as funções novas logo antes de `def _renderizar(`:
  1. `_eh_alvo_de_teste(alvo: str) -> bool` — com separador normalizado (`_normalizar_separador`), verdadeiro quando o caminho começa por `tests/` e o nome do arquivo começa por `test_` e termina em `.py`.
  2. `linhas_removidas_de_teste(root: Path, arquivos_alvo: list[str], desde: str | None = None) -> dict[str, list[str]]` — para cada alvo, na ordem, que não é curinga (`_eh_alvo_curinga`) e é de teste: a chave é o alvo como veio, e o valor são as linhas do texto de `_diff_para_arquivo(root, alvo, desde)` que começam por `-` e não por `---`, na ordem.
  3. `_renderizar_removidas_de_teste(removidas: dict[str, list[str]]) -> list[str]` — a seção, nesta forma exata: a linha `## Linhas removidas dos testes`; sem chave, a linha `- nenhum arquivo de teste entre os alvos`; por chave sem linha removida, `` ### `<caminho>` — nenhuma linha removida ``; por chave com linhas, `` ### `<caminho>` — <n> linha(s) removida(s) ``, uma linha com três crases, as linhas removidas como vieram e outra linha com três crases.
  4. `_renderizar(...)` ganha o parâmetro de palavra-chave `removidas_teste: dict[str, list[str]] | None = None` e põe a seção logo depois dos trechos de diff (depois da linha vazia que fecha a seção de trechos), seguida de uma linha vazia, antes da `## Medida do executor`; `montar_documento` passa `removidas_teste=linhas_removidas_de_teste(root, arquivos_alvo, desde)`.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_review_evidence.py` o helper `_repo_com_teste_versionado(tmp_path: Path) -> Path` (repositório de `_init_repo_com_baseline` com `tests/test_a.py` versionado, de três linhas: `def test_a():`, `    assert 1 == 1` e `    assert 2 == 2`) e os três testes da seção `Testes`.
  2. Rodar `python -m pytest tests/test_review_evidence.py -q -k removidas_de_teste` e conferir que os três falham.
  3. Aplicar as quatro regras de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 3 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Nenhuma linha que já existia em `tests/test_review_evidence.py` sai ou muda: o card só acrescenta ao fim do arquivo.
  - Os testes montam o próprio repositório em `tmp_path` com `_init_repo_com_baseline`; nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `montar_trechos` nem o teto dos trechos; não julgar a remoção (nenhum veredito novo); não editar `docs/RUBRICA_DE_REVISAO.md` (o critério é da `RAF-T12`).
- **Contingências:**
  - se um teste que já existia em `tests/test_review_evidence.py` cair por causa da seção nova no documento → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_removidas_de_teste_aparecem_na_evidencia` — `tests/test_a.py` versionado, `ref` capturado, depois a linha `    assert 2 == 2` sai; plano com alvo `tests/test_a.py`; o documento de `montar_documento(..., desde=ref)` tem as linhas `## Linhas removidas dos testes`, `` ### `tests/test_a.py` — 1 linha(s) removida(s) `` e `-    assert 2 == 2` (hoje a seção não existe). TR `test_tr_removidas_de_teste_so_acrescimo_diz_nenhuma` — o arquivo só ganha a linha `    assert 3 == 3`; alvos `tests/test_a.py` e `src/b.py`: o documento tem a linha `` ### `tests/test_a.py` — nenhuma linha removida `` e, depois do título da seção, nenhuma entrada de `src/b.py` (a regra concorrente que listasse todo alvo daria uma entrada para ele). TR `test_tr_removidas_de_teste_sem_alvo_de_teste` — alvo só `src/b.py`: o documento tem a linha `- nenhum arquivo de teste entre os alvos`. Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_review_evidence.py -q -k removidas_de_teste` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - dossiê de evidência.linhas removidas dos testes — para cada arquivo de teste entre os alvos, a evidência mostra as linhas que saíram — Verificação 1
- **Fora do escopo desta tarefa:** o critério da rubrica que reprova a asserção removida (`RAF-T12`); a leitura por `numstat` (o texto do diff já dá as linhas).
- **Handover:** 2026-09-29 · para `RAF-T12`
  - **Entregue:** review_evidence.py: o dossiê de evidência mostra, para cada arquivo de teste entre os alvos do card, as linhas que a entrega removeu (ver RDO RAF-T11)
  - **Contrato:** remoção de linha em arquivo de teste-alvo fica visível ao revisor no dossiê
  - **Não refazer:** a seção de linhas removidas e os testes
  - **Pendente:** nenhum

### RAF-T11a — A seção das linhas removidas cobre o teste sob curinga ou diretório e a linha que começa por dois hífens [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa faz a seção `## Linhas removidas dos testes` do dossiê de evidência mostrar também o arquivo de teste que um alvo curinga ou diretório cobre e a linha removida cujo conteúdo começa por `--`.
- **Fundamento:** `DRF-53`; `AE-149` (laudo da `RAF-T11`, ressalva 91); `DRF-33`; `F-17`; relatório `R-12`.
- **Depende de:** `RAF-T11`
- **Operação do modelo:** `OP-11`
  - OP-11: Quem executa faz o dossiê de evidência mostrar, para cada arquivo de teste entre os alvos do card, as linhas que a entrega removeu.
  - precisa de: dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; roda `git` por subprocesso sem escrever no índice real, na lista de stash nem na árvore de trabalho. A forma da seção (`_renderizar_removidas_de_teste`) não muda; muda quais arquivos entram nela e quais linhas contam como removidas. A seção informa, não julga.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Contratos/classes:** três regras em `.claude/tools/review_evidence.py`:
  1. `_linhas_removidas_do_diff(texto: str) -> list[str]`, nova, logo antes de `def linhas_removidas_de_teste(` — as linhas do texto que começam por `-` e vêm depois da primeira linha que começa por `@@`, na ordem; texto sem linha `@@` dá lista vazia. O cabeçalho (`--- a/...`) fica antes do primeiro `@@` e sai; a linha removida cujo conteúdo começa por `--` fica.
  2. `linhas_removidas_de_teste(root: Path, arquivos_alvo: list[str], desde: str | None = None, tocados: list[str] | None = None) -> dict[str, list[str]]` — para cada alvo, na ordem, os caminhos que ele cobre, pela mesma expansão de `montar_trechos`: alvo curinga (`_eh_alvo_curinga`) cobre os `tocados` que casam por `_casa_curinga` (separador normalizado nos dois lados); alvo diretório (`tocados` não vazio e `_eh_alvo_diretorio`) cobre os `tocados` sob o prefixo `<alvo>/` normalizado; outro alvo cobre a si mesmo, como veio. Cada caminho coberto que é de teste (`_eh_alvo_de_teste`) e cuja forma normalizada (`_normalizar_separador`) ainda não tem chave ganha a chave do caminho como veio e o valor `_linhas_removidas_do_diff(_diff_para_arquivo(root, caminho, desde))`. O docstring deixa de dizer que o curinga fica de fora e que o filtro é o de `---`.
  3. `montar_documento` passa os tocados que já coleta: `removidas_teste=linhas_removidas_de_teste(root, arquivos_alvo, desde, tocados)`.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_review_evidence.py` o helper `_secao_removidas(documento: str) -> str` (o trecho do documento depois de `## Linhas removidas dos testes` e antes de `## Medida do executor`) e os quatro testes da seção `Testes`.
  2. Rodar a Verificação 1 e conferir `3 failed, 1 passed` (o TR passa antes).
  3. Aplicar as três regras de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 4 testes novos (referência datada: `562 passed`, 2026-09-29, revisão da `RAF-T11`).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Nenhuma linha que já existia em `tests/test_review_evidence.py` sai ou muda: o card só acrescenta ao fim do arquivo.
  - Os testes montam o próprio repositório em `tmp_path` com `_repo_com_teste_versionado`; o `add` e o `commit` do TF dos dois hífens rodam por `_run_git` só nesse repositório; nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `montar_trechos`, `_renderizar_removidas_de_teste` nem os textos da seção; não julgar a remoção (nenhum veredito novo); não editar `docs/RUBRICA_DE_REVISAO.md` (o critério é da `RAF-T12`).
- **Contingências:**
  - se um teste que já existia em `tests/test_review_evidence.py` cair por causa da mudança → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_removidas_de_teste_curinga_cobre_teste_tocado` — repositório de `_repo_com_teste_versionado`, `ref` capturado, depois a linha `    assert 2 == 2` sai; plano com alvo `tests/test_*.py`; a seção (`_secao_removidas`) tem `` ### `tests/test_a.py` — 1 linha(s) removida(s) `` e `-    assert 2 == 2`, e não tem `- nenhum arquivo de teste entre os alvos` (hoje o curinga é pulado e a seção diz isso). TF `test_tf_removidas_de_teste_diretorio_cobre_teste_tocado` — o mesmo, com alvo `tests/` (hoje o diretório não é arquivo de teste e é pulado). TF `test_tf_removidas_de_teste_linha_que_comeca_por_dois_hifens` — `tests/test_a.py` ganha a quarta linha `--sep--`, commitada no repositório de `tmp_path`; `ref` capturado; a linha `--sep--` sai; alvo `tests/test_a.py`; a seção tem `` ### `tests/test_a.py` — 1 linha(s) removida(s) `` e, entre as suas linhas, `---sep--` (hoje o filtro de `---` a apaga com o cabeçalho e a seção diz `nenhuma linha removida`). TR `test_tr_removidas_de_teste_alvo_e_curinga_uma_entrada` — alvos `tests/test_a.py` e `tests/test_*.py`, a linha `    assert 2 == 2` sai: a seção tem uma só ocorrência de `` ### `tests/test_a.py` `` (a regra concorrente que expandisse o curinga sem conferir as chaves já postas daria duas). Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_review_evidence.py -q -k "removidas_de_teste and (curinga or hifens or diretorio)"` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - dossiê de evidência.linhas removidas dos testes — o arquivo de teste coberto por alvo curinga ou diretório e a linha removida que começa por `--` aparecem na seção — Verificação 1
- **Fora do escopo desta tarefa:** a linha `- nenhum arquivo de teste entre os alvos`, que passa a ler os alvos expandidos (nenhum tocado de teste coberto, nenhuma remoção a mostrar); o critério da rubrica (`RAF-T12`).
- **Handover:** 2026-09-29 · para `RAF-T12`
  - **Entregue:** review_evidence.py: linhas_removidas_de_teste(…, tocados) expande alvo curinga ou diretório contra os tocados (uma chave por arquivo); _linhas_removidas_do_diff conta só linhas '-' depois do primeiro @@; 4 testes novos, suíte 566
  - **Contrato:** a seção '## Linhas removidas dos testes' cobre teste sob curinga ou diretório e não perde linha que começa por '--'
  - **Não refazer:** a expansão dos alvos e o parser do diff
  - **Pendente:** nenhum

### RAF-T12 — A rubrica reprova a asserção de teste removida sem ordem do card [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa acrescenta à rubrica de revisão o critério que reprova a asserção de teste removida sem que o card mande removê-la.
- **Fundamento:** `DRF-33`; `F-18` (a dimensão `testes` não cobre a asserção existente removida); relatório `R-12` (`AE-97` e `AE-98` do `P-0754`).
- **Depende de:** `RAF-T11a`, `RAF-T8a`
- **Operação do modelo:** `OP-12`
  - OP-12: Quem executa acrescenta à rubrica de revisão o critério que reprova a asserção de teste removida sem que o card mande removê-la.
  - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.
- **Camada e fronteira:** doutrina do kit — a régua do revisor, `docs/RUBRICA_DE_REVISAO.md`, dimensão `testes`; nenhum código muda. O critério se apoia na seção `## Linhas removidas dos testes` que o dossiê de evidência passou a trazer na `RAF-T11` (uma entrada por arquivo de teste — sob `tests/`, com nome `test_*.py` — entre os alvos, com alvo curinga ou diretório expandido contra os tocados pela `RAF-T11a`, com as linhas que a entrega removeu desde o recorte do despacho). A regra mora só na rubrica; nenhum agente nem skill a repete.
- **Arquivos-alvo:**
  - `docs/RUBRICA_DE_REVISAO.md`
- **Passos:**
  1. Na seção da dimensão `testes` (o cabeçalho de nível 3 que abre a dimensão), trocar as duas linhas do bullet `- **Fonte da evidência:**` pelas duas do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card).

     Texto antigo:

     ```text
     - **Fonte da evidência:** mecânica — presença dos arquivos de teste declarados e exit code da suíte
       da área tocada.
     ```

     Texto novo:

     ```text
     - **Fonte da evidência:** mecânica — presença dos arquivos de teste declarados, exit code da suíte
       da área tocada e a seção `## Linhas removidas dos testes` da evidência.
     ```
  2. Na mesma seção, trocar as duas linhas do bullet `` - **`não conforme`:** `` pelas quatro do texto novo (mesma regra de quebra e recuo).

     Texto antigo:

     ```text
     - **`não conforme`:** teste exigido ausente, suíte em exit não-zero, ou teste cujo significado mudou
       removido em vez de reescrito.
     ```

     Texto novo:

     ```text
     - **`não conforme`:** teste exigido ausente, suíte em exit não-zero, teste cujo significado mudou
       removido em vez de reescrito, ou asserção de teste existente removida sem que o card mande
       removê-la — a linha aparece na seção `## Linhas removidas dos testes` da evidência (`R-12`,
       `P-0755`).
     ```
  3. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar os bullets `conforme`, `parcial` e `não se aplica` da dimensão; não mudar a tabela de pesos; não editar `.claude/agents/pantonic-reviewer.md` (a régua mora na rubrica).
- **Contingências:**
  - se o texto antigo de um dos passos 1 e 2 não existir verbatim em `docs/RUBRICA_DE_REVISAO.md` → parar e sinalizar `blocked` razão `premissa`, nomeando o passo.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8');print('rubrica=%d-%d'%(t.count('removido em vez de reescrito.'),t.count('asserção de teste existente removida sem que o card mande')))"` → `rubrica=0-1` — antes `rubrica=1-0`, depois `rubrica=0-1`
- **Pronto quando:**
  - rubrica de revisão.critério da asserção removida — a régua reprova a asserção de teste removida sem que o card mande removê-la — Verificação 1
- **Fora do escopo desta tarefa:** a seção da evidência (`RAF-T11`); a linha de invariância do card de revisão (`RAF-T17`).
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** docs/RUBRICA_DE_REVISAO.md, dimensão testes: Fonte da evidência inclui a seção '## Linhas removidas dos testes' e 'não conforme' cobre asserção de teste existente removida sem ordem do card (R-12)
  - **Contrato:** o revisor reprova na dimensão testes a asserção removida sem ordem do card, lendo a seção do dossiê
  - **Não refazer:** os dois bullets da rubrica
  - **Pendente:** nenhum

### RAF-T12a — A dimensão testes declara a fonte mista e o instrumento cita a rubrica pela seção [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa faz a rubrica de revisão declarar a dimensão `testes` de fonte mista — presença dos testes e exit da suíte mecânicos e travados, juízo sobre as linhas removidas dos testes — e faz o instrumento do dossiê e o seu teste citarem a rubrica pela seção, sem número de linha.
- **Fundamento:** `DRF-54`; `AE-151` (laudo da `RAF-T12`, ressalva 88); `docs/RUBRICA_DE_REVISAO.md` §3 ("Dimensão de fonte mista tem a parte mecânica travada e a parte de juízo livre"); relatório `R-12`.
- **Depende de:** `RAF-T12`
- **Operação do modelo:** `OP-12`
  - OP-12: Quem executa acrescenta à rubrica de revisão o critério que reprova a asserção de teste removida sem que o card mande removê-la.
  - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.
- **Camada e fronteira:** doutrina do kit — a régua do revisor, `docs/RUBRICA_DE_REVISAO.md`, dimensão `testes` — e o texto que cita essa régua em `.claude/tools/review_evidence.py` (docstrings e uma linha de saída) e nos docstrings de `tests/test_review_evidence.py`; nenhum comportamento muda. A trava segue a de hoje: `veredito_testes` lê o exit do `pytest`, e o `rdo.py laudo` só recusa `conforme` contra vermelho mecânico (`DA-7`); o juízo sobre as linhas removidas fica livre, como a §3 da rubrica manda para a fonte mista. As citações da rubrica por número de linha nos dois arquivos de código apontam hoje para a dimensão errada (a rubrica cresceu desde a `EXA-T9b`) e passam a citar a seção, que não envelhece.
- **Arquivos-alvo:**
  - `docs/RUBRICA_DE_REVISAO.md`
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Passos:**
  1. Na seção da dimensão `testes` de `docs/RUBRICA_DE_REVISAO.md` (o cabeçalho de nível 3 que abre a dimensão), trocar as duas linhas do bullet `- **Fonte da evidência:**` pelas três do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card).

     Texto antigo:

     ```text
     - **Fonte da evidência:** mecânica — presença dos arquivos de teste declarados, exit code da suíte
       da área tocada e a seção `## Linhas removidas dos testes` da evidência.
     ```

     Texto novo:

     ```text
     - **Fonte da evidência:** mista — presença dos arquivos de teste declarados e exit code da suíte
       da área tocada, mecânicos e travados; juízo sobre cada linha da seção
       `## Linhas removidas dos testes` da evidência, confrontada com o que o card manda remover.
     ```
  2. Em `.claude/tools/review_evidence.py`, na primeira linha do docstring de `veredito_testes`, trocar `Veredito mecânico travado da dimensão` por `Veredito travado da parte mecânica da dimensão` (sem quebra nova e sem refluxo).
  3. Em `.claude/tools/review_evidence.py` (sete ocorrências: seis em docstring, uma na linha de saída do veredito aberto de `escopo`) e nos docstrings de `tests/test_review_evidence.py` (três ocorrências), toda citação de `RUBRICA_DE_REVISAO.md` com sufixo de linha (`:63-77`, `:79-92` ou `:94-106`) perde o sufixo e ganha ` §4` logo depois do caminho — depois da crase que fecha o caminho, quando ele está entre crases (sem quebra nova e sem refluxo).
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `566 passed`, 2026-09-29, revisão da `RAF-T12`).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Em `.claude/tools/review_evidence.py` e `tests/test_review_evidence.py` só mudam as linhas das citações e a primeira linha do docstring de `veredito_testes`: nenhum código, nome, asserção nem teste muda.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não tocar o dado de entrada de `test_tr_extrair_arquivos_alvo_ignora_texto_sem_barra_e_referencia_de_linha` (a citação com sufixo de linha ali é o que o teste prova que o extrator descarta; é a única que fica); não mudar `veredito_testes` além do docstring nem o `rdo.py`; não mudar os bullets de nível da dimensão `testes` nem a §3 da rubrica; não editar `.claude/agents/pantonic-reviewer.md` (a régua mora na rubrica).
- **Contingências:**
  - se o texto antigo do passo 1 ou o trecho do passo 2 não existir verbatim → parar e sinalizar `blocked` razão `premissa`, nomeando o passo.
  - se as citações com sufixo de linha não forem sete em `.claude/tools/review_evidence.py` e quatro em `tests/test_review_evidence.py` (as três dos docstrings e a do dado de entrada) → parar e sinalizar `blocked` razão `premissa`, com a contagem medida.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; `tests/test_review_evidence.py` e a suíte inteira.
- **Verificação:**
  1. `python -c "from pathlib import Path;r=Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8');e=Path('.claude/tools/review_evidence.py').read_text(encoding='utf-8');t=Path('tests/test_review_evidence.py').read_text(encoding='utf-8');a=lambda s:sum(s.count('.md:'+n) for n in ('63-77','79-92','94-106'));print('testes=%d-%d ancoras=%d-%d docstring=%d'%(r.count('da área tocada e a seção'),r.count('da área tocada, mecânicos e travados'),a(e),a(t),e.count('Veredito travado da parte mecânica')))"` → `testes=0-1 ancoras=0-1 docstring=1` — antes `testes=1-0 ancoras=7-4 docstring=0`, depois `testes=0-1 ancoras=0-1 docstring=1`
- **Pronto quando:**
  - rubrica de revisão.critério da asserção removida — a dimensão `testes` declara a fonte mista, com a parte mecânica travada e o juízo sobre as linhas removidas, e o instrumento cita a rubrica pela seção — Verificação 1
- **Fora do escopo desta tarefa:** a trava do laudo (`rdo.py`, `DA-7`), que já só recusa `conforme` contra vermelho; citações da rubrica por número de linha em registro histórico (diário).
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** rubrica: dimensão testes declara fonte mista (parte mecânica travada, juízo livre sobre as linhas removidas); review_evidence.py e test_review_evidence.py citam a rubrica por §4 no lugar do número de linha
  - **Contrato:** nenhuma citação da rubrica por número de linha no instrumento, exceto o dado de entrada do teste do extrator
  - **Não refazer:** o bullet de fonte mista e as dez citações
  - **Pendente:** nenhum

### RAF-T13 — A conferência do card compara o depois com o esperado e lê o literal com pontuação [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** Quem executa faz a conferência de verificação do card comparar com o resultado que o card escreve, também no bloco cercado medido depois da entrega e no literal com pontuação.
- **Fundamento:** `DRF-13` (i) e (ii); `F-14`, `F-16` (um único par real com pontuação no literal, `docs/plans/P-0753-auditoria-estagio-1/plano.md` linha 434); relatório `R-09`, `R-10`.
- **Depende de:** `RAF-T7`
- **Operação do modelo:** `OP-13`
  - OP-13: Quem executa faz a conferência de verificação do card comparar com o resultado que o card escreve, também no bloco cercado medido depois da entrega e no literal com pontuação.
  - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/card_check.py`, só biblioteca padrão; carrega `rdo.py` e `caminhos.py` por caminho; roda o comando publicado por `subprocess.run` sem `shell=True`, como hoje. O card cobre as duas recomendações da operação (`R-09` e `R-10`) no mesmo arquivo. A forma normativa do bloco `Verificação` (`docs/RUBRICA_DE_REVISAO.md` §8.1, Formas A e B) não muda de texto; o card antigo continua lido como antes. O contrato do objeto é: "Quem implementa amplia o que a conferência aceita sem deixar de ler os cards já escritos na forma antiga."
- **Arquivos-alvo:**
  - `.claude/tools/card_check.py`
  - `tests/test_card_check.py`
- **Contratos/classes:** `verificar_tarefa(plano: Path, tarefa_id: str, root: Path, mundo: str | None = None) -> tuple[bool, list[str], dict]` e `main` — assinaturas inalteradas. Três regras:
  1. Forma de bloco cercado (`forma="8.1"`), `R-09`: depois das checagens de presença de hoje (comando, `→`, `Medido antes`), com `mundo == "depois"` o valor comparado é o literal do esperado — função nova `_literal_do_esperado(esperado: str) -> str | None`: o primeiro negrito `**<valor>**` do esperado (regex nova `_NEGRITO_RE = re.compile(r"\*\*(?P<val>[^*]+?)\*\*")`, valor sem espaços nas pontas); sem negrito, o primeiro trecho entre crases (`_CRASE_RE`); sem nenhum, `None` → falha `item <n>: esperado sem literal` e o item não roda. A divergência no mundo `depois` sai `item <n>: divergencia - esperado (depois) declara '<valor>', execução mediu exit <x> saída '<saída>'`. Com `mundo == "antes"`, tudo como hoje: compara `Medido antes`, e a divergência segue `item <n>: divergencia - Medido antes declara '<valor>', ...`. A comparação segue `_bate_com_medido` (`exit N` compara o código; outro valor, substring de stdout mais stderr).
  2. Forma inline, `R-10`: o par `antes`/`depois` é procurado só no trecho que começa no primeiro `→` depois do comando (sem `→`, no resto do item, como hoje), primeiro pela regex nova `_ANTES_DEPOIS_CRASE_RE = re.compile(r"antes\s+`(?P<antes>[^`]*)`\s*[,;]?\s*depois\s+`(?P<depois>[^`]*)`")`, que aceita `,`, `;` e `.` dentro do literal; sem par com crase, pela `_ANTES_DEPOIS_RE` de hoje (legado), no mesmo trecho.
  3. O docstring de `verificar_tarefa` troca a frase que diz que o mundo só afeta a forma inline pela regra 1.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_card_check.py` os helpers `_plano_com_item(tmp_path: Path, item: str) -> Path` (plano sintético em `tmp_path/plano.md` com o card `RX-T1`, campos `Objetivo`, `Entregável`, `Verificação` com o item dado e `Pronto quando`), `_bloco(valor_impresso: str, esperado: str, medido_antes: str) -> str` (item de bloco cercado com `python -c "print('<valor_impresso>')"`, a linha `→ <esperado>. **Medido antes: <medido_antes>**`) e `_rodar(card_check, plano: Path, mundo: str) -> int` (`main` com `--tarefa RX-T1`, `--root` na raiz do repositório e `--mundo`), e os sete testes da seção `Testes`.
  2. Rodar `python -m pytest tests/test_card_check.py -q -k "bloco_cercado_mundo or par_com_crase"` e conferir que os cinco TF falham e os dois TR passam.
  3. Aplicar as três regras de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 7 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Nenhuma linha que já existia em `tests/test_card_check.py` sai ou muda: o card só acrescenta ao fim do arquivo; as fixtures de `tests/fixtures/card_check/` não mudam.
  - O `card_check` deste plano continua saindo 0 sobre os cards `RAF-T1`..`RAF-T18` com a regra nova: todos usam o par com crase depois do `→`.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `_ANTES_DEPOIS_RE` (legado), `_SETA_INLINE_RE`, `_SETA_RE` nem `_MEDIDO_ANTES_RE`; não mudar a lista de programas aceitos nem a troca de `<ref>` (é da `RAF-T14`); não mudar `--gravar` nem `caminhos.destino_medida` (é da `RAF-T15`); não editar `docs/RUBRICA_DE_REVISAO.md`.
- **Contingências:**
  - se um teste que já existia em `tests/test_card_check.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_bloco_cercado_mundo_depois_compara_com_o_esperado` — bloco que imprime `a`, esperado `imprime **b**`, `Medido antes: a`: `--mundo depois` sai 1 com `divergencia - esperado (depois) declara 'b'` no stderr (hoje sai 0, comparando `a`); o mesmo bloco imprimindo `b` sai 0 com `--mundo depois` (hoje sai 1). TR `test_tr_bloco_cercado_mundo_antes_segue_com_o_medido` — imprimindo `a`, `--mundo antes` sai 0; imprimindo `b`, sai 1 com `divergencia - Medido antes declara 'a'`. TF `test_tf_bloco_cercado_mundo_depois_sem_literal_falha` — esperado `imprime o valor`, sem negrito nem crase: `--mundo depois` sai 1 com `item 1: esperado sem literal`. TF `test_tf_par_com_crase_depois_aceita_ponto` — item inline `` `python -c "print('a.txt: 2')"` → `a.txt: 3` — antes `a.txt: 2`, depois `a.txt: 3` ``: `--mundo antes` sai 0; `--mundo depois` sai 1 com `declara 'a.txt: 3'` (hoje a regex corta o literal em `a` e sai 0). TF `test_tf_par_com_crase_antes_aceita_virgula` — antes `x, y` com o comando imprimindo `x; z`: `--mundo antes` sai 1 com `divergencia - valor do mundo (antes) declara 'x, y'` (hoje sai 1 com `sem valor antes`); imprimindo `x, y`, sai 0. TF `test_tf_par_com_crase_so_depois_da_seta` — item `` `python -c "print('a')"` (nota: antes `z`, depois `z`) → `a` — antes `a`, depois `a` ``: `--mundo antes` sai 0 (hoje lê o par da nota e sai 1). TR `test_tr_par_com_crase_legado_sem_crase_segue_lido` — item `` `python -c "print(2)"` → 3 — antes 2, depois 3 ``, sem crase no par: `--mundo antes` sai 0 e `--mundo depois` sai 1. Suíte `tests/test_card_check.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_card_check.py -q -k bloco_cercado_mundo` → `exit 0` — antes `exit 5`, depois `exit 0`
  2. `python -m pytest tests/test_card_check.py -q -k par_com_crase` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - conferência de verificação do card.resultado esperado no bloco cercado — é comparada com o resultado que o card escreve para depois da entrega — Verificação 1
  - conferência de verificação do card.literal com pontuação — o valor entre crases é lido inteiro, só depois do comando; o card antigo continua lido como antes — Verificação 2
- **Fora do escopo desta tarefa:** o `git` de leitura, o `<ref>` no comando e a linha de invariância (`RAF-T14`); a pasta e o nome da medida gravada (`RAF-T15`); reescrever o par da linha 434 do plano `P-0753` (fora do alcance de todo card, §4 invariante 7).
- **Handover:** 2026-09-29 · para `RAF-T14`
  - **Entregue:** card_check.py: no mundo depois, bloco cercado compara com o literal do esperado (negrito ou crase; sem literal falha 'esperado sem literal'); par antes/depois com crase lido só depois da primeira →, aceita pontuação; 7 testes novos, suíte 573
  - **Contrato:** RAF-T1..RAF-T18 seguem saindo 0 no card_check; mundo antes segue com o Medido antes
  - **Não refazer:** _literal_do_esperado, _NEGRITO_RE, _ANTES_DEPOIS_CRASE_RE e os testes
  - **Pendente:** nenhum

### RAF-T13a — O docstring do módulo e a ajuda de --mundo da conferência do card dizem o mundo depois da forma 8.1 [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa faz o docstring do módulo e a ajuda da opção `--mundo` da conferência de verificação do card dizerem o que a regra 1 da `RAF-T13` entregou: no mundo `depois` a forma 8.1 compara com o literal do esperado, e o mundo vale nas duas formas.
- **Fundamento:** `DRF-55`; `AE-155` (laudo da `RAF-T13`, ressalva 91); relatório `R-09`.
- **Depende de:** `RAF-T13`
- **Operação do modelo:** `OP-13`
  - OP-13: Quem executa faz a conferência de verificação do card comparar com o resultado que o card escreve, também no bloco cercado medido depois da entrega e no literal com pontuação.
  - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** texto do instrumento `.claude/tools/card_check.py` — o docstring do módulo (linhas 5-7) e o `help` da opção `--mundo` em `main`; nenhum comportamento muda. A `RAF-T13` trocou só o docstring de `verificar_tarefa` (a regra 3 do card nomeou só ele); os outros dois textos seguiram dizendo que a conferência compara com o `Medido antes` e que o mundo só vale na forma inline.
- **Arquivos-alvo:**
  - `.claude/tools/card_check.py`
- **Passos:**
  1. No docstring do módulo de `.claude/tools/card_check.py`, trocar as três linhas do texto antigo pelas quatro do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card).

     Texto antigo:

     ```text
     item e **roda** cada comando publicado, comparando a saída medida agora com o `Medido antes`
     declarado — divergência é falha nomeada, porque significa que o card descreve um mundo que não é
     o que está na árvore.
     ```

     Texto novo:

     ```text
     item e **roda** cada comando publicado, comparando a saída medida agora com o valor declarado
     para o mundo comparado (`--mundo`, RAF-T13: `antes` lê o `Medido antes`, `depois` o literal do
     esperado) — divergência é falha nomeada, porque significa que o card descreve um mundo que não
     é o que está na árvore.
     ```
  2. No `help` da opção `--mundo`, em `main`, trocar as duas linhas do texto antigo pelas duas do texto novo (o recuo de 12 espaços fica; cada linha perde o recuo deste card).

     Texto antigo:

     ```text
     "Mundo do card a comparar na forma inline (DFP-14); ausente deriva do bullet "
     "- **Status:** (done -> depois; demais -> antes)."
     ```

     Texto novo:

     ```text
     "Mundo do card a comparar nas duas formas, 8.1 e inline (DFP-14, RAF-T13); "
     "ausente deriva do bullet - **Status:** (done -> depois; demais -> antes)."
     ```
  3. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `573 passed`, 2026-09-29, revisão da `RAF-T13`).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Em `.claude/tools/card_check.py` só mudam as cinco linhas dos dois textos antigos: nenhum código, nome, regex nem outro comentário muda; o arquivo segue em LF.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar o docstring de `verificar_tarefa` (a `RAF-T13` já o acertou) nem os comentários das regex; não mudar `choices`, `default` nem a derivação do mundo pelo `Status`; não tocar o que é da `RAF-T14` (`git` de leitura, `<ref>`, invariância).
- **Contingências:**
  - se o texto antigo do passo 1 ou do passo 2 não existir verbatim → parar e sinalizar `blocked` razão `premissa`, nomeando o passo.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo (nenhum teste lê o docstring do módulo nem a ajuda de `--mundo`); `tests/test_card_check.py` e a suíte inteira.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/tools/card_check.py').read_text(encoding='utf-8');print('docstring=%d-%d help=%d-%d'%(t.count('declarado — divergência'),t.count('para o mundo comparado ('),t.count('comparar na forma inline'),t.count('comparar nas duas formas')))"` → `docstring=0-1 help=0-1` — antes `docstring=1-0 help=1-0`, depois `docstring=0-1 help=0-1`
- **Pronto quando:**
  - conferência de verificação do card.resultado esperado no bloco cercado — o docstring do módulo e a ajuda de `--mundo` dizem que o mundo `depois` da forma 8.1 compara com o literal do esperado e que o mundo vale nas duas formas — Verificação 1
- **Fora do escopo desta tarefa:** o texto da `RAF-T13` (`done`), que fica como executado; a restrição de `card_check` sobre o próprio card (`AE-157`), que não se repete em card aberto.
- **Handover:** 2026-09-29 · para `RAF-T14`
  - **Entregue:** card_check.py: docstring do módulo e help de --mundo descrevem o mundo depois da forma 8.1 (compara com o literal do esperado)
  - **Contrato:** nenhum texto do card_check contradiz a regra do mundo depois
  - **Não refazer:** as duas trocas de texto
  - **Pendente:** nenhum

### RAF-T14 — A conferência do card roda o git de leitura contra o recorte do despacho [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** Quem executa faz a conferência de verificação do card rodar a leitura do versionador contra o recorte do despacho, inclusive a linha que prova que o alvo ficou igual.
- **Fundamento:** `DRF-13` (iii) e (iv), `DRF-36`; `F-14` (só `python` e `pwsh` rodam; sem `shell=True`); relatório `R-11` (e o suporte que a `R-27` pede, `DRF-28`).
- **Depende de:** `RAF-T3`, `RAF-T13`, `RAF-T13a`
- **Operação do modelo:** `OP-14`
  - OP-14: Quem executa faz a conferência de verificação do card rodar a leitura do versionador contra o recorte do despacho, inclusive a linha que prova que o alvo ficou igual.
  - precisa de: conferência de verificação do card — Quem implementa amplia o que a conferência aceita sem deixar de ler os cards já escritos na forma antiga.; despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/card_check.py`, só biblioteca padrão; o comando segue rodando por `subprocess.run` sem `shell=True`, decidido por token depois de `shlex.split`. O `git` entra só para ler: nenhum subcomando que escreve no índice, na árvore ou nas referências roda. O recorte vem de `.claude/estado/tarefa-corrente.json` sob o `--root`, que o `despachar` grava com `tarefa` e `ref` desde antes deste plano (e continua gravando depois da `RAF-T3`); como o despacho roda o `card_check` antes de gravar o recorte da tarefa nova, a linha com `<ref>` serve ao mundo `depois` (revisão e redespacho) e à linha de invariância.
- **Arquivos-alvo:**
  - `.claude/tools/card_check.py`
  - `tests/test_card_check.py`
- **Contratos/classes:** assinaturas públicas inalteradas. Quatro regras:
  1. `_COMANDOS_PERMITIDOS` ganha `git`; tupla nova `_GIT_LEITURA = ("status", "diff", "show", "ls-files", "check-ignore")`; `_validar_comando`, depois da checagem do primeiro token, recusa `git` sem segundo token ou com segundo token fora de `_GIT_LEITURA`, com a razão `subcomando git '<segundo token>' fora da lista de leitura <_GIT_LEITURA>` (o segundo token vazio quando falta), que o item reporta como hoje: `item <n>: comando recusado - <razão>`.
  2. Função nova `_ref_do_despacho(root: Path, tarefa_id: str) -> str | None`: lê `<root>/.claude/estado/tarefa-corrente.json`; devolve o `ref` só quando o JSON é objeto, o `tarefa` dele é `tarefa_id` e o `ref` não é vazio; arquivo ausente, ilegível ou de outra tarefa → `None`.
  3. `ItemVerificacao` ganha o parâmetro `invariancia: bool = False`; `_parsear_itens` o liga, nas duas formas, quando o resto do item depois do comando contém o literal `(invariância)` (regex `_INVARIANCIA_RE`, `r"\(invariância\)"`).
  4. Em `verificar_tarefa`, para cada item, logo depois de o registro entrar em `registros` e antes das regras de forma: item de invariância com `mundo == "antes"` → `registro["saida"] = "não medida (invariância)"`, sem falha, e o item não roda; comando com o literal `<ref>` → troca cada `<ref>` pelo valor de `_ref_do_despacho(root, dossie.tarefa_id)` (e o `registro["comando"]` passa a ser o comando trocado); com `None`, falha `item <n>: <ref> sem recorte do despacho para '<ID>' em .claude/estado/tarefa-corrente.json` e o item não roda. Na forma de bloco cercado, o item de invariância dispensa o `Medido antes` (a checagem de presença só o cobra de item sem invariância); no mundo `depois`, o item de invariância segue a comparação de hoje (inline: `depois` do par ou, sem par, a primeira crase do esperado; bloco: o esperado da `RAF-T13`).
  A forma da linha de invariância que os cards passam a publicar (`DRF-36`) é `` `git diff --exit-code <ref> --numstat -- <alvo>` → `exit 0` (invariância) ``: `--exit-code` faz o `git diff` sair 1 quando o alvo mudou desde o recorte, e 0 quando a saída é vazia.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_card_check.py` o helper `_raiz_com_despacho(tmp_path: Path, tarefa: str, ref: str) -> Path` (raiz temporária com cópias de `rdo.py` e `caminhos.py` em `.claude/tools/` e `.claude/estado/tarefa-corrente.json` com `tarefa` e `ref`) e os cinco testes da seção `Testes`, usando os helpers `_plano_com_item` e `_rodar` da `RAF-T13`.
  2. Rodar `python -m pytest tests/test_card_check.py -q -k "git_leitura or ref_do_despacho or invariancia"` e conferir que os quatro TF falham e o TR passa.
  3. Aplicar as quatro regras de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 5 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Nenhuma linha que já existia em `tests/test_card_check.py` sai ou muda: o card só acrescenta ao fim do arquivo.
  - Nenhum teste roda subcomando `git` que escreve: o teste da recusa só confere a razão, e o comando recusado nunca roda.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não passar `shell=True`; não aceitar `git` com opção global antes do subcomando (`git -C`, `git -c`); não gravar nem capturar `ref` no `card_check` (o recorte é do `despachar`); não mudar `--gravar` nem o nome da medida (é da `RAF-T15`); não editar a doutrina do planejador (é da `RAF-T17`).
- **Contingências:**
  - se um teste que já existia em `tests/test_card_check.py` ou um teste de `despachar` em `tests/test_backlog.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_git_leitura_roda_ls_files` — item `` `git ls-files tests/test_card_check.py` `` com `antes` e `depois` iguais a `tests/test_card_check.py`, `--root` na raiz do repositório: `--mundo antes` sai 0 (hoje sai 1, `primeiro token fora da lista fechada`). TF `test_tf_git_leitura_recusa_subcomando_de_escrita` — item `` `git commit -m x` ``: sai 1 com `subcomando git 'commit' fora da lista de leitura` no stderr (hoje a razão é a do primeiro token). TF `test_tf_ref_do_despacho_entra_no_comando` — raiz com `tarefa-corrente.json` de `RX-T1` e `ref` `abc123`, item que imprime o primeiro argumento com `<ref>` como argumento, `depois` `abc123`: `--mundo depois` sai 0 (hoje imprime `<ref>` e sai 1). TR `test_tr_ref_do_despacho_de_outra_tarefa_falha` — o JSON é de `OUTRA-T1`: sai 1 com `item 1: <ref> sem recorte do despacho para 'RX-T1'`. TF `test_tf_invariancia_nao_medida_antes_e_medida_depois` — item `` `python -c "import sys;sys.exit(1)"` → `exit 0` (invariância) ``, sem par: `--mundo antes` com `--gravar` sai 0 e o JSON gravado tem `não medida (invariância)` na `saida` do item 1 (hoje sai 1, `sem valor antes`); `--mundo depois` sai 1 (o item roda e o exit 1 não é o `exit 0` esperado). Suíte `tests/test_card_check.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_card_check.py -q -k git_leitura` → `exit 0` — antes `exit 5`, depois `exit 0`
  2. `python -m pytest tests/test_card_check.py -q -k ref_do_despacho` → `exit 0` — antes `exit 5`, depois `exit 0`
  3. `python -m pytest tests/test_card_check.py -q -k invariancia` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - conferência de verificação do card.comandos de leitura do versionador — o versionador roda nos subcomandos de leitura, e outro subcomando é recusado com mensagem que o nomeia — Verificação 1
  - conferência de verificação do card.recorte do despacho no comando — a marca do recorte no comando é trocada pelo recorte que o despacho gravou para a tarefa — Verificação 2
  - conferência de verificação do card.linha de invariância — a linha declarada de invariância não é medida antes da entrega e é medida depois dela — Verificação 3
- **Fora do escopo desta tarefa:** a pasta e o nome da medida gravada (`RAF-T15`); a regra do planejador para o card que deixa o alvo igual (`RAF-T17`).
- **Handover:** 2026-09-29 · para `RAF-T15`
  - **Entregue:** card_check.py: roda git de leitura (_GIT_LEITURA status/diff/show/ls-files/check-ignore; outro subcomando recusado); <ref> do comando vem de .claude/estado/tarefa-corrente.json (_ref_do_despacho); item marcado (invariância) não se mede no mundo antes; 5 testes novos, suíte 578
  - **Contrato:** Verificação de card pode usar git de leitura contra o <ref> do despacho; subcomando de escrita é recusado
  - **Não refazer:** _GIT_LEITURA, _ref_do_despacho, invariancia e os testes
  - **Pendente:** nenhum

### RAF-T15 — A medida gravada fica na pasta do plano da árvore medida, com o momento no nome [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** Quem executa faz a medida gravada do card ficar na pasta do plano da árvore medida, com o momento da medida no nome, onde o dossiê de evidência a encontra.
- **Fundamento:** `DRF-30`; `F-15` (hoje a pasta vem do `--plano`; 20 medidas versionadas com o nome sem mundo em `docs/plans/P-0753-auditoria-estagio-1/evidencia/`); relatório `R-05` (auditoria reg. 35).
- **Depende de:** `RAF-T11a`, `RAF-T14`, `RAF-T12a`
- **Operação do modelo:** `OP-15`
  - OP-15: Quem executa faz a medida gravada do card ficar na pasta do plano da árvore medida, com o momento da medida no nome, onde o dossiê de evidência a encontra.
  - precisa de: conferência de verificação do card — Quem implementa amplia o que a conferência aceita sem deixar de ler os cards já escritos na forma antiga.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumentos do kit — a residência dos caminhos `.claude/tools/caminhos.py` (a regra mora só em `destino_medida`), o escritor `.claude/tools/card_check.py` (`--gravar` sem caminho) e o leitor `.claude/tools/review_evidence.py` (`montar_documento`); só biblioteca padrão; os dois instrumentos carregam `caminhos.py` por caminho. As 20 medidas antigas do `P-0753` ficam como estão e seguem legíveis pelo nome sem mundo. O contrato do objeto é: "Quem implementa muda onde e com que nome a medida se grava, e faz o revisor achar tanto a nova quanto as vinte já gravadas com o nome antigo."
- **Arquivos-alvo:**
  - `.claude/tools/caminhos.py`
  - `.claude/tools/card_check.py`
  - `.claude/tools/review_evidence.py`
  - `tests/test_caminhos.py`
  - `tests/test_card_check.py`
  - `tests/test_review_evidence.py`
- **Contratos/classes:** três regras:
  1. `caminhos.destino_medida(raiz: Path, plano_path: Path, tarefa: str, mundo: str | None = None) -> Path` — plano em pasta (`pasta_do_plano(plano_path)` não `None`): `planos_dir(raiz) / <nome da pasta do plano> / "evidencia" / "<P-id>-<tarefa>-medida<sufixo>.json"`; plano legado ou tíquete: `<raiz>/docs/RDO/evidencia/<id ou stem>-<tarefa>-medida<sufixo>.json` (a regra de `<id ou stem>` de hoje); `<sufixo>` é `-<mundo>` quando `mundo` é dado e vazio quando é `None`. O comentário acima da função passa a descrever a regra nova.
  2. `card_check.py`, `main`: `--gravar` sem caminho grava em `_caminhos.destino_medida(args.root, args.plano, args.tarefa, medida["mundo"])` — o mundo efetivo da medida (o de `--mundo` ou o derivado do status); o texto de ajuda do `--gravar` cita `<mundo>`. Com caminho dado, nada muda.
  3. `review_evidence.py`, `montar_documento`: a medida lida é a primeira que existe desta lista, nesta ordem — com `dir_evidencia` dado: `<dir>/<plano_id>-<ID>-medida-depois.json`, `-medida-antes.json`, `-medida.json`; e, sempre depois: `destino_medida(root, plano_path, <ID>, "depois")`, `(…, "antes")`, `(…, None)`; sem nenhuma, o primeiro da lista vai para `secao_medida_do_executor`, que já imprime `ausente`. O bloco da `RAF-T7` (medida ao lado do `--out`, e na falta dela `destino_medida`) é substituído por esta lista, que o mantém: a do lado do `--out` vence.
- **Passos:**
  1. Em `tests/test_caminhos.py`, no teste `test_tf_destino_medida_tres_residencias`, trocar o valor esperado da terceira asserção, `Path("docs/plans/P-0002-y") / "evidencia" / "P-0002-T2-medida.json"`, por `raiz / "docs" / "plans" / "P-0002-y" / "evidencia" / "P-0002-T2-medida.json"`, e o docstring do teste pelas três linhas do bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os quatro espaços do corpo da função) — o significado mudou pela `R-05`, e a asserção se reescreve, não se remove.

     ```text
         """`TK-92a` — `destino_medida` cobre as três residências pela mesma função: tíquete do
         diário e plano legado caem em `<raiz>/docs/RDO/evidencia`, plano em pasta grava na pasta do
         plano sob a raiz, em `<raiz>/docs/plans/<pasta>/evidencia` (`R-05`, RAF-T15)."""
     ```
  2. Em `tests/test_card_check.py`, no teste `test_tf_gravar_sem_caminho_grava_no_destino_derivado`, trocar o nome `DIARIO_DE_OBRAS-CX-T1-medida.json` por `DIARIO_DE_OBRAS-CX-T1-medida-antes.json` na linha `destino = ...` e no docstring, acrescentando ao docstring que o nome leva o mundo desde a RAF-T15 (`R-05`) — o card `CX-T1` da fixture compara o mundo `antes`.
  3. Acrescentar ao fim de `tests/test_caminhos.py`, `tests/test_card_check.py` e `tests/test_review_evidence.py` os testes da seção `Testes` (em `tests/test_review_evidence.py`, com o helper `_gravar_medida(caminho: Path, exit_medido: int) -> None`, reusando `_plano_em_pasta_com_medida` da `RAF-T7`).
  4. Rodar `python -m pytest tests/test_caminhos.py tests/test_card_check.py tests/test_review_evidence.py -q -k "destino_medida or medida_gravada_com_o_mundo or medida_com_mundo or gravar_sem_caminho"` e conferir que os três TF e os dois testes reescritos falham e o TR passa.
  5. Aplicar as três regras de `Contratos/classes`.
  6. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 4 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Nos três arquivos de teste, as únicas linhas que já existiam e mudam são as dos passos 1 e 2; o resto só se acrescenta ao fim.
  - Os testes gravam só em `tmp_path`; nenhum grava em `docs/`.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/` (inclusive as 20 medidas com o nome antigo, que não se renomeiam), `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não renomear nem mover medida já gravada; não mudar `destino_evidencia`, `destino_rdo` nem `destino_laudo`; não mudar a forma da seção `## Medida do executor`; não editar a doutrina do planejador (a gravação dos dois mundos na rodada é da `RAF-T18`).
- **Contingências:**
  - se um teste que já existia na suíte, fora os reescritos nos passos 1 e 2, cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_destino_medida_na_raiz_com_o_mundo` (em `tests/test_caminhos.py`) — raiz `/copia`, plano `/real/docs/plans/P-0002-y/plano.md`, tarefa `T2`, mundo `depois`: `/copia/docs/plans/P-0002-y/evidencia/P-0002-T2-medida-depois.json`; plano legado `/real/docs/plans/P-0001-x.md`, `T1`, `antes`: `/copia/docs/RDO/evidencia/P-0001-T1-medida-antes.json` (hoje a função não aceita o mundo e a pasta vem de `/real`). TF `test_tf_medida_gravada_com_o_mundo_na_pasta_da_raiz` (em `tests/test_card_check.py`) — plano em pasta `P-0007-z` numa árvore `real`, `--root` numa árvore `copia` com `rdo.py` e `caminhos.py`, `--gravar` sem caminho rodado com `--mundo antes` e com `--mundo depois`: a pasta `copia/docs/plans/P-0007-z/evidencia/` tem exatamente `P-0007-RX-T1-medida-antes.json` e `P-0007-RX-T1-medida-depois.json`, e `real/docs/plans/P-0007-z/evidencia` não existe (hoje grava um arquivo só, sem mundo, na árvore `real`). TF `test_tf_medida_com_mundo_lida_na_ordem` (em `tests/test_review_evidence.py`) — plano `P-0999-teste` com a medida sem mundo de `exit` 7; com `-medida-antes.json` de `exit` 5, o documento traz a linha com `5`; com `-medida-depois.json` de `exit` 6 também, traz a linha com `6` (hoje traz `7` nos dois). TR `test_tr_medida_com_mundo_sem_mundo_ainda_lida` — só a medida sem mundo: o documento traz a linha com `7`. Suítes `tests/test_caminhos.py`, `tests/test_card_check.py`, `tests/test_review_evidence.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_caminhos.py -q -k destino_medida_na_raiz` → `exit 0` — antes `exit 5`, depois `exit 0`
  2. `python -m pytest tests/test_card_check.py -q -k medida_gravada_com_o_mundo` → `exit 0` — antes `exit 5`, depois `exit 0`
  3. `python -m pytest tests/test_review_evidence.py -q -k medida_com_mundo` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - medida gravada do card.pasta em que é gravada — a medida fica na pasta do plano dentro da árvore que foi medida — Verificação 1
  - medida gravada do card.momento no nome — o nome diz o momento, e as duas convivem — Verificação 2
  - medida gravada do card.leitura pelo revisor — o revisor lê a de depois, na falta dela a de antes, e por último as vinte já gravadas com o nome antigo — Verificação 3
- **Fora do escopo desta tarefa:** a regra do planejador de gravar os dois mundos na rodada de replanejamento (`RAF-T18`); a árvore em que o card dependente mede o `antes` (`RAF-T16`).
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** card_check/caminhos/review_evidence: a medida gravada fica na pasta do plano da árvore medida, com o momento no nome (P-<n>-<ID>-medida-<antes|depois>.json), e o leitor do review_evidence a encontra ali (ver RDO RAF-T15)
  - **Contrato:** medida de antes e de depois coexistem sem se sobrescrever, no plano da árvore medida
  - **Não refazer:** o destino da medida e o leitor
  - **Pendente:** nenhum

### RAF-T16 — O planejador mede o antes do card dependente na cópia com os anteriores aplicados [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa ensina o planejador a medir o antes do card que depende de outro na cópia de ensaio com os anteriores aplicados, declarando em que árvore mediu.
- **Fundamento:** `DRF-27`; relatório `R-26` (auditoria reg. 13).
- **Depende de:** `RAF-T15`
- **Operação do modelo:** `OP-16`
  - OP-16: Quem executa ensina o planejador a medir o antes do card que depende de outro na cópia de ensaio com os anteriores aplicados, declarando em que árvore mediu.
  - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; conferência de verificação do card — Quem implementa amplia o que a conferência aceita sem deixar de ler os cards já escritos na forma antiga.; medida gravada do card — Quem implementa muda onde e com que nome a medida se grava, e faz o revisor achar tanto a nova quanto as vinte já gravadas com o nome antigo.
- **Camada e fronteira:** doutrina do kit — a definição do agente planejador, `.claude/agents/pantonic-planner.md`, Fase 5; nenhum código muda. O comportamento que a regra usa já existe: `card_check --root <árvore>` roda os comandos do card na árvore dada, e `--gravar` grava a medida na pasta do plano dessa árvore, com o mundo no nome (`RAF-T15`). A regra mora só na Fase 5 do planejador; nenhum outro arquivo a repete.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md`
- **Passos:**
  1. Em `.claude/agents/pantonic-planner.md`, na `### Fase 5 — Registro e parada`, logo depois da linha `instrução explícita do dono.` (a última do parágrafo da Fase 5) e da linha vazia que a segue, e antes da linha que começa por `## Anatomia do card`, inserir o bloco abaixo seguido de uma linha vazia (as quebras são as do bloco; cada linha perde o recuo deste card e começa na coluna 0).

     ```text
     **Árvore do `antes`** (`R-26` da auditoria final, `P-0755`): o `card_check --mundo antes` que
     condiciona o registro roda, para o card cujo `antes` depende de um antecessor, na cópia do ensaio
     com os antecessores aplicados (`card_check --root <cópia>`); só o primeiro card de cada cadeia
     mede o `antes` contra a árvore real. O valor publicado nomeia a árvore em que foi medido: `real`
     ou `cópia com <IDs> aplicados`.
     ```
  2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_doutrina_unidade.py` lê este arquivo.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer no parágrafo existente da Fase 5 (a checagem de versão é da `RAF-T38`); não mexer no item 14 da Fase 4 (é da `RAF-T17` e da `RAF-T18`); não mexer na tabela de profundidade da Fase 4 (é da `RAF-T36`).
- **Contingências:**
  - se a linha `instrução explícita do dono.` seguida de linha vazia e da linha que começa por `## Anatomia do card` não existir em `.claude/agents/pantonic-planner.md` → parar e sinalizar `blocked` razão `premissa`, colando as dez linhas que antecedem `## Anatomia do card`.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê o arquivo.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('arvore=%d'%t.count('só o primeiro card de cada cadeia'))"` → `arvore=1` — antes `arvore=0`, depois `arvore=1`
- **Pronto quando:**
  - planejador.árvore em que se mede o antes — ele mede na cópia de ensaio com os anteriores aplicados, só o primeiro de cada cadeia mede na árvore real, e o valor publicado diz em que árvore foi medido — Verificação 1
- **Fora do escopo desta tarefa:** a linha de invariância do card que deixa o alvo igual (`RAF-T17`); a medida gravada na rodada de replanejamento (`RAF-T18`).
- **Handover:** 2026-09-29 · para `RAF-T17`
  - **Entregue:** .claude/agents/pantonic-planner.md Fase 5: o antes do card dependente se mede na cópia com os cards anteriores aplicados (R-26)
  - **Contrato:** o planejador não mede o antes de card dependente na árvore crua
  - **Não refazer:** o trecho da Fase 5
  - **Pendente:** nenhum

### RAF-T17 — O planejador discrimina o card que deixa o alvo igual pela invariância [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa ensina o planejador a discriminar o card cujo alvo deve ficar igual pela prova de que nada nele mudou desde o recorte do despacho.
- **Fundamento:** `DRF-28`, `DRF-36`; relatório `R-27` (auditoria reg. 14 e 35).
- **Depende de:** `RAF-T14`, `RAF-T16`
- **Operação do modelo:** `OP-17`
  - OP-17: Quem executa ensina o planejador a discriminar o card cujo alvo deve ficar igual pela prova de que nada nele mudou desde o recorte do despacho.
  - precisa de: planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão.; conferência de verificação do card — Quem implementa amplia o que a conferência aceita sem deixar de ler os cards já escritos na forma antiga.
- **Camada e fronteira:** doutrina do kit — a definição do agente planejador, `.claude/agents/pantonic-planner.md`, Fase 4, item 14; nenhum código muda. O mecanismo que a regra usa já existe desde a `RAF-T14`: o `card_check` roda `git diff` (subcomando de leitura), troca o literal `<ref>` do comando pelo recorte que o despacho gravou para a tarefa, e a linha marcada `(invariância)` não se mede no mundo `antes` e se mede no `depois`; a forma da linha é a da `DRF-36`. A regra mora só no item 14; nenhum outro arquivo a repete.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md`
- **Passos:**
  1. Em `.claude/agents/pantonic-planner.md`, na Fase 4, item 14 (o que começa por `14. **Ensaio dos cards em árvore temporária**`), logo depois da linha `   volta à autoria.` e antes da linha que começa por `   **A contingência se ensaia:**`, inserir o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card, e os três espaços que sobram no começo de cada linha entram no arquivo).

     ```text
        **Operação de estado final igual** (`R-27` da auditoria final, `P-0755`): o card cujo alvo
        deve ficar igual — revisão sem texto novo — não tem linha que dê valores diferentes antes e
        depois; a linha que o discrimina é a prova de que o alvo não mudou desde o recorte do
        despacho, `git diff --exit-code <ref> --numstat -- <alvo>` → `exit 0`, marcada
        `(invariância)`: o `card_check` não a mede no mundo `antes`, mede no `depois`, e ela falha
        quando o alvo muda.
     ```
  2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_doutrina_unidade.py` lê este arquivo.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não reescrever outra frase do item 14; não mexer no bloco `**Árvore do` da Fase 5 (`RAF-T16`); não acrescentar a regra da rodada de replanejamento (é da `RAF-T18`); não editar `docs/RUBRICA_DE_REVISAO.md`.
- **Contingências:**
  - se a linha `   volta à autoria.` seguida da linha que começa por `   **A contingência se ensaia:**` não existir em `.claude/agents/pantonic-planner.md` → parar e sinalizar `blocked` razão `premissa`, colando o item 14 inteiro.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê o arquivo.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('igual=%d'%t.count('**Operação de estado final igual**'))"` → `igual=1` — antes `igual=0`, depois `igual=1`
- **Pronto quando:**
  - planejador.card que deixa o alvo igual — a linha que o discrimina é a prova de que o alvo não mudou desde o recorte, declarada como invariância e medida depois da entrega — Verificação 1
- **Fora do escopo desta tarefa:** a mecânica da invariância no `card_check` (`RAF-T14`); a medida gravada na rodada (`RAF-T18`).
- **Handover:** 2026-09-29 · para `RAF-T18`
  - **Entregue:** .claude/agents/pantonic-planner.md item 14: card que deixa o alvo igual se discrimina pela Verificação de invariância (R-27)
  - **Contrato:** o item 14 do planejador trata o card que não muda o alvo pela invariância
  - **Não refazer:** o trecho do item 14
  - **Pendente:** nenhum

### RAF-T18 — A rodada de replanejamento grava a medida dos dois mundos [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa ensina o planejador a gravar, na rodada de replanejamento, a medida de antes e a de depois de cada card que ela reescreve.
- **Fundamento:** `DRF-28` (a mesma seção manda a rodada gravar os dois mundos), `DRF-30`; `F-21` (nenhum texto manda a rodada gravar medida); relatório `R-05` (auditoria reg. 35, `H-16`).
- **Depende de:** `RAF-T15`, `RAF-T17`
- **Operação do modelo:** `OP-18`
  - OP-18: Quem executa ensina o planejador a gravar, na rodada de replanejamento, a medida de antes e a de depois de cada card que ela reescreve.
  - precisa de: planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão.; medida gravada do card — Quem implementa muda onde e com que nome a medida se grava, e faz o revisor achar tanto a nova quanto as vinte já gravadas com o nome antigo.
- **Camada e fronteira:** doutrina do kit — a definição do agente planejador, `.claude/agents/pantonic-planner.md`, Fase 4, item 14, no mesmo trecho da `RAF-T17`, logo depois dele; nenhum código muda. O mecanismo que a regra usa já existe desde a `RAF-T15`: `card_check --gravar` sem caminho grava em `<raiz>/docs/plans/<pasta do plano>/evidencia/<P-id>-<ID>-medida-<mundo>.json`, a pasta vem do `--root` e o mundo vai no nome. A regra mora só no item 14; nenhum outro arquivo a repete.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md`
- **Passos:**
  1. Em `.claude/agents/pantonic-planner.md`, na Fase 4, item 14, logo depois da linha `   quando o alvo muda.` (a última do bloco `**Operação de estado final igual**` da `RAF-T17`) e antes da linha que começa por `   **A contingência se ensaia:**`, inserir o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card, e os três espaços que sobram no começo de cada linha entram no arquivo).

     ```text
        **A rodada grava a medida** (`R-05` da auditoria final, `P-0755`): a rodada de
        replanejamento grava, para cada card que reescreve, a medida de antes na árvore real
        (`card_check --mundo antes --gravar`) e a de depois na cópia do ensaio (`card_check --root
        <cópia> --mundo depois --gravar`), e copia o arquivo da cópia para a `evidencia/` do plano
        na árvore real: `-medida-antes.json` e `-medida-depois.json` convivem.
     ```
  2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_doutrina_unidade.py` lê este arquivo.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não reescrever o bloco `**Operação de estado final igual**` (`RAF-T17`) nem outra frase do item 14; não mexer na seção `## Rodada de replanejamento` do arquivo (a regra mora no item 14, `DRF-28`); não editar `.claude/agents/pantonic-consultant.md`.
- **Contingências:**
  - se a linha `   quando o alvo muda.` seguida da linha que começa por `   **A contingência se ensaia:**` não existir em `.claude/agents/pantonic-planner.md` → parar e sinalizar `blocked` razão `dependencia`, nomeando a `RAF-T17`.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê o arquivo.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('rodada=%d'%t.count('**A rodada grava a medida**'))"` → `rodada=1` — antes `rodada=0`, depois `rodada=1`
- **Pronto quando:**
  - planejador.medida gravada na rodada — a rodada grava a medida de antes na árvore real e a de depois na cópia de ensaio, para cada card que reescreve — Verificação 1
- **Fora do escopo desta tarefa:** o nome e a pasta da medida (`RAF-T15`); a rodada que escreve o card da operação nova (`RAF-T25`).
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** .claude/agents/pantonic-planner.md item 14: a rodada de replanejamento grava a medida dos dois mundos, antes e depois (R-05 doutrina)
  - **Contrato:** rodada de replanejamento deixa medida gravada de antes e de depois de cada card que ela emite
  - **Não refazer:** o trecho do item 14
  - **Pendente:** nenhum

### RAF-T19 — A conferência do modelo julga só a versão vigente quando pedida [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** Quem executa faz a conferência do modelo julgar só a versão vigente quando pedida assim, deixando a versão pendente para o marco.
- **Fundamento:** `DRF-1`, `DRF-14`, `DRF-37`; `F-19` (com a pendente presente, o `check` valida a `## 1A` e prefixa as violações com `1A: `; o `V1` da operação sem card vale em qualquer bloco); relatório `R-04` (auditoria reg. 31 e 32).
- **Depende de:** `RAF-T18`
- **Operação do modelo:** `OP-19`
  - OP-19: Quem executa faz a conferência do modelo julgar só a versão vigente quando pedida assim, deixando a versão pendente para o marco.
  - precisa de: escolhas do dono sobre o roteiro — Ninguém altera: fixam a rota das operações que dependem delas.; despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/modelo.py`, só biblioteca padrão; carrega o `backlog.py` da raiz dada por `--root` (`_load_backlog`) e chama `backlog._parse_plano`, que exige o plano sob essa raiz. Primeira tarefa da etapa C: nasce `blocked` até o `go` do Marco 3 (`DRF-5`). O `check` sem a flag nova segue julgando as duas versões; quem passa a pedir a flag é o despacho (`RAF-T20`). O contrato do objeto é: "Quem implementa acrescenta à conferência o que cada operação pede, sem mudar o que ela já julga quando chamada como hoje."
- **Arquivos-alvo:**
  - `.claude/tools/modelo.py`
  - `tests/test_modelo.py`
- **Contratos/classes:** `validar(modelo: Modelo, plano, modelo_pendente: Modelo | None = None, *, pendente: bool = False, so_vigente: bool = False) -> list[str]` (parâmetro novo `so_vigente`) e `verbo_check(args) -> int`. Quatro regras:
  1. O subparser `check` de `main` ganha a opção `--so-vigente` (`action="store_true"`, ajuda `Julga só a '## 1' (versão vigente); a '## 1A' fica para o marco (R-04).`).
  2. `verbo_check`, com `--so-vigente`: chama `validar(modelo, plano, modelo_pendente, so_vigente=True)` e **não** acrescenta as violações `1A: ` da pendente; sem a flag, tudo como hoje.
  3. `validar`, com `so_vigente=True`: a violação `V20` (pendente fora de sequência) não se emite; as demais, como hoje.
  4. `validar`, violação `V4` (`V4 <ID> — operação inexistente OP-<n>`), com ou sem a flag (`DRF-37`): conjunto novo `numeros_pendente` = os números das operações de `modelo_pendente` (vazio sem pendente), e `V4` só se emite quando o número citado não está em `numeros_operacoes` nem em `numeros_pendente`. O comentário acima do conjunto cita `DRF-37` do `P-0755`.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_modelo.py`, nesta ordem: o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card e começa na coluna 0); o helper `_raiz_modelo_pendente(tmp_path: Path, tarefas_op2: str = "", card_op2: bool = False, texto_op1: str = "Primeira operação da fixture.", texto_op2: str = "Segunda operação, nova na versão pendente.", op_card2: str = "OP-2") -> tuple[Path, Path]`, que cria `tmp_path/raiz/.claude/tools/` com cópias de `backlog.py` e `caminhos.py` do repositório (`shutil.copy2` a partir de `_ROOT`), grava em `tmp_path/raiz/docs/plans/P-0999-pendente.md` o `_MODELO_PENDENTE_TEXTO` com `@TAREFAS_OP2@` trocado por `tarefas_op2` e `@TEXTO_OP1@` por `texto_op1`, seguido, com `card_op2`, do `_CARD_OP2_TEXTO` com `@OP_CARD2@` trocado por `op_card2` e `@TEXTO_OP2@` por `texto_op2`, e devolve `(raiz, plano)`; e os quatro testes da seção `Testes`.

     ```python
     _MODELO_PENDENTE_TEXTO = """# P-0999 — Plano com versão pendente
     **Prefixo das tarefas no diário:** `EX-T<n>`

     ## 1. Modelo conceitual

     **Estado do modelo:** versão 1 · 2026-09-10 · autor: modelador · 1 operações · 2 propriedades · situação: vigente

     ### 1.1 Objetos

     | objeto | o que é | propriedades | contrato | origem | lastro |
     |---|---|---|---|---|---|
     | insumo | dado de entrada | status | um registro por rodada | externo | lastro da fixture |
     | produto | o produto da primeira operação | status | um registro validado | OP-1 | lastro da fixture |

     ### 1.2 Fluxo de operações

     - **OP-1** — Primeira operação da fixture.
       - `precisa de: insumo` · `altera: produto.status` · `tarefas: EX-T1`

     ### 1.3 Estado inicial e estado final

     | propriedade | estado inicial | estado final |
     |---|---|---|
     | insumo.status | lido | lido |
     | produto.status | rascunho | validado |

     ### 1.4 Registro de versões

     | versão | data | situação | por |
     |---|---|---|---|
     | 1 | 2026-09-10 | vigente | modelador |
     | 2 | 2026-09-21 | pendente | modelador, emenda |

     ## 1A. Modelo conceitual — versão pendente de validação

     **Estado do modelo:** versão 2 · 2026-09-21 · autor: modelador · 2 operações · 3 propriedades · situação: pendente

     ### 1.1 Objetos

     | objeto | o que é | propriedades | contrato | origem | lastro |
     |---|---|---|---|---|---|
     | insumo | dado de entrada | status | um registro por rodada | externo | lastro da fixture |
     | produto | o produto da primeira operação | status | um registro validado | OP-1 | lastro da fixture |
     | resultado | o produto da segunda operação | nível | um relatório derivado | OP-2 | lastro da fixture |

     ### 1.2 Fluxo de operações

     - **OP-1** — Primeira operação da fixture.
       - `precisa de: insumo` · `altera: produto.status` · `tarefas: EX-T1`
     - **OP-2** — Segunda operação, nova na versão pendente.
       - `precisa de: produto` · `altera: resultado.nível` · `tarefas: @TAREFAS_OP2@`

     ### 1.3 Estado inicial e estado final

     | propriedade | estado inicial | estado final |
     |---|---|---|
     | insumo.status | lido | lido |
     | produto.status | rascunho | validado |
     | resultado.nível | inicial | alto |

     ## 5. Tarefas

     ### EX-T1 — Um [Sonnet · classe mecanica]
     - **Operação do modelo:** `OP-1`
       - OP-1: @TEXTO_OP1@
       - precisa de: insumo — um registro por rodada
     """

     _CARD_OP2_TEXTO = """
     ### EX-T2 — Dois [Sonnet · classe mecanica]
     - **Operação do modelo:** `@OP_CARD2@`
       - @OP_CARD2@: @TEXTO_OP2@
       - precisa de: produto — um registro validado
     """
     ```
  2. Rodar `python -m pytest tests/test_modelo.py -q -k so_vigente` e conferir que os três testes que passam `--so-vigente` falham (a flag não existe) e o `test_tr_sem_so_vigente_julga_as_duas_versoes` passa.
  3. Aplicar as quatro regras de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 4 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - O `check` sem `--so-vigente` continua saindo como hoje sobre as fixtures de `tests/fixtures/modelo/`, exceto a linha `V4 EX-T2 — operação inexistente OP-2` de `fluxo-pendente.md`, que sai pela regra 4; nenhum teste existente afirma essa linha.
  - Nenhuma linha que já existia em `tests/test_modelo.py` sai ou muda: o card só acrescenta ao fim do arquivo; as fixtures de `tests/fixtures/modelo/` não mudam.
  - Os testes gravam só em `tmp_path`.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não editar `.claude/tools/backlog.py` (o despacho passa a pedir a flag na `RAF-T20`); não acrescentar violação nova ao vocabulário (a `V22` é da `RAF-T21`); não mexer em `_diff_fluxo` nem em `_diff_estado` (`RAF-T22`); não mudar a saída `modelo: OK — …` nem a `modelo: FALHOU — …`.
- **Contingências:**
  - se um teste que já existia em `tests/test_modelo.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_so_vigente_ignora_a_versao_pendente` — `tarefas_op2` vazio (a `OP-2` da `## 1A` sem card): `check --so-vigente --root <raiz>` sai 0 com `modelo: OK — 1 operações` no stdout e sem `1A:` no stderr (hoje o argparse recusa a flag e sai 2). TR `test_tr_sem_so_vigente_julga_as_duas_versoes` — o mesmo plano, sem a flag: sai 1 com `1A: V1 OP-2 — operação sem tarefa` no stderr (a regra concorrente, julgar sempre só a vigente, sairia 0). TF `test_tf_so_vigente_card_da_operacao_nova_nao_e_v4` — `tarefas_op2="EX-T2"` e o card `EX-T2` citando a `OP-2`: `check` sai 0 sem a flag e sai 0 com ela (hoje sai 1 com `V4 EX-T2 — operação inexistente OP-2`). TR `test_tr_so_vigente_operacao_ausente_das_duas_segue_v4` — o card `EX-T2` cita `OP-9`: `check --so-vigente` sai 1 com `V4 EX-T2 — operação inexistente OP-9`. Suíte `tests/test_modelo.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_modelo.py -q -k so_vigente` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - conferência do modelo.versões julgadas — pode julgar só a vigente quando pedida assim; sem o pedido, continua julgando as duas — Verificação 1
- **Fora do escopo desta tarefa:** o despacho com a flag (`RAF-T20`); a violação do texto copiado divergente (`RAF-T21`); a diferença entre versões (`RAF-T22`); a promoção no marco (`RAF-T23`).
- **Handover:** 2026-09-29 · para `RAF-T20`
  - **Entregue:** modelo.py check --so-vigente julga só a versão vigente (sem V20 e sem as violações 1A:); V4 aceita operação presente só na pendente (DRF-37), com ou sem a flag; 4 testes novos, suíte 586
  - **Contrato:** sem a flag o check segue julgando as duas versões, exceto o V4 de operação só da pendente (versão 3 pendente do modelo acerta o contrato)
  - **Não refazer:** --so-vigente, numeros_pendente e os testes
  - **Pendente:** nenhum

### RAF-T19a — O teste distingue o check com e sem --so-vigente pela versão pendente fora de sequência [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa acrescenta à suíte do `modelo.py` o caso que distingue a regra 3 da `RAF-T19`: com a versão pendente fora de sequência, o `check --so-vigente` não emite a `V20` e o `check` sem a flag a emite.
- **Fundamento:** `DRF-59`; `AE-169` (laudo da `RAF-T19`, ressalva 91: os quatro testes da `RAF-T19` montam a pendente em versão 2 contra a vigente 1, a `V20` nunca dispara, e tirar a guarda `not so_vigente` de `validar` deixa os quatro verdes, critério (ix) da rubrica §8); relatório `R-04`. Medido pelo consultor em cópia (2026-09-29): com os dois testes abaixo, tirar a linha `and not so_vigente` de `validar` faz o TF sair `1 failed`.
- **Depende de:** `RAF-T19`
- **Operação do modelo:** `OP-19`
  - OP-19: Quem executa faz a conferência do modelo julgar só a versão vigente quando pedida assim, deixando a versão pendente para o marco.
  - precisa de: escolhas do dono sobre o roteiro — Ninguém altera: fixam a rota das operações que dependem delas.; despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** teste do instrumento `.claude/tools/modelo.py`; nenhum código de produção muda. O caso reusa o helper `_raiz_modelo_pendente` da `RAF-T19` (com o card da `OP-2`, para que a `## 1A` saia limpa) e só troca a versão da pendente de 2 para 3 no plano gravado, de modo que a `V20` seja a única violação e a única diferença entre o `check` com e sem a flag.
- **Arquivos-alvo:**
  - `tests/test_modelo.py`
- **Passos:**
  1. Acrescentar ao fim de `tests/test_modelo.py` o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card e começa na coluna 0; duas linhas vazias antes de cada `def`).

     ```python
     def _raiz_pendente_fora_de_sequencia(tmp_path: Path) -> tuple[Path, Path]:
         """RAF-T19a: a raiz de `_raiz_modelo_pendente` com o card da `OP-2` e a `## 1A` em versão 3
         contra a vigente 1, para que só a `V20` distinga o `check` com e sem `--so-vigente`."""
         raiz, plano = _raiz_modelo_pendente(tmp_path, tarefas_op2="EX-T2", card_op2=True)
         texto = plano.read_text(encoding="utf-8")
         plano.write_text(
             texto.replace("**Estado do modelo:** versão 2 ·", "**Estado do modelo:** versão 3 ·"),
             encoding="utf-8",
         )
         return raiz, plano


     def test_tf_so_vigente_pendente_fora_de_sequencia_nao_e_v20(tmp_path, capsys):
         """TF (RAF-T19a): pendente em versão 3 contra a vigente 1 — `check --so-vigente` sai 0 sem
         `V20` no stderr (sem a guarda `not so_vigente` sairia 1 com a `V20`)."""
         modelo = _load_modelo()
         raiz, plano = _raiz_pendente_fora_de_sequencia(tmp_path)

         codigo = modelo.main(["check", "--plano", str(plano), "--root", str(raiz), "--so-vigente"])
         saida = capsys.readouterr()

         assert codigo == 0
         assert "V20" not in saida.err


     def test_tr_sem_so_vigente_pendente_fora_de_sequencia_segue_v20(tmp_path, capsys):
         """TR (RAF-T19a): o mesmo plano, sem a flag, sai 1 com
         `V20 secao — versão pendente fora de sequência` no stderr."""
         modelo = _load_modelo()
         raiz, plano = _raiz_pendente_fora_de_sequencia(tmp_path)

         codigo = modelo.main(["check", "--plano", str(plano), "--root", str(raiz)])
         saida = capsys.readouterr()

         assert codigo == 1
         assert "V20 secao — versão pendente fora de sequência" in saida.err
     ```
  2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `586 passed`, 2026-09-29, revisão da `RAF-T19`).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Nenhuma linha que já existia em `tests/test_modelo.py` sai ou muda: o card só acrescenta ao fim do arquivo; `.claude/tools/modelo.py` e as fixtures de `tests/fixtures/modelo/` não mudam.
  - Os testes gravam só em `tmp_path`.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `validar` nem `verbo_check` (a regra 3 já está entregue pela `RAF-T19`); não mudar `_raiz_modelo_pendente`, `_MODELO_PENDENTE_TEXTO` nem `_CARD_OP2_TEXTO`; não mexer nos quatro testes da `RAF-T19` nem no `test_tf_check_pendente_fora_de_sequencia_v20`.
- **Contingências:**
  - se um dos dois testes novos falhar → parar e sinalizar `blocked` razão `premissa`, nomeando o teste e a violação que saiu (a regra 3 da `RAF-T19` não está como o card a descreve).
  - se um teste que já existia em `tests/test_modelo.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_so_vigente_pendente_fora_de_sequencia_nao_e_v20` — card `EX-T2` da `OP-2` presente e a `## 1A` em versão 3 contra a vigente 1: `check --so-vigente --root <raiz>` sai 0 sem `V20` no stderr (sem a guarda `not so_vigente`, sai 1 com a `V20`). TR `test_tr_sem_so_vigente_pendente_fora_de_sequencia_segue_v20` — o mesmo plano, sem a flag: sai 1 com `V20 secao — versão pendente fora de sequência` no stderr (a regra concorrente, o `check` sem a flag também calar a `V20`, sairia 0). Suíte `tests/test_modelo.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_modelo.py -q -k "so_vigente and fora_de_sequencia"` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - conferência do modelo.versões julgadas — pedida só a vigente, a versão pendente fora de sequência não recusa a conferência; sem o pedido, a `V20` a recusa — Verificação 1
- **Fora do escopo desta tarefa:** o texto da `RAF-T19` (`done`), que fica como executado; o contrato do objeto `conferência do modelo` (versão 3 pendente, `DRF-60`); o despacho com a flag (`RAF-T20`).
- **Handover:** 2026-09-29 · para `RAF-T21`
  - **Entregue:** tests/test_modelo.py: 2 testes novos (pendente em versão 3 contra vigente 1): check --so-vigente sai 0 sem V20; sem a flag sai 1 com V20; suíte 588
  - **Contrato:** a regra 3 da RAF-T19 (so_vigente não emite V20) tem teste que a discrimina
  - **Não refazer:** os dois testes e o helper
  - **Pendente:** nenhum

### RAF-T20 — O despacho pede à conferência do modelo só a versão vigente [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa faz o despacho de tarefa pedir à conferência do modelo só o julgamento da versão vigente.
- **Fundamento:** `DRF-1`, `DRF-14`; `F-9` (o `despachar` roda `modelo.py check` por subprocesso e aceita exit 0 ou 2), `F-19` (emenda que cria operação sem card recusa o despacho por construção); relatório `R-04` (auditoria reg. 31 e 32: o ato do dono do plano fictício travou o despacho da tarefa seguinte).
- **Depende de:** `RAF-T19`
- **Operação do modelo:** `OP-20`
  - OP-20: Quem executa faz o despacho de tarefa pedir à conferência do modelo só o julgamento da versão vigente.
  - precisa de: conferência do modelo — Quem implementa acrescenta à conferência o que cada operação pede e mantém o que ela já julga quando chamada como hoje, com uma só mudança: enquanto houver versão pendente, o card que cita uma operação que só ela tem deixa de ser recusado.; despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/backlog.py`, função `despachar`; só biblioteca padrão. O `modelo.py` roda como subprocesso do irmão (`irmao / "modelo.py"`), nunca por `import`, e carrega o `backlog.py` da raiz dada por `--root`. A opção `--so-vigente` do `modelo.py check` existe desde a `RAF-T19`: julga só a `## 1`, não acrescenta as violações `1A: ` e não acusa `V4` do card cuja operação só existe na `## 1A`. O contrato do objeto é: "Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor."
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
- **Contratos/classes:** `despachar(repo: Path, id_: str, mundo: str | None = None) -> ResultadoStatus` — assinatura inalterada. Uma regra: a lista de argumentos do `subprocess.run` do `modelo.py check` (a que hoje é `[sys.executable, str(irmao / "modelo.py"), "check", "--plano", plano_abs, "--root", str(repo)]`) ganha `"--so-vigente"` depois de `str(repo)`, com o comentário `` # `R-04` (`DRF-14` do `P-0755`): o despacho julga só a `## 1`; a `## 1A` fica para o marco. `` na linha de cima. O teste do exit (0 ou 2 seguem, outro recusa com `despachar: recusado — modelo: <última linha do stderr>`) não muda.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_backlog.py`, nesta ordem: o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card e começa na coluna 0); o helper `_montar_repo_despachar_com_pendente(tmp_path: Path, operacao_gam_t2: str) -> Path`, que chama `_montar_repo_despachar(tmp_path)`, copia `.claude/tools/backlog.py` do repositório (`_ROOT`) para `.claude/tools/` da cópia (o `modelo.py check` carrega o `backlog.py` da raiz dada), grava em `docs/plans/P-0-gama/plano.md` da cópia o `_GAM_PLANO_COM_PENDENTE_TEXTO` com `@OPERACAO_GAM_T2@` trocado por `operacao_gam_t2`, roda `_run_git_despachar(["add", "-A"], repo)` e `_run_git_despachar(["commit", "-m", "plano com versão pendente"], repo)` e devolve a cópia; e os dois testes da seção `Testes`.

     ```python
     _GAM_PLANO_COM_PENDENTE_TEXTO = """# P-0 — Plano gama

     **Prefixo das tarefas no diário:** `GAM-T<n>`

     ## 1. Modelo conceitual

     **Estado do modelo:** versão 1 · 2026-01-01 · autor: modelador · 1 operações · 2 propriedades · situação: vigente

     ### 1.1 Objetos

     | objeto | o que é | propriedades | contrato | origem | lastro |
     |---|---|---|---|---|---|
     | insumo | dado de entrada | status | um registro por rodada | externo | lastro da fixture |
     | produto | o produto da primeira operação | status | um registro validado | OP-1 | lastro da fixture |

     ### 1.2 Fluxo de operações

     - **OP-1** — Primeira operação da fixture.
       - `precisa de: insumo` · `altera: produto.status` · `tarefas: GAM-T1, GAM-T2`

     ### 1.3 Estado inicial e estado final

     | propriedade | estado inicial | estado final |
     |---|---|---|
     | insumo.status | lido | lido |
     | produto.status | rascunho | validado |

     ### 1.4 Registro de versões

     | versão | data | situação | por |
     |---|---|---|---|
     | 1 | 2026-01-01 | vigente | modelador |
     | 2 | 2026-01-02 | pendente | modelador, emenda |

     ## 1A. Modelo conceitual — versão pendente de validação

     **Estado do modelo:** versão 2 · 2026-01-02 · autor: modelador · 2 operações · 3 propriedades · situação: pendente

     ### 1.1 Objetos

     | objeto | o que é | propriedades | contrato | origem | lastro |
     |---|---|---|---|---|---|
     | insumo | dado de entrada | status | um registro por rodada | externo | lastro da fixture |
     | produto | o produto da primeira operação | status | um registro validado | OP-1 | lastro da fixture |
     | resultado | o produto da segunda operação | nível | um relatório derivado | OP-2 | lastro da fixture |

     ### 1.2 Fluxo de operações

     - **OP-1** — Primeira operação da fixture.
       - `precisa de: insumo` · `altera: produto.status` · `tarefas: GAM-T1, GAM-T2`
     - **OP-2** — Segunda operação, nova na versão pendente.
       - `precisa de: produto` · `altera: resultado.nível` · `tarefas: `

     ### 1.3 Estado inicial e estado final

     | propriedade | estado inicial | estado final |
     |---|---|---|
     | insumo.status | lido | lido |
     | produto.status | rascunho | validado |
     | resultado.nível | inicial | alto |

     ## 5. Tarefas

     ### GAM-T1 — Primeira tarefa [Sonnet · classe implementacao]
     - **Objetivo:** fixture.
     - **Operação do modelo:** `OP-1`
       - OP-1: Primeira operação da fixture.
       - precisa de: insumo — um registro por rodada
     - **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
     - **Verificação:**
       1. `python -c "print('a')"` → `b` — antes `a`, depois `b`
     - **Pronto quando:** fixture existe.

     ### GAM-T2 — Segunda tarefa [Sonnet · classe implementacao]
     - **Objetivo:** fixture.
     @OPERACAO_GAM_T2@- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
     - **Verificação:**
       1. `python -c "print('a')"` → `b` — antes `a`, depois `b`
     - **Pronto quando:** fixture existe.
     """

     _OPERACAO_GAM_T2 = """- **Operação do modelo:** `OP-1`
       - OP-1: Primeira operação da fixture.
       - precisa de: insumo — um registro por rodada
     """
     ```
  2. Rodar `python -m pytest tests/test_backlog.py -q -k versao_vigente` e conferir que o TF falha (`despachar: recusado — modelo:`) e o TR passa.
  3. Aplicar a regra de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Nenhuma linha que já existia em `tests/test_backlog.py` sai ou muda: o card só acrescenta ao fim do arquivo; a fixture `tests/fixtures/backlog/pasta/` não muda (só a cópia em `tmp_path`).
  - Os testes gravam só em `tmp_path`; o `git` roda só no repositório da cópia.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não editar `.claude/tools/modelo.py` (a flag é da `RAF-T19`); não mudar o gate do modelo de `encerrar.py` (o fechamento roda o `check` completo, que desde a `RAF-T19` não acusa `V4` do card da operação nova); não mudar a ordem dos gates do `despachar` nem o que ele imprime ou grava.
- **Contingências:**
  - se um teste que já existia em `tests/test_backlog.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se `python .claude/tools/modelo.py check --help` não listar `--so-vigente` → parar e sinalizar `blocked` razão `dependencia`, nomeando a `RAF-T19`.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_despachar_versao_vigente_segue_com_pendente_incompleta` — plano gama com a `## 1A` cuja `OP-2` não tem card e o `GAM-T2` com o campo: `despachar GAM-T1` sai 0, sem `despachar: recusado` no stderr (hoje sai 1 com `despachar: recusado — modelo: modelo: FALHOU — 1 violação(ões)`, pela `1A: V1 OP-2 — operação sem tarefa`). TR `test_tr_despachar_versao_vigente_recusa_defeito_da_vigente` — o mesmo plano com `operacao_gam_t2` vazio (o `GAM-T2` sem `Operação do modelo`, `V2` da `## 1`): sai 1 com `despachar: recusado — modelo:` no stderr (a regra concorrente, tirar o gate do modelo, sairia 0). Suíte `tests/test_backlog.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_backlog.py -q -k versao_vigente` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - despacho de tarefa.versão do modelo julgada — o despacho julga só a versão vigente; a pendente fica para o marco — Verificação 1
- **Fora do escopo desta tarefa:** o `--so-vigente` do `modelo.py` (`RAF-T19`); a doutrina da rota do modelador com operação nova (`RAF-T24`); o card da operação nova (`RAF-T25`).
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** backlog.py despachar chama modelo.py check --so-vigente (a ## 1A fica para o marco); 2 testes novos, suíte 590
  - **Contrato:** versão pendente incompleta não trava o despacho; defeito da vigente continua recusando
  - **Não refazer:** a flag no despachar e os testes
  - **Pendente:** nenhum

### RAF-T21 — A conferência do modelo recusa o card que copia a operação com outro texto [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** Quem executa faz a conferência do modelo recusar o card cujo texto copiado da operação difere do texto da versão que ele cita.
- **Fundamento:** `DRF-15`, `DRF-37`, `DRF-61`; `F-19` (vocabulário `V1`..`V21`; `V4` e `V14` julgam o card; nenhum confere o texto copiado); relatório `R-06` (auditoria reg. 36 e 37: o `check` aprovou card com texto de operação divergente).
- **Depende de:** `RAF-T19`, `RAF-T19a`
- **Operação do modelo:** `OP-21`
  - OP-21: Quem executa faz a conferência do modelo recusar o card cujo texto copiado da operação difere do texto da versão que ele cita.
  - precisa de: conferência do modelo — Quem implementa acrescenta à conferência o que cada operação pede e mantém o que ela já julga quando chamada como hoje, com uma só mudança: enquanto houver versão pendente, o card que cita uma operação que só ela tem deixa de ser recusado.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/modelo.py`, função `validar`; só biblioteca padrão. A violação nova julga o card contra a versão que ele cita: a operação citada pelo número na vigente e, com a `## 1A` presente, também na pendente — o card da operação nova (escrito na rodada que segue a emenda, `DRF-14`) e o card antigo de uma operação renumerada pela emenda copiam textos de versões diferentes, e os dois são válidos até o marco (`DRF-37`). A reescrita do texto nos cards, na promoção, é da `RAF-T23`. O contrato do objeto é: "Quem implementa acrescenta à conferência o que cada operação pede, sem mudar o que ela já julga quando chamada como hoje."
- **Arquivos-alvo:**
  - `.claude/tools/modelo.py`
  - `tests/test_modelo.py`
- **Contratos/classes:** três regras:
  1. Função nova `_texto_copiado(item_texto: str, op_id: str) -> str | None`, logo antes de `validar`: o resto da primeira linha do card que começa por `  - <op_id>: ` (dois espaços, hífen, espaço, o id, dois-pontos, espaço), com os espaços colapsados (`" ".join(resto.split())`); `None` sem essa linha.
  2. Em `validar`, no laço dos cards (o bloco `if not pendente:` que emite `V2`, `V4` e `V14`), logo depois da checagem de `V14`, para cada `op_id` citado cujo número existe em alguma versão: os textos da operação são todos os de mesmo número na vigente e, havendo `modelo_pendente`, na pendente, com espaços colapsados — número duplicado numa versão (o caso da `V11`) conta cada um dos textos, nunca só o último (`DRF-61`); quando o texto copiado não é `None` e não é nenhum deles, emite `V22 <ID> — texto de OP-<n> diverge da versão <v>`, com `<v>` = versão da vigente quando o número existe nela, senão versão da pendente. Número que não existe em versão nenhuma já sai `V4` e não ganha `V22`. Vale com e sem `--so-vigente`.
  3. A descrição do `argparse` de `main` troca `contra o vocabulário de violações V1..V21 (### 16); show deriva` por `contra o vocabulário de violações V1..V22 (### 16; V22 do P-0755); show deriva`.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_modelo.py` os três testes da seção `Testes`, com o helper `_raiz_modelo_pendente` da `RAF-T19`.
  2. Rodar `python -m pytest tests/test_modelo.py -q -k texto_divergente` e conferir que os dois TF falham e o TR passa.
  3. Aplicar as três regras de `Contratos/classes` (redespacho, `DRF-61`: os três testes e as regras 1 e 3 já estão na árvore; a regra 2 se ajusta à forma de hoje, um conjunto de textos por número).
  4. Rodar `python .claude/tools/modelo.py check --plano docs/plans/P-0754-auditoria-final/plano.md` e conferir exit 0 (o único plano vivo com modelo além deste; medido no ensaio: nenhum card dele diverge).
  5. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 3 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Nenhuma linha que já existia em `tests/test_modelo.py` sai ou muda: o card só acrescenta ao fim do arquivo; as fixtures de `tests/fixtures/modelo/` não mudam.
  - Os testes gravam só em `tmp_path`.
  - O `check` passa a sair 1 sobre quatro planos encerrados, com a divergência que a `R-06` descreve (medido no ensaio, `F-31`): `docs/plans/P-0746-lastro-do-modelo.md` (1 linha `V22`, `LST-T5`), `docs/plans/P-0747-consultor-de-plano.md` (7, `CON-T3`..`CON-T5a`), `docs/plans/P-0748-tela-do-gerente.md` (5, `TLG-T2`..`TLG-T4`) e `docs/plans/P-0753-auditoria-estagio-1/plano.md` (1, `AF-T19`). Nenhum deles se edita: são registro histórico, e nenhum instrumento roda o `check` sobre plano encerrado (§7).
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não reescrever card de plano nenhum para acertar texto (a reescrita é da promoção, `RAF-T23`); não mexer em `_tem_subbullets` nem no `V14`; não mexer em `_diff_fluxo` nem em `_diff_estado` (`RAF-T22`); não renumerar nem reordenar as violações de hoje.
- **Contingências:**
  - se um teste que já existia em `tests/test_modelo.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o passo 4 der exit 1 → parar e sinalizar `blocked` razão `premissa`, colando as linhas `V22` do `P-0754`.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_texto_divergente_v22_da_vigente` — `tarefas_op2="EX-T2"`, `card_op2=True` e o `EX-T1` com o texto `Primeira operação da fixture, na redação antiga.`: `check` sai 1 com `V22 EX-T1 — texto de OP-1 diverge da versão 1` no stderr (hoje sai 0). TR `test_tr_texto_divergente_so_em_espacos_nao_e_v22` — o `EX-T1` com `Primeira  operação da fixture. ` (espaço duplo e espaço na ponta): `check` sai 0 (a regra concorrente, comparação literal, acusaria `V22`). TF `test_tf_texto_divergente_v22_da_pendente` — o `EX-T2` com o texto `Outra redação da segunda operação.`: `check --so-vigente` sai 1 com `V22 EX-T2 — texto de OP-2 diverge da versão 2` (hoje sai 0). O teste existente `test_tf_check_invalido_lista_catorze_violacoes_na_ordem` é o TR do número duplicado (`DRF-61`): o `EX2-T3` de `plano-invalido-2.md` copia o primeiro dos dois `OP-3`, e só a regra concorrente (um texto por número, o último vence) o acusa `V22`; ele passa sem linha mudada. Suíte `tests/test_modelo.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_modelo.py -q -k texto_divergente` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - conferência do modelo.fidelidade do texto copiado no card — recusa o card cujo texto copiado diverge da versão que ele cita — Verificação 1
- **Fora do escopo desta tarefa:** a reescrita do texto da operação nos cards, na promoção da versão aceita (`RAF-T23`); a diferença entre versões (`RAF-T22`).
- **Handover:** 2026-09-29 · para `RAF-T22`
  - **Entregue:** modelo.py: V22 recusa card que copia a operação com texto diferente da versão citada, comparando com todos os textos de mesmo número (vigente e pendente; número duplicado conta cada um); 3 testes novos
  - **Contrato:** check sobre P-0754 e P-0755 sai 0; o teste das catorze violações segue intacto
  - **Não refazer:** a V22 e os testes texto_divergente
  - **Pendente:** nenhum

### RAF-T22 — A diferença entre versões mostra a operação inserida, a renumerada e a propriedade nova [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** Quem executa faz a conferência do modelo mostrar, entre duas versões, a operação inserida, a renumerada e a propriedade que só uma delas tem.
- **Fundamento:** `DRF-16`; `F-19` (`_diff_fluxo` casa só por número e emite `[+]`, `[-]`, `[~]`; `_diff_estado` só mostra chave presente nas duas versões); relatório `R-07` (auditoria reg. 34: a inserção de uma operação apareceu como alterações em cascata, e a propriedade nova não apareceu).
- **Depende de:** `RAF-T21`
- **Operação do modelo:** `OP-22`
  - OP-22: Quem executa faz a conferência do modelo mostrar, entre duas versões, a operação inserida, a renumerada e a propriedade que só uma delas tem.
  - precisa de: conferência do modelo — Quem implementa acrescenta à conferência o que cada operação pede e mantém o que ela já julga quando chamada como hoje, com uma só mudança: enquanto houver versão pendente, o card que cita uma operação que só ela tem deixa de ser recusado.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/modelo.py`, funções `_diff_fluxo` e `_diff_estado`, chamadas por `montar_drift` (verbo `show --drift`); só biblioteca padrão. A seção de objetos do drift (`_diff_objetos`) e o cabeçalho não mudam; `sem drift` continua saindo quando nenhuma das três seções tem linha. O contrato do objeto é: "Quem implementa acrescenta à conferência o que cada operação pede, sem mudar o que ela já julga quando chamada como hoje."
- **Arquivos-alvo:**
  - `.claude/tools/modelo.py`
  - `tests/test_modelo.py`
- **Contratos/classes:** `_diff_fluxo(vigente: Modelo, pendente: Modelo) -> list[str]` e `_diff_estado(vigente: Modelo, pendente: Modelo) -> list[str]` — assinaturas inalteradas. Duas regras:
  1. `_diff_fluxo` passa a casar em duas rodadas, e ganha docstring que cita `R-07` e `DRF-16` do `P-0755`. Rodada 1, por texto: para cada operação da pendente, na ordem, o par é a primeira operação da vigente, na ordem, com o mesmo texto (igualdade exata de `texto`) e ainda sem par. Rodada 2, por número: para cada operação da pendente ainda sem par, o par é a operação da vigente de mesmo número, se ela ainda não tem par. Saída, nesta ordem: percorrendo a pendente, a operação sem par sai `[+] OP-<k> — <texto da pendente>`; com par de mesmo texto e outro número, `[=] OP-<k> (era OP-<j>)`; com par de outro texto, `[~] OP-<k> — <texto da vigente> => <texto da pendente>`; com par de mesmo texto e mesmo número, nenhuma linha. Depois, percorrendo a vigente, a operação que não virou par de ninguém sai `[-] OP-<j> — <texto da vigente>`.
  2. `_diff_estado` emite, antes das linhas `[~]` de hoje: `[+] <chave> — <estado final da pendente>` para cada chave da pendente, na ordem dela, que a vigente não tem; e `[-] <chave> — <estado final da vigente>` para cada chave da vigente, na ordem dela, que a pendente não tem; as linhas `[~]` seguem como hoje. O comentário acima das duas voltas cita `DRF-16` do `P-0755`.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_modelo.py` o helper `_modelo_drift(modelo, textos: list[str], estado: list[tuple[str, str, str]], versao: int)` (um `modelo.Modelo` com as operações `OP-1`..`OP-n` dos `textos`, na ordem, `precisa_de`, `altera` e `tarefas` vazios, o `estado` dado e `data="2026-09-28"`) e os três testes da seção `Testes`, que chamam `modelo.montar_drift(vigente, pendente)` direto.
  2. Rodar `python -m pytest tests/test_modelo.py -q -k drift_versoes` e conferir que os dois TF falham e o TR passa.
  3. Aplicar as duas regras de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 3 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). Os testes de drift que já existem (`test_tf_show_drift_tres_marcadores`, `test_tf_show_drift_sem_diferenca`, `test_tf_drift_mostra_contrato_alterado`) continuam passando sem mudança.
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Nenhuma linha que já existia em `tests/test_modelo.py` sai ou muda: o card só acrescenta ao fim do arquivo; as fixtures de `tests/fixtures/modelo/` não mudam.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `_diff_objetos`, `montar_drift` nem o verbo `show`; não comparar texto com espaços colapsados no drift (a igualdade é exata, como hoje); não mexer em `validar` (`RAF-T19`, `RAF-T21`).
- **Contingências:**
  - se um teste que já existia em `tests/test_modelo.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_drift_versoes_insercao_mostra_nova_e_renumerada` — vigente `Primeira.`, `Segunda.`; pendente `Primeira.`, `Nova.`, `Segunda.`; mesmo estado: as linhas do drift contêm `[+] OP-2 — Nova.` e `[=] OP-3 (era OP-2)` e nenhuma começa por `[~] OP-` nem por `[-] OP-` (hoje saem `[+] OP-3 — Segunda.` e `[~] OP-2 — Segunda. => Nova.`). TR `test_tr_drift_versoes_texto_alterado_segue_por_numero` — vigente `Primeira.`; pendente `Primeira, reescrita.`: contém `[~] OP-1 — Primeira. => Primeira, reescrita.` e nenhuma linha `[+] OP-` nem `[-] OP-` (a regra concorrente, casar só por texto, daria `[+]` e `[-]`). TF `test_tf_drift_versoes_propriedade_de_uma_versao_so` — estado vigente `x.a` (final `fim`) e `x.c` (final `baixo`), pendente `x.a` (final `fim`) e `x.b` (final `alto`): contém `[+] x.b — alto` e `[-] x.c — baixo` (hoje nenhuma das duas). Suíte `tests/test_modelo.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_modelo.py -q -k drift_versoes` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - conferência do modelo.diferença entre versões — casa primeiro pelo texto, mostra operação nova, renumerada e alterada, e lista a propriedade que só uma das versões tem — Verificação 1
- **Fora do escopo desta tarefa:** a promoção da versão aceita e a reescrita dos cards (`RAF-T23`); o drift de objetos, que já mostra `[+]`, `[-]` e `[~]`.
- **Handover:** 2026-09-29 · para `RAF-T23`
  - **Entregue:** modelo.py show --drift mostra operação inserida, operação renumerada e propriedade nova entre vigente e pendente (ver RDO RAF-T22)
  - **Contrato:** a diferença entre versões nomeia inserção, renumeração e propriedade nova
  - **Não refazer:** o drift novo e os testes
  - **Pendente:** nenhum

### RAF-T22a — A diferença entre versões mostra a operação que muda o que precisa ou o que altera sem mudar o texto [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa faz a conferência do modelo mostrar, entre duas versões, a operação de mesmo texto cujo `precisa de:` ou `altera:` mudou, que hoje sai do drift sem linha nenhuma.
- **Fundamento:** `DRF-73`; `AE-187` (emenda do modelador da `DRF-68`: na versão 4 pendente, a `OP-30` ganha `rubrica de revisão` em `precisa de:` e a propriedade nova em `altera:`, e o `show --drift` não mostra nada disso, medido 2026-09-30); `DRF-16`; relatório `R-07`.
- **Depende de:** `RAF-T36`
- **Operação do modelo:** `OP-22`
  - OP-22: Quem executa faz a conferência do modelo mostrar, entre duas versões, a operação inserida, a renumerada e a propriedade que só uma delas tem.
  - precisa de: conferência do modelo — Quem implementa acrescenta à conferência o que cada operação pede e mantém o que ela já julga quando chamada como hoje, com uma só mudança: enquanto houver versão pendente, o card que cita uma operação que só ela tem deixa de ser recusado.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/modelo.py`, função `_diff_fluxo`, chamada por `montar_drift` (verbo `show --drift`); só biblioteca padrão. A `RAF-T22` escreveu, pelo card, "com par de mesmo texto e mesmo número, nenhuma linha", e o casamento compara só `texto`: a mudança do contrato de uma operação (listas `precisa_de` e `altera` da `Operacao`) fica fora do que o dono lê no marco. O casamento em duas rodadas, as linhas `[+]`, `[=]`, `[~]` de texto e `[-]` de hoje, `_diff_objetos`, `_diff_estado`, o cabeçalho e o `sem drift` não mudam. O docstring do módulo e o `help` de `--drift` dizem só "a diferença entre a versão vigente e a pendente" (medido): não mudam. O contrato do objeto é: "Quem implementa acrescenta à conferência o que cada operação pede, sem mudar o que ela já julga quando chamada como hoje."
- **Arquivos-alvo:**
  - `.claude/tools/modelo.py`
  - `tests/test_modelo.py`
- **Contratos/classes:** `_diff_fluxo(vigente: Modelo, pendente: Modelo) -> list[str]`, assinatura inalterada. Uma regra: para todo par (operação da pendente com a da vigente que casou com ela, por texto ou por número), depois da linha de texto que o par já emite hoje (ou de nenhuma), sai `[~] OP-<k> — precisa de: <lista da vigente> => <lista da pendente>` quando as listas `precisa_de` diferem, e depois `[~] OP-<k> — altera: <lista da vigente> => <lista da pendente>` quando as listas `altera` diferem; `<k>` é o número da pendente, cada lista unida por `, ` e a comparação é de lista, exata e na ordem. A lista `tarefas` não entra (é lastro, não modelo). O docstring de `_diff_fluxo` passa a dizer isso e a citar `AE-187` e `DRF-73` do `P-0755`.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_modelo.py`, depois da última linha de hoje (`    assert "[-] x.c — baixo" in linhas`, fim de `test_tf_drift_versoes_propriedade_de_uma_versao_so`), o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card).

     ```python


     def test_tf_drift_contrato_da_operacao_mostra_precisa_e_altera():
         """TF (RAF-T22a, AE-187/DRF-73): `OP-1` tem o mesmo texto e o mesmo número nas duas versões e
         muda só `precisa de:` e `altera:` — o drift mostra as duas listas; hoje o par de texto igual não
         emite linha nenhuma e `montar_drift` devolve `sem drift`."""
         modelo = _load_modelo()
         vigente = modelo.Modelo(versao=1, data="2026-09-28", operacoes=[
             modelo.Operacao(numero=1, texto="Única.", precisa_de=["a"], altera=["x.a"]),
         ])
         pendente = modelo.Modelo(versao=2, data="2026-09-28", operacoes=[
             modelo.Operacao(numero=1, texto="Única.", precisa_de=["a", "b"], altera=["x.a", "x.b"]),
         ])

         linhas = modelo.montar_drift(vigente, pendente).splitlines()

         assert "[~] OP-1 — precisa de: a => a, b" in linhas
         assert "[~] OP-1 — altera: x.a => x.a, x.b" in linhas


     def test_tr_drift_contrato_da_operacao_ignora_tarefas():
         """TR (RAF-T22a, DRF-73): `OP-1` muda só `tarefas:`, que é lastro e não modelo — o drift segue
         `sem drift`; a regra concorrente, comparar todo o sub-bullet, daria uma linha de `tarefas:`."""
         modelo = _load_modelo()
         vigente = modelo.Modelo(versao=1, data="2026-09-28", operacoes=[
             modelo.Operacao(numero=1, texto="Única.", tarefas=["EX-T1"]),
         ])
         pendente = modelo.Modelo(versao=2, data="2026-09-28", operacoes=[
             modelo.Operacao(numero=1, texto="Única.", tarefas=["EX-T1", "EX-T1a"]),
         ])

         assert modelo.montar_drift(vigente, pendente) == "sem drift"
     ```
  2. Rodar `python -m pytest tests/test_modelo.py -q -k drift_contrato_da_operacao` e conferir `1 failed, 1 passed`: o TF falha (hoje `sem drift`) e o TR passa.
  3. Aplicar a regra de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `tests/test_modelo.py` com `46 passed`, 2026-09-30). Os testes de drift que já existem (`test_tf_show_drift_tres_marcadores`, `test_tf_show_drift_sem_diferenca`, `test_tf_drift_mostra_contrato_alterado` e os três `drift_versoes`) continuam passando sem mudança.
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Nenhuma linha que já existia em `tests/test_modelo.py` sai ou muda: o card só acrescenta ao fim do arquivo; as fixtures de `tests/fixtures/modelo/` não mudam. A edição não troca a quebra de linha de nenhum dos dois arquivos (hoje `modelo.py` em CRLF, `test_modelo.py` em LF, 0 CR).
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não comparar a lista `tarefas`; não mudar o casamento das duas rodadas nem as linhas que ele já emite; não mudar `_diff_objetos`, `_diff_estado`, `montar_drift` nem o verbo `show`; não mexer em `validar`.
- **Contingências:**
  - se um teste que já existia em `tests/test_modelo.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_drift_contrato_da_operacao_mostra_precisa_e_altera` — `OP-1` `Única.` nas duas versões, `precisa de:` `a` → `a, b` e `altera:` `x.a` → `x.a, x.b`: as linhas do drift contêm `[~] OP-1 — precisa de: a => a, b` e `[~] OP-1 — altera: x.a => x.a, x.b` (hoje `sem drift`). TR `test_tr_drift_contrato_da_operacao_ignora_tarefas` — `OP-1` `Única.` muda só `tarefas:`: o drift é `sem drift` (a regra concorrente, comparar todo o sub-bullet, daria linha). Suíte `tests/test_modelo.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_modelo.py -q -k drift_contrato_da_operacao` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - conferência do modelo.diferença entre versões — casa primeiro pelo texto, mostra operação nova, renumerada e alterada, e lista a propriedade que só uma das versões tem — Verificação 1
- **Fora do escopo desta tarefa:** o texto da `RAF-T22` (`done`), que fica como executado; a mensagem do Marco 5 ao dono, que carrega a mudança da `OP-30` à mão (`AE-187`); o drift do estado inicial (matéria inconclusiva do cenário, desenho do verbo).
- **Handover:** 2026-09-30 · para `RAF-T40`
  - **Entregue:** .claude/tools/modelo.py, _diff_fluxo: todo par de operações emite [~] OP-<k> — precisa de: <vigente> => <pendente> e [~] OP-<k> — altera: <vigente> => <pendente> quando a lista difere; tests/test_modelo.py com TF e TR novos
  - **Contrato:** show --drift mostra a mudança de precisa de/altera de operação com o mesmo texto; tarefas: não entra
  - **Não refazer:** nada a declarar
  - **Pendente:** lista vazia sai como lado em branco (achado do laudo, sem ação)

### RAF-T23 — O comando do marco promove a versão aceita e cobra a validação do consultor [Sonnet · esforço high · classe implementacao]
- **Objetivo:** Quem executa faz o fechamento do marco promover sozinho a versão aceita, cobrando a linha de validação do consultor e acertando o texto da operação em cada card.
- **Fundamento:** `DRF-1`, `DRF-17`, `DRF-38`; `F-20` (`marco --aceita-versao K` recusa sem `## 1A`, grava o veredito e imprime o dossiê `Ato: emenda`; não promove nem cobra o consultor), `F-21` (a promoção hoje é do modelador; a validação do consultor não tem forma escrita); relatório `R-06` e `R-08` (auditoria reg. 36 a 38: a promoção custou uma instância inteira do modelador, 55,0k, e os cards ficaram com a numeração antiga).
- **Depende de:** `RAF-T22`
- **Operação do modelo:** `OP-23`
  - OP-23: Quem executa faz o fechamento do marco promover sozinho a versão aceita, cobrando a linha de validação do consultor e acertando o texto da operação em cada card.
  - precisa de: conferência do modelo — Quem implementa acrescenta à conferência o que cada operação pede e mantém o que ela já julga quando chamada como hoje, com uma só mudança: enquanto houver versão pendente, o card que cita uma operação que só ela tem deixa de ser recusado.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/encerrar.py`, verbo `marco` (`gravar_marco` e `main`); só biblioteca padrão. O `encerrar.py` carrega os irmãos por `_carregar(<nome>)` (arquivo em `.claude/tools/` do kit, por caminho) e passa a carregar também `modelo.py` como `_modelo`, usando `_modelo.extrair_modelo`, `_modelo.validar` e as constantes `_modelo._HEADING_VIGENTE` e `_modelo._HEADING_PENDENTE` em processo — sem subprocesso, porque o `modelo.py check` carrega o `backlog.py` da raiz dada e a raiz dos testes não o tem. A validação da pendente é a mesma que o `check` completo prefixa com `1A: ` (`validar(pendente, plano, pendente=True)`), e o `validar` aceita, desde a `RAF-T21`, o card que copia o texto de qualquer das duas versões (`DRF-37`). `--recusa-versao` não muda. O contrato do objeto é: "Quem implementa recebe o comando que hoje só grava o veredito do marco e confere achados por semelhança de texto, e acrescenta o que a operação pede."
- **Arquivos-alvo:**
  - `.claude/tools/encerrar.py`
  - `tests/test_encerrar.py`
- **Contratos/classes:** `gravar_marco(repo: Path, plano_path: Path, *, marco: int, resultado: str, veredito: str, data: str, aceita_versao: str | None = None, recusa_versao: str | None = None, consultor: str | None = None) -> str | None` (parâmetro novo `consultor`); funções novas `promover_versao(linhas: list[str], k: int, data: str) -> tuple[list[str], int]`, `_checar_promocao(linhas: list[str], plano, k: str, marco: int, frase: str, plano_path: Path, repo: Path) -> None`, `_faixa_do_campo_operacao(linhas: list[str], tarefa_id: str) -> tuple[int, int] | None` e `_dossie_emenda(plano_path: Path, repo: Path, marco: int, frase: str, fato_novo: str, restricao: str) -> str`; classe nova `ConflitoDePromocao(EncerramentoError)`, com construtor `(mensagem: str, dossie: str)` e o atributo `dossie`. Oito regras:
  1. Depois da linha `_telemetria = _carregar("telemetria")`, a linha `_modelo = _carregar("modelo")`.
  2. `main`: o subparser `marco` ganha `--consultor` (`default=None`, ajuda `Linha de validação do consultor, verbatim; obrigatória com --aceita-versao (R-08).`), repassado a `gravar_marco` como `consultor=args.consultor`; no `except EncerramentoError`, no verbo `marco`, quando a exceção é `ConflitoDePromocao`, imprime `exc.dossie` no stdout antes da linha `marco: <mensagem>` do stderr.
  3. `gravar_marco`, checagens com `aceita_versao`, logo antes do comentário `# --- checagens concluídas; escritas a partir daqui`: `consultor` ausente ou vazio depois de `strip()` → `EncerramentoError("--aceita-versao exige --consultor com a linha de validação do consultor")`; `consultor` com mais de uma linha → `EncerramentoError("consultor: aceita no máximo uma linha")`; depois, `_checar_promocao(linhas, plano, aceita_versao.strip(), marco, veredito.strip(), plano_path, repo)`, com `plano` o `Plano` que a função já localiza no backlog.
  4. `_checar_promocao`, nesta ordem: `k` que não é só dígitos → `EncerramentoError("--aceita-versao exige o número da versão, recebeu '<k>'")`; conflitos, cada um `ConflitoDePromocao("conflito na promoção da versão <k> — <razão>", <dossiê>)`, com as razões `o plano não tem a ## 1` (sem a `## 1`), `a ## 1A é a versão <n>` (versão do cabeçalho da `## 1A` diferente de `k`), `o registro de versões não tem uma única linha vigente` e `o registro de versões não tem a linha pendente da versão <k>` (nenhuma linha do `### 1.4` da `## 1` com versão `k` e situação `pendente`); o dossiê é o `Ato: emenda` de hoje, montado por `_dossie_emenda`, com `Fato novo: o dono aceitou a versão <k> do modelo no Marco <m>. Conflito na promoção: <razão>.` e a `Restrição` de hoje do aceite; depois, as violações de `_modelo.validar(pendente, plano, pendente=True)`, cada uma prefixada `1A: `, → `EncerramentoError("versão pendente com violação — <violações unidas por '; '>")`; por fim, para cada id das listas `tarefas:` da pendente, `_faixa_do_campo_operacao` devolvendo `None` → `EncerramentoError("card '<ID>' da lista tarefas: da OP-<n> sem o campo Operação do modelo no plano")`.
  5. `gravar_marco`, célula do marco com `aceita_versao`: `f' {resultado} · {data} — "{frase_celula}" · consultor: "{consultor_celula}" '`, com `consultor_celula` = o `consultor` limpo e cada `|` trocado por `\|`, como a frase do dono; sem `aceita_versao`, a célula de hoje.
  6. `gravar_marco`, escrita com `aceita_versao`: depois de inserir o bloco da `## 0.` e antes de `_escrever_atomico`, `linhas, cards_reescritos = promover_versao(linhas, int(aceita_versao.strip()), data)`; o retorno passa a ser `marco: versão <k> promovida — <cards_reescritos> card(s) com a operação reescrita`, sem dossiê. Com `recusa_versao`, o dossiê de hoje, montado por `_dossie_emenda`. O docstring da função passa a descrever os três casos.
  7. `promover_versao` (`DRF-38`): (a) no `### 1.4 Registro de versões` da `## 1`, a linha de situação `vigente` passa a `obsoleta` e a célula `por` dela ganha `; Caiu pelo aceite da versão <k> em <data>`; a linha da versão `k` de situação `pendente` passa a `vigente`; cada linha do registro é reescrita `| <célula> | <célula> | … |`, com as células limpas; (b) a `## 1` nova é o cabeçalho `## 1. Modelo conceitual`, o conteúdo da `## 1A` sem o cabeçalho dela (até um `### 1.4` que houver nela, exclusive, e sem as linhas vazias do fim), com `situação: pendente` trocado por `situação: vigente` na linha que começa por `**Estado do modelo:**`, uma linha vazia, `### 1.4 Registro de versões`, uma linha vazia, o cabeçalho e o separador da tabela de antes, as linhas do registro de (a) e uma linha vazia; (c) a `## 1A` sai inteira, do cabeçalho à linha antes do próximo `## `; (d) para cada card das listas `tarefas:` da pendente, o campo `Operação do modelo` (a linha que começa por `- **Operação do modelo:**` dentro do card e as linhas seguintes que começam por dois espaços) é trocado pela linha `- **Operação do modelo:** ` seguida das operações da pendente que listam o card, cada uma `` `OP-<n>` ``, separadas por `, `, e, por operação, as linhas `  - OP-<n>: <texto da operação>` e `  - precisa de: <objeto> — <contrato>` (os objetos de `precisa de:` da operação, com os contratos da tabela de objetos da pendente, separados por `; `). Devolve as linhas e o número de cards distintos reescritos.
  8. `_faixa_do_campo_operacao`: o card vai do cabeçalho que começa por `### <ID> — ` até a linha antes do próximo `### ` ou `## `; devolve `(linha do campo, primeira linha depois dos sub-bullets)`, ou `None` sem card ou sem campo.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_encerrar.py`, nesta ordem: o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card e começa na coluna 0); o helper `_montar_repo_promocao(tmp_path: Path, tarefas_op1: str = "MRC-T2") -> Path`, que devolve `_montar_repo_marco(tmp_path, PLANO_MARCO_PROMOCAO.replace("@TAREFAS_OP1@", tarefas_op1))`; o helper `_card(texto: str, tarefa: str) -> str`, o trecho de `texto` do cabeçalho `### <tarefa> — ` até antes da próxima quebra seguida de `### `, ou até o fim; e os cinco testes da seção `Testes`, com `_argv_marco`.

     ```python
     PLANO_MARCO_PROMOCAO = """# P-0001 — Plano marco

     **Prefixo das tarefas no diário:** `MRC-T<n>`

     **Marcos de validação pelo dono:**

     | marco | o que o dono lê | veredito |
     |---|---|---|
     | **Marco 1** | a seção 1 | go |
     | **Marco 2** | a etapa A | pendente |

     ## 0. O problema, verbatim

     Texto do problema, verbatim.

     ## 1. Modelo conceitual

     **Estado do modelo:** versão 1 · 2026-09-10 · autor: modelador · 1 operações · 2 propriedades · situação: vigente

     ### 1.1 Objetos

     | objeto | o que é | propriedades | contrato | origem | lastro |
     |---|---|---|---|---|---|
     | insumo | dado de entrada | status | um registro por rodada | externo | lastro da fixture |
     | produto | o produto da operação | status | um registro validado | OP-1 | lastro da fixture |

     ### 1.2 Fluxo de operações

     - **OP-1** — Primeira operação da fixture.
       - `precisa de: insumo` · `altera: produto.status` · `tarefas: MRC-T1`

     ### 1.3 Estado inicial e estado final

     | propriedade | estado inicial | estado final |
     |---|---|---|
     | insumo.status | lido | lido |
     | produto.status | rascunho | validado |

     ### 1.4 Registro de versões

     | versão | data | situação | por |
     |---|---|---|---|
     | 1 | 2026-09-10 | vigente | modelador |
     | 2 | 2026-09-21 | pendente | modelador, emenda |

     ## 1A. Modelo conceitual — versão pendente de validação

     **Estado do modelo:** versão 2 · 2026-09-21 · autor: modelador · 2 operações · 3 propriedades · situação: pendente

     ### 1.1 Objetos

     | objeto | o que é | propriedades | contrato | origem | lastro |
     |---|---|---|---|---|---|
     | insumo | dado de entrada | status | um registro por rodada | externo | lastro da fixture |
     | esboço | o esboço da operação nova | estado | um esboço revisado | OP-1 | lastro da fixture |
     | produto | o produto da operação | status | um registro validado | OP-2 | lastro da fixture |

     ### 1.2 Fluxo de operações

     - **OP-1** — Operação nova, inserida antes.
       - `precisa de: insumo` · `altera: esboço.estado` · `tarefas: @TAREFAS_OP1@`
     - **OP-2** — Primeira operação da fixture.
       - `precisa de: esboço` · `altera: produto.status` · `tarefas: MRC-T1`

     ### 1.3 Estado inicial e estado final

     | propriedade | estado inicial | estado final |
     |---|---|---|
     | insumo.status | lido | lido |
     | esboço.estado | vazio | revisado |
     | produto.status | rascunho | validado |

     ## 5. Tarefas

     ### MRC-T1 — Tarefa da operação antiga [Sonnet · classe implementacao]
     - **Objetivo:** entregar algo.
     - **Operação do modelo:** `OP-1`
       - OP-1: Primeira operação da fixture.
       - precisa de: insumo — um registro por rodada
     - **Arquivos-alvo:** `a.py`.
     - **Verificação:** `pytest -q`.
     - **Pronto quando:** o teste passa.

     ### MRC-T2 — Tarefa da operação nova [Sonnet · classe implementacao]
     - **Objetivo:** entregar outra coisa.
     - **Operação do modelo:** `OP-1`
       - OP-1: Operação nova, inserida antes.
       - precisa de: insumo — um registro por rodada
     - **Arquivos-alvo:** `b.py`.
     - **Verificação:** `pytest -q`.
     - **Pronto quando:** o teste passa.
     """
     ```
  2. Rodar `python -m pytest tests/test_encerrar.py -q -k "promove_versao or validacao_do_consultor"` e conferir que os cinco falham (a opção `--consultor` não existe).
  3. Aplicar as oito regras de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 5 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). Os testes de `marco` que já existem, inclusive `test_tf_marco_recusa_versao_imprime_dossie_de_emenda`, continuam passando sem mudança.
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Todas as checagens da promoção correm antes da primeira escrita: recusa ou conflito deixam o plano byte a byte igual.
  - Nenhuma linha que já existia em `tests/test_encerrar.py` sai ou muda: o card só acrescenta ao fim do arquivo.
  - Os testes gravam só em `tmp_path`.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não rodar o `modelo.py` por subprocesso na promoção; não mudar o ramo `--recusa-versao` além de montar o dossiê por `_dossie_emenda`; não mexer no verbo `tarefa` (a origem do achado e o aviso `B1` são da `RAF-T30`); não editar a doutrina do modelador nem a do consultor (`RAF-T26`).
- **Contingências:**
  - se um teste que já existia em `tests/test_encerrar.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se `python .claude/tools/modelo.py check --help` não listar `--so-vigente` → parar e sinalizar `blocked` razão `dependencia`, nomeando a `RAF-T19`.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_marco_promove_versao_aceita_e_reescreve_os_cards` — `--marco 2 --resultado go --veredito "Aceito a versão 2" --aceita-versao 2 --consultor "valido a versão 2"`: sai 0; o stdout tem `marco: versão 2 promovida — 2 card(s) com a operação reescrita` e não tem `Ato: emenda`; o plano não tem `## 1A.` e tem `versão 2 · 2026-09-21 · autor: modelador · 2 operações · 3 propriedades · situação: vigente`, `| 1 | 2026-09-10 | obsoleta | modelador; Caiu pelo aceite da versão 2 em 2026-09-26 |` e `| 2 | 2026-09-21 | vigente | modelador, emenda |`; o card `MRC-T1` tem, seguidas, as linhas do campo com `OP-2`, `  - OP-2: Primeira operação da fixture.` e `  - precisa de: esboço — um esboço revisado`, e o `MRC-T2` as do campo com `OP-1`, `  - OP-1: Operação nova, inserida antes.` e `  - precisa de: insumo — um registro por rodada` (hoje sai 1: `--consultor` não existe; sem ele, o comando grava só o veredito e imprime o dossiê). TF `test_tf_marco_promove_versao_conflito_imprime_dossie` — `--aceita-versao 3`: sai 1, stderr com `marco: conflito na promoção da versão 3 — a ## 1A é a versão 2`, stdout com `Ato: emenda`, plano byte a byte igual. TR `test_tr_marco_promove_versao_recusa_pendente_com_violacao` — `tarefas_op1=""`: sai 1 com `marco: versão pendente com violação — 1A: V1 OP-1 — operação sem tarefa`, plano igual. TF `test_tf_marco_validacao_do_consultor_na_celula` — `--consultor "valido a versão 2 | sem ressalva"`: a linha do marco fica `| **Marco 2** | a etapa A | go · 2026-09-26 — "Aceito" · consultor: "valido a versão 2 \| sem ressalva" |`. TR `test_tr_marco_validacao_do_consultor_obrigatoria_no_aceite` — `--aceita-versao 2` sem `--consultor`: sai 1 com `marco: --aceita-versao exige --consultor com a linha de validação do consultor`, plano igual (a regra concorrente, consultor opcional, promoveria). Suíte `tests/test_encerrar.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_encerrar.py -q -k promove_versao` → `exit 0` — antes `exit 5`, depois `exit 0`
  2. `python -m pytest tests/test_encerrar.py -q -k validacao_do_consultor` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - fechamento.promoção da versão aceita — o próprio comando do marco promove a versão aceita, registra a anterior como obsoleta e acerta o texto da operação em cada card; havendo conflito, recusa e prepara o pedido ao modelador — Verificação 1
  - fechamento.validação do consultor — o aceite exige a linha de validação do consultor, gravada ao lado do veredito do dono — Verificação 2
- **Fora do escopo desta tarefa:** a doutrina da promoção no modelador e a forma da linha de validação no consultor (`RAF-T26`); o card da operação nova na rodada (`RAF-T25`); a origem do achado e o aviso de falha de instrumento no fechamento de tarefa (`RAF-T30`).
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** encerrar.py marco: promove a versão aceita (pendente vira vigente, anterior obsoleta, campo Operação do modelo dos cards reescrito — DRF-38) e cobra a validação do consultor antes (ver RDO RAF-T23)
  - **Contrato:** o comando do marco não promove versão sem a validação do consultor registrada
  - **Não refazer:** a promoção e a cobrança da validação, com os testes
  - **Pendente:** nenhum

### RAF-T23a — O comando do marco reconhece a versão pendente pela mesma regra do modelo.py [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa faz o comando do marco reconhecer a `## 1A` pela mesma regra que o `modelo.py` usa, recusando com a mensagem de erro do marco o cabeçalho que ele não lê, em vez de cair em exceção não tratada.
- **Fundamento:** `DRF-62`; `AE-176` (laudo da `RAF-T23`, ressalva 91: a pré-checagem de `gravar_marco` aceita a `## 1A` por prefixo, com `_MARCO_VERSAO_PENDENTE_RE`, e o `_checar_promocao` a lê por igualdade exata, com `_modelo._HEADING_PENDENTE` via `_localizar_secao`; o cabeçalho com texto a mais passa a pré-checagem e derruba `_checar_promocao` em `AttributeError`). Medido pelo consultor em cópia (2026-09-29): com o teste abaixo e sem a regra, o teste sai `1 failed` com `AttributeError: 'NoneType' object has no attribute 'versao'`; com a regra, `1 passed`, e `tests/test_encerrar.py` inteiro `43 passed`.
- **Depende de:** `RAF-T23`
- **Operação do modelo:** `OP-23`
  - OP-23: Quem executa faz o fechamento do marco promover sozinho a versão aceita, cobrando a linha de validação do consultor e acertando o texto da operação em cada card.
  - precisa de: conferência do modelo — Quem implementa acrescenta à conferência o que cada operação pede e mantém o que ela já julga quando chamada como hoje, com uma só mudança: enquanto houver versão pendente, o card que cita uma operação que só ela tem deixa de ser recusado.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/encerrar.py`, verbo `marco` (`gravar_marco`); só biblioteca padrão. A regra que fica é a do `modelo.py` (`_localizar_secao`: linha igual a `_HEADING_PENDENTE`), que o `check`, o `show` e a promoção já usam; a pré-checagem de `gravar_marco` passa a usá-la, e a regra do prefixo sai do arquivo. Vale para `--aceita-versao` e para `--recusa-versao`: a `## 1A` que o `modelo.py` não lê não é versão pendente para o marco.
- **Arquivos-alvo:**
  - `.claude/tools/encerrar.py`
  - `tests/test_encerrar.py`
- **Contratos/classes:** assinaturas inalteradas. Duas regras em `.claude/tools/encerrar.py`:
  1. A linha da constante `_MARCO_VERSAO_PENDENTE_RE = re.compile(...)` sai (seu único uso é o da regra 2).
  2. `gravar_marco`, a checagem `if (aceita_versao is not None or recusa_versao is not None) and not any(...)`: o gerador `_MARCO_VERSAO_PENDENTE_RE.match(l) for l in linhas` passa a `l == _modelo._HEADING_PENDENTE for l in linhas`; logo acima do `if`, um comentário de três linhas no máximo diz que a `## 1A` se reconhece pela mesma regra do `modelo.py` (igualdade exata com `_HEADING_PENDENTE`) e cita `AE-176` e `RAF-T23a` do `P-0755`. A mensagem `plano sem versão pendente (## 1A)` não muda.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_encerrar.py` o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card e começa na coluna 0; duas linhas vazias antes do `def`).

     ```python
     def test_tf_marco_cabecalho_1a_com_texto_a_mais_recusa_sem_pendente(tmp_path, capsys):
         """TF (RAF-T23a, `AE-176`): a `## 1A` cujo cabeçalho tem texto a mais não é a versão pendente
         que o `modelo.py` lê (igualdade exata com `_modelo._HEADING_PENDENTE`); a pré-checagem do
         marco usa a mesma regra e recusa antes de escrever, em vez de passar pelo prefixo e cair em
         `AttributeError` dentro de `_checar_promocao`."""
         texto = PLANO_MARCO_PROMOCAO.replace("@TAREFAS_OP1@", "MRC-T2").replace(
             "## 1A. Modelo conceitual — versão pendente de validação",
             "## 1A. Modelo conceitual — versão pendente de validação (rascunho)",
         )
         repo = _montar_repo_marco(tmp_path, texto)
         plano = repo / "docs" / "plans" / "P-0001-marco.md"
         antes = plano.read_text(encoding="utf-8")

         exit_code = encerrar.main(_argv_marco(
             repo, **{
                 "--marco": "2", "--resultado": "go", "--veredito": "Aceito a versão 2",
                 "--aceita-versao": "2", "--consultor": "valido a versão 2",
             },
         ))

         assert exit_code == 1
         assert "marco: plano sem versão pendente (## 1A)" in capsys.readouterr().err
         assert plano.read_text(encoding="utf-8") == antes
     ```
  2. Rodar `python -m pytest tests/test_encerrar.py -q -k cabecalho_1a` e conferir que o teste falha com `AttributeError`.
  3. Aplicar as duas regras de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma o teste novo (referência datada: `601 passed`, 2026-09-29, revisão da `RAF-T23`). Os testes de `marco` que já existem, inclusive `test_tf_marco_recusa_versao_imprime_dossie_de_emenda` e os cinco da `RAF-T23`, continuam passando sem mudança.
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - `grep -c _MARCO_VERSAO_PENDENTE_RE .claude/tools/encerrar.py` sai `0` ao fim.
  - Nenhuma linha que já existia em `tests/test_encerrar.py` sai ou muda: o card só acrescenta ao fim do arquivo.
  - Os testes gravam só em `tmp_path`.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `_checar_promocao`, `promover_versao` nem `_dossie_emenda`; não mudar `_HEADING_PENDENTE` nem nada do `.claude/tools/modelo.py`; não mudar a mensagem `plano sem versão pendente (## 1A)`; não mexer nos testes que já existem.
- **Contingências:**
  - se o teste novo não falhar no Passo 2 → parar e sinalizar `blocked` razão `premissa`, com a saída do teste (a pré-checagem não está como o card a descreve).
  - se um teste que já existia em `tests/test_encerrar.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_marco_cabecalho_1a_com_texto_a_mais_recusa_sem_pendente` — plano da promoção com o cabeçalho da `## 1A` seguido de ` (rascunho)`, `--aceita-versao 2 --consultor "valido a versão 2"`: sai 1 com `marco: plano sem versão pendente (## 1A)` no stderr e o plano byte a byte igual (a regra concorrente, o prefixo, deixa passar e derruba `_checar_promocao` em `AttributeError`). Suíte `tests/test_encerrar.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_encerrar.py -q -k cabecalho_1a` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - fechamento.promoção da versão aceita — havendo conflito, o comando do marco recusa antes de escrever; a `## 1A` que o `modelo.py` não lê sai com a mensagem de erro do marco, não com exceção não tratada — Verificação 1
- **Fora do escopo desta tarefa:** a promoção e a cobrança do consultor (`RAF-T23`, entregues); a doutrina da promoção (`RAF-T26`); o verbo `tarefa` (`RAF-T30`).
- **Handover:** 2026-09-29 · para `RAF-T30`
  - **Entregue:** encerrar.py: pré-checagem de gravar_marco reconhece a ## 1A por igualdade com _modelo._HEADING_PENDENTE (constante _MARCO_VERSAO_PENDENTE_RE removida); 1 teste novo
  - **Contrato:** cabeçalho de 1A com texto a mais sai 'marco: plano sem versão pendente (## 1A)', exit 1, plano intacto
  - **Não refazer:** a regra única do cabeçalho e o teste
  - **Pendente:** nenhum

### RAF-T23b — O dossiê do comando do marco pede ao modelador o que ele de fato devolve, no conflito e na recusa [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa faz o campo `Devolver` do dossiê `Ato: emenda` que o comando do marco imprime pedir ao modelador, no conflito da promoção, a `## 1` e a `## 1A` acertadas para o comando rodar de novo, e, na recusa da versão, a `## 1` sem a linha da versão recusada e o plano sem a `## 1A`.
- **Fundamento:** `DRF-64`; `AE-180` (laudo da `RAF-T26`, ressalva 90: o dossiê de conflito que `_dossie_emenda` monta pede "a seção ## 1 depois do ato e a linha nova do registro de versões", que é o que o próprio comando faz na promoção, e não o que o modelador acerta no conflito). O mesmo texto serve hoje à recusa, onde a `## 1A` e a linha dela saem e nenhuma linha nova entra no registro (`GOVERNANCA.md` §3.2; ato **Emenda** do modelador). Medido pelo consultor em cópia (2026-09-29): árvore real `-k devolver` `exit 5`; com os dois testes abaixo e sem a regra, `2 failed`; com a regra, `2 passed`, e `tests/test_encerrar.py` inteiro `45 passed`.
- **Depende de:** `RAF-T23a`
- **Operação do modelo:** `OP-23`
  - OP-23: Quem executa faz o fechamento do marco promover sozinho a versão aceita, cobrando a linha de validação do consultor e acertando o texto da operação em cada card.
  - precisa de: conferência do modelo — Quem implementa acrescenta à conferência o que cada operação pede e mantém o que ela já julga quando chamada como hoje, com uma só mudança: enquanto houver versão pendente, o card que cita uma operação que só ela tem deixa de ser recusado.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/encerrar.py`, verbo `marco`; só biblioteca padrão. `_dossie_emenda` é chamada em dois lugares, o `_conflito` de `_checar_promocao` e o fim de `gravar_marco` no ramo `--recusa-versao`, e hoje fixa o mesmo `Devolver` para os dois; o texto passa a vir de quem chama. As linhas `Plano`, `Ato`, `Motivo`, `Fato novo` e `Restrição` não mudam, nem as razões de conflito, nem a ordem das checagens.
- **Arquivos-alvo:**
  - `.claude/tools/encerrar.py`
  - `tests/test_encerrar.py`
- **Contratos/classes:** Três regras em `.claude/tools/encerrar.py`:
  1. `_dossie_emenda` ganha o parâmetro posicional `devolver: str`, depois de `restricao` (um parâmetro por linha na assinatura); a linha fixa `"Devolver: a seção ## 1 depois do ato e a linha nova do registro de versões.",` passa a `f"Devolver: {devolver}",`; o docstring acrescenta que o `Devolver` difere entre a recusa da versão e o conflito na promoção e cita `RAF-T23b`.
  2. O `_conflito` de `_checar_promocao` passa a `_dossie_emenda`, depois de `restricao`, o texto `"a ## 1 e a ## 1A acertadas, com o registro de versões, para o comando do marco rodar de novo."`
  3. O ramo `--recusa-versao` de `gravar_marco` passa a `_dossie_emenda`, depois de `restricao`, o texto `"a seção ## 1 depois do ato, com o registro de versões sem a linha da versão recusada, e o plano sem a ## 1A."`
- **Passos:**
  1. Acrescentar ao fim de `tests/test_encerrar.py` o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card e começa na coluna 0; duas linhas vazias antes de cada `def`).

     ```python
     def test_tf_marco_conflito_devolver_pede_a_1_e_a_1a(tmp_path, capsys):
         """TF (RAF-T23b, `AE-180`): no conflito da promoção o modelador acerta o que está (a
         `## 1`, a `## 1A` e o registro de versões) para o comando rodar de novo; o `Devolver` do
         dossiê não pede a seção depois do ato nem linha nova do registro, que o comando faz."""
         repo = _montar_repo_promocao(tmp_path)

         exit_code = encerrar.main(_argv_marco(
             repo, **{
                 "--marco": "2", "--resultado": "go", "--veredito": "Aceito a versão 3",
                 "--aceita-versao": "3", "--consultor": "valido a versão 3",
             },
         ))

         assert exit_code == 1
         saida = capsys.readouterr().out
         assert (
             "Devolver: a ## 1 e a ## 1A acertadas, com o registro de versões, para o comando do "
             "marco rodar de novo." in saida
         )
         assert "linha nova do registro" not in saida


     def test_tf_marco_recusa_devolver_sem_linha_nova_do_registro(tmp_path, capsys):
         """TF (RAF-T23b, `AE-180`): na recusa a `## 1A` e a linha dela saem e a vigente fica sem
         marca (`GOVERNANCA.md` §3.2); o `Devolver` do dossiê pede a `## 1` com o registro sem a linha
         da versão recusada, não uma linha nova."""
         repo = _montar_repo_marco(tmp_path)

         exit_code = encerrar.main(_argv_marco(
             repo, **{
                 "--marco": "1", "--resultado": "no-go", "--veredito": "Não aceito",
                 "--recusa-versao": "2",
             },
         ))

         assert exit_code == 0
         saida = capsys.readouterr().out
         assert (
             "Devolver: a seção ## 1 depois do ato, com o registro de versões sem a linha da versão "
             "recusada, e o plano sem a ## 1A." in saida
         )
         assert "linha nova do registro" not in saida
     ```
  2. Rodar `python -m pytest tests/test_encerrar.py -q -k devolver` e conferir que os dois testes falham.
  3. Aplicar as três regras de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os dois testes novos (referência datada: `602 passed`, 2026-09-29, revisão da `RAF-T26`). Os testes de `marco` que já existem, inclusive `test_tf_marco_recusa_versao_imprime_dossie_de_emenda` e `test_tf_marco_promove_versao_conflito_imprime_dossie`, continuam passando sem mudança.
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Nenhuma linha que já existia em `tests/test_encerrar.py` sai ou muda: o card só acrescenta ao fim do arquivo.
  - Os testes gravam só em `tmp_path`.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar as razões de conflito nem a ordem das checagens de `_checar_promocao`; não mudar `promover_versao` nem as linhas `Plano`, `Ato`, `Motivo`, `Fato novo` e `Restrição` do dossiê; não editar a doutrina do modelador (é da `RAF-T26a`); não mexer nos testes que já existem.
- **Contingências:**
  - se os testes novos não falharem os dois no Passo 2 → parar e sinalizar `blocked` razão `premissa`, com a saída do teste (o dossiê não está como o card o descreve).
  - se um teste que já existia em `tests/test_encerrar.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_marco_conflito_devolver_pede_a_1_e_a_1a` — plano da promoção com a `## 1A` na versão 2 e `--aceita-versao 3 --consultor "valido a versão 3"`: sai 1 e o stdout traz o `Devolver` do conflito, sem `linha nova do registro`. TF `test_tf_marco_recusa_devolver_sem_linha_nova_do_registro` — plano do marco com `--resultado no-go --recusa-versao 2`: sai 0 e o stdout traz o `Devolver` da recusa, sem `linha nova do registro`. Suíte `tests/test_encerrar.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_encerrar.py -q -k devolver` → `exit 0` — antes `exit 5`, depois `exit 0`
  2. `python -c "from pathlib import Path;t=Path('.claude/tools/encerrar.py').read_text(encoding='utf-8');print('devolver=%d-%d'%(t.count('linha nova do registro'),t.count('rodar de novo')))"` → `devolver=0-1` — antes `devolver=1-0`, depois `devolver=0-1`
- **Pronto quando:**
  - fechamento.promoção da versão aceita — havendo conflito, o comando do marco recusa e prepara o pedido ao modelador com o que o modelador acerta: a `## 1` e a `## 1A`, com o registro de versões, para o comando rodar de novo — Verificação 1, Verificação 2
- **Fora do escopo desta tarefa:** a doutrina do modelador sobre o conflito na promoção (`RAF-T26a`); o verbo `tarefa` (`RAF-T30`).
- **Handover:** 2026-09-29 · para `RAF-T26a`
  - **Entregue:** encerrar.py: _dossie_emenda ganhou o parâmetro devolver; o conflito pede a ## 1 e a ## 1A acertadas com o registro para o marco rodar de novo, e a recusa pede a ## 1 depois do ato sem a linha da versão recusada e sem a ## 1A; 2 testes novos
  - **Contrato:** o dossiê do comando do marco pede ao modelador o que ele devolve em cada ramo
  - **Não refazer:** o parâmetro devolver e os testes
  - **Pendente:** nenhum

### RAF-T24 — Quem conduz segue a janela quando o modelador cria operação nova e enfileira a rodada [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa ensina o gerente do loop a seguir a janela quando o modelador cria operação nova, enfileirando a rodada de replanejamento.
- **Fundamento:** `DRF-1`, `DRF-14`; `F-19`, `F-21` (a rota `modelador` segue sem parar a janela, mas a emenda que cria operação sem card recusava o despacho seguinte); relatório `R-04` (auditoria reg. 31 e 32).
- **Depende de:** `RAF-T20`
- **Operação do modelo:** `OP-24`
  - OP-24: Quem executa ensina o gerente do loop a seguir a janela quando o modelador cria operação nova, enfileirando a rodada de replanejamento.
  - precisa de: escolhas do dono sobre o roteiro — Ninguém altera: fixam a rota das operações que dependem delas.; conferência do modelo — Quem implementa acrescenta à conferência o que cada operação pede e mantém o que ela já julga quando chamada como hoje, com uma só mudança: enquanto houver versão pendente, o card que cita uma operação que só ela tem deixa de ser recusado.; despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.
- **Camada e fronteira:** doutrina do kit — a skill `scrum-master`, Passo 8 (*Roteamento, bloco A*), bullet `- **Triagem:**`, trecho da `rota=modelador`; nenhum código muda. O comportamento que a doutrina descreve já está nos instrumentos: o `despachar` roda `modelo.py check --so-vigente` desde a `RAF-T20` (a `## 1A` não recusa o despacho), o `check` completo acusa a operação nova sem card como `1A: V1 OP-<n> — operação sem tarefa` e o `encerrar.py marco --aceita-versao` cobra a `## 1A` sem violação desde a `RAF-T23`. Quem escreve o card da operação nova é o planejador, na rodada (`RAF-T25`). A regra mora só neste trecho da skill; nenhum outro arquivo a repete. O contrato do objeto é: "Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só."
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
- **Passos:**
  1. No `### Passo 8 — Roteamento, bloco A`, no bullet que começa por `- **Triagem:**` (uma linha só no arquivo), trocar o trecho antigo pelo novo, sem quebra nova e sem refluxo: o trecho fica na mesma linha.

     Trecho antigo:

     ```text
     e com a recusa o caso volta ao consultor para resolver preservando o modelo;
     ```

     Trecho novo:

     ```text
     e com a recusa o caso volta ao consultor para resolver preservando o modelo; quando, depois do modelador, `python .claude/tools/modelo.py check --plano <plano>` (sem `--so-vigente`) acusar `1A: V1 OP-<n> — operação sem tarefa`, a emenda criou operação nova, e o loop despacha em seguida o `pantonic-planner` para a rodada de replanejamento, que escreve o card dessa operação `blocked` até o aceite da versão no marco — a janela segue com as tarefas da versão vigente, porque o `despachar` julga só a `## 1` (`modelo.py check --so-vigente`) e a `## 1A` é cobrada no marco (`encerrar.py marco --aceita-versao`, `R-04` da auditoria final, `P-0755`);
     ```
  2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_progresso_hook.py` lê esta skill (tabela do repertório `M-0`..`M-18`), que o passo não toca.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer nas outras rotas do bullet `- **Triagem:**` nem na seção `### O que obriga parada e o que segue com registro`; não mexer nas regras `A3a`..`B1` das tabelas; não editar `.claude/agents/pantonic-planner.md` (o card da operação nova é da `RAF-T25`) nem `.claude/agents/pantonic-consultant.md`.
- **Contingências:**
  - se o trecho antigo não existir verbatim, uma única vez, em `.claude/skills/scrum-master/SKILL.md` → parar e sinalizar `blocked` razão `premissa`, colando o bullet `- **Triagem:**`.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_progresso_hook.py` lê a skill.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('rodada=%d'%t.count('o loop despacha em seguida o '))"` → `rodada=1` — antes `rodada=0`, depois `rodada=1`
- **Pronto quando:**
  - gerente do loop.rota do modelador com operação nova — o loop despacha o modelador e em seguida o planejador para a rodada, e a janela segue com as tarefas da versão vigente — Verificação 1
- **Fora do escopo desta tarefa:** o `--so-vigente` e o despacho que o usa (`RAF-T19`, `RAF-T20`); o card da operação nova, escrito pelo planejador (`RAF-T25`); a promoção no marco (`RAF-T23`).
- **Handover:** 2026-09-29 · para `RAF-T25`
  - **Entregue:** .claude/skills/scrum-master/SKILL.md: rota modelador com operação nova segue a janela e enfileira a rodada de replanejamento (R-04)
  - **Contrato:** quem conduz não para a janela quando o modelador cria operação nova; a rodada vira a próxima tarefa
  - **Não refazer:** o trecho da skill
  - **Pendente:** nenhum

### RAF-T24a — Quem conduz dá destino, no marco, ao card da operação nova que a rodada deixou bloqueado [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa completa, no trecho da rota `modelador` com operação nova da skill `scrum-master`, o destino do card que a rodada registrou `blocked` até o marco: `ready` no aceite da versão, fora do plano na recusa.
- **Fundamento:** `DRF-63`, `DRF-14`; `AE-178` (laudo da `RAF-T25`: a regra entregue registra o card da operação nova `blocked`, razão `dependencia`, nota `aguarda o aceite da versão <k> no marco`, e nenhum instrumento nem doutrina o tira de `blocked` no aceite; na recusa, o card fica sem destino nomeado); relatório `R-04` (auditoria reg. 31 e 32).
- **Depende de:** `RAF-T24`
- **Operação do modelo:** `OP-24`
  - OP-24: Quem executa ensina o gerente do loop a seguir a janela quando o modelador cria operação nova, enfileirando a rodada de replanejamento.
  - precisa de: escolhas do dono sobre o roteiro — Ninguém altera: fixam a rota das operações que dependem delas.; conferência do modelo — Quem implementa acrescenta à conferência o que cada operação pede e mantém o que ela já julga quando chamada como hoje, com uma só mudança: enquanto houver versão pendente, o card que cita uma operação que só ela tem deixa de ser recusado.; despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.
- **Camada e fronteira:** doutrina do kit — a skill `scrum-master`, Passo 8 (*Roteamento, bloco A*), bullet `- **Triagem:**`, o trecho da `rota=modelador` com operação nova que a `RAF-T24` escreveu; nenhum código muda. O comportamento que a doutrina descreve já está nos instrumentos: `encerrar.py marco --aceita-versao <k>` promove a `## 1A` e reescreve o campo `Operação do modelo` dos cards, sem tocar o `estado.tsv` das tarefas (`gravar_marco` só transita a linha do plano, no Marco 1 `go`); `backlog.py status <ID> ready` tira de `blocked` uma tarefa (medido na condução, Marcos 2 e 3, `RAF-T7` e `RAF-T19`); o `modelo.py check`, com ou sem `--so-vigente`, acusa `V4` o card que cita operação que não está na vigente nem na pendente, sem olhar o status do card (`validar`, lido no código), e por isso o card da operação recusada não fica no plano nem como `cancelled`. A regra mora só neste trecho da skill; o parágrafo `**Card da operação nova**` do planejador (`RAF-T25`) não a repete. O contrato do objeto é: "Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só."
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
- **Passos:**
  1. No `### Passo 8 — Roteamento, bloco A`, no bullet que começa por `- **Triagem:**` (uma linha só no arquivo), trocar o trecho antigo pelo novo, sem quebra nova e sem refluxo: o trecho fica na mesma linha.

     Trecho antigo:

     ```text
     e a `## 1A` é cobrada no marco (`encerrar.py marco --aceita-versao`, `R-04` da auditoria final, `P-0755`);
     ```

     Trecho novo:

     ```text
     e a `## 1A` é cobrada no marco (`encerrar.py marco --aceita-versao`, `R-04` da auditoria final, `P-0755`); gravado o marco, quem conduz dá destino a esse card, que o `encerrar.py marco` não tira de `blocked`: com `--aceita-versao <k>`, todo card `blocked` com a nota `aguarda o aceite da versão <k> no marco` passa a `ready` (`python .claude/tools/backlog.py status <ID> ready`); com `--recusa-versao <k>`, o consultor, a quem o caso volta, tira o card do plano junto com a linha dele no `estado.tsv`, porque a operação que ele materializa saiu com a versão recusada e o `modelo.py check` o acusaria `V4` (`AE-178` do `P-0755`);
     ```
  2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_progresso_hook.py` lê esta skill (tabela do repertório `M-0`..`M-18`), que o passo não toca.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - A skill fica em LF: nenhum retorno de carro (CR) no arquivo ao fim (`cr=0` na Verificação 1).
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer nas outras rotas do bullet `- **Triagem:**` nem no resto do trecho da `RAF-T24`; não mexer na seção `### O que obriga parada e o que segue com registro` nem nas regras `A3a`..`B1` das tabelas; não editar `.claude/agents/pantonic-planner.md` nem `.claude/tools/encerrar.py`.
- **Contingências:**
  - se o trecho antigo não existir verbatim, uma única vez, em `.claude/skills/scrum-master/SKILL.md` → parar e sinalizar `blocked` razão `premissa`, colando o bullet `- **Triagem:**`.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_progresso_hook.py` lê a skill.
- **Verificação:**
  1. `python -c "from pathlib import Path;b=Path('.claude/skills/scrum-master/SKILL.md').read_bytes();t=b.decode('utf-8');print('destino=%d-%d cr=%d'%(t.count('quem conduz dá destino a esse card'),t.count('tira o card do plano junto com a linha dele'),b.count(bytes([13]))))"` → `destino=1-1 cr=0` — antes `destino=0-0 cr=0`, depois `destino=1-1 cr=0`
- **Pronto quando:**
  - gerente do loop.rota do modelador com operação nova — o loop despacha o modelador e em seguida o planejador para a rodada, e a janela segue com as tarefas da versão vigente — Verificação 1
- **Fora do escopo desta tarefa:** o trecho da rota do modelador com operação nova (`RAF-T24`, feito); o card da operação nova, escrito pelo planejador (`RAF-T25`, feito); a promoção no marco (`RAF-T23`); a saída automática de `blocked` pelo `encerrar.py marco`, na aceitação e no gate de etapa (`DRF-63`, rota auditoria final).
- **Handover:** 2026-09-29 · para `RAF-T27`
  - **Entregue:** .claude/skills/scrum-master/SKILL.md Passo 8, Triagem: no aceite da versão k, todo card blocked com a nota 'aguarda o aceite da versão <k> no marco' vai a ready; na recusa, o caso volta ao consultor, que tira o card do plano e do estado.tsv
  - **Contrato:** o card da operação nova tem destino nomeado no aceite e na recusa do marco
  - **Não refazer:** a troca do trecho da skill
  - **Pendente:** nenhum

### RAF-T25 — O planejador escreve, na rodada que segue a emenda, o card da operação nova bloqueado até o marco [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa ensina o planejador a escrever, na rodada que segue a emenda, o card da operação nova bloqueado até o aceite da versão no marco.
- **Fundamento:** `DRF-1`, `DRF-14`; `F-21` (nada diz quem escreve o card da operação que a emenda cria no meio do loop); relatório `R-04` (auditoria reg. 31 e 32).
- **Depende de:** `RAF-T19`
- **Operação do modelo:** `OP-25`
  - OP-25: Quem executa ensina o planejador a escrever, na rodada que segue a emenda, o card da operação nova bloqueado até o aceite da versão no marco.
  - precisa de: escolhas do dono sobre o roteiro — Ninguém altera: fixam a rota das operações que dependem delas.; planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão.; conferência do modelo — Quem implementa acrescenta à conferência o que cada operação pede e mantém o que ela já julga quando chamada como hoje, com uma só mudança: enquanto houver versão pendente, o card que cita uma operação que só ela tem deixa de ser recusado.
- **Camada e fronteira:** doutrina do kit — a definição do agente planejador, `.claude/agents/pantonic-planner.md`, seção `## Rodada de replanejamento`, passo 4 (*Reescrever os cards*); nenhum código muda. O mecanismo que a regra usa já existe: o `modelo.py check` sem `--so-vigente` acusa a operação nova sem card como `1A: V1 OP-<n> — operação sem tarefa`; com `--so-vigente`, que o despacho usa, a `## 1A` não recusa nada, e o card que cita operação que só existe na `## 1A` não é `V4` (`RAF-T19`); a promoção do marco reescreve o campo `Operação do modelo` dos cards das listas `tarefas:` (`RAF-T23`). A regra mora só no passo 4 da rodada; nenhum outro arquivo a repete. O contrato do objeto é: "Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão."
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md`
- **Passos:**
  1. Em `.claude/agents/pantonic-planner.md`, na seção `## Rodada de replanejamento`, logo depois da última linha do parágrafo que começa por `   **Versão pendente reconfere a restrição que cita o estado do plano:**` e antes da linha que começa por `5. **Fechar o estado**`, inserir uma linha vazia e o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card, e os três espaços que sobram no começo de cada linha entram no arquivo).

     ```text
        **Card da operação nova** (`R-04` da auditoria final, `P-0755`): na rodada que segue uma
        emenda que cria operação sem card — o `modelo.py check` sem `--so-vigente` acusa
        `1A: V1 OP-<n> — operação sem tarefa` —, o planejador escreve o card dessa operação, com o
        campo `Operação do modelo` copiado da `## 1A` e o id da convenção de lastro sobre o número
        da operação na `## 1A` (com sufixo `a`, `b`, … quando esse id já existe no plano); apensa o
        id à lista `tarefas:` da operação na `## 1A`; e registra o card em `estado.tsv` `blocked`,
        razão `dependencia`, nota `aguarda o aceite da versão <k> no marco`. A janela segue com as
        tarefas da vigente, e a promoção do marco reescreve o campo dos cards.
     ```
  2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_doutrina_unidade.py` lê este arquivo.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não reescrever outro parágrafo do passo 4 nem os demais passos da rodada; não mexer no item 14 da Fase 4 (`RAF-T17`, `RAF-T18`) nem no bloco `**Árvore do` da Fase 5 (`RAF-T16`); não editar a skill `scrum-master` (a rota do modelador com operação nova é da `RAF-T24`).
- **Contingências:**
  - se o parágrafo que começa por `   **Versão pendente reconfere a restrição que cita o estado do plano:**`, seguido da linha que começa por `5. **Fechar o estado**`, não existir em `.claude/agents/pantonic-planner.md` → parar e sinalizar `blocked` razão `premissa`, colando o passo 4 da rodada inteiro.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê o arquivo.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('nova=%d'%t.count('**Card da operação nova**'))"` → `nova=1` — antes `nova=0`, depois `nova=1`
- **Pronto quando:**
  - planejador.card da operação nova — na rodada que segue a emenda, o planejador escreve esse card e o registra bloqueado até o aceite da versão no marco — Verificação 1
- **Fora do escopo desta tarefa:** a rota do modelador no loop (`RAF-T24`); a promoção que reescreve os cards (`RAF-T23`); a régua de profundidade e o pedido ao modelador (`RAF-T36`, `RAF-T37`).
- **Handover:** 2026-09-29 · para `RAF-T26`
  - **Entregue:** .claude/agents/pantonic-planner.md: na rodada que segue a emenda, o planejador escreve o card da operação nova nascido blocked até o marco (R-04)
  - **Contrato:** operação nova criada por emenda ganha card na rodada seguinte, bloqueado até o aceite do dono no marco
  - **Não refazer:** o trecho do planejador
  - **Pendente:** nenhum

### RAF-T26 — O modelador sai da promoção de versão e o consultor ganha a forma da linha de validação [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa reescreve no modelador e no consultor a doutrina da promoção de versão, que passa ao comando do marco e só chama o modelador no conflito.
- **Fundamento:** `DRF-17`, `DRF-38`; `F-21` (a promoção da `## 1A` é hoje do modelador, `pantonic-model-designer.md`; a validação prévia do consultor está em `pantonic-consultant.md` sem forma de linha); relatório `R-08` (auditoria reg. 37 e 38).
- **Depende de:** `RAF-T23`
- **Operação do modelo:** `OP-26`
  - OP-26: Quem executa reescreve no modelador e no consultor a doutrina da promoção de versão, que passa ao comando do marco e só chama o modelador no conflito.
  - precisa de: fechamento — Quem implementa recebe o comando que hoje só grava o veredito do marco e confere achados por semelhança de texto, e acrescenta o que a operação pede.
- **Camada e fronteira:** doutrina do kit — as definições do agente modelador (`.claude/agents/pantonic-model-designer.md`, lista de atos, ato **Emenda**, parágrafo `**No marco**`) e do agente consultor (`.claude/agents/pantonic-consultant.md`, a frase da validação no marco); nenhum código muda. O comportamento que a doutrina descreve já está no comando desde a `RAF-T23`: `encerrar.py marco --aceita-versao <k> --consultor "<linha>"` exige a linha do consultor, grava-a na célula do marco ao lado do veredito do dono, promove a `## 1A` (registro de versões com a anterior `obsoleta` e a frase `Caiu pelo aceite da versão <k> em <data>`) e reescreve o campo `Operação do modelo` dos cards das listas `tarefas:`; em conflito (a `## 1A` com outra versão, registro sem vigente único ou sem a linha pendente da versão), recusa e imprime o dossiê `Ato: emenda` para o modelador. A regra da promoção mora só no modelador, e a forma da linha só no consultor. O contrato do objeto "fechamento" é: "Quem implementa recebe o comando que hoje só grava o veredito do marco e confere achados por semelhança de texto, e acrescenta o que a operação pede."
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-model-designer.md`
  - `.claude/agents/pantonic-consultant.md`
- **Passos:**
  1. Em `.claude/agents/pantonic-model-designer.md`, trocar as seis linhas do texto antigo pelas doze do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os dois espaços iniciais que já tem no arquivo).

     Texto antigo:

     ```text
       **No marco**, o desfecho da pendente chega em novo dossiê `Ato: emenda`, com a validação do
       consultor e o ato do dono em `Motivo`. Aceita: o conteúdo da `## 1A` passa à `## 1`, com o
       cabeçalho em `situação: vigente`; a `## 1A` sai do plano; no registro de versões a pendente passa
       a `vigente` e a anterior a `obsoleta`, com a frase `Caiu pelo aceite da versão <N> em <data>` —
       a linha fica, o conteúdo da obsoleta não. Recusada: a `## 1A` e a linha dela saem, e a vigente
       fica sem marca (`GOVERNANCA.md` §3.2, *Versão vigente, pendente e obsoleta*).
     ```

     Texto novo:

     ```text
       **No marco**, a versão aceita é promovida pelo comando do marco, não por você
       (`R-08` da auditoria final, `P-0755`): `encerrar.py marco --aceita-versao <k> --consultor
       "<linha>"` passa o conteúdo da `## 1A` à `## 1`, com o cabeçalho em `situação: vigente`; tira
       a `## 1A` do plano; no registro de versões põe a pendente em `vigente` e a anterior em
       `obsoleta`, com a frase `Caiu pelo aceite da versão <N> em <data>` — a linha fica, o conteúdo
       da obsoleta não —; e reescreve o campo `Operação do modelo` dos cards das listas `tarefas:`.
       Você só é chamado na promoção quando o comando encontra **conflito** (a `## 1A` com outra
       versão, registro de versões sem vigente único ou sem a linha pendente da versão): o comando
       imprime o dossiê `Ato: emenda`, e você devolve a `## 1A` e o registro acertados para o
       comando rodar de novo. Recusada: o desfecho chega em dossiê `Ato: emenda`, com o ato do dono
       em `Motivo`; a `## 1A` e a linha dela saem, e a vigente fica sem marca (`GOVERNANCA.md` §3.2,
       *Versão vigente, pendente e obsoleta*).
     ```
  2. Em `.claude/agents/pantonic-consultant.md`, trocar o trecho antigo pelo novo, na mesma linha, sem quebra nova e sem refluxo.

     Trecho antigo:

     ```text
     No marco, você valida a versão pendente do modelo antes do dono (`GOVERNANCA.md` §3.2).
     ```

     Trecho novo:

     ```text
     No marco, você valida a versão pendente do modelo antes do dono (`GOVERNANCA.md` §3.2), numa linha só, na forma `valido a versão <k>: <razão em uma frase>` ou `não valido a versão <k>: <razão em uma frase>`; só a primeira segue ao dono, e quem conduz a passa verbatim a `encerrar.py marco --aceita-versao <k> --consultor "<linha>"`, que a grava na célula do marco, ao lado do veredito do dono (`R-08` da auditoria final, `P-0755`).
     ```
  3. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_doutrina_unidade.py` lê `pantonic-model-designer.md`, e `tests/test_frontmatter_yaml.py` lê o frontmatter de `pantonic-consultant.md`, que o passo 2 não toca.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer nos atos **Autoria**, **Conflito** e **Leitura** do modelador nem no resto do ato **Emenda**; não editar `GOVERNANCA.md` (a ordem consultor → dono em §3.2 não muda); não mexer na triagem nem nas rotas do consultor; não acrescentar a origem do achado ao consultor (é da `RAF-T35`).
- **Contingências:**
  - se o texto antigo do passo 1 ou o trecho antigo do passo 2 não existir verbatim, uma única vez, no arquivo dele → parar e sinalizar `blocked` razão `premissa`, nomeando o passo.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` e `tests/test_frontmatter_yaml.py` leem os dois arquivos.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-model-designer.md').read_text(encoding='utf-8');print('promocao=%d-%d'%(t.count('o desfecho da pendente chega em novo dossiê'),t.count('Você só é chamado na promoção quando o comando encontra')))"` → `promocao=0-1` — antes `promocao=1-0`, depois `promocao=0-1`
  2. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-consultant.md').read_text(encoding='utf-8');print('validacao=%d'%t.count('numa linha só, na forma'))"` → `validacao=1` — antes `validacao=0`, depois `validacao=1`
- **Pronto quando:**
  - modelador.papel na promoção de versão — o modelador só é chamado quando o comando do marco encontra conflito — Verificação 1
  - consultor.forma da validação da versão pendente — a definição do consultor dá a forma da linha de validação que o comando do marco cobra — Verificação 2
- **Fora do escopo desta tarefa:** a promoção por comando e a cobrança da linha (`RAF-T23`); a origem citada no achado do consultor (`RAF-T35`).
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** .claude/agents/pantonic-model-designer.md sem a promoção de versão (agora do comando do marco); .claude/agents/pantonic-consultant.md com a forma da linha de validação da versão pendente (R-08)
  - **Contrato:** a promoção de versão é do encerrar.py marco; o consultor valida a pendente numa linha de forma fixa
  - **Não refazer:** as trocas nos dois agentes
  - **Pendente:** nenhum

### RAF-T26a — O modelador conhece os quatro conflitos da promoção e devolve o que o dossiê pede [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa acerta no modelador a frase do conflito na promoção de versão: os quatro conflitos que o comando do marco recusa e o que o modelador devolve, o mesmo que o campo `Devolver` do dossiê pede.
- **Fundamento:** `DRF-64`; `AE-180` (laudo da `RAF-T26`, ressalva 90: o texto que a `RAF-T26` fixou enumera três conflitos, e `_checar_promocao` de `.claude/tools/encerrar.py` tem um quarto que também imprime o dossiê, `o plano não tem a ## 1`; e diz que o modelador devolve "a `## 1A` e o registro acertados", enquanto o dossiê, depois da `RAF-T23b`, pede a `## 1` e a `## 1A` acertadas, com o registro de versões). Medido pelo consultor em cópia (2026-09-29): trecho antigo único no arquivo, LF (0 CR); Verificação 1 antes `conflito=1-0`, depois `conflito=0-1`; `tests/test_doutrina_unidade.py` `8 passed` depois.
- **Depende de:** `RAF-T26`, `RAF-T23b`
- **Operação do modelo:** `OP-26`
  - OP-26: Quem executa reescreve no modelador e no consultor a doutrina da promoção de versão, que passa ao comando do marco e só chama o modelador no conflito.
  - precisa de: fechamento — Quem implementa recebe o comando que hoje só grava o veredito do marco e confere achados por semelhança de texto, e acrescenta o que a operação pede.
- **Camada e fronteira:** doutrina do kit — a definição do agente modelador (`.claude/agents/pantonic-model-designer.md`, ato **Emenda**, parágrafo `**No marco**`, as seis últimas linhas); nenhum código muda. O comportamento descrito é o do comando depois da `RAF-T23b`: `_checar_promocao` recusa com o dossiê `Ato: emenda` quando o plano não tem a `## 1`, quando a `## 1A` é outra versão, quando o registro de versões não tem uma única linha vigente e quando não tem a linha pendente da versão; o `Devolver` do conflito pede `a ## 1 e a ## 1A acertadas, com o registro de versões, para o comando do marco rodar de novo.` O contrato do objeto "fechamento" é: "Quem implementa recebe o comando que hoje só grava o veredito do marco e confere achados por semelhança de texto, e acrescenta o que a operação pede."
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-model-designer.md`
- **Passos:**
  1. Em `.claude/agents/pantonic-model-designer.md`, trocar as seis linhas do texto antigo pelas seis do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os dois espaços iniciais que já tem no arquivo).

     Texto antigo:

     ```text
       Você só é chamado na promoção quando o comando encontra **conflito** (a `## 1A` com outra
       versão, registro de versões sem vigente único ou sem a linha pendente da versão): o comando
       imprime o dossiê `Ato: emenda`, e você devolve a `## 1A` e o registro acertados para o
       comando rodar de novo. Recusada: o desfecho chega em dossiê `Ato: emenda`, com o ato do dono
       em `Motivo`; a `## 1A` e a linha dela saem, e a vigente fica sem marca (`GOVERNANCA.md` §3.2,
       *Versão vigente, pendente e obsoleta*).
     ```

     Texto novo:

     ```text
       Você só é chamado na promoção quando o comando encontra **conflito** (o plano sem a `## 1`, a
       `## 1A` com outra versão, registro de versões sem vigente único ou sem a linha pendente da
       versão): o comando imprime o dossiê `Ato: emenda`, e você devolve a `## 1` e a `## 1A`
       acertadas, com o registro de versões, para o comando rodar de novo. Recusada: o desfecho chega
       em dossiê `Ato: emenda`, com o ato do dono em `Motivo`; a `## 1A` e a linha dela saem, e a
       vigente fica sem marca (`GOVERNANCA.md` §3.2, *Versão vigente, pendente e obsoleta*).
     ```
  2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `602 passed`, 2026-09-29, revisão da `RAF-T26`). `tests/test_doutrina_unidade.py` lê `pantonic-model-designer.md`.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - O arquivo fica em LF, sem CR.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer nas seis primeiras linhas do parágrafo `**No marco**`, nos atos **Autoria**, **Conflito** e **Leitura** nem no resto do ato **Emenda**; não editar `GOVERNANCA.md` nem `.claude/agents/pantonic-consultant.md`; não editar `.claude/tools/encerrar.py` (é da `RAF-T23b`).
- **Contingências:**
  - se o texto antigo do passo 1 não existir verbatim, uma única vez, no arquivo → parar e sinalizar `blocked` razão `premissa`.
  - se o sistema de permissão negar a edição do arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê o arquivo.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-model-designer.md').read_text(encoding='utf-8');print('conflito=%d-%d'%(t.count('e o registro acertados para o'),t.count('(o plano sem a ')))"` → `conflito=0-1` — antes `conflito=1-0`, depois `conflito=0-1`
- **Pronto quando:**
  - modelador.papel na promoção de versão — o modelador só é chamado quando o comando do marco encontra conflito, e a doutrina nomeia os quatro conflitos e o que ele devolve, o mesmo que o dossiê pede — Verificação 1
- **Fora do escopo desta tarefa:** o `Devolver` do dossiê no comando (`RAF-T23b`); a forma da linha de validação do consultor (`RAF-T26`, entregue).
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** .claude/agents/pantonic-model-designer.md, parágrafo No marco: nomeia os quatro conflitos de _checar_promocao (inclui 'o plano não tem a ## 1') e devolve o que o dossiê do marco pede em cada ramo
  - **Contrato:** a doutrina do modelador e o dossiê do encerrar.py marco pedem a mesma devolução
  - **Não refazer:** a troca do parágrafo
  - **Pendente:** nenhum

### RAF-T27 — O pré-voo separa o caminho a criar do que já devia existir e não toma extensão solta por caminho [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** Quem executa faz o pré-voo do pedido separar o caminho que o pedido manda criar do caminho que já devia existir, sem tomar extensão solta por caminho.
- **Fundamento:** `DRF-19`; `F-22` (nove extensões; `_e_caminho` = termina numa delas ou em `/`; sobre o pedido do plano fictício, seis linhas `não`, uma delas `.txt`, e o `c.bin` ausente, exit 1); relatório `R-17` (auditoria reg. 2).
- **Depende de:** `RAF-T24`, `RAF-T24a`, `RAF-T25`, `RAF-T26`, `RAF-T26a`
- **Operação do modelo:** `OP-27`
  - OP-27: Quem executa faz o pré-voo do pedido separar o caminho que o pedido manda criar do caminho que já devia existir, sem tomar extensão solta por caminho.
  - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/prevoo.py`, só biblioteca padrão, sem import de `tests` nem de `caminhos` (`tests/conformance/test_camadas_do_kit.py`). Primeira tarefa da etapa D: nasce `blocked` até o `go` do Marco 4 (`DRF-5`), e depende dos três cards que fecham a etapa C. A saída continua `citado | existe | onde`, uma linha por item; o valor novo da coluna `existe` é `criar`, que não derruba o exit 0. O pedido é do planejador, que roda o pré-voo na Fase 0. O contrato do objeto é: "Quem implementa muda só a leitura do que é caminho e a classificação do que falta, com os testes que a provam."
- **Arquivos-alvo:**
  - `.claude/tools/prevoo.py`
  - `tests/test_prevoo.py`
- **Contratos/classes:** `_e_caminho(token: str) -> bool` (regra nova) e função nova `_caminhos_a_criar(texto: str) -> set[str]`; `main` muda só no laço dos caminhos. Três regras:
  1. `_e_caminho`, com docstring que cita `R-17` e `DRF-19` do `P-0755`: verdadeiro quando o token termina em `/`; ou quando contém `/` e o último segmento (depois da última `/`) casa `\.[A-Za-z0-9]{1,5}$` (constante nova `_RE_EXTENSAO_CURTA`); ou quando não contém `/`, termina numa das nove `_EXTENSOES_CAMINHO` e não começa por `.`.
  2. `_caminhos_a_criar`: constantes novas `_VERBOS_DE_CRIACAO = {"crie", "criar", "grave", "gravar", "escreva", "escrever", "gere", "gerar"}` e `_RE_FIM_DE_FRASE` = regex de `. ` (ponto e espaço) ou quebra de linha; o texto se divide em frases por essa regex; em cada frase, os tokens separados por espaço em branco passam por `_normalizar`; depois do primeiro token cujo `lower()` é um dos verbos, todo token que é caminho por `_e_caminho` entra no conjunto.
  3. `main`, laço dos caminhos: caminho que existe sob a raiz sai `<caminho> | sim | <caminho>`; que não existe e está em `_caminhos_a_criar(args.texto)` sai `<caminho> | criar | —` e **não** muda o exit; que não existe e não está no conjunto sai `<caminho> | não | —` e faz o exit ser 1, como hoje. Símbolos e flags não mudam.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_prevoo.py` a constante `_PEDIDO_MEDIDO_R17` com o pedido do plano fictício, verbatim, em uma string só: `Crie em scratch_sonda/ duas coisas: (1) as amostras scratch_sonda/amostras/a.txt, scratch_sonda/amostras/b.txt e o binário scratch_sonda/amostras/c.bin; (2) o utilitário scratch_sonda/contar.py, que recebe caminhos de arquivo e imprime, por arquivo .txt, o número de linhas, recusando com mensagem o caminho que não existe, com os testes em tests/test_sonda_auditoria_final.py. Tudo só com biblioteca padrão.` — e os quatro testes da seção `Testes`, com `_load_prevoo` e `--root` em `tmp_path`.
  2. Rodar `python -m pytest tests/test_prevoo.py -q -k "conta_como_caminho or caminho_a_criar"` e conferir que os dois TF falham e os dois TR passam.
  3. Aplicar as três regras de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 4 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). Os seis testes que já existem em `tests/test_prevoo.py` continuam passando sem mudança.
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Nenhuma linha que já existia em `tests/test_prevoo.py` sai ou muda: o card só acrescenta ao fim do arquivo.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `_normalizar`, `_e_flag`, `_simbolo_de`, `_achar_simbolo` nem `_achar_flag`; não acrescentar extensão às nove de `_EXTENSOES_CAMINHO`; não mudar o cabeçalho `citado | existe | onde`; não editar a doutrina do planejador.
- **Contingências:**
  - se um teste que já existia em `tests/test_prevoo.py` ou em `tests/conformance/` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_prevoo_conta_como_caminho_sem_extensao_solta` — texto `leia, por arquivo .txt, o binário dados/c.bin`, raiz vazia: exit 1 e a saída exatamente `citado | existe | onde` e `dados/c.bin | não | —` (hoje: `.txt | não | —` e nenhuma linha de `dados/c.bin`). TR `test_tr_prevoo_conta_como_caminho_nome_solto_conhecido` — `notas.md` na raiz, texto `leia notas.md antes`: exit 0 e `notas.md | sim | notas.md` (a regra concorrente, exigir `/`, o perderia). TF `test_tf_prevoo_caminho_a_criar_no_pedido_medido` — `_PEDIDO_MEDIDO_R17`, raiz vazia: exit 0 e a saída exatamente o cabeçalho e as seis linhas `scratch_sonda/ | criar | —`, `scratch_sonda/amostras/a.txt | criar | —`, `scratch_sonda/amostras/b.txt | criar | —`, `scratch_sonda/amostras/c.bin | criar | —`, `scratch_sonda/contar.py | criar | —` e `tests/test_sonda_auditoria_final.py | criar | —`, nesta ordem (hoje: seis linhas `não` e exit 1). TR `test_tr_prevoo_caminho_a_criar_so_na_mesma_frase` — texto `Crie o módulo novo. Leia docs/x.md depois`: exit 1 e `docs/x.md | não | —` (a regra concorrente, verbo em qualquer ponto do texto, daria `criar`). Suíte `tests/test_prevoo.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_prevoo.py -q -k conta_como_caminho` → `exit 0` — antes `exit 5`, depois `exit 0`
  2. `python -m pytest tests/test_prevoo.py -q -k caminho_a_criar` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - pré-voo do pedido.o que conta como caminho — conta o que termina em barra, o que tem pasta e extensão curta, e o nome solto com uma das extensões conhecidas — Verificação 1
  - pré-voo do pedido.caminho a criar — ele sai como a criar, sem derrubar o resultado; o pedido medido passa com seis linhas a criar — Verificação 2
- **Fora do escopo desta tarefa:** a doutrina do planejador sobre o pré-voo (a Fase 0 já manda rodar e colar a tabela; a linha `criar` não volta ao dono porque não é premissa ausente).
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** .claude/tools/prevoo.py:60 (_e_caminho: extensão curta só com '/', nome solto só começando por '.'), :114-118 (_VERBOS_DE_CRIACAO, _caminhos_a_criar), :199-200 (coluna existe = criar); tests/test_prevoo.py com os TF/TR do card
  - **Contrato:** prevoo.py segue citado | existe | onde, uma linha por item; 'criar' não derruba o exit 0; só a biblioteca padrão
  - **Não refazer:** nada a declarar
  - **Pendente:** a docstring do módulo (prevoo.py:13-15) ainda descreve a regra antiga de caminho e só sim/nao (achado do laudo, ao consultor)

### RAF-T27a — O docstring do módulo do pré-voo diz o que conta como caminho e quando o caminho sai a criar [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa faz o docstring do módulo do pré-voo do pedido dizer as três regras que a `RAF-T27` entregou: o que conta como caminho, o valor `criar` pelo verbo na mesma frase e o exit que ele não derruba.
- **Fundamento:** `DRF-66`; `AE-183` (laudo da `RAF-T27`, ressalva 91); `DRF-19`; relatório `R-17`.
- **Depende de:** `RAF-T27`
- **Operação do modelo:** `OP-27`
  - OP-27: Quem executa faz o pré-voo do pedido separar o caminho que o pedido manda criar do caminho que já devia existir, sem tomar extensão solta por caminho.
  - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** texto do instrumento `.claude/tools/prevoo.py` — o item `caminhos` do docstring do módulo (linhas 13-15); nenhum comportamento muda. A `RAF-T27` trocou só o docstring de `_e_caminho` e escreveu o de `_caminhos_a_criar` (as regras do card nomearam só eles); o docstring do módulo seguiu dizendo que caminho é o token terminado numa das nove extensões ou em `/`, sem o valor `criar`.
- **Arquivos-alvo:**
  - `.claude/tools/prevoo.py`
- **Passos:**
  1. No docstring do módulo de `.claude/tools/prevoo.py`, trocar as três linhas do texto antigo pelas oito do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card, e os dois espaços que sobram no começo das linhas de continuação entram no arquivo).

     Texto antigo:

     ```text
     - **caminhos** — token terminado em `.py`, `.md`, `.ps1`, `.json`, `.tsv`, `.txt`, `.yml`, `.yaml`
       ou `.toml`, ou terminado em `/`; existe quando `(<root> / <token>)` existe; `onde` é o próprio
       caminho.
     ```

     Texto novo:

     ```text
     - **caminhos** — token terminado em `/`; ou com `/` e o último segmento terminado numa extensão
       de 1 a 5 letras ou dígitos; ou, sem `/`, terminado em `.py`, `.md`, `.ps1`, `.json`, `.tsv`,
       `.txt`, `.yml`, `.yaml` ou `.toml` e não começado por `.` (`R-17` e `DRF-19` do `P-0755`);
       existe (`sim`) quando `(<root> / <token>)` existe, e `onde` é o próprio caminho; o que não
       existe sai `criar` quando a mesma frase (texto entre `. ` ou quebra de linha) o traz depois de
       um verbo de criação (`crie`, `criar`, `grave`, `gravar`, `escreva`, `escrever`, `gere`, `gerar`,
       sem distinção de caixa), e `criar` não derruba o exit 0; o que não existe e o pedido não manda
       criar sai `não` e, como o símbolo e a flag ausentes, faz o exit ser 1.
     ```
  2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Em `.claude/tools/prevoo.py` só mudam as três linhas do texto antigo: nenhum código, nome, regex, constante nem outro docstring muda; o fim de linha do arquivo não muda (hoje CRLF na árvore; o git normaliza no `add`, `eol=lf`).
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar os docstrings de `_e_caminho` e de `_caminhos_a_criar` (a `RAF-T27` já os escreveu); não mudar os itens `símbolos` e `flags` nem o parágrafo da normalização; não tocar `tests/test_prevoo.py`.
- **Contingências:**
  - se o texto antigo do passo 1 não existir verbatim → parar e sinalizar `blocked` razão `premissa`, nomeando o passo.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo (nenhum teste lê o docstring do módulo); `tests/test_prevoo.py` e a suíte inteira.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/tools/prevoo.py').read_text(encoding='utf-8');print('docstring=%d-%d-%d linhas=%d'%(t.count('ou terminado em'),t.count('de 1 a 5 letras ou dígitos'),t.count('não derruba o exit 0'),len(t.splitlines())))"` → `docstring=0-1-1 linhas=227` — antes `docstring=1-0-0 linhas=222`, depois `docstring=0-1-1 linhas=227`
- **Pronto quando:**
  - pré-voo do pedido.o que conta como caminho — o docstring do módulo diz a barra final, a pasta com extensão curta e o nome solto com uma das nove extensões que não começa por ponto — Verificação 1
  - pré-voo do pedido.caminho a criar — o docstring do módulo diz o valor criar pelo verbo na mesma frase, que não derruba o exit 0 — Verificação 1
- **Fora do escopo desta tarefa:** o texto da `RAF-T27` (`done`), que fica como executado; a doutrina do planejador sobre o pré-voo.
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** .claude/tools/prevoo.py docstring do módulo, item caminhos: as três regras de caminho, o valor criar (verbo de criação antes, na mesma frase, sem derrubar o exit 0) e o nao que faz exit 1; fim de linha CRLF preservado
  - **Contrato:** o cabeçalho do prevoo.py descreve o comportamento entregue pela RAF-T27
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum

### RAF-T28 — O controle do backlog avisa, ao drenar, a diretiva que não cita nada vivo [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa faz o controle do backlog avisar, ao tirar um plano da fila, que a diretiva de priorização não cita nada vivo nem o plano que saiu.
- **Fundamento:** `DRF-20`; `F-23` (`DIRETIVA_RE`; `_parse_diretiva` lê os ids entre crases antes de ` — `; `transacionar_drain`, chamado pelas skills `passagem-de-bastao` e `diario-de-obras`); relatório `R-18` (auditoria reg. 16: a diretiva seguiu apontando o plano que já tinha saído).
- **Depende de:** `RAF-T27`
- **Operação do modelo:** `OP-28`
  - OP-28: Quem executa faz o controle do backlog avisar, ao tirar um plano da fila, que a diretiva de priorização não cita nada vivo nem o plano que saiu.
  - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/backlog.py`, função `transacionar_drain` (verbo `drain`); só biblioteca padrão. O aviso é só texto no stderr: o `drain` continua escrevendo o diário, o inbox e o histórico como hoje, com o mesmo exit e a mesma saída no stdout. A reescrita da diretiva continua ato de quem conduz (`backlog.py diretiva`). O contrato do objeto é: "Quem implementa acrescenta um aviso ao tirar o plano da fila e uma recusa ao conferir, sem mudar o resultado do primeiro."
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
- **Contratos/classes:** `transacionar_drain(repo: Path, modelo: Modelo, inbox_planos: Path, historico: Path, data: str | None = None) -> ResultadoStatus` — assinatura inalterada; função nova `_id_vivo(modelo: Modelo, id_: str) -> bool`, logo antes de `_localizar`. Duas regras:
  1. `_id_vivo`: `_localizar(modelo, id_)`; `None` → `False`; senão, vivo quando o primeiro termo do `status` (texto até o primeiro espaço) não é `done`, `cancelled` nem `superseded` (status vazio conta como vivo). Docstring cita `DRF-20` do `P-0755`.
  2. `transacionar_drain`, logo depois das três chamadas a `_escrever_atomico` e antes do cálculo de `arquivos`: quando o diário (as `diario_linhas` já com as linhas de índice novas) tem a linha da diretiva (`DIRETIVA_RE`) e nenhum id de `modelo.diretiva_ids` é vivo por `_id_vivo`, para cada plano drenado, na ordem do inbox, cujo id não está em `modelo.diretiva_ids`, imprime no stderr `drain: aviso — a diretiva de priorização não cita nenhum id vivo nem <P-id>`. Sem linha de diretiva, nenhum aviso. O comentário acima do bloco cita `R-18` e `DRF-20` do `P-0755`.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_backlog.py` o helper `_repo_drain_com_diretiva(tmp_path: Path, ids_da_diretiva: str) -> Path` — copia a fixture `next_tk90` (`_copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")`), grava o plano `P-0800-alfa.md` com `_escrever_plano(repo, "P-0800-alfa.md", "P-0800", "Plano alfa de teste", "ALF", "ready")`, põe no inbox a linha `- docs/plans/P-0800-alfa.md — plano alfa de teste` (`_inbox_com_linhas`), chama `_inserir_bloco_gerado(repo)` e insere no diário, como segunda linha, `**Diretiva de priorização:** <ids_da_diretiva> — texto da fixture.` — e os dois testes da seção `Testes`, pelo `backlog.main(["drain", "--repo", <repo>, "--data", "2026-09-28"])`.
  2. Rodar `python -m pytest tests/test_backlog.py -q -k aviso_diretiva` e conferir que o TF falha e o TR passa.
  3. Aplicar as duas regras de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). Os testes de `drain` que já existem (fixture sem linha de diretiva) continuam passando sem mudança.
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Nenhuma linha que já existia em `tests/test_backlog.py` sai ou muda: o card só acrescenta ao fim do arquivo; as fixtures de `tests/fixtures/backlog/` não mudam (só a cópia em `tmp_path`).
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não reescrever a diretiva no `drain`; não mudar o exit, o stdout nem os arquivos que o `drain` escreve; não mexer em `transacionar_diretiva` nem em `_parse_diretiva`; não acrescentar a recusa do prefixo de decisão (é da `RAF-T29`).
- **Contingências:**
  - se um teste que já existia em `tests/test_backlog.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_drain_aviso_diretiva_sem_id_vivo` — diretiva `` `P-0001` `` (id que não existe na fixture): `drain` sai 0 e o stderr contém `drain: aviso — a diretiva de priorização não cita nenhum id vivo nem P-0800` (hoje sai 0 sem aviso). TR `test_tr_drain_aviso_diretiva_com_id_vivo_ou_drenado_cala` — diretiva `` `P-0090` `` (plano `ready` da fixture) e, em outra cópia, `` `P-0800` `` (o drenado): os dois saem 0 e nenhum stderr contém `drain: aviso` (a regra concorrente, avisar a cada drenagem, avisaria). Suíte `tests/test_backlog.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_backlog.py -q -k aviso_diretiva` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - controle do backlog.aviso de diretiva desatualizada — um aviso diz que a diretiva não cita nada vivo nem o plano que saiu; o resultado do comando não muda — Verificação 1
- **Fora do escopo desta tarefa:** a recusa do prefixo de decisão repetido (`RAF-T29`); a reescrita da diretiva, ato de quem conduz.
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** .claude/tools/backlog.py:1044 (_id_vivo) e o aviso de diretiva sem id vivo em transacionar_drain (:1978); testes em tests/test_backlog.py
  - **Contrato:** transacionar_drain com assinatura inalterada; o aviso não muda o exit do drain
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum

### RAF-T29 — O controle do backlog recusa o prefixo de decisão que outro plano já declarou [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa faz o controle do backlog recusar o plano que declara o mesmo prefixo de decisão que outro já declarou, nomeando o plano dono do prefixo.
- **Fundamento:** `DRF-29`; `F-23` (`PREFIXO_CAMPO_RE` lê só o prefixo das tarefas), `F-24` (34 planos, 17 declaram `**Prefixo das decisões:**`, nenhuma colisão de declaração; citar prefixo de outro plano é comum e legítimo); relatório `R-28` (auditoria reg. 17).
- **Depende de:** `RAF-T28`
- **Operação do modelo:** `OP-29`
  - OP-29: Quem executa faz o controle do backlog recusar o plano que declara o mesmo prefixo de decisão que outro já declarou, nomeando o plano dono do prefixo.
  - precisa de: controle do backlog — Quem implementa acrescenta um aviso ao tirar o plano da fila e uma recusa ao conferir, sem mudar o resultado do primeiro.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/backlog.py`, parser do cabeçalho do plano (`_parse_plano`) e verbo `check`; só biblioteca padrão. O vocabulário do `check` vai hoje de `C-1` a `C-17`; a violação nova é `C-18`. Sobre a árvore de 2026-09-28 a regra não acusa nada (medido no ensaio: nenhuma linha `C-18` no `check` do repositório). O contrato do objeto é: "Quem implementa acrescenta um aviso ao tirar o plano da fila e uma recusa ao conferir, sem mudar o resultado do primeiro."
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
- **Contratos/classes:** `Plano` ganha os campos `prefixo_decisoes: str | None = None` e `prefixo_decisoes_linha: int | None = None` (depois de `status_no_texto`); funções novas `_prefixo_decisoes_checks(modelo: Modelo, violacoes: list[Violacao]) -> None` e `_numero_do_plano(plano: Plano) -> tuple[int, str]`, logo antes de `check`. Quatro regras:
  1. Constante nova, logo depois de `PREFIXO_CAMPO_RE`: `PREFIXO_DECISOES_RE`, que casa `**Prefixo das decisões:**`, espaço e, entre crases, `<letras e dígitos>-<n>`, capturando as letras e dígitos; comentário acima cita `R-28` e `DRF-29` do `P-0755`.
  2. `_parse_plano`: no mesmo laço das 20 primeiras linhas que já lê `Status` e o prefixo das tarefas (pulando bullets), a primeira linha que casa `PREFIXO_DECISOES_RE` dá `prefixo_decisoes` e `prefixo_decisoes_linha` (número da linha, a contar de 1); os dois valores entram no construtor `Plano(...)`, logo depois de `prefixo=prefixo`.
  3. `_numero_do_plano`: `(int(<dígitos de P-<n>>), plano.id)` quando o id começa por `P-` e dígitos; senão `(10**9, plano.id)`. `_prefixo_decisoes_checks`: agrupa os planos de `modelo.planos` que declaram prefixo; em cada grupo de dois ou mais, o dono é o de menor `_numero_do_plano`; para cada outro plano do grupo que não é `fora_do_corpus`, `Violacao("C-18", plano.arquivo, plano.prefixo_decisoes_linha or plano.linha_header, f"{plano.id}: prefixo de decisão '{prefixo}' já declarado por {dono.id}")`. Docstring cita `C-18`, `R-28` e `DRF-29` do `P-0755` e diz que citar não é declarar.
  4. `check`: chama `_prefixo_decisoes_checks(modelo, violacoes)` logo depois do laço dos planos e antes do laço `for tiquete in modelo.tiquetes:`.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_backlog.py` o helper `_repo_prefixos_de_decisao(tmp_path: Path, prefixo_beta: str, texto_beta: str = "") -> Path` — copia a fixture `verde` (`_copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")`) e grava em `docs/plans/` da cópia dois planos: `P-0800-alfa.md` e `P-0801-beta.md`, cada um com a linha 1 `# <id> — Plano <nome do arquivo>`, a linha 2 vazia e a linha 3 com `**Status:**` `ready`, `**Prefixo das tarefas no diário:**` (`ALF-T<n>` e `BET-T<n>`) e `**Prefixo das decisões:**` (`DSA-<n>` e `<prefixo_beta>-<n>`), separados por ` · `, cada valor entre crases; depois uma linha vazia e `texto_beta` no `P-0801` — e os dois testes da seção `Testes`, pelo `backlog.main(["check", "--repo", <repo>])`.
  2. Rodar `python -m pytest tests/test_backlog.py -q -k prefixo_de_decisao` e conferir que o TF falha e o TR passa.
  3. Aplicar as quatro regras de `Contratos/classes`.
  4. Rodar `python .claude/tools/backlog.py check` na raiz do repositório e conferir que nenhuma linha começa por `C-18`.
  5. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Nenhuma linha que já existia em `tests/test_backlog.py` sai ou muda: o card só acrescenta ao fim do arquivo; as fixtures de `tests/fixtures/backlog/` não mudam.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não contar ocorrência de prefixo no corpo do plano (citar não é declarar); não acusar prefixo de plano legado sem o campo declarado; não mudar os códigos `C-1`..`C-17` nem a forma da linha de violação; não mexer no aviso do `drain` (`RAF-T28`).
- **Contingências:**
  - se um teste que já existia em `tests/test_backlog.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o passo 4 imprimir linha que começa por `C-18` → parar e sinalizar `blocked` razão `premissa`, colando a linha.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_check_prefixo_de_decisao_repetido_recusa` — `prefixo_beta="DSA"`: `check` sai 1 e há uma linha que começa por `C-18 docs/plans/P-0801-beta.md:3 — ` e contém `P-0801: prefixo de decisão 'DSA' já declarado por P-0800`; nenhuma linha `C-18 docs/plans/P-0800-alfa.md` (hoje nenhuma linha `C-18`). TR `test_tr_check_prefixo_de_decisao_citado_nao_e_colisao` — `prefixo_beta="DSB"` e o corpo do `P-0801` com `` Aplica a `DSA-3` do P-0800. ``: nenhuma linha contém `C-18` (a regra concorrente, contar ocorrências, acusaria). Suíte `tests/test_backlog.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_backlog.py -q -k prefixo_de_decisao` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - controle do backlog.prefixo de decisão repetido — a conferência recusa o segundo, nomeando o plano dono; citar o prefixo de outro plano continua permitido — Verificação 1
- **Fora do escopo desta tarefa:** o aviso da diretiva no `drain` (`RAF-T28`); a colisão de prefixo próprio dos planos legados sem declaração (`DC`, `DM`, `DP`, `F-24`), que a regra não alcança por construção.
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** .claude/tools/backlog.py: campos prefixo_decisoes/prefixo_decisoes_linha em Plano e a violação C-18 (prefixo de decisão declarado por dois planos, nomeando o dono); testes em tests/test_backlog.py
  - **Contrato:** C-1..C-17 inalterados; citar prefixo de outro plano segue permitido; plano legado sem o campo não é acusado
  - **Não refazer:** nada a declarar
  - **Pendente:** docstring do módulo backlog.py (linhas 3 e 7) e o comentário da linha 592 ainda dizem C-1..C-17 (achado do laudo, ao consultor)

### RAF-T29a — O cabeçalho do controle do backlog conta o vocabulário do check até C-18 [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa faz as três frases de `.claude/tools/backlog.py` que contam o vocabulário do `check` dizerem `C-1..C-18`, com a `C-18` nomeada no comentário da seção do `check`.
- **Fundamento:** `DRF-67`; `AE-184` (laudo da `RAF-T29`, ressalva 91, critério (viii) da rubrica); `DRF-29`; relatório `R-28`.
- **Depende de:** `RAF-T29`
- **Operação do modelo:** `OP-29`
  - OP-29: Quem executa faz o controle do backlog recusar o plano que declara o mesmo prefixo de decisão que outro já declarou, nomeando o plano dono do prefixo.
  - precisa de: controle do backlog — Quem implementa acrescenta um aviso ao tirar o plano da fila e uma recusa ao conferir, sem mudar o resultado do primeiro.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** texto do instrumento `.claude/tools/backlog.py` — as linhas 3 e 7 do docstring do módulo e o comentário da seção do `check` (linhas 592-595); nenhum comportamento muda. A `RAF-T29` acrescentou a violação `C-18` (`_prefixo_decisoes_checks`) e deixou as três frases que contam o vocabulário em `C-1..C-17`. Fora do módulo, nenhuma enumeração viva conta o vocabulário: `tests/test_backlog.py` linha 2 é o docstring atribuído à `BKL-T2` (`C-1..C-9`, o que aquele card testou) e `docs/OPERACOES_AS_IS_P-0751.md` linha 412 é medida datada; os dois ficam.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
- **Passos:**
  1. No docstring do módulo de `.claude/tools/backlog.py`, trocar `` (`C-1..C-17`, vocabulário fechado `` por `` (`C-1..C-18`, vocabulário fechado `` (linha 3) e `` fechado em `C-1..C-17`; `` por `` fechado em `C-1..C-18`; `` (linha 7); o resto das duas linhas fica.
  2. No comentário da seção do `check`, trocar as quatro linhas do texto antigo pelas cinco do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card).

     Texto antigo:

     ```text
     # check — violações C-1..C-17 (C-11 via resolver_citacao_secao, definido abaixo — TK-60a:
     # check é o chamador de produção, nenhum subcomando novo; C-12 via _depende_checks — TK-65a;
     # C-15 acusa tíquete vivo sem subtarefa — EBK-T1; C-16 confronta card vivo com a leitura de
     # dossiê do rdo.py e C-17 acusa entrada órfã de piso_c11 — EBK-T2)
     ```

     Texto novo:

     ```text
     # check — violações C-1..C-18 (C-11 via resolver_citacao_secao, definido abaixo — TK-60a:
     # check é o chamador de produção, nenhum subcomando novo; C-12 via _depende_checks — TK-65a;
     # C-15 acusa tíquete vivo sem subtarefa — EBK-T1; C-16 confronta card vivo com a leitura de
     # dossiê do rdo.py e C-17 acusa entrada órfã de piso_c11 — EBK-T2; C-18 acusa o prefixo de
     # decisão que dois planos declaram, via _prefixo_decisoes_checks — RAF-T29 do P-0755)
     ```
  3. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Em `.claude/tools/backlog.py` só mudam as linhas 3 e 7 e o comentário das linhas 592-595: nenhum código, nome, regex, constante nem outro docstring muda; o arquivo segue LF (hoje 0 CR).
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não tocar `tests/test_backlog.py` nem `docs/OPERACOES_AS_IS_P-0751.md`; não mudar o texto das violações nem os docstrings de `_prefixo_decisoes_checks` e `_numero_do_plano`.
- **Contingências:**
  - se o texto antigo de um passo não existir verbatim → parar e sinalizar `blocked` razão `premissa`, nomeando o passo.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo (nenhum teste lê o docstring do módulo nem o comentário); `tests/test_backlog.py` e a suíte inteira.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/tools/backlog.py').read_text(encoding='utf-8');print('vocabulario=%d-%d-%d linhas=%d'%(t.count('C-1..C-17'),t.count('C-1..C-18'),t.count('via _prefixo_decisoes_checks'),len(t.splitlines())))"` → `vocabulario=0-3-1 linhas=2613` — antes `vocabulario=3-0-0 linhas=2612`, depois `vocabulario=0-3-1 linhas=2613`
- **Pronto quando:**
  - controle do backlog.prefixo de decisão repetido — o cabeçalho do instrumento conta o vocabulário do check até C-18 e nomeia quem acusa o prefixo repetido — Verificação 1
- **Fora do escopo desta tarefa:** o texto da `RAF-T29` (`done`), que fica como executado; o docstring do teste atribuído à `BKL-T2`.
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** .claude/tools/backlog.py linhas 3 e 7 do docstring e o comentário da seção check (592-596) contam C-1..C-18 e nomeiam _prefixo_decisoes_checks
  - **Contrato:** o cabeçalho do backlog.py conta o vocabulário do check como o código o tem
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum

### RAF-T30 — O fechamento de tarefa registra o achado pela linha de origem e avisa a falha de instrumento [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** Quem executa faz o fechamento de tarefa tratar cada achado do laudo pela linha de origem, pulando o já registrado e avisando a falha de instrumento.
- **Fundamento:** `DRF-21`, `DRF-22`; `F-25` (`achados_do_laudo` lê a tabela `| alvo | achado |` de `## Achado de processo`; `apensar_achado` grava a `AE-` sem origem; a dedupe é por substring do texto; a regra `B1` mora só na skill `scrum-master`, e o código não lê `escalar`); relatório `R-19` (auditoria reg. 39: o achado que o consultor reescreveu entrou de novo, em duplicata) e `R-20` (reg. 47: falha de instrumento num laudo `seguir` não chegou ao consultor).
- **Depende de:** `RAF-T27`, `RAF-T23a`
- **Operação do modelo:** `OP-30`
  - OP-30: Quem executa faz o fechamento de tarefa tratar cada achado do laudo pela linha de origem, pulando o já registrado e avisando a falha de instrumento.
  - precisa de: fechamento — Quem implementa recebe o comando que hoje só grava o veredito do marco e confere achados por semelhança de texto, e acrescenta o que a operação pede.; rubrica de revisão — Quem implementa acrescenta um critério à régua de testes, apoiado no que a evidência passa a mostrar, e faz a régua e o laudo aceitarem um quinto alvo de achado, o de instrumento, além dos quatro de hoje.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/encerrar.py`, verbo `tarefa` (`fechar_tarefa` e `apensar_achado`); só biblioteca padrão. A forma da origem, `laudo:<TAREFA>#<n>` entre crases, é a mesma que o consultor passa a citar quando registra ou reescreve achado a partir de laudo (`RAF-T35`); a linha `encerrar: B1 — …` é a que a skill `scrum-master` passa a ler como pendência substantiva (`RAF-T34`). O verbo `marco` (`RAF-T23`) não muda. O contrato do objeto é: "Quem implementa recebe o comando que hoje só grava o veredito do marco e confere achados por semelhança de texto, e acrescenta o que a operação pede."
- **Arquivos-alvo:**
  - `.claude/tools/encerrar.py`
  - `tests/test_encerrar.py`
- **Contratos/classes:** `apensar_achado(plano_path: Path, tarefa_id: str, texto: str, rota: str, data: str, tiquete_id: str | None = None, origem: str | None = None) -> str` (parâmetro novo `origem`); `fechar_tarefa` — assinatura inalterada. Três regras:
  1. `apensar_achado`: com `origem`, a entrada ganha no fim ` **Origem:** ` seguido de `origem` entre crases, depois de `**Rota:** <rota>`; sem `origem`, a entrada de hoje. Comentário cita `R-19` e `DRF-21` do `P-0755`. O `--achado` do comando segue sem origem.
  2. `fechar_tarefa`, laço dos achados do laudo: numera os achados de `achados_do_laudo(texto_laudo)` a partir de 1, na ordem da tabela; a origem do achado `n` é `laudo:<tarefa_id>#<n>`; o achado é pulado quando a origem entre crases (`` `laudo:<tarefa_id>#<n>` ``) já está no texto das `AE-` do plano (`entradas_existentes`), ou, como hoje, quando o texto está nelas ou em `textos_gravados`; senão, `apensar_achado(..., origem=<origem>)`. A comparação com as crases impede que `laudo:ALF-T1#1` case dentro de `laudo:ALF-T1#11`.
  3. `fechar_tarefa`, aviso `B1`: constantes novas, logo depois de `ACHADO_PROCESSO_HEADING`, `_ACHADO_INSTRUMENTO_RE` (casa `achado de processo (instrumento): <resto>`, sem distinção de caixa, capturando `resto`) e `_TERMOS_DE_FALHA = ("queda", "traceback", "exceção", "excecao", "exception", "error")`; depois da linha `Detalhe:` do texto devolvido, para cada achado do laudo, na ordem, que casa `_ACHADO_INSTRUMENTO_RE` e cujo `resto` em minúsculas contém um dos termos, o texto devolvido ganha a linha `encerrar: B1 — achado de instrumento com falha: <resto>` — registrado ou pulado, o aviso sai do mesmo jeito. O `main` imprime esse texto antes da linha final `encerrar: OK - comando 'tarefa' concluído; …`, como hoje.
- **Passos:**
  0. Redespacho (`DRF-68`, `AE-186`): a primeira execução deixou na árvore as três regras de `Contratos/classes` e os cinco testes, e deslocou a última linha do teste do marco, `    assert "linha nova do registro" not in saida`, para o fim de `test_tr_falha_de_instrumento_sem_termo_ou_de_outro_alvo_cala`. Tirar essa linha do fim do TR e pô-la de volta como última linha de `test_tf_marco_recusa_devolver_sem_linha_nova_do_registro`, logo depois do `)` que fecha a asserção do `Devolver`, com os mesmos quatro espaços; nada mais muda no arquivo, e o TR passa a terminar em `    assert "encerrar: B1" not in saida`. Os Passos 1 a 3 já estão feitos e não se refazem (o Passo 2 não se reproduz: os testes novos já passam); seguir ao Passo 4 e rodar também a Verificação 3.
  1. Acrescentar ao fim de `tests/test_encerrar.py` os cinco testes da seção `Testes`, com `_montar_repo`, `_laudo_com_achado` e `_argv_tarefa`, que já existem no arquivo.
  2. Rodar `python -m pytest tests/test_encerrar.py -q -k "origem_do_achado or falha_de_instrumento"` e conferir que os três TF falham e os dois TR passam.
  3. Aplicar as três regras de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 5 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). Os testes de achado que já existem (`test_tf_achado_do_laudo_vira_ae_com_rota`, `test_tr_achado_do_laudo_repetido_nao_duplica`, `test_tf_achado_do_laudo_sem_rota_declarada`) continuam passando sem mudança: afirmam o começo da linha, que não muda.
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Nenhuma linha que já existia em `tests/test_encerrar.py` sai ou muda: o card só acrescenta ao fim do arquivo.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `achados_do_laudo` nem a forma de `texto` e `rota` que ele devolve; não mudar o exit do fechamento por causa do aviso `B1`; não gravar o aviso no RDO; não reescrever `AE-` já registradas para acrescentar origem; não mexer no verbo `marco`.
- **Contingências:**
  - se um teste que já existia em `tests/test_encerrar.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_origem_do_achado_gravada_na_linha` — laudo com as linhas `dossiê` e `doutrina`: o plano tem `` - **AE-3** (`ALF-T1`, fechamento, 2026-09-26) — achado de processo (doutrina): a skill não nomeia o gate. **Rota:** tíquete **Origem:** `laudo:ALF-T1#2` `` (hoje sem a origem). TF `test_tf_origem_do_achado_ja_registrada_pula` — o plano já tem `AE-2` com outro texto e `` **Origem:** `laudo:ALF-T1#1` ``; o laudo tem a linha 1 `dossiê`: o plano não ganha `AE-3` (hoje ganha, porque o texto difere). TR `test_tr_origem_do_achado_de_outra_linha_nao_pula` — a `AE-2` existente tem `` `laudo:ALF-T1#11` ``: a linha 1 vira `AE-3` (a regra concorrente, casar `laudo:ALF-T1#1` como substring sem as crases, a pularia). TF `test_tf_falha_de_instrumento_avisa_b1` — linha `| instrumento | o card_check caiu com Traceback no item 2. Rota: tíquete |`: o stdout tem `encerrar: B1 — achado de instrumento com falha: o card_check caiu com Traceback no item 2.` antes de `encerrar: OK - comando 'tarefa' concluído` (hoje nenhum aviso). TR `test_tr_falha_de_instrumento_sem_termo_ou_de_outro_alvo_cala` — linhas `| instrumento | a saída do card_check é longa. |` e `| dossiê | o teste deu error no ramo vazio. |`: o stdout não tem `encerrar: B1` (a regra concorrente, qualquer achado de instrumento ou qualquer termo em qualquer alvo, avisaria). Suíte `tests/test_encerrar.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_encerrar.py -q -k origem_do_achado` → `exit 0` — antes `exit 0`, depois `exit 0`
  2. `python -m pytest tests/test_encerrar.py -q -k falha_de_instrumento` → `exit 0` — antes `exit 0`, depois `exit 0`
  3. `python -c "from pathlib import Path;t=Path('tests/test_encerrar.py').read_text(encoding='utf-8');a=chr(34)+'linha nova do registro'+chr(34)+' not in saida';m=t.split('def test_tf_origem_do_achado_gravada_na_linha')[0];print('marco=%d total=%d'%(m.count(a),t.count(a)))"` → `marco=2 total=2` — antes `marco=1 total=2`, depois `marco=2 total=2`
- **Pronto quando:**
  - fechamento.origem do achado registrado — cada achado registrado cita a linha do laudo de onde veio, e o fechamento pula o que já foi registrado com essa origem — Verificação 1
  - fechamento.aviso de falha de instrumento — o fechamento avisa, numa linha própria, cada achado de instrumento que relata queda ou erro — Verificação 2
- **Fora do escopo desta tarefa:** a leitura da linha `B1` pela skill e a entrega do card ao consultor (`RAF-T34`); a origem citada pelo consultor (`RAF-T35`).
- **Handover:** 2026-09-29 · para `RAF-T30a`
  - **Entregue:** .claude/tools/encerrar.py: achado registrado pela linha de origem e o aviso 'encerrar: B1 — achado de instrumento com falha' (:588) lido do alvo instrumento; tests/test_encerrar.py com os cinco testes, e a asserção do TF do marco de volta ao lugar
  - **Contrato:** o aviso B1 só dispara com o alvo instrumento e termo de falha; outro alvo cala
  - **Não refazer:** nada a declarar
  - **Pendente:** o alvo instrumento ainda não é aceito pelo rdo.py nem pela rubrica: é a RAF-T30a (DRF-68)

### RAF-T30a — O laudo aceita o alvo instrumento que o aviso do fechamento lê [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa faz o gerador do laudo aceitar o quinto alvo de achado de processo, `instrumento`, com a rubrica e o revisor nomeando-o, para que o aviso `B1` do fechamento tenha o achado que lê.
- **Fundamento:** `DRF-68`; `AE-186` (laudo da `RAF-T30`, reprovado 74, achado de processo de alvo `dossiê`); `DRF-22`; relatório `R-20`.
- **Depende de:** `RAF-T30`
- **Operação do modelo:** `OP-30`
  - OP-30: Quem executa faz o fechamento de tarefa tratar cada achado do laudo pela linha de origem, pulando o já registrado e avisando a falha de instrumento.
  - precisa de: fechamento — Quem implementa recebe o comando que hoje só grava o veredito do marco e confere achados por semelhança de texto, e acrescenta o que a operação pede.; rubrica de revisão — Quem implementa acrescenta um critério à régua de testes, apoiado no que a evidência passa a mostrar, e faz a régua e o laudo aceitarem um quinto alvo de achado, o de instrumento, além dos quatro de hoje.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit `.claude/tools/rdo.py`, verbo `laudo` (`_ALVOS_ACHADO`, o docstring de `_formatar_achados_processo`, o docstring do módulo e o `help` de `--achado-processo`), e a doutrina que conta o vocabulário dos alvos: `docs/RUBRICA_DE_REVISAO.md` §6 e `.claude/agents/pantonic-reviewer.md`; só biblioteca padrão. A `RAF-T30` fez o `encerrar.py tarefa` avisar o achado de alvo `instrumento` (`_ACHADO_INSTRUMENTO_RE` sobre o texto `achado de processo (instrumento): …` que `achados_do_laudo` monta da célula `alvo` do laudo), mas o gerador recusa esse alvo (`rdo: FALHOU - alvo instrumento fora de [...]`, exit 1) e nenhum laudo real escreve a linha. O `encerrar.py` não muda: a célula `instrumento` já casa o aviso. Ficam como atribuição datada os docstrings de `test_tr_laudo_recusa_alvo_fora_dos_tres_e_linha_com_pipe` (`BKL-T2d`) e de `test_tf_laudo_aceita_alvo_modelo` (`MC-T2`), e o arquivo `.claude/estado/dossie-AF-T4.md`.
- **Arquivos-alvo:**
  - `.claude/tools/rdo.py`
  - `tests/test_rdo.py`
  - `docs/RUBRICA_DE_REVISAO.md`
  - `.claude/agents/pantonic-reviewer.md`
- **Contratos/classes:** `_ALVOS_ACHADO` ganha a chave `"instrumento"` com o rótulo `"instrumento"`; `_formatar_achados_processo`, `cmd_laudo` e o parser do verbo `laudo` — assinaturas inalteradas. A recusa de alvo fora do vocabulário continua como está (a mensagem lista o vocabulário por `sorted(_ALVOS_ACHADO)`).
- **Passos:**
  1. Acrescentar ao fim de `tests/test_rdo.py`, depois da última linha que já existe (hoje `    assert "| dossiê | linha do achado |" in conteudo`, que fica onde está e como está), o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card; as duas linhas em branco do começo separam o bloco da função anterior).

     ```python


     # --- laudo · achado de processo, alvo instrumento (RAF-T30a do P-0755, `DRF-68`) --------------


     def test_tf_laudo_alvo_instrumento_chega_ao_aviso_b1_do_fechamento(tmp_path):
         """TF (RAF-T30a, `DRF-68`): `--achado-processo instrumento "<linha>"` sai 0, o laudo tem a
         linha `| instrumento | <linha> |`, e o `achados_do_laudo` do `encerrar.py` a devolve como o
         achado que o aviso `B1` da `RAF-T30` casa — o caminho do gerador ao fechamento, que o card
         da `RAF-T30` montava à mão. Hoje o alvo é recusado (exit 1) e nenhum laudo o escreve."""
         rdo = _load_rdo()
         laudos_dir = tmp_path / "laudos"
         linha = "o card_check caiu com Traceback no item 2. Rota: tíquete"

         exit_code = rdo.main(_argv_laudo(laudos_dir) + ["--achado-processo", "instrumento", linha])

         assert exit_code == 0
         conteudo = (laudos_dir / "P-TESTE-T1.md").read_text(encoding="utf-8")
         assert f"| instrumento | {linha} |" in conteudo
         spec = importlib.util.spec_from_file_location(
             "encerrar_do_rdo", _ROOT / ".claude" / "tools" / "encerrar.py"
         )
         encerrar = importlib.util.module_from_spec(spec)
         sys.modules[spec.name] = encerrar
         spec.loader.exec_module(encerrar)
         textos = [texto for texto, _rota in encerrar.achados_do_laudo(conteudo)]
         assert textos == ["achado de processo (instrumento): o card_check caiu com Traceback no item 2."]
         assert encerrar._ACHADO_INSTRUMENTO_RE.search(textos[0])
     ```
  2. Rodar `python -m pytest tests/test_rdo.py -q -k alvo_instrumento` e conferir que o TF falha (`exit 1`).
  3. Em `.claude/tools/rdo.py`, trocar a linha antiga 3 pelas seis linhas novas 3 (as quebras são as do bloco; cada linha perde o recuo deste card).

     Linha antiga 3:

     ```text
     _ALVOS_ACHADO = {"dossie": "dossiê", "doutrina": "doutrina", "rubrica": "rubrica", "modelo": "modelo"}
     ```

     Linhas novas 3:

     ```text
     # O quinto alvo, `instrumento`, é o que o aviso `B1` do `encerrar.py tarefa` lê (RAF-T30a, `DRF-68`
     # do P-0755).
     _ALVOS_ACHADO = {
         "dossie": "dossiê", "doutrina": "doutrina", "rubrica": "rubrica", "modelo": "modelo",
         "instrumento": "instrumento",
     }
     ```
  4. Ainda em `.claude/tools/rdo.py`, três trocas de texto, cada uma na mesma linha, sem refluxo: no docstring do módulo, `` `doutrina`, `rubrica` ou `modelo`) grava a seção `` por `` `doutrina`, `rubrica`, `modelo` ou `instrumento`) grava a seção ``; no docstring de `_formatar_achados_processo`, `§6: campo próprio, quatro alvos.` por `§6: campo próprio, cinco alvos.`; e, no `help` de `--achado-processo`, as duas linhas do texto antigo 4 pelas duas do texto novo 4 (cada linha perde o recuo deste card e guarda os doze espaços iniciais que tem no arquivo).

     Texto antigo 4:

     ```text
                 "Achado de processo (repetivel): ALVO e dossie (ou dossiê), doutrina, rubrica ou modelo, "
                 "seguido de uma linha. Nao altera percentual, veredito, bloqueante nem recomendacao "
     ```

     Texto novo 4:

     ```text
                 "Achado de processo (repetivel): ALVO e dossie (ou dossiê), doutrina, rubrica, modelo "
                 "ou instrumento, seguido de uma linha. Nao altera percentual, veredito, bloqueante nem recomendacao "
     ```
  5. Em `docs/RUBRICA_DE_REVISAO.md` §6, trocar `com quatro alvos possíveis:` por `com cinco alvos possíveis:` e acrescentar, logo depois da linha da tabela que começa por `` | `modelo` | ``, a linha nova 5, sem mudar as demais.

     Linha nova 5:

     ```text
     | `instrumento` | instrumento do kit que caiu, devolveu saída errada ou recusou entrada válida na execução ou na revisão; o `encerrar.py tarefa` avisa, na linha `encerrar: B1 —`, o achado deste alvo que relata queda, traceback, exceção ou erro |
     ```
  6. Em `.claude/agents/pantonic-reviewer.md`, trocar as duas linhas do texto antigo 6 pelas três do texto novo 6 (cada linha perde o recuo deste card; as de continuação guardam os dois espaços iniciais que têm no arquivo).

     Texto antigo 6:

     ```text
     - Achado de processo (`docs/RUBRICA_DE_REVISAO.md` §6) tem campo próprio e quatro alvos possíveis —
       `dossiê`, `doutrina`, `rubrica`, `modelo`. Ele nunca rebaixa dimensão de entrega e sempre sai com rota.
     ```

     Texto novo 6:

     ```text
     - Achado de processo (`docs/RUBRICA_DE_REVISAO.md` §6) tem campo próprio e cinco alvos possíveis —
       `dossiê`, `doutrina`, `rubrica`, `modelo`, `instrumento`. Ele nunca rebaixa dimensão de entrega
       e sempre sai com rota.
     ```
  7. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma o teste novo. `tests/test_rdo.py`, `tests/test_encerrar.py` e `tests/test_doutrina_unidade.py` inteiros passam (medida do consultor, 2026-09-29: `127 passed` nos três juntos, antes do card).
  - Nenhuma linha que já existia em `tests/test_rdo.py` sai ou muda: o card só acrescenta depois da última linha do arquivo, e a asserção `| dossiê | linha do achado |` continua a última do teste a que pertence (`AE-186`: a `RAF-T30` inseriu antes da última linha e deslocou uma asserção).
  - Os quatro arquivos-alvo seguem LF (hoje 0 CR em cada um).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `.claude/tools/encerrar.py` nem `achados_do_laudo`; não mudar a mensagem de recusa de alvo nem o sinônimo `dossiê`; não mudar os docstrings dos testes que já existem; não mexer em outra seção da rubrica nem em outra linha do revisor.
- **Contingências:**
  - se um texto antigo de um passo não existir verbatim, uma única vez, no arquivo do passo → parar e sinalizar `blocked` razão `premissa`, nomeando o passo.
  - se um teste que já existia em `tests/test_rdo.py`, `tests/test_encerrar.py` ou `tests/test_doutrina_unidade.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_laudo_alvo_instrumento_chega_ao_aviso_b1_do_fechamento` — `rdo.py laudo --achado-processo instrumento "o card_check caiu com Traceback no item 2. Rota: tíquete"` sai 0, o laudo tem a linha `| instrumento | … |`, e `achados_do_laudo` do `encerrar.py` a devolve como `achado de processo (instrumento): o card_check caiu com Traceback no item 2.`, que `_ACHADO_INSTRUMENTO_RE` casa (hoje o gerador sai 1). Suítes `tests/test_rdo.py`, `tests/test_encerrar.py`, `tests/test_doutrina_unidade.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_rdo.py -q -k alvo_instrumento` → `exit 0` — antes `exit 5`, depois `exit 0`
  2. `python -c "from pathlib import Path;b=chr(96);r=Path('.claude/tools/rdo.py').read_text(encoding='utf-8');u=Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8');v=Path('.claude/agents/pantonic-reviewer.md').read_text(encoding='utf-8');print('alvos=%d-%d-%d rdo=%d-%d-%d'%(r.count('quatro alvos')+u.count('quatro alvos')+v.count('quatro alvos'),u.count('| '+b+'instrumento'+b+' |'),v.count(b+'modelo'+b+', '+b+'instrumento'+b),r.count('ou '+b+'instrumento'+b),r.count('ou instrumento, seguido'),r.count('cinco alvos')))"` → `alvos=0-1-1 rdo=1-1-1` — antes `alvos=3-0-0 rdo=0-0-0`, depois `alvos=0-1-1 rdo=1-1-1`
- **Pronto quando:**
  - fechamento.aviso de falha de instrumento — o fechamento avisa, numa linha própria, cada achado de instrumento que relata queda ou erro — Verificações 1 e 2
- **Fora do escopo desta tarefa:** a leitura da linha `B1` pela skill e a entrega do card ao consultor (`RAF-T34`); a comparação de asserções por função no dossiê de evidência (`AE-186` item 3, rota auditoria final).
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** .claude/tools/rdo.py _ALVOS_ACHADO com o quinto alvo instrumento (docstrings e help acertados); docs/RUBRICA_DE_REVISAO.md §6 com cinco alvos; .claude/agents/pantonic-reviewer.md com os cinco alvos; tests/test_rdo.py com o TF ponta a ponta laudo → aviso B1
  - **Contrato:** rdo.py laudo --achado-processo instrumento grava a linha que o aviso B1 do encerrar.py lê
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum

### RAF-T31 — A série de telemetria atribui pela linha de abertura do despacho e guarda uma linha por agente [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** Quem executa faz a série de telemetria guardar uma linha por agente, atribuída ao plano e à tarefa que a abertura do despacho declara.
- **Fundamento:** `DRF-18`, `DRF-39`; `F-26` (o hook deriva a tarefa de `tarefa-corrente.json` para executor, revisor e consultor e do primeiro `P-<n>` da primeira mensagem para os demais; `agent_transcript_path` já é lido; o cabeçalho da série tem oito colunas); relatório `R-16` (auditoria reg. 41 e 54: linhas no plano errado e duplicata por agente).
- **Depende de:** `RAF-T27`
- **Operação do modelo:** `OP-31`
  - OP-31: Quem executa faz a série de telemetria guardar uma linha por agente, atribuída ao plano e à tarefa que a abertura do despacho declara.
  - precisa de: despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumentos do kit — o hook `SubagentStop` `.claude/tools/telemetria_hook.py` e o escritor da série `.claude/tools/telemetria.py`, que o hook chama por subprocesso (`telemetria.py append … --file <série>`); só biblioteca padrão; o hook falha aberto (exceção nunca bloqueia). A série real `docs/telemetria.tsv` não se edita neste card: a primeira parada de subagente depois da entrega a migra, pelo próprio escritor (`DRF-39`). O único leitor da série em código, `_ler_tsv` de `.claude/tools/encerrar.py`, lê pelo cabeçalho e descarta linha com número de colunas diferente dele (medido no ensaio: `tests/test_encerrar.py` passa sem mudança; §8 risco 1). A linha de abertura do despacho (`despacho: <P-id>[ <ID>]`) já sai no texto pronto do `despachar` desde a `RAF-T3`; a regra de que todo despacho de subagente abre com ela é da `RAF-T33`. O contrato do objeto é: "Quem implementa faz o registro ler o plano e a tarefa na primeira linha do despacho e ganhar uma coluna que identifica o agente, completando as linhas antigas."
- **Arquivos-alvo:**
  - `.claude/tools/telemetria_hook.py`
  - `.claude/tools/telemetria.py`
  - `tests/test_telemetria_hook.py`
  - `tests/test_telemetria.py`
- **Contratos/classes:** `processar(payload: dict, estado_path: Path, telemetria_cli: Path, tsv_path: Path | None = None, data: str | None = None) -> bool` — assinatura inalterada; funções novas `_linha_de_despacho(linhas: list[str]) -> tuple[str, str | None] | None` (hook), `gravar_por_agente(path: Path, row: str, agente: str) -> None` e `_tem_coluna_agente(path: Path) -> bool` (escritor); `_contar_linhas_com_prefixo(tsv_path: Path, prefixo: str, excluir_agente: str | None = None) -> int` (parâmetro novo). Seis regras:
  1. Hook, constante nova logo depois de `_RE_ID_PLANO`: `_RE_LINHA_DESPACHO`, multilinha, que casa a linha inteira `despacho: <P-id>` seguida, opcionalmente, de espaço e `<ID>` — `P-id` = `P-` e dígitos; `ID` = tarefa (maiúscula, maiúsculas ou dígitos, `-T`, dígitos, uma minúscula opcional) ou tíquete (`TK-`, dígitos, uma minúscula opcional) —, com espaço opcional no fim; comentário cita `R-16` e `DRF-18` do `P-0755`. `_linha_de_despacho`: no texto da primeira entrada `user` do transcript (`_primeiro_texto_de_usuario`), a primeira linha que casa dá `(P-id, ID ou None)`; sem ela, `None`.
  2. Hook, `processar`, depois de ler o estado e as linhas: `agente` = nome do arquivo de `agent_transcript_path` sem extensão (`Path(...).stem`); `despacho = _linha_de_despacho(linhas)`. Executor: sem estado e sem `ID` no despacho → `False`, como hoje; a tarefa é o `ID` do despacho quando houver, senão a do estado; o modelo é o do estado quando a tarefa do estado é a mesma, senão o do transcript normalizado (`_normalizar_modelo_de_papel(_ultimo_modelo_assistant(linhas))`); o projeto é o do estado, ou o nome da raiz (`estado_path.parents[2].name`) sem estado. Revisor e consultor: a tarefa-base é o `ID` do despacho quando houver, senão a do estado; o resto como hoje. Demais papéis: o id do plano é o `P-id` do despacho quando houver, senão o primeiro `P-<n>` da primeira mensagem, como hoje. A forma do id da série (`<ID>`, `<ID>-revisao`, `<ID>-consultor-<n>`, `<P-id>-<sufixo>`, `sem-id-<sufixo>`) não muda.
  3. Hook: a numeração do consultor chama `_contar_linhas_com_prefixo(serie, f"{tarefa_base}-consultor-", excluir_agente=agente)`, que não conta a linha cuja coluna `agente` (quando o cabeçalho a tem) é o próprio agente; e os argumentos do CLI ganham `--agente <agente>` depois de `--file <série>`.
  4. Escritor, `append` do CLI: opção nova `--agente` (`default=None`, ajuda `Agente da linha (R-16): substitui a linha do mesmo agente em vez de apensar.`); com ela, `gravar_por_agente(target, row, args.agente)`, a mensagem `telemetria: OK - linha do agente '<agente>' gravada em '<target>'.` e exit 0; sem ela, `append_row` como hoje.
  5. Escritor, `gravar_por_agente` (`DRF-18`, `DRF-39`, docstring cita os dois): lê as linhas não vazias da série (arquivo ausente: nenhuma); sem cabeçalho (primeira linha que não começa por `data` e tabulação), põe o de `_COLUMNS`; cabeçalho que não termina na coluna `agente` ganha `\tagente`, e cada linha de dado ganha `\t-`; a linha nova é `row` + tabulação + `agente`; a linha de dado cuja última coluna é `agente` é trocada por ela, ou, sem nenhuma, ela entra no fim; escrita atômica (arquivo temporário no mesmo diretório e `os.replace`, como `append_row`).
  6. Escritor, `append_row`: logo depois de `checar_repetida`, quando `_tem_coluna_agente(path)` (a primeira linha começa por `data` e tabulação e termina na coluna `agente`) e a linha tem as colunas de `_COLUMNS`, ela ganha `\t-`; comentário cita `DRF-39` do `P-0755`. Série sem a coluna: tudo como hoje.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_telemetria_hook.py` o helper `_transcript_com_mensagem(caminho: Path, primeira_mensagem: str, input_tokens: int = 10) -> Path` (grava no `caminho` duas linhas: `_linha_user(primeira_mensagem)` e `_linha_assistant` com `input_tokens` e os outros três campos de uso em 0, timestamp `2026-09-26T10:00:00+00:00`, `n_tool_uses=1`, `model="claude-opus-4"`) e os cinco testes do hook da seção `Testes`; acrescentar ao fim de `tests/test_telemetria.py` o teste do escritor.
  2. Rodar `python -m pytest tests/test_telemetria_hook.py tests/test_telemetria.py -q -k "linha_de_despacho or linhas_por_agente"` e conferir que os cinco TF falham e o TR passa.
  3. Aplicar as seis regras de `Contratos/classes`.
  4. Reescrever, em `tests/test_telemetria_hook.py`, as três asserções que a coluna nova muda de sentido — o hook passa a gravar a coluna `agente` com o nome do transcript —, sem remover nenhuma: em `test_tf_processar_payload_de_fixture_grava_linha_esperada_no_tsv`, o cabeçalho esperado passa a `_HEADER.rstrip("\n") + "\tagente"` e a linha esperada ganha `\tagent-transcript` no fim; em `test_tr_processar_sem_tsv_path_grava_na_serie_do_repo_do_estado`, a linha esperada ganha `\tagent-transcript` no fim; em `test_tf_hook_executavel_stdin_utf8_nao_falha_e_preserva_invariancia`, `linha_esperada` passa a ser `_HEADER.rstrip("\n") + "\tagente\n"` seguido da linha de hoje com `\tanálise` no fim (a série nasce com cabeçalho, e o transcript da raiz isolada é `análise.jsonl`).
  5. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 6 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_encerrar.py` e os testes de `tests/test_telemetria.py` que já existem passam sem mudança.
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Nos dois arquivos de teste, as únicas linhas que já existiam e mudam são as do passo 4; o resto só se acrescenta ao fim.
  - Os testes gravam só em `tmp_path`; nenhum toca `docs/telemetria.tsv` nem `.claude/estado/` reais.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não editar `docs/telemetria.tsv` à mão nem por script; não mudar `_COLUMNS`, `build_row` nem `checar_repetida`; não mudar a forma do id da série; não mexer no painel (`.claude/tools/progresso_hook.py`, `RAF-T32`) nem em `.claude/tools/encerrar.py`; não ler `agent_id` do payload (não confirmado, `F-26`).
- **Contingências:**
  - se um teste que já existia na suíte, fora os três reescritos no passo 4, cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_linha_de_despacho_atribui_o_plano_antes_do_primeiro_id_citado` — planejador cuja primeira mensagem é `Contexto: veja o P-0700 antes.`, quebra, `despacho: P-0755`, quebra, `Planeje.`: a série grava a tarefa `P-0755-planejador` (hoje `P-0700-planejador`). TF `test_tf_linha_de_despacho_atribui_a_tarefa_antes_do_estado` — revisor com `despacho: P-0755 RAF-T3` e o estado da `EXA-T55`: `RAF-T3-revisao` (hoje `EXA-T55-revisao`). TR `test_tr_linha_de_despacho_ausente_segue_o_estado` — revisor sem a linha: `EXA-T55-revisao` (a regra concorrente, exigir a linha, não gravaria nada). TF `test_tf_linhas_por_agente_substitui_a_do_mesmo_agente` — série com a linha antiga `P-0700-scout` de oito colunas e duas paradas do planejador do transcript `agent-a1b2.jsonl`, a segunda com `input_tokens` 3000, `data="2026-09-28"`: o cabeçalho é o de hoje com `\tagente`, a linha antiga termina em `\t-`, e há uma só linha nova, com tarefa `P-0755-planejador`, `tokens_k` `3.0` e agente `agent-a1b2` (hoje: duas linhas, sem a coluna). TF `test_tf_linhas_por_agente_outro_agente_apensa` — transcripts `agent-um.jsonl` e `agent-dois.jsonl`: a última coluna das linhas de dado é `agent-um`, `agent-dois` (hoje a coluna não existe). TF `test_tf_linhas_por_agente_append_sem_agente_em_serie_migrada_leva_traco` (em `tests/test_telemetria.py`) — série só com o cabeçalho de nove colunas e `telemetria.main(["append", …])` sem `--agente`: a última linha é `2026-09-28\tPantonicApp\tRAF-T1\tsonnet\t3\t10.0\t5.0\tusage\t-` (hoje sai com oito colunas). Suítes `tests/test_telemetria_hook.py`, `tests/test_telemetria.py`, `tests/test_encerrar.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_telemetria_hook.py -q -k linha_de_despacho` → `exit 0` — antes `exit 5`, depois `exit 0`
  2. `python -m pytest tests/test_telemetria_hook.py tests/test_telemetria.py -q -k linhas_por_agente` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - série de telemetria.plano e tarefa atribuídos — a atribuição sai da linha de abertura do despacho, antes de qualquer outra pista — Verificação 1
  - série de telemetria.linhas por agente — uma linha por agente, a última e acumulada; as linhas antigas ganham a coluna nova vazia — Verificação 2
- **Fora do escopo desta tarefa:** o painel com a tarefa do despacho (`RAF-T32`); a regra da linha de abertura na governança (`RAF-T33`); o despacho do consultor com a linha do card em triagem (`RAF-T34`).
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** .claude/tools/telemetria_hook.py atribui a linha pela abertura do despacho; .claude/tools/telemetria.py com gravar_por_agente (uma linha por agente, append com --agente); testes em tests/test_telemetria_hook.py e tests/test_telemetria.py
  - **Contrato:** a série guarda uma linha por agente; o append com --agente não passa por checar_repetida
  - **Não refazer:** nada a declarar
  - **Pendente:** docstring de append_row/checar_repetida ainda diz que a recusa vale para todo escritor; destino da DFP-8 em aberto (achado do laudo, ao consultor)

### RAF-T31a — O escritor da série de telemetria diz nos docstrings quem recusa a linha repetida e que a linha do agente se troca [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa faz os docstrings de `.claude/tools/telemetria.py` dizerem que a recusa da linha repetida vale para o escritor sem agente e que a linha do mesmo agente se troca.
- **Fundamento:** `DRF-69`; `AE-190` (laudo da `RAF-T31`, ressalva 91, achado 2); `DRF-18`, `DRF-39`; `DFP-8` do `P-0752`.
- **Depende de:** `RAF-T31`
- **Operação do modelo:** `OP-31`
  - OP-31: Quem executa faz a série de telemetria guardar uma linha por agente, atribuída ao plano e à tarefa que a abertura do despacho declara.
  - precisa de: despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** texto do instrumento `.claude/tools/telemetria.py` — o docstring do módulo (o parágrafo da série histórica, linhas 8-11, e o do CLI, linhas 18-22) e os de `checar_repetida` (linhas 150-152), `gravar_por_agente` (linhas 178-182) e `append_row` (linhas 225-229); nenhum comportamento muda. A `RAF-T31` pôs o `append --agente` em `gravar_por_agente`, que troca a linha do mesmo agente e migra a série sem passar por `checar_repetida`, e deixou os textos dizendo que o script só apende e que a recusa vale para todo escritor. Pela `DRF-69`, a `DFP-8` segue no escritor sem agente (`append_row` e a pré-checagem do `encerrar.py`), e no escritor por agente a mesma rodada é a linha do mesmo agente. Nenhum teste lê esses docstrings (medido).
- **Arquivos-alvo:**
  - `.claude/tools/telemetria.py`
- **Passos:**
  1. No docstring do módulo, trocar as quatro linhas do texto antigo pelas sete do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card).

     Texto antigo:

     ```text
     A série histórica é insumo — nenhuma linha existente é reescrita, reordenada ou normalizada; o
     script só apende. Colunas na ordem do header real do TSV: `data`, `projeto`, `tarefa`, `modelo`,
     `tool_uses`, `tokens_k`, `duracao_s`, `fonte`. O mapeamento é sempre por nome de coluna (nunca por
     posição), o que elimina o risco de "coluna trocada em silêncio" que a edição manual admitia.
     ```

     Texto novo:

     ```text
     A série histórica é insumo — sem `--agente`, nenhuma linha existente é reescrita, reordenada ou
     normalizada, e o script só apende; com `--agente` (`DRF-18`, `DRF-39` do `P-0755`), a linha do
     mesmo agente é substituída, e a série sem a coluna `agente` a ganha, com `-` nas linhas antigas.
     Colunas na ordem do header real do TSV: `data`, `projeto`, `tarefa`, `modelo`, `tool_uses`,
     `tokens_k`, `duracao_s`, `fonte` e, na série migrada, `agente`. O mapeamento é sempre por nome
     de coluna (nunca por posição), o que elimina o risco de "coluna trocada em silêncio" que a
     edição manual admitia.
     ```
  2. No docstring do módulo, trocar as três últimas linhas do parágrafo do CLI pelas três do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card).

     Texto antigo:

     ```text
     [--file caminho/para/telemetria.tsv]``. Sem `--file`, resolve `docs/telemetria.tsv` a partir da
     raiz do repositório (mesmo desenho do `--root` de `.claude/checks/dead_code.py`: a raiz é
     derivada da posição do próprio script, não do diretório de trabalho).
     ```

     Texto novo:

     ```text
     [--file caminho/para/telemetria.tsv] [--agente A]``. Sem `--file`, resolve `docs/telemetria.tsv`
     a partir da raiz do repositório (mesmo desenho do `--root` de `.claude/checks/dead_code.py`: a
     raiz é derivada da posição do próprio script, não do diretório de trabalho).
     ```
  3. No docstring de `checar_repetida`, trocar a última linha pelas quatro do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os quatro espaços do docstring).

     Texto antigo:

     ```text
         (DFP-8) — chamada antes de qualquer escrita, para que a recusa valha para todo escritor."""
     ```

     Texto novo:

     ```text
         (DFP-8) — chamada antes de qualquer escrita sem agente (`append_row` e o `encerrar.py`),
         para que a recusa valha para todo escritor sem agente; o escritor por agente não a chama:
         nele a mesma rodada é a linha do mesmo agente, que `gravar_por_agente` substitui (`DRF-69`
         do `P-0755`)."""
     ```
  4. No docstring de `gravar_por_agente`, trocar a última linha pelas três do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os quatro espaços do docstring).

     Texto antigo:

     ```text
         arquivo temporário no mesmo diretório e `os.replace`, como `append_row`."""
     ```

     Texto novo:

     ```text
         arquivo temporário no mesmo diretório e `os.replace`, como `append_row`. Não chama
         `checar_repetida` (DFP-8): a linha do mesmo agente é a mesma rodada, e a troca a deixa
         idempotente (`DRF-69` do `P-0755`)."""
     ```
  5. No docstring de `append_row`, trocar a última linha pelas duas do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os quatro espaços do docstring).

     Texto antigo:

     ```text
         antes de ler os bytes — a recusa vale para todo escritor, não só o CLI."""
     ```

     Texto novo:

     ```text
         antes de ler os bytes — a recusa vale para todo escritor sem agente, não só o CLI; a linha
         com agente vai a `gravar_por_agente`, que não recusa (`DRF-69` do `P-0755`)."""
     ```
  6. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Em `.claude/tools/telemetria.py` só mudam os cinco trechos dos Passos 1 a 5: nenhum código, nome, constante, mensagem nem `help` muda; o arquivo segue LF (hoje 0 CR).
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar o código de `checar_repetida`, `gravar_por_agente`, `append_row` nem do CLI; não tocar `.claude/tools/telemetria_hook.py`, `.claude/tools/encerrar.py` nem o texto da `DFP-8` no `P-0752`.
- **Contingências:**
  - se o texto antigo de um passo não existir verbatim → parar e sinalizar `blocked` razão `premissa`, nomeando o passo.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo (nenhum teste lê os docstrings do escritor); `tests/test_telemetria.py`, `tests/test_telemetria_hook.py` e a suíte inteira.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/tools/telemetria.py').read_text(encoding='utf-8');print('docstring=%d-%d-%d-%d-%d linhas=%d'%(t.count('valha para todo escritor.'),t.count('para todo escritor, n'),t.count('reordenada ou normalizada;'),t.count('DRF-69'),t.count('[--agente A]'),len(t.splitlines())))"` → `docstring=0-0-0-3-1 linhas=314` — antes `docstring=1-1-1-0-0 linhas=305`, depois `docstring=0-0-0-3-1 linhas=314`
- **Pronto quando:**
  - série de telemetria.linhas por agente — o texto do escritor diz que a linha do mesmo agente se troca e que a recusa da linha repetida vale para o escritor sem agente — Verificação 1
- **Fora do escopo desta tarefa:** o texto da `RAF-T31` (`done`), que fica como executado; o texto da `DFP-8` no `P-0752`; o vermelho do `dead_code` pela sonda (`AE-189`, `DRF-44`).
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** .claude/tools/telemetria.py: cinco trechos de docstring (módulo, checar_repetida, gravar_por_agente, append_row) dizem quem recusa a linha repetida e que a linha do agente se troca
  - **Contrato:** nenhum código mudou; docstrings coerentes com a DRF-69
  - **Não refazer:** nada a declarar
  - **Pendente:** a frase de telemetria.py:5-6 ('só ganha uma linha no final') segue falsa para append --agente (achado do laudo, ao consultor)

### RAF-T31b — O primeiro parágrafo do docstring e o help do append da série de telemetria ressalvam o --agente [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa faz o primeiro parágrafo do docstring de `.claude/tools/telemetria.py` e o `help` do subcomando `append` dizerem que, com `--agente`, a linha do mesmo agente se troca em vez de só ganhar uma linha no final.
- **Fundamento:** `DRF-70`; `AE-191` (laudo da `RAF-T31a`, ressalva 91, achado 1); `DRF-69`; `DRF-18`, `DRF-39`.
- **Depende de:** `RAF-T31a`
- **Operação do modelo:** `OP-31`
  - OP-31: Quem executa faz a série de telemetria guardar uma linha por agente, atribuída ao plano e à tarefa que a abertura do despacho declara.
  - precisa de: despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** texto do instrumento `.claude/tools/telemetria.py` — o fim do primeiro parágrafo do docstring do módulo (linhas 5-6) e o `help` do subcomando `append` em `main` (linha 271); nenhum comportamento muda. A `RAF-T31a` reescreveu o segundo parágrafo do docstring (com `--agente`, a linha do mesmo agente é substituída) e deixou o primeiro dizendo que o conteúdo anterior só ganha uma linha no final, e o `help` do `append` dizendo que ele adiciona uma linha. São as duas frases do arquivo que ainda afirmam só o apêndice sem ressalva (medido: o `append_row` diz o mesmo só dele, o que é verdade; a `description` do parser nomeia o verbo). Nenhum teste lê o docstring nem o `help` (medido).
- **Arquivos-alvo:**
  - `.claude/tools/telemetria.py`
- **Passos:**
  1. No docstring do módulo, trocar as duas linhas do texto antigo pelas três do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card).

     Texto antigo:

     ```text
     diretório + `os.replace`) — nenhum leitor concorrente vê um arquivo parcialmente escrito, e o
     conteúdo anterior nunca é tocado por conteúdo (só ganha uma linha no final).
     ```

     Texto novo:

     ```text
     diretório + `os.replace`) — nenhum leitor concorrente vê um arquivo parcialmente escrito, e,
     sem `--agente`, o conteúdo anterior nunca é tocado por conteúdo (só ganha uma linha no final;
     com `--agente`, ver o parágrafo seguinte).
     ```
  2. Em `main`, trocar a linha do texto antigo pelas três do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda o recuo do código).

     Texto antigo:

     ```text
         append_parser = subparsers.add_parser("append", help="Adiciona uma linha validada ao TSV.")
     ```

     Texto novo:

     ```text
         append_parser = subparsers.add_parser(
             "append", help="Adiciona uma linha validada ao TSV; com --agente, troca a do mesmo agente."
         )
     ```
  3. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Em `.claude/tools/telemetria.py` só mudam os dois trechos dos Passos 1 e 2: nenhum código além da quebra da chamada do Passo 2, nenhum nome, constante nem mensagem muda; o arquivo segue LF (hoje 0 CR).
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar os docstrings que a `RAF-T31a` reescreveu (segundo parágrafo e CLI do módulo, `checar_repetida`, `gravar_por_agente`, `append_row`) nem a `description` do parser; não tocar `.claude/tools/telemetria_hook.py` nem `.claude/tools/encerrar.py`.
- **Contingências:**
  - se o texto antigo de um passo não existir verbatim → parar e sinalizar `blocked` razão `premissa`, nomeando o passo.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo (nenhum teste lê o docstring nem o `help`); `tests/test_telemetria.py`, `tests/test_telemetria_hook.py` e a suíte inteira.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/tools/telemetria.py').read_text(encoding='utf-8');print('texto=%d-%d-%d-%d linhas=%d'%(t.count('no final).'),t.count('no final;'),t.count('ver o par'),t.count('troca a do mesmo agente'),len(t.splitlines())))"` → `texto=0-1-1-1 linhas=317` — antes `texto=1-0-0-0 linhas=314`, depois `texto=0-1-1-1 linhas=317`
- **Pronto quando:**
  - série de telemetria.linhas por agente — nenhuma frase do escritor afirma só o apêndice sem ressalvar o `--agente` — Verificação 1
- **Fora do escopo desta tarefa:** o texto da `RAF-T31` e da `RAF-T31a` (`done`), que fica como executado; o vermelho do `dead_code` pela sonda (`DRF-44`).
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** .claude/tools/telemetria.py: primeiro parágrafo do docstring do módulo ressalva 'sem --agente' e o help do append diz 'com --agente, troca a do mesmo agente'
  - **Contrato:** a família de frases do escritor da telemetria está coerente com a DRF-69
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum

### RAF-T32 — O painel do gerente mostra a tarefa que a linha de abertura do despacho declara [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa faz o painel do gerente mostrar a tarefa que a abertura do despacho declara, e não a tarefa corrente do loop.
- **Fundamento:** `DRF-18`; `F-26` (`tarefa_corrente` usa o cache do loop e, sem ele, `tarefa-corrente.json` e `localizar_card`; o consultor e o painel ficaram com a tarefa corrente em vez da despachada); relatório `R-16` (auditoria reg. 54).
- **Depende de:** `RAF-T31`
- **Operação do modelo:** `OP-32`
  - OP-32: Quem executa faz o painel do gerente mostrar a tarefa que a abertura do despacho declara, e não a tarefa corrente do loop.
  - precisa de: série de telemetria — Quem implementa faz o registro ler o plano e a tarefa na primeira linha do despacho e ganhar uma coluna que identifica o agente, completando as linhas antigas.; despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/progresso_hook.py`, os ramos `PreToolUse` e `PostToolUse` da ferramenta `Agent` em `evento` (a função que trata os eventos do hook, linhas 334-497; o arquivo não define `processar`, que é de `backlog_hook.py` e `telemetria_hook.py`, `DRF-71`); só biblioteca padrão; o hook não importa o `telemetria_hook.py` (a gramática da linha é a mesma da `RAF-T31`, repetida com comentário que diz isso). O estado do loop (`estado_loop["tarefa"]`) não muda pela linha: ela só escolhe o título mostrado. As frases `M-3`..`M-16` não mudam de texto. O contrato do objeto é: "Quem implementa faz o painel ler a mesma linha de abertura do despacho antes de recorrer à tarefa corrente."
- **Arquivos-alvo:**
  - `.claude/tools/progresso_hook.py`
  - `tests/test_progresso_hook.py`
- **Contratos/classes:** função nova `tarefa_do_despacho(prompt: str, raiz: Path) -> tuple[str, str, str] | None`, logo antes de `tarefa_corrente`. Três regras:
  1. Constante nova `_RE_LINHA_DESPACHO`, multilinha, que casa a linha inteira `despacho: P-<dígitos> <ID>` — `ID` = tarefa (maiúscula, maiúsculas ou dígitos, `-T`, dígitos, uma minúscula opcional) ou tíquete (`TK-`, dígitos, uma minúscula opcional) —, com espaço opcional no fim; a linha sem `ID` não casa. Comentário cita `R-16` e `DRF-18` do `P-0755` e diz que a gramática é a do `telemetria_hook.py`, sem import cruzado.
  2. `tarefa_do_despacho`: sem casamento no `prompt` → `None`; com ele, `(ID, título, objetivo)` pelo `localizar_card(ID, raiz)` (que devolve título, objetivo e título do plano); não escreve no estado do loop.
  3. `evento`: no ramo `PreToolUse` · `Agent` (a atribuição `_, titulo, objetivo = tarefa_corrente(estado_loop, estado, raiz)`, linha 447 medida em 2026-09-29) e no ramo `PostToolUse` · `Agent` que chama `de_volta` (a atribuição `_, titulo, _ = tarefa_corrente(estado_loop, estado, raiz)` do `else`, linha 471; a do ramo `UserPromptSubmit`, linha 486, não muda), o trio `(_, titulo, objetivo)` passa a vir de `tarefa_do_despacho(str(ti.get("prompt", "")), raiz)` e, quando ela devolve `None`, de `tarefa_corrente(estado_loop, estado, raiz)`, como hoje.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_progresso_hook.py` o helper `_despachar_agente(estado, raiz, sub, prompt)` (roda o payload `PreToolUse` · `Agent` com `subagent_type` e `prompt` dados, pelo `rodar`, e devolve a última linha de `progresso(estado)`) e os dois testes da seção `Testes`, com as fixtures `estado` e `raiz` do arquivo (o plano `P-9999` tem `TLG-T9` "Um título de teste" e `TLG-T10` "Outro título").
  2. Rodar `python -m pytest tests/test_progresso_hook.py -q -k tarefa_do_despacho` e conferir que o TF falha e o TR passa.
  3. Aplicar as três regras de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Nenhuma linha que já existia em `tests/test_progresso_hook.py` sai ou muda: o card só acrescenta ao fim do arquivo.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não importar o `telemetria_hook.py`; não gravar a tarefa da linha em `estado_loop`; não mudar o texto de nenhuma frase do repertório nem a tabela da skill `scrum-master`; não mexer no ramo `UserPromptSubmit`.
- **Contingências:**
  - se um teste que já existia em `tests/test_progresso_hook.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_tarefa_do_despacho_no_painel_vence_a_corrente` — com a `TLG-T9` como corrente (payload do `backlog.py next`), o consultor despachado com o prompt `despacho: P-9999 TLG-T10`, quebra, `cenario=x`: a última linha do painel é `Agente consultor recebe a tarefa "Outro título" e vai triar.` e o estado do loop segue com `tarefa` `TLG-T9` (hoje o painel mostra "Um título de teste"). TR `test_tr_tarefa_do_despacho_ausente_segue_a_corrente` — o revisor com o prompt `Revise.` e o planejador com `despacho: P-9999`, quebra, `Planeje.`: as linhas são `Agente revisor recebe a tarefa "Um título de teste" e vai confrontar a entrega com o card.` e `Agente planejador recebe a tarefa "Um título de teste" e vai replanejar.` (a regra concorrente, exigir a linha com tarefa, perderia o título). Suíte `tests/test_progresso_hook.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_progresso_hook.py -q -k tarefa_do_despacho` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - painel do gerente.tarefa mostrada — mostra a tarefa que a linha de abertura do despacho declara — Verificação 1
- **Fora do escopo desta tarefa:** a série de telemetria (`RAF-T31`); a regra da linha de abertura (`RAF-T33`) e o despacho do consultor com ela (`RAF-T34`).
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** .claude/tools/progresso_hook.py:202 tarefa_do_despacho; os ramos PreToolUse e PostToolUse síncrono · Agent de evento tiram a tarefa da linha de abertura do despacho
  - **Contrato:** o ramo UserPromptSubmit segue com tarefa_corrente
  - **Não refazer:** nada a declarar
  - **Pendente:** o retorno assíncrono (hand-back) ainda usa tarefa_corrente; o ramo PostToolUse síncrono sem teste; ID sem card mostra o ID (achado do laudo, ao consultor)

### RAF-T32a — O painel do gerente mostra a tarefa despachada também no retorno por hand-back [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa faz a frase de volta do subagente que devolve por hand-back nomear a tarefa que a linha de abertura do despacho declarou, como já fazem a frase de despacho e a de volta síncrona.
- **Fundamento:** `DRF-72`; `AE-193` (laudo da `RAF-T32`, ressalva 91, achado 2); `DRF-71`; `DRF-18`; relatório `R-16`.
- **Depende de:** `RAF-T32`
- **Operação do modelo:** `OP-32`
  - OP-32: Quem executa faz o painel do gerente mostrar a tarefa que a abertura do despacho declara, e não a tarefa corrente do loop.
  - precisa de: série de telemetria — Quem implementa faz o registro ler o plano e a tarefa na primeira linha do despacho e ganhar uma coluna que identifica o agente, completando as linhas antigas.; despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/progresso_hook.py`, função `evento`: o ramo `PostToolUse` · `Agent` com `handback` `send` (hoje só grava `pendentes[agentId] = sub`, linha 495) e o ramo `UserPromptSubmit` com `<agent-message from="…">` (a atribuição `_, titulo, _ = tarefa_corrente(estado_loop, estado, raiz)` da linha 516). A `RAF-T32` levou a linha de abertura ao `PreToolUse` e ao `PostToolUse` síncrono e excluiu o `UserPromptSubmit`, onde mora a frase de volta do hand-back — o caminho real quando o subagente devolve por `SubagentHandback`: hoje o painel diz `Agente consultor recebe a tarefa "Outro título"` e, na volta, `Agente consultor devolveu a tarefa "Um título de teste"` (medido). O ID sem card segue mostrando o ID (`DRF-72`): não muda. O estado do loop (`tarefa`, `titulo`, `objetivo`, `pendentes`) não muda pela linha. As frases `M-3`..`M-16` não mudam de texto. O contrato do objeto é: "Quem implementa faz o painel ler a mesma linha de abertura do despacho antes de recorrer à tarefa corrente."
- **Arquivos-alvo:**
  - `.claude/tools/progresso_hook.py`
  - `tests/test_progresso_hook.py`
- **Contratos/classes:** duas regras em `evento`, sem função nova:
  1. Ramo `PostToolUse` · `Agent` com `handback` `send`: depois de `pendentes[agentId] = sub` (que fica como está), quando `tarefa_do_despacho(str(ti.get("prompt", "")), raiz)` devolve o trio, grava o título dele em `estado_loop["titulos_pendentes"][agentId]` (chave nova, criada com `setdefault`); sem a linha, não grava nada. O valor de `pendentes` segue string (os testes de hoje comparam `pendentes` inteiro).
  2. Ramo `UserPromptSubmit` com `<agent-message from="<agentId>">`: tira `titulos_pendentes[agentId]` junto com `pendentes[agentId]` (os dois `pop`, sempre, antes do teste do papel); o título da frase de volta é o tirado de `titulos_pendentes` e, sem ele, o de `tarefa_corrente(estado_loop, estado, raiz)`, como hoje.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_progresso_hook.py`, depois da última linha de hoje (o `)` que fecha o último `assert` de `test_tr_tarefa_do_despacho_ausente_segue_a_corrente`), o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card).

     ```python


     def _devolver_agente(estado, raiz, sub, prompt, resposta, agent_id=None):
         if agent_id is None:
             r = {"content": [{"type": "text", "text": resposta}]}
         else:
             r = {"status": "completed", "agentId": agent_id, "handback": "send",
                  "content": [{"type": "text", "text": "ptr"}]}
         rodar(P(hook_event_name="PostToolUse", tool_name="Agent",
                 tool_input={"subagent_type": sub, "prompt": prompt}, tool_response=r), estado, raiz)
         if agent_id is not None:
             rodar(P(hook_event_name="UserPromptSubmit", prompt=(
                 f'<agent-message from="{agent_id}">\n'
                 "[Subagent hand-back] The text below is the final report of a subagent this "
                 "session delegated to. The report follows:\n"
                 f"  {resposta}\n"
                 "</agent-message>"
             )), estado, raiz)
         return progresso(estado)[-1]


     def test_tf_retorno_do_despacho_assincrono_mostra_a_tarefa_despachada(estado, raiz):
         rodar(payload_next(
             "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
             "- **Objetivo:** Fazer x.\n"
         ), estado, raiz)

         ultima = _devolver_agente(
             estado, raiz, "pantonic-consultant", "despacho: P-9999 TLG-T10\ncenario=x",
             "rota=resolve", agent_id="c9",
         )

         assert ultima == 'Agente consultor devolveu a tarefa "Outro título": rota resolve.'
         estado_loop = json.loads((estado / progresso_hook.ESTADO_ARQ).read_text(encoding="utf-8"))
         assert estado_loop["tarefa"] == "TLG-T9"
         assert estado_loop["pendentes"] == {}
         assert estado_loop.get("titulos_pendentes", {}) == {}


     def test_tr_retorno_do_despacho_sincrono_mostra_a_tarefa_despachada(estado, raiz):
         rodar(payload_next(
             "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
             "- **Objetivo:** Fazer x.\n"
         ), estado, raiz)

         assert _devolver_agente(
             estado, raiz, "pantonic-consultant", "despacho: P-9999 TLG-T10\ncenario=x", "rota=resolve",
         ) == 'Agente consultor devolveu a tarefa "Outro título": rota resolve.'
         assert _devolver_agente(
             estado, raiz, "pantonic-consultant", "cenario=x", "rota=resolve",
         ) == 'Agente consultor devolveu a tarefa "Um título de teste": rota resolve.'
     ```
  2. Rodar `python -m pytest tests/test_progresso_hook.py -q -k retorno_do_despacho` e conferir `1 failed, 1 passed`: o TF falha (a volta diz "Um título de teste") e o TR passa (o ramo síncrono já lê a linha, `RAF-T32`).
  3. Aplicar as duas regras de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `tests/test_progresso_hook.py` com `47 passed`, 2026-09-29).
  - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Nenhuma linha que já existia em `tests/test_progresso_hook.py` sai ou muda: o card só acrescenta ao fim do arquivo. Os dois arquivos seguem LF (hoje 0 CR).
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não importar o `telemetria_hook.py`; não gravar a tarefa da linha em `estado_loop["tarefa"]`, `titulo` ou `objetivo`; não mudar a forma do valor de `pendentes`; não mudar `tarefa_do_despacho`, `tarefa_corrente` nem `localizar_card`; não mudar o texto de nenhuma frase do repertório nem a tabela da skill `scrum-master`.
- **Contingências:**
  - se um teste que já existia em `tests/test_progresso_hook.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_retorno_do_despacho_assincrono_mostra_a_tarefa_despachada` — com a `TLG-T9` como corrente, o consultor despachado com `despacho: P-9999 TLG-T10` devolve por hand-back `rota=resolve`: a última linha do painel é `Agente consultor devolveu a tarefa "Outro título": rota resolve.`, o estado segue com `tarefa` `TLG-T9` e sem pendência (hoje a volta diz "Um título de teste"). TR `test_tr_retorno_do_despacho_sincrono_mostra_a_tarefa_despachada` — a volta síncrona com a linha diz "Outro título" e sem ela "Um título de teste" (cobre o ramo que a `RAF-T32` mudou sem teste). Suíte `tests/test_progresso_hook.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_progresso_hook.py -q -k retorno_do_despacho` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - painel do gerente.tarefa mostrada — a frase de volta do hand-back mostra a tarefa que a linha de abertura do despacho declara — Verificação 1
- **Fora do escopo desta tarefa:** o texto da `RAF-T32` (`done`), que fica como executado; o ID sem card na linha (`DRF-72`); a regra da linha de abertura (`RAF-T33`) e o despacho do consultor com ela (`RAF-T34`); o vermelho do `dead_code` pela sonda (`AE-192`, `DRF-44`).
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** .claude/tools/progresso_hook.py: PostToolUse · Agent com hand-back grava titulos_pendentes[agentId] e o UserPromptSubmit <agent-message> usa esse título; tests/test_progresso_hook.py com TF assíncrono e TR síncrono
  - **Contrato:** pendentes segue string; sem título guardado, recorre a tarefa_corrente
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum

### RAF-T33 — A norma de consumo manda todo despacho de subagente abrir com a linha que declara plano e tarefa [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa escreve na norma de consumo do kit a regra de que todo despacho de subagente abre com a linha que declara o plano e a tarefa.
- **Fundamento:** `DRF-18` (a regra da linha mora em `GOVERNANCA.md` §4.2, residência da doutrina de telemetria), `DRF-39`; `F-26`; relatório `R-16` (auditoria reg. 41 e 54).
- **Depende de:** `RAF-T31`, `RAF-T32`
- **Operação do modelo:** `OP-33`
  - OP-33: Quem executa escreve na norma de consumo do kit a regra de que todo despacho de subagente abre com a linha que declara o plano e a tarefa.
  - precisa de: série de telemetria — Quem implementa faz o registro ler o plano e a tarefa na primeira linha do despacho e ganhar uma coluna que identifica o agente, completando as linhas antigas.; painel do gerente — Quem implementa faz o painel ler a mesma linha de abertura do despacho antes de recorrer à tarefa corrente.
- **Camada e fronteira:** doutrina do kit — `GOVERNANCA.md`, §4.2 (*Diário de obras*), bullet `- **Fonte única da série**`; nenhum código muda. O comportamento que a norma descreve já está nos instrumentos: o hook `SubagentStop` lê a linha `despacho: <P-id>[ <ID>]` da primeira mensagem antes de `tarefa-corrente.json` e antes do primeiro id de plano citado, e grava uma linha por agente com a coluna `agente` (`RAF-T31`); o painel mostra a tarefa que a linha declara (`RAF-T32`); o `despachar` já imprime a linha no texto pronto ao executor (`RAF-T3`). A regra mora só neste bullet; a skill `scrum-master` passa a despachar o consultor com ela na `RAF-T34`, remetendo a este bullet. O contrato do objeto é: "Quem implementa escreve a regra num lugar só, e os demais textos apontam para ela."
- **Arquivos-alvo:**
  - `GOVERNANCA.md`
- **Passos:**
  1. No bullet `- **Fonte única da série**` do §4.2 de `GOVERNANCA.md`, trocar o trecho antigo 1 pelo novo 1, na mesma linha, sem quebra nova e sem refluxo.

     Trecho antigo 1:

     ```text
     (append-only, colunas `data`, `projeto`,
     ```

     Trecho novo 1:

     ```text
     (colunas `data`, `projeto`,
     ```
  2. No mesmo bullet, trocar o trecho antigo 2 pelo novo 2, na mesma linha, sem quebra nova e sem refluxo.

     Trecho antigo 2:

     ```text
     nao_medido}`)
     ```

     Trecho novo 2:

     ```text
     nao_medido}`, `agente`)
     ```
  3. No fim do mesmo bullet, trocar as duas linhas do texto antigo pelas oito do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os dois espaços iniciais que já tem no arquivo).

     Texto antigo:

     ```text
       `<P-n>-scout` pelo primeiro id de plano da primeira mensagem do subagente, e
       `sem-id-<papel>` quando não há id a derivar.
     ```

     Texto novo:

     ```text
       `<P-n>-scout`, e `sem-id-<papel>` quando não há id a derivar. **Linha de abertura do
       despacho** (`R-16` da auditoria final, `P-0755`): todo despacho de subagente abre com a
       linha `despacho: <P-id>`, seguida de um espaço e do id da tarefa ou do tíquete quando
       houver; o hook lê o plano e a tarefa nela antes de `tarefa-corrente.json` e antes do
       primeiro id de plano citado na primeira mensagem, que só valem sem ela, e o painel do
       gerente mostra a tarefa que ela declara. A série guarda uma linha por agente, a última e
       acumulada, com o nome do agente na coluna `agente` (`-` nas linhas anteriores à coluna e
       nas gravadas sem agente).
     ```
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_doutrina_unidade.py` lê `GOVERNANCA.md`.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer nos outros bullets do §4.2 nem nas outras frases do bullet; não repetir a regra na skill `scrum-master`, em agente ou no `README.md` (a skill remete a este bullet na `RAF-T34`); não editar `docs/telemetria.tsv`.
- **Contingências:**
  - se um dos três textos antigos não existir verbatim, uma única vez, em `GOVERNANCA.md` → parar e sinalizar `blocked` razão `premissa`, colando o bullet `- **Fonte única da série**` inteiro.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê o arquivo.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('GOVERNANCA.md').read_text(encoding='utf-8');print('abertura=%d-%d'%(t.count('pelo primeiro id de plano da primeira mensagem do subagente'),t.count('todo despacho de subagente abre com a')))"` → `abertura=0-1` — antes `abertura=1-0`, depois `abertura=0-1`
- **Pronto quando:**
  - norma de consumo do kit.linha de abertura do despacho — todo despacho de subagente abre com uma linha que declara o plano e, quando houver, a tarefa ou o tíquete; a regra mora num lugar só — Verificação 1
- **Fora do escopo desta tarefa:** a mecânica do hook e do painel (`RAF-T31`, `RAF-T32`); o despacho do consultor com a linha e o aviso `B1` na skill (`RAF-T34`).
- **Handover:** 2026-09-29 · para quem vier depois
  - **Entregue:** GOVERNANCA.md, bullet Fonte única da série: sem 'append-only', coluna agente no esquema e o parágrafo 'Linha de abertura do despacho'
  - **Contrato:** todo despacho de subagente abre com a linha que declara plano e tarefa; a telemetria e o painel a leem
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum

### RAF-T34 — Quem conduz leva ao consultor a falha de instrumento que o fechamento avisa e a linha do card em triagem [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa ensina o gerente do loop a levar ao consultor a falha de instrumento que o fechamento avisa e a linha do card que ele vai triar.
- **Fundamento:** `DRF-18` (o consultor é despachado com a linha do card em triagem), `DRF-22` (a condição da `B1` ganha a linha `encerrar: B1 —` da saída do fechamento); `F-25` (a `B1` mora só na skill), `F-26` (o consultor recebe o card pelo texto da skill); relatório `R-20` (auditoria reg. 47) e `R-16` (reg. 54).
- **Depende de:** `RAF-T30`, `RAF-T30a`, `RAF-T33`
- **Operação do modelo:** `OP-34`
  - OP-34: Quem executa ensina o gerente do loop a levar ao consultor a falha de instrumento que o fechamento avisa e a linha do card que ele vai triar.
  - precisa de: fechamento — Quem implementa recebe o comando que hoje só grava o veredito do marco e confere achados por semelhança de texto, e acrescenta o que a operação pede.; norma de consumo do kit — Quem implementa escreve a regra num lugar só, e os demais textos apontam para ela.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.
- **Camada e fronteira:** doutrina do kit — a skill `scrum-master`: a linha da regra `B1` na tabela `### Bloco B — continuar ou encerrar a janela` e o molde do despacho na seção `## Acionamento do consultor`; nenhum código muda. O comportamento que a doutrina descreve já está nos instrumentos: o `encerrar.py tarefa` imprime, antes da linha final, `encerrar: B1 — achado de instrumento com falha: <texto>` para cada achado de laudo de alvo `instrumento` que relata queda, traceback, exceção ou erro (`RAF-T30`); o hook de telemetria e o painel leem a linha `despacho: <P-id>[ <ID>]` da primeira mensagem (`RAF-T31`, `RAF-T32`), cuja regra mora em `GOVERNANCA.md` §4.2 (`RAF-T33`). A skill remete à governança e não repete a regra. O contrato do objeto é: "Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só."
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
- **Passos:**
  1. Na linha da regra `B1` (a que começa por `` | `B1` | **pendência substantiva**: ``), trocar o trecho antigo 1 pelo novo 1, na mesma linha, sem quebra nova e sem refluxo.

     Trecho antigo 1:

     ```text
     integralmente atribuível a arquivo fora dos alvos por `B0` |
     ```

     Trecho novo 1:

     ```text
     integralmente atribuível a arquivo fora dos alvos por `B0`, **ou** linha `encerrar: B1 — achado de instrumento com falha: <texto>` na saída do `encerrar.py tarefa`, qualquer que seja a recomendação do laudo (`R-20` da auditoria final, `P-0755`) |
     ```
  2. Na seção `## Acionamento do consultor`, trocar as três linhas do texto antigo 2 pelas quatro do texto novo 2 (as quebras são as do bloco; cada linha perde o recuo deste card, e a linha do molde guarda os quatro espaços iniciais que tem no bloco).

     Texto antigo 2:

     ```text
     Molde do despacho — as três entradas, e nada além delas:

         cenario=docs/plans/P-<n>-<slug>/cenario.md
     ```

     Texto novo 2:

     ```text
     Molde do despacho — a linha de abertura com o card em triagem (`GOVERNANCA.md` §4.2, *Linha de abertura do despacho*; `R-16` da auditoria final, `P-0755`) e as três entradas, e nada além delas:

         despacho: P-<n> <ID do card em triagem>
         cenario=docs/plans/P-<n>-<slug>/cenario.md
     ```
  3. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_progresso_hook.py` lê esta skill (tabela do repertório `M-0`..`M-18`), que os passos não tocam.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer nas outras regras dos blocos A e B nem no resto do molde; não repetir a regra da linha de abertura (ela mora em `GOVERNANCA.md` §4.2); não mexer no repertório de mensagens; não editar `.claude/tools/encerrar.py` (`RAF-T30`).
- **Contingências:**
  - se o trecho antigo 1 ou o texto antigo 2 não existir verbatim, uma única vez, em `.claude/skills/scrum-master/SKILL.md` → parar e sinalizar `blocked` razão `premissa`, nomeando o passo.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_progresso_hook.py` lê a skill.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('b1=%d'%t.count('qualquer que seja a recomendação do laudo'))"` → `b1=1` — antes `b1=0`, depois `b1=1`
  2. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('molde=%d'%t.count('    despacho: P-<n> <ID do card em triagem>'))"` → `molde=1` — antes `molde=0`, depois `molde=1`
- **Pronto quando:**
  - gerente do loop.falha de instrumento levada ao consultor — o aviso de falha que o fechamento imprime também leva a tarefa ao consultor — Verificação 1
  - gerente do loop.card entregue ao consultor — o consultor é despachado com a linha que declara o card em triagem — Verificação 2
- **Fora do escopo desta tarefa:** o aviso no fechamento (`RAF-T30`); a regra da linha de abertura (`RAF-T33`); a origem citada pelo consultor (`RAF-T35`).
- **Handover:** 2026-09-30 · para quem vier depois
  - **Entregue:** .claude/skills/scrum-master/SKILL.md: quem conduz leva ao consultor a falha de instrumento que o fechamento avisa (encerrar: B1) e o molde do despacho do consultor abre com 'despacho: P-<n> <ID do card em triagem>'
  - **Contrato:** o aviso B1 do encerrar.py vira acionamento do consultor; a linha de abertura atribui a telemetria e o painel
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum

### RAF-T35 — O consultor cita no achado a linha do laudo de onde ele veio [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa ensina o consultor a citar a origem no laudo de todo achado que ele registra ou reescreve a partir dele.
- **Fundamento:** `DRF-21` (o consultor, ao registrar ou reescrever `AE-` a partir de achado de laudo, cita a mesma origem); `F-25` (nenhuma `AE-` traz origem; a reescrita do consultor escapa da dedupe por texto); relatório `R-19` (auditoria reg. 39).
- **Depende de:** `RAF-T30`
- **Operação do modelo:** `OP-35`
  - OP-35: Quem executa ensina o consultor a citar a origem no laudo de todo achado que ele registra ou reescreve a partir dele.
  - precisa de: fechamento — Quem implementa recebe o comando que hoje só grava o veredito do marco e confere achados por semelhança de texto, e acrescenta o que a operação pede.; consultor — Quem implementa acrescenta à definição do agente as duas formas de linha que as operações pedem, sem mudar a triagem.
- **Camada e fronteira:** doutrina do kit — a definição do agente consultor, `.claude/agents/pantonic-consultant.md`, item 3 (*Repara o plano e devolve o dossiê de modelo*); nenhum código muda. O mecanismo que a regra usa já existe desde a `RAF-T30`: o `encerrar.py tarefa` grava no fim de cada `AE-` que vem do laudo ` **Origem:** ` seguido de `laudo:<TAREFA>#<n>` entre crases (`<n>` = posição da linha na tabela `## Achado de processo`) e pula o achado cuja origem, entre crases, já aparece em alguma `AE-` do plano. A regra mora só neste item do consultor; nenhum outro arquivo a repete. O contrato do objeto é: "Quem implementa acrescenta à definição do agente as duas formas de linha que as operações pedem, sem mudar a triagem."
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-consultant.md`
- **Passos:**
  1. No item 3 de `.claude/agents/pantonic-consultant.md` (uma linha só no arquivo), trocar o trecho antigo pelo novo, na mesma linha, sem quebra nova e sem refluxo.

     Trecho antigo:

     ```text
     fila reordenada, achado absorvido com ponteiro.
     ```

     Trecho novo:

     ```text
     fila reordenada, achado absorvido com ponteiro. Achado que você registra ou reescreve a partir de um laudo cita a origem no fim da entrada `AE-<n>`: ` **Origem:** ` seguido de `laudo:<TAREFA>#<n>` entre crases, com `<n>` a posição da linha na tabela `## Achado de processo` do laudo — a mesma origem que o `encerrar.py tarefa` grava e confere para não registrar o achado de novo (`R-19` da auditoria final, `P-0755`).
     ```
  2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_frontmatter_yaml.py` lê o frontmatter deste arquivo, que o passo não toca.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer na frase da validação no marco (`RAF-T26`) nem nas rotas da triagem; não reescrever `AE-` já registradas em plano nenhum; não editar `.claude/tools/encerrar.py` (`RAF-T30`).
- **Contingências:**
  - se o trecho antigo não existir verbatim, uma única vez, em `.claude/agents/pantonic-consultant.md` → parar e sinalizar `blocked` razão `premissa`, colando o item 3.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_frontmatter_yaml.py` lê o arquivo.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-consultant.md').read_text(encoding='utf-8');print('origem=%d'%t.count('cita a origem no fim da entrada'))"` → `origem=1` — antes `origem=0`, depois `origem=1`
- **Pronto quando:**
  - consultor.origem citada no achado — o achado cita a mesma origem no laudo que o fechamento usa — Verificação 1
- **Fora do escopo desta tarefa:** a gravação e a conferência da origem no fechamento (`RAF-T30`); a forma da validação no marco (`RAF-T26`).
- **Handover:** 2026-09-30 · para quem vier depois
  - **Entregue:** .claude/agents/pantonic-consultant.md, item 3: o consultor cita no achado a linha do laudo de onde ele veio
  - **Contrato:** achado absorvido pelo consultor carrega a origem no laudo
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum

### RAF-T36 — O planejador ganha a régua de profundidade pelo tamanho do plano [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa dá ao planejador uma régua de profundidade pelo tamanho do plano, que dispensa no plano de até cinco operações os itens que não mudam o resultado.
- **Fundamento:** `DRF-2`, `DRF-23` (o conteúdo da régua); `F-6` (o planejamento custou 352,2k de 1.250,0k do gasto de subagentes do plano fictício); `F-28` (a tabela de profundidade da Fase 4); relatório `R-21` (auditoria reg. 8 e 9).
- **Depende de:** `RAF-T29`, `RAF-T29a`, `RAF-T34`, `RAF-T35`
- **Operação do modelo:** `OP-36`
  - OP-36: Quem executa dá ao planejador uma régua de profundidade pelo tamanho do plano, que dispensa no plano de até cinco operações os itens que não mudam o resultado.
  - precisa de: escolhas do dono sobre o roteiro — Ninguém altera: fixam a rota das operações que dependem delas.; relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão.
- **Camada e fronteira:** doutrina do kit — a definição do agente planejador, `.claude/agents/pantonic-planner.md`, abertura da `### Fase 4 — Auto-auditoria (antes de gravar, uma passada)`: o parágrafo que começa por `**Profundidade pela classe do plano.**` e a tabela de três linhas que o segue; nenhum código muda. Primeira tarefa da etapa E: nasce `blocked` até o `go` do Marco 5 (`DRF-5`). A régua mora só nessa tabela; nenhum outro arquivo a repete. O contrato do objeto é: "Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão."
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md`
- **Passos:**
  1. Em `.claude/agents/pantonic-planner.md`, trocar o trecho antigo pelo novo, na mesma linha, sem quebra nova e sem refluxo.

     Trecho antigo:

     ```text
     **Profundidade pela classe do plano.**
     ```

     Trecho novo:

     ```text
     **Profundidade pela classe e pelo tamanho do plano.**
     ```
  2. No mesmo parágrafo, trocar o trecho antigo pelo novo, na mesma linha, sem quebra nova e sem refluxo.

     Trecho antigo:

     ```text
     tabela dispensa não se aplica, e a razão é a própria classe.
     ```

     Trecho novo:

     ```text
     tabela dispensa não se aplica, e a razão é a classe ou o tamanho. Plano cuja seção 1.2 tem até cinco operações usa a última coluna, qualquer que seja a classe declarada (`R-21` da auditoria final, `P-0755`): nesse tamanho, o parser frio, a segunda leva e o ensaio sem arquivo compartilhado não mudam o resultado, e o ensaio da contingência só o muda quando ela escreve arquivo.
     ```
  3. Trocar a tabela que segue o parágrafo (cinco linhas) pela tabela nova (as quebras são as do bloco; cada linha perde o recuo deste card e começa na coluna 0).

     Trecho antigo:

     ```text
     | itens | ferramentaria | doutrina | produto |
     |---|---|---|---|
     | 1 a 6 e 8 a 12 | aplicam | aplicam | aplicam |
     | 7 (parser frio) e 13 (segunda leva) | só com gramática ou tabela normativa no plano | só com gramática ou tabela normativa no plano | aplicam |
     | 14 (ensaio em cópia) | só com arquivo compartilhado tocado por dois cards | só com arquivo compartilhado tocado por dois cards | aplica |
     ```

     Trecho novo:

     ```text
     | itens | ferramentaria | doutrina | produto | até 5 operações, qualquer classe |
     |---|---|---|---|---|
     | 1 a 6 e 8 a 12 | aplicam | aplicam | aplicam | aplicam |
     | 7 (parser frio) e 13 (segunda leva) | só com gramática ou tabela normativa no plano | só com gramática ou tabela normativa no plano | aplicam | só com gramática ou tabela normativa no plano |
     | 14 (ensaio em cópia) | só com arquivo compartilhado tocado por dois cards | só com arquivo compartilhado tocado por dois cards | aplica | só com arquivo compartilhado tocado por dois cards; o ensaio da contingência, só quando a contingência escreve arquivo |
     ```
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_doutrina_unidade.py` lê este arquivo e recusa nele os literais `atômic`, `50%`, `~80 linhas`, `tabela de classes` e `tabela de tetos`, que o texto novo não tem.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não reescrever os itens 1 a 14 da Fase 4 nem o parágrafo **A contingência se ensaia** do item 14; não mexer na Fase 3a (`RAF-T37`) nem na Fase 5 (`RAF-T38`); não criar outra tabela nem repetir a régua em outro arquivo.
- **Contingências:**
  - se algum dos três trechos antigos não existir verbatim, uma única vez, em `.claude/agents/pantonic-planner.md` → parar e sinalizar `blocked` razão `premissa`, colando as linhas do parágrafo que começa por `**Profundidade pela` até o item 1 da Fase 4.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê o arquivo.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('regua=%d-%d'%(t.count('a razão é a própria classe'),t.count('até 5 operações, qualquer classe')))"` → `regua=0-1` — antes `regua=1-0`, depois `regua=0-1`
- **Pronto quando:**
  - planejador.profundidade do planejamento — uma régua pelo tamanho do plano dispensa, no plano de até cinco operações, os itens que não mudam o resultado — Verificação 1
- **Fora do escopo desta tarefa:** o pedido do planejador ao modelador (`RAF-T37`); a checagem de versão do kit (`RAF-T38`); a medida do ganho da `R-21` sobre o custo de planejamento, que é da condução no relatório do Marco 6 (§7).
- **Handover:** 2026-09-30 · para quem vier depois
  - **Entregue:** .claude/agents/pantonic-planner.md, Fase 4 (Auto-auditoria): a profundidade passa a ser pela classe e pelo tamanho do plano, com a régua que dispensa no plano de até cinco operações os itens que não mudam o resultado
  - **Contrato:** o planejador lê a régua de profundidade pelo tamanho do plano na Fase 4
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum

### RAF-T37 — O pedido do planejador ao modelador deixa de exigir caminho, linha e nome de comando [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa tira do pedido do planejador ao modelador a exigência de caminho, linha e nome de comando nas células descritivas do modelo.
- **Fundamento:** `DRF-24`; `F-28` (a Fase 3a não traz o pedido de caminho, o dossiê de autoria do plano fictício o pediu por conta própria e o modelador o recusou pela norma `TK-76`); relatório `R-22` (auditoria reg. 7).
- **Depende de:** `RAF-T36`
- **Operação do modelo:** `OP-37`
  - OP-37: Quem executa tira do pedido do planejador ao modelador a exigência de caminho, linha e nome de comando nas células descritivas do modelo.
  - precisa de: planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão.; modelador — Quem implementa troca a regra da promoção da versão aceita, que deixa de ser ato do modelador salvo no conflito.
- **Camada e fronteira:** doutrina do kit — a definição do agente planejador, `.claude/agents/pantonic-planner.md`, `### Fase 3a — Esqueleto e dossiê (SAÍDA 3)`, o parágrafo que começa por `Então **pare** e devolva, na linha de retorno, o dossiê` (os seis campos do dossiê `Ato de modelo` de `autoria`), campo `Restrição`; nenhum código muda. A norma `TK-76` mora na definição do modelador (`.claude/agents/pantonic-model-designer.md`: nas células descritivas não entram caminho de arquivo, número de linha, identificador de decisão, fato ou item, nome de instrumento nem remissão a outra seção), que este card não edita; o planejador passa a dizer, no próprio pedido, que não exige esses dados e onde eles moram. O contrato do objeto é: "Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão."
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md`
- **Passos:**
  1. Em `.claude/agents/pantonic-planner.md`, trocar o trecho antigo pelo novo, na mesma linha, sem quebra nova e sem refluxo.

     Trecho antigo:

     ```text
     `tarefas: <prefixo>-T<n>` para `OP-<n>`) e `Devolver` (a §1 inteira e a linha da versão 1).
     ```

     Trecho novo:

     ```text
     `tarefas: <prefixo>-T<n>` para `OP-<n>`; e nunca caminho de arquivo, número de linha nem nome de instrumento nas células descritivas do modelo — a norma `TK-76` do modelador os recusa, e essas residências vão à seção 2 do plano e à `Camada e fronteira` do card, `R-22` da auditoria final, `P-0755`) e `Devolver` (a §1 inteira e a linha da versão 1).
     ```
  2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_doutrina_unidade.py` lê este arquivo e exige nele `SAÍDA 3` e `Fase 3b`, que o passo não toca.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não editar `.claude/agents/pantonic-model-designer.md` (a norma `TK-76` fica onde está); não mexer nos outros cinco campos do dossiê nem no esqueleto da Fase 3a; não mexer na tabela de profundidade (`RAF-T36`) nem na Fase 5 (`RAF-T38`).
- **Contingências:**
  - se o trecho antigo não existir verbatim, uma única vez, em `.claude/agents/pantonic-planner.md` → parar e sinalizar `blocked` razão `premissa`, colando o parágrafo que começa por `Então **pare** e devolva`.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê o arquivo.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('contrato=%d'%t.count('do modelador os recusa'))"` → `contrato=1` — antes `contrato=0`, depois `contrato=1`
- **Pronto quando:**
  - planejador.pedido ao modelador — o roteiro diz que o pedido não exige caminho, linha nem nome de comando nas células descritivas, e que esses dados vão aos fatos do plano e ao card — Verificação 1
- **Fora do escopo desta tarefa:** a régua de profundidade (`RAF-T36`); a checagem de versão do kit (`RAF-T38`); a norma `TK-76` do modelador, que não muda.
- **Handover:** 2026-09-30 · para quem vier depois
  - **Entregue:** .claude/agents/pantonic-planner.md: o pedido do planejador ao modelador (dossiê de autoria) deixa de exigir caminho, linha e nome de comando
  - **Contrato:** o dossiê de autoria ao modelador fala do domínio, sem caminho, linha nem comando
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum

### RAF-T38 — Quem conduz roda a checagem de versão do kit antes do planejador, que a registra no cabeçalho [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa passa a quem conduz, antes do despacho do planejador, a checagem de versão do kit que o planejador hoje é mandado invocar.
- **Fundamento:** `DRF-25`, `DRF-42`; `F-27` (a Fase 5 manda o planejador invocar a skill; nenhum agente lista `Skill` no `tools:`; se a plataforma bloqueia skill em subagente não se verifica pelo repositório); relatório `R-23` (auditoria reg. 15).
- **Depende de:** `RAF-T37`
- **Operação do modelo:** `OP-38`
  - OP-38: Quem executa passa a quem conduz, antes do despacho do planejador, a checagem de versão do kit que o planejador hoje é mandado invocar.
  - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão.
- **Camada e fronteira:** doutrina do kit — duas residências, uma regra cada: a seção `## Quando roda` da skill `.claude/skills/checar-versao-kit/SKILL.md` (quando a checagem roda e quem a roda: a residência do momento, `DRF-25`) e a `### Fase 5 — Registro e parada` de `.claude/agents/pantonic-planner.md` (o que o planejador faz com o resultado); nenhum código muda. O frontmatter da skill (`description`) fica como está: o índice derivado `.claude/README.md` o espelha, e o `kit_check.ps1 -Mode check-drift` compara os dois. O `tools:` do planejador não ganha `Skill` (`DRF-25`). Os contratos dos objetos são: "Quem implementa escreve na própria rotina que quem conduz a roda antes de despachar o planejador e passa o resultado no pedido." e "Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão."
- **Arquivos-alvo:**
  - `.claude/skills/checar-versao-kit/SKILL.md`
  - `.claude/agents/pantonic-planner.md`
- **Passos:**
  1. Em `.claude/skills/checar-versao-kit/SKILL.md`, seção `## Quando roda`, trocar o trecho antigo (a primeira linha da seção) pelo novo, na mesma linha, sem quebra nova e sem refluxo.

     Trecho antigo:

     ```text
     Na criação/registro de todo plano novo (skill `diario-de-obras`, operação "1. Registrar plano").
     ```

     Trecho novo:

     ```text
     Na criação de todo plano novo: quem conduz a sessão a roda antes de despachar o planejador (`pantonic-planner`) e passa o resultado no pedido a ele, e o planejador o registra no campo `**Checagem de versão do kit:**` do cabeçalho do plano — subagente, o planejador não invoca skill (`R-23` da auditoria final, `P-0755`). Plano registrado sem planejador roda a checagem no registro (skill `diario-de-obras`, operação "1. Registrar plano").
     ```
  2. Em `.claude/agents/pantonic-planner.md`, `### Fase 5 — Registro e parada`, trocar o trecho antigo pelo novo, na mesma linha, sem quebra nova e sem refluxo.

     Trecho antigo:

     ```text
     atualize o próximo id no mesmo ato; invoque `checar-versao-kit`; se o plano é derivado de outro
     ```

     Trecho novo:

     ```text
     atualize o próximo id no mesmo ato; registre no cabeçalho do plano, no campo `**Checagem de versão do kit:**`, o resultado da checagem de versão que o pedido de quem conduz traz (quem conduz roda a skill `checar-versao-kit` antes de despachar o planejador, e nenhuma fase deste roteiro a chama; sem o resultado no pedido, o campo registra `não recebida no pedido`, `R-23` da auditoria final, `P-0755`); se o plano é derivado de outro
     ```
  3. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_doutrina_unidade.py` lê o planejador.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer no frontmatter da skill (o `description` que o `.claude/README.md` espelha) nem no resto da seção `## Quando roda`; não acrescentar `Skill` ao `tools:` de agente nenhum; não editar a skill `diario-de-obras`; não mexer no bloco **Árvore do** da Fase 5 (`RAF-T16`).
- **Contingências:**
  - se algum dos dois trechos antigos não existir verbatim, uma única vez, no seu arquivo → parar e sinalizar `blocked` razão `premissa`, colando a seção `## Quando roda` da skill e o primeiro parágrafo da Fase 5 do planejador.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê o planejador.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/skills/checar-versao-kit/SKILL.md').read_text(encoding='utf-8');print('momento=%d'%t.count('a roda antes de despachar o planejador'))"` → `momento=1` — antes `momento=0`, depois `momento=1`
  2. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('versao=%d-%d'%(t.count('invoque'),t.count('Checagem de versão do kit:')))"` → `versao=0-1` — antes `versao=1-0`, depois `versao=0-1`
- **Pronto quando:**
  - checagem de versão do kit.momento em que roda — a rotina diz que quem conduz a roda antes de despachar o planejador e passa o resultado no pedido — Verificação 1
  - planejador.checagem de versão registrada — o planejador registra no cabeçalho a checagem que recebe pronta no pedido, e nenhuma fase manda invocar rotina — Verificação 2
- **Fora do escopo desta tarefa:** a régua de profundidade e o pedido ao modelador (`RAF-T36`, `RAF-T37`); a linha da skill na tabela de skills do `README.md` (`RAF-T40`).
- **Handover:** 2026-09-30 · para quem vier depois
  - **Entregue:** .claude/skills/checar-versao-kit/SKILL.md e .claude/agents/pantonic-planner.md (Fase 5): quem conduz roda a checagem de versão do kit antes do planejador, que registra o resultado no cabeçalho do plano
  - **Contrato:** o planejador recebe a checagem de versão pronta e a registra no cabeçalho
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum

### RAF-T39 — A mensagem de marco abre nomeando a entrega e o pedido do dono que a originou [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa ensina o gerente do loop a abrir a mensagem de marco nomeando a entrega e o pedido do dono que a originou.
- **Fundamento:** `DRF-26`, `DRF-41`; `F-29` (o repertório de mensagens é gerado pelo gancho e não tem frase de marco; a forma do relatório de encerramento está na skill `scrum-master`); relatório `R-25` (auditoria reg. 46: a mensagem do Marco 2 do `P-0754` levou o dono a perguntar "Você está pedindo mais uma auditoria?").
- **Depende de:** `RAF-T36`
- **Operação do modelo:** `OP-39`
  - OP-39: Quem executa ensina o gerente do loop a abrir a mensagem de marco nomeando a entrega e o pedido do dono que a originou.
  - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** doutrina do kit — a skill `.claude/skills/scrum-master/SKILL.md`, seção `## Relatório de encerramento`, que o condutor escreve à mão ao parar a janela; nenhum código muda. O repertório de mensagens ao gerente (`## Repertório de mensagens ao gerente`, ids `M-0`..`M-18`) é gerado pelo gancho `.claude/tools/progresso_hook.py` e não muda. A parada de marco se reconhece pela nota da tarefa: a primeira tarefa de uma etapa nasce `blocked` com a nota `Marco <m>: aguarda o veredito do dono sobre a etapa <X>` (`DRF-5`). A regra mora só na subseção nova; nenhum outro arquivo a repete. O contrato do objeto é: "Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só."
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
- **Passos:**
  1. Em `.claude/skills/scrum-master/SKILL.md`, logo antes da linha `### Quando a janela fecha o PLANO, e não só a janela`, inserir o bloco abaixo seguido de uma linha vazia (as quebras são as do bloco; cada linha perde o recuo deste card e começa na coluna 0).

     ```text
     ### Quando a janela para num marco

     A janela para num marco quando a próxima tarefa do plano está `blocked` à espera do veredito do dono sobre um marco da tabela de marcos do cabeçalho do plano (nota `Marco <m>: …`). Nessa parada, a primeira linha do relatório, antes da saída do `modelo.py show`, nomeia a entrega e o pedido do dono que a originou, na forma `"<entrega>", que você pediu em <data> ("<trecho verbatim do pedido, até 15 palavras>")`: a entrega é a célula *o que o dono lê* da linha do marco na tabela de marcos (plano sem tabela de marcos: o título do plano), e o pedido é a data e um trecho verbatim do ato do dono na seção 0 do plano (`R-25` da auditoria final, `P-0755`). Exemplo, no Marco 2 do `P-0755`: `"etapa A, custo da orquestração", que você pediu em 2026-09-28 ("faça double check dos achados, e elabore um plano de atuação")`. Sem essa linha, o dono já leu uma mensagem de marco e perguntou se lhe pediam mais uma auditoria.
     ```
  2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_progresso_hook.py` lê esta skill (tabela do repertório `M-0`..`M-18`), que o passo não toca.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer no primeiro parágrafo nem na lista do `## Relatório de encerramento`; não acrescentar linha ao repertório de mensagens (é gerado pelo gancho); não editar `.claude/tools/progresso_hook.py`.
- **Contingências:**
  - se a linha `### Quando a janela fecha o PLANO, e não só a janela` não existir, uma única vez, em `.claude/skills/scrum-master/SKILL.md` → parar e sinalizar `blocked` razão `premissa`, colando a seção `## Relatório de encerramento` inteira.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_progresso_hook.py` lê a skill.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('marco=%d'%t.count('Quando a janela para num marco'))"` → `marco=1` — antes `marco=0`, depois `marco=1`
- **Pronto quando:**
  - gerente do loop.abertura da mensagem de marco — a mensagem de marco abre nomeando a entrega e citando, com a data e poucas palavras do dono, o pedido que a originou — Verificação 1
- **Fora do escopo desta tarefa:** a linha do `README.md` sobre a parada de marco (`RAF-T40`); a medida de que a próxima mensagem de marco sai sem pergunta de esclarecimento, que é da condução no Marco 6.
- **Handover:** 2026-09-30 · para quem vier depois
  - **Entregue:** .claude/skills/scrum-master/SKILL.md: subseção nova '### Quando a janela para num marco', antes de '### Quando a janela fecha o PLANO': a mensagem de marco abre nomeando a entrega e o pedido do dono que a originou
  - **Contrato:** a mensagem de marco abre com a entrega e o pedido datado do dono
  - **Não refazer:** nada a declarar
  - **Pendente:** ambiguidade da célula do marco e remissão no primeiro parágrafo do Relatório de encerramento (achado do laudo, ao consultor)

### RAF-T39a — A abertura de marco nomeia a etapa, e o primeiro parágrafo do relatório remete a ela [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa corrige a subseção de abertura de marco da skill `scrum-master` para que a entrega seja o nome da etapa na tabela de marcos, e faz o primeiro parágrafo do relatório de encerramento remeter à linha que vem antes da saída do `modelo.py show`.
- **Fundamento:** `DRF-75`, `DRF-41`; `AE-204` (laudo da `RAF-T39`, ressalva 88, achado 2): a subseção manda a entrega ser a célula *o que o dono lê* inteira, o exemplo do Marco 2 usa só o trecho antes dos dois-pontos e a célula do Marco 1 do `P-0755` é um comando; o primeiro parágrafo do `## Relatório de encerramento` segue dizendo que o relatório abre com a saída do `modelo.py show`.
- **Depende de:** `RAF-T39`
- **Operação do modelo:** `OP-39`
  - OP-39: Quem executa ensina o gerente do loop a abrir a mensagem de marco nomeando a entrega e o pedido do dono que a originou.
  - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** doutrina do kit — a skill `.claude/skills/scrum-master/SKILL.md`, seção `## Relatório de encerramento`: o primeiro parágrafo e a subseção `### Quando a janela para num marco`, que a `RAF-T39` escreveu; nenhum código muda. A regra segue morando só na subseção; o primeiro parágrafo ganha uma remissão, não a regra, e a remissão não repete o nome da subseção (a Verificação da `RAF-T39` conta uma ocorrência dele). O contrato do objeto é: "Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só."
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
- **Passos:**
  1. Em `.claude/skills/scrum-master/SKILL.md`, fazer as duas trocas abaixo, cada uma na mesma linha do trecho antigo, sem quebra nova e sem refluxo; cada trecho antigo existe uma única vez no arquivo.

     Troca 1, primeiro parágrafo do `## Relatório de encerramento`. Trecho antigo:

     ```text
     .claude/tools/modelo.py show --plano <plano>` — a
     ```

     Trecho novo:

     ```text
     .claude/tools/modelo.py show --plano <plano>` (na parada de marco, logo depois da linha que nomeia a entrega, na subseção abaixo) — a
     ```

     Troca 2, subseção da parada de marco. Trecho antigo:

     ```text
     a entrega é a célula *o que o dono lê* da linha do marco na tabela de marcos (plano sem tabela de marcos: o título do plano)
     ```

     Trecho novo:

     ```text
     a entrega é o nome da etapa na célula *o que o dono lê* da linha do marco na tabela de marcos, o trecho antes dos dois-pontos, sem a lista que os segue (marco cuja célula não nomeia etapa, como o do modelo, que cita o comando `modelo.py show`, ou plano sem tabela de marcos: o título do plano)
     ```
  2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `630 passed`, 2026-09-30, laudo da `RAF-T39`). `tests/test_progresso_hook.py` lê esta skill (tabela do repertório `M-0`..`M-18`), que o passo não toca.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer na lista do `## Relatório de encerramento` nem no primeiro parágrafo além da troca 1; não repetir a regra da subseção em outro trecho; não acrescentar linha ao repertório de mensagens (é gerado pelo gancho); não editar `.claude/tools/progresso_hook.py`.
- **Contingências:**
  - se um dos dois trechos antigos não existir, ou existir mais de uma vez, em `.claude/skills/scrum-master/SKILL.md` → parar e sinalizar `blocked` razão `premissa`, colando a seção `## Relatório de encerramento` inteira.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_progresso_hook.py` lê a skill.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('marco=%d-%d-%d-%d'%(t.count('Quando a janela para num marco'),t.count('logo depois da linha que nomeia a entrega'),t.count('o trecho antes dos dois-pontos'),t.count('a entrega é a célula')))"` → `marco=1-1-1-0` — antes `marco=1-0-0-1`, depois `marco=1-1-1-0`
- **Pronto quando:**
  - gerente do loop.abertura da mensagem de marco — a mensagem de marco abre nomeando a etapa entregue, sem a lista de recomendações, e o parágrafo que manda o relatório abrir pela saída do `modelo.py show` remete a essa linha — Verificação 1
- **Fora do escopo desta tarefa:** o texto da `RAF-T39` (`done`), que fica como executado; a linha do `README.md` sobre a parada de marco (`RAF-T40`); a medida de que a próxima mensagem de marco sai sem pergunta de esclarecimento, que é da condução no Marco 6.
- **Handover:** 2026-09-30 · para `RAF-T40`
  - **Entregue:** .claude/skills/scrum-master/SKILL.md: a abertura de marco nomeia a etapa (trecho da célula antes dos dois-pontos; sem etapa, o título do plano) e o primeiro parágrafo do Relatório de encerramento remete à exceção do marco
  - **Contrato:** a mensagem de marco nomeia a etapa e o pedido datado do dono
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum

### RAF-T40 — O guia de entrada descreve o kit como ele fica depois das cinco etapas [Sonnet · esforço medium · classe redacao]
- **Objetivo:** Quem executa revisa o guia de entrada do kit para que ele descreva o kit como fica depois das cinco etapas.
- **Fundamento:** `DRF-34`, `DRF-40`; `F-4` (o `README.md` cita dez instrumentos em doze linhas; `card_check.py` e `telemetria_hook.py` sem menção; `check-readme.ps1` sai 0); G-README dever 2 (toda sprint termina com a revisão do `README.md`); invariante 10 da §4 (o veredito do dono sobre a revisão é gate do Marco 6, não critério de pronto).
- **Depende de:** `RAF-T38`, `RAF-T39`, `RAF-T39a`, `RAF-T22a`
- **Operação do modelo:** `OP-40`
  - OP-40: Quem executa revisa o guia de entrada do kit para que ele descreva o kit como fica depois das cinco etapas.
  - precisa de: medidor de custo da sessão — Quem implementa parte dos dois rascunhos da auditoria, sem mexer neles, e entrega um comando com teste que serve a tarefa de qualquer plano.; despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; gatilho do próximo passo — Quem implementa faz o gatilho reconhecer quem escreveu a mensagem antes de procurar a frase, com testes próprios.; filtro da saída dos testes — Quem implementa corrige o filtro na cópia que o kit guarda; levá-lo à máquina do dono é ato do próprio dono.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.; conferência de verificação do card — Quem implementa amplia o que a conferência aceita sem deixar de ler os cards já escritos na forma antiga.; medida gravada do card — Quem implementa muda onde e com que nome a medida se grava, e faz o revisor achar tanto a nova quanto as vinte já gravadas com o nome antigo.; conferência do modelo — Quem implementa acrescenta à conferência o que cada operação pede e mantém o que ela já julga quando chamada como hoje, com uma só mudança: enquanto houver versão pendente, o card que cita uma operação que só ela tem deixa de ser recusado.; fechamento — Quem implementa recebe o comando que hoje só grava o veredito do marco e confere achados por semelhança de texto, e acrescenta o que a operação pede.; pré-voo do pedido — Quem implementa muda só a leitura do que é caminho e a classificação do que falta, com os testes que a provam.; controle do backlog — Quem implementa acrescenta um aviso ao tirar o plano da fila e uma recusa ao conferir, sem mudar o resultado do primeiro.; série de telemetria — Quem implementa faz o registro ler o plano e a tarefa na primeira linha do despacho e ganhar uma coluna que identifica o agente, completando as linhas antigas.; painel do gerente — Quem implementa faz o painel ler a mesma linha de abertura do despacho antes de recorrer à tarefa corrente.
- **Camada e fronteira:** documentação pública — o `README.md` da raiz, seções `## 6. O loop de execução`, `### 8.1 O modelo de domínio do plano — o que o dono lê`, `## 9. O fechamento de tarefa e uma tarefa por contexto`, `## 11. Anatomia do kit` e `## 12. Memória e telemetria`; nenhum código muda. O que cada troca descreve já está entregue pelos cards `RAF-T1`..`RAF-T39`: a janela nova do loop (`RAF-T1`); o medidor `custo_sessao.py` com os verbos `medir` e `passos` (`RAF-T2`); o pacote da tarefa em arquivo e o texto pronto do despacho (`RAF-T3`, `RAF-T4`); o gatilho que só responde ao dono (`RAF-T5`); a evidência com curinga de shell, caminho acentuado e linhas removidas dos testes (`RAF-T9`..`RAF-T11`); as formas novas do `card_check.py` e a medida com o mundo no nome (`RAF-T13`..`RAF-T15`); o `modelo.py check --so-vigente`, a violação do texto copiado e o drift por texto (`RAF-T19`..`RAF-T22`); a promoção no `encerrar.py marco` com `--consultor` (`RAF-T23`); o status `criar` do `prevoo.py` (`RAF-T27`); o aviso do `drain` e a violação `C-18` do `check` (`RAF-T28`, `RAF-T29`); a origem do achado e a linha `encerrar: B1 —` (`RAF-T30`); a série de telemetria com a coluna `agente` e uma linha por agente (`RAF-T31`); a checagem de versão rodada por quem conduz (`RAF-T38`); a abertura da mensagem de marco (`RAF-T39`, `RAF-T39a`). Os comandos do kit que o guia cita são os onze de `DRF-40`: os dez que `F-4` conferiu e o `custo_sessao.py`. O índice derivado `.claude/README.md` não se edita. O contrato do objeto é: "Quem implementa revisa o guia contra o kit como ele fica depois das cinco etapas, incluindo os dois comandos que ele ainda não cita."
- **Arquivos-alvo:**
  - `README.md`
- **Passos:**
  1. Em `README.md`, fazer as dezesseis trocas abaixo, cada uma na mesma linha do trecho antigo, sem quebra nova e sem refluxo; cada trecho antigo existe uma única vez no arquivo.

     Troca 1, `## 6`, parágrafo **O que é** (a janela nova). Trecho antigo:

     ```text
     com a primeira linha gerada). No fim da janela, o gerente lê um relatório.
     ```

     Trecho novo:

     ```text
     com a primeira linha gerada). No fim da janela, o gerente lê um relatório. O loop de um plano recém-planejado abre numa janela nova, com o plano gravado como único insumo: a janela que planejou encerra no Marco 1.
     ```

     Troca 2, `## 6`, **Passo 4 — gate de delegação** (o pacote do despacho). Trecho antigo:

     ```text
     aberto é devolvida ao planejamento.
     ```

     Trecho novo:

     ```text
     aberto é devolvida ao planejamento. Passados os gates, o despacho grava o pacote da tarefa — o card, os handovers, a leitura do modelo e as âncoras conferidas no arquivo de hoje — num arquivo fora do versionamento, e quem conduz repassa ao executor só o texto pronto do despacho que o comando imprime, sem reconferir âncora à mão.
     ```

     Troca 3, `### 8.1` (a promoção da versão aceita). Trecho antigo:

     ```text
     que o dono aceita ou recusa.
     ```

     Trecho novo:

     ```text
     que o dono aceita ou recusa; no aceite, o comando do marco promove a versão aceita, cobrando a linha de validação do consultor, e só chama o modelador quando encontra conflito.
     ```

     Troca 4, `### 8.1` (o `check`). Trecho antigo:

     ```text
     pendente (`check`) e gera a leitura do dono (`show`), que abre pelo estágio atual e, com `--drift`,
     ```

     Trecho novo:

     ```text
     pendente (`check`; com `--so-vigente`, que o despacho usa, só a vigente, e a pendente fica para o marco), recusa o card cujo texto copiado da operação difere do da versão que ele cita e gera a leitura do dono (`show`), que abre pelo estágio atual e, com `--drift`,
     ```

     Troca 5, `### 8.1` (o drift). Trecho antigo:

     ```text
     mostra o que muda entre as duas versões, contratos inclusive.
     ```

     Trecho novo:

     ```text
     mostra o que muda entre as duas versões — a operação nova, a renumerada e a alterada, e a propriedade que só uma delas tem —, contratos inclusive.
     ```

     Troca 6, `## 9`, **Relatório de encerramento** (a abertura de marco). Trecho antigo:

     ```text
     iniciá-la, e a recomendação explícita de contexto novo.
     ```

     Trecho novo:

     ```text
     iniciá-la, e a recomendação explícita de contexto novo. Na parada de marco, o relatório abre nomeando a entrega e o pedido do dono que a originou, com a data e um trecho verbatim das palavras dele.
     ```

     Troca 7, `## 11`, tabela de skills (a checagem de versão). Trecho antigo:

     ```text
     | `checar-versao-kit` | Criação de um plano novo:
     ```

     Trecho novo:

     ```text
     | `checar-versao-kit` | Criação de um plano novo, rodada por quem conduz antes de despachar o planejador, que registra o resultado no cabeçalho do plano:
     ```

     Troca 8, `## 11`, item do `backlog.py` (a violação do prefixo de decisões). Trecho antigo:

     ```text
     ainda fora da fila, inclusive —,
     ```

     Trecho novo:

     ```text
     ainda fora da fila, inclusive — e recusa o plano que declara o prefixo de decisões que outro plano já declarou (`C-18`),
     ```

     Troca 9, `## 11`, item do `backlog.py` (o `despachar`). Trecho antigo:

     ```text
     `in-progress`, grava a tarefa corrente com o ponto de partida e imprime o card (com
     ```

     Trecho novo:

     ```text
     `in-progress`, grava a tarefa corrente com o ponto de partida, grava num arquivo da pasta do plano, fora do versionamento, o pacote da tarefa — o card, os handovers, a leitura do modelo, que ele julga só na versão vigente, e as âncoras conferidas — e imprime o texto pronto do despacho ao executor (com
     ```

     Troca 10, `## 11`, item do `backlog.py` (o `drain`). Trecho antigo:

     ```text
     inbox de planos ao índice, e `diretiva`
     ```

     Trecho novo:

     ```text
     inbox de planos ao índice e avisa quando a diretiva de priorização não cita mais nenhum item vivo nem o plano que saiu, e `diretiva`
     ```

     Troca 11, `## 11`, item do `backlog_hook.py` (o gatilho). Trecho antigo:

     ```text
     o hook do ponto de carga: quando o prompt traz o gatilho de
     ```

     Trecho novo:

     ```text
     o hook do ponto de carga: quando o prompt do dono — nunca o relato de um subagente nem o aviso do sistema — traz o gatilho de
     ```

     Troca 12, `## 11`, item do `encerrar.py` (o verbo `tarefa`). Trecho antigo:

     ```text
     inclusive cada achado de processo do laudo; `marco` grava o resultado que o dono deu num marco em
     ```

     Trecho novo:

     ```text
     inclusive cada achado de processo do laudo, com a linha do laudo de onde ele veio como origem, que impede registrá-lo duas vezes, e avisa numa linha `encerrar: B1 —` o achado de instrumento que relata falha, que leva a tarefa ao consultor; `marco` grava o resultado que o dono deu num marco em
     ```

     Troca 13, `## 11`, item do `encerrar.py` (o verbo `marco`). Trecho antigo:

     ```text
     todos os lugares onde o marco aparece;
     ```

     Trecho novo:

     ```text
     todos os lugares onde o marco aparece e, no aceite de uma versão pendente do modelo, exige a linha de validação do consultor (`--consultor`) e promove a versão aceita, acertando o texto da operação em cada card;
     ```

     Troca 14, `## 11`, item do `review_evidence.py`. Trecho antigo:

     ```text
     antes de procurar outra tarefa que o tenha declarado.
     ```

     Trecho novo:

     ```text
     antes de procurar outra tarefa que o tenha declarado; o curinga do alvo casa como na linha de comando — a estrela numa pasta só, a estrela dupla alcançando as subpastas —, o nome de arquivo acentuado chega inteiro, e, para cada arquivo de teste entre os alvos, a evidência mostra as linhas que a entrega removeu.
     ```

     Troca 15, `## 11`, item do `prevoo.py`. Trecho antigo:

     ```text
     do dono cita e imprime a tabela `citado | existe | onde`, que abre o plano antes de qualquer
     ```

     Trecho novo:

     ```text
     do dono cita e imprime a tabela `citado | existe | onde` — `sim`, `não`, ou `criar` para o caminho que o próprio pedido manda criar, que não derruba o resultado —, que abre o plano antes de qualquer
     ```

     Troca 16, `## 12`, **Telemetria** (três trechos da mesma frase, cada um na sua linha). Trecho antigo, primeiro:

     ```text
     `docs/telemetria.tsv` é append-only e é a **fonte única** da série de consumo, com as
     ```

     Trecho novo, primeiro:

     ```text
     `docs/telemetria.tsv` é a **fonte única** da série de consumo, com as
     ```

     Trecho antigo, segundo:

     ```text
     `duracao_s` e `fonte`. A coluna
     ```

     Trecho novo, segundo:

     ```text
     `duracao_s`, `fonte` e `agente`. A coluna
     ```

     Trecho antigo, terceiro:

     ```text
     Quem escreve a linha é o hook `SubagentStop`, a cada rodada de agente do kit, com o
     ```

     Trecho novo, terceiro:

     ```text
     Quem escreve a linha é o hook `SubagentStop` (`.claude/tools/telemetria_hook.py`), uma por agente — a rodada seguinte do mesmo agente substitui a dele —, atribuída ao plano e à tarefa que a primeira linha do despacho declara (`despacho: <P-id> <ID>`), com o
     ```
  2. Em `README.md`, `## 11`, logo depois da linha `  campanha.` (a última do item do `prevoo.py`) e antes da linha vazia que a segue, inserir os dois itens abaixo (as quebras são as do bloco; cada linha perde o recuo deste card, e os dois espaços que sobram no começo das linhas de continuação entram no arquivo).

     ```text
     - `.claude/tools/card_check.py` — a conferência da `Verificação` de um card: roda cada comando
       publicado na árvore dada e compara a saída com o que o card escreve — no mundo `antes`, o valor
       medido antes; no `depois`, o resultado da seta, também no bloco cercado —; lê o par
       `antes`/`depois` entre crases, com pontuação no literal; roda o `git` só nos subcomandos de
       leitura, troca `<ref>` pelo ponto de partida que o despacho gravou e mede a linha marcada
       `(invariância)` só depois da entrega; com `--gravar`, grava a medida na pasta do plano da
       árvore medida, com o mundo no nome, onde o revisor a lê.
     - `.claude/tools/custo_sessao.py` — o medidor de custo da sessão: `medir` lê a conversa gravada
       de uma sessão e grava o contexto reenviado em cada turno; `passos` reparte os turnos por passo
       do loop e por tarefa despachada, de qualquer plano ou tíquete, e informa zero numa janela sem
       despacho.
     ```
  3. Rodar a Verificação, `pwsh -NoProfile -File .claude/checks/check-readme.ps1` e a suíte inteira.
- **Restrições desta tarefa:**
  - `pwsh -NoProfile -File .claude/checks/check-readme.ps1` sai 0, com a linha que começa por `check-readme: OK` (G-README).
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_doutrina_unidade.py` lê o `README.md` e exige nele o literal `71 turnos e ~189 mil tokens`, que as trocas não tocam.
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - O `README.md` tem alteração não commitada de outra frente: cada troca é substituição de um trecho que existe uma vez, e nada fora dos trechos se reescreve, se reverte ou se reflui.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14.
  - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não editar `.claude/README.md` (índice derivado, regenerado pelo `kit_check.ps1 -Mode generate`); não acrescentar ao guia os módulos de `.claude/tools/` fora dos onze de `DRF-40` (`rdo.py`, `telemetria.py`, `caminhos.py`, `agentdef.py`, `ocupacao.py`, `crenca_hook.py`, §7); não reescrever seção inteira nem mudar título de seção ou a linha `> Fonte da verdade:` de nenhuma; não descrever o hook do pytest, que o guia não descreve hoje.
- **Contingências:**
  - se algum trecho antigo das trocas 1 a 16 ou a linha `  campanha.` não existir verbatim, uma única vez, em `README.md` → parar e sinalizar `blocked` razão `premissa`, colando o número da troca e as três linhas do `README.md` em volta do ponto que o trecho descreve.
  - se `check-readme.ps1` sair diferente de 0 → parar e sinalizar `blocked` razão `premissa`, colando a saída inteira do comando.
  - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; `pwsh -NoProfile -File .claude/checks/check-readme.ps1` e a suíte inteira, porque `tests/test_doutrina_unidade.py` lê o `README.md`.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('README.md').read_text(encoding='utf-8');n=['card_check.py','modelo.py','encerrar.py','backlog.py','review_evidence.py','backlog_hook.py','telemetria_hook.py','progresso_hook.py','prevoo.py','materializar.py','custo_sessao.py'];e=['abre numa janela nova','sem reconferir âncora à mão','só chama o modelador quando encontra conflito','--so-vigente','a propriedade que só uma delas tem','Na parada de marco','rodada por quem conduz antes de despachar o planejador','C-18','que ele julga só na versão vigente','não cita mais nenhum item vivo','nunca o relato de um subagente','encerrar: B1','--consultor','as linhas que a entrega removeu','que o próprio pedido manda criar','uma por agente'];print('guia=%d-%d-%d'%(sum(x in t for x in n),sum(x in t for x in e),t.count('append-only e é a')))"` → `guia=11-16-0` — antes `guia=8-0-1`, depois `guia=11-16-0`
- **Pronto quando:**
  - guia de entrada do kit.aderência ao kit entregue — o guia cita todos os comandos do kit, inclusive o medidor novo, descreve o que as cinco etapas mudaram, e a conferência do guia passa — Verificação 1; a conferência do guia, pela restrição do `check-readme.ps1` em exit 0
- **Fora do escopo desta tarefa:** o veredito do dono sobre a revisão, que é gate do Marco 6 e vai ao relatório de encerramento; a medida do ganho das `R-01`, `R-02`, `R-03` e `R-21` com o `custo_sessao.py`, que é da condução no relatório do Marco 6 (§7).
- **Handover:** 2026-09-30 · para quem vier depois
  - **Entregue:** README.md revisado: o guia de entrada descreve o kit como ele fica depois das cinco etapas do P-0755 (check-readme exit 0)
  - **Contrato:** o README reflete o kit depois das etapas A a E
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum

## 6. Ordem de execução

Etapas em sequência, A → B → C → D → E, cada uma fechada por marco (`DRF-5`). Dentro da etapa, a coluna "série"
lista as recomendações que tocam o mesmo arquivo, na ordem em que rodam; séries diferentes da mesma etapa podem
rodar em paralelo, salvo a dependência declarada. Os ids de card saem das operações (`RAF-T<n>` para `OP-<n>`) e
entram no campo `Depende de` na decomposição.

Toda tarefa de uma etapa depende, direta ou transitivamente, da primeira tarefa da etapa, que nasce `blocked` e carrega o gate do marco (`DRF-5`): assim o `next` não seleciona tarefa da etapa seguinte antes do `go` do dono. Quando uma operação da §1 agrupa recomendações que a coluna "série" lista como passos separados, o card cobre o grupo inteiro e a série mostra o grupo num card só: `OP-3` (`R-02` e `R-03`, instrumento do despacho, `RAF-T3`), `OP-4` (a doutrina dos Passos 3 e 4, `RAF-T4`), `OP-13` (`R-09` e `R-10`, `RAF-T13`), `OP-26`, `OP-30`, `OP-34` e `OP-38` (`R-23`, no planejador e na skill `checar-versao-kit`, `RAF-T38`). A doutrina da `R-05` (a rodada grava a medida dos dois mundos) é operação própria, `OP-18`, logo depois da `R-27` (`OP-17`), no mesmo trecho do planejador.

| etapa | série por arquivo | dependência entre séries |
|---|---|---|
| A | skill `scrum-master`: `R-01` doutrina (`RAF-T1`) → recuo do campo `Janela`, corretivo (`RAF-T1a`, `DRF-43`) → `R-02` e `R-03` doutrina dos Passos 3 e 4, num card só (`RAF-T4`) → Gate de delegação item 3 e `Entrada` do Passo 4, corretivo (`RAF-T4a`, `DRF-46`) · `custo_sessao.py`: `R-01` instrumento (`RAF-T2`) · `backlog.py`, `caminhos.py` e `.gitignore`: `R-02` e `R-03` num card só (`RAF-T3`) → âncora ausente só na linha citada, corretivo (`RAF-T3a`, `DRF-45`) · `backlog_hook.py`: `R-15` (`RAF-T5`) · `pytest_pretooluse.py` e `pytest_filter.py`: `R-24` (`RAF-T6`) → `||` e quebra de linha no hook, corretivo (`RAF-T6a`, `DRF-47`) | `RAF-T1` abre a etapa; `RAF-T2`, `RAF-T3`, `RAF-T5` e `RAF-T6` dependem só de `RAF-T1` e correm em paralelo entre si; `RAF-T4` depois de `RAF-T3` e `RAF-T3a` (a doutrina descreve o instrumento) e de `RAF-T1a` (mesmo arquivo); `RAF-T4a` depois de `RAF-T4`; `RAF-T6a` depois de `RAF-T6` |
| B | `review_evidence.py`: `R-13` (`RAF-T7`) → comparação de bytes que nunca iguala, corretivo (`RAF-T7a`, `DRF-49`) → `R-14` (`RAF-T8`) → frase da rubrica que conta os rótulos, corretivo (`RAF-T8a`, `DRF-50`) → `R-30` (`RAF-T9`) → docstring do teste da `AUF-T3`, corretivo (`RAF-T9a`, `DRF-51`) → `R-31` (`RAF-T10`) → arquivo acentuado já rastreado e alvo acentuado, corretivo (`RAF-T10a`, `DRF-52`) → `R-12` (`RAF-T11`) → teste sob curinga ou diretório e linha que começa por `--`, corretivo (`RAF-T11a`, `DRF-53`) · rubrica: `R-12` doutrina (`RAF-T12`) → dimensão `testes` de fonte mista e citações da rubrica pela seção, corretivo (`RAF-T12a`, `DRF-54`) · `card_check.py`: `R-09` e `R-10` num card só (`RAF-T13`) → docstring do módulo e ajuda de `--mundo`, corretivo (`RAF-T13a`, `DRF-55`) → `R-11` (`RAF-T14`) · `caminhos.py`, `card_check.py` e o leitor em `review_evidence.py`: `R-05` instrumento (`RAF-T15`) · `pantonic-planner.md`: `R-26` na Fase 5 (`RAF-T16`) → `R-27` no item 14 (`RAF-T17`) → `R-05` doutrina da rodada, no mesmo trecho do item 14, logo depois (`RAF-T18`) | `RAF-T7` abre a etapa; `RAF-T7a` depois de `RAF-T7` e `RAF-T8` depois de `RAF-T7a`; `RAF-T13` depende só de `RAF-T7` e corre em paralelo à série de `review_evidence.py`; `RAF-T8a` depois de `RAF-T8`; `RAF-T12` depois de `RAF-T11a` e de `RAF-T8a`; `RAF-T13a` depois de `RAF-T13`; `RAF-T14` depois de `RAF-T13a` (mesmo arquivo) e de `RAF-T3` (o `ref` que o despacho grava); `RAF-T12a` depois de `RAF-T12`; `RAF-T15` depois de `RAF-T11a`, de `RAF-T14` e de `RAF-T12a` (mesmo arquivo); `RAF-T16` depois de `RAF-T15`; `RAF-T17` depois de `RAF-T16` e de `RAF-T14`; `RAF-T18` depois de `RAF-T17` e de `RAF-T15` |
| C | `modelo.py`: `R-04` (`--so-vigente`, `RAF-T19`) → `R-06` (`V22`, `RAF-T21`) → `R-07` (drift, `RAF-T22`) · `backlog.py`: `R-04` (despacho com `--so-vigente`, `RAF-T20`) · `encerrar.py`: `R-08` e a promoção da `R-06`, num card só (`RAF-T23`) → `Devolver` do dossiê no conflito e na recusa, corretivo (`RAF-T23b`, `DRF-64`) · doutrina: skill `scrum-master` (rota `modelador` com operação nova, `R-04`, `RAF-T24`) → destino no marco do card da operação nova, corretivo (`RAF-T24a`, `DRF-63`) · `pantonic-planner.md` (card da operação nova na rodada, `R-04`, `RAF-T25`) · `pantonic-model-designer.md` e `pantonic-consultant.md` (`R-08`, num card só, `RAF-T26`) → os quatro conflitos e o que o modelador devolve, corretivo (`RAF-T26a`, `DRF-64`) | `RAF-T19` abre a etapa e depende de `RAF-T18`; `RAF-T20`, `RAF-T21` e `RAF-T25` dependem de `RAF-T19`; `RAF-T19a` (corretivo da `OP-19`, `DRF-59`) depende de `RAF-T19`, e `RAF-T21` também dele; `RAF-T22` depois de `RAF-T21`; `RAF-T23` depois de `RAF-T22`; `RAF-T23a` (corretivo da `OP-23`, `DRF-62`) depende de `RAF-T23`, e `RAF-T30` (mesmo arquivo) também dele; `RAF-T24` depois de `RAF-T20`; `RAF-T24a` (corretivo da `OP-24`, `DRF-63`) depois de `RAF-T24`; `RAF-T26` depois de `RAF-T23`; `RAF-T23b` (corretivo da `OP-23`, `DRF-64`) depois de `RAF-T23a`; `RAF-T26a` (corretivo da `OP-26`, `DRF-64`) depois de `RAF-T26` e de `RAF-T23b`; `RAF-T24a`, `RAF-T25` e `RAF-T26a` fecham a etapa |
| D | `prevoo.py`: `R-17` (`RAF-T27`) → docstring do módulo, corretivo (`RAF-T27a`, `DRF-66`) · `backlog.py`: `R-18` (`RAF-T28`) → `R-28` (`RAF-T29`) → frases que contam o vocabulário do `check`, corretivo (`RAF-T29a`, `DRF-67`) · `encerrar.py`: `R-19` e `R-20`, num card só (`RAF-T30`) → quinto alvo do achado de processo no gerador do laudo, na rubrica e no revisor, corretivo (`RAF-T30a`, `DRF-68`) · `telemetria_hook.py` e `telemetria.py` (`RAF-T31`) → docstrings do escritor sobre a recusa da linha repetida e a linha do agente, corretivo (`RAF-T31a`, `DRF-69`) → primeiro parágrafo do docstring e `help` do `append`, corretivo (`RAF-T31b`, `DRF-70`) · `progresso_hook.py` (`RAF-T32`): `R-16` → retorno por hand-back, corretivo (`RAF-T32a`, `DRF-72`) · doutrina: `GOVERNANCA.md` §4.2 (`R-16`, `RAF-T33`) · skill `scrum-master` (`B1` da `R-20` e despacho do consultor da `R-16`, num card só, `RAF-T34`) · `pantonic-consultant.md` (origem da `R-19`, `RAF-T35`) | `RAF-T27` abre a etapa e depende de `RAF-T24`, `RAF-T24a`, `RAF-T25`, `RAF-T26` e `RAF-T26a`; `RAF-T27a` (corretivo da `OP-27`, `DRF-66`) depois de `RAF-T27`; `RAF-T28`, `RAF-T30` e `RAF-T31` dependem de `RAF-T27`; `RAF-T29` depois de `RAF-T28`; `RAF-T29a` (corretivo da `OP-29`, `DRF-67`) depois de `RAF-T29`; `RAF-T31a` (corretivo da `OP-31`, `DRF-69`) depois de `RAF-T31`; `RAF-T31b` (corretivo da `OP-31`, `DRF-70`) depois de `RAF-T31a`; `RAF-T32` depois de `RAF-T31`; `RAF-T32a` (corretivo da `OP-32`, `DRF-72`) depois de `RAF-T32`; `RAF-T33` depois de `RAF-T31` e de `RAF-T32`; `RAF-T30a` (corretivo da `OP-30`, `DRF-68`) depois de `RAF-T30`; `RAF-T34` depois de `RAF-T30`, de `RAF-T30a` e de `RAF-T33`; `RAF-T35` depois de `RAF-T30`; `RAF-T27a`, `RAF-T29a`, `RAF-T31b`, `RAF-T32a`, `RAF-T34` e `RAF-T35` fecham a etapa |
| E | `pantonic-planner.md`: `R-21` (`RAF-T36`) → `R-22` (`RAF-T37`) → `R-23`, com a skill `checar-versao-kit`, num card só (`RAF-T38`) · skill `scrum-master`: `R-25` (`RAF-T39`) → a entrega pelo nome da etapa e a remissão no primeiro parágrafo do relatório, corretivo (`RAF-T39a`, `DRF-75`) · `modelo.py`: operação que muda `precisa de:` ou `altera:` sem mudar o texto, corretivo da `OP-22` (`RAF-T22a`, `DRF-73`) · `README.md`: revisão (`RAF-T40`, a última) | `RAF-T36` abre a etapa e depende de `RAF-T29`, `RAF-T29a`, `RAF-T34` e `RAF-T35`; `RAF-T37` depois de `RAF-T36`; `RAF-T38` depois de `RAF-T37`; `RAF-T39` depois de `RAF-T36`, em paralelo à série do planejador; `RAF-T39a` (corretivo da `OP-39`, `DRF-75`) depois de `RAF-T39`; `RAF-T22a` (corretivo da `OP-22`, `DRF-73`) depois de `RAF-T36`, em paralelo às duas séries; `RAF-T40` depois de `RAF-T38`, de `RAF-T39`, de `RAF-T39a` e de `RAF-T22a`, a última do plano (as etapas anteriores já fecharam nos Marcos 2 a 5) |

## 7. Fora de escopo (explícito)

- **`R-29`** (`next` limitado ao plano corrente): registrada sem ação (`DRF-3`); a residência é esta linha e o
  relatório `docs/audits/AUDITORIA_FINAL_KIT.md` §5.
- **Medida do ganho de `R-01`, `R-02`, `R-03` e `R-21`:** não é card; a `R-01` entrega o instrumento
  (`custo_sessao.py`), e a condução o roda sobre o transcript da janela de execução deste plano para o relatório
  do Marco 6, contra 285,6k por turno (F-6).
- **Os demais itens da auditoria §8 sem recomendação própria** — verbo `receber <ID> <linha>` (P5), prompt do
  revisor gerado (P6), handover pré-preenchido (P9): não estão na ação de nenhuma `R-n`; ficam no relatório.
- **Duplicatas de achados do `P-0754`** (`AE-100` e `AE-101`, `AE-117`..`AE-119`): cobertas pela `R-19`; não
  viram item.
- **Atos do dono:** commit; `materializar.py apply`; veredito do Marco 3 e fechamento do `P-0754`.
- **Reescrita da diretiva de priorização** (`docs/DIARIO_DE_OBRAS.md:4`): ato da condução, com `backlog.py
  diretiva`, depois do registro deste plano.
- **`Skill` no `tools:` dos agentes** (`DRF-25`).
- **Correção dos protótipos em `docs/audits/sonda-2026-09-28/`:** ficam como registro da auditoria; o instrumento
  é arquivo novo (`DRF-6`).
- **`docs/DOC_MAP.md:7`** (F-30): fora deste plano; a condução abre tíquete.
- **Módulos de `.claude/tools/` fora dos onze comandos que o `README.md` cita** (`rdo.py`, `telemetria.py`, `caminhos.py`,
  `agentdef.py`, `ocupacao.py`, `crenca_hook.py`; `DRF-40`): a revisão do guia não os acrescenta; a residência é esta
  linha.
- **Cards de planos encerrados com o texto da operação divergente** (`F-31`): `P-0746`, `P-0747`, `P-0748` e
  `P-0753` passam a sair `V22` no `modelo.py check` depois da `RAF-T21`; são registro histórico e não se
  reescrevem.

## 8. Riscos

1. **Um leitor de `docs/telemetria.tsv` quebra com a coluna `agente`** (`DRF-18`) → medido no ensaio da
   `RAF-T31`: o único leitor em código (`_ler_tsv` do `encerrar.py`) lê pelo cabeçalho, e o escritor põe `-` na
   linha gravada sem agente numa série já migrada (`DRF-39`); o card para `blocked` razão `premissa` se ainda
   assim um teste que já existia cair.
2. **`agent_transcript_path` ausente no payload** → a coluna `agente` recebe `-` e a linha é apensada sem dedupe.
3. **Instrumento do loop quebrado pela entrega que o altera** (`despachar`, `card_check`, `review_evidence` e
   `encerrar` são usados pelo próprio loop deste plano) → a revisão reprova; o consultor abre o corretivo `T<n>a`
   da mesma operação; o loop não despacha outra tarefa com o instrumento quebrado.
4. **WIP não commitado nos arquivos-alvo** (`review_evidence.py`, `encerrar.py`, `progresso_hook.py`,
   `README.md` e os testes deles estão modificados na árvore) → toda `Verificação` por diff mede o delta contra a
   base re-medida no despacho, nunca o total contra `HEAD`.
5. **Gate de qualidade vermelho por arquivo que o plano não toca** (por exemplo, `dead_code.py` sobre
   `docs/audits/sonda-2026-09-28/*.py`) → nenhum card exige esse verde; a entrega devolve `pendencia=` com o nome
   do gate e segue.
6. **Hook do pytest corrigido só no repositório** (`R-24`) → a sessão continua com a projeção antiga até o
   `materializar.py apply` do dono; nenhum card depende da projeção.
7. **Marco com `no-go`** → a etapa seguinte não começa; a condução leva o veredito ao consultor, que tria pela
   rota técnica ou pela rota `planejador`.
8. **Versão pendente do modelo durante a execução** → segue a `DRF-14` (despacho por `--so-vigente`, card novo
   `blocked` até o marco) e, depois da etapa C, a promoção pela `DRF-17`.

## 9. Achados da execução
- **AE-120** (`RAF-T1`, fechamento, 2026-09-28) — Prosa depois da linha de retorno válida do executor da RAF-T1 descartada pelo passo 5 (vale a primeira linha não vazia). **Rota:** sem ação — observação, forma já prevista no passo 5
- **AE-121** (`RAF-T1`, fechamento, 2026-09-28) — achado de processo (dossiê): dossie de evidencia do P-0755 herda vermelho de dead_code causado pela sonda untracked docs/audits/sonda-2026-09-28/passos.py (fora do alcance de toda tarefa do plano): toda revisao da janela vai reconciliar o mesmo vermelho. **Rota:** AE-<n> na §9 do P-0755 - excluir docs/audits/ da varredura do dead_code ou versionar/remover a sonda por decisao da conducao · **Triagem:** consultor, acionamento 1 → `DRF-44` (sem card: §7, §8 item 5 e a restrição dos cards já o cobrem; o escopo do `dead_code.py` sobre `docs/` segue com rota "auditoria final")
- **AE-122** (`RAF-T1`, fechamento, 2026-09-28) — achado de processo (dossiê): Passo 1 do RAF-T1 manda 'cada linha perde os dois espacos do recuo deste card' sobre um bloco recuado 5 espacos: o resultado literal (3 espacos) fez '- **Janela:**' virar sub-item aninhado do bullet '- **Ação:**' no Markdown, e nao campo irmao de Gatilho/Entrada/Acao/Saida. A execucao seguiu o card a letra; a Verificacao 1 (count do literal) nao discrimina o recuo. **Rota:** AE-<n> na §9 do P-0755 - decidir se o campo sobe a coluna 0 (card de reparo) e fixar no planejador a forma 'perde o recuo deste card' usada em RAF-T3/RAF-T4 · **Triagem:** consultor, acionamento 1 → `DRF-43`, card corretivo `RAF-T1a`
- **AE-123** (`RAF-T1a`, fechamento, 2026-09-28) — achado de processo (dossiê): o dossie de evidencia do P-0755 segue marcando guardas vermelho pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py, sem carregar que a falha e anterior a tarefa: cada revisao da janela reconcilia o mesmo vermelho a mao (reincidencia do achado do laudo RAF-T1). **Rota:** DRF-44 ja aberta no P-0755 (Fora do escopo da RAF-T1a); registrar a reincidencia como AE-<n> na §9 apontando para ela
- **AE-124** (`RAF-T2`, fechamento, 2026-09-28) — achado de processo (dossiê): reincidencia (terceira na janela, apos laudos RAF-T1 e RAF-T1a): o dossie de evidencia do P-0755 marca guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base do despacho, e cada revisao reconcilia o mesmo vermelho a mao. **Rota:** DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na §9 apontando para ela
- **AE-125** (`RAF-T3`, fechamento, 2026-09-28) — achado de processo (dossiê): A regra fechada de conferir_ancoras_do_card (Contratos/classes item 2, DRF-8/DRF-35) toma todo trecho entre crases de Passos e Contratos/classes como ancora: exercitada em leitura sobre cards reais do P-0755, marca como ausente comando, molde e nome de campo (RAF-T30: 21 de 33 linhas 'ancora ausente'; RAF-T3: 'Testes', 'backlog.main([...])'), fatia os code spans de crase dupla em fragmentos (') dos campos', '(regex'), e o padrao (c) nao casa arquivo sem extensao apos o ponto ('.gitignore:12' cai em ausente) nem caminho nao relativo a raiz ('caminhos.py:119') - o pacote leva ruido de ancora ausente falsa ao executor, que a RAF-T4 manda nao reconferir. Entrega fiel ao card. **Rota:** AE na secao 9 do P-0755, item de replanejamento a triar pelo consultor antes da RAF-T4. · **Triagem:** consultor, acionamento 2 → `DRF-45`, card corretivo `RAF-T3a`
- **AE-126** (`RAF-T4`, fechamento, 2026-09-28) — achado de processo (dossiê): A Camada do RAF-T4 afirma 'a regra muda so nos Passos 3 e 4; nenhum outro arquivo a repete', e o Pronto quando promete 'nenhum passo manda reconferir', mas .claude/skills/passagem-de-bastao/SKILL.md:117 (Gate de delegacao, item 3) segue mandando colar as ancoras 're-derivadas no ato' - e o Passo 3 da scrum-master manda quem conduz rodar esse gate antes do despachar; alem disso o campo Entrada do Passo 4 (scrum-master SKILL.md:99) segue 'dossie da tarefa copiado do plano', contra o 'sem copiar o card' do texto novo. A Verificacao 2 conta so a skill scrum-master e nao discrimina a promessa. Entrega fiel ao card (as tres trocas verbatim, Verificacoes 1 e 2 re-rodadas: entrega=0-1, ancoras=0-1). **Rota:** AE-<n> na secao 9 do P-0755, item de replanejamento a triar pelo consultor (card corretivo da OP-4 sobre passagem-de-bastao item 3 e a Entrada do Passo 4); a linha README.md:909-913 ('imprime o card') ja e da RAF-T40. · **Triagem:** consultor, acionamento 3 → `DRF-46`, card corretivo `RAF-T4a`
- **AE-127** (`RAF-T4a`, fechamento, 2026-09-28) — achado de processo (dossiê): reincidencia (quinta na janela): o dossie de evidencia do P-0755 segue marcando guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base que o proprio despacho declara (1 achado admitido); cada revisao reconcilia a mao. **Rota:** DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela
- **AE-128** (`RAF-T5`, fechamento, 2026-09-28) — achado de processo (dossiê): reincidencia na janela do P-0755 (apos RAF-T1..RAF-T4a): o dossie de evidencia segue marcando guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base que o proprio despacho declara (1 achado admitido); cada revisao reconcilia a mao. **Rota:** DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela
- **AE-129** (`RAF-T6`, fechamento, 2026-09-28) — achado de processo (dossiê): reincidencia apos RAF-T1..RAF-T5: o dossie de evidencia segue marcando guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o proprio despacho declara; cada revisao reconcilia a mao. **Rota:** DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela
- **AE-130** (`RAF-T6`, fechamento, 2026-09-28) — achado de processo (dossiê): contrato do card incoerente no separador duplo-pipe (OU logico): dividir_segmentos o reconhece como separador, mas o card manteve inalterada a condicao de passthrough de main() que recusa qualquer comando com o caractere pipe, entao comando encadeado por OU logico (ex.: pytest -q seguido de OU echo falhou) nunca chega a reescrever() e segue sem filtro (exit preservado, saida nao encurtada); exercitado na revisao: main() devolve {} para esse comando. A entrega seguiu o card fielmente. **Rota:** AE-<n> na secao 9 do P-0755, candidato a card que restrinja o guarda de pipe ao pipe simples · **Triagem:** consultor, acionamento 4 → `DRF-47`, card corretivo `RAF-T6a`
- **AE-131** (`RAF-T6a`, fechamento, 2026-09-29) — achado de processo (dossiê): reincidencia apos RAF-T1..RAF-T6: o dossie de evidencia segue marcando guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o proprio despacho declara; cada revisao reconcilia a mao. **Rota:** DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela
- **AE-132** (`RAF-T6a`, fechamento, 2026-09-29) — achado de processo (dossiê): decisao que o card nao fechou (G-NOASK): o card manda editar .claude/global/hooks/pytest_pretooluse.py, caminho que o auto mode classifica como Self-Modification, sem prever a negacao nem nomear o canal de edicao; negada a tentativa por python -c via Bash, a execucao decidiu sozinha refazer a mesma mudanca pela ferramenta Edit (o dono aceitou a edicao depois). **Rota:** AE-<n> na secao 9 do P-0755, triagem do consultor; candidato a linha de Restricao/Contingencia nos cards que editam hooks ou .claude/ (se a permissao negar -> blocked) · **Triagem:** consultor, acionamento 5 → `DRF-48`
- **AE-133** (`RAF-T6a`, fechamento, 2026-09-29) — achado de processo (doutrina): guardrail ausente: nenhuma regra de GOVERNANCA.md secao 7 diz o que o executor faz quando o sistema de permissao nega uma acao sobre um Arquivo-alvo; refazer a mesma mudanca por outra ferramenta e contorno de negacao, e o comportamento coerente com G-NOASK/G-PLANFIDELITY seria parar e devolver blocked. **Rota:** AE-<n> na secao 9 do P-0755, triagem do consultor, candidato a emenda de GOVERNANCA.md secao 7 · **Triagem:** consultor, acionamento 5 → `DRF-48`
- **AE-134** (`RAF-T7`, fechamento, 2026-09-29) — achado de processo (dossiê): reincidencia apos RAF-T1..RAF-T6a: o dossie de evidencia segue marcando guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o proprio despacho declara; cada revisao reconcilia a mao (passo 3a). **Rota:** DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela
- **AE-135** (`RAF-T7`, fechamento, 2026-09-29) — achado de processo (dossiê): Contratos/classes regra 3 do RAF-T7 manda, no ramo texto_ref None, devolver '(sem alteracao desde <ref>)' quando os bytes do ref igualam os do disco; esse ramo so e alcancado com texto_atual decodificado em UTF-8 e ref nao decodificavel, logo bytes iguais sao impossiveis e o ramo e inalcancavel por construcao (a entrega o implementou fielmente, sem teste que o exercite). **Rota:** AE-<n> na secao 9 do P-0755, para o card seguinte que tocar _diff_para_arquivo (RAF-T8) decidir se o ramo sai · **Triagem:** consultor, acionamento 6 → `DRF-49`, card corretivo `RAF-T7a`
- **AE-136** (`RAF-T7a`, fechamento, 2026-09-29) — achado de processo (dossiê): reincidencia apos RAF-T1..RAF-T7: o dossie de evidencia segue marcando guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) declarada no proprio card; a revisao reconcilia a mao (passo 3a). **Rota:** DRF-44 ja aberta no P-0755; somar a reincidencia ao AE-<n> que ja aponta para ela na secao 9
- **AE-137** (`RAF-T8`, fechamento, 2026-09-29) — achado de processo (dossiê): RUBRICA_DE_REVISAO.md §3 (linhas 48-53) ainda descreve a secao '## Arquivos tocados' com dois rotulos, 'da entrega' ou 'alheio'; a entrega (fiel ao card) criou o terceiro, 'registro da orquestracao', e o card nao pos a frase da rubrica nos Arquivos-alvo (criterio (viii) da §8). **Rota:** AE-<n> na §9 do P-0755, para card que emende a frase da §3 da rubrica ao novo rotulo. · **Triagem:** consultor, acionamento 7 → `DRF-50`, card corretivo `RAF-T8a`
- **AE-138** (`RAF-T8a`, fechamento, 2026-09-29) — achado de processo (dossiê): reincidencia apos RAF-T1..RAF-T8: o dossie de evidencia segue marcando guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o despacho declara, e esta restricao do card nao a admite nominalmente; a revisao reconcilia a mao (passo 3a). **Rota:** DRF-44 ja aberta no P-0755; somar a reincidencia ao AE-<n> que ja aponta para ela na secao 9
- **AE-139** (`RAF-T9`, fechamento, 2026-09-29) — achado de processo (dossiê): reincidencia apos RAF-T1..RAF-T8a: o dossie de evidencia segue marcando guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o proprio card declara; a revisao reconcilia a mao (passo 3a). **Rota:** DRF-44 ja aberta no P-0755; somar a reincidencia ao AE-<n> que ja aponta para ela na secao 9
- **AE-140** (`RAF-T9`, fechamento, 2026-09-29) — achado de processo (dossiê): a restricao que congela as linhas existentes de tests/test_review_evidence.py deixou o docstring de test_tf_alvo_com_curinga_casa_os_tocados (linha 1459) dizendo que o curinga casa 'por fnmatch', mecanismo que esta entrega removeu; o card mandou trocar so o docstring de _eh_alvo_curinga. **Rota:** item de replanejamento na secao 9 do P-0755, a acertar pelo proximo card que ja edita tests/test_review_evidence.py (RAF-T11 ou sucessor) · **Triagem:** consultor, acionamento 8 → `DRF-51`, card corretivo `RAF-T9a`
- **AE-141** (`RAF-T9a`, fechamento, 2026-09-29) — achado de processo (dossiê): reincidencia apos RAF-T1..RAF-T9: o dossie de evidencia segue marcando guardas nao conforme pelo dead_code da sonda nao rastreada docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que a restricao do card e o despacho declaram; a revisao reconcilia a mao (passo 3a). **Rota:** DRF-44 ja aberta no P-0755; somar a reincidencia ao AE-<n> que ja aponta para ela na secao 9
- **AE-142** (`RAF-T10`, fechamento, 2026-09-29) — achado de processo (modelo): OP-10 diz que o dossie de evidencia recebe inteiro o nome acentuado que o versionador lista, mas a entrega (fiel ao card) so cobre o git status -z: exercicio ponta a ponta com core.quotepath ligado e arquivo rastreado 'trilha acao.md' (com cedilha/til) editado depois do ref mostra, via git diff <ref> --name-only, o tocado como "trilha a\303\247\303\243o.md" (aspas e escape octal), atribuido alheio, e coletar_estado_git com duas chaves para o mesmo arquivo. **Rota:** dossie Ato de modelo de conflito devolvido com o laudo, ao pantonic-model-designer por quem conduz a sessao · **Triagem:** consultor, acionamento 9 → `DRF-52`, card corretivo `RAF-T10a`
- **AE-143** (`RAF-T10`, fechamento, 2026-09-29) — achado de processo (dossiê): O Fora do escopo da RAF-T10 excluiu git diff <ref> --name-only/--name-status e pediu o julgamento da revisao: julgado defeito (mesma evidencia do achado de modelo: caminho rastreado acentuado chega com escape octal e duplica chave em coletar_estado_git). **Rota:** AE-<n> na secao 9 do P-0755, card corretivo com -z (ou core.quotepath=false por invocacao) nas duas leituras de git diff · **Triagem:** consultor, acionamento 9 → `DRF-52`, card corretivo `RAF-T10a`
- **AE-144** (`RAF-T10`, fechamento, 2026-09-29) — achado de processo (dossiê): _CAMINHO_RE de review_evidence.py e ASCII-only: um arquivo acentuado declarado em Arquivos-alvo sai como Literal nao reconhecido como caminho, o tocado acentuado vira alheio e o dossie nao cola o trecho dele; o Pronto quando (chega com a sua diferenca, como qualquer outro) so vale em montar_trechos com alvos explicitos, que e o que a Verificacao 1 exercita. **Rota:** AE-<n> na secao 9 do P-0755 · **Triagem:** consultor, acionamento 9 → `DRF-52`, card corretivo `RAF-T10a`
- **AE-145** (`RAF-T10`, fechamento, 2026-09-29) — achado de processo (dossiê): Prosa residual que o card nao mandou tocar: o docstring de coletar_arquivos_tocados ainda descreve o ramo do git status com nome entre aspas e escape octal, e a primeira linha do de coletar_estado_git cita o comando sem -z. **Rota:** AE-<n> na secao 9 do P-0755, junto do card corretivo do achado anterior · **Triagem:** consultor, acionamento 9 → `DRF-52`, card corretivo `RAF-T10a`
- **AE-146** (`RAF-T10`, fechamento, 2026-09-29) — achado de processo (dossiê): Reincidencia na janela do P-0755 (apos RAF-T1..RAF-T9a): o dossie de evidencia segue marcando guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o despacho declara. **Rota:** DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela
- **AE-147** (`RAF-T10a`, fechamento, 2026-09-29) — achado de processo (dossiê): Reincidencia na janela do P-0755 (RAF-T10 e agora RAF-T10a): o dossie de evidencia segue marcando guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o despacho declara. **Rota:** DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela
- **AE-148** (`RAF-T11`, fechamento, 2026-09-29) — achado de processo (dossiê): Reincidencia na janela do P-0755 (RAF-T10, RAF-T10a e agora RAF-T11): o dossie de evidencia marca guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o card e o despacho declaram. **Rota:** DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela · **Triagem:** consultor, acionamento 10 → reincidência da `DRF-44`, sem ação
- **AE-149** (`RAF-T11`, fechamento, 2026-09-29) — achado de processo (dossiê): Lacuna latente das regras 2 e 3 do card RAF-T11, entregues como escritas: (a) alvo com curinga que cobre arquivos de teste (ex.: tests/test_*.py) e pulado, e a secao diz '- nenhum arquivo de teste entre os alvos' - afirmacao falsa e remocao invisivel (hoje sem caso vivo: F-17, 0 alvos com * no corpus); (b) linha removida cujo conteudo comeca por '--' cai no filtro de '---' e some. Exercitado na revisao em repositorio descartavel. **Rota:** item de replanejamento na secao 9 do P-0755 (AE-<n>), a triar pelo consultor contra RAF-T12, que consome a secao · **Triagem:** consultor, acionamento 10 → `DRF-53`, card corretivo `RAF-T11a`
- **AE-150** (`RAF-T11a`, fechamento, 2026-09-29) — achado de processo (dossiê): Reincidencia na janela do P-0755 (RAF-T10, RAF-T10a, RAF-T11 e agora RAF-T11a): o dossie de evidencia marca guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o card e o despacho declaram. **Rota:** DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela
- **AE-151** (`RAF-T12`, fechamento, 2026-09-29) — achado de processo (rubrica): O criterio novo de testes/nao conforme (asserção removida sem ordem do card) exige juizo - confrontar cada linha de '## Linhas removidas dos testes' com o que o card manda -, mas o bullet Fonte da evidencia segue 'mecanica' e o veredito travado de review_evidence.py (veredito_testes) le so o exit do pytest: a dimensao virou de fonte mista sem a rubrica dizer qual parte e travada e qual e juizo (§3). Texto entregue verbatim pelo card; nao rebaixa a entrega. **Rota:** item de replanejamento na secao 9 do P-0755 (AE-<n>), a triar pelo consultor junto de RAF-T17 (linha de invariancia do card de revisao) · **Triagem:** consultor, acionamento 11 → `DRF-54`, card corretivo `RAF-T12a`
- **AE-152** (`RAF-T12`, fechamento, 2026-09-29) — achado de processo (dossiê): Reincidencia na janela do P-0755 (RAF-T10, RAF-T10a, RAF-T11, RAF-T11a e agora RAF-T12): o dossie de evidencia marca guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o despacho declara. **Rota:** DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela · **Triagem:** consultor, acionamento 11 → reincidência da `DRF-44`, sem ação
- **AE-153** (`RAF-T12a`, fechamento, 2026-09-29) — achado de processo (dossiê): Reincidencia na janela do P-0755 (RAF-T10..RAF-T12 e agora RAF-T12a): o dossie de evidencia marca guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o despacho declara. **Rota:** DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela
- **AE-154** (`RAF-T13`, fechamento, 2026-09-29) — achado de processo (dossiê): dead_code vermelho pre-existente (docs/audits/sonda-2026-09-28/passos.py, DRF-44) admitido no despacho mas nao carregado pelo dossie de evidencia: toda tarefa do P-0755 sai com guardas parcial enquanto o arquivo viver na arvore. **Rota:** item de replanejamento do P-0755 (AE na secao 9) - linha de base admitida no review_evidence.py ou recorte de docs/audits/ no dead_code
- **AE-155** (`RAF-T13`, fechamento, 2026-09-29) — achado de processo (dossiê): card_check.py fica com dois textos que contradizem a regra 1 (mundo depois na forma 8.1): o docstring do modulo, linhas 5-6 ('comparando a saida medida agora com o Medido antes declarado'), e o help de --mundo ('Mundo do card a comparar na forma inline (DFP-14)'); a regra 3 do card nomeou so o docstring de verificar_tarefa, e a entrega seguiu o card. **Rota:** item de replanejamento do P-0755 (AE na secao 9), acerto dos dois textos no mesmo arquivo
- **AE-156** (`RAF-T13`, fechamento, 2026-09-29) — achado de processo (dossiê): G-NOASK: o card fixou antes 'x, y' e o valor impresso do test_tf_par_com_crase_antes_aceita_virgula, mas nao o esperado nem o depois do item; a entrega escolheu esperado 'esperado' e depois 'q' (sem efeito no mundo antes que o teste exercita). **Rota:** item de replanejamento do P-0755 (AE na secao 9), registro para o criterio (i) da secao 8 da rubrica
- **AE-157** (`RAF-T13`, fechamento, 2026-09-29) — achado de processo (dossiê): a restricao 'card_check deste plano continua saindo 0 sobre RAF-T1..RAF-T18' e inalcancavel para o proprio RAF-T13 no mundo antes (status review): a entrega consome o antes (exit 5 -> exit 0) e o card_check do RAF-T13 sai 1 em antes e 0 em --mundo depois; os demais 18 cards saem 0. **Rota:** item de replanejamento do P-0755 (AE na secao 9) - a restricao exclui o proprio card ou fixa --mundo depois para ele
- **AE-158** (`RAF-T13`, fechamento, 2026-09-29) — achado de processo (doutrina): o executor rodou git stash e git stash pop na arvore compartilhada, que carrega WIP nao commitado de varios planos, para provar o TDD; a conducao conferiu stash vazio e WIP intacto, e o Passo 2 do card ja dava a prova (TF vermelho antes da regra). Nenhuma guarda mecanica impede comando git que reverte a arvore inteira numa sessao de execucao, e a restricao 'nada fora deles se toca, se reverte' nao foi lida como cobrindo stash. **Rota:** tiquete indexado (AE na secao 9 do P-0755) - guarda PreToolUse que recusa git stash/reset/checkout --/restore na execucao
- **AE-159** (`RAF-T13a`, fechamento, 2026-09-29) — achado de processo (dossiê): Reincidencia (AE-150, AE-152, AE-153, AE-154): o dead_code vermelho pre-existente de docs/audits/sonda-2026-09-28/passos.py (DRF-44) e admitido no despacho mas o dossie de evidencia nao carrega essa linha de base, e toda tarefa do P-0755 sai com guardas nao conforme mecanico e parcial reconciliado enquanto o arquivo viver na arvore. **Rota:** item de replanejamento do P-0755 (AE na secao 9) - linha de base admitida no review_evidence.py ou recorte de docs/audits/ no dead_code
- **AE-160** (`RAF-T14`, fechamento, 2026-09-29) — achado de processo (dossiê): dead_code vermelho pre-existente (docs/audits/sonda-2026-09-28/passos.py, DRF-44) segue admitido no despacho e nao carregado pelo dossie de evidencia: guardas sai parcial em toda tarefa do P-0755 enquanto o arquivo viver na arvore. **Rota:** a mesma do achado do laudo RAF-T13 (item de replanejamento, AE na secao 9 do P-0755) - linha de base admitida no review_evidence.py ou recorte de docs/audits/ no dead_code
- **AE-161** (`RAF-T14`, fechamento, 2026-09-29) — achado de processo (dossiê): Passo 2 inalcancavel como escrito: manda conferir que 'os quatro TF falham e o TR passa', mas a secao Testes fixa para o TR test_tr_ref_do_despacho_de_outra_tarefa_falha a mensagem nova 'item 1: <ref> sem recorte do despacho para RX-T1', que so existe depois da regra 4; reproduzido pelo reviewer numa copia fora do repo com o card_check.py do ref 2d242634: 5 failed (4 TF + o TR, que falha com 'divergencia ... saida <ref>'). Executor que rodasse o Passo 2 fielmente pararia por duvida que o card nao previu (G-NOASK). **Rota:** item de replanejamento do P-0755 (AE na secao 9), registro para o criterio (ix) da secao 8 da rubrica - TR que confere mensagem nova nao e regressao que passa antes
- **AE-162** (`RAF-T14`, fechamento, 2026-09-29) — achado de processo (doutrina): a checagem de vermelho do TDD (Passo 2) nao deixa rastro mecanico: o dossie de evidencia so admite a medida verde do executor, e o salto do Passo 2 nesta tarefa so e conhecido por relato do executor; a prova foi recuperada pelo reviewer por reproducao fora da arvore. **Rota:** tiquete indexado (AE na secao 9 do P-0755) - medida do mundo vermelho dos TF gravada antes da implementacao e colada no review_evidence.py, ou o passo sai dos cards como verificacao nao auditavel
- **AE-163** (`RAF-T15`, fechamento, 2026-09-29) — achado de processo (dossiê): reincidencia da DRF-44 (apos AE-121..AE-160): o dossie de evidencia marca guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o card e o despacho declaram; cada revisao reconcilia a mao. **Rota:** DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela
- **AE-164** (`RAF-T15`, fechamento, 2026-09-29) — achado de processo (doutrina): reincidencia do AE-162 (DRF-57): o Passo 4 (checagem de vermelho do TDD), pedido no despacho como passo proprio, nao deixa rastro mecanico no dossie de evidencia; a prova foi reposta pelo reviewer por reproducao fora da arvore (codigo do ref 55117ff + testes da entrega: 5 failed = 3 TF + 2 reescritos, 1 passed = o TR, exatamente o que o Passo 4 manda). **Rota:** AE-162 com rota auditoria final (diretiva de 2026-09-26); registrar a reincidencia como AE-<n> na secao 9 apontando para ela
- **AE-165** (`RAF-T16`, fechamento, 2026-09-29) — achado de processo (dossiê): reincidencia da DRF-44 (apos AE-121..AE-160 e os laudos RAF-T13a/T14/T15): o dossie de evidencia marca guardas nao conforme pelo dead_code da sonda docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base admitida no despacho (1 achado); cada revisao reconcilia a mao. **Rota:** DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela
- **AE-166** (`RAF-T17`, fechamento, 2026-09-29) — achado de processo (dossiê): reincidencia da DRF-44 (apos os laudos RAF-T13a/T14/T15/T16): o dossie de evidencia marca guardas nao conforme pelo dead_code da sonda docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base admitida no despacho (1 achado); cada revisao reconcilia a mao. **Rota:** DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela
- **AE-167** (`RAF-T18`, fechamento, 2026-09-29) — achado de processo (dossiê): reincidencia da DRF-44 (apos os laudos RAF-T13a/T14/T15/T16/T17): o dossie de evidencia marca guardas nao conforme pelo dead_code da sonda docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base admitida no despacho (1 achado); cada revisao reconcilia a mao. **Rota:** DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela
- **AE-168** (`RAF-T19`, fechamento, 2026-09-29) — achado de processo (dossiê): reincidencia da DRF-44 (apos os laudos RAF-T13a..T18): o dossie de evidencia marca guardas nao conforme pelo dead_code da sonda docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base admitida no despacho (1 achado); cada revisao reconcilia a mao. **Rota:** DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela **Triagem:** consultor, acionamento 15 → `DRF-44` (reincidência, sem ação nova)
- **AE-169** (`RAF-T19`, fechamento, 2026-09-29) — achado de processo (dossiê): a regra 3 do card (validar com so_vigente=True nao emite V20) nao tem teste que a discrimine: a fixture dos quatro testes traz a pendente em versao 2 = vigente 1 + 1, entao V20 nunca dispara, e remover a guarda 'not so_vigente' deixa os 4 testes verdes (criterio (ix) da rubrica §8). A entrega implementou a regra como escrita. **Rota:** AE-<n> na secao 9 do P-0755, com teste de pendente fora de sequencia sob --so-vigente num card corretivo ou na RAF-T20 **Triagem:** consultor, acionamento 15 → `DRF-59`, card corretivo `RAF-T19a`
- **AE-170** (`RAF-T19`, fechamento, 2026-09-29) — achado de processo (modelo): objeto 'conferencia do modelo' (origem OP-19, tabela 1.1 linha 81): o contrato diz 'sem mudar o que ela ja julga quando chamada como hoje', mas a regra 4 do card RAF-T19 (DRF-37), entregue como escrita, muda o check sem --so-vigente: em tests/fixtures/modelo/fluxo-pendente.md a linha 'V4 EX-T2 — operacao inexistente OP-2' deixa de sair (5 -> 4 violacoes, conferido contra o modelo.py do ref 5e35c55). **Rota:** dossie Ato de modelo de conflito devolvido com o laudo ao pantonic-model-designer **Triagem:** consultor, acionamento 15 → `DRF-60` (versão 3 pendente validada; sobe ao dono no Marco 4)
- **AE-171** (`RAF-T19a`, fechamento, 2026-09-29) — achado de processo (dossiê): reincidencia da DRF-44 (apos os laudos RAF-T13a..T19): o dossie de evidencia marca guardas nao conforme pelo dead_code da sonda docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base admitida no despacho (1 achado); cada revisao reconcilia a mao. **Rota:** DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela
- **AE-172** (`RAF-T20`, fechamento, 2026-09-29) — achado de processo (dossiê): Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado pre-existente do dead_code (docs/audits/sonda-2026-09-28/passos.py) sem carregar que ele e admitido e anterior ao diff; o revisor reconcilia a mao a cada laudo. **Rota:** DRF-44 na secao 9 do P-0755 (lacuna ja roteada), sem acao nova nesta tarefa.
- **AE-173** (`RAF-T21`, fechamento, 2026-09-29) — achado de processo (dossiê): Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado pre-existente do dead_code (docs/audits/sonda-2026-09-28/passos.py) sem carregar a linha de base admitida no despacho; cada revisao reconcilia a mao. **Rota:** DRF-44 ja aberta na secao 9 do P-0755; registrar a reincidencia como AE-<n> apontando para ela.
- **AE-174** (`RAF-T21`, fechamento, 2026-09-29) — achado de processo (dossiê): Parada nao prevista pelo card: a regra 2 original (um texto por numero, o ultimo vence) derrubava test_tf_check_invalido_lista_catorze_violacoes_na_ordem (EX2-T3 copia o primeiro de dois OP-3), e o primeiro despacho parou blocked premissa pela contingencia 1 - defeito de autoria (o ensaio nao rodou a regra contra a suite existente, criterio (xix)/(xii)(b) da rubrica §8). **Rota:** ja corrigida pela DRF-61 do consultor (regra 2 reescrita); sem acao nova, registrar como AE-<n> na secao 9 apontando para DRF-61.
- **AE-175** (`RAF-T22`, fechamento, 2026-09-29) — achado de processo (dossiê): Decisoes da entrega que o card nao fechou (G-NOASK): (1) apagou o helper _op_por_numero de modelo.py, que ficou sem chamador ao reescrever _diff_fluxo - o card nao previu o orfao, e manter o helper faria o dead_code ganhar achado novo contra a restricao; (2) o estado inicial dos casos de teste saiu '-', valor que o card nao fixou (so os finais). Nenhuma das duas muda o mundo exercitado. **Rota:** AE-<n> na secao 9 do P-0755, sem acao (autoria futura: card que reescreve funcao nomeia o helper que ela deixa orfao), mesma classe do AE-156.
- **AE-176** (`RAF-T23`, fechamento, 2026-09-29) — achado de processo (dossiê): Contrato de erro do marco com duas regras para o mesmo cabecalho: a pre-checagem de gravar_marco aceita a ## 1A por prefixo (_MARCO_VERSAO_PENDENTE_RE), e o _checar_promocao que o card prescreveu le a secao por igualdade exata (_modelo._HEADING_PENDENTE, via _localizar_secao); cabecalho com texto a mais passa a pre-checagem e derruba _checar_promocao em AttributeError (modelo_pendente None) em vez de EncerramentoError com exit 1. O card enumerou as razoes de conflito sem a 'plano sem ## 1A legivel'; a entrega seguiu o card. **Rota:** AE-<n> na secao 9 do P-0755, card corretivo que unifique a leitura do cabecalho ou acrescente a razao de conflito. **Triagem:** consultor, acionamento 17 → `DRF-62`, card corretivo `RAF-T23a`
- **AE-177** (`RAF-T23a`, fechamento, 2026-09-29) — achado de processo (dossiê): Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado pre-existente do dead_code (docs/audits/sonda-2026-09-28/passos.py, blob 8ee3de5) sem carregar a linha de base admitida no despacho; cada revisao reconcilia a mao. **Rota:** DRF-44 ja aberta na secao 9 do P-0755; registrar a reincidencia como AE-<n> apontando para ela.
- **AE-178** (`RAF-T25`, fechamento, 2026-09-29) — achado de processo (dossiê): Buraco de coerencia da DRF-14 (nao da entrega): a regra entregue manda registrar o card da operacao nova em estado.tsv blocked, razao dependencia, nota 'aguarda o aceite da versao <k> no marco', mas nenhum instrumento nem doutrina o tira de blocked quando o marco aceita a versao - encerrar.py marco --aceita-versao so reescreve o campo Operacao do modelo (promover_versao) e move a linha do PLANO a ready; no ramo --recusa-versao o card da operacao eliminada fica blocked sem destino nomeado. **Rota:** item de replanejamento do P-0755 (AE-<n> na secao 9), card que fecha a transicao do card bloqueado no aceite e o destino dele na recusa. · **Triagem:** consultor, acionamento 18 → `DRF-63`, card corretivo `RAF-T24a`
- **AE-179** (`RAF-T24a`, fechamento, 2026-09-29) — achado de processo (dossiê): Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado pre-existente do dead_code (docs/audits/sonda-2026-09-28/passos.py, blob 8ee3de5) sem carregar a linha de base admitida no despacho; a revisao reconcilia a mao a cada tarefa. **Rota:** DRF-44 ja aberta na secao 9 do P-0755; somar a reincidencia ao AE-<n> que aponta para ela.
- **AE-180** (`RAF-T26`, fechamento, 2026-09-29) — achado de processo (dossiê): Texto novo fixado pelo card diverge do comando que ele descreve (nao da entrega, que e verbatim): (a) diz que o modelador devolve 'a ## 1A e o registro acertados', mas o dossie de conflito que encerrar.py imprime (_dossie_emenda) manda 'Devolver: a secao ## 1 depois do ato e a linha nova do registro de versoes'; (b) enumera tres conflitos, e _checar_promocao tem um quarto que tambem imprime o dossie ('o plano nao tem a ## 1'). **Rota:** item de replanejamento do P-0755 (AE-<n> na secao 9), corretivo que alinha o campo Devolver do _dossie_emenda no ramo de conflito ao que a doutrina do modelador pede, ou a doutrina ao comando, e fecha a lista de conflitos. · **Triagem:** consultor, acionamento 19 → `DRF-64`, cards corretivos `RAF-T23b` e `RAF-T26a`
- **AE-181** (`RAF-T23b`, fechamento, 2026-09-29) — achado de processo (dossiê): Decisao que o card nao fechou (G-NOASK): a regra 1 de Contratos/classes pede o parametro devolver 'depois de restricao (um parametro por linha na assinatura)', o que tanto le 'o novo em linha propria' quanto 'todos os parametros um por linha'; a entrega escolheu a primeira leitura (devolver em linha propria, os seis anteriores intactos na mesma linha). Desvio de detalhe, reversivel, sem efeito em teste. **Rota:** AE-<n> na secao 9 do P-0755 para a autoria de cards fixar a forma da assinatura por bloco cercado, nao por parentetico.
- **AE-182** (`RAF-T27`, fechamento, 2026-09-29) — achado de processo (dossiê): Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado pre-existente do dead_code (docs/audits/sonda-2026-09-28/passos.py, blob 8ee3de5) sem carregar a linha de base que o proprio card admite; cada revisao reconcilia a mao. **Rota:** DRF-44 ja aberta na secao 9 do P-0755; registrar a reincidencia como AE-<n> apontando para ela. · **Triagem:** consultor, acionamento 21 → reincidência da `DRF-44`, sem ação nova
- **AE-183** (`RAF-T27`, fechamento, 2026-09-29) — achado de processo (dossiê): O card RAF-T27 fixou as tres regras e nao mandou acertar a docstring do modulo .claude/tools/prevoo.py (linhas 13-15), que segue descrevendo caminho como 'token terminado em uma das nove extensoes ou em /' e so os valores sim/nao, sem a regra de extensao curta com '/', sem o nome solto que nao comeca por '.', e sem o valor 'criar' nem a regra de verbo na mesma frase; o card tambem nao declarou aceite de coerencia do modulo (RUBRICA 8, criterio iv). A entrega seguiu o card sem decidir por conta propria, e o comportamento esta certo; so a documentacao do cabecalho do instrumento ficou falsa. **Rota:** AE-<n> na secao 9 do P-0755 com card de acerto da docstring de prevoo.py. · **Triagem:** consultor, acionamento 21 → `DRF-66`, card corretivo `RAF-T27a`
- **AE-184** (`RAF-T29`, fechamento, 2026-09-29) — achado de processo (dossiê): Criterio (viii) da rubrica (AE-12): o card acrescenta C-18 ao vocabulario do check e nao fecha a frase que o conta - a docstring do modulo .claude/tools/backlog.py segue dizendo 'C-1..C-17' e 'vocabulario do instrumento fechado em C-1..C-17' (linhas 3 e 7) e o comentario de secao da linha 592 idem; a execucao seguiu o card a letra e nao decidiu editar. **Rota:** AE-<n> na secao 9 do P-0755, card de reparo que atualize as tres frases (e qualquer outra enumeracao do vocabulario do check fora do modulo) para C-1..C-18. · **Triagem:** consultor, acionamento 22 → `DRF-67`, card corretivo `RAF-T29a`
- **AE-185** (`RAF-T29a`, fechamento, 2026-09-29) — achado de processo (dossiê): O dossie de evidencia trava guardas em nao conforme pelo achado pre-existente de dead_code (docs/audits/sonda-2026-09-28/passos.py) que a Restricao do card admite nominalmente; a evidencia nao carrega a admissao nem o estado previo ao diff, e cada revisao do P-0755 reconcilia a mao. **Rota:** AE-<n> na secao 9 do P-0755 - o review_evidence.py confronta o achado com a baseline declarada no card
- **AE-186** (`RAF-T30`, revisão, 2026-09-29) — laudo reprovado 74%, bloqueante `testes`, recomendação `escalar` (`A6a`): (1) o aviso `B1` da `RAF-T30` é inalcançável — o `rdo.py laudo` recusa o alvo `instrumento` que o aviso lê (`_ALVOS_ACHADO` e a `RUBRICA` §6 fecham quatro alvos: dossiê, doutrina, rubrica, modelo), medido `rdo: FALHOU - alvo instrumento fora de [...]`, exit 1; a chave do `B1` precisa ser decidida antes da `RAF-T34`; (2) a inserção dos cinco testes entrou antes da última linha de `tests/test_encerrar.py` e deslocou a asserção `'linha nova do registro' not in saida` do TF do marco (`test_tf_marco_recusa_devolver_sem_linha_nova_do_registro`) para o TR novo; (3) achado de rubrica: a seção *Linhas removidas* do `review_evidence.py` é textual e não vê asserção migrada de função. **Rota:** consultor de plano (`A6a`), tarefa `blocked` razão `premissa`
- **AE-187** (`RAF-T30`, emenda do modelador, 2026-09-29) — achado de instrumento: `.claude/tools/modelo.py:527-567` (`_diff_fluxo`) casa e compara as operações só pelo texto; operação com texto igual e `precisa de:`/`altera:` mudados não aparece no `show --drift`. Na versão 4 pendente, a mudança da `OP-30` (`rubrica de revisão` em `precisa de:`, a propriedade nova em `altera:`) fica fora do que o dono lê no Marco 5. **Rota:** consultor no Marco 5, junto com a validação da versão 4; a mensagem do Marco 5 ao dono carrega a mudança da `OP-30` à mão **Absorção:** `DRF-73`/`RAF-T22a` (acionamento 28 do consultor).
- **AE-188** (`RAF-T30`, fechamento, 2026-09-29) — achado de processo (dossiê): Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado preexistente do dead_code (docs/audits/sonda-2026-09-28/passos.py) sem carregar a linha de base admitida no card; a revisao reconcilia a mao a cada tarefa. **Rota:** DRF-44 ja aberta na secao 9 do P-0755; registrar a reincidencia como AE-<n> apontando para ela. **Origem:** `laudo:RAF-T30#1`
- **AE-189** (`RAF-T31`, fechamento, 2026-09-29) — achado de processo (dossiê): Vermelho mecanico de guardas vem de docs/audits/sonda-2026-09-28/passos.py, pasta nao versionada fora da entrega, e a evidencia o reporta como 'nao conforme' sem carregar a admissao que o card faz (§8 risco 5); rota: AE na §9 do P-0755 para excluir a sonda do alcance do dead_code ou declarar a admissao na bateria, e o card que absorve a sonda **Rota:** não declarada no laudo **Origem:** `laudo:RAF-T31#1`
- **AE-190** (`RAF-T31`, fechamento, 2026-09-29) — achado de processo (dossiê): Regra 4 do card manda o append com --agente ir direto a gravar_por_agente, sem checar_repetida (DFP-8); a docstring de append_row/checar_repetida segue dizendo que a recusa 'vale para todo escritor', o que deixou de ser verdade no caminho do hook; o card nao fechou se DFP-8 se aposenta (substituida pela chave de agente) ou se estende a gravar_por_agente; rota: AE na §9 do P-0755 com a decisao e o acerto da docstring **Rota:** não declarada no laudo **Origem:** `laudo:RAF-T31#2`
- **AE-191** (`RAF-T31a`, fechamento, 2026-09-29) — achado de processo (dossiê): o card deixou fora dos Passos a frase do primeiro paragrafo do docstring do modulo (telemetria.py:5-6, 'o conteudo anterior nunca e tocado por conteudo (so ganha uma linha no final)'), que segue falsa para append --agente e agora contradiz o paragrafo das linhas 8-10 reescrito por este card; rota: card de redacao sucessor (RAF-T31b) trocando a frase pela ressalva 'sem --agente', registrado como AE-<n> na secao 9 do P-0755 **Rota:** não declarada no laudo **Origem:** `laudo:RAF-T31a#1`
- **Medidas fechadas do cenário** (consultor, acionamento 25, 2026-09-29; movidas de `cenario.md` pelo teto de 15k tokens; as decisões fechadas estão na §3) — medidas dos ensaios dos corretivos já `done` e a lista de absorções da §4 do cenário até o acionamento 24:
  - `check-drift` exit 0 (2026-09-28, antes da `RAF-T1a`); `dead_code.py` exit 1, 1 achado (a sonda).
  - `RAF-T1a` Verificação 1 ensaiada em cópia: antes `coluna0=0 aninhado=1 continua=0`, depois
    `coluna0=1 aninhado=0 continua=3`; 440 linhas antes e depois. `card_check --mundo antes` OK;
    `backlog.py check` OK; `modelo.py check` OK (41 tarefas).
  - `RAF-T3a` ensaiada em cópia (`%TEMP%`, `.claude/tools` + `tests/`): regra vigente 1066
    linhas / 573 ausentes nos 41 cards; nova 501 / 0. Verificações 1-3 antes `exit 5` (árvore
    real), depois `exit 0`; V4 `exit 0` nos dois; `test_backlog.py` inteiro verde na cópia salvo
    o teste do `.gitignore` (cópia sem git). `card_check` antes e depois OK; `backlog.py check`
    OK; `modelo.py check` OK (42 tarefas).
  - `RAF-T4a` ensaiada em cópia (`%TEMP%`, as duas skills): Verificações 1-3 antes `gate=1-0`,
    `entrada=1-0`, `linhas=306-445 cr=0-445`; depois `gate=0-1`, `entrada=0-1`,
    `linhas=306-445 cr=0-0`. `check-drift` exit 0 na árvore real. Depois de gravar: `card_check
    --mundo antes` OK; `backlog.py check` OK; `modelo.py check` OK (43 tarefas); `next` = `RAF-T4a`.
  - `RAF-T6a` ensaiada em cópia (`%TEMP%\raf_t6a_ensaio`, hooks + teste): hook da árvore devolve `{}`
    para `pytest -q || echo falhou`, `false || pytest -q` e `cd x`+quebra+`pytest -q`; os 2 TF novos
    falham antes (`2 failed, 6 passed`), `8 passed` depois; nós das Verificações 1-3 antes `exit 4`
    (árvore real), depois `exit 0`. Depois de gravar: `card_check --mundo antes` OK; `backlog.py
    check` OK; `modelo.py check --plano` OK (44 tarefas); `check-drift` exit 0; `next` = `RAF-T6a`.
    A linha do `estado.tsv` do corretivo se apensa à mão (`backlog.py status` recusa id sem linha).
  - `RAF-T7a` ensaiada em cópia (`%TEMP%\raf_t7a_ensaio`): contagem de `_bytes_do_ref(` 5 → 3
    (Verificação 1 `exit 1` → `exit 0`); `-k quebra` 5 passed; `tests/test_review_evidence.py` 83
    passed na cópia e na árvore. Depois de gravar: `card_check --mundo antes` OK em `RAF-T7a` e
    `RAF-T8`; `backlog.py check` OK; `modelo.py check --plano` OK (45 tarefas); `check-drift` 0.
    `card_check` só lê `antes`/`depois` como `` `exit <n>` `` logo depois da palavra.
  - `DRF-48` gravada por script (34 contingências, invariante 13, linha na §3, triagem de
    `AE-132`/`AE-133`): `backlog.py check` OK; `modelo.py check --plano` exit 0; `check-drift` exit
    0; `card_check --mundo antes` OK em `RAF-T8`, `RAF-T31`, `RAF-T40`.
  - `RAF-T8a` ensaiada em cópia (`%TEMP%\raf_t8a_ensaio`, só a rubrica, LF sem CR): Verificação 1
    `exit 1` (`arquivos=1-0`) na árvore real, `exit 0` (`arquivos=0-1`) na cópia. Depois de gravar:
    `card_check --mundo antes` OK em `RAF-T8a` e `RAF-T12`; `backlog.py check` OK; `modelo.py check
    --plano` OK (46 tarefas); `check-drift` 0; `next` = `RAF-T8a`. Linha do `estado.tsv` apensa à mão.
  - `RAF-T9a` ensaiada em cópia (`%TEMP%\raf_t9a_ensaio`, `.claude/tools` + `tests/`): Verificação 1
    `exit 1` (`docstring=1-0`) na árvore real e na cópia, `exit 0` (`docstring=0-1`) depois; linha
    mais longa 94; `tests/test_review_evidence.py` `88 passed` depois. Depois de gravar: `card_check
    --mundo antes` OK em `RAF-T9a` e `RAF-T10`; `backlog.py check` OK; `modelo.py check --plano` OK
    (47 tarefas); `check-drift` 0; `next` = `RAF-T9a`. O arquivo de teste está `w/crlf` (1921 CR).
  - `RAF-T10a` ensaiada em cópia (`%TEMP%\raf_t10a_ensaio`, `.claude/tools` + `tests/`; scripts
    `raf_t10a_aplica.py`, `raf_t10a_testes.py` em `%TEMP%`): antes `2 failed, 1 passed`; V1 real
    `exit 5`, V2 real `exit 1` (`diff=1-2-0-0-0`); depois V1 `exit 0`, V2 `exit 0`
    (`diff=0-0-1-1-1`), `test_review_evidence.py` `93 passed`, linha nova mais longa 99; sem o
    `-c core.quotepath=false` no `_git`, o TF do rastreado cai no cabeçalho do trecho. Suítes vizinhas na cópia: as
    mesmas 38 falhas (cópia sem infra) antes e depois. Depois de gravar: `card_check --mundo antes`
    OK em `RAF-T10a` e `RAF-T11`; `backlog.py check` OK; `modelo.py check --plano` OK (48 tarefas);
    `check-drift` 0; `next` = `RAF-T10a`. `card_check` exige `--plano`/`--tarefa` nomeados.
  - `RAF-T11a` ensaiada em cópia (`%TEMP%\raf_t11a_ensaio`; scripts `raf_t11a_testes.py`,
    `raf_t11a_aplica.py`, `raf_t11a_card.py` em `%TEMP%`): V1 antes `exit 5`; com os testes e sem
    a regra `3 failed, 1 passed` (`exit 1`); depois `4 passed` (`exit 0`),
    `test_review_evidence.py` `100 passed`. Depois de gravar: `card_check --mundo antes` OK em
    `RAF-T11a`, `RAF-T12`, `RAF-T15`; `backlog.py check` OK; `modelo.py check --plano` OK (49
    tarefas); `check-drift` 0; `next` = `RAF-T11a`. Linha do `estado.tsv` apensa à mão.
    Reincidência da armadilha do heredoc: string Python não crua com `\\n` virou quebra real
    no script de teste; corrigido com `Edit` antes de rodar.
  - `RAF-T12a` ensaiada em cópia (`%TEMP%\raf_t12a_ensaio`; scripts `raf_t12a_aplica.py`,
    `raf_t12a_card.py` em `%TEMP%`): V1 antes `testes=1-0 ancoras=7-4 docstring=0` (real e cópia),
    depois `testes=0-1 ancoras=0-1 docstring=1`; `test_review_evidence.py` `100 passed`; linha nova
    mais longa 98. Os dois arquivos de código estão `w/crlf`; o ensaio os deixou LF. Reincidência
    do heredoc: `%TEMP%` + barra + `raf_` virou CR; as linhas de `RAF-T7a` e `RAF-T9a` estavam
    partidas pelo mesmo defeito; as três consertadas por bytes. Texto com barra vai por `Write`. Depois de
    gravar: `card_check --mundo antes` OK em `RAF-T12a` e `RAF-T15`; `backlog.py check` OK;
    `modelo.py check --plano` OK (50 tarefas); `check-drift` 0; `next` = `RAF-T12a`.
  - `RAF-T13a` ensaiada em cópia (`%TEMP%\raf_t13a_ensaio`; `aplica.py`, `verif.sh`, `card.md`,
    `plano_aplica.py`): V1 real `docstring=1-0 help=1-0`, cópia `docstring=0-1 help=0-1` (`exit 0`
    nos dois); linhas novas até 94; `--help` renderiza; `card_check.py` em LF (0 CR). Depois de
    gravar: `card_check --mundo antes` OK em `RAF-T13a` e `RAF-T14`; `backlog.py check` OK (sem
    `--plano`); `modelo.py check --plano` OK (51 tarefas); `check-drift` 0; `next` = `RAF-T13a`.
    Texto do card e do script por `Write`, sem heredoc (armadilha acima).
  - Marco 3 (acionamento 14): `modelo.py check --plano` exit 0 com a §1A julgada; V1/V2 da
    `RAF-T10a` `exit 0` (`3 passed`, `diff=0-0-1-1-1`); `-k acento` `5 passed`;
    `test_review_evidence.py` `102 passed`.
  - Acionamento 13: `prevoo.py` de hoje sai `exit 0` com `notas.md | sim | notas.md` e `exit 1` com
    `docs/x.md | não | —` (TR da `RAF-T27` passam antes); `C-18`, `drain: aviso` e `encerrar: B1`
    ausentes do código (TR de ausência da `RAF-T28`..`T30` passam antes).
  - `RAF-T19a` ensaiada em cópia (`%TEMP%\raf_t19a_ensaio`; `raf_t19a_testes.py`, `raf_t19a_card.md`,
    `raf_t19a_plano.py` em `%TEMP%`): `-k fora_de_sequencia` casa também o teste antigo da `V20`
    (seletor é `"so_vigente and fora_de_sequencia"`); real `exit 5`, cópia `2 passed`; sem a linha
    `and not so_vigente` o TF sai `1 failed`; `test_modelo.py` `40 passed`. Depois de gravar:
    `card_check --mundo antes` OK em `RAF-T19a` e `RAF-T21`; `backlog.py check` OK; `modelo.py
    check --plano` OK (52 tarefas); `check-drift` 0; `next` = `RAF-T19a`. Linha do `estado.tsv`
    apensa à mão. Diferença §1 × §1A medida por `diff` das faixas (v3 = contrato + §1.3).
  - `DRF-61` ensaiada em cópia (`%TEMP%\raf_t21a_ensaio`; `aplica.py`, `plano_aplica.py`): real
    `tests/test_modelo.py` `1 failed, 42 passed`, cópia com conjunto por número `43 passed`;
    `check` do `P-0754` e do `P-0755` `exit 0`; `V22` nos encerrados 1, 7, 5, 1 (iguais à
    restrição). Depois de gravar: `card_check --mundo depois` OK em `RAF-T21`; `backlog.py check`
    OK; `modelo.py check --plano` OK (52 tarefas); `backlog.py status RAF-T21 ready` gravou.
  - `RAF-T23a` ensaiada em cópia (`%TEMP%\raf_t23a_ensaio`; `teste_novo.py`, `aplica.py`, `card.md`,
    `plano_aplica.py`): real `-k cabecalho_1a` `exit 5`; cópia com o teste e sem a regra `1 failed`
    (`AttributeError`); depois `1 passed`, `test_encerrar.py` `43 passed`. Depois de gravar:
    `card_check --mundo antes` OK em `RAF-T23a` e `RAF-T30`; `backlog.py check` OK; `modelo.py
    check --plano` OK (53 tarefas); `check-drift` 0; `next` = `RAF-T23a`. Linha do `estado.tsv`
    apensa à mão. Armadilha: no Bash, `#nofilter` comenta o resto da linha — vai no fim do comando.
  - `RAF-T24a` ensaiada em cópia (`%TEMP%` pasta `raf_t24a`; `card.md`, `ensaio.py`, `aplica_plano.py`):
    Verificação 1 real `destino=0-0 cr=0`, cópia `destino=1-1 cr=0`; trecho antigo único, skill LF
    (0 CR, 445 linhas). Depois de gravar: `card_check --mundo antes` OK em `RAF-T24a` e `RAF-T27`;
    `backlog.py check` OK; `modelo.py check --plano` e `--so-vigente` OK (54 tarefas); `check-drift`
    0; `next` = `RAF-T24a`. Linha do `estado.tsv` inserida depois da `RAF-T24`.
  - `DRF-64` ensaiada em cópia (`%TEMP%` pasta `raf_t23b`; `ensaio.py` com fases `copiar`, `testes`,
    `codigo`, `doutrina`; `testes_novos.py`, `card_t23b.md`, `card_t26a.md`, `aplica_plano.py`): real
    `-k devolver` `exit 5`; com os testes e sem a regra `2 failed`; depois `2 passed`,
    `test_encerrar.py` `45 passed`; `devolver=1-0` → `0-1`; modelador `conflito=1-0` → `0-1` (LF, 0
    CR); `test_doutrina_unidade.py` `8 passed` (cópia precisa de `GOVERNANCA.md` e `README.md`).
    Depois de gravar: `card_check --mundo antes` OK em `RAF-T23b`, `RAF-T26a`, `RAF-T27`; `backlog.py
    check` OK; `modelo.py check --plano` e `--so-vigente` OK (56 tarefas); `check-drift` 0; `next` =
    `RAF-T23b`. Verificação com crase no `python -c` evitada (PowerShell toma a crase por escape).
  - `DRF-66` ensaiada em cópia (`%TEMP%` pasta `raf_t27a`; `aplica.py` fases `ensaio` e `plano`,
    `card.md`, `drf66.txt`): `prevoo.py` está CRLF na árvore (222 CR), o texto antigo casa só em
    CRLF; V1 real `docstring=1-0-0 linhas=222`, cópia `docstring=0-1-1 linhas=227`, linha nova até
    98. Depois de gravar: `card_check --mundo antes` OK em `RAF-T27a`; `backlog.py check` OK;
    `modelo.py check --plano` e `--so-vigente` OK (57 tarefas, versão 3); `check-drift` 0; `next` =
    `RAF-T27a`. Armadilha: `Path.write_text` no Windows grava CRLF — ler o `card.md` tirando o CR.
  - `DRF-67` ensaiada em cópia (`%TEMP%` pasta `raf_t29a`; `ensaio.py`, `card.md`, `aplica_plano.py`):
    `backlog.py` LF (0 CR, 2612 linhas); V1 real `vocabulario=3-0-0 linhas=2612`, cópia
    `vocabulario=0-3-1 linhas=2613`, linha nova até 92, compila. Depois de gravar: `card_check --mundo
    antes` OK em `RAF-T29a` e `RAF-T36`; `backlog.py check` OK; `modelo.py check --plano` e
    `--so-vigente` OK (58 tarefas, versão 3); `check-drift` 0; `next` = `RAF-T29a`.
  - Absorções até o acionamento 24: Nenhum além dos absorvidos (`AE-121` → `DRF-44`; `AE-122` → `DRF-43`/`RAF-T1a`;
  `AE-125` → `DRF-45`/`RAF-T3a`; `AE-126` → `DRF-46`/`RAF-T4a`; `AE-130` → `DRF-47`/`RAF-T6a`;
  `AE-132`/`AE-133` → `DRF-48`; `AE-135` → `DRF-49`/`RAF-T7a`; `AE-137` → `DRF-50`/`RAF-T8a`;
  `AE-140` → `DRF-51`/`RAF-T9a`; `AE-142`..`AE-145` → `DRF-52`/`RAF-T10a`; `AE-149` →
  `DRF-53`/`RAF-T11a`; `AE-151` → `DRF-54`/`RAF-T12a`; `AE-155`..`AE-157` → `DRF-55`/`RAF-T13a`;
  `AE-158` → `DRF-56`; `AE-161`/`AE-162` → `DRF-57`; `AE-169` → `DRF-59`/`RAF-T19a`; `AE-170` →
  `DRF-60`; `AE-176` → `DRF-62`/`RAF-T23a`; `AE-178` → `DRF-63`/`RAF-T24a`; `AE-180` →
  `DRF-64`/`RAF-T23b`, `RAF-T26a`; `AE-183` → `DRF-66`/`RAF-T27a`; `AE-184` → `DRF-67`/`RAF-T29a`; `AE-186` → `DRF-68`/`RAF-T30a`,
  redespacho da `RAF-T30`; `AE-190` → `DRF-69`/`RAF-T31a`; `AE-189`, `AE-188`, `AE-185` e `AE-182` reincidem a
  `DRF-44`). O laudo da `RAF-T26` traz também reincidência da `DRF-44`, sem
  `AE-<n>` na §9 até este acionamento (registro é da condução). `AE-168`, `AE-167`, `AE-166`, `AE-160`, `AE-153`, `AE-154`, `AE-152`, `AE-136`, `AE-138`, `AE-139`, `AE-141`, `AE-146`, `AE-147`, `AE-148`
  reincidências da `DRF-44`. `AE-120` sem ação. `AE-123`,
  `AE-124`, `AE-127`, `AE-128`, `AE-129`, `AE-131`, `AE-134` são reincidências da `DRF-44` (sem
  ação nova; oito revisões reconciliaram o mesmo vermelho à mão).
- **AE-192** (`RAF-T32`, fechamento, 2026-09-29) — achado de processo (dossiê): Reincidencia: a evidencia marca guardas nao conforme pelo dead_code da sonda nao rastreada docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado) que o card admite; a revisao reconcilia a mao (passo 3a). **Rota:** somar ao AE da §9 do P-0755 que ja aponta para DRF-44 **Origem:** `laudo:RAF-T32#1`
- **AE-193** (`RAF-T32`, fechamento, 2026-09-29) — achado de processo (dossiê): O recorte do card deixa o modulo incoerente: a regra 3 troca a tarefa nos ramos PreToolUse e PostToolUse sincrono do Agent e proibe mexer no UserPromptSubmit, mas o retorno assincrono (PostToolUse com handback=send, frase de volta no UserPromptSubmit <agent-message>) segue com tarefa_corrente; exercitado na revisao: 'Agente consultor recebe a tarefa "Outro"' seguido de 'Agente consultor devolveu a tarefa "Um"'. Alem disso o ramo PostToolUse sincrono alterado nao tem teste exigido pelo card, e ID casado sem card (localizar_card devolve o proprio ID) mostra o ID em vez de cair na tarefa corrente, como a regra 2 manda. **Rota:** item de replanejamento na §9 do P-0755 (card irmao que guarde o titulo despachado em pendentes[agentId] e teste o PostToolUse) **Origem:** `laudo:RAF-T32#2`
- **AE-194** (`RAF-T33`, fechamento, 2026-09-29) — achado de processo (dossiê): O dossie de evidencia reporta dead_code vermelho sem marcar a causa como anterior a tarefa (docs/audits/sonda-2026-09-28/passos.py, fora dos alvos); cada revisao do P-0755 reconcilia o mesmo vermelho a mao. **Rota:** item de replanejamento do P-0755, junto ao AE-192 ja registrado - a evidencia deve atribuir o vermelho de guarda por arquivo, como faz com os tocados. **Origem:** `laudo:RAF-T33#1`
- **AE-195** (`RAF-T34`, fechamento, 2026-09-30) — achado de processo (dossiê): o dossie de evidencia marca guardas vermelho pelo dead_code de docs/audits/sonda-2026-09-28/passos.py sem carregar que o vermelho e anterior a tarefa e fora dos alvos (DRF-44); o reviewer reconciliou re-rodando. **Rota:** item de replanejamento do P-0755 (AE na secao 9) para review_evidence.py marcar vermelho de guarda atribuivel a arquivo alheio, como ja faz com os tocados **Origem:** `laudo:RAF-T34#1`
- **AE-196** (`RAF-T34`, fechamento, 2026-09-30) — achado de processo (dossiê): o trecho de diff do alvo trunca em 4000 caracteres no meio do hunk do molde (Passo 2), e a linha nova 'despacho: P-<n> <ID do card em triagem>' so se le abrindo o repositorio. **Rota:** item de replanejamento do P-0755 (AE na secao 9) para o teto do trecho de diff nao cortar hunk de alvo **Origem:** `laudo:RAF-T34#2`
- **AE-197** (`RAF-T35`, fechamento, 2026-09-30) — achado de processo (dossiê): reincidencia da DRF-44 (AE-195 do RAF-T34): o dossie de evidencia marca guardas vermelho pelo dead_code da sonda nao rastreada docs/audits/sonda-2026-09-28/passos.py sem carregar que a causa e anterior a tarefa e alheia aos alvos; o reviewer reconciliou re-rodando. **Rota:** item de replanejamento do P-0755 ja aberto na secao 9 (DRF-44), sem card novo **Origem:** `laudo:RAF-T35#1`
- **AE-198** (`RAF-T35`, fechamento, 2026-09-30) — achado de processo (dossiê): reincidencia do AE-196: o trecho de diff do alvo trunca em 4000 caracteres dentro da linha unica do item 3, e a substituicao so se confirma abrindo o repositorio (confirmada: trecho antigo 1 vez, linha nova igual a antiga com o trecho novo inserido, numstat 1/1). **Rota:** item de replanejamento do P-0755 ja aberto na secao 9 (AE-196) **Origem:** `laudo:RAF-T35#2`
- **AE-199** (`RAF-T22a`, fechamento, 2026-09-30) — achado de processo (dossiê): Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado pre-existente do dead_code (docs/audits/sonda-2026-09-28/passos.py) sem carregar a linha de base que o proprio card admite; cada revisao reconcilia a mao. **Rota:** DRF-44 ja aberta na secao 9 do P-0755; registrar a reincidencia como AE-<n> apontando para ela. **Origem:** `laudo:RAF-T22a#1`
- **AE-200** (`RAF-T22a`, fechamento, 2026-09-30) — achado de processo (dossiê): O card fixou a forma '[~] OP-<k> — precisa de: <vigente> => <pendente>' com listas unidas por ', ' e nao fechou a lista vazia: operacao cujo precisa de/altera sai de ou vai para vazio emite 'precisa de:  => z' (dois espacos, lado em branco), exercitado na revisao via montar_drift. A entrega aplicou a regra ao pe da letra, sem decisao propria. **Rota:** AE-<n> na secao 9 do P-0755, sem acao salvo se o dono quiser marcador de vazio (ex.: '—') num card futuro. **Origem:** `laudo:RAF-T22a#2`
- **AE-201** (`RAF-T37`, fechamento, 2026-09-30) — achado de processo (dossiê): reincidencia da DRF-44 (AE-195 do RAF-T34, repetida no RAF-T36): o dossie de evidencia marca guardas vermelho pelo dead_code da sonda nao rastreada docs/audits/sonda-2026-09-28/passos.py sem carregar que a causa e anterior a tarefa e alheia aos alvos; o reviewer reconciliou re-rodando. **Rota:** item de replanejamento do P-0755 ja aberto na secao 9 (DRF-44), sem card novo **Origem:** `laudo:RAF-T37#1`
- **AE-202** (`RAF-T38`, fechamento, 2026-09-30) — achado de processo (dossiê): reincidencia da DRF-44 (AE-195 do RAF-T34, repetida no RAF-T36 e RAF-T37): o dossie de evidencia marca guardas vermelho pelo dead_code da sonda nao rastreada docs/audits/sonda-2026-09-28/passos.py sem carregar que a causa e anterior a tarefa e alheia aos alvos; o reviewer reconciliou re-rodando. **Rota:** item de replanejamento do P-0755 ja aberto na secao 9 (DRF-44), sem card novo **Origem:** `laudo:RAF-T38#1`
- **AE-203** (`RAF-T39`, fechamento, 2026-09-30) — achado de processo (dossiê): reincidencia da DRF-44 (AE-195 do RAF-T34, repetida em RAF-T36..T38): o dossie de evidencia marca guardas vermelho pelo dead_code da sonda nao rastreada docs/audits/sonda-2026-09-28/passos.py sem carregar que a causa e anterior a tarefa e alheia aos alvos; reconciliado pelo reviewer. **Rota:** item de replanejamento do P-0755 ja aberto na secao 9 (DRF-44), sem card novo **Origem:** `laudo:RAF-T39#1`
- **AE-204** (`RAF-T39`, fechamento, 2026-09-30) — achado de processo (dossiê): o bloco que o card ditou manda a entrega ser 'a celula o que o dono le' da linha do marco, mas o exemplo do Marco 2 usa a celula aparada ('etapa A, custo da orquestracao', sem a lista R-01..R-24), e a celula do Marco 1 e um comando, nao o nome de uma entrega; alem disso o primeiro paragrafo do Relatorio de encerramento (intocavel pelo card) segue dizendo que o relatorio abre com o modelo.py show, sem remissao a excecao do marco. **Rota:** item de replanejamento do P-0755 na secao 9 (AE-<n> pela conducao), para a RAF-T40 ou o Marco 6 fixarem se a celula entra inteira ou so ate os dois-pontos **Origem:** `laudo:RAF-T39#2`
- **AE-205** (`RAF-T39a`, fechamento, 2026-09-30) — achado de processo (dossiê): reincidencia da DRF-44 (AE-195 do RAF-T34, repetida de RAF-T36 a RAF-T39): o dossie de evidencia marca guardas vermelho pelo dead_code da sonda nao rastreada docs/audits/sonda-2026-09-28/passos.py sem carregar que a causa e anterior a tarefa e alheia aos alvos; reconciliado pelo reviewer. **Rota:** item de replanejamento do P-0755 ja aberto na secao 9 (DRF-44), sem card novo **Origem:** `laudo:RAF-T39a#1`
- **AE-206** (`RAF-T40`, fechamento, 2026-09-30) — achado de processo (dossiê): reincidencia da DRF-44 (AE-195 do RAF-T34, repetida de RAF-T36 a RAF-T40): o dossie de evidencia marca guardas vermelho pelo dead_code da sonda nao rastreada docs/audits/sonda-2026-09-28/passos.py sem carregar que a causa e anterior a tarefa e alheia aos alvos; reconciliado pelo reviewer. **Rota:** item de replanejamento do P-0755 ja aberto na secao 9 (DRF-44), sem card novo **Origem:** `laudo:RAF-T40#1`
