# P-0739 — O pickup vira instrumento: `backlog.py` decide a próxima tarefa, fecha a tarefa e mantém o kanban

**Data:** 2026-09-15 · **Origem:** diretiva do dono, 2026-09-15 ("mecanizar o próximo passo") ·
**Status:** `done` (2026-09-18, retomado pela `RP-7`: `AE-8` absorvido, §2.5 item 6 emendado
com a forma completa de E-2 e a tarefa `BKL-T3b` autorada) ·
**Prefixo das tarefas no diário:** `BKL-T<n>` · **Prefixo das decisões:**
`DB-<n>` · **Checagem de versão do kit:** modo hub — congelada em `0.0.0` (`DE-7`), nada a comparar.
**Ordem de execução:** BKL-T11a → BKL-T12 (`BKL-T9a` `done` em 2026-09-19; `BKL-T2b`, `BKL-T2c` `done` em
2026-09-16; `BKL-T2d`, `BKL-T2e` `done` em 2026-09-17; `BKL-T3` `done` com ressalva em 2026-09-17;
`BKL-T3a` `done` com ressalva em 2026-09-18; `BKL-T3b` e `BKL-T4` `done` em 2026-09-18; `BKL-T5`,
`BKL-T6`, `BKL-T7`, `BKL-T8` e `BKL-T9` `cancelled` em 2026-09-19, absorvidas pelos módulos — a
`BKL-T5` pelo `BKL-T10a`, pela `DB-44`)
· **Rodadas de replanejamento:** `RP-1`
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
| **`DB-43`** | O corpus do instrumento é derivado do **índice do diário**, e plano terminal sai do corpus (`ESC-1` da retomada, sobre o `AE-15`) | Fato medido em 2026-09-19 sobre `eb93490`: `check` sai **exit 1 com 309 achados** e `next` **exit 3** exigindo linha `Status` de ~110 IDs, porque `carregar` varre **todo** `docs/plans/P-*.md` e decide *vivo* pelo campo `**Status:**` do próprio arquivo — campo que a `DB-15` **proíbe** acrescentar a plano fechado. Os 14 planos legados (`P-0721`..`P-0734`) não o têm, são lidos como vivos e respondem sozinhos por **238** dos 309 achados. A regra: **a célula de estado da linha do índice é a autoridade sobre a vida de um plano** (`DB-15` — *o índice é a projeção final deles*), casada pela regra de sufixo já residente em `_posicao_indice` (`.claude/tools/backlog.py:634`); núcleo em `done`/`superseded`/`cancelled` → o plano **sai do corpus**: `check` não o linta e suas tarefas não entram no conjunto de candidatos, logo não são avaliadas por **E-2** — e ele segue legível por `show` e pela resolução de `Depende de`. Superfície fechada no mesmo ato (G-SURFACE): §2.0 (corpus), §2.2 (âncora do índice), §2.5 item 3 e item 6 (fronteira de **E-2**) e §3. Três emendas junto: (i) o índice é a tabela sob `## Índice` e **só** ela — 17 linhas de tabela ilustrativa da seção `## TK-54` eram lidas como índice e produziam **34** dos 60 achados do diário; (ii) `C-5` e `C-9` passam a casar plano pela regra de sufixo (`P-0739` × `P-0739-BKL`) e `cancelled` entra no conjunto terminal de `C-9`; (iii) a **`DB-15` fica emendada** — o corpo de plano fechado segue imutável, mas o campo `**Status:**` do cabeçalho dele é reconciliado com o índice quando diverge, e `C-5` passa a acusar a divergência: medidas **3** hoje (`P-0735` `ready`×`done`, `P-0737` `ready`×`superseded`, `P-0738` `ready`×`done`). Efeito medido por simulação no ato: `check` cai de **309** para **27** achados — **24** em `docs/DIARIO_DE_OBRAS.md` (11 `C-2`, 8 `C-4`, 3 `C-3`, 2 `C-1`) e **3** `C-5` de cabeçalho —, e o alvo `docs/plans/P-0737-loop-autonomo.md` da `BKL-T6` **cai**: o plano está `superseded` desde 2026-09-18 (`DM-1` do `P-0740`) e os `AUT-T1..T10` deixam de ser matéria de migração. A rota (b) do `AE-15` é a adotada, **generalizada** — o defeito não é a âncora nem a exigência de `Status` isoladas, é o **corpus**. Rotas descartadas: (a) ampliar a migração aos 14 planos fechados (rota (a) do `AE-15`) — escreveria metadado em plano terminal contra a `DB-15` e poria 238 achados históricos no caminho crítico da retomada; (b) re-escopar o aceite aos dois alvos declarados deixando `check` vermelho por desenho (rota (c) do `AE-15`) — o verbo perderia poder discriminante no marco que o publica, e nenhum gate voltaria a usá-lo; (c) registrar e seguir — `next` fica em exit 3 permanente e o hook da `BKL-T7` injetaria o erro a cada prompt. |
| **`DB-44`** | O `BKL-T10` se parte em dois **pelo tema**, e o corte fica entre o corpus e o `drain` (`ESC-2`, sobre o `AE-17`) | Fato medido pela transcrição e confirmado pela revisão: o `BKL-T10` saiu com **20 passos, 6 `Arquivos-alvo` e 12 testes**, e o `Objetivo` dele confessava *três atos*. O que obriga a partir **não** é o teto ≤40: `GOVERNANCA.md` §3 diz que cruzar o número da classe é *alarme para quem dimensiona, nunca bloqueio*, que a divisão é **por tema, nunca por volume**, e que **nenhum dossiê de tarefa carrega teto** — a opção *seguir inteiro com o teto declarado no cabeçalho* é, por isso, inexequível como escrita. O que obriga é o critério **(i)** da unidade de trabalho: *a revisão exercita o módulo ponta a ponta*, e o card carregava **duas** proposições ponta a ponta que não se tocam — (`check` exit 0 · `next` sem exit 3) e (`drain` drena). **Onde o corte cai, e por que não onde o `AE-17` o supôs:** o `AE-17` nomeou os dois temas como *reparo de corpus no instrumento* × *migração dos documentos vivos*; esses dois são **um** tema, porque nenhum dos dois é verificável sozinho contra a árvore real — `check` só fica verde com os dois, e partir ali obrigaria o primeiro card a publicar *309 → 27 achados* como aceite, que é a constante de corpus proibida pelos critérios (xiii) e (xviii) da `RUBRICA_DE_REVISAO.md` §8. O `drain`, esse sim, é outro assunto, e por medida e não por impressão: vem de outro card (`BKL-T5`), de outra seção da norma (§2.4), opera sobre dois arquivos que **não** estão nos `Arquivos-alvo` do `BKL-T10` (`docs/plans/_INBOX.md` e `_INBOX_HISTORICO.md`), tem aceite próprio e independente, e **nenhum** passo do corpus ou da migração depende dele — medido no ato: o inbox real tem **0** linhas vivas, logo `drain` é inerte contra a árvore e não pode deslocar o `check` verde. O único vínculo entre os dois é o arquivo `.claude/tools/backlog.py`, e compartilhar **região** não faz dois assuntos virarem um (§3, item (iii), na direção inversa). **Produto:** `BKL-T10` fica com os blocos de corpus, migração do diário e reconciliação de cabeçalho (16 passos, 6 testes, mesmos 6 `Arquivos-alvo`); nasce o `BKL-T10a` com o verbo `drain` (5 passos, 6 testes, 2 `Arquivos-alvo`); ordem `BKL-T10` → `BKL-T10a` → `BKL-T11` → `BKL-T12`, com o `drain` **depois** do corpus porque a célula de índice que ele escreve tem de nascer na gramática já migrada. **Emenda o `AE-13` num ponto e só nele:** a `BKL-T5` passa a ser absorvida pelo `BKL-T10a`, não pelo `BKL-T10`; a partição em módulos, a ordem relativa e o mapa de herança seguem intactos, e nada do `ESC-1` é revogado. Rotas descartadas: (a) seguir inteiro — deixaria o reviewer sem ponta a ponta para exercitar e exigiria escrever teto em dossiê, contra `GOVERNANCA.md` §3; (b) partir entre instrumento e documentos, como o `AE-17` supunha — poria constante de corpus no aceite do primeiro card e partiria um tema, que é o *fragmento* que a doutrina do módulo proíbe; (c) partir em três (corpus · migração · `drain`) — a migração sem o corpus não tem aceite próprio, e o defeito da rota (b) reapareceria no primeiro dos três. |
| **`DB-45`** | Subtarefa tem projeção de estado, e ela mora **só** na linha `- **Status:**` dela; a projeção corre sempre **filho → pai** (`ESC-3`, sobre o `AE-19`) | **A norma.** A §2.1 já dá à subtarefa de tíquete *os mesmos campos da tarefa* (`Status`, `Tipo`, `Notas de execução`), e a §2.2/§2.5 já lhe negam linha de índice. Fica **explícito**: o estado de uma subtarefa mora na linha `- **Status:**` seguida do estado entre crases e de ` · AAAA-MM-DD`, na seção dela, **residência única**, e nenhuma linha de índice se cria para subtarefa. **A direção decide o resto:** a `DB-36` computa o `<done>/<total>` do pai **a partir** do `Status` dos filhos diretos, e a célula do índice do pai é projeção desse agregado — logo derivar o filho do pai **inverte** a projeção, fecha ciclo e destrói informação (dois filhos em estados diferentes seriam forçados a um valor só). Por isso as rotas *duplicar a célula do pai nas subtarefas* e *subtarefa herda o estado do pai* ficam descartadas, e vale **reconciliar**: o valor do filho é o que o próprio documento já registra para ele. **Por que a decisão traz valor fechado, item a item:** o estado de cada um existe no diário, mas em cinco formas e cinco lugares — cauda do cabeçalho (`TK-53b` *cancelada por absorção*), bullet de fechamento de seção, célula do pai, prosa de `Arquivos-alvo` (`TK-51`, *status → done*) e uma linha `**Status:**` fora de forma (`docs/DIARIO_DE_OBRAS.md:1284`). Mandar o executor *ler o valor registrado* é mandá-lo interpretar prosa, que é o critério (i) da `RUBRICA_DE_REVISAO.md` §8. A tabela da §2.1a fixa os **treze** valores, com a evidência de cada um, e o passo 11 do `BKL-T10` passa a transcrevê-la. **Dois defeitos que nenhum lint vê e que o aceite do `BKL-T10` exige** (medidos no ato): (a) `docs/DIARIO_DE_OBRAS.md:828` traz `### TK-51`, subtarefa com o id do **pai** — fora da gramática `TK-<n><letra>` (`C-1`) — e passa a `### TK-51a`; nenhum documento cita `TK-51a` hoje, então a renomeação não quebra ponteiro; (b) `docs/DIARIO_DE_OBRAS.md:150`, a linha de índice do `TK-54`, carrega prosa **depois** do pipe final, e por isso `INDICE_LINHA_RE` **não a lê** — é a única das 32 linhas da tabela nessa condição. Como a linha não existe para o instrumento, `check` não acusa nada, e o efeito só apareceria **depois** do card: com `TK-54b` `ready`, o `TK-54` vira pai de candidato elegível sem linha de índice e `next` sai **E-3**. Enquanto o `BKL-T10` estiver `in-progress`, a §2.5 item 2 curto-circuita a seleção antes da elegibilidade e o item 2 da `Verificação` passaria **pelo motivo errado**: a prosa vai para a seção `## TK-54`, verbatim, e a linha volta a fechar em `|`. **Reconferência pedida no ato (`ESC-3`, item 2):** a **`DB-36` não muda de fórmula** — muda o que ela imprime, e os valores ficam declarados: `TK-51` **1/1**, `TK-53` **1/1** (o `cancelled` da `TK-53b` sai do denominador), `TK-54` **1/2**. A **`DB-4` não muda em nada**, e por um fato medido, não por argumento: a expressão *candidato a fechamento* **não existe** em `.claude/tools/backlog.py` — o rodapé de `next` imprime `inbox de planos`, `fila de memória` e `blocked`, e nada mais. Norma publicada em §3 sem implementação e sem teste; matéria **pós-marco**, sem card, e evidência para a spec de robustez (`TK-55`). Rotas descartadas: (a) duplicar a célula do pai na subtarefa — escreveria `ready` numa `TK-54a` que o documento declara `done` desde 2026-09-18, e faria a projeção mentir; (b) subtarefa herda o estado do pai — mesmo defeito, com o agravante de tornar o `<done>/<total>` da `DB-36` constante por construção (todo filho igual ao pai ⇒ `0/n` ou `n/n`); (c) dar linha de índice à subtarefa — criaria a segunda residência que a `DB-2` proíbe e quebraria o FIFO da §2.5 item 4 (c), que ordena pela linha do **pai** justamente porque filho não tem linha; (d) deixar o passo 11 mandar *re-derivar o valor* — é a interpretação de prosa que o critério (i) proíbe, e foi o que parou o 1º despacho. |
| **`DB-46`** | Célula de índice de item **terminal** é projeção final e não se reescreve: `C-4` passa a valer só para linha viva; e o bloco de migração é **reautorado inteiro** (`ESC-4`, sobre o `AE-21`) | **O conflito medido:** o passo 10 mandava mover a narrativa de **toda** célula `C-3`/`C-4` para *a seção do item correspondente*; das 8 células, três publicam destino **ilícito neste card** — `P-0733-DHB` e `P-0734-EXA` ancoram em `docs/DIARIO_HISTORICO.md`, que o `Não fazer` proíbe, e `TK-52` ancora no corpo de `docs/plans/P-0738-contexto-esgotado.md`, onde a `Restrição` do bloco C só admite a linha `Status`. **A saída não é lista de exclusão, é regra:** a `DB-15` já diz que *o índice é a projeção final* do item fechado, e a `DB-43` já fixou que o lint governa o **corpus vivo**. Logo a narrativa de fechamento na célula de um item terminal **pertence** àquela célula — é a lápide dele —, e exigir token puro ali é exigir que o fechado mude depois de fechado, com destino que não existe. Regra: **núcleo em `done`/`superseded`/`cancelled` ⇒ célula congelada, sem `C-4`**; núcleo vivo ⇒ célula em token puro e narrativa para a seção do item **no próprio diário**. O critério é um *lookup de token*, aplicável por executor frio sem julgar caso a caso, e **`C-3` continua valendo para toda linha**, terminal ou não, porque o núcleo alimenta a decisão de corpus. Efeito medido no ato: `C-4` cai de **8** para **2** (`TK-38`, `TK-48`), ambas de tíquete vivo com seção no diário; com o núcleo do `TK-55` corrigido para `ready` pela `DB-45`, a célula dele entra e são **3**. As três células conflitantes são terminais e **não se tocam** — nenhuma edição em `DIARIO_HISTORICO.md` nem em corpo de plano fechado. **Segunda parte, e é a que responde ao segundo bloqueio:** a matéria deixou de ser passo. Varredura dos 16 passos contra a árvore, feita neste acionamento — bloco A: os **dez** referentes de `.claude/tools/backlog.py` conferidos um a um, todos exatos; bloco C: as **três** linhas de cabeçalho de plano conferidas, todas exatas; bloco D: sem referente a envelhecer; **bloco B: cinco dos seis passos defeituosos** — 11 e 12 já reautorados no `ESC-3`, 10 é o bloqueio de agora, e **9 estava quebrado sem que ninguém tivesse batido nele** (nomeia **um** parágrafo de fila e existem **três**, sendo o terceiro um bloco de **70 linhas**, e manda para `## TK-54` o parágrafo cujo próprio texto diz *migra para `## P-0739`*), e **8 estava incompleto** (não diz que os marcadores vão sozinhos na linha, que é como `transacionar_status` os acha por igualdade exata, e não diz o que acontece com a `Fila corrente` viva). O defeito é **do bloco**, não dos passos, e a causa é única: enumerações autoradas em 2026-09-15 contra uma árvore que mudou duas vezes (`DB-43`, `DB-45`). **Produto:** o bloco B é reescrito inteiro contra a árvore de 2026-09-19, com cada linha citada pelo literal que a abre, cada destino nomeado e nenhuma enumeração herdada; o bloco A ganha um passo (a regra desta decisão) e os testes passam de 6 para 7; os blocos A, C e D ficam como estavam, porque a varredura não achou defeito neles. Rotas descartadas: (a) inventar seção no diário para hospedar narrativa de item terminal — criaria residência viva para o que está fechado e duplicaria a projeção final da `DB-15`; (b) gravar no histórico e no corpo do plano fechado — quebra o `Não fazer` do card, a `DB-9` e a `DB-15`, e escreve em arquivo que o instrumento nunca lê; (c) excluir as três células por lista nominal — resolve o caso e não a classe, e o próximo plano fechado com prosa na célula reabre o mesmo bloqueio; (d) emendar só o passo 10 e despachar — é o que a varredura desmente: o passo 9 cederia no despacho seguinte. |
| **`DB-47`** | O aceite do `BKL-T10` foi **simulado ponta a ponta** antes do 4º despacho, e o que a simulação mostrou quebrado foi reautorado num ato (`ESC-5`, sobre o `AE-23`) | **O que motivou.** Três bloqueios do mesmo card, em série **decrescente em superfície e crescente em profundidade** — enumeração estagnada (`AE-19`), alcance colidindo com restrição do próprio card (`AE-21`), efeito de **segunda ordem** (`AE-23`) —, a **1.073,7k tk** e **156 tool uses** sem uma linha entregue. Os dois primeiros eram visíveis por leitura; o terceiro **não existe na árvore de hoje**: nasce quando o passo que restaura o parse da linha 150 roda, e faz a narrativa da célula 3 do `TK-54` virar `C-4`. Nenhuma conferência estática o alcança — a varredura do `ESC-4` declarou esse limite antes de o defeito aparecer. **O método muda, e é esta a decisão:** aceite de card de migração **não se confere, se roda**. Antes do 4º despacho, os 18 passos foram aplicados numa **cópia da árvore fora do versionamento** (`%TEMP%/p0739sim`, com `docs/DIARIO_DE_OBRAS.md` e os 20 `docs/plans/P-*.md`), e `check` — com os sete passos do bloco A já embutidos — rodou sobre o resultado. **Achado da simulação: exatamente uma violação**, e é a do `AE-23` — `C-4` na célula 3 do `TK-54`. Nenhuma outra: a série **convergiu no ato em que alguém rodou em vez de ler**. **Reparo:** os passos 11 e 12 trocam de ordem e de alcance. O novo passo 11 trata a linha 150 **inteira, num ato só** — a prosa depois do pipe final **e** a narrativa da célula 3 vão ambas para `## TK-54`, a célula fica em token puro `ready`, a linha volta a fechar em `|` —, e vem **antes** do passo de células justamente porque restaurar o parse é o que cria a violação. O novo passo 12 enumera as **cinco** células restantes e declara que a do `TK-54` **não** é dele. **Nada disto mexe na `DB-46`:** a regra de célula congelada está correta e intocada — `TK-54` tem núcleo `ready`, é item **vivo**, e sempre esteve do lado *token puro* da regra; o defeito era de **alcance de passo**, não de regra, e nenhuma das seis células terminais muda de tratamento. **Resultado medido na cópia, depois do reparo:** `check` **0 violações**; **E-2** ok; **E-3** ok; elegível `TK-54b`; a diretiva canônica é lida pelo parser como `['TK-54a']`; e os pares da `DB-36` saem `TK-51` **1/1**, `TK-53` **1/1**, `TK-54` **1/2** — confirmando por medida o que o `ESC-3` declarara por cálculo. Os literais de `Verificação` foram rodados **nos dois mundos**: 13 linhas `- **Status:**`, 1 linha do `TK-54` fechando em `|`, 1 `### TK-51a`, 1 diretiva canônica, 1 fechamento `<!-- /fila:gerada -->`. A `Verificação` ganha um item (o 8), que é o único que discrimina o `AE-23`: `1` na cópia migrada contra `0` na árvore de hoje. Rotas descartadas: (a) emendar mais um passo e despachar — é o que a série desmente, e um 4º defeito custaria outro despacho e outra passagem de consultor; (b) encerrar a janela e subir ao dono — o impedimento é técnico e a decisão é de uma célula; o que pertence ao dono é a **série de custo**, e ela sobe pelo relatório de encerramento do `scrum-master` (`G-NOASK`), não por aborto de janela; (c) partir o `BKL-T10` de novo — a simulação mostra o card inteiro chegando a `check` exit 0 num ato, e partir um tema que fecha é o fragmento que a doutrina do módulo proíbe. |
| **`DB-48`** | O bloco gerado da §2.3 se projeta **inteiro** e **dentro do corpus**, em card próprio **antes** do `BKL-T10a` (`ESC-6`, sobre o `AE-27`) | **O fato, medido rodando o verbo em cópia** (`%TEMP%/p0739sim6`, nunca a árvore viva): `backlog.py status TK-48 blocked` sai **exit 0** e **apaga** a linha `**Fila corrente:**`, porque `_bloco_fila_corrente` devolve só os bullets e o escritor substitui **tudo** entre os marcadores por esse retorno; e o bloco resultante não traz bullet de plano **nenhum**, porque o laço casa `plano.id == linha_idx.id` por igualdade exata enquanto o índice publica `P-0739-BKL`. **Há uma terceira metade, e só a simulação a mostrou:** reparadas as duas primeiras, o bloco sai com **15** bullets de plano, **14** de plano **fora do corpus** — cinco arquivos declarando o mesmo `P-0729`, vários com `Status` ausente saindo como `` (`None`, 0/n) ``. `check` e `_candidatos` ganharam o filtro de corpus na `BKL-T10`; `_bloco_fila_corrente` não ganhou. É a mesma classe do `ESC-27` do `P-0740` — *regra ingênua emitiria 12 bullets, 10 deles lixo* — reaparecendo na outra metade do módulo. Com as **três** metades, o bloco sai com **2** bullets (`P-0739` e `TK-54`) e a linha `**Fila corrente:**` sobrevive, regenerada. **Residência:** card **próprio**, `BKL-T10b`, **antes** do `BKL-T10a`. Duas razões, e a segunda é dirimente: (i) são duas proposições ponta a ponta que não se tocam — *o bloco é projetado inteiro* e *o inbox sai do contexto* —, e juntá-las repete o defeito que a `DB-44` partiu; (ii) é **bloqueante de uso**, e o `drain` do `BKL-T10a` **escreve no diário**: entregá-lo antes do reparo assentaria o comportamento quebrado nos TF do próprio `drain`. O identificador é `BKL-T10b` e a ordem de execução o põe **antes** do `BKL-T10a`: a letra numera a inserção, a `Ordem de execução` do cabeçalho manda na fila (§2.1, §2.5 item 4), e o card fica fisicamente entre os dois para que a ordem dos cabeçalhos concorde com ela. **Quarta constatação, e é ato do loop, não deste card:** `transacionar_diretiva` **não** regenera o bloco, contra a §2.3 — hoje isso protege por acidente, e o passo 4 do card unifica a regeneração numa função só (`DB-2`); enquanto o reparo não entra, `backlog.py diretiva` é o **único** verbo de escrita seguro contra o diário vivo. Rotas descartadas: (a) pôr o reparo no `BKL-T10a` — dois temas num card, e o `drain` nasceria testado contra o bloco quebrado; (b) reabrir o `BKL-T10`, que fechou aprovado com ressalva e cujo aceite (`check` exit 0) está satisfeito — o achado é de **uso**, não de entrega, e card fechado não se reabre (`DB-23`); (c) tratar só as duas metades que o `AE-27` nomeia — a simulação mostra que isso entrega um bloco com 14 bullets de lixo, trocando um defeito por outro. |
| **`DB-49`** | Rodar `drain` contra a árvore real é **ato de orquestração do `scrum-master`**, e acontece **entre a `BKL-T11` e a `BKL-T12`** (`ESC-7`, sobre o `AE-31`) | **Quem, e a razão é decisão já fechada:** a `DB-16` diz que *o executor não escreve estado; o `scrum-master` chama o verbo*. `drain` é verbo de escrita, logo rodá-lo é orquestração **por construção** — um card mandando um executor drenar a árvore real **violaria** a `DB-16`. Isso descarta a saída *card próprio*. **Por que não é matéria do dono:** a composição do backlog já foi exercida por ele quando registrou a linha em `docs/plans/_INBOX.md` (Controle 1.1 do `CLAUDE.md` global); `drain` não escolhe nada — §2.4 tira o estado do cabeçalho do próprio plano, o título da linha 1 e a âncora do caminho. Levar isto ao dono é pedir que ele ratifique um ato que já praticou, que é o que o `G-NOASK` proíbe. A leitura do reviewer — *o efeito é composição de backlog* — está certa sobre o **efeito** e não sobre a **decisão**: o efeito é a projeção mecânica de uma decisão anterior. **Quando, e este é o ponto dirimente:** a `BKL-T12` mede o pickup **em sessão nova**, e o conteúdo do corpus entra na medida. Drenar **depois** dela publicaria na `## 15` um número que envelhece no primeiro `drain`; drenar **antes** faz a aferição medir o **estado estável** — inbox em 0, índice completo, `P-0741` no corpus. Soma-se que `drain` é o **único** verbo do instrumento que nunca correu em produção: drenar antes da aferição fecha o plano com todos os verbos exercidos de verdade, que é o que a `## 5` itens 3 e 5 existem para afirmar. Não antes da `BKL-T11` apenas para não pôr variável nova no meio da instalação do hook — nenhum item de aceite das duas tarefas tem o diário no recorte, então a fronteira limpa é **entre** elas. **Não há contradição de prioridade:** a diretiva viva (*Priorize `P-0739`*, dono, 2026-09-20) mantém `P-0741` e `P-0742` atrás deste plano, e o `P-0742` declara `depende de P-0739 done`. Conferência e valores esperados: `## 5` item 6, apurados em cópia (`%TEMP%/p0739sim7`), inclusive a armadilha do contador, que fica em `P-0742` enquanto o arquivo `P-0742` já existe — o plano nasceu sem linha de inbox e o `max(id visto) + 1` nunca passou dele; `check` não acusa, e corrigir para `P-0743` é ato de quem drena. Rotas descartadas: (a) card próprio — viola a `DB-16`; (b) matéria do dono — viola o `G-NOASK` e devolve ao dono um ato mecânico; (c) drenar no fechamento, depois da `BKL-T12` — publica medida de estado transitório e fecha o plano com um verbo nunca exercido. |
| **`DB-50`** | A linha `- **Depende de:**` carrega **só IDs**; razão e insumos vão para bullet próprio (`ESC-7`, achado da simulação) | **Fato medido em cópia, 2026-09-20:** o leitor (`DEPENDE_BULLET_RE`, `.claude/tools/backlog.py:83`, mais `re.findall` de literais entre crases) casa **a primeira linha** do bullet e toma **todo** literal entre crases dela como id de dependência. A `BKL-T11` escrevia *`` `BKL-T10` `` — o hook injeta a saída de `` `next` `` …* e o parser lia `depende = ['BKL-T10', 'next']`; `next` nunca resolve para `done`, logo a tarefa **nunca ficava elegível**, e `backlog.py next` saía *nada delegável — 0 elegível(is)* com a fila cheia. Quatorze cards do plano carregam dependência fantasma pelo mesmo motivo (`DB-*`, `RP-*`, `done`, `drain`, `next`); **só as não-terminais importam**, porque `_eh_elegivel` exige `ready` antes de olhar dependência — e a única viva era a `BKL-T11`, a **próxima da fila**. Regra: essa linha é lista de IDs e nada mais; razão da dependência, decisões e insumos moram em bullet próprio. Aplicada **agora** à `BKL-T11` e à `BKL-T12`; cards `done` **não** são tocados (`DB-23`, sem retroação), porque a fantasma neles é inerte. Medido depois do reparo, na cópia: `next` sai **exit 0** com vencedor **`BKL-T11`** — o pickup selecionando de verdade pela primeira vez. **Nenhum instrumento acusa dependência fantasma:** não há violação `C-*` para id que não resolve, e o sintoma é uma fila vazia que parece decisão. Criar essa guarda é matéria **pós-marco**, sem card, e evidência para a spec de robustez (`TK-55`). Rotas descartadas: (a) deixar a prosa na linha e confiar que o parser só lê a primeira — é acidente, não gramática, e é a mesma classe do `AE-34` (rótulo quebrado faz o campo sumir); (b) alargar o parser para ignorar literal que não case a gramática de ID da `DB-14` — muda instrumento fora do escopo das duas tarefas que restam, e a norma da §2.1 já dizia *`ID`[, `ID`]*; (c) corrigir os quatorze cards — retroação proibida (`DB-23`) e sem efeito, já que card terminal não vira candidato. |
| **`DB-51`** | §2.5 e §2.6 são **comportamento do instrumento**, não matéria de skill: o ponteiro morre, e a skill manda **rodar o verbo** (`ESC-8`, sobre o `AE-33`) | **O fato:** o passo 6 mandava a heurística da `passagem-de-bastao` virar *ponteiro para a §2.5 publicada na skill `diario-de-obras`*, e essa seção **não existe lá** — `.claude/skills/diario-de-obras/SKILL.md:132` declara transcrever *§2.1–§2.4 e §2.7*, e a única ocorrência de `2.5` no arquivo inteiro (301 linhas) é `~2.5k chars`, em outro assunto. **A exclusão não é lacuna, é a decisão certa, e ela antecipava isto:** §2.1–§2.4 e §2.7 são a gramática dos **documentos** — que agentes e humanos escrevem, e por isso precisam ler; §2.5 (ordem de seleção) e §2.6 (forma da saída) são **comportamento de `next`**, que ninguém executa à mão. A residência delas é `.claude/tools/backlog.py`. **Decisão:** o ponteiro **morre**. Onde a prosa explicava a ordenação, o texto passa a mandar rodar `python .claude/tools/backlog.py next` e a dizer que, na recusa, o verbo **nomeia a condição** (`E-1`/`E-2`/`E-3`) e o que se faz é corrigir o dado nomeado. É a leitura que o próprio `Objetivo` do card já pedia — *as skills mandam rodar `backlog.py` em vez de ler diário e inbox à mão* —, e é o que a `DB-43` e a `DB-50` vinham fazendo com o resto do módulo: **um ponteiro a menos, não um ponteiro reapontado**. **Segundo produto, achado pela varredura:** o passo 6 cobria a fila e o fechamento e **não cobria o inbox**, embora o `Objetivo` o nomeie — a `Parte 1` item 1.1 da skill manda drenar *pela operação em prosa da `diario-de-obras`*, texto que o verbo `drain` (entregue na `BKL-T10a`) substitui. O passo passa a ter três atos, (a) fila, (b) inbox, (c) fechamento, com o item 1.2 — fila de candidatos a memória — **inalterado**, porque promover memória é ato do dono. A `Verificação` ganha dois itens que medem o **verbo** na skill (`backlog.py next` e `backlog.py drain`, 1 cada, medidos **0** antes), ao lado do item 4, que media só o arquivo. Rotas descartadas: (a) apontar para a §2.5 **deste plano** — mantém vivo um ponteiro entre skill e plano para matéria que ninguém executa, e é o acoplamento que o módulo vem desfazendo; (b) emendar a `diario-de-obras` para transcrever §2.5 — o `Não fazer` do card veda, a exclusão por desenho contradiz, e criaria **segunda residência** (`DB-2`) para um comportamento que o código já define, envelhecendo no primeiro ajuste de `next`. |
| **`DB-52`** | O reparo do hook mora em **card próprio antes da `BKL-T12`**, e a metade que carrega o peso é a **decodificação**, não a normalização (`ESC-9`, sobre o `AE-35`) | **Reproduzido no ato:** `python .claude/tools/backlog_hook.py` com payload UTF-8 na entrada padrão sai com **0** bytes; com `PYTHONUTF8=1`, **6.997**. **A `e/ou` do laudo está errada, e a medida mostra por quê:** o texto mis-decodificado é `execute o prÃ³ximo passo`, e normalizá-lo pelo `_norm` do precedente (minúsculas + NFKD sem combinantes) dá `execute o pra3ximo passo` — que **não** contém `proximo passo`, porque o `³` do `cp1252` decompõe em `3` sob NFKD. Normalizar **sozinho não conserta**; decodificar sozinho conserta. As duas entram, com papéis declarados: ler `sys.stdin.buffer` e decodificar UTF-8 explicitamente é o reparo; normalizar e escrever o gatilho **sem acento** é ampliação — faz casar `proximo passo`, que um dono digita sem pensar e que hoje falha em silêncio. **Residência: card próprio (`BKL-T11a`), não emenda da `BKL-T12`.** Três razões: (i) são dois temas — *o hook fala* e *o pickup é medido e publicado* —, e juntá-los repete o defeito que a `DB-44` partiu; (ii) a `BKL-T12` é `Opus + dono`, classe `redacao`, e receberia um reparo de código `classe implementacao`; (iii) **dirimente** — o card que **mede** não pode ser o card que **conserta o que ele mede**: a aferição sairia do mesmo ato que produziu o sujeito dela. **O teste que o card exige é o que faltava:** TF por `subprocess`, alimentando **bytes** pela entrada padrão do executável. Os TF da `BKL-T11` entram por importação, com a string já decodificada em memória, e por isso nunca tocaram o `sys.stdin` de um processo — é exatamente a distinção que deixou o defeito passar por um laudo de 91%. **Varredura da classe, feita no mesmo ato:** três entrypoints do kit leem `stdin` pelo mesmo padrão inseguro — `backlog_hook.py:72`, `ocupacao.py:141` e `telemetria_hook.py:213` —, e só o primeiro **quebra hoje**, porque só ele compara literal acentuado; os outros dois recebem mojibake sem falhar, e ficam **nomeados, sem card** (matéria de outro plano, critério (ii)). O achado maior é que **o precedente citado pelo laudo tem a mesma lacuna**: `modelo_por_fase_userpromptsubmit.py:101` também faz `sys.stdin.read()`, e o `_norm` dele não salva um prompt acentuado mis-decodificado — o gate de modelo-por-fase vem degradando em silêncio para prompt com acento. Corrigidos por contraste: `pytest_filter.py` faz `reconfigure(encoding="utf-8")` e `tail_filter.py` lê `sys.stdin.buffer` — os dois únicos que acertam. **Ordem do `drain` (`DB-49`, ponto re-fixado):** indiferente para o resultado — hook mudo não lê corpus, e `drain` não toca o hook —, e por isso fixada por propriedade: o `drain` é o **último ato antes da aferição**, depois do `BKL-T11a`, sem despacho de executor entre a drenagem e a medida. Rotas descartadas: (a) emendar a `BKL-T12` — mistura temas e faz o medidor consertar o medido; (b) só normalizar o gatilho, como a `e/ou` do laudo admite — medido: não conserta; (c) exigir `PYTHONUTF8=1` no registro do hook — move o defeito para a configuração do host, que o kit não controla e que nenhum teste exerce. |
| **`DB-53`** | A regra de teste de executável se completa **agora**, em três cláusulas; a emenda do TF é **pós-plano** (`ESC-10`, sobre o `AE-37`) | **A separação que decide:** o que urge é a **regra**, não o **arquivo de teste**. A propagação aos três entrypoints acontece **fora** do `P-0739`; dentro dele não se escreve mais teste nenhum — a `BKL-T12` é `Opus + dono`, classe `redacao`. Logo completar a regra custa uma decisão e protege as três propagações; emendar o TF custa retroação em card `done` (contra a `DB-23`), dessincroniza card, RDO e laudo, e **não protege nada dentro deste plano**. **A regra, completa, e as três cláusulas valem juntas:** **(1) roda o processo**, não o módulo importado — `subprocess.run([sys.executable, <arquivo>], input=<bytes>, capture_output=True)`, entrada em **bytes** e asserção sobre **bytes**; **(2) fixa o ambiente** com `env=` explícito, montado a partir de um dicionário mínimo, nunca herdado de `os.environ` — herdar faz o teste medir o **host**, não o código; **(3) exerce os dois mundos da variável que fixa e afirma a invariância** — o executável correto dá **a mesma** saída com e sem a variável, e o quebrado dá saídas diferentes. A cláusula 3 é a que o laudo não pediu e é a que torna a regra auto-evidente: ela não depende de o host ter ou não a variável, e é a mesma disciplina de **dois mundos** que o critério (xii)(b) da `RUBRICA_DE_REVISAO.md` §8 já exige de linha de aceite — aplicada ao teste. **Medido no ato, e é a assinatura que quem propaga confere:** hook **pré-reparo**, com `env={SYSTEMROOT, PATH}` → **0** bytes, e com `PYTHONUTF8=1` acrescido → **59**; hook **reparado**, nos dois mundos → **7.123** bytes, iguais. O TF entregue usa `env=None`: ele discrimina **neste** host por acidente (aqui não há `PYTHONUTF8`), e deixaria de discriminar num host que a exporte. Armadilha prática conferida no mesmo ato, para quem propagar: em Windows o subprocesso sobe com `env={}` e também com `{SYSTEMROOT, PATH}` — não é preciso replicar o ambiente inteiro, e é justamente a cópia preguiçosa de `os.environ` que reintroduz o defeito. **Residência do que fica pendente,** para que quem propagar **tropece antes** de propagar: a `DB-53` é a norma; o `AE-36` — entrada que nomeia os três entrypoints e que um propagador lê primeiro — recebe apenso declarando que a regra enunciada lá estava incompleta e apontando para cá; e a emenda do TF do `BKL-T11a` entra na fila do `TK-55` como item nomeado, por ato do `scrum-master`, que é quem escreve o diário. Rotas descartadas: (a) emendar o TF do `BKL-T11a` — card `done`, RDO escrito e laudo dado: retroação que a `DB-23` proíbe, por um risco que não se materializa neste plano; (b) card novo no `P-0739` — matéria nova a 17/18, contra a diretiva do dono de concluir o plano, e sem coesão com o tema (*o pickup vira instrumento*); (c) deixar a regra como está e confiar na conferência manual do `Pronto quando` — é o que o laudo desmonta: conferência manual não escala para três propagações, e a segunda delas é um hook **global**, usado por todos os projetos. |
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

### 2.0 Corpus — o que o instrumento governa (`DB-43`)

O instrumento carrega `docs/DIARIO_DE_OBRAS.md` e todo `docs/plans/P-*.md`, e **não** governa os
dois igualmente. A autoridade sobre a vida de um plano é a **célula de estado da linha dele no
índice do diário** — a `DB-15` já dizia que *o índice é a projeção final* do plano fechado —, casada
pela regra de sufixo da §2.2. Núcleo da célula em `done`, `superseded` ou `cancelled` → o plano está
**fora do corpus**:

- `check` **não o linta**: nem o cabeçalho dele, nem as tarefas dele;
- `next`, `status` e `start` **não o tomam por candidato**: as tarefas dele ficam fora do conjunto
  sobre o qual **E-2** corre (§2.5 item 6), e não só fora dos elegíveis do §2.5 item 3;
- `show <ID>` e a resolução de `Depende de` **continuam a lê-lo**: sair do corpus é deixar de ser
  governado, não deixar de existir.

O campo `**Status:**` do cabeçalho do plano **não** define o corpus. Ele é confrontado com o índice
(`C-5`) enquanto o plano está **dentro** dele; plano fechado cujo cabeçalho diverge do índice é
defeito de **uma linha**, e a `DB-15` fica emendada para autorizar a reconciliação *dessa linha e só
dela* — o corpo do plano fechado segue imutável.

O corpus do diário não depende do índice: todo tíquete e toda subtarefa de `docs/DIARIO_DE_OBRAS.md`
estão sempre dentro dele.

Medida que motivou a regra (2026-09-19, `AE-15`): `carregar` decidia *vivo* pelo campo do próprio
arquivo, campo que a `DB-15` proíbe acrescentar a plano fechado — os 14 planos legados
(`P-0721`..`P-0734`) não o têm, eram lidos como vivos e respondiam por **238** dos 309 achados de
`check`. Sob a regra acima, o único plano em corpus hoje é o **`P-0739`**.

### 2.1 Item e residência

| item | residência viva | cabeçalho | campos obrigatórios logo abaixo |
|---|---|---|---|
| plano | `docs/plans/P-NNNN-<slug>.md` | `# P-NNNN — <título>` (linha 1) | nas 20 primeiras linhas: `**Status:** \`<estado>\`` e `**Prefixo das tarefas no diário:** \`<PFX>-T<n>\``; opcional `**Ordem de execução:** ID → ID → …` (1ª ocorrência vence; ausente = ordem dos cabeçalhos) |
| tarefa de plano | no plano (`### <ID> …`) | `### <ID> — <título> [<modelo>[ + dono] · classe <classe>[ · teto <n>]]` (`DP-C`; ` + dono` marca aceite do dono, ` · teto <n>` é sufixo legado tolerado e ignorado — `DB-20`) | 1º bullet: `- **Status:** \`<estado>\` · AAAA-MM-DD[ · <razão de 1 linha>]`; opcionais `- **Depende de:** \`ID\`[, \`ID\`]`, `- **Tipo:** bug`; `- **Notas de execução:**` com sub-bullets `  - AAAA-MM-DD \`<estado>\` — <texto>` apensados pelo instrumento |
| tíquete | `docs/DIARIO_DE_OBRAS.md` | `## TK-<n> — <título>` (nível 2, **sem** bracket — tíquete não tem modelo nem classe; `DB-17`) | mesmos campos da tarefa (`Status`, `Tipo`, `Notas de execução`) |
| subtarefa de tíquete | `docs/DIARIO_DE_OBRAS.md`, dentro da seção do tíquete-pai | `### TK-<n><letra> — <título> [<modelo> · classe <classe>]` (`DP-C` completa, igual à tarefa de plano; `DB-17`) | mesmos campos da tarefa |

Uma tarefa é *do* plano cujo prefixo casa com o dela; `TK-<n><letra>` é *do* tíquete `TK-<n>`.
**A linha `- **Depende de:**` carrega só IDs** (`DB-50`): o leitor
(`DEPENDE_BULLET_RE` + `re.findall`) casa **a primeira linha do bullet** e toma **todo** literal
entre crases nela como id de dependência. Literal que não é id — nome de verbo, decisão, estado,
seção — vira **dependência fantasma**: ela nunca resolve para `done`, o item nunca fica elegível e
**nenhuma violação de `check` acusa isso**. Razão, decisões e insumos vão para bullet próprio, nunca
para essa linha.

A subtarefa tem os mesmos campos porque **tem projeção de estado própria**, e ela mora só na linha
`- **Status:**` da seção dela — §2.1a (`DB-45`), que também fixa a direção da projeção (filho → pai)
e os treze valores da migração.

### 2.1a Projeção de estado da subtarefa, e os treze valores da migração (`DB-45`)

**A regra.** Subtarefa de tíquete **tem** projeção de estado, e ela mora num lugar só: a linha
`- **Status:**` da seção dela, na forma que a §2.1 já fixa para tarefa e tíquete — estado entre
crases, `· AAAA-MM-DD` opcional, cauda em prosa depois de ` — `. Subtarefa **não** tem linha de
índice, e nenhuma se cria para ela (§2.2, §2.5 item 4 (c)).

**A direção da projeção é sempre filho → pai, nunca o contrário.** A `DB-36` computa o
`<done>/<total>` do pai **a partir** do `Status` dos filhos diretos; a célula do índice do pai é
projeção desse agregado. Derivar o estado do filho a partir do pai inverteria a projeção, fecharia
ciclo e destruiria informação — dois filhos em estados diferentes seriam forçados a um valor só.

**Os treze valores, fechados.** O estado de cada item vivo do diário já está registrado no próprio
documento, mas em cinco formas e cinco lugares diferentes; ler prosa e concluir é juízo, e o
critério (i) da `RUBRICA_DE_REVISAO.md` §8 o proíbe num card. A tabela abaixo é o referente do passo
13 do `BKL-T10`: o executor **transcreve**, não deduz. Medida de 2026-09-19 sobre `eb93490`.

Os números de linha da coluna *evidência* são **referência datada** da árvore de 2026-09-19, antes
da migração: o passo 10 do `BKL-T10` move os blocos de cabeçalho, e depois dele esses números não
apontam mais para o mesmo texto. O que vincula é o **valor** da coluna *estado*, não o ponteiro.

| item | tipo | estado | data | evidência no `docs/DIARIO_DE_OBRAS.md` |
|---|---|---|---|---|
| `TK-23` | tíquete | `cancelled` | 2026-08-24 | célula 145: `backlog *(…absorvido pelo P-0738)*` — a própria célula declara a absorção |
| `TK-32` | tíquete | `cancelled` | 2026-08-13 | célula 146: `**decidido em parte**` + *absorvida pela `DP-Q` em 2026-08-13* |
| `TK-38` | tíquete | `ready` | 2026-08-13 | célula 147, núcleo `ready` |
| `TK-48` | tíquete | `ready` | 2026-09-19 | célula 148, núcleo `ready` |
| `TK-51` | tíquete | `done` | 2026-08-24 | célula 139, núcleo `done` |
| `TK-51a` | subtarefa | `done` | 2026-08-24 | 843 (`linha TK-51 do índice (status → done)`) e 902 (*o `TK-51` está fechado no índice*) |
| `TK-53` | tíquete | `done` | 2026-08-31 | célula 149, núcleo `done` |
| `TK-53a` | subtarefa | `done` | 2026-08-31 | 44: *a `TK-53a` mediu o eixo tempo como `sem degrau`* |
| `TK-53b` | subtarefa | `cancelled` | 2026-08-31 | 46: ***`TK-53b` cancelada por absorção*** |
| `TK-54` | tíquete | `ready` | 2026-08-31 | célula 150, núcleo `ready` |
| `TK-54a` | subtarefa | `done` | 2026-09-18 | 1284, linha `**Status:** \`done\`` fora de forma, e 1588 (*`TK-54a` fechou `done` em 2026-09-18*) |
| `TK-54b` | subtarefa | `ready` | 2026-08-31 | 1588: *`TK-54b` intacta* |
| `TK-55` | tíquete | `ready` | 2026-09-19 | célula 151: `backlog *(aberto por ato do dono em 2026-09-19…)*` |

**Duas armadilhas que a tabela fecha, e que herdar número ou regra da `BKL-T6` reproduziria.**
Primeira: a `BKL-T6` (b) mandava mapear `backlog` → `cancelled` *"absorvido pelo P-0738"*. A regra
vale para `TK-23` e `TK-32` e **não** vale para `TK-55`, que também traz `backlog` na célula mas foi
**aberto** por ato do dono em 2026-09-19 — quatro dias depois de a `BKL-T6` ser autorada. `TK-55` é
`ready`. Segunda: a `BKL-T6` (c) enumerava **15** itens, dez deles `AUT-T1..T10` de um plano que a
`DB-43` tirou do corpus; os itens vivos são **treze**, e são os da tabela acima.

**Os dois defeitos invisíveis ao lint, no mesmo ato** (`DB-45`):

- `docs/DIARIO_DE_OBRAS.md:828` traz `### TK-51 — …`, subtarefa carregando o id do **pai**. Fora da
  gramática `TK-<n><letra>` (violação `C-1`), passa a `### TK-51a — …`; nenhum documento da árvore
  cita `TK-51a` hoje, de modo que a renomeação não quebra ponteiro nenhum.
- `docs/DIARIO_DE_OBRAS.md:150`, a linha de índice do `TK-54`, carrega prosa **depois** do pipe
  final. É a **única** das 32 linhas da tabela do índice que o parser não lê — e, por não a ler,
  `check` não acusa nada. O efeito aparece só depois do card: com `TK-54b` em `ready`, o `TK-54`
  vira pai de candidato elegível sem linha de índice e `next` sai **E-3**. A prosa vai, verbatim,
  para a seção `## TK-54`, e a linha volta a fechar em `|`.

**O que a `DB-36` passa a imprimir** (a fórmula não muda): `TK-51` **1/1**, `TK-53` **1/1** — o
`cancelled` da `TK-53b` sai do denominador —, `TK-54` **1/2**. A **`DB-4` não muda**: medido no ato,
a expressão *candidato a fechamento* não existe em `.claude/tools/backlog.py`, e o rodapé de `next`
imprime `inbox de planos`, `fila de memória` e `blocked`, só. Norma de §3 sem implementação e sem
teste — matéria **pós-marco**, sem card, evidência para a spec de robustez (`TK-55`).

### 2.2 Índice do diário

`| <ID> | <título curto> | <estado>[ <done>/<total>] | <âncora> |` — a célula `Status` contém **só**
o token do vocabulário, opcionalmente seguido de `<done>/<total>` para plano/tíquete com subtarefas.
Nada mais. Título e âncora seguem de autoria humana (o instrumento só cria a linha no `drain` e só
reescreve a célula `Status`).

**Célula de item terminal é projeção final e não se reescreve** (`DB-46`): quando o núcleo da
célula é `done`, `superseded` ou `cancelled`, a célula **pode** carregar a narrativa de fechamento —
ela é a projeção final do item (`DB-15`), e `C-4` não se aplica. A exigência de *só o token* vale
para a célula de item **vivo**, cuja narrativa vai para a seção do item. `C-3` vale para **toda**
linha, terminal ou não: o núcleo tem de ser sempre um token do vocabulário, porque é dele que sai a
decisão de corpus da §2.0.

**O índice tem linha para plano e para tíquete, e para mais ninguém** (`DB-45`): tarefa de plano e
subtarefa de tíquete **não** têm linha de índice, e nenhuma se cria para elas — o estado delas mora
na linha `- **Status:**` da seção própria (§2.1a) e chega ao índice só agregado, no `<done>/<total>`
do pai (`DB-36`). É por isso que o FIFO da §2.5 item 4 (c) lê a linha do **pai** do item, e é por
isso que **E-3** fala do pai, nunca do filho. **A linha do índice fecha em `|`**: texto depois do
pipe final faz a linha inteira deixar de ser lida, sem que `check` acuse nada — medido em
2026-09-19, uma ocorrência em 32 linhas (`docs/DIARIO_DE_OBRAS.md:150`, o `TK-54`).

**Âncora do índice** (`DB-43`): o índice é a tabela que segue o cabeçalho `## Índice` do diário, e
**só** ela — a leitura começa na primeira linha iniciada por `|` depois desse cabeçalho e termina na
primeira linha em branco. Qualquer outra tabela markdown do diário **não** é índice, e nenhuma linha
dela vira linha de índice para efeito nenhum (`check`, `next`, FIFO da §2.5 item 4, reescrita de
célula por `status`). O id de plano publicado no índice leva **sufixo mnemônico**
(`P-0739-BKL`, `P-0740-LM`) e o cabeçalho do arquivo de plano declara só `P-NNNN`: o casamento é
*id exato vence; na falta dele, a primeira linha em ordem de documento cujo id seja
`<id do plano>-<SUFIXO>`, com `SUFIXO` em `[A-Za-z0-9]+`* — residência única em `_posicao_indice`,
e `C-5`/`C-9` usam a mesma regra. Medida que motivou a âncora: 17 linhas de duas tabelas
ilustrativas da seção `## TK-54` eram lidas como índice e produziam **34** dos 60 achados de `check`
no diário.

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
   `Depende de` em `done`. Plano `blocked`/`superseded`/`done`/`cancelled` não contribui. Plano
   **fora do corpus** (§2.0) não produz candidato nenhum, e a exclusão dele **precede** a
   elegibilidade — logo precede também a avaliação de **E-2** do item 6 (`DB-43`).
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

   Fronteira contra o corpus (`DB-43`): o conjunto de candidatos sobre o qual **E-2** corre é o do
   **corpus** da §2.0. Tarefa de plano fora do corpus nunca é candidata e, por isso, **nunca**
   dispara E-2 — a ausência da linha `- **Status:**` nela não é defeito, é o estado normal de um
   plano fechado (`DB-15`). E-2 continua inteira para item e pai **dentro** do corpus: é lá que a
   linha ausente recusa a seleção.

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

Todo verbo age sobre o **corpus** da §2.0 (`DB-43`): `check` linta o diário e só os planos em
corpus; `next`, `status` e `start` só tomam por candidato item cujo pai está em corpus. `show` é a
exceção declarada — lê qualquer item, dentro ou fora dele. `C-5` e `C-9` casam plano pela regra de
sufixo da §2.2, e `cancelled` conta como terminal em `C-9` tanto quanto `done` e `superseded`.

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

### BKL-T9a — Rodada de transcrição: os três módulos `BKL-T10`..`BKL-T12` [Opus · esforço high · classe redacao · teto 50]

- **Status:** `done` · 2026-09-19 — **aprovada 100%**, bloqueante `nenhuma`, as sete dimensões `conforme`, recomendação `escalar`. RDO: `docs/RDO/P-0739-BKL-T9a-rodada-de-transcricao-os-tres-modulos-bkl-t10-bkl-t12.md`; laudo consumido e apagado (`DP-H`). A pendência do laudo **não morre com ele**: segue como `AE-17`, roteada ao consultor pelo `B1`. Fechada em **2 despachos**, **0 retentativas gastas** — o 1º voltou `blocked` razão `premissa` por conduta correta (`A3b` não gasta retentativa) e o `ESC-1` reparou a rota antes do 2º. Estado anterior, para registro: desbloqueada pelo `ESC-1`, rota **(b) generalizada** (`DB-43`), impedimento **técnico/tático**; `check` cai de **309** para **27** achados e o corpus de **20** planos para **1**. Card autorado pelo `scrum-master` no ato da retomada, sob o
  item 3 da *Diretiva de execução do `P-0739`* (dono, 2026-09-19). Lacuna medida: o primeiro ato da
  retomada estava **decidido** (`AE-13` desta série) e **nomeado** na `Fila corrente` do diário, e
  mesmo assim não tinha card despachável — `review_evidence.py --tarefa BKL-T10` saía **exit 1**
  onde `--tarefa BKL-T5` saía **exit 0**, na mesma árvore. Registrada como `AE-14`. **Esta rodada é um card,
  e não uma seção `RP-<n>` em prosa como as sete anteriores:** o `_ID_HEADER_RE` de
  `.claude/tools/rdo.py:85` só aceita identificador da forma `<PREFIXO>-T<n>`, e `RP-8` sai
  **exit 1** no extrator de dossiê. O sufixo de letra segue a convenção que o próprio plano já usa
  para card inserido por rodada (`BKL-T2a`, `BKL-T3a`, `BKL-T3b`): numera depois do card que
  antecede, e executa antes dos três módulos.
- **Esforço:** high
- **Objetivo:** um só — **transcrever**, sem re-decidir nada, a partição já fechada no `AE-13`,
  deixando o plano com três cards de módulo despacháveis a frio (`BKL-T10`, `BKL-T11`, `BKL-T12`) e
  os cinco cards absorvidos fora da fila. Partição, ordem, mapa de herança, regra de re-derivação do
  número e o encerramento do `AE-10` **já estão decididos**: o que falta é forma de card. Decisão
  nova de rota, escopo ou arquitetura **não se abre aqui** — matéria que exija uma volta como
  `blocked` razão `premissa`, nomeando-a.
- **Depende de:** nada. `BKL-T10`, `BKL-T11` e `BKL-T12` dependem desta.
- **Arquivos-alvo:**
  - `docs/plans/P-0739-backlog-instrumento.md`
- **Insumos, e são fechados** (não sondar nada além desta lista):
  - `### AE-13` deste arquivo — partição, ordem `BKL-T10` → `BKL-T11` → `BKL-T12`, mapa de herança
    das superfícies mortas, regra de re-derivação do número e encerramento do `AE-10`.
  - Os cinco cards a absorver, em `## 4` deste arquivo: `BKL-T5`, `BKL-T6`, `BKL-T7`, `BKL-T8` e
    `BKL-T9` — o corpo integral dos cinco é a matéria a reagrupar, e nada dela se perde.
  - `docs/RUBRICA_DE_REVISAO.md` `## 8` e `### 8.1` — rubrica de criação de tarefa e forma normativa
    do bloco `Verificação`; é a régua dos três cards novos.
  - `GOVERNANCA.md` §3, *A unidade de trabalho* — gramática de cabeçalho que os parsers aceitam, e
    a tabela de tetos de onde sai o campo `teto` de cada módulo.
  - `## 2` e `## 3` deste arquivo — gramática do instrumento e superfície de comandos que os três
    módulos realizam. **Já reparados** pela `DB-43` no `ESC-1` da retomada: §2.0 (corpus), âncora do
    índice em §2.2, fronteira de **E-2** em §2.5 e o parágrafo de corpus em §3.
  - `### DB-43` na tabela de `## 1` — decisão do consultor sobre o `AE-15`, que torna o aceite do
    `BKL-T10` satisfazível e **reduz** a matéria herdada da `BKL-T6`. A transcrição a **cita**; não
    a reabre e não a reescreve.
- **Duas superfícies estão mortas, e a varredura não se repete** (`AE-13`, via `ESC-35` do
  `P-0740`): `.claude/skills/proximo-passo/SKILL.md` e `.claude/skills/handover/SKILL.md` foram
  removidas da árvore, e a **herdeira da matéria** é `.claude/skills/passagem-de-bastao/SKILL.md`,
  com o `scrum-master` ficando com a parte de condução do loop. Card transcrito com alvo morto
  bloqueia no despacho — por isso o `BKL-T11` **não** herda os dois caminhos da `BKL-T8`. Não são
  alvo morto, apesar de ausentes: `backlog_hook.py` (arquivo a criar pela matéria da `BKL-T7`),
  `GOVERNANCA_MEMORIAS.md` (doc global, fora do repo) e os padrões de nome de plano em prosa.
- **A matéria herdada da `BKL-T6` encolheu, e o card transcreve o que a `DB-43` deixou** — sem
  re-decidir nada. `docs/plans/P-0737-loop-autonomo.md` **sai** dos `Arquivos-alvo` do `BKL-T10`: o
  plano está `superseded` desde 2026-09-18 (`DM-1` do `P-0740`) e, pela §2.0, fora do corpus — com
  ele morrem o item (c) *parte `AUT-T1..T10`*, o item (d) e o item (e) da `BKL-T6`. O que resta da
  `BKL-T6` é `docs/DIARIO_DE_OBRAS.md` — itens (a), (b), (c) *parte tíquetes* e (f) — mais **matéria
  nova**, criada pela `DB-43` e que nenhum dos cinco cards cobria: o reparo de corpus em
  `.claude/tools/backlog.py`, com TF em `tests/test_backlog.py`, e a reconciliação de **uma** linha
  `**Status:**` no cabeçalho de cada um dos três planos que divergem do índice (`P-0735`, `P-0737`,
  `P-0738`). Números medidos no ato do `ESC-1`, a **re-derivar** na transcrição como qualquer outro:
  `check` cai de **309** para **27** achados — **24** em `docs/DIARIO_DE_OBRAS.md` (11 `C-2`, 8
  `C-4`, 3 `C-3`, 2 `C-1`) e **3** `C-5` de cabeçalho de plano. Nota de armadilha, medida no mesmo
  ato: a linha de diretiva do diário hoje é `**Diretiva de priorização (EMERGÊNCIA — dono,
  2026-09-18):** …`, forma que o parser **não** casa (ele lê `**Diretiva de priorização:**`), então
  `next` corre hoje sem restrição de diretiva; a migração da `BKL-T6` (a) muda isso e o número de
  `next` pós-entrega se mede **depois** dela.
- **Nenhum número de aceite se copia dos cinco cards.** Todo número que um aceite herdado carregava
  — por exemplo o *≥ 3 arquivos* da `BKL-T8` — **re-deriva-se sobre a árvore de hoje**; o que se
  transcreve é a **relação**, *toda skill que invoca o instrumento o cita*. Medida de hoje para essa
  relação: **1**. O mesmo vale para os demais números de aceite dos três módulos: cada `Verificação`
  traz o número medido **no ato desta rodada**, com a linha `Medido antes:` explícita.
- **Produto do módulo:**
  - **(a) Três cards de módulo** em `## 4. Tarefas`, nesta ordem e imediatamente **antes** do
    `### BKL-T5`: `BKL-T10` (absorve `BKL-T5` + `BKL-T6` — `drain`, o reparo de corpus da `DB-43` e a
    migração dos documentos vivos até `check` verde), `BKL-T11` (absorve `BKL-T7` + `BKL-T8` — o hook, o ponto de carga e as
    skills que passam a invocar o instrumento), `BKL-T12` (absorve `BKL-T9` sozinha — aferição do
    pickup e revisão do `README.md`, com veredito do dono). Cada um com cabeçalho na gramática de
    `GOVERNANCA.md` §3, `Status: ready`, `Esforço`, `Objetivo` **único**, `Depende de`,
    `Arquivos-alvo` em caminhos vivos, `Restrições` e bloco `Verificação` conforme
    `RUBRICA_DE_REVISAO.md` §8.1.
  - **(b) Os cinco cards absorvidos passam a `cancelled`**, razão *absorvido por `<ID do módulo>`*,
    com o corpo preservado **verbatim** e o bullet `- **Absorvida por:**` mantido. Nada se apaga: o
    corpo dos cinco é a fonte que os três módulos citam.
  - **(c) O `AE-10` marcado como encerrado** onde ele mora, pelo reparo `AE-47` **do `P-0740`** (a
    guarda de `transacionar_status` dissolveu a dependência de ordem com os marcadores
    `<!-- fila:gerada -->`), com o qualificador de plano na citação, como o `AE-13` exige.
  - **(d) A linha `**Ordem de execução:**` do cabeçalho** reescrita para a ordem viva —
    `BKL-T10` → `BKL-T11` → `BKL-T12` —, com os cards terminais nomeados entre parênteses, como a
    linha já faz hoje.
- **Restrições desta tarefa:** um único arquivo é tocado — `docs/plans/P-0739-backlog-instrumento.md`.
  Nenhum código, nenhum teste, nenhuma skill, nenhum doc de kit, nenhuma linha do
  `docs/DIARIO_DE_OBRAS.md` (o kanban é do `scrum-master`). O corpo dos cinco cards absorvidos
  **não se reescreve**: muda a linha `Status` deles e nada mais. Nenhuma seção de `## 1` a `## 3`
  (decisões, gramática, superfície) é alterada — se a transcrição exigir mexer em qualquer uma
  delas, é decisão nova: devolver `blocked` razão `premissa`. As emendas que o `AE-15` exigia **já
  estão aplicadas** nessas seções pelo consultor (`DB-43`, `ESC-1`): a transcrição as **cita**, e
  não as reescreve.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0739-backlog-instrumento.md -Pattern '^### BKL-T1[012] ' | Measure-Object).Count"
     ```
     → **3**: os três módulos existem como heading. **Medido antes: 0**.
  2. ```
     python .claude/tools/review_evidence.py --plano docs/plans/P-0739-backlog-instrumento.md --tarefa BKL-T10 --desde HEAD
     ```
     idem para `BKL-T11` e `BKL-T12` → **exit 0** nos três: o parser que consome o card no despacho
     aceita os três. **Medido antes: exit 1 para `BKL-T10`**, contra **exit 0** para `BKL-T5` na
     mesma árvore — o par discrimina card ausente de card presente, e não a saúde do extrator.
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0739-backlog-instrumento.md -Pattern '^- \*\*Status:\*\* `cancelled`' | Measure-Object).Count"
     ```
     → **5**: um por card absorvido, nem mais nem menos. **Medido antes: 0** (medido no ato do
     `ESC-1`, com esta forma já escrita no arquivo). A âncora `^- ` conta **linha de campo
     `Status` de card** e nada mais: a própria linha de comando deste item não casa, e menção em
     prosa também não — a forma anterior (`-SimpleMatch` sem âncora) media **1** por contar a si
     mesma (`AE-15`, achado secundário).
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0739-backlog-instrumento.md -Pattern '^- \*\*Status:\*\* `ready`' | Measure-Object).Count"
     ```
     → **3**: só os três módulos ficam `ready`. **Medido antes: 5** — os cinco absorvidos, medidos
     no ato do `ESC-1` com esta forma já escrita no arquivo (a forma anterior media **6**, contando
     a si mesma). O par com o item 3 prova a **troca**, e não só a chegada dos novos: 5 `ready` + 0
     `cancelled` **antes**, 3 `ready` + 5 `cancelled` **depois**.
  5. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0739-backlog-instrumento.md -Pattern '\.claude/skills/proximo-passo/SKILL\.md','\.claude/skills/handover/SKILL\.md' | Measure-Object).Count"
     ```
     → **6**, **invariante**: as seis ocorrências do caminho completo vivem no `## Contexto`, no
     corpo preservado da `BKL-T8` (dois `Arquivos-alvo`), no bullet de superfície morta deste card e
     na prosa do `AE-13` (duas) — medidas no ato do `ESC-1`, com esta forma já escrita no arquivo.
     Número maior significa alvo morto transcrito para card novo, que é o defeito que esta rodada
     existe para não cometer. O padrão exige o caminho **inteiro** (`.claude/…/SKILL.md`), e por
     isso a própria linha de comando deste item não casa — a forma anterior (`'skills/proximo-passo'`
     solto) media **7**, contando a si mesma (`AE-15`, achado secundário). **Medido antes: 6**.
  6. ```
     git diff --unified=0 -- docs/plans/P-0739-backlog-instrumento.md
     ```
     → **dentro do corpo dos cinco cards absorvidos** (do heading `### BKL-T5` ao fim do
     `### BKL-T9`), a **única** remoção é a linha `Status` de cada um. Conferência contra a fonte:
     prova que o corpo dos cinco foi preservado verbatim, que é a condição de os três módulos
     poderem citá-los. **O diff contra `HEAD` traz também o reparo do consultor** (`DB-43`, `ESC-1`)
     nas seções `## 1`, `## 2` e `## 3` e neste card `BKL-T9a`, porque a janela não commita fora dos
     marcos de validação: essas linhas **não** são da entrega e não entram neste item — o recorte é
     a faixa dos cinco cards.
- **Pronto quando:** os seis itens de `Verificação` saem com o número esperado, e o `git diff`
  do item 6 mostra remoção **apenas** nas cinco linhas `Status` dos cards absorvidos, na linha
  `**Ordem de execução:**` do cabeçalho e na linha do `AE-10` que passa a encerrado — nenhuma
  outra remoção **autorada nesta rodada** no arquivo, e nenhum outro arquivo tocado. As linhas do
  reparo `DB-43` já presentes na árvore de trabalho não são remoção desta rodada e não contam aqui.

### BKL-T10 — Corpus do instrumento e a migração do diário até `check` verde [Sonnet · esforço high · classe implementacao]
- **Status:** `done` · 2026-09-20 — **aprovada com ressalva, 85%**, bloqueante `nenhuma`, recomendação `escalar`. RDO: `docs/RDO/P-0739-BKL-T10-corpus-do-instrumento-e-a-migracao-do-diario-ate-check-verde.md`; laudo consumido e apagado (`DP-H`). **`backlog.py check` exit 0, nenhuma violação** — o aceite que o card existia para produzir. Entregue no **6º despacho**, com **0 retentativas gastas**: os cinco anteriores não produziram linha e nenhum foi defeito de produto — três `blocked premissa` por defeito do card (`AE-19`, `AE-21`, `AE-23`), uma queda por limite de conta com o parcial descartado por ato do dono (`AE-25`) e um `blocked` por defeito do despacho (`AE-26`). A pendência do laudo **não morre com ele**: segue como `AE-27`, roteada ao consultor pelo `B1`, e é **bloqueante de uso** — o instrumento não deve receber `status`/`start` antes do reparo. Autorado pela `BKL-T9a`; absorve `BKL-T6` (a `BKL-T5` saiu para o `BKL-T10a` pela `DB-44`), e carrega a matéria nova que a `DB-43` criou
- **Esforço:** high
- **Objetivo:** `python .claude/tools/backlog.py check` sai **exit 0** contra a árvore real e `next`
  deixa de sair **exit 3**, por dois atos do mesmo tema — o instrumento passa a governar o **corpus**
  da §2.0 e o `docs/DIARIO_DE_OBRAS.md` é migrado para a gramática da §2. O verbo `drain` **saiu
  deste card** para o `BKL-T10a` (`DB-44`, `ESC-2`): é outra proposição ponta a ponta.
- **Depende de:** `BKL-T9a`. Decisões: `DB-43` (corpus derivado do índice), `DB-44` (partição deste
  card e do `BKL-T10a`), `DB-45` (projeção de estado da subtarefa e os treze valores da migração),
  `DB-46` (célula de item terminal é projeção final; bloco de migração reautorado), `DB-15` (o índice é a projeção final do plano fechado, emendada pela
  `DB-43`), `DB-11` (diretiva de priorização), `DB-17` (cabeçalho de subtarefa com modelo), `DB-33`
  (um bullet por pai vivo), `DB-36` (fórmula `<done>/<total>`), `DB-37` (exit 3 não toca arquivo).
  Fatos: §2.0, §2.1, §2.1a, §2.2, §2.3, §2.5 itens 3 e 6, §2.7 e §3 deste plano.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
  - `docs/DIARIO_DE_OBRAS.md`
  - `docs/plans/P-0735-residencia-e-ponto-de-carga.md`
  - `docs/plans/P-0737-loop-autonomo.md`
  - `docs/plans/P-0738-contexto-esgotado.md`
- **Passos — bloco A, o corpus (`DB-43`, `DB-46`), em `.claude/tools/backlog.py`:**
  1. Em `_parse_indice` (`.claude/tools/backlog.py:291`), ancorar a leitura do índice: começar na
     primeira linha iniciada por `|` **depois** do cabeçalho `## Índice` e parar na primeira linha
     em branco. Nenhuma outra tabela markdown do diário produz linha de índice.
  2. Em `carregar` (`.claude/tools/backlog.py:392`), marcar cada plano com o núcleo da célula de
     estado da linha dele no índice, casada pela regra de sufixo de `_posicao_indice`
     (`.claude/tools/backlog.py:634`); núcleo em `done`, `superseded` ou `cancelled` → o plano está
     **fora do corpus**.
  3. Em `check` (`.claude/tools/backlog.py:465`), não lintar plano fora do corpus: nem o cabeçalho
     dele (`C-7`, `C-8`), nem as tarefas dele (`C-1`, `C-2`).
  4. Em `_candidatos` (`.claude/tools/backlog.py:616`), não produzir candidato de plano fora do
     corpus; a exclusão por corpus **precede** a elegibilidade de `_eh_elegivel`
     (`.claude/tools/backlog.py:716`) e precede a avaliação de **E-2**.
  5. No ponto em que `check` resolve o id da linha de índice para `C-5` e para `C-9`
     (`.claude/tools/backlog.py:525`, hoje via `_status_do_id`, `.claude/tools/backlog.py:430`),
     casar id de plano pela mesma regra de sufixo de `_posicao_indice`, e acrescentar `cancelled` ao
     conjunto terminal de `C-9`, ao lado de `done` e `superseded`.
  6. No mesmo ponto, **`C-4` deixa de valer para linha de índice cujo núcleo é terminal**
     (`done`, `superseded`, `cancelled`): a célula de item terminal é a **projeção final** dele
     (`DB-15`) e não se reescreve (`DB-46`). **`C-3` segue valendo para toda linha**, terminal ou
     não — o núcleo alimenta a decisão de corpus do passo 2 e tem de ser sempre um token do
     vocabulário. Medida de 2026-09-19, fora do literal: `C-4` cai de **8** para **2**.
  7. Deixar `show` (`.claude/tools/backlog.py:588`) e a resolução de `Depende de` lendo plano fora
     do corpus: sair do corpus é deixar de ser governado, não deixar de existir.
- **Passos — bloco B, a migração de `docs/DIARIO_DE_OBRAS.md` (§2.2, §2.3).** Bloco **reautorado
  inteiro** no `ESC-4` (`DB-46`) contra a árvore de 2026-09-19: os números de linha e as
  enumerações abaixo são medidos no ato, e substituem os herdados da `BKL-T6` (2026-09-15). Toda
  linha citada vem com o literal que a abre, para que o executor confirme o alvo sem contar linhas:
  8. **A linha de diretiva.** `docs/DIARIO_DE_OBRAS.md:3`, que hoje abre em
     `**Diretiva de priorização (EMERGÊNCIA — dono, 2026-09-18):**`, passa à forma que
     `_parse_diretiva` lê: o rótulo exato `**Diretiva de priorização:**`, seguido de `Priorize `, do
     id `TK-54a` entre crases, de ` — ` e do texto de hoje preservado **verbatim** a partir de
     `vem antes de tudo`. O id priorizado é o que a própria linha já nomeia; a prioridade do dono
     não muda, só a forma que o parser lê. As duas *Diretivas de execução* (`P-0740`, linhas 5–23;
     `P-0739`, linhas 25–35) são atos do dono, **não** são fila e **não se tocam**.
  9. **O bloco gerado.** Inserir, imediatamente abaixo da linha de diretiva, o bloco da §2.3
     delimitado por `<!-- fila:gerada -->` e `<!-- /fila:gerada -->`, com a linha
     `**Fila corrente:**` na forma fixa e um bullet por pai vivo (`DB-33`). Os dois marcadores ficam
     **sozinhos na própria linha**: `transacionar_status` (`.claude/tools/backlog.py:1118-1121`) os
     localiza por **igualdade exata de linha**, e marcador embutido em linha de prosa não é achado
     por ele. Medida de 2026-09-19, fora do literal: a abertura aparece **1** vez hoje, embutida na
     prosa da linha 40, e o fechamento **0** — o par inserido por este passo é o primeiro real.
  10. **Os três parágrafos de fila, com destino nomeado um a um.** São **três**, medidos no ato, e
      nenhum se parte por assunto — partir é autoria, e aqui só se move:
      - `docs/DIARIO_DE_OBRAS.md:37-38`, que abre em `**Fila corrente:** **\`P-0740\` FECHADO em
        35/35` → vai para a seção **`## P-0739`**, como bullet datado `2026-09-19`;
      - `docs/DIARIO_DE_OBRAS.md:40`, que abre em `**Fila corrente anterior (texto de 2026-09-18` →
        vai para a seção **`## P-0739`**, como bullet datado `2026-09-18`. É o destino que a própria
        linha publica (*"migra para `## P-0739` na condensação"*);
      - `docs/DIARIO_DE_OBRAS.md:42-111`, que abre em `**Fila corrente anterior (texto de
        2026-08-31` e termina em `arquivos do plano/relatório. Consumo: ver \`docs/telemetria.tsv\`.`
        → vai **inteiro e verbatim**, as 70 linhas, para o fim da seção **`## TK-54`**, como bullet
        datado `2026-08-31`. A linha 42 cita `## TK-54`/`## TK-53` *conforme o assunto*: escolher
        assunto linha a linha é juízo, e a `DB-46` fecha em `## TK-54`, que é o assunto com que o
        bloco abre.
      A seção `## P-0739` **não existe** no diário (medido: existem `## P-0737` e `## P-0738`, e é a
      forma que eles já dão a registro de janela de plano). Criá-la, com o título
      `## P-0739 — O pickup vira instrumento`, imediatamente **antes** de `## TK-23`, é parte deste
      passo. Ela é seção de **registro**, não residência de plano: o plano segue em
      `docs/plans/P-0739-backlog-instrumento.md`, e a âncora da linha de índice do `P-0739-BKL`
      **não muda**.
  11. **A linha do índice do `TK-54`, inteira e num ato só.** `docs/DIARIO_DE_OBRAS.md:150` tem
      **dois** defeitos na mesma linha, e os dois se tratam juntos — este passo vem **antes** do 12
      por isso: (a) ela carrega prosa **depois** do pipe final, e por isso `INDICE_LINHA_RE`, que
      exige que a linha feche em `|`, **não a lê** — é a única das 32 linhas da tabela nessa
      condição, e `check` não acusa nada enquanto ela não for lida; (b) a **célula 3** dela é
      `ready *(**escopado em 2026-08-31** …)*` — item **vivo** com prosa, logo `C-4` pela `DB-46`,
      violação que **só passa a existir depois** de (a) ser corrigido. As duas prosas — a de depois
      do pipe e a da célula 3 — vão, verbatim, para o fim da seção `## TK-54`, como bullets datados
      `2026-09-19`; a célula 3 fica com o token puro `ready`; a linha volta a fechar em `|`. Sem
      isto, `check` **não** sai exit 0, e o `TK-54` fica pai de candidato elegível sem linha de
      índice assim que a `TK-54b` receber `ready`, com `next` em **E-3** — efeito que só apareceria
      depois do fim deste card, porque enquanto ele estiver `in-progress` a §2.5 item 2
      curto-circuita a seleção antes da elegibilidade.
  12. **As demais células do índice.** Só a célula de item **vivo** vira token puro; célula de item
      terminal é a projeção final dele e **fica como está** (`DB-46`, passo 6). A célula do `TK-54`
      **não** entra nesta lista: foi tratada inteira no passo 11. São **cinco** atos, enumerados e
      fechados, medidos em 2026-09-19:
      - `C-3`, núcleo fora do vocabulário — o núcleo é substituído e **a prosa da célula
        permanece**: linha 145, `TK-23`, `backlog` → `cancelled`; linha 146, `TK-32`,
        `**decidido em parte**` → `cancelled`. Os dois valores são os da tabela da §2.1a e não se
        deduzem;
      - `C-3` **e** `C-4` na mesma linha: linha 151, `TK-55`, núcleo `backlog` → `ready` e, como
        `ready` é vivo, a célula passa a token puro com a narrativa indo para `## TK-55`;
      - `C-4`, célula de item vivo com prosa — a célula passa a conter **só** o token e a narrativa
        vai **verbatim** para a seção do item no próprio diário, como bullet datado `2026-09-19`:
        linha 147, `TK-38` → `## TK-38`; linha 148, `TK-48` → `## TK-48`.
      - **Ficam como estão, por serem terminais** (nenhuma edição, nenhum movimento): linha 131
        `P-0733-DHB`, linha 132 `P-0734-EXA`, linha 135 `P-0737-AUT`, linha 139 `TK-51`, linha 140
        `TK-52`, linha 149 `TK-53`. É o que dissolve o conflito do `AE-21`: nenhuma narrativa
        precisa ir para `docs/DIARIO_HISTORICO.md` nem para corpo de plano fechado.
  13. **A linha `- **Status:**` dos treze itens vivos.** Dar a cada item vivo do diário a linha
      `- **Status:**` na forma da §2.1 — estado entre crases, ` · AAAA-MM-DD`, cauda em prosa
      opcional depois de ` — ` —, como **primeiro bullet** da seção do item. Os itens e os valores
      são os **treze** da tabela da §2.1a (`DB-45`), e são **transcritos**: nenhum valor se deduz,
      se re-deriva ou se lê de prosa, e o núcleo da célula do índice **não** é referente de
      subtarefa nenhuma, porque subtarefa não tem linha de índice. Dois casos são **substituição**,
      não inserção: a `TK-54a`, que traz em `docs/DIARIO_DE_OBRAS.md:1284` um `**Status:**` sem o
      `- ` inicial e sem data — a prosa entre parênteses dessa linha é preservada como cauda, depois
      de ` — ` —, e qualquer outro item em que a varredura encontre a mesma irregularidade.
  14. **Os dois cabeçalhos de subtarefa fora da gramática**, medidos em 2026-09-19 e fora do
      literal: (a) `docs/DIARIO_DE_OBRAS.md:1475`, `### TK-54b`, recebe `Sonnet · ` imediatamente
      antes de `classe` (`DB-17`) — a `TK-54a` **já** o tem e não se toca; (b)
      `docs/DIARIO_DE_OBRAS.md:828`, `### TK-51`, é subtarefa carregando o id do **pai** e passa a
      `### TK-51a`, mantido o resto do cabeçalho (`DB-45`). Só o id muda, e nenhum documento da
      árvore cita `TK-51a` hoje.
- **Passos — bloco C, a reconciliação de cabeçalho de plano fechado (`DB-15` emendada pela `DB-43`).**
  Os três referentes foram reconferidos no `ESC-4` e estão exatos:
  15. Em `docs/plans/P-0735-residencia-e-ponto-de-carga.md:3` — linha que abre em `**Data:**
      2026-08-15` e carrega o campo `**Status:**` adiante —, trocar o estado `ready` por `done`.
  16. Em `docs/plans/P-0737-loop-autonomo.md:4`, na linha que carrega o campo `**Status:**` do
      cabeçalho, trocar o estado `ready` por `superseded`.
  17. Em `docs/plans/P-0738-contexto-esgotado.md:4`, na linha que carrega o campo `**Status:**` do
      cabeçalho, trocar o estado `ready` por `done`.
- **Passos — bloco D, os testes:**
  18. Escrever em `tests/test_backlog.py` os sete TF do campo `Testes`, todos sobre cópia de
      fixture em `tmp_path`.
- **Restrições desta tarefa (copiadas inline; nenhuma vale por ponteiro):**
  - **Corpus (§2.0):** a autoridade sobre a vida de um plano é a célula de estado da linha dele no
    índice do diário. Núcleo em `done`, `superseded` ou `cancelled` → `check` não o linta e
    `next`/`status`/`start` não o tomam por candidato; `show` e a resolução de `Depende de`
    continuam a lê-lo. O campo `**Status:**` do cabeçalho do plano **não** define o corpus.
  - **`C-5` continua valendo para plano fora do corpus:** ele é o confronto da linha do índice com o
    campo do cabeçalho, e não lint do plano — é ele que acusa as três divergências do bloco D.
  - **Âncora do índice (§2.2):** o índice é a tabela que segue o cabeçalho `## Índice`, e só ela.
  - **Casamento de id de plano (§2.2):** id exato vence; na falta dele, a primeira linha em ordem de
    documento cujo id seja `<id do plano>-<SUFIXO>`, com `SUFIXO` em `[A-Za-z0-9]+`. Residência
    única em `_posicao_indice` — nenhum outro ponto do instrumento reescreve esse casamento.
  - **Célula do índice (§2.2):** contém só o token do vocabulário, opcionalmente seguido de
    `<done>/<total>`. Título e âncora são de autoria humana e o instrumento não os reescreve. A
    linha do índice **fecha em `|`**: texto depois do pipe final faz a linha inteira deixar de ser
    lida, e `check` não acusa nada.
  - **Célula de item terminal (§2.2, `DB-46`):** núcleo em `done`, `superseded` ou `cancelled` →
    a célula é a **projeção final** do item, carrega a narrativa de fechamento e **não se
    reescreve**; `C-4` não se aplica a ela. Só a célula de item **vivo** vira token puro, e só a
    narrativa dela se move — sempre para a seção do item **no próprio diário**. `C-3` vale para
    toda linha, terminal ou não.
  - **Estado de subtarefa (§2.1a, `DB-45`):** mora **só** na linha `- **Status:**` da seção dela;
    subtarefa **não** tem linha de índice e nenhuma se cria. A projeção corre **filho → pai** — a
    célula e o `<done>/<total>` do pai derivam do estado dos filhos, nunca o contrário. Os treze
    valores desta migração estão **fixados** na tabela da §2.1a e se **transcrevem**: nenhum se
    deduz de prosa, e nenhum se lê da célula do pai.
  - **Diretiva (§2.3):** o instrumento lê só os tokens de id entre crases que vêm **antes** do
    primeiro ` — `; o que vier depois é texto livre, para humanos.
  - **Mover, nunca apagar:** nenhum texto do diário se perde nesta migração; a narrativa sai da
    célula e entra na seção do item, verbatim.
  - **Plano fechado:** nos três arquivos do bloco D muda-se **uma** linha por arquivo — a que carrega
    o campo `**Status:**` do cabeçalho — e nada mais. O corpo de plano fechado é imutável.
  - **Nenhum número de aceite se copia dos cards absorvidos:** as *26 células* e os *15 itens* que a
    `BKL-T6` enumerava são referência datada de 2026-09-15. O que vale é a relação — `check` sai
    exit 0 —, e o número se re-deriva no despacho.
  - **Piso de regressão como relação:** a entrega soma os `<N>` testes novos e **não reduz** o total
    de `python -m pytest tests/ -q` re-medido no próprio despacho. Referência datada de 2026-09-19:
    `tests/test_backlog.py` com 49 testes, suíte inteira com 201.
- **Não fazer:**
  - Não acrescentar linha `Status` a tarefa de plano fora do corpus — os `AUT-T1`..`AUT-T10` do
    `P-0737`, os `CTX-T*` do `P-0738`, os `T1`..`T55` do `P-0734`: a `DB-43` os tirou do corpus e a
    `DB-15` proíbe escrever no corpo de plano fechado.
  - Não tocar `docs/DIARIO_HISTORICO.md`.
  - Não implementar o verbo `drain`, não tocar `docs/plans/_INBOX.md` nem
    `docs/plans/_INBOX_HISTORICO.md`: é matéria do `BKL-T10a` (`DB-44`).
  - Não editar `README.md`, nem `.claude/skills/`, nem `.claude/projecoes.json` — matéria do
    `BKL-T11` e do `BKL-T12`.
  - Não editar as seções `## 1`, `## 2` e `## 3` de `docs/plans/P-0739-backlog-instrumento.md`, nem
    card nenhum deste plano.
- **Contingências:**
  - se, depois dos blocos A a D, `check` acusar achado em arquivo que **não** está nos
    `Arquivos-alvo` deste card → parar e sinalizar `blocked` razão `premissa`, citando o código da
    violação e o caminho;
  - se `next` sair **exit 2** depois da migração → seguir com a entrega: o que o item 2 da
    `Verificação` afirma é que `next` deixou de sair exit 3, e exit 2 satisfaz isso;
  - se a linha `**Status:**` do cabeçalho de um dos três planos do bloco D já estiver com o estado do
    índice → seguir sem tocar naquele arquivo;
  - se `docs/DIARIO_DE_OBRAS.md` não tiver o cabeçalho `## Índice` → parar e sinalizar `blocked`
    razão `premissa`.
- **Testes** (`tests/test_backlog.py`, todos sobre cópia de fixture em `tmp_path`):
  - `test_tf_plano_terminal_no_indice_sai_do_corpus_do_check` — plano cujo núcleo de célula é `done`
    não produz violação nenhuma, e o mesmo plano com célula `ready` produz. A regra concorrente
    (corpus decidido pelo campo do cabeçalho) daria violação nos **dois** mundos: é isso que esta
    fixture separa.
  - `test_tf_plano_terminal_no_indice_nao_produz_candidato` — tarefa `ready` de plano com célula
    `superseded` não aparece em `next` e **não** dispara E-2 sobre o pai dela.
  - `test_tf_show_le_plano_fora_do_corpus` — `show` de um item desse mesmo plano devolve o dossiê.
  - `test_tf_tabela_alheia_nao_vira_linha_de_indice` — diário com uma tabela markdown fora da seção
    `## Índice`: nenhuma linha dela produz `C-3`/`C-9`, e a tabela sob `## Índice` produz.
  - `test_tf_c5_casa_plano_por_sufixo_do_indice` — linha de índice `P-0777-XYZ` com núcleo `done`
    contra cabeçalho de `P-0777` com campo `ready` → uma violação `C-5`; com o campo `done` →
    nenhuma.
  - `test_tf_c4_nao_vale_para_celula_de_item_terminal` — duas linhas de índice com a **mesma**
    prosa na célula, uma com núcleo `done` e outra com núcleo `ready`: `C-4` sai **só** para a
    viva. A regra concorrente — `C-4` para toda célula com prosa — acusaria as **duas**, e é isso
    que esta fixture separa (`DB-46`).
  - `test_tf_c9_aceita_cancelled_como_terminal` — linha de índice com núcleo `cancelled` e sem
    residência não produz `C-9`; com núcleo `ready`, produz.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command "python .claude/tools/backlog.py check > $null 2>&1; $LASTEXITCODE"
     ```
     → **0**. **Medido antes: 1**. Referência datada de 2026-09-19, fora do literal: o vermelho de
     hoje traz 309 achados, 238 deles em planos que a `DB-43` tira do corpus.
  2. ```
     pwsh -NoProfile -Command "python .claude/tools/backlog.py next > $null 2>&1; if ($LASTEXITCODE -eq 3) { 'exit-3' } else { 'sem-exit-3' }"
     ```
     → **sem-exit-3**. **Medido antes: exit-3**. O veredito é binário de propósito: `next` sair 0
     (vencedor) ou 2 (nada elegível) depende da diretiva e do estado dos itens, e o que esta tarefa
     possui é a saída do dado que impedia a seleção.
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/DIARIO_DE_OBRAS.md -Pattern '^\*\*Diretiva de prioriza[^ ]*o:\*\* ' | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. O padrão exige que o rótulo termine em `:` mais dois asteriscos
     sem espaço no meio, e por isso separa a forma canônica da forma de hoje
     (`**Diretiva de priorização (EMERGÊNCIA — dono, 2026-09-18):**`), que devolve 0.
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/DIARIO_DE_OBRAS.md -Pattern '<!-- /fila:gerada -->' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. O marcador de **fechamento** é o que discrimina: o de abertura já
     aparece hoje, uma vez, citado em prosa na `Fila corrente`, e mediria 1 nos dois mundos.
  5. ```
     python -m pytest tests/test_backlog.py -q
     ```
     → **verde**. **Medido antes: verde**. O que discrimina não é o veredito, e sim a relação: o
     total sai do total re-medido no início do despacho **mais** os `<N>` testes novos do campo
     `Testes`. Em seguida `python -m pytest tests/ -q` → **verde**, com total **não menor** que o
     total re-medido no início do despacho. Referência datada de 2026-09-19, fora do literal:
     `tests/test_backlog.py` com 49 testes e a suíte inteira com 201 testes.
  6. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/DIARIO_DE_OBRAS.md -Pattern '^- \*\*Status:\*\* `' | Measure-Object).Count"
     ```
     → **13**, um por item da tabela da §2.1a. **Medido antes: 0** — nenhuma linha de campo `Status`
     canônica existe no diário hoje, e a única que se parece com uma (`docs/DIARIO_DE_OBRAS.md:1284`)
     não casa a âncora `^- `, que é exatamente por que o instrumento não a lê. O valor conta linha
     que **este** card escreve, e nenhuma outra entrega o desloca.
  7. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/DIARIO_DE_OBRAS.md -Pattern '^\| TK-54 \|.*\|$' | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. O padrão exige que a linha do `TK-54` **feche** em `|`; hoje ela
     carrega prosa depois do pipe final e é a única das 32 linhas do índice que o parser não lê.
     Nenhuma violação de `check` cobre este caso, e é por isso que ele tem linha própria de aceite.
  8. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/DIARIO_DE_OBRAS.md -Pattern '^\| TK-54 \|[^|]*\| ready \|' | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. Mede a célula 3 do `TK-54` em **token puro**, que é o defeito do
     `AE-23`: a linha fechar em `|` (item 7) **não basta**, porque restaurar o parse é o que faz a
     narrativa da célula virar `C-4`. Valor rodado nos dois mundos na simulação do `ESC-4a`:
     **1** na cópia migrada, **0** na árvore de hoje.
  9. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/DIARIO_DE_OBRAS.md -Pattern '^### TK-51a ' | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0** — hoje o cabeçalho é `### TK-51`, com o id do pai, e mede **1**
     contra o padrão `^### TK-51 ` (que passa a **0** depois da entrega). O par separa *renomeado*
     de *ainda com o id do pai*.
  10. ```
     pwsh -NoProfile -Command "(git status --short -- docs/DIARIO_HISTORICO.md docs/plans/P-0733-divida-do-hub.md docs/plans/P-0734-execucao-autonoma.md | Measure-Object).Count"
     ```
     → **0**, **invariante**. **Medido antes: 0**. É a linha que prova a `DB-46` pelo lado do que
     **não** foi tocado: a narrativa das células terminais fica onde está, e nenhuma delas viaja
     para o histórico nem para corpo de plano fechado. Valor maior significa que o passo 11 tratou
     célula terminal como viva — o defeito que o `AE-21` mediu.
  11. ```
     pwsh -NoProfile -Command "(git status --short -- .claude/tools/backlog.py tests/test_backlog.py docs/DIARIO_DE_OBRAS.md docs/plans/P-0735-residencia-e-ponto-de-carga.md docs/plans/P-0737-loop-autonomo.md docs/plans/P-0738-contexto-esgotado.md | Measure-Object).Count"
     ```
     → **6**, uma linha por caminho. **Medido antes: 0**. Recorte por pathspec porque a
     árvore de trabalho carrega registro de orquestração alheio a esta tarefa (`DB-29`).
- **Pronto quando:** os onze itens de `Verificação` dão o resultado descrito; `check` sai exit 0 com
  o diário migrado e os três cabeçalhos de plano reconciliados; os treze itens da tabela da §2.1a
  têm a linha `- **Status:**` com o valor que a tabela fixa; as seis células terminais do passo 12
  seguem **intactas**; e nenhum texto do diário foi apagado — toda narrativa retirada de célula de
  índice viva, os três blocos de fila do passo 10 e a prosa que vinha depois do pipe final da linha
  do `TK-54` estão, verbatim, nas seções nomeadas.
- **Fora do escopo desta tarefa:** o verbo `drain` — `BKL-T10a` (`DB-44`); o hook e o ponto de
  carga, e as skills que passam a invocar o instrumento — `BKL-T11`; a aferição do pickup e a
  revisão do `README.md` — `BKL-T12`. Fica fora também, sem card e por decisão do `ESC-1` registrada
  no `AE-16`, a guarda de saída de corpus para plano vivo cuja célula de índice seja marcada
  terminal por engano.

### BKL-T10b — O bloco gerado da §2.3 é projetado inteiro e dentro do corpus [Sonnet · esforço medium · classe implementacao]
- **Status:** `done` · 2026-09-20 — **aprovada 100%**, bloqueante `nenhuma`, sete dimensões `conforme`, recomendação `seguir`, pendência do laudo `nenhuma`. RDO: `docs/RDO/P-0739-BKL-T10b-o-bloco-gerado-da-2-3-e-projetado-inteiro-e-dentro-do-corpus.md`; laudo consumido e apagado (`DP-H`). Fechada em **1 despacho**, **0 retentativas gastas**. As **três** metades do `AE-27` morreram, cada uma com o seu teste — inclusive a terceira, que a pendência não nomeava e a simulação do `ESC-6` achou (bloco emitia 15 bullets de plano, 14 fora do corpus). `backlog.py check` segue **exit 0** e a linha `Fila corrente` sobrevive ao verbo. **`status` e `start` voltam a ser seguros** contra o diário vivo. Ressalva do reviewer, com rota e sem rebaixar: a residência única do passo 4 garante a **residência**, não a **permanência** dela — nenhum teste falha se um terceiro escritor reimplementar a regeneração; o `BKL-T10a` deve declarar que o `drain` chama `_regenerar_bloco_fila`, ponto em que o teste encadeado deixa de ser redundante.
- **Esforço:** medium
- **Objetivo:** `_bloco_fila_corrente` passa a produzir o bloco da §2.3 **inteiro** — a linha
  `**Fila corrente:**` **mais** os bullets — e a enxergar o mesmo corpus que `check` e `next`
  enxergam, de modo que **todo verbo de escrita do instrumento possa correr contra o diário vivo
  sem destruir nem sujar o bloco**. Um ato, uma proposição.
- **Depende de:** `BKL-T10`. Decisões: `DB-48` (as três metades e a residência única do bloco),
  `DB-33` (um bullet por pai vivo, uma forma por tipo de pai), `DB-36` (fórmula do
  `<done>/<total>`), `DB-43` (corpus derivado do índice, e a regra de sufixo como residência única
  do casamento plano × linha de índice), `DB-2` (fonte única), `DB-1` (escrita atômica num ato).
  Fatos: §2.0, §2.3, §2.6 e §3 deste plano.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
- **Passos:**
  1. **Metade 1 — a linha `**Fila corrente:**` é parte do bloco gerado.** `_bloco_fila_corrente`
     (`.claude/tools/backlog.py:1029`) devolve hoje **só** os bullets, e o escritor substitui
     **tudo** entre os marcadores por esse retorno
     (`.claude/tools/backlog.py:1173`, `diario_linhas[ini + 1 : fim] = _bloco_fila_corrente(...)`).
     A função passa a devolver, como **primeiro** elemento, a linha `**Fila corrente:**` na forma
     fixa da §2.3 — `` `<ID>` `` — `<título>` (`<arquivo>:<l1>-<l2>`) · `fila: …` · `ready <n>` ·
     `blocked <m>` · `in-progress <k>` —, composta com as funções que já existem
     (`selecionar_next`, `_residencia_plano`, `_residencia_tiquete`, `_listar_blocked`). Sem
     vencedor, a linha declara o motivo em vez de sumir.
  2. **Metade 2 — o casamento de id de plano é o da residência única.** O laço de
     `_bloco_fila_corrente` casa `plano.id == linha_idx.id`, igualdade exata, e por isso **nenhum**
     plano jamais recebe bullet: o índice publica `P-0739-BKL` e o cabeçalho do arquivo declara
     `P-0739`. Passa a usar a regra de `_posicao_indice` (`.claude/tools/backlog.py:634`) — *id
     exato vence; na falta dele, a primeira linha cujo id seja `<id do plano>-<SUFIXO>`* —, sem
     reescrevê-la num segundo lugar (`DB-2`).
  3. **Metade 3 — o bloco enxerga o corpus.** *Pai vivo* da §2.3 é pai **em corpus** (§2.0): plano
     cuja célula de índice tem núcleo terminal não produz bullet, e não entra nas contagens
     `ready`/`blocked`/`in-progress` da linha da metade 1. `check` e `_candidatos` ganharam esse
     filtro na `BKL-T10`; `_bloco_fila_corrente` **não** ganhou, e é a terceira metade da mesma
     divergência. Medida de 2026-09-20 em cópia, fora do literal: sem este passo, as metades 1 e 2
     sozinhas emitem **15** bullets de plano, **14** deles de plano fora do corpus — cinco arquivos
     declarando o mesmo `P-0729`, e vários com `Status` ausente saindo como `` (`None`, 0/n) ``.
     Com o passo, o bloco sai com **2** bullets: `P-0739` e `TK-54`.
  4. **Residência única do bloco (`DB-2`).** A regeneração do trecho entre `<!-- fila:gerada -->` e
     `<!-- /fila:gerada -->` vira **uma** função, chamada por `transacionar_status` e por
     `transacionar_diretiva`. Medido em 2026-09-20: `transacionar_diretiva`
     (`.claude/tools/backlog.py:1197`) **não** regenera o bloco hoje, contra a §2.3 (*"tudo entre os
     marcadores é reescrito a cada verbo de escrita"*) — divergência que hoje protege por acidente e
     amanhã diverge por desenho. Os dois marcadores continuam localizados por **igualdade exata de
     linha**, e o comportamento de marcador ausente ou de fechamento ausente **não muda**.
  5. **Os testes.** Escrever em `tests/test_backlog.py` os três TF e o TR do campo `Testes`, todos
     sobre cópia de fixture em `tmp_path`.
- **Restrições desta tarefa (copiadas inline; nenhuma vale por ponteiro):**
  - **Forma do bloco (§2.3):** primeira linha `**Fila corrente:**` na forma fixa; depois **um
    bullet por pai vivo**, na ordem das linhas do índice; o pai plano escreve o token `` `P-NNNN` ``
    e o pai tíquete escreve `` `TK-<n>` ``; pai sem filho elegível escreve `próxima —`. Tudo entre
    os marcadores é gerado, e humano não edita ali.
  - **Corpus (§2.0, `DB-43`):** a autoridade sobre a vida de um plano é a célula de estado da linha
    dele no índice; núcleo `done`/`superseded`/`cancelled` → fora do corpus, e o que está fora do
    corpus não vira bullet nem entra em contagem.
  - **Casamento plano × linha de índice (§2.2, `DB-43`):** residência única em `_posicao_indice`.
    Nenhum outro ponto do módulo reescreve essa regra — esta tarefa **remove** a segunda cópia dela,
    não acrescenta uma terceira.
  - **`<done>/<total>` (`DB-36`):** `<total>` = filhos diretos cujo `Status` não é `cancelled`;
    `<done>` = os que estão `done`. A fórmula **não muda** nesta tarefa.
  - **Escrita atômica (`DB-1`):** o verbo de escrita segue escrevendo num ato só, e segue sem tocar
    arquivo quando recusa (`DB-37`).
- **Não fazer:**
  - Não rodar `status`, `start` nem `diretiva` contra `docs/DIARIO_DE_OBRAS.md` real: os TF rodam
    sobre cópia de fixture em `tmp_path`. É a razão de ser desta tarefa, e vale **durante** ela.
  - Não editar `docs/DIARIO_DE_OBRAS.md`, `docs/DIARIO_HISTORICO.md` nem a linha de diretiva.
  - Não mudar a §2.3, a §2.0 nem decisão nenhuma: a forma do bloco e a regra de corpus já estão
    fixadas, e esta tarefa faz o código alcançá-las.
  - Não implementar o verbo `drain` (`BKL-T10a`), o hook nem as skills (`BKL-T11`).
  - Não editar as seções `## 1`, `## 2` e `## 3` de `docs/plans/P-0739-backlog-instrumento.md`, nem
    card nenhum deste plano.
- **Contingências:**
  - se a composição da linha da metade 1 exigir dado que nenhuma função existente devolve → usar o
    que existe e declarar na linha de retorno o campo omitido, sem inventar função nova de coleta;
  - se um TF exigir fixture com plano cujo id se repete em dois arquivos → criá-la, porque é o caso
    real medido (`P-0729` em cinco arquivos) e é o que separa a metade 3 da metade 2;
  - se `transacionar_diretiva` não puder chamar a função única sem mudar a assinatura pública dela →
    manter a assinatura, extrair a regeneração para função interna e chamá-la dos dois pontos.
- **Testes** (`tests/test_backlog.py`, todos sobre cópia de fixture em `tmp_path`):
  - `test_tf_bloco_fila_preserva_linha_fila_corrente` — diário de fixture com o bloco completo
    (linha `**Fila corrente:**` + bullets) entre os marcadores; depois de um `status`, a linha
    `**Fila corrente:**` **continua** entre os marcadores e foi **regenerada** (o `<ID>` nela
    acompanha a transição). Hoje ela desaparece: é o defeito do `AE-27`, medido em cópia.
  - `test_tf_bloco_fila_casa_plano_por_sufixo` — índice com a linha `P-0777-XYZ` e um plano cujo
    cabeçalho declara `P-0777`, com filho não terminal: o bloco traz o bullet `` - `P-0777` ``. A
    regra concorrente (igualdade exata) **não** emitiria bullet nenhum, e é isso que a fixture
    separa.
  - `test_tf_bloco_fila_respeita_corpus` — dois planos com filho não terminal, um com célula de
    índice `ready` e outro com célula `superseded`: só o primeiro vira bullet, e só os filhos dele
    entram nas contagens da linha `**Fila corrente:**`. A regra concorrente (todo plano do
    diretório) emitiria os **dois**.
  - `test_tr_bloco_fila_nao_cresce_com_plano_terminal` — acrescentar à fixture um plano terminal a
    mais **não** muda o bloco, linha por linha.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/tools/backlog.py -Pattern 'if plano.id == linha_idx.id' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 1**. É o literal da segunda cópia da regra de casamento, recortado da
     fonte; zerá-lo prova que a residência única do `_posicao_indice` passou a valer também aqui.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path tests/test_backlog.py -Pattern 'def test_tf_bloco_fila_','def test_tr_bloco_fila_' | Measure-Object).Count"
     ```
     → **4**, um por teste do campo `Testes`. **Medido antes: 0**. O recorte casa só nome de teste
     que **este** card cria, e é invariante ao que outras entregas movem.
  3. ```
     python -m pytest tests/test_backlog.py -q -k bloco_fila
     ```
     → **4** selecionados e **verdes**. **Medido antes: 0 selecionados** — referência datada de
     2026-09-20, fora do literal: 56 testes no módulo, todos desselecionados. O par com o item 2
     separa *teste escrito* de *teste que passa*.
  4. ```
     python -m pytest tests/ -q
     ```
     → **verde**, com total **não menor** que o total re-medido no início deste despacho, e igual a
     ele **mais os quatro** testes do campo `Testes`. Referência datada de 2026-09-20, fora do
     literal: `tests/test_backlog.py` com 56 testes e a suíte inteira com 208.
- **Pronto quando:** os quatro itens de `Verificação` dão o resultado descrito; os quatro testes do
  campo `Testes` exercem, cada um, **uma** das três metades e o invariante; a regeneração do bloco
  mora em **uma** função, chamada por `transacionar_status` e por `transacionar_diretiva`; e
  `docs/DIARIO_DE_OBRAS.md` real **não** foi tocado por esta tarefa.
- **Fora do escopo desta tarefa:** o verbo `drain` — `BKL-T10a`, que executa **depois** desta; o
  hook, o ponto de carga e as skills — `BKL-T11`; a aferição e o `README.md` — `BKL-T12`. Fica fora
  também, e é ato de quem conduz o loop e não desta tarefa, a **atualização da linha de diretiva**,
  hoje priorizando `TK-54a`, que está `done` (`AE-28`).

### BKL-T10a — `drain`: o inbox de planos sai do contexto [Sonnet · esforço medium · classe implementacao]
- **Status:** `done` · 2026-09-20
- **Esforço:** medium
- **Objetivo:** o instrumento ganha o verbo `drain` — cada linha viva de `docs/plans/_INBOX.md` vira
  linha de índice do diário e sai do inbox **verbatim** para o histórico, e o contador de id é
  recalculado —, com os seis testes que o exercem. Um ato, uma proposição: **o inbox deixa de ser
  lido à mão no pickup**.
- **Depende de:** `BKL-T10b`. Decisões: `DB-44` (esta partição), `DB-48` (o bloco gerado é projetado inteiro — o `drain` escreve no diário e herda o bloco reparado), `DB-38` (gramática de linha viva do
  inbox de planos), `DB-9` (o histórico só recebe apenso e nunca é lido), `DB-1` (escrita atômica,
  funções recebem caminhos resolvidos), `DB-37` (exit 3 não toca arquivo nenhum). Fatos: §2.2 (forma
  da linha de índice e da célula de estado), §2.4 e §3 deste plano.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
- **Passos:**
  1. Acrescentar o subcomando `drain [--data AAAA-MM-DD]` ao `main`
     (`.claude/tools/backlog.py:1168`), ao lado de `check`, `show`, `next`, `status`, `start` e
     `diretiva`.
  2. Implementar `drain`: cada linha viva de `docs/plans/_INBOX.md` vira uma linha de índice do
     diário — estado lido do campo `**Status:**` do cabeçalho do plano, título da linha 1 do plano,
     âncora igual ao caminho do arquivo — e a linha do inbox é movida **verbatim**, prefixada de
     `- [drenado AAAA-MM-DD] `, para `docs/plans/_INBOX_HISTORICO.md`.
  3. Recalcular o contador `**Próximo id de plano: P-NNNN.**` do inbox como `max(id visto) + 1`.
  4. Sair **exit 3**, nomeando o arquivo e sem tocar arquivo nenhum, quando um plano referido por
     linha viva não tem `**Prefixo das tarefas no diário:**` ou não tem `**Status:**`; inbox sem
     linha viva é no-op com **exit 0**.
  5. Escrever em `tests/test_backlog.py` os cinco TF e o TR do campo `Testes`, todos sobre cópia de
     fixture em `tmp_path`.
- **Restrições desta tarefa (copiadas inline; nenhuma vale por ponteiro):**
  - **Linha viva do inbox de planos (`DB-38`):** começa com `- `, contém um caminho que casa
    `docs/plans/P-[0-9]{4}-<slug>.md` e **não** começa com `- [drenado `. A gramática de marcação do
    inbox de memória (`- ` sem `[promovido]` e sem `[descartado`) vale só para o inbox de memória e
    **nunca** se aplica a este arquivo.
  - **Histórico (`DB-9`):** `docs/plans/_INBOX_HISTORICO.md` só recebe apenso e **nunca é lido** pelo
    instrumento — nem para calcular o contador, nem para decidir se uma linha já foi drenada.
  - **Marca de drenada:** o prefixo é `- [drenado AAAA-MM-DD] ` e a linha drenada **nunca** é viva,
    mesmo trazendo o caminho de um plano.
  - **Célula de estado que `drain` escreve (§2.2):** só o token do vocabulário, opcionalmente
    seguido de `<done>/<total>`. O plano recém-drenado ainda não tem linha de índice, e por isso o
    campo `**Status:**` do cabeçalho dele é a única fonte possível do token — é o caso de
    *bootstrap*, e ele **não** contradiz a `DB-43`: a regra "o índice é a autoridade" pressupõe que
    exista linha de índice, e é esta que a cria.
  - **Escrita atômica (`DB-1`) e exit 3 sem escrita (`DB-37`):** `drain` escreve num ato só; quando
    recusa, não toca arquivo nenhum.
  - **Corpus (`DB-43`):** esta tarefa **não** mexe em corpus, em `check`, em `next`, em `_candidatos`
    nem em `_parse_indice` — o `BKL-T10` já os entregou, e eles são a base sobre a qual esta roda.
- **Não fazer:**
  - Não rodar `drain` contra o `docs/plans/_INBOX.md` real, nem contra o `docs/DIARIO_DE_OBRAS.md`
    real: os TF do verbo rodam sobre cópia de fixture em `tmp_path`. Medida de 2026-09-19, fora do
    literal: o inbox real tem **0** linhas vivas, de modo que o verbo seria inerte contra a árvore —
    o que **não** autoriza rodá-lo, porque a próxima linha apensada muda isso sem aviso.
  - Não editar `docs/DIARIO_DE_OBRAS.md`, nem `docs/plans/_INBOX.md`, nem
    `docs/plans/_INBOX_HISTORICO.md`, nem `docs/DIARIO_HISTORICO.md`.
  - Não reabrir nada do corpus (`BKL-T10`), do hook e das skills (`BKL-T11`) ou da aferição
    (`BKL-T12`).
  - Não editar as seções `## 1`, `## 2` e `## 3` de `docs/plans/P-0739-backlog-instrumento.md`, nem
    card nenhum deste plano.
- **Contingências:**
  - se o `BKL-T10` não tiver entregue a âncora de índice da §2.2 — `check` ainda lintando plano
    terminal — parar e sinalizar `blocked` razão `dependencia`, citando o `BKL-T10`;
  - se a fixture de inbox exigida por um TF não existir em `tests/fixtures/backlog/`, criá-la dentro
    da própria fixture do teste, em `tmp_path`, e seguir: fixture de teste é parte do teste, não
    entregável novo;
  - se `docs/plans/_INBOX.md` real tiver ganhado linha viva entre o despacho e a entrega, **não**
    drenar: registrar na linha de retorno e seguir, porque drenar a árvore real está fora do escopo
    deste card.
- **Testes** (`tests/test_backlog.py`, todos sobre cópia de fixture em `tmp_path`):
  - `test_tf_drain_move_linha_viva` — a linha drenada aparece idêntica (menos o prefixo) no histórico
    e some do inbox; a linha de índice correspondente aparece no diário, com a célula de estado em
    token puro.
  - `test_tf_drain_ignora_linha_ja_drenada` — inbox com uma linha viva, uma já prefixada
    `- [drenado AAAA-MM-DD] ` e uma sem caminho de plano: `drain` move **só** a viva, e o histórico
    cresce em exatamente uma linha. A gramática concorrente — a do inbox de memória, que só olha
    `[promovido]`/`[descartado` — moveria **duas**: é isso que esta fixture separa.
  - `test_tf_drain_inbox_vazio_e_no_op` — exit 0, nenhum arquivo tocado.
  - `test_tf_drain_plano_malformado_sai_exit_3` — plano sem `Prefixo` ou sem `Status`: exit 3, o nome
    do arquivo na mensagem, e **nada** drenado — nem a linha boa que vinha antes dele no mesmo inbox.
  - `test_tf_drain_recalcula_contador` — o contador do inbox passa a `max(id visto) + 1`, com o
    corpus da fixture trazendo um id maior que o do último drenado, para que a regra "`último + 1`" e
    a regra "`max + 1`" divirjam.
  - `test_tr_historico_do_inbox_so_cresce` — depois de `drain`, o histórico contém todas as linhas
    que continha antes.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command "python .claude/tools/backlog.py drain --help *> $null; $LASTEXITCODE"
     ```
     → **0**. **Medido antes: 2** — hoje o `argparse` recusa o subcomando. O valor é o exit code do
     comando, não um total de corpus: nenhuma outra entrega o desloca.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path tests/test_backlog.py -Pattern 'def test_tf_drain_','def test_tr_historico_do_inbox_so_cresce' | Measure-Object).Count"
     ```
     → **6**, um por teste do campo `Testes`. **Medido antes: 0**. O recorte casa só nome de teste
     que **este** card cria: nenhum dos seis testes do `BKL-T10` traz `drain` no nome, e por isso o
     valor é invariante ao que a entrega anterior move.
  3. ```
     python -m pytest tests/test_backlog.py -q -k drain
     ```
     → **5** selecionados e **verdes** — os cinco `test_tf_drain_*`. O TR
     `test_tr_historico_do_inbox_so_cresce` **não casa `-k drain`**, porque o nome dele não
     contém o literal; é exatamente por isso que o item 2 usa **dois** padrões separados, e os
     dois itens medem coisas diferentes de propósito: o 2 conta **seis** testes escritos, o 3
     conta **cinco** testes de `drain` que passam. **Medido antes: 0 selecionados** — referência
     datada de 2026-09-19, fora do literal: 49 testes no módulo, todos desselecionados. O par com
     o item 2 separa *teste escrito* de *teste que passa*. (Número corrigido de **6** para **5**
     em 2026-09-20 pelo `scrum-master`, `AE-30`: contradição interna ao card, não defeito de
     execução — o bloco `Testes` é a especificação e a `Verificação` mede o que ela prescreve.)
  4. ```
     python -m pytest tests/ -q
     ```
     → **verde**, com total **não menor** que o total re-medido no início deste despacho, e igual a
     ele **mais os seis** testes do campo `Testes`. Referência datada de 2026-09-19, antes do
     `BKL-T10`, fora do literal: `tests/test_backlog.py` com 49 testes e a suíte inteira com 201.
- **Pronto quando:** os quatro itens de `Verificação` dão o resultado descrito — item 3 em
  **5**, item 2 em **6**, e a diferença é o TR, por desenho; o verbo `drain`
  existe no `main` e é coberto pelos cinco TF e pelo TR; `docs/plans/_INBOX.md`,
  `docs/plans/_INBOX_HISTORICO.md` e `docs/DIARIO_DE_OBRAS.md` reais continuam **intocados**; e
  nenhum arquivo fora dos dois `Arquivos-alvo` foi modificado por esta tarefa.
- **Fora do escopo desta tarefa:** o corpus do instrumento e a migração do diário — `BKL-T10`,
  entregue antes desta; o hook e as skills — `BKL-T11`; a aferição do pickup e o `README.md` —
  `BKL-T12`.
- **Notas de execução:**
  - 2026-09-20 `done` — Aprovada 100%, bloqueante nenhuma, recomendacao escalar; contingencia 3 acionada (drain real nao executado); pendencia roteada como AE-31

### BKL-T11 — O hook, o ponto de carga e as skills que invocam o instrumento [Sonnet · esforço medium · classe implementacao]
- **Status:** `done` · 2026-09-20
- **Esforço:** medium
- **Objetivo:** o pickup passa a ser servido pelo instrumento — `.claude/tools/backlog_hook.py` novo,
  registrado em `.claude/projecoes.json` e materializado, e as duas skills vivas que conduzem fila
  mandam rodar `backlog.py` em vez de ler diário e inbox à mão.
- **Depende de:** `BKL-T10`
- **Razão da dependência e insumos (`DB-50`; fora da linha acima, que só carrega IDs):** o hook
  injeta a saída de `next` a cada prompt, e por isso o instrumento precisa ter deixado de sair exit 3
  antes. Decisões: `DB-8` (o hook), `DB-26` (um caminho por bullet em `Arquivos-alvo`), `DB-43`
  (corpus). Fatos: §2.6 (forma fixa da saída de `next`), §3 (superfície do instrumento), `AE-13`
  (mapa de herança das superfícies mortas).
- **Arquivos-alvo:**
  - `.claude/tools/backlog_hook.py`
  - `.claude/projecoes.json`
  - `tests/test_backlog.py`
  - `tests/test_materializar.py`
  - `.claude/skills/passagem-de-bastao/SKILL.md`
  - `.claude/skills/scrum-master/SKILL.md`
  - `GOVERNANCA.md`
  - `CHANGELOG.md`
- **Passos:**
  1. Criar `.claude/tools/backlog_hook.py`: lê em stdin o JSON do evento `UserPromptSubmit`, casa o
     gatilho no campo `prompt`, roda a seleção de `next` por **importação** de
     `.claude/tools/backlog.py` — nunca por subprocesso — e escreve em stdout um objeto JSON com a
     chave `hookSpecificOutput`, contendo `hookEventName` igual a `UserPromptSubmit` e
     `additionalContext` igual à saída de `next`.
  2. Fixar o gatilho: o prompt casa quando contém a substring `próximo passo`, sem distinção de
     maiúsculas e minúsculas. Prompt sem o gatilho → stdout vazio e **exit 0**.
  3. Fazer exit diferente de 0 em `next` virar o texto do `additionalContext`: o hook sai **exit 0**
     em todos os casos e nunca bloqueia o prompt.
  4. Registrar o hook em `.claude/projecoes.json`, no alvo `projeto`, sob a chave
     `hooks.UserPromptSubmit`, com o comando `python {KIT_ROOT}/tools/backlog_hook.py`, na mesma
     forma dos dois hooks já registrados nesse alvo.
  5. Rodar `python .claude/tools/materializar.py apply`.
  6. Em `.claude/skills/passagem-de-bastao/SKILL.md`, três atos — e **nenhum deles cria ponteiro
     novo para seção de plano** (`DB-51`):
     - **(a) `## Parte 1 — Apurar a fila`, item 2 e a heurística padrão que o segue** (linhas
       38-… na árvore de 2026-09-20): a prosa de ordenação **sai** e o texto passa a ser, no
       sentido, este — *apurar a fila é rodar o instrumento:
       `python .claude/tools/backlog.py next` devolve a próxima tarefa e o dossiê dela; a ordem de
       seleção não se reproduz aqui e não se lê antes de rodar, porque é comportamento do
       instrumento. Quando `next` recusa, ele **nomeia a condição** — `E-1` dois ou mais
       `in-progress`, `E-2` linha de status ausente, `E-3` linha de índice ausente — e o que se faz
       é corrigir o dado que ele nomeou, nunca escolher à mão.* A skill **não** ganha ponteiro para
       §2.5: essa seção é comportamento de `next`, e a residência dela é o código.
     - **(b) `## Parte 1`, item 1.1 — o inbox de planos** (linha 27 na árvore de 2026-09-20), que
       hoje manda drenar *"skill `diario-de-obras`, operação drenar inbox de planos"*: passa a
       mandar rodar `python .claude/tools/backlog.py drain`, um ato, que promove cada linha viva de
       `docs/plans/_INBOX.md` ao índice do diário e a move para `docs/plans/_INBOX_HISTORICO.md`. O
       `Objetivo` deste card nomeia o inbox e o passo não o cobria — lacuna fechada aqui. **O item
       1.2, a fila de candidatos a memória, não muda**: continua sendo apresentada ao dono, porque
       promover memória é ato dele.
     - **(c) `## Parte 3 — Fechar a tarefa`, item 2**: passa a mandar rodar
       `python .claude/tools/backlog.py status <ID> <estado>`, preservando a fronteira que o item já
       declara — quem materializa status é a orquestração, e o executor é autor apenas de `review` e
       `blocked`.
  7. Em `.claude/skills/scrum-master/SKILL.md`, fazer o `### Passo 2 — Seleção da próxima tarefa do
     plano` mandar rodar `python .claude/tools/backlog.py next` e o `### Passo 9 — Arquivamento`
     mandar rodar `python .claude/tools/backlog.py status <ID> <estado>`.
  8. Em `GOVERNANCA.md:480`, no bullet cujo rótulo é `**Retomada sem tarefa nomeada**`, acrescentar
     **uma** frase apontando `python .claude/tools/backlog.py next` como o caminho da retomada.
  9. Em `CHANGELOG.md:17`, acrescentar **uma** linha sob `## [Não lançado]` nomeando
     `.claude/tools/backlog_hook.py`.
  10. Escrever em `tests/test_backlog.py` os quatro TF do campo `Testes`.
- **Restrições desta tarefa (copiadas inline; nenhuma vale por ponteiro):**
  - **O hook nunca bloqueia o prompt:** qualquer falha — exit 3 de `next`, exceção, diário ausente —
    vira texto em `additionalContext`, e o processo sai 0.
  - **Sem subprocesso:** a seleção roda por importação do módulo `backlog`, para que o custo do hook
    seja o de uma chamada de função.
  - **Uma frase em `GOVERNANCA.md` e uma linha em `CHANGELOG.md`** — uma ocorrência de cada, nem mais
    nem menos, porque os itens 7 e 8 da `Verificação` afirmam o número 1.
  - **Ponteiro para seção de plano não se cria (`DB-51`):** §2.5 e §2.6 são comportamento de `next`,
    e a residência delas é `.claude/tools/backlog.py`. A skill `diario-de-obras` transcreve §2.1–§2.4
    e §2.7 — a gramática dos **documentos** — e exclui §2.5/§2.6 **por desenho**
    (`.claude/skills/diario-de-obras/SKILL.md:132`). Onde a prosa antiga explicava a ordenação, o
    texto novo manda **rodar o verbo**; não reaponta para lugar nenhum.
  - **As duas superfícies aposentadas não voltam:** as skills `proximo-passo` e `handover` foram
    removidas da árvore pela `LM-T4` do `P-0740`; a herdeira da matéria é
    `.claude/skills/passagem-de-bastao/SKILL.md`, com o `scrum-master` ficando com a condução do loop
    (`AE-13`). Card que nomeasse caminho morto bloquearia no despacho.
  - **Nenhum número de aceite se copia da `BKL-T8`:** o *≥ 3 arquivos* dela é referência datada de
    2026-09-15. A relação transcrita é *toda skill que invoca o instrumento o cita*, e o item 4 da
    `Verificação` a mede sobre os dois alvos declarados deste card.
  - **Piso de regressão como relação:** a entrega soma os `<N>` testes novos e **não reduz** o total
    de `python -m pytest tests/ -q` re-medido no próprio despacho. Referência datada de 2026-09-19:
    suíte inteira com 201 testes.
- **Não fazer:**
  - Não editar `README.md` — é do `BKL-T12`.
  - Não editar `docs/DIARIO_DE_OBRAS.md` — o kanban é do `scrum-master`.
  - Não editar `.claude/tools/backlog.py` — o instrumento fecha no `BKL-T10`.
  - Não editar `.claude/skills/diario-de-obras/SKILL.md`: a gramática já está publicada lá pela
    `BKL-T1`, e é para ela que as duas skills apontam.
  - Não editar as seções `## 1`, `## 2` e `## 3` de `docs/plans/P-0739-backlog-instrumento.md`, nem
    card nenhum deste plano.
- **Contingências:**
  - se `python .claude/tools/materializar.py apply` fizer `tests/test_materializar.py` falhar por
    causa da fixture de projeções → seguir com o ajuste da fixture no mesmo ato e devolver, na linha
    de retorno da entrega, `contingência 1 acionada: fixture de projeções ajustada em tests/test_materializar.py`;
  - se `python .claude/tools/backlog.py next` sair diferente de 0 na árvore real → seguir: é
    exatamente o caso que o passo 3 manda transformar em texto de contexto;
  - se `.claude/projecoes.json` não tiver a chave `hooks` no alvo `projeto` → parar e sinalizar
    `blocked` razão `premissa`;
  - se o guarda do item 10 da `Verificação` sair diferente de 0 depois da entrega → parar e sinalizar
    `blocked` razão `premissa`, colando a linha de saída do guarda.
- **Testes** (`tests/test_backlog.py`):
  - `test_tf_hook_com_gatilho_devolve_additional_context` — stdin com um JSON cujo campo `prompt` é
    `execute o próximo passo` produz stdout com a chave `additionalContext` preenchida e exit 0.
  - `test_tf_hook_sem_gatilho_e_silencio` — stdin com um JSON cujo campo `prompt` é `bom dia` produz
    stdout **vazio** e exit 0. Este é o par do teste acima: a implementação que sempre injeta
    contexto passa no primeiro e falha neste.
  - `test_tf_hook_exit_3_de_next_vira_contexto` — com um repositório de fixture que força exit 3, o
    hook sai **0** e o texto do erro aparece dentro de `additionalContext`.
  - `test_tf_hook_gatilho_ignora_caixa` — stdin com um JSON cujo campo `prompt` é
    `Execute o PRÓXIMO PASSO` casa o gatilho.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command "Test-Path .claude/tools/backlog_hook.py"
     ```
     → **True**. **Medido antes: False**.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/projecoes.json -Pattern 'backlog_hook.py' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. O literal é `backlog_hook.py` e não `UserPromptSubmit`: este
     último já aparece 3 vezes no arquivo hoje e mediria igual nos dois mundos.
  3. ```
     pwsh -NoProfile -Command "python .claude/tools/materializar.py drift > $null 2>&1; $LASTEXITCODE"
     ```
     → **0**, invariante. **Medido antes: 0**. O que este item afirma é que o registro novo foi
     materializado: sem o `apply` do passo 5, o `drift` passa a acusar diferença.
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/passagem-de-bastao/SKILL.md,.claude/skills/scrum-master/SKILL.md -Pattern 'backlog.py' -SimpleMatch | Select-Object -ExpandProperty Path -Unique | Measure-Object).Count"
     ```
     → **2**. **Medido antes: 0**. O recorte é pelos dois alvos declarados, e não pela pasta
     `.claude/skills/` inteira: hoje `.claude/skills/diario-de-obras/SKILL.md` já cita o instrumento,
     e a contagem da pasta mediria 1 antes e 3 depois, movida por entrega alheia.
  5. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/passagem-de-bastao/SKILL.md -Pattern 'backlog.py next' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. Mede o ato (a) do passo 6 na skill de condução — o verbo
     nomeado, e não o arquivo citado, que é o que o item 4 já cobre.
  6. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/passagem-de-bastao/SKILL.md -Pattern 'backlog.py drain' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. Mede o ato (b) — a lacuna do inbox, que o passo não cobria antes
     da `DB-51`. O par com o item 5 separa *a fila* de *o inbox*, que são as duas metades do
     `Objetivo`.
  7. ```
     pwsh -NoProfile -Command "(Select-String -Path GOVERNANCA.md -Pattern 'backlog.py next' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. O literal inclui o verbo porque `backlog.py` sozinho já aparece 2
     vezes em `GOVERNANCA.md` hoje.
  8. ```
     pwsh -NoProfile -Command "(Select-String -Path CHANGELOG.md -Pattern 'backlog_hook.py' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  9. ```
     python -m pytest tests/test_backlog.py -q
     ```
     → **verde**. **Medido antes: verde**. O que discrimina não é o veredito, e sim a relação: o
     total sai do total re-medido no início do despacho **mais** os quatro TF novos do campo
     `Testes`. Em seguida `python -m pytest tests/test_materializar.py -q` → **verde**, e
     `python -m pytest tests/ -q` → **verde**, com total **não menor** que o total re-medido no
     início do despacho. Referência datada de **2026-09-20**, fora do literal: suíte inteira com
     **218** testes — o literal anterior (201, de 2026-09-19) envelheceu com as entregas do
     `BKL-T10`, `BKL-T10b` e `BKL-T10a`, e foi re-medido no `ESC-8`.
  10. ```
     pwsh -NoProfile -Command "pwsh -NoProfile -File .claude/checks/check-readme.ps1 > $null 2>&1; $LASTEXITCODE"
     ```
     → **0**, invariante. **Medido antes: 0**. Esta tarefa não toca `README.md`, e o guarda tem de
     continuar verde depois de as duas skills mudarem.
- **Pronto quando:** os dez itens de `Verificação` dão o resultado descrito; nenhuma das duas skills
  alvo manda mais o agente ler diário ou inbox para achar ou fechar tarefa, e nenhuma delas ganhou
  ponteiro novo para seção de plano (`DB-51`); e o hook devolve
  `additionalContext` para prompt com gatilho e stdout vazio para prompt sem gatilho.
- **Fora do escopo desta tarefa:** a aferição do pickup e a revisão do `README.md` — `BKL-T12`. Fica
  fora, e não se transcreve, o apenso que a `BKL-T8` previa em `docs/plans/P-0737-loop-autonomo.md`
  `## 9`: o plano está `superseded` desde 2026-09-18 e a `DB-15`, como a `DB-43` a emendou, autoriza
  mudar em plano fechado **apenas** a linha do campo `**Status:**` do cabeçalho — linha que o
  `BKL-T10` já reconcilia.
- **Notas de execução:**
  - 2026-09-20 `done` — Aprovada com ressalva 91%, bloqueante nenhuma, recomendacao escalar; pendencia do hook em cp1252 roteada como AE-35/ESC-9

### BKL-T11a — O hook fala no ponto de carga real: `stdin` em UTF-8 explícito e gatilho normalizado [Sonnet · esforço low · classe implementacao]
- **Status:** `done` · 2026-09-20
- **Esforço:** low
- **Objetivo:** `python .claude/tools/backlog_hook.py`, rodado como **executável** com o payload de
  `UserPromptSubmit` em UTF-8 na entrada padrão, devolve `additionalContext` — hoje devolve **0
  bytes** —, e um teste passa a exercer **o processo**, não só o módulo importado. Um ato, uma
  proposição.
- **Depende de:** `BKL-T11`
- **Razão da dependência e insumos (`DB-50`):** o hook nasceu na `BKL-T11`, e é o executável dela
  que esta tarefa conserta. Decisões: `DB-52` (as duas metades e a residência do reparo), `DB-8` (o
  hook), `DB-1` (o instrumento é stdlib). Fato: `AE-35`, e o precedente
  `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, cujo `_norm` é a referência da segunda
  metade — **e cuja primeira metade não existe**, medido no `ESC-9`.
- **Arquivos-alvo:**
  - `.claude/tools/backlog_hook.py`
  - `tests/test_backlog.py`
- **Passos:**
  1. **Metade 1, e é ela que carrega o peso — ler `stdin` como bytes e decodificar UTF-8
     explicitamente.** Em `main` (`.claude/tools/backlog_hook.py:72`), trocar `sys.stdin.read()` por
     leitura de `sys.stdin.buffer` com `.decode("utf-8", errors="replace")`, mantendo o
     `try/except` que já existe e o contrato de **exit 0 sempre**. Razão medida em 2026-09-20, fora
     do literal: num host sem `PYTHONUTF8`, `sys.stdin.read()` decodifica em `cp1252` e o payload
     UTF-8 chega como `execute o prÃ³ximo passo`; o mesmo payload com `PYTHONUTF8=1` devolve
     **6.997** bytes de `additionalContext`, e sem ele, **0**.
  2. **Metade 2 — normalizar a comparação do gatilho, e escrever o literal sem acento.**
     `_casa_gatilho` (`.claude/tools/backlog_hook.py:32`) passa a comparar sobre texto normalizado —
     minúsculas e acentos removidos por `unicodedata.normalize("NFKD", …)` descartando os
     combinantes, o mesmo `_norm` do precedente —, e `_GATILHO`
     (`.claude/tools/backlog_hook.py:20`) passa a ser o literal **sem acento**, `proximo passo`.
     Isso faz casar tanto `próximo passo` quanto `proximo passo`, que é o que um dono digita sem
     pensar. **Esta metade sozinha não conserta o defeito** — medido no `ESC-9`: o texto
     mis-decodificado normaliza para `execute o pra3ximo passo`, que **não** contém
     `proximo passo`, porque o `³` do `cp1252` decompõe em `3` sob NFKD. Ela entra porque amplia o
     gatilho, não porque salva a metade 1.
  3. **O teste que faltava — exercer o executável.** Escrever em `tests/test_backlog.py` os dois TF
     do campo `Testes`, que rodam
     `subprocess.run([sys.executable, ".claude/tools/backlog_hook.py"], input=<bytes UTF-8>, …)`,
     alimentando **bytes** pela entrada padrão e afirmando sobre os **bytes** da saída. É a
     distinção que deixou o defeito passar: os TF da `BKL-T11` alimentam `processar` por importação,
     com a string já decodificada em memória, e nunca tocam o `sys.stdin` de um processo.
  4. **Não mudar mais nada do hook:** `processar`, `_texto_next`, `_carregar_backlog` e o contrato
     de exit 0 ficam como estão — o defeito é de I/O e de comparação, e o `next` que o hook invoca
     funciona.
- **Restrições desta tarefa (copiadas inline; nenhuma vale por ponteiro):**
  - **O hook nunca bloqueia o prompt:** qualquer falha — decodificação, exceção, exit 3 de `next` —
    vira texto em `additionalContext` ou stdout vazio, e o processo sai **0**. O reparo não
    introduz caminho novo de erro: `errors="replace"` nunca levanta.
  - **Sem subprocesso dentro do hook:** a seleção continua rodando por importação de
    `.claude/tools/backlog.py`. O subprocesso aparece **no teste**, que é quem precisa de um
    processo real para exercer `stdin`.
  - **Prompt sem gatilho continua em silêncio:** stdout vazio e exit 0. O par com o teste de gatilho
    é o que separa *injeta sempre* de *injeta quando casa*.
  - **Piso de regressão como relação:** a entrega soma os `<N>` testes novos e **não reduz** o total
    de `python -m pytest tests/ -q` re-medido no próprio despacho. Referência datada de 2026-09-20,
    fora do literal: `tests/test_backlog.py` com 70 testes e a suíte inteira com 222.
- **Não fazer:**
  - Não editar `.claude/tools/backlog.py` — o instrumento fechou no `BKL-T10`/`BKL-T10b`.
  - Não editar `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` nem qualquer outro hook:
    o `ESC-9` mediu que ele tem a **mesma** lacuna, e consertá-lo é matéria de outro plano
    (`AE-36`). Aqui ele é **referência**, não alvo.
  - Não editar `.claude/tools/ocupacao.py` nem `.claude/tools/telemetria_hook.py`, que leem `stdin`
    pelo mesmo padrão — mesma razão.
  - Não editar `README.md`, `docs/DIARIO_DE_OBRAS.md` nem card nenhum deste plano.
  - Não mexer em `.claude/projecoes.json`: o registro do hook já entrou pela `BKL-T11` e
    `materializar.py drift` está em 0.
- **Contingências:**
  - se `sys.stdin.buffer` não existir no ambiente de teste (stdin substituído por objeto sem
    `buffer`) → cair para `sys.stdin.read()` no mesmo `try`, mantendo exit 0, e declarar na linha de
    retorno `contingência 1 acionada: fallback de stdin sem buffer`;
  - se o TF de subprocesso ficar acima de 5 s por carregar o repo real → apontá-lo para uma cópia de
    fixture em `tmp_path` via a variável de ambiente que `resolve_repo` já respeita, e declarar na
    linha de retorno;
  - se o payload de fixture precisar de campo além de `hook_event_name` e `prompt` → acrescentá-lo,
    porque a forma do evento é do harness e não desta tarefa.
- **Testes** (`tests/test_backlog.py`):
  - `test_tf_hook_executavel_stdin_utf8_devolve_contexto` — `subprocess.run` do próprio arquivo
    `.claude/tools/backlog_hook.py`, com `input` igual aos **bytes UTF-8** de um payload cujo
    `prompt` é `execute o próximo passo`: a saída **não é vazia** e traz `additionalContext`. Hoje
    esse mesmo teste mede **0 bytes** — é o defeito do `AE-35`, e nenhum TF existente o expõe porque
    todos entram por importação.
  - `test_tf_hook_executavel_sem_gatilho_e_silencio` — mesmo subprocesso, `prompt` igual a
    `bom dia`: saída **vazia** e exit 0. É o par do teste acima; a implementação que sempre injeta
    passa no primeiro e falha neste.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/tools/backlog_hook.py -Pattern 'sys.stdin.buffer' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. Mede a metade 1 — a que carrega o peso — pelo literal recortado
     da fonte.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/tools/backlog_hook.py -Pattern 'unicodedata' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. Mede a metade 2.
  3. ```
     python -m pytest tests/test_backlog.py -q -k hook_executavel
     ```
     → **2** selecionados e **verdes**. **Medido antes: 0 selecionados** — referência datada de
     2026-09-20, fora do literal: 70 testes no módulo, todos desselecionados. É o item que prova
     que o **executável** passou a ser exercido, e não só o módulo.
  4. ```
     python -m pytest tests/ -q
     ```
     → **verde**, com total **não menor** que o total re-medido no início deste despacho, e igual a
     ele **mais os dois** testes do campo `Testes`. Referência datada de 2026-09-20, fora do
     literal: suíte inteira com 222.
- **Pronto quando:** os quatro itens de `Verificação` dão o resultado descrito; rodado à mão no
  ponto de carga — o executável com o payload UTF-8 na entrada padrão, **sem** `PYTHONUTF8` no
  ambiente —, o hook devolve `additionalContext` não vazio; e prompt sem gatilho continua devolvendo
  stdout vazio com exit 0.
- **Fora do escopo desta tarefa:** a aferição do pickup e a revisão do `README.md` — `BKL-T12`, que
  executa **depois** desta e cuja medida depende deste reparo. Ficam fora, nomeados no `AE-36` e sem
  card: a mesma lacuna em `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, em
  `.claude/tools/ocupacao.py` e em `.claude/tools/telemetria_hook.py`.
- **Notas de execução:**
  - 2026-09-20 `done` — Aprovada com ressalva 91%, bloqueante nenhuma; hook mede 9676 bytes no ponto de carga real sem PYTHONUTF8 (era 0). Pendencia do ambiente do subprocesso roteada como AE-37/ESC-10.

### BKL-T12 — Aferição do pickup e revisão do `README.md` com veredito do dono [Opus + dono · esforço medium · classe redacao]
- **Status:** `done` · 2026-09-20
- **Esforço:** medium
- **Objetivo:** o custo do pickup novo é medido e publicado em `docs/CUSTO_DO_PICKUP.md`, e o
  `README.md` mais o `docs/DOC_MAP.md` passam a descrever o pickup por instrumento — com o veredito
  do dono sobre o espelho (`DB-20`).
- **Depende de:** `BKL-T11a`
- **Razão da dependência e insumos (`DB-50`):** sem o hook no ponto de carga **falando** não há pickup novo para medir — e o hook só passou a falar no `BKL-T11a` (`DB-52`). Decisões:
  `DB-20` (o aceite do dono é parte desta tarefa) e o método `DC-4` de `docs/CUSTO_DO_PICKUP.md`
  (chars da saída do hook numa sessão nova mais o 1º `usage`). Fatos: a `## 3` de
  `docs/CUSTO_DO_PICKUP.md` (77.457 chars do pickup medido) e a `## 6` do mesmo arquivo (alvo de
  40.000 chars).
- **Arquivos-alvo:**
  - `docs/CUSTO_DO_PICKUP.md`
  - `README.md`
  - `docs/DOC_MAP.md`
- **Passos:**
  1. Medir o pickup novo pelo método `DC-4`: chars da saída do hook numa sessão nova, mais o 1º
     `usage` dessa sessão.
  2. Publicar em `docs/CUSTO_DO_PICKUP.md` a seção `## 14 `, de no máximo 30 linhas, com o número
     medido no passo 1 confrontado com os 77.457 chars da `## 3` e com o alvo de 40.000 da `## 6`. O
     número da seção é **14** porque a última seção do arquivo hoje é a `## 13` — medido em
     2026-09-19. A `BKL-T9` dizia `## 15`: número de 2026-09-15, que não se copia.
  3. Em `docs/DOC_MAP.md:104`, dentro da lista `**Seções:**` do bloco `## docs/CUSTO_DO_PICKUP.md`,
     acrescentar a entrada da seção nova imediatamente **depois** da entrada de `## 13`.
  4. Em `README.md`, acrescentar `.claude/tools/backlog.py` e `.claude/tools/backlog_hook.py` à seção
     de ferramentas, e reescrever o §9 do fluxo para descrever o pickup por instrumento.
  5. Rodar `pwsh -NoProfile -File .claude/checks/check-readme.ps1`.
  6. Apresentar o espelho ao dono e registrar o veredito dele (`DB-20`).
- **Restrições desta tarefa (copiadas inline; nenhuma vale por ponteiro):**
  - **Teto da seção nova:** no máximo 30 linhas em `docs/CUSTO_DO_PICKUP.md`, contadas com
    `(Get-Content <arquivo>).Count` sobre o recorte — `Measure-Object -Line` ignora linha vazia e
    erra o número.
  - **Frase que conta item fecha no mesmo ato:** se a seção de ferramentas do `README.md` tiver frase
    que declare o número de ferramentas, ela se atualiza na mesma edição. O
    `.claude/checks/check-readme.ps1` confere as contagens de agentes, skills e guardrails e **não**
    confere essa frase.
  - **O número publicado é o medido no passo 1, nunca estimado:** a seção traz o valor observado numa
    sessão nova, com a data da medida.
  - **O aceite do dono é parte da tarefa** (`DB-20`): a entrega não fecha sem o veredito dele sobre o
    espelho.
- **Não fazer:**
  - Não editar `.claude/tools/`, `.claude/skills/`, `docs/DIARIO_DE_OBRAS.md` nem
    `docs/plans/P-0739-backlog-instrumento.md`.
  - Não renumerar nenhuma seção existente de `docs/CUSTO_DO_PICKUP.md`.
- **Contingências:**
  - se o hook não injetar contexto na sessão nova → parar e sinalizar `blocked` razão `dependencia`,
    nomeando o `BKL-T11`;
  - se `docs/CUSTO_DO_PICKUP.md` já tiver uma seção `## 14 ` → seguir com o próximo número livre de
    seção e devolver, na linha de retorno da entrega,
    `contingência 2 acionada: seção publicada com outro número`;
  - se o guarda do item 4 da `Verificação` sair diferente de 0 → parar e sinalizar `blocked` razão
    `premissa`, colando a linha de saída do guarda;
  - se o dono não der o veredito no mesmo despacho → parar e sinalizar `blocked` razão `dependencia`,
    com os três arquivos já gravados.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/CUSTO_DO_PICKUP.md -Pattern '^## 14 ' | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/DOC_MAP.md -Pattern '## 14 ' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. O par com o item 1 é a conferência contra a fonte: a seção existe
     no documento **e** está indexada no mapa, que é a porta de entrada obrigatória.
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path README.md -Pattern 'backlog_hook.py' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. O literal é o do hook porque o `README.md` de hoje não cita
     nenhum dos dois instrumentos, e o hook é o item que a seção de ferramentas ganha.
  4. ```
     pwsh -NoProfile -Command "pwsh -NoProfile -File .claude/checks/check-readme.ps1 > $null 2>&1; $LASTEXITCODE"
     ```
     → **0**, invariante. **Medido antes: 0**.
  5. ```
     pwsh -NoProfile -Command "(git status --short -- docs/CUSTO_DO_PICKUP.md README.md docs/DOC_MAP.md | Measure-Object).Count"
     ```
     → **3**, uma linha por caminho. **Medido antes: 0**. Recorte por pathspec porque a
     árvore de trabalho carrega registro de orquestração alheio a esta tarefa (`DB-29`).
- **Pronto quando:** os cinco itens de `Verificação` dão o resultado descrito; a seção nova de
  `docs/CUSTO_DO_PICKUP.md` traz o número **medido** do pickup novo contra os 77.457 chars da `## 3`
  e o alvo de 40.000 da `## 6`, em no máximo 30 linhas; e o dono deu o veredito do espelho (`DB-20`).
- **Fora do escopo desta tarefa:** nada deste plano fica depois dela — o `BKL-T12` é a última tarefa
  do `P-0739`.
- **Notas de execução:**
  - 2026-09-20 `review` — Passos 1-5 entregues, aprovada com ressalva 88%, bloqueante nenhuma. Passo 6 (veredito do dono, DB-20) ABERTO: a tarefa nao fecha sem ele. Laudo preservado, RDO nao fechado. Ver AE-40.

### BKL-T5 — `drain`: o inbox sai do contexto [Sonnet · classe implementacao]
- **Status:** `cancelled` · 2026-09-19 · absorvido por `BKL-T10a` (`DB-44`; a atribuição original ao `BKL-T10` foi reatribuída quando o `drain` saiu para card próprio) — corpo preservado verbatim como
  fonte que o módulo cita; razão anterior, preservada: restrições inline e `Pronto quando`
  discriminante autorados pela `RP-6` (2026-09-18) a partir do achado 3 do `AE-7`.
- **Absorvida por:** `BKL-T10a` na retomada (ESC-34/ESC-35; reatribuída do `BKL-T10` para o `BKL-T10a` pela `DB-44`, `ESC-2`)
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
- **Status:** `cancelled` · 2026-09-19 · absorvido por `BKL-T10` — corpo preservado verbatim como fonte que o módulo cita
- **Absorvida por:** `BKL-T10` na retomada (ESC-34/ESC-35)
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
- **Status:** `cancelled` · 2026-09-19 · absorvido por `BKL-T11` — corpo preservado verbatim como fonte que o módulo cita
- **Absorvida por:** `BKL-T11` na retomada (ESC-34/ESC-35)
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
- **Status:** `cancelled` · 2026-09-19 · absorvido por `BKL-T11` — corpo preservado verbatim como fonte que o módulo cita
- **Absorvida por:** `BKL-T11` na retomada (ESC-34/ESC-35)
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
- **Status:** `cancelled` · 2026-09-19 · absorvido por `BKL-T12` — corpo preservado verbatim como fonte que o módulo cita
- **Absorvida por:** `BKL-T12` na retomada (ESC-34/ESC-35)
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
6. **Ato de orquestração, entre o `BKL-T11a` e a `BKL-T12` (`DB-49`, ponto re-fixado pela
   `DB-52`):** o `drain` real passa a ser o **último ato antes da aferição** — depois do reparo do
   hook, e com **nada** entre ele e a `BKL-T12`. A ordem entre `drain` e reparo é indiferente para o
   resultado (o hook mudo não lê corpus nenhum, e o `drain` não toca o hook); o que decide é a
   propriedade que se quer manter: a `## 15` mede o corpus no estado em que ele ficará, sem despacho
   de executor entre a drenagem e a medida.
   `python .claude/tools/backlog.py drain` contra a árvore real, pelo `scrum-master`. É o único
   verbo do instrumento que nunca correu em produção, e a `BKL-T12` mede o pickup **em sessão
   nova** — medir com o inbox por drenar publicaria um número que envelhece no primeiro `drain`.
   Conferência, com os valores apurados em cópia (2026-09-20): **antes**, `_INBOX.md` com 1 linha
   viva e nenhuma linha `P-0741` no índice; **depois**, exit 0 com os três arquivos nomeados na
   saída, a linha
   `| P-0741-MC | O modelo conceitual do plano: a interface entre o dono e o loop | ready | docs/plans/P-0741-modelo-conceitual.md |`
   no índice, `_INBOX.md` sem linha viva, `_INBOX_HISTORICO.md` com uma linha a mais prefixada de
   `- [drenado AAAA-MM-DD] `, `check` exit 0 e o rodapé de `next` em `inbox de planos: 0 por drenar`.
   **Armadilha conferida no mesmo ato, e ela não é do `drain`:** o contador do inbox fica em
   `**Próximo id de plano: P-0742.**` enquanto `docs/plans/P-0742-loop-fora-do-llm.md` **já
   existe** — o `P-0742` nasceu sem linha de inbox, então o `max(id visto) + 1` nunca passou dele.
   `check` não acusa. Corrigir o contador para `P-0743` é ato de quem drena.

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
  execução (`G-REPLAN`). **Encerrado em 2026-09-19 pela `BKL-T9a`:** o reparo `AE-47` **do `P-0740`** pôs em `transacionar_status` a guarda que declara a ausência dos marcadores `<!-- fila:gerada -->` em vez de estourar, e a dependência de ordem que este achado nomeava deixou de existir; a inserção dos marcadores no diário vivo é matéria do `BKL-T10`.
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
  **Reconciliado pelo `AE-13` desta série (2026-09-19, `ESC-36` do `P-0740`):** os números desta
  entrada **envelheceram**, e fecham juntos, não um a um — são **5** tarefas `ready`
  (`BKL-T5`..`BKL-T9`), **11** `done` e **16** no total, medidos no ato, porque a `BKL-T4` fechou em
  2026-09-18 **depois** desta redação; e a reescrita dos cards **não** é mais da `LM-T5`/`LM-T5a` do
  `P-0740`: ela é o **primeiro ato da retomada** deste plano, conforme o `AE-13` abaixo. O texto
  acima fica **literal**, como registro do que se sabia no dia.

- **`AE-13` (2026-09-19) — decisão de reagrupamento (`ESC-34`) e mapa de herança das superfícies
  mortas (`ESC-35`), transcritas sem re-decisão pela `LM-T5a` do `P-0740`.**

  **Identificador, e a regra que a colisão expôs (`ESC-36`):** a série `AE-<n>` é **por plano**.
  Este `AE-13` é da série **deste** arquivo (o `P-0739` ia de `AE-1` a `AE-12`) e **não** tem
  relação com o `AE-13` do `P-0740`, que nomeia achado vivo e diferente — citado **14** vezes
  naquele plano, inclusive em `docs/RUBRICA_DE_REVISAO.md` §3. A escolha da entrega foi correta (o
  próximo livre da série local); o que faltava era a regra escrita: **citação de achado de outro
  plano leva sempre o qualificador** — `AE-<n>` **do** `<plano>` —, como este arquivo e o `P-0740`
  já fazem em prosa. Nenhum instrumento confere isso hoje; publicar a regra em doutrina do kit é
  matéria **pós-marco**.

  **Partição** (`ESC-34`): três módulos absorvem os cinco cards `ready` — `BKL-T10` (absorve
  `BKL-T5` + `BKL-T6`), `BKL-T11` (absorve `BKL-T7` + `BKL-T8`), `BKL-T12` (absorve `BKL-T9`
  sozinha). Ordem de execução: `BKL-T10` → `BKL-T11` → `BKL-T12`. O `AE-10` encerra no `BKL-T10`:
  a dependência de ordem que ele nomeava (`transacionar_status` contra os marcadores
  `<!-- fila:gerada -->` ausentes) deixou de existir quando o `AE-47` pôs em `transacionar_status`
  a guarda que declara a ausência dos marcadores em vez de estourar. **A transcrição dos três
  módulos `BKL-T10`..`BKL-T12` é o primeiro ato da retomada deste plano, não desta nota.**

  **Mapa de herança** (`ESC-35`): `passagem-de-bastao` é a **herdeira da matéria** de skill da
  `BKL-T8` — sucessora de `.claude/skills/proximo-passo/SKILL.md` e
  `.claude/skills/handover/SKILL.md`, ambas aposentadas e removidas da árvore pela `LM-T4` do
  `P-0740` —, com `scrum-master` recebendo a parte de condução do loop. Isto **ratifica** o que a
  `LM-T4` já fez (ela criou a skill nova com o mesmo conteúdo); não inventa sucessão. O aceite
  herdado da `BKL-T8` — *Grep `backlog.py` em `.claude/skills/` ≥ 3 arquivos* — **não se
  transcreve** como número: a regra que se transcreve é *toda skill que invoca o instrumento o
  cita*, e o número se re-deriva na retomada, sobre a árvore de então.

- **`AE-14` (2026-09-19, abertura da janela de retomada, `scrum-master`) — o primeiro ato da
  retomada estava decidido e nomeado, e não tinha card; e a `Fila corrente` cita autoridade
  errada para o tratamento dos cinco absorvidos.** Duas partes, ambas de forma, nenhuma de rota.

  **(i) A lacuna, e o que ela media.** A `Fila corrente` do `docs/DIARIO_DE_OBRAS.md` nomeia como
  primeira tarefa da janela *"transcrever os três módulos `BKL-T10`..`BKL-T12`"*, e o `AE-13` deste
  arquivo declara que essa transcrição é o primeiro ato da retomada. Nenhum dos dois é card: o
  `## 4` deste plano não tinha heading para ela, e o parser que monta o dossiê no despacho media a
  ausência —
  `python .claude/tools/review_evidence.py --plano docs/plans/P-0739-backlog-instrumento.md --tarefa BKL-T10 --desde HEAD`
  saía **exit 1**, contra **exit 0** de `--tarefa BKL-T5` na mesma árvore. Pelo `G-PLANREADY` a
  janela pararia em `B3` sem entregar nada. **Fechada no ato**, sob o item 3 da *Diretiva de
  execução do `P-0739`* (dono, 2026-09-19): o `scrum-master` autorou o card `RP-8` — rodada de
  transcrição, classe `redacao` (o conjunto fechado do parser não tem `replanejamento`), despachada ao `pantonic-planner` conforme `GOVERNANCA.md`
  §7 item 17 — **sem decidir nada** que o `AE-13` já não tivesse decidido. O que o card acrescenta é
  forma: alvos, restrições, insumos fechados e um bloco `Verificação` que discrimina.

  **(ii) Ponteiro quebrado na `Fila corrente`.** O texto afirma que *"os cinco cards antigos ficam
  no arquivo como `cancelled` por absorção (`DM-33` (iii))"*. O `DM-33` do `P-0740` trata de outra
  coisa — *teste pré-existente que afirma a saída que o card reescreve é alvo da tarefa* —, e
  nenhuma das suas quatro partes fala de absorção de card. A autoridade real do tratamento é o
  `AE-13` deste arquivo, com o produto (c) da `LM-T5a` do `P-0740`, que deixou os cinco `ready` com
  o bullet `- **Absorvida por:**` **porque o plano estava estacionado** e a transcrição era da
  retomada. Chegada a retomada, é a `RP-8` que os move a `cancelled`. Correção aplicada na
  `Fila corrente` no mesmo ato; o achado fica registrado porque a citação errada sobreviveu a uma
  janela inteira sem que nenhum instrumento a flagrasse — **nenhum parser do kit confere
  qualificador de plano em citação cruzada de decisão**, que é a mesma lacuna que o `AE-13` já
  nomeara para a série `AE-<n>`. Matéria **pós-marco**, sem card, e evidência para a spec de
  robustez (`TK-55`), na classe *derivado que erra sem sinal* aberta pelo item 5 da diretiva do
  dono.

  **(iii) A classe `replanejamento` existe na doutrina e não existe no parser.** Medido ao autorar
  o card: `GOVERNANCA.md` §3 lista *Rodada de replanejamento* como item de classe própria, com teto
  **≤50** tool uses; o conjunto fechado que `.claude/tools/rdo.py` aceita no cabeçalho é
  `['comportamental', 'implementacao', 'investigacao', 'mecanica', 'redacao']`, e cabeçalho com
  `classe replanejamento` sai **exit 1** no extrator de dossiê. A `BKL-T9a` saiu, por isso, como
  `classe redacao · teto 50` — a classe que o parser aceita, com o teto que a doutrina prescreve
  para a rodada. Duas residências do mesmo conceito divergindo sem que nada o flagre: mesma família
  do item (ii), e mesma rota — matéria **pós-marco**, sem card, evidência para a spec de robustez
  (`TK-55`).

- **`AE-15` (2026-09-19, `BKL-T9a` devolvida `blocked` razão `premissa` pelo `A3b`) — o aceite
  herdado da `BKL-T6` é insatisfazível no escopo que o próprio card declara, e a transcrição não
  tem como consertá-lo.** Devolução por conduta correta: nenhum arquivo tocado, a medida feita
  antes de escrever qualquer linha (`G-EXECREADY`).

  **Fato medido (2026-09-19, `pantonic-planner`, sobre a árvore em `eb93490`):**
  - `python .claude/tools/backlog.py check` → **exit 1, 309 achados**. Apenas **71** caem nos dois
    `Arquivos-alvo` que a `BKL-T6` declara — `docs/DIARIO_DE_OBRAS.md` (60) e
    `docs/plans/P-0737-loop-autonomo.md` (11). Os outros **238** vivem em planos que o próprio card
    **proíbe tocar**: `P-0734` (68), `P-0730` (23), `P-0729` (21 + 13), `P-0731` (19), `P-0738`
    (18), `P-0733` (15) e outros.
  - `python .claude/tools/backlog.py next` → **exit 3**, exigindo linha `Status` para **~110** IDs
    que residem nesses mesmos planos (`T1`..`T55` em `P-0734`, `CTX-T*` em `P-0738`, `AUT-T*` em
    `P-0737`) — contra os **15** itens que o item (c) da `BKL-T6` enumera.
  - Dos 60 achados do diário, **~34 são falso positivo do instrumento**: `check` lê **qualquer**
    linha de tabela markdown como linha de índice e acusa `C-3`/`C-9` sobre linhas de tabelas
    alheias ao índice. Reais no diário: **3** `C-3` (`TK-23`, `TK-32`, `TK-55`) e **2** `C-9`
    (`P-0733-DHB`, `P-0739-BKL`).

  **Por que isto não é número a re-derivar.** A `BKL-T9a` autoriza re-derivar número de aceite
  sobre a árvore de hoje, e só isso. Aqui as três saídas possíveis são **decisão de escopo ou de
  rota**: (a) ampliar a migração aos planos que o card proíbe tocar; (b) corrigir a âncora de
  índice e a exigência de `Status` em `backlog.py`, o que altera `## 2`/`## 3` deste plano —
  alteração que o card manda bloquear; (c) re-escopar o aceite aos dois alvos declarados, deixando
  `check` vermelho por desenho. Critério (xii)(d) da `RUBRICA_DE_REVISAO.md` §8, mesma classe do
  `AE-4`/`LM-T4` do `P-0740`.

  **Por que a rodada parou inteira, e não só no `BKL-T10`.** Autorar `BKL-T11` e `BKL-T12` sem o
  `BKL-T10` cancelaria `BKL-T5` e `BKL-T6` **sem sucessor**, abrindo vão no plano — o oposto do que
  a partição do `AE-13` existe para fazer.

  **Achado secundário, do mesmo retorno, sobre a `Verificação` da própria `BKL-T9a`:** os itens 3,
  4 e 5 contam **a própria linha de comando** do bloco (`Select-String` sobre o arquivo que contém o
  padrão escrito). Medem hoje **1 / 6 / 7**, e não os `0 / 5 / 5` que o card afirma; os esperados
  verdadeiros pós-entrega seriam **6 / 4 / 7**. Defeito de autoria do `scrum-master`, corrigido no
  mesmo ato do reparo do card. Evidência para a spec de robustez (`TK-55`), classe *derivado que
  erra sem sinal*: nenhum instrumento flagra aceite que conta a si mesmo.

  **Resolvido pela `DB-43` (2026-09-19, `ESC-1`, `pantonic-consultant`).** O texto acima fica
  **literal**. A rota decidida é a **(b) do `AE-15`, generalizada**: o defeito não é a âncora de
  índice nem a exigência de `Status` tomadas isoladamente — é o **corpus**. O instrumento decidia a
  vida de um plano pelo campo `**Status:**` do próprio arquivo, campo que a `DB-15` **proíbe**
  acrescentar a plano fechado; a autoridade passa a ser a célula de estado da linha do índice, e
  plano terminal sai do corpus. Medida do efeito, por simulação no ato: `check` cai de **309** para
  **27** achados, **24** deles em `docs/DIARIO_DE_OBRAS.md` — que **é** alvo declarado — e **3**
  `C-5` de cabeçalho de plano; o outro alvo declarado, `docs/plans/P-0737-loop-autonomo.md`, **cai
  da lista**: o plano está `superseded` desde 2026-09-18 e os `AUT-T1..T10` deixam de ser matéria
  de migração. O aceite herdado da `BKL-T6` volta a ser satisfazível, e a `BKL-T9a` é despachável de
  novo. O achado secundário foi corrigido no mesmo ato: os itens 3, 4 e 5 passaram a forma ancorada
  (`^- **Status:** …`) e a caminho inteiro (`.claude/…/SKILL.md`), que não casam a própria linha de
  comando — medidos **0 / 5 / 6** com a forma nova já escrita no arquivo, contra os 1 / 6 / 7 da
  forma antiga.

### AE-16 — Estatística do acionamento `ESC-1` da retomada (`pantonic-consultant`, 2026-09-19)

Registro na forma que a `docs/consultant-spec.md` §9 prescreve enquanto a residência estruturada não
existe: **prosa, no bloco de achados do plano, um achado por acionamento**, com os três campos.

- **O que motivou:** a `BKL-T9a` — transcrição dos três módulos, primeiro ato da retomada — voltou
  `blocked` razão `premissa` **sem arquivo tocado**, porque o aceite que ela mandava herdar da
  `BKL-T6` (`check` exit 0, `next` verde) é insatisfazível dentro dos `Arquivos-alvo` declarados:
  238 dos 309 achados e ~110 exigências de linha `Status` vivem em planos que o card proíbe tocar.
  O planejador nomeou três saídas e classificou **todas** como decisão de escopo ou de rota.
- **Classe do impedimento:** *contradição entre duas decisões já fechadas do próprio plano* — a
  `DB-15` (plano fechado não recebe campo) contra a regra de corpus que o instrumento implementou
  (plano sem campo é lido como vivo). Não é decisão ausente (`ESC-34`) nem defeito de redação de
  card: as duas decisões existem, publicadas, e **se contradizem no ponto em que o instrumento as
  lê**. Classificado **técnico/tático** — a janela seguiu.
- **O que ficou inconclusivo:**
  - **O plano fora do corpus fica sem guarda de saída.** Se a célula do índice de um plano vivo for
    marcada terminal por engano, ele **desaparece** do corpus em silêncio. O `C-5` de cabeçalho
    (novo alvo da `DB-43`) só cobre o caso em que o plano **tem** campo `Status`; os 14 legados não
    têm, e para eles nenhum confronto existe. Sem rota decidida, e sem card.
  - **A linha de diretiva do diário não casa o parser** (`**Diretiva de priorização (EMERGÊNCIA —
    dono, 2026-09-18):**` contra `**Diretiva de priorização:**`), então `next` corre hoje **sem**
    restrição de diretiva — §2.5 item 1 está inerte na árvore real. Cai dentro da migração da
    `BKL-T6` (a); fica nomeado porque **nenhum verbo acusa** diretiva não-casada, e o `check` não
    tem violação para ela.
  - **O tamanho do `BKL-T10` não foi reaferido.** A `DB-43` tira dele um alvo (`P-0737`) e põe
    matéria nova (reparo de corpus com TF). A partição do `AE-13` fica **intacta** por decisão
    deste acionamento; se a transcrição medir o módulo acima do teto da classe, é achado dela.

**Para a spec de robustez (`TK-55`), classe *derivado que erra sem sinal*, duas evidências deste
acionamento:** (i) **aceite que conta a si mesmo** — três itens de `Verificação` mediam o próprio
bloco de comando e nenhum instrumento do kit flagra isso (mesma classe do achado secundário do
`AE-15`); (ii) **corpus implícito** — `check` varria 20 arquivos enquanto a norma (`F-1`, `DB-15`)
falava de 3, e o único sinal disso foi um número grande de achados, que o operador lê como *dívida*
e não como *defeito de escopo do instrumento*. Nos dois casos o derivado errou **sem emitir sinal de
erro**: exit 1 com 309 achados é a saída de sucesso do verbo.

- **`AE-17` (2026-09-19, pendência do laudo da `BKL-T9a`, roteada pelo `B1`) — o `BKL-T10` nasceu
  acima do teto, e a partição que o gerou está vedada à re-decisão pelo próprio card que o
  escreveu.** A entrega fechou **aprovada 100%**, bloqueante `nenhuma`, sete dimensões `conforme`:
  o achado não rebaixa nada, e por isso não morreu com o laudo.

  **Fato medido (2026-09-19, `pantonic-planner` no 2º despacho, confirmado pelo `pantonic-reviewer`):**
  o `BKL-T10` sai com **20 passos, 6 `Arquivos-alvo` e 12 testes**, cruzando **dois temas** — o
  reparo de corpus no instrumento e a migração dos documentos vivos. Acima do teto **≤40** da
  classe `implementacao` e fora do critério (ii) da `RUBRICA_DE_REVISAO.md` §8, que exige tema
  único.

  **Por que o executor não o desdobrou:** a partição vem do `AE-13`, foi ratificada pelo `ESC-1` e
  a `BKL-T9a` **veda expressamente a re-decisão** — transcrever não é repartir. A conduta foi
  correta nos dois sentidos: manteve a partição e **declarou a medida** em `pendencia=`, em vez de
  decidir por conta própria.

  **Dois efeitos de escopo registrados nos cards pelo mesmo despacho**, ambos consequência da
  `DB-43` e nenhum deles defeito: (i) `docs/plans/P-0737-loop-autonomo.md` permanece nos
  `Arquivos-alvo` do `BKL-T10` **só pela linha `**Status:**` do cabeçalho** — a `DB-43` o nomeia
  entre as três reconciliações de uma linha, e o corpo do plano segue imutável; (ii) o apenso que a
  `BKL-T8` previa em `P-0737` `## 9` foi declarado **fora de escopo** no `BKL-T11`, por ser corpo
  de plano fechado.

  **Rota:** decisão de planejamento, anterior ao despacho do `BKL-T10` — ou o módulo se desdobra,
  ou segue inteiro com o teto declarado no cabeçalho. Escalado ao consultor como `ESC-2`.

  **Resolvido pela `DB-44` (2026-09-19, `ESC-2`, `pantonic-consultant`).** O texto acima fica
  **literal**. Decisão: **desdobra**, e o corte **não** cai onde esta entrada o supôs. Os dois temas
  que ela nomeia — reparo de corpus × migração dos documentos vivos — são **um** tema: nenhum dos
  dois é verificável sozinho contra a árvore real, `check` só fica verde com os dois, e partir ali
  obrigaria o primeiro card a publicar *309 → 27 achados* como aceite — a constante de corpus que os
  critérios (xiii) e (xviii) da `RUBRICA_DE_REVISAO.md` §8 proíbem. O segundo tema é o **`drain`**:
  outra seção da norma (§2.4), outro card de origem (`BKL-T5`), dois arquivos que nem constam dos
  `Arquivos-alvo` do `BKL-T10`, aceite independente, e **0** linhas vivas no inbox real — medido no
  ato —, o que o torna inerte contra a árvore e incapaz de deslocar o `check` verde. Nasce o
  `BKL-T10a`; a ordem passa a `BKL-T10` → `BKL-T10a` → `BKL-T11` → `BKL-T12`. Os dois efeitos de
  escopo do item anterior foram reconferidos e **não mudam**: (i) `P-0737` continua nos
  `Arquivos-alvo` do `BKL-T10` só pela linha `**Status:**` do cabeçalho (bloco C, passo 14), porque
  a reconciliação ficou no `BKL-T10`; (ii) o apenso em `P-0737` `## 9` segue fora de escopo no
  `BKL-T11`, que esta decisão não toca. **Sobre o teto:** a opção *seguir inteiro com o teto
  declarado no cabeçalho* não existe como escrita — `GOVERNANCA.md` §3 diz que a tabela de tetos é a
  **única** residência de número de teto e que **nenhum dossiê de tarefa carrega teto**; e o
  ≤40 nunca foi o motivo da partição, porque cruzar o número da classe é *alarme para quem
  dimensiona, nunca bloqueio*.

### AE-18 — Estatística do acionamento `ESC-2` (`pantonic-consultant`, 2026-09-19)

Mesma residência e mesma forma do `AE-16`, como a `docs/consultant-spec.md` §9 prescreve enquanto a
residência estruturada não existe: prosa, no bloco de achados, um achado por acionamento.

- **O que motivou:** a `BKL-T9a` fechou **aprovada 100%**, e mesmo assim deixou pendência: o
  `BKL-T10` que ela transcreveu nasceu com 20 passos, 6 `Arquivos-alvo`, 12 testes e três atos
  declarados no próprio `Objetivo`. O executor **não** desdobrou — a partição vinha do `AE-13`, o
  `ESC-1` a ratificou e a `BKL-T9a` veda a re-decisão —, mediu e declarou. Acionamento **previsto**:
  é o ponto (3) do inconclusivo do `AE-16` voltando com número, e não uma surpresa.
- **Classe do impedimento:** *dimensionamento diferido* — decisão de planejamento que um
  acionamento anterior deixou **explicitamente** em aberto por falta de medida, e que a entrega
  seguinte mediu. Distinta das duas classes já vistas nesta instância: não é decisão ausente
  (`ESC-34`) nem contradição entre decisões fechadas (`ESC-1`). Classificada **técnico/tático** — a
  doutrina do módulo (`GOVERNANCA.md` §3) e a rubrica (§8) decidem sozinhas: escopo, rota e
  entregáveis do plano não mudam, nenhum ato do dono é requerido, e a fila só ganha uma fronteira
  interna. A janela segue para o despacho do `BKL-T10`.
- **O que ficou inconclusivo:**
  - **O `BKL-T10` continua grande, e ninguém sabe quanto.** Depois do corte ele tem 16 passos, 6
    testes e os mesmos 6 `Arquivos-alvo` — a partição por tema não reduziu o número de alvos, porque
    o `drain` já compartilhava os dois arquivos de código. Se o despacho estourar o ≤40, é **alarme
    para quem dimensiona**, registrado no corpo da tarefa, nunca bloqueio (`GOVERNANCA.md` §3): não
    há segunda partição decidida de antemão, e inventá-la sem medida repetiria o erro que esta
    decisão corrige.
  - **A cauda em prosa da linha `Status` da `BKL-T5` e da `BKL-T10` envelheceu.** As duas dizem
    *absorvido por `BKL-T10`* / *absorve `BKL-T5` e `BKL-T6`*, e a `DB-44` reatribuiu a `BKL-T5` ao
    `BKL-T10a`. O bullet `- **Absorvida por:**` foi corrigido no ato; a linha `Status` **não** — ela
    é materializada por quem conduz o loop, e a correção da cauda fica entregue a ele. Nenhum
    instrumento confere coerência entre a cauda da linha `Status` e o bullet de absorção.
  - **O critério que decidiu não tem instrumento.** A partição saiu de *duas proposições ponta a
    ponta no mesmo card*; nada no kit mede isso. O `card_check` está suspenso em efeito, e mesmo
    ativo ele confere a forma do bloco `Verificação`, não a contagem de proposições.

**Para a spec de robustez (`TK-55`), classe *derivado que erra sem sinal*, uma evidência deste
acionamento:** **entrega aprovada 100% com defeito de dimensionamento dentro.** Sete dimensões
`conforme`, bloqueante `nenhuma`, e ainda assim o produto saiu fora do critério (ii) da rubrica de
autoria — porque o gate julga a **entrega contra o card**, e o defeito estava no **card contra a
doutrina**. O único sinal foi o campo `pendencia=`, preenchido por disciplina do executor; nenhum
verbo, guarda ou parser o teria emitido. É a mesma família do `AE-16` (i): o derivado acerta o que
lhe pedem e erra o que ninguém lhe pede para medir.

- **`AE-19` (2026-09-19, `BKL-T10` devolvida `blocked` razão `premissa` pelo `A3b`) — o passo 11
  manda igualar o `Status` de uma subtarefa a uma célula de índice que a norma não dá a
  subtarefas.** Devolução por conduta correta: ambiguidade **declarada** em vez de decidida,
  nenhum arquivo tocado (`G-EXECREADY`).

  **Fato medido (2026-09-19, `pantonic-executor`, 14 tool uses, sobre a árvore em `eb93490`):**
  o passo 11 do card prescreve igualar o `- **Status:**` de `TK-54a` e `TK-54b` ao *"núcleo da
  célula do índice do mesmo item"*. Três coisas colidem aí:
  - **subtarefa não tem linha de índice própria** — `§2.2` e `§2.5` dão linha de índice a **plano**
    e a **tíquete**, e a `TK-54a`/`TK-54b` são subtarefas do `TK-54`. O referente que o passo manda
    ler não existe;
  - a `TK-54a` já carrega, em `docs/DIARIO_DE_OBRAS.md:1284`, um `**Status:** \`done\`` **fora da
    forma prescrita** — sem o `- ` inicial e sem `· data` —, de modo que o instrumento não o lê
    como linha de campo;
  - esse `done` **diverge** do `ready` da célula de índice do pai `TK-54`.

  **Por que o executor parou:** o passo não diz qual das três saídas vale — reconciliar o `done` da
  subtarefa contra o `ready` do pai, duplicar a célula do pai nas subtarefas, ou fazer a subtarefa
  herdar o estado do pai. São três estados finais diferentes para o mesmo arquivo, e escolher é
  decisão, não execução (Regra 8).

  **Rota:** decisão de planejamento sobre `§2.1`/`§2.2` — se subtarefa tem projeção de estado e,
  tendo, de onde ela sai. Escalado ao consultor como `ESC-3`.

  **Resolvido pela `DB-45` (2026-09-19, `ESC-3`, `pantonic-consultant`).** O texto acima fica
  **literal**. **Sim, subtarefa tem projeção de estado**, e ela mora só na linha `- **Status:**` da
  seção dela — §2.1a, nova. Das três saídas que o executor nomeou, vale a **reconciliação**, e as
  outras duas caem por um motivo estrutural, não de gosto: a `DB-36` computa o `<done>/<total>` do
  pai **a partir** do estado dos filhos, de modo que derivar o filho do pai inverte a projeção,
  fecha ciclo e força dois filhos em estados diferentes a um valor só — seria escrever `ready` numa
  `TK-54a` que o documento declara `done` desde 2026-09-18.

  **O que a devolução não viu, e a medida do reparo achou.** O `AE-19` mediu a ponta; o corpo é
  maior, e o passo 11 teria parado de novo três vezes: (i) a enumeração dele nomeava **5** itens
  (herança datada da `BKL-T6`, de 2026-09-15) contra os **13** vivos de hoje — dez dos quinze
  originais eram `AUT-T*` de um plano que a `DB-43` tirou do corpus; (ii) a regra herdada
  *`backlog` → `cancelled`, absorvido pelo `P-0738`* vale para `TK-23` e `TK-32` e **não** vale para
  `TK-55`, que traz o mesmo `backlog` na célula e foi **aberto** por ato do dono em 2026-09-19,
  quatro dias depois de a regra ser escrita; (iii) o passo 12 mandava pôr `Sonnet · ` na `TK-54a`,
  que **já o tem**. Os treze valores ficam fixados na tabela da §2.1a, com a evidência de cada um, e
  o passo passa a **transcrever**.

  **Dois defeitos que nenhum lint vê, e que o aceite do card exigia:** `docs/DIARIO_DE_OBRAS.md:828`
  traz `### TK-51`, subtarefa com o id do **pai** (`C-1`), que passa a `### TK-51a`; e
  `docs/DIARIO_DE_OBRAS.md:150`, a linha de índice do `TK-54`, carrega prosa **depois** do pipe
  final — a única das 32 linhas da tabela que o parser não lê. Como não é lida, `check` não acusa
  nada; e o efeito só apareceria **depois** do card, quando a `TK-54b` em `ready` fizesse do `TK-54`
  um pai de candidato elegível sem linha de índice, com `next` em **E-3**. Enquanto o `BKL-T10`
  estiver `in-progress`, a §2.5 item 2 curto-circuita a seleção antes da elegibilidade e o item 2 da
  `Verificação` passaria **pelo motivo errado**. Os dois viraram passo e ganharam linha de aceite
  própria (itens 7 e 8).

  **Reconferência do item 2 do acionamento.** A **`DB-36` não muda de fórmula**; muda o que ela
  imprime, e fica declarado: `TK-51` **1/1**, `TK-53` **1/1**, `TK-54` **1/2**. A **`DB-4` não muda
  em nada**, e por fato medido: a expressão *candidato a fechamento* **não existe** em
  `.claude/tools/backlog.py` — o rodapé de `next` imprime `inbox de planos`, `fila de memória` e
  `blocked`, e nada mais. Norma publicada em `## 3` sem implementação e sem teste.

### AE-20 — Estatística do acionamento `ESC-3` (`pantonic-consultant`, 2026-09-19)

Mesma residência e mesma forma do `AE-16` e do `AE-18` (`docs/consultant-spec.md` §9): prosa, no
bloco de achados, um achado por acionamento.

- **O que motivou:** o `BKL-T10`, primeiro card despachado depois de dois reparos de consultor,
  voltou `blocked` razão `premissa` em **14 tool uses**, sem tocar arquivo. O passo 11 mandava
  igualar o `Status` de uma subtarefa ao *núcleo da célula do índice do mesmo item*, e subtarefa não
  tem linha de índice — o referente **não existia**, e as três leituras possíveis davam três estados
  finais diferentes para o mesmo arquivo.
- **Classe do impedimento:** *norma silenciosa sobre um caso que o corpus tem* — a §2.1 dava à
  subtarefa os campos, a §2.2 lhe negava a linha de índice, e **nenhuma das duas dizia de onde sai o
  valor**. Não é decisão ausente (`ESC-34`), nem contradição entre decisões fechadas (`ESC-1`), nem
  dimensionamento diferido (`ESC-2`): é **lacuna de norma**, e o card herdou a lacuna ao citar um
  referente que a norma nunca definiu. Classificada **técnico/tático**: a `DB-36`, que já existia,
  fixa sozinha a direção da projeção; escopo, rota e entregáveis do plano não mudam e nenhum ato do
  dono é requerido. A janela segue para o redespacho do `BKL-T10`.
- **O que ficou inconclusivo:**
  - **A `DB-4` é norma sem implementação.** O rodapé *candidato a fechamento* está publicado na
    `## 3` deste plano e não existe no código; a `BKL-T4`, que entregou as projeções, fechou `done`
    com ressalva 85% e ninguém mediu esta. Fica **fora** do `BKL-T10` — é matéria nova, não corpus e
    não migração — e **sem card**: abri-lo aqui seria matéria transversal, que o critério (ii) da
    rubrica proíbe. Duas consequências reais ficam pendentes: com a migração, `TK-51` e `TK-53`
    passam a ter todos os filhos terminais e **deveriam** aparecer no rodapé; nada os mostrará.
  - **Quantas outras linhas do diário estão fora de forma sem violação.** Mediu-se **uma** classe (a
    linha que não fecha em `|`) e **uma** ocorrência dela, porque foi a que bloqueava o aceite. Não
    se varreu o arquivo em busca de outras formas invisíveis ao lint — a varredura é matéria de quem
    planejar o endurecimento do `check`, não deste reparo.
  - **O valor de data de quatro dos treze itens é o melhor disponível, não o medido.** `TK-23`,
    `TK-32`, `TK-38` e `TK-51` recebem a data que a própria célula ou a prosa citam; onde a prosa
    não datava o ato, usou-se a data do fato mais próximo. A data não entra em aceite nenhum e não
    muda estado; fica registrado que ela é **herdada**, não apurada.

**Para a spec de robustez (`TK-55`), classe *derivado que erra sem sinal*, três evidências deste
acionamento** — e a classe fecha a janela com seis: (i) a linha `**Status:**` de
`docs/DIARIO_DE_OBRAS.md:1284`, fora de forma, **não entra no lint** porque o parser não a reconhece
como linha de campo: o instrumento não vê o que não sabe ler, e a ausência de achado é lida como
saúde; (ii) a linha de índice do `TK-54`, pelo mesmo mecanismo — uma linha de tabela que não fecha
em `|` desaparece do modelo inteiro, e nenhuma das 9 violações de `check` cobre *linha que deveria
ser índice e não é*; (iii) **norma publicada sem implementação** (`DB-4`), que nenhum teste e nenhum
guarda confrontam — a `## 3` descreve um rodapé que o código nunca emitiu. As três têm a mesma
forma: **o derivado cala onde deveria falar**, e o silêncio é indistinguível de conformidade.

- **`AE-21` (2026-09-19, `BKL-T10` devolvida `blocked` razão `premissa` pelo `A3b`, **segundo
  bloqueio do mesmo card**) — o passo 10 manda mover prosa de célula de índice para destinos que o
  próprio card proíbe tocar.** Devolução por conduta correta: obstáculo medido, saídas nomeadas,
  nenhuma escolhida, nenhum arquivo tocado (`G-EXECREADY`).

  **Fato medido (2026-09-19, `pantonic-executor`, 39 tool uses, sobre a árvore em `eb93490`):** o
  passo 10 manda levar **toda** célula do índice com prosa (`C-4`) ou token fora do vocabulário
  (`C-3`) a token puro, movendo a narrativa **verbatim** para *"a seção do item correspondente"*.
  São **8** células, e o número bate exatamente com o *"8 `C-4`"* que a `DB-43` declara como
  remanescente após o corpus: `P-0733-DHB`, `P-0734-EXA`, `P-0737-AUT`, `TK-51`, `TK-52`, `TK-38`,
  `TK-48`, `TK-53` — linhas 131–149 do índice. Logo o passo 10 **também** alcança linhas de
  **plano**, e não só as treze subtarefas da `§2.1a`.

  **Para três das oito, o destino que a própria linha de índice publica é ilícito neste card:**
  - `P-0733-DHB` e `P-0734-EXA` ancoram em `docs/DIARIO_HISTORICO.md`, que o bloco `Não fazer`
    deste card **proíbe tocar**;
  - `TK-52` ancora em `docs/plans/P-0738-contexto-esgotado.md#9-achados-da-execução`, e a
    `Restrição` do bloco C deste mesmo card fixa que em corpo de plano fechado *"muda-se uma linha
    por arquivo — a que carrega o campo `Status` — e nada mais"*.

  **As três saídas, todas decisão:** inventar seção nova no diário para hospedar a narrativa;
  gravar mesmo assim no histórico e no corpo do plano fechado, contra duas restrições do card; ou
  deixar essas três células fora do escopo do passo 10. O card não fecha nenhuma, e escolher não é
  execução (Regra 8).

  **O que o segundo bloqueio do mesmo card mede, além do defeito.** Os dois bloqueios foram por
  **conduta correta** e **não consumiram retentativa** (`A3b`) — a tarefa segue com **0** gastas —,
  mas apontam para o mesmo lugar: o `BKL-T10` herda de `BKL-T6` uma enumeração e um passo de
  migração autorados em 2026-09-15, contra uma árvore e um corpus que mudaram duas vezes desde
  então (`DB-43`, `DB-45`). O `AE-19` corrigiu a enumeração do passo 11; este corrige o alcance do
  passo 10. Se um terceiro passo do mesmo bloco ceder pela mesma razão, a matéria deixa de ser
  passo e passa a ser o **bloco inteiro de migração**.

  **Rota:** decisão sobre o alcance do passo 10 e o destino da narrativa das três células
  conflitantes. Escalado ao consultor como `ESC-4`.

  **Resolvido pela `DB-46` (2026-09-19, `ESC-4`, `pantonic-consultant`).** O texto acima fica
  **literal**. **A saída não é lista de exclusão, é regra**, e ela já estava implícita em duas
  decisões: a `DB-15` diz que *o índice é a projeção final* do item fechado, e a `DB-43` fixou que o
  lint governa o **corpus vivo**. Logo a narrativa de fechamento na célula de um item terminal
  **pertence àquela célula** — é a lápide dele —, e exigir token puro ali é exigir que o fechado
  mude depois de fechado, para um destino que não existe. Regra: **núcleo terminal ⇒ célula
  congelada, sem `C-4`**; núcleo vivo ⇒ token puro, com a narrativa indo para a seção do item no
  próprio diário. O critério é um *lookup de token*, e um executor frio o aplica sem julgar caso a
  caso. `C-3` continua valendo para toda linha, porque o núcleo alimenta a decisão de corpus.
  Medido no ato: `C-4` cai de **8** para **2**, e as **três** células conflitantes (`P-0733-DHB`,
  `P-0734-EXA`, `TK-52`) são terminais e não se tocam — **nenhuma** edição em
  `docs/DIARIO_HISTORICO.md` nem em corpo de plano fechado, e o item 9 da `Verificação` passa a
  medir exatamente esse **não-toque**.

  **Resposta ao que esta entrada perguntou no fim.** Ela previu: *"se um terceiro passo do mesmo
  bloco ceder pela mesma razão, a matéria deixa de ser passo e passa a ser o bloco inteiro"*. A
  varredura dos 16 passos, feita neste acionamento, mostra que **já eram cinco de seis** no bloco de
  migração — 11 e 12 reautorados no `ESC-3`, 10 bloqueando agora, e **dois que ninguém tinha
  tocado**: o passo 9 nomeava **um** parágrafo de fila onde existem **três** (o terceiro com
  **70 linhas**) e mandava para `## TK-54` justamente o parágrafo cujo texto diz *migra para
  `## P-0739`*; e o passo 8 não dizia que os marcadores vão **sozinhos na linha**, que é como
  `transacionar_status` os acha (igualdade exata de linha), nem o que fazer com a `Fila corrente`
  viva. O bloco B foi **reescrito inteiro** contra a árvore de 2026-09-19. Os blocos A, C e D
  ficaram como estavam, e não por omissão: os **dez** referentes de código do bloco A e as **três**
  linhas de cabeçalho do bloco C foram conferidos um a um, e todos estão exatos.

### AE-22 — Estatística do acionamento `ESC-4` (`pantonic-consultant`, 2026-09-19)

Mesma residência e mesma forma do `AE-16`, `AE-18` e `AE-20` (`docs/consultant-spec.md` §9).

- **O que motivou:** **segundo** bloqueio do mesmo card, em **39 tool uses**, sem arquivo tocado. O
  passo 10 mandava mover a narrativa de toda célula `C-3`/`C-4` para *a seção do item
  correspondente*; para três das oito células, o destino que a própria linha publica é proibido pelo
  próprio card — `docs/DIARIO_HISTORICO.md` e corpo de plano fechado.
- **Classe do impedimento:** *enumeração herdada contra árvore que se moveu* — a mesma do `ESC-3`,
  e é a **reincidência** que muda a natureza do acionamento. Aqui o pedido do loop já não era
  *decida o caso*, e sim *diga se a matéria ainda é passo a passo ou se o bloco inteiro precisa ser
  reautorado*. O acionamento deixou de ser reativo e virou **varredura**: 16 passos conferidos
  contra a árvore, não só o que bloqueou. Classificado **técnico/tático** — a regra sai de duas
  decisões já fechadas (`DB-15`, `DB-43`), escopo e rota não mudam, nenhum ato do dono é requerido.
- **O que ficou inconclusivo:**
  - **A varredura cobriu referente, não semântica.** Conferiu-se que cada linha e cada função
    citadas existem e são o que o passo diz; não se simulou a execução de nenhum passo. Um defeito
    que só apareça ao aplicar a edição — colisão de âncora, seção que fica vazia, bullet que quebra
    lista — continua possível, e a contingência do card é a rede.
  - **A seção `## P-0739` nasce neste card e ninguém decidiu o fim dela.** Ela é destino de dois
    blocos de fila, e o `## P-0737`/`## P-0738` são o precedente de forma. Quando o `P-0739` fechar,
    a seção deveria ir para `docs/DIARIO_HISTORICO.md` como as dos planos fechados — não há regra
    escrita para isso, e este reparo não a cria.
  - **O bloco de 70 linhas vai inteiro para `## TK-54` e carrega matéria de `TK-53`.** Partir por
    assunto é autoria; não partir deixa registro de `TK-53` morando na seção do `TK-54`. Escolheu-se
    não partir, e o custo fica nomeado: quem condensar o diário depois herda a mistura.

**Para a spec de robustez (`TK-55`), classe *derivado que erra sem sinal*, a evidência deste
acionamento — e a mais cara da janela:** **o card herdado erra em silêncio até ser executado.** Os
dois passos que a varredura achou (8 e 9) estavam quebrados desde 2026-09-15 e **passaram por dois
gates** — a revisão da `BKL-T9a`, que aprovou a transcrição **100%**, e a conferência manual do
despacho —, porque ambos julgam a **forma** do card, e nenhum confronta os **referentes** dele com a
árvore. Um passo que cita `docs/DIARIO_DE_OBRAS.md:37` e uma enumeração de cinco itens tem a mesma
aparência estando certo ou errado; só o executor descobre, um por despacho. A lição roteada: o que
falta não é mais critério de autoria, é um **verbo que confronte cada referente de card com a
árvore** — o mesmo `card_check` que hoje confere três elementos de `Verificação` e não abre um único
arquivo citado pelos `Passos`.

- **`AE-23` (2026-09-19, `BKL-T10` devolvida `blocked` razão `premissa` pelo `A3b`, **terceiro
  bloqueio do mesmo card**) — o aceite do card é inatingível pelos próprios passos dele, e o
  defeito é de segunda ordem: só existe depois de uma edição que o card manda fazer.** Devolução
  por conduta correta: nenhum arquivo tocado (`G-EXECREADY`).

  **Fato medido (2026-09-19, `pantonic-executor`, 53 tool uses, sobre a árvore em `eb93490`):** o
  passo 11 fecha a lista de `C-4` em seis atos (`TK-38`, `TK-48`, `TK-55`) e o passo 12 só move a
  *"prosa depois do pipe final"* de `docs/DIARIO_DE_OBRAS.md:150`. **Nenhum dos 18 passos** trata a
  narrativa da **própria célula 3 do `TK-54`** — `ready *(**escopado em 2026-08-31**…)*` —, que
  passa a produzir `C-4` **assim que o passo 12 restaura o parse da linha**. Confirmado por regex
  pelo executor: `_celula_indice` casa `tem_narrativa=True`, e o núcleo `ready` **não é terminal**,
  logo a célula não é congelada pela `DB-46`. Consequência: o item 1 da `Verificação` e o
  `Pronto quando` — ambos `check` exit 0 — ficam **inatingíveis** pelos 18 passos como escritos.

  **Por que a varredura do `ESC-4` não o pegou, e isto não é falha dela.** O consultor declarou o
  limite no próprio relatório, antes de o defeito aparecer: *"a varredura cobriu referente, não
  semântica — conferi que cada linha e cada função citadas existem e são o que o passo diz; não
  simulei a aplicação de nenhuma edição"*. Este defeito **não existe na árvore de hoje**: ele nasce
  quando o passo 12 roda. Nenhuma conferência estática o alcançaria.

  **O que os três bloqueios medem juntos.** Todos por conduta correta, todos sem arquivo tocado,
  **0 retentativas gastas** (`A3b` não gasta), e cada um trouxe defeito real:
  `AE-19` (enumeração do passo 11 estagnada: nomeava 5 itens, os vivos eram 13), `AE-21` (alcance
  do passo 10 colidindo com duas restrições do próprio card, mais os passos 8 e 9 quebrados que a
  varredura do `ESC-4` encontrou de lambuja) e este. A série é **decrescente em superfície e
  crescente em profundidade**: enumeração → alcance → efeito de segunda ordem. Os dois primeiros
  eram visíveis por leitura; este só por simulação.

  **Custo medido do card até aqui, sem entrega:** três despachos de executor
  (108,4k + 169,7k + 259,6k) e duas passagens de consultor (245,7k + 290,3k) — **1.073,7k tk** e
  **156 tool uses** para zero linha entregue. A série está em `docs/telemetria.tsv`.

  **Rota:** escalado ao consultor como `ESC-5`, com a pergunta de classificação posta
  explicitamente — se o reparo é mais um passo, ou se o aceite do card precisa ser **simulado
  ponta a ponta** antes de qualquer 4º despacho, ou se a matéria virou estratégica.

  **Resolvido pela `DB-47` (2026-09-19, `ESC-5`, `pantonic-consultant`) — e a resposta à pergunta
  de convergência é: nem mais um passo, nem escalada. Simulação.** Os 18 passos foram aplicados
  numa **cópia da árvore fora do versionamento** (`%TEMP%/p0739sim`, com `docs/DIARIO_DE_OBRAS.md` e
  os 20 `docs/plans/P-*.md`), e `check` — com os sete passos do bloco A embutidos — rodou sobre o
  resultado. **Achado: exatamente uma violação, e é a desta entrada** — `C-4` na célula 3 do
  `TK-54`. Nenhuma outra. A série não estava divergindo: ela **convergiu no ato em que alguém rodou
  em vez de ler**.

  **Reparo, e ele é de alcance, não de regra.** Os passos 11 e 12 trocam de ordem e de escopo: o
  novo 11 trata a linha 150 **inteira, num ato só** — a prosa depois do pipe final **e** a narrativa
  da célula 3 vão ambas para `## TK-54`, a célula fica em token puro `ready`, a linha volta a fechar
  em `|` — e vem **antes** do passo de células, porque restaurar o parse é justamente o que cria a
  violação; o novo 12 enumera as cinco células restantes e declara que a do `TK-54` não é dele. **A
  `DB-46` não muda**: `TK-54` tem núcleo `ready`, é item vivo e sempre esteve do lado *token puro*
  da regra de célula congelada; as seis células terminais seguem intactas.

  **Medido na cópia, depois do reparo:** `check` **0 violações**; **E-2** ok; **E-3** ok; elegível
  `TK-54b`; diretiva canônica lida pelo parser como `['TK-54a']`; pares da `DB-36` em `TK-51`
  **1/1**, `TK-53` **1/1**, `TK-54` **1/2** — confirmando por medida o que o `ESC-3` declarara por
  cálculo. Os literais de `Verificação` saíram **nos dois mundos**, e a `Verificação` ganhou o item
  **8**, o único que discrimina este achado: **1** na cópia migrada contra **0** na árvore de hoje.
  O aceite do card deixou de ser afirmação e passou a ser **saída observada**.

### AE-24 — Estatística do acionamento `ESC-5` (`pantonic-consultant`, 2026-09-19)

Mesma residência e mesma forma do `AE-16`, `AE-18`, `AE-20` e `AE-22` (`docs/consultant-spec.md` §9).

- **O que motivou:** **terceiro** bloqueio do mesmo card, em **53 tool uses**, sem arquivo tocado —
  e, desta vez, o loop não pediu a decisão do caso: pediu a **decisão de método**. *O reparo é mais
  um passo, ou o aceite precisa ser simulado ponta a ponta?* Com a classificação posta
  explicitamente como pergunta aberta, e a saída estratégica oferecida como legítima.
- **Classe do impedimento:** *defeito de segunda ordem* — a violação não existe na árvore; ela é
  **criada** por uma edição que o próprio card manda fazer. É a primeira das cinco classes desta
  instância que **nenhuma leitura** alcança: enumeração (`ESC-3`) e alcance (`ESC-4`) eram
  visíveis; esta só por execução. Classificada **técnico/tático**, e o motivo é o conteúdo da
  decisão, não o custo: o reparo é de **alcance de passo**, uma célula, sem regra nova, sem mexer
  na `DB-46`, sem tocar escopo, rota ou entregável — não existe pergunta a fazer ao dono. A série
  de custo **é** matéria do dono, e sobe pelo relatório de encerramento do `scrum-master`
  (`G-NOASK`), que é o canal, e não por aborto de janela.
- **O que ficou inconclusivo:**
  - **A simulação valida o alvo, não a escrita.** Ela aplicou as edições por script, com as regras
    do bloco A reimplementadas no harness — não rodou o `backlog.py` alterado, que não existe, nem
    exercitou a mão do executor. Um defeito de **redação** dos passos (ambiguidade que o script
    resolveu de um jeito e o executor resolveria de outro) continua possível; o que ficou provado é
    que **existe um estado final** em que o aceite fecha, e qual é.
  - **O bloco gerado da §2.3 foi simulado com conteúdo plausível, não computado.** O passo 9 manda
    escrever `**Fila corrente:**` e um bullet por pai vivo; a cópia recebeu um bloco de forma
    correta, mas os valores não vieram de `_bloco_fila_corrente` — a função existe e não foi
    chamada, porque o que estava em jogo era `check`, que não lê o bloco. O conteúdo real sai no
    despacho.
  - **A cópia não é um repositório git.** O item 10 da `Verificação` (`git status` invariante sobre
    o histórico e dois planos fechados) **não** foi exercitado na simulação; ele mede ausência de
    escrita, e a ausência de escrita é o estado natural da cópia. Segue conferível só no despacho.

**Para a spec de robustez (`TK-55`), classe *derivado que erra sem sinal*, a evidência desta
passagem — e ela fecha a série da janela em sete:** **o aceite de um card pode ser inatingível sem
que nada o diga.** O `BKL-T10` passou por revisão de autoria (aprovada 100%), por duas reautorias de
consultor e por três conferências de despacho afirmando `check exit 0`, e em nenhum desses momentos
alguém **rodou** o aceite: todos o leram. O critério (xii)(d) da `RUBRICA_DE_REVISAO.md` §8 já exige
*alvo alcançável dentro do escopo declarado do card* — e a exigência é **verdadeira e inverificável
por leitura** quando o alvo depende do estado que os próprios passos produzem. A lição roteada, e é
a mesma do `AE-22` vista de outro ângulo: o kit não tem como confrontar um card com o **mundo que
ele cria**, só com o mundo que ele encontra. Enquanto não tiver, *aceite de card que edita corpus
roda em cópia antes do despacho* — que é o que a `DB-47` fez, e o custo dela foi **uma** passagem de
consultor contra os **três** despachos que a leitura consumiu.

- **`AE-25` (2026-09-19/20) — a janela encerrou por **poluição de contexto** (`B2`, Regra 2 do
  `CLAUDE.md` global) com o 4º despacho da `BKL-T10` caído por limite de sessão e trabalho parcial
  não julgado na árvore.** Dois fatos, e o segundo é o que encerra.

  **(i) Queda do subagente (`A1`).** O 4º despacho da `BKL-T10` foi interrompido por
  *session limit* da conta após **154 tool uses / 523,2k tk / 2.112,3 s** — consumo **medido**
  (o bloco `<usage>` veio na notificação), registrado em `docs/telemetria.tsv` como
  `BKL-T10-4o-despacho-PARCIAL`. A `A1` autorizaria **uma** retomada por `SendMessage`; ela **não
  foi feita**, pelo fato (ii).

  **(ii) Poluição por coesão, medida na árvore.** Entre a queda e a retomada da sessão, entraram
  na árvore dois planos que esta janela não produziu e não pode julgar:
  - `docs/plans/P-0742-loop-fora-do-llm.md` (22:32) — **"O loop sai do LLM"**, `Origem:` **decisão
    de rota do dono**, 2026-09-19, sobre a posição L8 de `_VIABILIDADE-agente-leitor.md` §7.4;
    `Status: blocked`, **depende de `P-0739` `done`**. É decisão do dono sobre a natureza do loop
    que executa esta janela, amarrada à conclusão **deste** plano;
  - `docs/plans/P-0741-modelo-conceitual.md` (22:22, 83 KB) — plano novo `ready`, 5 tarefas
    `MC-T1`..`MC-T5`, marco 1 dado pela aprovação do dono em 2026-09-19; `docs/plans/_INBOX.md` já
    o registra e o contador subiu para `P-0742`.

  Dois dos sinais que a Regra 2 enumera: *material de outra iniciativa entrou no contexto* e *a
  rota bifurcou / decisão do dono contradiz o que já foi ingerido*. A parada é **fatal e imediata**,
  **não graciosa**, e **sem ponteiro de retomada** — nada produzido depois do sinal se aproveita, e
  o `BKL-T10a` não foi despachado.

  **Estado medido da árvore no encerramento** (nada commitado, `HEAD` = `eb93490`):
  `.claude/tools/backlog.py` +83 linhas, `tests/test_backlog.py` +187, `docs/DIARIO_DE_OBRAS.md`
  +107/−86. A migração está **parcial**: há **1** marcador `fila:gerada` onde o par exige dois, e
  `backlog.py check` segue **vermelho** nos três `C-5` que o bloco C do card existe para reconciliar
  (`P-0735-RPC`, `P-0737-AUT`, `P-0738-CTX`). **Este trabalho não passou por revisão, não tem
  laudo e não tem RDO** — não é entrega, é rascunho interrompido, e a próxima janela decide entre
  descartá-lo e retomá-lo com o card na mão.

  **O `docs/DIARIO_DE_OBRAS.md` foi deixado intocado no encerramento**, inclusive a linha
  `**Fila corrente:**` que o relatório de janela normalmente reescreve: o arquivo está no meio da
  migração do passo 11, e editá-lo agora corromperia estado que só um `BKL-T10` julgado resolve. O
  relatório de encerramento da janela carrega o que a `Fila corrente` carregaria.

  **Resolução (ato do dono, 2026-09-20, sobre o relatório de encerramento desta janela):** duas
  decisões. **(a) Prioridade** — concluir o `P-0739`; o `P-0741` e o `P-0742` ficam atrás dele,
  o que é consistente com o próprio `P-0742`, que declara `depende de P-0739 done`. A rota
  deixa de estar bifurcada: é ordenação, não contradição. **(b) Pendência 1 — descartar e
  redespachar.** Executado no ato: `git checkout` de `.claude/tools/backlog.py`,
  `tests/test_backlog.py` e `docs/DIARIO_DE_OBRAS.md`, com a correção de ponteiro do
  `AE-14` (ii) reaplicada no diário logo depois — era a única linha do arquivo que não vinha do
  despacho caído, e a checagem de que o diário **não** continha matéria das sessões paralelas foi
  feita **antes** do descarte, não depois. Baselines reconferidas na árvore limpa: `check` de volta
  aos **309** achados, `review_evidence.py --tarefa BKL-T10` **exit 0**, `HEAD` em `eb93490`.
  O trabalho parcial do 4º despacho **não existe mais** e não se cita como precedente.

- **`AE-26` (2026-09-20, `BKL-T10` devolvida `blocked` razão `premissa` no 5º despacho) —
  defeito do `scrum-master`, não do card: o despacho afirmou estado de árvore que o próprio
  `scrum-master` tinha acabado de contrariar.** Custo: **3 tool uses / 60,0k tk / 27,7 s** — o
  mais barato da janela, porque o executor conferiu a premissa **antes** de editar e parou.

  **Fato medido:** o texto do despacho dizia *"a árvore está limpa... `git status` sem nenhuma
  modificação em código ou no diário"*. O executor rodou `git status --short` e mediu **seis**
  arquivos modificados e **cinco** não rastreados, entre eles os dois alvos centrais do card. A
  afirmação era falsa **como escrita**.

  **O que era verdade, e é a forma correta de dizê-la:** o descarte do 4º despacho devolveu
  `.claude/tools/backlog.py` e `tests/test_backlog.py` a `HEAD` — os dois estão **fora** do
  `git diff`, literalmente sem modificação — e o `docs/DIARIO_DE_OBRAS.md` tem **exatamente uma**
  linha alterada, o ponteiro do `AE-14` (ii), que **não** é migração. O resto da árvore suja é o
  produto desta janela e das sessões paralelas do dono: o plano com os cards e achados, o RDO da
  `BKL-T9a`, a telemetria, a `consultant-spec`, o `_INBOX.md` e os três planos novos.

  **A lição, e ela é de orquestração:** *"limpa" não é estado, é comparação com um referencial,
  e o referencial tem de vir no despacho.* Dizer **o que está em `HEAD`** e **o que está sujo e
  por quê** custa uma linha; dizer "limpa" custou um despacho. **Não consome retentativa** — o
  executor não falhou e o card não tem defeito; falhou o despacho, e a correção é do
  `scrum-master` (item 3 da *Diretiva de execução do `P-0739`*). Nenhuma regra do bloco A cobre
  "despacho com premissa falsa": a lacuna fica registrada, e o tratamento aplicado foi o mesmo do
  `A2` — reenvio ao mesmo card, sem gastar retentativa.

- **`AE-27` (2026-09-20, pendência do laudo da `BKL-T10`, roteada pelo `B1`) — o bloco gerado
  passa a existir na árvore real, e `_bloco_fila_corrente` não sabe produzi-lo: o primeiro verbo
  de escrita do instrumento destrói a `Fila corrente`.** A entrega fechou **aprovada com
  ressalva, 85%**, bloqueante `nenhuma` — o achado não a rebaixa, e por isso não morreu com o
  laudo. **É bloqueante de uso, não de entrega.**

  **Fato medido (2026-09-20, `pantonic-reviewer`, confirmando o `pendencia=` do executor):** com
  os marcadores `<!-- fila:gerada -->` agora presentes no `docs/DIARIO_DE_OBRAS.md`, o writer
  substitui **tudo** que está entre eles por bullets. Duas consequências:
  - o primeiro `status` ou `start` **apaga a linha `**Fila corrente:**`**, que hoje carrega o
    estado de janela inteiro;
  - os bullets são reescritos casando id de plano por **igualdade exata**, e não pela regra de
    **sufixo** que `_posicao_indice` aplica — divergência entre dois pontos do mesmo módulo.

  **Por que isto não é defeito da entrega.** O casamento por igualdade exata é **pré-existente** e
  está **fora dos 18 passos** do card; o executor o descobriu ao computar o conteúdo **real** do
  passo 9 — precisamente o ponto (ii) que o `ESC-5` declarara não coberto pela simulação, porque
  `_bloco_fila_corrente` nunca tinha sido chamada. A simulação previu a lacuna; a execução a
  mediu.

  **Consequência operacional imediata, e ela vale para esta janela:** **não rodar
  `backlog.py status` nem `backlog.py start` contra o diário vivo até o reparo entrar.** A
  materialização de status segue sendo feita à mão pelo `scrum-master`, como em toda esta janela.

  **Rota:** reparo de `_bloco_fila_corrente` — preservação da `Fila corrente` e casamento por
  sufixo —, com TF que exponha as duas metades. Escalado ao consultor como `ESC-6`, que decide se
  entra no `BKL-T10a` (o próximo da fila, que toca o mesmo arquivo) ou em card próprio antes dele.


  **Resolvido pela `DB-48` (2026-09-20, `ESC-6`, `pantonic-consultant`).** O texto acima fica
  **literal**. Rodei o verbo **em cópia** (`%TEMP%/p0739sim6`, com o diário migrado e os 20 planos;
  nunca a árvore viva) e as duas metades saíram medidas: `status TK-48 blocked` → **exit 0**, e a
  linha `**Fila corrente:**` **desaparece**; o bloco resultante não traz bullet de plano nenhum.

  **A simulação achou uma terceira metade que esta entrada não nomeia.** Reparadas as duas
  primeiras, o bloco sai com **15** bullets de plano, **14** deles de plano **fora do corpus** —
  cinco arquivos declarando o mesmo `P-0729`, vários com `Status` ausente saindo como
  `` (`None`, 0/n) ``. `check` e `_candidatos` ganharam o filtro de corpus na `BKL-T10`;
  `_bloco_fila_corrente` **não** ganhou. Tratar só as duas metades nomeadas trocaria um defeito por
  outro. Com as três, o bloco sai com **2** bullets — `P-0739` e `TK-54` — e a linha sobrevive,
  regenerada.

  **Residência: card próprio, `BKL-T10b`, antes do `BKL-T10a`.** São duas proposições ponta a ponta
  que não se tocam, e o `drain` do `BKL-T10a` **escreve no diário** — entregá-lo antes assentaria o
  comportamento quebrado nos TF dele. A `Ordem de execução` do cabeçalho manda na fila, e o card
  ficou fisicamente entre os dois para que a ordem dos cabeçalhos concorde com ela.

  **Enquanto o reparo não entra, a restrição operacional desta entrada continua valendo, com uma
  correção medida:** `backlog.py diretiva` **não** regenera o bloco (medido em
  `.claude/tools/backlog.py:1197`) e é, hoje, o **único** verbo de escrita seguro contra o diário
  vivo. `status` e `start` seguem proibidos até o `BKL-T10b` fechar.

### AE-28 — Estatística do acionamento `ESC-6` (`pantonic-consultant`, 2026-09-20)

Mesma residência e mesma forma do `AE-16`, `AE-18`, `AE-20`, `AE-22` e `AE-24`
(`docs/consultant-spec.md` §9).

- **O que motivou:** a `BKL-T10` **fechou** — aprovada com ressalva 85%, `check` exit 0 — e deixou
  pendência **bloqueante de uso**: com os marcadores agora presentes no diário, o primeiro `status`
  ou `start` apaga a linha `**Fila corrente:**`. Primeiro acionamento desta instância motivado por
  **entrega aprovada**, e não por card devolvido: o loop está impedido de usar o que acabou de
  construir.
- **Classe do impedimento:** *lacuna prevista que a execução materializou* — o `ESC-5` declarou, no
  inconclusivo (ii), que o bloco gerado fora simulado com conteúdo plausível e que
  `_bloco_fila_corrente` **nunca tinha sido chamada**. A execução chamou. Não é defeito de entrega
  (está fora dos 18 passos, e o casamento por igualdade exata é pré-existente), não é decisão
  ausente e não é enumeração estagnada: é **dívida conhecida vencendo na data marcada**.
  Classificada **técnico/tático** — o reparo vive dentro do instrumento e das seções §2.0/§2.3 que
  o plano já fixou, não muda escopo, rota nem entregável, e nenhum ato do dono é requerido; a
  prioridade que o dono deu de **concluir o `P-0739`** reforça seguir, não escalar.
- **O que ficou inconclusivo:**
  - **A linha de diretiva ficou obsoleta e trava o pickup.** Medido na cópia: `next` sai
    **"nada delegável — 0 elegível(is)"**, porque a diretiva canônica que a migração escreveu diz
    `Priorize \`TK-54a\`` e a `TK-54a` está **`done`**. Não é matéria deste card — diretiva é ato do
    dono e o diário é do `scrum-master` —, e o verbo `diretiva` é seguro de rodar hoje. Fica
    nomeado porque **nenhum lint acusa diretiva que prioriza item terminal**, e o efeito é uma fila
    vazia que parece decisão.
  - **A composição exata da linha `**Fila corrente:**` não foi fechada.** O passo 1 do card manda
    compô-la com as funções que já existem e a contingência cobre campo faltante; a simulação usou
    uma composição plausível, não a definitiva. A §2.3 fixa a **forma**; qual função devolve cada
    campo é escolha de implementação, e ficou com o executor por ser interna ao módulo.
  - **`test_tr_bloco_fila_nao_cresce_com_plano_terminal` é o único invariante do card.** Não há
    teste que exercite o bloco depois de **dois** verbos seguidos, nem `status` seguido de
    `diretiva`. A regeneração passa a ter residência única no passo 4, o que torna o segundo caso
    redundante por construção — mas *por construção* não é *por teste*.

**Para a spec de robustez (`TK-55`), classe *derivado que erra sem sinal*, a evidência desta
passagem:** **o verbo destrutivo saiu `exit 0`.** `status TK-48 blocked` apagou a linha que carrega
o estado de janela inteiro e devolveu **sucesso**, sem aviso, sem `mensagem`, sem nada no rodapé — e
o módulo tem, no próprio ponto, o precedente de declarar omissão em vez de calar (o `aviso` de
marcadores ausentes, que o `TK-55` já acumula como *skip silencioso*). A perda só aparece para quem
**comparar o arquivo antes e depois**. Some-se a isso que o bloco vinha sendo escrito à mão a janela
inteira, o que mascararia a perda por mais tempo. A lição roteada: **verbo que substitui um intervalo
de arquivo deve declarar o que removeu**, e a contagem de linhas removidas × escritas é o derivado
mais barato que existe para isso.

- **`AE-29` (2026-09-20, medido na abertura do despacho do `BKL-T10b`) — o contorno do `AE-27`
  dessincroniza o índice em silêncio, e `next` devolve fila vazia que parece decisão.** Achado de
  orquestração, sem card e sem rodada; rota nomeada abaixo.

  **Fato medido:** com a diretiva já corrigida (ver adiante), `python .claude/tools/backlog.py next`
  devolve **"nada delegável — 0 elegível(is) · blocked 0"**, enquanto o plano tem **4** tarefas
  `ready` (`BKL-T10a`, `BKL-T10b`, `BKL-T11`, `BKL-T12`). Estado real do `P-0739`, contado
  no ato: **22** cards — **13 `done`, 4 `ready`, 5 `cancelled`**. A célula do índice
  (`docs/DIARIO_DE_OBRAS.md:65`) ainda diz **`11/16`** e enumera `BKL-T1`..`T9` + `T2a`..`T2e`,
  nomenclatura anterior ao reagrupamento.

  **Causa, e ela é encadeada.** A `§3` fixa que `status` escreve **num ato só**: linha `Status`
  do item · célula do índice · `<done>/<total>` do pai · bloco `Fila corrente`. O `AE-27`
  tornou `status` e `start` **inseguros** contra o diário vivo, e a janela inteira materializou
  status **à mão** — o que atualiza a linha de campo do card e **não** a projeção do índice. O
  contorno era necessário e correto; o preço dele é esta divergência.

  **Por que `check` não acusa.** A igualdade que o `C-3` prova é entre célula de índice e campo
  `Status` **do item que tem linha de índice** — plano e tíquete (`§2.2`, `§2.1a`). O
  `<done>/<total>` de um plano é **derivado** dos filhos pela `DB-36`, e nenhuma violação cobre
  *derivado envelhecido*: `check` sai **exit 0, nenhuma violação** com o contador errado no
  arquivo. Terceira aparição da mesma classe nesta janela.

  **Consequência prática, e é a perigosa:** uma retomada que confie no instrumento lê
  **"nada delegável"** e conclui que não há trabalho, com quatro tarefas `ready` no plano. O
  `AE-25` já mediu o custo de uma fila vazia enganosa em outro projeto; aqui ela seria produzida
  pelo próprio instrumento que existe para evitá-la.

  **Rota:** recomputar a projeção do índice do `P-0739` é ato de `status`, logo depende do
  `BKL-T10b` fechar. Até lá o despacho **não** passa por `next`: sai do plano, como em toda esta
  janela. Registrado para que a próxima janela não leia a fila vazia como fato.

  **Diretiva corrigida no mesmo ato.** A linha canônica dizia *Priorize `TK-54a`*, e a
  `TK-54a` está `done` — o consultor nomeara isso como inconclusivo (1) do `ESC-6`, notando que
  **nenhum lint acusa diretiva que prioriza item terminal**. O dono declarou a prioridade em
  2026-09-20 (*"priorizar a conclusão deste plano"*), e a transcrição dela é materialização, não
  decisão: a linha passa a *Priorize `P-0739`* com a fila
  `BKL-T10b` → `BKL-T10a` → `BKL-T11` → `BKL-T12`. Escrita pelo verbo `diretiva`, que o
  `ESC-6` mediu como **o único verbo de escrita seguro** hoje (`transacionar_diretiva` não
  regenera o bloco); conferido depois: a linha `Fila corrente` **sobreviveu**. A narrativa
  histórica da diretiva anterior não se perdeu — a matéria medida dela vive no `## TK-54`
  (linhas 1332 e 1453) e a crônica das rodadas `RP-1`..`RP-7` no próprio plano.

  **Resolução (2026-09-20, no despacho do `BKL-T10a`) — fechado pelo próprio instrumento.** Com o
  `BKL-T10b` `done`, `status`/`start` voltaram a ser seguros, e o primeiro uso real do verbo na
  árvore viva foi o despacho seguinte: `python .claude/tools/backlog.py start BKL-T10a` → **exit
  0**. Conferido contra cópia do diário tirada imediatamente antes:
  - a linha `**Fila corrente:**` **sobreviveu e foi regenerada** — passou a apontar o `P-0739`
    (`ready 16 · blocked 0 · in-progress 1`), com o bullet `- `P-0739` (`in-progress`, 14/17)`;
  - a célula do índice saltou de **`11/16`** para **`14/17`**, que é exatamente a contagem apurada
    à mão minutos antes (**13 `done` + o `BKL-T10b` recém-fechado = 14**, sobre **17** não
    `cancelled`). O instrumento e a contagem manual **convergiram sem se consultarem** — é a
    verificação mais forte que a `DB-36` recebeu até aqui;
  - `backlog.py check` seguiu **exit 0**, e o arquivo cresceu **uma** linha (1705 → 1706), a do
    bullet novo.

  O defeito descrito acima, portanto, **não era do instrumento**: era do contorno manual que o
  `AE-27` impôs. Removido o contorno, a projeção se recompôs no primeiro ato.

  **Fica de pé um resíduo, sem card:** a **coluna descritiva** da linha de índice do `P-0739`
  segue com prosa envelhecida — ainda diz *“16 tarefas”*, *“11 fechadas”* e *“Primeiro ato da
  retomada: transcrever `BKL-T10`..`BKL-T12`”*, tudo já superado. O token de status e o contador
  estão certos e por isso `check` sai limpo: a `DB-46` governa o **núcleo** da célula, não a coluna
  de descrição. Matéria de condensação do diário, não deste plano.

- **`AE-30` (2026-09-20, `BKL-T10a` devolvida `blocked` razão `premissa`) — contradição
  aritmética interna ao card, fechada pelo `scrum-master` sem acionar o consultor.** Devolução
  por conduta correta: nenhum arquivo tocado, as duas saídas nomeadas e nenhuma escolhida.

  **Fato medido (2026-09-20, `pantonic-executor`, 38 tool uses):** o item 3 da `Verificação`
  mandava `python -m pytest tests/test_backlog.py -q -k drain` devolver **6** selecionados. O
  bloco `Testes` do mesmo card nomeia **cinco** `test_tf_drain_*` e **um** TR,
  `test_tr_historico_do_inbox_so_cresce` — cujo nome **não contém** o literal `drain`. Escritos
  os seis exatamente como o card os nomeia, `-k drain` seleciona **5**. O `Pronto quando` ficava
  irrealizável como escrito.

  **Por que não foi ao consultor.** O executor nomeou duas saídas — renomear o TR, ou aceitar o
  item 3 como está — e tratou as duas como equivalentes. Não são: o bloco `Testes` é a
  **especificação** (diz quais testes existirão) e a `Verificação` **mede** o que a
  especificação prescreve. Renomear o TR seria mudar a especificação para caber na medida, que é
  a direção errada. Corrigir a medida para **5** é aritmética, não rota — e o próprio card já
  provava a intenção ao usar **dois** padrões separados no item 2 justamente porque o TR não casa
  o literal. Fechado sob o item 3 da *Diretiva de execução do `P-0739`* (dono, 2026-09-19), que
  autoriza a orquestração a preencher lacuna de plano registrando a pendência.

  **Reparo aplicado:** item 3 passa a **5**, com a razão escrita no próprio item (o par 2×3 mede
  *seis escritos* contra *cinco de `drain` que passam*, de propósito), e o `Pronto quando` nomeia
  a diferença como desenho. **Não consome retentativa**: o card tinha defeito, o executor não
  falhou.

  **Classe, para a spec de robustez (`TK-55`):** *aceite que conta nomes por substring sem conferir
  a lista que o próprio card fixa.* É parente do `AE-26` — número afirmado sem ser rodado — e
  reincidente nesta janela apesar do método do `ESC-5`: a simulação roda o **aceite do corpus**,
  e não os **contadores de teste**, que só fecham depois de os testes existirem.

- **`AE-31` (2026-09-20, pendência do laudo da `BKL-T10a`, roteada pelo `B1`) — o verbo `drain`
  existe, está testado e **nunca correu contra a árvore real**; nenhum card do plano possui esse
  ato.** A entrega fechou **aprovada 100%**, bloqueante `nenhuma`: o achado não a rebaixa.

  **Fato medido:** quando o consultor autorou o `BKL-T10a` (`ESC-6`), `docs/plans/_INBOX.md` tinha
  **0** linhas vivas, e o card foi escrito sob a premissa de que o `drain` seria **inerte** contra
  a árvore — razão pela qual ele não prescreve a execução real. Entre a autoria e a entrega, uma
  **sessão paralela do dono** registrou ali o `P-0741`, e o inbox passou a ter **1** linha viva. O
  executor acionou a **contingência 3** do card, exercitou o verbo só sobre cópia em `tmp_path` e
  **declarou** a omissão — conduta correta: drenar matéria de uma sessão do dono sem ato dele não
  é decisão de executor.

  **O impasse, nos termos do reviewer:** ele classifica rodar o `drain` real como **ato de
  orquestração do `scrum-master` no fechamento do plano**, mas observa que o **efeito** — admitir
  o `P-0741` ao corpus vivo do instrumento — é **composição de backlog**, e isso pede decisão de
  planejamento. As duas leituras são defensáveis e levam a atos diferentes.

  **O que está em jogo, concretamente:** drenado, o `P-0741` ganha linha de índice e entra no
  corpus; a partir daí `next` passa a considerá-lo, e o `P-0742` — que declara
  `depende de P-0739 done` — também encosta na fila. A diretiva viva (*Priorize `P-0739`*, dono,
  2026-09-20) os mantém atrás deste plano, então **não há contradição de prioridade** — o que há
  é a questão de **quem** exerce o ato e **quando**.

  **Rota:** escalado ao consultor como `ESC-7`, com três saídas a pesar — ato de orquestração no
  fechamento do plano, card próprio antes do fechamento, ou matéria do dono por ser composição de
  backlog.

  **Nota de método, medida no mesmo ato:** a transição `in-progress → done` é **recusada** pela
  máquina de §2.7 (*transição fora da tabela*); o caminho legal é `in-progress → review → done`,
  e foi por ele que esta tarefa se materializou. É o instrumento impondo o ciclo que o loop
  descreve — comportamento correto, registrado porque a janela inteira materializou status **à
  mão** e essa guarda nunca tinha sido exercida.


  **Resolvido pelas `DB-49` e `DB-50` (2026-09-20, `ESC-7`, `pantonic-consultant`).** O texto acima
  fica **literal**.

  **A saída é a primeira — ato de orquestração —, e a razão é decisão já fechada.** A `DB-16` diz
  que *o executor não escreve estado; o `scrum-master` chama o verbo*: `drain` é verbo de escrita,
  logo rodá-lo é orquestração **por construção**, e um card mandando um executor drenar a árvore
  real violaria a `DB-16`. Não é matéria do dono porque a composição do backlog **já foi exercida
  por ele** ao registrar a linha no `_INBOX.md` (Controle 1.1); `drain` não escolhe nada — tira
  estado, título e âncora do próprio plano. A leitura do reviewer acerta sobre o **efeito** e erra
  sobre a **decisão**: o efeito é a projeção mecânica de um ato anterior, e levá-lo ao dono é pedir
  ratificação do que ele já fez (`G-NOASK`).

  **Quando: entre a `BKL-T11` e a `BKL-T12`** — e é o ponto que o loop levantou que dirime. A
  `BKL-T12` mede o pickup em sessão nova; drenar depois dela publicaria na `## 15` um número que
  envelhece no primeiro `drain`, e drenar antes faz a aferição medir o **estado estável**. Soma-se
  que `drain` é o único verbo que nunca correu em produção. Conferência e valores esperados na
  `## 5` item 6, apurados rodando o verbo em cópia (`%TEMP%/p0739sim7`, nunca a árvore viva):
  exit 0, três arquivos tocados, a linha `P-0741-MC` no índice, inbox sem linha viva, histórico +1,
  `check` exit 0 e rodapé em `inbox de planos: 0 por drenar`.

  **A simulação achou um segundo defeito, e esse era bloqueante da próxima tarefa.** `next` saía
  *nada delegável — 0 elegível(is)* com a fila cheia: a linha `- **Depende de:**` da `BKL-T11`
  escrevia *`` `BKL-T10` `` — o hook injeta a saída de `` `next` `` …*, e o parser lê **todo**
  literal entre crases da primeira linha do bullet como id — `depende = ['BKL-T10', 'next']`, e
  `next` nunca resolve para `done`. Quatorze cards do plano têm dependência fantasma pela mesma
  razão; só a `BKL-T11` importava, por ser a única viva. Reparada ela e a `BKL-T12` pela `DB-50`,
  medido na cópia: `next` sai **exit 0** com vencedor **`BKL-T11`** — o pickup selecionando de
  verdade pela primeira vez.

### AE-32 — Estatística do acionamento `ESC-7` (`pantonic-consultant`, 2026-09-20)

Mesma residência e mesma forma do `AE-16`, `AE-18`, `AE-20`, `AE-22`, `AE-24` e `AE-28`
(`docs/consultant-spec.md` §9).

- **O que motivou:** o `drain` existe, está testado e **nunca correu em produção**; entre a autoria
  do `BKL-T10a` e a entrega dele, uma sessão paralela do dono pôs uma linha viva no inbox, e o card
  — escrito sob a premissa medida de **0** linhas vivas — não possui o ato. O executor acionou a
  contingência 3 e declarou a omissão. O loop trouxe as três saídas já nomeadas e **não** decidiu
  sozinho porque reviewer e orquestração liam o ato de formas diferentes.
- **Classe do impedimento:** *premissa de card invalidada por ato externo ao plano* — primeira
  desta série. Não é defeito de autoria (a premissa era verdadeira e medida quando o card nasceu),
  não é enumeração estagnada, não é efeito de segunda ordem: é **o mundo se mexendo entre a autoria
  e a execução**, por ato de quem não participa do loop. Classificada **técnico/tático**: a
  resposta sai inteira de duas decisões já escritas (`DB-16` para *quem*, e a `BKL-T12` para
  *quando*), sem mudar escopo, rota nem entregável, e sem ato do dono.
- **O que ficou inconclusivo:**
  - **O contador do inbox aponta para um id já usado.** `**Próximo id de plano: P-0742.**` com
    `docs/plans/P-0742-loop-fora-do-llm.md` na árvore: o `P-0742` nasceu sem linha de inbox, e o
    `max(id visto) + 1` do `drain` nunca passou dele. O próximo plano aberto colide. Corrigir para
    `P-0743` é ato de quem drena; **impedir** que se repita é guarda que não existe — `check` não
    confronta o contador com os arquivos de `docs/plans/`.
  - **Quatorze cards seguem com dependência fantasma.** Todos terminais, todos inertes por
    `_eh_elegivel` exigir `ready` antes de olhar dependência. Não se tocam (`DB-23`), e o risco
    residual é um card terminal voltar a `ready` por reabertura — caso que o plano não prevê.
  - **A guarda de dependência não resolvida não existe e não foi aberta.** Seria uma violação
    `C-*` nova em `check`; abri-la aqui é matéria transversal às duas tarefas que restam, que o
    critério (ii) da rubrica proíbe. Fica nomeada, sem card.

**Para a spec de robustez (`TK-55`), classe *derivado que erra sem sinal*, a evidência desta
passagem — e é a mais silenciosa de todas:** **`next` respondeu *nada delegável — 0 elegível(is)* com
a fila cheia, e essa saída é indistinguível de um backlog legitimamente vazio.** Não houve exit 3,
não houve violação de `check`, não houve mensagem: o instrumento afirmou, com exit code de sucesso
parcial, que não havia o que fazer — quando havia duas tarefas `ready`, uma delas a próxima da fila.
A causa foi um literal entre crases numa linha de prosa. As duas notas de método que o loop trouxe
apontam para o mesmo lugar e merecem registro junto: a máquina de §2.7 **recusou** `in-progress →
done` e forçou o caminho por `review` — guarda correta, exercida pela primeira vez em toda a janela
porque o status vinha sendo materializado à mão; e o instrumento escreve a linha `Status` na **forma
canônica enxuta**, o que mostra que a prosa rica que a orquestração vinha pondo à mão é a anomalia,
não o instrumento. Nos três casos o veredito é o mesmo: **o que nunca foi exercido não estava certo,
estava apenas não medido.**

- **`AE-33` (2026-09-20, `BKL-T11` devolvida `blocked` razão `premissa` pelo `A3b`) — o passo 6
  aponta para uma seção que a skill de destino **declara não transcrever**, e o `Não fazer` do
  próprio card veda criá-la.** Devolução por conduta correta: nenhum arquivo tocado
  (`G-EXECREADY`), 26 tool uses.

  **Fato medido (2026-09-20, `pantonic-executor`):** o passo 6 manda a heurística de
  `.claude/skills/passagem-de-bastao/SKILL.md` virar *“ponteiro para a §2.5 publicada na skill
  `diario-de-obras`”*. Mas `.claude/skills/diario-de-obras/SKILL.md:132`, na seção *Gramática
  legível por máquina*, declara transcrever **só “§2.1–§2.4 e §2.7”** deste plano — excluindo
  §2.5 e §2.6 **por desenho** —, e o arquivo inteiro (**301** linhas) não contém **nenhuma**
  ocorrência do literal `2.5`. O referente do ponteiro **não existe**, e o `Não fazer` do card
  proíbe editar aquele arquivo para criá-lo.

  **As saídas, e são decisão:** apontar o ponteiro para a §2.5 **deste plano** em vez da skill;
  emendar a `diario-de-obras` para passar a transcrever §2.5 (o que o `Não fazer` veda e a
  exclusão por desenho contradiz); ou substituir o ponteiro por **“rode `backlog.py next`”** —
  leitura que o próprio `Objetivo` do card sugere, já que ele diz que as skills *“mandam rodar
  `backlog.py` em vez de ler diário e inbox à mão”*. As três produzem textos diferentes na skill
  viva, e escolher entre elas é decidir onde a matéria normativa reside — arquitetura de §2.x,
  não execução (Regra 8).

  **Rota:** escalado ao consultor como `ESC-8`. Nota de conteúdo, não de rota: a terceira saída é
  a única que **elimina** o ponteiro em vez de reapontá-lo, e um ponteiro a menos entre skill e
  plano é exatamente o que a `DB-43`/`DB-50` vêm fazendo com o resto do módulo.


  **Resolvido pela `DB-51` (2026-09-20, `ESC-8`, `pantonic-consultant`).** O texto acima fica
  **literal**. A saída é a **terceira**, e não por ser a mais barata: **a exclusão de §2.5/§2.6 na
  `diario-de-obras` é a decisão certa, e ela antecipava este caso.** §2.1–§2.4 e §2.7 são a
  gramática dos **documentos**, que agentes e humanos escrevem e por isso precisam ler; §2.5 (ordem
  de seleção) e §2.6 (forma da saída) são **comportamento de `next`**, que ninguém executa à mão — a
  residência delas é `.claude/tools/backlog.py`. Apontar para §2.5, em qualquer arquivo, manteria na
  skill a heurística que o instrumento passou a executar, contra o próprio `Objetivo` do card;
  transcrevê-la na skill criaria **segunda residência** (`DB-2`) para um comportamento que o código
  já define. O ponteiro **morre**, e o texto manda rodar o verbo — *um ponteiro a menos, não um
  ponteiro reapontado*, que é o que a `DB-43` e a `DB-50` vêm fazendo com o resto do módulo. A
  observação de conteúdo que o loop trouxe estava certa, e fica registrada como tal.

  **A varredura dos dez passos, pedida no mesmo ato (lição do `ESC-4`), achou uma lacuna e um
  literal envelhecido, e mais nada.** Conferidos um a um contra a árvore de 2026-09-20: passos 1–3
  não têm referente externo; passo 4 — o alvo `projeto` de `.claude/projecoes.json` tem `hooks` com
  **dois** ganchos (`PreToolUse`, `SubagentStop`), exatamente como o passo afirma, e o
  `UserPromptSubmit` que já existe vive no alvo `usuario`, sem colisão; passo 5 — `materializar.py
  drift` sai **0**; passo 6 — `## Parte 1 — Apurar a fila` (linha 24) e `## Parte 3 — Fechar a
  tarefa` (linha 142) existem, e **a lacuna é o inbox**: o `Objetivo` o nomeia e o passo não o
  cobria, deixando viva a ordem de drenar em prosa depois de o verbo `drain` existir; passo 7 —
  `### Passo 2` (linha 41) e `### Passo 9` (linha 140) existem; passo 8 — `GOVERNANCA.md:480` é
  exatamente o bullet `**Retomada sem tarefa nomeada**`; passo 9 — `CHANGELOG.md:17` é exatamente
  `## [Não lançado]`; passo 10 — sem referente. As **oito** baselines da `Verificação` foram
  re-rodadas e **todas conferem** (`False`, `0`, `0`, `0`, `2`, `0`, `3`, drift `0`). O único
  literal envelhecido é o piso de regressão — *suíte com 201 testes*, de 2026-09-19 —, re-medido em
  **218** e datado de hoje. Nenhum outro passo repete o defeito do passo 6.

### AE-34 — Estatística do acionamento `ESC-8` (`pantonic-consultant`, 2026-09-20)

Mesma residência e mesma forma do `AE-16`, `AE-18`, `AE-20`, `AE-22`, `AE-24`, `AE-28` e `AE-32`
(`docs/consultant-spec.md` §9).

- **O que motivou:** o passo 6 mandava criar ponteiro para uma seção que a skill de destino
  **declara não transcrever**, e o `Não fazer` do próprio card vedava criá-la. As três saídas
  produziam textos diferentes na skill viva, e escolher entre elas é decidir **onde a matéria
  normativa reside** — arquitetura de §2.x, não execução.
- **Classe do impedimento:** *ponteiro para residência que a residência recusa* — classe nova nesta
  série. Não é enumeração estagnada (`ESC-3`), nem alcance colidindo com restrição (`ESC-4`), nem
  efeito de segunda ordem (`ESC-5`), nem premissa invalidada por ato externo (`ESC-7`): aqui o
  referente **nunca existiu**, e não existia **por decisão anterior e correta**. O card herdou de
  `BKL-T8` (2026-09-15) uma frase escrita quando a partição de matéria entre skill e instrumento
  ainda não tinha sido feita. Classificada **técnico/tático**: a resposta sai da partição que a
  própria `diario-de-obras` já publicara, não muda escopo, rota nem entregável, e não requer ato do
  dono.
- **O que ficou inconclusivo:**
  - **O texto literal da skill ficou prescrito em sentido, não em letra.** O passo diz o que a
    seção passa a afirmar e qual verbo nomear; a redação final é do executor, dentro do estilo da
    skill. É deliberado — prescrever letra em arquivo de 301 linhas que não está nos olhos de quem
    decide é como nasceram os defeitos de referente desta série.
  - **A `Parte 1` da skill pode ter mais prosa de ordenação do que o item 2.** A varredura
    localizou as seções e a lacuna do inbox, não auditou as 301 linhas em busca de toda frase que
    reproduza heurística. O `Pronto quando` cobre isso por relação — *nenhuma das duas skills manda
    mais ler diário ou inbox para achar ou fechar tarefa* —, e a relação é verificável por leitura
    do diff, não por comando.
  - **Nenhum guarda impede ponteiro para seção inexistente.** Nem `check`, nem `card_check`, nem o
    gate de revisão confrontam `§<n>` citada num card com o arquivo que deveria contê-la. Fica
    nomeado, sem card — matéria transversal, proibida pelo critério (ii).

**Para a spec de robustez (`TK-55`), classe *derivado que erra sem sinal*, a evidência desta
passagem:** **a citação de seção é o único tipo de referência do kit que ninguém resolve.** Caminho
de arquivo tem `Test-Path`; id de tarefa tem `review_evidence`; literal de aceite tem `Select-String`
nos dois mundos. Mas `§2.5 publicada na skill X` atravessou a autoria da `BKL-T8`, a transcrição da
`BKL-T9a` — aprovada **100%** —, duas varreduras de consultor e um despacho, e só caiu quando um
executor foi **abrir o arquivo para editar**. A forma do defeito é a mesma do `AE-22`: o card cita um
referente, o referente não existe, e **a aparência do card é idêntica nos dois mundos**. A diferença
é que aqui nem o mundo que o card cria resolveria — a seção não ia passar a existir por efeito de
passo nenhum.

- **`AE-35` (2026-09-20, pendência do laudo da `BKL-T11`, roteada pelo `B1`) — o hook devolve
  **0 bytes** no ponto de carga real: `stdin` decodificado em `cp1252` e gatilho acentuado que
  não casa.** A entrega fechou **aprovada com ressalva, 91%**, bloqueante `nenhuma`, e o achado
  não a rebaixa — mas **o hook não funciona em produção como está**.

  **Fato medido (2026-09-20, `pantonic-reviewer`, exercitando o ponto de carga real):**
  `python .claude/tools/backlog_hook.py` com o payload de `UserPromptSubmit` em **UTF-8** sai com
  **0 bytes**, porque `sys.stdin.read()` decodifica em **`cp1252`** num host sem `PYTHONUTF8`, e a
  string `próximo passo` — acentuada — deixa de casar o literal do gatilho. **Com
  `PYTHONUTF8=1`, o mesmo payload devolve 9.913 bytes** de `additionalContext`. O defeito é de
  ambiente, não de lógica: o verbo `next` que o hook invoca funciona.

  **Por que passou pelos testes.** Os TF do módulo alimentam o hook por importação e por
  `tmp_path`, com strings já decodificadas em memória — o caminho que nunca exercitaram é
  `sys.stdin` **do processo real**, que é justamente onde a codificação do host entra. O reviewer
  só o encontrou porque rodou o executável no ponto de carga, e não o módulo em teste.

  **Precedente na própria árvore:** `modelo_por_fase_userpromptsubmit.py` já resolve o mesmo
  problema — é a referência de reparo que o laudo nomeia, e ela sugere as duas metades: ler
  `sys.stdin.buffer` como UTF-8 explícito **e/ou** normalizar acento na comparação do gatilho.

  **Por que é urgente, e não só correto:** a **`BKL-T12`** — última tarefa do plano — **mede o
  pickup em sessão nova** e publica o número na `## 15` do `CUSTO_DO_PICKUP.md`, contra os 77.457
  chars da `## 3` e o alvo de 40.000 da `## 6`. Com o hook mudo, essa medida sairia **zero** e
  seria publicada como fato. O reparo tem de entrar **antes** da `BKL-T12`.

  **Rota:** escalado ao consultor como `ESC-9` — card próprio antes da `BKL-T12`, ou emenda dela,
  com TF que exerça o **executável** e não só o módulo. Esta é a sétima ocorrência da mesma classe
  nesta janela — *o derivado cala onde deveria falar* — e a mais cara em consequência, porque o
  silêncio do hook seria lido como **medida** pela tarefa seguinte.


  **Resolvido pela `DB-52` (2026-09-20, `ESC-9`, `pantonic-consultant`).** O texto acima fica
  **literal**. Reproduzido no ato: **0** bytes sem `PYTHONUTF8`, **6.997** com ele.

  **A `e/ou` que esta entrada admite está errada, e a medida mostra por quê.** O texto
  mis-decodificado é `execute o prÃ³ximo passo`; normalizá-lo pelo `_norm` do precedente dá
  `execute o pra3ximo passo`, que **não** contém `proximo passo` — o `³` do `cp1252` decompõe em `3`
  sob NFKD. **Normalizar sozinho não conserta; decodificar sozinho conserta.** As duas metades
  entram, com papéis declarados: ler `sys.stdin.buffer` e decodificar UTF-8 explicitamente é o
  reparo; normalizar e escrever o gatilho sem acento é **ampliação**, para casar `proximo passo`,
  que um dono digita sem pensar e que hoje falha calado.

  **Residência: card próprio, `BKL-T11a`, antes da `BKL-T12`** — e a razão dirimente não é de tema,
  é de papel: **o card que mede não pode ser o card que conserta o que ele mede.** A aferição sairia
  do mesmo ato que produziu o sujeito dela.

  **A varredura da classe achou mais do que o card conserta.** Três entrypoints do kit leem `stdin`
  pelo mesmo padrão inseguro — `backlog_hook.py:72`, `ocupacao.py:141`, `telemetria_hook.py:213` —
  e só o primeiro quebra hoje, porque só ele compara literal acentuado. E **o precedente que este
  achado cita tem a mesma lacuna**: `modelo_por_fase_userpromptsubmit.py:101` também faz
  `sys.stdin.read()`, e o `_norm` dele não salva prompt acentuado mis-decodificado. Os dois únicos
  que acertam, por contraste, são `pytest_filter.py` (`reconfigure(encoding="utf-8")`) e
  `tail_filter.py` (`sys.stdin.buffer`). Nada disso vira card aqui: é matéria de outro plano.

  **Ordem do `drain` (`DB-49`, ponto re-fixado):** indiferente para o resultado — hook mudo não lê
  corpus, e `drain` não toca o hook. Fica fixada por propriedade: o `drain` é o **último ato antes
  da aferição**, depois do `BKL-T11a`, sem despacho de executor entre a drenagem e a medida.

### AE-36 — Estatística do acionamento `ESC-9` (`pantonic-consultant`, 2026-09-20)

Mesma residência e mesma forma do `AE-16`, `AE-18`, `AE-20`, `AE-22`, `AE-24`, `AE-28`, `AE-32` e
`AE-34` (`docs/consultant-spec.md` §9).

- **O que motivou:** o hook entregue e aprovado (91%) devolve **0 bytes** no ponto de carga real, e
  a tarefa seguinte — a última do plano — **mede o pickup e publica o número**. O silêncio seria
  lido como medida, e um zero ali, contra os 77.457 chars da `## 3` e o alvo de 40.000 da `## 6`,
  leria-se como sucesso espetacular.
- **Classe do impedimento:** *o teste exercita o módulo e o mundo exercita o processo* — classe nova
  nesta série. Não é enumeração, nem alcance, nem efeito de segunda ordem, nem premissa invalidada,
  nem ponteiro para residência que recusa: aqui a lógica está certa e **o invólucro não**. A
  fronteira que o card da `BKL-T11` desenhou com cuidado — *superfície testável separada do I/O de
  stdin* — é a mesma que pôs o I/O fora de teste. Classificada **técnico/tático**: o reparo é de
  quatro linhas em um arquivo do próprio plano, com precedente na árvore, sem mudar escopo, rota nem
  entregável, e sem ato do dono.
- **O que ficou inconclusivo:**
  - **Três entrypoints ficam com a lacuna aberta, e um deles é global.** `ocupacao.py` (PreToolUse,
    matcher `.*` — roda a cada chamada de ferramenta), `telemetria_hook.py` (SubagentStop) e
    `modelo_por_fase_userpromptsubmit.py` (o precedente). Os dois primeiros recebem mojibake sem
    falhar; o terceiro **degrada em silêncio** para prompt acentuado. Nenhum vira card aqui —
    matéria transversal —, e nenhum tem, hoje, quem o conserte.
  - **O `Pronto quando` do card pede um ato manual que nenhum comando cobre.** *Rodado à mão no
    ponto de carga, sem `PYTHONUTF8` no ambiente* — porque um teste que rode o subprocesso herda o
    ambiente do `pytest`, e não se pode afirmar por teste que o **host** está sem a variável. O TF
    prova o caminho; a conferência manual prova o ambiente.
  - **Não se mediu quantos outros pontos do kit comparam literal acentuado.** A varredura cobriu
    quem lê `stdin`; a classe irmã — *comparar string acentuada vinda de fora* — não foi varrida
    além desses arquivos.

**Completada pela `DB-53` (`ESC-10`, 2026-09-20) — leia-a antes de propagar.** A regra que esta
entrada enunciou — *teste que julga um executável roda o executável* — estava **incompleta**: um TF
por `subprocess.run` herda o ambiente do `pytest` e, num host com `PYTHONUTF8=1` exportado, passa
**com ou sem** o reparo. A forma completa tem três cláusulas (rodar o processo · fixar o ambiente
com `env=` explícito · exercer os dois mundos e afirmar a **invariância**) e está na `DB-53`, com a
assinatura medida que a confere. **Os três entrypoints nomeados abaixo só se corrigem com a regra
completa;** propagar a forma desta entrada multiplicaria por três um teste que não discrimina.

**Para a spec de robustez (`TK-55`): esta é a sétima ocorrência da classe *o derivado cala onde
deveria falar* nesta janela, e a mais cara em consequência.** As seis anteriores produziram silêncio
que **alguém** ainda precisava interpretar; esta produziria um **número**. O hook mudo devolve 0
bytes, exit 0, sem erro; a `BKL-T12` mediria esse zero, escreveria `0 chars` na `## 15` do
`CUSTO_DO_PICKUP.md` contra a linha de base de 77.457, e o plano fecharia declarando uma redução de
100% — com o dono dando veredito sobre um número que mede a **ausência do instrumento**, não o
instrumento. O que quebra a cadeia não é mais um guarda: é a regra que este card instala — **teste
que julga um executável roda o executável**. Registre-se junto o contraste medido: dos cinco
entrypoints do kit que leem `stdin`, **dois** acertam a codificação, e os dois que acertam são
justamente os que **não** têm teste — foram escritos por quem já tinha se queimado. O acerto veio de
cicatriz, não de norma, e é isso que a spec precisa converter em regra.

- **`AE-37` (2026-09-20, pendência do laudo da `BKL-T11a`, roteada pelo `B1`) — a regra que o card
  instala entra **incompleta**: teste por subprocesso que não fixa o ambiente pode passar pelo
  motivo errado.** A entrega fechou **aprovada com ressalva, 91%**, bloqueante `nenhuma`, e o
  reparo funciona — medido por mim no ponto de carga real, sem `PYTHONUTF8`: **9.676 bytes** com
  gatilho acentuado, **9.676** sem acento, **0** sem gatilho; os três eram **0** antes.

  **O achado é sobre a regra, não sobre o reparo.** *Teste que julga um executável roda o
  executável* resolve o buraco que deixou o defeito passar por um laudo de 91% — mas um TF por
  `subprocess.run` **herda o ambiente do `pytest`**. Num host com `PYTHONUTF8=1` exportado, o
  mesmo TF passa **com ou sem** o reparo: ele deixa de discriminar, e vira exatamente o tipo de
  verde que esta janela vem desmontando há nove escalonamentos.

  **Por que urge decidir agora:** o `AE-36` deixou **três entrypoints** com a mesma lacuna de
  codificação — `.claude/tools/ocupacao.py:141`, `.claude/tools/telemetria_hook.py:213` e
  `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py:101`, este último **global e usado por
  todos os projetos**. A regra vai ser **propagada** a eles. Propagá-la incompleta multiplica por
  três um teste que não discrimina.

  **O que falta é estreito e nomeado:** o TF tem de **fixar o ambiente do subprocesso**
  (`env` explícito, com `PYTHONUTF8` **ausente**), em vez de herdá-lo. O card já reconhecia
  metade disso ao pedir conferência manual do ambiente no `Pronto quando` — o que o laudo diz é
  que a conferência manual não escala para três propagações.

  **Rota:** escalado ao consultor como `ESC-10`, antes de qualquer propagação. Oitava ocorrência
  da classe *o derivado cala onde deveria falar* — e a primeira em que o silêncio previsto é de um
  **teste**, não de um instrumento.

  **Contraste medido pelo `ESC-9`, que pertence a este achado:** dos cinco entrypoints do kit que
  leem `stdin`, os **dois** que acertam a codificação — `pytest_filter.py` e `tail_filter.py` —
  são justamente os que **não têm teste**. Foram escritos por quem já tinha se queimado. O acerto
  veio de cicatriz, não de norma — e é a norma que esta rodada está tentando escrever.


  **Resolvido pela `DB-53` (2026-09-20, `ESC-10`, `pantonic-consultant`).** O texto acima fica
  **literal**. O achado está certo, e foi **medido** no ato: o hook **pré-reparo** devolve **0**
  bytes com `env={SYSTEMROOT, PATH}` e **59** com `PYTHONUTF8=1` acrescido — logo um TF que herda o
  ambiente passaria, num host que exporte a variável, **com ou sem** o reparo.

  **A decisão separa duas coisas que o achado une: a regra e o arquivo de teste.** O que urge é a
  **regra**, porque a propagação aos três entrypoints acontece **fora** deste plano; o arquivo de
  teste não urge, porque dentro do `P-0739` não se escreve mais teste nenhum — resta a `BKL-T12`,
  `Opus + dono`, classe `redacao`. Completar a regra custa uma decisão e protege as três
  propagações. Emendar o TF custaria **retroação em card `done`** (contra a `DB-23`), com card, RDO
  e laudo dessincronizados, por um risco que **não se materializa aqui**. A regra se completa
  **agora**; a emenda do TF é **pós-plano**.

  **A forma completa é mais forte do que o laudo pediu.** O laudo pede `env=` explícito com
  `PYTHONUTF8` ausente — a cláusula 2. Faltava a **3**: *exercer os dois mundos e afirmar a
  invariância*. Medido: o hook **reparado** devolve **7.123** bytes com e sem a variável — **iguais**
  —, e o quebrado devolve **0** e **59** — diferentes. A invariância **é** a asserção, e ela não
  depende de qual mundo o host habita. É a mesma disciplina de dois mundos que o critério (xii)(b)
  da rubrica já exige de linha de aceite, aplicada ao teste.

  **Onde a matéria fica, para que quem propagar tropece antes de propagar:** a `DB-53` é a norma; o
  `AE-36` — entrada que nomeia os três entrypoints e por onde um propagador entra — recebeu apenso
  apontando para ela; e a emenda do TF entra na fila do `TK-55` por ato do `scrum-master`, que é
  quem escreve o diário. Armadilha prática registrada junto, porque é o que reintroduziria o
  defeito: em Windows o subprocesso sobe com `env={}` e com `{SYSTEMROOT, PATH}` — copiar
  `os.environ` por preguiça é o caminho de volta.

### AE-38 — Estatística do acionamento `ESC-10` (`pantonic-consultant`, 2026-09-20)

Mesma residência e mesma forma do `AE-16`, `AE-18`, `AE-20`, `AE-22`, `AE-24`, `AE-28`, `AE-32`,
`AE-34` e `AE-36` (`docs/consultant-spec.md` §9).

- **O que motivou:** a **regra** que o `BKL-T11a` instalou entrou incompleta, e o `AE-36` a
  propagaria a três entrypoints — um deles **global**, usado por todos os projetos. O reparo do card
  funciona e foi medido pelo loop; o que não funciona é o **teste que o julga**, num host que exporte
  `PYTHONUTF8`.
- **Classe do impedimento:** *dívida de norma prestes a ser multiplicada* — classe nova, e a
  primeira desta série em que o impedimento **não bloqueia tarefa nenhuma**. Nada no `P-0739` para
  por causa dela: o plano fecharia igual, com o defeito latente saindo pela porta dentro de uma
  lição. O loop trouxe a pergunta certa — *reparo certo no momento errado?* — e trouxe junto o
  contrapeso, pedindo que a proximidade do fim não decidisse sozinha. Classificada
  **técnico/tático**: a resposta é uma decisão de norma dentro do próprio plano, sem card, sem
  retroação, sem mudar escopo, rota ou entregável, e sem ato do dono.
- **O que ficou inconclusivo:**
  - **O TF do `BKL-T11a` continua herdando o ambiente, e isso é deliberado.** Ele discrimina neste
    host — onde `PYTHONUTF8` não existe — e deixaria de discriminar noutro. Fica como está por
    `DB-23`, e a emenda depende de alguém tocar `tests/test_backlog.py` de novo, o que este plano
    não fará.
  - **A regra não tem residência normativa no kit.** `DB-53` é decisão **de plano**; a casa dela
    seria a `RUBRICA_DE_REVISAO.md` §8, ao lado dos dezoito critérios de autoria. Publicá-la lá é
    matéria transversal, proibida pelo critério (ii), e não foi aberta.
  - **A varredura da classe irmã segue sem fazer.** *Teste por subprocesso que herda ambiente* pode
    existir noutros pontos de `tests/`; mediu-se o que o `BKL-T11a` criou, não o repositório.
  - **Os três entrypoints continuam quebrados**, e agora com a regra completa esperando por eles —
    o que é melhor do que antes e ainda não é conserto.

**Para a spec de robustez (`TK-55`), oitava ocorrência da classe — e a primeira em que o silêncio
previsto é de um teste, não de um instrumento.** As sete anteriores tinham o mesmo formato: o
derivado devolve sucesso e a ausência de sinal é lida como saúde. Aqui o derivado é o **verde do
teste**, que é o sinal em que todo o resto se apoia — e o modo de falha é o mais difícil de ver de
todos, porque um teste que passa pelo motivo errado é indistinguível de um teste que passa. A
observação que o `ESC-9` mediu fecha o argumento e pertence a esta entrada: **dos cinco entrypoints
do kit que leem `stdin`, os dois que acertam a codificação são exatamente os dois que não têm
teste.** Foram escritos por quem já tinha se queimado. O acerto veio de **cicatriz, não de norma** —
e uma cicatriz não se propaga: ela morre com quem a tem. É isso que a `DB-53` existe para converter,
e é por isso que completá-la valia uma passagem inteira a uma tarefa do fim do plano.

- **`AE-39` (2026-09-20, ato de orquestração do `scrum-master`) — o `drain` correu em produção
  pela primeira vez, e a conferência bateu item por item com a simulação.** Executado no ponto
  prescrito pela `DB-49`/`DB-52`: depois do `BKL-T11a`, **imediatamente antes** da `BKL-T12`, sem
  nada entre a drenagem e a aferção.

  **Medido — antes:** `_INBOX.md` com **1** linha viva, **0** ocorrências de `P-0741-MC` no índice,
  `_INBOX_HISTORICO.md` com **2** linhas drenadas. **Depois:** `exit 0` nomeando os **três**
  arquivos; `_INBOX.md` com **0** linhas vivas; histórico com **3**; a linha
  `| P-0741-MC | O modelo conceitual do plano: a interface entre o dono e o loop | ready | docs/plans/P-0741-modelo-conceitual.md |`
  no índice — **exatamente** a que o `ESC-7` previra em cópia, campo por campo; `check` **exit 0**;
  rodapé de `next` em `inbox de planos: 0 por drenar`. **Todos os sete verbos do instrumento
  correram agora em produção.**

  **A armadilha do contador confirmou-se, e foi corrigida no mesmo ato.** O
  `**Próximo id de plano:**` ficou em `P-0742` **depois** do `drain`, com
  `docs/plans/P-0742-loop-fora-do-llm.md` **já existindo** — o `P-0742` nasceu sem linha de inbox,
  então o `max(id visto) + 1` nunca o alcançou, e `check` não acusa. Conferido o maior id da
  árvore por varredura de `docs/plans/P-*.md` (**742**), o contador foi corrigido para **`P-0743`**.
  Não é defeito do `drain`: ele computa sobre o que o inbox viu, e o que nunca passou pelo inbox
  lhe é invisível. **Guarda inexistente** — nada confronta o contador com `docs/plans/` —, e
  matria pós-plano.

  **Nota de procedência:** a linha drenada é do **dono**, registrada por sessão paralela dele
  (Controle 1.1). O `drain` a projetou **verbatim**, sem escolher nada — é o que a `DB-49`
  sustentava ao classificar o ato como orquestração e não como composição de backlog.

- **`AE-40` (2026-09-20, pendência do laudo da `BKL-T12`) — a última tarefa fica em `review`, e
  não em `done`, porque o card diz que ela não fecha sem o veredito do dono.** Entrega dos passos
  1–5 **aprovada com ressalva, 88%**, bloqueante `nenhuma`.

  **Por que o RDO não foi fechado e o laudo não foi consumido.** A `A8a` manda fechar o RDO pelo
  veredito transcrito, e a regra pressupõe que a tarefa **fecha**. Esta não fecha: o cabeçalho é
  `Opus + dono`, o passo 6 manda *apresentar o espelho ao dono e registrar o veredito dele*
  (`DB-20`), e o aceite diz literalmente que a entrega **não fecha sem ele**. Fechar o RDO agora
  seria registrar como concluída uma tarefa cujo último passo prescrito não ocorreu. O laudo fica
  **preservado**, contra o hábito da `DP-K` §14.4, porque ele ainda **não foi consumido** — e
  será, no ato em que o dono der o veredito.

  **Duas lacunas, e são de naturezas diferentes:**
  - **O veredito do dono (passo 6)** — prescrito pelo card, colhido no relatório de encerramento
    da janela. Não é impedimento: é a última etapa do desenho.
  - **A metade `usage_1` do método `DC-4`** — **não observável de dentro de um subagente**: exige
    uma janela principal recém-aberta. O executor **não a estimou, não a deduziu e não a inventou**;
    declarou-a como lacuna explícita na `## 14`, sem valor. Conduta correta, e o risco evitado era
    concreto — número inventado ali seria publicado como fato num documento que o dono usa para
    decidir.

  **O que ficou medido, e está no espelho:** saída do hook **7.079 chars / 7.080 bytes**, pickup
  composto **26.760 chars** — **−65,5%** contra os **77.457** da `## 3`, e **66,9%** do alvo de
  **40.000** da `## 6`. `V1`–`V5` = 1/1/1/exit 0/3; suíte **224 passed**; `check` exit 0; `next`
  seleciona; `**Fila corrente:**` viva; ratchet exit 0.

  **Nota sobre os dois números do hook, porque ambos aparecem no registro desta janela:** o
  `scrum-master` mediu **9.676 bytes** ao conferir o `BKL-T11a`; o executor mediu **7.079 chars** ao
  redigir o espelho. **Os dois estão certos nos seus momentos** — entre uma medida e outra correu
  o `drain` (`AE-39`), que mudou o estado do diário e, com ele, a saída do hook. O que vale para a
  `## 15` é o segundo, **datado**; o primeiro fica como registro de que a medida do pickup é
  função do corpus e envelhece a cada ato que o altera — razão pela qual a `DB-52` mandou o
  `drain` ser o último ato antes da aferção.

  **Achado fora de escopo, com rota:** `docs/DOC_MAP.md` declara `~431 linhas` para
  `docs/CUSTO_DO_PICKUP.md`, que agora tem **464**. Matéria de manutenção do mapa, sem card.

