# Operações as-is — o que o `P-0747` deixou no lugar

Documento de encerramento do plano `docs/plans/P-0747-consultor-de-plano.md`, redigido em
2026-09-23 na branch `plan/planner-modelo-escopo`, sem commit. Descreve **as operações que existem
hoje**. Todo número abaixo foi re-derivado por comando nesta data; o registro da execução mora no
plano (`## 9. Achados da execução`) e nos dezessete arquivos `docs/RDO/P-0747-CON-T*.md`.

Na mesma janela, antes do plano, rodou o tíquete `TK-76a`: as três tabelas do modelo de um plano
passam a ser escritas em frases curtas, para o dono ler. Ele muda a forma de modelos futuros, deixa
este plano intocado e fica fora da contagem de tarefas abaixo.

---

## O problema

Quando um agente executor devolve um card sem conseguir entregá-lo, alguém decide o que fazer com
essa devolução. Antes do plano, a decisão tinha dois donos escritos ao mesmo tempo.

- **47 residências** do kit — linhas de doutrina, das skills, das definições de agente e da regra
  global, contadas na abertura do plano — roteavam essa devolução ou citavam o consultor, e a
  maioria a mandava **direto a quem planeja**. A especificação do consultor
  (`docs/consultant-spec.md`) mandava **toda** devolução ao consultor e declarava prevalecer. O
  loop que conduz um plano tinha duas regras para o mesmo evento.
- O consultor (`.claude/agents/pantonic-consultant.md`) era figura **provisória**: a descrição
  curta dizia *"Figura ad-hoc, provisória"*, o arquivo declarava estar fora da doutrina, e a
  matriz de responsabilidades de `GOVERNANCA.md` §3 não tinha linha dele.
- A figura rodava **de prontidão**: uma instância por plano, mantida viva e retomada a cada
  escalonamento. No plano anterior, essa instância cresceu de **70,3k para 368,5k tokens** em oito
  acionamentos. O custo medido ia de **$3,7 a $4,5 por acionamento**, e de 25% a 48% dele era
  reescrita de cache, porque o cache de um subagente expira em cinco minutos.
- A especificação deixava **sete lacunas** abertas — forma do handover, residência da
  estatística, autoria de card novo, critério de não-acionamento, caminho de poluição, forma da
  figura e disciplina de saída —, e o histórico dos acionamentos existia só em prosa.

## A solução, em uma frase

A figura provisória vira papel de doutrina: toda devolução de card passa por uma triagem única, que
entrega ao loop a rota escrita numa linha que a máquina lê, e cada acionamento nasce numa instância
nova que lê o estado do plano de um arquivo.

## Vocabulário mínimo

| termo | o que é |
|---|---|
| **parada** | a devolução de um card sem entrega: o executor responde `blocked` com um motivo — `premissa` (o card está errado), `dependencia` (falta algo que outro card entrega) ou `ferramenta` (o harness negou uma ferramenta). Conta também o laudo do revisor com pendência substantiva |
| **laudo** | o julgamento que o agente revisor emite sobre a entrega de um card: veredito (`aprovado`, `ressalva`, `reprovado`), percentual e recomendação (`seguir`, `seguir com ressalva`, `refazer`, `escalar`) |
| **loop** | a skill `.claude/skills/scrum-master/SKILL.md`, que conduz um plano card a card: despacha executor e revisor e roteia o resultado por uma tabela de regras nomeadas (`A1`..`A9` para a tarefa, `B0`..`B4` para a janela) |
| **triagem** e **rota** | o ato do consultor sobre uma parada. A primeira linha do que ele devolve é a rota: `rota=resolve` (ele mesmo repara o plano), `rota=modelador` (o reparo muda o modelo do plano) ou `rota=planejador` (o plano precisa de rodada de replanejamento) |
| **modelo**, **drift** e **marco** | o modelo é a seção `## 1` do plano: objetos, operações e estados finais. Drift é decisão que muda o que está lá; ela nasce como **versão pendente** ao lado da vigente, e é validada ou recusada no **marco**, o ponto de validação do dono |
| **prontidão** e **forma efêmera** | as duas formas da figura. Prontidão: uma instância por plano, viva entre acionamentos. Efêmera: uma instância nova por acionamento, que se encerra ao devolver a rota |
| **cenário** | o arquivo `docs/plans/_CENARIO-<plano>.md`, com teto de 15k tokens, que carrega entre instâncias efêmeras as decisões vivas, a fila, os achados abertos e a matéria inconclusiva do plano |
| **card corretivo** | card com sufixo de letra (`CON-T3a`, `CON-T3b`) aberto durante a execução para reparar a entrega de um card irmão; soma-se à operação do modelo que o card irmão materializa |
| **residência** | o arquivo e a seção onde uma regra mora. A mesma regra em duas residências diverge no primeiro ajuste |

---

## O arco — os estratos

O modelo do plano tem **oito operações** em quatro blocos, e cada card materializa uma delas. O
plano nasceu com **oito cards de autoria** e fechou com **dezessete**: os nove corretivos nasceram
durante a execução, cada um de um laudo de revisão, e cada um se somou à operação que repara.

| estrato | operação | pergunta que responde | cards |
|---|---|---|---|
| **A — a doutrina** | `OP-1` | onde a figura existe como papel? | `CON-T1` |
| | `OP-2` | o que a própria definição do consultor manda ele fazer? | `CON-T2`, `CON-T2a` |
| **B — o loop** | `OP-3` | o que o loop faz com cada parada e com cada rota devolvida? | `CON-T3`, `CON-T3a`, `CON-T3b`, `CON-T3c` |
| | `OP-4` | como nasce, trabalha e morre cada instância do consultor? | `CON-T4`, `CON-T4a` |
| **C — os outros lados** | `OP-5` | o que dizem os demais papéis sobre a parada? | `CON-T5`, `CON-T5a` |
| | `OP-6` | que lugar sobra para a especificação? | `CON-T6`, `CON-T6a` |
| **D — a medida e a porta** | `OP-7` | a forma efêmera sai mais barata que a prontidão? | `CON-T7`, `CON-T7a` |
| | `OP-8` | o que a porta de entrada do repositório anuncia? | `CON-T8`, `CON-T8a` |

Cada estrato é inútil sem o anterior. O loop só cita a figura depois de a norma dizer que ela é
papel (A antes de B). Os demais papéis repetem o destino da parada que A e B fixaram (C depois de
B). A medida exige a forma efêmera instalada, e a porta de entrada descreve a forma que a medida
deixou vigente (D por último).

A ordem de execução segue essa lógica com um desvio deliberado: a forma efêmera (`CON-T4`) roda
cedo, para alargar a janela da medida. Por isso os acionamentos 1 a 3 do consultor rodaram de
prontidão e os acionamentos 4 a 9 na forma efêmera. A fila executada foi `CON-T1` → `CON-T2` →
`CON-T3` → `CON-T3a` → `CON-T4` → `CON-T2a` → `CON-T3b` → `CON-T4a` → `CON-T3c` → `CON-T5` →
`CON-T6` → `CON-T5a` → `CON-T6a` → `CON-T7` → `CON-T7a` → `CON-T8` → `CON-T8a`.

Nenhum card ficou fora de estrato, e nenhum foi `cancelled`.

---

## O modelo do plano no fechamento

A **versão 1** do modelo é a vigente, aceita no Marco 1. A **versão 2** está **pendente**: nasceu
de quatro atos de conflito durante a execução, cada um aberto quando um laudo mostrou que a entrega
dizia mais que o modelo. Nenhum dos quatro muda objeto. O comando que mostra a diferença entre as
duas:

```
$ python .claude/tools/modelo.py show --plano docs/plans/P-0747-consultor-de-plano.md --drift
# Drift do modelo — P-0747 — O consultor de plano: a figura, a triagem de toda parada e a fronteira com o planejador
vigente: versão 1 · 2026-09-22   pendente: versão 2 · 2026-09-23

## Fluxo
[~] OP-3 — O mantenedor do loop reescreve a condução das paradas: as duas fontes normativas da skill passam a citar as decisões deste plano, toda regra que roteia parada de executor ou laudo com pendência substantiva e o guardrail que manda a matéria ao planejador passam a levá-los ao consultor, o loop despacha a rota que ele devolve e, quando a rota é o modelador, despacha o modelador sem parar a janela e leva o pedido de validar o drift ao dono no marco. => O mantenedor do loop reescreve a condução das paradas: as duas fontes normativas da skill passam a citar as decisões deste plano, toda regra que roteia parada de executor ou laudo com pendência substantiva e o guardrail que manda a matéria ao planejador passam a levá-los ao consultor, o loop despacha a rota que ele devolve e, quando a rota é o modelador, despacha o modelador sem parar a janela e leva o pedido de validar o drift ao dono no marco; quando o consultor classifica o impedimento como estratégico, o loop para em qualquer rota e leva ao dono a classificação, a rota e o pedido de emenda, se houver; em resolver e em modelador para sem executar a ação e sem despachar o modelador, e em planejador executa a ação, que já é a parada.
[~] OP-5 — O autor de papéis escreve o outro lado da fronteira em toda definição de conduta que ainda manda a parada direto ao replanejamento: quem planeja passa a receber a rodada pela rota da triagem, quem escreve o modelo passa a nomear o consultor como origem da emenda e como quem estende a lista de tarefas, quem executa e quem revisa passam a devolver a parada e a pendência à triagem, e a regra de transição de estado do diário, a passagem de bastão e a regra global de não decidir passam a dizer o mesmo. => O autor de papéis escreve o outro lado da fronteira em toda definição de conduta que ainda manda a parada direto ao replanejamento: quem planeja passa a receber a rodada pela rota da triagem, quem escreve o modelo passa a nomear o consultor como origem da emenda e como quem estende a lista de tarefas, quem executa e quem revisa passam a devolver a parada e a pendência à triagem, e as regras do diário sobre revisão pedida e transição de estado, a passagem de bastão e a regra global de não decidir passam a dizer o mesmo.

## Estado final
[~] consultor.alcance da triagem das paradas — toda parada de executor — `premissa`, `dependencia` ou `ferramenta` — e todo laudo com pendência substantiva chegam ao consultor, que devolve uma rota entre resolver, modelador e planejador, e o loop a despacha; o motivo é evidência, não rota; nenhum dos 47 itens de `F-4` manda a parada direto ao planejador, e as duas fontes normativas da skill do loop citam as decisões deste plano; o que `DCS-18` deixa fora continua indo ao planejamento => toda parada de executor — `premissa`, `dependencia` ou `ferramenta` — e todo laudo com pendência substantiva chegam ao consultor, que devolve uma rota entre resolver, modelador e planejador, e o loop a despacha; o motivo é evidência, não rota; nenhum dos 50 itens de `F-4` manda a parada direto ao planejador, e as duas fontes normativas da skill do loop citam as decisões deste plano; o que `DCS-18` deixa fora continua indo ao planejamento. Exceção: com a linha `estrategico=`, o loop para em qualquer rota e leva a classificação ao dono. Em `resolve` e `modelador`, para sem executar a ação e sem despachar o modelador. Em `planejador`, executa a ação, que já é a parada
```

Em linguagem simples, a versão 2 acrescenta três coisas ao que a versão 1 dizia. Primeiro, o
comportamento do loop quando o consultor classifica um impedimento como estratégico (seção da
`CON-T3c`, abaixo). Segundo, as regras do diário sobre revisão pedida entram na fronteira que a
`OP-5` reescreve. Terceiro, a lista de residências da superfície passa de 47 a 50 itens. A saída do
comando mostra os dois primeiros; a partição da lista mora no contrato do objeto `consultor`, na
tabela de objetos da `## 1A`, e o comando a omite.

O instrumento confere a versão vigente contra os cards:

```
$ python .claude/tools/modelo.py check --plano docs/plans/P-0747-consultor-de-plano.md
modelo: OK — 8 operações, 5 objetos, 12 propriedades, 17 tarefas, versão 1
```

**Estado da validação da versão 2:** a validação tem dois degraus, primeiro o consultor e depois o
dono (`GOVERNANCA.md` §3.2). O **consultor já validou**, no acionamento 9, diferença a diferença
contra a árvore entregue; o registro está no plano, na decisão `DCS-34` e no achado `AE-21`. A
**validação do dono está pendente** (pendência nº 1). O mesmo acionamento anotou que o parágrafo de
leitura da `## 1A` e a linha da versão 2 no registro de versões narram duas reescritas onde houve
quatro; a narrativa se reescreve na promoção.

---

## `CON-T1` — O consultor ganha linha na matriz de responsabilidades

**Contexto que a motivou:** a matriz de `GOVERNANCA.md` §3 — a tabela que diz, para cada papel, que
modelo o roda, pelo que responde e o que nunca faz — não tinha linha do consultor. A escada de
revisão de plano dizia que a suspeita de que um plano precisa mudar *"chega aqui e só aqui"*, a
quem planeja; as linhas de planejamento, orquestração e execução diziam que as paradas *"sobem ao
**planejamento**"*; e os itens 17 e 18 de §7 mandavam a parada `premissa` à rodada de
replanejamento.

**O que é o artefato:** texto de doutrina em `GOVERNANCA.md`: a linha `| **Consultoria** |` da
matriz de §3, o parágrafo **Escada de revisão de plano** logo abaixo dela, a linha do consultor na
tabela *Quem escreve* de §3.2, e os itens 17 (`G-REPLAN`) e 18 (`G-NOASK`) de §7.

**Como funciona na prática:** é regra lida por quem conduz, planeja e executa, e citada pelas
demais residências. A linha nova diz, por rota, o que o consultor faz: em `resolve` fecha sozinho o
técnico e o tático — reescreve card, reordena fila, repara instrumento, toma decisão nova com id,
autora o card corretivo da mesma operação —, sem validação do dono; em `modelador` devolve o dossiê
de emenda do modelo junto com o reparo, e o loop despacha quem escreve o modelo **sem parar a
janela**; em `planejador`, só quando uma emenda aceita cria ou remove operação ou quando a premissa
do plano caiu por inteiro. A coluna *Não faz* fecha o papel: o consultor nunca reabre o objetivo do
plano, nunca escreve a `## 1`, nunca implementa, julga entrega, commita ou fala com o dono. A
presença e a remoção se aferem por literal:

```
$ grep -c -F '| **Consultoria** |' GOVERNANCA.md
1
$ grep -c -F 'chega aqui e só aqui' GOVERNANCA.md
0
$ grep -c -F 'sobem ao **planejamento**' GOVERNANCA.md
0
```

**Protege contra:** a parada que chega a destinos diferentes conforme a residência que o leitor
abriu. A matriz é a norma de onde as outras residências derivam, e ela diz um destino só.

**O procedimento que ela instalou:** **toda parada passa por uma triagem única, e a rota se lê
numa linha, nunca se deduz de prosa.** Duas situações ficam fora da triagem e continuam indo ao
planejamento: o plano recusado no gate de delegação por estar incompleto, e o contexto que acaba
dentro de uma tarefa. Nenhuma das duas tem a linha `blocked` de um executor.

---

## `CON-T2` — A definição do consultor perde o estatuto provisório

**Contexto que a motivou:** o arquivo do agente tinha 67 linhas. A descrição curta dizia *"Figura
ad-hoc, provisória"*, o corpo declarava estar fora da doutrina, o acionamento cobria os motivos
`dependencia` e `premissa` e omitia `ferramenta`, e nenhum dos dois deveres que a doutrina já dava
ao consultor — validar a versão pendente do modelo no marco e emitir o dossiê de emenda — estava no
arquivo. O histórico dos acionamentos não tinha residência estruturada.

**O que é o artefato:** dois arquivos. `.claude/agents/pantonic-consultant.md`, reescrito no
estatuto (papel de doutrina, com ponteiro para a linha *Consultoria*) e na seção *O que você faz*:
a triagem das três razões de parada e a forma do retorno, os dois deveres sobre o modelo, a saída
por edição mínima e a linha de estatística. E `docs/ACIONAMENTOS_CONSULTOR.tsv`, arquivo novo, uma
linha por acionamento.

**Como funciona na prática:**

1. **O que dispara** — o loop despacha o consultor com uma parada ou um laudo com pendência.
2. **A entrada** — o card em causa e a evidência: a linha de retorno do executor, a pendência do
   laudo ou o erro do instrumento.
3. **O processamento** — o consultor decide a rota, edita o plano com edição mínima e apensa uma
   linha ao arquivo de estatística, com os campos `data`, `plano`, `acionamento`, `tarefa`,
   `gatilho`, `motivo`, `classe_impedimento`, `rota`, `inconclusivo`.
4. **A saída** — a primeira linha do retorno é `rota=<resolve|modelador|planejador>`.

Linha real do arquivo de estatística, o acionamento 2 deste plano:

```
2026-09-23	P-0747	2	-	2	conferencia das copias apos o ato do modelador sobre DCS-24	conferencia card x modelo	resolve	-
```

E o estatuto aferido por literal:

```
$ grep -c -F 'Figura ad-hoc' .claude/agents/pantonic-consultant.md
0
$ grep -c -F 'rota=<resolve|modelador|planejador>' .claude/agents/pantonic-consultant.md
1
$ grep -c -F 'ACIONAMENTOS_CONSULTOR.tsv' .claude/agents/pantonic-consultant.md
1
```

**Protege contra:** a figura provisória citada como se fosse norma; a parada por ferramenta negada
que não chega a ninguém; e a estatística de acionamento que só se reconstrói lendo prosa.

---

## `CON-T2a` — A definição do consultor descreve uma forma só

**Contexto que a motivou:** depois da forma efêmera instalada (`CON-T4`), a abertura do arquivo do
consultor dizia que ele é efêmero, e o parágrafo *Por que você existe*, logo abaixo, ainda
prescrevia o cenário *"num contexto só, vivo"* — a forma de prontidão. E a linha que marca um
impedimento estratégico vivia só no arquivo de cenário, sem residência na definição do agente.

**O que é o artefato:** duas regiões de `.claude/agents/pantonic-consultant.md`: a última frase de
*Por que você existe* (o cenário fica num arquivo só, persistido, e cada acionamento nasce lendo o
que já houve) e o item 2 de *O que você faz*, que ganha a segunda linha do retorno,
`estrategico=<uma frase>`.

**Como funciona na prática:** a segunda linha aparece só quando o consultor classifica o
impedimento como estratégico — ele muda escopo ou objetivo do plano, ou revoga decisão do dono. É a
única matéria de uma parada que sobe ao dono durante a execução. O efeito dela no loop está na
seção da `CON-T3c`.

```
$ grep -c -F 'num contexto só, vivo' .claude/agents/pantonic-consultant.md
0
$ grep -c -F 'estrategico=<uma frase>' .claude/agents/pantonic-consultant.md
1
```

**Protege contra:** uma instância que lê a própria definição e encontra duas formas de existir; e a
classificação estratégica em prosa, que o loop teria de interpretar.

---

## `CON-T3` — O loop leva toda parada ao consultor

**Contexto que a motivou:** na skill do loop, a regra `A3b` mandava a parada `premissa` a quem
planeja, as regras `A3a` e `A3c` ignoravam o consultor, e o guardrail da skill mandava a matéria ao
planejador. A fonte normativa declarada da skill era um plano escrito antes de a figura existir, e
a cláusula da skill que resolve divergência *"a favor da seção"* resolveria a favor do texto antigo.

**O que é o artefato:** `.claude/skills/scrum-master/SKILL.md`, em quatro regiões: os dois
cabeçalhos de fonte normativa, que passam a citar as decisões `DCS-3`..`DCS-6` deste plano; o
passo 8, que ganha o item **Triagem**; as regras `A3a`, `A3b`, `A3c`, `A6a`, `A7` e `B1` da tabela
de roteamento; e a lista *O que obriga parada e o que segue com registro*.

**Como funciona na prática:**

1. **O que dispara** — o executor devolve `blocked`, ou o laudo traz pendência substantiva.
2. **A entrada** — a regra do bloco A que casa com o retorno, pela ordem de precedência da tabela.
3. **O processamento** — o loop materializa a tarefa como `blocked`, sem despachar o revisor nem
   escrever registro de tarefa, e escala ao consultor, que devolve a rota.
4. **A saída** — `resolve` segue com o reparo gravado; `modelador` segue com o despacho de quem
   escreve o modelo; `planejador` para a janela.

A regra `A3b`, como está hoje:

> `status=blocked` com `motivo=premissa` | materializa `blocked` com a razão na tarefa; **não**
> despacha o `reviewer` e **não** escreve RDO; escala ao **consultor**, que devolve a rota (passo
> 8): `resolve` segue com o reparo; `modelador` segue com o despacho do modelador; `planejador` e
> `estrategico=` **PARAM**, como o passo 8 manda.

```
$ grep -c -F 'escala ao **consultor**' .claude/skills/scrum-master/SKILL.md
3
$ grep -c -F 'P-0747' .claude/skills/scrum-master/SKILL.md
6
```

As três ocorrências da primeira linha são as regras `A3a`, `A3b` e `A3c`, uma por motivo de parada.

**Protege contra:** a parada `premissa` que chega a quem planeja sem triagem, e o loop que decide a
rota lendo prosa.

---

## `CON-T3a` — Toda regra que escala nomeia a mesma parada

**Contexto que a motivou:** depois da `CON-T3`, a regra `A6a` dizia que a janela segue com o que o
consultor devolver, sem a exceção da rota `planejador` que o passo 8 e a lista de parada exigem. A
classificação estratégica aparecia só na `B1` e na lista de parada, e o retorno `rota=resolve` com
impedimento estratégico caía ao mesmo tempo nas listas *Obriga parada* e *Segue com registro*. As
onze verificações do card passaram com a divergência, porque cada uma media um bloco isolado.

**O que é o artefato:** a mesma skill, nas regiões da `CON-T3`: o passo 8, as regras `A3a`, `A3b`,
`A3c`, `A6a`, `A7`, `B1` e as duas listas de parada, agora com a linha `estrategico=` como forma
mecânica.

**Como funciona na prática:** a lista de parada, hoje, separa os dois casos sem sobreposição:

> **Obriga parada:** a rota `planejador` que o consultor devolver a qualquer escalonamento (`A3a`,
> `A3b`, `A3c`, `A6a`, `A7`, `B1` e o gate do modelo do passo 9), e a linha `estrategico=` que ele
> devolver com qualquer rota […]
>
> **Segue com registro:** […] toda parada ou pendência em que o consultor devolve `rota=resolve`
> sem `estrategico=` […]

```
$ grep -c -F 'estrategico=' .claude/skills/scrum-master/SKILL.md
10
```

A mesma contagem, na skill anterior ao plano, dá `0`.

**Protege contra:** o mesmo retorno classificado em duas listas opostas.

**O procedimento que ela instalou:** **a linha de coerência do módulo.** O card corretivo carregou
uma verificação que cruza os blocos — toda regra que devolve rota nomeia a parada, e nenhuma
menção a `rota=resolve` aparece sem a ressalva. Ela vive no card; a skill não tem teste que a
repita (defeito nº 1 da seção de padrão).

---

## `CON-T3b` — Com impedimento estratégico, a parada vem antes da ação

**Contexto que a motivou:** a regra dizia que, com `estrategico=`, o loop para, e deixava aberto se
a ação da rota executa antes da parada. Com `rota=modelador`, o dossiê de emenda ficava sem destino
nomeado: ou quem escreve o modelo o recebia antes de o dono decidir, ou ninguém o recebia.

**O que é o artefato:** o item **Triagem** do passo 8 e a lista *Obriga parada* da skill do loop.

**Como funciona na prática:** com a linha presente, *"o reparo que o consultor já gravou fica no
plano, o modelador **não** é despachado, e a frase, a rota e o dossiê de emenda, se houver, vão ao
relatório de encerramento, para o dono decidir antes de qualquer ato sobre o modelo"* (texto do
passo 8).

```
$ grep -c -F 'sem executar a ação da rota' .claude/skills/scrum-master/SKILL.md
2
```

**Protege contra:** ato sobre o modelo do plano executado antes de o dono decidir matéria que muda
o escopo ou o objetivo do plano.

---

## `CON-T3c` — Na rota planejador, a ação já é a parada

**Contexto que a motivou:** o texto da `CON-T3b` suprimia a ação da rota em qualquer rota,
inclusive `planejador`. Com impedimento estratégico e rota `planejador`, a skill deixava de marcar
o plano como `blocked` e de enfileirar a rodada de replanejamento — o plano parava sem que nenhum
instrumento registrasse o bloqueio.

**O que é o artefato:** as mesmas duas regiões da skill do loop.

**Como funciona na prática:** o passo 8 diz: *"com `rota=planejador` a ação da rota já é a parada e
se executa como está — o plano materializado `blocked`, a rodada de replanejamento enfileirada — e
a frase vai junto ao relatório"*. O comportamento completo, por rota:

| rota devolvida | sem `estrategico=` | com `estrategico=` |
|---|---|---|
| `resolve` | o reparo está gravado; a janela segue | a janela para; o reparo fica; nada mais executa |
| `modelador` | quem escreve o modelo é despachado; a janela segue | a janela para; ninguém é despachado; o dossiê vai ao relatório |
| `planejador` | o plano vai a `blocked`, a rodada entra na fila; a janela para | o mesmo, com a frase no relatório |

```
$ grep -c -F 'a ação da rota já é a parada' .claude/skills/scrum-master/SKILL.md
1
```

**Protege contra:** o plano parado sem estado que o registre, que a retomada seguinte leria como
plano em andamento.

---

## `CON-T4` — Uma instância nova por acionamento, com o estado num arquivo

**Contexto que a motivou:** a skill do loop não tinha passo de criar, passar handover ou
substituir o consultor; a única menção era *"instanciado uma vez"*. A instância de prontidão
crescia a cada acionamento, e o custo por acionamento carregava de 25% a 48% de reescrita de cache
(números de **O problema**).

**O que é o artefato:** três peças. A seção `## Acionamento do consultor` da skill do loop — uma
seção logo antes de `## Relatório de encerramento`, fora da sequência de passos, porque os dez
passos da skill são citados por número em outras residências. O arquivo
`docs/plans/_CENARIO-P-0747.md`, o cenário deste plano. E as linhas do agente e da regra `B1` que
descrevem a forma.

**Como funciona na prática:**

1. **O que dispara** — qualquer escalonamento das regras `A3a`, `A3b`, `A3c`, `A6a`, `A7` e `B1`,
   e o gate do modelo do passo 9.
2. **A entrada** — três itens: o caminho do cenário do plano, o identificador do card em causa e
   a evidência.
3. **O processamento** — uma instância **nova** do consultor lê o cenário e o card, decide,
   reescreve o cenário com edição mínima e apensa a linha de estatística. Sem cenário na árvore, o
   primeiro acionamento o cria.
4. **A saída** — a linha `rota=`, e a instância se encerra. Nenhuma instância é retomada por
   mensagem e nenhuma é substituída por limite: o cenário **é** o handover.

O cenário deste plano, medido no fechamento:

```
$ wc -l -c docs/plans/_CENARIO-P-0747.md
  30 5902 docs/plans/_CENARIO-P-0747.md
$ grep -n '^## ' docs/plans/_CENARIO-P-0747.md
5:## Decisões vivas
16:## Fila
20:## Achados abertos
24:## Matéria inconclusiva
```

São 5.902 bytes, bem abaixo do teto de 15k tokens. Cada acionamento efêmero deixou a própria linha
na telemetria (`docs/telemetria.tsv`), com o campo `tokens_k` que a notificação reportou:
`CON-T4-consultor-1` 139,7k, `CON-T4a-consultor-1` 104,1k, `CON-T6-consultor-1` 135,8k,
`CON-T7-consultor-1` 99,0k, `CON-T8-consultor-1` 90,9k e `P-0747-consultor-marco` 63,4k.

**Protege contra:** a instância que cresce até o limite do contexto; a reescrita de cache paga a
cada acionamento que chega depois de cinco minutos; e o handover improvisado quando a instância
enche.

---

## `CON-T4a` — A instância do consultor que cai é descartada

**Contexto que a motivou:** a regra `A1` do loop tratava toda queda de subagente do mesmo jeito —
retomar por mensagem a mesma instância —, e a seção nova dizia que nenhuma instância do consultor
se retoma. Eram duas regras para a mesma queda.

**O que é o artefato:** a linha `A1` da tabela de roteamento da skill do loop.

**Como funciona na prática:** a regra separa os dois casos. Texto atual:

> executor ou `reviewer`: uma retomada por `SendMessage` ao mesmo `agentId` com "o que falta"; […]
> Consultor: **nenhuma** retomada — a instância caída se descarta, a telemetria dela registra
> `PARCIAL — trecho pré-queda não medido`, e o loop despacha **uma instância nova** com as mesmas
> três entradas, sobre o cenário como a caída o deixou […]. Caiu de novo no mesmo acionamento:
> **PARA**

```
$ grep -c -F 'Consultor: **nenhuma** retomada' .claude/skills/scrum-master/SKILL.md
1
```

**Protege contra:** o loop escolhendo entre duas regras para o mesmo evento. Resta um limite: a
instância que cai no meio de uma edição deixa cenário ou plano meio escritos, e a nova os lê como
estão, sem verificação de integridade.

---

## `CON-T5` — Os demais papéis devolvem a parada à triagem

**Contexto que a motivou:** a definição de quem planeja dizia que a rodada de replanejamento chega
*"só a você"*; a de quem escreve o modelo recebia a emenda *"no dossiê de quem a tomou"*, sem nomear
o consultor; executor e revisor mandavam a parada e a pendência à rodada de replanejamento; e o
diário, a passagem de bastão e a regra global de não decidir diziam o mesmo.

**O que é o artefato:** sete residências de conduta. `.claude/agents/pantonic-planner.md` (seção
*Rodada de replanejamento*), `.claude/agents/pantonic-model-designer.md` (ato de emenda e lista de
tarefas de cada operação), `.claude/agents/pantonic-executor.md`,
`.claude/agents/pantonic-reviewer.md`, as skills `diario-de-obras` (máquina de transições) e
`passagem-de-bastao`, e a Regra 8 de `.claude/global/CLAUDE.md`.

**Como funciona na prática:** cada papel, ao ler a própria definição, encontra o mesmo destino. A
definição de quem escreve o modelo, hoje: *"recebe uma decisão que muda o que o plano entrega, no
dossiê de quem a tomou — o `pantonic-consultant`, quando a decisão nasce da triagem de uma parada,
ou o `pantonic-planner`, na rodada de replanejamento"*. A do executor fecha a sequência de parada
com *"Quem recebe é a triagem do consultor."* As linhas que citam o consultor, antes do plano e
hoje:

| arquivo | antes | hoje |
|---|---|---|
| `pantonic-planner.md` | 0 | 2 |
| `pantonic-model-designer.md` | 0 | 3 |
| `pantonic-executor.md` | 0 | 4 |
| `pantonic-reviewer.md` | 0 | 2 |
| skill `diario-de-obras` | 0 | 3 |
| skill `passagem-de-bastao` | 1 | 4 |

Medido com `grep -c -i 'consultor\|pantonic-consultant'`, sobre o último commit e sobre a árvore.

**Protege contra:** o agente que manda a parada a um destino diferente daquele que o loop aplica.

---

## `CON-T5a` — O diário e a regra global dizem o que a triagem diz

**Contexto que a motivou:** um parágrafo da skill `diario-de-obras` levava o **plano** a `blocked`
e abria rodada de replanejamento em toda revisão pedida por quem executa — o loop só faz isso na
rota `planejador`. Esse parágrafo estava fora da lista de residências do plano. E a Regra 8 da
regra global usava "rota" em dois sentidos na mesma frase: a rota da triagem e a rota aprovada do
plano, com donos diferentes.

**O que é o artefato:** o parágrafo de `.claude/skills/diario-de-obras/SKILL.md` antes da *Máquina
de transições*, e a linha da Regra 8 em `.claude/global/CLAUDE.md`.

**Como funciona na prática:** o diário, hoje:

> Plano cuja revisão foi pedida por quem executa ou orquestra não vai a `blocked` por isso: a
> **tarefa** vai a `blocked` com a razão tipada `premissa`, e a parada vai à triagem do consultor,
> que devolve a rota […]. Só a rota `planejador` é caso de `blocked` **de plano** […]. Nas rotas
> `resolve` e `modelador` o plano segue.

A Regra 8 diz que o executor *"devolve `blocked` à triagem do plano, que decide o destino da
parada"*; a palavra "rota" fica só com o sentido de rota aprovada do plano.

**Protege contra:** plano marcado `blocked` em rota onde o loop segue, e a homonímia que faz uma
regra de conduta dizer duas coisas com a mesma palavra.

---

## `CON-T6` — A especificação vira lastro medido

**Contexto que a motivou:** `docs/consultant-spec.md` era a única descrição da figura, o índice de
documentos a descrevia assim, e a §10 listava sete lacunas sem destino.

**O que é o artefato:** o estatuto na abertura da especificação, os ponteiros apensados a cada
item da §10, e três entradas em `docs/DOC_MAP.md`: a da especificação, a do arquivo de estatística
e a do cenário.

**Como funciona na prática:** o estatuto, hoje:

> **Estatuto.** Lastro medido, não fonte normativa. […] o papel mora na linha *Consultoria* da
> matriz de `GOVERNANCA.md` §3 e a conduta em `.claude/agents/pantonic-consultant.md`.

Cada lacuna da §10 termina com o ponteiro do que a fecha:

```
$ sed -n '/^## 10\./,/^## 11\./p' docs/consultant-spec.md | grep -c -F '→ fechado'
5
$ sed -n '/^## 10\./,/^## 11\./p' docs/consultant-spec.md | grep -c -F '→ residência nomeada'
2
```

As cinco fechadas por norma: o handover (o cenário), a estatística (o arquivo de acionamentos), a
autoria de card novo (o corretivo da mesma operação é do consultor), a forma da figura (efêmera) e
a disciplina de saída (regra do agente). As duas com residência nomeada: o critério de
não-acionamento, no tíquete `TK-55`, e o caminho de poluição, na regra geral do agente. A mesma
contagem de setas, na especificação anterior ao plano, dá `0`.

**Protege contra:** medida lida como norma, e duas fontes normativas para a mesma figura.

---

## `CON-T6a` — A especificação para de afirmar que prevalece

**Contexto que a motivou:** o parágrafo *Consequência sobre a §2* da especificação dizia *"Enquanto
o bloco A não for reescrito, a spec prevalece"*. O bloco A da skill do loop foi reescrito pelas
`CON-T3`..`CON-T3c`, e a frase ficou falsa no presente. O parágrafo estava fora da lista de
residências do plano.

**O que é o artefato:** o parágrafo, em `docs/consultant-spec.md` §3, reescrito como registro
datado.

**Como funciona na prática:** o texto de hoje fecha com: *"Registro histórico: o bloco A foi
reescrito pela `CON-T3` do `P-0747` (2026-09-23; corretivos `CON-T3a`..`CON-T3c`), a regra mora
hoje na skill `scrum-master` e em `G-REPLAN` (`GOVERNANCA.md` §7 item 17), e a spec não
prevalece"*.

**Protege contra:** dois textos que reclamam precedência sobre a mesma regra.

---

## `CON-T7` — A medida do piloto da forma efêmera

**Contexto que a motivou:** a especificação estimava a forma efêmera em $1,2 a $1,5 por
acionamento, contra o piso medido de $3,7 da prontidão. A regra de veredito foi fixada antes da
medida: **adota** se a média ficar abaixo de $3,7 com zero reprovações; **recusa** caso contrário;
com menos de três acionamentos, **amostra insuficiente**.

**O que é o artefato:** a subseção *Veredito do piloto da forma efêmera* na §11 de
`docs/consultant-spec.md`. A sonda que apurou o custo é descartável e mora fora do repositório,
em `%TEMP%\claude\sonda_p0747.py`.

**Como funciona na prática:** a janela medida vai do aceite da `CON-T4` ao despacho da `CON-T7`. A
sonda lê os transcripts das instâncias do consultor cuja mensagem de entrada cita o cenário deste
plano, remove duplicatas por identificador de mensagem e precifica pela tabela Opus ($5/M de
entrada, $25/M de saída, leitura de cache a 10%, escrita de cache a 125%). Reprovação conta toda
revisão repetida das tarefas `CON-T5`, `CON-T6` e dos seus corretivos, sem atribuir causa. A tabela
gravada:

| acionamentos | $/acionamento, média | $/acionamento, mín–máx | reprovações | retentativas | veredito |
|---|---|---|---|---|---|
| 3 | $2,8 | $2,4–$3,0 | 0 | 0 | adotada |

**Protege contra:** a forma da figura escolhida por argumento. O veredito saiu da regra fixada
antes da medida, aplicada ao número.

---

## `CON-T7a` — O veredito declara em que modelo as instâncias rodaram

**Contexto que a motivou:** as três instâncias medidas rodaram o modelo `claude-fable-5-1`; a sonda
as precificou pela tabela Opus; e o piso de $3,7 foi medido em instâncias Opus. A subseção omitia o
modelo, e o $2,8 se lia como custo real da forma.

**O que é o artefato:** um parágrafo apensado à subseção do veredito; a linha da tabela fica igual.

**Como funciona na prática:** o texto de hoje:

> Modelo das instâncias medidas: as três rodaram `claude-fable-5-1` […]; as instâncias 1-4 da
> tabela desta seção, que dão o piso de $3,7, rodaram Opus. A coluna de custo é contagem de tokens
> precificada pela tabela Opus nos dois lados — preço-Opus-equivalente, não custo real — e compara
> a forma da figura (contexto reescrito e relido por acionamento), não o modelo; quanto um modelo
> distinto consome de tokens para a mesma decisão não foi medido. A sonda […] se reexecuta sobre a
> primeira execução de plano com o consultor em Opus, para conferir o veredito […].

O veredito `adotada` fica como medida da **forma**: o que a forma efêmera ataca — contexto
reescrito e relido a cada acionamento — é contagem de tokens, e os dois lados foram precificados
pela mesma tabela.

**Protege contra:** número de custo publicado como fato quando mede outra coisa.

---

## `CON-T8` — A porta de entrada descreve a figura nova

**Contexto que a motivou:** a tabela de agentes do `README.md` anunciava o consultor *"instanciado
uma vez, mantido de standby"*; a linha do guardrail 17 mandava a rodada de replanejamento ao
planejador; a descrição curta do agente o anunciava provisório; e a região gerada `kit:agents` de
`.claude/README.md`, montada a partir dessa descrição, repetia tudo.

**O que é o artefato:** a linha do consultor na tabela de agentes do `README.md`, a linha 17 da
tabela de guardrails, a `description` do frontmatter do agente e a região gerada, regenerada no
mesmo ato por `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate`.

**Como funciona na prática:** a linha da tabela de agentes, hoje:

> | `pantonic-consultant` | Opus | Ponto de triagem de **toda** parada de executor e de todo laudo
> com pendência substantiva: devolve a rota `resolve`, `modelador` ou `planejador`, fecha sozinho o
> técnico e o tático e leva ao dono só o drift do modelo. Efêmero: cada acionamento é uma instância
> nova que lê o cenário persistido do plano. Não implementa entrega, não julga e não commita. |

```
$ grep -c -i 'instanciado uma vez\|mantido de standby' README.md
0
$ pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift
kit_check: check-drift OK - .claude/README.md == regenerado (10 agente(s), 11 skill(s)); materializacao do alvo 'projeto' == canonico.
```

O card declara aceite do dono além do laudo; esse aceite está pendente (pendência nº 2).

**Protege contra:** a porta de entrada anunciando a forma aposentada a quem chega ao repositório.

---

## `CON-T8a` — A descrição do consultor volta a ser YAML que o harness lê

**Contexto que a motivou:** a `CON-T8` entregou a descrição com `Efêmero: cada acionamento` onde o
card mandava `Efêmero - cada acionamento`. Dois-pontos seguidos de espaço, num valor sem aspas,
quebram o YAML do frontmatter: o consultor ficou o único dos dez agentes cujo cabeçalho um parser
estrito recusa, e a região gerada reproduziu o defeito. A verificação do card casava só o prefixo
da descrição, e `kit_check.ps1 -Mode validate` saiu `0`.

**O que é o artefato:** a linha 3 de `.claude/agents/pantonic-consultant.md`, devolvida ao texto
do card, e a região `kit:agents` de `.claude/README.md`, regenerada no mesmo ato.

**Como funciona na prática:** a classe do defeito, reproduzida:

```
$ python -c "import yaml
try: yaml.safe_load('description: Efemero: cada acionamento')
except Exception as e: print(type(e).__name__, '-', str(e).splitlines()[0])"
ScannerError - mapping values are not allowed here
```

E o estado de hoje, com os dez frontmatters de `.claude/agents/` passados por `yaml.safe_load`:

```
pantonic-auditor-arch.md ok
pantonic-auditor-cleancode.md ok
pantonic-benchmarker.md ok
pantonic-consultant.md ok
pantonic-executor.md ok
pantonic-fora-da-caixa.md ok
pantonic-model-designer.md ok
pantonic-planner.md ok
pantonic-reviewer.md ok
pantonic-scout.md ok
```

**Protege contra:** o agente que o harness deixa de carregar sem aviso. A proteção cobre **este**
caso: o verificador do kit continua aceitando frontmatter inválido (pendência nº 7).

---

## O que vale além deste plano

| regra | o que resolve | residência |
|---|---|---|
| Toda parada de executor e todo laudo com pendência substantiva passam pela triagem do consultor, que devolve a rota numa linha | a parada tem um destino só, e o loop lê a rota sem interpretar prosa | `GOVERNANCA.md` §3, linha *Consultoria*; §7 item 17 (`G-REPLAN`); skill `scrum-master`, passo 8 |
| O consultor fecha o técnico e o tático sem validação do dono, inclusive o card corretivo da mesma operação | a correção de um card sai da fila de planejamento | `GOVERNANCA.md` §3, linha *Consultoria*, e §3.2, *Lastro* |
| Drift do modelo na parada mantém a janela aberta: a versão pendente coexiste com a vigente até o marco | a execução segue enquanto a mudança do modelo espera validação | `GOVERNANCA.md` §3, *Escada de revisão de plano*, e §3.2 |
| Com `estrategico=`, a janela para em qualquer rota; `resolve` e `modelador` ficam sem ação, `planejador` executa a sua | a matéria que muda escopo ou objetivo chega ao dono antes de qualquer ato | skill `scrum-master`, passo 8 e *O que obriga parada* |
| Uma instância efêmera por acionamento, com o cenário como handover; a instância que cai se descarta | o custo por acionamento para de crescer com o plano | skill `scrum-master`, `## Acionamento do consultor` e regra `A1` |
| Plano incompleto no gate de delegação e contexto que acaba dentro da tarefa ficam fora da triagem | os dois casos sem linha `blocked` continuam com o planejamento | `GOVERNANCA.md` §7, `G-PLANREADY`, e §4.3; skill `passagem-de-bastao`, gate de delegação |
| Uma linha de estatística por acionamento | o panorama dos pontos inconclusivos se acumula em forma que se conta | `.claude/agents/pantonic-consultant.md`, *O que você faz* item 5; `docs/ACIONAMENTOS_CONSULTOR.tsv` |
| Teste de saturação e distinção capacidade × término antes de abrir card | superfície que já recebeu cards seguidos acumula achado sem abrir card novo | `docs/consultant-spec.md` §2 — lastro medido, aplicado pelo consultor; sem residência normativa |

---

## Os ganhos, medidos

Tudo re-derivado em 2026-09-23. O **antes** é o último commit (`d75e7a6`), anterior à execução, ou
a linha **antes** das verificações dos cards, medida na abertura.

| medida | antes | depois |
|---|---|---|
| linha do consultor na matriz de responsabilidades | 0 | 1 |
| *"Figura ad-hoc"* na definição do consultor | 1 | 0 |
| linhas da definição do consultor | 67 | 54 |
| linhas que citam o consultor nas onze residências da superfície | 14 | 57 |
| linhas que mandam matéria ao planejamento nas mesmas onze residências | 18 | 10 — oito são os dois casos que ficam fora da triagem por regra, uma já passa pela triagem, uma é falso positivo do padrão de busca |
| menções a `estrategico=` na skill do loop | 0 | 10 |
| lacunas da especificação sem destino | 7 | 0 — 5 fechadas por norma, 2 com residência nomeada |
| registro estruturado dos acionamentos | nenhum; prosa | `docs/ACIONAMENTOS_CONSULTOR.tsv`, 9 linhas (acionamentos 1 a 9) |
| custo por acionamento | $3,7 a $4,5, prontidão, instâncias Opus | média $2,8 (mín $2,4, máx $3,0), 3 acionamentos efêmeros, preço-Opus-equivalente de instâncias `claude-fable-5-1` |
| `tokens_k` por linha de telemetria do consultor neste plano | 235,9 · 239,2 · 270,5 (acionamentos 1 a 3, prontidão, a mesma instância retomada) | de 63,4 a 139,7 (acionamentos 4 a 9, efêmeros, seis linhas) |
| frontmatters de agente que um parser YAML estrito aceita | 9 de 10 (depois da `CON-T8`) | 10 de 10 |
| suíte de testes | `277 passed` (ensaio da abertura) | `277 passed` — o plano edita doutrina, sem teste novo |
| instrumentos de fechamento | — | `backlog.py check` OK · `modelo.py check` OK · `kit_check` validate e check-drift OK · `check-readme` OK |
| vereditos de revisão | — | 17 cards julgados: 16 `aprovado` 100%, 1 `ressalva` 93% (`CON-T8`); zero reprovações, zero retentativas |
| paradas de executor e perguntas ao dono durante a execução | — | zero e zero: dos nove acionamentos do consultor, seis vieram de laudo com pendência, um de conferência depois de ato sobre o modelo e dois de ato do dono ou de marco |

A linha do custo compara a **forma** em tokens; a declaração do modelo das instâncias está na
seção da `CON-T7a`. Os `tokens_k` são o campo que cada notificação reportou, sem normalização.

**Custo da execução, medido.** `docs/telemetria.tsv` registra, para as tarefas `CON-T*` e
`P-0747-*` de 2026-09-23, **48 linhas**, somando **895 tool uses** e **4.790,0k tokens**, sem
linha duplicada (`sort | uniq -d` devolve vazio):

| papel | modelo | linhas | tool uses | tokens |
|---|---|---|---|---|
| executor | Sonnet | 17 | 321 | 1.122,4k |
| revisor | Opus | 17 | 326 | 1.406,2k |
| consultor | `claude-fable-5-1` | 9 | 227 | 1.378,5k |
| quem escreve o modelo | Opus | 5 | 21 | 882,9k |

A nona linha do consultor (`P-0747-consultor-marco`, 63,4k) é o acionamento 9, que validou a
versão 2 do modelo. O tíquete `TK-76a`, que rodou antes na mesma janela, soma 2 linhas
e 109,1k tokens fora desta conta.

---

## O padrão que a execução revelou

Os nove corretivos repararam defeitos que moravam **entre residências**. Todas as dezessete
entregas seguiram o card ao pé da letra, e os laudos fecharam em 100%, com uma exceção em 93%. Os
defeitos se agrupam em duas classes.

**A classe maior: a mesma regra dita de dois jeitos em duas residências.** Cinco corretivos
repararam isso. A skill do loop dizia numa regra que a janela segue e na regra vizinha que ela
para (`CON-T3a`); a definição do consultor dizia "efêmero" numa linha e descrevia a prontidão em
outra (`CON-T2a`); a regra da parada estratégica ficava muda sobre a ordem entre parar e agir
(`CON-T3b`); a regra de queda do loop contradizia a seção nova (`CON-T4a`); e o reparo de uma
dessas contradições criou a seguinte, ao suprimir a ação da rota `planejador` (`CON-T3c`). Cada
card media os próprios blocos, um a um, e todas as verificações passavam com a divergência na
árvore. Foi o revisor, lendo o módulo inteiro, quem a achou — cinco vezes.

**A segunda classe: residências fora da lista de superfície.** O plano abriu com
uma lista de 47 residências a reescrever, levantada por busca de padrões na abertura. A execução
achou mais três, em três laudos seguidos: a cláusula do consultor na regra de queda do loop, o
parágrafo do diário sobre revisão pedida e o parágrafo da especificação que afirmava prevalecer.
Duas delas viraram corretivos (`CON-T5a`, `CON-T6a`); a terceira entrou na lista por ato sobre o
modelo, sem card. **O levantamento da superfície foi o elo fraco do planejamento**: ele enumerou o
que os padrões casavam, e as três residências falavam do mesmo assunto com outras palavras.

Os dois corretivos restantes são casos isolados: a declaração do modelo das instâncias no veredito
(`CON-T7a`) e o frontmatter quebrado por dois-pontos (`CON-T8a`).

Um mecanismo segurou o volume: a skill do loop recebeu seis cards neste plano, cinco deles nascidos
de achado de revisão sobre o anterior, e o consultor a declarou **saturada** — achado novo sobre
ela acumula como pendência, sem abrir card. Quatro frases ficaram assim, sem card (pendências nº 3
a 5).

### Os defeitos da execução, com estado

| # | o que se descobriu | casos | estado | o que fecha |
|---|---|---|---|---|
| 1 | A mesma regra dita de dois jeitos em duas residências do mesmo módulo, com cada verificação do card medindo um bloco isolado | `CON-T3a`, `CON-T2a`, `CON-T3b`, `CON-T4a`, `CON-T3c` | 🟡 **Caso fechado, classe sem guarda** — os cinco reparados; nenhum teste cruza as residências entre si, e frases do mesmo tipo seguem abertas | pendência nº 6 (régua) e nº 3 a 5 (frases) |
| 2 | A lista de superfície do planejamento omitiu residências que falam do assunto com outras palavras | três residências; `CON-T5a`, `CON-T6a` e um item de lista sem card | 🔴 **Regra escrita, aplicação pendente** — os três casos corrigidos; a regra de levantar a superfície por padrão literal com contagem declarada está redigida e roteada à régua de autoria de card, sem aplicação | pendência nº 6 |
| 3 | O consultor declarou "nenhum drift de estado final" sem confrontar a decisão com a versão pendente do modelo; o conflito só apareceu na revisão seguinte | um acionamento | 🟡 **Caso fechado, classe sem guarda** — o acionamento seguinte aplicou o confronto antes de declarar; nada obriga o próximo a aplicá-lo | registrado na estatística do consultor, acumulada no `TK-55` |
| 4 | Verificação de card que casa o prefixo de um texto e deixa de lado o parse do arquivo onde ele mora | `CON-T8` | 🟡 **Caso fechado, classe sem guarda** — o corretivo mediu o parse YAML; o verificador do kit continua aceitando frontmatter inválido | pendência nº 7 |
| 5 | Veredito de custo publicado sem declarar o modelo das instâncias medidas | `CON-T7` | 🟡 **Caso fechado, classe sem guarda** — declarado na especificação; nenhuma regra exige a declaração em medida futura | pendência nº 9 |
| 6 | O critério de pronto de cada card enuncia a propriedade do modelo inteira, e só a fatia do card se verifica nele | todos os cards | 🔴 **Regra escrita, aplicação pendente** — o recorte à fatia da operação está roteado à régua de autoria de card | pendência nº 6 |
| 7 | O gerador de evidência do revisor atribui por arquivo, sobre árvore sem commit que mistura dois planos | todas as revisões | 🔴 **Regra escrita, aplicação pendente** — remédio conhecido, sem aplicação | pendência nº 8 |

---

## Pendências abertas ao fim do plano

| # | pendência | por que ficou aberta | o que a fecha | bloqueia algo? |
|---|---|---|---|---|
| **1** | Validação do dono sobre a versão 2 do modelo | a validação tem dois degraus; o consultor validou no acionamento 9, e o segundo degrau é do dono | ato do dono no marco: promover (quem escreve o modelo reescreve o bloco, inclusive a narrativa das quatro reescritas) ou recusar (as tarefas retroagem ao ponto do drift, conduta que mora no `TK-70`) | **sim** — o modelo do plano fecha só com ele |
| **2** | Aceite do dono sobre a porta de entrada | o card `CON-T8` declara aceite do dono além do laudo | leitura da linha do consultor e da linha 17 da tabela de guardrails do `README.md` | **sim** — o aceite da `OP-8` |
| **3** | O parágrafo do diário fecha com *"Nas rotas `resolve` e `modelador` o plano segue"*, sem a ressalva de `estrategico=` (a **janela** para nesse caso; o estado do **plano** confere) | superfície saturada; precondição rara | uma frase em `.claude/skills/diario-de-obras/SKILL.md` | não |
| **4** | A especificação afirma no presente que as regras `A3a`..`A3c` *"nunca foram revistas"*, e o ponteiro *"(estatuto, :3-5)"* envelheceu | a especificação é lastro medido; segunda frase na mesma subseção | uma passagem de redação em `docs/consultant-spec.md` §3 | não |
| **5** | Duas frases do módulo do loop: a nota de telemetria do passo 9 fala da *"retomada do executor pela `A1`"* (a `A1` retoma executor ou revisor); e o item 2 da definição do consultor diz que o loop para *"em qualquer rota sem executar a ação da rota"*, sem a exceção da rota `planejador` que a skill fixa | superfície saturada | duas substituições literais | não — o loop executa pela skill, que está certa |
| **6** | Três emendas à régua de autoria de card: levantar a superfície por padrão literal com contagem declarada; recortar o critério de pronto à fatia da operação; exigir linha de coerência do módulo | a régua é artefato de kit, fora do objeto deste plano | o tíquete `TK-72`, que já recebeu o texto das emendas | não bloqueia este plano; **efeito fora dele** — a classe segue possível em todo plano futuro |
| **7** | `kit_check.ps1 -Mode validate` aceita frontmatter de agente que um parser YAML estrito recusa | capacidade de instrumento, fora do escopo | o tíquete `TK-77`, `ready` | não; **efeito fora do plano** — qualquer edição futura de agente |
| **8** | O gerador de evidência do revisor atribui por arquivo, e a árvore carrega trabalho sem commit de mais de um plano: 35 arquivos modificados, 3.398 linhas inseridas | os commits são do dono no marco, e o instrumento está fora do escopo | o tíquete `TK-66` (atribuição por trecho) ou cadência de commit que isole cada entrega | não bloqueou entrega; **efeito fora do plano** — encarece toda revisão |
| **9** | Quanto o consultor consome de tokens em Opus para a mesma decisão | as três instâncias medidas rodaram `claude-fable-5-1` | reexecutar a sonda na primeira execução de plano com o consultor em Opus. A sonda mora em `%TEMP%\claude\sonda_p0747.py`, fora do repositório, e pode sumir antes dessa execução | não; **efeito fora do plano** — confere o veredito `adotada` |
| **10** | A cópia da regra global que o dono carrega em `~/.claude/CLAUDE.md` mantém a Regra 8 antiga: o executor *"escala para replanejamento"* (linha 192, medido hoje) | a propagação à cópia do dono e aos projetos derivados ficou fora do escopo | a skill `checar-versao-kit`, que propaga o kit | não bloqueia o plano; **efeito fora do projeto** — toda sessão de trabalho carrega a regra antiga |
| **11** | O cabeçalho do plano lista 14 dos 17 cards na ordem de execução; a `## 6` lista os 17 | o cabeçalho ficou como estava a cada corretivo | uma substituição da linha do cabeçalho | não — `backlog.py check` e `modelo.py check` saem limpos |

---

## O estado, sem enfeite

O plano entregou **dezessete cards, todos `done`**, contra as oito operações do seu modelo: oito de
autoria e nove corretivos nascidos de laudo e somados às operações que reparam. Nenhum card foi
cancelado, nenhuma entrega foi reprovada, nenhuma tarefa foi refeita, nenhum executor parou e
nenhuma pergunta subiu ao dono durante a execução. Dezesseis laudos fecharam em 100% e um com
ressalva, 93%. Os instrumentos de fechamento saem limpos: `backlog.py check` e `modelo.py check`
exit `0`, `kit_check` e `check-readme` OK, `277 passed` na suíte.

O que o repositório ganhou de durável: o consultor é papel de doutrina, com linha na matriz; toda
parada tem um destino, escrito do mesmo jeito nas residências de norma, do loop e de cada papel; a
rota chega ao loop numa linha que ele lê sem interpretar; a figura roda numa instância nova por
acionamento, com o estado num arquivo de 5,9 kB, a um custo médio de $2,8 contra o piso de $3,7 da
prontidão, em preço equivalente; e cada acionamento deixa uma linha que se conta.

Ficaram **onze pendências**. Duas **bloqueiam o veredito**: a validação da versão 2 do modelo e o
aceite da porta de entrada, ambas atos do dono. Cinco **têm efeito fora deste plano**: as emendas
à régua de autoria de card, o verificador que aceita frontmatter inválido, a atribuição de
evidência sobre árvore sem commit, a medida em Opus — cuja sonda mora num diretório temporário — e,
**fora do projeto**, a cópia da regra global que o dono carrega e que ainda manda o executor
escalar para replanejamento. As outras quatro são correções locais de texto, sem efeito sobre o
comportamento do loop.

A lição de planejamento que esta execução deixa: dezessete entregas corretas produziram nove
corretivos, porque o card mede o bloco que escreve e o defeito mora entre blocos e entre arquivos.
A régua que fecha as duas classes está redigida e aguarda aplicação no tíquete de régua de autoria.
