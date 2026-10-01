# Evidência de revisão — P-0755 RAF-T19a

## Diff (`git diff --stat`)
```
docs/DIARIO_DE_OBRAS.md                            |  6 ++--
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T19a-medida-depois.json   | 15 +++++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_modelo.py                               | 38 ++++++++++++++++++++++
 5 files changed, 58 insertions(+), 4 deletions(-)
```

## Arquivos tocados
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T19a-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_modelo.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `945a87abfe7d76f25a1bd5d68561148fd2d0e7a3`
- Arquivos-alvo declarados: `tests/test_modelo.py`
- Arquivos tocados: `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T19a-medida-depois.json`, `docs/telemetria.tsv`, `tests/test_modelo.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T19a-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `tests/test_modelo.py`
```
diff --git a/tests/test_modelo.py b/tests/test_modelo.py
index 8383770..5ea1d3c 100644
--- a/tests/test_modelo.py
+++ b/tests/test_modelo.py
@@ -792,3 +792,41 @@ def test_tr_so_vigente_operacao_ausente_das_duas_segue_v4(tmp_path, capsys):
 
     assert codigo == 1
     assert "V4 EX-T2 — operação inexistente OP-9" in saida.err
+
+
+def _raiz_pendente_fora_de_sequencia(tmp_path: Path) -> tuple[Path, Path]:
+    """RAF-T19a: a raiz de `_raiz_modelo_pendente` com o card da `OP-2` e a `## 1A` em versão 3
+    contra a vigente 1, para que só a `V20` distinga o `check` com e sem `--so-vigente`."""
+    raiz, plano = _raiz_modelo_pendente(tmp_path, tarefas_op2="EX-T2", card_op2=True)
+    texto = plano.read_text(encoding="utf-8")
+    plano.write_text(
+        texto.replace("**Estado do modelo:** versão 2 ·", "**Estado do modelo:** versão 3 ·"),
+        encoding="utf-8",
+    )
+    return raiz, plano
+
+
+def test_tf_so_vigente_pendente_fora_de_sequencia_nao_e_v20(tmp_path, capsys):
+    """TF (RAF-T19a): pendente em versão 3 contra a vigente 1 — `check --so-vigente` sai 0 sem
+    `V20` no stderr (sem a guarda `not so_vigente` sairia 1 com a `V20`)."""
+    modelo = _load_modelo()
+    raiz, plano = _raiz_pendente_fora_de_sequencia(tmp_path)
+
+    codigo = modelo.main(["check", "--plano", str(plano), "--root", str(raiz), "--so-vigente"])
+    saida = capsys.readouterr()
+
+    assert codigo == 0
+    assert "V20" not in saida.err
+
+
+def test_tr_sem_so_vigente_pendente_fora_de_sequencia_segue_v20(tmp_path, capsys):
+    """TR (RAF-T19a): o mesmo plano, sem a flag, sai 1 com
+    `V20 secao — versão pendente fora de sequência` no stderr."""
+    modelo = _load_modelo()
+    raiz, plano = _raiz_pendente_fora_de_sequencia(tmp_path)
+
+    codigo = modelo.main(["check", "--plano", str(plano), "--root", str(raiz)])
+    saida = capsys.readouterr()
+
+    assert codigo == 1
+    assert "V20 secao — versão pendente fora de sequência" in saida.err

```

## Linhas removidas dos testes
### `tests/test_modelo.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T19a-medida-depois.json; mundo: depois; gerado em: 2026-09-29T20:18:57+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_modelo.py -q -k "so_vigente and fora_de_sequencia"` | 0 | true |

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
