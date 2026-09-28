# Evidência de revisão — DIARIO_DE_OBRAS TK-89a

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
 .claude/skills/passagem-de-bastao/SKILL.md         |   54 +-
 .claude/skills/redacao-doc/SKILL.md                |    3 +-
 .claude/skills/scrum-master/SKILL.md               |  219 +-
 .claude/tools/backlog.py                           |  584 ++-
 .claude/tools/backlog_hook.py                      |   14 +-
 .claude/tools/card_check.py                        |  403 ++-
 .claude/tools/modelo.py                            |   39 +-
 .claude/tools/rdo.py                               |  322 +-
 .claude/tools/rdo_template.md                      |   12 +-
 .claude/tools/review_evidence.py                   |  170 +-
 .claude/tools/telemetria_hook.py                   |   15 +-
 GOVERNANCA.md                                      |  400 ++-
 README.md                                          |  196 +-
 docs/CUSTO_DO_PICKUP.md                            |  171 +
 docs/DIARIO_DE_OBRAS.md                            | 3745 +++++++++++++++++++-
 docs/DIARIO_HISTORICO.md                           |  154 +
 docs/DOC_MAP.md                                    |  115 +-
 docs/RDO/INDEX.md                                  |  127 +
 docs/RESIDENCIA_DOUTRINA.md                        |    4 +-
 docs/RUBRICA_DE_REVISAO.md                         |   27 +-
 docs/consultant-spec.md                            |   75 +-
 docs/plans/P-0741-modelo-conceitual.md             |    8 +-
 docs/plans/P-0745-planejador-modelo-operacao.md    | 1584 ++++++++-
 docs/plans/_INBOX.md                               |    3 +-
 docs/plans/_INBOX_HISTORICO.md                     |    8 +
 docs/telemetria.tsv                                |  388 ++
 .../backlog/vermelho/docs/DIARIO_DE_OBRAS.md       |    3 +
 tests/fixtures/modelo/fluxo-concluido.md           |   12 +-
 tests/fixtures/modelo/fluxo-pendente.md            |   20 +-
 tests/fixtures/modelo/fluxo-valido.md              |   12 +-
 tests/fixtures/modelo/plano-invalido-2.md          |   10 +-
 tests/fixtures/modelo/plano-invalido.md            |   12 +-
 tests/fixtures/modelo/plano-sem-cabecalho.md       |    8 +-
 tests/fixtures/modelo/plano-sem-estado.md          |    8 +-
 tests/test_backlog.py                              |  819 +++++
 tests/test_card_check.py                           |  208 ++
 tests/test_materializar.py                         |    2 +-
 tests/test_modelo.py                               |  143 +-
 tests/test_rdo.py                                  |  411 ++-
 tests/test_review_evidence.py                      |  286 +-
 tests/test_telemetria_hook.py                      |   35 +
 56 files changed, 10471 insertions(+), 1091 deletions(-)
```

## Arquivos tocados
- `.claude/tools/review_evidence.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-89a-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `d8fd8a2e8c571769352696b38518a7d80dbdaf00`
- Arquivos-alvo declarados: `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`
- Arquivos tocados: `.claude/tools/review_evidence.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-89a-medida.json`, `docs/telemetria.tsv`, `tests/test_review_evidence.py`
- Atribuídos a outra tarefa do mesmo plano: `docs/DIARIO_DE_OBRAS.md` → `TK-54b`, `docs/telemetria.tsv` → `TK-88b`
- Registro da orquestração (não atribuível a tarefa): `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-89a-medida.json`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index b06e479..e57b69f 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -80,6 +80,9 @@ _BACKTICK_RE = re.compile(r"`([^`]+)`")
 _STATUS_DESPACHADO = frozenset({"in-progress", "review", "done"})
 _LINHA_REF_RE = re.compile(r":\d+(-\d+)?$")
 _SECAO_REF_RE = re.compile(r"\s+§\S*$")
+_LITERAL_APOS_ANCORA_RE = re.compile(
+    r"(`[^`\s]+:\d+(?:-\d+)?`)\s*(?:—|:)\s*`(?:\\`|[^`\\])+`"
+)
 
 
 class ReviewEvidenceValidationError(ValueError):
@@ -130,6 +133,7 @@ def _classificar_campo_alvos(campos: dict) -> tuple[list[str], list[str]]:
     """Parte o campo `Arquivos-alvo`/`Entregável` em (alvos, literais descartados), por literal
     entre crases (`DB-27`). Descartado é fato impresso, nunca bloqueio (`DB-19`)."""
     texto = campos.get("arquivos-alvo") or campos.get("entregavel") or ""
+    texto = _LITERAL_APOS_ANCORA_RE.sub(r"\1", texto)
     alvos: dict[str, None] = {}
     descartados: list[str] = []
     for match in _BACKTICK_RE.finditer(texto):

```

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index f1fd721..8e683fd 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -464,7 +464,7 @@ def test_tr_extrair_literais_nao_caminho_lista_o_descartado():
     review_evidence = _load_review_evidence()
     campos = {
         "arquivos-alvo": (
-            "- `.claude/tools/rdo.py:79` — `_ID_HEADER_RE = re.compile(x)` "
+            "- `.claude/tools/rdo.py` — `_ID_HEADER_RE = re.compile(x)` "
             "- `CHANGELOG.md` — uma linha sob `## [Não lançado]` (`CHANGELOG.md:17`)"
         )
     }
@@ -473,6 +473,25 @@ def test_tr_extrair_literais_nao_caminho_lista_o_descartado():
     assert any("re.compile" in item for item in resultado)
 
 
+def test_tf_alvo_ancorado_com_literal_e_um_alvo():
+    """TF da TK-89a: âncora `caminho:linha` seguida do literal dela (mesmo com crase escapada
+    dentro do literal) é cortada antes da varredura por crase — o literal não vai para os
+    descartados e a âncora conta como um alvo só."""
+    review_evidence = _load_review_evidence()
+    campos = {"arquivos-alvo": "- `a/b.md:3` — `x \\` y` - `c/d.py`"}
+    resultado = review_evidence._classificar_campo_alvos(campos)
+    assert resultado == (["a/b.md", "c/d.py"], [])
+
+
+def test_tr_alvo_sem_ancora_nao_muda():
+    """Regressão da TK-89a: campo sem âncora `caminho:linha` (só caminhos entre crases e um
+    literal não caminho) não é afetado pelo corte — mesmo resultado de antes da TK-89a."""
+    review_evidence = _load_review_evidence()
+    campos = {"arquivos-alvo": "- `src/app.py` - `BKL-T9` - `docs/readme.md`"}
+    resultado = review_evidence._classificar_campo_alvos(campos)
+    assert resultado == (["src/app.py", "docs/readme.md"], ["BKL-T9"])
+
+
 def test_tr_extrair_arquivos_alvo_recusa_id_de_tarefa_e_de_decisao():
     """Regressão: identificador de tarefa/decisão entre crases (sem barra e sem extensão) não é
     caminho pela gramática da `DB-27` e não vira alvo declarado."""

```

## Medida do executor
- Arquivo: docs\RDO\evidencia\DIARIO_DE_OBRAS-TK-89a-medida.json; mundo: depois; gerado em: 2026-09-27T01:58:49+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "import sys;sys.path.insert(0,'.claude/tools');import review_evidence as r,rdo;from pathlib import Path;d=rdo.extrair_dossie(Path('docs/plans/P-0752-fato-no-ponto-de-uso.md'),'FPU-T2',esquema_legado=False,modelo_legado=None,classe_legado=None);print(len(r.extrair_arquivos_alvo(d.campos)))"` | 0 | true |
| 2 | `python -m pytest tests/test_review_evidence.py -q -k alvo_ancorado_com_literal` | 0 | true |
| 3 | `python -m pytest -q` | 0 | true |
| 4 | `python -m pytest tests/test_review_evidence.py -q -k literais_nao_caminho_lista` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
