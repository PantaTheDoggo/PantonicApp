# P-0746 — O lastro do modelo: o contrato se escreve do enunciado

**Data:** 2026-09-21 · **Origem:** sessão de validação prática do `P-0741` (dono, 2026-09-21),
transcrita na §0 · **Plano de origem:** `P-0741` (`ready` 7/8 — publicou o mecanismo que este plano
corrige) e `P-0743` (`done`, aceito — publicou a norma, a gramática, o instrumento e o modelador) ·
**Status:** `done` · 2026-09-24 · **aceito pelo dono no fechamento**, verbatim: *"Aceite os
planos, revise os tiquetes para ver quais são pertinentes ainda para enfileira-los na sequencia"* —
Marcos 2 e 3 fechados no mesmo ato; modelo na **versão 4 vigente**; documento de validação
`docs/OPERACOES_AS_IS_P-0746.md`. Marco 1 aceito em 2026-09-21 sobre a versão 3, depois de `no-go`
na versão 1 e aceite com uma correção na versão 2 ·
**Prefixo das tarefas no diário:** `LST-T<n>` · **Prefixo das decisões:** `DLS-<n>` ·
**Checagem de versão do kit:** modo hub — congelada em `0.0.0` (`GOVERNANCA.md` §10), nada a
comparar · **Branch de trabalho:** `plan/planner-modelo-escopo` (`DLS-6`) ·
**Ordem de execução:** LST-T1 → LST-T7 → LST-T3 → LST-T8 → LST-T9 → LST-T5 → LST-T6 ·
**Modelo de planejamento:** Opus 5, na sessão de 2026-09-21 em que o dono ditou o enunciado.

**Marcos de validação pelo dono:**

| marco | o que o dono lê | veredito |
|---|---|---|
| **Marco 1** — **fechado em 2026-09-21** | a `## 1. Modelo conceitual` deste plano — que é, ela mesma, o primeiro modelo escrito sob a regra que ele institui | exercido duas vezes: `no-go` na versão 1, que se reautorou sem cancelar o plano (`DLS-5`, `DLS-9`); **`go` na versão 3**, com a correção que retirou a restrição sem lastro (`DLS-11`). O modelo vigora a partir daqui |
| **Marco 2** — **fechado em 2026-09-24** | `python .claude/tools/modelo.py show --plano docs/plans/P-0746-lastro-do-modelo.md` depois da `LST-T5`, mais `GOVERNANCA.md` §3.2 reescrita e a **versão 4 pendente** do modelo (`## 1A`), que retira a metade de ator da `OP-5` (`DLS-13`) | **`go` em 2026-09-24**, no fechamento: a versão 4 passa a vigente e a 3 a obsoleta; o drift acumulado (`DLS-13`, `DLS-16`, `DLS-18`) fica validado (`DLS-4`) |
| **Marco 3** — **fechado em 2026-09-24** | o modelo do `P-0745` reautorado sob o conceito revisado, depois da `LST-T6` | **`go` em 2026-09-24**, no mesmo ato de aceite. A pendência `AE-18` (critério de ator inédito, dispensado pelo loop por medição) **não** foi decidida nesse ato e segue no `TK-73` Pacote 2 |

**Tarefas:** 7, fila única, sequencial — `LST-T1`, `LST-T7`, `LST-T3`, `LST-T8`, `LST-T9`,
`LST-T5`, `LST-T6`. Toda tarefa materializa operação do modelo: a `LST-T0` da versão 1 foi dissolvida na
republicação (`DLS-10`), e com ela a exceção de gate da `DLS-8`; a `LST-T2` e a `LST-T4` saíram na
versão 3 com a operação sem lastro que materializavam, e viraram o `TK-70` (`DLS-11`); a `LST-T8`
nasceu no reparo de escalonamento de 2026-09-21 (`AE-1`, `DLS-12`) e volta à `OP-1` e à `OP-2` para
publicar a residência da declaração de lastro, que a `LST-T1` exigiu sem dizer onde mora; e a
`LST-T9` nasceu no segundo reparo, em 2026-09-22 (`AE-7`, `AE-9`, `AE-10`, `AE-11`, `DLS-15`), para
acertar três frases da doutrina que as três tarefas de redação publicaram sem confrontar o corpus.

---

## 0. O problema, verbatim

Ditado pelo dono em 2026-09-21, ao ler o modelo do `P-0745` — primeiro plano nascido inteiro sob a
forma publicada pelo `P-0741`/`P-0743` — e reprová-lo.

> Estou vendo o modelo aqui, e ele não está bom. (…) Algumas restrições mais determinísticas para
> disciplinar a matéria: o modelo deve resultar diretamente do enunciado do problema. Um objeto ou
> operação ou propriedade sem esse lastro significa um requisito secundário, que deve ser
> transparente para o cliente/gerente.

> Tudo tem que ter lastro no problema e no prompt inicial que deu origem ao plano. (…) embora ainda
> seja um trabalho de inspiração alguns guardrails são determinísticos, como o lastro obrigatório de
> todos os elementos do modelo, e objetos, operações e propriedades diretamente derivados do prompt
> e problema. Qualquer entrega que não tiver lastro nesses textos são entregas que o agente supôs
> que o cliente quer.

> Novamente, isso não quer dizer que o que não tem lastro é proibido de executar. O que é proibido é
> para um elemento sem lastro é participar do modelo. Esses elementos que eu rejeitei podem entrar
> como requisitos não-fundamentais, mas são de responsabilidade inteira do agente idear, executar e
> garantir que eles não prejudiquem o modelo.

> O modelo sempre precisa ser validado pelo cliente/gerente, pois (…) é o contrato do serviço entre
> as partes. Um contrato onde só um dos atores estabelece as condições não é contrato, é imposição.

Sobre como o enunciado se lê — correção de uma interpretação que o agente errou na mesma sessão:

> tudo isso é propriedade. É o estado inicial do planejador. (…) O plano vai responder como as
> instruções contidas nesses agentes/skills responderão frente a essa mudança de estados.
> Critério de sucesso: instrumentos se utilizam do novo aparato construído.
> Critério de fracasso: instrumentos ainda utilizar os conceitos obsoletos.

Sobre o drift na execução autônoma:

> a criação do modelo é etapa do planejamento, e planejamento não é atividade do loop, que só ocorre
> após o plano estar pronto. E mesmo a execução autônoma tem marcos de descanso e validação. Nesses
> pontos também é feita a revisão do modelo pelos drifts que porventura tenham surgido durante a
> execução. O loop autônomo carrega o drift até o marco. No marco, o drift é validado e o plano
> continua, ou recusado, e as tarefas retroagem onde ocorreu o drift.

**Sobre quantos objetos um enunciado comporta** — ditado no `no-go` do Marco 1, em 2026-09-21, ao
ler a versão 1 do modelo **deste** plano e recusá-la. É o lastro da versão 2:

> Só existe um objeto nesse modelo: as restrições/guardrails. Nós iniciaremos o plano sem eles, e,
> nesse estado inicial, temos os demais elementos mencionados que são todas propriedades: modelo
> conceitual: não conforme, sem lastro, é a propriedade inicial do modelo.

> Após elaboradas as restrições/guardrails, o esperado é que o "modelo-propriedade" convirja para o
> estado "conforme". Como fará isso: por meio das demais operações: leitura de lastro, leitura de
> prompt, decomposição, atualização, decomposição de requisitos funcionais/nao funcionais.

> Nesse enunciado eu passei somente um objeto e diversas propriedades finais a serem alcançadas por
> meio da construção dessas restrições, os objetos.

---

## 1. Modelo conceitual
> **Versão 4, vigente desde o Marco 2 (2026-09-24).** Acumula, sobre a versão 3 aceita no Marco 1,
> os recortes que a própria regra de lastro impôs ao contrato durante a execução: a oração de ator
> sai da `OP-5` por inexequibilidade medida (`DLS-13`), a oração que reconhecia a tarefa de
> requisito não fundamental sai por falta de lastro (`DLS-18`, virou o `TK-71`), a `OP-5` passa a
> dizer **objeto** e a nomear a metade que o Marco guarda (quarto ato, de conflito), e as listas
> `tarefas:` contabilizam a `LST-T8` e a `LST-T9` (`DLS-12`, `DLS-16`). O plano constrói **uma**
> coisa — as restrições que disciplinam como o modelo conceitual de um plano se escreve — e tudo o
> mais que o enunciado nomeia é **propriedade** dela. Todo elemento aqui tem lastro na `## 0`.

**Estado do modelo:** versão 4 · 2026-09-24 · autor: modelador · 1 objeto · 6 operações · 6 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem | lastro na §0 |
|---|---|---|---|---|---|
| restrições do modelo conceitual | o conjunto de guardrails determinísticos que disciplinam como o modelo conceitual de um plano se escreve, se valida e se atualiza | leitura de lastro, leitura de prompt, decomposição em objeto e propriedade, decomposição de requisitos funcionais e não funcionais, aferição pelos instrumentos, conformidade do modelo | norma em `GOVERNANCA.md` §3.2; forma publicada na subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras`; aferição em `.claude/tools/modelo.py` (`check`), com `tests/test_modelo.py` e fixtures; autoria em `.claude/agents/pantonic-model-designer.md` | OP-1 | *"Só existe um objeto nesse modelo: as restrições/guardrails"*; *"Algumas restrições mais determinísticas para disciplinar a matéria"*; *"embora ainda seja um trabalho de inspiração alguns guardrails são determinísticos"* |

### 1.2 Fluxo de operações

**A. As restrições nascem da leitura do enunciado**

- **OP-1** — O redator da norma constrói a restrição de leitura de lastro: todo objeto, operação e propriedade do modelo tem âncora declarada num trecho do enunciado do problema ou do prompt que originou o plano, e elemento sem essa âncora não entra no modelo.
  - `precisa de: ` · `altera: restrições do modelo conceitual.leitura de lastro` · `tarefas: LST-T1, LST-T8, LST-T9`

- **OP-2** — O redator da norma constrói a restrição de leitura de prompt: o enunciado alimenta o modelo por duas vias declaradas — a via de estado, que popula o estado inicial e o estado final, e a via de operação, que é o que o plano faz diante do vão entre os dois.
  - `precisa de: restrições do modelo conceitual` · `altera: restrições do modelo conceitual.leitura de prompt` · `tarefas: LST-T1, LST-T8`

- **OP-3** — O redator da norma constrói a restrição de decomposição: o enunciado se decompõe primeiro em objeto e propriedade — o que o plano constrói é objeto, o que converge de um estado a outro é propriedade dele — e descrição de estado nunca vira objeto próprio.
  - `precisa de: restrições do modelo conceitual` · `altera: restrições do modelo conceitual.decomposição em objeto e propriedade` · `tarefas: LST-T7, LST-T9`

**B. O que não tem lastro ganha residência própria, em vez de sumir**

- **OP-4** — O redator da gramática constrói a restrição de decomposição de requisitos funcionais e não funcionais: o elemento com lastro é funcional e entra no modelo como contrato; o elemento sem lastro é não fundamental, reside em seção nomeada do plano fora do modelo, fica transparente para o dono e tem responsabilidade inteira do agente.
  - `precisa de: restrições do modelo conceitual` · `altera: restrições do modelo conceitual.decomposição de requisitos funcionais e não funcionais` · `tarefas: LST-T3, LST-T9`

**C. As restrições se tornam aferíveis, e o modelo converge para conforme**

- **OP-5** — O autor do instrumento faz a conferência automática passar a usar o aparato construído: ela acusa objeto do modelo sem lastro declarado, e o lastro da operação e o da propriedade ficam sob guarda do marco de validação.
  - `precisa de: restrições do modelo conceitual` · `altera: restrições do modelo conceitual.aferição pelos instrumentos` · `tarefas: LST-T5`

- **OP-6** — O modelador reautora o modelo do plano do planejador sob as restrições construídas e o devolve à medição do dono, provando no caso que originou o enunciado que o modelo convergiu de não conforme para conforme.
  - `precisa de: restrições do modelo conceitual` · `altera: restrições do modelo conceitual.conformidade do modelo` · `tarefas: LST-T6`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final |
|---|---|---|
| restrições do modelo conceitual.leitura de lastro | não existe: a norma descreve a forma do modelo — objetos, propriedades, operações, estados, versões — sem dizer de onde os elementos vêm; ocorrências de `lastro` em `GOVERNANCA.md` e na skill `diario-de-obras`: **0** cada (`F-9`), e o primeiro plano escrito sob ela admitiu dez objetos para um enunciado de nove substantivos | todo objeto, operação e propriedade tem âncora declarada num trecho do enunciado do problema ou do prompt de origem; elemento sem âncora não entra no modelo |
| restrições do modelo conceitual.leitura de prompt | o enunciado é lido como pedido de trabalho, sem distinguir o que descreve estado do que pede operação — descrição de estado vira objeto com propriedades próprias, e o modelo infla | o enunciado alimenta o modelo por duas vias declaradas: estado, que popula o inicial e o final, e operação, que é o que o plano faz diante do vão entre os dois |
| restrições do modelo conceitual.decomposição em objeto e propriedade | não existe: nada na norma diz quantos objetos um enunciado comporta nem como distinguir objeto de propriedade — medido em 2026-09-21 sobre a **versão 1 deste próprio modelo**, quatro propriedades foram escritas como objetos e o dono a recusou no Marco 1 (`F-11`) | o enunciado se decompõe primeiro em objeto e propriedade: o que o plano constrói é objeto, o que converge de um estado a outro é propriedade dele, e descrição de estado não vira objeto próprio |
| restrições do modelo conceitual.decomposição de requisitos funcionais e não funcionais | não existe: elemento sem lastro ou entra no modelo como se fosse contrato — e passa a ser cobrado como se o dono o tivesse pedido —, ou não aparece em lugar nenhum; `requisito secundário` na skill `diario-de-obras`: **0** (`F-9`) | o elemento com lastro é funcional e entra no modelo; o sem lastro reside em seção nomeada fora do modelo, transparente ao dono e sob responsabilidade inteira do agente |
| restrições do modelo conceitual.aferição pelos instrumentos | o instrumento aprova o que o dono reprovou: `check` sobre o `P-0745` sai `0` e imprime `modelo: OK` sobre exatamente o modelo recusado em 2026-09-21 (`F-6`) — ele afere forma, não procedência | o `check` acusa objeto sem lastro declarado — o lastro da operação e o da propriedade ficam sob guarda do Marco — e sobre o `P-0745` intocado o mesmo comando passa a sair `1` |
| restrições do modelo conceitual.conformidade do modelo | **não conforme, sem lastro** — o estado inicial que o dono nomeou no Marco 1 de 2026-09-21: o modelo do `P-0745` reprovado por ele, e a versão 1 do modelo **deste** plano reprovada pelo mesmo defeito | **conforme** — o modelo do `P-0745` reautorado sob as restrições construídas e devolvido à medição do dono, o mesmo teste prático que reprovou a forma anterior |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 4 | 2026-09-22 | vigente | modelador, por dossiê `Ato de modelo` de emenda despachado sobre o `AE-4` e a `DLS-13`: a oração de ator sai da `OP-5` e da linha de estado da aferição (`F-14`), e a `LST-T8` entra nas tarefas da `OP-1` e da `OP-2` (`DLS-12`). Validada pelas decisões do consultor que a acumularam (`DLS-13`, `DLS-16`, `DLS-18`) e **aceita pelo dono no fechamento de 2026-09-24** (Marco 2), verbatim: *"Aceite os planos, revise os tiquetes para ver quais são pertinentes ainda para enfileira-los na sequencia"* |
| 3 | 2026-09-21 | obsoleta | sessão de planejamento, sobre a correção do dono ao ler a versão 2 no Marco 1: a restrição de atualização não tem lastro e sai do modelo (`DLS-11`). **Aceita pelo dono no Marco 1 em 2026-09-21** — é a primeira versão que vigora Caiu pelo aceite da versão 4 no Marco 2, em 2026-09-24 |
| 2 | 2026-09-21 | obsoleta | caiu na correção do Marco 1 de 2026-09-21 — carregava uma operação sem lastro; substituída no lugar, sem nunca ter vigorado |
| 1 | 2026-09-21 | obsoleta | caiu no `no-go` do Marco 1 de 2026-09-21 — quatro propriedades escritas como objetos; substituída no lugar, sem nunca ter vigorado |
---


## 2. Requisitos secundários

> Primeira aplicação da residência que a `OP-3` institui. Nada aqui tem lastro na §0; nada aqui é
> contrato. São entregas que o agente julga necessárias para que o modelo não seja prejudicado, e a
> responsabilidade por elas é inteira dele. O dono as lê para saber que existem — não para aprová-las.

| requisito | por que o agente o julga necessário | quem responde |
|---|---|---|
| `README.md` §8.1 reescrito | a descrição pública do mecanismo ficaria contradizendo a norma revisada; porta de entrada errada é defeito que viaja para os cinco derivados | agente |
| `.claude/agents/pantonic-model-designer.md` atualizado | o prompt do modelador codifica o conceito que este plano substitui; sem atualizá-lo, o próximo modelo nasce sob a regra antiga | agente |
| teste de ausência da forma antiga | sem guarda executável, texto de doutrina regride no primeiro transporte do kit; é a aferição do critério de fracasso do dono, não um objeto do modelo | agente |
| `docs/DOC_MAP.md` com entrada deste plano | o índice de documentos é como um agente frio alcança o plano | agente |

## 3. Fatos estabelecidos

- **`F-1`** — O modelo do `P-0745` foi reprovado pelo dono em 2026-09-21, com seis classes de
  defeito tipificadas em `docs/DIARIO_DE_OBRAS.md` › `## TK-69` §3. Os casos citados são
  **exemplos, não avaliação exaustiva** — a revisão do conceito não se limita a eles.
- **`F-2`** — Dos **cinco** atores que o fluxo 1.2 do `P-0745` faz agir (*investigador*,
  *mantenedor*, *redator da norma*, *autor de papéis*, *redator da especificação*), **zero**
  existem na tabela 1.1 daquele plano. **Retificado em 2026-09-21 pelo `F-14`:** a mesma medição
  sobre o `P-0743` (modelo aceito) e sobre o modelo **deste** plano dá o mesmo resultado, de modo
  que ela **não** é a "medição mecânica mais dura" que este fato afirmava ser — mede um traço de
  estilo comum a todos os modelos do kit, não a procedência dos elementos.
- **`F-3`** — O `P-0745` está `blocked` e **não** foi cancelado. O Marco 1 dele previa só dois
  desfechos (`go`; `no-go` = `cancelled`); o desfecho real foi um terceiro, que o gate não tem.
- **`F-4`** — A norma vigente do modelo vive em `GOVERNANCA.md` §3.2, a gramática na subseção
  *Modelo de domínio (seção do plano)* da skill `diario-de-obras`, a aferição em
  `.claude/tools/modelo.py` (`check`/`show`, vocabulário `V1`..`V20`) e a autoria em
  `.claude/agents/pantonic-model-designer.md` — entregues pelo `P-0743`, `done` e aceito.
- **`F-5`** — `python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md`
  sai `0` hoje. Continuar saindo `0` é invariante deste plano (`I-2`).
- **`F-6`** — **O instrumento aprova o que o dono reprovou.**
  `python .claude/tools/modelo.py check --plano docs/plans/P-0745-planejador-modelo-operacao.md`
  sai `0` e imprime `modelo: OK — 7 operações, 11 objetos, 21 propriedades, 7 tarefas, versão 1`
  sobre exatamente o modelo que o dono recusou em 2026-09-21. É a medida mais direta do vão que a
  `OP-5` fecha: o `check` afere forma, não procedência.
- **`F-7`** — O conceito de **drift** já existe na norma (`GOVERNANCA.md:372-375`), distinto de
  medição. O que não existe é conduta nem desfecho: `drift` tem **0** ocorrências em
  `.claude/skills/scrum-master/SKILL.md`. **O vão é real e continua aberto**, mas saiu deste plano
  na versão 3 do modelo: o trecho da `## 0` que o descreve é explicação de como a coisa funciona,
  não pedido de trabalho, e portanto não é lastro (`DLS-11`). Virou o `TK-70`.
- **`F-13`** — **O dono aceitou a versão 2 do modelo com uma correção, em 2026-09-21:** a
  então-`OP-4` (restrição de atualização — vigência bilateral e conduta de drift) *"foge um pouco
  do escopo de lastro (…) foi mencionado do enunciado, mas a título de conversação"*, e o conteúdo
  dela *"já deve estar abrangido por outra ferramenta"*. É a primeira vez que a regra de lastro
  recorta o **próprio** plano que a institui, e o recorte foi feito por leitura do dono — não por
  comando, como o `F-12` previa.
- **`F-8`** — **Afastamento de norma registrado.** A tabela *Quem escreve* de `GOVERNANCA.md` §3.2
  diz que o planejador devolve o dossiê de autoria e que *"o plano não vai ao Marco 1 sem a seção
  escrita pelo modelador"*. Este plano vai ao Marco 1 com a seção escrita pela sessão de
  planejamento (`DLS-7`), e o afastamento fica declarado aqui em vez de silencioso.
- **`F-10`** — **A `V9` não era defeito da gramática; era sintoma do modelo mal decomposto.**
  Sobre a **versão 1** do modelo deste plano — quatro objetos, todos de origem `externo` — a
  violação `V9` (*operação desencadeada*) acusava `OP-2`, `OP-3` e `OP-4`, e a leitura da sessão
  foi de que a regra não acomodava plano de doutrina. **A medição desmentiu a leitura:** sobre a
  versão 2, em que o plano constrói **um** objeto e as demais operações o consomem, `V9` sai de
  três acusações para **zero**, sem uma linha tocada em `.claude/tools/modelo.py`. Medido em
  2026-09-21, antes e depois da reautoria. O afrouxamento que a `LST-T0` previa está **revogado**
  (`DLS-10`): relaxar `V9` teria enfraquecido o guardrail para acomodar um modelo defeituoso.
  Sobrevive só a segunda metade do fato — `V2` (*tarefa sem operação*) não conhece a categoria de
  requisito não fundamental que a `OP-4` institui —, e essa correção passou a ser conteúdo da
  `LST-T5`.
- **`F-11`** — **O dono recusou a versão 1 do modelo deste plano no Marco 1, em 2026-09-21**, pelo
  mesmo defeito que motivou a recusa do `P-0745`: quatro propriedades — *modelo conceitual*,
  *requisito secundário*, *marco de validação* e *loop autônomo* — escritas como objetos. O
  enunciado comporta **um** objeto, as restrições, e o ditado da recusa está na `## 0`. É a
  segunda ocorrência medida da mesma classe de defeito, e o que justifica a `LST-T7`.
- **`F-12`** — **A promoção indevida não é aferível por instrumento.** Nenhum `check` decide se um
  substantivo do enunciado é objeto ou propriedade — a `LST-T7` entrega norma, e a guarda dela é o
  Marco. As duas recusas do dono em 2026-09-21 (`F-1`, `F-11`) foram feitas por leitura humana,
  não por comando, e é assim que a restrição continua a ser exercida.
- **`F-14`** — **A regra de ator não discrimina — medido em 2026-09-21, no reparo de
  escalonamento.** Sobre o `P-0743`, cujo modelo está aceito e é protegido pelo `I-2`, a prosa de
  `### 1.2` faz agir **sete** atores (*redator da norma*, *redator da gramática*, *implementador do
  instrumento*, *implementador*, *autor de papéis*, *mantenedor*, *modelador*) e **um** existe na
  tabela `### 1.1` — o *modelador*, e só porque aquele plano o constrói. Sobre o modelo **vigente
  deste plano**, agem quatro (*redator da norma*, *redator da gramática*, *autor do instrumento*,
  *modelador*) e **zero** existem entre os objetos, que são um só. Uma violação de ator ao pé da
  letra reprovaria os dois. No mesmo ato mediu-se o outro lado: **nenhum** dos três planos —
  `P-0743`, `P-0745`, `P-0746` — declara lastro em `### 1.2` ou `### 1.3`, e só o `P-0746` o declara
  em `### 1.1` (sexta coluna).
- **`F-15`** — **O instrumento já conhece o status do plano.** `modelo.py` carrega `backlog.py` em
  `verbo_check` e chama `_parse_plano`, cujo `Plano.status` está disponível antes da validação.
  Medido em 2026-09-21: `done` para o `P-0743`, `blocked` para o `P-0745`, `ready` para o `P-0746`.
  É o único discriminador disponível entre modelo de plano vivo e modelo de plano fechado.
- **`F-16`** — **`grep -ciF` aborta neste ambiente.** Medido em 2026-09-21 (Git Bash, Windows):
  `grep -ciF 'lastro' GOVERNANCA.md` → `Aborted (core dumped)`, exit **134**, reproduzido duas
  vezes; `grep -cF` e `grep -ci` saem normalmente. Nenhum card deste plano prescreve `-iF`.
- **`F-17`** — **O parser lê a linha de máquina de `### 1.2` com regex ancorada em `$`.**
  `_OPERACAO_LINHA_RE` casa exatamente `precisa de:` · `altera:` · `tarefas:` e termina em `$`; um
  quarto campo faz a operação inteira deixar de ser reconhecida, silenciosamente. E `validar` só
  confere a **versão** da seção pendente (`V20`), de modo que um `## 1A` escrito na forma nova
  passaria por `check` sem violação e quebraria `show --drift`. É a razão da ordem `LST-T8` →
  `LST-T5` → ato de modelo: gramática nova não se aplica antes de o parser aprender.
- **`F-18`** — **Linha de base do corpus de fixtures, medida em 2026-09-22, antes da `LST-T5`.**
  `modelo.py check` sobre `tests/fixtures/modelo/`: `plano-invalido.md` → **10 violações**;
  `plano-invalido-2.md` → **4** (soma **14**, a do teste da ordem); `fluxo-valido.md` →
  `modelo: OK — 3 operações, 4 objetos, 4 propriedades, 3 tarefas, versão 1`; `fluxo-concluido.md`
  → `modelo: OK`; `fluxo-pendente.md` → **4**; `plano-sem-cabecalho.md` → **1**;
  `plano-sem-estado.md` → `modelo: forma anterior`. As **sete** fixtures que têm `### 1.1` declaram
  as cinco colunas antigas e leem `status='in-progress'` pelo mesmo `_parse_plano` que o `check`
  usa — estão, portanto, **dentro** do alcance da `V21` (`AE-14`), e é a forma delas que se migra,
  não a regra que se afrouxa (`DLS-17`).
- **`F-19`** — **A forma que a metade `V2` da `OP-5` mandava reconhecer nunca foi publicada.**
  Medido em 2026-09-22: `requisito não fundamental` tem **0** ocorrências em
  `.claude/skills/diario-de-obras/SKILL.md` e **0** em `GOVERNANCA.md`; a gramática define **uma**
  forma para o campo `Operação do modelo` do card, sem alternativa de declaração. E a `## 0` deste
  plano não a pede: o enunciado fala de **elemento** sem lastro — *"podem entrar como requisitos
  não-fundamentais, mas são de responsabilidade inteira do agente idear, executar e garantir"* —,
  âncora da `OP-4`, materializada na seção nomeada pela `LST-T3`. A cláusula desce do `F-10`, que é
  medição do instrumento; medição de instrumento não é âncora (`DLS-18`).
- **`F-9`** — Linhas de base medidas em 2026-09-21, antes da primeira tarefa: `python -m pytest
  tests -q` → **262 passed**; `tests/test_modelo.py` → **23 passed**; ocorrências de `lastro` em
  `GOVERNANCA.md` → **0**, na skill `diario-de-obras` → **0**; `requisito secundário` na skill →
  **0**.

## 4. Decisões (fechadas neste ato; o executor não as reabre)

- **`DLS-1`** — O lastro é **doutrina**, não correção pontual do `P-0745`. Razão do dono: os casos
  citados foram exemplos; a classe de defeito nasce do conceito, e corrigir só a instância deixa a
  próxima nascer igual.
- **`DLS-2`** — Elemento sem lastro **não é proibido de executar**; é proibido de **participar do
  modelo**. A residência dele é a seção de requisitos secundários, e a responsabilidade é inteira
  do agente.
- **`DLS-3`** — A validação do modelo pelo cliente **não é exceção ao loop autônomo**. Ato do dono
  de 2026-09-21: a criação do modelo é etapa de **planejamento**, e planejamento não é atividade do
  loop, que só começa com o plano pronto. A leitura anterior desta sessão — que tratava a validação
  como exceção declarada ao objetivo da `EXECUCAO-AUTONOMA` — fica **revogada**. A correção do
  `TK-69` §2 saiu deste plano com a `LST-T2` e é matéria do `TK-70` (`DLS-11`); esta decisão passa a
  vincular aquele tíquete.
- **`DLS-4`** — Drift na execução **não para o loop**. O loop carrega o drift até o marco; o marco
  adjudica. Recusa faz as tarefas retroagirem ao ponto do drift — não cancela o plano.
- **`DLS-5`** — O Marco 1 **deste** plano não tem o ramo `cancelled`: `no-go` reautora o modelo. O
  gate do `P-0745` será corrigido na mesma forma pela `LST-T6`.
- **`DLS-6`** — Trabalho na branch `plan/planner-modelo-escopo`, a mesma do `P-0745`, porque a
  `LST-T6` entrega dentro daquele plano. Merge em `main` é ato do dono.
- **`DLS-7`** — O modelo da `## 1` foi escrito pela **sessão de planejamento**, e não pelo
  `pantonic-model-designer`, cujo prompt codifica o conceito que este plano substitui — pedir a ele
  reproduziria o defeito. É exceção **de um ato**, registrada aqui, e caduca com a `LST-T5`: a
  partir dali o modelador volta a ser autor único, já sob o conceito revisado.

## 4.1 Decisões acrescentadas na publicação

- **`DLS-8`** — **Revogada em 2026-09-21, sem nunca ter sido exercida.** Ela abria exceção ao gate
  de orquestração para despachar a `LST-T0` com `modelo.py check` em exit `1`. A reautoria do
  modelo apagou a causa: o `check` sobre este plano passou a sair `0` por si (`F-10`), e não há
  gate vermelho a excetuar. O gate vale sem exceção desde a primeira tarefa.
- **`DLS-9`** — **O modelo foi reautorado sob a leitura do dono, não emendado.** O `no-go` do
  Marco 1 (`F-11`) não pediu ajuste de redação: pediu outra decomposição do mesmo enunciado — um
  objeto, as restrições, e tudo o mais como propriedade dele. A versão 1 nunca vigorou, então foi
  substituída no lugar, e o ditado da recusa entrou na `## 0` como lastro da versão 2. O plano
  **não** é cancelado (`DLS-5`), e volta ao Marco 1 para o veredito sobre a versão 2.
- **`DLS-11`** — **A restrição de atualização saiu do modelo, e o que ela entregaria virou o
  `TK-70`.** Correção do dono ao ler a versão 2 (`F-13`): vigência bilateral e conduta de drift
  aparecem na `## 0` a título de conversação, e conversa não é lastro. Pela `DLS-2` o conteúdo não
  fica proibido de existir — só de participar **deste** contrato; e pelo `I-4` achado fora de
  escopo vira tíquete, nunca tarefa deste plano. A `LST-T2` e a `LST-T4` saem da fila inteiras, com
  seus dossiês, para o `TK-70`. As `DLS-3` e `DLS-4`, que decidiam sobre drift e vigência, deixam
  de vincular este plano e passam a vincular o `TK-70` — inclusive a correção pendente do
  `TK-69` §2.
- **`DLS-12`** — **A declaração de lastro tem residência publicada, e o instrumento afere
  presença, não semântica.** Reparo do `AE-1` pelo consultor, em 2026-09-21. A residência é
  tripla — sexta coluna na tabela de `### 1.1`, quarto campo na linha de máquina de `### 1.2`,
  quarta coluna na tabela de `### 1.3` —, publicada pela `LST-T8` na gramática, sem tocar
  `GOVERNANCA.md`, cuja norma a `LST-T1` já fechou. **O que o `check` afere é a coluna de
  `### 1.1`**, não vazia por linha; o campo de `### 1.2` e a coluna de `### 1.3` são lidos quando
  existem, e a falta deles não é violação enquanto o modelo vigente deste plano não os declarar
  (`AE-6`). A pertinência do trecho citado continua sendo guarda do Marco (`F-12`). E a violação
  nova **não alcança plano em status terminal**: é a *Retroatividade* de `GOVERNANCA.md` §3.2
  aplicada — nenhum plano é migrado. Razão medida da regra por status: nenhuma regra de **conteúdo**
  separa o `P-0745`, que tem de falhar, do `P-0743`, que tem de passar pelo `I-2`, porque nenhum dos
  dois declara lastro em lugar algum (`F-14`); o status os separa (`F-15`).
- **`DLS-13`** — **A metade de ator da `OP-5` não se constrói, e a emenda do modelo foi devolvida ao
  modelador.** Medição do `F-14`: a regra reprovaria o modelo aceito do `P-0743` e o modelo vigente
  **deste** plano. Como isso muda o que o plano entrega, o consultor devolveu em 2026-09-21 o dossiê
  `Ato de modelo` de **emenda** (`GOVERNANCA.md` §3.2) — quem escreve na `## 1` é o
  `pantonic-model-designer`, e quem o despacha é quem conduz a sessão. A versão 4 nasce **pendente**,
  como `## 1A`, e o **Marco 2** adjudica; até lá o texto vigente da `OP-5` permanece no card da
  `LST-T5` com o recorte declarado. O `I-1` não é violado: nenhuma **tarefa** toca a `## 1`.
- **`DLS-14`** — **Aceite de card de classe `redacao` é recorte de literal, não contagem de
  palavra.** Reparo do `AE-2`. Toda verificação por contagem (`grep -ci '<palavra>'`) dos cards
  ainda não executados foi substituída por `grep -cF '<literal prescrito no card>'`, com o literal
  fixado no próprio card, e por par presença-ausência onde o texto antigo desaparece (`LST-T8`,
  Verificações 2 e 4). A `LST-T1` **não se refaz**: a entrega dela foi julgada boa e aceita com
  ressalva, e o que o laudo revelou é defeito de **aceite**, não de texto — refazê-la custaria mais
  do que corrigir a régua daqui para a frente. A promoção desta régua à doutrina do kit é matéria de
  tíquete, não deste plano (`I-4`).
- **`DLS-15`** — **Residência se identifica por rótulo, não por posição nem por número — e o
  rótulo casa por prefixo.** Reparo do `AE-9`, do `AE-10` e do `AE-11` pelo consultor, em
  2026-09-22, numa decisão só porque os três são a mesma pergunta. Duas aplicações: **(a)** a coluna
  de lastro de `### 1.1` é a sexta, e é reconhecida pelo cabeçalho que **começa com** `lastro` — o
  autor qualifica a âncora (`lastro na §0`, `lastro no prompt`) sem sair da forma; **(b)** a
  residência do requisito secundário é **seção de nível 2 nomeada `Requisitos secundários`**, em
  qualquer posição do plano, e não o número `## 2`. Razão medida, a mesma nos dois casos: a forma
  publicada não pode exigir do corpus vivo o que ele não tem e não pode ser levado a ter — a única
  instância viva da sexta coluna escreve `lastro na §0` na `## 1` **vigente** deste plano, que só
  se altera por versão adjudicada em marco (e o marco vem **depois** da `LST-T5`, o que reproduziria
  a circularidade do `AE-5`); e `## 2` já está ocupado por *Fatos estabelecidos* no `P-0743` e no
  `P-0745`, que a cláusula de retroatividade da própria `LST-T8` proíbe migrar. Consequência de
  rota: **nenhum dossiê de ato de modelo nesta rodada** — quem se ajusta é a gramática, não o
  modelo; e a aferição da `LST-T5` é de cabeçalho **por prefixo**, nunca por igualdade literal.
- **`DLS-16`** — **A emenda de modelo desta janela se acumula na versão 4 pendente, no lugar, e
  o Marco 2 adjudica uma versão só.** Decisão do consultor em 2026-09-22, no terceiro
  escalonamento. Razão **mecânica**, não de gosto: a `V20` exige que a pendente seja exatamente
  `vigente + 1`, e a vigente é a **3** — uma "versão 5" faria `modelo.py check` sair `1` e travaria
  o despacho. Como a versão 4 **não vigorou**, ela se reescreve no lugar, pelo mesmo princípio que a
  `DLS-9` aplicou à versão 1. Consequência: o dossiê desta rodada corrige as linhas `tarefas:` da
  `## 1A` (`AE-12`) e nada mais; o drift entre a `## 1` vigente e a `## 1A` é o que o dono lê no
  Marco 2, como a norma prevê.
- **`DLS-17`** — **Regra nova migra o corpus que a afere; a exceção continua sendo uma só.**
  Decisão do consultor em 2026-09-22, no quarto escalonamento (`AE-14`). **(a)** As fixtures do
  vocabulário existente **passam a falar a forma publicada** — ganham a coluna de lastro em
  `### 1.1` —, porque fixture que não fala a forma vigente deixa de isolar a regra que ela pina: o
  próprio `test_tf_check_invalido_lista_catorze_violacoes_na_ordem` é construído com todo o resto
  válido *"para que só as catorze violações-alvo"* disparem. **O invariante do reparo é que nenhum
  valor de asserção existente mude**: 14 continuam 14, na mesma ordem, e `fluxo-valido.md` continua
  `modelo: OK`. A cláusula original do card — *as fixtures do `V1`..`V20` não se alteram* — proibia
  **enfraquecer** a cobertura, e é isso que segue proibido; migrar a forma não é enfraquecer.
  **(b)** Fica **recusado** o segundo critério de exceção. A violação nova tem um único recorte, o
  status terminal (`DLS-12`): exceção por caminho de fixture — ou por status ilegível — ensinaria o
  instrumento a mentir e viraria porta de saída para qualquer modelo. Medido em 2026-09-22: as sete
  fixtures com `### 1.1` leem `status='in-progress'` pelo mesmo `_parse_plano` do `check`, então
  estão **dentro** do alcance, e é assim que tem de ser.
- **`DLS-18`** — **A metade `V2` da `OP-5` sai do modelo por falta de lastro, e o conteúdo vira o
  `TK-71`.** Decisão do consultor em 2026-09-22, no quinto escalonamento (`AE-15`), aplicando ao
  próprio plano a regra que ele institui. Medido na `## 0`: o enunciado fala de **elemento** sem
  lastro — *"podem entrar como requisitos não-fundamentais, mas são de responsabilidade inteira do
  agente idear, executar e garantir"* —, que é o lastro da `OP-4` e se materializou na seção
  nomeada do plano (`LST-T3`). **Não há, em trecho algum do enunciado, pedido de que o instrumento
  reconheça uma tarefa que se declara não fundamental**: essa metade da `OP-5` desce do `F-10`, que
  é medição do instrumento, e medição de instrumento não é âncora. É a terceira vez que a regra de
  lastro recorta este plano — a primeira foi do dono (`F-13`, `DLS-11`), a segunda por
  inexequibilidade medida (`AE-4`, `DLS-13`) —, e é o mesmo ato. Consequências: a metade sai da
  `OP-5` e da linha de estado da propriedade de aferição, por emenda acumulada na versão 4 pendente
  (`DLS-16`); o conteúdo vira o **`TK-71`**, aberto no mesmo ato para que a rota não fique órfã
  (`I-4`, lição do `AE-11`); e a `LST-T5` fica com a `V21`, cuja forma está publicada, cujo corpus
  está decidido (`DLS-17`) e cujo recorte está fechado (`DLS-12`, `DLS-15`). O que o plano promete
  — o instrumento recusar o que o dono recusou (`F-6`) — fica **inteiro**.
- **`DLS-10`** — **A `LST-T0` foi dissolvida, e não adiada.** As duas razões dela caíram por
  medição, não por opinião: a `V9` deixou de acusar sozinha com o modelo bem decomposto (`F-10`),
  e relaxá-la passaria a aceitar exatamente o modelo que o dono recusou; a `V2` continua sem
  conhecer a tarefa de requisito não fundamental, e essa correção é conteúdo da `LST-T5`, que já
  toca as mesmas duas residências. Nenhum card do plano fica sem operação do modelo.

## 5. Tarefas

Toda tarefa materializa operação do modelo, na ordem das operações. Uma exceção de arranjo, não de
princípio: a `LST-T1` materializa `OP-1` e `OP-2` — as duas leituras entram no mesmo parágrafo da
norma —, e a `LST-T8` volta às mesmas duas operações para publicar a **forma** que a `LST-T1` deixou
sem residência (`AE-1`): a norma diz que todo elemento tem lastro declarado, e a gramática precisa
dizer em que célula ele se declara. O mapa abaixo é índice; o dossiê fechado de cada card vem em seguida, e é dele que o
executor trabalha.

| tarefa | operação | objetivo em uma linha | residências |
|---|---|---|---|
| `LST-T1` | `OP-1`, `OP-2` | as restrições de leitura de lastro e de leitura de prompt entram na norma e na gramática | `GOVERNANCA.md` §3.2; skill `diario-de-obras` |
| `LST-T7` | `OP-3` | a restrição de decomposição em objeto e propriedade entra na norma e na gramática | `GOVERNANCA.md` §3.2; skill `diario-de-obras` |
| `LST-T3` | `OP-4` | a seção de requisitos secundários vira forma publicada do plano | skill `diario-de-obras` |
| `LST-T8` | `OP-1`, `OP-2` | a gramática publica **onde** o lastro se declara: coluna em `### 1.1`, campo em `### 1.2`, coluna em `### 1.3` | skill `diario-de-obras` |
| `LST-T9` | `OP-1`, `OP-2`, `OP-4` | a doutrina publicada passa a identificar residência por **rótulo**, não por posição nem por número, e o caso medido deixa de comprimir dois fatos | `GOVERNANCA.md` §3.2; skill `diario-de-obras` |
| `LST-T5` | `OP-5` | `modelo.py` passa a acusar elemento do modelo sem lastro declarado, e o `check` sobre o modelo que o dono reprovou deixa de sair `0` | `.claude/tools/modelo.py`; `tests/test_modelo.py`; `tests/fixtures/modelo/` |
| `LST-T6` | `OP-6` | o modelador reautora o modelo do `P-0745` e corrige o gate do Marco 1 dele | `docs/plans/P-0745-planejador-modelo-operacao.md` |

### LST-T1 — O critério de admissão do modelo e as duas vias do enunciado [Opus · esforço high · classe redacao]

- **Status:** `done` · 2026-09-21
- **Depende de:** —
- **Objetivo:** `GOVERNANCA.md` §3.2 e a subseção *Modelo de domínio (seção do plano)* da skill
  `diario-de-obras` passam a exigir lastro declarado para todo objeto, operação e propriedade, e a
  distinguir as duas vias pelas quais o enunciado alimenta o modelo — estado e operação.
- **Fundamento:** `DLS-1`, `DLS-2`; fatos `F-1`, `F-2`, `F-6`, `F-9`; invariantes `I-2`, `I-3`.
- **Operação do modelo:** `OP-1`, `OP-2`
  - OP-1: O redator da norma constrói a restrição de leitura de lastro: todo objeto, operação e propriedade do modelo tem âncora declarada num trecho do enunciado do problema ou do prompt que originou o plano, e elemento sem essa âncora não entra no modelo.
  - precisa de: — a `OP-1` constrói o objeto; não há objeto anterior a consumir
  - OP-2: O redator da norma constrói a restrição de leitura de prompt: o enunciado alimenta o modelo por duas vias declaradas — a via de estado, que popula o estado inicial e o estado final, e a via de operação, que é o que o plano faz diante do vão entre os dois.
  - precisa de: restrições do modelo conceitual — norma em `GOVERNANCA.md` §3.2; forma publicada na subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras`; aferição em `.claude/tools/modelo.py` (`check`), com `tests/test_modelo.py` e fixtures; autoria em `.claude/agents/pantonic-model-designer.md`
- **Camada e fronteira:** doutrina e gramática publicada. Nenhum instrumento, nenhum agente,
  nenhum teste novo — a aferição é da `LST-T5`.
- **Domínio:** *lastro* — a âncora de um elemento do modelo num trecho do enunciado (`## 0`) ou do
  prompt de origem. *Via de estado* — o trecho do enunciado que descreve como as coisas estão ou
  deverão estar; popula `### 1.3`. *Via de operação* — o trecho que pede ação; popula `### 1.2`.
- **Arquivos-alvo:**
  - `GOVERNANCA.md` §3.2 — parágrafo novo imediatamente depois de **Objeto, operação e
    propriedade** e antes de **Estado inicial, estado final e o aceite do plano**
  - `.claude/skills/diario-de-obras/SKILL.md` — subseção *Modelo de domínio (seção do plano)*
- **Verificação:**
  1. ```
     grep -ci 'lastro' GOVERNANCA.md
     ```
     → **≥ 3**. **Medido antes: 0** (`F-9`).
  2. ```
     grep -ci 'lastro' .claude/skills/diario-de-obras/SKILL.md
     ```
     → **≥ 1**. **Medido antes: 0** (`F-9`).
  3. ```
     python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md
     ```
     → exit **0** (`I-2`).
  4. ```
     python -m pytest tests -q
     ```
     → **≥ 262 passed** (`I-3`).
- **Pronto quando:** as quatro verificações imprimem os valores declarados e nenhum arquivo fora dos
  `Arquivos-alvo` foi editado. Por propriedade que a operação altera:
  - `restrições do modelo conceitual.leitura de lastro` — todo objeto, operação e propriedade tem âncora declarada num trecho do enunciado do problema ou do prompt de origem; elemento sem âncora não entra no modelo — Verificação 1 e 2.
  - `restrições do modelo conceitual.leitura de prompt` — o enunciado alimenta o modelo por duas vias declaradas: estado, que popula o inicial e o final, e operação, que é o que o plano faz diante do vão entre os dois — Verificação 1 e 2.
- **Fora do escopo desta tarefa:** a restrição de decomposição (`LST-T7`), a residência do
  requisito secundário (`LST-T3`), o instrumento (`LST-T5`). A vigência bilateral e o drift saíram
  do plano na versão 3 do modelo e viraram o `TK-70` (`DLS-11`).

### LST-T7 — A restrição de decomposição: o que é objeto e o que é propriedade [Opus · esforço high · classe redacao]

- **Status:** `done` · 2026-09-22
- **Depende de:** `LST-T1`
- **Objetivo:** `GOVERNANCA.md` §3.2 e a subseção *Modelo de domínio (seção do plano)* da skill
  `diario-de-obras` passam a declarar como o enunciado se decompõe antes de virar modelo: o que o
  plano constrói é **objeto**; o que converge de um estado a outro é **propriedade** dele;
  descrição de estado não vira objeto próprio; e operação é o ato que altera propriedade.
- **Fundamento:** `DLS-9`; fatos `F-11`, `F-12`. Card autorado na republicação: a versão 1 do
  modelo **deste** plano é o caso medido do defeito que a restrição proíbe.
- **Operação do modelo:** `OP-3`
  - OP-3: O redator da norma constrói a restrição de decomposição: o enunciado se decompõe primeiro em objeto e propriedade — o que o plano constrói é objeto, o que converge de um estado a outro é propriedade dele — e descrição de estado nunca vira objeto próprio.
  - precisa de: restrições do modelo conceitual — norma em `GOVERNANCA.md` §3.2; forma publicada na subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras`; aferição em `.claude/tools/modelo.py` (`check`), com `tests/test_modelo.py` e fixtures; autoria em `.claude/agents/pantonic-model-designer.md`
- **Camada e fronteira:** doutrina e gramática publicada. Nenhum instrumento, nenhum agente,
  nenhum teste novo — a restrição desta tarefa é de julgamento do autor do modelo, e a `LST-T5`
  **não** a torna aferível: não há como um `check` decidir se um substantivo do enunciado é objeto
  ou propriedade. A guarda dela é o Marco, não o instrumento.
- **Domínio:** *objeto* — o que o plano constrói ou torna conforme, e que não existia ou não estava
  conforme quando o plano começou. *Propriedade* — a dimensão do objeto que tem estado inicial e
  estado final distintos. *Promoção indevida* — propriedade escrita como objeto próprio, o defeito
  que infla a tabela `### 1.1` e que o dono recusou duas vezes em 2026-09-21 (`F-11`).
- **Arquivos-alvo:**
  - `GOVERNANCA.md` §3.2 — parágrafo novo imediatamente depois do que a `LST-T1` acrescentou
  - `.claude/skills/diario-de-obras/SKILL.md` — subseção *Modelo de domínio (seção do plano)*
- **Literais obrigatórios (verbatim, não parafrasear):** o card fixa o recorte que a norma tem de
  conter, e a prosa em volta é autoria do executor (`DLS-14`). São três: em `GOVERNANCA.md`,
  `o que o plano constrói é objeto` e `promoção indevida`; na skill, `descrição de estado não vira
  objeto próprio`.
- **Verificação:**
  1. ```
     grep -cF 'o que o plano constrói é objeto' GOVERNANCA.md
     ```
     → **≥ 1**. **Medido antes: 0** (2026-09-21).
  2. ```
     grep -cF 'promoção indevida' GOVERNANCA.md
     ```
     → **≥ 1**. **Medido antes: 0** (2026-09-21).
  3. ```
     grep -cF 'descrição de estado não vira objeto próprio' .claude/skills/diario-de-obras/SKILL.md
     ```
     → **≥ 1**. **Medido antes: 0** (2026-09-21).
  4. Par presença-ausência sobre o texto: a norma dá, por literal, o teste que separa os dois —
     objeto é o que o plano constrói, propriedade é o que converge — e nomeia a promoção indevida
     como defeito, citando o caso medido do `F-11`.
  5. ```
     python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md
     ```
     → exit **0** (`I-2`).
  6. ```
     python -m pytest tests -q
     ```
     → **≥ 262 passed** (`I-3`).
- **Nota de aceite (`F-16`):** use `grep -cF` (literal, sensível a maiúscula) — neste ambiente
  `grep -ciF` **aborta** com exit `134`. Contagem de ocorrência da palavra **não** é aceite: o
  defeito medido na `LST-T1` é que `grep -ci 'lastro'` sairia verde com três menções decorativas
  (`AE-2`, `DLS-14`).
- **Pronto quando:** as seis verificações saem nos valores declarados e nenhum arquivo fora dos
  `Arquivos-alvo` foi editado. Por propriedade que a operação altera:
  - `restrições do modelo conceitual.decomposição em objeto e propriedade` — o enunciado se decompõe primeiro em objeto e propriedade: o que o plano constrói é objeto, o que converge de um estado a outro é propriedade dele, e descrição de estado não vira objeto próprio — Verificação 1, 2, 3 e 4.
- **Fora do escopo desta tarefa:** as leituras de lastro e de prompt (`LST-T1`, já fechadas); a
  residência do requisito secundário (`LST-T3`); o instrumento (`LST-T5`); reescrever o modelo do
  `P-0745` (`LST-T6`); a vigência e o drift, que saíram do plano no `TK-70` (`DLS-11`).

### LST-T3 — A residência do requisito secundário [Opus · classe redacao]

- **Status:** `done` · 2026-09-22
- **Depende de:** `LST-T7`
- **Objetivo:** a gramática publicada do plano ganha a seção **Requisitos secundários** — onde o
  elemento sem lastro fica visível ao dono sem participar do contrato, com a responsabilidade
  declarada como inteira do agente.
- **Fundamento:** `DLS-2`; fatos `F-1`, `F-9`. Precedente de forma: a `## 2` **deste** plano, que
  já é a primeira aplicação da residência.
- **Operação do modelo:** `OP-4`
  - OP-4: O redator da gramática constrói a restrição de decomposição de requisitos funcionais e não funcionais: o elemento com lastro é funcional e entra no modelo como contrato; o elemento sem lastro é não fundamental, reside em seção nomeada do plano fora do modelo, fica transparente para o dono e tem responsabilidade inteira do agente.
  - precisa de: restrições do modelo conceitual — norma em `GOVERNANCA.md` §3.2; forma publicada na subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras`; aferição em `.claude/tools/modelo.py` (`check`), com `tests/test_modelo.py` e fixtures; autoria em `.claude/agents/pantonic-model-designer.md`
- **Camada e fronteira:** gramática publicada. Nenhum instrumento — a `LST-T5` não afere esta
  seção, só a ausência de elemento sem lastro **dentro** do modelo.
- **Domínio:** *requisito secundário* — entrega que o agente julga necessária e que o enunciado não
  pediu. *Transparente* — visível ao dono e declarada, **não** submetida a aprovação dele.
- **Arquivos-alvo:**
  - `.claude/skills/diario-de-obras/SKILL.md` — subseção da gramática do plano
- **Literais obrigatórios (verbatim, não parafrasear):** na skill, `Requisitos secundários` (o
  nome da seção, como a gramática o publica) e `não entra no modelo e não é aferido por lastro`
  (`DLS-14`).
- **Verificação:**
  1. ```
     grep -cF 'Requisitos secundários' .claude/skills/diario-de-obras/SKILL.md
     ```
     → **≥ 1**. **Medido antes: 0** (2026-09-21; `F-9` mediu 0 para a família da palavra).
  2. ```
     grep -cF 'não entra no modelo e não é aferido por lastro' .claude/skills/diario-de-obras/SKILL.md
     ```
     → **≥ 1**. **Medido antes: 0** (2026-09-21). É o literal que separa a seção nova do modelo:
     sem ele, a gramática nomearia a seção sem dizer que ela fica fora do contrato.
  3. Par presença-ausência sobre a forma: a seção é declarada **fora** da `## 1` — a gramática diz,
     por literal, que elemento da seção de requisitos secundários não entra no modelo e não é
     aferido por lastro.
  4. ```
     python -m pytest tests -q
     ```
     → **≥ 262 passed** (`I-3`).
- **Nota de aceite (`F-16`):** `grep -cF`, nunca `grep -ciF` (aborta, exit `134`).
- **Pronto quando:** as quatro verificações saem nos valores declarados. Por propriedade:
  - `restrições do modelo conceitual.decomposição de requisitos funcionais e não funcionais` — o elemento com lastro é funcional e entra no modelo; o sem lastro reside em seção nomeada fora do modelo, transparente ao dono e sob responsabilidade inteira do agente — Verificação 1 e 2.
- **Fora do escopo desta tarefa:** `GOVERNANCA.md` (fechado nas `LST-T1` e `LST-T7`), o instrumento
  (`LST-T5`), e a residência da declaração de lastro na tabela de gramática (`LST-T8`, a tarefa
  seguinte, que edita a mesma subseção) — as duas não se misturam no mesmo card.

### LST-T8 — A residência da declaração de lastro na gramática [Opus · esforço high · classe redacao]

- **Status:** `done` · 2026-09-22
- **Depende de:** `LST-T3`
- **Objetivo:** a gramática legível por máquina da subseção *Modelo de domínio (seção do plano)*
  passa a dizer **onde** o lastro se declara — sexta coluna na tabela de `### 1.1`, quarto campo na
  linha de máquina de `### 1.2`, quarta coluna na tabela de `### 1.3` —, a separar o que o
  instrumento afere do que o Marco guarda, e a declarar a retroatividade: plano em status terminal
  não se migra.
- **Fundamento:** `AE-1`, `DLS-12`, `DLS-14`; fatos `F-14`, `F-15`, `F-16`, `F-17`; invariantes
  `I-2`, `I-3`. Card autorado no reparo de escalonamento de 2026-09-21: a `LST-T1` instituiu a
  exigência de lastro sem publicar residência, e a `LST-T5` não tem campo cuja presença aferir
  enquanto a residência não existir.
- **Operação do modelo:** `OP-1`, `OP-2`
  - OP-1: O redator da norma constrói a restrição de leitura de lastro: todo objeto, operação e propriedade do modelo tem âncora declarada num trecho do enunciado do problema ou do prompt que originou o plano, e elemento sem essa âncora não entra no modelo.
  - precisa de: — a `OP-1` constrói o objeto; não há objeto anterior a consumir
  - OP-2: O redator da norma constrói a restrição de leitura de prompt: o enunciado alimenta o modelo por duas vias declaradas — a via de estado, que popula o estado inicial e o estado final, e a via de operação, que é o que o plano faz diante do vão entre os dois.
  - precisa de: restrições do modelo conceitual — norma em `GOVERNANCA.md` §3.2; forma publicada na subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras`; aferição em `.claude/tools/modelo.py` (`check`), com `tests/test_modelo.py` e fixtures; autoria em `.claude/agents/pantonic-model-designer.md`
  - **Afastamento declarado:** a linha `tarefas:` da `OP-1` e da `OP-2` no modelo **vigente** ainda
    lista só a `LST-T1`. A inclusão da `LST-T8` está no dossiê `Ato de modelo` de emenda devolvido
    em 2026-09-21 (`DLS-13`) e vigora com o aceite do Marco 2 — nenhuma tarefa escreve na `## 1`
    (`I-1`).
- **Camada e fronteira:** gramática publicada, **um arquivo**. Nenhuma edição de `GOVERNANCA.md` — a
  norma já diz que todo elemento tem lastro declarado (`LST-T1`) e que a gramática lida pelo
  instrumento mora na skill; esta tarefa publica a **forma**, não a regra. Nenhum instrumento e
  nenhum teste novo: ensinar o parser é da `LST-T5`, que vem em seguida e já encontra a forma
  publicada — a ordem é deliberada (`F-17`).
- **Domínio:** *residência da declaração* — a célula exata, na forma do plano, em que o autor do
  modelo escreve a âncora de um elemento. *Aferível* — o que o `check` mede é **presença de
  declaração não vazia**; a pertinência do trecho citado é juízo do Marco (`F-12`).
- **Arquivos-alvo:**
  - `.claude/skills/diario-de-obras/SKILL.md` — subseção *Modelo de domínio (seção do plano)*:
    linhas `objetos`, `operações` e `estado` da tabela de gramática, mais o parágrafo
    **Lastro, por elemento** que a `LST-T1` acrescentou
- **Forma prescrita (literal, não parafrasear):**
  - linha `objetos`: a tabela passa a `\| objeto \| o que é \| propriedades \| contrato \| origem \| lastro \|`,
    e `<lastro>` é o trecho do enunciado (`## 0`) ou do prompt de origem, citado ou apontado, não vazio
  - linha `operações`: a linha de máquina da operação admite um quarto campo, ` · ` + `` `lastro: <trecho>` ``,
    depois de `tarefas:` — **opcional na forma, obrigatório na doutrina** enquanto o acervo vivo não
    o declara (`F-14`)
  - linha `estado`: a tabela passa a `\| propriedade \| estado inicial \| estado final \| lastro \|`
  - o parágrafo de lastro ganha, verbatim, a frase `plano em status terminal não se migra`, e diz
    qual metade é de máquina: o `check` afere presença da coluna de `### 1.1`; o restante é guarda
    do Marco
- **Verificação:**
  1. ```
     grep -cF '\| contrato \| origem \| lastro \|`' .claude/skills/diario-de-obras/SKILL.md
     ```
     → **≥ 1**. **Medido antes: 0** (2026-09-21).
  2. ```
     grep -cF '\| contrato \| origem \|`' .claude/skills/diario-de-obras/SKILL.md
     ```
     → **0** — a forma de cinco colunas **desaparece**. **Medido antes: 1**. Com a Verificação 1,
     é par presença-ausência: as duas leituras dão resultados diferentes sobre o mesmo arquivo.
  3. ```
     grep -cF '\| propriedade \| estado inicial \| estado final \| lastro \|`' .claude/skills/diario-de-obras/SKILL.md
     ```
     → **≥ 1**. **Medido antes: 0** (2026-09-21).
  4. ```
     grep -cF '\| propriedade \| estado inicial \| estado final \|`' .claude/skills/diario-de-obras/SKILL.md
     ```
     → **0** — a forma de três colunas desaparece. **Medido antes: 1**. Par com a Verificação 3.
  5. ```
     grep -cF '`lastro:' .claude/skills/diario-de-obras/SKILL.md
     ```
     → **≥ 1** — o quarto campo da linha de máquina de `### 1.2` está publicado. **Medido antes: 0**.
  6. ```
     grep -cF 'plano em status terminal não se migra' .claude/skills/diario-de-obras/SKILL.md
     ```
     → **≥ 1**. **Medido antes: 0** (2026-09-21).
  7. ```
     python .claude/tools/modelo.py check --plano docs/plans/P-0746-lastro-do-modelo.md
     ```
     → exit **0** — publicar a forma não derruba o modelo deste plano, cuja `### 1.1` já usa a sexta
     coluna. **Medido antes: exit 0**, `modelo: OK — 6 operações, 1 objetos, 6 propriedades, 5
     tarefas, versão 3` (2026-09-21; a contagem de tarefas sobe para 6 com este card).
  8. ```
     python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md
     ```
     → exit **0** (`I-2`).
  9. ```
     python -m pytest tests -q
     ```
     → **≥ 262 passed** (`I-3`).
- **Nota de aceite (`F-16`):** `grep -cF`, nunca `grep -ciF` — neste ambiente o segundo **aborta**
  com exit `134`. As Verificações 2 e 4 esperam `0` e **não** são erro de comando: o `grep` sai `1`
  quando não acha, e é isso que se quer.
- **Pronto quando:** as nove verificações saem nos valores declarados, com os dois pares
  presença-ausência discriminando, e nenhum arquivo fora do alvo foi editado. Por propriedade que a
  operação altera:
  - `restrições do modelo conceitual.leitura de lastro` — a âncora deixa de ser exigência sem lugar: a forma publicada diz em que célula cada elemento declara a sua — Verificação 1, 2, 5 e 6.
  - `restrições do modelo conceitual.leitura de prompt` — as duas vias ganham residência na forma: a via de estado declara lastro na tabela de `### 1.3`, a via de operação no quarto campo de `### 1.2` — Verificação 3, 4 e 5.
- **Fora do escopo desta tarefa:** ensinar o parser a ler os campos novos e acusar ausência deles
  (`LST-T5`); reescrever `### 1.1`, `### 1.2` ou `### 1.3` **deste** plano (`I-1` — é ato do
  modelador sob dossiê); migrar plano algum à forma nova (`GOVERNANCA.md` §3.2, *Retroatividade*);
  a seção de requisitos secundários (`LST-T3`, já fechada).

### LST-T9 — A residência se identifica por rótulo, e o caso medido se desfaz em dois [Opus · esforço high · classe redacao]

- **Status:** `done` · 2026-09-22
- **Depende de:** `LST-T8`
- **Objetivo:** três frases já publicadas pela doutrina deste plano passam a bater com o corpus
  vivo: a coluna de lastro de `### 1.1` é reconhecida pelo cabeçalho que **começa com** `lastro`, a
  residência do requisito secundário é **seção nomeada**, em qualquer posição do plano, e o caso
  medido da promoção indevida em `GOVERNANCA.md` §3.2 deixa de comprimir duas recusas sobre modelos
  distintos numa recusa só.
- **Fundamento:** `DLS-15`; achados `AE-7`, `AE-9`, `AE-10`, `AE-11`; fatos `F-1`, `F-11`, `F-16`;
  invariantes `I-2`, `I-3`. Card autorado no segundo reparo de escalonamento, em 2026-09-22: as
  três frases nasceram corretas em intenção e erradas em confronto com o acervo — nenhuma entrega
  anterior é rebaixada por isto.
- **Operação do modelo:** `OP-1`, `OP-3`, `OP-4`
  - OP-1: O redator da norma constrói a restrição de leitura de lastro: todo objeto, operação e propriedade do modelo tem âncora declarada num trecho do enunciado do problema ou do prompt que originou o plano, e elemento sem essa âncora não entra no modelo.
  - precisa de: — a `OP-1` constrói o objeto; não há objeto anterior a consumir
  - OP-3: O redator da norma constrói a restrição de decomposição: o enunciado se decompõe primeiro em objeto e propriedade — o que o plano constrói é objeto, o que converge de um estado a outro é propriedade dele — e descrição de estado nunca vira objeto próprio.
  - precisa de: restrições do modelo conceitual — norma em `GOVERNANCA.md` §3.2; forma publicada na subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras`; aferição em `.claude/tools/modelo.py` (`check`), com `tests/test_modelo.py` e fixtures; autoria em `.claude/agents/pantonic-model-designer.md`
  - OP-4: O redator da gramática constrói a restrição de decomposição de requisitos funcionais e não funcionais: o elemento com lastro é funcional e entra no modelo como contrato; o elemento sem lastro é não fundamental, reside em seção nomeada do plano fora do modelo, fica transparente para o dono e tem responsabilidade inteira do agente.
  - precisa de: restrições do modelo conceitual — norma em `GOVERNANCA.md` §3.2; forma publicada na subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras`; aferição em `.claude/tools/modelo.py` (`check`), com `tests/test_modelo.py` e fixtures; autoria em `.claude/agents/pantonic-model-designer.md`
  - **Nota de leitura:** o texto da `OP-4` já dizia **seção nomeada**; o que divergiu foi a
    gramática, que a publicou por número. Esta tarefa alinha a forma ao texto da operação — não o
    contrário.
  - **Retificado em 2026-09-22 pelo consultor (`AE-13`), depois da entrega:** o card foi despachado
    citando `OP-1`, `OP-2` e `OP-4`. A terceira frase vive no parágrafo da **decomposição** de
    `GOVERNANCA.md` §3.2 — residência de `decomposição em objeto e propriedade` —, então quem ela
    materializa é a **`OP-3`**, não a `OP-2`, que trata das duas vias de leitura e não foi tocada.
    **A entrega não muda e não é rebaixada**: a *Forma prescrita* nomeou o alvo certo e o executor a
    cumpriu literalmente; o que estava errado era a atribuição no card. O dossiê despachado está
    preservado verbatim no RDO da tarefa.
- **Camada e fronteira:** doutrina e gramática publicada, dois arquivos, **três frases**. Nenhum
  instrumento, nenhum agente, nenhum teste novo, nenhuma seção nova: é correção cirúrgica de texto
  já publicado. **Nenhum ato sobre a `## 1` ou a `## 1A`** — a decisão do `DLS-15` é justamente que
  quem se ajusta é a gramática, não o modelo.
- **Domínio:** *rótulo* — o nome pelo qual a forma reconhece uma residência (cabeçalho de coluna,
  nome de seção), por oposição à *posição* (número da coluna, número da seção). *Casar por prefixo*
  — o cabeçalho conforme começa com o rótulo e pode qualificá-lo: `lastro`, `lastro na §0`,
  `lastro no prompt`.
- **Arquivos-alvo:**
  - `.claude/skills/diario-de-obras/SKILL.md` — linha `objetos` da tabela de gramática e os
    parágrafos **Lastro, por elemento** e **Requisito secundário, a residência do elemento sem
    lastro**
  - `GOVERNANCA.md` §3.2 — a frase do caso medido no parágrafo da decomposição
- **Forma prescrita (literal, não parafrasear):**
  - a linha `objetos` e o parágrafo de lastro passam a dizer que a coluna se reconhece pelo
    cabeçalho **`cujo cabeçalho começa com`** `lastro`, admitindo qualificação da âncora; a forma
    canônica da tabela (`\| … \| origem \| lastro \|`) **não muda**
  - o parágrafo do requisito secundário passa a dizer `seção de nível 2 nomeada`
    `Requisitos secundários`, fora da `## 1`, **em qualquer posição do plano** — o número `## 2`
    sai da prescrição, porque `P-0743` e `P-0745` já o usam para *Fatos estabelecidos* e a
    retroatividade publicada proíbe migrá-los
  - a frase do caso medido em `GOVERNANCA.md` §3.2 passa a registrar que as duas recusas de
    2026-09-21 foram sobre **`dois modelos distintos`** — uma sobre o modelo de um plano, outra
    sobre a versão 1 do próprio plano que instituía a regra, esta por quatro propriedades escritas
    como objetos — sem citar identificador de plano, no estilo do parágrafo
- **Verificação:**
  1. ```
     grep -cF 'cujo cabeçalho começa com' .claude/skills/diario-de-obras/SKILL.md
     ```
     → **≥ 1**. **Medido antes: 0** (2026-09-22).
  2. ```
     grep -cF 'afere a presença da coluna `lastro` na tabela de' .claude/skills/diario-de-obras/SKILL.md
     ```
     → **0** — a exigência de igualdade literal desaparece. **Medido antes: 1**. Par com a
     Verificação 1.
  3. ```
     grep -cF 'seção de nível 2 nomeada' .claude/skills/diario-de-obras/SKILL.md
     ```
     → **≥ 1**. **Medido antes: 0** (2026-09-22).
  4. ```
     grep -cF 'seção `## 2. Requisitos secundários` do plano' .claude/skills/diario-de-obras/SKILL.md
     ```
     → **0** — a prescrição por número desaparece. **Medido antes: 1**. Par com a Verificação 3.
  5. ```
     grep -cF 'dois modelos distintos' GOVERNANCA.md
     ```
     → **≥ 1**. **Medido antes: 0** (2026-09-22).
  6. ```
     grep -cF 'o dono recusou duas vezes a versão 1 de um modelo' GOVERNANCA.md
     ```
     → **0** — a frase comprimida desaparece. **Medido antes: 1**. Par com a Verificação 5.
  7. **Não-regressão dos literais já aceitos** (as três tarefas de redação anteriores não se
     desfazem): `grep -cF` devolve **≥ 1** para cada um —
     `o que o plano constrói é objeto` (`GOVERNANCA.md`), `promoção indevida` (`GOVERNANCA.md`),
     `quatro propriedades` (`GOVERNANCA.md`),
     `descrição de estado não vira objeto próprio` (skill), `Requisitos secundários` (skill),
     `não entra no modelo e não é aferido por lastro` (skill),
     `plano em status terminal não se migra` (skill),
     `` \| contrato \| origem \| lastro \|` `` (skill) — e **0** para
     `` \| contrato \| origem \|` `` (skill). Todos medidos nos valores acima em 2026-09-22.
  8. ```
     python .claude/tools/modelo.py check --plano docs/plans/P-0746-lastro-do-modelo.md
     ```
     → exit **0**.
  9. ```
     python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md
     ```
     → exit **0** (`I-2`).
  10. ```
     python -m pytest tests -q
     ```
     → **≥ 262 passed** (`I-3`).
- **Nota de aceite (`F-16`):** `grep -cF`, nunca `grep -ciF` — o segundo **aborta** com exit `134`
  neste ambiente. As Verificações 2, 4 e 6 esperam `0`: o `grep` sai `1` quando não acha, e é isso
  que se quer.
- **Pronto quando:** as dez verificações saem nos valores declarados, com os três pares
  presença-ausência discriminando e a não-regressão intacta, e nenhum arquivo fora dos
  `Arquivos-alvo` foi editado. Por propriedade que a operação altera:
  - `restrições do modelo conceitual.leitura de lastro` — a residência da âncora passa a ser reconhecível no corpus vivo: a coluna se identifica pelo rótulo, e o autor qualifica a âncora sem sair da forma — Verificação 1 e 2.
  - `restrições do modelo conceitual.decomposição em objeto e propriedade` — o caso medido da promoção indevida deixa de comprimir, numa recusa só, duas recusas sobre modelos distintos — Verificação 5 e 6 (`AE-13`: esta linha dizia `leitura de prompt` no card despachado).
  - `restrições do modelo conceitual.decomposição de requisitos funcionais e não funcionais` — a residência do elemento sem lastro é seção nomeada, como a própria operação diz, e não um número de seção já ocupado no acervo — Verificação 3 e 4.
- **Fora do escopo desta tarefa:** tocar a `## 1` ou a `## 1A` deste plano (`I-1`, `DLS-15` — não há
  dossiê nesta rodada); renumerar seção de plano algum; o instrumento (`LST-T5`, a tarefa seguinte,
  que implementa a leitura por prefixo); a `## 2` **deste** plano, cuja citação de operação o
  consultor já corrigiu no próprio ato de reparo (`AE-8`).

### LST-T5 — O instrumento afere lastro declarado [Sonnet · esforço high · classe implementacao]

- **Status:** `done` · 2026-09-22
- **Depende de:** `LST-T9`
- **Objetivo:** `.claude/tools/modelo.py` passa a **ler** os campos de lastro que a `LST-T8`
  publicou e a `LST-T9` acertou e a acusar uma violação nova — elemento do modelo sem lastro
  declarado —, e o `check` sobre o modelo que o dono reprovou deixa de sair `0`. A violação nova
  **não alcança plano em status
  terminal** (`done`, `cancelled`, `superseded`): norma nova não migra plano fechado (`DLS-12`;
  `GOVERNANCA.md` §3.2, *Retroatividade*). No mesmo ato, **o corpus de fixtures passa a falar a
  forma publicada** (`DLS-17`), sem que nenhum valor de asserção existente mude.
- **Fundamento:** `DLS-1`, `DLS-12`, `DLS-13`, `DLS-17`, `DLS-18`; fatos `F-6`, `F-9`, `F-14`,
  `F-15`, `F-16`, `F-17`, `F-18`; achados `AE-14`, `AE-15`; invariantes `I-2`, `I-3`.
- **Operação do modelo:** `OP-5`
  - OP-5: O autor do instrumento faz a conferência automática passar a usar o aparato construído: ela acusa elemento do modelo sem lastro declarado e ator citado no fluxo que não existe entre os objetos, e reconhece a tarefa que declara não materializar operação por ser requisito não fundamental.
  - precisa de: restrições do modelo conceitual — norma em `GOVERNANCA.md` §3.2; forma publicada na subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras`; aferição em `.claude/tools/modelo.py` (`check`), com `tests/test_modelo.py` e fixtures; autoria em `.claude/agents/pantonic-model-designer.md`
  - **Segundo recorte desta tarefa (`AE-15`, `DLS-18`):** a metade **`V2`** da `OP-5` — *"reconhece
    a tarefa que declara não materializar operação por ser requisito não fundamental"* — **também
    não se constrói**. Medido em 2026-09-22: `requisito não fundamental` tem **0** ocorrências na
    skill `diario-de-obras` e **0** em `GOVERNANCA.md` — a forma textual que o `check` teria de
    reconhecer nunca foi publicada, e o enunciado (`## 0`) não a pede: ele fala de **elemento** sem
    lastro, que é o lastro da `OP-4` e já reside na seção nomeada do plano. A metade sai do modelo
    pela regra que o próprio plano institui e o conteúdo vira o **`TK-71`**. Até o aceite no Marco 2
    o texto vigente da `OP-5` permanece acima, e o recorte fica declarado aqui.
  - **Recorte desta tarefa (`AE-4`, `DLS-13`):** a metade de **ator** da `OP-5` — *"ator citado no
    fluxo que não existe entre os objetos"* — **não se constrói**. Medido em 2026-09-21: ela
    acusaria 6 dos 7 atores do `P-0743`, cujo modelo está aceito e é protegido pelo `I-2`, e 4 dos
    4 atores do modelo **vigente deste plano** (`F-14`) — é traço de estilo comum a todos os
    modelos do kit, não o defeito que o dono recusou. O dossiê `Ato de modelo` de emenda que retira
    a metade foi devolvido em 2026-09-21; até o aceite no Marco 2 o texto vigente permanece acima,
    e o recorte fica **declarado aqui**, não silencioso.
- **Camada e fronteira:** instrumento e testes. Nenhuma edição de doutrina — a `LST-T1`, a `LST-T7`,
  a `LST-T3` e a `LST-T8` já a fecharam; este card só torna aferível a forma que a `LST-T8`
  publicou.
- **Domínio:** *violação* — item do vocabulário fechado do `check` (`V1`..`V20` hoje, `F-4`); a
  nova é a **`V21`**, `objeto sem lastro declarado`, **uma ocorrência por objeto** sem a célula —
  mesma granularidade da `V15` (*objeto sem propriedade*) e da `V7`, para que a contagem de
  violações de uma fixture continue previsível. O lastro é **declarado** pelo autor do modelo, não inferido: o `check`
  afere **presença de declaração não vazia**, nunca a semântica dela (§8, terceiro risco).
  *Status terminal* — `done`, `cancelled` ou `superseded`, lido de `Plano.status` pelo mesmo
  `backlog.py` que o `verbo_check` já carrega (`F-15`); plano nesse estado não é alcançado pela
  violação nova. *Coluna de lastro* — a **sexta** coluna de `### 1.1`, reconhecida pelo cabeçalho
  que **começa com** `lastro` e não por igualdade literal (`DLS-15`, `AE-10`): a única instância
  viva escreve `lastro na §0`, e exigir `lastro` exato reprovaria o modelo vigente deste plano.
- **Linha de base medida em 2026-09-22, na abertura desta tarefa:** `grep -c 'lastro'` devolve
  **0** em `.claude/tools/modelo.py` e **0** em `tests/test_modelo.py`, enquanto a gramática já
  afirma, no presente, que o `check` afere a presença da coluna cujo cabeçalho começa com `lastro`.
  O vão entre a forma publicada e o instrumento é exatamente o conteúdo desta tarefa — e é por isso
  que o aceite dela são **exit codes que mudam sobre arquivo intocado**, não contagem de palavra
  (`DLS-14`).
- **Arquivos-alvo:**
  - `.claude/tools/modelo.py`
  - `tests/test_modelo.py`
  - `tests/fixtures/modelo/` — as sete fixtures que têm `### 1.1` ganham a sexta coluna conforme
    (`fluxo-valido`, `plano-invalido`, `plano-invalido-2`, `fluxo-pendente`, `fluxo-concluido`,
    `plano-sem-cabecalho`, `plano-sem-estado`), e nascem três fixtures novas para a `V21`:
    `plano-sem-lastro.md` (status `in-progress`, sem a coluna), `plano-com-lastro.md` (status
    `in-progress`, com a coluna sob o cabeçalho **`lastro na §0`** — pina o casamento por prefixo
    do `DLS-15` — e com o campo `lastro:` em `### 1.2` e a quarta coluna em `### 1.3`, sendo a
    primeira fixture na forma nova inteira) e `plano-terminal-sem-lastro.md` (status `done`, sem a
    coluna — pina o recorte por status do `DLS-12`)
- **Verificação:**
  1. ```
     python .claude/tools/modelo.py check --plano docs/plans/P-0745-planejador-modelo-operacao.md
     ```
     → exit **1**, acusando a violação nova sobre os elementos sem lastro declarado. **Medido
     antes: exit 0**, com `modelo: OK — 7 operações, 11 objetos, 21 propriedades, 7 tarefas, versão
     1` (`F-6`, reconfirmado em 2026-09-21). É o par presença-ausência central desta tarefa: o
     mesmo arquivo intocado sai `0` antes e `1` depois — o instrumento passa a recusar exatamente o
     que o dono recusou.
  2. ```
     python .claude/tools/modelo.py check --plano docs/plans/P-0746-lastro-do-modelo.md
     ```
     → exit **0** — a `### 1.1` deste plano declara lastro na sexta coluna, uma linha, célula não
     vazia, sob o cabeçalho `lastro na §0` (medido em 2026-09-21 e reconfirmado em 2026-09-22 sobre
     a `## 1` vigente e a `## 1A` pendente). **O casamento de cabeçalho é por prefixo** (`DLS-15`):
     igualdade literal com `lastro` deixaria este plano vermelho e a tarefa sem rota, porque a `## 1`
     vigente só muda por versão adjudicada em marco, e o Marco 2 vem depois desta tarefa. **A aferição de ausência é a coluna de `### 1.1`**: o campo de
     `### 1.2` e a coluna de `### 1.3` são lidos quando existem, e a falta deles ainda **não** é
     violação — o modelo vigente deste plano não os declara, e emendá-lo é ato do modelador, não
     desta tarefa (`I-1`, `AE-6`).
  3. ```
     python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md
     ```
     → exit **0** (`I-2`) — o `P-0743` está `done` e a violação nova não o alcança. **Medido em
     2026-09-21:** `_parse_plano` devolve `status='done'` para o `P-0743`, `'blocked'` para o
     `P-0745` e `'ready'` para o `P-0746` (`F-15`). É por **status**, não por conteúdo, que os dois
     casos se separam: nenhum dos três declarava lastro em `### 1.2`/`### 1.3` (`F-14`), então
     nenhuma regra de conteúdo faria o `P-0745` falhar e o `P-0743` passar.
  4. Par de parser sobre fixture: a linha de máquina de `### 1.2` é lida **com e sem** o quarto
     campo `lastro:`, e a tabela de `### 1.3` com três e com quatro colunas — as duas formas
     produzem o mesmo conjunto de operações e propriedades. Sem isso, o primeiro modelo escrito na
     forma nova deixa de ser lido inteiro e o `check` aprova em silêncio (`F-17`). A fixture da
     forma nova inteira é `plano-com-lastro.md`; a da forma sem os campos opcionais é
     `fluxo-valido.md`, já existente.
  5. **Trio da `V21` sobre fixture nova** — o par presença-ausência da regra, mais a exceção:
     `check` sobre `plano-sem-lastro.md` **acusa** `V21`, uma vez por objeto, e sai `1`; sobre
     `plano-com-lastro.md` **não acusa** e sai `0` — mesmo com o cabeçalho qualificado
     `lastro na §0`, que é o casamento por prefixo do `DLS-15`; sobre
     `plano-terminal-sem-lastro.md`, que não tem a coluna mas está `done`, **não acusa** e sai `0`.
  6. **Não-regressão do corpus existente, por número medido** (`DLS-17`) — depois de as sete
     fixtures ganharem a coluna, `check` devolve exatamente o que devolvia antes:
     `plano-invalido.md` → **10 violações**, `plano-invalido-2.md` → **4**, somando as **14** do
     `test_tf_check_invalido_lista_catorze_violacoes_na_ordem`, **na mesma ordem**;
     `fluxo-valido.md` → `modelo: OK — 3 operações, 4 objetos, 4 propriedades, 3 tarefas, versão 1`;
     `fluxo-concluido.md` → `modelo: OK`; `fluxo-pendente.md` → **4 violações**;
     `plano-sem-cabecalho.md` → **1 violação**; `plano-sem-estado.md` → `modelo: forma anterior`.
     **Todos medidos nesses valores em 2026-09-22, antes da tarefa.** Nenhum valor esperado de
     asserção existente se edita: se algum mudar, a fixture volta ao que era e o achado sobe ao
     consultor — **não** se ajusta o número do teste.
  7. ```
     python -m pytest tests/test_modelo.py -q
     ```
     → **≥ 28 passed**. **Medido antes: 23 passed** (`F-9`) — pelo menos um teste por regra tocada
     e um por fixture nova: acusação da `V21`, não-acusação com cabeçalho qualificado, exceção por
     status terminal, leitura da linha de `### 1.2` com e sem o campo, leitura de `### 1.3` com
     três e com quatro colunas.
  8. ```
     python -m pytest tests -q
     ```
     → **≥ 262 passed** (`I-3`).
- **Pronto quando:** as oito verificações saem nos valores declarados, e a Verificação 1
  discrimina — o mesmo comando dava `0` antes e dá `1` depois, sobre o mesmo arquivo intocado. Por propriedade:
  - `restrições do modelo conceitual.aferição pelos instrumentos` — o `check` acusa elemento sem lastro declarado e, sobre o `P-0745` intocado, passa a sair `1` — Verificação 1, 2, 5, 6 e 7.
- **Fora do escopo desta tarefa:** reescrever o modelo do `P-0745` para fazê-lo passar — isso é a
  `LST-T6`, e antecipá-lo destruiria o par presença-ausência da Verificação 1. **Enfraquecer a
  cobertura do `V1`..`V20`** — editar valor esperado de asserção existente, remover caso ou afrouxar
  fixture para caber na regra nova; o que a cláusula original deste card proibia, e segue proibido.
  O que **não** é enfraquecer, e agora é obrigatório, é migrar as fixtures para a forma publicada
  mantendo todos os números (`DLS-17`, `AE-14`). **Abrir um segundo critério de exceção à `V21`**
  (caminho de fixture, status ilegível ou qualquer outro): o recorte é um só, o status terminal
  (`DLS-12`). **A metade `V2` não se constrói** (`AE-15`, `DLS-18`): implementá-la exigiria publicar uma
  forma de campo de card que nenhuma operação deste plano institui, e o conteúdo é o `TK-71`.
  **A violação de ator não se constrói**
  (`AE-4`, `DLS-13`), e nenhuma doutrina se edita — a residência já foi publicada pela `LST-T8`.

### LST-T6 — A reaplicação ao `P-0745` [Opus · esforço high · classe redacao]

- **Status:** `done` · 2026-09-22
- **Depende de:** `LST-T5`
- **Objetivo:** o modelo do `P-0745` é reautorado sob o conceito revisado — só elementos com lastro
  no enunciado daquele plano, sem propriedade promovida a objeto e sem ator inexistente —, o que
  não tem lastro migra para a seção de requisitos secundários dele, e o gate do Marco 1 dele ganha
  o ramo que faltava.
- **Fundamento:** `DLS-1`, `DLS-2`, `DLS-5`, `DLS-7` (que caduca aqui); fatos `F-1`, `F-2`, `F-3`.
- **Operação do modelo:** `OP-6`
  - OP-6: O modelador reautora o modelo do plano do planejador sob as restrições construídas e o devolve à medição do dono, provando no caso que originou o enunciado que o modelo convergiu de não conforme para conforme.
  - precisa de: restrições do modelo conceitual — norma em `GOVERNANCA.md` §3.2; forma publicada na subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras`; aferição em `.claude/tools/modelo.py` (`check`), com `tests/test_modelo.py` e fixtures; autoria em `.claude/agents/pantonic-model-designer.md`
- **Camada e fronteira:** um plano, e só ele. **Executada pelo `pantonic-model-designer`** — todo
  ato sobre a seção `## 1` de um plano é dele (`F-4`), e a exceção de um ato da `DLS-7` já caducou.
  Nenhuma tarefa do `P-0745` é executada aqui; o plano dele segue `blocked`.
- **Domínio:** o enunciado de lastro é a `## 0` do **`P-0745`**, mais o prompt de origem dele
  (pedido do dono de 2026-09-21 transcrito lá) — **não** a `## 0` deste plano.
- **Arquivos-alvo:**
  - `docs/plans/P-0745-planejador-modelo-operacao.md` — seção `## 1` reautorada; seção nova de
    requisitos secundários; tabela de marcos (ramo `no-go` do Marco 1, pela `DLS-5`)
- **Verificação:**
  1. ```
     python .claude/tools/modelo.py check --plano docs/plans/P-0745-planejador-modelo-operacao.md
     ```
     → exit **0**. **Medido antes desta tarefa: exit 1** (as violações que a `LST-T5` instituiu).
  2. O modelo reautorado declara lastro na sexta coluna de `### 1.1`, uma célula não vazia por
     linha, e todo objeto citado nas linhas de máquina de `### 1.2` existe em `### 1.1` — o que a
     `V5` já afere. **O teste de ator da versão anterior deste card saiu** (`AE-4`, `F-14`): "ator
     citado na prosa que não é objeto" não discrimina — o `P-0743`, cujo modelo está aceito, tem 6
     dos 7 fora da tabela, e o modelo **deste** plano, 4 dos 4. O defeito que o dono recusou no
     `P-0745` é a **promoção indevida** (`F-11`), e a guarda dela é o Marco (`F-12`).
  3. Nenhum dos elementos que o dono nomeou sem lastro permanece em `### 1.1` do `P-0745`; os que
     o plano ainda entrega aparecem na seção de requisitos secundários dele — **seção de nível 2
     nomeada `Requisitos secundários`, em qualquer posição** (`DLS-15`). O `P-0745` já usa `## 2`
     para *Fatos estabelecidos*: a seção nova entra sem renumerar nada, e renumerar está fora de
     escopo.
  4. ```
     grep -c 'cancelled' docs/plans/P-0745-planejador-modelo-operacao.md
     ```
     → o ramo `no-go = cancelled` do Marco 1 não existe mais na tabela de marcos (`DLS-5`).
  5. ```
     python -m pytest tests -q
     ```
     → **≥ 262 passed** (`I-3`).
- **Pronto quando:** as cinco verificações saem nos valores declarados e o plano está pronto para o
  Marco 3 — a nova medição do dono. Por propriedade:
  - `restrições do modelo conceitual.conformidade do modelo` — de não conforme para conforme: o modelo do `P-0745` reautorado sob as restrições construídas e devolvido à medição do dono — Verificação 1, 2 e 3.
- **Fora do escopo desta tarefa:** executar qualquer tarefa do `P-0745`; alterar a `## 0` dele;
  mudar o status dele de `blocked` — quem o destrava é o `go` do dono.

## 6. Invariantes de execução

- **`I-1`** — Nenhuma tarefa deste plano toca a seção `## 1` **deste** plano. Emenda de modelo é ato
  do modelador sob dossiê, e o Marco 1 é do dono. A reautoria de 2026-09-21 (`DLS-9`) não viola o
  invariante: foi ato da sessão de planejamento respondendo ao `no-go`, antes de qualquer tarefa
  ter sido despachada.
- **`I-2`** — `python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md`
  continua saindo `0` ao fim de cada tarefa (`F-5`).
- **`I-3`** — O piso de regressão não reduz: o total de `python -m pytest tests -q` não fica abaixo
  da referência medida na abertura da `LST-T1`.
- **`I-4`** — Achado fora de escopo vira tíquete, nunca tarefa deste plano (`G-PLANFIDELITY`).

## 7. Fora de escopo (explícito)

- **Reescrever o modelo do `P-0745` antes da `LST-T6`** — a ordem é do dono: revisar o conceito
  primeiro, reaplicar depois.
- **Cancelar o `P-0745`** — `F-3`; ele segue `blocked` até a `LST-T6` e a nova medição.
- **A unidade de trabalho e a régua de dimensionamento** — matéria do `P-0745`, intocada aqui.
- **Propagação aos derivados** — hub primeiro, medir, depois propagar; `sync-kit.ps1` inalterado.
- **A vigência bilateral do modelo e a conduta de drift do loop** — saíram na versão 3 por não
  terem lastro no enunciado (`F-13`, `DLS-11`). Matéria do `TK-70`, com os dossiês da `LST-T2` e da
  `LST-T4` preservados lá.

## 8. Riscos

| risco | sinal | resposta |
|---|---|---|
| o modelo deste plano falhar a própria regra — **realizado em 2026-09-21** | o dono apontou quatro propriedades escritas como objetos na `## 1`, versão 1 (`F-11`) | resposta aplicada: `no-go` reautorou o modelo (`DLS-5`, `DLS-9`), o plano não foi cancelado, e o achado virou a `LST-T7` em vez de caso de teste — a `F-12` mostra por que não é aferível por instrumento |
| a regra de lastro engessar o modelo a ponto de ele não descrever a entrega | operação necessária não ter substantivo no enunciado | a operação existe e o elemento vai para requisitos secundários (`DLS-2`); se isso se repetir, é sinal de enunciado incompleto — escala ao dono, não se afrouxa a regra |
| `LST-T5` aferir lastro por casamento literal e produzir falso positivo | violação acusada sobre elemento que o enunciado nomeia por sinônimo | o lastro é **declarado** pelo autor do modelo, não inferido pelo instrumento: o `check` afere presença da declaração, não a semântica dela |

## 9. Achados da execução

> **Encaminhamento do terceiro escalonamento (consultor, 2026-09-22).** `AE-12` e `AE-13` **não
> travam** o despacho da `LST-T5`: nenhum dos dois altera o que o instrumento tem de fazer, nenhum
> muda a forma publicada que ele vai ler, e o `check` sai `0` com as linhas `tarefas:` como estão —
> a `V3` afere que a tarefa citada existe, não que toda tarefa que materializa a operação esteja
> citada. O `AE-12` vai ao modelador **agora**, por dossiê, e não ao relatório: o laudo tem razão em
> que ele morre em silêncio se esperar, e a correção cabe inteira na versão 4 pendente (`DLS-16`). O
> `AE-13` foi retificado pelo consultor no próprio card da `LST-T9`, que é registro fora da `## 1`;
> a entrega não se refaz e não se rebaixa.

> **Encaminhamento do quarto escalonamento (consultor, 2026-09-22).** O `AE-14` é impedimento
> **real** e a parada do executor foi correta: o card prescrevia a regra e proibia tocar o corpus
> que a regra alcança. Decidido no `DLS-17` — o corpus migra, os números não mudam, a exceção
> continua sendo uma só. Card emendado, sem mudança de escopo, de classe nem de modelo: a `LST-T5`
> volta à fila para redespacho em contexto novo. **Nenhum ato sobre a `## 1` ou a `## 1A`.**

> **Encaminhamento do quinto escalonamento (consultor, 2026-09-22).** Classificado **técnico e
> tático**, com a razão dita por inteiro para o dono poder discordar no Marco 2. O `AE-15` é
> procedente e o padrão que ele revela é de **modelo**, não de card: a `OP-5` foi escrita com três
> orações, e duas delas não sobrevivem às regras que este próprio plano institui — a de ator por
> inexequibilidade medida (`AE-4`), a da `V2` por **falta de lastro** (`F-19`). Retirar oração sem
> lastro não é reduzir escopo: é o contrato sendo aplicado, e foi o **dono** quem abriu o precedente
> ao recusar a restrição de atualização por conversação (`F-13`, `DLS-11`). O que o plano promete
> segue inteiro — o instrumento passa a recusar o que o dono recusou (`F-6`). Parar a janela em
> `5/7` deixaria a norma sem aferição, o Marco 2 sem a leitura que ele especifica (*`show` depois da
> `LST-T5`*) e a propriedade de conformidade sem convergir, para decidir o que a regra já decide.
> **A metade `V2` virou o `TK-71`, aberto no mesmo ato** — a lição do `AE-11` é que rota sem card
> que a execute é rota órfã, e isso vale também para rota que sai do plano.

> **Consolidação de rota (consultor, 2026-09-22, plano `7/7`).** Nenhum achado desta janela fica sem
> residência. **Tíquetes abertos no mesmo ato:** `TK-71` (a `V2` e a tarefa que não materializa
> operação — `AE-15`); `TK-72` (régua de autoria de card, quatro pacotes — `AE-2`/`DLS-14`, `AE-11`,
> `AE-19`, `AE-20`); `TK-73` (a oração da operação: recorte e sujeito — `AE-4`, `AE-15`, `AE-18`,
> com o Pacote 2 **bloqueado na decisão do dono**); `TK-74` (`review_evidence.py` e o alvo terminado
> em barra — `AE-22`). **Roteado a tíquete existente:** `AE-21` para o `TK-70` Pacote A, com o caso
> medido apensado lá — a `## 1A` deste plano `pendente` e a `## 1` do `P-0745` `vigente`, mesmo
> estado de fato e valores opostos. **Ao dono, no relatório de encerramento:** (1) o Marco 2, que
> adjudica a versão 4 pendente com os dois recortes da `OP-5`; (2) o Marco 3, a nova medição sobre o
> `P-0745` reautorado; (3) a pendência `AE-18` — o critério de ator inédito, que ele nomeou e o loop
> dispensou por medição, com as duas opções e a recomendação do consultor. Nada disto reabre tarefa
> deste plano.


- **`AE-1`** — **A exigência de lastro foi instituída sem residência publicada na gramática legível
  por máquina.** Achado da `LST-T1` (executor, pendência autoral; laudo, `recomendacao=escalar`,
  `ressalva` 88%, `bloqueante=nenhuma`, 2026-09-21). Medido: a linha `objetos` da subseção *Modelo
  de domínio (seção do plano)* segue declarando **cinco** colunas
  (`| objeto | o que é | propriedades | contrato | origem |`), e nem `### 1.2` nem `### 1.3` ganharam
  campo de âncora — enquanto a `### 1.1` deste próprio plano já usa **seis**, com `| lastro na §0 |`.
  Consequência sobre a rota: a `LST-T5` exige `modelo.py check --plano P-0746` exit `0` aferindo
  **presença da declaração** de lastro, e declara `nenhuma edição de doutrina` — sem a residência
  publicada, não há campo cuja presença aferir. Roteado ao consultor de plano por `B1`.
  **Resolvido em 2026-09-21 pelo consultor: o vão é real e o reparo é card novo.** Nasce a
  `LST-T8`, entre a `LST-T3` e a `LST-T5`, materializando `OP-1` e `OP-2` — as mesmas operações da
  `LST-T1`, agora na camada de **forma** —, e a `LST-T5` passa a depender dela. A `LST-T1` **não**
  se refaz: a doutrina que ela escreveu está correta e aceita; o que faltava era a residência, que
  o card dela explicitamente excluía. A `LST-T5` mantém `nenhuma edição de doutrina` sem vão,
  porque encontra a forma já publicada (`DLS-12`).
- **`AE-2`** — **A verificação da `LST-T1` não discrimina.** Achado de processo do laudo da
  `LST-T1` (2026-09-21): `grep -ci 'lastro' ≥ 3` e `≥ 1` contam ocorrência da palavra e não aferem a
  propriedade que o `Pronto quando` certifica — a linha de aceite sairia verde com três menções
  decorativas. Para card de classe `redacao` sobre norma, o aceite discriminante é **recorte do
  literal da forma publicada**, não contagem. Rota: item de replanejamento do `P-0746`; alcança as
  verificações da `LST-T7` e da `LST-T3`, que têm a mesma forma.
  **Resolvido em 2026-09-21 pelo consultor (`DLS-14`):** as verificações da `LST-T7` e da `LST-T3`
  foram reescritas em `grep -cF` sobre literais que o card prescreve verbatim, medidos em **0**
  antes; a `LST-T8` nasce com dois pares presença-ausência mecânicos (a forma de cinco colunas e a
  de três colunas **desaparecem** da gramática). Generalização à doutrina do kit — régua de aceite
  para card de classe `redacao` — fica como tíquete a abrir no encerramento da janela, por `I-4`.
- **`AE-4`** — **A violação de ator da `OP-5` não é implementável como discriminador.** Achado do
  consultor no reparo de 2026-09-21, por medição (`F-14`): a regra acusaria 6 dos 7 atores do
  `P-0743` — modelo aceito, protegido pelo `I-2` — e 4 dos 4 atores do modelo vigente **deste**
  plano, cuja Verificação 2 da `LST-T5` exige exit `0`. Implementá-la ao pé da letra deixaria o
  `check` vermelho sobre todos os modelos do kit. Rota: a metade de ator sai da `OP-5` por dossiê
  `Ato de modelo` de emenda (`DLS-13`), a `LST-T5` declara o recorte, e a `LST-T6` troca o teste de
  ator pelo de lastro declarado. O defeito que o dono recusou continua coberto — é a promoção
  indevida (`F-11`), matéria da `LST-T7`, com guarda no Marco (`F-12`).
- **`AE-5`** — **Nenhuma regra de conteúdo separa o `P-0745` do `P-0743`.** Medido em 2026-09-21:
  os dois modelos estão no mesmo estado formal quanto a lastro — nenhum o declara (`F-14`) —, e a
  `LST-T5` precisa que o primeiro saia `1` e o segundo continue saindo `0` (`I-2`). O discriminador
  disponível é o **status** do plano, que o instrumento já carrega (`F-15`). Rota: `DLS-12`, com a
  regra ancorada na *Retroatividade* que `GOVERNANCA.md` §3.2 já publica.
- **`AE-6`** — **O modelo deste plano declara lastro por objeto, não por elemento — afastamento
  declarado.** A `### 1.1` traz a sexta coluna com três citações da `## 0`; a `### 1.2` e a
  `### 1.3` não trazem âncora por operação nem por propriedade, enquanto a norma que a `LST-T1`
  publicou exige lastro declarado de **todo** objeto, operação e propriedade. Corrigir isso é ato do
  modelador sobre a `## 1` (`I-1`), e **não pode anteceder** a `LST-T5`: escrever o quarto campo de
  `### 1.2` antes de o parser aprendê-lo faz a operação inteira deixar de ser lida, em silêncio
  (`F-17`). Rota: fica **fora** do dossiê de emenda de 2026-09-21, que só retira a metade de ator, e
  volta como ato de modelo depois do Marco 2. Até lá, a conformidade aferida deste plano é a coluna
  de `### 1.1` (`DLS-12`).
- **`AE-3`** — **Sem ação, reconciliado.** O dossiê de evidência da `LST-T1` marcou
  `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_HISTORICO.md` e `docs/DOC_MAP.md` como fora dos alvos e sem
  atribuição; os três já constavam modificados no `git status` anterior à abertura da janela, e os
  `mtime` (12:54, 19:09, 21:20) precedem os dos dois alvos (21:24). Não é resíduo da tarefa.
- **`AE-7`** — **A frase do caso medido que entrou na norma comprime dois fatos num só.** Achado de
  processo do laudo da `LST-T7` (2026-09-22, veredito `aprovado` 100%, sem rebaixamento de dimensão).
  O campo *Domínio* do card diz que o dono recusou **duas vezes** a **versão 1 de um modelo** por
  promoção indevida, citando só o `F-11`; mas as duas recusas foram sobre modelos **distintos** — o
  `F-1` é o modelo do `P-0745`, o `F-11` é a versão 1 deste plano —, e o recorte *quatro propriedades
  escritas como objetos* é exclusivo do `F-11`. O executor reproduziu a compressão fielmente e ela
  pousou em `GOVERNANCA.md` §3.2, que é doutrina de kit e propaga aos cinco derivados. Rota: card de
  replanejamento do `P-0746` corrige a frase do caso medido na norma. A entrega da `LST-T7` não é
  rebaixada — os três literais obrigatórios estão corretos; o que está impreciso é a moldura factual
  em volta deles.
  **Resolvido em 2026-09-22 pelo consultor:** a correção é o item 3 da `LST-T9`, com par
  presença-ausência medido (`dois modelos distintos` de 0 a ≥1; `o dono recusou duas vezes a versão
  1 de um modelo` de 1 a 0) e não-regressão de `quatro propriedades`.
- **`AE-8`** — **A `## 2` deste plano atribui a residência à operação errada.** Achado de processo do
  laudo da `LST-T3` (2026-09-22, `aprovado` 100%). O cabeçalho da `## 2. Requisitos secundários` diz
  ser *"a primeira aplicação da residência que a `OP-4` institui"* — quem a institui é a **`OP-4`**
  (a entrada do `DOC_MAP` já cita `OP-4` corretamente). O card da `LST-T3` nomeia essa seção como
  *Precedente de forma*, então o executor trabalhou contra um precedente cuja atribuição de operação
  está errada. Rota: item de replanejamento do `P-0746` — corrigir a citação na `## 2` para `OP-4`.
  Fora do `I-1`: a `## 2` não é o modelo.
  **Resolvido em 2026-09-22 pelo consultor, no próprio ato de reparo:** a `## 2` deste plano passou
  a citar a `OP-4`. Nenhum card carrega este item.
- **`AE-9`** — **A gramática nova prescreve um número de seção já ocupado no corpus.** Achado de
  processo do mesmo laudo. O card fixou `## 2` como precedente de forma sem confrontar o corpus: o
  `P-0743` e o `P-0745`, os dois planos vivos que já carregam `## 1. Modelo conceitual` sob esta
  gramática, usam `## 2. Fatos estabelecidos`. A gramática publicada passa a prescrever um número
  ocupado, sem instrumento que o afira (o próprio card declara que a `LST-T5` não afere esta seção) e
  sem cláusula de retroatividade. Rota: a `LST-T8`, que edita a mesma subseção e já declara
  retroatividade, fecha se a residência se identifica **por nome** ou **por número de seção**.
  **Decidido em 2026-09-22 (`DLS-15`): por nome.** A residência é seção de nível 2 nomeada
  `Requisitos secundários`, em qualquer posição do plano. Razão medida: `## 2` está ocupado por
  *Fatos estabelecidos* no `P-0743` e no `P-0745`, e a retroatividade que a `LST-T8` publicou
  proíbe migrá-los — prescrever o número obrigaria a renumerar plano vivo. Executa a `LST-T9`,
  itens 2 (rota do `AE-11` re-declarada).
- **`AE-10`** — **O literal do cabeçalho da sexta coluna não bate com o único plano vivo que a usa.**
  Achado do laudo da `LST-T8` (2026-09-22, `aprovado` 100%, `recomendacao=escalar`). A *Forma
  prescrita* do card fixou o cabeçalho no literal `lastro`; a única instância viva da forma de seis
  colunas — a `### 1.1` da `## 1` (versão 3, vigente) e da `## 1A` (versão 4, pendente) do próprio
  `P-0746` — escreve `lastro na §0`. A justificativa da Verificação 7 (*a `### 1.1` deste plano já
  usa a sexta coluna*) confunde **contagem de colunas** com **literal de cabeçalho**: a contagem
  casa, o literal não. Consequência à frente: a `LST-T5` recebe a aferição de *presença da coluna de
  `### 1.1`* e encontra no corpus vivo um cabeçalho que não é o publicado — o `P-0743` está protegido
  por ser `done` (retroatividade que esta mesma entrega publicou), o `P-0746` não está. A fechar
  **antes** do despacho da `LST-T5`; se a decisão for acertar o cabeçalho do modelo, é ato do
  `pantonic-model-designer` sob dossiê (`I-1`), na mesma passagem que adjudicar a versão 4 no Marco 2.
  **Decidido em 2026-09-22 (`DLS-15`): quem se ajusta é a gramática, não o modelo — sem dossiê.** O
  cabeçalho da sexta coluna casa **por prefixo**, e `lastro na §0` é conforme. A alternativa —
  acertar o cabeçalho na `## 1` — é inexecutável na janela: a `## 1` vigente só muda por versão
  adjudicada em marco, e o Marco 2 vem **depois** da `LST-T5`, que é a mesma circularidade do
  `AE-5`. Executa a `LST-T9`, item 1; a `LST-T5` passa a declarar a aferição por prefixo no campo
  *Domínio* e na Verificação 2.
- **`AE-11`** — **A rota do `AE-9` ficou órfã.** Achado do mesmo laudo. O `AE-9` roteava para a
  `LST-T8`, mas o card dela declara a `## 2. Requisitos secundários` **fora do escopo**: a tarefa
  fechou sem fechar a rota. Rota: re-declarar o `AE-9` para um card que possa executá-la, e decidir
  ali se a residência do requisito secundário se identifica por **nome** de seção ou por **número**.
  **Resolvido em 2026-09-22 pelo consultor:** a decisão é do `DLS-15` — por nome —, e a rota do
  `AE-9` está re-declarada para a `LST-T9`, cujo campo *Arquivos-alvo* e cujas Verificações 3 e 4
  cobrem a mesma subseção. Achado de método, para o encerramento: card que **recebe** rota de
  achado precisa dizê-lo no próprio dossiê; declarar a matéria fora de escopo e herdar a rota ao
  mesmo tempo é contradição que só aparece no laudo seguinte.
- **`AE-12`** — **As linhas `tarefas:` do fluxo não contabilizam esta janela.** Pendência do laudo da
  `LST-T9` (2026-09-22, `aprovado` 100%, `recomendacao=escalar`). A `OP-1` e a `OP-2` ganharam a
  `LST-T8` pelo dossiê de emenda de 2026-09-21 (`DLS-13`), mas **nenhuma** delas — nem a `OP-3`, nem
  a `OP-4` — lista a `LST-T9`, que materializou as quatro. Só o modelador escreve na `## 1` (`I-1`),
  então isto morre em silêncio se não entrar no dossiê do Marco 2. A fechar **antes** de o Marco 2
  adjudicar a versão 4.
- **`AE-13`** — **O card da `LST-T9` atribui a terceira frase à propriedade errada.** Achado de
  processo do mesmo laudo. O *Pronto quando* mapeia as Verificações 5 e 6 a `leitura de prompt`
  (`OP-2`) e chama o caso medido de *leitura pela via errada*; mas a frase editada vive no parágrafo
  da **decomposição** de `GOVERNANCA.md` §3.2, residência da propriedade `decomposição em objeto e
  propriedade` (`OP-3`, `tarefas: LST-T7`) — e o próprio *Objetivo* do card a chama de *caso medido
  da promoção indevida*, contradizendo o *Pronto quando*. Consequência: o campo *Operação do modelo*
  cita `OP-1`, `OP-2` e `OP-4` e **omite a `OP-3`**, cujo parágrafo a entrega de fato emendou. Não
  rebaixa a entrega — a *Forma prescrita* nomeou o alvo certo e o executor a cumpriu literalmente.
  Rota: levar ao Marco 2 junto com a adjudicação da versão 4.
- **`AE-14`** — **O card da `LST-T5` contradiz a si mesmo nas fixtures, e o executor parou.** Retorno
  `blocked motivo=premissa` do executor Sonnet em 2026-09-22 (31 tool uses, 144.8k), sob `G-NOASK`.
  A cláusula *"as fixtures do vocabulário `V1`..`V20` existente não se alteram"* (em *Fora do escopo*)
  é incompatível com a Verificação 1 e com o *Domínio*: a violação nova — elemento sem lastro
  declarado na `### 1.1`, por ausência da sexta coluna, cujo **único** critério de exceção é o status
  terminal (`DLS-12`, `F-15`, Verificação 3) — dispara também sobre
  `tests/fixtures/modelo/plano-invalido.md`, `plano-invalido-2.md` e `fluxo-valido.md`, que têm
  status `in-progress` e não declaram coluna de lastro. Com isso quebram
  `test_tf_check_invalido_lista_catorze_violacoes_na_ordem` e `test_tf_check_fluxo_valido_sai_zero`,
  e o `I-3` cai. Fechar a tarefa exigiria **ou** editar fixture que o card proíbe editar, **ou**
  abrir na regra uma exceção que o card não declara — decisão de rota, que o executor não toma.
  Rota: escalado ao consultor de plano em 2026-09-22. A tarefa está `blocked motivo=premissa`.
  **Resolvido em 2026-09-22 pelo consultor: o executor tem razão, a contradição é do card, e a
  parada foi correta.** Decisão no `DLS-17`, rota **(a)** com invariante: as fixtures migram para a
  forma publicada e **nenhum valor de asserção existente muda** — as 14 violações continuam 14, na
  mesma ordem, e `fluxo-valido.md` continua `modelo: OK`. A rota **(b)** — segundo critério de
  exceção — foi recusada: o recorte da `V21` é um só, o status terminal, e exceção por caminho de
  fixture ensinaria o instrumento a mentir. O card foi emendado: *Arquivos-alvo* passa a incluir
  `tests/fixtures/modelo/`, a cláusula contraditória virou *"enfraquecer a cobertura é que está
  proibido"*, e entraram as Verificações 6 e 7 — o trio da `V21` sobre fixture nova e a
  não-regressão do corpus por número medido (`F-18`). A tarefa volta à fila sem mudar de escopo:
  segue `Sonnet · classe implementacao`, com mais três fixtures novas e a migração mecânica de
  sete.
- **`AE-15`** — **Segundo `blocked motivo=premissa` no mesmo card, por executor frio independente.**
  Retorno da `LST-T5` em 2026-09-22 (18 tool uses, 76.2k), depois do reparo do `AE-14`/`DLS-17`.
  `defeito=ambiguidade`: o *Objetivo* e a Verificação 4 exigem que a `V2` deixe de acusar a tarefa
  que **declara** não materializar operação por ser requisito não fundamental — mas a gramática
  publicada define **uma só** forma para o campo (`- **Operação do modelo:** \`OP-<a>\`[, \`OP-<b>\`]`),
  sem forma alternativa para essa declaração. Medido pelo loop, independentemente:
  `grep -cF 'requisito não fundamental'` → **0** na skill `diario-de-obras` e **0** em
  `GOVERNANCA.md`; nenhuma fixture, plano ou entrega das `LST-T1`/`T3`/`T7`/`T8`/`T9` contém
  instância viva. A `LST-T3` publicou a **seção** de requisitos secundários; a **forma do campo do
  card** que a declara nunca foi publicada por tarefa nenhuma — é um vão de rota entre a `OP-4` e a
  `OP-5`, não um defeito de redação do card. Escolher o padrão textual seria decisão do executor
  (`G-NOASK`). Rota: escalado ao consultor de plano em 2026-09-22, com a pergunta de classificação —
  segundo bloqueio consecutivo no mesmo card é sinal sobre o card, não sobre quem executa.
  **Resolvido em 2026-09-22 pelo consultor, classificado técnico e tático (`DLS-18`).** O achado é
  procedente e o sinal é sobre o **modelo**: a metade `V2` da `OP-5` não tem lastro no enunciado
  (`F-19`), e sai por emenda acumulada na versão 4 pendente (`DLS-16`), como já saíram a restrição
  de atualização, por ato do dono (`DLS-11`), e a metade de ator, por inexequibilidade medida
  (`DLS-13`). O conteúdo virou o **`TK-71`**, aberto no mesmo ato — rota que sai do plano também
  precisa de residência (lição do `AE-11`). A `LST-T5` fica com a `V21` e volta à fila: o título, o
  objetivo, o campo da operação, as verificações (de nove para oito) e o *Fora do escopo* foram
  emendados. **Nenhum dos dois bloqueios foi falha de execução** — os dois executores pararam onde
  deviam parar, e os dois achados corrigiram o plano.
- **`AE-16`** — **A `OP-5` prometia mais do que a máquina afere; resolvido no ato.** Achado de alvo
  `modelo` do laudo da `LST-T5` (2026-09-22, `aprovado` 100%). O texto dizia que a conferência acusa
  **elemento** sem lastro declarado, e *elemento*, no enunciado deste plano, cobre objeto, operação e
  propriedade (`OP-1`); o instrumento entregue acusa **objeto** — uma `V21` por objeto da tabela de
  `### 1.1`, onze sobre o `P-0745` —, e a falta do lastro da operação ou da propriedade é silenciosa.
  Não era defeito da entrega: a gramática da `LST-T8` já pusera essa fronteira, deixando os dois sob
  **guarda do Marco**. **Fechado**: dossiê `Ato de modelo` de `conflito` devolvido pelo revisor,
  despachado pelo loop e escrito pelo `pantonic-model-designer` na `## 1A` (quarto ato acumulado na
  versão 4) — a `OP-5` passa a dizer *objeto* e a nomear na própria frase a metade que o Marco
  guarda. Sem pendência.
- **`AE-17`** — **Não está decidido se a `V21` alcança o bloco `## 1A` pendente.** Achado de processo
  do mesmo laudo. O card não fechou o ponto: a Verificação 5 só pina fixtures de bloco vigente, e a
  Verificação 2 não discrimina porque a `## 1A` do `P-0746` já tem a coluna. **A execução decidiu**
  alcançar só a `## 1` vigente — coerente com a `V15` e a `V17`, que também só varrem
  `modelo.objetos`, e por isso sem rebaixamento —, mas é decisão de execução sobre ponto aberto, sem
  teste que a cubra. Medido pelo revisor fora do repositório: um bloco `## 1A` sem a coluna de lastro
  sai com **zero** `V21`. Rota: item de replanejamento do `P-0746`, a decidir **antes** do Marco 2,
  que é justamente quem adjudica versão pendente.
- **`AE-18`** — **A classe de defeito "ator inédito na operação" foi dispensada pelo loop, e o dono
  não foi consultado.** Pendência do laudo da `LST-T6` (2026-09-22, `aprovado` 100%,
  `recomendacao=escalar`). O modelo v2 do `P-0745` entrega **5 de 5** atores citados em `### 1.2`
  que não são objetos de `### 1.1` — exatamente a classe que o dono tipificou no `TK-69` §3, chamou
  de *integralmente mecânica* e mediu ele mesmo em zero de cinco. O loop decidiu **não construir a
  regra** (`AE-4`, `F-14`, `DLS-13`), porque ela reprovaria 6 dos 7 atores do `P-0743` aceito e 4 dos
  4 do `P-0746`, e retirou o teste da Verificação 2 daquele card. A decisão está certa como
  engenharia e **não é defeito da entrega** — mas é classe que o dono nomeou e o loop dispensou sem
  ele. **Se ele a mantiver, o Marco 3 reprova o modelo pelo mesmo defeito de 2026-09-21.** Manter ou
  dispensar é decisão dele. É a pendência principal ao dono neste encerramento.
- **`AE-19`** — **`Arquivos-alvo` da `LST-T6` incompleto contra as próprias cláusulas de aceite.**
  Achado de processo do mesmo laudo. O campo recortava três seções do `P-0745`, mas reautorar o
  modelo de 7 para 6 operações renumeradas **obriga** a reescrever o campo `Operação do modelo` dos
  sete cards `PLN-T1..PLN-T7` — sem isso a `V4` e a `V14` disparam (`.claude/tools/modelo.py:406-416`)
  e a Verificação 1 não sai `0` —, e torna falsos os bullets por propriedade do `Pronto quando`
  deles, que citavam propriedades extintas (contra o `DPN-6`). O card não fechou a decisão e a
  execução teve de tomá-la; ela a **declarou por inteiro na pendência de retorno**, com razão por
  item, e o diff confirma a declaração linha a linha. Rota: regra de autoria — card que reautora
  modelo declara no `Arquivos-alvo` as seções acopladas por `V4`, `V14` e `DPN-6`.
- **`AE-20`** — **Verificação 4 da `LST-T6` sem valor esperado.** O comando era
  `grep -c 'cancelled'` sobre o arquivo inteiro, e a linha de seta trazia prosa, nenhum número.
  Medido antes: **2** — uma na tabela de marcos, uma na `## 11. Riscos`. Editando só a tabela o
  comando devolve `1`, e o card não dizia se `1` passa; a única leitura inequívoca de *"não existe
  mais"* é `0`. A ambiguidade forçou a execução a decidir, e ela editou também a linha de Riscos,
  que o `Arquivos-alvo` não nomeava. No mérito a decisão está certa: aquela linha repetia o ramo
  caduco que a `DLS-5` aposentou. Defeito de autoria, não de execução.
- **`AE-21`** — **`GOVERNANCA.md` §3.2 não tem ramo para primeira versão recusada e reautorada.**
  Achado de alvo `doutrina` do mesmo laudo. A norma prescreve que emenda versiona e não reescreve,
  que a versão nova nasce como bloco irmão `pendente`, e que a pendente recusada é eliminada. A
  entrega do `P-0745` substituiu no lugar, declarou a versão 2 `situação: vigente` sem aceite do dono
  e registrou a versão 1 como `obsoleta` — três afastamentos da letra, cada um defensável porque a
  versão 1 nunca vigorou, nenhum coberto pelo texto. A divergência está medida **dentro da própria
  janela e no mesmo papel**: a `## 1A` do `P-0746` (versão 4) está `pendente` aguardando o Marco 2, e
  a `## 1` do `P-0745` (versão 2) está `vigente` aguardando o Marco 3 — mesmo estado, valores
  opostos. Não rebaixa dimensão. Rota: `TK-70` Pacote A, que já é dono da vigência bilateral do
  modelo e já edita `GOVERNANCA.md` §3.2 imediatamente antes desse parágrafo.
- **`AE-22`** — **`review_evidence.py` não expande alvo em forma de diretório.** O dossiê de
  evidência da `LST-T6` acusou 13 arquivos *"fora dos alvos e sem atribuição"*, dos quais **10** são
  fixtures de `tests/fixtures/modelo/` — entrega declarada da `LST-T5`, cujo `Arquivos-alvo` nomeia
  aquele diretório e as fixtures uma a uma. A atribuição por arquivo falha quando o alvo termina em
  barra, e o reviewer da última tarefa da janela recebeu 10 falsos `sem-atribuicao` para reconciliar
  à mão. Os outros 3 são o `AE-3`, já sem ação. Rota: tíquete contra `.claude/tools/review_evidence.py`
  — expandir alvo terminado em barra como prefixo de caminho (`I-4`).
