# Evidência de revisão — P-0755 RAF-T14

## Diff (`git diff --stat`)
```
.claude/tools/card_check.py                        |  69 +++++++++++-
 docs/DIARIO_DE_OBRAS.md                            |   4 +-
 .../estado.tsv                                     |   2 +-
 .../evidencia/P-0755-RAF-T14-medida.json           |  29 +++++
 docs/telemetria.tsv                                |   1 +
 tests/test_card_check.py                           | 122 +++++++++++++++++++++
 6 files changed, 219 insertions(+), 8 deletions(-)
```

## Arquivos tocados
- `.claude/tools/card_check.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T14-medida.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_card_check.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `2d2426341d403ca8e2d3953064f90b63afb91f79`
- Arquivos-alvo declarados: `.claude/tools/card_check.py`, `tests/test_card_check.py`
- Arquivos tocados: `.claude/tools/card_check.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T14-medida.json`, `docs/telemetria.tsv`, `tests/test_card_check.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T14-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/card_check.py`
```
diff --git a/.claude/tools/card_check.py b/.claude/tools/card_check.py
index 87ab576..77c378d 100644
--- a/.claude/tools/card_check.py
+++ b/.claude/tools/card_check.py
@@ -112,8 +112,14 @@ _CRASE_RE = re.compile(r"`(?P<val>[^`]*)`")
 # da forma 8.1, antes de cair para `_CRASE_RE`.
 _NEGRITO_RE = re.compile(r"\*\*(?P<val>[^*]+?)\*\*")
 _AFERICAO_MANUAL_RE = re.compile(r"\*\*Aferição:\s*manual\*\*")
-
-_COMANDOS_PERMITIDOS = ("python", "pwsh")
+# Marca de invariância (RAF-T14, DRF-36): item cujo mundo `antes` não é medido — só o mundo
+# `depois` roda o comando.
+_INVARIANCIA_RE = re.compile(r"\(invariância\)")
+
+_COMANDOS_PERMITIDOS = ("python", "pwsh", "git")
+# Subcomandos de leitura do `git` (RAF-T14): o `git` entra na lista fechada só para ler — nenhum
+# subcomando que escreve no índice, na árvore ou nas referências roda.
+_GIT_LEITURA = ("status", "diff", "show", "ls-files", "check-ignore")
 _TOKENS_SHELL_RECUSADOS = frozenset({";", "&&", "||", "|", ">", ">>", "<", "<<"})
 _EXIT_RE = re.compile(r"^exit\s+(-?\d+)$", re.IGNORECASE)
 
@@ -134,6 +140,7 @@ class ItemVerificacao:
         forma: str = "8.1",
         antes: str | None = None,
         depois: str | None = None,
+        invariancia: bool = False,
     ):
         self.indice = indice
         self.comando = comando
@@ -143,6 +150,7 @@ class ItemVerificacao:
         self.forma = forma
         self.antes = antes
         self.depois = depois
+        self.invariancia = invariancia
 
 
 def _parsear_itens(linhas: list[str]) -> tuple[list[ItemVerificacao], list[str]]:
@@ -192,9 +200,16 @@ def _parsear_itens(linhas: list[str]) -> tuple[list[ItemVerificacao], list[str]]
             m_seta = _SETA_RE.search(pos_resto)
             esperado = m_seta.group("esperado").strip() if m_seta else None
             afericao_manual = bool(_AFERICAO_MANUAL_RE.search(pos_resto))
+            invariancia = bool(_INVARIANCIA_RE.search(pos_resto))
             itens.append(
                 ItemVerificacao(
-                    len(itens) + 1, comando, esperado, medido_antes, afericao_manual, forma="8.1"
+                    len(itens) + 1,
+                    comando,
+                    esperado,
+                    medido_antes,
+                    afericao_manual,
+                    forma="8.1",
+                    invariancia=invariancia,
                 )
             )
         elif resto.startswith("`"):
@@ -211,6 +226,7 @@ def _parsear_itens(linhas: list[str]) -> tuple[list[ItemVerificacao], list[str]]
             antes = m_par.group("antes").strip() if m_par else None
             depois = m_par.group("depois").strip() if m_par else None
             afericao_manual = bool(_AFERICAO_MANUAL_RE.search(pos_resto))
+            invariancia = bool(_INVARIANCIA_RE.search(pos_resto))
             itens.append(
                 ItemVerificacao(
                     len(itens) + 1,
@@ -221,6 +237,7 @@ def _parsear_itens(linhas: list[str]) -> tuple[list[ItemVerificacao], list[str]]
                     forma="inline",
                     antes=antes,
                     depois=depois,
+                    invariancia=invariancia,
                 )
             )
         else:
@@ -250,6 +267,10 @@ def _validar_comando(comando: str) -> str | None:
             )
     if not tokens or tokens[0] not in _COMANDOS_PERMITIDOS:
         return f"primeiro token fora da lista fechada {_COMANDOS_PERMITIDOS}"
+    if tokens[0] == "git":
+        segundo = tokens[1] if len(tokens) > 1 else ""
+        if segundo not in _GIT_LEITURA:
+            return f"subcomando git '{segundo}' fora da lista de leitura {_GIT_LEITURA}"
     return None
 
 
@@ -290,6 +311,28 @@ def _literal_do_esperado(esperado: str) -> str | None:
     return None
 
 
+def _ref_do_despacho(root: Path, tarefa_id: str) -> str | None:
+    """`ref` que o `despachar` gravou em `<root>/.claude/estado/tarefa-corrente.json` para
+    `tarefa_id` (RAF-T14, DRF-13 (iii)/(iv)): devolve o `ref` só quando o JSON é objeto
```
[truncado em 4000 caracteres]

### `tests/test_card_check.py`
```
diff --git a/tests/test_card_check.py b/tests/test_card_check.py
index 01e2262..e9a3c00 100644
--- a/tests/test_card_check.py
+++ b/tests/test_card_check.py
@@ -565,3 +565,125 @@ def test_tr_par_com_crase_legado_sem_crase_segue_lido(tmp_path, capsys):
     saida = capsys.readouterr()
     assert codigo == 1
     assert "card_check: FALHOU" in saida.err
+
+
+# --- RAF-T14 (DRF-13 (iii) e (iv), DRF-36): git de leitura, <ref> do despacho, invariância ------
+
+
+def _raiz_com_despacho(tmp_path: Path, tarefa: str, ref: str) -> Path:
+    ferramentas = tmp_path / ".claude" / "tools"
+    ferramentas.mkdir(parents=True)
+    shutil.copy2(_ROOT / ".claude" / "tools" / "rdo.py", ferramentas / "rdo.py")
+    shutil.copy2(_ROOT / ".claude" / "tools" / "caminhos.py", ferramentas / "caminhos.py")
+    estado = tmp_path / ".claude" / "estado"
+    estado.mkdir(parents=True)
+    (estado / "tarefa-corrente.json").write_text(
+        json.dumps({"tarefa": tarefa, "ref": ref}), encoding="utf-8"
+    )
+    return tmp_path
+
+
+def test_tf_git_leitura_roda_ls_files(tmp_path, capsys):
+    """`_COMANDOS_PERMITIDOS` ganha `git`, restrito aos subcomandos de leitura de `_GIT_LEITURA`:
+    `git ls-files tests/test_card_check.py` é um deles — `--mundo antes` sai 0 (hoje sai 1,
+    `primeiro token fora da lista fechada`, porque `git` não estava na lista)."""
+    card_check = _load_card_check()
+    item = (
+        "  1. `git ls-files tests/test_card_check.py` → `tests/test_card_check.py` — "
+        "antes `tests/test_card_check.py`, depois `tests/test_card_check.py`\n"
+    )
+    plano = _plano_com_item(tmp_path, item)
+
+    codigo = _rodar(card_check, plano, "antes")
+    saida = capsys.readouterr()
+
+    assert codigo == 0
+    assert "card_check: OK" in saida.out
+
+
+def test_tf_git_leitura_recusa_subcomando_de_escrita(tmp_path, capsys):
+    """`git commit` não está em `_GIT_LEITURA` — recusado com a razão nomeando o segundo token, e
+    o comando nunca roda (hoje a razão é `primeiro token fora da lista fechada`, sem nomear o
+    subcomando, porque `git` não estava na lista fechada)."""
+    card_check = _load_card_check()
+    item = "  1. `git commit -m x` → `x` — antes `x`, depois `x`\n"
+    plano = _plano_com_item(tmp_path, item)
+
+    codigo = _rodar(card_check, plano, "antes")
+    saida = capsys.readouterr()
+
+    assert codigo == 1
+    assert "card_check: FALHOU" in saida.err
+    assert "subcomando git 'commit' fora da lista de leitura" in saida.err
+
+
+def test_tf_ref_do_despacho_entra_no_comando(tmp_path, capsys):
+    """`<ref>` no comando é trocado pelo valor que o `despachar` gravou em
+    `.claude/estado/tarefa-corrente.json` para a mesma tarefa: raiz com `ref` `abc123` para
+    `RX-T1`, comando que imprime `<ref>` — `--mundo depois` compara com `abc123` e sai 0 (hoje
+    imprime o literal `<ref>` e sai 1)."""
+    card_check = _load_card_check()
+    raiz = _raiz_com_despacho(tmp_path, "RX-T1", "abc123")
+    plano = _plano_com_item(raiz, _bloco("<ref>", "imprime **abc123**", "<ref>"))
+
+    codigo = card_check.main(
+        ["--plano", str(plano), "--tarefa", "RX-T1", "--root", str(raiz), "--mundo", "depois"]
+    )
+    saida = capsys.readouterr()
+
+    assert codigo == 0
+    assert "card_check: OK" in saida.out
+
+
+def test_tr_ref_do_despacho_de_outra_tarefa_falha(tmp_path, capsys):
+    """O `tarefa-corrente.json` é de outra tarefa (`OUTRA-T1`): `_ref_do_despacho` devolve `None`
+    para `RX-T1`, e o item com `<ref>` no comando falha nomeado, sem rodar."""
+    card_check = _load_card_check()
+    raiz = _raiz_com_despacho(tmp_path, "OUTRA-T1", "abc123")
+    plano = _plano_com_item(raiz, _bloco("<ref>", "imprime **abc123**", "<ref>"))
+
+    codigo = card_check.main(
+        ["--plano", str(plano), "--tarefa", "RX-T1", "--root", str(raiz), "--mundo", "depois"]
+    )
+    saida = capsys.readouterr()
+
+    assert codigo == 1
+    assert "card_check: FALHOU" in saida.err
+    assert "item 1: <ref> 
```
[truncado em 4000 caracteres]

## Linhas removidas dos testes
### `tests/test_card_check.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T14-medida.json; mundo: depois; gerado em: 2026-09-29T10:30:43+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_card_check.py -q -k git_leitura` | 0 | true |
| 2 | `python -m pytest tests/test_card_check.py -q -k ref_do_despacho` | 0 | true |
| 3 | `python -m pytest tests/test_card_check.py -q -k invariancia` | 0 | true |

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
