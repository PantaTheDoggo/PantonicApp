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
| P-0729-V2B | Estágio 1 — benchmarking de 20 frameworks públicos (T1..T8) | backlog | `docs/plans/P-0729-v2-benchmarking.md` |
| P-0729-V2C | Estágio 2 — confronto, diagnóstico e autoria do plano 3B (T1..T6) | blocked | `docs/plans/P-0729-v2-confronto.md` |
| P-0729-V2M | Estágio 3A — doutrina herdada do P-0722 (T1..T5) | blocked | `docs/plans/P-0729-v2-melhoria.md` |
| P-0729-V2K | Estágio 3B — mudanças adotadas do benchmarking | por nascer | autorado fechado por `V2C-T6` |
| P-0729-V2D | Estágio 4 — README espelho, fechamento 2.0.0 e distribuição (T1..T5) | blocked | `docs/plans/P-0729-v2-documentacao.md` |
| P-0722 | Guardrails de doutrina anti-saga (G-DEADCODE, G-PLANFIDELITY, G-PREMISE, G-PLANREADY, G-EXECREADY) | superseded | mesclado em `P-0729-v2-melhoria.md` §1 |
| P-0721 | Governança single-source: PantonicApp como referência | done | `docs/plans/P-0721-governanca-single-source.md` |
| P-0725-3C | Governança em três camadas condicionais | superseded | substituído por `P-0725-governanca-hub-unico.md` |
| P-0725-HU | Hub único: PantonicApp canônico, PantonicVideo como prova | done | `docs/plans/P-0725-governanca-hub-unico.md` |

---

## SPRINT-PANTONICV2 — Consolidação do framework em V2

**Objetivo:** confrontar o framework PantonicApp com a prática pública registrada, corrigir o que
o confronto apontar, e entregar um `README.md` a partir do qual um humano decida sobre o framework
sem abrir nenhum outro arquivo — tudo sob controle de versão, fechando em `2.0.0`.

**Próxima tarefa da sprint:** `V2B-T3` (`docs/plans/P-0729-v2-benchmarking.md` §5).

**Origem:** pedido do dono, 2026-07-29. **Planejamento:** Opus, 2026-07-29 (4 planos registrados no
mesmo ato, com a cadeia de dependência declarada).

**Encadeamento:** os estágios são sequenciais. Só o Estágio 1 nasce `backlog`; os demais são
`blocked` por dependência do anterior e **não são escolhíveis** pela `proximo-passo` até o
predecessor fechar — assim a iniciativa mantém **um único plano vivo** por vez (skill
`diario-de-obras`, "Planos derivados", caso C). Exceção registrada em `P-0729-v2-melhoria` DM-4:
o Estágio 3A inteiro vem do `P-0722` (decisões fechadas em 2026-07-22) e pode ser antecipado se o
dono quiser paralelismo.

**Gate de publicação (decisão do dono, 2026-07-29):** nenhum plano desta iniciativa é publicado em
aberto. O Estágio 3B — as mudanças que só o benchmarking pode revelar — **ainda não existe, e é
correto que não exista**: ele é autorado já fechado por `V2C-T6`, a última tarefa do Estágio 2, e só
então entra no inbox e neste índice. A regra vira doutrina em `V2M-T1` (G-PLANREADY item 5).

### Estágio 1 — `P-0729-v2-benchmarking` [backlog]

- `V2B-T1` — Instituir o controle de versão do framework (`VERSION` + `KIT_VERSION` + `CHANGELOG`) — [Sonnet] — done
  - Resultado: `VERSION` e `.claude/KIT_VERSION` em `1.1.0` (paridade obrigatória); `CHANGELOG.md` criado na raiz; `GOVERNANCA.md` §10 ganhou parágrafo final com a regra de paridade e MAJOR/MINOR/PATCH; commit + tag anotada `kit-v1.1.0` (sem push).
  - Consumo: 13 tool uses, ~44k tokens, Sonnet, ~100s (medido no `<usage>` da notificação).
- `V2B-T2` — Agente `pantonic-benchmarker` + esquema D1..D16 — [Sonnet] — done
  - Resultado: agente `pantonic-benchmarker` (Haiku, sem Bash/Edit) e `docs/benchmark/_ESQUEMA.md` (D1..D16 + rodapé) criados; `.claude/README.md` atualizado; `VERSION`/`.claude/KIT_VERSION` em `1.2.0`; commit + tag `kit-v1.2.0` (sem push).
  - Consumo: (preenchido pelo orquestrador via notificação)
- `V2B-T3` — Curadoria e cache do corpus (25 candidatos → 20 confirmados) — [Sonnet] — backlog
- `V2B-T4` — Relatórios do lote 1 (repos 1-5) — [Haiku ×5] — backlog
- `V2B-T5` — Relatórios do lote 2 (repos 6-10) — [Haiku ×5] — backlog
- `V2B-T6` — Relatórios do lote 3 (repos 11-15) — [Haiku ×5] — backlog
- `V2B-T7` — Relatórios do lote 4 (repos 16-20) — [Haiku ×5] — backlog
- `V2B-T8` — Controle de qualidade e índice do corpus — [Sonnet] — backlog

### Estágio 2 — `P-0729-v2-confronto` [blocked — depende de `P-0729-v2-benchmarking` done]

- `V2C-T1` — Auto-retrato do PantonicApp no esquema do corpus (`BM-00`) — [Sonnet] — blocked
- `V2C-T2` — Matriz de cobertura dimensão × framework — [Sonnet] — blocked
- `V2C-T3` — Relatório consolidado de forças, fraquezas e dimensões novas — [Opus] — blocked
- `V2C-T4` — Backlog priorizado de candidatos (`C-NN`) — [Opus] — blocked
- `V2C-T5` — Ratificação do dono (decisão por candidato) — [dono] — blocked
- `V2C-T6` — Autorar `P-0729-v2-melhoria-candidatos.md` **já fechado** (Estágio 3B) — [Opus] — blocked

### Estágio 3A — `P-0729-v2-melhoria` [blocked — depende de `P-0729-v2-confronto` done; antecipável por DM-4]

- `V2M-T1` — Redigir a doutrina nova em `GOVERNANCA.md` §7 — 5 guardrails + **gate de publicação** (G-PLANREADY item 5) — [Opus] — blocked *(herdado de `P-0722` Fase 1)*
- `V2M-T2` — Skill global `modelo-por-fase` — [Sonnet] — blocked *(herdado de `P-0722` Fase 2)*
- `V2M-T3` — Promover G-PLANFIDELITY/G-EXECREADY ao CLAUDE.md global — [Sonnet] — blocked *(herdado de `P-0722` DP-G4)*
- `V2M-T4` — Contador sequencial de planos (`P-NNNN`) — [Sonnet] — blocked *(herdado de `P-0722` DP-G5)*
- `V2M-T5` — Check executável de código morto testado (G-DEADCODE) — [Sonnet] — blocked *(herdado de `P-0722` Fase 3)*

### Estágio 3B — `P-0729-v2-melhoria-candidatos` [por nascer — autorado fechado por `V2C-T6`]

Sem tarefas listadas **por desenho**, não por omissão: o plano não existe até o `CANDIDATOS.md` estar
ratificado. Não é backlog invisível — tem dono nomeado (`V2C-T6`) e critério de pronto.

### Estágio 4 — `P-0729-v2-documentacao` [blocked — depende do Estágio 3 inteiro done]

- `V2D-T1` — `docs/DOC_MAP.md` do hub — [Sonnet] — blocked
- `V2D-T2` — Redigir o `README.md` espelho (13 seções) — [Opus] — blocked
- `V2D-T3` — Guarda executável de drift do espelho — [Sonnet] — blocked
- `V2D-T4` — Fechar a versão `2.0.0` (CHANGELOG + tag) e **distribuir** — [Sonnet] — blocked *(acumula `P-0722` Fase 4)*
- `V2D-T5` — Teste de aceitação: 6 perguntas respondidas só pelo README — [dono] — blocked

**Notas de execução:** *(vazio — nenhuma tarefa iniciada)*
