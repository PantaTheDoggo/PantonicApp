# Evidência de revisão — DIARIO_DE_OBRAS TK-93a

## Diff (`git diff --stat`)
```
.claude/README.md                                  |    8 +-
 .claude/agents/pantonic-consultant.md              |   49 +-
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
 .claude/skills/scrum-master/SKILL.md               |  225 +-
 .claude/tools/backlog.py                           |  584 ++-
 .claude/tools/backlog_hook.py                      |   14 +-
 .claude/tools/card_check.py                        |  423 ++-
 .claude/tools/modelo.py                            |   39 +-
 .claude/tools/rdo.py                               |  322 +-
 .claude/tools/rdo_template.md                      |   12 +-
 .claude/tools/review_evidence.py                   |  301 +-
 .claude/tools/telemetria.py                        |   56 +-
 .claude/tools/telemetria_hook.py                   |   15 +-
 GOVERNANCA.md                                      |  413 ++-
 README.md                                          |  196 +-
 docs/CUSTO_DO_PICKUP.md                            |  171 +
 docs/DIARIO_DE_OBRAS.md                            | 3786 +++++++++++++++++++-
 docs/DIARIO_HISTORICO.md                           |  154 +
 docs/DOC_MAP.md                                    |  115 +-
 docs/RDO/INDEX.md                                  |  135 +
 docs/RESIDENCIA_DOUTRINA.md                        |    4 +-
 docs/RUBRICA_DE_REVISAO.md                         |   27 +-
 docs/consultant-spec.md                            |   75 +-
 docs/plans/P-0741-modelo-conceitual.md             |    8 +-
 docs/plans/P-0742-loop-fora-do-llm.md              |  976 ++++-
 docs/plans/P-0745-planejador-modelo-operacao.md    | 1584 +++++++-
 docs/plans/_INBOX.md                               |    3 +-
 docs/plans/_INBOX_HISTORICO.md                     |    9 +
 docs/telemetria.tsv                                |  411 +++
 .../backlog/vermelho/docs/DIARIO_DE_OBRAS.md       |    3 +
 tests/fixtures/modelo/fluxo-concluido.md           |   12 +-
 tests/fixtures/modelo/fluxo-pendente.md            |   20 +-
 tests/fixtures/modelo/fluxo-valido.md              |   12 +-
 tests/fixtures/modelo/plano-invalido-2.md          |   10 +-
 tests/fixtures/modelo/plano-invalido.md            |   12 +-
 tests/fixtures/modelo/plano-sem-cabecalho.md       |    8 +-
 tests/fixtures/modelo/plano-sem-estado.md          |    8 +-
 tests/test_backlog.py                              |  819 +++++
 tests/test_card_check.py                           |  235 ++
 tests/test_materializar.py                         |    2 +-
 tests/test_modelo.py                               |  143 +-
 tests/test_rdo.py                                  |  411 ++-
 tests/test_review_evidence.py                      |  333 +-
 tests/test_telemetria.py                           |   50 +
 tests/test_telemetria_hook.py                      |   35 +
 59 files changed, 11687 insertions(+), 1280 deletions(-)
```

## Arquivos tocados
- `.claude/skills/scrum-master/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/review_evidence.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-93a-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `b7d7b4b01808090f61a01082789e28a46921d5ea`
- Arquivos-alvo declarados: `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`, `.claude/skills/scrum-master/SKILL.md`
- Arquivos tocados: `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/review_evidence.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-93a-medida.json`, `docs/telemetria.tsv`, `tests/test_review_evidence.py`
- Atribuídos a outra tarefa do mesmo plano: `docs/DIARIO_DE_OBRAS.md` → `TK-54b`, `docs/telemetria.tsv` → `TK-88b`
- Registro da orquestração (não atribuível a tarefa): `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-93a-medida.json`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index 4b98a92..012487a 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -51,10 +51,19 @@ pelos alvos do card; alvo declarado por outra tarefa do mesmo plano; registro da
 (`docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/plans/`, `docs/RDO/`); ato do dono fora
 do ciclo de tarefa (`.claude/agents/`); fora dos alvos
 sem atribuição. Só o último resolve o veredito — `git` não sabe qual tarefa tocou qual arquivo,
-e o plano sabe qual tarefa declarou qual alvo."""
+e o plano sabe qual tarefa declarou qual alvo.
+
+`--capturar-ref` (`TK-93a`) imprime o `<ref>` do despacho (`capturar_ref`) e sai, sem exigir
+`--plano` nem `--tarefa`: um commit cuja árvore é a árvore de trabalho inteira no instante da
+captura, rastreados e não rastreados não ignorados, sem alterar árvore, índice real nem lista de
+stash. Com `--desde <esse ref>`, o não rastreado que já existia na árvore dele é julgado por
+conteúdo (linha a linha, fim de linha normalizado) em vez de por `st_mtime`, e o trecho dele é o
+diff unificado contra o conteúdo em `<ref>` — nunca o de `git diff <ref>`, que o daria como
+apagado por estar fora do índice atual."""
 from __future__ import annotations
 
 import argparse
+import difflib
 import importlib.util
 import json
 import os
@@ -166,10 +175,15 @@ def _forcar_utf8(stream) -> None:
         reconfigure(encoding="utf-8", errors="replace")
 
 
-def _git(args: list[str], root: Path) -> str:
+def _git(args: list[str], root: Path, env: dict[str, str] | None = None) -> str:
     try:
         resultado = subprocess.run(
-            ["git", *args], cwd=str(root), capture_output=True, text=True, encoding="utf-8"
+            ["git", *args],
+            cwd=str(root),
+            capture_output=True,
+            text=True,
+            encoding="utf-8",
+            env=env,
         )
     except FileNotFoundError as exc:
         raise ReviewEvidenceValidationError("git: executável não encontrado no PATH") from exc
@@ -189,6 +203,32 @@ def _diff(args_sem_head: list[str], root: Path) -> str:
         return _git(["diff", *args_sem_head], root)
 
 
+def capturar_ref(root: Path) -> str:
+    """`<ref>` do despacho (`TK-93a`, flag `--capturar-ref`): commit cujo pai é `HEAD` (sem pai em
+    repositório sem commit ainda) e cuja árvore é a árvore de trabalho inteira — rastreados e não
+    rastreados não ignorados —, gravado por um índice temporário (`GIT_INDEX_FILE`); a árvore de
+    trabalho, o índice real e a lista de stash saem exatamente como entraram, porque nada aqui
+    escreve nele."""
+    fd, indice_tmp = tempfile.mkstemp(prefix=".review-evidence-index-", suffix=".tmp")
+    os.close(fd)
+    Path(indice_tmp).unlink()
+    env = dict(os.environ)
+    env["GIT_INDEX_FILE"] = indice_tmp
+    try:
+        _git(["add", "-A"], root, env=env)
+        arvore = _git(["write-tree"], root, env=env).strip()
+        try:
+            pai = _git(["rev-parse", "--verify", "HEAD"], root).strip()
+        except ReviewEvidenceValidationError:
+            pai = None
+        args_commit = ["commit-tree", arvore, "-m", "review_evidence: captura de <ref> (TK-93a)"]
+        if pai is not None:
+            args_commit += ["-p", pai]
+        return _git(args_commit, root, env=env).strip()
+    finally:
+        Path(indice_tmp).unlink(missing_ok=True)
+
+
 def coletar_diff_stat(root: Path) -> str:
     return _diff(["--stat"], root).strip()
 
@@ -200,6 +240,46 @@ def _extrair_caminho_status(linha: str) -> str:
     return caminho.strip().strip('"')
 
 
+def _existe_no_ref(root: Path, ref: str, caminho: str) -> bool:
+    """`git cat-file -e <ref>:<caminho>` — existe como blob na árvore do commit `<ref>`."""
+    return (
+        subprocess.run(
+            ["git", "cat-file", "-e", f"{ref}:{caminho}"],
+            cwd=str(root),
+            capture_output=True,
+        ).returncode
+        == 0
+    )
+
+
```
[truncado em 4000 caracteres]

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index 8e683fd..09dccf5 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -1138,6 +1138,53 @@ def test_tf_trecho_desde_instantaneo_mostra_so_o_delta(tmp_path):
     assert "+linha-velha" not in trechos["a.md"]["texto"]
 
 
+def test_tf_capturar_ref_carrega_nao_rastreado(tmp_path):
+    """TF da TK-93a: `capturar_ref` grava um commit cuja árvore inclui o não rastreado — `git show
+    <ref>:<arquivo>` devolve o conteúdo dele — sem alterar árvore de trabalho, índice real nem
+    lista de stash (`git status` e `git stash list` saem iguais aos de antes da captura)."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    (repo / "novo.txt").write_text("conteudo novo\n", encoding="utf-8")
+
+    status_antes = _run_git(["status", "--porcelain=v1", "--untracked-files=all"], repo)
+    stash_antes = _run_git(["stash", "list"], repo)
+
+    ref = review_evidence.capturar_ref(repo)
+
+    assert _run_git(["show", f"{ref}:novo.txt"], repo) == "conteudo novo\n"
+    assert _run_git(["status", "--porcelain=v1", "--untracked-files=all"], repo) == status_antes
+    assert _run_git(["stash", "list"], repo) == stash_antes
+
+
+def test_tf_nao_rastreado_no_ref_mostra_so_o_hunk(tmp_path):
+    """TF da TK-93a: não rastreado de 400 linhas já presente no `<ref>` (capturado por
+    `capturar_ref`), com uma linha editada depois — o trecho traz a linha nova com `+` e não é
+    truncado no teto de 4000, e `coletar_arquivos_tocados` devolve só ele; outro não rastreado, sem
+    mudança desde `<ref>`, fica de fora."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    linhas = [f"linha-{i}\n" for i in range(400)]
+    (repo / "grande.txt").write_text("".join(linhas), encoding="utf-8")
+    (repo / "estavel.txt").write_text("sem mudanca\n", encoding="utf-8")
+
+    ref = review_evidence.capturar_ref(repo)
+
+    linhas[200] = "linha-200-editada\n"
+    (repo / "grande.txt").write_text("".join(linhas), encoding="utf-8")
+
+    tocados = review_evidence.coletar_arquivos_tocados(repo, desde=ref)
+    assert tocados == ["grande.txt"]
+
+    trechos = review_evidence.montar_trechos(repo, ["grande.txt"], 4000, desde=ref)
+    texto = trechos["grande.txt"]["texto"]
+    assert "+linha-200-editada" in texto
+    assert "-linha-200" in texto
+    assert "linha-399" not in texto
+    assert trechos["grande.txt"]["truncado"] is False
+
+
 def test_tf_trecho_desde_sem_alteracao_nao_despeja_o_arquivo(tmp_path):
     """TF da TK-78c: com `desde=<snap>`, um arquivo-alvo sem alteração desde o instantâneo não
     despeja o conteúdo integral — o texto é exatamente a linha `(sem alteração desde <snap>)`."""

```

### `.claude/skills/scrum-master/SKILL.md`
```
diff --git a/.claude/skills/scrum-master/SKILL.md b/.claude/skills/scrum-master/SKILL.md
index 920b0d5..01b5e38 100644
--- a/.claude/skills/scrum-master/SKILL.md
+++ b/.claude/skills/scrum-master/SKILL.md
@@ -84,10 +84,12 @@ Dez passos, nesta ordem.
   do `P-0740`; recriá-lo se tiver sido apagado nesta máquina) e gravar
   `.claude/estado/tarefa-corrente.json` (objeto único: `tarefa`, `projeto`,
   `modelo`, `plano`, `despachado_em` ISO 8601), insumo do hook `SubagentStop` (`T55`) para
-  `docs/telemetria.tsv`. Capturar como `<ref>` (schema `DP-S`) a saída de `git stash create` —
-  instantâneo dos arquivos rastreados no despacho, que não altera árvore, índice nem a lista de
-  stash —, ou `git rev-parse HEAD` quando ela vier vazia (árvore limpa); usada no passo 6
-  (`AUT-T5b`), onde o trecho de cada alvo passa a mostrar só o que mudou desde o despacho.
+  `docs/telemetria.tsv`. Capturar como `<ref>` (schema `DP-S`) a saída de
+  `python .claude/tools/review_evidence.py --capturar-ref` — instantâneo da árvore de trabalho
+  inteira no despacho, rastreados e não rastreados, que não altera árvore, índice nem a lista de
+  stash; usada no passo 6 (`AUT-T5b`), onde o trecho de cada alvo passa a mostrar só o que mudou
+  desde o despacho. No redespacho da mesma tarefa (retomada depois de `blocked`, ou retentativa),
+  o `<ref>` não se recaptura: vale o do primeiro despacho, para a evidência cobrir as duas execuções.
 
   Invocar `pantonic-executor` com `model` **igual ao do cabeçalho** (vence o `model:` do agente),
   com o dossiê da tarefa e a instrução de devolver **uma única linha**, domínio fechado (`DP-G`

```

## Medida do executor
- Arquivo: docs\RDO\evidencia\DIARIO_DE_OBRAS-TK-93a-medida.json; mundo: depois; gerado em: 2026-09-27T04:31:14+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python .claude/tools/review_evidence.py --capturar-ref` | 0 | true |
| 2 | `python -m pytest tests/test_review_evidence.py -q -k "capturar_ref or nao_rastreado_no_ref"` | 0 | true |
| 3 | `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print(t.count('git stash create'),t.count('review_evidence.py --capturar-ref'),t.count('vale o do primeiro despacho'))"` | 0 | true |
| 4 | `python -m pytest -q` | 0 | true |
| 5 | `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
