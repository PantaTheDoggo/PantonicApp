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
`GOVERNANCA.md` §4.3 e `### DP-Q` (encerramento); `### DP-G` item 3 (reordenação da fila); `docs/plans/P-0747-consultor-de-plano.md` `DCS-3`..`DCS-6` (triagem de toda parada pelo consultor e rota devolvida).

## Fluxo

Dez passos, nesta ordem.

### Passo 1 — Gate de modelo do contexto principal

- **Gatilho:** invocação da skill, antes de qualquer despacho.
- **Entrada:** modelo ativo do contexto principal.
- **Ação:** rodar `.claude/skills/modelo-por-fase/SKILL.md` (fase **orquestração**, matriz
  `GOVERNANCA.md` §3). Modelo ativo **acima** do exigido: **segue** nele — o contexto principal
  só orquestra, e o modelo de cada tarefa viaja no despacho (passo 4) — e anota a divergência em
  uma linha do relatório de encerramento. O loop nunca para para rebaixar o modelo. Modelo ativo
  **abaixo** do exigido: **PARA e pede ao dono o `/model` do modelo melhor** — a única parada do
  gate.
- **Saída:** modelo conferido, com a divergência anotada quando houver, ou parada com o `/model`
  do modelo melhor pedido.

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
  (`.claude/skills/passagem-de-bastao/SKILL.md`, seção "Gate de delegação", oito itens), sem
  recopiar o texto de nenhum dos dois. Recusa de qualquer um: **não delega** — vai ao passo 10 por `B3`.

  Terceiro gate, mecânico: `python .claude/tools/modelo.py check --plano <plano>`
  (`GOVERNANCA.md` §3.2). Exit `1`: **não delega** — o stderr vai à razão e a tarefa cai em
  `B3`. Exit `2`: plano anterior à doutrina do modelo; segue, com a nota "sem modelo" no
  relatório. Exit `0`: segue.

  Quarto gate, `card_check`: `python .claude/tools/card_check.py --plano <plano> --tarefa <ID>`
  — exit `1`: **não delega**, o stderr vai à razão e a tarefa cai em `B3`, com a nota
  `gate do card`.

  Aprovados os quatro, e **antes** de delegar, materializar `ready` → `in-progress` no kanban
  (`DP-G` item 1, consequência 3) — ato exclusivo do `scrum-master`.

  **Por comando** (`R-15`): `python .claude/tools/backlog.py despachar <ID>` roda, nesta ordem, o
  terceiro gate, o quarto e a coleta da suíte (`python -m pytest --co -q`), materializa
  `in-progress`, grava `.claude/estado/tarefa-corrente.json` com o `<ref>` e imprime o card
  inteiro, o bloco `HANDOVER` e a linha `ref=<sha>`. Recusa pelo primeiro gate que falhar, sem
  escrever nada: exit `1` **não delega**, e a linha de recusa vai à razão de `B3`. `G-PLANREADY` e o
  Gate de delegação continuam com quem conduz, antes do verbo; card de tíquete segue pelos passos
  à mão. Redespacho de tarefa cuja entrega já está na árvore (o consultor manteve o trabalho e a
  tarefa volta só para as verificações): `despachar <ID> --mundo depois`, que confere o card contra
  o `depois` e reaproveita o `<ref>` do primeiro despacho.
- **Saída:** tarefa materializada em `in-progress` e liberada para despacho, ou parada com o que
  falta fechar.

### Passo 4 — Despacho do executor

- **Gatilho:** gates do passo 3 aprovados e tarefa materializada em `in-progress`.
- **Entrada:** dossiê da tarefa copiado do plano; modelo declarado no cabeçalho.
- **Ação:** garantir o diretório `.claude/estado/` (ele viaja versionado com `.gitkeep`, `DM-10`
  do `P-0740`; recriá-lo se tiver sido apagado nesta máquina) e gravar
  `.claude/estado/tarefa-corrente.json` (objeto único: `tarefa`, `projeto`,
  `modelo`, `plano`, `despachado_em` ISO 8601), insumo do hook `SubagentStop` (`T55`) para
  `docs/telemetria.tsv`. Capturar como `<ref>` (schema `DP-S`) a saída de
  `python .claude/tools/review_evidence.py --capturar-ref` — instantâneo da árvore de trabalho
  inteira no despacho, rastreados e não rastreados, que não altera árvore, índice nem a lista de
  stash; usada no passo 6 (`AUT-T5b`), onde o trecho de cada alvo passa a mostrar só o que mudou
  desde o despacho. No redespacho da mesma tarefa (retomada depois de `blocked`, ou retentativa),
  o `<ref>` não se recaptura: vale o do primeiro despacho, para a evidência cobrir as duas execuções.

  Despachada pelo verbo `despachar` do passo 3, a tarefa já tem o arquivo gravado e o `<ref>` na
  linha `ref=<sha>` da saída: este passo só invoca o executor.

  Invocar `pantonic-executor` com `model` **igual ao do cabeçalho** (vence o `model:` do agente),
  com o dossiê da tarefa e a instrução de devolver **uma única linha**, domínio fechado (`DP-G`
  item 2):

  ```
  <tarefa> review
  <tarefa> review pendencia=<uma linha>
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
  `dependencia|premissa|ferramenta`, ou prosa no lugar da linha: **retorno inválido**, regra `A2`. Linha válida seguida de prosa **não** é retorno inválido: vale a primeira linha não vazia — a mesma que o gancho do painel lê —, a prosa depois dela é descartada sem reenvio de formato, e o descarte se anota numa linha do relatório de encerramento.
- **Saída:** `status` materializado (`review` ou `blocked`), o `motivo` quando `blocked`, a
  `pendencia` quando presente, e os `tools` gastos lidos do `<usage>`, e o arquivo de medida em
  o destino de `caminhos.destino_medida` (o `card_check.py --gravar` sem caminho grava ali e o `review_evidence.py` procura ali), cuja ausência vai ao laudo como verificação não
  feita.

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
    --out docs/RDO/evidencia/<plano>-<ID>.md   # só plano legado; plano em pasta: sem --out, grava docs/plans/P-<n>-<slug>/evidencia/<ID>.md
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
  `<tarefa> <veredito> <percentual> bloqueante=<dimensão|nenhuma> recomendacao=<seguir|seguir com ressalva|refazer|escalar>`
  `laudo=<caminho>`
  Dossiê presente: são os seis campos do `Ato de modelo` (`GOVERNANCA.md` §3.2). O loop não o
  reescreve, não o resume e não o interpreta — passa-o inteiro ao passo 8.
- **Ação:** ler `veredito` ∈ {`aprovado`, `ressalva`, `reprovado`}, `bloqueante`, `recomendacao` e o
  caminho do laudo — calculados pelo gerador e transcritos pelo revisor, não recalculados pelo
  loop. A `recomendação` vem **da primeira linha**, campo fechado (`seguir`, `seguir com
  ressalva`, `refazer`, `escalar`), lido por `A6`,
  `A6a`, `A8a`, `A8`, `A9` e `B1`.
- **Saída:** tripla (`veredito`, `bloqueante`, `recomendação`) para o roteamento, mais o dossiê `Ato de modelo` quando ele veio no retorno.

### Passo 8 — Roteamento, bloco A

- **Gatilho:** passo 5 concluído (regras `A1`..`A3c`) e passo 7 concluído (`A6`..`A9`, inclusive `A6a` e `A8a`).
- **Entrada:** `status`, `veredito`, `bloqueante`, `recomendação`, contador de retentativas.
- **Ação:** aplicar a tabela do bloco A **em ordem de precedência** — a primeira regra que casa
  vence.
- **Triagem:** toda regra que escala ao consultor (`A3a`, `A3b`, `A3c`, `A6a`, `A7`, `B1` e o gate do modelo do passo 9) recebe de volta a linha `rota=<resolve|modelador|planejador>` — e, quando o consultor classificar o impedimento como estratégico, a linha `estrategico=<uma frase>` logo abaixo dela — e despacha por ela: `estrategico=` presente — **PARA** em qualquer rota, e nas rotas `resolve` e `modelador` **sem executar a ação da rota**: o reparo que o consultor já gravou fica no plano, o modelador **não** é despachado, e a frase, a rota e o dossiê de emenda, se houver, vão ao relatório de encerramento, para o dono decidir antes de qualquer ato sobre o modelo (`G-NOASK`; `P-0747` `DCS-28`); com `rota=planejador` a ação da rota já é a parada e se executa como está — o plano materializado `blocked`, a rodada de replanejamento enfileirada — e a frase vai junto ao relatório; `rota=resolve` sem `estrategico=` — o reparo já está gravado no plano, e a janela segue; quando o reparo é a recusa do impedimento como improcedente (`P-0747` `DCS-35`), a mesma tarefa volta a `ready` com ao menos uma linha nova gravada pelo consultor e é redespachada **sem** consumir retentativa; `rota=modelador` — despacha o `pantonic-model-designer` com o dossiê `Ato de modelo` de `emenda` que o consultor devolveu, sem parar a janela: a versão pendente coexiste com a vigente até o marco, onde o pedido de validar ou recusar o drift sobe ao dono (`GOVERNANCA.md` §3.2), e com a recusa o caso volta ao consultor para resolver preservando o modelo; `rota=planejador` — materializa o plano como `blocked`, e a rodada de replanejamento vira a próxima tarefa do plano (`G-REPLAN`, `GOVERNANCA.md` §7 item 17): **PARA**.
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
- **Ação:** **dois comandos**, do mesmo instrumento (`TK-88`). Primeiro o **handover** — o que
  quem vem depois espera desta tarefa, inteiramente de máquina, registrado **no card** como campo
  `- **Handover:**`, com o conteúdo lido da linha de retorno do executor e da entrega na árvore:

  ```
  python .claude/tools/encerrar.py handover --plano <plano> --tarefa <ID> \
    --entregue "<o que existe agora, com caminho:linha>" \
    --contrato "<com o que a sucessora pode contar>" \
    [--nao-refazer "<o que já está pago>"] [--pendente "<o que fica de propósito>"] \
    [--para <ID da sucessora | papel>]...
  ```

  O `next` devolve esse campo à sucessora sob `=== HANDOVER DE <ID>` (Passo 2): o de todo irmão
  que a nomeia em `para` e, sem nenhum, o da antecessora imediata. Depois o **fechamento**:

  ```
  python .claude/tools/encerrar.py tarefa --plano <plano> --tarefa <ID> \
    [--resumo "<uma frase em linguagem corrente, para o dono>"] \
    [--pendencia "<pendência autoral do executor>"] \
    [--achado "<texto>" "<rota>"]... \
    [--tool-uses <N> --tokens-k <tokens_k> --duracao-s <N> | --nao-medido "<razão>"]
  ```

  Ele faz, nesta ordem e só depois de todas as checagens passarem: (1) o **gate do modelo** —
  `modelo.py check` exit `1` **não materializa e não fecha**: a tarefa **permanece em `review`**
  (o estado em que o reviewer a julgou; para o andamento é indiferente, `review` e `in-progress`
  deixam a operação igualmente `em curso`), o stderr vai ao consultor como escalonamento e o
  fechamento espera o reparo (`DMC-30`); exit `0` ou `2` segue; (2) materializa o `done`
  (`backlog.transacionar_status`, com a nota de fechamento no card); (3) escreve o RDO por
  `rdo.cmd_close`, com o pacote **transcrito do laudo** que o revisor gravou — o loop não redigita
  veredito, percentual, bloqueante, recomendação nem pendência (`DA-6`, `DP-H` item 4) —, o
  desdobramento **calculado**, e as três seções: `# Humano` (título da tarefa entre aspas, revisão
  em palavras, pendência ao dono, andamento do plano e próxima tarefa), `# Máquina` (dossiê
  verbatim, pacote, consumo, desdobramento) e `# Histórico` (as linhas que o gancho do painel
  gerou para a tarefa); (4) a **telemetria**: o consumo vem da linha da tarefa em
  `docs/telemetria.tsv` que o hook `SubagentStop` gravou — a fonte única —, ou, quando o loop traz
  o bloco `<usage>` da notificação em `--tool-uses/--tokens-k/--duracao-s`, apensa essa linha à
  série no mesmo ato (`--fonte usage`); sem nenhum dos dois o instrumento **recusa** — número
  inventado não fecha tarefa. Tarefa sem `<usage>` — executada fora do loop — fecha com
  `--nao-medido "<razão>"` (`GOVERNANCA.md` §4.2): a série registra a ausência, nunca um número.
  Quando o hook gravou valor que diverge do `<usage>` (`AE-3`), o loop
  passa o trio conferido, e a linha do hook fica na série como está. O hook **não dispara** quando
  um subagente é retomado por `SendMessage` — a retomada do executor pela `A1` — e nesse caso o
  trio vem sempre por argumento; o consultor nunca é retomado (seção *Acionamento do consultor*);
  (5) cada linha da tabela `## Achado de processo` do laudo e cada `--achado` viram `AE-<n>` com
  `**Rota:**` em `## Achados da execução` do plano, sem repetir achado do laudo já registrado. O
  `<tokens_k>` é o literal do `<usage>`, decimal de uma casa (ex.: `203.7`), sem conversão nem
  arredondamento (`DM-11` do `P-0740`). A saída do comando é a seção `# Humano` — o handover da
  tarefa, em ≤ 8 linhas. O laudo permanece no disco como fonte do pacote (`DP-H` item 3 deixa de
  mandar apagá-lo: o instrumento o lê).
- **Saída:** RDO escrito nas três seções, com o desdobramento calculado; `done` projetado no card,
  no índice e no bloco `Fila corrente`; linha da série de telemetria presente; achados registrados;
  contadores da janela atualizados.

### Passo 10 — Continuar ou encerrar a janela

- **Gatilho:** passo 9 concluído com "segue" do bloco A.
- **Entrada:** `pendencia` da tarefa recém-fechada; sinal de coesão do contexto do loop; medida de
  ocupação da janela, injetada pelo hook `PreToolUse` de medida ao cruzar o teto de trabalho;
  próxima tarefa do plano.
- **Ação:** aplicar a tabela do bloco B, também por precedência, começando por `B0` — a atribuição de arquivo é **medida** pelo comando do `B0`, não julgada de memória. O encerramento por capacidade lê a
  medida de ocupação (`GOVERNANCA.md` §4.3).
- **Saída:** volta ao passo 2 com a próxima tarefa, ou relatório de encerramento.

## Tabelas de roteamento

Forma operacional das regras; fonte normativa em `docs/plans/P-0734-execucao-autonoma.md` — `### DP-A`, `### DP-B` (com `### DP-Q`), `### DP-G` item 4, `### DP-K` §14.4 — e, para a triagem de toda parada pelo consultor, em `docs/plans/P-0747-consultor-de-plano.md` `DCS-3`..`DCS-6`, que prevalecem sobre o `P-0734` no que dispõem. Divergência entre esta tabela e essas seções resolve a favor da seção.

### Bloco A — o que fazer com a tarefa

| # | condição | ação |
|---|---|---|
| `A1` | queda do subagente (notificação sem bloco `<usage>`) | executor ou `reviewer`: uma retomada por `SendMessage` ao mesmo `agentId` com "o que falta"; registra `PARCIAL — trecho pré-queda não medido`. Retomou: segue por `A2`..`A9`. Não retomou: **PARA**. Consultor: **nenhuma** retomada — a instância caída se descarta, a telemetria dela registra `PARCIAL — trecho pré-queda não medido`, e o loop despacha **uma instância nova** com as mesmas três entradas, sobre o cenário como a caída o deixou (seção *Acionamento do consultor*; `P-0747` `DCS-29`). Caiu de novo no mesmo acionamento: **PARA** |
| `A2` | retorno ausente ou inválido (campo faltando, teto de campo estourado, linha fora da gramática, prosa no lugar da linha); prosa **depois** de linha válida não casa aqui — o passo 5 a descarta | um reenvio de **formato** ao mesmo executor; **não** consome a retentativa de conteúdo. Inválido de novo: **PARA** |
| `A3a` | `status=blocked` com `motivo=dependencia` | materializa `blocked` com a razão; **não** despacha o `reviewer`, **não** escreve RDO, **não** consome a retentativa e **não** incrementa o contador de tarefas fechadas; escala ao **consultor**, que devolve a rota (passo 8) — na rota `resolve`, a reordenação da fila que ele gravar, com a bloqueada depois da que a bloqueia: segue para a próxima elegível — ou, recusado o impedimento como improcedente (`DCS-35`), o redespacho da mesma tarefa, de volta a `ready` com a linha nova que ele gravou, **sem** consumir retentativa; `modelador` segue com o despacho do modelador; `planejador` e `estrategico=` **PARAM**, como o passo 8 manda |
| `A3b` | `status=blocked` com `motivo=premissa` | materializa `blocked` com a razão na tarefa; **não** despacha o `reviewer` e **não** escreve RDO; escala ao **consultor**, que devolve a rota (passo 8): `resolve` segue com o reparo — inclusive a recusa do impedimento como improcedente (`DCS-35`): a mesma tarefa volta a `ready` com ao menos uma linha nova e é redespachada **sem** consumir retentativa; `modelador` segue com o despacho do modelador; `planejador` e `estrategico=` **PARAM**, como o passo 8 manda. O motivo é evidência, não rota (`DP-G` item 1 do `P-0734`) |
| `A3c` | `status=blocked` com `motivo=ferramenta` | materializa `blocked` com a razão, **sem** reclassificar o motivo; escala ao **consultor** com a ferramenta, o caminho e a linha literal da recusa, e ele devolve a rota (passo 8): na rota `resolve`, havendo **fallback declarado** da superfície no card, **redespacha a mesma tarefa** por ele, **sem** consumir retentativa — a tarefa não falhou, a ferramenta foi negada —, e sem fallback aplica o reparo que o consultor gravar — inclusive a recusa do impedimento como improcedente (`DCS-35`), que redespacha a mesma tarefa, de volta a `ready` com a linha nova, **sem** consumir retentativa; `modelador` segue com o despacho do modelador; `planejador` e `estrategico=` **PARAM**, como o passo 8 manda. **Não** despacha o `reviewer` e **não** escreve RDO |
| `A6` | `recomendacao=refazer` e retentativas gastas = 0 | despacha um executor **novo, em contexto novo**, com o dossiê original mais as **diretivas atualizadas** que o loop extraiu da recomendação — **nunca** o caminho do laudo, e **sem reescrever o dossiê**; contador := 1: segue |
| `A6a` | `veredito=reprovado` e `recomendacao=escalar` (qualquer `bloqueante`, qualquer contador de retentativas) | **não** fecha RDO e **não** gasta retentativa: materializa a tarefa como `blocked` razão `premissa`, com a pendência do laudo transcrita na razão, registra o achado como `AE-<n>` em `## Achados da execução` do plano e escala ao **consultor de plano**, que devolve a rota (passo 8) — na rota `resolve`, refazer com diretivas novas ou emendar o card, e a janela **segue** com o que ele devolver (Diretiva de execução do `P-0740`, item 2; `P-0747` `DCS-3`); `modelador` segue com o despacho do modelador; `planejador` e `estrategico=` **PARAM**, como o passo 8 manda. Refazer antes de escalar gastaria a retentativa numa rota que o laudo já pediu para rever. Precedência: `A6` vence esta regra — lá o próprio laudo mandou refazer —, e esta vence `A7` e `A8a` |
| `A7` | `veredito=reprovado` e retentativas gastas = 1 | `reprovado` **não é desfecho de RDO** e esta regra **não** fecha RDO: o RDO só nasce na transição `review` → `done` (`DP-F` item 3, fechamento c), e `rdo.py close --veredito` aceita só `aprovado` e `ressalva` (medido: exit 2, `invalid choice`; `calcular_desdobramento('reprovado')` levanta `RdoValidationError`). Materializa a tarefa como `blocked` razão `premissa` — reprovada duas vezes, o que caiu foi a premissa de que o card é executável como está —, com o `bloqueante` e a pendência do laudo transcritos na razão, e registra o achado como `AE-<n>` em `## Achados da execução` do plano. A escalada é a do `A3b`: ao **consultor**, que devolve a rota (passo 8) — `resolve` segue, `modelador` segue com o despacho do modelador, `planejador` e `estrategico=` **PARAM** —, e a reprovação depois da última retentativa é nomeada no relatório de encerramento. Precedência: `A6` e `A6a` vencem esta regra; ela vence `A8a`, `A8` e `A9` |
| `A8a` | `recomendacao=escalar` e `veredito` ∈ {`aprovado`, `ressalva`} | **escalar não é desfecho de tarefa**: fecha o RDO pelo **veredito** transcrito — `aprovado` quando o veredito é `aprovado`, `aprovado com ressalva` quando é `ressalva` —, com cada achado do laudo saindo com rota, como em `A8`. A pendência **não** morre com o laudo: segue ao bloco B, onde o `B1` a registra como `AE-<n>` e a roteia ao consultor de plano. Precedência: `A6` e `A7` vencem esta regra — `bloqueante` diferente de `nenhuma` implica `veredito=reprovado`, que é `A7` —, e esta vence `A8` e `A9`, que leem a mesma recomendação |
| `A8` | `recomendacao=seguir com ressalva` | fecha o RDO como `aprovado com ressalva`; cada ressalva e cada achado do laudo sai **com rota** (card corretivo, tíquete ou `sem ação`); `sem ação` só serve a achado que não aponta erro — observação, ou reincidência de causa já roteada a card —, e **erro inequívoco nunca sai `sem ação` nem "para quem tocar depois"**, por menor que seja: vai ao consultor, que o corrige no ato ou o põe na fila como card corretivo; a rota tíquete vai ao consultor, que o abre já com o card (skill `diario-de-obras`, "Tíquete nasce executável"): segue |
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
| `B1` | **pendência substantiva**: `recomendacao=escalar` no laudo, **ou** `pendencia=` cujo texto **não** seja integralmente atribuível a arquivo fora dos alvos por `B0` | registra a pendência como `AE-<n>` em `## Achados da execução` do plano, descarta o laudo e escala ao **consultor de plano** (`pantonic-consultant`, uma instância efêmera por acionamento — seção *Acionamento do consultor*), que devolve a rota (passo 8): na rota `resolve` a janela **segue** com o reparo e na rota `modelador` com o despacho do modelador; **PARA** na rota `planejador` e com `estrategico=`, como o passo 8 manda; ao dono chega só isso (`G-NOASK`, `GOVERNANCA.md` §7 item 18) |
| `B2` | sinal de poluição do contexto do loop (**coesão**) **ou** aviso de ocupação da janela no teto de trabalho, injetado no contexto pelo hook de medida (**capacidade**) — as duas condições do `GOVERNANCA.md` §4.3 | encerra com relatório de janela: **PARA** (encerramento normal, não falha). Por coesão o encerramento **não é gracioso**: nada produzido depois do sinal de poluição se aproveita. Sem o aviso na rodada, valem a coesão e o fim do plano |
| `B3` | a próxima tarefa é recusada pelo `G-PLANREADY`, pelo gate de delegação, pelo `modelo.py check` ou pelo `card_check` do passo 3 (exit `1`) | não delega: **PARA**, com o que falta fechar |
| `B4` | nenhuma das anteriores | despacha a próxima tarefa do plano, sempre sequencial |

### O que obriga parada e o que segue com registro

- **Obriga parada:** a rota `planejador` que o consultor devolver a qualquer escalonamento (`A3a`, `A3b`, `A3c`, `A6a`, `A7`, `B1` e o gate do modelo do passo 9), e a linha `estrategico=` que ele devolver com qualquer rota — inclusive achado que invalida a rota do plano; plano não-pronto (`B3`). Escalonamento ao consultor **não** encerra a janela por si: encerram-na a rota `planejador` — cuja ação, materializar o plano `blocked` e enfileirar o replanejamento, se executa com ou sem `estrategico=` — e a linha `estrategico=` — esta, nas rotas `resolve` e `modelador`, sem executar a ação da rota, com o dossiê de emenda, se houver, no relatório de encerramento (`DCS-28`); a rota `modelador` sem `estrategico=` despacha o modelador e segue, com a versão pendente até o marco.
- **Segue com registro:** ressalva não bloqueante e achado fora de escopo com rota, pelo laudo (`A8`); e toda parada ou pendência em que o consultor devolve `rota=resolve` sem `estrategico=` (`A3a`, `A3b`, `A3c`, `A6a`, `A7`, `B1` e o gate do modelo do passo 9), com o reparo que ele gravou — a reordenação da fila no `A3a`, o redespacho pelo fallback declarado no `A3c`, o redespacho da mesma tarefa com a linha nova quando ele recusa o impedimento como improcedente (`A3a`, `A3b`, `A3c`; `DCS-35`), sem consumir retentativa; e a rota `modelador` sem `estrategico=`, com o despacho do `pantonic-model-designer` sobre o dossiê devolvido e a versão pendente até o marco (`GOVERNANCA.md` §3.2).
- **Parada defeituosa:** solicitar o dono em caminho feliz, sem pendência aberta e sem demanda
  dele. Despachar a próxima tarefa, criar o contexto novo e passar o bastão são execução
  normal. Uma única ocorrência é defeito da entrega (`GOVERNANCA.md` §4.3).
  Também defeituosa: qualquer pergunta ao dono (`AskUserQuestion` ou prosa) **entre o despacho de
  uma tarefa e o relatório de encerramento** — o loop não fica com dúvida: registra `AE-<n>`,
  materializa `blocked premissa` e para (`G-NOASK`). Toda opção de rota do relatório inclui
  **registrar e não agir** quando ela existir.

A fronteira do **ponto do dono** é a de `.claude/skills/passagem-de-bastao/SKILL.md`, seção "A
fronteira do ponto do dono", e não se redecide aqui.

## Acionamento do consultor

Forma **efêmera com cenário persistido**, em piloto (`docs/plans/P-0747-consultor-de-plano.md` `DCS-6`, `DCS-7`). O consultor não fica de prontidão: a cada escalonamento das regras `A3a`, `A3b`, `A3c`, `A6a`, `A7` e `B1` e do gate do modelo do passo 9, o loop despacha **uma instância nova** do `pantonic-consultant`, com três entradas — o caminho do cenário do plano, `docs/plans/P-<n>-<slug>/cenario.md` (plano legado: `_CENARIO-<plano>.md` em `docs/plans/`); o identificador do card em causa; e a evidência (a linha de retorno do executor, a pendência do laudo ou o stderr do instrumento). A instância lê o cenário e o card, decide, reescreve o cenário com `Edit` mínimo, apensa a linha dela a `docs/ACIONAMENTOS_CONSULTOR.tsv` e devolve `rota=<resolve|modelador|planejador>` — e, só quando classifica o impedimento como estratégico, a linha `estrategico=<uma frase>` logo abaixo (`DCS-27`) —, que o loop roteia pelo passo 8. Nenhuma instância é retomada por `SendMessage` e nenhuma é reprovisionada por limite: o cenário **é** o handover, e a instância que cai se descarta — a `A1` despacha outra, com as mesmas três entradas, sobre o cenário como ficou. Sem o arquivo de cenário na árvore, o primeiro acionamento do plano o cria, com as decisões vivas, a fila, os achados abertos e a matéria inconclusiva, em no máximo 15k tokens. A linha de telemetria de cada instância é gravada pelo hook `SubagentStop`, com a tarefa `<ID>-consultor-<n>`.

Molde do despacho — as três entradas, e nada além delas:

    cenario=docs/plans/P-<n>-<slug>/cenario.md
    card=<ID>
    evidencia=<a linha de retorno do executor, a pendência do laudo ou o stderr do instrumento, verbatim>
    Leia só o cenário, o card e a evidência acima e, da doutrina, só o que o cenário aponta.

## Relatório de encerramento

Uma vez por janela, na parada. Abre com a saída integral de `python
.claude/tools/modelo.py show --plano <plano>` — a
única exceção à regra de conteúdo, porque o modelo **é** o que o dono lê
(`GOVERNANCA.md` §3.2); plano sem modelo, a linha "sem modelo (plano anterior à
doutrina)". Depois, ponteiros e números, nunca conteúdo:

- Plano conduzido, pelo título entre aspas, e a regra que encerrou a janela, pela condição dela em palavras (a coluna *condição* das tabelas dos blocos A e B), com o identificador entre parênteses (*Mensagem legível ao dono*, `GOVERNANCA.md` §4.2).
- Tarefas fechadas na janela, cada uma pelo título entre aspas, com desdobramento e caminho do RDO.
- Contadores finais: tarefas fechadas na janela e consumo acumulado, como medida para a série —
  pela skill `fatos-frescos`: totais vêm do índice do diário e da série `docs/telemetria.tsv`, nunca de soma à mão.
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

Com o veredito do dono em mãos, o fechamento do plano é **um comando** (`TK-88`):

```
python .claude/tools/encerrar.py plano --plano <plano> --veredito "<frase do dono, verbatim>" \
  [--resumo "<uma frase>"] [--operacoes <documento de validação>]
```

Ele recusa enquanto houver tarefa não terminal, tarefa `done` sem RDO, achado `AE-<n>` sem
`**Rota:**` ou documento de validação ausente; passando, materializa o `done` do plano (regra de
plano do `backlog.py`: sem `review`, a partir de `ready`/`in-progress`/`blocked`), escreve o
relatório de entrega — `entrega.md` na pasta do plano, `docs/plans/_ENTREGA-<id>.md` no legado —
nas mesmas três seções (`# Humano`: veredito verbatim, contagens, validação, instrumentos,
consumo; `# Máquina`: tabela das tarefas com o veredito lido de cada RDO, achados verbatim,
consumo por papel, violações do `check`; `# Histórico`: as linhas do painel do plano inteiro) e
insere **uma** linha no cabeçalho do diário, com o veredito e os dois ponteiros — o parágrafo que
antes se escrevia à mão. A saída do comando é a seção `# Humano`, que é o que vai ao dono.

## Repertório de mensagens ao gerente

As linhas que o gerente lê no painel são **geradas** pelo gancho `.claude/tools/progresso_hook.py`
a partir do evento de cada transição do loop — o condutor não escreve nenhuma delas, não usa
marcador e não escreve no arquivo de progresso (`P-0748`, `DTG-30`, `I-2`, `I-11`). Esta tabela é a
cópia legível do que a função gera (a residência vigente é o dicionário `FRASES` do gancho; a
normativa, a `### 4.1` do plano): uma linha por forma de frase, com o gancho, a ferramenta e a
detecção que a disparam e o campo do evento que preenche cada lacuna `<…>`. `<título>` é o
título do card entre aspas duplas e `<título do plano>` o do plano — a sigla nunca chega sozinha
ao gerente (`I-12`). Outras ferramentas, outros comandos e outros `subagent_type` não geram linha.

| id | evento (gancho · ferramenta · detecção) | frase gerada | lacunas ← campo do evento ou leitura local |
|---|---|---|---|
| `M-0` | tarefa escolhida, primeira da sessão — `PostToolUse` · `Bash` · `command` contém `backlog.py next` · resposta contém `=== PRÓXIMA TAREFA: ` · estado sem `aberta` | `Abrindo a janela do plano "<título do plano>".` | `<título do plano>` ← `localizar_card(<ID>)`; vazio → linha omitida. Sai antes de `M-11` e de `M-1` |
| `M-1` | tarefa escolhida — o mesmo evento de `M-0`, sempre | `Tarefa "<título>". Passo: conferir os gates e preparar o despacho.` | `<ID>`, `<título>` ← linha `=== PRÓXIMA TAREFA: <ID> — <título> [` da resposta. Estado ← `tarefa`, `titulo`, `objetivo`, `titulo_plano` (de `localizar_card`), `aberta` = true |
| `M-2` | estado mudado para in-progress — `PreToolUse` · `Bash` · numa invocação do comando encadeado (`_dividir_invocacoes`, fora de aspas) o programa é `backlog.py`, o verbo é `status` e o `<estado>` dos argumentos dessa invocação é `in-progress` (`TK-88c`: script e argumentos se leem na própria invocação, nunca no comando inteiro) | `Tarefa "<título>": gates aprovados; vou materializar in-progress e gravar o ponto de partida.` | `<título>` ← estado se `<ID>` é a `tarefa` do estado, senão `localizar_card(<ID>)`. `status <ID> review` não gera linha |
| `M-3` | agente despachado, executor — `PreToolUse` · `Agent` · `subagent_type` = `pantonic-executor` · objetivo não vazio | `Agente executor recebe a tarefa "<título>" e vai executar: <objetivo>` | `<título>`, `<objetivo>` ← tarefa corrente (`DTG-33` (iv)) e `localizar_card`; `<objetivo>` já termina em ponto, ou em `…` se truncado |
| `M-3b` | o mesmo evento de `M-3`, objetivo vazio | `Agente executor recebe a tarefa "<título>" e vai executar o card.` | `<título>` como em `M-3` |
| `M-4` | agente de volta, executor — `PostToolUse` · `Agent` · `pantonic-executor`; se o agente entregou em hand-back (`handback` = `send` na resposta, e o `PostToolUse` só grava `pendentes[agentId]`), `UserPromptSubmit` com `prompt` começando por `<agent-message from="<agentId>">` de agente em `pendentes`, e a resposta é o trecho depois de `The report follows:` (`DTG-39`) · primeira linha não vazia da resposta casa `^(\S+) review(?:\s+\[?pendencia=(.*?)\]?)?$` | `Agente executor devolveu a tarefa "<título>": review — <pendência>.` | `<pendência>` ← grupo 2; ausente → `sem pendência` |
| `M-4b` | o mesmo evento, primeira linha casa `^(\S+) blocked motivo=(\S+)\s*(.*)$` | `Agente executor devolveu a tarefa "<título>": blocked — motivo <motivo>: <razão>.` | `<motivo>` ← grupo 2; `<razão>` ← grupo 3 |
| `M-5` | evidência coletada — `PreToolUse` · `Bash` · numa invocação do comando o programa é `review_evidence.py`, com `--tarefa <ID>` e sem `--atribuir` nos argumentos dessa mesma invocação (`TK-88c`) | `Tarefa "<título>": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.` | `<ID>` ← `--tarefa` da própria invocação; `<título>` ← estado ou `localizar_card` |
| `M-6` | agente despachado, revisor — `PreToolUse` · `Agent` · `pantonic-reviewer` | `Agente revisor recebe a tarefa "<título>" e vai confrontar a entrega com o card.` | `<título>` ← tarefa corrente |
| `M-7` | agente de volta, revisor — `PostToolUse` · `Agent` · `pantonic-reviewer`, ou o `UserPromptSubmit` da volta em hand-back, como em `M-4` · primeira linha casa `^(\S+) (\S+) (\d+)%? bloqueante=(\S+)(?: recomendacao=(.+))?$` | `Agente revisor devolveu a tarefa "<título>": <veredito> <percentual>%, bloqueante <bloqueante>, recomendação <recomendação>.` | `<veredito>` ← grupo 2; `<percentual>` ← grupo 3; `<bloqueante>` ← grupo 4; `<recomendação>` ← grupo 5, ou `não informada` sem o campo |
| `M-8` | agente despachado, consultor — `PreToolUse` · `Agent` · `pantonic-consultant` | `Agente consultor recebe a tarefa "<título>" e vai triar.` | `<título>` ← tarefa corrente. A regra A-n/B-n saiu (`DTG-34`); "a parada" saiu (`DTG-48`): o consultor também é despachado por laudo, por instrumento e no marco, e o evento não diz por qual |
| `M-9` | agente de volta, consultor — `PostToolUse` · `Agent` · `pantonic-consultant`, ou o `UserPromptSubmit` da volta em hand-back, como em `M-4` · uma linha da resposta começa, depois de brancos, por `rota=(\S+)`, e nenhuma por `estrategico=` | `Agente consultor devolveu a tarefa "<título>": rota <rota>.` | `<rota>` ← grupo 1 da primeira linha que casa; `rota=` ou `estrategico=` no meio de uma linha não conta |
| `M-9b` | o mesmo evento, uma linha da resposta começa, depois de brancos, também por `estrategico=(.*)` | `Agente consultor devolveu a tarefa "<título>": rota <rota>; estratégico: <frase>.` | `<frase>` ← grupo 1 de `estrategico=`, até o fim da linha |
| `M-10` | tarefa fechada — `PreToolUse` · `Bash` · numa invocação o programa é `backlog.py`, o verbo é `status` e o `<estado>` dos argumentos dessa invocação é `done`, **ou** o programa é `encerrar.py`, o verbo é `tarefa` e o `--tarefa <ID>` sai dos argumentos dessa mesma invocação (`TK-88`: o instrumento materializa o `done` em processo; `TK-88c`: script e verbo se leem na própria invocação — o `--tarefa` de outra invocação da linha não entra) | `Scrum master vai fechar a tarefa "<título>" como done: registrar estado, RDO e telemetria.` | Estado ← `tarefa_fechada` = `<ID>`, `titulo_fechada` = `<título>`. "e selecionar a próxima" saiu (`DTG-49`): depois do `done` o bloco B pode parar a janela sem `next` (`progresso.txt:83`, `86`); a seleção, quando há, sai na `M-11` ou na `M-12` |
| `M-10b` | o mesmo evento, `<estado>` igual a `blocked` ou `cancelled` | `Scrum master vai marcar a tarefa "<título>" como <estado>, sem RDO.` | `<estado>` ← grupo 2. Estado intocado, sem `tarefa_fechada`: a tarefa não foi concluída, e a `M-11` e a `M-12` diriam "concluiu". Sem RDO (`DP-F` item 3, fechamento c) e sem próxima: o `blocked` vai ao consultor, que pode parar a janela ou redespachar a mesma tarefa (`progresso.txt:74`, `77`; `DTG-49`) |
| `M-11` | tarefa escolhida com tarefa fechada na sessão — o evento de `M-1`, estado com `tarefa_fechada` | `Scrum master concluiu a tarefa "<título fechada>" e vai pegar a tarefa "<título>".` | `<título fechada>` ← `titulo_fechada` do estado; sai depois de `M-0` e antes de `M-1`, e limpa `tarefa_fechada` |
| `M-12` | fila vazia — `PostToolUse` · `Bash` · `backlog.py next` · resposta contém `nada delegável` · estado com `tarefa_fechada` | `Scrum master concluiu a tarefa "<título fechada>"; nada delegável na fila. Encerrando a janela com o relatório.` | `<título fechada>` ← estado; limpa `tarefa_fechada`. A regra B1..B3 saiu (`DTG-34`) |
| `M-12b` | o mesmo evento, estado sem `tarefa_fechada` | `Scrum master não encontrou tarefa delegável na fila. Encerrando a janela com o relatório.` | nenhuma lacuna |
| `M-13` | atribuição medida — `PreToolUse` · `Bash` · numa invocação o programa é `review_evidence.py`, com `--tarefa <ID>` e `--atribuir` nos argumentos dessa mesma invocação (`TK-88c`) | `Tarefa "<título>": vou medir a que arquivo a pendência é atribuível.` | como `M-5` |
| `M-14` | agente despachado, modelador — `PreToolUse` · `Agent` · `pantonic-model-designer` · `prompt` casa `Ato:\s*` seguido, com ou sem crase, de `autoria`, `emenda` ou `conflito` | `Agente modelador recebe a tarefa "<título>" e vai fazer <ato> no modelo.` | `<ato>` ← a palavra casada |
| `M-14b` | o mesmo evento, sem casamento no `prompt` | `Agente modelador recebe a tarefa "<título>" e vai atualizar o modelo.` | `<título>` ← tarefa corrente |
| `M-15` | agente despachado, planejador — `PreToolUse` · `Agent` · `pantonic-planner` | `Agente planejador recebe a tarefa "<título>" e vai replanejar.` | `<título>` ← tarefa corrente |
| `M-16` | agente de volta, forma genérica — `PostToolUse` · `Agent`, ou o `UserPromptSubmit` da volta em hand-back, como em `M-4` · `pantonic-model-designer` ou `pantonic-planner`; ou `pantonic-executor`, `pantonic-reviewer`, `pantonic-consultant` cuja resposta não casa `M-4`, `M-4b`, `M-7`, `M-9` nem `M-9b` | `Agente <papel> devolveu a tarefa "<título>": <primeira linha>.` | `<papel>` ← `executor`, `revisor`, `consultor`, `modelador` ou `planejador` pelo `subagent_type`; `<primeira linha>` ← primeira linha não vazia da resposta, até 160 caracteres mais `…`; resposta vazia → `(sem texto)` |
| `M-18` | plano fechado — `PreToolUse` · `Bash` · numa invocação o programa é `encerrar.py`, o verbo é `plano` e o `--plano <caminho>` sai dos argumentos dessa mesma invocação (`TK-88`; `TK-88c`: script e verbo se leem na própria invocação) | `Scrum master vai fechar o plano "<título do plano>": registrar estado, relatório de entrega e a linha do diário.` | `<título do plano>` ← `titulo_plano` do estado ou a linha 1 do arquivo apontado por `--plano`; vazio → linha omitida |
| `M-17` | modelo do plano mostrado e turno acabado — `Stop` · estado com `aberta` e com `relatorio` | `Scrum master mostrou o modelo do plano e aguarda; a resposta dele está na extensão.` | nenhuma lacuna; estado ← sem `relatorio` (`aberta` fica). `relatorio` = true é gravado por `PreToolUse` · `Bash` · `command` contém `modelo.py show` sem `--drift` nem `--pendente`, com a janela aberta, sem gerar linha; sai no despacho de agente seguinte e no `backlog.py next`. `Stop` sem `relatorio` não gera linha. A frase diz só o que o gancho vê — o modelo mostrado e o turno acabado —, não se a janela encerrou nem o que se aguarda (`DTG-48`) |

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
  revisão vai à triagem do consultor, e só a rota `planejador` leva o **plano** a `blocked`, com a razão registrada, e a matéria ao planejador.
- O consumo da janela é lido de `docs/telemetria.tsv`, jamais auto-relatado.
- Plano `superseded`, e plano `blocked` por decisão do dono ainda não tomada, não entram em janela.
- O gerente acompanha a execução num painel fora da extensão que mostra `.claude/estado/progresso.txt`; cada linha desse arquivo é **gerada** pelo gancho `.claude/tools/progresso_hook.py` (eventos `PreToolUse`, `PostToolUse`, `UserPromptSubmit` — a volta do agente que entrega em hand-back, `DTG-39` — e `Stop`) a partir do evento da transição — `backlog.py next`, `backlog.py status`, o despacho e o retorno de cada agente, `review_evidence.py` e o encerramento —, com o título da tarefa no lugar da sigla (seção *Repertório de mensagens ao gerente*). O condutor **não escreve** linha de repertório, não usa marcador e não escreve no arquivo; nenhuma saída de ferramenta chega a ele (`P-0748`, `DTG-30`, `I-2`, `I-11`).
