# Evidência de revisão — P-0755 RAF-T31

## Diff (`git diff --stat`)
```
.claude/tools/telemetria.py                        |   75 +
 .claude/tools/telemetria_hook.py                   |   71 +-
 docs/DIARIO_DE_OBRAS.md                            |    4 +-
 .../estado.tsv                                     |    2 +-
 .../evidencia/P-0755-RAF-T31-medida-depois.json    |   22 +
 docs/telemetria.tsv                                | 2425 ++++++++++----------
 tests/test_telemetria.py                           |   21 +
 tests/test_telemetria_hook.py                      |  192 +-
 8 files changed, 1581 insertions(+), 1231 deletions(-)
```

## Arquivos tocados
- `.claude/tools/telemetria.py` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/telemetria_hook.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T31-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_telemetria.py` — atribuição: da entrega; estado git: ` M`
- `tests/test_telemetria_hook.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `754c219f2136b7b127893f638b80cb0401fc7569`
- Arquivos-alvo declarados: `.claude/tools/telemetria_hook.py`, `.claude/tools/telemetria.py`, `tests/test_telemetria_hook.py`, `tests/test_telemetria.py`
- Arquivos tocados: `.claude/tools/telemetria.py`, `.claude/tools/telemetria_hook.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T31-medida-depois.json`, `docs/telemetria.tsv`, `tests/test_telemetria.py`, `tests/test_telemetria_hook.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T31-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/telemetria_hook.py`
```
diff --git a/.claude/tools/telemetria_hook.py b/.claude/tools/telemetria_hook.py
index 2d34e98..d67f3cc 100644
--- a/.claude/tools/telemetria_hook.py
+++ b/.claude/tools/telemetria_hook.py
@@ -72,6 +72,13 @@ _PAPEIS_POR_TAREFA_DO_ESTADO = {"pantonic-reviewer", "pantonic-consultant"}
 
 _RE_ID_PLANO = re.compile(r"P-\d+")
 
+# `R-16`, `DRF-18` do `P-0755`: a linha de abertura do despacho (`despacho: <P-id>[ <ID>]`) manda
+# sobre a prosa livre da mensagem na atribuição de plano e tarefa (`RAF-T31`).
+_RE_LINHA_DESPACHO = re.compile(
+    r"^despacho: (P-\d+)(?: ([A-Z][A-Z0-9]*-T\d+[a-z]?|TK-\d+[a-z]?))? *$",
+    re.MULTILINE,
+)
+
 
 def calcular_consumo(linhas: list[str]) -> tuple[float, int, float]:
     """`(tokens_k, tool_uses, duracao_s)` a partir das linhas cruas do `.jsonl` exclusivo do
@@ -196,6 +203,18 @@ def _primeiro_texto_de_usuario(linhas: list[str]) -> str | None:
     return None
 
 
+def _linha_de_despacho(linhas: list[str]) -> tuple[str, str | None] | None:
+    """`(P-id, ID ou None)` da primeira linha que casa `_RE_LINHA_DESPACHO` no texto da primeira
+    entrada `type == "user"` do transcript (`R-16`, `DRF-18` do `P-0755`); sem ela, `None`."""
+    texto = _primeiro_texto_de_usuario(linhas)
+    if not texto:
+        return None
+    encontrado = _RE_LINHA_DESPACHO.search(texto)
+    if not encontrado:
+        return None
+    return encontrado.group(1), encontrado.group(2)
+
+
 def _id_plano_da_primeira_mensagem(linhas: list[str]) -> str | None:
     """`<P-n>` — primeira ocorrência de `P-` seguido de dígitos no texto da primeira entrada
     `type == "user"` do transcript."""
@@ -240,9 +259,13 @@ def _normalizar_modelo_de_papel(bruto: str | None) -> str:
     return minusculo
 
 
-def _contar_linhas_com_prefixo(tsv_path: Path, prefixo: str) -> int:
+def _contar_linhas_com_prefixo(
+    tsv_path: Path, prefixo: str, excluir_agente: str | None = None
+) -> int:
     """Número de linhas da série cuja coluna `tarefa` começa por `prefixo` — usado para numerar
-    `<tarefa>-consultor-<n>`."""
+    `<tarefa>-consultor-<n>`. Quando o cabeçalho tem a coluna `agente` (`R-16`, `DRF-18` do
+    `P-0755`) e `excluir_agente` é dado, a linha cujo `agente` é ele não é contada — ela vai ser
+    substituída na mesma rodada, não apensada."""
     if not tsv_path.is_file():
         return 0
     linhas = tsv_path.read_text(encoding="utf-8").splitlines()
@@ -253,6 +276,7 @@ def _contar_linhas_com_prefixo(tsv_path: Path, prefixo: str) -> int:
         indice_tarefa = colunas.index("tarefa")
     except ValueError:
         return 0
+    indice_agente = colunas.index("agente") if "agente" in colunas else None
     total = 0
     for linha in linhas[1:]:
         if not linha.strip():
@@ -260,8 +284,16 @@ def _contar_linhas_com_prefixo(tsv_path: Path, prefixo: str) -> int:
         valores = linha.split("\t")
         if len(valores) <= indice_tarefa:
             continue
-        if valores[indice_tarefa].startswith(prefixo):
-            total += 1
+        if not valores[indice_tarefa].startswith(prefixo):
+            continue
+        if (
+            indice_agente is not None
+            and excluir_agente is not None
+            and len(valores) > indice_agente
+            and valores[indice_agente] == excluir_agente
+        ):
+            continue
+        total += 1
     return total
 
 
@@ -315,27 +347,39 @@ def processar(
 
     estado = ler_estado(estado_path)
     linhas = transcript.read_text(encoding="utf-8", errors="ignore").splitlines()
+    agente = Path(agent_transcript_path).stem
+    despacho = _linha_de_despacho(linhas)
 
     if agent_type == _AGENT_TYPE_EXECUTOR:
-        if estado is None:
+        id_despacho = despacho[1] if despacho else None
+        if estado is None and id_despacho is None:
             return False
-        tarefa = str(estado.get("tarefa", ""))
-        modelo = str(estado.get("modelo", ""))
-        projeto = str(estado.get("projeto", ""))
+        tarefa = id_despa
```
[truncado em 4000 caracteres]

### `.claude/tools/telemetria.py`
```
diff --git a/.claude/tools/telemetria.py b/.claude/tools/telemetria.py
index 595e85c..c8c79c2 100644
--- a/.claude/tools/telemetria.py
+++ b/.claude/tools/telemetria.py
@@ -159,6 +159,68 @@ def checar_repetida(path: Path, row: str) -> None:
         )
 
 
+def _tem_coluna_agente(path: Path) -> bool:
+    """`True` quando a série em `path` já tem cabeçalho e a última coluna dele é `agente`
+    (`R-16`, `DRF-18`/`DRF-39` do `P-0755`) — série já migrada pelo escritor de agente."""
+    if not path.exists():
+        return False
+    linhas = path.read_text(encoding="utf-8").splitlines()
+    if not linhas:
+        return False
+    primeira = linhas[0]
+    if not primeira.startswith("data\t"):
+        return False
+    colunas = primeira.split("\t")
+    return bool(colunas) and colunas[-1] == "agente"
+
+
+def gravar_por_agente(path: Path, row: str, agente: str) -> None:
+    """Escreve uma linha por agente na série (`DRF-18`, `DRF-39` do `P-0755`, `R-16`): a linha
+    nova do mesmo `agente` substitui a linha antiga dele, em vez de apensar. Cabeçalho ausente
+    ganha o de `_COLUMNS`; cabeçalho que não termina na coluna `agente` ganha `\tagente`, e cada
+    linha de dado existente ganha `\t-` (a coluna nova nasce vazia para elas). Escrita atômica:
+    arquivo temporário no mesmo diretório e `os.replace`, como `append_row`."""
+    linhas: list[str] = []
+    if path.exists():
+        linhas = [linha for linha in path.read_text(encoding="utf-8").splitlines() if linha]
+
+    if not linhas or not linhas[0].startswith("data\t"):
+        cabecalho = list(_COLUMNS)
+        dados = linhas
+    else:
+        cabecalho = linhas[0].split("\t")
+        dados = linhas[1:]
+
+    if not cabecalho or cabecalho[-1] != "agente":
+        cabecalho = cabecalho + ["agente"]
+        dados = [linha + "\t-" for linha in dados]
+
+    linha_nova = row + "\t" + agente
+    indice_agente = len(cabecalho) - 1
+    substituida = False
+    novas_linhas_dado = []
+    for linha in dados:
+        valores = linha.split("\t")
+        if len(valores) > indice_agente and valores[indice_agente] == agente:
+            novas_linhas_dado.append(linha_nova)
+            substituida = True
+        else:
+            novas_linhas_dado.append(linha)
+    if not substituida:
+        novas_linhas_dado.append(linha_nova)
+
+    conteudo = ("\t".join(cabecalho) + "\n" + "\n".join(novas_linhas_dado) + "\n").encode("utf-8")
+    path.parent.mkdir(parents=True, exist_ok=True)
+    fd, tmp_path = tempfile.mkstemp(dir=str(path.parent), prefix=".telemetria-", suffix=".tmp")
+    try:
+        with os.fdopen(fd, "wb") as tmp_file:
+            tmp_file.write(conteudo)
+        os.replace(tmp_path, path)
+    except Exception:
+        Path(tmp_path).unlink(missing_ok=True)
+        raise
+
+
 def append_row(path: Path, row: str) -> None:
     """Escrita atômica em modo append: lê o conteúdo atual (bytes, sem interpretar), monta
     conteúdo-anterior + linha-nova num arquivo temporário no mesmo diretório, e substitui via
@@ -166,6 +228,11 @@ def append_row(path: Path, row: str) -> None:
     é alterado, só sucedido pela linha nova. Recusa a linha repetida da mesma rodada (DFP-8)
     antes de ler os bytes — a recusa vale para todo escritor, não só o CLI."""
     checar_repetida(path, row)
+    # `DRF-39` do `P-0755`: série já migrada para a coluna `agente` (R-16) recebendo `append_row`
+    # sem `--agente` (escritor que não passa por `gravar_por_agente`) — a linha ganha `-` na
+    # coluna nova para não desalinhar contra o cabeçalho.
+    if _tem_coluna_agente(path) and len(row.split("\t")) == len(_COLUMNS):
+        row = row + "\t-"
     existing = path.read_bytes() if path.exists() else b""
     if existing and not existing.endswith(b"\n"):
         existing += b"\n"
@@ -204,6 +271,10 @@ def main(argv: list[str] | None = None) -> int:
     append_parser.add_argument(
         "--file", type=Path, default=None, help="Caminho do TSV (default: docs/telemet
```
[truncado em 4000 caracteres]

### `tests/test_telemetria_hook.py`
```
diff --git a/tests/test_telemetria_hook.py b/tests/test_telemetria_hook.py
index 1e7edb4..779086a 100644
--- a/tests/test_telemetria_hook.py
+++ b/tests/test_telemetria_hook.py
@@ -293,8 +293,8 @@ def test_tf_processar_payload_de_fixture_grava_linha_esperada_no_tsv(tmp_path):
 
     assert escreveu is True
     linhas = tsv_path.read_text(encoding="utf-8").splitlines()
-    assert linhas[0] == _HEADER.rstrip("\n")
-    assert linhas[1] == "2026-08-19\tPantonicApp\tEXA-T55\tsonnet\t5\t1.0\t0.0\tusage"
+    assert linhas[0] == _HEADER.rstrip("\n") + "\tagente"
+    assert linhas[1] == "2026-08-19\tPantonicApp\tEXA-T55\tsonnet\t5\t1.0\t0.0\tusage\tagent-transcript"
     assert estado_path.exists()
 
 
@@ -329,7 +329,7 @@ def test_tr_processar_sem_tsv_path_grava_na_serie_do_repo_do_estado(tmp_path):
 
     assert escreveu is True
     assert serie.read_text(encoding="utf-8").splitlines()[1] == (
-        "2026-08-19\tPantonicApp\tAE5-TR-SONDA\tsonnet\t2\t1.0\t0.0\tusage"
+        "2026-08-19\tPantonicApp\tAE5-TR-SONDA\tsonnet\t2\t1.0\t0.0\tusage\tagent-transcript"
     )
     assert (real.read_bytes() if real.is_file() else None) == antes_real
 
@@ -559,7 +559,10 @@ def test_tf_hook_executavel_stdin_utf8_nao_falha_e_preserva_invariancia(tmp_path
         "PYTHONUTF8": "1",
     }
     hoje = datetime.date.today().isoformat()
-    linha_esperada = f"{hoje}\tPantonicApp\tEXA-T55\tsonnet\t0\t0.0\t0.0\tusage"
+    linha_esperada = (
+        _HEADER.rstrip("\n") + "\tagente\n"
+        + f"{hoje}\tPantonicApp\tEXA-T55\tsonnet\t0\t0.0\t0.0\tusage\tanálise"
+    )
 
     def _rodar(nome: str, fonte_hook: str, env: dict):
         hook_path, estado_path, tsv_path, transcript_path = _montar_raiz_isolada(
@@ -597,3 +600,184 @@ def test_tf_hook_executavel_stdin_utf8_nao_falha_e_preserva_invariancia(tmp_path
     assert tsv_vh is None
     assert estado_vs is True
     assert tsv_vs is not None and tsv_vs.strip("\n") == linha_esperada
+
+
+def _transcript_com_mensagem(caminho: Path, primeira_mensagem: str, input_tokens: int = 10) -> Path:
+    """Transcript sintético de duas linhas — a primeira mensagem de usuário (`primeira_mensagem`)
+    e uma resposta `assistant` mínima — para os testes de `_linha_de_despacho` e de atribuição
+    por agente (`R-16`, `DRF-18` do `P-0755`, `RAF-T31`)."""
+    caminho.write_text(
+        "\n".join(
+            [
+                _linha_user(primeira_mensagem),
+                _linha_assistant(
+                    {
+                        "input_tokens": input_tokens,
+                        "cache_creation_input_tokens": 0,
+                        "cache_read_input_tokens": 0,
+                        "output_tokens": 0,
+                    },
+                    "2026-09-26T10:00:00+00:00",
+                    n_tool_uses=1,
+                    model="claude-opus-4",
+                ),
+            ]
+        ),
+        encoding="utf-8",
+    )
+    return caminho
+
+
+def test_tf_linha_de_despacho_atribui_o_plano_antes_do_primeiro_id_citado(tmp_path):
+    """TF (`R-16`, `DRF-18` do `P-0755`): a linha de abertura do despacho (`despacho: P-0755`)
+    manda antes de qualquer `P-<n>` citado na prosa livre da mensagem. Concorrente (ler o
+    primeiro `P-<n>` da mensagem inteira, ignorando a linha de despacho): gravaria
+    `P-0700-planejador`, o `P-<n>` do texto de contexto, não o do despacho."""
+    hook = _load_hook()
+
+    estado_path = tmp_path / "estado" / "tarefa-corrente.json"  # nunca criado
+
+    transcript_path = _transcript_com_mensagem(
+        tmp_path / "planejador-transcript.jsonl",
+        "Contexto: veja o P-0700 antes.\ndespacho: P-0755\nPlaneje.",
+    )
+
+    tsv_path = tmp_path / "telemetria.tsv"
+    tsv_path.write_text(_HEADER, encoding="utf-8")
+
+    payload = _payload(agent_type="pantonic-planner", agent_transcript_path=str(transcript_path))
+
+    escreveu = hook.processar(
+        payload, estado_path=estado_path, telemetria_cli=_TELEMETRIA_CLI_PATH, tsv_pa
```
[truncado em 4000 caracteres]

### `tests/test_telemetria.py`
```
diff --git a/tests/test_telemetria.py b/tests/test_telemetria.py
index e943c0e..409c034 100644
--- a/tests/test_telemetria.py
+++ b/tests/test_telemetria.py
@@ -250,3 +250,24 @@ def test_tr_serie_existente_nao_reescrita(tmp_path):
 
     assert exit_code == 3
     assert tsv.read_bytes() == bytes_antes
+
+
+def test_tf_linhas_por_agente_append_sem_agente_em_serie_migrada_leva_traco(tmp_path):
+    """TF (`R-16`, `DRF-39` do `P-0755`): série já migrada para a coluna `agente` (cabeçalho de
+    nove colunas) recebe `append` sem `--agente` — a linha nova ganha `-` na coluna extra, para
+    não desalinhar as colunas. Concorrente (ignorar a coluna nova): a linha sairia com oito
+    colunas, desalinhada com o cabeçalho de nove."""
+    telemetria = _load_telemetria()
+    tsv = tmp_path / "telemetria.tsv"
+    tsv.write_text(_HEADER.rstrip("\n") + "\tagente\n", encoding="utf-8")
+
+    exit_code = telemetria.main(
+        _args(
+            tsv, data="2026-09-28", tarefa="RAF-T1", modelo="sonnet",
+            tool_uses="3", tokens_k="10.0", duracao_s="5.0",
+        )
+    )
+
+    assert exit_code == 0
+    linhas = tsv.read_text(encoding="utf-8").splitlines()
+    assert linhas[-1] == "2026-09-28\tPantonicApp\tRAF-T1\tsonnet\t3\t10.0\t5.0\tusage\t-"

```

## Linhas removidas dos testes
### `tests/test_telemetria_hook.py` — 4 linha(s) removida(s)
```
-    assert linhas[0] == _HEADER.rstrip("\n")
-    assert linhas[1] == "2026-08-19\tPantonicApp\tEXA-T55\tsonnet\t5\t1.0\t0.0\tusage"
-        "2026-08-19\tPantonicApp\tAE5-TR-SONDA\tsonnet\t2\t1.0\t0.0\tusage"
-    linha_esperada = f"{hoje}\tPantonicApp\tEXA-T55\tsonnet\t0\t0.0\t0.0\tusage"
```
### `tests/test_telemetria.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T31-medida-depois.json; mundo: depois; gerado em: 2026-09-30T01:48:41+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_telemetria_hook.py -q -k linha_de_despacho` | 0 | true |
| 2 | `python -m pytest tests/test_telemetria_hook.py tests/test_telemetria.py -q -k linhas_por_agente` | 0 | true |

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
