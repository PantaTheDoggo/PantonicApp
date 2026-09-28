# Operações as-is — `P-0752`, "Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção"

Documento de validação do plano `docs/plans/P-0752-fato-no-ponto-de-uso.md`. Descreve o estado das
operações que o plano deixou em 2026-09-27, com exemplos de saídas reais rodadas nessa data.

---

## Por que o plano existiu

**O problema.** Uma amostra de 2026-09-26 classificou 156 trechos de transcrição de agentes de
todos os projetos, mais 40 linhas da tabela de acionamentos do consultor, ~60 lições de RDO e 118
achados de execução dos cinco planos anteriores. A classificação por causa: valor reutilizado do
contexto em vez de medido no instante do uso, ~35%; premissa afirmada na autoria de uma tarefa ou
no despacho dela sem sondar a árvore real, ~30%; auto-relato aceito como medida, ~10%; regra ou
precedente já registrado e não aplicado conforme a janela avança, ~10%; semântica de ferramenta
suposta, ~8%; contexto do dono presumido compartilhado, ~5%. Dos 40 acionamentos do consultor até
essa data, 25 eram por card com defeito de autoria ou por premissa não sondada — 62,5%. O
instrumento que já existia para conferir a forma de uma tarefa antes do despacho (`card_check.py`)
estava escrito e sem efeito: nenhum passo do loop de execução o chamava.

**A solução, em uma frase.** O que era lembrança de quem executa, ou frase de skill que pede para
"conferir antes", vira comando que roda no ponto de uso e falha de forma visível quando o estado
real da árvore diverge do que a tarefa afirma.

**Vocabulário mínimo.**

| termo | o que é |
|---|---|
| card | a tarefa de plano ou de tíquete, com as premissas, as âncoras de arquivo e os números que ela afirma sobre a árvore |
| régua executável | o conjunto de conferências que passam a rodar por comando no ponto de uso, em vez de dependerem de alguém lembrar |
| gate do card | a conferência `card_check.py`, que roda antes do despacho de uma tarefa e recusa o card cuja forma, âncora ou número não bate com a árvore real |
| dossiê de despacho | o texto que `backlog.py show` ou `backlog.py next` entrega a quem vai executar uma tarefa |
| achado (`AE-<n>`) | a entrada de defeito que um laudo de revisão deixa na seção "Achados da execução" de um plano, com uma rota de destino |
| RDO | o registro de fechamento de uma tarefa, gerado por `encerrar.py` em `docs/RDO/` |
| consultor | o papel que tria toda parada de um executor durante a execução de um plano e decide a rota: reparo do card, tíquete novo, ou ato do dono |
| veredito | o julgamento que o revisor grava no RDO: aprovado, ressalva ou recusado |

---

## O arco — oito estratos

| estrato | pergunta que responde | tarefas |
|---|---|---|
| 1. O gate do card | a forma que o card afirma sobre a árvore é a forma real, e o gate roda antes do despacho? | `FPU-T1`, `FPU-T1a`, `FPU-T3`, `FPU-T2` |
| 2. O aviso de crença | um número de aceite sem comando ao lado é notado no ato de gravar? | `FPU-T4`, `FPU-T4a` |
| 3. A medida do executor | o retorno de uma tarefa é um arquivo que o revisor lê, ou uma frase que se acredita? | `FPU-T5`, `FPU-T5a`, `FPU-T5b`, `FPU-T5c` |
| 4. O precedente herdado | quem despacha precisa lembrar de um achado anterior, ou o dossiê o carrega sozinho? | `FPU-T6` |
| 5. A duplicata na telemetria | quem grava uma linha de consumo precisa conferir antes, ou o escritor recusa por conta própria? | `FPU-T7` |
| 6. As armadilhas de ferramenta | a semântica que já enganou um agente está escrita em algum lugar, ou cada um a redescobre? | `FPU-T8`, `FPU-T8a` |
| 7. A origem do número | toda mensagem ao dono declara de onde vem o número que ela carrega? | `FPU-T9`, `FPU-T9a` |
| 8. A causa raiz da parada | cada parada do consultor tem uma classe de erro nomeada, em vez de só um relato solto? | `FPU-T10` |

O estrato 1 é a base: os estratos 2 a 8 acrescentam conferências novas à mesma régua, e a `FPU-T2`
(religar o gate no loop e na autoria) só entra depois de os instrumentos que ela cita existirem —
por isso ela fecha o estrato 1, depois de `FPU-T1`, `FPU-T3` e `FPU-T5`. Seis das dezessete tarefas
(`FPU-T1a`, `FPU-T4a`, `FPU-T5b`, `FPU-T5c`, `FPU-T8a`, `FPU-T9a`) são cards corretivos, nascidos de
um achado no fechamento de outro card do próprio plano — nenhuma foi cancelada, e cada uma tem
seção própria porque cada uma entrega um comportamento que não existia antes dela.

---

## Estrato 1 — O gate do card

### `FPU-T1` — O gate lê a forma real da Verificação, não uma forma imaginada

**Contexto que a motivou:** `card_check.py` só reconhecia uma forma de escrever a Verificação de
uma tarefa (bloco de comando cercado, com a linha `**Medido antes:**`). O corpus vivo de planos
usava outra forma, inline, em 67 dos itens de um único plano anterior e em zero linhas
`Medido antes:`. Rodado sobre uma tarefa `done` e aceita de um plano anterior, o gate acusava
"item fora da forma" em todos os itens — um item fantasma, porque o marcador de item casava
qualquer `N.` dentro do texto corrido, inclusive em prosa.

**O que é o artefato:** a função `_parsear_itens` (`.claude/tools/card_check.py:137`), que agora lê
as linhas brutas de cada item em vez do texto achatado, e `verificar_tarefa`
(`.claude/tools/card_check.py:332`), que deriva o "mundo" comparado do status do card (`done`
compara o valor "depois"; qualquer outro status compara o valor "antes"). O suporte para linhas
brutas por campo vem de `rdo._parsear_campos_com_linhas` (`.claude/tools/rdo.py`).

**Como funciona na prática:**
1. **O que dispara:** `python .claude/tools/card_check.py --plano <plano> --tarefa <ID>`.
2. **A entrada:** as linhas brutas do campo `Verificação` do card, em qualquer uma das duas formas.
3. **O processamento:** cada item roda o comando citado e compara a saída com o valor esperado do
   mundo resolvido.
4. **A saída:** exit `0` e `card_check: OK` quando todo item bate; exit `1` com uma falha nomeada
   por item quando não. Rodado hoje (2026-09-27) sobre a fixture do próprio corpus:

   ```
   $ python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-corpus.md --tarefa CX-T1
   card_check: OK - tarefa 'CX-T1' fecha.
   ```

   Rodado sobre a própria `FPU-T1`, já `done` (mundo "depois"): a suíte cresceu de 397 para 452
   testes desde o fechamento do card, e o item que afirma "73 passed" diverge do que a árvore mede
   hoje —

   ```
   $ python .claude/tools/card_check.py --plano docs/plans/P-0752-fato-no-ponto-de-uso.md --tarefa FPU-T1
   item 1: divergencia - valor do mundo (depois) declara '73 passed', execução mediu exit 0 saída
   '...89 passed in 2.32s'
   card_check: FALHOU - 1 item(ns) da tarefa 'FPU-T1' não fecham.
   ```

   Isso não é regressão da entrega: é a própria classe de número que envelhece, agora visível
   sobre o card do próprio plano que a combate (ver pendências).

**Protege contra:** um item de Verificação nunca lido pelo gate porque a forma dele não era a
forma que o instrumento esperava, e um item fantasma nascido de prosa que por acaso começa por
`N.` numa linha de continuação.

### `FPU-T1a` — Um teste tranca o marcador de item só no início de linha

**Contexto que a motivou:** o comportamento acima (marcador só no início de linha) já existia
depois da `FPU-T1`, mas nenhum teste o trancava com o caso exato do fantasma original: prosa que
contém `1.` e `2.` na continuação do próprio item de Verificação, não em outro campo.

**O que é o artefato:** o card `CX-T5` acrescentado a `tests/fixtures/card_check/plano-corpus.md` e
o teste `test_tf_prosa_na_continuacao_do_item_nao_vira_item` em `tests/test_card_check.py`.

**Como funciona na prática:** o teste roda `card_check.verificar_tarefa` sobre um item cuja
continuação cita "acionamento 1." e "revisão 2." em prosa, e afirma que o resultado tem exatamente
dois itens, não quatro. Rodado hoje:

```
$ python -m pytest tests/test_card_check.py -q -k prosa_na_continuacao
```

fecha em verde.

**Protege contra:** uma regressão futura do parser de item devolver a contar prosa como item de
Verificação sem que nenhum teste a note.

### `FPU-T3` — Toda âncora de arquivo e linha leva o literal, e o gate confere a linha de hoje

**Contexto que a motivou:** uma âncora como `` `arquivo.py:184` `` em um card apontava um número
de linha sem dizer o que deveria estar lá. Se o arquivo mudasse depois, a âncora envelhecia em
silêncio — ninguém era avisado de que a linha 184 já era outra coisa.

**O que é o artefato:** a função `conferir_ancoras` (`.claude/tools/card_check.py:272`), chamada
por `verificar_tarefa` só quando o card ainda não está `done`.

**Como funciona na prática:** ela varre as linhas de `Arquivos-alvo` e do campo `Passos` de um
card, procurando o padrão `` `caminho:linha` `` seguido de um literal entre crases, e confere se
esse literal está contido em alguma linha da faixa `linha..fim` do arquivo real. Rodado hoje sobre
uma fixture com uma âncora repetida e sem literal na segunda ocorrência:

```
$ python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-ancoras.md --tarefa AN-T2
âncora sem literal: `tests/fixtures/card_check/alvo.txt:2`
card_check: FALHOU - 1 item(ns) da tarefa 'AN-T2' não fecham.
```

A conferência fica fora de `Objetivo`, `Verificação` e `Contratos` — só `Arquivos-alvo` e `Passos`
são varridos, porque só esses dois campos citam onde a entrega deve tocar a árvore.

**Protege contra:** uma âncora de arquivo e linha que envelhece sem que ninguém note, e uma tarefa
que afirma tocar uma linha que, na prática, diz outra coisa.

### `FPU-T2` — O gate roda no ensaio da autoria e no despacho do loop

**Contexto que a motivou:** o gate acima existia como código, mas nenhum passo do processo de
planejamento nem do processo de execução o chamava — ele estava escrito e sem efeito desde
2026-09-19, por uma nota que o declarava suspenso.

**O que é o artefato:** um quarto gate mecânico na skill que conduz o loop de execução
(`.claude/skills/scrum-master/SKILL.md`), um item novo na checagem que autoriza delegar uma tarefa
(`.claude/skills/passagem-de-bastao/SKILL.md`), um passo novo no processo de autoria de plano
(`.claude/agents/pantonic-planner.md`) e a remoção da nota de suspensão em
`docs/RUBRICA_DE_REVISAO.md`.

**Como funciona na prática:** antes de qualquer tarefa ser despachada a um executor, o condutor do
loop roda `card_check.py --plano <plano> --tarefa <ID>`; exit `1` impede a delegação e devolve a
tarefa à triagem, em vez de seguir para quem executa. Hoje, `docs/RUBRICA_DE_REVISAO.md` não contém
mais o texto da suspensão:

```
$ python -c "from pathlib import Path;print('suspenso em efeito' in Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8'))"
False
```

**Protege contra:** um instrumento de conferência escrito e nunca chamado — a forma mais barata de
parecer que existe uma regra sem ela nunca ter rodado.

---

## Estrato 2 — O aviso de crença

### `FPU-T4` — Um gancho avisa, no ato de gravar, todo número sem comando ao lado

**Contexto que a motivou:** um plano ou o diário de obras podia registrar um número de aceite (por
exemplo, "`397 passed`") sem nenhum comando ao lado que o comprovasse. Esse número passava a ser
citado depois como fato, mesmo sendo, na origem, uma afirmação não verificada.

**O que é o artefato:** o gancho `.claude/tools/crenca_hook.py`, disparado pelo harness a cada
gravação (`Write` ou `Edit`) em `docs/plans/**` ou em `docs/DIARIO_DE_OBRAS.md`.

**Como funciona na prática:**
1. **O que dispara:** o harness chama o gancho antes de gravar, com o conteúdo novo no payload.
2. **A entrada:** o texto que está sendo escrito.
3. **O processamento:** `contar_crencas` (`.claude/tools/crenca_hook.py:42`) procura literais
   numéricos de aceite (contagem de teste, `antes`/`depois`, âncora de linha) que não estão na
   mesma linha de um comando nem dentro de um bloco cercado.
4. **A saída:** um aviso, nunca um bloqueio. Rodado hoje com um payload sintético cujo texto cita
   "410 passed" em prosa, sem comando ao lado:

   ```
   $ echo '{"tool_name":"Write","tool_input":{"file_path":"docs/plans/...","content":"...410 passed em prosa..."}}' | python .claude/tools/crenca_hook.py
   {"systemMessage": "1 número(s) de aceite sem comando no texto novo: número sem comando é crença — medir antes de gravar"}
   ```

**Protege contra:** um número de aceite que se torna fato só porque foi escrito, sem nenhum comando
que o tenha medido.

### `FPU-T4a` — Cada literal conta uma vez, mesmo quando dois padrões o casam

**Contexto que a motivou:** o texto "`antes \`397 passed\`, depois \`401 passed\`" casava dois
padrões de contagem no mesmo trecho (o padrão genérico de "`N` passed" e o padrão do par
antes/depois), e o aviso relatava "4 números" onde havia dois literais.

**O que é o artefato:** o agrupamento de trechos sobrepostos dentro de `contar_crencas`
(`.claude/tools/crenca_hook.py:42`): casamentos cujo intervalo de caracteres se sobrepõe contam como
um só.

**Como funciona na prática:** o mesmo texto do exemplo acima agora conta 2, não 4 — confirmado pelo
teste `test_tf_literais_sobrepostos_contam_uma_vez` de `tests/test_crenca_hook.py`, que roda a
função direto sobre o trecho.

**Protege contra:** um aviso que exagera a gravidade do que encontrou, o que treina quem lê a
ignorá-lo.

---

## Estrato 3 — A medida do executor

### `FPU-T5` — A verificação de uma tarefa sai como arquivo, não como frase de quem a rodou

**Contexto que a motivou:** o retorno de uma tarefa executada era só a linha final de quem a
executou — nenhum artefato comprovava que os comandos de Verificação de fato rodaram, e um
auto-relato de "verde" não tinha como ser conferido sem repetir o trabalho.

**O que é o artefato:** o parâmetro `--gravar <caminho.json>` de `card_check.py` (função `main`), e
a seção nova `## Medida do executor` que `review_evidence.py` acrescenta a um dossiê de evidência
quando o arquivo existe — `secao_medida_do_executor` em `.claude/tools/review_evidence.py:701`.

**Como funciona na prática:**
1. **O que dispara:** `card_check.py ... --gravar <caminho>`, chamado como o último passo antes da
   linha de retorno de uma tarefa.
2. **A entrada:** os mesmos itens de Verificação que o gate já roda.
3. **O processamento:** cada item roda de verdade, e o resultado (comando, código de saída, saída,
   se bateu com o esperado) vira um registro.
4. **A saída:** um JSON gravado no disco. Rodado hoje sobre a fixture:

   ```
   $ python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-corpus.md --tarefa CX-T1 --gravar /tmp/opas/medida-CX-T1.json
   card_check: OK - tarefa 'CX-T1' fecha.
   $ cat /tmp/opas/medida-CX-T1.json
   {
     "plano": "tests/fixtures/card_check/plano-corpus.md",
     "tarefa": "CX-T1",
     "mundo": "antes",
     "gerado_em": "2026-09-27T04:42:16+00:00",
     "itens": [{"indice": 1, "comando": "python -c \"print('a')\"", "exit": 0, "saida": "a", "bate": true}]
   }
   ```

   Quando o arquivo não existe, o dossiê de evidência mostra a seção com a palavra `ausente` — a
   ausência de medida também é informação.

**Protege contra:** o "verde" que ninguém mediu de fato, aceito porque quem executou disse que
estava tudo certo.

### `FPU-T5a` — O executor, o revisor e o loop passam a falar do arquivo de medida

**Contexto que a motivou:** o artefato acima existia, mas nada nos processos de execução, revisão
e condução do loop mandava gerá-lo ou lê-lo — ele ficaria como um recurso disponível e não usado.

**O que é o artefato:** um passo novo no processo do executor
(`.claude/agents/pantonic-executor.md`), uma frase no processo do revisor
(`.claude/agents/pantonic-reviewer.md`) que declara a seção `## Medida do executor` como a única
afirmação de verde admitida, e uma frase no relatório de recepção do loop
(`.claude/skills/scrum-master/SKILL.md`).

**Como funciona na prática:** todo executor roda `card_check.py --mundo depois --gravar <caminho>`
antes de encerrar; todo revisor lê a seção da evidência em vez de aceitar a palavra de quem
executou; `ausente` na seção conta como verificação não feita, não como aprovação por omissão.

**Protege contra:** um processo que cria um instrumento de medida e continua confiando em prosa
porque nenhum papel foi instruído a usar o instrumento.

### `FPU-T5b` — A medida guarda o fim da saída, onde mora o sumário

**Contexto que a motivou:** o JSON de medida guardava os primeiros 400 caracteres da saída de cada
comando. Numa saída de `pytest`, os primeiros caracteres são a barra de pontos de progresso, e o
sumário ("`N passed`") — o único número que interessa — ficava fora do arquivo.

**O que é o artefato:** a troca de `saida.strip()[:400]` por `saida.strip()[-400:]` em
`.claude/tools/card_check.py`, nas duas formas de item (a antiga e a inline).

**Como funciona na prática:** o teste `test_tf_gravar_guarda_a_cauda_da_saida`
(`tests/test_card_check.py`) grava a medida de um comando cuja saída tem mais de 400 caracteres e
confirma que o JSON termina no sumário do comando, não no seu início.

**Protege contra:** um arquivo de medida que existe, mas guarda a parte da saída que menos importa.

### `FPU-T5c` — A medida mora onde o revisor a procura, no plano legado e no plano em pasta

**Contexto que a motivou:** o executor gravava a medida num caminho fixo
(`docs/RDO/evidencia/<plano>-<ID>-medida.json`), mas `review_evidence.py` procura o JSON no
diretório-pai do destino da evidência — que em um plano organizado em pasta própria não é
`docs/RDO/evidencia`. Um plano em pasta gravaria a medida onde o revisor nunca olha, e a evidência
diria `ausente` mesmo com o executor tendo cumprido o texto.

**O que é o artefato:** a correção do caminho citado no processo do executor
(`.claude/agents/pantonic-executor.md`) e no relatório de recepção do loop
(`.claude/skills/scrum-master/SKILL.md`), agora derivado como `review_evidence.py` o resolve, e não
mais um literal fixo.

**Como funciona na prática:** o caminho é `<diretório de evidência>/<id do plano>-<ID>-medida.json`,
com `<diretório de evidência>` igual a `docs/RDO/evidencia` no plano legado (o caso do `P-0752`) ou
à pasta própria do plano quando ele estiver organizado em pasta.

**Protege contra:** um artefato que existe, foi gerado como o texto pedia, e mesmo assim não é
encontrado por quem deveria lê-lo — o mesmo defeito de fundo que a `FPU-T5` combate, agora na borda
entre dois formatos de plano.

---

## Estrato 4 — O precedente herdado

### `FPU-T6` — O dossiê de despacho carrega os achados já roteados a este card

**Contexto que a motivou:** um achado de revisão registrado no plano (uma entrada `AE-<n>` com uma
rota que cita uma tarefa futura) só chegava a quem fosse executar essa tarefa se alguém lembrasse de
colar o achado no despacho. A memória de quem despacha era o único carregador desse precedente.

**O que é o artefato:** as funções `achados_roteados` (`.claude/tools/backlog.py:1058`) e
`_bloco_achados` (`.claude/tools/backlog.py:1098`), chamadas por `show` e por `next` quando o alvo é
uma tarefa de um plano.

**Como funciona na prática:**
1. **O que dispara:** `backlog.py show <ID>` ou `backlog.py next`.
2. **A entrada:** o texto do plano e o identificador da tarefa.
3. **O processamento:** procura, na seção de achados do plano, toda entrada `AE-<n>` cuja rota cita
   o identificador da tarefa como palavra inteira.
4. **A saída:** um bloco `**Achados roteados a este card:**` logo depois do texto do card, com cada
   achado encontrado, ou a palavra `nenhum`. Rodado hoje sobre a própria `FPU-T1`:

   ```
   $ python .claude/tools/backlog.py show FPU-T1
   ...
   **Achados roteados a este card:**
   - **`AE-1`** (2026-09-26, `FPU-T1` `blocked` premissa) — [...] **Rota:** absorvido [...]
   - **`AE-2`** (2026-09-26, `FPU-T1` `blocked` premissa, 2ª parada) — [...]
   - **`AE-3`** (2026-09-26, `FPU-T1` `blocked` premissa, 3ª parada) — [...]
   ```

   Um card sem nenhum achado roteado (por exemplo, uma tarefa de tíquete) mostra
   `**Achados roteados a este card:** nenhum`, e não muda nada no dossiê de plano inteiro nem de
   tíquete.

**Protege contra:** repetir, na execução seguinte, um defeito que já foi encontrado e registrado
numa execução anterior — só porque quem despachou a tarefa não lembrou dele.

---

## Estrato 5 — A duplicata na telemetria

### `FPU-T7` — O escritor da série de telemetria recusa a linha repetida da mesma rodada

**Contexto que a motivou:** um gancho automático e um fechamento manual podiam apensar, cada um, uma
linha de consumo para a mesma tarefa — a mesma rodada de trabalho contada duas vezes na série.

**O que é o artefato:** `checar_repetida` (`.claude/tools/telemetria.py:149`), chamada por
`append_row` antes de qualquer escrita e, também, pelo fechamento de tarefa
(`.claude/tools/encerrar.py`) antes da primeira escrita do fechamento — a recusa fica no escritor, e
vale para todo chamador, não só para quem lembrar de checar antes.

**Como funciona na prática:** quando a última linha da mesma tarefa na série tem o mesmo modelo, o
mesmo número de usos de ferramenta e os mesmos milhares de tokens da linha nova, a escrita é
recusada. Rodado hoje contra um TSV temporário (nunca contra `docs/telemetria.tsv`):

```
$ python .claude/tools/telemetria.py append --data 2026-09-27 --projeto PantonicApp --tarefa OPAS-TESTE \
    --modelo sonnet --tool_uses 10 --tokens_k 50.0 --duracao_s 100.0 --fonte contado --file /tmp/t.tsv
telemetria: OK - linha adicionada a '/tmp/t.tsv'.
$ python .claude/tools/telemetria.py append --data 2026-09-27 --projeto PantonicApp --tarefa OPAS-TESTE \
    --modelo sonnet --tool_uses 10 --tokens_k 50.0 --duracao_s 999.0 --fonte contado --file /tmp/t.tsv
telemetria: FALHOU - linha repetida: OPAS-TESTE já tem linha com modelo, tool_uses e tokens_k iguais (data 2026-09-27)
```

exit `3` na segunda chamada, e o arquivo continuou com uma linha só.

**Protege contra:** o total de consumo de uma janela de trabalho saindo inflado porque duas fontes
diferentes gravaram a mesma rodada.

---

## Estrato 6 — As armadilhas de ferramenta

### `FPU-T8` — As armadilhas de ferramenta medidas ganham um arquivo só

**Contexto que a motivou:** o mesmo engano de ferramenta era redescoberto por agentes diferentes em
momentos diferentes — por exemplo, que aspas duplas do PowerShell expandem `` `t `` e convertem
`\t` em tabulação, ou que `Measure-Object -Line` ignora linha vazia. O conhecimento sobre cada
armadilha estava espalhado entre memória pessoal, achados de execução e lições soltas de RDO.

**O que é o artefato:** `docs/ARMADILHAS_DE_FERRAMENTA.md`, uma tabela
`ferramenta | armadilha | caso medido | forma segura`, apontada por `GOVERNANCA.md`, pelo processo
de autoria de card (`.claude/agents/pantonic-planner.md`) e por `docs/DOC_MAP.md`.

**Como funciona na prática:** quem vai escrever uma linha de Verificação consulta o arquivo antes;
quem mede uma armadilha nova apensa uma linha. O arquivo nasceu com oito linhas e hoje tem nove — a
nona (a ferramenta Bash reduzindo `\\` a `\` antes de o comando ser lido) foi medida e apensada
depois do fechamento desta tarefa, exercitando a própria regra que ela deixou:

```
$ python -c "from pathlib import Path;print(Path('docs/ARMADILHAS_DE_FERRAMENTA.md').read_text(encoding='utf-8').count(chr(10)+'| '))"
9
```

**Protege contra:** o mesmo engano de sintaxe ou de semântica de ferramenta custando o tempo de ser
redescoberto por um agente diferente do que já pagou por ele.

### `FPU-T8a` — A régua de autoria do card aponta as armadilhas de ferramenta

**Contexto que a motivou:** a `FPU-T8` apontou o arquivo de armadilhas em dois lugares
(`GOVERNANCA.md` e o processo de autoria do planejador), mas a seção de `docs/RUBRICA_DE_REVISAO.md`
que se declara, no próprio texto, "régua de autoria do card" ficou sem o ponteiro — exatamente o
segundo lugar que o card deveria ter apontado.

**O que é o artefato:** uma frase acrescentada à linha de abertura da seção `## 8` de
`docs/RUBRICA_DE_REVISAO.md`.

**Como funciona na prática:** quem lê a régua de autoria, no mesmo parágrafo que declara essa seção
como fonte da verdade, encontra o ponteiro para `docs/ARMADILHAS_DE_FERRAMENTA.md`. Confirmado hoje:

```
$ python -c "from pathlib import Path;print(Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8').count('ARMADILHAS_DE_FERRAMENTA'))"
1
```

**Protege contra:** uma régua que se declara fonte da verdade da autoria e não aponta, ela mesma,
para o recurso que deveria evitar o erro mais barato de se cometer de novo.

---

## Estrato 7 — A origem do número

### `FPU-T9` — A skill de fatos frescos

**Contexto que a motivou:** um relatório de janela já citou um total de consumo inflado por soma à
mão, e um handover já citou um hash copiado de um registro antigo em vez de medido na hora. Nenhuma
regra obrigava declarar de onde vinha um número antes de ele chegar ao dono.

**O que é o artefato:** a skill nova `.claude/skills/fatos-frescos/SKILL.md`, citada pela checagem
de mensagem ao dono (`.claude/skills/mensagem-ao-dono/SKILL.md`), pelo relatório de encerramento do
loop (`.claude/skills/scrum-master/SKILL.md`) e pela passagem de tarefas
(`.claude/skills/passagem-de-bastao/SKILL.md`).

**Como funciona na prática:** antes de escrever um despacho, um relatório, um encerramento, um
handover ou qualquer mensagem ao dono que leve número, caminho com linha, hash ou contagem, cada
valor é classificado numa de três origens — rodado neste turno, copiado de um arquivo e uma linha,
ou memória — e valor de origem memória não é enviado.

**Protege contra:** um número que chega ao dono sem que quem o escreveu saiba, no momento de
escrever, se ele foi medido ou só lembrado.

### `FPU-T9a` — A skill lê totais em instrumento de leitura, e se declara medida em prosa

**Contexto que a motivou:** a versão original da skill mandava rodar `encerrar.py plano` para
contar tarefas fechadas de uma janela — mas esse comando **fecha** o plano, exige o veredito do
dono e recusa um plano com tarefa aberta; rodá-lo no meio de uma janela para simplesmente contar
seria destrutivo. A skill também se descrevia como "a régua executável dessa medida", quando o
próprio modelo do plano diz que nenhuma conferência nova entra como frase de skill.

**O que é o artefato:** a reescrita da seção "Instrumentos por tipo de número" da skill, apontando
para leitura, não para escrita: tarefas fechadas na projeção do índice de
`docs/DIARIO_DE_OBRAS.md`, e consumo na série `docs/telemetria.tsv` — nunca nos comandos que
fecham um plano ou apensam uma linha.

**Como funciona na prática:** o exemplo da skill cita uma linha real da série de telemetria
(`docs/telemetria.tsv:894`, a linha da própria `FPU-T9`) em vez de um número solto; a skill se
declara "a medida em prosa" do princípio de origem declarada, e não uma conferência da régua
executável.

**Protege contra:** uma skill escrita para resolver esquecimento que ela mesma comete — mandar
rodar o comando errado (o que fecha, não o que lê) para obter um número que deveria só ser
consultado.

---

## Estrato 8 — A causa raiz da parada

### `FPU-T10` — A tabela de acionamentos ganha a coluna de causa raiz

**Contexto que a motivou:** cada vez que um executor parava e o consultor tria a parada, uma linha
era registrada em `docs/ACIONAMENTOS_CONSULTOR.tsv` — mas nenhum campo dizia qual das seis causas
da amostra original explicava aquela parada. A régua de causas ficava só na prosa do plano, sem
nenhum jeito de medir, ao longo do tempo, se a taxa de parada por premissa não sondada estava caindo.

**O que é o artefato:** a décima coluna `causa_raiz` do TSV, o vocabulário fechado de seis tokens
descrito no processo do consultor (`.claude/agents/pantonic-consultant.md`) e a subseção
`### 3.3 Vocabulário de causa raiz` de `GOVERNANCA.md`, que diz, para cada token, o que o detecta:
quatro deles têm uma conferência da régua executável (o literal da âncora, o aviso de número sem
comando, o arquivo de medida do executor, os achados roteados ao dossiê); os outros dois —
semântica de ferramenta suposta e contexto do dono presumido — não têm conferência automática, e o
que os pega é a lista de armadilhas e o checklist da mensagem ao dono, ambos fora da régua.

**Como funciona na prática:** todo acionamento novo do consultor recebe um dos seis tokens, ou `-`
quando nenhum dos seis explica a parada; as 62 linhas anteriores ao acréscimo da coluna receberam
`-` de propósito: classificar o passado é julgamento, fora do escopo desta tarefa.
Confirmado hoje:

```
$ python -c "import csv;from pathlib import Path;r=list(csv.reader(Path('docs/ACIONAMENTOS_CONSULTOR.tsv').open(encoding='utf-8',newline=''),delimiter='\t'));print(len(r[0]),r[0][-1],all(len(l)==len(r[0]) for l in r[1:]))"
10 causa_raiz True
```

**Protege contra:** medir a queda da taxa de "parada por crença" só de memória ou por relato — sem a
coluna, ninguém poderia responder, com número, se os mecanismos deste plano estão de fato reduzindo
as paradas que motivaram a amostra original.

---

## O que vale além deste plano

| regra | o que resolve | residência |
|---|---|---|
| Card vivo não se reescreve para caber num instrumento; o instrumento aprende a forma do corpus | instrumento que engessa a prática em vez de medi-la | contrato do objeto "card" no modelo de `docs/plans/P-0752-fato-no-ponto-de-uso.md` §1 |
| Todo aviso automático sobre número sem comando é aviso, nunca bloqueio | falso positivo travando a autoria de um plano | `.claude/tools/crenca_hook.py` |
| A recusa de linha duplicada mora no escritor da série, não em quem chama | uma rodada de trabalho contada duas vezes no consumo | `.claude/tools/telemetria.py`, função `checar_repetida` |
| Toda conferência nova entra como código que falha ruidosamente, nunca como frase de skill | regra escrita e não aplicada | `GOVERNANCA.md` §3, contrato do objeto "régua executável" |
| Armadilha de ferramenta medida ganha residência única; quem mede uma nova apensa uma linha | a mesma armadilha reaprendida por agentes diferentes | `docs/ARMADILHAS_DE_FERRAMENTA.md` |
| Toda mensagem ao dono declara a origem de cada número; memória não é origem admitida | número inflado por soma à mão, ou copiado de um registro antigo | skill `fatos-frescos` |
| Toda parada triada pelo consultor recebe uma classe de causa do vocabulário fechado | parada registrada sem se saber que classe de erro a originou | `GOVERNANCA.md` §3.3 |

---

## Os ganhos, medidos

| medida | antes | depois |
|---|---|---|
| conferências vivas no ponto de despacho (régua executável) | 0 (a única existente, o gate do card, estava suspensa desde 2026-09-19) | 6: forma do card, âncora com literal, número gravado sem comando, medida do executor, precedente roteado no dossiê, duplicata na telemetria |
| suíte de testes do hub | `397 passed` (2026-09-26) | `452 passed in 36.45s` (2026-09-27, medido) |
| itens de Verificação do corpus vivo que o gate lia sem "fora da forma" | 0 dos 67 itens inline de um plano anterior | 67 lidos; sobre o mesmo plano, o gate agora sai com exatamente duas falhas nomeadas, não quatro genéricas |
| colunas de `docs/ACIONAMENTOS_CONSULTOR.tsv` | 9 | 10 (`causa_raiz`); 62 linhas de dados, todas ainda `-` (medido hoje — ver pendências) |
| skills do kit citadas em `README.md` | doze | treze (`fatos-frescos`) |
| linha de consumo repetida na mesma rodada, aceita pela série de telemetria | até duas (gancho e fechamento, sem conferir um o outro) | recusada no escritor, exit `3`, medida contra TSV temporário |
| linhas na tabela de armadilhas de ferramenta | 0 | 9 (8 na autoria, 1 apensada depois, exercitando a própria regra) |

---

## O padrão que a execução revelou

Cinco das dezessete tarefas pararam, antes de qualquer despacho, pela mesma causa que a amostra
original apontou como a maior: uma premissa sobre o código ou sobre o comportamento de outro teste,
afirmada na autoria do card sem sondar a árvore real. As cinco paradas aconteceram nas primeiras
três tarefas do plano (`FPU-T1`, três vezes; `FPU-T3`; `FPU-T5`), todas antes de o gate do card
existir — a primeira metade do próprio mecanismo que o plano constrói.

Depois do despacho, um segundo padrão apareceu: seis tarefas foram aceitas fielmente ao que o card
pedia, e o laudo de revisão encontrou, mesmo assim, uma lacuna de alcance que só aparecia ao
exercitar a entrega contra o resto do plano — não um erro de quem executou. Cada lacuna dessas
virou uma tarefa nova e pequena (`FPU-T1a`, `FPU-T4a`, `FPU-T5b`, `FPU-T5c`, `FPU-T8a`, `FPU-T9a`),
nunca a reabertura do card já fechado.

### Defeitos da execução, com estado

| # | defeito | estado | o que fecha |
|---|---|---|---|
| 1 | as cinco paradas por premissa não sondada na autoria (acima) | 🟡 cada caso reparado no próprio card antes do despacho; o gate que a `FPU-T1`/`FPU-T2` constroem confere a forma e a âncora de um card, não se uma premissa de código foi sondada | nenhum instrumento cobre a classe hoje |
| 2 | item fantasma de prosa `N.` na continuação do próprio item de Verificação | 🟢 fechado com guarda: teste `test_tf_prosa_na_continuacao_do_item_nao_vira_item` (`FPU-T1a`) | — |
| 3 | medida do executor guardava a cabeça da saída, perdendo o sumário de comandos como `pytest` | 🟢 fechado com guarda: `FPU-T5b`, com teste que confere a cauda gravada |
| 4 | contagem de números sem comando inflada por casamento duplo de padrão | 🟢 fechado com guarda: `FPU-T4a`, com teste que confere a contagem por grupo |
| 5 | `review_evidence.py` não lia a forma de âncora com literal em `Arquivos-alvo`, listando alvo tocado como "fora dos alvos" | 🟢 fechado com guarda: tíquete `TK-89` (dois cards, ambos `done`) |
| 6 | caminho fixo de medida do executor incompatível com plano em pasta | 🟢 fechado com guarda: `FPU-T5c`, caminho agora derivado do mesmo cálculo do revisor |
| 7 | a coluna `causa_raiz` existe, mas nenhuma linha gravada até hoje — incluindo as do próprio `P-0752` — foi classificada | 🔴 regra escrita (vocabulário fechado, campo no processo do consultor), aplicação ainda não observada em nenhuma linha real | próximo acionamento do consultor que preencher a coluna |

---

## Pendências abertas ao fim do plano

| # | pendência | por que ficou aberta | o que a fecha | bloqueia algo? |
|---|---|---|---|---|
| 1 | `AE-50`: a evidência de revisão não carrega o conteúdo de arquivo não rastreado no momento do despacho (a referência de captura vem de `git stash create`, que ignora o não rastreado); o trecho de `encerrar.py`/`test_encerrar.py` tocado pela `FPU-T7` saiu inteiro no dossiê de evidência, sem diff | achado no fechamento da `FPU-T7`; a rota que o plano deu a ele foi "auditoria final", não um card deste plano | a auditoria final do repositório, ou a extensão do mecanismo que a `TK-93` já aplicou a um caso parecido (captura de referência com não rastreados) | não; a evidência foi reconciliada à mão nesta janela |
| 2 | `AE-51`: `docs/ACIONAMENTOS_CONSULTOR.tsv` está fora do controle de versão — a mesma causa do `AE-50` faz a evidência colar o arquivo inteiro sem uma base de comparação, e a regra "não mudar nenhum outro campo" da `FPU-T10` só pôde ser conferida por estrutura (contagem de colunas), não por diff de conteúdo | idem | idem | não; conferida por estrutura nesta janela |
| 3 | nenhuma linha de `docs/ACIONAMENTOS_CONSULTOR.tsv`, incluindo as 13 do próprio `P-0752`, tem a coluna `causa_raiz` preenchida com um dos seis tokens — todas as 62 linhas de dados estão em `-` | a `FPU-T10` entregou o campo e o vocabulário, não a classificação retroativa (decisão do plano: classificar o passado é julgamento) | o próximo acionamento do consultor, em qualquer plano, preencher a coluna | não; é a própria medida que dirá se a taxa de parada por crença está caindo |
| 4 | nenhum arquivo tocado por esta entrega tem commit | a entrega de código de um plano não commita por si; o commit é ato separado, depois do veredito | decisão de comitar, depois do veredito deste documento | não; confirmado por `git status --short`: os 17 RDOs, os 17 laudos, o plano e todo o código listado nas seções acima aparecem como modificados ou não rastreados |
| 5 | o gate do card, comparado no mundo "depois" de um card fechado há dias, diverge à medida que a suíte cresce depois do fechamento (medido sobre a própria `FPU-T1`: declarado `73 passed`, hoje `89 passed`) | "depois" é uma fotografia do dia do fechamento, e a suíte não parou de crescer | nenhum: é a mesma classe de número que envelhece que o plano nomeia como causa 1 da amostra original, agora visível sobre o próprio plano | não; o revisor já re-mede o "depois" no fechamento, e não há releitura automática depois dele |

**Estado honesto.** O plano entregou as 17 tarefas — 11 delas aprovadas sem ressalva e 2 aprovadas
com ressalva (`FPU-T2`, 88%; `FPU-T9`, 88%), ambas com o achado da ressalva absorvido por um card
corretivo próprio do mesmo plano. A suíte do hub sai `452 passed` e `backlog.py check` sai
`check: OK`. Ficaram 5 pendências: duas são achados que o próprio plano roteou para uma auditoria
futura fora do seu escopo (`AE-50`, `AE-51`); uma é a própria medida que o plano criou, ainda sem
nenhuma linha classificada; uma é o fato de que nada desta entrega foi commitado; e a última é uma
demonstração, não um defeito — o mecanismo do plano envelhecendo perante o próprio plano, do mesmo
jeito que ele previu que aconteceria com qualquer card.
