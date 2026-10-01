# Evidência de revisão — P-0755 RAF-T7

## Diff (`git diff --stat`)
```
.claude/tools/review_evidence.py                   |  28 +++-
 docs/DIARIO_DE_OBRAS.md                            |   4 +-
 .../estado.tsv                                     |   2 +-
 .../evidencia/P-0755-RAF-T7-medida.json            |  15 ++
 docs/telemetria.tsv                                |   1 +
 tests/test_review_evidence.py                      | 151 +++++++++++++++++++++
 6 files changed, 192 insertions(+), 9 deletions(-)
```

## Arquivos tocados
- `.claude/tools/review_evidence.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T7-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `bbe398bc5b9f4aceaf99faf64707c95ae8069dcb`
- Arquivos-alvo declarados: `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`
- Arquivos tocados: `.claude/tools/review_evidence.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T7-medida.json`, `docs/telemetria.tsv`, `tests/test_review_evidence.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T7-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index b5eb700..c58da13 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -296,8 +296,11 @@ def _eh_nao_rastreado(root: Path, caminho: str) -> bool:
     return saida.startswith("??")
 
 
-def _texto_do_ref(root: Path, ref: str, caminho: str) -> str:
-    return _git(["show", f"{ref}:{caminho}"], root)
+def _texto_do_ref_ou_none(root: Path, ref: str, caminho: str) -> str | None:
+    try:
+        return _bytes_do_ref(root, ref, caminho).decode("utf-8")
+    except UnicodeDecodeError:
+        return None
 
 
 def _texto_do_disco(root: Path, caminho: str) -> str | None:
@@ -327,7 +330,10 @@ def _nao_rastreado_mudou_desde_ref(root: Path, ref: str, caminho: str) -> bool:
         except FileNotFoundError:
             return True
         return _bytes_do_ref(root, ref, caminho) != bytes_atuais
-    return _texto_do_ref(root, ref, caminho).splitlines() != texto_atual.splitlines()
+    texto_ref = _texto_do_ref_ou_none(root, ref, caminho)
+    if texto_ref is None:
+        return _bytes_do_ref(root, ref, caminho) != (root / caminho).read_bytes()
+    return texto_ref.splitlines() != texto_atual.splitlines()
 
 
 def coletar_arquivos_tocados(root: Path, desde: str | None = None) -> list[str]:
@@ -619,7 +625,12 @@ def _diff_para_arquivo(root: Path, caminho_rel: str, desde: str | None = None) -
             texto_atual = _texto_do_disco(root, caminho_rel)
             if texto_atual is None:
                 return "(arquivo binário ou não-UTF-8 — trecho omitido)"
-            linhas_ref = _texto_do_ref(root, desde, caminho_rel).splitlines()
+            texto_ref = _texto_do_ref_ou_none(root, desde, caminho_rel)
+            if texto_ref is None:
+                if _bytes_do_ref(root, desde, caminho_rel) == (root / caminho_rel).read_bytes():
+                    return f"(sem alteração desde `{desde}`)"
+                return "(arquivo binário ou não-UTF-8 — trecho omitido)"
+            linhas_ref = texto_ref.splitlines()
             linhas_atual = texto_atual.splitlines()
             if linhas_ref == linhas_atual:
                 return f"(sem alteração desde `{desde}`)"
@@ -988,9 +999,10 @@ def montar_documento(
 
     plano_id = _caminhos.id_do_plano(plano_path) or plano_path.stem
 
+    caminho_medida = None
     if dir_evidencia is not None:
         caminho_medida = Path(dir_evidencia) / f"{plano_id}-{dossie.tarefa_id}-medida.json"
-    else:
+    if caminho_medida is None or not caminho_medida.is_file():
         caminho_medida = _caminhos.destino_medida(root, plano_path, dossie.tarefa_id)
 
     return _renderizar(
@@ -1076,7 +1088,11 @@ def main(argv: list[str] | None = None) -> int:
         parser.error("--plano e --tarefa são obrigatórios (exceto com --capturar-ref).")
 
     if args.atribuir:
-        rdo = _load_rdo(args.root)
+        try:
+            rdo = _load_rdo(args.root)
+        except ReviewEvidenceValidationError as exc:
+            print(f"review_evidence: FALHOU - {exc}", file=sys.stderr)
+            return 1
         try:
             _exigir_plano(args.plano)
             dossie = rdo.extrair_dossie(

```

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index cae0cb7..c56fc81 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -1651,3 +1651,154 @@ def test_tr_nao_rastreado_binario_alterado_entra_nos_tocados(tmp_path):
     (repo / "imagem.bin").write_bytes(bytes([0xFF, 0xFE, 0x00, 0x82]))
 
     assert review_evidence.coletar_arquivos_tocados(repo, desde=ref) == ["imagem.bin"]
+
+
+# --- RAF-T7 (R-13, AE-105/AE-106 do P-0754): o dossiê chega ao fim nos três casos em que quebrava
+
+
+def _plano_em_pasta_com_medida(repo: Path, exit_medido: int) -> Path:
+    """Plano em layout de pasta (`docs/plans/P-0999-teste/plano.md`) dentro do repositório de
+    fixture, com a medida do executor já gravada em `evidencia/` ao lado dele (`P-0999-T1-medida.json`,
+    no molde de `test_tf_evidencia_incorpora_medida`)."""
+    pasta_plano = repo / "docs" / "plans" / "P-0999-teste"
+    pasta_plano.mkdir(parents=True, exist_ok=True)
+    plano = pasta_plano / "plano.md"
+    _escrever_plano(plano, "cria `src/a.py`.")
+    (repo / "src" / "a.py").write_text("def a():\n    return 2\n", encoding="utf-8")
+    pasta_evidencia = pasta_plano / "evidencia"
+    pasta_evidencia.mkdir(parents=True, exist_ok=True)
+    medida = {
+        "plano": str(plano),
+        "tarefa": "T1",
+        "mundo": "antes",
+        "gerado_em": "2026-09-26T00:00:00+00:00",
+        "itens": [
+            {
+                "indice": 1,
+                "comando": "python -c \"print('a')\"",
+                "exit": exit_medido,
+                "saida": "a",
+                "bate": True,
+            }
+        ],
+    }
+    (pasta_evidencia / "P-0999-T1-medida.json").write_text(
+        json.dumps(medida, ensure_ascii=False, indent=2), encoding="utf-8"
+    )
+    return plano
+
+
+def test_tf_quebra_ref_binario_hoje_texto_compara_bytes(tmp_path):
+    """RAF-T7 (R-13): não rastreado binário no `<ref>`, regravado depois como texto — o julgamento
+    por conteúdo cai para os bytes brutos (que divergem) e o trecho relatado nomeia o binário/
+    não-UTF-8 em vez de deixar a leitura em texto do `<ref>` lançar exceção."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    (repo / "dados.txt").write_bytes(bytes([0xFF, 0xFE, 0x00, 0x81]))
+
+    ref = review_evidence.capturar_ref(repo)
+
+    (repo / "dados.txt").write_text("ola", encoding="utf-8")
+
+    tocados = review_evidence.coletar_arquivos_tocados(repo, desde=ref)
+    assert tocados == ["dados.txt"]
+
+    trechos = review_evidence.montar_trechos(repo, ["dados.txt"], 4000, tocados, desde=ref)
+    assert trechos["dados.txt"]["texto"] == "(arquivo binário ou não-UTF-8 — trecho omitido)"
+
+
+def test_tr_quebra_ref_texto_segue_por_linha(tmp_path):
+    """Regressão: não rastreado texto no `<ref>` (quebra `\\n`), regravado com `\\r\\n` — a
+    comparação por linha (`str.splitlines`) segue vencendo quando os dois lados decodificam como
+    UTF-8, mesmo com bytes brutos diferentes (uma regra que comparasse sempre os bytes daria
+    `["dados.txt"]`)."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    (repo / "dados.txt").write_text("ola\n", encoding="utf-8")
+
+    ref = review_evidence.capturar_ref(repo)
+
+    (repo / "dados.txt").write_bytes(b"ola\r\n")
+
+    assert review_evidence.coletar_arquivos_tocados(repo, desde=ref) == []
+
+
+def test_tf_quebra_atribuir_sem_rdo_falha_nomeado(tmp_path, capsys):
+    """RAF-T7 (R-13): `--atribuir` com `--root` sem `.claude/tools/rdo.py` falha nomeada pelo
+    canal do módulo (`review_evidence: FALHOU - rdo.py: módulo não encontrado em`), em vez de
+    deixar a exceção escapar sem essa linha."""
+    review_evidence = _load_review_evidence()
+    plano = tmp_path / "plano.md"
+    _escrever_plano(plano, "cria `src/a.py`.")
+
+    codigo = review_evidence.main(
+        ["--plano"
```
[truncado em 4000 caracteres]

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T7-medida.json; mundo: depois; gerado em: 2026-09-29T06:59:46+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_review_evidence.py -q -k quebra` | 0 | true |

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
