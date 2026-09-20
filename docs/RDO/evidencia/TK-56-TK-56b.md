# Evidência de revisão — DIARIO_DE_OBRAS TK-56b

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
 docs/DIARIO_DE_OBRAS.md                            |  659 ++++-
 docs/DOC_MAP.md                                    |    2 +
 docs/RDO/INDEX.md                                  |    9 +
 docs/consultant-spec.md                            |   66 +
 docs/plans/P-0735-residencia-e-ponto-de-carga.md   |    2 +-
 docs/plans/P-0737-loop-autonomo.md                 |    2 +-
 docs/plans/P-0738-contexto-esgotado.md             |    2 +-
 docs/plans/P-0739-backlog-instrumento.md           | 2526 +++++++++++++++++++-
 docs/plans/_INBOX.md                               |    2 +-
 docs/plans/_INBOX_HISTORICO.md                     |    1 +
 docs/telemetria.tsv                                |   46 +
 tests/test_backlog.py                              |  635 ++++-
 tests/test_materializar.py                         |   71 +
 tests/test_ocupacao.py                             |   66 +-
 tests/test_rdo.py                                  |   34 +
 tests/test_review_evidence.py                      |   37 +
 tests/test_telemetria_hook.py                      |  117 +-
 29 files changed, 4561 insertions(+), 185 deletions(-)
```

## Arquivos tocados
- `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` — atribuição: alheio; estado git: ` M`
- `.claude/projecoes.json` — atribuição: alheio; estado git: ` M`
- `.claude/skills/entrega-de-encerramento/SKILL.md` — atribuição: alheio; estado git: `??`
- `.claude/skills/passagem-de-bastao/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/scrum-master/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/tools/backlog.py` — atribuição: alheio; estado git: ` M`
- `.claude/tools/backlog_hook.py` — atribuição: alheio; estado git: `??`
- `.claude/tools/ocupacao.py` — atribuição: alheio; estado git: ` M`
- `.claude/tools/rdo.py` — atribuição: alheio; estado git: ` M`
- `.claude/tools/telemetria_hook.py` — atribuição: alheio; estado git: ` M`
- `CHANGELOG.md` — atribuição: alheio; estado git: ` M`
- `GOVERNANCA.md` — atribuição: alheio; estado git: ` M`
- `README.md` — atribuição: alheio; estado git: ` M`
- `docs/CUSTO_DO_PICKUP.md` — atribuição: alheio; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/DOC_MAP.md` — atribuição: alheio; estado git: ` M`
- `docs/Entregas Aceitas/Entregas - P-0739.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-56a-os-tres-pontos-de-carga-passam-a-ler-stdin-em-utf-8-explicit.md` — atribuição: alheio; estado git: `??`
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
- `docs/RDO/evidencia/TK-56-TK-56a.md` — atribuição: alheio; estado git: `??`
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
- `tests/test_ocupacao.py` — atribuição: alheio; estado git: ` M`
- `tests/test_rdo.py` — atribuição: alheio; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: alheio; estado git: ` M`
- `tests/test_telemetria_hook.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `eb93490c23e2964d1cd865a683a7d9969809c0a0`
- Arquivos-alvo declarados: `tests/test_telemetria_hook.py`, `tests/test_materializar.py`
- Arquivos tocados: `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, `.claude/projecoes.json`, `.claude/skills/entrega-de-encerramento/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/backlog.py`, `.claude/tools/backlog_hook.py`, `.claude/tools/ocupacao.py`, `.claude/tools/rdo.py`, `.claude/tools/telemetria_hook.py`, `CHANGELOG.md`, `GOVERNANCA.md`, `README.md`, `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/DOC_MAP.md`, `docs/Entregas Aceitas/Entregas - P-0739.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-56a-os-tres-pontos-de-carga-passam-a-ler-stdin-em-utf-8-explicit.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-57a-o-teste-do-hook-fixa-o-ambiente-e-afirma-a-invariancia.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-62a-rdo-py-reconhece-tk-n-letra-como-id-de-tarefa.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0739-BKL-T10-corpus-do-instrumento-e-a-migracao-do-diario-ate-check-verde.md`, `docs/RDO/P-0739-BKL-T10a-drain-o-inbox-de-planos-sai-do-contexto.md`, `docs/RDO/P-0739-BKL-T10b-o-bloco-gerado-da-2-3-e-projetado-inteiro-e-dentro-do-corpus.md`, `docs/RDO/P-0739-BKL-T11-o-hook-o-ponto-de-carga-e-as-skills-que-invocam-o-instrument.md`, `docs/RDO/P-0739-BKL-T11a-o-hook-fala-no-ponto-de-carga-real-stdin-em-utf-8-explicito.md`, `docs/RDO/P-0739-BKL-T9a-rodada-de-transcricao-os-tres-modulos-bkl-t10-bkl-t12.md`, `docs/RDO/evidencia/P-0739-BKL-T10.md`, `docs/RDO/evidencia/P-0739-BKL-T10a.md`, `docs/RDO/evidencia/P-0739-BKL-T10b.md`, `docs/RDO/evidencia/P-0739-BKL-T11.md`, `docs/RDO/evidencia/P-0739-BKL-T11a.md`, `docs/RDO/evidencia/P-0739-BKL-T12.md`, `docs/RDO/evidencia/P-0739-BKL-T9a.md`, `docs/RDO/evidencia/TK-56-TK-56a.md`, `docs/RDO/evidencia/TK-57-TK-57a.md`, `docs/RDO/evidencia/TK-62-TK-62a.md`, `docs/RDO/laudos/P-0739-BKL-T12.md`, `docs/consultant-spec.md`, `docs/plans/P-0735-residencia-e-ponto-de-carga.md`, `docs/plans/P-0737-loop-autonomo.md`, `docs/plans/P-0738-contexto-esgotado.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0742-loop-fora-do-llm.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VIABILIDADE-agente-leitor.md`, `docs/telemetria.tsv`, `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0777-gama.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0900-legado.md`, `tests/test_backlog.py`, `tests/test_materializar.py`, `tests/test_ocupacao.py`, `tests/test_rdo.py`, `tests/test_review_evidence.py`, `tests/test_telemetria_hook.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` → `TK-56a`, `.claude/tools/backlog.py` → `TK-59a`, `.claude/tools/ocupacao.py` → `TK-56a`, `.claude/tools/rdo.py` → `TK-62a`, `.claude/tools/telemetria_hook.py` → `TK-56a`, `README.md` → `TK-51a`, `docs/CUSTO_DO_PICKUP.md` → `TK-58a`, `tests/test_backlog.py` → `TK-57a`, `tests/test_ocupacao.py` → `TK-56a`, `tests/test_rdo.py` → `TK-62a`, `tests/test_review_evidence.py` → `TK-62a`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-56a-os-tres-pontos-de-carga-passam-a-ler-stdin-em-utf-8-explicit.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-57a-o-teste-do-hook-fixa-o-ambiente-e-afirma-a-invariancia.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-62a-rdo-py-reconhece-tk-n-letra-como-id-de-tarefa.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0739-BKL-T10-corpus-do-instrumento-e-a-migracao-do-diario-ate-check-verde.md`, `docs/RDO/P-0739-BKL-T10a-drain-o-inbox-de-planos-sai-do-contexto.md`, `docs/RDO/P-0739-BKL-T10b-o-bloco-gerado-da-2-3-e-projetado-inteiro-e-dentro-do-corpus.md`, `docs/RDO/P-0739-BKL-T11-o-hook-o-ponto-de-carga-e-as-skills-que-invocam-o-instrument.md`, `docs/RDO/P-0739-BKL-T11a-o-hook-fala-no-ponto-de-carga-real-stdin-em-utf-8-explicito.md`, `docs/RDO/P-0739-BKL-T9a-rodada-de-transcricao-os-tres-modulos-bkl-t10-bkl-t12.md`, `docs/RDO/evidencia/P-0739-BKL-T10.md`, `docs/RDO/evidencia/P-0739-BKL-T10a.md`, `docs/RDO/evidencia/P-0739-BKL-T10b.md`, `docs/RDO/evidencia/P-0739-BKL-T11.md`, `docs/RDO/evidencia/P-0739-BKL-T11a.md`, `docs/RDO/evidencia/P-0739-BKL-T12.md`, `docs/RDO/evidencia/P-0739-BKL-T9a.md`, `docs/RDO/evidencia/TK-56-TK-56a.md`, `docs/RDO/evidencia/TK-57-TK-57a.md`, `docs/RDO/evidencia/TK-62-TK-62a.md`, `docs/RDO/laudos/P-0739-BKL-T12.md`, `docs/plans/P-0735-residencia-e-ponto-de-carga.md`, `docs/plans/P-0737-loop-autonomo.md`, `docs/plans/P-0738-contexto-esgotado.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0742-loop-fora-do-llm.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VIABILIDADE-agente-leitor.md`, `docs/telemetria.tsv`
- Fato: 13 arquivo(s) fora dos alvos e sem atribuição: `.claude/projecoes.json`, `.claude/skills/entrega-de-encerramento/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/backlog_hook.py`, `CHANGELOG.md`, `GOVERNANCA.md`, `docs/DOC_MAP.md`, `docs/Entregas Aceitas/Entregas - P-0739.md`, `docs/consultant-spec.md`, `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0777-gama.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0900-legado.md`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `tests/test_telemetria_hook.py`
```
diff --git a/tests/test_telemetria_hook.py b/tests/test_telemetria_hook.py
index f3adc21..958b077 100644
--- a/tests/test_telemetria_hook.py
+++ b/tests/test_telemetria_hook.py
@@ -8,16 +8,23 @@ vem mais de inferência sobre prosa, e sim do estado que o `scrum-master` grava
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
 
+import datetime
 import importlib.util
 import json
+import os
+import subprocess
+import sys
 from pathlib import Path
 
 _ROOT = Path(__file__).resolve().parents[1]
@@ -67,6 +74,32 @@ def _payload(**overrides) -> dict:
     return valores
 
 
+def _montar_raiz_isolada(base: Path, nome: str, fonte_hook: str) -> tuple[Path, Path, Path, Path]:
+    """Raiz falsa em `base/nome` para relocar `_repo_root()` do hook (derivada de `__file__`):
+    hook copiado em `.claude/tools/telemetria_hook.py`, CLI real copiado em
+    `.claude/tools/telemetria.py`, estado válido em `.claude/estado/tarefa-corrente.json` e
+    `docs/` — nunca toca `.claude/estado/` nem `docs/telemetria.tsv` reais. Devolve
+    `(hook_path, estado_path, tsv_path, transcript_path)`; o transcript tem nome acentuado e é
+    o canal por onde o payload acentuado chega ao observável (efeito colateral, já que o hook
+    é silencioso por contrato)."""
+    raiz = base / nome
+    tools_dir = raiz / ".claude" / "tools"
+    tools_dir.mkdir(parents=True)
+    hook_path = tools_dir / "telemetria_hook.py"
+    hook_path.write_text(fonte_hook, encoding="utf-8")
+    (tools_dir / "telemetria.py").write_text(
+        _TELEMETRIA_CLI_PATH.read_text(encoding="utf-8"), encoding="utf-8"
+    )
+    estado_path = raiz / ".claude" / "estado" / "tarefa-corrente.json"
+    estado_path.parent.mkdir(parents=True)
+    estado_path.write_text(json.dumps(_estado_valido()), encoding="utf-8")
+    (raiz / "docs").mkdir(parents=True)
+    transcript_path = raiz / "análise.jsonl"
+    transcript_path.write_text("", encoding="utf-8")
+    tsv_path = raiz / "docs" / "telemetria.tsv"
+    return hook_path, estado_path, tsv_path, transcript_path
+
+
 def test_tf_calcular_consumo_soma_tokens_e_conta_tool_uses_de_n_entradas_assistant():
     """TF: `tokens_k` = `usage` (input+cache_creation+cache_read+output)/1000 da **última**
     entrada assistant (LM-T2b — contingência 2 acionada: esta asserção afirmava a soma por
@@ -296,3 +329,75 @@ def test_tr_processar_agent_type_fora_do_filtro_e_silencio_e_preserva_o_estado(t
     assert escreveu is False
     assert tsv_path.read_text(enco
```
[truncado em 4000 caracteres]

### `tests/test_materializar.py`
```
diff --git a/tests/test_materializar.py b/tests/test_materializar.py
index a96991b..c4f345d 100644
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
@@ -550,3 +555,69 @@ def test_tr_drift_projeto_ok_no_repositorio_real_depois_do_apply():
 
     assert exit_apply == 0
     assert exit_drift == 0
+
+
+def test_tf_hook_modelo_por_fase_executavel_stdin_utf8_classifica_a_fase(tmp_path):
+    """TK-56b: repara a ressalva da `TK-56a` — o par negativo deixa de ser um stub (que só
+    discriminava a si mesmo) e passa a ser o produto revertido, extraído do arquivo real do
+    hook global `modelo_por_fase_userpromptsubmit.py`. O prompt tem um único gatilho de
+    classificação, e ele é acentuado — `{"prompt": "me dê sua análise disso"}`; o payload usado
+    até aqui (`"faça uma análise arquitetural do módulo"`) casava por `arquitet` (sem acento) em
+    qualquer combinação e não discriminava nada. Mundo hostil: `env` mínimo +
+    `PYTHONIOENCODING=cp1252`. Mundo seguro: `env` mínimo + `PYTHONUTF8=1`. Medido em
+    2026-09-20: reparado dá 470 B nos dois mundos; revertido dá 2 B (`{}`) no hostil e 470 B no
+    seguro — comparação por bytes, válida porque a saída é `json.dumps` com `ensure_ascii`
+    default (`stdout` ASCII puro)."""
+    fonte = _MODELO_POR_FASE_HOOK_PATH.read_text(encoding="utf-8")
+    bloco_reparo = (
+        "        try:\n"
+        "            raw = sys.stdin.buffer.read().decode(\"utf-8\", errors=\"replace\")\n"
+        "        except AttributeError:\n"
+        "            raw = sys.stdin.read()\n"
+    )
+    assert bloco_reparo in fonte
+    fonte_revertida = fonte.replace(bloco_reparo, "        raw = sys.stdin.read()\n")
+
+    payload = json.dumps(
+        {"prompt": "me dê sua análise disso"},
+        ensure_ascii=False,
+    ).encode("utf-8")
+
+    env_hostil = {
+        "SYSTEMROOT": os.environ["SYSTEMROOT"],
+        "PATH": os.environ["PATH"],
+        "PYTHONIOENCODING": "cp1252",
+    }
+    env_seguro = {
+        "SYSTEMROOT": os.environ["SYSTEMROOT"],
+        "PATH": os.environ["PATH"],
+        "PYTHONUTF8": "1",
+    }
+
+    def _rodar(nome: str, fonte_hook: str, env: dict) -> subprocess.CompletedProcess:
+        script = tmp_path / nome
+        script.write_text(fonte_hook, encoding="utf-8")
+        return subprocess.run(
+            [sys.executable, str(script)], input=payload, capture_output=True, env=env,
+        )
+
+    reparado_hostil = _rodar("reparado_hostil.py", fonte, env_hostil)
+    reparado_seguro = _rodar("reparado_seguro.py", fonte, env_seguro)
+    revertido_hostil = _rodar("revertido_hostil.py", fonte_revertida, env_hostil)
+    revertido_seguro = _rodar("revertido_seguro.py", fonte_revertida, env_seguro)
+
+    for resultado in (reparado_hostil, reparado_seguro, revertido_hostil, revertido_seguro):
+        assert resultado.returncode == 0
+
+    # (i) produto reparado dá a mesma saída nos dois mundos
+    assert reparado_hostil.stdout == reparado_seguro.stdout
+    assert len(reparado_hostil.stdout.strip()) == 470
+    saida = json.loads(reparado_hostil.stdout.decode("utf-8"))
+    assert saida["hookSpecificOutput"]["hookEventName"] == "UserPromptSubmit"
+    # (iii) o valor acentuado chega íntegro ao observável no mundo hostil — a asserção acima
+    # já prova: a saída do mundo hostil é igual à do mundo seguro, byte a byte.
+
+    # (ii) produto revertido dá saídas diferentes entre os dois mundos
+    assert revertido_hostil.stdout != revertido_seguro.stdout
+    assert revertido_hostil.stdout.strip() == b"{}"
+    asser
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
