# Evidência de revisão — DIARIO_DE_OBRAS TK-56a

## Diff (`git diff --stat`)
```
.../hooks/modelo_por_fase_userpromptsubmit.py      |    5 +-
 .claude/projecoes.json                             |   10 +
 .claude/skills/passagem-de-bastao/SKILL.md         |   35 +-
 .claude/skills/scrum-master/SKILL.md               |   23 +-
 .claude/tools/backlog.py                           |  289 ++-
 .claude/tools/ocupacao.py                          |   10 +-
 .claude/tools/rdo.py                               |    6 +-
 .claude/tools/telemetria_hook.py                   |   10 +-
 CHANGELOG.md                                       |   15 +-
 GOVERNANCA.md                                      |    2 +-
 README.md                                          |   33 +-
 docs/CUSTO_DO_PICKUP.md                            |   31 +
 docs/DIARIO_DE_OBRAS.md                            |  519 +++-
 docs/DOC_MAP.md                                    |    2 +
 docs/RDO/INDEX.md                                  |    8 +
 docs/consultant-spec.md                            |   66 +
 docs/plans/P-0735-residencia-e-ponto-de-carga.md   |    2 +-
 docs/plans/P-0737-loop-autonomo.md                 |    2 +-
 docs/plans/P-0738-contexto-esgotado.md             |    2 +-
 docs/plans/P-0739-backlog-instrumento.md           | 2526 +++++++++++++++++++-
 docs/plans/_INBOX.md                               |    2 +-
 docs/plans/_INBOX_HISTORICO.md                     |    1 +
 docs/telemetria.tsv                                |   43 +
 tests/test_backlog.py                              |  635 ++++-
 tests/test_materializar.py                         |   59 +
 tests/test_ocupacao.py                             |   66 +-
 tests/test_rdo.py                                  |   34 +
 tests/test_review_evidence.py                      |   37 +
 tests/test_telemetria_hook.py                      |   71 +-
 29 files changed, 4359 insertions(+), 185 deletions(-)
```

## Arquivos tocados
- `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` — atribuição: da entrega; estado git: ` M`
- `.claude/projecoes.json` — atribuição: alheio; estado git: ` M`
- `.claude/skills/entrega-de-encerramento/SKILL.md` — atribuição: alheio; estado git: `??`
- `.claude/skills/passagem-de-bastao/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/scrum-master/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/tools/backlog.py` — atribuição: alheio; estado git: ` M`
- `.claude/tools/backlog_hook.py` — atribuição: alheio; estado git: `??`
- `.claude/tools/ocupacao.py` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/rdo.py` — atribuição: alheio; estado git: ` M`
- `.claude/tools/telemetria_hook.py` — atribuição: da entrega; estado git: ` M`
- `CHANGELOG.md` — atribuição: alheio; estado git: ` M`
- `GOVERNANCA.md` — atribuição: alheio; estado git: ` M`
- `README.md` — atribuição: alheio; estado git: ` M`
- `docs/CUSTO_DO_PICKUP.md` — atribuição: alheio; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/DOC_MAP.md` — atribuição: alheio; estado git: ` M`
- `docs/Entregas Aceitas/Entregas - P-0739.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-57a-o-teste-do-hook-fixa-o-ambiente-e-afirma-a-invariancia.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-62a-rdo-py-reconhece-tk-n-letra-como-id-de-tarefa.md` — atribuição: alheio; estado git: `??`
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
- `docs/RDO/evidencia/TK-57-TK-57a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-62-TK-62a.md` — atribuição: alheio; estado git: `??`
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
- `tests/test_backlog.py` — atribuição: alheio; estado git: ` M`
- `tests/test_materializar.py` — atribuição: da entrega; estado git: ` M`
- `tests/test_ocupacao.py` — atribuição: da entrega; estado git: ` M`
- `tests/test_rdo.py` — atribuição: alheio; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: alheio; estado git: ` M`
- `tests/test_telemetria_hook.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `eb93490c23e2964d1cd865a683a7d9969809c0a0`
- Arquivos-alvo declarados: `.claude/tools/ocupacao.py`, `.claude/tools/telemetria_hook.py`, `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, `tests/test_ocupacao.py`, `tests/test_telemetria_hook.py`, `tests/test_materializar.py`
- Arquivos tocados: `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, `.claude/projecoes.json`, `.claude/skills/entrega-de-encerramento/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/backlog.py`, `.claude/tools/backlog_hook.py`, `.claude/tools/ocupacao.py`, `.claude/tools/rdo.py`, `.claude/tools/telemetria_hook.py`, `CHANGELOG.md`, `GOVERNANCA.md`, `README.md`, `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/DOC_MAP.md`, `docs/Entregas Aceitas/Entregas - P-0739.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-57a-o-teste-do-hook-fixa-o-ambiente-e-afirma-a-invariancia.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-62a-rdo-py-reconhece-tk-n-letra-como-id-de-tarefa.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0739-BKL-T10-corpus-do-instrumento-e-a-migracao-do-diario-ate-check-verde.md`, `docs/RDO/P-0739-BKL-T10a-drain-o-inbox-de-planos-sai-do-contexto.md`, `docs/RDO/P-0739-BKL-T10b-o-bloco-gerado-da-2-3-e-projetado-inteiro-e-dentro-do-corpus.md`, `docs/RDO/P-0739-BKL-T11-o-hook-o-ponto-de-carga-e-as-skills-que-invocam-o-instrument.md`, `docs/RDO/P-0739-BKL-T11a-o-hook-fala-no-ponto-de-carga-real-stdin-em-utf-8-explicito.md`, `docs/RDO/P-0739-BKL-T9a-rodada-de-transcricao-os-tres-modulos-bkl-t10-bkl-t12.md`, `docs/RDO/evidencia/P-0739-BKL-T10.md`, `docs/RDO/evidencia/P-0739-BKL-T10a.md`, `docs/RDO/evidencia/P-0739-BKL-T10b.md`, `docs/RDO/evidencia/P-0739-BKL-T11.md`, `docs/RDO/evidencia/P-0739-BKL-T11a.md`, `docs/RDO/evidencia/P-0739-BKL-T12.md`, `docs/RDO/evidencia/P-0739-BKL-T9a.md`, `docs/RDO/evidencia/TK-57-TK-57a.md`, `docs/RDO/evidencia/TK-62-TK-62a.md`, `docs/RDO/laudos/P-0739-BKL-T12.md`, `docs/consultant-spec.md`, `docs/plans/P-0735-residencia-e-ponto-de-carga.md`, `docs/plans/P-0737-loop-autonomo.md`, `docs/plans/P-0738-contexto-esgotado.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0742-loop-fora-do-llm.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VIABILIDADE-agente-leitor.md`, `docs/telemetria.tsv`, `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0777-gama.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0900-legado.md`, `tests/test_backlog.py`, `tests/test_materializar.py`, `tests/test_ocupacao.py`, `tests/test_rdo.py`, `tests/test_review_evidence.py`, `tests/test_telemetria_hook.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/tools/backlog.py` → `TK-59a`, `.claude/tools/rdo.py` → `TK-62a`, `README.md` → `TK-51a`, `docs/CUSTO_DO_PICKUP.md` → `TK-58a`, `tests/test_backlog.py` → `TK-57a`, `tests/test_rdo.py` → `TK-62a`, `tests/test_review_evidence.py` → `TK-62a`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-57a-o-teste-do-hook-fixa-o-ambiente-e-afirma-a-invariancia.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-62a-rdo-py-reconhece-tk-n-letra-como-id-de-tarefa.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0739-BKL-T10-corpus-do-instrumento-e-a-migracao-do-diario-ate-check-verde.md`, `docs/RDO/P-0739-BKL-T10a-drain-o-inbox-de-planos-sai-do-contexto.md`, `docs/RDO/P-0739-BKL-T10b-o-bloco-gerado-da-2-3-e-projetado-inteiro-e-dentro-do-corpus.md`, `docs/RDO/P-0739-BKL-T11-o-hook-o-ponto-de-carga-e-as-skills-que-invocam-o-instrument.md`, `docs/RDO/P-0739-BKL-T11a-o-hook-fala-no-ponto-de-carga-real-stdin-em-utf-8-explicito.md`, `docs/RDO/P-0739-BKL-T9a-rodada-de-transcricao-os-tres-modulos-bkl-t10-bkl-t12.md`, `docs/RDO/evidencia/P-0739-BKL-T10.md`, `docs/RDO/evidencia/P-0739-BKL-T10a.md`, `docs/RDO/evidencia/P-0739-BKL-T10b.md`, `docs/RDO/evidencia/P-0739-BKL-T11.md`, `docs/RDO/evidencia/P-0739-BKL-T11a.md`, `docs/RDO/evidencia/P-0739-BKL-T12.md`, `docs/RDO/evidencia/P-0739-BKL-T9a.md`, `docs/RDO/evidencia/TK-57-TK-57a.md`, `docs/RDO/evidencia/TK-62-TK-62a.md`, `docs/RDO/laudos/P-0739-BKL-T12.md`, `docs/plans/P-0735-residencia-e-ponto-de-carga.md`, `docs/plans/P-0737-loop-autonomo.md`, `docs/plans/P-0738-contexto-esgotado.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0742-loop-fora-do-llm.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VIABILIDADE-agente-leitor.md`, `docs/telemetria.tsv`
- Fato: 13 arquivo(s) fora dos alvos e sem atribuição: `.claude/projecoes.json`, `.claude/skills/entrega-de-encerramento/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/backlog_hook.py`, `CHANGELOG.md`, `GOVERNANCA.md`, `docs/DOC_MAP.md`, `docs/Entregas Aceitas/Entregas - P-0739.md`, `docs/consultant-spec.md`, `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0777-gama.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0900-legado.md`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/ocupacao.py`
```
diff --git a/.claude/tools/ocupacao.py b/.claude/tools/ocupacao.py
index 730fd2f..1f08d7f 100644
--- a/.claude/tools/ocupacao.py
+++ b/.claude/tools/ocupacao.py
@@ -43,8 +43,8 @@ silenciada e o script sempre sai 0, nunca bloqueando nem atrasando a chamada que
 
 Superfície testável, separada do I/O do hook: `calcular_ocupacao(linhas) -> (tokens, fonte)` e
 `avaliar(tokens, janela) -> (fracao, cruzou)`. `tests/test_ocupacao.py` exercita as duas; o hook
-(`main`, leitura de stdin/arquivo) não é exercitado por teste — é a superfície de I/O que a
-separação existe para isolar.
+(`main`, leitura de stdin) lê stdin em UTF-8 explícito (`TK-56a`, `DB-53`) e ganhou cobertura por
+subprocesso no mesmo teste.
 """
 from __future__ import annotations
 
@@ -138,7 +138,11 @@ def main(argv: list[str] | None = None) -> int:  # noqa: ARG001 — hook não re
     """Ponto de entrada do hook `PreToolUse`. Falha aberta: qualquer exceção ⇒ exit 0
     silencioso, sem imprimir nada e sem atrasar a chamada de ferramenta que disparou o hook."""
     try:
-        payload = json.loads(sys.stdin.read())
+        try:
+            raw = sys.stdin.buffer.read().decode("utf-8", errors="replace")
+        except AttributeError:
+            raw = sys.stdin.read()
+        payload = json.loads(raw)
 
         if payload.get("agent_type"):
             return 0

```

### `.claude/tools/telemetria_hook.py`
```
diff --git a/.claude/tools/telemetria_hook.py b/.claude/tools/telemetria_hook.py
index 4e20912..b0d7064 100644
--- a/.claude/tools/telemetria_hook.py
+++ b/.claude/tools/telemetria_hook.py
@@ -34,8 +34,8 @@ sempre sai 0, sem nunca bloquear ou atrasar a chamada que disparou o hook.
 Superfície testável, separada do I/O de stdin do hook: `calcular_consumo` (pura) e `processar`
 (núcleo do hook, recebe payload e caminhos já resolvidos em vez de ler stdin/`sys.argv` — mesmo
 desenho de `apply`/`check`/`drift` em `materializar.py`). `tests/test_telemetria_hook.py`
-exercita as duas; `main` (leitura de stdin, subprocess real) não é exercitado por teste — é a
-superfície de I/O que a separação existe para isolar.
+exercita as duas; `main` lê stdin em UTF-8 explícito (`TK-56a`, `DB-53`) e ganhou cobertura por
+subprocesso no mesmo teste, restrita ao ramo `agent_type` fora do filtro do kit.
 """
 from __future__ import annotations
 
@@ -210,7 +210,11 @@ def main(argv: list[str] | None = None) -> int:  # noqa: ARG001 — hook não re
     """Ponto de entrada do hook `SubagentStop`. Falha aberta: qualquer exceção ⇒ exit 0
     silencioso, sem imprimir nada e sem atrasar/bloquear o encerramento do subagente."""
     try:
-        payload = json.loads(sys.stdin.read())
+        try:
+            raw = sys.stdin.buffer.read().decode("utf-8", errors="replace")
+        except AttributeError:
+            raw = sys.stdin.read()
+        payload = json.loads(raw)
         repo_root = _repo_root()
         processar(payload, _estado_path_default(repo_root), _telemetria_cli_default(repo_root))
         return 0

```

### `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`
```
diff --git a/.claude/global/hooks/modelo_por_fase_userpromptsubmit.py b/.claude/global/hooks/modelo_por_fase_userpromptsubmit.py
index 2b6302d..82a8713 100644
--- a/.claude/global/hooks/modelo_por_fase_userpromptsubmit.py
+++ b/.claude/global/hooks/modelo_por_fase_userpromptsubmit.py
@@ -98,7 +98,10 @@ _NUDGE = {
 
 def main() -> None:
     try:
-        raw = sys.stdin.read()
+        try:
+            raw = sys.stdin.buffer.read().decode("utf-8", errors="replace")
+        except AttributeError:
+            raw = sys.stdin.read()
         data = json.loads(raw) if raw.strip() else {}
     except (ValueError, OSError):
         print("{}")

```

### `tests/test_ocupacao.py`
```
diff --git a/tests/test_ocupacao.py b/tests/test_ocupacao.py
index 98e5219..6703ef7 100644
--- a/tests/test_ocupacao.py
+++ b/tests/test_ocupacao.py
@@ -1,7 +1,8 @@
 """EXA-T13 (`docs/plans/P-0734-execucao-autonoma.md` `### T13`) — TF/TR de
 `.claude/tools/ocupacao.py`: `calcular_ocupacao` (numerador, com ramo de fallback estimado) e
-`avaliar` (fração e cruzamento do limiar de 50%, `GOVERNANCA.md` §4.3). Por desenho da tarefa, o
-hook (`main`, I/O de stdin/transcript) não é exercitado aqui — só as duas funções puras.
+`avaliar` (fração e cruzamento do limiar de 50%, `GOVERNANCA.md` §4.3). O hook (`main`, I/O de
+stdin/transcript) ganhou cobertura por subprocesso na `TK-56a` (`DB-53`,
+`docs/plans/P-0739-backlog-instrumento.md:122`) — leitura de stdin em UTF-8 explícito.
 
 `.claude/tools/` não é pacote importável (diretório com ponto no nome) — o módulo é carregado por
 caminho via `importlib.util.spec_from_file_location`, mesmo padrão de `tests/test_rdo.py` e
@@ -11,6 +12,9 @@ from __future__ import annotations
 
 import importlib.util
 import json
+import os
+import subprocess
+import sys
 from pathlib import Path
 
 _ROOT = Path(__file__).resolve().parents[1]
@@ -169,3 +173,61 @@ def test_tr_janela_tokens_aceita_sufixo_e_ignora_lixo(monkeypatch):
     for lixo in ("lixo", "", "-5", "0"):
         monkeypatch.setenv("PANTONIC_CONTEXT_TOKENS_MAX", lixo)
         assert _load_ocupacao().JANELA_TOKENS == 1_000_000
+
+
+def test_tf_hook_executavel_stdin_utf8_cruza_o_limiar_e_devolve_aviso(tmp_path):
+    """TK-56a (`DB-53`): `main` lê stdin em UTF-8 explícito, não na codificação do host — as
+    três cláusulas: processo real via subprocess, `env=` mínimo, mesma saída nos dois mundos de
+    `PYTHONUTF8`. O `hook_event_name` acentuado viaja intacto do payload até a saída."""
+    transcript = tmp_path / "transcript.jsonl"
+    transcript.write_text("linha de teste ação " * 50, encoding="utf-8")
+    payload = json.dumps(
+        {"hook_event_name": "PreToolUse-ação", "transcript_path": str(transcript)},
+        ensure_ascii=False,
+    ).encode("utf-8")
+    env = {
+        "SYSTEMROOT": os.environ["SYSTEMROOT"],
+        "PATH": os.environ["PATH"],
+        "PANTONIC_CONTEXT_TOKENS_MAX": "1",
+    }
+
+    resultado = subprocess.run(
+        [sys.executable, str(_OCUPACAO_PATH)],
+        input=payload,
+        capture_output=True,
+        env=env,
+    )
+
+    assert resultado.returncode == 0
+    assert resultado.stdout.strip() != b""
+    saida = json.loads(resultado.stdout.decode("utf-8"))
+    assert saida["hookSpecificOutput"]["hookEventName"] == "PreToolUse-ação"
+
+    env_utf8 = dict(env)
+    env_utf8["PYTHONUTF8"] = "1"
+    resultado_utf8 = subprocess.run(
+        [sys.executable, str(_OCUPACAO_PATH)],
+        input=payload,
+        capture_output=True,
+        env=env_utf8,
+    )
+
+    assert resultado_utf8.returncode == 0
+    assert resultado_utf8.stdout == resultado.stdout
+
+    stub = tmp_path / "hook_quebrado.py"
+    stub.write_text(
+        "import sys\n"
+        "data = sys.stdin.read()\n"
+        "sys.stdout.write(str(len(data)))\n",
+        encoding="utf-8",
+    )
+
+    quebrado_sem = subprocess.run(
+        [sys.executable, str(stub)], input=payload, capture_output=True, env=env,
+    )
+    quebrado_com = subprocess.run(
+        [sys.executable, str(stub)], input=payload, capture_output=True, env=env_utf8,
+    )
+
+    assert quebrado_sem.stdout != quebrado_com.stdout

```

### `tests/test_telemetria_hook.py`
```
diff --git a/tests/test_telemetria_hook.py b/tests/test_telemetria_hook.py
index f3adc21..80ee51e 100644
--- a/tests/test_telemetria_hook.py
+++ b/tests/test_telemetria_hook.py
@@ -8,16 +8,22 @@ vem mais de inferência sobre prosa, e sim do estado que o `scrum-master` grava
 caminho via `importlib.util.spec_from_file_location`, mesmo padrão de `tests/test_ocupacao.py` e
 `tests/test_materializar.py`.
 
-Superfície testável, separada do I/O de stdin do hook (`main`, não exercitado aqui — mesmo desenho
-de `ocupacao.py`): `calcular_consumo` (pura, soma de tokens/tool_uses/duração a partir das linhas
-do `agent_transcript_path`) e `processar` (núcleo do hook, recebe payload e caminhos já resolvidos
-em vez de ler stdin/`sys.argv` — mesmo padrão de `apply`/`check`/`drift` em `materializar.py`).
-`processar` chama o CLI real de `telemetria.py` via subprocess (`--file` apontado para `tmp_path`),
-nunca reimplementa a validação de coluna (Cuidado do dossiê `T55`)."""
+Superfície testável, separada do I/O de stdin do hook: `calcular_consumo` (pura, soma de
+tokens/tool_uses/duração a partir das linhas do `agent_transcript_path`) e `processar` (núcleo do
+hook, recebe payload e caminhos já resolvidos em vez de ler stdin/`sys.argv` — mesmo padrão de
+`apply`/`check`/`drift` em `materializar.py`). `processar` chama o CLI real de `telemetria.py` via
+subprocess (`--file` apontado para `tmp_path`), nunca reimplementa a validação de coluna (Cuidado
+do dossiê `T55`). `main` ganhou cobertura por subprocesso na `TK-56a` (`DB-53`) — leitura de stdin
+em UTF-8 explícito — restrita ao ramo `agent_type` fora do filtro do kit, o único seguro para
+rodar contra os caminhos de produção reais que `main` resolve sozinho (`_estado_path_default`/
+`_telemetria_cli_default`, sem injeção possível pela CLI)."""
 from __future__ import annotations
 
 import importlib.util
 import json
+import os
+import subprocess
+import sys
 from pathlib import Path
 
 _ROOT = Path(__file__).resolve().parents[1]
@@ -296,3 +302,56 @@ def test_tr_processar_agent_type_fora_do_filtro_e_silencio_e_preserva_o_estado(t
     assert escreveu is False
     assert tsv_path.read_text(encoding="utf-8") == _HEADER
     assert estado_path.exists()
+
+
+def test_tf_hook_executavel_stdin_utf8_nao_falha_e_preserva_invariancia(tmp_path):
+    """TK-56a (`DB-53`): `main` lê stdin em UTF-8 explícito, não na codificação do host — as três
+    cláusulas: processo real via subprocess, `env=` mínimo, mesma saída nos dois mundos de
+    `PYTHONUTF8`. `agent_type` fora do filtro do kit é o único ramo seguro para rodar `main` por
+    subprocesso contra os caminhos de produção reais (sem tocar `.claude/estado/` nem o TSV
+    real — mesmo ramo de `test_tr_processar_agent_type_fora_do_filtro_e_silencio_e_preserva_o_estado`
+    acima, agora pelo executável)."""
+    payload = json.dumps(
+        {"agent_type": "context-scout", "agent_transcript_path": "não-existe.jsonl"},
+        ensure_ascii=False,
+    ).encode("utf-8")
+    env = {"SYSTEMROOT": os.environ["SYSTEMROOT"], "PATH": os.environ["PATH"]}
+
+    resultado = subprocess.run(
+        [sys.executable, str(_HOOK_PATH)],
+        input=payload,
+        capture_output=True,
+        env=env,
+    )
+
+    assert resultado.returncode == 0
+    assert resultado.stdout == b""
+
+    env_utf8 = dict(env)
+    env_utf8["PYTHONUTF8"] = "1"
+    resultado_utf8 = subprocess.run(
+        [sys.executable, str(_HOOK_PATH)],
+        input=payload,
+        capture_output=True,
+        env=env_utf8,
+    )
+
+    assert resultado_utf8.returncode == 0
+    assert resultado_utf8.stdout == resultado.stdout
+
+    stub = tmp_path / "hook_quebrado.py"
+    stub.write_text(
+        "import sys\n"
+        "data = sys.stdin.read()\n"
+        "sys.stdout.write(str(len(data)))\n",
+        encoding="utf-8",
+    )
+
+    quebrado_sem = subprocess.run(
+        [sys.executable, str(stub)], input=payload, capture_output=True, env=env,
+    )
+    quebrado_com =
```
[truncado em 4000 caracteres]

### `tests/test_materializar.py`
```
diff --git a/tests/test_materializar.py b/tests/test_materializar.py
index a96991b..65e260f 100644
--- a/tests/test_materializar.py
+++ b/tests/test_materializar.py
@@ -16,10 +16,15 @@ from __future__ import annotations
 import importlib.util
 import json
 import os
+import subprocess
+import sys
 from pathlib import Path
 
 _ROOT = Path(__file__).resolve().parents[1]
 _MATERIALIZAR_PATH = _ROOT / ".claude" / "tools" / "materializar.py"
+_MODELO_POR_FASE_HOOK_PATH = (
+    _ROOT / ".claude" / "global" / "hooks" / "modelo_por_fase_userpromptsubmit.py"
+)
 
 
 def _load_materializar():
@@ -550,3 +555,57 @@ def test_tr_drift_projeto_ok_no_repositorio_real_depois_do_apply():
 
     assert exit_apply == 0
     assert exit_drift == 0
+
+
+def test_tf_hook_modelo_por_fase_executavel_stdin_utf8_classifica_a_fase(tmp_path):
+    """TK-56a (`DB-53`): o hook global `modelo_por_fase_userpromptsubmit.py`
+    (`.claude/global/hooks/`, materializado no ponto de carga desta suíte) lê stdin em UTF-8
+    explícito, não na codificação do host — as três cláusulas: processo real via subprocess,
+    `env=` mínimo, mesma saída nos dois mundos de `PYTHONUTF8`. O reparo é global: vale para
+    todos os projetos consumidores do kit, não só o PantonicApp."""
+    payload = json.dumps(
+        {"prompt": "faça uma análise arquitetural do módulo"},
+        ensure_ascii=False,
+    ).encode("utf-8")
+    env = {"SYSTEMROOT": os.environ["SYSTEMROOT"], "PATH": os.environ["PATH"]}
+
+    resultado = subprocess.run(
+        [sys.executable, str(_MODELO_POR_FASE_HOOK_PATH)],
+        input=payload,
+        capture_output=True,
+        env=env,
+    )
+
+    assert resultado.returncode == 0
+    assert resultado.stdout.strip() != b""
+    saida = json.loads(resultado.stdout.decode("utf-8"))
+    assert saida["hookSpecificOutput"]["hookEventName"] == "UserPromptSubmit"
+
+    env_utf8 = dict(env)
+    env_utf8["PYTHONUTF8"] = "1"
+    resultado_utf8 = subprocess.run(
+        [sys.executable, str(_MODELO_POR_FASE_HOOK_PATH)],
+        input=payload,
+        capture_output=True,
+        env=env_utf8,
+    )
+
+    assert resultado_utf8.returncode == 0
+    assert resultado_utf8.stdout == resultado.stdout
+
+    stub = tmp_path / "hook_quebrado.py"
+    stub.write_text(
+        "import sys\n"
+        "data = sys.stdin.read()\n"
+        "sys.stdout.write(str(len(data)))\n",
+        encoding="utf-8",
+    )
+
+    quebrado_sem = subprocess.run(
+        [sys.executable, str(stub)], input=payload, capture_output=True, env=env,
+    )
+    quebrado_com = subprocess.run(
+        [sys.executable, str(stub)], input=payload, capture_output=True, env=env_utf8,
+    )
+
+    assert quebrado_sem.stdout != quebrado_com.stdout

```

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
