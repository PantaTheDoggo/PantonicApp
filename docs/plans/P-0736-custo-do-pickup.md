# P-0736 — Custo do pickup: medir antes de corrigir

**Data:** 2026-08-21 · **Origem:** diretiva do dono, prioridade zero (2026-08-21) · **Autoria:**
2026-08-22 · **Status:** `done` — fechado como **lições aprendidas** em 2026-08-22 (decisão do dono
no ato da `T4`): `T1`..`T3` entregues, `T4`/`T5` sem objeto, nenhuma rota implementada; o `P-0737`
previsto no §1 é substituído pela rodada de consolidação da `EXECUCAO-AUTONOMA` ·
**Prefixo das tarefas no diário:** `CPK-T<n>` · **Checagem de
versão do kit:** modo hub — **congelada em `0.0.0`** (`DE-7`), comparação local × remoto suspensa,
nada a comparar.

## 0. O problema

Cinco pickups consecutivos (2026-08-20, 2026-08-21 ×3, 2026-08-22); os quatro primeiros
**encerraram por capacidade sem executar tarefa nenhuma** — a janela acabou antes da primeira
delegação. Diretiva do dono: *"esse panorama de esgotar a janela logo de início é uma distorção que
inviabiliza o framework (…) no estado atual, o framework caminha para a inviabilidade dessa forma"*.
Nada mais é delegado até que o custo de **saber onde o trabalho parou** volte a caber numa janela
saudável.

Medidas já colhidas no pickup de 2026-08-22, ancoragem inicial (a `T1` amplia e ranqueia):

| fonte | medida |
|---|---|
| `docs/DIARIO_DE_OBRAS.md` | 2.471 linhas / **307.541 chars** (~77k tokens) — Read integral estoura o teto de 25k tokens da ferramenta e **falha** |
| índice do diário, linha 35 (célula do `P-0734`) | **10.528 chars numa única linha**; um Read de 18 linhas (20-37) devolveu ~14k chars |
| `docs/plans/_INBOX.md` | 231 linhas / 22.213 chars — lido integral para drenar **1** linha |
| `docs/DIARIO_HISTORICO.md` | 280.961 chars |
| `.claude/skills/proximo-passo/SKILL.md` | 15.613 chars |
| `.claude/skills/diario-de-obras/SKILL.md` | 16.767 chars |

## 1. Fronteira de escopo (regra escalonada, nível 2)

O plano se autora sob o **nível 2** da regra escalonada de 2026-08-21: *existe decisão, faltam
elementos para tomá-la — o plano se reescopa, começa e termina **antes** da decisão, as entregas são
avaliadas, e só então se decide*.

**Este plano entrega medida + rotas candidatas. Nenhuma tarefa dele corrige o fluxo de pickup.**
Fora de escopo, explicitamente:

- editar `.claude/skills/proximo-passo/`, `.claude/skills/diario-de-obras/` ou qualquer outro
  artefato do kit;
- condensar, particionar, reordenar ou mover conteúdo de `docs/DIARIO_DE_OBRAS.md`,
  `docs/DIARIO_HISTORICO.md` ou `docs/plans/_INBOX.md`;
- criar ferramenta versionada de geração/consulta (a sonda desta rodada é descartável);
- corrigir a afirmação hoje falsa de `docs/DOC_MAP.md` de que `docs/DIARIO_DE_OBRAS.md` fica abaixo
  de 500 linhas — é **achado** da `T1`, registrado no relatório, e rota candidata, não conserto;
- tocar qualquer derivado (`DA-3`: hub primeiro, medir, depois propagar);
- autorar o `P-0737`.

A escolha da rota e a implementação nascem no **`P-0737`**, plano posterior, aberto em contexto novo
depois da avaliação do dono. **Qualquer que seja o veredito da `T4`, este plano fecha na `T5`:
nenhuma tarefa daqui ramifica pelo conteúdo do veredito.**

## 2. Decisões de planejamento (fechadas no ato)

Zero questão em aberto, zero bloco a preencher, zero ramo condicional, zero decisão owner-gated
pendente dentro do plano — a avaliação da `DC-9` é o **fim** do plano, não um ponto de parada dele.

| Id | Decisão | Conteúdo |
|---|---|---|
| **`DC-1`** | O plano termina antes da decisão | Medida e rotas candidatas são o entregável; correção é `P-0737`. Toda tarefa cuja verificação incluir `git status --short` prova o cumprimento: só o arquivo do relatório (e, na `T3`, o `docs/DOC_MAP.md`) aparece modificado |
| **`DC-2`** | Definição operacional de **pickup típico** | Sessão nova de orquestração no `PantonicApp`, do turno zero até ter **o dossiê da próxima tarefa em mãos**, sem executá-la, com o repositório no `HEAD` de 2026-08-22. Compreende exatamente: (a) custo fixo de entrada (doutrina global, índice de memória e memórias indexadas, definição do agente, skill do fluxo); (b) drenagem dos **dois** inboxes — `docs/plans/_INBOX.md` e o inbox de memórias do projeto; (c) leitura da diretiva de prioridade no topo do diário; (d) apuração da fila corrente (qual é a próxima tarefa e seu status); (e) leitura do dossiê dessa tarefa no plano corrente. Nada além disso conta |
| **`DC-3`** | Unidade e fator | **Chars** é a medida primária (`(Get-Content -Raw <f>).Length`); **tokens estimados = chars ÷ 4**, fator único declarado em toda tabela e **nunca reportado sem os chars ao lado**. O fator reproduz a ancoragem já colhida (307.541 ÷ 4 ≈ 77k). Duas colunas distintas e obrigatórias: **chars do arquivo** × **chars ingeridos** no pickup típico — passo de leitura parcial conta só a fatia |
| **`DC-4`** | Método de sondagem (tarefa-investigação, item 6 do gate de delegação) | Sonda **programática** por script Python descartável escrito no scratchpad da sessão (`sonda_pickup.py`), que abre os arquivos, calcula as métricas e emite **só um agregado**. Proibido, para artefato > 500 linhas ou com linha de mais de 2.000 chars: `Read` integral (estoura) e `Grep -output_mode content` (colapsa o contexto ao devolver a célula inteira). O agregado tem **≤ 120 linhas** e todo trecho textual é truncado em **60 chars**. O script não é versionado: ferramenta versionada é rota candidata, não entregável desta rodada |
| **`DC-5`** | Residência do relatório | **`docs/CUSTO_DO_PICKUP.md`**, teto de **200 linhas**. Em `docs/` porque é medida durável do framework, consumida pelo `P-0737` e por auditoria futura; **não** no plano (plano é decisão, e o plano é descartável quando a iniciativa fecha) e **não** no diário (que é justamente o artefato medido — engordá-lo com a medida do próprio inchaço seria caricato). O arquivo é o **portador durável entre as tarefas**: cada tarefa **acrescenta** sua seção, nenhuma reescreve a anterior, e o scratchpad não precisa sobreviver de um contexto a outro |
| **`DC-6`** | Formato do relatório | Sete seções fixas, com teto de linhas: `## 1 Pickup típico medido` (definição da `DC-2` + `HEAD` medido) e `## 2 Orçamento por fonte` — **≤ 80 linhas**, `T1`; `## 3 Orçamento por passo do roteiro` e `## 4 Hipóteses H1..H5` — **≤ 50 linhas**, `T2`; `## 5 Rota candidata por fonte` e `## 6 Orçamento-alvo proposto` — **≤ 50 linhas**, `T3`; `## 7 Veredito do dono` — **≤ 20 linhas**, `T4`. Sem narrativa de proveniência, sem histórico da decisão: tabela e número |
| **`DC-7`** | Taxonomia fechada das rotas | Conjunto fechado de cinco valores, um por fonte: `condensar`, `ponteiro`, `gerar-por-instrumento`, `mover-ao-historico`, `manter`. A `T3` escolhe dentro do conjunto e nunca inventa vocabulário; o `P-0737` decide sobre conjunto fechado |
| **`DC-8`** | Ranking e forma do alvo | Ranking **decrescente por chars ingeridos** no pickup típico (medida bruta; ordenar por "economia potencial" já seria juízo de rota). Empate desfaz pela ordem de leitura. O **orçamento-alvo** da `T3` tem forma fixa: fração da janela nominal de 200k tokens, coerente com o teto de trabalho de ~50% da janela (Regra 2), escrito em **chars e tokens**, com a folga de execução declarada em número. A `T3` **sempre** escreve um número |
| **`DC-9`** | Como a avaliação do dono é apresentada | Na `T4`, **uma única mensagem** com quatro itens: (i) o número único do orçamento medido do pickup típico; (ii) a tabela das fontes ranqueadas com % do total e a rota candidata de cada uma; (iii) o orçamento-alvo proposto; (iv) três perguntas fechadas — *ratifica o alvo?*, *aceita a rota candidata de cada fonte (ou troca por outra do conjunto fechado)?*, *autoriza abrir o `P-0737`?*. As respostas viram a `## 7` do relatório, datada. Nenhuma correção começa nessa execução |

## 3. Hipóteses, instrumento e número que decide

Nenhuma é premissa: hipótese refutada entra no relatório como refutada e **não gera rota**.

| Id | Hipótese | Instrumento | Número que confirma ou refuta |
|---|---|---|---|
| **`H1`** | A coluna *Título* do índice do diário acumula a narrativa inteira do plano; a célula do `P-0734` é lida em todo pickup só para extrair *status* e *âncora* | sonda: top 10 linhas por chars no diário | chars da maior linha e chars ingeridos por um Read da faixa do índice |
| **`H2`** | `docs/plans/_INBOX.md` é append-only e se lê integral para drenar zero ou uma linha | sonda: total de linhas × linhas sem marca `[drenado]` | chars do arquivo ÷ chars das linhas drenáveis |
| **`H3`** | A fila corrente não tem ponteiro estável e se reconstrói varrendo `Próxima tarefa`, devolvendo ~200 matches históricos dos quais um é o vigente | sonda: contagem de linhas casando `Próxima tarefa` e soma dos chars delas | nº de matches e chars devolvidos por uma varredura equivalente |
| **`H4`** | O custo fixo de entrada (skill do fluxo, doutrina global, índice de memória e memórias) é consumido antes de qualquer leitura de projeto | sonda sobre a lista fixa + roteiro da skill (`T2`) | chars do bloco fixo e sua fração do orçamento total |
| **`H5`** | Seção de plano terminal (`P-0735`, 13/13 `done`) permanece no diário ativo em vez de condensada no histórico | sonda: por seção `^## ` do diário, chars + contagem de cada status do vocabulário | chars das seções sem nenhum status vivo |

## 4. Invariantes de execução (valem para todas as tarefas)

1. **Nenhuma correção do fluxo de pickup nesta sprint** (§1). Obstáculo que pareça exigir correção
   vira achado no relatório, nunca edição (Regra 8: rota é do dono).
2. **Nada se lê integralmente acima de 500 linhas.** Artefato grande ou com linha de milhares de
   chars mede-se por sonda programática (`DC-4`); entrada em doc grande é sempre Grep de âncora →
   Read com `offset`/`limit`.
3. **Saída de ferramenta vai para arquivo**; só o agregado entra no contexto. Nenhum `cat`, nenhum
   dump de célula, nenhum `Grep -output_mode content` sobre o diário.
4. **Sem bump e sem tag** (`DE-7`). O relatório é medida do hub, não doutrina nem superfície do kit:
   **nada entra no `CHANGELOG.md`** nesta sprint — a mudança que altera superfície nasce no `P-0737`.
5. **Nenhum guardrail novo, nenhum derivado tocado.**
6. `.claude/skills/redacao-doc/SKILL.md` é normativa para todo texto publicado aqui.
7. No diário as tarefas são `CPK-T1..CPK-T5`; no plano o cabeçalho usa o ID `T<N>` exigido pelo
   parser (`DP-C`, `.claude/tools/rdo.py`).

## 5. Tarefas

### T1 — Sonda programática: orçamento medido por fonte [Sonnet · classe investigacao · teto 20]
- **Objetivo:** medir, sem ingerir conteúdo, quanto pesa cada artefato que o pickup típico lê, e
  como o peso do diário se distribui por dentro — o dataset de que as demais tarefas vivem.
- **Arquivos-alvo:** cria `sonda_pickup.py` **no scratchpad da sessão** (descartável, não
  versionado); cria `docs/CUSTO_DO_PICKUP.md` com as seções `## 1` e `## 2` (**≤ 80 linhas**).
- **Lista fixa de fontes** (uma linha de tabela cada; fonte ausente sai com `ausente`):
  `docs/DIARIO_DE_OBRAS.md`, `docs/DIARIO_HISTORICO.md`, `docs/plans/_INBOX.md`,
  `C:\Users\panta\.claude\projects\d--workspaces-PantonicApp\memory\_INBOX.md`,
  `C:\Users\panta\.claude\projects\d--workspaces-PantonicApp\memory\MEMORY.md` **+ a soma dos
  arquivos de memória que ele indexa** (linha própria), `.claude/global/CLAUDE.md`, `CLAUDE.md` da
  raiz, `.claude/skills/proximo-passo/SKILL.md`, `.claude/skills/diario-de-obras/SKILL.md`, cada
  `.claude/agents/*.md` (linha própria + subtotal), `docs/DOC_MAP.md`, `GOVERNANCA.md`,
  `docs/plans/P-0734-execucao-autonoma.md`, `docs/plans/P-0736-custo-do-pickup.md`.
- **Métricas por fonte:** linhas · chars · tokens estimados (`chars ÷ 4`) · nº e chars da maior
  linha · nº de linhas com mais de 2.000 chars.
- **Recortes internos (só o script os produz):** (a) chars por seção `^## ` de
  `docs/DIARIO_DE_OBRAS.md`, top 10 + agregado do resto; (b) top 10 linhas do diário por chars, com
  nº da linha e preview truncado em 60 chars; (c) por seção `^## `, contagem de cada status do
  vocabulário (`triage`, `ready`, `blocked`, `in-progress`, `review`, `done`, `cancelled`) — seção
  sem status vivo é candidata da `H5`; (d) contagem de linhas casando `Próxima tarefa` e soma dos
  chars dessas linhas; (e) em `docs/plans/_INBOX.md`, total de linhas × linhas sem `[drenado]`.
- **Método:** `python <scratchpad>\sonda_pickup.py > <scratchpad>\sonda_pickup.md`; ler **só** o
  agregado (≤ 120 linhas) e transcrevê-lo ranqueado (`DC-8`) para a `## 2` do relatório. Se um
  caminho não existir, o script emite `ausente` e segue — nunca aborta.
- **Achados a registrar em uma linha cada, sem conserto:** a afirmação de `docs/DOC_MAP.md` de que o
  diário fica abaixo de 500 linhas, e qualquer outra divergência entre doc e medida.
- **Verificação:** script em exit 0; agregado ≤ 120 linhas; `(Get-Content docs\CUSTO_DO_PICKUP.md).Count`
  ≤ 80; toda fonte da lista fixa presente com as cinco métricas; `git status --short` acusa **só**
  `docs/CUSTO_DO_PICKUP.md`.
- **Pronto quando:** as seções `## 1` e `## 2` do relatório estão publicadas, com a tabela ranqueada
  por chars ingeridos e os cinco recortes internos, e nenhum conteúdo de artefato grande entrou no
  contexto.

### T2 — O roteiro do pickup: orçamento por passo e veredito das hipóteses [Sonnet · classe investigacao · teto 18]
- **Objetivo:** converter o inventário estático da `T1` no orçamento do fluxo — que leituras o
  roteiro **obriga**, em que ordem, com que forma de leitura, e quanto cada passo ingere — fechando
  num número único.
- **Arquivos-alvo:** edita `docs/CUSTO_DO_PICKUP.md`, acrescentando `## 3` e `## 4` (**≤ 50 linhas**
  somadas). Nenhum outro arquivo.
- **Fontes de leitura (dirigida, nunca integral):** `.claude/skills/proximo-passo/SKILL.md` e a
  parte de pickup de `.claude/skills/diario-de-obras/SKILL.md` — entrar por
  `Grep pattern:"^#{2,3} "` e ler só as faixas do roteiro com `offset`/`limit`.
- **Tabela `## 3`, uma linha por passo:** ordem · passo · fonte · obrigatório/condicional · forma de
  leitura prescrita (integral | Grep+Read parcial | sonda) · **chars ingeridos** · tokens estimados.
  Passo parcial usa a fatia, não o arquivo (`DC-3`); a fatia sai dos recortes da `## 2` ou de uma
  execução pontual da mesma sonda.
- **Seção `## 4`:** uma linha por hipótese `H1`..`H5` com veredito `confirmada` | `parcial` |
  `refutada` **e o número** que o sustenta.
- **Verificação:** todo passo do roteiro tem uma linha; a soma dos passos **obrigatórios** é escrita
  como o número único *"orçamento medido do pickup típico"*, em chars e tokens, e a decomposição
  soma exatamente a ele; `## 3` + `## 4` ≤ 50 linhas; `git status --short` acusa só
  `docs/CUSTO_DO_PICKUP.md`.
- **Pronto quando:** existe um número único do pickup típico com decomposição que fecha, e as cinco
  hipóteses têm veredito numérico.

### T3 — Rota candidata por fonte e orçamento-alvo proposto [Opus · classe redacao · teto 30]
- **Objetivo:** entregar ao dono o material de decisão — para cada fonte, uma rota do conjunto
  fechado, o que ela faz perder, e o alvo proposto —, **sem implementar nenhuma**.
- **Arquivos-alvo:** edita `docs/CUSTO_DO_PICKUP.md` (`## 5` e `## 6`, **≤ 50 linhas** somadas);
  edita `docs/DOC_MAP.md` acrescentando a entrada do relatório (propósito · quando consultar ·
  seções `## 1`..`## 7` · padrão de acesso por Grep de âncora).
- **Tabela `## 5`, uma linha por fonte da `## 2`, sem exceção:** fonte · chars ingeridos · % do
  orçamento · rota ∈ {`condensar`, `ponteiro`, `gerar-por-instrumento`, `mover-ao-historico`,
  `manter`} (`DC-7`) · o que se perde · ordem de grandeza do conserto (`mecanica` |
  `implementacao` | `comportamental`). Fonte de hipótese refutada recebe `manter`.
- **Seção `## 6`:** o orçamento-alvo na forma da `DC-8` — fração da janela de 200k tokens, em chars
  e tokens, com a folga de execução em número —, mais a redução exigida (medido − alvo) e as fontes
  que, somadas, a entregam.
- **Proibido:** prescrever implementação, abrir tarefa de correção, tocar skill, diário ou inbox.
- **Verificação:** cada fonte da `## 2` aparece exatamente uma vez na `## 5` com valor do conjunto
  fechado; `## 5` + `## 6` ≤ 50 linhas; relatório inteiro ≤ 200 linhas; `docs/DOC_MAP.md` lista o
  relatório; `git status --short` acusa só esses dois arquivos.
- **Pronto quando:** toda fonte tem rota candidata e o orçamento-alvo está escrito em número.

### T4 — Avaliação do dono: rota por fonte e ratificação do alvo [Opus · classe redacao · teto 30]
- **Objetivo:** cumprir o nível 2 — as entregas são avaliadas antes de qualquer decisão de rota.
- **Arquivos-alvo:** edita `docs/CUSTO_DO_PICKUP.md`, acrescentando `## 7 Veredito do dono
  (<data>)` (**≤ 20 linhas**). Nenhum outro arquivo.
- **Roteiro:** apresentar em **uma** mensagem os quatro itens da `DC-9` e registrar a resposta como:
  uma linha por fonte com a rota escolhida (ou `medir-mais`), o alvo ratificado em chars e tokens, e
  a autorização (ou não) de abrir o `P-0737`.
- **Proibido:** iniciar qualquer correção nesta execução; autorar o `P-0737`; reabrir a medida.
- **Verificação:** a `## 7` existe, datada, com uma linha por fonte apresentada e o número
  ratificado; `git status --short` acusa só `docs/CUSTO_DO_PICKUP.md`.
- **Pronto quando:** o dono responde e o veredito está registrado verbatim no que decide.

### T5 — Revisão do `README.md` da raiz [Opus · classe redacao · teto 30]
- **Objetivo:** fechar a sprint pelo contrato entre o framework e o cliente (`G-README` dever 2). O
  guarda executável é instrumento da atividade; o **único teste de sentido é o veredito do dono**.
- **Arquivos-alvo:** `README.md` (raiz) — correção do que esta rodada tenha dessincronizado;
  `docs/DOC_MAP.md` só se a entrada da `T3` divergir do publicado.
- **Roteiro:**
  1. Rodar `pwsh .claude/checks/check-readme.ps1` e resolver toda falha estrutural.
  2. Ler o `README.md` procurando o que o guarda **não** vê: prosa que descreva o estado anterior,
     número por extenso divergente de tabela, seção que prometa artefato inexistente, e a menção (ou
     falta dela) ao relatório novo onde o espelho enumera os docs de `docs/`.
  3. Aplicar a `redacao-doc` ao que for reescrito.
  4. Apresentar ao dono, em uma mensagem, o que mudou no espelho nesta sprint e **pedir o veredito**.
     Aprovado, a sprint fecha; reprovado, o veredito vira insumo da rodada seguinte e a tarefa
     devolve ao planejamento.
- **Proibido:** fechar a tarefa sem o veredito do dono; tratar o exit 0 do guarda como aceite.
- **Verificação:** `pwsh .claude/checks/check-readme.ps1` em exit 0 **e** veredito do dono registrado.
- **Pronto quando:** o dono aceita o espelho.

## 6. Ordem de execução

Linear, sem ramo: `T1 → T2 → T3 → T4 → T5`.

O corte é por valor validável cedo: a `T1` já devolve, sozinha, a tabela que diz onde a janela some;
a `T2` transforma a tabela num número único; a `T3` é o material de decisão; a `T4` é a avaliação
que o nível 2 exige; a `T5` é o aceite da sprint.

Dependências duras: a `T2` consome a `## 2`; a `T3` consome a `## 3` e a `## 4`; a `T4` consome a
`## 5` e a `## 6`. O relatório é o portador entre tarefas (`DC-5`) — nenhuma tarefa depende do
scratchpad de outra, e trocar de contexto entre tarefas não custa remedição.

**Critério de aceitação da iniciativa** (a aferir depois da correção do `P-0737`, não aqui): um
pickup completo — dois inboxes drenados, diretiva lida, fila apurada e dossiê da tarefa em mãos —
cabendo no orçamento-alvo ratificado na `T4`, medido pelo mesmo método da `DC-4`, deixando a janela
com a folga de execução declarada.

## 7. Riscos

| Risco | Mitigação |
|---|---|
| A sonda medir **arquivo** onde o pickup ingere **fatia**, inflando o orçamento e apontando rota errada | `DC-3` obriga as duas colunas; a `T2` usa a fatia em todo passo de leitura parcial |
| O executor "aproveitar a viagem" e corrigir o que mediu, matando o nível 2 | Invariante 1 + `git status --short` na verificação de todas as cinco tarefas |
| O relatório virar prosa e reproduzir o defeito que mede | Teto por seção (`DC-6`), teto de 200 linhas (`DC-5`) e vocabulário fechado (`DC-7`) |
