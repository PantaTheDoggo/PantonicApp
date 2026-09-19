# DOC_MAP — PantonicApp

> Nunca Read integral em doc > 500 linhas. Sempre: DOC_MAP → Grep pela âncora → Read com
> `offset`/`limit` na faixa encontrada. Âncoras são cabeçalhos/marcadores, nunca números de
> linha — eles desatualizam.

Docs abaixo de 500 linhas (`docs/DIARIO_DE_OBRAS.md`, `GOVERNANCA.md` na raiz,
`docs/RESIDENCIA_DOUTRINA.md`, `docs/benchmark/CANDIDATOS.md`,
`docs/plans/_INBOX.md`, demais `docs/plans/*.md` e `docs/benchmark/BM-*.md`) não precisam de
entrada — Read direto.

Os tamanhos abaixo são referência de ordem de grandeza medida em **2026-08-05**, não âncora: o
que localiza a seção é sempre o padrão de Grep.

## docs/DIARIO_HISTORICO.md (~970 linhas)
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

## docs/benchmark/RELATORIO_CONSOLIDADO.md (~636 linhas)
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

## docs/plans/P-0721-governanca-single-source.md (~524 linhas)
**Propósito:** plano fechado (`done`) que estabeleceu PantonicApp como repositório de referência
single-source da governança comum Pantonic*.
**Quando consultar:** para entender decisões `DP-*` herdadas (arquitetura alvo, mecanismo D1) que
planos posteriores (`P-0725-*`) ainda referenciam.
**Seções:**
- `## 2. Decisões (owner-gated)` — `DP-1..DP-8`
- `## 4. Tarefas (fases)` — `Fase 0..6`, todas `DONE`
- `## Achados da execução` — uma `###` por fase concluída, com data
**Acesso:** `Grep pattern:"^### Fase 3 " path:docs/plans/P-0721-governanca-single-source.md -n`.

## docs/plans/P-0725-governanca-hub-unico.md (~669 linhas)
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

## docs/plans/P-0729-v2-melhoria-candidatos.md (~526 linhas) — Estágio 3B, `done` (20/20)
**Propósito:** plano fechado do Estágio 3B — mudanças adotadas do benchmarking, dossiê de cada
tarefa (`T1..T19`, com `T12` partida em `T12a`/`T12b`) mapeada a um `C-NN` ratificado.
**Quando consultar:** para recuperar a decisão de origem (`C-NN`) de um artefato do kit
introduzido pelo Bloco A/C, ou o dossiê de uma tarefa já executada.
**Seções:**
- `## 2. Ordem de execução e entrelaçamento com o Estágio 3A`
- `## 3. Tarefas` — `### T1..T19`, uma por candidato `C-NN`
- `## 6. Decisões (fechadas no planejamento)`
**Acesso:** `Grep pattern:"^### T5 " path:docs/plans/P-0729-v2-melhoria-candidatos.md -n`
(trocar `T5` pela tarefa desejada).

## ARQUITETURA_PANTONICA.md (raiz, ~513 linhas)
**Propósito:** doutrina de clean architecture + DDD do framework — modelo de camadas, portas de
runtime do core, estrutura de pastas canônica, plugins/manifests, residência do caso de uso e
contenção de falhas.
**Quando consultar:** para o contrato de uma porta do core, a doutrina de residência/forma do
caso de uso de um plugin, ou o grau de aderência medido da implementação de referência.
**Seções:**
- `## 1. Golden rules` — inclui o grau de aderência medido (domínio, infracore, plugins, camada
  de aplicação)
- `## 2. Modelo de camadas` / `## 3. Estrutura de pastas canônica`
- `## 4. Infracore — as dez portas de runtime do core`
- `## 9. Plugins e manifests` — doutrina POC-first, manifest, validação no load
- `### 9.1 O caso de uso dentro do plugin` — residência (`plugins/<nome>/use_case.py`), campo
  `use_case` do manifest, regra de exatamente um caso de uso por plugin
- `## 10. Operações de OS e IN/OUT` / `## 11. Contenção de falhas [REPLICAR]`
**Acesso:** `Grep pattern:"^### 9\.1" path:ARQUITETURA_PANTONICA.md -n` (trocar a âncora por
qualquer heading `##`/`###` da lista acima).

## docs/CUSTO_DO_PICKUP.md (~431 linhas)
**Propósito:** medida por fonte do que uma retomada de backlog ingere — orçamento em chars e
tokens, veredito das hipóteses, rota candidata por fonte, orçamento-alvo e anatomia medida de
uma janela de orquestração real.
**Quando consultar:** ao decidir ou implementar qualquer mudança no fluxo de pickup (skills
`scrum-master`/`passagem-de-bastao`/`diario-de-obras`, diário, inboxes), para partir do número
medido em vez de remedir; e para o valor de referência contra o qual uma correção se afere.
**Seções:**
- `## 1 Pickup típico medido` — definição operacional e `HEAD` da medida
- `## 2 Orçamento por fonte` — tabela ranqueada por chars ingeridos + cinco recortes internos
- `## 3 Orçamento por passo do roteiro` — uma linha por passo, com o número único do pickup
- `## 4 Hipóteses H1..H5` — veredito e número de cada uma
- `## 5 Rota candidata por fonte` — rota do conjunto fechado, perda e ordem de grandeza
- `## 6 Orçamento-alvo proposto` — alvo, folga de execução e redução exigida
- `## 7 Anatomia de uma janela de orquestração` — 3 janelas `AUT-T5b`/2026-08-22 medidas por
  `sonda_janela.py`: ocupação do 1º `usage`, decomposição fixo × variável, turno de cruzamento
  de 100k tokens e o que a leva lá
- `## 8 A série: custo por papel e custo do controle` — decomposição do consumo por papel agêntico
- `## 9 Causas raízes e veredito do dono (2026-08-23)` — as causas classificadas e a rota decidida
- `## 10 Aferição (2026-08-24)` — antes × depois medido das correções, com veredito dos critérios
- `## 11 Composição do 1º usage (2026-08-24)` — decomposição visível × opaco (`TK-51`): dispersão
  da baseline estendida, tabela por janela canônica e regressão `usage_1 ~ chars_preâmbulo` por papel
- `## 12 Onde e quando o degrau do 1º usage acontece (2026-08-24)` — discriminação por tempo/tipo
  de janela/projeto do degrau (`TK-53a`): série diária, `depois` linha a linha, papel de subagente
  e projeto antes × depois, veredito por eixo e a janela temporal do degrau
- `## 13 Extrato do custo de abertura de uma janela principal (2026-09-18)` — uma linha por
  fonte carregada, com chars medidos, estrato E1/E2/E3, regime e a classificacao que o dono ratifica
**Acesso:** `Grep pattern:"^## 5 " path:docs/CUSTO_DO_PICKUP.md -n` (trocar `5` pela seção
desejada).

## docs/plans/P-0737-loop-autonomo.md (~586 linhas)
**Propósito:** plano vivo único da iniciativa `EXECUCAO-AUTONOMA` — rebase do `P-0734` por
classificação (B), poda nominal dos 25 tíquetes vivos e as dez tarefas `AUT-T1..T10` que fecham a
consolidação.
**Quando consultar:** para o destino de uma tarefa herdada do `P-0734`, o critério e a disposição
de um tíquete podado/absorvido/encaminhado, ou o dossiê de uma `AUT-T<n>`.
**Seções:**
- `## 2. Decisões`
- `## 4. Rebase do P-0734-execucao-autonoma — classificação (B)` — mapa das 9 tarefas herdadas
- `## 5. Poda de tíquetes — os 25 vivos, nominalmente` — (a) podados, (b) absorvidos, (c)
  encaminhados, (d) preservados
- `## 6. Tarefas` — `### AUT-T1..AUT-T10`
- `## 8. Saída da AUT-T10 — as três recomendações de plano`
- `## 11. Riscos`
**Acesso:** `Grep pattern:"^### AUT-T5 " path:docs/plans/P-0737-loop-autonomo.md -n` (trocar
`AUT-T5` pela tarefa desejada).

## docs/consultant-spec.md (~339 linhas)
**Propósito:** especificação da figura **provisória** do consultor de plano (`pantonic-consultant`)
como ela se comportou em três instâncias medidas — gatilho, domínio de decisão, fronteira com o
`pantonic-planner`, instrumento, custo e teto, encerramento, fim de vida e sucessão, e estatística
do próprio acionamento. **Não é doutrina** e não se cita como fonte normativa.
**Quando consultar:** antes de planejar, acionar ou redesenhar o consultor de plano; para o número
medido do custo do papel em vez de remedi-lo; e para o panorama dos pontos inconclusivos que serve
de insumo à especificação de robustez da figura.
**Seções:**
- `## 1. A figura, em uma página` — o mecanismo da permanência + tabela das três instâncias medidas
- `## 2. (a) Gatilho — o que aciona e o que não aciona` — as três classes de gatilho e os dois
  tetos de saída (teste de saturação; capacidade × término)
- `## 3. (b) Domínio de decisão — o que ela fecha e o que sobe` — critério de estratégico
- `## 4. (c) Fronteira com o planejador — e o veredito sobre autoria de card`
- `## 5. (d) Instrumento — por que a figura nasce com execução de comando` — os quatro modos de uso
- `## 6. (e) Custo e teto — a série, e quando não acionar` — 68,5% e 63%, e a baseline por módulo
- `## 7. (f) Encerramento — decisão de janela × poluição`
- `## 8. (g) Fim de vida por limite, e a sucessão` — handover, seus três itens, e a forma ad-hoc
- `## 9. (h) Estatística do próprio acionamento` — o que se coleta, onde mora, quem lê + tabela do
  panorama dos dez acionamentos
- `## 10. O que esta especificação não fecha` — as cinco matérias sem rota decidida
**Acesso:** `Grep pattern:"^## 6\." path:docs/consultant-spec.md -n` (trocar `6` pela seção
desejada; as perguntas (a)..(h) mapeiam nas seções 2..9).
