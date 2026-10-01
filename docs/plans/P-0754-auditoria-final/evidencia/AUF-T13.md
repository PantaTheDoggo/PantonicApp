# Evidência de revisão — P-0754 AUF-T13

## Diff (`git diff --stat`)
```
.claude/agents/pantonic-planner.md                        |  5 +++++
 docs/DIARIO_DE_OBRAS.md                                   |  4 ++--
 docs/plans/P-0754-auditoria-final/estado.tsv              |  2 +-
 .../evidencia/P-0754-AUF-T13-medida.json                  | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 24 insertions(+), 3 deletions(-)
```

## Arquivos tocados
- `.claude/agents/pantonic-planner.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0754-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T13-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `3ad886a84908a7f2d4c18437c18b05fd2458d446`
- Arquivos-alvo declarados: `.claude/agents/pantonic-planner.md`
- Arquivos tocados: `.claude/agents/pantonic-planner.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T13-medida.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T13-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/agents/pantonic-planner.md`
```
diff --git a/.claude/agents/pantonic-planner.md b/.claude/agents/pantonic-planner.md
index 949905f..ba141bf 100644
--- a/.claude/agents/pantonic-planner.md
+++ b/.claude/agents/pantonic-planner.md
@@ -134,6 +134,11 @@ repositório, o que deve voltar (caminho:linha, assinatura, condição de seleç
   exit code" (≤ 40 linhas). Vale para ferramenta externa do dia a dia — `git`, `pytest`, `pwsh` —,
   não só para instrumento do kit: o erro que custou a `LM-T1` do `P-0740` foi escrever a saída de
   `git check-ignore -v` e de `git status --porcelain` de memória (2026-09-18, `RP-2`).
+- **Impedimento de papel é pergunta antes de ser dado**: diante de "o papel X não consegue Y", a
+  campanha pergunta primeiro se o impedimento é **configuração do kit** — frontmatter `tools:` do
+  agente, `.claude/settings*.json` — ou **limite da plataforma**. Configuração do kit se corrige
+  como tarefa do plano; só o limite da plataforma se contorna, com a razão registrada na §2
+  (2026-09-27, `RP-1` do `P-0753`).
 
 Orçamento: no máximo **duas** rodadas de levantamento. O que continuar desconhecido depois da
 segunda é, por definição, investigação — e vira tarefa, não terceira rodada.

```

## Medida do executor
- Arquivo: docs\plans\P-0754-auditoria-final\evidencia\P-0754-AUF-T13-medida.json; mundo: depois; gerado em: 2026-09-28T15:14:51+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('[%d]'%t.count('Impedimento de papel é pergunta antes de ser dado'))"` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
