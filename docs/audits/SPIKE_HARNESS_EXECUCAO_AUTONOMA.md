# SPIKE — Harness de Execução Autônoma (EXA-T1)

Medição das três premissas de plataforma do §2 de `docs/plans/P-0734-execucao-autonoma.md`,
antes de qualquer decisão de desenho (`DA-1`, `DA-8`, hooks). Sem proposta de solução — só
medição, com evidência colada.

## Nota de correção

Os vereditos originais das Sondas 1 e 4 (abaixo) foram substituídos por re-medição. A rodada
original usou `context-scout` como cobaia — um agente cujo toolset declarado (`Read, Glob,
Grep`) não inclui `Agent`. O resultado media a definição daquele agente específico, não um
limite de plataforma. Este documento não conta mais a versão anterior como válida.

## Sonda 1 — Aninhamento de subagentes

**Premissa:** subagente não invoca subagente.

**O que foi feito (re-medição):** invocação do subagente `general-purpose` (`Tools: *`)
instruído a (1) escrever um arquivo-marcador no scratchpad e (2) tentar invocar um terceiro
subagente (`context-scout`) pedindo que lesse esse arquivo e colasse o conteúdo — testando
aninhamento em profundidade 3 (contexto principal → `pantonic-executor` → `general-purpose` →
`context-scout`).

**O que foi observado:**

```
PASSO 1: Confirmado — arquivo escrito com sucesso em C:\Users\panta\AppData\Local\Temp\claude\d--workspaces-PantonicApp\dee42d12-df2c-4f01-a6d1-110b7230ee8a\scratchpad\file_lifecycle_probe_slice2.txt

PASSO 2: A invocação funcionou. Resposta literal do context-scout:

PROBE-EXA-T1-SLICE2-b71e4d09: escrito por subagente general-purpose para teste de aninhamento profundidade 3.

(metadados retornados junto: agentId: a453aa7001ed79ef4; usage: subagent_tokens: 8526, tool_uses: 1, duration_ms: 4449)
```

Evidência adicional, já presente no próprio documento antes desta re-medição: o payload colado
na Sonda 3 traz `"agent_type": "pantonic-executor", "agent_id": "ab60045d5947af2de"` —
confirmando que quem executou as três invocações de subagente da rodada original
(`context-scout` nas Sondas 1/4, `pantonic-scout` duas vezes na Sonda 2) já era, ele mesmo, um
subagente.

**Veredito:** `derrubada`. Aninhamento de subagentes ocorre e foi observado funcionando até
profundidade 3 nesta instalação (contexto principal → `pantonic-executor` → `general-purpose`
→ `context-scout`), com sucesso na única tentativa medida — nenhuma falha de profundidade foi
observada nesta amostra. A formulação original ("subagente não invoca subagente") é falsa como
testada; o resultado anterior desta sonda media apenas o toolset restrito de `context-scout`,
não um limite de plataforma.

## Sonda 2 — Sobreposição de modelo por chamada

**Premissa:** o parâmetro `model` da invocação de agente vence o `model:` do arquivo do
agente.

**O que foi feito:** arquivo `.claude/agents/pantonic-scout.md` linha 4 confirma
`model: haiku`. Duas invocações de `pantonic-scout` passando `model` diferente do arquivo:
primeiro `model: "sonnet"` (resposta não teve marcador de auto-identificação de modelo),
depois `model: "opus"`, pedindo à sonda para citar literalmente a frase do próprio system
prompt que declara o modelo em execução.

**O que foi observado:**

```
A frase existe no meu system prompt. Citação literal:

"You are powered by the model named Opus 5. The exact model ID is claude-opus-5."

Observações para a sonda:
- A frase aparece em bloco separado, após as instruções de papel (agente de coleta Pantonic) e antes das notas de ambiente/scratchpad.
- Há duas partes na mesma linha: nome legível ("Opus 5") e ID exato ("claude-opus-5").
- Nenhuma ferramenta foi executada.

Nota de confiabilidade: esse texto é o que minhas instruções de sistema declaram, não uma introspecção do modelo real que atende a requisição — se a plataforma injetar um valor incorreto ou desatualizado, eu reproduzo o valor injetado. Meu conhecimento próprio não me permite confirmar independentemente que "claude-opus-5" é o modelo que está de fato servindo esta chamada.
```

**Veredito:** `confirmada`. Arquivo do agente declara `haiku`; a invocação passou `model:
"opus"`; o system prompt injetado no subagente declara `claude-opus-5`. O parâmetro da
chamada venceu o `model:` do arquivo. Ressalva colada acima: a evidência é o texto que a
plataforma injeta no system prompt do subagente, não uma introspecção independente do
subagente sobre si mesmo — é a mesma classe de evidência que o próprio executor usa para
saber seu modelo (linha "You are powered by..." no system prompt deste agente).

## Sonda 3 — Observabilidade do próprio contexto

**Premissa (fato declarado no plano):** o modelo não enxerga a própria ocupação de contexto;
precisa de proxy. Duas variantes candidatas: (a) hook que meça o transcript e injete aviso,
(b) contador de tarefas por janela calibrado pela série de `docs/telemetria.tsv`. Medir qual
das duas é viável.

**O que foi feito:** inventário dos hooks já configurados em `~/.claude/settings.json`
(amostra real da instalação) e registro temporário de um hook de sonda descartável
(`C:\Users\panta\AppData\Local\Temp\claude\d--workspaces-PantonicApp\dee42d12-df2c-4f01-a6d1-110b7230ee8a\scratchpad\hook_probe.py`)
em `PreToolUse` via `.claude/settings.local.json` local, disparado por um comando `Bash`
trivial (`echo hook-trigger-EXA-T1`), com o payload de stdin gravado em log no scratchpad.
`.claude/settings.local.json` foi apagado ao final da sonda — reversão confirmada por `test -f`
retornando `REVERTED_CONFIRMED`.

**O que foi observado** (payload literal recebido pelo hook `PreToolUse`, campo `raw_stdin`
já parseado):

```json
{"session_id": "dee42d12-df2c-4f01-a6d1-110b7230ee8a", "transcript_path": "C:\\Users\\panta\\.claude\\projects\\d--workspaces-PantonicApp\\dee42d12-df2c-4f01-a6d1-110b7230ee8a.jsonl", "cwd": "d:\\workspaces\\PantonicApp", "prompt_id": "68f5c402-0752-4e94-83c8-eb50a693ee32", "permission_mode": "acceptEdits", "agent_id": "ab60045d5947af2de", "agent_type": "pantonic-executor", "effort": {"level": "high"}, "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "echo hook-trigger-EXA-T1", "description": "Trivial command to trigger PreToolUse hook for probe"}, "tool_use_id": "toolu_01DUTwZ2orJDiSwruUdK5M9w"}
```

Campos presentes: `session_id`, `transcript_path`, `cwd`, `prompt_id`, `permission_mode`,
`agent_id`, `agent_type`, `effort.level`, `hook_event_name`, `tool_name`, `tool_input`,
`tool_use_id`. Nenhum bloco de uso de tokens/contexto (`usage`, `context_window` ou
equivalente) está presente no payload de `PreToolUse`.

**Veredito:** `parcial`. Confirmado que a variante (a) é viável: `PreToolUse` expõe
`transcript_path` — um hook pode ler o arquivo `.jsonl` do transcript nesse caminho e medir
ocupação de contexto por proxy (tamanho/contagem de entradas), sem que o próprio modelo precise
se autoavaliar. Nenhum bloco de uso de tokens vem pronto no payload do hook — a medição via
transcript exigiria parsear o `.jsonl`, não ler um campo direto. A variante (b) — contador de
tarefas por janela calibrado por `docs/telemetria.tsv` — **não foi medida** nesta sonda: não
houve tool use restante no orçamento de 20 para levantar e validar a série de telemetria contra
um calibre real. Fica indefinido se (b) é viável ou preferível a (a); só (a) tem evidência
direta de viabilidade técnica.

## Sonda 4 — Ciclo de vida de arquivo entre agentes

**Premissa:** um arquivo escrito por um subagente é legível por outro subagente da mesma
sessão (premissa de transporte por arquivo da `T2`).

**O que foi feito (re-medição, variante original):** aproveitando a mesma invocação da Sonda
1: o subagente `general-purpose` escreveu
`C:\Users\panta\AppData\Local\Temp\claude\d--workspaces-PantonicApp\dee42d12-df2c-4f01-a6d1-110b7230ee8a\scratchpad\file_lifecycle_probe_slice2.txt`
com marcador único (`PROBE-EXA-T1-SLICE2-b71e4d09`) e, na sequência, invocou o subagente
`context-scout` pedindo que lesse esse arquivo e colasse o conteúdo exato — cenário
subagente-escreve → outro-subagente-lê.

**O que foi observado:** (mesmo payload colado na Sonda 1, PASSO 2) — conteúdo lido por
`context-scout` idêntico ao escrito por `general-purpose`:

```
PROBE-EXA-T1-SLICE2-b71e4d09: escrito por subagente general-purpose para teste de aninhamento profundidade 3.
```

Evidência adicional (variante já medida na rodada anterior, mantida por consistência):
arquivo escrito pelo executor (`file_lifecycle_probe.txt`, marcador `PROBE-EXA-T1-9f3a7c21`)
e lido por `context-scout` com conteúdo idêntico ao escrito.

**Veredito:** `confirmada`. Cenário original produzido: subagente escreve, outro subagente
(invocado pelo primeiro) lê o mesmo arquivo com conteúdo íntegro. A variante
executor-escreve/subagente-lê, medida na rodada anterior, é consistente com o mesmo
resultado.

## Nota de escopo — sonda não completada

A variante (b) da Sonda 3 (contador de tarefas por janela calibrado por `docs/telemetria.tsv`)
não foi medida — orçamento de tool uses da tarefa esgotado antes de levantar a série. Candidato
a tarefa de medição dedicada antes de `T3`/`T13` decidirem entre proxy (a) e (b), caso o plano
ainda considere (b) uma alternativa viva.

## Sonda 5 — Consumo de subagente exposto ao hook `SubagentStop` (EXA-T14)

**Premissa:** se o harness expuser o consumo (tokens, tool uses, duração) de um subagente
encerrado a um hook, `docs/telemetria.tsv` passa a se alimentar sem gastar turno de agente
nenhum. Candidato principal: evento `SubagentStop`.

**O que foi feito:** mesmo método da Sonda 3 — hook de sonda descartável
(`...\scratchpad\hook_probe_subagentstop.py`, grava o `stdin` bruto em log) registrado em
`SubagentStop` via `.claude/settings.local.json` local (arquivo separado do `settings.json`,
fora do materializador). Disparo por uma invocação trivial do subagente `context-scout` pedindo
uma resposta literal fixa, sem uso de ferramenta. `.claude/settings.local.json` apagado ao final
da sonda — reversão confirmada (arquivo inexistente após o apagamento, nenhum outro conteúdo
tocado; não havia `settings.local.json` prévio para preservar).

**O que foi observado** (payload literal recebido pelo hook `SubagentStop`):

```json
{"session_id":"d704fa95-0c60-4238-a159-368dcac15ad2","transcript_path":"C:\\Users\\panta\\.claude\\projects\\d--workspaces-PantonicApp\\d704fa95-0c60-4238-a159-368dcac15ad2.jsonl","cwd":"D:\\workspaces\\PantonicApp","prompt_id":"1f9316b3-c3b6-43a8-b9b5-54d53ab1a708","permission_mode":"acceptEdits","agent_id":"ab9c31787f9afde46","agent_type":"context-scout","hook_event_name":"SubagentStop","stop_hook_active":false,"agent_transcript_path":"C:\\Users\\panta\\.claude\\projects\\d--workspaces-PantonicApp\\d704fa95-0c60-4238-a159-368dcac15ad2\\subagents\\agent-ab9c31787f9afde46.jsonl","last_assistant_message":"PROBE-EXA-T14-SUBAGENTSTOP-ok","background_tasks":[],"session_crons":[]}
```

Campos presentes: `session_id`, `transcript_path`, `cwd`, `prompt_id`, `permission_mode`,
`agent_id`, `agent_type`, `hook_event_name`, `stop_hook_active`, `agent_transcript_path`,
`last_assistant_message`, `background_tasks`, `session_crons`. Nenhum bloco de uso
(`usage`/`tokens`/`tool_uses`/`duration`) vem direto no payload — mas `agent_transcript_path`
aponta para um `.jsonl` **exclusivo do subagente**, que foi lido na mesma sonda e contém, em
cada entrada `type == "assistant"`, um bloco `message.usage` completo (`input_tokens`,
`output_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens`) e `message.model`
(ex.: `"claude-haiku-4-5-20251001"`) — o mesmo padrão de "consumo via parse do transcript" já
usado por `.claude/tools/ocupacao.py` (`T13`) sobre `transcript_path`. `tool_uses` seria contável
por entradas com blocos `tool_use`; `duracao_s`, pela diferença de `timestamp` entre a primeira e
a última entrada. Nada disso, porém, identifica **qual tarefa do plano** (`tarefa` — coluna
obrigatória de `telemetria.py append`, ex. `EXA-T14`) o subagente estava executando: essa
informação não é um campo de schema do harness, só existe como texto livre dentro do prompt que o
orquestrador escreveu (primeira entrada `type == "user"` do `agent_transcript_path`) — inferi-la
exigiria casar regex sobre prosa de prompt, sem contrato do harness por trás, com risco real de
nunca casar (hook nunca escreve nada, automação morta em silêncio) ou de casar errado (linha
gravada com `tarefa` incorreta, corrompendo a série que `GOVERNANCA.md` §4.2 existe para manter
íntegra). `projeto` seria derivável de `cwd` (basename), então não é o mesmo obstáculo.

**Veredito:** `parcial, insuficiente para a automação completa`. O evento `SubagentStop` existe e
expõe, indiretamente (via `agent_transcript_path`, mesma classe de fato que `transcript_path` na
Sonda 3), tokens/modelo/tool-uses/duração do subagente encerrado — mas não expõe, em campo algum
do schema, a identidade da tarefa do plano em execução, que `telemetria.py append --tarefa` exige
como coluna obrigatória. Escrever essa coluna a partir de inferência sobre texto livre do prompt
não é um fato do harness e arrisca corromper a série (pior que não escrever). `T14` mantém o
fluxo vigente da `T7` (chamada explícita de `telemetria.py append` pelo orquestrador, que já tem
a identidade da tarefa em seu próprio estado) — sem pendência aberta.
