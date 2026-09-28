# Evidência de revisão — DIARIO_DE_OBRAS TK-90a

## Diff (`git diff --stat`)
```
.claude/README.md                                  |    8 +-
 .claude/agents/pantonic-consultant.md              |   43 +-
 .claude/agents/pantonic-executor.md                |   11 +-
 .claude/agents/pantonic-fora-da-caixa.md           |    2 +-
 .claude/agents/pantonic-model-designer.md          |   81 +-
 .claude/agents/pantonic-planner.md                 |  217 +-
 .claude/agents/pantonic-reviewer.md                |   15 +-
 .claude/checks/kit_check.ps1                       |   39 +-
 .claude/global/CLAUDE.md                           |   67 +-
 .../hooks/modelo_por_fase_userpromptsubmit.py      |   13 +-
 .claude/projecoes.json                             |   47 +
 .claude/skills/bootstrap-pantonic/SKILL.md         |    6 +-
 .claude/skills/diario-de-obras/SKILL.md            |  156 +-
 .claude/skills/entrega-de-encerramento/SKILL.md    |    2 +-
 .claude/skills/modelo-por-fase/SKILL.md            |   26 +-
 .claude/skills/passagem-de-bastao/SKILL.md         |   54 +-
 .claude/skills/redacao-doc/SKILL.md                |    3 +-
 .claude/skills/scrum-master/SKILL.md               |  223 +-
 .claude/tools/backlog.py                           |  584 ++-
 .claude/tools/backlog_hook.py                      |   14 +-
 .claude/tools/card_check.py                        |  403 ++-
 .claude/tools/modelo.py                            |   39 +-
 .claude/tools/rdo.py                               |  322 +-
 .claude/tools/rdo_template.md                      |   12 +-
 .claude/tools/review_evidence.py                   |  170 +-
 .claude/tools/telemetria_hook.py                   |   15 +-
 GOVERNANCA.md                                      |  400 ++-
 README.md                                          |  196 +-
 docs/CUSTO_DO_PICKUP.md                            |  171 +
 docs/DIARIO_DE_OBRAS.md                            | 3759 +++++++++++++++++++-
 docs/DIARIO_HISTORICO.md                           |  154 +
 docs/DOC_MAP.md                                    |  115 +-
 docs/RDO/INDEX.md                                  |  129 +
 docs/RESIDENCIA_DOUTRINA.md                        |    4 +-
 docs/RUBRICA_DE_REVISAO.md                         |   27 +-
 docs/consultant-spec.md                            |   75 +-
 docs/plans/P-0741-modelo-conceitual.md             |    8 +-
 docs/plans/P-0745-planejador-modelo-operacao.md    | 1584 ++++++++-
 docs/plans/_INBOX.md                               |    3 +-
 docs/plans/_INBOX_HISTORICO.md                     |    9 +
 docs/telemetria.tsv                                |  393 ++
 .../backlog/vermelho/docs/DIARIO_DE_OBRAS.md       |    3 +
 tests/fixtures/modelo/fluxo-concluido.md           |   12 +-
 tests/fixtures/modelo/fluxo-pendente.md            |   20 +-
 tests/fixtures/modelo/fluxo-valido.md              |   12 +-
 tests/fixtures/modelo/plano-invalido-2.md          |   10 +-
 tests/fixtures/modelo/plano-invalido.md            |   12 +-
 tests/fixtures/modelo/plano-sem-cabecalho.md       |    8 +-
 tests/fixtures/modelo/plano-sem-estado.md          |    8 +-
 tests/test_backlog.py                              |  819 +++++
 tests/test_card_check.py                           |  208 ++
 tests/test_materializar.py                         |    2 +-
 tests/test_modelo.py                               |  143 +-
 tests/test_rdo.py                                  |  411 ++-
 tests/test_review_evidence.py                      |  286 +-
 tests/test_telemetria_hook.py                      |   35 +
 56 files changed, 10495 insertions(+), 1093 deletions(-)
```

## Arquivos tocados
- `docs/DIARIO_DE_OBRAS.md` — atribuição: da entrega; estado git: ` M`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-90a-medida.json` — atribuição: alheio; estado git: `??`
- `docs/plans/_INBOX_HISTORICO.md` — atribuição: da entrega; estado git: ` M`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `d69f95f1ad23893385ffc83b6bc75481b007ac3e`
- Arquivos-alvo declarados: `docs/plans/_INBOX.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/_INBOX_HISTORICO.md`
- Literais não reconhecidos como caminho (3): `Fila corrente`, `drain`, `drain`
- Arquivos tocados: `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-90a-medida.json`, `docs/plans/_INBOX_HISTORICO.md`, `docs/telemetria.tsv`
- Atribuídos a outra tarefa do mesmo plano: `docs/telemetria.tsv` → `TK-88b`
- Registro da orquestração (não atribuível a tarefa): `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-90a-medida.json`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `docs/plans/_INBOX.md`
```
(sem alteração desde `d69f95f1ad23893385ffc83b6bc75481b007ac3e`)
```

### `docs/DIARIO_DE_OBRAS.md`
```
diff --git a/docs/DIARIO_DE_OBRAS.md b/docs/DIARIO_DE_OBRAS.md
index c426b50..7426aae 100644
--- a/docs/DIARIO_DE_OBRAS.md
+++ b/docs/DIARIO_DE_OBRAS.md
@@ -65,12 +65,13 @@ estão triados, todos com `**Rota:**` explícita.
    entrega e toda revisão exige aviso à mão mais reconciliação por hunk e mtime.
 
 <!-- fila:gerada -->
-**Fila corrente:** `TK-90` — O `P-0742` está fora do índice do diário, `blocked` com a condição já satisfeita (`docs/DIARIO_DE_OBRAS.md:6066-6125`) · fila: — · ready 13 · blocked 0 · in-progress 1
+**Fila corrente:** `P-0752` — Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção (`docs/plans/P-0752-fato-no-ponto-de-uso.md:1-785`) · fila: — · ready 13 · blocked 0 · in-progress 0
 - `TK-85` (`ready`, 0/1): próxima —
 - `TK-90` (`ready`, 0/2): próxima —
 - `TK-92` (`ready`, 0/1): próxima `TK-92a`
 - `TK-93` (`ready`, 0/1): próxima —
 - `P-0752` (`ready`, 15/17): próxima `FPU-T7`
+- `P-0742` (`blocked`, 0/8): próxima —
 <!-- /fila:gerada -->
 
 > **⏹ Os quatro blocos de diretiva abaixo são HISTÓRICO — o `P-0743` fechou `done` 18/18 e foi
@@ -304,6 +305,7 @@ da resposta.
 | P-0750-CAH | Comunicação agente↔humano: a mensagem ao dono se entende sozinha | done 6/6 | docs/plans/P-0750-comunicacao-agente-humano.md |
 | P-0751-EBK | Esgotar o backlog antes da publicação do kit | done 16/16 | docs/plans/P-0751-esgotar-backlog.md |
 | P-0752-FPU | Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção | ready 15/17 | docs/plans/P-0752-fato-no-ponto-de-uso.md |
+| P-0742-LF | O loop sai do LLM | blocked | docs/plans/P-0742-loop-fora-do-llm.md |
 
 ---
 
@@ -6075,7 +6077,7 @@ card: `TK-55`, `TK-67`, `TK-70`, `TK-72`, `TK-73` e `TK-81`; o `TK-71` fechou po
 
 ### TK-90a — O `P-0742` entra no índice do diário como `blocked` [Sonnet · esforço low · classe mecanica]
 
-- **Status:** `in-progress` · 2026-09-26
+- **Status:** `review` · 2026-09-26
 - **Objetivo:** o índice de `docs/DIARIO_DE_OBRAS.md` ganha a linha do `P-0742`, com o status do cabeçalho do plano, pelo caminho canônico do inbox, sem mexer no contador de id de plano.
 - **Arquivos-alvo:**
   - `docs/plans/_INBOX.md`

```

### `docs/plans/_INBOX_HISTORICO.md`
```
diff --git a/docs/plans/_INBOX_HISTORICO.md b/docs/plans/_INBOX_HISTORICO.md
index 296a257..585fe7d 100644
--- a/docs/plans/_INBOX_HISTORICO.md
+++ b/docs/plans/_INBOX_HISTORICO.md
@@ -302,3 +302,4 @@ vivo, se e quando o pickup precisar aliviá-lo de novo. O pickup do backlog lê
 - [drenado 2026-09-25] `2026-09-25` — `P-0750` — `docs/plans/P-0750-comunicacao-agente-humano.md` — **Comunicação agente↔humano: a mensagem ao dono se entende sozinha.** 5 tarefas `CAH-T1`..`CAH-T5`; nasce `ready` no Marco 1 (aceite do dono na sessão de planejamento); absorve o `TK-38`; `CAH-T1` espera `SAN-T5` do `P-0749`.
 - [drenado 2026-09-25] 2026-09-25 · `docs/plans/P-0751-esgotar-backlog.md` · Esgotar o backlog antes da publicação do kit — os 14 cards de tíquete `ready` num único loop (pedido e modelo ditados pelo dono, 2026-09-25).
 - [drenado 2026-09-26] 2026-09-26 · `docs/plans/P-0752-fato-no-ponto-de-uso.md` · Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção — 11 tarefas `FPU-T1`..`FPU-T10`; nasce `ready` (pedido e ordem do dono, 2026-09-26).
+- [drenado 2026-09-26] 2026-09-19 · `docs/plans/P-0742-loop-fora-do-llm.md` · O loop sai do LLM — registro tardio no índice (`TK-90a`).

```

## Medida do executor
- Arquivo: docs\RDO\evidencia\DIARIO_DE_OBRAS-TK-90a-medida.json; mundo: depois; gerado em: 2026-09-27T02:17:09+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;print(sum(1 for l in Path('docs/DIARIO_DE_OBRAS.md').read_text(encoding='utf-8').splitlines() if l.startswith('\| P-0742-')))"` | 0 | true |
| 2 | `python .claude/tools/backlog.py check` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
