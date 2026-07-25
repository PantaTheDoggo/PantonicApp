---
name: proximo-passo
description: Ponto de entrada de contexto novo para "execute o próximo passo do backlog" — drena o inbox de planos, escolhe a próxima tarefa do diário de obras pela diretiva de priorização (ou heurística padrão), delega a execução e fecha com relatório fixo. Usar quando o usuário pedir para pegar/continuar o backlog sem nomear uma tarefa específica.
---

# proximo-passo — retomada de backlog em contexto novo

Ponto de entrada canônico para o fluxo "abro contexto novo, digo 'execute o próximo passo do
backlog', recebo um relatório". Não substitui GOVERNANCA §4 — orquestra `diario-de-obras` +
`pantonic-executor` + `handover` numa sequência fixa.

## Fluxo

1. **Drenar inbox** — skill `diario-de-obras`, operação "drenar inbox de planos": promove linhas
   novas de `docs/plans/_INBOX.md` para o índice do diário antes de escolher qualquer tarefa.

2. **Ler diretiva de priorização** — primeira linha do diário (`docs/DIARIO_DE_OBRAS.md`), logo
   abaixo do título. Se vazia, aplicar heurística padrão, nesta ordem:
   1. Itens `blocked` cuja razão registrada já não se aplica (destravar).
   2. Itens `in progress` (WIP de 1 iniciativa por vez — nunca abrir uma segunda enquanto uma
      primeira está em andamento).
   3. Tíquetes avulsos de bug (`TK-*` descritos como bug).
   4. Demais itens `backlog`, por ordem de entrada no índice (FIFO).
   Se a diretiva nomear uma iniciativa/bug específico, ela tem precedência total sobre a
   heurística — ex.: "Priorize iniciativa X" pula direto para a próxima tarefa `backlog`/
   `in progress` daquela âncora, mesmo que outra iniciativa esteja mais antiga no índice.

   Se houver 2+ iniciativas `in progress` com Diretiva vazia, não desempatar por FIFO nem
   "momentum": `AskUserQuestion` — empate de WIP é prioridade não persistida. Instrução de
   prioridade do dono que dispara execução escreve a linha de Diretiva no mesmo ato, não só
   nota de seção.

3. **Escolher UMA tarefa atômica** — nunca mais de uma por contexto (GOVERNANCA §4.3). Grep pelo
   ID no diário, ler só a seção correspondente (nunca o diário inteiro).

   Para retomar sprint `in progress`: Grep por `Próxima tarefa da sprint` (`output_mode:
   content`, `-A 2`) e ir direto ao dossiê referenciado — nunca leitura sequencial da seção.
   Tíquete N/A-legado (campos "N/A — migrado", autorado dias/semanas atrás): classificar antes
   de qualquer delegação — (1) objetivo AFIRMA estado de código → 1-3 sondas baratas
   (Grep/Read/`git log`) verificam se a premissa ainda existe; já satisfeita → fechar inline
   com ponteiro ao commit; (2) objetivo é PERGUNTA de produto ("se X for desejado...") →
   `AskUserQuestion`, nunca delegar; (3) objetivo correto mas sem design definido → fase de
   escopamento própria (scouts + verificações), orçada fora do teto do executor. Se a varredura
   FIFO percorrer vários itens consecutivos sem achar um atômico, parar e apresentar o cluster
   inteiro (agrupado por perfil) para decisão em lote do dono — 1 round-trip, não N.

4. **Delegar execução** — agente `pantonic-executor`, com a tarefa atômica completa (objetivo,
   arquivos-alvo, contratos, testes, critério de pronto) copiada da seção do diário. Se a tarefa
   disser respeito a um domínio já coberto por um agente mais especializado (ex.: `clean-code`
   para refactor comportamento-preservado, `architect-auditor` para auditoria), delegar a ele em
   vez do executor genérico é aceitável — a escolha do agente certo é critério do orquestrador,
   não uma etapa mecânica. **Dieta do prompt:** carregar só o dossiê da tarefa — guardrails de arquitetura (regra de camadas, MVVM,
   ACL) já vivem nos "fatos estáveis" de `pantonic-executor.md` e não devem ser repetidos aqui;
   repetir paga o mesmo texto em todos os turnos do executor. **Levantamento de contexto antes do
   dossiê:** se entender o estado atual exigir ler mais de ~1-2 arquivos de código-fonte
   integrais (mismatch de shape, assinaturas, comportamento vigente), essa varredura vai para o
   agente `context-scout` (skill `context-prep`), não para leitura direta do modelo principal —
   o orquestrador monta o prompt de delegação a partir só do dossiê compacto devolvido pelo
   scout. Pular direto para leitura própria só quando a tarefa for trivial e o(s) arquivo(s) já
   forem conhecidos/pequenos.

   **Fonte do contexto, em ordem de preferência:** (1) dossiê pré-autorado (`sprint_plan.md`,
   card de plano) copiado verbatim — exceto números de aceite, ver gate abaixo; (2) precedente
   já pago no contexto (notas de tarefas-irmãs lidas no pickup) colado na delegação — custo
   marginal zero; (3) `context-scout` (skill `context-prep`): DESCOBERTA quando não há dossiê;
   DETALHE (1 pergunta fechada por spawn, paralelos) quando o pré-autorado referencia shapes de
   módulos implementados depois dele; (4) leitura direta só para ≤1-2 arquivos pequenos já
   conhecidos, ou trechos via Grep+offset. A mesma régua vale FORA deste fluxo: pedido direto
   de planejamento/análise cuja exploração estimada passe de ~15 tool uses usa `context-prep`.

   **Gate de delegação — rodar ANTES de despachar o executor:**
   1. Alvo único, sem cláusula "investigue X" (nem introduzida pelo orquestrador ao
      transcrever); bifurcação prevista resolvida por verificação barata, dossiê de scout ou
      decisão do dono. Exceção: bifurcação só decidível DENTRO da tarefa → delegar com os ramos
      enumerados + critério de parada explícito por ramo.
   2. Toda linha "lacuna/não confirmado" de scout descarregada antes, ou promovida a sub-tarefa.
      Nota herdada do plano tipo "aproveitar para Y (custo ~zero)" conta como alvo adicional.
   3. Números de aceite (piso, contagem de suíte, call sites) re-derivados por 1 comando barato
      agora — nunca copiados do plano (contagens envelhecem com a própria sprint). String
      destinada a assert é citação colada do output de verificação, nunca paráfrase — token
      negativo errado passa em silêncio.
   4. Afirmação negativa de escopo ("não toca contracts/services") com campo novo persistido
      exige 1 grep pelo gate de ESCRITA (`extra.*forbid`, validador) antes de ser afirmada.
      Rename/move de símbolo público: grep também em docs vivos (`docs/*.md`, excluindo
      históricos) e somar essa rede ao orçamento.
   5. Orçamento por volume: contar write-clusters (1 região editada = 1 cluster) — mecânico ~2
      tool uses, comportamental (muda contrato/fluxo; edit-run-debug: sync→async, timing de
      teste) ~4-6. Se "Arquivos-alvo" cruza ≥3 camadas da regra de dependência E ≥1 exige
      padrão sem precedente no código → decompor por camada. Conta >~40 → fixar teto numérico
      por ramo no dossiê ("PARE e reporte ao atingir N") ou dividir; nunca "aceitável estourar"
      sem número. **>8 write-clusters → dividir em sub-tarefas ANTES de delegar** (decisão do
      dono 2026-07-16: executores não param no teto — série UXROUND3 T3 56/35, T4 61/40,
      T5 112/50; o teto é alarme, a divisão é o controle).
   6. Tarefa-investigação (entregável = descoberta/mapeamento): itens 1-5 não se aplicam; fixar
      teto numérico por padrão e PRESCREVER o método de sondagem (artefato grande/linha única =
      sonda programática via scratchpad; Read estoura e Grep colapsa).
   7. Build/verify com artefato existente (`dist/`, `.exe`): dossiê declara "não deletar o
      artefato de saída" — deleção não autorizada é ação destrutiva, não limpeza.

5. **Handover** (skill `handover`) — o relatório final ao usuário segue o formato já exigido por
   `handover`, com destaque para:
   - **Tarefa executada** (ID + título) e status final.
   - **Iniciativa/plano de origem** (sprint, ou "tíquete avulso").
   - **Índice de conclusão do plano**: `<done>/<total>` tarefas daquele plano no diário.
   - Próxima tarefa sugerida pela mesma heurística/diretiva, **sem iniciá-la**.
   - Recomendação de `/clear`/`/compact` antes do próximo "execute o próximo passo".

   **Telemetria pós-notificação:** a linha `Consumo:` é do orquestrador. O dossiê instrui o
   executor a gravar o placeholder literal "Consumo: (preenchido pelo orquestrador via
   notificação)" — ou a não editar o diário (orquestrador escreve o bullet inteiro). Preencher
   = Grep pelo placeholder → Read offset/limit da região → Edit; NUNCA Edit apoiado em Read
   anterior à chamada `Agent` (o hiato de delegação invalida o rastreio). No pickup, 1 Grep
   pelo texto-promessa: match de sessão anterior = telemetria vencida → substituir por "NÃO
   MEDIDO — placeholder expirado", mantendo autoestimativa marcada como tal.
   **Queda de subagente:** notificação de falha não traz `<usage>` → registrar "PARCIAL —
   trecho pré-queda não medido". Antes de re-delegar a frio: `git status --short` + Read do
   artefato-alvo + `SendMessage` ao MESMO agentId com "o que falta"; só re-delegar se não
   retomar. Transcript/output de subagente é read-only — nunca apagar/mover/editar.

## Guardrails

- Nunca escolhe mais de uma tarefa por invocação.
- **Nunca escolhe tarefa de plano `superseded`** (terminal, fora do backlog) nem `blocked` cuja
  razão seja `validação postergada` enquanto suas implementações-dependência não estiverem todas
  `done`. Um plano `superseded` NÃO é retomado nem "continuado" — a rota foi substituída; se ele
  parece a próxima coisa a fazer, o erro está na leitura do estado, não no plano vivo.
- **Convergência de iniciativa (rebase antes de escolher):** se uma iniciativa tiver 2+ planos
  vivos (`backlog`/`in progress`/`blocked` não-postergado) disputando a mesma rota, NÃO desempatar
  por FIFO/momentum — isso significa que a reconciliação A/B/C (skill `diario-de-obras`, seção
  "Planos derivados") foi pulada. Parar, rebasear (marcar `superseded` os planos que a premissa
  atual contradiz, `blocked` os travados por fato novo, checar gaps já tratados sem registro) e só
  então escolher o **único** plano vivo — sempre o mais recente cuja premissa não foi contradita.
- Plano `blocked` por decisão owner-gated não resolvida (ex.: DP-1..DP-N pendentes) **não é
  delegável ao executor**: apresentar os DPs ao dono (`AskUserQuestion` ou resumo) e parar — nunca
  iniciar a implementação nem redescobrir o que o plano já responde.
- Se a heurística empatar entre itens do mesmo nível, desempate por ordem de entrada no índice
  (mais antigo primeiro).
- Se o diário estiver vazio (nenhum item `backlog`/`in progress`/`blocked`), reportar isso
  explicitamente ao usuário — não inventar trabalho nem reabrir item `done`/`cancelled`.
- Diretiva de priorização só muda por escrita explícita no diário (skill `diario-de-obras`,
  operação "registrar diretiva de priorização") — nunca inferida de uma conversa que não a
  persistiu.
- Higiene de busca (série de ~45 chamadas perdidas medida): Grep que precisa do TEXTO usa
  sempre `output_mode: content`; tarefa de sprint no diário é bullet dentro de `## SPRINT-*`
  (nunca heading `###` — Grep pelo ID literal); padrão de busca é colado do texto real, nunca
  suposto (aspas/pipes espúrios e ramo vazio de alternância casam tudo ou nada); `Grep.offset`
  conta MATCHES, não linhas de arquivo — seek posicional é `Read offset/limit`; âncora
  confirmada + especulativa vão juntas numa alternância na mesma chamada.
- Achado de processo recorrente (≥3×) e de risco zero (edição de 1 linha em doc/skill) não
  espera lote de tíquete acumulador: vira `AskUserQuestion` pontual ao dono na mesma rodada.
