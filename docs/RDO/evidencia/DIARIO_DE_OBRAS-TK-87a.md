# Evidência de revisão — DIARIO_DE_OBRAS TK-87a

## Diff (`git diff --stat`)
```
.claude/README.md                                  |    8 +-
 .claude/agents/pantonic-consultant.md              |   43 +-
 .claude/agents/pantonic-executor.md                |   11 +-
 .claude/agents/pantonic-fora-da-caixa.md           |    2 +-
 .claude/agents/pantonic-model-designer.md          |   81 +-
 .claude/agents/pantonic-planner.md                 |  217 +-
 .claude/agents/pantonic-reviewer.md                |   15 +-
 .claude/checks/kit_check.ps1                       |   39 +-
 .claude/global/CLAUDE.md                           |   67 +-
 .../hooks/modelo_por_fase_userpromptsubmit.py      |   13 +-
 .claude/projecoes.json                             |   47 +
 .claude/skills/bootstrap-pantonic/SKILL.md         |    6 +-
 .claude/skills/diario-de-obras/SKILL.md            |  156 +-
 .claude/skills/entrega-de-encerramento/SKILL.md    |    2 +-
 .claude/skills/modelo-por-fase/SKILL.md            |   26 +-
 .claude/skills/passagem-de-bastao/SKILL.md         |   53 +-
 .claude/skills/redacao-doc/SKILL.md                |    3 +-
 .claude/skills/scrum-master/SKILL.md               |  217 +-
 .claude/tools/backlog.py                           |  549 ++-
 .claude/tools/backlog_hook.py                      |   14 +-
 .claude/tools/card_check.py                        |  403 ++-
 .claude/tools/modelo.py                            |   39 +-
 .claude/tools/rdo.py                               |  228 +-
 .claude/tools/rdo_template.md                      |   10 +
 .claude/tools/review_evidence.py                   |  166 +-
 GOVERNANCA.md                                      |  389 ++-
 README.md                                          |  196 +-
 docs/CUSTO_DO_PICKUP.md                            |  171 +
 docs/DIARIO_DE_OBRAS.md                            | 3694 +++++++++++++++++++-
 docs/DIARIO_HISTORICO.md                           |  154 +
 docs/DOC_MAP.md                                    |  115 +-
 docs/RDO/INDEX.md                                  |  121 +
 docs/RESIDENCIA_DOUTRINA.md                        |    4 +-
 docs/RUBRICA_DE_REVISAO.md                         |   27 +-
 docs/consultant-spec.md                            |   75 +-
 docs/plans/P-0741-modelo-conceitual.md             |    8 +-
 docs/plans/P-0745-planejador-modelo-operacao.md    | 1584 ++++++++-
 docs/plans/_INBOX.md                               |    3 +-
 docs/plans/_INBOX_HISTORICO.md                     |    8 +
 docs/telemetria.tsv                                |  378 ++
 .../backlog/vermelho/docs/DIARIO_DE_OBRAS.md       |    3 +
 tests/fixtures/modelo/fluxo-concluido.md           |   12 +-
 tests/fixtures/modelo/fluxo-pendente.md            |   20 +-
 tests/fixtures/modelo/fluxo-valido.md              |   12 +-
 tests/fixtures/modelo/plano-invalido-2.md          |   10 +-
 tests/fixtures/modelo/plano-invalido.md            |   12 +-
 tests/fixtures/modelo/plano-sem-cabecalho.md       |    8 +-
 tests/fixtures/modelo/plano-sem-estado.md          |    8 +-
 tests/test_backlog.py                              |  799 +++++
 tests/test_card_check.py                           |  208 ++
 tests/test_materializar.py                         |    2 +-
 tests/test_modelo.py                               |  143 +-
 tests/test_rdo.py                                  |  357 +-
 tests/test_review_evidence.py                      |  265 +-
 54 files changed, 10144 insertions(+), 1057 deletions(-)
```

## Arquivos tocados
- `.claude/tools/backlog.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-87a-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_backlog.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `67b5e4f5ef6ea23a63e6bbee83538951471c0bc0`
- Arquivos-alvo declarados: `.claude/tools/backlog.py`, `tests/test_backlog.py`
- Arquivos tocados: `.claude/tools/backlog.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-87a-medida.json`, `docs/telemetria.tsv`, `tests/test_backlog.py`
- Atribuídos a outra tarefa do mesmo plano: `docs/DIARIO_DE_OBRAS.md` → `TK-54b`
- Registro da orquestração (não atribuível a tarefa): `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-87a-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/backlog.py`
```
diff --git a/.claude/tools/backlog.py b/.claude/tools/backlog.py
index 40478a7..952b310 100644
--- a/.claude/tools/backlog.py
+++ b/.claude/tools/backlog.py
@@ -300,6 +300,21 @@ def _extrair_tipo(linhas: list[str], inicio_idx: int, fim_idx: int) -> str | Non
     return None
 
 
+def _fim_na_secao(linhas: list[str], inicio_idx: int, fim_idx: int) -> int:
+    """TK-87a — fim do item também corta na primeira linha, entre `inicio_idx + 1` e `fim_idx`,
+    que casa `NIVEL_1_OU_2_RE` fora de cerca de código (```` ``` ```` ou `~~~` abre/fecha).
+    Devolve `fim_idx` sem alteração se nenhuma linha assim existir fora de cerca."""
+    em_cerca = False
+    for j in range(inicio_idx + 1, fim_idx + 1):
+        linha = linhas[j]
+        if linha.startswith("```") or linha.startswith("~~~"):
+            em_cerca = not em_cerca
+            continue
+        if not em_cerca and NIVEL_1_OU_2_RE.match(linha):
+            return j - 1
+    return fim_idx
+
+
 def _scan_items(linhas: list[str], arquivo_rel: str) -> list[Item]:
     heading_idxs = [i for i, l in enumerate(linhas) if HEADING_RE.match(l)]
     itens: list[Item] = []
@@ -332,6 +347,7 @@ def _scan_items(linhas: list[str], arquivo_rel: str) -> list[Item]:
                     esforco_tok = det.group("esforco")
 
         fim_idx = heading_idxs[pos + 1] - 1 if pos + 1 < len(heading_idxs) else len(linhas) - 1
+        fim_idx = _fim_na_secao(linhas, i, fim_idx)
         linha_header = i + 1
         linha_fim = fim_idx + 1
         texto_secao = "\n".join(linhas[i : fim_idx + 1])

```

### `tests/test_backlog.py`
```
diff --git a/tests/test_backlog.py b/tests/test_backlog.py
index 38cb4e8..17cee9b 100644
--- a/tests/test_backlog.py
+++ b/tests/test_backlog.py
@@ -142,6 +142,35 @@ def test_tf_parser_tres_formas_de_id_db14():
     assert all(it.header_valido for it in itens)
 
 
+def test_scan_items_corta_no_nivel_2():
+    backlog = _load_backlog()
+    linhas = [
+        "# P-0999 — Plano",
+        "",
+        "## 5. Tarefas",
+        "",
+        "### X-T1 — Um [Sonnet · esforço low · classe implementacao]",
+        "",
+        "- **Status:** `ready`",
+        "",
+        "~~~~",
+        "## Dentro da cerca",
+        "~~~~",
+        "",
+        "## 6. Ordem de execução",
+        "",
+        "`X-T1`",
+        "",
+        "## 8. Achados",
+        "",
+        "- achado",
+    ]
+    item = backlog._scan_items(linhas, "p.md")[0]
+    assert item.linha_fim == 12
+    assert "## Dentro da cerca" in item.texto
+    assert "## 6. Ordem de execução" not in item.texto
+
+
 def test_tf_status_com_e_sem_razao():
     backlog = _load_backlog()
     linhas_com_razao = [

```

## Medida do executor
- Arquivo: docs\RDO\evidencia\DIARIO_DE_OBRAS-TK-87a-medida.json; mundo: depois; gerado em: 2026-09-26T23:17:35+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "import subprocess,sys;o=subprocess.run([sys.executable,'.claude/tools/backlog.py','show','EBK-T14'],capture_output=True,text=True,encoding='utf-8').stdout;print(sum(1 for l in o.splitlines() if l.startswith('## ')))"` | 0 | true |
| 2 | `python .claude/tools/backlog.py check` | 0 | true |
| 3 | `python -m pytest tests/test_backlog.py -q -k scan_items_corta_no_nivel_2` | 0 | true |
| 4 | `python -m pytest tests/test_backlog.py -q` | 0 | true |
| 5 | `python -m pytest -q` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
