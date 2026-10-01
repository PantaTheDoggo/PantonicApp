# Evidência de revisão — P-0755 RAF-T13a

## Diff (`git diff --stat`)
```
.claude/tools/card_check.py                               | 11 ++++++-----
 docs/DIARIO_DE_OBRAS.md                                   |  6 +++---
 .../plans/P-0755-recomendacoes-auditoria-final/estado.tsv |  2 +-
 .../evidencia/P-0755-RAF-T13a-medida.json                 | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 26 insertions(+), 9 deletions(-)
```

## Arquivos tocados
- `.claude/tools/card_check.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T13a-medida.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`

## Escopo
- Recorte: desde `a6c34a987129c18f0d5f64e394a5f768a3c9c99e`
- Arquivos-alvo declarados: `.claude/tools/card_check.py`
- Arquivos tocados: `.claude/tools/card_check.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T13a-medida.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T13a-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/card_check.py`
```
diff --git a/.claude/tools/card_check.py b/.claude/tools/card_check.py
index e2b3adc..87ab576 100644
--- a/.claude/tools/card_check.py
+++ b/.claude/tools/card_check.py
@@ -2,9 +2,10 @@
 `python .claude/tools/card_check.py --plano <plano> --tarefa <ID>` recorta o bloco `Verificação`
 do card pela forma normativa de `docs/RUBRICA_DE_REVISAO.md` `### 8.1` (comando em bloco cercado,
 linha `→` com o esperado, literal `**Medido antes: <valor>**`), exige os três elementos em cada
-item e **roda** cada comando publicado, comparando a saída medida agora com o `Medido antes`
-declarado — divergência é falha nomeada, porque significa que o card descreve um mundo que não é
-o que está na árvore.
+item e **roda** cada comando publicado, comparando a saída medida agora com o valor declarado
+para o mundo comparado (`--mundo`, RAF-T13: `antes` lê o `Medido antes`, `depois` o literal do
+esperado) — divergência é falha nomeada, porque significa que o card descreve um mundo que não
+é o que está na árvore.
 
 Reusa `rdo.extrair_dossie` (que por sua vez usa `rdo._parsear_campos_com_linhas`, `.claude/tools/rdo.py:187`,
 para localizar o cabeçalho da tarefa e recortar o bloco de campos) — o parser de campos é
@@ -562,8 +563,8 @@ def main(argv: list[str] | None = None) -> int:
         choices=["antes", "depois"],
         default=None,
         help=(
-            "Mundo do card a comparar na forma inline (DFP-14); ausente deriva do bullet "
-            "- **Status:** (done -> depois; demais -> antes)."
+            "Mundo do card a comparar nas duas formas, 8.1 e inline (DFP-14, RAF-T13); "
+            "ausente deriva do bullet - **Status:** (done -> depois; demais -> antes)."
         ),
     )
     parser.add_argument(

```

## Linhas removidas dos testes
- nenhum arquivo de teste entre os alvos

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T13a-medida.json; mundo: depois; gerado em: 2026-09-29T10:14:58+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/tools/card_check.py').read_text(encoding='utf-8');print('docstring=%d-%d help=%d-%d'%(t.count('declarado — divergência'),t.count('para o mundo comparado ('),t.count('comparar na forma inline'),t.count('comparar nas duas formas')))"` | 0 | true |

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
