# Evidência de revisão — P-0755 RAF-T4

## Diff (`git diff --stat`)
```
.claude/skills/scrum-master/SKILL.md               | 21 +++++++++++++--------
 docs/DIARIO_DE_OBRAS.md                            |  4 ++--
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T4-medida.json            | 22 ++++++++++++++++++++++
 docs/telemetria.tsv                                |  1 +
 5 files changed, 39 insertions(+), 11 deletions(-)
```

## Arquivos tocados
- `.claude/skills/scrum-master/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T4-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `c3d19d2b61cb3a596ed7629054828cc9654f24eb`
- Arquivos-alvo declarados: `.claude/skills/scrum-master/SKILL.md`
- Arquivos tocados: `.claude/skills/scrum-master/SKILL.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T4-medida.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T4-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/skills/scrum-master/SKILL.md`
```
diff --git a/.claude/skills/scrum-master/SKILL.md b/.claude/skills/scrum-master/SKILL.md
index 0f07295..7a59b06 100644
--- a/.claude/skills/scrum-master/SKILL.md
+++ b/.claude/skills/scrum-master/SKILL.md
@@ -81,8 +81,10 @@ Dez passos, nesta ordem.
 
   **Por comando** (`R-15`): `python .claude/tools/backlog.py despachar <ID>` roda, nesta ordem, o
   terceiro gate, o quarto e a coleta da suíte (`python -m pytest --co -q`), materializa
-  `in-progress`, grava `.claude/estado/tarefa-corrente.json` com o `<ref>` e imprime o card
-  inteiro, o bloco `HANDOVER` e a linha `ref=<sha>`. Recusa pelo primeiro gate que falhar, sem
+  `in-progress`, grava `.claude/estado/tarefa-corrente.json` com o `<ref>`, grava o pacote da
+  tarefa em `<pasta-do-plano>/despacho/<ID>.md` (fora do versionamento: o card, os handovers e as
+  âncoras conferidas contra a árvore de agora) e imprime só o texto pronto do despacho ao
+  executor e a linha `ref=<sha>`. Recusa pelo primeiro gate que falhar, sem
   escrever nada: exit `1` **não delega**, e a linha de recusa vai à razão de `B3`. `G-PLANREADY` e o
   Gate de delegação continuam com quem conduz, antes do verbo; card de tíquete segue pelos passos
   à mão. Redespacho de tarefa cuja entrega já está na árvore (o consultor manteve o trabalho e a
@@ -106,11 +108,14 @@ Dez passos, nesta ordem.
   desde o despacho. No redespacho da mesma tarefa (retomada depois de `blocked`, ou retentativa),
   o `<ref>` não se recaptura: vale o do primeiro despacho, para a evidência cobrir as duas execuções.
 
-  Despachada pelo verbo `despachar` do passo 3, a tarefa já tem o arquivo gravado e o `<ref>` na
-  linha `ref=<sha>` da saída: este passo só invoca o executor.
+  Despachada pelo verbo `despachar` do passo 3, a tarefa já tem o arquivo gravado, o pacote em
+  `<pasta-do-plano>/despacho/<ID>.md` e o `<ref>` na linha `ref=<sha>` da saída: este passo só
+  invoca o executor.
 
   Invocar `pantonic-executor` com `model` **igual ao do cabeçalho** (vence o `model:` do agente),
-  com o dossiê da tarefa e a instrução de devolver **uma única linha**, domínio fechado (`DP-G`
+  com o texto pronto que o `despachar` imprimiu entre a linha `=== DESPACHO:` e a linha
+  `ref=<sha>`, repassado como está — sem copiar o card nem o handover na conversa —, que já traz
+  a instrução de devolver **uma única linha**, domínio fechado (`DP-G`
   item 2):
 
   ```
@@ -121,9 +126,9 @@ Dez passos, nesta ordem.
 
   Desempate (`DP-G` item 3): na dúvida sobre o motivo, `premissa`. RDO e guardrails de
   arquitetura não vão no despacho.
-  O despacho cola, junto do dossiê, as **âncoras** (arquivo, linha e texto do ponto a editar)
-  re-derivadas no ato e o **range de linhas do bullet de fechamento anterior** quando a tarefa
-  fecha em plano em andamento.
+  As **âncoras** (arquivo, linha e texto do ponto a editar) chegam conferidas no pacote do
+  despacho; nenhum passo as reconfere à mão. Quando a tarefa fecha em plano em andamento, o
+  despacho acrescenta ao texto pronto o **range de linhas do bullet de fechamento anterior**.
 - **Saída:** uma linha de retorno do executor.
 
 ### Passo 5 — Recepção do retorno do executor

```

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T4-medida.json; mundo: depois; gerado em: 2026-09-29T02:24:09+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('entrega=%d-%d'%(t.count('com o dossiê da tarefa e a instrução de devolver'),t.count('repassado como está — sem copiar o card nem o handover na conversa')))"` | 0 | true |
| 2 | `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('ancoras=%d-%d'%(t.count('re-derivadas no ato'),t.count('nenhum passo as reconfere à mão')))"` | 0 | true |

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
