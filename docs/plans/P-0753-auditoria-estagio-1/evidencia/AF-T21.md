# Evidência de revisão — P-0753 AF-T21

## Diff (`git diff --stat`)
```
.claude/agents/pantonic-planner.md                 | 14 ++++++++++-
 docs/plans/P-0753-auditoria-estagio-1/estado.tsv   |  2 +-
 .../evidencia/P-0753-AF-T21-medida.json            | 29 ++++++++++++++++++++++
 docs/telemetria.tsv                                |  1 +
 4 files changed, 44 insertions(+), 2 deletions(-)
```

## Arquivos tocados
- `.claude/agents/pantonic-planner.md` — atribuição: da entrega; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T21-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `52b5b16f29438016e5228ef0e20c74f7ea9e6a68`
- Arquivos-alvo declarados: `.claude/agents/pantonic-planner.md`
- Arquivos tocados: `.claude/agents/pantonic-planner.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T21-medida.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T21-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/agents/pantonic-planner.md`
```
diff --git a/.claude/agents/pantonic-planner.md b/.claude/agents/pantonic-planner.md
index acdeca0..c8012f6 100644
--- a/.claude/agents/pantonic-planner.md
+++ b/.claude/agents/pantonic-planner.md
@@ -186,7 +186,7 @@ no mesmo ato, `estado.tsv` na mesma pasta com o cabeçalho e só a linha do plan
 `dependencia` — a linha do `_INBOX.md` e o contador ficam para a Fase 5. O esqueleto, nesta ordem:
 
 ```
-# P-<n> — <título>            (cabeçalho: data de origem, iniciativa, plano de origem se derivado)
+# P-<n> — <título>            (cabeçalho: data de origem, iniciativa, plano de origem se derivado, classe do plano)
 ## 0. O problema, verbatim
 ## 1. Modelo conceitual          (VAZIA aqui: é do pantonic-model-designer, GOVERNANCA.md §3.2 —
                                   objetos com propriedades, fluxo de operações OP-<n>, estado inicial
@@ -235,6 +235,18 @@ rebase que absorve fase de outro plano mapeia **tarefa a tarefa**, nunca fase a
 
 ### Fase 4 — Auto-auditoria (antes de gravar, uma passada)
 
+**Profundidade pela classe do plano.** O cabeçalho do plano declara `**Classe do plano:**` com um
+de três valores: `ferramentaria` (o produto é instrumento do kit — código, teste, fixture),
+`doutrina` (o produto é texto normativo — agente, skill, `GOVERNANCA.md`, rubrica) ou `produto`
+(o produto é código do projeto consumidor). A passada aplica os itens pela tabela; item que a
+tabela dispensa não se aplica, e a razão é a própria classe.
+
+| itens | ferramentaria | doutrina | produto |
+|---|---|---|---|
+| 1 a 6 e 8 a 12 | aplicam | aplicam | aplicam |
+| 7 (parser frio) e 13 (segunda leva) | só com gramática ou tabela normativa no plano | só com gramática ou tabela normativa no plano | aplicam |
+| 14 (ensaio em cópia) | só com arquivo compartilhado tocado por dois cards | só com arquivo compartilhado tocado por dois cards | aplica |
+
 1. **G-PLANREADY, as cinco condições** (`GOVERNANCA.md` §7 item 11): id sequencial; `T1..Tn` em
    ordem de dependência, um por operação, com objetivo copiado da operação, "pronto quando"
    derivado do estado final e modelo; nenhuma decisão postergada; linear

```

## Medida do executor
- Arquivo: docs\plans\P-0753-auditoria-estagio-1\evidencia\P-0753-AF-T21-medida.json; mundo: depois; gerado em: 2026-09-27T17:15:01+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print(t.count('Profundidade pela classe do plano'),t.count('plano de origem se derivado, classe do plano)'))"` | 0 | true |
| 2 | `python -m pytest -q` | 0 | true |
| 3 | `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
