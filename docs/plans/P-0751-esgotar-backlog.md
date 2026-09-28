# P-0751 — Esgotar o backlog antes da publicação do kit

**Data:** 2026-09-25 · **Origem:** pedido do dono na sessão de 2026-09-25 (§0) e os 14 cards de tíquete `ready` do diário de obras naquela data · **Status:** `done` · 2026-09-25 · **Prefixo das tarefas no diário:** `EBK-T<n>` · **Prefixo das decisões:** `DEB-<n>` · **Forma:** legado (arquivo único, id de 4 dígitos).
**Ordem de execução:** EBK-T1 → EBK-T2 → EBK-T3 → EBK-T4 → EBK-T5 → EBK-T5a → EBK-T6 → EBK-T7 → EBK-T8 → EBK-T9 → EBK-T10 → EBK-T11 → EBK-T12 → EBK-T13 → EBK-T13a → EBK-T14
**Checagem de versão do kit:** modo hub, congelada em `0.0.0`.

**Pronto quando:** os 14 cards estão `done` e o backlog do plano chegou a zero card pronto, num único loop.

## 0. O problema, verbatim

Pedido (dono, 2026-09-25): *"Crie um plano com esses cards para que sejam fechados em um único loop"*.

Modelo ditado pelo dono (2026-09-25): *"O plano tem um objetivo claro: encerrar esse backlog. O modelo consiste dos múltiplos cards que compõem o backlog. A propriedade de inicio do backlog são X cards, e a propriedade de término é 0. Cada tarefa vai ser uma operação aplicada que modifique a tarefa de ready para done"*.

Sobre o tíquete dos kits derivados (dono, 2026-09-25): *"A publicação do kit ocorrerá depois que o backlog se encerrar."* e, perguntado se ele sai do backlog: *"Não, fica bloqueado"*.

Aceite (dono, 2026-09-25): *"No que depender de aceite, considerar aceito."*

## 1. Modelo conceitual

**Estado do modelo:** versão 1 · 2026-09-25 · autor: planejador · 14 operações · 2 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem | lastro na §0 | tipo |
|---|---|---|---|---|---|---|
| backlog | a fila de cards que este plano esgota, um por vez, no mesmo loop | cards prontos | Quem implementa fecha um card por operação, sem acrescentar card ao plano. | OP-1 | *"A propriedade de inicio do backlog são X cards, e a propriedade de término é 0"* | escopo |
| card | cada um dos 14 cards que compõem o backlog, com o próprio aceite escrito | status | Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz. | externo | *"O modelo consiste dos múltiplos cards que compõem o backlog"* | escopo |

### 1.2 Fluxo de operações

- **OP-1** — O card que faz a conferência do diário acusar tíquete aberto sem card sai de pronto para concluído, e o backlog do plano começa a esvaziar.
  - `precisa de: card` · `altera: card.status, backlog.cards prontos` · `tarefas: EBK-T1` · `lastro: Cada tarefa vai ser uma operação aplicada que modifique a tarefa de ready para done`
- **OP-2** — O card que faz a conferência do diário recusar o card que o fechamento não lê sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - `precisa de: card, backlog` · `altera: card.status, backlog.cards prontos` · `tarefas: EBK-T2` · `lastro: Cada tarefa vai ser uma operação aplicada que modifique a tarefa de ready para done`
- **OP-3** — O card que faz a escolha da próxima tarefa mostrar o cabeçalho inteiro do card sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - `precisa de: card, backlog` · `altera: card.status, backlog.cards prontos` · `tarefas: EBK-T3` · `lastro: Cada tarefa vai ser uma operação aplicada que modifique a tarefa de ready para done`
- **OP-4** — O card que faz o fechamento de tarefa recusar a que não foi concluída sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - `precisa de: card, backlog` · `altera: card.status, backlog.cards prontos` · `tarefas: EBK-T4` · `lastro: Cada tarefa vai ser uma operação aplicada que modifique a tarefa de ready para done`
- **OP-5** — O card que faz a conferência do kit contar um defeito por vez sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - `precisa de: card, backlog` · `altera: card.status, backlog.cards prontos` · `tarefas: EBK-T5, EBK-T5a` · `lastro: Cada tarefa vai ser uma operação aplicada que modifique a tarefa de ready para done`
- **OP-6** — O card que impede fixture de teste com nome que o harness descobre sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - `precisa de: card, backlog` · `altera: card.status, backlog.cards prontos` · `tarefas: EBK-T6` · `lastro: Cada tarefa vai ser uma operação aplicada que modifique a tarefa de ready para done`
- **OP-7** — O card que publica a doutrina do teste que discrimina e da medida publicada sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - `precisa de: card, backlog` · `altera: card.status, backlog.cards prontos` · `tarefas: EBK-T7` · `lastro: Cada tarefa vai ser uma operação aplicada que modifique a tarefa de ready para done`
- **OP-8** — O card que diz quando o modelo passa a valer e o que acontece com a versão recusada sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - `precisa de: card, backlog` · `altera: card.status, backlog.cards prontos` · `tarefas: EBK-T8` · `lastro: Cada tarefa vai ser uma operação aplicada que modifique a tarefa de ready para done`
- **OP-9** — O card que publica a regra de uma operação, uma oração sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - `precisa de: card, backlog` · `altera: card.status, backlog.cards prontos` · `tarefas: EBK-T9` · `lastro: Cada tarefa vai ser uma operação aplicada que modifique a tarefa de ready para done`
- **OP-10** — O card que acrescenta a segunda leva da régua de autoria do card sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - `precisa de: card, backlog` · `altera: card.status, backlog.cards prontos` · `tarefas: EBK-T10` · `lastro: Cada tarefa vai ser uma operação aplicada que modifique a tarefa de ready para done`
- **OP-11** — O card que faz o planejador publicar a busca da superfície e ensaiar os cards sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - `precisa de: card, backlog` · `altera: card.status, backlog.cards prontos` · `tarefas: EBK-T11` · `lastro: Cada tarefa vai ser uma operação aplicada que modifique a tarefa de ready para done`
- **OP-12** — O card dos três ajustes de regra existente sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - `precisa de: card, backlog` · `altera: card.status, backlog.cards prontos` · `tarefas: EBK-T12` · `lastro: Cada tarefa vai ser uma operação aplicada que modifique a tarefa de ready para done`
- **OP-13** — O card que mede quanto custa retomar o planejador por mensagem sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - `precisa de: card, backlog` · `altera: card.status, backlog.cards prontos` · `tarefas: EBK-T13, EBK-T13a` · `lastro: Cada tarefa vai ser uma operação aplicada que modifique a tarefa de ready para done`
- **OP-14** — O card da rodada de revisão das regras de guarda sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - `precisa de: card, backlog` · `altera: card.status, backlog.cards prontos` · `tarefas: EBK-T14` · `lastro: Cada tarefa vai ser uma operação aplicada que modifique a tarefa de ready para done`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final | lastro na §0 |
|---|---|---|---|
| backlog.cards prontos | 14 cards prontos | nenhum card pronto | *"A propriedade de inicio do backlog são X cards, e a propriedade de término é 0"* |
| card.status | pronto | concluído | *"Cada tarefa vai ser uma operação aplicada que modifique a tarefa de ready para done"* |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 1 | 2026-09-25 | vigente | planejador — modelo ditado pelo dono na sessão e transcrito nela, sem o ciclo planejador–modelador, como no `P-0750`; aceito pelo ato *"No que depender de aceite, considerar aceito."* |

## 2. Fatos estabelecidos

- **F-1** Em 2026-09-25, depois da doutrina *Tíquete nasce executável* (`TK-83`), o diário tinha 14 cards de tíquete `ready` e um `blocked` (`TK-81a`); nenhum plano vivo.
- **F-2** Cada card foi escrito e medido na sessão de 2026-09-25: toda âncora de substituição aparece exatamente uma vez no arquivo-alvo, todo valor "antes" publicado bate com a medida, e os 14 são lidos sem erro pelo `rdo.py` (medido na autoria).
- **F-3** Referência de 2026-09-25: `python -m pytest -q` → `360 passed`.
- **F-4** O `TK-81a` (levar o kit atual aos derivados) é a publicação do kit e fica fora deste plano, bloqueado à espera de decisão do dono (§0).

## 3. Decisões

| id | decisão | razão |
|---|---|---|
| DEB-1 | Os 14 cards são transcritos dos tíquetes sem mudança além dos identificadores e dos ponteiros que perderiam o referente fora do diário; cada um traz a linha `Origem` com o card de onde veio | §0; os cards já estavam medidos (F-2) |
| DEB-2 | Os tíquetes `TK-55`, `TK-67`, `TK-70`, `TK-72`, `TK-73` e `TK-83` são absorvidos por este plano: os cards de origem e os tíquetes vão a `cancelled` com a nota `absorvido pelo P-0751`, e as seções deles ficam no diário como registro | forma usada no `P-0750` (`DCH-7`) |
| DEB-3 | Ordem: primeiro os instrumentos do backlog (`EBK-T1`..`EBK-T6`), depois a doutrina (`EBK-T7`..`EBK-T12`), a medida de custo (`EBK-T13`) e, por último, a rodada de revisão das regras de guarda (`EBK-T14`), que julga a doutrina já ajustada | a rodada avalia regra por caso registrado; rodar por último evita revisar o que o plano ainda muda |
| DEB-4 | O modelo tem dois objetos e duas propriedades, como o dono ditou; cada operação leva um card de pronto a concluído e tira um do backlog | §0 |
| DEB-5 | O aceite do plano e de cada marco é o ato do dono de 2026-09-25 | §0 |
| DEB-6 | (consultor, acionamento 1) Na fixture `vermelho`, a subtarefa que cala o `C-15` do `TK-2` nasce `ready`, não com o status do tíquete; a asserção de `test_tf_check_vermelho_dispara_cada_codigo_uma_vez` (C-1..C-9, uma vez cada) fica como está | o `TK-2` carrega `backlog` de propósito para produzir o `C-3`; herdar o status duplicaria o `C-3` (`AE-1`). Descartado pôr `C-15` nos esperados: mudaria o que o teste existente afirma, e o `C-15` já tem par próprio sobre a `verde` |
| DEB-7 | (consultor, acionamento 2) As duas regras novas do `EBK-T2` julgam o corpus deste repositório e entram no `check` por parâmetro desligado por padrão — `piso_c11` (o `C-17` confronta o piso recebido, não a constante) e `dossie` (liga o `C-16`); só o subcomando `check` do `main` passa `_PISO_C11` e `dossie=True` (`EBK-T2`, propriedade 5) | aplicadas a todo `repo`, as duas derrubam as asserções de `check` sobre fixtura: o piso sai inteiro órfão numa fixtura sem citação (`test_tf_san_7_pasta_check_verde`, `test_tf_san_20_c10_projeto_novo_sem_plano`), e a leitura do `rdo.py` recusa todo card vivo de toda fixtura. Medido em cópia com as duas ligadas só no `main`: `362 passed`; a árvore acusa só a órfã `GOVERNANCA.md` §3.2, que a contingência 2 remove, e nenhum `C-16`. Descartado condicionar ao `repo` ser a raiz do kit (regra escondida, e o par em teste não teria como ligá-la) e completar os campos de todas as fixturas (toca fixtura de outros testes para calar regra que não é deles) |
| DEB-8 | (consultor, acionamento 3; linha lançada no acionamento 4, que a achou faltando nesta tabela) `rdo.py close` trata status ausente como não-`done`: recusa, e a mensagem diz `ausente`. Os testes de `close` não tocam `docs/plans/P-0734-execucao-autonoma.md` nem `tests/fixtures/` (montagem no card `EBK-T4`) | em produção o loop roda `backlog.py status <ID> done` antes do `close`, então não há falso positivo. Descartados: tocar o plano real (fora de escopo, histórico) e tolerar status ausente (abre a porta que o card fecha) |
| DEB-9 | (consultor, acionamento 4) Dos quatro achados do laudo da `EBK-T5`, os dois que acusam a própria entrega (`kit_check` conta a linha de sumário do `materializar.py` como problema nos modos `validate` e `check-drift`; linha de detalhe impressa como item) viram um card corretivo só, `EBK-T5a`, da mesma `OP-5`, despachado logo depois da `EBK-T5`. Os dois de instrumento alheio a este plano abrem tíquete no diário, já com card: `TK-84` (`review_evidence.py` com `--desde` lista não rastreado anterior ao despacho) e `TK-85` (`rdo.py laudo` sem campo para o motivo de dimensão, e o alvo `dossiê` recusado) | o objetivo da `EBK-T5` prometeu os dois modos e o card só prescreveu o README; o laudo mandou o primeiro achado para tíquete, mas tíquete fora do plano deixaria a operação que o plano fecha entregue pela metade, e o card corretivo da mesma operação é do consultor. O `I-2` rege tarefa, não a triagem. Os outros dois não pertencem a operação nenhuma deste plano. O `TK-84` supera, com fato novo, o "sem ação" que a rodada de planejamento de 2026-09-25 do `TK-55` (triagem de agente, não decisão do dono) deu ao mesmo defeito, com fato novo: 3 arquivos no `TK-68a`, 19 na `EBK-T5`, e a reconciliação por data de modificação refeita a mão em cada laudo |
| DEB-10 | (consultor, acionamento 5) O `EBK-T12` passa a trazer o bloco 6: em `tests/test_materializar.py`, a asserção `len(...) == 470` do teste de classificação de fase do hook de modelo sai, e entra a asserção de que o `systemMessage` do aviso diz `Fase intelectual`. As edições dos blocos 1-5 que o executor deixou na árvore foram revertidas ao instantâneo do despacho `7ff8f3d`; o redespacho aplica os seis blocos a partir do estado original | o bloco 5 muda o texto do aviso de propósito, e o teste fixava o tamanho do texto, não a fase, que é o que ele nomeia. Medido numa cópia com os seis blocos: suíte `376 passed`, `kit_check` `validate` e `check-drift` exit 0; com o aviso intelectual adulterado, a asserção nova cai (discrimina). Descartados: trocar 470 por 510 (quebra de novo na próxima mudança de texto) e partir das edições na árvore (o laudo mede a entrega a partir do instantâneo do redespacho e não veria os blocos 1-5; a contingência do Texto atual dispararia) |
| DEB-11 | (consultor, acionamento 6) Na `EBK-T13`, segmento se enumera por chave: abre na linha 0 e em toda entrada `type=user` de conteúdo texto com `origin.kind == "coordinator"`; `isMeta=true` sem `origin` fica no segmento em curso. O agregado publica o número de mensagens por segmento, e o Texto novo B perde a causa "o cache do subagente expira entre as rodadas" | nos dois transcripts do corpus, a invocação é a linha 0 (sem `isMeta`), a linha 1 é `isMeta` sem `origin` 12 ms depois, e as seis retomadas também são `isMeta=true`, com `origin.kind == "coordinator"`: contar toda entrada zera a fria, ignorar `isMeta` zera as retomadas, e só a chave `origin` separa os dois casos. O `promptId` não serve (no `agent-a19e...` troca na linha 55, não na retomada da linha 23). Medido só por chaves, contagens e datas: 2 frias, 6 retomadas, fria de custo não nulo; nas retomadas a leitura de cache domina a criação, então a causa que o Texto B afirmava não é o que o corpus mostra. Descartados: `promptId` como fronteira e manter a causa no texto |
| DEB-12 | (consultor, acionamento 7) A regra do `EBK-T13` ("Rodada de replanejamento abre instância fria do planejador") fica no `GOVERNANCA.md`, com a razão trocada: o corretivo `EBK-T13a`, da mesma `OP-13`, publica em `docs/CUSTO_DO_PICKUP.md` a decomposição do custo de partida e reescreve a razão da linha. Descartados: tirar a regra (a decomposição a sustenta) e abrir tíquete para medir de novo (a medida já está feita; o tíquete deixaria a `OP-13` entregue com a razão errada fora do plano) | a média por segmento soma o trabalho da rodada, e a média por mensagem também (inclui os tokens de saída): por mensagem, a fria dá $0,22 e as retomadas de $0,13 a $0,30, e a inversão de 5 em 6 que o laudo aponta confere. O que difere entre as duas opções é a partida — a retomada relê a cada mensagem o contexto carregado, a fria recria a base e redescobre. Medido só por chaves: partida das seis retomadas $6,30 contra fria de $1,16 a $3,80, mesmo com a fria recriando todo o contexto carregado; a retomada vence as duas rodadas curtas (5 e 7 mensagens) e perde as três longas |
| DEB-13 | (consultor, acionamento 8) Os dois achados do fechamento (`AE-6`) vão a tíquete com card, porque o plano não recebe card novo (`I-2`): o piso do `C-11` deixa o código do `backlog.py` e vira dado do repositório, em `docs/PISO_C11.tsv` — arquivo ausente, nenhum piso e nenhum `C-17` (`TK-86`/`TK-86a`); o item do `backlog.py` termina também no primeiro cabeçalho de nível 1 ou 2 fora de cerca de código (`TK-87`/`TK-87a`). Supera, no `DEB-7`, o "só o `main` liga" do piso: o `main` passa o piso lido do `--repo` | o piso é dívida medida num corpus, não regra do instrumento, e o `backlog.py` vai aos derivados com a publicação do kit; protótipo dos dois reparos medido em cópia (suíte `376 passed`, `check` da árvore OK, a cópia da `verde` sem `C-17`, `show EBK-T14` sem a `## 6`) |

## 4. Invariantes de execução

- **I-1** Nenhum executor escreve em `C:\Users\panta\.claude\`. A cópia do hook de modelo no ponto de carga é o **último passo do fechamento do `EBK-T12`**, feito pelo condutor depois do `done`, com o único comando que o dono liberou por regra de permissão em 2026-09-25 (ferramenta Bash, literal): `python .claude/tools/materializar.py apply --alvo usuario --kit-root .claude --home "C:/Users/panta/.claude"`. Antes, o condutor copia para `%TEMP%\claude\ebk-t12-bak\` os destinos que `python .claude/tools/materializar.py drift --alvo usuario` acusar; depois, roda o mesmo `drift` e exige saída sem `FALHOU`. Se falhar, não tenta restaurar: reporta ao dono com o caminho das cópias.
- **I-2** Nenhuma tarefa acrescenta card a este plano; achado com rota de tíquete abre tíquete no diário, já com card.

## 5. Tarefas

### EBK-T1 — O `check` acusa tíquete vivo sem card [Sonnet · esforço medium · classe implementacao]

- **Status:** `done` · 2026-09-25
- **Origem:** card `TK-83a` do diário de obras, seção `## TK-83`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-1`
  - OP-1: O card que faz a conferência do diário acusar tíquete aberto sem card sai de pronto para concluído, e o backlog do plano começa a esvaziar.
  - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.
- **Objetivo:** `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
  tíquete `## TK-<n>` cujo status não é `done`, `cancelled` nem `superseded` e que não tem nenhuma
  subtarefa `### TK-<n><letra>`; a skill `diario-de-obras` nomeia o código.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
  - `.claude/skills/diario-de-obras/SKILL.md`
  - `tests/fixtures/backlog/candidato_a_fechamento/docs/DIARIO_DE_OBRAS.md`,
    `tests/fixtures/backlog/contador_inbox/docs/DIARIO_DE_OBRAS.md`,
    `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md` e
    `tests/fixtures/backlog/vermelho/docs/DIARIO_DE_OBRAS.md` — só pela contingência abaixo
- **Propriedades:**
  1. O `C-15` sai uma vez por tíquete vivo sem subtarefa, nomeando o tíquete.
  2. Tíquete terminal sem subtarefa não é acusado.
  3. As menções `C-1..C-14` do módulo passam a `C-1..C-15`.
- **Texto atual 1** (`.claude/skills/diario-de-obras/SKILL.md`, uma ocorrência):

  ~~~~
  aberto. No loop, achado com rota `tíquete` vai ao consultor, que abre o tíquete já com o card — o
  ~~~~

- **Texto novo 1** (as quebras são as do bloco):

  ~~~~
  aberto — o `backlog.py check` o acusa como `C-15`. No loop, achado com rota `tíquete` vai ao
  consultor, que abre o tíquete já com o card — o
  ~~~~

- **Medido na autoria (2026-09-25):** quatro fixtures têm tíquete vivo sem subtarefa —
  `candidato_a_fechamento` (`TK-4`), `contador_inbox` (`TK-1`), `corpus` (`TK-1`) e `vermelho`
  (`TK-2`); a fixture `verde` tem `TK-1` com `TK-1a`.
- **Testes (novos, em `tests/test_backlog.py`):**
  - TF par sobre cópia da fixture `verde`: como está → nenhum `C-15`; com a subtarefa `TK-1a`
    removida → um `C-15` que nomeia `TK-1`.
  - TF: a mesma cópia sem `TK-1a` e com `TK-1` em `cancelled` (seção e índice) → nenhum `C-15`.
- **Verificação:**
  1. `python -m pytest tests/test_backlog.py -q` → verde, com os testes acima.
  2. `python .claude/tools/backlog.py check` na árvore → `check: OK — nenhuma violação.`
  3. `(Select-String -Path .claude/skills/diario-de-obras/SKILL.md -SimpleMatch 'o acusa como').Count` — antes `0`, depois `1`.
  4. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho mais os testes novos
     (referência medida na autoria: `360 passed`, 2026-09-25).
- **Pronto quando:** o `check` acusa tíquete vivo sem card, com par em teste, e sai `OK` sobre a
  árvore.
- **Não fazer:** não mudar outro código de violação; não tocar `next`.
- **Contingências:**
  - se um teste existente ficar vermelho só por causa do `C-15` numa das quatro fixtures → acrescentar
    ao tíquete acusado dessa fixture uma subtarefa mínima `### TK-<n>a — Card de fixture [Sonnet ·
    classe mecanica]` com o mesmo status do tíquete — **exceto na fixture `vermelho`**, cujo `TK-2`
    tem `backlog` de propósito (é o `C-3` do teste): ali a subtarefa é `### TK-2a — Card de fixture
    [Sonnet · classe mecanica]` com a linha de status na forma das demais da fixture, estado `ready`,
    data `2026-01-01`, apensa ao fim do arquivo
    depois de uma linha em branco, sem linha no índice (DEB-6); se, com isso, outra asserção do
    mesmo teste mudar de resultado → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - **Medido pelo consultor (2026-09-25, acionamento 1, numa cópia da árvore com um `C-15` mínimo
    no `check`):** sem subtarefa, só `test_tf_check_vermelho_dispara_cada_codigo_uma_vez` fica
    vermelho (`1 failed, 359 passed`) — nenhum teste das outras três fixtures cai, e elas não se
    tocam; com o `TK-2a` `ready` acima → `360 passed` e `backlog.py check` na cópia →
    `check: OK — nenhuma violação.`, exit 0.
  - se a Verificação 2 acusar `C-15` na árvore → parar e sinalizar `blocked` razão `premissa`,
    colando as violações.
- **Notas de execução:**
  - 2026-09-25 `ready` — consultor acionamento 1: contingencia reparada (DEB-6, AE-1)

### EBK-T2 — O `check` confronta o card com o `rdo.py` e o piso com o corpus [Sonnet · esforço medium · classe implementacao]

- **Status:** `done` · 2026-09-25
- **Origem:** card `TK-55a` do diário de obras, seção `## TK-55`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-2`
  - OP-2: O card que faz a conferência do diário recusar o card que o fechamento não lê sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Objetivo:** `python .claude/tools/backlog.py check` passa a emitir `C-16` para toda tarefa de
  plano e toda subtarefa de tíquete com status `ready`, `in-progress` ou `review` que a leitura de
  dossiê do `rdo.py` recusa, com a mensagem dessa leitura no texto da violação; e `C-17` para toda
  entrada de `_PISO_C11` que não casa nenhuma ocorrência de citação quebrada no corpus corrente.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
  - `.claude/skills/diario-de-obras/SKILL.md`
- **Propriedades:**
  1. A leitura que decide `C-16` é a mesma que `rdo.py close` usa para o dossiê — um card que o
     `close` recusaria sai acusado, e um que ele aceita não sai. A gramática não é reimplementada
     no `backlog.py`.
  2. Card `done`, `cancelled` ou `blocked` não é lido para `C-16`.
  3. `C-17` nomeia a entrada órfã; entrada órfã no corpus vivo sai de `_PISO_C11` neste card.
  4. As menções do intervalo de códigos no módulo e na skill (`C-1..C-15`, depois do `EBK-T1`) passam
     a `C-1..C-17`.
  5. (DEB-7) `C-16` e `C-17` julgam o corpus deste repositório, não todo `repo` passado a `check`,
     e entram por parâmetro que só o chamador de produção liga. `check` ganha
     `piso_c11: set[tuple[str, str]] | None = None` — ele, não a constante, decide o silêncio do
     `C-11` e o `C-17`; `None` = sem piso (nenhuma citação silenciada, nenhum `C-17`) — e
     `dossie: bool = False` — só com `True` (e `repo` dado) a leitura do `rdo.py` corre e sai
     `C-16`. O único chamador de produção (`main`, subcomando `check`; nenhum outro ponto do kit chama
     `check()`, medido por grep) passa `piso_c11=_PISO_C11, dossie=True`. Os testes que hoje chamam
     `check(...)` ficam intactos: medido (consultor, acionamento 2), a leitura estrita do
     `rdo.py` recusa todo card vivo das fixturas (`verde`, `pasta`, `vermelho`, `corpus`,
     `next_tk90`, …, nenhuma traz `Objetivo`/`Verificação`), e ligada por padrão derrubaria as
     asserções de `check` sobre elas. Leitura estrita = `extrair_dossie(..., esquema_legado=False,
     modelo_legado=None, classe_legado=None)`: card vivo de cabeçalho sem colchete sai `C-16` com a
     mensagem do `rdo.py` (na árvore, medido: 21 cards vivos, nenhum recusado).
- **Texto atual 1** (`.claude/skills/diario-de-obras/SKILL.md`, uma ocorrência):

  ~~~~
  mesmo ato do card corretivo que ele já escreve.
  ~~~~

- **Texto novo 1** (sem quebra nova):

  ~~~~
  mesmo ato do card corretivo que ele já escreve. Card vivo que o `rdo.py` não lê é `C-16` no `backlog.py check`.
  ~~~~

- **Casos medidos que motivaram (2026-09-20 e 2026-09-25):** seis cards de tíquete sem
  `Arquivos-alvo`, `Verificação` e `Pronto quando` passaram no `check` e só falharam no
  `rdo.py close`; o `TK-68a` passou no `check` e o `review_evidence.py` recusou com `campo
  obrigatório ausente em 'TK-68a': 'verificacao'`, porque o literal do card tinha uma linha
  `### Controle 1.1 — …` na coluna 0.
- **Testes (novos, em `tests/test_backlog.py`):**
  - TF par sobre cópia da fixture `verde`: card `ready` íntegro → nenhum `C-16`; o mesmo card sem
    a linha `- **Verificação:**` → um `C-16` com o id; o mesmo card com uma linha `### X` na coluna
    0 antes da `Verificação` → um `C-16` com o id.
  - TF: o mesmo card defeituoso com status `done` → nenhum `C-16`.
  - Montagem medida (consultor, acionamento 2): o card é o `TK-1a` da cópia da `verde`, que nasce
    sem campos; logo abaixo da linha `Status` dele entram `Objetivo`, `Arquivos-alvo` (um item),
    `Verificação` (um item) e `Pronto quando`. Com `check(carregar(repo), repo=repo, dossie=True)`:
    íntegro → `[]`; sem `Verificação` → só `C-16` `campo obrigatório ausente em 'TK-1a':
    'verificacao'`; `### X` antes da `Verificação` → o mesmo `C-16`; sem `Verificação` e status
    `done` → `[]`.
  - TF par para `C-17`: piso com uma entrada que casa ocorrência da fixture → nenhum `C-17`;
    acrescida uma entrada que não casa nada → um `C-17` que a nomeia. Nenhuma fixture traz
    citação de seção; a cópia da `verde` recebe o arquivo
    `.claude/skills/diario-de-obras/SKILL.fixture.md` (`# X`, `## 1. Um`, prosa com `2.5`, sem
    heading `2.5`) e, apensa ao `docs/DIARIO_DE_OBRAS.md`, uma linha `Ver ` + esse caminho entre
    crases + um espaço + o sinal de seção e `2.5.` (a forma que o `C-11` colhe; não se escreve
    literal aqui porque o plano é corpus do `check`) — medido (consultor,
    acionamento 2): `check(carregar(repo), repo=repo)` sobre ela devolve exatamente um `C-11`, e
    nada mais. O piso do par é `{(".claude/skills/diario-de-obras/SKILL.fixture.md", "2.5")}`,
    passado por `piso_c11=` (propriedade 5).
- **Verificação:**
  1. `python -m pytest tests/test_backlog.py -q` → verde, com os testes acima.
  2. `python .claude/tools/backlog.py check` na árvore → `check: OK — nenhuma violação.`
  3. `(Select-String -Path .claude/skills/diario-de-obras/SKILL.md -SimpleMatch 'Card vivo que o').Count` — antes `0`, depois `1`.
  4. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho mais os testes novos
     (referência medida na autoria: `360 passed`, 2026-09-25).
- **Pronto quando:** o `check` acusa card vivo que o `rdo.py` recusa e entrada de piso órfã, cada
  um com par em teste, e sai `OK` sobre a árvore.
- **Não fazer:** não mudar a gramática aceita pelo `rdo.py`; não corrigir card de plano fechado;
  não tocar `rdo.py`.
- **Contingências:**
  - se o Verificação 2 acusar `C-16` em card vivo da árvore → parar e sinalizar `blocked`
    razão `premissa`, colando as violações (o card acusado é defeito de autoria, de outro dono).
  - se `C-17` acusar entrada órfã no corpus vivo → remover a entrada de `_PISO_C11` e seguir
    (propriedade 3). Medido (consultor, acionamento 2, cópia da árvore com a propriedade 5 e
    `C-17` mínimo): a árvore acusa um `C-17`, `('GOVERNANCA.md', '3.2')`; removida a entrada,
    `check: OK — nenhuma violação.` exit 0, e a suíte inteira `362 passed` antes dos testes novos.
- **Notas de execução:**
  - 2026-09-25 `ready` — consultor acionamento 2: onde vale o piso fechado em DEB-7 (propriedade 5), par C-17 medido; defeito do card, nao improcedencia

### EBK-T3 — O `next` projeta o colchete do cabeçalho inteiro [Sonnet · esforço low · classe implementacao]

- **Status:** `done` · 2026-09-25
- **Origem:** card `TK-55c` do diário de obras, seção `## TK-55`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-3`
  - OP-3: O card que faz a escolha da próxima tarefa mostrar o cabeçalho inteiro do card sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Objetivo:** a primeira linha de `backlog.py next` reproduz o colchete do cabeçalho do card como
  ele está no plano — com ` + dono` e ` · esforço <e>` quando o cabeçalho os tem.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
- **Caso medido (2026-09-25):** o card `TK-68a` tinha o cabeçalho `[Sonnet · esforço low · classe
  redacao]` e o `next` imprimiu `[Sonnet · classe redacao]`; em 2026-09-20 o `TK-58a` perdeu o
  ` + dono`, que é a marca de tarefa não delegável. A linha é montada em `backlog.py:1250` como
  `[{item.modelo} · classe {item.classe}]`.
- **Testes:** TF par sobre cópia da fixture `verde` — card `[Sonnet · classe mecanica]` → primeira
  linha termina em `[Sonnet · classe mecanica]`; card `[Opus + dono · esforço high · classe
  investigacao]` → termina em `[Opus + dono · esforço high · classe investigacao]`.
- **Verificação:**
  1. `python -m pytest tests/test_backlog.py -q` → verde, com o par acima.
  2. `python -m pytest tests/test_progresso_hook.py -q` → verde (o gancho do painel lê essa linha).
  3. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho mais os testes novos.
- **Pronto quando:** o colchete do `next` é o do cabeçalho, provado pelo par.
- **Não fazer:** não mudar o formato do resto da saída de `next`; não tocar `progresso_hook.py`.

### EBK-T4 — `rdo.py close` recusa tarefa que não está `done` [Sonnet · esforço medium · classe implementacao]

- **Status:** `done` · 2026-09-25
- **Origem:** card `TK-55b` do diário de obras, seção `## TK-55`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-4`
  - OP-4: O card que faz o fechamento de tarefa recusar a que não foi concluída sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Objetivo:** `rdo.py close` sai com código diferente de `0`, sem escrever arquivo, quando o
  status corrente da tarefa não é `done` — lido na mesma fonte que o `backlog.py status` escreve:
  bullet `- **Status:**` no plano legado e no diário, linha da tarefa em `estado.tsv` no plano em
  pasta. A mensagem nomeia a tarefa, o status encontrado e o exigido. Status ausente (card sem o
  bullet, tarefa sem linha no `estado.tsv`, `estado.tsv` inexistente) não é `done`: recusa, e a
  mensagem diz `ausente` (`DEB-8`).
- **Arquivos-alvo:**
  - `.claude/tools/rdo.py`
  - `tests/test_rdo.py` — e só ele do lado dos testes: nenhum arquivo sob `tests/fixtures/` e
    nenhum plano sob `docs/plans/` muda (`DEB-8`)
- **Montagem dos testes existentes:** `DEB-8`, medida pelo consultor numa cópia da árvore com a
  regra mínima no `close` — sem a montagem, 17 dos 57 testes do `test_rdo.py` caem; com ela,
  `57 passed` e suíte `367 passed`.
  - `_argv_close` deixa de apontar `--plano` para `_PLANO_REAL`: aponta uma cópia dele em
    `tmp_path / "plano-real" / _PLANO_REAL.name` (subpasta, porque vários testes contam os `.md`
    de `tmp_path` como RDO), com a linha `` - **Status:** `done` · 2026-09-25 `` inserida logo
    abaixo de cada linha que começa por `### T7 — ` e por `### T8a — `; o plano real não é tocado.
  - `_escrever_plano_sintetico` ganha parâmetro opcional `status` (padrão sem linha de status, e
    os testes de `extrair_dossie` seguem como estão); o teste do cabeçalho histórico com teto que
    chama `close` passa `status="done"`.
  - Os dois testes de `close` sobre plano em pasta (`test_tf_san_13_…` e `test_tr_san_19_…`)
    gravam `plano.parent / "estado.tsv"` com o cabeçalho de `caminhos.CABECALHO_ESTADO` e a linha
    `T1`, `tarefa`, `done`, `-`, `2026-09-25`, `-`, separada por tabulação.
  - Em `test_tf_close_gera_rdo_completo_a_partir_do_plano_pacote_e_consumo`, a asserção de que a
    palavra `status` não aparece no RDO passa a excluir a linha transcrita do plano:
    `assert "status" not in conteudo.replace("- **Status:** `done` · 2026-09-25", "").lower()`.
    O RDO transcreve o bullet de status do card como campo extra, e isso já acontece em
    produção: o RDO do `EBK-T3` em `docs/RDO/` traz a linha. A intenção da asserção fica de pé:
    o `close` não produz status por conta própria.
- **Caso medido que motivou (2026-09-20):** o `close` escreveu RDO para uma tarefa `in-progress`
  um comando depois de o `backlog.py status` ter recusado `in-progress → done`. Hoje `rdo.py:14`
  declara: *"`close` não tem `--status` e não lê `status` de lugar nenhum"*.
- **Testes:** TF par — tarefa `in-progress` → exit diferente de `0` e nenhum RDO no destino; a
  mesma tarefa `done` → exit `0` e o RDO escrito. Um par no plano legado e um no plano em pasta.
- **Verificação:**
  1. `python -m pytest tests/test_rdo.py -q` → verde, com os pares acima.
  2. `(Select-String -Path .claude/tools/rdo.py -SimpleMatch 'de lugar nenhum').Count` — antes `1`, depois `0`.
  3. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho mais os testes novos.
- **Pronto quando:** o `close` só escreve RDO de tarefa `done`, provado pelos dois pares, e a
  docstring do módulo diz que ele lê o status.
- **Não fazer:** não acrescentar flag `--status`; não mudar o pacote de campos do `close`; não
  tocar `backlog.py`.
- **Contingências:**
  - se, com a montagem acima, outro teste existente de `close` além dos 17 medidos cair, ou outra
    asserção deles além da da palavra `status` mudar de resultado → parar e sinalizar `blocked`
    razão `premissa`, nomeando o teste.
- **Notas de execução:**
  - 2026-09-25 `ready` — DEB-8: status ausente recusa; testes de close sobre copia do plano real em tmp_path; montagem medida (367 passed)

### EBK-T5 — O `kit_check` conta defeito, não linha [Sonnet · esforço low · classe implementacao]

- **Status:** `done` · 2026-09-25
- **Origem:** card `TK-55d` do diário de obras, seção `## TK-55`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-5`
  - OP-5: O card que faz a conferência do kit contar um defeito por vez sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Objetivo:** o número em `kit_check: check-drift FALHOU (<n> problema(s))` e em
  `kit_check: FALHOU (<n> problema(s))` passa a ser o número de defeitos: uma divergência de
  README conta `1`, e as linhas `[regenerado]`/`[versionado]` que a detalham continuam impressas
  sem entrar na contagem.
- **Arquivos-alvo:**
  - `.claude/checks/kit_check.ps1`
  - `tests/test_kit_check.py` (novo, ou o arquivo de teste do `kit_check` que já existir)
- **Caso medido (2026-09-25):** cópia de `.claude/` em diretório temporário, com uma frase
  acrescentada a uma linha da região gerada de `.claude/README.md` → a saída listou
  `README.md diverge do regenerado (2 linha(s) diferente(s)):` mais as duas linhas de detalhe
  como três itens `- ` da mesma lista, todos contados.
- **Testes:** TF sobre cópia do kit sob `tmp_path` (pular se `pwsh` não estiver no `PATH`): uma
  divergência de README com duas linhas diferentes → a contagem de problemas atribuída ao README
  é `1` e as duas linhas de detalhe aparecem na saída.
- **Verificação:**
  1. `python -m pytest <arquivo de teste do kit_check> -q` → verde, com o teste acima.
  2. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` na árvore → exit `0`.
  3. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho mais os testes novos.
- **Pronto quando:** uma divergência conta um problema, provado pelo teste, e o check segue verde
  na árvore.
- **Não fazer:** não mudar o que o `kit_check` considera divergência; não mexer na codificação do
  console (já correta).

### EBK-T5a — O `kit_check` não conta o sumário do `materializar` e detalha sob o problema [Sonnet · esforço low · classe implementacao]

- **Status:** `done` · 2026-09-26
- **Origem:** corretivo da `EBK-T5`, achados (1) e (2) do laudo dela (`AE-2`, `DEB-9`), escrito pelo consultor no acionamento 4.
- **Operação do modelo:** `OP-5`
  - OP-5: O card que faz a conferência do kit contar um defeito por vez sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Objetivo:** fechar o que o objetivo da `EBK-T5` prometeu e o card dela não prescreveu, em
  `.claude/checks/kit_check.ps1`:
  1. nos dois ramos que chamam o `materializar.py` — `materializar check` no modo `validate` e
     `materializar drift` no modo `check-drift` —, a linha de sumário que o `materializar.py`
     imprime por último quando falha (começa por `materializar: FALHOU - `) não entra na lista de
     problemas e não é impressa; o número do cabeçalho passa a ser o número de defeitos;
  2. no modo `check-drift`, as linhas de detalhe da divergência de README saem logo abaixo do item
     do README, indentadas com quatro espaços e sem o marcador `- `
     (`    [versionado] <linha>` e `    [regenerado] <linha>`); o número de linhas de item
     (`  - `) da saída é igual ao número do cabeçalho.
- **Arquivos-alvo:**
  - `.claude/checks/kit_check.ps1`
  - `tests/test_kit_check.py`
- **Caso medido (2026-09-26, consultor, cópia de `.claude/` e `VERSION` em diretório temporário):**
  `-Mode check-drift` → `check-drift FALHOU (13 problema(s))` para 12 defeitos, e o 13º item é
  `materializar drift: materializar: FALHOU - 12 problema(s) de drift.`; com a frase extra no
  README do teste existente, 14 no cabeçalho e 16 itens. `-Mode validate` com uma entrada a mais em
  `arquivos` de um alvo de `projecoes.json`, `de` apontando `nao/existe.md` →
  `kit_check: FALHOU (2 problema(s))` para 1 defeito.
- **Fatos para a execução (medidos):** o `materializar.py` imprime cada problema antes do sumário e
  só imprime o sumário quando há ao menos um problema, então descartar a linha de sumário nunca
  esvazia a lista de um ramo que saiu `1`. No `check-drift`, o item do README é sempre o primeiro da
  lista quando há divergência (entra antes do ramo do `materializar.py`). O protótipo do consultor
  (descartar a linha que casa `^materializar: FALHOU - ` no laço de cada ramo; guardar o detalhe
  sem prefixo e imprimi-lo com quatro espaços depois do primeiro item quando há divergência) deu,
  na mesma cópia: `validate` → `kit_check: FALHOU (1 problema(s))` com um item; `check-drift` com
  README divergente → `(13 problema(s))`, 13 itens e as duas linhas de detalhe logo abaixo do item
  do README; e, rodado com `-KitRoot .claude` sobre a árvore, os dois modos exit `0`.
- **Testes (novos, em `tests/test_kit_check.py`, reusando `_copiar_kit`; pular se `pwsh` não
  estiver no `PATH`):**
  1. `check-drift` sobre a cópia intacta: sai diferente de `0` e a saída contém `materializar drift:`
     (pré-condição: a cópia tem drift de materialização, porque o `settings.json` copiado aponta o
     repositório de origem); a saída não contém `materializar: FALHOU`; o número do cabeçalho é
     igual ao número de linhas que começam por `  - `.
  2. `validate` sobre a cópia com a entrada a mais em `projecoes.json` descrita no caso medido:
     sai diferente de `0`, a saída contém `kit_check: FALHOU (1 problema(s))` e não contém
     `materializar: FALHOU`.
  3. `check-drift` com a mesma divergência de README do teste existente: as duas linhas logo abaixo
     do item que começa por `  - README.md diverge do regenerado` casam
     `^    \[(versionado|regenerado)\] `; nenhuma linha que começa por `  - ` contém `[versionado]`
     ou `[regenerado]`; o número do cabeçalho é igual ao número de linhas que começam por `  - `.
  Medido no protótipo: os três falham sobre o `kit_check.ps1` de hoje e passam com o reparo; o
  teste existente segue verde nos dois.
- **Verificação:**
  1. `python -m pytest tests/test_kit_check.py -q` → `4 passed`.
  2. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → exit `0`.
  3. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` → exit `0`.
  4. `python -m pytest -q` → nenhuma falha; `passed` = o do despacho mais 3.
- **Pronto quando:** nos dois modos, o número do cabeçalho conta defeito e é igual ao número de
  itens da lista, provado pelos três testes, e os dois modos seguem exit `0` na árvore.
- **Não fazer:** não mudar o `materializar.py`; não mudar o que o `kit_check` considera divergência;
  não tocar os modos `generate` e `consumers`; não mexer na codificação do console.
- **Contingências:**
  - se o teste existente `test_divergencia_de_readme_conta_um_problema_e_detalha_as_duas_linhas`
    cair com o reparo → parar e sinalizar `blocked` razão `premissa`, colando a saída do teste.

### EBK-T6 — Nenhuma fixture carrega nome que o harness descobre [Sonnet · esforço low · classe mecanica]

- **Status:** `done` · 2026-09-26
- **Origem:** card `TK-55f` do diário de obras, seção `## TK-55`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-6`
  - OP-6: O card que impede fixture de teste com nome que o harness descobre sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Objetivo:** um teste falha, nomeando o arquivo, quando existe sob `tests/fixtures/` um arquivo
  chamado `SKILL.md`, `CLAUDE.md`, `AGENTS.md`, `settings.json` ou `settings.local.json`.
- **Arquivos-alvo:**
  - `tests/test_fixtures_higiene.py` (novo)
- **Caso medido (2026-09-20):** uma fixture do `TK-60a` continha `SKILL.md`, e o harness passou a
  listá-la como skill invocável real. Hoje há `0` arquivos com esses nomes sob `tests/fixtures/`
  (medido em 2026-09-25).
- **Testes:** função pura `nomes_de_descoberta(raiz: Path) -> list[Path]`; TF par — diretório sob
  `tmp_path` com `a/SKILL.md` → 1 caminho; sem ele → 0; TR — `tests/fixtures/` real → 0.
- **Verificação:**
  1. `python -m pytest tests/test_fixtures_higiene.py -q` → verde.
  2. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho mais os testes novos.
- **Pronto quando:** o TR acusa fixture com nome de descoberta, provado pelo par.

### EBK-T7 — A doutrina do teste que discrimina e da medida publicada [Sonnet · esforço low · classe redacao]

- **Status:** `done` · 2026-09-26
- **Origem:** card `TK-55g` do diário de obras, seção `## TK-55`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-7`
  - OP-7: O card que publica a doutrina do teste que discrimina e da medida publicada sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Objetivo:** `GOVERNANCA.md` §4.4 passa a carregar as quatro regras do teste que discrimina, e a
  *Disciplina de instrumento* de §3 passa de cinco para oito regras, com as três da medida
  publicada. A regra corrigida da `DB-53` do `P-0739` ganha residência aqui, e o plano fechado não
  é editado.
- **Arquivos-alvo:**
  - `GOVERNANCA.md`
- **Passos:** substituir cada **Texto atual** pelo **Texto novo** de mesmo número; rodar as
  Verificações.
- **Texto atual 1** (§4.4, uma ocorrência):

  ~~~~
  nunca a cada micro-edição; tier superior só no fechamento (`.claude/global/CLAUDE.md` Regra 7;
  skill `test-tiers`).
  ~~~~

- **Texto novo 1** (as quebras são as do bloco):

  ~~~~
  nunca a cada micro-edição; tier superior só no fechamento (`.claude/global/CLAUDE.md` Regra 7;
  skill `test-tiers`).

  **Teste que discrimina.** Teste verde só prova algo se ficaria vermelho sem o que ele protege.
  Quatro regras, cada uma com caso medido de teste que passou pelo motivo errado:

  1. **Asserção afirma relação, nunca magnitude.** O teste compara mundos: o produto certo dá a
     mesma saída nos dois, o produto revertido dá saídas diferentes, e a saída do mundo hostil não
     é vazia. A magnitude medida vai para o docstring, com a data e o mundo da medida.
  2. **Executável que lê `stdin` se testa em mundo hostil construído, não herdado.** Os mundos são
     ambiente mínimo com `PYTHONIOENCODING` de byte único e ambiente mínimo com `PYTHONUTF8=1`. O
     payload acentuado tem de chegar a um canal observável — a saída, ou o efeito colateral do
     executável silencioso —; sem canal que o carregue, o fato se declara e o teste não se escreve.
     O par negativo é o próprio produto revertido por substituição textual da fonte, nunca um stub.
  3. **Teste de instrumento roda sobre fixture copiada, nunca sobre o diário ou os planos vivos** —
     o estado vivo torna o teste instável e leva conteúdo alheio ao contexto de quem roda a suíte.
  4. **Fixture não carrega nome que o harness descobre** — `SKILL.md`, `CLAUDE.md`, `AGENTS.md`,
     `settings.json`, `settings.local.json` —, porque o harness passa a tratá-la como artefato real.
  ~~~~

- **Texto atual 2** (§3, uma ocorrência):

  ~~~~
  - **Disciplina de instrumento** — cinco regras de método, medidas na janela de 2026-09-16
  ~~~~

- **Texto novo 2** (sem quebra nova):

  ~~~~
  - **Disciplina de instrumento** — oito regras de método, as cinco primeiras medidas na janela de 2026-09-16
  ~~~~

- **Texto atual 3** (§3, uma ocorrência):

  ~~~~
    só se ele produzir; protocolo lido antes de evidência que não veio é leitura paga sem uso.
  ~~~~

- **Texto novo 3** (as quebras são as do bloco):

  ~~~~
    só se ele produzir; protocolo lido antes de evidência que não veio é leitura paga sem uso.
    **(f)** Medida publicada nomeia o objeto medido — registro, texto renderizado e texto-fonte do
    mesmo artefato têm comprimentos diferentes, e o rótulo errado sobrevive à recontagem. **(g)**
    Contagem publicada traz a regra de enumeração do corpus — o que conta e o que se descarta —,
    sem a qual o `n` não se reconcilia por quem refaz a medida. **(h)** Efeito publicado vem com a
    dispersão do controle pareado — sessão gêmea, mesmo dia, mesma árvore —, e efeito dentro da
    faixa do controle não é efeito.
  ~~~~

- **Verificação:** no PowerShell, na raiz; **antes** medido em 2026-09-25.
  1. `(Select-String -Path GOVERNANCA.md -SimpleMatch '**Teste que discrimina.**').Count` — antes `0`, depois `1`
  2. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'cinco regras de método').Count` — antes `1`, depois `0`
  3. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'efeito dentro da').Count` — antes `0`, depois `1`
  4. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.
- **Pronto quando:** as três contagens saem nos valores de depois.
- **Não fazer:** não editar `docs/plans/P-0739-backlog-instrumento.md`; não tocar outro parágrafo de §4.4.
- **Contingências:**
  - se um **Texto atual** não for encontrado exatamente uma vez → parar e sinalizar `blocked`
    razão `premissa`, citando o número do bloco.

### EBK-T8 — A vigência do modelo, o desfecho do drift recusado e o lastro na descrição pública [Sonnet · esforço low · classe redacao]

- **Status:** `done` · 2026-09-26
- **Origem:** card `TK-70a` do diário de obras, seção `## TK-70`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-8`
  - OP-8: O card que diz quando o modelo passa a valer e o que acontece com a versão recusada sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Objetivo:** `GOVERNANCA.md` §3.2 passa a dizer que o modelo só vigora depois de validado pelo
  dono — o rascunho carrega `situação: vigente` por forma, não por vigência — e o que acontece com o
  que foi entregue sob uma versão pendente recusada; `README.md` §8.1 passa a dizer ao leitor que
  todo elemento do modelo tem lastro no pedido.
- **Fundamento:** `DLS-3` e `DLS-4` do `P-0746`; `AE-21` daquele plano; confirmação medida em 2026-09-25, na seção `## TK-70` do diário de obras.
- **Arquivos-alvo:**
  - `GOVERNANCA.md`
  - `README.md`
- **Passos:** substituir cada **Texto atual** pelo **Texto novo** de mesmo número; rodar as
  Verificações.
- **Texto atual 1** (`GOVERNANCA.md` §3.2, *Rascunho antes do Marco 1*, uma ocorrência):

  ~~~~
  a versão 1 **no lugar**, sem bloco irmão e sem linha nova no registro. Versionar só começa no
  Marco 1.
  ~~~~

- **Texto novo 1** (as quebras são as do bloco):

  ~~~~
  a versão 1 **no lugar**, sem bloco irmão e sem linha nova no registro. Versionar só começa no
  Marco 1. O rascunho carrega `situação: vigente` porque essa é a forma da `## 1`, não porque
  vigore: **o modelo só vigora depois de validado pelo dono**, e antes disso não obriga nenhuma das
  partes. Rascunho recusado e reescrito continua rascunho — substitui-se no lugar —, e
  `situação: pendente` só existe na `## 1A`, depois do Marco 1.
  ~~~~

- **Texto atual 2** (`GOVERNANCA.md` §3.2, *Versão vigente, pendente e obsoleta*, uma ocorrência):

  ~~~~
  registra qual versão ficou obsoleta, quando e por aceite de qual versão. Recusada, a pendente é
  **eliminada** e a vigente permanece, sem marca.
  ~~~~

- **Texto novo 2** (as quebras são as do bloco):

  ~~~~
  registra qual versão ficou obsoleta, quando e por aceite de qual versão. Recusada, a pendente é
  **eliminada** e a vigente permanece, sem marca — e o plano **retroage ao ponto do drift**: o que
  foi entregue sob a versão recusada é refeito, sob a vigente, por card corretivo da operação
  afetada, porque `done` é terminal e não se reabre. O plano não é cancelado.
  ~~~~

- **Texto atual 3** (`README.md` §8.1, uma ocorrência):

  ~~~~
  O modelo **versiona, não se reescreve**: quando uma decisão muda o que o plano entrega, a versão
  ~~~~

- **Texto novo 3** (as quebras são as do bloco; a linha em branco separa parágrafos):

  ~~~~
  Todo elemento do modelo tem **lastro** no pedido: um trecho do enunciado que o justifica. O que o
  pedido não traz não entra no modelo — se o agente o julga necessário, entrega-o como requisito
  secundário, declarado numa seção à parte e sob a responsabilidade inteira dele.

  O modelo **versiona, não se reescreve**: quando uma decisão muda o que o plano entrega, a versão
  ~~~~

- **Verificação:** no PowerShell, na raiz; **antes** medido em 2026-09-25.
  1. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'o modelo só vigora depois de validado pelo dono').Count` — antes `0`, depois `1`
  2. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'retroage ao ponto do drift').Count` — antes `0`, depois `1`
  3. `(Select-String -Path README.md -SimpleMatch 'Todo elemento do modelo tem **lastro** no pedido').Count` — antes `0`, depois `1`
  4. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.
- **Pronto quando:** as três contagens saem nos valores de depois e a suíte segue verde.
- **Não fazer:** não tocar `.claude/skills/scrum-master/SKILL.md` (o Pacote B já está lá); não
  editar modelo de plano nenhum; não editar a seção do `TK-69`.
- **Contingências:**
  - se um **Texto atual** não for encontrado exatamente uma vez → parar e sinalizar `blocked`
    razão `premissa`, citando o número do bloco.

### EBK-T9 — Uma operação, uma oração [Sonnet · esforço low · classe redacao]

- **Status:** `done` · 2026-09-26
- **Origem:** card `TK-73a` do diário de obras, seção `## TK-73`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-9`
  - OP-9: O card que publica a regra de uma operação, uma oração sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Objetivo:** `GOVERNANCA.md` §3.2 e a skill `diario-de-obras` passam a dizer que operação escrita
  com mais de uma oração é operação mal recortada, que cada oração vira operação própria, e que a
  guarda é o marco.
- **Fundamento:** Pacote 1 do `TK-73`; medição da §5 da seção `## TK-73` do diário de obras.
- **Arquivos-alvo:**
  - `GOVERNANCA.md`
  - `.claude/skills/diario-de-obras/SKILL.md`
- **Passos:** substituir cada **Texto atual** pelo **Texto novo** de mesmo número; rodar as
  Verificações.
- **Texto atual 1** (`GOVERNANCA.md` §3.2, *Objeto, operação e propriedade*, uma ocorrência):

  ~~~~
  identificam-se as propriedades, e deles caem por decomposição — não por intuição.
  ~~~~

- **Texto novo 1** (as quebras são as do bloco):

  ~~~~
  identificam-se as propriedades, e deles caem por decomposição — não por intuição.
  **Uma operação, uma oração.** Operação escrita com mais de uma oração — cada uma com o seu verbo
  e o seu lastro — é operação mal recortada: cada oração vira operação própria, com a sua
  propriedade e o seu card. A guarda é o Marco 1, que lê operação a operação contra a `## 0`;
  nenhuma validação a apanha, porque a conjunção também aparece dentro de uma oração só.
  ~~~~

- **Texto atual 2** (`.claude/skills/diario-de-obras/SKILL.md`, *Objeto e propriedade, na
  decomposição*, uma ocorrência; sem quebra nova):

  ~~~~
  marco.
  ~~~~

- **Texto novo 2:**

  ~~~~
  marco. Operação escrita com mais de uma oração é operação mal recortada: cada oração vira operação própria, e a guarda também é o marco.
  ~~~~

- **Verificação:** no PowerShell, na raiz; **antes** medido em 2026-09-25.
  1. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'Uma operação, uma oração.').Count` — antes `0`, depois `1`
  2. `(Select-String -Path .claude/skills/diario-de-obras/SKILL.md -SimpleMatch 'Operação escrita com mais de uma oração').Count` — antes `0`, depois `1`
  3. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` → exit `0`
  4. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.
- **Pronto quando:** as duas contagens saem nos valores de depois.
- **Não fazer:** não mudar `modelo.py` nem o `check`; não editar modelo de plano nenhum.
- **Contingências:**
  - se um **Texto atual** não for encontrado exatamente uma vez → parar e sinalizar `blocked`
    razão `premissa`, citando o número do bloco (o **Texto atual 2** é a linha que termina o
    parágrafo *Objeto e propriedade, na decomposição*, que hoje é exatamente `marco.`).

### EBK-T10 — A régua de autoria do card, segunda leva [Sonnet · esforço medium · classe redacao]

- **Status:** `done` · 2026-09-26
- **Origem:** card `TK-72a` do diário de obras, seção `## TK-72`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-10`
  - OP-10: O card que acrescenta a segunda leva da régua de autoria do card sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Objetivo:** a Fase 4 do `pantonic-planner` ganha o item 13 com os dez critérios de autoria que
  faltam; o `pantonic-consultant` passa a aplicar os itens 11 a 13 a todo card que escreve; e
  `GOVERNANCA.md` §3.2 limita o contrato copiado no card ao que a operação dele usa.
- **Fundamento:** pacotes 1, 2, 3, 5, 9, 11 e 12 do `TK-72`; itens nomeados do `TK-55`
  (escalonamentos 3 a 6 de 2026-09-20); caso do `TK-68a` (2026-09-25).
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md`
  - `.claude/agents/pantonic-consultant.md`
  - `GOVERNANCA.md`
- **Passos:** substituir cada **Texto atual** pelo **Texto novo** de mesmo número, no arquivo
  indicado; rodar as Verificações.
- **Texto atual 1** (`.claude/agents/pantonic-planner.md`, fim do item 12 da Fase 4, uma ocorrência):

  ~~~~
     construção (2026-09-19, `AE-19`).
  ~~~~

- **Texto novo 1** (as quebras são as do bloco; a linha em branco separa os itens):

  ~~~~
     construção (2026-09-19, `AE-19`).

  13. **Régua de autoria, segunda leva** — dez critérios medidos em janelas de execução de
     2026-09-20 a 2026-09-25; valem para todo card, de plano ou de tíquete, e para o
     `pantonic-consultant` quando ele escreve card:
     (i) **O card fixa a propriedade e a medida; a técnica é do executor** — o card diz o que tem de
     ser verdade ao final e o comando que o prova, e só prescreve o *como* quando o como é a própria
     propriedade.
     (ii) **Premissa citada se mede, e pelo instrumento quando ele sabe medir** — gramática,
     domínio, população e contagem citados no card se medem antes de publicar; número que um
     instrumento do kit calcula vem do instrumento, nunca de varredura que conte outra coisa
     (`grep -c` conta linha, não ocorrência).
     (iii) **Aceite de redação é recorte de literal** — o card fixa o texto verbatim e a verificação
     conta o literal (`Select-String -SimpleMatch`); onde há texto a substituir, conta também o
     literal antigo sumir. Contar palavra solta aprova menção decorativa.
     (iv) **O literal declara a quebra de linha** — cada bloco diz "as quebras são as do bloco" ou
     "sem quebra nova e sem refluxo".
     (v) **Literal com cabeçalho markdown entra recuado** — linha que começa com `## ` ou `### ` na
     coluna 0 encerra o card para o `rdo.py` e o `review_evidence.py`; todo bloco literal do card
     vai recuado dois espaços.
     (vi) **`Arquivos-alvo` fecha o efeito colateral mecânico** — entrega cujo efeito em outro
     arquivo é obrigatório e previsível lista esse arquivo; o executor não decide absorvê-lo.
     (vii) **Rota de achado só vai para card que a aceita** — o achado roteado a um card está no
     dossiê dele; rota que sai do plano abre tíquete no mesmo ato, já com o card (skill
     `diario-de-obras`, "Tíquete nasce executável").
     (viii) **Valor medido de aceite nunca viaja na linha de retorno** — `pendencia=` é só para
     pendência; a medida vai para a evidência que o revisor gera.
     (ix) **O veredito do dono é gate do marco, não critério de pronto** — `Pronto quando` só cita
     verificação que o revisor roda; card que precisa do veredito do dono o leva ao relatório de
     encerramento.
     (x) **Menção de referência quebrada vai em forma que o lint não colhe** — reproduzir a citação
     quebrada na forma colhível, para falar dela, cria mais uma ocorrência.
  ~~~~

- **Texto atual 2** (`.claude/agents/pantonic-consultant.md`, uma ocorrência; sem quebra nova):

  ~~~~
  no caso que a skill `diario-de-obras` determina em "Tíquete nasce executável".
  ~~~~

- **Texto novo 2:**

  ~~~~
  no caso que a skill `diario-de-obras` determina em "Tíquete nasce executável". Todo card que você escreve passa pelos itens 11 a 13 da Fase 4 do `pantonic-planner` (`.claude/agents/pantonic-planner.md`).
  ~~~~

- **Texto atual 3** (`GOVERNANCA.md` §3.2, *O contrato chega ao card*, uma ocorrência):

  ~~~~
  estágio está e do que precisa.
  ~~~~

- **Texto novo 3** (as quebras são as do bloco):

  ~~~~
  estágio está e do que precisa. O contrato copiado se limita ao que **esta** operação usa: a
  partição que é de outra operação fica fora, e lista de residências entra por ponteiro ao fato da
  `## 2` que é a residência única dela, nunca copiada card a card.
  ~~~~

- **Verificação:** no PowerShell, na raiz; **antes** medido em 2026-09-25.
  1. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'Régua de autoria, segunda leva').Count` — antes `0`, depois `1`
  2. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'Literal com cabeçalho markdown entra recuado').Count` — antes `0`, depois `1`
  3. `(Select-String -Path .claude/agents/pantonic-consultant.md -SimpleMatch 'itens 11 a 13 da Fase 4').Count` — antes `0`, depois `1`
  4. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'O contrato copiado se limita ao que').Count` — antes `0`, depois `1`
  5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` e `-Mode check-drift` → exit `0`
  6. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.
- **Pronto quando:** as quatro contagens saem nos valores de depois e o kit segue válido e sem drift.
- **Não fazer:** não renumerar nem reescrever os itens 1 a 12 da Fase 4; não tocar
  `docs/RUBRICA_DE_REVISAO.md`.
- **Contingências:**
  - se um **Texto atual** não for encontrado exatamente uma vez → parar e sinalizar `blocked`
    razão `premissa`, citando o número do bloco.

### EBK-T11 — O planejador publica o grep da superfície e ensaia os cards antes de gravar [Sonnet · esforço low · classe redacao]

- **Status:** `done` · 2026-09-26
- **Origem:** card `TK-72b` do diário de obras, seção `## TK-72`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-11`
  - OP-11: O card que faz o planejador publicar a busca da superfície e ensaiar os cards sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Depende de:** `EBK-T10`
- **Objetivo:** o `pantonic-planner` passa a ter dois usos para o `Bash` — o comando de aceite e o
  grep de verificação de superfície, publicado com padrão e contagem —, e a Fase 4 ganha o item 14,
  o ensaio dos cards numa cópia da árvore.
- **Fundamento:** pacotes 6 e 7 do `TK-72`.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md`
- **Passos:** substituir cada **Texto atual** pelo **Texto novo** de mesmo número; rodar as
  Verificações.
- **Texto atual 1** (uma ocorrência):

  ~~~~
  única matéria-prima é decisão; seu único produto é plano fechado. Você **tem `Bash`**, e ele
  serve a **um** uso: rodar o comando de aceite que você mesmo vai publicar num card, antes de
  publicá-lo — não é licença para levantamento próprio.
  ~~~~

- **Texto novo 1** (as quebras são as do bloco):

  ~~~~
  única matéria-prima é decisão; seu único produto é plano fechado. Você **tem `Bash`**, e ele
  serve a **dois** usos: rodar o comando de aceite que você mesmo vai publicar num card, antes de
  publicá-lo, e re-rodar o **grep de verificação de superfície** que um fato da `## 2` publica — não
  é licença para levantamento próprio. Toda lista de residências que um fato publica traz o padrão
  de grep que a produziu e a contagem que ele deu: peça ao `pantonic-scout` o padrão e a contagem,
  não só a lista, e re-rode o padrão antes de gravar.
  ~~~~

- **Texto atual 2** (fim do item 13 da Fase 4, escrito pelo `EBK-T10`; uma ocorrência):

  ~~~~
     quebrada na forma colhível, para falar dela, cria mais uma ocorrência.
  ~~~~

- **Texto novo 2** (as quebras são as do bloco; a linha em branco separa os itens):

  ~~~~
     quebrada na forma colhível, para falar dela, cria mais uma ocorrência.

  14. **Ensaio dos cards em árvore temporária** — antes de gravar, aplique os cards em sequência
     numa cópia da árvore fora do repositório e rode cada linha de `Verificação` antes e depois de
     cada card; o valor publicado é o medido no ensaio. Linha que dá o mesmo valor antes e depois
     não discrimina e volta à autoria.
  ~~~~

- **Verificação:** no PowerShell, na raiz; **antes** medido em 2026-09-25 (itens 1 e 2) e depois do
  `EBK-T10` (item 3).
  1. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'serve a **dois** usos').Count` — antes `0`, depois `1`
  2. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'serve a **um** uso').Count` — antes `1`, depois `0`
  3. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'Ensaio dos cards em árvore temporária').Count` — antes `0`, depois `1`
  4. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` → exit `0`
  5. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.
- **Pronto quando:** as três contagens saem nos valores de depois e o kit segue válido.
- **Não fazer:** não tocar `.claude/agents/pantonic-scout.md`; não renumerar itens da Fase 4.
- **Contingências:**
  - se um **Texto atual** não for encontrado exatamente uma vez → parar e sinalizar `blocked`
    razão `premissa`, citando o número do bloco.

### EBK-T12 — Três ajustes de regra existente: a devolução do modelador, o enunciado composto e o aviso de modelo [Sonnet · esforço medium · classe redacao]

- **Status:** `done` · 2026-09-26
- **Origem:** card `TK-67b` do diário de obras, seção `## TK-67`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-12`
  - OP-12: O card dos três ajustes de regra existente sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Objetivo:** o `pantonic-model-designer` passa a devolver ponteiro, cabeçalho, linha da versão,
  saída do `check` e o campo `Achados fora da seção` — em vez de recopiar a seção —, com
  `GOVERNANCA.md` §3 e §3.2 dizendo o mesmo; §3.2 reconhece o enunciado composto de atos do dono
  registrados; e o aviso da fase intelectual do hook de modelo deixa de mandar parar quem está em
  Fable.
- **Fundamento:** itens 1, 2 e 3 do insumo do veredito dos procedimentos, na seção `## TK-67` do diário de obras, com os casos
  medidos no `P-0747`.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-model-designer.md`
  - `GOVERNANCA.md`
  - `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`
  - `tests/test_materializar.py` (só o bloco 6, `DEB-10`)
- **Passos:** substituir cada **Texto atual** pelo **Texto novo** de mesmo número, no arquivo
  indicado; rodar `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate`; rodar as
  Verificações.
- **Texto atual 1** (`.claude/agents/pantonic-model-designer.md`, uma ocorrência):

  ~~~~
  Todo ato devolve exatamente duas coisas, e nada além delas:

  1. A seção **inteira e literal** — a `## 1. Modelo conceitual` na autoria; a
     `## 1A. Modelo conceitual — versão pendente de validação` em todo ato que versiona. Não um
     trecho, não um resumo do que mudou.
  2. A linha da versão do ato, registrada em `### 1.4 Registro de versões` dentro da própria seção,
     com a situação que o ato produz.

  Nenhuma prosa fora da seção, nenhum comentário sobre a qualidade do plano, nenhuma recomendação.
  ~~~~

- **Texto novo 1** (as quebras são as do bloco):

  ~~~~
  Todo ato devolve quatro coisas, e nada além delas:

  1. O **ponteiro** para a seção que o ato escreveu na árvore — a `## 1. Modelo conceitual` na
     autoria; a `## 1A. Modelo conceitual — versão pendente de validação` em todo ato que
     versiona —, com a linha `**Estado do modelo:**` copiada. A seção já está no arquivo: não a
     recopie.
  2. A linha da versão do ato, registrada em `### 1.4 Registro de versões` dentro da própria seção,
     com a situação que o ato produz.
  3. A saída literal de `python .claude/tools/modelo.py check --plano <plano>` depois do ato.
  4. O campo `Achados fora da seção:` — o que você viu fora da seção e que afeta o plano, um por
     linha, com arquivo, linha e fato —, ou `nenhum`. Quem conduz a sessão o roteia ao planejador.

  Nenhum comentário sobre a qualidade do plano e nenhuma recomendação fora do campo 4.
  ~~~~

- **Texto atual 2** (`GOVERNANCA.md` §3, matriz, linha *Modelagem*; sem quebra nova):

  ~~~~
  devolve a seção literal e a linha do registro de versões que registra o ato (`pantonic-model-designer`)
  ~~~~

- **Texto novo 2:**

  ~~~~
  devolve o ponteiro da seção, a linha do registro de versões que registra o ato, a saída do `check` e os achados fora da seção (`pantonic-model-designer`)
  ~~~~

- **Texto atual 3** (`GOVERNANCA.md` §3.2, tabela de papéis, linha *modelador*; sem quebra nova):

  ~~~~
  devolve a seção literal e a linha do ato em `### 1.4 Registro de versões`;
  ~~~~

- **Texto novo 3:**

  ~~~~
  devolve o ponteiro da seção, a linha do ato em `### 1.4 Registro de versões`, a saída do `check` e os achados fora da seção;
  ~~~~

- **Texto atual 4** (`GOVERNANCA.md` §3.2, *Lastro no enunciado*; sem quebra nova e sem refluxo):

  ~~~~
  o que o modelador imaginou. E o
  ~~~~

- **Texto novo 4:**

  ~~~~
  o que o modelador imaginou. O enunciado pode ser composto — uma frase do dono mais atos dele registrados em datas diferentes, transcritos na `## 0`, cada ato com a data e o ponteiro ao registro —, e o lastro vale igual para cada parte. E o
  ~~~~

- **Texto atual 5** (`.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, uma ocorrência):

  ~~~~
          "Se o modelo ativo NAO for Opus, PARE e peca ao dono `/model opus` antes de "
          "prosseguir (anuncie a troca — Regra 5). Se ja estiver em Opus, ignore.",
  ~~~~

- **Texto novo 5:**

  ~~~~
          "Se o modelo ativo for Sonnet ou Haiku, PARE e peca ao dono `/model opus` antes de "
          "prosseguir (anuncie a troca — Regra 5). Em Opus ou Fable, ignore: o modelo "
          "da sessao e escolha do dono.",
  ~~~~

- **Texto atual 6** (`tests/test_materializar.py`, `test_tf_hook_modelo_por_fase_executavel_stdin_utf8_classifica_a_fase`, uma ocorrência; `DEB-10`):

  ~~~~
      assert len(reparado_hostil.stdout.strip()) == 470
      saida = json.loads(reparado_hostil.stdout.decode("utf-8"))
  ~~~~

- **Texto novo 6** (a asserção de tamanho fixava o texto do aviso, que o bloco 5 muda de 470 para 510 bytes; a nova fixa a fase classificada, que é o que o teste nomeia):

  ~~~~
      saida = json.loads(reparado_hostil.stdout.decode("utf-8"))
      assert "Fase intelectual" in saida["systemMessage"]
  ~~~~

- **Verificação:** no PowerShell, na raiz; **antes** medido em 2026-09-25 (itens 1-7) e 2026-09-26 (item 8).
  1. `(Select-String -Path .claude/agents/pantonic-model-designer.md -SimpleMatch 'Achados fora da seção:').Count` — antes `0`, depois `1`
  2. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'devolve a seção literal').Count` — antes `2`, depois `0`
  3. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'O enunciado pode ser composto').Count` — antes `0`, depois `1`
  4. `(Select-String -Path .claude/global/hooks/modelo_por_fase_userpromptsubmit.py -SimpleMatch 'Em Opus ou Fable, ignore').Count` — antes `0`, depois `1`
  5. `python -m py_compile .claude/global/hooks/modelo_por_fase_userpromptsubmit.py` → exit `0`
  6. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` e `-Mode check-drift` → exit `0`
  7. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho (medido pelo consultor numa cópia com os seis blocos: `376 passed`).
  8. `(Select-String -Path tests/test_materializar.py -SimpleMatch '== 470').Count` — antes `1`, depois `0`
- **Pronto quando:** as quatro contagens saem nos valores de depois, o hook compila e o kit segue
  sem drift interno.
- **Não fazer:** não rodar `materializar.py apply` nem escrever em `C:\Users\panta\.claude\` — a
  cópia do hook no ponto de carga é do condutor, no fechamento deste card (invariante I-1); não tocar o
  aviso da fase de execução nem o `systemMessage` da fase intelectual.
- **Contingências:**
  - se um **Texto atual** não for encontrado exatamente uma vez → parar e sinalizar `blocked`
    razão `premissa`, citando o número do bloco.
- **Notas de execução:**
  - 2026-09-26 `ready` — consultor acionamento 5: DEB-10, bloco 6 no test_materializar; edicoes da arvore revertidas

### EBK-T13 — Quanto custa retomar o planejador por mensagem [Sonnet · esforço high · classe investigacao]

- **Status:** `done` · 2026-09-26
- **Origem:** card `TK-72c` do diário de obras, seção `## TK-72`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-13`
  - OP-13: O card que mede quanto custa retomar o planejador por mensagem sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Objetivo:** medir, nos transcripts do `pantonic-planner` da sessão de planejamento do `P-0747`,
  o custo de cada retomada por mensagem e o de cada invocação fria do mesmo papel; publicar a
  medida em `docs/CUSTO_DO_PICKUP.md` e aplicar a `GOVERNANCA.md` a regra que o resultado determina.
- **Fundamento:** pacote 8 do `TK-72`.
- **Arquivos-alvo:**
  - `docs/CUSTO_DO_PICKUP.md`
  - `GOVERNANCA.md`
- **Método de sondagem:**
  1. **Corpus fechado:** os arquivos `agent-*.meta.json` sob
     `C:\Users\panta\.claude\projects\d--workspaces-PantonicApp\*\subagents\` com `agentType` igual
     a `pantonic-planner` e cujo `.jsonl` irmão cita `P-0747` na primeira linha.
  2. **Segmento:** cada trecho do `.jsonl` que começa numa mensagem do tipo `user` vinda de fora do
     agente (a invocação ou uma retomada por mensagem) e vai até a próxima. O primeiro segmento de
     cada agente é a **invocação fria**; os seguintes são **retomadas**. Regra de enumeração
     (`DEB-11`), só por chaves: abre segmento a linha 0 (a invocação) e toda entrada `type=user` com
     `message.content` do tipo texto e `origin.kind == "coordinator"` (a retomada por mensagem, que
     o transcript grava com `isMeta=true`). Entrada `isMeta=true` sem `origin` (a linha 1, injetada
     pelo harness na mesma invocação) não abre segmento e fica no segmento em curso; `promptId`
     não delimita segmento. Medido pelo consultor: 2 frias e 6 retomadas, nenhuma fria com custo
     zero.
  3. **Métrica por segmento:** soma de `input_tokens`, `output_tokens`, `cache_read_input_tokens` e
     `cache_creation_input_tokens` das mensagens `assistant` com `message.id` distinto, e o custo
     com os preços da sonda `%TEMP%\claude\sonda_p0747.py` (5, 25, 0,5 e 6,25 dólares por milhão, na
     ordem); mais o intervalo, em minutos, desde o fim do segmento anterior. Adaptar a sonda
     trocando `pantonic-consultant` por `pantonic-planner`, o filtro por `P-0747` e somando por
     segmento. Nenhum texto de mensagem entra no contexto: só chaves, contagens e datas.
  4. **Agregado que volta:** no máximo 20 linhas — por grupo (fria, retomada): `n`, média, mínimo e
     máximo do custo, e o intervalo de cada retomada; e, por segmento, o número de mensagens
     `assistant` de `message.id` distinto (o custo do segmento soma o trabalho feito nele, e a seção
     publicada mostra esse volume ao lado da média).
  5. **O que cada resultado dispara:** média das retomadas **menor** que a das invocações frias →
     entra em `GOVERNANCA.md` o **Texto novo A**; **igual ou maior** → o **Texto novo B**; nenhuma
     retomada no corpus → nenhum dos dois, e a seção publica "não mensurável neste corpus".
- **Texto atual 1** (`GOVERNANCA.md` §3, uma ocorrência):

  ~~~~
    execução inline a abrir um subagente.
  ~~~~

- **Texto novo A** (as quebras são as do bloco):

  ~~~~
    execução inline a abrir um subagente.
  - **Rodada de replanejamento retoma o mesmo planejador por mensagem**, sem abrir instância fria:
    a retomada custou menos que a invocação fria do mesmo papel (`docs/CUSTO_DO_PICKUP.md`, seção
    *Retomada do planejador por mensagem*).
  ~~~~

- **Texto novo B** (as quebras são as do bloco):

  ~~~~
    execução inline a abrir um subagente.
  - **Rodada de replanejamento abre instância fria do planejador**, sem retomá-lo por mensagem: a
    retomada custou o mesmo ou mais que a invocação fria do mesmo papel (`docs/CUSTO_DO_PICKUP.md`,
    seção *Retomada do planejador por mensagem*).
  ~~~~

- **Pronto quando (o fato que tem de existir ao final):** `docs/CUSTO_DO_PICKUP.md` tem uma seção
  nova, com o próximo número da sequência, titulada `Retomada do planejador por mensagem × invocação
  fria`, com a data, o corpus, a regra de enumeração dos segmentos, o agregado do passo 4 e o
  desfecho do passo 5; e `GOVERNANCA.md` carrega exatamente o texto que o desfecho determinou.
- **Verificação:**
  1. `(Select-String -Path docs/CUSTO_DO_PICKUP.md -SimpleMatch 'Retomada do planejador por mensagem × invocação fria').Count` — antes `0`, depois `1`
  2. `(Select-String -Path GOVERNANCA.md -Pattern 'Rodada de replanejamento (retoma|abre instância fria)').Count` — antes `0`, depois `1` (ou `0`, com o desfecho "não mensurável" publicado)
  3. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.
- **Não fazer:** não ler conteúdo de mensagem dos transcripts; não medir outro papel; não mudar o
  `pantonic-planner`.
- **Contingências:**
  - se a sonda não existir no despacho → escrever a soma direto sobre o corpus do passo 1, com as
    mesmas chaves e preços.
  - se a regra do passo 2 der outro número que 2 frias e 6 retomadas, ou uma fria de custo zero →
    parar e sinalizar `blocked` razão `premissa`, citando a contagem.
- **Notas de execução:**
  - 2026-09-26 `ready` — consultor acionamento 6: DEB-11, segmento por origin.kind=coordinator; agregado com mensagens por segmento; Texto B sem a causa

### EBK-T13a — A razão da regra da retomada sai do custo de partida, não da média [Sonnet · esforço low · classe investigacao]

- **Status:** `done` · 2026-09-26
- **Origem:** corretivo da `EBK-T13`, pendência do laudo dela (`AE-5`, `DEB-12`), escrito pelo consultor no acionamento 7.
- **Operação do modelo:** `OP-13`
  - OP-13: O card que mede quanto custa retomar o planejador por mensagem sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Objetivo:** refazer a comparação da `EBK-T13` separando o custo de partida do trabalho da
  rodada, publicá-la em `docs/CUSTO_DO_PICKUP.md` ao fim da seção *Retomada do planejador por
  mensagem* e aplicar a `GOVERNANCA.md` o texto que o resultado determina.
- **Arquivos-alvo:**
  - `docs/CUSTO_DO_PICKUP.md`
  - `GOVERNANCA.md`
- **Método de sondagem:**
  1. **Corpus e segmentos:** os mesmos da `EBK-T13` (regra do `DEB-11`), com a sonda
     `%TEMP%\claude\estrutura_t13c.py`; nenhum texto de mensagem entra no contexto.
  2. **Por segmento:** `n` = mensagens `assistant` de `message.id` distinto; contexto de uma
     mensagem = `input_tokens` + `cache_read_input_tokens` + `cache_creation_input_tokens` do
     `usage` dela. Base `b` = contexto da primeira mensagem da fria do mesmo agente; carregado
     `c` = contexto da primeira mensagem da retomada menos `b`; cache expirado = o
     `cache_creation_input_tokens` da primeira mensagem da retomada é maior ou igual a `c`.
  3. **Partida, em dólares:** retomada = `c × (n × 0,5 + (5,75 se expirou, senão 0)) / 10^6`;
     fria mínima = `b × 5,75 / 10^6`; fria máxima = fria mínima + `c × 6,25 / 10^6` (a instância
     fria recria todo o contexto carregado). Por retomada: vence `retomada` se a partida dela é
     menor que a fria mínima, `fria` se é maior que a fria máxima, senão `indeterminado`.
  4. **O que cada resultado dispara** (somas das seis retomadas): partida da retomada **maior** que
     a soma das frias máximas → o Texto novo 1 e o Texto novo 2 abaixo, como estão; **menor** que a
     soma das frias mínimas → a linha da regra sai do `GOVERNANCA.md` trocada pelo Texto novo A da
     `EBK-T13`, e o Texto novo 2 termina com "O **Texto novo A** substitui o B."; **entre as duas**
     → a linha da regra sai do `GOVERNANCA.md`, e o Texto novo 2 termina com "Não mensurável neste
     corpus; a regra sai do `GOVERNANCA.md`.".
- **Medido pelo consultor (2026-09-26, só chaves):** a tabela e as somas do Texto novo 2, com o
  primeiro desfecho do passo 4 (retomada $6,30 contra frias de $1,16 a $3,80); os "antes" da
  Verificação medidos na árvore, os "depois" numa cópia com os dois textos novos aplicados.
- **Texto atual 1** (`GOVERNANCA.md` §3, uma ocorrência):

  ~~~~
  - **Rodada de replanejamento abre instância fria do planejador**, sem retomá-lo por mensagem: a
    retomada custou o mesmo ou mais que a invocação fria do mesmo papel (`docs/CUSTO_DO_PICKUP.md`,
    seção *Retomada do planejador por mensagem*).
  ~~~~

- **Texto novo 1** (as quebras são as do bloco):

  ~~~~
  - **Rodada de replanejamento abre instância fria do planejador**, sem retomá-lo por mensagem: a
    retomada relê, a cada mensagem, o contexto carregado das rodadas anteriores, e no corpus medido
    esse custo somou mais que a partida da instância fria, mesmo supondo que ela recrie todo o
    contexto carregado (`docs/CUSTO_DO_PICKUP.md`, seção *Retomada do planejador por mensagem*).
  ~~~~

- **Texto novo 2** (acrescentado ao fim de `docs/CUSTO_DO_PICKUP.md`, depois do parágrafo
  **Resultado.** da seção *Retomada do planejador por mensagem*, com uma linha em branco antes):

  ~~~~
  **Decomposição do custo de retomada (2026-09-26, EBK-T13a).** A média por segmento soma o
  trabalho feito na rodada (3 mensagens nas frias, 5 a 74 nas retomadas), e a média por mensagem
  também não decide: ela inclui os tokens de saída, que são trabalho, e dá a fria a $0,22 e as
  retomadas de $0,13 a $0,30. O que difere entre as duas opções é o custo de partida. Base `b` =
  contexto da primeira mensagem da fria; carregado `c` = contexto da primeira mensagem da
  retomada menos `b`; `n` = mensagens `assistant` de `message.id` distinto. Partida da retomada =
  `c × (n × 0,5 + 5,75 se o cache expirou)` por milhão; partida da fria = `b × 5,75` por milhão
  mais a redescoberta, entre zero e `c × 6,25` por milhão (recriar todo o contexto carregado).

  | agente | segmento | n | carregado | cache expirou | partida da retomada | partida da fria (mín–máx) | vence |
  |---|---|---|---|---|---|---|---|
  | `a19e1fec` | 1 | 7 | 18 668 | não | $0,07 | $0,19–$0,31 | retomada |
  | `a19e1fec` | 2 | 74 | 48 125 | não | $1,78 | $0,19–$0,49 | fria |
  | `a332b22b` | 1 | 5 | 32 168 | não | $0,08 | $0,19–$0,40 | retomada |
  | `a332b22b` | 2 | 14 | 56 587 | sim | $0,72 | $0,19–$0,55 | fria |
  | `a332b22b` | 3 | 9 | 121 526 | não | $0,55 | $0,19–$0,95 | indeterminado |
  | `a332b22b` | 4 | 43 | 144 261 | não | $3,10 | $0,19–$1,10 | fria |

  Soma: partida das retomadas $6,30; partida da fria de $1,16 a $3,80. A retomada vence as rodadas
  curtas (5 e 7 mensagens, $0,11 a $0,13 a menos cada, contra a fria mínima) e perde as longas
  ($0,17 a $2,01 a mais cada, contra a fria máxima); no corpus, abrir fria custa menos mesmo
  supondo que ela recrie todo o contexto carregado. O **Texto novo B** fica, com a razão reescrita.
  ~~~~

- **Pronto quando:** `docs/CUSTO_DO_PICKUP.md` termina com a decomposição do passo 3 e o desfecho
  do passo 4, e `GOVERNANCA.md` carrega exatamente o texto que o desfecho determinou.
- **Verificação:**
  1. `(Select-String -Path docs/CUSTO_DO_PICKUP.md -SimpleMatch 'Decomposição do custo de retomada').Count` — antes `0`, depois `1`
  2. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'mesmo supondo que ela recrie').Count` — antes `0`, depois `1`
  3. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'custou o mesmo ou mais').Count` — antes `1`, depois `0`
  4. `(Select-String -Path GOVERNANCA.md -Pattern 'Rodada de replanejamento (retoma|abre instância fria)').Count` — antes `1`, depois `1`
  5. `python -m pytest -q` → nenhuma falha; `passed` = o do despacho (nenhum teste lê os dois arquivos, medido por grep em `tests/`).
- **Não fazer:** não ler conteúdo de mensagem dos transcripts; não mudar a seção *Retomada do
  planejador por mensagem* acima do parágrafo **Resultado.**, nem ele; não mudar outra linha do
  `GOVERNANCA.md`.
- **Contingências:**
  - se a sonda der número diferente da tabela do Texto novo 2 em qualquer célula, ou outro
    desfecho do passo 4 → parar e sinalizar `blocked` razão `premissa`, citando a célula e os dois
    valores.

### EBK-T14 — A rodada de revisão de guardrails pendente desde 2026-08-08 [Opus · esforço high · classe investigacao]

- **Status:** `done` · 2026-09-26
- **Origem:** card `TK-67a` do diário de obras, seção `## TK-67`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-14`
  - OP-14: O card da rodada de revisão das regras de guarda sai de pronto para concluído, sobre o backlog que a operação anterior deixou.
  - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Objetivo:** registrar em `GOVERNANCA.md` §7.1, *Registro das rodadas*, a rodada disparada
  pelos planos fechados depois da rodada `P-0731`, aplicando o procedimento de §7.1 às guardrails
  em escopo, e marcar `OBSOLETA desde <rodada>` a que ficar sem caso citável.
- **Arquivos-alvo:**
  - `GOVERNANCA.md`
- **Método de sondagem:**
  1. **Rótulo e gatilho.** A rodada se rotula pelo plano fechado mais recente, `P-0750`, e pela data
     da execução: `P-0750 — <AAAA-MM-DD>`. Os planos que a disparam são os `done` do índice de
     `docs/DIARIO_DE_OBRAS.md` fechados depois de 2026-08-08: `P-0732`, `P-0735`, `P-0736`,
     `P-0738`, `P-0739`, `P-0740`, `P-0741`, `P-0743`, `P-0745`, `P-0746`, `P-0747`, `P-0748`,
     `P-0749` e `P-0750` (medido em 2026-09-25).
  2. **Escopo.** O registro ainda não tem duas rodadas do regime por plano, então a `1.4.0` segue
     como penúltima e o escopo é o mesmo da rodada `P-0731`: treze guardrails, por nome — regra de
     dependência, ACL, egress G6, namespace de estado, gate de conformance, allowlist de
     subcomandos destrutivos, piso de regressão, disciplina de contexto, `G-DEADCODE`,
     `G-PLANFIDELITY`, `G-PREMISE`, `G-PLANREADY` e `G-EXECREADY`. Fora por idade: `G-README`,
     `G-SCOPE`, `G-SURFACE`, `G-REPLAN`, `G-NOASK`, `G-MODULO` e `G-TOOLDENY`.
  3. **Isenção, re-confirmada e não herdada.** Para cada uma das seis isentas na rodada `P-0731`,
     rodar hoje o check que a isentou e registrar a linha de sumário: em
     `D:\workspaces\PantonicVideo`, `python -m pytest tests/conformance/test_layer_imports.py
     tests/conformance/test_acl_no_external_in_plugins.py tests/conformance/test_filesystem_egress.py
     tests/boundary/test_state_writer_namespacing.py -q -rs`; no hub, `python -m pytest -q`; e a
     contagem de `permissions.deny` em `.claude/settings.json`. Check que não roda, que sai com
     `skip`/`xfail` no alvo ou cuja lista cobre tudo **não isenta**: a guardrail vai para o passo 4
     e o check morto entra na entrada como achado.
  4. **Pergunta única**, para cada guardrail em escopo e não isenta: *"Esta regra mudou algum
     comportamento desde a penúltima rodada registrada? Cite o caso."* Caso citável é ocorrência
     **registrada** entre 2026-08-08 e a data da execução — em `docs/DIARIO_DE_OBRAS.md`,
     `docs/DIARIO_HISTORICO.md`, `docs/plans/`, `docs/RDO/`, `docs/Entregas Aceitas/` ou no diário de
     `D:\workspaces\PantonicVideo` — em que a regra bloqueou algo, forçou correção ou embasou
     decisão. Suíte verde não é caso; lembrança sem registro não é caso. O caso se cita por
     arquivo e identificador (`AE-`, `DB-`, id de tarefa).
  5. **Resultado.** Guardrail sem caso citável recebe, no próprio item de §7, a marca
     `OBSOLETA desde P-0750` — permanece em vigor por uma rodada, e a remoção é tarefa da rodada
     seguinte. Zero marcações é resultado legítimo.
- **Pronto quando (o fato que tem de existir ao final):** a entrada `P-0750 — <data>` no *Registro
  das rodadas* de §7.1, com os planos que a dispararam, as treze em escopo, as sete fora por
  idade, cada isenta com o check e a linha de sumário de hoje, e cada uma das demais com o caso
  citável (arquivo e identificador) ou com a marca aplicada no item de §7.
- **Verificação:**
  1. Contagem da entrada nova:

     ```
     (Select-String -Path GOVERNANCA.md -Pattern '^- \*\*.P-0750. — 2026-').Count
     ```

     antes `0` (medido em 2026-09-25), depois `1`.
  2. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.
- **Não fazer:** não criar guardrail; não remover guardrail (remoção é da rodada seguinte); não
  editar plano fechado; não tocar as matérias do `EBK-T12`.
- **Contingências:**
  - se `D:\workspaces\PantonicVideo` ou um dos quatro arquivos de teste não existir → a guardrail
    daquele check vai para o passo 4, e a entrada registra `check ausente: <caminho>`.

## 6. Ordem de execução

`EBK-T1` → `EBK-T2` → … → `EBK-T14`, sequencial (DEB-3). `EBK-T11` depende de `EBK-T10`. O corretivo `EBK-T5a` vem logo depois da `EBK-T5` (DEB-9); o `EBK-T13a`, logo depois da `EBK-T13` (DEB-12).

## 7. Fora de escopo

- A publicação do kit e o `TK-81a` (F-4).

## 8. Achados da execução

- **AE-1** (`EBK-T1`, `blocked` premissa, 2026-09-25) — a contingência mandava a subtarefa da fixture herdar "o mesmo status do tíquete"; o `TK-2` da `vermelho` tem `backlog`, fora do vocabulário, e a herança duplicaria o `C-3`. Absorvido pelo consultor no card (contingência 1) e em `DEB-6`. Régua de autoria (`EBK-T10`): contingência que copia um valor de fixture confere se a fixture carrega aquele valor de propósito. **Rota:** resolve — absorvido pelo consultor no card da `EBK-T1` (`DEB-6`).
- **AE-2** (`EBK-T5`, laudo `ressalva` 91%, 2026-09-25) — quatro achados de processo. (1) O objetivo prometeu o número de defeitos em `kit_check: check-drift FALHOU` e em `kit_check: FALHOU`, e o card só prescreveu o README: os dois ramos do `materializar.py` seguem contando a linha de sumário dele (medido: 13 problemas para 12 defeitos no `check-drift` de uma cópia do kit; 2 para 1 no `validate` com uma entrada do manifesto apontando arquivo ausente). (2) As linhas de detalhe do README saem com o marcador de item, e a lista tem mais itens que o número do cabeçalho. (3) O `review_evidence.py` com `--desde` lista como "sem atribuição" os não rastreados anteriores ao commit do despacho (19 na `EBK-T5`). (4) O `rdo.py laudo` não tem campo para o motivo de dimensão fora de `conforme`, e o alvo `dossiê` que o `pantonic-reviewer` grafa é recusado pelo gerador, que só aceita `dossie`. Destino (`DEB-9`): (1) e (2) no corretivo `EBK-T5a`; (3) no `TK-84`; (4) no `TK-85`, os dois com card no diário. Régua de autoria (`EBK-T10`): objetivo que nomeia mais de um caso tem um caso prescrito e testado para cada um; card de instrumento que conta problema confere de onde vem cada linha contada. **Rota:** corretivo `EBK-T5a` para (1) e (2); tíquetes `TK-84` para (3) e `TK-85` para (4) (`DEB-9`).
- **AE-5** (`EBK-T13`, laudo `aprovado` 100% com recomendação `escalar`, 2026-09-26; regra `A8a`/`B1`) — A regra 'Rodada de replanejamento abre instância fria do planejador', que o EBK-T13 pôs na GOVERNANCA.md §3 como o card mandava, se apoia numa comparação de médias sem normalizar pelo volume. Normalizada por mensagem, a comparação se inverte em 5 das 6 retomadas. A triagem do consultor decide se a regra fica ou se abre tíquete para medir de novo. Destino (`DEB-12`): a regra fica, e a razão dela passa ao custo de partida no corretivo `EBK-T13a`. Régua de autoria (`EBK-T10`): função de desfecho que compara custo de segmentos normaliza pelo que as opções têm de diferente, e não pelo volume de trabalho da rodada. **Rota:** corretivo `EBK-T13a` (`DEB-12`).
- **AE-6** (fechamento do plano, condutor, 2026-09-26) — (1) `python .claude/tools/backlog.py check --repo <cópia da fixture verde>` sai exit 1 com `C-17 GOVERNANCA.md:1 — piso_c11 nomeia entrada órfã: `GOVERNANCA.md` §1.1`: o subcomando `check` liga `piso_c11=_PISO_C11` para qualquer `--repo`, e toda entrada do piso deste repositório sai órfã em outro corpus (efeito provável nos kits derivados). (2) `backlog.py next`/`show` do `EBK-T14`, último card antes da `## 6`, imprimiu como dossiê também as seções `## 6`, `## 7` e `## 8` do plano. Destino (`DEB-13`, consultor, acionamento 8): (1) no `TK-86`, (2) no `TK-87`, os dois com card `ready` no diário. Régua de autoria: dado medido num corpus (piso, lista de dívida) não mora em constante de instrumento que vai a outro corpus; e a fronteira de um card na leitura do instrumento é a mesma que o autor vê, o cabeçalho seguinte do plano. **Rota:** tíquetes `TK-86` para (1) e `TK-87` para (2) (`DEB-13`).
