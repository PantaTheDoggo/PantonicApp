# Evidência de revisão — P-0755 RAF-T33

## Diff (`git diff --stat`)
```
GOVERNANCA.md                                             | 14 ++++++++++----
 docs/DIARIO_DE_OBRAS.md                                   |  4 ++--
 .../plans/P-0755-recomendacoes-auditoria-final/estado.tsv |  2 +-
 .../evidencia/P-0755-RAF-T33-medida-depois.json           | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 29 insertions(+), 7 deletions(-)
```

## Arquivos tocados
- `GOVERNANCA.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T33-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`

## Escopo
- Recorte: desde `6f0ad5036b8fa967baa90ff8a69bef76e575c9ab`
- Arquivos-alvo declarados: `GOVERNANCA.md`
- Arquivos tocados: `GOVERNANCA.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T33-medida-depois.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T33-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `GOVERNANCA.md`
```
diff --git a/GOVERNANCA.md b/GOVERNANCA.md
index 5371d0b..a6cb032 100644
--- a/GOVERNANCA.md
+++ b/GOVERNANCA.md
@@ -634,9 +634,9 @@ também como um kanban adaptado:
   para detectar regressão de consumo por tarefa, mesmo racional do piso de regressão de testes
   aplicado a custo. O registro do consumo, na série e no diário, é escrito pelo **orquestrador** a
   partir do dado medido da notificação.
-- **Fonte única da série** — `docs/telemetria.tsv` (append-only, colunas `data`, `projeto`,
+- **Fonte única da série** — `docs/telemetria.tsv` (colunas `data`, `projeto`,
   `tarefa`, `modelo`, `tool_uses`, `tokens_k`, `duracao_s`, `fonte` ∈ `{usage, contado,
-  nao_medido}`) é a **fonte da série de consumo**; o diário/histórico **aponta** para ela
+  nao_medido}`, `agente`) é a **fonte da série de consumo**; o diário/histórico **aponta** para ela
   (`Consumo: ver docs/telemetria.tsv`) em vez de copiar o número. Duplicar a medição em prosa
   recriaria duas fontes que divergem à primeira edição. Registro qualitativo que não cabe em
   coluna (estouro de teto, execução inline, ressalva sobre a medida) continua no bullet do diário,
@@ -655,8 +655,14 @@ também como um kanban adaptado:
   executor e vale até o despacho seguinte; o hook `SubagentStop` grava a rodada de todo papel
   `pantonic-*`, com o papel no identificador da tarefa: `<ID>` do executor, `<ID>-revisao` do
   revisor, `<ID>-consultor-<n>` do consultor, `<P-n>-planejador`, `<P-n>-modelador` e
-  `<P-n>-scout` pelo primeiro id de plano da primeira mensagem do subagente, e
-  `sem-id-<papel>` quando não há id a derivar.
+  `<P-n>-scout`, e `sem-id-<papel>` quando não há id a derivar. **Linha de abertura do
+  despacho** (`R-16` da auditoria final, `P-0755`): todo despacho de subagente abre com a
+  linha `despacho: <P-id>`, seguida de um espaço e do id da tarefa ou do tíquete quando
+  houver; o hook lê o plano e a tarefa nela antes de `tarefa-corrente.json` e antes do
+  primeiro id de plano citado na primeira mensagem, que só valem sem ela, e o painel do
+  gerente mostra a tarefa que ela declara. A série guarda uma linha por agente, a última e
+  acumulada, com o nome do agente na coluna `agente` (`-` nas linhas anteriores à coluna e
+  nas gravadas sem agente).
 
 ### 4.3 Execução em contexto limpo
 

```

## Linhas removidas dos testes
- nenhum arquivo de teste entre os alvos

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T33-medida-depois.json; mundo: depois; gerado em: 2026-09-30T02:48:10+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('GOVERNANCA.md').read_text(encoding='utf-8');print('abertura=%d-%d'%(t.count('pelo primeiro id de plano da primeira mensagem do subagente'),t.count('todo despacho de subagente abre com a')))"` | 0 | true |

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
