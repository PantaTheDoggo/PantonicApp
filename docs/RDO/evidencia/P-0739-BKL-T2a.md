# Evidência de revisão — P-0739 BKL-T2a

## Diff (`git diff --stat`)
```
.claude/agents/pantonic-planner.md       |   6 +
 .claude/tools/rdo.py                     |   6 +-
 CHANGELOG.md                             |   6 +
 docs/DIARIO_DE_OBRAS.md                  |   8 +-
 docs/plans/P-0739-backlog-instrumento.md | 210 +++++++++++++++++++++++++++++--
 docs/telemetria.tsv                      |   3 +
 tests/test_rdo.py                        |  66 ++++++++++
 7 files changed, 289 insertions(+), 16 deletions(-)
```

## Arquivos tocados
- `.claude/agents/pantonic-planner.md`
- `.claude/tools/rdo.py`
- `CHANGELOG.md`
- `docs/DIARIO_DE_OBRAS.md`
- `docs/RDO/evidencia/P-0739-BKL-T2.md`
- `docs/RDO/evidencia/P-0739-BKL-T2a.md`
- `docs/plans/P-0739-backlog-instrumento.md`
- `docs/telemetria.tsv`
- `tests/test_rdo.py`

## Escopo
- Recorte: desde `6d7433c`
- Arquivos-alvo declarados: `.claude/tools/rdo.py`, `_ID_HEADER_RE = re.compile(r"^### (T[0-9]+[a-z]?)(?=[\s—])")`, `tests/test_rdo.py`
- Arquivos tocados: `.claude/agents/pantonic-planner.md`, `.claude/tools/rdo.py`, `CHANGELOG.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/evidencia/P-0739-BKL-T2.md`, `docs/RDO/evidencia/P-0739-BKL-T2a.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/telemetria.tsv`, `tests/test_rdo.py`
- Fato: 7 arquivo(s) fora dos alvos: `.claude/agents/pantonic-planner.md`, `CHANGELOG.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/evidencia/P-0739-BKL-T2.md`, `docs/RDO/evidencia/P-0739-BKL-T2a.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/telemetria.tsv`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/rdo.py`
```
diff --git a/.claude/tools/rdo.py b/.claude/tools/rdo.py
index 62c64fe..4dc3f3b 100644
--- a/.claude/tools/rdo.py
+++ b/.claude/tools/rdo.py
@@ -76,11 +76,11 @@ _CLASSE_ALIASES: dict[str, str] = {
     "redacao/planejamento": "redacao",
 }
 
-_ID_HEADER_RE = re.compile(r"^### (T[0-9]+[a-z]?)(?=[\s—])")
+_ID_HEADER_RE = re.compile(r"^### ((?:[A-Z0-9]+-)?T[0-9]+[a-z]?)(?=[\s—])")
 _ID_LAUDO_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")  # identificador, nunca caminho
 _HEADER_BRACKET_RE = re.compile(
-    r"^### (?P<id>T[0-9]+[a-z]?) — (?P<titulo>.+?) "
-    r"\[(?P<modelo>Opus|Sonnet|Haiku) · classe (?P<classe>.+?)"
+    r"^### (?P<id>(?:[A-Z0-9]+-)?T[0-9]+[a-z]?) — (?P<titulo>.+?) "
+    r"\[(?P<modelo>Opus|Sonnet|Haiku)(?: \+ dono)? · classe (?P<classe>.+?)"
     r"(?: · teto (?:prescrito )?[0-9]+)?\](?P<sufixo>.*)$"
 )
 _HEADER_LEGADO_TITULO_FMT = r"^### {id} — (?P<titulo>.+)$"

```

### `_ID_HEADER_RE = re.compile(r"^### (T[0-9]+[a-z]?)(?=[\s—])")`
```
(sem diferença coletável — arquivo ausente na árvore de trabalho)
```

### `tests/test_rdo.py`
```
diff --git a/tests/test_rdo.py b/tests/test_rdo.py
index 7f2d51c..6d29173 100644
--- a/tests/test_rdo.py
+++ b/tests/test_rdo.py
@@ -560,3 +560,69 @@ def test_tr_laudo_recusa_plano_e_tarefa_em_forma_de_caminho(tmp_path, capsys):
     assert exit_code != 0
     assert "--plano" in capsys.readouterr().err
     assert not laudos_dir.exists() or list(laudos_dir.glob("*.md")) == []
+
+
+def test_tf_extrair_dossie_id_prefixado(tmp_path):
+    """TF da BKL-T2a (`DB-22`): ID de tarefa com prefixo de plano (`BKL-T2`) é localizado pelo
+    cabeçalho e casado por igualdade exata, prefixo incluído."""
+    rdo = _load_rdo()
+    plano = tmp_path / "plano.md"
+    _escrever_plano_sintetico(plano, "### BKL-T2 — Tarefa sintética [Sonnet · classe implementacao]")
+
+    dossie = rdo.extrair_dossie(
+        plano, "BKL-T2", esquema_legado=False, modelo_legado=None, classe_legado=None,
+    )
+
+    assert dossie.tarefa_id == "BKL-T2"
+    assert dossie.modelo == "Sonnet"
+    assert dossie.classe == "implementacao"
+    assert dossie.esquema == "padrao"
+
+
+def test_tf_extrair_dossie_id_prefixado_com_letra_e_teto_legado(tmp_path):
+    """TF da BKL-T2a (`DB-22`): ID prefixado com letra de subtarefa (`CTX-T1d`) e segmento de
+    teto histórico (`· teto 30`), aceito e descartado."""
+    rdo = _load_rdo()
+    plano = tmp_path / "plano.md"
+    _escrever_plano_sintetico(plano, "### CTX-T1d — Tarefa sintética [Opus · classe redacao · teto 30]")
+
+    dossie = rdo.extrair_dossie(
+        plano, "CTX-T1d", esquema_legado=False, modelo_legado=None, classe_legado=None,
+    )
+
+    assert dossie.tarefa_id == "CTX-T1d"
+    assert dossie.classe == "redacao"
+    assert dossie.esquema == "padrao"
+
+
+def test_tf_extrair_dossie_bracket_com_aceite_do_dono(tmp_path):
+    """TF da BKL-T2a (`DB-20`): segmento ` + dono` no bracket é aceito e descartado."""
+    rdo = _load_rdo()
+    plano = tmp_path / "plano.md"
+    _escrever_plano_sintetico(plano, "### BKL-T9 — Tarefa sintética [Opus + dono · classe redacao]")
+
+    dossie = rdo.extrair_dossie(
+        plano, "BKL-T9", esquema_legado=False, modelo_legado=None, classe_legado=None,
+    )
+
+    assert dossie.modelo == "Opus"
+    assert dossie.classe == "redacao"
+    assert dossie.esquema == "padrao"
+
+
+def test_tr_extrair_dossie_id_casa_por_igualdade_exata(tmp_path):
+    """TR da BKL-T2a: prefixo nunca casa por sufixo nem por ID parcial — `T1` não encontra
+    `BKL-T1`, e `BKL-T2` não encontra `BKL-T1`."""
+    rdo = _load_rdo()
+    plano = tmp_path / "plano.md"
+    _escrever_plano_sintetico(plano, "### BKL-T1 — Tarefa sintética [Sonnet · classe redacao]")
+
+    with pytest.raises(rdo.RdoValidationError):
+        rdo.extrair_dossie(
+            plano, "T1", esquema_legado=False, modelo_legado=None, classe_legado=None,
+        )
+
+    with pytest.raises(rdo.RdoValidationError):
+        rdo.extrair_dossie(
+            plano, "BKL-T2", esquema_legado=False, modelo_legado=None, classe_legado=None,
+        )

```

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
