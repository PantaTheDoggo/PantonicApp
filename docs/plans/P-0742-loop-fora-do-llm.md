# P-0742 — O loop sai do LLM

**Data:** 2026-09-19 · **Origem:** decisão de rota do dono, 2026-09-19, sobre a posição L8 de
`docs/plans/_VIABILIDADE-agente-leitor.md` §7.4 · **Status:** `blocked` · 2026-09-19 · depende de
`P-0739` `done`: o driver consome os verbos de `backlog.py` (`next`, `start`, `status`, `show`) que
o `P-0739` está migrando; retomar quando o índice do diário marcar `P-0739` `done` ·
**Prefixo das tarefas no diário:** `LF-T<n>` · **Prefixo das decisões:** `DLF-<n>` ·
**Checagem de versão do kit:** modo hub — congelada em `0.0.0` (`GOVERNANCA.md` §10), nada a
comparar.
**Ordem de execução:** LF-T1 → LF-T2 → LF-T3 → LF-T4 → LF-T5 → LF-T6 → LF-T7 → LF-T8.
**Modelo de planejamento:** Fable 5.1 (sessão do dono de 2026-09-19).

**Marcos de validação pelo dono:**

| marco | o que o dono lê | veredito |
|---|---|---|
| **Marco 1** | este plano, quando o `P-0739` fechar | `go` = plano sai de `blocked` para `ready`; `no-go` = `cancelled`, nada executado |
| **Marco 2** | a seção `## 3. Piloto medido` depois da `LF-T6`, mais o `README.md` revisado (`LF-T8`) | aceite registrado no diário (`GOVERNANCA.md` §4.5) |

**Tarefas:** 8 (`LF-T1`..`LF-T8`), fila única, sequencial.

---

## 0. O problema, medido

O loop do `scrum-master` roda num LLM e o LLM relê o contexto inteiro a cada turno. Medido em
2026-09-19 (`_VIABILIDADE-agente-leitor.md` §7.1, F2): 7–13 turnos do orquestrador por despacho,
a `contexto × $0,50/M` o turno; orquestrar uma tarefa custa **$2–6**, mais que executor e reviewer
juntos ($0,60 + $1,51). As sete sessões que rodaram o loop somaram $139,7. Sessões principais ≈ 40%
de um plano de ~$500.

A doutrina já descreve o loop como **algoritmo**: roteamento pelo veredito calculado, materialização
por instrumento, "sem discricionariedade" (`DP-G`), sem pergunta ao dono (`G-NOASK`), sem improviso
(`scrum-master` blocos A e B). O que decide não precisa de modelo; o que precisa de modelo (executar,
julgar, escalar) já roda em subagente. Este plano move o loop para um driver Python que invoca o
harness em modo headless (`claude -p`) para cada papel, e só ele.

**Sonda de viabilidade (2026-09-19, antes da recomendação):** `claude.exe` 2.1.265 existe em
`C:\Users\panta\.vscode\extensions\anthropic.claude-code-2.1.265-win32-x64\resources\native-binary\claude.exe`
(não está no `PATH`) e aceita `-p`, `--agent <agent>`, `--model <model>`, `--output-format json`,
`--allowedTools`, `--append-system-prompt`, `--json-schema`, `--resume`. Suficiente para o
mecanismo; o contrato fino (campos do JSON, hooks, permissões) é o que a `LF-T1` mede.

## 1. Decisões

| id | decisão | por quê |
|---|---|---|
| `DLF-1` | **v1 sem consultor.** Escalonamento (`A3b`, `A6a`/`escalar`, `A7`, `B3`) **encerra o loop** com relatório; nenhuma figura de replanejamento é invocada pelo driver | a forma do consultor (standby × efêmera com cenário) é decisão do plano próprio dele (`docs/consultant-spec.md` §11); o driver não a antecipa |
| `DLF-2` | binário por `PANTONIC_CLAUDE_BIN`; default o caminho da extensão medido na sonda | não está no `PATH`; fixar por variável evita chutar |
| `DLF-3` | modelo do papel = `<modelo>` do cabeçalho do card → `--model`; agente = `--agent pantonic-executor` / `pantonic-reviewer` | é a regra do Passo 4 do `scrum-master` (modelo do cabeçalho vence o `model:` do agente) |
| `DLF-4` | saída `--output-format json`; o `usage` da resposta alimenta `telemetria.py append`; `SubagentStop` **não** dispara em `-p` (o papel É a sessão) — a `LF-T1` confirma | telemetria é medida (`GOVERNANCA.md` §4.2); a fonte muda de hook para JSON |
| `DLF-5` | driver = `.claude/tools/loop.py`; testes com stub de `claude` (`tests/stubs/claude_stub.py`, devolve JSON fixo); **nenhum teste chama a rede** | TDD obrigatório (§4.4) sem custo de modelo |
| `DLF-6` | roteamento = transcrição literal dos blocos A e B do `scrum-master`; estado fora da tabela → parada com relatório | `G-NOASK`; o driver não improvisa |
| `DLF-7` | o dono interrompe por `Ctrl-C`; o driver grava checkpoint por tarefa em `.claude/estado/loop.json` e retoma de `backlog.py next` | substitui "o dono interrompe sem derrubar a sessão" (`GOVERNANCA.md` §3, linha *Orquestração*) |
| `DLF-8` | despacho ao executor cola `backlog.py show <ID>` (card verbatim) + linha do índice + gramática de retorno `DP-G` | `TK-58` fixa o mesmo para o loop atual; aqui é por construção |

## 2. Contrato headless — escrito pela `LF-T1`

Esta seção é o entregável da `LF-T1` e insumo das `LF-T2`..`LF-T5`: uma tabela com os fatos
medidos (campos do JSON de saída, exit codes, hooks que disparam, permissões exigidas por
ferramenta, tempo por chamada). Até a `LF-T1` fechar, nenhuma tarefa posterior é despachada.

## 3. Piloto medido — escrito pela `LF-T6`

Custo por tarefa (execução + revisão + orquestração) do piloto contra a série de
`docs/telemetria.tsv` e o `_VIABILIDADE` §7.1 (orquestração $2–6 por tarefa no loop em LLM).

## 4. Tarefas

### LF-T1 — Sonda do contrato headless [Sonnet · classe investigacao]
- **Status:** `ready` · 2026-09-19
- **Objetivo:** medir, não deduzir, o contrato de `claude -p` para os dois papéis, e publicar a
  seção `## 2` deste plano.
- **Método de sondagem:** na raiz do repositório, `& $env:PANTONIC_CLAUDE_BIN -p "responda a
  palavra ok" --agent pantonic-executor --model sonnet --output-format json --allowedTools Read`
  com a saída redirecionada para `%TEMP%\claude\lf-t1\executor.json`; repetir com
  `--agent pantonic-reviewer --model opus`; terceira chamada com `--allowedTools Bash Edit` e um
  prompt que cria um arquivo no scratchpad, para medir se `--permission-mode` é exigido. Para cada
  chamada registrar: exit code; campos de topo do JSON (`usage`, `total_cost_usd`, `session_id`,
  `result`, `num_turns`); se `docs/telemetria.tsv` ganhou linha (hook `SubagentStop`); se o
  `PreToolUse` de `ocupacao.py` disparou (stdout); duração.
- **Arquivos-alvo:** `docs/plans/P-0742-loop-fora-do-llm.md` §2 (tabela, 3 linhas × 7 colunas).
- **Verificação:** `python -c "import json;d=json.load(open(r'%TEMP%\claude\lf-t1\executor.json'));print(sorted(d))"`
  imprime a lista de chaves citada na tabela · `grep -c "^| chamada" docs/plans/P-0742-loop-fora-do-llm.md` → `3`.
- **Pronto quando:** a tabela tem as três linhas com todos os campos medidos e nenhuma célula
  "não medido".

### LF-T2 — Despacho do executor pelo driver [Sonnet · classe implementacao]
- **Status:** `ready` · 2026-09-19
- **Depende de:** `LF-T1`
- **Objetivo:** `loop.py despachar <plano>`: `backlog.py next` → `backlog.py start <ID>` → prompt
  = `backlog.py show <ID>` + linha do índice + gramática de retorno (`<ID> review [pendencia=…]` |
  `<ID> blocked motivo=<dependencia|premissa|ferramenta> …`) → `claude -p` (`DLF-2..4`) → parse da
  **última linha** do `result` → `backlog.py status <ID> review|blocked --razao …`.
- **Arquivos-alvo:** `.claude/tools/loop.py` (novo); `tests/test_loop.py` (novo);
  `tests/stubs/claude_stub.py` (novo, imprime JSON fixo lido de `PANTONIC_STUB_RESULT`).
- **Testes:** TF `test_despacho_review` (stub devolve `X review` → status `review` materializado
  numa cópia de fixture do plano); TF `test_despacho_blocked_premissa`; TR
  `test_retorno_invalido_para_sem_materializar` (`A2`: linha fora da gramática → parada, plano
  intacto).
- **Verificação:** `python -m pytest tests/test_loop.py -q` verde · `python .claude/tools/loop.py --help` exit 0.
- **Pronto quando:** os três testes passam e nenhum teste toca a rede (`PANTONIC_CLAUDE_BIN`
  aponta para o stub em `conftest`).

### LF-T3 — Revisão pelo driver [Sonnet · classe implementacao]
- **Status:** `ready` · 2026-09-19
- **Depende de:** `LF-T2`
- **Objetivo:** após `review`: `review_evidence.py --plano --tarefa --out <evidência>` →
  `claude -p --agent pantonic-reviewer --model opus` com o mesmo card, o caminho da evidência e a
  instrução de devolver as duas linhas de veredito → parse `veredito=` e `recomendacao=` →
  `rdo.py laudo` conforme o Passo 7 do `scrum-master`.
- **Arquivos-alvo:** `.claude/tools/loop.py`; `tests/test_loop.py`; `tests/stubs/claude_stub.py`.
- **Testes:** TF `test_revisao_aprovado_fecha_rdo`; TF `test_revisao_refazer_redespacha_uma_vez`
  (`A6`: retentativa = 1, agente novo); TR `test_laudo_fora_da_gramatica_para`.
- **Verificação:** `python -m pytest tests/test_loop.py -q` verde.
- **Pronto quando:** os três testes passam e o RDO gerado no fixture bate com o gerador (`rdo.py`).

### LF-T4 — Roteamento e encerramento [Sonnet · classe implementacao]
- **Status:** `ready` · 2026-09-19
- **Depende de:** `LF-T3`
- **Objetivo:** blocos A (`A1`..`A8a`) e B (`B0`..`B4`) do `scrum-master` transcritos como tabela
  em código (`_ROTAS`), por precedência; `B2` (ocupação) deixa de existir — o driver não tem
  contexto; escalonamento encerra (`DLF-1`); relatório de encerramento gerado por função, no
  formato do `## Relatório de encerramento` do `scrum-master`; checkpoint `.claude/estado/loop.json`
  (`DLF-7`).
- **Arquivos-alvo:** `.claude/tools/loop.py`; `tests/test_loop.py`.
- **Testes:** um TF por regra `A*`/`B*` (tabela parametrizada, uma linha por regra da skill); TR
  `test_estado_fora_da_tabela_para_com_relatorio`.
- **Verificação:** `python -m pytest tests/test_loop.py -q -k "rota"` → tantos `passed` quantas
  linhas têm os blocos A e B da skill no dia da execução.
- **Pronto quando:** cada regra da skill tem um teste com o seu id no nome.

### LF-T5 — Telemetria a partir do JSON [Sonnet · classe implementacao]
- **Status:** `ready` · 2026-09-19
- **Depende de:** `LF-T4`
- **Objetivo:** por chamada, `telemetria.py append` com `tokens_k`, `tool_uses` e `duracao_s`
  derivados do JSON (`usage`, `num_turns`, duração medida pelo driver), `fonte=json`; a coluna
  `fonte` distingue da série do hook (`fonte=usage`).
- **Arquivos-alvo:** `.claude/tools/loop.py`; `.claude/tools/telemetria.py` (aceitar `fonte=json`
  se o validador restringir o valor); `tests/test_loop.py`; `tests/test_telemetria.py`.
- **Testes:** TF `test_linha_de_telemetria_por_chamada`; TR `test_fonte_json_aceita`.
- **Verificação:** `python -m pytest tests/test_loop.py tests/test_telemetria.py -q` verde.
- **Pronto quando:** cada despacho do stub produz uma linha válida no TSV de fixture.

### LF-T6 — Piloto medido [Sonnet + dono · classe investigacao]
- **Status:** `ready` · 2026-09-19
- **Depende de:** `LF-T5`
- **Objetivo:** rodar o driver sobre ≥ 5 tarefas `ready` de um plano real escolhido pelo dono no
  Marco 1, e publicar a seção `## 3` deste plano: custo por tarefa (execução + revisão +
  orquestração, esta última = 0 por construção, mais o custo do driver = 0), reprovações,
  retentativas e paradas, contra a série (`docs/telemetria.tsv`; `_VIABILIDADE` §7.1).
- **Arquivos-alvo:** `docs/plans/P-0742-loop-fora-do-llm.md` §3.
- **Verificação:** `grep -c "^| LF-piloto" docs/plans/P-0742-loop-fora-do-llm.md` ≥ 5.
- **Pronto quando:** a tabela existe com ≥ 5 tarefas e o dono registrou o veredito do Marco 2.

### LF-T7 — Doutrina: o loop mora no driver [Opus · classe redacao]
- **Status:** `ready` · 2026-09-19
- **Depende de:** `LF-T6`
- **Objetivo:** `GOVERNANCA.md` §3, linha *Orquestração*: o loop roda no driver
  (`.claude/tools/loop.py`), o dono interrompe por `Ctrl-C` (`DLF-7`), o modelo da coluna passa a
  "nenhum — instrumento"; §4.3: a janela de orquestração deixa de ser a unidade de encerramento
  (encerra o plano, o bloqueio ou o escalonamento); `.claude/skills/scrum-master/SKILL.md` passa a
  ser a especificação do driver (blocos A e B como fonte da tabela `_ROTAS`), com nota de que a
  condução manual é fallback; `docs/DOC_MAP.md` ganha a entrada se algum dos docs cruzar 500 linhas.
- **Arquivos-alvo:** `GOVERNANCA.md` §3 e §4.3; `.claude/skills/scrum-master/SKILL.md` (cabeçalho e
  §Passo 10); `docs/DOC_MAP.md`.
- **Verificação:** `grep -c "loop.py" GOVERNANCA.md .claude/skills/scrum-master/SKILL.md` ≥ 1 em
  cada · `python .claude/tools/materializar.py check` exit 0.
- **Pronto quando:** os greps batem e o materializador não acusa deriva.

### LF-T8 — Revisão do README ao encerrar [Opus + dono · classe redacao]
- **Status:** `ready` · 2026-09-19
- **Depende de:** `LF-T7`
- **Objetivo:** revisar `README.md` contra o estado da árvore ao fim do plano (`G-README` dever 2,
  `GOVERNANCA.md` §7 item 14), com o guarda executável como instrumento e o veredito do dono como
  aceite.
- **Arquivos-alvo:** `README.md`.
- **Verificação:** `pwsh .claude/checks/check-readme.ps1` exit 0.
- **Pronto quando:** o guarda passa e o dono registrou o aceite (Marco 2).

## 5. Fora de escopo

- A forma do consultor e o seu acionamento pelo driver (`docs/consultant-spec.md` §11; plano
  próprio). Em v1 o escalonamento encerra o loop (`DLF-1`).
- O modelo conceitual do plano como interface dono↔loop (`P-0741`): o driver consome o plano pela
  gramática do `P-0739`; o que o `P-0741` acrescentar ao plano é lido pelos papéis, não pelo driver.
- Restringir a lista de ferramentas do executor (`TK-60` decide se há tíquete).

## 6. Riscos

- **Hooks em `-p`:** se o `PreToolUse` de projeto disparar dentro do papel (esperado, os hooks rodam
  em qualquer sessão), `ocupacao.py` mede o contexto do papel, não do driver — inofensivo; se
  `SubagentStop` disparar, a telemetria duplica — a `LF-T1` mede e a `LF-T5` desduplica pela coluna
  `fonte`.
- **Permissões:** `-p` sem modo de permissão pode negar `Edit`/`Bash` ao executor. A `LF-T1` mede o
  flag exigido; a `DLF` correspondente nasce na retomada, com o valor medido, nunca chutado.
- **Cache de prompt:** cada papel nasce frio (prefixo 17–37k reescrito a cada chamada) — igual ao
  regime atual de subagentes; não há piora. O ganho vem de zerar o contexto do orquestrador.

## Achados da execução

(vazio — apensado pelas rodadas.)
