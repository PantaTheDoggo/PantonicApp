# Evidência de revisão — P-0755 RAF-T36

## Diff (`git diff --stat`)
```
.claude/agents/pantonic-planner.md                        | 14 +++++++-------
 docs/DIARIO_DE_OBRAS.md                                   |  4 ++--
 .../plans/P-0755-recomendacoes-auditoria-final/estado.tsv |  2 +-
 .../evidencia/P-0755-RAF-T36-medida-depois.json           | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 26 insertions(+), 10 deletions(-)
```

## Arquivos tocados
- `.claude/agents/pantonic-planner.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T36-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`

## Escopo
- Recorte: desde `cbfc089d669826fb2368c6a7825a253cbf6963ae`
- Arquivos-alvo declarados: `.claude/agents/pantonic-planner.md`
- Arquivos tocados: `.claude/agents/pantonic-planner.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T36-medida-depois.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T36-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/agents/pantonic-planner.md`
```
diff --git a/.claude/agents/pantonic-planner.md b/.claude/agents/pantonic-planner.md
index c189117..4d81ec5 100644
--- a/.claude/agents/pantonic-planner.md
+++ b/.claude/agents/pantonic-planner.md
@@ -240,17 +240,17 @@ rebase que absorve fase de outro plano mapeia **tarefa a tarefa**, nunca fase a
 
 ### Fase 4 — Auto-auditoria (antes de gravar, uma passada)
 
-**Profundidade pela classe do plano.** O cabeçalho do plano declara `**Classe do plano:**` com um
+**Profundidade pela classe e pelo tamanho do plano.** O cabeçalho do plano declara `**Classe do plano:**` com um
 de três valores: `ferramentaria` (o produto é instrumento do kit — código, teste, fixture),
 `doutrina` (o produto é texto normativo — agente, skill, `GOVERNANCA.md`, rubrica) ou `produto`
 (o produto é código do projeto consumidor). A passada aplica os itens pela tabela; item que a
-tabela dispensa não se aplica, e a razão é a própria classe.
+tabela dispensa não se aplica, e a razão é a classe ou o tamanho. Plano cuja seção 1.2 tem até cinco operações usa a última coluna, qualquer que seja a classe declarada (`R-21` da auditoria final, `P-0755`): nesse tamanho, o parser frio, a segunda leva e o ensaio sem arquivo compartilhado não mudam o resultado, e o ensaio da contingência só o muda quando ela escreve arquivo.
 
-| itens | ferramentaria | doutrina | produto |
-|---|---|---|---|
-| 1 a 6 e 8 a 12 | aplicam | aplicam | aplicam |
-| 7 (parser frio) e 13 (segunda leva) | só com gramática ou tabela normativa no plano | só com gramática ou tabela normativa no plano | aplicam |
-| 14 (ensaio em cópia) | só com arquivo compartilhado tocado por dois cards | só com arquivo compartilhado tocado por dois cards | aplica |
+| itens | ferramentaria | doutrina | produto | até 5 operações, qualquer classe |
+|---|---|---|---|---|
+| 1 a 6 e 8 a 12 | aplicam | aplicam | aplicam | aplicam |
+| 7 (parser frio) e 13 (segunda leva) | só com gramática ou tabela normativa no plano | só com gramática ou tabela normativa no plano | aplicam | só com gramática ou tabela normativa no plano |
+| 14 (ensaio em cópia) | só com arquivo compartilhado tocado por dois cards | só com arquivo compartilhado tocado por dois cards | aplica | só com arquivo compartilhado tocado por dois cards; o ensaio da contingência, só quando a contingência escreve arquivo |
 
 1. **G-PLANREADY, as cinco condições** (`GOVERNANCA.md` §7 item 11): id sequencial; `T1..Tn` em
    ordem de dependência, um por operação, com objetivo copiado da operação, "pronto quando"

```

## Linhas removidas dos testes
- nenhum arquivo de teste entre os alvos

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T36-medida-depois.json; mundo: depois; gerado em: 2026-09-30T05:37:16+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('regua=%d-%d'%(t.count('a razão é a própria classe'),t.count('até 5 operações, qualquer classe')))"` | 0 | true |

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
