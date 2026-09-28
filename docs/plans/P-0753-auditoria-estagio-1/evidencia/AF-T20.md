# Evidência de revisão — P-0753 AF-T20

## Diff (`git diff --stat`)
```
.claude/tools/backlog.py                           |   2 +-
 .claude/tools/uow.py                               | 408 ---------------------
 docs/DIARIO_DE_OBRAS.md                            |   4 +-
 docs/plans/P-0753-auditoria-estagio-1/estado.tsv   |   2 +-
 .../evidencia/P-0753-AF-T20-medida.json            |  36 ++
 docs/telemetria.tsv                                |   1 +
 6 files changed, 41 insertions(+), 412 deletions(-)
```

## Arquivos tocados
- `.claude/tools/backlog.py` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/uow.py` — atribuição: da entrega; estado git: ` D`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T20-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `4157cfccac5120e4a18bf730bb05e5546e3f0261`
- Arquivos-alvo declarados: `.claude/tools/uow.py`, `.claude/tools/backlog.py`
- Arquivos tocados: `.claude/tools/backlog.py`, `.claude/tools/uow.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T20-medida.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T20-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/uow.py`
```
diff --git a/.claude/tools/uow.py b/.claude/tools/uow.py
deleted file mode 100644
index e4cf575..0000000
--- a/.claude/tools/uow.py
+++ /dev/null
@@ -1,408 +0,0 @@
-"""Unidade de trabalho (UoW) para autoria de artefato canônico.
-
-Regra 9 da doutrina global: artefato canônico do harness não se edita em
-incrementos in-place. A tarefa abre uma UoW, edita **cópias** fora da árvore do
-repositório, apresenta o diff para revisão e materializa tudo num ato só.
-
-Motivo, nos três custos que a edição in-place cobra:
-
-1. Cada `Edit` em caminho protegido abre uma janela de aceite. N edições, N
-   interrupções.
-2. Ninguém vê a mudança inteira antes de ela valer — a revisão é fragmentada em
-   pedaços que chegam um a um.
-3. Tarefa interrompida deixa artefato meio-editado, e o estado parcial vira
-   dívida de governança em outro lugar (o diário passa a carregar a receita do
-   que falta).
-
-O (3) é o caro. Cópia fora da árvore transforma "tarefa morta não deixa
-resíduo" de acidente em propriedade: o original só é tocado no `close`.
-
-Escopo — o que entra na UoW: tudo que a tarefa editaria por `Edit`/`Write`.
-O que não entra: ledger escrito por ferramenta via Bash (`rdo.py`,
-`telemetria.py`) e `.claude/settings.json` (ponto de carga, do `materializar.py`,
-`GOVERNANCA.md` §3.1).
-
-O portão é conversacional, não modal: `close` **recusa** rodar antes de um
-`diff` ter sido emitido para a UoW corrente (marca `diff_em` no manifesto).
-Como a cópia de volta roda por Bash, ela não abre janela nenhuma — a revisão do
-diff é o único portão que resta, e por isso é obrigatória.
-
-Residência da UoW: fora do repositório, em
-``<tempdir>/claude/uow/<slug do repo>/``. Fora da árvore não suja `git status`,
-e o slug derivado do caminho do repo (não da sessão) mantém a UoW viva se a
-sessão cair no meio da tarefa.
-
-`close` é **sem argumento** de propósito: os alvos vêm do manifesto, nunca da
-linha de comando. Comando com argumento variável não é aprovável de uma vez —
-é o que produziu as ~190 entradas de uma-vez-só na allow-list do dono.
-
-Superfície testável: as funções `abrir`/`estado`/`diferenca`/`fechar` recebem
-`raiz_uow`/`repo` já resolvidos e nunca leem `sys.argv` — mesmo desenho de
-`materializar.py` (`--kit-root`/`--home`) e `dead_code.py` (`--root`), para que
-o teste exercite tudo contra `tmp_path` sem jamais escrever no repositório real.
-
-CLI: ``python .claude/tools/uow.py {open,status,diff,close,abort}
-[--arquivos ...] [--tarefa ID] [--repo <caminho>] [--raiz-uow <caminho>]``
-"""
-from __future__ import annotations
-
-import argparse
-import difflib
-import hashlib
-import json
-import shutil
-import sys
-import tempfile
-from datetime import datetime, timezone
-from pathlib import Path
-
-_MANIFESTO_BASENAME = "manifesto.json"
-_COPIAS_DIRNAME = "copias"
-
-
-class UoWInvalida(Exception):
-    """Manifesto ausente, malformado, ou operação fora da ordem do ciclo."""
-
-
-class DriftDoOriginal(Exception):
-    """O original mudou depois do `open`: copiar de volta destruiria a mudança."""
-
-
-# --------------------------------------------------------------------------- #
-# Resolução de topologia
-# --------------------------------------------------------------------------- #
-
-
-def resolve_repo(repo_arg: str | None) -> Path:
-    if repo_arg:
-        return Path(repo_arg).resolve()
-    return Path(__file__).resolve().parent.parent.parent
-
-
-def _slug_do_repo(repo: Path) -> str:
-    """Identidade estável da UoW: deriva do caminho do repo, não da sessão.
-
-    Sessão que cai no meio da tarefa não deve levar a UoW junto; o caminho do
-    repo é o que permanece.
-    """
-    bruto = str(repo).replace("\\", "/").strip("/")
-    return "".join(c if c.isalnum() else "-" for c in bruto).strip("-").lower()
-
-
-def resolve_raiz_uow(raiz_arg: str | None, repo: Path) -> Path:
-    if raiz_arg:
-        return Path(raiz_arg).resolve()
-    return Path(tempfile.gettempdir()) / "claude" / "uow" / _slug_do_repo(repo)
-
-
```
[truncado em 4000 caracteres]

### `.claude/tools/backlog.py`
```
diff --git a/.claude/tools/backlog.py b/.claude/tools/backlog.py
index 8933be2..1647a51 100644
--- a/.claude/tools/backlog.py
+++ b/.claude/tools/backlog.py
@@ -35,7 +35,7 @@ por máquina" — replicada aqui igual, `DB-17`/`DB-18`):
 `carregar` só lê `docs/DIARIO_DE_OBRAS.md` e `docs/plans/P-*.md` — nunca abre `*_HISTORICO.md`
 nem `_INBOX.md` (fora de escopo desta tarefa; a migração e o `drain` são tarefas futuras do
 plano). Superfície testável: `carregar`/`check`/`show` recebem `repo`/`modelo` já resolvidos e
-nunca leem `sys.argv` — mesmo desenho de `uow.py`/`telemetria.py` (`DB-1`).
+nunca leem `sys.argv` — mesmo desenho de `telemetria.py` (`DB-1`).
 
 CLI: ``python .claude/tools/backlog.py check [--repo <caminho>]`` (exit 0 sem violação, 1 com
 violação) e ``python .claude/tools/backlog.py show <ID> [--repo <caminho>]``. A CLI só embrulha

```

## Medida do executor
- Arquivo: docs\plans\P-0753-auditoria-estagio-1\evidencia\P-0753-AF-T20-medida.json; mundo: depois; gerado em: 2026-09-27T17:06:21+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;print(Path('.claude/tools/uow.py').exists())"` | 0 | true |
| 2 | `python -c "from pathlib import Path;print(Path('.claude/tools/backlog.py').read_text(encoding='utf-8').count('uow.py'))"` | 0 | true |
| 3 | `python -m pytest -q` | 0 | true |
| 4 | `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
