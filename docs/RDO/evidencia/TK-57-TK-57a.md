# Evidência de revisão — DIARIO_DE_OBRAS TK-57a

## Diff (`git diff --stat`)
```
.claude/projecoes.json                           |   10 +
 .claude/skills/passagem-de-bastao/SKILL.md       |   35 +-
 .claude/skills/scrum-master/SKILL.md             |   23 +-
 .claude/tools/backlog.py                         |  289 ++-
 .claude/tools/rdo.py                             |    6 +-
 CHANGELOG.md                                     |   15 +-
 GOVERNANCA.md                                    |    2 +-
 README.md                                        |   33 +-
 docs/CUSTO_DO_PICKUP.md                          |   31 +
 docs/DIARIO_DE_OBRAS.md                          |  520 ++++-
 docs/DOC_MAP.md                                  |    2 +
 docs/RDO/INDEX.md                                |    6 +
 docs/consultant-spec.md                          |   66 +
 docs/plans/P-0735-residencia-e-ponto-de-carga.md |    2 +-
 docs/plans/P-0737-loop-autonomo.md               |    2 +-
 docs/plans/P-0738-contexto-esgotado.md           |    2 +-
 docs/plans/P-0739-backlog-instrumento.md         | 2526 +++++++++++++++++++++-
 docs/plans/_INBOX.md                             |    2 +-
 docs/plans/_INBOX_HISTORICO.md                   |    1 +
 docs/telemetria.tsv                              |   39 +
 tests/test_backlog.py                            |  635 +++++-
 tests/test_rdo.py                                |   34 +
 tests/test_review_evidence.py                    |   37 +
 23 files changed, 4148 insertions(+), 170 deletions(-)
```

## Arquivos tocados
- `.claude/projecoes.json` — atribuição: alheio; estado git: ` M`
- `.claude/skills/entrega-de-encerramento/SKILL.md` — atribuição: alheio; estado git: `??`
- `.claude/skills/passagem-de-bastao/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/scrum-master/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/tools/backlog.py` — atribuição: alheio; estado git: ` M`
- `.claude/tools/backlog_hook.py` — atribuição: alheio; estado git: `??`
- `.claude/tools/rdo.py` — atribuição: alheio; estado git: ` M`
- `CHANGELOG.md` — atribuição: alheio; estado git: ` M`
- `GOVERNANCA.md` — atribuição: alheio; estado git: ` M`
- `README.md` — atribuição: alheio; estado git: ` M`
- `docs/CUSTO_DO_PICKUP.md` — atribuição: alheio; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/DOC_MAP.md` — atribuição: alheio; estado git: ` M`
- `docs/Entregas Aceitas/Entregas - P-0739.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/INDEX.md` — atribuição: alheio; estado git: ` M`
- `docs/RDO/P-0739-BKL-T10-corpus-do-instrumento-e-a-migracao-do-diario-ate-check-verde.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0739-BKL-T10a-drain-o-inbox-de-planos-sai-do-contexto.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0739-BKL-T10b-o-bloco-gerado-da-2-3-e-projetado-inteiro-e-dentro-do-corpus.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0739-BKL-T11-o-hook-o-ponto-de-carga-e-as-skills-que-invocam-o-instrument.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0739-BKL-T11a-o-hook-fala-no-ponto-de-carga-real-stdin-em-utf-8-explicito.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0739-BKL-T9a-rodada-de-transcricao-os-tres-modulos-bkl-t10-bkl-t12.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0739-BKL-T10.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0739-BKL-T10a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0739-BKL-T10b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0739-BKL-T11.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0739-BKL-T11a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0739-BKL-T12.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0739-BKL-T9a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0739-BKL-T12.md` — atribuição: alheio; estado git: `??`
- `docs/consultant-spec.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0735-residencia-e-ponto-de-carga.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0737-loop-autonomo.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0738-contexto-esgotado.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0739-backlog-instrumento.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0741-modelo-conceitual.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0742-loop-fora-do-llm.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_INBOX.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/_INBOX_HISTORICO.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/_VIABILIDADE-agente-leitor.md` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/corpus/docs/plans/P-0777-gama.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/corpus/docs/plans/P-0900-legado.md` — atribuição: alheio; estado git: `??`
- `tests/test_backlog.py` — atribuição: da entrega; estado git: ` M`
- `tests/test_rdo.py` — atribuição: alheio; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `eb93490c23e2964d1cd865a683a7d9969809c0a0`
- Arquivos-alvo declarados: `tests/test_backlog.py`
- Arquivos tocados: `.claude/projecoes.json`, `.claude/skills/entrega-de-encerramento/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/backlog.py`, `.claude/tools/backlog_hook.py`, `.claude/tools/rdo.py`, `CHANGELOG.md`, `GOVERNANCA.md`, `README.md`, `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/DOC_MAP.md`, `docs/Entregas Aceitas/Entregas - P-0739.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0739-BKL-T10-corpus-do-instrumento-e-a-migracao-do-diario-ate-check-verde.md`, `docs/RDO/P-0739-BKL-T10a-drain-o-inbox-de-planos-sai-do-contexto.md`, `docs/RDO/P-0739-BKL-T10b-o-bloco-gerado-da-2-3-e-projetado-inteiro-e-dentro-do-corpus.md`, `docs/RDO/P-0739-BKL-T11-o-hook-o-ponto-de-carga-e-as-skills-que-invocam-o-instrument.md`, `docs/RDO/P-0739-BKL-T11a-o-hook-fala-no-ponto-de-carga-real-stdin-em-utf-8-explicito.md`, `docs/RDO/P-0739-BKL-T9a-rodada-de-transcricao-os-tres-modulos-bkl-t10-bkl-t12.md`, `docs/RDO/evidencia/P-0739-BKL-T10.md`, `docs/RDO/evidencia/P-0739-BKL-T10a.md`, `docs/RDO/evidencia/P-0739-BKL-T10b.md`, `docs/RDO/evidencia/P-0739-BKL-T11.md`, `docs/RDO/evidencia/P-0739-BKL-T11a.md`, `docs/RDO/evidencia/P-0739-BKL-T12.md`, `docs/RDO/evidencia/P-0739-BKL-T9a.md`, `docs/RDO/laudos/P-0739-BKL-T12.md`, `docs/consultant-spec.md`, `docs/plans/P-0735-residencia-e-ponto-de-carga.md`, `docs/plans/P-0737-loop-autonomo.md`, `docs/plans/P-0738-contexto-esgotado.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0742-loop-fora-do-llm.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VIABILIDADE-agente-leitor.md`, `docs/telemetria.tsv`, `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0777-gama.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0900-legado.md`, `tests/test_backlog.py`, `tests/test_rdo.py`, `tests/test_review_evidence.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/tools/backlog.py` → `TK-59a`, `.claude/tools/rdo.py` → `TK-62a`, `README.md` → `TK-51a`, `docs/CUSTO_DO_PICKUP.md` → `TK-58a`, `tests/test_rdo.py` → `TK-62a`, `tests/test_review_evidence.py` → `TK-62a`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0739-BKL-T10-corpus-do-instrumento-e-a-migracao-do-diario-ate-check-verde.md`, `docs/RDO/P-0739-BKL-T10a-drain-o-inbox-de-planos-sai-do-contexto.md`, `docs/RDO/P-0739-BKL-T10b-o-bloco-gerado-da-2-3-e-projetado-inteiro-e-dentro-do-corpus.md`, `docs/RDO/P-0739-BKL-T11-o-hook-o-ponto-de-carga-e-as-skills-que-invocam-o-instrument.md`, `docs/RDO/P-0739-BKL-T11a-o-hook-fala-no-ponto-de-carga-real-stdin-em-utf-8-explicito.md`, `docs/RDO/P-0739-BKL-T9a-rodada-de-transcricao-os-tres-modulos-bkl-t10-bkl-t12.md`, `docs/RDO/evidencia/P-0739-BKL-T10.md`, `docs/RDO/evidencia/P-0739-BKL-T10a.md`, `docs/RDO/evidencia/P-0739-BKL-T10b.md`, `docs/RDO/evidencia/P-0739-BKL-T11.md`, `docs/RDO/evidencia/P-0739-BKL-T11a.md`, `docs/RDO/evidencia/P-0739-BKL-T12.md`, `docs/RDO/evidencia/P-0739-BKL-T9a.md`, `docs/RDO/laudos/P-0739-BKL-T12.md`, `docs/plans/P-0735-residencia-e-ponto-de-carga.md`, `docs/plans/P-0737-loop-autonomo.md`, `docs/plans/P-0738-contexto-esgotado.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0742-loop-fora-do-llm.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VIABILIDADE-agente-leitor.md`, `docs/telemetria.tsv`
- Fato: 13 arquivo(s) fora dos alvos e sem atribuição: `.claude/projecoes.json`, `.claude/skills/entrega-de-encerramento/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/backlog_hook.py`, `CHANGELOG.md`, `GOVERNANCA.md`, `docs/DOC_MAP.md`, `docs/Entregas Aceitas/Entregas - P-0739.md`, `docs/consultant-spec.md`, `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0777-gama.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0900-legado.md`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `tests/test_backlog.py`
```
diff --git a/tests/test_backlog.py b/tests/test_backlog.py
index cdd5555..8f509ee 100644
--- a/tests/test_backlog.py
+++ b/tests/test_backlog.py
@@ -13,18 +13,24 @@ from __future__ import annotations
 
 import hashlib
 import importlib.util
+import io
+import json
+import os
 import shutil
+import subprocess
 import sys
 from pathlib import Path
 
 _ROOT = Path(__file__).resolve().parents[1]
 _BACKLOG_PATH = _ROOT / ".claude" / "tools" / "backlog.py"
+_HOOK_PATH = _ROOT / ".claude" / "tools" / "backlog_hook.py"
 _FIXTURES = Path(__file__).resolve().parent / "fixtures" / "backlog"
 _FIXTURE_VERDE = _FIXTURES / "verde"
 _FIXTURE_VERMELHO = _FIXTURES / "vermelho"
 _FIXTURE_NEXT_TK90 = _FIXTURES / "next_tk90"
 _FIXTURE_NEXT_TK90_SEM_INDICE = _FIXTURES / "next_tk90_sem_indice"
 _FIXTURE_INBOX_PLANOS = _FIXTURES / "inbox_planos" / "_INBOX.md"
+_FIXTURE_CORPUS = _FIXTURES / "corpus"
 
 
 def _load_backlog():
@@ -42,6 +48,13 @@ def _copiar_fixture(origem: Path, destino: Path) -> Path:
     return destino
 
 
+def _load_hook():
+    spec = importlib.util.spec_from_file_location("backlog_hook", _HOOK_PATH)
+    module = importlib.util.module_from_spec(spec)
+    spec.loader.exec_module(module)
+    return module
+
+
 def _hashes(repo: Path) -> dict[str, str]:
     return {
         str(caminho.relative_to(repo)): hashlib.sha256(caminho.read_bytes()).hexdigest()
@@ -50,6 +63,24 @@ def _hashes(repo: Path) -> dict[str, str]:
     }
 
 
+def _mudar_linha_unica(repo: Path, relpath: str, velha: str, nova: str) -> None:
+    """Troca uma linha por outra numa cópia de fixture em `tmp_path` — nunca na fixture do
+    repositório. `velha` tem de ser única no arquivo (mesmo padrão de `_indice_com_sufixo`)."""
+    caminho = repo / relpath
+    texto = caminho.read_text(encoding="utf-8")
+    assert texto.count(velha) == 1, f"linha não é única (ou ausente) em {relpath}: {velha!r}"
+    caminho.write_text(texto.replace(velha, nova, 1), encoding="utf-8")
+
+
+def _inserir_linhas_indice(repo: Path, linhas_novas: list[str]) -> None:
+    """Acrescenta linhas à tabela do índice da fixture `corpus`, logo depois da linha do
+    `TK-1` — sempre sobre a cópia em `tmp_path`, nunca na fixture do repositório."""
+    ancora = "| TK-1 | Tiquete base | ready | docs/DIARIO_DE_OBRAS.md#tk-1 |\n"
+    _mudar_linha_unica(
+        repo, "docs/DIARIO_DE_OBRAS.md", ancora.rstrip("\n"), ancora.rstrip("\n") + "\n" + "\n".join(linhas_novas)
+    )
+
+
 def _inserir_bloco_gerado(repo: Path) -> None:
     """Prepara a cópia da fixture para os TF de escrita da `BKL-T4`: a fixture
     `next_tk90` não carrega os marcadores `<!-- fila:gerada -->`/`<!-- /fila:gerada -->`
@@ -145,6 +176,124 @@ def test_tf_check_verde_sem_violacoes(tmp_path):
     assert violacoes == []
 
 
+# --------------------------------------------------------------------------- #
+# BKL-T10 (`docs/plans/P-0739-backlog-instrumento.md` `### BKL-T10`) — TF do corpus
+# (`DB-43`) e da célula de item terminal (`DB-46`). Fixture `corpus`: `P-0900` (índice
+# `ready`, cabeçalho sem `Status`/`Prefixo`), `P-0777-XYZ` (índice `done`, sufixo
+# mnemônico, cabeçalho `ready` — diverge de propósito), `TK-1` (limpo) e uma tabela
+# markdown ilustrativa fora de `## Índice`, dentro da prosa do `TK-1`.
+# --------------------------------------------------------------------------- #
+
+
+def test_tf_plano_terminal_no_indice_sai_do_corpus_do_check(tmp_path):
+    backlog = _load_backlog()
+
+    repo_vivo = _copiar_fixture(_FIXTURE_CORPUS, tmp_path / "repo_vivo")
+    violacoes_vivo = backlog.check(backlog.carregar(repo_vivo))
+    assert any(v.arquivo == "docs/plans/P-0900-legado.md" for v in violacoes_vivo)
+
+    repo_terminal = _copiar_fixture(_FIXTURE_CORPUS, tmp_path / "repo_terminal")
+    _mudar_linha_unica(
+        repo_terminal,
+        "docs/DIARIO_DE_OBRAS.md",
+        "| P-0900 | Plano legado | ready | docs/plans/P-0900-legado.md |",
+        "| P-0900 | Plano legado | done | docs/plans/P-0900-legado.md |",

```
[truncado em 4000 caracteres]

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 1
  ```
  kit_check: check-drift FALHOU (2 problema(s)):
    - README.md diverge do regenerado (1 linha(s) diferente(s)):
    -   [regenerado] | `entrega-de-encerramento` | Produz o documento de encerramento de um plano Pantonic* - o modelo "as-is" que mapeia cada tarefa ao contexto que a motivou, ao artefato concreto que ela criou, a um exemplo real de funcionamento e ao que ela protege, mais o estado honesto do que ficou aberto. � o artefato pelo qual o dono valida o plano. Usar ao fechar qualquer plano, antes de pedir o veredito. |
  ```
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): não conforme
- Veredito mecânico (`testes`): conforme
