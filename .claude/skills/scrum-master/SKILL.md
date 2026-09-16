---
name: scrum-master
description: Conduz o loop de execução de um plano Pantonic* — despacha as tarefas do plano em sequência ao executor e ao reviewer, roteia pelo veredito calculado e encerra a janela por coesão e ocupação de contexto, sem round-trip com o dono a cada tarefa. Usar quando o pedido for tocar um plano inteiro em regime autônomo, e não uma tarefa avulsa.
---

# scrum-master — o loop de execução de um plano

Procedimento de **Orquestração** (`GOVERNANCA.md` §3) no **contexto principal**: cada tarefa é
executada por um subagente e julgada por outro. **Modo tarefa única**:
`.claude/skills/proximo-passo/SKILL.md`. Esta skill é o **modo loop** sobre um plano nomeado; não
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
- **Ação:** tomar a **primeira** tarefa ainda não fechada na fila corrente. Sem tarefa aberta:
  encerrar pelo relatório de janela.
- **Saída:** identificador da tarefa corrente e o cabeçalho dela, gramática
  `### <ID> — <título> [<modelo> · classe <classe>]`.

### Passo 3 — Gates herdados

- **Gatilho:** tarefa corrente selecionada.
- **Entrada:** dossiê da tarefa no plano; estado do plano.
- **Ação:** rodar `G-PLANREADY` (`GOVERNANCA.md` §7, item 11) e o Gate de delegação
  (`.claude/skills/proximo-passo/SKILL.md`, seção "Gate de delegação", sete itens), sem recopiar o
  texto de nenhum dos dois. Recusa de qualquer um: **não delega** — vai ao passo 10 por `B3`.

  Aprovados os dois, e **antes** de delegar, materializar `ready` → `in-progress` no kanban
  (`DP-G` item 1, consequência 3) — ato exclusivo do `scrum-master`.
- **Saída:** tarefa materializada em `in-progress` e liberada para despacho, ou parada com o que
  falta fechar.

### Passo 4 — Despacho do executor

- **Gatilho:** gates do passo 3 aprovados e tarefa materializada em `in-progress`.
- **Entrada:** dossiê da tarefa copiado do plano; modelo declarado no cabeçalho.
- **Ação:** gravar `.claude/estado/tarefa-corrente.json` (objeto único: `tarefa`, `projeto`,
  `modelo`, `plano`, `despachado_em` ISO 8601), insumo do hook `SubagentStop` (`T55`) para
  `docs/telemetria.tsv`. Capturar `git rev-parse HEAD` como `<ref>` (schema `DP-S`), usada no
  passo 6 (`AUT-T5b`).

  Invocar `pantonic-executor` com `model` **igual ao do cabeçalho** (vence o `model:` do agente),
  com o dossiê da tarefa e a instrução de devolver **uma única linha**, domínio fechado (`DP-G`
  item 2):

  ```
  <tarefa> review [pendencia=<uma linha>]
  <tarefa> blocked motivo=<dependencia|premissa> <uma linha de razão>
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
  status nem reclassifica o motivo — quem decide é o roteamento (passo 8). Palavra fora das duas, `blocked` sem `motivo=`, `motivo=` fora do par
  `dependencia|premissa`, ou prosa no lugar da linha: **retorno inválido**, regra `A2`.
- **Saída:** `status` materializado (`review` ou `blocked`), o `motivo` quando `blocked`, a
  `pendencia` quando presente, e os `tools` gastos lidos do `<usage>`.

### Passo 6 — Despacho do `reviewer`

- **Gatilho:** **gatilho 1** da `DP-E` — a tarefa entrou em `review`. Tarefa `blocked` **não** passa
  por aqui (`DP-G` item 4): não há entregável a julgar.
- **Entrada:** o **mesmo dossiê** que o executor recebeu; plano e identificador da tarefa. Nenhum
  caminho de RDO é repassado.
- **Ação:** gerar o dossiê de evidência mecânica, exigido pelo `reviewer`:

  ```
  python .claude/tools/review_evidence.py --plano <plano> --tarefa <ID> \
    --desde <ref capturada no passo 4> \
    --out docs/RDO/evidencia/<plano>-<ID>.md
  ```

  Redirecionar a saída padrão do comando. Em seguida invocar `pantonic-reviewer` com o dossiê da
  tarefa e o caminho do dossiê de evidência, instrução de devolver só as duas linhas de veredito.
- **Saída:** duas linhas do `reviewer`.

### Passo 7 — Leitura do veredito

- **Gatilho:** retorno do `reviewer`.
- **Entrada:** as duas linhas fixas:
  `<tarefa> <veredito> <percentual> bloqueante=<dimensão|nenhuma>`
  `laudo=<caminho>`
- **Ação:** ler `veredito` ∈ {`aprovado`, `ressalva`, `reprovado`}, `bloqueante` e o caminho do
  laudo — calculados pelo gerador, não recalculados pelo loop. Colher a `recomendação` **do
  laudo**, campo fechado (`seguir`, `seguir com ressalva`, `refazer`, `escalar`), lido por `A6`,
  `A8`, `A9` e `B1`.
- **Saída:** tripla (`veredito`, `bloqueante`, `recomendação`) para o roteamento.

### Passo 8 — Roteamento, bloco A

- **Gatilho:** passo 5 concluído (regras `A1`..`A3b`) e passo 7 concluído (`A6`..`A9`).
- **Entrada:** `status`, `veredito`, `bloqueante`, `recomendação`, contador de retentativas.
- **Ação:** aplicar a tabela do bloco A **em ordem de precedência** — a primeira regra que casa
  vence.
- **Saída:** "segue" (vai ao passo 9) ou "PARA" (vai ao relatório de encerramento).

### Passo 9 — Arquivamento

- **Gatilho:** **gatilho 2** da `DP-E` — a tarefa entrou em `done`. `cancelled`/`blocked` **não**
  disparam RDO (`DP-F` item 3, fechamento c); o gasto continua registrado pela telemetria.
- **Entrada:** o **pacote** extraído do laudo — os cinco campos obrigatórios (`DP-H` item 4):
  veredito, percentual, dimensão bloqueante, recomendação e pendência — mais o consumo medido, o
  plano e o identificador da tarefa.
- **Ação:** escrever o RDO por **uma** chamada de `rdo.py close`, com o pacote como argumento:

  ```
  python .claude/tools/rdo.py close --plano <plano> --tarefa <ID> \
    --tool-uses <N> --tokens-k <N> --duracao-s <N> \
    --veredito <aprovado|ressalva> --percentual <0..100> --bloqueante <dimensão|nenhuma> \
    --recomendacao "…" --pendencia-laudo "…" [--pendencia "<pendência autoral do executor>"]
  ```

  O desdobramento é **calculado** pelo `close`, não escrito pelo loop (`DA-6`, `DP-H` item 4).
  Consumido o pacote, **apagar o laudo** (`DP-H` item 3).

  Depois do fechamento, apender **uma linha** a `docs/telemetria.tsv` com o dado do bloco `<usage>`
  via `python .claude/tools/telemetria.py append` (`--fonte usage`; sem `<usage>`,
  `--fonte nao_medido`) — nunca copiado para o diário.
- **Saída:** RDO escrito com o desdobramento calculado, laudo apagado, linha nova em
  `docs/telemetria.tsv`, contadores da janela atualizados.

### Passo 10 — Continuar ou encerrar a janela

- **Gatilho:** passo 9 concluído com "segue" do bloco A.
- **Entrada:** `pendencia` da tarefa recém-fechada; sinal de coesão do contexto do loop; medida de
  ocupação da janela, injetada pelo hook `PreToolUse` de medida ao cruzar o teto de trabalho;
  próxima tarefa do plano.
- **Ação:** aplicar a tabela do bloco B, também por precedência. O encerramento por capacidade lê a
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
| `A6` | `recomendacao=refazer` e retentativas gastas = 0 | despacha um executor **novo, em contexto novo**, com o dossiê original mais as **diretivas atualizadas** que o loop extraiu da recomendação — **nunca** o caminho do laudo, e **sem reescrever o dossiê**; contador := 1: segue |
| `A7` | `veredito=reprovado` e retentativas gastas = 1 | fecha o RDO como `reprovado`: **PARA** |
| `A8` | `recomendacao=seguir com ressalva` | fecha o RDO como `aprovado com ressalva`; cada ressalva e cada achado do laudo sai **com rota** (tíquete ou `sem ação`): segue |
| `A9` | `recomendacao=seguir` | fecha o RDO como `aprovado`: segue |

A recomendação é de domínio fechado — o loop a **lê**, não a deriva do veredito. `bloqueante`
diferente de `nenhuma` implica `veredito=reprovado`. O consumo medido é **medida e registro, nunca
critério de rota** (`DP-Q`): vai para `docs/telemetria.tsv`. **O laudo morre no consumo, em
qualquer ramo** (`DP-K` §14.4): `A6`, `A7`..`A9` e `B1` — o que a reexecução precisa saber viaja
nas **diretivas atualizadas**.

### Bloco B — continuar ou encerrar a janela

Avaliado **depois** de `A6`..`A9`, sobre a tarefa já fechada, e só quando o bloco A disse "segue".

| # | condição | ação |
|---|---|---|
| `B1` | `pendencia=` no retorno do executor, ou `recomendacao=escalar` no laudo | registra a pendência como `AE-<n>` em `## Achados da execução` do plano, descarta o laudo e escala ao **planejador** — a rodada de replanejamento vira a próxima tarefa do plano (`G-REPLAN`) e o relatório de encerramento a nomeia; ao dono chega só o que o planejador classificar como estratégico (`G-NOASK`, `GOVERNANCA.md` §7 item 18): **PARA**, mesmo com veredito `aprovado` |
| `B2` | sinal de poluição do contexto do loop (**coesão**) **ou** aviso de ocupação da janela no teto de trabalho, injetado no contexto pelo hook de medida (**capacidade**) — as duas condições do `GOVERNANCA.md` §4.3 | encerra com relatório de janela: **PARA** (encerramento normal, não falha). Por coesão o encerramento **não é gracioso**: nada produzido depois do sinal de poluição se aproveita. Sem o aviso na rodada, valem a coesão e o fim do plano |
| `B3` | a próxima tarefa é recusada pelo `G-PLANREADY` ou pelo gate de delegação | não delega: **PARA**, com o que falta fechar |
| `B4` | nenhuma das anteriores | despacha a próxima tarefa do plano, sempre sequencial |

### O que obriga parada e o que segue com registro

- **Obriga parada:** decisão de arquitetura ou de requisito, que chega **sempre** pelo `pendencia=`
  do retorno do executor ou pela recomendação `escalar` do laudo (`B1`), roteada ao planejador —
  inclusive achado que invalida a rota do plano; executor `blocked` por `motivo=premissa` (`A3b`); reprovação depois da
  última retentativa (`A7`); plano não-pronto (`B3`).
- **Segue com registro:** ressalva não bloqueante e achado fora de escopo com rota, pelo laudo
  (`A8`); e o `blocked` por `motivo=dependencia` (`A3a`), que reordena a fila e segue para a
  próxima elegível.
- **Parada defeituosa:** solicitar o dono em caminho feliz, sem pendência aberta e sem demanda
  dele. Despachar a próxima tarefa, criar o contexto novo e distribuir o handover são execução
  normal. Uma única ocorrência é defeito da entrega (`GOVERNANCA.md` §4.3).
  Também defeituosa: qualquer pergunta ao dono (`AskUserQuestion` ou prosa) **entre o despacho de
  uma tarefa e o relatório de encerramento** — o loop não fica com dúvida: registra `AE-<n>`,
  materializa `blocked premissa` e para (`G-NOASK`). Toda opção de rota do relatório inclui
  **registrar e não agir** quando ela existir.

A fronteira do **ponto do dono** é a de `.claude/skills/proximo-passo/SKILL.md`, e não se redecide
aqui.

## Relatório de encerramento

Uma vez por janela, na parada. Ponteiros e números, nunca conteúdo:

- Plano conduzido e regra que encerrou a janela (`A1`..`A9` ou `B1`..`B4`, pelo identificador).
- Tarefas fechadas na janela, cada uma com identificador, desdobramento e caminho do RDO.
- Contadores finais: tarefas fechadas na janela e consumo acumulado, como medida para a série.
- **Pendências ao dono**, uma a uma, com o fato medido que a originou, o que cada opção implica, o
  que fica bloqueado sem resposta e a recomendação com o motivo.
- Próxima tarefa do plano, **sem iniciá-la**, e a recomendação de contexto novo antes da próxima
  janela. No mesmo ato, reescreve a linha `**Fila corrente:**` do cabeçalho de
  `docs/DIARIO_DE_OBRAS.md` (primeiras 15 linhas).

## Proibições

- Não despacha duas tarefas em paralelo, e não encerra a janela por percepção de contexto.
- Não pergunta ao dono entre o despacho e o relatório de encerramento (`G-NOASK`).

## Guardrails

- Uma janela conduz **um** plano. Troca de plano ou de iniciativa é troca de cenário: encerra a
  janela e recomeça em contexto novo (`.claude/global/CLAUDE.md` Regra 2).
- O modelo de cada tarefa vem do cabeçalho dela no plano. Cabeçalho sem
  `[<modelo> · classe <classe>]` é tarefa fora da gramática: cai em `B3`.
- O `scrum-master` **não revisa plano** (`GOVERNANCA.md` §3): indício de que o plano precisa de
  revisão leva o **plano** a `blocked`, com a razão registrada, e a matéria ao planejador.
- O consumo da janela é lido de `docs/telemetria.tsv`, jamais auto-relatado.
- Plano `superseded`, e plano `blocked` por decisão do dono ainda não tomada, não entram em janela.
