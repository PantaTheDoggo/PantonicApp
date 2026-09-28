# Evidência de revisão — P-0753 AF-T14

## Diff (`git diff --stat`)
```
.claude/tools/modelo.py                            | 52 ++++++++-----
 docs/DIARIO_DE_OBRAS.md                            |  4 +-
 docs/plans/P-0753-auditoria-estagio-1/estado.tsv   |  2 +-
 .../evidencia/P-0753-AF-T14-medida.json            | 43 ++++++++++
 docs/telemetria.tsv                                |  1 +
 tests/fixtures/modelo/fluxo-pendente-contrato.md   | 91 ++++++++++++++++++++++
 tests/test_modelo.py                               | 35 +++++++++
 7 files changed, 204 insertions(+), 24 deletions(-)
```

## Arquivos tocados
- `.claude/tools/modelo.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T14-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/modelo/fluxo-pendente-contrato.md` — atribuição: da entrega; estado git: `??`
- `tests/test_modelo.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `f824f7585adc32805b4553f2468337b9678a48b9`
- Arquivos-alvo declarados: `.claude/tools/modelo.py`, `tests/test_modelo.py`, `tests/fixtures/modelo/fluxo-pendente-contrato.md`
- Arquivos tocados: `.claude/tools/modelo.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T14-medida.json`, `docs/telemetria.tsv`, `tests/fixtures/modelo/fluxo-pendente-contrato.md`, `tests/test_modelo.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T14-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/modelo.py`
```
diff --git a/.claude/tools/modelo.py b/.claude/tools/modelo.py
index 3571d95..987c404 100644
--- a/.claude/tools/modelo.py
+++ b/.claude/tools/modelo.py
@@ -316,7 +316,9 @@ def _tem_subbullets(item_texto: str, op_id: str) -> bool:
     return False
 
 
-def validar(modelo: Modelo, plano, modelo_pendente: Modelo | None = None) -> list[str]:
+def validar(
+    modelo: Modelo, plano, modelo_pendente: Modelo | None = None, *, pendente: bool = False
+) -> list[str]:
     violacoes_op: list[str] = []
     violacoes_objeto: list[str] = []
     violacoes_id: list[str] = []
@@ -332,21 +334,22 @@ def validar(modelo: Modelo, plano, modelo_pendente: Modelo | None = None) -> lis
         not modelo.cabecalho_presente
         or not modelo.tabela_objetos
         or not modelo.tabela_estado
-        or not modelo.tabela_versoes
+        or (not pendente and not modelo.tabela_versoes)
     ):
         violacoes_op.append(
             "V13 secao — cabeçalho, objetos, estado ou registro de versões ausente"
         )
 
-    situacoes_versoes = [
-        _parse_linha_tabela(linha)[2] if len(_parse_linha_tabela(linha)) >= 3 else ""
-        for linha in modelo.versoes
-    ]
-    if situacoes_versoes.count("vigente") != 1:
-        violacoes_op.append("V19 secao — registro de versões sem vigente único")
+    if not pendente:
+        situacoes_versoes = [
+            _parse_linha_tabela(linha)[2] if len(_parse_linha_tabela(linha)) >= 3 else ""
+            for linha in modelo.versoes
+        ]
+        if situacoes_versoes.count("vigente") != 1:
+            violacoes_op.append("V19 secao — registro de versões sem vigente único")
 
-    if modelo_pendente is not None and modelo_pendente.versao != modelo.versao + 1:
-        violacoes_op.append("V20 secao — versão pendente fora de sequência")
+        if modelo_pendente is not None and modelo_pendente.versao != modelo.versao + 1:
+            violacoes_op.append("V20 secao — versão pendente fora de sequência")
 
     numeros_vistos: set[int] = set()
     for posicao, operacao in enumerate(modelo.operacoes, start=1):
@@ -405,17 +408,18 @@ def validar(modelo: Modelo, plano, modelo_pendente: Modelo | None = None) -> lis
             if mo is None or int(mo.group(1)) not in numeros_operacoes:
                 violacoes_objeto.append(f"V7 objeto — origem inexistente {objeto.nome}")
 
-    for item in plano.tarefas:
-        ops_citadas = campo_operacoes(item.texto)
-        if not ops_citadas:
-            violacoes_id.append(f"V2 {item.id} — tarefa sem operação")
-        for op_id in ops_citadas or []:
-            mo = _ORIGEM_OP_RE.match(op_id)
-            numero = int(mo.group(1)) if mo else None
-            if numero not in numeros_operacoes:
-                violacoes_id.append(f"V4 {item.id} — operação inexistente {op_id}")
-            if not _tem_subbullets(item.texto, op_id):
-                violacoes_id.append(f"V14 {item.id} — contrato ausente para {op_id}")
+    if not pendente:
+        for item in plano.tarefas:
+            ops_citadas = campo_operacoes(item.texto)
+            if not ops_citadas:
+                violacoes_id.append(f"V2 {item.id} — tarefa sem operação")
+            for op_id in ops_citadas or []:
+                mo = _ORIGEM_OP_RE.match(op_id)
+                numero = int(mo.group(1)) if mo else None
+                if numero not in numeros_operacoes:
+                    violacoes_id.append(f"V4 {item.id} — operação inexistente {op_id}")
+                if not _tem_subbullets(item.texto, op_id):
+                    violacoes_id.append(f"V14 {item.id} — contrato ausente para {op_id}")
 
     return violacoes_op + violacoes_objeto + violacoes_id
 
@@ -470,6 +474,8 @@ def _diff_objetos(vigente: Modelo, pendente: Modelo) -> list[str]:
                 f"[~] {nome} — {', '.join(objeto_v.propriedades)} => "
                 f"{', '.join(objeto_p.propriedades)}"
             )
+        if objeto_p is not None and objeto_v.contrato != objeto_p.contrato:
+    
```
[truncado em 4000 caracteres]

### `tests/test_modelo.py`
```
diff --git a/tests/test_modelo.py b/tests/test_modelo.py
index 37a95fa..664cfc6 100644
--- a/tests/test_modelo.py
+++ b/tests/test_modelo.py
@@ -44,6 +44,7 @@ _PLANO_SEM_ESTADO = _FIXTURES / "plano-sem-estado.md"
 _FLUXO_VALIDO = _FIXTURES / "fluxo-valido.md"
 _FLUXO_CONCLUIDO = _FIXTURES / "fluxo-concluido.md"
 _FLUXO_PENDENTE = _FIXTURES / "fluxo-pendente.md"
+_FLUXO_PENDENTE_CONTRATO = _FIXTURES / "fluxo-pendente-contrato.md"
 _PLANO_SEM_LASTRO = _FIXTURES / "plano-sem-lastro.md"
 _PLANO_COM_LASTRO = _FIXTURES / "plano-com-lastro.md"
 _PLANO_TERMINAL_SEM_LASTRO = _FIXTURES / "plano-terminal-sem-lastro.md"
@@ -389,6 +390,22 @@ def test_tf_check_objeto_sem_lastro_nao_alcanca_status_terminal_v21():
     assert not any(v.startswith("V21") for v in violacoes)
 
 
+def test_tf_check_pendente_roda_o_vocabulario(capsys):
+    """`fluxo-pendente-contrato.md` tem, no bloco `## 1A`, a `OP-3` citando o objeto inexistente
+    `objeto fantasma` — `check` passa a julgar a versão pendente pelo mesmo vocabulário da
+    vigente (`OP-14`) e sai 1 com a violação prefixada `1A: ` (a regra de hoje, que não julga a
+    pendente, sairia 0)."""
+    modelo = _load_modelo()
+
+    codigo = modelo.main(
+        ["check", "--plano", str(_FLUXO_PENDENTE_CONTRATO), "--root", str(_ROOT)]
+    )
+    saida = capsys.readouterr()
+
+    assert codigo == 1
+    assert "1A: V5 OP-3 — objeto inexistente objeto fantasma" in saida.err
+
+
 def test_tf_check_forma_anterior_sai_dois(capsys):
     """`plano-forma-anterior.md` tem `## 1. Modelo conceitual`, mas não tem `### 1.2 Fluxo de
     operações` (é a forma de orações da `MC-T2`) — `check` sai 2 com a substring `modelo: forma
@@ -575,6 +592,24 @@ def test_tf_show_drift_sem_diferenca():
     assert resultado == "sem drift"
 
 
+def test_tf_drift_mostra_contrato_alterado(capsys):
+    """`fluxo-pendente-contrato.md` muda o contrato de `resultado um` entre vigente e pendente,
+    sem mudar as propriedades — `--drift` acrescenta a linha de contrato (`OP-14`; a regra de
+    hoje não imprime linha de objeto nenhuma para ele, porque as propriedades não mudaram)."""
+    modelo = _load_modelo()
+
+    codigo = modelo.main(
+        ["show", "--plano", str(_FLUXO_PENDENTE_CONTRATO), "--drift", "--root", str(_ROOT)]
+    )
+    saida = capsys.readouterr()
+
+    assert codigo == 0
+    assert (
+        "[~] resultado um — contrato: um registro validado => um registro validado e datado"
+        in saida.out
+    )
+
+
 def test_tf_check_plano_inexistente_sai_2_sem_traceback(tmp_path, capsys):
     """TF da TK-74b: `check` com `--plano` que não é arquivo sai em uma linha com exit `2`."""
     codigo = _load_modelo().main(["check", "--plano", "TK-74", "--root", str(tmp_path)])

```

### `tests/fixtures/modelo/fluxo-pendente-contrato.md`
```
# EX-0005 — Plano de exemplo de fluxo válido
**Status:** `in-progress`
**Prefixo das tarefas no diário:** `EX-T<n>`

## 1. Modelo conceitual

**Estado do modelo:** versão 1 · 2026-09-20 · autor: planejador · 3 operações · 4 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem | lastro |
|---|---|---|---|---|---|
| insumo externo | dado de entrada do fluxo de exemplo | status | um registro por rodada | externo | lastro sintético da fixture |
| resultado um | o produto da primeira operação | status | um registro validado | OP-1 | lastro sintético da fixture |
| resultado dois | o produto da segunda operação | status | um relatório derivado | OP-2 | lastro sintético da fixture |
| registro auxiliar | apoio usado só pela terceira operação | status | uma nota de apoio | externo | lastro sintético da fixture |

### 1.2 Fluxo de operações

- **OP-1** — Primeira operação do fluxo de exemplo.
  - `precisa de: insumo externo` · `altera: resultado um.status` · `tarefas: EX-T1`
- **OP-2** — Segunda operação do fluxo de exemplo.
  - `precisa de: resultado um` · `altera: resultado dois.status` · `tarefas: EX-T2`
- **OP-3** — Terceira operação do fluxo de exemplo.
  - `precisa de: resultado dois, registro auxiliar` · `altera: registro auxiliar.status` · `tarefas: EX-T3`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final |
|---|---|---|
| insumo externo.status | recebido | processado |
| resultado um.status | rascunho | validado |
| resultado dois.status | rascunho | validado |
| registro auxiliar.status | aberto | encerrado |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 1 | 2026-09-20 | vigente | planejador |

## 1A. Modelo conceitual — versão pendente de validação

**Estado do modelo:** versão 2 · 2026-09-27 · autor: modelador · 3 operações · 4 propriedades · situação: pendente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem | lastro |
|---|---|---|---|---|---|
| insumo externo | dado de entrada do fluxo de exemplo | status | um registro por rodada | externo | lastro sintético da fixture |
| resultado um | o produto da primeira operação | status | um registro validado e datado | OP-1 | lastro sintético da fixture |
| resultado dois | o produto da segunda operação | status | um relatório derivado | OP-2 | lastro sintético da fixture |
| registro auxiliar | apoio usado só pela terceira operação | status | uma nota de apoio | externo | lastro sintético da fixture |

### 1.2 Fluxo de operações

- **OP-1** — Primeira operação do fluxo de exemplo.
  - `precisa de: insumo externo` · `altera: resultado um.status` · `tarefas: EX-T1`
- **OP-2** — Segunda operação do fluxo de exemplo.
  - `precisa de: resultado um` · `altera: resultado dois.status` · `tarefas: EX-T2`
- **OP-3** — Terceira operação do fluxo de exemplo.
  - `precisa de: resultado dois, registro auxiliar, objeto fantasma` · `altera: registro auxiliar.status` · `tarefas: EX-T3`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final |
|---|---|---|
| insumo externo.status | recebido | processado |
| resultado um.status | rascunho | validado |
| resultado dois.status | rascunho | validado |
| registro auxiliar.status | aberto | encerrado |

## 4. Tarefas

### EX-T1 — Um [Sonnet · classe mecanica]
- **Status:** `done` · 2026-09-20
- **Operação do modelo:** `OP-1`
  - OP-1: Primeira operação do fluxo de exemplo.
  - precisa de: insumo externo — um registro por rodada

### EX-T2 — Dois [Sonnet · classe mecanica]
- **Status:** `in-progress` · 2026-09-20
- **Operação do modelo:** `OP-2`
  - OP-2: Segunda operação do fluxo de exemplo.
  - precisa de: resultado um — um registro validado

### EX-T3 — Três [Sonnet · classe mecanica]
- **Status:** `ready` · 2026-09-20
- **Operação do modelo:** `OP-3`
  - OP-3: Terceira operação do fluxo de exemplo.
  - precisa de: resultado dois — um relatório derivado; registro auxiliar 
```
[truncado em 4000 caracteres]

## Medida do executor
- Arquivo: docs\plans\P-0753-auditoria-estagio-1\evidencia\P-0753-AF-T14-medida.json; mundo: depois; gerado em: 2026-09-27T16:03:45+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_modelo.py -q -k "pendente_roda_o_vocabulario or drift_mostra_contrato"` | 0 | true |
| 2 | `python .claude/tools/modelo.py check --plano tests/fixtures/modelo/fluxo-pendente-contrato.md` | 1 | true |
| 3 | `python .claude/tools/modelo.py show --plano tests/fixtures/modelo/fluxo-pendente-contrato.md --drift` | 0 | true |
| 4 | `python -m pytest -q` | 0 | true |
| 5 | `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
