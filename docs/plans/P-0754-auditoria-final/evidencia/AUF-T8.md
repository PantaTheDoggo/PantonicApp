# Evidência de revisão — P-0754 AUF-T8

## Diff (`git diff --stat`)
```
.claude/tools/encerrar.py                          |  2 +-
 docs/DIARIO_DE_OBRAS.md                            |  4 ++--
 docs/plans/P-0754-auditoria-final/estado.tsv       |  2 +-
 .../evidencia/P-0754-AUF-T8-medida.json            | 22 ++++++++++++++++++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_encerrar.py                             | 20 ++++++++++++++++++--
 6 files changed, 45 insertions(+), 6 deletions(-)
```

## Arquivos tocados
- `.claude/tools/encerrar.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0754-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T8-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_encerrar.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `0e011ab9837338509cd5c9fcceca89097f443dc5`
- Arquivos-alvo declarados: `.claude/tools/encerrar.py`, `tests/test_encerrar.py`
- Arquivos tocados: `.claude/tools/encerrar.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T8-medida.json`, `docs/telemetria.tsv`, `tests/test_encerrar.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T8-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/encerrar.py`
```
diff --git a/.claude/tools/encerrar.py b/.claude/tools/encerrar.py
index fe4909f..0196278 100644
--- a/.claude/tools/encerrar.py
+++ b/.claude/tools/encerrar.py
@@ -1290,7 +1290,7 @@ def main(argv: list[str] | None = None) -> int:
         return 1
 
     print(humano)
-    print(f"encerrar: OK - {args.comando} fechado; relatório em '{destino}'.")
+    print(f"encerrar: OK - comando '{args.comando}' concluído; relatório em '{destino}'.")
     return 0
 
 

```

### `tests/test_encerrar.py`
```
diff --git a/tests/test_encerrar.py b/tests/test_encerrar.py
index bff07ef..d595dc3 100644
--- a/tests/test_encerrar.py
+++ b/tests/test_encerrar.py
@@ -480,7 +480,7 @@ def test_tf_plano_fecha_status_entrega_tres_secoes_e_linha_do_diario(tmp_path):
 def test_tf_fechado_conta_como_o_indice(tmp_path, capsys):
     """TF (`TK-88d`): a linha `FECHADO` conta as tarefas como o índice conta (`_done_total`,
     que tira as `cancelled` do total) — fixture com uma `done` (`ALF-T1`) e uma `cancelled`
-    (`ALF-T2`) fecha com `1/1`, não `1/2`, e o stdout do fechamento diz `plano fechado`."""
+    (`ALF-T2`) fecha com `1/1`, não `1/2`, e o stdout do fechamento diz `comando 'plano' concluído`."""
     repo = _montar_repo(tmp_path)
     _fechar_tarefa_e_preparar_plano(repo)
 
@@ -489,7 +489,7 @@ def test_tf_fechado_conta_como_o_indice(tmp_path, capsys):
     assert exit_code == 0
     diario = (repo / "docs" / "DIARIO_DE_OBRAS.md").read_text(encoding="utf-8").splitlines()
     assert any("FECHADO `done` 1/1 em 2026-09-26" in l for l in diario)
-    assert "plano fechado" in capsys.readouterr().out
+    assert "encerrar: OK - comando 'plano' concluído;" in capsys.readouterr().out
 
 
 @pytest.mark.parametrize(
@@ -885,3 +885,19 @@ def test_tr_esqueleto_de_operacoes_plano_relativo(tmp_path, monkeypatch, capsys)
     assert exit_code == 0
     assert "nao citados: nenhum" in saida
     assert "sem seção: nenhum" in saida
+
+
+def test_tf_conclusao_da_tarefa_sem_erro_de_concordancia(tmp_path, capsys):
+    """TF: a frase final do fechamento serve a todos os comandos — para `tarefa` ela diz
+    `comando 'tarefa' concluído`, nunca `tarefa fechado` (a regra antiga imprimia
+    `encerrar: OK - tarefa fechado;`)."""
+    repo = _montar_repo(tmp_path)
+
+    exit_code = encerrar.main(_argv_tarefa(
+        repo, **{"--resumo": "A primeira coisa está entregue.", "--pendencia": "nomear a função"},
+    ))
+
+    assert exit_code == 0
+    saida = capsys.readouterr().out
+    assert "encerrar: OK - comando 'tarefa' concluído;" in saida
+    assert "tarefa fechado" not in saida

```

## Medida do executor
- Arquivo: docs\plans\P-0754-auditoria-final\evidencia\P-0754-AUF-T8-medida.json; mundo: depois; gerado em: 2026-09-28T14:49:20+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_encerrar.py -q -k "conclusao_da_tarefa"` | 0 | true |
| 2 | `python -c "from pathlib import Path;t=Path('.claude/tools/encerrar.py').read_text(encoding='utf-8');print('[%d-%d]'%(t.count('concluído; relatório em'),t.count('fechado; relatório em')))"` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
