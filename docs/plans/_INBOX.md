# Inbox de planos — PantonicApp (hub de governança) — append-only

Cada linha aponta para um `docs/plans/P-NNNN-<slug>.md`, com `NNNN` um contador global monotônico
(nunca reutilizado, zero-padded) e a data de origem registrada como campo de cabeçalho do próprio
plano — não no nome do arquivo. **Próximo id de plano: P-0756.** Os planos já existentes
`P-0721`..`P-0729` mantêm o nome atual e não são renomeados (renomear quebraria ponteiros
cruzados de planos fechados sem ganho — DP-G5). Uma vez promovida ao índice/heading do
`docs/DIARIO_DE_OBRAS.md`, a linha é marcada como drenada e migra para
`docs/plans/_INBOX_HISTORICO.md` — nunca é apagada. Este arquivo carrega só o que ainda não foi
drenado; o pickup lê apenas ele. O marcador e o texto integral das linhas já drenadas, com as
correções que se referem a elas, vivem no histórico.

