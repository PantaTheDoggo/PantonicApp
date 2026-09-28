# Evidência de revisão — DIARIO_DE_OBRAS TK-84a

## Diff (`git diff --stat`)
```
.claude/README.md                                  |    8 +-
 .claude/agents/pantonic-consultant.md              |   43 +-
 .claude/agents/pantonic-executor.md                |   11 +-
 .claude/agents/pantonic-fora-da-caixa.md           |    2 +-
 .claude/agents/pantonic-model-designer.md          |   81 +-
 .claude/agents/pantonic-planner.md                 |  217 +-
 .claude/agents/pantonic-reviewer.md                |   10 +-
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
 .claude/tools/backlog.py                           |  482 ++-
 .claude/tools/backlog_hook.py                      |   14 +-
 .claude/tools/card_check.py                        |  403 ++-
 .claude/tools/modelo.py                            |   39 +-
 .claude/tools/rdo.py                               |  172 +-
 .claude/tools/rdo_template.md                      |   10 +
 .claude/tools/review_evidence.py                   |  166 +-
 GOVERNANCA.md                                      |  389 ++-
 README.md                                          |  196 +-
 docs/CUSTO_DO_PICKUP.md                            |  171 +
 docs/DIARIO_DE_OBRAS.md                            | 3543 ++++++++++++++++++--
 docs/DIARIO_HISTORICO.md                           |  154 +
 docs/DOC_MAP.md                                    |  115 +-
 docs/RDO/INDEX.md                                  |  120 +
 docs/RESIDENCIA_DOUTRINA.md                        |    4 +-
 docs/RUBRICA_DE_REVISAO.md                         |   27 +-
 docs/consultant-spec.md                            |   75 +-
 docs/plans/P-0741-modelo-conceitual.md             |    8 +-
 docs/plans/P-0745-planejador-modelo-operacao.md    | 1584 ++++++++-
 docs/plans/_INBOX.md                               |    3 +-
 docs/plans/_INBOX_HISTORICO.md                     |    8 +
 docs/telemetria.tsv                                |  373 +++
 .../backlog/vermelho/docs/DIARIO_DE_OBRAS.md       |    3 +
 tests/fixtures/modelo/fluxo-concluido.md           |   12 +-
 tests/fixtures/modelo/fluxo-pendente.md            |   20 +-
 tests/fixtures/modelo/fluxo-valido.md              |   12 +-
 tests/fixtures/modelo/plano-invalido-2.md          |   10 +-
 tests/fixtures/modelo/plano-invalido.md            |   12 +-
 tests/fixtures/modelo/plano-sem-cabecalho.md       |    8 +-
 tests/fixtures/modelo/plano-sem-estado.md          |    8 +-
 tests/test_backlog.py                              |  746 +++++
 tests/test_card_check.py                           |  208 ++
 tests/test_materializar.py                         |    2 +-
 tests/test_modelo.py                               |  143 +-
 tests/test_rdo.py                                  |  284 +-
 tests/test_review_evidence.py                      |  265 +-
 54 files changed, 9749 insertions(+), 1041 deletions(-)
```

## Arquivos tocados
- `.claude/tools/review_evidence.py` — atribuição: da entrega; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `298f84057e1d37f83e3c7e8ba5bc4b7283b7895a`
- Arquivos-alvo declarados: `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`
- Arquivos tocados: `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index 9b13746..b06e479 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -206,8 +206,10 @@ def coletar_arquivos_tocados(root: Path, desde: str | None = None) -> list[str]:
     Com `desde=<ref>` (AUT-T5b): recorta o conjunto de rastreados para só os alterados **desde**
     `<ref>` (`git diff <ref> --name-only`), em vez da árvore de trabalho inteira — necessário
     quando outras tarefas têm mudanças soltas, não commitadas, no mesmo repositório. Untracked
-    nunca é "desde um ref" (não existe no histórico), então as entradas `??` do `git status`
-    entram sempre, com ou sem `desde`."""
+    não existe no histórico, então o recorte dele é pela data: a entrada `??` cujo arquivo tem
+    `st_mtime` menor que a data de commit de `<ref>` (`%ct`) fica de fora; a de data igual ou
+    maior entra, e também a que não existe no disco como veio do `git status` (nome entre aspas
+    com escape octal, por exemplo)."""
     saida_status = _git(["status", "--porcelain=v1", "--untracked-files=all"], root)
     tocados: dict[str, None] = {}
     if desde is None:
@@ -217,10 +219,15 @@ def coletar_arquivos_tocados(root: Path, desde: str | None = None) -> list[str]:
             tocados.setdefault(_extrair_caminho_status(linha), None)
         return sorted(tocados.keys())
 
+    corte = int(_git(["show", "-s", "--format=%ct", desde], root).strip())
     for linha in saida_status.splitlines():
         if not linha.startswith("??"):
             continue
-        tocados.setdefault(_extrair_caminho_status(linha), None)
+        caminho = _extrair_caminho_status(linha)
+        arquivo = root / caminho
+        if arquivo.exists() and arquivo.stat().st_mtime < corte:
+            continue
+        tocados.setdefault(caminho, None)
     saida_diff = _git(["diff", desde, "--name-only"], root)
     for linha in saida_diff.splitlines():
         linha = linha.strip()

```

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index 33f3da6..f1fd721 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -15,6 +15,7 @@ from __future__ import annotations
 
 import importlib.util
 import json
+import os
 import shutil
 import subprocess
 from pathlib import Path
@@ -380,8 +381,8 @@ def test_alvo_diretorio_casa_por_prefixo_com_arquivo_tocado_dentro(tmp_path):
 def test_desde_recorta_tocados_a_partir_da_referencia(tmp_path):
     """AUT-T5b: `--desde <ref>` recorta o conjunto de tocados — só arquivos rastreados alterados
     **depois** de `<ref>` entram; um arquivo que já divergia do HEAD anterior mas não mudou depois
-    do `<ref>` fica de fora. Untracked sempre entra, com ou sem `--desde` (não existe no histórico,
-    então nunca é "desde um ref")."""
+    do `<ref>` fica de fora. Untracked criado depois do `<ref>` entra (o anterior sai pela data —
+    TK-84a)."""
     review_evidence = _load_review_evidence()
     repo = tmp_path / "repo"
     _init_repo_com_baseline(repo)
@@ -400,6 +401,29 @@ def test_desde_recorta_tocados_a_partir_da_referencia(tmp_path):
     assert tocados == ["src/b.py", "src/d.py"]
 
 
+def test_coletar_nao_rastreado_anterior_ao_desde_sai_dos_tocados(tmp_path):
+    """TF da TK-84a: com `desde=<ref>`, o não rastreado com `st_mtime` anterior à data de commit
+    de `<ref>` sai dos tocados e o posterior entra; sem `desde`, o anterior continua na lista."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    ref = _run_git(["rev-parse", "HEAD"], repo).strip()
+    ct = int(_run_git(["show", "-s", "--format=%ct", ref], repo).strip())
+
+    velho = repo / "src" / "velho.py"
+    velho.write_text("def velho():\n    return 1\n", encoding="utf-8")
+    os.utime(velho, (ct - 60, ct - 60))
+    novo = repo / "src" / "novo.py"
+    novo.write_text("def novo():\n    return 2\n", encoding="utf-8")
+    os.utime(novo, (ct + 60, ct + 60))
+
+    tocados_desde = review_evidence.coletar_arquivos_tocados(repo, desde=ref)
+    assert "src/novo.py" in tocados_desde
+    assert "src/velho.py" not in tocados_desde
+
+    assert "src/velho.py" in review_evidence.coletar_arquivos_tocados(repo)
+
+
 def test_escopo_declara_recorte_arvore_inteira_sem_desde(tmp_path):
     """AUT-T5b: sem `--desde`, a seção `## Escopo` declara explicitamente que o recorte medido é a
     árvore de trabalho inteira — o dossiê nunca afirma escopo que não mediu."""

```

## Medida do executor
- ausente: docs\RDO\evidencia\DIARIO_DE_OBRAS-TK-84a-medida.json não existe

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
