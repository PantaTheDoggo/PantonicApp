# Evidência de revisão — P-0754 AUF-T9

## Diff (`git diff --stat`)
```
.claude/agents/pantonic-planner.md                        |  8 ++++++++
 docs/DIARIO_DE_OBRAS.md                                   |  4 ++--
 docs/plans/P-0754-auditoria-final/estado.tsv              |  2 +-
 .../evidencia/P-0754-AUF-T9-medida.json                   | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 27 insertions(+), 3 deletions(-)
```

## Arquivos tocados
- `.claude/agents/pantonic-planner.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0754-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T9-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `676e753a37b9e3994bad32ae1723a7a883280a98`
- Arquivos-alvo declarados: `.claude/agents/pantonic-planner.md`
- Arquivos tocados: `.claude/agents/pantonic-planner.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T9-medida.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T9-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/agents/pantonic-planner.md`
```
diff --git a/.claude/agents/pantonic-planner.md b/.claude/agents/pantonic-planner.md
index c8012f6..d310c71 100644
--- a/.claude/agents/pantonic-planner.md
+++ b/.claude/agents/pantonic-planner.md
@@ -268,6 +268,10 @@ tabela dispensa não se aplica, e a razão é a própria classe.
    "documentar" sem caminho de arquivo e campo é defeito. Contingência acionada é **devolvida na
    linha de retorno da entrega**, na forma `contingência <n> acionada: <o que mudou>`, e a
    orquestração a materializa na coluna `nota` da linha da tarefa em `estado.tsv` (plano legado: na linha `**Status:**` do card) (2026-09-16, `RP-4`).
+   **A contingência não contradiz o card:** a ação `seguir com <X>` de uma contingência não
+   contraria nenhuma `Restrição` do mesmo card, e todo arquivo que ela escreve entra nos
+   `Arquivos-alvo`, no próprio bullet, seguido de `(condicional: contingência <n>)`, com `<n>` a
+   posição do bullet em `Contingências` (2026-09-27, `AE-24` do `P-0753`).
 4. **Rastreabilidade**: toda decisão da §2 é consumida por ≥ 1 card; todo card cita as decisões e
    fatos de que depende; nenhum card cita algo que não está na §1 ou §2. **Coerência entre decisões
    do mesmo plano:** regra normativa cujo sujeito é um item que outra decisão do mesmo plano torna
@@ -436,6 +440,10 @@ tabela dispensa não se aplica, e a razão é a própria classe.
    antes` sobre cada card antes de gravar e `--mundo depois` sobre a cópia depois de aplicar o
    card; valor publicado é o medido. Linha que dá o mesmo valor antes e depois não discrimina e
    volta à autoria.
+   **A contingência se ensaia:** cada contingência de ação `seguir com <X>` se aplica na cópia
+   como passo do card, e as linhas de `Verificação` se re-rodam depois dela; linha cujo valor ela
+   muda publica, na própria contingência, o valor medido com ela aplicada (2026-09-27, pendência 1
+   do `P-0753`).
 
 ### Fase 5 — Registro e parada
 

```

## Medida do executor
- Arquivo: docs\plans\P-0754-auditoria-final\evidencia\P-0754-AUF-T9-medida.json; mundo: depois; gerado em: 2026-09-28T14:54:06+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('[%d-%d]'%(t.count('A contingência não contradiz o card'),t.count('A contingência se ensaia')))"` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
