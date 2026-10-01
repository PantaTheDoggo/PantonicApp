# Evidência de revisão — P-0755 RAF-T20

## Diff (`git diff --stat`)
```
.claude/tools/backlog.py                           |   3 +-
 docs/DIARIO_DE_OBRAS.md                            |   4 +-
 .../estado.tsv                                     |   2 +-
 .../evidencia/P-0755-RAF-T20-medida-depois.json    |  15 +++
 docs/telemetria.tsv                                |   1 +
 tests/test_backlog.py                              | 130 +++++++++++++++++++++
 6 files changed, 151 insertions(+), 4 deletions(-)
```

## Arquivos tocados
- `.claude/tools/backlog.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T20-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_backlog.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `c974ad37333f770e8ae9fee449746602a730a348`
- Arquivos-alvo declarados: `.claude/tools/backlog.py`, `tests/test_backlog.py`
- Arquivos tocados: `.claude/tools/backlog.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T20-medida-depois.json`, `docs/telemetria.tsv`, `tests/test_backlog.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T20-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/backlog.py`
```
diff --git a/.claude/tools/backlog.py b/.claude/tools/backlog.py
index 54ee4fa..ecb2c39 100644
--- a/.claude/tools/backlog.py
+++ b/.claude/tools/backlog.py
@@ -2264,8 +2264,9 @@ def despachar(repo: Path, id_: str, mundo: str | None = None) -> ResultadoStatus
     # `DAF-42` (`AE-14`): os irmãos escrevem o stderr em UTF-8; sem `encoding` explícito o
     # texto sai na codificação do locale (cp1252 no Windows) — razão com mojibake, ou stderr
     # `None` quando um byte UTF-8 não existe em cp1252. Vale para os quatro `subprocess.run`.
+    # `R-04` (`DRF-14` do `P-0755`): o despacho julga só a `## 1`; a `## 1A` fica para o marco.
     resultado_modelo = subprocess.run(
-        [sys.executable, str(irmao / "modelo.py"), "check", "--plano", plano_abs, "--root", str(repo)],
+        [sys.executable, str(irmao / "modelo.py"), "check", "--plano", plano_abs, "--root", str(repo), "--so-vigente"],
         capture_output=True,
         text=True,
         encoding="utf-8",

```

### `tests/test_backlog.py`
```
diff --git a/tests/test_backlog.py b/tests/test_backlog.py
index 7d11fbd..e5358fe 100644
--- a/tests/test_backlog.py
+++ b/tests/test_backlog.py
@@ -3347,3 +3347,133 @@ def test_tr_ancoras_marcam_ausente_a_linha_citada_que_sumiu(tmp_path, capsys):
     assert "- src/alvo.py:2 — def alvo():" in pacote
     assert "- âncora ausente: texto que sumiu" in pacote
     assert "- âncora ausente: src/alvo.py:9" in pacote
+
+
+_GAM_PLANO_COM_PENDENTE_TEXTO = """# P-0 — Plano gama
+
+**Prefixo das tarefas no diário:** `GAM-T<n>`
+
+## 1. Modelo conceitual
+
+**Estado do modelo:** versão 1 · 2026-01-01 · autor: modelador · 1 operações · 2 propriedades · situação: vigente
+
+### 1.1 Objetos
+
+| objeto | o que é | propriedades | contrato | origem | lastro |
+|---|---|---|---|---|---|
+| insumo | dado de entrada | status | um registro por rodada | externo | lastro da fixture |
+| produto | o produto da primeira operação | status | um registro validado | OP-1 | lastro da fixture |
+
+### 1.2 Fluxo de operações
+
+- **OP-1** — Primeira operação da fixture.
+  - `precisa de: insumo` · `altera: produto.status` · `tarefas: GAM-T1, GAM-T2`
+
+### 1.3 Estado inicial e estado final
+
+| propriedade | estado inicial | estado final |
+|---|---|---|
+| insumo.status | lido | lido |
+| produto.status | rascunho | validado |
+
+### 1.4 Registro de versões
+
+| versão | data | situação | por |
+|---|---|---|---|
+| 1 | 2026-01-01 | vigente | modelador |
+| 2 | 2026-01-02 | pendente | modelador, emenda |
+
+## 1A. Modelo conceitual — versão pendente de validação
+
+**Estado do modelo:** versão 2 · 2026-01-02 · autor: modelador · 2 operações · 3 propriedades · situação: pendente
+
+### 1.1 Objetos
+
+| objeto | o que é | propriedades | contrato | origem | lastro |
+|---|---|---|---|---|---|
+| insumo | dado de entrada | status | um registro por rodada | externo | lastro da fixture |
+| produto | o produto da primeira operação | status | um registro validado | OP-1 | lastro da fixture |
+| resultado | o produto da segunda operação | nível | um relatório derivado | OP-2 | lastro da fixture |
+
+### 1.2 Fluxo de operações
+
+- **OP-1** — Primeira operação da fixture.
+  - `precisa de: insumo` · `altera: produto.status` · `tarefas: GAM-T1, GAM-T2`
+- **OP-2** — Segunda operação, nova na versão pendente.
+  - `precisa de: produto` · `altera: resultado.nível` · `tarefas: `
+
+### 1.3 Estado inicial e estado final
+
+| propriedade | estado inicial | estado final |
+|---|---|---|
+| insumo.status | lido | lido |
+| produto.status | rascunho | validado |
+| resultado.nível | inicial | alto |
+
+## 5. Tarefas
+
+### GAM-T1 — Primeira tarefa [Sonnet · classe implementacao]
+- **Objetivo:** fixture.
+- **Operação do modelo:** `OP-1`
+  - OP-1: Primeira operação da fixture.
+  - precisa de: insumo — um registro por rodada
+- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
+- **Verificação:**
+  1. `python -c "print('a')"` → `b` — antes `a`, depois `b`
+- **Pronto quando:** fixture existe.
+
+### GAM-T2 — Segunda tarefa [Sonnet · classe implementacao]
+- **Objetivo:** fixture.
+@OPERACAO_GAM_T2@- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
+- **Verificação:**
+  1. `python -c "print('a')"` → `b` — antes `a`, depois `b`
+- **Pronto quando:** fixture existe.
+"""
+
+_OPERACAO_GAM_T2 = """- **Operação do modelo:** `OP-1`
+  - OP-1: Primeira operação da fixture.
+  - precisa de: insumo — um registro por rodada
+"""
+
+
+def _montar_repo_despachar_com_pendente(tmp_path: Path, operacao_gam_t2: str) -> Path:
+    """RAF-T20 (`DRF-1`, `DRF-14`) — plano gama com uma `## 1A` pendente ao lado da `## 1`
+    vigente, para provar que `despachar` pede ao `modelo.py check` só o julgamento da versão
+    vigente (`--so-vigente`). Reaproveita `_montar_repo_despachar` e sobrescreve o
+    `plano.md` da cópia; o `modelo.py check` carrega o `backlog.py` da raiz dada por `--root`,
+    por isso a cópia também ganha o `backlog.py` do repositóri
```
[truncado em 4000 caracteres]

## Linhas removidas dos testes
### `tests/test_backlog.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T20-medida-depois.json; mundo: depois; gerado em: 2026-09-29T20:29:02+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_backlog.py -q -k versao_vigente` | 0 | true |

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
