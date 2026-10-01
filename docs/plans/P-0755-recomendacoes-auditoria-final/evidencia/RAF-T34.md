# Evidência de revisão — P-0755 RAF-T34

## Diff (`git diff --stat`)
```
.claude/skills/scrum-master/SKILL.md               |  5 +++--
 docs/DIARIO_DE_OBRAS.md                            |  4 ++--
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T34-medida-depois.json    | 22 ++++++++++++++++++++++
 docs/telemetria.tsv                                |  1 +
 5 files changed, 29 insertions(+), 5 deletions(-)
```

## Arquivos tocados
- `.claude/skills/scrum-master/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T34-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`

## Escopo
- Recorte: desde `a693dae623524eba6722e5664892896505799052`
- Arquivos-alvo declarados: `.claude/skills/scrum-master/SKILL.md`
- Arquivos tocados: `.claude/skills/scrum-master/SKILL.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T34-medida-depois.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T34-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/skills/scrum-master/SKILL.md`
```
diff --git a/.claude/skills/scrum-master/SKILL.md b/.claude/skills/scrum-master/SKILL.md
index 056d613..af4c527 100644
--- a/.claude/skills/scrum-master/SKILL.md
+++ b/.claude/skills/scrum-master/SKILL.md
@@ -307,7 +307,7 @@ Avaliado **depois** de `A6`..`A9`, sobre a tarefa já fechada, e só quando o bl
 | # | condição | ação |
 |---|---|---|
 | `B0` | vermelho de verificação, ou item de `pendencia=`, **atribuível a arquivo fora dos `Arquivos-alvo` da tarefa** — atribuição **medida** por `python .claude/tools/review_evidence.py --plano <plano> --tarefa <ID> --desde <ref> --atribuir`, nunca julgada de memória | não é pendência da tarefa: registra `AE-<n>` com a atribuição medida, **não rebaixa** a entrega, não refaz laudo e **segue** por `B4` |
-| `B1` | **pendência substantiva**: `recomendacao=escalar` no laudo, **ou** `pendencia=` cujo texto **não** seja integralmente atribuível a arquivo fora dos alvos por `B0` | registra a pendência como `AE-<n>` em `## Achados da execução` do plano, descarta o laudo e escala ao **consultor de plano** (`pantonic-consultant`, uma instância efêmera por acionamento — seção *Acionamento do consultor*), que devolve a rota (passo 8): na rota `resolve` a janela **segue** com o reparo e na rota `modelador` com o despacho do modelador; **PARA** na rota `planejador` e com `estrategico=`, como o passo 8 manda; ao dono chega só isso (`G-NOASK`, `GOVERNANCA.md` §7 item 18) |
+| `B1` | **pendência substantiva**: `recomendacao=escalar` no laudo, **ou** `pendencia=` cujo texto **não** seja integralmente atribuível a arquivo fora dos alvos por `B0`, **ou** linha `encerrar: B1 — achado de instrumento com falha: <texto>` na saída do `encerrar.py tarefa`, qualquer que seja a recomendação do laudo (`R-20` da auditoria final, `P-0755`) | registra a pendência como `AE-<n>` em `## Achados da execução` do plano, descarta o laudo e escala ao **consultor de plano** (`pantonic-consultant`, uma instância efêmera por acionamento — seção *Acionamento do consultor*), que devolve a rota (passo 8): na rota `resolve` a janela **segue** com o reparo e na rota `modelador` com o despacho do modelador; **PARA** na rota `planejador` e com `estrategico=`, como o passo 8 manda; ao dono chega só isso (`G-NOASK`, `GOVERNANCA.md` §7 item 18) |
 | `B2` | sinal de poluição do contexto do loop (**coesão**) **ou** aviso de ocupação da janela no teto de trabalho, injetado no contexto pelo hook de medida (**capacidade**) — as duas condições do `GOVERNANCA.md` §4.3 | encerra com relatório de janela: **PARA** (encerramento normal, não falha). Por coesão o encerramento **não é gracioso**: nada produzido depois do sinal de poluição se aproveita. Sem o aviso na rodada, valem a coesão e o fim do plano |
 | `B3` | a próxima tarefa é recusada pelo `G-PLANREADY`, pelo gate de delegação, pelo `modelo.py check` ou pelo `card_check` do passo 3 (exit `1`) | não delega: **PARA**, com o que falta fechar |
 | `B4` | nenhuma das anteriores | despacha a próxima tarefa do plano, sempre sequencial |
@@ -331,8 +331,9 @@ fronteira do ponto do dono", e não se redecide aqui.
 
 Forma **efêmera com cenário persistido**, em piloto (`docs/plans/P-0747-consultor-de-plano.md` `DCS-6`, `DCS-7`). O consultor não fica de prontidão: a cada escalonamento das regras `A3a`, `A3b`, `A3c`, `A6a`, `A7` e `B1` e do gate do modelo do passo 9, o loop despacha **uma instância nova** do `pantonic-consultant`, com três entradas — o caminho do cenário do plano, `docs/plans/P-<n>-<slug>/cenario.md` (plano legado: `_CENARIO-<plano>.md` em `docs/plans/`); o identificador do card em causa; e a evidência (a linha de retorno do executor, a pendência do laudo ou o stderr do instrumento). A instância lê o cenário e o card, decide, reescreve o cenário com `Edit` mínimo, apensa a linha dela a `docs/ACIONAMENTOS_CONSULTOR.tsv` e devolve `rota=<resolve|modelador|planejador>` — e, só quando classifica o impedimento como estratégico, a linha `estrategico=<uma frase>` logo abaixo (`DCS-27`) —, que o l
```
[truncado em 4000 caracteres]

## Linhas removidas dos testes
- nenhum arquivo de teste entre os alvos

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T34-medida-depois.json; mundo: depois; gerado em: 2026-09-30T02:54:59+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('b1=%d'%t.count('qualquer que seja a recomendação do laudo'))"` | 0 | true |
| 2 | `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('molde=%d'%t.count('    despacho: P-<n> <ID do card em triagem>'))"` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 1
  ```
  docs\audits\sonda-2026-09-28\passos.py:13: docs.audits.sonda-2026-09-28.passos.passo (function) - sem chamador de producao alcancavel
  dead_code: FALHOU - 1 achado(s) de simbolo de producao sem chamador.
  ```
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): não conforme
- Veredito mecânico (`testes`): conforme
