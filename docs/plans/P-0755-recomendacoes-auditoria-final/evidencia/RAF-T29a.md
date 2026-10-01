# Evidência de revisão — P-0755 RAF-T29a

## Diff (`git diff --stat`)
```
.claude/tools/backlog.py                                  |  9 +++++----
 docs/DIARIO_DE_OBRAS.md                                   |  6 +++---
 .../plans/P-0755-recomendacoes-auditoria-final/estado.tsv |  2 +-
 .../evidencia/P-0755-RAF-T29a-medida-depois.json          | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 25 insertions(+), 8 deletions(-)
```

## Arquivos tocados
- `.claude/tools/backlog.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T29a-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`

## Escopo
- Recorte: desde `4a340b1c44deaddc45011a3d79572c34227e03c1`
- Arquivos-alvo declarados: `.claude/tools/backlog.py`
- Arquivos tocados: `.claude/tools/backlog.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T29a-medida-depois.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T29a-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/backlog.py`
```
diff --git a/.claude/tools/backlog.py b/.claude/tools/backlog.py
index 40b395e..917caec 100644
--- a/.claude/tools/backlog.py
+++ b/.claude/tools/backlog.py
@@ -1,10 +1,10 @@
 """BKL-T2 (`docs/plans/P-0739-backlog-instrumento.md` `### BKL-T2`) — núcleo somente-leitura do
 instrumento de backlog: carrega o índice do diário, os planos vivos e o próprio diário; monta o
-grafo item → tarefas; `check` acusa cada violação de gramática (`C-1..C-17`, vocabulário fechado
+grafo item → tarefas; `check` acusa cada violação de gramática (`C-1..C-18`, vocabulário fechado
 definido no card) com `arquivo:linha`; `resolver_citacao_secao` (`TK-60a`) resolve uma citação
 `` `<arquivo>.md` §<N>[.<N>]* `` contra o arquivo citado, acusando `C-11` quando a seção não
 existe; `C-12` (`TK-65a`) acusa `Depende de:` fora da gramática ou citando id que não é item —
-vocabulário do instrumento fechado em `C-1..C-17`; `show` emite o dossiê verbatim de um item,
+vocabulário do instrumento fechado em `C-1..C-18`; `show` emite o dossiê verbatim de um item,
 inteiro no card de tarefa; o teto `DB-7` (8.000 chars / 120 linhas, com ponteiro `arquivo:l1-l2` quando corta) vale para plano, notas de execução e achados.
 
 Gramática implementada (residência canônica: skill `diario-de-obras`, seção "Gramática legível
@@ -589,10 +589,11 @@ def carregar(repo: Path) -> Modelo:
 
 
 # --------------------------------------------------------------------------- #
-# check — violações C-1..C-17 (C-11 via resolver_citacao_secao, definido abaixo — TK-60a:
+# check — violações C-1..C-18 (C-11 via resolver_citacao_secao, definido abaixo — TK-60a:
 # check é o chamador de produção, nenhum subcomando novo; C-12 via _depende_checks — TK-65a;
 # C-15 acusa tíquete vivo sem subtarefa — EBK-T1; C-16 confronta card vivo com a leitura de
-# dossiê do rdo.py e C-17 acusa entrada órfã de piso_c11 — EBK-T2)
+# dossiê do rdo.py e C-17 acusa entrada órfã de piso_c11 — EBK-T2; C-18 acusa o prefixo de
+# decisão que dois planos declaram, via _prefixo_decisoes_checks — RAF-T29 do P-0755)
 # --------------------------------------------------------------------------- #
 
 

```

## Linhas removidas dos testes
- nenhum arquivo de teste entre os alvos

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T29a-medida-depois.json; mundo: depois; gerado em: 2026-09-30T00:49:24+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/tools/backlog.py').read_text(encoding='utf-8');print('vocabulario=%d-%d-%d linhas=%d'%(t.count('C-1..C-17'),t.count('C-1..C-18'),t.count('via _prefixo_decisoes_checks'),len(t.splitlines())))"` | 0 | true |

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
