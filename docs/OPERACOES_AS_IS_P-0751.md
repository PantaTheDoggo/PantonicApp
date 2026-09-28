# Operações as-is — `P-0751`, "Esgotar o backlog antes da publicação do kit"

Documento de validação do plano `docs/plans/P-0751-esgotar-backlog.md`. Descreve o estado das
operações que o plano deixou em 2026-09-26, com exemplos de saídas reais rodadas nessa data.

---

## Por que o plano existiu

**O problema.** Em 2026-09-25, o diário de obras (`docs/DIARIO_DE_OBRAS.md`, o kanban do projeto)
tinha **14 cards de tíquete prontos** (`ready`) e nenhum plano vivo. Os cards vinham de seis
tíquetes (`TK-55`, `TK-67`, `TK-70`, `TK-72`, `TK-73` e `TK-83`) e cobriam três tipos de dívida:
instrumentos que só acusavam defeito no fechamento da tarefa, doutrina que a execução já tinha
corrigido na prática e não no texto, e uma rodada de revisão das regras de guarda pendente desde
2026-08-08. A publicação do kit nos projetos derivados (tíquete `TK-81a`) esperava o backlog zerar.

**A solução, em uma frase.** Os 14 cards viraram um plano só, com uma operação por card, fechado
num único loop de execução: 14 cards prontos no início, zero no fim.

**Vocabulário mínimo.**

| termo | o que é |
|---|---|
| card | a unidade de trabalho escrita para um executor: objetivo, arquivos-alvo, verificação com números, "pronto quando" |
| tíquete | seção `## TK-<n>` do diário; guarda um problema e os cards que o resolvem (`### TK-<n><letra>`) |
| `backlog.py check` | comando que confere a gramática do diário e dos planos e imprime uma violação por linha, com código `C-<n>` |
| RDO | registro de fechamento de tarefa, escrito por `rdo.py close` em `docs/RDO/` |
| `kit_check` | script `.claude/checks/kit_check.ps1`, que valida o kit (`-Mode validate`) e acusa divergência entre o versionado e o gerado (`-Mode check-drift`) |
| fixture | cópia mínima de diário ou de kit sob `tests/fixtures/`, usada só por teste |
| consultor | o agente `pantonic-consultant`, que faz a triagem de toda parada de executor durante o loop e devolve a rota |
| piso do `C-11` | lista de citações quebradas já conhecidas neste repositório, que o `check` tolera sem acusar |

---

## O arco — quatro estratos

| estrato | pergunta que responde | tarefas |
|---|---|---|
| 1. Instrumentos do backlog | o defeito de um card aparece **antes** de alguém tentar fechá-lo? | `EBK-T1`, `EBK-T2`, `EBK-T3`, `EBK-T4`, `EBK-T5`, `EBK-T5a`, `EBK-T6` |
| 2. Doutrina | o texto das regras diz o que a execução já aprendeu? | `EBK-T7`, `EBK-T8`, `EBK-T9`, `EBK-T10`, `EBK-T11`, `EBK-T12` |
| 3. Medida | a regra de custo sobre retomar o planejador tem número por trás? | `EBK-T13`, `EBK-T13a` |
| 4. Revisão das guardas | as regras de guarda em vigor ainda mudam comportamento? | `EBK-T14` |

O estrato 2 escreve regras que os instrumentos do estrato 1 passam a conferir; por exemplo, o
`C-15` e o `C-16` dão corpo à doutrina "Tíquete nasce executável". O estrato 4 vem por último
porque julga a doutrina já ajustada.

O plano nasceu com 14 cards e fechou com 16. Os dois cards a mais são **corretivos da mesma
operação**, escritos pelo consultor quando a revisão achou falta na entrega: `EBK-T5a` completa a
`EBK-T5`, e `EBK-T13a` corrige a justificativa da `EBK-T13`. Nenhuma tarefa foi cancelada.

---

## Estrato 1 — Instrumentos do backlog

## `EBK-T1` — O `check` acusa tíquete aberto sem card

**Contexto que a motivou:** a doutrina "Tíquete nasce executável" exige que todo tíquete aberto
tenha ao menos um card, mas nada conferia isso. Um tíquete sem card só era notado quando alguém
procurava o que executar.

**O que é o artefato:** a violação `C-15` na função `check` de `.claude/tools/backlog.py`, e a
menção a ela na skill `diario-de-obras`. Os testes estão em `tests/test_backlog.py`.

**Como funciona na prática:**
1. **O que dispara:** `python .claude/tools/backlog.py check`, rodado por qualquer pessoa ou agente.
2. **A entrada:** cada seção `## TK-<n>` do diário cujo status não é `done`, `cancelled` nem
   `superseded`.
3. **O processamento:** procura ao menos uma subtarefa `### TK-<n><letra>` nessa seção.
4. **A saída:** uma linha por tíquete vivo sem subtarefa. Numa cópia da fixture `verde`, sem a
   subtarefa `TK-1a` (2026-09-26):

   ```
   C-15 docs/DIARIO_DE_OBRAS.md:11 — TK-1 vivo sem subtarefa
   ```

**Protege contra:** um tíquete aberto que nenhum loop consegue executar porque não tem card.

## `EBK-T2` — O `check` recusa o card que o fechamento não consegue ler

**Contexto que a motivou:** seis cards de tíquete sem `Arquivos-alvo`, `Verificação` e `Pronto
quando` passaram pelo `check` e só falharam em `rdo.py close`, no fim da tarefa. O `TK-68a` passou
pelo `check` e foi recusado pelo gerador de evidência porque uma linha `### ` na coluna 0, dentro
do texto citado, encerrava o card antes da hora.

**O que é o artefato:** duas violações novas em `check` (`.claude/tools/backlog.py`), ligadas por
dois parâmetros que só o subcomando de linha de comando ativa:
- `C-16`: todo card vivo (`ready`, `in-progress` ou `review`) passa pela **mesma leitura** que o
  `rdo.py close` usa (`extrair_dossie` em `.claude/tools/rdo.py`). Se essa leitura recusa o card, a
  mensagem dela vira a violação. A gramática não foi reescrita no `backlog.py`.
- `C-17`: toda entrada do piso do `C-11` que não corresponde a nenhuma citação quebrada existente
  é acusada como órfã. Na execução, a entrada órfã `('GOVERNANCA.md', '3.2')` saiu do piso.

**Como funciona na prática:** o gatilho é o mesmo `backlog.py check`. Numa cópia intacta da fixture
`verde`, cujos cards não têm campos (2026-09-26):

```
C-16 docs/DIARIO_DE_OBRAS.md:14 — campo obrigatório ausente em 'TK-1a': 'objetivo'
```

Na árvore do hub, a saída é `check: OK — nenhuma violação.`: 21 cards vivos lidos e nenhum
recusado, conforme a medida do consultor na execução.

**Protege contra:** card que parece pronto no kanban e quebra só no fechamento, depois de o
executor ter gasto a tarefa inteira.

**Limite conhecido:** o piso do `C-11` mora numa constante do código, e o subcomando a aplica a
**qualquer** repositório passado em `--repo`. Numa cópia da fixture `verde`, a mesma rodada acusou
`C-17 GOVERNANCA.md:1 — piso_c11 nomeia entrada órfã: ...`. A correção está no tíquete `TK-86`
(pendência 3, abaixo).

## `EBK-T3` — A escolha da próxima tarefa mostra o cabeçalho inteiro do card

**Contexto que a motivou:** `backlog.py next` imprimia só `[<modelo> · classe <classe>]` e perdia o
esforço declarado e a marca ` + dono`, que indica tarefa não delegável. O `TK-58a` perdeu essa
marca em 2026-09-20.

**O que é o artefato:** a montagem da primeira linha em `backlog.py next` (`.claude/tools/backlog.py`),
que agora copia o colchete do cabeçalho tal como está no plano.

**Como funciona na prática:** quem conduz o loop roda `python .claude/tools/backlog.py next`. A
primeira linha real da última tarefa deste plano (2026-09-26):

```
=== PRÓXIMA TAREFA: EBK-T14 — A rodada de revisão de guardrails pendente desde 2026-08-08 [Opus · esforço high · classe investigacao]
```

Antes do card, a mesma linha sairia `[Opus · classe investigacao]`.

**Protege contra:** despachar uma tarefa com esforço errado, ou delegar uma tarefa que o dono
reservou para si.

## `EBK-T4` — O fechamento recusa tarefa que não está concluída

**Contexto que a motivou:** em 2026-09-20, `rdo.py close` escreveu RDO para uma tarefa
`in-progress`, um comando depois de o `backlog.py status` ter recusado a transição para `done`. O
próprio módulo declarava que não lia status de lugar nenhum.

**O que é o artefato:** a checagem de status em `cmd_close` (`.claude/tools/rdo.py`). O status vem
da mesma fonte que o `backlog.py status` escreve: o bullet `- **Status:**` no plano legado e no
diário, ou a linha da tarefa em `estado.tsv` no plano em pasta. Status ausente conta como "não
concluído" (decisão `DEB-8` do plano).

**Como funciona na prática:** quem fecha a tarefa roda `rdo.py close`. Numa cópia do plano com a
`EBK-T6` em `in-progress` (2026-09-26):

```
rdo: FALHOU - status: tarefa 'EBK-T6' está 'in-progress', exigido 'done'
```

A saída é exit 1, e nenhum arquivo é escrito.

**Protege contra:** RDO de tarefa que não terminou, que faria o registro dizer "fechado" sobre algo
aberto.

## `EBK-T5` e `EBK-T5a` — A conferência do kit conta defeitos, não linhas

**Contexto que a motivou:** uma única frase alterada no `.claude/README.md` gerado produzia três
itens contados como problemas: o aviso e as duas linhas de detalhe. Além disso, cada ramo que chama
o `materializar.py` contava a linha de resumo dele como mais um problema. Na medida da execução, o
cabeçalho dizia 13 problemas para 12 defeitos no `check-drift`, e 2 para 1 no `validate`.

**O que é o artefato:** a contagem de `.claude/checks/kit_check.ps1`, nos modos `validate` e
`check-drift`. Duas tarefas fizeram a mudança:
- `EBK-T5`: a divergência de README conta 1, e as linhas de detalhe saem da contagem.
- `EBK-T5a`: a linha de resumo `materializar: FALHOU - ...` sai da lista, e o detalhe passa a ser
  impresso logo abaixo do seu problema, recuado quatro espaços e sem o marcador `- `.

Os testes estão em `tests/test_kit_check.py` (4 testes).

**Como funciona na prática:** o check roda nos testes e à mão, com
`pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift`. Numa cópia do kit com uma
frase a mais no README (2026-09-26):

```
kit_check: check-drift FALHOU (13 problema(s)):
  - README.md diverge do regenerado (2 linha(s) diferente(s)):
    [regenerado] | `pantonic-scout` | Haiku | ... preservam o contexto dos agentes de planejamento e execução. |
    [versionado] | `pantonic-scout` | Haiku | ... preservam o contexto dos agentes de planejamento e execução. Frase extra. |
```

São 13 itens `  - ` para 13 defeitos: o do README e 12 de materialização, porque a cópia aponta o
repositório de origem. A linha de resumo do `materializar.py` não aparece. Na árvore, os dois modos
saem com exit 0.

**Protege contra:** um número de problemas que não se reconcilia com os defeitos, o que leva quem
lê a procurar defeitos que não existem.

## `EBK-T6` — Nenhuma fixture carrega nome que o harness descobre

**Contexto que a motivou:** em 2026-09-20, uma fixture continha um arquivo `SKILL.md`, e o harness
passou a listá-la como skill real, invocável.

**O que é o artefato:** `tests/test_fixtures_higiene.py`, com a função pura `nomes_de_descoberta`.
O teste falha, nomeando o arquivo, quando existe sob `tests/fixtures/` um `SKILL.md`, `CLAUDE.md`,
`AGENTS.md`, `settings.json` ou `settings.local.json`.

**Como funciona na prática:** o teste roda com a suíte (`python -m pytest -q`). Hoje há zero
arquivos com esses nomes. Junto com os testes do `kit_check`: `7 passed in 4.00s` (2026-09-26).

**Protege contra:** uma fixture de teste que vira, sem ninguém perceber, skill ou configuração ativa
da sessão.

---

## Estrato 2 — Doutrina

As seis tarefas deste estrato editam texto normativo. O artefato é o texto, e a prova é a contagem
do literal novo no arquivo. Todas as contagens abaixo foram re-medidas em 2026-09-26 e dão `1`.

## `EBK-T7` — O teste que discrimina e a medida publicada

**Contexto que a motivou:** vários testes passaram pelo motivo errado. Exemplos: asserção sobre um
tamanho medido, em vez de uma relação; teste rodado sobre o diário vivo; fixture com nome de
descoberta. E vários números foram publicados sem dizer o que mediam.

**O que é o artefato:** duas regras em `GOVERNANCA.md`:
- o parágrafo **Teste que discrimina.**, com quatro regras, em §4.4 (linha 699);
- as regras (f), (g) e (h) da *Disciplina de instrumento*, em §3, que passou de cinco para oito
  regras (linhas 220 e 235).

**Como funciona na prática:** é regra de conduta. Quem escreve um teste ou publica uma medida a
aplica, e o revisor a cobra. Exemplo do texto: *"Asserção afirma relação, nunca magnitude."*

**Protege contra:** teste verde que ficaria verde mesmo sem o que ele deveria proteger, e número
publicado que ninguém consegue reconciliar.

## `EBK-T8` — Quando o modelo vale, e o que acontece com a versão recusada

**Contexto que a motivou:** o rascunho do modelo de um plano carregava `situação: vigente` por
forma, e o texto não dizia se isso o tornava obrigatório. Também não dizia o que fazer com o que
fora entregue sob uma versão depois recusada.

**O que é o artefato:** três trechos:
- `GOVERNANCA.md` §3.2, linha 466: *"o modelo só vigora depois de validado pelo dono"*;
- `GOVERNANCA.md` §3.2, linha 418: recusada a versão pendente, o plano *"retroage ao ponto do
  drift"*, e o que foi entregue sob ela é refeito por card corretivo;
- `README.md` §8.1, linha 685: todo elemento do modelo tem **lastro** num trecho do pedido.

**Como funciona na prática:** é regra de conduta para quem modela e para quem conduz o marco do
plano.

**Protege contra:** tratar rascunho como contrato, e deixar entregue, sem refazer, trabalho feito
sob uma versão recusada.

## `EBK-T9` — Uma operação, uma oração

**Contexto que a motivou:** houve operações do modelo escritas com duas orações, cada uma com o seu
verbo. Elas geravam um card que cobria dois assuntos.

**O que é o artefato:** o parágrafo **Uma operação, uma oração.** em `GOVERNANCA.md` §3.2
(linha 347), e a frase correspondente na skill `diario-de-obras` (linha 252).

**Como funciona na prática:** a guarda é o Marco 1, em que o dono lê operação por operação. Nenhum
validador apanha o caso, porque a conjunção também aparece dentro de uma oração só.

**Protege contra:** operação mal recortada, que vira card de dois temas.

## `EBK-T10` — A régua de autoria do card, segunda leva

**Contexto que a motivou:** as janelas de execução de 2026-09-20 a 2026-09-25 mediram dez defeitos
de autoria de card. Exemplos: literal com `## ` na coluna 0 encerrando o card, contagem de palavra
solta aprovando menção decorativa, valor de aceite viajando na linha de retorno.

**O que é o artefato:**
- o item 13 da Fase 4 de `.claude/agents/pantonic-planner.md` (linha 380), com os critérios (i) a (x);
- a frase em `.claude/agents/pantonic-consultant.md` (linha 28) que manda o consultor aplicar os
  itens 11 a 13 a todo card que escreve;
- a limitação do contrato copiado no card, em `GOVERNANCA.md` §3.2 (linha 430).

**Como funciona na prática:** o planejador aplica a régua antes de gravar o plano, e o consultor a
aplica ao escrever um card corretivo.

**Protege contra:** as dez classes de defeito de card já medidas.

## `EBK-T11` — O planejador confere a superfície e ensaia os cards antes de gravar

**Contexto que a motivou:** listas de "onde isto aparece" chegavam ao plano sem o padrão de busca
que as produziu, e cards eram publicados sem que a verificação deles tivesse rodado alguma vez.

**O que é o artefato:** dois trechos de `.claude/agents/pantonic-planner.md`:
- linha 16: o `Bash` do planejador passa a servir a **dois** usos. O segundo é re-rodar o grep que
  produziu uma lista de residências, publicada com padrão e contagem.
- linha 411: o item 14 da Fase 4, **Ensaio dos cards em árvore temporária**.

**Como funciona na prática:** antes de gravar o plano, o planejador aplica os cards em sequência
numa cópia da árvore e roda cada verificação antes e depois de cada card. Uma verificação que dá o
mesmo valor antes e depois não discrimina e volta à autoria.

**Protege contra:** card cuja verificação ou contingência nunca foi exercitada. É exatamente a
classe das cinco paradas deste plano (ver "O padrão que a execução revelou").

## `EBK-T12` — Três ajustes de regra existente

**Contexto que a motivou:** três casos medidos no `P-0747`:
- o modelador recopiava a seção inteira do modelo no retorno;
- o lastro não previa enunciado composto por vários atos do dono;
- o aviso do hook de modelo mandava parar quem estava em Fable.

**O que é o artefato:**
- `.claude/agents/pantonic-model-designer.md`: o ato devolve ponteiro, linha de versão, saída do
  `check` e o campo `Achados fora da seção:` (linha 120). Não recopia a seção.
- `GOVERNANCA.md` §3 e §3.2: a matriz e a tabela de papéis dizem o mesmo, e o lastro aceita
  enunciado composto (linha 355).
- `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`: o aviso da fase intelectual.
- `tests/test_materializar.py`: o teste do hook deixou de afirmar o tamanho do aviso (470 bytes) e
  passou a afirmar a fase classificada.

**Como funciona na prática:** o hook roda a cada prompt do dono, por evento `UserPromptSubmit` do
harness. Depois do fechamento, o condutor copiou o hook para o ponto de carga com
`materializar.py apply --alvo usuario`, e o `drift` seguinte respondeu `materializar: OK - sem
drift.` O aviso real injetado nesta sessão depois da cópia:

```
Gate modelo-por-fase: este prompt e trabalho intelectual (Regra 7). Se o modelo ativo for Sonnet ou
Haiku, PARE e peca ao dono `/model opus` antes de prosseguir (anuncie a troca — Regra 5). Em Opus ou
Fable, ignore: o modelo da sessao e escolha do dono.
```

**Protege contra:**
- retorno do modelador que custa uma seção inteira de contexto;
- pedido de troca de modelo a quem já está num modelo acima do exigido;
- teste que quebra a cada ajuste de redação.

---

## Estrato 3 — Medida

## `EBK-T13` e `EBK-T13a` — Retomar o planejador por mensagem ou abrir um novo

**Contexto que a motivou:** numa rodada de replanejamento, o condutor pode fazer duas coisas:
retomar o planejador que já trabalhou no plano, mandando-lhe uma mensagem, ou abrir uma instância
nova ("fria"). Não havia medida de qual das duas custa menos.

**O que é o artefato:**
- a seção `## 17` de `docs/CUSTO_DO_PICKUP.md`, com a medida;
- a regra **"Rodada de replanejamento abre instância fria do planejador"**, em `GOVERNANCA.md` §3
  (linha 133).

**Como funciona na prática:**
1. **Corpus:** as duas instâncias do planejador que trabalharam no `P-0747`. A medida lê só chaves,
   contagens e datas dos transcripts, nunca o texto das mensagens.
2. **Segmento:** um trecho de trabalho do agente. Abre na invocação e em cada mensagem de retomada,
   que se reconhece pela chave `origin.kind == "coordinator"`. Resultado: 2 invocações frias e 6
   retomadas.
3. **Primeira comparação (`EBK-T13`):** média por segmento. Retomadas: $5,19. Frias: $0,65.
4. **Correção (`EBK-T13a`):** a revisão apontou que a média por segmento soma o trabalho da rodada
   (3 mensagens nas frias; de 5 a 74 nas retomadas). O que difere entre as opções é o **custo de
   partida**: a retomada relê, a cada mensagem, o contexto que carregou das rodadas anteriores; a
   instância fria recria a base e redescobre o que precisa.

| comparação | retomadas | fria |
|---|---|---|
| soma da partida, nas 6 rodadas | $6,30 | de $1,16 a $3,80 (o teto supõe recriar todo o contexto carregado) |
| rodadas curtas (5 e 7 mensagens) | vence a retomada | — |
| rodadas longas (14, 43 e 74 mensagens) | — | vence a fria |
| 1 rodada (9 mensagens) | indeterminada | indeterminada |

**Protege contra:** retomar por hábito um agente cujo contexto acumulado custa mais do que começar
de novo. Também contra justificar uma regra com uma média que compara volumes de trabalho
diferentes.

**Limite declarado:** o corpus tem 2 agentes de um só plano, e a redescoberta que a instância fria
faria não é medida: só se mediria lendo o conteúdo das mensagens.

---

## Estrato 4 — Revisão das guardas

## `EBK-T14` — A rodada de revisão das regras de guarda

**Contexto que a motivou:** o procedimento de §7.1 do `GOVERNANCA.md` manda revisar as regras de
guarda sempre que um plano fecha. A última rodada registrada era de 2026-08-08 (`P-0731`), e
catorze planos tinham fechado depois dela.

**O que é o artefato:** a entrada `P-0750 — 2026-09-26` no *Registro das rodadas*, em `GOVERNANCA.md`
§7.1 (linha 1179).

**Como funciona na prática:**
1. **Escopo:** 13 das 20 regras de guarda. As 7 mais novas ficam fora por idade.
2. **Seis isentas**, porque têm check executável. O check foi rodado de novo nesta data, e a
   isenção não foi herdada: os quatro testes de conformance do `PantonicVideo` (`17 passed in
   9.62s`), a suíte do hub (`376 passed in 36.57s`) e as 6 entradas de `permissions.deny`.
3. **Sete na pergunta** *"esta regra mudou algum comportamento desde a rodada anterior? Cite o
   caso."* Todas com caso registrado. Exemplo: **G-EXECREADY** → `LM-T1` do `P-0740`, devolvida
   `blocked` sem tocar arquivo.
4. **Resultado:** zero regras marcadas `OBSOLETA`.

**Protege contra:** regra de guarda que continua no texto sem mudar nenhum comportamento.

---

## O que vale além deste plano

| regra | o que resolve | residência |
|---|---|---|
| Teste que discrimina | teste verde pelo motivo errado | `GOVERNANCA.md` §4.4 |
| Medida publicada nomeia objeto, regra de enumeração e dispersão | número que não se reconcilia | `GOVERNANCA.md` §3, *Disciplina de instrumento* (f)–(h) |
| O modelo só vigora depois de validado; o drift recusado retroage | rascunho tratado como contrato | `GOVERNANCA.md` §3.2 |
| Uma operação, uma oração | card de dois temas | `GOVERNANCA.md` §3.2; skill `diario-de-obras` |
| Régua de autoria, segunda leva; ensaio dos cards em árvore temporária | card com defeito de autoria já medido | `.claude/agents/pantonic-planner.md`, Fase 4, itens 13 e 14 |
| Rodada de replanejamento abre instância fria do planejador | retomada mais cara que recomeçar | `GOVERNANCA.md` §3 |

---

## Os ganhos, medidos

| medida | antes | depois |
|---|---|---|
| cards prontos no backlog do plano | 14 (2026-09-25) | 0 (2026-09-26) |
| testes da suíte do hub | `360 passed` (2026-09-25) | `376 passed in 36.58s` (2026-09-26) |
| códigos de violação do `backlog.py check` | `C-1..C-14` | `C-1..C-17` |
| problemas contados para 1 divergência de README com 2 linhas diferentes | 3 | 1 |
| linha de resumo do `materializar.py` contada como problema | sim, em `validate` e em `check-drift` | não |
| arquivos com nome de descoberta sob `tests/fixtures/` | 0, sem teste | 0, com teste |

Consumo do loop, lido de `docs/telemetria.tsv` (46 linhas desta janela): executores 1 771,3 mil
tokens, revisores 1 362,2 mil, consultor 663,8 mil. Total: 3 797,3 mil tokens.

---

## O padrão que a execução revelou

Cinco das dezesseis tarefas pararam na primeira tentativa. Nas cinco, o executor devolveu `blocked`
com motivo `premissa`, e a causa foi a mesma: **o card previa uma contingência ou um método sem ter
medido de onde vinha a entrada do teste**.

| tarefa | o que o card não mediu |
|---|---|
| `EBK-T1` | a fixture `vermelho` tem um status fora do vocabulário de propósito, e a subtarefa que o card mandava criar duplicaria uma violação que o teste conta |
| `EBK-T2` | as fixtures não trazem citação nenhuma: ligar o `C-17` para todo repositório acusaria cada entrada do piso |
| `EBK-T4` | os testes de `close` leem um plano histórico sem nenhuma linha de status |
| `EBK-T12` | um teste fixava o tamanho em bytes do aviso cujo texto o card mudava |
| `EBK-T13` | os transcripts têm entradas internas com a mesma marca das retomadas; só a chave `origin` as separa |

Em todas, o executor parou em vez de decidir. O consultor mediu, reparou o card e o redespachou, e a
segunda tentativa passou.

### Defeitos da execução, com estado

| # | defeito | estado | o que fecha |
|---|---|---|---|
| 1 | as cinco paradas acima | 🟡 cada caso reparado no próprio card; a regra que impede a classe (ensaio dos cards, `EBK-T11`) está escrita, mas nenhum plano foi autorado sob ela ainda | primeira autoria de plano sob o item 14 |
| 2 | a `EBK-T5` prometeu dois modos e só prescreveu um | 🟢 fechado com guarda: os 4 testes de `tests/test_kit_check.py` | — |
| 3 | a regra da `EBK-T13` justificada por média sem normalizar | 🟡 caso fechado pela `EBK-T13a`; nada impede outra comparação de volumes diferentes | pendência 7 |
| 4 | as lições de autoria anotadas pelo consultor em `## 8. Achados da execução` (por exemplo, "contingência que copia valor de fixture confere se a fixture o carrega de propósito") | 🔴 regra escrita no plano, fora da régua do planejador | pendência 7 |
| 5 | a linha de telemetria gravada pelo hook divergiu do consumo medido (durações 0,2 a 0,5 s menores; na `EBK-T4`, também 1 ferramenta e 0,9 mil tokens) | 🟡 corrigida à mão pelo condutor, linha a linha; o hook segue gravando o valor do evento dele | — |

---

## Pendências abertas ao fim do plano

| # | pendência | por que ficou aberta | o que a fecha | bloqueia algo? |
|---|---|---|---|---|
| 1 | `TK-84a`: `review_evidence.py --desde` lista como "sem atribuição" os arquivos não rastreados anteriores ao despacho (19 na `EBK-T5`) | achado de revisão; a regra `I-2` proíbe card novo neste plano | executar o card `TK-84a`, pronto no diário | não; todo laudo desta janela reconciliou à mão |
| 2 | `TK-85a`: o `rdo.py laudo` não tem campo para o motivo de dimensão fora de `conforme`, e recusa a grafia `dossiê` | idem | executar o card `TK-85a`, pronto | não |
| 3 | `TK-86a`: o piso do `C-11` mora no código, e o `check` acusa `C-17` em qualquer outro repositório | achado ao montar este documento | executar o card `TK-86a`, pronto: o piso passa a ser lido de `docs/PISO_C11.tsv` do repositório checado | **sim, fora do projeto:** sem ele, o `check` dos kits derivados nasce vermelho. Precisa fechar antes da publicação (`TK-81a`) |
| 4 | `TK-87a`: o dossiê do último card de um plano leva as seções seguintes (`## 6`..`## 8`) | idem | executar o card `TK-87a`, pronto | não; o despacho desta janela recortou à mão |
| 5 | `TK-81a`: publicação do kit nos derivados | fora de escopo, à espera de decisão do dono | decisão do dono, depois do `TK-86a` | é a própria publicação |
| 6 | o consultor aplica os itens 11 a 13 da régua, mas não o item 14 (ensaio), que a `EBK-T11` criou depois | a `EBK-T10` escreveu "11 a 13" antes de o item 14 existir | uma linha em `.claude/agents/pantonic-consultant.md` | não |
| 7 | as lições de autoria de `AE-1`, `AE-2` e `AE-5` (em `## 8` do plano) não estão na Fase 4 do planejador | ficaram registradas como insumo, sem card | um card que as leve à régua | não |
| 8 | o `C-16` também julgará os cards dos kits derivados | deixado de propósito pelo consultor: o `rdo.py close` do kit recusaria lá o mesmo card | nada, se o comportamento for o desejado | não |

**Estado honesto.** O plano entregou os 14 cards de origem mais os 2 corretivos, 16 de 16, com
suíte `376 passed` e `check` OK. Ficaram 8 pendências. Quatro são tíquetes com card pronto no
diário (`TK-84a` a `TK-87a`), nascidos da própria execução. Uma tem efeito fora do projeto: o
`TK-86a` precisa fechar antes da publicação do kit. O registro da execução mora em `## 8. Achados
da execução` do plano, nos RDOs `docs/RDO/P-0751-*.md` e no cenário
`docs/plans/_CENARIO-P-0751.md`.
