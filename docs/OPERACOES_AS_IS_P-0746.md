# Operações as-is — o lastro do modelo (`P-0746`)

Documento de validação do plano `docs/plans/P-0746-lastro-do-modelo.md`. Descreve o estado
corrente das regras que o plano deixou e do instrumento que as confere; o registro da execução
mora na `## 9. Achados da execução` do plano e nos RDOs em `docs/RDO/`.

---

## Por que o plano existiu

**O problema.** A norma do modelo conceitual (`GOVERNANCA.md` §3.2) descrevia a **forma** do modelo
— objetos, propriedades, operações, estados, versões — sem dizer **de onde** cada elemento vem.
Medido em 2026-09-21:

- `lastro` aparecia **0** vezes em `GOVERNANCA.md` e **0** vezes na skill `diario-de-obras`;
  `requisito secundário`, **0** vezes na skill.
- O modelo do `P-0745`, escrito sob essa norma, trazia **11 objetos** para um pedido que nomeava
  poucas coisas. O dono o reprovou; o instrumento de conferência (`modelo.py check`) aprovava o
  mesmo modelo com `modelo: OK`, exit `0` — ele conferia forma, não procedência.
- A primeira versão do modelo **deste** plano repetiu o defeito: quatro propriedades escritas como
  objetos próprios. O dono a recusou no Marco 1.

**A solução, em uma frase.** Todo elemento do modelo passa a ter âncora declarada no pedido do
dono; o que não tem âncora sai do contrato para uma seção própria, e o instrumento recusa objeto sem
âncora.

**Vocabulário mínimo.**

| termo | significa |
|---|---|
| **modelo conceitual** | a seção `## 1` de todo plano: os objetos que o plano constrói, as operações que os alteram e o estado inicial × final de cada propriedade. É o contrato entre o dono e o loop |
| **enunciado** | o pedido do dono, transcrito verbatim na `## 0` do plano |
| **lastro** | a âncora de um elemento do modelo: o trecho do enunciado (ou do prompt de origem) que o justifica |
| **requisito secundário** | entrega que o agente julga necessária e que o enunciado não pediu; fica visível ao dono, fora do contrato |
| **promoção indevida** | escrever como objeto próprio o que é propriedade de outro objeto |
| **versão vigente / pendente** | o modelo em vigor / uma emenda que aguarda o marco para vigorar (`GOVERNANCA.md` §3.2) |
| **Marco** | ponto em que o dono lê e dá o veredito; o que o instrumento não afere, o Marco guarda |

---

## O arco

| estrato | pergunta que responde | tarefas |
|---|---|---|
| 1. A regra | de onde vem cada elemento do modelo, e como o pedido se lê? | `LST-T1`, `LST-T7` |
| 2. A residência | onde fica o que não tem lastro, e onde o lastro se escreve? | `LST-T3`, `LST-T8`, `LST-T9` |
| 3. A aferição | o que a máquina recusa sozinha? | `LST-T5` |
| 4. A prova | o modelo que originou o pedido converge sob a regra nova? | `LST-T6` |

Cada estrato é inútil sem o anterior: sem regra não há o que declarar; sem residência o
instrumento não tem campo cuja presença aferir; sem aferição a regra depende de alguém lembrar; e
sem a prova no caso de origem, a regra não mostra que resolve o que o dono recusou.

**Fora da tabela:** a `LST-T0` foi dissolvida antes da execução (`DLS-10`); a `LST-T2` e a
`LST-T4` saíram com a operação sem lastro que materializavam e viraram o `TK-70` (`DLS-11`). Nenhuma
das três produziu artefato.

---

## `LST-T1` — Todo elemento do modelo precisa de âncora no pedido

**Contexto que a motivou:** a norma não perguntava de onde vinha um objeto; `lastro` tinha 0
ocorrências na doutrina. Um modelo podia listar qualquer coisa que o autor achasse relevante, e o
dono passava a ser cobrado por um contrato que não pediu.

**O que é o artefato:** regra de doutrina — o parágrafo **Lastro no enunciado, e as duas vias de
leitura** em `GOVERNANCA.md` §3.2 (linha 338) e o parágrafo **Lastro, por elemento** na subseção
*Modelo de domínio (seção do plano)* de `.claude/skills/diario-de-obras/SKILL.md` (linha 190).

**Como funciona na prática:**
1. **O que dispara:** o `pantonic-model-designer` escrevendo ou emendando a `## 1` de um plano.
2. **A entrada:** a `## 0` do plano (o enunciado verbatim).
3. **O processamento:** cada trecho do enunciado é lido por uma de duas vias — **via de estado**
   (descreve como as coisas estão ou deverão estar → popula a tabela de estado inicial × final) ou
   **via de operação** (pede ação → popula o fluxo de operações).
4. **A saída:** todo objeto, operação e propriedade cita o trecho que o sustenta. Exemplo real, a
   linha de objeto deste plano: o objeto `restrições do modelo conceitual` tem como lastro
   *"Só existe um objeto nesse modelo: as restrições/guardrails"*.

Medido hoje: `grep -ci lastro GOVERNANCA.md` → **8**; na skill → **11** (eram 0 e 0).

**Protege contra:** elemento do modelo sem pedido que o sustente — o modelo inflado que o dono
recusou no `P-0745`.

## `LST-T7` — O que o plano constrói é objeto; o que muda de estado é propriedade

**Contexto que a motivou:** nada na norma dizia como distinguir objeto de propriedade. A versão 1
do modelo deste plano escreveu quatro propriedades como objetos, e o dono a reprovou.

**O que é o artefato:** regra de doutrina — o parágrafo de decomposição em `GOVERNANCA.md` §3.2
(linhas 350-362) e o trecho correspondente da skill `diario-de-obras` (linha 214).

**Como funciona na prática:** antes de escrever a tabela de objetos, o autor decompõe o enunciado
nesta ordem: **o que o plano constrói é objeto**; o que converge de um estado a outro é
**propriedade** dele; **descrição de estado não vira objeto próprio**. Exemplo real: este plano
tem **1 objeto** (`restrições do modelo conceitual`) e **6 propriedades** — as quatro que a
versão 1 escrevia como objetos são hoje propriedades desse objeto (`modelo.py check` sobre o plano:
`1 objetos, 6 propriedades`).

**Protege contra:** **promoção indevida**. A norma declara que essa guarda **não é aferível por
instrumento** — é o Marco quem a exerce.

## `LST-T3` — A seção do que não tem lastro

**Contexto que a motivou:** elemento sem lastro tinha dois destinos, ambos ruins: entrar no modelo
como se fosse pedido do dono, ou sumir.

**O que é o artefato:** gramática publicada — o parágrafo **Requisito secundário, a residência do
elemento sem lastro** na skill `diario-de-obras` (linha 202), que define a seção de nível 2
`Requisitos secundários` com a tabela `| requisito | por que o agente o julga necessário | quem
responde |`.

**Como funciona na prática:** quando o autor encontra algo que o plano precisa entregar mas o
enunciado não pediu, escreve uma linha nessa seção em vez de um objeto no modelo. A skill diz, com
esse literal: *"Elemento dessa seção não entra no modelo e não é aferido por lastro."* Exemplos
reais: `## 2. Requisitos secundários` deste plano (linha 246) e `## Requisitos secundários` do
`P-0745` (linha 140), onde foi parar o que a reautoria tirou do modelo.

**Protege contra:** entrega não pedida cobrada como contrato, e entrega necessária escondida do
dono. A responsabilidade pela linha é inteira do agente.

## `LST-T8` — Onde o lastro se escreve, para a máquina poder ler

**Contexto que a motivou:** a `LST-T1` exigiu lastro sem dizer em que campo ele mora. O instrumento
não tinha o que conferir (`AE-1`).

**O que é o artefato:** as linhas `objetos`, `operações` e `estado` da tabela de gramática na
skill `diario-de-obras`: coluna de lastro na tabela de objetos, campo `lastro:` na linha de máquina
de cada operação, coluna de lastro na tabela de estados. A mesma entrega separa o que o instrumento
afere do que o Marco guarda e declara a **retroatividade** (`GOVERNANCA.md` §3.2, linha 449): plano
em status terminal (`done`, `cancelled`, `superseded`) não se migra.

**Como funciona na prática:** o autor do modelo preenche a coluna; o `check` confere a presença
dela na tabela de objetos. O lastro da operação, o da propriedade e a pertinência do trecho citado
ficam com o Marco. Exemplo real: a tabela de objetos do `P-0745` abre com
`| objeto | o que é | propriedades | contrato | origem | lastro na §0 | tipo |`.

**Protege contra:** regra sem campo — exigência que nenhum instrumento consegue conferir.

## `LST-T9` — Três frases da norma acertadas contra os planos reais

**Contexto que a motivou:** as três tarefas de redação publicaram três frases corretas em
intenção e erradas quando confrontadas com os planos existentes (`AE-7`, `AE-9`, `AE-10`, `AE-11`):
o cabeçalho de coluna exigido por igualdade literal, que nenhum plano vivo usava; a seção de
requisitos secundários fixada pelo número `## 2`, já ocupado por *Fatos estabelecidos* em outros
planos; e um caso medido que fundia duas recusas distintas numa só.

**O que é o artefato:** três trechos editados — na skill, a coluna é reconhecida pelo cabeçalho que
**começa com** `lastro` e a seção é **nomeada**, em qualquer posição; em `GOVERNANCA.md` §3.2, o caso
medido da promoção indevida separa as duas recusas.

**Como funciona na prática:** o `check` casa o cabeçalho por prefixo. Exemplo real: a coluna
`lastro na §0` deste plano e do `P-0745` é reconhecida sem ser renomeada.

**Protege contra:** norma que o próprio acervo não consegue cumprir sem ser reescrito.

## `LST-T5` — O instrumento recusa objeto sem lastro

**Contexto que a motivou:** `modelo.py check` aprovava com `modelo: OK` exatamente o modelo que o
dono havia reprovado.

**O que é o artefato:** a violação `V21` em `.claude/tools/modelo.py` (linha 392), dentro do
`check`, com testes em `tests/test_modelo.py` e as fixtures de `tests/fixtures/modelo/`, que
passaram a falar a forma publicada (`DLS-17`).

**Como funciona na prática:**
1. **O que dispara:** `python .claude/tools/modelo.py check --plano <plano>` — rodado pelo loop no
   despacho e no fechamento de tarefa, ou à mão.
2. **A entrada:** a tabela de objetos da `## 1` vigente do plano e o status do plano.
3. **O processamento:** para cada objeto sem célula de lastro, emite `V21` — **exceto** se o plano
   está em status terminal.
4. **A saída:** exemplo real, o `P-0745` na versão anterior à reautoria (a do commit `d75e7a6`),
   rodado em 2026-09-24:

```
V21 objeto — objeto sem lastro declarado agregado medido do planejador
V21 objeto — objeto sem lastro declarado norma da unidade de trabalho
…  (mais 8 linhas)
V21 objeto — objeto sem lastro declarado citações históricas de medida
modelo: FALHOU — 11 violação(ões)
```
   exit `1`. O mesmo plano, reautorado, hoje: `modelo: OK — 6 operações, 3 objetos, 7 propriedades,
   10 tarefas, versão 4`, exit `0`.

`tests/test_modelo.py`: **30 passed** (2026-09-24).

**Protege contra:** o instrumento aprovar modelo sem procedência. **Limite declarado:** a `V21`
afere **objeto**; lastro de operação e de propriedade é guarda do Marco. Dois recortes da
operação que a especificava saíram por decisão registrada: a checagem de "ator citado que não é
objeto" reprovaria modelos já aceitos (`DLS-13`), e o reconhecimento de tarefa de requisito não
fundamental não tinha forma publicada (`DLS-18`, virou o `TK-71`).

## `LST-T6` — O modelo que originou o pedido, reautorado

**Contexto que a motivou:** o modelo do `P-0745` é o caso que o dono reprovou em 2026-09-21. A
regra nova só vale se converter justamente ele.

**O que é o artefato:** a `## 1` de `docs/plans/P-0745-planejador-modelo-operacao.md`, reautorada
pelo `pantonic-model-designer`, mais a seção `## Requisitos secundários` daquele plano e o ramo de
`no-go` do Marco 1 na tabela de marcos dele.

**Como funciona na prática:** de **11 objetos sem lastro** para **3 objetos com lastro** —
`agente de planejamento`, `agente model designer` e `tarefa` —, cada um com a coluna `lastro na §0`
preenchida. O que não tinha âncora migrou para a seção de requisitos secundários. O modelo do
`P-0745` seguiu sendo emendado depois (hoje na versão 4) e continua saindo `0` no `check`.

**Protege contra:** regra aprovada em abstrato que não resolve o caso concreto.

---

## O que vale além deste plano

| regra | o que resolve | residência |
|---|---|---|
| Lastro obrigatório e as duas vias de leitura | elemento do modelo sem pedido que o sustente | `GOVERNANCA.md` §3.2, *Lastro no enunciado, e as duas vias de leitura* |
| Decomposição objeto × propriedade | promoção indevida | `GOVERNANCA.md` §3.2, parágrafo da decomposição |
| Requisitos secundários | entrega não pedida cobrada como contrato | skill `diario-de-obras`, *Requisito secundário, a residência do elemento sem lastro* |
| Retroatividade | norma nova reescrevendo plano fechado | `GOVERNANCA.md` §3.2, *Retroatividade* |
| Recorte do próprio contrato pela regra de lastro | oração de operação sem âncora sobrevivendo por inércia | decisões `DLS-11`, `DLS-13`, `DLS-18` do plano |

---

## Os ganhos, medidos

| medida | antes | depois |
|---|---|---|
| ocorrências de `lastro` em `GOVERNANCA.md` | 0 | 8 |
| ocorrências de `lastro` na skill `diario-de-obras` | 0 | 11 |
| `modelo.py check` sobre o modelo que o dono reprovou (`P-0745`, pré-reautoria) | exit `0`, `modelo: OK` | exit `1`, 11 × `V21` |
| objetos no modelo do `P-0745` | 11 | 3 |
| propriedades escritas como objeto no modelo deste plano | 4 (versão 1, recusada) | 0 (1 objeto, 6 propriedades) |
| `tests/test_modelo.py` | — | 30 passed |

---

## O padrão que a execução revelou

**A regra de lastro recortou o próprio plano que a institui, três vezes.** O dono tirou a restrição
de atualização por não ter âncora (`DLS-11`); o consultor tirou a checagem de ator por
inexequibilidade medida (`DLS-13`) e o reconhecimento de tarefa não fundamental por falta de âncora
(`DLS-18`). Nenhum recorte reduziu o que o plano promete: todos aplicaram a regra ao contrato.

**Defeitos da execução, com estado:**

| defeito | estado | o que fecha |
|---|---|---|
| Regra exigida sem campo onde se declarar (`AE-1`) | 🟢 **Fechado com guarda** — a `V21` confere a coluna | — |
| Frase da norma incompatível com o acervo vivo (`AE-7`, `AE-9`, `AE-10`) | 🟡 **Caso fechado, classe sem guarda** — nenhum verificador confronta norma nova com os planos vivos antes de publicar | pendência 4 |
| Card sem `Arquivos-alvo` completo / verificação sem valor esperado (`AE-19`, `AE-20`) | 🔴 **Regra escrita, aplicação pendente** | pendência 4 (`TK-72`) |
| `review_evidence.py` não expande alvo terminado em barra (`AE-22`) | 🔴 **Regra escrita, aplicação pendente** | pendência 5 (`TK-74`) |
| Norma sem ramo para primeira versão recusada e reautorada (`AE-21`) | 🔴 **Regra escrita, aplicação pendente** | pendência 3 (`TK-70`) |
| Alcance da `V21` sobre a versão pendente (`## 1A`) decidido pela execução, sem teste (`AE-17`) | 🟡 **Caso fechado, classe sem guarda** — a `V21` só varre a `## 1` vigente | pendência 6 |

---

## Pendências abertas ao fim do plano

| # | pendência | por que ficou aberta | o que a fecha | bloqueia algo? |
|---|---|---|---|---|
| 1 | Critério de "ator inédito na operação" (`AE-18`) | o dono tipificou a classe; o loop a dispensou por medição (reprovaria 6 de 7 atores do `P-0743` aceito) | decisão do dono: manter ou dispensar — `TK-73` Pacote 2 | não |
| 2 | Reconhecer tarefa de requisito não fundamental | forma textual nunca publicada; saiu do modelo (`DLS-18`) | `TK-71` | não |
| 3 | Vigência bilateral do modelo e ramo de primeira versão recusada | fora do lastro deste plano (`DLS-11`, `AE-21`) | `TK-70` | não |
| 4 | Régua de autoria de card (aceite por literal, `Arquivos-alvo` completo, valor esperado) | lições de autoria, fora do objeto deste plano | `TK-72` | não |
| 5 | Alvo de diretório em `review_evidence.py` | instrumento de outro plano | `TK-74` | não |
| 6 | `V21` sobre a versão pendente | ponto aberto no card, sem teste | sem tíquete próprio; registrado em `AE-17` | não |

**Resumo do estado.** O plano entregou as 7 tarefas: a regra de lastro, a decomposição
objeto × propriedade, a residência do requisito secundário, a gramática do lastro, a violação `V21`
e a reautoria do `P-0745`. Ficam 6 pendências, 5 delas com tíquete; nenhuma bloqueia outro plano e
nenhuma tem efeito fora do repositório — a doutrina nova ainda não foi propagada aos kits
derivados.
