# Evidência de revisão — DIARIO_DE_OBRAS TK-89b

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
 docs/DIARIO_DE_OBRAS.md                            | 3751 +++++++++++++++++++-
 docs/DIARIO_HISTORICO.md                           |  154 +
 docs/DOC_MAP.md                                    |  115 +-
 docs/RDO/INDEX.md                                  |  128 +
 docs/RESIDENCIA_DOUTRINA.md                        |    4 +-
 docs/RUBRICA_DE_REVISAO.md                         |   27 +-
 docs/consultant-spec.md                            |   75 +-
 docs/plans/P-0741-modelo-conceitual.md             |    8 +-
 docs/plans/P-0745-planejador-modelo-operacao.md    | 1584 ++++++++-
 docs/plans/_INBOX.md                               |    3 +-
 docs/plans/_INBOX_HISTORICO.md                     |    8 +
 docs/telemetria.tsv                                |  391 ++
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
 56 files changed, 10483 insertions(+), 1093 deletions(-)
```

## Arquivos tocados
- `.claude/skills/scrum-master/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-89b-medida.json` — atribuição: alheio; estado git: `??`
- `docs/RUBRICA_DE_REVISAO.md` — atribuição: da entrega; estado git: ` M`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `0b53ead2a4e1aad5ca3456ee0b39580ce554c854`
- Arquivos-alvo declarados: `.claude/skills/scrum-master/SKILL.md`, `docs/RUBRICA_DE_REVISAO.md`, `.claude/README.md`
- Arquivos tocados: `.claude/skills/scrum-master/SKILL.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-89b-medida.json`, `docs/RUBRICA_DE_REVISAO.md`, `docs/telemetria.tsv`
- Atribuídos a outra tarefa do mesmo plano: `docs/DIARIO_DE_OBRAS.md` → `TK-54b`, `docs/telemetria.tsv` → `TK-88b`
- Registro da orquestração (não atribuível a tarefa): `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-89b-medida.json`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/skills/scrum-master/SKILL.md`
```
diff --git a/.claude/skills/scrum-master/SKILL.md b/.claude/skills/scrum-master/SKILL.md
index 6daa0c4..a70e30f 100644
--- a/.claude/skills/scrum-master/SKILL.md
+++ b/.claude/skills/scrum-master/SKILL.md
@@ -59,7 +59,7 @@ Dez passos, nesta ordem.
 - **Gatilho:** tarefa corrente selecionada.
 - **Entrada:** dossiê da tarefa no plano; estado do plano.
 - **Ação:** rodar `G-PLANREADY` (`GOVERNANCA.md` §7, item 11) e o Gate de delegação
-  (`.claude/skills/passagem-de-bastao/SKILL.md`, seção "Gate de delegação", sete itens), sem
+  (`.claude/skills/passagem-de-bastao/SKILL.md`, seção "Gate de delegação", oito itens), sem
   recopiar o texto de nenhum dos dois. Recusa de qualquer um: **não delega** — vai ao passo 10 por `B3`.
 
   Terceiro gate, mecânico: `python .claude/tools/modelo.py check --plano <plano>`
@@ -282,7 +282,7 @@ Avaliado **depois** de `A6`..`A9`, sobre a tarefa já fechada, e só quando o bl
 | `B0` | vermelho de verificação, ou item de `pendencia=`, **atribuível a arquivo fora dos `Arquivos-alvo` da tarefa** — atribuição **medida** por `python .claude/tools/review_evidence.py --plano <plano> --tarefa <ID> --desde <ref> --atribuir`, nunca julgada de memória | não é pendência da tarefa: registra `AE-<n>` com a atribuição medida, **não rebaixa** a entrega, não refaz laudo e **segue** por `B4` |
 | `B1` | **pendência substantiva**: `recomendacao=escalar` no laudo, **ou** `pendencia=` cujo texto **não** seja integralmente atribuível a arquivo fora dos alvos por `B0` | registra a pendência como `AE-<n>` em `## Achados da execução` do plano, descarta o laudo e escala ao **consultor de plano** (`pantonic-consultant`, uma instância efêmera por acionamento — seção *Acionamento do consultor*), que devolve a rota (passo 8): na rota `resolve` a janela **segue** com o reparo e na rota `modelador` com o despacho do modelador; **PARA** na rota `planejador` e com `estrategico=`, como o passo 8 manda; ao dono chega só isso (`G-NOASK`, `GOVERNANCA.md` §7 item 18) |
 | `B2` | sinal de poluição do contexto do loop (**coesão**) **ou** aviso de ocupação da janela no teto de trabalho, injetado no contexto pelo hook de medida (**capacidade**) — as duas condições do `GOVERNANCA.md` §4.3 | encerra com relatório de janela: **PARA** (encerramento normal, não falha). Por coesão o encerramento **não é gracioso**: nada produzido depois do sinal de poluição se aproveita. Sem o aviso na rodada, valem a coesão e o fim do plano |
-| `B3` | a próxima tarefa é recusada pelo `G-PLANREADY`, pelo gate de delegação ou pelo `modelo.py check` do passo 3 (exit `1`) | não delega: **PARA**, com o que falta fechar |
+| `B3` | a próxima tarefa é recusada pelo `G-PLANREADY`, pelo gate de delegação, pelo `modelo.py check` ou pelo `card_check` do passo 3 (exit `1`) | não delega: **PARA**, com o que falta fechar |
 | `B4` | nenhuma das anteriores | despacha a próxima tarefa do plano, sempre sequencial |
 
 ### O que obriga parada e o que segue com registro

```

### `docs/RUBRICA_DE_REVISAO.md`
```
diff --git a/docs/RUBRICA_DE_REVISAO.md b/docs/RUBRICA_DE_REVISAO.md
index 2fc0b18..54fe3e3 100644
--- a/docs/RUBRICA_DE_REVISAO.md
+++ b/docs/RUBRICA_DE_REVISAO.md
@@ -337,8 +337,8 @@ do item, quando não há par). O mundo comparado deriva do status do card: `done
 sem literal`) (DFP-2, emendada por DFP-14).
 
 Toda ocorrência `` `<caminho>:<linha>` `` em `Arquivos-alvo` e `Passos` é âncora: o literal é o
-texto entre crases logo após ` — ` ou `: ` na mesma linha, desescapado e comparado por `strip()`
-contra a linha citada; âncora sem literal e literal fora da linha são falhas nomeadas, e âncora
+texto entre crases logo após ` — ` ou `: ` na mesma linha, desescapado e com `strip()`, e confere
+quando está contido em alguma linha (`strip()`) da faixa `linha..fim`; âncora sem literal e literal fora da linha são falhas nomeadas, e âncora
 sem literal só passa se o mesmo texto de âncora tiver literal noutra ocorrência do card — a
 conferência roda só com mundo `antes` (DFP-4, emendada por DFP-16).
 

```

### `.claude/README.md`
```
(sem alteração desde `0b53ead2a4e1aad5ca3456ee0b39580ce554c854`)
```

## Medida do executor
- Arquivo: docs\RDO\evidencia\DIARIO_DE_OBRAS-TK-89b-medida.json; mundo: depois; gerado em: 2026-09-27T02:09:52+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print(t.count('sete itens'),t.count('oito itens'))"` | 0 | true |
| 2 | `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print(sum(1 for l in t.splitlines() if l.startswith('\| ') and 'B3' in l[:8] and 'card_check' in l))"` | 0 | true |
| 3 | `python -c "from pathlib import Path;print(Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8').count('contra a linha citada'))"` | 0 | true |
| 4 | `pwsh .claude/checks/kit_check.ps1` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
