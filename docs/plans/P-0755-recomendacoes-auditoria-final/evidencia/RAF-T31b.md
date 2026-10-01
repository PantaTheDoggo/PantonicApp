# Evidência de revisão — P-0755 RAF-T31b

## Diff (`git diff --stat`)
```
.claude/tools/telemetria.py                               |  9 ++++++---
 docs/DIARIO_DE_OBRAS.md                                   |  6 +++---
 .../plans/P-0755-recomendacoes-auditoria-final/estado.tsv |  2 +-
 .../evidencia/P-0755-RAF-T31b-medida-depois.json          | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 26 insertions(+), 7 deletions(-)
```

## Arquivos tocados
- `.claude/tools/telemetria.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T31b-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`

## Escopo
- Recorte: desde `6abc5eed5d5cc5f88bf6668b06651ab6ee1fefc5`
- Arquivos-alvo declarados: `.claude/tools/telemetria.py`
- Arquivos tocados: `.claude/tools/telemetria.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T31b-medida-depois.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T31b-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/telemetria.py`
```
diff --git a/.claude/tools/telemetria.py b/.claude/tools/telemetria.py
index b6dd6ef..a1e47be 100644
--- a/.claude/tools/telemetria.py
+++ b/.claude/tools/telemetria.py
@@ -2,8 +2,9 @@
 editado à mão. Cada linha nova passa por `python .claude/tools/telemetria.py append ...`: valida
 tipo e domínio de cada coluna antes de tocar o arquivo, falha ruidosa (exit != 0) em qualquer
 coluna inválida sem escrever nada, e faz a escrita em modo atômico (arquivo temporário no mesmo
-diretório + `os.replace`) — nenhum leitor concorrente vê um arquivo parcialmente escrito, e o
-conteúdo anterior nunca é tocado por conteúdo (só ganha uma linha no final).
+diretório + `os.replace`) — nenhum leitor concorrente vê um arquivo parcialmente escrito, e,
+sem `--agente`, o conteúdo anterior nunca é tocado por conteúdo (só ganha uma linha no final;
+com `--agente`, ver o parágrafo seguinte).
 
 A série histórica é insumo — sem `--agente`, nenhuma linha existente é reescrita, reordenada ou
 normalizada, e o script só apende; com `--agente` (`DRF-18`, `DRF-39` do `P-0755`), a linha do
@@ -268,7 +269,9 @@ def main(argv: list[str] | None = None) -> int:
     )
     subparsers = parser.add_subparsers(dest="command", required=True)
 
-    append_parser = subparsers.add_parser("append", help="Adiciona uma linha validada ao TSV.")
+    append_parser = subparsers.add_parser(
+        "append", help="Adiciona uma linha validada ao TSV; com --agente, troca a do mesmo agente."
+    )
     append_parser.add_argument("--data", required=True)
     append_parser.add_argument("--projeto", required=True)
     append_parser.add_argument("--tarefa", required=True)

```

## Linhas removidas dos testes
- nenhum arquivo de teste entre os alvos

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T31b-medida-depois.json; mundo: depois; gerado em: 2026-09-30T02:14:58+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/tools/telemetria.py').read_text(encoding='utf-8');print('texto=%d-%d-%d-%d linhas=%d'%(t.count('no final).'),t.count('no final;'),t.count('ver o par'),t.count('troca a do mesmo agente'),len(t.splitlines())))"` | 0 | true |

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
