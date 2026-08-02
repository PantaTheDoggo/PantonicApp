# DOC_MAP — PantonicApp

> Nunca Read integral em doc > 500 linhas. Sempre: DOC_MAP → Grep pela âncora → Read com
> `offset`/`limit` na faixa encontrada. Âncoras são cabeçalhos/marcadores, nunca números de
> linha — eles desatualizam.

Docs abaixo de 500 linhas (`docs/DIARIO_DE_OBRAS.md`, `docs/GOVERNANCA.md`,
`docs/plans/_INBOX.md`, `docs/plans/P-0729-v2-*.md` restantes, demais `docs/plans/*.md` e
`docs/benchmark/BM-*.md`) não precisam de entrada — Read direto.

## docs/DIARIO_HISTORICO.md (1007 linhas)
**Propósito:** arquivo append-only de seções condensadas do diário de obras ativo (itens
`done`/`cancelled`/`superseded` movidos para fora do kanban vigente).
**Quando consultar:** para reconstituir o histórico detalhado de uma tarefa já fechada (ex.:
consumo, desvios, veredito) cujo índice no `DIARIO_DE_OBRAS.md` aponta para cá.
**Seções:**
- `## Tíquetes avulsos — condensado em 2026-08-01` — `TK-01` (residência de `modelo-por-fase`)
- `## SPRINT-PANTONICV2 — Estágios 1, 2 e 3A (concluídos, condensado em 2026-08-01)`
  - `### Estágio 1 — P-0729-v2-benchmarking` — `V2B-T1..T9`, benchmarking de 21 frameworks
  - `### Estágio 2 — P-0729-v2-confronto` — `V2C-T1..T6`, confronto e diagnóstico
  - `### Estágio 3A — P-0729-v2-melhoria` — `V2M-T1..T5`, doutrina herdada do `P-0722`
- `## Tíquetes avulsos — 2ª condensação (2026-08-01)` — `TK-02` (achatamento de
  `Get-ExcludedKeys` em `.claude/sync-kit.ps1`)
- `## SPRINT-PANTONICV2 — Estágio 3B: contexto encerrado e tarefas T1..T12b (condensado em
  2026-08-01)` — preâmbulo encerrado da sprint (ficha da `V2K-T12`, decisões resolvidas,
  narrativa dos Estágios 1/2/3A) + bullets de fechamento de `V2K-T1..T12b`
  - `### Contexto encerrado do preâmbulo de ## SPRINT-PANTONICV2`
  - `### Tarefas V2K-T1..T12b (done) — bullets de fechamento`
**Acesso:** `Grep pattern:"^### Estágio 1" path:docs/DIARIO_HISTORICO.md -n` (ou 2/3A; ou
`^- \`TK-01\`` / `^- \`TK-02\`` para os tíquetes; ou `^- \`V2K-T9\`` para uma tarefa do
Estágio 3B).

## docs/benchmark/RELATORIO_CONSOLIDADO.md (808 linhas)
**Propósito:** confronto dimensão-a-dimensão (D1..D16 + D17..D22 propostas) do framework
PantonicApp contra os 21 repositórios públicos do corpus de benchmarking.
**Quando consultar:** ao decidir se um candidato de melhoria (`C-NN` do Estágio 3B) é
`MANTER`/`ADAPTAR`/`ADOTAR`/`REJEITAR`, ou para justificar uma dimensão específica.
**Seções:**
- `## 1. Veredito em uma página` — à frente / atrás / prioridade única
- `## 2. Dimensão por dimensão (D1..D16)` — uma `###` por dimensão, veredito no título
- `## 3. Dimensões novas propostas (D17+)` — `D17..D22`
- `## 4. Descartes justificados`
- `## 5. Vieses do corpus`
**Acesso:** `Grep pattern:"^### D7 " path:docs/benchmark/RELATORIO_CONSOLIDADO.md -n` (trocar
`D7` pela dimensão desejada).

## docs/plans/P-0721-governanca-single-source.md (619 linhas)
**Propósito:** plano fechado (`done`) que estabeleceu PantonicApp como repositório de referência
single-source da governança comum Pantonic*.
**Quando consultar:** para entender decisões `DP-*` herdadas (arquitetura alvo, mecanismo D1) que
planos posteriores (`P-0725-*`) ainda referenciam.
**Seções:**
- `## 2. Decisões (owner-gated)` — `DP-1..DP-8`
- `## 4. Tarefas (fases)` — `Fase 0..6`, todas `DONE`
- `## Achados da execução` — uma `###` por fase concluída, com data
**Acesso:** `Grep pattern:"^### Fase 3 " path:docs/plans/P-0721-governanca-single-source.md -n`.

## docs/plans/P-0725-governanca-hub-unico.md (834 linhas)
**Propósito:** plano fechado (`done`) que substituiu o `P-0725-3C` — hub único de governança com
PantonicApp canônico e PantonicVideo como prova de aceitação, incl. `sync-kit.ps1` e
`KIT_VERSION`.
**Quando consultar:** para entender o mecanismo de versionamento/anti-drift do kit ou histórico
de bugs do `sync-kit.ps1`/`KIT_VERSION` já resolvidos.
**Seções:**
- `## 3. Regra nova de governança — versionamento e atualização sob comando`
- `## 4. Fases` — `Fase 1..5`, todas `done`
- `## Notas de execução` / `## Achados da execução` — uma `###` por fase/achado, com data
**Acesso:** `Grep pattern:"^### Fase 3b " path:docs/plans/P-0725-governanca-hub-unico.md -n`.

## docs/plans/P-0729-v2-melhoria-candidatos.md (532 linhas) — Estágio 3B, `in progress`
**Propósito:** plano vivo do Bloco C (`V2K-T5..T19`) — mudanças adotadas do benchmarking,
dossiê de cada tarefa (`T1..T19`) mapeada a um `C-NN` ratificado.
**Quando consultar:** ao pegar a próxima tarefa do Bloco C (`proximo-passo`) ou verificar
dependência entre candidatos.
**Seções:**
- `## 2. Ordem de execução e entrelaçamento com o Estágio 3A`
- `## 3. Tarefas` — `### T1..T19`, uma por candidato `C-NN`
- `## 6. Decisões (fechadas no planejamento)`
**Acesso:** `Grep pattern:"^### T5 " path:docs/plans/P-0729-v2-melhoria-candidatos.md -n`
(trocar `T5` pela tarefa desejada).
