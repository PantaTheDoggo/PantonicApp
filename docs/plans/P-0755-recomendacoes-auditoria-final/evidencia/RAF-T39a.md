# Evidência de revisão — P-0755 RAF-T39a

## Diff (`git diff --stat`)
```
.claude/skills/scrum-master/SKILL.md                      |  4 ++--
 docs/DIARIO_DE_OBRAS.md                                   |  6 +++---
 .../plans/P-0755-recomendacoes-auditoria-final/estado.tsv |  2 +-
 .../evidencia/P-0755-RAF-T39a-medida-depois.json          | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 22 insertions(+), 6 deletions(-)
```

## Arquivos tocados
- `.claude/skills/scrum-master/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T39a-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`

## Escopo
- Recorte: desde `a66c546cadb7500821c9a68759a613ac83bd72a4`
- Arquivos-alvo declarados: `.claude/skills/scrum-master/SKILL.md`
- Arquivos tocados: `.claude/skills/scrum-master/SKILL.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T39a-medida-depois.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T39a-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/skills/scrum-master/SKILL.md`
```
diff --git a/.claude/skills/scrum-master/SKILL.md b/.claude/skills/scrum-master/SKILL.md
index 42adc49..ede8b71 100644
--- a/.claude/skills/scrum-master/SKILL.md
+++ b/.claude/skills/scrum-master/SKILL.md
@@ -342,7 +342,7 @@ Molde do despacho — a linha de abertura com o card em triagem (`GOVERNANCA.md`
 ## Relatório de encerramento
 
 Uma vez por janela, na parada. Abre com a saída integral de `python
-.claude/tools/modelo.py show --plano <plano>` — a
+.claude/tools/modelo.py show --plano <plano>` (na parada de marco, logo depois da linha que nomeia a entrega, na subseção abaixo) — a
 única exceção à regra de conteúdo, porque o modelo **é** o que o dono lê
 (`GOVERNANCA.md` §3.2); plano sem modelo, a linha "sem modelo (plano anterior à
 doutrina)". Depois, ponteiros e números, nunca conteúdo:
@@ -360,7 +360,7 @@ doutrina)". Depois, ponteiros e números, nunca conteúdo:
 
 ### Quando a janela para num marco
 
-A janela para num marco quando a próxima tarefa do plano está `blocked` à espera do veredito do dono sobre um marco da tabela de marcos do cabeçalho do plano (nota `Marco <m>: …`). Nessa parada, a primeira linha do relatório, antes da saída do `modelo.py show`, nomeia a entrega e o pedido do dono que a originou, na forma `"<entrega>", que você pediu em <data> ("<trecho verbatim do pedido, até 15 palavras>")`: a entrega é a célula *o que o dono lê* da linha do marco na tabela de marcos (plano sem tabela de marcos: o título do plano), e o pedido é a data e um trecho verbatim do ato do dono na seção 0 do plano (`R-25` da auditoria final, `P-0755`). Exemplo, no Marco 2 do `P-0755`: `"etapa A, custo da orquestração", que você pediu em 2026-09-28 ("faça double check dos achados, e elabore um plano de atuação")`. Sem essa linha, o dono já leu uma mensagem de marco e perguntou se lhe pediam mais uma auditoria.
+A janela para num marco quando a próxima tarefa do plano está `blocked` à espera do veredito do dono sobre um marco da tabela de marcos do cabeçalho do plano (nota `Marco <m>: …`). Nessa parada, a primeira linha do relatório, antes da saída do `modelo.py show`, nomeia a entrega e o pedido do dono que a originou, na forma `"<entrega>", que você pediu em <data> ("<trecho verbatim do pedido, até 15 palavras>")`: a entrega é o nome da etapa na célula *o que o dono lê* da linha do marco na tabela de marcos, o trecho antes dos dois-pontos, sem a lista que os segue (marco cuja célula não nomeia etapa, como o do modelo, que cita o comando `modelo.py show`, ou plano sem tabela de marcos: o título do plano), e o pedido é a data e um trecho verbatim do ato do dono na seção 0 do plano (`R-25` da auditoria final, `P-0755`). Exemplo, no Marco 2 do `P-0755`: `"etapa A, custo da orquestração", que você pediu em 2026-09-28 ("faça double check dos achados, e elabore um plano de atuação")`. Sem essa linha, o dono já leu uma mensagem de marco e perguntou se lhe pediam mais uma auditoria.
 
 ### Quando a janela fecha o PLANO, e não só a janela
 

```

## Linhas removidas dos testes
- nenhum arquivo de teste entre os alvos

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T39a-medida-depois.json; mundo: depois; gerado em: 2026-09-30T06:18:23+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('marco=%d-%d-%d-%d'%(t.count('Quando a janela para num marco'),t.count('logo depois da linha que nomeia a entrega'),t.count('o trecho antes dos dois-pontos'),t.count('a entrega é a célula')))"` | 0 | true |

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
