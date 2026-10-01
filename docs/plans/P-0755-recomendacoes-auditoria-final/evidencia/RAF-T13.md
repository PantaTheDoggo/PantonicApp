# Evidência de revisão — P-0755 RAF-T13

## Diff (`git diff --stat`)
```
.claude/tools/card_check.py                        |  67 +++++++--
 docs/DIARIO_DE_OBRAS.md                            |   4 +-
 .../estado.tsv                                     |   2 +-
 .../evidencia/P-0755-RAF-T13-medida.json           |  22 +++
 docs/telemetria.tsv                                |   1 +
 tests/test_card_check.py                           | 165 +++++++++++++++++++++
 6 files changed, 247 insertions(+), 14 deletions(-)
```

## Arquivos tocados
- `.claude/tools/card_check.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T13-medida.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_card_check.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `e0043041fed40a1513fb2fd38b7010bc13b73993`
- Arquivos-alvo declarados: `.claude/tools/card_check.py`, `tests/test_card_check.py`
- Arquivos tocados: `.claude/tools/card_check.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T13-medida.json`, `docs/telemetria.tsv`, `tests/test_card_check.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T13-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/card_check.py`
```
diff --git a/.claude/tools/card_check.py b/.claude/tools/card_check.py
index fdc20c1..e2b3adc 100644
--- a/.claude/tools/card_check.py
+++ b/.claude/tools/card_check.py
@@ -97,9 +97,19 @@ _SETA_INLINE_RE = re.compile(r"→\s*(?P<esperado>.+?)(?=\s—\s*antes\b|\Z)")
 _ANTES_DEPOIS_RE = re.compile(
     r"antes\s+`?(?P<antes>[^`,;]+)`?[,;]?\s*depois\s+`?(?P<depois>[^`.\n]+)`?"
 )
+# Par `antes`/`depois` com o literal inteiro entre crases (RAF-T13) — aceita `,`, `;` e `.`
+# dentro do valor, porque a extensão é delimitada pela própria crase, não por um caractere de
+# parada; tentada antes da `_ANTES_DEPOIS_RE` (legado), que fica intocada para os cards sem
+# crase no par.
+_ANTES_DEPOIS_CRASE_RE = re.compile(
+    r"antes\s+`(?P<antes>[^`]*)`\s*[,;]?\s*depois\s+`(?P<depois>[^`]*)`"
+)
 # Primeiro trecho entre crases simples — usado tanto para extrair o comando da forma inline
 # quanto para achar o literal dentro de um `esperado` sem par `antes`/`depois`.
 _CRASE_RE = re.compile(r"`(?P<val>[^`]*)`")
+# Primeiro negrito **<valor>** do `esperado` (RAF-T13) — o literal comparado no mundo `depois`
+# da forma 8.1, antes de cair para `_CRASE_RE`.
+_NEGRITO_RE = re.compile(r"\*\*(?P<val>[^*]+?)\*\*")
 _AFERICAO_MANUAL_RE = re.compile(r"\*\*Aferição:\s*manual\*\*")
 
 _COMANDOS_PERMITIDOS = ("python", "pwsh")
@@ -192,7 +202,11 @@ def _parsear_itens(linhas: list[str]) -> tuple[list[ItemVerificacao], list[str]]
             pos_resto = texto_item[m_cmd.end() :] if m_cmd else texto_item[m_num.end() :]
             m_seta = _SETA_INLINE_RE.search(pos_resto)
             esperado = m_seta.group("esperado").strip() if m_seta else None
-            m_par = _ANTES_DEPOIS_RE.search(pos_resto)
+            m_seta_bruta = re.search(r"→", pos_resto)
+            trecho_par = pos_resto[m_seta_bruta.start() :] if m_seta_bruta else pos_resto
+            m_par = _ANTES_DEPOIS_CRASE_RE.search(trecho_par) or _ANTES_DEPOIS_RE.search(
+                trecho_par
+            )
             antes = m_par.group("antes").strip() if m_par else None
             depois = m_par.group("depois").strip() if m_par else None
             afericao_manual = bool(_AFERICAO_MANUAL_RE.search(pos_resto))
@@ -261,6 +275,20 @@ def _bate_com_medido(valor_declarado: str, returncode: int, saida: str) -> bool:
     return valor in saida
 
 
+def _literal_do_esperado(esperado: str) -> str | None:
+    """Literal comparado no mundo `depois` da forma 8.1 (RAF-T13): o primeiro negrito
+    `**<valor>**` do `esperado`; sem negrito, o primeiro trecho entre crases (`_CRASE_RE`); sem
+    nenhum dos dois, `None` — a falha e a decisão de não rodar o item são responsabilidade de
+    quem chama (`verificar_tarefa`)."""
+    m = _NEGRITO_RE.search(esperado)
+    if m:
+        return m.group("val").strip()
+    m = _CRASE_RE.search(esperado)
+    if m:
+        return m.group("val").strip()
+    return None
+
+
 # --- âncoras de arquivo:linha (FPU-T3, DFP-4/DFP-16): toda âncora `<caminho>:<linha>` (ou
 # `<caminho>:<linha>-<fim>`) citada em `Arquivos-alvo` ou `Passos` leva o literal citado logo em
 # seguida (separado por "—" ou ":", entre crases), e o literal precisa estar contido (após
@@ -340,10 +368,12 @@ def verificar_tarefa(
     `{"plano": ..., "tarefa": ..., "mundo": ..., "itens": [...]}` — um registro por item de
     `itens` (`_parsear_itens`), com `exit`/`saida`/`bate` preenchidos só quando o comando roda.
 
-    `mundo` em `{"antes", "depois", None}` — só afeta a forma inline (a forma 8.1 sempre compara
-    `Medido antes`, qualquer que seja o mundo). `None` deriva do bullet `- **Status:**` do card
-    (`rdo._status_atual`): `done` → `depois`; qualquer outro (inclusive ausente) → `antes`. Status
-    ausente imprime o aviso `status ausente: comparando antes`."""
+    `mundo` em `{"antes", "depois", None}` — afeta as duas formas (RAF-T13): na 8.1, `depois`
+    compara com o literal do `esperado` (`_literal_do_esperado`: negrito ou crase) e `antes`
+    segue comparando com `Med
```
[truncado em 4000 caracteres]

### `tests/test_card_check.py`
```
diff --git a/tests/test_card_check.py b/tests/test_card_check.py
index a6e6672..01e2262 100644
--- a/tests/test_card_check.py
+++ b/tests/test_card_check.py
@@ -400,3 +400,168 @@ def test_tr_estado_tsv_ready_compara_antes(capsys):
 
     assert codigo == 0
     assert "card_check: OK" in saida.out
+
+
+# --- RAF-T13 (DRF-13 (i) e (ii)): mundo `depois` na forma 8.1 e literal com pontuação -----------
+
+
+def _plano_com_item(tmp_path: Path, item: str) -> Path:
+    plano = tmp_path / "plano.md"
+    plano.write_text(
+        "### RX-T1 — Card sintético do RAF-T13 [Sonnet · classe mecanica]\n"
+        "- **Objetivo:** fixture de `card_check` para os testes de mundo `depois` na forma 8.1 e "
+        "do par com pontuação no literal da forma inline.\n"
+        "- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.\n"
+        "- **Verificação:**\n"
+        f"{item}"
+        "- **Pronto quando:** fixture existe e `card_check.py --tarefa RX-T1` sai conforme o "
+        "teste.\n",
+        encoding="utf-8",
+    )
+    return plano
+
+
+def _bloco(valor_impresso: str, esperado: str, medido_antes: str) -> str:
+    return (
+        "  1. ```\n"
+        f"     python -c \"print('{valor_impresso}')\"\n"
+        "     ```\n"
+        f"     → {esperado}. **Medido antes: {medido_antes}**\n"
+    )
+
+
+def _rodar(card_check, plano: Path, mundo: str) -> int:
+    return card_check.main(
+        ["--plano", str(plano), "--tarefa", "RX-T1", "--root", str(_ROOT), "--mundo", mundo]
+    )
+
+
+def test_tf_bloco_cercado_mundo_depois_compara_com_o_esperado(tmp_path, capsys):
+    """Bloco cercado que imprime `a`, esperado `imprime **b**`, `Medido antes: a`: `--mundo
+    depois` compara com o literal do esperado (`b`), não com `Medido antes` — diverge e sai 1
+    (hoje sai 0, comparando `a`). O mesmo bloco imprimindo `b` bate com o esperado e sai 0."""
+    card_check = _load_card_check()
+
+    plano = _plano_com_item(tmp_path, _bloco("a", "imprime **b**", "a"))
+    codigo = _rodar(card_check, plano, "depois")
+    saida = capsys.readouterr()
+    assert codigo == 1
+    assert "card_check: FALHOU" in saida.err
+    assert "divergencia - esperado (depois) declara 'b'" in saida.err
+
+    plano = _plano_com_item(tmp_path, _bloco("b", "imprime **b**", "a"))
+    codigo = _rodar(card_check, plano, "depois")
+    saida = capsys.readouterr()
+    assert codigo == 0
+    assert "card_check: OK" in saida.out
+
+
+def test_tr_bloco_cercado_mundo_antes_segue_com_o_medido(tmp_path, capsys):
+    """O mesmo bloco cercado de cima, comparado com `--mundo antes`, segue comparando com
+    `Medido antes` (comportamento de hoje, intocado pela regra nova)."""
+    card_check = _load_card_check()
+
+    plano = _plano_com_item(tmp_path, _bloco("a", "imprime **b**", "a"))
+    codigo = _rodar(card_check, plano, "antes")
+    saida = capsys.readouterr()
+    assert codigo == 0
+    assert "card_check: OK" in saida.out
+
+    plano = _plano_com_item(tmp_path, _bloco("b", "imprime **b**", "a"))
+    codigo = _rodar(card_check, plano, "antes")
+    saida = capsys.readouterr()
+    assert codigo == 1
+    assert "card_check: FALHOU" in saida.err
+    assert "divergencia - Medido antes declara 'a'" in saida.err
+
+
+def test_tf_bloco_cercado_mundo_depois_sem_literal_falha(tmp_path, capsys):
+    """Esperado `imprime o valor`, sem negrito nem crase: `--mundo depois` não tem literal para
+    comparar — o item não roda e `card_check` nomeia `esperado sem literal`."""
+    card_check = _load_card_check()
+
+    plano = _plano_com_item(tmp_path, _bloco("a", "imprime o valor", "a"))
+    codigo = _rodar(card_check, plano, "depois")
+    saida = capsys.readouterr()
+
+    assert codigo == 1
+    assert "card_check: FALHOU" in saida.err
+    assert "item 1: esperado sem literal" in saida.err
+
+
+def test_tf_par_com_crase_depois_aceita_ponto(tmp_path, capsys):
+    """O par `antes`/`depois` com o literal inteiro entre crases aceita ponto dentro
```
[truncado em 4000 caracteres]

## Linhas removidas dos testes
### `tests/test_card_check.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T13-medida.json; mundo: depois; gerado em: 2026-09-29T09:58:20+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_card_check.py -q -k bloco_cercado_mundo` | 0 | true |
| 2 | `python -m pytest tests/test_card_check.py -q -k par_com_crase` | 0 | true |

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
