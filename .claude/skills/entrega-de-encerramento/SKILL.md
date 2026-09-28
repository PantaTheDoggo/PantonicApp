---
name: entrega-de-encerramento
description: Produz o documento de encerramento de um plano Pantonic* — o modelo "as-is" que mapeia cada tarefa ao contexto que a motivou, ao artefato concreto que ela criou, a um exemplo real de funcionamento e ao que ela protege, mais o estado honesto do que ficou aberto. É o artefato pelo qual o dono valida o plano. Usar ao fechar qualquer plano, antes de pedir o veredito.
---

# entrega-de-encerramento — o documento pelo qual o dono valida um plano

**Todo plano entregue gera este documento.** Ele é o artefato de validação: o dono não dá veredito
sobre um plano lendo o plano — dá lendo o modelo **as-is** das operações que o plano deixou.

**Residência:** `docs/plans/P-<n>-<slug>/operacoes.md`, na pasta do plano. Plano legado: `docs/OPERACOES_AS_IS.md` quando o plano é o primeiro a produzir um; a partir do
segundo, `docs/OPERACOES_AS_IS_<PLANO>.md`, ou uma seção nova no documento existente quando o plano
altera operações já descritas nele. A decisão é do `scrum-master` no fechamento, e o critério é um
só: **um leitor que abra o documento tem de encontrar o estado corrente, não a união de estados
históricos.**

**Quando rodar:** depois da última tarefa entregar e antes de pedir o veredito. O documento é
insumo do veredito, não consequência dele.

---

## A regra que governa tudo neste documento

> **Quem lê não tem o plano na cabeça.**

O leitor não sabe o que é um "balde", um "corpus", uma "célula congelada". Ele não acompanhou a
execução. Todo termo interno ou é **definido no texto** ou **não se usa**. Toda afirmação sobre
comportamento vem com **um exemplo real**, copiado de uma saída que se rodou — nunca inventado e
nunca parafraseado de memória.

Três testes que um parágrafo tem de passar:

1. **Teste do referente.** Cada substantivo técnico tem antecedente no próprio documento? *"Só o
   balde sem atribuição pesa"* reprova: nem "balde" nem "pesa" foram definidos.
2. **Teste do artefato.** O leitor sabe **o que a coisa é** — arquivo, função, seção de skill,
   hook, regra de conduta? *"O confronto de escopo classifica em quatro baldes"* reprova: não diz
   se é código, doutrina ou hábito.
3. **Teste do gatilho.** O leitor sabe **o que faz aquilo rodar**? Um comando que alguém digita? Um
   evento do harness? Um passo de outro procedimento?

Se um parágrafo reprova em qualquer um, reescreve-se.

---

## Estrutura do documento

### Abertura — por que o plano existiu

Três blocos, nesta ordem:

- **O problema**, com **os números que o motivaram**. Não "o processo era ineficiente", e sim *"o
  primeiro turno consumia 60.472 tokens, 30,2% da janela, antes de qualquer trabalho"*.
- **A solução, em uma frase** — o que mudou de natureza. *"O que era leitura vira comando; o que era
  heurística vira código."*
- **Vocabulário mínimo**, em tabela. Todo termo que o documento vai usar e que o leitor não tem
  como saber. Se a tabela passar de ~8 linhas, o documento está usando jargão demais.

### O arco — os estratos

As tarefas de um plano raramente são N assuntos independentes. Agrupe-as em **camadas**, cada uma
respondendo a uma pergunta, e diga por que cada camada é inútil sem a anterior. Uma tabela
`estrato | pergunta que responde | tarefas`.

Tarefas que não pertencem a estrato nenhum (rodadas de replanejamento, reagrupamentos) ficam
nomeadas **fora** da tabela, com a razão.

### Uma seção por tarefa — o núcleo do documento

**Toda tarefa viva do plano tem seção própria**, com estes quatro blocos, nesta ordem e com estes
nomes:

```markdown
## `<ID>` — <título curto, em linguagem de quem lê, não o título do card>

**Contexto que a motivou:** o que estava quebrado ou faltando **antes**. Com número quando houver.

**O que é o artefato:** a coisa concreta. Arquivo e função (`confrontar_escopo` em
`review_evidence.py`), seção de skill, hook, parâmetro de comando, regra de conduta.

**Como funciona na prática:** o gatilho, o processamento e a saída — com **exemplo real rodado**.

**Protege contra:** a classe de defeito que deixa de ser possível.
```

Para tarefa cujo funcionamento tem passos, use a forma numerada: **o que dispara** → **a entrada**
→ **o processamento** → **a saída**. Foi assim que a descrição mais difícil do documento de
referência ficou legível.

Quando a tarefa instalou um procedimento que vale além dela, acrescente um quinto bloco
**"O procedimento que ela instalou"**, com o nome da regra em negrito.

**Tarefas `cancelled` por absorção** não ganham seção: são nomeadas no arco, com o ponteiro de quem
as absorveu.

### O que vale além deste plano

Tabela `regra | o que resolve | residência`. São os procedimentos que continuam verdadeiros mesmo
sem o código que o plano escreveu. **Aponte a residência normativa, não transcreva a regra** — duas
residências do mesmo fato divergem no primeiro ajuste.

### Os ganhos, medidos

Tabela `medida | antes | depois`. **Só número medido.** Nada de "melhorou significativamente".
Medida que não se conseguiu tomar não entra nesta tabela: entra nas pendências, declarada.

### O padrão que a execução revelou

Se os defeitos da execução formam uma classe, nomeie a classe. Esta seção é o que transforma uma
execução em aprendizado — mas **ela é a que mais facilmente fica ambígua**, e por isso tem regra
própria na seção seguinte.

### Pendências abertas ao fim do plano

Tabela com, no mínimo: `pendência | por que ficou aberta | o que a fecha | bloqueia algo?`.

Feche com um **resumo honesto do estado**: o que o plano entregou, quantas pendências ficaram, e
quais delas têm efeito **fora** do projeto.

---

## A regra do estado — a que mais falha

Um leitor que chega às seções finais precisa saber, **de cada item**, se aquilo **já está resolvido
ou ainda está pendente**. Listar defeitos sem dizer o estado deles faz o documento parecer um
inventário de problemas abertos quando metade já foi consertada — e o contrário também: faz dívida
real passar por lição aprendida.

**Nunca liste um defeito sem o estado dele.** E o estado não é binário: corrigir **o caso** não é
o mesmo que impedir **a classe**. Use três:

| estado | significa |
|---|---|
| 🟢 **Fechado com guarda** | o defeito não existe mais **e** há teste ou verificador que barra a volta |
| 🟡 **Caso fechado, classe sem guarda** | este caso foi corrigido; **nada impede outro igual** |
| 🔴 **Regra escrita, aplicação pendente** | sabe-se o que fazer, e ainda não foi feito em toda parte |

A distinção entre 🟢 e 🟡 é a informação mais valiosa do documento inteiro, porque é ela que diz
onde o processo ainda depende de alguém lembrar.

**Separe fisicamente as duas seções finais:** *defeitos da execução, com estado* é uma coisa;
*pendências abertas* é outra. Se um item aparece nas duas, a coluna "o que fecha" da primeira
aponta para a pendência da segunda, pelo número.

---

## Procedimento

1. **Levante todas as tarefas do plano**, inclusive as `cancelled`, e confirme a contagem contra o
   arquivo — não contra a memória. A contagem errada na abertura desmoraliza o documento inteiro.
2. **Leia o código dos artefatos que vai descrever.** Descrição de comportamento escrita de memória
   erra: numa redação de referência, o autor contou "quatro categorias" onde o código tinha cinco.
3. **Colha saídas reais.** Rode os comandos e copie a saída. Onde a saída já existe no registro da
   execução, cite-a de lá.
4. **Escreva as seções por tarefa** sobre o esqueleto que `python .claude/tools/encerrar.py operacoes --plano <plano>` gera (uma seção por tarefa viva, com os quatro blocos vazios), aplicando os três testes da regra de leitura.
5. **Classifique cada defeito e cada pendência** pelos três estados.
6. **Verifique a cobertura e a estrutura por comando**, não por leitura — todo card do plano citado
   no documento, toda tarefa viva com a sua seção e toda seção de tarefa com os quatro blocos
   obrigatórios: `python .claude/tools/encerrar.py operacoes --plano <plano> --checar`, exit `0`
   com as linhas `nao citados: nenhum`, `sem seção: nenhum` e `sem os quatro blocos: nenhum`.
7. **Apresente ao dono** e colha o veredito.

---

## Armadilhas medidas

- **A verificação de cobertura mede presença, não compreensibilidade.** Um documento pode sair
  23/23 cards citados e ser ilegível. A cobertura é piso, nunca aceite.
- **Jargão do plano é invisível para quem o escreveu.** O autor conviveu com "balde" e "corpus" por
  uma execução inteira e não percebe que são opacos. Na revisão, leia procurando substantivos sem
  antecedente.
- **Número de memória erra.** Todo número no documento é re-derivado no ato, e datado quando puder
  envelhecer. Duas medidas do mesmo fato em momentos diferentes **ambas corretas** devem aparecer
  com a razão da diferença, não ser reconciliadas à força.
- **Medida que não se pôde tomar não se estima.** Declara-se a lacuna, sem valor. Número inventado
  num documento de decisão é publicado como fato.
- **O título do card não serve de título de seção.** Ele foi escrito para quem executa; o documento
  é para quem valida.

---

## Fronteira

Este documento descreve **operações**, não história. Não narra a execução, não cita interlocutor e
não reproduz a sequência de escalonamentos — a régua da `redacao-doc` vale aqui por inteiro. O
registro da execução mora no plano (`## Achados da execução`) e nos RDOs; este documento aponta
para eles quando precisa.

Ele também **não é doutrina**: não cria regra. Onde um procedimento virou norma, a norma tem
residência própria e este documento a referencia.
