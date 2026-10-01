# Evidência de revisão — P-0754 AUF-T6

## Diff (`git diff --stat`)
```
.claude/tools/review_evidence.py                   | 17 +++++++++--
 docs/DIARIO_DE_OBRAS.md                            |  4 +--
 docs/plans/P-0754-auditoria-final/estado.tsv       |  2 +-
 .../evidencia/P-0754-AUF-T6-medida.json            | 15 ++++++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_review_evidence.py                      | 33 ++++++++++++++++++++++
 6 files changed, 67 insertions(+), 5 deletions(-)
```

## Arquivos tocados
- `.claude/tools/review_evidence.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0754-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T6-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `55123364fce5dc6afa1bad832786e707ee0b9397`
- Arquivos-alvo declarados: `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`
- Arquivos tocados: `.claude/tools/review_evidence.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T6-medida.json`, `docs/telemetria.tsv`, `tests/test_review_evidence.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T6-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index 56cfb1f..b5eb700 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -307,13 +307,26 @@ def _texto_do_disco(root: Path, caminho: str) -> str | None:
         return None
 
 
+def _bytes_do_ref(root: Path, ref: str, caminho: str) -> bytes:
+    resultado = subprocess.run(
+        ["git", "show", f"{ref}:{caminho}"], cwd=str(root), capture_output=True
+    )
+    return resultado.stdout
+
+
 def _nao_rastreado_mudou_desde_ref(root: Path, ref: str, caminho: str) -> bool:
     """Julgamento por conteúdo (linha a linha, fim de linha normalizado por `str.splitlines`) do
     não rastreado que já existia na árvore de `<ref>` — em vez do recorte por `st_mtime` usado
-    para o não rastreado ausente de `<ref>` (esse permanece intocado)."""
+    para o não rastreado ausente de `<ref>` (esse permanece intocado). Quando o arquivo não se lê
+    como texto (`_texto_do_disco` devolve `None`), o julgamento cai para os bytes brutos do
+    arquivo contra os de `<ref>` (AUF-T6)."""
     texto_atual = _texto_do_disco(root, caminho)
     if texto_atual is None:
-        return True
+        try:
+            bytes_atuais = (root / caminho).read_bytes()
+        except FileNotFoundError:
+            return True
+        return _bytes_do_ref(root, ref, caminho) != bytes_atuais
     return _texto_do_ref(root, ref, caminho).splitlines() != texto_atual.splitlines()
 
 

```

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index 2978566..cae0cb7 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -1618,3 +1618,36 @@ def test_tf_versionado_ignorado_intocado_fica_fora_dos_tocados_e_alterado_entra(
 
     assert review_evidence.coletar_arquivos_tocados(repo, desde=ref) == ["versionado.log"]
     assert "versionado.log" in review_evidence.coletar_diff_stat(repo, desde=ref)
+
+
+def test_tf_nao_rastreado_binario_intocado_fica_fora_dos_tocados(tmp_path):
+    """AUF-T6 (`DAU-19`, `H-20` §2.1, `F-13`): não rastreado binário já presente na árvore de
+    `<ref>` — o julgamento por conteúdo cai para os bytes brutos quando o arquivo não se lê como
+    texto UTF-8; intocado desde `<ref>`, ele não entra em `coletar_arquivos_tocados` (a regra
+    antiga, por dar `_texto_do_disco` como `None` e tratar isso como "mudou", devolvia
+    `["imagem.bin"]`)."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    (repo / "imagem.bin").write_bytes(bytes([0xFF, 0xFE, 0x00, 0x81]))
+
+    ref = review_evidence.capturar_ref(repo)
+
+    assert review_evidence.coletar_arquivos_tocados(repo, desde=ref) == []
+
+
+def test_tr_nao_rastreado_binario_alterado_entra_nos_tocados(tmp_path):
+    """AUF-T6 (`DAU-19`, `H-20` §2.1, `F-13`): o mesmo não rastreado binário, regravado com bytes
+    diferentes depois de `<ref>`, entra em `coletar_arquivos_tocados` — trava o comportamento
+    novo contra regressão para a regra antiga (que sempre devolvia o binário como tocado, mudado
+    ou não)."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    (repo / "imagem.bin").write_bytes(bytes([0xFF, 0xFE, 0x00, 0x81]))
+
+    ref = review_evidence.capturar_ref(repo)
+
+    (repo / "imagem.bin").write_bytes(bytes([0xFF, 0xFE, 0x00, 0x82]))
+
+    assert review_evidence.coletar_arquivos_tocados(repo, desde=ref) == ["imagem.bin"]

```

## Medida do executor
- Arquivo: docs\plans\P-0754-auditoria-final\evidencia\P-0754-AUF-T6-medida.json; mundo: depois; gerado em: 2026-09-28T14:34:45+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_review_evidence.py -q -k "binario"` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
