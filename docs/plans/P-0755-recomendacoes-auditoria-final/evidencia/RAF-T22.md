# Evidência de revisão — P-0755 RAF-T22

## Diff (`git diff --stat`)
```
.claude/tools/modelo.py                            | 62 ++++++++++++++++------
 docs/DIARIO_DE_OBRAS.md                            |  4 +-
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T22-medida-depois.json    | 15 ++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_modelo.py                               | 60 +++++++++++++++++++++
 6 files changed, 125 insertions(+), 19 deletions(-)
```

## Arquivos tocados
- `.claude/tools/modelo.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T22-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_modelo.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `2a3eda0a8f71e98021e71e45008358245c4f5802`
- Arquivos-alvo declarados: `.claude/tools/modelo.py`, `tests/test_modelo.py`
- Arquivos tocados: `.claude/tools/modelo.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T22-medida-depois.json`, `docs/telemetria.tsv`, `tests/test_modelo.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T22-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/modelo.py`
```
diff --git a/.claude/tools/modelo.py b/.claude/tools/modelo.py
index 6b4fc3c..7adc0a7 100644
--- a/.claude/tools/modelo.py
+++ b/.claude/tools/modelo.py
@@ -498,10 +498,6 @@ def _obj_por_nome(modelo: Modelo) -> dict[str, Objeto]:
     return {o.nome: o for o in modelo.objetos}
 
 
-def _op_por_numero(modelo: Modelo) -> dict[int, Operacao]:
-    return {op.numero: op for op in modelo.operacoes}
-
-
 def _estado_por_chave(modelo: Modelo) -> dict[str, tuple[str, str]]:
     return {chave: (inicial, final) for chave, inicial, final in modelo.estado}
 
@@ -529,26 +525,60 @@ def _diff_objetos(vigente: Modelo, pendente: Modelo) -> list[str]:
 
 
 def _diff_fluxo(vigente: Modelo, pendente: Modelo) -> list[str]:
-    ops_vigente = _op_por_numero(vigente)
-    ops_pendente = _op_por_numero(pendente)
+    """Compara o fluxo de operações entre duas versões do modelo (R-07, DRF-16 do `P-0755`): casa
+    em duas rodadas — primeiro por texto igual, na ordem; o que sobra casa por número — para que a
+    inserção de uma operação não apareça como uma cascata de alterações em cadeia."""
+    pareada_de: dict[int, Operacao] = {}  # índice em pendente.operacoes -> operação vigente pareada
+    vigente_pareada: set[int] = set()  # índices em vigente.operacoes já pareados
+
+    for i, operacao_p in enumerate(pendente.operacoes):
+        for j, operacao_v in enumerate(vigente.operacoes):
+            if j in vigente_pareada:
+                continue
+            if operacao_v.texto == operacao_p.texto:
+                pareada_de[i] = operacao_v
+                vigente_pareada.add(j)
+                break
+
+    for i, operacao_p in enumerate(pendente.operacoes):
+        if i in pareada_de:
+            continue
+        for j, operacao_v in enumerate(vigente.operacoes):
+            if j in vigente_pareada:
+                continue
+            if operacao_v.numero == operacao_p.numero:
+                pareada_de[i] = operacao_v
+                vigente_pareada.add(j)
+                break
+
     linhas: list[str] = []
-    for numero, operacao in ops_pendente.items():
-        if numero not in ops_vigente:
-            linhas.append(f"[+] OP-{numero} — {operacao.texto}")
-    for numero, operacao in ops_vigente.items():
-        if numero not in ops_pendente:
-            linhas.append(f"[-] OP-{numero} — {operacao.texto}")
-    for numero, operacao_v in ops_vigente.items():
-        operacao_p = ops_pendente.get(numero)
-        if operacao_p is not None and operacao_v.texto != operacao_p.texto:
-            linhas.append(f"[~] OP-{numero} — {operacao_v.texto} => {operacao_p.texto}")
+    for i, operacao_p in enumerate(pendente.operacoes):
+        operacao_v = pareada_de.get(i)
+        if operacao_v is None:
+            linhas.append(f"[+] OP-{operacao_p.numero} — {operacao_p.texto}")
+        elif operacao_v.texto == operacao_p.texto and operacao_v.numero != operacao_p.numero:
+            linhas.append(f"[=] OP-{operacao_p.numero} (era OP-{operacao_v.numero})")
+        elif operacao_v.texto != operacao_p.texto:
+            linhas.append(
+                f"[~] OP-{operacao_p.numero} — {operacao_v.texto} => {operacao_p.texto}"
+            )
+    for j, operacao_v in enumerate(vigente.operacoes):
+        if j not in vigente_pareada:
+            linhas.append(f"[-] OP-{operacao_v.numero} — {operacao_v.texto}")
     return linhas
 
 
 def _diff_estado(vigente: Modelo, pendente: Modelo) -> list[str]:
+    # DRF-16 (P-0755): antes das alterações, a propriedade que só uma das versões tem.
     estado_vigente = _estado_por_chave(vigente)
     estado_pendente = _estado_por_chave(pendente)
     linhas: list[str] = []
+    for chave, _, final_p in pendente.estado:
+        if chave not in estado_vigente:
+            linhas.append(f"[+] {chave} — {final_p}")
+    for chave, _, final_v in vigente.estado:
+        if chave not in estado_pendente:
+            linhas.append(f"[-] {chave} — {final_v}")
     for chave, (_, final_v) in estado_
```
[truncado em 4000 caracteres]

### `tests/test_modelo.py`
```
diff --git a/tests/test_modelo.py b/tests/test_modelo.py
index 5bbd368..2636129 100644
--- a/tests/test_modelo.py
+++ b/tests/test_modelo.py
@@ -887,3 +887,63 @@ def test_tf_texto_divergente_v22_da_pendente(tmp_path, capsys):
 
     assert codigo == 1
     assert "V22 EX-T2 — texto de OP-2 diverge da versão 2" in saida.err
+
+
+def _modelo_drift(modelo, textos: list[str], estado: list[tuple[str, str, str]], versao: int):
+    """Monta um `Modelo` sintético para os testes de drift entre versões (RAF-T22): operações
+    `OP-1`..`OP-n` na ordem de `textos`, sem `precisa_de`/`altera`/`tarefas`."""
+    operacoes = [
+        modelo.Operacao(numero=numero, texto=texto)
+        for numero, texto in enumerate(textos, start=1)
+    ]
+    return modelo.Modelo(versao=versao, data="2026-09-28", operacoes=operacoes, estado=estado)
+
+
+def test_tf_drift_versoes_insercao_mostra_nova_e_renumerada():
+    """TF (RAF-T22, R-07/DRF-16): a pendente insere `Nova.` entre `Primeira.` e `Segunda.` — o
+    casamento por texto primeiro reconhece `Segunda.` como a mesma operação renumerada (`[=] OP-3
+    (era OP-2)`) e só `Nova.` sai como inserção (`[+] OP-2`); hoje, casando só por número, sairiam
+    `[+] OP-3 — Segunda.` e `[~] OP-2 — Segunda. => Nova.`."""
+    modelo = _load_modelo()
+    vigente = _modelo_drift(modelo, ["Primeira.", "Segunda."], [], 1)
+    pendente = _modelo_drift(modelo, ["Primeira.", "Nova.", "Segunda."], [], 2)
+
+    resultado = modelo.montar_drift(vigente, pendente)
+    linhas = resultado.splitlines()
+
+    assert "[+] OP-2 — Nova." in linhas
+    assert "[=] OP-3 (era OP-2)" in linhas
+    assert not any(linha.startswith("[~] OP-") or linha.startswith("[-] OP-") for linha in linhas)
+
+
+def test_tr_drift_versoes_texto_alterado_segue_por_numero():
+    """TR (RAF-T22): sem par de texto igual, `OP-1` casa por número entre as duas versões e sai
+    como alteração (`[~]`) — a regra concorrente, casar só por texto, daria `[+] OP-1` (pendente)
+    e `[-] OP-1` (vigente) por não achar par nenhum."""
+    modelo = _load_modelo()
+    vigente = _modelo_drift(modelo, ["Primeira."], [], 1)
+    pendente = _modelo_drift(modelo, ["Primeira, reescrita."], [], 2)
+
+    resultado = modelo.montar_drift(vigente, pendente)
+    linhas = resultado.splitlines()
+
+    assert "[~] OP-1 — Primeira. => Primeira, reescrita." in linhas
+    assert not any(linha.startswith("[+] OP-") or linha.startswith("[-] OP-") for linha in linhas)
+
+
+def test_tf_drift_versoes_propriedade_de_uma_versao_so():
+    """TF (RAF-T22, DRF-16): `x.c` só existe na vigente e `x.b` só existe na pendente — `_diff_estado`
+    hoje só mostra chave presente nas duas versões, então nenhuma das duas linhas aparecia."""
+    modelo = _load_modelo()
+    vigente = _modelo_drift(
+        modelo, ["Única."], [("x.a", "-", "fim"), ("x.c", "-", "baixo")], 1
+    )
+    pendente = _modelo_drift(
+        modelo, ["Única."], [("x.a", "-", "fim"), ("x.b", "-", "alto")], 2
+    )
+
+    resultado = modelo.montar_drift(vigente, pendente)
+    linhas = resultado.splitlines()
+
+    assert "[+] x.b — alto" in linhas
+    assert "[-] x.c — baixo" in linhas

```

## Linhas removidas dos testes
### `tests/test_modelo.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T22-medida-depois.json; mundo: depois; gerado em: 2026-09-29T21:02:07+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_modelo.py -q -k drift_versoes` | 0 | true |

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
