# Evidência de revisão — P-0755 RAF-T31a

## Diff (`git diff --stat`)
```
.claude/tools/telemetria.py                        | 29 ++++++++++++++--------
 docs/DIARIO_DE_OBRAS.md                            |  6 ++---
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T31a-medida-depois.json   | 15 +++++++++++
 docs/telemetria.tsv                                |  1 +
 5 files changed, 39 insertions(+), 14 deletions(-)
```

## Arquivos tocados
- `.claude/tools/telemetria.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T31a-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`

## Escopo
- Recorte: desde `3f96fd9d19b5e2fddf3c4acf646393f281abc879`
- Arquivos-alvo declarados: `.claude/tools/telemetria.py`
- Arquivos tocados: `.claude/tools/telemetria.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T31a-medida-depois.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T31a-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/telemetria.py`
```
diff --git a/.claude/tools/telemetria.py b/.claude/tools/telemetria.py
index c8c79c2..b6dd6ef 100644
--- a/.claude/tools/telemetria.py
+++ b/.claude/tools/telemetria.py
@@ -5,10 +5,13 @@ coluna inválida sem escrever nada, e faz a escrita em modo atômico (arquivo te
 diretório + `os.replace`) — nenhum leitor concorrente vê um arquivo parcialmente escrito, e o
 conteúdo anterior nunca é tocado por conteúdo (só ganha uma linha no final).
 
-A série histórica é insumo — nenhuma linha existente é reescrita, reordenada ou normalizada; o
-script só apende. Colunas na ordem do header real do TSV: `data`, `projeto`, `tarefa`, `modelo`,
-`tool_uses`, `tokens_k`, `duracao_s`, `fonte`. O mapeamento é sempre por nome de coluna (nunca por
-posição), o que elimina o risco de "coluna trocada em silêncio" que a edição manual admitia.
+A série histórica é insumo — sem `--agente`, nenhuma linha existente é reescrita, reordenada ou
+normalizada, e o script só apende; com `--agente` (`DRF-18`, `DRF-39` do `P-0755`), a linha do
+mesmo agente é substituída, e a série sem a coluna `agente` a ganha, com `-` nas linhas antigas.
+Colunas na ordem do header real do TSV: `data`, `projeto`, `tarefa`, `modelo`, `tool_uses`,
+`tokens_k`, `duracao_s`, `fonte` e, na série migrada, `agente`. O mapeamento é sempre por nome
+de coluna (nunca por posição), o que elimina o risco de "coluna trocada em silêncio" que a
+edição manual admitia.
 
 A célula vazia é a sentinela de métrica não medida. `tool_uses`, `tokens_k` e `duracao_s` aceitam
 célula vazia sempre que `fonte` é `contado` ou `nao_medido`. Com `fonte=usage` os três campos são
@@ -17,9 +20,9 @@ ausente.
 
 CLI: ``python .claude/tools/telemetria.py append --data AAAA-MM-DD --projeto P --tarefa T
 --modelo M --tool_uses N --tokens_k K --duracao_s S --fonte {usage,contado,nao_medido}
-[--file caminho/para/telemetria.tsv]``. Sem `--file`, resolve `docs/telemetria.tsv` a partir da
-raiz do repositório (mesmo desenho do `--root` de `.claude/checks/dead_code.py`: a raiz é
-derivada da posição do próprio script, não do diretório de trabalho).
+[--file caminho/para/telemetria.tsv] [--agente A]``. Sem `--file`, resolve `docs/telemetria.tsv`
+a partir da raiz do repositório (mesmo desenho do `--root` de `.claude/checks/dead_code.py`: a
+raiz é derivada da posição do próprio script, não do diretório de trabalho).
 """
 from __future__ import annotations
 
@@ -149,7 +152,10 @@ def eh_repetida(ultima: dict, nova: dict) -> bool:
 def checar_repetida(path: Path, row: str) -> None:
     """Lê `row` pelas colunas de `_COLUMNS` e lança `TelemetriaRepetidaError` quando a última
     linha da mesma `tarefa` na série de `path` já tem `modelo`, `tool_uses` e `tokens_k` iguais
-    (DFP-8) — chamada antes de qualquer escrita, para que a recusa valha para todo escritor."""
+    (DFP-8) — chamada antes de qualquer escrita sem agente (`append_row` e o `encerrar.py`),
+    para que a recusa valha para todo escritor sem agente; o escritor por agente não a chama:
+    nele a mesma rodada é a linha do mesmo agente, que `gravar_por_agente` substitui (`DRF-69`
+    do `P-0755`)."""
     nova = dict(zip(_COLUMNS, row.split("\t")))
     ultima = ultima_linha_da_tarefa(path, nova.get("tarefa", ""))
     if ultima is not None and eh_repetida(ultima, nova):
@@ -179,7 +185,9 @@ def gravar_por_agente(path: Path, row: str, agente: str) -> None:
     nova do mesmo `agente` substitui a linha antiga dele, em vez de apensar. Cabeçalho ausente
     ganha o de `_COLUMNS`; cabeçalho que não termina na coluna `agente` ganha `\tagente`, e cada
     linha de dado existente ganha `\t-` (a coluna nova nasce vazia para elas). Escrita atômica:
-    arquivo temporário no mesmo diretório e `os.replace`, como `append_row`."""
+    arquivo temporário no mesmo diretório e `os.replace`, como `append_row`. Não chama
+    `checar_repetida` (DFP-8): a linha do mesmo agente é a mesma rodada, e a troca a deixa
+    idempotente (`DRF-69` do `P-0755`)."""
     linhas: list
```
[truncado em 4000 caracteres]

## Linhas removidas dos testes
- nenhum arquivo de teste entre os alvos

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T31a-medida-depois.json; mundo: depois; gerado em: 2026-09-30T02:02:46+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/tools/telemetria.py').read_text(encoding='utf-8');print('docstring=%d-%d-%d-%d-%d linhas=%d'%(t.count('valha para todo escritor.'),t.count('para todo escritor, n'),t.count('reordenada ou normalizada;'),t.count('DRF-69'),t.count('[--agente A]'),len(t.splitlines())))"` | 0 | true |

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
