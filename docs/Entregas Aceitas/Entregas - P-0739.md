# Entregas — `P-0739`

**O modelo as-is das operações que o plano deixou**, tarefa a tarefa, com o estado de cada
pendência. É o artefato pelo qual o plano foi validado.

## Por que este plano existiu

**O problema:** decidir "qual é a próxima tarefa" era um ato de leitura. Um agente abria uma sessão
nova, carregava o diário de obras inteiro, o inbox de planos e os planos vivos — **77.457
caracteres** — e aplicava de cabeça uma heurística escrita em prosa numa skill. Três consequências
medidas:

1. **custo** — o primeiro turno de uma janela consumia 60.472 tokens, 30,2% de uma janela de 200k,
   ocupados antes de qualquer trabalho;
2. **divergência** — dois agentes liam os mesmos documentos e escolhiam tarefas diferentes, porque
   a heurística era interpretável;
3. **estado inconsistente** — o status de uma tarefa vivia em até cinco lugares (linha do card,
   célula do índice, contador do pai, bloco de fila, prosa de fechamento), atualizados à mão e um
   de cada vez.

**A solução:** um programa — `.claude/tools/backlog.py` — passa a **decidir, escrever e conferir**.
O que era leitura vira comando; o que era heurística vira código; o que era atualização manual vira
uma escrita atômica.

**Este documento** mapeia as 23 tarefas do plano ao que cada uma construiu, com um exemplo real de
funcionamento. Descreve o **estado corrente**, não a história. Onde um procedimento tem residência
normativa (`DB-<n>` do plano, `GOVERNANCA.md`, `RUBRICA_DE_REVISAO.md`), este documento aponta em
vez de transcrever.

**Vocabulário mínimo**, para o texto não exigir o plano na cabeça:

| termo | o que é |
|---|---|
| **índice** | a tabela no topo de `docs/DIARIO_DE_OBRAS.md`, com uma linha por plano e por tíquete |
| **residência** | o lugar onde um fato é escrito **uma vez**; todo o resto é projeção dele |
| **projeção** | cópia derivada de um fato, escrita pelo programa (célula do índice, contador `<done>/<total>`, bloco de fila) |
| **corpus** | o conjunto de documentos que o programa considera **vivos** e, portanto, sujeitos a conferência |
| **dossiê** | o texto que um agente recebe para executar uma tarefa, sem precisar ler mais nada |

---

## O arco: quatro estratos

As 23 tarefas (18 vivas, 5 `cancelled` por absorção) não são 23 assuntos. São quatro camadas
empilhadas, cada uma inútil sem a anterior:

| estrato | pergunta que responde | tarefas |
|---|---|---|
| **A** | como um documento fica legível por máquina? | `BKL-T1` |
| **B** | como o programa **lê** e decide? | `BKL-T2`, `T2a`–`T2e`, `T3`, `T3a`, `T3b` |
| **C** | como o programa **escreve** sem destruir nada? | `BKL-T4`, `T10`, `T10b`, `T10a` |
| **D** | como isso chega ao agente sem ele pedir? | `BKL-T11`, `T11a`, `T12` |

A **`BKL-T9a`** fica fora dos estratos: reagrupou cinco cards atômicos em três módulos. Os cinco
absorvidos (`BKL-T5`+`BKL-T6` → `BKL-T10`; `BKL-T7`+`BKL-T8` → `BKL-T11`; `BKL-T9` → `BKL-T12`)
seguem íntegros no plano como fonte que os módulos citam.

---

# Estrato A — tornar o documento legível por máquina

## `BKL-T1` — a gramática publicada onde quem escreve a lê

**Contexto que a motivou:** o programa ia passar a ler documentos que **humanos e agentes escrevem
à mão**. Sem uma regra publicada de como escrevê-los, cada autor inventaria um formato e o parser
quebraria.

**O que é o artefato:** uma seção — `## Gramática legível por máquina` — dentro de
`.claude/skills/diario-de-obras/SKILL.md`, a skill que qualquer agente carrega antes de mexer no
diário.

**Como funciona na prática:** um agente vai registrar um plano novo. A skill que ele carrega já traz
a gramática: cabeçalho de tarefa como `### <ID> — <título> [<modelo> · classe <classe>]`, estado
como `- **Status:** \`<estado>\` · <data>`. Ele escreve nesse formato porque é o que a skill manda,
e o parser lê sem adivinhar.

**Decisão deliberada que importa três estratos adiante:** a skill transcreve §2.1–§2.4 e §2.7 do
plano — a gramática dos **documentos** — e **exclui** §2.5 e §2.6, que descrevem o **comportamento**
do verbo `next`. A razão: ninguém executa a ordem de seleção à mão, então publicá-la na skill
criaria um texto que envelhece no primeiro ajuste do código.

**Protege contra:** documento que o programa não lê; e contra duas versões da mesma regra — uma na
skill, outra no plano — divergindo com o tempo.

---

# Estrato B — o programa lê e decide

## `BKL-T2` — o núcleo somente-leitura: `check` e `show`

**Contexto que a motivou:** antes de escrever qualquer coisa, era preciso provar que o programa
**entende** os documentos, e ter um jeito de descobrir onde eles estavam malformados.

**O que é o artefato:** o núcleo de `.claude/tools/backlog.py` — carrega o índice, os planos vivos e
o diário, monta o grafo item→tarefas, e expõe dois verbos de leitura: `check` e `show`.

**Como funciona `check`, com saída real desta execução:**

```
$ python .claude/tools/backlog.py check
C-5 docs/DIARIO_DE_OBRAS.md:57 — P-0735-RPC: índice 'done' diverge do campo 'ready'
C-5 docs/DIARIO_DE_OBRAS.md:59 — P-0737-AUT: índice 'superseded' diverge do campo 'ready'
```

Cada linha é uma **violação com endereço**: código, arquivo, linha, explicação. O vocabulário é
fechado em nove códigos:

| código | o que acusa |
|---|---|
| `C-1` | cabeçalho de tarefa fora da gramática |
| `C-2` | item sem linha `- **Status:**` |
| `C-3` | status na célula do índice fora do vocabulário permitido |
| `C-4` | célula do índice com prosa, em vez de token puro |
| `C-5` | célula do índice **diverge** do campo `Status` do item |
| `C-7` | plano vivo sem declarar o prefixo das tarefas dele |
| `C-8` | plano vivo sem `Status` |
| `C-9` | item sem residência — não está em plano vivo nem no diário |

Sem violação, sai `check: OK — nenhuma violação.` e `exit 0`.

**Como funciona `show`:** `python .claude/tools/backlog.py show BKL-T12` imprime o card inteiro —
cabeçalho, status, objetivo, passos, verificação — como está no plano. É o dossiê que um executor
recebe.

**Protege contra:** divergência silenciosa entre documento e projeção. "O índice está certo?" era
pergunta de inspeção; virou comando com resposta binária.

---

## `BKL-T2a` — o parser passa a aceitar identificador com prefixo

**Contexto que a motivou:** as ferramentas de revisão (`review_evidence.py`, `rdo.py`) reconheciam
identificadores simples como `T9a`. Mas os planos vivos usam prefixo — `BKL-T2`, `AUT-T4`,
`CTX-T1d` — e alguns cabeçalhos trazem ` + dono`. Resultado: **nenhuma tarefa dos três planos vivos
gerava dossiê de evidência.** A revisão estava travada.

**O que é o artefato:** a expressão regular de cabeçalho em `.claude/tools/rdo.py:85`, que passa a
aceitar `<PREFIXO>-T<n>[letra]` e o sufixo ` + dono`.

**Como funciona na prática:** o `scrum-master` roda
`review_evidence.py --plano docs/plans/P-0739-... --tarefa BKL-T10 --desde <sha>`. O parser localiza
`### BKL-T10 — … [Sonnet · esforço high · classe implementacao]`, extrai os campos e monta o
dossiê. Antes desta tarefa, saía `exit 1` — *tarefa não encontrada*.

**Protege contra:** ferramenta de revisão que só funciona no plano que a originou.

---

## `BKL-T2b` — a lista de arquivos-alvo é lida por gramática de caminho

**Contexto que a motivou:** o campo `Arquivos-alvo` de um card é uma lista de bullets escrita por
humano, e dentro dela aparece de tudo: caminhos de verdade, trechos de expressão regular entre
crases, nomes de seção. O parser pegava qualquer literal entre crases e tratava como arquivo.

**O que é o artefato:** a função `extrair_arquivos_alvo` em `review_evidence.py`, com uma gramática
de caminho que aceita `CHANGELOG.md` e `docs/plans/` e **recusa** coisas como
`_ID_HEADER_RE = re.compile(...)`.

**Como funciona na prática:** ao montar o dossiê, o script separa a lista em dois conjuntos e
**imprime os dois** — os caminhos aceitos, e numa seção `## Escopo` os literais descartados. O
reviewer vê o que o instrumento ignorou.

**Protege contra:** silêncio. Um parser que descarta sem avisar faz o reviewer confiar numa lista
incompleta sem ter como saber.

---

## `BKL-T2c` — o dossiê classifica cada arquivo tocado, e só uma categoria pesa

**Contexto que a motivou:** a revisão precisa responder *"a entrega ficou dentro do escopo?"*. O
método ingênuo compara os arquivos alterados desde um commit com os `Arquivos-alvo` do card. Mas
numa janela que roda várias tarefas **sem commitar**, os arquivos das tarefas anteriores também
aparecem: o reviewer via **33 arquivos alterados para uma entrega de 2**, e teve de provar por
datação de arquivo que a tarefa não os tocara.

**O que é o artefato:** a função `confrontar_escopo` em `.claude/tools/review_evidence.py`.

**Como funciona, passo a passo:**

1. **O que dispara:** o `scrum-master`, antes de despachar o reviewer, roda
   `review_evidence.py --plano <plano> --tarefa <ID> --desde <sha capturado no despacho>`.
2. **A entrada:** a lista de arquivos que o `git` diz terem mudado desde aquele SHA, mais a lista
   de `Arquivos-alvo` do card.
3. **O processamento:** cada arquivo tocado cai em **uma** de cinco categorias, testadas nesta
   ordem — a primeira que casa vence:

   | ordem | categoria | exemplo real desta execução |
   |---|---|---|
   | 1ª | coberto pelos alvos do card | `.claude/tools/backlog.py`, na revisão da `BKL-T10` |
   | 2ª | alvo de **outra tarefa do mesmo plano** | `tests/test_backlog.py`, alvo da `BKL-T10b`, aparecendo na revisão da `BKL-T10a` |
   | 3ª | registro da orquestração | `docs/telemetria.tsv`, `docs/RDO/**` |
   | 4ª | ato do dono fora do ciclo | arquivos sob `.claude/agents/` (categoria acrescentada pela `BKL-T2e`) |
   | 5ª | **fora dos alvos, sem atribuição** | qualquer outro |

4. **A saída:** uma seção `## Escopo` no dossiê, listando cada categoria nominalmente, e um veredito
   mecânico em que **só a 5ª categoria decide**: vazia → `conforme`; não vazia → veredito **aberto**,
   para o reviewer julgar.

**Por que só a 5ª pesa:** as quatro primeiras têm explicação conhecida — é alvo do card, é de outra
tarefa, é registro, é ato do dono. Só a quinta significa *"alguém mexeu em algo que ninguém pediu"*,
que é a única pergunta que o confronto de escopo existe para fazer.

**Protege contra:** entrega boa rebaixada por arquivo alheio; e contra o reviewer ter de produzir à
mão a prova que o dossiê existe para dar.

---

## `BKL-T2d` — achado de processo sai por canal próprio

**Contexto que a motivou:** um reviewer encontra dois tipos de coisa — defeito **da entrega** e
defeito **do método** (card mal escrito, instrumento com lacuna, rubrica ambígua). Só havia um
canal: o veredito. Registrar um defeito de método rebaixava a nota de uma entrega que estava boa.

**O que é o artefato:** o parâmetro `--achado-processo <alvo> "<uma linha>"` no gerador de laudo
(`rdo.py laudo`), que grava uma seção `## Achado de processo` com o alvo declarado — dossiê,
instrumento ou rubrica. Ele **não** altera percentual, veredito, dimensão bloqueante nem
recomendação.

**Como funciona na prática:** nesta execução a `BKL-T3b` fechou **aprovada 100%**, sem nenhuma
dimensão rebaixada, **e** deixou um achado de processo sobre o dossiê de evidência. Esse achado
virou a tarefa `BKL-T2c`, descrita acima.

**Protege contra:** a escolha falsa entre calar o defeito de método ou punir quem entregou bem.

---

## `BKL-T2e` — a categoria "ato do dono"

**Contexto que a motivou:** o dono altera um arquivo de configuração de agente no meio de uma
execução. Esse arquivo aparece como tocado, cai na categoria *"fora dos alvos sem atribuição"*, e a
entrega é marcada como fora de escopo — por uma alteração que o executor não fez.

**O que é o artefato:** a função `_eh_ato_do_dono` em `review_evidence.py`, que reconhece caminhos
sob `.claude/agents/` e os desvia para a quinta categoria da tabela acima.

**Como funciona na prática:** o arquivo é **impresso nominalmente** no dossiê, sob `ato do dono`, e
**não pesa** no veredito mecânico. O reviewer vê que mudou, e de quem foi.

**Protege contra:** penalizar a entrega por ato de quem está fora do ciclo — sem esconder que o ato
existiu.

---

## `BKL-T3` — `next`: a seleção vira código

**Contexto que a motivou:** esta é a tarefa central do plano. A ordem de escolha da próxima tarefa
vivia em prosa numa skill, e era aplicada de cabeça por quem lesse.

**O que é o artefato:** o verbo `next` em `.claude/tools/backlog.py`, implementando a ordem total de
seleção (§2.5) e a forma fixa de saída (§2.6).

**Como funciona, com saída real desta execução:**

```
$ python .claude/tools/backlog.py next
=== PRÓXIMA TAREFA: BKL-T11 — O hook, o ponto de carga e as skills que invocam o instrumento [Sonnet · classe implementacao]
plano: P-0739 — O pickup vira instrumento … (15/17) · residência: docs/plans/P-0739-backlog-instrumento.md:1-4983
antecessora: BKL-T10a (done; notas em docs/plans/P-0739-backlog-instrumento.md:2623-2624)
--- dossiê (verbatim, teto DB-7) ---
### BKL-T11 — O hook, o ponto de carga e as skills que invocam o instrumento […]
- **Status:** `ready` · 2026-09-19 …
```

Ele devolve **a tarefa e o dossiê dela**, mais a antecessora e onde estão as notas de execução
daquela. Três códigos de saída: `0` escolheu, `2` não há nada elegível, `3` o dado impede a escolha.

**Protege contra:** dois agentes chegarem a tarefas diferentes lendo os mesmos documentos.

---

## `BKL-T3a` — a recusa nomeia a condição

**Contexto que a motivou:** `next` podia recusar-se a escolher por três razões diferentes e saía
apenas com `exit 3`. Quem recebia tinha de investigar qual dado faltava.

**O que é o artefato:** as três condições de `exit 3` em `backlog.py`, cada uma imprimindo a
substring que a nomeia; e o contador do rodapé, que passa a contar pela gramática.

**Como funciona na prática:** em vez de um código mudo, sai a condição:

- **`E-1`** — há duas ou mais tarefas `in-progress` no mesmo pai;
- **`E-2`** — falta a linha `- **Status:**` do item **ou do pai dele**;
- **`E-3`** — falta a linha de índice.

O que se faz é **corrigir o dado nomeado**, sem procurar.

**Protege contra:** recusa que obriga a uma investigação para descobrir o que ela quis dizer.

---

## `BKL-T3b` — a condição de erro cobre o sujeito inteiro

**Contexto que a motivou:** a condição `E-2` recusava candidato sem linha de status, mas **não** o
pai do candidato. Faltando o dado do pai, `next` não recusava — elegia por heurística, que é
exatamente o que o plano veio eliminar.

**O que é o artefato:** a condição `E-2` em `backlog.py`, estendida ao pai; e o contador
`fila de memória:`, que deixa de contar a régua markdown `---` como se fosse item.

**Como funciona na prática:** com o pai sem linha de status, `next` passa a sair `exit 3` nomeando
`E-2`, em vez de escolher assim mesmo.

**Protege contra:** meia condição de erro — pior que nenhuma, porque passa a impressão de estar
coberta.

---

# Estrato C — o programa escreve sem destruir nada

## `BKL-T4` — uma transição escreve todas as projeções num ato

**Contexto que a motivou:** mudar o status de uma tarefa exigia editar até cinco lugares à mão. Na
prática alguns eram esquecidos, e o índice envelhecia em silêncio.

**O que é o artefato:** os verbos `status`, `start` e `diretiva` em `backlog.py`, mais a máquina de
transições (§2.7).

**Como funciona, com saída real desta execução:**

```
$ python .claude/tools/backlog.py start BKL-T11
start: BKL-T11 → in-progress. arquivos tocados: docs/DIARIO_DE_OBRAS.md, docs/plans/P-0739-backlog-instrumento.md
```

Num único ato ele escreve: a linha `Status` do card · a célula do índice · o contador
`<done>/<total>` do pai · o bloco de fila. E **lista os arquivos que tocou**, para conferência.

A máquina de transições recusa o que não está na tabela. Medido nesta execução:

```
$ python .claude/tools/backlog.py status BKL-T10a done
transição fora da tabela de §2.7: in-progress → done para BKL-T10a
```

O caminho legal é `in-progress → review → done`: o programa **obriga** o ciclo que o processo
descreve, em vez de confiar que quem opera se lembre dele.

**Protege contra:** a classe de defeito *"linha de campo atualizada, índice esquecido"*.

---

## `BKL-T9a` — reagrupar cinco cards em três módulos

**Contexto que a motivou:** cinco cards restantes tinham sido escritos sob uma régua antiga, de
"tarefa atômica". Executá-los um a um reproduziria defeitos já medidos. A decisão de reagrupá-los já
estava tomada — faltava escrevê-la em forma de card executável a frio.

**O que é o artefato:** três cards novos no plano (`BKL-T10`, `BKL-T11`, `BKL-T12`) e os cinco
antigos movidos para `cancelled`, com o corpo preservado como fonte.

**Como funciona na prática:** um executor pede a próxima tarefa e recebe `BKL-T10` — um módulo com
objetivo único, 18 passos e 11 itens de verificação —, em vez de dois cards atômicos que só fazem
sentido juntos. Os cinco antigos continuam legíveis no plano, cada um com a linha
`- **Absorvida por:** <ID do módulo>`, então quem quiser a matéria original a encontra pelo
ponteiro. Verificação real: `review_evidence.py --tarefa BKL-T10 --desde HEAD` saía **exit 1**
(tarefa inexistente) antes da transcrição, e **exit 0** depois.

**O procedimento que ela instalou — separar decisão de transcrição:** decidir carrega o contexto do
momento e se escreve **agora**; transcrever mede a árvore e se escreve **quando a árvore para**. A
razão é concreta: dois caminhos citados pelos cards antigos
(`.claude/skills/proximo-passo/SKILL.md` e `handover/SKILL.md`) tinham sido **removidos da árvore**
no intervalo. Transcritos sem re-medir, virariam cards que bloqueiam no despacho por apontar para
arquivo inexistente.

**Protege contra:** card que herda alvo morto; e contra quem transcreve ter de re-decidir.

---

## `BKL-T10` — o programa passa a saber o que é "vivo", e o diário é migrado

**Contexto que a motivou:** `check` acusava **309 violações**. Parecia dívida acumulada de anos. Não
era: o programa decidia se um plano estava vivo lendo o campo `Status` **do arquivo do plano** —
campo que a doutrina **proíbe** acrescentar a plano fechado. Sem o campo, todo plano fechado parecia
vivo, e o lint varria **20 planos** onde a norma falava de 3.

**O que é o artefato:** duas regras no programa, mais a migração do diário real.

1. **Corpus derivado do índice** (`DB-43`): "vivo" passa a ser lido da **célula do índice**, não do
   arquivo. Plano marcado terminal no índice sai do corpus.
2. **Célula congelada** (`DB-46`): se o status do item é terminal (`done`, `cancelled`), a narrativa
   de fechamento **pertence** àquela célula e não é violação. Se é vivo, a célula leva token puro e
   a narrativa vai para a seção do item.

**Como funciona na prática:** a regra da célula é um teste de uma linha — *o status é terminal?* —
que qualquer executor aplica sem julgar caso a caso. Antes, a alternativa considerada era uma lista
nominal de exceções, que resolveria os casos de hoje e reabriria o problema no próximo plano
fechado com prosa.

**Resultado medido:** `check` de **309 violações** para **0**, `exit 0`.

**Protege contra:** exigir que um documento fechado mude depois de fechado; e contra ler defeito de
escopo do instrumento como se fosse dívida do time.

---

## `BKL-T10b` — o bloco de fila é projetado inteiro, e o verbo para de destruir

**Contexto que a motivou:** o mais grave da execução. Com os marcadores `<!-- fila:gerada -->` agora
presentes no diário, o primeiro `status` ou `start` **apagava a linha `**Fila corrente:**`** — que
carrega o estado da janela inteira — porque o escritor substituía *tudo* entre os marcadores por
bullets. E devolvia **`exit 0`**: sucesso silencioso, com perda de dado.

**O que é o artefato:** a função `_regenerar_bloco_fila` em `backlog.py`, com três correções — e as
três eram necessárias:

1. projeta o bloco **inteiro** — a linha de estado **mais** os bullets;
2. casa identificador de plano pela regra de **sufixo**, não por igualdade exata;
3. aplica o **mesmo corpus** que `check` e `next` aplicam. Sem isso, reparadas só as duas primeiras,
   o bloco saía com **15 bullets de plano, 14 deles de planos fechados**.

**Como funciona, resultado real:**

```
**Fila corrente:** nada delegável — 0 elegível(is) · blocked 0
- `P-0739` (`in-progress`, 17/18): próxima —
- `TK-54` (`ready`, 1/2): próxima `TK-54b`
- `P-0741` (`ready`, 0/5): próxima —
```

Quatro linhas regeneradas a cada transição, onde antes havia um parágrafo de centenas de palavras
mantido à mão.

**Protege contra:** verbo destrutivo que devolve sucesso. A perda só aparecia para quem comparasse
o arquivo antes e depois.

---

## `BKL-T10a` — `drain`: o inbox sai do contexto

**Contexto que a motivou:** planos novos entram por uma fila em `docs/plans/_INBOX.md`. Enquanto não
fossem promovidos ao índice, o pickup carregava o inbox inteiro — e a promoção era leitura e
digitação humanas.

**O que é o artefato:** o verbo `drain` em `backlog.py`.

**Como funciona, com saída real desta execução:**

```
$ python .claude/tools/backlog.py drain
drain: arquivos tocados: docs/DIARIO_DE_OBRAS.md, docs/plans/_INBOX.md, docs/plans/_INBOX_HISTORICO.md
```

Para cada linha viva do inbox ele lê o **estado do cabeçalho do plano**, o **título da linha 1** e
usa o **caminho como âncora**, e escreve a linha de índice. A linha sai do inbox **verbatim** para o
histórico, prefixada de `- [drenado AAAA-MM-DD]`. Nada se apaga. A linha que ele escreveu:

```
| P-0741-MC | O modelo conceitual do plano: a interface entre o dono e o loop | ready | docs/plans/P-0741-modelo-conceitual.md |
```

**Protege contra:** carregar o inbox no contexto; e contra promoção por julgamento — o `drain` não
escolhe nada, projeta.

---

# Estrato D — o instrumento chega ao agente sem ele pedir

## `BKL-T11` — o hook, o ponto de carga, e as skills que rodam o verbo

**Contexto que a motivou:** de nada adianta o programa decidir se o agente continua abrindo
documentos para descobrir o que fazer. Faltava o **ponto de carga**: o momento em que a resposta
chega sem ser pedida.

**O que é o artefato:** três coisas.

1. `.claude/tools/backlog_hook.py` — um hook de `UserPromptSubmit`;
2. o registro dele em `.claude/projecoes.json`, materializado por `materializar.py apply`;
3. a reescrita das duas skills vivas (`passagem-de-bastao` e `scrum-master`) para **rodar o verbo**
   em vez de descrever a heurística.

**Como funciona o hook, na prática:** a cada prompt do usuário, o harness entrega um JSON na entrada
padrão do hook. Ele casa o gatilho — a constante é `GATILHO = "proximo passo"` — e, casando, roda
`next` por importação e devolve a saída em `hookSpecificOutput.additionalContext`. O agente começa o
turno **já sabendo** qual é a próxima tarefa, com o dossiê dela. **Sem gatilho, sai em silêncio.**
Erro do `next` vira texto de contexto e **nunca bloqueia o prompt**.

**O procedimento que ela instalou — o ponteiro morre, a skill roda o verbo** (`DB-51`): a heurística
de fila **deixa de existir em texto**. A skill não aponta para uma seção de especificação; manda
rodar o comando. Quando `next` recusa, ele nomeia a condição (`E-1`, `E-2`, `E-3`), e o que se faz é
corrigir o dado nomeado — nunca escolher à mão.

**Protege contra:** a doutrina envelhecer em relação ao código. O que muda é o programa; o texto
aponta para ele.

---

## `BKL-T11a` — o hook estava mudo, e ninguém sabia

**Contexto que a motivou:** o hook foi entregue, testado e **aprovado com 91%**. Mas os testes o
alimentavam por **importação**, com a string já decodificada em memória. Rodado como **executável**
no ponto de carga real, devolvia **0 bytes** — e `exit 0`.

**A causa:** `sys.stdin.read()` decodifica usando a codificação do host. Num Windows sem
`PYTHONUTF8`, isso é `cp1252`: o payload UTF-8 chegava como `execute o prÃ³ximo passo`, e a string
acentuada deixava de casar o gatilho.

**Por que era grave:** a tarefa seguinte — `BKL-T12` — **mede o tamanho do pickup e publica o
número**. Com o hook mudo, a medida sairia **zero**, e zero ali leria-se como o sucesso espetacular
de ter eliminado o pickup inteiro. O silêncio viraria um fato publicado num documento de decisão.

**O que é o artefato:** duas mudanças em `backlog_hook.py`, com papéis **diferentes e medidos**:

- **o reparo:** `raw = sys.stdin.buffer.read().decode("utf-8", errors="replace")` — lê bytes e
  decodifica explicitamente. **Sozinho, conserta.**
- **a ampliação:** normalizar acento e escrever o gatilho sem ele. **Sozinha, não conserta** —
  normalizar o texto já mis-decodificado produz `pra3ximo`, porque o `³` do `cp1252` decompõe em
  `3`. O ganho dela é outro: faz casar `proximo passo` sem acento, que alguém digita sem pensar e
  que antes falhava calado.

**Como funciona na prática:** o hook é alimentado com o mesmo payload que o harness entrega, em
bytes, e o que se observa é o tamanho da resposta:

```
$ printf '{"hook_event_name":"UserPromptSubmit","prompt":"execute o prÃ³ximo passo"}'     | python .claude/tools/backlog_hook.py | wc -c
9676
```

**Medido no ponto de carga real, sem `PYTHONUTF8` no ambiente:**

| payload | antes | depois |
|---|---|---|
| `execute o próximo passo` | 0 bytes | **9.676 bytes** |
| `execute o proximo passo` | 0 bytes | **9.676 bytes** |
| `ola` (sem gatilho) | 0 bytes | 0 bytes — correto |

**O procedimento que ela instalou — teste que julga um executável roda o executável** (`DB-53`), em
três cláusulas: (1) roda o **processo**, com entrada em bytes; (2) **fixa o ambiente** com `env`
explícito, nunca herdado — herdar faz o teste medir o host, não o código; (3) **afirma a
invariância**: o executável correto dá a **mesma** saída com e sem a variável; o quebrado dá saídas
diferentes.

**Protege contra:** teste que passa pelo motivo errado — indistinguível de um teste que passa.

---

## `BKL-T12` — medir o resultado e publicá-lo

**Contexto que a motivou:** o plano nasceu de um número — 77.457 caracteres de pickup, 30,2% de uma
janela ocupados antes do trabalho. Ele só fecha mostrando o número novo.

**O que é o artefato:** a seção `## 15` de `docs/CUSTO_DO_PICKUP.md`, mais as atualizações de
`README.md` e `docs/DOC_MAP.md` descrevendo o pickup por instrumento.

**Como funciona a medida:** o método tem duas metades — os caracteres que o hook injeta numa sessão
nova, e o primeiro `usage` dessa sessão. A primeira se mede rodando o hook; a segunda exige abrir
uma janela principal nova.

**Resultado:** pickup composto de **26.760 caracteres** — **−65,5%** contra os 77.457, e 66,9% do
alvo de 40.000.

**O procedimento que ela instalou — lacuna declarada, nunca estimada:** a metade `usage_1` **não é
observável de dentro de um subagente**. Foi registrada como lacuna explícita, **sem valor**, em vez
de estimada. Um número inventado ali seria publicado como fato num documento usado para decidir
custo.

**Protege contra:** meia medida apresentada como inteira.

---

# O que vale além deste plano

Nove regras saíram desta execução e continuam verdadeiras sem o `backlog.py`:

| regra | o que resolve | residência |
|---|---|---|
| **Corpus derivado do índice** | escopo de conferência não se infere do arquivo; lê-se da projeção | `DB-43` |
| **Célula congelada** | narrativa de fechamento pertence ao item terminal; não se exige que o fechado mude | `DB-46` |
| **Projeção filho → pai** | estado mora na linha do filho; o contador do pai deriva. A direção inversa fecha ciclo | `DB-45` |
| **Linha de dependência só com identificadores** | o parser lê todo literal entre crases como id; prosa ali cria dependência que nunca resolve | `DB-50` |
| **Teste que julga executável roda o executável** | roda o processo, fixa o ambiente, afirma a invariância | `DB-53` |
| **Aceite que edita documento roda em cópia antes do despacho** | aceite cujo alvo depende do estado que os próprios passos criam é inverificável por leitura | `DB-47` |
| **Separar decisão de transcrição** | decidir carrega o contexto do momento; transcrever mede a árvore | `AE-13` |
| **`drain` é ato de orquestração** | projeção mecânica de um ato anterior não é decisão nova | `DB-49` |
| **Verbo que substitui intervalo declara o que removeu** | linhas removidas × escritas é o derivado mais barato contra perda silenciosa | `TK-55` |

---

# Os ganhos, medidos

| medida | antes | depois |
|---|---|---|
| pickup carregado por sessão | **77.457** chars | **26.760** chars (**−65,5%**) |
| saída do hook no ponto de carga real | **0** bytes | **7.079** chars |
| `check` contra a árvore real | **309** violações | **0**, `exit 0` |
| documentos varridos pelo lint | 20 planos | só os vivos |
| linha `Fila corrente` | parágrafo mantido à mão | **4 linhas** regeneradas por verbo |
| contador `<done>/<total>` | atualizado à mão, envelhecia calado | recomputado; convergiu com contagem manual independente |
| suíte de testes | **201** | **224** |
| verbos exercidos em produção | 0 de 7 | **7 de 7** |

---

# O padrão que a execução revelou — e o estado de cada caso

Oito defeitos distintos desta execução são a **mesma classe**: **o derivado cala onde deveria
falar.** Um instrumento que erra em silêncio é indistinguível de um que acerta.

**Os oito foram encontrados e corrigidos dentro desta execução — nenhum está pendente como
defeito.** O que varia, e é o que importa para quem vier depois, é se existe algo que **impeça o
mesmo defeito de voltar**. Três estados:

- 🟢 **Fechado com guarda** — o defeito não existe mais e há teste ou verificador que barra a volta.
- 🟡 **Caso fechado, classe sem guarda** — este caso foi corrigido; nada impede outro igual.
- 🔴 **Regra escrita, aplicação pendente** — sabe-se o que fazer, e ainda não foi feito em toda parte.

| # | o defeito | como se manifestava | estado | o que fecha (ou faltaria fechar) |
|---|---|---|---|---|
| 1 | `check` varria 20 planos | número grande de achados, que se lê como dívida do time | 🟢 | corpus derivado do índice (`DB-43`), com testes. 309 → 0 violações |
| 2 | `status` apagava a linha de estado da janela | `exit 0`, sem aviso; a perda só aparecia comparando o arquivo antes e depois | 🟢 | `_regenerar_bloco_fila` projeta o bloco inteiro (`BKL-T10b`), com 4 testes |
| 3 | o hook devolvia 0 bytes | `exit 0`; e a tarefa seguinte publicaria esse zero como **medida** | 🟢 **neste hook** | `stdin` lido em bytes (`BKL-T11a`), com teste por subprocesso. **Ver pendência 1** |
| 4 | `next` dizia *"nada delegável"* com a fila cheia | indistinguível de backlog legitimamente vazio | 🟡 | `DB-50` normalizou os cards vivos, e `next` voltou a selecionar. **14 cards terminais seguem com a mesma dependência fantasma** — inertes, porque `next` só olha dependência de card `ready`. Nenhum verificador acusa |
| 5 | aceite que contava a si mesmo | o item de verificação fazia `Select-String` sobre o arquivo que continha o próprio padrão escrito | 🟡 | os itens da `BKL-T9a` foram corrigidos. Nada impede escrever outro aceite assim |
| 6 | aceite inatingível pelos próprios passos do card | aprovado em **100%** por quem o **leu** em vez de rodar | 🟡 | `DB-47` fixa o método — *aceite que edita documento roda em cópia antes do despacho*. É regra de conduta, sem verificador que a force |
| 7 | ponteiro para seção que não existe | atravessou autoria, transcrição aprovada em 100%, duas varreduras e um despacho | 🟡 | `DB-51` eliminou o ponteiro em vez de reapontá-lo. **Nenhum verificador resolve citação de seção** — nem `check`, nem `card_check`, nem o gate |
| 8 | teste que passa pelo motivo errado | TF por subprocesso herda o ambiente do `pytest` e deixa de discriminar | 🔴 | `DB-53` fixa a regra em três cláusulas. **O teste do próprio `BKL-T11a` ainda herda o ambiente.** Ver pendência 2 |

O inventário completo, com as evidências, está em `## TK-55` de `docs/DIARIO_DE_OBRAS.md`, que é o
acumulador da spec de robustez.

**O contraste que resume tudo:** dos cinco pontos do kit que leem entrada padrão, os **dois** que
acertam a codificação são exatamente os dois que **não têm teste**. Foram escritos por quem já
tinha se queimado. O acerto veio de cicatriz, não de norma — e cicatriz não se propaga: morre com
quem a tem. Converter cicatriz em norma é o que a coluna "estado" acima mede.

---

# Pendências abertas ao fim do plano

Seis itens. **Nenhum bloqueia o uso do instrumento** — ele está em produção, com os sete verbos
exercidos e `check` verde. São dívidas conhecidas, cada uma com dono declarado ou explicitamente
sem dono.

| # | tíquete | pendência | por que ficou aberta | o que a fecha | bloqueia algo? |
|---|---|---|---|---|---|
| 1 | `TK-56` | **três pontos de carga com a mesma falha de codificação** — `ocupacao.py:141`, `telemetria_hook.py:213` e `modelo_por_fase_userpromptsubmit.py:101` | matéria transversal a este plano: consertá-los aqui violaria o recorte do plano | aplicar `DB-53` aos três. **O terceiro é global e ativo em todos os projetos** — vem degradando em silêncio para prompt acentuado | não bloqueia o `P-0739`. **Afeta outros projetos hoje** |
| 2 | `TK-57` | **o teste do `BKL-T11a` herda o ambiente** | emendá-lo exigiria retroagir em card já `done` e com RDO escrito | fixar `env=` explícito no TF | **é pré-requisito da pendência 1** — propagar a regra incompleta multiplicaria por três um teste que não discrimina |
| 3 | `TK-58` | **metade `usage_1` da medida de pickup** | não é observável de dentro de um subagente; exige janela principal recém-aberta | abrir uma sessão nova e ler o primeiro `usage` | não bloqueia. A medida em caracteres já está publicada, e a lacuna está **declarada sem valor** na `## 14` de `docs/CUSTO_DO_PICKUP.md` |
| 4 | `TK-59` | **contador de id do inbox** | conta o que passou pelo inbox; plano criado sem passar por ele fica invisível | um verificador que confronte o contador com `docs/plans/` | não bloqueia. O valor **já foi corrigido à mão** nesta execução (`P-0742` → `P-0743`); o que falta é a guarda |
| 5 | `TK-60` | **citação de seção sem verificador** | abrir o verificador seria matéria transversal | um verbo que resolva *"§X.Y publicada em Z"* como o kit já resolve caminho e identificador | não bloqueia. É a classe do defeito 7 acima |
| 6 | `TK-61` | **`DB-4` — "candidato a fechamento"** | norma publicada em §3 **sem implementação e sem teste**; nem corpus nem migração, então ficou fora dos módulos | implementar o rodapé que a norma descreve | não bloqueia. Consequência real: planos cujos filhos ficaram todos terminais *deveriam* aparecer no rodapé de `next`, e nada os mostra |

**Resumo honesto do estado:** o plano entregou o que se propôs — o pickup caiu 65,5%, o programa
decide e escreve, e os sete verbos rodaram em produção. As seis pendências acima são **dívida
declarada**, não trabalho esquecido: cinco delas são guardas que faltam, e uma é uma medida que
exige um ato manual. A única com efeito **fora deste projeto** é a pendência 1.

**Todas as seis viraram tíquete avulso**, abertos no encerramento do plano e **priorizados para a
próxima execução** (ato do dono, 2026-09-20). A diretiva viva do `docs/DIARIO_DE_OBRAS.md` os
coloca à frente do `P-0741`.

**A ordem entre eles não é livre:** o `TK-57` vem **antes** do `TK-56`, porque propagar a regra de
teste aos três pontos de carga com o teste ainda incompleto multiplicaria por três um teste que não
discrimina. Os outros quatro são independentes entre si.


# Desfecho das pendências (2026-09-20)

As seis pendências acima foram executadas em janela própria, em sequência. **Cinco fecharam
entregues; uma fechou com o resultado invertido** — e é a mais informativa das seis.

| # | tíquete | desfecho | o que ficou |
|---|---|---|---|
| 1 | `TK-56` | **entregue** | os três pontos de carga leem `stdin` em UTF-8 explícito, cada um com teste por subprocesso e ambiente fixo. O terceiro é global: o reparo vale para todos os projetos da família. Exigiu um card extra (`TK-56b`) porque dois dos três testes ficavam **verdes com o reparo revertido** |
| 2 | `TK-57` | **entregue** | o TF fixa `env=` de dicionário mínimo, afirma a invariância do executável correto e tem par negativo. Abriu o `TK-63`, que estendeu a mesma disciplina aos sítios que discriminavam **por acidente de plataforma** |
| 3 | `TK-58` | **medida feita, conclusão invertida** | o `usage_1` foi medido — **39.650 tk** — e a medida **não sustenta** o que dela se esperava. Ver a seção seguinte |
| 4 | `TK-59` | **entregue** | violação `C-10`: `check` confronta o contador de `_INBOX.md` com o maior id presente em `docs/plans/` e acusa quando o contador aponta para id já usado |
| 5 | `TK-60` | **entregue** | violação `C-11`: o terceiro resolvedor de referência do kit. Custou três cards — o primeiro foi **reprovado 56%** por defeito de autoria do card, não de execução |
| 6 | `TK-61` | **entregue** | o rodapé de `next` imprime *candidato a fechamento*, em linha própria, com as quatro cláusulas da definição verificadas uma a uma |

**Quatro tíquetes que a execução teve de abrir**, todos fechados na mesma janela:

- **`TK-62`** — `rdo.py` não reconhecia ID de subtarefa de tíquete (`TK-<n><letra>`). Travava o
  dossiê de evidência e o fechamento de RDO para **todo** tíquete. A `DB-17` justificara a forma do
  card afirmando que os instrumentos *"já leem essa forma"*; a cláusula era falsa e nunca fora
  verificada.
- **`TK-63`** — os testes de executável discriminavam **por acidente de plataforma**: o mundo "sem
  `PYTHONUTF8`" só é hostil num host Windows-cp1252. O mundo hostil passa a ser **construído**
  (`PYTHONIOENCODING=cp1252`), que é hostil em qualquer host.
- **`TK-64`** — `check-drift` estava vermelho por faltar em `.claude/README.md` a linha de uma skill
  entregue por card já fechado. O vermelho chegava **sem dono** a toda revisão e obrigou três
  reconciliações manuais.
- **`TK-58b`..`TK-58d`** — três correções sucessivas do texto que publica a medida de pickup.

# A medida de pickup: o que ela sustenta, e o que não

A metade em **chars** está medida e **de pé**: **26.760 chars**, **−65,5%** sobre os 77.457 da
`## 3` de `docs/CUSTO_DO_PICKUP.md`, e **66,9%** do alvo de 40.000 da `## 6`. Esse é o ganho que o
plano entregou, e ele nunca dependeu da outra metade.

A metade **`usage_1`** foi medida em 2026-09-20: **39.650 tk**, em sessão principal aberta com o
gatilho na primeira mensagem. **Ela não fecha o par**, e o motivo é uma propriedade do método, não
um defeito da medição:

- o registro do pickup é **~16%** dos ~48,5 mil chars renderizados que precedem o primeiro `usage`
  — o resto é listagem de agentes, listagem de skills, arquivos anexados, contexto de sessão, MCP e
  ambiente;
- **39.650 cai dentro da linha de base sem pickup do mesmo dia** (36.023 · 36.262 · 48.171 ·
  49.533). O efeito buscado é **menor que a dispersão do controle**.

A seção publicada mede, portanto, **abertura de janela que fez pickup** — comparável aos regimes já
publicados —, e **não** o custo do pickup. O par do `DC-4` fica **aberto por declaração**; fechá-lo
exige **controle pareado**: duas sessões gêmeas, mesmo dia e mesma árvore, diferindo só no gatilho.

O método ganhou três cláusulas que este caso ensinou: **o pickup é função da tarefa**, não constante,
e toda medida nomeia o dossiê que projetou; **a metade `usage_1` só vale se isolar o pickup**; e
**todo número publicado nomeia o objeto medido** — comprimento de registro, de texto renderizado e
de texto-fonte são três objetos distintos.

Fica **a apurar**, antes de qualquer republicação da `## 14`: nesta data `CLAUDE.md` mede 12.313
chars contra os 10.376 publicados, e as 8.488 chars de memórias indexadas não aparecem entre os
anexos da primeira requisição da sessão medida.

# O padrão que a execução das pendências revelou

Um só, e ele atravessou a janela inteira: **o card cita medida real feita em outra data, e nada
confronta a medida com a data**. Quatro casos, três barrados no gate antes do despacho e um só no
laudo:

| o que o card afirmava | o que a re-derivação mediu |
|---|---|
| saída do hook: 7.123 bytes | **1.237** |
| *"as 301 linhas não contêm o literal `2.5`"* | **contêm**, uma vez, em prosa |
| *"casos vivos: `TK-51` e `TK-53`"* | ambos `done`; a população do fenômeno **zerada** pela própria execução |
| 13 ocorrências de dívida | **15**, contadas pelo instrumento |

O corolário mais duro é o do terceiro caso: **aceite ancorado em população viva é o pior tipo**,
porque a execução do plano a extingue enquanto o plano roda.

Segundo padrão, nomeado no fim: **o card fixa a propriedade a satisfazer, não a técnica**. Das
reprovações e ressalvas desta janela, a maioria nasceu de card que prescreveu *como* fazer —
um shim, um registro em RDO, uma gramática autorada — onde devia fixar *o quê*. Em todas, quem
executou cumpriu a prescrição à risca e o defeito estava na premissa.

Os dezesseis achados desta classe estão registrados em `docs/DIARIO_DE_OBRAS.md` › `## TK-55`, como
insumo da spec de robustez.

# Estado final

- **Suíte:** 238 testes verdes (eram 224 na abertura da janela).
- **Guardas:** `backlog.py check` OK · `dead_code.py` exit 0 · `kit_check -Mode check-drift` exit 0.
- **Vocabulário de violações:** `C-1` a `C-11` — duas nascidas nesta janela.
- **Dezesseis cards fechados**, cada um com RDO e laudo consumido; nenhum laudo órfão.

**O plano fecha em 18/18.** As seis pendências que ele deixou estão fechadas; a única questão que
permanece aberta — o par do `DC-4` — está **declarada como aberta**, com o experimento que a fecha
nomeado, e não bloqueia nada.
