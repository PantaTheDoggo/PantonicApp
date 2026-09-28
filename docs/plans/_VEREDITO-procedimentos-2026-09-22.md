# Veredito dos procedimentos recentes, medido no planejamento do `P-0747`

**Data:** 2026-09-22 · **Sessão:** planejamento do consultor de plano (`P-0747`), conduzida no
contexto principal com o `pantonic-planner`, o `pantonic-model-designer` e três `pantonic-scout`
como subagentes · **O que se julga:** os procedimentos publicados pelo `P-0743` (modelador dono da
`## 1`, `modelo.py check`), pelo `P-0745` (SAÍDA 3, um card por operação, `V1`/`V3` como lastro do
planejador) e pelo `P-0746` (lastro obrigatório, duas vias, tipo de objeto, requisitos
secundários, rascunho substituído no lugar antes do Marco 1) — na primeira aplicação inteira a um
plano real · **Estatuto:** insumo para a revisão de doutrina pendente (`TK-67`) e para a régua de
autoria de card (`TK-72`). Nada aqui é norma.

---

## 1. O que a sessão produziu

`docs/plans/P-0747-consultor-de-plano.md`: 2.524 linhas, `## 0` com o pedido e oito atos do dono
como lastro, modelo com 5 objetos (1 de escopo, 2 externos, 2 de medição), 8 operações, 12
propriedades, 8 cards `CON-T1`..`CON-T8`, 22 decisões `DCS-*`, superfície de 47 residências
(`F-4`). `modelo.py check` e `backlog.py check` em exit `0`, conferidos pelo condutor. Plano
`blocked` até o `go` do dono no Marco 1. Nenhuma pergunta subiu ao dono durante o planejamento.

## 2. O custo, medido nas notificações de conclusão

| papel | acionamentos | tool uses | tokens | duração |
|---|---|---|---|---|
| planejador (Opus) | 5 (1 frio + 4 retomadas por mensagem) | 122 | 816,9k | 55,3 min |
| modelador (Opus) | 3 (1 frio + 2 retomadas) | 80 | 384,0k | 16,5 min |
| scouts (Haiku) | 3, em paralelo | 61 | 131,4k | 5,8 min |
| **total dos subagentes** | 11 | 263 | **1.332,3k** | ~77 min |

Linhas em `docs/telemetria.tsv` (`P-0747-planner-1..5`, `P-0747-modelador-1..3`,
`P-0747-scout-1..3`). O contexto do condutor não é medido pelo harness e fica fora.

Referência: a série de sessões de planejamento tinha **uma** linha antes desta
(`RPC-P0735-planejamento`, 183k). Esta sessão é a segunda amostra e é 7× maior — não se lê
tendência, lê-se que a forma nova custa outra ordem de grandeza e que a série precisa de mais
pontos antes de qualquer régua.

**Onde o custo foi:** a última retomada do planejador (332,8k, 70 tool uses, 38 min) contém o
**ensaio** — a cópia da árvore em pasta temporária com os oito cards aplicados em sequência e cada
comando de `Verificação` rodado antes e depois. É o `DM-12` levado ao limite, e é o que faz os
números publicados nos cards serem medidos e não deduzidos. As retomadas 3 e 4 (333k somados) e as
autorias 2 e 3 do modelador (294k somados) são o vaivém de três dossiês antes do primeiro card,
tratado na §3.2.

## 3. Veredito por procedimento

### 3.1 SAÍDA 1 — a campanha de investigação por scouts · **ressalva forte**

Funcionou na forma e falhou na substância. O planejador frio devolveu, com 4 tool uses, sete
perguntas fechadas bem formadas e seis decisões pré-tomadas. Os scouts responderam em paralelo
em menos de 6 minutos. Mas a pergunta central — *quem roteia parada em volta do consultor* — voltou
com **22** residências; o grep do próprio planejador, feito ao verificar os cards, achou **43**; a
partição por linha achou **47**. Duas das três rodadas de reautoria do modelo nasceram desse
buraco, não de erro de modelagem.

É a classe *censo por enumeração não é censo* (`docs/OPERACOES_AS_IS_P-0745.md`, degrau 2),
repetida por um papel diferente. Causa: a pergunta foi semântica ("linhas que mandam parada ao
planejador ou ao dono") e o Haiku respondeu por amostra; o Haiku também hesitou numa contagem
simples (4 ou 5 ocorrências) em vez de devolver o número. Para censo de superfície, o scout serve
quando a pergunta é um **grep literal com padrão e contagem** que o planejador pode re-rodar para
conferir — não uma pergunta de leitura.

Consequência a decidir (dono): o `pantonic-planner` diz que `Bash` serve a um único uso (comando
de aceite). Nesta sessão ele usou grep de superfície para verificar a `F-4` e foi isso que
salvou o plano. Ou a regra ganha a exceção nomeada *grep de verificação de superfície, com o
padrão publicado no fato*, ou a campanha passa a exigir, para toda lista de residências, o
padrão de grep e a contagem que o scout rodou. Residência: `TK-72` ou `TK-67`.

### 3.2 SAÍDA 3 e a autoria pelo modelador · **aprovado, com o custo do vaivém anotado**

O planejador não escreveu uma linha da `## 1` e devolveu o dossiê de seis campos fechado; o
modelador escreveu a seção inteira sobre ele. A regra *rascunho antes do Marco 1 se substitui no
lugar* foi exercida **três vezes** e funcionou: sem bloco irmão, sem versão nova, a linha da
versão 1 reescrita a cada vez.

O que a série de três versões mostra: a **estrutura** do modelo não mudou (5/8/12 nas três; o
objeto de escopo, os externos e os de medição foram os mesmos desde a primeira). O que mudou foi
o **contrato** (a partição das residências entre operações) e o texto de seis operações, e a
causa das três voltas foi a `F-4` do planejador crescer de 22 para 43 para 47 itens. Ou seja: a
modelagem foi estável e a base de fatos foi o elo fraco. Com a `F-4` completa desde a
campanha, o modelo teria saído certo na primeira autoria.

O teste de dimensionamento da Fase 4 (*propriedade alterada que a operação não declara*) foi o
que apanhou o terceiro defeito — a forma da figura morando também no corpo do agente, e a
`description` amarrada à regeneração do índice pelo gate de drift. É exatamente o sinal que a
norma prevê como "operação mal recortada volta ao modelador". O mecanismo está certo.

### 3.3 `V1`/`V3` como lastro do planejador · **aprovado**

Exercido três vezes sem ruído: o modelador devolveu a saída literal do `check` com oito `V3`,
nomeou-as como não suas e o condutor as roteou à decomposição. O primeiro card fez o `check`
sair de `1` para `0`. Nada a mudar.

### 3.4 O contrato copiado no card · **reprovado na forma atual**

A regra manda o card copiar, em `precisa de:`, o contrato de cada objeto de que a operação
precisa. O contrato do objeto de escopo deste plano tem ~600 palavras — a partição inteira das 47
residências, as exclusões, os intocados —, e foi copiado nos oito cards, ao lado dos contratos
dos outros quatro objetos. Cada card carrega uma página de contrato antes do primeiro passo;
`CON-T3` tem 259 linhas para 11 substituições literais. O plano ficou com 2.524 linhas para 8
cards (o `P-0745`, na forma antiga, tinha 2.620 para 10).

O executor frio não ganha nada com a partição das outras sete operações: ele tem
`Arquivos-alvo`. Proposta para o `TK-72`: o contrato copiado no card se limita ao que **este** card
precisa (o contrato do objeto, sem a partição alheia), e lista de residências vive por ponteiro
no fato da `## 2` — que é o que o próprio modelador fez dentro do modelo na segunda autoria, e
que a regra do card desfez ao copiar.

### 3.5 A forma da devolução do modelador · **a regra está errada em dois pontos**

O `pantonic-model-designer` manda devolver "a seção inteira e literal … nenhuma prosa fora da
seção, nenhum comentário, nenhuma recomendação". O modelador desviou duas vezes, e as duas
vezes acertou: não copiou 94 linhas que já estavam no arquivo (devolveu ponteiro, cabeçalho de
estado, linha da versão e saída do `check`), e devolveu **fora da seção** o achado de que quatro
linhas de `GOVERNANCA.md` e do próprio arquivo dele ficavam fora da `F-4` — o achado mais útil da
primeira autoria, que a regra proíbe. Proposta: a devolução passa a ser ponteiro + cabeçalho +
linha da versão + `check` literal + um campo nomeado `Achados fora da seção`, que quem conduz
roteia ao planejador.

### 3.6 Lastro, duas vias, tipo de objeto e requisitos secundários (`P-0746`) · **aprovado**

Primeira aplicação inteira. Todo objeto, operação e propriedade cita um dos oito atos do dono ou o
pedido; *parada de executor* e *acionamento do consultor* como objetos de **medição** deram ao
plano um critério de aceite observável antes e depois (o caminho da parada, o custo do
acionamento) sem inflar o escopo; *planejador* e *modelador* como **externos** delimitaram a
fronteira sem que o plano prometa transformá-los. Os requisitos secundários ficaram com duas
linhas — o resto tinha lastro.

Uma coisa a reconhecer na norma: o "enunciado" aqui não foi um prompt — foi **uma frase do dono
mais oito atos registrados em datas diferentes**, transcritos pelo condutor na `## 0`. A doutrina
fala em "enunciado do problema ou prompt de origem"; o caso medido mostra que o enunciado
composto de atos registrados é forma legítima e frequente, e a norma deveria nomeá-la, com a
exigência de que cada ato entre com data e ponteiro.

### 3.7 "Nenhum agente aciona outro" e a retomada por mensagem · **aprovado, com uma medida a fazer**

O condutor despachou tudo; nenhum agente chamou outro. O planejador foi retomado quatro vezes
**por mensagem**, com o contexto intacto, e o modelador duas — em vez da "invocação nova" que o
protocolo do planejador prevê para quem foi chamado como subagente. A retomada evitou reler o
plano, a spec e a campanha a cada volta. O que não se mediu: o custo em dólares — os intervalos
entre retomadas passaram de 5 minutos, então o cache do subagente provavelmente expirou e o
contexto foi reescrito a preço cheio (a mesma anatomia medida no consultor, spec §11). A
comparação retomada × invocação fria, em dólares, é medida a fazer antes de a doutrina escolher.

### 3.8 O ensaio dos cards em árvore temporária · **aprovado; é a prática que vale o custo**

O planejador aplicou os oito cards em sequência numa cópia da árvore e mediu antes e depois de
cada comando de `Verificação`, incluindo o gate de drift ficando vermelho no meio da `CON-T8`
e verde depois. É a primeira sessão em que **todo** literal de aceite publicado foi rodado, e é a
resposta à classe de defeito que mais apareceu no `P-0745` (número que envelhece, comando que
responde à pergunta errada). Custou 333k de tokens e 38 minutos. Manter, e nomear no
`pantonic-planner` como o modo normal da Fase 4, não como exceção.

## 4. Matéria para o dono no Marco 1

Quatro decisões técnicas do planejador tocam fronteira de papel ou conduta do loop e merecem
leitura antes do `go`, porque o modelo as materializa:

1. **`DCS-5` — drift para o loop.** A `DC-2` (2026-09-22) foi lida ao pé da letra: havendo drift,
   o loop **para** e leva o dossiê de emenda ao dono. O ato do dono de 2026-09-21 no `P-0746` diz
   que *"o loop autônomo carrega o drift até o marco"*. As duas leituras são compatíveis se o
   "pedido que sobe" for o do marco; o plano escolheu a parada imediata. É a decisão de maior
   efeito sobre a autonomia do loop.
2. **`DCS-4` — o consultor autora o card corretivo `T<n>a` e apensa o id à lista `tarefas:`.** Era
   empréstimo medido (spec §4) e vira atribuição. Vai ao planejador só quando emenda aceita cria ou
   remove operação, ou quando a premissa cai inteira.
3. **`DCS-6`/`DCS-7` — o piloto da forma efêmera roda na execução deste próprio plano**, com
   adoção se a média ficar abaixo de $3,7 por acionamento e zero reprovações por perda de cenário;
   `DCS-22` conta reprovação e retentativa sem atribuir causa.
4. **`DCS-18` — plano não-pronto no gate e contexto acabando dentro da tarefa seguem ao
   planejamento**, fora da triagem do consultor.

## 5. Ruído do harness observado

O hook `UserPromptSubmit` injetou, no meio da sessão de planejamento, a "PRÓXIMA TAREFA:
`TK-65a`" com o dossiê inteiro — contexto de outra iniciativa entrando numa sessão que a Regra 2
manda manter coesa. E o gate `modelo-por-fase` pediu Opus numa sessão que o dono abriu em Fable,
que a matriz admite "só sob solicitação explícita do dono" — a solicitação é a própria escolha do
modelo na sessão; o gate não reconhece o caso. Os dois são matéria de `modelo-por-fase` e do hook,
não deste plano.
