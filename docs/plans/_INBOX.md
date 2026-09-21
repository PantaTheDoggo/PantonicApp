# Inbox de planos — PantonicApp (hub de governança) — append-only

Cada linha aponta para um `docs/plans/P-NNNN-<slug>.md`, com `NNNN` um contador global monotônico
(nunca reutilizado, zero-padded) e a data de origem registrada como campo de cabeçalho do próprio
plano — não no nome do arquivo. **Próximo id de plano: P-0746.** Os planos já existentes
`P-0721`..`P-0729` mantêm o nome atual e não são renomeados (renomear quebraria ponteiros
cruzados de planos fechados sem ganho — DP-G5). Uma vez promovida ao índice/heading do
`docs/DIARIO_DE_OBRAS.md`, a linha é marcada como drenada e migra para
`docs/plans/_INBOX_HISTORICO.md` — nunca é apagada. Este arquivo carrega só o que ainda não foi
drenado; o pickup lê apenas ele. O marcador e o texto integral das linhas já drenadas, com as
correções que se referem a elas, vivem no histórico.

- `2026-09-21` — `P-0745` — `docs/plans/P-0745-planejador-modelo-operacao.md` — **O planejador diante do modelo: uma operação, um card.** Melhoramento do agente de planejamento com o modelo de domínio e o modelador estabelecidos (`P-0743` `done`): a unidade de trabalho passa a ser a materialização de uma operação do modelo (um card por operação), o percentual de ocupação e a tabela de tetos saem do dimensionamento de tarefa, o protocolo do planejador ganha a SAÍDA 3 (esqueleto + dossiê de autoria antes dos cards) e o gate do modelador devolve `V1`/`V3` como lastro do planejador. Sucede o `P-0744` (classe B — `superseded`), herdando as três tarefas dele. 7 tarefas `PLN-T1`..`PLN-T7`; Marco 1 = go do dono sobre a §1. Branch `plan/planner-modelo-escopo`. **Checagem de versão do kit:** modo hub — congelada em `0.0.0`, nada a comparar. **Próximo id após este: `P-0746`.**
