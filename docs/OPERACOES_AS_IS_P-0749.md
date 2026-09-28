# Operações as-is — P-0749, saneamento de artefatos

Documento de validação do plano `docs/plans/P-0749-saneamento-artefatos.md`. Descreve o que o kit
faz hoje, depois das 10 tarefas do plano (`SAN-T1`, `SAN-T2`, `SAN-T2a`, `SAN-T3`, `SAN-T3a`,
`SAN-T4`, `SAN-T5`, `SAN-T6`, `SAN-T6a`, `SAN-T6b`), todas `done`, nenhuma `cancelled`. Saídas
citadas foram rodadas em 2026-09-25, num repositório temporário montado a partir da fixture
`tests/fixtures/backlog/pasta/` ou na própria árvore do hub, como indicado.

## Por que o plano existiu

**O problema.** O planejamento do kit era um amontoado de texto: planos de até 8465 linhas, diário
de 3967, 153 arquivos soltos em `docs/RDO/`. O estado de cada plano e de cada tarefa morava numa
linha `**Status:**` escrita no meio do texto do plano, então saber "em que pé está a tarefa X"
exigia abrir e ler o plano. O número do plano tinha quatro dígitos que pareciam data (`P-0748`), e
toda ferramenta que reconhecia um plano guardava a sua própria cópia dessa forma: oito cópias da
mesma expressão regular espalhadas por cinco ferramentas, todas exigindo exatamente 4 dígitos —
um plano `P-0` era recusado por `backlog.py check`, `rdo.py close` e `review_evidence.py`.

**A solução, em uma frase.** Plano novo ganha uma pasta própria com tudo o que é dele dentro, o
estado sai do texto e vai para uma tabela que se consulta por busca, e o texto que o dono lê passa
a ter uma regra única de tamanho mínimo.

**Vocabulário mínimo.**

| termo | o que é |
|---|---|
| plano legado | plano no formato antigo: um arquivo único `docs/plans/P-NNNN-<slug>.md`. Todo plano existente no hub é legado, este inclusive |
| plano em pasta | plano no formato novo: `docs/plans/P-<n>-<slug>/`, com `plano.md` e os demais arquivos dele dentro |
| `estado.tsv` | tabela de texto separada por TAB, na pasta do plano, com uma linha por plano/tarefa: id, tipo, status, razão, data, nota |
| artefato de máquina / de humano | de máquina é o que uma ferramenta ou agente lê por gramática (TSV, card); de humano é o que o dono lê |
| `backlog.py` | ferramenta de linha de comando do kit que lê o diário e os planos: `check` acusa violações de gramática por código (`C-1`..`C-14`), `status` muda o estado de um item, `next` escolhe a próxima tarefa, `drain` registra plano novo e avança o contador |
| contador | a linha `**Próximo id de plano: P-<n>.**` em `docs/plans/_INBOX.md`, que diz qual número o próximo plano recebe |
| RDO, laudo, evidência | os três registros de uma tarefa: o relato de fechamento (`rdo.py close`), o julgamento do revisor (`rdo.py laudo`) e o dossiê mecânico que o revisor lê (`review_evidence.py`) |

## O arco

| estrato | pergunta que responde | tarefas |
|---|---|---|
| 1. reconhecer | as ferramentas sabem o que é um plano em pasta e um número a partir do zero? | `SAN-T1` |
| 2. guardar o estado | onde mora o estado de um plano em pasta, e quem o escreve? | `SAN-T2`, `SAN-T2a` |
| 3. gravar os registros | onde nascem RDO, laudo e evidência de uma tarefa de plano em pasta? | `SAN-T3`, `SAN-T3a` |
| 4. ensinar | o que a doutrina e a porta de entrada dizem a quem vai escrever o próximo plano? | `SAN-T4`, `SAN-T5`, `SAN-T6`, `SAN-T6a`, `SAN-T6b` |

Cada estrato é inútil sem o anterior: sem o estrato 1 nenhuma ferramenta acha um `plano.md`; sem o
2 o plano em pasta não tem estado; sem o 3 os registros caem na pasta comum; e sem o 4 o
planejador continua escrevendo plano legado. As tarefas com sufixo de letra (`SAN-T2a`,
`SAN-T3a`, `SAN-T6a`, `SAN-T6b`) são corretivos abertos durante a execução, cada um na operação da
tarefa que corrige.

## `SAN-T1` — Uma forma só para o número e o caminho de um plano

**Contexto que a motivou:** oito cópias da regex de id de plano em cinco ferramentas, todas presas
a 4 dígitos; nenhuma reconhecia `docs/plans/P-0-x/plano.md` (o nome do arquivo é `plano`, sem id).

**O que é o artefato:** o módulo novo `.claude/tools/caminhos.py` — as regex de id, contador e
caminho de plano, e as funções `e_layout_pasta`, `arquivos_de_plano`, `id_do_plano`,
`pasta_do_plano`. `backlog.py`, `backlog_hook.py`, `progresso_hook.py`, `rdo.py` e
`review_evidence.py` o carregam por caminho e não guardam mais cópia própria. O módulo tem uma CLI
que lista os planos.

**Como funciona na prática:** o reconhecimento é pela forma do caminho, sem configuração: um
arquivo chamado `plano.md` dentro de pasta `P-<n>-…` é plano em pasta; `P-<n>-<slug>.md` direto em
`docs/plans/` é legado. Sobre a fixture:

```
> python .claude/tools/caminhos.py --root <fixture>
P-0	docs/plans/P-0-gama/plano.md
```

Sobre o hub, a mesma CLI lista 30 planos, de `P-0721 docs/plans/P-0721-governanca-single-source.md`
a `P-0750 docs/plans/P-0750-comunicacao-agente-humano.md`, todos legados.

**Protege contra:** ferramenta que reconhece plano de um jeito e outra de outro; e a recusa de
plano numerado a partir do zero.

## `SAN-T2` — O estado sai do texto e vai para o `estado.tsv`

**Contexto que a motivou:** o estado de plano e de tarefa só existia na linha `**Status:**` do
texto; achar o estado exigia ler o plano.

**O que é o artefato:** em `backlog.py`, a função `_aplicar_estado_tsv` (lê o estado do plano em
pasta a partir de `estado.tsv`), o bloco de escrita em `transacionar_status` (o `backlog.py status`
reescreve a linha da tarefa no `estado.tsv`, e não o `plano.md`), e duas violações novas no
`check`: `C-13` (card sem linha no `estado.tsv`, linha sem card, arquivo ausente ou fora do
esquema) e `C-14` (linha `**Status:**` escrita no `plano.md` de um plano em pasta). Em
`caminhos.py`, `estado_tsv` e `formatar_id` (o contador preserva a largura que já tem: depois de `P-1`
vem `P-2`; depois de `P-0750`, `P-0751`).

**Como funciona na prática:**

1. **O que dispara:** `python .claude/tools/backlog.py status GAM-T1 in-progress`.
2. **A entrada:** a fixture com `plano.md` sem nenhuma linha `**Status:**` e o `estado.tsv` com as tarefas em `ready`.
3. **O processamento:** a ferramenta vê que o plano é de pasta e reescreve só a linha `GAM-T1` do `estado.tsv`.
4. **A saída:**

```
status: GAM-T1 → in-progress. arquivos tocados: docs/DIARIO_DE_OBRAS.md, docs/plans/P-0-gama/estado.tsv
```
```
id <TAB> tipo <TAB> status <TAB> razao <TAB> data <TAB> nota
P-0 <TAB> plano <TAB> ready <TAB> - <TAB> 2026-01-01 <TAB> -
GAM-T1 <TAB> tarefa <TAB> in-progress <TAB> - <TAB> 2026-09-25 <TAB> -
GAM-T2 <TAB> tarefa <TAB> ready <TAB> - <TAB> 2026-01-01 <TAB> -
```

O `plano.md` continua com zero linhas `**Status:**`. Com uma linha `**Status:**` inserida à mão
no `plano.md` e a linha `GAM-T2` apagada do `estado.tsv`, o `check` acusa:

```
C-13 docs/plans/P-0-gama/plano.md:9 — GAM-T2 sem linha em estado.tsv
C-14 docs/plans/P-0-gama/plano.md:3 — P-0: linha **Status:** em plano de pasta
C-2 docs/plans/P-0-gama/plano.md:9 — GAM-T2 sem linha de Status
```

A busca sem abrir arquivo é `rg "^GAM-T1\t" docs/plans/*/estado.tsv`. Sobre o hub, que só tem
plano legado, `check` e `next` saem idênticos aos de antes da tarefa (comparação feita contra a
cópia do código de antes da edição).

**Protege contra:** estado escrito em dois lugares; plano em pasta com estado de volta no texto;
card sem estado ou estado sem card.

## `SAN-T2a` — Projeto novo com contador em `P-0` passa no `check`

**Contexto que a motivou:** o estado que a doutrina passou a ensinar para projeto novo (`SAN-T4`:
`_INBOX.md` só com `**Próximo id de plano: P-0.**` e nenhum plano) fazia o `check` falhar, porque
a regra `C-10` ("o contador aponta para um número já usado") tratava "nenhum plano" como "maior id
= 0".

**O que é o artefato:** a condição do bloco `C-10` em `check` (`backlog.py`): só se aplica quando
existe plano em `docs/plans/`.

**Como funciona na prática:** num repositório vazio de projeto novo, com o `backlog.py` de antes
desta tarefa:

```
C-10 docs/plans/_INBOX.md:1 — contador aponta para P-0, já presente em docs/plans/
1 violação(ões) encontrada(s).
```

Com o `backlog.py` atual, no mesmo repositório: `check: OK — nenhuma violação.`, exit 0. Com plano
presente, a regra e a mensagem não mudaram.

**Protege contra:** o primeiro `check` de todo projeto novo sair vermelho.

## `SAN-T3` — Relato, laudo e evidência nascem na pasta do plano

**Contexto que a motivou:** todo RDO, laudo e evidência ia para `docs/RDO/`, misturado aos de todos
os planos.

**O que é o artefato:** em `caminhos.py`, `pasta_por_id`, `destino_rdo`, `destino_laudo`,
`destino_evidencia`; em `rdo.py`, os subcomandos `close` e `laudo`, e em `review_evidence.py`, o
`main`, passam a escolher o destino pela forma do plano.

**Como funciona na prática:** sem flag de destino, tarefa de plano em pasta grava em
`<pasta-do-plano>/rdo/<tarefa>.md`, `laudos/<tarefa>.md` e `evidencia/<tarefa>.md`, sem `INDEX.md`
(a pasta e o `estado.tsv` já são o índice). Plano legado e tíquete seguem gravando em `docs/RDO/`,
como antes. Os casos estão presos pelos testes `test_tf_san_13_close_grava_rdo_na_pasta_do_plano`,
`test_tf_san_14_laudo_na_pasta_e_no_legado` e `test_tf_san_15_evidencia_na_pasta_do_plano`.

**Protege contra:** registro de plano novo espalhado na pasta comum.

## `SAN-T3a` — A flag explícita vence também no índice

**Contexto que a motivou:** com `--rdo-dir` sobre plano em pasta, o `close` gravava no diretório
da flag mas deixava de regenerar o `INDEX.md` dele; o texto de ajuda da CLI só anunciava o destino
antigo; e o teste novo da `SAN-T3` tinha sido inserido no meio de um teste existente, cortando a
metade que conferia a recusa de `--tarefa TK-62`.

**O que é o artefato:** a condição de regeneração do índice no `close` de `rdo.py`; o texto de
ajuda de `rdo.py` e `review_evidence.py`; e o teste
`test_cli_main_reconhece_tk_subtarefa_de_ticket_e_recusa_id_fora_da_gramatica` restaurado inteiro.

**Como funciona na prática:** o `INDEX.md` é regenerado sempre que o destino não é a pasta do
plano. A ajuda agora diz os dois destinos:

```
  --rdo-dir RDO_DIR     Diretório de saída (default: <pasta-do-plano>/rdo/
                        para plano em pasta, sem INDEX.md; docs/RDO para plano
                        legado ou tíquete).
```

O teste `test_tr_san_19_close_com_rdo_dir_sobre_plano_em_pasta_vence_a_flag` falha no código da
`SAN-T3` e passa no atual.

**Protege contra:** diretório de RDO com índice desatualizado quando alguém passa a flag; e a
perda silenciosa da regressão de gramática de tíquete.

## `SAN-T4` — A doutrina ensina a pasta, o `estado.tsv` e a contagem em zero

**Contexto que a motivou:** `GOVERNANCA.md`, os agentes planejador, revisor e consultor e as skills
`diario-de-obras`, `bootstrap-pantonic`, `scrum-master` e `entrega-de-encerramento` ensinavam só o
plano legado.

**O que é o artefato:** 29 trocas de texto nesses oito arquivos. As centrais: `GOVERNANCA.md` ganha
o bullet *Pasta do plano* e a nomenclatura `P-<n>-<slug>/plano.md` com contador começando em `0` no
projeto novo; a skill `diario-de-obras` ganha a seção *Estado do plano em pasta (`estado.tsv`)* com
o esquema; o planejador passa a gravar `estado.tsv` ao registrar um plano; o `bootstrap-pantonic`
cria `_INBOX.md` com `**Próximo id de plano: P-0.**`.

**Como funciona na prática:** o gatilho é o próximo agente que ler a doutrina — o planejador, ao
registrar o próximo plano, segue essas residências. Nenhuma ferramenta muda com esta tarefa.

**Protege contra:** o kit instalar uma forma nova de plano que o planejador não sabe escrever.

## `SAN-T5` — A regra do artefato de humano mínimo, uma vez só

**Contexto que a motivou:** não existia regra geral de tamanho para o que o dono lê; só dois
limites locais (handover ≤ 8 linhas; célula do índice do diário ≤ 1-2 frases).

**O que é o artefato:** o bullet *Artefato de humano mínimo* em `GOVERNANCA.md` §4.2 (linha 559),
logo depois de *Fechamento enxuto*. Os dois limites locais passam a dizer que são aplicações dele
(`GOVERNANCA.md:556` e `.claude/skills/diario-de-obras/SKILL.md:39`).

**Como funciona na prática:** é regra de conduta, lida por quem escreve texto para o dono: não
repetir dado que mora em tabela de máquina (no máximo o ponteiro), não narrar o que o git, o RDO ou
um TSV já registram, e cortar frase que não serve à decisão do dono. O card de execução fica fora
da regra: nele, ser autossuficiente vence ser curto.

**O procedimento que ela instalou:** **Artefato de humano mínimo** — residência única em
`GOVERNANCA.md` §4.2; o texto da regra aparece uma vez em todo o kit (medido: 1 ocorrência da frase
"não repete dado cuja residência é artefato de máquina").

**Protege contra:** plano, handover e diário crescendo com cópia do que já está registrado em outro
lugar.

## `SAN-T6` — A porta de entrada descreve a pasta, a tabela e o texto mínimo

**Contexto que a motivou:** o `README.md` descrevia plano em arquivo único com `P-NNNN`.

**O que é o artefato:** quatro trocas no `README.md` (`M1`..`M4`): o item *Plano `P-<n>`* do
glossário diz a pasta própria; um bullet novo aponta a regra do artefato de humano mínimo para
`GOVERNANCA.md` §4.2 (sem copiá-la); a nomenclatura sequencial vira `P-<n>-<slug>/plano.md`.

**Como funciona na prática:** a guarda `.claude/checks/check-readme.ps1` segue exit 0 com
`check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s)`.

**Protege contra:** a porta de entrada contradizer a doutrina.

## `SAN-T6a` e `SAN-T6b` — O `README.md` para de chamar o contador de "global"

**Contexto que a motivou:** depois da `SAN-T6`, duas linhas ainda chamavam o contador de "global"
— no glossário (linha 159) e na tabela *Decisões estruturantes* (linha 1045) —, enquanto a regra
nova diz que cada repositório conta a partir do zero.

**O que é o artefato:** duas trocas de uma linha cada no `README.md` (`M5` em `SAN-T6a`, `M6` em
`SAN-T6b`).

**Como funciona na prática:** as duas linhas agora dizem "contador monotônico do repositório" e
"contador sequencial do repositório". Nenhuma ocorrência de "contador global" ou "contador
sequencial global" sobra no `README.md`.

**Protege contra:** a porta de entrada descrever o contador de dois jeitos.

## O que vale além deste plano

| regra | o que resolve | residência |
|---|---|---|
| Pasta do plano | onde mora tudo o que é de um plano novo | `GOVERNANCA.md`, bullet *Pasta do plano*; lista normativa em `P-0749` §3.1 |
| Esquema do `estado.tsv` | estado de plano e tarefa de máquina, achado por busca | skill `diario-de-obras`, seção *Estado do plano em pasta* |
| Contador a partir do zero, na largura que já tem | numeração de projeto novo; o hub segue em `P-0750`… | `GOVERNANCA.md` §7 item 11 (`G-PLANREADY`, condição 1) |
| Artefato de humano mínimo | tamanho do texto que o dono lê | `GOVERNANCA.md` §4.2 |
| Flag explícita vence, índice inclusive | destino de RDO previsível | `P-0749` `DSA-21`; ajuda de `rdo.py close` |

## Os ganhos, medidos

| medida | antes | depois |
|---|---|---|
| cópias da regex de id/caminho de plano | 8, em 5 ferramentas (F-4 do plano) | 1, em `caminhos.py` |
| plano `P-0` em pasta aceito por `backlog.py check` | recusado (F-4) | aceito: `check: OK — nenhuma violação.` |
| `check` de projeto novo recém-criado | exit 1, `C-10` falso | exit 0 |
| saída de `check` + `next` sobre o hub | — | idêntica à de antes (comparação `I-2`, `IGUAL`, em `SAN-T2` e `SAN-T2a`) |
| suíte de testes | 340 passed no despacho da janela (313 em 2026-09-24) | 353 passed; 20 testes do plano (`-k "tf_san or tr_san"`: 20 passed) |
| texto da regra de humano mínimo no kit | 0 ocorrências | 1 (e 3 ponteiros) |

Não medido: tamanho dos artefatos de humano antes × depois. A regra vale para o que se escrever
daqui em diante; nenhum artefato existente foi enxugado (decisão do dono: este plano e o acervo
são legado).

## Defeitos da execução, com estado

| # | defeito | estado | o que fecha |
|---|---|---|---|
| D1 | `caminhos.py`, carregado por caminho, era invisível ao detector de código morto (`AE-1`) | 🟢 fechado com guarda: CLI `main` como entry point; `dead_code.py` exit 0 roda em todo card | — |
| D2 | a comparação "saída antes × depois" usava arquivo gravado, e dava `DIFERE` falso (`AE-1` (b)) | 🟢 fechado com guarda: `DSA-20`, cópia do código de referência em `$env:TEMP` na mesma árvore | — |
| D3 | teste novo inserido no meio de teste existente, cortando a regressão de `TK-62` (`AE-3`) | 🟡 caso fechado (`SAN-T3a`), classe sem guarda: nada barra outra inserção igual | P2 |
| D4 | `--rdo-dir` sobre plano em pasta sem regenerar `INDEX.md` (`AE-3` (a)) | 🟢 fechado com guarda: `test_tr_san_19_…` | — |
| D5 | ajuda da CLI anunciando só o destino antigo (`AE-3` (b)) | 🟡 caso fechado, classe sem guarda: nenhum teste lê o `--help` | — |
| D6 | `C-10` falso no projeto novo (`AE-4`) | 🟢 fechado com guarda: `test_tf_san_20_c10_projeto_novo_sem_plano` | — |
| D7 | "contador global" sobrando no `README.md` em duas linhas (`AE-5` (b), `AE-6`) | 🟡 caso fechado (`SAN-T6a`, `SAN-T6b`), classe sem guarda: `check-readme.ps1` não confere vocabulário | — |
| D8 | cards com número esperado errado ou datado no próprio texto (`AE-2`: 6 em vez de 7 testes; `AE-7`: total da suíte no literal) e trocas de redação sem dizer a quebra de linha (`AE-5` (a), (c)) | 🔴 regra escrita, aplicação pendente: a régua de autoria já existe e não foi aplicada | P1 |

O padrão que a execução revelou: **seis dos sete achados nasceram no texto do card, não na
entrega** (a exceção é o teste cortado de D3) — número esperado copiado sem re-medir, troca literal que não fechou a frase vizinha,
aceite que só conta texto e não exercita o estado que o texto ensina (D6). Nos seis, a entrega foi
fiel ao card, e o revisor pegou o resíduo. Os corretivos (`SAN-T2a`, `SAN-T3a`, `SAN-T6a`,
`SAN-T6b`) fecharam os casos; a classe depende da régua de autoria do planejador.

## Pendências abertas ao fim do plano

| # | pendência | por que ficou aberta | o que a fecha | bloqueia algo? |
|---|---|---|---|---|
| P0 | veredito do dono sobre as seis trocas do `README.md` (`M1`..`M6`) | é aferição manual por desenho (`DSA-23`, `DSA-24`) | o veredito | sim: o aceite do plano |
| P1 | régua de autoria de card: número esperado re-medido e datado fora do literal, veredito do dono fora do *Pronto quando*, quebra de linha declarada | fora do escopo do plano | `TK-72`, Pacotes 11 e 12 (`ready`) | não |
| P2 | evidência do revisor lista arquivos não rastreados anteriores ao despacho como "sem atribuição" | defeito de `review_evidence.py` anterior ao plano, recorrente em todas as revisões desta janela | família `TK-78c` / `TK-55` | não, é ruído |
| P3 | `rdo.py` imprime em cp1252 quando a saída é redirecionada no Windows | anterior ao plano | `TK-82` (`ready`, aberto nesta janela) | não |
| P4 | com a linha de uma tarefa faltando no `estado.tsv`, o `check` acusa também `C-2` "sem linha de Status", mensagem que manda o autor de plano em pasta escrever exatamente o que o `C-14` proíbe | observado ao montar este documento, sem rota ainda | tíquete a abrir, se o dono concordar | não |
| P5 | propagar `caminhos.py`, `estado.tsv` e a doutrina aos kits derivados | `sync-kit.ps1` projeta só skills e agentes (F-8); `.claude/tools/` não chega ao herdeiro | ato de sincronização próprio, fora do plano | não no hub |

**Resumo do estado.** O plano entregou o que prometeu: o kit reconhece, guarda estado, grava
registros e ensina o plano em pasta com contagem a partir do zero, e a regra do artefato de humano
mínimo tem residência única — sem mudar a leitura de nenhum plano existente do hub. Ficaram seis
pendências; só a P0 bloqueia o aceite. A que tem efeito fora do projeto é a P5: nenhum kit derivado
recebe isto até uma sincronização própria.
