# Evidência de revisão — P-0753 AF-T16

## Diff (`git diff --stat`)
```
.claude/checks/check-readme.ps1                    |  1 +
 .claude/checks/kit_check.ps1                       |  1 +
 docs/DIARIO_DE_OBRAS.md                            |  4 +--
 docs/plans/P-0753-auditoria-estagio-1/estado.tsv   |  2 +-
 .../evidencia/P-0753-AF-T16-medida.json            | 36 ++++++++++++++++++++++
 docs/telemetria.tsv                                |  1 +
 6 files changed, 42 insertions(+), 3 deletions(-)
```

## Arquivos tocados
- `.claude/checks/check-readme.ps1` — atribuição: da entrega; estado git: ` M`
- `.claude/checks/kit_check.ps1` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T16-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `44ffafa7fe0444360f927e5a1684da65fb5ef075`
- Arquivos-alvo declarados: `.claude/checks/check-readme.ps1`, `.claude/checks/kit_check.ps1`
- Arquivos tocados: `.claude/checks/check-readme.ps1`, `.claude/checks/kit_check.ps1`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T16-medida.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T16-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/checks/check-readme.ps1`
```
diff --git a/.claude/checks/check-readme.ps1 b/.claude/checks/check-readme.ps1
index f4106ec..5a4c5c3 100644
--- a/.claude/checks/check-readme.ps1
+++ b/.claude/checks/check-readme.ps1
@@ -42,6 +42,7 @@ param(
 )
 
 $ErrorActionPreference = 'Stop'
+[Console]::OutputEncoding = [Text.Encoding]::UTF8
 
 if (-not $Root) {
     # .claude/checks/check-readme.ps1 -> .claude -> raiz do repo

```

### `.claude/checks/kit_check.ps1`
```
diff --git a/.claude/checks/kit_check.ps1 b/.claude/checks/kit_check.ps1
index 0fd2252..8754cec 100644
--- a/.claude/checks/kit_check.ps1
+++ b/.claude/checks/kit_check.ps1
@@ -32,6 +32,7 @@ param(
 )
 
 $ErrorActionPreference = 'Stop'
+[Console]::OutputEncoding = [Text.Encoding]::UTF8
 
 if (-not $KitRoot) {
     # .claude/checks/kit_check.ps1 -> .claude/

```

## Medida do executor
- Arquivo: docs\plans\P-0753-auditoria-estagio-1\evidencia\P-0753-AF-T16-medida.json; mundo: depois; gerado em: 2026-09-27T16:23:32+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "import subprocess;r=subprocess.run(['pwsh','-NoProfile','-File','.claude/checks/check-readme.ps1'],capture_output=True);print(r.stdout.decode('utf-8','replace').count(chr(65533))>0)"` | 0 | true |
| 2 | `python -c "from pathlib import Path;s='[Console]::OutputEncoding = [Text.Encoding]::UTF8';print(Path('.claude/checks/kit_check.ps1').read_text(encoding='utf-8').count(s),Path('.claude/checks/check-readme.ps1').read_text(encoding='utf-8').count(s))"` | 0 | true |
| 3 | `python -m pytest -q` | 0 | true |
| 4 | `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
