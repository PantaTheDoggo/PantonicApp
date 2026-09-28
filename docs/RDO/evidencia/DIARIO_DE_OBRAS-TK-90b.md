# Evidência de revisão — DIARIO_DE_OBRAS TK-90b

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
 docs/DIARIO_DE_OBRAS.md                            | 3766 +++++++++++++++++++-
 docs/DIARIO_HISTORICO.md                           |  154 +
 docs/DOC_MAP.md                                    |  115 +-
 docs/RDO/INDEX.md                                  |  130 +
 docs/RESIDENCIA_DOUTRINA.md                        |    4 +-
 docs/RUBRICA_DE_REVISAO.md                         |   27 +-
 docs/consultant-spec.md                            |   75 +-
 docs/plans/P-0741-modelo-conceitual.md             |    8 +-
 docs/plans/P-0742-loop-fora-do-llm.md              |  976 ++++-
 docs/plans/P-0745-planejador-modelo-operacao.md    | 1584 +++++++-
 docs/plans/_INBOX.md                               |    3 +-
 docs/plans/_INBOX_HISTORICO.md                     |    9 +
 docs/telemetria.tsv                                |  396 ++
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
 57 files changed, 11303 insertions(+), 1272 deletions(-)
```

## Arquivos tocados
- `docs/DIARIO_DE_OBRAS.md` — atribuição: da entrega; estado git: ` M`
- `docs/plans/P-0742-loop-fora-do-llm.md` — atribuição: da entrega; estado git: ` M`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `38a9bd26b37b6382eccb476bab2a609626a954a4`
- Arquivos-alvo declarados: `docs/plans/P-0742-loop-fora-do-llm.md`, `docs/DIARIO_DE_OBRAS.md`
- Literais não reconhecidos como caminho (5): `LF-T*`, `## Achados da execução`, `RP-1`, `P-0742`, `backlog.py status`
- Arquivos tocados: `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0742-loop-fora-do-llm.md`, `docs/telemetria.tsv`
- Atribuídos a outra tarefa do mesmo plano: `docs/telemetria.tsv` → `TK-88b`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `docs/plans/P-0742-loop-fora-do-llm.md`
```
diff --git a/docs/plans/P-0742-loop-fora-do-llm.md b/docs/plans/P-0742-loop-fora-do-llm.md
index 875072a..841e338 100644
--- a/docs/plans/P-0742-loop-fora-do-llm.md
+++ b/docs/plans/P-0742-loop-fora-do-llm.md
@@ -1,202 +1,820 @@
 # P-0742 — O loop sai do LLM
 
-**Data:** 2026-09-19 · **Origem:** decisão de rota do dono, 2026-09-19, sobre a posição L8 de
-`docs/plans/_VIABILIDADE-agente-leitor.md` §7.4 · **Status:** `blocked` · 2026-09-19 · depende de
-`P-0739` `done`: o driver consome os verbos de `backlog.py` (`next`, `start`, `status`, `show`) que
-o `P-0739` está migrando; retomar quando o índice do diário marcar `P-0739` `done` ·
-**Prefixo das tarefas no diário:** `LF-T<n>` · **Prefixo das decisões:** `DLF-<n>` ·
-**Checagem de versão do kit:** modo hub — congelada em `0.0.0` (`GOVERNANCA.md` §10), nada a
-comparar.
-**Ordem de execução:** LF-T1 → LF-T2 → LF-T3 → LF-T4 → LF-T5 → LF-T6 → LF-T7 → LF-T8.
-**Modelo de planejamento:** Fable 5.1 (sessão do dono de 2026-09-19).
+**Data:** 2026-09-19 · **Origem:** decisão de rota do dono, 2026-09-19, sobre a posição L8 de `docs/plans/_VIABILIDADE-agente-leitor.md` §7.4; retomado pela decisão do dono *"Retomar"* (2026-09-26, `TK-90b`) · **Status:** `ready` · 2026-09-26 · rodada de replanejamento `RP-1` fechada (`TK-90b`): a seção do modelo, versão 1, e os cards reescritos um por operação, na forma que o gate do card lê · **Prefixo das tarefas no diário:** `LF-T<n>` · **Prefixo das decisões:** `DLF-<n>` · **Forma:** legado (arquivo único, id de 4 dígitos).
+**Ordem de execução:** fila única, sequencial, na ordem das operações da `### 1.2` (§6).
+**Checagem de versão do kit:** modo hub, congelada em `0.0.0` (`GOVERNANCA.md` §10), nada a comparar.
+**Modelo de planejamento:** Fable 5.1 (sessão do dono de 2026-09-19); rodada `RP-1` em Opus 5.5 (2026-09-26).
+
+**Pronto quando:** o loop de execução de um plano roda em `.claude/tools/loop.py`, um driver Python que despacha executor e revisor por `claude -p` e materializa cada passo mecânico pelos instrumentos do kit; o piloto mediu o custo por tarefa contra a série do loop em LLM; a doutrina diz que o loop mora no driver; e o `README.md` foi revisado.
 
 **Marcos de validação pelo dono:**
 
 | marco | o que o dono lê | veredito |
 |---|---|---|
-| **Marco 1** | este plano, quando o `P-0739` fechar | `go` = plano sai de `blocked` para `ready`; `no-go` = `cancelled`, nada executado |
-| **Marco 2** | a seção `## 3. Piloto medido` depois da `LF-T6`, mais o `README.md` revisado (`LF-T8`) | aceite registrado no diário (`GOVERNANCA.md` §4.5) |
-
-**Tarefas:** 8 (`LF-T1`..`LF-T8`), fila única, sequencial.
+| **Marco 1** | a `## 1. Modelo conceitual` e este plano, antes do primeiro despacho | `go` = o plano entra na janela pela diretiva de priorização, ato do dono (o `ready` da rodada `RP-1` não o põe na janela); `no-go` = `cancelled`, nada executado |
+| **Marco 2** | a `## 11. Piloto medido` depois do piloto, mais o `README.md` revisado | aceite registrado no diário (`GOVERNANCA.md` §4.5) |
 
 ---
 
-## 0. O problema, medido
+## 0. O problema, verbatim
+
+Decisão do dono de 2026-09-19, sobre a tabela de posições de `docs/plans/_VIABILIDADE-agente-leitor.md` §7.4, linha L8, verbatim: *"L8 — loop fora do LLM (driver + `claude -p`) | viável, **recomendável como decisão de rota**, depois de L1/L2/L3 medidas | ~$180/plano; ataca a causa; muda a rota do framework"*. Destino dado pelo dono na mesma data, verbatim do registro: *"o que depende do `P-0739` → plano `docs/plans/P-0742-loop-fora-do-llm.md` (L8, absorve L5), `blocked` até o `P-0739` fechar."*
+
+Retomada (dono, 2026-09-26, card `TK-90b`): *"Retomar"*.
+
+O problema, medido (2026-09-19, `_VIABILIDADE-agente-leitor.md` §7.1, F2): o loop do `scrum-master` roda num LLM e o LLM relê o contexto inteiro a cada turno — 7–13 turnos do orquestrador por despacho, a `contexto × $0,50/M` o turno; orquestrar uma tarefa custa **$2–6**, mais que executor e reviewer juntos ($0,60 + $1,51). As sete sessões 
```
[truncado em 4000 caracteres]

### `docs/DIARIO_DE_OBRAS.md`
```
diff --git a/docs/DIARIO_DE_OBRAS.md b/docs/DIARIO_DE_OBRAS.md
index 8e3d9b6..6b57d4a 100644
--- a/docs/DIARIO_DE_OBRAS.md
+++ b/docs/DIARIO_DE_OBRAS.md
@@ -65,13 +65,13 @@ estão triados, todos com `**Rota:**` explícita.
    entrega e toda revisão exige aviso à mão mais reconciliação por hunk e mtime.
 
 <!-- fila:gerada -->
-**Fila corrente:** `TK-90` — O `P-0742` está fora do índice do diário, `blocked` com a condição já satisfeita (`docs/DIARIO_DE_OBRAS.md:6068-6134`) · fila: — · ready 12 · blocked 0 · in-progress 1
+**Fila corrente:** `P-0752` — Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção (`docs/plans/P-0752-fato-no-ponto-de-uso.md:1-785`) · fila: — · ready 12 · blocked 0 · in-progress 0
 - `TK-85` (`ready`, 0/1): próxima —
 - `TK-90` (`ready`, 1/2): próxima —
 - `TK-92` (`ready`, 0/1): próxima `TK-92a`
 - `TK-93` (`ready`, 0/1): próxima —
 - `P-0752` (`ready`, 15/17): próxima `FPU-T7`
-- `P-0742` (`blocked`, 0/8): próxima —
+- `P-0742` (`ready`, 0/8): próxima `LF-T1`
 <!-- /fila:gerada -->
 
 > **⏹ Os quatro blocos de diretiva abaixo são HISTÓRICO — o `P-0743` fechou `done` 18/18 e foi
@@ -305,7 +305,7 @@ da resposta.
 | P-0750-CAH | Comunicação agente↔humano: a mensagem ao dono se entende sozinha | done 6/6 | docs/plans/P-0750-comunicacao-agente-humano.md |
 | P-0751-EBK | Esgotar o backlog antes da publicação do kit | done 16/16 | docs/plans/P-0751-esgotar-backlog.md |
 | P-0752-FPU | Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção | ready 15/17 | docs/plans/P-0752-fato-no-ponto-de-uso.md |
-| P-0742-LF | O loop sai do LLM | blocked | docs/plans/P-0742-loop-fora-do-llm.md |
+| P-0742-LF | O loop sai do LLM | ready 0/8 | docs/plans/P-0742-loop-fora-do-llm.md |
 
 ---
 
@@ -6105,7 +6105,7 @@ card: `TK-55`, `TK-67`, `TK-70`, `TK-72`, `TK-73` e `TK-81`; o `TK-71` fechou po
 
 ### TK-90b — A rodada de replanejamento `RP-1` do `P-0742`: os oito cards passam no gate do card [Opus · esforço high · classe redacao]
 
-- **Status:** `in-progress` · 2026-09-26 — decisão do dono *"Retomar"*; espera o `TK-90a`
+- **Status:** `review` · 2026-09-27 — decisão do dono *"Retomar"*; espera o `TK-90a`
 - **Depende de:** `TK-90a`
 - **Decisão do dono (2026-09-26):** *"Retomar"* — a opção (a) que este card levava ao dono; a (b), encerrar o plano, fica descartada.
 - **Despacho:** ao `pantonic-planner`, em instância fria — é a rodada de replanejamento `RP-1` do `P-0742` (`GOVERNANCA.md` §7 item 17, `G-REPLAN`), não card de executor. O dossiê `Ato de modelo` de `autoria` que o planejador devolver, quem conduz a sessão despacha ao `pantonic-model-designer` (`GOVERNANCA.md` §3.2), e a rodada segue com a seção escrita.

```

## Medida do executor
- ausente: docs\RDO\evidencia\DIARIO_DE_OBRAS-TK-90b-medida.json não existe

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
