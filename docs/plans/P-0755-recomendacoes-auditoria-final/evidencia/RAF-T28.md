# Evidência de revisão — P-0755 RAF-T28

## Diff (`git diff --stat`)
```
.claude/tools/backlog.py                           | 25 ++++++++++++
 docs/DIARIO_DE_OBRAS.md                            |  4 +-
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T28-medida-depois.json    | 15 +++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_backlog.py                              | 47 ++++++++++++++++++++++
 6 files changed, 91 insertions(+), 3 deletions(-)
```

## Arquivos tocados
- `.claude/tools/backlog.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T28-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_backlog.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `3fbe7a6ade1e0478c4c0c0cbec487823ed6a770e`
- Arquivos-alvo declarados: `.claude/tools/backlog.py`, `tests/test_backlog.py`
- Arquivos tocados: `.claude/tools/backlog.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T28-medida-depois.json`, `docs/telemetria.tsv`, `tests/test_backlog.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T28-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/backlog.py`
```
diff --git a/.claude/tools/backlog.py b/.claude/tools/backlog.py
index ecb2c39..63ef637 100644
--- a/.claude/tools/backlog.py
+++ b/.claude/tools/backlog.py
@@ -1041,6 +1041,18 @@ def _citacoes_do_texto(texto: str) -> list[tuple[int, str]]:
 # --------------------------------------------------------------------------- #
 
 
+def _id_vivo(modelo: Modelo, id_: str) -> bool:
+    """RAF-T28 (`DRF-20` do `P-0755`): id vivo é o que `_localizar` encontra na árvore e cujo
+    `status` (texto até o primeiro espaço) não é `done`, `cancelled` nem `superseded` — status
+    vazio conta como vivo."""
+    alvo = _localizar(modelo, id_)
+    if alvo is None:
+        return False
+    if not alvo.status:
+        return True
+    return alvo.status.split(" ", 1)[0] not in {"done", "cancelled", "superseded"}
+
+
 def _localizar(modelo: Modelo, id_: str) -> Plano | Item | None:
     for plano in modelo.planos:
         if plano.id == id_:
@@ -2065,6 +2077,19 @@ def transacionar_drain(
     _escrever_atomico(inbox_planos, linhas_novo_inbox)
     _escrever_atomico(historico, linhas_historico)
 
+    # R-18 (DRF-20 do P-0755): a auditoria achou a diretiva de priorização ainda apontando um
+    # plano que já tinha saído da fila. Aviso, não recusa, e não reescreve a diretiva — isso é
+    # ato de quem conduz, via `backlog.py diretiva`.
+    if any(DIRETIVA_RE.match(l) for l in diario_linhas) and not any(
+        _id_vivo(modelo, id_) for id_ in modelo.diretiva_ids
+    ):
+        for _, _, plano in drenos:
+            if plano.id not in modelo.diretiva_ids:
+                print(
+                    f"drain: aviso — a diretiva de priorização não cita nenhum id vivo nem {plano.id}",
+                    file=sys.stderr,
+                )
+
     arquivos = sorted(
         {
             modelo.diario_arquivo,

```

### `tests/test_backlog.py`
```
diff --git a/tests/test_backlog.py b/tests/test_backlog.py
index e5358fe..b3552ea 100644
--- a/tests/test_backlog.py
+++ b/tests/test_backlog.py
@@ -3477,3 +3477,50 @@ def test_tr_despachar_versao_vigente_recusa_defeito_da_vigente(tmp_path, capsys)
 
     erro = capsys.readouterr().err
     assert "despachar: recusado — modelo:" in erro
+
+
+# --------------------------------------------------------------------------- #
+# RAF-T28 (`DRF-20`, `F-23` do `P-0755`) — `drain` avisa, no stderr, quando a diretiva de
+# priorização não cita nenhum id vivo nem o plano que acabou de sair da fila (`R-18`: a
+# auditoria achou a diretiva ainda apontando um plano já drenado).
+# --------------------------------------------------------------------------- #
+
+
+def _repo_drain_com_diretiva(tmp_path: Path, ids_da_diretiva: str) -> Path:
+    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
+    _escrever_plano(repo, "P-0800-alfa.md", "P-0800", "Plano alfa de teste", "ALF", "ready")
+    _inbox_com_linhas(repo, ["- docs/plans/P-0800-alfa.md — plano alfa de teste"])
+    _inserir_bloco_gerado(repo)
+    diario = repo / "docs" / "DIARIO_DE_OBRAS.md"
+    linhas = diario.read_text(encoding="utf-8").splitlines()
+    linhas.insert(1, f"**Diretiva de priorização:** {ids_da_diretiva} — texto da fixture.")
+    diario.write_text("\n".join(linhas) + "\n", encoding="utf-8")
+    return repo
+
+
+def test_tf_drain_aviso_diretiva_sem_id_vivo(tmp_path, capsys):
+    """TF da RAF-T28: diretiva com `` `P-0001` `` (id que não existe na fixture) — `drain`
+    sai 0 e o stderr traz o aviso nomeando o plano drenado (`P-0800`); hoje sai 0 em
+    silêncio."""
+    backlog = _load_backlog()
+    repo = _repo_drain_com_diretiva(tmp_path, "`P-0001`")
+
+    assert backlog.main(["drain", "--repo", str(repo), "--data", "2026-09-28"]) == 0
+
+    erro = capsys.readouterr().err
+    assert "drain: aviso — a diretiva de priorização não cita nenhum id vivo nem P-0800" in erro
+
+
+def test_tr_drain_aviso_diretiva_com_id_vivo_ou_drenado_cala(tmp_path, capsys):
+    """TR da RAF-T28: diretiva com um id vivo (`P-0090`, `ready` na fixture) e, em outra
+    cópia, com o próprio id drenado (`P-0800`) — os dois saem 0 sem `drain: aviso` no stderr;
+    a regra concorrente, avisar a cada drenagem, avisaria nos dois casos."""
+    backlog = _load_backlog()
+
+    repo_vivo = _repo_drain_com_diretiva(tmp_path / "vivo", "`P-0090`")
+    assert backlog.main(["drain", "--repo", str(repo_vivo), "--data", "2026-09-28"]) == 0
+    assert "drain: aviso" not in capsys.readouterr().err
+
+    repo_drenado = _repo_drain_com_diretiva(tmp_path / "drenado", "`P-0800`")
+    assert backlog.main(["drain", "--repo", str(repo_drenado), "--data", "2026-09-28"]) == 0
+    assert "drain: aviso" not in capsys.readouterr().err

```

## Linhas removidas dos testes
### `tests/test_backlog.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T28-medida-depois.json; mundo: depois; gerado em: 2026-09-30T00:08:46+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_backlog.py -q -k aviso_diretiva` | 0 | true |

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
