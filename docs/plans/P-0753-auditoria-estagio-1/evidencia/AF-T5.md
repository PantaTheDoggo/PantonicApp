# Evidência de revisão — P-0753 AF-T5

## Diff (`git diff --stat`)
```
.claude/skills/scrum-master/SKILL.md               |   2 +-
 .claude/tools/encerrar.py                          |  12 +-
 .claude/tools/telemetria_hook.py                   | 192 +++++++++++++++++++--
 GOVERNANCA.md                                      |   8 +-
 docs/ACIONAMENTOS_CONSULTOR.tsv                    |   1 +
 docs/DIARIO_DE_OBRAS.md                            |   2 +-
 docs/plans/P-0753-auditoria-estagio-1/cenario.md   |  46 +++++
 docs/plans/P-0753-auditoria-estagio-1/estado.tsv   |   2 +-
 .../evidencia/P-0753-AF-T5-medida.json             |  50 ++++++
 docs/plans/P-0753-auditoria-estagio-1/plano.md     |   5 +-
 docs/telemetria.tsv                                |   2 +
 tests/test_encerrar.py                             |  22 +++
 tests/test_telemetria_hook.py                      | 153 ++++++++++++++--
 13 files changed, 456 insertions(+), 41 deletions(-)
```

## Arquivos tocados
- `.claude/skills/scrum-master/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/encerrar.py` — atribuição: da entrega; estado git: `??`
- `.claude/tools/telemetria_hook.py` — atribuição: da entrega; estado git: ` M`
- `GOVERNANCA.md` — atribuição: da entrega; estado git: ` M`
- `docs/ACIONAMENTOS_CONSULTOR.tsv` — atribuição: alheio; estado git: `??`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/cenario.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T5-medida.json` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/plano.md` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_encerrar.py` — atribuição: da entrega; estado git: `??`
- `tests/test_telemetria_hook.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `c0a8e22e48e6a6242972b055f9224ad0c9eb2f5d`
- Arquivos-alvo declarados: `.claude/tools/telemetria_hook.py`, `tests/test_telemetria_hook.py`, `.claude/tools/encerrar.py`, `tests/test_encerrar.py`, `GOVERNANCA.md`, `.claude/skills/scrum-master/SKILL.md`
- Arquivos tocados: `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/encerrar.py`, `.claude/tools/telemetria_hook.py`, `GOVERNANCA.md`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/cenario.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T5-medida.json`, `docs/plans/P-0753-auditoria-estagio-1/plano.md`, `docs/telemetria.tsv`, `tests/test_encerrar.py`, `tests/test_telemetria_hook.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/cenario.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T5-medida.json`, `docs/plans/P-0753-auditoria-estagio-1/plano.md`, `docs/telemetria.tsv`
- Fato: 1 arquivo(s) fora dos alvos e sem atribuição: `docs/ACIONAMENTOS_CONSULTOR.tsv`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/telemetria_hook.py`
```
diff --git a/.claude/tools/telemetria_hook.py b/.claude/tools/telemetria_hook.py
index b635aa0..772503b 100644
--- a/.claude/tools/telemetria_hook.py
+++ b/.claude/tools/telemetria_hook.py
@@ -19,13 +19,22 @@ de turnos); `tool_uses` = contagem de blocos `type == "tool_use"` no `message.co
 exatamente uma entrada, nunca repetido); `duracao_s` = diferença, em segundos, entre o primeiro e
 o último `timestamp` do transcript.
 
-**Filtro** (`DP-S` `### 23.3` item 4; restrito na `TK-88b`): o hook só age quando `agent_type` é
-`pantonic-executor` — o estado `tarefa-corrente.json` é do despacho do executor
-(`.claude/skills/scrum-master/SKILL.md`, Passo 4), e nenhum outro papel do kit o consome. Fora do
-filtro (inclusive outro papel `pantonic-*`, como `pantonic-reviewer`), ou sem estado gravado
-(despacho fora do loop), é silêncio: exit 0, sem escrever nada e **sem consumir o estado** (ele
-fica para o despacho real consumir depois). O estado só é apagado depois de a linha ser escrita
-com sucesso.
+**Filtro** (`DP-S` `### 23.3` item 4; generalizado na `DAF-15`/`DAF-25`): o hook age para todo
+`agent_type` iniciado por `pantonic-` — cada papel do kit grava a própria rodada, com o papel no
+identificador da tarefa. Fora do filtro (`agent_type` que não começa por `pantonic-`, ou vazio),
+ou sem `agent_transcript_path` legível, é silêncio: exit 0, sem escrever nada. O estado
+`tarefa-corrente.json` **não se apaga mais** — ele vale até o despacho seguinte do executor, que
+o sobrescreve; só o executor depende dele para a própria linha (sem estado, o executor fica em
+silêncio, como antes).
+
+**Papel da linha:** `pantonic-executor` grava `estado["tarefa"]`; `pantonic-reviewer` grava
+`<tarefa>-revisao`; `pantonic-consultant` grava `<tarefa>-consultor-<n>` (`<n>` = 1 + linhas da
+série cuja `tarefa` já começa por `<tarefa>-consultor-`); `pantonic-planner` grava
+`<P-n>-planejador`; `pantonic-model-designer` grava `<P-n>-modelador`; `pantonic-scout` grava
+`<P-n>-scout`; outro `pantonic-<nome>` grava `<P-n>-<nome>`. `<tarefa>` vem de `estado["tarefa"]`;
+`<P-n>` vem da primeira ocorrência de `P-` seguido de dígitos no texto da primeira entrada
+`type == "user"` do transcript. Sem o id que o papel pede, a linha grava `sem-id-<sufixo>` em vez
+de ficar em silêncio.
 
 **Cuidado:** este hook é **cliente** do CLI que a `T7` entregou
 (`.claude/tools/telemetria.py append`) — chamado via subprocess, nunca reimplementa validação de
@@ -44,11 +53,24 @@ from __future__ import annotations
 
 import datetime
 import json
+import re
 import subprocess
 import sys
 from pathlib import Path
 
-_AGENT_TYPE_EXECUTOR = "pantonic-executor"  # TK-88b — só o executor grava/consome o estado
+_AGENT_TYPE_EXECUTOR = "pantonic-executor"  # papel com regra própria de tarefa/modelo/projeto
+
+_SUFIXO_POR_AGENT_TYPE = {
+    "pantonic-reviewer": "revisao",
+    "pantonic-consultant": "consultor",
+    "pantonic-planner": "planejador",
+    "pantonic-model-designer": "modelador",
+    "pantonic-scout": "scout",
+}
+
+_PAPEIS_POR_TAREFA_DO_ESTADO = {"pantonic-reviewer", "pantonic-consultant"}
+
+_RE_ID_PLANO = re.compile(r"P-\d+")
 
 
 def calcular_consumo(linhas: list[str]) -> tuple[float, int, float]:
@@ -138,6 +160,119 @@ def ler_estado(caminho: Path) -> dict | None:
     return dados
 
 
+def _sufixo_do_papel(agent_type: str) -> str:
+    """Sufixo de identificador do papel: os nomeados de `_SUFIXO_POR_AGENT_TYPE`, ou o nome
+    depois de `pantonic-` para qualquer outro papel do kit."""
+    return _SUFIXO_POR_AGENT_TYPE.get(agent_type, agent_type[len("pantonic-"):])
+
+
+def _primeiro_texto_de_usuario(linhas: list[str]) -> str | None:
+    """Texto (ou concatenação dos blocos `text`) da primeira entrada `type == "user"` do
+    transcript, ou `None` quando não há nenhuma."""
+    for linha in linhas:
+        linha_strip = linha.strip()
+        if not linha_strip:
+            continue
+        try:
+            entrada = json.loads(linha_strip)
+        excep
```
[truncado em 4000 caracteres]

### `tests/test_telemetria_hook.py`
```
diff --git a/tests/test_telemetria_hook.py b/tests/test_telemetria_hook.py
index 9039328..754684c 100644
--- a/tests/test_telemetria_hook.py
+++ b/tests/test_telemetria_hook.py
@@ -42,7 +42,11 @@ def _load_hook():
 
 
 def _linha_assistant(
-    usage: dict | None, timestamp: str, n_tool_uses: int = 0, message_id: str | None = None
+    usage: dict | None,
+    timestamp: str,
+    n_tool_uses: int = 0,
+    message_id: str | None = None,
+    model: str | None = None,
 ) -> str:
     conteudo = [{"type": "text", "text": "ok"}]
     for i in range(n_tool_uses):
@@ -50,9 +54,15 @@ def _linha_assistant(
     mensagem = {"usage": usage or {}, "content": conteudo}
     if message_id is not None:
         mensagem["id"] = message_id
+    if model is not None:
+        mensagem["model"] = model
     return json.dumps({"type": "assistant", "timestamp": timestamp, "message": mensagem})
 
 
+def _linha_user(texto: str, timestamp: str = "2026-09-26T09:00:00+00:00") -> str:
+    return json.dumps({"type": "user", "timestamp": timestamp, "message": {"role": "user", "content": texto}})
+
+
 def _estado_valido(**overrides) -> dict:
     valores = {
         "tarefa": "EXA-T55",
@@ -285,7 +295,7 @@ def test_tf_processar_payload_de_fixture_grava_linha_esperada_no_tsv(tmp_path):
     linhas = tsv_path.read_text(encoding="utf-8").splitlines()
     assert linhas[0] == _HEADER.rstrip("\n")
     assert linhas[1] == "2026-08-19\tPantonicApp\tEXA-T55\tsonnet\t5\t1.0\t0.0\tusage"
-    assert not estado_path.exists()
+    assert estado_path.exists()
 
 
 def test_tr_processar_sem_estado_e_silencio_sem_escrita(tmp_path):
@@ -331,11 +341,11 @@ def test_tr_processar_agent_type_fora_do_filtro_e_silencio_e_preserva_o_estado(t
     assert estado_path.exists()
 
 
-def test_tr_hook_so_executor_consome_estado(tmp_path):
-    """TR (`TK-88b`): `agent_type` `pantonic-reviewer` — outro papel do kit, não o executor —
-    com estado e transcript presentes devolve `False`, sem escrever no TSV e preservando o
-    estado. Concorrente: o filtro antigo (`pantonic-*` por prefixo) processaria este payload,
-    porque `pantonic-reviewer` também começa por `pantonic-`."""
+def test_tf_hook_grava_revisor_com_papel(tmp_path):
+    """TF (`DAF-15`/`DAF-25`): `agent_type` `pantonic-reviewer` grava a própria rodada — tarefa
+    `<tarefa>-revisao` (a do estado corrente) e modelo normalizado do `message.model` do
+    transcript — e o estado permanece no disco (a regra de hoje não gravaria nada, porque
+    filtrava todo papel que não fosse o executor)."""
     hook = _load_hook()
 
     estado_path = tmp_path / "estado" / "tarefa-corrente.json"
@@ -348,6 +358,7 @@ def test_tr_hook_so_executor_consome_estado(tmp_path):
             {"input_tokens": 10, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0, "output_tokens": 0},
             "2026-09-26T10:00:00+00:00",
             n_tool_uses=1,
+            model="claude-opus-4",
         ),
         encoding="utf-8",
     )
@@ -361,11 +372,125 @@ def test_tr_hook_so_executor_consome_estado(tmp_path):
         payload, estado_path=estado_path, telemetria_cli=_TELEMETRIA_CLI_PATH, tsv_path=tsv_path
     )
 
-    assert escreveu is False
-    assert tsv_path.read_text(encoding="utf-8") == _HEADER
+    assert escreveu is True
+    linhas = tsv_path.read_text(encoding="utf-8").splitlines()
+    colunas = linhas[1].split("\t")
+    assert colunas[2] == "EXA-T55-revisao"
+    assert colunas[3] == "opus"
     assert estado_path.exists()
 
 
+def test_tf_hook_grava_consultor_numerado_por_papel(tmp_path):
+    """TF: `pantonic-consultant` numera pela série já existente — com uma linha
+    `EXA-T55-consultor-1` presente, a nova rodada grava `EXA-T55-consultor-2`."""
+    hook = _load_hook()
+
+    estado_path = tmp_path / "estado" / "tarefa-corrente.json"
+    estado_path.parent.mkdir(parents=True)
+    estado_path.write_text(json.dumps(_estado_valido()), encoding="utf-8")
+
+    transcript_path = tmp_path / "consultor-trans
```
[truncado em 4000 caracteres]

### `.claude/tools/encerrar.py`
```
--- .claude/tools/encerrar.py@c0a8e22e48e6a6242972b055f9224ad0c9eb2f5d
+++ .claude/tools/encerrar.py
@@ -669,9 +669,11 @@
 
 def _consumo_do_plano(tsv: Path, plano_id: str, ids: list[str]) -> dict[str, dict[str, float]]:
     """Agregado por papel da série de telemetria: `<ID>` executor, `<ID>-revisao` revisor,
-    `*-consultor-*` consultor, o resto em `outros`. Célula vazia não soma."""
+    `*-consultor-*` consultor, `<P-n>-planejador` planejador, `<P-n>-modelador` modelador,
+    `<P-n>-scout` scout, o resto em `outros`. Célula vazia não soma."""
     grupos: dict[str, dict[str, float]] = {
-        p: {"linhas": 0, "tool_uses": 0, "tokens_k": 0.0} for p in ("executor", "revisor", "consultor", "outros")
+        p: {"linhas": 0, "tool_uses": 0, "tokens_k": 0.0}
+        for p in ("executor", "revisor", "consultor", "planejador", "modelador", "scout", "outros")
     }
     for registro in _ler_tsv(tsv):
         tarefa = registro.get("tarefa", "")
@@ -684,6 +686,12 @@
             papel = "revisor"
         elif "-consultor" in tarefa:
             papel = "consultor"
+        elif tarefa.endswith("-planejador"):
+            papel = "planejador"
+        elif tarefa.endswith("-modelador"):
+            papel = "modelador"
+        elif tarefa.endswith("-scout"):
+            papel = "scout"
         else:
             papel = "outros"
         g = grupos[papel]

```

### `tests/test_encerrar.py`
```
--- tests/test_encerrar.py@c0a8e22e48e6a6242972b055f9224ad0c9eb2f5d
+++ tests/test_encerrar.py
@@ -413,6 +413,28 @@
     (repo / "docs" / "OPERACOES_AS_IS_P-0001.md").write_text("# Operações as-is\n", encoding="utf-8")
 
 
+def test_tf_consumo_por_papel_separa_planejador_modelador_scout(tmp_path):
+    """TF (`DAF-15`/`DAF-25`): a série do plano ganha rodadas de `planejador` e `scout` — papéis
+    que a regra de hoje somaria em `outros`, por não terminarem em `-revisao` nem conterem
+    `-consultor` — e a tabela de consumo da entrega os separa em grupos próprios."""
+    repo = _montar_repo(tmp_path)
+    (repo / "docs" / "telemetria.tsv").write_text(
+        TELEMETRIA
+        + "2026-09-24\trepo\tP-0001-planejador\tsonnet\t3\t12.0\t60.0\tusage\n"
+        + "2026-09-24\trepo\tP-0001-scout\thaiku\t2\t4.0\t20.0\tusage\n",
+        encoding="utf-8",
+    )
+    _fechar_tarefa_e_preparar_plano(repo)
+
+    exit_code = encerrar.main(_argv_plano(repo))
+
+    assert exit_code == 0
+    entrega = (repo / "docs" / "plans" / "_ENTREGA-P-0001.md").read_text(encoding="utf-8")
+    maquina = entrega.split("# Máquina", 1)[1].split("# Histórico", 1)[0]
+    assert "| planejador | 1 | 3 | 12.0 |" in maquina
+    assert "| scout | 1 | 2 | 4.0 |" in maquina
+
+
 def test_tf_plano_fecha_status_entrega_tres_secoes_e_linha_do_diario(tmp_path):
     """TF: o plano sem tarefa aberta fecha num comando — `done` no plano e no índice, relatório
     de entrega nas três seções (tabela das tarefas com o veredito lido do RDO, achados verbatim,

```

### `GOVERNANCA.md`
```
diff --git a/GOVERNANCA.md b/GOVERNANCA.md
index 0fcb95e..9751733 100644
--- a/GOVERNANCA.md
+++ b/GOVERNANCA.md
@@ -652,9 +652,11 @@ também como um kanban adaptado:
   ponto de partida (`git stash create`, ou `git rev-parse HEAD` com a árvore limpa) antes da
   primeira edição e grava a medida do executor (`card_check --gravar`), para a evidência do
   revisor sair com `--desde`. O `.claude/estado/tarefa-corrente.json` se grava só no despacho do
-  executor, e o hook `SubagentStop` só grava a linha do `pantonic-executor`; a rodada de outro
-  papel gravada sob o id da tarefa (caso medido, 2026-09-26: a do revisor da `TK-88a`) sai da
-  série por card corretivo que a cita.
+  executor e vale até o despacho seguinte; o hook `SubagentStop` grava a rodada de todo papel
+  `pantonic-*`, com o papel no identificador da tarefa: `<ID>` do executor, `<ID>-revisao` do
+  revisor, `<ID>-consultor-<n>` do consultor, `<P-n>-planejador`, `<P-n>-modelador` e
+  `<P-n>-scout` pelo primeiro id de plano da primeira mensagem do subagente, e
+  `sem-id-<papel>` quando não há id a derivar.
 
 ### 4.3 Execução em contexto limpo
 

```

### `.claude/skills/scrum-master/SKILL.md`
```
diff --git a/.claude/skills/scrum-master/SKILL.md b/.claude/skills/scrum-master/SKILL.md
index 8f7a247..2c6dabd 100644
--- a/.claude/skills/scrum-master/SKILL.md
+++ b/.claude/skills/scrum-master/SKILL.md
@@ -305,7 +305,7 @@ fronteira do ponto do dono", e não se redecide aqui.
 
 ## Acionamento do consultor
 
-Forma **efêmera com cenário persistido**, em piloto (`docs/plans/P-0747-consultor-de-plano.md` `DCS-6`, `DCS-7`). O consultor não fica de prontidão: a cada escalonamento das regras `A3a`, `A3b`, `A3c`, `A6a`, `A7` e `B1` e do gate do modelo do passo 9, o loop despacha **uma instância nova** do `pantonic-consultant`, com três entradas — o caminho do cenário do plano, `docs/plans/P-<n>-<slug>/cenario.md` (plano legado: `_CENARIO-<plano>.md` em `docs/plans/`); o identificador do card em causa; e a evidência (a linha de retorno do executor, a pendência do laudo ou o stderr do instrumento). A instância lê o cenário e o card, decide, reescreve o cenário com `Edit` mínimo, apensa a linha dela a `docs/ACIONAMENTOS_CONSULTOR.tsv` e devolve `rota=<resolve|modelador|planejador>` — e, só quando classifica o impedimento como estratégico, a linha `estrategico=<uma frase>` logo abaixo (`DCS-27`) —, que o loop roteia pelo passo 8. Nenhuma instância é retomada por `SendMessage` e nenhuma é reprovisionada por limite: o cenário **é** o handover, e a instância que cai se descarta — a `A1` despacha outra, com as mesmas três entradas, sobre o cenário como ficou. Sem o arquivo de cenário na árvore, o primeiro acionamento do plano o cria, com as decisões vivas, a fila, os achados abertos e a matéria inconclusiva, em no máximo 15k tokens. A linha de telemetria de cada instância vem do bloco `<usage>` da notificação, como a de qualquer subagente, com a tarefa `<ID>-consultor-<n>`.
+Forma **efêmera com cenário persistido**, em piloto (`docs/plans/P-0747-consultor-de-plano.md` `DCS-6`, `DCS-7`). O consultor não fica de prontidão: a cada escalonamento das regras `A3a`, `A3b`, `A3c`, `A6a`, `A7` e `B1` e do gate do modelo do passo 9, o loop despacha **uma instância nova** do `pantonic-consultant`, com três entradas — o caminho do cenário do plano, `docs/plans/P-<n>-<slug>/cenario.md` (plano legado: `_CENARIO-<plano>.md` em `docs/plans/`); o identificador do card em causa; e a evidência (a linha de retorno do executor, a pendência do laudo ou o stderr do instrumento). A instância lê o cenário e o card, decide, reescreve o cenário com `Edit` mínimo, apensa a linha dela a `docs/ACIONAMENTOS_CONSULTOR.tsv` e devolve `rota=<resolve|modelador|planejador>` — e, só quando classifica o impedimento como estratégico, a linha `estrategico=<uma frase>` logo abaixo (`DCS-27`) —, que o loop roteia pelo passo 8. Nenhuma instância é retomada por `SendMessage` e nenhuma é reprovisionada por limite: o cenário **é** o handover, e a instância que cai se descarta — a `A1` despacha outra, com as mesmas três entradas, sobre o cenário como ficou. Sem o arquivo de cenário na árvore, o primeiro acionamento do plano o cria, com as decisões vivas, a fila, os achados abertos e a matéria inconclusiva, em no máximo 15k tokens. A linha de telemetria de cada instância é gravada pelo hook `SubagentStop`, com a tarefa `<ID>-consultor-<n>`.
 
 ## Relatório de encerramento
 

```

## Medida do executor
- Arquivo: docs\plans\P-0753-auditoria-estagio-1\evidencia\P-0753-AF-T5-medida.json; mundo: depois; gerado em: 2026-09-27T12:52:34+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_telemetria_hook.py -q -k "papel"` | 0 | true |
| 2 | `python -m pytest tests/test_encerrar.py -q -k "consumo_por_papel"` | 0 | true |
| 3 | `python -c "from pathlib import Path;c=chr(96);t=Path('GOVERNANCA.md').read_text(encoding='utf-8');print(t.count('só grava a linha do '+c+'pantonic-executor'+c),t.count('grava a rodada de todo papel'))"` | 0 | true |
| 4 | `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print(t.count('da notificação, como a de qualquer subagente'))"` | 0 | true |
| 5 | `python -m pytest -q` | 0 | true |
| 6 | `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
