---
name: passagem-de-bastao
description: Maquinário de transição entre tarefas de um plano Pantonic*, na superfície agente↔agente — drena os inboxes, apura a fila pela diretiva, monta o dossiê de delegação sob o gate, herda o contexto da tarefa anterior, fecha a tarefa no registro canônico e grava o checkpoint da janela. Usar como procedimento interno do scrum-master, nunca como ponto de entrada do gerente.
---

# passagem-de-bastao — a transição entre tarefas

Procedimento da **Orquestração** (`GOVERNANCA.md` §3). Ele é o maquinário que o
`.claude/skills/scrum-master/SKILL.md` usa entre uma tarefa e a seguinte: **superfície
agente↔agente**, transparente para o gerente do projeto — ele não a invoca, não a lê e não a
acompanha. Não é skill de comunicação com humano; o que chega ao dono chega pelo **relatório de
encerramento** do `scrum-master`, e só lá.

Esta skill não implementa, não julga entrega e não substitui decisão do dono
(`.claude/global/CLAUDE.md` Regra 8). Os "fatos estáveis" da arquitetura de cada projeto ficam no
arquivo do agente executor daquele projeto (`.claude/agents/*.md`), não aqui.

**Vocabulário de estados:** esta skill *consome* o kanban e não define estado nenhum. A lista final
de valores de `Status`, a máquina de transições e o alcance de cada estado por objeto (tarefa,
plano/iniciativa, tíquete) têm residência única — skill `diario-de-obras`, seção
`## Status — residência única`. Em dúvida sobre um estado, ler lá; nunca reenunciar a lista aqui.
`superseded` é vocabulário de **plano/iniciativa**: não existe tarefa `superseded`.

## Parte 1 — Apurar a fila

1. **Drenar os dois inboxes** — antes de escolher qualquer tarefa:
   1. **Inbox de planos** — `python .claude/tools/backlog.py drain` promove cada linha viva de
      `docs/plans/_INBOX.md` ao índice do diário e a move para `docs/plans/_INBOX_HISTORICO.md`.
   2. **Fila de candidatos a memória** — se `<memory-dir>/_INBOX.md` tiver linha ainda não marcada
      (`<memory-dir>` = `~/.claude/projects/<slug>/memory/`), apresentá-la ao dono **na abertura da
      janela** — `AskUserQuestion` com promover/descartar por candidato — e marcar a linha conforme
      a decisão. O agente **nunca promove sozinho**; sem esta drenagem a fila acumula e a disciplina
      degrada de volta para gravar direto em memória
      (`.claude/global/docs/GOVERNANCA_MEMORIAS.md` §8). Fila vazia ou toda marcada: seguir sem
      ruído.

2. **Apurar a fila é rodar o instrumento**: `python .claude/tools/backlog.py next` devolve a
   próxima tarefa e o dossiê dela; a ordem de seleção não se reproduz aqui e não se lê antes de
   rodar, porque é comportamento do instrumento. Quando `next` recusa, ele **nomeia a condição** —
   `E-1` dois ou mais `in-progress`, `E-2` linha de status ausente, `E-3` linha de índice ausente —
   e o que se faz é corrigir o dado que ele nomeou, nunca escolher à mão.

3. **Tomar UMA tarefa** — Grep pelo ID no diário, ler só a seção correspondente (nunca o diário
   inteiro). Para retomar sprint `in-progress`: `Read docs/DIARIO_DE_OBRAS.md offset:1 limit:15` — o
   bloco `**Fila corrente:**` no cabeçalho carrega o ID da tarefa e o range exato do dossiê dela; ir
   direto lá, nunca leitura sequencial nem varredura por Grep.

   Tíquete N/A-legado (campos "N/A — migrado", autorado dias/semanas atrás): classificar antes de
   qualquer delegação — (1) objetivo AFIRMA estado de código → 1-3 sondas baratas (Grep/Read/
   `git log`) verificam se a premissa ainda existe; já satisfeita → fechar inline com ponteiro ao
   commit; (2) objetivo é PERGUNTA de produto ("se X for desejado...") → decisão do dono, nunca
   delegar; (3) objetivo correto mas sem design definido → fase de escopamento própria (scouts +
   verificações), cujo produto é o que torna o dossiê autossuficiente para quem executa. Se a
   varredura FIFO percorrer vários itens consecutivos sem achar um despachável, parar e apresentar o
   cluster inteiro (agrupado por tipo) para decisão em lote do dono — 1 round-trip, não N.

## Parte 2 — Montar o dossiê e delegar

**Despachar ao papel competente é critério do orquestrador, não etapa mecânica.** O dossiê da tarefa
é copiado da seção do diário ou do card do plano, com objetivo, arquivos-alvo, contratos, testes e
critério de pronto.

**Instrumento antes de protocolo** (disciplina de instrumento, `GOVERNANCA.md` §3): ao preparar a
revisão, rodar `review_evidence.py`/`rdo.py` primeiro e abrir o protocolo do `pantonic-reviewer` só
se a evidência existir; `--help` antes do primeiro uso de cada instrumento na janela.

**Dieta do prompt:** carregar só o dossiê da tarefa — guardrails de arquitetura já vivem nos "fatos
estáveis" do arquivo do agente e não devem ser repetidos aqui; repetir paga o mesmo texto em todos os
turnos do executor.

**Levantamento de contexto antes do dossiê** — regra de precedência, não gatilho condicional: toda
coleta que não seja Read de âncora já conhecida (arquivo + range de linhas) ou Grep de string exata
vai para o papel barato — `pantonic-scout` (agente Pantonic* do projeto) ou, fora dele,
`context-scout` (`.claude/global/agents/context-scout.md`) via skill `context-prep`
(`.claude/global/skills/context-prep/SKILL.md`) —, nunca para leitura direta do modelo principal.
O orquestrador monta o prompt de delegação a partir só do dossiê compacto devolvido pelo scout.

**Fonte do contexto, em ordem de preferência:** (1) dossiê pré-autorado (`sprint_plan.md`, card de
plano) copiado verbatim, **inclusive o campo `Oração do modelo` com os sub-bullets de texto** (é a única forma de o executor ler o
modelo — `GOVERNANCA.md` §3.2) — exceto números de aceite, ver gate abaixo; (2) **herança de contexto** da
tarefa predecessora: precedente já pago nesta janela (âncoras re-derivadas, rota confirmada, rota
descartada, achado já medido) colado na delegação — custo marginal zero, e é o que impede a sucessora
de redescobrir o que a antecessora já pagou; (3) `pantonic-scout`/`context-scout` (skill
`context-prep`): DESCOBERTA quando não há dossiê; DETALHE (1 pergunta fechada por spawn, paralelos)
quando o pré-autorado referencia shapes de módulos implementados depois dele; (4) leitura direta —
exceção declarada no ato, motivo escrito — só para Read de âncora já conhecida ou Grep de string
exata; qualquer outra coleta é (3). A mesma régua vale FORA deste fluxo: pedido direto de
planejamento/análise cuja exploração estimada passe de ~15 tool uses usa `context-prep`.

**Gate `G-PLANREADY` (`GOVERNANCA.md` §7 item 11) — antes do gate de delegação:** só se delega tarefa
de plano **fechado**. Se o plano da tarefa escolhida tem questão pendente, bloco a preencher, ramo
condicional não resolvido ou tarefa cujo conteúdo depende de artefato inexistente, **não se delega**:
registra-se o que falta fechar e a matéria volta ao planejamento. Delegar plano aberto empurra a
decisão para o executor, no modelo mais barato e sem o contexto de quem decidiu.

**Gate de delegação — residência única, roda ANTES de despachar o executor:**

1. **Tema único**, sem cláusula "investigue X" (nem introduzida pelo orquestrador ao transcrever);
   bifurcação prevista resolvida por verificação barata, dossiê de scout ou decisão do dono. Exceção:
   bifurcação só decidível DENTRO da tarefa → delegar com os ramos enumerados + critério de parada
   explícito por ramo.
2. Toda linha "lacuna/não confirmado" de scout descarregada antes, ou promovida a sub-tarefa. Nota
   herdada do plano tipo "aproveitar para Y (custo ~zero)" conta como **assunto adicional**.
3. Números de aceite (piso, contagem de suíte, call sites) re-derivados por 1 comando barato agora —
   nunca copiados do plano (contagens envelhecem com a própria sprint). String destinada a assert é
   citação colada do output de verificação, nunca paráfrase — token negativo errado passa em
   silêncio. Junto dos números vão as **âncoras** (arquivo, linha e texto do ponto a editar)
   re-derivadas no ato e, quando a tarefa fecha em plano em andamento, o **range de linhas do bullet
   de fechamento anterior**: sem isso o dossiê não é autossuficiente e quem executa precisa
   redescobrir a localização — trabalho que a tarefa não pediu.
4. Afirmação negativa de escopo ("não toca contracts/services") com campo novo persistido exige 1
   grep pelo gate de ESCRITA (`extra.*forbid`, validador) antes de ser afirmada. Rename/move de
   símbolo público: grep também em docs vivos (`docs/*.md`, excluindo históricos).
5. **Decomposição por tema, não por volume** — **dimensionamento do planejador**
   (`GOVERNANCA.md` §3), nunca instrução de parada a quem executa. A unidade de trabalho é o
   **módulo coeso**: divide-se quando o card cruza **dois assuntos**, nunca quando cruza muitas
   regiões do **mesmo** assunto. Número de regiões editadas é medida informativa, não gatilho de
   divisão. Se "Arquivos-alvo" cruza ≥3 camadas da regra de dependência E ≥1 exige padrão sem
   precedente no código, isso é indício de **dois temas** — decompor por camada. A divisão é o
   controle; a régua que dimensiona cada tarefa mora na tabela de `GOVERNANCA.md` §3 e não se
   reapresenta no dossiê.
6. Tarefa-investigação (entregável = descoberta/mapeamento): itens 1-5 não se aplicam; o dossiê
   PRESCREVE o método de sondagem (artefato grande/linha única = sonda programática via scratchpad;
   Read estoura e Grep colapsa). O dimensionamento continua sendo do planejador, pela régua de
   `GOVERNANCA.md` §3, e não vira declaração no card.
7. Build/verify com artefato existente (`dist/`, `.exe`): o dossiê declara "não deletar o artefato de
   saída" — deleção não autorizada é ação destrutiva, não limpeza.

Recusa de qualquer item do gate: **não delega**, e o que falta fechar volta ao planejamento.

## Parte 3 — Fechar a tarefa

1. **Gate** — tarefa dada como concluída já passou pela skill `guardrails-check` (Tier 2 no mínimo —
   dirs tocados + `tests/conformance/` verde; Tier 3 completo só quando a própria tarefa/sprint
   exigir). Sem gate verde, o destino é `blocked` ou permanece `in-progress`, nunca `done`. No mesmo gate, `python .claude/tools/modelo.py check --plano <plano>` sai `0` ou `2` (`GOVERNANCA.md` §3.2); exit `1` mantém
   `in-progress` e escala ao consultor com o stderr.

2. **Materializar o status e registrar**: `python .claude/tools/backlog.py status <ID> <estado>`
   materializa o `status`, em qualquer estado — ato exclusivo da **orquestração**: o executor é
   **autor** de `review` e `blocked`, e de mais nada. O registro canônico da tarefa é o **RDO**; o
   diário guarda a linha de status que aponta para lá (`GOVERNANCA.md` §4.2, "Fronteira de
   registro").
   - **Nunca na célula do índice:** se a tarefa pertence a um `### <ID>` do diário, o destino é a
     "Notas de execução" daquela seção; se a sprint vive inteiramente em `docs/plans/P-*.md`, o
     destino é uma seção do próprio plano — a célula do índice fica travada em status + ≤ ~1-2 frases
     + ponteiro.
   - **Registro único do achado** (`GOVERNANCA.md` §4.2): o achado — de bloqueio, de obstáculo ou
     fora de escopo — é escrito **uma vez**, como entrada `AE-<n>` em `## Achados da execução` do
     plano. Nota da tarefa, `Fila corrente` e célula do índice recebem `AE-<n>` + `caminho:linhas`.
     Escrever o mesmo fato em cinco lugares custou um terço de uma janela.
   - **Achado fora de escopo com ação futura** (falha de teste pré-existente OU risco/recomendação
     registrado só em decision record/prosa) vira, NA MESMA SESSÃO: (a) a entrada `AE-<n>` apensada
     ao final do plano de origem, com o contexto que a motivou, e (b) linha de índice no diário com
     âncora apontando para ela. Nota em prosa não satisfaz o guardrail. `TK-*` solto (seção no
     próprio diário) só quando a tarefa de origem for avulsa, sem plano-pai.
   - **Dono do gatilho de condensação:** diário acima de ~500 linhas OU bullet recém-escrito acima de
     ~30 linhas → operação Condensar (skill `diario-de-obras`) na mesma sessão. O flip de status da
     sprint acompanha o início/fim de suas tarefas — índice nunca defasado do WIP real.
   - **Gate de triagem no fechamento de sprint:** o flip da sprint para `done` exige triagem da seção
     `## Achados da execução` do plano — cada achado sai com rota: (a) tarefa em plano derivado,
     (b) decisão do dono em lote, ou (c) rejeitado com razão de 1 linha na própria entrada. Sprint
     não fecha com achado sem rota.
   - **Nota-forward de obsolescência:** obsolescência de plano/audit descoberta na execução (arquivo
     movido, contagem mudada, escopo invalidado) que afete tarefas RESTANTES do mesmo plano é
     registrada junto à sugestão de próxima tarefa — o plano histórico não se edita; a nota do diário
     é o canal vivo.

3. **Telemetria pós-notificação** — a série é do orquestrador, e o executor não edita o diário nem
   relata o próprio consumo. Fechar = apender **uma linha** a `docs/telemetria.tsv`
   (`.claude/tools/telemetria.py append`; `--fonte usage` a partir do bloco `<usage>` da notificação,
   `--fonte contado` na execução inline sem `<usage>` — contagem efetiva das chamadas no transcript,
   nunca estimativa; sem contagem, `nao_medido`) e escrever no registro o ponteiro
   `Consumo: ver docs/telemetria.tsv` — **nunca o número em prosa** (`GOVERNANCA.md` §4.2, fonte
   única). Read offset/limit da região do bullet → Edit; NUNCA Edit apoiado em Read anterior à
   chamada `Agent` (o hiato de delegação invalida o rastreio). No pickup, 1 Grep pelo texto-promessa:
   match de sessão anterior = telemetria vencida → linha na série com `fonte: nao_medido`.

   **Queda de subagente:** notificação de falha não traz `<usage>` → registrar "PARCIAL — trecho
   pré-queda não medido". Antes de re-delegar a frio: `git status --short` + Read do artefato-alvo +
   `SendMessage` ao MESMO agentId com "o que falta"; só re-delegar se não retomar. Transcript/output
   de subagente é read-only — nunca apagar/mover/editar.

4. **Registrar decisões e lições** (se houver): mudança comportamental intencional → decision record
   `D-*` no doc AS-IS; incidente com diagnóstico não-óbvio → entrada no doc de lições aprendidas.

## Parte 4 — Checkpoint da janela

A Parte 3 fecha uma tarefa que chegou ao fim. O checkpoint é outra coisa: quem **orquestra** chega ao
fim da janela com o **plano** ainda aberto. Sem ele, a descoberta já paga (o que já foi decidido, o
que já foi descartado, onde a série parou) morre com o contexto e a janela seguinte a reexecuta do
zero — pagando duas vezes pelo mesmo achado.

**O portador é a Orquestração**: quem grava o checkpoint é quem conduz a janela, nunca quem executa
a tarefa.

O checkpoint é **ponteiro de estado, não relatório intermediário**: não narra o que foi feito, não
justifica decisões, não repete o que já está no diário ou no plano.

- **Gatilho** — a janela de orquestração se encerra (coesão ou ocupação) com tarefas do plano ainda
  abertas: sinal qualitativo, não número — nenhum teto de consumo dispara o checkpoint. Não esperar a
  certeza plena: sem orçamento sobrando não há como escrever o checkpoint.
- **Entregável** — até **5 linhas** na "Notas de execução" do plano em curso, uma linha por item:
  1. o que já está **descoberto e decidido** (inclusive rotas descartadas — descarte é achado);
  2. o que **falta**;
  3. **arquivos tocados**, com `caminho:linha`;
  4. o **próximo passo exato** (a ação seguinte, não o objetivo da tarefa);
  5. o que **não precisa ser refeito**.
- **Teto do próprio checkpoint: 2 tool uses** — um `Grep` para achar a âncora e um `Edit`. O
  checkpoint tem de custar menos que a descoberta que preserva; se está custando mais que 2 chamadas,
  ele virou relatório. Sem releitura de verificação, sem varredura para "completar" o estado.
- Depois do checkpoint, o **plano** fica com o ponto de parada anotado; a tarefa que não chegou a ser
  entregue volta ao estado em que estava — nunca `done`.

**Dois casos que NÃO são checkpoint.**

- **Contexto poluído — retorno não gracioso.** Ao sinal de poluição (`.claude/global/CLAUDE.md`
  Regra 2; texto operacional em `GOVERNANCA.md` §4.3), nada se inicia e nada do que foi produzido
  depois do sinal se aproveita. **Não se escreve ponteiro de retomada, porque não há retomada**: o
  retorno é a declaração de contexto poluído mais a demanda de **reexecução em contexto limpo**.
- **Contexto acabando dentro de uma tarefa — tarefa mal dimensionada.** Não é evento a mitigar com
  checkpoint: é **sintoma** de que o recorte errou a *Diretriz de dimensionamento de tarefa*
  (`GOVERNANCA.md` §3), e dimensionar é do planejador. Registra-se o fato no corpo da tarefa e
  devolve-se a matéria ao planejamento. **Não** se retoma a tarefa pela metade em contexto novo.

## A fronteira do ponto do dono

Residência única desta fronteira; quem precisar dela aponta para cá.

- **O que conta como ponto do dono:** só decisão de **arquitetura** ou de **requisitos**. **Evento
  intrínseco do projeto não se pergunta — executa-se:** desbloqueio de plano cuja dependência
  registrada foi satisfeita, flip de status, avanço para a fase seguinte de uma iniciativa já
  aprovada e demais consequências mecânicas de um plano vigente são evolução natural, já decidida
  quando o plano foi aprovado. Escalar evento intrínseco gasta turno do dono e devolve a ele trabalho
  que o plano já resolveu — é o erro simétrico ao de decidir arquitetura sozinho
  (`.claude/global/CLAUDE.md` Regra 8).
- **Quando o ponto do dono se apresenta:** só no **relatório de encerramento** da janela — nunca
  entre o despacho e o fechamento. Obstáculo, instrumento que não produz ou dúvida no meio da janela
  não viram pergunta: viram `AE-<n>` em `## Achados da execução` do plano, tarefa `blocked` razão
  `premissa` e rodada de replanejamento como próxima tarefa (`G-NOASK`, `GOVERNANCA.md` §7 item 18).
- **Decisão pendente é o próximo passo:** se a tarefa executada deixou ponto para o dono decidir, o
  próximo passo é **a decisão**, não a próxima tarefa do backlog. Cada ponto é apresentado com (1) o
  **fato medido** que o originou, (2) o que **cada opção implica**, (3) o que **fica bloqueado ou
  nasce errado** sem resposta e (4) uma **recomendação** com o motivo. Toda opção de rota inclui
  **registrar e não agir** quando ela existir.

## Guardrails

- Uma tarefa por despacho; nunca duas em paralelo.
- **Nunca escolhe tarefa de plano `superseded`** (terminal, fora do backlog) nem `blocked` cuja razão
  seja `validação postergada` enquanto suas implementações-dependência não estiverem todas `done`.
  Plano `superseded` NÃO é retomado nem "continuado" — a rota foi substituída; se ele parece a
  próxima coisa a fazer, o erro está na leitura do estado, não no plano vivo.
- **Convergência de iniciativa (rebase antes de escolher):** iniciativa com 2+ planos vivos
  (`ready`/`in-progress`/`blocked` não-postergado) disputando a mesma rota significa que a
  reconciliação A/B/C (skill `diario-de-obras`, seção "Planos derivados") foi pulada. Parar, rebasear
  e só então escolher o **único** plano vivo — sempre o mais recente cuja premissa não foi
  contradita.
- Plano `blocked` por decisão owner-gated não resolvida **não é delegável ao executor**: os pontos
  pendentes vão ao dono e o procedimento para — nunca iniciar a implementação nem redescobrir o que o
  plano já responde.
- **Bloqueio por premissa abre rodada, não pula tarefa** (`G-REPLAN`, `GOVERNANCA.md` §7 item 17):
  tarefa `blocked` com razão `premissa` no plano priorizado torna a **rodada de replanejamento** a
  próxima tarefa — delegada ao `pantonic-planner`, com o achado do corpo da tarefa como dossiê, nunca
  ao executor; a tarefa seguinte do mesmo plano não é despachada enquanto a rodada não fechar. Só o
  que o planejador classificar como estratégico chega ao dono.
- Empate entre itens do mesmo nível desempata por ordem de entrada no índice (mais antigo primeiro).
- Diário sem item `ready`/`in-progress`/`blocked`: reportar explicitamente — não inventar trabalho
  nem reabrir item `done`/`cancelled`.
- Diretiva de priorização só muda por escrita explícita no diário (skill `diario-de-obras`, operação
  "registrar diretiva de priorização") — nunca inferida de uma conversa que não a persistiu.
- **Trava de contexto (vale para QUALQUER agente):** depois de a tarefa fechar, pedido para iniciar a
  próxima **no mesmo contexto** do executor não se atende — responde-se com o ID/título e a
  recomendação de contexto limpo. A trava só cai se o dono, já avisado, insistir explicitamente.
- Higiene de busca: Grep que precisa do TEXTO usa sempre `output_mode: content`; tarefa de sprint no
  diário é bullet dentro de `## SPRINT-*` (nunca heading `###` — Grep pelo ID literal); padrão de
  busca é colado do texto real, nunca suposto; `Grep.offset` conta MATCHES, não linhas de arquivo —
  seek posicional é `Read offset/limit`; âncora confirmada + especulativa vão juntas numa alternância
  na mesma chamada.
- Achado de processo recorrente (≥3×) e de risco zero (edição de 1 linha em doc/skill) não espera
  lote de tíquete acumulador: entra no relatório de encerramento da mesma janela como pendência ao
  dono, com a opção de registrar e não agir — nunca como pergunta no meio da janela (`G-NOASK`).

## Proibições

- Não decide arquitetura, não replaneja e não revisa plano — indício de que o plano precisa mudar vai
  ao planejador (`GOVERNANCA.md` §3, escada de revisão de plano).
- Não marca `done` com conformance vermelho ou piso de regressão abaixo do registrado.
- Não deixa o registro canônico desatualizado: tarefa fechada sem RDO e sem a linha de status no
  diário não está fechada.
