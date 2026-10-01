# Evidência de revisão — P-0754 AUF-T16

## Diff (`git diff --stat`)
```
docs/DIARIO_DE_OBRAS.md                            |   2 +-
 docs/audits/AUDITORIA_FINAL_KIT.md                 | 278 +++++++++++++++++++++
 docs/plans/P-0754-auditoria-final/estado.tsv       |   2 +-
 .../evidencia/P-0754-AUF-T16-medida.json           |  50 ++++
 4 files changed, 330 insertions(+), 2 deletions(-)
```

## Arquivos tocados
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/audits/AUDITORIA_FINAL_KIT.md` — atribuição: da entrega; estado git: `??`
- `docs/plans/P-0754-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T16-medida.json` — atribuição: alheio; estado git: `??`

## Escopo
- Recorte: desde `620dbc9c8362a7b6e6cd97cf14adb87fa50b8b64`
- Arquivos-alvo declarados: `docs/audits/AUDITORIA_FINAL_KIT.md`, `docs/plans/P-0754-auditoria-final/plano.md`
- Arquivos tocados: `docs/DIARIO_DE_OBRAS.md`, `docs/audits/AUDITORIA_FINAL_KIT.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T16-medida.json`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T16-medida.json`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `docs/audits/AUDITORIA_FINAL_KIT.md`
```
(arquivo novo — ausente em `620dbc9c8362a7b6e6cd97cf14adb87fa50b8b64`)
--- docs/audits/AUDITORIA_FINAL_KIT.md@620dbc9c8362a7b6e6cd97cf14adb87fa50b8b64
+++ docs/audits/AUDITORIA_FINAL_KIT.md
@@ -0,0 +1,278 @@
+# Auditoria final do kit — 2026-09-28
+
+**Objeto:** o kit agêntico Pantonic* (`.claude/` + `GOVERNANCA.md` + `docs/`), na árvore de trabalho de 2026-09-28 (branch `plan/planner-modelo-escopo`, HEAD `2513964`, com o WIP não commitado do `P-0754` — as `AUF-T1`..`AUF-T15` entregues e aprovadas).
+**Método:** o do estágio 1 (`docs/audits/AUDITORIA_ENCERRAMENTO_ESTAGIO1_2026-09-27.md`): um plano fictício, `docs/plans/P-0755-sonda-auditoria-final/`, executado ponta a ponta contra o kit real pelo procedimento que o kit prescreve (planejador → batedor → modelador → decomposição → Marco 1 → loop do `scrum-master` → revisão → ato do dono no loop → consultor → emenda do modelo → rodada de replanejamento → Marco 2 com aceite de versão → fechamento), com um registro por cláusula exercitada. Somam-se as medidas do loop real das `AUF-T1`..`AUF-T15`, conduzido na mesma sessão, e o custo da sessão principal, lido do transcript (`message.usage` de cada resposta). O plano fictício foi descartado ao fim.
+**Auditor:** a sessão principal, no papel que o dono nomeou (card `AUF-T16`, exceção à matriz de papéis válida só para ele).
+
+## 0. O pedido, verbatim
+
+Atos do dono de 2026-09-28, nesta ordem:
+
+> "execute oplano de auditoria final"
+
+> Escopo — **"Herdado + auditoria nova"**: *"Tudo o que foi herdado mais uma varredura nova do kit, que gera um relatório de auditoria, no formato usado na auditoria de encerramento do estágio 1 (P-0753)."*
+
+> Condução — **"Quem conduz (Recomendado)"**: *"A auditoria é a última tarefa do plano, executada pela sessão principal, como no estágio 1. O loop para antes dela e só a abre quando você mandar. Isso abre uma exceção à matriz de papéis, válida só para essa tarefa. A tarefa passa pela revisão. A avaliação do scrum-master que você pediu é medida no loop real, com o custo real de orquestrar."*
+
+> Marco 2 — "pode  iniciar a auditoria neste contexto"
+
+Matéria herdada que esta auditoria recebe como item de avaliação: o `AE-95` do `P-0742` (*"pode existir potencial para ganhor mecanizado ações mecânicas do scrum-master ou otimizar as rotinas dele"*, com o `scrum-master` mantido no loop) e o `H-16` do `P-0754` (onde a rodada de replanejamento grava a medida dos cards que reescreve).
+
+## 1. Modelo conceitual da auditoria
+
+| objeto | o que é | propriedades | tipo |
+|---|---|---|---|
+| relatório final | este documento | cláusulas, registros, conclusão por dimensão, recomendações, custo, avaliação do gerente do loop | escopo |
+| plano fictício | o `P-0755` que exercita as cláusulas | cláusulas cobertas, passagens, descarte | escopo |
+| teste do kit | cada passagem do plano fictício ou do loop real por uma cláusula | cláusula, procedimento, resultado esperado | escopo |
+| recomendação | tíquete derivado de um registro inadequado ou de oportunidade | causa, ação, verificação | escopo |
+| cláusula do kit | cada mecanismo testável (skill, agente, instrumento, hook, regra) | forma prescrita | externo |
+| execução do teste | a passagem real, medida | lacuna, erro, confiabilidade, custo evitável, qualidade, mecanização, fluxo | medição |
+| gerente do loop | a rotina do `scrum-master` na sessão principal | passos P1..P10, turnos e tokens por passo | medição |
+
+Fluxo: OP-1 enumerar as cláusulas → OP-2 autorar o plano fictício que as cobre → OP-3 executar cada teste e registrar a medição → OP-4 medir o gerente do loop por passo → OP-5 concluir por dimensão → OP-6 emitir as recomendações → OP-7 descartar o plano fictício.
+
+## 2. Cláusulas do kit exercitadas
+
+Uma linha por mecanismo testável; *teste* diz por qual passagem ele foi exercitado. `real` = loop real das `AUF-T1`..`AUF-T15`; `sonda` = sonda direta, sem passagem no plano fictício.
+
+| id | cláusula (mecanismo) | residência | teste |
+|---|
```
[truncado em 4000 caracteres]

### `docs/plans/P-0754-auditoria-final/plano.md`
```
(sem alteração desde `620dbc9c8362a7b6e6cd97cf14adb87fa50b8b64`)
```

## Medida do executor
- Arquivo: docs\plans\P-0754-auditoria-final\evidencia\P-0754-AUF-T16-medida.json; mundo: depois; gerado em: 2026-09-28T17:53:16+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;p=Path('docs/audits/AUDITORIA_FINAL_KIT.md');L=p.read_text(encoding='utf-8').splitlines() if p.exists() else None;H=['## 0. O pedido, verbatim','## 1. Modelo conceitual da auditoria','## 2. Cláusulas do kit exercitadas','## 3. Registros — um por teste','## 4. Conclusão por dimensão','## 5. Recomendações — um tíquete por registro viável','## 6. Custo medido da execução do plano fictício','## 7. O que ficou na árvore e o que foi descartado','## 8. As ações mecânicas do gerente do loop'];print('ausente' if L is None else '[%d]'%sum(1 for h in H if h in L))"` | 0 | true |
| 2 | `python -c "from pathlib import Path;p=Path('docs/audits/AUDITORIA_FINAL_KIT.md');L=p.read_text(encoding='utf-8').splitlines() if p.exists() else None;D=['Integração ponta a ponta','Lacunas (L)','Erros de execução (E)','Confiabilidade (C)','Custo evitável','Qualidade da entrega (Q)','Mecanização (M)','Fluxo (F)'];print('ausente' if L is None else '[%d]'%sum(1 for d in D if any(l.startswith('\| ') and d in l for l in L)))"` | 0 | true |
| 3 | `python -c "from pathlib import Path;p=Path('docs/audits/AUDITORIA_FINAL_KIT.md');L=p.read_text(encoding='utf-8').splitlines() if p.exists() else None;print('ausente' if L is None else '[%d]'%sum(1 for n in range(1,11) if any(l.startswith('\| P%d \|'%n) for l in L)))"` | 0 | true |
| 4 | `python -c "from pathlib import Path;p=Path('docs/audits/AUDITORIA_FINAL_KIT.md');L=p.read_text(encoding='utf-8').splitlines() if p.exists() else None;print('ausente' if L is None else '[%d]'%sum(1 for l in L if l.startswith('\| K-') and 'rodada de replanejamento grava a medida' in l))"` | 0 | true |
| 5 | `python -c "from pathlib import Path;p=Path('docs/audits/AUDITORIA_FINAL_KIT.md');t=p.read_text(encoding='utf-8') if p.exists() else None;print('ausente' if t is None else '[%d-%d]'%(t.count('As recomendações deste relatório não se aplicam no P-0754'),min(1,t.count('### R-'))))"` | 0 | true |
| 6 | `python -c "from pathlib import Path;p=Path('docs/audits/AUDITORIA_FINAL_KIT.md');t=p.read_text(encoding='utf-8') if p.exists() else None;print('ausente' if t is None else '[%d]'%min(1,t.count('-sonda-auditoria-final')))"` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
