# Evidência de revisão — P-0755 RAF-T15

## Diff (`git diff --stat`)
```
.claude/tools/caminhos.py                          | 23 ++++---
 .claude/tools/card_check.py                        |  6 +-
 .claude/tools/review_evidence.py                   | 17 ++++--
 docs/DIARIO_DE_OBRAS.md                            |  4 +-
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T15-medida-depois.json    | 29 +++++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_caminhos.py                             | 25 +++++++-
 tests/test_card_check.py                           | 61 ++++++++++++++++++-
 tests/test_review_evidence.py                      | 70 ++++++++++++++++++++++
 10 files changed, 215 insertions(+), 23 deletions(-)
```

## Arquivos tocados
- `.claude/tools/caminhos.py` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/card_check.py` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/review_evidence.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T15-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_caminhos.py` — atribuição: da entrega; estado git: ` M`
- `tests/test_card_check.py` — atribuição: da entrega; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `55117ffdbdee195677377fc33ac237e65d74ddb3`
- Arquivos-alvo declarados: `.claude/tools/caminhos.py`, `.claude/tools/card_check.py`, `.claude/tools/review_evidence.py`, `tests/test_caminhos.py`, `tests/test_card_check.py`, `tests/test_review_evidence.py`
- Arquivos tocados: `.claude/tools/caminhos.py`, `.claude/tools/card_check.py`, `.claude/tools/review_evidence.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T15-medida-depois.json`, `docs/telemetria.tsv`, `tests/test_caminhos.py`, `tests/test_card_check.py`, `tests/test_review_evidence.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T15-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/caminhos.py`
```
diff --git a/.claude/tools/caminhos.py b/.claude/tools/caminhos.py
index b2daa37..2d836eb 100644
--- a/.claude/tools/caminhos.py
+++ b/.claude/tools/caminhos.py
@@ -103,17 +103,26 @@ def destino_entrega(raiz: Path, plano_path: Path) -> Path:
     return planos_dir(raiz) / f"_ENTREGA-{id_do_plano(plano_path)}.md"
 
 
-# Destino único da medida do executor (`TK-92a`): plano em pasta grava/procura ao lado do
-# plano; plano legado e tíquete do diário (ex.: `docs/DIARIO_DE_OBRAS.md`) caem em
-# `<raiz>/docs/RDO/evidencia`, com `<id ou stem>` = `id_do_plano(plano_path) or
-# Path(plano_path).stem` — a mesma regra que `review_evidence.py` já usava para o plano_id.
-def destino_medida(raiz: Path, plano_path: Path, tarefa: str) -> Path:
+# Destino único da medida do executor (`TK-92a`, `RAF-T15`/`R-05`): plano em pasta grava/procura
+# na pasta do plano dentro da raiz medida (`planos_dir(raiz) / <pasta> / "evidencia"`, não ao
+# lado do `plano.md` real — a árvore de `plano_path` pode ser uma cópia); plano legado e tíquete
+# do diário (ex.: `docs/DIARIO_DE_OBRAS.md`) caem em `<raiz>/docs/RDO/evidencia`, com
+# `<id ou stem>` = `id_do_plano(plano_path) or Path(plano_path).stem` — a mesma regra que
+# `review_evidence.py` já usava para o plano_id. `mundo` (`"antes"`/`"depois"`/`None`) vira
+# sufixo `-<mundo>` no nome, vazio quando `None`.
+def destino_medida(raiz: Path, plano_path: Path, tarefa: str, mundo: str | None = None) -> Path:
     plano_path = Path(plano_path)
+    sufixo = f"-{mundo}" if mundo is not None else ""
     pasta = pasta_do_plano(plano_path)
     if pasta is not None:
-        return pasta / "evidencia" / f"{id_do_plano(plano_path)}-{tarefa}-medida.json"
+        return (
+            planos_dir(raiz)
+            / pasta.name
+            / "evidencia"
+            / f"{id_do_plano(plano_path)}-{tarefa}-medida{sufixo}.json"
+        )
     plano_id = id_do_plano(plano_path) or plano_path.stem
-    return Path(raiz) / "docs" / "RDO" / "evidencia" / f"{plano_id}-{tarefa}-medida.json"
+    return Path(raiz) / "docs" / "RDO" / "evidencia" / f"{plano_id}-{tarefa}-medida{sufixo}.json"
 
 
 def destino_despacho(raiz: Path, plano_path: Path, tarefa: str) -> Path:

```

### `.claude/tools/card_check.py`
```
diff --git a/.claude/tools/card_check.py b/.claude/tools/card_check.py
index 77c378d..40ff720 100644
--- a/.claude/tools/card_check.py
+++ b/.claude/tools/card_check.py
@@ -634,8 +634,8 @@ def main(argv: list[str] | None = None) -> int:
         default=None,
         help=(
             "Grava a medida (FPU-T5, DFP-17, TK-92a) — com caminho, neste .json; sem caminho, "
-            "em caminhos.destino_medida(--root, --plano, --tarefa) — um registro por item de "
-            "Verificação, ok ou não; não muda exit, stdout nem stderr."
+            "em caminhos.destino_medida(--root, --plano, --tarefa, <mundo>) — um registro por "
+            "item de Verificação, ok ou não; não muda exit, stdout nem stderr."
         ),
     )
     args = parser.parse_args(argv)
@@ -648,7 +648,7 @@ def main(argv: list[str] | None = None) -> int:
 
     if args.gravar is not None:
         destino = (
-            _caminhos.destino_medida(args.root, args.plano, args.tarefa)
+            _caminhos.destino_medida(args.root, args.plano, args.tarefa, medida["mundo"])
             if args.gravar is True
             else args.gravar
         )

```

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index 710818b..1af1aff 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -1146,11 +1146,20 @@ def montar_documento(
 
     plano_id = _caminhos.id_do_plano(plano_path) or plano_path.stem
 
-    caminho_medida = None
+    # RAF-T15 (R-05): a primeira que existir, nesta ordem — ao lado do --out (depois > antes >
+    # sem mundo) e só então na pasta do plano da raiz medida (mesma ordem de mundo); sem nenhuma,
+    # a primeira da lista (a de depois ao lado do --out, ou a de depois na pasta do plano quando
+    # dir_evidencia é None) vai para secao_medida_do_executor, que já imprime "ausente".
+    candidatos_medida: list[Path] = []
     if dir_evidencia is not None:
-        caminho_medida = Path(dir_evidencia) / f"{plano_id}-{dossie.tarefa_id}-medida.json"
-    if caminho_medida is None or not caminho_medida.is_file():
-        caminho_medida = _caminhos.destino_medida(root, plano_path, dossie.tarefa_id)
+        dir_evidencia = Path(dir_evidencia)
+        candidatos_medida.append(dir_evidencia / f"{plano_id}-{dossie.tarefa_id}-medida-depois.json")
+        candidatos_medida.append(dir_evidencia / f"{plano_id}-{dossie.tarefa_id}-medida-antes.json")
+        candidatos_medida.append(dir_evidencia / f"{plano_id}-{dossie.tarefa_id}-medida.json")
+    candidatos_medida.append(_caminhos.destino_medida(root, plano_path, dossie.tarefa_id, "depois"))
+    candidatos_medida.append(_caminhos.destino_medida(root, plano_path, dossie.tarefa_id, "antes"))
+    candidatos_medida.append(_caminhos.destino_medida(root, plano_path, dossie.tarefa_id, None))
+    caminho_medida = next((c for c in candidatos_medida if c.is_file()), candidatos_medida[0])
 
     return _renderizar(
         plano_id=plano_id,

```

### `tests/test_caminhos.py`
```
diff --git a/tests/test_caminhos.py b/tests/test_caminhos.py
index 0e98a0b..16a418b 100644
--- a/tests/test_caminhos.py
+++ b/tests/test_caminhos.py
@@ -35,8 +35,8 @@ def test_tf_san_2_id_do_plano_nas_duas_formas():
 
 def test_tf_destino_medida_tres_residencias():
     """`TK-92a` — `destino_medida` cobre as três residências pela mesma função: tíquete do
-    diário e plano legado caem em `<raiz>/docs/RDO/evidencia`, plano em pasta grava ao lado
-    do plano, em `<pasta>/evidencia`."""
+    diário e plano legado caem em `<raiz>/docs/RDO/evidencia`, plano em pasta grava na pasta do
+    plano sob a raiz, em `<raiz>/docs/plans/<pasta>/evidencia` (`R-05`, RAF-T15)."""
     raiz = Path("/raiz")
 
     assert caminhos.destino_medida(
@@ -49,7 +49,7 @@ def test_tf_destino_medida_tres_residencias():
 
     assert caminhos.destino_medida(
         raiz, Path("docs/plans/P-0002-y/plano.md"), "T2"
-    ) == Path("docs/plans/P-0002-y") / "evidencia" / "P-0002-T2-medida.json"
+    ) == raiz / "docs" / "plans" / "P-0002-y" / "evidencia" / "P-0002-T2-medida.json"
 
 
 def test_tf_san_3_arquivos_de_plano(tmp_path):
@@ -112,3 +112,22 @@ def test_tf_san_6_formatar_id_preserva_largura():
     assert caminhos.formatar_id(750, 4) == "P-0750"
     assert caminhos.formatar_id(1, 1) == "P-1"
     assert caminhos.formatar_id(10, 1) == "P-10"
+
+
+# --- RAF-T15 (R-05): a medida gravada fica na pasta do plano da árvore medida, com o mundo no nome
+
+
+def test_tf_destino_medida_na_raiz_com_o_mundo():
+    """`RAF-T15` (`R-05`) — `destino_medida` recebe `mundo` e grava/procura na pasta do plano
+    dentro da raiz medida, não na árvore real de `plano_path` (que pode ser uma cópia): plano em
+    pasta some sob `raiz` mesmo com `plano_path` apontando para `/real`, e o nome leva o sufixo
+    `-<mundo>`; hoje a função não aceita `mundo` e a pasta vem de `/real`."""
+    raiz = Path("/copia")
+
+    assert caminhos.destino_medida(
+        raiz, Path("/real/docs/plans/P-0002-y/plano.md"), "T2", "depois"
+    ) == raiz / "docs" / "plans" / "P-0002-y" / "evidencia" / "P-0002-T2-medida-depois.json"
+
+    assert caminhos.destino_medida(
+        raiz, Path("/real/docs/plans/P-0001-x.md"), "T1", "antes"
+    ) == raiz / "docs" / "RDO" / "evidencia" / "P-0001-T1-medida-antes.json"

```

### `tests/test_card_check.py`
```
diff --git a/tests/test_card_check.py b/tests/test_card_check.py
index e9a3c00..533f407 100644
--- a/tests/test_card_check.py
+++ b/tests/test_card_check.py
@@ -351,8 +351,10 @@ def test_tf_gravar_sem_caminho_grava_no_destino_derivado(tmp_path, capsys):
     """`TK-92a` — `--gravar` sem caminho grava em `caminhos.destino_medida(--root, --plano,
     --tarefa)`: com `plano-corpus.md` copiado como `docs/DIARIO_DE_OBRAS.md` numa raiz
     temporária (que carrega uma cópia de `rdo.py`/`caminhos.py`, como `verificar_tarefa`
-    exige de qualquer `--root`), o destino é `docs/RDO/evidencia/DIARIO_DE_OBRAS-CX-T1-medida.json`,
-    dentro da própria raiz temporária — nada é gravado no repositório."""
+    exige de qualquer `--root`), o destino é
+    `docs/RDO/evidencia/DIARIO_DE_OBRAS-CX-T1-medida-antes.json`, dentro da própria raiz
+    temporária — nada é gravado no repositório. Desde a `RAF-T15` (`R-05`) o nome leva o mundo
+    efetivo da medida; `CX-T1` da fixture compara o mundo `antes`."""
     card_check = _load_card_check()
     ferramentas = tmp_path / ".claude" / "tools"
     ferramentas.mkdir(parents=True)
@@ -368,7 +370,7 @@ def test_tf_gravar_sem_caminho_grava_no_destino_derivado(tmp_path, capsys):
     capsys.readouterr()
 
     assert codigo == 0
-    destino = tmp_path / "docs" / "RDO" / "evidencia" / "DIARIO_DE_OBRAS-CX-T1-medida.json"
+    destino = tmp_path / "docs" / "RDO" / "evidencia" / "DIARIO_DE_OBRAS-CX-T1-medida-antes.json"
     dados = json.loads(destino.read_text(encoding="utf-8"))
     assert dados["tarefa"] == "CX-T1"
 
@@ -687,3 +689,56 @@ def test_tf_invariancia_nao_medida_antes_e_medida_depois(tmp_path, capsys):
     capsys.readouterr()
 
     assert codigo2 == 1
+
+
+# --- RAF-T15 (R-05): a medida gravada fica na pasta do plano da árvore medida, com o mundo no nome
+
+
+def test_tf_medida_gravada_com_o_mundo_na_pasta_da_raiz(tmp_path, capsys):
+    """`RAF-T15` (`R-05`) — plano em pasta (`P-0007-z`) numa árvore `real`; `--root` aponta para
+    uma árvore `copia` (com cópia de `rdo.py`/`caminhos.py`). `--gravar` sem caminho, rodado uma
+    vez com `--mundo antes` e outra com `--mundo depois`, grava os dois na pasta do plano dentro
+    de `copia`, cada um com o mundo no nome; `real` não ganha pasta de evidência — hoje grava um
+    arquivo só, sem mundo, na árvore `real`."""
+    card_check = _load_card_check()
+    real = tmp_path / "real"
+    copia = tmp_path / "copia"
+    ferramentas = copia / ".claude" / "tools"
+    ferramentas.mkdir(parents=True)
+    shutil.copy2(_ROOT / ".claude" / "tools" / "rdo.py", ferramentas / "rdo.py")
+    shutil.copy2(_ROOT / ".claude" / "tools" / "caminhos.py", ferramentas / "caminhos.py")
+    pasta_plano = real / "docs" / "plans" / "P-0007-z"
+    pasta_plano.mkdir(parents=True)
+    plano = pasta_plano / "plano.md"
+    plano.write_text(
+        "### RX-T1 — Card inline para medida com mundo [Sonnet · classe mecanica]\n"
+        "- **Status:** `ready`\n"
+        "- **Objetivo:** fixture de `card_check` para a `RAF-T15`.\n"
+        "- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.\n"
+        "- **Verificação:**\n"
+        "  1. `python -c \"print('a')\"` → `a` — antes `a`, depois `b`\n"
+        "- **Pronto quando:** fixture existe e `card_check.py --tarefa RX-T1` sai 0.\n",
+        encoding="utf-8",
+    )
+
+    card_check.main(
+        [
+            "--plano", str(plano), "--tarefa", "RX-T1", "--root", str(copia),
+            "--mundo", "antes", "--gravar",
+        ]
+    )
+    capsys.readouterr()
+    card_check.main(
+        [
+            "--plano", str(plano), "--tarefa", "RX-T1", "--root", str(copia),
+            "--mundo", "depois", "--gravar",
+        ]
+    )
+    capsys.readouterr()
+
+    pasta_evidencia = copia / "docs" / "plans" / "P-0007-z" / "evidencia"
+    assert sorted(p.name for p in pasta_evidencia.iterdir()) == [
+        "P-0007-RX-T1-medida-antes.json",
+        "P-0007-RX-T1-medida-depois.json",
+ 
```
[truncado em 4000 caracteres]

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index 78f9c6f..2bcea38 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -2214,3 +2214,73 @@ def test_tr_removidas_de_teste_alvo_e_curinga_uma_entrada(tmp_path):
 
     secao = _secao_removidas(documento)
     assert secao.count("### `tests/test_a.py`") == 1
+
+
+# --- RAF-T15 (R-05): a medida gravada fica na pasta do plano da árvore medida, com o mundo no nome
+
+
+def _gravar_medida(caminho: Path, exit_medido: int) -> None:
+    """Grava uma medida no molde de `_plano_em_pasta_com_medida` (RAF-T7) em `caminho` (RAF-T15),
+    mesmo formato de item, variando só o destino e o `exit`."""
+    caminho.parent.mkdir(parents=True, exist_ok=True)
+    medida = {
+        "plano": str(caminho),
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
+    caminho.write_text(json.dumps(medida, ensure_ascii=False, indent=2), encoding="utf-8")
+
+
+def test_tf_medida_com_mundo_lida_na_ordem(tmp_path):
+    """`RAF-T15` (`R-05`) — sem medida com mundo, `montar_documento` lê a sem mundo (`exit 7`,
+    gravada por `_plano_em_pasta_com_medida`); gravando também `-medida-antes.json` (`exit 5`), a
+    leitura passa a essa; gravando também `-medida-depois.json` (`exit 6`), a leitura passa a
+    essa — a de depois vence sobre a de antes, que vence sobre a sem mundo (hoje sempre lia a
+    sem mundo, `exit 7`, nos três casos)."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    plano = _plano_em_pasta_com_medida(repo, 7)
+    pasta_evidencia = plano.parent / "evidencia"
+
+    documento = review_evidence.montar_documento(
+        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
+    )
+    assert '| 1 | `python -c "print(\'a\')"` | 7 | true |' in documento
+
+    _gravar_medida(pasta_evidencia / "P-0999-T1-medida-antes.json", 5)
+    documento = review_evidence.montar_documento(
+        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
+    )
+    assert '| 1 | `python -c "print(\'a\')"` | 5 | true |' in documento
+
+    _gravar_medida(pasta_evidencia / "P-0999-T1-medida-depois.json", 6)
+    documento = review_evidence.montar_documento(
+        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
+    )
+    assert '| 1 | `python -c "print(\'a\')"` | 6 | true |' in documento
+
+
+def test_tr_medida_com_mundo_sem_mundo_ainda_lida(tmp_path):
+    """Regressão: só a medida sem mundo (formato das vinte já gravadas do `P-0753`) continua lida
+    quando não há `-medida-antes.json` nem `-medida-depois.json`."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    plano = _plano_em_pasta_com_medida(repo, 7)
+
+    documento = review_evidence.montar_documento(
+        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
+    )
+
+    assert '| 1 | `python -c "print(\'a\')"` | 7 | true |' in documento

```

## Linhas removidas dos testes
### `tests/test_caminhos.py` — 3 linha(s) removida(s)
```
-    diário e plano legado caem em `<raiz>/docs/RDO/evidencia`, plano em pasta grava ao lado
-    do plano, em `<pasta>/evidencia`."""
-    ) == Path("docs/plans/P-0002-y") / "evidencia" / "P-0002-T2-medida.json"
```
### `tests/test_card_check.py` — 3 linha(s) removida(s)
```
-    exige de qualquer `--root`), o destino é `docs/RDO/evidencia/DIARIO_DE_OBRAS-CX-T1-medida.json`,
-    dentro da própria raiz temporária — nada é gravado no repositório."""
-    destino = tmp_path / "docs" / "RDO" / "evidencia" / "DIARIO_DE_OBRAS-CX-T1-medida.json"
```
### `tests/test_review_evidence.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T15-medida-depois.json; mundo: depois; gerado em: 2026-09-29T10:50:21+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_caminhos.py -q -k destino_medida_na_raiz` | 0 | true |
| 2 | `python -m pytest tests/test_card_check.py -q -k medida_gravada_com_o_mundo` | 0 | true |
| 3 | `python -m pytest tests/test_review_evidence.py -q -k medida_com_mundo` | 0 | true |

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
