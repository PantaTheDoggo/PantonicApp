# Operações — Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor

## Abertura

**O problema:** a auditoria de encerramento do estágio 1 do kit
(`docs/audits/AUDITORIA_ENCERRAMENTO_ESTAGIO1_2026-09-27.md`) mediu 58 registros de inadequação e
dezoito recomendações, mais dois tíquetes que o consultor tinha deixado prontos. Os números que
pesaram:
- quem conduz o loop repetia **seis atos mecânicos à mão** a cada despacho de tarefa;
- o consumo impresso do plano **subestimava cerca de 66%** (399,6 mil tokens contra ≈ 1.168 mil),
  porque só o executor gravava telemetria;
- o resumo de diferenças que o revisor recebe listava **59 arquivos** de trabalho em andamento
  alheio à tarefa;
- o card chegava ao executor **cortado em 8.000 caracteres / 120 linhas**;
- o batedor, agente de coleta que rodava no modelo mais barato, errou contagens grandes **sem
  avisar** (246 em vez de 325).

**A solução, em uma frase:** o que quem conduz fazia de memória virou comando, e cada leitura que
decidia rota (a do revisor, a do consultor, a do batedor) passou a chegar inteira e medida.

| termo | o que é |
|---|---|
| condutor | quem conduz o loop de execução (skill `scrum-master`, no contexto principal): despacha cada tarefa e roteia pelo veredito |
| card | a seção `### <ID>` de uma tarefa no plano: objetivo, arquivos-alvo, passos, verificações — tudo o que o executor recebe |
| dossiê de evidência | arquivo gerado por `review_evidence.py` antes da revisão: o que mudou na árvore desde o despacho, quem tocou o quê, testes e guardas |
| laudo | o julgamento do revisor sobre uma tarefa: veredito, percentual, recomendação e achados |
| achado (`AE-<n>`) | registro de defeito ou observação na seção `## 9` do plano, sempre com uma rota (quem o fecha) |
| série de telemetria | `docs/telemetria.tsv`: uma linha por rodada de agente, com modelo, ferramentas usadas, milhares de tokens e duração |
| plano em pasta | plano cujo arquivo mora em `docs/plans/P-<n>-<slug>/plano.md`, com a situação de cada tarefa em `estado.tsv` na mesma pasta |
| batedor | o agente de coleta (`pantonic-scout` no projeto, `context-scout` na camada global): busca, lê e devolve um resumo compacto |

## O arco

Os estratos são, na maior parte, independentes entre si: cada um fecha uma classe de trabalho à
mão. A dependência forte é a do último — o guia de entrada só pode descrever o kit depois que os
outros quatro o mudaram.

| estrato | pergunta que responde | tarefas |
|---|---|---|
| 1. O que o revisor e o loop leem | o julgamento de uma tarefa parte da evidência certa, e o veredito chega ao loop sem reabrir arquivo? | `AF-T1`, `AF-T2`, `AF-T4`, `AF-T6`, `AF-T7` |
| 2. Condução sem ato à mão | o condutor despacha, registra e fecha por comando, e o painel e a telemetria veem tudo? | `AF-T3`, `AF-T5`, `AF-T9`, `AF-T10`, `AF-T12`, `AF-T13` |
| 3. Conferências que faltavam | os verificadores do kit acusam o que deveriam, sem falso alarme nem silêncio? | `AF-T8`, `AF-T14`, `AF-T15`, `AF-T16` |
| 4. Papéis com a leitura certa | planejador, consultor e batedor leem só o que precisam e acertam o que leem? | `AF-T11`, `AF-T17`, `AF-T19a`, `AF-T21` |
| 5. O kit como ficou | sai o que é obsoleto, e o guia descreve o resultado? | `AF-T20`, `AF-T18` |

Fora dos estratos: `AF-T19` (`cancelled`) — a primeira rota para o batedor, que só separava as
perguntas de leitura das de comando. Foi substituída por `AF-T19a` depois de uma avaliação medida
do batedor em três modelos, que levou o dono a escolher outra rota (ver `AF-T19a`).

| tarefa | título | status |
|---|---|---|
| `AF-T1` | Com `--desde`, o resumo de diferenças do dossiê sai do recorte dos tocados | done |
| `AF-T2` | O relatório de auditoria de quem conduz entra no balde de registro da orquestração | done |
| `AF-T3` | O painel do gerente reconhece o programa depois das opções do interpretador | done |
| `AF-T4` | O fechamento transcreve o achado de processo do laudo para os achados do plano | done |
| `AF-T5` | O gancho de telemetria grava todo papel do kit, e a soma do plano os separa | done |
| `AF-T6` | A recomendação do laudo viaja na primeira linha do revisor | done |
| `AF-T7` | A conferência do card lê a situação da tarefa no estado do plano em pasta | done |
| `AF-T8` | A conferência do backlog aceita o plano em esboço, e o planejador o registra no esboço | done |
| `AF-T9` | O `next` e o `show` entregam o card inteiro | done |
| `AF-T10` | Um verbo `despachar` roda as conferências do despacho e recusa pela primeira que falhar | done |
| `AF-T11` | O consultor lê só as três entradas, e `estrategico=` é uma frase | done |
| `AF-T12` | O veredito do marco é um comando | done |
| `AF-T13` | O esqueleto do relatório de operações sai por comando | done |
| `AF-T14` | A conferência do modelo julga a versão pendente, e a comparação mostra o contrato | done |
| `AF-T15` | O piso comportamental e o teste de camadas passam a existir no hub | done |
| `AF-T16` | Os verificadores em PowerShell escrevem UTF-8 no console | done |
| `AF-T17` | O pré-voo do pedido confere o que o dono cita antes da campanha | done |
| `AF-T18` | O guia de entrada descreve o kit como ele fica | done |
| `AF-T19` | A campanha do planejador separa as perguntas de leitura das de comando | cancelled |
| `AF-T19a` | O batedor roda no Opus, com a ferramenta de comando, e o kit deixa de mandar a coleta ao modelo barato | done |
| `AF-T20` | `uow.py` sai do kit | done |
| `AF-T21` | A auto-auditoria do planejador se dosa pela classe do plano | done |

## `AF-T1` — O resumo de diferenças mostra só o que a tarefa tocou

**Contexto que a motivou:** o bloco `## Diff` do dossiê de evidência era um `git diff --stat` contra
o último commit. Com 59 arquivos de trabalho em andamento na árvore, o revisor recebia 59 linhas, e
só algumas eram da tarefa.

**O que é o artefato:** a função `coletar_diff_stat(root, desde=None)` em
`.claude/tools/review_evidence.py`. Com a opção `--desde <ref>` (o instantâneo da árvore tirado no
despacho), ela recorta o resumo pelos arquivos tocados desde aquele instante, rastreados ou não.

**Como funciona na prática:**
1. **O que dispara:** o condutor roda `review_evidence.py --plano <plano> --tarefa <ID> --desde <ref>` antes de chamar o revisor.
2. **A entrada:** o `<ref>` gravado no despacho e a árvore atual.
3. **O processamento:** calcula os arquivos tocados desde o `<ref>` e roda o `--stat` só sobre eles.
4. **A saída:** no dossiê da `AF-T19a`, o bloco `## Diff` terminou em `18 files changed, 79 insertions(+), 40 deletions(-)`, e são exatamente os 18 nomes da lista `## Arquivos tocados` do mesmo dossiê. Sem `--desde`, nada muda.

**Protege contra:** o revisor julgar a tarefa pelo trabalho alheio que estava na árvore.

## `AF-T2` — O relatório de auditoria de quem conduz não conta contra a tarefa

**Contexto que a motivou:** um arquivo que o condutor grava em `docs/audits/` durante a janela
aparecia no dossiê como "fora dos alvos e sem atribuição", como se o executor tivesse saído do
escopo.

**O que é o artefato:** a tupla `_REGISTRO_ORQUESTRACAO` em `.claude/tools/review_evidence.py`,
que lista os caminhos que são registro da condução, e não entrega. `docs/audits/` entrou nela.

**Como funciona na prática:** o dossiê separa os arquivos tocados em grupos. No da `AF-T19a`, a
linha foi: `Registro da orquestração (não atribuível a tarefa): docs/DIARIO_DE_OBRAS.md,
docs/plans/P-0753-auditoria-estagio-1/cenario.md, … docs/telemetria.tsv`. Um arquivo sob
`docs/audits/` cai nesse mesmo grupo. Se `docs/audits/` for alvo do card, ele continua contando
como entrega.

**Protege contra:** entrega correta rebaixada por um arquivo que o próprio condutor escreveu.

## `AF-T3` — O painel do gerente vê o comando mesmo com `python -X utf8`

**Contexto que a motivou:** o painel do gerente (`.claude/estado/progresso.txt`) recebe uma frase
por transição do loop, gerada pelo gancho `.claude/tools/progresso_hook.py` a partir do comando que
rodou. A função `_programa` pulava todo token iniciado por `-` e tomava o seguinte como o script.
Com `python -X utf8 .claude/tools/backlog.py status`, o "script" virava `utf8`, e cinco frases do
painel não saíam.

**O que é o artefato:** `_programa` em `.claude/tools/progresso_hook.py`, que agora pula `-X` e `-W`
com o valor (separado ou colado), devolve o módulo depois de `-m` e devolve nada para `-c`. A
armadilha está registrada em `docs/ARMADILHAS_DE_FERRAMENTA.md`.

**Como funciona na prática:** medido em 2026-09-27:
`_programa(['python','-X','utf8','.claude/tools/backlog.py','status'])` devolve
`('backlog.py', ['status'])`. Antes devolvia `utf8`.

**Protege contra:** o painel ficar mudo justamente quando se usa a opção que o próprio kit
recomenda para acentos no Windows.

## `AF-T4` — Os achados do laudo entram no plano sem ninguém redigitar

**Contexto que a motivou:** o fechamento de tarefa (`encerrar.py tarefa`) lia do laudo os cinco
campos do veredito, mas ignorava a tabela `## Achado de processo`. O achado só chegava ao plano se
o condutor lembrasse de repassá-lo, e na janela medida ele esqueceu.

**O que é o artefato:** a função `achados_do_laudo` em `.claude/tools/encerrar.py`, chamada no
fechamento depois dos `--achado` que o condutor passar, sem repetir texto já registrado. O Passo 9,
item (5), da skill `scrum-master` descreve o comportamento.

**Como funciona na prática:** no fechamento da `AF-T19a` (2026-09-27), o condutor passou um
`--achado`, e o laudo tinha duas linhas de achado de processo. A saída do comando foi
`Achados: AE-26, AE-27, AE-28.` O `AE-26` veio do `--achado`; o `AE-27` e o `AE-28` foram copiados
do laudo, cada um com a rota que o revisor declarou.

**Protege contra:** achado que morre com o laudo porque ninguém o transcreveu.

## `AF-T5` — A telemetria grava todos os papéis, não só o executor

**Contexto que a motivou:** o gancho `SubagentStop` (evento que o Claude Code dispara quando um
subagente termina) só gravava a rodada do `pantonic-executor`. As rodadas do revisor e do consultor
entravam à mão ou não entravam, e o consumo impresso de um plano medido ficou 66% abaixo do real.

**O que é o artefato:** `processar` em `.claude/tools/telemetria_hook.py`, que grava a rodada de
todo agente `pantonic-*` com o papel no identificador: `<ID>` para o executor, `<ID>-revisao`,
`<ID>-consultor-<n>`, `<P-n>-planejador`/`-modelador`/`-scout`. Ela também deixou de apagar
`.claude/estado/tarefa-corrente.json`, que agora vale até o próximo despacho. `_consumo_do_plano`,
em `.claude/tools/encerrar.py`, separa os papéis na soma.

**Como funciona na prática:** linhas gravadas pelo gancho na janela de 2026-09-27, sem nenhum
argumento do condutor:

```
2026-09-27	PantonicApp	AF-T19a-consultor-1	opus	22	56.1	259.5	usage
2026-09-27	PantonicApp	AF-T19a	sonnet	9	54.1	72.2	usage
2026-09-27	PantonicApp	AF-T19a-revisao	opus	23	78.5	197.1	usage
```

**Protege contra:** decisão de custo tomada sobre um consumo que omite dois terços do gasto.

## `AF-T6` — O revisor devolve a recomendação na primeira linha

**Contexto que a motivou:** o loop roteia pela recomendação do revisor (`seguir`,
`seguir com ressalva`, `refazer`, `escalar`), mas a linha de retorno trazia só veredito, percentual
e dimensão bloqueante. O condutor tinha de abrir o laudo para decidir.

**O que é o artefato:** o passo 7 de `.claude/agents/pantonic-reviewer.md` (forma da linha), o
Passo 7 da skill `scrum-master` (onde o loop a lê) e a frase `M-7` do painel, em
`.claude/tools/progresso_hook.py`, que passa a mostrar a recomendação.

**Como funciona na prática:** a linha real devolvida pelo revisor da `AF-T19a`:
`AF-T19a ressalva 93% bloqueante=nenhuma recomendacao=seguir com ressalva`. O loop aplicou a regra
de "seguir com ressalva" direto dela. Sem o campo, o painel escreve "recomendação não informada".

**Protege contra:** o loop rotear pela interpretação que o condutor faz do laudo, e não pelo campo
que o revisor calculou.

## `AF-T7` — A conferência do card sabe se a tarefa já foi feita

**Contexto que a motivou:** o `card_check.py` compara os valores que o card declara (o "antes" e o
"depois" de cada verificação) com a árvore real. Em plano em pasta, ele não lia `estado.tsv` e
imprimia `status ausente: comparando antes`, até para tarefa já `done`, cuja árvore está no
"depois".

**O que é o artefato:** `verificar_tarefa` em `.claude/tools/card_check.py`, que passa a pasta do
plano a `rdo._status_atual`. A situação da tarefa vem de `estado.tsv`: `done` compara com o
"depois", e o resto compara com o "antes".

**Como funciona na prática:** `python .claude/tools/card_check.py --plano
docs/plans/P-0753-auditoria-estagio-1/plano.md --tarefa AF-T1` saiu, em 2026-09-27,
`card_check: OK - tarefa 'AF-T1' fecha.`, sem a linha "status ausente". A `AF-T1` está `done`, e a
árvore bate com o "depois".

**Protege contra:** falso vermelho sobre tarefa pronta e, pior, falso verde sobre tarefa que
regrediu.

## `AF-T8` — Um plano em esboço passa pela conferência do backlog

**Contexto que a motivou:** enquanto o planejador escreve um plano novo em pasta, existe um estado
intermediário: `estado.tsv` só com a linha do plano, `blocked`, e o plano ainda fora do inbox.
Nesse estado, `backlog.py check` recusava com
`C-10 docs/plans/_INBOX.md:5 — contador aponta para P-0753, já presente em docs/plans/`, e o
planejador improvisava um registro antecipado.

**O que é o artefato:** o predicado `_plano_em_esboco` em `.claude/tools/backlog.py`, que deixa de
fora da regra `C-10` o plano em pasta em esboço cujo id é o do contador. As Fases 3a e 5 de
`.claude/agents/pantonic-planner.md` e a skill `diario-de-obras` mandam gravar `estado.tsv` já no
esboço.

**Como funciona na prática:** sobre a fixture desse estado, em 2026-09-27,
`python .claude/tools/backlog.py check --repo tests/fixtures/backlog/esqueleto` sai
`check: OK — nenhuma violação.`, com exit 0. Um plano **legado** `blocked` com o id do contador
continua acusando `C-10`: o teste `test_tr_check_plano_legado_blocked_no_contador_segue_acusando_c10`
tranca isso.

**Protege contra:** o planejador contornar o instrumento com um registro que ninguém revisou.

## `AF-T9` — O card chega inteiro a quem executa

**Contexto que a motivou:** `backlog.py next` e `show` cortavam o card em 8.000 caracteres ou 120
linhas, muitas vezes no meio de `Passos` ou de `Restrições`. O condutor relia o trecho no plano
para completar o despacho.

**O que é o artefato:** `_card_inteiro` em `.claude/tools/backlog.py`, usada pelo `next` e pelo
`show` de tarefa. Ela entrega o card até `- **Notas de execução:**`; as notas e os achados
continuam com teto. O `show` de plano segue truncado.

**Como funciona na prática:** no despacho da `AF-T19a` (2026-09-27), a saída trouxe o card de ponta
a ponta: os 13 passos, as restrições, as contingências e as seis verificações, até
`- **Fora do escopo desta tarefa:**`. O card tem mais de 120 linhas.

**Protege contra:** executor trabalhando sobre um card sem as restrições do fim.

## `AF-T10` — Despachar uma tarefa é um comando

**Contexto que a motivou:** a cada despacho, o condutor rodava seis atos idênticos: a conferência
do modelo, a do card, a coleta da suíte, a mudança para `in-progress`, a gravação de
`tarefa-corrente.json` à mão e a captura do `<ref>`.

**O que é o artefato:** o verbo `python .claude/tools/backlog.py despachar <ID>` (função
`despachar`). Ele roda as conferências nesta ordem e recusa pela primeira que falhar, sem escrever
nada. Passando todas, muda a tarefa para `in-progress`, grava `tarefa-corrente.json` e imprime o
card, o handover da tarefa anterior e o `ref=`. No redespacho da mesma tarefa, reaproveita o `<ref>`
do primeiro despacho.

**Como funciona na prática:** saídas reais de 2026-09-27, na mesma tarefa:
- recusa: `despachar: recusado — card_check: card_check: FALHOU - 4 item(ns) da tarefa 'AF-T19a' não fecham.` (exit 1, nada gravado);
- aceite: `=== DESPACHO: AF-T19a — O batedor roda no Opus, …`, seguido do card e de `ref=b3ba047cb323ed0e5ba6e3a40ffc1792f27b605a`, o mesmo `<ref>` do primeiro despacho.

**Protege contra:** esquecer um dos seis atos, e despachar tarefa cujo card não confere com a
árvore.

## `AF-T11` — O consultor lê só o que recebe

**Contexto que a motivou:** o consultor (`pantonic-consultant`, que decide a rota de toda parada)
leu o relatório de auditoria inteiro num acionamento e custou 131,2 mil tokens. A linha
`estrategico=`, que para a janela para o dono decidir, veio em três frases.

**O que é o artefato:** o item 1 de `.claude/agents/pantonic-consultant.md` ("lê só as três
entradas") e o item 2 (a regra de uma frase para `estrategico=`). A seção *Acionamento do
consultor* da skill `scrum-master` traz o molde do despacho.

**Como funciona na prática:** o despacho real do consultor na `AF-T19a` foi só isto: `cenario=`
(o arquivo de handover do plano), `card=AF-T19a` e `evidencia=` (a linha de retorno do executor,
verbatim). A instância devolveu `rota=resolve` e custou 56,1 mil tokens, segundo a série de
telemetria.

**Protege contra:** consultor caro por leitura que não muda a decisão, e parada estratégica
ilegível.

## `AF-T12` — O veredito do dono num marco se grava por comando

**Contexto que a motivou:** o veredito de um marco não tinha quem o escrevesse. A tabela de
marcos, a `## 0` do plano, o cenário do consultor e `estado.tsv` ficavam defasados entre si a cada
marco.

**O que é o artefato:** o subcomando
`encerrar.py marco --plano <plano> --marco <n> --resultado {go,no-go} --veredito "<frase>"`
(função `gravar_marco`). Ele grava a célula do marco e o ato na `## 0` e, no Marco 1 `go` com plano
`blocked`, a passagem a `ready`. Com `--aceita-versao` ou `--recusa-versao`, imprime o pedido ao
modelador. Todas as checagens rodam antes da primeira escrita.

**Como funciona na prática:** o veredito do Marco 2 deste plano é o primeiro caso real que ele
grava. As bordas corrigidas no fechamento (a célula com `|` escapado, gravada duas vezes, e a
passagem recusada depois de gravar) têm um teste de regressão cada em `tests/test_encerrar.py`.

**Protege contra:** quatro registros do mesmo veredito divergindo entre si.

## `AF-T13` — O esqueleto deste documento sai por comando

**Contexto que a motivou:** o relatório de operações de cada plano era reescrito de memória a
partir da estrutura da skill `entrega-de-encerramento`.

**O que é o artefato:** o subcomando `encerrar.py operacoes --plano <plano>`, que grava o esqueleto
(tabela do arco e uma seção por tarefa viva, com os quatro blocos vazios) e recusa se o arquivo já
existe. Com `--checar`, ele não escreve e confere a cobertura: `nao citados`, `sem seção` e
`sem os quatro blocos`.

**Como funciona na prática:** este documento nasceu de
`encerrar: OK - esqueleto de operações gravado em 'docs/plans/P-0753-auditoria-estagio-1/operacoes.md'.`
(2026-09-27). O caminho do plano pode ser relativo ou absoluto: com o relativo, o comando quebrava
até ser corrigido no fechamento (`AE-29`), e o teste `test_tr_esqueleto_de_operacoes_plano_relativo`
tranca o caso.

**Protege contra:** relatório de fechamento que esquece uma tarefa ou uma das quatro perguntas.

## `AF-T14` — A conferência do modelo julga também a versão pendente

**Contexto que a motivou:** a seção `## 1` do plano é o modelo de domínio (operações, objetos,
estados). Uma emenda proposta mora em `## 1A` como "versão pendente" até o dono aceitar.
`modelo.py check` só conferia a `## 1`, e a comparação `show --drift` não mostrava contrato
alterado.

**O que é o artefato:** em `.claude/tools/modelo.py`, `validar(pendente=True)` roda as mesmas
regras sobre a `## 1A`, e o `check` soma as violações com o prefixo `1A: `. `_diff_objetos` passa a
mostrar `[~] <objeto> — contrato: <vigente> => <pendente>`.

**Como funciona na prática:** `python .claude/tools/modelo.py check --plano
docs/plans/P-0753-auditoria-estagio-1/plano.md` saiu, em 2026-09-27,
`modelo: OK — 21 operações, 21 objetos, 30 propriedades, 22 tarefas, versão 3`. No fechamento da
`AF-T14`, o mesmo `check` saiu 0 com a versão 2 pendente presente no plano, já exercitando a
conferência nova (`AE-20`).

**Protege contra:** o dono aceitar uma emenda que nenhuma regra conferiu.

## `AF-T15` — O hub passa a ter piso de testes e teste de camadas

**Contexto que a motivou:** `tests/conformance/` e `tests/piso_comportamental.txt` não existiam no
hub. O `ratchet_piso` saía 0 por "nenhum piso declarado", e a skill `guardrails-check` chamava de
obrigatória uma conferência que não existia.

**O que é o artefato:**
- `tests/piso_comportamental.txt`: a lista dos testes de regressão que não podem sumir, conferida por `.claude/checks/ratchet_piso.py`;
- `tests/conformance/test_camadas_do_kit.py`: proíbe que um instrumento do kit importe de `tests` ou de `caminhos`.

**Como funciona na prática:** medido em 2026-09-27:
- o piso tem 128 entradas;
- `ratchet_piso.py` sai `ratchet_piso: OK - piso intacto sob 'D:\workspaces\PantonicApp' (…\tests\piso_comportamental.txt).`;
- `pytest tests/conformance` sai `2 passed`.

**Protege contra:** apagar um teste de regressão sem ninguém notar, e instrumento do kit que só
funciona com a pasta de testes presente.

## `AF-T16` — Os verificadores em PowerShell mostram acento

**Contexto que a motivou:** `check-readme.ps1` imprimia o caractere de substituição no lugar dos
acentos (`vers�o`) quando a saída era capturada: 8 ocorrências em 2026-09-27.

**O que é o artefato:** a linha `[Console]::OutputEncoding = [Text.Encoding]::UTF8`, logo depois de
`$ErrorActionPreference`, em `.claude/checks/check-readme.ps1` e em `.claude/checks/kit_check.ps1`.

**Como funciona na prática:** a saída capturada em 2026-09-27 foi
`check-readme: OK - 10 agente(s), 13 skill(s), 20 guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida; …`,
com `versão` e `seção` legíveis.

**Protege contra:** agente lendo mensagem de verificador corrompida e decidindo sobre ela.

## `AF-T17` — O planejador confere o que o dono cita antes de planejar

**Contexto que a motivou:** uma premissa falsa no pedido do dono (uma função que não existia)
custou uma instância inteira do planejador, 41,4 mil tokens, mais a campanha de coleta. Um grep a
teria revelado.

**O que é o artefato:** o instrumento `.claude/tools/prevoo.py`. Ele recebe o texto do pedido,
extrai os caminhos, as funções e as opções citadas e diz se cada um existe na árvore e onde. Exit 0
quando tudo existe, 1 quando algo falta. A Fase 0 de `.claude/agents/pantonic-planner.md` manda
rodá-lo antes da campanha.

**Como funciona na prática:** saída real de 2026-09-27, com exit 1:

```
$ python .claude/tools/prevoo.py "Mude .claude/tools/backlog.py e .claude/tools/naoexiste.py, a funcao _card_inteiro() e a flag --desde"
citado | existe | onde
.claude/tools/backlog.py | sim | .claude/tools/backlog.py
.claude/tools/naoexiste.py | não | —
_card_inteiro | sim | .claude/tools/backlog.py:1123
--desde | sim | .claude/tools/review_evidence.py:970
```

A leitura aceita citação em crase, com pontuação e na forma de chamada (`nome()`), correção feita
no fechamento com três testes de regressão.

**Protege contra:** planejar em cima de algo que não existe.

## `AF-T18` — O guia de entrada descreve o kit como ele ficou

**Contexto que a motivou:** o `README.md` da raiz descrevia os instrumentos como eram antes desta
janela: sem `despachar`, sem `marco` e `operacoes`, sem o pré-voo, sem a versão pendente do modelo e
com a telemetria só do executor.

**O que é o artefato:** as seções do `README.md` sobre `backlog.py` (oito verbos, com
`despachar`), `encerrar.py` (cinco verbos, com `marco` e `operacoes`), `prevoo.py`, o `check` e o
`show --drift` do modelo sobre a versão pendente e a telemetria gravada pelo gancho `SubagentStop`.

**Como funciona na prática:** `pwsh -NoProfile -File .claude/checks/check-readme.ps1`, que confere
o guia contra a árvore, sai exit 0 em 2026-09-27 (saída na `AF-T16`).

**Protege contra:** quem chega ao kit aprender um procedimento que não existe mais.

## `AF-T19a` — O batedor roda no Opus e pode rodar comando de consulta

**Contexto que a motivou:** o batedor rodava no Haiku, só com ferramentas de leitura, e o
planejador mandava a ele perguntas do tipo "rode `<comando>`", que ele não podia rodar. A avaliação
de 2026-09-27 comparou os três modelos em quatro coletas deste repositório:

| modelo | coletas pequenas | coletas grandes | tokens gastos nas grandes |
|---|---|---|---|
| Haiku | acertou as duas | errou as contagens sem avisar (246 em vez de 325; 3 de 16 certas) | 67,0 mil e 85,6 mil |
| Sonnet | acertou as duas | acertou uma; na outra, 11 de 16, com o erro declarado | 87,8 mil e 149,5 mil |
| Opus | acertou as duas | acertou as duas | 33,4 mil e 88,9 mil |

**O que é o artefato:** o frontmatter e as regras dos dois batedores
(`.claude/agents/pantonic-scout.md` e o canônico global `.claude/global/agents/context-scout.md`),
agora com `model: opus` e `tools: Read, Glob, Grep, Bash`. Duas regras novas:
- **Comando de consulta:** o batedor roda verbatim o comando que a pergunta traz e devolve a saída literal e o exit; nunca roda comando que escreva na árvore;
- **Contagem e filtro:** o número vem da ferramenta, nunca de soma à mão.

A linha *Coleta* de `GOVERNANCA.md` §3, os dois README, cinco skills, o gancho global de modelo por
fase e `.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md` deixaram de mandar a coleta ao modelo
barato. Leitura pontual (âncora conhecida, grep exato), quem precisa do dado faz direto.

**Como funciona na prática:** a verificação 3 do card conta a palavra `haiku` nos doze arquivos
tocados: era 27 e ficou 8. As 8 que restam são a ordem de modelos e o `pantonic-benchmarker`, fora
do batedor. `kit_check.ps1 -Mode check-drift` sai
`kit_check: check-drift OK - .claude/README.md == regenerado (10 agente(s), 13 skill(s)); …`.

**Protege contra:** a coleta, que alimenta toda decisão seguinte, errar uma contagem em silêncio.

## `AF-T20` — `uow.py` sai do kit

**Contexto que a motivou:** `.claude/tools/uow.py` não era citado por nenhuma skill, agente, teste
ou verificador. A docstring apontava para uma regra da doutrina global que hoje é outra, e o
`status` sem unidade aberta saía 0 com `erro:` no texto.

**O que é o artefato:** o arquivo apagado. A docstring de `.claude/tools/backlog.py`, que o citava
como precedente de desenho, passou a citar só `telemetria.py`.

**Como funciona na prática:** `Test-Path .claude/tools/uow.py` → `False` (2026-09-27). A suíte
segue com 498 testes coletados.

**Protege contra:** instrumento morto que confunde quem lê o kit, confusão que o dono relatou.

## `AF-T21` — O planejador dosa a auto-auditoria pelo tamanho do plano

**Contexto que a motivou:** planejar 3 operações custou 319 mil tokens em três instâncias. A
auto-auditoria da Fase 4 (14 itens) e o ensaio em cópia foram aplicados inteiros, qualquer que
fosse o porte do plano.

**O que é o artefato:** em `.claude/agents/pantonic-planner.md`, o esqueleto da Fase 3a passa a
declarar a **classe do plano** no cabeçalho, e a Fase 4 abre com "Profundidade pela classe do
plano": uma tabela que diz quais itens da auto-auditoria valem em cada classe.

**Como funciona na prática:** o planejador lê a classe no cabeçalho do plano que ele mesmo gravou
na Fase 3a e aplica a linha correspondente da tabela da Fase 4. O primeiro plano a nascer com a
classe declarada é o próximo que o planejador escrever.

**Protege contra:** gastar a auditoria completa num plano pequeno, ou uma auditoria rasa num
plano grande.

## O que vale além deste plano

| regra | o que resolve | residência |
|---|---|---|
| Despacho por comando | os seis atos do despacho viram um | skill `scrum-master`, Passo 3 |
| Veredito de marco por comando | um registro por veredito, nos quatro lugares | skill `scrum-master`, *Relatório de encerramento*; `encerrar.py marco` |
| Esqueleto de operações por comando | este documento parte de estrutura gerada e é conferido por `--checar` | skill `entrega-de-encerramento`, Procedimento itens 4 e 6 |
| Recomendação na linha do revisor | o loop roteia sem abrir o laudo | `.claude/agents/pantonic-reviewer.md`, passo 7 |
| Consultor lê três entradas; parada estratégica em uma frase | triagem barata e legível | `.claude/agents/pantonic-consultant.md`, itens 1 e 2 |
| Telemetria de todo papel pelo gancho | consumo real do plano, sem linha à mão | `GOVERNANCA.md` §4.2 |
| Pré-voo do pedido | premissa falsa descoberta antes da campanha | `.claude/agents/pantonic-planner.md`, Fase 0 |
| Profundidade da auto-auditoria pela classe | custo de planejamento proporcional ao plano | `.claude/agents/pantonic-planner.md`, Fase 4 |
| Coleta no Opus; leitura pontual direto | coleta sem erro silencioso | `GOVERNANCA.md` §3, linha *Coleta* |

## Os ganhos, medidos

| medida | antes | depois |
|---|---|---|
| Atos do condutor por despacho | 6, à mão | 1 comando (`backlog.py despachar`) |
| Arquivos no resumo de diferenças do dossiê | 59 (todo o trabalho em andamento) | 18 na `AF-T19a`, exatamente os tocados |
| Papéis gravados pelo gancho de telemetria | só o executor | todos: neste plano, 30 linhas de executor, 17 de revisor, 11 de consultor e 6 de modelador (série em 2026-09-27) |
| Tamanho do card no despacho | cortado em 8.000 caracteres / 120 linhas | inteiro |
| Acento corrompido na saída de `check-readme.ps1` | 8 ocorrências | 0 |
| Ocorrências de `haiku` nos 12 arquivos da coleta | 27 | 8 (fora do batedor) |
| Testes coletados pela suíte | 452 | 505 |
| Entradas no piso comportamental do hub | arquivo inexistente | 134 |

O consumo total do plano por papel sai no relatório de entrega que `encerrar.py plano` escreve;
este documento não o soma à mão.

## O padrão que a execução revelou

**O card prometia o que ninguém tinha rodado.** Dez vezes na janela, o consultor teve de reparar
um card cujo texto contradizia a árvore: uma contingência que enumerava testes sem varredura
(`DAF-37`, `DAF-38`), uma fixture que o instrumento recusava (`DAF-39`), um teste que só
discriminava uma das cláusulas da regra (`DAF-40`), uma montagem de teste que faltava (`DAF-41`),
texto atravessando processo sem codificação fixada (`DAF-42`), um verbo que relê o próprio formato
sem teste de ida e volta (`DAF-43`), uma conferência de cobertura sem teste por forma de ausência
(`DAF-44`), uma leitura de texto do dono sem normalização (`DAF-45`) e uma contingência sobre a
saída de um gerador que ninguém rodou (`DAF-47`). Nenhuma dessas paradas foi erro do executor:
todas pararam pela contingência do próprio card.

| defeito | estado | o que fecha |
|---|---|---|
| Predicado do esboço sem a cláusula *plano em pasta* (`DAF-40`) | 🟢 Fechado com guarda — teste de regressão dedicado | — |
| Mensagem de recusa do `despachar` em codificação errada (`DAF-42`) | 🟢 Fechado com guarda | — |
| Veredito de marco regravado com resto do anterior; escrita antes da checagem (`DAF-43`) | 🟢 Fechado com guarda — um teste por caminho | — |
| `--checar` não acusava seção apagada (`DAF-44`) | 🟢 Fechado com guarda | — |
| Pré-voo sem ler citação em crase, pontuada ou em chamada (`DAF-45`) | 🟢 Fechado com guarda — três testes, no piso | — |
| `encerrar.py operacoes` quebrava com o caminho do plano relativo (`AE-29`) | 🟢 Fechado com guarda — teste de regressão no piso | — |
| O registro de acionamentos do consultor saía no dossiê como "fora dos alvos" (`AE-4`, repetido em `AE-6`, `AE-9`, `AE-15`, `AE-28`) | 🟢 Fechado com guarda — o arquivo entrou no grupo de registro da condução; teste no piso | — |
| Exercitar o gancho de telemetria com estado de teste gravava na série real (`AE-5`) | 🟢 Fechado com guarda — o gancho grava sempre na série do repositório do estado; teste no piso | — |
| Redespacho de tarefa já aplicada não passava pelo `despachar` (`AE-26`) | 🟢 Fechado com guarda — `despachar <ID> --mundo depois`; teste no piso | — |
| O teste da guarda "sem arquivo tocado, o resumo sai vazio" passava com ou sem a guarda (`AE-3`) | 🟢 Fechado com guarda — teste novo que cai sem a guarda, no piso | — |
| O teste do card inteiro não passava pelo leitor do plano nem pela linha de comando (`AE-12`) | 🟢 Fechado com guarda — teste sobre plano gravado em disco, pelos dois verbos | — |
| O aviso de corte dos achados apontava o plano inteiro, e não a seção de achados (`AE-11`) | 🟢 Fechado com guarda — teste no piso | — |
| O consultor era mandado a ler "só as três entradas" e, no mesmo arquivo, a ler outras fontes (`AE-16`) | 🟡 Caso fechado, classe sem guarda — texto do agente corrigido; nada confere contradição entre itens de um agente | pendência 1 |
| O card do pré-voo prometia ordem de aparição, e o instrumento entrega ordem por categoria (`AE-23`) | 🟢 Fechado — ordem por categoria confirmada como contrato; o teste do card a trava | — |
| Conflito entre o modelo e a entrega da `AF-T7` (`AE-7`) | 🟢 Fechado — versão 2 do modelo aceita pelo dono, hoje versão 3 vigente | — |
| A classe inteira: valor ou contingência publicada no card sem ensaio (`DAF-37`..`DAF-39`, `DAF-41`, `DAF-47`) | 🟡 Caso fechado, classe sem guarda — cada card foi reparado; nada impede o próximo | pendência 1 |

## Pendências abertas ao fim do plano

| # | pendência | por que ficou aberta | o que a fecha | bloqueia algo? |
|---|---|---|---|---|
| 1 | Card publicado com contingência ou valor não ensaiado (classe acima) | a diretiva do dono veda card novo por ajuste | auditoria final | não |
| 2 | Notas sobre a redação de cards já fechados, sem defeito no que está em uso: `AE-8`, `AE-13`, `AE-18` (parte não resolvida), `AE-20`, `AE-21`, `AE-22`, `AE-24` | são registro de como o card foi escrito; a entrega de cada um está conferida | auditoria final, como insumo da pendência 1 | não |
| 3 | Projeção da camada global em `~/.claude`: o `context-scout` instalado na máquina continua no Haiku até que se rode `materializar.py apply` | ato do dono, fora do repositório | o dono roda a projeção | **efeito fora do projeto** |
| 4 | Propagação aos projetos derivados | fora do escopo | plano próprio | **efeito fora do projeto** |
| 5 | A revisão da doutrina de `P-0751` e `P-0752` segue sem rodada registrada | fora das recomendações deste plano | rodada de revisão da doutrina | não |

**Estado honesto:**
- **Entrega:** 21 das 22 tarefas fecharam `done`. A 22ª, `AF-T19`, foi cancelada e substituída pela `AF-T19a`. Todas foram aprovadas: 16 a 100% e 5 com ressalva, entre 91% e 93%.
- **Ressalvas:** as de cinco tarefas (`AF-T8`, `AF-T10`, `AF-T12`, `AF-T17` e `AF-T19a`) foram corrigidas com teste de regressão antes do veredito.
- **O que falta:** cinco pendências. Duas vão à auditoria final e uma à rodada de revisão da doutrina. As outras duas têm efeito fora deste repositório: a projeção em `~/.claude` e a propagação aos derivados. O trabalho da janela foi commitado no Marco 2, com as skills `fatos-frescos` e `mensagem-ao-dono`, que o guia `.claude/README.md` já cita.
