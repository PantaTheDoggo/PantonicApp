# Modo de operação do framework — antes e agora

**Propósito:** material de avaliação para o **veredito do dono** na `LM-T6` do `P-0740`. Não é
doutrina e não substitui `GOVERNANCA.md`: se o veredito for de aprovação, a pergunta de onde cada
fato aqui deve residir é matéria de planejamento, não deste documento.

**Data:** 2026-09-19. **Base:** a série medida em `docs/telemetria.tsv` (**333 linhas em
2026-09-19**), os **30 RDOs** de `docs/RDO/` na mesma data, e o run de aferição da `BKL-T4` que
abriu o `P-0740`. Toda contagem deste documento é **datada**: elas se movem a cada tarefa fechada,
e número de contagem sem data é o defeito que a `DM-23` proíbe.

---

## 1. O ciclo, antes dos artefatos

Uma tarefa custava um **round-trip humano**. O ciclo era:

1. Você abria uma sessão e pedia o próximo passo.
2. O agente lia o diário, decidia o que vinha a seguir e **perguntava a você** se era aquilo.
3. Você confirmava. O agente implementava.
4. O agente declarava a própria entrega pronta — **quem executou também julgou**.
5. Você lia o resultado, aceitava ou mandava refazer.
6. Para a tarefa seguinte, tudo recomeçava: contexto novo, diário relido inteiro, estado
   redescoberto.

Três consequências, e as três eram estruturais:

- **Você era o loop.** Nada avançava entre duas tarefas sem a sua presença. O agente não tinha a
  quem entregar senão a você, e não tinha de quem receber senão de você.
- **Ninguém media nada.** Não havia série de consumo, não havia registro por tarefa. O custo de uma
  decisão era percebido, nunca medido; a comparação entre dois modos de trabalho era opinião.
- **Auto-aceitação.** O mesmo contexto que implementou dizia se estava bom. Um executor que erra e
  não percebe entrega o erro com a mesma confiança com que entregaria o acerto.

E havia um quarto, mais caro que os três: **o plano vivia na sessão**. Um `/clear` destruía o que
tinha sido decidido, e a sessão seguinte replanejava o mesmo alvo do zero.

---

## 2. O ciclo, hoje

Você diz **"execute próximo loop"** e vai embora. O que acontece sem você:

1. **Gate de modelo.** O contexto principal confere se está no modelo que a fase exige e **para para
   pedir** se não estiver. (Nesta janela ele parou e você decidiu manter Opus — o override é seu,
   e ficou registrado.)
2. **Seleção.** A próxima tarefa sai da fila do plano, lendo o `status` de cada card. Não há
   pergunta.
3. **Dois gates antes de delegar.** `G-PLANREADY` e o gate de delegação de sete itens. Um deles
   exige **re-derivar os números de aceite no ato** — piso de testes, contagens, âncoras de linha —
   em vez de copiá-los do plano, porque número copiado envelhece.
4. **Despacho ao executor**, em contexto limpo, no modelo declarado no cabeçalho do card. O
   executor recebe o dossiê fechado e devolve **uma linha**, de domínio fechado: `review` ou
   `blocked motivo=<dependencia|premissa>`.
5. **Despacho ao reviewer**, em contexto próprio, **em modelo mais forte que o do executor** e com
   a escrita restrita ao caminho do laudo — a independência é imposta pela lista de ferramentas,
   não pedida por instrução. Ele recebe um dossiê de evidência **mecânica** (diff, arquivos
   tocados, atribuição de cada arquivo a alvo ou não) gerado por instrumento.
6. **Roteamento por tabela.** O veredito e a recomendação do laudo são lidos, não julgados: uma
   tabela de precedência decide fechar, refazer, escalar ou parar.
7. **Arquivamento.** RDO escrito por instrumento a partir do laudo, laudo apagado, uma linha nova
   na série de telemetria.
8. **Continua.** A janela vai até o **marco validável**, não até a primeira tarefa.

Você aparece **uma vez**, no marco.

### O que o loop faz quando dá errado

Isto é o que mais mudou, e o que menos se vê num diagrama.

- **Executor não decide e não pergunta.** Se o card exigiria uma escolha dele, ele **recusa** e
  devolve `blocked`. Aconteceu duas vezes nesta janela. Na primeira, o card mandava publicar uma
  régua "no arquivo do planner" sem dizer **onde** — o executor parou em vez de escolher um lugar e
  seguir. Antes, isso teria virado uma decisão silenciosa dentro de uma entrega.
- **A recusa vira escalonamento, não parada.** Um **consultor de plano** — instanciado **uma vez**
  por execução e mantido com o cenário no contexto — recebe o impedimento, decide se é tático ou
  estratégico, e **repara o plano**. Nesta janela ele reescreveu dois cards e registrou **quatro**
  decisões (`DM-46`..`DM-49`). Só o que ele classificar como **estratégico** sobe a você — e ele
  **parte a matéria** quando ela é mista: no último escalonamento deu residência ao problema e
  **recusou escolher a regra**, porque qualquer escolha moveria uma fronteira que só você move.
- **O loop também é auditado.** Nesta janela eu dupliquei duas linhas da série de telemetria e, ao
  somar, suspeitei que a medida do marco estivesse inflada. Redespachei para re-derivar, e o
  executor **me corrigiu com medida**: o total não mudava, e o delta que eu tinha calculado
  por subtração estava errado — o mesmo defeito que uma tarefa desta janela existiu para consertar.
  O achado ficou registrado contra mim (`AE-43`).

---

## 3. Os artefatos, e o que cada um substituiu

| artefato | o que existe hoje | o que fazia esse trabalho antes |
|---|---|---|
| **9 agentes** (`planner`, `executor`, `reviewer`, `consultant`, `scout`, 2 auditores, `fora-da-caixa`, `benchmarker`) | papéis com toolset e modelo próprios; o reviewer não consegue editar código porque não tem a ferramenta | um agente genérico fazia tudo, no mesmo contexto |
| **10 skills** | procedimentos nomeados; o `scrum-master` conduz o loop e a `passagem-de-bastao` faz a transição entre tarefas | `proximo-passo` + `handover`, **ambas aposentadas** nesta iniciativa |
| **`GOVERNANCA.md`** | matriz de responsabilidades, gramática do card, **19** guardas nomeadas (`G-NOASK`, `G-REPLAN`, `G-PLANREADY`…) — medido em 2026-09-19 por `check-readme.ps1`, exit 0; eram 18 antes desta iniciativa, que acrescentou o `G-MODULO` | convenção oral, redescoberta a cada sessão |
| **`docs/plans/` + diário** | o plano **sobrevive ao `/clear`**; cada card tem objetivo, arquivos-alvo, verificação e critério de pronto | o plano vivia na sessão |
| **`rdo.py`, `review_evidence.py`, `card_check.py`, `backlog.py`, `telemetria*.py`** | fechamento, evidência, régua de autoria de card e série de consumo, todos por comando | tudo à mão, quando era feito |
| **`docs/telemetria.tsv`** | **333 linhas** de consumo medido por papel (2026-09-19) | nada |
| **`docs/RDO/`** | **30 registros** de obra (2026-09-19), um por tarefa fechada, com desdobramento e consumo | nada |
| **`RUBRICA_DE_REVISAO.md`** | sete dimensões, percentual, dimensão bloqueante, e um catálogo de **defeitos de autoria de card** aprendidos na prática | juízo livre do revisor, quando havia revisor |

---

## 4. O que é medido hoje e não era

Baseline do run de aferição sobre a `BKL-T4`, **uma** tarefa conduzida pelo loop na sua primeira
versão: **284,6k tk · 71 tool uses · 21 min**.

Agregado do `P-0740` até este marco, **21 módulos fechados em 4 janelas**: **3.712,8k tk · 1.098
tool uses · 11.147,7 s**, o que dá, por módulo, **−37,9% em tokens, −26,3% em tool uses e −57,9%
em duração** contra aquela baseline.

Qualidade na série: **zero reprovações e zero retentativas consumidas** em 21 módulos; sete
tarefas fechadas em 100% só na janela anterior.

Esses números são de **21 módulos**, o corpus que a `LM-T6` fechou para o marco. A janela que
escreveu este documento fechou mais duas (`LM-T2f` e `LM-T8`, ambas 100%), levando o plano a
**22/27**, e custou **1.201,7k tk · 223 tool uses · 0,86 h** — ela não entra no agregado acima,
que ficou congelado no recorte do marco.

---

## 5. O que continua sendo seu

Por desenho, não por limitação:

- **O veredito de marco** — este documento existe para um.
- **Rota e escopo.** O consultor decide o operacional e o tático; sobe só o estratégico — o que altera o modelo que o dono descreveu ou o prompt da demanda (`G-ESCALA`, `GOVERNANCA.md` §7 item 21).
- **Superfície de permissão.** O loop não altera o que ele próprio pode fazer.
- **Commit.** O loop acumula e commita no marco; nesta janela não commitou, porque o marco é *de
  validação* e a validação é sua.
- **A doutrina de produto** — o quê e o porquê.

---

## 6. O que a evidência não sustenta

Isto pesa no veredito tanto quanto a seção 4.

1. **Os caminhos de recuperação do loop nunca foram exercitados.** Zero reprovações e zero
   retentativas é um bom número de qualidade e um **mau número de cobertura**: as regras de queda de
   subagente, retorno inválido, refazer e reprovar-duas-vezes existem no papel e **nunca rodaram em
   campo**. O loop é comprovado no caminho feliz e no caminho de recusa; não no de erro.
2. **O corpus é o próprio repositório do framework** — documentos e ferramentas Python pequenas.
   Nada aqui demonstra o loop sobre código de aplicação com suíte grande e domínio real. A
   comparação da seção 4 é contra **uma** tarefa, no mesmo repositório.
3. **A instrumentação está pela metade.** A materialização de `status` ainda é feita **à mão** pelo
   orquestrador: `backlog.py start` recusa neste plano por divergência de identificador entre o
   plano e o índice do diário. O gate `card_check` está **suspenso em efeito** porque dá falso
   vermelho. O hook de telemetria grava a linha do executor e **não** a do reviewer nem a do
   consultor — foi daí que veio o meu erro de duplicação.
   **O outro lado, e ele é medido:** mesmo suspenso como gate, o `card_check` pegou **quatro
   defeitos reais de autoria** nesta janela, nos dois cards que o consultor reparou, **antes** de
   qualquer despacho — três marcadores de item espúrios e um padrão `^tools:` que casava nos dois
   mundos e portanto não discriminava mundo nenhum. Suspenso como veredito, ele funciona como
   instrumento.
4. **O consultor é caro e não é especificado.** Nesta janela ele custou **578,2k tk — 48% do
   consumo da janela** (1.201,7k tk, medido em 2026-09-19, 3 escalonamentos). Ele é figura
   *ad-hoc* criada por decisão sua em 2026-09-18, e a especificação dela (`LM-T9`) ainda não foi
   escrita — por ordem sua, ela vem depois deste marco.
5. **Três dos quatro despachos de executor da `LM-T8` terminaram `blocked`**, e nenhum por defeito
   de execução: um por defeito de card, dois por recusa de ferramenta. (Na janela inteira, as
   demais tarefas foram: `LM-T2f`, fechada em um despacho; e a `LM-T6`, cujos dois `blocked` são
   **por desenho** — o card manda parar quando falta o veredito.) O loop absorveu tudo sem parar e
   sem improvisar, que é o comportamento desejado — mas o custo de um card mal autorado continua
   sendo **uma rodada inteira de consultor**.

---

## 7. A pergunta do veredito

O objetivo que abriu a iniciativa, em 2026-08-22, era:

> transformar o trabalho de `proximo-passo` num agente autônomo, capaz de rodar sozinho todas as
> delegações e ajustes de modelo, e entregar ao cliente o entregável do plano, e não delegar ao
> humano uma tarefa rotineira e mecânica.

O que está demonstrado: o loop **roda sozinho todas as delegações**, escolhe o modelo por fase,
julga por um papel independente, registra tudo que gasta, sobrevive a card defeituoso e a bloqueio
de ferramenta, e entrega no **marco** — não por tarefa.

O que **não** está demonstrado: que ele se recupera de erro de execução real, e que faz isso fora
do próprio repositório.
