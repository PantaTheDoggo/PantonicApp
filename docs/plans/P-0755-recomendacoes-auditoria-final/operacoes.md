# Operações — Aplicação das recomendações da auditoria final do kit

## Abertura

**O problema:** a auditoria final de 2026-09-28 (`docs/audits/AUDITORIA_FINAL_KIT.md`) mediu o kit
executando um plano fictício ponta a ponta contra o kit real. A sessão principal reenviava 285,6 mil
tokens de contexto por turno no loop de execução e 485,6 mil por turno na sonda da própria auditoria,
porque planejamento, loop e auditoria corriam sempre na mesma janela. O planejamento sozinho consumiu
352,2 dos 1.250,0 mil tokens gastos em subagentes do plano fictício (≈28%) para produzir 5 arquivos. O
gatilho de próximo passo injetou 15,3 KB do mesmo card três vezes numa única janela, porque casava
também no relato que um subagente devolve, não só na mensagem do dono. A rodada de replanejamento não
tinha onde gravar a medida que prova o antes e o depois de um card reescrito. E um card podia copiar,
no campo que cita uma operação do modelo, um texto diferente do texto vigente daquela operação, sem que
a conferência (`modelo.py check`) acusasse nada — o defeito que os registros 36 e 37 do relatório
descrevem.

**A solução, em uma frase:** as 31 recomendações da auditoria (`R-01`..`R-31`, exceto a `R-29`,
registrada sem ação) viraram instrumento, teste e doutrina em cinco etapas — o que era leitura e cópia
manual da sessão principal vira comando do kit, e o que era falha registrada sem guarda vira caso
coberto por teste.

| termo | o que é |
|---|---|
| card | a tarefa do plano — um bloco fechado com objetivo, arquivos-alvo e verificação, que materializa uma operação do modelo de domínio do plano |
| marco | ponto da execução em que a janela para e o dono dá o veredito antes de a etapa seguinte começar |
| versão pendente (`## 1A`) | rascunho de mudança do modelo de domínio do plano, ao lado da versão vigente (`## 1`), até o dono aceitar ou recusar essa mudança no marco |
| drift | a diferença que a conferência do modelo mostra entre a versão vigente e a versão pendente |
| consultor | papel que examina um achado ou a parada de um card e decide a rota a seguir, sem parar a janela de execução |
| laudo | o veredito calculado que o revisor emite sobre a entrega de um card |
| achado (`AE-<n>`) | registro numerado de um defeito encontrado na execução, roteado pelo consultor |
| instrumento | o comando ou hook do kit que a doutrina (a prosa de uma skill ou de um agente) manda usar |

## O arco

| estrato | pergunta que responde | tarefas |
|---|---|---|
| A — o custo da orquestração | Como o gerente do loop deixa de carregar, em cada turno, o peso do planejamento, da auditoria e do card colado inteiro na conversa? | `RAF-T1`, `RAF-T1a`, `RAF-T2`, `RAF-T3`, `RAF-T3a`, `RAF-T4`, `RAF-T4a`, `RAF-T5`, `RAF-T6`, `RAF-T6a` |
| B — os instrumentos de revisão e medida | Como a evidência que o revisor lê chega ao fim nos casos em que hoje quebra, sem perder linha de teste removida nem confundir o mundo antes com o depois? | `RAF-T7`, `RAF-T7a`, `RAF-T8`, `RAF-T8a`, `RAF-T9`, `RAF-T9a`, `RAF-T10`, `RAF-T10a`, `RAF-T11`, `RAF-T11a`, `RAF-T12`, `RAF-T12a`, `RAF-T13`, `RAF-T13a`, `RAF-T14`, `RAF-T15`, `RAF-T16`, `RAF-T17`, `RAF-T18` |
| C — modelo, card e versão | Como um card fica preso ao texto certo da operação do modelo que ele cita, mesmo com uma versão pendente em curso, e como essa versão se promove sem gastar outra instância do modelador? | `RAF-T19`, `RAF-T19a`, `RAF-T20`, `RAF-T21`, `RAF-T22`, `RAF-T23`, `RAF-T23a`, `RAF-T23b`, `RAF-T24`, `RAF-T24a`, `RAF-T25`, `RAF-T26`, `RAF-T26a` |
| D — backlog, fechamento e telemetria | Como o fechamento de uma tarefa registra achado, falha de instrumento e linha de telemetria sem lacuna nem duplicata? | `RAF-T27`, `RAF-T27a`, `RAF-T28`, `RAF-T29`, `RAF-T29a`, `RAF-T30`, `RAF-T30a`, `RAF-T31`, `RAF-T31a`, `RAF-T31b`, `RAF-T32`, `RAF-T32a`, `RAF-T33`, `RAF-T34`, `RAF-T35` |
| E — doutrina do planejador e comunicação | Como o planejador dosa o esforço pelo tamanho do plano, larga exigência que o modelador já recusa, e como a mensagem ao dono nomeia o que ele já pediu? | `RAF-T36`, `RAF-T37`, `RAF-T38`, `RAF-T39`, `RAF-T39a`, `RAF-T40` |

Fora do estrato: `RAF-T22a` é corretivo da `OP-19`..`OP-22` (a mesma diferença entre versões do
estrato C — mostra operação cujo `precisa de:` ou `altera:` mudou sem mudar o texto), mas a emenda que
ela corrige só chegou depois do gate da etapa E (`RAF-T36`); por isso corre na janela dessa etapa e
está descrita, abaixo, na posição em que a `## 1` do modelo a lista.

| tarefa | título | status |
|---|---|---|
| `RAF-T1` | O loop de plano recém-planejado abre em janela nova | done |
| `RAF-T1a` | O campo Janela do Passo 1 fica irmão dos outros campos do passo | done |
| `RAF-T2` | O medidor de custo da sessão vira comando do kit | done |
| `RAF-T3` | O despacho grava o pacote da tarefa e imprime só o recado ao executor | done |
| `RAF-T3a` | O pacote do despacho marca ausente só a linha citada que sumiu | done |
| `RAF-T4` | Quem conduz repassa o texto pronto do despacho e não reconfere âncora | done |
| `RAF-T4a` | O gate de delegação e a entrada do Passo 4 deixam de mandar re-derivar e copiar | done |
| `RAF-T5` | O gatilho do próximo passo responde só ao dono | done |
| `RAF-T6` | O filtro do pytest devolve o exit dos testes no comando encadeado | done |
| `RAF-T6a` | O filtro do pytest alcança o comando encadeado por OU lógico e por quebra de linha | done |
| `RAF-T7` | O dossiê de evidência chega ao fim nos três casos em que quebrava | done |
| `RAF-T7a` | O ramo que o conteúdo antigo não texto nunca alcança sai do dossiê de evidência | done |
| `RAF-T8` | O binário novo leva a marca de novo e o registro da orquestração tem um nome só | done |
| `RAF-T8a` | A rubrica nomeia o rótulo do registro da orquestração | done |
| `RAF-T9` | O curinga do alvo casa como na linha de comando | done |
| `RAF-T9a` | O teste do curinga da AUF-T3 nomeia o mecanismo que casa o alvo | done |
| `RAF-T10` | O caminho acentuado chega inteiro ao dossiê de evidência | done |
| `RAF-T10a` | O arquivo acentuado já rastreado chega com um nome só ao dossiê de evidência | done |
| `RAF-T11` | A evidência mostra as linhas que a entrega tirou dos testes | done |
| `RAF-T11a` | A seção das linhas removidas cobre o teste sob curinga ou diretório e a linha que começa por dois hífens | done |
| `RAF-T12` | A rubrica reprova a asserção de teste removida sem ordem do card | done |
| `RAF-T12a` | A dimensão testes declara a fonte mista e o instrumento cita a rubrica pela seção | done |
| `RAF-T13` | A conferência do card compara o depois com o esperado e lê o literal com pontuação | done |
| `RAF-T13a` | O docstring do módulo e a ajuda de --mundo da conferência do card dizem o mundo depois da forma 8.1 | done |
| `RAF-T14` | A conferência do card roda o git de leitura contra o recorte do despacho | done |
| `RAF-T15` | A medida gravada fica na pasta do plano da árvore medida, com o momento no nome | done |
| `RAF-T16` | O planejador mede o antes do card dependente na cópia com os anteriores aplicados | done |
| `RAF-T17` | O planejador discrimina o card que deixa o alvo igual pela invariância | done |
| `RAF-T18` | A rodada de replanejamento grava a medida dos dois mundos | done |
| `RAF-T19` | A conferência do modelo julga só a versão vigente quando pedida | done |
| `RAF-T19a` | O teste distingue o check com e sem --so-vigente pela versão pendente fora de sequência | done |
| `RAF-T20` | O despacho pede à conferência do modelo só a versão vigente | done |
| `RAF-T21` | A conferência do modelo recusa o card que copia a operação com outro texto | done |
| `RAF-T22` | A diferença entre versões mostra a operação inserida, a renumerada e a propriedade nova | done |
| `RAF-T22a` | A diferença entre versões mostra a operação que muda o que precisa ou o que altera sem mudar o texto | done |
| `RAF-T23` | O comando do marco promove a versão aceita e cobra a validação do consultor | done |
| `RAF-T23a` | O comando do marco reconhece a versão pendente pela mesma regra do modelo.py | done |
| `RAF-T23b` | O dossiê do comando do marco pede ao modelador o que ele de fato devolve, no conflito e na recusa | done |
| `RAF-T24` | Quem conduz segue a janela quando o modelador cria operação nova e enfileira a rodada | done |
| `RAF-T24a` | Quem conduz dá destino, no marco, ao card da operação nova que a rodada deixou bloqueado | done |
| `RAF-T25` | O planejador escreve, na rodada que segue a emenda, o card da operação nova bloqueado até o marco | done |
| `RAF-T26` | O modelador sai da promoção de versão e o consultor ganha a forma da linha de validação | done |
| `RAF-T26a` | O modelador conhece os quatro conflitos da promoção e devolve o que o dossiê pede | done |
| `RAF-T27` | O pré-voo separa o caminho a criar do que já devia existir e não toma extensão solta por caminho | done |
| `RAF-T27a` | O docstring do módulo do pré-voo diz o que conta como caminho e quando o caminho sai a criar | done |
| `RAF-T28` | O controle do backlog avisa, ao drenar, a diretiva que não cita nada vivo | done |
| `RAF-T29` | O controle do backlog recusa o prefixo de decisão que outro plano já declarou | done |
| `RAF-T29a` | O cabeçalho do controle do backlog conta o vocabulário do check até C-18 | done |
| `RAF-T30` | O fechamento de tarefa registra o achado pela linha de origem e avisa a falha de instrumento | done |
| `RAF-T30a` | O laudo aceita o alvo instrumento que o aviso do fechamento lê | done |
| `RAF-T31` | A série de telemetria atribui pela linha de abertura do despacho e guarda uma linha por agente | done |
| `RAF-T31a` | O escritor da série de telemetria diz nos docstrings quem recusa a linha repetida e que a linha do agente se troca | done |
| `RAF-T31b` | O primeiro parágrafo do docstring e o help do append da série de telemetria ressalvam o --agente | done |
| `RAF-T32` | O painel do gerente mostra a tarefa que a linha de abertura do despacho declara | done |
| `RAF-T32a` | O painel do gerente mostra a tarefa despachada também no retorno por hand-back | done |
| `RAF-T33` | A norma de consumo manda todo despacho de subagente abrir com a linha que declara plano e tarefa | done |
| `RAF-T34` | Quem conduz leva ao consultor a falha de instrumento que o fechamento avisa e a linha do card em triagem | done |
| `RAF-T35` | O consultor cita no achado a linha do laudo de onde ele veio | done |
| `RAF-T36` | O planejador ganha a régua de profundidade pelo tamanho do plano | done |
| `RAF-T37` | O pedido do planejador ao modelador deixa de exigir caminho, linha e nome de comando | done |
| `RAF-T38` | Quem conduz roda a checagem de versão do kit antes do planejador, que a registra no cabeçalho | done |
| `RAF-T39` | A mensagem de marco abre nomeando a entrega e o pedido do dono que a originou | done |
| `RAF-T39a` | A abertura de marco nomeia a etapa, e o primeiro parágrafo do relatório remete a ela | done |
| `RAF-T40` | O guia de entrada descreve o kit como ele fica depois das cinco etapas | done |

## `RAF-T1` — O loop de plano recém-planejado abre em janela nova

**Contexto que a motivou:** a auditoria mediu que a sessão principal reenviava 285,6 mil tokens por
turno porque planejamento, loop de execução e auditoria corriam na mesma janela (`R-01`, registro 9 do
relatório).

**O que é o artefato:** doutrina, não código — o Passo 1 de `.claude/skills/scrum-master/SKILL.md`
ganha o campo `- **Janela:**` (a redação exata desse campo foi corrigida pela `RAF-T1a`, ver abaixo).

**Como funciona na prática:** o gatilho é o dono aprovar o plano no marco de modelo (Marco 1); quem
conduz encerra o relatório dessa janela e não despacha nela a primeira tarefa; o dono abre uma janela
nova, e ali o loop começa lendo só o plano gravado. Verificação real (contagem de string no arquivo):
`janela-nova=0` antes, `janela-nova=1` depois.

**Protege contra:** o custo composto de carregar planejamento, loop e auditoria na mesma janela — os
285,6 mil tokens por turno medidos.

## `RAF-T1a` — O campo Janela do Passo 1 fica irmão dos outros campos do passo

**Contexto que a motivou:** o laudo da `RAF-T1` (ressalva 88%) achou que a instrução de recuo do card
("cada linha perde os dois espaços do recuo deste card") produziu um bloco recuado 3 espaços em vez de
0 — o campo `- **Janela:**` nasceu como sub-item aninhado do bullet `- **Ação:**`, não como campo irmão
de `Gatilho`/`Entrada`/`Ação`/`Saída`.

**O que é o artefato:** o mesmo campo da `RAF-T1`, em `.claude/skills/scrum-master/SKILL.md` — correção
de recuo, sem mudar o texto do campo.

**Como funciona na prática:** a Verificação passa a medir o literal junto com a linha anterior, para
discriminar a coluna, e confirma que o texto do campo não mudou (invariância). Antes `coluna0=0
aninhado=1`; depois `coluna0=1 aninhado=0`.

**Protege contra:** instrução de recuo relativa ("perde N espaços") aplicada dentro de um bloco já
recuado, que o `card_check` não discrimina porque não mede indentação — lição registrada na decisão
`DRF-43`.

## `RAF-T2` — O medidor de custo da sessão vira comando do kit

**Contexto que a motivou:** sem instrumento, não havia como medir, no próximo loop, se o custo por
turno de fato caiu depois da `RAF-T1`.

**O que é o artefato:** `.claude/tools/custo_sessao.py`, dois verbos — `medir <transcript.jsonl>
<saida.tsv>` e `passos <saida.tsv> <regex_inicio> <regex_fim>` —, só biblioteca padrão; teste
`tests/test_custo_sessao.py`.

**Como funciona na prática:** gatilho é quem conduz rodar o comando sobre o transcript da janela;
entrada é o JSONL da conversa; o processamento lê a linha `despachar ([A-Z]+-T\d+[a-z]?|TK-\d+)` para
atribuir turnos a tarefas; saída é um TSV com tokens por turno e por passo do loop, e janela sem
despacho imprime `por tarefa: n=0`, saindo 0. Verificação real: `pytest -k medir` e `-k passos`, exit
4→0 nos dois.

**Protege contra:** custo evitável não medido — sem instrumento, "o loop ficou mais barato" seria
opinião, não número.

## `RAF-T3` — O despacho grava o pacote da tarefa e imprime só o recado ao executor

**Contexto que a motivou:** no loop real medido pela auditoria, cada despacho colava 3,06 mil tokens de
saída na tela de quem conduz, e 23 turnos da janela foram gastos re-derivando âncora (`arquivo:linha`)
à mão.

**O que é o artefato:** `.claude/tools/backlog.py despachar <ID>`, que grava card, handovers, a saída
do `modelo.py show` e as âncoras conferidas num arquivo `<pasta-do-plano>/despacho/<ID>.md` (ou
`docs/RDO/despacho/<ID>.md` para plano legado ou tíquete), e grava `ref=<sha>` em
`.claude/estado/tarefa-corrente.json`; `.gitignore` ganha a pasta `despacho/`.

**Como funciona na prática:** o gatilho é `despachar <ID>`; a saída na tela passa a ser só a linha
`=== DESPACHO: <ID> — <título>`, o caminho do arquivo e a linha `ref=`. Verificação real: `pytest -k
pacote`, `-k texto_pronto` e `-k confere_as_ancoras`, todos exit 5→0.

**Protege contra:** o custo de colar o card inteiro na conversa (3,06 mil tokens por despacho) e o de
re-derivar âncora à mão (23 turnos medidos).

## `RAF-T3a` — O pacote do despacho marca ausente só a linha citada que sumiu

**Contexto que a motivou:** o laudo da `RAF-T3` (ressalva 91%) mediu, sobre os 41 cards do próprio
`P-0755`, 573 falsos `âncora ausente` em 1.066 linhas — a regra tomava por âncora qualquer trecho entre
crases, inclusive nome de comando e rótulo de campo que nunca estiveram no arquivo.

**O que é o artefato:** a mesma função de conferência de âncoras em `.claude/tools/backlog.py`.

**Como funciona na prática:** passa a ler só os bullets `- **<Rótulo>:**` de coluna 0 dos campos
`Passos` e `Contratos/classes`, pula trecho com menos de 4 caracteres e o que já é um dos
`Arquivos-alvo`, e só marca `âncora ausente` a linha citada (`caminho:n`) que não existe mais e o texto
citado logo depois dela que não está no arquivo. Verificação real: a regra nova, sobre os mesmos 41
cards, sai com 501 linhas e 0 `âncora ausente` (contra 1.066 linhas e 573 falsos positivos da regra
anterior).

**Protege contra:** ruído que afogaria o pacote de despacho — um falso positivo a cada duas linhas do
pacote, na regra anterior.

## `RAF-T4` — Quem conduz repassa o texto pronto do despacho e não reconfere âncora

**Contexto que a motivou:** a doutrina da skill ainda mandava colar o card e o handover na conversa e
reconferir âncora à mão, duplicando o que o instrumento da `RAF-T3` já resolveu.

**O que é o artefato:** Passos 3 e 4 de `.claude/skills/scrum-master/SKILL.md`.

**Como funciona na prática:** o Passo 3 passa a rodar `despachar` e usar a saída dele; o Passo 4 usa
esse texto pronto como `Entrada`, sem copiar card ou handover e sem reconferir âncora. Verificação
real: `entrega=1-0` (frase antiga presente) → `0-1` (frase nova); `ancoras=1-0` → `0-1`.

**Protege contra:** o mesmo custo de cópia e re-derivação que a `RAF-T3` fechou no instrumento, se a
doutrina continuasse mandando fazer à mão o que o comando já faz.

## `RAF-T4a` — O gate de delegação e a entrada do Passo 4 deixam de mandar re-derivar e copiar

**Contexto que a motivou:** o consultor (achado `AE-126`, varredura de "re-derivad" e "copiado do
plano" em `.claude/`) achou que a `RAF-T4` não alcançou o item 3 do gate de delegação da skill
`passagem-de-bastao` — que o Passo 3 da `scrum-master` manda rodar antes do `despachar` — nem a
`Entrada` do Passo 4, que ainda dizia "dossiê da tarefa copiado do plano".

**O que é o artefato:** `.claude/skills/passagem-de-bastao/SKILL.md` (item 3 do gate) e
`.claude/skills/scrum-master/SKILL.md` (entrada do Passo 4); a `scrum-master` volta também ao fim de
linha LF que o `.gitattributes` declara.

**Como funciona na prática:** o gate deixa de mandar colar âncoras re-derivadas para tarefa de plano (só
a de tíquete, despachada à mão, ainda re-deriva); a `Entrada` do Passo 4 passa a ser o texto pronto do
`despachar`. Verificação real: `gate=1-0`→`0-1`; `entrada=1-0`→`0-1`; contagem de `\r` (CRLF)
`cr=0-445`→`0-0`.

**Protege contra:** a mesma regra reincidindo em pontos que uma varredura por nome de arquivo não
alcança — a `RAF-T4` havia afirmado "nenhum outro arquivo a repete" sem essa varredura.

## `RAF-T5` — O gatilho do próximo passo responde só ao dono

**Contexto que a motivou:** a auditoria (registro 42) mediu o hook `backlog_hook.py` casando o texto
"Próximo passo de quem conduz" dentro de relatórios de subagente e injetando 15,3 KB do card `next` três
vezes na mesma janela.

**O que é o artefato:** `.claude/tools/backlog_hook.py`; teste novo `tests/test_backlog_hook.py`.

**Como funciona na prática:** o hook, que roda a cada `UserPromptSubmit`, deixa de injetar quando o
prompt, depois de `lstrip()`, começa por `<agent-message` ou por `[SYSTEM NOTIFICATION` — ou seja,
quando quem "fala" não é o dono. Verificação real: suíte nova, exit 4→0.

**Protege contra:** injeção repetida de conteúdo pesado (15,3 KB × 3) disparada pelo próprio texto que o
kit produz, não pelo dono.

## `RAF-T6` — O filtro do pytest devolve o exit dos testes no comando encadeado

**Contexto que a motivou:** a auditoria (registro 45) mediu que `cd … && pytest …; echo "exit=$?"`
devolvia o exit do filtro (o script que reescreve a saída), não o dos testes — um `pytest` que falhou
podia sair como se tivesse passado.

**O que é o artefato:** `.claude/global/hooks/pytest_pretooluse.py` (reescreve só o segmento do
`pytest` dentro do comando encadeado) e `.claude/global/hooks/pytest_filter.py` (consome o marcador);
teste novo `tests/test_pytest_pretooluse.py`.

**Como funciona na prática:** o hook envolve o segmento do pytest para emitir, depois da saída normal, a
linha `__PYTEST_EXIT__=<exit>`; o filtro lê essa linha, não a imprime, e sai com esse código. A
projeção para `~/.claude/hooks/`, onde o hook de fato roda nas sessões, é ato do dono, fora do plano.
Verificação real: suíte nova, exit 4→0.

**Protege contra:** um teste que quebrou saindo mascarado de "passou", porque o exit final era o do
filtro, não o da suíte.

## `RAF-T6a` — O filtro do pytest alcança o comando encadeado por OU lógico e por quebra de linha

**Contexto que a motivou:** o laudo da `RAF-T6` (ressalva 91%) e a medida do consultor acharam que
`pytest -q || echo falhou`, `false || pytest -q` e `cd x` seguido de quebra de linha e `pytest -q`
continuavam saindo sem filtro — o hook lia `||` como metade de pipe simples, e o pré-filtro não achava o
pytest depois de `||` nem de quebra de linha.

**O que é o artefato:** o mesmo `.claude/global/hooks/pytest_pretooluse.py`.

**Como funciona na prática:** o hook passa a recusar por pipe só o `|` que não é metade de `||`, e o
pré-filtro passa a achar o pytest também depois de `||` e de quebra de linha. Verificação real: os dois
casos que falhavam antes (`2 failed` na suíte reproduzida) passam a `8 passed` depois; os cinco
passthroughs de `main()` seguem inalterados.

**Protege contra:** o mesmo mascaramento de exit da `RAF-T6`, nos dois padrões de encadeamento que a
primeira correção não cobria.

## `RAF-T7` — O dossiê de evidência chega ao fim nos três casos em que quebrava

**Contexto que a motivou:** a auditoria (registros 25 e 26; `AE-105`, `AE-106` do `P-0754`) mediu
`review_evidence.py` caindo com `AttributeError` quando o conteúdo antigo (no `<ref>`) não decodifica
como texto e o de hoje decodifica, e com traceback cru quando `--atribuir` roda sem `rdo.py` na raiz, ou
quando `--out` procura a medida só ao lado do próprio `--out`.

**O que é o artefato:** `.claude/tools/review_evidence.py`; teste `tests/test_review_evidence.py -k
quebra`.

**Como funciona na prática:** no ramo texto, quando o `<ref>` não decodifica, o instrumento compara
bytes em vez de cair; os dois pontos que carregam o `rdo.py` do `--atribuir` entram no mesmo bloco
protegido, e a ausência sai como mensagem nomeada (`review_evidence: FALHOU - rdo.py: módulo não
encontrado em '<caminho>'`, exit 1); com `--out`, a medida ausente passa a ser procurada também na pasta
do plano. Verificação real: exit 5→0.

**Protege contra:** o dossiê de evidência — o material que o revisor lê para julgar qualquer card —
quebrar antes de terminar.

## `RAF-T7a` — O ramo que o conteúdo antigo não texto nunca alcança sai do dossiê de evidência

**Contexto que a motivou:** o laudo da `RAF-T7` (ressalva 91%) achou que, no ramo em que o `ref` não
decodifica e o de hoje decodifica, os bytes de hoje (UTF-8 válido) nunca podem ser iguais aos do `ref`
(inválidos) — duas comparações de bytes que a `RAF-T7` acrescentou ficaram mortas: uma guardava um
retorno inalcançável, a outra era sempre verdadeira.

**O que é o artefato:** o mesmo `.claude/tools/review_evidence.py`, função `_bytes_do_ref`.

**Como funciona na prática:** as duas comparações saem do código (inspeção mecânica, sem teste novo).
Verificação real: ocorrências de `_bytes_do_ref(` no arquivo, 5 antes → 3 depois; suíte completa `83
passed` antes e depois.

**Protege contra:** código morto que simula uma checagem sem nunca poder discriminar nada — a leitura do
trecho dava a falsa impressão de uma comparação ativa.

## `RAF-T8` — O binário novo leva a marca de novo e o registro da orquestração tem um nome só

**Contexto que a motivou:** a auditoria (registros 23 e 24) mediu um arquivo binário novo saindo sem a
marca `(arquivo novo — ausente em <ref>)` que o texto novo já ganhava; e o mesmo fato — arquivo que a
condução grava por ofício (diário, `estado.tsv`, medida, telemetria) — com dois rótulos diferentes:
`atribuição: alheio` na lista por arquivo, `Registro da orquestração` no resumo.

**O que é o artefato:** `.claude/tools/review_evidence.py`.

**Como funciona na prática:** binário novo abre com a mesma marca do texto novo; a lista por arquivo
passa a rotular esses arquivos `atribuição: registro da orquestração`, igual ao resumo. Verificação
real: dois testes (`marca_e_rotulo_binario`, `marca_e_rotulo_registro`), exit 5→0 nos dois.

**Protege contra:** o revisor lendo dois nomes para o mesmo fato e não reconhecendo que são a mesma
coisa — confusão medida na auditoria.

## `RAF-T8a` — A rubrica nomeia o rótulo do registro da orquestração

**Contexto que a motivou:** o laudo da `RAF-T8` (ressalva 91%) achou que a frase da rubrica que conta os
rótulos possíveis da seção `## Arquivos tocados` (`da entrega` ou `alheio`) não foi atualizada para
incluir `registro da orquestração`, criado pela própria `RAF-T8`.

**O que é o artefato:** `docs/RUBRICA_DE_REVISAO.md` §3, mesma frase.

**Como funciona na prática:** a frase passa a nomear os três rótulos. Verificação real: `arquivos=1-0`
(texto antigo) → `0-1` (texto novo).

**Protege contra:** doutrina descrevendo um vocabulário fechado que ficou desatualizado no mesmo card
que o estendeu — a mesma classe de lapso que reincide nas `RAF-T9a`, `RAF-T27a` e `RAF-T29a`.

## `RAF-T9` — O curinga do alvo casa como na linha de comando

**Contexto que a motivou:** a auditoria (registro 27; `AE-104` do `P-0754`) mediu que um alvo com
curinga como `relatorios/*.md` casava, por `fnmatch`, também `relatorios/sub/x.md` — diferente da linha
de comando, onde `*` não atravessa `/`.

**O que é o artefato:** `.claude/tools/review_evidence.py`, função `_casa_curinga` (substitui o uso de
`fnmatch`).

**Como funciona na prática:** tradução própria do glob para regex: `*` não atravessa `/`, `**/` casa
zero ou mais pastas. Verificação real: teste `-k glob_estrela`, exit 5→0.

**Protege contra:** um alvo com curinga capturando arquivo de subpasta que o card não pretendia cobrir.

## `RAF-T9a` — O teste do curinga da AUF-T3 nomeia o mecanismo que casa o alvo

**Contexto que a motivou:** o laudo da `RAF-T9` (ressalva 91%) achou que o docstring do teste
`test_tf_alvo_com_curinga_casa_os_tocados` continuou dizendo que o curinga casa "por `fnmatch`", depois
de a própria `RAF-T9` já ter tirado o `fnmatch` do código.

**O que é o artefato:** `tests/test_review_evidence.py`.

**Como funciona na prática:** o docstring passa a nomear `_casa_curinga`. Verificação real:
`docstring=1-0` (menção a `fnmatch`) → `0-1` (menção a `_casa_curinga (RAF-T9)`).

**Protege contra:** um teste cujo texto descreve um mecanismo que o código, ao lado, já não usa.

## `RAF-T10` — O caminho acentuado chega inteiro ao dossiê de evidência

**Contexto que a motivou:** a auditoria (registro 28; `AE-99` do `P-0754`) mediu as duas leituras do
`git status` porcelain, sem `-z`, devolvendo nome acentuado em escape octal — que `montar_trechos` não
reconhecia, dando o arquivo por ausente.

**O que é o artefato:** `.claude/tools/review_evidence.py`, função `coletar_arquivos_tocados`.

**Como funciona na prática:** a leitura passa a `-z`, com parse por `\0`. Verificação real: teste `-k
acento_z`, exit 5→0.

**Protege contra:** arquivo com nome acentuado desaparecendo silenciosamente da evidência que o revisor
lê.

## `RAF-T10a` — O arquivo acentuado já rastreado chega com um nome só ao dossiê de evidência

**Contexto que a motivou:** o laudo da `RAF-T10` (ressalva 91%, achados `AE-142`..`AE-145`) achou que a
correção cobriu só a leitura de `git status`; as duas leituras de `git diff <ref>` continuavam sem
`-z`, e o resumo `--stat` e o cabeçalho do trecho mostravam o nome em escape octal mesmo com o caminho
já corrigido alhures — o mesmo arquivo podia aparecer com dois nomes diferentes no mesmo dossiê.

**O que é o artefato:** o mesmo `.claude/tools/review_evidence.py`. A correção também abriu uma versão
2 pendente do modelo de domínio do plano (propriedade `dossiê de evidência.caminho acentuado`),
validada pelo consultor no Marco 3.

**Como funciona na prática:** as duas leituras de `git diff <ref>` passam a uma só, `git diff <ref>
--name-status -z`, com parse por NUL; a gramática de caminho aceita letra acentuada; todo `git` chamado
ganha `-c core.quotepath=false`. Verificação real: `diff=1-2-0-0-0` (padrão antigo) → `0-0-1-1-1`
(padrão novo); testes `-k "acento_diff or acento_alvo"`, exit 5→0.

**Protege contra:** o mesmo arquivo aparecer com nomes diferentes em pontos diferentes do mesmo dossiê
(lista, resumo, cabeçalho do trecho), sem o revisor ter como reconciliá-los como o mesmo objeto.

## `RAF-T11` — A evidência mostra as linhas que a entrega tirou dos testes

**Contexto que a motivou:** a auditoria (registro 30; `AE-97`, `AE-98` do `P-0754`) mediu a remoção de
uma asserção de teste vizinha — não a que o card mandava tocar — passando verde numa revisão, sem
aparecer em nenhuma evidência.

**O que é o artefato:** `.claude/tools/review_evidence.py`, nova seção `## Linhas removidas dos
testes`.

**Como funciona na prática:** para cada arquivo-alvo sob `tests/` com nome `test_*.py`, a evidência
lista as linhas removidas desde o `<ref>`. Verificação real: teste `-k removidas_de_teste`, exit 5→0.

**Protege contra:** enfraquecimento de teste (remoção de asserção) que nem a Verificação por `-k` nem o
piso por contagem de testes discriminam, porque o teste continua existindo — só perde uma linha.

## `RAF-T11a` — A seção das linhas removidas cobre o teste sob curinga ou diretório e a linha que começa por dois hífens

**Contexto que a motivou:** o laudo da `RAF-T11` (ressalva 91%, `AE-149`) achou duas lacunas na seção
nova: um alvo curinga ou diretório que cobre um arquivo de teste não era reconhecido como "arquivo de
teste entre os alvos", e o filtro que descarta cabeçalho de diff (`---`) apagava junto a linha removida
cujo conteúdo começa por `--`.

**O que é o artefato:** o mesmo `.claude/tools/review_evidence.py`, função `montar_trechos`.

**Como funciona na prática:** passa a checar contra os arquivos de fato tocados (não só contra os
`Arquivos-alvo` literais), uma chave por arquivo; só conta linha depois do primeiro `@@` do hunk (o que
também tira, corretamente, o conteúdo de arquivo novo sem `ref` da contagem). Verificação real: teste
`-k "removidas_de_teste and (curinga or hifens or diretorio)"`, exit 5→0.

**Protege contra:** uma remoção de asserção continuar invisível quando o card usa alvo com curinga ou
diretório, ou quando a linha removida por acaso começa com `--`.

## `RAF-T12` — A rubrica reprova a asserção de teste removida sem ordem do card

**Contexto que a motivou:** mesmo caso da `RAF-T11` (`AE-97`/`AE-98`): a seção de linhas removidas já
existe, mas nada na rubrica obrigava o revisor a julgá-la.

**O que é o artefato:** `docs/RUBRICA_DE_REVISAO.md`, dimensão `testes`.

**Como funciona na prática:** a dimensão ganha, em `não conforme`, o critério "asserção de teste
existente removida sem que o card mande removê-la". Verificação real: `rubrica=1-0` → `0-1`.

**Protege contra:** a evidência mostrar a remoção e o revisor não ter obrigação doutrinária de reprová-la.

## `RAF-T12a` — A dimensão testes declara a fonte mista e o instrumento cita a rubrica pela seção

**Contexto que a motivou:** o laudo da `RAF-T12` (ressalva 88%) achou que o critério novo é juízo (cada
linha removida confrontada com o card), mas o bullet "Fonte da evidência" da dimensão `testes` seguiu
dizendo "mecânica" — contra a própria §3 da rubrica, que manda declarar fonte mista quando parte é
mecânica e parte é juízo.

**O que é o artefato:** `docs/RUBRICA_DE_REVISAO.md` (dimensão `testes` passa a mista) e
`.claude/tools/review_evidence.py` com seu teste (sete citações por número de linha da rubrica passam a
citar por seção, `§4`).

**Como funciona na prática:** presença dos testes e exit da suíte seguem mecânicos e travados; o juízo
sobre as linhas removidas fica livre. Verificação real: `testes=1-0`→`0-1`; `ancoras=7-4`→`0-1`
(citações por linha zeradas, por seção ativas).

**Protege contra:** a rubrica se autocontradizendo (diz "mecânica" onde a própria §3 exige "mista") e
citação por número de linha que quebra a cada edição do arquivo citado.

## `RAF-T13` — A conferência do card compara o depois com o esperado e lê o literal com pontuação

**Contexto que a motivou:** a auditoria (registros 10 e 11) mediu que, no bloco cercado,
`card_check.py` sempre comparava com `Medido antes`, ignorando `--mundo depois`; e que o par inline
antes/depois recusava vírgula, ponto-e-vírgula e ponto no literal, forçando cards a esconder o valor
esperado dentro de um comando que imprime "uma palavra".

**O que é o artefato:** `.claude/tools/card_check.py`.

**Como funciona na prática:** no bloco cercado, `--mundo depois` passa a comparar com o literal da linha
`→` (`exit N` ou substring), não mais com `Medido antes`; o par inline, delimitado por crase, passa a
aceitar `,`, `;` e `.` no literal; sem par com crase, mantém a regra antiga (legado). Verificação real:
`-k bloco_cercado_mundo` e `-k par_com_crase`, exit 5→0 nos dois; único caso real com pontuação no
corpus, `docs/plans/P-0753-auditoria-estagio-1/plano.md:434`.

**Protege contra:** uma Verificação declarada `--mundo depois` nunca medir de fato o depois — falso
positivo estrutural na forma normativa da rubrica §8.1.

## `RAF-T13a` — O docstring do módulo e a ajuda de --mundo da conferência do card dizem o mundo depois da forma 8.1

**Contexto que a motivou:** o laudo da `RAF-T13` (ressalva 91%, `AE-155`) achou que a regra foi entregue
no código, mas o docstring do módulo e a ajuda de `--mundo` continuaram dizendo que a conferência
compara sempre com `Medido antes` e que o mundo só vale na forma inline.

**O que é o artefato:** `.claude/tools/card_check.py`, docstring do módulo e `help` de `--mundo`.

**Como funciona na prática:** os dois textos passam a dizer a regra entregue (mundo `depois` compara com
o literal do esperado; mundo vale nas duas formas). Verificação real: `docstring=1-0`→`0-1`;
`help=1-0`→`0-1`.

**Protege contra:** a mesma classe de lapso da `RAF-T8a`/`RAF-T9a` — código mudou, o texto que o
descreve ficou para trás.

## `RAF-T14` — A conferência do card roda o git de leitura contra o recorte do despacho

**Contexto que a motivou:** a auditoria (registro 12) mediu que `card_check.py` só executava comando
que começasse por `python` ou `pwsh` — uma Verificação com `git status` precisava de um invólucro
`python -c`.

**O que é o artefato:** `.claude/tools/card_check.py`.

**Como funciona na prática:** `git` entra na lista de programas aceitos só com o primeiro argumento em
{`status`, `diff`, `show`, `ls-files`, `check-ignore`}; outro subcomando é recusado, nomeando-o; o
token literal `<ref>` no comando é trocado pelo `ref` gravado em `tarefa-corrente.json`; linha marcada
`(invariância)` sai `não medida (invariância)` no mundo antes, sem falhar, e roda no mundo depois.
Verificação real: três testes (`git_leitura`, `ref_do_despacho`, `invariancia`), exit 5→0.

**Protege contra:** um card ter de embrulhar todo comando de leitura em `python -c`, e Verificação de
invariância (linha que deve continuar igual) não ter forma prevista.

## `RAF-T15` — A medida gravada fica na pasta do plano da árvore medida, com o momento no nome

**Contexto que a motivou:** `card_check.py --gravar` gravava a medida sob a pasta derivada de
`--plano`, não de `--root` — um ensaio em cópia com o `--plano` real gravaria a medida da cópia na pasta
real, e a medida seguinte a sobrescreveria; 20 medidas do `P-0753` estavam versionadas com nome sem
indicar o mundo.

**O que é o artefato:** `.claude/tools/caminhos.py` (`destino_medida`), `.claude/tools/card_check.py`
(`--gravar`) e `.claude/tools/review_evidence.py` (leitura da medida).

**Como funciona na prática:** `destino_medida` resolve a pasta sob a raiz dada
(`<raiz>/docs/plans/<plano>/evidencia/`), e o nome do arquivo ganha o mundo:
`<P-id>-<ID>-medida-<mundo>.json`; `review_evidence` lê `-depois`, depois `-antes`, depois o nome sem
mundo (legado). Verificação real: três testes (`destino_medida_na_raiz`, `medida_gravada_com_o_mundo`,
`medida_com_mundo`), exit 5→0.

**Protege contra:** a rodada de replanejamento (`RAF-T18`) não ter onde gravar a medida de antes/depois
de um card reescrito, sem sobrescrever a medida real com a da cópia de ensaio.

## `RAF-T16` — O planejador mede o antes do card dependente na cópia com os anteriores aplicados

**Contexto que a motivou:** a auditoria (registro 13) mediu que um card cujo `antes` depende do
antecessor (por exemplo, um arquivo que o card anterior já mudou) só passava se o valor fosse igual nos
dois mundos — o protocolo não dizia em que árvore medir.

**O que é o artefato:** `.claude/agents/pantonic-planner.md`, Fase 5.

**Como funciona na prática:** card cujo `antes` depende de antecessor mede o `antes` na cópia de ensaio
com os antecessores já aplicados; só o primeiro card de cada cadeia mede contra a árvore real; o valor
publicado nomeia a árvore (`real` ou `cópia com <IDs> aplicados`). Verificação real: `arvore=0`→`1`.

**Protege contra:** um card intermediário de uma cadeia falhar o ensaio por medir o `antes` na árvore
errada.

## `RAF-T17` — O planejador discrimina o card que deixa o alvo igual pela invariância

**Contexto que a motivou:** a auditoria (registro 14) mediu que o item 14 da Fase 4 não previa exceção
para card cujo estado final é "igual" (por exemplo, revisão do `README.md` sem texto novo) — a linha
"trava" não tinha forma para esse caso.

**O que é o artefato:** `.claude/agents/pantonic-planner.md`, item 14 da Fase 4.

**Como funciona na prática:** ganha a forma **Operação de estado final igual**: a linha discriminante é
`git diff <ref> --numstat -- <alvo>` com saída vazia, marcada `(invariância)`, medida no mundo depois.
Verificação real: `igual=0`→`1`.

**Protege contra:** card sem texto novo não ter Verificação nenhuma que discrimine "nada mudou" de "algo
mudou e ninguém percebeu".

## `RAF-T18` — A rodada de replanejamento grava a medida dos dois mundos

**Contexto que a motivou:** a auditoria (registro 35, `H-16`) constatou que nada instruía a rodada de
replanejamento a gravar a medida de antes/depois de cada card que reescreve — a única residência era
prosa da §5 do plano.

**O que é o artefato:** `.claude/agents/pantonic-planner.md`, mesmo trecho do item 14.

**Como funciona na prática:** a rodada passa a gravar a medida dos dois mundos de cada card reescrito,
usando o destino que a `RAF-T15` corrigiu. Verificação real: `rodada=0`→`1`.

**Protege contra:** uma reescrita de card no meio do plano não deixar rastro medido do que mudou.

## `RAF-T19` — A conferência do modelo julga só a versão vigente quando pedida

**Contexto que a motivou:** a auditoria (registros 31 e 32) mediu que, com uma versão pendente presente,
`modelo.py check` validava as duas seções juntas e prefixava violações com `1A: `; o ato do dono do
plano fictício travou o despacho da tarefa seguinte porque a pendente, ainda sem cards, saía com
violação por construção.

**O que é o artefato:** `.claude/tools/modelo.py`, novo parâmetro `--so-vigente`.

**Como funciona na prática:** `check --so-vigente` julga só a versão vigente, sem contar violação de
card cuja operação citada só existe na pendente; sem a flag, `check` continua julgando as duas.
Verificação real: teste `-k so_vigente`, exit 5→0.

**Protege contra:** uma versão pendente ainda incompleta travar o despacho de tarefas que não têm nada a
ver com ela.

## `RAF-T19a` — O teste distingue o check com e sem --so-vigente pela versão pendente fora de sequência

**Contexto que a motivou:** o laudo da `RAF-T19` (ressalva 91%, `AE-169`) achou que os quatro testes
originais usavam pendente em versão 2 contra vigente 1 — sequência em que a violação de "fora de
sequência" nunca dispara, então nada provava que `--so-vigente` de fato a suprime.

**O que é o artefato:** `tests/test_modelo.py`.

**Como funciona na prática:** novo caso com pendente em versão 3 contra vigente 1 (fora de sequência):
`check --so-vigente` sai 0 sem a violação; `check` sem a flag sai 1 com ela. Verificação real: `-k
"so_vigente and fora_de_sequencia"`, exit 5→0.

**Protege contra:** uma guarda condicional ficar sem o caso de teste que a distingue de "nunca dispara
mesmo".

## `RAF-T20` — O despacho pede à conferência do modelo só a versão vigente

**Contexto que a motivou:** mesmo caso da `RAF-T19`: o `despachar` chamava `modelo.py check` sem a
flag, herdando o mesmo travamento.

**O que é o artefato:** `.claude/tools/backlog.py`, chamada ao `modelo.py check`.

**Como funciona na prática:** `despachar` passa a chamar `check --so-vigente`. Verificação real: teste
`-k versao_vigente`, exit 5→0.

**Protege contra:** o mesmo travamento de despacho da `RAF-T19`, agora no ponto de entrada real do loop.

## `RAF-T21` — A conferência do modelo recusa o card que copia a operação com outro texto

**Contexto que a motivou:** a auditoria (registros 36 e 37) mediu `check` aprovando um card cujo campo
`Operação do modelo` copiava um texto diferente do da operação de mesmo número na versão citada — nada
amarrava o texto copiado ao texto oficial.

**O que é o artefato:** `.claude/tools/modelo.py`, nova violação `V22`.

**Como funciona na prática:** `V22 <ID> — texto de OP-<n> diverge da versão <v>` compara (espaços
colapsados, pontas limpas) o texto do campo com o de toda operação de mesmo número na versão citada —
inclusive quando o número aparece duas vezes na mesma versão. Verificação real: teste `-k
texto_divergente`, exit 5→0; medido também sobre os quatro planos encerrados (`P-0746`, `P-0747`,
`P-0748`, `P-0753`), que passam a acusar `V22` como registro histórico, sem reescrita.

**Protege contra:** um card citando uma operação do modelo com texto próprio, divergente do que o modelo
de fato diz — a lacuna que permitiu o defeito medido.

## `RAF-T22` — A diferença entre versões mostra a operação inserida, a renumerada e a propriedade nova

**Contexto que a motivou:** a auditoria (registro 34) mediu que inserir uma operação no meio do fluxo
fazia toda operação seguinte aparecer como "alterada" (casamento só por número), e que uma propriedade
só da versão pendente não aparecia no drift.

**O que é o artefato:** `.claude/tools/modelo.py`, funções `_diff_fluxo` e `_diff_estado`.

**Como funciona na prática:** `_diff_fluxo` casa operações primeiro por texto idêntico, depois por
número — operação nova, renumerada ou de texto alterado saem com marcas distintas (`[+]`, `[=] (era
OP-j)`, `[~] texto => texto`); `_diff_estado` lista chave presente numa só versão. Verificação real:
teste `-k drift_versoes`, exit 5→0.

**Protege contra:** o dono ler, no marco, um drift que mostra "cascata de alterações" onde, na verdade,
uma operação só foi inserida — leitura enganosa do que de fato mudou.

## `RAF-T22a` — A diferença entre versões mostra a operação que muda o que precisa ou o que altera sem mudar o texto

**Contexto que a motivou:** a emenda do modelador de domínio (Marco 5) deu à operação de rubrica de
revisão uma nova dependência e uma propriedade nova, mas o `show --drift`, medido em 2026-09-30, não
mostrou nenhuma das duas — `_diff_fluxo` (`RAF-T22`) só compara operações pelo texto, e um par de mesmo
texto e mesmo número não gerava linha nenhuma mesmo quando o que ele precisa ou o que ele altera mudou.

**O que é o artefato:** `.claude/tools/modelo.py`, mesma função `_diff_fluxo` da `RAF-T22`.

**Como funciona na prática:** todo par de mesmo texto passa a emitir uma linha própria quando a lista do
que a operação precisa, ou do que ela altera, difere entre as duas versões. Verificação real: teste `-k
drift_contrato_da_operacao`, exit 5→0; o `show --drift` do próprio `P-0755` passou a mostrar as duas
linhas novas.

**Protege contra:** o dono aceitar um marco cujo drift, por ele lido, parece não mudar nada numa
operação — quando na verdade uma dependência ou um efeito colateral dela mudou.

## `RAF-T23` — O comando do marco promove a versão aceita e cobra a validação do consultor

**Contexto que a motivou:** a auditoria (registros 37 e 38) mediu que promover a versão pendente exigia
outra instância do modelador (55,0 mil tokens), e que `encerrar.py marco --aceita-versao` não cobrava a
validação prévia do consultor que `GOVERNANCA.md` §3.2 exige.

**O que é o artefato:** `.claude/tools/encerrar.py`, `marco --aceita-versao <k> --consultor "<linha>"`.

**Como funciona na prática:** grava a linha de validação verbatim na célula do marco, ao lado do
veredito do dono; roda `modelo.py check` completo e recusa se houver violação de versão pendente;
promove mecanicamente — a versão pendente vira a vigente, o registro de versões ganha a linha "Caiu
pelo aceite da versão `<k>`", e o campo `Operação do modelo` de cada card listado é reescrito com
número, texto e dependências da versão promovida. Conflito (cabeçalho divergente, registro sem vigente
único) recusa e imprime o dossiê de emenda para o modelador. Verificação real: dois testes
(`promove_versao`, `validacao_do_consultor`), exit 5→0; medido no próprio Marco 4 deste plano:
`modelo.py check --plano` sai `exit 0` com a versão já promovida.

**Protege contra:** o custo de outra instância do modelador (55,0 mil tokens) só para mover texto de uma
seção para outra, e a promoção acontecer sem o consultor ter validado a diferença que o dono está
aceitando.

## `RAF-T23a` — O comando do marco reconhece a versão pendente pela mesma regra do modelo.py

**Contexto que a motivou:** o laudo da `RAF-T23` (ressalva 91%, `AE-176`) achou que a pré-checagem do
comando reconhecia a versão pendente por uma regra própria (prefixo), e a checagem de promoção a lia
por igualdade exata da constante do `modelo.py` — cabeçalho com texto a mais passava a pré-checagem e
caía em exceção não tratada.

**O que é o artefato:** `.claude/tools/encerrar.py`.

**Como funciona na prática:** a pré-checagem passa a usar a mesma regra do `modelo.py`; cabeçalho
divergente sai com mensagem própria (`marco: plano sem versão pendente (## 1A)`, exit 1) em vez de
exceção. Verificação real: teste `-k cabecalho_1a`, exit 5→0.

**Protege contra:** duas regras diferentes reconhecendo a mesma seção em dois pontos do mesmo comando —
divergência que se manifestava como queda, não como mensagem.

## `RAF-T23b` — O dossiê do comando do marco pede ao modelador o que ele de fato devolve, no conflito e na recusa

**Contexto que a motivou:** o laudo da `RAF-T26` (ressalva 90%, `AE-180`) achou que o campo `Devolver`
do dossiê de emenda tinha um texto único para conflito e para recusa — no conflito, pedia o que o
próprio comando já faz na promoção; na recusa, pedia uma linha que não entra.

**O que é o artefato:** `.claude/tools/encerrar.py`, função que monta o dossiê de emenda.

**Como funciona na prática:** no conflito, `Devolver` passa a pedir a versão vigente e a pendente
acertadas para o comando rodar de novo; na recusa, a versão vigente sem a linha da versão recusada e o
plano sem a pendente. Verificação real: teste `-k devolver`, exit 5→0; `devolver=1-0`→`0-1`.

**Protege contra:** o modelador receber um pedido que não corresponde ao que o comando vai de fato
consumir em cada um dos dois casos.

## `RAF-T24` — Quem conduz segue a janela quando o modelador cria operação nova e enfileira a rodada

**Contexto que a motivou:** a rota que segue sem parar a janela quando o modelador cria uma operação
nova não dizia que, em seguida, quem conduz devia despachar o planejador para a rodada de
replanejamento.

**O que é o artefato:** `.claude/skills/scrum-master/SKILL.md`.

**Como funciona na prática:** quando o modelador cria operação nova, o loop despacha em seguida o
planejador para a rodada, que escreve o card da operação nova. Verificação real: `rodada=0`→`1`.

**Protege contra:** a janela ficar sem próximo passo definido depois de uma emenda que cria operação —
a lacuna que produzia o estado que o próprio despacho recusava.

## `RAF-T24a` — Quem conduz dá destino, no marco, ao card da operação nova que a rodada deixou bloqueado

**Contexto que a motivou:** o laudo da `RAF-T25` (`AE-178`) achou que o card da operação nova nasce
bloqueado até o marco, mas nada o tirava desse estado quando o marco chegava — nem no aceite, nem na
recusa.

**O que é o artefato:** `.claude/skills/scrum-master/SKILL.md`, mesmo trecho da rota do modelador.

**Como funciona na prática:** com a versão aceita, o card passa a `ready`; com a versão recusada, o
consultor — a quem o caso já volta — tira o card do plano. Verificação real: `destino=0-0`→`1-1`.

**Protege contra:** um card ficar bloqueado para sempre depois de o marco já ter decidido o destino da
versão que o desbloquearia.

## `RAF-T25` — O planejador escreve, na rodada que segue a emenda, o card da operação nova bloqueado até o marco

**Contexto que a motivou:** nada dizia quem escreve o card da operação que uma emenda cria no meio do
loop.

**O que é o artefato:** `.claude/agents/pantonic-planner.md`.

**Como funciona na prática:** na rodada de replanejamento que segue a emenda, o planejador escreve o
card da operação nova e o registra bloqueado até o aceite da versão no marco. Verificação real:
`nova=0`→`1`.

**Protege contra:** a rodada de replanejamento terminar sem o card que a operação nova precisa, deixando
a emenda sem tarefa executável.

## `RAF-T26` — O modelador sai da promoção de versão e o consultor ganha a forma da linha de validação

**Contexto que a motivou:** a doutrina do modelador ainda descrevia a promoção como ato dele — o que a
`RAF-T23` tirou do comando —, e a doutrina do consultor não tinha a forma da linha de validação que o
`--consultor` da `RAF-T23` exige.

**O que é o artefato:** `.claude/agents/pantonic-model-designer.md` e
`.claude/agents/pantonic-consultant.md`.

**Como funciona na prática:** o modelador passa a dizer que só é chamado na promoção quando o comando
encontra conflito; o consultor ganha a forma fixa da linha de validação (uma frase, `valido`/`não
valido a versão <k>: <razão>`). Verificação real: `promocao=1-0`→`0-1`; `validacao=0`→`1`.

**Protege contra:** dois textos de doutrina descrevendo um procedimento que o código já não segue mais
daquele jeito.

## `RAF-T26a` — O modelador conhece os quatro conflitos da promoção e devolve o que o dossiê pede

**Contexto que a motivou:** o laudo da `RAF-T26` (ressalva 90%, `AE-180`) achou que o texto entregue
enumerava três conflitos da promoção, quando o comando tem um quarto que também imprime o dossiê, e
dizia que o modelador devolve algo diferente do que o campo `Devolver` (`RAF-T23b`) pede em cada caso.

**O que é o artefato:** `.claude/agents/pantonic-model-designer.md`.

**Como funciona na prática:** o texto passa a nomear os quatro conflitos e a devolver exatamente o que o
campo `Devolver` de cada caso pede. Verificação real: `conflito=1-0`→`0-1`.

**Protege contra:** o modelador, chamado no conflito, devolver um dossiê incompleto porque a doutrina
que o instrui está desalinhada com o comando que o chamou.

## `RAF-T27` — O pré-voo separa o caminho a criar do que já devia existir e não toma extensão solta por caminho

**Contexto que a motivou:** a auditoria (registro 2) mediu o pré-voo do próprio pedido de criação deste
plano saindo exit 1, com "não" em todo arquivo que o pedido mandava criar (um `.txt` foi tomado por
caminho a mais; um `.bin` nem foi citado) — o planejador teve de contornar à mão.

**O que é o artefato:** `.claude/tools/prevoo.py`.

**Como funciona na prática:** caminho passa a ser o token terminado em `/`, ou com `/` e extensão curta
no último segmento, ou sem `/` terminado numa das nove extensões reconhecidas; caminho inexistente sai
`criar` (não `não`) quando a mesma frase traz antes um verbo de criação, e `criar` não derruba o exit 0.
Verificação real: dois testes (`conta_como_caminho`, `caminho_a_criar`), exit 5→0; sobre o pedido
original citado na auditoria, 6 linhas `criar`, exit 0.

**Protege contra:** o pré-voo devolver "premissa quebrada" para um pedido que, na verdade, está pedindo
para criar o arquivo.

## `RAF-T27a` — O docstring do módulo do pré-voo diz o que conta como caminho e quando o caminho sai a criar

**Contexto que a motivou:** o laudo da `RAF-T27` (ressalva 91%, `AE-183`) achou que a correção atualizou
os docstrings das funções, mas não o do módulo, que seguiu descrevendo a regra antiga.

**O que é o artefato:** `.claude/tools/prevoo.py`, docstring do módulo.

**Como funciona na prática:** passa a dizer as três regras entregues: o que conta como caminho, a
atribuição `criar` pelo verbo na mesma frase, e que `criar` não derruba o exit 0. Verificação real:
`docstring=1-0-0` (222 linhas) → `0-1-1` (227 linhas).

**Protege contra:** a mesma classe de lapso das `RAF-T8a`/`T9a`/`T13a` — a documentação de entrada de um
módulo ficando desatualizada.

## `RAF-T28` — O controle do backlog avisa, ao drenar, a diretiva que não cita nada vivo

**Contexto que a motivou:** a auditoria (registro 16) mediu a diretiva de priorização seguindo citar um
plano que já tinha saído da fila, e o `next` filtrando a fila inteira (0 elegível) até alguém perceber e
reescrever a diretiva à mão.

**O que é o artefato:** `.claude/tools/backlog.py drain`.

**Como funciona na prática:** depois de drenar, se a diretiva não cita nenhum id vivo nem o plano
recém-drenado, imprime em stderr o aviso "a diretiva de priorização não cita nenhum id vivo"; o exit não
muda. Verificação real: teste `-k aviso_diretiva`, exit 5→0.

**Protege contra:** a fila do `next` ficar vazia por uma diretiva obsoleta, sem aviso no momento em que a
obsolescência nasce.

## `RAF-T29` — O controle do backlog recusa o prefixo de decisão que outro plano já declarou

**Contexto que a motivou:** a auditoria (registro 17) mediu um prefixo de decisão colidindo com 72
ocorrências já usadas por outro plano — nenhum instrumento lia prefixo de decisão para acusar a
colisão.

**O que é o artefato:** `.claude/tools/backlog.py check`, nova violação `C-18`.

**Como funciona na prática:** recusa plano cujo prefixo de decisão declarado já é declarado por outro
plano de `docs/plans/`, nomeando o plano dono (o de menor id); citar prefixo alheio (referenciar decisão
de outro plano) não é colisão — só a declaração repetida é. Verificação real: teste `-k
prefixo_de_decisao`, exit 5→0.

**Protege contra:** duas decisões de planos diferentes ficarem com o mesmo prefixo, tornando ambígua a
citação.

## `RAF-T29a` — O cabeçalho do controle do backlog conta o vocabulário do check até C-18

**Contexto que a motivou:** o laudo da `RAF-T29` (ressalva 91%) achou que a violação `C-18` foi
acrescentada sem atualizar as três frases que contam o vocabulário do `check`.

**O que é o artefato:** `.claude/tools/backlog.py`.

**Como funciona na prática:** as três frases passam de `C-1..C-17` a `C-1..C-18`, e o comentário nomeia
a `C-18` e a função que a acusa. Verificação real: `vocabulario=3-0-0` (2.612 linhas) → `0-3-1` (2.613
linhas).

**Protege contra:** a mesma classe de lapso das correções de doutrina anteriores — vocabulário fechado
que o código estende sem a contagem que o descreve acompanhar.

## `RAF-T30` — O fechamento de tarefa registra o achado pela linha de origem e avisa a falha de instrumento

**Contexto que a motivou:** a auditoria mediu, no registro 39, achados de laudo reescritos escapando da
dedupe (comparada só por texto); e no registro 47, um achado real de queda de instrumento
(`AE-106`) chegando num laudo com recomendação "seguir", sem escalar — só apareceu no relatório porque a
diretiva daquela janela roteava tudo à auditoria.

**O que é o artefato:** `.claude/tools/encerrar.py tarefa`.

**Como funciona na prática:** cada achado de processo grava, na própria linha, a origem
`laudo:<TAREFA>#<n>`; o fechamento pula achado cuja origem já foi citada por outra `AE-` do plano (a
dedupe por texto continua como segundo teste); e imprime, antes da linha final,
`encerrar: B1 — achado de instrumento com falha: <texto>` para achado de alvo `instrumento` cujo texto
contém termo de falha (queda, traceback, exceção, erro). Verificação real: checagens dedicadas mantêm
exit 0 (regressão) e passam a contar `marco=2 total=2` onde antes era `marco=1 total=2`.

**Protege contra:** um achado real de queda de instrumento ficar preso dentro de um laudo "seguir" e
nunca subir ao consultor.

## `RAF-T30a` — O laudo aceita o alvo instrumento que o aviso do fechamento lê

**Contexto que a motivou:** o próprio laudo da `RAF-T30` (reprovado 74%, `AE-186`) achou que o aviso
novo já checava o alvo `instrumento`, mas o gerador do laudo, a rubrica e o revisor só conheciam quatro
alvos — nenhum deles nomeava `instrumento`.

**O que é o artefato:** `.claude/tools/rdo.py`, `docs/RUBRICA_DE_REVISAO.md` §6 e
`.claude/agents/pantonic-reviewer.md`; abriu drift no modelo (versão 4 pendente, validada pelo consultor
no Marco 5).

**Como funciona na prática:** `instrumento` passa a ser o quinto alvo de achado de processo reconhecido
pelo gerador do laudo, pela rubrica e pelo revisor. Verificação real: teste `-k alvo_instrumento`, exit
5→0; `alvos=3-0-0`→`0-1-1`; `rdo=0-0-0`→`1-1-1`.

**Protege contra:** o aviso da `RAF-T30` checar um alvo que o resto da cadeia (gerador, rubrica,
revisor) não sabia produzir — a regra existia, mas não tinha como nascer num laudo real.

## `RAF-T31` — A série de telemetria atribui pela linha de abertura do despacho e guarda uma linha por agente

**Contexto que a motivou:** a auditoria (registros 41 e 54) mediu a série de telemetria do plano
fictício somando 1.138,0 mil tokens contra 1.250,0 mil medido — um planejador inteiro (69,96 mil
tokens) ficou atribuído ao plano errado, porque o hook lia o primeiro `P-<n>` citado na primeira
mensagem em vez de uma fonte própria.

**O que é o artefato:** `.claude/tools/telemetria_hook.py` e `.claude/tools/telemetria.py`.

**Como funciona na prática:** todo despacho de subagente abre com a linha `despacho: <P-id>[ <ID>]`; o
hook de telemetria e o de progresso passam a lê-la antes de `tarefa-corrente.json` e antes do primeiro
`P-<n>` citado; a série ganha a coluna `agente`, e o escritor substitui a linha do mesmo agente em vez
de apensar. Verificação real: dois testes (`linha_de_despacho`, `linhas_por_agente`), exit 5→0.

**Protege contra:** uma instância de subagente ser atribuída ao plano ou à tarefa errada por causa de um
`P-<n>` citado dentro da conversa, em vez da linha que o próprio despacho declara.

## `RAF-T31a` — O escritor da série de telemetria diz nos docstrings quem recusa a linha repetida e que a linha do agente se troca

**Contexto que a motivou:** o laudo da `RAF-T31` (ressalva 91%) achou que os docstrings de duas funções
seguiram dizendo "todo escritor" recusa linha repetida, e o do módulo seguiu dizendo que a série "só
apende" — quando o escritor por agente, entregue na mesma tarefa, de fato troca a linha do mesmo agente.

**O que é o artefato:** `.claude/tools/telemetria.py`.

**Como funciona na prática:** os docstrings passam a dizer que a recusa de linha repetida vale para o
escritor sem agente, e que a linha do mesmo agente se troca. Verificação real: `docstring=1-1-1-0-0`
(305 linhas) → `0-0-0-3-1` (314 linhas).

**Protege contra:** a mesma classe de lapso — texto descrevendo um comportamento que o próprio card
mudou ao lado.

## `RAF-T31b` — O primeiro parágrafo do docstring e o help do append da série de telemetria ressalvam o --agente

**Contexto que a motivou:** o laudo da `RAF-T31a` (ressalva 91%) achou que a varredura anterior corrigiu
os parágrafos que o laudo da `RAF-T31` havia nomeado, mas não o arquivo inteiro — o primeiro parágrafo
do docstring do módulo e o `help` do subcomando `append` continuaram afirmando só o apêndice.

**O que é o artefato:** `.claude/tools/telemetria.py`.

**Como funciona na prática:** o primeiro parágrafo ganha a ressalva "sem `--agente`"; o `help` de
`append` ganha "com `--agente`, troca a do mesmo agente". Verificação real: `texto=1-0-0-0` (314
linhas) → `0-1-1-1` (317 linhas).

**Protege contra:** a mesma reincidência, desta vez porque a varredura seguiu o que o laudo apontou em
vez de varrer o arquivo inteiro pelas frases que afirmam o comportamento.

## `RAF-T32` — O painel do gerente mostra a tarefa que a linha de abertura do despacho declara

**Contexto que a motivou:** a auditoria (registro 54) mediu o painel mostrando a tarefa corrente do
loop, não a que de fato foi despachada — planejador e modelador do plano fictício saíram no painel com
o título da tarefa errada.

**O que é o artefato:** `.claude/tools/progresso_hook.py`.

**Como funciona na prática:** os ramos de despacho e de volta síncrona de subagente passam a ler a mesma
linha de abertura do despacho que a `RAF-T31` introduziu. Verificação real: teste `-k
tarefa_do_despacho`, exit 5→0.

**Protege contra:** o painel mostrar o título de uma tarefa diferente da que o subagente de fato
recebeu.

## `RAF-T32a` — O painel do gerente mostra a tarefa despachada também no retorno por hand-back

**Contexto que a motivou:** o laudo da `RAF-T32` (ressalva 91%) achou que a correção cobriu os ramos
síncronos, mas excluiu o caminho de retorno por hand-back, onde o painel seguiu mostrando o título
errado.

**O que é o artefato:** `.claude/tools/progresso_hook.py`.

**Como funciona na prática:** grava o título despachado numa chave própria no evento de saída do
hand-back, e o consome na volta. Verificação real: teste `-k retorno_do_despacho`, exit 5→0.

**Protege contra:** o mesmo defeito da `RAF-T32` sobrevivendo no caminho de retorno menos comum, que a
exclusão por nome de ramo, sem medir o que ele emite, deixou passar.

## `RAF-T33` — A norma de consumo manda todo despacho de subagente abrir com a linha que declara plano e tarefa

**Contexto que a motivou:** mesmo caso das `RAF-T31`/`RAF-T32`: a regra existe no código dos hooks, mas
não em doutrina.

**O que é o artefato:** `GOVERNANCA.md` §4.2.

**Como funciona na prática:** fixa a regra de que todo despacho de subagente abre com a linha que
declara plano e tarefa, e que os hooks a leem antes de qualquer outra fonte. Verificação real:
`abertura=1-0`→`0-1`.

**Protege contra:** um autor de card ou de skill reintroduzir, sem saber da regra, um despacho que não
abre com a linha — quebrando telemetria e painel de novo.

## `RAF-T34` — Quem conduz leva ao consultor a falha de instrumento que o fechamento avisa e a linha do card em triagem

**Contexto que a motivou:** mesmo caso da `RAF-T30` (achado de queda preso num laudo "seguir") e da
`RAF-T31`/`T32` (consultor recebendo o card da tarefa corrente, não o card em triagem).

**O que é o artefato:** `.claude/skills/scrum-master/SKILL.md`.

**Como funciona na prática:** a condição de escalar ao consultor passa a valer sempre que existir a
linha de aviso que a `RAF-T30` passou a imprimir, qualquer que seja a recomendação do laudo; o despacho
do consultor ganha a linha de abertura com o id do card em triagem. Verificação real: `b1=0`→`1`;
`molde=0`→`1`.

**Protege contra:** um achado de queda de instrumento, já detectado pelo código, não chegar ao consultor
porque a doutrina que decide quem escala não lia a linha nova.

## `RAF-T35` — O consultor cita no achado a linha do laudo de onde ele veio

**Contexto que a motivou:** auditoria registro 39: a reescrita do consultor, quando ele registra ou
reformula um achado a partir de um laudo, escapava da dedupe por não ter a mesma origem que a `RAF-T30`
passou a gravar.

**O que é o artefato:** `.claude/agents/pantonic-consultant.md`.

**Como funciona na prática:** ao registrar ou reescrever um achado a partir de laudo, o consultor passa
a citar a mesma origem que `apensar_achado` grava. Verificação real: `origem=0`→`1`.

**Protege contra:** um achado reescrito pelo consultor escapar da dedupe da `RAF-T30` e duplicar o mesmo
achado sob outro texto.

## `RAF-T36` — O planejador ganha a régua de profundidade pelo tamanho do plano

**Contexto que a motivou:** a auditoria (registros 8 e 9) mediu o planejamento sozinho consumindo 352,2
dos 1.250,0 mil tokens gastos em subagentes do plano fictício (≈28%) para produzir 5 arquivos — a Fase
4 aplicava a mesma profundidade a qualquer plano, independentemente do tamanho.

**O que é o artefato:** `.claude/agents/pantonic-planner.md`, Fase 4.

**Como funciona na prática:** ganha uma coluna de régua para "plano de até 5 operações, qualquer
classe": a maior parte dos itens continua aplicando sempre; alguns só valem com gramática ou tabela
normativa no plano, ou com arquivo compartilhado tocado por dois cards. Verificação real:
`regua=1-0`→`0-1`.

**Protege contra:** um plano pequeno pagar o mesmo custo de análise de um plano grande — o próprio custo
que a auditoria mediu neste plano.

## `RAF-T37` — O pedido do planejador ao modelador deixa de exigir caminho, linha e nome de comando

**Contexto que a motivou:** a auditoria (registro 7) mediu o dossiê de autoria do planejador pedindo ao
modelador "o caminho mora no contrato", e o modelador recusando pela norma que proíbe célula descritiva
com caminho — os dois liam a mesma doutrina de jeitos opostos.

**O que é o artefato:** `.claude/agents/pantonic-planner.md`, Fase 3a.

**Como funciona na prática:** a Fase 3a deixa de pedir caminho, linha ou nome de instrumento em célula
descritiva do modelo, e passa a dizer que o modelador os recusa. Verificação real: `contrato=0`→`1`.

**Protege contra:** planejador e modelador divergindo sobre a mesma norma por o primeiro nunca ter lido
a proibição na própria doutrina.

## `RAF-T38` — Quem conduz roda a checagem de versão do kit antes do planejador, que a registra no cabeçalho

**Contexto que a motivou:** a auditoria (registro 15) mediu a Fase 5 do planejador mandando invocar a
skill `checar-versao-kit`, mas o planejador é subagente sem essa ferramenta disponível — instrução
impossível de cumprir no próprio papel.

**O que é o artefato:** `.claude/skills/checar-versao-kit/SKILL.md` e
`.claude/agents/pantonic-planner.md`.

**Como funciona na prática:** quem conduz roda a checagem antes de despachar o planejador e põe o
resultado no dossiê; a Fase 5 deixa de mandar invocar skill e passa a registrar, no cabeçalho do plano,
a checagem que o dossiê já trouxe. Verificação real: `momento=0`→`1`; `versao=1-0`→`0-1`.

**Protege contra:** uma instrução no papel do subagente que nenhuma configuração de ferramentas permite
cumprir.

## `RAF-T39` — A mensagem de marco abre nomeando a entrega e o pedido do dono que a originou

**Contexto que a motivou:** a auditoria (registro 46) mediu a mensagem de um marco anterior pedindo "a
auditoria nova" sem dizer que era a auditoria que o dono já tinha pedido, levando-o a perguntar "Você
está pedindo mais uma auditoria?" — falha registrada em `docs/FALHAS_COMUNICACAO.tsv`.

**O que é o artefato:** `.claude/skills/scrum-master/SKILL.md`, subseção nova "Quando a janela para num
marco".

**Como funciona na prática:** a mensagem de marco abre nomeando a entrega e citando a data e um trecho
verbatim do pedido do dono de origem; a entrega é o que a tabela de marcos do plano já nomeia para
aquele marco. Verificação real: `marco=0`→`1`.

**Protege contra:** o dono ter de perguntar o que uma mensagem de marco está pedindo.

## `RAF-T39a` — A abertura de marco nomeia a etapa, e o primeiro parágrafo do relatório remete a ela

**Contexto que a motivou:** o laudo da `RAF-T39` (ressalva 88%, `AE-204`) achou que a subseção nova
mandava usar a célula inteira da tabela de marcos como entrega, mas o próprio exemplo de um marco usava
só um trecho dela, e a célula de outro marco é um comando — não o nome de uma entrega; o primeiro
parágrafo do relatório de encerramento continuou dizendo que ele sempre abre pela saída do `modelo.py
show`.

**O que é o artefato:** `.claude/skills/scrum-master/SKILL.md`, mesma subseção e o primeiro parágrafo do
relatório de encerramento.

**Como funciona na prática:** a entrega passa a ser o trecho da célula antes dos dois-pontos, sem a
lista que o segue; célula que não nomeia etapa, ou plano sem tabela de marcos, usa o título do plano; o
primeiro parágrafo do relatório ganha a remissão a essa exceção. Verificação real:
`marco=1-0-0-1`→`1-1-1-0`.

**Protege contra:** a regra nova produzir, num marco sem etapa nomeada, uma mensagem que cola um comando
bruto onde deveria nomear uma entrega.

## `RAF-T40` — O guia de entrada descreve o kit como ele fica depois das cinco etapas

**Contexto que a motivou:** o `README.md` citava dez instrumentos do kit, mas dois —
`card_check.py` e `telemetria_hook.py` — não apareciam, e nenhuma das mudanças de comportamento das
etapas A a D estava refletida no texto.

**O que é o artefato:** `README.md`.

**Como funciona na prática:** passa a citar os onze comandos do kit (os dez conferidos mais
`custo_sessao.py`), com o que cada etapa mudou entrando por troca de trecho nas seções que já descrevem
cada instrumento; a descrição da série `docs/telemetria.tsv` deixa de dizer que ela é append-only (a
`RAF-T31` passou a trocar a linha do mesmo agente). Verificação real: `guia=8-0-1` (8 instrumentos
citados, 0 frases novas, "append-only" ainda presente) → `11-16-0`; `pwsh
.claude/checks/check-readme.ps1` sai `exit 0` (confirmado nesta entrega: `check-readme: OK - 10
agente(s), 13 skill(s), 20 guardrail(s)…`).

**Protege contra:** o guia de entrada do kit — a porta de quem chega ao projeto — descrever um
comportamento que as 39 tarefas anteriores já mudaram.

## O que vale além deste plano

| regra | o que resolve | residência |
|---|---|---|
| O loop de plano recém-planejado abre em janela nova | custo por turno da orquestração carregando planejamento e auditoria juntos | `.claude/skills/scrum-master/SKILL.md`, Passo 1 |
| Despacho por arquivo, sem colar o card na conversa | custo de saída da sessão principal a cada despacho | `.claude/tools/backlog.py despachar` |
| Card só passa se citar a operação do modelo pelo texto vigente | drift entre o que o card diz e o que o modelo de fato diz | `.claude/tools/modelo.py check` (violação `V22`) |
| Promoção de versão do modelo por comando, com validação do consultor | custo de instância do modelador só para mover texto entre seções | `.claude/tools/encerrar.py marco --aceita-versao` |
| Achado com origem no laudo, dedupe por origem, não por texto | achado perdido ou duplicado no fechamento de tarefa | `.claude/tools/encerrar.py tarefa`, `apensar_achado` |
| Achado de instrumento com falha escala ao consultor, qualquer que seja a recomendação do laudo | erro de instrumento preso num laudo "seguir" | `.claude/skills/scrum-master/SKILL.md`, bloco A |
| Todo despacho de subagente abre com a linha que declara plano e tarefa | atribuição errada de telemetria e do painel do gerente | `GOVERNANCA.md` §4.2 |
| Régua de profundidade do planejador pelo tamanho do plano | custo de planejamento desproporcional a um plano pequeno | `.claude/agents/pantonic-planner.md`, Fase 4 |
| Mensagem de marco nomeia a entrega e o pedido de origem do dono | dono ter de perguntar o que a mensagem está pedindo | `.claude/skills/scrum-master/SKILL.md`, "Quando a janela para num marco" |

## Os ganhos, medidos

| medida | antes | depois |
|---|---|---|
| custo de saída da sessão principal por despacho (Passo 4) | 3,06 mil tokens (card colado na conversa, loop real medido na auditoria) | 0,72 mil tokens (despacho por arquivo, variante medida na mesma auditoria, −77%) |
| falsos "âncora ausente" na conferência do despacho, sobre os 41 cards do próprio `P-0755` | 573 falsos positivos em 1.066 linhas (regra da `RAF-T3`) | 0 falsos positivos em 501 linhas (regra da `RAF-T3a`) |
| custo de uma promoção de versão do modelo (aceite de versão pendente, sem conflito) | 55,0 mil tokens (instância própria do modelador, medida na auditoria) | 0 tokens de modelador — comando único (`RAF-T23`); o modelador só é chamado se o comando encontrar conflito |
| testes coletados pela suíte do kit | 521 (referência de 2026-09-28, antes da etapa A) | 630 (`pytest --collect-only -q`, medido nesta entrega, 2026-09-30) |
| `check-readme.ps1` sobre o `README.md` revisado | citava 8 dos 11 instrumentos do kit; nenhuma frase das etapas A-D | cita os 11; 16 das frases-marca das etapas presentes; `exit 0` |

**Não medido nesta entrega** (a própria `R-01` manda medir no próximo loop, ainda não aberto): o custo
por turno da sessão principal no uso real, comparado aos 285,6 mil tokens/turno da auditoria — entra nas
pendências abaixo.

## O padrão que a execução revelou

**Doutrina desatualizada ao lado do código que ela descreve.** Pelo menos oito tarefas corretivas
(`RAF-T8a`, `RAF-T9a`, `RAF-T13a`, `RAF-T26a`, `RAF-T27a`, `RAF-T29a`, `RAF-T31a`, `RAF-T31b`) nasceram
porque um card mudou o comportamento de um instrumento e deixou docstring, `help`, linha de rubrica ou
doutrina de agente dizendo o comportamento antigo. As decisões `DRF-67`, `DRF-69` e `DRF-70` nomeiam a
reincidência explicitamente e fixam a mesma lição de autoria futura: quem muda o comportamento de um
instrumento varre o arquivo inteiro pelas frases que o afirmam (docstring do módulo, das funções,
`help`, doutrina), não só o trecho que um laudo nomeou.

**24 das 64 tarefas do plano são corretivas**, cada uma gerada pelo laudo ou pela triagem do consultor
sobre a entrega da tarefa anterior — quase duas em cada cinco. Nenhuma delas parou a janela: o mecanismo
de achado → consultor → card corretivo (`T<n>a`/`T<n>b`) funcionou como projetado nas 87 linhas de
achado (`AE-<n>`) e nas 75 decisões (`DRF-<n>`) registradas na execução.

## Pendências abertas ao fim do plano

| pendência | por que ficou aberta | o que a fecha | bloqueia algo? |
|---|---|---|---|
| `dead_code.py` acusa `docs/audits/sonda-2026-09-28/passos.py:13` (🔴 regra escrita, aplicação pendente) | a decisão `DRF-44` (Marco 2) registrou o achado sem abrir card nem tíquete, por diretiva do dono de 2026-09-26; a sonda, fora de controle de versão, ficou fora do alcance de todo card do plano; reincidiu em pelo menos 15 achados (`AE-121`, `AE-123`, `AE-154`, `AE-160`, `AE-168`, `AE-169`, `AE-182`, `AE-184`, `AE-189`, `AE-192`, `AE-194`, `AE-195`, `AE-197`, `AE-199`, `AE-201`..`AE-206`), do primeiro card ao último; confirmado ainda vermelho nesta entrega (`python .claude/checks/dead_code.py` → `dead_code: FALHOU - 1 achado(s)`) | versionar ou remover a sonda, ou excluir `docs/audits/` da varredura do `dead_code.py`, por decisão da condução | não bloqueia entrega de card algum; obriga cada revisão do plano a reconciliar o vermelho à mão |
| custo por turno da sessão principal no uso real (`R-01`) | a própria verificação da recomendação manda medir no próximo loop de execução, que ainda não abriu depois deste plano | rodar `.claude/tools/custo_sessao.py` sobre o transcript da próxima janela e comparar aos 285,6 mil tokens/turno da auditoria | não bloqueia; é a única forma de confirmar o ganho central que motivou a etapa A |
| `R-29` (limitar o `next` ao plano corrente) | registrada sem ação por decisão do dono (`DRF-3`); a `R-15` já fechou a causa que a motivou | decisão futura do dono, se o caso reaparecer | não bloqueia |
| guarda mecânica contra `git` que escreve na árvore compartilhada (`stash`, `reset`, `checkout --`, `restore`) durante a execução | `DRF-56` documentou a regra como restrição de escopo dos cards; a guarda por hook ficou com rota "auditoria final", pela diretiva de 2026-09-26 | um hook `PreToolUse` que recuse esses comandos na árvore do repositório durante a execução | não bloqueia; hoje depende de o executor ler a restrição |
| mecanização das duas saídas do card de operação nova bloqueado no marco (`DRF-63`) | a saída manual (comando `status ready` ou remoção pelo consultor) é a `DRF-5` como está escrita; automatizar mudaria o desenho de quem passa o card a `ready` | decisão futura sobre mecanizar `encerrar.py marco` para também mudar o status do card | não bloqueia |
| `docs/DOC_MAP.md:7` desatualizado (`F-30`) e módulos de `.claude/tools/` fora dos onze citados pelo `README.md` revisado (`rdo.py`, `telemetria.py`, `caminhos.py`, `agentdef.py`, `ocupacao.py`, `crenca_hook.py`) | fora do escopo explícito deste plano (§7) | tíquete próprio, a critério da condução | não bloqueia |

**Resumo do estado:** as 64 tarefas do plano (40 principais mais 24 corretivas) estão `done`; as etapas
A a D já passaram por marco com veredito `go` do dono, e a etapa E está pronta para o Marco 6. Seis
pendências seguem abertas — uma delas (`dead_code` sobre a sonda da auditoria) é o único item com efeito
visível fora deste plano: aparece em toda evidência futura do kit até que a condução decida versionar,
remover a sonda ou ajustar a varredura.
