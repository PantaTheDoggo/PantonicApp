# Evidência de revisão — P-0755 RAF-T37

## Diff (`git diff --stat`)
```
.claude/agents/pantonic-planner.md                        |  2 +-
 docs/DIARIO_DE_OBRAS.md                                   |  4 ++--
 .../plans/P-0755-recomendacoes-auditoria-final/estado.tsv |  2 +-
 .../evidencia/P-0755-RAF-T37-medida-depois.json           | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 20 insertions(+), 4 deletions(-)
```

## Arquivos tocados
- `.claude/agents/pantonic-planner.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T37-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`

## Escopo
- Recorte: desde `69bbe2c316243c70a24c5637971b5e32750ca341`
- Arquivos-alvo declarados: `.claude/agents/pantonic-planner.md`
- Arquivos tocados: `.claude/agents/pantonic-planner.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T37-medida-depois.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T37-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/agents/pantonic-planner.md`
```
diff --git a/.claude/agents/pantonic-planner.md b/.claude/agents/pantonic-planner.md
index 4d81ec5..9c0aa65 100644
--- a/.claude/agents/pantonic-planner.md
+++ b/.claude/agents/pantonic-planner.md
@@ -212,7 +212,7 @@ Então **pare** e devolva, na linha de retorno, o dossiê `Ato de modelo` de `au
 campos, fechados: `Plano` (o caminho gravado), `Ato: autoria`, `Motivo` (o pedido da §0),
 `Fato novo` (em uma frase, o que o plano entrega quando termina — a frase da Fase 0), `Restrição`
 (os invariantes da §4 que limitam o que o plano pode entregar; a convenção de lastro
-`tarefas: <prefixo>-T<n>` para `OP-<n>`) e `Devolver` (a §1 inteira e a linha da versão 1).
+`tarefas: <prefixo>-T<n>` para `OP-<n>`; e nunca caminho de arquivo, número de linha nem nome de instrumento nas células descritivas do modelo — a norma `TK-76` do modelador os recusa, e essas residências vão à seção 2 do plano e à `Camada e fronteira` do card, `R-22` da auditoria final, `P-0755`) e `Devolver` (a §1 inteira e a linha da versão 1).
 **Nenhum agente aciona outro:** quem conduz a sessão despacha o modelador. Você não escreve uma
 linha da §1, nem "só para adiantar".
 

```

## Linhas removidas dos testes
- nenhum arquivo de teste entre os alvos

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T37-medida-depois.json; mundo: depois; gerado em: 2026-09-30T05:52:14+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('contrato=%d'%t.count('do modelador os recusa'))"` | 0 | true |

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
