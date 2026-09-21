# Entregas — `P-0743`

**O modelo as-is das operações que o plano deixou**, tarefa a tarefa, com o estado de cada
pendência. É o artefato pelo qual o plano foi validado — **aceito em 2026-09-21**.

**Cobertura:** `P-0741` (o modelo conceitual) e `P-0743` (o modelo de domínio), numa leitura só ·
**Medido em 2026-09-21** · Este documento descreve **o que existe hoje na árvore**. O registro da
execução mora nos dois planos e em `docs/RDO/`.

---

## Por que estes planos existiram

**O problema.** Um plano deste repositório é um documento de milhares de linhas: o `P-0743` tem
5.452 linhas, o `P-0741` tem 1.852. Quem encomendou o trabalho não tem como validá-lo lendo isso, e
não deveria precisar. Antes destes dois planos, a descrição do que um plano entregava era uma lista
de **frases numeradas independentes**, cada uma carregando o próprio estado gravado à mão. Três
consequências medidas:

- **O estado era escrito, e portanto podia mentir.** Cada frase trazia o próprio `concluída` /
  `prevista`, digitado por quem passava. Um plano exibia **vinte estados paralelos** e não dizia em
  que ponto estava.
- **Não havia encadeamento.** Frases paralelas não dizem o que depende do quê, então não havia como
  derivar posição no fluxo.
- **Não havia aceite.** O plano não declarava de onde partia nem onde queria chegar, e o sucesso
  dele não era confrontável contra nada.

**A solução, em uma frase.** O que era prosa vira **estrutura verificável por máquina**, e o que
era estado escrito à mão vira **estado derivado**: o plano declara objetos, as propriedades deles e
as operações que as alteram, mais o retrato de onde parte e onde quer chegar — e um programa lê
tudo isso e responde, num comando, em que estágio o plano está.

### Vocabulário mínimo

| termo | o que é |
|---|---|
| **modelo** | a seção `## 1. Modelo conceitual`, que abre todo plano e descreve o que ele entrega |
| **propriedade** | a característica de um objeto que o trabalho altera, ou que precisa manter e por isso vigia |
| **objeto** | o que **possui** propriedade (um arquivo de norma, um programa, um papel de agente) |
| **operação** | o que **altera** a propriedade de um objeto; numeradas `OP-1`, `OP-2`, … |
| **estágio** | a primeira operação que ainda não concluiu — a posição do plano no fluxo |
| **o instrumento** | `.claude/tools/modelo.py`, o programa que confere o modelo (`check`) e o exibe (`show`) |
| **o modelador** | `.claude/agents/pantonic-model-designer.md`, o único papel que escreve no modelo |
| **card / tarefa** | a unidade de trabalho despachada a um executor; identificada `DOM-T1`, `MC-T2`… |

---

## Como validar este documento

Três comandos, re-rodáveis a qualquer momento nesta árvore. Toda afirmação de comportamento abaixo
sai de um deles.

```
python .claude/tools/modelo.py show  --plano docs/plans/P-0743-modelo-de-dominio.md
python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md
python -m pytest tests/ -q
```

---

## O que foi pedido, e o que chegou

| artefato pedido | entregue? |
|---|---|
| **A forma do modelo** — estrutura fixa para descrever o que um plano entrega | **Sim**, e verificada por máquina: 20 regras |
| **O estado derivado** — andamento que ninguém escreve à mão | **Sim**. Nenhum papel grava estado; o instrumento o deriva das tarefas |
| **O aceite do plano** — de onde parte, onde quer chegar | **Sim**. 21 propriedades, cada uma com estado inicial e estado final declarados |
| **O agente modelador** — dono único de todo ato sobre o modelo | **Sim**, e com autoria real exercida |
| **Um plano escrito na forma nova** | **Sim** — o `P-0743` é o primeiro do acervo |
| **A porta de entrada pública** | **Sim**, `README.md` §8.1 |

---

## A leitura do dono — a saída real

Esta é a entrega central, e o coração da validação. O `P-0743` é **o primeiro plano do acervo cujo
próprio modelo está na forma nova**, escrito pelo modelador na primeira autoria real dele.

`python .claude/tools/modelo.py show --plano docs/plans/P-0743-modelo-de-dominio.md`, rodado em
2026-09-21, abre assim:

```
# Modelo de domínio — P-0743 — O modelo conceitual vira modelo de domínio
Estado do modelo: versão 1 · 2026-09-21 · situação: vigente · 13 operações · estágio atual: concluído
```

A seguir vem a tabela de objetos. **Trecho** — a saída traz os nove:

```
## Objetos
| objeto | o que é | propriedades | contrato | origem |
|---|---|---|---|---|
| instrumento do modelo | o programa que confere a seção contra a gramática e gera a leitura do
dono | vocabulário de violações, leitura do dono, tolerância à forma anterior, descrição de si
mesmo | `.claude/tools/modelo.py`, verbos `check` e `show`, exits `0`, `1` e `2` com literais
fixos; lê as tarefas do plano por `backlog._parse_plano` e não reescreve `backlog.py`; cada regra
nova nasce com fixture e teste pelo caminho do usuário | OP-3 |
| modelador | o agente único dono de todo ato sobre o modelo de um plano | atos declarados,
ensinamento de autoria, gate de devolução | `.claude/agents/pantonic-model-designer.md`; front
matter com nome, descrição e lista de ferramentas, e corpo com os atos, o ensinamento e o gate; as
duas portas de inventário do kit contam os agentes e hoje fecham sobre dez | OP-5 |
```

Depois o fluxo inteiro, agrupado nos quatro trechos em que o trabalho realmente se dividiu. **A
saída completa traz as treze operações**; estas são as quatro que abrem cada trecho:

```
## Fluxo

**A. A forma nasce: norma, gramática e instrumento**
[concluída] OP-1 — O redator da norma grava na doutrina do kit o que o modelo de um plano passa a
            ser: objetos e operações encadeadas no lugar de frases soltas, a posição no fluxo
            derivada do andamento das tarefas, e a autoria concentrada num papel só.
            precisa de: acervo de planos na forma anterior, doutrina publicada do kit
            altera: norma do modelo de domínio.forma prescrita, norma do modelo de domínio.regra
            de estágio, norma do modelo de domínio.divisão de papéis

**B. O papel nasce, e os demais papéis se alinham a ele**
[concluída] OP-5 — O autor de papéis cria o agente único dono de todo ato sobre o modelo e escreve
            nele o ensinamento de como um modelo se escreve, que deixa de ficar pulverizado nos
            demais agentes.
            precisa de: norma do modelo de domínio, gramática do modelo
            altera: modelador.atos declarados, modelador.ensinamento de autoria

**C. A propriedade entra, e com ela o aceite e a versão**
[concluída] OP-7 — O redator da norma reescreve a norma para propriedades: objeto passa a ser o
            que possui propriedade, o plano declara estado inicial e estado final, o aceite do
            plano é a confrontação dos dois, e a emenda ao modelo versiona em vez de reescrever.
            precisa de: norma do modelo de domínio
            altera: norma do modelo de domínio.forma prescrita, norma do modelo de domínio.regra
            de aceite, norma do modelo de domínio.regra de versão

**D. O modelo deste plano, e a porta de entrada**
[concluída] OP-13 — O mantenedor abre a porta de entrada pública ao modelo de domínio e confere a
            documentação pública contra o estado da árvore ao fim do plano.
            precisa de: modelo deste plano, doutrina publicada do kit, instrumento do modelo
            altera: documentação pública do kit.descrição do modelo na porta de entrada
```

E termina no confronto que **é** o aceite do plano — o estado de onde cada propriedade partiu e
onde chegou. **Trecho** — a saída traz as vinte e uma linhas:

```
## Estado
| propriedade | estado inicial | estado final |
|---|---|---|
| instrumento do modelo.vocabulário de violações | nove regras, de V1 a V9, sobre a forma anterior,
medidas em 2026-09-20 | vinte regras, de V1 a V20, cobrindo propriedade, estado inicial e final,
registro de versões e versão pendente, cada uma com fixture e teste pelo caminho do usuário |
| modelador.atos declarados | não existia agente dono do modelo, e o kit tinha nove agentes |
existe um décimo agente, com quatro atos declarados — autoria, emenda, conflito e leitura —, e as
duas portas de inventário do kit fecham sobre dez |
| modelo deste plano.forma da seção | a seção trazia doze frases numeradas com estado gravado em
cada uma, mais uma tabela de mudanças do modelo | a seção traz nove objetos com propriedades,
treze operações encadeadas, o estado inicial e o final de cada propriedade e o registro de versões |
```

**Uma ressalva de fidelidade, declarada.** A linha de estado final do vocabulário de violações diz
*"cada uma com fixture e teste pelo caminho do usuário"*. Isso é verdade para `V1`..`V14` e **não é
verdade para `V15`..`V20`** — é o defeito `AE-20`, medido, aberto e descrito abaixo. O texto do
modelo descreve o alvo; a medição de hoje mostra a diferença.

---

## O arco — os estratos

As 18 tarefas do `P-0743` e as 8 do `P-0741` não são 26 assuntos. São quatro camadas, e cada uma é
inútil sem a anterior: não se escreve uma gramática sem a norma que diz o que ela governa, não se
programa um instrumento sem a gramática que ele lê, e não se pede a um agente que escreva um modelo
antes de existir forma que ele obedeça.

| estrato | pergunta que responde | tarefas |
|---|---|---|
| **0. A forma, primeira versão** | *Como se descreve o que um plano entrega?* | `MC-T1`, `MC-T2`, `MC-T3`, `MC-T4`, `MC-T5` |
| **A. A forma nasce em objetos** | *E se a descrição tiver encadeamento, em vez de frases soltas?* | `DOM-T1`, `DOM-T2`, `DOM-T3` |
| **B. O papel nasce** | *Quem escreve isso, e quem para de escrever?* | `DOM-T4`, `DOM-T5` |
| **C. A propriedade entra** | *Como o plano declara de onde parte e onde chega?* | `DOM-T7`, `DOM-T8`, `DOM-T9`, `DOM-T9a` |
| **D. A forma se prova em si mesma** | *A forma nova sobrevive ao primeiro uso real?* | `DOM-T10`, `DOM-T6` |

**Fora dos estratos.** Dez tarefas não respondem pergunta nova: elas reparam a entrega de outra
tarefa, e nasceram de defeito medido durante a execução. São `MC-T2a`, `MC-T2b`, `MC-T4a`,
`DOM-T3a`, `DOM-T3b`, `DOM-T5a`, `DOM-T5b`, `DOM-T8a`, `DOM-T9b` e `DOM-T9c`. Cada uma tem seção
própria no **Apêndice A**, onde a regra de apresentação vigente manda que matéria corretiva resida.

---

# Estrato 0 — a forma, primeira versão (`P-0741`)

## `MC-T1` — A primeira norma do modelo, e a gramática que a máquina lê

**Contexto que a motivou:** não existia forma nenhuma. Cada plano descrevia o que entregava do
jeito que o autor preferisse, e não havia texto que dissesse o que essa descrição deveria conter.

**O que é o artefato:** três textos normativos, cada um com residência única — a seção `### 3.2` de
`GOVERNANCA.md` (a norma: o que o modelo é); a subseção `Modelo conceitual (seção do plano)` da
skill `.claude/skills/diario-de-obras/SKILL.md` (a gramática: a forma exata de cada linha); e, em
`docs/RUBRICA_DE_REVISAO.md`, o alvo `modelo` na tabela de achados de processo.

**Como funciona na prática:** não é programa e não tem gatilho — é o texto que todos os demais
artefatos obedecem e citam. A separação entre os dois primeiros é o que permitiu o resto: a norma
diz **o que** o modelo é, em prosa que uma pessoa lê; a gramática diz **onde cada caractere vai**,
em tabela que um programa lê. Sem essa divisão, o instrumento do card seguinte teria de adivinhar.

**Protege contra:** plano cuja descrição de entrega só faz sentido para quem a escreveu.

## `MC-T2` — O instrumento: um comando que confere, outro que mostra

**Contexto que a motivou:** uma norma que ninguém verifica é uma sugestão. Escrita a forma, nada
impedia um plano de violá-la.

**O que é o artefato:** `.claude/tools/modelo.py`, com dois verbos — `check` (julga) e `show`
(exibe) — e três códigos de saída: `0` conforme, `1` violação, `2` forma anterior.

**Como funciona na prática:** quem dispara é a orquestração, antes de despachar cada tarefa e antes
de fechar cada uma. A entrada é o caminho de um plano; a saída é um veredito e, no caso de falha, a
lista de violações. Rodado hoje sobre uma fixture defeituosa:

```
$ python .claude/tools/modelo.py check --plano tests/fixtures/modelo/plano-invalido.md
V13 secao — cabeçalho, objetos, estado ou registro de versões ausente
V5 OP-1 — objeto inexistente objeto fantasma
V1 OP-2 — operação sem tarefa
V3 OP-3 — tarefa inexistente EX-T99
V12 OP-4 — literal técnico no texto
V6 objeto — objeto externo sem uso objeto sem uso
V7 objeto — origem inexistente objeto orfão
V2 EX-T2 — tarefa sem operação
V4 EX-T3 — operação inexistente OP-77
V14 EX-T4 — contrato ausente para OP-2
modelo: FALHOU — 10 violação(ões)
EXIT=1
```

Cada linha nomeia a regra violada (`V5`), onde (`OP-1`) e o quê (`objeto fantasma`). `V1` e `V2`
são o par que sustenta o resto: **toda operação tem de ter tarefa que a materialize, e toda tarefa
tem de citar a operação que materializa.** É o que impede um plano de prometer o que ninguém vai
fazer, e de fazer o que ninguém prometeu.

**Protege contra:** plano cuja descrição de entrega e cuja lista de tarefas divergem sem que
ninguém note.

## `MC-T3` — Os papéis que escrevem o modelo

**Contexto que a motivou:** escrita a forma e o verificador, faltava dizer **quem** escreve. Sem
isso, ou ninguém escreve, ou todo mundo escreve.

**O que é o artefato:** as definições de conduta de três agentes — `.claude/agents/`
`pantonic-planner.md`, `pantonic-reviewer.md` e `pantonic-consultant.md` —, cada uma ganhando a
cláusula do que aquele papel faz diante do modelo.

**Como funciona na prática:** o gatilho é o despacho de cada agente; a definição de conduta é lida
por ele no início do trabalho. Nesta primeira versão os **três** escreviam no modelo: o planejador
na autoria, o revisor confirmando, o consultor emendando.

**Protege contra:** modelo que envelhece porque nenhum papel tem o dever de atualizá-lo. Esta
solução foi substituída no estrato B — três mãos na mesma região é a origem do defeito que o
`DOM-T4` fechou.

## `MC-T4` — O loop passa a ler o modelo

**Contexto que a motivou:** o instrumento existia e nada o chamava. Verificador que ninguém executa
não verifica.

**O que é o artefato:** duas skills de procedimento — `.claude/skills/scrum-master/SKILL.md` e
`.claude/skills/passagem-de-bastao/SKILL.md` — que passam a chamar `modelo.py` em pontos nomeados.

**Como funciona na prática:** o gatilho é o próprio ciclo de execução. A orquestração roda
`modelo.py check` antes de despachar uma tarefa e antes de fechá-la: exit `1` segura a tarefa,
exit `2` (forma anterior) segue com nota. E abre todo marco e todo relatório de encerramento com
`modelo.py show`. É por esse último ponto que este documento existe na forma em que está.

**Protege contra:** verificação que depende de alguém lembrar de rodá-la.

## `MC-T5` — A porta de entrada pública, e o veredito (a tarefa que segue aberta)

**Contexto que a motivou:** o modelo estava descrito para quem trabalha dentro do repositório, e em
nenhum lugar para quem chega de fora.

**O que é o artefato:** as seções §5 e §8 do `README.md`, mais o ato de leitura do dono sobre a
saída de `modelo.py show`.

**Como funciona na prática:** a parte escrita está na árvore. **O `Pronto quando` do card exige o
veredito do dono, que é ato dele e não de nenhum agente** — por isso esta é a única tarefa dos dois
planos que não fechou: está em `review`, não em `done`.

**Protege contra:** entrega que se declara aceita por quem a produziu.

---

# Estrato A — a forma nasce em objetos (`P-0743`)

## `DOM-T1` — A norma, reescrita em objetos e operações

**Contexto que a motivou:** a forma do `P-0741` descrevia um plano como frases numeradas
independentes, cada uma com estado gravado à mão. Frases paralelas não têm encadeamento, e estado
escrito à mão diverge do real.

**O que é o artefato:** a seção `### 3.2` de `GOVERNANCA.md`, substituída inteira; mais a matriz de
responsabilidades do §3 do mesmo arquivo, que ganha a linha `**Modelagem**` e passa de nove para
dez papéis.

**Como funciona na prática:** é texto normativo, sem gatilho próprio — todo agente e toda skill que
tocam o modelo o citam. Três regras nasceram aqui, e são as que governam tudo o mais:

1. A descrição de um plano é feita de **objetos e operações encadeadas**, não de frases soltas.
2. O andamento é **derivado e nunca gravado** — operação está `concluída` quando todas as tarefas
   dela fecharam, e o **estágio atual** é a primeira que não está.
3. A autoria do modelo se concentra em **um papel só**.

**Protege contra:** plano que exibe vinte estados paralelos, todos escritos à mão, e não diz em que
ponto está.

**O procedimento que ela instalou** — **estado é derivado, não escrito.** Nenhum papel grava
andamento no modelo. Residência: `GOVERNANCA.md` §3.2, parágrafo *"Estágio, não status"*.

## `DOM-T2` — A gramática que a máquina lê

**Contexto que a motivou:** publicada a norma em prosa, faltava a forma exata de cada linha. Um
programa não lê prosa.

**O que é o artefato:** a subseção `### Modelo de domínio (seção do plano)` da skill
`.claude/skills/diario-de-obras/SKILL.md` — uma tabela com uma linha por elemento: a forma à
esquerda, a regra e o código da violação à direita.

**Como funciona na prática:** o gatilho é a autoria de um modelo. Quem escreve consulta a tabela
para saber o que vai em cada linha; o instrumento implementa exatamente aquelas regras. A tabela é
a **residência única** da forma: é dela que sai o código de violação que o `check` imprime, e é por
isso que a mensagem de erro do programa e a regra escrita não podem divergir.

**Protege contra:** norma e verificador que discordam sobre o que é válido.

## `DOM-T3` — O instrumento aprende a forma nova

**Contexto que a motivou:** o instrumento do `P-0741` conhecia **nove** regras (`V1`..`V9`), todas
sobre a forma de frases numeradas. A forma nova não era verificável.

**O que é o artefato:** `.claude/tools/modelo.py` reescrito para ler objetos e operações, com o
vocabulário passando de 9 para **14** violações e o `show` reorganizado para abrir pelo estágio.

**Como funciona na prática:** duas propriedades entram aqui e são as que fazem o instrumento
utilizável num repositório real.

A primeira é a **tolerância à forma anterior**. O acervo tem **24 planos** hoje, e só um está na
forma nova. Se o instrumento reprovasse os outros 23, travaria o repositório. Ele os reconhece e
sai `2`, que não bloqueia nada:

```
$ python .claude/tools/modelo.py check --plano docs/plans/P-0741-modelo-conceitual.md
modelo: forma anterior — plano na forma de orações (sem '### 1.2 Fluxo de operações')
EXIT=2

$ python .claude/tools/modelo.py check --plano docs/plans/P-0739-backlog-instrumento.md
modelo: ausente — plano anterior à doutrina (sem '## 1. Modelo conceitual')
EXIT=2
```

Repare que os dois casos são **distinguidos**: um plano na forma intermediária e um plano anterior
a tudo dão mensagens diferentes. **Nenhum plano do acervo foi migrado, e nenhum será.**

A segunda é a verificação de **ordem real de encadeamento**. Não basta que os objetos existam: o
plano não pode depender de uma coisa antes de ela nascer. Medido hoje na segunda fixture defeituosa:

```
$ python .claude/tools/modelo.py check --plano tests/fixtures/modelo/plano-invalido-2.md
V9 OP-2 — operação desencadeada
V10 OP-3 — objeto produzido depois objeto de OP-5
V8 OP-3 — fora da sequência
V11 OP-3 — identificador duplicado
modelo: FALHOU — 4 violação(ões)
EXIT=1
```

`V10` é a mais forte: **nenhuma operação pode precisar de objeto que só nasce depois dela.** É o
que torna o estágio uma informação confiável em vez de uma numeração arbitrária.

**Protege contra:** plano cuja ordem declarada não é a ordem em que o trabalho pode acontecer.

---

# Estrato B — o papel nasce, e os demais se alinham

## `DOM-T4` — O modelador: um dono, quatro atos

**Contexto que a motivou:** três papéis escreviam no modelo — planejador, revisor e consultor —,
cada um com uma cláusula própria. Três mãos na mesma região, sem regra de precedência. E o
ensinamento de *como* se escreve um modelo estava pulverizado entre eles.

**O que é o artefato:** `.claude/agents/pantonic-model-designer.md`, o **décimo** agente do kit
(eram nove; `ls .claude/agents/*.md | wc -l` imprime `10` hoje). Carrega os atos declarados, o
ensinamento de autoria e o gate de devolução.

**Como funciona na prática:** o gatilho **nunca é outro agente** — nenhum agente do kit tem
ferramenta para despachar outro. Quem precisa de um ato de modelo devolve um **dossiê fechado de
seis campos** (`Plano`, `Ato`, `Motivo`, `Fato novo`, `Restrição`, `Devolver`) na própria linha de
retorno, e **para**. Quem conduz a sessão lê o dossiê e despacha o modelador.

| ato | quando | o que devolve |
|---|---|---|
| **autoria** | o plano nasce | a seção do modelo, escrita pela primeira vez |
| **emenda** | uma decisão muda o que o plano entrega | a versão nova, como bloco irmão da vigente |
| **conflito** | a entrega contradiz o texto de uma operação | a seção corrigida para o fato verificável |
| **leitura** | alguém precisa entender o modelo | a explicação, sem mudar nada |

O ensinamento que mora nele **começa pela propriedade**: identificam-se as características que o
trabalho altera ou vigia, e delas caem os objetos e as operações por decomposição — não por
intuição.

**Protege contra:** região de documento com várias mãos e nenhuma regra de precedência.

**O procedimento que ela instalou** — **nenhum agente aciona outro agente.** Pedido de trabalho
viaja como dossiê na linha de retorno; quem conduz a sessão despacha. Residência:
`GOVERNANCA.md` §3.2, parágrafo final.

## `DOM-T5` — Os demais papéis param de escrever

**Contexto que a motivou:** criar o dono único não basta enquanto os outros três mantêm a cláusula
que os autoriza a escrever. Duas residências do mesmo direito divergem no primeiro ajuste.

**O que é o artefato:** as definições de conduta de `pantonic-reviewer.md`, `pantonic-planner.md` e
`pantonic-consultant.md`, mais a skill `scrum-master`.

**Como funciona na prática:** o revisor **perde a ferramenta de escrita** fora do caminho do laudo.
A divergência que ele encontra entre a entrega e o texto de uma operação não vira mais uma edição:
vira **achado de processo de alvo `modelo`**, registrado no laudo. O planejador entrega o plano sem
a seção do modelo e devolve o dossiê de autoria junto. O consultor devolve o dossiê de emenda junto
com o reparo do escalonamento.

O desenho é assimétrico de propósito: **quem detecta não conserta**. Quem detecta descreve o que
mediu; quem conserta é o dono da região.

**Protege contra:** a fenda entre julgar e escrever — o papel que avalia uma entrega e também a
edita não tem como ser auditado.

---

# Estrato C — a propriedade entra, e com ela o aceite

## `DOM-T7` — A norma ganha propriedade, estado e versão

**Contexto que a motivou:** a forma do estrato A dizia o que um plano faz, e não de onde ele parte
nem onde quer chegar. Sem isso, o sucesso do plano não é confrontável contra nada — e a fronteira
entre objeto e operação era intuição, não teste.

**O que é o artefato:** a seção `### 3.2` de `GOVERNANCA.md`, reescrita pela segunda vez.

**Como funciona na prática:** quatro regras entram, e a primeira é a que torna o método
**decidível** em vez de intuitivo:

1. **O teste de objeto e operação.** *Objeto é o que possui propriedade. Operação não possui
   propriedade* — operação é o que **altera** a propriedade de um objeto. Propriedade que aparece
   numa operação é sinal de operação mal recortada, e a operação **decompõe-se em um objeto mais
   uma operação nova**.
2. **O critério de entrada.** Característica que não interessa a quem encomendou **não é
   propriedade e não entra no modelo**.
3. **O aceite do plano.** O **estado inicial** é o retrato de antes, e serve para calibrar as
   tarefas — tarefa escrita sem conhecer o que será trabalhado é adivinhação. O **estado final** é
   o desejo de quem encomendou, quantificável ou apenas qualificável. **O aceite é a confrontação
   dos dois.**
4. **A emenda versiona, não reescreve.** A versão nova nasce como bloco irmão, marcada pendente, e
   as duas coexistem até o marco seguinte, quando é aceita ou eliminada.

**Protege contra:** plano que não pode ser declarado bem-sucedido ou malsucedido contra critério
nenhum; e recorte de modelo que depende do gosto de quem escreve.

**O procedimento que ela instalou** — **o aceite de um plano é a confrontação do estado final real
contra o estado final especificado.** Residência: `GOVERNANCA.md` §3.2.

## `DOM-T8` — A gramática acompanha

**Contexto que a motivou:** a norma passou a prescrever quatro blocos onde a gramática ainda
descrevia três. Norma e gramática divergindo é o defeito que o estrato A existiu para impedir.

**O que é o artefato:** a subseção `### Modelo de domínio (seção do plano)` da skill
`diario-de-obras`, reescrita para a forma nova.

**Como funciona na prática:** a tabela passa a declarar as propriedades na tabela de objetos, o
`altera:` em cada operação, o bloco de estado inicial e final no lugar da antiga lista de mudanças,
o registro de versões, e o bloco irmão `## 1A` para a versão pendente. A lista de mudanças **sai**:
o que ela registrava passa a ser derivável do confronto entre duas versões.

**Protege contra:** gramática que descreve uma forma que a norma já substituiu.

## `DOM-T9` — O instrumento aprende propriedade, estado e versão

**Contexto que a motivou:** norma e gramática prescreviam a forma nova, e o instrumento conhecia 14
regras, todas da forma do estrato A.

**O que é o artefato:** `.claude/tools/modelo.py` (690 linhas), com o vocabulário passando de 14
para **20** violações e dois modos novos de exibição.

**Como funciona na prática:** as seis regras novas (`V15`..`V20`) cobrem exatamente o que entrou
na norma — objeto sem propriedade, operação sem `altera:`, propriedade sem estado declarado,
registro de versões malformado, versão pendente com número incoerente. O vocabulário completo, hoje
na árvore, é `V1`..`V20`:

```
$ grep -oE '\bV[0-9]{1,2}\b' .claude/tools/modelo.py | sort -u | wc -l
20
```

E o `check` sobre o plano que este documento valida sai limpo:

```
$ python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md
modelo: OK — 13 operações, 9 objetos, 21 propriedades, 18 tarefas, versão 1
EXIT=0
```

**Protege contra:** forma prescrita que nenhum programa consegue conferir.

**Ressalva medida, e é o `AE-20`.** As seis regras novas **não têm fixture**. As duas fixtures
inválidas do repositório emitem apenas `V1`..`V14` — as saídas coladas acima, nesta árvore, são a
prova: dez violações numa, quatro na outra, nenhuma acima de `V14`. `V15`..`V20` são exercitadas
por chamada direta à função `validar`, com objetos sintéticos, **sem passar pelo leitor de
markdown**. O próprio módulo declara isso, em `.claude/tools/modelo.py:21`: *"Os testes de `V15`..
`V20` chamam `validar`/`montar_drift` diretamente"*. As seis funcionam — a revisão reconstruiu o
caminho ponta a ponta —, mas **a suíte não prova que funcionam**.

## `DOM-T9a` — O modelador passa a falar a forma nova

**Contexto que a motivou:** a forma mudou por baixo do agente. O modelador continuava ensinando a
escrever a forma que acabara de sair de uso.

**O que é o artefato:** `.claude/agents/pantonic-model-designer.md`, com o ensinamento reescrito
para começar pela propriedade e o registro do ato migrado para o bloco `### 1.4 Registro de
versões`.

**Como funciona na prática:** o gatilho é o despacho do modelador. Ele lê a própria definição,
escreve a seção e **termina rodando `modelo.py check`** — o gate. A fronteira do gate foi o ponto
mais difícil dos dois planos e está descrita no `DOM-T9b` e no `DOM-T9c`, no Apêndice A.

**Protege contra:** agente que ensina a forma que a doutrina já substituiu.

---

# Estrato D — a forma se prova em si mesma

## `DOM-T10` — O primeiro plano do acervo escrito na forma nova

**Contexto que a motivou:** norma, gramática, instrumento e agente existiam, e **nenhum plano do
acervo estava escrito na forma que os quatro descreviam**. A forma nunca tinha sido exercida.

**O que é o artefato:** a seção `## 1. Modelo conceitual` do próprio `docs/plans/
P-0743-modelo-de-dominio.md` — 9 objetos, 21 propriedades, 13 operações, o estado inicial e final
de cada propriedade, e o registro de versões. Mais o campo `Operação do modelo` de cada um dos 18
cards.

**Como funciona na prática:** este card é a **primeira autoria real do modelador**. E foi desenhado
em dois atos com regra de precedência explícita, porque duas mãos diferentes escrevem duas regiões
do mesmo arquivo: **o modelador escreve a seção do modelo, e só ele**; o executor converte o campo
`Operação do modelo` de cada card, copiando o texto da operação e o contrato de cada objeto de que
ela precisa. As duas mãos não se cruzam.

A prova de que funcionou é a saída de `show` colada no topo deste documento, e o `check` saindo `0`
sobre o plano — o instrumento aceita o modelo que o modelador escreveu, e o modelo tem lastro em
todas as 18 tarefas.

O efeito no executor é o que justifica o desenho: **o contrato chega ao card**. Quem recebe a
tarefa `DOM-T1` lê, no próprio card, a operação que materializa e o contrato de cada objeto de que
precisa — sem abrir um plano de 5.452 linhas.

**Protege contra:** forma prescrita que nunca foi exercida e cujos defeitos só apareceriam no
primeiro uso real de quem não a escreveu.

## `DOM-T6` — A porta de entrada pública

**Contexto que a motivou:** quem chega ao repositório encontrava, no `README.md`, a descrição da
forma antiga.

**O que é o artefato:** a seção `### 8.1 O modelo de domínio do plano — o que o dono lê` do
`README.md`, mais a revisão do arquivo inteiro contra o estado final da árvore.

**Como funciona na prática:** é a última tarefa dos dois planos por desenho — só se descreve
publicamente a árvore quando ela para de mudar. A seção explica os quatro blocos do modelo, o
estágio derivado, o versionamento e o modelador, e fecha declarando a tolerância: *"Planos escritos
antes desta doutrina não são migrados: o instrumento os reconhece como forma anterior e não bloqueia
nada."*

**Protege contra:** documentação pública que descreve uma versão do sistema que não existe mais.

---

## O que vale além destes planos

Procedimentos que continuam verdadeiros mesmo sem o código que estes planos escreveram.

| regra | o que resolve | residência |
|---|---|---|
| **Estado é derivado, não escrito** | estado à mão diverge do real e ninguém percebe | `GOVERNANCA.md` §3.2, *"Estágio, não status"* |
| **Objeto é o que possui propriedade; operação altera propriedade** | torna o recorte do modelo decidível em vez de intuitivo | `GOVERNANCA.md` §3.2, *"Objeto, operação e propriedade"* |
| **O aceite é a confrontação do estado final real contra o especificado** | plano sem critério de sucesso | `GOVERNANCA.md` §3.2, *"Estado inicial, estado final e o aceite"* |
| **Emenda versiona, não reescreve** | o que a reescrita apaga não fica registrado | `GOVERNANCA.md` §3.2, *"Versão vigente, pendente e obsoleta"* |
| **Nenhum agente aciona outro agente** | cadeia de despacho sem dono e sem auditoria | `GOVERNANCA.md` §3.2, parágrafo final |
| **Quem detecta não conserta** | o papel que julga e edita não pode ser auditado | `.claude/agents/pantonic-reviewer.md`; `docs/RUBRICA_DE_REVISAO.md` §6 e §7 |
| **Residência única** | duas cópias do mesmo fato divergem no primeiro ajuste | `GOVERNANCA.md` §3.2 |
| **Forma anterior não se migra** | migração retroativa de plano fechado reescreve história | `GOVERNANCA.md` §3.2; exits `2` de `modelo.py` |

---

## Os ganhos, medidos

Todos re-derivados por comando em 2026-09-21.

| medida | antes | depois |
|---|---|---|
| Regras de forma verificadas por máquina | 9 (`V1`..`V9`, início do `P-0743`) | **20** (`V1`..`V20`) |
| Planos do acervo escritos na forma nova | 0 | **1** (`P-0743`) |
| Propriedades com estado inicial e final declarados | 0 (não havia o conceito) | **21** |
| Papéis que escrevem no modelo | 3 (planejador, revisor, consultor) | **1** (o modelador) |
| Agentes do kit | 9 | **10** |
| Estados escritos à mão no modelo de um plano | 20 estados paralelos | **0** — derivados |
| Suíte de testes | 249 *(registro da versão anterior deste documento, 2026-09-20)* | **262 passed** |
| Planos do acervo quebrados pela mudança | — | **0** — dos 24 planos, 1 sai `0`, 23 saem `2`, nenhum sai `1` |

**Duas medidas que envelhecem, e a razão da diferença.** O número de violações tem três valores,
todos corretos no momento em que foram tomados: **9** no início do `P-0743`, **14** ao fim do
`DOM-T3`, **20** hoje. A versão anterior deste documento registrou 14 — era o valor certo quando
foi escrita. O tamanho do acervo tem dois: o texto do modelo diz **22 planos**, medido em
2026-09-20, e a contagem de hoje dá **24**. Nenhum dos dois está errado; o acervo cresceu no
intervalo.

---

## Defeitos da execução, com estado

A execução produziu 25 achados (`AE-1`..`AE-25`), 10 escalonamentos (`ESC-1`..`ESC-10`) e uma
rodada de replanejamento. Eles formam **uma classe só**, e vale nomeá-la:

> **O aceite inalcançável por construção.** Um card declara "pronto quando o comando X imprimir
> Y" — e X não pode imprimir Y, por desenho, sem que quem escreveu o card tivesse como saber. O
> caso mais caro: o gate do modelador dizia *"só devolve com `check` exit `0`"*, o que é impossível
> na conversão de um plano para a forma nova — gravada a seção nova, o `check` acusa violação em
> toda tarefa que ainda cita a forma antiga, e essas linhas moram nos **cards**, que o modelador
> está proibido de tocar. Era um gate que só se fecha corrigindo o que não é seu.

| defeito | estado |
|---|---|
| Gate do modelador inalcançável na conversão | 🟢 **Fechado com guarda.** O gate passou a ler por fronteira medida: violação da seção é ato não concluído e ele mesmo corrige; violação que mora no card volta como saída literal, para a orquestração rotear |
| Literal de aceite que atravessa quebra de linha (`grep` nunca casa) | 🟢 **Fechado com guarda.** Literal de bloco se extrai linha a linha e se mede antes de publicar; proposição partida vira dois `grep`, um por linha |
| Cláusula de aceite com escopo de seção sem censo medido | 🟢 **Fechado com guarda.** Cláusula do tipo *"nenhuma linha de X descreve Y"* só entra num card se a verificação trouxer comando que percorra X inteiro, com o número de hoje e o esperado |
| Norma e gramática disputando a mesma residência | 🟢 **Fechado com guarda.** Residência é o arquivo da árvore; seção de plano é insumo literal de card, nunca residência depois da transcrição |
| Metade de mudança de papel publicada (uma ponta muda, a outra não) | 🟡 **Caso fechado, classe sem guarda.** Os casos medidos foram reparados card a card; nada impede que a próxima mudança de papel volte a ser publicada pela metade |
| Regra nova do instrumento nascendo sem fixture | 🔴 **Regra escrita, aplicação pendente.** O contrato do instrumento já diz *"cada regra nova nasce com fixture e teste pelo caminho do usuário"*, e `V15`..`V20` não o cumprem. Fecha pela pendência **P-1** |
| Rótulo de telemetria por card, não por ato | 🟡 **Caso fechado, classe sem guarda.** As duas linhas duplicadas de hoje foram corrigidas à mão; a regra de rótulo não existe. Fecha pela pendência **P-3** |
| Atribuição de autoria fabricada sobre tarefa nunca despachada | 🟡 **Caso fechado, classe sem guarda.** Os três laudos da janela desmentiram a evidência mecânica à mão. Fecha pela pendência **P-4** |

---

## Pendências abertas ao fim dos planos

| # | pendência | por que ficou aberta | o que a fecha | bloqueia algo? |
|---|---|---|---|---|
| **P-1** | **`AE-20` — `V15`..`V20` sem fixture.** As seis regras novas do instrumento não são exercitadas pelo caminho `leitor de markdown → check`; só por chamada direta à função de validação | As duas fixtures inválidas estão saturadas por `V1`..`V14`, e um teste afirma a **ordem de emissão** sobre elas: somar as seis quebra esse teste. O card só autorizava redistribuir entre as duas existentes | Uma **terceira** fixture inválida (`plano-invalido-3.md`) e um teste funcional por violação nova, via `modelo.py check --plano`, exit `1` e a substring no stderr. Escopo já fechado | **Não.** As seis funcionam — a revisão reconstruiu o caminho ponta a ponta. É furo de aferição, não de comportamento |
| **P-2** | **Premissa escrita.** Nada declara o que um modelo **assume**, nem o que fica explicitamente fora dele | Não foi endereçada por nenhuma das decisões dos três estágios; `grep -ci premissa` sobre `GOVERNANCA.md` §3.2 imprime `0` | Uma regra na norma que obrigue o modelo a declarar premissa e fronteira | **Não** |
| **P-3** | **`AE-25` — rótulo de telemetria por card, não por ato.** O hook registra pelo id do **card**; um card despachado em dois atos entra duas vezes na série | Fora dos alvos do card que a mediu | Emendar `GOVERNANCA.md` §4.2 fixando o rótulo **por ato** | **Não.** As duas linhas duplicadas de hoje foram removidas à mão. Os números estão certos; falta regra de rótulo |
| **P-3b** | **O mesmo hook não é confiável no disparo**, e a série não permite distinguir linha escrita por hook de linha apensada à mão — o hook grava `--fonte usage`, exatamente o mesmo valor que a orquestração grava (`.claude/tools/telemetria_hook.py:152`) | Sintoma irmão do `P-3`; já tem tíquete próprio (`TK-55`) | Um valor de `fonte` próprio do hook, que torne a diferença mecanicamente detectável | **Não**, mas mantém a série dependente de conferência a olho |
| **P-4** | **`TK-66` — o atribuidor de autoria fabrica evidência.** `review_evidence.py --atribuir` casa caminho contra os alvos de **qualquer** tarefa do plano sem olhar o `status` dela: rotulou quatorze arquivos como entrega de tarefas que nunca foram despachadas | Os três instrumentos de evidência estão sob invariante de não-edição nestes planos | Filtrar a atribuição por `status` da tarefa | **Não**, mas custa caro: os três laudos da janela tiveram de desmentir a evidência mecânica à mão |
| **P-5** | **`AE-24` — provas de proveniência sem residência.** Num card desenhado em dois atos, a saída literal do estado de entrada do segundo ato e o registro de quem despachou o modelador entre os dois chegaram ao revisor apenas na mensagem da orquestração | Nenhum alvo do card é residência de registro de execução | Fixar a RDO da tarefa como residência das provas de proveniência de todo card de dois atos | **Não.** O aceite do card foi satisfeito. Mas as provas **morrem com o laudo**, e são justamente as que discriminam qual mão escreveu cada região |
| **P-6** | **A forma é aferida; o conteúdo não.** As 20 regras são de **boa formação**, não de **correção**: garantem que o modelo é internamente coerente, não que descreve o plano com fidelidade | O confronto entre modelo e realidade é juízo, não regra mecânica | Parcialmente endereçada: o **aceite por confrontação de estados** dá âncora que antes não existia. O que falta é aferição mecânica da fidelidade | **Não** |
| **P-7** | **`MC-T5` do `P-0741` segue em `review`** | O `Pronto quando` dela exige veredito de quem encomendou, que não é ato de nenhum agente | O veredito sobre este documento | **Sim** — é o que mantém o `P-0741` em 7/8 |

**Duas lacunas que o documento anterior listava e que hoje estão fechadas**, por decisão registrada
no terceiro estágio:

- **Teste do que é objeto** — era circular (*"o que o plano manipula"*). **Fechado:** *objeto é o
  que possui propriedade; operação não possui propriedade*, publicado em `GOVERNANCA.md` §3.2, com
  a regra de decomposição para o caso ambíguo.
- **Régua de granularidade** — havia teto (40 operações) e nenhuma referência. **Fechado como
  método:** o recorte deixa de ser escolha de tamanho e passa a ser consequência das propriedades —
  identificam-se as propriedades, e objetos e operações caem por decomposição. O critério de
  entrada é o interesse de quem encomendou. *Ressalva honesta: o teto de 40 permanece e não há
  piso; o que mudou é que a granularidade agora se deriva em vez de se arbitrar.*

Uma terceira mudou de estado sem fechar: o **padrão de conteúdo publicado** morava como quatro
heurísticas dentro do corpo do agente. Hoje o **método** é doutrina pública em `GOVERNANCA.md`
§3.2, e o **ensinamento de autoria** tem residência declarada na definição do modelador. Segue sem
aferição mecânica — é a pendência **P-6**.

---

## Fora de escopo por desenho

Não são pendências: são decisões de não fazer.

| o que ficou de fora | por quê |
|---|---|
| **Os Marcos 4 e 5 não ganharam cards** | Pela régua vigente, marco é **detector de desvio**, não ponto de passagem: se a forma nova não for reconhecida como o resultado desejado, tudo que esses marcos escreveriam estaria errado. Escrever esses cards antes do veredito é gastar antes do detector |
| **Migrar os 23 planos que não estão na forma nova** | Estão fechados, e o que eles afirmam é verdadeiro sobre o que entregaram. O instrumento os reconhece e não bloqueia |
| **Editar `backlog.py`, `review_evidence.py` e `card_check.py`** | Invariante declarado dos dois planos |
| **A enumeração de agentes de `GOVERNANCA.md` §9** | Já estava defasada antes destes planos; corrigi-la aqui seria varredura fora do tema |

---

## Estado, honestamente

**Entregue.** O `P-0743` fechou **18 de 18 tarefas**, todas aprovadas. O `P-0741` está em **7 de
8** — a que falta é a que pede o veredito. Existe uma forma para descrever o que um plano entrega;
existem 20 regras que a verificam por máquina; existe um agente que a escreve e três que pararam de
escrever; existe um plano — este — cujo próprio modelo está na forma nova, com 9 objetos, 21
propriedades e 13 operações, e cujo `check` sai `0`. A suíte fecha em **262 testes**, e nenhum dos
planos anteriores quebrou.

**Oito pendências ficaram abertas** — sete independentes, mais a `P-3b`, que é sintoma irmão da
`P-3`. Nenhuma bloqueia o uso do que foi entregue. A mais importante
tecnicamente é a **P-1** (seis regras do instrumento funcionam e a suíte não prova que funcionam).
A mais cara no dia a dia é a **P-4** (a atribuição de autoria fabrica evidência, e alguém tem de
desmenti-la à mão a cada revisão). A **P-6** é a mais funda e a que menos tem solução à vista: a
forma é aferida, o conteúdo não.

**Três pendências têm efeito fora destes planos** — `P-3`/`P-3b` e `P-4` tocam a telemetria e a
evidência de revisão de **todo** plano do repositório, não só destes dois.

**Nada foi commitado.** A árvore carrega os dois planos inteiros: `git status --porcelain` conta
**76** entradas, e o último commit é `e0efcf6`.

---

# Apêndice A — os cards corretivos

Dez tarefas não avançaram o modelo: repararam a entrega de outra tarefa, e nasceram de defeito
medido durante a execução. Ficam aqui por regra de apresentação — matéria corretiva não desaparece
e não sobe ao corpo do relatório.

## `DOM-T3a` — O que o instrumento diz de si mesmo

**Contexto que a motivou:** o `DOM-T3` reescreveu o instrumento para a forma nova, e o texto em que
o instrumento **se descreve** — o docstring do módulo e o `--help` — continuou descrevendo a forma
anterior.

**O que é o artefato:** o docstring de `.claude/tools/modelo.py`, o texto de `--help`, e o preâmbulo
da skill `diario-de-obras` que **nomeia** a subseção da gramática.

**Como funciona na prática:** o gatilho é qualquer pessoa ou agente que rode `--help` ou abra o
módulo. A correção removeu todo resíduo da forma anterior, exceto os literais normativos de saída —
que precisam permanecer porque são exatamente as mensagens que o `check` imprime ao reconhecer um
plano antigo (`modelo: forma anterior — …`).

**Protege contra:** programa cuja apresentação descreve uma versão de si mesmo que não existe mais.

## `DOM-T3b` — A referência cruzada do docstring

**Contexto que a motivou:** o docstring apontava o invariante errado do plano — citava `I-3` onde a
frase explicava `I-1`.

**O que é o artefato:** o docstring de `.claude/tools/modelo.py`, alinhado linha a linha ao texto
de referência.

**Como funciona na prática:** sem gatilho próprio; é texto lido por quem abre o módulo. O defeito é
pequeno e a classe não é: **ponteiro que aponta para o lugar errado é pior que ponteiro ausente**,
porque quem o segue não percebe que errou.

**Protege contra:** referência cruzada que parece correta e leva ao texto errado.

## `DOM-T5a` — O passo que proibia o que outro passo mandava fazer

**Contexto que a motivou:** o `DOM-T5` alinhou os papéis à norma, e dentro da **mesma** definição
de conduta do revisor o passo 7 passou a proibir exatamente o que o passo `5a` mandava fazer — o
dossiê de pedido de ato não cabia mais na linha de retorno de onde a orquestração o lê.

**O que é o artefato:** o passo 7 de `.claude/agents/pantonic-reviewer.md`.

**Como funciona na prática:** o gatilho é o retorno do revisor ao fim de cada revisão. Corrigido, o
dossiê volta a caber na linha de retorno, que é de onde o bloco correspondente da skill
`scrum-master` o lê.

**Protege contra:** definição de conduta internamente contraditória, em que obedecer um passo é
violar outro.

## `DOM-T5b` — A cadeia inteira, de ponta a ponta

**Contexto que a motivou:** o `DOM-T5a` fechou a contradição **dentro** do revisor e a cadeia
continuou aberta **entre** o revisor e quem consome o retorno dele. A tabela que se declarava
exaustiva tinha doze elos; a medição encontrou um décimo terceiro.

**O que é o artefato:** cinco pontos que proíbem, contam ou transportam a linha de retorno do
revisor — a definição do papel, o despacho do passo 6, a leitura do passo 7 e o que o passo 7
entrega ao passo 8, na skill `scrum-master`.

**Como funciona na prática:** o gatilho é o mesmo retorno do revisor. A correção alinhou os cinco
pontos entre si, de modo que nenhum elo mande fazer o que outro elo proíbe.

**Protege contra:** correção que fecha o ponto medido e deixa a cadeia aberta um elo adiante. Este
card disparou o limite que manda tratar ponto novo da mesma família como replanejamento, e não como
mais um card corretivo — foi o que encerrou a primeira janela de execução.

## `DOM-T8a` — Os ponteiros que a forma nova deixou para trás

**Contexto que a motivou:** o `DOM-T8` removeu a última residência de um token de registro que
quatro regiões da árvore ainda mandavam o modelador devolver. Nenhum card as re-declarava: quatro
ponteiros órfãos, apontando para uma forma que saíra de uso.

**O que é o artefato:** quatro regiões — duas em `GOVERNANCA.md`, duas em
`.claude/agents/pantonic-planner.md` — reapontadas para `### 1.4 Registro de versões`, mais o
preâmbulo da skill.

**Como funciona na prática:** é texto normativo. A correção mudou **para onde** cada ponteiro
aponta, sem mudar o que papel nenhum faz — a distinção que permitiu fazê-la sem tocar a fronteira
dos papéis, que estava fora de escopo.

**Protege contra:** doutrina que manda registrar um ato numa forma que já foi removida.

## `DOM-T9b` — O gate que o modelador consegue fechar

**Contexto que a motivou:** o gate dizia *"só devolve com `check` exit `0`"*, e isso é inalcançável
na conversão de um plano para a forma nova. Gravada a seção nova, o `check` acusa violação em toda
tarefa que ainda cita a forma antiga — e essas linhas moram nos **cards**, que o modelador está
proibido de tocar. Era um gate que só se fecha corrigindo o que não é seu.

**O que é o artefato:** o bullet do gate em `.claude/agents/pantonic-model-designer.md`.

**Como funciona na prática:** o gatilho é o fim de todo ato do modelador. O gate passou a
distinguir **a violação que é dele** da **que mora no card**: a primeira é ato não concluído e ele
mesmo corrige; a segunda volta como saída literal, para a orquestração rotear a quem tem mão nos
cards.

**Protege contra:** condição de aceite que não pode ser satisfeita por quem tem de satisfazê-la.

## `DOM-T9c` — A fronteira do gate, por complemento

**Contexto que a motivou:** o `DOM-T9b` descreveu a fronteira nomeando **duas** famílias de
violação, e a fronteira tem **quatro**. Enumeração incompleta apresentada como completa.

**O que é o artefato:** o mesmo bullet, reescrito para definir a fronteira **por complemento** em
vez de por enumeração.

**Como funciona na prática:** em vez de listar quais violações são do modelador — lista que
envelhece a cada regra nova —, o texto define o que é violação da seção e trata o resto como
complemento. `V6`, `V7`, `V15` e `V17`, que são das tabelas que o modelador escreve, caem no ramo
do ato não concluído sem precisar ser nomeadas.

**Protege contra:** enumeração que se apresenta como exaustiva e envelhece na próxima regra. Este
card precisou de uma rodada de replanejamento: a primeira versão dele repetiu o defeito do aceite
inalcançável, com um literal de verificação que atravessava uma quebra de linha e que nenhum `grep`
conseguiria casar.

## `MC-T2a` e `MC-T2b` — O campo sem leitor sai do instrumento

**Contexto que a motivou:** o instrumento declarava e preenchia um campo que nenhum código lia.

**O que é o artefato:** `.claude/tools/modelo.py` — primeiro o campo, depois a cadeia inteira de
símbolos que ficaram sem leitor por consequência da remoção.

**Como funciona na prática:** a segunda tarefa existe porque a primeira não bastou: remover o campo
deixou órfãos os símbolos que só existiam para alimentá-lo. O aceite das duas é o mesmo — a saída
dos dois verbos continua **idêntica**, e a suíte não perde teste.

**Protege contra:** estrutura de dados que carrega campo que ninguém consome, e limpeza parcial que
deixa a cauda para trás.

## `MC-T4a` — O gate que criava o vermelho que devia reparar

**Contexto que a motivou:** o gate do modelo no fechamento de tarefa rodava **depois** da
materialização do estado. Como o andamento é derivado das tarefas, o gate media um estado que ele
mesmo acabara de produzir — e acusava uma violação que a própria ordem de execução criara.

**O que é o artefato:** o passo de fechamento da skill `.claude/skills/scrum-master/SKILL.md`.

**Como funciona na prática:** o gate passou a rodar **antes** da materialização, e exit `1` segura
a tarefa em `review` em vez de deixá-la fechar. As duas frases do mesmo arquivo que contam quantos
gates existem passaram a contar três.

**Protege contra:** verificação cuja própria ordem de execução fabrica o defeito que ela reporta.

---

# Apêndice B — onde está o registro

| o quê | onde |
|---|---|
| Os dois planos, com os cards e os achados da execução | `docs/plans/P-0743-modelo-de-dominio.md` (§9 tarefas, `## Achados da execução`); `docs/plans/P-0741-modelo-conceitual.md` |
| O registro de cada tarefa entregue | `docs/RDO/P-0743-*.md` (18 arquivos) e `docs/RDO/P-0741-*.md` (7) |
| O consumo medido | `docs/telemetria.tsv` — 23 linhas em 2026-09-21 (2.659,0k tokens, 535 usos de ferramenta, 1,75 h) e 26 linhas do `P-0743` em 2026-09-20 (2.224,8k, 517, 1,96 h) |
| A fila e o estado dos planos | `docs/DIARIO_DE_OBRAS.md` |
| A norma vigente | `GOVERNANCA.md` §3.2 |
| A gramática vigente | `.claude/skills/diario-de-obras/SKILL.md`, *Modelo de domínio (seção do plano)* |
