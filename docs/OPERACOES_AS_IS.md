# Operações as-is — o lastro do modelo conceitual

Estado corrente das operações que disciplinam **como o modelo conceitual de um plano se escreve,
se valida e se afere**. Produzido no encerramento do `P-0746`, em 2026-09-22. Todo número aqui foi
re-derivado no ato; onde a medida envelhece, vem datada.

---

## Por que isto existiu

### O problema, com os números

O framework já publicava, desde o `P-0743`, a **forma** do modelo conceitual de um plano: que
seções ele tem, que tabelas, que colunas, e um verificador que recusa quem desviasse da forma. O
que ele não publicava era **de onde os elementos do modelo saem**.

A consequência foi medida em 2026-09-21, sobre o primeiro plano escrito inteiro sob aquela forma:

| medida | valor |
|---|---|
| ocorrências de `lastro` em `GOVERNANCA.md` | **0** |
| ocorrências de `lastro` na skill `diario-de-obras` | **0** |
| objetos que aquele plano declarou | **11** |
| `modelo.py check` sobre esse modelo | exit **0** — `modelo: OK` |
| veredito do dono sobre o mesmo modelo | **reprovado** |

O instrumento aprovava o que o dono reprovava. Ele aferia **forma**, não **procedência**: um modelo
podia estar impecavelmente formatado e descrever coisas que ninguém tinha pedido.

### A solução, em uma frase

Todo elemento do modelo passa a carregar, na própria tabela, o trecho do enunciado de onde saiu — e
o que não tem trecho de origem sai do contrato, sem sair da entrega.

### Vocabulário mínimo

| termo | o que é |
|---|---|
| **enunciado** | a seção `## 0. O problema, verbatim` de um plano: o pedido original, transcrito sem reescrita, mais o prompt que o originou |
| **lastro** | o trecho do enunciado de onde um elemento do modelo saiu, escrito numa célula da própria tabela do modelo |
| **objeto** | o que o plano constrói ou torna conforme, e que não existia ou não estava conforme quando ele começou |
| **propriedade** | a dimensão de um objeto que tem estado inicial e estado final distintos |
| **operação** | o ato que altera uma propriedade. Não possui propriedade própria |
| **promoção indevida** | propriedade escrita como se fosse objeto. Infla a tabela de objetos com linhas que nenhuma operação constrói |
| **requisito secundário** | entrega que o agente julga necessária e que o enunciado não pediu |
| **status terminal** | `done`, `cancelled` ou `superseded` — planos fechados, que norma nova não alcança |

---

## O arco

Sete tarefas, em três estratos. Cada estrato é inútil sem o anterior: não se pode aferir uma
exigência que não tem forma publicada, e não se pode publicar a forma de uma exigência que a norma
ainda não fez.

| estrato | pergunta que responde | tarefas |
|---|---|---|
| **1 — a norma** | o que um modelo pode conter, e como o enunciado se lê | `LST-T1`, `LST-T7`, `LST-T3` |
| **2 — a forma** | em que célula, exatamente, cada elemento declara a sua origem | `LST-T8`, `LST-T9` |
| **3 — a prova** | a máquina recusa o que o dono recusou, e o caso que originou tudo converge | `LST-T5`, `LST-T6` |

Três tarefas previstas na primeira publicação do plano não existem mais e não têm seção aqui: uma
foi dissolvida quando a medição desmentiu a razão dela, e duas saíram inteiras — com os dossiês
preservados — para o `TK-70`, porque o conteúdo delas não tinha lastro no enunciado. É a regra
deste plano aplicada ao próprio plano, antes da primeira linha de execução.

---

## `LST-T1` — de onde os elementos do modelo têm de vir

**Contexto que a motivou:** a norma descrevia a forma do modelo — objetos, propriedades, operações,
estados, versões — sem dizer a origem de nada. `lastro` tinha **0** ocorrências em `GOVERNANCA.md`
e **0** na skill `diario-de-obras`.

**O que é o artefato:** dois parágrafos de doutrina. Um em `GOVERNANCA.md` §3.2, intitulado
**Lastro no enunciado, e as duas vias de leitura**; outro na subseção *Modelo de domínio (seção do
plano)* de `.claude/skills/diario-de-obras/SKILL.md`, intitulado **Lastro, por elemento**.

**Como funciona na prática:** é regra de conduta para quem escreve um modelo, lida antes de
escrever. Ela diz duas coisas. A primeira, verbatim da norma:

> Todo objeto, toda operação e toda propriedade do modelo tem **lastro declarado**: uma âncora num
> trecho do enunciado do problema (`## 0. O problema, verbatim`) ou do prompt que originou o plano.
> Elemento sem esse lastro **não entra no modelo** — o modelo descreve o que foi pedido, não o que o
> modelador imaginou.

A segunda separa **duas vias** de leitura do mesmo enunciado: a *via de estado* é o trecho que
descreve como as coisas estão ou deverão estar, e popula a tabela de estado inicial e final; a *via
de operação* é o trecho que pede ação, e popula o fluxo. Ler pela via errada produz operação sem
lastro, ou estado final que nenhuma operação alcança.

**Protege contra:** modelo que descreve o que o agente supôs que o cliente queria. Um elemento sem
trecho de origem deixa de ser admissível no contrato.

---

## `LST-T7` — quantos objetos um enunciado comporta

**Contexto que a motivou:** nada na norma dizia como distinguir objeto de propriedade. O efeito foi
medido duas vezes em 2026-09-21, sobre dois modelos diferentes, e das duas vezes o dono recusou pelo
mesmo motivo. Num deles, quatro propriedades estavam escritas como objetos, para um enunciado que
comportava **um**.

**O que é o artefato:** o parágrafo **A decomposição do enunciado: objeto e propriedade** em
`GOVERNANCA.md` §3.2, imediatamente depois do parágrafo de lastro, e o parágrafo **Objeto e
propriedade, na decomposição** na skill.

**Como funciona na prática:** dá o teste literal que separa os dois. *O que o plano constrói é
objeto*; o que converge de um estado inicial a um estado final distinto é **propriedade** dele; e
**descrição de estado não vira objeto próprio** — o retrato de como as coisas estão entra como
propriedade e aparece na tabela de estado. A norma nomeia o defeito — **promoção indevida** — e
registra o caso medido em que ele apareceu.

**Protege contra:** a tabela de objetos inflada com linhas que nenhuma operação constrói. Não é
aferível por máquina: nenhum verificador decide se um substantivo do enunciado é objeto ou
propriedade. A guarda é o marco de validação, e a norma diz isso explicitamente.

---

## `LST-T3` — onde mora o que o enunciado não pediu

**Contexto que a motivou:** instituída a regra de lastro, faltava destino para o que não tem
lastro. Sem destino, um elemento sem origem ou entrava no modelo como se fosse contrato — e passava
a ser cobrado como se o dono o tivesse pedido — ou desaparecia do plano. `requisito secundário`
tinha **0** ocorrências na skill.

**O que é o artefato:** o parágrafo **Requisito secundário, a residência do elemento sem lastro**
na subseção de gramática da skill `diario-de-obras`.

**Como funciona na prática:** publica uma seção do plano, fora do modelo. Verbatim da gramática:

> O elemento com lastro é o requisito funcional e entra no modelo como contrato; o elemento sem
> lastro é não fundamental e reside na seção de nível 2 nomeada `Requisitos secundários`, em
> qualquer posição do plano, fora da `## 1`, em tabela
> `| requisito | por que o agente o julga necessário | quem responde |` (…)
> Elemento dessa seção não entra no modelo e não é aferido por lastro.

E fixa a natureza dela: é **transparente** ao dono — visível e declarada, **não** submetida à
aprovação dele —, com responsabilidade inteira do agente.

**Protege contra:** as duas falhas simétricas. O agente cobrado por entregar algo que ninguém pediu,
e o dono descobrindo tarde uma entrega que nunca lhe foi mostrada.

---

## `LST-T8` — a célula em que a origem se escreve

**Contexto que a motivou:** a norma passou a exigir lastro declarado, e nenhuma tarefa tinha dito
**onde** se declara. A tabela de objetos da gramática seguia em cinco colunas, e o verificador não
tinha campo cuja presença aferir.

**O que é o artefato:** três linhas da tabela de gramática da skill `diario-de-obras` — as linhas
`objetos`, `operações` e `estado` — mais a emenda do parágrafo de lastro.

**Como funciona na prática:** é a forma que um autor de modelo copia. A tabela de objetos passa a
seis colunas, terminando em `lastro`; a linha de máquina de cada operação admite um quarto campo
`` `lastro: <trecho>` `` depois de `tarefas:`; e a tabela de estado admite uma quarta coluna. O
mesmo parágrafo separa o que a máquina afere do que o marco guarda, e declara a **retroatividade**
em literal: *plano em status terminal não se migra*.

**Protege contra:** exigência sem lugar. Antes desta tarefa a norma pedia uma declaração que não
tinha onde ser escrita — e o card que viria depois não teria campo cuja presença medir.

---

## `LST-T9` — a residência se reconhece pelo nome, não pela posição

**Contexto que a motivou:** duas frases recém-publicadas não sobreviviam ao confronto com os planos
vivos. A forma prescrevia o cabeçalho de coluna `lastro` por igualdade literal, e o único modelo
vivo que já a usava escrevia `lastro na §0`; e prescrevia a seção de requisitos secundários pelo
**número** `## 2`, que dois planos vivos já usam para *Fatos estabelecidos* — enquanto a
retroatividade recém-publicada proíbe migrá-los.

**O que é o artefato:** três frases, em dois arquivos. Duas na skill `diario-de-obras` (o
casamento de cabeçalho e a residência por nome), uma em `GOVERNANCA.md` §3.2 (o caso medido).

**Como funciona na prática:** a coluna de lastro passa a ser reconhecida pelo cabeçalho que
**começa com** `lastro`, admitindo qualificação da âncora — `lastro na §0`, `lastro no prompt`. A
residência do requisito secundário passa a ser *seção de nível 2 nomeada*, em qualquer posição. E a
frase do caso medido, que comprimia duas recusas sobre modelos distintos numa só, passa a registrar
**dois modelos distintos** — um de um plano, outro da primeira versão do próprio plano que
instituía a regra.

**Protege contra:** doutrina que só é verdadeira em laboratório. Uma regra que prescreve um número
de seção já ocupado obriga a renumerar plano vivo, que é justamente o que a cláusula de
retroatividade proíbe.

---

## `LST-T5` — a máquina passa a recusar o que o dono recusou

**Contexto que a motivou:** a gramática já afirmava, no presente, que o verificador afere a coluna
de lastro — e `grep -c 'lastro'` devolvia **0** em `.claude/tools/modelo.py` e **0** em
`tests/test_modelo.py`. O verificador não sabia ler nada do que as quatro tarefas anteriores
publicaram.

**O que é o artefato:** a violação **`V21`** em `.claude/tools/modelo.py` — o vocabulário fechado
passa de `V1..V20` para `V1..V21` —, mais o campo `lastro` na estrutura de objeto, a função
`_indice_coluna_lastro`, a constante `_STATUS_TERMINAL_PLANO`, a leitura do quarto campo da linha de
operação, sete testes novos em `tests/test_modelo.py` e dez fixtures em `tests/fixtures/modelo/`.

**Como funciona na prática, em quatro passos:**

1. **O que dispara:** alguém roda `python .claude/tools/modelo.py check --plano <caminho>` — o mesmo
   comando que a orquestração já roda antes de despachar e antes de fechar cada tarefa.
2. **A entrada:** a seção `## 1. Modelo conceitual` do plano, mais o `status` do plano, lido do
   diário de obras pelo mesmo carregador que o comando já usava.
3. **O processamento:** se o plano está em status terminal, a regra não o alcança e nada acontece.
   Caso contrário, o verificador localiza a coluna de lastro pelo cabeçalho que começa com `lastro`
   e emite **uma violação por objeto** cuja célula esteja vazia ou ausente.
4. **A saída:** uma linha por objeto sem lastro e exit `1`. Saída real, sobre a fixture de
   ausência:

   ```
   V21 objeto — objeto sem lastro declarado insumo do teste
   V21 objeto — objeto sem lastro declarado resultado do teste
   modelo: FALHOU — 2 violação(ões)
   ```

   Sobre a fixture que declara lastro sob o cabeçalho qualificado `lastro na §0`, e sobre a fixture
   sem lastro mas em status `done`, o mesmo comando devolve `modelo: OK` e exit `0`. As três
   fixtures diferem entre si só no ponto que cada uma fixa.

**Protege contra:** o vão entre a doutrina e o instrumento. Antes desta tarefa a norma exigia
lastro e o verificador não o via; um modelo sem uma única origem declarada saía `modelo: OK`.

**O procedimento que ela instalou — migrar não é afrouxar.** Regra nova alcança o corpus de teste
que ela regula: as sete fixtures que tinham tabela de objetos ganharam a coluna, e **nenhum valor de
asserção existente mudou**. A distinção fica publicada no próprio card: migrar a forma é manutenção
obrigatória; editar valor esperado, remover caso ou afrouxar fixture para caber na regra nova é
enfraquecer cobertura, e continua proibido. Fixture que não fala a forma vigente deixa de isolar a
regra que ela existe para fixar.

---

## `LST-T6` — o caso que originou tudo converge

**Contexto que a motivou:** o plano que motivou toda esta doutrina seguia com o modelo que o dono
recusou: **11 objetos**, 21 propriedades, e nenhuma origem declarada. Depois da tarefa anterior, o
verificador passou a recusá-lo — exit `1`, com **11 violações `V21`**, uma por objeto.

**O que é o artefato:** o modelo do `P-0745` reautorado na **versão 2**, mais a seção
`## Requisitos secundários` nova naquele plano e a tabela de marcos dele corrigida.

**Como funciona na prática:** não é código nem regra — é o caso de prova. O enunciado daquele plano
foi relido pelas duas vias e decomposto de novo: **11 objetos viraram 3** (*tarefa*, *agente de
planejamento*, *agente model designer*), 21 estados finais viraram **6**. O que não tinha lastro
migrou para a seção nomeada, sem renumerar nada — aquele plano usa `## 2` para *Fatos
estabelecidos*, e a seção nova entrou pelo nome. O gate do marco de validação, que previa só dois
desfechos, ganhou o terceiro que a execução real produziu: recusa **reautora o modelo**, não cancela
o plano.

A decomposição discriminou **dentro** de cada objeto promovido em vez de descartá-lo inteiro: de um
objeto que reunia duas coisas, a metade com lastro voltou como propriedade de uma tarefa e só a
metade sem lastro foi para requisitos secundários.

Saída real, sobre o mesmo arquivo que antes saía `FALHOU`:

```
modelo: OK — 6 operações, 3 objetos, 6 propriedades, 7 tarefas, versão 2
```

Os **23 fragmentos de lastro** declarados — 5 na tabela de objetos, 12 no fluxo, 6 na tabela de
estado — foram conferidos um a um contra o enunciado daquele plano: 23 de 23 são recorte verbatim,
com os erros de digitação do original preservados. Recorte, não paráfrase.

**Protege contra:** doutrina que se escreve e não se aplica. O plano que originou o enunciado é o
primeiro a ser julgado por ele.

---

## O que vale além deste plano

| regra | o que resolve | residência |
|---|---|---|
| Lastro declarado por elemento | modelo que descreve o que ninguém pediu | `GOVERNANCA.md` §3.2, *Lastro no enunciado* |
| As duas vias de leitura do enunciado | estado tratado como trabalho, e vice-versa | `GOVERNANCA.md` §3.2, mesmo parágrafo |
| Objeto, propriedade e promoção indevida | tabela de objetos inflada | `GOVERNANCA.md` §3.2, *A decomposição do enunciado* |
| Residência do requisito secundário | entrega invisível ao dono, ou cobrada como contrato | skill `diario-de-obras`, *Requisito secundário* |
| Residência se identifica por rótulo, não por posição | doutrina que obriga a renumerar plano vivo | skill `diario-de-obras`, *Lastro, por elemento* |
| Retroatividade: plano em status terminal não se migra | norma nova invalidando trabalho aceito | skill `diario-de-obras`, mesmo parágrafo |
| Migrar corpus de teste não é afrouxar cobertura | fixture que deixa de isolar a regra que fixa | card `LST-T5` do `P-0746`; matéria do `TK-72` |

---

## Os ganhos, medidos

Todos re-derivados em 2026-09-22, no fechamento.

| medida | antes | depois |
|---|---|---|
| `lastro` em `GOVERNANCA.md` | 0 | 4 |
| `lastro` na skill `diario-de-obras` | 0 | ≥1 |
| `lastro` em `.claude/tools/modelo.py` | 0 | presente (campo, função, constante, regra) |
| vocabulário de violações do verificador | `V1..V20` | `V1..V21` |
| `check` sobre o modelo que o dono reprovou | exit **0**, `modelo: OK` | exit **1**, 11 violações `V21` |
| o mesmo, depois da reautoria | — | exit **0**, `6 operações, 3 objetos, 6 propriedades` |
| objetos naquele modelo | 11 | 3 |
| estados finais naquele modelo | 21 | 6 |
| ramo caduco `cancelled` naquele plano | 2 ocorrências | 0 |
| suíte completa (`pytest tests -q`) | 262 passed | **269 passed** |
| `tests/test_modelo.py` | 23 passed | 30 passed |
| fixtures de modelo | 9 | 12 |

O piso de regressão subiu em vez de cair: nenhum valor de asserção existente foi editado, e as sete
fixtures migradas reproduzem **número a número** o que produziam antes.

---

## O padrão que a execução revelou

Os defeitos desta execução formam uma classe, e ela tem nome: **operação de modelo com mais de uma
oração é operação mal recortada.**

Uma das seis operações deste plano foi escrita com três orações. Cada uma tinha um lastro diferente,
e duas não sobreviveram às regras que o próprio plano institui: uma era inexequível — a medição
mostrou que reprovaria um modelo já aceito e o modelo do próprio plano —, a outra mandava a máquina
reconhecer uma forma textual que nunca foi publicada. As duas foram recortadas, e cada recorte ficou
declarado em vez de silencioso.

O custo é a parte que importa: as duas orações defeituosas só apareceram **na implementação**, e
custaram duas paradas de executor. Nenhuma delas era invisível — o marco de validação que aprovou o
modelo as tinha diante dos olhos, redigidas numa frase só.

Um segundo padrão, menor e mais barato: **card cujo referente não existe na árvore no momento do
despacho não produz uma linha.** As duas paradas foram sobre o mesmo card, e as duas foram
reparadas no card, não na execução. Quando os dois referentes ausentes foram fechados, a mesma
tarefa executou linearmente.

---

## Defeitos da execução, com estado

| defeito | estado | o que fecha |
|---|---|---|
| Verificação de card de redação por contagem de ocorrência de palavra: sairia verde com três menções decorativas | 🟡 caso fechado, classe sem guarda — os cards seguintes passaram a recorte de literal, nada impede o próximo de voltar à contagem | pendência 4 (`TK-72`) |
| Card que herda rota de achado e declara a matéria fora de escopo: a rota fica órfã | 🟡 a rota foi re-declarada e executada; nenhuma guarda impede a repetição | pendência 4 (`TK-72`) |
| `Arquivos-alvo` que não nomeia o efeito colateral obrigatório da própria mudança | 🟡 a execução absorveu e declarou item a item; o diff confirma a declaração | pendência 4 (`TK-72`) |
| Verificação com comando mas sem valor esperado | 🟡 a execução decidiu pela única leitura inequívoca, e acertou no mérito | pendência 4 (`TK-72`) |
| Operação com três orações de lastros diferentes | 🟡 as duas orações sem lastro foram recortadas com ato de modelo registrado; nada impede a próxima operação de nascer igual | pendência 5 (`TK-73`) |
| Frase de doutrina que comprimia duas recusas sobre modelos distintos numa só | 🟢 corrigida na norma, com par presença-ausência sobre o literal | — |
| Gramática prescrevendo número de seção já ocupado no acervo | 🟢 residência passou a ser por nome, com par presença-ausência | — |
| Cabeçalho de coluna exigido por igualdade literal, contra o único modelo vivo que o usava | 🟢 casamento por prefixo, fixado por fixture dedicada | — |
| Verificador aprovando modelo sem nenhuma origem declarada | 🟢 `V21`, com três fixtures e sete testes | — |
| `review_evidence.py` não expande alvo terminado em barra: dez fixtures chegaram ao revisor como falso "sem atribuição" | 🔴 diagnosticado e medido, instrumento intocado | pendência 6 (`TK-74`) |
| `GOVERNANCA.md` §3.2 sem ramo para primeira versão recusada e reautorada | 🔴 regra ausente, e a divergência já se manifestou | pendência 3 (`TK-70`) |

---

## Pendências abertas ao fim do plano

| # | pendência | por que ficou aberta | o que a fecha | bloqueia? |
|---|---|---|---|---|
| **1** | **O critério de "ator inédito na operação"** — o modelo reautorado tem 5 de 5 sujeitos citados no fluxo que não são objetos da tabela. É classe que o dono tipificou e chamou de integralmente mecânica; foi dispensada por medição, porque a régua literal reprova 6 dos 7 sujeitos de um modelo **já aceito** e 4 dos 4 do modelo deste plano | decisão do dono, não do loop | veredito dele: manter a dispensa, ou manter a classe e reformulá-la de modo aferível | **o marco de validação do modelo reautorado.** Mantida a leitura literal, aquele modelo é reprovado pelo mesmo motivo de 2026-09-21 |
| **2** | **A versão pendente do modelo deste plano** — existe como bloco irmão, `pendente`, e carrega os dois recortes de operação mais a contabilidade de tarefas da janela | o aceite é ato do dono, num marco | `go` do dono; aceita, a versão ocupa a seção vigente, em ato do modelador | não bloqueia entrega; sem ele o plano fica com duas seções de modelo convivendo |
| **3** | **Vigência do modelo, e o estado de uma primeira versão recusada** — dois modelos vivos estão **no mesmo estado de fato** com valores opostos: um `pendente` aguardando marco, outro `vigente` aguardando marco | a norma não tem ramo para primeira versão recusada e reautorada | `TK-70`, Pacote A, que já edita esse parágrafo | não |
| **4** | **A régua de autoria de card** — quatro defeitos da mesma família, todos sobre como se escreve um card para quem chega frio | fora do escopo deste plano | `TK-72`, quatro pacotes | não |
| **5** | **Recorte e sujeito da oração de operação** | fora do escopo deste plano | `TK-73`, Pacote 1; o Pacote 2 depende da pendência 1 | não |
| **6** | **Atribuição de alvo em forma de diretório** no gerador de evidência | fora do escopo deste plano | `TK-74` | não |
| **7** | **A categoria "tarefa que não materializa operação"** — se existe, e como se declara | nenhum plano vivo tem o caso hoje | `TK-71`; sem caso, fecha por obsolescência | não |

### Estado honesto

O plano entregou **7 de 7 tarefas**, todas julgadas: seis `aprovado` 100% e uma `aprovado com
ressalva` 88%. A norma, a gramática, o instrumento e o caso de prova estão no lugar, e o verificador
passou a recusar exatamente o modelo que o dono recusou — que era a medida que originou tudo.

Ficaram **sete pendências**. Uma só é bloqueante, e é a **pendência 1**: ela decide se o modelo
reautorado passa ou não no marco de validação, e é decisão do dono por construção — reparar antes de
ele ler escolheria uma leitura do critério dele sem ele, e alcançaria três modelos, dois fora deste
plano.

**Efeito fora do projeto:** as pendências 3, 4 e 5 tocam doutrina do kit, que é transportada para os
cinco projetos derivados. Enquanto abertas, o defeito que cada uma descreve continua possível em
qualquer um deles. As pendências 2, 6 e 7 são internas ao hub.
