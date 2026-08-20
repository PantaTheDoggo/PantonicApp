---
name: scrum-master
description: Conduz o loop de execução de um plano Pantonic* — despacha as tarefas do plano em sequência ao executor e ao reviewer, roteia pelo veredito calculado e encerra a janela por coesão e ocupação de contexto, sem round-trip com o dono a cada tarefa. Usar quando o pedido for tocar um plano inteiro em regime autônomo, e não uma tarefa avulsa.
---

# scrum-master — o loop de execução de um plano

Procedimento de **Orquestração** (`GOVERNANCA.md` §3, matriz de responsabilidades), executado no
**contexto principal** — é onde o dono interrompe o loop sem derrubar a sessão. Cada tarefa do plano
é executada por um subagente de contexto próprio e julgada por outro; o contexto do loop só recebe
as três linhas de transporte por tarefa.

**Modo tarefa única** (uma tarefa por invocação, escolhida pela diretiva do diário) continua sendo
`.claude/skills/proximo-passo/SKILL.md`. Esta skill é o **modo loop** sobre um plano nomeado.

O que o loop **não** faz: não implementa, não julga entrega e não decide arquitetura. Ele é o ponto
onde a decisão do dono é **devolvida ao dono** — nunca substituída por uma decisão própria
(`.claude/global/CLAUDE.md` Regra 8).

## Estado do loop

Três contadores, e só três. Nenhum outro estado governa o loop, e nenhuma decisão do loop se apoia
em percepção — o modelo não enxerga a própria ocupação de contexto.

| contador | zera em | onde é lido | para que serve |
|---|---|---|---|
| retentativas da tarefa corrente | início de cada tarefa | contador do loop | roteamento de `A6` e `A7`, com **uma** retentativa por tarefa |
| tarefas fechadas na janela | início da janela | contador do loop | relatório de encerramento |
| consumo acumulado da janela | início da janela | soma de `tokens_k` das linhas da janela em `docs/telemetria.tsv` | medida informativa, que alimenta a série |

Além deles, o loop guarda o **plano corrente** (caminho do `docs/plans/P-*.md`), a **tarefa corrente**
(identificador) e a **fila corrente** — a ordem em que as tarefas do plano serão tomadas. A fila
nasce da ordem de execução declarada pelo plano e é **reordenada em execução** pela regra `A3a`, que
é o motivo de ela ser estado do loop e não leitura do plano. Nada mais entra. Fonte normativa da
retentativa única e da ordem de precedência do bloco A: `docs/plans/P-0734-execucao-autonoma.md`,
seção `### DP-B`, lida junto da marca de revogação parcial no topo dela; do que encerra a janela,
`GOVERNANCA.md` §4.3 e a seção `### DP-Q`; da reordenação da fila, `### DP-G`, item 3.

## Fluxo

Dez passos, nesta ordem. Cada passo declara gatilho, entrada e saída; nenhum depende de juízo sobre
prosa.

### Passo 1 — Gate de modelo do contexto principal

- **Gatilho:** invocação da skill, antes de qualquer despacho.
- **Entrada:** modelo ativo do contexto principal.
- **Ação:** rodar `.claude/skills/modelo-por-fase/SKILL.md`. A fase do loop é **orquestração**
  (despacho, roteamento, arquivamento — não é juízo), e a linha `Orquestração` da matriz de
  `GOVERNANCA.md` §3 fixa o modelo. Modelo ativo diferente do exigido: **PARA e pede `/model` ao
  dono** — o loop não roda caro por conveniência.
- **Saída:** modelo conferido, ou parada com o `/model` pedido.

### Passo 2 — Seleção da próxima tarefa do plano

- **Gatilho:** passo 1 conferido, ou tarefa anterior fechada com "segue" no passo 10.
- **Entrada:** fila corrente do plano; `status` das tarefas no índice de `docs/DIARIO_DE_OBRAS.md`.
- **Ação:** tomar a **primeira** tarefa ainda não fechada **na fila corrente** — a ordem declarada
  pelo plano enquanto `A3a` não agiu nesta janela, e a ordem reordenada por `A3a` a partir daí; o
  §5 do plano deixa de ser lido diretamente depois da primeira reordenação, porque a fila é que
  carrega a dependência descoberta em execução. **Sempre uma, sempre sequencial** — o loop nunca
  despacha duas tarefas em paralelo, porque o roteamento do bloco A é por tarefa e retentativa
  concorrente não tem contador.
  Sem tarefa aberta no plano: encerrar pelo relatório de janela (o plano acabou).
- **Saída:** identificador da tarefa corrente e o cabeçalho dela, que carrega modelo, classe e teto
  na gramática `### <ID> — <título> [<modelo> · classe <classe> · teto <N>]`.

### Passo 3 — Gates herdados

- **Gatilho:** tarefa corrente selecionada.
- **Entrada:** dossiê da tarefa no plano; estado do plano.
- **Ação:** rodar, nesta ordem, **sem recopiar o texto de nenhum dos dois**:
  1. **`G-PLANREADY`** — `GOVERNANCA.md` §7, item 11 ("plano só é executável quando fechado").
  2. **Gate de delegação** — `.claude/skills/proximo-passo/SKILL.md`, seção "Gate de delegação —
     rodar ANTES de despachar o executor" (sete itens). É a cópia normativa.
  Qualquer um dos dois recusando: o loop **não delega** — vai ao passo 10 pela regra `B3`.

  Aprovados os dois, e **antes** de delegar, materializar `ready` → `in-progress` no kanban
  (`DP-G`, item 1, consequência 3). Materializar `status` é ato exclusivo do `scrum-master`: o
  executor recebe a tarefa já em `in-progress` e nunca produz esse valor.
- **Saída:** tarefa materializada em `in-progress` e liberada para despacho, ou parada com o que
  falta fechar.

### Passo 4 — Despacho do executor

- **Gatilho:** gates do passo 3 aprovados e tarefa materializada em `in-progress`.
- **Entrada:** dossiê da tarefa copiado do plano; modelo declarado no cabeçalho.
- **Ação:** antes de invocar o executor, gravar `.claude/estado/tarefa-corrente.json` — objeto
  único, sobrescrito a cada despacho, com os campos `tarefa` (identificador do card), `projeto`
  (nome do repositório), `modelo` (o mesmo do cabeçalho), `plano` (caminho do `docs/plans/P-*.md`
  corrente) e `despachado_em` (carimbo ISO 8601 do instante do despacho) — insumo do hook de
  `SubagentStop` (`T55`) que grava `docs/telemetria.tsv` sem gastar turno de agente. Local de
  máquina, gitignorado (`.claude/estado/`); o `scrum-master` só escreve esse arquivo, nunca o lê de
  volta — quem consome é o hook, depois do encerramento do subagente.

  Em seguida, invocar o agente `pantonic-executor` com o parâmetro `model` **igual ao modelo do
  cabeçalho** — o parâmetro da chamada vence o `model:` do arquivo do agente, e é assim que a
  escolha registrada no plano prevalece. O prompt de despacho leva o dossiê da tarefa e a instrução
  de devolver **uma única linha**, em uma das duas formas do domínio fechado (`DP-G`, item 2):

  ```
  <tarefa> review [pendencia=<uma linha>]
  <tarefa> blocked motivo=<dependencia|premissa> <uma linha de razão>
  ```

  O despacho declara também a **regra de desempate** (`DP-G`, item 3): na dúvida sobre qual dos dois
  motivos, o executor devolve `premissa` — reordenar por engano custa uma janela, e escalar por
  engano custa um turno do dono. Nenhuma instrução de RDO vai no despacho: o RDO nasce no
  fechamento (passo 9) e o executor não o toca. Guardrails de arquitetura também não são repetidos
  aqui: já vivem nos fatos estáveis do arquivo do agente. O despacho cola, junto do dossiê, as
  **âncoras** (arquivo, linha e texto do ponto a editar) re-derivadas no ato e o **range de linhas
  do bullet de fechamento anterior** quando a tarefa fecha em plano em andamento — a localização
  não paga em tool uses do executor, e é dela que vem o excedente de teto.
- **Saída:** uma linha de retorno do executor.

### Passo 5 — Recepção do retorno do executor

- **Gatilho:** retorno (ou queda) do executor.
- **Entrada:** a linha devolvida, em uma das duas formas da gramática do passo 4.
- **Ação:** ler a palavra devolvida — ela **é** o `status` da tarefa (`DP-G`, item 2) — e, quando
  ela for `blocked`, o `motivo=`. O `scrum-master` **materializa** o valor devolvido, transcrevendo
  **sem discricionariedade** (`DP-G`, item 1): não converte `blocked` em `review`, não converte
  `review` em `done` e não reclassifica o motivo. O que ele decide é o roteamento (passo 8), nunca o
  valor. Palavra fora das duas, `blocked` sem `motivo=`, `motivo=` fora do par
  `dependencia|premissa`, ou prosa no lugar da linha: **retorno inválido**, regra `A2`.

  Os `tools` gastos **não vêm daqui**: são lidos do bloco `<usage>` da notificação de conclusão,
  nunca do relato de quem executou.
- **Saída:** `status` materializado (`review` ou `blocked`), o `motivo` quando `blocked`, a
  `pendencia` quando presente, e os `tools` gastos lidos do `<usage>`, medida que segue para a
  série.

### Passo 6 — Despacho do `reviewer`

- **Gatilho:** **gatilho 1** da `DP-E` — a tarefa entrou em `review`. Tarefa devolvida `blocked`
  **não** passa por aqui (`DP-G`, item 4): não há entregável a julgar, e o roteamento dela é do
  passo 8.
- **Entrada:** o **mesmo dossiê** que o executor recebeu; plano e identificador da tarefa. Nenhum
  caminho de RDO é repassado, porque não existe RDO nesta altura do loop.
- **Ação:** gerar primeiro o dossiê de evidência mecânica, que o `reviewer` exige antes do despacho:

  ```
  python .claude/tools/review_evidence.py --plano <plano> --tarefa <ID> \
    --out docs/RDO/evidencia/<plano>-<ID>.md
  ```

  Redirecionar a saída padrão do comando (`> $null` no PowerShell, `> /dev/null` no Bash): o
  documento é para o `reviewer`, não para o contexto do loop. Em seguida invocar o agente
  `pantonic-reviewer` com o dossiê da tarefa e o caminho do dossiê de evidência, e a instrução de
  devolver só as duas linhas de veredito.
- **Saída:** duas linhas do `reviewer`.

### Passo 7 — Leitura do veredito

- **Gatilho:** retorno do `reviewer`.
- **Entrada:** as duas linhas fixas:
  `<tarefa> <veredito> <percentual> bloqueante=<dimensão|nenhuma>`
  `laudo=<caminho>`
- **Ação:** ler `veredito` ∈ {`aprovado`, `ressalva`, `reprovado`}, `bloqueante` e o caminho do
  laudo. Percentual e veredito são **calculados** pelo gerador; o loop não os recalcula, não os
  interpreta e não os discute. Em seguida colher a `recomendação` **do laudo**, onde ela é campo
  fechado (`seguir`, `seguir com ressalva`, `refazer`, `escalar`) — é o campo que `A6`, `A8`, `A9` e
  `B1` leem. Nada é acrescentado ao retorno de duas linhas do `reviewer`.
- **Saída:** tripla (`veredito`, `bloqueante`, `recomendação`) para o roteamento.

### Passo 8 — Roteamento, bloco A

- **Gatilho:** passo 5 concluído (regras `A1`..`A3b`) e passo 7 concluído (`A6`..`A9`).
- **Entrada:** `status`, `veredito`, `bloqueante`, `recomendação`, contador de retentativas.
- **Ação:** aplicar a tabela do bloco A **em ordem de precedência** — a primeira regra que casa
  vence e nenhuma outra é avaliada. Sem interpretação: toda condição é valor de campo ou contador.
- **Saída:** "segue" (vai ao passo 9) ou "PARA" (vai ao relatório de encerramento).

### Passo 9 — Arquivamento

- **Gatilho:** **gatilho 2** da `DP-E` — a tarefa entrou em `done`. Tarefa que termina em
  `cancelled`, e tarefa que para em `blocked`, **não** disparam RDO (`DP-F`, item 3, fechamento
  (c)); o gasto delas continua registrado pela telemetria.
- **Entrada:** o **pacote** extraído do laudo — os cinco campos que o `reviewer` é obrigado a
  deixar nele: veredito, percentual, dimensão bloqueante, recomendação e pendência (`DP-H`, item 4)
  — mais o consumo medido, o plano e o identificador da tarefa.
- **Ação:** escrever o RDO por **uma** chamada de `rdo.py close`, com o pacote passado como
  argumento e o consumo lido do `<usage>`:

  ```
  python .claude/tools/rdo.py close --plano <plano> --tarefa <ID> \
    --tool-uses <N> --tokens-k <N> --duracao-s <N> \
    --veredito <aprovado|ressalva> --percentual <0..100> --bloqueante <dimensão|nenhuma> \
    --recomendacao "…" --pendencia-laudo "…" [--pendencia "<pendência autoral do executor>"]
  ```

  Transcrever o valor que o gerador calculou não é originá-lo (`DA-6`, na leitura da `DP-H`, item
  4): o juízo continua saindo do cálculo de `rdo.py laudo`, e o loop apenas o carrega. O
  desdobramento é **calculado** pelo `close` a partir do veredito transcrito — não é escrito pelo
  loop. Os `tool-uses` medidos entram como registro do consumo, e nenhum desdobramento se abre por
  causa deles.

  Consumido o pacote, **apagar o laudo** (`DP-H`, item 3): ele é efêmero, nada dele é reinserido
  numa rodada seguinte e o RDO não guarda ponteiro para ele.

  Depois do fechamento, apender **uma linha** a `docs/telemetria.tsv` com o dado do bloco `<usage>`
  da notificação de conclusão, via `python .claude/tools/telemetria.py append` (`--fonte usage`;
  sem `<usage>`, `--fonte nao_medido`). O número nunca é copiado para o diário nem estimado pelo
  próprio agente: é essa linha que alimenta o contador de consumo da janela.

- **Saída:** RDO escrito com o desdobramento calculado, laudo apagado, linha nova em
  `docs/telemetria.tsv`, contadores da janela atualizados.

### Passo 10 — Continuar ou encerrar a janela

- **Gatilho:** passo 9 concluído com "segue" do bloco A.
- **Entrada:** `pendencia` da tarefa recém-fechada; sinal de coesão do contexto do loop; medida de
  ocupação da janela, injetada no contexto do loop pelo hook `PreToolUse` de medida quando ela
  cruza o teto de trabalho; próxima tarefa do plano.
- **Ação:** aplicar a tabela do bloco B, também por precedência. O encerramento por capacidade lê a
  medida de ocupação da janela (`GOVERNANCA.md` §4.3), injetada como aviso no contexto do loop
  quando cruza o teto; sem esse aviso na rodada, a janela encerra por coesão ou pelo fim do plano,
  e nunca por percepção, que o modelo não tem.
- **Saída:** volta ao passo 2 com a próxima tarefa, ou relatório de encerramento.

## Tabelas de roteamento

Forma operacional das regras. A fonte normativa — condições, motivo de cada valor e a prova de que
as regras cobrem o domínio inteiro — é `docs/plans/P-0734-execucao-autonoma.md`, seções `### DP-A`
(transporte), `### DP-B` (roteamento, lida junto da marca de revogação parcial no topo dela e da
`### DP-Q`, que remove o poder de rota dos tetos), `### DP-G` item 4 (a partição de `A3` e a queda de
`A5`) e `### DP-K` §14.4 (o laudo morre em qualquer desdobramento). Divergência entre esta tabela e
essas seções resolve sempre a favor da seção.

### Bloco A — o que fazer com a tarefa

| # | condição | ação |
|---|---|---|
| `A1` | queda do subagente (notificação sem bloco `<usage>`) | uma retomada por `SendMessage` ao mesmo `agentId` com "o que falta"; registra `PARCIAL — trecho pré-queda não medido`. Retomou: segue por `A2`..`A9`. Não retomou: **PARA** |
| `A2` | retorno ausente ou inválido (campo faltando, teto de campo estourado, linha fora da gramática) | um reenvio de **formato** ao mesmo executor; **não** consome a retentativa de conteúdo. Inválido de novo: **PARA** |
| `A3a` | `status=blocked` com `motivo=dependencia` | reordena a fila para que a bloqueada suceda a que a bloqueia e materializa `blocked` com a razão; **não** despacha o `reviewer`, **não** escreve RDO, **não** consome a retentativa e **não** incrementa o contador de tarefas fechadas: segue para a próxima elegível |
| `A3b` | `status=blocked` com `motivo=premissa` | materializa `blocked` com a razão; **não** despacha o `reviewer` e **não** escreve RDO: **PARA**, escalada ao dono |
| `A6` | `recomendacao=refazer` e retentativas gastas = 0 | despacha um executor **novo, em contexto novo**, com o dossiê original mais as **diretivas atualizadas** que o loop extraiu da recomendação — **nunca** o caminho do laudo, e **sem reescrever o dossiê**; contador := 1: segue |
| `A7` | `veredito=reprovado` e retentativas gastas = 1 | fecha o RDO como `reprovado`: **PARA** |
| `A8` | `recomendacao=seguir com ressalva` | fecha o RDO como `aprovado com ressalva`; cada ressalva e cada achado do laudo sai **com rota** (tíquete ou `sem ação`): segue |
| `A9` | `recomendacao=seguir` | fecha o RDO como `aprovado`: segue |

A recomendação é de domínio fechado — `seguir`, `seguir com ressalva`, `refazer`, `escalar` — e sai
calculada do laudo: o loop a **lê**, não a deriva do veredito. `bloqueante` diferente de `nenhuma`
implica `veredito=reprovado` — a combinação "aprovado com dimensão bloqueante vermelha" não chega à
tabela. Tarefa devolvida `blocked` não passa pelo `reviewer` (`DP-G`, item 4): não há entregável a
julgar, e a reordenação de `A3a` não fecha tarefa nenhuma.

O consumo medido da tarefa — os `tools` gastos contra o teto da classe declarada no cabeçalho — é
**alarme, nunca bloqueio**, e não é condição de nenhuma linha desta tabela: a entrega segue, o número
vai para `docs/telemetria.tsv` e rende insight no agregado da série (`GOVERNANCA.md` §3). O registro
qualitativo daquela tarefa, quando houver o que observar, mora no card **"Lições aprendidas na
tarefa"** do laudo, a critério do `reviewer`; sem observação, o número isolado se desconsidera.

**O laudo morre no consumo, em qualquer ramo** (`DP-K` §14.4). Extraída a recomendação, o
`scrum-master` **apaga** o laudo tanto na reexecução (`A6`) quanto no fechamento (`A7`..`A9`, passo
9) e na escalada (`B1`). Nenhuma linha destas tabelas guarda ponteiro para ele e nada dele é
reinserido numa rodada seguinte: o que a reexecução precisa saber viaja nas **diretivas
atualizadas**.

### Bloco B — continuar ou encerrar a janela

Avaliado **depois** de `A6`..`A9`, sobre a tarefa já fechada, e só quando o bloco A disse "segue".

| # | condição | ação |
|---|---|---|
| `B1` | `pendencia=` no retorno do executor, ou `recomendacao=escalar` no laudo | leva a pendência ao dono no relatório de encerramento e descarta o laudo: **PARA**, mesmo com veredito `aprovado` |
| `B2` | sinal de poluição do contexto do loop (**coesão**) **ou** aviso de ocupação da janela no teto de trabalho, injetado no contexto pelo hook de medida (**capacidade**) — as duas condições do `GOVERNANCA.md` §4.3 | encerra com relatório de janela: **PARA** (encerramento normal, não falha). Sem o aviso na rodada, valem a coesão e o fim do plano |
| `B3` | a próxima tarefa é recusada pelo `G-PLANREADY` ou pelo gate de delegação | não delega: **PARA**, com o que falta fechar |
| `B4` | nenhuma das anteriores | despacha a próxima tarefa do plano, sempre sequencial |

### O que obriga parada e o que segue com registro

- **Obriga parada:** decisão de arquitetura ou de requisito, que chega **sempre** pelo `pendencia=`
  do retorno do executor ou pela recomendação `escalar` do laudo (`B1`) — inclusive o achado que
  invalida a rota do plano; executor `blocked` por `motivo=premissa` (`A3b`); reprovação depois da
  última retentativa (`A7`); plano não-pronto (`B3`).
- **Segue com registro:** ressalva não bloqueante e achado fora de escopo **com rota**, ambos pelo
  laudo (`A8`) — a rota chega pelo laudo, ou pela linha de achado do sinal do executor, e é
  transcrita no RDO por quem fecha a tarefa; o loop só verifica que existe; e o
  `blocked` por `motivo=dependencia` (`A3a`), que reordena a fila e segue para a próxima elegível.
- **Parada defeituosa:** solicitar o dono em **caminho feliz ou caminho natural**, sem pendência
  aberta e sem demanda que seja dele. Despachar a próxima tarefa, criar o contexto novo e distribuir
  o handover são execução normal, e o loop os faz sozinho; parar para que o dono limpe o contexto ou
  invoque a tarefa seguinte o põe a **mediar execução normal**. Uma única ocorrência é defeito da
  entrega, mesmo com o plano correndo sem problema (`GOVERNANCA.md` §4.3).

Parada legítima não tem teto: acionamento cuja causa é do dono — ambiguidade, conflito de requisito
ou de aceitação — é ilimitado, e nenhum contador desta skill o restringe. O encerramento de janela
(`B2`) mede a **ocupação da janela de contexto** pelo aviso que o hook de medida injeta no
contexto quando ela cruza o teto, nas duas condições do `GOVERNANCA.md` §4.3, e o que sobe ao dono
fica fora dessa conta.

A fronteira do que é **ponto do dono** — decisão de arquitetura ou de requisito sim, evento
intrínseco do plano não — é a de `.claude/skills/proximo-passo/SKILL.md`, e não se redecide aqui. O
loop não classifica prosa: cada classe chega a ele por um campo ou por um contador.

## Relatório de encerramento

Uma vez por janela, na parada. Ponteiros e números, nunca o conteúdo dos registros:

- Plano conduzido e regra que encerrou a janela (`A1`..`A9` ou `B1`..`B4`, pelo identificador).
- Tarefas fechadas na janela, cada uma com identificador, desdobramento e caminho do RDO.
- Contadores finais: tarefas fechadas na janela e consumo acumulado, como medida para a série.
- **Pendências ao dono**, uma a uma, com o fato medido que a originou, o que cada opção implica, o
  que fica bloqueado sem resposta e a recomendação com o motivo.
- Próxima tarefa do plano, **sem iniciá-la**, e a recomendação de contexto novo antes da próxima
  janela.

## Proibições

- Não despacha duas tarefas em paralelo, e não encerra a janela por percepção de contexto.

## Guardrails

- Uma janela conduz **um** plano. Troca de plano ou de iniciativa é troca de cenário: encerra a
  janela e recomeça em contexto novo (`.claude/global/CLAUDE.md` Regra 2).
- O modelo de cada tarefa vem do cabeçalho dela no plano. Cabeçalho sem `[<modelo> · classe <classe>
  · teto <N>]` é tarefa fora da gramática: não se adivinha o modelo — cai em `B3`.
- O teto de tool uses da tarefa é o da classe registrada (`GOVERNANCA.md` §3), e vale a classe
  escolhida antes da delegação: o loop não a renegocia depois, porque reclassificar a posteriori
  falsifica a série. O número é referência de dimensionamento e alarme, e o loop segue com ele
  registrado.
- O consumo da janela é lido de `docs/telemetria.tsv`, jamais auto-relatado pelo subagente que
  executou — auto-relato desvia o suficiente para invalidar a série.
- Plano `superseded`, e plano `blocked` por decisão do dono ainda não tomada, não entram em janela.
