# P-0742 — O loop sai do LLM

**Data:** 2026-09-19 · **Origem:** decisão de rota do dono, 2026-09-19, sobre a posição L8 de `docs/plans/_VIABILIDADE-agente-leitor.md` §7.4; retomado pela decisão do dono *"Retomar"* (2026-09-26, `TK-90b`) · **Status:** `cancelled` · 2026-09-27 · no-go do dono no Marco 1 (ver `## 9`, `AE-95`) · rodada de replanejamento `RP-1` fechada (`TK-90b`): a seção do modelo, versão 1, e os cards reescritos um por operação, na forma que o gate do card lê · **Prefixo das tarefas no diário:** `LF-T<n>` · **Prefixo das decisões:** `DLF-<n>` · **Forma:** legado (arquivo único, id de 4 dígitos).
**Ordem de execução:** fila única, sequencial, na ordem das operações da `### 1.2` (§6).
**Checagem de versão do kit:** modo hub, congelada em `0.0.0` (`GOVERNANCA.md` §10), nada a comparar.
**Modelo de planejamento:** Fable 5.1 (sessão do dono de 2026-09-19); rodada `RP-1` em Opus 5.5 (2026-09-26).

**Pronto quando:** o loop de execução de um plano roda em `.claude/tools/loop.py`, um driver Python que despacha executor e revisor por `claude -p` e materializa cada passo mecânico pelos instrumentos do kit; o piloto mediu o custo por tarefa contra a série do loop em LLM; a doutrina diz que o loop mora no driver; e o `README.md` foi revisado.

**Marcos de validação pelo dono:**

| marco | o que o dono lê | veredito |
|---|---|---|
| **Marco 1** | a `## 1. Modelo conceitual` e este plano, antes do primeiro despacho | `go` = o plano entra na janela pela diretiva de priorização, ato do dono (o `ready` da rodada `RP-1` não o põe na janela); `no-go` = `cancelled`, nada executado |
| **Marco 2** | a `## 11. Piloto medido` depois do piloto, mais o `README.md` revisado | aceite registrado no diário (`GOVERNANCA.md` §4.5) |

---

## 0. O problema, verbatim

Decisão do dono de 2026-09-19, sobre a tabela de posições de `docs/plans/_VIABILIDADE-agente-leitor.md` §7.4, linha L8, verbatim: *"L8 — loop fora do LLM (driver + `claude -p`) | viável, **recomendável como decisão de rota**, depois de L1/L2/L3 medidas | ~$180/plano; ataca a causa; muda a rota do framework"*. Destino dado pelo dono na mesma data, verbatim do registro: *"o que depende do `P-0739` → plano `docs/plans/P-0742-loop-fora-do-llm.md` (L8, absorve L5), `blocked` até o `P-0739` fechar."*

Retomada (dono, 2026-09-26, card `TK-90b`): *"Retomar"*.

O problema, medido (2026-09-19, `_VIABILIDADE-agente-leitor.md` §7.1, F2): o loop do `scrum-master` roda num LLM e o LLM relê o contexto inteiro a cada turno — 7–13 turnos do orquestrador por despacho, a `contexto × $0,50/M` o turno; orquestrar uma tarefa custa **$2–6**, mais que executor e reviewer juntos ($0,60 + $1,51). As sete sessões que rodaram o loop somaram $139,7. Sessões principais ≈ 40% de um plano de ~$500. A doutrina já descreve o loop como **algoritmo**: roteamento pelo veredito calculado, materialização por instrumento, "sem discricionariedade" (`DP-G`), sem pergunta ao dono (`G-NOASK`), sem improviso (`scrum-master` blocos A e B). O que decide não precisa de modelo; o que precisa de modelo (executar, julgar) roda em subagente. Este plano move o loop para um driver Python que invoca o harness em modo headless (`claude -p`) para cada papel, e só ele.

## 1. Modelo conceitual

**Estado do modelo:** versão 1 · 2026-09-26 · autor: modelador · 8 operações · 12 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem | lastro na §0 | tipo |
|---|---|---|---|---|---|---|
| loop de execução | o ciclo que pega a próxima tarefa de um plano, manda executar, manda revisar, decide o passo seguinte e fecha a tarefa — e as regras escritas que o descrevem | forma medida de chamar cada papel, quem entrega a tarefa ao executor, quem conduz a revisão da entrega, quem registra o consumo de cada chamada, quem decide o passo seguinte, prova em plano real, onde a norma diz que ele mora, como a porta de entrada o apresenta | Um programa em Python, sem modelo, que chama o assistente uma vez por papel — só o executor e o revisor — e grava tudo pelos programas que o kit já tem. Ele não decide, não redige e não pergunta: segue as regras de roteamento ao pé da letra, e o que foge delas ou pede consultor ou modelador encerra o loop com um relatório que traz a evidência para quem conduz; nos testes, um dublê faz o papel do assistente e nada chama a rede. | OP-1 | *"L8 — loop fora do LLM (driver + `claude -p`)"*; *"Este plano move o loop para um driver Python que invoca o harness em modo headless (`claude -p`) para cada papel, e só ele."* | escopo |
| assistente sem conversa | o próprio assistente chamado de fora, uma vez por pedido, sem uma conversa aberta que releia o contexto | forma de chamada e de resposta | Recebe numa linha de comando o pedido, o papel e o modelo, e devolve num bloco legível por programa a resposta, a sessão para retomar e o consumo da chamada. Este plano não o altera. | externo | *"driver + `claude -p`"*; *"invoca o harness em modo headless (`claude -p`) para cada papel"* | externo |
| papéis que precisam de modelo | o executor, que faz a tarefa, e o revisor, que julga a entrega — o único trabalho do loop que precisa de modelo | o que cada um recebe e devolve | O executor recebe o card inteiro e devolve uma linha dizendo se a entrega vai à revisão ou se parou, e por quê; o revisor recebe o card e a evidência e devolve o veredito com o laudo. Nenhum dos dois muda neste plano. | externo | *"o que precisa de modelo (executar, julgar) roda em subagente"* | externo |
| instrumentos do kit | os programas que já gravam o andamento das tarefas, o fechamento, o consumo e a evidência da revisão | o que cada um aceita e grava | São a única via de escrita do loop novo: ele os chama como estão e não os modifica. | externo | *"materialização por instrumento"* | externo |
| tarefa conduzida pelo loop | cada tarefa que o loop leva do despacho ao fechamento | custo de orquestrar a tarefa | Nenhuma operação deste plano altera uma tarefa; o que se observa nela, antes e depois, é quanto custa conduzi-la. | externo | *"orquestrar uma tarefa custa **$2–6**, mais que executor e reviewer juntos"* | medição |

### 1.2 Fluxo de operações

**A. O contrato com o assistente se mede antes de qualquer código**

- **OP-1** — O investigador mede, com uma chamada real para cada papel, a forma exata com que o assistente sem conversa aceita um pedido e devolve a resposta e o consumo.
  - `precisa de: assistente sem conversa, papéis que precisam de modelo` · `altera: loop de execução.forma medida de chamar cada papel` · `tarefas: LF-T1` · `lastro: driver + claude -p; invoca o harness em modo headless (claude -p) para cada papel`

**B. O programa aprende, passo a passo, o que a conversa fazia**

- **OP-2** — O implementador ensina o programa a despachar ao executor a próxima tarefa da fila, com o card inteiro e a forma exata da resposta esperada.
  - `precisa de: loop de execução, papéis que precisam de modelo, instrumentos do kit` · `altera: loop de execução.quem entrega a tarefa ao executor` · `tarefas: LF-T2` · `lastro: o que precisa de modelo (executar, julgar) roda em subagente; move o loop para um driver Python`
- **OP-3** — O implementador ensina o programa a conduzir a revisão de cada entrega, da coleta da evidência à leitura do veredito.
  - `precisa de: loop de execução, papéis que precisam de modelo, instrumentos do kit` · `altera: loop de execução.quem conduz a revisão da entrega` · `tarefas: LF-T3` · `lastro: o que precisa de modelo (executar, julgar) roda em subagente`
- **OP-4** — O implementador ensina o programa a registrar o consumo de cada chamada a partir do que o próprio assistente devolve.
  - `precisa de: loop de execução, assistente sem conversa, instrumentos do kit` · `altera: loop de execução.quem registra o consumo de cada chamada` · `tarefas: LF-T4` · `lastro: o problema, medido; materialização por instrumento`
- **OP-5** — O implementador ensina o programa a decidir o passo seguinte de cada tarefa pelas regras de roteamento já escritas, fechando, refazendo ou parando com relatório.
  - `precisa de: loop de execução, instrumentos do kit` · `altera: loop de execução.quem decide o passo seguinte` · `tarefas: LF-T5` · `lastro: roteamento pelo veredito calculado, materialização por instrumento, sem discricionariedade; sem pergunta ao dono; sem improviso`

**C. A medida vem antes da norma, e a norma antes da porta de entrada**

- **OP-6** — O investigador mede, conduzindo pelo programa até cinco tarefas reais da fila, o custo de cada uma contra a série do loop em conversa.
  - `precisa de: loop de execução, tarefa conduzida pelo loop` · `altera: loop de execução.prova em plano real` · `tarefas: LF-T6` · `lastro: ataca a causa; orquestrar uma tarefa custa $2–6`
- **OP-7** — O redator da norma declara que o loop de execução mora no programa, e não mais na conversa principal.
  - `precisa de: loop de execução` · `altera: loop de execução.onde a norma diz que ele mora` · `tarefas: LF-T7` · `lastro: recomendável como decisão de rota; muda a rota do framework`
- **OP-8** — O mantenedor revisa a apresentação do repositório contra o estado em que o plano deixa o loop, para o aceite do dono.
  - `precisa de: loop de execução` · `altera: loop de execução.como a porta de entrada o apresenta` · `tarefas: LF-T8` · `lastro: muda a rota do framework`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final | lastro na §0 |
|---|---|---|---|
| loop de execução.forma medida de chamar cada papel | a forma da chamada foi decidida no papel, e a única medida é de uma semana atrás, sobre uma versão do assistente que já foi substituída | a forma da chamada e da resposta está medida para os dois papéis — o que volta, o que dispara, o que é aceito ou negado —, e o programa é escrito contra ela | *"driver + `claude -p`"* |
| loop de execução.quem entrega a tarefa ao executor | a conversa com o modelo monta o despacho e lê a resposta, relendo o contexto inteiro a cada turno | o programa pega a próxima tarefa, cola o card e a forma da resposta, chama o executor e grava se a entrega foi à revisão ou parou | *"o que precisa de modelo (executar, julgar) roda em subagente"* |
| loop de execução.quem conduz a revisão da entrega | a conversa junta a evidência, chama o revisor e lê o veredito | o programa junta a evidência, chama o revisor e lê o veredito e o laudo, sem modelo no meio | *"o que precisa de modelo (executar, julgar) roda em subagente"* |
| loop de execução.quem registra o consumo de cada chamada | o consumo se grava quando o papel termina dentro da conversa aberta | o programa grava uma linha por chamada, com o consumo que o próprio assistente devolve, e a tarefa fecha lendo essa linha | *"O problema, medido"* |
| loop de execução.quem decide o passo seguinte | a conversa aplica regras que já estão escritas como algoritmo, e paga modelo para cumprir o que não exige juízo | o programa aplica as mesmas regras, transcritas uma a uma: fecha a tarefa aprovada, manda refazer a reprovada e para com relatório em tudo que pede consultor, modelador ou foge da tabela | *"A doutrina já descreve o loop como **algoritmo**"*; *"O que decide não precisa de modelo"* |
| loop de execução.prova em plano real | o programa nunca conduziu uma tarefa real | o programa conduziu até cinco tarefas da fila real, e o custo de cada uma está registrado ao lado da série do loop em conversa, para o dono julgar | *"~$180/plano; ataca a causa"* |
| loop de execução.onde a norma diz que ele mora | a norma diz que o loop roda na conversa principal, onde o dono interrompe sem derrubar a sessão | a norma diz que o loop mora no programa, que o dono o interrompe pelo teclado e que conduzir à mão é recurso de exceção | *"recomendável como decisão de rota"*; *"muda a rota do framework"* |
| loop de execução.como a porta de entrada o apresenta | a apresentação do repositório descreve o loop conduzido na conversa principal | a apresentação do repositório descreve o loop conduzido pelo programa, revisada contra o estado real e aceita pelo dono | *"muda a rota do framework"* |
| assistente sem conversa.forma de chamada e de resposta | aceita pedido, papel, modelo, forma da saída e ferramentas permitidas numa linha de comando, e devolve um bloco legível por programa | a mesma — este plano não o altera | *"invoca o harness em modo headless (`claude -p`) para cada papel"* |
| papéis que precisam de modelo.o que cada um recebe e devolve | o executor recebe o card e devolve uma linha de retorno; o revisor recebe o card e a evidência e devolve veredito e laudo | o mesmo — este plano não os altera | *"o que precisa de modelo (executar, julgar) roda em subagente"* |
| instrumentos do kit.o que cada um aceita e grava | cada um grava a sua parte — andamento, fechamento, consumo, evidência — pelos comandos que já tem | o mesmo — o loop novo os consome sem mudá-los | *"materialização por instrumento"* |
| tarefa conduzida pelo loop.custo de orquestrar a tarefa | de dois a seis dólares por tarefa, com sete a treze turnos do orquestrador por despacho — mais que executor e revisor juntos | perto de zero: o programa não paga modelo, e o que resta por tarefa é o custo do executor e do revisor | *"orquestrar uma tarefa custa **$2–6**"*; *"~$180/plano; ataca a causa"* |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 1 | 2026-09-26 | vigente | modelador — autoria na rodada de replanejamento RP-1, aberta pela decisão do dono "Retomar" (TK-90b) |

## 2. Fatos estabelecidos

| id | fato | fonte |
|---|---|---|
| `F-1` | Sonda de 2026-09-19: `claude.exe` 2.1.265 aceita `-p`, `--agent <agent>`, `--model <model>`, `--output-format json`, `--allowedTools`, `--append-system-prompt`, `--json-schema`, `--resume`. | sonda registrada neste plano em 2026-09-19 |
| `F-2` | Em 2026-09-26 a extensão instalada é outra: `C:\Users\panta\.vscode\extensions\anthropic.claude-code-2.1.280-win32-x64` (única pasta de `~/.vscode/extensions` com `claude` no nome), e `claude` não está no `PATH` (`which claude` sem resultado). A pasta `2.1.265` medida em 2026-09-19 não existe mais. | medido na rodada `RP-1` |
| `F-3` | `backlog.py` tem os verbos `check`, `show`, `next`, `status`, `start`, `diretiva`, `drain`; `status` recebe `id estado [--razao] [--nota] [--repo]`. O `P-0739` está `done 18/18` no índice (`docs/DIARIO_DE_OBRAS.md:245`). | `backlog.py --help` e `status --help`, rodada `RP-1` |
| `F-4` | A skill `.claude/skills/scrum-master/SKILL.md` (411 linhas) tem dez passos e duas tabelas de roteamento: bloco A com 11 regras (`A1`, `A2`, `A3a`, `A3b`, `A3c`, `A6`, `A6a`, `A7`, `A8a`, `A8`, `A9`) e bloco B com 5 (`B0`..`B4`); o grep de linhas de tabela que começam por id `A` ou `B` entre crases dá 16. | grep na rodada `RP-1` |
| `F-5` | Toda regra que escala (`A3a`, `A3b`, `A3c`, `A6a`, `A7`, `B1` e o gate do modelo do passo 9) despacha uma instância nova do `pantonic-consultant` com três entradas — o cenário do plano (`docs/plans/_CENARIO-<plano>.md` no legado; `<pasta>/cenario.md` no plano em pasta), o id do card, a evidência — e roteia pela linha `rota=` (`resolve`, `modelador` ou `planejador`) e, quando houver, `estrategico=<frase>`. A forma do consultor é a efêmera com cenário persistido, em piloto (`P-0747` `DCS-6`, `DCS-7`). | skill `scrum-master`, passo 8 e seção *Acionamento do consultor* |
| `F-6` | O passo 3 tem quatro gates: `G-PLANREADY` e o gate de delegação (oito itens), ambos de juízo; `modelo.py check --plano <plano>` (exit `1` → não delega, `B3`; exit `2` → segue com a nota "sem modelo"; exit `0` → segue); `card_check.py --plano <plano> --tarefa <ID>` (exit `1` → não delega, `B3`, nota `gate do card`). Aprovados, materializa `ready` → `in-progress`. | skill `scrum-master`, passo 3 |
| `F-7` | O passo 4 captura `<ref>` = saída de `git stash create`, ou `git rev-parse HEAD` quando ela vier vazia; grava `.claude/estado/tarefa-corrente.json` (`tarefa`, `projeto`, `modelo`, `plano`, `despachado_em`) para o hook `SubagentStop`; e pede ao executor uma linha em uma de três formas: `<tarefa> review`; `<tarefa> review pendencia=<uma linha>`; `<tarefa> blocked motivo=<dependencia, premissa ou ferramenta> <razão>`. O passo 5 lê a primeira linha não vazia e descarta a prosa depois dela. | skill `scrum-master`, passos 4 e 5 |
| `F-8` | O passo 6 roda `review_evidence.py --plano <plano> --tarefa <ID> --desde <ref> --out docs/RDO/evidencia/<plano>-<ID>.md` (legado) e invoca `pantonic-reviewer`, que devolve a linha `<tarefa> <veredito> <percentual> bloqueante=<dimensão ou nenhuma>` e a linha `laudo=<caminho>`, e às vezes um dossiê `Ato de modelo` anexo; a `recomendação` (`seguir`, `seguir com ressalva`, `refazer`, `escalar`) se lê do laudo. | skill `scrum-master`, passos 6 e 7 |
| `F-9` | O passo 9 fecha por `encerrar.py tarefa --plano --tarefa`, com `--resumo`, `--pendencia`, `--achado TEXTO ROTA` e o trio `--tool-uses --tokens-k --duracao-s` (ou `--nao-medido`) opcionais: gate do modelo, `done`, RDO em três seções, telemetria (lê a linha da tarefa já gravada em `docs/telemetria.tsv`, ou apensa o trio), achados como `AE-<n>`. O `encerrar.py handover` é opcional: `encerrar.py tarefa` só o cita se o campo existir (`.claude/tools/encerrar.py:470`). | skill `scrum-master`, passo 9; `encerrar.py tarefa --help` |
| `F-10` | `telemetria.py append` aceita `--fonte` só em `usage`, `contado`, `nao_medido`; com `usage`, `tool_uses`, `tokens_k` e `duracao_s` são obrigatórios. A série nomeia a linha do executor `<ID>`, a do revisor `<ID>-revisao` e a do consultor `<ID>-consultor-<n>` (últimas linhas de `docs/telemetria.tsv`). | `.claude/tools/telemetria.py`, docstring e `_validar_fonte`; rodada `RP-1` |
| `F-11` | `.gitignore` ignora `.claude/estado/*` e versiona só `.claude/estado/.gitkeep`; `git check-ignore -q .claude/estado/loop.json` sai `0`. `tests/stubs/` não existe. | medido na rodada `RP-1` |
| `F-12` | `pantonic-executor` declara `model: sonnet` e nenhuma linha `tools:`; `pantonic-reviewer` declara `model: opus` e `tools: Read, Glob, Grep, Bash`. | frontmatter dos dois agentes, rodada `RP-1` |
| `F-13` | `GOVERNANCA.md:93`, linha *Orquestração* da matriz do §3: *"o loop roda no contexto principal, onde o dono interrompe sem derrubar a sessão"*; `### 4.3 Execução em contexto limpo` está em `GOVERNANCA.md:646`. `materializar.py` tem o verbo `check`; `.claude/checks/check-readme.ps1` existe. | rodada `RP-1` |
| `F-14` | Antes da rodada: os oito cards `LF-T1`..`LF-T8` saem `card_check` exit 1 com `nenhum item reconhecido (comando em bloco cercado ausente)`; `modelo.py check` sai exit 2 (`plano anterior à doutrina`); o índice tem a linha do `P-0742` como `blocked` (`docs/DIARIO_DE_OBRAS.md:308`, `TK-90a`). | caso medido do `TK-90`; handover do `TK-90a` |
| `F-15` | Na Bash de um agente do harness, o ambiente traz `CLAUDECODE=1`, `CLAUDE_CODE_ENTRYPOINT=claude-vscode` e outras 11 variáveis de nome começado por `CLAUDE` (13 no total). | `env`, rodada `RP-1` |
| `F-16` | Ensaio da cadeia de instrumentos num repositório sintético (pasta temporária com cópia de `.claude/tools`, diário com a linha de índice `\| P-0001 \| Plano alfa \| ready 0/1 \| docs/plans/P-0001-alfa.md \|`, plano legado com a tarefa `ALF-T1`, `git init` e um commit): `backlog.py next --repo .` sai 0 e imprime na segunda linha `plano: P-0001 — Plano alfa (0/1) · residência: docs/plans/P-0001-alfa.md:1-18 · índice: docs/plans/P-0001-alfa.md`; `modelo.py check` sai 2; `card_check.py --root .` sai 0; `backlog.py start` e `status review` saem 0; `review_evidence.py --root . --desde <ref> --out docs/RDO/evidencia/P-0001-ALF-T1.md` sai 0 e cita o arquivo tocado; `telemetria.py append --fonte usage --file docs/telemetria.tsv` sai 0; `encerrar.py tarefa --repo .` sem o trio sai 0, grava o RDO com `**Consumo:** 3 tool uses, 12.3 k tokens, 4.5 s` lido da série e imprime ``Detalhe: `docs/RDO/P-0001-ALF-T1-primeira-tarefa-do-plano.md`.``; `next` sobre a tarefa em `review` sai 2 com `nada delegável — 0 elegível(is) · blocked 0`, e sobre a tarefa em `in-progress` sai 0 e a devolve. `card_check.py` e `modelo.py` carregam `rdo.py` e `backlog.py` de `<root>/.claude/tools/`. | ensaio na rodada `RP-1` |
| `F-17` | `backlog.py status`: transições `ready→in-progress`, `ready→blocked`, `in-progress→review`, `in-progress→blocked`, `review→done`, `review→in-progress`, `review→blocked`, `blocked→ready` (`_TRANSICOES`); `blocked` exige `--razao`, e razão com travessão `—` sai 1 (`razão contém travessão`). `next` sai 2 com `nada delegável` no stdout e 3 com erro no stderr. | `.claude/tools/backlog.py` `_TRANSICOES` e `checar_transicao`, rodada `RP-1` |
| `F-18` | O laudo gravado por `rdo.py laudo` tem `**Percentual:**`, `**Veredito:**`, `**Dimensão bloqueante:**`, `**Recomendação:**` e `**Pendência:**`, e as seções `## Motivo das dimensões fora de conforme`, `## Achado de processo` e `## Lições aprendidas na tarefa` (`.claude/tools/rdo.py:663-677`). A recomendação tem domínio fechado (`seguir`, `seguir com ressalva`, `refazer`, `escalar`); nos laudos de `docs/RDO/laudos/`: 22 `seguir`, 5 `escalar`, 4 `seguir com ressalva`. `encerrar.ler_laudo(caminho)` devolve `percentual`, `veredito`, `bloqueante`, `recomendacao`, `pendencia` e `licoes` (`.claude/tools/encerrar.py:132`). | rodada `RP-1` |
| `F-19` | Nomes medidos: evidência de card de plano legado `docs/RDO/evidencia/<P-id>-<ID>.md` (ex.: `P-0752-FPU-T1.md`) e de tíquete `docs/RDO/evidencia/DIARIO_DE_OBRAS-<ID>.md` (ex.: `DIARIO_DE_OBRAS-TK-90a.md`); cenário do consultor `docs/plans/_CENARIO-<P-id>.md` ou `docs/plans/_CENARIO-<TK-id>.md`; nenhum plano em pasta na árvore. `python .claude/tools/loop.py --help` sai 2 (arquivo ausente), `python -m pytest tests/test_loop.py -q` sai 4, e `python -m pytest tests/ -q` dá `444 passed` (2026-09-26, referência). | rodada `RP-1` |
| `F-20` | `backlog.py show` corta o dossiê no teto `DB-7` (8.000 caracteres ou 120 linhas), com a linha `… truncado (<arquivo>:<l1>-<l2>)`: `show TLG-T3b` sai com 8.210 bytes. | rodada `RP-1` |

## 3. Decisões

| id | decisão | razão |
|---|---|---|
| `DLF-1` | **v1 sem consultor e sem modelador** (reafirmada na `RP-1`, lista re-derivada da skill de 2026-09-26): toda ação que a skill `scrum-master` atribui ao consultor ou ao modelador — as escaladas `A3a`, `A3b`, `A3c`, `A6a`, `A7`, `B1` e o gate do modelo do passo 9, o dossiê `Ato de modelo` anexo ao retorno do revisor e o achado de laudo que a `A8` manda ao consultor — **encerra o loop** com relatório; o driver não invoca papel além de executor e revisor | a razão de 2026-09-19 (a forma do consultor não estava decidida) caiu: a forma está decidida e em piloto (`F-5`); a razão vigente é de fatia — o piloto do driver mede o custo do caminho feliz dos dois papéis, e acrescentar as rotas do consultor muda o escopo que o dono retomou |
| `DLF-2` | binário por `PANTONIC_CLAUDE_BIN`; sem ela, o default de `DLF-9` | não está no `PATH` (`F-2`); fixar por variável evita chutar |
| `DLF-3` | modelo do papel = `<modelo>` do cabeçalho do card, em minúsculas, → `--model`; agente = `--agent pantonic-executor` e `--agent pantonic-reviewer` | é a regra do passo 4 do `scrum-master` (modelo do cabeçalho vence o `model:` do agente) |
| `DLF-4` | saída `--output-format json`; o `usage` da resposta alimenta a telemetria pela forma de `DLF-10`; `SubagentStop` **não** dispara em `-p` (o papel é a sessão) — a sonda confirma | telemetria é medida (`GOVERNANCA.md` §4.2); a fonte muda de hook para JSON |
| `DLF-5` | driver = `.claude/tools/loop.py`; testes com stub de `claude` (`tests/stubs/claude_stub.py`, imprime o JSON lido de `PANTONIC_STUB_RESULT`); `PANTONIC_CLAUDE_BIN` aponta para o stub em toda suíte; **nenhum teste chama a rede** | TDD obrigatório (§4.4) sem custo de modelo; `tests/stubs/` nasce com o driver (`F-11`) |
| `DLF-6` | roteamento = transcrição literal dos blocos A e B do `scrum-master` (`F-4`) como tabela em código, por precedência, cada regra com seu id; `B2` não existe no driver (sem contexto, não há coesão nem ocupação a medir); estado fora da tabela → parada com relatório | `G-NOASK`; o driver não improvisa |
| `DLF-7` | o dono interrompe por `Ctrl-C`; o driver grava checkpoint por tarefa em `.claude/estado/loop.json` e retoma de `backlog.py next` | substitui "o dono interrompe sem derrubar a sessão" (`F-13`); o arquivo é estado de sessão, ignorado pelo git (`F-11`) |
| `DLF-8` | o despacho ao executor cola `backlog.py show <ID>` (card verbatim) + linha do índice + a gramática de retorno de `F-7` | `TK-58` fixa o mesmo para o loop atual; aqui é por construção |
| `DLF-9` | default do binário: a pasta `anthropic.claude-code-<versão>-win32-x64` de maior versão sob `%USERPROFILE%\.vscode\extensions`, arquivo `resources\native-binary\claude.exe`; nenhuma das duas fontes → o driver sai `2` com a mensagem `loop: binário do claude ausente (PANTONIC_CLAUDE_BIN)` | a pasta muda a cada atualização da extensão (`F-1` → `F-2`); o caminho fixo de 2026-09-19 já quebrou |
| `DLF-10` | telemetria: o driver apensa uma linha por chamada por `telemetria.py append --fonte usage` — tarefa `<ID>` para o executor e `<ID>-revisao` para o revisor, modelo = `--model`, `tokens_k` = soma de `input_tokens`, `output_tokens`, `cache_creation_input_tokens` e `cache_read_input_tokens` de `usage` dividida por 1000, uma casa; `duracao_s` = `duration_ms` dividido por 1000, uma casa; `tool_uses` = `num_turns` — e fecha por `encerrar.py tarefa` **sem** o trio, que então lê a linha `<ID>` já gravada | o domínio de `fonte` é fechado (`F-10`) e a série do revisor tem nome próprio; o driver faz o papel do hook, e `encerrar.py` lê a linha como leria a do hook (`F-9`) |
| `DLF-11` | o driver roda só os gates mecânicos do passo 3 — `modelo.py check` e `card_check.py`, com as saídas de `F-6` — e materializa `in-progress` por `backlog.py start <ID>`; o passo 1 (modelo do contexto) e os gates de juízo (`G-PLANREADY`, gate de delegação) não rodam no driver: valem no Marco 1 de cada plano que o dono põe na janela | o driver não tem contexto nem juízo; o gate mecânico é o que a skill já prescreve como terceiro e quarto gates |
| `DLF-12` | `A1` no driver = saída do `claude` diferente de `0`, stdout que não é JSON ou JSON sem `result`: uma retomada por `--resume <session_id>` com o texto fixo `Retome a tarefa do ponto em que parou e devolva só a linha de retorno.` quando há `session_id`; sem `session_id`, ou caída de novo, PARA. `A2` = um reenvio de formato por `--resume <session_id>` com a gramática de `F-7` como texto fixo; inválido de novo, PARA | `--resume` é o análogo de `SendMessage` no modo headless (`F-1`); texto fixo porque o driver não redige |
| `DLF-13` | linha de comando: `<bin> -p <prompt> --agent <agente> --model <modelo> --output-format json --allowedTools <lista>`, lista do executor `Read Edit Write Bash Glob Grep`, do revisor `Read Glob Grep Bash`; sem `--permission-mode` | a lista do revisor é a do frontmatter dele (`F-12`); a do executor são as ferramentas que o card de execução usa; a sonda mede se `Edit` e `Bash` passam sem modo de permissão |
| `DLF-14` | chaves do JSON que o driver consome: `result`, `session_id`, `num_turns`, `duration_ms`, `is_error`, e `usage` com `input_tokens`, `output_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens`; o stub imprime essas chaves; chave ausente numa chamada real → parada com relatório | o driver e o stub são escritos contra um contrato decidido, e a sonda o confirma antes de qualquer implementação |
| `DLF-15` | o driver não escreve `encerrar.py handover` nem `--resumo`; as diretivas atualizadas da `A6` são o texto do campo de recomendação do laudo, transcrito verbatim sob o título fixo `Diretivas da revisão anterior`, apensado ao dossiê original | handover e resumo são redação, e o `encerrar.py tarefa` não os exige (`F-9`); transcrição não é redação |
| `DLF-16` | o relatório de parada por `DLF-1` traz as três entradas do acionamento do consultor (`F-5`) e, quando houver, o dossiê `Ato de modelo` do revisor verbatim, para quem conduz despachar o papel | a parada só é útil se quem retoma não precisar reconstituir a evidência |
| `DLF-17` | o contrato medido pela sonda mora na `## 10. Contrato headless` deste plano, e o piloto na `## 11. Piloto medido`; cada uma diz de si mesma que é a residência | são fatos medidos do próprio plano, lidos pelo Marco 2; ficam fora das seções de autoria para não se confundirem com a `## 2` |
| `DLF-18` | o piloto roda o driver sobre as tarefas que `backlog.py next` devolver no dia da execução, até 5 tarefas fechadas ou fila vazia, e registra o número alcançado | o alvo se deriva da diretiva de priorização vigente, ato do dono; nenhuma escolha fica para o executor |
| `DLF-19` | o driver e a sonda chamam o `claude` com o ambiente do processo menos toda variável cujo nome começa por `CLAUDE`, e com `cwd` = raiz do repositório; `PANTONIC_*` passam | o driver roda também de dentro de um agente (a sonda, o piloto), onde há `CLAUDECODE=1` e outras 12 (`F-15`); a chamada tem de ser a mesma que do terminal do dono, e a sonda mede se ela passa |
| `DLF-20` | forma do driver: linha de comando `python .claude/tools/loop.py [--repo <raiz>] [--max-tarefas <n>]`, `--repo` com default na raiz do kit; cada instrumento roda como `<python> <repo>/.claude/tools/<nome>.py`, com `--repo`, `--root` ou `--file` apontando o `<repo>` e `PYTHONIOENCODING=utf-8`; `PANTONIC_CLAUDE_BIN` terminado em `.py` roda por `sys.executable`; o revisor roda com `--model opus`; o prompt vai como argumento (`DLF-13`); os testes montam repositório sintético em `tmp_path` com cópia de `.claude/tools`; o dublê lê de `PANTONIC_STUB_RESULT` uma lista JSON, consome um elemento por chamada (`json` ou `stdout`, `exit`, `arquivos`) e registra cada chamada em `<PANTONIC_STUB_RESULT>.argv.jsonl` | o repositório sintético exerce os instrumentos reais sem tocar a árvore (`I-4`, `I-5`), e a cadeia inteira passou nele (`F-16`); o revisor declara `model: opus` (`F-12`); o `show` limita o prompt a 8.000 caracteres (`F-20`); a fila do dublê cobre as rotas com mais de uma chamada (`A1`, `A2`, `A6`) sem mudar `DLF-5` |
| `DLF-21` | roteamento do driver = a tabela da `## 12. Roteamento do driver`, residência única | aplica `DLF-1`, `DLF-6` e `DLF-12` linha a linha; o que o driver não sabe decidir sem ler texto — atribuir `pendencia=` a arquivo (`B0`), dar rota a achado de laudo (`A8`), retorno do revisor fora da gramática, tarefa `in-progress` sem checkpoint — para com relatório (`I-3`); a troca de `—` por `-` na razão vem de `F-17` |
| `DLF-22` | as diretivas da `A6` (`DLF-15`) são, do laudo, a linha `**Pendência:**` inteira e o corpo de `## Motivo das dimensões fora de conforme` até o próximo `## `, verbatim, sob a linha `Diretivas da revisão anterior` | o campo `**Recomendação:**` tem domínio fechado e não carrega diretiva (`F-18`); pendência e motivo são o texto do revisor, e transcrever não é redigir (`DLF-15`) |
| `DLF-23` | checkpoint `.claude/estado/loop.json` com a tarefa, a fase (`executor` ou `revisor`), a `ref`, as retentativas e a pendência, gravado antes de cada chamada e apagado no fechamento e em toda parada; na partida, fase `revisor` retoma a revisão da tarefa dele e fase `executor` autoriza redespachar a tarefa `in-progress` dele; `Ctrl-C` sai 130 e deixa o checkpoint; `FIM` e `LIM` saem 0, toda outra parada 1, binário ausente 2; o relatório tem a forma da `## 12` | `DLF-7` fixa o checkpoint e a retomada por `next`, e o `next` não devolve tarefa em `review` (`F-16`): a fase da revisão só se retoma pelo checkpoint |

## 4. Invariantes de execução

Regras que valem para todos os cards; cada card repete, inline, a parte que o vincula.

- `I-1` **Nenhum teste chama a rede nem um modelo:** `PANTONIC_CLAUDE_BIN` aponta para `tests/stubs/claude_stub.py` em toda suíte (`DLF-5`).
- `I-2` **TDD:** o teste que afirma o comportamento nasce vermelho antes do código (`GOVERNANCA.md` §4.4).
- `I-3` **O driver não decide nem redige:** rota é linha da tabela transcrita (`DLF-6`); estado fora dela para com relatório; nenhuma pergunta ao dono (`G-NOASK`); texto enviado a um papel é fixo ou transcrito (`DLF-12`, `DLF-15`).
- `I-4` **O driver escreve só por instrumento:** status por `backlog.py status` e `start`, fechamento por `encerrar.py tarefa`, telemetria por `telemetria.py append`, evidência por `review_evidence.py`; nunca edita plano, diário ou TSV à mão.
- `I-5` **O plano não altera os instrumentos que consome** (`backlog.py`, `encerrar.py`, `review_evidence.py`, `card_check.py`, `modelo.py`, `telemetria.py`, `rdo.py`); divergência entre o instrumento e o que o card diz → `blocked` razão `premissa`.
- `I-6` **Doutrina só muda no card de doutrina, depois do piloto:** `GOVERNANCA.md` e `.claude/skills/scrum-master/SKILL.md` não mudam em card de implementação.
- `I-7` **Piso de regressão é relação:** o total da suíte re-medido no despacho não diminui; a entrega soma os testes novos.
- `I-8` **Estado de sessão não se versiona:** `.claude/estado/loop.json` é ignorado pelo git (`F-11`), e nenhum card mexe no `.gitignore`.

## 5. Tarefas

Um card por operação da `### 1.2`, na ordem delas (`OP-<n>` → `LF-T<n>`), reescritos na rodada `RP-1` (2026-09-26, `TK-90b`). Os cards de 2026-09-19 saíram inteiros; o que deles continua vale pelo texto abaixo.

### LF-T1 — A sonda mede o contrato do assistente sem conversa para os dois papéis [Sonnet · esforço medium · classe investigacao]
- **Status:** `cancelled` · 2026-09-27 · plano P-0742 cancelado no Marco 1 (no-go do dono, 2026-09-27)
- **Objetivo:** O investigador mede, com uma chamada real para cada papel, a forma exata com que o assistente sem conversa aceita um pedido e devolve a resposta e o consumo.
- **Fundamento:** `DLF-2`, `DLF-9`, `DLF-13`, `DLF-14`, `DLF-17`, `DLF-19`; `F-1`, `F-2`, `F-10`, `F-11`, `F-12`, `F-15`; riscos da `## 8` (hooks em `-p`, permissões, contrato do JSON).
- **Operação do modelo:** `OP-1`
  - OP-1: O investigador mede, com uma chamada real para cada papel, a forma exata com que o assistente sem conversa aceita um pedido e devolve a resposta e o consumo.
  - precisa de: assistente sem conversa — Recebe numa linha de comando o pedido, o papel e o modelo, e devolve num bloco legível por programa a resposta, a sessão para retomar e o consumo da chamada. Este plano não o altera.; papéis que precisam de modelo — O executor recebe o card inteiro e devolve uma linha dizendo se a entrega vai à revisão ou se parou, e por quê; o revisor recebe o card e a evidência e devolve o veredito com o laudo. Nenhum dos dois muda neste plano.
- **Camada e fronteira:** investigação fora do código do kit: três chamadas reais ao binário do `claude`, na raiz do repositório, e uma tabela escrita na `## 10. Contrato headless` deste plano. Nenhum arquivo de `.claude/tools/`, de `tests/`, `GOVERNANCA.md` ou de skill muda.
- **Domínio:** *assistente sem conversa* = o binário do `claude` chamado com `-p`, uma vez por pedido; *papel* = o agente passado em `--agent` (`pantonic-executor` ou `pantonic-reviewer`); *chaves de `DLF-14`* = `result`, `session_id`, `num_turns`, `duration_ms`, `is_error` e, dentro de `usage`, `input_tokens`, `output_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens`.
- **Arquivos-alvo:**
  - `docs/plans/P-0742-loop-fora-do-llm.md`
- **Método de sondagem:**
  1. Binário (`DLF-2`, `DLF-9`): o valor de `PANTONIC_CLAUDE_BIN`, se definida; senão `C:\Users\panta\.vscode\extensions\anthropic.claude-code-2.1.280-win32-x64\resources\native-binary\claude.exe` (`F-2`: a única pasta `anthropic.claude-code-*` hoje). Registrar o caminho usado.
  2. Ambiente de cada chamada (`DLF-19`): o do processo menos toda variável cujo nome começa por `CLAUDE` (`F-15`: dentro de um agente há `CLAUDECODE=1` e outras 12); `cwd` = raiz do repositório. Rodar as chamadas por um script Python descartável em `%TEMP%\claude\lf-t1\`, com `subprocess.run(argv, cwd=<raiz>, env=<ambiente>, capture_output=True, text=True, encoding="utf-8")`, gravando o stdout de cada uma em `%TEMP%\claude\lf-t1\sonda-<n>.json`.
  3. Antes de cada chamada, contar as linhas de `docs/telemetria.tsv`; depois dela, contar de novo (a diferença mede se o hook `SubagentStop` grava linha em `-p`).
  4. As três chamadas, com o `argv` exato (cada item é um argumento; o prompt é um argumento só):
     - `sonda-1`: `[<bin>, "-p", "Responda só a palavra ok. Ação — teste de acentuação.", "--agent", "pantonic-executor", "--model", "sonnet", "--output-format", "json", "--allowedTools", "Read Edit Write Bash Glob Grep"]`
     - `sonda-2`: `[<bin>, "-p", "Responda só a palavra ok.", "--agent", "pantonic-reviewer", "--model", "opus", "--output-format", "json", "--allowedTools", "Read Glob Grep Bash"]`
     - `sonda-3`: o `argv` da `sonda-1` com o prompt trocado por `Crie com a ferramenta Write o arquivo .claude/estado/sonda-lf-t1.txt com o conteúdo ok, rode com a ferramenta Bash o comando python --version e devolva só a palavra feito.`
  5. Depois da `sonda-3`, registrar se `.claude/estado/sonda-lf-t1.txt` existe e apagá-lo (estado de sessão, ignorado pelo git, `F-11`).
  6. Escrever na `## 10. Contrato headless`, logo abaixo do parágrafo que já está lá e separada dele por uma linha em branco, a tabela com este cabeçalho, verbatim (as quebras são as do bloco), e uma linha por chamada, na ordem, cuja primeira célula é `sonda-1`, `sonda-2` e `sonda-3`:

     ```
     | chamada | linha de comando | exit | chaves de topo do JSON | chaves de DLF-14 ausentes | linhas novas em docs/telemetria.tsv | ferramenta negada | duration_ms e num_turns |
     |---|---|---|---|---|---|---|---|
     ```

     Célula a célula: *linha de comando* = o `argv` sem o caminho do binário, com o prompt trocado por `<prompt da sonda-<n>>`; *exit* = o código de saída; *chaves de topo do JSON* = as chaves de `json.loads(stdout)` em ordem alfabética, separadas por vírgula, ou `stdout não é JSON:` seguido dos primeiros 200 caracteres; *chaves de DLF-14 ausentes* = a lista, ou `nenhuma`; *linhas novas em docs/telemetria.tsv* = a diferença do passo 3; *ferramenta negada* = o conteúdo de `permission_denials` quando a chave existe e não é vazia; senão, na `sonda-3`, `nenhuma (arquivo criado: sim)` ou `nenhuma (arquivo criado: não)`, e nas outras `nenhuma`; *duration_ms e num_turns* = os dois valores, separados por ` / `. Nenhuma célula vazia e nenhuma com barra vertical dentro.
  7. Abaixo da tabela, separada por uma linha em branco, a linha `Binário medido: <caminho do passo 1> · ambiente sem variáveis CLAUDE* · <data da medida AAAA-MM-DD>`.
- **Restrições desta tarefa:** esta é a única tarefa do plano que chama o modelo real (`I-1` vale para as demais); nenhum arquivo além do plano muda — os instrumentos do kit não mudam (`I-5`) e o `.gitignore` não muda (`I-8`); a tabela é fato medido, e nenhuma célula se deduz da documentação da ferramenta.
- **Não fazer:** não usar `--permission-mode` nem `--dangerously-skip-permissions`; não repetir uma chamada para obter outro resultado (uma chamada por linha da tabela); não editar `docs/telemetria.tsv`, `.gitignore`, `.claude/settings.json`, `.claude/settings.local.json` nem outra seção do plano.
- **Contingências:**
  1. se o binário do passo 1 não existe → parar e sinalizar `blocked` razão `premissa`, com o caminho procurado.
  2. se alguma chamada sai diferente de 0 com texto sobre sessão aninhada (`nested` ou `another Claude Code session` no stdout ou no stderr) → registrar a linha como está na tabela, terminar as outras e parar e sinalizar `blocked` razão `premissa`, com a linha literal do erro.
  3. se a coluna *linhas novas em docs/telemetria.tsv* passa de 0 em qualquer chamada → terminar a tabela e parar e sinalizar `blocked` razão `premissa`, com as linhas novas (a telemetria de `DLF-10` duplicaria).
  4. se a `sonda-3` tem ferramenta negada ou o arquivo não foi criado → terminar a tabela e parar e sinalizar `blocked` razão `premissa`, com a linha literal da recusa.
  5. se alguma chave de `DLF-14` falta numa chamada que saiu 0 → terminar a tabela e parar e sinalizar `blocked` razão `premissa`, com as chaves medidas.
- **Testes:** nenhum teste novo; nenhuma suíte a rodar (nenhum código muda).
- **Verificação:**
  1. `python -c "from pathlib import Path;L=Path('docs/plans/P-0742-loop-fora-do-llm.md').read_text(encoding='utf-8').splitlines();i=L.index('## 10. Contrato headless');j=L.index('## 11. Piloto medido');r=[l for l in L[i:j] if l.startswith('| sonda-')];print('sondas=%d completas=%d' % (len(r),sum(1 for l in r if len([c for c in l.strip().strip('|').split('|') if c.strip()])==8)))"` → antes `sondas=0 completas=0`, depois `sondas=3 completas=3`
- **Pronto quando (o fato que tem de existir ao final):**
  - `loop de execução.forma medida de chamar cada papel` — *a forma da chamada e da resposta está medida para os dois papéis — o que volta, o que dispara, o que é aceito ou negado —, e o programa é escrito contra ela* — Verificação 1.
- **Fora do escopo desta tarefa:** escrever o driver (`LF-T2`); o modo de permissão e toda mudança em `DLF-13` e `DLF-14` diante de medida divergente (triagem, pelas contingências 2 a 5).

### LF-T2 — O driver despacha ao executor a próxima tarefa da fila [Sonnet · esforço high · classe implementacao]
- **Status:** `cancelled` · 2026-09-27 · plano P-0742 cancelado no Marco 1 (no-go do dono, 2026-09-27)
- **Depende de:** `LF-T1`
- **Objetivo:** O implementador ensina o programa a despachar ao executor a próxima tarefa da fila, com o card inteiro e a forma exata da resposta esperada.
- **Fundamento:** `DLF-2`, `DLF-3`, `DLF-5`, `DLF-8`, `DLF-9`, `DLF-11`, `DLF-13`, `DLF-19`, `DLF-20`, `DLF-21`; `F-3`, `F-6`, `F-7`, `F-15`, `F-16`, `F-17`, `F-19`; os textos fixos da `## 12`.
- **Operação do modelo:** `OP-2`
  - OP-2: O implementador ensina o programa a despachar ao executor a próxima tarefa da fila, com o card inteiro e a forma exata da resposta esperada.
  - precisa de: loop de execução — Um programa em Python, sem modelo, que chama o assistente uma vez por papel — só o executor e o revisor — e grava tudo pelos programas que o kit já tem. Ele não decide, não redige e não pergunta: segue as regras de roteamento ao pé da letra, e o que foge delas ou pede consultor ou modelador encerra o loop com um relatório que traz a evidência para quem conduz; nos testes, um dublê faz o papel do assistente e nada chama a rede.; papéis que precisam de modelo — O executor recebe o card inteiro e devolve uma linha dizendo se a entrega vai à revisão ou se parou, e por quê; o revisor recebe o card e a evidência e devolve o veredito com o laudo. Nenhum dos dois muda neste plano.; instrumentos do kit — São a única via de escrita do loop novo: ele os chama como estão e não os modifica.
- **Camada e fronteira:** kit, ferramenta nova `.claude/tools/loop.py`, só biblioteca padrão; ela chama os instrumentos do kit **por subprocesso**, como `[sys.executable, str(<repo>/".claude"/"tools"/"<nome>.py"), ...]` com `cwd=<repo>` e o ambiente do processo mais `PYTHONIOENCODING=utf-8`, lendo stdout e stderr como UTF-8 — nunca por import (a exceção é a `LF-T3`, que importa `encerrar.ler_laudo`). O binário do `claude` roda com o ambiente de `ambiente_do_papel`. Testes em `tests/test_loop.py` e dublê em `tests/stubs/claude_stub.py`; nenhum teste toca a árvore real nem a rede.
- **Domínio:** *próxima tarefa* = a que `backlog.py next` devolve (saída 0: primeira linha `=== PRÓXIMA TAREFA: <ID> — <título> [<modelo>[ + dono][ · esforço <e>] · classe <c>]`, segunda linha `plano: <P-id> — <título> (<d>/<t>) · residência: <caminho>:<a>-<b> · índice: <âncora>` ou a mesma com `tíquete:`; saída 2: `nada delegável — …` no stdout; saída 3: erro no stderr — `F-16`, `F-17`); *linha do índice* = essa segunda linha, verbatim; *gates mecânicos* (`DLF-11`) = `modelo.py check` (exit 1 recusa; 2 e 0 seguem) e `card_check.py` (exit 1 recusa); *retorno do executor* = a primeira linha não vazia do `result`, numa das três formas da gramática (`F-7`); prosa depois dela se descarta.
- **Arquivos-alvo:**
  - `.claude/tools/loop.py` (novo)
  - `tests/test_loop.py` (novo)
  - `tests/stubs/claude_stub.py` (novo)
- **Contratos/classes:** em `.claude/tools/loop.py`, com `from __future__ import annotations` e `@dataclass` onde indicado:
  - `KIT = Path(__file__).resolve().parents[2]`.
  - `class BinarioAusente(Exception)` — `str(exc) == "loop: binário do claude ausente (PANTONIC_CLAUDE_BIN)"`.
  - `class FalhaDeInstrumento(RuntimeError)` — `__init__(self, instrumento: str, stderr: str)`; atributos `instrumento` (ex.: `"backlog.py next"`) e `stderr`; `str(exc) == f"{instrumento}: {stderr}"`.
  - `def resolver_binario(env: Mapping[str, str], home: Path) -> list[str]` — `env["PANTONIC_CLAUDE_BIN"]` não vazio: `[sys.executable, valor]` quando termina em `.py`, senão `[valor]`; sem ela, as pastas `home/.vscode/extensions/anthropic.claude-code-<versão>-win32-x64` com `resources/native-binary/claude.exe` presente, a de maior `<versão>` comparada como tupla de inteiros (`2.1.280` > `2.1.9`), → `[str(<exe>)]`; nenhuma → `raise BinarioAusente()`.
  - `def ambiente_do_papel(env: Mapping[str, str]) -> dict[str, str]` — cópia sem toda chave que começa por `CLAUDE` (`DLF-19`).
  - `@dataclass class Chamada: exit: int; stdout: str; resposta: dict | None` — `resposta` = `json.loads(stdout)` quando o resultado é `dict`, senão `None`.
  - `def chamar(prefixo: list[str], repo: Path, prompt: str, papel: str, modelo: str, resume: str | None = None) -> Chamada` — `papel` `"executor"` → agente `pantonic-executor`, ferramentas `"Read Edit Write Bash Glob Grep"`; `"revisor"` → `pantonic-reviewer`, `"Read Glob Grep Bash"` (`DLF-13`); `argv = prefixo + ["-p", prompt, "--agent", agente, "--model", modelo, "--output-format", "json", "--allowedTools", ferramentas] + (["--resume", resume] if resume else [])`; `subprocess.run(argv, cwd=repo, env=ambiente_do_papel(os.environ), capture_output=True, text=True, encoding="utf-8", errors="replace")`.
  - `@dataclass class Proxima: tarefa: str; titulo: str; modelo: str; pai: str; plano: Path; linha_indice: str; status: str` — `modelo` = primeira palavra dentro dos colchetes; `plano` = `repo / <caminho da residência>`; `status` = valor da primeira linha `- **Status:** \`<valor>\`` depois da linha `--- dossiê`.
  - `def proxima(repo: Path) -> Proxima | None` — roda `backlog.py next --repo <repo>`; saída 2 → `None`; outra saída diferente de 0 → `raise FalhaDeInstrumento("backlog.py next", <stderr>)`.
  - `def gates(repo: Path, prox: Proxima) -> str | None` — `modelo.py check --plano <plano> --root <repo>` sai 1 → `"modelo.py check: " + <stderr>`; `card_check.py --plano <plano> --tarefa <ID> --root <repo>` sai 1 → `"gate do card: " + <stderr>`; senão `None`.
  - `def gramatica(tarefa: str) -> str` e `def montar_prompt(repo: Path, prox: Proxima) -> str` — textos fixos abaixo.
  - `@dataclass class Retorno: tarefa: str; status: str; motivo: str | None; razao: str | None; pendencia: str | None; linha: str | None; sessao: str | None` — `status` ∈ {`"review"`, `"blocked"`, `"invalido"`, `"queda"`}.
  - `def interpretar_retorno(chamada: Chamada, tarefa: str) -> Retorno` — `queda` quando `exit != 0`, `resposta is None` ou sem `"result"` (`sessao` = `resposta.get("session_id")` se houver resposta); senão casa a primeira linha não vazia de `result` (sem espaços nas pontas) com a regex abaixo e exige `id == tarefa`; não casou → `invalido`, com `linha` = essa linha (ou `None` se o `result` é vazio).
  - `def materializar_retorno(repo: Path, ret: Retorno) -> None` — `review` → `backlog.py status <ID> review --repo <repo>`; `blocked` → `backlog.py status <ID> blocked --razao "<motivo> <razão>" --repo <repo>`, com todo `—` da razão trocado por `-` (`F-17`); saída diferente de 0 → `raise FalhaDeInstrumento("backlog.py status", <stderr>)`; `invalido` e `queda` → nada.
  - `@dataclass class Despacho: estado: str; prox: Proxima | None = None; razao: str | None = None; ref: str | None = None; prompt: str | None = None; chamada: Chamada | None = None; retorno: Retorno | None = None` — `estado` ∈ {`"vazia"`, `"fora"`, `"recusada"`, `"despachada"`}.
  - `def despachar(repo: Path, prefixo: list[str], retomar: str | None = None, antes_da_chamada: Callable[[Proxima, str], None] | None = None) -> Despacho` — `proxima` → `None`: `Despacho("vazia")`; status `ready`: segue com `backlog.py start <ID> --repo <repo>` (saída diferente de 0 → `FalhaDeInstrumento("backlog.py start", …)`); status `in-progress` **e** `tarefa == retomar`: segue sem `start`; qualquer outro: `Despacho("fora", prox, razao=f"tarefa {ID} em {status} sem checkpoint")`, sem chamada. Os `gates` rodam antes do `start`; recusa → `Despacho("recusada", prox, razao=<texto>)`. Depois: `ref` = stdout de `git stash create` (sem espaços nas pontas), ou `git rev-parse HEAD` quando vier vazio; `prompt = montar_prompt(repo, prox)`; `antes_da_chamada(prox, ref)` quando dado; `chamar(prefixo, repo, prompt, "executor", prox.modelo.lower())`; `interpretar_retorno`; `materializar_retorno`; → `Despacho("despachada", prox, None, ref, prompt, chamada, retorno)`.
  - Regex do retorno (a linha inteira):

    ```
    ^(?P<id>\S+) (?:review(?: pendencia=(?P<pend>.+))?|blocked motivo=(?P<motivo>dependencia|premissa|ferramenta) (?P<razao>.+))$
    ```

  - Dublê `tests/stubs/claude_stub.py` (`DLF-20`): `sys.stdout.reconfigure(encoding="utf-8")`; lê a lista JSON do arquivo em `PANTONIC_STUB_RESULT`; vazia → imprime `stub: fila vazia` no stderr e sai 3; senão tira o primeiro elemento, regrava o resto no arquivo, apensa a `<PANTONIC_STUB_RESULT>.argv.jsonl` a linha `json.dumps({"argv": sys.argv[1:], "env_claude": sorted(k for k in os.environ if k.startswith("CLAUDE"))}, ensure_ascii=False)`, grava cada par de `"arquivos"` (caminho relativo ao `cwd` → conteúdo, UTF-8, criando as pastas), imprime `json.dumps(elemento["json"], ensure_ascii=False)` quando há `"json"`, ou `elemento["stdout"]` quando há `"stdout"`, e sai com `elemento.get("exit", 0)`.
- **Texto novo, literal:** os textos fixos da `## 12`, copiados daqui (as quebras são as do bloco; `<ID>` é trocado pelo id da tarefa). `gramatica(tarefa)`:

  ```
  Devolva uma única linha, numa destas três formas, e nada antes dela:
  <ID> review
  <ID> review pendencia=<uma linha>
  <ID> blocked motivo=<dependencia|premissa|ferramenta> <uma linha de razão>
  ```

  `montar_prompt(repo, prox)` = stdout de `backlog.py show <ID> --repo <repo>` sem espaços no fim, uma linha em branco, `prox.linha_indice`, uma linha em branco, `gramatica(<ID>)`.
- **Passos:**
  1. Criar `tests/stubs/claude_stub.py` como em `Contratos/classes`.
  2. Escrever em `tests/test_loop.py` o cabeçalho de teste de `Testes` e os nove testes, e rodá-los vermelhos (`I-2`).
  3. Escrever `.claude/tools/loop.py` com o que está em `Contratos/classes`, e nada de `main` nem bloco `if __name__ == "__main__"` (são da `LF-T5`).
  4. Rodar a Verificação 1 e 2 e `python -m pytest tests/ -q`.
- **Restrições desta tarefa:** `I-1` — nenhum teste chama a rede nem um modelo: `PANTONIC_CLAUDE_BIN` aponta para o dublê em todo teste; `I-2` — o teste nasce vermelho antes do código; `I-3` — o driver não decide nem redige: todo texto enviado ao executor é o fixo acima ou saída de instrumento; `I-4` — o driver escreve só por instrumento (`backlog.py start` e `status`); `I-5` — `backlog.py`, `encerrar.py`, `review_evidence.py`, `card_check.py`, `modelo.py`, `telemetria.py` e `rdo.py` não mudam; `I-7` — o total de `python -m pytest tests/ -q` re-medido no despacho não diminui e ganha os 9 testes novos (referência 2026-09-26: `444 passed`).
- **Não fazer:** não importar `backlog`, `rdo`, `modelo` nem `card_check` em `loop.py`; não escrever `main`, argparse, checkpoint, roteamento, revisão nem telemetria (são `LF-T3` a `LF-T5`); não usar `shell=True`; não tocar a árvore real nos testes (todo teste usa `_montar_repo`); não criar `tests/conftest.py`.
- **Contingências:**
  1. se a `## 10. Contrato headless` deste plano tem, em alguma linha `sonda-`, *chaves de DLF-14 ausentes* diferente de `nenhuma` ou *ferramenta negada* diferente de `nenhuma` e de `nenhuma (arquivo criado: sim)` → parar e sinalizar `blocked` razão `premissa`, citando a linha.
  2. se `backlog.py next --repo <repo>` no repositório de teste imprime a segunda linha fora da forma de `Domínio` → parar e sinalizar `blocked` razão `premissa`, com a linha impressa.
  3. se `python -m pytest tests/ -q` reduz o total por teste fora de `tests/test_loop.py` → parar e sinalizar `blocked` razão `dependencia`, com o nome do teste.
- **Testes:** `tests/test_loop.py` (novo). Cabeçalho do arquivo, reusado pelas `LF-T3` a `LF-T5`:
  - `_ROOT = Path(__file__).resolve().parents[1]`; `loop` carregado por caminho de `_ROOT/".claude"/"tools"/"loop.py"` com `importlib.util.spec_from_file_location("loop", …)`, registrado em `sys.modules["loop"]` antes do `exec_module`; `STUB = _ROOT/"tests"/"stubs"/"claude_stub.py"`; `PREFIXO = [sys.executable, str(STUB)]`.
  - `_montar_repo(tmp_path, status_t1="ready", antes_t1="ok", duas_tarefas=False) -> Path` — `repo = tmp_path/"repo"`; `shutil.copytree(_ROOT/".claude"/"tools", repo/".claude"/"tools", ignore=shutil.ignore_patterns("__pycache__"))`; cria `repo/.claude/estado/`; grava os arquivos abaixo em UTF-8; `git init -q`, `git -c user.email=t@t -c user.name=t add -A`, `git -c user.email=t@t -c user.name=t commit -qm base`, todos com `cwd=repo`. `docs/DIARIO_DE_OBRAS.md` (as quebras são as do bloco; `<t>` = `2` com `duas_tarefas`, senão `1`):

    ```
    # Diário de Obras — Teste
    **Diretiva de priorização:** Priorize `P-0001`.

    <!-- fila:gerada -->
    **Fila corrente:** —
    <!-- /fila:gerada -->

    ## Índice

    | ID | Título | Status | Âncora |
    |---|---|---|---|
    | P-0001 | Plano alfa | ready 0/<t> | docs/plans/P-0001-alfa.md |
    ```

    `docs/plans/P-0001-alfa.md` (as quebras são as do bloco; `<s>` = `status_t1`, `<a>` = `antes_t1`; o bloco de `ALF-T2` entra só com `duas_tarefas`, entre o de `ALF-T1` e o `## 9`, precedido de uma linha em branco):

    ```
    # P-0001 — Plano alfa

    **Status:** `ready` · **Prefixo das tarefas no diário:** `ALF-T<n>`

    ## 5. Tarefas

    ### ALF-T1 — Primeira tarefa do plano [Sonnet · classe implementacao]
    - **Status:** `<s>` · 2026-09-26
    - **Objetivo:** entregar a primeira coisa.
    - **Arquivos-alvo:**
      - `a.txt`
    - **Verificação:**
      1. `python -c "print('ok')"` → antes `<a>`, depois `ok`
    - **Pronto quando:** o arquivo existe.

    ### ALF-T2 — Segunda tarefa do plano [Sonnet · classe implementacao]
    - **Status:** `ready` · 2026-09-26
    - **Objetivo:** entregar a segunda coisa.
    - **Arquivos-alvo:**
      - `b.txt`
    - **Verificação:**
      1. `python -c "print('ok')"` → antes `ok`, depois `ok`
    - **Pronto quando:** o arquivo existe.

    ## 9. Achados da execução

    (vazio)
    ```

    `docs/plans/_INBOX.md` = `**Próximo id de plano: P-0002.**` e uma quebra; `docs/telemetria.tsv` = a linha `data	projeto	tarefa	modelo	tool_uses	tokens_k	duracao_s	fonte` (separada por tabulação) e uma quebra.
  - `E(texto, sessao="s1", arquivos=None) -> dict` — `{"json": {"result": texto, "session_id": sessao, "num_turns": 3, "duration_ms": 1500, "is_error": False, "usage": {"input_tokens": 1000, "output_tokens": 2000, "cache_creation_input_tokens": 300, "cache_read_input_tokens": 45000}}}`, mais `"arquivos": arquivos` quando dado.
  - `_fila(tmp_path, monkeypatch, *elementos) -> Path` — grava a lista em `tmp_path/"fila.json"` e faz `monkeypatch.setenv("PANTONIC_CLAUDE_BIN", str(STUB))` e `monkeypatch.setenv("PANTONIC_STUB_RESULT", str(<fila>))`; `_chamadas(fila) -> list[dict]` — as linhas de `<fila>.argv.jsonl` (lista vazia se o arquivo não existe); `_arg(argv, flag)` — o valor depois de `flag`; `_status(repo, tarefa) -> str` — o valor de `- **Status:** \`…\`` no bloco `### <tarefa> —` de `docs/plans/P-0001-alfa.md`.
  - `test_tf_lft2_despacho_review_materializa` — fila `E("ALF-T1 review")`; `despachar(repo, PREFIXO, antes_da_chamada=<registra os argumentos>)` → `estado == "despachada"`, `retorno.status == "review"`, `_status == "review"`; a função registrada foi chamada uma vez, com `prox.tarefa == "ALF-T1"` e `ref` de 40 caracteres hexadecimais; uma chamada, com `_arg` de `--agent` = `pantonic-executor`, `--model` = `sonnet`, `--output-format` = `json`, `--allowedTools` = `Read Edit Write Bash Glob Grep`; o prompt (`_arg` de `-p`) contém `### ALF-T1 — Primeira tarefa do plano [Sonnet · classe implementacao]`, `plano: P-0001 — Plano alfa (0/1)` e `ALF-T1 blocked motivo=<dependencia|premissa|ferramenta> <uma linha de razão>`.
  - `test_tf_lft2_primeira_linha_vale` — `E("ALF-T1 review\n\nprosa final qualquer")` → `retorno.status == "review"` (a regra concorrente, última linha, daria `invalido`).
  - `test_tf_lft2_blocked_razao_sem_travessao` — `E("ALF-T1 blocked motivo=premissa o alvo — não existe")` → `retorno.status == "blocked"`, `motivo == "premissa"`, `_status == "blocked"` e o plano contém `premissa o alvo - não existe` (sem a troca, o `backlog.py status` sai 1 e a tarefa fica `in-progress`).
  - `test_tr_lft2_retorno_invalido_nao_materializa` — `E("feito, tudo certo")` → `retorno.status == "invalido"`, `retorno.linha == "feito, tudo certo"`, `_status == "in-progress"`.
  - `test_tr_lft2_gate_do_card_recusa_sem_chamada` — `_montar_repo(antes_t1="nao")` → `estado == "recusada"`, `"gate do card" in razao`, `_status == "ready"`, `_chamadas == []`.
  - `test_tr_lft2_tarefa_em_curso_sem_retomada_nao_despacha` — `_montar_repo(status_t1="in-progress")`, fila `E("ALF-T1 review")`; `despachar(repo, PREFIXO)` → `estado == "fora"`, `razao == "tarefa ALF-T1 em in-progress sem checkpoint"`, `_chamadas == []`; em seguida `despachar(repo, PREFIXO, retomar="ALF-T1")` → `estado == "despachada"` e `_status == "review"`.
  - `test_tf_lft2_binario_maior_versao_numerica` — em `tmp_path/"home"`, arquivos vazios `.vscode/extensions/anthropic.claude-code-2.1.9-win32-x64/resources/native-binary/claude.exe` e o mesmo com `2.1.280` → `resolver_binario({}, home) == [str(<o de 2.1.280>)]` (a ordem de texto escolheria `2.1.9`); e `resolver_binario({"PANTONIC_CLAUDE_BIN": "x/claude_stub.py"}, home) == [sys.executable, "x/claude_stub.py"]`.
  - `test_tr_lft2_binario_ausente` — `resolver_binario({}, tmp_path/"vazio")` levanta `BinarioAusente` com `str == "loop: binário do claude ausente (PANTONIC_CLAUDE_BIN)"`.
  - `test_tf_lft2_ambiente_sem_variaveis_claude` — `monkeypatch.setenv("CLAUDECODE", "1")` e `monkeypatch.setenv("CLAUDE_CODE_ENTRYPOINT", "x")`; fila `E("ALF-T1 review")`; `despachar` → `_chamadas(fila)[0]["env_claude"] == []`.

  Suítes: `python -m pytest tests/test_loop.py -q`; `python -m pytest tests/ -q`.
- **Verificação:**
  1. `python -c "import re,subprocess,sys;from pathlib import Path;p=Path('tests/test_loop.py');k='lft2';t=p.read_text(encoding='utf-8') if p.is_file() else '';r=subprocess.run([sys.executable,'-m','pytest',str(p),'-q','-k',k],capture_output=True,text=True).stdout if k in t else '';m=re.search('([0-9]+) passed',r);f=re.search('([0-9]+) failed',r);print(k,'passed=%s failed=%s' % (m.group(1) if m else 0,f.group(1) if f else 0))"` → antes `lft2 passed=0 failed=0`, depois `lft2 passed=9 failed=0`
  2. `python -c "from pathlib import Path;p=Path('tests/stubs/claude_stub.py');print('stub', p.is_file() and 'PANTONIC_STUB_RESULT' in p.read_text(encoding='utf-8'))"` → antes `stub False`, depois `stub True`
- **Pronto quando:**
  - `loop de execução.quem entrega a tarefa ao executor` — *o programa pega a próxima tarefa, cola o card e a forma da resposta, chama o executor e grava se a entrega foi à revisão ou parou* — Verificação 1 e 2.
- **Fora do escopo desta tarefa:** a revisão (`LF-T3`); o registro de consumo (`LF-T4`); a retomada da `A1`, o reenvio da `A2`, o checkpoint, o relatório e a linha de comando (`LF-T5`).

### LF-T3 — O driver conduz a revisão da entrega, da evidência ao veredito [Sonnet · esforço high · classe implementacao]
- **Status:** `cancelled` · 2026-09-27 · plano P-0742 cancelado no Marco 1 (no-go do dono, 2026-09-27)
- **Depende de:** `LF-T2`
- **Objetivo:** O implementador ensina o programa a conduzir a revisão de cada entrega, da coleta da evidência à leitura do veredito.
- **Fundamento:** `DLF-1`, `DLF-13`, `DLF-16`, `DLF-19`, `DLF-20`, `DLF-21`; `F-8`, `F-12`, `F-16`, `F-18`, `F-19`; os textos fixos da `## 12`.
- **Operação do modelo:** `OP-3`
  - OP-3: O implementador ensina o programa a conduzir a revisão de cada entrega, da coleta da evidência à leitura do veredito.
  - precisa de: loop de execução — Um programa em Python, sem modelo, que chama o assistente uma vez por papel — só o executor e o revisor — e grava tudo pelos programas que o kit já tem. Ele não decide, não redige e não pergunta: segue as regras de roteamento ao pé da letra, e o que foge delas ou pede consultor ou modelador encerra o loop com um relatório que traz a evidência para quem conduz; nos testes, um dublê faz o papel do assistente e nada chama a rede.; papéis que precisam de modelo — O executor recebe o card inteiro e devolve uma linha dizendo se a entrega vai à revisão ou se parou, e por quê; o revisor recebe o card e a evidência e devolve o veredito com o laudo. Nenhum dos dois muda neste plano.; instrumentos do kit — São a única via de escrita do loop novo: ele os chama como estão e não os modifica.
- **Camada e fronteira:** kit, `.claude/tools/loop.py` (existe desde a `LF-T2`): acrescenta a fase do revisor. Os instrumentos rodam por subprocesso, como na `LF-T2` (`[sys.executable, str(<repo>/".claude"/"tools"/"<nome>.py"), ...]`, `cwd=<repo>`, `PYTHONIOENCODING=utf-8`); a única importação de instrumento é `encerrar.ler_laudo`, carregado por caminho de `Path(__file__).resolve().parent / "encerrar.py"` com `importlib.util.spec_from_file_location("encerrar", …)` e registrado em `sys.modules["encerrar"]` antes do `exec_module`. O revisor roda por `chamar(prefixo, repo, prompt, "revisor", "opus")`, a função da `LF-T2`.
- **Domínio:** *evidência mecânica* = o dossiê que `review_evidence.py` grava, recortado desde a `ref` capturada no despacho; *retorno do revisor* = duas linhas, `<ID> <veredito> <percentual> bloqueante=<dimensão|nenhuma>` e `laudo=<caminho>`, e às vezes um dossiê `Ato de modelo` depois delas (`F-8`); *recomendação* = o campo `**Recomendação:**` do laudo, domínio fechado `seguir`, `seguir com ressalva`, `refazer`, `escalar` — lida do laudo, nunca derivada do veredito (`F-18`).
- **Arquivos-alvo:**
  - `.claude/tools/loop.py`
  - `tests/test_loop.py`
- **Contratos/classes:** em `.claude/tools/loop.py`:
  - `@dataclass class Revisao: status: str; veredito: str | None = None; percentual: str | None = None; bloqueante: str | None = None; laudo: str | None = None; pacote: dict | None = None; ato_de_modelo: str | None = None; sessao: str | None = None; texto: str | None = None; evidencia: str | None = None; erro: str | None = None` — `status` ∈ {`"ok"`, `"queda"`, `"invalido"`, `"falha_instrumento"`}.
  - `def caminho_evidencia(prox: Proxima) -> str | None` — plano cujo caminho, em forma POSIX, termina em `/plano.md` → `None`; `prox.linha_indice` começando por `tíquete:` → `f"docs/RDO/evidencia/{prox.plano.stem}-{prox.tarefa}.md"`; senão `f"docs/RDO/evidencia/{prox.pai}-{prox.tarefa}.md"` (`F-19`).
  - `def prompt_revisor(repo: Path, prox: Proxima, evidencia: str) -> str` — texto fixo abaixo.
  - `def interpretar_revisao(repo: Path, chamada: Chamada, tarefa: str) -> Revisao` — `queda` pelas mesmas condições de `interpretar_retorno` (com `sessao`); senão a primeira linha não vazia do `result` tem de casar `^(?P<id>\S+) (?P<veredito>aprovado|ressalva|reprovado) (?P<pct>\d+)%? bloqueante=(?P<bloq>\S+)$` com `id == tarefa`, e a linha não vazia seguinte `^laudo=(?P<laudo>\S+)$`; qualquer falha → `invalido` com `texto` = o `result`. Casou: `pacote = encerrar.ler_laudo(repo / laudo)`; `encerrar.EncerramentoError` → `invalido` com `erro = str(exc)`. O texto depois da linha do laudo, sem espaços nas pontas, vai para `ato_de_modelo` quando contém `Ato de modelo`, senão `None`. → `Revisao("ok", veredito, pct, bloq, laudo, pacote, ato_de_modelo, sessao, result)`.
  - `def revisar(repo: Path, prefixo: list[str], prox: Proxima, ref: str) -> Revisao` — roda `review_evidence.py --plano <plano> --tarefa <ID> --root <repo> --desde <ref>` mais `--out <repo>/<caminho_evidencia>` quando não é `None`; saída diferente de 0 → `Revisao("falha_instrumento", erro=<stderr>)`. A evidência citada no prompt é `caminho_evidencia(prox)` ou, sem ele, `<pasta do plano>/evidencia/<ID>.md` relativo ao repositório. Depois `chamar(prefixo, repo, prompt_revisor(...), "revisor", "opus")` e `interpretar_revisao`, com `evidencia` preenchido.
- **Texto novo, literal:** `prompt_revisor(repo, prox, evidencia)` = stdout de `backlog.py show <ID> --repo <repo>` sem espaços no fim, uma linha em branco, a linha `Evidência mecânica: <evidencia>`, uma linha em branco e este bloco (as quebras são as do bloco; `<ID>` trocado pelo id da tarefa):

  ```
  Devolva as duas linhas, nesta ordem, e nada antes delas:
  <ID> <aprovado|ressalva|reprovado> <percentual> bloqueante=<dimensão|nenhuma>
  laudo=<caminho do laudo>
  ```

- **Passos:**
  1. Acrescentar a `tests/test_loop.py` os ajudantes `_laudo` e `R` de `Testes` e os quatro testes; rodá-los vermelhos (`I-2`).
  2. Acrescentar a `.claude/tools/loop.py` o que está em `Contratos/classes`.
  3. Rodar a Verificação 1 e 2 e `python -m pytest tests/ -q`.
- **Restrições desta tarefa:** `I-1` — nenhum teste chama a rede nem um modelo (dublê da `LF-T2`); `I-2` — teste vermelho antes do código; `I-3` — o driver não decide nem redige: o prompt do revisor é o texto fixo acima e saída de instrumento, e o veredito, o percentual, o bloqueante e a recomendação são transcritos, nunca recalculados; `I-4` — a evidência sai só por `review_evidence.py`; `I-5` — nenhum instrumento muda, e `encerrar.py` é importado, nunca copiado; `I-7` — o total de `python -m pytest tests/ -q` re-medido no despacho não diminui e ganha os 4 testes novos.
- **Não fazer:** não reescrever em `loop.py` a leitura do laudo (nada de regex de `**Recomendação:**` ou de `**Veredito:**`: é `encerrar.ler_laudo`); não mudar a assinatura nem o comportamento das funções da `LF-T2`; não registrar consumo (`LF-T4`); não rotear nem fechar tarefa (`LF-T5`); não escrever `main`.
- **Contingências:**
  1. se `review_evidence.py` no repositório de teste sai diferente de 0 com a tarefa em `review` → parar e sinalizar `blocked` razão `premissa`, com o stderr.
  2. se `encerrar.ler_laudo` não existe em `.claude/tools/encerrar.py` com a assinatura `ler_laudo(caminho: Path) -> dict[str, str]` → parar e sinalizar `blocked` razão `premissa`.
  3. se `python -m pytest tests/ -q` reduz o total por teste fora de `tests/test_loop.py` → parar e sinalizar `blocked` razão `dependencia`, com o nome do teste.
- **Testes:** `tests/test_loop.py`, com o cabeçalho da `LF-T2` e estes ajudantes:
  - `_laudo(veredito, recomendacao, pct="100", bloqueante="nenhuma", pendencia="nenhuma", motivo="", tarefa="ALF-T1") -> str` — o texto (as quebras são as do bloco; os `<…>` trocados pelos parâmetros):

    ```
    # Laudo — P-0001 · <tarefa>

    **Percentual:** <pct>%
    **Veredito:** <veredito>
    **Dimensão bloqueante:** <bloqueante>
    **Recomendação:** <recomendacao>
    **Pendência:** <pendencia>

    ## Motivo das dimensões fora de conforme

    <motivo>

    ## Achado de processo

    nenhum

    ## Lições aprendidas na tarefa

    ```

  - `R(linha, laudo, extra="", tarefa="ALF-T1") -> dict` — o elemento `E(linha + f"\nlaudo=docs/RDO/laudos/P-0001-{tarefa}.md" + extra)` com `"arquivos": {f"docs/RDO/laudos/P-0001-{tarefa}.md": laudo}`.
  - Em todos: `repo = _montar_repo(tmp_path)`; `d = loop.despachar(repo, PREFIXO)`; `r = loop.revisar(repo, PREFIXO, d.prox, d.ref)`; o primeiro elemento da fila é `E("ALF-T1 review", arquivos={"a.txt": "x\n"})`.
  - `test_tf_lft3_revisao_le_veredito_e_recomendacao` — segundo elemento `R("ALF-T1 ressalva 91 bloqueante=nenhuma", _laudo("ressalva", "seguir com ressalva", pct="91"))` → `r.status == "ok"`, `r.veredito == "ressalva"`, `r.percentual == "91"`, `r.pacote["recomendacao"] == "seguir com ressalva"`, `r.ato_de_modelo is None`; `repo/"docs/RDO/evidencia/P-0001-ALF-T1.md"` existe e contém `a.txt`; a segunda chamada tem `_arg` de `--agent` = `pantonic-reviewer`, `--model` = `opus`, `--allowedTools` = `Read Glob Grep Bash`, e o prompt contém `Evidência mecânica: docs/RDO/evidencia/P-0001-ALF-T1.md` e `### ALF-T1 — Primeira tarefa do plano`.
  - `test_tf_lft3_recomendacao_vem_do_laudo` — `R("ALF-T1 aprovado 100 bloqueante=nenhuma", _laudo("aprovado", "escalar", pendencia="rever a regra"))` → `r.pacote["recomendacao"] == "escalar"` e `r.pacote["pendencia"] == "rever a regra"` (a regra concorrente, recomendação derivada do veredito `aprovado`, daria `seguir`).
  - `test_tf_lft3_ato_de_modelo_verbatim` — `R("ALF-T1 aprovado 100 bloqueante=nenhuma", _laudo("aprovado", "seguir"), extra="\n\nAto de modelo\n- Plano: docs/plans/P-0001-alfa.md\n- Ato: conflito")` → `r.ato_de_modelo == "Ato de modelo\n- Plano: docs/plans/P-0001-alfa.md\n- Ato: conflito"`.
  - `test_tr_lft3_retorno_fora_da_gramatica` — segundo elemento `E("aprovado, ficou ótimo")` → `r.status == "invalido"` e `_status(repo, "ALF-T1") == "review"`.

  Suítes: `python -m pytest tests/test_loop.py -q`; `python -m pytest tests/ -q`.
- **Verificação:**
  1. `python -c "import re,subprocess,sys;from pathlib import Path;p=Path('tests/test_loop.py');k='lft3';t=p.read_text(encoding='utf-8') if p.is_file() else '';r=subprocess.run([sys.executable,'-m','pytest',str(p),'-q','-k',k],capture_output=True,text=True).stdout if k in t else '';m=re.search('([0-9]+) passed',r);f=re.search('([0-9]+) failed',r);print(k,'passed=%s failed=%s' % (m.group(1) if m else 0,f.group(1) if f else 0))"` → antes `lft3 passed=0 failed=0`, depois `lft3 passed=4 failed=0`
  2. `python -c "from pathlib import Path;p=Path('.claude/tools/loop.py');t=p.read_text(encoding='utf-8') if p.is_file() else '';print('ler_laudo', 'ler_laudo(' in t, 'Recomendação:' in t)"` → antes `ler_laudo False False`, depois `ler_laudo True False`
- **Pronto quando:**
  - `loop de execução.quem conduz a revisão da entrega` — *o programa junta a evidência, chama o revisor e lê o veredito e o laudo, sem modelo no meio* — Verificação 1 e 2.
- **Fora do escopo desta tarefa:** o registro de consumo da chamada do revisor (`LF-T4`); a retomada da `A1` do revisor, o roteamento pelo veredito e o fechamento (`LF-T5`).

### LF-T4 — O driver registra o consumo de cada chamada pelo que o assistente devolve [Sonnet · esforço medium · classe implementacao]
- **Status:** `cancelled` · 2026-09-27 · plano P-0742 cancelado no Marco 1 (no-go do dono, 2026-09-27)
- **Depende de:** `LF-T3`
- **Objetivo:** O implementador ensina o programa a registrar o consumo de cada chamada a partir do que o próprio assistente devolve.
- **Fundamento:** `DLF-4`, `DLF-10`, `DLF-14`, `DLF-20`; `F-9`, `F-10`, `F-16`; `I-5`.
- **Operação do modelo:** `OP-4`
  - OP-4: O implementador ensina o programa a registrar o consumo de cada chamada a partir do que o próprio assistente devolve.
  - precisa de: loop de execução — Um programa em Python, sem modelo, que chama o assistente uma vez por papel — só o executor e o revisor — e grava tudo pelos programas que o kit já tem. Ele não decide, não redige e não pergunta: segue as regras de roteamento ao pé da letra, e o que foge delas ou pede consultor ou modelador encerra o loop com um relatório que traz a evidência para quem conduz; nos testes, um dublê faz o papel do assistente e nada chama a rede.; assistente sem conversa — Recebe numa linha de comando o pedido, o papel e o modelo, e devolve num bloco legível por programa a resposta, a sessão para retomar e o consumo da chamada. Este plano não o altera.; instrumentos do kit — São a única via de escrita do loop novo: ele os chama como estão e não os modifica.
- **Camada e fronteira:** kit, `.claude/tools/loop.py`: acrescenta o registro de consumo e o liga ao `despachar` (`LF-T2`) e ao `revisar` (`LF-T3`). A linha vai à série só por `telemetria.py append`, por subprocesso como os demais instrumentos (`[sys.executable, str(<repo>/".claude"/"tools"/"telemetria.py"), "append", ...]`, `cwd=<repo>`, `PYTHONIOENCODING=utf-8`). `telemetria.py` não muda: o domínio de `--fonte` é fechado em `usage`, `contado`, `nao_medido` (`F-10`), e o driver usa `usage`.
- **Domínio:** *série* = `docs/telemetria.tsv`, colunas `data`, `projeto`, `tarefa`, `modelo`, `tool_uses`, `tokens_k`, `duracao_s`, `fonte`; a linha do executor se chama `<ID>` e a do revisor `<ID>-revisao` (`F-10`); `encerrar.py tarefa` sem o trio `--tool-uses/--tokens-k/--duracao-s` fecha lendo a **última** linha `<ID>` da série (`F-9`, `encerrar.consumo_da_serie`); *chamada caída* = a de `status` `queda` nas funções da `LF-T2` e da `LF-T3` — não tem consumo medido e não gera linha.
- **Arquivos-alvo:**
  - `.claude/tools/loop.py`
  - `tests/test_loop.py`
- **Contratos/classes:** em `.claude/tools/loop.py`:
  - `CHAVES = ("result", "session_id", "num_turns", "duration_ms", "is_error")`; `CHAVES_USAGE = ("input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens")`.
  - `class ContratoIncompleto(Exception)` — `__init__(self, ausentes: list[str])`; atributo `ausentes`; `str(exc) == "chaves ausentes: " + ", ".join(ausentes)`.
  - `def chaves_ausentes(resposta: dict) -> list[str]` — as de `CHAVES` fora de `resposta`, na ordem de `CHAVES`, seguidas de `f"usage.{k}"` para cada `k` de `CHAVES_USAGE` fora de `resposta["usage"]` (todas as quatro quando `usage` falta ou não é `dict`).
  - `def registrar_consumo(repo: Path, serie: str, modelo: str, resposta: dict, data: str | None = None) -> None` — `ausentes` não vazia → `raise ContratoIncompleto(ausentes)`; senão roda `telemetria.py append --data <data ou date.today().isoformat()> --projeto <repo.resolve().name> --tarefa <serie> --modelo <modelo> --tool_uses <resposta["num_turns"]> --tokens_k <f"{soma dos quatro campos de usage / 1000:.1f}"> --duracao_s <f"{resposta['duration_ms'] / 1000:.1f}"> --fonte usage --file <repo>/docs/telemetria.tsv`; saída diferente de 0 → `raise FalhaDeInstrumento("telemetria.py append", <stderr>)`.
  - Ligação: em `despachar`, logo depois de `interpretar_retorno` e **antes** de `materializar_retorno`, quando `retorno.status != "queda"`: `registrar_consumo(repo, prox.tarefa, prox.modelo.lower(), chamada.resposta)`. Em `revisar`, logo depois da chamada e antes de `interpretar_revisao` ler o laudo, quando a chamada não é caída: `registrar_consumo(repo, f"{prox.tarefa}-revisao", "opus", chamada.resposta)`. `ContratoIncompleto` sobe sem ser capturado — nada se materializa depois dela.
- **Passos:**
  1. Acrescentar os quatro testes de `Testes` a `tests/test_loop.py` e rodá-los vermelhos (`I-2`).
  2. Acrescentar a `.claude/tools/loop.py` o que está em `Contratos/classes`.
  3. Rodar a Verificação 1 e `python -m pytest tests/ -q`.
- **Restrições desta tarefa:** `I-1` — nenhum teste chama a rede nem um modelo; `I-2` — teste vermelho antes do código; `I-4` — a série só se escreve por `telemetria.py append`, nunca abrindo o TSV; `I-5` — `telemetria.py`, `encerrar.py` e `tests/test_telemetria.py` não mudam; `I-7` — o total de `python -m pytest tests/ -q` re-medido no despacho não diminui e ganha os 4 testes novos.
- **Não fazer:** não criar valor de `--fonte` novo nem editar `telemetria.py`; não somar nem arredondar de outro jeito (uma casa decimal pelo formato `.1f`, sem `round`); não gravar linha para chamada caída; não mudar asserção existente dos testes `lft2` e `lft3`; não rotear nem fechar tarefa (`LF-T5`).
- **Contingências:**
  1. se `telemetria.py append` recusa `--fonte usage` com os valores do dublê → parar e sinalizar `blocked` razão `premissa`, com o stderr.
  2. se `encerrar.py tarefa` sem o trio sai diferente de 0 no teste `test_tf_lft4_encerrar_le_a_linha_gravada` com a linha `ALF-T1` já na série → parar e sinalizar `blocked` razão `premissa`, com o stderr.
  3. se `python -m pytest tests/ -q` reduz o total por teste fora de `tests/test_loop.py` → parar e sinalizar `blocked` razão `dependencia`, com o nome do teste.
- **Testes:** `tests/test_loop.py`, com o cabeçalho da `LF-T2` e os ajudantes `_laudo` e `R` da `LF-T3`; em todos, `repo = _montar_repo(tmp_path)` e `hoje = date.today().isoformat()`; `_serie(repo)` = as linhas de `docs/telemetria.tsv` depois do cabeçalho, cada uma partida por tabulação.
  - `test_tf_lft4_linha_por_chamada_executor_e_revisor` — fila `E("ALF-T1 review", arquivos={"a.txt": "x\n"})`, `R("ALF-T1 aprovado 100 bloqueante=nenhuma", _laudo("aprovado", "seguir"))`; `despachar` e `revisar` → `_serie(repo) == [[hoje, "repo", "ALF-T1", "sonnet", "3", "48.3", "1.5", "usage"], [hoje, "repo", "ALF-T1-revisao", "opus", "3", "48.3", "1.5", "usage"]]` (a regra concorrente, sem os dois campos de cache, daria `3.0`).
  - `test_tf_lft4_encerrar_le_a_linha_gravada` — o mesmo fluxo; depois `subprocess.run([sys.executable, str(repo/".claude"/"tools"/"encerrar.py"), "tarefa", "--plano", str(repo/"docs"/"plans"/"P-0001-alfa.md"), "--tarefa", "ALF-T1", "--repo", str(repo), "--laudo", str(repo/"docs"/"RDO"/"laudos"/"P-0001-ALF-T1.md")], capture_output=True, text=True, encoding="utf-8", env={**os.environ, "PYTHONIOENCODING": "utf-8"})` → exit 0, `_status(repo, "ALF-T1") == "done"` e `repo/"docs"/"RDO"/"P-0001-ALF-T1-primeira-tarefa-do-plano.md"` contém `48.3 k tokens`.
  - `test_tr_lft4_usage_ausente_nao_grava_nem_materializa` — fila com o elemento `E("ALF-T1 review")` sem a chave `"usage"` no `"json"` → `despachar` levanta `ContratoIncompleto` cujo `str` contém `usage.input_tokens`; `_serie(repo) == []`; `_status(repo, "ALF-T1") == "in-progress"`.
  - `test_tr_lft4_queda_nao_grava` — fila `{"stdout": "boom", "exit": 1}` → `despachar(...).retorno.status == "queda"` e `_serie(repo) == []`.

  Suítes: `python -m pytest tests/test_loop.py -q`; `python -m pytest tests/ -q`.
- **Verificação:**
  1. `python -c "import re,subprocess,sys;from pathlib import Path;p=Path('tests/test_loop.py');k='lft4';t=p.read_text(encoding='utf-8') if p.is_file() else '';r=subprocess.run([sys.executable,'-m','pytest',str(p),'-q','-k',k],capture_output=True,text=True).stdout if k in t else '';m=re.search('([0-9]+) passed',r);f=re.search('([0-9]+) failed',r);print(k,'passed=%s failed=%s' % (m.group(1) if m else 0,f.group(1) if f else 0))"` → antes `lft4 passed=0 failed=0`, depois `lft4 passed=4 failed=0`
- **Pronto quando:**
  - `loop de execução.quem registra o consumo de cada chamada` — *o programa grava uma linha por chamada, com o consumo que o próprio assistente devolve, e a tarefa fecha lendo essa linha* — Verificação 1 (`test_tf_lft4_linha_por_chamada_executor_e_revisor` e `test_tf_lft4_encerrar_le_a_linha_gravada`).
- **Fora do escopo desta tarefa:** o fechamento conduzido pelo driver e a parada `FC` diante de `ContratoIncompleto` (`LF-T5`).

### LF-T5 — O driver decide o passo seguinte pela tabela de roteamento e fecha a tarefa [Sonnet · esforço high · classe implementacao]
- **Status:** `cancelled` · 2026-09-27 · plano P-0742 cancelado no Marco 1 (no-go do dono, 2026-09-27)
- **Depende de:** `LF-T4`
- **Objetivo:** O implementador ensina o programa a decidir o passo seguinte de cada tarefa pelas regras de roteamento já escritas, fechando, refazendo ou parando com relatório.
- **Fundamento:** `DLF-1`, `DLF-6`, `DLF-7`, `DLF-10`, `DLF-12`, `DLF-15`, `DLF-16`, `DLF-21`, `DLF-22`, `DLF-23`; `F-4`, `F-5`, `F-9`, `F-16`, `F-17`, `F-18`, `F-19`; a `## 12. Roteamento do driver`, copiada abaixo.
- **Operação do modelo:** `OP-5`
  - OP-5: O implementador ensina o programa a decidir o passo seguinte de cada tarefa pelas regras de roteamento já escritas, fechando, refazendo ou parando com relatório.
  - precisa de: loop de execução — Um programa em Python, sem modelo, que chama o assistente uma vez por papel — só o executor e o revisor — e grava tudo pelos programas que o kit já tem. Ele não decide, não redige e não pergunta: segue as regras de roteamento ao pé da letra, e o que foge delas ou pede consultor ou modelador encerra o loop com um relatório que traz a evidência para quem conduz; nos testes, um dublê faz o papel do assistente e nada chama a rede.; instrumentos do kit — São a única via de escrita do loop novo: ele os chama como estão e não os modifica.
- **Camada e fronteira:** kit, `.claude/tools/loop.py` (existe desde a `LF-T2`, com revisão da `LF-T3` e consumo da `LF-T4`): acrescenta a condução — roteamento, fechamento, checkpoint, relatório e a linha de comando. Instrumentos só por subprocesso, como nas tarefas anteriores; o driver não invoca papel além de executor e revisor (`DLF-1`).
- **Domínio:** *regra* = uma linha da tabela abaixo, pelo `id`; *parada com escalada* = parada em que quem conduz despacha o consultor ou o modelador a partir do relatório (`DLF-16`); *retentativas* = contador da tarefa corrente, 0 ou 1, zerado a cada tarefa nova; *checkpoint* = `.claude/estado/loop.json`, estado de sessão ignorado pelo git (`F-11`, `I-8`).
- **Arquivos-alvo:**
  - `.claude/tools/loop.py`
  - `tests/test_loop.py`
- **Contratos/classes:** em `.claude/tools/loop.py`, sem mudar a assinatura de nada das `LF-T2` a `LF-T4`:
  - `CONDICOES: dict[str, str]` — `id` → o texto da coluna *condição* da tabela, verbatim, para as 21 linhas.
  - `def ler_checkpoint(repo: Path) -> dict | None`; `def gravar_checkpoint(repo: Path, dados: dict) -> None` (cria `.claude/estado/`, JSON em UTF-8); `def apagar_checkpoint(repo: Path) -> None`. Forma: `{"prox": {"tarefa", "titulo", "modelo", "pai", "plano" (texto), "linha_indice", "status"}, "fase": "executor" | "revisor", "ref": str, "retentativas": int, "pendencia": str | None}`; na leitura, `Proxima(**dados["prox"])` com `plano` convertido para `Path`.
  - `def fechar(repo: Path, prox: Proxima, laudo: str, pendencia: str | None) -> str` — roda o fechamento da tabela; devolve o caminho do RDO lido da linha ``Detalhe: `<caminho>`.``; saída diferente de 0 → `FalhaDeInstrumento("encerrar.py tarefa", <stderr>)`.
  - `def relatorio(repo: Path, regra: str, prox: Proxima | None, fechadas: list[tuple[str, str, str]], evidencia: str | None = None, escalada: bool = False, ato: str | None = None) -> str` — a forma do relatório abaixo; `fechadas` = `(ID, título, caminho do RDO)`.
  - `def conduzir(repo: Path, prefixo: list[str], max_tarefas: int | None = None) -> tuple[int, str]` — `(exit, relatório)`.
  - `def main(argv: list[str] | None = None) -> int` — `sys.stdout.reconfigure(encoding="utf-8")` e o mesmo para `sys.stderr`; `argparse` com `--repo` (default `KIT`) e `--max-tarefas` (`int`, default `None`); logo depois de `parse_args`, antes de qualquer outro ato, `prefixo = resolver_binario(os.environ, Path.home())` — `BinarioAusente` → imprime `str(exc)` no stderr e devolve 2; depois `conduzir`, imprime o relatório e devolve o exit dele; `KeyboardInterrupt` → imprime `loop: interrompido; checkpoint em .claude/estado/loop.json` no stderr e devolve 130, sem apagar o checkpoint. No fim do arquivo, `if __name__ == "__main__": sys.exit(main())`.
- **Texto novo, literal:** a `## 12. Roteamento do driver` do plano, copiada (as quebras são as do bloco):

  | id | fase | condição | ação do driver | desfecho |
  |---|---|---|---|---|
  | `FIM` | seleção | `backlog.py next` sai 2 (nada delegável) | nenhuma | para, exit 0 |
  | `FS` | seleção | `backlog.py next` sai 3, ou a tarefa devolvida não está `ready` e não é a tarefa `in-progress` de um checkpoint com fase `executor` | nenhuma | para, exit 1 |
  | `B3` | seleção | `modelo.py check` sai 1, ou `card_check.py` sai 1 | nenhuma; a tarefa fica `ready` | para, exit 1 |
  | `A1` | executor ou revisor | a chamada sai diferente de 0, o stdout não é objeto JSON, ou o JSON não tem `result` | com `session_id`: uma retomada por `--resume <session_id>` com o texto de retomada, e o retorno dela segue pelas linhas da mesma fase; sem `session_id`, ou caída de novo: nenhuma | para, exit 1 |
  | `FC` | executor ou revisor | o JSON tem `result` e falta alguma chave de `DLF-14` | nenhuma linha de consumo e nenhuma materialização | para, exit 1 |
  | `A2` | executor | a primeira linha não vazia do `result` está fora da gramática | um reenvio por `--resume <session_id>` com a gramática como texto; inválido de novo: nenhuma | para, exit 1 |
  | `A3a` | executor | `<ID> blocked motivo=dependencia <razão>` | `backlog.py status <ID> blocked --razao "dependencia <razão>"` | para com escalada, exit 1 |
  | `A3b` | executor | `<ID> blocked motivo=premissa <razão>` | `backlog.py status <ID> blocked --razao "premissa <razão>"` | para com escalada, exit 1 |
  | `A3c` | executor | `<ID> blocked motivo=ferramenta <razão>` | `backlog.py status <ID> blocked --razao "ferramenta <razão>"` | para com escalada, exit 1 |
  | `FR` | revisor | o `result` não traz as duas linhas da gramática do revisor, ou o laudo apontado não se lê por `encerrar.ler_laudo` | nenhuma; a tarefa fica `review` | para, exit 1 |
  | `MOD` | revisor | o `result` traz, depois das duas linhas, texto com `Ato de modelo` | nenhuma; a tarefa fica `review` | para com escalada, exit 1 |
  | `A6` | revisor | recomendação `refazer` e retentativas 0 | `backlog.py status <ID> in-progress`; executor novo, sem `--resume`, com o prompt original seguido do bloco de diretivas; retentativas passa a 1; volta à fase executor | segue |
  | `A6a` | revisor | veredito `reprovado` e recomendação `escalar` | `backlog.py status <ID> blocked --razao "premissa <pendência do laudo>"` | para com escalada, exit 1 |
  | `A7` | revisor | veredito `reprovado` e retentativas 1 | `backlog.py status <ID> blocked --razao "premissa reprovada na retentativa: <bloqueante>; <pendência do laudo>"` | para com escalada, exit 1 |
  | `A8a` | revisor | recomendação `escalar` e veredito `aprovado` ou `ressalva` | fecha a tarefa; a pendência do laudo vai ao `B1` | segue ao bloco B |
  | `A8` | revisor | recomendação `seguir com ressalva` e veredito `aprovado` ou `ressalva` | fecha a tarefa | para com escalada, exit 1 |
  | `A9` | revisor | recomendação `seguir` e veredito `aprovado` ou `ressalva` | fecha a tarefa | segue ao bloco B |
  | `B1` | bloco B | a `A8a` casou, ou a linha do executor trouxe `pendencia=` | nenhuma além do fechamento | para com escalada, exit 1 |
  | `LIM` | bloco B | tarefas fechadas no run igual a `--max-tarefas` | nenhuma | para, exit 0 |
  | `B4` | bloco B | nenhuma das anteriores | volta à seleção | segue |
  | `FORA` | qualquer | estado sem linha acima: veredito e recomendação que nenhuma linha da fase revisor casa, ou instrumento que materializa, coleta ou fecha (`backlog.py start`, `backlog.py status`, `review_evidence.py`, `telemetria.py append`, `encerrar.py tarefa`) sai diferente de 0 | nenhuma | para, exit 1 |

  Toda razão levada a `--razao` troca `—` por `-` (`F-17`). **Fecha a tarefa** = `encerrar.py tarefa --plano <plano> --tarefa <ID> --repo <repo> --laudo <repo>/<laudo>`, mais `--pendencia "<texto>"` quando a linha do executor trouxe `pendencia=`; sem `--resumo`, sem o trio de consumo e sem `encerrar.py handover` (`DLF-10`, `DLF-15`); o caminho do RDO é o da linha ``Detalhe: `<caminho>`.`` do stdout.

  Texto de retomada, uma linha: `Retome a tarefa do ponto em que parou e devolva só a linha de retorno.` A gramática do executor é `gramatica(<ID>)` e o prompt original é `montar_prompt(repo, prox)` (`LF-T2`).

  Bloco de diretivas da `A6` (`DLF-22`), apensado ao prompt original: linha em branco, a linha `Diretivas da revisão anterior`, a linha `**Pendência:** <valor do laudo>` e o corpo da seção `## Motivo das dimensões fora de conforme` do laudo até o próximo cabeçalho `## `, sem espaços nas pontas.

  Relatório, impresso no stdout em toda parada, nesta ordem, uma linha por item (as quebras são as do bloco):

    ```
    === RELATÓRIO DO LOOP
    <modelo>
    regra: <id> — <condição>
    tarefas fechadas: <n>
    - <ID> "<título>" — <caminho do RDO>
    tarefa corrente: <ID>
    evidência: <texto>
    cenário: <caminho>
    card: <ID>
    ato de modelo:
    <dossiê verbatim>
    ```

  - `<modelo>`: sem tarefa selecionada no run, `nenhuma tarefa conduzida`; senão o stdout de `modelo.py show --plano <plano da última tarefa> --root <repo>` quando sai 0, ou `sem modelo (plano anterior à doutrina)`.
  - `<condição>`: o texto da coluna *condição* da linha, como está na tabela.
  - `- <ID> …`: uma linha por tarefa fechada no run, na ordem.
  - `tarefa corrente:` em toda parada com tarefa selecionada, exceto `FIM` e `LIM`.
  - `evidência:` em toda parada, exceto `FIM` e `LIM`: `FS` — o stderr do `next`, ou `tarefa <ID> em <status> sem checkpoint`; `B3` — o texto do gate; `A1` — `exit <n>: ` e os primeiros 400 caracteres do stdout; `FC` — `chaves ausentes: <lista>`; `A2` — a linha inválida, ou `vazio`; `A3a`, `A3b`, `A3c` — a linha do executor; `FR` — o erro de leitura do laudo, ou os primeiros 400 caracteres do `result`; `MOD` — a primeira linha do revisor; `A6a` e `A7` — a pendência do laudo; `A8` — `laudo=<caminho>`; `B1` — o texto de `pendencia=` do executor, ou a pendência do laudo quando veio da `A8a`; `FORA` — o stderr do instrumento, ou `veredito <v> recomendação <r>`.
  - `cenário:` e `card:` só nas paradas com escalada (`A3a`, `A3b`, `A3c`, `MOD`, `A6a`, `A7`, `A8`, `B1`): `cenário` = `<pasta>/cenario.md` quando o plano termina em `/plano.md`, senão `docs/plans/_CENARIO-<pai>.md` (`F-19`, `DLF-16`).
  - `ato de modelo:` e o dossiê só na `MOD`.
- **Passos:**
  1. Acrescentar a `tests/test_loop.py` os ajudantes e os 23 testes de `Testes`; rodá-los vermelhos (`I-2`).
  2. Acrescentar a `.claude/tools/loop.py` `CONDICOES`, o checkpoint, `fechar`, `relatorio`, `conduzir` e `main`, com `conduzir` nesta sequência:
     - a. `fechadas = []`, `ultima = None`; checkpoint com fase `revisor` → a tarefa dele vai direto à fase revisor, com `ref`, `retentativas` e `pendencia` dele; checkpoint com fase `executor` → `retomar` = a tarefa dele.
     - b. Seleção: `despachar(repo, prefixo, retomar, antes_da_chamada=<grava checkpoint fase executor>)`; `FalhaDeInstrumento` com `instrumento == "backlog.py next"` → `FS`, outra → `FORA`; estado `vazia` → `FIM`; `fora` → `FS`; `recusada` → `B3`; `ContratoIncompleto` → `FC`.
     - c. Fase executor, sobre o `Retorno`: `queda` → `A1`; `invalido` → `A2`; `blocked` → `A3a`, `A3b` ou `A3c` pelo motivo; `review` → grava o checkpoint com fase `revisor` e segue à fase revisor. Toda nova chamada ao executor (retomada, reenvio, `A6`) passa por `chamar`, `registrar_consumo` (quando não é queda), `interpretar_retorno` e `materializar_retorno`, na ordem da `LF-T4`.
     - d. Fase revisor: `revisar`; `falha_instrumento` → `FORA`; `queda` → `A1` (retomada por `chamar(prefixo, repo, <texto de retomada>, "revisor", "opus", resume=<sessão>)`, `registrar_consumo` da série `<ID>-revisao` quando não é queda, e `interpretar_revisao`); `invalido` → `FR`; `ok` → `MOD`, `A6`, `A6a`, `A7`, `A8a`, `A8`, `A9`, `FORA`, nessa precedência.
     - e. Fechamento (`A8a`, `A8`, `A9`): `fechar`, apensa `(ID, título, RDO)` a `fechadas`, apaga o checkpoint.
     - f. Bloco B: `B1`, `LIM`, `B4`, nessa precedência; `B4` zera retentativas e pendência e volta ao passo b sem `retomar`.
     - g. Toda parada apaga o checkpoint e devolve `(exit, relatorio(...))`.
  3. Rodar a Verificação 1 a 3 e `python -m pytest tests/ -q`.
- **Restrições desta tarefa:** `I-1` — nenhum teste chama a rede nem um modelo (dublê da `LF-T2`); `I-2` — teste vermelho antes do código; `I-3` — o driver não decide nem redige: rota é linha da tabela, estado fora dela para com relatório, nenhuma pergunta a ninguém, e todo texto enviado a um papel é o fixo ou transcrito; `I-4` — o driver escreve só por instrumento (`backlog.py start` e `status`, `encerrar.py tarefa`, `telemetria.py append`, `review_evidence.py`), e o único arquivo que ele grava direto é o checkpoint; `I-5` — nenhum instrumento do kit muda; `I-6` — `GOVERNANCA.md` e `.claude/skills/scrum-master/SKILL.md` não mudam; `I-7` — o total de `python -m pytest tests/ -q` re-medido no despacho não diminui e ganha os 23 testes novos; `I-8` — o checkpoint não se versiona e o `.gitignore` não muda.
- **Não fazer:** não invocar consultor, modelador nem planejador; não escrever `B0` nem `B2` (não existem no driver, `DLF-6`, `DLF-21`); não passar `--resumo`, trio de consumo ou `encerrar.py handover`; não registrar achado `AE-<n>` no plano (quem conduz o faz a partir do relatório); não mudar a assinatura nem o comportamento das funções das `LF-T2` a `LF-T4`, nem asserção dos testes `lft2`, `lft3` e `lft4`.
- **Contingências:**
  1. se `encerrar.py tarefa` sai diferente de 0 no repositório de teste com a tarefa em `review`, o laudo gravado e a linha `<ID>` na série → parar e sinalizar `blocked` razão `premissa`, com o stderr.
  2. se `backlog.py status <ID> in-progress` sai diferente de 0 com a tarefa em `review` (caso `A6`) → parar e sinalizar `blocked` razão `premissa`, com o stderr.
  3. se `python -m pytest tests/ -q` reduz o total por teste fora de `tests/test_loop.py` → parar e sinalizar `blocked` razão `dependencia`, com o nome do teste.
- **Testes:** `tests/test_loop.py`, com o cabeçalho da `LF-T2` e os ajudantes da `LF-T3`, mais: `EA(texto)` = `E(texto, arquivos={"a.txt": "x\n"})`; `RV(v, p, b, rec, pend="nenhuma", motivo="", extra="", tarefa="ALF-T1")` = `R(f"{tarefa} {v} {p} bloqueante={b}", _laudo(v, rec, pct=p, bloqueante=b, pendencia=pend, motivo=motivo, tarefa=tarefa), extra=extra, tarefa=tarefa)`; `S` = `{"json": {"session_id": "s1", "is_error": True}, "exit": 1}`; `U` = o elemento `E("ALF-T1 review")` sem a chave `"usage"`; `RX` = `E("aprovado, ficou ótimo")`; `_regra(rel)` = a linha de `rel` que começa por `regra: `.
  - `test_tf_lft5_rota`, parametrizado por `id` (o id do caso no pytest é o `id` da linha), 21 casos. Cada caso: `repo = _montar_repo(tmp_path, **opções)`; `fila = _fila(tmp_path, monkeypatch, *elementos)`; `codigo, rel = loop.conduzir(repo, PREFIXO, max_tarefas=<m>)`; afirma `codigo == <exit>`, `_regra(rel).startswith(f"regra: {<regra>} — ")`, o status de cada tarefa listada, `len(_chamadas(fila)) == <n>` e a afirmação extra:

    | id | opções | elementos da fila | m | exit | regra | status ao fim | n | afirmação extra |
    |---|---|---|---|---|---|---|---|---|
    | `FIM` | `status_t1="review"` | nenhum | `None` | 0 | `FIM` | ALF-T1 `review` | 0 | `rel` contém `nenhuma tarefa conduzida` |
    | `FS` | `status_t1="in-progress"` | nenhum | `None` | 1 | `FS` | ALF-T1 `in-progress` | 0 | `rel` contém `evidência: tarefa ALF-T1 em in-progress sem checkpoint` |
    | `B3` | `antes_t1="nao"` | nenhum | `None` | 1 | `B3` | ALF-T1 `ready` | 0 | `rel` contém `evidência: gate do card` |
    | `A1` | nenhuma | `S`, `S` | `None` | 1 | `A1` | ALF-T1 `in-progress` | 2 | a 2ª chamada tem `--resume` igual a `s1` e prompt igual a `Retome a tarefa do ponto em que parou e devolva só a linha de retorno.` |
    | `FC` | nenhuma | `U` | `None` | 1 | `FC` | ALF-T1 `in-progress` | 1 | `rel` contém `chaves ausentes: usage.input_tokens` |
    | `A2` | nenhuma | `E("feito")`, `E("feito de novo")` | `None` | 1 | `A2` | ALF-T1 `in-progress` | 2 | a 2ª chamada tem `--resume` igual a `s1` e prompt igual a `loop.gramatica("ALF-T1")`; `rel` contém `evidência: feito de novo` |
    | `A3a` | nenhuma | `E("ALF-T1 blocked motivo=dependencia falta a tabela")` | `None` | 1 | `A3a` | ALF-T1 `blocked` | 1 | `rel` contém `cenário: docs/plans/_CENARIO-P-0001.md`, `card: ALF-T1` e `evidência: ALF-T1 blocked motivo=dependencia falta a tabela` |
    | `A3b` | nenhuma | `E("ALF-T1 blocked motivo=premissa o alvo não existe")` | `None` | 1 | `A3b` | ALF-T1 `blocked` | 1 | `rel` contém `card: ALF-T1` |
    | `A3c` | nenhuma | `E("ALF-T1 blocked motivo=ferramenta Edit negada")` | `None` | 1 | `A3c` | ALF-T1 `blocked` | 1 | `rel` contém `card: ALF-T1` |
    | `FR` | nenhuma | `EA("ALF-T1 review")`, `RX` | `None` | 1 | `FR` | ALF-T1 `review` | 2 | nenhuma |
    | `MOD` | nenhuma | `EA("ALF-T1 review")`, `RV("aprovado", "100", "nenhuma", "seguir", extra="\n\nAto de modelo\n- Ato: conflito")` | `None` | 1 | `MOD` | ALF-T1 `review` | 2 | `rel` contém `ato de modelo:` e `- Ato: conflito` |
    | `A6` | nenhuma | `EA("ALF-T1 review")`, `RV("reprovado", "40", "testes", "refazer", pend="falta o TF", motivo="testes: faltou o TF de borda")`, `E("ALF-T1 review")`, `RV("aprovado", "100", "nenhuma", "seguir")` | `None` | 0 | `FIM` | ALF-T1 `done` | 4 | a 3ª chamada não tem `--resume`, e o prompt dela contém `Diretivas da revisão anterior`, `**Pendência:** falta o TF` e `testes: faltou o TF de borda` |
    | `A6a` | nenhuma | `EA("ALF-T1 review")`, `RV("reprovado", "40", "escopo", "escalar", pend="o card pede X")` | `None` | 1 | `A6a` | ALF-T1 `blocked` | 2 | o plano contém `premissa o card pede X` |
    | `A7` | nenhuma | `EA("ALF-T1 review")`, `RV("reprovado", "40", "testes", "refazer", pend="falta o TF")`, `E("ALF-T1 review")`, `RV("reprovado", "50", "testes", "refazer", pend="de novo")` | `None` | 1 | `A7` | ALF-T1 `blocked` | 4 | o plano contém `premissa reprovada na retentativa: testes; de novo` |
    | `A8a` | nenhuma | `EA("ALF-T1 review")`, `RV("aprovado", "100", "nenhuma", "escalar", pend="rever a regra")` | `None` | 1 | `B1` | ALF-T1 `done` | 2 | `rel` contém `evidência: rever a regra` |
    | `A8` | nenhuma | `EA("ALF-T1 review")`, `RV("ressalva", "91", "nenhuma", "seguir com ressalva", pend="o ramo vazio")` | `None` | 1 | `A8` | ALF-T1 `done` | 2 | `rel` contém `evidência: laudo=docs/RDO/laudos/P-0001-ALF-T1.md` |
    | `A9` | nenhuma | `EA("ALF-T1 review")`, `RV("aprovado", "100", "nenhuma", "seguir")` | `None` | 0 | `FIM` | ALF-T1 `done` | 2 | `repo/".claude"/"estado"/"loop.json"` não existe |
    | `B1` | nenhuma | `EA("ALF-T1 review pendencia=o teste de borda ficou de fora")`, `RV("aprovado", "100", "nenhuma", "seguir")` | `None` | 1 | `B1` | ALF-T1 `done` | 2 | `rel` contém `evidência: o teste de borda ficou de fora` |
    | `LIM` | `duas_tarefas=True` | `EA("ALF-T1 review")`, `RV("aprovado", "100", "nenhuma", "seguir")` | 1 | 0 | `LIM` | ALF-T1 `done`, ALF-T2 `ready` | 2 | nenhuma |
    | `B4` | `duas_tarefas=True` | `EA("ALF-T1 review")`, `RV("aprovado", "100", "nenhuma", "seguir")`, `E("ALF-T2 review", arquivos={"b.txt": "y\n"})`, `RV("aprovado", "100", "nenhuma", "seguir", tarefa="ALF-T2")` | `None` | 0 | `FIM` | ALF-T1 `done`, ALF-T2 `done` | 4 | `rel` contém `tarefas fechadas: 2` |
    | `FORA` | nenhuma | `EA("ALF-T1 review")`, `RV("reprovado", "40", "testes", "seguir")` | `None` | 1 | `FORA` | ALF-T1 `review` | 2 | `rel` contém `evidência: veredito reprovado recomendação seguir` |

  - `test_tf_lft5_relatorio_lista_tarefa_fechada` — o caso `A9` → `rel` contém `sem modelo (plano anterior à doutrina)`, `tarefas fechadas: 1` e `- ALF-T1 "Primeira tarefa do plano" — docs/RDO/P-0001-ALF-T1-primeira-tarefa-do-plano.md`.
  - `test_tf_lft5_checkpoint_retoma_revisao` — `_montar_repo(tmp_path, status_t1="review")`; grava `repo/.claude/estado/loop.json` com `{"prox": {"tarefa": "ALF-T1", "titulo": "Primeira tarefa do plano", "modelo": "Sonnet", "pai": "P-0001", "plano": str(repo/"docs"/"plans"/"P-0001-alfa.md"), "linha_indice": "plano: P-0001 — Plano alfa (0/1) · residência: docs/plans/P-0001-alfa.md:1-19 · índice: docs/plans/P-0001-alfa.md", "status": "review"}, "fase": "revisor", "ref": <stdout de git rev-parse HEAD no repo>, "retentativas": 0, "pendencia": None}`; fila `RV("aprovado", "100", "nenhuma", "seguir")` → `codigo == 0`, regra `FIM`, `_status == "done"`, uma chamada, com `--agent` igual a `pantonic-reviewer`, e `loop.json` não existe (a regra concorrente, sem ler o checkpoint, iria ao `next`, que não devolve tarefa em `review`: `FIM` com 0 chamadas e a tarefa em `review`).

  Suítes: `python -m pytest tests/test_loop.py -q`; `python -m pytest tests/ -q`.
- **Verificação:**
  1. `python -c "import re,subprocess,sys;from pathlib import Path;p=Path('tests/test_loop.py');k='lft5';t=p.read_text(encoding='utf-8') if p.is_file() else '';r=subprocess.run([sys.executable,'-m','pytest',str(p),'-q','-k',k],capture_output=True,text=True).stdout if k in t else '';m=re.search('([0-9]+) passed',r);f=re.search('([0-9]+) failed',r);print(k,'passed=%s failed=%s' % (m.group(1) if m else 0,f.group(1) if f else 0))"` → antes `lft5 passed=0 failed=0`, depois `lft5 passed=23 failed=0`
  2. `python -c "import subprocess,sys;from pathlib import Path;t=Path('.claude/tools/loop.py');s=t.read_text(encoding='utf-8') if t.is_file() else '';r=subprocess.run([sys.executable,str(t),'--help'],capture_output=True,text=True) if 'def main(' in s else None;print('cli', r.returncode if r else '-', bool(r) and '--max-tarefas' in r.stdout)"` → antes `cli - False`, depois `cli 0 True`
  3. `python -c "import os,subprocess,sys,tempfile;from pathlib import Path;t=Path('.claude/tools/loop.py');s=t.read_text(encoding='utf-8') if t.is_file() else '';d=tempfile.mkdtemp();e={k:v for k,v in os.environ.items() if k!='PANTONIC_CLAUDE_BIN'};e.update(USERPROFILE=d,HOME=d);r=subprocess.run([sys.executable,str(t)],capture_output=True,text=True,encoding='utf-8',env=e) if 'def main(' in s else None;print('ausente', r.returncode if r else '-', bool(r) and 'loop: binário do claude ausente (PANTONIC_CLAUDE_BIN)' in r.stderr)"` → antes `ausente - False`, depois `ausente 2 True`
- **Pronto quando:**
  - `loop de execução.quem decide o passo seguinte` — *o programa aplica as mesmas regras, transcritas uma a uma: fecha a tarefa aprovada, manda refazer a reprovada e para com relatório em tudo que pede consultor, modelador ou foge da tabela* — Verificação 1, 2 e 3.
- **Fora do escopo desta tarefa:** rodar o driver contra a fila real (`LF-T6`); a norma e a porta de entrada (`LF-T7`, `LF-T8`); as rotas do consultor e do modelador dentro do driver (`## 7`).

### LF-T6 — O piloto conduz pelo driver até cinco tarefas reais e mede o custo de cada uma [Sonnet + dono · esforço medium · classe investigacao]
- **Status:** `cancelled` · 2026-09-27 · plano P-0742 cancelado no Marco 1 (no-go do dono, 2026-09-27)
- **Depende de:** `LF-T5`
- **Objetivo:** O investigador mede, conduzindo pelo programa até cinco tarefas reais da fila, o custo de cada uma contra a série do loop em conversa.
- **Fundamento:** `DLF-10`, `DLF-17`, `DLF-18`, `DLF-19`, `DLF-23`; `F-10`, `F-15`; a `## 12` (regras e relatório); `_VIABILIDADE-agente-leitor.md` §7.1 como série de referência (`## 0`).
- **Operação do modelo:** `OP-6`
  - OP-6: O investigador mede, conduzindo pelo programa até cinco tarefas reais da fila, o custo de cada uma contra a série do loop em conversa.
  - precisa de: loop de execução — Um programa em Python, sem modelo, que chama o assistente uma vez por papel — só o executor e o revisor — e grava tudo pelos programas que o kit já tem. Ele não decide, não redige e não pergunta: segue as regras de roteamento ao pé da letra, e o que foge delas ou pede consultor ou modelador encerra o loop com um relatório que traz a evidência para quem conduz; nos testes, um dublê faz o papel do assistente e nada chama a rede.; tarefa conduzida pelo loop — Nenhuma operação deste plano altera uma tarefa; o que se observa nela, antes e depois, é quanto custa conduzi-la.
- **Camada e fronteira:** medição no repositório real: o driver `.claude/tools/loop.py` roda uma vez sobre a fila que `backlog.py next` devolver no dia (`DLF-18`), e o resultado vai para a `## 11. Piloto medido` deste plano. O driver escreve, pelos instrumentos, nos planos e no diário das tarefas que conduzir, em `docs/telemetria.tsv` e em `docs/RDO/` — efeito da medida, não matéria deste card. Nenhum código muda.
- **Domínio:** *tarefa conduzida* = tarefa que o driver selecionou no run: as linhas `- <ID> …` do relatório (fechadas) e a linha `tarefa corrente: <ID>` (a da parada); *custo por tarefa* = soma de `tokens_k` das linhas `<ID>` (executor) e `<ID>-revisao` (revisor) que o run apensou a `docs/telemetria.tsv`; *orquestração* = 0 por construção (o driver não chama modelo); *série de referência* = o loop em conversa, `$2–6` por tarefa de orquestração e 7–13 turnos do orquestrador por despacho (`docs/plans/_VIABILIDADE-agente-leitor.md` §7.1, citada na `## 0`).
- **Arquivos-alvo:**
  - `docs/plans/P-0742-loop-fora-do-llm.md`
- **Método de sondagem:**
  1. Rodar `python .claude/tools/backlog.py next` e ler a primeira linha (contingências 1 e 2).
  2. Contar as linhas de `docs/telemetria.tsv` (`<L0>`).
  3. Rodar, na raiz do repositório, pela ferramenta `Bash` com execução em segundo plano, `python .claude/tools/loop.py --max-tarefas 5`, com stdout e stderr redirecionados para `%TEMP%\claude\lf-t6\loop.log`; esperar o fim do processo e anotar o exit.
  4. Ler do log só o bloco que começa em `=== RELATÓRIO DO LOOP` (≤ 40 linhas no contexto): a regra da linha `regra:`, os ids das linhas `- <ID> …` e o da linha `tarefa corrente:`.
  5. Ler as linhas de `docs/telemetria.tsv` depois da `<L0>` e, por tarefa conduzida, somar `tokens_k` da série `<ID>` e da série `<ID>-revisao` e contar as linhas das duas.
  6. Escrever na `## 11. Piloto medido`, logo abaixo do parágrafo que já está lá e separada dele por uma linha em branco, a tabela com este cabeçalho, verbatim (as quebras são as do bloco), e uma linha por tarefa conduzida, na ordem do relatório, cuja primeira célula é `piloto-1`, `piloto-2` e assim por diante:

     ```
     | piloto | tarefa | desfecho | tokens_k do executor | tokens_k do revisor | tokens_k da orquestração | chamadas |
     |---|---|---|---|---|---|---|
     ```

     Célula a célula: *desfecho* = `done` para tarefa fechada, ou o id da regra de parada para a tarefa corrente; *tokens_k* com uma casa decimal; *tokens_k da orquestração* = `0`; *chamadas* = o número de linhas das duas séries. Sem tarefa conduzida, uma linha só: `| piloto-0 | nenhuma | <regra> | 0 | 0 | 0 | 0 |`.
  7. Abaixo da tabela, separadas por uma linha em branco, duas linhas: `Tarefas fechadas: <n> de 5 · regra que encerrou: <id> · exit <código> · <data AAAA-MM-DD>` e `Referência do loop em conversa (docs/plans/_VIABILIDADE-agente-leitor.md §7.1): orquestração de $2–6 por tarefa, 7–13 turnos do orquestrador por despacho.`
- **Restrições desta tarefa:** o driver roda uma vez só, com `--max-tarefas 5` (`DLF-18`), e nenhuma tarefa é escolhida à mão; nenhum código do kit muda (`I-5`, `I-6`); nenhum número da tabela sai de estimativa — vem do relatório e da série; o relatório do driver não se copia para o plano além da tabela e das duas linhas.
- **Não fazer:** não editar `docs/telemetria.tsv`, planos, diário ou RDO à mão; não rodar o driver de novo para completar cinco tarefas; não mudar a diretiva de priorização (ato do dono); não despachar o consultor nem o modelador diante da parada do driver.
- **Contingências:**
  1. se a primeira linha do `next` do passo 1 é `=== PRÓXIMA TAREFA: LF-T` seguida de um número → parar e sinalizar `blocked` razão `dependencia`: o piloto precisa de outra tarefa à frente da fila, e a diretiva de priorização é ato do dono.
  2. se o `next` do passo 1 sai 2 (nada delegável) → não rodar o driver; escrever a linha `| piloto-0 | nenhuma | FIM | 0 | 0 | 0 | 0 |` e as duas linhas do passo 7 com `Tarefas fechadas: 0 de 5 · regra que encerrou: FIM · exit 0`, e seguir para a Verificação.
  3. se o driver sai 2 → parar e sinalizar `blocked` razão `premissa`, com a linha do stderr.
  4. se a ferramenta `Bash` recusa a execução em segundo plano → parar e sinalizar `blocked` razão `ferramenta`, com a linha literal da recusa.
  5. se o driver para por regra diferente de `FIM` e de `LIM` → escrever a tabela com a regra na coluna *desfecho* da tarefa corrente e devolver `LF-T6 review pendencia=o driver parou em <regra> na tarefa <ID>; relatório em %TEMP%\claude\lf-t6\loop.log`.
- **Testes:** nenhum teste novo; nenhuma suíte a rodar (nenhum código muda).
- **Verificação:**
  1. `python -c "from pathlib import Path;L=Path('docs/plans/P-0742-loop-fora-do-llm.md').read_text(encoding='utf-8').splitlines();i=L.index('## 11. Piloto medido');j=L.index('## 12. Roteamento do driver');r=[l for l in L[i:j] if l.startswith('| piloto-')];print('piloto', len(r)>0, all(len([c for c in l.strip().strip('|').split('|') if c.strip()])==7 for l in r))"` → antes `piloto False True`, depois `piloto True True`
- **Pronto quando (o fato que tem de existir ao final):**
  - `loop de execução.prova em plano real` — *o programa conduziu até cinco tarefas da fila real, e o custo de cada uma está registrado ao lado da série do loop em conversa, para o dono julgar* — Verificação 1. O julgamento do dono é o gate do Marco 2 e vai ao relatório de encerramento, não a este critério.
- **Fora do escopo desta tarefa:** a triagem das paradas do driver (quem conduz, pela pendência devolvida); a norma (`LF-T7`); a porta de entrada (`LF-T8`).

### LF-T7 — A norma diz que o loop mora no driver [Sonnet · esforço low · classe redacao]
- **Status:** `cancelled` · 2026-09-27 · plano P-0742 cancelado no Marco 1 (no-go do dono, 2026-09-27)
- **Depende de:** `LF-T6`
- **Objetivo:** O redator da norma declara que o loop de execução mora no programa, e não mais na conversa principal.
- **Fundamento:** `DLF-7`, `DLF-21`; `F-13`; `I-6`; o piloto da `## 11`.
- **Operação do modelo:** `OP-7`
  - OP-7: O redator da norma declara que o loop de execução mora no programa, e não mais na conversa principal.
  - precisa de: loop de execução — Um programa em Python, sem modelo, que chama o assistente uma vez por papel — só o executor e o revisor — e grava tudo pelos programas que o kit já tem. Ele não decide, não redige e não pergunta: segue as regras de roteamento ao pé da letra, e o que foge delas ou pede consultor ou modelador encerra o loop com um relatório que traz a evidência para quem conduz; nos testes, um dublê faz o papel do assistente e nada chama a rede.
- **Camada e fronteira:** doutrina: uma célula da matriz de papéis de `GOVERNANCA.md` §3 (linha *Orquestração*, coluna do modelo) e um parágrafo novo no topo de `.claude/skills/scrum-master/SKILL.md`. Nenhum código, nenhum teste, nenhuma outra linha desses arquivos.
- **Domínio:** *norma* = `GOVERNANCA.md` e a skill `scrum-master`; *condução à mão* = o loop rodado pela conversa principal, como a skill descreve do passo 1 ao 10.
- **Arquivos-alvo:**
  - `GOVERNANCA.md:93` — `| **Orquestração** |`
  - `.claude/skills/scrum-master/SKILL.md:6` — `# scrum-master — o loop de execução de um plano`
- **Texto novo, literal:**
  - Em `GOVERNANCA.md:93`, trocar este trecho da segunda célula (sem quebra nova e sem refluxo):

    ```
    Melhor custo-benefício (Sonnet); o loop roda no contexto principal, onde o dono interrompe sem derrubar a sessão, e **nunca para para rebaixar o modelo**, porque só orquestra e o modelo de cada tarefa viaja no despacho; para para pedir `/model` só quando o modelo ativo está abaixo do que a fase exige
    ```

    por este (sem quebra nova e sem refluxo):

    ```
    Nenhum: o loop mora no driver `.claude/tools/loop.py`, um programa sem modelo que despacha executor e revisor por `claude -p` e escreve só pelos instrumentos do kit; o dono o interrompe pelo teclado (`Ctrl-C`), e o driver retoma pela próxima tarefa do `backlog.py next`. Conduzir o loop à mão, no contexto principal, é recurso de exceção: roda em Sonnet, **nunca para para rebaixar o modelo**, porque só orquestra e o modelo de cada tarefa viaja no despacho, e para para pedir `/model` só quando o modelo ativo está abaixo do que a fase exige
    ```

  - Em `.claude/skills/scrum-master/SKILL.md`, depois da linha 6 e da linha em branco que a segue, antes da linha que começa por `Procedimento de **Orquestração**`, inserir este parágrafo seguido de uma linha em branco (as quebras são as do bloco):

    ```
    **O loop mora no driver.** `python .claude/tools/loop.py` conduz a fila sem modelo: pega a próxima tarefa do `backlog.py next`, despacha executor e revisor por `claude -p`, aplica as tabelas de roteamento desta skill transcritas em código (`docs/plans/P-0742-loop-fora-do-llm.md`, seção 12) e escreve só pelos instrumentos do kit; o dono o interrompe pelo teclado (`Ctrl-C`). Esta skill é a especificação do driver e o procedimento da condução à mão, que é recurso de exceção.
    ```

- **Passos:**
  1. Conferir a contingência 1 na `## 11. Piloto medido` deste plano.
  2. Aplicar as duas edições de `Texto novo, literal`.
  3. Rodar a Verificação 1 e 2, `python .claude/tools/materializar.py check` e `python -m pytest tests/ -q`.
- **Restrições desta tarefa:** `I-6` — esta é a tarefa de doutrina, depois do piloto; nenhuma outra linha de `GOVERNANCA.md` nem da skill muda; `I-7` — o total de `python -m pytest tests/ -q` re-medido no despacho não diminui; `python .claude/tools/materializar.py check` segue saindo 0 (medido 0 em 2026-09-26).
- **Não fazer:** não mexer em `GOVERNANCA.md` §4.3, na descrição do frontmatter da skill, nos passos 1 a 10 nem nas tabelas de roteamento da skill; não editar `README.md` (é a `LF-T8`); não editar `docs/DOC_MAP.md`.
- **Contingências:**
  1. se a `## 11. Piloto medido` não tem nenhuma linha `| piloto-` com `done` na coluna *desfecho* → parar e sinalizar `blocked` razão `premissa`: a norma não declara que o loop mora num driver que não fechou tarefa real.
  2. se o trecho antigo não está na linha 93 de `GOVERNANCA.md` → localizar a linha que começa por `| **Orquestração** |` e aplicar nela; se nenhuma linha começa assim → parar e sinalizar `blocked` razão `premissa`.
  3. se `python -m pytest tests/ -q` falha em teste que afirma o texto antigo da linha *Orquestração* → parar e sinalizar `blocked` razão `premissa`, com o nome do teste.
  4. se `python .claude/tools/materializar.py check` sai diferente de 0 depois da edição → parar e sinalizar `blocked` razão `premissa`, com o stderr.
- **Testes:** nenhum teste novo. Suítes de regressão: `python -m pytest tests/ -q`; `python .claude/tools/materializar.py check`.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('GOVERNANCA.md').read_text(encoding='utf-8');print('novo',t.count('Nenhum: o loop mora no driver'),'velho',t.count('o loop roda no contexto principal, onde o dono interrompe sem derrubar a sessão'))"` → antes `novo 0 velho 1`, depois `novo 1 velho 0`
  2. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('skill',t.count('O loop mora no driver.'))"` → antes `skill 0`, depois `skill 1`
- **Pronto quando:**
  - `loop de execução.onde a norma diz que ele mora` — *a norma diz que o loop mora no programa, que o dono o interrompe pelo teclado e que conduzir à mão é recurso de exceção* — Verificação 1 e 2.
- **Fora do escopo desta tarefa:** a porta de entrada (`LF-T8`); reescrever a skill como especificação linha a linha do driver.

### LF-T8 — A porta de entrada apresenta o loop conduzido pelo driver [Sonnet + dono · esforço low · classe redacao]
- **Status:** `cancelled` · 2026-09-27 · plano P-0742 cancelado no Marco 1 (no-go do dono, 2026-09-27)
- **Depende de:** `LF-T7`
- **Objetivo:** O mantenedor revisa a apresentação do repositório contra o estado em que o plano deixa o loop, para o aceite do dono.
- **Fundamento:** `G-README` dever 2 (`GOVERNANCA.md` §7 item 14); o piloto da `## 11`; a norma da `LF-T7`.
- **Operação do modelo:** `OP-8`
  - OP-8: O mantenedor revisa a apresentação do repositório contra o estado em que o plano deixa o loop, para o aceite do dono.
  - precisa de: loop de execução — Um programa em Python, sem modelo, que chama o assistente uma vez por papel — só o executor e o revisor — e grava tudo pelos programas que o kit já tem. Ele não decide, não redige e não pergunta: segue as regras de roteamento ao pé da letra, e o que foge delas ou pede consultor ou modelador encerra o loop com um relatório que traz a evidência para quem conduz; nos testes, um dublê faz o papel do assistente e nada chama a rede.
- **Camada e fronteira:** documentação pública: um parágrafo novo na seção `## 6. O loop de execução` do `README.md`. Nenhum outro arquivo.
- **Domínio:** *porta de entrada* = o `README.md`; *gerente* = o dono, como o `README.md` o chama.
- **Arquivos-alvo:**
  - `README.md:479` — `passo, como último desempate.`
- **Texto novo, literal:** depois da linha 479 do `README.md` (a que termina o parágrafo **O que é.** da `## 6`), inserir uma linha em branco e este parágrafo, antes da linha em branco que precede `**Passo 1 — drenar os dois inboxes`; o parágrafo é uma linha só (sem quebra nova e sem refluxo):

  ```
  **Pelo driver.** Desde o plano "O loop sai do LLM" (`P-0742`), o loop mora no driver `python .claude/tools/loop.py`: um programa sem modelo que pega a próxima tarefa do `backlog.py next`, despacha executor e revisor por `claude -p`, aplica as tabelas de roteamento da `scrum-master` transcritas em código e escreve só pelos instrumentos do kit, de modo que o loop não paga modelo para orquestrar. O gerente o interrompe pelo teclado (`Ctrl-C`) e lê, na parada, o relatório que ele imprime; conduzir a janela à mão, como nos passos abaixo, é recurso de exceção. O custo medido no piloto está na seção 11, "Piloto medido", do plano.
  ```

- **Passos:**
  1. Inserir o parágrafo de `Texto novo, literal`.
  2. Rodar a Verificação 1 e `pwsh -NoProfile -File .claude/checks/check-readme.ps1`.
- **Restrições desta tarefa:** só o `README.md` muda, e só com o parágrafo acima; `pwsh -NoProfile -File .claude/checks/check-readme.ps1` segue saindo 0 (medido 0 em 2026-09-26, `check-readme: OK - 10 agente(s), 13 skill(s), 20 guardrail(s)`).
- **Não fazer:** não reescrever os passos 1 a 5 da `## 6`, a tabela de skills nem a de guardrails; não mudar contagem de agentes, skills ou guardrails; não editar `GOVERNANCA.md` nem a skill `scrum-master`.
- **Contingências:**
  1. se a linha 479 do `README.md` não é `passo, como último desempate.` → localizar essa linha dentro da `## 6. O loop de execução` e inserir depois dela; se ela não existe → parar e sinalizar `blocked` razão `premissa`.
  2. se `pwsh -NoProfile -File .claude/checks/check-readme.ps1` sai diferente de 0 depois da edição → parar e sinalizar `blocked` razão `premissa`, com a linha impressa.
- **Testes:** nenhum teste novo. Guarda: `pwsh -NoProfile -File .claude/checks/check-readme.ps1`.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('README.md').read_text(encoding='utf-8');print('readme',t.count('Pelo driver.'),t.count('o loop mora no driver'))"` → antes `readme 0 0`, depois `readme 1 1`
- **Pronto quando:**
  - `loop de execução.como a porta de entrada o apresenta` — *a apresentação do repositório descreve o loop conduzido pelo programa, revisada contra o estado real e aceita pelo dono* — Verificação 1; o aceite do dono é o gate do Marco 2 e vai ao relatório de encerramento, não a este critério.
- **Fora do escopo desta tarefa:** propagar o driver aos kits derivados; reescrever a `## 6` inteira para o driver.

## 6. Ordem de execução

Fila única, sequencial: cada card depende do anterior na ordem das operações da `### 1.2`, e nada roda em paralelo. A sonda do contrato headless precede toda implementação (o driver e o stub são escritos contra `DLF-13` e `DLF-14`, que ela confirma); o piloto precede a doutrina; a revisão do `README.md` fecha o plano.

## 7. Fora de escopo (explícito)

- O driver invocar o consultor, o modelador ou o planejador (`DLF-1`): a triagem continua com quem conduz, a partir do relatório de parada (`DLF-16`); sem residência hoje — nasce por decisão do dono depois do Marco 2.
- Handover e resumo redigidos pelo driver (`DLF-15`).
- O modelo conceitual do plano como interface dono↔loop (`P-0741`): o driver consome o plano pela gramática do `P-0739`; o que o modelo acrescenta é lido pelos papéis, não pelo driver.
- Restringir a lista de ferramentas do executor além de `DLF-13` (`TK-60`).
- Mudar os instrumentos que o driver consome (`I-5`).
- `B0` no driver, a atribuição de `pendencia=` a arquivo fora dos alvos (`DLF-21`): toda `pendencia=` para em `B1`; sem residência hoje.

## 8. Riscos

- **Hooks em `-p`:** se a sonda medir linha nova em `docs/telemetria.tsv` gravada pelo hook `SubagentStop` numa chamada `-p`, a telemetria de `DLF-10` duplicaria → a sonda sai `blocked` razão `premissa` com a medida, e a triagem decide antes de qualquer implementação. O `PreToolUse` de `ocupacao.py` disparando dentro do papel é inofensivo (mede o contexto do papel).
- **Permissões:** se a sonda medir `Edit` ou `Bash` negados com a linha de comando de `DLF-13` → `blocked` razão `premissa`, com a linha literal da recusa; o modo de permissão nasce como decisão na triagem, com o valor medido.
- **Contrato do JSON:** chave de `DLF-14` ausente na saída real → a sonda sai `blocked` razão `premissa`, com as chaves medidas.
- **Extensão atualizada no meio do plano:** `DLF-9` resolve a pasta de maior versão no momento da chamada; nada a fazer.
- **Fila do piloto com menos de 5 tarefas:** o piloto registra o número alcançado (`DLF-18`) e o Marco 2 julga com ele.
- **Cache de prompt:** cada papel nasce frio (prefixo 17–37k reescrito a cada chamada), igual ao regime atual de subagentes; o ganho vem de zerar o contexto do orquestrador.
- **Sessão aninhada:** se a sonda medir recusa por sessão aninhada mesmo com o ambiente de `DLF-19` → o `LF-T1` sai `blocked` razão `premissa` (contingência 2 dele), com a linha literal.
- **Piloto selecionando o próprio plano:** se o `next` do dia do piloto devolver um card `LF-T<n>` → o `LF-T6` sai `blocked` razão `dependencia` (contingência 1 dele): a diretiva de priorização é ato do dono.

## 9. Achados da execução

- **RP-1** (`TK-90b`, rodada de replanejamento, 2026-09-26) — retomada pela decisão do dono *"Retomar"* (2026-09-26, `TK-90b`). **Classificação:** técnica e tática: nenhuma decisão do dono mudou e o objetivo do plano é o mesmo. O plano ganhou a `## 1. Modelo conceitual` (modelador, versão 1, oito operações) e os oito cards foram reescritos um por operação, com o campo `Operação do modelo` e a `Verificação` na forma que `card_check.py` lê. Em relação aos cards de 2026-09-19: a ordem das operações 4 e 5 inverteu (o registro de consumo vem antes do roteamento com fechamento, que lê a linha gravada); o card antigo que mandava `telemetria.py` aceitar `fonte=json` saiu, por contradizer `I-5` e `DLF-10`; o piloto segue `DLF-18` (a fila do `next` do dia, até 5 tarefas) e não mais "≥ 5 tarefas de plano escolhido pelo dono". Decisões novas `DLF-19` a `DLF-23`; fatos novos `F-15` a `F-20`; residência nova `## 12. Roteamento do driver`. **Causa-raiz na autoria:** o plano de 2026-09-19 nasceu antes da doutrina do modelo e da forma normativa da `Verificação` (`docs/RUBRICA_DE_REVISAO.md` `### 8.1`): cards em prosa, sem valor medido antes, com remissões a seções depois renumeradas; e a fase 1 não pediu o ensaio da cadeia de instrumentos num repositório sintético (agora `F-16`), de que os testes do driver dependem. **Verificação que teria evitado:** `card_check.py --plano <plano> --tarefa <ID>` exit 0 por card antes de gravar e o ensaio da fase 4, item 14, do planejador. Classe de erro já coberta pelo protocolo do planejador: só esta entrada.

- **Marco 1** (dono, 2026-09-27) — **no-go**; plano `cancelled`, nada executado, os oito cards `cancelled`. Veredito verbatim: *"Eu não concordo em tirar o agente scrum-master do loop, acho que é necessário algum nível de julgamento no processo, pois a orquestração de multiplos agentes eventualmente requer tratar diversos casos  não padronizados ainda. O que eu concordo é que pode existir potencial para ganhor mecanizado ações mecânicas do scrum-master ou otimizar as rotinas dele. Mas essas tarefas podem ser herdadas no plano de auditoria. Deixe registrado na spec do plano de auditoria essa matéria de avaliação, e encerre este plano"* A matéria de avaliação foi para a auditoria final como `AE-95` (`docs/DIARIO_DE_OBRAS.md`, bloco de fechamento do `P-0742`).

## 10. Contrato headless

Residência do contrato medido pela sonda (`DLF-17`): uma tabela com os fatos medidos por chamada — chaves do JSON de saída, exit code, hooks que disparam, ferramentas aceitas ou negadas, duração. Nasce vazia; a escreve a operação que sonda o contrato.

## 11. Piloto medido

Residência do piloto (`DLF-17`): custo por tarefa (execução + revisão + orquestração) contra a série de `docs/telemetria.tsv` e o `_VIABILIDADE` §7.1 (orquestração $2–6 por tarefa no loop em LLM). Nasce vazia; a escreve a operação do piloto.

## 12. Roteamento do driver

Residência única (`DLF-21`, `DLF-22`, `DLF-23`) da tabela de roteamento do driver, dos textos fixos que ele envia e da forma do relatório que ele imprime. O card `LF-T5` copia esta seção inteira; o `LF-T2` copia a gramática do executor e o `LF-T3` o texto do revisor. A tabela vale por fase, de cima para baixo: dentro da fase, a primeira linha que casa vence.

| id | fase | condição | ação do driver | desfecho |
|---|---|---|---|---|
| `FIM` | seleção | `backlog.py next` sai 2 (nada delegável) | nenhuma | para, exit 0 |
| `FS` | seleção | `backlog.py next` sai 3, ou a tarefa devolvida não está `ready` e não é a tarefa `in-progress` de um checkpoint com fase `executor` | nenhuma | para, exit 1 |
| `B3` | seleção | `modelo.py check` sai 1, ou `card_check.py` sai 1 | nenhuma; a tarefa fica `ready` | para, exit 1 |
| `A1` | executor ou revisor | a chamada sai diferente de 0, o stdout não é objeto JSON, ou o JSON não tem `result` | com `session_id`: uma retomada por `--resume <session_id>` com o texto de retomada, e o retorno dela segue pelas linhas da mesma fase; sem `session_id`, ou caída de novo: nenhuma | para, exit 1 |
| `FC` | executor ou revisor | o JSON tem `result` e falta alguma chave de `DLF-14` | nenhuma linha de consumo e nenhuma materialização | para, exit 1 |
| `A2` | executor | a primeira linha não vazia do `result` está fora da gramática | um reenvio por `--resume <session_id>` com a gramática como texto; inválido de novo: nenhuma | para, exit 1 |
| `A3a` | executor | `<ID> blocked motivo=dependencia <razão>` | `backlog.py status <ID> blocked --razao "dependencia <razão>"` | para com escalada, exit 1 |
| `A3b` | executor | `<ID> blocked motivo=premissa <razão>` | `backlog.py status <ID> blocked --razao "premissa <razão>"` | para com escalada, exit 1 |
| `A3c` | executor | `<ID> blocked motivo=ferramenta <razão>` | `backlog.py status <ID> blocked --razao "ferramenta <razão>"` | para com escalada, exit 1 |
| `FR` | revisor | o `result` não traz as duas linhas da gramática do revisor, ou o laudo apontado não se lê por `encerrar.ler_laudo` | nenhuma; a tarefa fica `review` | para, exit 1 |
| `MOD` | revisor | o `result` traz, depois das duas linhas, texto com `Ato de modelo` | nenhuma; a tarefa fica `review` | para com escalada, exit 1 |
| `A6` | revisor | recomendação `refazer` e retentativas 0 | `backlog.py status <ID> in-progress`; executor novo, sem `--resume`, com o prompt original seguido do bloco de diretivas; retentativas passa a 1; volta à fase executor | segue |
| `A6a` | revisor | veredito `reprovado` e recomendação `escalar` | `backlog.py status <ID> blocked --razao "premissa <pendência do laudo>"` | para com escalada, exit 1 |
| `A7` | revisor | veredito `reprovado` e retentativas 1 | `backlog.py status <ID> blocked --razao "premissa reprovada na retentativa: <bloqueante>; <pendência do laudo>"` | para com escalada, exit 1 |
| `A8a` | revisor | recomendação `escalar` e veredito `aprovado` ou `ressalva` | fecha a tarefa; a pendência do laudo vai ao `B1` | segue ao bloco B |
| `A8` | revisor | recomendação `seguir com ressalva` e veredito `aprovado` ou `ressalva` | fecha a tarefa | para com escalada, exit 1 |
| `A9` | revisor | recomendação `seguir` e veredito `aprovado` ou `ressalva` | fecha a tarefa | segue ao bloco B |
| `B1` | bloco B | a `A8a` casou, ou a linha do executor trouxe `pendencia=` | nenhuma além do fechamento | para com escalada, exit 1 |
| `LIM` | bloco B | tarefas fechadas no run igual a `--max-tarefas` | nenhuma | para, exit 0 |
| `B4` | bloco B | nenhuma das anteriores | volta à seleção | segue |
| `FORA` | qualquer | estado sem linha acima: veredito e recomendação que nenhuma linha da fase revisor casa, ou instrumento que materializa, coleta ou fecha (`backlog.py start`, `backlog.py status`, `review_evidence.py`, `telemetria.py append`, `encerrar.py tarefa`) sai diferente de 0 | nenhuma | para, exit 1 |

Toda razão levada a `--razao` troca `—` por `-` (`F-17`). **Fecha a tarefa** = `encerrar.py tarefa --plano <plano> --tarefa <ID> --repo <repo> --laudo <repo>/<laudo>`, mais `--pendencia "<texto>"` quando a linha do executor trouxe `pendencia=`; sem `--resumo`, sem o trio de consumo e sem `encerrar.py handover` (`DLF-10`, `DLF-15`); o caminho do RDO é o da linha ``Detalhe: `<caminho>`.`` do stdout.

**Textos fixos.** Gramática do executor (as quebras são as do bloco; `<ID>` trocado pelo id da tarefa):

  ```
  Devolva uma única linha, numa destas três formas, e nada antes dela:
  <ID> review
  <ID> review pendencia=<uma linha>
  <ID> blocked motivo=<dependencia|premissa|ferramenta> <uma linha de razão>
  ```

Texto de retomada, uma linha: `Retome a tarefa do ponto em que parou e devolva só a linha de retorno.`

Prompt do executor: stdout de `backlog.py show <ID>` sem espaços no fim, linha em branco, a segunda linha do `next`, linha em branco, a gramática. Prompt do revisor: stdout de `backlog.py show <ID>` sem espaços no fim, linha em branco, `Evidência mecânica: <caminho>`, linha em branco e (as quebras são as do bloco):

  ```
  Devolva as duas linhas, nesta ordem, e nada antes delas:
  <ID> <aprovado|ressalva|reprovado> <percentual> bloqueante=<dimensão|nenhuma>
  laudo=<caminho do laudo>
  ```

Bloco de diretivas da `A6` (`DLF-22`), apensado ao prompt original: linha em branco, a linha `Diretivas da revisão anterior`, a linha `**Pendência:** <valor do laudo>` e o corpo da seção `## Motivo das dimensões fora de conforme` do laudo até o próximo cabeçalho `## `, sem espaços nas pontas.

**Relatório.** Impresso no stdout em toda parada, nesta ordem, uma linha por item (as quebras são as do bloco):

  ```
  === RELATÓRIO DO LOOP
  <modelo>
  regra: <id> — <condição>
  tarefas fechadas: <n>
  - <ID> "<título>" — <caminho do RDO>
  tarefa corrente: <ID>
  evidência: <texto>
  cenário: <caminho>
  card: <ID>
  ato de modelo:
  <dossiê verbatim>
  ```

- `<modelo>`: sem tarefa selecionada no run, `nenhuma tarefa conduzida`; senão o stdout de `modelo.py show --plano <plano da última tarefa> --root <repo>` quando sai 0, ou `sem modelo (plano anterior à doutrina)`.
- `<condição>`: o texto da coluna *condição* da linha, como está na tabela.
- `- <ID> …`: uma linha por tarefa fechada no run, na ordem.
- `tarefa corrente:` em toda parada com tarefa selecionada, exceto `FIM` e `LIM`.
- `evidência:` em toda parada, exceto `FIM` e `LIM`: `FS` — o stderr do `next`, ou `tarefa <ID> em <status> sem checkpoint`; `B3` — o texto do gate; `A1` — `exit <n>: ` e os primeiros 400 caracteres do stdout; `FC` — `chaves ausentes: <lista>`; `A2` — a linha inválida, ou `vazio`; `A3a`, `A3b`, `A3c` — a linha do executor; `FR` — o erro de leitura do laudo, ou os primeiros 400 caracteres do `result`; `MOD` — a primeira linha do revisor; `A6a` e `A7` — a pendência do laudo; `A8` — `laudo=<caminho>`; `B1` — o texto de `pendencia=` do executor, ou a pendência do laudo quando veio da `A8a`; `FORA` — o stderr do instrumento, ou `veredito <v> recomendação <r>`.
- `cenário:` e `card:` só nas paradas com escalada (`A3a`, `A3b`, `A3c`, `MOD`, `A6a`, `A7`, `A8`, `B1`): `cenário` = `<pasta>/cenario.md` quando o plano termina em `/plano.md`, senão `docs/plans/_CENARIO-<pai>.md` (`F-19`, `DLF-16`).
- `ato de modelo:` e o dossiê só na `MOD`.
