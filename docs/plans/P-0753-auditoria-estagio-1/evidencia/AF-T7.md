# Evidência de revisão — P-0753 AF-T7

## Diff (`git diff --stat`)
```
.claude/tools/card_check.py                        |  4 ++-
 docs/ACIONAMENTOS_CONSULTOR.tsv                    |  1 +
 docs/DIARIO_DE_OBRAS.md                            |  2 +-
 docs/plans/P-0753-auditoria-estagio-1/cenario.md   | 19 +++++++++---
 docs/plans/P-0753-auditoria-estagio-1/estado.tsv   |  2 +-
 .../evidencia/P-0753-AF-T7-medida.json             | 36 ++++++++++++++++++++++
 docs/plans/P-0753-auditoria-estagio-1/plano.md     | 17 +++++-----
 docs/telemetria.tsv                                |  3 ++
 tests/fixtures/card_check/P-0-pasta/estado.tsv     |  4 +++
 tests/fixtures/card_check/P-0-pasta/plano.md       | 17 ++++++++++
 tests/test_card_check.py                           | 30 ++++++++++++++++++
 11 files changed, 121 insertions(+), 14 deletions(-)
```

## Arquivos tocados
- `.claude/tools/card_check.py` — atribuição: da entrega; estado git: ` M`
- `docs/ACIONAMENTOS_CONSULTOR.tsv` — atribuição: alheio; estado git: `??`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/cenario.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T7-medida.json` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/plano.md` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/card_check/P-0-pasta/estado.tsv` — atribuição: da entrega; estado git: `??`
- `tests/fixtures/card_check/P-0-pasta/plano.md` — atribuição: da entrega; estado git: `??`
- `tests/test_card_check.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `2f63d417db590dd5170b41b7c5e151db18a0585e`
- Arquivos-alvo declarados: `.claude/tools/card_check.py`, `tests/test_card_check.py`, `tests/fixtures/card_check/P-0-pasta/plano.md`, `tests/fixtures/card_check/P-0-pasta/estado.tsv`
- Arquivos tocados: `.claude/tools/card_check.py`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/cenario.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T7-medida.json`, `docs/plans/P-0753-auditoria-estagio-1/plano.md`, `docs/telemetria.tsv`, `tests/fixtures/card_check/P-0-pasta/estado.tsv`, `tests/fixtures/card_check/P-0-pasta/plano.md`, `tests/test_card_check.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/cenario.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T7-medida.json`, `docs/plans/P-0753-auditoria-estagio-1/plano.md`, `docs/telemetria.tsv`
- Fato: 1 arquivo(s) fora dos alvos e sem atribuição: `docs/ACIONAMENTOS_CONSULTOR.tsv`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/card_check.py`
```
diff --git a/.claude/tools/card_check.py b/.claude/tools/card_check.py
index e363b76..fdc20c1 100644
--- a/.claude/tools/card_check.py
+++ b/.claude/tools/card_check.py
@@ -360,7 +360,9 @@ def verificar_tarefa(
         raise CardCheckValidationError(str(exc)) from exc
 
     if mundo is None:
-        status = rdo._status_atual(plano_path, dossie.tarefa_id, dossie, None)
+        status = rdo._status_atual(
+            plano_path, dossie.tarefa_id, dossie, _caminhos.pasta_do_plano(plano_path)
+        )
         if status is None:
             print("status ausente: comparando antes")
             mundo = "antes"

```

### `tests/test_card_check.py`
```
diff --git a/tests/test_card_check.py b/tests/test_card_check.py
index f9ae5df..a6e6672 100644
--- a/tests/test_card_check.py
+++ b/tests/test_card_check.py
@@ -16,6 +16,7 @@ _CARD_CHECK_PATH = _ROOT / ".claude" / "tools" / "card_check.py"
 _PLANO_FIXTURE = _ROOT / "tests" / "fixtures" / "card_check" / "plano-exemplo.md"
 _PLANO_CORPUS = _ROOT / "tests" / "fixtures" / "card_check" / "plano-corpus.md"
 _PLANO_ANCORAS = _ROOT / "tests" / "fixtures" / "card_check" / "plano-ancoras.md"
+_PLANO_PASTA = _ROOT / "tests" / "fixtures" / "card_check" / "P-0-pasta" / "plano.md"
 
 
 def _load_card_check():
@@ -370,3 +371,32 @@ def test_tf_gravar_sem_caminho_grava_no_destino_derivado(tmp_path, capsys):
     destino = tmp_path / "docs" / "RDO" / "evidencia" / "DIARIO_DE_OBRAS-CX-T1-medida.json"
     dados = json.loads(destino.read_text(encoding="utf-8"))
     assert dados["tarefa"] == "CX-T1"
+
+
+# --- AF-T7 (DAF-18/DAF-39): status de plano em pasta lido de `estado.tsv`, não do card ----------
+
+
+def test_tf_estado_tsv_done_compara_depois(capsys):
+    """`CP-T1` (`tests/fixtures/card_check/P-0-pasta/`) não declara `- **Status:**` no card — o
+    status `done` mora só na linha `CP-T1` de `estado.tsv`. `verificar_tarefa` passa a pasta do
+    plano a `rdo._status_atual`, que lê essa linha: mundo `depois`, e o comando declarado
+    (`python -c "print('b')"`) imprime `b`, batendo com o valor `depois` — `card_check` sai 0."""
+    card_check = _load_card_check()
+
+    codigo = card_check.main(["--plano", str(_PLANO_PASTA), "--tarefa", "CP-T1", "--root", str(_ROOT)])
+    saida = capsys.readouterr()
+
+    assert codigo == 0
+    assert "card_check: OK" in saida.out
+
+
+def test_tr_estado_tsv_ready_compara_antes(capsys):
+    """`CP-T2` está `ready` só em `estado.tsv` — mundo `antes`, e o comando declarado
+    (`python -c "print('a')"`) imprime `a`, batendo com o valor `antes` — `card_check` sai 0."""
+    card_check = _load_card_check()
+
+    codigo = card_check.main(["--plano", str(_PLANO_PASTA), "--tarefa", "CP-T2", "--root", str(_ROOT)])
+    saida = capsys.readouterr()
+
+    assert codigo == 0
+    assert "card_check: OK" in saida.out

```

### `tests/fixtures/card_check/P-0-pasta/plano.md`
```
# P-0 — Fixture de card_check em plano em pasta

**Prefixo das tarefas no diário:** `CP-T<n>`

### CP-T1 — Card concluído de plano em pasta [Sonnet · classe mecanica]
- **Objetivo:** fixture de `card_check`: o status `done` mora só em `estado.tsv`.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Verificação:**
  1. `python -c "print('b')"` → `b` — antes `a`, depois `b`
- **Pronto quando:** `card_check.py --tarefa CP-T1` sai 0, comparando `depois`.

### CP-T2 — Card pronto de plano em pasta [Sonnet · classe mecanica]
- **Objetivo:** fixture de `card_check`: o status `ready` mora só em `estado.tsv`.
- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.
- **Verificação:**
  1. `python -c "print('a')"` → `b` — antes `a`, depois `b`
- **Pronto quando:** `card_check.py --tarefa CP-T2` sai 0, comparando `antes`.

```

### `tests/fixtures/card_check/P-0-pasta/estado.tsv`
```
id	tipo	status	razao	data	nota
P-0	plano	in-progress	-	2026-09-27	-
CP-T1	tarefa	done	-	2026-09-27	-
CP-T2	tarefa	ready	-	2026-09-27	-

```

## Medida do executor
- Arquivo: docs\plans\P-0753-auditoria-estagio-1\evidencia\P-0753-AF-T7-medida.json; mundo: depois; gerado em: 2026-09-27T13:38:47+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python .claude/tools/card_check.py --plano tests/fixtures/card_check/P-0-pasta/plano.md --tarefa CP-T1` | 0 | true |
| 2 | `python -m pytest tests/test_card_check.py -q -k "estado_tsv"` | 0 | true |
| 3 | `python -m pytest -q` | 0 | true |
| 4 | `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
