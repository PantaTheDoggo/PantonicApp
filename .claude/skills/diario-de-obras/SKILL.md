---
name: diario-de-obras
description: Cria e mantém o diário de obras do projeto Pantonic* — kanban central em docs/DIARIO_DE_OBRAS.md com índice, status e arquivamento de planejamentos. Usar ao registrar um plano novo, abrir tíquete avulso, mudar status de tarefa ou condensar itens concluídos.
---

# diario-de-obras — kanban central do projeto

O diário de obras (`docs/DIARIO_DE_OBRAS.md`) é o documento centralizado onde todo planejamento
e tíquete avulso é arquivado, com identificação imediata do trabalho e seu status
(`GOVERNANCA.md` §4.2 no hub do kit).

## Estrutura do documento

```markdown
# Diário de Obras — <projeto>

**Diretiva de priorização:** <vazio = heurística padrão | "Priorize <iniciativa/bug>">

## Índice
| ID | Título | Status | Âncora |
|---|---|---|---|
| S1-T3 | <título curto> | in-progress | `## S1 — <sprint>` |
| TK-042 | <título curto> | ready | `## TK-042` |

## <um heading `##` por sprint/tíquete, apêndice cronológico>
```

- **Status:** os estados válidos, a máquina de transições e o alcance por objeto vivem em
  "Status — residência única" (abaixo). É o único lugar onde essa lista é enunciada; todo o
  resto do kit aponta para lá e não recopia.
- **IDs:** `S<n>-T<m>` para tarefas de sprint; `TK-<seq>` para tíquetes avulsos.
- O índice fica **no topo** e tem UMA linha por item — é por ele que o executor localiza sua
  tarefa sem ler seções irrelevantes. Toda mudança de status atualiza índice E seção.
- **A célula "Título" do índice NUNCA recebe prosa de resultado de execução.** O handover de
  fechamento (skill `passagem-de-bastao`) escreve o detalhe (o que foi feito, testes, consumo) na seção
  própria (`### <ID>` no diário) ou, para sprint que vive inteiramente em `docs/plans/P-*.md`
  (linha única no índice, sem heading no diário), numa seção do próprio plano (`## Notas de
  execução` / `## Achados da execução`) — nunca de volta na linha do índice. A célula do índice
  fica travada em ≤ ~1-2 frases + status + ponteiro, ponto final (aplicação de *Artefato de humano mínimo*, `GOVERNANCA.md` §4.2); se um handover for editá-la
  para além disso, é sinal de que falta a seção/satélite de destino — criar a seção, não apensar
  ao índice (defeito medido: `TK-DIARIO-SANEAMENTO`, célula de `SPRINT-REVEALENV` cresceu de
  ~2.5k para ~5k chars por handovers sucessivos apensando parágrafos). Mesmo mecanismo do
  "Guardrail anti-log-narrativo" abaixo, generalizado para toda tarefa — não só planos derivados.
- **Diretiva de priorização** é a linha imediatamente abaixo do título. Guia a
  skill `scrum-master` quando o usuário pede para seguir o backlog sem nomear tarefa. Vazia por
  padrão — heurística: destravar `blocked` → concluir `in-progress` (WIP de 1 iniciativa por vez)
  → bugs → demais por FIFO (ordem de entrada no índice).
- **Sprints multi-tarefa** (`## SPRINT-<nome>`) têm, imediatamente abaixo do `**Objetivo:**`, a
  linha `**Próxima tarefa da sprint:** <ID> (<ponteiro ao dossiê>)` — atualizada a cada handover,
  ANTES das `**Notas de execução:**` (que crescem por apensamento a cada tarefa concluída).
  Heading + essa linha cabem num Read curto, sem varrer notas de execução potencialmente longas.
  No mesmo ato, o mesmo autor reescreve a linha `**Fila corrente:**` do cabeçalho de
  `docs/DIARIO_DE_OBRAS.md` (primeiras 15 linhas, logo abaixo da Diretiva) com o novo ID, o
  ponteiro ao dossiê e a fila restante — é projeção da linha `Próxima tarefa`, não fonte nova.

## Status — residência única

Esta seção é o **único lugar** do repositório onde a lista de estados, a máquina de transições e o
alcance por objeto são enunciados. Todo o resto **aponta** para cá e não recopia.

**Escritor:** o `status` é **materializado** pelo `scrum-master`, e só por ele, em qualquer estado — a
regra vale para a lista inteira e não se repete linha a linha. A **autoria** é outro ato: o executor
é autor de `review` e de `blocked`, os dois valores que devolve ao fim da tarefa, e o `scrum-master`
os transcreve sem discricionariedade; nos demais estados, autoria e materialização são ambas do
`scrum-master` (fronteira fixada pela `DP-G` de `docs/plans/P-0734-execucao-autonoma.md`).

### Lista final

| estado | significado | o que dispara a entrada |
|---|---|---|
| `triage` | item registrado, ainda não avaliado quanto a entrar no backlog | registro do item na fila de entrada (`docs/plans/_INBOX.md`) |
| `ready` | item com o trabalho escrito e elegível para execução — em tíquete, só com ao menos um card `ready` | o tíquete é aberto já com o card (*Tíquete nasce executável*, abaixo); ou o planejamento cria a tarefa dentro de plano aprovado; ou um `blocked` é destravado |
| `blocked` | item que existe e não pode ser executado agora, com razão registrada | fato novo derruba a premissa; dependência não satisfeita; validação postergada; escalada do executor ou do laudo |
| `in-progress` | item em execução neste exato momento | o `scrum-master` delega o item a um contexto de execução |
| `review` | o entregável existe e aguarda aceite ou feedback de correção | o executor devolve a linha de retorno da `DP-G` |
| `done` | entregável aceito | laudo `seguir` ou `seguir com ressalva` acolhido e, onde o dono é o teste de sentido, o veredito dele |
| `cancelled` | item que não será executado, por qualquer motivo | a triagem recusa; o escopo é descartado; o item é absorvido por outro |

Plano cuja revisão foi pedida por quem executa ou orquestra não vai a `blocked` por isso: a **tarefa**
vai a `blocked` com a razão tipada `premissa`, e a parada vai à triagem do consultor, que devolve a
rota (`G-REPLAN`, `GOVERNANCA.md` §7 item 17). Só a rota `planejador` é caso de `blocked` **de plano**,
com a razão registrada, e abre uma **rodada de replanejamento** como próxima tarefa do plano: o plano
só sai de `blocked` quando a rodada fecha — a tarefa volta a `ready` ou `cancelled`, e a entrada
`RP-<n>` fica em `## Achados da execução` do plano. Nas rotas `resolve` e `modelador` o plano segue.

### Máquina de transições

Toda transição é **materializada** pelo `scrum-master`; a **autoria** de `in-progress` → `review` e
de `in-progress` → `blocked` é do executor (`DP-G`); a de `blocked` → `review` é do **consultor**, na rota `resolve` da triagem, ou do **planejador**,
na rodada de replanejamento (`G-REPLAN`, `GOVERNANCA.md` §7 item 17), e nunca do executor. A coluna
**gatilho** cita os dois — e só os dois — gatilhos que disparam ação automática.

| transição | quando | gatilho |
|---|---|---|
| (entrada) → `triage` | o item é registrado na fila de entrada | — |
| `triage` → `ready` | a triagem aceita: o item entra no kanban | — |
| `triage` → `cancelled` | a triagem recusa | — |
| `ready` → `in-progress` | o `scrum-master` delega (uma tarefa por contexto, WIP de 1) | — |
| `ready` → `blocked` | fato novo derruba a premissa, com razão registrada | — |
| `ready` → `cancelled` | escopo descartado ou absorvido por outro item | — |
| `blocked` → `ready` | a razão registrada não se aplica mais | — |
| `blocked` → `cancelled` | o bloqueio é permanente ou a rota mudou | — |
| `blocked` → `review` | a triagem do consultor (rota `resolve`) ou a rodada de replanejamento corrigiu o **aceite** de um `blocked premissa` cuja entrega material já está na árvore (`G-REPLAN`, saída (c)); nenhum retorno novo de executor é exigido | **gatilho 1** — o `scrum-master` invoca o `pantonic-reviewer` |
| `in-progress` → `review` | o executor devolve a linha de retorno da `DP-G` | **gatilho 1** — o `scrum-master` invoca o `pantonic-reviewer` |
| `in-progress` → `blocked` | o executor para e escala | — |
| `review` → `done` | laudo `seguir` ou `seguir com ressalva`, mais o aceite do dono onde ele é o teste de sentido | **gatilho 2** — o `scrum-master` escreve o RDO |
| `review` → `in-progress` | laudo `refazer`, dentro do teto de retentativa; a retentativa é agente novo | — |
| `review` → `blocked` | laudo `escalar`, ou `refazer` com o teto de retentativa esgotado | — |
| `ready` / `in-progress` / `blocked` → `done` (**plano**) | nenhuma tarefa do plano está aberta, ao menos uma é `done`, e o dono deu o veredito sobre o documento de validação (skill `entrega-de-encerramento`) | **gatilho 3** — `encerrar.py plano` escreve o relatório de entrega e a linha do diário |

**Fechamentos.** (a) `done` e `cancelled` são **terminais** e não têm saída: retrabalho depois do
`done` nasce como **item novo**, porque reabrir falsificaria o registro. (b) Só as três transições
marcadas disparam ação automática; **nenhuma outra dispara nada**. (c) Item que termina em
`cancelled`, e item que para em `blocked` por escalada, **não** disparam RDO — o gasto continua
registrado pela telemetria. (d) Plano não passa por `review` (o aceite é das tarefas): o `done`
dele é a linha de plano acima, aceita pelo `backlog.py` só com toda tarefa terminal (`TK-88`).

### Alcance por objeto

A lista governa a tarefa e, por extensão, todo item do kanban: o índice de
`docs/DIARIO_DE_OBRAS.md` tem **uma** coluna `Status`, compartilhada por iniciativa, plano, tíquete
e tarefa. **Exceção declarada, única:** `superseded` é estado **exclusivo de plano/iniciativa** e
**não é estado de tarefa** — tarefa que a realidade tornou obsoleta é `cancelled`; plano cuja
premissa caiu é `superseded`, com ponteiro para o substituto. Nem todo estado se aplica a todo
objeto:

| objeto | estados aplicáveis |
|---|---|
| tíquete | `ready`, `in-progress`, `review`, `done`, `blocked`, `cancelled` — os mesmos da tarefa, e **sem `triage`**: o tíquete nasce com o card (*Tíquete nasce executável*) |
| tarefa (de plano ou de sprint) | `ready`, `in-progress`, `review`, `done`, `blocked`, `cancelled` — **sem `triage`** (a tarefa nasce de plano já aprovado) e **sem `superseded`** |
| plano / iniciativa | `ready`, `in-progress`, `blocked`, `done`, `cancelled`, `superseded` — **sem `review`** (o aceite é das tarefas; o veredito do dono no fecho da sprint é tarefa em `review`) e **sem `triage`** (ideia de plano é triada como tíquete) |

### Tíquete nasce executável

Tíquete é trabalho, não lembrete. Quem registra um problema no diário escreve, **no mesmo ato**, o
card que o resolve — `### TK-<n><letra>` na forma de *Formato de uma tarefa*, com `Arquivos-alvo`,
`Verificação` e `Pronto quando` medidos no ato. Tíquete `ready` sem card `ready` não existe: o
`ready` diz que o loop pode despachar o trabalho agora, e é só isso que ele diz.

No ato de registrar, o problema cai em um de três casos, e só três:

1. **A correção é conhecida** — o card nasce `ready`.
2. **A correção depende de uma medida** — o card é de `classe investigacao`: mede, publica o
   número ou o fato e declara, para cada resultado possível, o que se segue; nenhum ramo fica para
   decidir depois.
3. **A correção depende de decisão do dono ou de outro item** — o card nasce `blocked`, razão
   `dependencia`, nomeando a decisão ou o item de que depende e, quando é decisão do dono, as
   opções e o que cada uma implica. A pergunta vai ao dono no relatório seguinte.

Bloqueio de tíquete é só o do caso 3. "Falta escrever o card" não é bloqueio: é tíquete que não foi
aberto — o `backlog.py check` o acusa como `C-15`. No loop, achado com rota `tíquete` vai ao
consultor, que abre o tíquete já com o card — o mesmo ato do card corretivo que ele já escreve. Card vivo que o `rdo.py` não lê é `C-16` no `backlog.py check`.

## Gramática legível por máquina

Transcrição normativa de `docs/plans/P-0739-backlog-instrumento.md` §2.1–§2.4 e §2.7 — é a
gramática que `.claude/tools/backlog.py` (§3 do mesmo plano) lê e escreve. Esta seção é a
residência única do texto; o plano de origem não a recopia depois da transcrição. A subseção
"Modelo de domínio (seção do plano)" transcreve `docs/plans/P-0743-modelo-de-dominio.md` §5 e §15 —
onde as duas divergem, governa a §15 — e é lida por `.claude/tools/modelo.py`.

### Item e residência

| item | residência viva | cabeçalho | campos obrigatórios logo abaixo |
|---|---|---|---|
| plano em pasta | `docs/plans/P-<n>-<slug>/plano.md` | `# P-<n> — <título>` (linha 1) | nas 20 primeiras linhas: `**Prefixo das tarefas no diário:** \`<PFX>-T<n>\``; **sem** linha `**Status:**` — o estado é a linha `plano` de `estado.tsv`, na mesma pasta |
| plano legado | `docs/plans/P-NNNN-<slug>.md` | `# P-NNNN — <título>` (linha 1) | nas 20 primeiras linhas: `**Status:** \`<estado>\`` e `**Prefixo das tarefas no diário:** \`<PFX>-T<n>\``; opcional `**Ordem de execução:** ID → ID → …` (1ª ocorrência vence; ausente = ordem dos cabeçalhos) |
| tarefa de plano | no plano (`### <ID> …`) | `### <ID> — <título> [<modelo>[ + dono] · classe <classe>[ · teto <n>]]` (`DP-C`; ` + dono` marca aceite do dono, ` · teto <n>` é sufixo legado tolerado e ignorado — `DB-20`) | plano legado: 1º bullet `- **Status:** \`<estado>\` · AAAA-MM-DD[ · <razão de 1 linha>]`; opcionais `- **Depende de:** \`ID\`[, \`ID\`]`, `- **Tipo:** bug`; `- **Notas de execução:**` com sub-bullets `  - AAAA-MM-DD \`<estado>\` — <texto>` apensados pelo instrumento; plano em pasta: sem bullet de Status nem de Notas de execução — estado, razão e nota na linha da tarefa em `estado.tsv` |
| tíquete | `docs/DIARIO_DE_OBRAS.md` | `## TK-<n> — <título>` (nível 2, **sem** bracket — tíquete não tem modelo nem classe; `DB-17`) | mesmos campos da tarefa (`Status`, `Tipo`, `Notas de execução`); nasce com ao menos uma subtarefa (*Tíquete nasce executável*) |
| subtarefa de tíquete | `docs/DIARIO_DE_OBRAS.md`, dentro da seção do tíquete-pai | `### TK-<n><letra> — <título> [<modelo> · classe <classe>]` (`DP-C` completa, igual à tarefa de plano; `DB-17`) | mesmos campos da tarefa |

Uma tarefa é *do* plano cujo prefixo casa com o dela; `TK-<n><letra>` é *do* tíquete `TK-<n>`.

### Índice do diário

`| <ID> | <título curto> | <estado>[ <done>/<total>] | <âncora> |` — a célula `Status` contém **só**
o token do vocabulário, opcionalmente seguido de `<done>/<total>` para plano/tíquete com subtarefas.
Nada mais. Título e âncora seguem de autoria humana (o instrumento só cria a linha no `drain` e só
reescreve a célula `Status`).

### Cabeçalho do diário (bloco gerado)

```markdown
**Diretiva de priorização:** [Priorize `<ID>`[, `<ID>`…]] [— <texto livre>]
<!-- fila:gerada -->
**Fila corrente:** `<ID>` — <título> (`<arquivo>:<l1>-<l2>`) · fila: <ID2>, <ID3> · ready <n> · blocked <m> · in-progress <k>
- `P-<n>` (`<estado>`, <done>/<total>): próxima `<ID>`
<!-- /fila:gerada -->
```

O instrumento lê só os tokens `` `ID` `` antes de ` — ` na diretiva; o texto livre é para humanos.
Tudo entre os marcadores é reescrito a cada verbo de escrita; humano não edita ali.

### Inbox de planos

Linha viva: começa com `- ` e contém um caminho `docs/plans/P-<n>-<slug>/plano.md` ou, legado, `docs/plans/P-NNNN-<slug>.md` (o resto é livre).
Drenada: prefixada `- [drenado AAAA-MM-DD] ` e movida **verbatim** para `_INBOX_HISTORICO.md`.
Contador: `**Próximo id de plano: P-<n>.**` — `drain` o recalcula como `max(id visto) + 1`, na largura de dígitos que o contador já tem (projeto novo: `P-0`, `P-1`…; hub: `P-0750`…).

### Estado do plano em pasta (`estado.tsv`)

`docs/plans/P-<n>-<slug>/estado.tsv`, separador TAB (escrito `<TAB>` aqui). Primeira linha
`id<TAB>tipo<TAB>status<TAB>razao<TAB>data<TAB>nota`; depois uma linha por item, estado corrente,
reescrita no lugar. `id` = `P-<n>` na linha do plano (a primeira) ou o id da tarefa; `tipo` ∈
{`plano`, `tarefa`}; `status` no vocabulário acima; `razao` ∈ {`-`, `dependencia`, `premissa`};
`data` `AAAA-MM-DD`; `nota` uma linha sem TAB, ou `-`. O planejador grava o arquivo na Fase 3a,
junto do esqueleto, só com a linha do plano (`blocked`, razão `dependencia`), e acrescenta uma
linha por card ao registrar o plano; depois só `backlog.py status` o reescreve. `check` acusa
`C-13` (card sem linha, linha
sem card, arquivo ausente ou fora do esquema) e `C-14` (linha `**Status:**` em `plano.md`).
Busca sem leitura: `rg "^<id>\t" docs/plans/*/estado.tsv`.

### Modelo de domínio (seção do plano)

Seção `## 1. Modelo conceitual` do plano (`GOVERNANCA.md` §3.2), delimitada pelo próximo heading de
nível 2. Dentro dela, nesta ordem:

| elemento | forma | regra |
|---|---|---|
| cabeçalho | `**Estado do modelo:** versão <n> · AAAA-MM-DD · autor: <papel> · <k> operações · <p> propriedades · situação: <vigente \| pendente>` | linha única; obrigatória (`V13`); `<n>` monotônico e `situação` é `vigente` na seção `## 1` |
| objetos | `### 1.1 Objetos` + tabela `\| objeto \| o que é \| propriedades \| contrato \| origem \| lastro \| tipo \|`; `<objeto>` é um nome em linguagem corrente, único na tabela; `<propriedades>` é uma lista separada por vírgula, em linguagem corrente, não vazia; `<origem>` é `externo` ou `OP-<n>`; `<lastro>` é o trecho do enunciado (`## 0`) ou do prompt de origem, citado ou apontado, não vazio, e a coluna de lastro é a coluna cujo cabeçalho começa com `lastro`, que pode qualificar a âncora (`lastro na §0`, `lastro no prompt`); `<tipo>` é `escopo`, `externo` ou `medição`, na coluna cujo cabeçalho é `tipo` | obrigatória (`V13`); objeto sem propriedade é violação (`V15`); `<origem>` `OP-<n>` existe no fluxo (`V7`); objeto de origem `externo` é citado por alguma operação (`V6`) |
| operações | `### 1.2 Fluxo de operações`; cada operação é o par de linhas: `- **OP-<n>** — <texto>` e, na linha seguinte, `  - \`precisa de: <objeto>[, <objeto>]\` · \`altera: <objeto>.<propriedade>[, <objeto>.<propriedade>]\` · \`tarefas: <ID>[, <ID>]\` · \`lastro: <trecho>\`` | numeração `1..k` na ordem do encadeamento, sem salto (`V8`); `<n>` único (`V11`); `<texto>` sem crase e sem `/` (`V12`); todo `<objeto>` existe na tabela de objetos (`V5`); todo par `<objeto>.<propriedade>` de `altera:` existe na tabela de objetos (`V16`); toda `<ID>` existe como `### <ID> — …` no plano (`V3`); lista de tarefas não vazia (`V1`); operação com `<n>` maior que 1 cita ao menos um objeto de origem `OP-<m>` (`V9`), e esse `<m>` é menor que `<n>` (`V10`). O quarto campo `lastro:` é opcional na forma e obrigatório na doutrina, enquanto o acervo vivo não o declara. Subtítulos `**A. …**` entre operações são livres e ignorados |
| estado | `### 1.3 Estado inicial e estado final` + tabela `\| propriedade \| estado inicial \| estado final \| lastro \|`; a célula `propriedade` é `<objeto>.<propriedade>`; `estado inicial` é o retrato antes da implementação; `estado final` é o desejo do dono, quantificável ou qualificável | obrigatória (`V13`); toda propriedade da tabela de objetos tem exatamente uma linha aqui (`V17`) |
| versões | `### 1.4 Registro de versões` + tabela `\| versão \| data \| situação \| por \|`; `situação` é `vigente`, `pendente` ou `obsoleta`; a linha `obsoleta` registra por aceite de qual versão ela caiu, e o conteúdo dela não fica no plano | obrigatória (`V13`); exatamente uma linha `vigente` (`V19`) |
| campo do card | `- **Operação do modelo:** \`OP-<a>\`[, \`OP-<b>\`]` como campo de todo `### <ID> — …` do plano, seguido, por operação citada, de dois sub-bullets: `  - OP-<a>: <texto copiado>` e `  - precisa de: <objeto> — <contrato copiado>[; <objeto> — <contrato copiado>]` | obrigatório em toda tarefa do plano (`V2`); toda `OP-<a>` citada existe (`V4`); os dois sub-bullets existem para cada operação citada (`V14`) |

**Lastro, por elemento.** Todo objeto, toda operação e toda propriedade da seção tem lastro
declarado — a âncora num trecho do enunciado do problema (`## 0. O problema, verbatim`) ou do prompt
que originou o plano. Elemento sem âncora não entra no modelo. O enunciado alimenta a seção por
**duas vias**: a **via de estado**, o trecho que descreve como as coisas estão ou como deverão
estar, que popula `### 1.3`; e a **via de operação**, o trecho que pede ação, que popula `### 1.2` e
é o que o plano faz diante do vão entre os dois estados. Metade disso é de máquina: na tabela de
`### 1.1`, o `check` afere a presença da coluna cujo cabeçalho começa com `lastro` — o rótulo
identifica a residência, e o autor qualifica a âncora sem sair da forma; o lastro da operação, o da
propriedade e a pertinência do trecho citado são guarda do Marco. A forma vale para plano vivo:
plano em status terminal não se migra.

**Requisito secundário, a residência do elemento sem lastro.** Elemento sem lastro não é proibido
de ser entregue — é proibido de participar do modelo. O elemento com lastro é o requisito
funcional e entra no modelo como contrato; o elemento sem lastro é não fundamental e reside na
seção de nível 2 nomeada `Requisitos secundários`, em qualquer posição do plano, fora da `## 1`,
em tabela
`| requisito | por que o agente o julga necessário | quem responde |`, uma linha por entrega que o
agente julga necessária e que o enunciado não pediu.
Elemento dessa seção não entra no modelo e não é aferido por lastro.
Ele é transparente para o dono — visível e declarado, não submetido à aprovação dele — e a
responsabilidade por ele é inteira do agente.

**Objeto e propriedade, na decomposição.** O enunciado se decompõe primeiro em objeto e
propriedade: o que o plano constrói é objeto, e o que converge de um estado inicial a um estado
final distinto é propriedade dele — **descrição de estado não vira objeto próprio**, entra como
propriedade e aparece na `### 1.3`. Operação é o ato que altera propriedade, e não possui
propriedade (`GOVERNANCA.md` §3.2). Propriedade escrita como objeto próprio é promoção indevida e
infla a `### 1.1` com linhas que nenhuma operação constrói: `V15` cobra que o objeto tenha
propriedade, não que ele seja objeto. Nenhuma validação apanha a promoção indevida; a guarda é o
marco. Operação escrita com mais de uma oração é operação mal recortada: cada oração vira operação própria, e a guarda também é o marco.

**Tipo de objeto, na tabela.** A coluna `tipo` de `### 1.1` diz o que o plano faz com cada objeto:
`escopo` para o que ele transforma — e que por isso limita a atuação dele —, `externo` para o que
gera insumo ou evento sem ser transformado, e `medição` para o que porta a propriedade que prova a
transformação (`GOVERNANCA.md` §3.2). Ela não substitui `origem`, que diz quem produz o objeto.
Nenhuma operação altera propriedade de objeto `externo` ou de `medição`; tarefa que o preveja é
colateral e se escala. Como o `lastro`, a coluna é **obrigatória na doutrina e opcional na forma**
enquanto o acervo vivo não a declara: o `check` não a exige, e a guarda da classificação é o marco.

**Versão pendente, como bloco irmão.** Uma versão pós-drift não sobrescreve a vigente: nasce como a
seção `## 1A. Modelo conceitual — versão pendente de validação`, imediatamente depois da `## 1` e
delimitada pelo próximo heading de nível 2, com a mesma estrutura interna de `### 1.1` a `### 1.3` e
o cabeçalho em `situação: pendente`. As duas coexistem até o marco. `modelo.py show` mostra a
**vigente** por omissão, a pendente com `--pendente` e a diferença entre as duas com `--drift`.
Aceita a pendente, ela ocupa a `## 1` e a `## 1A` desaparece; recusada, a `## 1A` é eliminada e a
`## 1` permanece sem marca.

**Andamento, nunca gravado.** Nenhum elemento da seção carrega estado. `modelo.py show` deriva:
operação `concluída` quando todas as tarefas dela estão `done` ou `cancelled`; `em curso` quando
alguma está `in-progress` ou `review`; `prevista` nos demais casos. O **estágio atual** é a
primeira operação não `concluída`, e é `concluído` quando não há nenhuma.

Plano sem a seção `## 1. Modelo conceitual`, e plano com a seção mas sem o heading
`### 1.2 Fluxo de operações`, são **forma anterior**: `modelo.py check` sai `2` e nada se exige
deles.

## Formato de uma tarefa

Uma tarefa é a **materialização de uma operação do modelo** (`GOVERNANCA.md` §3.2): o `Objetivo`
copia o texto da operação, o campo `Operação do modelo` traz o texto e os contratos copiados
(gramática em "Modelo de domínio (seção do plano)", acima), e o `Pronto quando` deriva do estado
final das propriedades que a operação altera. Um card por operação; card corretivo (`T<n>a`)
soma-se à operação do card que corrige.

```markdown
### S1-T3 — <título>  [status]
- **Objetivo:** <uma frase>
- **Operação do modelo:** `OP-<n>` + os dois sub-bullets copiados (texto da operação; `precisa de:` com contrato)
- **Arquivos-alvo:** <caminho:linha (âncora já conhecida); caminho §seção quando o alvo ainda não
  tem linha fixa no momento do planejamento; caminho (novo) para arquivo que a própria tarefa cria>
- **Contratos/classes:** <Protocols, classes envolvidas>
- **Testes:** TF-<id> (novo), TR-<id> (tranca), suítes a rodar
- **Verificação:** <comando copiado do terminal — não a intenção de verificar; para tarefa sem
  artefato executável, a ação concreta aplicada e o resultado registrado>
- **Pronto quando:** <por propriedade que a operação altera, o estado final da ### 1.3 e a verificação que o mede>
- **Handover:** <data> · para `<ID da sucessora>`  ← escrito por `encerrar.py handover`, nunca à mão;
  sub-bullets fixos `Entregue` (com caminho:linha), `Contrato`, `Não refazer`, `Pendente`; o `next`
  o devolve à sucessora sob `=== HANDOVER DE <ID>`
- **Notas de execução:** <≤ ~5 linhas + ponteiros (decision record, commit); preenchido no
  fechamento — custo composto: nota extensa é relida por todo agente em toda tarefa futura>
```

`caminho:linha` é a forma preferida — mas é ponteiro de leitura, envelhece e não se mantém como
contrato (`GOVERNANCA.md` §4.2). `§seção` e `(novo)` são as formas mais fracas ainda aceitas,
quando a linha exata não existe no momento do planejamento (`C-06`, padrão de `BM-20§D5`).

## Operações

1. **Registrar plano** — apensar a seção do sprint com o checklist completo; inserir cada tarefa
   no índice como `ready`.
   **Gate de publicação (G-PLANREADY, `GOVERNANCA.md` §7 item 12) — verificar ANTES de apensar:**
   o plano está fechado (id sequencial; `T1..Tn` em ordem de dependência, com objetivo/"pronto
   quando"/modelo; nenhuma decisão owner-gated postergada; linear, sem "TBD" nem referência para
   frente)? Se não, o registro **não acontece**: devolve ao planejamento o que falta fechar. Quando
   uma parte depende de insumo futuro, registra-se o plano fechado agora e o dependente nasce como
   **a última tarefa** do plano que produz o insumo — nunca um plano com vão.
   Plano que antecipa múltiplas rodadas de Q&A mantém tabela única "Decisões" (id → valor → 1
   linha) referenciada pelas seções, em vez de restatar cada regra em prosa em cada seção
   (reduz fan-out de Edits por rodada de confirmação).
   Ao criar um plano novo, invocar a skill `checar-versao-kit` (`GOVERNANCA.md` §10 no hub) antes
   de fechar o registro: se a versão local do kit bate com a do hub, segue em silêncio; se
   divergir, pergunta ao dono "atualizar agora ou postergar?" e registra a resposta no próprio
   plano; se a rede estiver indisponível, anota "não verificado" e segue sem bloquear.
2. **Mudar status** — forma canônica: `python .claude/tools/backlog.py status <ID> <estado>
   [--razao "…"] [--nota "…"]` (verbo de `docs/plans/P-0739-backlog-instrumento.md` §3); a prosa
   abaixo descreve o efeito. Efeito: atualizar a linha do índice e o `[status]` da seção; `blocked`
   exige razão registrada em "Notas de execução".
3. **Condensar** — quando itens `done`/`cancelled` dominarem o documento (ou ele passar de ~500
   linhas): (a) mover as seções concluídas para `docs/DIARIO_HISTORICO.md` (append-only), deixando
   no diário só a linha do índice com ponteiro; (b) se passar de 500 linhas mesmo assim, criar
   entrada no `docs/DOC_MAP.md`.
   Gatilhos adicionais: (c) uma única seção — mesmo `ready` — que passe de ~300 linhas migra
   para arquivo satélite próprio (`docs/DIARIO_<ID>.md` ou `docs/audits/<ID>_LOG.md`,
   append-only), ficando no diário só a linha de índice + "última rodada: N / último achado:
   M"; (d) o dono do gatilho é o fechamento de cada tarefa (skill `passagem-de-bastao`) — não existe
   "ninguém verifica". Tíquete acumulador (log de evidência que não fecha por desenho) nasce
   já como arquivo satélite + linha de índice, nunca como seção crescente do diário — também
   elimina colisão de append concorrente entre sessões.
4. **Registrar diretiva de priorização** — forma canônica: `python .claude/tools/backlog.py
   diretiva "Priorize \`ID\`[, \`ID\`…] — …"` (verbo de `docs/plans/P-0739-backlog-instrumento.md`
   §3); a prosa abaixo descreve o efeito. Efeito: sobrescrever a linha "Diretiva de priorização" no
   topo do diário. Só acontece por pedido explícito do usuário (ex.: "Priorize iniciativa X",
   "priorize tarefas desse bug") — nunca inferida implicitamente de uma conversa. Ficar vazia
   quando o usuário não nomeou prioridade (heurística padrão assume).
5. **Drenar inbox de planos** — forma canônica: `python .claude/tools/backlog.py drain [--data
   AAAA-MM-DD]` (verbo de `docs/plans/P-0739-backlog-instrumento.md` §3); a prosa abaixo descreve o
   efeito. Efeito: no início de qualquer sessão que vá tocar o diário (em especial
   ao abrir a skill `scrum-master`), ler `docs/plans/_INBOX.md` — única fonte da drenagem; o
   pickup nunca lê o histórico. Cada linha não drenada aponta
   para um `docs/plans/P-<n>-<slug>/plano.md` gravado por um agente de planejamento (possivelmente em
   paralelo com outros); promover cada plano ainda não promovido para uma entrada no índice +
   heading do diário (ou manter o heading no próprio `docs/plans/P-*.md` com só a linha de índice
   apontando para lá, se o plano for grande), e marcar a linha do inbox como drenada (ex.:
   riscar/prefixar `[drenado]`) movendo-a, verbatim, para `docs/plans/_INBOX_HISTORICO.md` — nunca
   apagá-la nem reescrevê-la lá; `_INBOX.md` continua append-only para as linhas ainda vivas. O
   `NNNN` do novo plano vem do contador declarado no cabeçalho do `_INBOX.md` (alocar = maior id já
   registrado + 1); atualizar a linha de próximo id do `_INBOX.md` no mesmo ato de registrar o
   plano.
6. **Abrir tíquete** — num único ato: a linha do índice, a seção `## TK-<n> — <título>` com o fato
   medido e o card `### TK-<n>a` (ou os cards) no caso que *Tíquete nasce executável* determinar.
   Tíquete aberto sem card não é registrado; o `backlog.py check` fecha com zero violação antes de
   o ato terminar.
7. **Passar o bastão, fechar tarefa, fechar plano** — forma canônica: `python .claude/tools/encerrar.py
   handover --plano <plano> --tarefa <ID> --entregue "…" --contrato "…" [--nao-refazer "…"]
   [--pendente "…"] [--para <ID>]...`, `python .claude/tools/encerrar.py tarefa
   --plano <plano> --tarefa <ID> [--resumo "…"] [--pendencia "…"] [--achado "<texto>" "<rota>"]...`
   e `python .claude/tools/encerrar.py plano --plano <plano> --veredito "<frase do dono>"` (`TK-88`;
   efeito descrito na skill `scrum-master`, Passo 9 e *Quando a janela fecha o PLANO*). Efeito do
   handover: o campo `- **Handover:**` no card (o que a sucessora espera da tarefa, de máquina),
   que `next` devolve sob `=== HANDOVER DE <ID>`. Efeito da
   tarefa: `review` → `done` projetado (card, índice, `Fila corrente`, `estado.tsv`), RDO nas três
   seções com o pacote transcrito do laudo, linha de telemetria garantida, achados como `AE-<n>`
   com rota. Efeito do plano: `done` do plano projetado, relatório de entrega (`entrega.md` /
   `docs/plans/_ENTREGA-<id>.md`) e **uma** linha no cabeçalho do diário. Os dois recusam sem
   escrever quando falta insumo (laudo, consumo medido, RDO de tarefa `done`, rota de achado,
   documento de validação) — a regra não manda fazer o que o instrumento recusa.

## Planos derivados de uma investigação em curso (reconciliação obrigatória)

Uma iniciativa complexa gera descobertas, e cada descoberta tende a gerar um plano novo. O defeito
que isto governa: o plano novo passa a coexistir em silêncio com o de origem, e o executor volta a
"continuar" o plano de origem já superado — às vezes refazendo perguntas já respondidas. **No ato
de registrar um plano derivado**, classifique-o e aplique o efeito ao plano de origem. A
classificação é explícita e imediata, nunca fica implícita para "resolver depois":

- **(A) Fato novo que pode alterar o passo subsequente, mas ainda não substitui a rota** (uma
  verificação levantou uma hipótese que muda o próximo passo; a estratégia geral segue): o plano de
  origem vai para **`blocked`**, com razão registrada apontando o fato/plano novo. Não é escolhível
  até o fato ser resolvido. Destrava quando a hipótese é confirmada/descartada.
- **(B) Plano que muda completamente o entendimento do plano atual** (a premissa que o sustentava
  caiu; a rota agora é outra): o plano de origem inteiro vira **`superseded`** — obsoleto, fora do
  backlog, com ponteiro `substituído por: <plano novo>`. Código já entregue permanece; nenhuma
  tarefa nova sai dele. **Nunca deixar dois planos vivos disputando a mesma iniciativa.**
- **(C) Passo de verificação/validação enquanto há implementação pendente na mesma iniciativa**: a
  validação é **postergada** — registrada como `blocked` com razão `validação postergada até
  <tarefas de implementação> done`, e só volta a ser escolhível quando **todas** as implementações
  vivas fecharem. Não se abre rodada de validação enquanto existe implementação em aberto que possa
  invalidá-la (evita revalidar o que a próxima tarefa vai mudar).

**Regra de convergência:** uma iniciativa tem no máximo **UM** plano vivo (`ready`/`in-progress`/
`blocked` não-postergado) por vez. O plano vivo é sempre o mais recente cuja premissa não foi
contradita. Se ao drenar o inbox ou escolher tarefa você achar 2+ planos vivos na mesma iniciativa,
é sinal de que uma reconciliação A/B/C foi pulada: **rebasear antes de escolher** — marcar
`superseded` os planos cuja premissa a realidade atual contradiz, `blocked` os travados por fato
novo, e verificar se algum gap já foi tratado (por outra rota) mas ficou sem registro.

**Guardrail anti-log-narrativo:** uma célula da coluna "Título" do índice que vira **log de
descobertas sucessivas** é o mesmo defeito de uma seção que cresce demais — o gatilho de satélite
vale para ela: a saga migra para `docs/DIARIO_<ID>.md` (append-only), ficando no índice só **uma
frase** + status + ponteiro. Cada handover da saga escreve no satélite, nunca engorda a célula do
índice.

## Regras

- Grep pelo ID (`^### S1-T3` ou `^## TK-042`) antes de qualquer Read — nunca leia o diário
  inteiro.
- Nunca deletar itens: estados finais são `done` ou `cancelled`, e depois condensação para o
  histórico.
- Planos de agentes de planejamento paralelos nunca são escritos direto no diário: cada agente
  grava seu plano completo em `docs/plans/P-<n>-<slug>/plano.md` e apensa uma linha a
  `docs/plans/_INBOX.md` — evita conflito de edição concorrente no mesmo arquivo.
- Tíquete nascido de achado durante a execução de um plano vive na seção
  `## Achados da execução` apensada ao FINAL do próprio `docs/plans/P-*.md` (nunca fora do
  plano); o diário guarda só a linha de índice com âncora para lá. `TK-*` com seção no diário
  é reservado a demanda sem plano de origem. A sprint só flipa para `done` com todos os
  achados do plano triados (rota registrada) — ver skill `passagem-de-bastao` §2.
