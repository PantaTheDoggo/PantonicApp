# P-0738 — Contexto esgotado na partida: o custo fixo que se repaga a cada janela

**Data:** 2026-08-22 · **Origem:** diretiva do dono, **prioridade zero** (2026-08-22), linha
`P-0738-contexto-esgotado` de `docs/plans/_INBOX.md` · **Status:** `done` · **Prefixo das tarefas:**
`CTX-T<n>` · **Prefixo das decisões:** `DX-<n>` · **Paralisa:** `P-0737-loop-autonomo` (`blocked` em
3/12; nenhuma tarefa sai dele até este fechar) · **Checagem de versão do kit:** modo hub —
**congelada em `0.0.0`** (`DE-7`), comparação local × remoto suspensa, **nada a comparar** · **Sem
bump e sem tag.**

## 0. O problema, verbatim

> "contextos iniciam já esgotados; custos fixos recorrentes são repagos em cada tarefa, gerando
> desperdício massivo" (dono, 2026-08-22)

**Evidência medida que originou a decisão.** A `AUT-T5b` — uma tarefa atômica cujo trabalho real
coube num único subagente em background — consumiu **três janelas de orquestração**:

| janela | o que pagou | o que entregou |
|---|---|---|
| A | pickup completo | cruzou o teto **no gate de delegação, sem delegar** |
| B | pickup completo | delegou e cruzou o teto **antes do retorno**; o ato de fechamento ficou órfão |
| C | pickup completo | verificou entrega já pronta, escreveu 2 edits e **deixou a telemetria pendente** |

Cada uma repagou o pickup que a `CPK-T2` mediu em **77.457 chars (~19.364 tokens)**, dos quais
**33.932 chars (43,8%)** são custo fixo de entrada, antes de tocar qualquer fonte do projeto.

**Diagnóstico preliminar do dono — enunciado, não ratificado** (a `CTX-T4` o confronta com número):
**(i)** o gate de delegação orça o teto do **executor** e não o **saldo restante do orquestrador**,
de modo que delegar com janela curta garante uma janela fria pagando pickup inteiro por um
fechamento que vale ~5 tool uses; **(ii)** o custo fixo de entrada não amortiza entre tarefas — todo
contexto novo reconstrói do zero o mesmo estado; **(iii)** a verificação de entrega foi feita à mão,
no contexto mais caro, existindo instrumento (`.claude/tools/review_evidence.py`) e papel
(`.claude/agents/pantonic-reviewer.md`) construídos para isso.

**Marcador de revisão (2026-08-22, `DX-13`):** a metade **normativa** do diagnóstico `(i)` — *orçar o
teto do executor* — deixou de ser matéria de veredito: o dono decidiu que orçar é do **planejador**.
O texto acima fica como está (registro); o que a `CTX-T4` ainda confronta com número é a metade
**medível** de `(i)`.

## 1. O que já está medido e não se remede

Insumo direto: `docs/plans/P-0736-custo-do-pickup.md` (fechado como **lições aprendidas**) e o
relatório `docs/CUSTO_DO_PICKUP.md` `## 1`..`## 6`. O que de lá vale como dado de entrada:

- **Pickup típico = 77.457 chars (~19.364 tokens)**, decomposto em 10 passos obrigatórios (`## 3`).
- **Custo fixo de entrada = 33.932 chars (43,8%)** — `H4` confirmada.
- **Ranking por fonte ingerida** (`## 5`): `_INBOX.md` 21.505 (27,8%) · dossiê do plano corrente
  19.872 (25,7%) · `proximo-passo/SKILL.md` 15.081 (19,5%) · `global/CLAUDE.md` 9.546 (12,3%) ·
  memórias indexadas 8.488 (11,0%).
- **Alvo proposto e nunca ratificado** (`## 6`): 40.000 chars / 10.000 tokens, com redução exigida de
  37.457 chars (−48,4%).
- **Achado do próprio relatório:** *"o orçamento medido é piso, não teto"* — a soma por arquivo não
  explica uma janela que estoura em 100k tokens. É exatamente esse vão que este plano mede.

**Método herdado, não reinventado:** `DC-2` (definição operacional), `DC-3` (chars primário, tokens =
chars ÷ 4), `DC-4` (sonda programática descartável no scratchpad; nunca `Read` integral nem
`Grep -output_mode content` sobre artefato grande), `DC-7` (rotas como conjunto fechado), `DC-8`
(ranking por medida bruta), `DC-9` (round-trip único com o dono).

## 2. Decisões de planejamento (fechadas neste ato)

Zero bloco a preencher, zero ramo condicional, zero decisão owner-gated solta dentro de tarefa.
O bloco `## Questões ao dono` está no fim deste arquivo. **Rodada de 2026-08-22 (`DX-15`):** ele
deixa de estar vazio e passa a carregar **uma** questão — `Q1`, o que o campo `classe` carrega —,
**aberta pelo próprio dono** e endereçada a ele. O `G-PLANREADY` item 5 segue satisfeito pela sua
condição operacional: **nenhuma tarefa publicada depende do desfecho dela**, nenhuma consome
artefato que ainda não existe e nenhuma para no meio para perguntar. Enquanto `Q1` estiver aberta,
o campo `classe` **permanece no cabeçalho exatamente como está**, e é isso que mantém a
independência.

| Id | Decisão | Conteúdo e racional |
|---|---|---|
| **`DX-1`** | **Três estágios num arquivo só, com tarefa-charneira** — como o plano vai da medida à execução sem publicar vão | O mandato exige (a) investigação medida antes de rota **e** (b) execução dentro deste plano; o `G-PLANREADY` item 5 proíbe publicar bloco em aberto. Resolve-se pelo padrão da casa (a `V2C-T6` autorou o Estágio 3B inteiro já fechado): **Estágio A** — medida (`CTX-T2`, `CTX-T3`); **Estágio B** — causas raízes e round-trip único (`CTX-T4`); **charneira** — `CTX-T5`, rodada de replanejamento que **autora `CTX-T6..T9` já fechados neste mesmo arquivo**; **Estágio C** — execução; **fecho** — `CTX-T10` (aferição) e `CTX-T11` (README). A faixa `CTX-T6..T9` é **reservada e nomeada**, não vão: tem dono (`CTX-T5`), critério de fechamento e data. Nenhuma tarefa publicada hoje depende do conteúdo dela. **Dividir em dois planos está recusado:** custaria um pickup inteiro a mais (dossiê de 19.872 chars + reautoria) — o plano que existe para eliminar repagamento não pode se dividir e repagar |
| **`DX-2`** | **Nenhuma correção antes da medida** | Contrapartida da `DX-1`: entre a publicação e a `## 9` do relatório, a única mudança que este plano escreve é a `CTX-T1`, e ela é **transcrição de decisão do dono**, não derivação de causa. Obstáculo que pareça exigir correção vira linha em `## 9. Achados da execução`, nunca edição (Regra 8) |
| **`DX-3`** | **Residência da medida** | `docs/CUSTO_DO_PICKUP.md`, seções novas `## 7`..`## 10`, teto do arquivo elevado de 200 para **320 linhas**. O arquivo **não se renomeia**: `docs/DOC_MAP.md`, o `P-0736` e o diário apontam para ele, e trocar o nome é ganho cosmético pago em ponteiros quebrados. Duas medidas do mesmo fenômeno em dois arquivos divergem na primeira edição e forçam duas leituras dentro do próprio pickup — o defeito que se está medindo |
| **`DX-4`** | **Unidade da medida de janela** | Para **arquivo**, vale a `DC-3` (chars, tokens = chars ÷ 4). Para **janela**, a unidade primária é **token medido**, lido do transcript pelo mesmo parse que `.claude/tools/ocupacao.py:63` já usa — `input_tokens + cache_read_input_tokens + cache_creation_input_tokens` da entrada `assistant` com `message.usage`. Nenhum leitor novo se inventa e nenhuma estimativa substitui o medido |
| **`DX-5`** | **Definição operacional de "contexto que inicia esgotado"** | A ocupação do **primeiro** `usage` de `assistant` da janela: o que se paga **antes de qualquer ato**. É o número que este plano existe para reduzir, e é ele que a `CTX-T10` afere depois |
| **`DX-6`** | **Conjunto fechado de rotas** | Os cinco da `DC-7` — `condensar`, `ponteiro`, `gerar-por-instrumento`, `mover-ao-historico`, `manter` — mais dois que a matéria de janela exige: **`amortizar`** (o custo passa a ser pago uma vez e reusado entre tarefas/janelas) e **`delegar`** (o ato sai do contexto caro para papel barato já existente). Sete valores; a `CTX-T4` escolhe dentro do conjunto e nunca inventa vocabulário |
| **`DX-7`** | **Fronteira do que se remede** | Nada do que o `P-0736` mediu é remedido. A medida nova é de **janela** (ocupação real, atribuída por evento), não de **arquivo** (soma de chars). Onde a forense contradisser a soma por arquivo, manda a forense, e a divergência entra como linha de achado — não como refutação silenciosa (`G-PREMISE`) |
| **`DX-8`** | **Absorções — este é o "plano de contexto" que o `P-0737` §8 recomendou** | Absorve as recomendações **(b)** (otimização de contexto do `scrum-master`, com o `TK-23`) e **(c)** (otimização dos contextos dos agentes que ele instancia, com o `TK-32` e o desdobramento do item 4 da `T17`). **Não** absorve a recomendação (a), o piloto medido do loop, que segue reservada ao `P-0737`. As notas nas células `TK-23` e `TK-32` do índice foram **aplicadas no ato do planejamento** — não repetir, não conferir por reedição |
| **`DX-9`** | **Fronteira com o `P-0737`, que está `blocked`** | **A matéria de contexto é deste plano; a de responsabilidade e fluxo é do `P-0737`.** Este plano pode `condensar` e `amortizar` texto de artefato do kit **sem alterar responsabilidade, passo, gate, contador ou tabela de roteamento**. Se a `CTX-T5` concluir que a rota exige mexer em fluxo, ela **não autora o card**: registra em `## 9` e o encaminha como insumo obrigatório da `AUT-T6`/`AUT-T9`. Como o `P-0737` está paralisado, não há edição concorrente — só herança: quando destravar, a `AUT-T6` recebe o texto já enxuto |
| **`DX-10`** | **Superfície e versão** | Sem bump, sem tag (`DE-7`, congelada em `0.0.0`). Mudança em artefato **canônico** do kit escreve uma linha em `CHANGELOG.md` sob `## [Não lançado]` (`G-SURFACE`, guardrail 16). Nenhum derivado é tocado (`DA-3`) e `.claude/sync-kit.ps1` fica inalterado |
| **`DX-11`** | **Alvo default, para que nenhuma tarefa dependa de resposta** | O alvo do custo fixo por janela é o proposto no `P-0736` `## 6` — **40.000 chars / 10.000 tokens** — e **vale como escrito** se a `CTX-T4` não o trocar por ratificação do dono. A `CTX-T10` afere contra o valor vigente na `## 9`, qualquer que seja |
| **`DX-12`** | **Telemetria** | Toda tarefa fecha com uma linha em `docs/telemetria.tsv` pelo dado **medido** da notificação (`GOVERNANCA.md` §4.2), escrita pela orquestração. A linha `nao_medido` da `AUT-T5b` **não se retifica**: é registro histórico e é dado de entrada da `CTX-T3` |
| **`DX-13`** | **Adendo do dono: poluição e capacidade são duas regras, de naturezas diferentes** — decisão do dono de **2026-08-22**, posterior à autoria deste plano e **anterior** à execução da `CTX-T1`; **ratificada, não se reabre** | O enunciado único que a `CTX-T1` publicaria (*"só a capacidade da janela e a poluição do contexto interrompem o curso de uma tarefa"*) fundia duas regras que não têm a mesma natureza. Elas se separam: **(1) Poluição é regra final, vale 100% do tempo** — havendo poluição, é **obrigatório parar não graciosamente**, porque o que foi produzido depois do sinal já está comprometido: retornar ao orquestrador e **demandar contexto limpo para a reexecução**. Não há "termino o que está aberto e limpo depois", não há fechamento cerimonioso e **nada do produzido depois do sinal se aproveita**. **(2) Capacidade não é regra final e muda de natureza** — deixa de ser regra de execução e de guardrail e passa a ser **diretriz do planejador**: no planejamento, delimita o **escopo de cada tarefa**, que deve ser dimensionada para **(a)** caber num contexto **coerente e coeso**, **(b)** ser **autossuficiente em contexto para a execução** — sem exigir leitura ad hoc durante a execução — e **(c)** respeitar uma **estimativa de 50% de ocupação, com tolerância até 60%**. O número **não é arbitrário e não é constante mágica**: vem da literatura sobre **decaimento de desempenho de agentes em função do enchimento do contexto**, e **é revisável se a literatura indicar outro valor** — registra-se com proveniência e cláusula de revisão. Decorre: o **executor não se preocupa com teto nem com orçamento** — isso é responsabilidade **estrita do planejador** —, e a **única** responsabilidade do executor é **executar a tarefa**; **estouros** de teto, de orçamento e de contexto são **registrados no corpo da tarefa** e viram **insumo** para (i) revisão do plano e (ii) eventual **reexecução da tarefa**, havendo suspeita de degradação acentuada por enchimento de contexto; e **nunca** o **executor** ou o **`scrum-master`** revisa plano — havendo indício de que o plano deve ser revisto, o plano vai a **`blocked`** e a matéria é **obrigatoriamente escalada a um agente planejador**, que tem autonomia sobre revisão **técnica e tática**, enquanto revisão de cunho **estratégico ou que altere escopo** exige **mais uma escalada, ao dono**. **Fato medido que motivou o adendo:** a regra de capacidade vinha sendo usada para **interromper tarefas à força** e retomá-las em contexto novo para conclusões parciais, **pagando o custo fixo em dobro** — exatamente o defeito que este plano existe para eliminar (`## 0`: a `AUT-T5b` em três janelas, cada uma repagando 77.457 chars) |
| **`DX-14`** | **Residências do adendo, e o que ele arrasta de superfície** — derivação de planejamento da `DX-13` pela régua de `GOVERNANCA.md` §3.1 | **(1) Poluição — regra final de execução, com guardrail.** Régua §3.1 pergunta 1: vale para projeto **não-Pantonic** do dono e já mora lá — **canônica em `.claude/global/CLAUDE.md`, Regra 2**, com o texto operacional do framework em `GOVERNANCA.md` §4.3 (bullet *Coesão*) e o **guardrail** em §7 item 7, que passa a enunciar **só** a poluição. Precedente da casa: `G-PLANFIDELITY` (§7 item 9), promovido ao global com o item mantendo enforcement e ponteiro. **(2) Capacidade — diretriz de planejamento, sem guardrail.** Diretriz não mora onde guardrail mora: sai de §4.3 como condição de execução e passa a **`GOVERNANCA.md` §3**, no bloco de dimensionamento pré-delegação que já é o lar do orçamento por classe, sob subtítulo próprio, com os três critérios, o número (50%, tolerância a 60%), a **proveniência** e a **cláusula de revisão**; **projeta-se** em `.claude/agents/pantonic-planner.md` (§3.1 pergunta 4: papel de quem dimensiona). §4.3 fica com **uma linha de ponteiro** e com a regra de que **capacidade nunca interrompe tarefa em curso**. **(3) Encerramento planejado de janela de orquestração** permanece em §4.3 como ato da **orquestração entre tarefas** — nunca dentro de tarefa, nunca do executor —, e `.claude/tools/ocupacao.py` permanece **como está**, reclassificado de instrumento de condição de execução para **aviso informativo à orquestração** (`manter`, `DX-6`): mexer no `LIMIAR` ou no hook seria inventar número novo, que a própria `DX-13` proíbe. **(4) Escada de escalada** (executor e `scrum-master` não revisam plano) é matéria de responsabilidade: canônica em `GOVERNANCA.md` §3 (matriz + parágrafo da escada), projetada por **ponteiro** nos agentes e skills. **(5) O campo `[<modelo> · classe <classe> · teto <N>]` do cabeçalho de tarefa permanece, com o nome que tem**, e muda de destinatário: é a **declaração do dimensionamento feito pelo planejador**, lida por `.claude/tools/rdo.py` e pela série de `docs/telemetria.tsv`, **nunca instrução ao executor**. Renomear o campo quebraria `rdo.py`, seus testes e todo cabeçalho histórico, por ganho cosmético. **(6) Carve-out declarado à `DX-9` e à `DX-2`:** reconciliar superfície de artefato de fluxo com decisão do dono **posterior** ao `P-0737` **não é mexer no fluxo** — é **retirar de artefato de fluxo texto que a decisão do dono tornou falso**, por **deleção ou ponteiro**, sem criar passo, ramo, contador ou linha de roteamento; e essa reconciliação, como a `CTX-T1`, é **transcrição de decisão do dono**, não derivação de causa medida, e por isso corre antes da medida. Mudança que **acrescente** passo ou altere roteamento continua fora (`DX-9`): vira linha em `## 9. Achados`, insumo obrigatório da `AUT-T6`/`AUT-T9`. **(7) `G-SURFACE` (guardrail 16) é obrigatória no ato:** a varredura desta rodada achou 20 pontos de contato, distribuídos entre `CTX-T1` (doutrina canônica), `CTX-T1b` (papéis) e `CTX-T1c` (skills de fluxo e instrumentos) |
| **`DX-15`** | **O campo `teto` cai do cabeçalho de tarefa** — decisão do dono de **2026-08-22**, posterior à `DX-14` e anterior a qualquer execução deste plano; **ratificada, não se reabre**. **Revoga**, com esta data, a parte do **item 5 da `DX-14`** que mantinha o campo `teto` no cabeçalho "com o nome que tem, mudando de destinatário" — o texto da `DX-14` fica onde está, como registro do que se decidiu antes, e **não vale mais nesta parte**: o campo **não muda de destinatário, ele deixa de existir**. O que sobrevive do item 5: **`Modelo` permanece**, e agora com consumidor nomeado pelo dono — é por ele que o `scrum-master` **instancia o executor adequado**; **`classe` permanece como está** enquanto a `Q1` estiver aberta (`## Questões ao dono`) | **Racional, palavra do dono:** *"todas as tarefas respeitarão a regra de contexto, aplicável apenas ao planejador no dimensionamento de escopo. Como somente o planejador tem autoridade para revisar o escopo, uma informação de teto é poluição."* É o fecho lógico da `DX-13`: se teto é matéria exclusiva de quem dimensiona, publicá-lo no cabeçalho o entrega justamente a quem não tem autoridade sobre ele — o executor e o orquestrador —, e informação sem consumidor legítimo é volume, o defeito que este plano existe para atacar. **Confirmação medida (Grep, 2026-08-22):** o campo já era **redundante** — `.claude/tools/rdo.py:217` **recusa** qualquer `teto` diferente do default da classe (`_CLASSE_TETO_DEFAULT`), isto é, o número do cabeçalho nunca carregou informação que a `classe` já não carregasse. **Gramática nova, decidida aqui (tática, do planejamento):** `### <ID> — <título> [<modelo> · classe <classe>]`. **Retrocompatibilidade:** o segmento `· teto <N>` vira **opcional** na regex do `rdo.py` e, quando presente, é **descartado** — cabeçalho histórico continua parseável e **nenhum plano fechado se reescreve** (invariante 8). **Migração:** os cabeçalhos do **próprio `P-0738`** migram **no ato desta rodada** (nenhuma tarefa executada; publicar plano vivo na gramática revogada seria contradição); o **`P-0737`** está `blocked` e **não se toca** (`DX-9`, e o §7 daquele plano já congela os cabeçalhos) — quando destravar, quem replanejar reautora na gramática vigente; `P-0734`/`P-0735`/`P-0736` são registro fechado. **`--esquema-legado` do `rdo.py` fica**, com o sentido que sempre teve — cabeçalho **sem colchete algum** —, e perde o `--teto` (`--modelo`/`--classe` bastam). **Carve-out estendido à `DX-14` item 6:** reconciliar o **parser** com a gramática nova é **remoção de campo**, não fluxo novo — `rdo.py` não roteia, não decide e não ganha passo, ramo ou contador —, e por isso corre antes da medida, na **`CTX-T1d`**, tarefa nova desta rodada. **Consequência de `G-SURFACE` (guardrail 16):** os 20 pontos da `DX-14` item 7 **mudam de natureza** — deixam de ser "reendereçar o teto ao planejador" e passam a ser **deleção**; a varredura complementar desta rodada acrescentou a **gramática em si** (`scrum-master` linhas 65-66 e 325-326), os **cabeçalhos publicados** deste plano (9), as **duas linhas de `GOVERNANCA.md` §3 que prescrevem teto "no dossiê"** (tabela de classes, ramos *comportamental* e *investigação*) e o **instrumento** (`rdo.py`, `rdo_template.md`, `review_evidence.py`, `tests/`) |
| **`DX-16`** | **Destino do texto vivo do índice, e o flip dos 11 tíquetes já absorvidos** — decisão do dono de **2026-08-23**, tomada sobre a premissa falsa que bloqueou a `CTX-T6a`; **ratificada, não se reabre** | **Fato que a originou:** o contrato de corte da `CTX-T6a` exigia coluna *Título* ≤ 200 chars **sem exceção** (item 3) mas só autorizava destino para linha **terminal** (item 1). O executor mediu **16 linhas não-terminais** acima do teto, com conteúdo substantivo e sem destino — `P-0737-AUT` (421) e os tíquetes vivos `TK-04` (240), `TK-18` (1.084), `TK-23` (517), `TK-26` (3.015), `TK-27` (800), `TK-30` (2.016), `TK-32` (2.170), `TK-36` (2.447), `TK-37` (2.113), `TK-38` (2.743), `TK-42` (890), `TK-44` (896), `TK-46` (621), `TK-48` (508), `TK-50` (1.064) — somando **~21.545 chars (~5.386 tok)**, entre 35% e 70% do ganho que a própria tarefa promete. Parou e escalou, conforme a `DX-13`. **(1) Destino do vivo: seção no próprio diário.** Item vivo acima do teto ganha **seção `## <ID> — <título>` no próprio `docs/DIARIO_DE_OBRAS.md`**, e a célula do índice passa a **hook ≤ 200 chars + âncora** para ela — a mesma forma que os planos vivos já têm. Nenhuma residência nova nasce e `Arquivos-alvo` fica nos dois arquivos. **Recusadas, com o custo de cada uma:** arquivo próprio de tíquetes vivos (terceira residência de registro, arrastaria a skill `diario-de-obras` e o bootstrap — escopo além dos dois alvos); e relaxar o item 3 (deixaria a causa `C3` intacta justamente na tabela que todo pickup lê). **(2) Consequência sobre o aceite:** o critério **"≤ 450 linhas" cai** — texto que sai da tabela e fica no mesmo arquivo não reduz linha; o aceite passa a medir **o que o pickup lê**: chars da tabela do índice, com o teto por célula. **(3) Flip autorizado, com carve-out declarado à `DX-9`:** os **11 tíquetes** que a poda de 2026-08-22 declarou **absorvidos pelo `P-0737`** (`TK-04`, `TK-18`, `TK-26`, `TK-27`, `TK-30`, `TK-36`, `TK-37`, `TK-42`, `TK-44`, `TK-46`, `TK-50`) passam a `cancelled *(absorvido pelo P-0737, fecha na AUT-T<n>)*` **nesta tarefa** e migram como terminais. É **consequência mecânica de decisão já tomada pelo dono**, cuja execução estava alocada à `AUT-T1` de um plano que **este plano paralisou**; trocar marcador de status de tíquete não cria passo, ramo, contador nem roteamento, logo não é mexer em fluxo. **Salvaguarda contra a objeção que o executor levantou** (arquivar item aberto misrepresenta trabalho vivo como fechado): o ponteiro `fecha na AUT-T<n>` é preservado **verbatim** em cada linha migrada, e a seção `## P-0737` do diário ativo recebe a **lista dos 11**, de modo que a matéria continua visível a partir do plano vivo que a carrega. Sobram **5** linhas vivas acima do teto — `P-0737-AUT`, `TK-23`, `TK-32`, `TK-38`, `TK-48` —, tratadas pelo item (1) |

## 3. Invariantes de execução (valem para todas as tarefas)

1. **As duas regras do `DX-13` valem desde já, separadas** — **(a)** sinal de **poluição** do contexto
   para a tarefa **no ato e não graciosamente**: nada se termina, nada do produzido depois do sinal se
   aproveita, e o retorno ao orquestrador **demanda contexto limpo para a reexecução**. **(b)**
   **Capacidade** não interrompe tarefa em curso: é diretriz de **dimensionamento** exercida por quem
   planeja — cada tarefa deste plano foi dimensionada para caber em contexto coeso, autossuficiente e
   em ~50% de ocupação (tolerância a 60%). Teto, orçamento e contagem de write-clusters **não são do
   executor**: são régua **interna** de quem planeja, e estouro é **registrado no corpo da tarefa**
   como insumo de revisão do plano. **`DX-15`:** régua interna **não se publica** — o cabeçalho de
   tarefa não carrega teto, e a única referência numérica vive na tabela de classes de
   `GOVERNANCA.md` §3, endereçada ao planejador. É o que a `CTX-T1`/`CTX-T1b`/`CTX-T1c`/`CTX-T1d`
   tornam permanente; aqui já vale.
9. **Gramática do cabeçalho de tarefa (`DX-15`), vigente desde esta rodada:**
   `### <ID> — <título> [<modelo> · classe <classe>]`. `<modelo>` existe para o `scrum-master`
   instanciar o executor adequado; `<classe>` permanece como está enquanto a `Q1` estiver aberta.
   Card autorado daqui em diante — inclusive os `CTX-T6..T9` da charneira — nasce nesta gramática.
2. **Nada se lê integralmente acima de 500 linhas.** Artefato grande ou com linha de milhares de
   chars mede-se por **sonda programática** (`DC-4`); entrada em doc grande é sempre Grep de âncora →
   Read com `offset`/`limit`. Saída de ferramenta vai para arquivo: só o agregado entra no contexto.
3. **Nenhuma correção de fluxo antes da `## 9` ratificada** (`DX-2`), exceto a `CTX-T1`.
4. **Instrumento nasce com teste.** Todo `.py` tocado entra com teste em `tests/`, e o piso de
   regressão da suíte nunca desce.
5. **Bateria de fechamento de toda tarefa** — os quatro primeiros em exit 0:
   `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate`,
   `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift`,
   `pwsh -NoProfile -File .claude/checks/check-readme.ps1`,
   `python .claude/checks/dead_code.py`, e `python -m pytest` na raiz do hub.
6. **Redação:** `.claude/skills/redacao-doc/SKILL.md` é normativa em todo texto publicado. Plano e
   decision record são registro e são isentos.
7. **Contagem de linha herdada se reconfere por Grep na entrada da tarefa** — nenhuma edição se apoia
   em número de linha copiado de rodada anterior.
8. **Registro já escrito não se reescreve.** Bullets de fechamento, dossiês e prosa que narra o
   ocorrido ficam como estão; só marcador vivo migra.

## 4. Absorção — o que este plano recolhe (`DX-8`)

| Origem | Matéria | Onde fecha |
|---|---|---|
| `P-0737` §8 **(b)** — otimização de contexto do `scrum-master` | `.claude/skills/scrum-master/SKILL.md` tem 21.660 chars, maior que a maior fonte do pickup medido | medida na `CTX-T2`/`CTX-T3`, rota na `CTX-T4`, card no Estágio C |
| `TK-23` | variante (b) do proxy de ocupação (contador de tarefas por janela) nunca medida; a variante (a) já é `.claude/tools/ocupacao.py` | `CTX-T3` (mede a série) e `CTX-T4` (rota; `manter` é resposta válida) |
| `P-0737` §8 **(c)** — contextos dos agentes instanciados | custo de instanciar cada papel, por janela de subagente | `CTX-T3` |
| `TK-32` + item 4 da `T17` do `P-0734` | uso e teto como medida de **agregado**: (i) quantas tarefas por classe cruzaram o teto e por quanto, (ii) em quantos cruzamentos a consequência prescrita ocorreu, (iii) o custo do próprio controle em turnos | os três números na `CTX-T3`; a matéria doutrinária fecha na `CTX-T1` |

**Não absorvido:** `P-0737` §8 **(a)**, o piloto medido do loop — validação do loop, matéria daquele
plano. `TK-38` e `TK-48` seguem vivos, sem toque.

## 5. Tarefas

### CTX-T1 — As duas normas do `DX-13` na doutrina canônica [Opus · classe redacao]
- **Objetivo:** publicar como permanentes, cada uma na residência que a régua de `GOVERNANCA.md`
  §3.1 lhe dá (`DX-14`), as **duas** normas em que o adendo do dono partiu o enunciado único que
  hoje só vive como regra temporária do `P-0737` (§3, invariante 5, `DU-14`) e morre com ele:
  **(1) poluição de contexto** — regra **final** de execução, com guardrail; **(2) capacidade de
  contexto** — **diretriz de planejamento**, sem guardrail.
- **Contexto fechado (não buscar):** o conteúdo normativo das duas está integralmente na `DX-13`
  desta `## 2`; as residências e o racional delas, na `DX-14`. Nada mais se lê para decidir — só
  para editar.
- **Arquivos-alvo, com a âncora de entrada** (reconferir a linha por Grep, invariante 7):
  1. `.claude/global/CLAUDE.md`, **Regra 2 — Integridade do contexto** (âncora: `## Regra 2 —`).
     **Residência canônica da norma (1)** (§3.1 pergunta 1: vale fora de projeto Pantonic e já mora
     aqui). Duas edições: o bullet **Coesão** recebe a consequência obrigatória — parada **não
     graciosa** no ato, **nada do produzido depois do sinal se aproveita**, retorno a quem orquestra
     **demandando contexto limpo para a reexecução**; o bullet **Capacidade** deixa de prescrever
     interrupção e passa a prescrever **dimensionamento do trabalho antes de começar**, com o
     número, a proveniência e a cláusula de revisão da `DX-13`. O parágrafo **Como aplicar** perde
     "ao cruzar a capacidade, grave um checkpoint" como caminho de interrupção de tarefa.
  2. `GOVERNANCA.md` §4.3 (âncora: `### 4.3 Execução em contexto limpo`): o bullet **Coesão** ganha a
     mesma consequência não graciosa, em texto operacional do framework; o bullet **Capacidade**
     **sai** de condição de execução e vira **uma linha de ponteiro** para §3, declarando que
     **capacidade nunca interrompe tarefa em curso**; o parágrafo que hoje faz a janela de
     orquestração "encerrar na capacidade" é preservado, **requalificado** como encerramento
     planejado da janela de orquestração **entre tarefas** — nunca dentro de tarefa, nunca do
     executor —, com `.claude/tools/ocupacao.py` citado como **aviso informativo** (`DX-14`, item 3).
  3. `GOVERNANCA.md` §3, bloco *"Orçamento de turnos por tarefa atômica"* (âncora:
     `**Orçamento de turnos por tarefa atômica`): **residência canônica da norma (2)**, em subtítulo
     próprio — **Diretriz de dimensionamento de tarefa (do planejador)** — com os três critérios
     (contexto coerente e coeso; autossuficiência de contexto para a execução; ~50% de ocupação com
     tolerância a 60%), a **proveniência** (literatura sobre decaimento de desempenho de agentes em
     função do enchimento do contexto) e a **cláusula de revisão** (o número cai se a literatura
     indicar outro). A tabela de classes e o parágrafo *"alarme, nunca bloqueio"* ficam onde estão,
     agora **subordinados** à diretriz e explicitamente **endereçados ao planejador** — a tabela
     passa a ser a **única** residência de número de teto, e é **régua interna** de quem dimensiona.
     **`DX-15`, duas células da tabela ficaram falsas e se corrigem aqui** (âncoras:
     `teto numérico por ramo obrigatório no dossiê`, no ramo *Comportamental multi-camada*, e
     `o teto é **prescrito no dossiê**`, no ramo *Investigação / mapeamento*): o dossiê **não
     carrega mais teto** — em *Comportamental*, o que era teto por ramo vira critério de
     **partição** da tarefa (ramo que não cabe vira outra tarefa); em *Investigação*, o que fica
     prescrito no dossiê é o **método de sondagem**, e o teto é régua interna do planejador. Mesmo
     tratamento na linha do parágrafo de replanejamento (âncora: `fica na mesma classe, com teto`),
     que declara `≤50`: o número **fica na tabela**, não no card.
  4. `GOVERNANCA.md` §7 item 7 (*Disciplina de contexto*): passa a enunciar **só a poluição**, como
     guardrail, com ponteiro para a residência canônica; a menção a "teto de trabalho de ~50% da
     janela" **sai do guardrail** e vira ponteiro para §3 — diretriz não mora onde guardrail mora.
  5. `CHANGELOG.md`, sob `## [Não lançado]` — uma linha (`G-SURFACE`).
  6. `docs/plans/P-0737-loop-autonomo.md` §3, invariante 5 — **uma linha** de ponteiro declarando a
     regra promovida a permanente, **partida em duas** pela `DX-13`, e onde cada metade passa a
     morar. É registro, não reabertura: nada mais daquele plano é tocado e nenhuma tarefa sai dele.
- **Contratos/artefatos:** régua de residência (`GOVERNANCA.md` §3.1) — **um** lugar canônico por
  norma, os demais apontam; **nenhum guardrail novo é criado** e **nenhuma sigla nova** (sigla nova é
  volume de doutrina, que é parte do defeito que este plano ataca); **nenhum número novo** se
  inventa — 50%/60% são os da `DX-13` e o `LIMIAR` de `ocupacao.py` não se toca.
- **Proibido:** editar `.claude/skills/`, `.claude/agents/` ou `.claude/tools/` — a superfície
  executável é da `CTX-T1b` e da `CTX-T1c`, e duplicar a edição aqui cria duas fontes que divergem.
  Reabrir o mérito do adendo (é decisão do dono, `DX-13`).
- **Verificação:** `Grep pattern:"contexto limpo para a reexecução" path:.claude/global/CLAUDE.md`
  e `path:GOVERNANCA.md` devolvem a consequência nos dois lugares; `Grep pattern:"tolerância"
  path:GOVERNANCA.md` devolve a diretriz em §3 e **não** em §4.3 nem em §7; bateria do §3 em exit 0;
  `git status --short` acusa só os quatro arquivos.
- **Nota de projeção:** a projeção do alvo `usuario` (`~/.claude/CLAUDE.md`) é **opt-in do dono**
  (`DL-4`) e está **fora** do `check-drift`; **não** é critério de pronto desta tarefa.
- **Pronto quando:** a norma (1) é canônica na Regra 2 do `.claude/global/CLAUDE.md`, com texto
  operacional em §4.3 e guardrail em §7 item 7; a norma (2) é canônica em `GOVERNANCA.md` §3, com
  ponteiro em §4.3; o `CHANGELOG.md` registra; e o `P-0737` aponta para as duas residências.

### CTX-T1b — Responsabilidade: o executor só executa, e quem revisa plano é o planejador [Opus · classe redacao]
- **Objetivo:** reconciliar a superfície de **papéis** com a `DX-13` (`G-SURFACE`, guardrail 16):
  teto e orçamento saem do horizonte do executor e entram no do planejador; a **escada de escalada**
  passa a ser explícita — indício de que o plano deve ser revisto leva o plano a **`blocked`** e a
  matéria ao **planejador**, que decide revisão **técnica e tática**, escalando ao **dono** o que for
  **estratégico ou alterar escopo**.
- **Contexto fechado (não buscar):** a norma está na `DX-13`; as residências, na `DX-14` (itens 4
  e 5). Os pontos de contato desta tarefa foram varridos e estão listados abaixo com a âncora.
- **Arquivos-alvo, com a âncora de entrada** (reconferir a linha por Grep, invariante 7):
  1. `GOVERNANCA.md` §3, **matriz de responsabilidades** (âncora: `| Papel | Modelo | Responde por`)
     — **residência canônica** desta matéria. Quatro células: **Planejamento** / *Responde por* ganha
     o **dimensionamento de cada tarefa sob a diretriz de §3** e a **exclusividade da revisão de
     plano**, com a escada técnico-tático → estratégico/escopo; **Execução** / *Responde por* fica
     com **executar a tarefa** como responsabilidade única, e / *Não faz* ganha **não se ocupa de
     teto nem de orçamento** e **não revisa plano**; **Orquestração** / *Não faz* ganha **não revisa
     plano** (o `scrum-master` roteia, não replaneja); **Revisão** fica como está — já diz que
     consumo é informação e não fundamento de marcação (confirmar por Grep, sem editar).
  2. `GOVERNANCA.md` §3, logo abaixo da matriz — **parágrafo da escada**, curto: quem suspeita,
     quem marca `blocked`, quem recebe, o que o planejador decide sozinho e o que sobe ao dono. Sem
     sigla nova.
  3. `GOVERNANCA.md` §4, tabela de filiação ágil, linha *Item de backlog / história* (âncora:
     `o orçamento de turnos por classe (§3) dimensiona, não delimita`) e o parágrafo das duas
     práticas que não viajam (âncora: `Duas práticas ágeis`) — reapontar para a diretriz de §3 e
     nomear o **planejador** como quem dimensiona.
  4. `.claude/agents/pantonic-planner.md`, `## Suas responsabilidades` — **item novo**: dimensionar
     cada tarefa sob a diretriz (coeso, autossuficiente, ~50% com tolerância a 60%) e **receber a
     escalada** de revisão de plano, com a fronteira do que sobe ao dono. Ponteiro para
     `GOVERNANCA.md` §3, sem repetir o texto normativo. **`DX-15`:** o dimensionamento é **exercido,
     não publicado** — o cabeçalho que o planejador escreve é
     `### <ID> — <título> [<modelo> · classe <classe>]`, e `<modelo>` está lá por um consumidor
     nomeado: é por ele que o `scrum-master` instancia o executor adequado. **Nenhum teto se
     escreve em card**; a régua numérica é a tabela de classes de `GOVERNANCA.md` §3, interna a
     este papel.
  5. `.claude/agents/pantonic-executor.md`, bullet **Economia de turnos** (âncora:
     `O orçamento de turnos da classe declarada no dossiê`) — o trecho sobre orçamento **sai**: o
     executor não o observa. Fica: a **única** responsabilidade é executar a tarefa; o consumo é
     medido por quem orquestra; **estouro de teto, de orçamento ou de contexto se registra no corpo
     da tarefa** e é insumo do planejador, nunca decisão do executor. A disciplina de **economia de
     turnos** (batching, cadência de testes, não reler arquivo editado) **permanece** — é método de
     trabalho, não teto. No item 4 do `## Protocolo de execução` (âncora: `Escopo estrito`), o
     `blocked` com razão tipada ganha o caso **"o plano parece precisar de revisão"** mapeado à razão
     **`premissa`** já existente — **nenhum valor novo se cria**.
  6. `.claude/skills/handover/SKILL.md`, seção do **checkpoint intermediário** (âncoras:
     `Contexto acabando sem plano de parada` e `Teto do próprio checkpoint`) — separar os dois casos
     que hoje o mesmo checkpoint atende: **poluição** passa a ser retorno **não gracioso** (declaração
     de contexto poluído + demanda de reexecução, sem ponteiro de retomada, porque não há retomada);
     **contexto acabando dentro de uma tarefa** passa a ser **sintoma de tarefa mal dimensionada** —
     registra-se no corpo da tarefa e devolve-se ao planejador, e **não** se retoma parcialmente em
     contexto novo (é o custo dobrado que a `DX-13` proíbe). O checkpoint de ponteiro de estado
     **permanece** para o encerramento planejado da **janela de orquestração**.
  7. `CHANGELOG.md`, sob `## [Não lançado]` — uma linha (`G-SURFACE`).
- **Contratos/artefatos:** matriz de responsabilidades (`GOVERNANCA.md` §3) é a **fonte única**; os
  agentes e a skill **apontam**. Conjunto de razões tipadas de `blocked` (`dependencia` | `premissa`)
  é fechado e **não se amplia** — residência única na skill `diario-de-obras`.
- **Proibido:** criar valor de status, razão tipada, guardrail ou sigla; alterar a tabela de
  roteamento do `scrum-master` (é da `CTX-T1c`, e só por deleção/ponteiro); reabrir o `DX-13`.
- **Verificação:** `Grep pattern:"revisa plano" path:GOVERNANCA.md -n` devolve a matriz e o
  parágrafo da escada; `Grep pattern:"orçamento" path:.claude/agents/pantonic-executor.md` **não
  devolve nada**; `Grep pattern:"tolerância" path:.claude/agents/pantonic-planner.md` devolve o item
  novo; bateria do §3 em exit 0 (inclui `kit_check -Mode check-drift`, que cobre o `.claude/README.md`
  regenerado); `git status --short` acusa só os cinco arquivos.
- **Pronto quando:** um executor que leia só o próprio agente não encontra nenhuma instrução de
  observar teto ou orçamento, e a escada de revisão de plano está escrita uma única vez, em
  `GOVERNANCA.md` §3, com ponteiro nos três artefatos que a exercem.

### CTX-T1c — Skills de fluxo e instrumentos: retirar o que a decisão do dono tornou falso [Opus · classe redacao]
- **Objetivo:** fechar a `G-SURFACE` no kit executável — retirar de artefato de fluxo, **por deleção
  ou ponteiro**, o texto que orça teto do executor e manda parar por número, e registrar como achado
  o que exigiria **fluxo novo** (que é do `P-0737`, `blocked`).
- **Fronteira, declarada antes do trabalho (`DX-14`, item 6):** retirar texto falso **não é** mexer
  no fluxo. Esta tarefa **não cria** passo, ramo, contador nem linha de roteamento; onde a
  reconciliação exigiria criar, a tarefa **para de editar** e escreve **uma linha** em `## 9.
  Achados` deste plano, insumo obrigatório da `AUT-T6`/`AUT-T9`.
- **Contexto fechado (não buscar):** a norma está na `DX-13`; a fronteira e as residências, na
  `DX-14`. Os pontos de contato foram varridos e estão abaixo com a âncora.
- **Arquivos-alvo, com a âncora de entrada** (reconferir a linha por Grep, invariante 7):
  1. `.claude/skills/proximo-passo/SKILL.md`, **gate de delegação**, item 5 (âncora:
     `Orçamento por volume: contar write-clusters`) — o **"PARE e reporte ao atingir N"** e o teto
     numérico por ramo **saem**: são responsabilidade devolvida ao planejador. O que **fica** é o
     critério de **decomposição** (>8 write-clusters → dividir **antes** de delegar; ≥3 camadas da
     regra de dependência → decompor por camada), reapresentado como **dimensionamento do
     planejador** sob a diretriz de `GOVERNANCA.md` §3, com ponteiro. Mesmo tratamento no item 6
     (âncora: `Tarefa-investigação`), que fixa "teto numérico por padrão": o **método de sondagem
     prescrito** fica, e o teto **sai do dossiê** (`DX-15`) — não vira declaração no card, vira
     régua interna da tabela de §3. No item 3 (âncora: `sem isso o executor
     paga a localização em tool uses`) e no item 1 do escopamento (âncora: `orçada fora do teto do
     executor`), a justificativa por "excedente de teto do executor" vira justificativa por
     **autossuficiência de contexto da tarefa** — o critério (b) da diretriz.
  2. `.claude/skills/scrum-master/SKILL.md` — **seis** âncoras, todas por deleção ou ponteiro.
     **Gramática (`DX-15`), duas âncoras:** `na gramática `### <ID> — <título>` (passo 3, "Saída")
     e `Cabeçalho sem `[<modelo> · classe <classe>` (seção de precedência) passam a enunciar
     `### <ID> — <título> [<modelo> · classe <classe>]`, e a frase de rota fica **só sobre o
     modelo** — cabeçalho sem `[<modelo> · …]` é tarefa fora da gramática e cai em `B3`, porque
     sem modelo não há como **instanciar o executor adequado**, que é o consumidor nomeado pelo
     dono. **Teto (`DX-15`), duas âncoras, por deleção:**
     `O teto de tool uses da tarefa é o da classe registrada` **sai inteira** (não há teto no
     cabeçalho e o `scrum-master` não observa teto), e `O consumo medido da tarefa — os `tools`
     gastos contra o teto` perde o "contra o teto": o consumo é **medido e registrado**, ponto —
     nunca critério de rota (`DP-Q`). A âncora `teto de campo estourado` da linha `A2` é
     **homônima** (limite de tamanho do campo de retorno) e **não se toca**. **Poluição e
     escalada, duas âncoras:** a âncora `Parada legítima não tem teto` e o bloco **B2** (âncora:
     `sinal de poluição do contexto
     do loop`) recebem a consequência **não graciosa** da norma (1) — encerra **sem aproveitar o
     produzido depois do sinal** —, sem criar ramo novo, porque **B2 já existe e já para**; e a
     seção de precedência ganha **uma linha de ponteiro**: o `scrum-master` **não revisa plano**
     (`GOVERNANCA.md` §3) — indício de revisão leva o **plano** a `blocked` e a matéria ao
     planejador. **Se a materialização do retorno de poluição exigir valor ou ramo novo na tabela
     `A`/`B`, não se cria:** vira linha em `## 9. Achados`.
  3. `.claude/skills/diario-de-obras/SKILL.md`, seção **Status — residência única** (âncora:
     `| `blocked` | item que existe e não pode ser executado agora`) — **uma linha**, sem valor novo:
     "plano cuja revisão foi pedida por quem executa ou orquestra" é caso de **`blocked` de plano**,
     com razão registrada, e a razão tipada de **tarefa** correspondente é `premissa`. A máquina de
     transições **não muda**.
  4. `.claude/tools/ocupacao.py`, docstring de módulo e comentário do `LIMIAR` (âncoras:
     `instrumento da condição de **capacidade**` e `LIMIAR = 0.50`) — **só o texto**: o instrumento
     é reclassificado como **aviso informativo à orquestração entre tarefas** e o ponteiro de
     residência muda de "§4.3, condição de execução" para "§3, diretriz de dimensionamento". **O
     valor `0.50`, o hook e o comportamento não mudam** (`DX-14`, item 3) — logo **nenhum teste novo
     é exigido** por esta edição, e nenhum teste existente pode quebrar; se algum teste afirmar o
     texto da docstring, ele acompanha a edição.
  5. **Confirmações sem edição** (uma verificação cada, e o resultado vai no corpo da tarefa):
     `.claude/tools/telemetria.py` — registra medida, **sem objeto**;
     `.claude/agents/pantonic-reviewer.md` — já conforme. Nenhum dos dois entra no `git status`.
     **`DX-15` moveu os instrumentos daqui:** `.claude/tools/rdo.py`, `.claude/tools/rdo_template.md`
     e `.claude/tools/review_evidence.py` deixaram de ser confirmação e passaram a ser edição — são
     matéria da **`CTX-T1d`**, que corre logo depois desta. Esta tarefa **não toca `.py`** (a
     proibição abaixo continua literal).
  6. `CHANGELOG.md`, sob `## [Não lançado]` — uma linha (`G-SURFACE`).
- **Contratos/artefatos:** conjunto fechado de status e razões tipadas (skill `diario-de-obras`,
  residência única); tabela de roteamento do `scrum-master` (**não se altera**); `DX-9` e o carve-out
  da `DX-14` item 6.
- **Proibido:** criar passo, ramo, contador, status, razão tipada ou linha de roteamento; mexer em
  `LIMIAR`, no hook de `.claude/settings.json` ou em qualquer comportamento de `.py`; reescrever a
  skill `proximo-passo` além das âncoras listadas (a rota dela está **fora de escopo**, `## 7`).
- **Verificação:** `Grep pattern:"PARE e reporte" path:.claude/skills/` **não devolve nada**;
  `Grep pattern:"teto" path:.claude/skills/ -n` não devolve **nenhuma** linha que prescreva número
  a quem executa ou orquestra — só ponteiro para `GOVERNANCA.md` §3 e a linha **homônima**
  `teto de campo estourado` do ramo `A2` do `scrum-master`;
  `Grep pattern:"classe <classe>" path:.claude/skills/scrum-master/SKILL.md` devolve as duas linhas
  de gramática **sem** ` · teto`; `python -m pytest` verde com o piso de regressão intacto; bateria do §3 em
  exit 0; `git status --short` acusa só os cinco arquivos editáveis.
- **Pronto quando:** nenhum artefato do kit executável manda o executor parar por número, o
  `scrum-master` declara que não revisa plano, e todo resíduo que exigiria fluxo novo está em `## 9`
  com destino nomeado.

### CTX-T1d — A gramática nova do cabeçalho nos instrumentos [Sonnet · classe implementacao]
- **Objetivo:** fazer o parser da `DP-C` falar a gramática que a `DX-15` fixou —
  `### <ID> — <título> [<modelo> · classe <classe>]` — **aceitando** o cabeçalho histórico com
  ` · teto <N>` e **descartando** o valor. É remoção de campo, não fluxo novo: nenhum passo, ramo,
  contador ou linha de roteamento nasce aqui (carve-out da `DX-15`).
- **Contexto fechado (não buscar):** a gramática e o racional estão na `DX-15`. O campo era
  **redundante por construção** — `rdo.py` já recusava `teto` diferente do default da classe —,
  então **nada se perde** ao descartá-lo, e **nada se deriva** para substituí-lo: o número não
  reaparece em lugar nenhum do RDO.
- **Arquivos-alvo, com a âncora de entrada** (reconferir a linha por Grep, invariante 7):
  1. `.claude/tools/rdo.py`, **regex do cabeçalho** (âncora: `_HEADER_BRACKET_RE = re.compile`) —
     o segmento de teto vira opcional e **anônimo** (deixa de ser grupo nomeado, porque ninguém o
     lê). Texto exato do substituto, para não haver invenção:
     ```python
     _HEADER_BRACKET_RE = re.compile(
         r"^### (?P<id>T[0-9]+[a-z]?) — (?P<titulo>.+?) "
         r"\[(?P<modelo>Opus|Sonnet|Haiku) · classe (?P<classe>.+?)"
         r"(?: · teto (?:prescrito )?[0-9]+)?\](?P<sufixo>.*)$"
     )
     ```
  2. `.claude/tools/rdo.py`, **`DossieTarefa`** (âncora: `def __init__(self, tarefa_id, titulo,`) —
     o parâmetro e o atributo `teto` **saem**.
  3. `.claude/tools/rdo.py`, **`extrair_dossie`** (âncora: `def extrair_dossie(`) — sai o kwarg
     `teto_legado`; saem os **dois** blocos de validação `teto != default_teto` (âncora, duas
     ocorrências: `diferente do default da classe`); sai `("--teto", teto_legado)` da lista
     `faltando` e o `int(teto_legado)` com o `RdoValidationError` de "não é inteiro"; sai
     `teto=teto` do `return DossieTarefa(`. A mensagem de plano legado passa a dizer
     **"não declara modelo/classe"**. **`classe` não se toca** — normalização, aliases e recusa de
     classe fora do conjunto ficam **idênticas** (`Q1` está aberta, e nada aqui pode antecipá-la).
  4. `.claude/tools/rdo.py`, **`_CLASSE_TETO_DEFAULT`** (âncora: `_CLASSE_TETO_DEFAULT`) — o dict
     **permanece com o nome e os valores que tem**, e o comentário acima dele passa a declarar o que
     ele é agora: o **conjunto normativo de classes** (usado nas mensagens de erro); os números são
     **régua do planejador** em `GOVERNANCA.md` §3 e **este módulo não os lê mais**. Renomear
     arrastaria mensagens e testes por ganho cosmético, e o destino do campo `classe` é a `Q1`.
  5. `.claude/tools/rdo.py`, **CLI** (âncoras: `"--esquema-legado",` e
     `close_parser.add_argument("--teto"`) — o argumento `--teto` **sai**; o `help` do
     `--esquema-legado` passa a `Cabeçalho sem [modelo · classe] — exige --modelo/--classe`; some
     `teto_legado=args.teto` da chamada (âncora: `esquema_legado=args.esquema_legado`).
  6. `.claude/tools/rdo.py`, **docstring de módulo** (âncoras: `[--esquema-legado --modelo --classe`
     e `Plano legado (cabeçalho sem`) — a linha de uso perde `--teto`; o parágrafo de plano legado
     passa a definir legado como **cabeçalho sem colchete algum** e a citar a gramática nova, com
     a nota de que ` · teto <N>` histórico é **aceito e descartado** (`DX-15`).
  7. `.claude/tools/rdo_template.md`, duas linhas (âncoras: `**Modelo:** {{MODELO}}` e
     `**Consumo:** {{TOOL_USES}}`) — o placeholder `{{TETO}}` **sai das duas**: a linha de
     identificação fica `**Modelo:** {{MODELO}} · **Classe:** {{CLASSE}}` e a de consumo fica
     `**Consumo:** {{TOOL_USES}} tool uses, {{TOKENS_K}} k tokens, {{DURACAO_S}} s (fonte: `<usage>`
     do encerramento)`. Some também a entrada `"TETO"` do mapping (âncora: `"CLASSE": dossie.classe`).
     **O RDO não passa a derivar o teto da classe:** o número deixa de existir no documento.
  8. `.claude/tools/review_evidence.py` (âncora: `esquema_legado=False,`) — sai o `teto_legado=None`
     da chamada a `extrair_dossie`. **`teto_diff_chars`/`teto_chars` é homônimo** (truncamento de
     evidência) e **não se toca**.
  9. `tests/test_rdo.py` e `tests/test_review_evidence.py` (âncoras: `classe implementação padrão`,
     `TETO`, `teto do cabeçalho`) — as fixtures migram para a gramática nova; o teste do erro
     "teto diferente do default" **cai** (o erro não existe mais); os asserts sobre `{{TETO}}`/
     `TOOL_USES` acompanham a linha nova de consumo. **Dois testes novos:** (a) cabeçalho na
     gramática nova parseia, com `modelo` e `classe` corretos; (b) cabeçalho **histórico** com
     ` · teto 40` parseia, devolve o mesmo `titulo`/`classe` e o RDO gerado **não contém** a palavra
     `Teto`. O piso de regressão da suíte **não desce**.
  10. `CHANGELOG.md`, sob `## [Não lançado]` — uma linha (`G-SURFACE`).
- **Contratos/artefatos:** `DP-C` (gramática do cabeçalho e política de plano legado); `DP-Q`
  (nenhum número governa fluxo); conjunto de classes de `GOVERNANCA.md` §3, **inalterado**.
- **Proibido:** tocar `_ID_HEADER_RE` (ver o achado de identificador prefixado na `## 9` — é
  matéria de outro plano, e corrigi-lo aqui seria correção antes da medida, `DX-2`); mexer em
  `_CLASSE_ALIASES`, em `_normalizar_classe` ou em qualquer coisa que dependa do desfecho da `Q1`;
  reescrever cabeçalho de plano fechado ou do `P-0737` (`DX-15`, migração); criar flag, subcomando
  ou campo novo.
- **Verificação:** `python -m pytest tests/test_rdo.py tests/test_review_evidence.py` verde;
  `Grep pattern:"teto" path:.claude/tools/rdo.py -n` devolve **apenas** o segmento opcional da regex,
  o comentário do `_CLASSE_TETO_DEFAULT` e a nota de descarte na docstring — nenhuma validação e
  nenhum argumento; `Grep pattern:"TETO" path:.claude/tools/` **não devolve nada**;
  `python .claude/checks/dead_code.py` em exit 0; bateria do §3 em exit 0; `git status --short`
  acusa só os cinco arquivos (`rdo.py`, `rdo_template.md`, `review_evidence.py`, os dois de teste)
  mais o `CHANGELOG.md`.
- **Pronto quando:** um cabeçalho escrito na gramática da `DX-15` é parseado sem flag nenhuma, um
  cabeçalho histórico com teto continua parseando com o número ignorado, nenhum teto sobrevive no
  RDO gerado, e a suíte está verde com o piso intacto.

### CTX-T2 — Forense das janelas da `AUT-T5b`: onde a ocupação nasce e onde ela cresce [Sonnet · classe investigacao]
- **Objetivo:** medir, com dado do transcript e não com estimativa, **quanto uma janela de
  orquestração já custa antes do primeiro ato** e **o que a leva ao teto** — o vão que o `P-0736`
  deixou aberto ao declarar que o pickup medido é piso, não teto.
- **Arquivos-alvo:** cria `sonda_janela.py` **no scratchpad da sessão** (descartável, não
  versionado); edita `docs/CUSTO_DO_PICKUP.md` acrescentando `## 7 Anatomia de uma janela de
  orquestração` (**≤ 60 linhas**); edita `docs/DOC_MAP.md` (entrada do relatório).
- **Corpus:** `C:\Users\panta\.claude\projects\d--workspaces-PantonicApp\*.jsonl` — **só** os `.jsonl`
  de sessão principal (raiz do diretório; os de `**/subagents/*.jsonl` são da `CTX-T3`). Seleção
  fechada: os que contêm a string `AUT-T5b` e cujo primeiro `timestamp` é de **2026-08-22**,
  ordenados por esse timestamp. Encontrados menos de três, a tarefa mede os que existirem e registra
  `ausente` para os demais — **o método não depende de as três estarem lá**, porque a decomposição
  fixo × variável se prova com uma janela.
- **Métricas por janela** (`DX-4`, parse de `.claude/tools/ocupacao.py:63`): ocupação do **primeiro**
  `usage` (`DX-5`) · ocupação final · nº de turnos · nº de blocos `tool_use` · turno em que a
  ocupação cruza **100.000 tokens** (os ~50% da diretriz de dimensionamento — residência em
  `GOVERNANCA.md` §3 depois da `CTX-T1`; aqui o número é **régua de medida**, não gatilho) e o que havia sido
  ingerido até ali · **top 10 contribuintes** por `tool_result` (nome da ferramenta + alvo truncado
  em 60 chars + chars do resultado) · decomposição **fixo** (o primeiro `usage`) × **variável** (o
  resto).
- **Método:** `python <scratchpad>\sonda_janela.py > <scratchpad>\sonda_janela.md`; ler **só** o
  agregado (**≤ 120 linhas**, todo trecho textual truncado em 60 chars) e transcrevê-lo para a
  `## 7`. O script nunca aborta: caminho ausente ou JSON malformado vira linha `ausente` e segue.
  **Nenhum conteúdo de transcript entra no contexto** — só o agregado.
- **Correção de fato, no mesmo ato:** `docs/DOC_MAP.md` promete hoje uma seção `## 7 Veredito do
  dono` em `docs/CUSTO_DO_PICKUP.md` que **não existe** (a `CPK-T4` ficou sem objeto). A entrada é
  corrigida para o conteúdo real do arquivo, já com as seções desta rodada e o teto novo de 320
  linhas (`DX-3`).
- **Verificação:** script em exit 0; agregado ≤ 120 linhas; a `## 7` traz, por janela medida, as
  sete métricas e o número da `DX-5` em destaque; `(Get-Content docs\CUSTO_DO_PICKUP.md).Count` ≤ 320;
  `git status --short` acusa só `docs/CUSTO_DO_PICKUP.md` e `docs/DOC_MAP.md`.
- **Pronto quando:** existe um número medido para *"quanto custa abrir uma janela de orquestração
  sem fazer nada"* e a atribuição do crescimento até o teto está publicada.

### CTX-T3 — A série: custo por papel, custo do controle e os três números do `TK-32` [Sonnet · classe investigacao]
- **Objetivo:** sair do caso e ir à série — quanto custa **instanciar** cada papel do kit, quantas
  janelas uma tarefa atômica consome em regime, e o que o controle por teto de fato produziu.
- **Arquivos-alvo:** reusa/estende `sonda_janela.py` **no scratchpad**; edita
  `docs/CUSTO_DO_PICKUP.md` acrescentando `## 8 A série: custo por papel e custo do controle`
  (**≤ 50 linhas**). Nenhum outro arquivo.
- **Fontes:** `docs/telemetria.tsv` (fonte única da série, `GOVERNANCA.md` §4.2 — colunas `data`,
  `projeto`, `tarefa`, `modelo`, `tool_uses`, `tokens_k`, `duracao_s`, `fonte`) e os transcripts de
  subagente `C:\Users\panta\.claude\projects\d--workspaces-PantonicApp\**\subagents\*.jsonl`.
- **Entregáveis, cada um em número:**
  1. **Custo fixo de instanciação por papel** — mediana do primeiro `usage` (`DX-5`) das janelas de
     subagente, agrupadas por `agent_type`, com `n` por grupo.
  2. **Janelas por tarefa atômica** — para as tarefas do `P-0737` e do `P-0735` presentes na série,
     quantas janelas de orquestração cada uma consumiu; diz se a `AUT-T5b` é caso isolado ou padrão.
  3. **Os três números do `TK-32`** — (i) quantas tarefas **por classe** cruzaram o teto do regime
     anterior (o do cabeçalho, enquanto ele existiu — `DX-15`) e por quanto; (ii) em quantos desses cruzamentos a consequência prescrita de fato ocorreu; (iii)
     o custo do **próprio controle** em turnos (tool uses gastos em gate, contagem e partição).
     **Reconciliado pela `DX-13`:** os três números continuam sendo medidos, agora como **leitura
     histórica do regime anterior** e como **insumo de dimensionamento do planejador** — a **norma**
     já foi decidida pelo dono e **não se deriva daqui**. O item (ii) em particular mede uma
     consequência que **deixou de ser prescrita**: mede-se o passado, não se propõe rota normativa.
  4. **Estado do `TK-23`** — a variante (b) (contador de tarefas por janela) é medível pela série?
     Responder com número, sem escolher rota (a rota é da `CTX-T4`).
- **Verificação:** as quatro entregas têm número e `n`; toda linha da série usada é rastreável à
  `tarefa`; `## 8` ≤ 50 linhas; `git status --short` acusa só `docs/CUSTO_DO_PICKUP.md`.
- **Pronto quando:** os quatro blocos estão publicados com número, e o `TK-23`/`TK-32` deixam de ser
  matéria de opinião.

### CTX-T4 — Causas raízes, rota por causa e o round-trip único do dono [Opus · classe redacao]
- **Objetivo:** converter os números das `CTX-T2`/`CTX-T3` em **causas raízes**, cada uma com rota do
  conjunto fechado, e fechar a decisão do dono numa **única** mensagem (`DC-9`).
- **Arquivos-alvo:** edita `docs/CUSTO_DO_PICKUP.md` acrescentando `## 9 Causas raízes e veredito do
  dono (<data>)` (**≤ 40 linhas**). Nenhum outro arquivo.
- **Conteúdo da `## 9`, em tabela:** uma linha por causa raiz — causa · **evidência numérica** (da
  `## 7` ou `## 8`, com o número colado) · artefato-alvo com caminho exato · rota ∈ {`condensar`,
  `ponteiro`, `gerar-por-instrumento`, `mover-ao-historico`, `manter`, `amortizar`, `delegar`}
  (`DX-6`) · ganho esperado em tokens por janela · ordem de grandeza (`mecanica` | `implementacao` |
  `comportamental`). Causa sem número medido **não entra** na tabela: vira linha de `## 9. Achados`
  deste plano.
- **Veredito obrigatório dos três diagnósticos preliminares** do §0 — `(i)`, `(ii)`, `(iii)` — cada um
  `confirmado` | `parcial` | `refutado`, **com o número** que o sustenta. Diagnóstico refutado **não
  gera rota**. **Reconciliação pela `DX-13`:** a **metade normativa** do diagnóstico `(i)` — *"o gate
  de delegação orça o teto do executor"* — **já está decidida pelo dono** e sai do veredito: orçar
  teto é do planejador, e a superfície disso já se reconcilia na `CTX-T1c`. O que resta de `(i)` para
  o veredito é a **metade medível**: *delegar com a janela curta garante uma janela fria pagando
  pickup inteiro por um fechamento que vale ~5 tool uses*. Os diagnósticos `(ii)` e `(iii)` vão
  inteiros.
- **Round-trip único, uma só mensagem, quatro itens:** (1) o número da `DX-5` medido — quanto custa
  abrir uma janela hoje; (2) a tabela de causas ranqueada por ganho; (3) o alvo — o default da
  `DX-11` (40.000 chars / 10.000 tokens), pedindo ratificação ou troca; (4) perguntas fechadas:
  *ratifica as causas?*, *aceita a rota de cada uma (ou troca por outra do conjunto fechado)?*,
  *ratifica o alvo?*. As respostas viram a `## 9`, datadas e verbatim no que decidem.
- **Nada que a `DX-13` já decidiu volta ao dono** — levar de novo é desperdício de turno dele
  (`DC-9`). **Fora do round-trip, sem exceção:** a natureza das regras de poluição e de capacidade;
  de quem é a responsabilidade por teto e orçamento; a escada de revisão de plano; o número 50%/60%
  e sua proveniência. Se uma causa medida tocar esse terreno, a linha da tabela registra
  *"decidido em `DX-13`"* e **não vira pergunta**.
- **Proibido:** implementar qualquer rota; abrir card de correção (é da `CTX-T5`); reabrir a medida;
  reabrir a `DX-13`.
- **Verificação:** toda causa tem número e rota do conjunto fechado; os três diagnósticos têm
  veredito numérico; a `## 9` está datada e registra o alvo vigente; `git status --short` acusa só
  `docs/CUSTO_DO_PICKUP.md`.
- **Pronto quando:** o dono respondeu e a `## 9` registra causa, rota e alvo — o insumo fechado da
  charneira.

### CTX-T5 — Charneira: autorar o Estágio C já fechado [Opus · classe redacao (rodada de replanejamento)]
- **Objetivo:** transformar a `## 9` ratificada em cards de execução **fechados**, dentro deste mesmo
  arquivo — a tarefa que existe para que este plano vá até a execução sem publicar vão (`DX-1`).
- **Classe:** rodada de replanejamento (`GOVERNANCA.md` §3; o número da régua fica **lá**, não neste
  card — `DX-15`) — fechar a decisão e
  escrever os dossiês que ela produz acontecem no mesmo contexto, e parti-los obrigaria a repagar a
  leitura da decisão.
- **Arquivos-alvo:** `docs/plans/P-0738-contexto-esgotado.md` (esta `## 5`, acrescentando
  `### CTX-T6` .. `### CTX-T9`, e a `## 6` com a ordem final); `docs/DIARIO_DE_OBRAS.md` (seção
  `## P-0738 — Contexto esgotado na partida`: lista de tarefas e a linha **`Próxima tarefa`**;
  e a célula do índice, atualizando o denominador).
- **Regras de fechamento de cada card, sem exceção:**
  1. Cabeçalho na gramática vigente (`DX-15`): `### CTX-T<n> — <título> [<modelo> · classe <classe>]`
     — **sem teto**. `<modelo>` é obrigatório: é por ele que o `scrum-master` instancia o executor.
  2. Objetivo · arquivos-alvo com caminho exato · contratos/artefatos · verificação executável ·
     critério de pronto · **a causa da `## 9` que ele ataca** · o **ganho esperado em tokens**.
  3. **Nenhum card sem causa ratificada**; **nenhuma causa ratificada com rota diferente de
     `manter`** fica sem card — ou recebe, na `## 9`, a linha *"não vira card, porque…"*.
  4. Instrumento novo nasce com teste em `tests/` (invariante 4) e com chamador de produção
     (`G-DEADCODE`).
  5. **Fronteira `DX-9`:** card que precise alterar responsabilidade, passo, gate, contador ou tabela
     de roteamento do loop **não se autora** — vira linha em `## 9. Achados` deste plano, encaminhada
     à `AUT-T6`/`AUT-T9` do `P-0737`.
  6. Faixa `CTX-T6..T9`. Precisando de mais, **parte por letra** (`CTX-T6a`/`CTX-T6b`), nunca
     identificador fora da faixa; a `CTX-T10` e a `CTX-T11` não se renumeram.
  7. Ordem por **valor testável cedo**: o card de maior ganho medido por menor grandeza vem primeiro.
  8. **Dimensionamento sob a diretriz da `DX-13`, exercido aqui e *não* publicado no card** (`DX-15`:
     informação de teto é poluição para quem não tem autoridade sobre escopo) — a `CTX-T5` é
     ato de **planejamento**, e dimensionar é responsabilidade dela, não de quem executar o card.
     Cada card do Estágio C nasce dimensionado para **(a)** caber num **contexto coerente e coeso**
     (uma matéria só; matéria que muda de cenário no meio vira outro card), **(b)** ser
     **autossuficiente em contexto para a execução** — âncoras, números de aceite e contratos vêm no
     dossiê, e o executor não faz **nenhuma** busca transversal —, e **(c)** caber numa estimativa de
     **~50% de ocupação, com tolerância a 60%**. Card que não couber **se parte antes de ser
     publicado** (regra 6), nunca depois, e nunca durante a execução. **`DX-15`:** esse
     dimensionamento **não se declara no card** — o cabeçalho não carrega teto, a régua numérica é a
     tabela de classes de `GOVERNANCA.md` §3 e ela é interna a quem planeja. O que o card publica é
     o que tem consumidor: `<modelo>`, para instanciar o executor, e `<classe>`, como está.
- **Verificação:** `Grep pattern:"^### CTX-T[6-9]" path:docs/plans/P-0738-contexto-esgotado.md -n`
  devolve um cabeçalho por card, todos na gramática; cada causa da `## 9` aparece exatamente uma vez
  (como card ou como linha justificada); a `## 6` deste plano lista a ordem final; a linha
  `Próxima tarefa` do diário aponta para o primeiro card do Estágio C.
- **Pronto quando:** o Estágio C está escrito e fechado, e um executor consegue tomar o primeiro card
  sem precisar de nenhuma busca transversal à tarefa.

### Estágio C — cards autorados pela `CTX-T5` em 2026-08-23

*(faixa `CTX-T6..T9`, partida por letra onde o volume exigiu — regra 6 da charneira. **Cobertura das
9 causas da `## 9`:** `C3`→`T6a`, `C4`→`T6b`, `C6`+`C7`→`T7`, `C1`→`T8a`, `C2`→`T8b`, `C5`→`T8c`,
`C8`→`T9`. **`C9` não vira card porque sua rota ratificada é `manter`** (ganho 0: o `TK-23`(b)
fechou por medida na `CTX-T3`, sem instrumento novo) — é o único caso em que a regra 3 dispensa
card. Todo card nasce na gramática da `DX-15`, com o dimensionamento exercido aqui e **não**
publicado.)*

### CTX-T6a — O diário para de ser lido inteiro [Sonnet · classe redacao]
- **Objetivo:** tirar do kanban ativo tudo que é terminal, de modo que o pickup leia um arquivo
  pequeno em vez de reingerir a narrativa de sete planos fechados.
- **Causa atacada:** `C3` — diário relido dentro da própria janela. **Ganho esperado:** 7.800 (piso)
  a 15.252 tok por janela.
- **Arquivos-alvo:** `docs/DIARIO_DE_OBRAS.md`; `docs/DIARIO_HISTORICO.md`. Nenhum outro.
- **Números herdados, a reconferir na entrada (invariante 7):** diário em **341.964 chars / 2.935
  linhas**. Contagem de linha em PowerShell é `(Get-Content <f>).Count` — `Measure-Object -Line`
  ignora linha vazia e devolve número menor.
- **Contrato de corte** — itens 3-A, 3-B e 4 reescritos pela **`DX-16`** (decisão do dono,
  2026-08-23), que fechou a premissa falsa que bloqueou a primeira delegação:
  1. **Migra** para `docs/DIARIO_HISTORICO.md`, verbatim, toda seção `## <ID> — …` cujo `Status` na
     tabela do índice seja `done`, `superseded` ou `cancelled`, e toda **linha de tíquete `TK-*`**
     do índice nos mesmos três estados.
  2. **Ficam** no diário ativo: a Diretiva, a tabela do índice, `## P-0737` (`blocked`) e
     `## P-0738` (`in-progress`).
  3. **A coluna *Título* do índice passa a hook de ≤ 200 chars, sem exceção**, e o excedente tem
     **dois destinos, conforme o estado da linha**:
     - **3-A — linha terminal:** o texto longo vai, verbatim, para a seção correspondente do
       **histórico** (invariante 8 — registro escrito não se reescreve, muda de arquivo). A linha de
       **plano** terminal **permanece** no índice ativo como hook + âncora para o histórico; a linha
       de **tíquete** terminal sai do índice inteira, pelo item 1.
     - **3-B — linha viva** (`P-0737-AUT` e os tíquetes que sobrarem vivos após o item 4): o texto
       longo vai, verbatim, para uma **seção `## <ID> — <título>` no próprio diário ativo** — a mesma
       forma que os planos vivos já têm —, e a célula fica com hook + âncora para ela. Item vivo
       **não** vai para o histórico e **não** tem texto descartado.
  4. **Flip dos 11 tíquetes absorvidos (`DX-16` item 3).** Antes de aplicar o item 1, passar a
     `cancelled` as 11 linhas que a poda de 2026-08-22 declarou absorvidas pelo `P-0737` — `TK-04`,
     `TK-18`, `TK-26`, `TK-27`, `TK-30`, `TK-36`, `TK-37`, `TK-42`, `TK-44`, `TK-46`, `TK-50` —, na
     forma `cancelled *(absorvido pelo P-0737, fecha na AUT-T<n>)*`, **preservando verbatim o
     ponteiro `fecha na AUT-T<n>` que cada célula já carrega**. Com o flip elas viram terminais e
     migram pelo item 1. Acrescentar à seção `## P-0737` do diário ativo **um bullet datado
     (2026-08-23) listando os 11**, com o ponteiro de cada um, para que a matéria siga visível a
     partir do plano vivo que a carrega. Nenhum outro status muda: `TK-23`, `TK-32`, `TK-38` e
     `TK-48` continuam vivos exatamente como estão.
  5. **A coluna *Âncora*** passa a apontar para o plano, para a âncora do histórico (linha terminal)
     ou para a seção viva do próprio diário (linha viva).
- **Método obrigatório (invariante 2):** arquivo acima de 500 linhas e com célula de dezenas de
  milhares de chars **não se lê integralmente** — a fatia é feita por sonda programática no
  scratchpad (Python, corte por `^## `), e só o agregado (linhas movidas, linhas finais, chars
  finais) entra no contexto.
- **Verificação** (reescrita pela `DX-16` item 2 — o critério "≤ 450 linhas" **caiu**, porque texto
  que sai da tabela e fica no mesmo arquivo não reduz linha; o que se mede agora é o que o pickup
  lê): **nenhuma célula da coluna *Título* acima de 200 chars** (medido por sonda, sobre todas as
  linhas do índice); a **tabela do índice inteira ≤ 8.000 chars** (sonda: da linha `## Índice` até o
  próximo `^## `); `Grep pattern:"^## P-07" path:docs/DIARIO_DE_OBRAS.md -n` devolve **exatamente
  duas** seções (`P-0737` e `P-0738`); `Grep pattern:"\[drenado\]|cancelled|superseded" ` não é
  critério — o que fecha o item 4 é `Grep pattern:"^\| TK-(04|18|26|27|30|36|37|42|44|46|50) "
  path:docs/DIARIO_DE_OBRAS.md` **sem retorno** e as mesmas 11 linhas presentes em
  `docs/DIARIO_HISTORICO.md`; a **soma de chars dos dois arquivos não diminui** (nada foi
  descartado); `git status --short` acusa só os dois arquivos.
- **Pronto quando:** a tabela do índice cabe em 8.000 chars com toda célula *Título* ≤ 200,
  nenhum texto se perdeu, todo ponteiro do índice resolve (histórico, plano ou seção viva do
  próprio diário) e os 11 tíquetes absorvidos estão fechados com o ponteiro `AUT-T<n>` preservado.

### CTX-T6b — O inbox de planos sai do pickup [Sonnet · classe mecanica]
- **Objetivo:** parar de reingerir, a cada retomada, 291 linhas já drenadas para drenar zero.
- **Causa atacada:** `C4` — inbox lido integral e reingerido a cada corte. **Ganho esperado:**
  ~6.600 tok por janela.
- **Arquivos-alvo:** `docs/plans/_INBOX.md`; `docs/plans/_INBOX_HISTORICO.md` (novo);
  `.claude/skills/proximo-passo/SKILL.md:25`; `.claude/skills/diario-de-obras/SKILL.md:178,183,184,185,230`.
- **Números herdados, a reconferir:** `_INBOX.md` em **27.381 chars / 292 linhas**, das quais
  **291** já `[drenado]`.
- **Contrato:** `_INBOX.md` mantém o cabeçalho (inclusive a linha **Próximo id de plano**), as
  linhas **não drenadas** e uma linha de ponteiro para o histórico; as linhas `[drenado]` migram
  verbatim para `_INBOX_HISTORICO.md`, na ordem em que estão. O append-only continua valendo para o
  arquivo vivo; o histórico é destino de arquivamento e nunca de reescrita (invariante 8). As duas
  skills passam a citar o arquivo vivo como única fonte da drenagem, com uma linha dizendo onde o
  drenado foi parar. `.claude/skills/bootstrap-pantonic/SKILL.md` **não se toca**: projeto novo
  nasce só com o arquivo vivo.
- **Verificação:** `Grep pattern:"\[drenado\]" path:docs/plans/_INBOX.md` **sem retorno**;
  `(Get-Content docs/plans/_INBOX.md).Count` ≤ 40; a soma das linhas dos dois arquivos ≥ 292;
  `git status --short` acusa só os quatro arquivos.
- **Pronto quando:** o pickup drena lendo um arquivo de dezenas de linhas, e nenhuma linha
  histórica se perdeu.

### CTX-T7 — A fila corrente e o dossiê viram ponteiro [Sonnet · classe redacao]
- **Objetivo:** a próxima tarefa e o lugar exato do dossiê dela passam a ser lidos num offset fixo,
  em vez de reconstruídos por varredura de 39 matches históricos.
- **Causas atacadas:** `C6` (fila sem ponteiro estável) e `C7` (dossiê do plano reingerido inteiro).
  **Ganho esperado:** ~6.000–6.900 tok por janela (3.500 + 2.500–3.400).
- **Arquivos-alvo:** `docs/DIARIO_DE_OBRAS.md` (bloco de cabeçalho, logo abaixo da Diretiva);
  `.claude/skills/diario-de-obras/SKILL.md:49`; `.claude/skills/proximo-passo/SKILL.md:54`;
  `.claude/skills/scrum-master/SKILL.md:317`.
- **Contrato do bloco — uma linha, dentro das 15 primeiras do diário:**
  `**Fila corrente:** <PLANO> · <ID da tarefa> · dossiê <caminho do plano> \`### <ID>\` linhas <ini>-<fim> · fila <ID> → <ID> → …`
  É **projeção**, não fonte nova: a linha `Próxima tarefa` da seção do plano continua existindo,
  continua sendo escrita por quem fecha a tarefa e continua sendo a prosa do fechamento. O bloco é
  reescrito **pelo mesmo autor, no mesmo ato** — nenhum autor novo, nenhum ato novo.
- **Edições nas skills:** o passo 3 do `proximo-passo` troca o `Grep "Próxima tarefa da sprint"` por
  `Read docs/DIARIO_DE_OBRAS.md offset:1 limit:15`; `diario-de-obras:49` e `scrum-master:317`
  passam a mandar reescrever o bloco no mesmo ato em que já escrevem a próxima tarefa.
- **Fronteira `DX-9`, declarada antes do trabalho:** nenhum passo, gate, contador ou linha de
  roteamento nasce — muda **onde se lê** e **o que a linha carrega**. Se materializar isso exigir
  criar passo ou ramo, a tarefa **para de editar** e escreve uma linha em `## 9. Achados`,
  encaminhada à `AUT-T6`/`AUT-T9` do `P-0737`.
- **Verificação:** `Read docs/DIARIO_DE_OBRAS.md offset:1 limit:15` devolve o bloco preenchido;
  `Grep pattern:"Fila corrente" path:docs/DIARIO_DE_OBRAS.md` = 1 ocorrência;
  `Grep pattern:"Próxima tarefa da sprint" path:.claude/skills/proximo-passo/SKILL.md` sem retorno;
  as três skills citam o bloco.
- **Pronto quando:** uma retomada sabe qual é a tarefa e onde está o dossiê lendo 15 linhas.

### CTX-T8a — A varredura sai do papel caro [Sonnet · classe redacao]
- **Objetivo:** fechar a maior causa medida — instanciar um papel de 34.016 tok para fazer o que um
  papel de 8.340 tok já é encarregado de fazer.
- **Causa atacada:** `C1`. **Ganho esperado:** ~25.700 tok por varredura movida (executor 34.016
  tok, n=149, × `pantonic-scout` 8.340, n=10 = 4,1×).
- **Arquivos-alvo:** `.claude/skills/proximo-passo/SKILL.md`, passo 4 — blocos *"Levantamento de
  contexto antes do dossiê"* (linhas 71-77) e *"Fonte do contexto, em ordem de preferência"*
  (linhas 78-86). Nenhum outro arquivo.
- **Contrato:** o gatilho da delegação deixa de ser condicional e frouxo (*"se exigir ler mais de
  ~1-2 arquivos de código-fonte integrais"*) e passa a ser **regra de precedência**: toda coleta que
  não seja Read de âncora já conhecida (arquivo + range de linhas) ou Grep de string exata vai ao
  scout; leitura direta no contexto caro é **exceção declarada no ato**, com o motivo escrito, e não
  o default. Nenhum papel novo e nenhum passo novo: o passo 4 já prescreve a delegação e o agente
  já existe (`DX-6` — papel barato **já existente**).
- **Fronteira `DX-9`:** o texto muda o **critério de acionamento** de um ato que já é do passo 4;
  não cria passo, gate, contador nem linha de roteamento. Precisando criar, para e registra em
  `## 9. Achados`.
- **Verificação:** `Grep pattern:"1-2 arquivos" path:.claude/skills/proximo-passo/SKILL.md` **sem
  retorno**; o bloco reescrito nomeia `pantonic-scout`/`context-scout` e o critério de exceção;
  `git status --short` acusa só o arquivo-alvo.
- **Pronto quando:** ler no contexto caro passou a exigir justificativa escrita, e o default é
  delegar.

### CTX-T8b — A janela de orquestração amortiza o custo fixo [Sonnet · classe redacao]
- **Objetivo:** o custo fixo de protocolo passa a ser pago uma vez por **plano**, e não uma vez por
  tarefa atômica.
- **Causa atacada:** `C2`. **Ganho esperado:** ~8.400 tok da segunda tarefa da janela em diante
  (Δ = 32 tok entre os primeiros `usage` de J1 e J2 sobre 33.723 chars de texto de protocolo
  repagos idênticos).
- **Arquivos-alvo:** `GOVERNANCA.md` §4.3; `CHANGELOG.md` (uma linha sob `## [Não lançado]`,
  `DX-10`/`G-SURFACE`). Nenhum outro.
- **Contrato:** a §4.3 passa a dizer que a janela de orquestração **atravessa as tarefas atômicas do
  mesmo plano** e encerra na **troca de plano ou iniciativa** — que é o que
  `.claude/global/CLAUDE.md` Regra 2 já enuncia para quem orquestra —, nunca por tarefa concluída.
  **Preserva integralmente a `DX-14` item 3:** o encerramento planejado continua existindo como ato
  **entre tarefas** e da orquestração, e `.claude/tools/ocupacao.py` **não se toca** (nem `LIMIAR`,
  nem hook, nem mensagem).
- **Fronteira `DX-9`:** só texto de doutrina. Materializar a regra em passo, contador ou tabela de
  roteamento do `scrum-master` é matéria da `AUT-T6` — vira linha em `## 9. Achados`, não edição.
- **Verificação:** na §4.3 não sobra nenhuma linha que mande encerrar janela por tarefa concluída
  (`Grep pattern:"encerr" path:GOVERNANCA.md -n`, inspeção das linhas da §4.3);
  `Grep pattern:"ocupacao.py" path:GOVERNANCA.md -n` devolve o mesmo conjunto de linhas de antes;
  `git status --short` acusa só os dois arquivos.
- **Pronto quando:** a doutrina de capacidade não manda mais fechar janela entre tarefas do mesmo
  plano, e nada do instrumento mudou.

### CTX-T8c — A verificação de entrega sai do contexto caro [Sonnet · classe redacao]
- **Objetivo:** parar de **ler** o instrumento de verificação no papel mais caro, quando existe
  papel barato encarregado de **executá-lo**.
- **Causa atacada:** `C5`. **Ganho esperado:** ~3.700 tok por fechamento (J3 leu
  `.claude/tools/review_evidence.py`, 14.652 chars, em 3 chamadas; `pantonic-reviewer` instanciado
  n=1 contra n=149 do executor em toda a série).
- **Arquivos-alvo:** `.claude/agents/pantonic-reviewer.md:31`;
  `.claude/skills/scrum-master/SKILL.md:149`. **Nenhum `.py` é tocado** — logo a invariante 4
  (instrumento nasce com teste) não se aplica a esta tarefa.
- **Contrato:** os dois pontos passam a publicar a **linha de invocação completa** de
  `review_evidence.py` (comando e parâmetros, como já aparece em `scrum-master:149`), de modo que
  nenhum contexto precise abrir o fonte para saber chamá-lo, e a declarar que o instrumento se
  **executa** — abrir o `.py` para entender a chamada é sinal de documentação insuficiente, não
  caminho normal. Nenhuma responsabilidade muda: o ato já é do `pantonic-reviewer` pela matriz.
- **Fronteira `DX-9`:** texto e ponteiro; não cria passo nem altera quem verifica.
- **Verificação:** `Grep pattern:"review_evidence.py --plano"` devolve a **mesma** linha de comando
  nos dois arquivos; `git status --short` acusa só os dois.
- **Pronto quando:** a chamada está publicada onde é consumida, e ninguém precisa do fonte.

### CTX-T9 — A skill de orquestração encolhe sem perder ato [Sonnet · classe redacao]
- **Objetivo:** reduzir o maior artefato de kit do fluxo, que hoje é maior que a skill de pickup e
  que o `CLAUDE.md` global.
- **Causa atacada:** `C8`. **Ganho esperado:** ~2.800 tok por janela de orquestração.
- **Arquivos-alvo:** `.claude/skills/scrum-master/SKILL.md`; `CHANGELOG.md` (uma linha sob
  `## [Não lançado]`). Nenhum outro.
- **Números herdados, a reconferir:** 22.443 chars / 336 linhas, contra 15.070 chars da skill de
  pickup e 10.165 chars do `CLAUDE.md` global. **Alvo: ≤ 15.000 chars.**
- **Contrato:** condensa **prosa** — justificativa, racional e exemplo viram ponteiro à doutrina
  (`GOVERNANCA.md`) ou caem. **Não remove, não acrescenta e não reordena** passo, gate, contador ou
  linha de roteamento (`DX-9`): a sequência de passos e a tabela de roteamento ficam idênticas.
- **Inclui a 7ª âncora da `G-SURFACE` da `DX-13`**, hoje viva na **linha 119** (achado registrado
  pela `CTX-T1c` e não absorvido pela `CTX-T1d`): sai a justificativa que a decisão do dono tornou
  falsa — *"a localização não paga em tool uses do executor, e é dela que vem o excedente de teto"*
  —, do mesmo modo que saiu o gêmeo dela no `proximo-passo`. **Com isto o achado fecha e a `CTX-T1e`
  deixa de ser necessária**: a `G-SURFACE` daquela decisão vai a 7/7.
- **Verificação:** chars antes × depois medidos e registrados no fechamento, com o depois
  **≤ 15.000**; `Grep pattern:"excedente de teto" path:.claude/skills/scrum-master/SKILL.md` **sem
  retorno**; a lista de cabeçalhos (`Grep pattern:"^#{2,3} " -n`) tem os **mesmos títulos, na mesma
  ordem**, antes e depois; `git status --short` acusa só os dois arquivos.
- **Pronto quando:** a skill cabe em 15.000 chars com a mesma sequência de atos, e a sétima âncora
  morreu.

### CTX-T10 — Aferição: a janela depois, contra a janela antes [Sonnet · classe investigacao]
- **Objetivo:** provar por medida, e não por argumento, que a execução mudou o número — ou registrar
  em número que não mudou.
- **Arquivos-alvo:** reusa `sonda_janela.py` **no scratchpad**; edita `docs/CUSTO_DO_PICKUP.md`
  acrescentando `## 10 Aferição (<data>)` (**≤ 30 linhas**).
- **Método, fixo e independente de quais cards o Estágio C teve:** rodar a **mesma sonda** da
  `CTX-T2` sobre a primeira janela de orquestração posterior ao fechamento do último card do Estágio
  C, e publicar antes × depois para: ocupação do primeiro `usage` (`DX-5`), ocupação no primeiro
  despacho, e nº de janelas consumidas pela tarefa aferida.
- **Critério de aceitação da iniciativa** (fechado aqui, aferido aqui): **(a)** a ocupação do
  primeiro `usage` de uma janela de orquestração cabe no alvo vigente da `## 9` (default `DX-11`:
  10.000 tokens); **(b)** uma tarefa atômica se abre, delega, fecha e registra telemetria numa
  **única** janela. Falhando (a) ou (b), a tarefa publica o número e o gap e **não corrige**: o gap
  vira linha em `## 9. Achados` e tíquete.
- **Verificação:** a `## 10` traz as três comparações com número medido dos dois lados e o veredito
  de (a) e (b); `git status --short` acusa só `docs/CUSTO_DO_PICKUP.md`.
- **Pronto quando:** o antes × depois está publicado e o critério de aceitação tem veredito numérico.

### CTX-T11 — Revisão do `README.md` da raiz [Opus · classe redacao]
- **Objetivo:** fechar a sprint pelo contrato entre o framework e o cliente (`G-README`, dever 2). O
  guarda executável é instrumento **desta atividade**; o **único teste de sentido é o veredito do
  dono**.
- **Arquivos-alvo:** `README.md` (raiz) — o que esta rodada tenha dessincronizado; `docs/DOC_MAP.md`
  só se a entrada do relatório divergir do publicado.
- **Roteiro:**
  1. Rodar `pwsh .claude/checks/check-readme.ps1` e resolver toda falha estrutural.
  2. Ler o `README.md` procurando o que o guarda **não** vê: prosa que descreva o estado anterior às
     **duas normas** da `CTX-T1`/`CTX-T1b`/`CTX-T1c` — em especial texto que ainda trate capacidade
     como regra de execução ou teto como coisa do executor —, **cabeçalho de tarefa citado na
     gramática revogada** (`· teto <N>`, `DX-15`; a vigente é `[<modelo> · classe <classe>]`),
     número por extenso divergente de tabela — **três âncoras já localizadas nesta rodada**:
     `polui o contexto e obriga parada imediata` (espelho da Regra 2), `com teto por ramo no dossiê`
     (espelho da tabela de classes, célula que a `CTX-T1` corrige) e o item 7 da tabela de guardrails
     (`Disciplina de contexto`) —, seção que prometa
     artefato inexistente, e a menção (ou a falta dela) às seções novas de
     `docs/CUSTO_DO_PICKUP.md` onde o espelho enumera os docs de `docs/`.
  3. Aplicar a `.claude/skills/redacao-doc/SKILL.md` ao que for reescrito.
  4. Apresentar ao dono, em **uma** mensagem, o que mudou no espelho nesta sprint e **pedir o
     veredito**. Aprovado, a sprint fecha; reprovado, o veredito vira insumo da rodada seguinte e a
     tarefa devolve ao planejamento.
- **Proibido:** fechar a tarefa sem o veredito do dono; tratar o exit 0 do guarda como aceite.
- **Verificação:** `pwsh .claude/checks/check-readme.ps1` em exit 0 **e** veredito do dono registrado.
- **Pronto quando:** o dono aceita o espelho.

## 6. Ordem de execução

Linear, sem ramo:
`CTX-T1 → CTX-T1b → CTX-T1c → CTX-T1d → CTX-T2 → CTX-T3 → CTX-T4 → CTX-T5 →
CTX-T6a → CTX-T6b → CTX-T7 → CTX-T8a → CTX-T8b → CTX-T8c → CTX-T9 → CTX-T10 → CTX-T11`.

**Ordem do Estágio C, fixada pela charneira (regra 7 — maior ganho pela menor grandeza primeiro):**
as três de grandeza **mecânica** abrem, porque entregam número já na primeira janela seguinte e se
verificam por contagem (`T6a` 7.800–15.252 · `T6b` ~6.600 · `T7` ~6.000–6.900); as de grandeza
**comportamental** vêm depois, por ganho (`T8a` ~25.700 · `T8b` ~8.400 · `T8c` ~3.700); a
condensação do artefato de orquestração (`T9`, ~2.800) fecha o estágio, porque é a única que compete
por arquivo com o `P-0737` quando ele destravar e por isso convém ser a última escrita.

O corte é por valor validável cedo:

1. **`CTX-T1`** entrega no primeiro contexto as duas normas que o dono mandou publicar (`DX-13`) —
   verificáveis por um Grep, e válidas para a própria execução deste plano. **`CTX-T1b`** e
   **`CTX-T1c`** fecham a `G-SURFACE` no mesmo trecho contíguo: papéis primeiro (onde a norma muda
   responsabilidade), fluxo depois (onde ela só apaga texto falso). **`CTX-T1d`** fecha o mesmo
   trecho nos **instrumentos**, e vem por último das quatro porque só faz sentido depois que a
   gramática está escrita na doutrina que a `CTX-T1c` edita. As quatro correm antes da medida porque
   são **transcrição de decisão do dono**, não derivação de causa medida (`DX-2`, com o carve-out da
   `DX-14` item 6, estendido pela `DX-15` ao parser). **Janela conhecida e inofensiva:** entre esta
   publicação (cabeçalhos já migrados) e a `CTX-T1d`, `rdo.py`/`review_evidence.py` não parseiam os
   cabeçalhos deste plano — e já não parseavam antes, por causa do identificador prefixado (achado
   da `## 9`); nenhuma tarefa deste plano depende deles para fechar.
2. **`CTX-T2`** devolve, sozinha, o número que a diretiva pede: quanto custa abrir uma janela antes
   de qualquer ato.
3. **`CTX-T3`** diz se o caso é padrão e fecha `TK-23`/`TK-32` em número.
4. **`CTX-T4`** é o material de decisão, num round-trip único.
5. **`CTX-T5`** converte decisão em cards fechados; daí em diante o plano é execução.
6. **`CTX-T10`** prova o resultado; **`CTX-T11`** é o aceite da sprint.

**Dependências duras:** a `CTX-T3` reusa a sonda da `CTX-T2`; a `CTX-T4` consome `## 7` e `## 8`; a
`CTX-T5` consome a `## 9`; a `CTX-T10` consome a `## 7` como linha de base. O relatório
`docs/CUSTO_DO_PICKUP.md` é o **portador durável entre tarefas** (`DC-5`): trocar de contexto entre
tarefas não custa remedição, e nenhuma tarefa depende do scratchpad de outra.

**Denominador do plano, fechado pela charneira em 2026-08-23:** **17 tarefas** — as 10 publicadas na
autoria (`CTX-T1`, `CTX-T1b`, `CTX-T1c`, `CTX-T1d`, `CTX-T2`..`CTX-T5`, `CTX-T10`, `CTX-T11`) mais
os **7 cards** do Estágio C (`T6a`, `T6b`, `T7`, `T8a`, `T8b`, `T8c`, `T9`). A previsão de `n/14`
supunha quatro cards; oito causas com rota diferente de `manter` couberam em quatro temas, e a
partição por letra (regra 6) manteve cada card numa matéria só, dimensionado para contexto coeso e
autossuficiente. Nenhum identificador fora da faixa reservada.

## 7. Fora de escopo (explícito)

- **O piloto medido do loop** — recomendação (a) do `P-0737` §8, que continua reservada àquele plano.
- **Responsabilidade, passo, gate, contador e tabela de roteamento do loop** (`DX-9`) — matéria do
  `P-0737`, hoje `blocked`.
- **A rota do `proximo-passo`** — questão **abolida** por decisão do dono (custo transitório de skill
  marcada para descontinuação); a descontinuação em si é da `AUT-T6`. **Ressalva (`DX-14`, item 6):**
  a `CTX-T1c` toca essa skill **apenas** nas âncoras que a `DX-13` tornou falsas, por deleção ou
  ponteiro — retirar texto falso não é escolher rota, e a rota segue fora.
- **Fluxo novo por causa do adendo** — valor de status, razão tipada, ramo ou linha de roteamento que
  a materialização da norma (1) venha a exigir no `scrum-master`: é `DX-9`, matéria do `P-0737`, e
  sai daqui como linha em `## 9. Achados`.
- **Retificar a série histórica de `docs/telemetria.tsv`** (`DX-12`).
- **Derivados** (`DA-3`: hub primeiro, medir, depois propagar), `.claude/sync-kit.ps1`, bump e tag
  (`DE-7`).
- **Reabrir decisão ratificada** — `DC-1`..`DC-9` do `P-0736` e `DU-1`..`DU-14` do `P-0737` são
  insumo, não matéria.

## 8. Riscos

| Risco | Sinal | Resposta |
|---|---|---|
| Os transcripts das três janelas não serem localizáveis | a seleção fechada da `CTX-T2` devolver menos de três | mede as que existirem e registra `ausente`; a decomposição fixo × variável se prova com uma janela — a rota não depende do `n` |
| A forense contradizer a soma por arquivo do `P-0736` | divergência entre `## 7` e `## 5` | manda a forense (`DX-7`), e a divergência entra como linha de achado reconciliada, nunca como refutação silenciosa (`G-PREMISE`) |
| O dono trocar a rota na `CTX-T4` | veredito diferente do recomendado | **nada a invalidar por desenho**: nenhum card do Estágio C existe antes da `CTX-T5` (`DX-1`) |
| O Estágio C crescer além da faixa reservada | a `CTX-T5` precisar de mais de quatro cards | partição por letra (`CTX-T6a`/`T6b`), precedente medido (`RPC-T7`, `AUT-T5`); nunca identificador fora da faixa |
| Colisão de arquivo com o `P-0737` ao destravar | um card do Estágio C tocar `scrum-master/SKILL.md` onde a `AUT-T6` reescreverá | `DX-9`: só texto, nunca fluxo; o `P-0737` está paralisado, então a herança é sequencial, não concorrente |
| A reconciliação da `G-SURFACE` virar reescrita de fluxo | a `CTX-T1c` precisar **criar** passo, ramo, contador ou linha de roteamento para materializar a norma (1) | a fronteira está declarada antes do trabalho (`DX-14`, item 6): a tarefa **para de editar** e escreve uma linha em `## 9. Achados`, encaminhada à `AUT-T6`/`AUT-T9`; nenhuma decisão de fluxo se toma aqui |
| Sobrar superfície não varrida que ainda orce teto do executor | Grep de fechamento devolver texto novo fora dos 20 pontos varridos | achado com rota: linha em `## 9`, e a `CTX-T11` (README) é a segunda rede — o guarda estrutural mais a leitura de sentido do dono |
| Cabeçalho legado deixar de ser parseável quando o campo `teto` cair (`DX-15`) | `rdo.py`/`review_evidence.py` falharem sobre plano fechado ou sobre o `P-0737` | o segmento ` · teto <N>` fica **opcional e descartado** na regex (`CTX-T1d`), com teste dedicado; nenhum plano fechado se reescreve (invariante 8), e o `P-0737` `blocked` não se toca (`DX-9`) |
| A `Q1` (campo `classe`) contaminar tarefa publicada | um dossiê citar `classe` como coisa a decidir, ou a `CTX-T1d` mexer em `_CLASSE_ALIASES` | `classe` está **congelada como está** enquanto a questão correr, e a proibição é literal na `CTX-T1d`; qualquer desfecho da `Q1` é card próprio, autorado depois — o plano segue fechado pelo `G-PLANREADY` item 5 |
| O plano reproduzir o volume que mede | seção de relatório ou card crescendo em prosa | teto por seção (`## 7` ≤ 60, `## 8` ≤ 50, `## 9` ≤ 40, `## 10` ≤ 30), teto de 320 linhas do relatório (`DX-3`) e vocabulário fechado (`DX-6`) |

## 9. Achados da execução

*(vazio na publicação; cada tarefa apende aqui o que achar fora do próprio escopo, uma linha com
rota)*

- **2026-08-22, planejamento (`DX-15`) — `rdo.py` não enxerga identificador prefixado.**
  `_ID_HEADER_RE` (`^### (T[0-9]+[a-z]?)`) exige que o id comece em `T`, então **nenhuma** tarefa
  `CTX-T*` (deste plano) ou `AUT-T*` (`P-0737`) é localizável por `rdo.py`/`review_evidence.py` — e
  `--esquema-legado` não salva, porque a falha é na busca do cabeçalho, antes do colchete. Defeito
  **pré-existente**, não causado pela `DX-15`, nunca exercitado (só há RDO de `P-0734-T11` e
  `P-0734-T13`, ambos sem prefixo). **Rota:** não se corrige aqui (`DX-2`: correção antes da medida,
  e não é reconciliação de superfície); é insumo da `AUT-T4` do `P-0737`, que é a dona do `rdo.py`.
- **2026-08-22, `CTX-T1c` — sétima ocorrência da justificativa falsa no `scrum-master`, fora do
  conjunto fechado de âncoras.** `.claude/skills/scrum-master/SKILL.md:119` (passo 4, despacho)
  repete o gêmeo do item 3 do gate de delegação: *"a localização não paga em tool uses do executor,
  e é dela que vem o excedente de teto"*. A `CTX-T1c` corrigiu o gêmeo em `proximo-passo` (virou
  autossuficiência de contexto) e **não editou este**, porque o dossiê fixou **seis** âncoras neste
  arquivo e exceder enumeração fechada é replanejar. Deleção/reescrita textual pura, sem fluxo novo.
  **Rota:** emenda de uma linha, pelo planejador, na `CTX-T1d` ou numa `CTX-T1e`.
- **2026-08-22, `CTX-T1c` — mensagem de runtime do proxy de ocupação ficou mais imperativa que o
  estatuto novo.** `.claude/tools/ocupacao.py:57` (`MENSAGEM_AVISO`) manda *"Encerre a tarefa
  corrente… e pare"*, enquanto a `CTX-T1c` reclassificou o instrumento como **aviso informativo à
  orquestração entre tarefas**. Não foi editada por vedação explícita do dossiê (é comportamento de
  `.py`, e o hook/`LIMIAR` não mudam); o filtro por `agent_type` já a restringe à sessão de
  orquestração, então a falsidade é de tom, não de destinatário. **Rota:** decidir com a `AUT-T6`
  do `P-0737` (dona do texto que o loop consome), junto do estatuto do aviso de capacidade.
- **2026-08-23, `CTX-T1d` (gate de delegação) — critério de aceitação impossível no dossiê
  publicado.** A linha *Verificação* do `### CTX-T1d` exigia `Grep pattern:"TETO"
  path:.claude/tools/` **sem retorno**, o que contradiz o **item 4 do mesmo dossiê**, que manda
  preservar `_CLASSE_TETO_DEFAULT` — 5 ocorrências medidas no ato (`rdo.py:50,212,216,248,254`).
  Como publicado, o critério nunca fecha. O corpo do dossiê prevaleceu e o gate transcreveu o
  critério corrigido (`{{TETO}}` e `"TETO"`, que fecha sem retorno); a tarefa executou e verificou
  por ele. **Classe:** critério derivado de uma abreviação que não acompanhou a exceção declarada no
  próprio dossiê — mesma família do que o `G-PLANREADY` item 5 evita, mas em critério de aceitação,
  não em escopo. **Rota:** nada a corrigir no código; é insumo para a autoria dos dossiês restantes
  (`CTX-T2`..`CTX-T11`) — critério de grep negativo precisa citar a string exata, nunca o radical.
- **2026-08-23, `CTX-T1d` — a emenda de `scrum-master:119` não foi absorvida.** O achado da
  `CTX-T1c` (2ª linha desta seção) nomeou como rota *"emenda de uma linha, pelo planejador, na
  `CTX-T1d` ou numa `CTX-T1e`"*. A `CTX-T1d` **fechou sem ela** — o dossiê publicado não lista
  `.claude/skills/scrum-master/SKILL.md` em *Arquivos-alvo*, e o executor não podia acrescentá-lo
  (`G-SCOPE`). A sétima ocorrência da justificativa falsa **segue viva** em
  `.claude/skills/scrum-master/SKILL.md:119`, e a rota agora depende de uma `CTX-T1e` que **não
  existe**. **Rota:** o planejador decide entre autorar a `CTX-T1e` (emenda de uma linha) ou
  reencaminhar o achado; enquanto não decidir, a `G-SURFACE` da `DX-13` está fechada em 6/7 âncoras.

- **2026-08-23, `CTX-T4` — o custo de abrir um papel é dominado pela superfície de ferramentas
  registrada, não pelo prompt.** Medido: `.claude/agents/pantonic-executor.md` tem **4.685 chars
  (~1.171 tok)** e abrir o papel custa **34.016 tok** de mediana (n=149) — o arquivo é **3,4%** do
  custo; `pantonic-scout`, com três ferramentas, abre em 8.340 tok (n=10). A diferença entre os
  papéis não está no texto que se pode condensar. **Rota:** não vira linha da `## 9` do relatório —
  atacar a superfície de ferramenta de um papel altera **responsabilidade**, que a `DX-9` põe fora
  deste plano. Insumo obrigatório da `AUT-T6`/`AUT-T9` do `P-0737`. Ratificado pelo dono em
  2026-08-23, no round-trip da `CTX-T4`.
- **2026-08-24, `CTX-T10` — a rodada Estágio C não reduziu `DX-5`; ele subiu.** Medido
  (`docs/CUSTO_DO_PICKUP.md` `## 10`): 1º `usage` da primeira janela pós-`CTX-T9` = **46.071 tok**,
  contra 34.260/34.292/45.872 antes (`## 9`) — +34,4% vs. mediana, ainda +0,4% acima do pior caso
  pré-rodada. Critério (a) da iniciativa **reprovado**. `DX-2` proíbe corrigir aqui. **Rota:** a
  causa não está isolada por esta medida (fixo × variável de `## 7` só decompõe o **antes**; nenhum
  card do Estágio C tocou o que compõe o próprio 1º `usage`, ex.: nº/tamanho de ferramentas
  registradas, `CTX-T4` já achou que isso domina o custo de abrir um papel). Abre-se tíquete de
  investigação; decisão do dono é pré-requisito antes de qualquer nova rodada de rotas.
- **2026-08-24, `CTX-T11` — `GOVERNANCA.md` §4.3 ainda atribui o checkpoint ao executor, contra a
  própria §4.3 e contra a skill.** O bullet *"Contexto acabando sem plano de parada"* (§4.3, linhas
  416-420) diz que **o executor** grava o checkpoint quando conclui que o contexto acaba antes da
  tarefa, e que *"o mesmo checkpoint responde ao sinal de poluição"*. As duas afirmações são
  contraditas por três superfícies vivas: o bullet **Capacidade** da mesma §4.3 (*"nunca interrompe
  tarefa em curso; quem executa não para, não parte a entrega"*), o parágrafo seguinte (encerramento
  é *"ato da orquestração, entre tarefas — nunca dentro de uma tarefa, nunca do executor"*) e o bloco
  **"Dois casos que NÃO são checkpoint"** de `.claude/skills/handover/SKILL.md`, que nomeia
  exatamente esses dois casos como **não**-checkpoint. É resíduo que a `CTX-T1` não varreu: editou os
  bullets Coesão/Capacidade de §4.3 e deixou o bullet de baixo, na mesma seção.
  **Rota:** correção de superfície de doutrina, fora dos arquivos-alvo da `CTX-T11` (`README.md` e
  `docs/DOC_MAP.md`) — tíquete próprio de redação, a autorar. O `README.md` §9 **não** ficou exposto:
  sua *Fonte da verdade* declarada é `.claude/skills/handover/SKILL.md`, e foi a essa fonte que o
  espelho se alinhou nesta tarefa.

## Questões ao dono

### `Q1` — que informação o campo `classe` carrega, agora que o teto caiu (aberta em 2026-08-22)

**Origem:** o dono, ao decidir a `DX-15`, declarou **não saber** o que o campo `classe` carrega.
Não é escolha feita, é pergunta aberta — e por isso o planejamento **não decidiu**: enquanto ela
correr, `classe` **fica no cabeçalho exatamente como está**, e nenhuma tarefa publicada depende do
desfecho (`G-PLANREADY` item 5 segue satisfeito).

**Levantamento medido (Grep, 2026-08-22), que é o insumo da decisão:**

| Onde | O que faz com `classe` hoje |
|---|---|
| `.claude/tools/rdo.py` | parseia (regex do cabeçalho), normaliza por `_CLASSE_ALIASES` (aceita as grafias históricas), recusa classe fora do conjunto, e **usava** o slug só para achar o teto default — validação que a `DX-15` derruba. Sobrevive como **rótulo transcrito** para o RDO (`"CLASSE": dossie.classe`) |
| `.claude/skills/scrum-master/SKILL.md` | **só** para localizar o teto — linhas 256 (*"os `tools` gastos contra o teto da classe declarada"*) e 327 (*"o teto de tool uses da tarefa é o da classe registrada"*). Quem **roteia o executor é o campo `Modelo`** (passo 4, `model:` da chamada), nunca a classe |
| `.claude/tools/rdo_template.md` / `docs/telemetria.tsv` | rótulo descritivo: aparece no RDO e é o eixo de agregação da série (é por classe que o `TK-32` conta "quantas tarefas cruzaram o teto") |
| `GOVERNANCA.md` §3 | a tabela de classes é a **régua de dimensionamento do planejador** — a classe nomeia qual linha dela foi usada |

**Confirma-se o que o dono suspeitou:** caindo o teto, `classe` **perde o único consumidor
funcional** e sobra como rótulo descritivo. Três destinos, com o custo de cada um:

1. **Cair junto com o teto** — cabeçalho vira `[<modelo>]`. *Custo:* uma segunda passagem pela mesma
   superfície da `CTX-T1d` (regex, `DossieTarefa`, aliases, template, dois arquivos de teste, as
   duas linhas de gramática do `scrum-master`); e perde-se o **eixo de agregação** da série — a
   `CTX-T3` e o `TK-32` medem *por classe*, e sem ele a pergunta "que tipo de tarefa estoura" deixa
   de ter resposta no dado. *Ganho:* o cabeçalho fica com um campo só, e todo campo publicado passa
   a ter consumidor de execução.
2. **Sobreviver como rótulo descritivo, com consumidor declarado** — permanece no cabeçalho, e a
   doutrina passa a **nomear** para que serve: (i) eixo de agregação de `docs/telemetria.tsv` e do
   RDO, (ii) marcador de qual linha da régua de `GOVERNANCA.md` §3 o planejador usou ao dimensionar,
   auditável depois contra o consumo medido. *Custo:* uma linha de doutrina (sem ela o campo volta a
   parecer órfão na próxima auditoria) e zero migração. **É a recomendação do planejamento**, porque
   preserva a série medida que este plano inteiro depende — mas a escolha é do dono.
3. **Sobreviver com função nova** — por exemplo, passar a governar perfil/agente ou seleção de
   rubrica. *Custo:* é **fluxo novo**, `DX-9` — matéria do `P-0737`, hoje `blocked` —, exige decisão
   do dono **antes** de qualquer card e não cabe neste plano.

**Se a resposta for (1) ou (3):** vira card próprio, autorado depois pelo planejamento; nada do que
está publicado hoje precisa ser desfeito, porque a `CTX-T1d` congelou `classe` no estado atual.

### Rodada anterior (2026-08-22, `DX-13`/`DX-14`) — nenhuma questão

**Nenhuma.** A rodada de revisão de **2026-08-22** (adendo do dono, `DX-13`) não abriu questão: o
adendo é decisão **ratificada** e não volta para reconfirmação, e as duas consequências que podiam
ser estratégicas foram resolvidas **dentro** da autonomia técnica e tática do planejamento, com o
racional escrito na `DX-14` — **(a)** o instrumento `.claude/tools/ocupacao.py` **se mantém como
está**, reclassificado como aviso informativo, porque mexer no `LIMIAR` seria inventar número novo,
que a própria `DX-13` proíbe; **(b)** a materialização do retorno de poluição no **roteamento** do
loop **não se decide aqui** — é `DX-9`, matéria do `P-0737`, e sai como achado com destino nomeado.
Toda decisão de arquitetura ou de requisito que este plano precisa está concentrada na
**`CTX-T4`**, que é tarefa nomeada, com entregável próprio (a `## 9` do relatório) e round-trip
único — e nenhuma tarefa publicada assume o resultado dela (`DX-1`, `DX-2`). As demais escolhas foram
fechadas por derivação do já medido (`P-0736`) e do já ratificado (`DE-7`, `DA-3`, `DU-1`..`DU-14`),
e estão numeradas em `DX-1`..`DX-14` com o racional.
