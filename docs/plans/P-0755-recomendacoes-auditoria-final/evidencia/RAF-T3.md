# Evidência de revisão — P-0755 RAF-T3

## Diff (`git diff --stat`)
```
.claude/tools/backlog.py                           | 133 ++++++++++++++++++++-
 .claude/tools/caminhos.py                          |   7 ++
 .gitignore                                         |   5 +
 docs/DIARIO_DE_OBRAS.md                            |   4 +-
 .../estado.tsv                                     |   2 +-
 .../evidencia/P-0755-RAF-T3-medida.json            |  29 +++++
 docs/telemetria.tsv                                |   1 +
 tests/test_backlog.py                              | 101 ++++++++++++++++
 8 files changed, 275 insertions(+), 7 deletions(-)
```

## Arquivos tocados
- `.claude/tools/backlog.py` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/caminhos.py` — atribuição: da entrega; estado git: ` M`
- `.gitignore` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T3-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_backlog.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `830cab272d7f3a25ac723c40aa69560e5ff11640`
- Arquivos-alvo declarados: `.claude/tools/backlog.py`, `.claude/tools/caminhos.py`, `.gitignore`, `tests/test_backlog.py`
- Arquivos tocados: `.claude/tools/backlog.py`, `.claude/tools/caminhos.py`, `.gitignore`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T3-medida.json`, `docs/telemetria.tsv`, `tests/test_backlog.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T3-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/backlog.py`
```
diff --git a/.claude/tools/backlog.py b/.claude/tools/backlog.py
index 942533c..ecc2937 100644
--- a/.claude/tools/backlog.py
+++ b/.claude/tools/backlog.py
@@ -2080,6 +2080,95 @@ def _ultima_linha_stderr(texto: str) -> str:
     return linhas[-1] if linhas else ""
 
 
+_CAMPO_CARD_RE = re.compile(r"^- \*\*(?P<rotulo>[^*]+):\*\*(?P<resto>.*)$")
+
+
+def _campos_do_card(texto: str) -> dict[str, str]:
+    """RAF-T3 — cada linha que abre um campo de topo do card (`- **<rótulo>:**`) inicia um
+    campo cujo texto vai do resto da linha até a linha anterior ao próximo campo."""
+    campos: dict[str, str] = {}
+    rotulo_atual: str | None = None
+    linhas_atual: list[str] = []
+    for linha in texto.splitlines():
+        m = _CAMPO_CARD_RE.match(linha)
+        if m:
+            if rotulo_atual is not None:
+                campos[rotulo_atual] = "\n".join(linhas_atual)
+            rotulo_atual = m.group("rotulo").strip()
+            linhas_atual = [m.group("resto")]
+        elif rotulo_atual is not None:
+            linhas_atual.append(linha)
+    if rotulo_atual is not None:
+        campos[rotulo_atual] = "\n".join(linhas_atual)
+    return campos
+
+
+_TRECHO_ANCORA_RE = re.compile(r"`([^`\n]+)`")
+_ANCORA_CAMINHO_LINHA_RE = re.compile(r"^(?P<caminho>[^:\s]+\.[A-Za-z0-9]+):(?P<linha>\d+)(?:-\d+)?$")
+
+
+def conferir_ancoras_do_card(repo: Path, texto_card: str) -> list[str]:
+    """RAF-T3 (`DRF-8`, `DRF-35`) — regra fechada: (a) alvos = trechos entre crases do campo
+    `Arquivos-alvo` que são arquivo existente sob `repo`, na ordem do card e sem repetição; (b)
+    trechos entre crases de `Passos` e, depois, `Contratos/classes`, pulando o menor que 4
+    caracteres, o já visto e o que é um dos alvos; (c) `<caminho>:<n>`/`<caminho>:<n>-<m>` com
+    caminho existente e `n` na faixa de linhas → linha citada com o número e o texto atuais;
+    (d) outro trecho → a primeira linha, do primeiro alvo em ordem, que o contém; (e) sem linha
+    → `- âncora ausente: <trecho>`; (f) item repetido não se repete; sem nenhum → `- nenhuma
+    âncora citada`."""
+    campos = _campos_do_card(texto_card)
+
+    alvos: list[str] = []
+    for trecho in _TRECHO_ANCORA_RE.findall(campos.get("Arquivos-alvo", "")):
+        caminho = trecho.strip()
+        if caminho in alvos:
+            continue
+        if (Path(repo) / caminho).is_file():
+            alvos.append(caminho)
+
+    resultado: list[str] = []
+    vistos: set[str] = set()
+
+    def _acrescentar(item: str) -> None:
+        if item not in resultado:
+            resultado.append(item)
+
+    def _processar(trecho_bruto: str) -> None:
+        trecho = trecho_bruto.strip()
+        if len(trecho) < 4 or trecho in vistos or trecho in alvos:
+            return
+        vistos.add(trecho)
+
+        m = _ANCORA_CAMINHO_LINHA_RE.match(trecho)
+        if m:
+            caminho = m.group("caminho")
+            n = int(m.group("linha"))
+            alvo_path = Path(repo) / caminho
+            if alvo_path.is_file():
+                linhas_alvo = alvo_path.read_text(encoding="utf-8", errors="replace").splitlines()
+                if 1 <= n <= len(linhas_alvo):
+                    _acrescentar(f"- {caminho}:{n} — {linhas_alvo[n - 1].strip()}")
+                    return
+
+        for caminho in alvos:
+            linhas_alvo = (Path(repo) / caminho).read_text(
+                encoding="utf-8", errors="replace"
+            ).splitlines()
+            achado = next((i for i, l in enumerate(linhas_alvo, start=1) if trecho in l), None)
+            if achado is not None:
+                _acrescentar(f"- {caminho}:{achado} — {linhas_alvo[achado - 1].strip()}")
+                return
+
+        _acrescentar(f"- âncora ausente: {trecho}")
+
+    for trecho in _TRECHO_ANCORA_RE.findall(campos.get("Passos", "")):
+        _processar(trecho)
+    for trecho in _TRECHO_ANCORA_RE.findall(campos.get("Contratos/classes", "")):
+        _processar(trecho)
+
+    return result
```
[truncado em 4000 caracteres]

### `.claude/tools/caminhos.py`
```
diff --git a/.claude/tools/caminhos.py b/.claude/tools/caminhos.py
index 0b1d1f8..b2daa37 100644
--- a/.claude/tools/caminhos.py
+++ b/.claude/tools/caminhos.py
@@ -116,6 +116,13 @@ def destino_medida(raiz: Path, plano_path: Path, tarefa: str) -> Path:
     return Path(raiz) / "docs" / "RDO" / "evidencia" / f"{plano_id}-{tarefa}-medida.json"
 
 
+def destino_despacho(raiz: Path, plano_path: Path, tarefa: str) -> Path:
+    pasta = pasta_do_plano(plano_path)
+    if pasta is not None:
+        return pasta / "despacho" / f"{tarefa}.md"
+    return Path(raiz) / "docs" / "RDO" / "despacho" / f"{tarefa}.md"
+
+
 def main(argv: list[str] | None = None) -> int:
     """Lista os planos da raiz, um por linha: `<id><TAB><caminho relativo à raiz>`."""
     parser = argparse.ArgumentParser(description="Lista os planos, legado e em pasta.")

```

### `.gitignore`
```
diff --git a/.gitignore b/.gitignore
index 38b12bd..d45fcd3 100644
--- a/.gitignore
+++ b/.gitignore
@@ -11,6 +11,11 @@
 .claude/estado/*
 !.claude/estado/.gitkeep
 
+# Pacote do despacho (`R-02`, `P-0755`): projeção regenerável do card, gravada por
+# `backlog.py despachar` a cada despacho — nunca se versiona.
+docs/plans/*/despacho/
+docs/RDO/despacho/
+
 # Bytecode do Python — a suíte do hub (`tests/`) carrega os verificadores de
 # `.claude/checks/` por caminho, e cada rodada grava `__pycache__/` ao lado deles
 __pycache__/

```

### `tests/test_backlog.py`
```
diff --git a/tests/test_backlog.py b/tests/test_backlog.py
index bc8df89..f2df391 100644
--- a/tests/test_backlog.py
+++ b/tests/test_backlog.py
@@ -3146,3 +3146,104 @@ def test_tr_despachar_mundo_depois_redespacha_tarefa_ja_aplicada(tmp_path, capsy
     estado_tsv = (repo / "docs" / "plans" / "P-0-gama" / "estado.tsv").read_text(encoding="utf-8")
     linha_gam_t1 = next(l for l in estado_tsv.splitlines() if l.startswith("GAM-T1\t"))
     assert linha_gam_t1.split("\t")[2] == "in-progress"
+
+
+# --------------------------------------------------------------------------- #
+# RAF-T3 — o despacho grava o pacote da tarefa num arquivo fora do versionamento e
+# imprime só o recado ao executor.
+# --------------------------------------------------------------------------- #
+
+
+def test_tf_despachar_grava_o_pacote_na_pasta_do_plano(tmp_path, capsys):
+    """TF da RAF-T3: `despachar GAM-T1` grava o pacote da tarefa (card, handovers e âncoras
+    conferidas) em `<pasta do plano>/despacho/<ID>.md` — a regra de hoje não grava arquivo
+    nenhum."""
+    backlog = _load_backlog()
+    repo = _montar_repo_despachar(tmp_path)
+
+    assert backlog.main(["despachar", "GAM-T1", "--repo", str(repo)]) == 0
+
+    pacote = repo / "docs" / "plans" / "P-0-gama" / "despacho" / "GAM-T1.md"
+    texto = pacote.read_text(encoding="utf-8")
+    assert "### GAM-T1 — Primeira tarefa [Sonnet · classe implementacao]" in texto
+    assert "despacho: P-0 GAM-T1" in texto
+    assert "## Âncoras conferidas" in texto
+
+
+def test_tr_despachar_recusado_nao_grava_o_pacote(tmp_path, capsys):
+    """TR da RAF-T3: `GAM-T2` é recusado pelo gate `card_check` — a pasta `despacho/` não
+    existe, porque a gravação do pacote só acontece depois da última checagem passar."""
+    backlog = _load_backlog()
+    repo = _montar_repo_despachar(tmp_path)
+
+    assert backlog.main(["despachar", "GAM-T2", "--repo", str(repo)]) == 1
+
+    pasta_despacho = repo / "docs" / "plans" / "P-0-gama" / "despacho"
+    assert not pasta_despacho.exists()
+
+
+def test_tf_gitignore_ignora_o_pacote_do_despacho():
+    """TF da RAF-T3: o pacote do despacho nunca se versiona, no layout de plano em pasta e no
+    de plano legado/tíquete — hoje `git check-ignore -q` sai 1 para os dois."""
+    caminhos = [
+        "docs/plans/P-0755-recomendacoes-auditoria-final/despacho/RAF-T1.md",
+        "docs/RDO/despacho/TK-1.md",
+    ]
+    for caminho in caminhos:
+        resultado = subprocess.run(
+            ["git", "check-ignore", "-q", caminho], cwd=str(_ROOT), capture_output=True
+        )
+        assert resultado.returncode == 0, caminho
+
+
+def test_tf_despachar_imprime_o_texto_pronto_ao_executor(tmp_path, capsys):
+    """TF da RAF-T3: a tela de quem despacha recebe só o recado pronto ao executor, não o card
+    inteiro — hoje o card inteiro sai na tela."""
+    backlog = _load_backlog()
+    repo = _montar_repo_despachar(tmp_path)
+
+    assert backlog.main(["despachar", "GAM-T1", "--repo", str(repo)]) == 0
+
+    linhas = capsys.readouterr().out.splitlines()
+    assert linhas[0] == "=== DESPACHO: GAM-T1 — Primeira tarefa"
+    assert linhas[1] == "despacho: P-0 GAM-T1"
+    assert "docs/plans/P-0-gama/despacho/GAM-T1.md" in linhas[2]
+    assert "GAM-T1 review" in linhas
+    assert "GAM-T1 review pendencia=<uma linha>" in linhas
+    assert (
+        "GAM-T1 blocked motivo=<dependencia|premissa|ferramenta> <uma linha de razão>" in linhas
+    )
+    assert linhas[-1].startswith("ref=")
+    assert "- **Objetivo:** fixture." not in "\n".join(linhas)
+
+
+def test_tf_despachar_confere_as_ancoras_do_card(tmp_path, capsys):
+    """TF da RAF-T3: o pacote traz cada âncora citada em `Arquivos-alvo`/`Passos` com o número
+    e o texto atuais da linha, e marca ausente o texto que já não está no arquivo — hoje o
+    despacho não confere nenhuma âncora."""
+    backlog = _load_backlog()
+    repo = _montar_repo_despachar(tmp_path)
+
+    plano = repo / "docs" / "plans" / "P-0-
```
[truncado em 4000 caracteres]

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T3-medida.json; mundo: depois; gerado em: 2026-09-29T01:50:34+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_backlog.py -q -k pacote` | 0 | true |
| 2 | `python -m pytest tests/test_backlog.py -q -k texto_pronto` | 0 | true |
| 3 | `python -m pytest tests/test_backlog.py -q -k confere_as_ancoras` | 0 | true |

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
