# Evidência de revisão — P-0755 RAF-T38

## Diff (`git diff --stat`)
```
.claude/agents/pantonic-planner.md                 |  2 +-
 .claude/skills/checar-versao-kit/SKILL.md          |  2 +-
 docs/DIARIO_DE_OBRAS.md                            |  4 ++--
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T38-medida-depois.json    | 22 ++++++++++++++++++++++
 docs/telemetria.tsv                                |  1 +
 6 files changed, 28 insertions(+), 5 deletions(-)
```

## Arquivos tocados
- `.claude/agents/pantonic-planner.md` — atribuição: da entrega; estado git: ` M`
- `.claude/skills/checar-versao-kit/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T38-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`

## Escopo
- Recorte: desde `6bf6e3c47be98a170196958a6d691041b2d46383`
- Arquivos-alvo declarados: `.claude/skills/checar-versao-kit/SKILL.md`, `.claude/agents/pantonic-planner.md`
- Arquivos tocados: `.claude/agents/pantonic-planner.md`, `.claude/skills/checar-versao-kit/SKILL.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T38-medida-depois.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T38-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/skills/checar-versao-kit/SKILL.md`
```
diff --git a/.claude/skills/checar-versao-kit/SKILL.md b/.claude/skills/checar-versao-kit/SKILL.md
index 99935c3..72041a8 100644
--- a/.claude/skills/checar-versao-kit/SKILL.md
+++ b/.claude/skills/checar-versao-kit/SKILL.md
@@ -10,7 +10,7 @@ procedimento que a executa. Em caso de dúvida sobre a regra, §10 é a fonte, n
 
 ## Quando roda
 
-Na criação/registro de todo plano novo (skill `diario-de-obras`, operação "1. Registrar plano").
+Na criação de todo plano novo: quem conduz a sessão a roda antes de despachar o planejador (`pantonic-planner`) e passa o resultado no pedido a ele, e o planejador o registra no campo `**Checagem de versão do kit:**` do cabeçalho do plano — subagente, o planejador não invoca skill (`R-23` da auditoria final, `P-0755`). Plano registrado sem planejador roda a checagem no registro (skill `diario-de-obras`, operação "1. Registrar plano").
 Esse é o único gatilho de invocação — não roda a cada turno, nem a cada tarefa, só quando um plano
 é criado. Uma vez invocada, executa **duas** checagens independentes: a de versão (passos 1-3
 abaixo) e a de revisão da doutrina (última seção); as duas compartilham só o momento de invocação,

```

### `.claude/agents/pantonic-planner.md`
```
diff --git a/.claude/agents/pantonic-planner.md b/.claude/agents/pantonic-planner.md
index 9c0aa65..0e275f9 100644
--- a/.claude/agents/pantonic-planner.md
+++ b/.claude/agents/pantonic-planner.md
@@ -472,7 +472,7 @@ tabela dispensa não se aplica, e a razão é a classe ou o tamanho. Plano cuja
 
 Com a §1 e a §5 na árvore, rode `python .claude/tools/modelo.py check --plano <plano>` (exit `0`)
 e, para todo card, `card_check` exit `0` como condição de registro, ao lado de `modelo.py check`;
-complete o `estado.tsv` da pasta do plano com uma linha por card (esquema da skill `diario-de-obras`; a linha do plano já está lá desde a Fase 3a), apense a linha ao `_INBOX.md` e atualize o próximo id no mesmo ato; invoque `checar-versao-kit`; se o plano é derivado de outro, classifique (A/B/C) e
+complete o `estado.tsv` da pasta do plano com uma linha por card (esquema da skill `diario-de-obras`; a linha do plano já está lá desde a Fase 3a), apense a linha ao `_INBOX.md` e atualize o próximo id no mesmo ato; registre no cabeçalho do plano, no campo `**Checagem de versão do kit:**`, o resultado da checagem de versão que o pedido de quem conduz traz (quem conduz roda a skill `checar-versao-kit` antes de despachar o planejador, e nenhuma fase deste roteiro a chama; sem o resultado no pedido, o campo registra `não recebida no pedido`, `R-23` da auditoria final, `P-0755`); se o plano é derivado de outro, classifique (A/B/C) e
 aplique o efeito ao plano de origem (skill `diario-de-obras`, "Planos derivados"). Então **pare**:
 plano registrado é fim do turno (Regra 1 global) — a execução começa em outro contexto, por
 instrução explícita do dono.

```

## Linhas removidas dos testes
- nenhum arquivo de teste entre os alvos

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T38-medida-depois.json; mundo: depois; gerado em: 2026-09-30T05:59:16+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/skills/checar-versao-kit/SKILL.md').read_text(encoding='utf-8');print('momento=%d'%t.count('a roda antes de despachar o planejador'))"` | 0 | true |
| 2 | `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('versao=%d-%d'%(t.count('invoque'),t.count('Checagem de versão do kit:')))"` | 0 | true |

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
