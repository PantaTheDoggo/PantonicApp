# Evidência de revisão — DIARIO_DE_OBRAS TK-88b

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
 .claude/tools/backlog.py                           |  549 ++-
 .claude/tools/backlog_hook.py                      |   14 +-
 .claude/tools/card_check.py                        |  403 ++-
 .claude/tools/modelo.py                            |   39 +-
 .claude/tools/rdo.py                               |  284 +-
 .claude/tools/rdo_template.md                      |   12 +-
 .claude/tools/review_evidence.py                   |  166 +-
 .claude/tools/telemetria_hook.py                   |   15 +-
 GOVERNANCA.md                                      |  400 ++-
 README.md                                          |  196 +-
 docs/CUSTO_DO_PICKUP.md                            |  171 +
 docs/DIARIO_DE_OBRAS.md                            | 3702 +++++++++++++++++++-
 docs/DIARIO_HISTORICO.md                           |  154 +
 docs/DOC_MAP.md                                    |  115 +-
 docs/RDO/INDEX.md                                  |  122 +
 docs/RESIDENCIA_DOUTRINA.md                        |    4 +-
 docs/RUBRICA_DE_REVISAO.md                         |   27 +-
 docs/consultant-spec.md                            |   75 +-
 docs/plans/P-0741-modelo-conceitual.md             |    8 +-
 docs/plans/P-0745-planejador-modelo-operacao.md    | 1584 ++++++++-
 docs/plans/_INBOX.md                               |    3 +-
 docs/plans/_INBOX_HISTORICO.md                     |    8 +
 docs/telemetria.tsv                                |  378 ++
 .../backlog/vermelho/docs/DIARIO_DE_OBRAS.md       |    3 +
 tests/fixtures/modelo/fluxo-concluido.md           |   12 +-
 tests/fixtures/modelo/fluxo-pendente.md            |   20 +-
 tests/fixtures/modelo/fluxo-valido.md              |   12 +-
 tests/fixtures/modelo/plano-invalido-2.md          |   10 +-
 tests/fixtures/modelo/plano-invalido.md            |   12 +-
 tests/fixtures/modelo/plano-sem-cabecalho.md       |    8 +-
 tests/fixtures/modelo/plano-sem-estado.md          |    8 +-
 tests/test_backlog.py                              |  799 +++++
 tests/test_card_check.py                           |  208 ++
 tests/test_materializar.py                         |    2 +-
 tests/test_modelo.py                               |  143 +-
 tests/test_rdo.py                                  |  393 ++-
 tests/test_review_evidence.py                      |  265 +-
 tests/test_telemetria_hook.py                      |   35 +
 56 files changed, 10288 insertions(+), 1080 deletions(-)
```

## Arquivos tocados
- `.claude/skills/passagem-de-bastao/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/skills/scrum-master/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/encerrar.py` — atribuição: da entrega; estado git: `??`
- `.claude/tools/rdo.py` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/rdo_template.md` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/telemetria_hook.py` — atribuição: da entrega; estado git: ` M`
- `GOVERNANCA.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88b-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: da entrega; estado git: ` M`
- `tests/test_encerrar.py` — atribuição: da entrega; estado git: `??`
- `tests/test_rdo.py` — atribuição: da entrega; estado git: ` M`
- `tests/test_telemetria_hook.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `57cb445c034a38c10f5f58a2a7103512481683a8`
- Arquivos-alvo declarados: `.claude/tools/encerrar.py`, `.claude/tools/rdo.py`, `.claude/tools/rdo_template.md`, `.claude/tools/telemetria_hook.py`, `docs/telemetria.tsv`, `GOVERNANCA.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `tests/test_encerrar.py`, `tests/test_rdo.py`, `tests/test_telemetria_hook.py`
- Literais não reconhecidos como caminho (12): `fechar_tarefa`, `main`, `--nao-medido`, `tarefa`, `cmd_close`, `close`, `cmd_close`, `--nao-medido`, `**Consumo:**`, `processar`, `TK-88a`, `encerrar.py tarefa`
- Arquivos tocados: `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/encerrar.py`, `.claude/tools/rdo.py`, `.claude/tools/rdo_template.md`, `.claude/tools/telemetria_hook.py`, `GOVERNANCA.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88b-medida.json`, `docs/telemetria.tsv`, `tests/test_encerrar.py`, `tests/test_rdo.py`, `tests/test_telemetria_hook.py`
- Atribuídos a outra tarefa do mesmo plano: `docs/DIARIO_DE_OBRAS.md` → `TK-54b`
- Registro da orquestração (não atribuível a tarefa): `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88b-medida.json`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/encerrar.py`
```
"""TK-88 (`docs/DIARIO_DE_OBRAS.md` `## TK-88`) — o fechamento de tarefa e o de plano deixam de
ser uma sequência de comandos e prosa escrita à mão e passam a ser **um comando cada**, que recebe
a informação da tarefa realizada, escreve os artefatos de fechamento que o kit já tinha e faz os
registros nos documentos de backlog no mesmo ato.

Lugar comum medido (2026-09-26, sobre os fechamentos de `P-0745`..`P-0751`): fechar uma tarefa
eram quatro comandos em turnos separados — `modelo.py check`, `backlog.py status <ID> done`,
`rdo.py close` com o pacote do laudo **redigitado** a partir do arquivo que `rdo.py laudo` já
tinha gravado, e `telemetria.py append` conferindo a linha do hook —, mais o achado `AE-<n>`
editado no plano; fechar um plano era inteiramente manual, porque o instrumento recusava
`ready → done` para plano (registrado no diário em 2026-09-25) e o parágrafo de fechamento, a
linha do índice e a triagem dos achados eram escritos à mão.

Três verbos, todos com as checagens **antes** de qualquer escrita. `tarefa` e `plano` **reportam**
resultado e histórico; `handover` **entrega** — é o que quem vem depois espera da tarefa, de forma
inequívoca, direta e objetiva, inteiramente de máquina, registrado **na própria tarefa**:

``python .claude/tools/encerrar.py handover --plano <caminho.md> --tarefa <ID> --entregue "<o que
existe, com caminho:linha>" --contrato "<com o que a sucessora conta>" [--nao-refazer "<o que já
está pago>"] [--pendente "<o que fica de propósito>"] [--para <ID|papel>]... [--repo] [--data]``

Escreve (ou substitui) o campo `- **Handover:** <data> · para \\`<ID>\\`...` com os sub-bullets
`Entregue`, `Contrato`, `Não refazer` e `Pendente` no card, antes de `- **Notas de execução:**`;
exige entrega na árvore (`in-progress`, `review`, `done` ou `blocked`). A nomenclatura é a
âncora da recuperação: `backlog.py next` (`handovers_para`) devolve, sob `=== HANDOVER DE <ID>`,
junto com a próxima tarefa, o handover de todo irmão que a nomeia em `para` e, na falta, o da
antecessora imediata — o orquestrador cola na delegação o que for pertinente. O `rdo.py close`
transcreve o campo no RDO como extra do card, e `show <ID>` o imprime verbatim.

Os outros dois:

``python .claude/tools/encerrar.py tarefa --plano <caminho.md> --tarefa <ID> [--resumo "<frase>"]
[--pendencia "<uma linha>"] [--achado "<texto>" "<rota>"]... [--laudo <caminho>]
[--tool-uses N --tokens-k K --duracao-s S [--modelo-agente <nome>]] [--progresso <caminho>]
[--rdo-dir <dir>] [--repo <raiz>] [--data AAAA-MM-DD]``

1. a tarefa está em `review` (única transição que produz RDO — skill `diario-de-obras`,
   *Máquina de transições*, gatilho 2); 2. o laudo existe (`<pasta>/laudos/<ID>.md` ou
   `docs/RDO/laudos/<plano>-<ID>.md`) e o pacote é **transcrito** dele — veredito, percentual,
   bloqueante, recomendação, pendência e lições —, nunca redigitado; `reprovado` é recusado
   (`GOVERNANCA.md` §4.2: não é desfecho de RDO); 3. o consumo vem da **fonte única**
   `docs/telemetria.tsv` (última linha da tarefa, gravada pelo hook `SubagentStop`) ou, quando o
   chamador traz o bloco `<usage>` em `--tool-uses/--tokens-k/--duracao-s`, é apensado à série no
   mesmo ato; sem nenhum dos dois o fechamento é recusado — número inventado não fecha tarefa;
   4. `modelo.py check` sai `0` ou `2` (exit `1` mantém a tarefa em `review`, `DMC-30`).
   Passadas as checagens, e nesta ordem: `backlog.transacionar_status(<ID>, done)` com a nota de
   fechamento (bullet do card, índice `done/total`, bloco `Fila corrente`, `estado.tsv`);
   `rdo.cmd_close` em processo, com as seções `# Humano` e `# Histórico` preenchidas — o humano em
   linguagem corrente, com o título da tarefa no lugar da sigla (`GOVERNANCA.md` §4.2, *Mensagem
   legível ao dono*), e o histórico com as linhas que o painel do gerente (`progresso_hook.py`)
   gerou para a tarefa; a linha de telemetria, se o consumo veio por argumento; e cada `--achado`
   como entrada `AE-<n>` com `**Rota:**` em `## Achados
```
[truncado em 4000 caracteres]

### `.claude/tools/rdo.py`
```
diff --git a/.claude/tools/rdo.py b/.claude/tools/rdo.py
index 2b76a80..bd5785d 100644
--- a/.claude/tools/rdo.py
+++ b/.claude/tools/rdo.py
@@ -761,12 +761,28 @@ def _regenerar_indice(rdo_dir: Path) -> Path:
 
 
 def cmd_close(args: argparse.Namespace) -> Path:
-    # Guarda de domínio do consumo (`P-0740` `LM-T1a`, `DM-15` (iii)) — corre antes de qualquer
-    # outra checagem de `cmd_close`, `--plano` incluso: nada é lido nem escrito se um dos três
-    # campos estiver fora do domínio.
-    tool_uses = _validar_inteiro_nao_negativo("tool_uses", args.tool_uses)
-    tokens_k = _validar_numero_nao_negativo_finito("tokens_k", args.tokens_k)
-    duracao_s = _validar_numero_nao_negativo_finito("duracao_s", args.duracao_s)
+    # Guarda de domínio do consumo (`P-0740` `LM-T1a`, `DM-15` (iii); `--nao-medido` na `TK-88b`)
+    # — corre antes de qualquer outra checagem de `cmd_close`, `--plano` incluso: nada é lido nem
+    # escrito se o trio estiver fora do domínio, incompleto, ou junto de `--nao-medido`.
+    trio = (args.tool_uses, args.tokens_k, args.duracao_s)
+    tem_nao_medido = args.nao_medido is not None
+    if tem_nao_medido and any(v is not None for v in trio):
+        raise RdoValidationError("consumo: --tool-uses/--tokens-k/--duracao-s e --nao-medido não vêm juntos")
+    if not tem_nao_medido and any(v is not None for v in trio) and not all(v is not None for v in trio):
+        raise RdoValidationError("consumo: --tool-uses, --tokens-k e --duracao-s vão juntos")
+    if not tem_nao_medido and not all(v is not None for v in trio):
+        raise RdoValidationError("consumo: exige --tool-uses/--tokens-k/--duracao-s ou --nao-medido")
+
+    razao_nao_medido: str | None = None
+    tool_uses = tokens_k = duracao_s = None
+    if tem_nao_medido:
+        razao_nao_medido = args.nao_medido.strip()
+        if not razao_nao_medido or _contar_linhas(args.nao_medido) > 1:
+            raise RdoValidationError("nao_medido: razão é uma linha não vazia")
+    else:
+        tool_uses = _validar_inteiro_nao_negativo("tool_uses", args.tool_uses)
+        tokens_k = _validar_numero_nao_negativo_finito("tokens_k", args.tokens_k)
+        duracao_s = _validar_numero_nao_negativo_finito("duracao_s", args.duracao_s)
 
     plano_path = Path(args.plano)
     if not plano_path.is_file():
@@ -812,10 +828,14 @@ def cmd_close(args: argparse.Namespace) -> Path:
         if valor is not None and _contar_linhas(valor) > 1:
             raise RdoValidationError(f"{nome_campo}: aceita no máximo uma linha")
 
-    # Consumo (`tool_uses`/`tokens_k`/`duracao_s`, validados no topo desta função) é medido e vai
-    # para o documento via TOOL_USES/TOKENS_K/DURACAO_S no `mapping` abaixo — não decide o
-    # desdobramento (`DP-Q`, §21 do `P-0734`).
+    # Consumo (`tool_uses`/`tokens_k`/`duracao_s`, validados no topo desta função, ou a razão de
+    # `--nao-medido`) é medido — ou declarado ausente — e vai para o documento via CONSUMO no
+    # `mapping` abaixo — não decide o desdobramento (`DP-Q`, §21 do `P-0734`).
     desdobramento = calcular_desdobramento(args.veredito)
+    if razao_nao_medido is not None:
+        consumo_texto = f"não medido — {razao_nao_medido}"
+    else:
+        consumo_texto = f"{tool_uses} tool uses, {tokens_k:.1f} k tokens, {duracao_s:.1f} s (fonte: `<usage>` do encerramento)"
 
     linhas_pendencia = []
     if args.pendencia:
@@ -861,9 +881,7 @@ def cmd_close(args: argparse.Namespace) -> Path:
         "PRONTO_QUANDO": dossie.campos["pronto-quando"],
         "DOSSIE_FECHADO_POR": dossie.campos.get("dossie-fechado-por") or "nenhum",
         "EXTRAS": extras_bloco,
-        "TOOL_USES": str(tool_uses),
-        "TOKENS_K": f"{tokens_k:.1f}",
-        "DURACAO_S": f"{duracao_s:.1f}",
+        "CONSUMO": consumo_texto,
         "PENDENCIA": pendencia_final,
         "VEREDITO": args.veredito,
         "PERCENTUAL": str(args.percentual),
@@ -982,17 +1000,23 @@ def main(argv: list[str] | None = None) -> int:
     cl
```
[truncado em 4000 caracteres]

### `.claude/tools/rdo_template.md`
```
diff --git a/.claude/tools/rdo_template.md b/.claude/tools/rdo_template.md
index a112207..690c456 100644
--- a/.claude/tools/rdo_template.md
+++ b/.claude/tools/rdo_template.md
@@ -29,7 +29,7 @@
 
 ## Execução
 
-**Consumo:** {{TOOL_USES}} tool uses, {{TOKENS_K}} k tokens, {{DURACAO_S}} s (fonte: `<usage>` do encerramento)
+**Consumo:** {{CONSUMO}}
 
 **Pendência para o dono:** {{PENDENCIA}}
 

```

### `.claude/tools/telemetria_hook.py`
```
diff --git a/.claude/tools/telemetria_hook.py b/.claude/tools/telemetria_hook.py
index b0d7064..b635aa0 100644
--- a/.claude/tools/telemetria_hook.py
+++ b/.claude/tools/telemetria_hook.py
@@ -19,10 +19,13 @@ de turnos); `tool_uses` = contagem de blocos `type == "tool_use"` no `message.co
 exatamente uma entrada, nunca repetido); `duracao_s` = diferença, em segundos, entre o primeiro e
 o último `timestamp` do transcript.
 
-**Filtro** (`DP-S` `### 23.3` item 4): o hook só age quando `agent_type` é papel do kit —
-convenção de nome `pantonic-*`. Fora do filtro, ou sem estado gravado (despacho fora do loop),
-é silêncio: exit 0, sem escrever nada e **sem consumir o estado** (ele fica para o despacho real
-consumir depois). O estado só é apagado depois de a linha ser escrita com sucesso.
+**Filtro** (`DP-S` `### 23.3` item 4; restrito na `TK-88b`): o hook só age quando `agent_type` é
+`pantonic-executor` — o estado `tarefa-corrente.json` é do despacho do executor
+(`.claude/skills/scrum-master/SKILL.md`, Passo 4), e nenhum outro papel do kit o consome. Fora do
+filtro (inclusive outro papel `pantonic-*`, como `pantonic-reviewer`), ou sem estado gravado
+(despacho fora do loop), é silêncio: exit 0, sem escrever nada e **sem consumir o estado** (ele
+fica para o despacho real consumir depois). O estado só é apagado depois de a linha ser escrita
+com sucesso.
 
 **Cuidado:** este hook é **cliente** do CLI que a `T7` entregou
 (`.claude/tools/telemetria.py append`) — chamado via subprocess, nunca reimplementa validação de
@@ -45,7 +48,7 @@ import subprocess
 import sys
 from pathlib import Path
 
-_AGENT_TYPE_PREFIX_KIT = "pantonic-"  # DP-S §23.3 item 4 — "agent_type é papel do kit"
+_AGENT_TYPE_EXECUTOR = "pantonic-executor"  # TK-88b — só o executor grava/consome o estado
 
 
 def calcular_consumo(linhas: list[str]) -> tuple[float, int, float]:
@@ -164,7 +167,7 @@ def processar(
     `sys.argv`. Devolve `True` quando escreveu (e consumiu o estado), `False` em qualquer ramo de
     silêncio previsto (sem nenhum efeito colateral nesse caso)."""
     agent_type = payload.get("agent_type") or ""
-    if not agent_type.startswith(_AGENT_TYPE_PREFIX_KIT):
+    if agent_type != _AGENT_TYPE_EXECUTOR:
         return False
 
     estado = ler_estado(estado_path)

```

### `docs/telemetria.tsv`
```
diff --git a/docs/telemetria.tsv b/docs/telemetria.tsv
index dd139a2..50b71b3 100644
--- a/docs/telemetria.tsv
+++ b/docs/telemetria.tsv
@@ -903,10 +903,10 @@ data	projeto	tarefa	modelo	tool_uses	tokens_k	duracao_s	fonte
 2026-09-26	PantonicApp	P-0752-consultor-11	opus	62	143.5	621.8	usage
 2026-09-26	PantonicApp	TK-91a	sonnet	9	52.1	72.8	usage
 2026-09-26	PantonicApp	TK-91a-revisao	opus	24	70.2	126.6	usage
-2026-09-26	PantonicApp	TK-88a	opus	60	186.4	464.1	usage
 2026-09-26	PantonicApp	TK-88a-revisao	opus	60	186.4	464.3	usage
 2026-09-26	PantonicApp	TK-86a-consultor-1	opus	14	53.9	286.4	usage
 2026-09-26	PantonicApp	TK-86a	sonnet	20	56.1	208.0	usage
 2026-09-26	PantonicApp	TK-86a-revisao	opus	24	67.4	204.0	usage
 2026-09-26	PantonicApp	TK-86a-consultor-2	opus	61	147.6	1681.0	usage
 2026-09-26	PantonicApp	TK-87a	sonnet	28	74.0	302.2	usage
+2026-09-26	PantonicApp	TK-88b	sonnet	74	170.8	679.3	usage

```

### `GOVERNANCA.md`
```
diff --git a/GOVERNANCA.md b/GOVERNANCA.md
index 1513acd..3acd43b 100644
--- a/GOVERNANCA.md
+++ b/GOVERNANCA.md
@@ -631,6 +631,17 @@ também como um kanban adaptado:
   desta regra ficam como estão: são registro histórico, já espelhado na série. **`contado` exige
   contagem efetiva** — chamadas contadas no transcript, não estimadas de memória; contagem não
   feita entra como `nao_medido` (caso medido, 2026-09-16: `contado` = 14 contra 29 reais).
+  **Tarefa sem medida fecha declarando a ausência:** tarefa sem `<usage>` — executada na sessão
+  principal, fora do loop — fecha com `encerrar.py tarefa --nao-medido "<razão>"`, que apensa à
+  série a linha `nao_medido` com as células de consumo vazias e escreve no RDO "não medido —
+  <razão>"; número estimado nunca entra, e medida existente não se descarta (o instrumento recusa
+  `--nao-medido` quando a série já mede a tarefa). Quem executa fora do loop captura a ref do
+  ponto de partida (`git stash create`, ou `git rev-parse HEAD` com a árvore limpa) antes da
+  primeira edição e grava a medida do executor (`card_check --gravar`), para a evidência do
+  revisor sair com `--desde`. O `.claude/estado/tarefa-corrente.json` se grava só no despacho do
+  executor, e o hook `SubagentStop` só grava a linha do `pantonic-executor`; a rodada de outro
+  papel gravada sob o id da tarefa (caso medido, 2026-09-26: a do revisor da `TK-88a`) sai da
+  série por card corretivo que a cita.
 
 ### 4.3 Execução em contexto limpo
 

```

### `.claude/skills/scrum-master/SKILL.md`
```
diff --git a/.claude/skills/scrum-master/SKILL.md b/.claude/skills/scrum-master/SKILL.md
index d48e2fa..985a3cb 100644
--- a/.claude/skills/scrum-master/SKILL.md
+++ b/.claude/skills/scrum-master/SKILL.md
@@ -199,7 +199,7 @@ Dez passos, nesta ordem.
     [--resumo "<uma frase em linguagem corrente, para o dono>"] \
     [--pendencia "<pendência autoral do executor>"] \
     [--achado "<texto>" "<rota>"]... \
-    [--tool-uses <N> --tokens-k <tokens_k> --duracao-s <N>]
+    [--tool-uses <N> --tokens-k <tokens_k> --duracao-s <N> | --nao-medido "<razão>"]
   ```
 
   Ele faz, nesta ordem e só depois de todas as checagens passarem: (1) o **gate do modelo** —
@@ -217,7 +217,9 @@ Dez passos, nesta ordem.
   `docs/telemetria.tsv` que o hook `SubagentStop` gravou — a fonte única —, ou, quando o loop traz
   o bloco `<usage>` da notificação em `--tool-uses/--tokens-k/--duracao-s`, apensa essa linha à
   série no mesmo ato (`--fonte usage`); sem nenhum dos dois o instrumento **recusa** — número
-  inventado não fecha tarefa. Quando o hook gravou valor que diverge do `<usage>` (`AE-3`), o loop
+  inventado não fecha tarefa. Tarefa sem `<usage>` — executada fora do loop — fecha com
+  `--nao-medido "<razão>"` (`GOVERNANCA.md` §4.2): a série registra a ausência, nunca um número.
+  Quando o hook gravou valor que diverge do `<usage>` (`AE-3`), o loop
   passa o trio conferido, e a linha do hook fica na série como está. O hook **não dispara** quando
   um subagente é retomado por `SendMessage` — a retomada do executor pela `A1` — e nesse caso o
   trio vem sempre por argumento; o consultor nunca é retomado (seção *Acionamento do consultor*);

```

### `.claude/skills/passagem-de-bastao/SKILL.md`
```
diff --git a/.claude/skills/passagem-de-bastao/SKILL.md b/.claude/skills/passagem-de-bastao/SKILL.md
index 7d372bc..4f913aa 100644
--- a/.claude/skills/passagem-de-bastao/SKILL.md
+++ b/.claude/skills/passagem-de-bastao/SKILL.md
@@ -184,7 +184,8 @@ Recusa de qualquer item do gate: **não delega**, e o que falta fechar volta ao
    pelo trio `--tool-uses/--tokens-k/--duracao-s` do `encerrar.py tarefa`, lido do bloco `<usage>`
    da notificação (`--fonte usage`); fora do instrumento, `.claude/tools/telemetria.py append`
    (`--fonte contado` na execução inline sem `<usage>` — contagem efetiva das chamadas no
-   transcript, nunca estimativa; sem contagem, `nao_medido`). No registro vai o ponteiro
+   transcript, nunca estimativa; sem contagem, `nao_medido`); no fechamento, `encerrar.py tarefa
+   --nao-medido "<razão>"`. No registro vai o ponteiro
    `Consumo: ver docs/telemetria.tsv` — **nunca o número em prosa** (`GOVERNANCA.md` §4.2, fonte
    única). Read offset/limit da região do bullet → Edit; NUNCA Edit apoiado em Read anterior à
    chamada `Agent` (o hiato de delegação invalida o rastreio). No pickup, 1 Grep pelo texto-promessa:

```

### `tests/test_encerrar.py`
```
"""TK-88 (`docs/DIARIO_DE_OBRAS.md` `## TK-88`) — TF/TR de `.claude/tools/encerrar.py`, o
instrumento de fechamento de tarefa e de plano. Repositório sintético em `tmp_path` com diário,
plano legado, laudo, série de telemetria e painel do gerente; nenhum teste toca a árvore real.
Padrão de carga por caminho igual ao de `tests/test_backlog.py` (`.claude/` não é pacote)."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
_ENCERRAR_PATH = _ROOT / ".claude" / "tools" / "encerrar.py"


def _load_encerrar():
    spec = importlib.util.spec_from_file_location("encerrar", _ENCERRAR_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


encerrar = _load_encerrar()

TITULO_T1 = "Primeira tarefa do plano"
TITULO_T2 = "Segunda tarefa, cancelada"
TITULO_PLANO = "Plano alfa"

DIARIO = (
    "# Diário de Obras — Teste\n"
    "**Diretiva de priorização:** Priorize `P-0001`.\n"
    "\n"
    "<!-- fila:gerada -->\n"
    "**Fila corrente:** —\n"
    "<!-- /fila:gerada -->\n"
    "\n"
    "## Índice\n"
    "\n"
    "| ID | Título | Status | Âncora |\n"
    "|---|---|---|---|\n"
    "| P-0001 | Plano alfa | ready 0/1 | docs/plans/P-0001-alfa.md |\n"
)

PLANO = (
    f"# P-0001 — {TITULO_PLANO}\n"
    "\n"
    "**Status:** `ready` · **Prefixo das tarefas no diário:** `ALF-T<n>`\n"
    "\n"
    "## 5. Tarefas\n"
    "\n"
    f"### ALF-T1 — {TITULO_T1} [Sonnet · classe implementacao]\n"
    "- **Status:** `{status_t1}` · 2026-09-20\n"
    "- **Objetivo:** entregar a primeira coisa.\n"
    "- **Arquivos-alvo:** `a.py`.\n"
    "- **Verificação:** `pytest -q`.\n"
    "- **Pronto quando:** o teste passa.\n"
    "\n"
    f"### ALF-T2 — {TITULO_T2} [Sonnet · classe implementacao]\n"
    "- **Status:** `cancelled` · 2026-09-20 · absorvida\n"
    "- **Objetivo:** nada.\n"
    "- **Arquivos-alvo:** `b.py`.\n"
    "- **Verificação:** nenhuma.\n"
    "- **Pronto quando:** nunca.\n"
    "\n"
    "## 8. Achados da execução\n"
    "\n"
    "- **AE-1** (`ALF-T1`, laudo, 2026-09-21) — achado antigo. **Rota:** registrado, sem ação.\n"
)

LAUDO = (
    "# Laudo — P-0001 · ALF-T1\n"
    "\n"
    "**Percentual:** 91%\n"
    "**Veredito:** ressalva\n"
    "**Dimensão bloqueante:** nenhuma\n"
    "**Recomendação:** seguir com ressalva\n"
    "**Pendência:** o teste novo não cobre o ramo vazio\n"
    "\n"
    "## Lições aprendidas na tarefa\n"
    "\n"
    "Observação qualitativa do revisor.\n"
)

TELEMETRIA = (
    "data\tprojeto\ttarefa\tmodelo\ttool_uses\ttokens_k\tduracao_s\tfonte\n"
    "2026-09-25\trepo\tALF-T1\tsonnet\t21\t77.5\t300.2\tusage\n"
    "2026-09-25\trepo\tALF-T1-revisao\topus\t9\t40.0\t120.0\tusage\n"
)

PAINEL = (
    f'Abrindo a janela do plano "{TITULO_PLANO}".\n'
    f'Tarefa "{TITULO_T1}". Passo: conferir os gates e preparar o despacho.\n'
    'Tarefa "Outra coisa de outro plano". Passo: conferir os gates e preparar o despacho.\n'
    f'Agente revisor devolveu a tarefa "{TITULO_T1}": ressalva 91%, bloqueante nenhuma.\n'
)


def _montar_repo(tmp_path: Path, status_t1: str = "review") -> Path:
    repo = tmp_path / "repo"
    (repo / "docs" / "plans").mkdir(parents=True)
    (repo / "docs" / "RDO" / "laudos").mkdir(parents=True)
    (repo / ".claude" / "estado").mkdir(parents=True)
    (repo / "docs" / "DIARIO_DE_OBRAS.md").write_text(DIARIO, encoding="utf-8")
    (repo / "docs" / "plans" / "P-0001-alfa.md").write_text(PLANO.format(status_t1=status_t1), encoding="utf-8")
    (repo / "docs" / "plans" / "_INBOX.md").write_text("**Próximo id de plano: P-0002.**\n", encoding="utf-8")
    (repo / "docs" / "RDO" / "laudos" / "P-0001-ALF-T1.md").write_text(LAUDO, encoding="utf-8")
    (repo / "docs" / "telemetria.tsv").write_text(TELEMETRIA, encoding="utf-8")
    (repo / ".claude" / "estado" / "progresso.txt").write_text(PAINEL, encoding="utf-8")
    return repo

```
[truncado em 4000 caracteres]

### `tests/test_rdo.py`
```
diff --git a/tests/test_rdo.py b/tests/test_rdo.py
index 2dbbb16..25c8091 100644
--- a/tests/test_rdo.py
+++ b/tests/test_rdo.py
@@ -387,6 +387,42 @@ def test_tf_close_tokens_k_decimal_grava_sem_conversao(tmp_path):
     assert "203.7" in conteudo
 
 
+def test_tf_close_nao_medido_sem_trio(tmp_path):
+    """TF (`TK-88b`): `--nao-medido "<razão>"` no lugar do trio de consumo grava o RDO com
+    `**Consumo:** não medido — <razão>`, sem nenhum número de consumo no documento."""
+    rdo = _load_rdo()
+
+    exit_code = rdo.main(
+        _argv_close(
+            tmp_path,
+            omit=("--tool-uses", "--tokens-k", "--duracao-s"),
+            **{"--nao-medido": "executada fora do loop, sem <usage>"},
+        )
+    )
+
+    assert exit_code == 0
+    gerados = [p for p in tmp_path.glob("*.md") if p.name != "INDEX.md"]
+    assert len(gerados) == 1
+    conteudo = gerados[0].read_text(encoding="utf-8")
+    assert "**Consumo:** não medido — executada fora do loop, sem <usage>" in conteudo
+    assert "tool uses" not in conteudo
+    assert "{{" not in conteudo
+
+
+def test_tr_close_sem_trio_nem_nao_medido_recusa(tmp_path, capsys):
+    """TR (`TK-88b`): sem o trio de consumo e sem `--nao-medido`, `cmd_close` recusa (exit != 0)
+    antes de escrever qualquer coisa — exatamente um dos dois é exigido."""
+    rdo = _load_rdo()
+
+    exit_code = rdo.main(
+        _argv_close(tmp_path, omit=("--tool-uses", "--tokens-k", "--duracao-s"))
+    )
+
+    assert exit_code == 1
+    assert "exige --tool-uses/--tokens-k/--duracao-s ou --nao-medido" in capsys.readouterr().err
+    assert [p for p in tmp_path.glob("*.md")] == []
+
+
 def test_tr_close_tokens_k_inteiro_grava_uma_casa_decimal_sempre(tmp_path):
     """TR (`DM-11`): `--tokens-k 80` grava `80.0` — uma casa decimal sempre, o que discrimina da
     regra concorrente `str(int)`, que daria `80` sem o `.0`."""

```

### `tests/test_telemetria_hook.py`
```
diff --git a/tests/test_telemetria_hook.py b/tests/test_telemetria_hook.py
index 958b077..9039328 100644
--- a/tests/test_telemetria_hook.py
+++ b/tests/test_telemetria_hook.py
@@ -331,6 +331,41 @@ def test_tr_processar_agent_type_fora_do_filtro_e_silencio_e_preserva_o_estado(t
     assert estado_path.exists()
 
 
+def test_tr_hook_so_executor_consome_estado(tmp_path):
+    """TR (`TK-88b`): `agent_type` `pantonic-reviewer` — outro papel do kit, não o executor —
+    com estado e transcript presentes devolve `False`, sem escrever no TSV e preservando o
+    estado. Concorrente: o filtro antigo (`pantonic-*` por prefixo) processaria este payload,
+    porque `pantonic-reviewer` também começa por `pantonic-`."""
+    hook = _load_hook()
+
+    estado_path = tmp_path / "estado" / "tarefa-corrente.json"
+    estado_path.parent.mkdir(parents=True)
+    estado_path.write_text(json.dumps(_estado_valido()), encoding="utf-8")
+
+    transcript_path = tmp_path / "reviewer-transcript.jsonl"
+    transcript_path.write_text(
+        _linha_assistant(
+            {"input_tokens": 10, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0, "output_tokens": 0},
+            "2026-09-26T10:00:00+00:00",
+            n_tool_uses=1,
+        ),
+        encoding="utf-8",
+    )
+
+    tsv_path = tmp_path / "telemetria.tsv"
+    tsv_path.write_text(_HEADER, encoding="utf-8")
+
+    payload = _payload(agent_type="pantonic-reviewer", agent_transcript_path=str(transcript_path))
+
+    escreveu = hook.processar(
+        payload, estado_path=estado_path, telemetria_cli=_TELEMETRIA_CLI_PATH, tsv_path=tsv_path
+    )
+
+    assert escreveu is False
+    assert tsv_path.read_text(encoding="utf-8") == _HEADER
+    assert estado_path.exists()
+
+
 def test_tf_hook_executavel_stdin_utf8_nao_falha_e_preserva_invariancia(tmp_path):
     """TK-56b: repara a ressalva da `TK-56a` — o par negativo deixa de ser um stub (que só
     discriminava a si mesmo) e passa a ser o produto revertido, extraído do arquivo real. Mundo

```

## Medida do executor
- Arquivo: docs\RDO\evidencia\DIARIO_DE_OBRAS-TK-88b-medida.json; mundo: depois; gerado em: 2026-09-27T00:34:31+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_encerrar.py tests/test_rdo.py tests/test_telemetria_hook.py -q -k "nao_medido or so_executor"` | 0 | true |
| 2 | `python -c "from pathlib import Path;print(sum(1 for l in Path('docs/telemetria.tsv').read_text(encoding='utf-8').splitlines() if l.split(chr(9))[2:3]==['TK-88a'] and l.endswith(chr(9)+'usage')))"` | 0 | true |
| 3 | `python -c "from pathlib import Path;print(all('--nao-medido' in Path(f).read_text(encoding='utf-8') for f in ('GOVERNANCA.md','.claude/skills/scrum-master/SKILL.md','.claude/tools/encerrar.py','.claude/tools/rdo.py')))"` | 0 | true |
| 4 | `python -m pytest -q` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
