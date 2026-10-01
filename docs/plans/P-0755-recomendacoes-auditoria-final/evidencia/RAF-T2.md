# Evidência de revisão — P-0755 RAF-T2

## Diff (`git diff --stat`)
```
.claude/tools/custo_sessao.py                      | 249 +++++++++++++++++++++
 docs/DIARIO_DE_OBRAS.md                            |   4 +-
 .../estado.tsv                                     |   2 +-
 .../evidencia/P-0755-RAF-T2-medida.json            |  22 ++
 docs/telemetria.tsv                                |   1 +
 tests/test_custo_sessao.py                         | 199 ++++++++++++++++
 6 files changed, 474 insertions(+), 3 deletions(-)
```

## Arquivos tocados
- `.claude/tools/custo_sessao.py` — atribuição: da entrega; estado git: `??`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T2-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_custo_sessao.py` — atribuição: da entrega; estado git: `??`

## Escopo
- Recorte: desde `9eb2af006f42b61cb2714664ceb813a2325fe526`
- Arquivos-alvo declarados: `.claude/tools/custo_sessao.py`, `tests/test_custo_sessao.py`
- Arquivos tocados: `.claude/tools/custo_sessao.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T2-medida.json`, `docs/telemetria.tsv`, `tests/test_custo_sessao.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T2-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/custo_sessao.py`
```
(arquivo novo — ausente em `9eb2af006f42b61cb2714664ceb813a2325fe526`)
--- .claude/tools/custo_sessao.py@9eb2af006f42b61cb2714664ceb813a2325fe526
+++ .claude/tools/custo_sessao.py
@@ -0,0 +1,249 @@
+"""RAF-T2 (`docs/plans/P-0755-recomendacoes-auditoria-final/plano.md` `### RAF-T2`) — o medidor de
+custo da sessão vira comando do kit: lê uma conversa gravada (transcript, uma linha JSON por
+evento) e reparte o contexto reenviado por turno, por passo do loop e por tarefa despachada.
+
+Fundamento: `DRF-6`; `F-6` (285,6k por turno no loop real), `F-13` (os rascunhos de
+`docs/audits/sonda-2026-09-28/{medir,passos}.py` quebram e fixam `AUF-T`). Os rascunhos são o
+ponto de partida lido e ficam intocados — este módulo não importa deles nem os reescreve.
+
+Dois subcomandos:
+
+``python .claude/tools/custo_sessao.py medir <transcript> <saida>`` — grava em `<saida>` (TSV) uma
+linha por turno `assistant` com `usage` não vazio: `timestamp`, `message.id`, o contexto reenviado
+(`input_tokens + cache_read_input_tokens + cache_creation_input_tokens`, campo ausente conta 0),
+`output_tokens` e as ferramentas do turno unidas por ` | `.
+
+``python .claude/tools/custo_sessao.py passos <tsv> <regex_inicio> <regex_fim>`` — agrupa o TSV por
+`message.id`, recorta a janela entre a primeira mensagem cujas ferramentas casam `regex_inicio` e
+a última que casa `regex_fim`, e imprime o total da janela, o total por passo do loop
+(`classificar_passo`) e o total por tarefa despachada (regex `despachar
+([A-Z]+-T\\d+[a-z]?|TK-\\d+)`, de qualquer plano ou tíquete — não só `AUF-T`)."""
+from __future__ import annotations
+
+import argparse
+import json
+import re
+import sys
+from pathlib import Path
+
+_REGEX_BACKLOG_STATUS_REVIEW = re.compile(r"backlog\.py status \S+ review")
+_REGEX_GREP_MECANICO = re.compile(r"grep -n|--co -q|wc -l")
+_REGEX_TAREFA = re.compile(r"despachar ([A-Z]+-T\d+[a-z]?|TK-\d+)")
+
+
+def _forcar_utf8(stream) -> None:
+    """Console cp1252 do Windows estoura `UnicodeEncodeError` ao imprimir certos caracteres —
+    duplicado do mesmo utilitário de `card_check.py`/`review_evidence.py`/`crenca_hook.py`
+    (`DM-11`, sem import cruzado entre módulos)."""
+    reconfigure = getattr(stream, "reconfigure", None)
+    if reconfigure is not None:
+        reconfigure(encoding="utf-8", errors="replace")
+
+
+def _ferramentas_do_turno(blocos: list) -> str:
+    ferramentas: list[str] = []
+    for bloco in blocos or []:
+        tipo = bloco.get("type")
+        if tipo == "tool_use":
+            nome = bloco.get("name")
+            entrada = bloco.get("input") or {}
+            if nome == "Agent":
+                subagent_type = entrada.get("subagent_type", "")
+                descricao = entrada.get("description", "")
+                ferramentas.append(f"Agent:{subagent_type}:{descricao}")
+            elif nome in ("Bash", "PowerShell"):
+                comando = re.sub(r"\s+", " ", str(entrada.get("command", "")))
+                ferramentas.append("Bash:" + comando[:220])
+            else:
+                valor = entrada.get("file_path", entrada.get("pattern", ""))
+                ferramentas.append(f"{nome}:" + str(valor)[:120])
+        elif tipo == "text" and str(bloco.get("text", "")).strip():
+            ferramentas.append("TEXT")
+    return " | ".join(ferramentas)
+
+
+def medir(transcript: Path, saida: Path) -> int:
+    """Grava em `saida` uma linha do TSV por turno `assistant` com `usage` não vazio; devolve o
+    número de linhas gravadas."""
+    linhas: list[tuple[str, str, int, int, str]] = []
+    for linha_bruta in transcript.read_text(encoding="utf-8").splitlines():
+        try:
+            evento = json.loads(linha_bruta)
+        except (json.JSONDecodeError, ValueError):
+            continue
+        if evento.get("type") != "assistant":
+            continue
+        mensagem = evento.get("message") or {}
+        uso = mensagem.get("usage") or {}
+        if not uso:
+            continue
+    
```
[truncado em 4000 caracteres]

### `tests/test_custo_sessao.py`
```
(arquivo novo — ausente em `9eb2af006f42b61cb2714664ceb813a2325fe526`)
--- tests/test_custo_sessao.py@9eb2af006f42b61cb2714664ceb813a2325fe526
+++ tests/test_custo_sessao.py
@@ -0,0 +1,199 @@
+"""RAF-T2 (`docs/plans/P-0755-recomendacoes-auditoria-final/plano.md` `### RAF-T2`) — TF/TR de
+`.claude/tools/custo_sessao.py`: o medidor de custo da sessão, que lê uma conversa gravada e
+reparte o contexto reenviado por turno, por passo do loop e por tarefa despachada.
+
+`.claude/tools/` não é pacote importável (diretório com ponto no nome) — o módulo é carregado por
+caminho via `importlib.util.spec_from_file_location`, mesmo padrão de `tests/test_ocupacao.py` e
+`tests/test_telemetria.py`.
+
+Todo transcript sintético desta suíte é escrito em `tmp_path`: uma linha `user`, os turnos
+`assistant` do teste e uma linha que não é JSON (prova de que `medir` pula linha ilegível sem
+quebrar)."""
+from __future__ import annotations
+
+import importlib.util
+import json
+from pathlib import Path
+
+_ROOT = Path(__file__).resolve().parents[1]
+_CUSTO_SESSAO_PATH = _ROOT / ".claude" / "tools" / "custo_sessao.py"
+
+
+def _load_custo_sessao():
+    spec = importlib.util.spec_from_file_location("custo_sessao", _CUSTO_SESSAO_PATH)
+    module = importlib.util.module_from_spec(spec)
+    spec.loader.exec_module(module)
+    return module
+
+
+def _linha_user() -> str:
+    return json.dumps({"type": "user", "message": {"content": []}})
+
+
+def _linha_assistant(ts: str, mid: str, usage: dict, content: list) -> str:
+    return json.dumps(
+        {
+            "type": "assistant",
+            "timestamp": ts,
+            "message": {"id": mid, "usage": usage, "content": content},
+        }
+    )
+
+
+def _escreve_transcript(tmp_path: Path, turnos_assistant: list[str]) -> Path:
+    caminho = tmp_path / "transcript.jsonl"
+    linhas = [_linha_user(), *turnos_assistant, "isto não é json {{{"]
+    caminho.write_text("\n".join(linhas) + "\n", encoding="utf-8")
+    return caminho
+
+
+def test_tf_medir_grava_uma_linha_por_turno_com_contexto_reenviado(tmp_path, capsys):
+    """TF: uma linha do TSV por turno `assistant` com `usage` não vazio; o contexto reenviado é a
+    soma dos três campos (a regra concorrente que somasse só `cache_read_input_tokens` daria
+    1000 no primeiro turno, não 1210)."""
+    custo_sessao = _load_custo_sessao()
+    t1 = _linha_assistant(
+        "t1",
+        "m1",
+        {
+            "input_tokens": 10,
+            "cache_read_input_tokens": 1000,
+            "cache_creation_input_tokens": 200,
+            "output_tokens": 30,
+        },
+        [{"type": "tool_use", "name": "Bash", "input": {"command": "python .claude/tools/backlog.py next"}}],
+    )
+    t2 = _linha_assistant(
+        "t2",
+        "m2",
+        {
+            "input_tokens": 5,
+            "cache_read_input_tokens": 2000,
+            "cache_creation_input_tokens": 0,
+            "output_tokens": 40,
+        },
+        [{"type": "text", "text": "algo"}],
+    )
+    transcript = _escreve_transcript(tmp_path, [t1, t2])
+    saida = tmp_path / "medido.tsv"
+
+    codigo = custo_sessao.main(["medir", str(transcript), str(saida)])
+
+    assert codigo == 0
+    assert capsys.readouterr().out.strip() == "2 linhas"
+    linhas = saida.read_text(encoding="utf-8").splitlines()
+    assert linhas == [
+        "t1\tm1\t1210\t30\tBash:python .claude/tools/backlog.py next",
+        "t2\tm2\t2005\t40\tTEXT",
+    ]
+
+
+def test_tf_passos_reparte_por_passo_e_por_tarefa_de_qualquer_plano(tmp_path, capsys):
+    """TF: os turnos se repartem por passo do loop (`classificar_passo`) e por tarefa despachada
+    de QUALQUER plano ou tíquete — inclusive `TK-12`, que o rascunho preso a `AUF-T` não conta."""
+    custo_sessao = _load_custo_sessao()
+    turnos = [
+        _linha_assistant(
+            "t1",
+            "m1",
+            {"input_tokens": 1000, "output_tokens": 0},
+            [{"type": "tool_use", "name": "Bash", "input":
```
[truncado em 4000 caracteres]

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T2-medida.json; mundo: depois; gerado em: 2026-09-29T01:34:52+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_custo_sessao.py -q -k medir` | 0 | true |
| 2 | `python -m pytest tests/test_custo_sessao.py -q -k passos` | 0 | true |

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
