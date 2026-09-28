# Evidência de revisão — DIARIO_DE_OBRAS TK-54b

## Diff (`git diff --stat`)
```
docs/CUSTO_DO_PICKUP.md        | 113 +++++++++++++++++++++++++++++++++++++++++
 docs/DIARIO_DE_OBRAS.md        |  78 +++++++++++++++++++++++++---
 docs/DOC_MAP.md                |   7 ++-
 docs/plans/_INBOX.md           |   1 -
 docs/plans/_INBOX_HISTORICO.md |   1 +
 docs/telemetria.tsv            |   1 +
 6 files changed, 192 insertions(+), 9 deletions(-)
```

## Arquivos tocados
- `docs/CUSTO_DO_PICKUP.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: da entrega; estado git: ` M`
- `docs/DOC_MAP.md` — atribuição: da entrega; estado git: ` M`
- `docs/RDO/evidencia/TK-54-TK-54b.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_INBOX.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/_INBOX_HISTORICO.md` — atribuição: alheio; estado git: ` M`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `d75e7a656fe73d398263dde88dce8f29535d8dcb`
- Arquivos-alvo declarados: `docs/CUSTO_DO_PICKUP.md`, `docs/DOC_MAP.md`, `docs/DIARIO_DE_OBRAS.md`
- Literais não reconhecidos como caminho (2): `Status`, `## TK-54`
- Arquivos tocados: `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/DOC_MAP.md`, `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/RDO/evidencia/TK-54-TK-54b.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `docs/CUSTO_DO_PICKUP.md`
```
diff --git a/docs/CUSTO_DO_PICKUP.md b/docs/CUSTO_DO_PICKUP.md
index 28378ff..53c89fb 100644
--- a/docs/CUSTO_DO_PICKUP.md
+++ b/docs/CUSTO_DO_PICKUP.md
@@ -516,3 +516,116 @@ requisição desta sessão. Esse item fica **a apurar** antes de qualquer republ
 3. **Todo número publicado nomeia o objeto medido.** "16.459 bytes de `additionalContext`" era o
    comprimento da linha do JSONL. Comprimento de registro, de texto renderizado e de texto-fonte
    são três objetos; o rótulo diz qual.
+
+## 16 A fonte da bimodalidade (2026-09-21, TK-54b)
+
+Sonda `sonda_tk54b.py` (scratchpad, descartável, stdlib, fora do repo — mesmo método da `## 12`
+e da `## 13`). Corpus: `C:\Users\panta\.claude\projects\` inteiro, janelas principais
+(`*.jsonl` na raiz de cada diretório de projeto). Fórmula: `usage_1 = input_tokens +
+cache_creation_input_tokens + cache_read_input_tokens` da 1ª entrada `assistant`.
+
+**Gate — PASS.** As quatro canônicas reproduzidas exatamente: `08a29a54`=34.260, `a7432333`=34.292,
+`29dd40a9`=45.872, `95db6421`=46.071.
+
+**Corpus:** 303 janelas principais, 302 com `usage` observável (1 descartada, `usage` zerado).
+
+**Partição pelo valor discreto de `cache_read` (18 valores distintos no corpus):**
+
+| `cache_read` | n | `usage_1` mediana | `deferred_tools_delta` n_names (conjunto) | chars (conjunto) |
+|---|---|---|---|---|
+| 0 | 36 | 52.584 | {17, 18, 25} | {182, 191, 194, 449} |
+| 14.721 | 4 | 37.194 | {25} | {449} |
+| 18.012 | 3 | 35.810 | {25} | {449} |
+| **18.084** | **120** | 38.285 | **{18}** | **{191}** |
+| 18.866 | 1 | 36.262 | {25} | {449} |
+| 26.691 | 5 | 45.999 | {18} | {191} |
+| **26.695** | **74** | 50.034 | **{18}** | **{191}** |
+| 29.946 | 11 | 49.518 | {17, 18} | {182, 194} |
+| 31.429 | 2 | 52.681 | {17} | {182} |
+| 33.224 | 2 | 59.243 | {25} | {449} |
+| 33.237 | 10 | 49.042 | {17} | {182} |
+| 33.238 | 1 | 54.547 | {17} | {182} |
+| 34.091 | 3 | 50.475 | {17} | {182} |
+| 36.516 | 2 | 59.199 | {25} | {449} |
+| 36.737 | 4 | 64.390 | {17} | {182} |
+| 38.671 | 2 | 66.062 | {17} | {182} |
+| 42.702 | 9 | 64.066 | {17, 18} | {182, 194} |
+| 44.340 | 13 | 61.074 | {17} | {182} |
+
+O par nomeado pela `## 12` — `cache_read` 18.084 (n=120) vs 26.695 (n=74), Δ **8.611 tok** — tem o
+**mesmo** conjunto de `deferred_tools_delta`: 18 nomes, 191 chars, lista idêntica
+(`CronCreate, CronDelete, CronList, DesignSync, EnterPlanMode, EnterWorktree, ExitPlanMode,
+ExitWorktree, Monitor, NotebookEdit, PushNotification, RemoteTrigger, SendMessage, TaskOutput,
+TaskStop, TodoWrite, WebFetch, WebSearch`) nos dois grupos.
+
+**Comparação completa do par nomeado — todo anexo (`attachment`) observável antes da 1ª resposta,
+nos dois grupos:**
+
+| atributo | `cache_read`=18.084 (n=120) | `cache_read`=26.695 (n=74) | separa o par? |
+|---|---|---|---|
+| `version` (harness) | `{2.1.220}` | `{2.1.220}` | não — idêntico |
+| `deferred_tools_delta` chars | `{191}` | `{191}` | não — idêntico |
+| `agent_listing_delta` chars | `{231, 240}` | `{218, 231, 240}` | não — sobreposto |
+| `hook_system_message` chars | `{128, 129}` | `{128, 129}` | não — sobreposto |
+| `hook_additional_context` chars | `{213, 220}` | `{213, 220}` | não — sobreposto |
+| `skill_listing` chars | `{8.496, 11.113}` | `{8.496, 9.371, 11.113}` | não — sobreposto (os dois extremos ocorrem nos dois grupos) |
+| `auto_mode` (presença) | ausente (0/120) | 8/74 | não — presente só numa fração do grupo `26.695`, que é 100% constante em `cache_read`; não pode explicar um valor discreto uniforme |
+
+Nenhum atributo observável nos anexos do primeiro request particiona o par 18.084/26.695. O teto de
+explicação medida, para qualquer atributo correlacionado com o regime, é **0 chars**.
+
+**Aritmética (decisão 1 do escopamento — medir em chars, conversão só como faixa declarada):** o
+candidato *deferred tools* explica **0 chars / 0 tok** do Δ de 8.611 tok exigido — não bate nem em
+ordem de grandeza, porque o conteúdo é byte-idêntico nos dois grupos. **Ca
```
[truncado em 4000 caracteres]

### `docs/DOC_MAP.md`
```
diff --git a/docs/DOC_MAP.md b/docs/DOC_MAP.md
index 8f241b5..b425438 100644
--- a/docs/DOC_MAP.md
+++ b/docs/DOC_MAP.md
@@ -101,7 +101,7 @@ caso de uso de um plugin, ou o grau de aderência medido da implementação de r
 **Acesso:** `Grep pattern:"^### 9\.1" path:ARQUITETURA_PANTONICA.md -n` (trocar a âncora por
 qualquer heading `##`/`###` da lista acima).
 
-## docs/CUSTO_DO_PICKUP.md (~431 linhas)
+## docs/CUSTO_DO_PICKUP.md (~631 linhas)
 **Propósito:** medida por fonte do que uma retomada de backlog ingere — orçamento em chars e
 tokens, veredito das hipóteses, rota candidata por fonte, orçamento-alvo e anatomia medida de
 uma janela de orquestração real.
@@ -134,6 +134,11 @@ medido em vez de remedir; e para o valor de referência contra o qual uma corre
   metade em chars (26.760) e a metade `usage_1` (39.650 tk) medidas, o par do `DC-4` **aberto** à
   espera de controle pareado, com proveniência de sessão, a linha de base do dia e a correção do
   que a `## 14` afirmava sobre a observabilidade do número
+- `## 16 A fonte da bimodalidade (2026-09-21, TK-54b)` — gate PASS das quatro canônicas, partição
+  do corpus por `cache_read` discreto, candidato *deferred tools* descartado por medida direta
+  (byte-idêntico no par 18.084/26.695), cinco suspeitos adicionais descartados, veredito `não
+  identificada` com o achado de que `system`/`tools` do request não são logados em nenhuma versão
+  do transcript
 **Acesso:** `Grep pattern:"^## 5 " path:docs/CUSTO_DO_PICKUP.md -n` (trocar `5` pela seção
 desejada).
 

```

### `docs/DIARIO_DE_OBRAS.md`
```
diff --git a/docs/DIARIO_DE_OBRAS.md b/docs/DIARIO_DE_OBRAS.md
index ce9cd22..0e49b0f 100644
--- a/docs/DIARIO_DE_OBRAS.md
+++ b/docs/DIARIO_DE_OBRAS.md
@@ -2,11 +2,11 @@
 
 **Diretiva de priorização:** sem alvo fixo — a priorização volta a ser do agente (default), porque o alvo fixado foi entregue. O `P-0743` foi **aceito pelo dono em 2026-09-21**, fechou `done` 18/18, e a entrega validada está em `docs/Entregas Aceitas/Entregas - P-0743.md` — o as-is saiu de `docs/OPERACOES_AS_IS.md`, que volta a ficar livre para o próximo plano a produzir um. Fila viva: `TK-54`, `P-0741` (`MC-T5` em `review`), `TK-65`, `TK-66`, `TK-55`, `TK-67`, `TK-68`; o `P-0744` foi a `superseded` em 2026-09-21, substituído pelo `P-0745`, que nasce `blocked` aguardando o `go` do dono no Marco 1 e por isso não é elegível. Oito pendências do `P-0743` estão listadas na entrega aceita, três delas com efeito fora daquele plano.
 <!-- fila:gerada -->
-**Fila corrente:** `TK-54` — Extrato do custo de abertura de uma janela principal (`docs/DIARIO_DE_OBRAS.md:1286-1770`) · fila: — · ready 15 · blocked 0 · in-progress 0
-- `TK-54` (`ready`, 1/2): próxima `TK-54b`
+**Fila corrente:** `TK-65` — Três defeitos medidos de `backlog.py` na abertura da janela do `P-0741` (`docs/DIARIO_DE_OBRAS.md:2715-2789`) · fila: — · ready 18 · blocked 0 · in-progress 0
+- `TK-54` (`ready`, 1/2): próxima —
 - `P-0741` (`ready`, 7/8): próxima —
 - `TK-65` (`ready`, 0/3): próxima `TK-65a`
-- `P-0744` (`blocked`, 0/3): próxima —
+- `P-0745` (`blocked`, 0/7): próxima —
 <!-- /fila:gerada -->
 
 > **⏹ Os quatro blocos de diretiva abaixo são HISTÓRICO — o `P-0743` fechou `done` 18/18 e foi
@@ -190,7 +190,7 @@ da resposta.
 | TK-38 | **Comunicação entre agente e humano — skill própria e requisitos mínimos.** Aberto por decisão do dono em 2026-08-13. O framework nomeia objetos de projeto por prefixo abreviado (`DP-`, `DR-`,… | ready | docs/DIARIO_DE_OBRAS.md#tk-38--comunicação-entre-agente-e-humano--skill-própria-e-requisitos-mínimos |
 | TK-48 | `~/.claude/settings.json` **perdeu a chave `hooks` inteira silenciosamente**, sem ação intencional do dono, entre a `RPC-T4` e a escolha da `RPC-T5` — os 4 hooks registrados (premissa da `T5`) somem sem rastro. | ready | docs/DIARIO_DE_OBRAS.md#tk-48--~/claude/settingsjson-perdeu-a-chave-hooks-inteira-silenciosamente |
 | TK-53 | O que mudou no corte da `95db6421…` que desloca o custo opaco de abertura de janela para as 6 janelas pós-corte inteiras (mediana 46.070 vs. 34.347 do grupo `antes`) — decisão do dono em 2026-08-24 sobre o achado do `TK-51`, causa ainda não investigada. Bloqueia `P-0737`. | done *(**desfecho negativo, decisão do dono em 2026-08-31** — a `TK-53a` mediu que não há degrau no corte: os dois regimes (`cache_read` 18.084 e 26.695) coexistem **antes e depois** dele, então a causa procurada não existe. `TK-53b` **cancelada por absorção** (seu insumo único, o bracket temporal, perdeu o objeto). A pergunta viva migrou para `TK-54`: não *o que mudou*, mas *do que o custo é feito*)* | docs/DIARIO_DE_OBRAS.md#tk-53--causa-do-deslocamento-de-custo-nas-janelas-pós-corte |
-| TK-54 | **Extrato do custo de abertura de uma janela principal.** O 1º `usage` decompõe-se em uma linha por fonte carregada, com tamanho medido, origem (nossa ou do harness) e classificação em *válido / necessário / dispensável / economizável* — o detalhamento sem o qual o dono não decide corte nenhum. Substitui o objetivo morto da `TK-53`. Bloqueia `P-0737`. | ready | docs/DIARIO_DE_OBRAS.md#tk-54--extrato-do-custo-de-abertura-de-uma-janela-principal |
+| TK-54 | **Extrato do custo de abertura de uma janela principal.** O 1º `usage` decompõe-se em uma linha por fonte carregada, com tamanho medido, origem (nossa ou do harness) e classificação em *válido / necessário / dispensável / economizável* — o detalhamento sem o qual o dono não decide corte nenhum. Substitui o objetivo morto da `TK-53`. Bloqueia `P-0737`. | ready 1/2 | docs/DIARIO_DE_OBRAS.md#tk-54--extrato-do-cu
```
[truncado em 4000 caracteres]

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
