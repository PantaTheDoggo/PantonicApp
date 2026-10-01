# Evidência de revisão — P-0755 RAF-T39

## Diff (`git diff --stat`)
```
.claude/skills/scrum-master/SKILL.md                      |  4 ++++
 docs/DIARIO_DE_OBRAS.md                                   |  4 ++--
 .../plans/P-0755-recomendacoes-auditoria-final/estado.tsv |  2 +-
 .../evidencia/P-0755-RAF-T39-medida-depois.json           | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 23 insertions(+), 3 deletions(-)
```

## Arquivos tocados
- `.claude/skills/scrum-master/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T39-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`

## Escopo
- Recorte: desde `4e56d2b844a06067878b2f414b64e8f41a34838e`
- Arquivos-alvo declarados: `.claude/skills/scrum-master/SKILL.md`
- Arquivos tocados: `.claude/skills/scrum-master/SKILL.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T39-medida-depois.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T39-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/skills/scrum-master/SKILL.md`
```
diff --git a/.claude/skills/scrum-master/SKILL.md b/.claude/skills/scrum-master/SKILL.md
index af4c527..42adc49 100644
--- a/.claude/skills/scrum-master/SKILL.md
+++ b/.claude/skills/scrum-master/SKILL.md
@@ -358,6 +358,10 @@ doutrina)". Depois, ponteiros e números, nunca conteúdo:
   `docs/DIARIO_DE_OBRAS.md` (primeiras 15 linhas) — ou, quando o instrumento já mantém o bloco
   gerado, deixa que `status`/`start` a regenerem e **não** a escreve à mão.
 
+### Quando a janela para num marco
+
+A janela para num marco quando a próxima tarefa do plano está `blocked` à espera do veredito do dono sobre um marco da tabela de marcos do cabeçalho do plano (nota `Marco <m>: …`). Nessa parada, a primeira linha do relatório, antes da saída do `modelo.py show`, nomeia a entrega e o pedido do dono que a originou, na forma `"<entrega>", que você pediu em <data> ("<trecho verbatim do pedido, até 15 palavras>")`: a entrega é a célula *o que o dono lê* da linha do marco na tabela de marcos (plano sem tabela de marcos: o título do plano), e o pedido é a data e um trecho verbatim do ato do dono na seção 0 do plano (`R-25` da auditoria final, `P-0755`). Exemplo, no Marco 2 do `P-0755`: `"etapa A, custo da orquestração", que você pediu em 2026-09-28 ("faça double check dos achados, e elabore um plano de atuação")`. Sem essa linha, o dono já leu uma mensagem de marco e perguntou se lhe pediam mais uma auditoria.
+
 ### Quando a janela fecha o PLANO, e não só a janela
 
 Fechada a última tarefa, o relatório **não** é o artefato de validação: o dono não dá veredito

```

## Linhas removidas dos testes
- nenhum arquivo de teste entre os alvos

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T39-medida-depois.json; mundo: depois; gerado em: 2026-09-30T06:06:38+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('marco=%d'%t.count('Quando a janela para num marco'))"` | 0 | true |

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
