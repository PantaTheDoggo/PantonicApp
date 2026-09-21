---
name: scrum-master
description: Conduz o loop de execução de um plano Pantonic* — despacha as tarefas do plano em sequência ao executor e ao reviewer, roteia pelo veredito calculado e encerra a janela por coesão e ocupação de contexto, sem round-trip com o dono a cada tarefa. Usar quando o pedido for tocar um plano inteiro em regime autônomo, e não uma tarefa avulsa.
---

# scrum-master — o loop de execução de um plano

Procedimento de **Orquestração** (`GOVERNANCA.md` §3) no **contexto principal**: cada tarefa é
executada por um subagente e julgada por outro. Esta skill é o **ponto de entrada único** da
execução de backlog — plano nomeado ou "execute o próximo passo" —, e o maquinário de transição
entre uma tarefa e a seguinte é a `.claude/skills/passagem-de-bastao/SKILL.md`, interna a ela. Não
implementa, não julga entrega e não substitui decisão do dono (`.claude/global/CLAUDE.md` Regra 8).

## Estado do loop

Três contadores, e só três.

| contador | zera em | onde é lido | para que serve |
|---|---|---|---|
| retentativas da tarefa corrente | início de cada tarefa | contador do loop | roteamento de `A6` e `A7`, com **uma** retentativa por tarefa |
| tarefas fechadas na janela | início da janela | contador do loop | relatório de encerramento |
| consumo acumulado da janela | início da janela | soma de `tokens_k` das linhas da janela em `docs/telemetria.tsv` | medida informativa, que alimenta a série |

Além deles: **plano corrente**, **tarefa corrente** e **fila corrente** (ordem do plano,
**reordenada em execução** por `A3a`). Nada mais entra. Fonte normativa:
`docs/plans/P-0734-execucao-autonoma.md` `### DP-B` (retentativa/precedência do bloco A);
`GOVERNANCA.md` §4.3 e `### DP-Q` (encerramento); `### DP-G` item 3 (reordenação da fila).

## Fluxo

Dez passos, nesta ordem.

### Passo 1 — Gate de modelo do contexto principal

- **Gatilho:** invocação da skill, antes de qualquer despacho.
- **Entrada:** modelo ativo do contexto principal.
- **Ação:** rodar `.claude/skills/modelo-por-fase/SKILL.md` (fase **orquestração**, matriz
  `GOVERNANCA.md` §3). Modelo diferente do exigido: **PARA e pede `/model` ao dono**.
- **Saída:** modelo conferido, ou parada com o `/model` pedido.

### Passo 2 — Seleção da próxima tarefa do plano

- **Gatilho:** passo 1 conferido, ou tarefa anterior fechada com "segue" no passo 10.
- **Entrada:** fila corrente do plano; `status` das tarefas no índice de `docs/DIARIO_DE_OBRAS.md`.
- **Ação:** `python .claude/tools/backlog.py next` devolve a próxima tarefa e o dossiê dela — a
  primeira ainda não fechada na fila corrente. Sem tarefa aberta: encerrar pelo relatório de
  janela.
- **Saída:** identificador da tarefa corrente e o cabeçalho dela, na gramática de
  `GOVERNANCA.md` §3 (*A unidade de trabalho*):
  `### <ID> — <título> [<modelo>[ + dono][ · esforço <esforço>] · classe <classe>[ · teto <n>]]`.

### Passo 3 — Gates herdados

- **Gatilho:** tarefa corrente selecionada.
- **Entrada:** dossiê da tarefa no plano; estado do plano.
- **Ação:** rodar `G-PLANREADY` (`GOVERNANCA.md` §7, item 11) e o Gate de delegação
  (`.claude/skills/passagem-de-bastao/SKILL.md`, seção "Gate de delegação", sete itens), sem
  recopiar o texto de nenhum dos dois. Recusa de qualquer um: **não delega** — vai ao passo 10 por `B3`.

  Terceiro gate, mecânico: `python .claude/tools/modelo.py check --plano <plano>`
  (`GOVERNANCA.md` §3.2). Exit `1`: **não delega** — o stderr vai à razão e a tarefa cai em
  `B3`. Exit `2`: plano anterior à doutrina do modelo; segue, com a nota "sem modelo" no
  relatório. Exit `0`: segue.

  Aprovados os três, e **antes** de delegar, materializar `ready` → `in-progress` no kanban
  (`DP-G` item 1, consequência 3) — ato exclusivo do `scrum-master`.
- **Saída:** tarefa materializada em `in-progress` e liberada para despacho, ou parada com o que
  falta fechar.

### Passo 4 — Despacho do executor

- **Gatilho:** gates do passo 3 aprovados e tarefa materializada em `in-progress`.
- **Entrada:** dossiê da tarefa copiado do plano; modelo declarado no cabeçalho.
- **Ação:** garantir o diretório `.claude/estado/` (ele viaja versionado com `.gitkeep`, `DM-10`
  do `P-0740`; recriá-lo se tiver sido apagado nesta máquina) e gravar
  `.claude/estado/tarefa-corrente.json` (objeto único: `tarefa`, `projeto`,
  `modelo`, `plano`, `despachado_em` ISO 8601), insumo do hook `SubagentStop` (`T55`) para
  `docs/telemetria.tsv`. Capturar `git rev-parse HEAD` como `<ref>` (schema `DP-S`), usada no
  passo 6 (`AUT-T5b`).

  Invocar `pantonic-executor` com `model` **igual ao do cabeçalho** (vence o `model:` do agente),
  com o dossiê da tarefa e a instrução de devolver **uma única linha**, domínio fechado (`DP-G`
  item 2):

  ```
  <tarefa> review [pendencia=<uma linha>]
  <tarefa> blocked motivo=<dependencia|premissa|ferramenta> <uma linha de razão>
  ```

  Desempate (`DP-G` item 3): na dúvida sobre o motivo, `premissa`. RDO e guardrails de
  arquitetura não vão no despacho.
  O despacho cola, junto do dossiê, as **âncoras** (arquivo, linha e texto do ponto a editar)
  re-derivadas no ato e o **range de linhas do bullet de fechamento anterior** quando a tarefa
  fecha em plano em andamento.
- **Saída:** uma linha de retorno do executor.

### Passo 5 — Recepção do retorno do executor

- **Gatilho:** retorno (ou queda) do executor.
- **Entrada:** a linha devolvida, em uma das duas formas da gramática do passo 4.
- **Ação:** ler a palavra devolvida — ela **é** o `status` da tarefa (`DP-G` item 2) — e, quando
  `blocked`, o `motivo=`. Materializa **sem discricionariedade** (`DP-G` item 1): não converte
  status nem reclassifica o motivo — quem decide é o roteamento (passo 8). Palavra fora das duas, `blocked` sem `motivo=`, `motivo=` fora do trio
  `dependencia|premissa|ferramenta`, ou prosa no lugar da linha: **retorno inválido**, regra `A2`.
- **Saída:** `status` materializado (`review` ou `blocked`), o `motivo` quando `blocked`, a
  `pendencia` quando presente, e os `tools` gastos lidos do `<usage>`.

### Passo 6 — Despacho do `reviewer`

- **Gatilho:** **gatilho 1** da `DP-E` — a tarefa entrou em `review`. Tarefa `blocked` **não** passa
  por aqui (`DP-G` item 4): não há entregável a julgar. **Confira, antes de invocar, que o status materializado da tarefa no plano é mesmo
  `review`** — é o estado em que o reviewer julga, e materializá-lo é ato do passo 5. O
  reviewer **não escreve** no modelo de domínio do plano: o andamento é derivado das tarefas e
  nenhum papel o grava (`GOVERNANCA.md` §3.2), então não há gravação de revisor a conferir
  aqui. Status diferente de `review` é defeito de condução do passo 5, não do revisor:
  materialize e só então invoque.
- **Entrada:** o **mesmo dossiê** que o executor recebeu; plano e identificador da tarefa. Nenhum
  caminho de RDO é repassado.
- **Ação:** gerar o dossiê de evidência mecânica, exigido pelo `reviewer`:

  ```
  python .claude/tools/review_evidence.py --plano <plano> --tarefa <ID> \
    --desde <ref capturada no passo 4> \
    --out docs/RDO/evidencia/<plano>-<ID>.md
  ```

  Redirecionar a saída padrão do comando. Em seguida invocar `pantonic-reviewer` com o dossiê da
  tarefa e o caminho do dossiê de evidência. **Não limite o retorno dele às duas linhas.**
  A forma do retorno é a que a definição do papel fixa: as duas linhas de veredito e, quando o
  passo `5a` apurar divergência, o dossiê `Ato de modelo` de `conflito` anexo abaixo delas
  (`GOVERNANCA.md` §3.2). É esse dossiê que o passo 8 consome para despachar o modelador.
- **Saída:** as duas linhas do `reviewer` e, quando houver, o dossiê `Ato de modelo` anexo.

### Passo 7 — Leitura do veredito

- **Gatilho:** retorno do `reviewer`.
- **Entrada:** as duas linhas fixas e, quando houver, o dossiê anexo abaixo delas:
  `<tarefa> <veredito> <percentual> bloqueante=<dimensão|nenhuma>`
  `laudo=<caminho>`
  Dossiê presente: são os seis campos do `Ato de modelo` (`GOVERNANCA.md` §3.2). O loop não o
  reescreve, não o resume e não o interpreta — passa-o inteiro ao passo 8.
- **Ação:** ler `veredito` ∈ {`aprovado`, `ressalva`, `reprovado`}, `bloqueante` e o caminho do
  laudo — calculados pelo gerador, não recalculados pelo loop. Colher a `recomendação` **do
  laudo**, campo fechado (`seguir`, `seguir com ressalva`, `refazer`, `escalar`), lido por `A6`,
  `A6a`, `A8a`, `A8`, `A9` e `B1`.
- **Saída:** tripla (`veredito`, `bloqueante`, `recomendação`) para o roteamento, mais o dossiê `Ato de modelo` quando ele veio no retorno.

### Passo 8 — Roteamento, bloco A

- **Gatilho:** passo 5 concluído (regras `A1`..`A3c`) e passo 7 concluído (`A6`..`A9`, inclusive `A6a` e `A8a`).
- **Entrada:** `status`, `veredito`, `bloqueante`, `recomendação`, contador de retentativas.
- **Ação:** aplicar a tabela do bloco A **em ordem de precedência** — a primeira regra que casa
  vence.
- **Saída:** "segue" (vai ao passo 9) ou "PARA" (vai ao relatório de encerramento). Se a
  linha de retorno do reviewer trouxer um dossiê `Ato de modelo`, despache o
  `pantonic-model-designer` com esse dossiê **antes** de seguir ao passo 9: o texto do modelo
  se acerta com a tarefa ainda aberta, e o andamento, que é derivado, não trava nada no
  intervalo.

### Passo 9 — Arquivamento

- **Gatilho:** **gatilho 2** da `DP-E` — a tarefa entrou em `done`. `cancelled`/`blocked` **não**
  disparam RDO (`DP-F` item 3, fechamento c); o gasto continua registrado pela telemetria.
- **Entrada:** o **pacote** extraído do laudo — os cinco campos obrigatórios (`DP-H` item 4):
  veredito, percentual, dimensão bloqueante, recomendação e pendência — mais o consumo medido, o
  plano e o identificador da tarefa.
- **Ação:** **primeiro o gate do modelo** (parágrafo ao final desta ação, `DMC-30`), e só então materializar o status com `python .claude/tools/backlog.py status <ID> <estado>`.
  Em seguida, escrever o RDO por **uma** chamada de `rdo.py close`, com o pacote como argumento:

  ```
  python .claude/tools/rdo.py close --plano <plano> --tarefa <ID> \
    --tool-uses <N> --tokens-k <tokens_k> --duracao-s <N> \
    --veredito <aprovado|ressalva> --percentual <0..100> --bloqueante <dimensão|nenhuma> \
    --recomendacao "…" --pendencia-laudo "…" [--pendencia "<pendência autoral do executor>"]
  ```

  O desdobramento é **calculado** pelo `close`, não escrito pelo loop (`DA-6`, `DP-H` item 4).
  Consumido o pacote, **apagar o laudo** (`DP-H` item 3).

  Depois do fechamento, apender **uma linha** a `docs/telemetria.tsv` com o dado do bloco `<usage>`
  via `python .claude/tools/telemetria.py append` (`--fonte usage`; sem `<usage>`,
  `--fonte nao_medido`) — nunca copiado para o diário. O número da linha é o do bloco `<usage>` da
  notificação, **conferido**: o hook `SubagentStop` grava sozinho e já gravou valor inflado
  (`AE-3`); linha do hook que divergir do `<usage>` é corrigida à mão pelo loop. E o hook **não
  dispara** quando o subagente é retomado por `SendMessage` — nesse caso a linha é apensada pelo
  loop, como todas as outras.

  O `<tokens_k>` é o mesmo literal nas duas chamadas — decimal de uma casa (ex.: `203.7`), a forma
  que o hook `SubagentStop` já produz. O loop não converte, não arredonda e não trunca o número
  entre uma chamada e outra (`DM-11` do `P-0740`).

  **Antes de materializar o status**, e portanto antes de `rdo.py close`, rodar de novo
  `python .claude/tools/modelo.py check --plano <plano>`: o modelo de domínio do plano pode ter
  sido emendado pelo `pantonic-model-designer` desde o despacho (`GOVERNANCA.md` §3.2), e exit
  `1` aqui é defeito dessa emenda. Exit `1`: **não materializa e não fecha** — a tarefa
  **permanece em `review`**, o stderr vai ao consultor como escalonamento, e o fechamento
  espera o reparo. A tarefa fica em `review` porque é o estado em que o reviewer a julgou; para
  o **andamento** a escolha é indiferente, já que `review` e `in-progress` deixam a operação
  igualmente `em curso`. Exit `0` ou `2`: materializa e fecha.
- **Saída:** RDO escrito com o desdobramento calculado, laudo apagado, linha nova em
  `docs/telemetria.tsv`, contadores da janela atualizados.

### Passo 10 — Continuar ou encerrar a janela

- **Gatilho:** passo 9 concluído com "segue" do bloco A.
- **Entrada:** `pendencia` da tarefa recém-fechada; sinal de coesão do contexto do loop; medida de
  ocupação da janela, injetada pelo hook `PreToolUse` de medida ao cruzar o teto de trabalho;
  próxima tarefa do plano.
- **Ação:** aplicar a tabela do bloco B, também por precedência, começando por `B0` — a atribuição de arquivo é **medida** pelo comando do `B0`, não julgada de memória. O encerramento por capacidade lê a
  medida de ocupação (`GOVERNANCA.md` §4.3).
- **Saída:** volta ao passo 2 com a próxima tarefa, ou relatório de encerramento.

## Tabelas de roteamento

Forma operacional das regras; fonte normativa em `docs/plans/P-0734-execucao-autonoma.md` —
`### DP-A`, `### DP-B` (com `### DP-Q`), `### DP-G` item 4, `### DP-K` §14.4. Divergência entre
esta tabela e essas seções resolve a favor da seção.

### Bloco A — o que fazer com a tarefa

| # | condição | ação |
|---|---|---|
| `A1` | queda do subagente (notificação sem bloco `<usage>`) | uma retomada por `SendMessage` ao mesmo `agentId` com "o que falta"; registra `PARCIAL — trecho pré-queda não medido`. Retomou: segue por `A2`..`A9`. Não retomou: **PARA** |
| `A2` | retorno ausente ou inválido (campo faltando, teto de campo estourado, linha fora da gramática) | um reenvio de **formato** ao mesmo executor; **não** consome a retentativa de conteúdo. Inválido de novo: **PARA** |
| `A3a` | `status=blocked` com `motivo=dependencia` | reordena a fila para que a bloqueada suceda a que a bloqueia e materializa `blocked` com a razão; **não** despacha o `reviewer`, **não** escreve RDO, **não** consome a retentativa e **não** incrementa o contador de tarefas fechadas: segue para a próxima elegível |
| `A3b` | `status=blocked` com `motivo=premissa` | materializa `blocked` com a razão na tarefa e no plano; **não** despacha o `reviewer` e **não** escreve RDO: **PARA**. A escalada é ao **planejador**: a rodada de replanejamento vira a próxima tarefa do plano (`G-REPLAN`, `GOVERNANCA.md` §7 item 17) e o relatório de janela a nomeia; ao dono só chega o que o planejador classificar como estratégico |
| `A3c` | `status=blocked` com `motivo=ferramenta` | materializa `blocked` com a razão, **sem** reclassificar o motivo; lê o **fallback declarado** da superfície no card e, havendo, **redespacha a mesma tarefa** por ele, **sem** consumir retentativa — a tarefa não falhou, a ferramenta foi negada; não havendo fallback declarado, **PARA** e a recusa sobe como matéria de plano, com a ferramenta, o caminho e a linha literal da recusa. **Não** despacha o `reviewer` e **não** escreve RDO |
| `A6` | `recomendacao=refazer` e retentativas gastas = 0 | despacha um executor **novo, em contexto novo**, com o dossiê original mais as **diretivas atualizadas** que o loop extraiu da recomendação — **nunca** o caminho do laudo, e **sem reescrever o dossiê**; contador := 1: segue |
| `A6a` | `veredito=reprovado` e `recomendacao=escalar` (qualquer `bloqueante`, qualquer contador de retentativas) | **não** fecha RDO e **não** gasta retentativa: materializa a tarefa como `blocked` razão `premissa`, com a pendência do laudo transcrita na razão, registra o achado como `AE-<n>` em `## Achados da execução` do plano e escala ao **consultor de plano**, que decide entre refazer com diretivas novas, emendar o card ou mudar a rota; a janela **segue** com o que ele devolver (Diretiva de execução do `P-0740`, item 2). Refazer antes de escalar gastaria a retentativa numa rota que o laudo já pediu para rever. Precedência: `A6` vence esta regra — lá o próprio laudo mandou refazer —, e esta vence `A7` e `A8a` |
| `A7` | `veredito=reprovado` e retentativas gastas = 1 | `reprovado` **não é desfecho de RDO** e esta regra **não** fecha RDO: o RDO só nasce na transição `review` → `done` (`DP-F` item 3, fechamento c), e `rdo.py close --veredito` aceita só `aprovado` e `ressalva` (medido: exit 2, `invalid choice`; `calcular_desdobramento('reprovado')` levanta `RdoValidationError`). Materializa a tarefa como `blocked` razão `premissa` — reprovada duas vezes, o que caiu foi a premissa de que o card é executável como está —, com o `bloqueante` e a pendência do laudo transcritos na razão, e registra o achado como `AE-<n>` em `## Achados da execução` do plano: **PARA**. A escalada é a do `A3b`: a reprovação depois da última retentativa é nomeada no relatório de encerramento e a rodada de replanejamento vira a próxima tarefa do plano (`G-REPLAN`, `GOVERNANCA.md` §7 item 17). Precedência: `A6` e `A6a` vencem esta regra; ela vence `A8a`, `A8` e `A9` |
| `A8a` | `recomendacao=escalar` e `veredito` ∈ {`aprovado`, `ressalva`} | **escalar não é desfecho de tarefa**: fecha o RDO pelo **veredito** transcrito — `aprovado` quando o veredito é `aprovado`, `aprovado com ressalva` quando é `ressalva` —, com cada achado do laudo saindo com rota, como em `A8`. A pendência **não** morre com o laudo: segue ao bloco B, onde o `B1` a registra como `AE-<n>` e a roteia ao consultor de plano. Precedência: `A6` e `A7` vencem esta regra — `bloqueante` diferente de `nenhuma` implica `veredito=reprovado`, que é `A7` —, e esta vence `A8` e `A9`, que leem a mesma recomendação |
| `A8` | `recomendacao=seguir com ressalva` | fecha o RDO como `aprovado com ressalva`; cada ressalva e cada achado do laudo sai **com rota** (tíquete ou `sem ação`): segue |
| `A9` | `recomendacao=seguir` | fecha o RDO como `aprovado`: segue |

A recomendação é de domínio fechado — o loop a **lê**, não a deriva do veredito. `bloqueante`
diferente de `nenhuma` implica `veredito=reprovado`. O consumo medido é **medida e registro, nunca
critério de rota** (`DP-Q`): vai para `docs/telemetria.tsv`. **O laudo morre no consumo, em
qualquer ramo** (`DP-K` §14.4): `A6`, `A6a`, `A7`..`A9` (inclusive `A8a`) e `B1` — o que a reexecução
precisa saber viaja nas **diretivas atualizadas**. A `A8a` existe porque o caso foi medido
**quatro vezes** na janela de 2026-09-18/19 (`LM-T7`, `LM-T3`, `LM-T2a` e `LM-T2`), todas com
`bloqueante=nenhuma`, e em todas o loop materializou o fechamento **por julgamento próprio** —
improviso que a `DP-G` proíbe.

O bloco A parte **primeiro por veredito, depois por recomendação**: `veredito=reprovado` é decidido por `A6`, `A6a` ou `A7` e **nunca por `A8a`, `A8` ou `A9`**, que só são alcançadas com veredito `aprovado` ou `ressalva`. É essa partição que impede entrega reprovada de ser fechada como aprovada por uma recomendação `seguir`, e é ela que garante que nenhuma regra mande fechar o que o instrumento recusa — medido: `rdo.py close --veredito reprovado` sai exit 2, `invalid choice`.

### Bloco B — continuar ou encerrar a janela

Avaliado **depois** de `A6`..`A9`, sobre a tarefa já fechada, e só quando o bloco A disse "segue". A precedência dentro do bloco é `B0` → `B1` → `B2` → `B3` → `B4`: o que é atribuível a arquivo alheio sai em `B0` e nunca chega a `B1`.

| # | condição | ação |
|---|---|---|
| `B0` | vermelho de verificação, ou item de `pendencia=`, **atribuível a arquivo fora dos `Arquivos-alvo` da tarefa** — atribuição **medida** por `python .claude/tools/review_evidence.py --plano <plano> --tarefa <ID> --desde <ref> --atribuir`, nunca julgada de memória | não é pendência da tarefa: registra `AE-<n>` com a atribuição medida, **não rebaixa** a entrega, não refaz laudo e **segue** por `B4` |
| `B1` | **pendência substantiva**: `recomendacao=escalar` no laudo, **ou** `pendencia=` cujo texto **não** seja integralmente atribuível a arquivo fora dos alvos por `B0` | registra a pendência como `AE-<n>` em `## Achados da execução` do plano, descarta o laudo e escala ao **consultor de plano** (`pantonic-consultant`, instanciado uma vez por execução), que devolve decisão e reparo: a janela **segue** com o que ele devolver. **PARA** só se o consultor classificar o impedimento como **estratégico**; ao dono chega só isso (`G-NOASK`, `GOVERNANCA.md` §7 item 18) |
| `B2` | sinal de poluição do contexto do loop (**coesão**) **ou** aviso de ocupação da janela no teto de trabalho, injetado no contexto pelo hook de medida (**capacidade**) — as duas condições do `GOVERNANCA.md` §4.3 | encerra com relatório de janela: **PARA** (encerramento normal, não falha). Por coesão o encerramento **não é gracioso**: nada produzido depois do sinal de poluição se aproveita. Sem o aviso na rodada, valem a coesão e o fim do plano |
| `B3` | a próxima tarefa é recusada pelo `G-PLANREADY`, pelo gate de delegação ou pelo `modelo.py check` do passo 3 (exit `1`) | não delega: **PARA**, com o que falta fechar |
| `B4` | nenhuma das anteriores | despacha a próxima tarefa do plano, sempre sequencial |

### O que obriga parada e o que segue com registro

- **Obriga parada:** decisão de arquitetura ou de requisito, que chega pelo `pendencia=`
  do retorno do executor ou pela recomendação `escalar` do laudo (`B1`), roteada ao **consultor de plano** —
  inclusive achado que invalida a rota do plano; executor `blocked` por `motivo=premissa` (`A3b`); o `blocked`
  por `motivo=ferramenta` como recusa de ferramenta sem fallback declarado (`A3c`); reprovação depois da
  última retentativa (`A7`); plano não-pronto (`B3`). Escalonamento ao consultor **não** encerra a janela: encerra-a só a classificação `estratégico` que ele devolver.
- **Segue com registro:** ressalva não bloqueante e achado fora de escopo com rota, pelo laudo
  (`A8`); o `blocked` por `motivo=dependencia` (`A3a`), que reordena a fila e segue para a
  próxima elegível; e o `blocked` por `motivo=ferramenta` como recusa de ferramenta com fallback
  declarado, que redespacha a mesma tarefa sem consumir retentativa (`A3c`).
- **Parada defeituosa:** solicitar o dono em caminho feliz, sem pendência aberta e sem demanda
  dele. Despachar a próxima tarefa, criar o contexto novo e passar o bastão são execução
  normal. Uma única ocorrência é defeito da entrega (`GOVERNANCA.md` §4.3).
  Também defeituosa: qualquer pergunta ao dono (`AskUserQuestion` ou prosa) **entre o despacho de
  uma tarefa e o relatório de encerramento** — o loop não fica com dúvida: registra `AE-<n>`,
  materializa `blocked premissa` e para (`G-NOASK`). Toda opção de rota do relatório inclui
  **registrar e não agir** quando ela existir.

A fronteira do **ponto do dono** é a de `.claude/skills/passagem-de-bastao/SKILL.md`, seção "A
fronteira do ponto do dono", e não se redecide aqui.

## Relatório de encerramento

Uma vez por janela, na parada. Abre com a saída integral de `python
.claude/tools/modelo.py show --plano <plano> --desde <data de abertura da janela>` — a
única exceção à regra de conteúdo, porque o modelo **é** o que o dono lê
(`GOVERNANCA.md` §3.2); plano sem modelo, a linha "sem modelo (plano anterior à
doutrina)". Depois, ponteiros e números, nunca conteúdo:

- Plano conduzido e regra que encerrou a janela (`A1`..`A9`, inclusive `A3c`, `A6a` e `A8a`, ou `B0`..`B4`, pelo identificador).
- Tarefas fechadas na janela, cada uma com identificador, desdobramento e caminho do RDO.
- Contadores finais: tarefas fechadas na janela e consumo acumulado, como medida para a série.
- **Pendências ao dono**, uma a uma, com o fato medido que a originou, o que cada opção implica, o
  que fica bloqueado sem resposta e a recomendação com o motivo.
- Próxima tarefa do plano, **sem iniciá-la**, e a recomendação de contexto novo antes da próxima
  janela. No mesmo ato, reescreve a linha `**Fila corrente:**` do cabeçalho de
  `docs/DIARIO_DE_OBRAS.md` (primeiras 15 linhas) — ou, quando o instrumento já mantém o bloco
  gerado, deixa que `status`/`start` a regenerem e **não** a escreve à mão.

### Quando a janela fecha o PLANO, e não só a janela

Fechada a última tarefa, o relatório **não** é o artefato de validação: o dono não dá veredito
sobre um plano lendo o plano. Antes de pedir o veredito, roda-se a
`.claude/skills/entrega-de-encerramento/SKILL.md`, que produz o **modelo as-is** das operações que
o plano deixou — uma seção por tarefa, com o contexto que a motivou, o artefato concreto, um
exemplo real de funcionamento e o que ela protege; mais os ganhos medidos e o estado de cada
pendência.

Esse documento é o insumo do veredito, não a consequência dele. O relatório de encerramento da
janela **aponta** para ele e não repete o conteúdo.

## Proibições

- Não despacha duas tarefas em paralelo, e não encerra a janela por percepção de contexto.
- Não pergunta ao dono entre o despacho e o relatório de encerramento (`G-NOASK`).

## Guardrails

- Uma janela conduz **um** plano. Troca de plano ou de iniciativa é troca de cenário: encerra a
  janela e recomeça em contexto novo (`.claude/global/CLAUDE.md` Regra 2).
- O modelo de cada tarefa vem do cabeçalho dela no plano, e o **esforço** declarado nele calibra a
  profundidade que o executor aplica. Cabeçalho fora da gramática de `GOVERNANCA.md` §3 — sem
  `[<modelo> · classe <classe>]`, que é o mínimo que os parsers do kit aceitam — é tarefa fora da
  gramática: cai em `B3`.
- O `scrum-master` **não revisa plano** (`GOVERNANCA.md` §3): indício de que o plano precisa de
  revisão leva o **plano** a `blocked`, com a razão registrada, e a matéria ao planejador.
- O consumo da janela é lido de `docs/telemetria.tsv`, jamais auto-relatado.
- Plano `superseded`, e plano `blocked` por decisão do dono ainda não tomada, não entram em janela.
