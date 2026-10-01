# Evidência de revisão — P-0755 RAF-T21

## Diff (`git diff --stat`)
```
.claude/tools/modelo.py                            | 39 ++++++++++++++-
 docs/ACIONAMENTOS_CONSULTOR.tsv                    |  1 +
 docs/DIARIO_DE_OBRAS.md                            |  4 +-
 .../cenario.md                                     | 18 ++++++-
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T21-medida-depois.json    | 15 ++++++
 .../P-0755-recomendacoes-auditoria-final/plano.md  |  9 ++--
 docs/telemetria.tsv                                |  3 ++
 tests/test_modelo.py                               | 57 ++++++++++++++++++++++
 9 files changed, 138 insertions(+), 10 deletions(-)
```

## Arquivos tocados
- `.claude/tools/modelo.py` — atribuição: da entrega; estado git: ` M`
- `docs/ACIONAMENTOS_CONSULTOR.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/cenario.md` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T21-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_modelo.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `a10ab41d56496deaa73ce64ec4446d735f41a214`
- Arquivos-alvo declarados: `.claude/tools/modelo.py`, `tests/test_modelo.py`
- Arquivos tocados: `.claude/tools/modelo.py`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/cenario.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T21-medida-depois.json`, `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`, `docs/telemetria.tsv`, `tests/test_modelo.py`
- Registro da orquestração (não atribuível a tarefa): `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/cenario.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T21-medida-depois.json`, `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/modelo.py`
```
diff --git a/.claude/tools/modelo.py b/.claude/tools/modelo.py
index 0f8dcf3..6b4fc3c 100644
--- a/.claude/tools/modelo.py
+++ b/.claude/tools/modelo.py
@@ -316,6 +316,14 @@ def _tem_subbullets(item_texto: str, op_id: str) -> bool:
     return False
 
 
+def _texto_copiado(item_texto: str, op_id: str) -> str | None:
+    prefixo = f"  - {op_id}: "
+    for linha in item_texto.splitlines():
+        if linha.startswith(prefixo):
+            return " ".join(linha[len(prefixo) :].split())
+    return None
+
+
 def validar(
     modelo: Modelo,
     plano,
@@ -335,6 +343,18 @@ def validar(
     numeros_pendente = (
         {op.numero for op in modelo_pendente.operacoes} if modelo_pendente is not None else set()
     )
+    # RAF-T21 (P-0755): textos da operação, colapsados, para conferir o texto copiado no card —
+    # todos os de mesmo número (DRF-61: número duplicado numa versão conta cada texto, não só o
+    # último).
+    textos_vigente_por_numero: dict[int, list[str]] = {}
+    for op in modelo.operacoes:
+        textos_vigente_por_numero.setdefault(op.numero, []).append(" ".join(op.texto.split()))
+    textos_pendente_por_numero: dict[int, list[str]] = {}
+    if modelo_pendente is not None:
+        for op in modelo_pendente.operacoes:
+            textos_pendente_por_numero.setdefault(op.numero, []).append(
+                " ".join(op.texto.split())
+            )
     origem_por_objeto = {o.nome: o.origem for o in modelo.objetos}
     propriedades_por_objeto = {o.nome: set(o.propriedades) for o in modelo.objetos}
     propriedades_com_estado = {chave for chave, _, _ in modelo.estado}
@@ -433,6 +453,22 @@ def validar(
                     violacoes_id.append(f"V4 {item.id} — operação inexistente {op_id}")
                 if not _tem_subbullets(item.texto, op_id):
                     violacoes_id.append(f"V14 {item.id} — contrato ausente para {op_id}")
+                if numero in numeros_operacoes or numero in numeros_pendente:
+                    texto_copiado = _texto_copiado(item.texto, op_id)
+                    if texto_copiado is not None:
+                        textos_validos = []
+                        textos_validos.extend(textos_vigente_por_numero.get(numero, []))
+                        textos_validos.extend(textos_pendente_por_numero.get(numero, []))
+                        if texto_copiado not in textos_validos:
+                            versao_ref = (
+                                modelo.versao
+                                if numero in numeros_operacoes
+                                else modelo_pendente.versao
+                            )
+                            violacoes_id.append(
+                                f"V22 {item.id} — texto de OP-{numero} diverge da versão "
+                                f"{versao_ref}"
+                            )
 
     return violacoes_op + violacoes_objeto + violacoes_id
 
@@ -710,7 +746,8 @@ def main(argv: list[str] | None = None) -> int:
     parser = argparse.ArgumentParser(
         description=(
             "modelo.py (P-0743): check julga a seção '## 1. Modelo conceitual' de um plano "
-            "contra o vocabulário de violações V1..V21 (### 16); show deriva a leitura do dono "
+            "contra o vocabulário de violações V1..V22 (### 16; V22 do P-0755); show deriva a "
+            "leitura do dono "
             "a partir do modelo real, abrindo pelo estágio atual, com --pendente para o bloco "
             "'## 1A' e --drift para a diferença entre a versão vigente e a pendente."
         )

```

### `tests/test_modelo.py`
```
diff --git a/tests/test_modelo.py b/tests/test_modelo.py
index 5ea1d3c..5bbd368 100644
--- a/tests/test_modelo.py
+++ b/tests/test_modelo.py
@@ -830,3 +830,60 @@ def test_tr_sem_so_vigente_pendente_fora_de_sequencia_segue_v20(tmp_path, capsys
 
     assert codigo == 1
     assert "V20 secao — versão pendente fora de sequência" in saida.err
+
+
+def test_tf_texto_divergente_v22_da_vigente(tmp_path, capsys):
+    """TF (RAF-T21): `tarefas_op2="EX-T2"`, `card_op2=True` e o `EX-T1` com o texto `Primeira
+    operação da fixture, na redação antiga.` — `check` sai 1 com `V22 EX-T1 — texto de OP-1
+    diverge da versão 1` no stderr (hoje sai 0)."""
+    modelo = _load_modelo()
+    raiz, plano = _raiz_modelo_pendente(
+        tmp_path,
+        tarefas_op2="EX-T2",
+        card_op2=True,
+        texto_op1="Primeira operação da fixture, na redação antiga.",
+    )
+
+    codigo = modelo.main(["check", "--plano", str(plano), "--root", str(raiz)])
+    saida = capsys.readouterr()
+
+    assert codigo == 1
+    assert "V22 EX-T1 — texto de OP-1 diverge da versão 1" in saida.err
+
+
+def test_tr_texto_divergente_so_em_espacos_nao_e_v22(tmp_path, capsys):
+    """TR (RAF-T21): o `EX-T1` com `Primeira  operação da fixture. ` (espaço duplo e espaço na
+    ponta) — `check` sai 0 (a regra concorrente, comparação literal, acusaria `V22`)."""
+    modelo = _load_modelo()
+    raiz, plano = _raiz_modelo_pendente(
+        tmp_path,
+        tarefas_op2="EX-T2",
+        card_op2=True,
+        texto_op1="Primeira  operação da fixture. ",
+    )
+
+    codigo = modelo.main(["check", "--plano", str(plano), "--root", str(raiz)])
+    saida = capsys.readouterr()
+
+    assert codigo == 0
+    assert "V22" not in saida.err
+
+
+def test_tf_texto_divergente_v22_da_pendente(tmp_path, capsys):
+    """TF (RAF-T21): o `EX-T2` com o texto `Outra redação da segunda operação.` — `check
+    --so-vigente` sai 1 com `V22 EX-T2 — texto de OP-2 diverge da versão 2` (hoje sai 0)."""
+    modelo = _load_modelo()
+    raiz, plano = _raiz_modelo_pendente(
+        tmp_path,
+        tarefas_op2="EX-T2",
+        card_op2=True,
+        texto_op2="Outra redação da segunda operação.",
+    )
+
+    codigo = modelo.main(
+        ["check", "--plano", str(plano), "--root", str(raiz), "--so-vigente"]
+    )
+    saida = capsys.readouterr()
+
+    assert codigo == 1
+    assert "V22 EX-T2 — texto de OP-2 diverge da versão 2" in saida.err

```

## Linhas removidas dos testes
### `tests/test_modelo.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T21-medida-depois.json; mundo: depois; gerado em: 2026-09-29T20:48:57+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_modelo.py -q -k texto_divergente` | 0 | true |

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
