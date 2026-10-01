# Evidência de revisão — P-0755 RAF-T3a

## Diff (`git diff --stat`)
```
.claude/tools/backlog.py                           | 124 +++++++++++++++------
 docs/DIARIO_DE_OBRAS.md                            |   6 +-
 .../estado.tsv                                     |   2 +-
 .../evidencia/P-0755-RAF-T3a-medida.json           |  36 ++++++
 docs/telemetria.tsv                                |   1 +
 tests/test_backlog.py                              | 102 ++++++++++++++++-
 6 files changed, 235 insertions(+), 36 deletions(-)
```

## Arquivos tocados
- `.claude/tools/backlog.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T3a-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_backlog.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `7036a6042b183f25bc377aa70a3151c8416fc757`
- Arquivos-alvo declarados: `.claude/tools/backlog.py`, `tests/test_backlog.py`
- Arquivos tocados: `.claude/tools/backlog.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T3a-medida.json`, `docs/telemetria.tsv`, `tests/test_backlog.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T3a-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/backlog.py`
```
diff --git a/.claude/tools/backlog.py b/.claude/tools/backlog.py
index ecc2937..54ee4fa 100644
--- a/.claude/tools/backlog.py
+++ b/.claude/tools/backlog.py
@@ -2103,23 +2103,36 @@ def _campos_do_card(texto: str) -> dict[str, str]:
     return campos
 
 
-_TRECHO_ANCORA_RE = re.compile(r"`([^`\n]+)`")
-_ANCORA_CAMINHO_LINHA_RE = re.compile(r"^(?P<caminho>[^:\s]+\.[A-Za-z0-9]+):(?P<linha>\d+)(?:-\d+)?$")
+_CODE_SPAN_RE = re.compile(r"(?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)")
+_ANCORA_CAMINHO_LINHA_RE = re.compile(r"^(?P<caminho>[^:\s`]+):(?P<linha>\d+)(?:-\d+)?$")
+_SEPARADOR_LINHA_CITADA_RE = re.compile(r"^[ \t]*[—:][ \t]*$")
 
 
 def conferir_ancoras_do_card(repo: Path, texto_card: str) -> list[str]:
     """RAF-T3 (`DRF-8`, `DRF-35`) — regra fechada: (a) alvos = trechos entre crases do campo
     `Arquivos-alvo` que são arquivo existente sob `repo`, na ordem do card e sem repetição; (b)
     trechos entre crases de `Passos` e, depois, `Contratos/classes`, pulando o menor que 4
-    caracteres, o já visto e o que é um dos alvos; (c) `<caminho>:<n>`/`<caminho>:<n>-<m>` com
-    caminho existente e `n` na faixa de linhas → linha citada com o número e o texto atuais;
-    (d) outro trecho → a primeira linha, do primeiro alvo em ordem, que o contém; (e) sem linha
-    → `- âncora ausente: <trecho>`; (f) item repetido não se repete; sem nenhum → `- nenhuma
-    âncora citada`."""
+    caracteres, o já visto e o que é um dos alvos; (f) item repetido não se repete; sem nenhum →
+    `- nenhuma âncora citada`. RAF-T3a (`DRF-45`) muda o resto da regra: (g) trecho entre crases
+    é o *code span* do Markdown, lido linha a linha do campo: uma sequência de N crases abre, a
+    próxima sequência de exatamente N crases fecha, e o trecho é o que fica entre elas, sem
+    espaços nas pontas; vale também para os alvos de `Arquivos-alvo`. (h) trecho de linha citada
+    é `<caminho>:<n>` (ou `<caminho>:<n>-<m>`); o caminho resolve para ele mesmo quando é arquivo
+    sob `repo` e, se não for, para o primeiro alvo, na ordem do card, cujo caminho termina em `/`
+    mais o caminho citado; resolvido e com `1 <= n <= número de linhas` → `- <caminho
+    resolvido>:<n> — <linha n sem espaços nas pontas>`; senão → `- âncora ausente: <trecho>`.
+    (i) trecho que, na mesma linha do card, vem logo depois de um trecho da forma (h), com só
+    espaços e um `—` ou um `:` entre os dois, é o texto daquela linha citada: a primeira linha
+    do arquivo resolvido que o contém → `- <caminho resolvido>:<k> — <texto da linha sem
+    espaços nas pontas>`; caminho não resolvido ou nenhuma linha que o contenha → `- âncora
+    ausente: <trecho>`. Um trecho da forma (h) pulado por já visto continua abrindo o (i) do
+    trecho seguinte. (j) outro trecho → a primeira linha, do primeiro alvo em ordem, que o
+    contém, como antes; sem linha, o trecho não entra no pacote: não cita linha (comando, nome
+    que a tarefa cria, rótulo de campo)."""
     campos = _campos_do_card(texto_card)
 
     alvos: list[str] = []
-    for trecho in _TRECHO_ANCORA_RE.findall(campos.get("Arquivos-alvo", "")):
+    for _abertura, trecho in _CODE_SPAN_RE.findall(campos.get("Arquivos-alvo", "")):
         caminho = trecho.strip()
         if caminho in alvos:
             continue
@@ -2133,38 +2146,87 @@ def conferir_ancoras_do_card(repo: Path, texto_card: str) -> list[str]:
         if item not in resultado:
             resultado.append(item)
 
-    def _processar(trecho_bruto: str) -> None:
-        trecho = trecho_bruto.strip()
+    def _pode_registrar(trecho: str) -> bool:
         if len(trecho) < 4 or trecho in vistos or trecho in alvos:
-            return
+            return False
         vistos.add(trecho)
+        return True
 
-        m = _ANCORA_CAMINHO_LINHA_RE.match(trecho)
-        if m:
-            caminho = m.group("caminho")
-            n = int(m.group("linha"))
-            alvo_path = Path(repo) / caminho
-            if alvo_path.is_file():
-                linh
```
[truncado em 4000 caracteres]

### `tests/test_backlog.py`
```
diff --git a/tests/test_backlog.py b/tests/test_backlog.py
index f2df391..7d11fbd 100644
--- a/tests/test_backlog.py
+++ b/tests/test_backlog.py
@@ -3232,7 +3232,9 @@ def test_tf_despachar_confere_as_ancoras_do_card(tmp_path, capsys):
         "  - `src/alvo.py`\n"
         "- **Passos:**\n"
         "  1. Editar `src/alvo.py:1` — `x = 1`.\n"
-        "  2. Trocar `return 1` e `texto que sumiu`.\n"
+        "  2. Trocar `return 1`.\n"
+        "- **Contratos/classes:**\n"
+        "  1. `src/alvo.py:2` — `texto que sumiu`.\n"
     )
     plano.write_text(texto_original.replace(bloco_entregavel, bloco_ancoras, 1), encoding="utf-8")
 
@@ -3247,3 +3249,101 @@ def test_tf_despachar_confere_as_ancoras_do_card(tmp_path, capsys):
     assert "- src/alvo.py:1 — x = 1" in pacote
     assert "- src/alvo.py:3 — return 1" in pacote
     assert "- âncora ausente: texto que sumiu" in pacote
+
+
+def test_tf_ancoras_nao_marcam_ausente_o_trecho_que_nao_cita_linha(tmp_path, capsys):
+    """TF da RAF-T3a (`AE-125`): comando, rótulo de campo e fragmento de crase dupla — trechos
+    entre crases que não citam linha — não entram no pacote como ausente; a regra de hoje os
+    marca ausentes."""
+    backlog = _load_backlog()
+    repo = _montar_repo_despachar(tmp_path)
+
+    plano = repo / "docs" / "plans" / "P-0-gama" / "plano.md"
+    texto_original = plano.read_text(encoding="utf-8")
+    bloco_entregavel = "- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.\n"
+    bloco_ancoras = (
+        "- **Arquivos-alvo:**\n"
+        "  - `src/alvo.py`\n"
+        "- **Passos:**\n"
+        "  1. Rodar `python -m pytest -q` e preencher o campo `Testes`.\n"
+        "  2. Conferir ``campo `Testes` do card`` e trocar `return 1`.\n"
+    )
+    plano.write_text(texto_original.replace(bloco_entregavel, bloco_ancoras, 1), encoding="utf-8")
+
+    (repo / "src").mkdir(parents=True, exist_ok=True)
+    (repo / "src" / "alvo.py").write_text("x = 1\ndef alvo():\n    return 1\n", encoding="utf-8")
+
+    assert backlog.main(["despachar", "GAM-T1", "--repo", str(repo)]) == 0
+
+    pacote = (repo / "docs" / "plans" / "P-0-gama" / "despacho" / "GAM-T1.md").read_text(
+        encoding="utf-8"
+    )
+    assert "- src/alvo.py:3 — return 1" in pacote
+    assert "- âncora ausente" not in pacote
+
+
+def test_tf_ancoras_leem_arquivo_sem_extensao_e_caminho_pelo_alvo(tmp_path, capsys):
+    """TF da RAF-T3a: linha citada resolve arquivo sem extensão sob `repo` e caminho citado só
+    pelo nome, pelo alvo cujo caminho termina nele — a regra de hoje marca os dois ausentes."""
+    backlog = _load_backlog()
+    repo = _montar_repo_despachar(tmp_path)
+
+    plano = repo / "docs" / "plans" / "P-0-gama" / "plano.md"
+    texto_original = plano.read_text(encoding="utf-8")
+    bloco_entregavel = "- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.\n"
+    bloco_ancoras = (
+        "- **Arquivos-alvo:**\n"
+        "  - `src/alvo.py`\n"
+        "  - `.alvorc`\n"
+        "- **Passos:**\n"
+        "  1. Aplicar Contratos/classes.\n"
+        "- **Contratos/classes:**\n"
+        "  1. Editar `.alvorc:2` e `alvo.py:3`.\n"
+    )
+    plano.write_text(texto_original.replace(bloco_entregavel, bloco_ancoras, 1), encoding="utf-8")
+
+    (repo / "src").mkdir(parents=True, exist_ok=True)
+    (repo / "src" / "alvo.py").write_text("x = 1\ndef alvo():\n    return 1\n", encoding="utf-8")
+    (repo / ".alvorc").write_text("chave = 1\noutra = 2\n", encoding="utf-8")
+
+    assert backlog.main(["despachar", "GAM-T1", "--repo", str(repo)]) == 0
+
+    pacote = (repo / "docs" / "plans" / "P-0-gama" / "despacho" / "GAM-T1.md").read_text(
+        encoding="utf-8"
+    )
+    assert "- .alvorc:2 — outra = 2" in pacote
+    assert "- src/alvo.py:3 — return 1" in pacote
+    assert "- âncora ausente" not in pacote
+
+
+def test_tr_ancoras_marcam_ausente_a_linha_citada_que_sumiu(tmp_path, capsys):
+    """TR da RAF-T3a (`AE-125`): trecho que cit
```
[truncado em 4000 caracteres]

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T3a-medida.json; mundo: depois; gerado em: 2026-09-29T02:16:21+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_backlog.py -q -k nao_marcam_ausente` | 0 | true |
| 2 | `python -m pytest tests/test_backlog.py -q -k sem_extensao` | 0 | true |
| 3 | `python -m pytest tests/test_backlog.py -q -k linha_citada_que_sumiu` | 0 | true |
| 4 | `python -m pytest tests/test_backlog.py -q -k confere_as_ancoras` | 0 | true |

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
