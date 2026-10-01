# Evidência de revisão — P-0754 AUF-T11

## Diff (`git diff --stat`)
```
.claude/agents/pantonic-planner.md                        |  7 +++++++
 docs/DIARIO_DE_OBRAS.md                                   |  4 ++--
 docs/plans/P-0754-auditoria-final/estado.tsv              |  2 +-
 .../evidencia/P-0754-AUF-T11-medida.json                  | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 26 insertions(+), 3 deletions(-)
```

## Arquivos tocados
- `.claude/agents/pantonic-planner.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0754-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T11-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `c7c629cb327458d083b1200093bc009ba1327ce5`
- Arquivos-alvo declarados: `.claude/agents/pantonic-planner.md`
- Arquivos tocados: `.claude/agents/pantonic-planner.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T11-medida.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T11-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/agents/pantonic-planner.md`
```
diff --git a/.claude/agents/pantonic-planner.md b/.claude/agents/pantonic-planner.md
index d310c71..564e1bd 100644
--- a/.claude/agents/pantonic-planner.md
+++ b/.claude/agents/pantonic-planner.md
@@ -338,6 +338,13 @@ tabela dispensa não se aplica, e a razão é a própria classe.
    fato na §1 ou partição da tarefa — **ou o card não sai**. Plano liberado com ponto de
    interrupção é a pergunta que chega ao dono no meio da execução, sem contexto e sem insumos:
    falha sua, não do executor.
+   Três pontos de parada medidos que o enunciado geral deixou passar, e que se conferem pelo nome
+   em todo card: (a) **Objetivo condicional contra contrato incondicional** — o `Objetivo` diz "se"
+   enquanto `Contratos/classes` ou `Passos` mandam fazer sempre (`AE-8` do `P-0753`); (b) **caminho
+   sem forma fixada** — argumento ou campo de caminho sem dizer se é relativo à raiz do repositório
+   ou absoluto (`AE-13` do `P-0753`); (c) **argumento sem limpeza nem recusas fechadas** — argumento
+   de texto sem a normalização aplicada antes do uso (`strip()`, separador) e sem a lista fechada
+   das entradas que ele recusa, cada uma com a mensagem (`AE-18` do `P-0753`).
 9. **Campo de card lido por máquina é escrito na forma que a máquina lê**, nunca como prosa:
    `Arquivos-alvo` carrega um caminho por bullet e nenhum outro literal entre crases; arquivo citado
    para ser evitado vai para `Não fazer`; trecho de código vai para `Texto novo, literal`

```

## Medida do executor
- Arquivo: docs\plans\P-0754-auditoria-final\evidencia\P-0754-AUF-T11-medida.json; mundo: depois; gerado em: 2026-09-28T15:03:57+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('[%d-%d-%d]'%(t.count('Objetivo condicional contra contrato incondicional'),t.count('sem forma fixada'),t.count('argumento sem limpeza nem recusas fechadas')))"` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
