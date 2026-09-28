# Evidência de revisão — P-0753 AF-T10

## Diff (`git diff --stat`)
```
.claude/skills/scrum-master/SKILL.md               |  11 ++
 .claude/tools/backlog.py                           | 125 +++++++++++++++++++++
 docs/ACIONAMENTOS_CONSULTOR.tsv                    |   1 +
 docs/DIARIO_DE_OBRAS.md                            |   2 +-
 docs/plans/P-0753-auditoria-estagio-1/cenario.md   |  22 +++-
 docs/plans/P-0753-auditoria-estagio-1/estado.tsv   |   2 +-
 .../evidencia/P-0753-AF-T10-medida.json            |  43 +++++++
 docs/plans/P-0753-auditoria-estagio-1/plano.md     |  35 ++++--
 docs/telemetria.tsv                                |   3 +
 tests/test_backlog.py                              | 118 +++++++++++++++++++
 10 files changed, 349 insertions(+), 13 deletions(-)
```

## Arquivos tocados
- `.claude/skills/scrum-master/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/backlog.py` — atribuição: da entrega; estado git: ` M`
- `docs/ACIONAMENTOS_CONSULTOR.tsv` — atribuição: alheio; estado git: `??`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/cenario.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T10-medida.json` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/plano.md` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_backlog.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `9f6bf68ea11876bdf231f7eee58b6bfa68560a6d`
- Arquivos-alvo declarados: `.claude/tools/backlog.py`, `tests/test_backlog.py`, `.claude/skills/scrum-master/SKILL.md`
- Arquivos tocados: `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/backlog.py`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/cenario.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T10-medida.json`, `docs/plans/P-0753-auditoria-estagio-1/plano.md`, `docs/telemetria.tsv`, `tests/test_backlog.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/cenario.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T10-medida.json`, `docs/plans/P-0753-auditoria-estagio-1/plano.md`, `docs/telemetria.tsv`
- Fato: 1 arquivo(s) fora dos alvos e sem atribuição: `docs/ACIONAMENTOS_CONSULTOR.tsv`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/backlog.py`
```
diff --git a/.claude/tools/backlog.py b/.claude/tools/backlog.py
index d4f4699..3e20b07 100644
--- a/.claude/tools/backlog.py
+++ b/.claude/tools/backlog.py
@@ -46,8 +46,10 @@ from __future__ import annotations
 import argparse
 import datetime
 import importlib.util
+import json
 import os
 import re
+import subprocess
 import sys
 from dataclasses import dataclass, field
 from pathlib import Path
@@ -2061,6 +2063,119 @@ def transacionar_drain(
     return ResultadoStatus(0, aviso, arquivos)
 
 
+def _ultima_linha_stderr(texto: str) -> str:
+    linhas = texto.splitlines()
+    return linhas[-1] if linhas else ""
+
+
+def despachar(repo: Path, id_: str) -> ResultadoStatus:
+    """AF-T10 (`DAF-41`) — um comando roda as conferências do despacho do passo 3/4 de
+    `.claude/skills/scrum-master/SKILL.md` (tarefa, `modelo.py check`, `card_check.py`,
+    `pytest --co`, captura do `<ref>`, materialização em `in-progress`), nesta ordem, recusando
+    pela primeira que falhar e sem escrever nada até a última checagem passar. `modelo.py`,
+    `card_check.py` e `review_evidence.py` rodam como subprocessos do irmão em
+    `Path(__file__).parent` (`sys.executable`), nunca por `import`."""
+
+    def _recusar(gate: str, razao: str) -> ResultadoStatus:
+        print(f"despachar: recusado — {gate}: {razao}", file=sys.stderr)
+        return ResultadoStatus(1, razao)
+
+    modelo = carregar(repo)
+    alvo = _localizar(modelo, id_)
+    if not isinstance(alvo, Item) or alvo.tipo != "tarefa":
+        return _recusar("tarefa", f"{id_} não é tarefa de plano")
+    if alvo.status != "ready":
+        return _recusar("tarefa", f"{id_} está {alvo.status}, não ready")
+
+    pai, tipo_pai = _pai_do_alvo(modelo, alvo)
+    irmao = Path(__file__).resolve().parent
+    # `--plano` absoluto (`repo / pai.arquivo`): `card_check.verificar_tarefa` usa `Path(plano)`
+    # direto, sem juntar com `--root` — relativo dependeria do cwd do subprocesso, que este
+    # comando não fixa (`modelo.py` aceita os dois por `_resolver_plano`, mas o absoluto serve
+    # aos dois irmãos sem depender de onde o processo-pai foi invocado).
+    plano_abs = str(repo / pai.arquivo)
+
+    resultado_modelo = subprocess.run(
+        [sys.executable, str(irmao / "modelo.py"), "check", "--plano", plano_abs, "--root", str(repo)],
+        capture_output=True,
+        text=True,
+    )
+    if resultado_modelo.returncode not in (0, 2):
+        return _recusar("modelo", _ultima_linha_stderr(resultado_modelo.stderr))
+
+    resultado_cc = subprocess.run(
+        [
+            sys.executable,
+            str(irmao / "card_check.py"),
+            "--plano",
+            plano_abs,
+            "--tarefa",
+            id_,
+            "--root",
+            str(repo),
+        ],
+        capture_output=True,
+        text=True,
+    )
+    if resultado_cc.returncode != 0:
+        return _recusar("card_check", _ultima_linha_stderr(resultado_cc.stderr))
+
+    resultado_pytest = subprocess.run(
+        [sys.executable, "-m", "pytest", "--co", "-q"],
+        cwd=str(repo),
+        capture_output=True,
+        text=True,
+    )
+    if resultado_pytest.returncode not in (0, 5):
+        return _recusar("pytest --co", f"exit {resultado_pytest.returncode}")
+
+    estado_path = repo / ".claude" / "estado" / "tarefa-corrente.json"
+    ref: str | None = None
+    if estado_path.is_file():
+        try:
+            dados_existentes = json.loads(estado_path.read_text(encoding="utf-8"))
+        except (json.JSONDecodeError, OSError):
+            dados_existentes = {}
+        if dados_existentes.get("tarefa") == id_ and dados_existentes.get("ref"):
+            ref = dados_existentes["ref"]
+    if ref is None:
+        resultado_ref = subprocess.run(
+            [sys.executable, str(irmao / "review_evidence.py"), "--capturar-ref", "--root", str(repo)],
+            capture_output=True,
+            text=True,
+        )
+        if resultado_ref.returncode != 0:
+    
```
[truncado em 4000 caracteres]

### `tests/test_backlog.py`
```
diff --git a/tests/test_backlog.py b/tests/test_backlog.py
index 9a036a5..3644654 100644
--- a/tests/test_backlog.py
+++ b/tests/test_backlog.py
@@ -2940,3 +2940,121 @@ def test_piso_c11_tsv_entrada_orfa_e_linha_malformada(tmp_path, capsys):
     saida = capsys.readouterr().out
     assert any("piso_c11 nomeia entrada órfã" in l and "9.9" in l for l in saida.splitlines())
     assert "C-17 docs/PISO_C11.tsv:3 — linha fora do esquema" in saida
+
+
+# --------------------------------------------------------------------------- #
+# AF-T10 (`DAF-41`) — `despachar`: um comando roda as conferências do despacho e
+# recusa pela primeira que falhar. Cópia isolada da fixture `pasta` em `tmp_path`,
+# nunca sobre o repositório real.
+# --------------------------------------------------------------------------- #
+
+_GAM_PLANO_DESPACHAR_TEXTO = (
+    "# P-0 — Plano gama\n"
+    "\n"
+    "**Prefixo das tarefas no diário:** `GAM-T<n>`\n"
+    "\n"
+    "### GAM-T1 — Primeira tarefa [Sonnet · classe implementacao]\n"
+    "- **Objetivo:** fixture.\n"
+    "- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.\n"
+    "- **Verificação:**\n"
+    "  1. `python -c \"print('a')\"` → `b` — antes `a`, depois `b`\n"
+    "- **Pronto quando:** fixture existe.\n"
+    "\n"
+    "### GAM-T2 — Segunda tarefa [Sonnet · classe implementacao]\n"
+    "- **Objetivo:** fixture.\n"
+    "- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.\n"
+    "- **Verificação:**\n"
+    "  1. `python -c \"print('a')\"` → `b` — antes `z`, depois `b`\n"
+    "- **Pronto quando:** fixture existe.\n"
+)
+
+
+def _run_git_despachar(args: list[str], cwd: Path) -> None:
+    resultado = subprocess.run(["git", *args], cwd=str(cwd), capture_output=True, text=True)
+    assert resultado.returncode == 0, f"git {args}: {resultado.stderr}"
+
+
+def _montar_repo_despachar(tmp_path: Path, nome: str = "repo") -> Path:
+    """`DAF-41` — cópia em quatro tempos, ensaiada pelo consultor no redespacho: (a) fixture
+    `pasta`; (b) `rdo.py`/`caminhos.py` reais em `.claude/tools/` da cópia (`card_check` carrega
+    `rdo.py` de `<root>/.claude/tools/`, e `rdo.py` carrega `caminhos.py` ao lado — sem eles o
+    gate `card_check` recusa com `rdo.py: módulo não encontrado`); (c) `docs/plans/P-0-gama/plano.md`
+    sobrescrito com os campos que `rdo.extrair_dossie` exige (`Objetivo`, `Verificação`, `Pronto
+    quando` e exatamente um entre `Arquivos-alvo`/`Entregável`) — `GAM-T1` o `card_check` aceita,
+    `GAM-T2` recusa (`antes` `z` contra a saída real `a`); (d) `git init` + commit inicial com
+    tudo, para `review_evidence.py --capturar-ref` ter uma árvore para gravar. A fixture do
+    repositório não muda — só a cópia."""
+    repo = _copiar_fixture(_FIXTURE_PASTA, tmp_path / nome)
+    ferramentas = repo / ".claude" / "tools"
+    ferramentas.mkdir(parents=True, exist_ok=True)
+    shutil.copy2(_ROOT / ".claude" / "tools" / "rdo.py", ferramentas / "rdo.py")
+    shutil.copy2(_ROOT / ".claude" / "tools" / "caminhos.py", ferramentas / "caminhos.py")
+    (repo / "docs" / "plans" / "P-0-gama" / "plano.md").write_text(
+        _GAM_PLANO_DESPACHAR_TEXTO, encoding="utf-8"
+    )
+    _run_git_despachar(["init"], repo)
+    _run_git_despachar(["config", "user.email", "teste@example.com"], repo)
+    _run_git_despachar(["config", "user.name", "Teste"], repo)
+    _run_git_despachar(["add", "-A"], repo)
+    _run_git_despachar(["commit", "-m", "baseline"], repo)
+    return repo
+
+
+def test_tf_despachar_grava_estado_e_imprime_ref(tmp_path, capsys):
+    """TF da AF-T10: `despachar GAM-T1` roda as conferências do despacho, materializa
+    `in-progress` em `estado.tsv` e imprime o `<ref>` capturado, gravado em
+    `tarefa-corrente.json`."""
+    backlog = _load_backlog()
+    repo = _montar_repo_despachar(tmp_path)
+
+    assert backlog.main(["despachar", "GAM-T1", "--repo", str(repo)]) == 0
+
+    saida = capsys.readouterr().out
+    linha_ref = nex
```
[truncado em 4000 caracteres]

### `.claude/skills/scrum-master/SKILL.md`
```
diff --git a/.claude/skills/scrum-master/SKILL.md b/.claude/skills/scrum-master/SKILL.md
index b92f951..4bf9d88 100644
--- a/.claude/skills/scrum-master/SKILL.md
+++ b/.claude/skills/scrum-master/SKILL.md
@@ -73,6 +73,14 @@ Dez passos, nesta ordem.
 
   Aprovados os quatro, e **antes** de delegar, materializar `ready` → `in-progress` no kanban
   (`DP-G` item 1, consequência 3) — ato exclusivo do `scrum-master`.
+
+  **Por comando** (`R-15`): `python .claude/tools/backlog.py despachar <ID>` roda, nesta ordem, o
+  terceiro gate, o quarto e a coleta da suíte (`python -m pytest --co -q`), materializa
+  `in-progress`, grava `.claude/estado/tarefa-corrente.json` com o `<ref>` e imprime o card
+  inteiro, o bloco `HANDOVER` e a linha `ref=<sha>`. Recusa pelo primeiro gate que falhar, sem
+  escrever nada: exit `1` **não delega**, e a linha de recusa vai à razão de `B3`. `G-PLANREADY` e o
+  Gate de delegação continuam com quem conduz, antes do verbo; card de tíquete segue pelos passos
+  à mão.
 - **Saída:** tarefa materializada em `in-progress` e liberada para despacho, ou parada com o que
   falta fechar.
 
@@ -91,6 +99,9 @@ Dez passos, nesta ordem.
   desde o despacho. No redespacho da mesma tarefa (retomada depois de `blocked`, ou retentativa),
   o `<ref>` não se recaptura: vale o do primeiro despacho, para a evidência cobrir as duas execuções.
 
+  Despachada pelo verbo `despachar` do passo 3, a tarefa já tem o arquivo gravado e o `<ref>` na
+  linha `ref=<sha>` da saída: este passo só invoca o executor.
+
   Invocar `pantonic-executor` com `model` **igual ao do cabeçalho** (vence o `model:` do agente),
   com o dossiê da tarefa e a instrução de devolver **uma única linha**, domínio fechado (`DP-G`
   item 2):

```

## Medida do executor
- Arquivo: docs\plans\P-0753-auditoria-estagio-1\evidencia\P-0753-AF-T10-medida.json; mundo: depois; gerado em: 2026-09-27T14:49:20+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python .claude/tools/backlog.py despachar --help` | 0 | true |
| 2 | `python -m pytest tests/test_backlog.py -q -k "despachar"` | 0 | true |
| 3 | `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print(t.count('backlog.py despachar'),t.count('Despachada pelo verbo'))"` | 0 | true |
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
