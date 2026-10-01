# Evidência de revisão — P-0755 RAF-T22a

## Diff (`git diff --stat`)
```
.claude/tools/modelo.py                            | 15 +++++++++-
 docs/DIARIO_DE_OBRAS.md                            |  4 +--
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T22a-medida-depois.json   | 15 ++++++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_modelo.py                               | 32 ++++++++++++++++++++++
 6 files changed, 65 insertions(+), 4 deletions(-)
```

## Arquivos tocados
- `.claude/tools/modelo.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T22a-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_modelo.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `8590d1f9f11b9dbf74e22e4d7d5164df4935edde`
- Arquivos-alvo declarados: `.claude/tools/modelo.py`, `tests/test_modelo.py`
- Arquivos tocados: `.claude/tools/modelo.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T22a-medida-depois.json`, `docs/telemetria.tsv`, `tests/test_modelo.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T22a-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/modelo.py`
```
diff --git a/.claude/tools/modelo.py b/.claude/tools/modelo.py
index 7adc0a7..1595bda 100644
--- a/.claude/tools/modelo.py
+++ b/.claude/tools/modelo.py
@@ -527,7 +527,10 @@ def _diff_objetos(vigente: Modelo, pendente: Modelo) -> list[str]:
 def _diff_fluxo(vigente: Modelo, pendente: Modelo) -> list[str]:
     """Compara o fluxo de operações entre duas versões do modelo (R-07, DRF-16 do `P-0755`): casa
     em duas rodadas — primeiro por texto igual, na ordem; o que sobra casa por número — para que a
-    inserção de uma operação não apareça como uma cascata de alterações em cadeia."""
+    inserção de uma operação não apareça como uma cascata de alterações em cadeia. Para todo par
+    casado, depois da linha de texto (ou de nenhuma), compara `precisa_de` e `altera` — o contrato
+    da operação — e emite `[~] OP-<k> — precisa de: ...` / `[~] OP-<k> — altera: ...` quando a
+    lista muda, mesmo com texto e número iguais (AE-187, DRF-73 do `P-0755`)."""
     pareada_de: dict[int, Operacao] = {}  # índice em pendente.operacoes -> operação vigente pareada
     vigente_pareada: set[int] = set()  # índices em vigente.operacoes já pareados
 
@@ -562,6 +565,16 @@ def _diff_fluxo(vigente: Modelo, pendente: Modelo) -> list[str]:
             linhas.append(
                 f"[~] OP-{operacao_p.numero} — {operacao_v.texto} => {operacao_p.texto}"
             )
+        if operacao_v is not None and operacao_v.precisa_de != operacao_p.precisa_de:
+            linhas.append(
+                f"[~] OP-{operacao_p.numero} — precisa de: {', '.join(operacao_v.precisa_de)} "
+                f"=> {', '.join(operacao_p.precisa_de)}"
+            )
+        if operacao_v is not None and operacao_v.altera != operacao_p.altera:
+            linhas.append(
+                f"[~] OP-{operacao_p.numero} — altera: {', '.join(operacao_v.altera)} "
+                f"=> {', '.join(operacao_p.altera)}"
+            )
     for j, operacao_v in enumerate(vigente.operacoes):
         if j not in vigente_pareada:
             linhas.append(f"[-] OP-{operacao_v.numero} — {operacao_v.texto}")

```

### `tests/test_modelo.py`
```
diff --git a/tests/test_modelo.py b/tests/test_modelo.py
index 2636129..21fb6ad 100644
--- a/tests/test_modelo.py
+++ b/tests/test_modelo.py
@@ -947,3 +947,35 @@ def test_tf_drift_versoes_propriedade_de_uma_versao_so():
 
     assert "[+] x.b — alto" in linhas
     assert "[-] x.c — baixo" in linhas
+
+
+def test_tf_drift_contrato_da_operacao_mostra_precisa_e_altera():
+    """TF (RAF-T22a, AE-187/DRF-73): `OP-1` tem o mesmo texto e o mesmo número nas duas versões e
+    muda só `precisa de:` e `altera:` — o drift mostra as duas listas; hoje o par de texto igual não
+    emite linha nenhuma e `montar_drift` devolve `sem drift`."""
+    modelo = _load_modelo()
+    vigente = modelo.Modelo(versao=1, data="2026-09-28", operacoes=[
+        modelo.Operacao(numero=1, texto="Única.", precisa_de=["a"], altera=["x.a"]),
+    ])
+    pendente = modelo.Modelo(versao=2, data="2026-09-28", operacoes=[
+        modelo.Operacao(numero=1, texto="Única.", precisa_de=["a", "b"], altera=["x.a", "x.b"]),
+    ])
+
+    linhas = modelo.montar_drift(vigente, pendente).splitlines()
+
+    assert "[~] OP-1 — precisa de: a => a, b" in linhas
+    assert "[~] OP-1 — altera: x.a => x.a, x.b" in linhas
+
+
+def test_tr_drift_contrato_da_operacao_ignora_tarefas():
+    """TR (RAF-T22a, DRF-73): `OP-1` muda só `tarefas:`, que é lastro e não modelo — o drift segue
+    `sem drift`; a regra concorrente, comparar todo o sub-bullet, daria uma linha de `tarefas:`."""
+    modelo = _load_modelo()
+    vigente = modelo.Modelo(versao=1, data="2026-09-28", operacoes=[
+        modelo.Operacao(numero=1, texto="Única.", tarefas=["EX-T1"]),
+    ])
+    pendente = modelo.Modelo(versao=2, data="2026-09-28", operacoes=[
+        modelo.Operacao(numero=1, texto="Única.", tarefas=["EX-T1", "EX-T1a"]),
+    ])
+
+    assert modelo.montar_drift(vigente, pendente) == "sem drift"

```

## Linhas removidas dos testes
### `tests/test_modelo.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T22a-medida-depois.json; mundo: depois; gerado em: 2026-09-30T05:45:52+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_modelo.py -q -k drift_contrato_da_operacao` | 0 | true |

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
