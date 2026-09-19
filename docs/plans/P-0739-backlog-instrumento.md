# P-0739 — O pickup vira instrumento: `backlog.py` decide a próxima tarefa, fecha a tarefa e mantém o kanban

**Data:** 2026-09-15 · **Origem:** diretiva do dono, 2026-09-15 ("mecanizar o próximo passo") ·
**Status:** `in-progress` (2026-09-18, retomado pela `RP-7`: `AE-8` absorvido, §2.5 item 6 emendado
com a forma completa de E-2 e a tarefa `BKL-T3b` autorada) ·
**Prefixo das tarefas no diário:** `BKL-T<n>` · **Prefixo das decisões:**
`DB-<n>` · **Checagem de versão do kit:** modo hub — congelada em `0.0.0` (`DE-7`), nada a comparar.
**Ordem de execução:** BKL-T3b → BKL-T4 → BKL-T5 → BKL-T6 → BKL-T7 →
BKL-T8 → BKL-T9 (`BKL-T2b`, `BKL-T2c` `done` em 2026-09-16; `BKL-T2d`, `BKL-T2e` `done` em
2026-09-17; `BKL-T3` `done` com ressalva em 2026-09-17; `BKL-T3a` `done` com ressalva em
2026-09-18) · **Rodadas de replanejamento:** `RP-1`
(2026-09-16, sobre `AE-1`) · `RP-2` (2026-09-16,
sobre `AE-2` — fechada) · `RP-3` (2026-09-16, sobre `AE-3` — fechada) · `RP-4` (2026-09-16, sobre
`AE-4` — fechada) · `RP-5` (2026-09-17, sobre `AE-6`, com a emenda do `AE-5` — fechada) · `RP-6`
(2026-09-18, sobre `AE-7` — fechada) · `RP-7` (2026-09-18, sobre `AE-8` — fechada; ver
`## Achados da execução`).

**Tarefas:** 16 (`BKL-T1`, `BKL-T2`, `BKL-T2a`, `BKL-T2b`, `BKL-T2c`, `BKL-T2d`, `BKL-T2e`,
`BKL-T3`, `BKL-T3a`, `BKL-T3b`, `BKL-T4`..`BKL-T9`).
As três tarefas novas da `RP-3` consertam o instrumento de revisão que a `BKL-T2` exercitou pela
primeira vez de ponta a ponta: `BKL-T2b` e `BKL-T2c` em `review_evidence.py` (leitura do campo
`Arquivos-alvo` e atribuição de arquivo a tarefa no confronto de escopo), `BKL-T2d` em `rdo.py laudo`
(campo de achado de processo). A `RP-4` acrescenta a `BKL-T2e`, também em `review_evidence.py`: o
balde do ato do dono no confronto de escopo (`DB-32`). Nenhuma delas toca `backlog.py`. A `RP-6`
acrescenta a `BKL-T3a`, em `backlog.py`: as três condições de exit 3 de `next` (`DB-37`) e o contador
do rodapé pela gramática do arquivo que ele lê (`DB-38`). A `RP-7` acrescenta a `BKL-T3b`, no mesmo
verbo `next`: a metade "pai de candidato" de E-2 (`DB-40`) e o prefixo `- ` do contador de fila de
memória (`DB-41`); é ela que abre a fila do produto, antes da `BKL-T4`.

## Contexto

O fluxo "execute o próximo passo" é hoje um roteiro em prosa (`.claude/skills/proximo-passo/SKILL.md`,
201 linhas) que manda o agente **ler para descobrir**: drenar `docs/plans/_INBOX.md`, ler a diretiva e a
`Fila corrente` no cabeçalho do diário, apurar status no índice, grep pelo ID, ler a seção. A medida
está publicada em `docs/CUSTO_DO_PICKUP.md`: pickup típico de **77.457 chars** (`## 3`), rotas
`gerar-por-instrumento` / `ponteiro` / `condensar` ratificadas pelo dono em 2026-08-23 (`## 9`), e
a rodada de prosa do `P-0738` (Estágio C) **não** reduziu o custo — a `CTX-T10` mediu +34%
(`## 10`). O que falta não é mais prosa: é o instrumento que a `## 5` listou como rota e ninguém
implementou.

Três defeitos estruturais impedem que o pickup seja programático hoje (verificados nesta sessão):

1. **Status por tarefa não é legível por máquina.** Os cabeçalhos seguem a gramática `DP-C`
   (`### <ID> — <título> [<modelo> · classe <classe>]`) sem estado; o estado vive em prosa
   ("`TK-54a` é a próxima tarefa delegável", "3/12", bullets "`CTX-T9` — … — `done` em …").
2. **A célula `Status` do índice carrega narrativa.** Das 26 linhas do índice ativo, 9 têm estado
   seguido de parêntese narrativo, 1 usa `backlog` e 1 usa `**decidido em parte**` — valores fora do
   vocabulário fechado da residência única (skill `diario-de-obras`).
3. **Os ponteiros de fila são parágrafos.** `**Fila corrente:**` no cabeçalho tem 30 linhas de
   decisões acumuladas; `**Próxima tarefa:**` existe em 2 seções vivas (mais 39 históricas) e é
   reescrita à mão. O agente lê tudo isso para extrair um ID.

**Resultado esperado:** uma chamada (`python .claude/tools/backlog.py next`) devolve o dossiê da única
tarefa a tratar; uma chamada (`backlog.py status <ID> <estado>`) fecha a tarefa e reescreve todas as
projeções; a ambiguidade deixa de ser escolha do agente e vira **defeito nomeado** pelo instrumento.
Nada do diário, do inbox ou do histórico entra no contexto além do dossiê.

**Relação com planos vivos (Controle 1.2 verificado):** `P-0737` está `blocked` pela `TK-54` e sua
`AUT-T6` transpõe a *prosa* de `proximo-passo`/`handover` para `passagem-de-bastao`; este plano
entrega o *instrumento* que aquela skill vai chamar, sem tocar o `P-0737` (classificação: enabler,
não A nem B — registrado como apenso em `P-0737` `## 9` no ato do registro). `P-0736`/`P-0738` estão
`done`; suas rotas ratificadas são a autoridade deste plano.

## 1. Decisões (fechadas no ato; o executor não reabre)

| Id | Decisão | Conteúdo |
|---|---|---|
| **`DB-1`** | Um instrumento, stdlib, testável por caminho | `.claude/tools/backlog.py`: funções recebem `repo`/caminhos já resolvidos e nunca leem `sys.argv` (desenho de `uow.py`/`materializar.py`); escrita atômica (temp + `os.replace`, como `telemetria.py`); parser próprio de ID (`DB-14`), sem tocar `rdo.py` |
| **`DB-2`** | Fonte única do estado = linha de campo na residência do item | Todo item vivo (tarefa `###`, tíquete `## TK-`, plano `# P-`) tem `**Status:**` legível por máquina (§2). A célula `Status` do índice é **projeção** escrita no mesmo ato pelo instrumento; `check` prova a igualdade e falha se divergir |
| **`DB-3`** | Vocabulário fechado, sem exceção | Só os estados da residência única (`triage`, `ready`, `blocked`, `in-progress`, `review`, `done`, `cancelled`; `superseded` só para plano). `backlog` e `decidido em parte` não existem: a migração (`BKL-T6`) os converte com razão registrada |
| **`DB-4`** | O instrumento não decide o que exige juízo | Não destrava `blocked`, não flipa plano para `done`, não promove memória, não escolhe entre dois `in-progress`. Esses casos saem num **rodapé fixo** de uma linha cada, e o agente decide com o dono |
| **`DB-5`** | `next` é somente-leitura e idempotente | Por isso pode rodar em hook. Toda escrita é verbo explícito (`status`, `drain`, `diretiva`) |
| **`DB-6`** | Ambiguidade é defeito, não escolha | Dado ambíguo faz `next` sair com **exit 3** nomeando o conserto; o agente nunca "resolve por grep" — conserta o dado ou escala. **Enumeração emendada pela `DB-37` (`RP-6`, 2026-09-18):** a lista das condições de exit 3 de `next` sai desta célula e passa a morar **só** em §2.5 item 6; as duas condições que esta célula listava e que `next` não distingue (linha de índice fora da gramática, plano vivo sem prefixo) têm destino nomeado na `DB-37`. Esta decisão segue valendo como princípio |
| **`DB-7`** | Teto do dossiê emitido | Seção da tarefa verbatim até **8.000 chars / 120 linhas**; além disso, truncado com ponteiro `arquivo:l1-l2`. Alvo do pickup ratificado: 40.000 chars (`CUSTO_DO_PICKUP.md` `## 6`); o dossiê é a maior fatia |
| **`DB-8`** | Hook `UserPromptSubmit`, registrado no canônico | `backlog_hook.py` casa o gatilho (`pr[oó]ximo passo` / `continue o backlog` / `retome o backlog`, case-insensitive) e injeta a saída de `next` como `additionalContext`. Entra em `.claude/projecoes.json` e chega a `settings.json` só por `materializar.py apply` (`P-0735`) |
| **`DB-9`** | Históricos são append-only e nunca lidos | `_INBOX_HISTORICO.md` e `DIARIO_HISTORICO.md` só recebem apenso de `drain`; o instrumento nunca os abre para ler |
| **`DB-10`** | Toda escrita imprime a lista de arquivos tocados | Permite a verificação `git status --short` de cada tarefa e a revisão do diff antes do commit |
| **`DB-11`** | Diretiva de priorização reescrita no registro | O pedido do dono de 2026-09-15 é instrução de prioridade: ao registrar o plano, a linha vira `**Diretiva de priorização:** Priorize \`P-0739\` — depois retoma \`TK-54\`.` O texto atual da diretiva (decisões sobre `TK-53`/`TK-54`) migra verbatim para a seção `## TK-54`. **Único ponto a confirmar na aprovação** |
| **`DB-12`** | `Próxima tarefa` de seção deixa de ser fonte | A projeção viva é o bloco gerado `Fila corrente` no cabeçalho (§2.5). As linhas `**Próxima tarefa:**` das seções vivas viram ponteiro fixo ("ver bloco *Fila corrente*"); as históricas ficam como estão |
| **`DB-13`** | Sem bump, sem tag, hub primeiro | `DE-7`/`DA-3`: linha em `CHANGELOG.md` sob `## [Não lançado]`; nenhum derivado tocado — propagação é ato posterior (memória `kit-pantonic-propagacao`) |
| **`DB-14`** | Gramática de ID do instrumento | `P-[0-9]{4}` (plano) · `TK-[0-9]+[a-z]?` (tíquete/subtarefa) · `(?:[A-Z0-9]+-)?T[0-9]+[a-z]?` (tarefa de plano, com ou sem prefixo). Achado pré-existente, **não corrigido aqui**: `rdo.py` `_ID_HEADER_RE` só aceita `T<n>` sem prefixo — por isso não há RDO de `CTX-*`. Vai para `## Achados da execução` |
| **`DB-15`** | Plano vivo recebe linhas de campo; plano fechado não se toca | Adicionar `- **Status:**` sob cabeçalhos de `P-0737` é metadado, autorizado por esta decisão; corpo do plano segue imutável. Planos `done`/`superseded` não recebem nada (o índice é a projeção final deles) |
| **`DB-16`** | Executor não escreve estado; `scrum-master` chama o verbo | Mantém `DP-G`: quem materializa status é a orquestração. O executor devolve a linha de retorno; o orquestrador roda `backlog.py status`. `rdo.py close` e `telemetria.py append` seguem separados e sequenciados pela skill, não chamados pelo instrumento |
| **`DB-17`** | Cabeçalho de tíquete e de subtarefa — forma normativa (`RP-1`) | Tíquete: `## TK-<n> — <título>`, nível 2, **sem** bracket (tíquete é fila de entrada: não tem modelo nem classe). Subtarefa de tíquete: `### TK-<n><letra> — <título> [<modelo> · classe <classe>]` — a `DP-C` completa, idêntica à tarefa de plano, porque a subtarefa é executada como tarefa e `rdo.py`/`review_evidence.py` já leem essa forma. As duas subtarefas reais sem modelo (`TK-54a`, `TK-54b`, `[classe investigacao]`) recebem `Sonnet · ` na migração `BKL-T6` (f) — execução roda em Sonnet (`GOVERNANCA.md` §3). Ratifica a leitura A do `AE-1` para tíquete; a leitura B não descreve nada real |
| **`DB-18`** | Tabela normativa não usa `idem` nem remissão | Toda linha de tabela de gramática escreve a forma inteira; `idem`, `análogo`, `mesmo que acima` são defeito de autoria (léxico proibido do planejador). Cada linha da gramática cita ≥ 1 ocorrência real que a casa, e toda forma real fora da gramática está nomeada como item de migração — o inventário é o fato `F-1` (antes de §2) |
| **`DB-19`** | Forma fora da gramática é violação nomeada, nunca decisão | `check` classifica o que não casa em violações de vocabulário fechado (`C-1..C-9`, inline no card `BKL-T2`). O executor nunca escolhe entre leituras: se a gramática admitir duas leituras para a mesma linha real, o defeito é da gramática e o card volta ao planejador (`G-REPLAN`, `GOVERNANCA.md` §7 item 17) |
| **`DB-20`** | Bracket de tarefa: variantes reais toleradas (`RP-1`, `F-1`) | `<modelo>` pode vir seguido de ` + dono` (o aceite do dono é parte da tarefa: `BKL-T9`, `AUT-T10`) e o bracket pode terminar em ` · teto <n>` (sufixo legado dos 10 cards de `P-0737`; a doutrina atual não escreve teto no card). O parser aceita os dois e ignora o teto; nenhum vira violação e a `BKL-T6` não toca esses cabeçalhos (`DB-15`: corpo de plano é imutável) |
| **`DB-21`** | O gate de revisão vale para plano com ID prefixado, sem exceção (`RP-2`) | Tarefa de plano com prefixo (`AUT-*`, `CTX-*`, `BKL-*`) é revisável como qualquer outra: o dossiê de evidência (`review_evidence.py`) é uma das três entradas de julgamento do `pantonic-reviewer` e a autoridade mecânica sobre as dimensões `guardas` e `testes`. O precedente herdado do `DB-14` ("por isso não há RDO de `CTX-*`" — fechar sem RDO) **não** é doutrina: nunca foi decidido em lugar nenhum, e fica revogado aqui. Limitação de instrumento não dispensa gate — conserta-se o instrumento |
| **`DB-22`** | Rota da correção: a gramática de ID mora num ponto só, em `rdo.py` (`RP-2`) | Corrigir `_ID_HEADER_RE` (`rdo.py:79`) e `_HEADER_BRACKET_RE` (`rdo.py:81-85`) para o ID da `DB-14` (`(?:[A-Z0-9]+-)?T[0-9]+[a-z]?`) e para o ` + dono` da `DB-20`, com regressão em `tests/test_rdo.py` — tarefa `BKL-T2a`. Revoga a cláusula "não corrigido aqui" da `DB-14`. Rotas descartadas: (a) parser próprio em `review_evidence.py` — duplicaria a gramática em dois arquivos, contra a residência única do `DB-1`; (b) renomear as tarefas dos planos vivos para `T<n>` sem prefixo — quebraria `DB-14`, o índice do diário, o parser da `BKL-T2` e 36 cabeçalhos em 3 planos; (c) manter o precedente e fechar sem evidência — deixa `guardas`/`testes` sem autoridade mecânica, que é exatamente o que a `AE-2` denuncia |
| **`DB-23`** | A correção é do instrumento e não retroage (`RP-2`) | Nenhum RDO nem dossiê de evidência é gerado retroativamente para tarefa já fechada sem ele (`CTX-*` do `P-0738` `done`, `AUT-*` do `P-0737`). O gate vale das tarefas vivas em diante, a começar pela revisão da `BKL-T2`. Retroagir custaria contexto sem produzir julgamento útil: o trabalho já foi aceito e registrado |
| **`DB-24`** | A correção entra neste plano, e o `P-0737` não é tocado (`RP-2`) | A `BKL-T2a` nasce aqui porque é este plano que está parado por ela e é aqui que a gramática de ID foi fixada (`DB-14`). O encaminhamento informal do achado à `AUT-T4` (nota do diário, `docs/DIARIO_DE_OBRAS.md:702-704`) fica absorvido: o card publicado da `AUT-T4` (`docs/plans/P-0737-loop-autonomo.md:305-325`) nunca citou `_ID_HEADER_RE`, então **nenhum escopo publicado do `P-0737` muda** e nenhum arquivo dele é editado — regra de convergência preservada (um alvo, um dono) |
| **`DB-25`** | Atribuição de arquivo a tarefa é do instrumento, não de doutrina de commit (`RP-3`) | `review_evidence.py` passa a classificar cada arquivo tocado em quatro baldes, nesta ordem de precedência: (1) coberto pelos arquivos-alvo do card; (2) declarado como alvo por **outra** tarefa do mesmo plano (lido do próprio `.md`, tarefa a tarefa); (3) registro da orquestração — lista fechada `docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, prefixo `docs/plans/`, prefixo `docs/RDO/`; (4) fora dos alvos **sem atribuição**. Só o balde (4) pesa no veredito mecânico; (2) e (3) são impressos com a atribuição ao lado, nunca escondidos. Tarefa `BKL-T2c`. Rotas descartadas: (a) exigir commit isolado por tarefa antes da revisão — o registro da própria orquestração (diário, telemetria, plano) é escrito **depois** da entrega e **antes** da revisão, então nem o commit isolado o tiraria da árvore, e a regra viveria só em prosa, sem guarda mecânica; (b) receber a lista de tocados por argumento, a partir do auto-relato do executor — troca fato medido por alegação (Regra 7, "telemetria é medida, não auto-relatada"); (c) deixar o revisor filtrar a olho — é o estado que produziu os 38 falsos positivos da `BKL-T2` |
| **`DB-26`** | Forma canônica de autoria do campo `Arquivos-alvo` (`RP-3`) | O campo é uma lista de bullets, **um caminho por bullet**, o caminho sendo o primeiro literal entre crases do bullet, com sufixo opcional `:<linha>` ou `:<l1>-<l2>`; prosa vem depois de ` — `. **Nenhum outro caminho entre crases no campo**: arquivo citado para ser **evitado** vai para `Não fazer`, arquivo citado como contexto vai para `Restrições desta tarefa`, e instrumento invocado no passo vai para `Passos`. Literal entre crases que **não** é caminho (nome de função, cabeçalho de seção, trecho de código) é tolerado na prosa do bullet como âncora do trecho a editar: pela `DB-27` ele nunca vira alvo e sai listado como descartado. Residência mecânica da regra: docstring do módulo + `extrair_arquivos_alvo` em `review_evidence.py` (`BKL-T2b`). A anatomia do card mora em `.claude/agents/pantonic-planner.md`, que só o dono edita (precedente da `RP-2`): o `P-0739` não depende dessa edição. Rotas descartadas: (a) publicar a forma numa seção nova de `GOVERNANCA.md` — criaria segunda residência para a anatomia do card; (b) inventar campo novo legível por máquina (`Alvos:`) — quebraria `extrair_dossie`, `rdo.py close` e os 36 cabeçalhos vivos sem ganho |
| **`DB-27`** | Leitura mecânica do campo é por literal, não por linha (`RP-3`) | Fato que manda: `_parsear_campos` (`.claude/tools/rdo.py:151-183`) junta as linhas de um campo com **espaço** — a estrutura de bullets não chega ao instrumento. Logo a regra mecânica é: todo literal entre crases do campo é candidato; remove-se o sufixo `:<n>`/`:<n>-<m>`; o candidato é caminho quando casa `^[A-Za-z0-9_.][A-Za-z0-9_./\\-]*$` **e** tem extensão (`\.[A-Za-z0-9]+$`), contém `/` ou `\`, ou termina em `/`. O que não casa é listado no dossiê como "não reconhecido como caminho" e **nunca** bloqueia (`DB-19`). Mede o defeito do `AE-3`: `_ID_HEADER_RE = re.compile(…)` deixa de virar alvo (tem espaço) e `CHANGELOG.md` volta a ser alvo (tem extensão). Tarefa `BKL-T2b`. Rotas descartadas: (a) "primeiro literal de cada bullet" — inexequível sem mudar `_parsear_campos`, que é contrato de `rdo.py close`; (b) manter o filtro atual ("contém `/`") — é o que perde `CHANGELOG.md` e aceita literal de regex |
| **`DB-28`** | Achado de processo ganha campo próprio no laudo; `--escalar` volta ao seu uso (`RP-3`) | `rdo.py laudo` ganha `--achado-processo <alvo> "<uma linha>"`, repetível, com alvo em `dossie`\|`doutrina`\|`rubrica` (gravado como `dossiê`/`doutrina`/`rubrica`), e grava a seção `## Achado de processo`. O achado **não** entra em `calcular_laudo`: não muda percentual, veredito, dimensão bloqueante nem recomendação — invariante 1 de `docs/RUBRICA_DE_REVISAO.md` §6. `--escalar` fica reservado ao que a §6 manda escalar: achado de alvo `dossiê` que **invalida a rota**, decisão de arquitetura ou de requisito. Tarefa `BKL-T2d`. Rotas descartadas: (a) seguir usando `--escalar` para achado de processo — força `recomendacao=escalar` e distorce o veredito (medido nos dois laudos de 2026-09-16); (b) empurrar o achado para `--licoes-aprendidas` — perde o alvo que a §6 exige e não é indexável; (c) fazer o achado rebaixar dimensão — proibido pela invariante 1 da §6 |
| **`DB-29`** | Critério de pronto não depende de ato de registro fora dos arquivos-alvo (`RP-3`) | `Pronto quando` e `Verificação` de um card só citam efeito observável nos **arquivos-alvo do próprio card** e comandos que o executor roda. Registro em diário, telemetria, RDO, laudo e plano é ato da orquestração (`DB-16`) e nunca entra no critério de pronto do executor; o que o executor deve devolver vai para a linha de retorno da entrega, não para o critério. Aplicada nesta rodada aos cards `BKL-T2b`/`BKL-T2c`/`BKL-T2d` e à `BKL-T9`. Publicação na anatomia do card (`.claude/agents/pantonic-planner.md`) é ato do dono, como na `RP-1`/`RP-2`. Rotas descartadas: (a) manter o item e cobrar do executor — é o que rendeu `registro` `parcial` na `BKL-T2`, com o item fechado por quem orquestra; (b) virar contingência do card — continuaria fora do alcance de quem executa |
| **`DB-30`** | Contingência acionada tem residência: a linha `**Status:**` do próprio card (`RP-4`) | Contingência prevista que o executor aciona é **devolvida na linha de retorno da entrega**, na forma `contingência <n> acionada: <o que mudou>`; quem a materializa é a orquestração, na linha `- **Status:**` do card (à mão hoje; por `python .claude/tools/backlog.py status <ID> <estado> --nota "…"` a partir da `BKL-T4`, §2.7 — `--nota` apensa sub-bullet datado sem tocar a célula do índice). O campo `Contingências` de card nenhum manda "registrar na nota de execução": a ação fechada termina em devolver na linha de retorno (`DB-16` — executor não escreve estado; `DB-29` — registro fora dos arquivos-alvo não entra no critério de pronto). Mede o defeito 1 do `AE-4`: a `BKL-T2c` acionou a contingência 2 e o ajuste da asserção só ficou auditável pelo diff. Aplicada nesta rodada à `BKL-T2d` e à `BKL-T2e`. Publicação na anatomia do card (`.claude/agents/pantonic-planner.md`) é ato do dono, como na `RP-1`/`RP-2`/`RP-3`; o `P-0739` não depende dela. Rotas descartadas: (a) criar artefato novo "nota de execução" com residência própria — segunda residência para um fato que a linha `Status` já carrega (`DB-1`, `DB-15`); (b) mandar o executor escrever a linha `Status` — viola `DB-16` e devolve ao executor um ato de estado; (c) deixar o diff como registro — é exatamente o estado que o `AE-4` denuncia, com o revisor reconstruindo a contingência a partir do código |
| **`DB-31`** | O defeito 1 do `AE-4` **não** gera tarefa (`RP-4`) | Nenhum instrumento muda por causa da `DB-30`: o canal de escrita já está no escopo do plano (`--nota` de `backlog.py status`, §2.7, com TF na `BKL-T4`) e a linha `- **Status:**` já existe em todo card vivo (`DB-15`). O que muda é **autoria de card**: o campo `Contingências` dos cards ainda não despachados é reescrito nesta rodada (`BKL-T2d`) e a `BKL-T2e` nasce já na forma da `DB-30`; o parágrafo de anatomia fica como pendência de publicação do dono. Cards `done` (`BKL-T2`, `BKL-T2a`, `BKL-T2b`, `BKL-T2c`) não são tocados (`DB-23`, sem retroação). Rotas descartadas: (a) tarefa para varrer os cards fechados e trocar a frase — retroação proibida e sem julgamento útil; (b) tarefa em `backlog.py` para validar a forma `contingência <n> acionada:` dentro da nota — guarda mecânica sobre texto livre, sem corpus para calibrar e fora do escopo publicado; (c) registrar e não agir — o defeito reincidiria já no próximo card com contingência, que é a `BKL-T2e` |
| **`DB-32`** | Ato do dono é o quinto balde do confronto de escopo (`RP-4`) | `review_evidence.py` ganha o balde **ato do dono / fora do ciclo de tarefa** — lista fechada de um item, o prefixo `.claude/agents/` — inserido entre `registro da orquestração` e `fora dos alvos sem atribuição`. A precedência passa a ser: coberto pelos alvos do card > alvo de outra tarefa do mesmo plano > registro da orquestração > ato do dono > fora sem atribuição. O balde é **impresso nominalmente** na seção `## Escopo` (o revisor continua vendo o fato, como na `DB-25`) e não pesa no veredito mecânico. `_REGISTRO_ORQUESTRACAO` **não** recebe `.claude/agents/`: o `Não fazer` da `BKL-T2c` segue válido e nada da entrega dela é desfeito. Fato que manda: definição de agente só o dono edita (`RP-1`, `RP-2`, `RP-3`), a árvore de trabalho é compartilhada, e `.claude/agents/pantonic-planner.md` saiu em "fora dos alvos sem atribuição" em três dossiês seguidos (`BKL-T2a`, `BKL-T2b`, `BKL-T2c`), zerando o poder discriminante do veredito de `escopo` — o mesmo defeito que a `DB-25` corrigiu para os outros baldes. Tarefa `BKL-T2e`. Rotas descartadas: (a) manter a atribuição externa como insumo do despacho — deixa o veredito mecânico `aberto` em toda revisão enquanto houver edição de agente pendente, estado já medido pela `AE-3`, e contraria "o gate mede fato, e fato ambíguo é defeito do instrumento" (`DA-7`, `DB-6`); (b) incluir `.claude/agents/` em `_REGISTRO_ORQUESTRACAO` — funde dois fatos distintos (escrita de ofício **dentro** do ciclo da tarefa vs. ato do dono **fora** dele) e apaga a distinção que a `BKL-T2c` gravou no `Não fazer`; (c) exigir que o dono trabalhe em branch ou stash separado — doutrina de commit sem guarda mecânica, descartada pelo mesmo motivo da rota (a) da `DB-25`; (d) filtrar por autoria do `git` — o arquivo está não commitado, não há autor a consultar |
| **`DB-33`** | Projeção que nomeia o pai tem uma forma por tipo de pai (`RP-5`) | O vencedor de `next` é sempre um item com bracket `DP-C` — tarefa de plano **ou** subtarefa de tíquete (tíquete não tem bracket e nunca é selecionado, `DB-17`) —, logo o pai é um plano ou um tíquete, e toda projeção que nomeia o pai carrega as duas formas, com o **mesmo conjunto de campos** e o rótulo escolhido pelo tipo de pai: `plano: P-NNNN — …` e `tíquete: TK-<n> — …`. Superfícies fechadas no mesmo ato (G-SURFACE): §2.6 linha 2 (com worked example completo para cada tipo) e o bullet por pai do bloco `Fila corrente` (§2.3). Os quatro campos existem para os dois tipos: `<título>` (texto após ` — ` no cabeçalho do pai), `(<done>/<total>)` (`DB-36`), `residência: <arquivo>:<l1>-<l2>`, `índice: <âncora>` (4ª célula da linha do índice do pai); pai vivo sem linha no índice → exit 3 (`DB-6`) com a mensagem `linha de índice ausente para <ID do pai>`. Rotas descartadas: (a) manter o rótulo literal `plano:` e preencher os campos com substituto (`—`, vazio, ou o próprio `TK-<n>`) — o rótulo passaria a mentir sobre a residência (tíquete mora em `docs/DIARIO_DE_OBRAS.md`, não em `docs/plans/`) e obrigaria quem lê a inferir o tipo do pai pelo formato do ID, sendo que **nenhum** campo precisa de substituto; (b) omitir a linha de contexto quando o pai é tíquete — tira do dossiê a residência e a âncora do pai justamente no caso em que o agente mais precisa delas (o pai mora no diário, arquivo que este plano tirou do pickup) e produz saída com número variável de linhas sem regra que diga qual; (c) bloco de duas linhas, uma por tipo de pai, com a do tipo ausente preenchida por `—` — dobra a linha 2 em toda saída para cobrir um caso por vez, contra o teto do dossiê (`DB-7`); (d) tratar o tíquete-pai como plano sintético (`P-0000`) — inventa ID fora da gramática `DB-14` e faz `check` falhar no próprio dado que ele gera |
| **`DB-34`** | A linha `antecessora` é o irmão anterior na ordem interna do pai, e se omite no primeiro irmão (`RP-5`) | `antecessora` = o **irmão imediatamente anterior** ao vencedor entre os filhos diretos do mesmo pai, na ordem interna da §2.5 regra 4 (plano: `Ordem de execução` do cabeçalho, senão ordem dos cabeçalhos no arquivo; tíquete: ordem dos cabeçalhos `### TK-<n><letra>` dentro da seção), **qualquer que seja o estado dela**. Vencedor que é o primeiro irmão da ordem → a linha `antecessora:` **não é impressa** (a saída simplesmente não a tem). `<estado>` = token da linha `- **Status:**` da antecessora; `notas em <arquivo>:<l1>-<l2>` = intervalo do bloco `- **Notas de execução:**` dela (da linha do bullet até o último sub-bullet); antecessora sem esse bloco → a saída escreve `antecessora: <ID> (<estado>; sem notas)`. Rotas descartadas: (a) imprimir `antecessora: —` no primeiro irmão — linha sem informação em toda primeira tarefa de plano, e o executor teria de decidir o que pôr nos parênteses; (b) antecessora = última tarefa `done` do pai — salta irmão `cancelled`/`blocked` que é exatamente o contexto que o agente precisa ver; (c) antecessora = item anterior na fila global (outro pai) — nomeia trabalho de outra iniciativa dentro do dossiê, contra o WIP de 1 iniciativa da §2.5 regra 4 (a) |
| **`DB-35`** | A faixa de bug ordena **itens elegíveis**, não tíquetes (`RP-5`) | §2.5 regra 4 (b) tem por sujeito o item que pode ser selecionado, não o pai: casa o elegível que tem `- **Tipo:** bug` na própria linha de campo **ou** cujo **tíquete-pai** tem essa linha. Plano-pai não carrega `Tipo` (§2.1) e por isso nunca marca uma tarefa de plano como bug — tarefa de plano só entra na faixa (b) pelo `Tipo` do próprio card. A faixa (c) (FIFO) ordena pela linha do **pai** do item no índice do diário, porque tarefa e subtarefa não têm linha de índice (§2.2). Rotas descartadas: (a) manter "tíquetes `Tipo: bug`" — a faixa ficaria vazia por construção, já que tíquete nunca é o item selecionado (`DB-17`), e é o defeito que o `AE-6` mediu; (b) fazer o `Tipo: bug` do tíquete valer só para o tíquete e exigir a linha repetida em cada subtarefa — duplica o mesmo fato em dois lugares, contra a fonte única do `DB-2`; (c) criar faixa separada para bug de plano e bug de tíquete — duas faixas para um critério só, sem caso real que as distinga |
| **`DB-36`** | Fórmula fechada de `<done>/<total>`, igual para plano e tíquete (`RP-5`) | Filhos diretos: de plano, os cabeçalhos `### <PFX>-T<n>` do arquivo do plano; de tíquete, os cabeçalhos `### TK-<n><letra>` dentro da seção dele. `<total>` = número de filhos diretos cujo `Status` **não** é `cancelled`; `<done>` = número desses mesmos filhos cujo `Status` é `done`. Pai sem filho direto não `cancelled` → `(0/0)`. A mesma fórmula serve as três projeções que imprimem o par: §2.6 linha 2, bullet do bloco `Fila corrente` (§2.3) e célula do índice escrita por `status` (§2.2, §3). Rotas descartadas: (a) contar `cancelled` no denominador — a projeção nunca alcança `n/n` e um pai inteiramente despachado aparece incompleto para sempre; (b) contar `done` + `cancelled` no numerador — apaga a diferença entre trabalho feito e trabalho descartado, que é o que a célula comunica; (c) deixar a fórmula implícita e cada verbo contar do seu jeito — `next` e `status` imprimiriam pares diferentes para o mesmo pai, e `check` (`DB-2`) acusaria divergência no próprio dado que o instrumento gera |
| **`DB-37`** | A lista de condições de exit 3 de `next` mora em §2.5 item 6, e só lá (`RP-6`) | Três condições, cada uma com a **substring obrigatória** da mensagem: **E-1** dois ou mais itens candidatos com `Status` `in-progress` → `dois ou mais itens in-progress: ` seguida dos IDs em ordem alfabética crescente, separados por `, `; **E-2** item candidato, ou pai de candidato, sem linha `- **Status:**` → `linha de status ausente para <ID>`; **E-3** pai de candidato elegível sem linha no índice do diário → `linha de índice ausente para <ID>` (literal já fixado pela `DB-33`). Nenhuma outra condição sai exit 3 em `next`. **`DB-6` fica emendada**: mantém o princípio e deixa de enumerar. As duas condições que ela listava e que `next` não distingue ganham destino nomeado: *linha de índice fora da gramática* é descartada na leitura do índice (não existe para `next`) e, quando a linha descartada é a do pai de um candidato elegível, o caso cai em **E-3**; o lint dela é do verbo `check` (`C-4 celula-do-indice-com-prosa`, `C-9 id-do-indice-sem-residencia`); *plano vivo sem prefixo* é `C-7 plano-vivo-sem-prefixo` no `check` e exit 3 do `drain` (`BKL-T5`), porque `next` acha os filhos diretos de um plano pela gramática de ID da `DB-14` e não usa o prefixo declarado. **Segunda cláusula:** `status` e `start` aplicam **E-2** e **E-3** antes de qualquer escrita e saem exit 3 **sem tocar arquivo** (a escrita é um ato só, `DB-1`); a recusa de `start` por já haver outro item `in-progress` no mesmo pai é **exit 1**, recusa de transição, e não exit 3 — o dado não é ambíguo, o instrumento sabe exatamente o que está errado. A cópia inline das quatro condições no card `BKL-T3` (`done`) fica como registro do que foi executado, não se edita (`DB-23`) e deixa de ser residência. Rotas descartadas: (a) manter as quatro condições do card e implementar em `next` um checador dedicado para "linha de índice fora da gramática" — duplicaria `C-4`/`C-9` dentro de um verbo somente-leitura que já descarta a linha, criando segunda residência para o mesmo lint (`DB-2`); (b) manter a lista da `DB-6` e corrigir o card para "plano vivo sem prefixo" — poria em `next` uma condição que `check` (`C-7`) e `drain` já cobrem e que não impede a seleção; (c) deixar as duas listas vivas e anotar a divergência como achado — é o defeito que a `DB-2` proíbe e que esta rodada mede; (d) fixar a mensagem inteira em vez da substring — a `BKL-T3` está `done` (`DB-23`) e a forma completa das mensagens entregues não é fato apurado; substring obrigatória é discriminante para TF e não retroage |
| **`DB-38`** | Uma gramática de linha viva por arquivo de inbox; o rodapé conta com a gramática do arquivo que lê (`RP-6`) | O rodapé de §2.6 tem dois contadores e eles **não** compartilham regra. `inbox de planos: <n> por drenar` conta as linhas de `docs/plans/_INBOX.md` que começam com `- `, contêm um caminho que casa `docs/plans/P-[0-9]{4}-<slug>.md` e **não** começam com `- [drenado ` (gramática de §2.4). `fila de memória: <m> candidato(s)` conta as linhas do inbox de memória (`<memory-dir>/_INBOX.md`) que começam com `- ` e não trazem `[promovido]` nem `[descartado` — gramática de `~/.claude/docs/GOVERNANCA_MEMORIAS.md` §8, residência dela, que não se aplica ao inbox de planos. Todo campo do rodapé tem TF que **afirma o valor impresso**, sobre corpus em que as duas gramáticas dariam números diferentes: fixture em que as regras concorrentes dão o mesmo número não é verificação. Mede o desvio do achado 3 do `AE-7` — `_contar_pendentes_inbox` aplicava a gramática de memória ao inbox de planos e as duas fixtures da `BKL-T3` têm inbox sem linha viva, onde as duas regras dão 0. Rotas descartadas: (a) unificar as duas gramáticas numa só ("linha `- ` não marcada") — apagaria a marca `- [drenado AAAA-MM-DD] ` da §2.4, que é o fato que distingue drenado de vivo, e faria `drain` e `next` discordarem sobre o mesmo arquivo; (b) contar o inbox de planos a partir de `_INBOX_HISTORICO.md` — históricos nunca são lidos (`DB-9`); (c) registrar o desvio e não agir — o campo errado sai em toda injeção do hook (`DB-8`), a cada prompt, e é insumo do `Pronto quando` da `BKL-T5` |
| **`DB-39`** | Os dois defeitos de código do `AE-7` residem na tarefa nova `BKL-T3a`, despachada antes da `BKL-T4` (`RP-6`) | Um card só, `classe implementacao`: mesmo módulo (`.claude/tools/backlog.py`, verbo `next`), mesmo arquivo de teste (`tests/test_backlog.py`) e mesma família de fixture. Nenhuma entrega fechada é reaberta (`DB-23`): a `BKL-T3` segue `done` com a ressalva registrada na linha `Status` dela, e a `BKL-T3a` nasce como `BKL-T2a`..`BKL-T2e` nasceram das rodadas `RP-2`/`RP-3`/`RP-4` — correção de instrumento em card próprio, com dossiê próprio e gate próprio. Ordem `BKL-T3a` → `BKL-T4`, porque a `BKL-T4` aplica E-2 e E-3 antes de escrever (`DB-37`) e reusa as funções que a `BKL-T3a` normaliza. Rotas descartadas: (a) absorver os dois defeitos na `BKL-T4` — o card já carrega os TF da `RP-5` e passaria a misturar verbo de escrita com defeito de `next`, contra o "exatamente um entregável observável" por tarefa; (b) duas tarefas, uma por achado — mesmo módulo, mesmo arquivo de teste e mesma fixture em dois contextos de executor, dobrando custo sem fatiar risco; (c) registrar e não agir — deixaria `rota` `parcial` de pé e o contador errado no dossiê que o hook injeta a cada prompt |
| **`DB-40`** | **E-2** vale para o pai tanto quanto para o item, e a mensagem lista ID distinto uma vez, em ordem alfabética (`RP-7`) | `next` aplica **E-2** sobre a união de dois conjuntos — o item de cada candidato **e** o pai de cada candidato —, e o ID sem a linha `- **Status:**` produz uma ocorrência de `linha de status ausente para <ID>`. **Três cláusulas fechadas:** (i) **ID distinto uma vez** — pai com dois filhos candidatos aparece uma única vez na mensagem; (ii) **ordem alfabética crescente do `<ID>`**, ocorrências separadas por `, ` (a mesma ordenação que a `DB-37` já fixou para **E-1**); (iii) **E-2 é avaliada antes de E-1 e de E-3**, ordem que a `BKL-T3` entregou e esta decisão preserva. Residência da regra: §2.5 item 6 (`DB-37`), emendada no mesmo ato — esta célula remete a ela e não a reenuncia. Fronteira contra o instrumento vizinho: a ausência da linha é violação `C-2` (tarefa, tíquete, subtarefa) ou `C-8` (plano vivo) do verbo `check`; `next` recusa a seleção e não classifica a violação. Mede o desvio do achado 1 do `AE-8`: com `sem_status` filtrando só `c.item.status is None`, o pai sem `Status` cai no filtro de elegibilidade (`c.pai.status in ("ready", "in-progress")`) e os candidatos dele somem **em silêncio**. Rotas descartadas: (a) manter E-2 só sobre o item — é o desvio medido, e desempatar por heurística é o que `DB-6` proíbe; (b) tratar pai sem `Status` como pai `ready` — inventa estado que o dado não tem, contra `DB-2` (fonte única) e `DB-3` (vocabulário fechado); (c) repetir o ID do pai uma vez por filho candidato — a mesma mensagem n vezes num verbo com teto de dossiê (`DB-7`), sem informação nova; (d) registrar e não agir — `next` sai no hook a cada prompt (`DB-8`) e a seleção silenciosa é exatamente o que este plano existe para eliminar |
| **`DB-41`** | O prefixo de candidato do contador de fila de memória inclui o espaço; régua `---` não é candidato (`RP-7`) | `_contar_inbox_memoria` conta a linha cujo texto, depois de `strip()`, **começa com `- `** (hífen **e** espaço) e não traz `[promovido]` nem `[descartado`. A norma **não muda**: §2.6 e a residência dela (`~/.claude/docs/GOVERNANCA_MEMORIAS.md` §8) já escrevem `- `; o que desviou foi o código (`s.startswith("-")`, sem o espaço), que faz a régua markdown `---` contar como candidato por prefixo. O contador **não ganha nenhum outro filtro** — nem indentação, nem data, nem campo `**origem:**`: o que exclui linha é só a marca `[promovido]`/`[descartado`. O campo tem TF sobre corpus em que as duas leituras dão números diferentes (`DB-38`, mesma exigência). Rotas descartadas: (a) alargar a norma para "começa com `-`" — o campo passaria a mentir em todo inbox com separador, e a gramática mora em `GOVERNANCA_MEMORIAS.md` §8, que este plano não edita; (b) filtrar régua por regex própria (`^-{3,}$`) — segunda regra para o que o prefixo `- ` já resolve, contra a residência única (`DB-2`); (c) acrescentar filtro de indentação no mesmo ato — não há forma real apurada (o inventário desta rodada não mediu sub-bullet em inbox de memória) e gramática autorada de memória é o defeito da `RP-1`; (d) registrar e não agir — o campo errado sai em toda injeção do hook (`DB-8`) |
| **`DB-42`** | Os dois defeitos do `AE-8` residem na tarefa nova `BKL-T3b`, despachada antes da `BKL-T4` (`RP-7`) | Um card só, `classe implementacao`: mesmo módulo (`.claude/tools/backlog.py`, verbo `next`), mesmo arquivo de teste (`tests/test_backlog.py`) e mesma família de fixture (`tests/fixtures/backlog/next_tk90/` copiada no `tmp_path`, mais inbox de memória escrito no `tmp_path`). Nenhuma entrega fechada é reaberta (`DB-23`): a `BKL-T3a` segue `done` com a ressalva registrada na linha `Status` dela, e a `BKL-T3b` nasce como `BKL-T2a`..`BKL-T2e` e `BKL-T3a` nasceram — correção de instrumento em card próprio, com dossiê próprio e gate próprio. Ordem `BKL-T3b` → `BKL-T4`, pelo mesmo motivo da `DB-39`: a `BKL-T4` aplica **E-2** ao item alvo **e ao pai dele** antes de escrever (`DB-37`, segunda cláusula) e reusa a função que a `BKL-T3b` normaliza; despachar a `BKL-T4` antes faria o verbo de escrita implementar a metade "pai" por conta própria, criando segunda residência para a mesma regra. Rotas descartadas: (a) absorver os dois defeitos na `BKL-T4` — o card já carrega os TF da `RP-5` e da `RP-6` e passaria a misturar verbo de escrita com defeito de `next`, contra o "exatamente um entregável observável"; (b) duas tarefas, uma por achado — mesmo módulo, mesmo arquivo de teste e dois contextos de executor, dobrando custo sem fatiar risco (mesma razão da `DB-39`); (c) `BKL-T3b` depois da `BKL-T4` — deixa o verbo de escrita nascer sobre a metade entregue de E-2; (d) registrar e não agir — deixaria `next` elegendo por heurística quando falta a linha do pai, com desvio já medido na revisão |
### Inventário do corpus (fato `F-1`, apurado na `RP-1` de 2026-09-16)

Formas reais de cabeçalho de item vivo, contadas por regex sobre `docs/DIARIO_DE_OBRAS.md`,
`docs/plans/P-0737-loop-autonomo.md` e este plano. A gramática de §2.1 é escrita **contra** esta
lista: toda forma casa exatamente uma linha da tabela ou está nomeada como item de migração.

| forma real | ocorrências | exemplo | destino na gramática |
|---|---|---|---|
| `### <PFX>-T<n> — <título> [<modelo> · classe <classe>]` (tarefa de plano, `DP-C` pura) | 8 de 19 | `docs/plans/P-0739-backlog-instrumento.md:153` | linha *tarefa de plano* (`DP-C`) |
| `### <PFX>-T<n> — <título> [<modelo> · classe <classe> · teto <n>]` (sufixo legado `teto`) | 10 de 19 | `docs/plans/P-0737-loop-autonomo.md:218` | linha *tarefa de plano*: sufixo tolerado e ignorado (`DB-20`); não migra (`DB-15`) |
| `### <PFX>-T<n> — <título> [<modelo> + dono · classe <classe>[ · teto <n>]]` (aceite do dono) | 2 de 19 | `docs/plans/P-0739-backlog-instrumento.md:333` | linha *tarefa de plano*: ` + dono` aceito (`DB-20`) |
| `## TK-<n> — <título>` (tíquete, nível 2, sem bracket) | 7 | `docs/DIARIO_DE_OBRAS.md:705` | linha *tíquete* (`DB-17`) |
| `### TK-<n><letra> — <título> [classe <classe>]` (subtarefa **sem** `<modelo>`) | 2 de 4 | `docs/DIARIO_DE_OBRAS.md:1233` | **migração `BKL-T6` (f)**: vira `[Sonnet · classe <classe>]` (`DB-17`) |

Nenhum item vivo tem linha `**Status:**` hoje (defeito 1 do Contexto) — migração `BKL-T6` (c).

## 2. Gramática legível por máquina (normativa; `BKL-T1` a transcreve para a skill `diario-de-obras`)

### 2.1 Item e residência

| item | residência viva | cabeçalho | campos obrigatórios logo abaixo |
|---|---|---|---|
| plano | `docs/plans/P-NNNN-<slug>.md` | `# P-NNNN — <título>` (linha 1) | nas 20 primeiras linhas: `**Status:** \`<estado>\`` e `**Prefixo das tarefas no diário:** \`<PFX>-T<n>\``; opcional `**Ordem de execução:** ID → ID → …` (1ª ocorrência vence; ausente = ordem dos cabeçalhos) |
| tarefa de plano | no plano (`### <ID> …`) | `### <ID> — <título> [<modelo>[ + dono] · classe <classe>[ · teto <n>]]` (`DP-C`; ` + dono` marca aceite do dono, ` · teto <n>` é sufixo legado tolerado e ignorado — `DB-20`) | 1º bullet: `- **Status:** \`<estado>\` · AAAA-MM-DD[ · <razão de 1 linha>]`; opcionais `- **Depende de:** \`ID\`[, \`ID\`]`, `- **Tipo:** bug`; `- **Notas de execução:**` com sub-bullets `  - AAAA-MM-DD \`<estado>\` — <texto>` apensados pelo instrumento |
| tíquete | `docs/DIARIO_DE_OBRAS.md` | `## TK-<n> — <título>` (nível 2, **sem** bracket — tíquete não tem modelo nem classe; `DB-17`) | mesmos campos da tarefa (`Status`, `Tipo`, `Notas de execução`) |
| subtarefa de tíquete | `docs/DIARIO_DE_OBRAS.md`, dentro da seção do tíquete-pai | `### TK-<n><letra> — <título> [<modelo> · classe <classe>]` (`DP-C` completa, igual à tarefa de plano; `DB-17`) | mesmos campos da tarefa |

Uma tarefa é *do* plano cujo prefixo casa com o dela; `TK-<n><letra>` é *do* tíquete `TK-<n>`.

### 2.2 Índice do diário

`| <ID> | <título curto> | <estado>[ <done>/<total>] | <âncora> |` — a célula `Status` contém **só**
o token do vocabulário, opcionalmente seguido de `<done>/<total>` para plano/tíquete com subtarefas.
Nada mais. Título e âncora seguem de autoria humana (o instrumento só cria a linha no `drain` e só
reescreve a célula `Status`).

### 2.3 Cabeçalho do diário (bloco gerado)

```markdown
**Diretiva de priorização:** [Priorize `<ID>`[, `<ID>`…]] [— <texto livre>]
<!-- fila:gerada -->
**Fila corrente:** `<ID>` — <título> (`<arquivo>:<l1>-<l2>`) · fila: <ID2>, <ID3> · ready <n> · blocked <m> · in-progress <k>
- `P-NNNN` (`<estado>`, <done>/<total>): próxima `<ID>`
- `TK-<n>` (`<estado>`, <done>/<total>): próxima `<ID>`
<!-- /fila:gerada -->
```

O instrumento lê só os tokens `` `ID` `` antes de ` — ` na diretiva; o texto livre é para humanos.
Tudo entre os marcadores é reescrito a cada verbo de escrita; humano não edita ali.

Bullets do bloco (`DB-33`): **um bullet por pai vivo** — plano ou tíquete — que tenha ao menos um
filho direto em estado não terminal, na ordem das linhas do índice do diário. O pai plano escreve o
token `` `P-NNNN` ``; o pai tíquete escreve o token `` `TK-<n>` ``. `<estado>` é o token da linha
`Status` do pai; `<done>/<total>` é a contagem da `DB-36`; o `<ID>` de `próxima` é o filho direto
que vence a ordem interna da §2.5 regra 4 **dentro daquele pai**, e o pai sem nenhum filho elegível
escreve `próxima —`.

### 2.4 Inbox de planos

Linha viva: começa com `- `, contém um caminho que casa `docs/plans/P-[0-9]{4}-<slug>.md` e **não**
começa com `- [drenado ` (o resto da linha é livre).
Drenada: prefixada `- [drenado AAAA-MM-DD] ` e movida **verbatim** para `_INBOX_HISTORICO.md`; a
linha drenada nunca é viva, mesmo trazendo o caminho do plano.
Contador: `**Próximo id de plano: P-NNNN.**` — `drain` o recalcula como `max(id visto) + 1`.

Esta é a única gramática de linha viva deste arquivo (`DB-38`): a gramática de marcação do inbox de
memória (`~/.claude/docs/GOVERNANCA_MEMORIAS.md` §8 — linha `- ` sem `[promovido]` e sem
`[descartado`) vale só para `<memory-dir>/_INBOX.md` e nunca se aplica a `docs/plans/_INBOX.md`.

### 2.5 Ordem total de seleção (`next`)

1. Diretiva com IDs → candidatos restritos a esses itens e suas tarefas; sem IDs → todos.
2. Exatamente um `in-progress` → é a resposta (retomada). Dois ou mais → exit 3, condição **E-1** do
   item 6.
3. Elegíveis: tarefas `ready` cujo plano/tíquete-pai está `ready` ou `in-progress`, com todo
   `Depende de` em `done`. Plano `blocked`/`superseded`/`done`/`cancelled` não contribui.
4. Ordem, em três faixas de precedência sobre os **itens elegíveis** (`DB-35`): (a) tarefas cujo
   plano-pai está `in-progress` (WIP de 1 iniciativa); (b) itens marcados como bug — o item tem
   `- **Tipo:** bug` na própria linha de campo **ou** o tíquete-pai dele tem essa linha (plano-pai
   não carrega `Tipo`, §2.1); (c) FIFO pela ordem das linhas do índice do diário, lida na linha do
   **pai** do item (tarefa e subtarefa não têm linha de índice, §2.2). Ordem interna, nas três
   faixas: entre filhos do mesmo pai vale a `Ordem de execução` do plano-pai, senão a ordem dos
   cabeçalhos na residência do pai (para tíquete, a ordem dos `### TK-<n><letra>` na seção dele);
   entre pais diferentes vale a ordem das linhas do índice.
5. Resultado: uma tarefa (exit 0) ou "nada delegável" com contagens (exit 2). `blocked` e
   memórias por promover aparecem só no rodapé.
6. **Condições de exit 3 de `next` — lista única (`DB-37`).** Esta tabela é a residência da lista;
   toda cópia inline em card deriva **desta** tabela, verbatim, e nenhuma outra seção, decisão ou
   card a reenuncia. São três, e nenhuma outra condição sai exit 3 em `next`:

   | # | condição observável | substring obrigatória da mensagem | `<ID>` na mensagem |
   |---|---|---|---|
   | **E-1** | dois ou mais itens candidatos com `Status` `in-progress` | `dois ou mais itens in-progress: ` seguida dos IDs, em ordem alfabética crescente, separados por `, ` | todos os itens `in-progress` entre os candidatos |
   | **E-2** | item candidato, ou pai de candidato, sem a linha `- **Status:**` | `linha de status ausente para <ID>`, uma ocorrência por **ID distinto**, em ordem alfabética crescente do `<ID>`, separadas por `, ` | o ID do item ou do pai sem a linha; pai com dois filhos candidatos aparece **uma vez** |
   | **E-3** | pai de candidato elegível sem linha no índice do diário | `linha de índice ausente para <ID>` | o ID do pai (`P-NNNN` ou `TK-<n>`) |

   Ordem de avaliação (`DB-40`): **E-2** é avaliada **antes** de E-1 e de E-3 — dado sem a linha
   `Status` recusa a seleção antes de qualquer contagem de `in-progress` ou de leitura do índice.
   O conjunto sobre o qual E-2 corre é a união do **item de cada candidato** com o **pai de cada
   candidato**; pai sem a linha nunca é tratado como pai `ready` (`DB-2`, `DB-3`).

   Fronteira contra o lint (`DB-37`, `DB-40`): a **ausência** da linha `- **Status:**` é violação
   `C-2` (tarefa, tíquete, subtarefa) ou `C-8` (plano vivo) do verbo `check`; em `next` ela é
   **E-2**, que recusa a seleção e não classifica a violação. Linha de índice que não casa a gramática de §2.2 é
   **descartada na leitura** e não existe para `next`; quando a linha descartada é a do pai de um
   candidato elegível, o caso cai em **E-3**, e o lint dela é do verbo `check` (`C-4`, `C-9`). Plano
   vivo sem prefixo é `C-7` no `check` e exit 3 do `drain` (`BKL-T5`), nunca exit 3 de `next`, porque
   `next` acha os filhos diretos de um plano pela gramática de ID da `DB-14`.

   Os verbos de escrita reusam a mesma tabela (`DB-37`, segunda cláusula): `status` e `start`
   aplicam **E-2** e **E-3** antes de qualquer escrita e saem exit 3 **sem tocar arquivo**; a recusa
   de `start` por já haver outro item `in-progress` no mesmo pai é **exit 1** (recusa de transição,
   §2.7), não exit 3.

### 2.6 Saída de `next` (forma fixa)

O vencedor é sempre um item com bracket `DP-C`: tarefa de plano **ou** subtarefa de tíquete —
tíquete não tem bracket e nunca é selecionado (`DB-17`). Logo o pai do vencedor é um plano ou um
tíquete, a **linha 2** tem uma forma por tipo de pai (`DB-33`) e as demais linhas são as mesmas nos
dois casos.

Esqueleto:

```
=== PRÓXIMA TAREFA: <ID> — <título> [<modelo> · classe <classe>]
<linha 2: contexto do pai — forma pai-plano ou forma pai-tíquete>
antecessora: <ID> (<estado>; notas em <arquivo>:<l1>-<l2>)
--- dossiê (verbatim, teto DB-7) ---
<seção da tarefa>
--- pendências mecânicas ---
inbox de planos: <n> por drenar · fila de memória: <m> candidato(s) · blocked: <ID> (<razão>), …
```

Linha 2, forma **pai-plano**:

```
plano: P-NNNN — <título> (<done>/<total>) · residência: <arquivo>:<l1>-<l2> · índice: <âncora>
```

Linha 2, forma **pai-tíquete**:

```
tíquete: TK-<n> — <título> (<done>/<total>) · residência: <arquivo>:<l1>-<l2> · índice: <âncora>
```

Campo a campo (`DB-33`; nenhuma célula remete a outra — `DB-18`):

| campo da linha 2 | pai é plano | pai é tíquete |
|---|---|---|
| rótulo | o literal `plano: ` | o literal `tíquete: ` |
| `<ID>` | o `P-NNNN` do cabeçalho `# P-NNNN — <título>` (linha 1 do arquivo do plano) | o `TK-<n>` do cabeçalho `## TK-<n> — <título>` da seção do tíquete no diário |
| `<título>` | o texto após ` — ` no cabeçalho `# P-NNNN — <título>` (linha 1 do arquivo do plano) | o texto após ` — ` no cabeçalho `## TK-<n> — <título>` da seção do tíquete no diário |
| `(<done>/<total>)` | contagem da `DB-36` sobre os cabeçalhos `### <PFX>-T<n>` do arquivo do plano | contagem da `DB-36` sobre os cabeçalhos `### TK-<n><letra>` da seção do tíquete |
| `residência:` | caminho do arquivo do plano, seguido de `:1-<número de linhas do arquivo>` | `docs/DIARIO_DE_OBRAS.md:`, seguido da linha do cabeçalho `## TK-<n>` e da linha imediatamente anterior ao próximo cabeçalho de nível 1 ou 2 (na última seção do arquivo, a última linha do arquivo) |
| `índice:` | 4ª célula da linha do índice do diário cuja 1ª célula é `P-NNNN`; linha ausente → exit 3 (`DB-6`) com a mensagem `linha de índice ausente para P-NNNN` | 4ª célula da linha do índice do diário cuja 1ª célula é `TK-<n>`; linha ausente → exit 3 (`DB-6`) com a mensagem `linha de índice ausente para TK-<n>` |

Linha 3 (`antecessora`, `DB-34`): é o irmão imediatamente anterior ao vencedor entre os filhos
diretos do mesmo pai, na ordem interna da §2.5 regra 4, qualquer que seja o estado dele; o vencedor
que é o primeiro irmão da ordem **não recebe a linha** (a saída passa direto da linha 2 para
`--- dossiê`). `<estado>` é o token da linha `- **Status:**` da antecessora; `notas em
<arquivo>:<l1>-<l2>` é o intervalo do bloco `- **Notas de execução:**` dela, e a antecessora sem
esse bloco produz `antecessora: <ID> (<estado>; sem notas)`.

**Worked example A — pai-plano, vencedor não é o primeiro irmão** (valores ilustrativos; `[…]`
marca elisão **deste exemplo**, não da saída, que imprime a seção verbatim até o teto da `DB-7`):

```
=== PRÓXIMA TAREFA: BKL-T4 — `status`, `start`, `diretiva`: transição e projeções [Sonnet · classe implementacao]
plano: P-0739 — O pickup vira instrumento: `backlog.py` decide a próxima tarefa, fecha a tarefa e mantém o kanban (7/14) · residência: docs/plans/P-0739-backlog-instrumento.md:1-1900 · índice: docs/plans/P-0739-backlog-instrumento.md
antecessora: BKL-T3 (done; notas em docs/plans/P-0739-backlog-instrumento.md:1240-1243)
--- dossiê (verbatim, teto DB-7) ---
[… cabeçalho `### BKL-T4 — … [Sonnet · classe implementacao]` e corpo da seção, verbatim …]
--- pendências mecânicas ---
inbox de planos: 0 por drenar · fila de memória: 1 candidato(s) · blocked: nenhum
```

**Worked example B — pai-tíquete, vencedor é o primeiro irmão** (linha `antecessora` ausente por
`DB-34`; mesmos valores ilustrativos):

```
=== PRÓXIMA TAREFA: TK-90a — Corrigir o parser de data do relatório [Sonnet · classe mecanica]
tíquete: TK-90 — Relatório diário sai com data trocada (0/2) · residência: docs/DIARIO_DE_OBRAS.md:812-871 · índice: docs/DIARIO_DE_OBRAS.md:812
--- dossiê (verbatim, teto DB-7) ---
[… cabeçalho `### TK-90a — … [Sonnet · classe mecanica]` e corpo da seção, verbatim …]
--- pendências mecânicas ---
inbox de planos: 0 por drenar · fila de memória: 1 candidato(s) · blocked: TK-48 (dependencia)
```

**Rodapé `--- pendências mecânicas ---` (`DB-38`):** uma linha, três campos separados por ` · `, na
ordem do esqueleto, sempre os três.

| campo | valor | gramática que conta |
|---|---|---|
| `inbox de planos: <n> por drenar` | `<n>` = número de linhas vivas de `docs/plans/_INBOX.md` | §2.4: começa com `- `, contém caminho que casa `docs/plans/P-[0-9]{4}-<slug>.md`, não começa com `- [drenado ` |
| `fila de memória: <m> candidato(s)` | `<m>` = número de candidatos por promover em `<memory-dir>/_INBOX.md` | `~/.claude/docs/GOVERNANCA_MEMORIAS.md` §8: começa com `- ` — hífen **e** espaço, de modo que a régua markdown `---` não é candidato (`DB-41`) — e não traz `[promovido]` nem `[descartado`. Nenhuma outra exclusão: só essas duas marcas tiram a linha da contagem |
| `blocked: <ID> (<razão>), …` | os itens `blocked`, com a razão de cada um entre parênteses; nenhum item `blocked` → o literal `blocked: nenhum` | linha `- **Status:** \`blocked\` · AAAA-MM-DD · <razão>` (§2.1) |

Os dois caminhos de inbox chegam por parâmetro já resolvido (`DB-1`) e cada contador usa **só** a
gramática do seu arquivo: aplicar a gramática de um ao outro é o desvio que o achado 3 do `AE-7`
mediu. Cada campo tem TF que afirma o valor impresso sobre corpus em que as duas gramáticas dariam
números diferentes (`BKL-T3a`).

### 2.7 Máquina de transições

Tabela da residência única (skill `diario-de-obras`, "Máquina de transições") transcrita para
`_TRANSICOES: dict[tuple[str, str], ...]`; `blocked` exige `--razao`; `done`/`cancelled` são
terminais; `superseded` só para plano. Transição fora da tabela → exit 1 sem escrever nada, e a
recusa de `start` por já haver outro item `in-progress` no mesmo pai é exit 1 pelo mesmo motivo
(`DB-37`). Antes de escrever, `status` e `start` aplicam as condições **E-2** e **E-3** de §2.5 item
6 e saem exit 3 sem tocar arquivo nenhum.

## 3. Superfície do instrumento

```
python .claude/tools/backlog.py next      [--sem-dossie] [--repo]        # somente leitura, exit 0/2/3
python .claude/tools/backlog.py show <ID>                                 # dossiê de um item
python .claude/tools/backlog.py check     [--repo]                        # lint da gramática, exit 0/1
python .claude/tools/backlog.py status <ID> <estado> [--razao "…"] [--nota "…"]   # transição + projeções, exit 0/1/3
python .claude/tools/backlog.py start <ID>                                # = status <ID> in-progress, exit 0/1/3
python .claude/tools/backlog.py drain     [--data AAAA-MM-DD]             # inbox → índice + histórico
python .claude/tools/backlog.py diretiva "Priorize `P-0739` — …"          # reescreve a linha
```

`status` escreve, num ato: linha `Status` do item · apenso em `Notas de execução` (se `--nota`) ·
célula do índice · `<done>/<total>` do pai, plano ou tíquete, pela fórmula da `DB-36` · bloco
`Fila corrente`, com um bullet por pai vivo na forma da §2.3 (`DB-33`). Pai — plano **ou** tíquete —
cujos filhos diretos ficaram todos terminais (`done` ou `cancelled`) entra no rodapé como
"candidato a fechamento" (`DB-4`). `status` e `start` saem **exit 1** quando a transição pedida está
fora da tabela de §2.7 (inclusive a recusa de `start` por outro `in-progress` no mesmo pai) e **exit
3** quando o dado impede a escrita, pelas condições `E-2` e `E-3` de §2.5 item 6; nos dois casos,
nenhum arquivo é tocado (`DB-37`).

## 4. Tarefas

Ordem linear `BKL-T1 → BKL-T2 → BKL-T2a → BKL-T2b → BKL-T2c → BKL-T2d → BKL-T3 → … → BKL-T9`; cada
uma cabe num contexto de executor frio. Quatro tarefas não tocam `backlog.py`: a `BKL-T2a` (`RP-2`)
corrige a gramática de ID de `rdo.py`, e a `BKL-T2b`/`BKL-T2c`/`BKL-T2d` (`RP-3`) consertam o
instrumento de revisão que a `BKL-T2` exercitou pela primeira vez de ponta a ponta. Testes em
`tests/test_backlog.py` sobre fixtures em `tests/fixtures/backlog/` (mini-diário + 2 planos +
inbox), carregando o módulo por `importlib` como `tests/test_telemetria.py`; nunca contra o repo
real. Teto de linhas é instrumentação (`DU-14`), não comando.

### BKL-T1 — A gramática publicada na residência única [Sonnet · classe redacao]
- **Status:** `done` · 2026-09-16
- **Objetivo:** a skill `diario-de-obras` ganha a seção `## Gramática legível por máquina`
  (transcrição de §2.1–§2.4 e §2.7, sem reescrever), e as operações 2, 4 e 5 passam a apontar
  para os verbos de §3 como forma canônica (a prosa atual fica como descrição do efeito).
- **Arquivos-alvo:** `.claude/skills/diario-de-obras/SKILL.md` (via `uow.py`, artefato canônico).
- **Verificação:** `Grep "^## Gramática legível por máquina"` → 1 match; `git status --short` só
  esse arquivo.
- **Pronto quando:** a gramática existe num lugar só e o plano aponta para ela.
- **Notas de execução:**
  - 2026-09-16 `done` — seção `## Gramática legível por máquina` publicada em
  `.claude/skills/diario-de-obras/SKILL.md:125` (transcrição verbatim de §2.1–§2.4 e §2.7 acima);
  operações 2/4/5 de `SKILL.md` `## Operações` passam a apontar para os verbos `status`/
  `diretiva`/`drain` de §3 como forma canônica, prosa original preservada como descrição do
  efeito. Editado via `uow.py open/diff/close` (artefato canônico). Verificação: `Grep "^##
  Gramática legível por máquina" .claude/skills/diario-de-obras/SKILL.md` → 1 match; `git status
  --short` sem arquivo novo além do já sujo na sessão. Consumo: ver `docs/telemetria.tsv`.

### BKL-T2 — `backlog.py`: modelo, parser, `check` e `show` [Sonnet · classe implementacao]
- **Status:** `done` · 2026-09-16 · **com ressalva** (94%, bloqueante nenhuma; única dimensão fora de `conforme`: `registro` `parcial`) — laudo `docs/RDO/laudos/P-0739-BKL-T2.md`, evidência `docs/RDO/evidencia/P-0739-BKL-T2.md` (recorte `--desde 1a9645a`)
- **Depende de:** `BKL-T1`
- **Objetivo:** o núcleo somente-leitura — carregar índice, planos vivos e diário; construir o
  grafo item→tarefas; `check` acusa cada violação `C-1..C-9` com `arquivo:linha`; `show` emite o
  dossiê com teto `DB-7`.
- **Arquivos-alvo:** `.claude/tools/backlog.py` (novo); `tests/test_backlog.py` (novo);
  `tests/fixtures/backlog/` (novo: `DIARIO_DE_OBRAS.md` mínimo, 2 planos, `_INBOX.md`).
- **Gramática que o parser implementa** (inline por `DB-17`/`DB-18`; a residência é a skill
  `diario-de-obras`, seção "Gramática legível por máquina" — igual a esta lista):
  - plano: linha 1 `# P-NNNN — <título>`; nas 20 primeiras linhas `**Status:** \`<estado>\`` e
    `**Prefixo das tarefas no diário:** \`<PFX>-T<n>\``; opcional `**Ordem de execução:** ID → ID`.
  - tarefa de plano: `### <ID> — <título> [<modelo> · classe <classe>]`, `<ID>` =
    `(?:[A-Z0-9]+-)?T[0-9]+[a-z]?` (`DB-14`); bracket completo `[<modelo>[ + dono] · classe
    <classe>[ · teto <n>]]` — ` + dono` e ` · teto <n>` são aceitos e não são violação (`DB-20`).
  - tíquete: `## TK-<n> — <título>` (nível 2, **sem** bracket).
  - subtarefa de tíquete: `### TK-<n><letra> — <título> [<modelo> · classe <classe>]`, dentro da
    seção do tíquete-pai.
  - campos (tarefa, subtarefa, tíquete): 1º bullet `- **Status:** \`<estado>\` · AAAA-MM-DD[ ·
    <razão>]`; opcionais `- **Depende de:**`, `- **Tipo:** bug`, `- **Notas de execução:**` com
    sub-bullets `  - AAAA-MM-DD \`<estado>\` — <texto>`.
  - índice: `| <ID> | <título> | <estado>[ <done>/<total>] | <âncora> |`.
  - `<modelo>` ∈ `Opus|Sonnet|Haiku`; `<classe>` ∈
    `mecanica|implementacao|comportamental|investigacao|redacao`; `<estado>` ∈ vocabulário `DB-3`.
- **Violações de `check`** (vocabulário fechado; cada uma sai como `<código> <arquivo>:<linha> —
  <texto>`): `C-1 cabecalho-fora-da-gramatica` (heading `##`/`###` cujo ID casa `DB-14` mas cuja
  forma não casa nenhuma linha acima — inclui bracket sem `<modelo> ·`) · `C-2 item-sem-status` ·
  `C-3 status-fora-do-vocabulario` · `C-4 celula-do-indice-com-prosa` · `C-5
  divergencia-indice-x-campo` · `C-6 dois-in-progress` (no mesmo plano ou tíquete) · `C-7
  plano-vivo-sem-prefixo` · `C-8 plano-vivo-sem-status` · `C-9 id-do-indice-sem-residencia`
  (linha do índice cujo ID não existe em plano vivo nem no diário; planos `done`/`superseded` do
  índice são isentos, `DB-15`).
- **Passos:** (1) `tests/fixtures/backlog/` com um caso verde (tudo conforme) e um caso vermelho
  que dispara `C-1..C-9` uma vez cada; (2) `backlog.py`: dataclasses `Plano`, `Item`,
  `LinhaIndice`, `Violacao`; funções `carregar(repo: Path) -> Modelo`, `check(modelo) ->
  list[Violacao]`, `show(modelo, id: str) -> str`; a CLI `check`/`show` só embrulha (`DB-1`);
  (3) testes abaixo; (4) rodar `check` no repo real e colar a lista na nota de execução.
- **Testes:** TF parser (3 formas de ID de `DB-14`; campo `Status` com e sem razão; heading `###`
  legado sem bracket → `C-1`); TF `check` vermelho uma vez por código `C-1..C-9`; TF `check` verde
  na fixture conforme; TF `show` trunca em 8.000 chars / 120 linhas com ponteiro `arquivo:l1-l2`;
  TR `carregar` nunca abre `*_HISTORICO.md` (monkeypatch em `Path.open`/`open` que falha se o
  caminho casar `_HISTORICO`).
- **Contingências:** se o repo real tiver forma que não casa nenhuma linha da gramática → `C-1`
  com `arquivo:linha`, nunca bloqueio (`DB-19`); se a gramática admitir duas leituras para a
  mesma linha real → parar e sinalizar `blocked motivo=premissa defeito=ambiguidade` citando a
  linha e as duas leituras (`G-REPLAN`).
- **Não fazer:** não editar diário, planos, inbox ou histórico (esta tarefa é somente-leitura);
  não tocar `rdo.py`; não decidir migração (é a `BKL-T6`); não ler `docs/DIARIO_DE_OBRAS.md` além
  do que o parser lê por código.
- **Verificação:** `python -m pytest tests/test_backlog.py -q` verde; `python .claude/tools/backlog.py check` no repo real → exit 1 e a lista colada na nota (esperada: `C-1` em `TK-54a`/`TK-54b`, `C-2` nos itens vivos sem `Status`, `C-4` nas células narrativas do índice, `C-3` em `backlog`/`decidido em parte`), insumo da `BKL-T6`.
- **Pronto quando:** `check` e `show` funcionam sobre a fixture e a lista de defeitos reais está na nota.
- **Notas de execução:**
  - 2026-09-16 `blocked` — nenhum arquivo criado; contradição na tabela §2.1 (`idem` na coluna
    "cabeçalho" do tíquete), achado `AE-1`.
  - 2026-09-16 `ready` — `RP-1`: gramática de tíquete/subtarefa fechada (`DB-17`), violações
    `C-1..C-9` inline, contingência de forma desconhecida (`DB-19`).
  - 2026-09-16 `review` — entregues `.claude/tools/backlog.py` (584 linhas: dataclasses `Plano`,
    `Item`, `LinhaIndice`, `Violacao`, `Modelo`; `carregar`/`check`/`show`; CLI fina por `DB-1`),
    `tests/test_backlog.py` (8 TF/TR, verdes) e `tests/fixtures/backlog/{verde,vermelho}/`.
    Nenhum artefato de registro tocado (tarefa somente-leitura sobre diário/planos/inbox).
    **Defeitos reais do repo** (`python .claude/tools/backlog.py check` → exit 1, 274 violações,
    re-derivado pelo orquestrador): `C-1`=153 · `C-2`=79 · `C-7`=15 · `C-8`=14 · `C-4`=8 ·
    `C-9`=3 · `C-3`=2; `C-5` e `C-6` não ocorrem hoje — quase nenhum item vivo tem campo
    `Status`, então não há divergência índice×campo nem dois `in-progress` detectáveis. Confirma
    a expectativa do card (`C-1` em `TK-54a`/`TK-54b`; `C-3` em `backlog` e `decidido em parte`)
    e é o insumo da `BKL-T6`. Achado fora de escopo, não corrigido:
    `check-readme.ps1` acusa divergência pré-existente README × `GOVERNANCA.md` §7 (16 linhas × 17
    itens), sem relação com os alvos desta tarefa. Consumo: ver `docs/telemetria.tsv`.
  - 2026-09-16 `blocked` — razão `premissa`, achado `AE-2`: a rodada de revisão não roda porque o
    `review_evidence.py` não localiza ID prefixado (`rdo.py:79-81`). **O entregável não é
    descartado** — o bloqueio é da revisão. Decisão do dono no pickup: anotar e escalar. Próxima
    tarefa do plano é a `RP-2` (`pantonic-planner`), não a `BKL-T3`.
  - 2026-09-16 `review` — `RP-2`: bloqueio levantado sem tocar o entregável. O gate de revisão vale
    para ID prefixado (`DB-21`) e a correção do instrumento virou a tarefa `BKL-T2a` (`DB-22`). Esta
    tarefa volta ao estado em que estava antes do bloqueio (`review`): quem a leva a `done` é o
    `scrum-master`, depois do veredito do `pantonic-reviewer`, e a rodada de revisão só é despachada
    **após** a `BKL-T2a` (sem ela, `review_evidence.py` não monta o dossiê).

### BKL-T2a — `rdo.py`: a gramática de ID aceita prefixo e aceite do dono [Sonnet · classe implementacao]
- **Status:** `done` · 2026-09-16 · **aprovado** (100%, bloqueante nenhuma) — laudo `docs/RDO/laudos/P-0739-BKL-T2a.md`, evidência `docs/RDO/evidencia/P-0739-BKL-T2a.md` (recorte `--desde 6d7433c`). Entrega verde (`pantonic-executor`): 4 testes novos em
  `tests/test_rdo.py`, `python -m pytest tests/ -q` → `98 passed`, e
  `review_evidence.py --tarefa BKL-T2` → `review_evidence: OK` (exit 0) — o dossiê de evidência
  está destravado. Nenhuma contingência acionada; 3 arquivos tocados, exatamente os prescritos.
  Consumo: ver `docs/telemetria.tsv` (`BKL-T2a`).
- **Depende de:** `DB-14`, `DB-20`, `DB-21`, `DB-22`, `DB-23`, `DB-24` (`RP-2`). Nenhuma tarefa é
  insumo: a entrega da `BKL-T2` já está no repositório e esta tarefa não a lê nem a edita.
- **Objetivo:** `extrair_dossie` passa a localizar tarefa de plano com ID prefixado (`BKL-T2`,
  `AUT-T4`, `CTX-T1d`) e cabeçalho com ` + dono`, destravando `review_evidence.py` e `rdo.py close`
  para os três planos vivos.
- **Camada e fronteira:** camada de instrumento (`.claude/tools/`), fora das camadas de produto. A
  tarefa toca **três** arquivos e nenhum outro: `.claude/tools/rdo.py`, `tests/test_rdo.py`,
  `CHANGELOG.md`. Não importa, não edita e não lê `backlog.py`; não edita `review_evidence.py`
  (que só **reusa** a função corrigida); não edita plano, diário nem inbox.
- **Arquivos-alvo:**
  - `.claude/tools/rdo.py:79` — `_ID_HEADER_RE = re.compile(r"^### (T[0-9]+[a-z]?)(?=[\s—])")`.
  - `.claude/tools/rdo.py:81-85` — bloco `_HEADER_BRACKET_RE = re.compile(` … `)`.
  - `tests/test_rdo.py` — apenso de 4 testes ao **final** do arquivo.
  - `CHANGELOG.md` — uma linha sob `## [Não lançado]` (`CHANGELOG.md:17`), por `DB-13` (sem bump,
    sem tag, nenhum derivado tocado).
- **Fatos verificados na `RP-2` (não re-apurar, não re-grepar):**
  - `extrair_dossie` (`.claude/tools/rdo.py:186`) é o **único** ponto de casamento do cabeçalho:
    usa `_ID_HEADER_RE` em `rdo.py:198` e `_HEADER_BRACKET_RE` em `rdo.py:206`. `grep -n 'T\[0-9\]'`
    não casa mais nada em `rdo.py` e não casa nada em `review_evidence.py`.
  - O ID é comparado por **igualdade exata** (`rdo.py:199`: `if m and m.group(1) == tarefa_id`) —
    por isso o grupo 1 tem de capturar o ID inteiro, prefixo incluído.
  - Consumidores da função, ambos com os mesmos kwargs: `review_evidence.py:407` e `rdo.py:576`
    (`cmd_close`), os dois com `esquema_legado=False, modelo_legado=None, classe_legado=None`.
  - `_ID_LAUDO_RE` (`rdo.py:80`, `^[A-Za-z0-9][A-Za-z0-9_-]*$`, validação de `--plano`/`--tarefa` do
    `laudo` em `rdo.py:454-455`) **já aceita** `BKL-T2`: não é defeito e não se toca.
  - `tests/test_rdo.py:291` define `_escrever_plano_sintetico(caminho: Path, cabecalho: str)`, que
    escreve um plano com o cabeçalho recebido e os quatro campos que `extrair_dossie` exige
    (`Objetivo`, `Arquivos-alvo`, `Verificação`, `Pronto quando`); `_load_rdo()` (`test_rdo.py:38`)
    carrega o módulo por caminho.
  - `.claude/tools/` **não** está na lista `ask` de `.claude/settings.json:4-7` (só as quatro
    skills): editar por `Edit` direto. **Não abrir UoW** (`uow.py`) para esta tarefa.
- **Texto novo, literal** (substitui as duas definições; os nomes de grupo `id`, `titulo`, `modelo`,
  `classe`, `sufixo` são preservados exatamente como estão):
  ```python
  _ID_HEADER_RE = re.compile(r"^### ((?:[A-Z0-9]+-)?T[0-9]+[a-z]?)(?=[\s—])")
  _ID_LAUDO_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")  # identificador, nunca caminho
  _HEADER_BRACKET_RE = re.compile(
      r"^### (?P<id>(?:[A-Z0-9]+-)?T[0-9]+[a-z]?) — (?P<titulo>.+?) "
      r"\[(?P<modelo>Opus|Sonnet|Haiku)(?: \+ dono)? · classe (?P<classe>.+?)"
      r"(?: · teto (?:prescrito )?[0-9]+)?\](?P<sufixo>.*)$"
  )
  ```
- **Passos:**
  1. Substituir a linha `rdo.py:79` pela primeira linha do bloco acima (a linha `_ID_LAUDO_RE` fica
     idêntica ao que já está em `rdo.py:80`; está transcrita só para fixar a vizinhança).
  2. Substituir o bloco `rdo.py:81-85` pelo `_HEADER_BRACKET_RE` do bloco acima.
  3. Apensar ao final de `tests/test_rdo.py` os quatro testes da seção **Testes**, cada um com
     `rdo = _load_rdo()`, `plano = tmp_path / "plano.md"` e `_escrever_plano_sintetico(plano, …)`.
  4. Rodar a verificação 1 e a verificação 2 desta tarefa.
  5. Apensar a linha do `CHANGELOG.md` sob `## [Não lançado]`: ``- `rdo.py`: `extrair_dossie` aceita
     ID de tarefa prefixado (`(?:[A-Z0-9]+-)?T[0-9]+[a-z]?`, `DB-14`) e bracket com ` + dono`
     (`DB-20`) — `review_evidence.py` e `rdo.py close` passam a funcionar para `AUT-*`/`CTX-*`/
     `BKL-*` (`P-0739` `BKL-T2a`, `DB-22`).``
  6. Rodar a verificação 3 e colar a linha de saída dela na nota de execução.
- **Testes** (nomes fixos; todos com `tmp_path`):
  - `test_tf_extrair_dossie_id_prefixado` — TF: cabeçalho
    `### BKL-T2 — Tarefa sintética [Sonnet · classe implementacao]`; chamada
    `rdo.extrair_dossie(plano, "BKL-T2", esquema_legado=False, modelo_legado=None,
    classe_legado=None)`; afirma `dossie.tarefa_id == "BKL-T2"`, `dossie.modelo == "Sonnet"`,
    `dossie.classe == "implementacao"`, `dossie.esquema == "padrao"`.
  - `test_tf_extrair_dossie_id_prefixado_com_letra_e_teto_legado` — TF: cabeçalho
    `### CTX-T1d — Tarefa sintética [Opus · classe redacao · teto 30]`; afirma
    `dossie.tarefa_id == "CTX-T1d"`, `dossie.classe == "redacao"`, `dossie.esquema == "padrao"`.
  - `test_tf_extrair_dossie_bracket_com_aceite_do_dono` — TF: cabeçalho
    `### BKL-T9 — Tarefa sintética [Opus + dono · classe redacao]`; afirma `dossie.modelo == "Opus"`,
    `dossie.classe == "redacao"`, `dossie.esquema == "padrao"` (` + dono` é aceito e descartado,
    `DB-20`).
  - `test_tr_extrair_dossie_id_casa_por_igualdade_exata` — TR: plano sintético com um único
    cabeçalho `### BKL-T1 — Tarefa sintética [Sonnet · classe redacao]`; afirma
    `pytest.raises(rdo.RdoValidationError)` ao pedir `"T1"` e `pytest.raises(rdo.RdoValidationError)`
    ao pedir `"BKL-T2"` — prefixo nunca casa por sufixo nem por ID parcial.
- **Restrições desta tarefa (copiadas inline):**
  - Não alterar a assinatura de `extrair_dossie` nem o nome de nenhum kwarg: `review_evidence.py:407`
    e `rdo.py:576` chamam com `esquema_legado`/`modelo_legado`/`classe_legado`.
  - Preservar os nomes de grupo `id`, `titulo`, `modelo`, `classe`, `sufixo` em `_HEADER_BRACKET_RE`.
  - Não tocar `_ID_LAUDO_RE`, `_CLASSE_ALIASES`, `_normalizar_classe`, `_HEADER_LEGADO_TITULO_FMT`,
    `_SECTION_BREAK_RE`, `_CAMPO_RE`, nem o ramo legado (`rdo.py:219-245`).
  - Não gerar RDO nem dossiê de evidência retroativo de tarefa já fechada (`DB-23`).
  - Não escrever em `docs/RDO/` — a verificação 3 grava em caminho temporário e apaga o arquivo.
  - Sem bump de versão e sem tag; nenhum projeto derivado é tocado (`DB-13`).
- **Não fazer:** não editar os textos de `help` dos `add_argument` (`rdo.py:680`, `rdo.py:721`,
  `review_evidence.py:454` dizem "ex.: T18"/"ex.: T9a") — são exemplos, não gramática; não estender
  `_ID_HEADER_RE` para `TK-<n><letra>` (subtarefa de tíquete mora no diário, e `rdo.py` só lê
  plano); não renomear ID de tarefa em plano nenhum; não editar `backlog.py`, `review_evidence.py`,
  `docs/DIARIO_DE_OBRAS.md`, `docs/plans/*`; não abrir UoW.
- **Contingências:**
  - se o texto de `rdo.py:79` ou do bloco `rdo.py:81-85` não for **literalmente** o transcrito em
    **Arquivos-alvo** → parar e sinalizar `blocked` razão `premissa`, citando o texto encontrado.
  - se um teste **já existente** falhar citando `_ID_HEADER_RE`, `_HEADER_BRACKET_RE` ou
    `extrair_dossie` → seguir com o ajuste desse teste ao texto novo e registrar o ajuste na nota
    de execução.
  - se um teste já existente falhar **sem** citar nenhum dos três → parar e sinalizar `blocked`
    razão `dependencia`, nomeando o teste e a mensagem.
  - se a verificação 3 falhar por motivo diferente de localização da tarefa (bateria de guardas,
    `git`, `pwsh`) → seguir com a tarefa e colar a mensagem na nota: esta tarefa afirma que o dossiê
    é **localizado**, não que a bateria de guardas está verde.
- **Verificação:**
  1. `python -m pytest tests/test_rdo.py tests/test_review_evidence.py -q` → verde, com os 4 testes
     novos entre os coletados.
  2. `python -m pytest tests/ -q` → verde.
  3. `python .claude/tools/review_evidence.py --plano docs/plans/P-0739-backlog-instrumento.md --tarefa BKL-T2 --desde HEAD --out $env:TEMP\rdo-smoke-BKL-T2.md` → stdout com `review_evidence: OK` e exit 0; em seguida `Remove-Item $env:TEMP\rdo-smoke-BKL-T2.md`.
  4. `git status --short` → exatamente três caminhos: `.claude/tools/rdo.py`, `tests/test_rdo.py`,
     `CHANGELOG.md`.
- **Pronto quando:** os quatro testes novos passam, `python -m pytest tests/ -q` está verde e a
  verificação 3 sai com `review_evidence: OK` para `--tarefa BKL-T2`.
- **Fora do escopo desta tarefa:** a rodada de revisão da `BKL-T2` (é do `pantonic-reviewer`, e roda
  depois desta tarefa); RDO ou evidência retroativa de `CTX-*`/`AUT-*` (`DB-23`); qualquer mudança
  em `.claude/tools/backlog.py` (é a `BKL-T3`).

### BKL-T2b — `review_evidence.py`: o campo `Arquivos-alvo` lido por gramática de caminho [Sonnet · classe implementacao]
- **Status:** `done` · 2026-09-16 · revisão fechada (`pantonic-reviewer`, laudo
  `docs/RDO/laudos/P-0739-BKL-T2b.md`): **aprovado 100%**, bloqueante nenhuma, as sete dimensões
  `conforme`. Entrega verde (`pantonic-executor`): `_eh_caminho`/`_classificar_campo_alvos`/`extrair_literais_nao_caminho`/`_forcar_utf8` em
  `.claude/tools/review_evidence.py`, 4 testes novos em `tests/test_review_evidence.py`
  (`13 passed` → `17 passed`), `python -m pytest tests/ -q` → `102 passed` (piso 98), e a
  verificação 3 imprime `['.claude/tools/rdo.py', 'tests/test_rdo.py', 'CHANGELOG.md']`.
  Nenhuma contingência acionada; 3 arquivos tocados, exatamente os prescritos.
  Consumo: ver `docs/telemetria.tsv` (`BKL-T2b`; rodada de revisão em `BKL-T2bc-revisao`).
- **Depende de:** `DB-13`, `DB-19`, `DB-26`, `DB-27` (`RP-3`). Tarefa anterior cujo produto usa:
  `BKL-T2a` (já entregue no repositório — sem ela `extrair_dossie` não localiza ID prefixado).
- **Objetivo:** `extrair_arquivos_alvo` passa a reconhecer arquivo de raiz (`CHANGELOG.md`) e a
  recusar literal que não é caminho (trecho de regex, cabeçalho de seção), e a seção `## Escopo`
  lista o que descartou; `main` força UTF-8 em `stdout`/`stderr`.
- **Camada e fronteira:** camada de instrumento (`.claude/tools/`), fora das camadas de produto. A
  tarefa toca **três** arquivos e nenhum outro: `.claude/tools/review_evidence.py`,
  `tests/test_review_evidence.py`, `CHANGELOG.md`. Não edita `rdo.py` (só **reusa**
  `extrair_dossie`), não edita `backlog.py`, plano, diário nem inbox.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py:19-24` — parágrafo do docstring que começa em "Limitação
    conhecida e aceita da extração de arquivos-alvo:".
  - `.claude/tools/review_evidence.py:78-90` — bloco `def extrair_arquivos_alvo(campos: dict)` até
    `return list(vistos.keys())`.
  - `.claude/tools/review_evidence.py:446` — linha `def main(argv: list[str] | None = None) -> int:`.
  - `tests/test_review_evidence.py` — apenso de 4 testes ao final do arquivo.
  - `CHANGELOG.md` — uma linha sob `## [Não lançado]`, por `DB-13`.
- **Fatos verificados na `RP-3` (não re-apurar, não re-grepar):**
  - `_parsear_campos` (`.claude/tools/rdo.py:151-183`) junta as linhas de um campo com **espaço**
    (`rdo.py:179`): a estrutura de bullets do campo não chega ao instrumento. Por isso a regra é
    por literal entre crases, não por linha (`DB-27`).
  - `_BACKTICK_RE` (`review_evidence.py:56`) e `_LINHA_REF_RE` (`review_evidence.py:57`) já existem
    e são reusados como estão.
  - `extrair_arquivos_alvo` tem dois chamadores, ambos neste arquivo: `montar_documento`
    (`review_evidence.py:417`) e o teste `tests/test_review_evidence.py:163`. A assinatura
    `(campos: dict) -> list[str]` é preservada.
  - `sys.stdout.reconfigure` existe em CPython ≥ 3.7 para stream de texto real; objeto de captura
    de teste pode não ter o método — daí o `getattr` do texto novo.
- **Texto novo, literal** (substitui o bloco `review_evidence.py:78-90` inteiro):
  ```python
  _CAMINHO_RE = re.compile(r"^[A-Za-z0-9_.][A-Za-z0-9_./\\-]*$")
  _EXTENSAO_RE = re.compile(r"\.[A-Za-z0-9]+$")


  def _eh_caminho(candidato: str) -> bool:
      """Gramática de caminho da `DB-27` (`P-0739`): sem espaço e sem metacaractere de regex, e
      com extensão, barra, ou barra final. Recusa `_ID_HEADER_RE = re.compile(...)` (espaço) e
      `BKL-T9` (sem extensão e sem barra); aceita `CHANGELOG.md` e `tests/fixtures/backlog/`."""
      if not _CAMINHO_RE.fullmatch(candidato):
          return False
      return (
          "/" in candidato
          or "\\" in candidato
          or candidato.endswith("/")
          or bool(_EXTENSAO_RE.search(candidato))
      )


  def _classificar_campo_alvos(campos: dict) -> tuple[list[str], list[str]]:
      """Parte o campo `Arquivos-alvo`/`Entregável` em (alvos, literais descartados), por literal
      entre crases (`DB-27`). Descartado é fato impresso, nunca bloqueio (`DB-19`)."""
      texto = campos.get("arquivos-alvo") or campos.get("entregavel") or ""
      alvos: dict[str, None] = {}
      descartados: list[str] = []
      for match in _BACKTICK_RE.finditer(texto):
          bruto = match.group(1).strip()
          candidato = _LINHA_REF_RE.sub("", bruto)
          if _eh_caminho(candidato):
              alvos.setdefault(candidato, None)
          else:
              descartados.append(bruto)
      return list(alvos.keys()), descartados


  def extrair_arquivos_alvo(campos: dict) -> list[str]:
      """Caminhos declarados no campo `Arquivos-alvo`/`Entregável` do dossiê, na ordem em que
      aparecem, sem repetição."""
      return _classificar_campo_alvos(campos)[0]


  def extrair_literais_nao_caminho(campos: dict) -> list[str]:
      """Literais entre crases do mesmo campo que não são caminho pela `DB-27` — vão para a seção
      `## Escopo` como transparência da extração."""
      return _classificar_campo_alvos(campos)[1]


  def _forcar_utf8(stream) -> None:
      """Console cp1252 do Windows estoura `UnicodeEncodeError` ao imprimir `→` do documento; o
      arquivo de `--out` já é gravado em UTF-8. `reconfigure` só existe em stream de texto real."""
      reconfigure = getattr(stream, "reconfigure", None)
      if reconfigure is not None:
          reconfigure(encoding="utf-8", errors="replace")
  ```
- **Texto novo, literal** (parágrafo que substitui `review_evidence.py:19-24`, dentro do docstring
  do módulo):
  ```
  Forma canônica do campo `Arquivos-alvo` (`P-0739` `DB-26`/`DB-27`): um caminho por bullet, o
  caminho como primeiro literal entre crases do bullet, com sufixo opcional `:<linha>`. A extração
  é mecânica e por **literal**, não por linha — `_parsear_campos` (`.claude/tools/rdo.py:151-183`)
  junta as linhas de um campo com espaço, e a estrutura de bullets não chega até aqui. Todo literal
  entre crases é candidato; vira alvo só quando casa `_CAMINHO_RE` e tem extensão, barra ou termina
  em `/`. Literal descartado (trecho de regex, cabeçalho de seção) sai na seção `## Escopo` como
  "não reconhecido como caminho", nunca como bloqueio. Limitação que permanece e é do revisor, não
  deste script: caminho citado em prosa negativa dentro do campo ("não editar `x/y.py`") conta como
  alvo declarado — por isso a forma canônica manda a citação negativa para `Não fazer`.
  ```
- **Passos:**
  1. Substituir o parágrafo `review_evidence.py:19-24` pelo parágrafo literal acima.
  2. Substituir o bloco `review_evidence.py:78-90` pelo bloco de código literal acima.
  3. Inserir, como primeiras duas linhas do corpo de `main` (`review_evidence.py:446`, antes de
     `parser = argparse.ArgumentParser(`): `_forcar_utf8(sys.stdout)` e `_forcar_utf8(sys.stderr)`.
  4. Em `_renderizar`, acrescentar o parâmetro somente-nomeado
     `literais_descartados: list[str] | None = None` (na lista de parâmetros somente-nomeados que
     começa em `review_evidence.py:322`) e inserir, imediatamente depois da linha
     `linhas.append(f"- Arquivos-alvo declarados: {alvos_txt}")` (`review_evidence.py:358`), este
     bloco literal, com a indentação de quatro espaços do corpo da função:
     ```python
         if literais_descartados:
             descartados_txt = ", ".join(f"`{c}`" for c in literais_descartados)
             linhas.append(
                 f"- Literais não reconhecidos como caminho "
                 f"({len(literais_descartados)}): {descartados_txt}"
             )
     ```
  5. Em `montar_documento`, inserir a linha
     `literais_descartados = extrair_literais_nao_caminho(dossie.campos)` logo depois de
     `arquivos_alvo = extrair_arquivos_alvo(dossie.campos)` (`review_evidence.py:417`), e
     acrescentar `literais_descartados=literais_descartados,` à chamada de `_renderizar`
     (`review_evidence.py:429-443`), depois de `arquivos_alvo=arquivos_alvo,`.
  6. Apensar ao final de `tests/test_review_evidence.py` os quatro testes da seção **Testes**.
  7. Rodar as verificações 1 e 2.
  8. Apensar a linha do `CHANGELOG.md` sob `## [Não lançado]`: ``- `review_evidence.py`: campo
     `Arquivos-alvo` lido por gramática de caminho (`DB-27`) — arquivo de raiz volta a ser alvo,
     literal de regex deixa de ser; `stdout`/`stderr` forçados a UTF-8 (`P-0739` `BKL-T2b`).``
  9. Rodar a verificação 3.
- **Testes** (nomes fixos, apensos a `tests/test_review_evidence.py`):
  - `test_tf_extrair_arquivos_alvo_aceita_arquivo_de_raiz_e_recusa_literal_de_regex` — TF: `campos`
    com `arquivos-alvo` = ``- `.claude/tools/rdo.py:79` — `_ID_HEADER_RE = re.compile(x)` - `CHANGELOG.md` — uma linha sob `## [Não lançado]` (`CHANGELOG.md:17`)``;
    afirma `extrair_arquivos_alvo(campos) == [".claude/tools/rdo.py", "CHANGELOG.md"]`.
  - `test_tr_extrair_literais_nao_caminho_lista_o_descartado` — TR: mesmos `campos`; afirma que
    `"## [Não lançado]"` está na lista devolvida e que algum item contém `"re.compile"`.
  - `test_tr_extrair_arquivos_alvo_recusa_id_de_tarefa_e_de_decisao` — TR: `campos` com
    `arquivos-alvo` = ``ver `BKL-T9` e `DB-13`.``; afirma `extrair_arquivos_alvo(campos) == []`.
  - `test_tf_secao_escopo_lista_literais_nao_reconhecidos_como_caminho` — TF de ponta a ponta:
    `_init_repo_com_baseline`, `_escrever_plano(plano, "cria `src/a.py`; ver `_RE = re.compile(x)`.")`,
    `montar_documento(plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE)`; afirma que o
    documento contém `"Literais não reconhecidos como caminho (1)"`.
- **Restrições desta tarefa (copiadas inline):**
  - Preservar a assinatura `extrair_arquivos_alvo(campos: dict) -> list[str]`: `montar_documento` e
    `tests/test_review_evidence.py:163` a chamam assim.
  - Não alterar `_BACKTICK_RE`, `_LINHA_REF_RE`, `coletar_arquivos_tocados`, `confrontar_escopo`,
    `montar_trechos`, `rodar_bateria_guardas` nem a seção `## Guardas`.
  - Não editar `.claude/tools/rdo.py` nem `tests/test_rdo.py` (a gramática de ID mora lá e já está
    correta — `DB-22`).
  - `.claude/tools/` não está na lista `ask` de `.claude/settings.json`: editar por `Edit` direto,
    **sem** abrir UoW (`uow.py`).
  - Sem bump de versão e sem tag; nenhum projeto derivado é tocado (`DB-13`).
- **Não fazer:** não tentar interpretar prosa negativa dentro do campo (a limitação é do revisor,
  e está escrita no docstring novo); não reescrever o campo `Arquivos-alvo` de card nenhum de plano
  nenhum; não gerar dossiê de evidência retroativo (`DB-23`); não editar `docs/DIARIO_DE_OBRAS.md`,
  `docs/telemetria.tsv`, `docs/plans/*`, `docs/RDO/*`.
- **Contingências:**
  - se o texto de `review_evidence.py:78-90` ou do parágrafo `19-24` não for literalmente o
    transcrito → parar e sinalizar `blocked` razão `premissa`, citando o texto encontrado.
  - se `test_tr_extrair_arquivos_alvo_ignora_texto_sem_barra_e_referencia_de_linha`
    (`tests/test_review_evidence.py:152`) falhar → seguir com o ajuste das asserções desse teste ao
    comportamento da `DB-27` (arquivo de raiz com extensão passa a ser alvo), preservando a
    asserção sobre remoção do sufixo `:<linha>`, e registrar o ajuste na nota de execução.
  - se outro teste já existente falhar sem citar `extrair_arquivos_alvo`, `_renderizar` ou
    `montar_documento` → parar e sinalizar `blocked` razão `dependencia`, nomeando o teste e a
    mensagem.
- **Verificação:**
  1. `python -m pytest tests/test_review_evidence.py -q` → verde, com os 4 testes novos entre os
     coletados.
  2. `python -m pytest tests/ -q` → verde.
  3. Da raiz do repositório:
     `python -c "import importlib.util, pathlib; spec = importlib.util.spec_from_file_location('re_', '.claude/tools/review_evidence.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); rdo = m._load_rdo(pathlib.Path('.')); d = rdo.extrair_dossie(pathlib.Path('docs/plans/P-0739-backlog-instrumento.md'), 'BKL-T2a', esquema_legado=False, modelo_legado=None, classe_legado=None); print(m.extrair_arquivos_alvo(d.campos))"`
     → imprime exatamente `['.claude/tools/rdo.py', 'tests/test_rdo.py', 'CHANGELOG.md']`.
  4. `git status --short` → exatamente três caminhos: `.claude/tools/review_evidence.py`,
     `tests/test_review_evidence.py`, `CHANGELOG.md`.
- **Pronto quando:** os quatro testes novos passam, `python -m pytest tests/ -q` está verde e a
  verificação 3 imprime a lista de três caminhos acima, nessa ordem.
- **Fora do escopo desta tarefa:** a atribuição de arquivo tocado a outra tarefa e o balde de
  registro da orquestração (é a `BKL-T2c`); o campo de achado de processo do laudo (é a `BKL-T2d`);
  qualquer mudança em `.claude/tools/backlog.py` (é a `BKL-T3`).

### BKL-T2c — `review_evidence.py`: atribuição por tarefa no confronto de escopo [Sonnet · classe implementacao]
- **Status:** `done` · 2026-09-16 · revisão fechada (`pantonic-reviewer`, laudo
  `docs/RDO/laudos/P-0739-BKL-T2c.md`): **aprovado 100%**, bloqueante nenhuma, as sete dimensões
  `conforme`. Entrega verde (`pantonic-executor`): os quatro baldes da `DB-25` em
  `confrontar_escopo`, `_REGISTRO_ORQUESTRACAO` com exatamente os quatro itens prescritos, 4 testes
  novos em `tests/test_review_evidence.py` (`17 passed` → `21 passed`), suíte `106 passed`
  (piso 102). **Contingência 2 do card acionada** — prevista no próprio dossiê, logo `rota`
  `conforme`: a asserção de `test_escopo_violado_gera_fato_sem_inventar_parcial` foi ajustada
  porque a frase do fato virou "fora dos alvos e sem atribuição".
  Consumo: ver `docs/telemetria.tsv` (`BKL-T2c`; rodada de revisão em `BKL-T2bc-revisao`).
- **Depende de:** `DB-13`, `DB-19`, `DB-25` (`RP-3`). Tarefa anterior cujo produto usa: `BKL-T2b`
  (a extração corrigida de `extrair_arquivos_alvo` é insumo do mapa de alvos, e o `→` que esta
  tarefa imprime depende do UTF-8 forçado lá).
- **Objetivo:** a seção `## Escopo` do dossiê classifica todo arquivo tocado em quatro baldes
  (`DB-25`) e só o balde sem atribuição pesa no veredito mecânico.
- **Camada e fronteira:** camada de instrumento (`.claude/tools/`), fora das camadas de produto. A
  tarefa toca **três** arquivos e nenhum outro: `.claude/tools/review_evidence.py`,
  `tests/test_review_evidence.py`, `CHANGELOG.md`. Não edita `rdo.py`, `backlog.py`, plano, diário
  nem inbox.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py:172-197` — bloco `def confrontar_escopo(` até
    `return {"fora_dos_alvos": fora, "veredito": None}`.
  - `.claude/tools/review_evidence.py:360-368` — bloco de renderização do veredito da seção
    `## Escopo`, dentro de `_renderizar`.
  - `.claude/tools/review_evidence.py:420` — linha `escopo = confrontar_escopo(tocados, arquivos_alvo, root)`.
  - `tests/test_review_evidence.py` — apenso de 1 helper e 4 testes ao final do arquivo.
  - `CHANGELOG.md` — uma linha sob `## [Não lançado]`, por `DB-13`.
- **Fatos verificados na `RP-3` (não re-apurar, não re-grepar):**
  - `_load_rdo(root)` (`review_evidence.py:68`) carrega `rdo.py` por caminho e devolve o módulo;
    `_ID_HEADER_RE` é atributo do módulo e é a **única** residência da gramática de ID (`DB-22`).
  - `extrair_dossie` compara o ID por igualdade exata (`rdo.py:199`) e levanta
    `rdo.RdoValidationError` quando a tarefa não tem os campos obrigatórios (`rdo.py:254-263`).
  - `_normalizar_separador` (`review_evidence.py:160`) e `_eh_alvo_diretorio`
    (`review_evidence.py:164`) já existem e são reusados como estão.
  - `confrontar_escopo` tem um chamador de produção (`review_evidence.py:420`) e é chamado
    indiretamente pelos testes via `montar_documento`.
- **Texto novo, literal** (substitui o bloco `review_evidence.py:172-197` inteiro):
  ```python
  _REGISTRO_ORQUESTRACAO = (
      "docs/DIARIO_DE_OBRAS.md",
      "docs/telemetria.tsv",
      "docs/plans/",
      "docs/RDO/",
  )


  def _eh_registro_orquestracao(caminho: str) -> bool:
      """Balde (3) da `DB-25` (`P-0739`): arquivo que a orquestração escreve por ofício — kanban,
      telemetria, plano, RDO. Não é atribuível a tarefa nenhuma e por isso não pesa no veredito;
      aparece nomeado na seção `## Escopo`. Item terminado em `/` casa por prefixo."""
      alvo = _normalizar_separador(caminho)
      for item in _REGISTRO_ORQUESTRACAO:
          if item.endswith("/"):
              if alvo.startswith(item):
                  return True
          elif alvo == item:
              return True
      return False


  def mapear_alvos_de_outras_tarefas(plano_path: Path, tarefa_id: str, root: Path) -> dict[str, str]:
      """Balde (2) da `DB-25`: `git` não sabe qual tarefa tocou qual arquivo, mas o plano sabe qual
      tarefa declarou qual alvo. Percorre os cabeçalhos `### <ID>` do mesmo plano com a gramática
      de ID que mora em `rdo.py` (residência única, `DB-22`), extrai o dossiê de cada tarefa que
      não seja `tarefa_id` e devolve `caminho -> primeiro ID que o declara`, na ordem do arquivo.
      Tarefa cujo dossiê não extrai é pulada: atribuição ausente nunca bloqueia (`DB-19`)."""
      rdo = _load_rdo(root)
      mapa: dict[str, str] = {}
      for linha in Path(plano_path).read_text(encoding="utf-8").splitlines():
          m = rdo._ID_HEADER_RE.match(linha)
          if not m or m.group(1) == tarefa_id:
              continue
          try:
              dossie = rdo.extrair_dossie(
                  plano_path,
                  m.group(1),
                  esquema_legado=False,
                  modelo_legado=None,
                  classe_legado=None,
              )
          except rdo.RdoValidationError:
              continue
          for caminho in extrair_arquivos_alvo(dossie.campos):
              mapa.setdefault(_normalizar_separador(caminho), m.group(1))
      return mapa


  def confrontar_escopo(
      tocados: list[str],
      arquivos_alvo: list[str],
      root: Path,
      alvos_de_outras_tarefas: dict[str, str] | None = None,
  ) -> dict:
      """Veredito mecânico da dimensão `escopo` (`docs/RUBRICA_DE_REVISAO.md:63-77`) com os quatro
      baldes da `DB-25`, nesta precedência: coberto pelos alvos do card > alvo de outra tarefa do
      mesmo plano > registro da orquestração > fora dos alvos sem atribuição. Só o último resolve o
      veredito: vazio → `conforme`; não vazio → `None` (aberto), porque a faixa `parcial` depende de
      desvio declarado na entrega, insumo que este script não recebe.

      Alvo-diretório (`_eh_alvo_diretorio`) casa por prefixo (AUT-T5b); a atribuição a outra tarefa
      casa por caminho exato, depois de normalizar `\\`→`/` nos dois lados."""
      alvo_set = set(arquivos_alvo)
      prefixos_dir = [
          _normalizar_separador(alvo).rstrip("/") + "/"
          for alvo in arquivos_alvo
          if _eh_alvo_diretorio(root, alvo)
      ]
      outros = alvos_de_outras_tarefas or {}

      def coberto(tocado: str) -> bool:
          if tocado in alvo_set:
              return True
          tocado_norm = _normalizar_separador(tocado)
          return any(tocado_norm.startswith(prefixo) for prefixo in prefixos_dir)

      de_outra_tarefa: dict[str, str] = {}
      registro: list[str] = []
      fora: list[str] = []
      for tocado in sorted(tocados):
          if coberto(tocado):
              continue
          tocado_norm = _normalizar_separador(tocado)
          if tocado_norm in outros:
              de_outra_tarefa[tocado] = outros[tocado_norm]
          elif _eh_registro_orquestracao(tocado):
              registro.append(tocado)
          else:
              fora.append(tocado)
      return {
          "fora_dos_alvos": fora,
          "de_outra_tarefa": de_outra_tarefa,
          "registro_orquestracao": registro,
          "veredito": "conforme" if not fora else None,
      }
  ```
- **Texto novo, literal** (substitui o bloco `review_evidence.py:360-368`, dentro de `_renderizar`;
  a indentação é a do corpo da função, quatro espaços):
  ```python
      if escopo.get("de_outra_tarefa"):
          pares = ", ".join(
              f"`{caminho}` → `{tarefa}`"
              for caminho, tarefa in sorted(escopo["de_outra_tarefa"].items())
          )
          linhas.append(f"- Atribuídos a outra tarefa do mesmo plano: {pares}")
      if escopo.get("registro_orquestracao"):
          reg_txt = ", ".join(f"`{c}`" for c in escopo["registro_orquestracao"])
          linhas.append(f"- Registro da orquestração (não atribuível a tarefa): {reg_txt}")
      if escopo["veredito"] == "conforme":
          linhas.append("- Veredito mecânico: conforme")
      else:
          fora_txt = ", ".join(f"`{c}`" for c in escopo["fora_dos_alvos"])
          linhas.append(
              f"- Fato: {len(escopo['fora_dos_alvos'])} arquivo(s) fora dos alvos e sem "
              f"atribuição: {fora_txt}"
          )
          linhas.append(
              "- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, "
              "não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)"
          )
  ```
- **Passos:**
  1. Substituir o bloco `review_evidence.py:172-197` pelo primeiro bloco de código literal acima.
  2. Substituir o bloco `review_evidence.py:360-368` pelo segundo bloco de código literal acima.
  3. Em `montar_documento`, substituir a linha `escopo = confrontar_escopo(tocados, arquivos_alvo, root)`
     por duas linhas: `alvos_de_outras = mapear_alvos_de_outras_tarefas(plano_path, dossie.tarefa_id, root)`
     e `escopo = confrontar_escopo(tocados, arquivos_alvo, root, alvos_de_outras)`.
  4. Apensar ao final do docstring do módulo (antes das aspas de fechamento) o parágrafo:
     `A seção `## Escopo` classifica o arquivo tocado em quatro baldes (`P-0739` `DB-25`): coberto
     pelos alvos do card; alvo declarado por outra tarefa do mesmo plano; registro da orquestração
     (`docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/plans/`, `docs/RDO/`); fora dos alvos
     sem atribuição. Só o último resolve o veredito — `git` não sabe qual tarefa tocou qual arquivo,
     e o plano sabe qual tarefa declarou qual alvo.`
  5. Apensar ao final de `tests/test_review_evidence.py` o helper e os quatro testes da seção
     **Testes**.
  6. Rodar as verificações 1 e 2.
  7. Apensar a linha do `CHANGELOG.md` sob `## [Não lançado]`: ``- `review_evidence.py`: confronto
     de escopo atribui arquivo tocado a outra tarefa do plano e separa o registro da orquestração,
     em vez de reportar tudo como fora-de-alvo (`P-0739` `BKL-T2c`, `DB-25`).``
  8. Rodar a verificação 3.
- **Testes** (nomes fixos, apensos a `tests/test_review_evidence.py`; o helper vem antes deles):
  ```python
  def _escrever_plano_duas_tarefas(
      caminho: Path, alvo_t1: str, alvo_t2: str, verificacao_t2: str | None = "bateria do §3."
  ) -> None:
      """Plano sintético com duas tarefas; `verificacao_t2=None` omite um campo obrigatório de T2
      para exercitar o ramo 'dossiê inválido é pulado' de `mapear_alvos_de_outras_tarefas`."""
      linha_verificacao = f"- **Verificação:** {verificacao_t2}\n" if verificacao_t2 else ""
      texto = (
          "# Plano de teste\n\n"
          "### T1 — Tarefa sintética de teste [Sonnet · classe implementacao]\n"
          "- **Objetivo:** validar review_evidence.py.\n"
          f"- **Arquivos-alvo:** {alvo_t1}\n"
          "- **Verificação:** bateria do §3.\n"
          "- **Pronto quando:** o teste passa.\n\n"
          "### T2 — Outra tarefa sintética [Sonnet · classe implementacao]\n"
          "- **Objetivo:** ser a dona de outro arquivo.\n"
          f"- **Arquivos-alvo:** {alvo_t2}\n"
          f"{linha_verificacao}"
          "- **Pronto quando:** o teste passa.\n"
      )
      caminho.write_text(texto, encoding="utf-8")
  ```
  - `test_tf_arquivo_alvo_de_outra_tarefa_sai_atribuido_e_nao_pesa_no_veredito` — TF:
    `_init_repo_com_baseline(repo)`; plano com `alvo_t1 = "edita `src/b.py`."` e
    `alvo_t2 = "cria `src/a.py`."`; escrever `src/a.py` e alterar `src/b.py`;
    `montar_documento(plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE)`; afirma que o
    documento contém ``"`src/a.py` → `T2`"`` e `"Veredito mecânico: conforme"`.
  - `test_tf_registro_da_orquestracao_sai_em_balde_proprio` — TF: mesmo cenário, tocando também
    `docs/DIARIO_DE_OBRAS.md` e `docs/telemetria.tsv` (criados no repo de fixture); afirma que o
    documento contém `"Registro da orquestração (não atribuível a tarefa)"` e
    `"Veredito mecânico: conforme"`.
  - `test_tr_arquivo_sem_atribuicao_continua_fora_dos_alvos_com_veredito_aberto` — TR: mesmo
    cenário, tocando também `src/c.py`, que não é alvo de tarefa nenhuma; afirma que o documento
    contém `"1 arquivo(s) fora dos alvos e sem atribuição"` e `"(aberto"`.
  - `test_tr_tarefa_com_dossie_invalido_e_pulada_pela_atribuicao` — TR: plano com
    `verificacao_t2=None`; afirma que
    `mapear_alvos_de_outras_tarefas(plano, "T1", repo) == {}` e que nenhuma exceção sobe.
- **Restrições desta tarefa (copiadas inline):**
  - A gramática de ID mora em `rdo.py` e é **lida** daqui por `rdo._ID_HEADER_RE`; não escrever
    regex de ID neste arquivo (`DB-22`).
  - Preservar as chaves `fora_dos_alvos` e `veredito` no dicionário devolvido por
    `confrontar_escopo`: `_renderizar` as lê.
  - Não alterar `coletar_arquivos_tocados`, `montar_trechos`, `rodar_bateria_guardas`, a seção
    `## Guardas` nem o parâmetro `--desde`.
  - `.claude/tools/` não está na lista `ask` de `.claude/settings.json`: editar por `Edit` direto,
    **sem** abrir UoW (`uow.py`).
  - Sem bump de versão e sem tag; nenhum projeto derivado é tocado (`DB-13`).
- **Não fazer:** não acrescentar caminho nenhum a `_REGISTRO_ORQUESTRACAO` além dos quatro
  transcritos (em especial, `.claude/agents/` fica **fora**: edição de definição de agente é fato
  que o revisor tem de ver); não fazer o balde de outra tarefa casar por prefixo de diretório; não
  editar `.claude/tools/rdo.py`, `tests/test_rdo.py`, `docs/DIARIO_DE_OBRAS.md`,
  `docs/telemetria.tsv`, `docs/plans/*`, `docs/RDO/*`.
- **Contingências:**
  - se o texto de `review_evidence.py:172-197` ou de `360-368` não for literalmente o transcrito →
    parar e sinalizar `blocked` razão `premissa`, citando o texto encontrado.
  - se um teste já existente falhar citando `confrontar_escopo`, `_renderizar` ou `montar_documento`
    → seguir com o ajuste das asserções desse teste ao texto novo (a frase do fato passou a ser
    "fora dos alvos e sem atribuição") e registrar o ajuste na nota de execução.
  - se um teste já existente falhar sem citar nenhum dos três → parar e sinalizar `blocked` razão
    `dependencia`, nomeando o teste e a mensagem.
  - se a verificação 3 imprimir `KeyError` → seguir com a correção do mapa nesta tarefa e repetir a
    verificação; se imprimir um ID diferente de `BKL-T2a`, parar e sinalizar `blocked` razão
    `premissa` com o ID impresso.
- **Verificação:**
  1. `python -m pytest tests/test_review_evidence.py -q` → verde, com os 4 testes novos entre os
     coletados.
  2. `python -m pytest tests/ -q` → verde.
  3. Da raiz do repositório:
     `python -c "import importlib.util, pathlib; spec = importlib.util.spec_from_file_location('re_', '.claude/tools/review_evidence.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); print(m.mapear_alvos_de_outras_tarefas(pathlib.Path('docs/plans/P-0739-backlog-instrumento.md'), 'BKL-T2b', pathlib.Path('.'))['tests/test_rdo.py'])"`
     → imprime `BKL-T2a`.
  4. `git status --short` → exatamente três caminhos: `.claude/tools/review_evidence.py`,
     `tests/test_review_evidence.py`, `CHANGELOG.md`.
- **Pronto quando:** os quatro testes novos passam, `python -m pytest tests/ -q` está verde e a
  verificação 3 imprime `BKL-T2a`.
- **Fora do escopo desta tarefa:** a gramática de caminho do campo `Arquivos-alvo` (é a `BKL-T2b`);
  o campo de achado de processo do laudo (é a `BKL-T2d`); qualquer mudança em
  `.claude/tools/backlog.py` (é a `BKL-T3`).

### BKL-T2d — `rdo.py laudo`: o campo de achado de processo com os três alvos [Sonnet · classe implementacao]
- **Status:** `done` · 2026-09-17 · **aprovado** (100%, bloqueante nenhuma) — RDO
  `docs/RDO/P-0739-BKL-T2d-rdo-py-laudo-o-campo-de-achado-de-processo-com-os-tres-alvos.md`
  (laudo consumido e apagado, `DP-H`). Sete dimensões `conforme`. Achado de processo do laudo
  aponta para o mesmo fato já registrado como `AE-5` (Verificação 3 do card não discrimina estado
  alheio na árvore compartilhada) — rota já aberta ali (emenda de `BKL-T3`/`BKL-T4`), sem ação
  nova. Entrega: `tests/test_rdo.py` 38 passed, suíte 110 passed (piso 106), nenhuma contingência
  acionada. Consumo (entrega): ver `docs/telemetria.tsv` (`BKL-T2d`). Consumo (revisão): ver
  `docs/telemetria.tsv` (`BKL-T2d-revisao`).
- **Depende de:** `DB-13`, `DB-28` (`RP-3`), `DB-30`/`DB-31` (`RP-4`, forma do campo
  `Contingências`). Nenhuma tarefa é insumo: esta tarefa não lê nem edita o que a
  `BKL-T2b`/`BKL-T2c` produzem.
- **Objetivo:** `rdo.py laudo` grava a seção `## Achado de processo` a partir de
  `--achado-processo <alvo> "<uma linha>"`, sem alterar percentual, veredito, dimensão bloqueante
  nem recomendação.
- **Camada e fronteira:** camada de instrumento (`.claude/tools/`), fora das camadas de produto. A
  tarefa toca **três** arquivos e nenhum outro: `.claude/tools/rdo.py`, `tests/test_rdo.py`,
  `CHANGELOG.md`. Não edita `review_evidence.py`, `backlog.py`, `rdo_template.md`,
  `docs/RUBRICA_DE_REVISAO.md`, plano, diário nem inbox.
- **Arquivos-alvo:**
  - `.claude/tools/rdo.py:24` — início do parágrafo do docstring que hoje diz "`laudo` (EXA-T8b/T18)
    não é tocado por esta rodada:".
  - `.claude/tools/rdo.py:450-488` — corpo de `cmd_laudo` até a linha `)` que fecha
    `conteudo_final`.
  - `.claude/tools/rdo.py:698-705` — bloco `laudo_parser.add_argument("--escalar", …)`.
  - `tests/test_rdo.py` — apenso de 4 testes ao final do arquivo.
  - `CHANGELOG.md` — uma linha sob `## [Não lançado]`, por `DB-13`.
- **Fatos verificados na `RP-3` (não re-apurar, não re-grepar):**
  - `docs/RUBRICA_DE_REVISAO.md:239-246` define o campo e os três alvos (`dossiê`, `doutrina`,
    `rubrica`); a invariante 1 (`:249-251`) proíbe o achado de rebaixar dimensão de entrega, e a
    invariante 2 (`:252-254`) exige rota (tíquete, replanejamento ou emenda), que é ato da
    orquestração, não do gerador.
  - `calcular_laudo` (`rdo.py:386`) decide percentual, veredito, bloqueante e recomendação; o
    achado **não** passa por ela e a assinatura dela não muda.
  - `conteudo_final` é montado em `rdo.py:476-488`, com `## Lições aprendidas na tarefa` por último;
    `licoes_aprendidas` (`rdo.py:474`) é o precedente de campo discricionário com corpo vazio
    legítimo.
  - `_argv_laudo(laudos_dir, plano="P-TESTE", tarefa="T1", escalar=None, **overrides)`
    (`tests/test_rdo.py:48-70`) monta o argv completo do subcomando `laudo` com as sete dimensões;
    `rdo.main(...)` devolve exit code e os testes de recusa afirmam
    `not laudos_dir.exists() or list(laudos_dir.glob("*.md")) == []`.
- **Texto novo, literal** (constante e função, inseridas imediatamente acima de `def cmd_laudo(`,
  `rdo.py:450`):
  ```python
  _ALVOS_ACHADO = {"dossie": "dossiê", "doutrina": "doutrina", "rubrica": "rubrica"}


  def _formatar_achados_processo(pares: list[list[str]] | None) -> str:
      """`docs/RUBRICA_DE_REVISAO.md` §6: campo próprio, três alvos. Invariante 1 — o achado não
      rebaixa dimensão de entrega e não muda recomendação; por isso nada disto passa por
      `calcular_laudo`. Sem achado, o corpo é `nenhum` (a seção existe sempre)."""
      if not pares:
          return "nenhum"
      linhas = ["| alvo | achado |", "|---|---|"]
      for alvo, texto in pares:
          linhas.append(f"| {_ALVOS_ACHADO[alvo]} | {texto.strip()} |")
      return "\n".join(linhas)
  ```
- **Texto novo, literal** (validação, inserida em `cmd_laudo` logo depois do laço
  `for flag, valor in (("--plano", args.plano), ("--tarefa", args.tarefa)):` e antes de
  `niveis = {...}`):
  ```python
      for alvo, texto in (args.achado_processo or []):
          if alvo not in _ALVOS_ACHADO:
              raise RdoValidationError(
                  f"--achado-processo: alvo '{alvo}' fora de {sorted(_ALVOS_ACHADO)} "
                  "(RUBRICA_DE_REVISAO.md §6)"
              )
          if not texto.strip():
              raise RdoValidationError("--achado-processo: a linha do achado não pode ser vazia")
          if "|" in texto or "\n" in texto:
              raise RdoValidationError(
                  "--achado-processo: uma linha, sem '|' — a tabela do laudo quebraria"
              )
  ```
- **Texto novo, literal** (as duas linhas que entram em `conteudo_final`, entre
  `f"{tabela_niveis}\n\n"` e `"## Lições aprendidas na tarefa\n\n"`):
  ```python
          "## Achado de processo\n\n"
          f"{_formatar_achados_processo(args.achado_processo)}\n\n"
  ```
- **Texto novo, literal** (argumento novo, inserido logo depois do bloco
  `laudo_parser.add_argument("--escalar", …)`):
  ```python
      laudo_parser.add_argument(
          "--achado-processo",
          dest="achado_processo",
          nargs=2,
          action="append",
          metavar=("ALVO", "LINHA"),
          default=None,
          help=(
              "Achado de processo (repetivel): ALVO e dossie, doutrina ou rubrica, seguido de uma "
              "linha. Nao altera percentual, veredito, bloqueante nem recomendacao (RUBRICA §6)."
          ),
      )
  ```
- **Passos:**
  1. Substituir, em `rdo.py:24`, o trecho "`laudo` (EXA-T8b/T18) não é tocado por esta rodada:" por
     "`laudo` (EXA-T8b/T18, estendido pela `BKL-T2d` do `P-0739`):".
  2. Apensar ao final desse mesmo parágrafo do docstring (depois de "…que a regra `B1` consome.") a
     frase: ``--achado-processo <alvo> "<uma linha>"` (repetível; alvo em `dossie`, `doutrina` ou
     `rubrica`) grava a seção `## Achado de processo` e **não** altera percentual, veredito,
     bloqueante nem recomendação — invariante 1 de `docs/RUBRICA_DE_REVISAO.md` §6; `--escalar`
     fica reservado ao achado que invalida a rota (decisão de arquitetura ou de requisito).`
  3. Inserir a constante `_ALVOS_ACHADO` e a função `_formatar_achados_processo` imediatamente
     acima de `def cmd_laudo(`.
  4. Inserir em `cmd_laudo` o bloco de validação literal acima.
  5. Inserir em `conteudo_final` as duas linhas literais acima, entre a tabela de níveis e
     `## Lições aprendidas na tarefa`.
  6. Inserir o `add_argument` literal acima depois do bloco do `--escalar`.
  7. Apensar ao final de `tests/test_rdo.py` os quatro testes da seção **Testes**.
  8. Rodar as verificações 1 e 2.
  9. Apensar a linha do `CHANGELOG.md` sob `## [Não lançado]`: ``- `rdo.py laudo`: campo
     `--achado-processo <alvo> "<linha>"` com os três alvos da `RUBRICA_DE_REVISAO.md` §6, sem
     mexer em percentual, veredito nem recomendação — `--escalar` volta a ser só pendência de
     arquitetura ou de requisito (`P-0739` `BKL-T2d`, `DB-28`).``
- **Testes** (nomes fixos; todos com `tmp_path` e `_argv_laudo`):
  - `test_tf_laudo_achado_de_processo_grava_secao_com_os_tres_alvos` — TF:
    `rdo.main(_argv_laudo(laudos_dir) + ["--achado-processo", "dossie", "criterio de pronto exige registro fora dos alvos", "--achado-processo", "doutrina", "sem guardrail de atribuicao por tarefa"])`;
    afirma exit 0, `"## Achado de processo"` no arquivo gravado, e as duas linhas `| dossiê | …` e
    `| doutrina | …`.
  - `test_tr_laudo_achado_de_processo_nao_muda_veredito_nem_recomendacao` — TR: mesmo comando com
    **um** achado e todas as dimensões no default de `_argv_laudo`; afirma que o arquivo contém
    `"**Recomendação:** seguir"`, `"**Pendência:** nenhuma"` e o mesmo `"**Percentual:**"` do laudo
    gerado sem o achado (dois laudos, comparação da linha).
  - `test_tr_laudo_secao_achado_de_processo_existe_com_nenhum_sem_a_flag` — TR:
    `rdo.main(_argv_laudo(laudos_dir))`; afirma `"## Achado de processo"` e a linha `nenhum` no
    arquivo.
  - `test_tr_laudo_recusa_alvo_fora_dos_tres_e_linha_com_pipe` — TR: dois casos, cada um em seu
    `laudos_dir`: `["--achado-processo", "escopo", "x"]` e
    `["--achado-processo", "dossie", "a | b"]`; cada um afirma exit != 0 e
    `not laudos_dir.exists() or list(laudos_dir.glob("*.md")) == []`.
- **Restrições desta tarefa (copiadas inline):**
  - Não alterar `calcular_laudo`, `LaudoResultado`, `_RECOMENDACOES_VALIDAS`, `_DIMENSOES_ORDEM`,
    `_PESO`, `_VALOR_NIVEL` nem a semântica de `--escalar` e `--vermelho-mecanico`.
  - Não tocar `cmd_close`, `calcular_desdobramento`, `.claude/tools/rdo_template.md` nem
    `docs/RUBRICA_DE_REVISAO.md`: o achado é gravado no laudo, e o laudo é consumido e descartado
    pelo `scrum-master` (`DP-H`).
  - Nenhum caractere fora de cp1252 no texto de `help` do `add_argument` (o `--help` é impresso no
    console do Windows): a seta `→` e o símbolo de pertinência ficam fora.
  - `.claude/tools/` não está na lista `ask` de `.claude/settings.json`: editar por `Edit` direto,
    **sem** abrir UoW (`uow.py`).
  - Sem bump de versão e sem tag; nenhum projeto derivado é tocado (`DB-13`).
- **Não fazer:** não fazer o achado entrar em `calcular_laudo` nem alterar dimensão, percentual ou
  recomendação (invariante 1 da §6); não acrescentar alvo fora dos três; não gerar nem regerar
  laudo de tarefa já fechada (`DB-23`); não editar `docs/RDO/laudos/*`, `docs/DIARIO_DE_OBRAS.md`,
  `docs/telemetria.tsv`, `docs/plans/*`.
- **Contingências:**
  - se o texto de `rdo.py:450-488` ou do bloco do `--escalar` não for literalmente o transcrito →
    parar e sinalizar `blocked` razão `premissa`, citando o texto encontrado.
  - se `argparse` recusar `metavar=("ALVO", "LINHA")` com `nargs=2` → seguir com
    `metavar="ALVO LINHA"` e devolver na linha de retorno da entrega a frase
    `contingência 2 acionada: metavar trocada para "ALVO LINHA"` (`DB-30`).
  - se um teste já existente de `laudo` falhar por causa da seção nova → seguir com o ajuste das
    asserções desse teste (a seção `## Achado de processo` passa a existir sempre) e devolver na
    linha de retorno da entrega a frase `contingência 3 acionada: asserções de <nome do teste>
    ajustadas à seção nova` (`DB-30`).
  - se um teste já existente falhar sem citar `cmd_laudo`, `laudo` ou `conteudo_final` → parar e
    sinalizar `blocked` razão `dependencia`, nomeando o teste e a mensagem.
- **Verificação:**
  1. `python -m pytest tests/test_rdo.py -q` → verde, com os 4 testes novos entre os coletados.
  2. `python -m pytest tests/ -q` → verde.
  3. `git status --short` → exatamente três caminhos: `.claude/tools/rdo.py`, `tests/test_rdo.py`,
     `CHANGELOG.md`.
- **Pronto quando:** os quatro testes novos passam e `python -m pytest tests/ -q` está verde.
- **Fora do escopo desta tarefa:** a rota do achado (tíquete, replanejamento ou emenda da rubrica)
  é ato da orquestração, não do gerador; a seção `## Escopo` do dossiê de evidência (é a `BKL-T2b`
  e a `BKL-T2c`); qualquer mudança em `.claude/tools/backlog.py` (é a `BKL-T3`).

### BKL-T2e — `review_evidence.py`: o balde do ato do dono no confronto de escopo [Sonnet · classe implementacao]
- **Status:** `done` · 2026-09-17 · **aprovado** (100%, bloqueante nenhuma) — RDO
  `docs/RDO/P-0739-BKL-T2e-review-evidence-py-o-balde-do-ato-do-dono-no-confronto-de-es.md`
- **Depende de:** `DB-13`, `DB-25` (`RP-3`), `DB-30`, `DB-32` (`RP-4`). Tarefa anterior cujo produto
  usa: `BKL-T2c` (`done`), que instalou `confrontar_escopo` com os quatro baldes, o
  `_REGISTRO_ORQUESTRACAO` e o bloco de renderização da seção `## Escopo`; esta tarefa insere um
  quinto balde nesses mesmos blocos.
- **Objetivo:** a seção `## Escopo` do dossiê classifica arquivo sob `.claude/agents/` no balde
  `ato do dono`, impresso nominalmente e sem peso no veredito mecânico (`DB-32`).
- **Camada e fronteira:** camada de instrumento (`.claude/tools/`), fora das camadas de produto. A
  tarefa toca **três** arquivos e nenhum outro: `.claude/tools/review_evidence.py`,
  `tests/test_review_evidence.py`, `CHANGELOG.md`. Não edita `rdo.py`, `backlog.py`,
  `.claude/agents/*`, plano, diário nem inbox.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py` — funções `_eh_registro_orquestracao`,
    `mapear_alvos_de_outras_tarefas`, `confrontar_escopo` e o bloco da seção `## Escopo` dentro de
    `_renderizar`; as linhas mudaram na entrega da `BKL-T2c`, então os pontos de edição vêm por
    trecho literal nos **Passos**.
  - `tests/test_review_evidence.py` — apenso de 4 testes ao final do arquivo.
  - `CHANGELOG.md` — uma linha sob `## [Não lançado]`, por `DB-13`.
- **Fatos verificados na `RP-4` (não re-apurar, não re-grepar):**
  - A `BKL-T2c` está `done` com laudo **aprovado 100%** (`docs/RDO/laudos/P-0739-BKL-T2c.md`) e
    entregou literalmente os blocos transcritos no card dela: `_REGISTRO_ORQUESTRACAO` com os
    quatro itens, `_eh_registro_orquestracao`, `mapear_alvos_de_outras_tarefas` e
    `confrontar_escopo` com os quatro baldes.
  - `_normalizar_separador` já existe em `review_evidence.py` e troca `\` por `/`; é a função que o
    balde novo reusa.
  - `tests/test_review_evidence.py` está em `21 passed` e a suíte inteira em `106 passed`; o helper
    `_escrever_plano_duas_tarefas(caminho, alvo_t1, alvo_t2, verificacao_t2="bateria do §3.")`, o
    helper `_init_repo_com_baseline(repo)` e a constante `_BATERIA_FAKE_VERDE` existem no arquivo e
    são reusados como estão.
  - `.claude/agents/pantonic-planner.md` apareceu em "fora dos alvos sem atribuição" nos dossiês de
    `BKL-T2a`, `BKL-T2b` e `BKL-T2c`: é o caso real que esta tarefa mede.
- **Texto novo, literal 1** (inserir **antes** da linha
  `def mapear_alvos_de_outras_tarefas(plano_path: Path, tarefa_id: str, root: Path) -> dict[str, str]:`,
  deixando duas linhas em branco entre o bloco novo e essa linha):
  ```python
  _ATO_DO_DONO = (".claude/agents/",)


  def _eh_ato_do_dono(caminho: str) -> bool:
      """Balde (4) da `DB-32` (`P-0739`): arquivo que só o dono edita, fora do ciclo de qualquer
      tarefa — definição de agente. A árvore de trabalho é compartilhada, então essa edição aparece
      em toda tarefa executada enquanto estiver pendente; sai nomeada na seção `## Escopo` e não
      pesa no veredito. Item terminado em `/` casa por prefixo."""
      alvo = _normalizar_separador(caminho)
      return any(alvo.startswith(item) for item in _ATO_DO_DONO)
  ```
- **Texto novo, literal 2** (substitui, dentro do docstring de `confrontar_escopo`, as três linhas
  que vão de `"""Veredito mecânico` até `Só o último resolve o`):
  ```python
      """Veredito mecânico da dimensão `escopo` (`docs/RUBRICA_DE_REVISAO.md:63-77`) com os cinco
      baldes da `DB-25` e da `DB-32`, nesta precedência: coberto pelos alvos do card > alvo de outra
      tarefa do mesmo plano > registro da orquestração > ato do dono fora do ciclo de tarefa > fora
      dos alvos sem atribuição. Só o último resolve o
  ```
- **Texto novo, literal 3** (substitui as três linhas de declaração das listas locais em
  `confrontar_escopo`):
  ```python
      de_outra_tarefa: dict[str, str] = {}
      registro: list[str] = []
      ato_do_dono: list[str] = []
      fora: list[str] = []
  ```
- **Texto novo, literal 4** (substitui as quatro linhas finais do laço `for tocado in sorted(tocados):`):
  ```python
          elif _eh_registro_orquestracao(tocado):
              registro.append(tocado)
          elif _eh_ato_do_dono(tocado):
              ato_do_dono.append(tocado)
          else:
              fora.append(tocado)
  ```
- **Texto novo, literal 5** (substitui a linha `"registro_orquestracao": registro,` do dicionário
  devolvido por `confrontar_escopo`):
  ```python
          "registro_orquestracao": registro,
          "ato_do_dono": ato_do_dono,
  ```
- **Texto novo, literal 6** (inserir em `_renderizar` **logo depois** da linha
  `linhas.append(f"- Registro da orquestração (não atribuível a tarefa): {reg_txt}")`, na mesma
  indentação do corpo da função, quatro espaços):
  ```python
      if escopo.get("ato_do_dono"):
          dono_txt = ", ".join(f"`{c}`" for c in escopo["ato_do_dono"])
          linhas.append(f"- Ato do dono, fora do ciclo de tarefa: {dono_txt}")
  ```
- **Passos:**
  1. Inserir o **texto novo, literal 1** em `.claude/tools/review_evidence.py`, antes da linha
     `def mapear_alvos_de_outras_tarefas(plano_path: Path, tarefa_id: str, root: Path) -> dict[str, str]:`.
  2. Substituir as três primeiras linhas do docstring de `confrontar_escopo` pelo **texto novo,
     literal 2**.
  3. Substituir as três linhas de declaração de listas locais de `confrontar_escopo` pelo **texto
     novo, literal 3**.
  4. Substituir as quatro linhas finais do laço `for tocado in sorted(tocados):` pelo **texto novo,
     literal 4**.
  5. Substituir a linha `"registro_orquestracao": registro,` pelo **texto novo, literal 5**.
  6. Inserir em `_renderizar` o **texto novo, literal 6**, logo depois da linha
     `linhas.append(f"- Registro da orquestração (não atribuível a tarefa): {reg_txt}")`.
  7. No docstring **do módulo** `review_evidence.py`, trocar a frase `quatro baldes` por
     `cinco baldes` e, na enumeração dos baldes desse mesmo parágrafo, inserir
     `ato do dono fora do ciclo de tarefa (`.claude/agents/`);` imediatamente antes de
     `fora dos alvos`.
  8. Apensar ao final de `tests/test_review_evidence.py` os quatro testes da seção **Testes**.
  9. Rodar as verificações 1 e 2.
  10. Apensar a linha do `CHANGELOG.md` sob `## [Não lançado]`: ``- `review_evidence.py`: confronto
      de escopo separa o ato do dono (`.claude/agents/`) do arquivo fora dos alvos sem atribuição
      (`P-0739` `BKL-T2e`, `DB-32`).``
  11. Rodar as verificações 3 e 4.
- **Testes** (nomes fixos, apensos a `tests/test_review_evidence.py`, reusando
  `_init_repo_com_baseline`, `_escrever_plano_duas_tarefas` e `_BATERIA_FAKE_VERDE`):
  - `test_tf_ato_do_dono_sai_em_balde_proprio_e_nao_pesa_no_veredito` — TF:
    `_init_repo_com_baseline(repo)`; plano com `alvo_t1 = "edita `src/b.py`."` e
    `alvo_t2 = "cria `src/a.py`."`; alterar `src/b.py`; criar
    `.claude/agents/pantonic-planner.md` no repo de fixture (com
    `(repo / ".claude" / "agents").mkdir(parents=True, exist_ok=True)`);
    `montar_documento(plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE)`; afirma que o
    documento contém ``"- Ato do dono, fora do ciclo de tarefa: `.claude/agents/pantonic-planner.md`"``
    e `"Veredito mecânico: conforme"`.
  - `test_tr_arquivo_em_claude_fora_de_agents_continua_sem_atribuicao` — TR: mesmo cenário, criando
    `.claude/settings.json` em vez do arquivo de agente; afirma que o documento contém
    `"1 arquivo(s) fora dos alvos e sem atribuição"` e `"(aberto"`.
  - `test_tr_agente_declarado_como_alvo_do_card_fica_no_balde_de_cobertura` — TR: plano com
    ``alvo_t1 = "edita `.claude/agents/pantonic-planner.md`."`` e `alvo_t2 = "cria `src/a.py`."`;
    criar `.claude/agents/pantonic-planner.md` no repo de fixture; afirma que o documento contém
    `"Veredito mecânico: conforme"` e **não** contém `"Ato do dono"` (a cobertura pelos alvos do
    card tem precedência, `DB-32`).
  - `test_tf_confrontar_escopo_devolve_a_chave_ato_do_dono_com_separador_do_windows` — TF: chamar
    `confrontar_escopo([".claude\\agents\\pantonic-planner.md"], [], tmp_path)`; afirma que
    `resultado["ato_do_dono"] == [".claude\\agents\\pantonic-planner.md"]`,
    `resultado["fora_dos_alvos"] == []` e `resultado["veredito"] == "conforme"`.
- **Restrições desta tarefa (copiadas inline):**
  - `_REGISTRO_ORQUESTRACAO` continua com exatamente os quatro itens da `BKL-T2c`
    (`docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/plans/`, `docs/RDO/`): o balde novo é
    outro, com constante própria (`DB-32`).
  - `_ATO_DO_DONO` tem exatamente um item, `".claude/agents/"`. Nenhum outro caminho entra.
  - Preservar as chaves `fora_dos_alvos`, `de_outra_tarefa`, `registro_orquestracao` e `veredito`
    no dicionário devolvido por `confrontar_escopo`: `_renderizar` as lê.
  - A precedência do laço não muda de ordem: cobertura pelos alvos do card, depois alvo de outra
    tarefa, depois registro da orquestração, depois ato do dono, depois fora sem atribuição.
  - Não alterar `coletar_arquivos_tocados`, `montar_trechos`, `rodar_bateria_guardas`,
    `extrair_arquivos_alvo`, `mapear_alvos_de_outras_tarefas`, a seção `## Guardas` nem o parâmetro
    `--desde`.
  - `.claude/tools/` não está na lista `ask` de `.claude/settings.json`: editar por `Edit` direto,
    **sem** abrir UoW (`uow.py`).
  - Sem bump de versão e sem tag; nenhum projeto derivado é tocado (`DB-13`).
- **Não fazer:** não editar nenhum arquivo sob `.claude/agents/` (definição de agente é ato do
  dono); não acrescentar `.claude/agents/` a `_REGISTRO_ORQUESTRACAO`; não fazer o balde novo casar
  por sufixo nem por nome de arquivo; não gerar nem regerar dossiê de evidência de tarefa já
  fechada (`DB-23`); não editar `.claude/tools/rdo.py`, `tests/test_rdo.py`,
  `docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/plans/*`, `docs/RDO/*`.
- **Contingências:**
  - se qualquer trecho a substituir dos passos 1–6 não for encontrado literalmente em
    `.claude/tools/review_evidence.py` → parar e sinalizar `blocked` razão `premissa`, citando o
    trecho procurado e o texto encontrado no lugar.
  - se a frase `quatro baldes` não existir no docstring do módulo (passo 7) → seguir sem editar o
    docstring do módulo e devolver na linha de retorno da entrega a frase `contingência 2 acionada:
    docstring do módulo sem a frase "quatro baldes"; balde novo documentado em _eh_ato_do_dono`
    (`DB-30`).
  - se um teste já existente falhar citando `confrontar_escopo`, `_renderizar` ou `montar_documento`
    → seguir com o ajuste das asserções desse teste ao texto novo e devolver na linha de retorno da
    entrega a frase `contingência 3 acionada: asserções de <nome do teste> ajustadas ao balde novo`
    (`DB-30`).
  - se um teste já existente falhar sem citar nenhum dos três → parar e sinalizar `blocked` razão
    `dependencia`, nomeando o teste e a mensagem.
  - se `test_tf_ato_do_dono_sai_em_balde_proprio_e_nao_pesa_no_veredito` falhar porque
    `.claude/agents/pantonic-planner.md` não aparece em balde nenhum do documento → parar e
    sinalizar `blocked` razão `dependencia`, nomeando `_init_repo_com_baseline` e colando a seção
    `## Escopo` produzida.
  - se a verificação 3 imprimir `.claude/agents/pantonic-planner.md` fora da primeira lista → parar
    e sinalizar `blocked` razão `premissa`, colando a saída.
- **Verificação:**
  1. `python -m pytest tests/test_review_evidence.py -q` → `25 passed` (eram 21).
  2. `python -m pytest tests/ -q` → verde.
  3. Da raiz do repositório:
     `python -c "import importlib.util, pathlib; spec = importlib.util.spec_from_file_location('re_', '.claude/tools/review_evidence.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); r = m.confrontar_escopo(['.claude/agents/pantonic-planner.md', 'src/x.py'], [], pathlib.Path('.')); print(r['ato_do_dono'], r['fora_dos_alvos'], r['veredito'])"`
     → imprime `['.claude/agents/pantonic-planner.md'] ['src/x.py'] None`.
  4. `git status --short -- .claude/tools/review_evidence.py tests/test_review_evidence.py CHANGELOG.md`
     → exatamente três linhas, uma por caminho.
- **Pronto quando:** `python -m pytest tests/test_review_evidence.py -q` imprime `25 passed`,
  `python -m pytest tests/ -q` está verde e a verificação 3 imprime
  `['.claude/agents/pantonic-planner.md'] ['src/x.py'] None`.
- **Fora do escopo desta tarefa:** o campo de achado de processo do laudo (é a `BKL-T2d`); a
  gramática de caminho do campo `Arquivos-alvo` (já entregue pela `BKL-T2b`); a atribuição a outra
  tarefa e o registro da orquestração (já entregues pela `BKL-T2c`); qualquer mudança em
  `.claude/tools/backlog.py` (é a `BKL-T3`).

### BKL-T3 — `next`: a seleção determinística [Sonnet · classe implementacao]
- **Status:** `done` · 2026-09-17 · ressalva 94%, bloqueante nenhuma, `rota` `parcial` — `AE-7`
  Entregue pelo `pantonic-executor` (13 testes novos, `tests/test_backlog.py` `21 passed`, suíte
  `127 passed`, duas fixtures novas; nenhuma contingência acionada) e revisada pelo
  `pantonic-reviewer` no mesmo dia. RDO
  `docs/RDO/P-0739-BKL-T3-next-a-selecao-deterministica.md`; laudo consumido e apagado (`DP-H`),
  com os três achados de processo registrados em `### AE-7`. Antes disso esteve `blocked` razão
  `premissa` em 2026-09-17 e foi reaberta pela `RP-5` (`G-REPLAN`), que absorveu o `AE-6`: a linha
  de contexto do pai ganhou forma por tipo de pai (`DB-33`), com worked example para cada uma em
  §2.6, e as regras que o TF "bug antes de FIFO" exigia foram fechadas (`DB-34`, `DB-35`, `DB-36`).
- **Depende de:** `BKL-T2`, `BKL-T2a`; decisões `DB-5`, `DB-6`, `DB-7`, `DB-33`, `DB-34`, `DB-35`,
  `DB-36`.
- **Objetivo:** implementar §2.5 e §2.6 no verbo `next` de `.claude/tools/backlog.py`; exit 0/2/3.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py` — o verbo `next` e as funções de seleção e de renderização.
  - `tests/test_backlog.py` — os TF/TR deste card.
  - `tests/fixtures/backlog/` — os arquivos de fixture que os TF deste card exigem.
- **Restrições desta tarefa (copiadas inline):**
  - `next` é somente-leitura: nenhuma função deste card escreve em arquivo do repositório
    (`DB-5`). Escrita é verbo de `BKL-T4`.
  - Ambiguidade é defeito, não escolha: dois `in-progress`, item vivo sem linha `Status`, linha de
    índice fora da gramática e pai vivo sem linha no índice saem em **exit 3** nomeando o conserto
    (`DB-6`, `DB-33`) — o código nunca desempata por heurística.
  - Teto do dossiê: seção da tarefa verbatim até 8.000 chars / 120 linhas; além disso, truncada com
    ponteiro `arquivo:l1-l2` (`DB-7`).
  - As funções recebem `repo` e caminhos já resolvidos por parâmetro e nunca leem `sys.argv`
    (`DB-1`); o módulo é carregado nos testes por `importlib`, como em `tests/test_telemetria.py`.
  - `<done>/<total>` de qualquer pai sai da fórmula única da `DB-36`: `<total>` = filhos diretos com
    `Status` diferente de `cancelled`; `<done>` = destes, os com `Status` igual a `done`.
- **Não fazer:** não implementar `status`, `start`, `drain` nem `diretiva` (são `BKL-T4` e
  `BKL-T5`); não rodar o instrumento contra `docs/DIARIO_DE_OBRAS.md` nem contra `docs/plans/` do
  repositório real — toda asserção é sobre a fixture; não editar `.claude/agents/`,
  `docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/plans/*` nem `docs/RDO/*`.
- **Testes:** um TF por ramo — retomada de `in-progress`; diretiva restringe os candidatos;
  `Depende de` não `done` segura o candidato; plano `blocked` não contribui; `Ordem de execução`
  vence a ordem dos cabeçalhos; fila vazia → exit 2; dois `in-progress` → exit 3 com os dois IDs;
  rodapé lista os `blocked` e conta as linhas não marcadas de `<memory-dir>/_INBOX.md` (caminho
  injetado por parâmetro no teste). Mais os quatro que a `RP-5` fecha:
  - `test_tf_bug_antes_de_fifo` — a fixture tem um tíquete `TK-90` com `- **Tipo:** bug`, linha no
    índice e duas subtarefas `### TK-90a`/`### TK-90b` (`[Sonnet · classe mecanica]`, `Status`
    `ready`), mais uma tarefa de plano `ready` que venceria por FIFO e cujo plano-pai **não** está
    `in-progress`. Afirma: `next` devolve `TK-90a` (faixa (b) da §2.5 regra 4 pelo `Tipo` do
    tíquete-pai, `DB-35`) e a linha 2 da saída é exatamente
    `tíquete: TK-90 — <título> (0/2) · residência: <caminho do diário da fixture>:<l1>-<l2> · índice: <âncora>`
    (`DB-33`, worked example B de §2.6).
  - `test_tf_linha_do_pai_plano` — vencedor com plano-pai: a linha 2 começa pelo literal `plano: `,
    traz `P-NNNN`, o título da linha 1 do arquivo do plano, o par da `DB-36` e os campos
    `residência:` e `índice:` (worked example A de §2.6).
  - `test_tf_antecessora_omitida_no_primeiro_irmao` — vencedor que é o primeiro irmão na ordem
    interna do pai: a saída **não** contém a substring `antecessora:`; vencedor que não é o primeiro
    irmão: a linha 3 nomeia o irmão imediatamente anterior, com o estado dele, e escreve
    `sem notas` quando esse irmão não tem bloco `- **Notas de execução:**` (`DB-34`).
  - `test_tf_pai_sem_linha_de_indice_sai_exit_3` — tíquete-pai sem linha no índice da fixture →
    exit 3 e a mensagem contém `linha de índice ausente para TK-90` (`DB-6`, `DB-33`).
  - TR: `test_tr_saida_do_next_cabe_no_teto` — `len(saida) <= 8200` para o dossiê da fixture.
- **Contingências:**
  - se `tests/fixtures/backlog/` não existir no repositório → criar o diretório e os arquivos que os
    TF deste card exigem (mini-diário com índice, um plano, o tíquete `TK-90` com as duas
    subtarefas, inbox), nas formas de §2.1 a §2.4, e devolver na linha de retorno da entrega a frase
    `contingência 1 acionada: fixture de tests/fixtures/backlog/ criada neste card` (`DB-30`).
  - se a fixture já trouxer um tíquete com `- **Tipo:** bug` → reutilizar esse tíquete em vez de
    criar `TK-90`, ajustar os IDs das asserções acima ao dele e devolver na linha de retorno da
    entrega a frase `contingência 2 acionada: TF de bug escrito sobre o tíquete <ID> já existente`
    (`DB-30`).
  - se qualquer regra de §2.5 ou §2.6 admitir duas leituras para o mesmo dado da fixture → parar e
    sinalizar `blocked` razão `premissa`, citando a regra e as duas leituras (`DB-19`).
  - se um teste já existente de `tests/test_backlog.py` falhar por causa da renderização nova →
    seguir com o ajuste das asserções desse teste à forma de §2.6 e devolver na linha de retorno da
    entrega a frase `contingência 4 acionada: asserções de <nome do teste> ajustadas à §2.6`
    (`DB-30`).
- **Verificação:**
  1. `python -m pytest tests/test_backlog.py -q` → verde, com os cinco testes novos deste card
     entre os coletados.
  2. `python -m pytest tests/ -q` → verde.
- **Pronto quando:** `python -m pytest tests/ -q` está verde; cada uma das cinco regras de §2.5 tem
  ao menos um teste em `tests/test_backlog.py`; e as duas formas da linha 2 de §2.6 (pai-plano e
  pai-tíquete) estão afirmadas literalmente por `test_tf_linha_do_pai_plano` e
  `test_tf_bug_antes_de_fifo`.

### BKL-T3a — As três condições de exit 3 de `next` e o contador do rodapé [Sonnet · classe implementacao]
- **Status:** `done` · revisada em 2026-09-18 pelo `pantonic-reviewer` — **ressalva 94%**,
  bloqueante nenhuma, única dimensão fora de `conforme`: `rota` `parcial` (RDO
  `docs/RDO/P-0739-BKL-T3a-as-tres-condicoes-de-exit-3-de-next-e-o-contador-do-rodape.md`).
  Entregue em 2026-09-18 pelo `pantonic-executor`, **nenhuma contingência acionada** (suíte
  `130 passed`, piso 127; `tests/test_backlog.py` `24`). Autorada pela `RP-6` a partir dos achados 1
  e 3 do `AE-7` (`DB-39`); nenhuma entrega fechada é reaberta (`DB-23`). Achados de processo da
  revisão registrados como `AE-8` (E-2 cobre só metade "item candidato"; contador de fila de
  memória aceita `---`), sem retroação — a `RP-7` é a próxima tarefa.
- **Depende de:** `BKL-T3` (`done`, entregou o verbo `next`); decisões `DB-1`, `DB-5`, `DB-6`,
  `DB-37`, `DB-38`, `DB-39`; seções §2.4 (gramática do inbox de planos), §2.5 item 6 (lista única
  das condições de exit 3) e o rodapé de §2.6.
- **Objetivo:** em `.claude/tools/backlog.py`, cada uma das três condições de exit 3 de `next`
  imprime a substring obrigatória de §2.5 item 6, e o campo `inbox de planos: <n> por drenar` do
  rodapé conta pela gramática de §2.4 — com um TF por condição sem TF e um TF discriminante para o
  contador.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py` — a função do verbo `next` que decide exit 3 e a função que renderiza o rodapé de pendências mecânicas.
  - `tests/test_backlog.py` — os TF deste card.
  - `tests/fixtures/backlog/inbox_planos/_INBOX.md` (novo) — o inbox de planos com uma linha viva, uma drenada e uma sem caminho de plano.
- **Restrições desta tarefa (copiadas inline de §2.5 item 6 e de §2.4):**
  - `next` segue somente-leitura: nenhuma função deste card escreve em arquivo do repositório
    (`DB-5`). Escrita é verbo da `BKL-T4`.
  - Condições de exit 3 de `next`, lista fechada de três (`DB-37`):
    - **E-1** — dois ou mais itens candidatos com `Status` `in-progress`: a mensagem contém
      `dois ou mais itens in-progress: ` seguida dos IDs, em ordem alfabética crescente, separados
      por `, `.
    - **E-2** — item candidato, ou pai de candidato, sem a linha `- **Status:**`: a mensagem contém
      `linha de status ausente para <ID>`, com `<ID>` sendo o item ou o pai sem a linha.
    - **E-3** — pai de candidato elegível sem linha no índice do diário: a mensagem contém
      `linha de índice ausente para <ID>`, com `<ID>` sendo o ID do pai.
    - Nenhuma outra condição sai exit 3 em `next`. Linha de índice que não casa a gramática de §2.2
      é descartada na leitura e não existe para `next`; quando é a linha do pai de um candidato
      elegível, o caso cai em E-3. O lint dela é do verbo `check` (`C-4`, `C-9`) e plano vivo sem
      prefixo é `C-7` no `check` e exit 3 do `drain`, nunca exit 3 de `next`.
  - Contador do rodapé (`DB-38`): `inbox de planos: <n> por drenar` conta as linhas de
    `docs/plans/_INBOX.md` que começam com `- `, contêm um caminho que casa
    `docs/plans/P-[0-9]{4}-<slug>.md` e **não** começam com `- [drenado `;
    `fila de memória: <m> candidato(s)` conta as linhas do inbox de memória que começam com `- ` e
    não trazem `[promovido]` nem `[descartado`. São duas gramáticas, uma por arquivo: nenhuma das
    duas serve o outro arquivo.
  - As funções recebem `repo` e os dois caminhos de inbox já resolvidos por parâmetro e nunca leem
    `sys.argv` (`DB-1`); o módulo é carregado nos testes por `importlib`, como em
    `tests/test_telemetria.py`.
- **Passos:**
  1. Em `.claude/tools/backlog.py`, partir a função `_contar_pendentes_inbox` em duas —
     `_contar_inbox_planos(caminho)` e `_contar_inbox_memoria(caminho)` —, cada uma com a gramática
     da sua residência (Restrições acima), e ligar cada uma ao seu campo do rodapé: a primeira a
     `inbox de planos: <n> por drenar`, a segunda a `fila de memória: <m> candidato(s)`.
  2. Criar `tests/fixtures/backlog/inbox_planos/_INBOX.md` com o texto literal abaixo, sem mais
     nenhuma linha.
  3. Na função do verbo `next` que decide exit 3, escrever as mensagens de E-1 e de E-2 com as
     substrings obrigatórias da tabela de Restrições, mantendo a de E-3 como já está entregue.
  4. Em `tests/test_backlog.py`, acrescentar os três TF da seção `Testes` abaixo.
  5. Rodar os quatro comandos da seção `Verificação`, nesta ordem.
- **Texto novo, literal** (conteúdo de `tests/fixtures/backlog/inbox_planos/_INBOX.md`):

  ```markdown
  # Inbox de planos (fixture)

  **Próximo id de plano: P-0742.**

  - `docs/plans/P-0740-exemplo-vivo.md` — plano vivo, por drenar
  - [drenado 2026-09-18] `docs/plans/P-0741-exemplo-drenado.md` — já drenado
  - nota solta, sem caminho de plano
  ```

  Pela gramática de §2.4 o arquivo tem **1** linha viva; pela gramática do inbox de memória teria
  **3** — é essa diferença que dá poder discriminante ao TF (`DB-38`).
- **Testes:**
  - `test_tf_contador_do_inbox_de_planos_ignora_drenada_e_linha_sem_plano` — roda `next` sobre a
    fixture `tests/fixtures/backlog/next_tk90/` com o caminho do inbox de planos apontado para
    `tests/fixtures/backlog/inbox_planos/_INBOX.md`; afirma que a saída contém a substring
    `inbox de planos: 1 por drenar` e **não** contém `inbox de planos: 3 por drenar`.
  - `test_tf_exit_3_dois_in_progress_nomeia_os_ids` — copia `tests/fixtures/backlog/next_tk90/` para
    o `tmp_path` do pytest com `shutil.copytree`, troca na cópia o token da linha
    `- **Status:**` de dois itens `ready` para `in-progress` e roda `next` sobre a cópia; afirma
    exit 3 e a substring `dois ou mais itens in-progress: ` seguida dos dois IDs em ordem alfabética
    crescente, separados por `, `.
  - `test_tf_exit_3_item_sem_linha_de_status` — copia `tests/fixtures/backlog/next_tk90/` para o
    `tmp_path` do pytest com `shutil.copytree`, apaga na cópia a linha `- **Status:**` do item que
    `next` devolve na fixture intacta e roda `next` sobre a cópia; afirma exit 3 e a substring
    `linha de status ausente para ` seguida do ID desse item.
  - E-3 já tem TF entregue pela `BKL-T3` (`test_tf_pai_sem_linha_de_indice_sai_exit_3`, fixture
    `tests/fixtures/backlog/next_tk90_sem_indice/`): este card **não** cria outro para ela.
- **Não fazer:** não implementar `status`, `start`, `drain` nem `diretiva` (são `BKL-T4` e
  `BKL-T5`); não editar os arquivos de `tests/fixtures/backlog/next_tk90/` nem de
  `tests/fixtures/backlog/next_tk90_sem_indice/` — o teste que precisa de dado diferente copia a
  fixture para o `tmp_path` do pytest; não criar condição de exit 3 em `next` além de E-1, E-2 e
  E-3; não mexer no verbo `check` nem nos códigos `C-1..C-9`; não rodar o instrumento contra
  `docs/DIARIO_DE_OBRAS.md` nem contra `docs/plans/` do repositório real; não editar
  `.claude/agents/`, `docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/plans/*` nem
  `docs/RDO/*`.
- **Contingências:**
  - se não existir função com o nome `_contar_pendentes_inbox` em `.claude/tools/backlog.py` →
    seguir com a função que o verbo `next` usa hoje para produzir o campo `inbox de planos:` do
    rodapé, aplicando a ela o passo 1, e devolver na linha de retorno da entrega a frase
    `contingência 1 acionada: contador do rodapé reside em <nome real da função>` (`DB-30`).
  - se a função que renderiza o rodapé não receber o caminho do inbox de planos por parâmetro →
    acrescentar o parâmetro com valor default `repo / "docs" / "plans" / "_INBOX.md"` (`DB-1`) e
    devolver na linha de retorno da entrega a frase
    `contingência 2 acionada: parâmetro de caminho do inbox de planos acrescentado` (`DB-30`).
  - se `tests/test_backlog.py` já tiver um teste com um dos três nomes acima → acrescentar as
    asserções deste card ao corpo do teste existente, sem criar outro, e devolver na linha de
    retorno da entrega a frase
    `contingência 3 acionada: asserções acrescentadas a <nome do teste>` (`DB-30`).
  - se um teste já existente de `tests/test_backlog.py` falhar por causa da mensagem nova de E-1 ou
    de E-2 → seguir com o ajuste das asserções desse teste às substrings da tabela de Restrições e
    devolver na linha de retorno da entrega a frase
    `contingência 4 acionada: asserções de <nome do teste> ajustadas a §2.5 item 6` (`DB-30`).
  - se a tabela de §2.5 item 6 ou a gramática de §2.4 admitir duas leituras para o mesmo dado da
    fixture → parar e sinalizar `blocked` razão `premissa`, citando a regra e as duas leituras
    (`DB-19`).
- **Verificação:**
  1. `python -m pytest tests/test_backlog.py -q` → verde.
  2. `python -m pytest tests/test_backlog.py --collect-only -q` → a lista traz os nomes
     `test_tf_contador_do_inbox_de_planos_ignora_drenada_e_linha_sem_plano`,
     `test_tf_exit_3_dois_in_progress_nomeia_os_ids` e `test_tf_exit_3_item_sem_linha_de_status`.
  3. `python -m pytest --collect-only -q` → não menos de 127 testes coletados (piso medido em
     2026-09-18, com `tests/test_backlog.py` em 21).
  4. `python -m pytest tests/ -q` → verde.
- **Pronto quando:** os quatro comandos da `Verificação` dão o resultado descrito, e a saída de
  `next` sobre `tests/fixtures/backlog/next_tk90/` com o inbox deste card contém
  `inbox de planos: 1 por drenar`.
- **Fora do escopo desta tarefa:** aplicar E-2 e E-3 aos verbos `status` e `start` (é a `BKL-T4`);
  migrar os documentos vivos (é a `BKL-T6`).

### BKL-T3b — E-2 sobre o pai do candidato e o prefixo `- ` do contador de memória [Sonnet · classe implementacao]
- **Status:** `done` · 2026-09-18 · entregue pelo `pantonic-executor` sem contingência acionada e
  **aprovada 100%** pelo `pantonic-reviewer` (bloqueante nenhuma, sete dimensões `conforme`,
  recomendação `seguir`, sem `--escalar`); RDO
  `docs/RDO/P-0739-BKL-T3b-e-2-sobre-o-pai-do-candidato-e-o-prefixo-do-contador-de-memo.md`
  (laudo consumido e apagado, `DP-H`); único achado de processo registrado como `AE-9`, alvo
  `dossiê`, sem retroação · autorado pela `RP-7` a partir dos achados 1 e 2 do `AE-8`
  (`DB-40`, `DB-41`, `DB-42`); nenhuma entrega fechada reaberta (`DB-23`).
- **Depende de:** `BKL-T3a` (`done`, entregou as substrings de E-1/E-2 e os dois contadores do
  rodapé); decisões `DB-1`, `DB-5`, `DB-6`, `DB-37`, `DB-38`, `DB-40`, `DB-41`, `DB-42`; §2.5 item 6
  (residência única das condições de exit 3) e o rodapé de §2.6.
- **Objetivo:** em `.claude/tools/backlog.py`, a condição E-2 de `next` passa a recusar também o
  **pai** de candidato sem a linha `- **Status:**`, e o contador `fila de memória:` deixa de contar
  a régua markdown `---` — com um TF discriminante por defeito.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py` — a função do verbo `next` que decide exit 3 e a função que conta o inbox de memória para o rodapé.
  - `tests/test_backlog.py` — os dois TF deste card.
- **Restrições desta tarefa (copiadas inline de §2.5 item 6 e do rodapé de §2.6):**
  - `next` segue somente-leitura: nenhuma função deste card escreve em arquivo do repositório
    (`DB-5`). Escrita é verbo da `BKL-T4`.
  - **E-2, forma completa** (`DB-37`, `DB-40`): a condição casa **item candidato ou pai de
    candidato** sem a linha `- **Status:**`; a mensagem traz uma ocorrência de
    `linha de status ausente para <ID>` por **ID distinto**, em ordem alfabética crescente do
    `<ID>`, separadas por `, `. Pai com dois filhos candidatos aparece **uma vez** na mensagem.
  - E-2 é avaliada **antes** de E-1 e de E-3, como já está entregue. O conjunto sobre o qual ela
    corre é a união do **item de cada candidato** com o **pai de cada candidato**; pai sem a linha
    nunca é tratado como pai `ready` (`DB-2`, `DB-3`).
  - As outras duas condições ficam como estão entregues e este card não as altera: **E-1** — dois ou
    mais itens candidatos com `Status` `in-progress`, mensagem com `dois ou mais itens in-progress: `
    seguida dos IDs em ordem alfabética crescente, separados por `, `; **E-3** — pai de candidato
    elegível sem linha no índice do diário, mensagem com `linha de índice ausente para <ID>`.
    Nenhuma outra condição sai exit 3 em `next`.
  - Fronteira contra o instrumento vizinho (`DB-40`): a **ausência** da linha `- **Status:**` é
    violação `C-2` (tarefa, tíquete, subtarefa) ou `C-8` (plano vivo) do verbo `check`; em `next` ela
    é E-2, que recusa a seleção e **não** classifica a violação. Este card não toca o `check`.
  - Contador de fila de memória (`DB-41`): conta a linha cujo texto, depois de `strip()`, **começa
    com `- `** — hífen **e** espaço — e não traz `[promovido]` nem `[descartado`. Nenhuma outra
    exclusão entra no contador. O contador irmão `_contar_inbox_planos` (gramática de §2.4) não é
    tocado.
  - As funções recebem `repo` e os caminhos já resolvidos por parâmetro e nunca leem `sys.argv`
    (`DB-1`); o módulo é carregado nos testes por `importlib`, como em `tests/test_telemetria.py`.
- **Passos:**
  1. Em `.claude/tools/backlog.py`, na função `selecionar_next`, substituir a lista `sem_status` —
     hoje formada só pelos candidatos cujo `item.status` é `None` — por uma lista de **IDs
     distintos**, formada pelo `item.id` de cada candidato com `item.status is None` e pelo `pai.id`
     de cada candidato com `pai.status is None`, ordenada alfabeticamente por `sorted`, mantendo o
     bloco na posição em que já está (antes da contagem de `in-progress`).
  2. No mesmo bloco, montar a mensagem juntando `linha de status ausente para <ID>` por ID dessa
     lista, separados por `, `, e devolver `SelecaoNext(3, None, <mensagem>)`.
  3. Na função `_contar_inbox_memoria`, trocar o teste de prefixo `s.startswith("-")` por
     `s.startswith("- ")`, sem acrescentar nenhum outro filtro à função.
  4. Em `tests/test_backlog.py`, acrescentar os dois TF da seção `Testes` abaixo.
  5. Rodar os quatro comandos da seção `Verificação`, nesta ordem.
- **Texto novo, literal** (conteúdo do inbox de memória que o segundo TF escreve no `tmp_path` do
  pytest):

  ```markdown
  # Inbox de memória (fixture)

  - 2026-01-01 — a — feedback — candidato 1 — **origem:** x
  - 2026-01-02 — b — feedback — candidato 2 — **origem:** y [promovido]

  ---

  - 2026-01-03 — c — feedback — candidato 3 — **origem:** z
  ```

  Pela gramática de `GOVERNANCA_MEMORIAS.md` §8 (prefixo `- `, hífen e espaço) o arquivo tem **2**
  candidatos; pela leitura sem o espaço (`-`) teria **3**, porque a régua `---` entraria — é essa
  diferença que dá poder discriminante ao TF (`DB-41`).
- **Testes:**
  - `test_tf_exit_3_pai_de_candidato_sem_linha_de_status` — copia
    `tests/fixtures/backlog/next_tk90/` para o `tmp_path` do pytest (o helper de cópia de fixture já
    usado nos testes deste arquivo) e, **na cópia**: (a) apaga de `docs/DIARIO_DE_OBRAS.md` a linha
    `- **Status:** \`ready\` · 2026-01-01` que vem logo abaixo do cabeçalho
    `## TK-90 — Relatório diário sai com data trocada`; (b) substitui em
    `docs/plans/P-0090-fifo.md` a linha
    `**Status:** \`ready\` · **Prefixo das tarefas no diário:** \`FFO-T<n>\`` pela linha
    `**Prefixo das tarefas no diário:** \`FFO-T<n>\``. Carrega o modelo da cópia, roda a seleção e
    afirma, sobre o resultado: `exit_code == 3`;
    `mensagem.count("linha de status ausente para TK-90") == 1`;
    `"linha de status ausente para P-0090" in mensagem`; e
    `mensagem.index("P-0090") < mensagem.index("TK-90")`. **Poder discriminante:** com a E-2 como
    entregue hoje (só o item), essa mesma cópia **não** sai exit 3 — os candidatos dos dois pais
    caem no filtro de elegibilidade `pai.status in ("ready", "in-progress")` e a seleção devolve
    exit 2 (`nada delegável`), sem nomear conserto nenhum; e, quando só o tíquete perde a linha,
    devolve exit 0 elegindo `FFO-T2`, que é o desvio medido na revisão da `BKL-T3a` (`AE-8`).
  - `test_tf_contador_de_memoria_ignora_regua_e_marcadas` — escreve no `tmp_path` do pytest um
    arquivo `_INBOX.md` com o texto literal da seção `Texto novo, literal`, roda a seleção sobre a
    fixture `tests/fixtures/backlog/next_tk90/` intacta (exit 0) e renderiza a saída de `next`
    passando esse arquivo como inbox de memória; afirma que a saída contém a substring
    `fila de memória: 2 candidato(s)` e **não** contém `fila de memória: 3 candidato(s)`.
    **Poder discriminante:** o valor 3 é exatamente o que a leitura sem o espaço no prefixo imprime
    sobre o mesmo corpus.
- **Não fazer:** não tocar `_contar_inbox_planos` nem a fixture
  `tests/fixtures/backlog/inbox_planos/_INBOX.md`; não acrescentar ao contador de memória filtro de
  indentação, de data ou de campo `**origem:**`; não criar condição de exit 3 em `next` além de E-1,
  E-2 e E-3; não alterar as mensagens de E-1 e E-3; não implementar `status`, `start`, `drain` nem
  `diretiva` (são `BKL-T4` e `BKL-T5`); não editar os arquivos de
  `tests/fixtures/backlog/next_tk90/` nem de `tests/fixtures/backlog/next_tk90_sem_indice/` — o
  teste que precisa de dado diferente copia a fixture para o `tmp_path` do pytest; não mexer no
  verbo `check` nem nos códigos `C-1..C-9`; não rodar o instrumento contra
  `docs/DIARIO_DE_OBRAS.md` nem contra `docs/plans/` do repositório real; não editar
  `.claude/agents/`, `docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/plans/*` nem
  `docs/RDO/*`.
- **Contingências:**
  - se a linha a apagar abaixo de `## TK-90` ou a linha de cabeçalho de `docs/plans/P-0090-fifo.md`
    não tiver o texto literal transcrito no TF → aplicar a edição à linha que **começa** com
    `- **Status:**` logo abaixo do cabeçalho `## TK-90` e à linha do cabeçalho do plano que
    **contém** `**Status:**`, preservando o resto dessa linha, e devolver na linha de retorno da
    entrega a frase
    `contingência 1 acionada: linha de Status da fixture localizada por prefixo, não por literal`
    (`DB-30`).
  - se `tests/test_backlog.py` já tiver um teste com um dos dois nomes acima → acrescentar as
    asserções deste card ao corpo do teste existente, sem criar outro, e devolver na linha de
    retorno da entrega a frase
    `contingência 2 acionada: asserções acrescentadas a <nome do teste>` (`DB-30`).
  - se um teste já existente de `tests/test_backlog.py` falhar por causa da mensagem nova de E-2 ou
    do contador de memória corrigido → seguir com o ajuste das asserções desse teste às Restrições
    deste card e devolver na linha de retorno da entrega a frase
    `contingência 3 acionada: asserções de <nome do teste> ajustadas às Restrições da BKL-T3b`
    (`DB-30`).
  - se a tabela de §2.5 item 6 ou o rodapé de §2.6 admitir duas leituras para o mesmo dado da
    fixture → parar e sinalizar `blocked` razão `premissa`, citando a regra e as duas leituras
    (`DB-19`).
- **Verificação:**
  1. `python -m pytest tests/test_backlog.py -q` → verde.
  2. `python -m pytest tests/test_backlog.py --collect-only -q` → a lista traz os nomes
     `test_tf_exit_3_pai_de_candidato_sem_linha_de_status` e
     `test_tf_contador_de_memoria_ignora_regua_e_marcadas`.
  3. `python -m pytest --collect-only -q` → não menos de 130 testes coletados (piso medido em
     2026-09-18, no fechamento da `BKL-T3a`: suíte `130 passed`, `tests/test_backlog.py` em 24).
  4. `python -m pytest tests/ -q` → verde.
- **Pronto quando:** os quatro comandos da `Verificação` dão o resultado descrito; na cópia da
  fixture no `tmp_path` sem a linha `- **Status:**` do tíquete `TK-90`, a seleção sai exit 3 com a
  substring `linha de status ausente para TK-90` aparecendo **uma única vez** na mensagem; e a saída
  de `next` sobre `tests/fixtures/backlog/next_tk90/` com o inbox de memória deste card contém
  `fila de memória: 2 candidato(s)`.
- **Fora do escopo desta tarefa:** aplicar E-2 e E-3 aos verbos `status` e `start` (é a `BKL-T4`);
  migrar os documentos vivos (é a `BKL-T6`).

### BKL-T4 — `status`, `start`, `diretiva`: transição e projeções [Sonnet · classe implementacao]
- **Status:** `done` · 2026-09-15 · fechada 2026-09-18 (`ressalva` 85%, bloqueante `nenhuma`, RDO `docs/RDO/P-0739-BKL-T4-status-start-diretiva-transicao-e-projecoes.md`; ressalva roteada como `AE-10`) · restrições, `Não fazer` e contingências autorados pela `RP-6`
  (2026-09-18) a partir do achado 1 do `AE-7`; `Depende de` e a forma da mensagem de E-2 emendados
  pela `RP-7` (2026-09-18, `DB-40`, `DB-42`).
- **Depende de:** `BKL-T3`, `BKL-T3a`, `BKL-T3b`; decisões `DB-33`, `DB-36` (forma do bullet por pai
  e contagem do par `<done>/<total>`, iguais às que a `BKL-T3` já implementou para `next`), `DB-37`
  (as condições `E-2` e `E-3` valem antes de escrever) e `DB-40` (E-2 casa o item alvo **e** o pai
  dele, com ID distinto uma vez e em ordem alfabética).
- **Objetivo:** §2.7 + escrita atômica de todas as projeções num ato (§3), com lista de arquivos
  tocados na saída (`DB-10`).
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py` — os verbos `status`, `start` e `diretiva` e a escrita das projeções.
  - `tests/test_backlog.py` — os TF/TR deste card.
- **Restrições desta tarefa (copiadas inline):**
  - Escrita atômica, num ato só: temp + `os.replace` (`DB-1`). Transição fora da tabela de §2.7 →
    **exit 1** sem escrever nada; `blocked` exige `--razao`; `done` e `cancelled` são terminais;
    `superseded` só para plano.
  - Antes de qualquer escrita, `status` e `start` aplicam duas das três condições de exit 3 de §2.5
    item 6 (`DB-37`), saindo **exit 3** com **nenhum arquivo tocado**: **E-2** — item alvo, ou pai
    dele, sem a linha `- **Status:**` → a mensagem contém `linha de status ausente para <ID>`;
    **E-3** — pai do item alvo sem linha no índice do diário → a mensagem contém
    `linha de índice ausente para <ID>`. A recusa de `start` por já haver outro item `in-progress`
    no mesmo pai **não** é exit 3: é recusa de transição, **exit 1**, sem escrever — o dado não é
    ambíguo.
  - Forma da mensagem de E-2 nestes dois verbos (`DB-40`, a mesma de `next`): uma ocorrência de
    `linha de status ausente para <ID>` por **ID distinto** sem a linha, em ordem alfabética
    crescente do `<ID>`, separadas por `, ` — item alvo e pai dele sem a linha produzem as duas
    ocorrências na mesma mensagem. A função de E-2 usada aqui é a que a `BKL-T3b` normaliza em
    `.claude/tools/backlog.py`: este card **reusa**, não reescreve a regra.
  - `--nota` apensa um sub-bullet datado `  - AAAA-MM-DD \`<estado>\` — <texto>` sob
    `- **Notas de execução:**` do item e **nunca** toca a célula `Status` do índice (`DB-30`).
  - Num ato, `status` escreve: a linha `Status` do item · o apenso da nota, se houver `--nota` · a
    célula do índice · o par `<done>/<total>` do pai pela fórmula da `DB-36` (`<total>` = filhos
    diretos com `Status` diferente de `cancelled`; `<done>` = destes, os com `Status` igual a
    `done`) · o bloco entre `<!-- fila:gerada -->` e `<!-- /fila:gerada -->`, com um bullet por pai
    vivo na forma de §2.3 (`DB-33`): token `` `P-NNNN` `` para pai plano, `` `TK-<n>` `` para pai
    tíquete, na ordem das linhas do índice.
  - As funções recebem `repo` e caminhos já resolvidos por parâmetro e nunca leem `sys.argv`
    (`DB-1`); o módulo é carregado nos testes por `importlib`, como em `tests/test_telemetria.py`.
- **Testes:** TF cada transição válida escreve campo + célula + `<done>/<total>` + bloco gerado;
  TF `blocked` sem `--razao` recusa; TF transição inválida não escreve nada (hash antes = depois);
  TF `--nota` apensa sub-bullet datado e **nunca** toca a célula do índice (TR do guardrail
  anti-log-narrativo); TF `start` recusa com outro `in-progress` no mesmo plano; TF `diretiva`
  preserva o texto livre. Mais o que a `RP-5` fecha:
  - `test_tf_bloco_gerado_tem_bullet_por_pai` — fechar uma subtarefa do tíquete `TK-90` da fixture
    reescreve o bloco entre `<!-- fila:gerada -->` e `<!-- /fila:gerada -->` com um bullet
    `` - `TK-90` (`<estado>`, 1/2): próxima `TK-90b` `` **e** o bullet do plano vivo, nesta ordem, a
    das linhas do índice (`DB-33`, §2.3); e a célula do índice de `TK-90` passa a `1/2` (`DB-36`).

  E o que a `RP-6` fecha (`DB-37`):
  - `test_tf_status_recusa_pai_sem_linha_de_indice` — `status` sobre item cujo pai não tem linha no
    índice, na cópia de `tests/fixtures/backlog/next_tk90_sem_indice/` feita no `tmp_path` do
    pytest: afirma exit 3, a substring `linha de índice ausente para ` seguida do ID do pai, e que
    o hash de cada arquivo da cópia é o mesmo antes e depois da chamada.
- **Não fazer:** não implementar `drain` (é a `BKL-T5`) nem tocar o verbo `next` (são a `BKL-T3a` e
  a `BKL-T3b`);
  não editar os arquivos de `tests/fixtures/backlog/next_tk90/` nem de
  `tests/fixtures/backlog/next_tk90_sem_indice/` — o teste que escreve copia a fixture para o
  `tmp_path` do pytest; não rodar o instrumento contra `docs/DIARIO_DE_OBRAS.md` nem contra
  `docs/plans/` do repositório real; não editar `.claude/agents/`, `docs/DIARIO_DE_OBRAS.md`,
  `docs/telemetria.tsv`, `docs/plans/*` nem `docs/RDO/*`.
- **Contingências:**
  - se nenhuma fixture de `tests/fixtures/backlog/` tiver um pai cujo par `<done>/<total>` mude com
    uma única chamada `status` → montar no `tmp_path` do pytest a cópia editada que o TF exige, sem
    alterar as fixtures do repositório, e devolver na linha de retorno da entrega a frase
    `contingência 1 acionada: cópia de fixture editada no tmp_path para o TF <nome>` (`DB-30`).
  - se um teste já existente de `tests/test_backlog.py` falhar por causa da escrita nova do bloco
    `Fila corrente` → seguir com o ajuste das asserções desse teste à forma de §2.3 e devolver na
    linha de retorno da entrega a frase
    `contingência 2 acionada: asserções de <nome do teste> ajustadas à §2.3` (`DB-30`).
  - se §2.3, §2.7 ou a tabela de §2.5 item 6 admitir duas leituras para o mesmo dado da fixture →
    parar e sinalizar `blocked` razão `premissa`, citando a regra e as duas leituras (`DB-19`).
- **Verificação:**
  1. `python -m pytest tests/test_backlog.py -q` → verde.
  2. `python -m pytest tests/test_backlog.py --collect-only -q` → a lista traz os nomes
     `test_tf_bloco_gerado_tem_bullet_por_pai` e `test_tf_status_recusa_pai_sem_linha_de_indice`.
  3. `python -m pytest tests/ -q` → verde.
- **Pronto quando:** os três comandos da `Verificação` dão o resultado descrito; na cópia da fixture
  no `tmp_path`, uma única chamada `status <ID> done` deixa a linha `Status` do item, a célula do
  índice, o par `<done>/<total>` do pai e o bloco `Fila corrente` coerentes entre si; e `status`
  sobre item cujo pai não tem linha no índice sai exit 3 sem alterar arquivo nenhum da cópia.

### BKL-T5 — `drain`: o inbox sai do contexto [Sonnet · classe implementacao]
- **Status:** `ready` · 2026-09-15 · restrições inline e `Pronto quando` discriminante autorados pela
  `RP-6` (2026-09-18) a partir do achado 3 do `AE-7`.
- **Depende de:** `BKL-T4`; decisão `DB-38` (gramática de linha viva do inbox de planos).
- **Objetivo:** §2.4 — cada linha viva vira linha de índice (`status` do plano lido do cabeçalho
  dele, título da linha 1, âncora = caminho) e é movida verbatim com marca ao histórico; contador
  recalculado; plano sem `Prefixo` ou sem `Status` → exit 3 nomeando o arquivo.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py` — o verbo `drain`.
  - `tests/test_backlog.py` — os TF/TR deste card.
- **Restrições desta tarefa (copiadas inline de §2.4):**
  - Linha viva do inbox de planos: começa com `- `, contém um caminho que casa
    `docs/plans/P-[0-9]{4}-<slug>.md` e **não** começa com `- [drenado ` (`DB-38`). A gramática de
    marcação do inbox de memória não se aplica a este arquivo.
  - Drenar é prefixar `- [drenado AAAA-MM-DD] ` e mover a linha **verbatim** para
    `docs/plans/_INBOX_HISTORICO.md`; o histórico só recebe apenso e nunca é lido (`DB-9`).
  - Contador: `**Próximo id de plano: P-NNNN.**`, recalculado como `max(id visto) + 1`.
- **Testes:** TF linha drenada aparece idêntica (menos o prefixo) no histórico e some do inbox; TF
  inbox vazio é no-op com exit 0; TF plano malformado não drena nada; TR o histórico só cresce. Mais
  o que a `RP-6` fecha:
  - `test_tf_drain_ignora_linha_ja_drenada` — inbox com uma linha viva, uma já prefixada
    `- [drenado AAAA-MM-DD] ` e uma sem caminho de plano: `drain` move **só** a viva, e o histórico
    cresce em exatamente uma linha.
- **Verificação:**
  1. `python -m pytest tests/test_backlog.py -q` → verde.
  2. `python -m pytest tests/ -q` → verde.
- **Pronto quando:** os dois comandos da `Verificação` dão o resultado descrito e, na cópia de
  fixture usada pelos TF, o inbox começa com ao menos uma linha viva pela gramática acima, `drain` a
  move para o histórico e uma chamada seguinte de `next` imprime `inbox de planos: 0 por drenar`.

### BKL-T6 — Migração dos documentos vivos até `check` verde [Sonnet · classe mecanica]
- **Status:** `ready` · 2026-09-15
- **Depende de:** `BKL-T5`
- **Objetivo:** aplicar §2 ao estado real: (a) cabeçalho do diário → diretiva de `DB-11` + bloco
  gerado, com o parágrafo atual da `Fila corrente` movido verbatim para `## TK-54`/`## TK-53`
  conforme o assunto; (b) 26 células do índice → token puro, narrativa movida para a seção do item
  como bullet datado (`backlog`/`decidido em parte` → `cancelled` com razão "absorvido pelo
  P-0738", conforme já diz a própria célula); (c) linha `Status` sob cada item vivo: `TK-38`,
  `TK-48`, `TK-54`, `TK-54a`, `TK-54b`, e `AUT-T1..T10` em `P-0737` (`DB-15`), com data de origem;
  (d) `Próxima tarefa` das seções `P-0737`/`P-0738` → ponteiro fixo (`DB-12`); (e) `Ordem de
  execução` copiada do §7 do `P-0737` para o cabeçalho dele; (f) cabeçalhos `### TK-54a`/
  `### TK-54b` recebem `Sonnet · ` antes de `classe` (`DB-17`); os cards `BKL-T1..T9` já têm
  linha `Status` (aposta pela `RP-1`).
- **Arquivos-alvo:**
  - `docs/DIARIO_DE_OBRAS.md` — cabeçalho, índice e as seções dos itens vivos.
  - `docs/plans/P-0737-loop-autonomo.md` — linha `Status` de cada tarefa `AUT-T1` a `AUT-T10`,
    `Ordem de execução` no cabeçalho e a linha `Próxima tarefa` da seção.
- **Proibido:** apagar texto (mover, nunca remover); tocar `DIARIO_HISTORICO.md`; tocar planos
  `done`/`superseded`.
- **Verificação:**
  1. `python .claude/tools/backlog.py check` → exit 0.
  2. `python .claude/tools/backlog.py next` → devolve `BKL-T7` (efeito da diretiva `DB-11`, não
     `TK-54a`).
  3. `git status --short -- docs/DIARIO_DE_OBRAS.md docs/plans/P-0737-loop-autonomo.md` →
     exatamente duas linhas, uma por caminho (recorte por pathspec: a árvore de trabalho carrega
     registro de orquestração e ato do dono alheios a esta tarefa — `DB-29`).
- **Pronto quando:** `check` verde e `next` responde a próxima tarefa deste plano.

### BKL-T7 — O hook e o ponto de carga [Sonnet · classe implementacao]
- **Status:** `ready` · 2026-09-15
- **Depende de:** `BKL-T6`
- **Objetivo:** `backlog_hook.py` (`DB-8`): lê o JSON do `UserPromptSubmit` em stdin, casa o
  gatilho, roda `next` por importação e devolve `{"hookSpecificOutput": {"hookEventName":
  "UserPromptSubmit", "additionalContext": <saída>}}`; sem gatilho, sai em silêncio; exit ≠ 0 do
  `next` vira texto de contexto (nunca bloqueia o prompt). Registro em `.claude/projecoes.json`
  (alvo `projeto`) e `python .claude/tools/materializar.py apply` + `drift` verde.
- **Arquivos-alvo:** `.claude/tools/backlog_hook.py` (novo); `.claude/projecoes.json`;
  `tests/test_backlog.py` (TF gatilho/não-gatilho, TF exit 3 vira contexto).
- **Verificação:** pytest verde; `materializar.py drift` exit 0; `tests/test_materializar.py`
  verde (fixture do projecoes pode exigir ajuste — se exigir, é nota, não bloqueio).
- **Pronto quando:** digitar "execute o próximo passo" numa sessão nova traz o dossiê sem nenhuma
  chamada de ferramenta.

### BKL-T8 — As skills passam a invocar o instrumento [Sonnet · classe redacao]
- **Status:** `ready` · 2026-09-15
- **Depende de:** `BKL-T7`
- **Objetivo:** `proximo-passo` passos 1–3 e 5 → "rode `backlog.py next` / `status`" (a heurística
  em prosa vira ponteiro para §2.5 na skill `diario-de-obras`); `handover` §2 → `status` + nota;
  `scrum-master` passos 2 e 9 → `next`/`status`; `GOVERNANCA.md` §4 bullet "Retomada sem tarefa
  nomeada" → uma frase apontando o instrumento; `CHANGELOG.md` linha sob `## [Não lançado]`;
  apenso em `P-0737` `## 9` ("`AUT-T6` embrulha `backlog.py` em vez de transpor a heurística").
- **Arquivos-alvo** (forma canônica da `DB-26`: um caminho por bullet):
  - `.claude/skills/proximo-passo/SKILL.md` — passos 1–3 e 5; editar pelo fluxo de UoW (artefato
    canônico), como fez a `BKL-T1`.
  - `.claude/skills/handover/SKILL.md` — §2; mesmo fluxo de UoW.
  - `.claude/skills/scrum-master/SKILL.md` — passos 2 e 9; mesmo fluxo de UoW.
  - `GOVERNANCA.md` — §4, bullet "Retomada sem tarefa nomeada".
  - `CHANGELOG.md` — uma linha sob `## [Não lançado]`.
  - `docs/plans/P-0737-loop-autonomo.md` — só o apenso em `## 9`.
- **Não fazer:** não editar `README.md` (é da `BKL-T9`); não tocar `docs/DIARIO_DE_OBRAS.md`.
- **Verificação:** `Grep 'Grep "Próxima tarefa' .claude/skills/` vazio; `Grep backlog.py
  .claude/skills/` ≥ 3 arquivos; `pwsh .claude/checks/check-readme.ps1` inalterado.
- **Pronto quando:** nenhuma skill manda o agente ler diário/inbox para achar ou fechar tarefa.

### BKL-T9 — Aferição e revisão do `README.md` com veredito do dono [Opus + dono · classe redacao]
- **Status:** `ready` · 2026-09-15
- **Depende de:** `BKL-T8`
- **Objetivo:** (a) medir o pickup novo pelo método de `CUSTO_DO_PICKUP.md` `DC-4` (chars da
  saída do hook numa sessão nova + 1º `usage`) e publicar `## 15` (≤ 30 linhas) contra os 77.457
  chars da `## 3` e o alvo de 40.000 da `## 6`; (b) `README.md`: seção de ferramentas ganha
  `backlog.py`/hook, §9 do fluxo descreve o pickup por instrumento; `docs/DOC_MAP.md` entrada da
  `## 15`; `pwsh .claude/checks/check-readme.ps1` exit 0; veredito do dono.
- **Arquivos-alvo** (campo reposto pela `RP-3`, forma canônica da `DB-26` — sem ele `extrair_dossie`
  recusa a tarefa e não há dossiê de evidência):
  - `docs/CUSTO_DO_PICKUP.md` — seção `## 15` nova, ≤ 30 linhas.
  - `README.md` — seção de ferramentas e §9 do fluxo.
  - `docs/DOC_MAP.md` — entrada de índice da `## 15`.
- **Verificação:**
  1. `pwsh .claude/checks/check-readme.ps1` → exit 0.
  2. `Grep "^## 15" docs/CUSTO_DO_PICKUP.md` → 1 match.
  3. `git status --short -- docs/CUSTO_DO_PICKUP.md README.md docs/DOC_MAP.md` → exatamente três
     linhas, uma por caminho (recorte por pathspec: a árvore de trabalho carrega registro de
     orquestração e ato do dono alheios a esta tarefa — `DB-29`).
- **Pronto quando:** a `## 15` de `docs/CUSTO_DO_PICKUP.md` traz o número medido, o
  `check-readme.ps1` sai 0 e o dono dá o veredito do espelho (o aceite do dono é parte desta
  tarefa, `DB-20`).

## 5. Verificação de ponta a ponta

1. `python -m pytest tests/ -q` verde (suíte inteira: `rdo`, `telemetria`, `materializar`,
   `backlog`).
2. `python .claude/tools/backlog.py check` exit 0 no repo real.
3. Sessão nova, prompt "execute o próximo passo": o dossiê chega pelo hook; nenhum `Read` de
   `DIARIO_DE_OBRAS.md`/`_INBOX.md` no transcript.
4. `backlog.py status <ID> review --nota "…"` → `git diff` mostra só campo, célula, bloco gerado e
   nota; `check` continua verde.
5. `## 15` de `docs/CUSTO_DO_PICKUP.md` com chars medidos abaixo de 40.000.

## 6. Riscos

| Risco | Mitigação |
|---|---|
| Migração (`BKL-T6`) perder narrativa do índice | `DB-10` + regra "mover, nunca remover" + diff revisado antes do commit |
| Hook roda `next` num repo com `check` vermelho e injeta erro a cada prompt | Gatilho estreito (`DB-8`); erro vira 1 linha de contexto com o conserto nomeado |
| `AUT-T6` (P-0737) e `BKL-T8` editarem as mesmas skills | `BKL-T8` é transitório e menor; apenso em `P-0737` `## 9` avisa a `AUT-T6` |
| Parser de `rdo.py` sem prefixo trava a revisão de toda tarefa dos planos vivos | **Ocorreu** (`AE-2`, 2026-09-16): entrou em escopo por `DB-21`/`DB-22` e virou a tarefa `BKL-T2a`; sem retroação para tarefa já fechada (`DB-23`) |
| Confronto de escopo sem atribuição por tarefa enche o dossiê de falso positivo e tira poder do gate | **Ocorreu** (`AE-3`, 2026-09-16, 38 falsos positivos na `BKL-T2` e 7 na `BKL-T2a`): entrou em escopo por `DB-25`/`DB-26`/`DB-27` e virou as tarefas `BKL-T2b` e `BKL-T2c`; sem retroação (`DB-23`) |
| O balde de registro da orquestração (`DB-25`) esconde arquivo que o próprio executor tocou sem declarar | O dossiê **lista** cada caminho do balde com a atribuição ao lado, então o revisor vê o fato; `.claude/agents/` fica fora da lista fechada; o card de cada executor nomeia os caminhos proibidos em `Não fazer` |
| Atribuição a outra tarefa do mesmo plano cobre arquivo tocado por descuido nesta tarefa | A atribuição casa por caminho exato e sai impressa como `arquivo → tarefa`; o revisor confronta com a linha de retorno da entrega, que lista os arquivos tocados (`DB-10`) |
| Edição de agente pendente na árvore compartilhada zera o poder discriminante do veredito de `escopo` | **Ocorreu** (`AE-4`, 2026-09-16, em três dossiês: `BKL-T2a`, `BKL-T2b`, `BKL-T2c`): entrou em escopo por `DB-32` e virou a tarefa `BKL-T2e`; sem retroação para tarefa já fechada (`DB-23`) |
| O balde do ato do dono (`DB-32`) esconde edição de agente feita por quem executa | O dossiê **imprime** o caminho com o rótulo `Ato do dono, fora do ciclo de tarefa`, então o revisor vê o fato; o `Não fazer` de cada card proíbe tocar `.claude/agents/`; o revisor confronta com a linha de retorno da entrega (`DB-10`) |
| Contingência acionada não chega à linha `**Status:**` e some no diff | **Ocorreu** (`AE-4`, 2026-09-16, `BKL-T2c`): a `DB-30` fixa a residência e a forma da devolução; até a `BKL-T4` entregar o `--nota` de `backlog.py status`, a orquestração escreve a linha `Status` à mão, como fez no fechamento da `BKL-T2c` |
| Projeção do instrumento nomeia o pai numa forma só, e o vencedor pode ter pai-tíquete | **Ocorreu** (`AE-6`, 2026-09-17, `BKL-T3` devolvida `blocked` sem nenhuma edição): entrou em escopo por `DB-33`..`DB-36`, que fecham §2.6 (linha 2 e `antecessora`), §2.3 (bullet por pai), §2.5 regra 4 e §3 para os dois tipos de pai no mesmo ato; não gera tarefa nova — a `BKL-T3` e a `BKL-T4` absorvem os TF |
| Condição de erro enumerada num card sem literal de mensagem, sem TF e sem fronteira contra o lint vizinho | **Ocorreu** (`AE-7` achado 1, 2026-09-17, `BKL-T3` fechada com ressalva 94% e `rota` `parcial`): entrou em escopo por `DB-37` — a lista única de §2.5 item 6 tem três condições, uma substring obrigatória por condição e destino nomeado para o que saiu (`C-4`/`C-9`, `C-7`, `drain`); os TF que faltavam são da `BKL-T3a`; sem retroação (`DB-23`) |
| Cópia inline de lista normativa num card diverge da decisão que ela cita | **Ocorreu** (`AE-7` achado 2, 2026-09-17: `DB-6` listava `plano vivo sem prefixo` e a `BKL-T3` listava `pai vivo sem linha no índice` como quarta condição de exit 3): `DB-37` tira a enumeração da `DB-6` e a põe em §2.5 item 6, residência única de onde toda cópia deriva (`DB-2`); a cópia do card `done` fica como registro e deixa de ser residência |
| Campo de saída cujo valor nenhum TF afirma, com a gramática errada passando despercebida | **Ocorreu** (`AE-7` achado 3, 2026-09-17, desvio medido em `_contar_pendentes_inbox`: a gramática do inbox de memória aplicada ao inbox de planos, com as duas fixtures da `BKL-T3` dando 0 pelas duas regras): `DB-38` fixa uma gramática por arquivo e a `BKL-T3a` entrega a fixture discriminante (linha viva, linha drenada, linha sem caminho de plano) mais o TF que afirma o valor impresso |
| Condição de erro implementada pela metade porque o TF só exercita metade do sujeito que a norma enuncia | **Ocorreu** (`AE-8` achado 1, 2026-09-18, `BKL-T3a` fechada com ressalva 94% e `rota` `parcial`): E-2 enuncia "item candidato **ou pai de candidato**" e só a metade "item" tinha TF — `next` elegia por heurística com o tíquete-pai sem `Status`; entrou em escopo por `DB-40`/`DB-42` e virou a tarefa `BKL-T3b`, cujo TF afirma as duas metades na mesma cópia de fixture; sem retroação (`DB-23`) |
| Cópia inline de gramática de string com a forma certa, e código com a forma errada por um caractere | **Ocorreu** (`AE-8` achado 2, 2026-09-18: a Restrição da `BKL-T3a` dizia `- ` e `_contar_inbox_memoria` testava `-`, fazendo a régua `---` contar como candidato): `DB-41` fixa que o espaço faz parte do prefixo e a `BKL-T3b` entrega o TF sobre corpus em que as duas leituras discordam (2 contra 3); o contador irmão `_contar_inbox_planos`, que já usava `- `, não é tocado |
| `Verificação` de card afirma estado da árvore inteira e falha por estado alheio à tarefa | **Ocorreu** (`AE-5`, 2026-09-16, `BKL-T2d`): emenda mecânica de recorte por pathspec (`git status --short -- <caminho> …`) nos cards vivos que a carregavam, `BKL-T6` e `BKL-T9`, na forma que a `RP-4` fixou na `BKL-T2e` (`DB-29`); cards `done` não se reabrem (`DB-23`) |

## 7. Registro (após aprovação, Controle 1.1 — não é execução)

Copiar este plano para `docs/plans/P-0739-backlog-instrumento.md`; apensar linha em
`docs/plans/_INBOX.md` e atualizar `Próximo id: P-0740`; reescrever a diretiva (`DB-11`) movendo o
texto atual para `## TK-54`; apenso em `P-0737` `## 9`. Depois, parar (Regra 1).

## Achados da execução

### AE-1 — `BKL-T2` blocked: tabela §2.1 não descreve cabeçalho de tíquete/subtarefa sem ambiguidade

**2026-09-16, achado do executor (`pantonic-executor`), devolvido sem decisão (Regra 8).**

A linha `tíquete` da tabela §2.1 acima (idêntica em `.claude/skills/diario-de-obras/SKILL.md:135-137`)
tem a coluna "cabeçalho" preenchida só com `idem`:

```
| tíquete | `docs/DIARIO_DE_OBRAS.md`, `## TK-<n> — <título>` | idem | mesmos campos da tarefa (`Status`, `Tipo`, `Notas de execução`) |
```

`idem` remete, por convenção de tabela, ao valor da linha `tarefa` logo acima — heading nível 3
com bracket (`### <ID> — <título> [<modelo> · classe <classe>]`, `DP-C`). Mas a própria coluna
"residência viva" desta mesma linha já mostra o cabeçalho completo e diferente: heading nível 2,
sem bracket (`## TK-<n> — <título>`). As duas leituras da tabela produzem parsers e vereditos de
`check` diferentes:

- **Leitura A** — cabeçalho de tíquete é `## TK-<n> — <título>` (nível 2, sem bracket), como a
  própria célula "residência viva" mostra.
- **Leitura B** — `idem` clona o valor inteiro da célula "cabeçalho" da linha `tarefa`: nível 3,
  com bracket `[<modelo> · classe <classe>]`.

**Confronto com o estado real do diário** (nenhuma das duas bate integralmente):

```
docs/DIARIO_DE_OBRAS.md:705   ## TK-23 — A variante (b) do proxy de ocupação de contexto        (nível 2, sem bracket → bate com A)
docs/DIARIO_DE_OBRAS.md:721   ## TK-38 — Comunicação entre agente e humano — ...                (nível 2, sem bracket → bate com A)
docs/DIARIO_DE_OBRAS.md:729   ## TK-54 — Extrato do custo de abertura de uma janela principal   (nível 2, sem bracket → bate com A)
docs/DIARIO_DE_OBRAS.md:1170  ### TK-54a — O extrato [classe investigacao]                       (nível 3, bracket sem "<modelo> ·" → não bate com A nem B)
docs/DIARIO_DE_OBRAS.md:1233  ### TK-54b — A fonte da bimodalidade [classe investigacao]         (nível 3, bracket sem "<modelo> ·" → não bate com A nem B)
```

Tíquete-pai bate com a leitura A; subtarefa não bate com nenhuma leitura nem com o `DP-C` citado
(falta `<modelo>` no bracket). A tabela §2.1, como publicada, não descreve nenhum estado do mundo
de forma inequívoca — três formas coexistem no repo real (`[Sonnet · classe implementacao]` nas
tarefas de plano, `## TK-n` sem bracket nos tíquetes, `[classe investigacao]` nas subtarefas) e a
tabela não nomeia qual é a normativa para tíquete/subtarefa.

**Por que bloqueia `BKL-T2` especificamente:** a tarefa exige que `check` acuse violações de §2 e
que a lista de defeitos reais vá para `BKL-T6` como insumo. Um parser escrito sobre uma aposta do
executor entre A/B produziria uma lista de defeitos construída sobre leitura não autorizada — a
mesma classe de decisão que a Regra 8 reserva ao dono/planejamento.

**Pendência para a próxima rodada de planejamento:** decidir a forma normativa do cabeçalho de
tíquete e de subtarefa (opções: ratificar leitura A, ratificar leitura B, ou redigir uma terceira
forma que descreva o real e ajustar tabela + migração `BKL-T6` de acordo) e corrigir a célula
"cabeçalho" da linha `tíquete` em §2.1 (aqui e em `SKILL.md:135-137`) para não depender de `idem`
ambíguo. Sem essa decisão, `BKL-T2` não pode ser retomada.

**Escopo não tocado pelo executor:** `.claude/tools/backlog.py`, `tests/test_backlog.py`,
`tests/fixtures/backlog/` seguem inexistentes; nenhum outro arquivo foi criado ou editado.

**Desfecho (`RP-1`, 2026-09-16):** absorvido. Decisões `DB-17`..`DB-19`; tabela §2.1 corrigida aqui e na
skill `diario-de-obras`; card `BKL-T2` reescrito com a gramática e as violações inline; `BKL-T2`
volta a `ready` e é a próxima tarefa (diretiva e `Fila corrente` do diário).

### RP-1 — Rodada de replanejamento sobre `AE-1` (2026-09-16, classe replanejamento)

**Classificação:** técnica — a forma do cabeçalho é gramática do instrumento, não objetivo,
prioridade nem escopo; decidida pelo planejador (`DB-17`..`DB-19`), sem rodada de decisões ao dono.
O dono pediu a rodada, a análise crítica da causa e a governança do gatilho.

**Análise crítica — por que o plano nasceu com o defeito:**

1. **Gramática autorada sem inventário do corpus.** A §2.1 saiu da `DP-C` e da memória do
   planejador, não de um dossiê com as formas reais do diário. O plano não tem `## 1. Fatos
   estabelecidos` (esqueleto obrigatório do agente): a tabela não tinha contra o que ser testada,
   e as três formas reais (tarefa de plano com `[<modelo> · classe]`, tíquete `##` sem bracket,
   subtarefa `###` com `[classe …]` sem modelo) nunca foram confrontadas com as linhas dela. O
   inventário `F-1` que agora precede §2 é o que faltava.
2. **`idem` é ponteiro dentro de tabela.** A auto-auditoria do planejador proíbe restrição por
   ponteiro no card e tem léxico proibido, mas a lista não cobria remissão em tabela normativa
   (`idem`, `análogo`) e a auditoria é feita card a card: a §2, que os cards citam por ponteiro,
   não passou por nenhuma passada.
3. **Card com restrição por ponteiro.** `BKL-T2` dizia "acusa cada violação de §2" em vez de
   enumerar as violações inline; o executor frio precisou abrir a §2 e foi ele quem achou a
   contradição — no momento mais caro (contexto de execução aberto, nada produzido).
4. **Sem contingência para forma desconhecida.** O card não dizia o que fazer com forma real fora
   da gramática. Com `DB-19`, só ambiguidade *da gramática* bloqueia; dado que não casa vira
   violação nomeada.
5. **Registro do plano incompleto.** O plano foi aprovado e o inbox recebeu a linha, mas o índice
   do diário não ganhou a linha `P-0739` e a `BKL-T1` rodou sem drenar o inbox — o kanban não
   sabia que o plano existia. Corrigido nesta rodada (linha drenada, índice atualizado).
6. **Custo.** Um contexto de executor Sonnet sem produto, mais esta rodada. A pergunta ao scout
   que evitaria tudo ("liste todas as formas de cabeçalho `## TK-` e `### TK-` do diário, com
   linha e contagem") custaria um dossiê de ≤ 10 linhas na fase 1.

**Lição para o planejador** (aplicada em `.claude/agents/pantonic-planner.md`): fase 1 exige
inventário do corpus para plano de parser/lint/migração/gramática; fase 4 ganha o teste do parser
frio (toda linha da gramática com exemplo real, toda forma real com destino) e `idem`/`análogo`
entram no léxico proibido, inclusive em célula de tabela.

**Governança** (aplicada em `GOVERNANCA.md` §7 item 17, `G-REPLAN`): bloqueio por `premissa` abre a
rodada de replanejamento como próxima tarefa do plano, roteada ao planejador; `scrum-master`
`A3b`, `proximo-passo` e `diario-de-obras` alinhados; `CHANGELOG.md` sob `## [Não lançado]`.

**Saída:** `DB-17`..`DB-20`; `F-1`; §2.1 corrigida aqui e na skill; `BKL-T2` reescrita, `ready`, no
topo da fila (diretiva + `Fila corrente` do diário); cards `BKL-T1..T9` com linha `Status`;
`P-0739` `in-progress` (1/9) no índice; `AE-1` absorvido. Consumo: `docs/telemetria.tsv`
(`BKL-RP1`, contado).

### AE-2 — `BKL-T2` blocked: o dossiê de evidência não pode ser gerado para ID prefixado

**2026-09-16, achado do orquestrador no pickup, devolvido sem decisão (Regra 8). Decisão do dono
no mesmo ato: anotar como bloqueio do card e escalar ao planejador na janela seguinte.**

A entrega da `BKL-T2` existe e está verde, mas a **rodada de revisão** que a `Fila corrente` exigia
antes da `BKL-T3` não roda — o `review_evidence.py` não localiza a tarefa:

```
$ python .claude/tools/review_evidence.py --plano docs/plans/P-0739-backlog-instrumento.md \
    --tarefa BKL-T2 --desde HEAD --out docs/RDO/evidencia/P-0739-BKL-T2.md
review_evidence: FALHOU - tarefa: 'BKL-T2' não encontrada em 'docs\plans\P-0739-backlog-instrumento.md'
```

**Causa medida:** o `review_evidence.py` reusa `extrair_dossie` de `.claude/tools/rdo.py:186`, que
casa o heading por `_ID_HEADER_RE = ^### (T[0-9]+[a-z]?)(?=[\s—])` (`rdo.py:79`) e por
`_HEADER_BRACKET_RE` (`rdo.py:80-84`) — as duas **sem** o prefixo opcional que a `DB-14` tornou
normativo (`(?:[A-Z0-9]+-)?T[0-9]+[a-z]?`). São os dois únicos pontos: `grep -n 'T\[0-9\]'` não casa
mais nada em `rdo.py` e não casa nada em `review_evidence.py`.

**O que ainda funciona:** `rdo.py laudo --plano P-0739 --tarefa BKL-T2` aceita o ID prefixado — o
gerador do laudo não passa por `extrair_dossie`. O bloqueio é só no dossiê de evidência, que o
protocolo do `pantonic-reviewer` nomeia como uma das "três entradas de julgamento, e só elas" e que
é a autoridade mecânica sobre as dimensões `guardas` e `testes`.

**Alcance:** os três planos vivos usam prefixo — `AUT-*` (`P-0737`, 10 tarefas), `CTX-*` (`P-0738`,
17) e `BKL-*` (`P-0739`, 9). Nenhuma tarefa deles é revisável pelo instrumento hoje. O precedente
que a própria `DB-14` registra ("por isso não há RDO de `CTX-*`") era fechar sem RDO — desfecho que
nunca foi decidido em lugar nenhum, só herdado.

**Por que não foi corrigido no pickup:** a §6 deste plano gateia a correção no dono ("Achado
registrado (`DB-14`), fora de escopo; tíquete só se o dono pedir") e a rota de um plano é do dono
(Regra 8). Consultado no ato, o dono optou por anotar o bloqueio e escalar.

**Rota:** `RP-2` — rodada de replanejamento sobre este achado, delegada ao `pantonic-planner` na
próxima janela (`G-REPLAN`, `GOVERNANCA.md` §7 item 17). É a **próxima tarefa do plano**: a
`BKL-T3` não é despachada enquanto a rodada não fechar. Matéria a decidir: se o gate de revisão
vale para plano com ID prefixado e, valendo, por qual rota (corrigir as 2 regexes de `rdo.py` mais
regressão em `tests/test_rdo.py`, ou outra).

**Não descartar:** a entrega da `BKL-T2` está no repositório e verde (`.claude/tools/backlog.py`,
`tests/test_backlog.py`, `tests/fixtures/backlog/{verde,vermelho}/`) — o bloqueio é da revisão, não
do entregável. Pelo fechamento (c) da máquina de transições, `blocked` por escalada não dispara RDO.

**Desfecho (`RP-2`, 2026-09-16):** absorvido. Decisões `DB-21`..`DB-24`; tarefa `BKL-T2a` autorada
(correção de `rdo.py` + regressão em `tests/test_rdo.py`); `BKL-T2` volta a `review` — a rodada de
revisão dela roda depois da `BKL-T2a`; plano de volta a `in-progress`.

### RP-2 — Rodada de replanejamento sobre `AE-2` (2026-09-16, classe replanejamento)

**Classificação:** técnica — a matéria é gramática de ID de um instrumento do kit e a rota de
correção dele, não objetivo, prioridade nem doutrina. Decidida pelo planejador (`DB-21`..`DB-24`),
sem rodada de decisões ao dono. Teste de legitimidade do escalonamento, item a item: (a) o escopo
publicado do `P-0739` **não** muda de objetivo — ganha uma tarefa de instrumento que o próprio plano
já precisava para fechar a `BKL-T2`; (b) o escopo publicado do `P-0737` **não** muda (`DB-24`: o
card da `AUT-T4` nunca citou `_ID_HEADER_RE`, e nenhum arquivo dele é editado); (c) o default de
"todo trabalho passa pelo gate de revisão" se deriva da doutrina vigente (`GOVERNANCA.md`, protocolo
do `pantonic-reviewer`, `RUBRICA_DE_REVISAO.md`) — o precedente contrário nunca foi decidido, só
herdado. Nada aqui é estratégico.

**A pergunta que a `AE-2` colocou, e a resposta:** "o gate de revisão vale para plano com ID
prefixado?" — vale, sem exceção (`DB-21`). A alternativa (fechar sem dossiê de evidência, como
aconteceu com `CTX-*`) tira do revisor a autoridade mecânica sobre `guardas` e `testes` e transforma
uma limitação de 2 regexes em doutrina por omissão. O custo da correção é uma tarefa de instrumento
com 2 substituições e 4 testes; o custo da omissão é toda tarefa de todo plano vivo fechada sem
evidência.

**Análise crítica — por que o plano nasceu com o defeito:**

1. **Achado conhecido, gateado no dono sem necessidade.** A `DB-14` registrou o defeito de
   `_ID_HEADER_RE` no ato do planejamento e o mandou para fora de escopo ("tíquete só se o dono
   pedir"), com a mesma frase repetida na linha de riscos da §6. Mas o plano **depende** do gate de
   revisão para fechar cada tarefa: o defeito não era adjacente, era pré-requisito. Achado que
   bloqueia o próprio plano não é "fora de escopo" — é tarefa do plano.
2. **Consequência não derivada na autoria.** O planejador viu a causa (`rdo.py` só aceita `T<n>`) e
   não derivou o efeito (nenhuma tarefa `BKL-*` seria revisável), porque a §6 tratou o item como
   risco de terceiro e não como caminho crítico do próprio plano. A pergunta que faltou na fase 1 é
   de uma linha: "as ferramentas do gate de revisão aceitam o ID prefixado que este plano usa?".
3. **Precedente herdado passou por doutrina.** "Por isso não há RDO de `CTX-*`" foi escrito como
   constatação e valeu como regra nas duas rodadas seguintes, sem nunca ter sido decidido. Desfecho
   de exceção que ninguém decidiu é dívida silenciosa — `DB-21` a fecha por escrito.
4. **Custo.** Um pickup do orquestrador consumido sem despachar tarefa, mais esta rodada. A
   pergunta da (2), feita na fase 1, teria custado um dossiê de ≤ 5 linhas.

**Lição para o planejador** (classe de erro nova — instrumento do gate de aceite não exercitado
contra a convenção que o próprio plano adota): o teste de interrupção (fase 4, item 8) já manda
verificar "instrumento do kit citado sem a chamada exata já sondada", mas só dentro do card. Esta
rodada mostra a mesma falha **fora** do card: o instrumento que fecha a tarefa (`review_evidence.py`,
`rdo.py close`) não é citado por card nenhum e por isso escapou da auditoria. Verificação a
acrescentar: **plano que introduz ou usa convenção de identificador, caminho ou nome de artefato
verifica, na fase 1, que os instrumentos do gate de aceite aceitam essa convenção — e, se não
aceitam, a correção do instrumento é tarefa do plano, nunca achado adiado.**

**Aplicada em 2026-09-16, por ordem do dono:** o texto acima entrou em
`.claude/agents/pantonic-planner.md`, fase 1 (último bullet da lista de encaminhamento), como fez a
`RP-1`, com a linha correspondente em `CHANGELOG.md` sob `## [Não lançado]`.
Arquivo de definição de agente é configuração do harness: quem o edita é o dono (ou uma tarefa
autorada por ele), não o próprio agente dentro da rodada. O `P-0739` não depende dessa edição para
seguir — a `BKL-T2a` está fechada e despachável desde já.

**Saída:** `DB-21`..`DB-24`; card `BKL-T2a` (`ready`, próxima tarefa do plano); `BKL-T2` de volta a
`review`, com a rodada de revisão despachada depois da `BKL-T2a`; §6 riscos atualizada; `P-0739`
de volta a `in-progress` (10 tarefas); `AE-2` absorvido. Nenhum arquivo fora deste plano foi editado
nesta rodada.

### AE-3 — O confronto de `escopo` do gate de revisão não atribui arquivo a tarefa

**2026-09-16, achado convergente das duas revisões (`pantonic-reviewer`), devolvido sem decisão
(Regra 8).** Laudos: `docs/RDO/laudos/P-0739-BKL-T2.md` (ressalva 94%, bloqueante nenhuma) e
`docs/RDO/laudos/P-0739-BKL-T2a.md` (aprovado 100%, bloqueante nenhuma). **Sem retroação sobre as
duas entregas:** as sete dimensões fecharam sem vermelho mecânico, e o achado é de processo — alvos
`doutrina` e `dossiê`, não da execução.

Três defeitos independentes, todos na seção `Escopo` do dossiê que `review_evidence.py` produz:

1. **Alvo `doutrina` — não há guardrail de atribuição por tarefa.** O recorte do instrumento é
   `git`, e `git` não sabe qual tarefa tocou qual arquivo. Na `BKL-T2` isso rendeu 38 falsos
   positivos de fora-de-alvo: o commit `6d7433c` mistura a entrega da tarefa com doutrina (`G-NOASK`)
   e material de outras rodadas, e a árvore de trabalho carrega a entrega da `BKL-T2a` mais as
   edições de registro da própria orquestração (`docs/DIARIO_DE_OBRAS.md`, este plano,
   `docs/telemetria.tsv`, `.claude/agents/pantonic-planner.md`). Arquivos nomeados no "Não fazer" do
   card aparecem como violação sem que a entrega os tenha tocado. Rotas possíveis: exigir entrega
   isolada por commit antes da revisão, ou dar atribuição por tarefa ao `review_evidence.py`.
2. **Alvo `dossiê` — o campo `Arquivos-alvo` não é legível pelo instrumento.** No card da `BKL-T2a`
   o campo mistura caminhos com literais de regex e ranges de linha; o parser extraiu
   `_ID_HEADER_RE = re.compile(...)` como se fosse um arquivo-alvo e **perdeu** `CHANGELOG.md`, que
   era alvo real. A seção `Escopo` daquele dossiê ficou sem poder discriminante (7 fora-de-alvo, 6
   deles da orquestração e 1 alvo real não reconhecido). Falta a forma canônica do campo.
3. **Alvo `rubrica` — o gerador não tem o campo que a rubrica exige.** `docs/RUBRICA_DE_REVISAO.md`
   §6 define achado de processo com campo próprio e três alvos; `rdo.py laudo` não o implementa, e o
   único canal disponível é `--escalar`. Os dois laudos desta rodada usaram `--escalar` para achado
   de processo, o que força a recomendação a `escalar` sem que haja pendência de arquitetura ou de
   requisito — o canal está sobrecarregado e o veredito, distorcido.

**Observação de card, do laudo da `BKL-T2`:** o item "lista de defeitos reais colada na nota" do
critério de pronto acabou re-derivado pela orquestração. Critério de pronto que exige ato de
registro fora dos arquivos-alvo tende a ser fechado por quem orquestra, não por quem executa — e o
card não ganha poder discriminante com ele. (Motivo da única dimensão fora de `conforme` na série:
`registro` `parcial` na `BKL-T2`.)

**Pendência para a próxima rodada de planejamento (`RP-3`):** decidir a rota de cada um dos três
itens e a forma canônica de `Arquivos-alvo`, sem retroação sobre `BKL-T2`/`BKL-T2a`. Enquanto a
rodada não fechar, a `BKL-T3` não é despachada (`G-REPLAN`).

**Defeito menor observado no mesmo instrumento (insumo da `RP-3`, 1 linha):**
`review_evidence.py` escreve o documento em `stdout` sem forçar UTF-8 e estoura
`UnicodeEncodeError: 'charmap' codec can't encode character '→'` no console cp1252 do
Windows quando o dossiê contém `→`. A escrita via `--out` não é afetada; o contorno usado nesta
rodada foi `PYTHONIOENCODING=utf-8`.

**Desfecho (`RP-3`, 2026-09-16):** absorvido. Decisões `DB-25`..`DB-29`; três tarefas autoradas
(`BKL-T2b`, `BKL-T2c`, `BKL-T2d`), todas `ready`; campo `Arquivos-alvo` da `BKL-T8` reescrito na
forma canônica e o da `BKL-T9` reposto (estava ausente); §6 riscos com quatro linhas novas; plano
segue `in-progress` com 13 tarefas. Sem retroação sobre `BKL-T2`/`BKL-T2a` (`DB-23`).

### RP-3 — Rodada de replanejamento sobre `AE-3` (2026-09-16, classe replanejamento)

**Classificação:** técnica e tática — a matéria é o recorte que um instrumento de revisão mede, a
forma de um campo de card e um campo novo no gerador de laudo. Decidida pelo planejador
(`DB-25`..`DB-29`), sem rodada de decisões ao dono. Teste de legitimidade do escalonamento, item a
item: (a) o objetivo publicado do `P-0739` não muda — ganha três tarefas de instrumento que o
próprio plano precisa para ser julgado; (b) a rota alternativa que **seria** do dono (exigir commit
isolado por tarefa antes da revisão) foi **descartada** por mérito, não adiada: ela é doutrina de
commit, vive só em prosa e nem resolveria o caso, porque o registro da orquestração é escrito depois
da entrega e antes da revisão (`DB-25`); (c) o default "o gate mede fato, e fato ambíguo é defeito
do instrumento" se deriva do `DA-7` e do `DB-6`, já vigentes. Nada aqui é estratégico. Duas lições
de autoria (`DB-26`, `DB-29`) pertencem à anatomia do card, que mora em
`.claude/agents/pantonic-planner.md` — arquivo que só o dono edita (precedente da `RP-2`): elas
ficam registradas aqui e o `P-0739` **não** depende dessa edição para seguir.

**A pergunta que a `AE-3` colocou, e a resposta:** "quem atribui arquivo a tarefa, a disciplina
humana ou o instrumento?" — o instrumento (`DB-25`). `git` não sabe qual tarefa tocou qual arquivo,
mas o **plano** sabe qual tarefa declarou qual alvo, e a orquestração escreve num conjunto fechado e
conhecido de arquivos. Os dois fatos já estavam em mãos do script e não estavam sendo usados: a
atribuição é derivável, não precisa de promessa de ninguém. O que sobra sem atribuição é o fato que
interessa ao revisor, e só ele pesa no veredito.

**Análise crítica — por que o defeito chegou até aqui:**

1. **Instrumento de gate nunca exercitado contra corpus sujo.** `review_evidence.py` foi entregue e
   testado contra repositório de fixture, onde a árvore de trabalho só tem a entrega da tarefa. A
   primeira execução contra o repositório real — com commit misto, entrega de outra tarefa solta e
   registro da orquestração no meio — produziu 38 falsos positivos. A `RP-2` já mandou verificar, na
   fase 1, que os instrumentos do gate **aceitam** a convenção do plano; faltou a face seguinte:
   instrumento que aceita e roda ainda pode não **discriminar** nada.
2. **Campo lido por máquina autorado como prosa.** O `Arquivos-alvo` da `BKL-T2a` foi escrito para
   humano — caminho, prosa e literal de regex no mesmo bullet — enquanto `review_evidence.py` o lê
   como dado. O parser extraiu `_ID_HEADER_RE = re.compile(…)` como arquivo-alvo e perdeu
   `CHANGELOG.md`. O card estava impecável para o executor e ilegível para o instrumento que o
   julga; ninguém tinha escrito qual das duas leituras manda (`DB-26`).
3. **Canal sobrecarregado vira veredito errado.** A rubrica §6 exige campo próprio para achado de
   processo desde que existe; o gerador nunca o implementou, e o único canal disponível (`--escalar`)
   força `recomendacao=escalar`. Os dois laudos de 2026-09-16 saíram com recomendação de escalada
   sem que houvesse pendência de arquitetura ou de requisito. Instrumento que não implementa o
   documento normativo empurra o operador para o canal errado — e o dado registrado fica falso.
4. **Critério de pronto fora do alcance de quem executa.** O item "lista de defeitos reais colada na
   nota" da `BKL-T2` foi fechado pela orquestração, não pelo executor, e derrubou `registro` para
   `parcial` — a única dimensão fora de `conforme` na série. Critério que depende de ato de registro
   não discrimina execução boa de execução ruim (`DB-29`).
5. **Custo.** Duas revisões com a seção `Escopo` sem poder discriminante, mais esta rodada. As três
   perguntas que teriam evitado tudo cabem em três linhas de fase 1.

**Lições para o planejador** (duas classes de erro novas, uma já coberta):

- **Classe nova — instrumento de gate cuja saída nunca foi inspecionada contra o corpus real.**
  Verificação a acrescentar à fase 1: *plano cuja tarefa será julgada por instrumento de gate que
  ainda não rodou contra o repositório real pede um dossiê com uma **saída real** do instrumento
  (≤ 40 linhas); saída sem poder discriminante é tarefa do plano, não achado da revisão.* A
  verificação da `RP-2` ("os instrumentos do gate aceitam esta convenção?") responde se o
  instrumento **roda**; esta responde se o que ele imprime **serve**.
- **Classe nova — campo de card lido por máquina autorado como prosa.** Verificação a acrescentar à
  fase 4: *todo campo do card que um instrumento lê é escrito na forma que o instrumento lê —
  `Arquivos-alvo` carrega um caminho por bullet e nenhum outro literal entre crases; arquivo citado
  para ser evitado vai para `Não fazer`, trecho de código vai para `Texto novo, literal`* (`DB-26`).
- **Classe já coberta, reforçada — critério de pronto sem poder discriminante.** Verificação a
  acrescentar à fase 4, item 2: *`Pronto quando` e `Verificação` só citam efeito nos arquivos-alvo
  do próprio card e comandos que o executor roda; registro em diário, telemetria, RDO, laudo ou
  plano é ato da orquestração e nunca entra no critério de pronto* (`DB-29`).

Como na `RP-1` e na `RP-2`, a publicação desses três parágrafos em `.claude/agents/pantonic-planner.md`
é ato do dono, com a linha correspondente em `CHANGELOG.md` sob `## [Não lançado]`. O `P-0739` não
depende dela: as três tarefas novas estão fechadas e despacháveis desde já. **Publicada em 2026-09-17, por ordem do dono** ("publicar o pantonic-planner; nós iniciamos esse plano exatamente para modificar"): as lições desta rodada estão em `.claude/agents/pantonic-planner.md`, com a linha correspondente em `CHANGELOG.md` sob `## [Não lançado]`.

**Saída:** `DB-25`..`DB-29`; cards `BKL-T2b`, `BKL-T2c` e `BKL-T2d` (`ready`, nesta ordem, antes da
`BKL-T3`); campo `Arquivos-alvo` da `BKL-T8` reescrito na forma canônica e o da `BKL-T9` reposto,
com `Verificação` própria; cabeçalho do plano em 13 tarefas e ordem de execução atualizada; §6
riscos com quatro linhas novas; `AE-3` absorvido; plano segue `in-progress`. Nenhum arquivo fora
deste plano foi editado nesta rodada.

### AE-4 — Onde mora o registro de contingência acionada, e o balde que falta para ato fora do ciclo

**2026-09-16, achado convergente das duas revisões (`pantonic-reviewer`), devolvido sem decisão
(Regra 8).** Laudos: `docs/RDO/laudos/P-0739-BKL-T2b.md` (aprovado 100%, bloqueante nenhuma) e
`docs/RDO/laudos/P-0739-BKL-T2c.md` (aprovado 100%, bloqueante nenhuma). **Sem retroação sobre as
duas entregas:** as sete dimensões fecharam `conforme` nas duas e nenhum dos dois defeitos
rebaixou dimensão — são de processo, alvo `dossiê`.

Dois defeitos independentes:

1. **Residência do registro de contingência acionada não existe.** A contingência 2 da `BKL-T2c`
   manda registrar o ajuste na *"nota de execução"*, mas "nota de execução" não é artefato com
   residência nomeada no repositório: o ajuste da asserção só ficou auditável pelo diff. A linha
   `**Status:**` da `BKL-T2c`, ao contrário da da `BKL-T2b`, não carregava nem a contingência
   acionada nem o ponteiro de consumo — corrigido no fechamento desta rodada, mas a anatomia do
   card continua sem prescrever o lugar. **Rota candidata:** fixar na anatomia do card
   (`.claude/agents/pantonic-planner.md`) que contingência acionada se registra na linha `Status`
   do próprio card.

2. **Ato do dono não tem balde, e por isso todo veredito mecânico de `escopo` sai "aberto".** Por
   desenho da `DB-25`, `.claude/agents/` fica fora do balde de registro da orquestração. Como a
   árvore de trabalho é compartilhada, toda tarefa executada enquanto houver edição de agente
   pendente sai com `.claude/agents/pantonic-planner.md` no balde "fora sem atribuição", e o
   recorte tem de vir do despacho em vez do próprio dossiê de evidência — já observado no laudo da
   `BKL-T2a` e agora **reincidente em duas tarefas**. **Rota candidata:** decidir se cabe um quinto
   balde ("ato do dono / fora do ciclo de tarefa") em `review_evidence.py` ou se a atribuição
   externa continua sendo insumo do despacho, assumida como tal.

Nenhum dos dois é decisão de arquitetura ou de requisito: a rodada `RP-4` os absorve como decisão
técnica/tática, no mesmo precedente da `RP-2` e da `RP-3`. Nenhum bloqueia a `BKL-T2d`, que segue
despachável.

**Absorvido pela `RP-4` (2026-09-16):** defeito 1 → `DB-30` (residência) e `DB-31` (não gera
tarefa); defeito 2 → `DB-32` e a tarefa `BKL-T2e`. Ver `### RP-4` abaixo.

### RP-4 — Rodada de replanejamento sobre `AE-4` (2026-09-16, classe replanejamento)

**Classificação:** técnica e tática nos dois defeitos — a matéria é onde um registro mora e o que um
instrumento de revisão conta como fato atribuível. Decidida pelo planejador (`DB-30`..`DB-32`), sem
rodada de decisões ao dono, no precedente da `RP-2` e da `RP-3`. Teste de legitimidade do
escalonamento, item a item: (a) o objetivo publicado do `P-0739` não muda — ganha uma tarefa de
instrumento e uma regra de autoria; (b) a rota alternativa que **seria** do dono no defeito 2
(mandar o dono trabalhar em branch ou stash separado enquanto houver tarefa em execução) foi
**descartada** por mérito, não adiada: é doutrina de commit sem guarda mecânica, descartada pelo
mesmo argumento que derrubou a rota (a) da `DB-25`; (c) o default "fato ambíguo é defeito do
instrumento" se deriva do `DA-7` e do `DB-6`, já vigentes. Nada aqui é estratégico.

**Defeito 1 — a pergunta e a resposta:** "onde mora o registro de uma contingência acionada?" — na
linha `- **Status:**` do próprio card, escrita pela orquestração a partir da linha de retorno da
entrega (`DB-30`). Os três canais já existiam e ninguém tinha dito qual deles manda: a linha
`Status` existe em todo card vivo (`DB-15`), o `--nota` de `backlog.py status` já está especificado
(§2.7, TF na `BKL-T4`) e a linha de retorno da entrega já é o canal do executor (`DB-10`, `DB-16`).
O card mandava "registrar na nota de execução", frase que não nomeia artefato nenhum e que, lida por
um executor frio, ou vira ato de estado proibido (`DB-16`) ou vira nada — foi o que aconteceu: o
ajuste da asserção da `BKL-T2c` só ficou auditável pelo diff, e a linha `Status` teve de ser
completada no fechamento, por quem orquestra. **Veredito: não gera tarefa** (`DB-31`) — nenhum
instrumento muda, o que muda é autoria de card; a `BKL-T2d` teve as duas contingências reescritas
nesta rodada e a `BKL-T2e` nasce na forma nova.

**Defeito 2 — a pergunta e a resposta:** "quem é o dono de um arquivo que nenhuma tarefa tocou?" — o
instrumento tem de saber dizer "ninguém desta série", e por isso ganha o quinto balde (`DB-32`). A
`DB-25` resolveu três dos quatro casos de arquivo não coberto pelo card (alvo de outra tarefa,
registro da orquestração, resto) partindo de um fato: a atribuição é **derivável**, não depende de
promessa de ninguém. Faltou o quarto caso, que é derivável do mesmo jeito: `.claude/agents/` é
editado só pelo dono, fora do ciclo de qualquer tarefa (precedente firmado na `RP-1`, na `RP-2` e na
`RP-3`), logo nenhum card jamais o declara como alvo e nenhuma tarefa é responsável por ele. Deixar
esse caminho no balde "fora sem atribuição" faz o veredito mecânico de `escopo` sair `aberto` em
**toda** revisão enquanto houver edição de agente pendente — medido em três dossiês seguidos — e
empurra o recorte para o despacho, que é prosa sem guarda. O balde novo não esconde nada: imprime o
caminho com rótulo próprio, e `_REGISTRO_ORQUESTRACAO` continua sem `.claude/agents/`, exatamente
como o `Não fazer` da `BKL-T2c` mandou. **Veredito: gera a tarefa `BKL-T2e`**, fechada e
despachável, que não bloqueia nem depende da `BKL-T2d`.

**Análise crítica — por que os dois defeitos chegaram até aqui:**

1. **Ação de contingência com verbo sem residência.** "Registrar o ajuste na nota de execução" tem
   verbo e objeto, mas não tem **local** — e o teste do executor frio (fase 4, item 2) cobra verbo +
   objeto + **local**. A frase passou em três cards (`BKL-T2`, `BKL-T2a`, `BKL-T2b`, `BKL-T2c`)
   porque soava concreta. Contingência é o ponto do card em que o executor age fora do roteiro:
   é justamente ali que a ação precisa terminar num artefato nomeado.
2. **Balde de classificação desenhado a partir dos casos observados, não do conjunto.** A `DB-25`
   nasceu dos 38 falsos positivos da `BKL-T2`, e o inventário que a sustentou foi a lista de
   arquivos daquela execução. `.claude/agents/pantonic-planner.md` **estava** naquela lista, e
   mesmo assim não ganhou balde: foi tratado como ruído do momento em vez de classe recorrente. Uma
   classificação de vocabulário fechado só está pronta quando **toda** forma do inventário tem
   destino nomeado — a mesma verificação da fase 4, item 7, que o plano aplica a gramática de
   parser e que ninguém aplicou ao conjunto de baldes.
3. **Reincidência tratada como dado do despacho.** O caso apareceu no laudo da `BKL-T2a` e foi
   resolvido por prosa no despacho seguinte ("desconsidere o arquivo de agente"). Achado que volta
   é defeito de instrumento; achado corrigido à mão a cada rodada é imposto de contexto pago em
   toda revisão.
4. **Custo.** Três dossiês com a seção `Escopo` sem veredito discriminante, três despachos com
   recorte manual, mais esta rodada.

**Lições para o planejador** (uma classe de erro nova, uma já coberta e reforçada):

- **Classe nova — ação de contingência sem residência nomeada.** Verificação a acrescentar à fase 4,
  item 3: *toda ação fechada de contingência termina num artefato com residência nomeada; "registrar
  em nota", "anotar", "documentar" sem caminho de arquivo e campo é ponteiro vazio. Contingência
  acionada é **devolvida na linha de retorno da entrega**, na forma `contingência <n> acionada:
  <o que mudou>`, e a orquestração a materializa na linha `**Status:**` do card* (`DB-30`).
- **Classe já coberta, reforçada — classificação de vocabulário fechado sem destino para toda forma
  do inventário.** A fase 4, item 7, já exige isso de gramática de parser; a verificação passa a
  valer para **qualquer** tabela de classificação que um instrumento aplique a um corpus (baldes,
  rótulos, categorias de lint): *cada forma real do inventário casa exatamente um item da
  classificação, e forma que só tem o item "resto" é item faltando, não resíduo* (`DB-32`).

Como na `RP-1`, na `RP-2` e na `RP-3`, a publicação desses dois parágrafos em
`.claude/agents/pantonic-planner.md` é **ato do dono**, com a linha correspondente em `CHANGELOG.md`
sob `## [Não lançado]`. O `P-0739` não depende dela: a `BKL-T2d` e a `BKL-T2e` estão fechadas e
despacháveis desde já. **Publicada em 2026-09-17, por ordem do dono** ("publicar o pantonic-planner; nós iniciamos esse plano exatamente para modificar"): as lições desta rodada estão em `.claude/agents/pantonic-planner.md`, com a linha correspondente em `CHANGELOG.md` sob `## [Não lançado]`.

**Saída:** `DB-30`, `DB-31`, `DB-32`; card novo `BKL-T2e` (`ready`), entre a `BKL-T2d` e a
`BKL-T3`; campo `Depende de` e duas contingências da `BKL-T2d` reescritos na forma da `DB-30`;
cabeçalho do plano em 14 tarefas e ordem de execução atualizada; §6 riscos com três linhas novas;
`AE-4` absorvido; plano segue `in-progress`. Nenhuma entrega fechada foi reaberta (`DB-23`) e
nenhum arquivo fora deste plano foi editado nesta rodada.

### AE-5 — `Verificação` de card afirma estado da árvore inteira, e a própria sprint torna isso insatisfazível

**2026-09-16, achado da execução da `BKL-T2d` (`pantonic-executor`), devolvido sem decisão
(Regra 8).** Entrega verde e fechada como `review`: os quatro testes novos passam, suíte
`110 passed`, nenhuma das quatro contingências do card acionada. **Sem retroação sobre a entrega**
— o defeito é do card, alvo `dossiê`, e não rebaixa dimensão nenhuma.

A Verificação 3 manda `git status --short` devolver *exatamente três caminhos*. A árvore de
trabalho já carregava, antes da tarefa começar, as entregas não commitadas da `BKL-T2a`..`BKL-T2c`,
o registro da orquestração (diário, telemetria, evidência, laudos) e o ato do dono pendente em
`.claude/agents/pantonic-planner.md`. O critério, como escrito, só fecharia numa árvore limpa —
estado que a própria sprint não produz — e por isso **não discrimina**: falha por estado alheio à
tarefa, nunca por defeito dela. É a `DB-29` (autorada pela `RP-3`) contrariada dentro do mesmo
plano: `Pronto quando`/`Verificação` só citam efeito nos arquivos-alvo do card.

A forma correta já existe no plano: a `RP-4` autorou a `BKL-T2e` com recorte por pathspec —
`git status --short -- <caminho> <caminho> <caminho>`, que afirma o mesmo fato sem depender do
resto da árvore. Cards **vivos** que ainda carregam a forma de árvore inteira: `BKL-T3` e `BKL-T4`.
As `BKL-T2b`/`BKL-T2c` também a carregam, mas estão fechadas e não se reabrem (`DB-23`).

Não é decisão de arquitetura nem de requisito. **Rota candidata:** emenda mecânica de uma linha em
cada um dos dois cards vivos, na forma que a `RP-4` já fixou — não exige rodada de replanejamento
própria. **Alternativa:** registrar e não agir, assumindo que o recorte da Verificação 3 é insumo
do despacho. Nada disto bloqueia a `BKL-T2e`, que já nasceu com a forma correta.

**Correção de registro (`RP-5`, 2026-09-17):** a premissa deste achado sobre **quais** cards
carregam a forma de árvore inteira estava errada. O parágrafo acima nomeia `BKL-T3` e `BKL-T4`;
`grep` por `git status --short` sobre este plano, conferido ocorrência a ocorrência na rodada,
mostra que nem a `BKL-T3` nem a `BKL-T4` têm `git status` na `Verificação` (elas verificam por
`pytest`). Os cards **vivos** que carregavam a forma de árvore inteira são a **`BKL-T6`** e a
**`BKL-T9`**, e são esses dois que a `RP-5` emendou para pathspec. Os demais casos da busca são
cards `done` (`BKL-T1`, `BKL-T2a`, `BKL-T2b`, `BKL-T2c`, `BKL-T2d`), que não se reabrem (`DB-23`),
a `BKL-T2e` (já por pathspec, modelo copiado) e prosa (`DB-10` e este próprio achado). Nada aqui
retroage sobre entrega nenhuma: o que se corrige é o registro do achado.

**Absorvido pela `RP-5` (2026-09-17):** emenda aplicada à `Verificação` da `BKL-T6` e da `BKL-T9`.
Ver `### RP-5` abaixo.

### AE-6 — `next` não tem forma de saída para vencedor com pai-tíquete, e o TF "bug antes de FIFO" a exige

**2026-09-17, achado da execução da `BKL-T3` (`pantonic-executor`), devolvido sem decisão e sem
edição (Regra 8).** A triagem parou no primeiro sinal: nenhuma linha de `.claude/tools/backlog.py`
nem de `tests/test_backlog.py` foi tocada, e os demais ramos do card (parsing de `Depende de`,
`Ordem de execução`, diretiva) não chegaram a ser exercitados — o desenho das fixtures desses
testes depende da mesma forma que falta.

**O defeito.** §2.5 regra 4 (`:153`) ordena os elegíveis em três faixas: "(a) tarefas de plano
`in-progress`; (b) tíquetes `Tipo: bug`; (c) FIFO". A faixa (b) tem por sujeito o **tíquete**, não
a tarefa de plano — e tíquete não carrega bracket `[modelo · classe]` (`DB-17`), logo nunca é o
item selecionado: quem vence nesse ramo é uma **subtarefa cujo pai é tíquete**. §2.6 (`:161-169`),
porém, fixa uma única linha de contexto do pai, com rótulo literal `plano:` e os campos
`P-NNNN`/`<done>/<total>`/`residência`/`índice`. Não há no plano inteiro um segundo worked example
nem regra para o caso de pai-tíquete. §2.5 regra 3 (`:151`) já diz "plano/tíquete-pai" ao
descrever elegibilidade — o plano sabe que o pai pode ser tíquete —, mas a distinção não chega a
§2.6. O TF **"bug antes de FIFO"** é obrigatório no card (`:1219-1221`) e só é satisfazível
instanciando exatamente esse caso.

**Alternativas levantadas pela execução, sem preferência** (a escolha é do planejador): (1) mesma
forma com rótulo trocado — `tíquete: TK-<n> — <título> (<done>/<total>) · residência: … · índice:
…`; (2) manter o rótulo literal `plano:` e preencher os campos de plano com substituto (vazio,
`—`, ou o próprio `TK-<n>`); (3) omitir a linha de contexto do pai quando o pai é tíquete; (4)
alguma quarta forma ainda não descrita.

Não é decisão de arquitetura nem de requisito — é forma de saída de instrumento interno, dentro do
escopo já aprovado do plano. **Rota:** rodada `RP-5` (`pantonic-planner`) fecha a forma em §2.6 e
reabre a `BKL-T3`. Enquanto a forma não fechar, a `BKL-T3` fica `blocked` razão `premissa`
(`G-REPLAN`): a `BKL-T4` **não** é despachada na frente dela — e ela consome a mesma forma (escreve
o bloco `Fila corrente`, §3 `:189-191`), logo fechar §2.6 uma vez resolve as duas.

**Oportunidade da mesma rodada, sem custo de decisão:** a emenda mecânica pendente do `AE-5`
(Verificação por pathspec em vez de árvore inteira) incide exatamente nos mesmos dois cards vivos,
`BKL-T3` e `BKL-T4`.

**Absorvido pela `RP-5` (2026-09-17):** forma fechada por `DB-33` (linha de contexto do pai, uma por
tipo de pai, em §2.6 e no bloco `Fila corrente` de §2.3), `DB-34` (linha `antecessora`), `DB-35`
(sujeito da faixa de bug em §2.5 regra 4) e `DB-36` (fórmula de `<done>/<total>`); `BKL-T3` de volta
a `ready`. A oportunidade acima foi aproveitada, mas sobre os cards certos: a premissa do `AE-5`
sobre *quais* cards vivos carregam a forma de árvore inteira estava errada — são a `BKL-T6` e a
`BKL-T9` (ver a correção de registro no `AE-5`). Ver `### RP-5` abaixo.

### RP-5 — Rodada de replanejamento sobre `AE-6` (2026-09-17, classe replanejamento)

**Classificação:** técnica — a matéria é a forma de saída de um instrumento interno, dentro do
escopo já aprovado, e a coerência entre duas seções normativas do mesmo plano. Decidida pelo
planejador (`DB-33`..`DB-36`), sem rodada de decisões ao dono, no precedente da `RP-2`, da `RP-3` e
da `RP-4`. Teste de legitimidade do escalonamento, item a item: (a) **duas respostas levam a planos
materialmente diferentes?** Não — nenhuma das quatro alternativas do `AE-6` muda objetivo, rota,
tarefa ou custo do plano; muda o texto de uma linha impressa por um instrumento que só o próprio
agente lê; (b) **existe default derivável?** Sim, e ele decide: §2.1 e §2.2 já garantem que tíquete
tem cabeçalho com título, seção com residência, linha de índice com âncora e par `<done>/<total>`,
então **nenhum campo da linha 2 precisa de substituto** — a única diferença legítima entre os dois
casos é o rótulo; (c) **o dono já respondeu?** A pergunta nunca lhe foi posta e não precisa ser:
`DB-17` (tíquete sem bracket) e a §2.5 regra 3 ("plano/tíquete-pai") são decisões já vigentes deste
plano, e a forma da linha 2 é consequência delas. Nada aqui é estratégico nem altera escopo.

**O defeito — a pergunta e a resposta:** "como a saída de `next` nomeia o pai do vencedor quando o
pai é um tíquete?" — com o **mesmo conjunto de campos e o rótulo trocado** (`DB-33`, rota (1) do
`AE-6`). O plano já sabia, em §2.5 regra 3, que o pai pode ser tíquete; §2.6 foi escrita a partir de
um caso só — o caso que o próprio `P-0739` vive, em que todo vencedor tem plano-pai — e fixou o
rótulo literal `plano:` com campos de plano. A faixa (b) da §2.5 regra 4 carregava o mesmo vício
pelo outro lado: tinha por sujeito o **tíquete**, que por `DB-17` nunca é o item selecionado, de
modo que a faixa era vazia por construção e o TF obrigatório do card ("bug antes de FIFO") não tinha
como ser instanciado — nem o item a devolver, nem a saída a afirmar. As rotas (2) e (3) do `AE-6` e
mais duas que a rodada levantou estão despachadas com motivo na `DB-33`; a rota (4) ("alguma quarta
forma") foi instanciada e descartada ali como bloco de duas linhas.

**Dois vãos vizinhos fechados no mesmo ato (G-SURFACE):** fechar só o rótulo deixaria a `BKL-T3`
parar de novo três passos adiante. (i) A linha `antecessora` de §2.6 nunca foi definida — nem quem
é, nem o que acontece quando o vencedor é o primeiro irmão, nem o que se imprime quando não há bloco
`Notas de execução` (`DB-34`). (ii) O par `<done>/<total>` aparece em três projeções (§2.6, §2.3,
célula do índice de §2.2/§3) e a fórmula não estava escrita em lugar nenhum; sem ela, `next` e
`status` contariam de jeitos diferentes e o `check` da `DB-2` acusaria divergência no dado que o
próprio instrumento gera (`DB-36`). (iii) O bullet por pai do bloco `Fila corrente` (§2.3) tinha o
mesmo defeito da §2.6 — token fixo `P-NNNN` — e é consumido pela `BKL-T4`: fechar §2.6 sem fechar
§2.3 apenas adiaria o bloqueio da `BKL-T3` para a tarefa seguinte. (iv) A frase de §3 sobre
"candidato a fechamento" falava só de plano, e agora fala de pai, plano ou tíquete.

**Veredito: não gera tarefa nova.** Nenhum instrumento ganha função por causa desta rodada — o que
faltava era forma normativa, e ela cabe inteira nas seções §2.3, §2.5, §2.6 e §3, cujos
implementadores já existem: a `BKL-T3` (`next`, reaberta `ready`) e a `BKL-T4` (`status`). Cada uma
recebeu os TF que trancam a forma nova.

**Emenda do `AE-5` na mesma rodada (mecânica, sem custo de decisão):** a rota já estava fixada pela
`RP-4` — `Verificação` afirma estado da árvore por pathspec, nunca pela árvore inteira (`DB-29`). O
que a rodada corrigiu foi o **alvo**: o achado nomeava `BKL-T3` e `BKL-T4`, que não têm `git status`
na `Verificação`; a busca por `git status --short` neste plano, conferida ocorrência a ocorrência,
mostra que os cards vivos com a forma de árvore inteira são a `BKL-T6` e a `BKL-T9`, e foram esses
dois que receberam o recorte por pathspec. A correção de registro está apensada ao próprio `AE-5`.

**Colateral de autoria, nos cards que esta rodada já abriu:** `Arquivos-alvo` de `BKL-T3`, `BKL-T4`
e `BKL-T6` passou de prosa com dois caminhos numa linha para um caminho por bullet, a forma canônica
da `DB-26`; e o `Pronto quando` da `BKL-T4` deixou de exigir "`check` verde", que depende da
migração dos documentos vivos entregue só pela `BKL-T6` e portanto não é observável nos
arquivos-alvo daquele card (`DB-29`).

**Análise crítica — por que o vão chegou até aqui:**

1. **Forma de saída autorada a partir do caso que o próprio plano vive.** O `P-0739` só tem tarefas
   de plano; nenhuma das suas 14 tarefas tem pai-tíquete. A §2.6 foi escrita olhando para esse
   corpus e ganhou um worked example só — o que a fase 4, item 7, proíbe para gramática de parser
   ("linha sem exemplo real, forma real sem destino") e que ninguém aplicou à direção inversa: a
   **saída** também é uma forma normativa, e o conjunto de casos dela é dado pelas **regras de
   seleção do mesmo plano**, não pelo corpus à mão.
2. **Regra de ordenação com sujeito que o instrumento nunca devolve.** "Tíquetes `Tipo: bug`" era
   uma faixa de ordenação cujo sujeito, por outra decisão do mesmo plano (`DB-17`), não pode ser o
   resultado. Duas decisões corretas, incoerentes entre si, e o plano passou por quatro rodadas de
   replanejamento sem que ninguém confrontasse uma com a outra.
3. **TF obrigatório sem a forma que ele afirma.** O card exigia o teste "bug antes de FIFO" — e o
   teste precisa de duas coisas que o plano não tinha: o item que `next` devolve nesse ramo e a
   saída exata a comparar. Um TF nomeado no card é uma promessa de que o plano contém o valor
   esperado; quando não contém, o executor frio para (e, aqui, parou certo).
4. **Achado citado por número de linha envelhecido e por fato não re-derivado.** O `AE-5` nomeou os
   cards errados e o card da `BKL-T3` citava `:1833-1865` para um achado que já estava em
   `:1836-1869`. Ponteiro por linha dentro do arquivo que a própria rodada reescreve vence dentro da
   sprint; fato afirmado pela execução é indício, não fato.
5. **Custo.** Um contexto de executor gasto até a triagem, sem uma linha de código, mais esta
   rodada. Nenhuma linha de `.claude/tools/backlog.py` nem de `tests/test_backlog.py` foi tocada —
   a parada foi limpa e barata, que é o comportamento certo do executor sob `G-REPLAN`.

**Lições para o planejador** (uma classe de erro nova, duas já cobertas e reforçadas):

- **Classe nova — forma normativa de saída com menos casos do que as regras do mesmo plano
  admitem.** Verificação a acrescentar à fase 4, item 7: *toda forma de saída, projeção ou template
  normativo tem um worked example por caso que as **regras do próprio plano** admitem — o conjunto
  de casos sai das regras de seleção/classificação, nunca do corpus que o plano tem à mão. Caso
  admitido por uma seção e não instanciado na seção que o imprime é defeito, e TF nomeado num card
  exige que o plano contenha a saída exata que esse TF afirma.*
- **Classe já coberta, reforçada — coerência entre decisões do mesmo plano.** Regra normativa cujo
  sujeito é um item que outra decisão do mesmo plano torna inatingível é defeito de autoria, não
  resíduo: na fase 4, item 4 (rastreabilidade), confrontar cada regra de ordenação ou de seleção com
  o vocabulário de itens que o instrumento **pode devolver**.
- **Classe já coberta, reforçada — fato afirmado por achado de execução é indício.** Na fase 1 da
  rodada de replanejamento, re-derivar por busca o fato factual do achado (quais arquivos, quais
  cards, quais linhas) antes de emendar: o `AE-5` nomeou dois cards errados e teria produzido duas
  emendas inúteis e duas pendentes.

Como na `RP-1`, na `RP-2`, na `RP-3` e na `RP-4`, a publicação desses parágrafos em
`.claude/agents/pantonic-planner.md` é **ato do dono**, com a linha correspondente em `CHANGELOG.md`
sob `## [Não lançado]`. O `P-0739` não depende dela: a `BKL-T3` está fechada e despachável desde já. **Publicada em 2026-09-17, por ordem do dono** ("publicar o pantonic-planner; nós iniciamos esse plano exatamente para modificar"): as lições desta rodada estão em `.claude/agents/pantonic-planner.md`, com a linha correspondente em `CHANGELOG.md` sob `## [Não lançado]`.

**Saída:** `DB-33`, `DB-34`, `DB-35`, `DB-36`; §2.6 reescrita com esqueleto, tabela campo a campo e
dois worked examples; §2.3 com bullet por tipo de pai e a regra do bloco; §2.5 regra 4 reescrita em
três faixas sobre itens elegíveis; §3 com pai plano ou tíquete; `BKL-T3` de `blocked` para `ready`,
com restrições, contingências e cinco testes novos; `BKL-T4` com o TF do bullet por pai; `BKL-T6` e
`BKL-T9` com `Verificação` por pathspec (`AE-5`); §6 com duas linhas de risco; cabeçalho com a
`RP-5` e a ordem de execução atualizada (`BKL-T2e` `done`). Nenhuma tarefa nova, contagem segue em
14; nenhuma entrega fechada foi reaberta (`DB-23`) e nenhum arquivo fora deste plano foi editado.

### AE-7 — A lista de condições de exit 3 de `next` tem duas residências divergentes, e o rodapé de §2.6 não tem teste com poder discriminante

**2026-09-17, achados da rodada de revisão da `BKL-T3` (`pantonic-reviewer`), devolvidos sem
decisão (Regra 8).** Entrega fechada como `done` com **ressalva** (94%, bloqueante nenhuma, única
dimensão fora de `conforme`: `rota` `parcial`; RDO
`docs/RDO/P-0739-BKL-T3-next-a-selecao-deterministica.md`). **Sem retroação sobre a entrega**
(`DB-23`): o veredito do laudo é o que vale, e os três achados abaixo são alvo `dossiê` — dois do
card, um com consequência medida no código entregue. **Nada escalado ao dono:** nenhum é decisão de
arquitetura nem de requisito.

**Achado 1 — quarta condição de exit 3 inverificável como escrita.** As `Restrições` da `BKL-T3`
enumeram quatro condições de exit 3 para `next`; `linha de índice fora da gramática` não tem TF
prescrito na seção `Testes`, não tem literal de mensagem (a `DB-33` só fixa
`linha de índice ausente para <ID>`) e não tem fronteira que a separe de `C-3`/`C-4` do `check()`.
A entrega implementou as outras três e deixou essa sem checador dedicado. Apurado na revisão como
atenuante, e não como desvio: `_parse_indice` descarta linha que não casa `INDICE_LINHA_RE`, e
`selecionar_next` resolve a posição de índice de todo pai de candidato elegível antes de ordenar —
pai vivo com linha malformada cai em `linha de índice ausente para <ID>` e sai exit 3 do mesmo
jeito. O invariante da `DB-6` (o código nunca desempata por heurística) segue de pé; o que falha é
a **nomeação do conserto**. **Rota:** item de replanejamento **antes de despachar a `BKL-T4`**, que
herda a mesma prosa de `Restrições`.

**Achado 2 — a cópia inline de `Restrições` diverge da decisão que cita.** A `DB-6` (`:66`) lista
`plano vivo sem prefixo` como quarta condição de exit 3 de `next`; o card a trocou por
`pai vivo sem linha no índice` (`DB-33`) sem revogar nem citar a troca, e o `check()` já cobre o
prefixo por `C-7`. Duas residências divergentes para a mesma lista é o defeito que a `DB-2` proíbe.
**Rota:** fixar a lista única de condições de exit 3 de `next` numa residência só, e a cópia inline
passar a derivar dela.

**Achado 3 — verificação sem poder discriminante no rodapé de §2.6, com desvio medido.** Nenhum TF
do card afirma o valor de `inbox de planos: <n> por drenar`, e o TF do rodapé fala em "linhas não
marcadas" do inbox de memória sem definir "marcada". **Consequência medida nesta entrega:**
`_contar_pendentes_inbox` aplica ao inbox de **planos** a gramática de marcação do inbox de
**memória** (`GOVERNANCA_MEMORIAS.md` §8: linha `- ` sem `[promovido]`/`[descartado`), quando a
§2.4 deste mesmo plano (`:156-158`) define a linha viva de outro jeito — "começa com `- ` e contém
`docs/plans/P-NNNN-<slug>.md`"; drenada = prefixo `- [drenado AAAA-MM-DD] `. A regra estava no
dossiê e não foi seguida, e **nenhum teste acusou**: as duas fixtures têm inbox sem linha viva,
onde as duas regras dão 0. Foi este achado, e não o 1, que moveu `rota` para `parcial`. **Rota:**
TF que afirme o contador de planos sobre fixture com linha viva e linha drenada, mais a correção
de `_contar_pendentes_inbox` para a gramática de §2.4.

**Consequência de fila:** os três achados têm rota de replanejamento e o achado 1 incide sobre a
prosa que a `BKL-T4` herda, logo a rodada `RP-6` (`pantonic-planner`) é a próxima tarefa, antes da
`BKL-T4` — evento intrínseco do plano, não decisão do dono.

**Correção de registro (`RP-6`, 2026-09-18):** o achado 1 diz que a prosa defeituosa é "a prosa de
`Restrições` que a `BKL-T4` herda". Re-derivado campo a campo nesta rodada: a `BKL-T4`, como estava
publicada, **não tinha campo `Restrições desta tarefa`** — nem `Não fazer`, nem `Contingências`. Não
havia herança a corrigir: havia ausência, que é o defeito maior (um card de `classe implementacao`
sobre o verbo que escreve todas as projeções, sem uma restrição inline e sem contingência fechada).
A rodada autorou os três campos do zero. Nada aqui retroage sobre entrega nenhuma: o que se corrige
é o registro do achado.

**Absorvido pela `RP-6` (2026-09-18):** achados 1 e 2 fechados por `DB-37` (lista única das três
condições de exit 3 de `next`, com substring obrigatória por condição, fronteira contra `check` e
`drain`, e a enumeração retirada da `DB-6`), residência em §2.5 item 6; achado 3 fechado por `DB-38`
(uma gramática de linha viva por arquivo de inbox, com TF que afirma o valor impresso), com §2.4 e o
rodapé de §2.6 reescritos; a correção de código dos achados 1 e 3 reside na tarefa nova `BKL-T3a`
(`DB-39`), despachada antes da `BKL-T4`. Nenhuma entrega fechada foi reaberta (`DB-23`). Ver
`### RP-6` abaixo.

### RP-6 — Rodada de replanejamento sobre `AE-7` (2026-09-18, classe replanejamento)

**Classificação:** técnica nos três achados — a matéria é a lista de condições de erro de um verbo
interno, a residência de uma lista normativa do próprio plano e a gramática com que um contador lê um
arquivo do próprio repositório, tudo dentro do escopo já aprovado. Decidida pelo planejador
(`DB-37`, `DB-38`, `DB-39`), sem rodada de decisões ao dono, no precedente da `RP-2`..`RP-5`. Teste
de legitimidade do escalonamento, item a item: (a) **duas respostas levam a planos materialmente
diferentes?** Não — nenhuma alternativa muda objetivo, rota ou entregável do plano; muda quais
condições um verbo somente-leitura nomeia e por qual regra um contador conta; (b) **existe default
derivável?** Sim, e ele decide: `DB-2` (fonte única), `DB-19` (forma fora da gramática é violação
nomeada pelo `check`, nunca decisão) e a §2.4 já escrita fixam tanto a residência única quanto a
gramática do contador; (c) **o dono já respondeu?** A pergunta nunca lhe foi posta e não precisa
ser. Nada aqui é estratégico nem altera escopo.

**Fatos que mandam nesta rodada** (re-derivados no arquivo, não herdados do texto do achado):
`DB-6` enumerava quatro condições de exit 3 e a quarta era `plano vivo sem prefixo`; as `Restrições`
da `BKL-T3` enumeravam quatro e a quarta era `pai vivo sem linha no índice`; o único literal de
mensagem fixado no plano inteiro era `linha de índice ausente para <ID>` (`DB-33`); o `check` já tem
`C-7 plano-vivo-sem-prefixo`, `C-4 celula-do-indice-com-prosa` e `C-9 id-do-indice-sem-residencia` no
vocabulário fechado da `BKL-T2`; a `BKL-T5` já manda `drain` sair exit 3 em plano sem `Prefixo`; a
§2.4 define linha viva do inbox de planos por caminho de plano e marca de drenado; e a `BKL-T4`, como
publicada, não tinha `Restrições`, `Não fazer` nem `Contingências` (ver a correção de registro no
`AE-7`).

**Achado 1 — rota escolhida: três condições, não quatro, com substring obrigatória por condição.**
A pergunta é "o que, exatamente, faz `next` sair exit 3?" e a resposta é a tabela de §2.5 item 6:
E-1, E-2, E-3, cada uma com a substring que a mensagem tem de conter e o `<ID>` que ela nomeia.
`linha de índice fora da gramática` **deixa de ser condição de `next`**: a linha que não casa §2.2 é
descartada na leitura e não existe para o verbo; quando é a linha do pai de um candidato elegível, o
caso cai em E-3 — que é exatamente o que o revisor apurou como atenuante no código entregue. O lint
dela é do `check`, onde ela já mora. Rotas descartadas: (a) implementar em `next` um checador
dedicado para a quarta condição — duplicaria `C-4`/`C-9` dentro de um verbo somente-leitura que já
descarta a linha, criando segunda residência para o mesmo lint (`DB-2`); (b) fixar a mensagem
inteira de cada condição, e não a substring — a `BKL-T3` está `done` (`DB-23`) e a forma completa
das mensagens entregues não é fato apurado, de modo que a norma nasceria contra um código que não se
pode reabrir; substring obrigatória é discriminante para TF e não retroage; (c) registrar e não agir
— deixaria a `BKL-T4` herdar a mesma lista sem literal e sem fronteira, e a `BKL-T4` é o verbo que
escreve.

**Achado 2 — rota escolhida: residência única em §2.5 item 6; a `DB-6` deixa de enumerar.** Entre as
duas listas divergentes não se escolhe uma: tira-se a enumeração da célula de decisão e põe-se numa
seção normativa, que é onde regra de forma mora neste plano (§2.1 a §2.7), com a `DB-6` mantida como
princípio e marcada como emendada. A cópia inline continua obrigatória em card — restrição por
ponteiro é defeito —, mas passa a **derivar** verbatim da tabela, e a tabela diz isso de si mesma. A
cópia das quatro condições no card `done` da `BKL-T3` fica como registro do que foi executado e
deixa de ser residência (`DB-23`, sem retroação). Rotas descartadas: (a) corrigir o card para a
lista da `DB-6` — poria em `next` uma condição que `check` e `drain` já cobrem e que não impede a
seleção; (b) corrigir a `DB-6` para a lista do card e manter as duas enunciações — duas residências
para a mesma lista, que é o defeito medido; (c) registrar a divergência como achado e seguir — a
`BKL-T4` copiaria uma das duas e a próxima revisão mediria o mesmo defeito.

**Achado 3 — rota escolhida: uma gramática por arquivo de inbox, e TF que afirma o valor impresso
sobre corpus onde as regras concorrentes discordam.** O desvio de código só passou porque a fixture
não separava a regra certa da errada: inbox sem linha viva dá 0 pelas duas gramáticas. A norma nova
(`DB-38`) fixa os três campos do rodapé com a gramática de cada um, e a fixture da `BKL-T3a` tem uma
linha viva, uma drenada e uma sem caminho de plano — 1 pela regra de §2.4, 3 pela regra do inbox de
memória. Rotas descartadas: (a) unificar as duas gramáticas numa só — apagaria a marca
`- [drenado AAAA-MM-DD] ` e faria `drain` e `next` discordarem sobre o mesmo arquivo; (b) corrigir o
código sem TF discriminante — repõe o estado em que o desvio nasceu; (c) registrar e não agir — o
campo errado sai em toda injeção do hook (`DB-8`), a cada prompt, e é insumo do `Pronto quando` da
`BKL-T5`, que também era vazio por construção (corrigido nesta rodada).

**Superfícies vizinhas fechadas no mesmo ato (G-SURFACE):** (i) §2.7 e §3 passam a dizer o que
`status`/`start` fazem quando o dado impede a escrita — exit 3 pelas condições E-2 e E-3, sem tocar
arquivo — e que a recusa de `start` por outro `in-progress` é exit 1, recusa de transição, não
ambiguidade; sem isso a `BKL-T4` teria um caso observável sem contingência e o executor frio pararia.
(ii) A `BKL-T4` ganha `Restrições desta tarefa`, `Não fazer` e `Contingências`, que não existiam, mais
o TF `test_tf_status_recusa_pai_sem_linha_de_indice`. (iii) A `BKL-T5` ganha a gramática de §2.4
inline, o TF da linha já drenada e um `Pronto quando` que exige o inbox começar com linha viva — o
anterior (`next` reporta `inbox de planos: 0`) era satisfeito por um inbox vazio, o mesmo vício de
poder discriminante do achado 3. (iv) O `Arquivos-alvo` da `BKL-T5` passou de prosa com dois caminhos
numa linha para um caminho por bullet, a forma canônica da `DB-26`.

**Veredito: uma tarefa nova.** Ao contrário da `RP-5`, aqui há código a mudar numa entrega já
fechada: as mensagens de E-1 e E-2 e o contador do rodapé. Como `DB-23` proíbe retroagir sobre a
`BKL-T3`, a correção nasce em card próprio, `BKL-T3a` (`DB-39`), com dossiê e gate próprios — o mesmo
padrão de `BKL-T2a`..`BKL-T2e`. Contagem do plano: 15 tarefas.

**Análise crítica — por que o vão chegou até aqui:**

1. **Lista normativa copiada para o card sem residência nomeada.** A doutrina do planejador manda
   copiar restrição inline (ponteiro é defeito) — e é isso que cria cópias. O que faltava era a outra
   metade da regra: toda cópia deriva de **uma** residência nomeada, e a residência é seção
   normativa, nunca célula de decisão usada como lista. Sem isso, a cópia e a origem envelhecem em
   direções diferentes, que é o que `DB-6` × `BKL-T3` mediu.
2. **Condição de erro tratada como prosa, e não como forma de saída.** A `RP-5` aprendeu que forma de
   saída precisa de um worked example por caso admitido pelas regras do plano. A lista de exit 3 é
   forma de saída — e foi escrita como enumeração em prosa, sem literal, sem TF e sem fronteira
   contra o instrumento vizinho que cobre o mesmo dado (`check`). Três das quatro condições ficaram
   de pé por acidente do código entregue.
3. **Fixture que não separa a regra certa da errada.** O TF do rodapé existia em espírito (o card
   pedia "rodapé lista os blocked e conta as linhas") mas nenhum afirmava o **valor** de
   `inbox de planos:`, e as duas fixtures davam 0 pelas duas gramáticas concorrentes. Verificação que
   passa igual sob a regra certa e sob a errada não é verificação.
4. **Custo.** A entrega não foi perdida: a `BKL-T3` fechou `done` com ressalva e segue valendo. Esta
   rodada custou um contexto de planejador e acrescentou uma tarefa pequena; nenhuma linha de
   `.claude/tools/backlog.py` nem de `tests/test_backlog.py` foi tocada aqui.

**Lição para o planejador** (uma classe de erro nova, duas já cobertas e reforçadas):

- **Classe nova — cópia inline sem residência única nomeada.** Verificação a acrescentar à fase 4,
  item 4: *toda lista normativa que um card copia inline tem uma residência declarada e única, que é
  uma seção normativa do plano — nunca uma célula da tabela de decisões usada como lista. A seção diz
  de si mesma que é a residência; a decisão remete a ela em vez de reenunciar; e a auto-auditoria
  confronta cada cópia inline com a residência, item a item, antes de publicar. Duas enunciações da
  mesma lista em dois lugares é defeito de autoria, mesmo quando as duas estão corretas no dia em que
  foram escritas.*
- **Classe já coberta, reforçada — condição de erro é forma de saída.** A verificação da fase 4, item
  7, vale para a lista de condições de erro de um instrumento: cada condição enumerada num card tem
  (i) a substring literal que a mensagem imprime, (ii) o TF que a afirma e (iii) a fronteira explícita
  contra o instrumento vizinho que cobre o mesmo dado. Condição sem os três não é verificável, e o
  revisor só descobre isso depois da entrega.
- **Classe já coberta, reforçada — verificação sem poder discriminante (`DB-29`, `RP-3`).** Não basta
  que o critério de pronto cite efeito nos arquivos-alvo: o **corpus** do teste tem de separar a regra
  certa da errada. Na fase 4, item 7, ao prescrever um TF, escrever também o valor que a regra
  concorrente daria sobre a mesma fixture; se for o mesmo, a fixture está errada, não o teste.

A publicação desses parágrafos em `.claude/agents/pantonic-planner.md` é ato da orquestração, com a
linha correspondente em `CHANGELOG.md` sob `## [Não lançado]`. O `P-0739` não depende dela: a
`BKL-T3a` está fechada e despachável desde já.

**Saída:** `DB-37`, `DB-38`, `DB-39`; `DB-6` emendada (deixa de enumerar); §2.4 com a marca de
drenado como discriminante e a gramática do inbox de memória excluída deste arquivo; §2.5 item 2
reescrito e **item 6 novo** (residência única das três condições de exit 3, com fronteira contra
`check` e `drain`); §2.6 com a tabela do rodapé campo a campo; §2.7 e §3 com os exit de `status`/
`start`; tarefa nova `BKL-T3a` (`ready`, primeira da fila); `BKL-T4` com `Restrições desta tarefa`,
`Não fazer`, `Contingências` e um TF novo; `BKL-T5` com gramática inline, TF novo, `Arquivos-alvo`
por bullet e `Pronto quando` discriminante; §6 com três linhas de risco; cabeçalho com a `RP-6`, a
ordem de execução nova e 15 tarefas. Nenhuma entrega fechada foi reaberta (`DB-23`) e nenhum arquivo
fora deste plano foi editado.

### AE-8 — `BKL-T3a` cobre só a metade "item candidato" de E-2, e o contador de fila de memória aceita `---`

**2026-09-18, achados da rodada de revisão da `BKL-T3a` (`pantonic-reviewer`), devolvidos sem
decisão (Regra 8).** Entrega fechada como `done` com **ressalva** (94%, bloqueante nenhuma, única
dimensão fora de `conforme`: `rota` `parcial`; RDO
`docs/RDO/P-0739-BKL-T3a-as-tres-condicoes-de-exit-3-de-next-e-o-contador-do-rodape.md`). **Sem
retroação sobre a entrega** (`DB-23`): o veredito do laudo é o que vale, e os dois achados abaixo são
alvo `dossiê`. **Nada escalado ao dono:** nenhum é decisão de arquitetura nem de requisito.

**Achado 1 — E-2 entregue pela metade, com desvio medido.** A tabela de §2.5 item 6 define E-2 como
"item candidato **ou pai de candidato** sem a linha `- **Status:**`"; a `BKL-T3a` só testou o item
(`sem_status = [c for c in candidatos if c.item.status is None]`), sem testar `c.pai.status is None`.
**Consequência medida na revisão:** removida a linha `- **Status:**` do tíquete-pai `TK-90` numa
cópia da fixture, `next` sai **exit 0** e elege `FFO-T2`, descartando os candidatos do pai em
silêncio — o mesmo desempate por heurística que `DB-6`/`DB-33` proíbem. **Rota:** card novo, sucessor
da `RP-6`, com TF próprio para a metade "pai de candidato" de E-2 (não retroage sobre a `BKL-T3a`,
`DB-23`).

**Achado 2 — gramática do contador de fila de memória aceita linha que não é candidata.** A
Restrição da `BKL-T3a` (copiada de §2.4/§2.5, herdada da gramática de marcação de
`GOVERNANCA_MEMORIAS.md` §8) diz "linhas que começam com `- `"; `_contar_inbox_memoria` testa
`s.startswith("-")`, sem o espaço — uma régua markdown `---` conta como candidato. O contador irmão
`_contar_inbox_planos` usa `- ` corretamente. **Rota:** corrigir `_contar_inbox_memoria` para
`startswith("- ")`, no mesmo card do achado 1 ou em card próprio, com TF que use uma fixture com
linha `---`.

**Consequência de fila:** os dois achados têm rota de replanejamento e nenhum bloqueia a `BKL-T4`
(o verbo `next` já entrega E-2 suficiente para o caso que a `BKL-T4` exercita hoje) — a rodada
`RP-7` (`pantonic-planner`) é a próxima tarefa, e a `BKL-T4` segue despachável em paralelo à decisão
de onde a `RP-7` encaixa o card novo na fila (antes ou depois da `BKL-T4`, decisão do planejador).

**Absorvido pela `RP-7`** (2026-09-18): achado 1 → `DB-40`, achado 2 → `DB-41`, alocação e posição na
fila → `DB-42`; os dois viram a tarefa `BKL-T3b`, **antes** da `BKL-T4`.

### RP-7 — Rodada de replanejamento sobre `AE-8` (2026-09-18, classe replanejamento)

**Classificação:** técnica nos dois achados — a matéria é o sujeito de uma condição de erro de um
verbo interno e o prefixo com que um contador lê um arquivo, tudo dentro do escopo já aprovado.
Decidida pelo planejador (`DB-40`, `DB-41`, `DB-42`), sem rodada de decisões ao dono, no precedente
da `RP-2`..`RP-6`. Teste de legitimidade do escalonamento, item a item: (a) **duas respostas levam a
planos materialmente diferentes?** Não — nenhuma alternativa muda objetivo, rota ou entregável do
plano; muda sobre que conjunto uma condição corre e qual prefixo um contador aceita; (b) **existe
default derivável?** Sim, e ele decide: a própria tabela de §2.5 item 6 já enuncia E-2 com o pai
dentro do sujeito, e §2.6 já escreve o prefixo `- ` do contador de memória — nos dois casos o código
é que desviou da norma escrita; (c) **o dono já respondeu?** A pergunta nunca lhe foi posta e não
precisa ser. Nada aqui é estratégico nem altera escopo. O próprio `AE-8` já classificara os dois como
decisão técnica/tática.

**Fatos que mandam nesta rodada** (re-derivados no código e nas fixtures, não herdados do texto do
achado, passo 1 do protocolo): em `.claude/tools/backlog.py`, `selecionar_next` monta
`sem_status = [c for c in candidatos if c.item.status is None]` e só depois filtra elegíveis por
`c.pai.status in ("ready", "in-progress")` — logo o pai sem `Status` **não** produz exit 3, e os
filhos dele são descartados em silêncio; quando **só** o tíquete perde a linha, a seleção sai exit 0
e elege `FFO-T2` (o desvio que a revisão mediu), e quando os dois pais da fixture a perdem, sai exit
2 `nada delegável — 0 elegível(is)`, igualmente sem nomear conserto. `_contar_inbox_memoria` testa
`s.startswith("-")` enquanto o irmão `_contar_inbox_planos` testa `s.startswith("- ")`, e a única
exclusão do contador de memória é a marca `[promovido]`/`[descartado`. A fixture
`tests/fixtures/backlog/next_tk90/` tem o `Status` do tíquete-pai numa linha própria
(`docs/DIARIO_DE_OBRAS.md`, logo abaixo de `## TK-90 — …`) e o do plano-pai numa linha de cabeçalho
compartilhada com o `Prefixo` (`docs/plans/P-0090-fifo.md`) — fato que decide **como** o TF edita a
cópia. No `check`, `_item_checks` já emite `C-2` para tarefa, tíquete e subtarefa sem `Status` e
`C-8` para plano vivo sem `Status`: a fronteira contra o lint existe e não precisa de código novo.
Piso de teste vigente: suíte `130`, `tests/test_backlog.py` `24` (fechamento da `BKL-T3a`).

**Achado 1 — rota escolhida: E-2 corre sobre a união item ∪ pai, com ID distinto uma vez e em ordem
alfabética.** A norma não muda de sujeito — §2.5 item 6 sempre disse "item candidato, **ou pai de
candidato**" —, o que faltava era (i) o código cobrir a segunda metade e (ii) a norma fechar os dois
casos observáveis que a segunda metade cria e que a primeira não tinha: **pai compartilhado por dois
candidatos** (repetiria a mesma mensagem) e **item e pai os dois sem a linha** (duas mensagens, em
que ordem?). `DB-40` fecha os dois com a mesma regra que a `DB-37` já usa em E-1 — ID distinto, ordem
alfabética crescente, separador `, ` — e ratifica a ordem de avaliação entregue (E-2 antes de E-1 e
E-3), que era escolha implícita do código e agora é norma. A fronteira contra o `check` (`C-2`/`C-8`)
entra na mesma tabela, porque condição de erro sem fronteira contra o instrumento vizinho é o defeito
que a `RP-6` nomeou. Rotas descartadas: as quatro da `DB-40` — manter E-2 só sobre o item, tratar pai
sem `Status` como `ready`, repetir o ID do pai por filho, registrar e não agir.

**Achado 2 — rota escolhida: corrigir o código para o prefixo que a norma já escreve, com TF sobre
corpus em que as duas leituras discordam.** Aqui não há norma nova a fazer: §2.6 e
`GOVERNANCA_MEMORIAS.md` §8 já dizem `- `. O que a rodada acrescenta é (i) a célula de §2.6
explicitando que o espaço faz parte do prefixo — a régua `---` não é candidato — e que **nenhuma
outra exclusão** entra no contador, e (ii) a exigência, herdada da `DB-38`, de um TF que afirme o
valor impresso sobre corpus discriminante: o inbox literal do card dá **2** pela regra certa e **3**
pela errada. A tentação de aproveitar a passagem para filtrar sub-bullet indentado foi descartada:
não há forma real apurada no corpus, e gramática autorada de memória é exatamente o defeito da
`RP-1`. Rotas descartadas: as quatro da `DB-41`.

**Veredito: uma tarefa nova, antes da `BKL-T4`.** Os dois defeitos moram no mesmo verbo, no mesmo
módulo, no mesmo arquivo de teste e na mesma família de fixture — um card só (`DB-42`), pelo mesmo
raciocínio da `DB-39`. A posição na fila, que o `AE-8` deixou em aberto, é **antes** da `BKL-T4`: a
`BKL-T4` aplica E-2 ao item alvo **e ao pai dele** antes de escrever (`DB-37`, segunda cláusula) e
reusa a função que a `BKL-T3b` normaliza; despachada primeiro, ela implementaria a metade "pai" por
conta própria e criaria segunda residência para a mesma regra — o defeito que a `RP-6` acabou de
fechar. Contagem do plano: 16 tarefas.

**Superfícies vizinhas fechadas no mesmo ato (G-SURFACE):** (i) §2.5 item 6 ganha a forma completa da
mensagem de E-2 (ID distinto, ordem alfabética, separador), a ordem de avaliação e a fronteira
`C-2`/`C-8`; (ii) a célula do contador de memória em §2.6 passa a dizer que o espaço faz parte do
prefixo e que não há outra exclusão; (iii) a `BKL-T4` ganha `BKL-T3b` no `Depende de`, a forma da
mensagem de E-2 nas suas `Restrições` — com a instrução explícita de **reusar** a função em vez de
reescrever a regra — e o `Não fazer` atualizado; (iv) §6 ganha duas linhas de risco ocorrido.

**Análise crítica — por que o vão chegou até aqui:**

1. **TF que exercita metade do sujeito de uma regra.** A `RP-6` escreveu a norma de E-2 com o sujeito
   composto ("item candidato **ou** pai de candidato") e prescreveu **um** TF para ela. Um sujeito
   composto admite dois casos observáveis; um TF cobre um. A verificação que faltava não é sobre a
   norma nem sobre o card: é sobre a **correspondência entre o número de casos que o sujeito admite e
   o número de TF prescritos**.
2. **Gramática de string copiada certa, implementada errada por um caractere.** A cópia inline da
   `BKL-T3a` dizia `- ` e o código escreveu `-`. Nenhuma revisão de texto pega isso; só pega o TF
   cujo corpus contém a forma que os dois prefixos classificam diferente — que é a mesma lição da
   `DB-38`, aplicada ao **contador irmão** que ninguém tinha mandado testar. O card corrigiu o
   contador acusado e deixou o vizinho como estava.
3. **Custo.** A entrega não foi perdida: a `BKL-T3a` fechou `done` com ressalva e segue valendo. Esta
   rodada custou um contexto de planejador e acrescentou uma tarefa pequena; nenhuma linha de
   `.claude/tools/backlog.py` nem de `tests/test_backlog.py` foi tocada aqui.

**Lição para o planejador** (uma classe de erro nova; o achado 2 é instância de classe já coberta):

- **Classe nova — regra com sujeito composto tem um TF por termo do sujeito.** Verificação a
  acrescentar à fase 4, item 7: *quando a regra enuncia um sujeito composto ("A ou B", "item ou
  pai", "plano ou tíquete"), cada termo é um caso observável e exige TF próprio; um TF que exercita
  só o primeiro termo deixa o segundo sem poder discriminante e a entrega fecha verde pela metade.
  No mesmo passo, todo caso que o sujeito composto cria e o sujeito simples não tinha — repetição do
  mesmo referente, dois termos falhando juntos — é fechado na norma antes de virar card.*
- **Classe já coberta — verificação sem poder discriminante (`DB-38`, `RP-6`).** O achado 2 é
  instância: quando um card corrige um instrumento que tem **irmão** com a mesma matéria (dois
  contadores, dois parsers, duas projeções), a auto-auditoria confronta o irmão com a mesma
  gramática — a correção de um deles é o momento em que o outro é auditável de graça. Reforço do item
  7, sem item novo.

A publicação desses parágrafos em `.claude/agents/pantonic-planner.md` é ato da orquestração
(precedente do dono, 2026-09-17: publicar é consequência do plano, não pergunta), com a linha
correspondente em `CHANGELOG.md` sob `## [Não lançado]`. O `P-0739` não depende dela: a `BKL-T3b`
está fechada e despachável desde já.

**Saída:** `DB-40`, `DB-41`, `DB-42`; §2.5 item 6 com a forma completa da mensagem de E-2, a ordem de
avaliação e a fronteira contra `C-2`/`C-8`; §2.6 com o prefixo `- ` do contador de memória
explicitado; tarefa nova `BKL-T3b` (`ready`, primeira da fila, antes da `BKL-T4`); `BKL-T4` com
`Depende de`, `Restrições` e `Não fazer` emendados; §6 com duas linhas de risco; cabeçalho com a
`RP-7`, a ordem de execução nova e 16 tarefas. Nenhuma entrega fechada foi reaberta (`DB-23`).

### AE-9 — A atribuição cruzada de `review_evidence.py` casa só por caminho exato, e alvo-diretório de outra tarefa nunca casa

**Origem:** laudo da `BKL-T3b` (2026-09-18, `pantonic-reviewer`), achado de processo alvo `dossiê` —
único achado da rodada; a tarefa fechou **aprovada 100%**, sem dimensão rebaixada, sem `--escalar` e
com recomendação `seguir`. Registro sem retroação sobre a entrega (`DB-23`).

**Fato medido:** `.claude/tools/review_evidence.py:295-320` atribui arquivo tocado a outra tarefa do
mesmo plano **só por caminho exato**. O casamento por prefixo (`prefixos_dir`) vale apenas para os
alvos-diretório do card **em revisão**, não para os das demais tarefas. Consequência apurada nesta
rodada: os 5 arquivos de `tests/fixtures/backlog/next_tk90*/`, cobertos pelo alvo-diretório
`tests/fixtures/backlog/` que a `BKL-T3` declara (plano, linha 1379), caíram no balde *fora dos
alvos e sem atribuição*; o veredito mecânico de `escopo` saiu **aberto** e a prova de que a
`BKL-T3b` não os tocou teve de ser produzida pelo reviewer por datação de `mtime` — trabalho que o
dossiê existe para dispensar (`DB-25`).

**Rota (do laudo):** estender o casamento por prefixo aos alvos-diretório das demais tarefas do
plano, em card próprio de `review_evidence.py`. Não bloqueia a `BKL-T4`.

**Fato adjacente, da seção "Lições aprendidas" do mesmo laudo** — não é defeito de instrumento e não
tem rota técnica: a revisão correu contra árvore de trabalho com **7 tarefas do mesmo plano ainda
não commitadas**, e o recorte `--desde 6d7433c` trouxe **33 arquivos tocados para uma entrega de 2**.
Enquanto o plano acumular entregas sem commit, o custo de revisão por tarefa cresce com o número de
tarefas anteriores em aberto. Commitar é **ato do dono**, não decisão do planejamento — apresentado
no relatório de encerramento da janela.

**Checkpoint de orquestração (2026-09-18, janela nova):** Descoberto/decidido: dono decidiu sobre `AE-9` — seguir para `BKL-T4` sem abrir `RP-8`; commit das 7 entregas `BKL-T2a`..`BKL-T3b` já estava feito em `428246c` (17:57:52) antes desta janela abrir — o texto de `Fila corrente` que dizia "não commitadas" estava desatualizado, não a árvore (`git status` limpo). · Falta: despachar `BKL-T4` (não iniciada nesta janela). · Tocados: `docs/DIARIO_DE_OBRAS.md` (duas correções na `Fila corrente`: resolução do `AE-9`/commit, base de recorte `--desde 428246c`). · Próximo passo: delegar `BKL-T4` ao `pantonic-executor`, dossiê em `docs/plans/P-0739-backlog-instrumento.md:1710-1791` (re-derivar âncora no despacho, item 3 do gate). · Não refazer: drenagem dos dois inboxes (vazios/já marcados), decisão do dono sobre `AE-9`, verificação do commit `428246c`.

- **`AE-10` (2026-09-18, `BKL-T4`, regra `B1` do `scrum-master`) — `transacionar_status` depende de
  marcadores que a `BKL-T6` ainda não inseriu no diário vivo.** Achado do laudo (dimensão `dossiê`,
  ressalva não bloqueante, veredito 85% `ressalva`, bloqueante `nenhuma`): a função chama
  `diario_linhas.index('<!-- fila:gerada -->')` **sem guarda**, e o `docs/DIARIO_DE_OBRAS.md` real
  ainda não tem os marcadores — a inserção deles é o item (a) da `BKL-T6`. Enquanto a migração não
  rodar, `status` e `start` estouram `ValueError` contra o diário vivo em vez de sair `exit 1`/
  `exit 3` como a tabela de §2.7 prescreve. Não afeta a suíte (os TF rodam sobre cópia de fixture
  no `tmp_path`, onde os marcadores existem), por isso a entrega fechou verde e com ressalva.
  **Rota:** rodada de replanejamento fixando ou a dependência de ordem (`BKL-T6` item (a) antes de
  qualquer uso de `status`/`start` contra o diário real) ou a guarda com exit code próprio. Achado
  de ordenação entre tarefas do mesmo plano, portanto matéria de planejamento — não se resolve na
  execução (`G-REPLAN`).
- **`AE-11` (2026-09-18, achado do próprio run de aferição do `scrum-master`, sem ação nesta
  janela).** A `BKL-T4` foi executada como caso-teste para medir o loop de ponta a ponta. Cinco
  defeitos do instrumento apareceram e estão no relatório de janela; o que toca este plano é um só:
  a regra `B1` **para a janela sempre que houver `pendencia=`**, sem distinguir pendência
  substantiva de observação transitória já resolvida. Nesta rodada o `pendencia=` do executor
  relatava uma falha de teste que era WIP da própria orquestração, corrigida antes da revisão — e
  ainda assim `B1` encerra a janela. Rota: matéria do plano do `scrum-master`, não deste.

- **`AE-12` (2026-09-18) — este plano fica PARADO até a baseline do `scrum-master` fechar
  (`DM-9` do `P-0740-loop-de-modulos`).** Nenhuma das 6 tarefas `ready` restantes é delegável neste
  intervalo, e o `AE-10` **não** abre rodada de replanejamento própria: ele foi absorvido pela
  `LM-T5` do `P-0740`, que reescreve os 6 cards como módulos coesos sob a gramática nova
  (`DM-2`..`DM-5`) e resolve a dependência de ordem dentro do reagrupamento. Este plano volta à
  fila como **fila de módulos**, e fecha em **rodada única** na `LM-T6`. Razão: os 6 cards foram
  autorados sob a régua atômica; executá-los um a um reproduziria os seis defeitos que o run de
  aferição de 2026-09-18 mediu (`P-0740` §3).

