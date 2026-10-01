# Evidência de revisão — P-0755 RAF-T19

## Diff (`git diff --stat`)
```
.claude/tools/modelo.py                            |  28 +++-
 docs/DIARIO_DE_OBRAS.md                            |   4 +-
 .../estado.tsv                                     |   2 +-
 .../evidencia/P-0755-RAF-T19-medida-depois.json    |  15 ++
 docs/telemetria.tsv                                |   3 +
 tests/test_modelo.py                               | 168 +++++++++++++++++++++
 6 files changed, 212 insertions(+), 8 deletions(-)
```

## Arquivos tocados
- `.claude/tools/modelo.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T19-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_modelo.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `5e35c55946ccbf8001236b0f977f487afc1d7127`
- Arquivos-alvo declarados: `.claude/tools/modelo.py`, `tests/test_modelo.py`
- Arquivos tocados: `.claude/tools/modelo.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T19-medida-depois.json`, `docs/telemetria.tsv`, `tests/test_modelo.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T19-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/modelo.py`
```
diff --git a/.claude/tools/modelo.py b/.claude/tools/modelo.py
index 987c404..0f8dcf3 100644
--- a/.claude/tools/modelo.py
+++ b/.claude/tools/modelo.py
@@ -317,7 +317,12 @@ def _tem_subbullets(item_texto: str, op_id: str) -> bool:
 
 
 def validar(
-    modelo: Modelo, plano, modelo_pendente: Modelo | None = None, *, pendente: bool = False
+    modelo: Modelo,
+    plano,
+    modelo_pendente: Modelo | None = None,
+    *,
+    pendente: bool = False,
+    so_vigente: bool = False,
 ) -> list[str]:
     violacoes_op: list[str] = []
     violacoes_objeto: list[str] = []
@@ -326,6 +331,10 @@ def validar(
     ids_tarefas = {t.id for t in plano.tarefas}
     nomes_objetos = {o.nome for o in modelo.objetos}
     numeros_operacoes = {op.numero for op in modelo.operacoes}
+    # DRF-37 (P-0755): operação que só existe na versão pendente ainda cobre a tarefa que a cita.
+    numeros_pendente = (
+        {op.numero for op in modelo_pendente.operacoes} if modelo_pendente is not None else set()
+    )
     origem_por_objeto = {o.nome: o.origem for o in modelo.objetos}
     propriedades_por_objeto = {o.nome: set(o.propriedades) for o in modelo.objetos}
     propriedades_com_estado = {chave for chave, _, _ in modelo.estado}
@@ -348,7 +357,11 @@ def validar(
         if situacoes_versoes.count("vigente") != 1:
             violacoes_op.append("V19 secao — registro de versões sem vigente único")
 
-        if modelo_pendente is not None and modelo_pendente.versao != modelo.versao + 1:
+        if (
+            modelo_pendente is not None
+            and not so_vigente
+            and modelo_pendente.versao != modelo.versao + 1
+        ):
             violacoes_op.append("V20 secao — versão pendente fora de sequência")
 
     numeros_vistos: set[int] = set()
@@ -416,7 +429,7 @@ def validar(
             for op_id in ops_citadas or []:
                 mo = _ORIGEM_OP_RE.match(op_id)
                 numero = int(mo.group(1)) if mo else None
-                if numero not in numeros_operacoes:
+                if numero not in numeros_operacoes and numero not in numeros_pendente:
                     violacoes_id.append(f"V4 {item.id} — operação inexistente {op_id}")
                 if not _tem_subbullets(item.texto, op_id):
                     violacoes_id.append(f"V14 {item.id} — contrato ausente para {op_id}")
@@ -583,8 +596,8 @@ def verbo_check(args: argparse.Namespace) -> int:
 
     backlog = _load_backlog(root)
     plano = backlog._parse_plano(plano_path, root)
-    violacoes = validar(modelo, plano, modelo_pendente)
-    if modelo_pendente is not None:
+    violacoes = validar(modelo, plano, modelo_pendente, so_vigente=args.so_vigente)
+    if modelo_pendente is not None and not args.so_vigente:
         violacoes = violacoes + [
             f"1A: {linha}" for linha in validar(modelo_pendente, plano, pendente=True)
         ]
@@ -707,6 +720,11 @@ def main(argv: list[str] | None = None) -> int:
     p_check = sub.add_parser("check")
     p_check.add_argument("--plano", required=True, help="Caminho do .md do plano.")
     p_check.add_argument("--root", default=_default_root(), help="Raiz do repositório.")
+    p_check.add_argument(
+        "--so-vigente",
+        action="store_true",
+        help="Julga só a '## 1' (versão vigente); a '## 1A' fica para o marco (R-04).",
+    )
     p_check.set_defaults(func=verbo_check)
 
     p_show = sub.add_parser("show")

```

### `tests/test_modelo.py`
```
diff --git a/tests/test_modelo.py b/tests/test_modelo.py
index 664cfc6..8383770 100644
--- a/tests/test_modelo.py
+++ b/tests/test_modelo.py
@@ -28,6 +28,7 @@ from __future__ import annotations
 
 import importlib.util
 import re
+import shutil
 import sys
 from pathlib import Path
 from types import SimpleNamespace
@@ -624,3 +625,170 @@ def test_tf_show_plano_inexistente_sai_2_sem_traceback(tmp_path, capsys):
 
     assert codigo == 2
     assert "modelo: plano não encontrado 'TK-74'" in capsys.readouterr().out
+
+
+_MODELO_PENDENTE_TEXTO = """# P-0999 — Plano com versão pendente
+**Prefixo das tarefas no diário:** `EX-T<n>`
+
+## 1. Modelo conceitual
+
+**Estado do modelo:** versão 1 · 2026-09-10 · autor: modelador · 1 operações · 2 propriedades · situação: vigente
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
+  - `precisa de: insumo` · `altera: produto.status` · `tarefas: EX-T1`
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
+| 1 | 2026-09-10 | vigente | modelador |
+| 2 | 2026-09-21 | pendente | modelador, emenda |
+
+## 1A. Modelo conceitual — versão pendente de validação
+
+**Estado do modelo:** versão 2 · 2026-09-21 · autor: modelador · 2 operações · 3 propriedades · situação: pendente
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
+  - `precisa de: insumo` · `altera: produto.status` · `tarefas: EX-T1`
+- **OP-2** — Segunda operação, nova na versão pendente.
+  - `precisa de: produto` · `altera: resultado.nível` · `tarefas: @TAREFAS_OP2@`
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
+### EX-T1 — Um [Sonnet · classe mecanica]
+- **Operação do modelo:** `OP-1`
+  - OP-1: @TEXTO_OP1@
+  - precisa de: insumo — um registro por rodada
+"""
+
+_CARD_OP2_TEXTO = """
+### EX-T2 — Dois [Sonnet · classe mecanica]
+- **Operação do modelo:** `@OP_CARD2@`
+  - @OP_CARD2@: @TEXTO_OP2@
+  - precisa de: produto — um registro validado
+"""
+
+
+def _raiz_modelo_pendente(
+    tmp_path: Path,
+    tarefas_op2: str = "",
+    card_op2: bool = False,
+    texto_op1: str = "Primeira operação da fixture.",
+    texto_op2: str = "Segunda operação, nova na versão pendente.",
+    op_card2: str = "OP-2",
+) -> tuple[Path, Path]:
+    """RAF-T19: raiz sintética com cópias de `backlog.py`/`caminhos.py` e um plano com versão
+    pendente (`## 1A`), para exercitar `--so-vigente` sem depender de `## 1A` existir no plano
+    real (a versão 2 do modelo foi promovida a vigente no Marco 3)."""
+    raiz = tmp_path / "raiz"
+    ferramentas = raiz / ".claude" / "tools"
+    ferramentas.mkdir(parents=True)
+    shutil.copy2(_ROOT / ".claude" / "tools" / "backlog.py", ferramentas / "backlog.py")
+    shutil.copy2(_ROOT / ".claude" / "tools" / "caminhos.py", ferramentas / "caminhos.py")
+
+    texto = _MODELO_PENDENTE_TEXTO.replace("@TAREFAS_OP2@", tarefas_op2).replace(

```
[truncado em 4000 caracteres]

## Linhas removidas dos testes
### `tests/test_modelo.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T19-medida-depois.json; mundo: depois; gerado em: 2026-09-29T19:58:31+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_modelo.py -q -k so_vigente` | 0 | true |

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
