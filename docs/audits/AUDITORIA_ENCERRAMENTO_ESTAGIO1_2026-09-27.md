# Auditoria de encerramento do primeiro estágio do kit — 2026-09-27

**Objeto:** o kit agêntico Pantonic* (`.claude/` + `GOVERNANCA.md` + `docs/`), na árvore de trabalho de 2026-09-27 (branch `plan/planner-modelo-escopo`, HEAD `d75e7a6`, com WIP não commitado).
**Método:** um plano fictício, executado ponta a ponta contra o kit real pelo procedimento que o kit prescreve (planejador → modelador → decomposição → loop do scrum-master → revisão → fechamento), com um registro por cláusula exercitada. O plano fictício foi descartado ao fim; este relatório é o que fica.
**Auditor:** o consultor (o agente que conduziu a sessão), no papel que o dono nomeou.

## 0. O pedido, verbatim

> Crie um plano fictício que exercite todas as valências dos mecanismos atuais. Performe de maneira autônoma esse plano contra o kit real, registrando: lacunas, erros de execução, passagens de pouca confiabilidade, passagens de alto custo evitável, qualidade da entrega, oportunidades de mecanização (por python, powershell ou bash), oportunidades de melhoria do fluxo de atividades. Ao término, conclua qualitativamente como adequado, inadequado, tem oportunidade de melhoria. Elabore recomendações em tíquetes individuais para cada registro de inadequado e oportunidade de melhoria viável. Entregue o relatório com a avaliação e tíquetes.

## 1. Modelo conceitual da auditoria

| objeto | o que é | propriedades | tipo |
|---|---|---|---|
| relatório final | este documento | tabela de registros, conclusão por dimensão, recomendações | escopo |
| plano fictício | o plano `P-0753` que exercita as cláusulas | cláusulas cobertas, estágio | escopo |
| teste do kit | cada passagem do plano fictício por uma cláusula | cláusula, procedimento, resultado esperado | escopo |
| recomendação | tíquete derivado de um registro inadequado ou de oportunidade | causa, ação, verificação | escopo |
| cláusula do kit | cada mecanismo testável (skill, agente, instrumento, hook, regra) | forma prescrita | externo |
| execução do teste | a passagem real, medida | lacuna, erro, confiabilidade, custo evitável, qualidade, mecanização, fluxo | medição |

Fluxo: OP-1 enumerar as cláusulas → OP-2 autorar o plano fictício que as cobre → OP-3 executar cada teste e registrar a medição na tabela → OP-4 concluir por dimensão → OP-5 emitir as recomendações → OP-6 descartar o plano fictício.

## 2. Cláusulas do kit exercitadas

Uma linha por mecanismo testável; a coluna *teste* diz por qual passagem do plano fictício ele foi exercitado. Cláusula sem passagem no plano fictício foi exercitada por sonda direta e está marcada `sonda`.

| id | cláusula (mecanismo) | residência | teste |
|---|---|---|---|
| K-01 | gate modelo-por-fase (hook `UserPromptSubmit` + skill) | `.claude/global/hooks/`, skill `modelo-por-fase` | abertura desta sessão |
| K-02 | guardas executáveis: `kit_check` validate/check-drift, `check-readme`, `dead_code`, `ratchet_piso`, `materializar` check/drift | `.claude/checks/`, `.claude/tools/materializar.py` | baseline + fechamento de cada tarefa |
| K-03 | skill `guardrails-check` (tiers, conformance, piso) | `.claude/skills/guardrails-check` | fechamento de tarefa pelo executor |
| K-04 | `pantonic-planner` Fase 0–1: intake + campanha de investigação (SAÍDA 1) | `.claude/agents/pantonic-planner.md` | autoria do plano fictício |
| K-05 | `pantonic-scout` (coleta barata) | `.claude/agents/pantonic-scout.md` | campanha da K-04 |
| K-06 | `pantonic-planner` Fase 3a: esqueleto + dossiê `Ato de modelo` de autoria (SAÍDA 3) | idem | autoria |
| K-07 | `pantonic-model-designer` ato de autoria + `modelo.py check` | `.claude/agents/pantonic-model-designer.md`, `.claude/tools/modelo.py` | autoria |
| K-08 | `pantonic-planner` Fase 3b–5: um card por operação, ensaio `card_check`, `estado.tsv`, `_INBOX.md`, `checar-versao-kit` | idem | decomposição |
| K-09 | plano em pasta (`P-<n>-<slug>/plano.md` + `estado.tsv` + `rdo/ laudos/ evidencia/`) | skill `diario-de-obras`, `caminhos.py` | forma escolhida para o plano fictício |
| K-10 | skill `checar-versao-kit` (congelamento + gatilho de revisão §7.1) | `.claude/skills/checar-versao-kit` | registro do plano |
| K-11 | `backlog.py drain` (inbox → índice + contador) | `.claude/tools/backlog.py` | abertura da janela |
| K-12 | `backlog.py check` (lint C-xx) | idem | após cada escrita no plano |
| K-13 | Marco 1: `modelo.py show` + veredito do dono sobre o modelo | `GOVERNANCA.md` §3.2 | antes do loop |
| K-14 | `backlog.py next` (seleção, dossiê, `=== HANDOVER DE`, achados roteados) | idem | Passo 2 de cada tarefa |
| K-15 | gates do Passo 3: G-PLANREADY, gate de delegação (8 itens), `modelo.py check`, `card_check.py` | skills `scrum-master`/`passagem-de-bastao` | cada tarefa |
| K-16 | `backlog.py status` + projeções (card, índice, `Fila corrente`, `estado.tsv`) | idem | cada transição |
| K-17 | `.claude/estado/tarefa-corrente.json` + `review_evidence.py --capturar-ref` | Passo 4 | cada despacho |
| K-18 | `pantonic-executor` (linha de retorno, `card_check --gravar`, TDD) | `.claude/agents/pantonic-executor.md` | cada tarefa |
| K-19 | hook `SubagentStop` → `docs/telemetria.tsv` | `.claude/tools/telemetria_hook.py` | cada retorno de executor |
| K-20 | hook de progresso → painel `.claude/estado/progresso.txt` | `.claude/tools/progresso_hook.py` | toda a janela |
| K-21 | `review_evidence.py` (evidência, `--desde`, medida do executor, `--atribuir`) | `.claude/tools/review_evidence.py` | Passo 6 / B0 |
| K-22 | `pantonic-reviewer` + `rdo.py laudo` (sete dimensões, pacote) | `.claude/agents/pantonic-reviewer.md`, `.claude/tools/rdo.py` | cada tarefa |
| K-23 | bloco A (roteamento por veredito e recomendação) | skill `scrum-master` | cada laudo |
| K-24 | `encerrar.py handover` + `backlog.py next` devolvendo o handover | `.claude/tools/encerrar.py` | fechamento de cada tarefa |
| K-25 | `encerrar.py tarefa` (gate do modelo, `done`, RDO 3 seções, telemetria, achados) | idem | fechamento de cada tarefa |
| K-26 | bloco B (B0 atribuição medida, B1 pendência → consultor, B2–B4) | skill `scrum-master` | após cada fechamento |
| K-27 | `pantonic-consultant` efêmero: cenário persistido, `rota=`, `ACIONAMENTOS_CONSULTOR.tsv`, card corretivo | `.claude/agents/pantonic-consultant.md` | parada `blocked premissa` provocada |
| K-28 | `pantonic-model-designer` ato de emenda (`## 1A` pendente) + `modelo.py show --drift` | idem | se a triagem devolver `rota=modelador` |
| K-29 | hook de crença ao gravar plano/diário | `.claude/tools/crenca_hook.py` | edições do plano por Write/Edit |
| K-30 | hook de ocupação (aviso de janela) | `.claude/tools/ocupacao.py` | toda a janela |
| K-31 | skill `entrega-de-encerramento` (`operacoes.md`) | `.claude/skills/entrega-de-encerramento` | fechamento do plano |
| K-32 | `encerrar.py plano` (`done` do plano, `entrega.md`, linha do diário) | `.claude/tools/encerrar.py` | fechamento do plano |
| K-33 | relatório de encerramento + skills `fatos-frescos` e `mensagem-ao-dono` | skill `scrum-master` | fim da janela |
| K-34 | `backlog.py diretiva` | `.claude/tools/backlog.py` | sonda |
| K-35 | `uow.py` (unidade de trabalho) | `.claude/tools/uow.py` | sonda |
| K-36 | tíquete nasce executável (`## TK-<n>` + card) | skill `diario-de-obras` | via consultor, se houver rota tíquete; senão sonda |

## 3. Registros — um por teste

Dimensões: **L** lacuna · **E** erro de execução · **C** passagem de pouca confiabilidade · **$** custo evitável · **Q** qualidade da entrega · **M** oportunidade de mecanização · **F** oportunidade de melhoria de fluxo. Avaliação: `adequado` · `inadequado` · `oportunidade`.

| # | cláusula | teste | medido | dimensões | avaliação |
|---|---|---|---|---|---|
| 1 | K-01 | hook `UserPromptSubmit` de modelo-por-fase na abertura | disparou o aviso "trabalho intelectual" com modelo Fable ativo (acima do exigido); a skill manda seguir e anotar — seguiu | — | adequado |
| 2 | K-02 | baseline dos sete guardas + suíte antes de qualquer ato | todos exit 0; `452 passed`; `check-readme.ps1` imprime acentos corrompidos no console cp1252 (`vers�o`) | C (cosmético: a saída que o card copia como literal muda com o console) | oportunidade |
| 3 | K-03 | `guardrails-check` Tier 2 "obrigatório e bloqueante" exige `tests/conformance/` e cita `tests/piso_comportamental.txt` | no hub **nenhum dos dois existe**: `conformance: NAO existe`, `piso: ausente`; `ratchet_piso` sai 0 por "nenhum piso declarado" | L, C (o gate prescrito como bloqueante é vazio no próprio hub; verde por ausência) | inadequado |
| 4 | K-35 | `uow.py` — quem o consome? | grep `uow.py` em skills, agentes, GOVERNANCA, README, rubrica → **0 ocorrências**; o próprio docstring cita "Regra 9 da doutrina global", que hoje é a regra de mensagem legível (renumerada) | L (instrumento sem consumidor nem residência de doutrina; ponteiro de regra envelhecido) | inadequado |
| 5 | K-19 | quem grava a telemetria de cada papel | `telemetria_hook.py:51` — só `pantonic-executor`; revisor, consultor, modelador e planejador dependem de `telemetria.py append` à mão pelo orquestrador a partir do `<usage>` | M (o hook já recebe o `<usage>` de todo `SubagentStop`; gravar todos os papéis com sufixo é mecânico) | oportunidade |
| 6 | K-04 | `pantonic-planner` Fase 0–1 sobre o pedido fictício (instância 1) | SAÍDA 1 correta: 10 perguntas fechadas; detectou o risco da premissa `ler_texto_utf8`; custo 41,4k tokens / 4 tool uses / 75 s só para chegar à campanha | $ (uma sonda de 1 comando antes de abrir o Opus revelaria a premissa falsa por ~0 tokens), F | oportunidade |
| 7 | K-04/K-05 | forma das perguntas da campanha × ferramentas do scout | 5 das 10 perguntas pedem **rodar comando** (`Test-Path`, `git check-ignore`, `pytest`, `pwsh`, `python -c`); o `pantonic-scout` tem só `Read, Glob, Grep` — quem rodou foi o orquestrador, à mão, em 2 chamadas | L, F (o protocolo do planejador manda pôr na campanha "rode <comando> e devolva o stdout", mas nenhum papel de coleta pode rodá-lo) | inadequado |
| 8 | K-05 | `pantonic-scout` (Haiku) sobre as 6 perguntas de leitura | dossiê correto e compacto; 47,7k tokens / 27 tool uses / 119 s; custo maior que o do planejador que o pediu | $ (Haiku barato por token, mas 27 leituras; metade das perguntas eram greps de 1 linha que o orquestrador faria em 1 chamada) | oportunidade |
| 9 | K-09 | planos em pasta existentes | Glob `docs/plans/P-*/plano.md` → **0**; todos os planos desde o `P-0749` (que instituiu a pasta) nasceram legado | C (a forma canônica nunca rodou ponta a ponta fora de fixture; o `P-0753` é o primeiro) | oportunidade |
| 10 | K-04 | premissa falsa no pedido do dono (`ler_texto_utf8`) | o planejador classificou como "poluição → volta ao dono, contexto limpo": custou a instância inteira (41,4k) + campanha para descobrir um fato de 1 grep; a decisão coube ao dono | $, F (pré-voo mecânico do pedido: todo caminho/símbolo citado pelo dono é conferido por grep antes de abrir o planejador) | oportunidade |
| 11 | K-06 | `pantonic-planner` Fase 2–3a (instância 2, fria, com o dossiê) | SAÍDA 3 conforme: esqueleto de 112 linhas (13 fatos, 11 decisões, 7 invariantes, 8 casos observáveis, 5 riscos), dossiê de autoria fechado; **108,1k tokens / 29 tool uses / 445 s** para um entregável de ~40 linhas de Python | $ (o custo do plano supera em ordens de grandeza o do produto; a Fase 4 de auto-auditoria com 14 itens é lida e aplicada inteira mesmo num plano trivial) | oportunidade |
| 12 | K-08/K-12 | `backlog.py check` durante a Fase 3a (plano só com `plano.md`) | saiu 1 com `C-8` (plano vivo sem Status), `C-13` (estado.tsv ausente) e `C-10` (contador aponta id existente); o planejador **improvisou** — antecipou o registro da Fase 5 (estado.tsv `blocked dependencia` + linha do inbox + contador para P-0754) "seguindo o precedente do P-0745" | C, F (o protocolo do planejador e o lint discordam sobre quando o plano passa a existir para a máquina: entre a Fase 3a e a Fase 5 a árvore está num estado que o `check` recusa, e cada planejador resolve à sua maneira) | inadequado |
| 13 | K-07 | `pantonic-model-designer`, ato de autoria | §1 conforme (3 operações, 12 propriedades, tipos escopo/externo/medição, lastro por célula); devolveu os quatro itens da forma; `modelo.py check` exit 1 só com `V3` de lastro, como a norma prevê; 68,1k tokens / 12 tool uses / 205 s | $ (68k para 3 operações; leu GOVERNANCA §3.2 + gramática da skill inteira, como o próprio arquivo manda) | adequado |
| 14 | K-07 | `modelo.py check` sobre plano em pasta real (primeira vez) | rodou e leu a forma nova sem erro de caminho | — | adequado |
| 15 | K-08 | `pantonic-planner` Fase 3b–5 (instância 3): 3 cards, ensaio em cópia, registro | cards completos e fechados (81 linhas o `SF-T1`); o ensaio (item 14) achou dois fatos reais (`-X utf8` não propaga ao filho; mutação derruba os testes de recusa); `checar-versao-kit` rodou e acusou **revisão da doutrina pendente** (`P-0751`, `P-0752` fora de rodada); **169,5k tokens / 46 tool uses / 21,7 min** | $, Q (qualidade alta; custo total do planejamento ≈ 435k tokens para ~40 linhas de produto) | oportunidade |
| 16 | K-10 | skill `checar-versao-kit` na criação do plano | modo hub, congelada `0.0.0`, sem rede; gatilho §7.1 armado e reportado ao dono — achado **real**, não fictício | — | adequado |
| 17 | K-13 | Marco 1 pelo `modelo.py show` | leitura do dono legível: objetos, fluxo com `[prevista ]`, estados; `go` dado sobre o instrumento sem abrir o plano | Q | adequado |
| 18 | K-11/K-16 | `backlog.py drain` + `status P-0753 ready` sobre plano em pasta | drain promoveu a linha ao índice (`P-0753-SF`, `blocked`) e ao histórico; status reescreveu `estado.tsv`, índice e `Fila corrente`; `check` 0 | — | adequado |
| 19 | K-14 | `backlog.py next` — dossiê "verbatim" | o card tem 81 linhas; `next` imprime ~45 e corta o meio com `… truncado (plano.md:134-214)` — justamente `Camada`, `Passos` e `Restrições`, que o executor precisa; `show` também trunca (51 linhas). O orquestrador pagou um Read do range de qualquer forma | F, $ (o teto DB-7 corta o insumo do despacho e obriga a leitura dupla; ou o teto sobe, ou o `next` imprime só o cabeçalho + range e deixa a cópia para o despacho) | inadequado |
| 20 | K-15 | `card_check.py` sobre card de plano em pasta | `status ausente: comparando antes` — o instrumento não lê `estado.tsv` para derivar o mundo; em card `done` de plano em pasta compararia `antes` por omissão | C (forma nova sem cobertura no instrumento; funciona por acaso enquanto se passa `--mundo`) | oportunidade |
| 21 | K-18 | `pantonic-executor` (Sonnet) sobre `SF-T1` | `SF-T1 review` na primeira linha, seguida de prosa (descartada, Passo 5); 10/10 verificações; guardas verdes; `458 passed`; medida gravada; 62,6k tokens / 17 tool uses / 223 s; nenhuma contingência | Q (entrega conforme, executor frio funcionou) | adequado |
| 22 | K-19 | hook `SubagentStop` → telemetria | linha `SF-T1 sonnet 17 62.6 222.5 usage` gravada sozinha, batendo com o `<usage>` | — | adequado |
| 23 | K-21 | `review_evidence.py --desde <ref>` em plano em pasta | gerou `evidencia/SF-T1.md` (263 linhas): tocados × alvos com atribuição (entrega / orquestração), diff por alvo, medida do executor incorporada (10 itens `bate`), bateria de guardas; veredito mecânico `conforme` | Q | adequado |
| 24 | K-09 | nome do arquivo de medida no plano em pasta | `evidencia/P-0753-SF-T1-medida.json` ao lado de `evidencia/SF-T1.md` — o prefixo do plano é redundante dentro da pasta do plano | C (duas convenções de nome na mesma pasta) | oportunidade |
| 25 | K-20 | painel do gerente durante o loop | `M-0`, `M-1`, `M-3`, `M-4` saíram certas com o título; **`M-2`** (in-progress) e **`M-5`** (evidência) **não saíram** — os comandos rodaram encadeados numa única chamada Bash com heredoc/`$(...)`, e o gancho não os reconheceu; nas fases de planejamento o painel escreveu `Agente planejador recebe a tarefa "(tarefa não identificada)"` (ruído para o gerente); modelador e scout não geram linha | C (o painel depende da forma da linha de comando do condutor; silêncio não é detectável pelo gerente) | inadequado |
| 26 | K-22 | `pantonic-reviewer` (Opus) + `rdo.py laudo` sobre `SF-T1` | duas linhas exatas; laudo gerado em `laudos/SF-T1.md` (plano em pasta) com pacote calculado (aprovado 100, seguir); **achado de processo real** de alvo `dossiê`: o bloco `git diff --stat` da evidência ignora o `--desde` e lista os 59 arquivos do WIP; 70,4k tokens / 11 tool uses / 112 s | Q (revisão exercitou o módulo e achou defeito real do instrumento) | adequado |
| 27 | K-23 | bloco A sobre (`aprovado`, `nenhuma`, `seguir`) | `A9` casou sem ambiguidade; a leitura do pacote exigiu abrir o laudo (`grep`) — a linha de retorno não traz a recomendação | F (a recomendação, campo que decide o roteamento, poderia viajar na 1ª linha do revisor e poupar a leitura do laudo) | oportunidade |
| 28 | K-24 | `encerrar.py handover` + `next` da sucessora | o bloco `=== HANDOVER DE SF-T1` chegou ao `next` de `SF-T2` com `Entregue`, `Contrato`, `Não refazer`, `Pendente` | Q | adequado |
| 29 | K-25 | `encerrar.py tarefa` sobre `SF-T1` (plano em pasta) | um comando: `done` em `estado.tsv`, índice `ready 1/3`, `Fila corrente`, RDO 3 seções em `rdo/SF-T1.md`, telemetria já garantida pelo hook; saída = `# Humano` legível. **Mas** o achado de processo do laudo (rota tíquete) **não foi transcrito** ao `## 9` do plano nem ao RDO: o instrumento lê o pacote (5 campos) e ignora a tabela `Achado de processo`; cabe ao condutor redigitar via `--achado` — e o condutor esqueceu (caso medido nesta auditoria; `AE-1` gravado à mão) | M, C (o laudo já carrega alvo, texto e rota do achado em tabela; `encerrar.py tarefa` pode transcrevê-los como `AE-<n>` sem intervenção — a "regra conferir antes de X vira guarda dentro de X" do `P-0752` não chegou aqui) | inadequado |
| 30 | K-25 | `# Histórico` do RDO | 5 linhas do painel; faltam as de `M-2`, `M-5` e `M-10`, perdidas pelo gancho (registro 25) — o RDO herda o silêncio do painel | C | oportunidade |
| 31 | K-19 | telemetria do revisor | linha `SF-T1-revisao opus 11 70.4 112.3 usage` apensada **à mão** via `telemetria.py append`, copiando 3 números do `<usage>` — ponto de erro por transcrição a cada tarefa | M (o hook `SubagentStop` já vê o `<usage>` do revisor; registro 5) | oportunidade |
| 32 | K-20 | causa do silêncio do painel (registro 25), medida no código | `progresso_hook.py:293-309` (`_programa`): pula todo token iniciado por `-` e toma o seguinte como script — com `python -X utf8 .claude/tools/backlog.py status …`, o "script" vira `utf8` e nenhum evento por invocação (`M-2`, `M-5`, `M-10`, `M-13`, `M-18`) casa. O `-X utf8` é a forma segura que `docs/ARMADILHAS_DE_FERRAMENTA.md:14` recomenda; o próprio kit ensina a invocação que cega o painel. `M-1`/`M-12` sobrevivem porque casam por substring | E, C (defeito de instrumento com reprodução determinística: flag com valor separado) | inadequado |
| 33 | K-18 | `pantonic-executor` sobre `SF-T2` | `SF-T2 review` + prosa; 9/9 verificações; `460 passed`; 58,2k tokens / 16 tool uses / 172 s; nenhuma contingência; handover da antecessora usado (auxiliar `_rodar_sonda` reaproveitado) | Q | adequado |
| 34 | K-15/K-16 | segundo ciclo de gates e materialização (`SF-T2`) | `modelo.py check` 0, `card_check` 0 (agora com o mundo `antes` existente), `458 collected` re-medido, `status in-progress` ok; sequência de 6 comandos por despacho, todos mecânicos e idênticos tarefa a tarefa | M (um único verbo `despachar <ID>` faria gates + `in-progress` + `tarefa-corrente.json` + `--capturar-ref` + impressão do dossiê, hoje 4 chamadas e um JSON escrito à mão pelo condutor) | oportunidade |
| 35 | K-22 | `pantonic-reviewer` sobre `SF-T2` | `aprovado 100`, seguir; exercitou o módulo ponta a ponta em leitura (bytes crus do stderr, barra invertida, diretório, argparse sem argumento); citou `AE-1` sem duplicar; 77,9k tokens / 15 tool uses / 92 s | Q | adequado |
| 36 | K-25 | `encerrar.py tarefa` sobre `SF-T2` | um comando, `2/3` projetado, RDO em `rdo/SF-T2.md`; laudo sem achado → nada a transcrever | — | adequado |
| 37 | K-20 | painel sem `-X utf8` | `M-2` ("gates aprovados; vou materializar"), `M-5` ("vou reunir para o revisor") e `M-10` ("vai fechar a tarefa") passaram a sair — confirma o registro 32 por controle pareado | — | (confirmação) |
| 38 | K-14 | `backlog.py next` para `SF-T3` | selecionou `SF-T3` (dependência `SF-T2` satisfeita) e trouxe `=== HANDOVER DE SF-T2` | — | adequado |
| 39 | K-18 | `pantonic-executor` sobre `SF-T3` (redacao) | devolveu **exatamente** `SF-T3 review`, sem prosa; guia com os dois exemplos rodados e datados; 54,1k tokens / 13 tool uses / 158 s | Q | adequado |
| 40 | K-21 | `review_evidence.py` sobre `SF-T3` com WIP do condutor na janela | acusou `docs/audits/AUDITORIA_…md` como "fora dos alvos e sem atribuição" e deixou o veredito mecânico **aberto** — comportamento correto: o instrumento não adivinha; a reconciliação é do revisor (3a) e a atribuição é o `B0` | — | adequado |
| 41 | K-22 | `pantonic-reviewer` sobre `SF-T3` com WIP alheio na evidência | reconciliou o vermelho aberto (passo 3a) com o contexto injetado no despacho; `aprovado 100`; achado de processo de alvo `dossiê` com rota tíquete: o instrumento deveria aceitar a declaração de WIP da orquestração; 76,4k tokens / 13 tool uses / 130 s | Q, F (a reconciliação dependeu de o condutor lembrar de avisar; regra "conferir antes de X vira guarda dentro de X" não chegou ao `review_evidence`) | oportunidade |
| 42 | K-32 | `encerrar.py plano` com tarefa não terminal | recusou (`FALHOU - plano P-0753 tem tarefa(s) não terminal(is): SF-T3`, exit 1) e não escreveu `entrega.md` nem linha do diário | — | adequado |
| 43 | K-34 | `backlog.py diretiva` | reescreveu a linha de diretiva; `check` 0 | — | adequado |
| 44 | K-35 | `uow.py status` sem UoW aberta | mensagem clara ("nenhuma UoW aberta … rode `uow.py open`"), mas sai **0** num erro nomeado (`erro:` no stdout) | C (exit code não discrimina o erro) | oportunidade |
| 45 | K-27 | `pantonic-consultant` efêmero, gatilho 2 (achados com rota tíquete) | criou `cenario.md`, apensou a linha à `ACIONAMENTOS_CONSULTOR.tsv`, marcou `AE-1`/`AE-2` absorvidos, mediu dois protótipos fora da árvore e devolveu `rota=resolve` **com `estrategico=`** — detectou sozinho a colisão com a diretiva do dono de 2026-09-26 ("nenhum tíquete novo por ajuste"); o loop parou como o Passo 8 manda. **131,2k tokens / 47 tool uses / 11,8 min** para abrir dois tíquetes; leu o relatório da auditoria (fora das três entradas); `estrategico=` veio em 3 frases, não em uma | Q (juízo correto), $ (acionamento mais caro da janela), C (leitura fora do cenário) | oportunidade |
| 46 | K-36 | tíquete nasce executável (`TK-94a`, `TK-95a`) | dois tíquetes no diário, cada um com card `ready` na gramática, `Verificação` medida (`card_check --mundo antes` exit 0 nos dois), índice `ready 0/1`; `backlog.py check` 0 | Q | adequado |
| 47 | K-23 | bloco A/Passo 8 com `estrategico=` | a rota `resolve` **não** executou ação adicional; o reparo gravado ficou; a frase vai ao relatório de encerramento para o dono — conforme `DCS-27/28` | — | adequado |
| 48 | K-27 | `pantonic-consultant`, gatilho 4 (ato do dono no marco), acionamento 2 | classificou o ato como drift (`rota=modelador`, sem `estrategico=`), registrou `DSF-12` na `## 3`, transcreveu o ato na `## 0`, corrigiu a tabela de marcos (Marco 1 ainda dizia `pendente` — ninguém a atualiza no `go`), devolveu o dossiê de emenda com seis campos; 67,4k tokens / 12 tool uses / 136 s — **metade** do acionamento 1, com a instrução "não leia fora do cenário" | Q; F (a tabela de marcos do plano não tem escritor mecânico: o `go` do Marco 1 só foi ao `estado.tsv`) | oportunidade |
| 49 | K-28 | `pantonic-model-designer`, ato de emenda | `## 1A` pendente gravada como bloco irmão (linhas 72–111), linha `versão 2 · pendente` no `### 1.4`, `## 1` intacta, `check` 0 (só a `## 1` é aferida — a `## 1A` não passa por `V1..V21`); devolveu a declaração propriedade a propriedade; achados fora da seção corretos (README, testes, sonda, 10 linhas do plano com a mensagem antiga); 82,4k tokens / 14 tool uses / 140 s | Q; L (o `check` não valida a `## 1A`: uma pendente malformada só apareceria no aceite) | oportunidade |
| 50 | K-28 | `modelo.py show --drift` / `--pendente` no marco | drift legível: `[~] OP-2` e `[~] sonda.recusa…` com antes ⇒ depois; a mudança no **contrato** do objeto não aparece no drift (só operações e estado final) | L (o dono valida o drift sem ver a alteração de contrato) | oportunidade |
| 51 | K-31 | skill `entrega-de-encerramento` → `operacoes.md` na pasta do plano | escrito pelo condutor inline (estrutura da skill: abertura, arco, seção por tarefa com 4 blocos, ganhos, defeitos com estado, pendências); cobertura por comando: `nao citados: nenhum` | Q; $ (custo de redação do condutor ≈ 2k tokens de saída; a skill não tem instrumento de esqueleto — cada plano reescreve a estrutura de memória) | oportunidade |
| 52 | K-28 | `pantonic-model-designer`, desfecho do marco (recusa) | `## 1A` e a linha da pendente removidas; `## 1` sem marca; `check` 0; 52,4k tokens / 7 tool uses / 50 s. Validação prévia do consultor no marco **não exercitada** (custo) — registrada como fato | Q | adequado (parcial) |
| 53 | K-13 | quem registra o veredito do marco | a tabela *Marcos de validação* do plano ficou `pendente` no Marco 1 (o `go` só foi ao `estado.tsv`, corrigido depois pelo consultor) e `pendente — emenda pedida` no Marco 2 depois da recusa; `DSF-12` sem caducidade marcada; `cenario.md` `C-4` sem desfecho; `## 0` com o ato e sem o veredito | F, M (o veredito do marco não tem escritor nem instrumento: cinco residências ficam defasadas a cada marco) | inadequado |
| 54 | K-32 | `encerrar.py plano` com o veredito do dono | um comando: `done` do plano em `estado.tsv` e no índice (`done 3/3`), `entrega.md` nas três seções, linha no cabeçalho do diário; recusou antes enquanto havia tarefa aberta (registro 42) | Q | adequado |
| 55 | K-19/K-33 | "Consumo do plano na série" que o fechamento imprime | `399.6 mil tokens em 6 linha(s)` — só as linhas `SF-*` (3 execuções + 3 revisões apensadas à mão); planejador, scout, modelador e consultor **não estão na série** porque nenhum instrumento os grava; o custo real do plano foi ≈ 1.168k tokens (tabela da §6): o número publicado ao dono subestima em ~66% | C, M (mesma causa do registro 5) | inadequado |
| 56 | K-29 | gancho de crença (`crenca_hook.py`) por payload sintético e por `Edit` real | só acusa as formas literais que conhece (`N passed`, `antes N`, `depois N`, `Medido antes`, âncora `arquivo:linha`); `Edit` real com "a suíte tinha 460 testes" passou em silêncio; com comando na mesma linha não avisa (correto); nunca bloqueia | L (leve: número de aceite fora dessas formas não é visto) | adequado |
| 57 | K-30 | gancho de ocupação | limiar 50% de 1M (`ocupacao.py:83`); disparou nesta sessão no despacho do modelador do plano da auditoria, depois de 17 subagentes: `PreToolUse` injetou o aviso de encerrar a tarefa corrente e não abrir tarefa nova, sem bloquear; a condução fechou a criação do plano (tarefa em curso) e parou no Marco 1 | — | adequado |
| 58 | K-33 | relatório de encerramento e skills `fatos-frescos`/`mensagem-ao-dono` | aplicadas na redação deste relatório e da mensagem final: todo número desta tabela vem do `<usage>` da notificação do subagente ou de comando rodado na janela; as siglas vão com título | — | adequado |

## 4. Conclusão por dimensão

| dimensão | veredito | fundamento (registros da §3) |
|---|---|---|
| **Integração ponta a ponta** (a dúvida de origem do dono) | **adequado** | o plano fictício atravessou todos os mecanismos sem improviso do condutor no caminho feliz: planejador → modelador → decomposição → drain → next → gates → executor → hook de telemetria → evidência → revisor → laudo calculado → bloco A → handover → fechamento por comando → consultor → emenda/drift → recusa → `operacoes.md` → `encerrar.py plano`. O plano em pasta (forma nova) rodou pela primeira vez fora de fixture (9, 14, 18, 23, 29, 54) |
| **Lacunas (L)** | **inadequado em 3 pontos** | o gate "obrigatório e bloqueante" de conformance e piso não existe no hub (3); a campanha do planejador pede comandos que o scout não roda (7); `uow.py` sem consumidor nem residência (4). Leves: `card_check` sem `estado.tsv` (20), `check` não afere a `## 1A` (49), `--drift` sem contrato (50), gancho de crença de formas fechadas (56) |
| **Erros de execução (E)** | **um defeito de instrumento** | o painel do gerente cega com `python -X utf8` (25, 32), a forma que o próprio kit recomenda; nenhum outro instrumento falhou sobre plano em pasta |
| **Confiabilidade (C)** | **tem oportunidade de melhoria** | seis pontos ainda dependem de o condutor lembrar: `--achado` no fechamento (29), a linha de telemetria dos papéis não executores (31, 55), a declaração de WIP à evidência (41), o veredito do marco em cinco residências (53), a forma da linha de comando para o painel (25), o `--mundo` do `card_check` em plano em pasta (20). Um deles falhou de fato nesta janela (29) |
| **Custo evitável ($)** | **inadequado** | ≈ 1.168k tokens de subagentes para ~40 linhas de produto (§6): planejamento 319k + modelagem 203k + consultoria 199k + revisão 225k = 946k de fase intelectual contra 175k de execução (5,4 : 1). Evitáveis por mudança de fluxo: a instância do planejador gasta só para descobrir uma premissa falsa (6, 10), a auto-auditoria de 14 itens aplicada inteira a um plano trivial (11, 15), o consultor lendo fora do cenário (45), o dossiê truncado que obriga leitura dupla (19) |
| **Qualidade da entrega (Q)** | **adequado** | 3/3 `aprovado 100` na primeira passagem, zero `blocked`, zero retentativa, zero pergunta ao dono no meio da janela; a revisão achou dois defeitos reais de instrumento (26, 41); o consultor achou sozinho a colisão com a diretiva vigente (45); todo número publicado foi medido |
| **Mecanização (M)** | **tem oportunidade de melhoria** | seis mecanizações com instrumento já existente: hook de telemetria para todo papel (5), transcrição do achado do laudo no fechamento (29), verbo `despachar` (34), veredito do marco por comando (53), pré-voo do pedido (10), esqueleto de `operacoes.md` (51) |
| **Fluxo (F)** | **tem oportunidade de melhoria** | o `next` corta o dossiê que o executor precisa (19); o lint recusa o plano entre a Fase 3a e a Fase 5 (12); a recomendação do laudo não viaja na linha do revisor (27); a fase intelectual não é dimensionada pela classe do plano (11) |

**Veredito qualitativo geral: adequado na integração e na qualidade; tem oportunidade de melhoria em confiabilidade, mecanização e fluxo; inadequado em custo e em três lacunas entre doutrina e instrumento.**

**Sobre a dúvida de origem ("ganhei confiabilidade e custo em relação a usar a ferramenta nativa?").** O que se mediu responde a metade. **Confiabilidade, sim:** todo número publicado saiu de comando, cada entrega foi julgada por instrumento e por revisor independentes, o consultor barrou uma colisão com a diretiva do dono que um agente único não veria, e a única perda de informação da janela (o achado do laudo não transcrito) foi apanhada pelo próprio processo. **Custo, não:** para um entregável deste tamanho o kit gastou 15 instâncias de subagente e ≈ 1,17M tokens; uma sessão nativa de um agente faria o mesmo script num contexto só (estimativa, não medida: nenhuma execução nativa foi rodada como controle nesta auditoria). O custo do kit é **fixo por plano** (≈ 720k entre planejamento, modelagem e consultoria) mais **≈ 130k por tarefa** (executor + revisor), e por isso só se dilui em plano cujo produto seja grande ou arriscado o bastante para pagar o controle. A recomendação é dupla: as mecanizações da §5 cortam o custo variável; e o planejador precisa de uma régua de profundidade pela classe do plano, porque um plano de 3 operações sobre ferramentaria não deveria pagar a mesma auto-auditoria de 14 itens que um plano de doutrina.

## 5. Recomendações — um tíquete por registro viável

Forma: título, origem (registro da §3), causa, ação fechada, verificação e cabeçalho de card. Todos nascem `ready`, salvo os que dependem de decisão do dono (marcados). **Nenhum foi aberto no diário**, por causa da diretiva do dono de 2026-09-26 ("nenhum card nem tíquete novo por ajuste"); os dois que o consultor abriu durante o plano fictício (`TK-94`, `TK-95`) foram removidos na limpeza e estão no Apêndice A, prontos para reabrir.

### R-01 — O gate de conformance e piso que a doutrina chama de bloqueante passa a existir no hub
- **Origem:** registro 3 (L, C — inadequado). **Causa:** a skill `guardrails-check` (Tier 2) exige `tests/conformance/` e `tests/piso_comportamental.txt`; nenhum existe em `PantonicApp`, e `ratchet_piso` sai verde "por ausência".
- **Ação:** criar `tests/piso_comportamental.txt` com os comportamentos já trancados pelos `test_tr_*` do kit (uma linha `<nodeid> — <frase>` por TR), e ou criar `tests/conformance/` com o teste de camadas do kit (nenhum `.claude/tools/*.py` importa de `tests/`; instrumentos carregam `caminhos.py` por caminho), ou reescrever o item 2 da skill declarando que no hub o Tier 2 é a bateria de `.claude/checks/`.
- **Verificação:** `python .claude/checks/ratchet_piso.py` → exit 0 com "N comportamento(s)" e não "nenhum piso declarado"; `pytest --co -q` coleta `tests/conformance/` ou a skill deixa de citá-la.
- **Card:** `[Sonnet · esforço medium · classe implementacao]`.

### R-02 — A campanha do planejador só pede ao scout o que o scout pode responder
- **Origem:** registro 7 (L, F — inadequado). **Causa:** a Fase 1 do `pantonic-planner` manda pôr na campanha "rode `<comando>` e devolva o stdout"; o `pantonic-scout` tem só `Read, Glob, Grep`.
- **Ação (decisão técnica, uma de duas):** (a) o planejador separa a campanha em *perguntas de leitura* (scout) e *perguntas de comando* (quem conduz a sessão roda e cola), com o formato de cada bloco fixado no arquivo do agente; ou (b) nasce `.claude/tools/sondar.py`, que recebe um arquivo com um comando por linha e devolve stdout, stderr e exit de cada um, e a campanha cita esse instrumento.
- **Verificação:** a frase da Fase 1 que hoje manda "rode" na campanha não existe mais no arquivo do planejador (`Select-String -SimpleMatch`); `pwsh .claude/checks/kit_check.ps1 -Mode check-drift` exit 0.
- **Card:** `[Opus · esforço low · classe redacao]` para (a); `[Sonnet · esforço medium · classe implementacao]` para (b).

### R-03 — `uow.py` ganha consumidor ou sai do kit
- **Origem:** registros 4 e 44 (L — inadequado). **Causa:** nenhum agente, skill, doutrina ou README cita `uow.py`; o docstring aponta "Regra 9 da doutrina global", que hoje é outra regra; `uow.py status` sem UoW aberta sai 0 com `erro:` no stdout.
- **Ação (decisão do dono):** ou o papel que deveria usá-lo (o executor, ao editar artefato canônico do harness) passa a citá-lo e o exit de erro vira 1; ou o arquivo e os testes dele saem no mesmo commit.
- **Verificação:** `grep -rl "uow.py" .claude/skills .claude/agents GOVERNANCA.md README.md` ≥ 1, ou o arquivo não existe.
- **Card:** `[Sonnet · esforço low · classe mecanica]`. Nasce `blocked` razão `dependencia`: decisão do dono.

### R-04 — `backlog.py check` aceita o plano entre a Fase 3a e a Fase 5 do planejador
- **Origem:** registro 12 (C, F — inadequado). **Causa:** o esqueleto gravado na Fase 3a (`plano.md` sem `estado.tsv` e sem linha no inbox) dispara `C-8`, `C-13` e `C-10`; o planejador improvisou o registro antecipado.
- **Ação:** o protocolo do planejador grava `estado.tsv` com a linha do plano `blocked dependencia` na própria Fase 3a, junto do esqueleto; a linha do inbox e o contador continuam na Fase 5; o `check` trata plano em pasta cujo `estado.tsv` só tem a linha do plano como válido. Fixture nova com esse estado intermediário.
- **Verificação:** `python .claude/tools/backlog.py check --repo tests/fixtures/backlog/esqueleto` → exit 0; `pytest -k esqueleto` → 1 passed.
- **Card:** `[Sonnet · esforço medium · classe implementacao]`.

### R-05 — `backlog.py next` e `show` entregam o card inteiro ao despacho
- **Origem:** registro 19 (F, $ — inadequado). **Causa:** o teto `DB-7` corta o dossiê no meio (`Camada`, `Passos`, `Restrições`), e o condutor relê o range do plano.
- **Ação:** o `next` imprime o card inteiro (o teto passa a valer só para `## Achados` e `Notas de execução`), ou imprime só o cabeçalho, o range e o bloco `HANDOVER` e declara que o dossiê se lê pelo range; nunca a metade. A escolha vai à skill `passagem-de-bastao` (Parte 2, fonte 1).
- **Verificação:** `python .claude/tools/backlog.py next` sobre fixture com card de 80 linhas → sem a linha `… truncado (` dentro do dossiê; `pytest -k next` verde.
- **Card:** `[Sonnet · esforço low · classe implementacao]`.

### R-06 — O painel do gerente reconhece `python -X utf8 <script>`
- **Origem:** registros 25, 32 e 37 (E, C — inadequado). **Causa:** `progresso_hook.py:293-309` (`_programa`) pula tokens iniciados por `-` e toma o token seguinte como script; com `-X utf8` o "script" vira `utf8`.
- **Ação:** `_programa` conhece as flags do interpretador que levam valor (`-X`, `-W`, `-c`, `-m`) e pula o valor junto; TF com `python -X utf8 .claude/tools/backlog.py status X in-progress` gerando `M-2`; a armadilha entra em `docs/ARMADILHAS_DE_FERRAMENTA.md`.
- **Verificação:** `pytest tests/test_progresso_hook.py -k utf8` → 1 passed (antes: exit 5).
- **Card:** `[Sonnet · esforço low · classe implementacao]`.

### R-07 — `encerrar.py tarefa` transcreve o achado de processo do laudo como `AE-<n>`
- **Origem:** registro 29 (M, C — inadequado; falha medida nesta janela). **Causa:** o instrumento lê o pacote de cinco campos e ignora a tabela `## Achado de processo` do laudo; o `--achado` depende da memória do condutor.
- **Ação:** `encerrar.fechar_tarefa` lê a tabela `| alvo | achado |` do laudo e, para cada linha, grava `AE-<n>` com `**Rota:**` (a rota é o trecho depois de `Rota:` no texto), sem duplicar achado idêntico já presente; `--achado` continua para o que não veio do laudo.
- **Verificação:** `pytest tests/test_encerrar.py -k achado_do_laudo` → 1 passed; fechar tarefa de fixture cujo laudo tem 1 achado → `## Achados da execução` ganha `AE-1` com rota.
- **Card:** `[Sonnet · esforço medium · classe implementacao]`.

### R-08 — O veredito do marco é um comando
- **Origem:** registros 48 e 53 (F, M — inadequado). **Causa:** o `go`/`no-go` do dono no marco não tem escritor: `estado.tsv`, tabela *Marcos de validação*, decisão de emenda, `cenario.md` e `## 0` ficam defasados entre si.
- **Ação:** `encerrar.py marco --plano <p> --marco <n> --veredito "<frase>" [--aceita-versao <k> | --recusa-versao <k>]`: escreve a célula do marco na tabela, apensa o ato à `## 0` com data, tira o plano de `blocked` no Marco 1 e imprime o dossiê `Ato de modelo` de desfecho para o modelador quando há versão pendente.
- **Verificação:** `python .claude/tools/encerrar.py marco --help` exit 0; sobre fixture com `## 1A`, `--recusa-versao 2` imprime dossiê com `Ato: emenda` e a frase do dono em `Motivo`.
- **Card:** `[Sonnet · esforço medium · classe implementacao]`.

### R-09 — O hook de telemetria grava todo papel do kit
- **Origem:** registros 5, 31 e 55 (M, C). **Causa:** `telemetria_hook.py:51` só grava `pantonic-executor`; revisor, consultor, modelador, planejador e scout entram à mão (três números copiados por rodada) ou não entram, e o "consumo do plano" impresso ao dono subestimou 66%.
- **Ação:** o hook grava toda notificação `SubagentStop` de `subagent_type` `pantonic-*`, com `tarefa` = `<ID>-<papel>[-<n>]` (id lido de `tarefa-corrente.json` para o executor e do último `next` para os demais; planejador e modelador com o id do plano); `encerrar.py plano` soma por prefixo do plano e pelas linhas com o id do plano.
- **Verificação:** `pytest tests/test_telemetria_hook.py -k revisor` → 1 passed; após um despacho do revisor, `tail -1 docs/telemetria.tsv` traz `<ID>-revisao opus`.
- **Card:** `[Sonnet · esforço medium · classe implementacao]`.

### R-10 — Pré-voo mecânico do pedido antes de abrir o planejador
- **Origem:** registros 6 e 10 ($, F). **Causa:** uma premissa falsa no pedido (`ler_texto_utf8`) custou uma instância inteira do planejador (41k) mais a campanha para virar um fato de um grep.
- **Ação:** `.claude/tools/prevoo.py "<pedido>"` extrai todo caminho, símbolo `nome(` e flag citados no texto do dono, confere por existência e grep, e imprime `citado | existe | onde`; quem conduz roda antes do primeiro despacho do planejador e cola a tabela na `## 0` como fatos do pré-voo.
- **Verificação:** `python .claude/tools/prevoo.py "reutilizando a função ler_texto_utf8 de .claude/tools/caminhos.py"` → linha `ler_texto_utf8 | não | —`.
- **Card:** `[Sonnet · esforço medium · classe implementacao]`.

### R-11 — Profundidade da auto-auditoria do planejador pela classe do plano
- **Origem:** registros 11 e 15 ($). **Causa:** 319k tokens de planejador para 3 operações; a Fase 4 (14 itens) e o ensaio em cópia foram aplicados integralmente a um plano de ferramentaria trivial.
- **Ação (decisão do dono, muda o protocolo):** o cabeçalho do plano ganha `classe do plano` ∈ `{ferramentaria, doutrina, produto}`; a Fase 4 declara quais itens valem por classe (ex.: "parser frio" e a segunda leva só para plano com gramática; ensaio em cópia só com arquivo compartilhado tocado ou mais de N cards). Medir na série antes e depois.
- **Verificação:** dois planos de 3 operações, um por regime, com `tokens_k` do planejador na série; o de `ferramentaria` gasta menos.
- **Card:** `[Opus · esforço medium · classe redacao]`. Nasce `blocked` razão `dependencia`: decisão do dono.

### R-12 — O consultor lê só as três entradas, e `estrategico=` é uma frase
- **Origem:** registro 45 (C, $). **Causa:** o acionamento 1 leu o relatório da auditoria (fora do cenário) e custou 131k; o acionamento 2, com a instrução "não leia fora do cenário", custou 67k; `estrategico=` veio em três frases.
- **Ação:** o arquivo do `pantonic-consultant` fixa a regra de leitura (cenário, card, evidência e a doutrina que o cenário aponta; nada mais) e a forma de `estrategico=` em uma frase; a skill `scrum-master` (*Acionamento do consultor*) traz o molde do despacho com as três entradas.
- **Verificação:** `Select-String -SimpleMatch "uma frase" .claude/agents/pantonic-consultant.md` ≥ 2; `kit_check -Mode check-drift` exit 0.
- **Card:** `[Opus · esforço low · classe redacao]`.

### R-13 — `card_check` lê `estado.tsv` para derivar o mundo
- **Origem:** registro 20 (C). **Causa:** em plano em pasta o instrumento imprime `status ausente: comparando antes`; um card `done` seria comparado no mundo errado sem `--mundo`.
- **Ação:** `card_check.py` resolve o status pela linha da tarefa em `estado.tsv` (via `caminhos.estado_tsv`) quando o card não tem bullet `Status`.
- **Verificação:** `pytest tests/test_card_check.py -k estado_tsv` → 1 passed; sobre fixture em pasta com tarefa `done`, a saída diz `status done: comparando depois`.
- **Card:** `[Sonnet · esforço low · classe implementacao]`.

### R-14 — A recomendação do laudo viaja na primeira linha do revisor
- **Origem:** registro 27 (F). **Causa:** o bloco A roteia pela recomendação, mas a linha de retorno só traz veredito, percentual e bloqueante; o condutor abre o laudo a cada tarefa.
- **Ação:** a linha passa a `<tarefa> <veredito> <percentual> bloqueante=<d> recomendacao=<seguir|seguir com ressalva|refazer|escalar>`; o gancho do painel (`M-7`), a skill `scrum-master` (Passo 7) e o arquivo do revisor acompanham.
- **Verificação:** `pytest tests/test_progresso_hook.py -k M7` verde com a forma nova; `grep -c "recomendacao=" .claude/agents/pantonic-reviewer.md` ≥ 1.
- **Card:** `[Sonnet · esforço low · classe implementacao]`.

### R-15 — Um verbo `despachar` para os passos 3 e 4 do loop
- **Origem:** registro 34 (M). **Causa:** por despacho o condutor roda `modelo.py check`, `card_check`, `pytest --co`, `status in-progress`, escreve `tarefa-corrente.json` à mão e captura o `<ref>`: seis atos idênticos por tarefa.
- **Ação:** `backlog.py despachar <ID>` roda os gates mecânicos, materializa `in-progress`, grava `tarefa-corrente.json`, captura o `<ref>` e imprime o card inteiro, o `HANDOVER` e a linha `ref=<sha>`; recusa com a razão do primeiro gate que falhar.
- **Verificação:** sobre a fixture em pasta, `python .claude/tools/backlog.py despachar GAM-T1` → `ref=` presente e `estado.tsv` com `in-progress`.
- **Card:** `[Sonnet · esforço medium · classe implementacao]`.

### R-16 — `modelo.py check` afere a `## 1A`, e `--drift` mostra o contrato
- **Origem:** registros 49 e 50 (L). **Causa:** a versão pendente não passa por `V1..V21`; o drift só compara operações e estado final.
- **Ação:** o `check` roda o mesmo vocabulário sobre a `## 1A` quando ela existe (rótulo `1A:` nas violações); `show --drift` ganha a seção `## Objetos` com `[~]` por contrato ou propriedade alterada.
- **Verificação:** `pytest tests/test_modelo.py -k "pendente or drift"` verde; fixture com contrato alterado na `## 1A` → linha `[~] sonda — contrato`.
- **Card:** `[Sonnet · esforço medium · classe implementacao]`.

### R-17 — Esqueleto gerado para `operacoes.md`
- **Origem:** registro 51 ($). **Causa:** a skill `entrega-de-encerramento` descreve a estrutura, e cada plano a reescreve de memória.
- **Ação:** `encerrar.py operacoes --plano <p>` gera o esqueleto (abertura, arco com a tabela de tarefas lida do plano, uma seção por tarefa com os quatro blocos vazios, ganhos, defeitos, pendências), e a checagem de cobertura vira verbo do mesmo instrumento.
- **Verificação:** `python .claude/tools/encerrar.py operacoes --plano <fixture>` → arquivo com tantas seções `## \`<ID>\`` quantos cards.
- **Card:** `[Sonnet · esforço low · classe implementacao]`.

### R-18 — Os verificadores em PowerShell escrevem UTF-8 no console
- **Origem:** registro 2 (C, cosmético). **Causa:** `check-readme.ps1` imprime `vers�o`; um card que copie a saída como literal fixa o valor errado.
- **Ação:** `[Console]::OutputEncoding = [Text.Encoding]::UTF8` no topo dos `.ps1` de `.claude/checks/`, ou saída só em ASCII.
- **Verificação:** `pwsh .claude/checks/check-readme.ps1 | Select-String -SimpleMatch "versão"` → 1 linha.
- **Card:** `[Sonnet · esforço low · classe mecanica]`.

### Fora das recomendações, mas para o dono
- **Revisão da doutrina pendente (`GOVERNANCA.md` §7.1):** a skill `checar-versao-kit` acusou, ao registrar o plano fictício, que "Esgotar o backlog" (`P-0751`) e "Fato no ponto de uso" (`P-0752`) fecharam `done` sem rodada de revisão registrada (registro 15). Achado real, independente do plano fictício.
- **Os dois tíquetes do consultor** (defeitos reais do `review_evidence.py`, cards medidos): removidos na limpeza por colidirem com a diretiva de 2026-09-26; texto no Apêndice A. Decisão do dono: reabrir agora ou junto com as recomendações.

## 6. Custo medido da execução do plano fictício

Origem de todo número: o bloco `<usage>` da notificação de conclusão de cada subagente nesta sessão (2026-09-27), somado por papel na própria janela; nenhum valor de memória.

| papel | instâncias | tokens (k) | tool uses | duração (s) |
|---|---|---|---|---|
| planejador (Opus) | 3 | 319,0 | 79 | 1.823 |
| scout (Haiku) | 1 | 47,7 | 27 | 119 |
| modelador (Opus) | 3 | 202,9 | 33 | 395 |
| executor (Sonnet) | 3 | 174,9 | 46 | 553 |
| revisor (Opus) | 3 | 224,7 | 39 | 334 |
| consultor (Opus) | 2 | 198,6 | 59 | 843 |
| **total** | **15** | **1.167,8** | **283** | **4.067 (≈ 68 min)** |

Produto entregue: uma função de 3 linhas, um script de ~40 linhas, 8 testes, um README. Razão fase intelectual : execução = 946 : 175 ≈ 5,4 : 1. O contexto principal (orquestração e esta auditoria) não entra na tabela: não há instrumento que o meça (registro 57).

## 6a. Custo medido da criação do plano das recomendações (`P-0753-auditoria-estagio-1`)

Origem: `<usage>` das notificações desta sessão. Planejador (esqueleto) 124,1k / 21 tool uses / 462 s; modelador (autoria, 21 operações) 106,3k / 16 / 359 s; planejador (21 cards, `card_check` em todos, sem ensaio em cópia) 389,5k / 127 / 3.624 s. Total: 619,9k tokens, 164 tool uses, ≈ 74 min, para um plano de 21 cards. O gancho de ocupação disparou no meio (registro 57).

## 7. O que ficou na árvore e o que foi descartado

**Descartado (restaurado do retrato inicial de 2026-09-27, tirado antes do primeiro ato):** `docs/plans/P-0753-sonda-fantasma/` (plano, estado, RDO, laudos, evidência, cenário, operações, entrega), `scratch_fantasma/`, `tests/test_sonda_fantasma.py`, a função `ler_texto_utf8` em `.claude/tools/caminhos.py`, as linhas do plano fictício em `docs/DIARIO_DE_OBRAS.md` (cabeçalho, diretiva, índice, `TK-94`, `TK-95`), `docs/plans/_INBOX.md` (contador de volta a `P-0753`), `docs/plans/_INBOX_HISTORICO.md`, `docs/telemetria.tsv` (6 linhas `SF-*`) e `docs/ACIONAMENTOS_CONSULTOR.tsv` (2 linhas). Cópia integral dos artefatos descartados, fora do repositório: `%TEMP%\claude\auditoria\p0753_artefatos\`.

**Mantido:** este relatório e, criado depois dele a pedido do dono, o plano `docs/plans/P-0753-auditoria-estagio-1/` (plano em pasta, 21 cards: as 18 recomendações, os dois tíquetes do Apêndice A como `AF-T1`/`AF-T2`, e a revisão do README), `blocked` até o go do dono no Marco 1. O painel `.claude/estado/progresso.txt` (ignorado pelo git) guarda as linhas da janela.

**Conferência feita após a limpeza (2026-09-27):** `git status --porcelain` idêntico ao retrato inicial mais este arquivo; `pytest --co -q` = `452 tests collected`; `backlog.py check` OK; `modelo.py check` do `P-0752` OK; `dead_code` 0 achados; `kit_check -Mode check-drift` OK; `ler_texto_utf8` com 0 ocorrências; `backlog.py next` = nada delegável.

## Apêndice A — Os dois tíquetes abertos pelo consultor (texto verbatim, removidos na limpeza)

## TK-94 — O `--stat` do dossiê de evidência ignora o recorte `--desde`

- **Status:** `ready` · 2026-09-27 — aberto pelo consultor do `P-0753` (acionamento 1), rota do achado `AE-1` do plano (laudo da `SF-T1`; recorreu no laudo da `SF-T3`).

**Caso medido (2026-09-27):** no dossiê de evidência da `SF-T1` e no da `SF-T3` do `P-0753`, o bloco `## Diff (git diff --stat)` listou os 59 arquivos do WIP da árvore contra `HEAD`, nenhum da entrega, e deixou fora os alvos entregues, não rastreados; só `## Arquivos tocados` respeitou o `--desde`. Causa: `coletar_diff_stat(root)` roda `git diff HEAD --stat` e não recebe o `desde` que `montar_documento` já tem. Medido na árvore em 2026-09-27: o bloco de hoje tem 60 linhas (59 arquivos e o sumário); o protótipo do consultor (fora da árvore, sem tocar o instrumento), que grava a árvore de trabalho num índice temporário como `capturar_ref` faz e roda `git diff --stat <ref> <árvore> -- <tocados>`, deu, sobre o recorte `a1bea86` da `SF-T3`, 10 arquivos, os mesmos 10 de `## Arquivos tocados`, `scratch_fantasma/README.md` (não rastreado) incluído.

**O que decide:** correção conhecida — com `--desde`, o `--stat` sai do mesmo recorte dos tocados, não rastreados incluídos; sem `--desde`, nada muda. Card `TK-94a`, `ready`. Descartado: tirar o bloco do dossiê (o revisor perde a contagem de linhas por arquivo, que nenhum outro bloco dá).
- **Notas de execução:**
  - 2026-09-27 `ready` — aberto com o card TK-94a (consultor P-0753, acionamento 1)



### TK-94a — Com `--desde`, o `--stat` do dossiê sai do recorte dos tocados [Sonnet · esforço medium · classe implementacao]

- **Status:** `ready` · 2026-09-27
- **Objetivo:** em `.claude/tools/review_evidence.py`, com `--desde <ref>` informado, o bloco `## Diff (git diff --stat)` do dossiê lista exatamente os arquivos da seção `## Arquivos tocados` do mesmo recorte — rastreados e não rastreados —, cada um com as linhas mudadas desde `<ref>`; sem arquivo tocado, o bloco traz `(sem diferenças)`. Sem `--desde`, o bloco é o de hoje (`git diff HEAD --stat`).
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Contratos/classes:** `coletar_diff_stat(root: Path, desde: str | None = None) -> str`, e `montar_documento` repassa o `desde` que já recebe. Com lista de tocados vazia, o `git diff` não roda sem caminho (sem caminho ele devolveria a árvore inteira). Árvore de trabalho, índice real e lista de stash saem como entraram. O cabeçalho do bloco não muda.
- **Caso medido que motivou:** ver `## TK-94`.
- **Testes (novos, em `tests/test_review_evidence.py`):** TF `test_tf_diff_stat_desde_recorta_como_os_tocados` — repositório temporário com baseline commitado; um rastreado alterado antes da captura (WIP alheio); `<ref>` por `capturar_ref`; depois, um rastreado alterado e um não rastreado criado: o bloco `## Diff` de `montar_documento(..., desde=<ref>)` cita os dois arquivos da entrega e não cita o WIP alheio. TR `test_tr_diff_stat_desde_sem_tocados_sai_sem_diferencas` — `<ref>` capturado e nada mudado depois: o bloco traz `(sem diferenças)`.
- **Verificação:**
  1. `python -m pytest tests/test_review_evidence.py -q -k "diff_stat_desde"` → verde — antes `exit 5`, depois `exit 0`.
  2. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`.
  3. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `kit_check: check-drift OK` — antes `exit 0`, depois `exit 0`.
- **Pronto quando:** com `--desde`, o `--stat` do dossiê cobre o mesmo recorte dos tocados, com o não rastreado da entrega e sem o WIP alheio (Verificação 1); sem `--desde`, nada muda e a suíte segue verde (Verificação 2). Referência histórica, não piso: suíte `460 passed` na autoria (2026-09-27); o piso é o total re-medido no despacho mais os 2 testes novos.
- **Não fazer:** não mudar `coletar_arquivos_tocados` nem `capturar_ref` (os `AE-93` e `AE-94` do `TK-93` têm rota na auditoria final); não tocar `_REGISTRO_ORQUESTRACAO` (é do `TK-95a`); não mudar o cabeçalho do bloco nem o teto de caracteres dos trechos; não usar `git stash push` nem nada que escreva na árvore, no índice real ou na lista de stash.
- **Contingências:**
  - se um teste existente de `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.

## TK-95 — O relatório de auditoria do condutor cai como fora dos alvos na evidência

- **Status:** `ready` · 2026-09-27 — aberto pelo consultor do `P-0753` (acionamento 1), rota do achado `AE-2` do plano (laudo da `SF-T3`).

**Caso medido (2026-09-27):** a evidência da `SF-T3` do `P-0753` (`--desde a1bea86`) deu `docs/audits/AUDITORIA_ENCERRAMENTO_ESTAGIO1_2026-09-27.md` como "fora dos alvos e sem atribuição" e deixou o veredito mecânico aberto: o arquivo é o relatório da auditoria que o condutor escrevia na janela, não entrega do card. O revisor reconciliou à mão porque o condutor lembrou de avisar no despacho (linha 41 do relatório: a reconciliação dependeu de memória). `_REGISTRO_ORQUESTRACAO` tem `docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/plans/` e `docs/RDO/`, e não `docs/audits/`, onde a orquestração grava auditoria (`audit-sweep`, auditoria de encerramento). Protótipo do consultor (fora da árvore): com `docs/audits/` no balde, a mesma evidência sai `conforme`, com zero arquivos sem atribuição.

**O que decide:** correção conhecida — `docs/audits/` entra no balde de registro da orquestração; a precedência não muda, e card cujo alvo mora em `docs/audits/` segue coberto. Card `TK-95a`, `ready`, depois do `TK-94a` (os dois tocam `review_evidence.py` e o arquivo de teste dele). Descartado: a declaração de WIP da orquestração no despacho — ainda depende de o condutor lembrar de declarar, o mesmo defeito medido, e só o que ele declarasse sairia do vermelho. Edição do condutor fora de `docs/audits/` na janela segue para a reconciliação do revisor (passo 3a), que é o comportamento certo do instrumento: ele não adivinha autoria.
- **Notas de execução:**
  - 2026-09-27 `ready` — aberto com o card TK-95a (consultor P-0753, acionamento 1)



### TK-95a — `docs/audits/` entra no balde de registro da orquestração [Sonnet · esforço low · classe implementacao]

- **Status:** `ready` · 2026-09-27
- **Depende de:** `TK-94a`
- **Objetivo:** em `.claude/tools/review_evidence.py`, arquivo sob `docs/audits/` tocado fora dos alvos do card cai no balde de registro da orquestração de `confrontar_escopo`, no dossiê e no `--atribuir`; a docstring do módulo e a de `_eh_registro_orquestracao` nomeiam a pasta junto com as de hoje (texto em `Passos`). Arquivo de `docs/audits/` que é alvo do card segue coberto.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Passos:**
  1. Na docstring do módulo, o trecho depois de `antigo:` vira o trecho depois de `novo:` (sem quebra nova e sem refluxo; o rótulo não entra no arquivo):

     ```text
     antigo: `docs/plans/`, `docs/RDO/`); ato do dono fora
     novo: `docs/plans/`, `docs/RDO/`, `docs/audits/`); ato do dono fora
     ```
  2. Na docstring de `_eh_registro_orquestracao`, idem:

     ```text
     antigo: telemetria, plano, RDO. Não é atribuível
     novo: telemetria, plano, RDO, relatório de auditoria. Não é atribuível
     ```
- **Caso medido que motivou:** ver `## TK-95`.
- **Testes (novos, em `tests/test_review_evidence.py`):** TF `test_tf_relatorio_de_auditoria_sai_como_registro_da_orquestracao` — `docs/audits/AUDITORIA_X.md` tocado fora dos alvos de `T1`: o documento traz `Registro da orquestração (não atribuível a tarefa)` e `Veredito mecânico: conforme`. TR `test_tr_relatorio_de_auditoria_alvo_do_card_segue_coberto` — card cujo alvo é `docs/audits/AUDITORIA_X.md`: a atribuição do arquivo é `da entrega`.
- **Verificação:**
  1. `python -c "import importlib.util as u;from pathlib import Path;s=u.spec_from_file_location('r',Path('.claude/tools/review_evidence.py'));m=u.module_from_spec(s);s.loader.exec_module(m);print(m._eh_registro_orquestracao('docs/audits/AUDITORIA_X.md'))"` → `True` — antes `False`, depois `True`.
  2. `python -c "from pathlib import Path;c=chr(96);t=Path('.claude/tools/review_evidence.py').read_text(encoding='utf-8');print(t.count(c+'docs/RDO/'+c+')'),t.count(c+'docs/RDO/'+c+', '+c+'docs/audits/'+c+')'),t.count('plano, RDO, relatório de auditoria'))"` → `0 1 1` — antes `1 0 0`, depois `0 1 1`.
  3. `python -m pytest tests/test_review_evidence.py -q -k "auditoria"` → verde — antes `exit 5`, depois `exit 0`.
  4. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`.
  5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `kit_check: check-drift OK` — antes `exit 0`, depois `exit 0`.
- **Pronto quando:** arquivo de `docs/audits/` fora dos alvos não pesa no veredito e sai nomeado como registro da orquestração, e o que é alvo do card segue coberto (Verificação 1 e 3); as duas docstrings nomeiam a pasta (Verificação 2). Referência histórica, não piso: suíte `460 passed` na autoria (2026-09-27); o piso é o total re-medido no despacho mais os 2 testes novos.
