# Viabilidade — agente de leitura em standby por plano

Análise de viabilidade, **anterior a qualquer plano**, da figura proposta em 2026-09-19: um agente
Haiku instanciado uma vez por plano, mantido em standby, que executa todo Read/Grep/Glob dos demais
papéis e devolve relatórios padronizados, com hooks automatizando o que couber. Duas perguntas a
responder: **quanto se economiza por plano** e **se a qualidade dos demais agentes sobe**.

Método: medida, não estimativa. Sonda descartável (`%TEMP%\claude\sonda_leituras.py`, stdlib) sobre
os **90 transcripts de subagente** mais recentes e as **12 sessões principais** mais recentes de
`~/.claude/projects/d--workspaces-PantonicApp/`. Custo em dólar pela tabela da skill `claude-api`
(Haiku 1 / Sonnet 2 / Opus 5 $/M de entrada; cache read 10%; cache write 125%; saída 5× a entrada).
Leitura = resultado de `Read`, `Grep`, `Glob` e `Bash` de leitura (`cat`, `sed -n`, `grep`, `git
log`…); o custo atribuído a uma leitura inclui a ingestão e a releitura em cache em todos os turnos
seguintes do mesmo contexto. Medido em 2026-09-19, HEAD `eb93490`.

> **Errata (2026-09-19, 3ª rodada).** As seções 1, 3 e 6 somaram `usage` por **linha** do
> transcript; o harness grava uma linha por bloco de conteúdo, cada uma com `usage` próprio (341
> linhas para 188 mensagens no consultor medido). Os **percentuais** se sustentam (numerador e
> denominador inflaram juntos); os **valores absolutos em dólar** estão ~1,6–1,8× altos. Valores
> corrigidos, deduplicados por `message.id` (mediana por tarefa): executor Sonnet **$0,60** (não
> $1,16), executor Opus **$1,64**, reviewer **$1,51**, planner **$4,22**, consultor **$17–52** por
> instância, sessão principal **$7–39**. Plano de referência ≈ **$500**, não $700. As economias
> das variantes A/C escalam na mesma proporção (A ≈ $5–7, C ≈ $3–5); os vereditos não mudam. A
> seção 7 já usa os valores corrigidos.

## 1. O que o dado diz — a fatia de leitura é pequena

Custo por tarefa (mediana), decomposto em quatro fatias:

| papel / modelo | n | turnos | ctx final | prefixo de entrada | custo/tarefa | **leituras** | leituras de alvo editado | saída própria (paga + relida) | prefixo relido |
|---|---|---|---|---|---|---|---|---|---|
| executor / Sonnet | 14 | 38 | 83k | 37k | $1,16 | **$0,10 (9%)** · 10k tk · 12 chamadas | $0,05 | $0,31 (25%) | $0,36 (32%) |
| executor / Opus | 4 | 35 | 93k | 31k | $3,03 | **$0,27 (8%)** · 13k tk | — | $0,78 (25%) | $0,73 (28%) |
| reviewer / Opus | 13 | 42 | 80k | 18k | $2,72 | **$0,43 (14%)** · 16k tk | — | $0,76 (28%) | $0,49 (17%) |
| planner / Opus | 3 | 65 | 101k | 28k | $4,60 | **$0,58 (12%)** · 18k tk | — | $1,14 (25%) | $1,02 (22%) |
| consultor / Opus (standby) | 4 | 253 | 352k | 17k | $52,56 | **$3,35 (8%)** · 36k tk | — | $18,12 (34%) | $2,16 (4%) |
| sessão principal / Opus | 9 | 69–481 | 147–470k | — | $9–92 | **0–9%** · 0–29k tk | — | 45–86% | 17–25% |

Três leituras do quadro:

1. **Leitura é a terceira fatia, não a primeira.** Em todo papel, o próprio output do modelo
   (25–34%) e o prefixo fixo de entrada (17–32% nos subagentes) custam mais do que tudo que o agente
   lê. O executor Sonnet entra com **37k tokens** de prefixo antes do primeiro turno — 3,7× o que
   ele lê na tarefa inteira; o reviewer entra com 18k. A causa dessa diferença não foi medida aqui.
2. **A ocupação está longe da faixa de decaimento.** Executor e reviewer fecham em 80–93k de uma
   janela de 1M (8–9%). A diretriz de 50% (`GOVERNANCA.md` §3) não está em jogo para eles; está
   em jogo para o consultor (352k) e para a sessão principal (até 470k), cujas leituras são 0–9%.
3. **Metade da leitura do executor Sonnet é de arquivo que ele mesmo edita** ($0,05 de $0,10). O
   harness exige `Read` antes de `Edit`, e a doutrina do kit já fixa que "quem edita precisa ler o
   original, sem intermediário" (`context-prep`). Essa metade **nenhum leitor intermediário
   remove**.

Arquivos que concentram a leitura nos 90 transcripts (1.429k tokens em 1.189 chamadas): a
`RUBRICA_DE_REVISAO.md` (188k tk, 43 leituras, **39 integrais** de 4,4k cada — todo reviewer a lê
inteira), o plano `P-0740` (172k, 91 chamadas, 77 por faixa), `P-0739` (66k), o diário (59k) e
`backlog.py` (50k — o instrumento sendo editado e testado). É **conjunto de trabalho**, não
exploração: card, instrumento-alvo, teste do instrumento, rubrica. O regime de "varredura ampla"
que o `pantonic-scout` existe para absorver quase não aparece na série.

## 2. Três restrições estruturais da figura proposta

**R1 — Alcance: subagente não instancia nem endereça outro agente.** Executor, reviewer, consultor
e planner rodam como subagentes; só o contexto principal (o `scrum-master`) pode dar `Agent` ou
`SendMessage`. O kit já registra o fato (`pantonic-planner.md` §"Se este contexto pode instanciar o
scout… se não pode (você foi invocado como subagente)"). Um leitor em standby seria alcançável
**apenas** pelo orquestrador — e as leituras do orquestrador são 0–9% de janelas cujo custo é
dominado pelo próprio output. Os papéis que mais leem em proporção (reviewer 14%, planner 12%) não
o alcançam.

**R2 — Janela: Haiku 4.5 tem 200k, e standby acumula.** Um contexto de agente é append-only; cada
`SendMessage` ao mesmo agente reenvia tudo. A série do consultor mostra a curva: 258k → 451k em 11
acionamentos. Um leitor que ingere os **1,4M tokens brutos** de leitura de um plano (ou os ~165k só
do orquestrador em ~11 janelas) estoura 200k antes de o plano chegar à metade. A figura "uma
instância por plano" é inviável para ingestão bruta; só sobreviveria guardando **índice**, não
conteúdo — e índice se gera por script, a custo zero.

**R3 — Hooks: podem mudar a entrada de um Read, não a saída.** Confirmado na referência de hooks:
`PreToolUse` aceita `updatedInput` para qualquer ferramenta (inclusive `Read`/`Grep`); `PostToolUse`
**não** substitui o resultado que o modelo vê; hooks de projeto **rodam dentro de subagentes**;
`SubagentStart` injeta contexto ao nascer. Logo a automação possível é: (a) reescrever um Read
conhecido para um digest pré-gerado; (b) injetar um relatório padronizado no nascimento do
subagente. Nenhuma das duas precisa de um LLM leitor.

## 3. Estimativa de economia por plano

Base: plano com a forma do `P-0740` (35 tarefas; 36 despachos Sonnet, 10 Opus, 35 revisões, ~7
rodadas de planejador, 4 instâncias de consultor, ~11 janelas principais). Custo total do plano na
ordem de **$700**; tokens brutos lidos por modelos caros na ordem de **1,5M**.

| variante | alcança | tokens que deixam de entrar em Sonnet/Opus | $ por plano | % do plano |
|---|---|---|---|---|
| **A — leitor Haiku em standby por plano** (a figura pedida) | só o orquestrador (R1); janela estoura (R2) | ~115–210k (leituras do orquestrador × ~0,7 de compressão) | **$8–12** | **1–2%** |
| **B — leitor Haiku efêmero por pergunta** (= `pantonic-scout` já existente, não usado nesta série) | orquestrador e planner inline | idem A, sem R2; spawn frio custa ~5–10k tk por pergunta | $8–12 | 1–2% |
| **C — leitor mecânico**: script gera relatório padronizado (card + âncoras + mapa de símbolos + faixas relevantes) no despacho; `SubagentStart` injeta; `PreToolUse` reescreve Reads conhecidos para digests | **todos os papéis** (hooks rodam em subagentes) | ~600–900k | **$20–30** | **3–4%** |
| teto teórico (toda leitura a custo zero, exceto alvo editado) | — | ~1,4M | ~$55 | ~8% |

Contas da variante A: leitura do orquestrador custa $0,3–4,7 por janela; Haiku a 1/5 do Opus mais o
dossiê (~30% do bruto) reentrando no contexto caro → poupa ~50% dessa fatia. Da variante C: fatia de
leitura medida por grupo ($2,6 executor Sonnet, $1,1 executor Opus, $5,7 reviewer, $1,9 planner,
$14,2 consultor, ~$15 orquestrador), menos a metade irremovível do executor, com captura realista de
40–60%.

Para comparação, no mesmo plano: o **prefixo de entrada** dos subagentes custa ~$45 (36×0,36 +
10×0,73 + 35×0,49 + 7×1,02) — mais que toda a leitura removível —, e a **rubrica lida integral 35
vezes** custa sozinha ~$5 por plano.

## 4. Efeito sobre a qualidade dos demais agentes

- **Executor: neutro a negativo.** Ganho por higiene de contexto não existe a 8% de ocupação. O
  risco é o oposto: o kit já registrou que "dossiê de scout pode estar confiante e errado, não só
  incompleto" (`context-prep`, aceitação), e a falha típica de intermediário é âncora/linha errada,
  que vira `Edit` por mismatch e turno de correção (`pantonic-executor.md`, higiene de edição). O
  executor lê seu conjunto de trabalho, não explora; não há exploração a delegar.
- **Reviewer: neutro.** Suas leituras são rubrica, evidência e diff — matéria de juízo que não se
  resume sem perder o que o laudo precisa. O ganho de padronização já existe no
  `review_evidence.py`; o que falta é mecânico (rubrica como digest ou ponteiro), não um leitor.
- **Consultor e orquestrador: onde a higiene importaria (352k–470k), a leitura é 0–9%.** O peso é
  o próprio output e a saída de instrumentos; leitor não atua nisso.
- **Causa real das rodadas caras (série `ESC-27..36`, `consultant-spec.md` §9):** decisão ausente
  no card, contradição norma × instrumento, gramática não aprendida pelo parser. Nenhuma tem leitura
  como causa. Relatório padronizado **melhora consistência** onde o relatório é mecânico e
  determinístico (variante C); um LLM barato no meio adiciona uma fonte de erro sem remover
  nenhuma.

## 5. Veredito para decisão

- **Variante A (a figura pedida): não viável** como especificada — R1 tira dela os papéis que
  leem, R2 tira dela o standby, e o teto é 1–2% do plano.
- **Variante C (leitor mecânico + hooks): viável, pequena** — 3–4% do plano, sem risco de
  intermediário, alcança subagentes, e é a única que entrega "relatório padronizado com estrutura
  de dados definida" de fato. Cabe num plano curto (script `dossie.py` + hook `SubagentStart` +
  reescrita de Reads conhecidos + rubrica condensada).
- **Variante B já existe** (`pantonic-scout`, Haiku, 0 usos na série do `P-0740`): não precisa de
  plano, precisa de gatilho de uso no planner/orquestrador para perguntas abertas.
- **O dado aponta duas alavancas maiores que qualquer leitor**, fora do escopo pedido e registradas
  como insumo: o prefixo de entrada dos subagentes (37k no executor Sonnet, 2× o do reviewer —
  causa não medida) e o custo do output relido nos contextos longos (consultor 34%, sessão
  principal 45–86%).

Nada aqui é plano nem decisão; é insumo. O passo seguinte, se houver, é a escolha do dono entre
C, B, nenhuma — ou uma investigação do prefixo de entrada.

## 6. Variante C especificada — e o veredito "ganho sem drawbacks" (2026-09-19, 2ª rodada)

Decisão do dono na 1ª rodada: **A é inviável — aceito.** Pergunta da 2ª rodada: C é ganho sem
drawbacks? Resposta curta: **não.** C é viável tecnicamente, rende ~1% do plano e carrega três
drawbacks que este repositório já mediu na própria história. O que sobra sem drawback são duas
correções editoriais, não um leitor.

### 6.1 Duas medidas novas que mudam a conta

**O despacho não carrega o card.** O prompt que o executor recebe mede **0,8k tokens** (mediana,
n=15); um card do `P-0740` tem ~7,3k chars (~1,8k tokens). O Passo 4 do `scrum-master` prescreve
"dossiê da tarefa copiado do plano", mas a prática medida é ponteiro + instrução de retorno. Por isso
o executor lê o próprio card no plano — 2,4k tokens por tarefa Sonnet, 11,8k por tarefa Opus.

**Partição da leitura por categoria** ($ por tarefa, custo atribuído com releitura):

| papel | leitura total | plano | diário | doutrina/docs | rubrica | código/instrumento | testes |
|---|---|---|---|---|---|---|---|
| executor / Sonnet (n=15) | $0,20 | 0,07 | 0,04 | 0,01 | 0,00 | 0,05 | 0,02 |
| executor / Opus (n=4) | $0,27 | 0,24 | — | 0,00 | 0,02 | — | — |
| reviewer / Opus (n=13) | $0,44 | 0,11 | 0,00 | 0,11 | **0,16** | 0,03 | 0,00 |
| planner / Opus (n=3) | $0,64 | 0,48 | 0,04 | 0,06 | 0,05 | — | — |
| consultor / Opus (n=4) | $3,64 | 2,07 | 0,86 | 0,09 | 0,13 | 0,18 | — |

Arquivos: o executor lê o **diário 54 vezes em 15 tarefas** (61k tk — "localize sua tarefa pelo
índice" num doc de 2,5k linhas) e o plano 43 vezes; o reviewer lê a **rubrica integral em 13 de 13
revisões** (6k tk cada, 363 linhas). Planner e consultor leem o plano porque **editam** o plano — não
é leitura substituível por relatório.

### 6.2 Os componentes de C, um a um

| # | componente | mecanismo | o que substitui (medido) | custo próprio | drawback | saldo / plano |
|---|---|---|---|---|---|---|
| C1 | **relatório de despacho por instrumento** (`dossie.py`): card integral, linha do índice do diário, âncoras `arquivo:linha:texto`, mapa `def/class` dos alvos, range do bullet anterior | colado no prompt pelo `scrum-master` **ou** injetado por `SubagentStart` (`systemMessage`), chaveado por `.claude/estado/tarefa-corrente.json` | executor: plano+diário $0,11/tarefa; reviewer: plano $0,11 | o relatório entra no prefixo (~2–3k tk) e é relido em todo turno — quase os mesmos tokens que as leituras traziam; o ganho é só o **overshoot** das leituras por faixa e a **repetição** (3,6 leituras de diário por tarefa) | **(i)** instrumento novo no kit: a classe que motivou 4 dos 10 acionamentos `ESC-27..36` (instrumento sem card, contradição norma×instrumento, cobertura) e mais um parser da gramática do card (`AE-5`/`AE-6`); **(ii)** se o relatório estiver incompleto e o executor for proibido de reler → `blocked` ou edição sobre âncora velha; se for permitido reler → o ganho some (medido: 91 leituras do plano em 90 transcripts apesar da doutrina de despacho); **(iii)** injeção por `SubagentStart` chaveada em arquivo de estado: `tarefa-corrente.json` velho injeta o card errado num redespacho (`A6`) | **$4–5** (40–60% de $0,11 × 36 + $0,05 × 35) |
| C2 | **reescrita de Read por `PreToolUse`** (`updatedInput`) para digest de doc conhecido (rubrica, `GOVERNANCA` §7) | hook global, roda em subagentes | reviewer: rubrica $0,16/tarefa | zero | **substituição silenciosa**: o reviewer pede a rubrica e recebe um digest; critério perdido muda veredito, e o laudo declara "contra a rubrica" — falsifica a trilha de evidência. **Rejeitar.** O mesmo ganho vem de condensar o doc (edição, sem instrumento) | 0 (rejeitado) |
| C3 | **mapa de símbolos / índice de código por instrumento** (DOC_MAP para código) | gerado no despacho | greps exploratórios | pequeno | nenhum relevante — mas o alvo é ~0: o executor lê o instrumento que edita (`backlog.py`, 26 leituras/46k) e o teste dele; exploração não aparece na série | ≈ 0 |
| C4 | **hook que nega releitura** da mesma faixa (enforcement de "sem re-leitura de verificação") | `PreToolUse` deny | releituras | zero | a doutrina do executor **autoriza** re-Read após `Edit` por mismatch; o deny vira `blocked motivo=ferramenta` e rota `A3c` — mais turnos, não menos | negativo |

**Saldo de C inteira: ~$5–8 por plano (≈1%)**, com os drawbacks (i)–(iii) reais. Não é "ganho sem
drawbacks".

### 6.3 O que sobra sem drawback — e é ticket, não plano

- **Despacho que carrega o card e a linha do índice do diário**, como o Passo 4 já prescreve — sem
  instrumento novo, é o `scrum-master` cumprir a própria skill. Ganho ~$2–3/plano; único custo é
  prefixo do executor +1,8k tk. Zero risco novo.
- **Condensação editorial da rubrica** (363 linhas, lida integral 35× por plano): ~$3/plano se
  couber pela metade. É decisão de doutrina (o reviewer julga contra ela), não mecânica — só se o
  dono aceitar que a forma condensada é a rubrica.

### 6.4 Onde o dinheiro está — para não perder de vista

No plano de referência, consultor (~33%) e sessões principais (~45%) dominam, e o custo deles é
**Σ turnos × contexto**: 250–480 turnos relendo 200–470k. A alavanca é **número de turnos** (Regra 7)
e tamanho do output relido, não leitura. Fora isso, um lead barato de sondar: o executor Sonnet
entra com 37k de prefixo contra 18k do reviewer; o executor é o único papel com `tools: *` (schemas
de todas as ferramentas, MCP incluso) — 1 despacho de sonda com lista de ferramentas restrita mede
a hipótese pelo `usage_1`.

## 7. Consultor e releitura de contexto — anatomia e alavancas (2026-09-19, 3ª rodada)

Pergunta do dono: como reduzir o consumo do consultor e das releituras de contexto. Medida
deduplicada sobre 5 instâncias de consultor com `usage` e 12 sessões principais.

### 7.1 Dois fatos que decidem a questão

**F1 — O cache de subagente expira em 5 minutos; o da sessão principal, em 1 hora.** No consultor,
todo pico de `cache_creation` acima de 30k tokens ocorre após pausa ≥ 5 min (gaps medidos: 5, 6, 7,
7, 8, 8, 8, 10, 11, 12, 13, 15, 16, 17, 18, 20, 21, 23, 35, 55 min); o maior gap **sem** pico é 4,3
min. Nas sessões principais, gaps de 11–27 min passam sem pico, e os únicos picos vêm após 90–100
min. Consequência: **cada acionamento do consultor reescreve o contexto inteiro a preço cheio**
($6,25/M no Opus), porque executor e reviewer levam 10–20 min entre um acionamento e outro.

| instância | turnos | ctx final | duração | custo | reescrita de cache (TTL) | releitura de cache | output | acionamentos | $/acionamento |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 171 | 405k | 151 min | $39,5 | **$15,4 (39%)** | $17,9 | $6,2 (247k tk) | 9 | $4,4 |
| 2 | 188 | 452k | 252 min | $52,2 | **$25,3 (48%)** | $19,2 | $7,7 (307k) | 14 | $3,7 |
| 3 | 124 | 320k | 114 min | $22,6 | $7,3 (32%) | $10,7 | $4,6 | 5 | $4,5 |
| 4 | 114 | 280k | 115 min | $17,3 | $4,4 (25%) | $8,6 | $4,3 | 4 | $4,3 |
| 5 (morta por limite) | 233 | — | 209 min | sem `usage` | 3,5M tk reescritos (~$22) | — | 268k tk | 15 | — |

**F2 — O orquestrador gasta 7–13 turnos por despacho, a $0,10–0,23 o turno.** Custo por turno é
`contexto × $0,50/M` (Opus, cache read); a 300k, $0,15. Com 2–3 despachos por tarefa (executor,
reviewer, eventualmente consultor), a orquestração custa **$2–6 por tarefa**, mais que executor +
reviewer juntos ($0,60 + $1,51). Nas 7 sessões principais que rodaram o loop, todas em **Opus**
(doutrina: Sonnet), o custo somou $139,7, 60–77% em releitura de cache. Chamadas por turno: 1,04–1,26
— não há batching.

Composição do plano de referência (corrigida): sessões principais ~40%, consultor ~35%, executor +
reviewer ~18%, planner ~6%.

### 7.2 Alavancas, quantificadas, com o que custam

| # | alavanca | mecanismo | economia estimada / plano | drawback |
|---|---|---|---|---|
| L1 | **Loop do orquestrador em Sonnet**, como a doutrina já manda (`GOVERNANCA.md` §3) | disciplina + o hook de nudge que já existe; nenhum build | **~$80** (7 sessões de loop: $140 → ~$56; Sonnet custa 2,5× menos por token relido e por token de saída) | nenhum estrutural: o roteamento do loop é "sem discricionariedade" por doutrina; o Opus fica para planejar e revisar. Requer que a sessão de planejamento (Opus) **não** vire a sessão do loop |
| L2 | **Janela curta**: fechar a janela principal a ~100–150k, não a 450k | `PANTONIC_JANELA_TOKENS` de volta a ~200k (o hook "descalibrado" fechava janelas mais baratas) + a passagem de bastão que já existe | **~$60–100** (custo de releitura ∝ contexto médio; uma janela de 226 turnos a 450k custa $30 de releitura; três de 75 turnos a ~150k custam ~$10 + 2 pickups de ~$0,5) | mais pickups e handovers (pickup medido 19–60k tk); a diretriz de 50% é de qualidade, esta é de custo — as duas apontam para o mesmo lado |
| L3 | **Consultor efêmero com cenário persistido** (o handover da `consultant-spec` §8 como modo normal, não de fim de vida): a cada acionamento nasce um consultor, lê `docs/plans/<plano>-CENARIO.md` (≤ 15k tk: decisões vivas, fila, achados abertos, inconclusivos), decide, **atualiza o cenário**, encerra | agente + arquivo; sem hook | **~$90–120** (acionamento a ~$1,2–1,5 em vez de $3,7–4,5: prefixo 17k + cenário 15k + leituras dirigidas 20k reescritos = $0,3; ~15 turnos a ~70k = $0,5; saída $0,4). Elimina a morte por limite (instância 5) e a curva 258k→451k | o cenário é resumo, e resumo perde; a continuidade "no contexto" que a figura vendia **já é paga a preço cheio a cada acionamento** (F1), então o que se perde é o que o consultor não escreveu no cenário. Exige que o consultor **não leia o plano** (178k tk hoje) e sim o cenário + o card. Piloto de uma janela mede a diferença em reprovações |
| L4 | **Manter o consultor aquecido** (ping a cada ≤ 4 min via `SendMessage` enquanto executor/reviewer rodam) | orquestrador com agente em background + wakeup | ~$50 (ping = releitura de 300k = $0,15; 3 pings por gap de 15 min = $0,45 contra $1,9 de reescrita) | frágil: depende de o orquestrador estar acordado durante o despacho; cada ping é turno e conteúdo no contexto do consultor; não resolve a curva de crescimento nem a morte por limite. **Só se L3 for recusada** |
| L5 | **Menos turnos por despacho no orquestrador**: um instrumento `passagem.py` que encadeia `card_check → materializar → estado → (retorno) → review_evidence → rdo → telemetria` em 1–2 chamadas em vez de 6–8 | consolidação de instrumentos existentes, sem parser novo | **~$40–60** (7–13 turnos/despacho → 3–5; custo ∝ turnos) | instrumento consolidado é superfície nova de defeito (classe `ESC-27..33`), ainda que não crie gramática. Multiplica com L1/L2 |
| L6 | **Output do consultor**: `Edit` mínimo em vez de `Write` de seção inteira (16–65k tk de payload de `Write` por instância); resposta curta como a definição já manda | prompt/definição do agente | ~$10–15 (output é 12–16% do consultor) | nenhum |
| L7 | **Critério de entrada do acionamento** (aberto na `consultant-spec` §10): `dependencia` resolve no loop sem consultor; `escalar` sem bloqueante vira achado, não acionamento | regra no roteamento `B1` | não medido — 4 dos 10 acionamentos medidos foram no mesmo arquivo periférico | risco de o executor ficar sem desbloqueio quando precisava; exige a estatística de acionamento estruturada (§9) para calibrar |
| L8 | **Tirar o loop do LLM**: driver Python que roda o loop (`claude -p --agent pantonic-executor` / `pantonic-reviewer`), roteia pelo veredito calculado e só invoca LLM no escalonamento (consultor L3) | build médio; muda a rota do framework — **decisão do dono, não do executor** (Regra 8) | **~$180** (sessões principais → ~$5–10/plano); com L3, o plano cai de ~$500 para ~$200 | perde o dono interrompendo o loop "sem derrubar a sessão" (ganha Ctrl-C); hooks `SubagentStop` não disparam por `claude -p` — telemetria passa a vir do `--output-format json`, mais simples; a doutrina do `scrum-master` já é um algoritmo (roteamento fechado, sem improviso, `G-NOASK`), o que é o pré-requisito para isso funcionar. É a resposta de fundo ao "40% do plano é um LLM relendo contexto para rotear" |

### 7.3 Leitura de conjunto

Três alavancas não exigem build e somam ~$150–200 de um plano de ~$500: **L1** (Sonnet no loop),
**L2** (janela curta) e **L6** (output do consultor). **L3** é a correção estrutural do consultor:
o standby não entrega continuidade barata — sob TTL de 5 min ele reescreve tudo a cada chamada, e
a figura efêmera com cenário persistido custa um terço e não morre por limite; pede um piloto
medido, como o `P-0740` fez com o loop. **L8** é a única que ataca a causa (o loop é mecânico e
roda num LLM caro) e é decisão de rota do dono.

### 7.4 Posição para decisão (2026-09-19, 4ª rodada)

| item | posição | por quê |
|---|---|---|
| A — leitor Haiku em standby | **não viável** | alcance (R1), janela (R2), teto 1–2% |
| C — leitor mecânico + hooks | viável, **não recomendável** | ~1% com três drawbacks medidos |
| tíquetes: despacho com card + índice; rubrica condensada | viável, **recomendável como tíquete** | ganho marginal, custo zero, sem drawback |
| L1 — loop em Sonnet | viável, **recomendável — agora** | ~$80/plano; é cumprir a doutrina |
| L2 — janela curta (~100–150k) | viável, **recomendável — agora** | ~$60–100/plano; custo ∝ contexto médio |
| L6 — output do consultor (Edit mínimo, resposta curta) | viável, **recomendável — agora** | ~$10–15/plano, sem drawback |
| L3 — consultor efêmero com cenário persistido | viável, **recomendável como piloto medido** (uma janela) | ~$90–120/plano; resumo pode perder; mede-se em reprovações antes de virar doutrina |
| L5 — instrumento encadeado do despacho | viável, **adiar** | absorvido por L8; sozinho é superfície nova por ~$40–60 |
| L4 — ping para manter cache | viável, **não recomendável** | superado por L3 |
| L7 — critério de entrada do acionamento | **não decidível ainda** | falta a estatística estruturada (`consultant-spec` §9–10) |
| L8 — loop fora do LLM (driver + `claude -p`) | viável, **recomendável como decisão de rota**, depois de L1/L2/L3 medidas | ~$180/plano; ataca a causa; muda a rota do framework |

**Sequência recomendada:** onda 1 sem plano (L1, L2, L6, dois tíquetes) → uma janela medida →
onda 2, plano curto (piloto L3) → onda 3, decisão de rota (L8, que absorve L5). Esperado ao fim:
plano de ~$500 para ~$150–200.

**Destinos dados pelo dono em 2026-09-19:** tudo do consultor (L3, L4, L6, L7 e a medida F1) →
`docs/consultant-spec.md` §11, insumo do plano próprio da figura; o que não depende dos planos em
andamento → tíquetes `TK-56` (L1), `TK-57` (L2), `TK-58` (despacho com card), `TK-59` (rubrica
condensada), `TK-60` (sonda do prefixo) no diário, `ready`; o que depende do `P-0739` → plano
`docs/plans/P-0742-loop-fora-do-llm.md` (L8, absorve L5), `blocked` até o `P-0739` fechar.

A hipótese "reduzir leituras" (seções 1–6) fica onde estava: ≈1–4%. As leituras não eram o custo;
o **contexto relido por turno** era — e as alavancas acima agem sobre ele por três vias distintas:
preço do token relido (L1), tamanho do contexto (L2, L3) e número de turnos (L5, L8).
