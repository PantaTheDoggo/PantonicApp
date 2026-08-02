# Diário de Obras — PantonicApp (hub de governança Pantonic*)

**Diretiva de priorização:** Priorize a iniciativa `PANTONIC-V2` (consolidação do framework —
benchmarking → confronto → melhoria → documentação).

> Este diário é o kanban do backlog de **governança comum** dos projetos Pantonic*. Os planos
> completos vivem em `docs/plans/P-*.md`; aqui ficam o índice, o status e o ponteiro. Entrada de
> planos novos: `docs/plans/_INBOX.md` (append-only), drenado por quem abrir a skill
> `proximo-passo`.

## Índice

| ID | Título | Status | Âncora |
|---|---|---|---|
| SPRINT-PANTONICV2 | Consolidação do framework em V2 — 4 estágios encadeados | in progress | `## SPRINT-PANTONICV2` |
| P-0729-V2B | Estágio 1 — benchmarking de 21 frameworks públicos (T1..T9) | done | `docs/plans/P-0729-v2-benchmarking.md` |
| P-0729-V2C | Estágio 2 — confronto, diagnóstico e autoria do plano 3B (T1..T6) | done | `docs/plans/P-0729-v2-confronto.md` |
| P-0729-V2M | Estágio 3A — doutrina herdada do P-0722 (T1..T5 completos, 5/5) | done | `docs/plans/P-0729-v2-melhoria.md` |
| P-0729-V2K | Estágio 3B — mudanças adotadas do benchmarking (T1..T19, com `T12` partida em `T12a`/`T12b`; 13/20) | in progress | `docs/plans/P-0729-v2-melhoria-candidatos.md` |
| P-0729-V2D | Estágio 4 — README espelho, fechamento 2.0.0 e distribuição (T1..T5) | blocked | `docs/plans/P-0729-v2-documentacao.md` |
| P-0722 | Guardrails de doutrina anti-saga (G-DEADCODE, G-PLANFIDELITY, G-PREMISE, G-PLANREADY, G-EXECREADY) | superseded | mesclado em `P-0729-v2-melhoria.md` §1 |
| P-0721 | Governança single-source: PantonicApp como referência | done | `docs/plans/P-0721-governanca-single-source.md` |
| P-0725-3C | Governança em três camadas condicionais | superseded | substituído por `P-0725-governanca-hub-unico.md` |
| P-0725-HU | Hub único: PantonicApp canônico, PantonicVideo como prova | done | `docs/plans/P-0725-governanca-hub-unico.md` |
| TK-01 | Corrigir residência de `modelo-por-fase` em `GOVERNANCA.md` §3 e no bullet `V2M-T1` do `CHANGELOG.md` (ainda apontam `~/.claude/skills/`, superado por `DM-7`) | done *(absorvido pela `V2M-T3`)* | `docs/DIARIO_HISTORICO.md#tíquetes-avulsos--condensado-em-2026-08-01` |
| TK-02 | `.claude/sync-kit.ps1`: `Get-ExcludedKeys`/`Test-Excluded` quebram sem `kit-exclude.txt` presente (achado pré-existente, `V2K-T11`) | done | docs/DIARIO_HISTORICO.md#tíquetes-avulsos--2ª-condensação-2026-08-01 |

---

## SPRINT-PANTONICV2 — Consolidação do framework em V2

**Objetivo:** confrontar o framework PantonicApp com a prática pública registrada, corrigir o que
o confronto apontar, e entregar um `README.md` a partir do qual um humano decida sobre o framework
sem abrir nenhum outro arquivo — tudo sob controle de versão, fechando em `2.0.0`.

**Próxima tarefa da sprint:** `V2K-T13` — Compatibilidade por major entre kit e consumidor
(`C-14`) — **[Sonnet]** — ficha fechada em `docs/plans/P-0729-v2-melhoria-candidatos.md` §T13,
resumida no bloco "**Ficha da `V2K-T13`**" logo abaixo. O `C-09` fechou por inteiro em
2026-08-01 (`V2K-T12a` produtor + `V2K-T12b` coletor).

**Ficha da `V2K-T13`** (íntegra em `docs/plans/P-0729-v2-melhoria-candidatos.md` §T13):
Arquivos-alvo `.claude/skills/checar-versao-kit/SKILL.md` e `GOVERNANCA.md` §10 (uma linha).
Divergência de **MAJOR** entre kit e consumidor deixa de ser tratada como divergência comum:
três casos distinguidos na saída da skill — igual (silêncio) · MINOR/PATCH divergente
(reportar, como hoje) · MAJOR divergente (reportar como incompatível e parar). A regra do §10a
é preservada: o agente reporta, nunca atualiza. Verificação: no scratchpad, um
`.claude/kit/KIT_VERSION` sintético com MAJOR diferente produz a mensagem de incompatibilidade;
com MINOR diferente, a mensagem antiga; igual, silêncio.

**Condensado em 2026-08-01 (2ª rodada).** O gate aberto pela `V2K-T12b` foi resolvido pelo dono
antes desta tarefa: o contexto encerrado da sprint — ficha da `V2K-T12`, decisões já resolvidas,
histórico dos Estágios 1/2/3A e os bullets de fechamento de `V2K-T1..T12b` — está em
`docs/DIARIO_HISTORICO.md`. Diário ativo: 569 → 98 linhas; histórico: 516 → 1007 linhas.

**Origem:** pedido do dono, 2026-07-29. **Planejamento:** Opus, 2026-07-29 (4 planos registrados no
mesmo ato, com a cadeia de dependência declarada).

**Encadeamento:** os estágios são sequenciais. Só o Estágio 1 nasce `backlog`; os demais são
`blocked` por dependência do anterior e **não são escolhíveis** pela `proximo-passo` até o
predecessor fechar — assim a iniciativa mantém **um único plano vivo** por vez (skill
`diario-de-obras`, "Planos derivados", caso C). Exceção registrada em `P-0729-v2-melhoria` DM-4:
o Estágio 3A inteiro vem do `P-0722` (decisões fechadas em 2026-07-22) e pode ser antecipado se o
dono quiser paralelismo.

**Gate de publicação (decisão do dono, 2026-07-29):** nenhum plano desta iniciativa é publicado em
aberto. O Estágio 3B — as mudanças que só o benchmarking podia revelar — **nasceu fechado em
2026-07-29**, autorado pela `V2C-T6` (última tarefa do Estágio 2) a partir do `CANDIDATOS.md` já
ratificado, e só então entrou no inbox e neste índice: 19 tarefas, 14 candidatos cobertos, nenhuma
questão pendente. O ciclo do gate está fechado na prática antes de virar doutrina em `V2M-T1`
(G-PLANREADY item 5).

### Estágio 3B — `P-0729-v2-melhoria-candidatos` [in progress — 13/20 (Bloco A fechado, Bloco C em andamento; `T12` partida em `T12a`/`T12b` ⇒ 20 tarefas), nascido fechado em 2026-07-29 pela `V2C-T6`]

19 tarefas, cada uma com o `C-NN` de origem. Ordem normativa em `docs/plans/P-0729-v2-melhoria-candidatos.md`
§2 — **Bloco A** (`T1..T4`) antes do Estágio 3A; **Bloco C** (`T5..T19`) depois dele.

**Bloco A (`T1..T4`) e Bloco C até `T12b`: `done`, 13/20.** Os bullets de fechamento (resultado,
verificação, veredito e `Consumo:` de cada tarefa) estão em `docs/DIARIO_HISTORICO.md`, seção
"Estágio 3B: contexto encerrado e tarefas `T1..T12b`".

**Bloco C — em aberto:**
- `V2K-T13` — Compatibilidade por major kit × consumidor — [Sonnet] — backlog *(`C-14`; contíguo a `T11`/`T12` por DK-11)*
- `V2K-T14` — Doutrina do piso de regressão **comportamental** (§4.4) — [Opus] — backlog *(`C-11`a; nunca percentual)*
- `V2K-T15` — Receita executável de ratchet do piso — [Sonnet] — backlog *(`C-11`b)*
- `V2K-T16` — Decisão de residência item a item + ratificação do dono — [Opus + dono] — backlog *(`C-12`a; depende de `T4`)*
- `V2K-T17` — Mover o texto e corrigir os ponteiros — [Sonnet] — backlog *(`C-12`b; depende da ratificação em `T16`)*
- `V2K-T18` — Formato e arquivo da série de telemetria (`docs/telemetria.tsv`) — [Sonnet] — backlog *(`C-13`a)*
- `V2K-T19` — Escrita da série nos dois pontos de fechamento + bump `1.4.0` — [Sonnet] — backlog *(`C-13`b)*

### Estágio 4 — `P-0729-v2-documentacao` [blocked — depende do Estágio 3 inteiro done]

- `V2D-T1` — `docs/DOC_MAP.md` do hub — [Sonnet] — blocked
- `V2D-T2` — Redigir o `README.md` espelho (13 seções) — [Opus] — blocked
- `V2D-T3` — Guarda executável de drift do espelho — [Sonnet] — blocked
- `V2D-T4` — Fechar a versão `2.0.0` (CHANGELOG + tag) e **distribuir** — [Sonnet] — blocked *(acumula `P-0722` Fase 4)*
- `V2D-T5` — Teste de aceitação: 6 perguntas respondidas só pelo README — [dono] — blocked

**Notas de execução:** *(vazio — nenhuma tarefa iniciada)*
