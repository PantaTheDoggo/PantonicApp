# Especificação do agente de planejamento

Medido e redigido em 2026-09-22, na branch `plan/planner-modelo-escopo`.
Duas fontes, e só elas: a `## 12. Agregado medido` de `docs/plans/P-0745-planejador-modelo-operacao.md` — o retrato do **antes** — e a `## 3. Decisões` do mesmo plano — o que institui o **depois**.
A figura descrita aqui é a que existe **depois** das `PLN-T2`..`PLN-T5`: nenhuma afirmação descreve o estado anterior a elas sem dizer que o descreve.

---

## 0. O que esta especificação não é

Não é a residência do **escopo do papel**: o que o planejamento responde e o que não responde está na matriz de responsabilidades de `GOVERNANCA.md` §3, e aqui é citado, nunca reenunciado.
Não é a residência do **protocolo de conduta**: as fases, as saídas e a anatomia do card estão em `.claude/agents/pantonic-planner.md`, e aqui são citadas, nunca reenunciadas.
É a descrição **medida** da figura, escrita para quem precisa decidir quando acioná-la, o que esperar dela e quanto ela custa — e cada afirmação abaixo tem uma âncora no retrato medido ou na decisão que a instituiu.

---

## 1. A figura, em uma página

O agregado registra, para esta dimensão, **sem ocorrência no corpus medido em 2026-09-21**. O corpus fechado de oito fontes não produziu nenhuma ocorrência que descrevesse a figura como um todo — ele mediu o comportamento dela, dimensão a dimensão, nunca o retrato.

O que as decisões deste plano instituíram para esta dimensão:

- A figura passa a ter **descrição pública própria** — este documento —, ancorada no retrato medido (o antes) e nas decisões deste plano (o depois), com a lista de dimensões residindo na §4 do plano (`DPN-8`, `DPN-1`).
- A unidade que ela recorta passa a ser a **operação do modelo**: um card por operação, uma operação por card (`DPN-2`).
- A sessão dela passa a ter uma **terceira saída** antes do plano fechado, e a decomposição só começa com o modelo na árvore (`DPN-4`).

E nada mais: o parágrafo que a dimensão pede — *o que é o planejamento, em um parágrafo que quem nunca viu entende* — não tem lastro no corpus medido, e por isso não é escrito aqui. A pergunta está nomeada na seção 10.

> **Âncoras:** agregado, dimensão 1 (`ocorrências | sem ocorrência no corpus medido`); `DPN-1`, `DPN-2`, `DPN-4`, `DPN-8`; seção 10, linha *o retrato de uma página*.

---

## 2. Gatilho

**O que aciona, medido.** O corpus fecha **14 ocorrências** nesta dimensão. A mais antiga é `AE-1`→`RP-1` (`P-0739`), de 2026-09-16; a mais recente é `AE-23`→`RP-1` (`P-0743`), de 2026-09-21. A classe dominante é uma só, e é a mesma da primeira à última: **`blocked motivo=premissa` do executor ou do revisor** — a parada de quem executa, ou o achado de quem julga, é o que abre uma sessão. A ocorrência de exemplo é a própria `AE-1`→`RP-1` (`P-0739`), 2026-09-16.

Duas leituras que os números sustentam, e só elas:

- O acionamento medido é **reativo**: as 14 ocorrências nascem de um sinal vindo do loop de execução, não de iniciativa da figura.
- O acionamento medido é **contínuo no período**: a mais antiga e a mais recente cobrem de 2026-09-16 a 2026-09-21, cinco dias, sem interrupção registrada de classe.

**O que não aciona.** O corpus fechado mede o que aconteceu, não o que foi recusado: não há, nele, ocorrência de sessão **não** aberta. A única fronteira negativa que o agregado fixa é uma pergunta em aberto — se o escalonamento ao consultor (`ESC-*`) é ocorrência desta dimensão ou da dimensão 3, já que não é rodada de replanejamento nem decisão do dono. A pergunta está reproduzida na seção 10.

O que as decisões instituíram sobre a relação entre o gatilho e o desfecho: a sessão acionada pode terminar **sem plano fechado**, com o esqueleto gravado e o dossiê `Ato de modelo` de autoria devolvido na linha de retorno — a `SAÍDA 3` da `DPN-4`. Um gatilho não implica mais um plano completo na mesma sessão.

> **Âncoras:** agregado, dimensão 2 (`ocorrências | 14`; mais antiga, mais recente, classe dominante, exemplo); agregado, dimensão 10, 2ª linha; `DPN-4`.

---

## 3. Domínio de decisão

**O que a figura fecha por si, medido.** O corpus fecha **14 ocorrências** nesta dimensão. A mais antiga é `RP-1` (`P-0739`), 2026-09-16; a mais recente é `RP-1` (`P-0743`), 2026-09-21. A classe dominante é **decisão técnica ou tática fechada no próprio contexto**, sob a `G-NOASK`. A ocorrência de exemplo é `RP-1` (`P-0741`), 2026-09-20 — e é exemplo justamente por ser a fronteira com a decisão do dono.

**O que sobe ao dono, medido.** A dimensão 9 fecha o número pelo outro lado: das 14 rodadas, **13** fecharam como decisão técnica ou tática no próprio contexto e **0** subiram ao dono como saída da rodada. Houve **1** decisão do dono **antecedente** à rodada — `RP-1` (`P-0741`), 2026-09-20 —, que é caso distinto: o dono decidiu antes, e a rodada materializou a decisão.

O que as decisões instituíram sobre o que continua sendo do dono:

- O **veto no Marco 1** sobre alvo de edição fora do repositório, nominalmente a cópia do dono das regras globais (`DPN-12`).
- O **merge em `main`**: nada é commitado por tarefa, o commit é no marco, e o merge é ato do dono (`DPN-11`).
- O **aceite do plano** pela confrontação do estado inicial com o estado final, que é o critério que o card herda por propriedade (`DPN-6`).

E o que as decisões **tiraram** do domínio de decisão da figura: o percentual de ocupação da janela e a tabela de tetos de turnos deixaram de dimensionar tarefa — a régua passa a três critérios sem número, e o único limiar que sobra é o da janela de orquestração, declarado fora do dimensionamento de tarefa (`DPN-3`).

> **Âncoras:** agregado, dimensão 3 (`ocorrências | 14`; mais antiga, mais recente, classe dominante, exemplo); agregado, dimensão 9 (`fecharam técnica/tática no contexto | 13`, `subiram ao dono | 0`, `decisão do dono antecedente à rodada | 1`); `DPN-3`, `DPN-6`, `DPN-11`, `DPN-12`.

---

## 4. Operacionalização do plano em cards

**O antes, medido.** O corpus fecha **7 ocorrências** nesta dimensão. A mais antiga é `AE-1`/`RP-1` (`P-0739`), 2026-09-16; a mais recente é a régua de granularidade registrada em `docs/Entregas Aceitas/Entregas - P-0743.md`, 2026-09-21. A classe dominante é **gramática ou campo de card ambíguo** — a falha medida não estava em o que o card pedia, e sim em como o card dizia o que pedia. A ocorrência de exemplo é `AE-1` (`P-0739`), 2026-09-16.

O agregado desta dimensão **não nomeia** as duas formas que o fato `F-3` do plano registra como o custo medido do arranjo anterior: **duas mãos sobre a mesma região sem regra de precedência** (`AE-21` do `P-0743`) e **card de dois atos** (`AE-24` e `AE-25` do `P-0743`). Elas são o antes desta dimensão, e estão aqui pelo `F-3`, não pelo agregado — a contagem `7` da dimensão 4 não as discrimina.

**A operação como unidade — o depois.** A `DPN-2` fecha a partição: na autoria, cada card materializa **exatamente uma** operação e cada operação tem **exatamente um** card, com o id derivado do número da operação (`<prefixo>-T<n>` ↔ `OP-<n>`). Card corretivo nascido em replanejamento (`T<n>a`, `T<n>b`) **soma-se** à operação do card que corrige, em vez de abrir operação nova. E o planejador **nunca parte uma operação em dois cards**: operação que não cabe num card coeso é defeito do modelo — operação com propriedade embutida — e volta ao modelador por dossiê, não vira duas tarefas.

A consequência que a `DPN-2` explicita: *módulo coeso* deixa de ser recorte por juízo e passa a ser **consequência do modelo**. A relação foi medida uma vez, e o número está na própria decisão: o `P-0743` fechou com **13 operações, 13 cards de autoria e 5 corretivos**.

**O que entra num card.** A `DPN-6` deriva o aceite do estado final, campo a campo: `Objetivo` é o texto da operação copiado; `Pronto quando` enumera, por propriedade que a operação `altera:`, o estado final da `### 1.3` e a linha de `Verificação` que o mede; `Camada e fronteira` transcreve o contrato dos objetos de `precisa de:`. Card cuja `Verificação` não mede alguma propriedade alterada é **card incompleto** — e o critério é por propriedade, não por card inteiro.

**O que fica fora, e onde a decomposição para.** A `DPN-4` parte a Fase 3 em duas e institui a parada. Na **Fase 3a** o planejador grava o plano **sem** a `## 1` e **sem** os cards — §0, fatos, decisões, invariantes, fora de escopo, riscos — e devolve, na linha de retorno, o dossiê `Ato de modelo` de `autoria`; quem conduz a sessão despacha o modelador. Na **Fase 3b**, com a `## 1` na árvore, ele escreve um card por operação, na ordem das operações, e só então roda a Fase 4 e a Fase 5. A parada é obrigatória porque nenhum agente aciona outro: sem ela, a figura continuaria escrevendo cards que citam operações antes de elas existirem.

**Por que a partição é do modelo e não do planejador.** As três decisões convergem num mesmo ponto: a unidade não é escolhida no momento de recortar o trabalho, ela é **lida** do modelo. Quem decide quantos cards um plano tem é a contagem de operações; quem decide o que cada card entrega é o estado final das propriedades que a operação altera; e o que sobra fora dessa correspondência é defeito de modelo, com rota própria de volta ao modelador.

> **Âncoras:** agregado, dimensão 4 (`ocorrências | 7`; mais antiga, mais recente, classe dominante, exemplo); `F-3` do plano (`AE-21`, `AE-24`, `AE-25` do `P-0743`); `DPN-2` (inclusive a relação medida 13/13/5), `DPN-4`, `DPN-6`.

---

## 5. Fronteira

**O medido.** O corpus fecha **5 ocorrências** nesta dimensão. A mais antiga é `RP-3` (`P-0739`), 2026-09-16; a mais recente é a redução dos papéis que escrevem no modelo, de três para um, registrada em `docs/Entregas Aceitas/Entregas - P-0743.md`, 2026-09-21. A classe dominante é **quem escreve ou edita — papel contra ferramenta**. A ocorrência de exemplo é `AE-11` (`P-0740`), 2026-09-18.

**Com o modelador.** O espelho é a tabela *Quem escreve* de `GOVERNANCA.md` §3.2, e a linha `planejador` dela diz onde o planejamento termina: ele grava o esqueleto do plano **sem** a seção do modelo e **sem** os cards e devolve o dossiê `Ato de modelo` de autoria; com a seção na árvore, escreve um card por operação e **mantém a lista `tarefas:` de cada operação** — lastro, não modelo — na decomposição e em toda rodada de replanejamento; e o plano não vai ao Marco 1 sem a seção escrita pelo modelador, sem os cards e sem `modelo.py check` saindo `0`. A linha `modelador` fecha o outro lado: a seção inteira é dele, em todo ato, inclusive sobre plano que ainda não tem cards.

O que instituiu cada metade: a `DPN-4` (as duas fases e a devolução do dossiê) e a `DPN-5` (a lista `tarefas:` é lastro do planejador depois da autoria, e as violações `V1` e `V3` voltam medidas para ele em vez de travarem a devolução de quem escreve o modelo).

**Com o consultor.** O espelho é a §4 de `docs/consultant-spec.md`, que declara a fronteira do lado de lá. Ela mede que a figura do consultor **reescreve card aberto**, **repara instrumento do loop com código** e **recusa-se a editar o artefato que é alvo de um card aberto** — e que **autorar card novo** ficou **fora** da enumeração do papel dela. O veredito registrado lá é que a autoria de card é **empréstimo, não atribuição** da figura do consultor, por três fatos, um dos quais é que *autorar card é ato de planejamento*. Espelhado deste lado: **a autoria de card novo é atribuição do planejamento**, e o empréstimo existe como fato medido, sem norma que o autorize. O documento do consultor registra o empréstimo e **não** o promove; este documento também não o promove.

A `docs/consultant-spec.md` §4 registra ainda a única linha que nenhuma instância do consultor cruzou: ela **nunca reabriu o objetivo do plano**. É essa linha — e não a autoria de card — que separa as duas figuras na prática medida.

**Com a orquestração.** A tabela *Quem escreve* põe a orquestração fora da escrita do modelo: ela **não escreve**; despacha o modelador ao receber um dossiê `Ato de modelo`, roda `modelo.py check` antes de despachar e antes de fechar cada tarefa, e abre o relatório de encerramento e cada marco com `modelo.py show`. A fronteira é operante porque **nenhum agente aciona outro**: o papel que precisa de um ato de modelo devolve o dossiê na própria linha de retorno, e quem conduz a sessão o despacha — que é exatamente a razão pela qual a parada da `DPN-4` é obrigatória e não recomendada.

**Com a revisão.** A mesma tabela: o revisor **não escreve**; divergência entre a entrega e o texto de uma operação vira achado de processo de alvo `modelo`. A fronteira do planejamento com a revisão é, portanto, assimétrica — o revisor devolve achado, não emenda.

Nenhuma divergência entre os dois espelhos foi medida ao redigir esta seção: `docs/consultant-spec.md` §4 atribui a autoria de card ao planejamento, e a tabela *Quem escreve* de `GOVERNANCA.md` §3.2 atribui ao planejador a decomposição em cards e o lastro. As duas perguntas que a redação deixou abertas sobre esta fronteira estão na seção 10.

> **Âncoras:** agregado, dimensão 5 (`ocorrências | 5`; mais antiga, mais recente, classe dominante, exemplo); tabela *Quem escreve* de `GOVERNANCA.md` §3.2 (linhas `planejador`, `modelador`, `consultor`, `revisor`, `orquestração`) e o parágrafo *Nenhum agente aciona outro agente*; `docs/consultant-spec.md` §4; `DPN-4`, `DPN-5`.

---

## 6. Instrumento

**O medido.** O corpus fecha **3 ocorrências** nesta dimensão. A classe dominante é **comando citado numa linha de `Verificação` sem execução medida** — a figura escreveu o literal esperado de memória em vez de o ter observado.

As ocorrências nomeadas pelo agregado, com o identificador no formato `RP-<n>` (`P-<plano>`) usado nas outras nove dimensões e com o `arquivo:linha` medido em 2026-09-22:

| ocorrência | identificador | data | onde o corpus a hospeda |
|---|---|---|---|
| mais antiga | `RP-1` (`P-0739`) | 2026-09-16 | `.claude/agents/pantonic-planner.md:109` |
| mais recente | `RP-2` (`P-0740`) | 2026-09-18 | `.claude/agents/pantonic-planner.md:124` e `:342` (esta com `AE-4`) |

A terceira ocorrência que a contagem declara **não se nomeia a partir do agregado**: a tabela fixa os extremos e o número, não o conjunto. As duas candidatas remanescentes no corpus são `.claude/agents/pantonic-planner.md:115` (`RP-2`, `P-0739`, 2026-09-16) e `:119` (`RP-3`, `P-0739`, 2026-09-16), ambas da mesma data da mais antiga. Qual das duas entrou na contagem e qual ficou fora é pergunta da seção 10, e não se responde aqui por escolha.

Sobre o identificador: `RP-<n>` é **por plano** — cada plano tem o seu `RP-1` —, e `.claude/agents/pantonic-planner.md` o hospeda apenas por referência. Por isso toda citação acima nomeia o plano da rodada, e o arquivo aparece como `arquivo:linha`, nunca como qualificador do identificador.

**O que a figura roda, e o que ela não mede por conta própria.** A residência da regra é `.claude/agents/pantonic-planner.md` — Fase 1 e Fase 4 —, citada aqui e não reenunciada. O que a tabela *Quem escreve* de `GOVERNANCA.md` §3.2 fixa como **não sendo** da figura: `modelo.py check` antes de despachar e antes de fechar cada tarefa, e `modelo.py show` em cada marco e relatório, são da orquestração. O planejador é o papel para quem `modelo.py check` precisa sair `0` — não o papel que o roda no gate.

O que as decisões acrescentaram ao instrumental: a `DPN-9` institui uma **guarda executável** — `tests/test_doutrina_unidade.py` — que afere por literal a ausência do percentual de ocupação e da tabela de tetos nas residências que este plano edita. É a primeira vez que uma mudança de doutrina do papel nasce com aferição automática em vez de só com texto.

> **Âncoras:** agregado, dimensão 6 (`ocorrências | 3`; mais antiga, mais recente, classe dominante); `AE-5` do plano (forma da citação e a ocorrência do meio não re-derivável); `AE-4` do plano (a âncora `RP-2` do `P-0740`); tabela *Quem escreve* de `GOVERNANCA.md` §3.2, linha `orquestração`; `DPN-9`.

---

## 7. Custo e teto

**O que a série permite dizer.** A série medida do planejamento em `docs/telemetria.tsv` tem **uma linha** (`F-9`). Dela sai, e só dela:

| métrica | valor |
|---|---|
| linhas de planejamento | 1 |
| consumo mediano | 183k tokens |
| consumo máximo | 183k tokens — a mesma linha |
| data da primeira | 2026-08-15 |
| data da última | 2026-08-15 |
| a linha | `RPC-P0735-planejamento`, 2026-08-15, Opus, 64 tool uses |

Mediana e máximo coincidem porque há uma única observação. Primeira e última data coincidem pela mesma razão. Com `n = 1` não há dispersão, não há tendência e não há valor típico: **183k tokens é uma observação, não uma expectativa**, e esta seção não a converte em previsão.

**Quando não abrir uma sessão.** A série de uma linha não sustenta nenhum critério de custo para essa decisão, e nenhum é escrito aqui.

**O teto.** A `DPN-3` retirou o teto do dimensionamento de tarefa: a *Diretriz de dimensionamento de tarefa* passa a três critérios **sem número** — (a) uma operação inteira do modelo; (b) contexto coerente e coeso; (c) autossuficiência em contexto para a execução —, a tabela *Orçamento de turnos por tarefa atômica* é aposentada, e a **classe** do cabeçalho permanece como natureza do trabalho, sem teto, porque os parsers a leem. O único número de ocupação que fica é o limiar da **janela de orquestração**, que é de outra figura e não dimensiona tarefa.

Logo, a resposta desta dimensão à metade *teto* não é um número: é a ausência dele, por decisão, e a substituição por um critério de coesão que não se mede em tokens.

**O que seria preciso medir.** A série pode estar subcontada — o filtro que a produziu seleciona as linhas cujo campo `tarefa` contém `planej` ou `planner`, e sessão de planejamento nomeada de outro modo não entra. E toda a série é **anterior** à régua instituída pela `DPN-3`: nenhuma das observações descreve o custo da figura sob os três critérios novos. As duas pendências estão na seção 10.

> **Âncoras:** agregado, dimensão 7 (as seis linhas da tabela); `F-9` do plano; agregado, dimensão 10, 3ª linha; `DPN-3`.

---

## 8. A rodada de replanejamento

**O medido.** O corpus fecha **14 ocorrências**. Delas, **13** foram replanejamento conduzido pelo planejador e **1** foi reparo conduzido pelo consultor como substituto — `RP-5` (`P-0740`), 2026-09-18. A mais antiga é `RP-1` (`P-0739`), 2026-09-16; a mais recente é `RP-1` (`P-0743`), 2026-09-21. A classe dominante é **decisão técnica ou tática sobre achado do executor ou do revisor**. A ocorrência de exemplo é `RP-6` (`P-0739`), 2026-09-18.

**Entrada.** O agregado da dimensão 2 e o desta dimensão medem a mesma origem por dois ângulos: a entrada é o achado do executor ou do revisor — classe dominante `blocked motivo=premissa` na dimensão 2, achado do executor ou revisor na dimensão 8. Entrada e gatilho coincidem no corpus medido.

**Saída.** O desfecho medido é a decisão fechada no próprio contexto: 13 de 14 (dimensão 9), com **0** subindo ao dono como saída da rodada e **0** terminando com o plano `superseded`. A saída que as decisões acrescentaram: o card corretivo (`T<n>a`, `T<n>b`) **não abre operação nova** — soma-se à operação do card que corrige (`DPN-2`) —, e a lista `tarefas:` da operação é estendida pelo planejador na própria rodada, porque é lastro dele e não do modelador (`DPN-5`).

**Posição na fila.** A forma da rodada tem residência única na `G-REPLAN` (`GOVERNANCA.md` §7 item 17), citada aqui e não reenunciada.

**A série das rodadas já ocorridas.** O corpus a fecha por extremos e por classe, não por enumeração: 14 rodadas entre 2026-09-16 e 2026-09-21, sobre os planos `P-0739`, `P-0740`, `P-0741` e `P-0743`, com uma única rodada fora do papel — a do consultor, em 2026-09-18. Se essa rodada de reparo conta como rodada desta dimensão ou é classe à parte é pergunta em aberto, reproduzida na seção 10.

> **Âncoras:** agregado, dimensão 8 (`ocorrências | 14`, `replanejamento (planejador) | 13`, `reparo (consultor, substituto) | 1`, mais antiga, mais recente, classe dominante, exemplo); agregado, dimensão 9 (`subiram ao dono | 0`, `terminaram com plano superseded | 0`); agregado, dimensão 2 (classe dominante); agregado, dimensão 10, 1ª linha; `DPN-2`, `DPN-5`.

---

## 9. Estatística do próprio acionamento

| métrica | valor |
|---|---|
| rodadas totais | 14 |
| fecharam técnica ou tática no próprio contexto | 13 |
| subiram ao dono como saída da rodada | 0 |
| decisão do dono antecedente à rodada | 1 — `RP-1` (`P-0741`), 2026-09-20 |
| terminaram com o plano `superseded` | 0 |
| mais antiga | `RP-1` (`P-0739`), 2026-09-16 |
| mais recente | `RP-1` (`P-0743`), 2026-09-21 |
| exemplo | `RP-2` (`P-0739`), 2026-09-16 |

Três leituras que os números sustentam, e só elas:

- **A figura fecha o que abre.** 13 de 14 rodadas terminaram dentro do próprio contexto; nenhuma devolveu a decisão ao dono como saída.
- **Nenhuma rodada matou um plano.** `0` terminaram com o plano `superseded` — o replanejamento medido reparou o plano em curso, nunca o sucedeu.
- **A única decisão do dono no recorte é antecedente, não consequente.** A `1` linha de decisão do dono precede a rodada que a materializou; ela não é saída de rodada.

A décima quarta rodada — a que não é do planejador — é a do consultor (`RP-5`, `P-0740`, 2026-09-18), contada aqui pela dimensão 8 e pendente de classificação na seção 10.

> **Âncoras:** agregado, dimensão 9 (as oito linhas da tabela); agregado, dimensão 8 (`reparo (consultor, substituto) | 1`); agregado, dimensão 10, 1ª linha.

---

## 10. O que esta especificação não fecha

As cinco perguntas que o agregado já trazia, e as quatro que esta redação acrescentou. Nenhuma é respondida aqui por adivinhação.

| pergunta que o corpus medido não responde | o que seria preciso medir para respondê-la |
|---|---|
| Se a rodada de reparo conduzida pelo consultor (`RP-5`, `P-0740`) conta como rodada de replanejamento das dimensões 8 e 9, ou é classe à parte | Uma regra de classificação declarada, aplicada de volta às 14 rodadas do recorte; e a contagem re-derivada sob as duas leituras, para saber se o `13/14` muda |
| Se escalonamento ao consultor (`ESC-*`) é ocorrência da dimensão 2 ou da 3, já que não é rodada de replanejamento nem decisão do dono | O universo de `ESC-*` do recorte, cada um classificado por gatilho e por desfecho, contra as classes dominantes já medidas das dimensões 2 e 3 |
| O custo de sessão de planejamento cuja `tarefa` em `docs/telemetria.tsv` não contém `planej` nem `planner` — a linha única da dimensão 7 pode subcontar | Uma varredura de `docs/telemetria.tsv` por critério que não dependa do nome do campo `tarefa` — por exemplo, o agente registrado na linha —, com a série re-derivada e comparada à de uma linha |
| Por que a dimensão 1 não tem ocorrência medida no corpus fechado | Se a ausência é do corpus (as oito fontes não descrevem a figura como um todo) ou do método (a dimensão não tinha critério de ocorrência); resolve-se declarando o critério e reaplicando-o às oito fontes |
| Se *papéis que escrevem no modelo: 3→1* (`docs/Entregas Aceitas/Entregas - P-0743.md`) é decisão retroativa sobre a dimensão 3 ou fato novo da dimensão 5 | A data e o ato que produziram a redução, confrontados com a data das ocorrências já contadas em cada uma das duas dimensões |
| **Acrescentada por esta redação.** Qual é a terceira ocorrência da dimensão 6: o agregado conta `3` e nomeia os extremos, e as candidatas remanescentes são `.claude/agents/pantonic-planner.md:115` (`RP-2`, `P-0739`) e `:119` (`RP-3`, `P-0739`) | O critério de inclusão que a medição da dimensão 6 usou, aplicado de volta às quatro citações de instrumento do corpus; enquanto ele não for declarado, o conjunto de `3` não se reconstrói a partir da tabela |
| **Acrescentada por esta redação.** O retrato de uma página que a dimensão 1 pede — *o que é o planejamento, em um parágrafo que quem nunca viu entende* | Uma ocorrência de descrição integral da figura no corpus, ou uma fonte nova admitida ao corpus com esse conteúdo; sem uma das duas, o parágrafo seria escrito sem âncora |
| **Acrescentada por esta redação.** O que **não** aciona uma sessão de planejamento: as 14 ocorrências da dimensão 2 medem sessões abertas, e o corpus não registra sessão recusada | Um registro de recusa — pedido que chegou à figura e não abriu sessão —, com o motivo; não existe hoje no corpus fechado, e sem ele a metade negativa da dimensão 2 não tem lastro |
| **Acrescentada por esta redação.** O custo da figura sob a régua da `DPN-3`: toda a série da dimensão 7 é anterior aos três critérios sem número, e nenhuma observação descreve uma sessão dimensionada por coesão | Ao menos duas sessões de planejamento posteriores à `DPN-3` registradas em `docs/telemetria.tsv`, para que mediana e máximo deixem de coincidir e a série passe a ter dispersão |

> **Âncoras:** agregado, dimensão 10 (as cinco linhas da tabela); agregado, dimensões 1, 2, 6 e 7; `AE-5` do plano; `DPN-3`.
