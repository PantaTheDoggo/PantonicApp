# Evidência de revisão — P-0755 RAF-T17

## Diff (`git diff --stat`)
```
.claude/agents/pantonic-planner.md                        |  6 ++++++
 docs/DIARIO_DE_OBRAS.md                                   |  4 ++--
 .../plans/P-0755-recomendacoes-auditoria-final/estado.tsv |  2 +-
 .../evidencia/P-0755-RAF-T17-medida-depois.json           | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 25 insertions(+), 3 deletions(-)
```

## Arquivos tocados
- `.claude/agents/pantonic-planner.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T17-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`

## Escopo
- Recorte: desde `eeb6f20a3e44d5ddc49a876d58407940ee0d1459`
- Arquivos-alvo declarados: `.claude/agents/pantonic-planner.md`
- Arquivos tocados: `.claude/agents/pantonic-planner.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T17-medida-depois.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T17-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/agents/pantonic-planner.md`
```
diff --git a/.claude/agents/pantonic-planner.md b/.claude/agents/pantonic-planner.md
index 4adc765..9d2377e 100644
--- a/.claude/agents/pantonic-planner.md
+++ b/.claude/agents/pantonic-planner.md
@@ -452,6 +452,12 @@ tabela dispensa não se aplica, e a razão é a própria classe.
    antes` sobre cada card antes de gravar e `--mundo depois` sobre a cópia depois de aplicar o
    card; valor publicado é o medido. Linha que dá o mesmo valor antes e depois não discrimina e
    volta à autoria.
+   **Operação de estado final igual** (`R-27` da auditoria final, `P-0755`): o card cujo alvo
+   deve ficar igual — revisão sem texto novo — não tem linha que dê valores diferentes antes e
+   depois; a linha que o discrimina é a prova de que o alvo não mudou desde o recorte do
+   despacho, `git diff --exit-code <ref> --numstat -- <alvo>` → `exit 0`, marcada
+   `(invariância)`: o `card_check` não a mede no mundo `antes`, mede no `depois`, e ela falha
+   quando o alvo muda.
    **A contingência se ensaia:** cada contingência de ação `seguir com <X>` se aplica na cópia
    como passo do card, e as linhas de `Verificação` se re-rodam depois dela; linha cujo valor ela
    muda publica, na própria contingência, o valor medido com ela aplicada (2026-09-27, pendência 1

```

## Linhas removidas dos testes
- nenhum arquivo de teste entre os alvos

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T17-medida-depois.json; mundo: depois; gerado em: 2026-09-29T11:07:35+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('igual=%d'%t.count('**Operação de estado final igual**'))"` | 0 | true |

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
