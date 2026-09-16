# Custo do pickup — medida por fonte

Portador durável entre as tarefas de `P-0736`. Cada tarefa acrescenta sua seção; nenhuma
reescreve a anterior (`DC-5`). Sonda: `sonda_pickup.py` (scratchpad, descartável, `DC-4`).

## 1 Pickup típico medido

Definição (`DC-2`): sessão nova de orquestração no `PantonicApp`, do turno zero até o dossiê da
próxima tarefa em mãos, sem executá-la. Compreende só: (a) custo fixo de entrada — doutrina
global, índice de memória + memórias indexadas, definição do agente, skill do fluxo; (b)
drenagem dos dois inboxes; (c) diretiva de prioridade no topo do diário; (d) apuração da fila
corrente; (e) dossiê da tarefa no plano corrente.

HEAD medido: `1a9645a` · Data: 2026-08-22.

## 2 Orçamento por fonte

Unidade (`DC-3`): chars é a medida primária; tokens estimados = chars ÷ 4 (nunca só tokens).
Ranking (`DC-8`): decrescente por **chars ingeridos** no pickup típico; empate = ordem de
leitura. `ingerido=0` com nota "fora de DC-2" = medido para referência, não lido no pickup.

| fonte | linhas | chars(arquivo) | tokens~ | maior linha (chars) | linhas>2000c | **ingerido** |
|---|---|---|---|---|---|---|
| docs/plans/_INBOX.md | 231 | 21.505 | 5.376 | 129 (114c) | 0 | **21.505** |
| docs/plans/P-0736-custo-do-pickup.md | 225 | 19.872 | 4.968 | 59 (669c) | 0 | **19.872** |
| .claude/skills/diario-de-obras/SKILL.md | 232 | 16.178 | 4.044 | 3 (270c) | 0 | **16.178** |
| .claude/skills/proximo-passo/SKILL.md | 195 | 15.081 | 3.770 | 3 (351c) | 0 | **15.081** |
| .claude/global/CLAUDE.md | 156 | 9.546 | 2.386 | 57 (98c) | 0 | **9.546** |
| memórias indexadas (soma de 5) | 137 | 8.488 | 2.122 | 262c | 0 | **8.488** |
| docs/DIARIO_DE_OBRAS.md | 2.493 | 299.643 | 74.911 | 35 (10.528c) | 14 | **5.859** (c+d) |
| memory/_INBOX.md | 16 | 967 | 242 | 16 (484c) | 0 | **967** |
| memory/MEMORY.md | 5 | 817 | 204 | 3 (183c) | 0 | **817** |
| docs/DIARIO_HISTORICO.md | 3.023 | 272.074 | 68.018 | 694 (1.347c) | 0 | 0 |
| CLAUDE.md (raiz) | ausente | ausente | ausente | ausente | ausente | 0 |
| .claude/agents/pantonic-auditor-arch.md | 108 | 6.755 | 1.689 | 3 (232c) | 0 | 0 |
| .claude/agents/pantonic-auditor-cleancode.md | 62 | 3.399 | 850 | 3 (251c) | 0 | 0 |
| .claude/agents/pantonic-benchmarker.md | 83 | 5.512 | 1.378 | 3 (288c) | 0 | 0 |
| .claude/agents/pantonic-executor.md | 61 | 4.437 | 1.109 | 3 (212c) | 0 | 0 |
| .claude/agents/pantonic-fora-da-caixa.md | 73 | 4.223 | 1.056 | 3 (286c) | 0 | 0 |
| .claude/agents/pantonic-planner.md | 42 | 2.503 | 626 | 3 (240c) | 0 | 0 |
| .claude/agents/pantonic-reviewer.md | 97 | 6.079 | 1.520 | 3 (231c) | 0 | 0 |
| .claude/agents/pantonic-scout.md | 34 | 1.801 | 450 | 3 (224c) | 0 | 0 |
| .claude/agents/* (subtotal 8) | 560 | 34.709 | 8.677 | 288c | 0 | 0 |
| docs/DOC_MAP.md | 102 | 6.212 | 1.553 | 54 (97c) | 0 | 0 |
| GOVERNANCA.md | 898 | 71.792 | 17.948 | 97 (684c) | 0 | 0 |
| docs/plans/P-0734-execucao-autonoma.md | 4.688 | 373.233 | 93.308 | 60 (2.290c) | 1 | 0 |

**Total chars ingeridos = 98.313 (~24.578 tokens).**

**Recorte a — seções `## ` do diário por chars** (6 seções, sem resto): P-0734 Execução
autônoma 182.203 · Índice 83.162 · P-0735 Residência e ponto de carga 27.300 · P-0733 Quitação
da dívida 1.578 · (preâmbulo) 1.500 · P-0736 Custo do pickup 1.234.

**Recorte b — top10 linhas do diário por chars:** L35/10.528c "P-0734-EXA / Execução autônoma —
o backlog deixa de..." · L66/3.170c "TK-26" · L84/3.106c "TK-43" · L36/3.088c "P-0735-RPC" ·
L79/2.953c "TK-38" · L85/2.879c "TK-45" · L74/2.869c "TK-33" · L73/2.782c "TK-32" · L77/2.713c
"TK-36" · L78/2.448c "TK-37".

**Recorte c — seções sem status vivo (candidatas `H5`):** 3 de 6 — (preâmbulo), P-0735 Residência
e ponto de carga, P-0736 Custo do pickup.

**Recorte d — linhas `Próxima tarefa`:** 39 matches, 4.358 chars somados.

**Recorte e — `docs/plans/_INBOX.md`:** 231 linhas totais, 212 sem marca `[drenado]`.

**Achados (divergência doc × medida, sem conserto):**
- `docs/DOC_MAP.md` linha 7 lista `docs/DIARIO_DE_OBRAS.md` como "abaixo de 500 linhas"; medido
  2.493 linhas (~5x).
- `docs/DOC_MAP.md` linha 7 lista `GOVERNANCA.md` como "abaixo de 500 linhas"; medido 898 linhas.
- `docs/DOC_MAP.md` linha 15 estima `docs/DIARIO_HISTORICO.md` em "~970 linhas" (referência de
  2026-08-05); medido 3.023 linhas.

## 3 Orçamento por passo do roteiro

Fonte: `.claude/skills/proximo-passo/SKILL.md` §Fluxo, passos 1-3 (`DC-2`: pickup termina antes
do passo 4 "Delegar"). Custo fixo de entrada roda antes do passo 1.

| ordem | passo | fonte | obrig./cond. | forma | chars | tokens~ |
|---|---|---|---|---|---|---|
| 0a | custo fixo — doutrina global | .claude/global/CLAUDE.md | obrigatório | integral | 9.546 | 2.386 |
| 0b | custo fixo — skill do fluxo | .claude/skills/proximo-passo/SKILL.md | obrigatório | integral | 15.081 | 3.770 |
| 0c | custo fixo — índice de memória | memory/MEMORY.md | obrigatório | integral | 817 | 204 |
| 0d | custo fixo — memórias indexadas (5) | memory/*.md (soma) | obrigatório | integral | 8.488 | 2.122 |
| 0e | custo fixo — definição do agente | CLAUDE.md (raiz) | condicional | integral | 0 (ausente) | 0 |
| P1a | drenar inbox de planos | docs/plans/_INBOX.md | obrigatório | integral | 21.505 | 5.376 |
| P1b | drenar inbox de planos (operação) | diario-de-obras/SKILL.md L174-182 | obrigatório | Grep+Read parcial | 870 | 218 |
| P1c | drenar fila de memória | memory/_INBOX.md | obrigatório | integral | 967 | 242 |
| P2 | ler diretiva de priorização | docs/DIARIO_DE_OBRAS.md L1-3 | obrigatório | sonda (Read offset/limit) | 161 | 40 |
| P3a | apurar fila corrente | docs/DIARIO_DE_OBRAS.md (Grep "Próxima tarefa da sprint" -A2) | obrigatório | Grep+Read parcial | 150 | 38 |
| P3b | ler dossiê da tarefa escolhida | docs/plans/P-0736-custo-do-pickup.md | obrigatório | integral | 19.872 | 4.968 |

**Orçamento medido do pickup típico = 77.457 chars (~19.364 tokens)** — soma dos 10 passos
obrigatórios (0a-0d, P1a-c, P2, P3a-b); 0e é condicional e soma 0 no caso medido (arquivo
ausente). Decomposição fecha exatamente no total.

## 4 Hipóteses H1..H5

- **H1** (célula do diário acumula narrativa do plano, P-0734 lida só p/ status/âncora):
  confirmada — diário ingerido = 5.859 de 299.643 chars (2%) no pickup medido; P-0734
  (182.203c, maior seção) não lido além de trechos pontuais (T1, Recorte a+c).
- **H2** (_INBOX.md append-only, lido integral p/ drenar zero/uma linha): parcial — mecanismo
  confirmado (21.505c/231 linhas, sem ponteiro incremental), mas volume diverge da hipótese:
  212/231 linhas sem marca `[drenado]` (T1, Recorte e), não zero/uma.
- **H3** (fila sem ponteiro estável, varredura devolve ~200 matches históricos): refutada —
  grep exato do roteiro (`Próxima tarefa da sprint`, `proximo-passo/SKILL.md:54`) devolve
  **1 match** no diário ativo (L2485), não ~200; ponteiro é estável.
- **H4** (custo fixo de entrada consumido antes de leitura de projeto): confirmada — 33.932
  chars (0a-0d) ingeridos antes de tocar qualquer inbox/diário do projeto = 43,8% do
  orçamento total.
- **H5** (seção terminal P-0735 13/13 done fora do histórico): confirmada — P-0735 ocupa
  27.300 chars no diário ativo (9,1% de 299.643), não condensada em `DIARIO_HISTORICO.md`
  (T1, Recorte a).

## 5 Rota candidata por fonte

Rotas (`DC-7`, conjunto fechado): `condensar` · `ponteiro` · `gerar-por-instrumento` ·
`mover-ao-historico` · `manter`. Nenhuma implementada aqui (`DC-1`). `ingerido` = valor refinado
da `## 3` (fatia efetiva); diverge da `## 2` em duas fontes (diário 5.859→311;
`diario-de-obras/SKILL.md` 16.178→870). % sobre 77.457, arredondado.

| fonte | ingerido | % | rota | o que se perde | grandeza |
|---|---|---|---|---|---|
| docs/plans/_INBOX.md | 21.505 | 27,8 | gerar-por-instrumento | nada — o arquivo segue íntegro e consultável sob demanda | implementacao |
| docs/plans/P-0736-custo-do-pickup.md | 19.872 | 25,7 | gerar-por-instrumento | o contexto adjacente do plano, hoje ingerido junto do dossiê | implementacao |
| .claude/skills/proximo-passo/SKILL.md | 15.081 | 19,5 | condensar | o racional medido que acompanha cada guardrail no corpo | mecanica |
| .claude/global/CLAUDE.md | 9.546 | 12,3 | condensar | o *Motivo* em prosa das 8 regras | mecanica |
| memórias indexadas (soma de 5) | 8.488 | 11,0 | ponteiro | o corpo da memória fora do contexto até ser pedido | mecanica |
| memory/_INBOX.md | 967 | 1,2 | manter | — | — |
| .claude/skills/diario-de-obras/SKILL.md | 870 | 1,1 | manter | — | — |
| memory/MEMORY.md | 817 | 1,1 | manter | — | — |
| docs/DIARIO_DE_OBRAS.md | 311 | 0,4 | condensar | a narrativa acumulada na coluna *Título* do índice | mecanica |
| docs/DIARIO_HISTORICO.md | 0 | 0 | manter | — | — |
| CLAUDE.md (raiz) | 0 (ausente) | 0 | manter | — | — |
| .claude/agents/pantonic-auditor-arch.md | 0 | 0 | manter | — | — |
| .claude/agents/pantonic-auditor-cleancode.md | 0 | 0 | manter | — | — |
| .claude/agents/pantonic-benchmarker.md | 0 | 0 | manter | — | — |
| .claude/agents/pantonic-executor.md | 0 | 0 | manter | — | — |
| .claude/agents/pantonic-fora-da-caixa.md | 0 | 0 | manter | — | — |
| .claude/agents/pantonic-planner.md | 0 | 0 | manter | — | — |
| .claude/agents/pantonic-reviewer.md | 0 | 0 | manter | — | — |
| .claude/agents/pantonic-scout.md | 0 | 0 | manter | — | — |
| .claude/agents/* (subtotal 8) | 0 | 0 | manter | — | — |
| docs/DOC_MAP.md | 0 | 0 | manter | — | — |
| GOVERNANCA.md | 0 | 0 | manter | — | — |
| docs/plans/P-0734-execucao-autonoma.md | 0 | 0 | manter | — | — |

O diário não recebe `manter` apesar da `H3` refutada: a refutação atinge só a apuração da fila —
`H1` e `H5` seguem confirmadas e é delas que sai a rota. **Achado, sem conserto:** o passo `P3a`
modela a fila em 150 chars por grep de âncora, mas o índice (83.162 chars, célula máxima de
10.528) é lido para status, âncora e denominador; o orçamento medido é piso, não teto.

## 6 Orçamento-alvo proposto

Forma (`DC-8`): fração da janela nominal de 200k tokens (800.000 chars), com o teto de trabalho
de ~50% da janela (Regra 2) em 100.000 tokens / 400.000 chars.

- **Alvo do pickup completo: 40.000 chars (10.000 tokens)** — 5% da janela, 10% do teto.
- **Folga de execução: 360.000 chars (90.000 tokens)** — 90% do teto livre para a tarefa.
- **Medido: 77.457 chars (19.364 tokens)** — 19,4% do teto de trabalho.
- **Redução exigida: 37.457 chars (~9.364 tokens), −48,4%.**
- **Fontes que a entregam:** `docs/plans/_INBOX.md` (21.505) + dossiê do plano corrente (19.872)
  = 41.377 chars, 53,4% do orçamento — as duas maiores sozinhas cobrem a redução.

## 7 Anatomia de uma janela de orquestração

Sonda: `sonda_janela.py` (scratchpad, descartável, `DX-4`). Corpus: janelas de orquestração
principal (não subagente) que citam `AUT-T5b` e nasceram em 2026-08-22, raiz de
`C:\Users\panta\.claude\projects\d--workspaces-PantonicApp\*.jsonl`, ordenadas por timestamp.
Três encontradas, nenhuma `ausente`.

| janela | arquivo (hh:mm) | 1º `usage` (`DX-5`) | final | turnos | `tool_use` | cruza 100k | fixo | variável |
|---|---|---|---|---|---|---|---|---|
| 1 | 08a29a54 15:04 | **34.260** | 98.865 | 48 | 28 | não cruzou | 34.260 | 64.605 |
| 2 | a7432333 19:55 | **34.292** | 123.507 | 46 | 26 | turno 26 | 34.292 | 89.215 |
| 3 | 29dd40a9 20:06 | **45.872** | 114.847 | 51 | 27 | turno 43 | 45.872 | 68.975 |

Top contribuintes por `tool_result` (3 de 10 medidos por janela, chars):
- J1: `Read` DIARIO_DE_OBRAS.md 31.285c (n=3) · `Read` _INBOX.md 25.665c (n=1) · `Read`
  P-0737-loop-autonomo.md 10.186c (n=4).
- J2: `Read` DIARIO_DE_OBRAS.md 61.006c (n=3) · `Read` _INBOX.md 25.665c (n=1) · `Grep`
  "Próxima tarefa" 13.981c (n=1).
- J3: `Read` _INBOX.md 25.665c (n=1) · `Read` review_evidence.py 14.652c (n=3) · `Read`
  P-0737-loop-autonomo.md 13.675c (n=2).

O que havia sido ingerido até o turno de cruzamento (soma por ferramenta): J2/turno 26 —
`Read` 108.940c, `Grep` 16.389c, `PowerShell` 113c; J3/turno 43 — `Read` 65.446c, `Grep`
5.490c, `PowerShell` 418c. `Read` domina os dois cruzamentos; J1 não cruza dentro dos 48
turnos medidos.

**Fixo × variável:** o primeiro `usage` — custo de abrir a janela, antes de qualquer ato de
tarefa — já mede 34.260–45.872 tokens, 17,1%–22,9% da janela nominal de 200k **antes do
turno 1 de trabalho**. É maior que o pickup típico da `## 3` (19.364 tokens) porque aquele
número isola só o texto dos passos de protocolo; o primeiro `usage` real soma isso ao
overhead de serialização (system prompt, ferramentas registradas, ids) que a medida por
chars de arquivo não captura. É aqui que o vão do `P-0736` fecha: o pickup medido é piso
porque não inclui o custo fixo de instanciar a janela em si.

**Atribuição do crescimento até 100k:** nas duas janelas que cruzam, o maior bloco recorrente
não é arquivo novo — é releitura do mesmo arquivo dentro da própria janela
(`DIARIO_DE_OBRAS.md` n=3, `P-0737-loop-autonomo.md` n=2-4, mesmo `_INBOX.md` de 25.665c
reaparecendo por completo a cada corte). Reforça a `H1`/`H2` da `## 4`: o custo não nasce de
ingerir fonte nova, nasce de reingerir a mesma sem ponteiro incremental.

## 8 A série: custo por papel e custo do controle

Sonda: `sonda_janela.py` (scratchpad, estendida da `CTX-T2`). Fontes: `docs/telemetria.tsv`
(196 linhas) e sessões-raiz/subagente de
`C:\Users\panta\.claude\projects\d--workspaces-PantonicApp\`.

**1. Custo fixo por papel** (mediana do 1º `usage` de janela de subagente, por `agentType`):
`pantonic-executor` n=149 · 34.016 tok · `pantonic-planner` n=15 · 13.980 tok ·
`pantonic-benchmarker` n=16 · 10.352 tok · `context-scout` n=13 · 9.150 tok ·
`pantonic-scout` n=10 · 8.340 tok · `pantonic-reviewer` n=1 · 13.995 tok. Papéis Opus
(planner/reviewer) custam ~4x mais para abrir que os scouts (Haiku), antes de qualquer ato.

**2. Janelas por tarefa atômica** — contagem bruta (citação em qualquer sessão histórica)
infla por releitura de diário; corrigida pelo dia de execução (`data` da telemetria), mesmo
método `DATA_ALVO` da `CTX-T2`: `AUT-T5b` consome **5** janelas no dia — não é caso isolado:
`AUT-T1` (tarefa `mecanica`, teto 20) consome **8**, `RPC-T2`/`RPC-T3` **13** cada, `RPC-T4`
**12**, `RPC-T5` **11**. Padrão, não exceção — a maioria das tarefas atômicas do `P-0735`/
`P-0737` reabre janela mais de uma vez no mesmo dia.

**3. Os três números do `TK-32`** (regime do teto no cabeçalho, enquanto existiu — `EXA-*`/
`RPC-*`/`AUT-*` resolvidos por `classe`/`teto` extraído dos cabeçalhos de `P-0734`/`P-0735`/
`P-0737`; leitura histórica, não gera rota):
- **(i)** cruzamentos por classe — `redacao`: n=40, cruzou=13, excedente total=85 (méd. 6,5/
  tarefa) · `implementacao`: n=23, cruzou=6, excedente=41 (méd. 6,8) · `mecanica`: n=3,
  cruzou=**3/3**, excedente=19 (méd. 6,3) · `investigacao`: n=2, cruzou=1, excedente=6.
- **(ii)** `Grep` de `parad[ao] por teto|bloque\w* por teto|incompleta por teto|recusad[ao]
  por teto|escalad[ao] por teto` (case-insensitive) no diário + `P-0734`/`P-0735`/`P-0737`:
  **0 ocorrências em 4 arquivos** — nenhum dos 23 cruzamentos achou registro de a consequência
  antes prescrita (rota `A4`, removida do roteamento do `scrum-master`) ter de fato disparado.
- **(iii)** custo do próprio controle: **198 tool_uses** (n=5) — `EXA-T3` (política de tetos)
  26 · `EXA-T4` (gramática classe/teto) 34 · `EXA-TK32-insumo` (insumo do regime interino) 44
  · `CTX-T1c`/`CTX-T1d` (as duas correções medidas do gate de delegação) 32+62.

**4. Estado do `TK-23`(b)** — `telemetria.tsv` tem 8 colunas (`data, projeto, tarefa, modelo,
tool_uses, tokens_k, duracao_s, fonte`), nenhuma de sessão/janela: **não medível só por ela**.
Pelos transcripts brutos (mesmo corpus do item 2), sim: as 3 janelas `AUT-T5b`/2026-08-22 já
selecionadas citam **8, 15 e 14** marcadores de tarefa distintos cada — várias tarefas
atômicas dividem uma janela, com número.

## 9 Causas raízes e veredito do dono (2026-08-23)

Insumo: `## 7` e `## 8`; rotas do conjunto fechado da `DX-6`. As 9 causas, os 3 vereditos e as 9
rotas foram **ratificados pelo dono em 2026-08-23**, na forma proposta.

| # | causa | evidência | artefato-alvo | rota | ganho tok/janela | grandeza |
|---|---|---|---|---|---|---|
| C1 | papel caro instanciado para trabalho de papel barato | executor 34.016 tok (n=149) × `pantonic-scout` 8.340 (n=10) = 4,1× | `.claude/skills/proximo-passo/SKILL.md`, passo 4 | `delegar` | ~25.700 por varredura movida | comportamental |
| C2 | custo fixo de protocolo não amortiza entre tarefas | 1º `usage` 34.260 e 34.292, Δ=32 tok; texto de protocolo = 33.723c | janela de orquestração (`GOVERNANCA.md` §4.3) | `amortizar` | ~8.400 da 2ª tarefa em diante | comportamental |
| C3 | diário relido dentro da própria janela | J2 61.006c (n=3) = 15.252 tok; J1 31.285c (n=3) | `docs/DIARIO_DE_OBRAS.md` (341.964c, 2.935 l.) | `condensar` | 7.800 (piso) a 15.252 | mecanica |
| C4 | inbox lido integral e reingerido a cada corte | 25.665c (n=1) nas três janelas; 291 de 292 linhas já `[drenado]` | `docs/plans/_INBOX.md` (27.381c) | `mover-ao-historico` | ~6.600 | mecanica |
| C5 | verificação de entrega à mão, no contexto mais caro | J3 leu `review_evidence.py` 14.652c (n=3); `pantonic-reviewer` n=1 × executor n=149 | `.claude/tools/review_evidence.py`; `.claude/agents/pantonic-reviewer.md` | `delegar` | ~3.700 | comportamental |
| C6 | fila corrente sem ponteiro estável | `Grep "Próxima tarefa"` 13.981c numa chamada; 39 linhas casadas, 1 vigente | `docs/DIARIO_DE_OBRAS.md`; `proximo-passo/SKILL.md`, passo 3 | `ponteiro` | ~3.500 | mecanica |
| C7 | dossiê do plano corrente reingerido inteiro | J1 10.186c (n=4); J3 13.675c (n=2); `P-0738` integral = 19.615 tok | `docs/plans/P-*.md` | `ponteiro` | 2.500–3.400 | comportamental |
| C8 | skill de orquestração maior que a skill de pickup e que o global | 22.443c (5.611 tok), 336 l. × 15.070c da skill de pickup e 10.165c do `CLAUDE.md` global | `.claude/skills/scrum-master/SKILL.md` | `condensar` | ~2.800 | mecanica |
| C9 | `TK-23`(b), contador de tarefas por janela | 3 janelas citam 8, 15 e 14 marcadores; `telemetria.tsv` sem coluna de sessão | `.claude/tools/ocupacao.py` | `manter` | 0 | mecanica |

**Custo de abrir uma janela hoje (`DX-5`):** primeiro `usage` de `assistant` em **34.260 · 34.292 ·
45.872 tokens** — 17,1%–22,9% da janela nominal, antes de qualquer ato.

**Vereditos dos três diagnósticos preliminares** (§0 do plano), todos **`confirmado`**:
- **(i)**, metade medível: J3 abriu em 45.872 tok — 33,9% acima de J1 —, gastou 51 turnos e 27
  `tool_use` e entregou 2 edits deixando a telemetria pendente; `AUT-T5b` consome 5 janelas no dia,
  `RPC-T2`/`T3` 13, `RPC-T4` 12, `RPC-T5` 11.
- **(ii)**: Δ de 32 tokens entre os primeiros `usage` de J1 e J2, e o mesmo `_INBOX.md` de 25.665c
  reaparece completo nas três janelas.
- **(iii)**: `pantonic-reviewer` instanciado 1 vez em toda a série contra 149 do executor, e o
  instrumento foi lido 3× em vez de executado.

**Alvo — recusado pelo dono em 2026-08-23, verbatim:** *"Não aceito valores sem respaldo teórico. Se
é um número mágico, ignorar."* Caem os dois: o default de 40.000 chars / 10.000 tokens da `DX-11` e a
proposta de 1º `usage` ≤ 25.000 tokens. Nenhuma constante nova entra. O único número com proveniência
declarada é o da `DX-13` — ocupação de ~50%, tolerância a 60%, vinda da literatura de decaimento de
desempenho por enchimento de contexto e revisável se ela indicar outro valor. **Critério vigente para
a `CTX-T10`:** aferição **relativa e sem constante** — medir o mesmo `DX-5` depois das rotas e
comparar com o antes registrado nesta seção.

## 10 Aferição (2026-08-24)

Sonda: `sonda_janela.py` (scratchpad, descartável). Corpus: primeira janela de orquestração
principal aberta após o fechamento do último card do Estágio C (`CTX-T9`, `done`) —
`95db6421-3bbd-4938-b97d-f60a28435084.jsonl`, raiz de
`C:\Users\panta\.claude\projects\d--workspaces-PantonicApp\`.

| medida | valor |
|---|---|
| 1º `usage` (`DX-5`) | **46.071** |
| último `usage` no despacho (esta chamada) | 94.393 |
| entradas `assistant` com `usage` | 32 |

**(a) novo × antes** (`## 9`: 34.260 · 34.292 · 45.872, mediana 34.292): novo `DX-5` = 46.071 —
Δ vs. mediana = +11.779 tok (+34,4%); Δ vs. melhor caso (34.260) = +11.811 tok (+34,5%); Δ vs.
pior caso antes (45.872) = +199 tok (+0,4%, ainda acima). Nas três comparações o número **subiu**,
não desceu. **Veredito (a): sem redução** — a rodada Estágio C não baixou o custo fixo de abrir a
janela; esta janela abriu mais cara que qualquer uma das três medidas em `## 7`/`## 9`.

**(b):** confirmado pelo orquestrador no fechamento — esta janela (`95db6421…`) abriu, drenou os
dois inboxes, apurou a fila, delegou `CTX-T10` ao `pantonic-executor` (o despacho medido acima),
fechou e registra telemetria sem reabrir contexto. **Veredito (b): sim**, numa única janela.

**Veredito da iniciativa:** (a) reprovado — a rodada Estágio C **não** reduziu `DX-5`, ele subiu
34,4%–34,5% contra o antes. (b) aprovado. Falhando (a), a rota **não se corrige aqui** (`DX-2`):
o gap vai para `## 9. Achados da execução` do plano, com tíquete — decisão do dono sobre a causa
do aumento é pré-requisito para qualquer nova rodada de rotas.

## 11 Composição do 1º usage (2026-08-24)

Sonda `sonda_dx5.py` (scratchpad, descartável). Corpus: 464 janelas de `C:\Users\panta\.claude\projects\d--workspaces-PantonicApp\` — 239 principais (`*.jsonl` na raiz) e 225 de subagente (`<sessão>/subagents/agent-*.jsonl`, papel lido do sidecar `.meta.json`, único lugar do corpus onde `agentType` existe de fato). **Fórmula calibrada:** `usage_1 = input_tokens + cache_creation_input_tokens + cache_read_input_tokens` — primeira testada, reproduziu as quatro do registro: `08a29a54`=34.260, `a7432333`=34.292, `29dd40a9`=45.872, `95db6421`=46.071.

**Tabela A — M1, dispersão (janelas principais, corte = início de `95db6421`):**

| grupo | n | mediana | mín | máx | p25 | p75 |
|---|---|---|---|---|---|---|
| antes | 233 | 34.347 | 0 *(1 chamada com usage zerado)* | 46.429 | 33.508 | 34.959 |
| depois | 6 | 46.070 | 34.644 | 46.401 | 37.500 | 46.076 |

46.071 cai no **percentil 94,8** do grupo antes (n=233).

**Tabela B — M2, visível × opaco (4 janelas canônicas, câmbio 0,590 chars/tok, M3/`principal`):**

| janela | usage_1 | chars_preâmbulo | visível (tok) | opaco (tok) |
|---|---|---|---|---|
| 08a29a54 | 34.260 | 11.684 | 19.788 | 14.472 |
| a7432333 | 34.292 | 11.684 | 19.788 | 14.504 |
| 29dd40a9 | 45.872 | 12.138 | 20.557 | 25.315 |
| 95db6421 | 46.071 | 11.683 | 19.786 | 26.285 |

Blocos: nas 4 janelas o texto armazenado não contém marcador `<system-reminder>`/`gitStatus:`/`<env>` — tudo cai em `pedido` (comando `/clear` + listagem de skills + pedido curto). Mediana `pedido` das 3 de 2026-08-22 = 11.684c; `95db6421` = 11.683c → **Δ pedido = −1c (≈0 tok)**. Mediana `opaco` das 3 = 14.504 tok; `95db6421` = 26.285 tok → **Δ opaco = +11.781 tok**.

**Tabela C — M3, regressão `usage_1 ~ chars_preâmbulo` (mínimos quadrados, Python puro; papéis n<10 — `pantonic-reviewer`, `claude`, `general-purpose` etc. — fora por n insuficiente):**

| papel | n | intercepto (tok) | inclinação (tok/char) | r² |
|---|---|---|---|---|
| principal | 239 | 17.155 | 1,694 | 0,030 |
| principal/antes | 233 | 19.056 | 1,513 | 0,025 |
| principal/depois | 6 | instável (n=6, sinal absurdo) | — | 0,0001 |
| pantonic-executor | 161 | 27.310 | 0,354 | 0,055 |
| pantonic-planner | 16 | 12.189 | 0,276 | 0,394 |
| pantonic-benchmarker | 16 | 10.211 | 0,556 | 0,972 |
| context-scout | 13 | 8.384 | 0,362 | 0,079 |
| pantonic-scout | 10 | 8.927 | −0,111 | 0,017 |

**Veredito:**
- visível (`chars_preâmbulo` convertido): **estável (Δ ≈ 0 tok, |Δ| < 500)**.
- opaco (resíduo `usage_1` − visível): **subiu 11.781 tok**.
- intercepto `principal` antes × depois: **não isolado** — falta medir com `depois` n≥30; n=6 dá regressão instável (r²≈0,0001).
- dispersão M1 (`antes`, n=233): **subiu** frente à mediana, mas **estável** frente ao máximo histórico (46.429 > 46.071).

**O Δ de +11.779 tok vs. mediana é carregado por `opaco`** (resíduo `usage_1` − visível; o visível ficou estável, Δ≈−1c/≈0 tok). **Dispersão: 46.071 está dentro do intervalo [mín, máx] da baseline estendida (n=233)** — no percentil 94,8, colado ao teto (`29dd40a9`, a 3ª janela do controle original, já tinha opaco 25.315 tok, próximo do `95db6421`; as outras duas do controle é que eram baixas).

## 12 Onde e quando o degrau do 1º usage acontece (2026-08-24)
Sonda `sonda_dx6.py` (scratchpad, descartável). Corpus: `C:\Users\panta\.claude\projects\` inteiro — principal = `*.jsonl` na raiz de um diretório de projeto, subagente = `<sessão>/subagents/agent-*.jsonl` (papel do sidecar `.meta.json`). Corte: início de `95db6421…` (mesmo corte da `## 11`). Fórmula: `usage_1 = input_tokens + cache_creation_input_tokens + cache_read_input_tokens`. **Gate:** reproduziu as 4 canônicas (34.260/34.292/45.872/46.071) e o grupo `antes` da Tabela A da `## 11` (n=233, mediana 34.347, máx 46.429) — **PASS**. `n_depois` medido hoje (`d--workspaces-PantonicApp`, fora do gate, decisão 3 da `TK-53a`): **9** (cresceu sobre o `n=6` da `## 11`). Tabela A — série diária (7 dias) a seguir:
| dia | n | mediana | n ≥ 40.000 |
|---|---|---|---|
| 2026-08-18 | 3 | 34.967 | 0 |
| 2026-08-19 | 10 | 35.012,5 | 3 |
| 2026-08-20 | 5 | 46.349 | 4 |
| 2026-08-21 | 2 | 39.836,5 | 1 |
| 2026-08-22 | 18 | 34.318,5 | 7 |
| 2026-08-23 | 19 | 34.583 | 5 |
| 2026-08-24 | 12 | 46.070 | 8 |
**Tabela B — grupo `depois` linha a linha + 5 `antes` imediatamente anteriores ao corte** (todas `version` 2.1.220):
| marca | ts_inicio | usage_1 | input | criação | leitura | preâmbulo |
|---|---|---|---|---|---|---|
| antes | 08-23 22:07:43 | 34.607 | 2 | 16.521 | 18.084 | 11.684 |
| antes | 08-23 23:01:43 | 34.605 | 2 | 16.519 | 18.084 | 11.684 |
| antes | 08-24 00:09:49 | 34.629 | 2 | 16.543 | 18.084 | 11.684 |
| antes | 08-24 01:20:21 | 45.978 | 2 | 19.281 | 26.695 | 11.652 |
| antes | 08-24 06:50:09 | 0 *(usage zerado)* | 0 | 0 | 0 | 11.263 |
| depois | 08-24 07:18:55 | 46.071 | 2 | 19.374 | 26.695 | 11.683 |
| depois | 08-24 07:34:42 | 46.069 | 2 | 19.372 | 26.695 | 11.683 |
| depois | 08-24 12:31:31 | 46.078 | 2 | 19.381 | 26.695 | 11.684 |
| depois | 08-24 13:15:33 | 34.644 | 2 | 16.558 | 18.084 | 11.683 |
| depois | 08-24 13:37:08 | 34.644 | 2 | 16.558 | 18.084 | 11.684 |
| depois | 08-24 13:44:08 | 46.401 | 2 | 19.704 | 26.695 | 11.684 |
| depois | 08-24 14:35:56 | 46.416 | 2 | 19.719 | 26.695 | 11.684 |
| depois | 08-24 14:59:39 | 46.415 | 2 | 19.718 | 26.695 | 11.684 |
| depois | 08-24 16:41:06 | 46.415 | 2 | 19.718 | 26.695 | 11.684 |
Janelas ≥ 40.000 tok no grupo `antes`: **45 de 233**; ts da mais recente: `2026-08-24T01:20:21.050Z`. Tabela C (papel de subagente, n_total ≥ 10) e Tabela D (projeto) a seguir:
| papel | n_antes | mediana_antes | n_depois | mediana_depois | Δ mediana |
|---|---|---|---|---|---|
| context-scout | 18 | 9.176 | 0 | — | — |
| pantonic-benchmarker | 16 | 10.351,5 | 0 | — | — |
| pantonic-executor | 228 | 35.088 | 4 | 36.271 | +1.183 |
| pantonic-planner | 15 | 13.980 | 3 | 13.620 | −360 |
| pantonic-scout | 10 | 8.339,5 | 0 | — | — |
**Tabela D — por projeto** (`antes` = 14 dias antes do corte, `depois` = desde o corte):
| projeto | n_antes | mediana_antes | n_depois | mediana_depois |
|---|---|---|---|---|
| d--workspaces-PantonicApp | 110 | 34.872 | 9 | 46.078 |
| d--workspaces-PantonicMonitor | 0 | — | 0 | — |
| d--workspaces-PantonicScanlator-pocOcr-ocrManga | 0 | — | 0 | — |
| d--workspaces-PantonicVideo | 31 | 38.619 | 0 | — |
| d--workspaces-PantonicVideo-POCs-desidratar-subtitle | 0 | — | 0 | — |
**Veredito:**
- eixo tempo: **sem degrau (oscilação pré-existente)** — 08-20 já tinha mediana 46.349 (acima da de 08-24) e 45/233 janelas `antes` já cruzavam 40.000; o grupo `depois` também mistura valores baixos (34.644 ×2) com altos.
- eixo janela: **só na principal** — `pantonic-executor` (n_depois=4) sobe +1.183 (+3,4%) e `pantonic-planner` (n_depois=3) cai −360; nenhum dos dois acompanha o salto de ~+11.700 tok (+34%) da principal.
- eixo projeto: **controle externo ausente** — todo projeto ≠ `d--workspaces-PantonicApp` fecha `depois` com n=0.

Janela temporal do degrau: 2026-08-24T06:50:09.164Z → 2026-08-24T07:18:55.063Z
