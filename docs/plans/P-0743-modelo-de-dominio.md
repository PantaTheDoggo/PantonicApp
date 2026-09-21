# P-0743 — O modelo conceitual vira modelo de domínio

**Data:** 2026-09-20 · **Origem:** diretiva do dono sobre o Marco 2 do `P-0741`
(`docs/plans/P-0741-modelo-conceitual.md`, `AE-18`), apontamentos 1, 2 e 4 · **Plano de origem:**
`P-0741` (classe B — continuação: o entregue fica de pé e a rota se estende) · **Status:** `done`
· 2026-09-21 · **Prefixo das tarefas no diário:** `DOM-T<n>` · **Prefixo das decisões:** `D-<n>` ·
**Checagem de versão do kit:** modo hub — congelada em `0.0.0` (`GOVERNANCA.md` §10), nada a
comparar.
**Ordem de execução:** DOM-T1 → DOM-T2 → DOM-T3 → DOM-T3a → DOM-T3b → DOM-T4 → DOM-T5 → DOM-T5a → DOM-T5b → DOM-T7 → DOM-T8 → DOM-T8a → DOM-T9 → DOM-T9a → DOM-T9b → DOM-T9c → DOM-T10 → DOM-T6
A `DOM-T6` foi reordenada para o fim pela orquestração em 2026-09-20: ela revisa o `README.md` contra a árvore final (`G-README` dever 2), e o terceiro estágio reescreve a norma, a gramática e o instrumento que a §8.1 pública descreve. Ela pertence ao **Marco 5**. Ver `AE-16`.
**Modelo de planejamento:** Opus 5 (rodada de replanejamento de 2026-09-20).

**Marcos de validação pelo dono:**

| marco | o que o dono lê | veredito |
|---|---|---|
| **Marco 1** | a `## 1. Modelo conceitual` deste plano **e** a `## 7. A leitura do dono — exemplo trabalhado`, que é a forma nova já preenchida com dados reais | `go` = o plano sai para execução; `no-go` = `cancelled`, nada executado |
| **Marco 2** | ~~a saída de `modelo.py show` sobre o `P-0744` depois da `DOM-T3`, mais o `README.md` revisado (`DOM-T6`)~~ **extinto em 2026-09-20 pela régua da `D-43`** | a leitura de `show` que ele apresentaria é a da forma que o terceiro estágio substitui, e um marco que mede um estado que vai ser descartado não é detector de desvio: ele não permite inferir que o estado final está sendo atingido. A entrega da `DOM-T6` não se perde — migra para o **Marco 5** |
| **Marco 3** | ~~a saída de `modelo.py show` depois da `DOM-T10`~~ **dispensado em 2026-09-21 por ato do dono** — a entrega foi apresentada e o veredito sobre ela recusado: *"Eu somente vou validar com base no AS-IS"* | a régua da `D-43` não cai; muda **qual artefato** é o detector. A validação inteira migra para o **Marco 5**, pelo `docs/OPERACOES_AS_IS.md`, e a `DOM-T6` fica destravada. Diretiva integral em `docs/DIARIO_DE_OBRAS.md`, *Diretiva de validação do `P-0743`* |
| **Marco 4** | uma versão pendente ao lado da vigente, com o consultor exercendo a primeira instância e o dono a segunda (`D-36`) | aceite registrado no diário; **sem cards até o Marco 3 dar `go`** |
| **Marco 5** | um relatório de encerramento sem questão tática nos resultados (`D-42`) e o `README.md` descrevendo a forma nova (`DOM-T6`) | aceite registrado no diário; **sem cards até o Marco 3 dar `go`** |

**Tarefas:** 18 — `DOM-T1`..`DOM-T6` e os corretivos `DOM-T3a`, `DOM-T3b`, `DOM-T5a` e
`DOM-T5b` (estágios 1 e 2, `ESC-1` a `ESC-5`), mais `DOM-T7`..`DOM-T10` e os corretivos `DOM-T8a`
e `DOM-T9a` (`ESC-6`), `DOM-T9b` (`ESC-9`) e `DOM-T9c` (`ESC-10`), que são o **Marco 3** do
terceiro estágio. Os Marcos 4 e 5 estão declarados em §13.5 e **ainda não têm cards**, por
decisão registrada ali. Fila única, sequencial.

> **Este é o último plano escrito na forma anterior do modelo** (orações `M-<n>` com estado
> gravado). O instrumento que lê a forma nova nasce na `DOM-T3`; um plano escrito na forma nova
> antes disso seria recusado pelo gate de despacho. O primeiro plano na forma nova é o `P-0744`,
> que já está escrito assim e pode ser aberto lado a lado com a §7 deste (`D-11`).

---

## 0. O problema, verbatim

Diretiva do dono, 2026-09-20, sobre a leitura do Marco 2 do `P-0741` (`AE-18`), nas palavras dele:

1. **A forma prescrita não é o modelo conceitual do DDD.** O modelo deve ser fidedigno à
   **intuição do objetivo** do plano, descrito **em objetos e operações**. Exemplo dado: um plano
   que copia de uma pasta para outra teria como modelo "agente lê pasta de origem, executa operação
   de cópia em memória, localiza a pasta de destino, executa operação de colagem". O que o `P-0741`
   prescreveu — orações independentes afirmando comportamento observável, cada uma com estado
   próprio — **não** é isso: falta o encadeamento de operações sobre objetos.
2. **O estado tem de ser posição no fluxo, não status por frase.** O dono quer ler "o estágio atual
   é a leitura da pasta de origem" e opinar sobre esse fato; o agente, lendo o mesmo, deriva o que
   precisa ("então preciso de um caminho e de um toolset de leitura"). Hoje o `show` devolve 20
   estados paralelos, não uma posição.
3. **Contratos que tornem o conceito em implementação**, e uma proposição que **padronize** que
   cada tarefa terá um texto com essas características.
4. **O ensinamento não pode ficar pulverizado dentro dos agentes.** Decisão do dono no mesmo ato,
   contra a recomendação do planejamento, com o critério declarado: *"o modelo é a etapa de ouro da
   programação por IA; é ela quem fecha o vínculo entre homem e máquina, então o benefício da
   consistência máxima com julgamento do domínio se sobrepõe à fenda entre julgar e escrever."*
   Um agente único `model-designer`, dono de todas as operações do modelo; os demais o acionam para
   resolver conflito, entender contexto e propor mudança. **E o plano deve propor medidas
   alternativas que reduzam essa fenda.**

---

## 1. Modelo conceitual

> **Como ler esta seção (Marco 3).** Ela descreve, em linguagem corrente, o que este plano entrega:
> os objetos que ele trabalha, as propriedades desses objetos, a ordem em que as operações as
> alteram e o estado final que o dono especificou. A leitura gerada por
> `python .claude/tools/modelo.py show --plano docs/plans/P-0743-modelo-de-dominio.md` é esta mesma
> seção com o estágio atual derivado do andamento das tarefas.

**Estado do modelo:** versão 1 · 2026-09-21 · autor: modelador · 13 operações · 21 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem |
|---|---|---|---|---|
| norma do modelo de domínio | o texto de governança que diz o que o modelo de um plano é, o que cada bloco dele carrega e quem escreve cada parte | forma prescrita, regra de estágio, divisão de papéis, regra de versão, regra de aceite | residência única em `GOVERNANCA.md` §3.2; prosa normativa em blocos que substituem parágrafos nomeados, sem recopiar a gramática nem o ensinamento de autoria; nenhum outro documento a repete | OP-1 |
| gramática do modelo | a forma exata de cada elemento da seção do modelo, escrita para a máquina ler e para o autor obedecer | elementos declarados, forma do campo do card | residência única na skill `diario-de-obras`, subseção `Modelo de domínio (seção do plano)`; uma linha de tabela por elemento, com a forma à esquerda e a regra mais o código de violação à direita | OP-2 |
| instrumento do modelo | o programa que confere a seção contra a gramática e gera a leitura do dono | vocabulário de violações, leitura do dono, tolerância à forma anterior, descrição de si mesmo | `.claude/tools/modelo.py`, verbos `check` e `show`, exits `0`, `1` e `2` com literais fixos; lê as tarefas do plano por `backlog._parse_plano` e não reescreve `backlog.py`; cada regra nova nasce com fixture e teste pelo caminho do usuário | OP-3 |
| modelador | o agente único dono de todo ato sobre o modelo de um plano | atos declarados, ensinamento de autoria, gate de devolução | `.claude/agents/pantonic-model-designer.md`; front matter com nome, descrição e lista de ferramentas, e corpo com os atos, o ensinamento e o gate; as duas portas de inventário do kit contam os agentes e hoje fecham sobre dez | OP-5 |
| cadeia de papéis diante do modelo | as definições de conduta dos demais papéis e do procedimento que conduz o plano, no ponto exato em que tocam o modelo | escrita no modelo, transporte do dossiê | `.claude/agents/pantonic-reviewer.md`, `pantonic-planner.md` e `pantonic-consultant.md`, mais a skill `scrum-master`; cada elo declara o que devolve e quem o lê, e nenhum elo manda fazer o que outro elo proíbe | OP-6 |
| modelo deste plano | a seção que abre o `P-0743` e descreve o que ele entrega, mais o lastro que cada card tem nela | forma da seção, lastro das tarefas | seção `## 1. Modelo conceitual` de `docs/plans/P-0743-modelo-de-dominio.md` e o campo `Operação do modelo` de cada card da §9; a seção é ato do modelador e o campo é ato do executor que converte os cards, e as duas mãos não se cruzam | OP-12 |
| documentação pública do kit | a porta de entrada por onde quem chega ao repositório entende o que o kit faz | descrição do modelo na porta de entrada | `README.md`, seção 8.1 e as remissões a ela; toda afirmação sobre o instrumento confere com o comportamento medido na árvore, e o verificador de README confronta os numerais por extenso com a contagem de arquivos | OP-13 |
| acervo de planos na forma anterior | os planos já escritos antes desta rota, com o modelo em frases numeradas e estado gravado em cada uma | legibilidade pelo instrumento | `docs/plans/`, vinte e dois planos medidos em 2026-09-20, dos quais vinte e um são anteriores à doutrina do modelo; nenhum é tocado por este plano e nenhum é migrado | externo |
| doutrina publicada do kit | o corpo de regras, gramáticas e definições de papel que o repositório já carrega e que esta rota toca em pontos nomeados | ponteiros para a residência do modelo | `GOVERNANCA.md`, as skills e os agentes do kit; cada ponteiro nomeia a seção vigente que governa a forma, e ponteiro órfão é defeito no caminho da entrega, não dívida a pagar depois | externo |

### 1.2 Fluxo de operações

**A. A forma nasce: norma, gramática e instrumento**

- **OP-1** — O redator da norma grava na doutrina do kit o que o modelo de um plano passa a ser: objetos e operações encadeadas no lugar de frases soltas, a posição no fluxo derivada do andamento das tarefas, e a autoria concentrada num papel só.
  - `precisa de: acervo de planos na forma anterior, doutrina publicada do kit` · `altera: norma do modelo de domínio.forma prescrita, norma do modelo de domínio.regra de estágio, norma do modelo de domínio.divisão de papéis` · `tarefas: DOM-T1`
- **OP-2** — O redator da gramática publica a forma exata de cada elemento da seção do modelo, para que a máquina a leia sem adivinhar e quem escreve saiba o que vai em cada linha.
  - `precisa de: norma do modelo de domínio` · `altera: gramática do modelo.elementos declarados, gramática do modelo.forma do campo do card` · `tarefas: DOM-T2`
- **OP-3** — O implementador do instrumento faz o programa conferir a seção contra a gramática e gerar a leitura do dono, que abre pelo estágio atual e não bloqueia plano escrito na forma anterior.
  - `precisa de: gramática do modelo, acervo de planos na forma anterior` · `altera: instrumento do modelo.vocabulário de violações, instrumento do modelo.leitura do dono, instrumento do modelo.tolerância à forma anterior` · `tarefas: DOM-T3`
- **OP-4** — O implementador acerta o que o instrumento e a gramática dizem de si mesmos, para que nenhum texto de apresentação descreva a forma que acabou de sair de uso.
  - `precisa de: instrumento do modelo, doutrina publicada do kit` · `altera: instrumento do modelo.descrição de si mesmo, doutrina publicada do kit.ponteiros para a residência do modelo` · `tarefas: DOM-T3a, DOM-T3b`

**B. O papel nasce, e os demais papéis se alinham a ele**

- **OP-5** — O autor de papéis cria o agente único dono de todo ato sobre o modelo e escreve nele o ensinamento de como um modelo se escreve, que deixa de ficar pulverizado nos demais agentes.
  - `precisa de: norma do modelo de domínio, gramática do modelo` · `altera: modelador.atos declarados, modelador.ensinamento de autoria` · `tarefas: DOM-T4`
- **OP-6** — O autor de papéis alinha os demais papéis à norma: o revisor perde a escrita no modelo, e quem precisa de um ato devolve o dossiê fechado na própria linha de retorno, que quem conduz a sessão despacha.
  - `precisa de: norma do modelo de domínio, modelador` · `altera: cadeia de papéis diante do modelo.escrita no modelo, cadeia de papéis diante do modelo.transporte do dossiê` · `tarefas: DOM-T5, DOM-T5a, DOM-T5b`

**C. A propriedade entra, e com ela o aceite e a versão**

- **OP-7** — O redator da norma reescreve a norma para propriedades: objeto passa a ser o que possui propriedade, o plano declara estado inicial e estado final, o aceite do plano é a confrontação dos dois, e a emenda ao modelo versiona em vez de reescrever.
  - `precisa de: norma do modelo de domínio` · `altera: norma do modelo de domínio.forma prescrita, norma do modelo de domínio.regra de aceite, norma do modelo de domínio.regra de versão` · `tarefas: DOM-T7`
- **OP-8** — O redator da gramática reescreve a gramática para a forma nova: propriedade na tabela de objetos, o que cada operação altera, o estado inicial e o final, o registro de versões, e a versão pendente como bloco irmão da vigente.
  - `precisa de: norma do modelo de domínio, gramática do modelo` · `altera: gramática do modelo.elementos declarados, gramática do modelo.forma do campo do card` · `tarefas: DOM-T8`
- **OP-9** — O mantenedor reaponta cada região da doutrina que ainda mandava registrar o ato do modelo na forma que a versão substituiu, sem mudar o que papel nenhum faz.
  - `precisa de: gramática do modelo, doutrina publicada do kit` · `altera: doutrina publicada do kit.ponteiros para a residência do modelo` · `tarefas: DOM-T8a`
- **OP-10** — O implementador ensina o instrumento a ler propriedade, estado e versão, e a leitura do dono passa a terminar no estado final que ele mesmo especificou.
  - `precisa de: gramática do modelo, instrumento do modelo` · `altera: instrumento do modelo.vocabulário de violações, instrumento do modelo.leitura do dono` · `tarefas: DOM-T9`
- **OP-11** — O autor de papéis põe o modelador a falar a forma nova e fixa a fronteira do que ele devolve: o que é da seção ele corrige antes de devolver, e o que mora no card volta medido, para quem conduz a sessão rotear.
  - `precisa de: modelador, gramática do modelo, instrumento do modelo` · `altera: modelador.ensinamento de autoria, modelador.gate de devolução` · `tarefas: DOM-T9a, DOM-T9b, DOM-T9c`

**D. O modelo deste plano, e a porta de entrada**

- **OP-12** — O modelador constrói o modelo deste plano na forma nova, e o executor converte o campo de cada card para a operação que ele materializa, com o texto e o contrato copiados.
  - `precisa de: modelador, cadeia de papéis diante do modelo, gramática do modelo, instrumento do modelo` · `altera: modelo deste plano.forma da seção, modelo deste plano.lastro das tarefas` · `tarefas: DOM-T10`
- **OP-13** — O mantenedor abre a porta de entrada pública ao modelo de domínio e confere a documentação pública contra o estado da árvore ao fim do plano.
  - `precisa de: modelo deste plano, doutrina publicada do kit, instrumento do modelo` · `altera: documentação pública do kit.descrição do modelo na porta de entrada` · `tarefas: DOM-T6`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final |
|---|---|---|
| norma do modelo de domínio.forma prescrita | a norma prescrevia frases numeradas independentes, cada uma afirmando um comportamento observável, sem objeto, sem propriedade e sem encadeamento | a norma prescreve objetos com propriedades e operações encadeadas que as alteram, e objeto e operação se descobrem por decomposição da propriedade, não por intuição |
| norma do modelo de domínio.regra de estágio | o andamento era gravado frase a frase, e o plano exibia vinte estados paralelos sem dizer em que ponto estava | o andamento é derivado do andamento das tarefas e nenhum papel o grava; o estágio atual é a primeira operação que ainda não concluiu |
| norma do modelo de domínio.divisão de papéis | o ensinamento sobre o modelo estava pulverizado entre os agentes, e mais de um papel escrevia na seção | um agente único é dono de todo ato sobre o modelo, nenhum outro papel escreve na seção, e nenhum agente aciona outro |
| norma do modelo de domínio.regra de versão | não havia versão: emenda ao modelo era reescrita, e o que a reescrita apagava não ficava registrado em lugar nenhum | a emenda versiona: a vigente e a pendente coexistem até o marco, a validação se busca no consultor e depois no dono, e a obsoleta deixa no plano só a linha que registra a queda |
| norma do modelo de domínio.regra de aceite | o plano não declarava estado inicial nem estado final, e o sucesso dele não era confrontável contra nada | o plano declara estado inicial e estado final por propriedade, e o aceite é a confrontação dos dois: é essa diferença que tem valor para o dono |
| gramática do modelo.elementos declarados | a gramática descrevia cabeçalho, vocabulário, frases numeradas e uma lista de mudanças do modelo | a gramática descreve cabeçalho com versão e contagem de propriedades, objetos com propriedades, operações com o que precisam e o que alteram, estado inicial e final, registro de versões e a versão pendente como bloco irmão |
| gramática do modelo.forma do campo do card | o card citava a frase do modelo que materializava, sem trazer o contrato do que a tarefa recebe nas mãos | o card cita a operação, com o texto dela copiado e o contrato de cada objeto de que ela precisa, de modo que o executor saiba em que estágio está sem abrir o plano |
| instrumento do modelo.vocabulário de violações | nove regras, de V1 a V9, sobre a forma anterior, medidas em 2026-09-20 | vinte regras, de V1 a V20, cobrindo propriedade, estado inicial e final, registro de versões e versão pendente, cada uma com fixture e teste pelo caminho do usuário |
| instrumento do modelo.leitura do dono | a saída listava um estado por frase e não dizia em que ponto do fluxo o plano estava | a saída abre pelo estágio atual, mostra os objetos com propriedades, o fluxo inteiro e o estado final, e compara a versão vigente com a pendente quando as duas existem |
| instrumento do modelo.tolerância à forma anterior | plano anterior à doutrina saía com aviso próprio e não bloqueava o loop | mantida, e com as três condições nomeadas: ausência da seção, ausência do fluxo e ausência do estado inicial e final saem como forma anterior, e o loop segue |
| instrumento do modelo.descrição de si mesmo | o instrumento e o preâmbulo da gramática se descreviam pela forma anterior, que era a vigente no começo do plano | os dois se descrevem pela forma vigente e nomeiam a seção que a governa, sem resíduo da forma anterior fora dos literais normativos de saída |
| modelador.atos declarados | não existia agente dono do modelo, e o kit tinha nove agentes | existe um décimo agente, com quatro atos declarados — autoria, emenda, conflito e leitura —, e as duas portas de inventário do kit fecham sobre dez |
| modelador.ensinamento de autoria | o ensinamento de como se escreve um modelo não tinha residência própria | o ensinamento mora na definição do agente, começa pela propriedade e termina no teste de encadeamento, separado da norma e da gramática |
| modelador.gate de devolução | não havia gate, porque não havia ato a fechar | o gate fecha pela fronteira medida: violação da seção é ato não concluído e ele mesmo corrige; violação que mora no card volta como saída literal, para quem conduz a sessão rotear |
| cadeia de papéis diante do modelo.escrita no modelo | o revisor gravava confirmação no modelo e tinha ferramenta de escrita fora do laudo | nenhum papel além do modelador escreve no modelo, e a divergência que o revisor apura vira achado de processo |
| cadeia de papéis diante do modelo.transporte do dossiê | não havia dossiê: o pedido de mudança no modelo não tinha forma nem caminho de volta | o dossiê é fechado, com seis campos, viaja na linha de retorno de quem precisou dele e chega ao modelador pelo despacho de quem conduz a sessão |
| modelo deste plano.forma da seção | a seção trazia doze frases numeradas com estado gravado em cada uma, mais uma tabela de mudanças do modelo | a seção traz nove objetos com propriedades, treze operações encadeadas, o estado inicial e o final de cada propriedade e o registro de versões |
| modelo deste plano.lastro das tarefas | os dezoito cards citavam a frase do modelo que materializavam | os dezoito cards citam a operação que materializam, com o texto e o contrato copiados, e o instrumento sai sem violação sobre o plano |
| documentação pública do kit.descrição do modelo na porta de entrada | a documentação pública descrevia o modelo conceitual na forma de frases numeradas | a documentação pública descreve o modelo de domínio, quem o escreve e como o dono lê o estágio atual, conferida contra o estado da árvore ao fim do plano |
| acervo de planos na forma anterior.legibilidade pelo instrumento | vinte e dois planos, vinte e um anteriores à doutrina do modelo e um escrito na forma anterior, medidos em 2026-09-20 | mantida sem migração: os vinte e dois continuam legíveis, nenhum é reescrito e nenhum bloqueia o loop |
| doutrina publicada do kit.ponteiros para a residência do modelo | os ponteiros nomeavam a forma e a residência anteriores, que eram as vigentes no começo do plano | cada ponteiro nomeia a seção vigente e a forma que ela governa, e nenhuma região da doutrina manda registrar o ato do modelo na forma que saiu de uso |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 1 | 2026-09-21 | vigente | modelador · ato de autoria na forma nova, despachado pelo Ato 1 da `DOM-T10` (`D-31`, `D-52`). Primeira versão da seção na forma nova: a numeração da forma anterior contava mudanças de texto, não versões do modelo, e não continua aqui |

---

## 2. Fatos estabelecidos

- **F-1** — A confirmação de uma oração é ato do revisor, no mesmo ato do laudo, com a tarefa em
  `review`. Fechar o descasamento entre esse instante e a regra `V6` custou quatro atos: a `DMC-20`
  admitiu `review`, a `MC-T3` descobriu o descasamento, a `DMC-27` reescreveu o contrato nos três
  lugares e a `MC-T4a` inteira corrigiu o desfecho do gate. Fonte: `docs/OPERACOES_AS_IS.md`,
  seções `MC-T3` e `MC-T4a`, e `AE-18`.
- **F-2** — Nenhum agente do kit pode despachar outro agente: as listas `tools:` medidas em
  2026-09-20 são `Read, Glob, Grep, Bash, Edit` (reviewer), `Read, Glob, Grep, Bash, Write, Edit`
  (consultant) e `Read, Glob, Grep, Write, Edit, Bash` (planner). Nenhuma contém ferramenta de
  despacho.
- **F-3** — O corpus da forma anterior é **um** plano: dos 22 do acervo, 21 são anteriores à
  doutrina (exit `2`) e 1 tem modelo — o próprio `P-0741`. Fonte: `docs/OPERACOES_AS_IS.md`,
  tabela *Os ganhos, medidos*.
- **F-4** — `.claude/tools/modelo.py` tem 389 linhas, nove regras `V1`..`V9`, dois verbos
  (`check`, `show`) e lê as tarefas por `backlog._parse_plano`; `tests/test_modelo.py` tem 6 testes
  funcionais; `tests/fixtures/modelo/` tem `plano-valido.md`, `plano-invalido.md`,
  `plano-sem-cabecalho.md` e `plano-sem-modelo.md`. Medido 2026-09-20.
- **F-5** — `python -m pytest tests -q --collect-only` coleta **245 testes** (2026-09-20).
- **F-6** — Os três guardas do kit saem verdes hoje, com estas saídas medidas em 2026-09-20:
  `python .claude/tools/backlog.py check` → `check: OK — nenhuma violação.`, exit `0`;
  `pwsh -NoProfile -File .claude/checks/check-readme.ps1` → começa por
  `check-readme: OK - 9 agente(s), 11 skill(s), 20 guardrail(s)`, exit `0`;
  `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → começa por
  `kit_check: check-drift OK - .claude/README.md == regenerado (9 agente(s), 11 skill(s))`, exit `0`.
- **F-7** — `README.md` linha 802 carrega a frase `O kit são nove agentes, onze skills, quatro
  verificadores executáveis e a declaração de projeções,`; a tabela **Agentes** da §11 tem **9**
  linhas (`grep -c` do prefixo de linha, 2026-09-20); `.claude/checks/check-readme.ps1` confronta o
  numeral por extenso dessa frase com a contagem de `.claude/agents/*.md` e falha quando divergem.
- **F-8** — `.claude/README.md` tem região gerada entre `<!-- kit:agents:begin -->` e
  `<!-- kit:agents:end -->`, com **9** linhas de agente, reescrita por
  `pwsh .claude/checks/kit_check.ps1 -Mode generate` e conferida por `-Mode check-drift`. A região
  deriva do front matter dos arquivos de agente; editá-la à mão recria a divergência.
- **F-9** — A matriz de responsabilidades de `GOVERNANCA.md` §3 tem **9** linhas de papel
  (linhas 89..98). Nenhuma frase de `GOVERNANCA.md` conta essas linhas: busca simples por
  "nove papéis", "oito papéis" e "nove agentes" não retornou ocorrência (2026-09-20). A §3.2
  ocupa as linhas 320..356.
- **F-10** — Em `.claude/agents/pantonic-reviewer.md`: a linha 5 é `tools: Read, Glob, Grep, Bash,
  Edit`; a linha 47 declara a escrita no modelo como única do papel; a linha 100 é o passo `5a`,
  que manda gravar a confirmação; a linha 140 delimita essa escrita. Medido 2026-09-20.
- **F-11** — Em `.claude/skills/scrum-master/SKILL.md`: `modelo.py check` é chamado na linha 60
  (passo 3, terceiro gate) e na linha 184 (passo 9, gate de fechamento); a linha 113 cita a regra
  `V6`; `modelo.py show` está na linha 276. Medido 2026-09-20.
- **F-12** — Em `.claude/skills/diario-de-obras/SKILL.md`: `## Gramática legível por máquina`
  começa na linha 130; `### Inbox de planos` na 169; `### Modelo conceitual (seção do plano)` na
  175; `## Formato de uma tarefa atômica` na 197. Medido 2026-09-20.
- **F-13** — Em `README.md`: `### 8.1 O modelo conceitual — o que o dono lê` começa na linha 644;
  a linha 420 remete a ela com a frase `O plano nasce com o **modelo conceitual** (§8.1), e o dono
  dá go ou no-go lendo só ele — é o Marco 1 de todo plano.`. Medido 2026-09-20.
- **F-14** — Em `docs/RUBRICA_DE_REVISAO.md`: `## 6. Achado de processo` começa na linha 246 e
  `## 7. Fronteira do papel` na 278. Medido 2026-09-20.
- **F-15** — `P-0742` está `blocked` e reescreve o roteamento do `scrum-master` como **transcrição
  literal** dos blocos dele (`DLF-6`). Editar a skill antes de o driver existir é, portanto, a
  ordem barata: a edição viaja de graça para o driver.
- **F-16** — `python .claude/tools/backlog.py check` lê o campo `- **Depende de:**` e só aceita id
  de tarefa entre crases, sem prosa e sem faixa; id que não é item torna a tarefa inselecionável.

---

## 3. Decisões (fechadas neste ato; o executor não as reabre)

| id | decisão | razão |
|---|---|---|
| `D-1` | A forma do modelo passa a ser **objetos com contrato** e **operações encadeadas**; a oração independente com estado por frase é aposentada | diretiva do dono (§0 item 1): o modelo deve ser fiel à intuição do objetivo, em objetos e operações; frases paralelas não têm encadeamento |
| `D-2` | O andamento é **derivado e nunca gravado**: operação `concluída` quando todas as tarefas dela estão `done` ou `cancelled`, `em curso` quando alguma está `in-progress` ou `review`, `prevista` nos demais casos; **estágio atual** é a primeira operação não concluída | o dono pediu posição no fluxo (§0 item 2); e a gravação de estado é a origem medida da fenda entre julgar e escrever (`F-1`) |
| `D-3` | A forma anterior **não é migrada**: o instrumento a reconhece pela ausência do heading `### 1.2 Fluxo de operações` e sai `2`, como já faz com plano anterior à doutrina | o corpus da forma anterior é um plano só, e ele está fechado (`F-3`); migrar plano fechado contraria a regra de não retroagir, já publicada em `GOVERNANCA.md` §3.2 |
| `D-4` | O campo do card passa a ser `- **Operação do modelo:**`, com o texto da operação copiado e a linha `precisa de` trazendo cada objeto com o contrato dele | é a proposição de padronização que o dono pediu (§0 item 3): todo card de todo plano abre com um texto da mesma natureza, e o executor deriva dali o que precisa |
| `D-5` | Nasce o agente `pantonic-model-designer`, dono de **todo** ato sobre o modelo: autoria, emenda, conflito e leitura | decisão do dono (§0 item 4), com o critério declarado dele |
| `D-6` | Nenhum agente aciona outro agente: quem precisa de um ato de modelo devolve o dossiê `Ato de modelo` na própria linha de retorno, e **quem conduz a sessão** despacha o modelador | `F-2`: nenhuma lista `tools:` do kit tem ferramenta de despacho; a rota alternativa não existe na plataforma |
| `D-7` | Mitigação da fenda julgar-escrever: as três de §3.1 marcadas como escolhidas, juntas | enumeração completa, escolha e rejeição em §3.1 |
| `D-8` | O revisor **perde** a ferramenta `Edit` e volta a não escrever fora do laudo | consequência direta de `D-5` e `D-6`; restaura a independência por lista de ferramentas que a `MC-T3` teve de quebrar |
| `D-9` | Três residências disjuntas: a **norma** (o que um modelo é, quem escreve) em `GOVERNANCA.md` §3.2; a **gramática** (o que a máquina lê) na skill `diario-de-obras`; o **ensinamento** (como se escreve um modelo bom) na definição do modelador | §0 item 4 recusa ensinamento pulverizado; e o padrão `DR-A` de `docs/RESIDENCIA_DOUTRINA.md` exige um assunto por residência |
| `D-10` | O `P-0741` **não** é reescrito: as 20 orações dele ficam como estão, confirmadas, e a supersessão entra como linha `MD-9` na lista de mudanças dele | as orações afirmam o que aquele plano entregou, e o que entregou está de pé — palavras do dono no `AE-18` |
| `D-11` | Este plano é o **último** escrito na forma anterior; o `P-0744` é o **primeiro** escrito na forma nova, e fica `blocked` até este fechar | o instrumento que lê a forma nova nasce na `DOM-T3`; plano em forma nova antes disso é recusado pelo gate de despacho do passo 3 do `scrum-master` (`F-11`) |
| `D-12` | O modelo do `P-0743` e do `P-0744` é escrito pelo **planejador**, não pelo modelador; a exceção expira quando a `DOM-T4` fechar | bootstrap: o modelador nasce na `DOM-T4`, e um plano não pode depender de um agente que ele mesmo cria |
| `D-13` | A especificação do agente de planejamento sai em **plano próprio**, o `P-0744` | fronteira de arquivos disjunta: o `P-0744` não toca nenhum arquivo de doutrina, de instrumento ou de agente que este plano toca (§11) |
| `D-14` | Os códigos de violação são renumerados `V1`..`V14` com significados novos, e os antigos desaparecem no mesmo ato | há uma forma só depois da `DOM-T3`; manter dois vocabulários de violação é a duplicação que a auto-auditoria proíbe |
| `D-16` | O resíduo de forma anterior no **que o instrumento e a gramática dizem de si mesmos** (docstring e `--help` de `modelo.py`; preâmbulo da seção `## Gramática legível por máquina` da skill) é reparado por **card próprio**, a `DOM-T3a`, despachada logo depois da `DOM-T3` — e não por ampliação da `DOM-T6` | decisão do consultor de plano no escalonamento `ESC-1`, 2026-09-20. Ampliar a `DOM-T6` misturaria documentação pública com interior de instrumento e skill, quebraria o `Fora do escopo` dela e adiaria para o fim do plano um defeito que a `DOM-T4` e a `DOM-T5` leem enquanto trabalham (`AE-2`, `AE-5`) |
| `D-17` | **Toda contingência que cria arquivo declara esse arquivo nos `Arquivos-alvo` do card e exige a declaração da ativação na linha de retorno**; card cuja contingência só possa ser cumprida criando arquivo não declarado está incompleto | decisão do consultor de plano no `ESC-1`, 2026-09-20, sobre o `AE-6`: a contingência 2 da `DOM-T3` criou `tests/fixtures/modelo/plano-invalido-2.md` sem declará-lo, e a evidência mecânica saiu com escopo `aberto` e o arquivo `sem-atribuicao` — exatamente no regime de commit por marco, em que a atribuição é o que separa uma entrega da outra |
| `D-18` | A divergência de um token entre o bloco literal de um card e o que foi publicado na árvore é reparada por **card próprio**, a `DOM-T3b`, e não por cláusula pendurada num card de outro assunto | decisão do consultor de plano no escalonamento `ESC-2`, 2026-09-20 (`AE-8`). Nenhum dos cards restantes toca `.claude/tools/modelo.py`, e foi exatamente o "não ter onde cair" que produziu o `AE-5`. O custo de um despacho xlow é menor que o de publicar uma referência cruzada errada no instrumento que o kit inteiro lê |
| `D-19` | Os `Arquivos-alvo` passam a ter **um caminho puro por bullet**, sem prosa nem símbolo na mesma linha; qualificação de região, faixa e justificativa vai em **sub-bullet** indentado | decisão do consultor de plano no `ESC-2`, 2026-09-20, sobre o `AE-9`: `review_evidence.py` leu `argparse.ArgumentParser` como caminho e deixou **6 literais** sem reconhecer, porque a forma vigente mistura caminho e prosa. Consertar a forma do plano é barato e não depende do `TK-66`; o instrumento fica para o tíquete |
| `D-20` | Card que muda texto normativo **publica bloco literal para cada ponto que manda mudar**; passo em prosa sobre texto normativo é defeito de autoria. Quem executa e encontra ponto sem bloco **não redige**: sinaliza `blocked` razão `premissa` | decisão do consultor de plano no escalonamento `ESC-3`, 2026-09-20 (`AE-10`). A `DOM-T5` mandava, em prosa, "trocar a rastreabilidade de orações por rastreabilidade de operações"; o quarto ponto do planejador nem citado estava, e reescrevê-lo exigia redigir a gramática de `OP-<n>` que nenhum bloco fornecia. Terceira falha seguida da mesma família — `AE-8` (fidelidade), `AE-10` (ponto sem bloco) —, e a única que produziu `blocked` |
| `D-21` | O quinto ponto de `pantonic-reviewer.md` — o passo 7, `Retorno ao chamador` — é reparado por **card próprio**, a `DOM-T5a`, e **não** por cláusula pendurada na `DOM-T6` | decisão do consultor de plano no escalonamento `ESC-4`, 2026-09-20 (`AE-11`). A `DOM-T6` é `medium` e o tema dela é a porta de entrada e o `README.md`; o passo 7 é definição de conduta, tema da `DOM-T5`. Pendurar assunto alheio num card é como o `AE-2` nasceu, e a mesma opção já foi rejeitada no `ESC-1` |
| `D-22` | **Aceite de fidelidade é comando no repositório, nunca frase do executor sobre si mesmo.** A declaração `fidelidade conferida:` continua, como **sinal** na linha de retorno e em `Passos`; o `Pronto quando` e a `Verificação` se apoiam só em comandos re-deriváveis | decisão do consultor de plano no `ESC-4`, 2026-09-20, sobre o `AE-12`: os treze blocos da `DOM-T5` bateram byte a byte, mas **duas das treze** declarações trouxeram contagem errada (`reviewer-5a` 5 contra 7; bloco `E` 9 contra 12). Aceite ancorado ali teria reprovado entrega correta — ou aprovado entrega errada |
| `D-23` | A cadeia do retorno do revisor é reparada **de ponta a ponta num card só**, a `DOM-T5b`, com a tabela emissor → meio → consumidor declarada e **exaustiva**; um **sexto** ponto da mesma família, se aparecer, não vira sexto card: vira **replanejamento** | decisão do consultor de plano no escalonamento `ESC-5`, 2026-09-20 (`AE-14`). `AE-11` e `AE-14` são o mesmo defeito em dois pontos da mesma interface, e o padrão que os produziu é o plano ter mudado um **protocolo entre papéis** com cards escopados **por arquivo** — nenhum card era dono do protocolo inteiro. A tabela da `DOM-T5b` é a correção do padrão, e o tripwire é o custo de ela estar errada |
| `D-24` | A subseção `### 1.3 Mudanças do modelo` **sai** da seção do modelo | dono, 2026-09-20, verbatim: *"Mudanças, na forma descrita, não deve ser parte do modelo, ele a descrição indica um evento, e eventos são ocorrências que alteram o estado do modelo. O estado do modelo é definido por duas variáveis: os objetos trabalhados, e o fluxo de operações nos quais esses objetos participam."* Evento não é estado |
| `D-25` | No lugar de mudanças entram **propriedades**: os objetos entram com propriedades iniciais e o fluxo de operações as altera; as propriedades finais são o estado desejável do modelo | dono, 2026-09-20, verbatim: *"No lugar de 'mudanças', deve entrar 'propriedades'. Um modelo de modelo inicia com os objetos com certas propriedades, e, por meio do fluxo de operações, essas propriedades se alteram, sendo geralmente as propriedades finais o estado 'desejável' do modelo."* |
| `D-26` | O **aceite do plano passa a ser modelável**: o plano só é bem-sucedido se o estado final real for o especificado, e a confrontação dos dois é a validação da mecânica | dono, 2026-09-20, verbatim: *"por meio das propriedades é possível modelar o 'aceite' do plano: o plano somente será bem sucedido se o estado final for o especificado no modelo"*; e *"A validação da mecânica será evidente apenas pela confrontação do estado final do modelo real com o estado final modelo conceitual, e essa diferença é de valor para o cliente."* |
| `D-27` | Tarefa **fora** do modelo é legítima: faz-se, e mantém-se de forma **transparente**. **Isto contradiz a `V2` vigente**, que exige campo `Operação do modelo` em toda tarefa do plano; a contradição é declarada aqui e a forma de materializá-la é questão aberta (`Q-6`) | dono, 2026-09-20, verbatim: *"As tarefas resultantes que não estejam abrangidas no modelo significam que não tem interesse para o usuário/gerente do projeto/domain expert, e devem ser realizadas, sim, mas devem ser mantidas de forma transparente."* |
| `D-28` | A elaboração do modelo é **mecânica**, com entrada de dados declarada: **objetos, operações, estado inicial e estado final** | dono, 2026-09-20, verbatim: *"fica mecânico a elaboração do modelo: ele demandará uma entrada de dados: objetos, operações e estados inicial e final."* |
| `D-29` | **Versionamento**: emenda ao modelo **versiona, não reescreve**; o drift é apresentado no marco seguinte e avaliado ali; validado, cabe **merge** das versões | dono, 2026-09-20, verbatim: *"Se um agentes escrever uma emenda ao modelo original, o novo modelo deverá ser versionado. No final do plano, o 'drift' será avaliado se adequado ou não. Modelos são seres vivos que podem se alterar com base na evolução do projeto, mas um 'rewrite' não é adequado. O versionamento deve ser criado, apresentado no próximo marco, e, caso validado, aí pode ser feito um 'merge' nas versões."* |
| `D-30` | O **modelador perde a resolução de conflito**, que passa ao **consultor**: o modelador guarda o que recebe e versiona; quem tem o cenário decide a pertinência | dono, 2026-09-20, verbatim: *"Deixe a resolução de conflitos com o consultor. Se o agente model designer consegue versionar mudanças, ele pode guardar as informações recebidas, e deixar para o agente apropriado decidir. Não quero que o model designer seja mais um controle do processo. Sua função é ver o modelo, e não o projeto, por isso ele não tem o cenário completo para inferir se uma mudança é pertinente ou não."* **Tensiona `M-8`**, que dá ao modelador o ato de resolver conflito; a oração fica falsa quando o terceiro estágio fechar |
| `D-31` | O **teste do desenho é este plano**: o modelo dele seria `agente model designer` e `modelo`, com a operação *construir o modelo* devolvendo `modelo` no padrão esperado | dono, 2026-09-20, verbatim: *"Essa abordagem funcionaria neste plano em particular: nosso modelo seria o agente model designer e o modelo. Por meio da operação 'construir o modelo', receberiamos o 'modelo' no padrão esperado, facilmente testável e ajustável."* e *"Vamos começar por esse 'modelo de um modelo', e se a necessidade requerer outra forma de modelo, veremos no futuro."* |
| `D-32` | O terceiro estágio fica registrado **neste plano** — decisões `D-24`..`D-31` na §3 e a §13 —, por instrução explícita do dono. **Ressalva do consultor, para decisão dele:** o terceiro estágio muda o que o plano entrega (cai `### 1.3`, cai a resolução de conflito do modelador, cai a universalidade da `V2`), refaz as oito residências que os estágios 1 e 2 acabaram de publicar e invalida a leitura do Marco 2 antes de o dono a aceitar — o que, pela régua de convergência de iniciativa, é **plano novo** com o `P-0743` fechando no que entregou. A formulação está em §13.4 e sobe pelo relatório de encerramento | dono, 2026-09-20, verbatim: *"Gere novos cards no mesmo plano para continuar no próximo contexto o terceiro estágio do 'modelo', e das responsabilidades revistas do 'model designer'"* |
| `D-33` | **O que é propriedade.** Propriedade é a característica **observada** de um objeto: a que o processo altera, **ou** a que o processo tem de manter e por isso precisa ser vigiada. O critério de entrada é o **interesse para o modelo** — característica que não interessa ao dono não é propriedade e não entra. Exemplo do dono, para calibrar granularidade: no plugin de *re-anchoring* do PantonicVideo, as propriedades são **tempo/timestamp** e **propriedades de Capcut**; o estado inicial é o timestamp inicial das âncoras mais as propriedades de Capcut dos assets, e o estado final são âncoras com novos timestamps, assets solidários a esses timestamps, e propriedades de Capcut **mantidas** | dono, 2026-09-20, verbatim: *"Propriedade são caracteristicas que serão alteradas no processo, e caracteristicas de interesse para o modelo, sendo por isso, observadas."* |
| `D-34` | **Teste do que é objeto e do que é operação, e ele é decidível.** **Objeto é o que possui propriedade. Operação não possui propriedade** — operação é o que **altera** a propriedade do objeto. Se aparecer propriedade numa operação, a operação está mal recortada e **deve ser decomposta em um objeto mais uma operação nova**. O método de descoberta é este, e não a intuição: identificam-se as propriedades, e delas caem objetos e operações por decomposição | dono, 2026-09-20, verbatim: *"Um objeto é o que possui propriedade. Uma operação não possui propriedade. Se existe propriedade na operação, a operação deverá ser decomposta em um objeto + uma nova operação. Operação é o que altera a propriedade do objeto. Você descobre objeto e operação por decomposição e identificação das propriedades."* |
| `D-35` | **Estado inicial e estado final.** O **estado inicial** é o *snapshot* do começo do plano, **antes** de ele ser implementado, e a finalidade dele é **calibrar as tarefas** — tarefa escrita sem conhecer o que será trabalhado é adivinhação. O **estado final** é o **desejo do dono**, e pode ser **quantificável** (como os timestamps do exemplo) **ou apenas qualificável** — neste plano o modelo é qualitativo: ele atende a requisitos, não é um valor | dono, 2026-09-20, verbatim: *"O estado inicial é o snapshot do início do plano, antes dele ser implementado. Sua finalidade é calibrar as tarefas do plano, afinal, tarefa sem conhecer o que será trabalhado é tentar adivinhar o seu trabalho. O estado final é o desejo do dono. Pode ser quantificável, como no caso dos timestamps, ou só qualificável, por exemplo, neste plano atual, o modelo é qualitativo. Ele atende aos requisitos, não é um valor."* |
| `D-36` | **Governança das versões vivas.** Havendo duas versões vivas, o **marco** busca validação em **duas instâncias, nesta ordem**: primeiro o **consultor**; validando ele, o **cliente**. Mudança de versão do modelo **é mudança da entrega**. Aceita pelo cliente, a versão nova passa a ser a **vigente** e a anterior passa a **obsoleta** | dono, 2026-09-20, verbatim: *"Quando há duas versões vivas, nos marcos deverá ser buscada a validação tanto do agente consultor, e, se ele validar, do cliente. Afinal, mudança de versão do modelo é modificar a entrega. Se a modificação for aceita pelo cliente, então esse modelo será o vigente, e o anterior passa a ser obsoleto."* |
| `D-37` | **Forma do versionamento** (decisão **tática**, delegada pelo dono e tomada pela orquestração em 2026-09-20). A seção `## 1. Modelo conceitual` do plano carrega **sempre o modelo vigente**, com o número de versão no cabeçalho, monotônico. Uma versão pós-drift **não sobrescreve**: nasce como bloco irmão, declarado **pendente de validação**, e as duas coexistem até o marco. Aceita, a pendente vira vigente e ocupa a seção; **a obsoleta não fica no plano** — a residência do histórico é o git, e o plano guarda só a linha que registra qual versão se tornou obsoleta, em que data e por aceite de qual versão. Recusada, a pendente é eliminada e a vigente permanece, sem marca. `modelo.py show` mostra a **vigente** por omissão; a diferença entre vigente e pendente é o que o marco apresenta | orquestração, 2026-09-20, por delegação: *"A forma do versionamento é tático, então deixo contigo."* |
| `D-38` | **Drift e medição são duas coisas distintas, e não se confundem.** **Medição** é o confronto dos **resultados do processo** contra o modelo; **drift** é a **variação do modelo** em si. À medida que o modelo varia, as informações originais se perdem ou se modificam — e é por isso que o drift importa. O confronto de estados que a `D-26` chama de validação da mecânica é **medição**, não drift | dono, 2026-09-20, verbatim: *"O confronto de estados não é drift, é medição. Drift é a variação do modelo. A medida que o modelo varia, mais as informações originais se perdem ou se modificam. Isso é um drift, e é relevante... Assim, medição se refere aos resultados, drift se refere ao modelo."* |
| `D-39` | **Modelo vigente e modelo obsoleto, e contra qual se mede.** A medição parte **sempre do último modelo vigente** e confronta os resultados do processo — **nunca do modelo obsoleto**. **Modelo obsoleto** é o modelo anterior ao drift, cujo modelo pós-drift foi **validado e aceito**. Drift **não aceito** não produz obsoleto: a versão nova é **eliminada** e a versão anterior aceita é **resgatada** | dono, 2026-09-20, verbatim: *"Se o drift não for aceito, deverá ser eliminada a versão nova, e resgatada a versão anterior aceita. A medição parte do último modelo vigente e confronta os resultados do processo, e não do modelo... E os resultados são medidos com base no modelo vigente, nunca com o modelo obsoleto. Modelo obsoleto é o modelo anterior ao drift, cujo modelo após o drift foi validado e aceito."* |
| `D-40` | **O ato `conflito` sai do modelador.** Como o modelador **não decide** qual é o modelo vigente — isso é do consultor em primeira instância e do cliente em segunda —, ele **não precisa registrar conflito**. Ele registra **apenas a versão com drift**: a versão que será avaliada | dono, 2026-09-20, verbatim: *"Remover o conflito, pois se o model designer não irá decidir qual é o modelo vigente (premissa do consultor na primeira instância, e cliente na segunda), então ele não precisa registrar isso. Ele só registra a versão com drift, a versão que deverá ser avaliada."* |
| `D-41` | **O que é conflito, e qual é a autoridade do consultor.** **Conflito é a existência de um modelo pós-drift e de um modelo vigente que não é o pós-drift.** O consultor **resolve** o conflito **quando recusa** o drift, declarando que o modelo pós-drift não é aceitável. Se ele entender que o drift é **pertinente**, ele **escala** — e não altera o modelo. **O consultor tem autoridade para recusar um drift; não tem autoridade para alterar o modelo sem escalar ao cliente.** Consequência: o modelador continua sendo o **único** que escreve no modelo, e a `M-9` não cai | dono, 2026-09-20, verbatim: *"O conflito é a existencia de um modelo pós-drift e um modelo vigente, que não é o pós-drift. O consultor resolve se ele recusar o drift, dizendo que o modelo pós-drift não é aceitável. Se o consultor entender que o drift é pertinente, então ele escala. Ele não tem autoridade de alterar o modelo sem escalar para o cliente, mas tem autoridade para recusar um drift."* |
| `D-42` | **Tática e estratégia, e o que "transparente" quer dizer.** **Tarefa sem lastro no modelo de operação é tática; tarefa com lastro é estratégia.** Tarefa tática é legítima e se executa. **Transparência é não apresentar questão tática nos resultados nem nas decisões — ou deixá-la como apêndice do relatório.** Isto fecha a `Q-6`: a `V2` **não** vira violação de outra classe; o que muda é o **que sobe ao dono**, não o que se permite no plano. Caso medido que originou a regra: o `docs/OPERACOES_AS_IS.md` de 826 linhas, cujas seções o dono não recusou como entrega — recusou como **apresentação**, por serem táticas | dono, 2026-09-20, verbatim: *"Eu não recusei aquelas entregas, eu reclamei de estar sendo apresentado questões táticas, e não estratégicas. Tarefa sem lastro no modelo de operação é tática. Tarefa com lastro no modelo de operação é estratégia. Transparência é não apresentar questões táticas nos resultados ou decisões, ou deixá-los como apendices nos relatórios."* |
| `D-43` | **O que é um marco, e para que ele serve.** Marco é a **subdivisão de um plano grande que seja mensurável pelo cliente**: um **estado intermediário** entre o inicial e o final, do qual se possa **inferir que o final está sendo atingido**. Entrega que o cliente não consegue visualizar **não é marco** — o exemplo do dono: no PantonicVideo, concluir contratos não era marco; ver a interface e ver os plugins funcionando eram. E o marco é **detector de desvio, não só ponto de passagem**: indo de `0` a `10`, chegar a `5` é o marco da metade; chegar a `−100` diz que o processo **já falhou**, sem que seja preciso esperar o término do plano | dono, 2026-09-20, verbatim: *"Marco representa uma subdivisão de um plano grande e mensurável pelo cliente... Assim, marco será um estado intermediário entre o inicial e o final, e que possa inferir que o final está sendo atingido... Mas, se depois de meio processo, o número for -100, indica que houve um desvio sério. Não precisa chegar ao término do plano para concluir o desvio. O processo já teria falhado no marco intermediário."* |
| `D-44` | **Ordem entre versionar e guardar** (decisão **tática**, delegada pelo dono e tomada pela orquestração em 2026-09-20). **O versionamento vem primeiro, e não há guarda provisória.** Enquanto o versionamento não existir, o modelador **não aceita ato que produza drift**: exerce apenas a autoria. Não se cria depósito temporário para a informação recebida — depósito temporário vira permanente, e este plano já mediu quatro vezes o custo de ad-hoc que virou doutrina por ter funcionado uma vez. Consequência de planejamento: **o card do versionamento é o primeiro do terceiro estágio** | orquestração, 2026-09-20, por delegação: *"É uma decisão tática, deixo contigo."* |
| `D-45` | **O terceiro estágio fica no `P-0743`.** A recomendação de abrir plano novo — do consultor e da orquestração, com o argumento de que o estágio refaz as oito residências que os estágios 1 e 2 publicaram — foi **apresentada e recusada**. A `D-32` fica confirmada e a ressalva dela, encerrada. O plano segue sendo um só, de `DOM-T1` a `DOM-T13` | dono, 2026-09-20, verbatim: *"Manter plano."* |
| `D-46` | **A `Q-12` fecha, e fecha como questão de apresentação — não de mecanismo.** A `V2` **não se toca**: segue exigindo o campo `Operação do modelo` em toda tarefa do plano, e nenhuma regra do instrumento afrouxa. O que a `D-42` chamou de tática é **matéria de relatório**, e a resolução é migrá-la para **apêndice**. Consequência de conduta, vinculante para a orquestração: o corpo de todo relatório carrega o que tem lastro no modelo, e o que é tático desce para apêndice — não some, não sobe. Leitura da orquestração registrada para correção do dono, caso divirja: em plano bem formado toda tarefa cita operação, logo *"tarefa sem lastro"* é categoria de **relato**, não de plano | dono, 2026-09-20, verbatim: *"Q12, você pode migrar questões táticas para apendice do relatorio."* |
| `D-47` | **Destino da divergência que o revisor apura — fecha a `Q-11`** (decisão **tática**, delegada pelo dono e tomada pela orquestração em 2026-09-20). A divergência que o revisor acha no passo `5a` é **medição** (`D-38`), e medição **não é ato de modelo**: ela sai como **achado de alvo `modelo` no laudo**, e **nada mais viaja na linha de retorno do revisor**. A razão é que a medição admite duas leituras — ou a **entrega** errou, ou o **modelo** deixou de descrever o que o plano entrega — e o revisor não tem cenário para distinguir. Quem tem é o **consultor**: a orquestração roteia o achado a ele, que **recusa** (e recusar resolve, `D-41`) ou **escala ao cliente**, sem alterar o modelo. Aceito pelo cliente, o **modelador** escreve a versão pós-drift por `Ato: emenda` — ele segue sendo o único escritor e a `M-9` não cai. **Consequências:** (i) o ato `conflito` **deixa de existir** e o modelador passa a ter **três** atos — `autoria`, `emenda`, `leitura` (`D-40`); (ii) o **revisor deixa de ser produtor de dossiê**, e o edit do passo 7 dele, entregue pela `DOM-T5a`, fica sem uso próprio — permanece como forma geral, sem custo, e não se reverte; (iii) o transporte construído pela `DOM-T5b` **não se perde**: é por ele que `autoria` e `emenda` chegam ao modelador, vindas do planejador e do consultor; (iv) a confrontação de estado final da `D-26` é **medição de marco**, de outra granularidade que a medição por tarefa, e as duas não se confundem | orquestração, 2026-09-20, por delegação: *"Q11 deixo para você responder."* |
| `D-48` | **O token do registro do ato é forma, não papel — e o Marco 3 é o dono dele.** As linhas da árvore que mandam o modelador devolver a linha `MD-<n>` (`GOVERNANCA.md` 95 e 388; `pantonic-planner.md` 165-168 e 180-191; `pantonic-model-designer.md` 15, 28-30 e 42-77) descrevem **a forma do que o modelador devolve**, e essa forma é exatamente o que o terceiro estágio substitui — o registro de versões da `### 1.4`. Elas são reparadas **neste estágio**, por dois cards corretivos: `DOM-T8a` (norma e planejador) e `DOM-T9a` (modelador). **Como isto não repete o `AE-11`:** o `AE-11` é publicar metade de uma mudança de **papel**; aqui **nenhuma atribuição de papel muda** — cada linha tocada conserva verbatim quem faz o quê, inclusive o ato `conflito`, que só desaparece no Marco 4 (`D-47`). O eixo do corte é forma × papel, e o teste é mecânico: depois dos dois cards, nenhuma linha da árvore diz que um papel faz algo que outra linha nega | decisão do consultor de plano no escalonamento `ESC-6`, 2026-09-20 (`AE-17`). A alternativa — deixar o token sobreviver até o Marco 4 — foi descartada por fato medido: a `DOM-T10` **despacha o modelador**, que lê a própria definição antes de agir; com a definição na forma anterior, ele devolve `### 1.3 Mudanças do modelo` e a contingência 1 da `DOM-T10` bloqueia. O token órfão não é dívida doutrinária: é defeito no caminho da entrega que o Marco 3 mede |
| `D-49` | **A `Q-11` e a `Q-12` estão fechadas, e isso não abre os Marcos 4 e 5.** A `D-47` fecha a `Q-11` e a `D-46` fecha a `Q-12`; as tabelas de §13.3 e §13.5 ficaram para trás e passam a carregar a nota de superação. A trava vigente dos Marcos 4 e 5 é **uma só**, e é a primeira razão da §13.5: a régua da `D-43` — marco é detector de desvio, e escrever card de Marco 4 antes do `go` do Marco 3 é gastar antes do detector. Todo card deste estágio mantém `tudo que muda papel (Marco 4)` fora de escopo, **pela régua do marco**, não por questão aberta | decisão do consultor de plano no escalonamento `ESC-6`, 2026-09-20. O `AE-17` escalou sobre a premissa *"a `Q-11` está aberta"*, medida falsa desde a `D-47` do mesmo dia: a contradição viva entre a §3 e a §13 é o que a produziu, e fechá-la aqui evita que o próximo card a herde |
| `D-50` | **Cláusula de `Pronto quando` com escopo de seção ou de arquivo exige censo medido.** Cláusula do tipo *"nenhuma linha de X descreve Y"* só entra num card se a `Verificação` trouxer um comando que **percorra X inteiro**, com o número de hoje e o número esperado. Sem esse comando, a cláusula não tem poder discriminante e cai em juízo do executor sobre a própria entrega (`I-11`). Os quatro cards abertos do estágio recebem o censo | decisão do consultor de plano no escalonamento `ESC-6`, 2026-09-20, sobre o achado irmão do `AE-17`: a cláusula da `DOM-T7` tinha escopo da `### 3.2` inteira e o único instrumento dela alcançava um heading só — a linha 388 passava por baixo |
| `D-51` | **Residência é o arquivo da árvore; seção de plano é insumo literal de card.** Nenhuma seção deste plano é residência de texto doutrinário **depois** da transcrição — a residência é `GOVERNANCA.md` §3.2, a skill `diario-de-obras` ou `.claude/tools/modelo.py`, conforme o caso, e é essa a fórmula que os preâmbulos das §4, §5 e §6 já usavam. Quando um estágio posterior substitui **parte** do texto transcrito, valem três atos, e nenhum deles é reescrever a seção antiga: (i) a seção antiga leva **nota de superação** apontando a nova, e o bloco cercado dela fica intacto, porque é o registro do que um card fechado transcreveu — reescrevê-lo falsificaria o diff de aceite daquele card; (ii) a seção nova leva a **mesma fórmula** de preâmbulo, dizendo de que card é insumo e qual arquivo é a residência; (iii) **o ponteiro que a árvore carrega passa a nomear a seção vigente**, e esse ato tem card. Consequência imediata: a §15 governa a gramática onde ela e a §5 divergem, e a `DOM-T8a` corrige o ponteiro do preâmbulo da skill | decisão do consultor de plano no escalonamento `ESC-7`, 2026-09-21 (`AE-18`). O defeito nasceu de duas fórmulas de preâmbulo convivendo: as §4-§6 diziam *"residência única **depois** da transcrição: `<arquivo>`"*, e as §14-§16, escritas no replanejamento, diziam *"residência única"* sem o complemento — lidas juntas, duas seções do mesmo plano reivindicavam o mesmo texto. A `Restrição` da `DOM-T8` fechou o ponteiro por decisão (*"a §15 é continuação dela, não substituição"*), e a medição do revisor mostrou a premissa falsa: é substituição em quatro das seis linhas |
| `D-52` | **Quem grava a `## 1. Modelo conceitual` no arquivo é o modelador, e só ele — a `DOM-T10` não tem mão nessa região.** A `DOM-T9a` tornou vinculante o gate `modelo.py check` exit `0` no ato do modelador, e esse gate **exige que ele grave**: não há como sair `0` sobre seção que não está no arquivo. Logo a precedência não é escolha — está decidida pela norma (`M-9`, `D-5`: nenhum outro papel escreve ali) e agora pelo instrumento. Consequências, todas na `DOM-T10`: (i) a seção **sai dos `Arquivos-alvo`**, e o único alvo do card passa a ser o campo `Operação do modelo` dos cards; (ii) o card é **dois atos com gate entre eles** — ato 1 devolve o dossiê e sinaliza `blocked` razão `dependencia`; ato 2 converte os campos; (iii) **o aceite discrimina pelo estado de entrada do ato 2**: o primeiro comando, antes de qualquer edição, é `modelo.py check --plano`, que tem de sair `1` com **17** violações, **todas** `V2`. Esse estado é impossível no caminho errado — antes do ato do modelador o mesmo comando sai `2` com `modelo: forma anterior`, e depois da conversão sai `0`; (iv) o despacho do modelador é **ato do loop**, e consta do registro dele: a prova de que a outra mão agiu **não** é testemunho do executor | decisão do consultor de plano no escalonamento `ESC-9`, 2026-09-21 (`AE-21`). Medição que a fechou: `violacoes_id` do instrumento indexa `V2`, `V4` e `V14` pelo `<ID>` da tarefa — são as três violações que moram no **card**, não na seção; **toda outra violação é da seção**. **Correção do `ESC-10` (`AE-22`):** esta linha dizia *"todas as demais são indexadas por `OP-<n>` ou `secao`"*, e a enumeração estava **incompleta** — o instrumento emite **quatro** tokens de índice, e o quarto é `objeto` (`V6`, `V7`, `V15`, `V17`). A fronteira **não muda** (o que é do card continua sendo `<ID>`); o que muda é a frase que a descrevia por enumeração em vez de por complemento |
| `D-53` | **O gate do modelador é sobre o que ele escreve, não sobre o que ele não pode escrever.** *"Só devolve com exit `0`"* é inalcançável na conversão de um plano para a forma nova: gravada a seção, o `check` acusa `V2` em toda tarefa que ainda cita `Oração do modelo`, e essas linhas moram nos cards, que o modelador **está proibido de tocar** (`M-9`). Era gate que se fecha corrigindo o que não é seu — deadlock medido no `ESC-9`, **antes** do despacho, e da mesma família do `AE-19`: aceite inalcançável por construção. O gate passa a ler: exit `0` devolve; exit `1` com violação de **seção** (`OP-<n>`, `secao`) é ato não concluído e ele corrige; exit `1` com violação indexada por `<ID>` de tarefa (`V2`, `V4`, `V14`) **não é dele** — devolve o ato com a **saída literal** do `check`, e quem conduz roteia para a tarefa que converte os cards. Residência: `.claude/agents/pantonic-model-designer.md`, linhas 22-24; card `DOM-T9b`, literal na §19. **Emendada pelo `ESC-10` (`AE-22`):** *"violação de seção (`OP-<n>`, `secao`)"* omitia a família `objeto` — `V6`, `V7`, `V15` e `V17`, que são de `### 1.1 Objetos` e `### 1.3 Estado` e **são do modelador**. O ramo passa a ser definido por **complemento**: seção é tudo que não é indexado pelo `<ID>` de uma tarefa. Literal corrigido na §20, card `DOM-T9c` | decisão do consultor de plano no escalonamento `ESC-9`, 2026-09-21. Sem isto, a `DOM-T10` trava no primeiro despacho do modelador, e ele não tem protocolo de `blocked` para sair |
| `D-15` | `tests/fixtures/modelo/plano-valido.md` é **renomeado** para `plano-forma-anterior.md` e passa a ser a fixture do exit `2` de forma anterior | a fixture já é um plano válido na forma anterior; renomeá-la é mais barato e mais fiel que escrever outra |
| `D-54` | **Literal de aceite de bloco se extrai do bloco, linha a linha, e se mede antes de publicar; proposição que atravessa a quebra vira dois greps, um por linha.** Três consequências imediatas, todas nesta rodada: (i) a `Verificação` da `DOM-T9c` passa a conferir o bloco `T2` por **seis** literais, cada um contido integralmente em **uma** linha da §20 — 4163 (borda de cima), 4164 e 4165 (os dois greps da proposição partida), 4166, 4168 e 4171 (borda de baixo) —, e nenhum literal do card atravessa quebra; (ii) todo número publicado por esta rodada é **par medido**, o valor na árvore e o valor no texto anterior, nunca um valor só nem valor deduzido; (iii) a rodada que corrige um literal **audita todos os literais dos cards abertos pelo mesmo critério**, e os dois defeitos achados caem no mesmo ato — o `### 1.3` da `DOM-T10`, que sem âncora imprime `9` hoje e passaria antes de a tarefa começar, e o censo `modelo de domínio` da `DOM-T6`, cuja linha de base declarada era `0` e é `1`, mais o `sed` de fidelidade da §8.1, que terminava em `^## 9\.` e por isso imprimia duas linhas a mais que o bloco cercado | `AE-23`: a `I-15` existe desde o `ESC-8` e **não foi aplicada ao bloco que nasceu depois**, no `ESC-10` — o literal de entrada do `T2` foi derivado da frase, atravessou a quebra 4164/4165 e ficou insatisfazível junto com a `I-3`, custando um despacho inteiro. Invariante escrito não basta: o autor do bloco **roda** cada literal antes de publicar, e a rodada corretiva varre o resto dos cards abertos em vez de corrigir só o que bloqueou (`I-15`, `I-5`, `I-16`) |

### 3.1 A fenda entre julgar e escrever — mitigações enumeradas

A fenda é medida, não hipotética (`F-1`): a confirmação é juízo do revisor no ato do laudo, e um
agente separado que escreve põe um round-trip exatamente ali. Seis mitigações possíveis, com a
escolha e a razão:

| id | mitigação | veredito | razão |
|---|---|---|---|
| `MIT-1` | **Andamento derivado, nunca gravado** (`D-2`) | **escolhida** | elimina a escrita do caminho feliz: não há o que gravar no ato do laudo, logo não há round-trip. É a mitigação que fecha a fenda por construção, não por processo |
| `MIT-2` | **Divergência do revisor vira achado de alvo `modelo`**, rota que já existe desde a `MC-T1` | **escolhida** | o juízo fica onde nasce (o laudo), a escrita fica com o modelador, e nada no meio do caminho precisa de ferramenta nova nem de mudança no gerador de laudo |
| `MIT-3` | **Dossiê `Ato de modelo` fechado, de seis campos, devolvido na linha de retorno** | **escolhida** | torna o acionamento uma via só: quem julga não conversa com quem escreve, entrega um pedido completo. Sem isso o round-trip vira diálogo, que é o custo real |
| `MIT-4` | O modelador **devolve a seção inteira, literal**, e quem recebe transcreve sem parafrasear | **escolhida** | fecha a segunda metade da fenda: o intermediário não interpreta o que o modelador decidiu |
| `MIT-5` | O revisor mantém `Edit` e grava ele mesmo, com o modelador só para conflito | **rejeitada** | é a origem da fenda e contradiz a decisão do dono de um agente dono de **todas** as operações do modelo |
| `MIT-6` | O revisor despacha o modelador de dentro do próprio contexto, sincronamente | **rejeitada** | inviável na plataforma: nenhuma lista `tools:` do kit tem ferramenta de despacho (`F-2`) |

**O que sobra de fenda, e por que é aceitável.** Depois de `MIT-1`..`MIT-4`, o único ato de
escrita que resta é a **mudança de texto do modelo** — e essa é juízo de domínio puro, que é
precisamente o que o dono quis concentrar num agente só. O intervalo entre o laudo que aponta a
divergência e o ato do modelador não trava nada, porque o andamento é derivado: o plano continua
legível, o estágio continua correto e nenhum gate fecha em falso enquanto a emenda não chega.

---

## 4. Norma do modelo de domínio (texto literal para `GOVERNANCA.md` `### 3.2`)

> Residência **depois** da transcrição pela `DOM-T1`: `GOVERNANCA.md` §3.2, substituindo
> integralmente as linhas 320..356. Este plano não recopia o texto após a transcrição; o bloco
> abaixo é o insumo literal do card.
>
> **Superada em parte pela §14** (terceiro estágio, `DOM-T7`, 2026-09-20), que substituiu três
> parágrafos deste bloco na residência. Onde as duas divergem, **governa a §14** (`D-51`). O bloco
> abaixo **não se reescreve**: é o registro do que a `DOM-T1` transcreveu, e o diff de aceite dela
> se faz contra ele.

```markdown
### 3.2 O modelo de domínio do plano

**O que é.** Todo plano carrega, logo depois de `## 0. O problema, verbatim`, a seção
`## 1. Modelo conceitual`: a descrição, em linguagem corrente, do que o plano entrega, escrita como
**objetos** e **operações encadeadas** sobre esses objetos. São três blocos, nesta ordem: a tabela
de **objetos** (`### 1.1 Objetos`), com o contrato de cada um e a operação que o produz; o **fluxo
de operações** (`### 1.2 Fluxo de operações`), numeradas `OP-<n>`, cada uma nomeando quem age, o
que faz e de que objetos precisa; e a **lista de mudanças** (`### 1.3 Mudanças do modelo`),
`MD-<n>`. É um objeto único: uma cópia, dentro do plano, do primeiro rascunho ao fechamento. A
gramática que o instrumento lê mora na skill `diario-de-obras` (*Gramática legível por máquina*,
"Modelo de domínio (seção do plano)").

**Para quem é.** O modelo é a interface entre o dono e o loop. Quem lê só o modelo entende o que o
plano entrega, **em que estágio está** e o que mudou desde a última leitura. Por isso o texto de
uma operação não carrega crase, barra, caminho de arquivo, sigla nem identificador técnico — o
instrumento recusa crase e barra (`V12`); o resto é dever de autoria. Máximo de 40 operações por
plano.

**Estágio, não status.** O andamento é **derivado e nunca gravado**. Uma operação está `concluída`
quando todas as tarefas que a materializam estão `done` ou `cancelled`; está `em curso` quando
alguma está `in-progress` ou `review`; está `prevista` nos demais casos. O **estágio atual** do
plano é a primeira operação que não está `concluída`, e é `concluído` quando não há nenhuma.
Nenhum papel escreve estado no modelo: `modelo.py show` o deriva do andamento das tarefas, e é a
única fonte da leitura do dono.

**O contrato chega ao card.** Todo card carrega o campo `Operação do modelo` com as operações que
materializa, o texto de cada uma copiado e a linha `precisa de` trazendo cada objeto com o contrato
dele, copiado da tabela de objetos. É por esse campo que o executor sabe, sem abrir o plano, em que
estágio está e do que precisa.

**Quem escreve.** Um agente único — `pantonic-model-designer` — é dono de **todo** ato sobre o
modelo: autoria, emenda, resolução de conflito entre o texto e a entrega, e explicação de contexto.
Nenhum outro papel escreve na seção `## 1. Modelo conceitual`.

| papel | o que faz diante do modelo |
|---|---|
| modelador | escreve a seção inteira, em todo ato; devolve a seção literal e a linha `MD-<n>` que registra o ato |
| planejador | escreve o plano sem a seção do modelo e devolve o dossiê `Ato de modelo` de autoria junto com o plano gravado; o plano não vai ao Marco 1 sem a seção escrita pelo modelador e sem `modelo.py check` exit `0` |
| consultor | devolve o dossiê `Ato de modelo` de emenda junto com o reparo do escalonamento, quando a decisão muda o que o plano entrega |
| revisor | **não escreve**; divergência entre a entrega e o texto de uma operação vira achado de processo de alvo `modelo` (`docs/RUBRICA_DE_REVISAO.md` §6) |
| executor | **não escreve**; lê a operação e o contrato no card |
| orquestração | **não escreve**; despacha o modelador ao receber um dossiê `Ato de modelo`, roda `modelo.py check` antes de despachar e antes de fechar cada tarefa (exit `1` bloqueia; exit `2` = forma anterior, segue com nota) e abre o relatório de encerramento e cada marco com `modelo.py show` |
| dono | lê o modelo no Marco 1 de todo plano e a leitura gerada pelo instrumento em cada marco e relatório |

**Nenhum agente aciona outro agente.** Papel que precisa de um ato de modelo **devolve o dossiê na
própria linha de retorno**; quem conduz a sessão o despacha. O dossiê é fechado e tem seis campos:
`Plano`, `Ato` (`autoria`, `emenda`, `conflito` ou `leitura`), `Motivo` com o identificador da
decisão ou do achado, `Fato novo` em uma frase, `Restrição` e `Devolver`.

**Retroatividade.** Plano sem a seção `## 1. Modelo conceitual`, e plano com a seção na **forma
anterior** — frases `M-<n>` com estado gravado —, são forma anterior: `modelo.py check` sai `2`
para eles e o loop segue. Nenhum plano é migrado. Caso medido de origem: diretiva do dono de
2026-09-20 sobre o Marco 2 do `P-0741`.
```

**Linha nova da matriz de responsabilidades de `GOVERNANCA.md` §3 (texto literal), inserida depois
da linha `**Revisão**`:**

```markdown
| **Modelagem** | O mais poderoso disponível (Opus) — escrever o modelo de domínio de um plano é julgamento de domínio, e a consistência entre planos é o que um agente único compra | **Todo** ato sobre o modelo de domínio do plano (§3.2): escrever a seção na autoria, emendá-la quando uma decisão muda o que o plano entrega, resolver conflito entre o texto e a entrega e explicar o contexto do modelo a quem pergunta; devolve a seção literal e a linha de mudança que registra o ato (`pantonic-model-designer`) | Não planeja, não executa, não julga entrega e não escreve nenhuma outra linha do plano; não é acionado por outro agente — recebe despacho de quem conduz a sessão |
```

**Substituições nas três linhas de papel que citam o modelo (texto literal do trecho a trocar):**

| linha | trecho vigente | trecho novo |
|---|---|---|
| `**Planejamento**` | `**o modelo conceitual do plano** (§3.2), escrito antes da decomposição e emendado em rodada de replanejamento` | `**o dossiê de ato de modelo** (§3.2): o planejador não escreve a seção do modelo — devolve o dossiê de autoria junto com o plano gravado, e o de emenda em rodada de replanejamento` |
| `**Revisão**` | `**confirma e emenda o modelo conceitual** do plano (§3.2) — sua única escrita fora do laudo` | `**não escreve no modelo de domínio** do plano (§3.2) — divergência entre a entrega e o texto de uma operação vira achado de alvo `modelo`, e a escrita é do modelador` |
| `**Orquestração**` | `roda `modelo.py check` antes de despachar e antes de fechar cada tarefa e abre o relatório e cada marco com `modelo.py show` (§3.2)` | `roda `modelo.py check` antes de despachar e antes de fechar cada tarefa, abre o relatório e cada marco com `modelo.py show` e **despacha o modelador** ao receber um dossiê de ato de modelo (§3.2)` |

**Emendas a `docs/RUBRICA_DE_REVISAO.md` (texto literal para a `DOM-T1`):**

Substituição integral da linha `modelo` da tabela de alvos da §6:

```markdown
| `modelo` | operação do modelo de domínio do plano que a entrega tornou falsa ou ambígua (`GOVERNANCA.md` §3.2); rota: dossiê `Ato de modelo` de conflito, devolvido junto com o laudo e despachado ao `pantonic-model-designer` por quem conduz a sessão — nunca corrigido pelo reviewer |
```

Substituição integral do parágrafo da §7:

```markdown
O reviewer marca dimensões, anexa achados e emite o laudo pelo gerador. O reviewer não corrige o que
aponta, não replaneja, não edita os arquivos da tarefa e não escreve percentual nem veredito. A
correção do que o laudo aponta pertence a uma execução seguinte, com o laudo em mãos. **O reviewer
não escreve fora do caminho do laudo**, e isso inclui o modelo de domínio do plano
(`GOVERNANCA.md` §3.2): divergência entre a entrega e o texto de uma operação vira achado de
processo de alvo `modelo`, e o texto fica como está até o modelador agir.
```

---

## 5. Gramática do modelo de domínio (texto literal para a skill `diario-de-obras`)

> Residência **depois** da transcrição pela `DOM-T2`:
> `.claude/skills/diario-de-obras/SKILL.md`, substituindo integralmente a subseção
> `### Modelo conceitual (seção do plano)` (linha 175, `F-12`). É a gramática que
> `.claude/tools/modelo.py` lê (§6, hoje §16).
>
> **Superada em parte pela §15** (terceiro estágio, `DOM-T8`, 2026-09-20), que substituiu **quatro
> das seis** linhas da tabela na residência — cabeçalho, objetos, operações e a linha de mudanças,
> que virou duas. Onde as duas divergem, **governa a §15** (`D-51`). Sobrevivem deste bloco a linha
> `| campo do card |`, o parágrafo de abertura e o `**Andamento, nunca gravado.**`. O bloco abaixo
> **não se reescreve**: é o registro do que a `DOM-T2` transcreveu.

```markdown
### Modelo de domínio (seção do plano)

Seção `## 1. Modelo conceitual` do plano (`GOVERNANCA.md` §3.2), delimitada pelo próximo heading de
nível 2. Dentro dela, nesta ordem:

| elemento | forma | regra |
|---|---|---|
| cabeçalho | `**Estado do modelo:** versão <n> · AAAA-MM-DD · autor: <papel> · <k> operações · última mudança: <MD-<n> \| nenhuma>` | linha única; obrigatória (`V13`) |
| objetos | `### 1.1 Objetos` + tabela `\| objeto \| o que é \| contrato \| origem \|`; `<objeto>` é um nome em linguagem corrente, único na tabela; `<origem>` é `externo` ou `OP-<n>` | obrigatória (`V13`); `<origem>` `OP-<n>` existe no fluxo (`V7`); objeto de origem `externo` é citado por alguma operação (`V6`) |
| operações | `### 1.2 Fluxo de operações`; cada operação é o par de linhas: `- **OP-<n>** — <texto>` e, na linha seguinte, `  - \`precisa de: <objeto>[, <objeto>]\` · \`tarefas: <ID>[, <ID>]\`` | numeração `1..k` na ordem do encadeamento, sem salto (`V8`); `<n>` único (`V11`); `<texto>` sem crase e sem `/` (`V12`); todo `<objeto>` existe na tabela de objetos (`V5`); toda `<ID>` existe como `### <ID> — …` no plano (`V3`); lista de tarefas não vazia (`V1`); operação com `<n>` maior que 1 cita ao menos um objeto de origem `OP-<m>` (`V9`), e esse `<m>` é menor que `<n>` (`V10`). Subtítulos `**A. …**` entre operações são livres e ignorados |
| mudanças | `### 1.3 Mudanças do modelo` + tabela `\| id \| data \| autor \| operações \| o que mudou e por quê \|`; linha `\| MD-<n> \| AAAA-MM-DD \| <papel> · <ref> \| OP-<a>, OP-<b> \| <texto> \|`; sem mudança, uma linha com `—` nas quatro primeiras células | obrigatória (`V13`) |
| campo do card | `- **Operação do modelo:** \`OP-<a>\`[, \`OP-<b>\`]` como campo de todo `### <ID> — …` do plano, seguido, por operação citada, de dois sub-bullets: `  - OP-<a>: <texto copiado>` e `  - precisa de: <objeto> — <contrato copiado>[; <objeto> — <contrato copiado>]` | obrigatório em toda tarefa do plano (`V2`); toda `OP-<a>` citada existe (`V4`); os dois sub-bullets existem para cada operação citada (`V14`) |

**Andamento, nunca gravado.** Nenhum elemento da seção carrega estado. `modelo.py show` deriva:
operação `concluída` quando todas as tarefas dela estão `done` ou `cancelled`; `em curso` quando
alguma está `in-progress` ou `review`; `prevista` nos demais casos. O **estágio atual** é a
primeira operação não `concluída`, e é `concluído` quando não há nenhuma.

Plano sem a seção `## 1. Modelo conceitual`, e plano com a seção mas sem o heading
`### 1.2 Fluxo de operações`, são **forma anterior**: `modelo.py check` sai `2` e nada se exige
deles.
```

---

## 6. Superfície do instrumento `modelo.py` (normativa; a `DOM-T3` a implementa)

> Residência **depois** da implementação pela `DOM-T3`: `.claude/tools/modelo.py`. O texto abaixo é
> o insumo normativo do card, não a documentação viva do módulo.
>
> **Superada em parte pela §16** (terceiro estágio, `DOM-T9`), que acrescenta seis violações, muda
> o literal da `V13`, acrescenta um exit e dois modificadores de `show`. Onde as duas divergem,
> **governa a §16** (`D-51`). O bloco abaixo **não se reescreve**: é o registro do que a `DOM-T3`
> implementou, e o ponteiro cruzado do docstring que ainda nomeia esta seção é reparado pela
> `DOM-T9`.

**Chamadas (inalteradas):**

```
python .claude/tools/modelo.py check --plano <caminho do plano> [--root <raiz do repo>]
python .claude/tools/modelo.py show  --plano <caminho do plano> [--desde AAAA-MM-DD] [--root <raiz do repo>]
```

`--root` default, carregamento de `backlog.py` por `importlib.util.spec_from_file_location`,
chamada a `backlog._parse_plano(Path(plano), Path(root))` e UTF-8 forçado por `_forcar_utf8`:
tudo preservado como está hoje (`F-4`). Nada de `backlog.py` é reescrito.

**Exit codes e forma de saída de `check`:**

| condição | exit | stdout / stderr |
|---|---|---|
| seção `## 1. Modelo conceitual` ausente | `2` | stdout: `modelo: ausente — plano anterior à doutrina (sem '## 1. Modelo conceitual')` |
| seção presente, heading `### 1.2 Fluxo de operações` ausente | `2` | stdout: `modelo: forma anterior — plano na forma de orações (sem '### 1.2 Fluxo de operações')` |
| seção e fluxo presentes, zero violações | `0` | stdout: `modelo: OK — <k> operações, <o> objetos, <t> tarefas, <m> mudanças` |
| seção e fluxo presentes, ≥ 1 violação | `1` | stderr: `modelo: FALHOU — <n> violação(ões)` e, uma por linha, `V<k> <sujeito> — <texto>` (sujeito = `OP-<n>`, `<ID>`, `objeto` ou `secao`) |

**Vocabulário fechado de violações.** Cada linha traz a substring literal que a saída imprime.
Forma fora desta tabela não bloqueia: é ignorada (subtítulo, prosa entre operações). Fronteira
contra o instrumento vizinho: `backlog.py check` julga cabeçalho e status das **tarefas**;
`modelo.py check` julga só a seção do modelo e o campo `Operação do modelo` dos cards; nenhum dos
dois repete a checagem do outro.

| código | condição | substring literal |
|---|---|---|
| `V1` | operação com lista `tarefas:` vazia ou ausente | `V1 OP-<n> — operação sem tarefa` |
| `V2` | tarefa do plano sem campo `Operação do modelo` ou com lista vazia | `V2 <ID> — tarefa sem operação` |
| `V3` | operação cita `<ID>` que não é heading de tarefa do plano | `V3 OP-<n> — tarefa inexistente <ID>` |
| `V4` | card cita `OP-<n>` que não existe no fluxo | `V4 <ID> — operação inexistente OP-<n>` |
| `V5` | `precisa de:` cita nome que não é linha da tabela de objetos | `V5 OP-<n> — objeto inexistente <nome>` |
| `V6` | objeto de origem `externo` que nenhuma operação cita em `precisa de:` | `V6 objeto — objeto externo sem uso <nome>` |
| `V7` | coluna `origem` cita `OP-<n>` que não existe no fluxo | `V7 objeto — origem inexistente <nome>` |
| `V8` | numeração das operações não é `1..k` na ordem do arquivo | `V8 OP-<n> — fora da sequência` |
| `V9` | operação com `<n>` maior que 1 cujo `precisa de:` não cita nenhum objeto de origem `OP-<m>` | `V9 OP-<n> — operação desencadeada` |
| `V10` | operação `OP-<n>` que cita objeto de origem `OP-<m>` com `<m>` maior ou igual a `<n>` | `V10 OP-<n> — objeto produzido depois <nome>` |
| `V11` | `OP-<n>` repetido | `V11 OP-<n> — identificador duplicado` |
| `V12` | texto da operação contém **backtick** (U+0060) ou **barra** (U+002F) — e só esses dois caracteres; letra acentuada do português não é violação | `V12 OP-<n> — literal técnico no texto` |
| `V13` | falta o cabeçalho `**Estado do modelo:**`, ou `### 1.1 Objetos`, ou `### 1.3 Mudanças do modelo` | `V13 secao — cabeçalho, objetos ou lista de mudanças ausente` |
| `V14` | card cita `OP-<n>` sem o sub-bullet do texto copiado ou sem o sub-bullet `precisa de:` | `V14 <ID> — contrato ausente para OP-<n>` |

**Ordem de emissão:** as violações de sujeito `OP-<n>` e `secao`, na ordem em que ocorrem no
arquivo; depois as de sujeito `objeto`, na ordem da tabela; depois as de sujeito `<ID>`, na ordem
das tarefas no plano. É a mesma disciplina de ordem do instrumento vigente.

**Forma de saída de `show` (fixa; `--desde` ausente = todas as mudanças):**

```
# Modelo de domínio — <P-NNNN> — <título do plano>
Estado do modelo: versão <n> · <data> · <k> operações · estágio atual: <OP-<j> — <texto> | concluído>

## Objetos
<tabela da §1.1, copiada verbatim>

## Fluxo
[concluída] OP-1 — <texto>
            precisa de: <objeto>[, <objeto>]
[em curso ] OP-2 — <texto>
            precisa de: <objeto>[, <objeto>]
[prevista ] OP-3 — <texto>
            precisa de: <objeto>[, <objeto>]

## Mudanças desde <AAAA-MM-DD | o início>
<linhas da tabela da §1.3 com data ≥ --desde, verbatim; sem nenhuma: nenhuma>
```

Os três rótulos têm largura fixa de **nove** caracteres entre colchetes — `[concluída]`,
`[em curso ]` e `[prevista ]`, onze com os colchetes —, e a linha `precisa de:` é indentada com
doze espaços, que é o que alinha o texto dela sob o texto da operação. Subtítulos `**A. …**` do
fluxo são reproduzidos como linha em branco seguida do subtítulo, para preservar a leitura por
blocos. Sobre plano de forma anterior, `show` imprime a mesma linha de `check` e sai `2`.

---

## 7. A leitura do dono — exemplo trabalhado

> Esta seção **não** é residência de forma: ela é uma **instância** da forma normativa da §6,
> preenchida com o modelo real do `P-0744` (`docs/plans/P-0744-spec-do-planejador.md` §1). Existe
> por dois motivos: é o que o dono julga no Marco 1, e é o worked example que a auto-auditoria
> exige — um por caso que as regras admitem. Os quatro casos de rótulo e estágio que a §6 admite
> estão instanciados nos três momentos abaixo.

**Caso A — o plano acabou de abrir (nenhuma tarefa iniciada):**

```
# Modelo de domínio — P-0744 — A especificação do agente de planejamento
Estado do modelo: versão 1 · 2026-09-20 · 3 operações · estágio atual: OP-1 — O investigador percorre o registro medido da atuação do planejador e devolve o agregado da atuação, dentro do teto de linhas.

## Objetos
| objeto | o que é | contrato | origem |
|---|---|---|---|
| registro medido da atuação do planejador | o conjunto fechado de rodadas de replanejamento e de achados de execução já escritos no repositório | uma ocorrência por linha, com o plano, a data, a classe do erro e a verificação que o teria evitado | externo |
| agregado da atuação | o resumo que volta da sondagem, dentro do teto de linhas | uma tabela por dimensão da especificação, com contagem e ocorrência de exemplo, sem nenhum dado bruto | OP-1 |
| especificação do planejador | o documento que descreve a figura do planejamento como o precedente do consultor descreve a dele | um documento próprio, uma seção por dimensão, toda afirmação ancorada em ocorrência do agregado | OP-2 |
| índice de documentos | a porta de entrada por onde todo documento grande do repositório é alcançado | uma entrada por documento, com tamanho, âncoras e a forma de acesso barata | externo |

## Fluxo
[prevista ] OP-1 — O investigador percorre o registro medido da atuação do planejador e devolve o agregado da atuação, dentro do teto de linhas.
            precisa de: registro medido da atuação do planejador
[prevista ] OP-2 — O redator escreve a especificação do planejador sobre o agregado da atuação, uma seção por dimensão, sem nenhuma afirmação que o agregado não sustente.
            precisa de: agregado da atuação
[prevista ] OP-3 — O mantenedor inscreve a especificação do planejador no índice de documentos e confere a documentação pública contra a árvore.
            precisa de: especificação do planejador, índice de documentos

## Mudanças desde o início
nenhuma
```

**Caso B — a primeira tarefa fechou e a segunda está em revisão.** Os blocos `## Objetos` e
`## Mudanças` saem idênticos ao caso A; mudam só a linha de estado e o bloco `## Fluxo`:

```
Estado do modelo: versão 1 · 2026-09-20 · 3 operações · estágio atual: OP-2 — O redator escreve a especificação do planejador sobre o agregado da atuação, uma seção por dimensão, sem nenhuma afirmação que o agregado não sustente.

## Fluxo
[concluída] OP-1 — O investigador percorre o registro medido da atuação do planejador e devolve o agregado da atuação, dentro do teto de linhas.
            precisa de: registro medido da atuação do planejador
[em curso ] OP-2 — O redator escreve a especificação do planejador sobre o agregado da atuação, uma seção por dimensão, sem nenhuma afirmação que o agregado não sustente.
            precisa de: agregado da atuação
[prevista ] OP-3 — O mantenedor inscreve a especificação do planejador no índice de documentos e confere a documentação pública contra a árvore.
            precisa de: especificação do planejador, índice de documentos
```

**Caso C — as três tarefas fecharam.** Mesma regra: mudam a linha de estado e o bloco `## Fluxo`:

```
Estado do modelo: versão 1 · 2026-09-20 · 3 operações · estágio atual: concluído

## Fluxo
[concluída] OP-1 — O investigador percorre o registro medido da atuação do planejador e devolve o agregado da atuação, dentro do teto de linhas.
            precisa de: registro medido da atuação do planejador
[concluída] OP-2 — O redator escreve a especificação do planejador sobre o agregado da atuação, uma seção por dimensão, sem nenhuma afirmação que o agregado não sustente.
            precisa de: agregado da atuação
[concluída] OP-3 — O mantenedor inscreve a especificação do planejador no índice de documentos e confere a documentação pública contra a árvore.
            precisa de: especificação do planejador, índice de documentos
```

**O que muda para o dono, em uma frase.** Antes, vinte estados paralelos e nenhuma posição; agora,
uma linha que diz qual é o estágio, e um fluxo em que se lê o que já passou e o que vem. **O que
muda para o agente:** a linha `precisa de` do estágio atual é o contrato de entrada da próxima
tarefa, e ela chega ao card copiada.

---

## 8. Invariantes de execução

Valem para todas as tarefas; cada card repete a parte que o vincula.

- **I-1** — Nenhum card edita `.claude/tools/backlog.py`, `.claude/tools/review_evidence.py` ou
  `.claude/tools/card_check.py`.
- **I-2** — Piso de regressão é **relação**, nunca constante: o total de `python -m pytest tests -q`
  re-medido no despacho não reduz, e a entrega soma os testes novos do card. Referência histórica
  datada: **245 coletados em 2026-09-20** (`F-5`).
- **I-3** — Texto normativo entra **verbatim** dos blocos cercados deste plano (§4, §5, §6) e dos
  blocos "Texto novo, literal" dos cards. O executor não parafraseia norma.
- **I-4** — **Card que publica norma que altera uma contagem ou uma enumeração fecha, no mesmo
  card, todas as frases da mesma seção que contam ou qualificam o conjunto.** Classe de defeito
  medida cinco vezes no `P-0741`, e nenhuma linha de aceite dela pegou.
- **I-5** — Todo número de aceite deste plano é **referência datada de 2026-09-20**; quem despacha
  o re-deriva antes de delegar. Entrega irmã caduca número de card ainda aberto — ocorreu três
  vezes no `P-0741`.
- **I-6** — Nenhuma tarefa commita. O commit é ato do loop no Marco 2.
- **I-7** — A região gerada de `.claude/README.md` só se escreve por
  `pwsh .claude/checks/kit_check.ps1 -Mode generate`, nunca à mão.
- **I-8** — Contingência acionada é devolvida na linha de retorno como `contingência <n> acionada:
  <o que mudou>`; a orquestração a materializa na linha `**Status:**` do card.
- **I-14** — **Card que muda protocolo entre papéis publica a cadeia e o aceite a percorre**:
  emissor → meio → consumidor, cada elo com residência e estado, e o aceite confere **todos** os
  elos, inclusive os que o card declara corretos e não toca (`D-23`). Escopo por **arquivo** não
  serve a mudança de protocolo: `AE-11` e `AE-14` são o mesmo defeito em dois pontos da mesma
  interface, corrigidos em escalonamentos diferentes porque cada card via só o seu arquivo.
- **I-13** — **Um bloco literal por ponto**: todo ponto que um card manda mudar em texto
  normativo tem bloco cercado próprio, nomeado e ancorado por conteúdo (`D-20`). Passo em prosa
  do tipo "trocar X por Y" sobre texto normativo é defeito de autoria, e o executor que o
  encontra sinaliza `blocked` razão `premissa` em vez de redigir — conduta correta, medida e
  endossada no `AE-10`. Corolário de `G-NOASK`: redigir doutrina em execução é decidir.
- **I-12** — **`Arquivos-alvo` é lista de caminhos puros**: um caminho por bullet, sozinho na
  linha, sem prosa, símbolo de código nem faixa colada nele. Região, faixa de linhas e
  justificativa vão em **sub-bullet** indentado sob o caminho (`D-19`). Defeito medido no
  `AE-9`: com prosa na linha, `review_evidence.py` leu `argparse.ArgumentParser` como caminho e
  não reconheceu seis literais.
- **I-11** — **Aceite de transcrição verbatim confronta o bloco entregue contra o bloco cercado
  do card, e a prova é comando, nunca declaração** (emendado no `ESC-4` por `D-22`). Contagem de
  resíduo não discrimina fidelidade (`AE-8`), e frase do executor sobre a própria entrega não é
  evidência (`AE-12`, rubrica §3). Todo card que manda transcrever publica, por bloco, **três**
  itens de `Verificação`, todos re-deriváveis por quem revisa:
  1. `sed -n '<a>,<b>p' <arquivo>` imprimindo a região entregue, para confronto linha a linha
     com o bloco cercado;
  2. `grep -c` da **primeira** e da **última** linha do bloco, cada um com o valor de chegada
     medido — é o que fecha as bordas da substituição;
  3. `grep -c` da frase que **tem de sumir**, com valor de chegada `0`.
  A declaração `fidelidade conferida: <bloco>` continua, mas mora em `Passos` e vale como
  **sinal**: nenhum `Pronto quando` se apoia nela, e ela não leva contagem de linhas — foi o
  número autodeclarado que errou duas vezes em treze no `AE-12`. Divergência de **um token**,
  ainda que a semântica não mude, é defeito de transcrição (`I-3`).
- **I-10** — **Contingência que cria arquivo declara o arquivo nos `Arquivos-alvo` e exige a
  declaração da ativação na linha de retorno** (`D-17`). E **recorte por faixa de linhas dentro de
  um arquivo-alvo orienta a edição, nunca delimita o aceite**: card que muda a semântica de um
  arquivo fecha com aceite de coerência do **arquivo inteiro** — docstring, `--help`, mensagens,
  preâmbulo que o nomeia. Classe de defeito medida duas vezes nesta execução (`AE-2`, `AE-5`).
- **I-9** — `README.md` (a raiz) e `.claude/README.md` são **dois arquivos diferentes**, com donos
  diferentes: o primeiro é escrito à mão e conferido por `check-readme.ps1`; o segundo tem região
  gerada e é conferido por `kit_check.ps1 -Mode check-drift`. Tratá-los como um só foi defeito
  medido na `MC-T5`.
- **I-15** — **Literal de aceite sai de uma linha do bloco, nunca de uma frase do autor.** Todo
  `grep -cF` de um card confere trecho contido **integralmente em uma linha** do bloco literal que a
  residência publica: `grep -cF` casa **dentro** da linha, e literal que atravessa a quebra é
  inalcançável junto com a `I-3` — só passaria se a árvore divergisse do bloco. Quando a proposição
  a conferir atravessa linhas, o aceite usa **dois greps, um por linha**, ou
  `sed -n '/<início>/,/<fim>/p'` comparado ao bloco. Quem escreve a linha de aceite a deriva **do
  bloco**, não da frase que tinha em mente, e quem despacha a re-deriva (`I-5`). Defeito medido em
  2026-09-21 (`AE-19`): a linha de aceite do bloco `R5`, escrita pelo **consultor** no `ESC-7`.
- **I-17** — **Bloco literal que descreve o comportamento de um instrumento não fecha só por
  `grep`.** O `grep` prova que o texto **chegou**; não prova que ele é **verdadeiro**. Card cujo
  bloco afirma o que um instrumento faz fecha com **ao menos um comando do próprio instrumento**
  cuja saída confirma a afirmação, medido **pelo caminho do usuário** — a CLI, não a função por
  dentro. Defeito medido em 2026-09-21 (`AE-22`): a §19 afirmava uma fronteira de violações que o
  `modelo.py` não emite, os sete literais bateram, o card fechou `aprovado 100%` e a afirmação
  continuou falsa. Vale para quem escreve o card e para quem o revisa.
- **I-16** — **Aceite que não casa com bloco verbatim não é decisão do executor.** Se um literal de
  aceite imprimir número diferente do declarado **e** o bloco estiver transcrito verbatim, o
  executor **para** e devolve `blocked` razão `premissa` com três dados medidos: o comando, a
  contagem obtida e a linha do bloco de onde o literal deveria sair. **Não** ajusta o texto
  publicado para o aceite passar (quebraria a `I-3`), **não** relaxa o comando e **não** atribui a
  falha a causa não medida — *"artefato de transmissão de shell"*, *"codificação"*: diagnóstico sem
  medição é decisão disfarçada, e decidir não é do executor (`G-NOASK`, Regra 8). Defeito medido em
  2026-09-21 (`AE-19`).

---

## 9. Tarefas

### DOM-T1 — A norma do modelo de domínio, e o papel que a executa [Sonnet · esforço high · classe implementacao]
- **Status:** `done` · 2026-09-20
- **Objetivo:** `GOVERNANCA.md` §3.2 substituída pela norma do modelo de domínio, a matriz de
  responsabilidades com a linha `**Modelagem**` e as três linhas de papel corrigidas, e a rubrica
  de revisão com a linha de alvo e o parágrafo de fronteira novos.
- **Fundamento:** `D-1`, `D-2`, `D-5`, `D-6`, `D-8`, `D-9`; fatos `F-9`, `F-14`. O card transcreve
  os blocos cercados da §4 deste plano, que é a residência única deles até a transcrição.
- **Operação do modelo:** `OP-1`
  - OP-1: O redator da norma grava na doutrina do kit o que o modelo de um plano passa a ser: objetos e operações encadeadas no lugar de frases soltas, a posição no fluxo derivada do andamento das tarefas, e a autoria concentrada num papel só.
  - precisa de: acervo de planos na forma anterior — `docs/plans/`, vinte e dois planos medidos em 2026-09-20, dos quais vinte e um são anteriores à doutrina do modelo; nenhum é tocado por este plano e nenhum é migrado; doutrina publicada do kit — `GOVERNANCA.md`, as skills e os agentes do kit; cada ponteiro nomeia a seção vigente que governa a forma, e ponteiro órfão é defeito no caminho da entrega, não dívida a pagar depois
- **Camada e fronteira:** documentação de doutrina. Nenhum código, nenhum teste. A regra de
  dependência `infracore ← contracts ← services ← plugins` não é tocada.
- **Arquivos-alvo:**
  - `GOVERNANCA.md:320` (`### 3.2 O modelo conceitual do plano`, até a linha 356 inclusive)
  - `GOVERNANCA.md:94` (linha `| **Revisão** |` da matriz de responsabilidades)
  - `GOVERNANCA.md:91` (linha `| **Planejamento** |`)
  - `GOVERNANCA.md:92` (linha `| **Orquestração** |`)
  - `docs/RUBRICA_DE_REVISAO.md:246` (`## 6. Achado de processo`, linha da tabela cujo primeiro campo é `modelo`)
  - `docs/RUBRICA_DE_REVISAO.md:278` (`## 7. Fronteira do papel`, parágrafo único)
- **Passos:**
  1. Substituir as linhas 320..356 de `GOVERNANCA.md` pelo bloco cercado de `### 3.2 O modelo de
     domínio do plano` da §4 deste plano, verbatim.
  2. Inserir, imediatamente depois da linha `| **Revisão** |` da matriz de §3, a linha
     `| **Modelagem** | …` da §4 deste plano, verbatim.
  3. Trocar, na linha `| **Planejamento** |`, o trecho vigente pelo trecho novo da tabela de
     substituições da §4.
  4. Repetir a troca na linha `| **Revisão** |` e na linha `| **Orquestração** |`, com os trechos
     correspondentes da mesma tabela.
  5. Substituir integralmente a linha de alvo `modelo` da tabela da §6 de
     `docs/RUBRICA_DE_REVISAO.md` pelo bloco cercado correspondente da §4.
  6. Substituir integralmente o parágrafo da §7 de `docs/RUBRICA_DE_REVISAO.md` pelo bloco cercado
     correspondente da §4.
  7. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - Texto normativo entra **verbatim** dos blocos cercados da §4. Não parafrasear, não resumir,
    não reordenar tabela (`I-3`).
  - Card que publica norma que altera contagem ou enumeração fecha, no mesmo card, as frases da
    mesma seção que contam o conjunto (`I-4`). A matriz passa de 9 para 10 linhas de papel.
  - Não commitar (`I-6`).
- **Não fazer:**
  - Não tocar `.claude/agents/*`, `.claude/skills/*`, `.claude/tools/*`, `README.md` nem
    `.claude/README.md` — cada um tem card próprio.
  - Não criar o agente `pantonic-model-designer` aqui: a norma o nomeia, a `DOM-T4` o cria.
  - Não editar `GOVERNANCA.md` §9, que enumera três agentes de um total de nove: a enumeração já
    está defasada antes deste plano e está declarada fora de escopo (§11).
- **Contingências:**
  1. Se `Select-String -Path GOVERNANCA.md -SimpleMatch -Pattern 'nove papéis','oito papéis'`
     imprimir alguma linha → editar cada linha impressa para o numeral `dez`, no mesmo ato.
  2. Se as linhas 320..356 de `GOVERNANCA.md` não começarem exatamente por
     `### 3.2 O modelo conceitual do plano` → parar e sinalizar `blocked` razão `premissa`.
  3. Se a tabela da §6 de `docs/RUBRICA_DE_REVISAO.md` não tiver linha cujo primeiro campo seja
     `modelo` → parar e sinalizar `blocked` razão `premissa`.
- **Testes:** nenhum teste automatizado — a entrega é texto normativo. A aferição é a verificação
  abaixo.
- **Verificação:**

  ```
  grep -c '^| \*\*' GOVERNANCA.md
  ```
  imprime `15` (hoje imprime `14`, medido 2026-09-20 — a matriz de §3 ganha uma linha).

  ```
  grep -n '### 3.2 O modelo de domínio do plano' GOVERNANCA.md
  ```
  imprime uma linha (hoje não imprime nada).

  ```
  grep -c 'confirma e emenda o modelo conceitual' GOVERNANCA.md
  ```
  imprime `0` (hoje imprime `1`).

  ```
  grep -c 'O reviewer não escreve fora do caminho do laudo' docs/RUBRICA_DE_REVISAO.md
  ```
  imprime `1` (hoje imprime `0`).

  `python .claude/tools/backlog.py check` imprime `check: OK — nenhuma violação.` e sai `0`
  (mesma saída medida em 2026-09-20).
- **Pronto quando:** `GOVERNANCA.md` §3.2 é o texto da §4 deste plano palavra por palavra, a matriz
  de §3 tem dez linhas de papel com a linha `**Modelagem**` logo depois de `**Revisão**`, as três
  linhas de papel citadas carregam o trecho novo, e os dois blocos da rubrica estão substituídos.
- **Fora do escopo desta tarefa:** a gramática que a máquina lê (`DOM-T2`), o instrumento
  (`DOM-T3`), o agente (`DOM-T4`), as definições de conduta dos papéis (`DOM-T5`) e a documentação
  pública (`DOM-T6`).

### DOM-T2 — A gramática que a máquina lê [Sonnet · esforço medium · classe implementacao]
- **Status:** `done` · 2026-09-20
- **Depende de:** `DOM-T1`
- **Objetivo:** a subseção `### Modelo conceitual (seção do plano)` da skill `diario-de-obras`
  substituída pela subseção `### Modelo de domínio (seção do plano)`, que é a gramática lida pelo
  instrumento.
- **Fundamento:** `D-1`, `D-2`, `D-4`, `D-9`; fato `F-12`. O card transcreve o bloco cercado da §5
  deste plano, residência única dele até a transcrição.
- **Operação do modelo:** `OP-2`
  - OP-2: O redator da gramática publica a forma exata de cada elemento da seção do modelo, para que a máquina a leia sem adivinhar e quem escreve saiba o que vai em cada linha.
  - precisa de: norma do modelo de domínio — residência única em `GOVERNANCA.md` §3.2; prosa normativa em blocos que substituem parágrafos nomeados, sem recopiar a gramática nem o ensinamento de autoria; nenhum outro documento a repete
- **Camada e fronteira:** skill de gramática. Nenhum código, nenhum teste.
- **Arquivos-alvo:**
  - `.claude/skills/diario-de-obras/SKILL.md:175` (`### Modelo conceitual (seção do plano)`, até a
    linha imediatamente anterior a `## Formato de uma tarefa atômica`, hoje a 197)
- **Passos:**
  1. Substituir a subseção inteira, do heading da linha 175 até a linha anterior ao heading
     `## Formato de uma tarefa atômica`, pelo bloco cercado `### Modelo de domínio (seção do
     plano)` da §5 deste plano, verbatim.
  2. Percorrer a seção `## Gramática legível por máquina` inteira (a partir da linha 130) e trocar
     toda ocorrência de `Oração do modelo` por `Operação do modelo` e de `oração` por `operação`
     **dentro dessa seção apenas**.
  3. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - Texto entra verbatim do bloco cercado da §5 (`I-3`).
  - A troca do passo 2 é confinada à seção `## Gramática legível por máquina`; nenhuma outra seção
    do arquivo é tocada.
  - Não commitar (`I-6`).
- **Não fazer:**
  - Não tocar `GOVERNANCA.md` nem a rubrica: a `DOM-T1` já os fechou.
  - Não tocar `.claude/tools/modelo.py`: a gramática é texto; o instrumento é a `DOM-T3`.
  - Não alterar `### Inbox de planos` nem `## Formato de uma tarefa atômica`.
- **Contingências:**
  1. Se a linha 175 não for `### Modelo conceitual (seção do plano)` → localizar o heading pelo
     texto exato com `grep -n`; se não existir no arquivo, parar e sinalizar `blocked` razão
     `premissa`.
  2. Se o passo 2 encontrar ocorrência de `Oração do modelo` **fora** da seção
     `## Gramática legível por máquina` → deixar como está e registrar a ocorrência na linha de
     retorno como `contingência 2 acionada: <arquivo:linha>`.
- **Testes:** nenhum teste automatizado — a entrega é gramática em texto. A aferição é a
  verificação abaixo.
- **Verificação:**

  ```
  grep -c 'Modelo de domínio (seção do plano)' .claude/skills/diario-de-obras/SKILL.md
  ```
  imprime `1` (hoje imprime `0`).

  ```
  grep -c 'Oração do modelo' .claude/skills/diario-de-obras/SKILL.md
  ```
  imprime `0` (hoje imprime `1`, medido 2026-09-20).

  ```
  grep -c 'Fluxo de operações' .claude/skills/diario-de-obras/SKILL.md
  ```
  imprime `2` ou mais (hoje imprime `0`).

  `python .claude/tools/backlog.py check` imprime `check: OK — nenhuma violação.` e sai `0`.
- **Pronto quando:** a subseção da skill é o bloco da §5 palavra por palavra, e nenhuma ocorrência
  de `Oração do modelo` resta na seção `## Gramática legível por máquina`.
- **Fora do escopo desta tarefa:** o instrumento (`DOM-T3`), o agente (`DOM-T4`), a anatomia do
  card na definição do planejador (`DOM-T5`).

### DOM-T3 — O instrumento lê a forma nova [Sonnet · esforço xhigh · classe implementacao]
- **Status:** `done` · 2026-09-20
- **Depende de:** `DOM-T2`
- **Objetivo:** `.claude/tools/modelo.py` conferindo e mostrando o modelo de domínio pela §6 deste
  plano, com as fixtures e os testes que afirmam as quatorze violações, os três rótulos, os dois
  casos de estágio e os dois exits de forma anterior.
- **Fundamento:** `D-1`, `D-2`, `D-3`, `D-14`, `D-15`; fatos `F-4`, `F-5`. O card implementa a §6
  deste plano, residência única da superfície, e lê a gramática que a `DOM-T2` gravou.
- **Operação do modelo:** `OP-3`
  - OP-3: O implementador do instrumento faz o programa conferir a seção contra a gramática e gerar a leitura do dono, que abre pelo estágio atual e não bloqueia plano escrito na forma anterior.
  - precisa de: gramática do modelo — residência única na skill `diario-de-obras`, subseção `Modelo de domínio (seção do plano)`; uma linha de tabela por elemento, com a forma à esquerda e a regra mais o código de violação à direita; acervo de planos na forma anterior — `docs/plans/`, vinte e dois planos medidos em 2026-09-20, dos quais vinte e um são anteriores à doutrina do modelo; nenhum é tocado por este plano e nenhum é migrado
- **Camada e fronteira:** ferramenta do kit, em `.claude/tools/`. Pode importar `backlog.py` por
  `importlib` e chamar `backlog._parse_plano`; **não** pode editar `backlog.py`. Nenhuma camada de
  produto é tocada.
- **Contratos/classes:** a dataclass de operação substitui a de oração e carrega `numero: int`,
  `texto: str`, `precisa_de: list[str]`, `tarefas: list[str]`. A dataclass de objeto carrega
  `nome: str`, `contrato: str`, `origem: str`. A dataclass de modelo carrega `versao: int`,
  `data: str`, `objetos: list`, `operacoes: list`, `mudancas: list[str]`, `tabela_objetos:
  list[str]`. `extrair_modelo(linhas: list[str]) -> Modelo | None` e
  `campo_operacoes(item_texto: str) -> list[str] | None` mantêm a forma das funções homônimas
  vigentes. `validar(modelo, plano) -> list[str]` devolve as linhas de violação na ordem da §6.
  `derivar_andamento(operacao, status_por_id) -> str` devolve `concluída`, `em curso` ou
  `prevista`. `derivar_estagio(modelo, status_por_id) -> str` devolve `OP-<j> — <texto>` ou
  `concluído`.
- **Arquivos-alvo:**
  - `.claude/tools/modelo.py:53` (dataclasses `Oracao` e `Modelo`, até a linha 71)
  - `.claude/tools/modelo.py:74` (bloco de expressões regulares, até a linha 84)
  - `.claude/tools/modelo.py:87` (funções `_extrair_tabela`, `_extrair_oracoes`, `extrair_modelo`,
    `campo_oracoes`, `_estado_valido`, `validar`, `derivar_estado`, até a linha 260)
  - `.claude/tools/modelo.py:268` (`verbo_check`, `_linha_oracao`, `_montar_show`, `verbo_show`,
    até a linha 361)
  - `tests/test_modelo.py` (os 6 testes vigentes saem; 10 entram)
  - `tests/fixtures/modelo/plano-valido.md` (renomear para `plano-forma-anterior.md`)
  - `tests/fixtures/modelo/plano-invalido.md` (substituir conteúdo)
  - `tests/fixtures/modelo/plano-sem-cabecalho.md` (substituir conteúdo)
  - `tests/fixtures/modelo/fluxo-valido.md` (novo)
  - `tests/fixtures/modelo/fluxo-concluido.md` (novo)
  - `tests/fixtures/modelo/plano-sem-modelo.md` (intocado)
- **Passos:**
  1. Reescrever as dataclasses e as expressões regulares para a gramática da §5 deste plano:
     cabeçalho com `<k> operações`, tabela `### 1.1 Objetos` de quatro colunas, par de linhas
     `- **OP-<n>** — <texto>` mais `  - \`precisa de: …\` · \`tarefas: …\``, tabela
     `### 1.3 Mudanças do modelo`, e campo de card `- **Operação do modelo:**` com os dois
     sub-bullets.
  2. Implementar as quatorze regras da tabela de violações da §6, cada uma emitindo exatamente a
     substring literal que a tabela declara, na ordem de emissão que a §6 fixa.
  3. Implementar os quatro exits de `check` da tabela de exit codes da §6, com os literais de
     stdout e stderr exatamente como escritos lá.
  4. Implementar `show` na forma fixa da §6, com os três rótulos de largura dez, a indentação de
     doze espaços da linha `precisa de:`, a linha de estágio e o filtro `--desde`.
  5. Renomear `tests/fixtures/modelo/plano-valido.md` para `plano-forma-anterior.md`, sem alterar o
     conteúdo: ele passa a ser a fixture do exit `2` de forma anterior.
  6. Escrever `tests/fixtures/modelo/fluxo-valido.md`: um plano sintético com quatro objetos, três
     operações e três tarefas, com os status escolhidos de modo que a primeira operação fique
     `concluída`, a segunda `em curso` e a terceira `prevista`.
  7. Escrever `tests/fixtures/modelo/fluxo-concluido.md`: o mesmo plano com as três tarefas `done`,
     para o caso de estágio `concluído`.
  8. Substituir o conteúdo de `plano-invalido.md` por um plano sintético que dispare **as quatorze**
     violações, uma vez cada.
  9. Substituir o conteúdo de `plano-sem-cabecalho.md` por um plano na forma nova sem a linha
     `**Estado do modelo:**`, para a `V13`.
  10. Substituir os 6 testes de `tests/test_modelo.py` pelos 10 da lista de `Testes`.
  11. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - Não editar `.claude/tools/backlog.py`, `review_evidence.py` nem `card_check.py` (`I-1`).
  - Preservar, sem alteração, o carregamento de `backlog.py` por `importlib`, a chamada a
    `backlog._parse_plano`, o default de `--root` e o `_forcar_utf8` (`F-4`).
  - O literal de exit `2` para plano sem seção continua **idêntico** ao vigente:
    `modelo: ausente — plano anterior à doutrina (sem '## 1. Modelo conceitual')`.
  - Piso de regressão é relação (`I-2`): este card **remove 6** testes e **acrescenta 10**; o total
    re-medido no despacho, menos 6, mais 10, é o piso. Referência datada: 245 em 2026-09-20.
  - Nenhum símbolo do módulo fica sem leitor depois da reescrita. Declarar na linha de retorno
    `cadeia fechada: <símbolos removidos>` — a propriedade que a `MC-T2b` instalou.
- **Não fazer:**
  - Não manter nenhuma regra da forma anterior no instrumento: há uma forma só depois desta tarefa
    (`D-14`).
  - Não migrar plano nenhum do acervo (`D-3`).
  - Não tocar `docs/plans/P-0741-modelo-conceitual.md`: ele é, a partir daqui, forma anterior, e é
    a `DOM-T3` que faz o instrumento dizê-lo sem bloquear.
  - Não escrever estado em fixture: o andamento é derivado do status das tarefas (`D-2`).
- **Contingências:**
  1. Se `backlog._parse_plano` não devolver o status de alguma tarefa citada por uma operação →
     tratar como tarefa sem status, que não é `done` nem `cancelled` nem `in-progress` nem
     `review`, e portanto mantém a operação `prevista`. Não é violação.
  2. Se a fixture do passo 8 não conseguir disparar as quatorze violações em um só arquivo sem que
     uma esconda a outra → partir em `plano-invalido.md` e `plano-invalido-2.md`, distribuir as
     quatorze entre os dois e ajustar o teste correspondente para somar as duas saídas.
  3. Se o renomear do passo 5 deixar alguma referência a `plano-valido.md` em outro arquivo de
     teste → atualizar a referência no mesmo ato.
- **Testes:** dez testes funcionais em `tests/test_modelo.py`:
  - `test_tf_check_fluxo_valido_sai_zero` — sobre `fluxo-valido.md`, exit `0` e stdout começando
    por `modelo: OK — 3 operações, 4 objetos`.
  - `test_tf_check_invalido_lista_catorze_violacoes_na_ordem` — sobre `plano-invalido.md`, exit `1`,
    as quatorze substrings literais da §6 presentes, na ordem de emissão que a §6 fixa.
  - `test_tf_check_sem_cabecalho_v13` — sobre `plano-sem-cabecalho.md`, exit `1` e a substring
    `V13 secao — cabeçalho, objetos ou lista de mudanças ausente`.
  - `test_tf_check_forma_anterior_sai_dois` — sobre `plano-forma-anterior.md`, exit `2` e a
    substring `modelo: forma anterior — plano na forma de orações`. **Poder discriminante:** a
    regra concorrente (tratar forma anterior como plano sem seção) daria a substring
    `modelo: ausente — plano anterior à doutrina`, que é diferente — a fixture separa as duas.
  - `test_tf_check_sem_modelo_sai_dois` — sobre `plano-sem-modelo.md`, exit `2` e a substring
    `modelo: ausente — plano anterior à doutrina`.
  - `test_tf_show_tres_rotulos_e_estagio_atual` — sobre `fluxo-valido.md`, a saída tem
    `[concluída]`, `[em curso ]` e `[prevista ]`, uma vez cada, e a linha de estado tem
    `estágio atual: OP-2 —`. **Poder discriminante:** a regra concorrente (estágio = primeira
    operação `em curso`) daria `OP-2` também nesta fixture; por isso o teste seguinte existe.
  - `test_tf_show_estagio_pula_operacao_concluida_fora_de_ordem` — sobre uma variação inline de
    `fluxo-valido.md` em que a primeira operação está `prevista` e a segunda `concluída`: a linha
    de estado tem `estágio atual: OP-1 —`. **Poder discriminante:** a regra concorrente (primeira
    `em curso`, ou primeira não `prevista`) daria `OP-2`.
  - `test_tf_show_fluxo_concluido_sem_estagio` — sobre `fluxo-concluido.md`, a linha de estado
    termina em `estágio atual: concluído` e a saída não tem `[prevista ]` nem `[em curso ]`.
  - `test_tf_show_desde_filtra_mudancas` — sobre `fluxo-valido.md` com `--desde` numa data entre as
    duas linhas de mudança da fixture: só a mais recente aparece.
  - `test_tf_show_forma_anterior_sai_dois` — sobre `plano-forma-anterior.md`, exit `2` e a mesma
    substring de forma anterior que `check` imprime.
- **Verificação:**

  ```
  python -m pytest tests/test_modelo.py -q
  ```
  passa, com 10 testes coletados neste arquivo (hoje são 6, medido 2026-09-20).

  ```
  python .claude/tools/modelo.py check --plano tests/fixtures/modelo/fluxo-valido.md
  ```
  sai `0` e imprime `modelo: OK — 3 operações, 4 objetos, 3 tarefas, 2 mudanças`.

  ```
  python .claude/tools/modelo.py check --plano docs/plans/P-0741-modelo-conceitual.md
  ```
  sai `2` e imprime `modelo: forma anterior — plano na forma de orações (sem '### 1.2 Fluxo de operações')`
  (hoje sai `0` e imprime `modelo: OK — 20 orações, …`).

  ```
  python .claude/tools/modelo.py check --plano docs/plans/P-0744-spec-do-planejador.md
  ```
  sai `0` (hoje sai `1`, porque o instrumento vigente não conhece a forma nova).

  ```
  python -m pytest tests -q
  ```
  passa, com total não menor que o total re-medido no despacho menos 6 mais 10.
- **Pronto quando:** os dez testes passam, os quatro comandos de `modelo.py` acima devolvem os
  exits e os literais declarados, e a suíte inteira passa com o piso da relação acima.
- **Fora do escopo desta tarefa:** o agente (`DOM-T4`), as definições de conduta (`DOM-T5`), a
  documentação pública (`DOM-T6`), e qualquer edição em plano do acervo.

### DOM-T3a — O que o instrumento e a gramática dizem de si mesmos [Sonnet · esforço low · classe implementacao]
- **Status:** `done` · 2026-09-20
- **Depende de:** `DOM-T3`
- **Objetivo:** o texto em que `.claude/tools/modelo.py` se descreve — docstring do módulo e
  `--help` — e o preâmbulo da skill `diario-de-obras` que **nomeia** a subseção da gramática
  passam a descrever a forma nova, sem nenhum resíduo da forma anterior fora dos literais
  normativos de saída.
- **Fundamento:** `D-14`, `D-16`; invariantes `I-1`, `I-3`, `I-10`; achados `AE-2` e `AE-5` desta
  execução. Card corretivo criado no escalonamento `ESC-1` (consultor de plano, 2026-09-20): a
  `DOM-T3` recortou `modelo.py` em quatro faixas de linhas e a `DOM-T2` confinou a edição da skill
  ao recorte da subseção; os dois recortes deixaram de fora o texto que **nomeia** a forma, e
  nenhum card restante o alcança.
- **Operação do modelo:** `OP-4`
  - OP-4: O implementador acerta o que o instrumento e a gramática dizem de si mesmos, para que nenhum texto de apresentação descreva a forma que acabou de sair de uso.
  - precisa de: instrumento do modelo — `.claude/tools/modelo.py`, verbos `check` e `show`, exits `0`, `1` e `2` com literais fixos; lê as tarefas do plano por `backlog._parse_plano` e não reescreve `backlog.py`; cada regra nova nasce com fixture e teste pelo caminho do usuário; doutrina publicada do kit — `GOVERNANCA.md`, as skills e os agentes do kit; cada ponteiro nomeia a seção vigente que governa a forma, e ponteiro órfão é defeito no caminho da entrega, não dívida a pagar depois
- **Camada e fronteira:** ferramenta do kit (`.claude/tools/`) e skill do kit (`.claude/skills/`).
  Só texto de descrição: **nenhuma linha de comportamento muda**, nenhum literal de saída muda,
  nenhuma assinatura muda, nenhum teste vigente muda de resultado.
- **Contratos/classes:** nenhum. O card não cria, não remove e não renomeia símbolo algum.
- **Arquivos-alvo:**
  - `.claude/tools/modelo.py` — **arquivo inteiro**. As duas regiões abaixo são as únicas que
    mudam, mas o aceite é de coerência do módulo todo (`I-10`): (a) o docstring do módulo, da aspa
    tripla de abertura da linha 1 à de fechamento, 14 linhas medidas em 2026-09-20; (b) o argumento
    `description=(...)` do `argparse.ArgumentParser` dentro de `main()`, localizado por
    `grep -n 'description=(' .claude/tools/modelo.py` — linha 438 em 2026-09-20, e o número se
    re-deriva no despacho (`I-5`).
  - `.claude/skills/diario-de-obras/SKILL.md` — **arquivo inteiro**. Muda só o preâmbulo da seção
    `## Gramática legível por máquina`, localizado por conteúdo (o bloco de três linhas transcrito
    abaixo; linhas 134-136 em 2026-09-20).
- **Texto novo, literal — docstring do módulo `.claude/tools/modelo.py` (substitui integralmente o
  docstring vigente, aspas de abertura e de fechamento incluídas):**

  ```python
  """`modelo.py` — os verbos `check` e `show` sobre a seção `## 1. Modelo conceitual` de um plano,
  na superfície normativa da `### 6. Superfície do instrumento modelo.py` de
  `docs/plans/P-0743-modelo-de-dominio.md`.

  Gramática lida (residência única: skill `diario-de-obras`, subseção "Modelo de domínio (seção do
  plano)"): cabeçalho `**Estado do modelo:**`, tabela `### 1.1 Objetos`, `### 1.2 Fluxo de
  operações` — pares de linhas `- **OP-<n>** — <texto>` e o sub-bullet com `precisa de:` e
  `tarefas:`, com subtítulos `**A. …**` livres — e tabela `### 1.3 Mudanças do modelo`.

  `check` julga a seção contra o vocabulário fechado de violações `V1`..`V14` (`### 6` do `P-0743`)
  e `show` deriva a leitura do dono a partir do modelo real: ela abre pelo estágio atual, que é a
  primeira operação ainda não concluída, derivada do status das tarefas e não gravada por nenhum
  papel. Ambos carregam `backlog.py` por caminho (`importlib.util.spec_from_file_location`) e
  chamam `backlog._parse_plano` para obter `Plano.tarefas`; `backlog.py` não é reescrito (`I-1` do
  `P-0743`)."""
  ```

- **Texto novo, literal — `description=(...)` do `argparse.ArgumentParser` em `main()` (substitui
  integralmente o argumento, preservando a indentação vigente do arquivo):**

  ```python
          description=(
              "modelo.py (P-0743): check julga a seção '## 1. Modelo conceitual' de um plano "
              "contra o vocabulário de violações V1..V14; show deriva a leitura do dono a partir "
              "do modelo real, abrindo pelo estágio atual."
          )
  ```

- **Texto novo, literal — preâmbulo da seção `## Gramática legível por máquina` de
  `.claude/skills/diario-de-obras/SKILL.md` (substitui as três linhas que hoje começam em
  `residência única do texto;`):**

  ```markdown
  residência única do texto; o plano de origem não a recopia depois da transcrição. A subseção
  "Modelo de domínio (seção do plano)" transcreve `docs/plans/P-0743-modelo-de-dominio.md` §5 e é
  lida por `.claude/tools/modelo.py`.
  ```

- **Passos:**
  1. Substituir o docstring do módulo de `.claude/tools/modelo.py` pelo literal acima, verbatim
     (`I-3`), preservando a linha `from __future__ import annotations` imediatamente abaixo dele.
  2. Substituir o argumento `description=(...)` de `main()` pelo literal acima, verbatim,
     preservando a indentação e os parênteses que o arquivo já tem em volta.
  3. Substituir as três linhas do preâmbulo de `SKILL.md` pelo literal acima, verbatim.
  4. Varrer `.claude/tools/modelo.py` **inteiro** atrás de resíduo da forma anterior:
     `grep -n -e 'oraç' -e 'MC-T2' -e 'P-0741' -e 'V1\.\.V9' -e '1\.1 Vocabulário' .claude/tools/modelo.py`.
     **A única ocorrência que sobrevive** é a da linha do literal normativo de saída
     `modelo: forma anterior — plano na forma de orações (sem '### 1.2 Fluxo de operações')`
     (linha 84 em 2026-09-20). Qualquer outra ocorrência é resíduo e se corrige neste mesmo card,
     respeitada a contingência 1.
  5. Varrer `.claude/skills/diario-de-obras/SKILL.md` **inteiro**:
     `grep -n -e 'Modelo conceitual' -e 'P-0741' .claude/skills/diario-de-obras/SKILL.md`. Toda
     ocorrência que **nomeie a subseção da gramática ou a residência dela** se corrige neste card,
     com o mesmo teor do literal acima; ocorrência que cite o `P-0741` como fato histórico de outro
     assunto fica como está.
  6. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - Nenhum literal de **saída** de `modelo.py` muda. Em particular, as duas mensagens de exit `2` e
    as quatorze substrings `V1`..`V14` ficam byte a byte como a `DOM-T3` as entregou — elas são a
    norma da §6 e estão afirmadas por teste.
  - Nenhuma linha de comportamento muda: nem `import`, nem expressão regular, nem função, nem
    dataclass, nem `_forcar_utf8`, nem o carregamento de `backlog.py` por `importlib` (`F-4`).
  - Não editar `.claude/tools/backlog.py`, `review_evidence.py` nem `card_check.py` (`I-1`).
  - Texto entra verbatim dos três blocos literais acima (`I-3`).
  - Piso de regressão é relação (`I-2`): este card **não remove nem acrescenta teste**; o total
    re-medido no despacho é o piso e a entrega o mantém. Referência datada: **249 em 2026-09-20**.
  - Nenhuma contingência deste card cria arquivo. Se alguma só puder ser cumprida criando arquivo
    não declarado nos `Arquivos-alvo`, o card está incompleto: sinalizar `blocked` razão `premissa`
    (`I-10`).
  - Não commitar (`I-6`).
- **Não fazer:**
  - Não tocar `docs/plans/P-0741-modelo-conceitual.md` nem nenhum outro plano do acervo (`D-3`).
  - Não reescrever a subseção `### Modelo de domínio (seção do plano)` de `SKILL.md`: ela é a
    entrega da `DOM-T2`, está aprovada, e este card conserta só o **preâmbulo que a nomeia**.
  - Não mexer em `tests/test_modelo.py` nem nas fixtures: o docstring de `tests/test_modelo.py` já
    foi corrigido pela `DOM-T3`.
  - Não tocar `README.md`, `.claude/README.md`, `GOVERNANCA.md` nem `docs/RUBRICA_DE_REVISAO.md`.
- **Contingências:**
  1. Se o passo 4 encontrar resíduo em **linha de comportamento** (nome de símbolo, expressão
     regular, literal de saída) e não em texto de descrição → **não corrigir**: parar, sinalizar
     `blocked` razão `premissa` e devolver as linhas encontradas na linha de retorno. Resíduo em
     comportamento é defeito da `DOM-T3` e não cabe neste card.
  2. Se o passo 5 encontrar em `SKILL.md` mais de uma frase que nomeie a subseção da gramática ou a
     residência dela → substituir **todas** pelo mesmo teor do literal acima e devolver na linha de
     retorno `contingência 2 acionada: <linhas corrigidas>` (`I-8`).
- **Testes:** nenhum teste novo — a entrega é texto de descrição, e a superfície de comportamento
  já está afirmada pelos dez testes da `DOM-T3`. A aferição são os greps de coerência abaixo, que
  discriminam a forma nova da anterior no **arquivo inteiro**, não só nas regiões editadas.
- **Verificação:**

  ```
  grep -c 'oraç' .claude/tools/modelo.py
  ```
  imprime `1` (hoje imprime `2`, medido 2026-09-20) — a única sobrevivente é a linha do literal
  normativo de saída de forma anterior.

  ```
  grep -c "plano na forma de orações (sem '### 1.2 Fluxo de operações')" .claude/tools/modelo.py
  ```
  imprime `1`, **inalterado** (hoje imprime `1`, medido 2026-09-20).

  ```
  grep -c 'MC-T2' .claude/tools/modelo.py
  ```
  imprime `0` (hoje imprime `2`, medido 2026-09-20).

  ```
  grep -c 'P-0741' .claude/tools/modelo.py
  ```
  imprime `0` (hoje imprime `1`, medido 2026-09-20).

  ```
  grep -c '1\.1 Vocabulário' .claude/tools/modelo.py
  ```
  imprime `0` (hoje imprime `1`, medido 2026-09-20).

  ```
  grep -c 'V1\.\.V9' .claude/tools/modelo.py
  ```
  imprime `0` (hoje imprime `1`, medido 2026-09-20).

  ```
  grep -c 'V1\.\.V14' .claude/tools/modelo.py
  ```
  imprime `1` (hoje imprime `0`, medido 2026-09-20).

  ```
  python .claude/tools/modelo.py --help
  ```
  sai `0`; a saída contém `V1..V14` e **não** contém `V1..V9`.

  ```
  grep -c 'P-0741' .claude/skills/diario-de-obras/SKILL.md
  ```
  imprime `0` (hoje imprime `1`, medido 2026-09-20).

  ```
  grep -c 'Modelo conceitual (seção do plano)' .claude/skills/diario-de-obras/SKILL.md
  ```
  imprime `0` (hoje imprime `1`, medido 2026-09-20).

  ```
  grep -c 'P-0743' .claude/skills/diario-de-obras/SKILL.md
  ```
  imprime `1` ou mais (hoje imprime `0`, medido 2026-09-20).

  ```
  python .claude/tools/modelo.py check --plano docs/plans/P-0744-spec-do-planejador.md
  ```
  sai `0` e imprime `modelo: OK — 3 operações, 4 objetos, 3 tarefas, 0 mudanças` — **inalterado**
  (hoje idem, medido 2026-09-20: este card não pode mexer neste resultado).

  ```
  python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md
  ```
  sai `2` e imprime `modelo: forma anterior — plano na forma de orações (sem '### 1.2 Fluxo de operações')`
  — **inalterado** (hoje idem, medido 2026-09-20).

  ```
  python -m pytest tests -q
  ```
  passa, com total **não menor** que o total re-medido no despacho. Referência datada: **249 em
  2026-09-20**.
- **Pronto quando:** os onze greps acima devolvem os números declarados, `--help` anuncia
  `V1..V14`, os dois `modelo.py check` devolvem exits e literais **inalterados**, a suíte inteira
  passa no piso da relação, e **nenhuma linha de `.claude/tools/modelo.py` ou de
  `.claude/skills/diario-de-obras/SKILL.md` descreve o modelo como orações numeradas com estado
  gravado** — exceto o literal normativo de saída que nomeia a forma anterior.
- **Fora do escopo desta tarefa:** o agente (`DOM-T4`), as definições de conduta (`DOM-T5`), a
  documentação pública e o `README.md` (`DOM-T6`), a subseção `### Modelo de domínio (seção do
  plano)` de `SKILL.md` (entrega da `DOM-T2`, aprovada) e qualquer edição em plano do acervo.

### DOM-T3b — A referência cruzada do docstring [Sonnet · esforço low · classe implementacao]
- **Status:** `done` · 2026-09-20
- **Depende de:** `DOM-T3a`
- **Objetivo:** o docstring de `.claude/tools/modelo.py` idêntico, linha a linha, ao bloco cercado
  deste card — em particular apontando o invariante `I-1` do `P-0743`, que é o que a frase explica,
  e não o `I-3`.
- **Fundamento:** `D-18`; invariantes `I-3`, `I-11`, `I-12`; achado `AE-8`. Card corretivo criado no
  escalonamento `ESC-2` (consultor de plano, 2026-09-20): a `DOM-T3a` passou em 11/11 greps de
  aceite e ainda assim publicou `(I-3 do P-0743)` onde o bloco literal dela mandava
  `(I-1 do P-0743)` — token herdado do docstring substituído, invisível a aceite por contagem de
  resíduo. Nenhum card restante toca `.claude/tools/modelo.py`.
- **Operação do modelo:** `OP-4`
  - OP-4: O implementador acerta o que o instrumento e a gramática dizem de si mesmos, para que nenhum texto de apresentação descreva a forma que acabou de sair de uso.
  - precisa de: instrumento do modelo — `.claude/tools/modelo.py`, verbos `check` e `show`, exits `0`, `1` e `2` com literais fixos; lê as tarefas do plano por `backlog._parse_plano` e não reescreve `backlog.py`; cada regra nova nasce com fixture e teste pelo caminho do usuário; doutrina publicada do kit — `GOVERNANCA.md`, as skills e os agentes do kit; cada ponteiro nomeia a seção vigente que governa a forma, e ponteiro órfão é defeito no caminho da entrega, não dívida a pagar depois
- **Camada e fronteira:** ferramenta do kit, em `.claude/tools/`. Um token de texto de descrição.
  Nenhuma linha de comportamento, nenhum literal de saída, nenhuma assinatura.
- **Contratos/classes:** nenhum.
- **Arquivos-alvo:**
  - `.claude/tools/modelo.py`
    - só o docstring do módulo, da aspa tripla de abertura da linha 1 à de fechamento da linha 15
      (medido 2026-09-20; os números se re-derivam no despacho, `I-5`)
- **Texto novo, literal — docstring do módulo de `.claude/tools/modelo.py` (substitui integralmente
  o docstring vigente, aspas de abertura e de fechamento incluídas):**

  ```python
  """`modelo.py` — os verbos `check` e `show` sobre a seção `## 1. Modelo conceitual` de um plano,
  na superfície normativa da `### 6. Superfície do instrumento modelo.py` de
  `docs/plans/P-0743-modelo-de-dominio.md`.

  Gramática lida (residência única: skill `diario-de-obras`, subseção "Modelo de domínio (seção do
  plano)"): cabeçalho `**Estado do modelo:**`, tabela `### 1.1 Objetos`, `### 1.2 Fluxo de
  operações` — pares de linhas `- **OP-<n>** — <texto>` e o sub-bullet com `precisa de:` e
  `tarefas:`, com subtítulos `**A. …**` livres — e tabela `### 1.3 Mudanças do modelo`.

  `check` julga a seção contra o vocabulário fechado de violações `V1`..`V14` (`### 6` do `P-0743`)
  e `show` deriva a leitura do dono a partir do modelo real: ela abre pelo estágio atual, que é a
  primeira operação ainda não concluída, derivada do status das tarefas e não gravada por nenhum
  papel. Ambos carregam `backlog.py` por caminho (`importlib.util.spec_from_file_location`) e
  chamam `backlog._parse_plano` para obter `Plano.tarefas`; `backlog.py` não é reescrito (`I-1` do
  `P-0743`)."""
  ```

  **A única diferença contra o que está na árvore hoje é o token `I-1` na penúltima linha**, onde
  hoje se lê `I-3`. As outras quatorze linhas já estão idênticas — conferir, não reescrever.
- **Passos:**
  1. Imprimir o docstring vigente com `sed -n '1,15p' .claude/tools/modelo.py` e confrontá-lo, linha
     a linha, com o bloco cercado acima.
  2. Corrigir a única linha divergente, trocando `(\`I-3\` do` por `(\`I-1\` do`. Nenhuma outra
     linha do arquivo é tocada.
  3. Repetir o passo 1 e devolver, na linha de retorno, `fidelidade conferida: docstring — 15
     linhas idênticas ao bloco cercado da DOM-T3b` (`I-11`).
  4. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - Nenhuma linha fora do docstring muda. Em particular, o `description=(...)` de `main()` já está
    correto e **não** se toca.
  - Nenhum literal de saída de `modelo.py` muda (`I-3`).
  - Não editar `backlog.py`, `review_evidence.py` nem `card_check.py` (`I-1`).
  - Piso de regressão é relação (`I-2`): nenhum teste entra nem sai. Referência datada: **249 em
    2026-09-20**.
  - Nenhuma contingência deste card cria arquivo (`I-10`).
  - Não commitar (`I-6`).
- **Não fazer:**
  - Não reescrever o docstring inteiro "por segurança": catorze das quinze linhas já estão certas, e
    reescrever é como o `AE-8` nasceu.
  - Não tocar `.claude/skills/diario-de-obras/SKILL.md`: a entrega da `DOM-T3a` ali está conforme.
  - Não tocar `README.md`, `.claude/README.md`, `GOVERNANCA.md` nem `docs/RUBRICA_DE_REVISAO.md`.
- **Contingências:**
  1. Se o passo 1 encontrar **mais de uma** linha divergente do bloco cercado → corrigir todas no
     mesmo ato, pelo bloco cercado, e devolver `contingência 1 acionada: <linhas corrigidas>`
     (`I-8`).
- **Testes:** nenhum teste novo — a entrega é um token de texto de descrição.
- **Verificação:**

  ```
  grep -c 'I-3' .claude/tools/modelo.py
  ```
  imprime `0` (hoje imprime `1`, na linha 14, medido 2026-09-20).

  ```
  grep -n 'I-1' .claude/tools/modelo.py
  ```
  imprime **exatamente uma** linha, a 14 (hoje não imprime nenhuma, medido 2026-09-20).

  ```
  sed -n '1,15p' .claude/tools/modelo.py
  ```
  sai idêntico, linha a linha, ao bloco cercado deste card (`I-11`).

  ```
  python .claude/tools/modelo.py --help
  ```
  sai `0`; a saída contém `V1..V14` — **inalterada** (hoje idem, medido 2026-09-20).

  ```
  python .claude/tools/modelo.py check --plano docs/plans/P-0744-spec-do-planejador.md
  ```
  sai `0` e imprime `modelo: OK — 3 operações, 4 objetos, 3 tarefas, 0 mudanças` — **inalterado**.

  ```
  python -m pytest tests -q
  ```
  passa, com total **não menor** que o re-medido no despacho. Referência datada: **249 em
  2026-09-20**.
- **Pronto quando:** `sed -n '1,15p' .claude/tools/modelo.py` é idêntico, linha a linha, ao bloco
  cercado deste card; `grep -c 'I-3'` imprime `0`; `--help` e os dois `check` seguem inalterados; a
  suíte passa no piso; e a linha de retorno traz a declaração de fidelidade do `I-11`.
- **Fora do escopo desta tarefa:** o agente (`DOM-T4`), as definições de conduta (`DOM-T5`), a
  documentação pública (`DOM-T6`), e qualquer outra linha de `.claude/tools/modelo.py`.

### DOM-T4 — O modelador [Sonnet · esforço high · classe implementacao]
- **Status:** `done` · 2026-09-20
- **Depende de:** `DOM-T3`
- **Objetivo:** o agente `pantonic-model-designer` existindo como décimo agente do kit, com o
  ensinamento de como se escreve um modelo de domínio, e as duas portas de inventário do kit
  fechadas sobre dez agentes.
- **Fundamento:** `D-5`, `D-6`, `D-9`, `D-12`; fatos `F-2`, `F-7`, `F-8`; invariantes `I-4`, `I-7`,
  `I-9`. A norma que este agente executa foi gravada pela `DOM-T1`; a gramática que ele escreve,
  pela `DOM-T2`; o instrumento que o confere, pela `DOM-T3`.
- **Operação do modelo:** `OP-5`
  - OP-5: O autor de papéis cria o agente único dono de todo ato sobre o modelo e escreve nele o ensinamento de como um modelo se escreve, que deixa de ficar pulverizado nos demais agentes.
  - precisa de: norma do modelo de domínio — residência única em `GOVERNANCA.md` §3.2; prosa normativa em blocos que substituem parágrafos nomeados, sem recopiar a gramática nem o ensinamento de autoria; nenhum outro documento a repete; gramática do modelo — residência única na skill `diario-de-obras`, subseção `Modelo de domínio (seção do plano)`; uma linha de tabela por elemento, com a forma à esquerda e a regra mais o código de violação à direita
- **Camada e fronteira:** definição de agente, em `.claude/agents/`. O arquivo novo tem front
  matter com `name`, `description`, `model` e `tools`, na mesma forma dos nove vigentes.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-model-designer.md`
    - arquivo novo
  - `README.md`
    - a frase de contagem da §11 — linha 802 em 2026-09-20
    - a tabela **Agentes** da §11: a linha nova entra **depois** da última linha da tabela, que
      é a de `pantonic-benchmarker` — linha 819 em 2026-09-20. O 816 previsto no planejamento
      estava defasado, medido no `ESC-1`; os dois números se re-derivam no despacho (`I-5`)
  - `.claude/README.md`
    - só a região entre os marcadores `kit:agents` de início e fim, e só por instrumento (`I-7`)
- **Texto novo, literal — front matter de `.claude/agents/pantonic-model-designer.md`:**

  ```markdown
  ---
  name: pantonic-model-designer
  description: Modelador de domínio de plano Pantonic*. Dono único de todo ato sobre a seção Modelo conceitual de um plano - escreve na autoria, emenda quando uma decisão muda o que o plano entrega, resolve conflito entre o texto e a entrega e explica o contexto do modelo. Não planeja, não executa, não julga entrega e não escreve nenhuma outra linha do plano.
  model: opus
  tools: Read, Glob, Grep, Bash, Edit
  ---
  ```

- **Texto novo, literal — linha a acrescentar ao fim da tabela **Agentes** de `README.md` §11:**

  ```markdown
  | `pantonic-model-designer` | Opus | Todo ato sobre o modelo de domínio de um plano: escrever na autoria, emendar por decisão, resolver conflito entre o texto e a entrega e explicar o contexto. Não planeja, não executa e não julga. |
  ```

- **Texto novo, literal — frase de contagem de `README.md` §11:**

  ```markdown
  O kit são dez agentes, onze skills, quatro verificadores executáveis e a declaração de projeções,
  ```

- **Passos:**
  1. Criar `.claude/agents/pantonic-model-designer.md` com o front matter literal acima e o corpo
     descrito no passo 2.
  2. Escrever o corpo do agente com sete blocos, nesta ordem: (a) o papel, apontando para a matriz
     de `GOVERNANCA.md` §3 como residência única dele; (b) os fatos estáveis — a norma em
     `GOVERNANCA.md` §3.2, a gramática na skill `diario-de-obras`, o instrumento
     `.claude/tools/modelo.py`; (c) **o ensinamento**: como se escreve um modelo de domínio —
     começar pelos objetos que o plano manipula, dar a cada um o contrato que quem implementa
     precisa, encadear as operações na ordem em que o produto as executa, escrever cada operação
     nomeando quem age, e conferir que a primeira operação é a única que só depende de objeto
     externo; (d) os quatro atos — `autoria`, `emenda`, `conflito`, `leitura` —, com o que cada um
     recebe e o que devolve; (e) a gramática do dossiê `Ato de modelo` de seis campos, copiada da
     norma; (f) a forma da devolução: a seção `## 1. Modelo conceitual` inteira e literal, mais a
     linha `MD-<n>` do ato, e nada mais; (g) o que o modelador nunca faz — não planeja, não executa,
     não julga entrega, não escreve fora da seção `## 1. Modelo conceitual` e não aciona outro
     agente.
  3. Acrescentar, no bloco (b), a linha de auto-conferência: todo ato termina com
     `python .claude/tools/modelo.py check --plano <plano>` e só devolve com exit `0`.
  4. Acrescentar a linha literal da tabela **Agentes** ao fim dela em `README.md` §11, depois da
     linha de `pantonic-benchmarker`.
  5. Trocar a frase de contagem de `README.md` §11 pela frase literal acima.
  6. Regenerar `.claude/README.md` com `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate`.
  7. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - `README.md` (a raiz) e `.claude/README.md` são arquivos diferentes com donos diferentes
    (`I-9`): o primeiro é editado à mão nos passos 4 e 5; o segundo **só** pelo instrumento do
    passo 6 (`I-7`).
  - A frase de contagem e a tabela são a mesma seção: quem acrescenta a linha fecha a frase no
    mesmo ato (`I-4`). O aceite é de coerência do **inventário inteiro**, não das duas linhas
    editadas (`I-10`): depois do passo 6, nenhuma frase do `README.md` nem de `.claude/README.md`
    pode contar nove agentes.
  - Nenhuma contingência deste card cria arquivo além de
    `.claude/agents/pantonic-model-designer.md`, que já está nos `Arquivos-alvo`. Se alguma só
    puder ser cumprida criando outro arquivo, o card está incompleto: sinalizar `blocked` razão
    `premissa` (`I-10`). O numeral vai **por extenso**, como o vigente, porque é assim que
    `check-readme.ps1` o lê.
  - `tools:` do agente novo não inclui `Write`: o modelador edita a seção de um plano que já
    existe, nunca cria arquivo.
  - Não commitar (`I-6`).
- **Não fazer:**
  - Não editar a região gerada de `.claude/README.md` à mão, em nenhuma circunstância.
  - Não tocar `GOVERNANCA.md` §9, cuja enumeração de agentes já está defasada e está fora de escopo
    (§11).
  - Não mudar o front matter de nenhum dos nove agentes existentes.
  - Não escrever no corpo do agente a norma nem a gramática: elas têm residência própria e o corpo
    aponta para elas (`D-9`).
- **Contingências:**
  1. Se `kit_check.ps1 -Mode generate` sair diferente de `0` → parar e sinalizar `blocked` razão
     `ferramenta`, com a saída literal na linha de retorno.
  2. Se `check-readme.ps1` acusar divergência de contagem depois do passo 5 → a frase ficou com
     numeral errado; corrigir a frase e repetir, sem tocar a tabela.
- **Testes:** nenhum teste automatizado — a entrega é definição de agente e inventário. A aferição
  são os dois guardas abaixo, que já discriminam a contagem.
- **Verificação:**

  ```
  pwsh -NoProfile -File .claude/checks/check-readme.ps1
  ```
  sai `0` e a saída começa por `check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s)`
  (hoje: `check-readme: OK - 9 agente(s), 11 skill(s), 20 guardrail(s)`, medido 2026-09-20).

  ```
  pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift
  ```
  sai `0` e a saída começa por
  `kit_check: check-drift OK - .claude/README.md == regenerado (10 agente(s), 11 skill(s))`
  (hoje: `(9 agente(s), 11 skill(s))`, medido 2026-09-20).

  ```
  grep -c '^| `pantonic-' README.md
  ```
  imprime `10` (hoje imprime `9`).

  ```
  grep -c '^| `pantonic-' .claude/README.md
  ```
  imprime `10` (hoje imprime `9`).

  ```
  grep -c 'O kit são dez agentes' README.md
  ```
  imprime `1` (hoje imprime `0`).

  ```
  grep -c -e 'nove agentes' -e '9 agente' README.md .claude/README.md
  ```
  imprime `0` para os dois arquivos (hoje `README.md` imprime `1`, na linha 802, e
  `.claude/README.md` imprime `0`, medido 2026-09-20). É o aceite de coerência do inventário
  inteiro (`I-10`).

  ```
  sed -n '1,6p' .claude/agents/pantonic-model-designer.md
  ```
  sai idêntico, linha a linha, ao bloco cercado do front matter deste card; e a linha nova da
  tabela **Agentes** e a frase de contagem entregues conferem palavra por palavra com os blocos
  cercados correspondentes.
  Devolver na linha de retorno a declaração de fidelidade do `I-11`:
  `fidelidade conferida: <bloco> — <n> linhas idênticas ao bloco cercado do card`, uma por
  bloco literal deste card. **Divergência de um único token é defeito de transcrição (`I-3`),
  ainda que a semântica não mude** — foi assim que o `AE-8` passou por 11/11 greps verdes.
- **Pronto quando:** `.claude/agents/pantonic-model-designer.md` existe com os sete blocos, os dois
  guardas saem `0` anunciando dez agentes, as duas tabelas de inventário têm dez linhas de
  agente e **nenhuma frase dos dois READMEs conta nove agentes** (`I-10`).
- **Fora do escopo desta tarefa:** as cláusulas dos outros papéis (`DOM-T5`), a seção pública §8.1
  (`DOM-T6`) e qualquer ato de modelo sobre plano real.

### DOM-T5 — Os papéis diante do modelador [Sonnet · esforço high · classe implementacao]
- **Status:** `done` · 2026-09-20
- **Depende de:** `DOM-T4`
- **Objetivo:** as quatro definições de conduta que citam o modelo alinhadas à norma: o revisor sem
  ferramenta de escrita e com a rota de achado, o planejador e o consultor devolvendo o dossiê, e o
  loop despachando o modelador.
- **Fundamento:** `D-4`, `D-6`, `D-8`; fatos `F-2`, `F-10`, `F-11`, `F-15`. A norma que estes
  arquivos executam foi gravada pela `DOM-T1`; o agente que eles acionam, pela `DOM-T4`.
- **Operação do modelo:** `OP-6`
  - OP-6: O autor de papéis alinha os demais papéis à norma: o revisor perde a escrita no modelo, e quem precisa de um ato devolve o dossiê fechado na própria linha de retorno, que quem conduz a sessão despacha.
  - precisa de: norma do modelo de domínio — residência única em `GOVERNANCA.md` §3.2; prosa normativa em blocos que substituem parágrafos nomeados, sem recopiar a gramática nem o ensinamento de autoria; nenhum outro documento a repete; modelador — `.claude/agents/pantonic-model-designer.md`; front matter com nome, descrição e lista de ferramentas, e corpo com os atos, o ensinamento e o gate; as duas portas de inventário do kit contam os agentes e hoje fecham sobre dez
- **Camada e fronteira:** definições de agente e skill de orquestração. Nenhum código, nenhum teste.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-reviewer.md`
    - linha 5 (a linha `tools:`), linha 47 (bullet da escrita única), linha 100 (passo `5a`) e
      linha 140 (bullet de fronteira) — medidas em 2026-09-20, re-derivadas no despacho (`I-5`)
  - `.claude/agents/pantonic-planner.md`
    - **quatro** pontos, medidos em 2026-09-20 e re-derivados no despacho (`I-5`): o esqueleto
      do plano na Fase 3, linhas 165-167 (bloco D); o parágrafo `**O modelo antes das
      tarefas.**`, linhas 179-186 (bloco E); o item `4a` da Fase 4, linha 229 (bloco F); e o
      campo da anatomia do card, linha 363 (bloco G)
    - o `ESC-3` mediu que `grep -c 'Oração do modelo'` neste arquivo imprime **2**, nas linhas
      184 e 363, e que a 184 mora no parágrafo do bloco E — que o planejamento não havia
      citado (`AE-10`)
  - `.claude/agents/pantonic-consultant.md`
    - **dois** pontos, medidos em 2026-09-20: a linha `description:` do front matter, linha 3
      (bloco H); e o item 3 da lista "O que você faz", linhas 38-40 (bloco I)
  - `.claude/README.md`
    - só a região gerada, e só por instrumento (`I-7`): o bloco H muda a `description` de um
      agente, e a região gerada deriva de `name`, `model` e `description`
  - `.claude/skills/scrum-master/SKILL.md`
    - **três** regiões, medidas em 2026-09-20 e re-derivadas no despacho (`I-5`): o passo 6,
      linhas 111-116 (a frase que funda a conferência na regra `V6`); o passo 8, linha 149 (a
      linha `- **Saída:**`); e o passo 9, linhas 183-192 (a fundamentação do gate do modelo, que
      afirma que o reviewer acabou de gravar). O `ESC-2` mediu que a frase da regra `V6` **não**
      cabe numa linha só e que há uma segunda ocorrência dela no passo 9
- **Texto novo, literal — linha 5 de `.claude/agents/pantonic-reviewer.md`:**

  ```markdown
  tools: Read, Glob, Grep, Bash
  ```

- **Texto novo, literal — substituição do bullet da linha 47 de `pantonic-reviewer.md`:**

  ```markdown
  - **Você não escreve no modelo de domínio do plano** (`GOVERNANCA.md` §3.2;
    `docs/RUBRICA_DE_REVISAO.md` §7). Quando a entrega contradiz o texto de uma operação, o laudo
    leva `--achado-processo modelo "<operação e a divergência>"` e o texto fica como está. A escrita
    é do `pantonic-model-designer`, despachado por quem conduz a sessão.
  ```

- **Texto novo, literal — substituição integral do passo `5a` da linha 100 de `pantonic-reviewer.md`:**

  ```markdown
  5a. **Modelo de domínio** — leia o campo `Operação do modelo` do card. Para cada operação citada,
  compare o texto dela com o que está no repositório. Corresponde: nada a fazer — o andamento do
  modelo é derivado das tarefas e ninguém o grava. Não corresponde: o laudo leva
  `--achado-processo modelo "<operação e a divergência>"`, e você devolve, junto com o laudo, o
  dossiê `Ato de modelo` de `conflito` com os seis campos da norma. Você não abre o plano para
  escrever, em nenhuma hipótese. Plano em forma anterior, sem o campo `Operação do modelo`: nada a
  fazer.
  ```

- **Texto novo, literal — substituição do bullet da linha 140 de `pantonic-reviewer.md`:**

  ```markdown
  - Não escreve em nenhuma linha de nenhum plano. Divergência entre a entrega e o texto de uma
    operação vai como achado de alvo `modelo`, com o dossiê de conflito anexo à linha de retorno.
  ```

- **Texto novo, literal — `scrum-master`, bloco A: passo 6, substituindo da frase
  `**Confira, antes de invocar` até `materialize e só então invoque.` (linhas 111-116 em
  2026-09-20), preservando o que vem antes dela na mesma linha 111:**

  ```markdown
  **Confira, antes de invocar, que o status materializado da tarefa no plano é mesmo
  `review`** — é o estado em que o reviewer julga, e materializá-lo é ato do passo 5. O
  reviewer **não escreve** no modelo de domínio do plano: o andamento é derivado das tarefas e
  nenhum papel o grava (`GOVERNANCA.md` §3.2), então não há gravação de revisor a conferir
  aqui. Status diferente de `review` é defeito de condução do passo 5, não do revisor:
  materialize e só então invoque.
  ```

- **Texto novo, literal — `scrum-master`, bloco B: passo 8, substituindo integralmente a linha
  `- **Saída:** "segue" (vai ao passo 9) ou "PARA" (vai ao relatório de encerramento).`
  (linha 149 em 2026-09-20):**

  ```markdown
  - **Saída:** "segue" (vai ao passo 9) ou "PARA" (vai ao relatório de encerramento). Se a
    linha de retorno do reviewer trouxer um dossiê `Ato de modelo`, despache o
    `pantonic-model-designer` com esse dossiê **antes** de seguir ao passo 9: o texto do modelo
    se acerta com a tarefa ainda aberta, e o andamento, que é derivado, não trava nada no
    intervalo.
  ```

- **Texto novo, literal — `scrum-master`, bloco C: passo 9, substituindo o parágrafo do gate do
  modelo de `**Antes de materializar o status**` até `Exit \`0\` ou \`2\`: materializa e fecha.`
  — **linhas 183-192** em 2026-09-20, re-medidas no `ESC-3`: `**Antes de materializar o
  status**` está na 183 e `Exit \`0\` ou \`2\`: materializa e fecha.` na 192. A **chamada** e os
  **três exits** ficam byte a byte como estão; o que muda é a fundamentação, que hoje afirma
  que o reviewer acabou de gravar:**

  ```markdown
  **Antes de materializar o status**, e portanto antes de `rdo.py close`, rodar de novo
  `python .claude/tools/modelo.py check --plano <plano>`: o modelo de domínio do plano pode ter
  sido emendado pelo `pantonic-model-designer` desde o despacho (`GOVERNANCA.md` §3.2), e exit
  `1` aqui é defeito dessa emenda. Exit `1`: **não materializa e não fecha** — a tarefa
  **permanece em `review`**, o stderr vai ao consultor como escalonamento, e o fechamento
  espera o reparo. A tarefa fica em `review` porque é o estado em que o reviewer a julgou; para
  o **andamento** a escolha é indiferente, já que `review` e `in-progress` deixam a operação
  igualmente `em curso`. Exit `0` ou `2`: materializa e fecha.
  ```

- **Texto novo, literal — `pantonic-planner.md`, bloco D: esqueleto do plano na Fase 3,
  substituindo as **três** linhas da entrada `## 1. Modelo conceitual` do bloco cercado
  (linhas 165-167 em 2026-09-20). A indentação das linhas de continuação é de **34 espaços**,
  como no bloco vigente:**

  ```markdown
  ## 1. Modelo conceitual          (GOVERNANCA.md §3.2 — escrito pelo pantonic-model-designer ANTES
                                    de decompor: tabela de objetos, fluxo de operações OP-<n>, lista
                                    de mudanças MD-<n>; nada carrega estado; é o que o dono lê no
                                    Marco 1 e dá go/no-go)
  ```

- **Texto novo, literal — `pantonic-planner.md`, bloco E: substituição integral do parágrafo
  `**O modelo antes das tarefas.**`, da linha 179 (`**O modelo antes das tarefas.** A §1 se escreve`)
  à linha 186 (`` `no-go` o cancela antes da primeira tarefa.``), medidas em 2026-09-20:**

  ```markdown
  **O modelo antes das tarefas.** A §1 se escreve antes da §5, e **não é você quem a escreve**:
  o dono de todo ato sobre o modelo é o `pantonic-model-designer` (`GOVERNANCA.md` §3.2). Você
  devolve, na própria linha de retorno, o dossiê `Ato de modelo` de `autoria` — nenhum agente
  aciona outro, e quem conduz a sessão despacha o modelador. A forma está na gramática da skill
  `diario-de-obras` ("Modelo de domínio (seção do plano)"): tabela de objetos, cada um com o
  contrato que quem implementa precisa; fluxo de operações `OP-<n>` encadeadas, cada uma nomeando
  quem age, o que faz e de que objetos precisa; lista de mudanças `MD-<n>`. **Nenhum elemento da
  seção carrega estado** — o andamento é derivado das tarefas e o estágio atual é a primeira
  operação não concluída. Só então decompor: cada operação vira ≥ 1 card, e cada card cita ≥ 1
  operação no campo `Operação do modelo`, com o texto copiado e o contrato dos objetos de que ela
  precisa. O Marco 1 de todo plano é o dono lendo só a §1 — `go` aprova o plano, `no-go` o cancela
  antes da primeira tarefa.
  ```

- **Texto novo, literal — `pantonic-planner.md`, bloco F: substituição integral do item `4a` da
  Fase 4, que é **uma linha só** (linha 229 em 2026-09-20):**

  ```markdown
  4a. **Rastreabilidade do modelo** (`GOVERNANCA.md` §3.2): toda operação `OP-<n>` é citada por ≥ 1 card e todo card cita ≥ 1 operação existente, com o texto copiado e o sub-bullet `precisa de:`; nenhuma operação tem crase ou barra no texto; todo objeto citado existe na tabela de objetos, e nenhuma operação depende de objeto que só nasce depois dela; a auto-auditoria roda `python .claude/tools/modelo.py check --plano <plano>` e só publica com exit `0`. Renumeração da Fase 4 não é necessária: o item entra como `4a`.
  ```

- **Texto novo, literal — `pantonic-planner.md`, bloco G: substituição integral da linha do campo
  `- **Oração do modelo:**` na anatomia do card, que é **uma linha só** (linha 363 em 2026-09-20):**

  ```markdown
  - **Operação do modelo:** `OP-<a>`[, `OP-<b>`] — as operações da §1 que este card materializa; por operação citada, dois sub-bullets: `  - OP-<a>: <texto copiado>` e `  - precisa de: <objeto> — <contrato copiado>[; <objeto> — <contrato copiado>]`. Obrigatório (`modelo.py check`, `V2`, `V4`, `V14`).
  ```

- **Texto novo, literal — `pantonic-consultant.md`, bloco H: substituição integral da linha
  `description:` do front matter, que é **uma linha só** (linha 3 em 2026-09-20):**

  ```markdown
  description: Consultor de plano Pantonic*, instanciado UMA vez por execução de plano e mantido de standby com o cenário inteiro no contexto. Acionado a cada escalonamento para desbloquear impedimento de executor e reparar o plano, devolvendo ao loop o dossiê Ato de modelo quando a decisão exigir emenda do modelo de domínio - quem escreve no modelo é o pantonic-model-designer. Figura ad-hoc, provisória, criada por decisão do dono em 2026-09-18.
  ```

- **Texto novo, literal — `pantonic-consultant.md`, bloco I: substituição integral do item 3 da
  lista "O que você faz", da linha 38 (`3. **Repara o plano e emenda o modelo conceitual.**`) à
  linha 40 (`   disciplina que custou caro para ser aprendida:`), medidas em 2026-09-20. **Três
  linhas saem, duas entram**; os sub-bullets que vêm depois da linha 40 ficam como estão:**

  ```markdown
  3. **Repara o plano e devolve o dossiê de modelo.** Você edita o plano: decisão nova com id, cards reescritos, fila reordenada, achado absorvido com ponteiro. **Você não escreve na seção `## 1. Modelo conceitual`** — o dono de todo ato sobre o modelo é o `pantonic-model-designer` (`GOVERNANCA.md` §3.2). Quando a decisão muda o que o plano entrega ou como funciona, devolva na própria linha de retorno o dossiê `Ato de modelo` de `emenda`, com os seis campos da norma; quem conduz a sessão despacha o modelador, porque nenhum agente aciona outro. Vale para você, integralmente, a
     disciplina que custou caro para ser aprendida:
  ```

- **Passos:**
  1. **Conferir — não reaplicar** — os quatro literais de `pantonic-reviewer.md` (linhas 5, 47,
     100 e 140): o `ESC-3` mediu que a execução anterior **já os aplicou** antes de parar
     (`AE-10`). Imprimir as quatro regiões e confrontá-las com os blocos cercados. Idênticas:
     nada a fazer, e declarar assim na linha de retorno. Divergentes: aplicar o literal.
  2. Substituir as três linhas 165-167 de `pantonic-planner.md` pelo **bloco D**.
  3. Substituir o parágrafo das linhas 179-186 de `pantonic-planner.md` pelo **bloco E**.
  4. Substituir a linha 229 de `pantonic-planner.md` pelo **bloco F**.
  5. Substituir a linha 363 de `pantonic-planner.md` pelo **bloco G**.
  6. Substituir a linha 3 de `pantonic-consultant.md` pelo **bloco H**.
  7. Substituir as linhas 38-40 de `pantonic-consultant.md` pelo **bloco I** (três linhas saem,
     duas entram).
  8. Substituir, em `.claude/skills/scrum-master/SKILL.md`, as **três** regiões pelos blocos
     literais **A**, **B** e **C**, nessa ordem, cada uma localizada por conteúdo.
  9. Regenerar `.claude/README.md` com
     `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate`, porque o bloco H muda
     a `description` de um agente (`I-7`). Nenhuma edição à mão nesse arquivo.
  10. Imprimir cada região entregue com `sed -n '<a>,<b>p' <arquivo>` e confrontá-la linha a
      linha com o bloco cercado correspondente deste card; devolver a declaração de fidelidade
      do `I-11` na linha de retorno, uma por bloco.
  11. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - Nenhum agente aciona outro agente (`D-6`, `F-2`): nenhum texto escrito aqui pode mandar um
    agente invocar o modelador. Quem despacha é quem conduz a sessão.
  - As **chamadas** de `modelo.py check` das linhas 60 e 184 do `scrum-master` e os **três
    exits** de cada uma permanecem byte a byte como estão: os dois gates continuam válidos. O
    bloco C muda só a fundamentação em volta da chamada da linha 184, que hoje afirma que o
    reviewer acabou de gravar — afirmação que morre com `D-8`.
  - Cada bloco literal entra verbatim e é confrontado com o entregue (`I-11`): divergência de um
    token é defeito de transcrição, mesmo sem mudança de semântica (`AE-8`).
  - Texto entra verbatim dos blocos literais acima (`I-3`).
  - **Nenhum passo deste card manda redigir texto normativo novo.** Todo ponto a mudar tem bloco
    cercado: quatro no reviewer, A/B/C no `scrum-master`, D/E/F/G no planejador e H/I no
    consultor. Se algum ponto que o card manda mudar **não** tiver bloco correspondente, o card
    está incompleto: **não redija** — sinalize `blocked` razão `premissa`, nomeando o ponto
    (`G-NOASK`; foi assim que o `AE-10` foi apanhado, e a conduta é a correta).
  - Os quatro recortes de linha de `pantonic-reviewer.md` orientam a edição, **não** delimitam o
    aceite (`I-10`): o card fecha com o arquivo inteiro coerente — nenhuma frase dele pode
    descrever o revisor como quem escreve no modelo. Medido em 2026-09-20: as três frases dessa
    classe estão nas linhas 47, 100 e 140, e `Edit` aparece uma vez só, na linha `tools:`.
  - Nenhuma contingência deste card cria arquivo. Se alguma só puder ser cumprida criando
    arquivo não declarado nos `Arquivos-alvo`, o card está incompleto: sinalizar `blocked` razão
    `premissa` (`I-10`).
  - Não commitar (`I-6`).
- **Não fazer:**
  - Não remover `Edit` de `pantonic-consultant.md`: o consultor repara o plano fora da seção do
    modelo, e essa escrita continua.
  - Não reescrever o passo 3 do `scrum-master`, nem nenhuma outra parte do passo 9 além do
    parágrafo do bloco C.
  - Não tocar `.claude/tools/*` nem `README.md` (a raiz). `.claude/README.md` é outro arquivo
    (`I-9`) e se toca **só** pelo instrumento do passo 9.
  - Não tocar as linhas 144-145 de `pantonic-planner.md`, que contam o caso medido do `P-0741`:
    são **fato histórico verdadeiro** sobre um plano fechado, não descrição da forma vigente
    (`D-10`). A palavra `orações` ali fica.
  - Não acrescentar ao `scrum-master` nenhuma instrução sobre o driver do `P-0742`: aquele plano
    transcreve esta skill literalmente (`F-15`), e a edição viaja sozinha.
- **Contingências:**
  1. Se `pantonic-reviewer.md` usar `Edit` em algum passo que não seja a escrita no modelo →
     parar e sinalizar `blocked` razão `premissa`, com a linha encontrada.
  2. Se as linhas medidas não casarem com o conteúdo descrito → localizar por
     `grep -n 'V6' .claude/skills/scrum-master/SKILL.md`, que em 2026-09-20 imprime **duas**
     linhas: a 113 (região do bloco A) e a 188 (região do bloco C). Ambas somem com os blocos A
     e C. Ocorrência de `V6` em qualquer outra região → parar e sinalizar `blocked` razão
     `premissa`, com as linhas encontradas.
  3. Se as linhas medidas de `pantonic-planner.md` ou de `pantonic-consultant.md` não casarem
     com o conteúdo descrito nos blocos D..I → localizar cada ponto por conteúdo e seguir. Se
     `grep -n 'Oração do modelo' .claude/agents/pantonic-planner.md` imprimir alguma linha que
     **não** esteja nas regiões dos blocos E e G → parar e sinalizar `blocked` razão `premissa`,
     com as linhas encontradas. Medido em 2026-09-20: imprime exatamente 184 e 363.
  4. Se `kit_check.ps1 -Mode generate` sair diferente de `0` no passo 9 → parar e sinalizar
     `blocked` razão `ferramenta`, com a saída literal na linha de retorno.
- **Testes:** nenhum teste automatizado — a entrega é definição de conduta. A aferição é a
  verificação abaixo.
- **Verificação:**

  > **Nota de `I-5`, medida no `ESC-3` em 2026-09-20.** A execução que parou em `blocked`
  > **já aplicou os quatro literais de `pantonic-reviewer.md`**. Os três primeiros comandos
  > abaixo **já devolvem o valor de chegada** — `1`, `0` e `0` —, e os "hoje imprime" deles
  > descrevem a árvore de antes daquela execução. Isso não é defeito: é o estado parcial de
  > que o passo 1 parte. Todos os demais números seguem valendo como referência a re-derivar.

  ```
  grep -c 'tools: Read, Glob, Grep, Bash$' .claude/agents/pantonic-reviewer.md
  ```
  imprime `1` (hoje imprime `0`, porque a linha termina em `Bash, Edit`).

  ```
  grep -c 'Oração do modelo' .claude/agents/pantonic-reviewer.md .claude/agents/pantonic-planner.md
  ```
  imprime `0` para os dois arquivos. No planejador são **duas** ocorrências, nas linhas 184
  (bloco E) e 363 (bloco G), medidas em 2026-09-20; no reviewer era uma, na linha 100, e a
  execução anterior já a fechou.

  ```
  grep -c 'Operação do modelo' .claude/agents/pantonic-planner.md
  ```
  imprime `2` ou mais (hoje imprime `0`, medido 2026-09-20): o campo novo aparece no bloco E e
  no bloco G.

  ```
  grep -c -e 'estado: prevista' -e 'orações M-<n> com estado' .claude/agents/pantonic-planner.md
  ```
  imprime `0` (hoje imprime `2`, nas linhas 166 e 182, medido 2026-09-20). É o aceite que o
  `AE-10` faltou ter: a §5 deste plano proíbe estado gravado, e o planejador o prescrevia.

  ```
  grep -c 'emenda o modelo conceitual' .claude/agents/pantonic-consultant.md
  ```
  imprime `0` (hoje imprime `1`, na linha 38, medido 2026-09-20).

  ```
  grep -c 'pantonic-model-designer' .claude/agents/pantonic-reviewer.md .claude/skills/scrum-master/SKILL.md
  ```
  imprime `1` ou mais para os dois arquivos (hoje imprime `0` para os dois).

  ```
  pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift
  ```
  sai `0` e anuncia `(10 agente(s), 11 skill(s))` **depois** do passo 9. Atenção: a mudança de
  `tools:` do reviewer não altera a região gerada, mas o **bloco H altera**, porque a região
  deriva de `name`, `model` e `description` — sem o passo 9 este guarda acusa drift, e isso é
  defeito de execução, não do card.

  ```
  grep -c -e 'única escrita sua' -e 'emenda oração' -e 'Confirmar oração' .claude/agents/pantonic-reviewer.md
  ```
  imprime `0` (hoje imprime `2`, nas linhas 47 e 140, medido 2026-09-20 — ambas são alvo de
  substituição literal deste card). É o aceite de coerência do arquivo inteiro (`I-10`).

  ```
  grep -c 'Edit' .claude/agents/pantonic-reviewer.md
  ```
  imprime `0` (hoje imprime `1`, só na linha `tools:` — medido 2026-09-20; nenhum passo do corpo
  usa `Edit`, então a contingência 1 não deve disparar).

  ```
  grep -c 'V6' .claude/skills/scrum-master/SKILL.md
  ```
  imprime `0` (hoje imprime `2`, nas linhas 113 e 188, medido 2026-09-20 — a 113 some com o
  bloco A e a 188 com o bloco C).

  ```
  grep -c -e 'reviewer acabou de gravar' -e 'confirmação ou emenda' .claude/skills/scrum-master/SKILL.md
  ```
  imprime `0` (hoje imprime `2`, nas linhas 184 e 185, medido 2026-09-20). É o aceite de
  coerência do arquivo inteiro (`I-10`): nenhuma linha do `scrum-master` pode seguir afirmando
  que o reviewer grava no modelo depois de `D-8`.

  Imprimir cada uma das seis regiões entregues — as quatro de `pantonic-reviewer.md` e as três
  do `scrum-master`, com `sed -n '<a>,<b>p' <arquivo>` — e confrontá-las linha a linha com os
  blocos cercados A, B e C e com os literais do reviewer.
  Devolver na linha de retorno a declaração de fidelidade do `I-11`:
  `fidelidade conferida: <bloco> — <n> linhas idênticas ao bloco cercado do card`, uma por
  bloco literal deste card. **Divergência de um único token é defeito de transcrição (`I-3`),
  ainda que a semântica não mude** — foi assim que o `AE-8` passou por 11/11 greps verdes.


  `python .claude/tools/backlog.py check` imprime `check: OK — nenhuma violação.` e sai `0`.
- **Pronto quando:** o reviewer não tem `Edit` em nenhuma linha do arquivo e os quatro trechos
  dele conferem com os literais; os blocos D..I estão aplicados; o `scrum-master` carrega A, B e
  C; `.claude/README.md` foi regenerado por instrumento e `check-drift` sai `0`; **nenhuma frase
  de nenhum dos cinco arquivos** descreve o revisor, o planejador ou o consultor escrevendo no
  modelo, cita `Oração do modelo` ou prescreve estado gravado (`I-10`); e a linha de retorno traz
  a declaração de fidelidade do `I-11` por bloco.
- **Fora do escopo desta tarefa:** a documentação pública (`DOM-T6`) e qualquer ato de modelo sobre
  plano real.

### DOM-T5a — A costura do retorno do revisor [Sonnet · esforço low · classe implementacao]
- **Status:** `done` · 2026-09-20
- **Depende de:** `DOM-T5`
- **Objetivo:** o passo 7 de `.claude/agents/pantonic-reviewer.md` deixando de proibir o que o passo
  `5a` e o bullet de fronteira do mesmo arquivo mandam fazer — o dossiê `Ato de modelo` de
  `conflito` volta a caber na linha de retorno, que é de onde o bloco B do `scrum-master` o lê.
- **Fundamento:** `D-5`, `D-6`, `D-8`, `D-21`; invariantes `I-3`, `I-11`, `I-13`; achado `AE-11`.
  Card corretivo criado no escalonamento `ESC-4` (consultor de plano, 2026-09-20): a `DOM-T5` nomeou
  **quatro** pontos no reviewer e não deu bloco literal para o **quinto**; a execução acertou em não
  redigir (`I-13`) e o laudo saiu `aprovado 100%` com recomendação `escalar`.
- **Operação do modelo:** `OP-6`
  - OP-6: O autor de papéis alinha os demais papéis à norma: o revisor perde a escrita no modelo, e quem precisa de um ato devolve o dossiê fechado na própria linha de retorno, que quem conduz a sessão despacha.
  - precisa de: norma do modelo de domínio — residência única em `GOVERNANCA.md` §3.2; prosa normativa em blocos que substituem parágrafos nomeados, sem recopiar a gramática nem o ensinamento de autoria; nenhum outro documento a repete; modelador — `.claude/agents/pantonic-model-designer.md`; front matter com nome, descrição e lista de ferramentas, e corpo com os atos, o ensinamento e o gate; as duas portas de inventário do kit contam os agentes e hoje fecham sobre dez
- **Camada e fronteira:** definição de agente, em `.claude/agents/`. Nenhum código, nenhum teste,
  nenhuma mudança de front matter — portanto **nenhum drift** em `.claude/README.md`.
- **Contratos/classes:** nenhum.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-reviewer.md`
    - **um** ponto: o item 7 da lista de passos, `**Retorno ao chamador**`, linhas 127-135 em
      2026-09-20, do `7. **Retorno ao chamador**` até `pendência ao dono ficam no laudo, que é onde
      eles têm leitor.` — nove linhas, re-derivadas no despacho (`I-5`)
- **Texto novo, literal — bloco J: substituição integral do item 7 de
  `.claude/agents/pantonic-reviewer.md` (linhas 127-135). O bloco traz uma cerca interna de três
  crases, por isso a cerca externa aqui é de quatro; transcreva o **conteúdo**, não a cerca externa:**

  ````markdown
  7. **Retorno ao chamador** — as duas linhas fixas e, quando houver, o dossiê:

     ```
     <tarefa> <veredito> <percentual> bloqueante=<dimensão|nenhuma>
     laudo=<caminho>
     ```

     **Nada além disso, com uma exceção fechada:** se o passo `5a` apurou divergência entre a
     entrega e o texto de uma operação, anexe **abaixo** das duas linhas o dossiê `Ato de modelo`
     de `conflito`, com os seis campos da norma (`GOVERNANCA.md` §3.2). É esse dossiê que quem
     conduz a sessão lê para despachar o `pantonic-model-designer`; sem ele, a divergência fica só
     no laudo e o texto do modelo nunca é acertado. Você **não aciona** o modelador — devolve o
     dossiê e para.

     O motivo de cada dimensão fora de `conforme`, os achados de processo com alvo e rota e a
     pendência ao dono ficam no laudo, que é onde eles têm leitor.
  ````

- **Passos:**
  1. Imprimir a região vigente com `sed -n '127,135p' .claude/agents/pantonic-reviewer.md` e
     confrontá-la com o bloco J, para confirmar as âncoras antes de editar.
  2. Substituir as linhas 127-135 pelo conteúdo do bloco J, verbatim (`I-3`), preservando a
     indentação de três espaços das linhas de continuação do item 7, que é a do arquivo.
  3. Imprimir a região entregue e devolver, na linha de retorno, o **sinal**
     `fidelidade conferida: bloco J` — sinal, não prova: a prova são os comandos da `Verificação`
     (`I-11`).
  4. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - **Um bloco literal por ponto** (`I-13`): este card muda **um** ponto e traz **um** bloco. Se a
    execução concluir que algum outro ponto do arquivo precisa mudar, **não redija** — sinalize
    `blocked` razão `premissa`, nomeando a linha (`D-20`).
  - Nada de front matter: `name`, `model`, `description` e `tools` do reviewer ficam como a
    `DOM-T5` os deixou. `tools` continua **sem** `Edit` (`D-8`).
  - Não tocar `.claude/README.md`: sem mudança de front matter não há região gerada a regenerar
    (`I-7`, `I-9`).
  - Texto entra verbatim do bloco J (`I-3`); a prova de fidelidade é comando, não declaração
    (`I-11`).
  - Nenhuma contingência deste card cria arquivo (`I-10`).
  - Não commitar (`I-6`).
- **Não fazer:**
  - Não tocar os passos `5a` (linha 107) nem o bullet de fronteira (linha 150): eles já estão
    corretos, são entrega aprovada da `DOM-T5`, e é o passo 7 que os contradizia.
  - Não tocar `.claude/skills/scrum-master/SKILL.md`: o bloco B já lê o dossiê e está aprovado.
  - Não tocar `.claude/agents/pantonic-planner.md`, `pantonic-consultant.md`, `README.md`,
    `GOVERNANCA.md` nem `docs/RUBRICA_DE_REVISAO.md`.
  - Não acrescentar ao reviewer nenhuma instrução de despachar agente: quem despacha é quem conduz
    a sessão (`D-6`).
- **Contingências:**
  1. Se as linhas 127-135 não casarem com o conteúdo descrito → localizar o item 7 por
     `grep -n 'Retorno ao chamador' .claude/agents/pantonic-reviewer.md`, que em 2026-09-20 imprime
     **uma** linha, a 127, e seguir a partir dela até a linha anterior a `## Proibições` (137 em
     2026-09-20). Mais de uma ocorrência → parar e sinalizar `blocked` razão `premissa`.
- **Testes:** nenhum teste automatizado — a entrega é definição de conduta.
- **Verificação:**

  ```
  grep -c 'duas linhas, nada além' .claude/agents/pantonic-reviewer.md
  ```
  imprime `0` (hoje imprime `1`, na linha 127, medido 2026-09-20). É a frase que contradizia o
  passo `5a`.

  ```
  grep -c 'as duas linhas fixas e, quando houver, o dossiê' .claude/agents/pantonic-reviewer.md
  ```
  imprime `1` (hoje imprime `0`) — **primeira** linha do bloco J.

  ```
  grep -c 'pendência ao dono ficam no laudo, que é onde eles têm leitor.' .claude/agents/pantonic-reviewer.md
  ```
  imprime `1` (hoje imprime `1`, **inalterado**) — **última** linha do bloco J: o fim da região não
  se perde na substituição.

  ```
  grep -c 'devolve o dossiê e para.' .claude/agents/pantonic-reviewer.md
  ```
  imprime `1` (hoje imprime `0`).

  ```
  grep -c 'Ato de modelo' .claude/agents/pantonic-reviewer.md
  ```
  imprime `2` (hoje imprime `1`, na linha 107, medido 2026-09-20): o passo `5a` e o passo 7.

  ```
  sed -n '127,142p' .claude/agents/pantonic-reviewer.md
  ```
  sai idêntico, linha a linha, ao conteúdo do bloco J deste card — **é este comando, e não a
  declaração do executor, que prova a fidelidade** (`I-11`). Quem revisa confronta a saída contra o
  bloco; contagem de linhas autodeclarada não é evidência (`AE-12`).

  ```
  grep -c 'Edit' .claude/agents/pantonic-reviewer.md
  ```
  imprime `0` (hoje imprime `0`, **inalterado**): o card não devolve ferramenta de escrita ao
  revisor.

  ```
  pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift
  ```
  sai `0` e anuncia `(10 agente(s), 11 skill(s))` — **inalterado** (hoje idem, medido 2026-09-20):
  sem mudança de front matter não há drift.
- **Pronto quando:** os sete greps devolvem os números declarados, `sed -n '127,142p'` sai idêntico
  ao bloco J, `check-drift` sai `0`, e **nenhuma linha de `pantonic-reviewer.md` proíbe o que outra
  linha dele manda** — a cadeia revisor → loop → modelador fecha. O `Pronto quando` **não** se
  apoia em nenhuma frase escrita pelo executor sobre a própria entrega (`I-11`, `AE-12`).
- **Fora do escopo desta tarefa:** a documentação pública e o `README.md` (`DOM-T6`), qualquer outra
  linha de `pantonic-reviewer.md`, e qualquer ato de modelo sobre plano real.

### DOM-T5b — A cadeia do retorno, do emissor ao consumidor [Sonnet · esforço medium · classe implementacao]
- **Status:** `done` · 2026-09-20
- **Depende de:** `DOM-T5a`
- **Objetivo:** os cinco pontos que ainda proíbem, contam ou transportam a linha de retorno do
  revisor alinhados entre si, de ponta a ponta: a definição do papel, o **despacho** do passo 6, a
  **leitura** do passo 7 e o que o passo 7 entrega ao passo 8 — de modo que o dossiê `Ato de
  modelo` que o bloco B do passo 8 consome possa existir.
- **Fundamento:** `D-5`, `D-6`, `D-8`, `D-23`; invariantes `I-3`, `I-11`, `I-13`, `I-14`; achados
  `AE-11`, `AE-13`, `AE-14`. Card corretivo criado no escalonamento `ESC-5` (consultor de plano,
  2026-09-20). A `DOM-T5a` fechou a contradição **dentro** de `pantonic-reviewer.md`; o
  `scrum-master` a reimpõe no ato do despacho, que é onde a instrução de fato vincula o revisor.
  **Este card fecha a cadeia inteira de uma vez**, e não o próximo elo.
- **Operação do modelo:** `OP-6`
  - OP-6: O autor de papéis alinha os demais papéis à norma: o revisor perde a escrita no modelo, e quem precisa de um ato devolve o dossiê fechado na própria linha de retorno, que quem conduz a sessão despacha.
  - precisa de: norma do modelo de domínio — residência única em `GOVERNANCA.md` §3.2; prosa normativa em blocos que substituem parágrafos nomeados, sem recopiar a gramática nem o ensinamento de autoria; nenhum outro documento a repete; modelador — `.claude/agents/pantonic-model-designer.md`; front matter com nome, descrição e lista de ferramentas, e corpo com os atos, o ensinamento e o gate; as duas portas de inventário do kit contam os agentes e hoje fecham sobre dez
- **Camada e fronteira:** skill de orquestração e definição de agente. Nenhum código, nenhum teste,
  **nenhuma mudança de front matter** — portanto nenhum drift em `.claude/README.md`.
- **Contratos/classes:** nenhum. O contrato que muda é o **da linha de retorno do revisor**, e ele
  já está escrito em `GOVERNANCA.md` §3.2: duas linhas fixas e, quando houver, o dossiê `Ato de
  modelo` de seis campos anexo abaixo delas.
- **A cadeia, medida no `ESC-5` em 2026-09-20.** Emissor → meio → consumidor, com o estado de cada
  elo. É esta tabela que o aceite percorre (`I-14`):

  | elo | residência | estado hoje |
  |---|---|---|
  | norma | `GOVERNANCA.md` §3.2, tabela de papéis e o parágrafo "Nenhum agente aciona outro agente" | **correto** — a linha do revisor diz o que ele faz diante do modelo, e o parágrafo seguinte já manda devolver o dossiê na própria linha de retorno. **Não se toca** |
  | rubrica | `docs/RUBRICA_DE_REVISAO.md` §6, alvo `modelo` | **correto** — "dossiê de conflito, devolvido junto com o laudo e despachado pelo `pantonic-model-designer` por quem conduz a sessão". **Não se toca** |
  | emissor, domínio de saída | `pantonic-reviewer.md:51-52` | **defeituoso** — conta só duas linhas. Bloco **O** |
  | emissor, apuração | `pantonic-reviewer.md:107` (passo `5a`) | **correto**, entrega da `DOM-T5`. Não se toca |
  | emissor, retorno | `pantonic-reviewer.md:127` (passo 7) | **correto**, entrega da `DOM-T5a`. Não se toca |
  | emissor, fronteira | `pantonic-reviewer.md:150` | **correto**, entrega da `DOM-T5`. Não se toca |
  | despacho | `scrum-master` passo 6, ação, linhas 127-128 | **defeituoso** — instrui a devolver só duas linhas. Bloco **K** |
  | despacho, saída | `scrum-master` passo 6, linha 129 | **defeituoso** — conta duas linhas. Bloco **L** |
  | leitura, entrada | `scrum-master` passo 7, linhas 134-136 | **defeituoso** — declara duas linhas fixas e nada mais. Bloco **M** |
  | leitura, saída | `scrum-master` passo 7, linha 141 | **defeituoso** — a tripla não carrega o dossiê ao passo 8. Bloco **N** |
  | roteamento | `scrum-master` passo 8, linha 150 (bloco B) | **correto**, entrega da `DOM-T5`. Não se toca |
  | gate de fechamento | `scrum-master` passo 9 (bloco C) | **correto**, entrega da `DOM-T5`. Não se toca |

- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
    - **quatro** pontos, medidos em 2026-09-20 e re-derivados no despacho (`I-5`): passo 6 ação,
      linhas 127-128 (bloco K); passo 6 saída, linha 129 (bloco L); passo 7 entrada, linhas 134-136
      (bloco M); passo 7 saída, linha 141 (bloco N)
  - `.claude/agents/pantonic-reviewer.md`
    - **um** ponto: o bullet `- Saída:` do domínio de saída, linhas 51-52 (bloco O)
- **Texto novo, literal — bloco K: `scrum-master`, passo 6, substituição integral das linhas
  127-128, que começam em `Redirecionar a saída padrão do comando.`:**

  ```markdown
  Redirecionar a saída padrão do comando. Em seguida invocar `pantonic-reviewer` com o dossiê da
  tarefa e o caminho do dossiê de evidência. **Não limite o retorno dele às duas linhas.**
  A forma do retorno é a que a definição do papel fixa: as duas linhas de veredito e, quando o
  passo `5a` apurar divergência, o dossiê `Ato de modelo` de `conflito` anexo abaixo delas
  (`GOVERNANCA.md` §3.2). É esse dossiê que o passo 8 consome para despachar o modelador.
  ```

- **Texto novo, literal — bloco L: `scrum-master`, passo 6, substituição integral da linha 129,
  que é **uma linha só**:**

  ```markdown
  - **Saída:** as duas linhas do `reviewer` e, quando houver, o dossiê `Ato de modelo` anexo.
  ```

- **Texto novo, literal — bloco M: `scrum-master`, passo 7, substituição integral das linhas
  134-136 (o bullet `- **Entrada:**` e as duas linhas de forma que vêm sob ele):**

  ```markdown
  - **Entrada:** as duas linhas fixas e, quando houver, o dossiê anexo abaixo delas:
    `<tarefa> <veredito> <percentual> bloqueante=<dimensão|nenhuma>`
    `laudo=<caminho>`
    Dossiê presente: são os seis campos do `Ato de modelo` (`GOVERNANCA.md` §3.2). O loop não o
    reescreve, não o resume e não o interpreta — passa-o inteiro ao passo 8.
  ```

- **Texto novo, literal — bloco N: `scrum-master`, passo 7, substituição integral da linha 141,
  que é **uma linha só**:**

  ```markdown
  - **Saída:** tripla (`veredito`, `bloqueante`, `recomendação`) para o roteamento, mais o dossiê `Ato de modelo` quando ele veio no retorno.
  ```

- **Texto novo, literal — bloco O: `pantonic-reviewer.md`, substituição integral do bullet
  `- Saída:` das linhas 51-52:**

  ```markdown
  - Saída: as duas linhas de veredito ao chamador, o dossiê `Ato de modelo` de `conflito` quando o
    passo 7 o exigir, e o laudo em documento próprio, gravado pelo gerador
    em `docs/RDO/laudos/<plano>-<tarefa>.md`.
  ```

- **Nota de autoria sobre os literais de aceite (`AE-1`, `AE-13`).** Cada literal citado na
  `Verificação` abaixo cabe **inteiro numa linha só** do bloco correspondente — nenhum atravessa
  quebra de linha, e a conferência foi feita bloco a bloco no `ESC-5`. E **todo comando de aceite
  deste card usa `grep -cF -e`**: `-F` porque os literais têm `**`, que não é literal em expressão
  regular; `-e` porque cinco deles **começam por `-`**, e sem `-e` o `grep` os lê como opção e
  falha com `unknown option`. Medido no `ESC-5`: sem o `-e`, os cinco comandos abortam.
- **Passos:**
  1. Substituir as linhas 127-128 de `.claude/skills/scrum-master/SKILL.md` pelo **bloco K**.
  2. Substituir a linha 129 pelo **bloco L**.
  3. Substituir as linhas 134-136 pelo **bloco M**.
  4. Substituir a linha 141 pelo **bloco N**.
  5. Substituir as linhas 51-52 de `.claude/agents/pantonic-reviewer.md` pelo **bloco O**.
  6. Percorrer a cadeia inteira com o comando de residuo da `Verificação` e conferir que os elos
     marcados **correto** na tabela acima seguem intocados.
  7. Imprimir cada região entregue e devolver, na linha de retorno, o **sinal**
     `fidelidade conferida: bloco K, L, M, N, O` — sinal, não prova (`I-11`).
  8. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - **Um bloco literal por ponto** (`I-13`): cinco pontos, cinco blocos. Nenhum passo manda redigir.
  - **Tripwire de replanejamento (`D-23`).** A tabela da cadeia acima é **exaustiva**, medida no
    `ESC-5`. Se a execução encontrar um **sexto** ponto da mesma família — frase que proíba, conte
    ou transporte a linha de retorno do revisor e que não esteja na tabela —, **não corrija e não
    redija**: pare, sinalize `blocked` razão `premissa` e devolva a linha encontrada. Um sexto
    ponto significa que a superfície não está delimitada, e a resposta é **replanejar**, não um
    sexto card corretivo.
  - Nada de front matter em nenhum dos dois arquivos; `tools` do reviewer continua **sem** `Edit`
    (`D-8`). Sem mudança de front matter não há região gerada a regenerar (`I-7`, `I-9`).
  - Texto entra verbatim dos cinco blocos (`I-3`); a prova de fidelidade é comando, não declaração
    (`I-11`).
  - Nenhuma contingência deste card cria arquivo (`I-10`).
  - Não commitar (`I-6`).
- **Não fazer:**
  - Não tocar `GOVERNANCA.md` §3.2 nem `docs/RUBRICA_DE_REVISAO.md` §6: os dois elos de norma da
    tabela foram conferidos no `ESC-5` e **estão corretos**. A linha do revisor na tabela de papéis
    da §3.2 descreve o que ele faz **diante do modelo**, e o parágrafo seguinte já manda devolver o
    dossiê na própria linha de retorno — não há omissão a fechar ali.
  - Não tocar os passos `5a` (107), 7 (127) e o bullet de fronteira (150) de `pantonic-reviewer.md`:
    entregas aprovadas da `DOM-T5` e da `DOM-T5a`.
  - Não tocar os blocos B (passo 8, linha 150) e C (passo 9) do `scrum-master`: entregas aprovadas.
  - Não tocar `.claude/agents/pantonic-planner.md`, `pantonic-consultant.md`,
    `pantonic-model-designer.md`, `README.md` nem `.claude/README.md`.
  - Não acrescentar a nenhum agente instrução de despachar outro agente (`D-6`).
- **Contingências:**
  1. Se alguma das cinco faixas não casar com o conteúdo descrito → localizar o ponto por conteúdo,
     com os literais de saída da `Verificação`, e seguir. Se um literal de saída imprimir mais de
     `1` → parar e sinalizar `blocked` razão `premissa`, com as linhas encontradas.
- **Testes:** nenhum teste automatizado — a entrega é definição de conduta e de orquestração.
- **Verificação:**

  Os cinco literais que **saem** — todos medidos em 2026-09-20, cada um numa linha só do destino:

  ```
  grep -cF -e 'instrução de devolver só as duas linhas de veredito.' .claude/skills/scrum-master/SKILL.md
  ```
  imprime `0` (hoje imprime `1`, na linha 128).

  ```
  grep -cF -e '- **Saída:** duas linhas do `reviewer`.' .claude/skills/scrum-master/SKILL.md
  ```
  imprime `0` (hoje imprime `1`, na linha 129).

  ```
  grep -cF -e '- **Entrada:** as duas linhas fixas:' .claude/skills/scrum-master/SKILL.md
  ```
  imprime `0` (hoje imprime `1`, na linha 134).

  ```
  grep -cF -e '- **Saída:** tripla (`veredito`, `bloqueante`, `recomendação`) para o roteamento.' .claude/skills/scrum-master/SKILL.md
  ```
  imprime `0` (hoje imprime `1`, na linha 141).

  ```
  grep -cF -e '- Saída: duas linhas de veredito ao chamador e o laudo em documento próprio' .claude/agents/pantonic-reviewer.md
  ```
  imprime `0` (hoje imprime `1`, na linha 51).

  Os cinco literais que **entram** — a borda de cada bloco:

  ```
  grep -cF -e '**Não limite o retorno dele às duas linhas.**' .claude/skills/scrum-master/SKILL.md
  ```
  imprime `1` (hoje imprime `0`).

  ```
  grep -cF -e '- **Saída:** as duas linhas do `reviewer` e, quando houver, o dossiê' .claude/skills/scrum-master/SKILL.md
  ```
  imprime `1` (hoje imprime `0`).

  ```
  grep -cF -e '- **Entrada:** as duas linhas fixas e, quando houver, o dossiê anexo abaixo delas:' .claude/skills/scrum-master/SKILL.md
  ```
  imprime `1` (hoje imprime `0`).

  ```
  grep -cF -e 'para o roteamento, mais o dossiê `Ato de modelo` quando ele veio no retorno.' .claude/skills/scrum-master/SKILL.md
  ```
  imprime `1` (hoje imprime `0`).

  ```
  grep -cF -e 'as duas linhas de veredito ao chamador, o dossiê' .claude/agents/pantonic-reviewer.md
  ```
  imprime `1` (hoje imprime `0`).

  A cadeia inteira, de ponta a ponta (`I-14`):

  ```
  grep -c -e 'só as duas linhas' -e 'somente as duas' -e 'só duas linhas' .claude/skills/scrum-master/SKILL.md .claude/agents/pantonic-reviewer.md
  ```
  imprime `0` para os dois arquivos (hoje o `scrum-master` imprime `1` e o reviewer `0`, medido
  2026-09-20). **Nenhuma linha de nenhum dos dois pode limitar o retorno do revisor a duas linhas.**

  ```
  grep -c 'Ato de modelo' .claude/skills/scrum-master/SKILL.md .claude/agents/pantonic-reviewer.md
  ```
  imprime `4` ou mais para o `scrum-master` (hoje `1`, o bloco B) e `3` ou mais para o reviewer
  (hoje `2`, o passo `5a` e o passo 7), medido 2026-09-20: os blocos K, M e N acrescentam três
  citações ao `scrum-master` e o bloco O uma ao reviewer.

  ```
  grep -cF -e 'Edit' .claude/agents/pantonic-reviewer.md
  ```
  imprime `0` (hoje imprime `0`, **inalterado**).

  As cinco regiões entregues, para confronto linha a linha com os blocos K, L, M, N e O (`I-11`
  item 1) — **é este comando, e não a declaração do executor, que prova a fidelidade**:

  ```
  sed -n '125,150p' .claude/skills/scrum-master/SKILL.md
  sed -n '49,55p' .claude/agents/pantonic-reviewer.md
  ```

  ```
  pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift
  ```
  sai `0` e anuncia `(10 agente(s), 11 skill(s))` — **inalterado** (hoje idem, medido 2026-09-20).
- **Pronto quando:** os cinco literais de saída imprimem `0`, os cinco de entrada imprimem `1`, o
  comando de cadeia imprime `0` para os dois arquivos, as contagens de `Ato de modelo` subiram como
  declarado, `check-drift` sai `0`, e **nenhum elo da tabela da cadeia contradiz outro** — a rota
  revisor → despacho → leitura → roteamento → modelador fecha de ponta a ponta. Nenhum item deste
  `Pronto quando` se apoia em frase escrita pelo executor sobre a própria entrega (`I-11`, `D-22`).
- **Fora do escopo desta tarefa:** a documentação pública e o `README.md` (`DOM-T6`), a norma e a
  rubrica (elos conferidos e corretos), e qualquer ato de modelo sobre plano real.

### DOM-T7 — A norma da forma nova: propriedades, estado e versão [Sonnet · esforço high · classe implementacao]
- **Status:** `done` · 2026-09-20
- **Depende de:** `DOM-T5b`
- **Nota de fila:** dependência corrigida de `DOM-T6` para `DOM-T5b` pela orquestração em 2026-09-20; a `DOM-T6` pertence ao Marco 5 e nada do terceiro estágio depende dela (§13.5). Ver `AE-16`
- **Objetivo:** `GOVERNANCA.md` `### 3.2` descrevendo o modelo como objetos **com propriedades**,
  com o teste decidível de objeto e operação, o estado inicial e final como aceite do plano, o
  versionamento vigente/pendente/obsoleta e a distinção entre medição e drift.
- **Fundamento:** `D-24`, `D-25`, `D-26`, `D-28`, `D-29`, `D-33`, `D-34`, `D-35`, `D-36`, `D-37`,
  `D-38`, `D-39`, `D-44`; invariantes `I-3`, `I-10`, `I-11`, `I-13`. O card transcreve a **§14**
  deste plano, residência única do texto. **O que muda nos papéis não está aqui** (`D-40`, `D-41`):
  é Marco 4, e depende da `Q-11`, aberta.
- **Operação do modelo:** `OP-7`
  - OP-7: O redator da norma reescreve a norma para propriedades: objeto passa a ser o que possui propriedade, o plano declara estado inicial e estado final, o aceite do plano é a confrontação dos dois, e a emenda ao modelo versiona em vez de reescrever.
  - precisa de: norma do modelo de domínio — residência única em `GOVERNANCA.md` §3.2; prosa normativa em blocos que substituem parágrafos nomeados, sem recopiar a gramática nem o ensinamento de autoria; nenhum outro documento a repete
- **Camada e fronteira:** doutrina publicada, na raiz. Nenhum código, nenhum teste.
- **Contratos/classes:** nenhum.
- **Arquivos-alvo:**
  - `GOVERNANCA.md`
    - **três** pontos da `### 3.2`, medidos em 2026-09-20 e re-derivados no despacho (`I-5`):
      o parágrafo `**O que é.**`, linhas 323-331 (bloco **P1**); a inserção imediatamente antes do
      parágrafo `**O contrato chega ao card.**`, linha 346 (bloco **P2**); o parágrafo
      `**Retroatividade.**`, linhas 370-373 (bloco **P3**)
- **Passos:**
  1. Substituir as linhas 323-331 pelo **bloco P1** da §14, verbatim (`I-3`).
  2. Inserir o **bloco P2** da §14 imediatamente antes da linha do parágrafo
     `**O contrato chega ao card.**`, separado dele por uma linha em branco.
  3. Substituir as linhas 370-373 pelo **bloco P3** da §14, verbatim.
  4. Imprimir as três regiões entregues e devolver, na linha de retorno, o **sinal**
     `fidelidade conferida: P1, P2, P3` — sinal, não prova (`I-11`).
  5. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - **Um bloco literal por ponto** (`I-13`): três pontos, três blocos. Nenhum passo manda redigir.
    Ponto que precise mudar e não tenha bloco → `blocked` razão `premissa`, nunca redação.
  - **Não tocar a tabela de papéis nem o parágrafo `Nenhum agente aciona outro agente`**: o ato
    `conflito` do modelador e a autoridade do consultor são Marco 4 e dependem da `Q-11`. Publicar
    metade da mudança de papéis é o defeito `AE-11`, que este plano já pagou duas vezes.
  - Não tocar `docs/RUBRICA_DE_REVISAO.md`, `.claude/tools/*`, `.claude/agents/*` nem
    `.claude/skills/*`.
  - Nenhuma contingência deste card cria arquivo (`I-10`).
  - Não commitar (`I-6`).
- **Não fazer:**
  - Não alterar os parágrafos `**Para quem é.**`, `**Estágio, não status.**`,
    `**O contrato chega ao card.**` e `**Quem escreve.**`: os quatro seguem verdadeiros.
  - Não renumerar nada da `### 3.2` nem de `## 3`.
- **Contingências:**
  1. Se alguma das três faixas não casar com o conteúdo descrito → localizar por conteúdo, com os
     literais de saída da `Verificação`. Se um literal de saída imprimir mais de `1` → parar e
     sinalizar `blocked` razão `premissa`, com as linhas encontradas.
- **Testes:** nenhum teste automatizado — a entrega é doutrina publicada.
- **Verificação:**

  Os literais que **saem**, cada um inteiro numa linha só do destino (`AE-1`, `AE-13`):

  ```
  grep -cF -e 'São três blocos, nesta ordem' GOVERNANCA.md
  ```
  imprime `0` (hoje imprime `1`, na linha 325, medido 2026-09-20).

  ```
  grep -cF -e '### 1.3 Mudanças do modelo' GOVERNANCA.md
  ```
  imprime `0` (hoje imprime `1`, medido 2026-09-20).

  Os literais que **entram**, cada um inteiro numa linha só do bloco:

  ```
  grep -cF -e 'objetos com propriedades' GOVERNANCA.md
  ```
  imprime `1` (hoje imprime `0`) — bloco P1.

  ```
  grep -cF -e 'Objeto é o que possui' GOVERNANCA.md
  ```
  imprime `1` (hoje imprime `0`) — bloco P2, primeiro parágrafo.

  ```
  grep -cF -e 'O aceite do plano é a confrontação dos dois' GOVERNANCA.md
  ```
  imprime `1` (hoje imprime `0`) — bloco P2, segundo parágrafo.

  ```
  grep -cF -e 'Medição e drift não são a mesma coisa' GOVERNANCA.md
  ```
  imprime `1` (hoje imprime `0`) — bloco P2, quarto parágrafo.

  ```
  grep -cF -e 'plano sem estado inicial e final' GOVERNANCA.md
  ```
  imprime `0` (hoje imprime `0`, **inalterado**): o literal de exit é do instrumento (`DOM-T9`) e
  **não** entra na norma.

  A cadeia interna da `### 3.2` (`I-14`): nenhuma linha dela pode afirmar que o modelador resolve
  conflito e, ao mesmo tempo, que não resolve.

  ```
  grep -cF -e 'resolução de conflito entre o texto e a entrega' GOVERNANCA.md
  ```
  imprime `1` (hoje imprime `1`, **inalterado**): a mudança de papéis é Marco 4.

  ```
  pwsh -NoProfile -File .claude/checks/check-readme.ps1
  ```
  sai `0` — o guarda confere as linhas `Fonte da verdade` das seções, e este card não mexe em
  nenhuma (hoje sai `0`, medido 2026-09-20).
- **Pronto quando:** os dois literais de saída imprimem `0`, os quatro de entrada imprimem `1`, o
  literal de papéis segue **inalterado** em `1`, `check-readme.ps1` sai `0`, e nenhuma linha da
  `### 3.2` descreve o modelo como tendo lista de mudanças. Nenhum item se apoia em frase escrita
  pelo executor sobre a própria entrega (`I-11`, `D-22`).
- **Fora do escopo desta tarefa:** a gramática (`DOM-T8`), o instrumento (`DOM-T9`), o modelo deste
  plano (`DOM-T10`), e tudo que muda papel (Marco 4).

### DOM-T8 — A gramática da forma nova [Sonnet · esforço high · classe implementacao]
- **Status:** `done` · 2026-09-20
- **Depende de:** `DOM-T7`
- **Objetivo:** a subseção `### Modelo de domínio (seção do plano)` da skill `diario-de-obras`
  lendo a forma nova: propriedades na tabela de objetos, `altera:` na operação, estado inicial e
  final no lugar da lista de mudanças, registro de versões e o bloco irmão `## 1A`.
- **Fundamento:** `D-24`, `D-25`, `D-28`, `D-29`, `D-33`, `D-34`, `D-35`, `D-37`; invariantes
  `I-3`, `I-10`, `I-11`, `I-13`. O card transcreve a **§15** deste plano. Depende da `DOM-T7`
  porque a gramática é a forma da norma: publicá-la antes abriria a janela em que as duas divergem,
  defeito medido na `MC-T1` e repetido no `AE-4`.
- **Operação do modelo:** `OP-8`
  - OP-8: O redator da gramática reescreve a gramática para a forma nova: propriedade na tabela de objetos, o que cada operação altera, o estado inicial e o final, o registro de versões, e a versão pendente como bloco irmão da vigente.
  - precisa de: norma do modelo de domínio — residência única em `GOVERNANCA.md` §3.2; prosa normativa em blocos que substituem parágrafos nomeados, sem recopiar a gramática nem o ensinamento de autoria; nenhum outro documento a repete; gramática do modelo — residência única na skill `diario-de-obras`, subseção `Modelo de domínio (seção do plano)`; uma linha de tabela por elemento, com a forma à esquerda e a regra mais o código de violação à direita
- **Camada e fronteira:** skill do kit, em `.claude/skills/`. Nenhum código, nenhum teste.
- **Contratos/classes:** nenhum.
- **Arquivos-alvo:**
  - `.claude/skills/diario-de-obras/SKILL.md`
    - **cinco** pontos, medidos em 2026-09-20 e re-derivados no despacho (`I-5`): a linha
      `| cabeçalho |`, 182 (bloco **G1**); a linha `| objetos |`, 183 (bloco **G2**); a linha
      `| operações |`, 184 (bloco **G3**); a linha `| mudanças |`, 185, que vira **duas** linhas
      (bloco **G4**); e a inserção imediatamente antes do parágrafo
      `**Andamento, nunca gravado.**`, 188 (bloco **G5**)
- **Passos:**
  1. Substituir a linha 182 pelo **bloco G1** da §15, verbatim (`I-3`).
  2. Substituir a linha 183 pelo **bloco G2**.
  3. Substituir a linha 184 pelo **bloco G3**.
  4. Substituir a linha 185 pelas **duas** linhas do **bloco G4**.
  5. Inserir o **bloco G5** imediatamente antes do parágrafo `**Andamento, nunca gravado.**`,
     separado dele por uma linha em branco.
  6. Imprimir as cinco regiões e devolver o **sinal** `fidelidade conferida: G1, G2, G3, G4, G5`.
  7. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - **Um bloco literal por ponto** (`I-13`): cinco pontos, cinco blocos.
  - A linha `| campo do card |` (186) **não muda**: a `V2` fica como está, e a `D-46` fechou a
    `Q-12` **mantendo-a intacta** — não é questão aberta que a protege, é decisão (`D-49`).
  - O preâmbulo da seção `## Gramática legível por máquina` **não muda**: ele já aponta para a §5
    deste plano, e a §15 é continuação dela, não substituição — a `DOM-T3a` fechou aquele ponto.
  - Não tocar `.claude/tools/*`: o instrumento aprende a gramática na `DOM-T9`, e **nesta ordem**
    (`AE-5`, `AE-6`: gramática nova não se aplica antes de o parser aprender — aqui a ordem é a
    inversa e proposital, porque a gramática é a residência que o instrumento lê).
  - Nenhuma contingência deste card cria arquivo (`I-10`). Não commitar (`I-6`).
- **Não fazer:**
  - Não alterar o parágrafo `**Andamento, nunca gravado.**`: ele segue verdadeiro, e o estado de
    que a §15 fala é o das **propriedades**, não o andamento das operações.
  - Não alterar a subseção `### Item e residência` nem nenhuma outra seção da skill.
- **Contingências:**
  1. Se alguma das cinco faixas não casar com o conteúdo descrito → localizar por conteúdo, com os
     literais de saída da `Verificação`. Literal de saída com mais de `1` → `blocked` razão
     `premissa`.
- **Testes:** nenhum teste automatizado — a entrega é gramática publicada. Quem a afere é a
  `DOM-T9`, que a implementa e traz os testes.
- **Verificação:**

  Literais que **saem**, cada um inteiro numa linha só:

  ```
  grep -cF -e '| mudanças | `### 1.3 Mudanças do modelo`' .claude/skills/diario-de-obras/SKILL.md
  ```
  imprime `0` (hoje imprime `1`, na linha 185, medido 2026-09-20).

  Literais que **entram**, cada um inteiro numa linha só do bloco:

  ```
  grep -cF -e '| estado | `### 1.3 Estado inicial e estado final`' .claude/skills/diario-de-obras/SKILL.md
  ```
  imprime `1` (hoje imprime `0`) — primeira linha do bloco G4.

  ```
  grep -cF -e '| versões | `### 1.4 Registro de versões`' .claude/skills/diario-de-obras/SKILL.md
  ```
  imprime `1` (hoje imprime `0`) — segunda linha do bloco G4.

  ```
  grep -cF -e 'propriedades \| contrato \| origem' .claude/skills/diario-de-obras/SKILL.md
  ```
  imprime `1` (hoje imprime `0`) — bloco G2, a coluna nova da tabela de objetos.

  ```
  grep -cF -e '## 1A. Modelo conceitual' .claude/skills/diario-de-obras/SKILL.md
  ```
  imprime `1` (hoje imprime `0`) — bloco G5.

  ```
  grep -cF -e '<p> propriedades · situação:' .claude/skills/diario-de-obras/SKILL.md
  ```
  imprime `1` (hoje imprime `0`) — bloco G1.

  ```
  grep -cF -e '| campo do card |' .claude/skills/diario-de-obras/SKILL.md
  ```
  imprime `1` (hoje imprime `1`, **inalterado**): a `V2` não é tocada.

  **Censo da subseção** (`D-50`), que é o que dá poder discriminante à cláusula do
  `Pronto quando` — o grep do heading sozinho não alcança a linha do cabeçalho:

  ```
  grep -c 'MD-' .claude/skills/diario-de-obras/SKILL.md
  ```
  imprime `0` (hoje imprime `2`, nas linhas 182 e 185, medido 2026-09-20).

  ```
  python .claude/tools/backlog.py check
  ```
  imprime `check: OK — nenhuma violação.` e sai `0`.
- **Pronto quando:** o literal de saída imprime `0`, os cinco de entrada imprimem `1`, a linha do
  campo do card segue **inalterada**, `backlog.py check` sai `0`, e **o censo do token imprime `0`**
  — é ele, e não juízo do executor, que afirma que nenhuma linha da subseção descreve o modelo como
  tendo lista de mudanças (`D-50`, `I-11`).
- **Fora do escopo desta tarefa:** o instrumento (`DOM-T9`), o modelo deste plano (`DOM-T10`), a
  `V2` e a `Q-12`, e tudo que muda papel (Marco 4).

### DOM-T8a — Os ponteiros que a forma nova deixou para trás [Sonnet · esforço medium · classe implementacao]
- **Status:** `done` · 2026-09-21
- **Depende de:** `DOM-T8`
- **Objetivo:** as quatro regiões da árvore que mandam o modelador devolver a linha `MD-<n>` — duas
  em `GOVERNANCA.md`, duas em `.claude/agents/pantonic-planner.md` — apontando para
  `### 1.4 Registro de versões`, que é onde o ato passa a ser registrado; e o preâmbulo da skill
  `diario-de-obras` nomeando a seção que de fato governa a gramática do modelo. Cinco ponteiros
  defasados, **nenhum deles mudando papel**.
- **Fundamento:** `D-24`, `D-28`, `D-29`, `D-48`, `D-49`, `D-50`, `D-51`; invariantes `I-3`, `I-4`,
  `I-5`, `I-11`, `I-13`. O card transcreve a **§17** deste plano. Nasceu do `AE-17`, no
  escalonamento `ESC-6`: a `DOM-T8` remove a última residência do token `MD-<n>` e quatro regiões
  continuavam exigindo-o, sem card que as re-declarasse. O quinto ponto entrou no `ESC-7`
  (`AE-18`): o preâmbulo da skill manda ler a §5 deste plano, que a §15 substituiu em quatro das
  seis linhas — **é ponteiro, não texto**, e por isso cabe aqui e não numa reabertura da `DOM-T8`,
  que fechou `aprovado 100%` e cujo aceite está satisfeito.
- **Operação do modelo:** `OP-9`
  - OP-9: O mantenedor reaponta cada região da doutrina que ainda mandava registrar o ato do modelo na forma que a versão substituiu, sem mudar o que papel nenhum faz.
  - precisa de: gramática do modelo — residência única na skill `diario-de-obras`, subseção `Modelo de domínio (seção do plano)`; uma linha de tabela por elemento, com a forma à esquerda e a regra mais o código de violação à direita; doutrina publicada do kit — `GOVERNANCA.md`, as skills e os agentes do kit; cada ponteiro nomeia a seção vigente que governa a forma, e ponteiro órfão é defeito no caminho da entrega, não dívida a pagar depois
- **Camada e fronteira:** doutrina (`GOVERNANCA.md`) e agente do kit (`.claude/agents/`). Nenhum
  código, nenhum teste.
- **Contratos/classes:** nenhum.
- **Arquivos-alvo:**
  - `GOVERNANCA.md`
    - **dois** pontos, medidos em 2026-09-20 e re-derivados no despacho (`I-5`): a linha
      `| **Modelagem** |` da matriz de responsabilidades da §3, 95 (bloco **R1**); e a linha
      `| modelador |` da tabela de papéis da `### 3.2`, 388 (bloco **R2**)
  - `.claude/agents/pantonic-planner.md`
    - **dois** pontos, medidos em 2026-09-20 e re-derivados no despacho (`I-5`): as quatro linhas
      do item `## 1. Modelo conceitual` do esqueleto da Fase 3, 165-168 (bloco **R3**); e o
      parágrafo `**O modelo antes das tarefas.**`, 180-191 (bloco **R4**)
  - `.claude/skills/diario-de-obras/SKILL.md`
    - **um** ponto, medido em 2026-09-21 e re-derivado no despacho (`I-5`): as duas linhas do
      preâmbulo de `## Gramática legível por máquina` que nomeiam a seção de origem da subseção do
      modelo, 135-136 (bloco **R5**). **A subseção `### Modelo de domínio (seção do plano)` não é
      tocada**: ela está correta desde a `DOM-T8`
- **Passos:**
  1. Substituir a linha 95 de `GOVERNANCA.md` pelo **bloco R1** da §17, verbatim (`I-3`).
  2. Substituir a linha 388 de `GOVERNANCA.md` pelo **bloco R2**.
  3. Substituir as linhas 165-168 de `pantonic-planner.md` pelas quatro linhas do **bloco R3**,
     preservando os **34** espaços de indentação das linhas de continuação.
  4. Substituir o parágrafo das linhas 180-191 de `pantonic-planner.md` pelo **bloco R4**.
  5. Substituir as linhas 135-136 de `.claude/skills/diario-de-obras/SKILL.md` pelas duas linhas
     do **bloco R5**.
  6. Imprimir as cinco regiões e devolver o **sinal** `fidelidade conferida: R1, R2, R3, R4, R5`.
  7. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - **Um bloco literal por ponto** (`I-13`): cinco pontos, cinco blocos.
  - **Nenhuma atribuição de papel muda** (`D-48`). O ato `conflito` **permanece** na linha 95 e na
    tabela de papéis; nenhuma linha entra na tabela de papéis e nenhuma sai; nenhuma outra célula
    da linha 95 é tocada. O que muda é só a forma do que o modelador devolve, e a `Verificação`
    publica os dois guardas que o afirmam.
  - As demais linhas da tabela de papéis (`planejador`, `consultor`, `revisor`, `executor`,
    `orquestração`, `dono`) **não mudam**: são Marco 4 (`D-49`), e a régua da `D-43` as tranca.
  - Não tocar `.claude/agents/pantonic-model-designer.md`: é a `DOM-T9a`, e a ordem é proposital.
  - Na skill, **só** as duas linhas do preâmbulo mudam. A subseção
    `### Modelo de domínio (seção do plano)` é entrega fechada da `DOM-T8` e **não se reabre**
    (`I-3`); as quatro linhas do preâmbulo que falam do `P-0739` e do `backlog.py` são de outro
    plano e **não se tocam**.
  - Nenhuma contingência deste card cria arquivo (`I-10`). Não commitar (`I-6`).
- **Não fazer:**
  - Não tocar a `### 3.2` fora da linha 388: os blocos `P1`, `P2` e `P3` que a `DOM-T7` publicou
    são fidelidade conferida e **não se reabrem** (`I-3`).
  - Não tocar `GOVERNANCA.md` §9, cuja enumeração de agentes já está defasada e está fora de escopo
    (§11).
  - Não alterar a anatomia do card nem o item `4a` da Fase 4 de `pantonic-planner.md`: a `DOM-T5`
    os fechou e eles não citam o token.
- **Contingências:**
  1. Se alguma das quatro faixas não casar com o conteúdo descrito → localizar por conteúdo, com os
     literais de saída da `Verificação`. Literal de saída com contagem maior que a declarada →
     `blocked` razão `premissa`.
- **Testes:** nenhum teste automatizado — a entrega é doutrina publicada. Quem a afere são os
  censos da `Verificação`.
- **Verificação:**

  **Censo do token** (`D-50`), que percorre os dois arquivos inteiros:

  ```
  grep -c 'MD-' GOVERNANCA.md
  ```
  imprime `0` (hoje imprime `1`, medido 2026-09-20).

  ```
  grep -c 'MD-' .claude/agents/pantonic-planner.md
  ```
  imprime `0` (hoje imprime `2`, medido 2026-09-20).

  ```
  grep -c 'carrega estado' .claude/agents/pantonic-planner.md
  ```
  imprime `0` (hoje imprime `2`, medido 2026-09-20): as duas ocorrências falam de **andamento** e
  os blocos R3 e R4 as reescrevem com a palavra certa, agora que o modelo carrega estado inicial
  e final.

  ```
  grep -c 'lista de mudanças' .claude/agents/pantonic-planner.md
  ```
  imprime `0` (hoje imprime `1`, medido 2026-09-20).

  Literais que **entram**, cada um inteiro numa linha só do bloco:

  ```
  grep -cF -e 'a linha do registro de versões que registra o ato' GOVERNANCA.md
  ```
  imprime `1` (hoje imprime `0`) — bloco R1.

  ```
  grep -cF -e 'a linha do ato em `### 1.4 Registro de versões`' GOVERNANCA.md
  ```
  imprime `1` (hoje imprime `0`) — bloco R2.

  ```
  grep -cF -e 'estado inicial e final, registro de versões' .claude/agents/pantonic-planner.md
  ```
  imprime `1` (hoje imprime `0`) — bloco R3.

  ```
  grep -cF -e 'Nenhum elemento da seção carrega andamento' .claude/agents/pantonic-planner.md
  ```
  imprime `1` (hoje imprime `0`) — bloco R4.

  **Guardas — o que não pode mudar** (`D-48`, `AE-11`):

  ```
  grep -cF -e 'resolver conflito entre o texto e a entrega' GOVERNANCA.md
  ```
  imprime `1` (hoje imprime `1`, **inalterado**): o ato `conflito` segue com o modelador até o
  Marco 4.

  ```
  sed -n '/^| papel | o que faz diante do modelo |/,/^$/p' GOVERNANCA.md | grep -c '^|'
  ```
  imprime `9` (hoje imprime `9`, **inalterado**): cabeçalho, separador e **sete** papéis.

  ```
  grep -c '^| \*\*' GOVERNANCA.md
  ```
  imprime `15` (hoje imprime `15`, **inalterado**): a matriz de responsabilidades não ganha nem
  perde linha.

  **O ponteiro da skill** (bloco R5):

  ```
  grep -cF -e '§5 e é' .claude/skills/diario-de-obras/SKILL.md
  ```
  imprime `0` (hoje imprime `1`, na linha 135, medido 2026-09-21).

  ```
  grep -cF -e '§5 e §15 — onde as duas divergem, governa a §15' .claude/skills/diario-de-obras/SKILL.md
  ```
  imprime `1` (hoje imprime `0`, medido 2026-09-21).

  ```
  grep -c 'transcreve' .claude/skills/diario-de-obras/SKILL.md
  ```
  imprime `2` (hoje imprime `2`, **inalterado**): a outra ocorrência é o preâmbulo do `P-0739`, de
  outro plano, que este card não toca.

  ```
  python .claude/tools/backlog.py check
  ```
  imprime `check: OK — nenhuma violação.` e sai `0`.
- **Pronto quando:** os cinco censos imprimem `0`, os cinco literais de entrada imprimem `1`, os
  quatro guardas imprimem os mesmos números de hoje, `backlog.py check` sai `0` e o sinal de
  fidelidade das cinco regiões foi devolvido. **Nenhum item deste `Pronto quando` se apoia em
  frase escrita pelo executor sobre a própria entrega** (`I-11`, `D-50`): a fidelidade do literal é
  conferida pelo revisor, por diff contra a §17.
- **Fora do escopo desta tarefa:** o modelador (`DOM-T9a`), o instrumento (`DOM-T9`), o modelo
  deste plano (`DOM-T10`), e tudo que muda papel (Marco 4, trancado pela régua da `D-43`).

### DOM-T9 — O instrumento aprende propriedades, estado e versão [Sonnet · esforço xhigh · classe implementacao]
- **Status:** `done` · 2026-09-21
- **Depende de:** `DOM-T8`
- **Objetivo:** `.claude/tools/modelo.py` conferindo e mostrando a forma da §15, com as seis
  violações novas, a `V13` de literal novo, os cinco exits, `show --pendente` e `show --drift`, e as
  fixtures e os testes que afirmam cada um.
- **Fundamento:** `D-28`, `D-29`, `D-37`, `D-38`, `D-39`; invariantes `I-1`, `I-2`, `I-3`, `I-10`,
  `I-11`, `I-13`, `I-15`, `I-16`. O card implementa a **§16** deste plano, insumo normativo da
  superfície (`D-51`), e lê a
  gramática que a `DOM-T8` gravou.
- **Operação do modelo:** `OP-10`
  - OP-10: O implementador ensina o instrumento a ler propriedade, estado e versão, e a leitura do dono passa a terminar no estado final que ele mesmo especificou.
  - precisa de: gramática do modelo — residência única na skill `diario-de-obras`, subseção `Modelo de domínio (seção do plano)`; uma linha de tabela por elemento, com a forma à esquerda e a regra mais o código de violação à direita; instrumento do modelo — `.claude/tools/modelo.py`, verbos `check` e `show`, exits `0`, `1` e `2` com literais fixos; lê as tarefas do plano por `backlog._parse_plano` e não reescreve `backlog.py`; cada regra nova nasce com fixture e teste pelo caminho do usuário
- **Camada e fronteira:** ferramenta do kit, em `.claude/tools/`. Pode importar `backlog.py` por
  `importlib` e chamar `backlog._parse_plano`; **não** pode editar `backlog.py` (`I-1`).
- **Contratos/classes:** a dataclass de objeto ganha `propriedades: list[str]`; a de operação ganha
  `altera: list[str]`, cada item na forma `<objeto>.<propriedade>`; a de modelo ganha
  `estado: list[tuple[str, str, str]]` (propriedade, inicial, final), `versoes: list[str]` e
  `situacao: str`. `extrair_modelo(linhas, heading)` passa a receber o heading da seção, para ler
  `## 1` ou `## 1A` com o mesmo código. `montar_drift(vigente, pendente) -> str` devolve a saída
  fixa da §16.
- **Arquivos-alvo:**
  - `.claude/tools/modelo.py`
    - **arquivo inteiro**: o aceite é de coerência do módulo (`I-10`), inclusive docstring e
      `--help`, que descrevem a forma e mudam com ela
  - `tests/test_modelo.py`
    - **arquivo inteiro**: os dez testes vigentes são reescritos para a forma nova e entram os
      novos da lista de `Testes`
  - `tests/fixtures/modelo/fluxo-valido.md`
    - reescrito na forma nova, com propriedades, estado e registro de versões
  - `tests/fixtures/modelo/fluxo-concluido.md`
    - reescrito na forma nova
  - `tests/fixtures/modelo/plano-invalido.md`
    - reescrito para disparar as violações da forma nova
  - `tests/fixtures/modelo/plano-invalido-2.md`
    - reescrito, se a contingência 1 for acionada
  - `tests/fixtures/modelo/plano-sem-cabecalho.md`
    - reescrito na forma nova, sem o cabeçalho
  - `tests/fixtures/modelo/fluxo-pendente.md`
    - **novo**: plano com `## 1` e `## 1A`, para `show --pendente` e `show --drift`
  - `tests/fixtures/modelo/plano-sem-estado.md`
    - **novo**: plano com fluxo e sem `### 1.3`, para o exit `2` de forma anterior
  - `tests/fixtures/modelo/plano-forma-anterior.md`
    - **intocado**
  - `tests/fixtures/modelo/plano-sem-modelo.md`
    - **intocado**
- **Passos:**
  1. Reescrever as dataclasses e as expressões regulares para a gramática da §15.
  2. Implementar `V15`..`V20` e o literal novo da `V13`, cada um com a substring exata da §16, na
     ordem de emissão que a §16 fixa.
  3. Implementar os **cinco** exits da tabela da §16, com os literais exatos.
  4. Implementar `show --pendente` e `show --drift` na forma fixa da §16, com os três marcadores
     `[+]`, `[-]` e `[~]`, de **três** caracteres com os colchetes.
  5. Atualizar o docstring do módulo e a `description` do `argparse` para a forma nova — são texto
     que descreve a forma e caducam com ela (`AE-5`, `AE-8`). **Inclusive as duas referências
     cruzadas à `### 6` do plano** (linhas 2 e 10 em 2026-09-20), que passam a nomear a **§16**, e
     a enumeração `V1`..`V14` do docstring, que passa a `V1`..`V20` (`D-51`, `AE-18`; é o defeito
     que custou a `DOM-T3b` inteira).
  6. Reescrever as fixtures e escrever as duas novas.
  7. Reescrever `tests/test_modelo.py` com os testes da lista abaixo.
  8. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - Não editar `backlog.py`, `review_evidence.py` nem `card_check.py` (`I-1`).
  - Preservar o carregamento de `backlog.py` por `importlib`, a chamada a `backlog._parse_plano`, o
    default de `--root` e o `_forcar_utf8` (`F-4`).
  - Os literais de `V1`..`V14` **não mudam**, exceto o da `V13`, que a §16 republica. A `V2`
    permanece como está (`Q-12` **fechada** pela `D-46`, que a mantém intacta — `D-49`).
  - Piso de regressão é relação (`I-2`): referência datada **249 em 2026-09-20**; o total re-medido
    no despacho, menos os testes removidos, mais os acrescentados, é o piso, e o card declara os
    dois números na linha de retorno.
  - **Toda contingência que cria arquivo já tem o arquivo nos `Arquivos-alvo`** e exige a
    declaração da ativação na linha de retorno (`I-10`, `D-17`).
  - Não commitar (`I-6`).
- **Não fazer:**
  - Não migrar plano nenhum do acervo (`D-3`): o `P-0743` e o `P-0744` passam a sair `2` por falta
    de `### 1.3`, e é isso que o exit novo da §16 declara.
  - Não tocar a `V2` nem a linha `| campo do card |` da gramática.
  - Não escrever estado de andamento em fixture: o andamento segue derivado (`D-2`).
- **Contingências:**
  1. Se as violações novas não couberem numa fixture inválida só, sem que uma esconda a outra →
     distribuir entre `plano-invalido.md` e `plano-invalido-2.md`, **ambas já declaradas nos
     `Arquivos-alvo`**, e devolver `contingência 1 acionada: <o que foi para cada fixture>`
     (`I-8`, `I-10`).
  2. Se um literal de aceite imprimir número diferente do declarado **e** o bloco estiver
     transcrito verbatim → **parar** e devolver `blocked` razão `premissa` com o comando, a
     contagem obtida e a linha do bloco de onde o literal sai (`I-16`, `AE-19`). Não ajustar o
     texto publicado, não relaxar o comando e não atribuir a falha a causa não medida.
- **Testes:** funcionais em `tests/test_modelo.py`, um por comportamento da §16:
  - `test_tf_check_forma_nova_sai_zero` — exit `0` e stdout começando por `modelo: OK — ` com as
    cinco contagens da §16.
  - `test_tf_check_objeto_sem_propriedade_v15` — a substring `V15 objeto — objeto sem propriedade`.
  - `test_tf_check_altera_propriedade_inexistente_v16` — a substring `V16 OP-`.
  - `test_tf_check_propriedade_sem_estado_v17` — a substring `V17 objeto — propriedade sem estado`.
  - `test_tf_check_operacao_sem_altera_v18` — a substring `V18 OP-`.
  - `test_tf_check_registro_sem_vigente_unico_v19` — a substring `V19 secao`.
  - `test_tf_check_pendente_fora_de_sequencia_v20` — a substring `V20 secao`.
  - `test_tf_check_v13_literal_novo` — a substring exata
    `V13 secao — cabeçalho, objetos, estado ou registro de versões ausente`.
  - `test_tf_check_sem_estado_sai_dois` — sobre `plano-sem-estado.md`, exit `2` e a substring
    `modelo: forma anterior — plano sem estado inicial e final`. **Poder discriminante:** a regra
    concorrente (tratar como violação `V13`) daria exit `1`.
  - `test_tf_show_vigente_por_omissao` — sobre `fluxo-pendente.md`, a saída **não** contém a versão
    pendente. **Poder discriminante:** a regra concorrente (mostrar a mais recente) mostraria a
    pendente.
  - `test_tf_show_pendente` — com `--pendente`, a saída traz a versão pendente.
  - `test_tf_show_drift_tres_marcadores` — com `--drift`, a saída tem `[+]`, `[-]` e `[~]`.
  - `test_tf_show_drift_sem_pendente_sai_dois` — exit `2` e a substring `modelo: sem versão pendente`.
  - `test_tf_show_drift_sem_diferenca` — exit `0` e a substring `sem drift`.
- **Verificação:**

  ```
  python -m pytest tests/test_modelo.py -q
  ```
  passa, com **ao menos 14** testes coletados neste arquivo (hoje são 10, medido 2026-09-20).

  ```
  python .claude/tools/modelo.py check --plano tests/fixtures/modelo/fluxo-valido.md
  ```
  sai `0` e imprime uma linha começando por `modelo: OK — `.

  ```
  python .claude/tools/modelo.py check --plano docs/plans/P-0744-spec-do-planejador.md
  ```
  sai `2` e imprime `modelo: forma anterior — plano sem estado inicial e final` (hoje sai `0`,
  medido 2026-09-20 — a mudança é esperada e é o que a `D-3` prescreve).

  ```
  python .claude/tools/modelo.py show --plano tests/fixtures/modelo/fluxo-pendente.md --drift
  ```
  sai `0` e a saída começa por `# Drift do modelo — `.

  ```
  grep -cF -e 'V13 secao — cabeçalho, objetos, estado ou registro de versões ausente' .claude/tools/modelo.py
  ```
  imprime `1` (hoje imprime `0`, medido 2026-09-20).

  ```
  grep -c 'V15' .claude/tools/modelo.py
  ```
  imprime `1` ou mais (hoje imprime `0`, medido 2026-09-20).

  ```
  python .claude/tools/modelo.py --help
  ```
  sai `0`; a saída cita `--drift` e não cita `V1..V14`.

  ```
  python -m pytest tests -q
  ```
  passa, com total não menor que o re-medido no despacho menos os removidos mais os acrescentados.
  Referência datada: **249 em 2026-09-20**.

  **Censo do módulo** (`D-50`), que é o que dá poder discriminante à cláusula do `Pronto quando`:

  ```
  grep -c 'Mudanças do modelo' .claude/tools/modelo.py
  ```
  imprime `0` (hoje imprime `3`, nas linhas 8, 208 e 209, medido 2026-09-20).

  ```
  grep -c 'MD-' .claude/tools/modelo.py
  ```
  imprime `0` (hoje imprime `1`, na linha 95, medido 2026-09-20): a expressão regular que lê a
  tabela de mudanças sai junto com a tabela.

  ```
  grep -c '### 6' .claude/tools/modelo.py
  ```
  imprime `0` (hoje imprime `2`, nas linhas 2 e 10, medido 2026-09-21) — o padrão não casa dentro
  de `### 16`, que começa por `### 1`.

  ```
  grep -c '### 16' .claude/tools/modelo.py
  ```
  imprime `1` ou mais (hoje imprime `0`, medido 2026-09-21) — a referência cruzada apontando para a
  seção que o módulo de fato implementa.
- **Pronto quando:** os testes passam com ao menos 14 no arquivo do modelo, os cinco exits e os
  literais da §16 saem exatos, `show --drift` imprime a forma fixa, o `--help` e o docstring
  descrevem a forma nova **e apontam para a §16**, e **os três censos do módulo imprimem `0`** — são eles, e não juízo do
  executor sobre a própria entrega, que afirmam que nenhuma linha do módulo descreve a forma
  anterior (`D-50`, `I-11`). Os literais normativos de saída que **nomeiam** a forma anterior não
  contêm nenhum dos dois padrões censados, e por isso sobrevivem ao censo (`I-10`).
- **Fora do escopo desta tarefa:** o modelo deste plano (`DOM-T10`), a `V2` e a `Q-12`, e tudo que
  muda papel (Marco 4).

### DOM-T9a — O modelador fala a forma nova [Sonnet · esforço medium · classe implementacao]
- **Status:** `done` · 2026-09-21
- **Depende de:** `DOM-T9`
- **Objetivo:** `.claude/agents/pantonic-model-designer.md` devolvendo o que a forma nova define —
  versão em `### 1.4 Registro de versões`, bloco irmão `## 1A` na emenda, propriedades como ponto
  de partida do ensinamento — com os **quatro atos** e todas as responsabilidades intactos.
- **Fundamento:** `D-28`, `D-29`, `D-34`, `D-35`, `D-48`, `D-49`, `D-50`; invariantes `I-3`, `I-4`,
  `I-5`, `I-11`, `I-13`, `I-15`, `I-16`. O card transcreve a **§18** deste plano. É o segundo corretivo do `AE-17`
  (`ESC-6`): cinco pontos do agente exigem a linha `MD-<n>`, e um sexto manda começar pelos
  objetos, contra o parágrafo `**Objeto, operação e propriedade.**` que a `DOM-T7` publicou.
- **Operação do modelo:** `OP-11`
  - OP-11: O autor de papéis põe o modelador a falar a forma nova e fixa a fronteira do que ele devolve: o que é da seção ele corrige antes de devolver, e o que mora no card volta medido, para quem conduz a sessão rotear.
  - precisa de: modelador — `.claude/agents/pantonic-model-designer.md`; front matter com nome, descrição e lista de ferramentas, e corpo com os atos, o ensinamento e o gate; as duas portas de inventário do kit contam os agentes e hoje fecham sobre dez; gramática do modelo — residência única na skill `diario-de-obras`, subseção `Modelo de domínio (seção do plano)`; uma linha de tabela por elemento, com a forma à esquerda e a regra mais o código de violação à direita; instrumento do modelo — `.claude/tools/modelo.py`, verbos `check` e `show`, exits `0`, `1` e `2` com literais fixos; lê as tarefas do plano por `backlog._parse_plano` e não reescreve `backlog.py`; cada regra nova nasce com fixture e teste pelo caminho do usuário
- **Camada e fronteira:** agente do kit, em `.claude/agents/`. Nenhum código, nenhum teste.
- **Contratos/classes:** nenhum.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-model-designer.md`
    - **seis** pontos, medidos em 2026-09-20 e re-derivados no despacho (`I-5`): o bullet da norma
      em `## Fatos estáveis`, 15-17 (bloco **S1**); o item 1 de `## O ensinamento`, 28-30 (bloco
      **S2**); o bullet **Autoria**, 42-44 (bloco **S3**); o bullet **Emenda**, 45-48 (bloco
      **S4**); os bullets **Conflito** e **Leitura**, 49-55 (bloco **S5**); e a seção
      `## A forma da devolução` inteira, 69-77 (bloco **S6**)
- **Passos:**
  1. Substituir as linhas 15-17 pelo **bloco S1** da §18, verbatim (`I-3`).
  2. Substituir as linhas 28-30 pelo **bloco S2**.
  3. Substituir as linhas 42-44 pelo **bloco S3**.
  4. Substituir as linhas 45-48 pelo **bloco S4**.
  5. Substituir as linhas 49-55 pelo **bloco S5**.
  6. Substituir as linhas 69-77 pelo **bloco S6**.
  7. Imprimir as seis regiões e devolver o **sinal** `fidelidade conferida: S1, S2, S3, S4, S5, S6`.
  8. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - **Um bloco literal por ponto** (`I-13`): seis pontos, seis blocos.
  - **Nenhum ato nasce, morre ou muda de dono** (`D-48`). O heading `## Os quatro atos` e os quatro
    bullets permanecem, inclusive **Conflito** — a `D-47` o extingue no **Marco 4**, e publicar
    isso agora é o defeito `AE-11`, que este plano já pagou duas vezes. A `Verificação` publica os
    guardas que o afirmam.
  - O front matter (linhas 1-6) **não muda**: a `description` descreve papel, não forma, e a
    `DOM-T4` a fechou com aceite próprio.
  - A seção `## O que você nunca faz` e a seção `## A gramática do dossiê Ato de modelo` **não
    mudam**: a primeira é papel; a segunda é cópia da norma, cujos seis campos a §14 não tocou.
  - Não tocar `GOVERNANCA.md`, `pantonic-planner.md`, `.claude/tools/*` nem a skill
    `diario-de-obras`: cada um tem o seu card, e todos vêm antes deste.
  - Nenhuma contingência deste card cria arquivo (`I-10`). Não commitar (`I-6`).
- **Não fazer:**
  - Não acrescentar item novo ao `## O ensinamento`: são **quatro** itens antes e depois, e o
    estado inicial, o estado final e o versionamento moram na norma, que o próprio corpo manda ler
    e **não recopia** (`D-9`).
  - Não reescrever o bullet do instrumento nem o do gate `modelo.py check` exit `0`: a `DOM-T9`
    acabou de os tornar verdadeiros.
- **Contingências:**
  1. Se alguma das seis faixas não casar com o conteúdo descrito → localizar por conteúdo, com os
     literais de saída da `Verificação`. Literal de saída com contagem maior que a declarada →
     `blocked` razão `premissa`.
  2. Se um literal de aceite imprimir número diferente do declarado **e** o bloco estiver
     transcrito verbatim → **parar** e devolver `blocked` razão `premissa` com o comando, a
     contagem obtida e a linha do bloco de onde o literal sai (`I-16`, `AE-19`). Não ajustar o
     texto publicado, não relaxar o comando e não atribuir a falha a causa não medida.
- **Testes:** nenhum teste automatizado — a entrega é a definição de um agente. Quem a afere são os
  censos da `Verificação`.
- **Verificação:**

  **Censo do arquivo inteiro** (`D-50`):

  ```
  grep -c 'MD-' .claude/agents/pantonic-model-designer.md
  ```
  imprime `0` (hoje imprime `5`, medido 2026-09-20).

  ```
  grep -c 'Mudanças do modelo' .claude/agents/pantonic-model-designer.md
  ```
  imprime `0` (hoje imprime `2`, medido 2026-09-20).

  ```
  grep -c 'três blocos' .claude/agents/pantonic-model-designer.md
  ```
  imprime `0` (hoje imprime `1`, medido 2026-09-20).

  Literais que **entram**, cada um inteiro numa linha só do bloco:

  ```
  grep -cF -e 'os quatro blocos que a compõem' .claude/agents/pantonic-model-designer.md
  ```
  imprime `1` (hoje imprime `0`) — bloco S1.

  ```
  grep -cF -e 'Comece pelas **propriedades**' .claude/agents/pantonic-model-designer.md
  ```
  imprime `1` (hoje imprime `0`) — bloco S2.

  ```
  grep -cF -e 'linha da **versão 1** em `### 1.4 Registro de versões`' .claude/agents/pantonic-model-designer.md
  ```
  imprime `1` (hoje imprime `0`) — bloco S3.

  ```
  grep -cF -e '**Versiona, não reescreve.**' .claude/agents/pantonic-model-designer.md
  ```
  imprime `1` (hoje imprime `0`) — bloco S4.

  ```
  grep -cF -e 'nenhuma linha de versão é gerada' .claude/agents/pantonic-model-designer.md
  ```
  imprime `1` (hoje imprime `0`) — bloco S5.

  ```
  grep -cF -e '## 1A. Modelo conceitual' .claude/agents/pantonic-model-designer.md
  ```
  imprime `2` (hoje imprime `0`) — uma no bloco S4, uma no bloco S6.

  **Guardas — o que não pode mudar** (`D-48`, `AE-11`):

  ```
  grep -cF -e '## Os quatro atos' .claude/agents/pantonic-model-designer.md
  ```
  imprime `1` (hoje imprime `1`, **inalterado**).

  ```
  grep -cF -e '- **Conflito** —' .claude/agents/pantonic-model-designer.md
  ```
  imprime `1` (hoje imprime `1`, **inalterado**): o ato segue existindo e segue sendo dele.

  ```
  grep -c '^## ' .claude/agents/pantonic-model-designer.md
  ```
  imprime `6` (hoje imprime `6`, **inalterado**): nenhuma seção nasce e nenhuma morre.

  ```
  sed -n '1,6p' .claude/agents/pantonic-model-designer.md
  ```
  imprime o front matter com `name: pantonic-model-designer`, `model: opus` e a linha `tools:`
  **inalterados**.

  ```
  python .claude/tools/backlog.py check
  ```
  imprime `check: OK — nenhuma violação.` e sai `0`.
- **Pronto quando:** os três censos imprimem `0`, os seis literais de entrada imprimem os números
  declarados, os quatro guardas imprimem os mesmos números de hoje, `backlog.py check` sai `0` e o
  sinal de fidelidade das seis regiões foi devolvido. **Nenhum item deste `Pronto quando` se apoia
  em frase escrita pelo executor sobre a própria entrega** (`I-11`, `D-50`): a fidelidade do
  literal é conferida pelo revisor, por diff contra a §18.
- **Fora do escopo desta tarefa:** o modelo deste plano (`DOM-T10`), a `V2`, e tudo que muda papel
  — inclusive a extinção do ato `conflito` que a `D-47` já decidiu (Marco 4, trancado pela régua da
  `D-43`).

### DOM-T9b — O gate que o modelador consegue fechar [Sonnet · esforço low · classe implementacao]
- **Status:** `done` · 2026-09-21
- **Depende de:** `DOM-T9a`
- **Objetivo:** o bullet do gate em `.claude/agents/pantonic-model-designer.md` distinguindo a
  violação que é do modelador da que mora no card, para que o ato dele possa terminar num plano em
  conversão.
- **Fundamento:** `D-5`, `D-52`, `D-53`; invariantes `I-3`, `I-11`, `I-13`, `I-15`, `I-16`. O card
  transcreve a **§19** deste plano. Nasceu do `ESC-9`: com o gate vigente, a `DOM-T10` trava no
  primeiro despacho do modelador — gravada a seção, o `check` acusa `V2` em toda tarefa que ainda
  cita `Oração do modelo`, e essas linhas moram nos cards, que ele é **proibido** de tocar (`M-9`).
  Gate que só se fecha corrigindo o que não é seu é aceite inalcançável por construção, a mesma
  família do `AE-19`.
- **Operação do modelo:** `OP-11`
  - OP-11: O autor de papéis põe o modelador a falar a forma nova e fixa a fronteira do que ele devolve: o que é da seção ele corrige antes de devolver, e o que mora no card volta medido, para quem conduz a sessão rotear.
  - precisa de: modelador — `.claude/agents/pantonic-model-designer.md`; front matter com nome, descrição e lista de ferramentas, e corpo com os atos, o ensinamento e o gate; as duas portas de inventário do kit contam os agentes e hoje fecham sobre dez; gramática do modelo — residência única na skill `diario-de-obras`, subseção `Modelo de domínio (seção do plano)`; uma linha de tabela por elemento, com a forma à esquerda e a regra mais o código de violação à direita; instrumento do modelo — `.claude/tools/modelo.py`, verbos `check` e `show`, exits `0`, `1` e `2` com literais fixos; lê as tarefas do plano por `backlog._parse_plano` e não reescreve `backlog.py`; cada regra nova nasce com fixture e teste pelo caminho do usuário
- **Camada e fronteira:** agente do kit, em `.claude/agents/`. Nenhum código, nenhum teste.
- **Contratos/classes:** nenhum.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-model-designer.md`
    - **um** ponto, medido em 2026-09-21 e re-derivado no despacho (`I-5`): o bullet do gate em
      `## Fatos estáveis`, linhas 22-24 (bloco **T1**)
- **Passos:**
  1. Substituir as linhas 22-24 pelo **bloco T1** da §19, verbatim (`I-3`).
  2. Imprimir a região e devolver o **sinal** `fidelidade conferida: T1`.
  3. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - **Um bloco literal por ponto** (`I-13`): um ponto, um bloco.
  - Os outros três bullets de `## Fatos estáveis` **não mudam**, e nenhuma outra seção do arquivo é
    tocada: a `DOM-T9a` fechou seis pontos dele e eles **não se reabrem** (`I-3`).
  - Nenhum ato do modelador nasce, morre ou muda de dono: o gate muda de **leitura**, não de dono.
  - Nenhuma contingência deste card cria arquivo (`I-10`). Não commitar (`I-6`).
- **Não fazer:**
  - Não tocar `.claude/tools/modelo.py`: nenhuma violação muda de código, de literal ou de classe —
    a fronteira que o bloco usa (`violacoes_id` × `violacoes_op`) **já existe** no instrumento.
  - Não tocar `GOVERNANCA.md` §3.2: a norma não fala do gate, fala de quem escreve.
- **Contingências:**
  1. Se a faixa 22-24 não casar com o conteúdo descrito → localizar por conteúdo, com o literal de
     saída da `Verificação`. Literal de saída com contagem maior que a declarada → `blocked` razão
     `premissa`.
  2. Se um literal de aceite imprimir número diferente do declarado **e** o bloco estiver
     transcrito verbatim → **parar** e devolver `blocked` razão `premissa` com o comando, a
     contagem obtida e a linha do bloco de onde o literal sai (`I-16`, `AE-19`). Não ajustar o
     texto publicado, não relaxar o comando e não atribuir a falha a causa não medida.
- **Testes:** nenhum teste automatizado — a entrega é a definição de um agente.
- **Verificação:**

  Literal que **sai**, inteiro numa linha só:

  ```
  grep -cF -e 'o ato com exit `0`. Exit diferente de `0` é ato não concluído' .claude/agents/pantonic-model-designer.md
  ```
  imprime `0` (hoje imprime `1`, na linha 23, medido 2026-09-21).

  Literais que **entram**, cada um inteiro numa linha só do bloco (`I-15`):

  ```
  grep -cF -e 'Violação indexada pelo **`<ID>` de uma tarefa** (`V2`, `V4`, `V14`) **não é sua**' .claude/agents/pantonic-model-designer.md
  ```
  imprime `1` (hoje imprime `0`, medido 2026-09-21).

  ```
  grep -cF -e 'do `check`, nomeando as violações que ficaram' .claude/agents/pantonic-model-designer.md
  ```
  imprime `1` (hoje imprime `0`, medido 2026-09-21).

  **Guardas — o que não pode mudar:**

  ```
  grep -c '^## ' .claude/agents/pantonic-model-designer.md
  ```
  imprime `6` (hoje imprime `6`, **inalterado**).

  ```
  grep -cF -e '## Os quatro atos' .claude/agents/pantonic-model-designer.md
  ```
  imprime `1` (hoje imprime `1`, **inalterado**).

  ```
  grep -c '^- ' .claude/agents/pantonic-model-designer.md
  ```
  imprime `19` (hoje imprime `19`, **inalterado**, medido 2026-09-21): o bloco T1 é **um** bullet,
  como o que ele substitui — o total de bullets de primeiro nível do arquivo não muda.

  ```
  python .claude/tools/backlog.py check
  ```
  imprime `check: OK — nenhuma violação.` e sai `0`.
- **Pronto quando:** o literal de saída imprime `0`, os dois de entrada imprimem `1`, os três
  guardas imprimem os mesmos números de hoje, `backlog.py check` sai `0` e o sinal de fidelidade
  foi devolvido. A fidelidade do literal é conferida pelo revisor, por diff contra a §19 (`I-11`).
- **Fora do escopo desta tarefa:** o modelo deste plano (`DOM-T10`), o instrumento, e tudo que muda
  papel (Marco 4).

### DOM-T9c — A quarta família de violações, que é do modelador [Sonnet · esforço low · classe implementacao]
- **Status:** `done` · 2026-09-21
- **Depende de:** `DOM-T9b`
- **Objetivo:** o bullet do gate em `.claude/agents/pantonic-model-designer.md` definindo por
  **complemento** o que é violação da seção, de modo que `V6`, `V7`, `V15` e `V17` — as de
  `### 1.1 Objetos` e `### 1.3 Estado`, que são do modelador — caiam no ramo do *ato não
  concluído*.
- **Fundamento:** `D-5`, `D-52`, `D-53`, `D-54`; invariantes `I-3`, `I-11`, `I-13`, `I-15`,
  `I-16`, `I-17`.
  O card transcreve a **§20** deste plano. Nasceu do `AE-22`: o bloco `T1`, que a `DOM-T9b`
  publicou, nomeia **dois** tokens de índice, e o instrumento emite **quatro**. As quatro violações
  órfãs são as mais prováveis de uma **autoria** — e a `DOM-T10`, a próxima tarefa, é a primeira
  autoria do modelador neste plano. Sem esta emenda, o deadlock que o `ESC-9` fechou pelo ramo
  `<ID>` reabre por um ramo que o texto não nomeia.
  **Nota de atribuição para quem revisa (rodada `RP-1`, 2026-09-21).** A entrega material desta
  tarefa **já está na árvore**: o bullet do gate em `.claude/agents/pantonic-model-designer.md` é
  o bloco `T2` da §20, transcrito verbatim, e os doze valores dos seis pares de literais desta
  `Verificação` foram medidos contra ela em 2026-09-21. O que voltou `blocked` razão `premissa`
  foi a **`Verificação` deste card**, não a entrega: o literal de entrada antigo atravessava a
  quebra 4164/4165 do bloco e era insatisfazível junto com a `I-3` (`AE-23`). A rodada `RP-1`
  reescreveu a `Verificação` (`D-54`) e a tarefa voltou a `review` **sem despacho novo de
  executor** — julgue-a contra este dossiê corrigido. A parada do executor, com comando, contagem
  obtida e linha de origem do literal, é a conduta que a `I-16` exige, e é o primeiro caso real em
  que ela funcionou.
- **Operação do modelo:** `OP-11`
  - OP-11: O autor de papéis põe o modelador a falar a forma nova e fixa a fronteira do que ele devolve: o que é da seção ele corrige antes de devolver, e o que mora no card volta medido, para quem conduz a sessão rotear.
  - precisa de: modelador — `.claude/agents/pantonic-model-designer.md`; front matter com nome, descrição e lista de ferramentas, e corpo com os atos, o ensinamento e o gate; as duas portas de inventário do kit contam os agentes e hoje fecham sobre dez; gramática do modelo — residência única na skill `diario-de-obras`, subseção `Modelo de domínio (seção do plano)`; uma linha de tabela por elemento, com a forma à esquerda e a regra mais o código de violação à direita; instrumento do modelo — `.claude/tools/modelo.py`, verbos `check` e `show`, exits `0`, `1` e `2` com literais fixos; lê as tarefas do plano por `backlog._parse_plano` e não reescreve `backlog.py`; cada regra nova nasce com fixture e teste pelo caminho do usuário
- **Camada e fronteira:** agente do kit, em `.claude/agents/`. Nenhum código, nenhum teste.
- **Contratos/classes:** nenhum.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-model-designer.md`
    - **um** ponto, medido em 2026-09-21 e re-derivado no despacho (`I-5`): o bullet do gate em
      `## Fatos estáveis`, hoje com **oito** linhas, que a `DOM-T9b` publicou (bloco **T2**)
- **Passos:**
  1. Substituir o bullet inteiro do gate pelo **bloco T2** da §20, verbatim (`I-3`).
  2. Imprimir a região e devolver o **sinal** `fidelidade conferida: T2`.
  3. Rodar as verificações abaixo — **inclusive a de comportamento** (`I-17`): o bloco afirma o que
     o instrumento emite, e `grep` prova que o texto chegou, nunca que ele é verdadeiro.
- **Restrições desta tarefa:**
  - **Um bloco literal por ponto** (`I-13`): um ponto, um bloco.
  - Os outros três bullets de `## Fatos estáveis` **não mudam**, e nenhuma outra seção do arquivo é
    tocada (`I-3`).
  - **Não tocar `.claude/tools/modelo.py`**: nenhuma violação muda de código, de literal, de classe
    ou de token de índice. O defeito é do **texto**, não do instrumento — e o texto é que se
    conforma ao que o instrumento já faz.
  - Nenhum ato do modelador nasce, morre ou muda de dono.
  - Nenhuma contingência deste card cria arquivo (`I-10`). Não commitar (`I-6`).
- **Não fazer:**
  - Não reescrever o bloco `T1` na §19 deste plano: ele é o registro do que a `DOM-T9b` transcreveu
    e o aceite dela se confere contra ele (`D-51`).
  - Não tocar `GOVERNANCA.md` §3.2: a norma fala de quem escreve, não do gate.
- **Contingências:**
  1. Se o bullet do gate não casar com o conteúdo descrito → localizar por conteúdo, com os
     literais de saída da `Verificação`. Literal de saída com contagem maior que a declarada →
     `blocked` razão `premissa`.
  2. Se a verificação de comportamento devolver famílias diferentes das quatro declaradas → **parar
     e sinalizar `blocked` razão `premissa`**, com a saída literal. O bloco afirma o que o
     instrumento emite: divergência aqui significa que o **texto** da §20 está errado, e corrigi-lo
     é ato de plano, nunca de execução (`I-16`, `I-17`).
  3. Se um literal de aceite imprimir número diferente do declarado **e** o bloco estiver
     transcrito verbatim → **parar** e devolver `blocked` razão `premissa` com o comando, a
     contagem obtida e a linha do bloco de onde o literal sai (`I-16`, `AE-19`).
- **Testes:** nenhum teste automatizado — a entrega é a definição de um agente. O guarda executável
  é a verificação de comportamento abaixo.
- **Verificação:**

  Literais que **saem** (são do bloco `T1` da §19, que o `T2` supersede), cada um inteiro numa
  linha só:

  ```
  grep -cF -e 'por `secao` — é ato não concluído: corrija a seção que você mesmo escreveu e rode de novo antes de' .claude/agents/pantonic-model-designer.md
  ```
  imprime `0`. Na árvore, depois da entrega: `0`; contra o bloco `T1`, que é o texto que o bullet
  tinha antes dela: `1`.

  ```
  grep -cF -e 'mora no card, e card não é linha que você escreve. Nesse caso devolva o ato com a **saída literal**' .claude/agents/pantonic-model-designer.md
  ```
  imprime `0`. Na árvore, depois da entrega: `0`; contra o bloco `T1`: `1`.

  Literais que **entram**. Cada um está contido **integralmente em uma linha** do bloco `T2` da
  §20, e a linha de origem vai nomeada (`I-15`, `D-54`). A proposição *"é da seção toda violação
  que o instrumento não indexa pelo `<ID>` de uma tarefa: as de `secao`, as de `OP-<n>` e as de
  `objeto`"* **atravessa a quebra** entre as linhas 4164 e 4165 do bloco, e `grep -cF` só casa
  dentro de uma linha: por isso ela é conferida por **dois greps, um por linha**. Os seis pares
  abaixo foram medidos em 2026-09-21 — o primeiro valor contra a árvore, **depois** da entrega; o
  segundo contra o bloco `T1` da §19, que é o texto anterior. É o par que discrimina os dois
  mundos. Os números de linha são os da árvore em 2026-09-21 e se re-derivam no despacho (`I-5`):
  a âncora de cada literal é o **conteúdo** da linha do bloco `T2`, não o número.

  ```
  grep -cF -e 'devolve. Exit `1` é ato não concluído **sempre que ao menos uma violação for da seção** — e é da' .claude/agents/pantonic-model-designer.md
  ```
  imprime `1` — linha 4163 da §20, **borda de cima** da substituição: é a primeira linha em que o `T2`
  diverge do `T1`. Na árvore, depois da entrega: `1`;
  contra o bloco `T1`: `0`.

  ```
  grep -cF -e 'violação que o instrumento não indexa pelo `<ID>` de uma tarefa: as de `secao`' .claude/agents/pantonic-model-designer.md
  ```
  imprime `1` — linha 4164 da §20, primeira metade da proposição partida — a que **termina** a linha. Na árvore, depois da entrega: `1`;
  contra o bloco `T1`: `0`.

  ```
  grep -cF -e 'de `OP-<n>` e as de `objeto`, estas últimas vindas de `### 1.1 Objetos` e de' .claude/agents/pantonic-model-designer.md
  ```
  imprime `1` — linha 4165 da §20, segunda metade da mesma proposição — a que **abre** a linha
  seguinte. É este par, e não um grep sobre a frase inteira, que confere a proposição (`I-15`,
  `D-54`, `AE-23`). Na árvore, depois da entrega: `1`;
  contra o bloco `T1`: `0`.

  ```
  grep -cF -e '`### 1.3 Estado inicial e estado final` (`V6`, `V7`, `V15`, `V17`). Corrija a seção que você mesmo' .claude/agents/pantonic-model-designer.md
  ```
  imprime `1` — linha 4166 da §20, a enumeração das quatro violações da família `objeto`. Na árvore, depois da entrega: `1`;
  contra o bloco `T1`: `0`.

  ```
  grep -cF -e 'pelo `<ID>` de uma tarefa: `V2`, `V4` e `V14` — elas moram no card, e card não é linha que você' .claude/agents/pantonic-model-designer.md
  ```
  imprime `1` — linha 4168 da §20, as três violações que **não** são do modelador. Na árvore, depois da entrega: `1`;
  contra o bloco `T1`: `0`.

  ```
  grep -cF -e '`2` é plano ainda na forma anterior: se o seu ato é justamente trazê-lo para a forma nova, ele' .claude/agents/pantonic-model-designer.md
  ```
  imprime `1` — linha 4171 da §20, **borda de baixo**: a linha 4172, última do bloco, é idêntica no
  `T1` e no `T2` e por isso **não** discrimina — esta é a última que discrimina. Na árvore, depois da entrega: `1`;
  contra o bloco `T1`: `0`.


  **Comportamento — o texto confrontado com o instrumento** (`I-17`), pelo caminho do usuário:

  ```
  python .claude/tools/modelo.py check --plano tests/fixtures/modelo/plano-invalido.md
  ```
  sai `1` com `modelo: FALHOU — 10 violação(ões)` e, no stderr, as **quatro** famílias que o bloco
  nomeia: `V13 secao`, quatro linhas `OP-<n>` (`V5`, `V1`, `V3`, `V12`), **duas linhas `objeto`**
  (`V6`, `V7`) e três linhas de `<ID>` (`V2`, `V4`, `V14`). Medido 2026-09-21.

  ```
  python .claude/tools/modelo.py check --plano tests/fixtures/modelo/plano-invalido.md 2>&1 | grep -c ' objeto — '
  ```
  imprime `2` (hoje imprime `2`, medido 2026-09-21). **É este comando que prova que a família
  `objeto` existe** — o que a §19 negava e nenhum `grep` de texto teria pego.

  **Guardas — o que não pode mudar:**

  ```
  grep -c '^- ' .claude/agents/pantonic-model-designer.md
  ```
  imprime `19`. Na árvore, depois da entrega: `19`; antes dela: `19` — **inalterado** é o aceite,
  porque o bullet do gate conta como **um** item de lista nos dois mundos (medido 2026-09-21).

  ```
  grep -c '^## ' .claude/agents/pantonic-model-designer.md
  ```
  imprime `6`. Na árvore, depois da entrega: `6`; antes dela: `6` — **inalterado** (medido
  2026-09-21).

  ```
  python .claude/tools/backlog.py check
  ```
  imprime `check: OK — nenhuma violação.` e sai `0`.
- **Pronto quando:** os **dois** literais de saída imprimem `0`, os **seis** de entrada imprimem
  `1` — inclusive as duas bordas (4163 e 4171) e os **dois** greps que cobrem, um por linha, a
  proposição que atravessa a quebra 4164/4165 (`I-15`, `D-54`) —, **a verificação de comportamento
  devolve as quatro famílias e o contador de `objeto` imprime `2`**, os dois guardas ficam
  inalterados e `backlog.py check` sai `0`. A fidelidade do literal é conferida pelo revisor, por
  diff da árvore contra o bloco `T2` da §20 (`I-11`): é o diff, e não frase de quem executou, que
  prova a transcrição. O sinal `fidelidade conferida: T2` vale pelo que a linha de retorno do
  despacho de 2026-09-21 trouxer — esta tarefa **não recebe despacho novo de executor** (rodada
  `RP-1`).
- **Fora do escopo desta tarefa:** o instrumento (nenhuma linha de `modelo.py` muda), o modelo
  deste plano (`DOM-T10`), a fixture que falta para `V15`..`V20` (`AE-20`, matéria de
  replanejamento) e tudo que muda papel (Marco 4).
- **Notas de execução:**
  - 2026-09-21 `ready` — rodada RP-1 (2026-09-21): bloqueio DE ACEITE absorvido pela D-54; Verificacao reescrita.
  - 2026-09-21 `review` — rodada RP-1 (2026-09-21): bloqueio DE ACEITE absorvido pela decisao D-54. A Verificacao do card foi reescrita (seis literais de entrada, cada um contido em uma linha do bloco T2 da §20, cada um com o par de valores medido na arvore e contra o bloco T1). A entrega ja estava na arvore, transcrita verbatim: a tarefa entra em review sem despacho novo de executor. Nao ha RDO, porque blocked nao produz RDO: a evidencia e a arvore mais este card.

### DOM-T10 — O modelo deste plano, na forma nova [Sonnet · esforço medium · classe implementacao]
- **Status:** `done` · 2026-09-21
- **Depende de:** `DOM-T9c`
- **Objetivo:** a seção `## 1. Modelo conceitual` do `P-0743` reescrita na forma nova — objetos com
  propriedades, fluxo com `altera:`, estado inicial e estado final, registro de versões — de modo
  que o dono leia, em `modelo.py show`, o estado final que ele mesmo especificou. **É a entrega que
  o Marco 3 mede.**
- **Fundamento:** `D-31`, `D-33`, `D-34`, `D-35`, `D-37`, `D-43`, `D-52`, `D-53`; invariantes
  `I-3`, `I-11`, `I-15`, `I-16`.
  O dono nomeou este plano como o **teste do desenho**: *"nosso modelo seria o agente model designer
  e o modelo. Por meio da operação 'construir o modelo', receberiamos o 'modelo' no padrão
  esperado"*. O conteúdo do modelo é **ato do modelador** (`D-5`), e **também a gravação dele**
  (`D-52`): este card não redige a seção **e não a transcreve** — ele pede o ato, espera, e
  converte os campos dos cards depois que a seção já está no arquivo. **São dois despachos deste
  mesmo card, com o ato do modelador entre eles.**
- **Operação do modelo:** `OP-12`
  - OP-12: O modelador constrói o modelo deste plano na forma nova, e o executor converte o campo de cada card para a operação que ele materializa, com o texto e o contrato copiados.
  - precisa de: modelador — `.claude/agents/pantonic-model-designer.md`; front matter com nome, descrição e lista de ferramentas, e corpo com os atos, o ensinamento e o gate; as duas portas de inventário do kit contam os agentes e hoje fecham sobre dez; cadeia de papéis diante do modelo — `.claude/agents/pantonic-reviewer.md`, `pantonic-planner.md` e `pantonic-consultant.md`, mais a skill `scrum-master`; cada elo declara o que devolve e quem o lê, e nenhum elo manda fazer o que outro elo proíbe; gramática do modelo — residência única na skill `diario-de-obras`, subseção `Modelo de domínio (seção do plano)`; uma linha de tabela por elemento, com a forma à esquerda e a regra mais o código de violação à direita; instrumento do modelo — `.claude/tools/modelo.py`, verbos `check` e `show`, exits `0`, `1` e `2` com literais fixos; lê as tarefas do plano por `backlog._parse_plano` e não reescreve `backlog.py`; cada regra nova nasce com fixture e teste pelo caminho do usuário
- **Camada e fronteira:** o plano, em `docs/plans/`. Nenhum código, nenhum teste.
- **Contratos/classes:** nenhum.
- **Arquivos-alvo:**
  - `docs/plans/P-0743-modelo-de-dominio.md`
    - **um** ponto, e só um: o campo `- **Oração do modelo:**` de **todos** os cards da §9, que
      vira `- **Operação do modelo:**`. **Medido no `ESC-10`, 2026-09-21: são 18 cards** — 14 na
      autoria, 16 depois do `ESC-6`, 17 com a `DOM-T9b` e 18 com a `DOM-T9c` —, e a `V2` exige o
      campo em cada um: sem esta conversão o `check` sai `1` dezoito vezes, e não `0`
    - **A seção `## 1. Modelo conceitual` NÃO é alvo deste card** (`D-52`). Quem a grava é o
      `pantonic-model-designer`, no despacho próprio dele, porque o gate do ato dele exige que ela
      já esteja no arquivo. Edição do executor nessa região é edição **fora de alvo**, e o laudo a
      trata como tal
- **Passos:**
  **Ato 1 — pedir, e parar.**
  1. **Não redigir e não transcrever o modelo.** Devolver, na linha de retorno, o dossiê
     `Ato de modelo` de `autoria`, com os seis campos da norma, pedindo o modelo do `P-0743` na
     forma nova, e **sinalizar `blocked` razão `dependencia`**: o card volta à fila depois do ato
     do modelador. Quem conduz a sessão o despacha (`D-5`, `D-6`); nenhum agente aciona outro.
     Insumos a declarar no campo `Fato novo` do dossiê: a §14, a §15 e a §16 deste plano, e o ponto
     de partida que o dono deu — objetos `agente model designer` e `modelo`, operação
     `construir o modelo` (`D-31`). O campo `Restrição` do dossiê declara, literalmente, **três**
     coisas: (a) o ato é `autoria` e **substitui** a `## 1. Modelo conceitual` em forma anterior —
     **não** se cria `## 1A`, que é a forma da emenda; (b) nenhuma outra linha do plano é dele; e
     (c) o `check` vai acusar `V2` em toda tarefa enquanto os cards ainda citam `Oração do modelo`,
     e essas violações **não são dele** — devolve o ato com a saída literal (`D-53`, `DOM-T9b`).
  **Ato 2 — converter, depois que a outra mão agiu.**
  2. **Antes de qualquer edição**, rodar `python .claude/tools/modelo.py check --plano
     docs/plans/P-0743-modelo-de-dominio.md` e **devolver a saída literal** na linha de retorno. O
     estado de entrada esperado é exit `1`, `modelo: FALHOU — 18 violação(ões)`, e **todas** as
     linhas começando por `V2 `. Qualquer outro estado cai nas contingências 1, 3 ou 4 — **nenhum
     deles se resolve editando** (`D-52`, `I-16`).
  3. Conferir que a `### 1.4 Registro de versões` que o modelador gravou traz a linha da versão
     vigente. Se não trouxer, é ato dele incompleto: contingência 1.
  4. Converter o campo de cada card da §9 de `- **Oração do modelo:**` para
     `- **Operação do modelo:**`, **derivando a lista do que o modelador devolveu**: cada
     operação do fluxo traz a própria lista `tarefas:`, e o campo de um card é o conjunto das
     operações que o citam. Por operação citada, os dois sub-bullets que a gramática exige
     (`V14`): o texto copiado e a linha `precisa de:` com o contrato de cada objeto. **É
     derivação mecânica da entrega do modelador, não escolha do executor.**
  5. Card que nenhuma operação citar → **parar e sinalizar `blocked` razão `premissa`**, com a
     lista dos cards órfãos. Não inventar operação para cobri-lo, e não apagar o card: a
     `D-46` fechou a `Q-12` **sem afrouxar a `V2`**: card sem operação não passa no `check`, e
     resolver isso é replanejamento, nunca ato de executor (`D-49`).
  6. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - **O executor não escreve na `## 1. Modelo conceitual` — nem para corrigir.** A região não é
    alvo deste card (`D-52`): defeito nela é ato do modelador, e a rota é `blocked` razão
    `dependencia` com a saída literal do `check`. Redigir ou retocar o modelo aqui seria o executor
    decidindo domínio, que é o que a `D-5` concentra num agente só.
  - **O estado de entrada do ato 2 é evidência, não opinião**: vai na linha de retorno como saída
    literal do comando, nunca como frase sobre ela (`I-11`, `AE-12`). Quem confirma que o modelador
    agiu é o **registro do loop**, que o despachou — não o executor.
  - As demais seções do plano **não mudam** neste card: a fila, os achados e as decisões ficam.
  - Nenhuma contingência deste card cria arquivo (`I-10`). Não commitar (`I-6`).
- **Não fazer:**
  - Não apagar nem reescrever as orações `M-1`..`M-12` em outro lugar do plano: os cards vigentes
    as citam no campo `Oração do modelo`, e quebrar essas citações é defeito de coerência.
  - Não tocar plano nenhum do acervo (`D-3`).
- **Contingências:**
  1. Se o `check` do ato 2 sair `1` com **alguma** violação que não seja `V2` — indexada por
     `OP-<n>`, por `secao` ou por `objeto` (`V6`, `V7`, `V15`, `V17`), ou ainda `V4`/`V14` —, a
     seção entregue tem defeito → devolver a saída literal e sinalizar `blocked` razão
     `dependencia`. A família `objeto` foi medida no `ESC-10` e é a mais provável numa autoria
     (`AE-22`). **Não corrigir o modelo**: corrigir é ato
     do modelador.
  2. Se o `check` do ato 2 sair `2` (`modelo: forma anterior`) → a seção **não foi gravada**:
     `blocked` razão `dependencia`, com a saída literal. Não transcrever a seção você mesmo, mesmo
     que a tenha recebido no despacho — é a região que a `D-52` tira deste card.
  3. Se o `check` do ato 2 sair `0` **antes** de qualquer edição sua → alguém já converteu os
     campos, e há **duas mãos** na mesma região: `blocked` razão `premissa`, com a saída literal.
     É exatamente o caso que o `AE-21` mediu, e ele não se resolve seguindo em frente.
  4. Se um literal de aceite imprimir número diferente do declarado **e** o bloco estiver
     transcrito verbatim → **parar** e devolver `blocked` razão `premissa` com o comando, a
     contagem obtida e a linha do bloco de onde o literal sai (`I-16`, `AE-19`). Não ajustar o
     texto publicado, não relaxar o comando e não atribuir a falha a causa não medida.
- **Testes:** nenhum teste automatizado.
- **Verificação:**

  ```
  python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md
  ```
  sai `0` e imprime uma linha começando por `modelo: OK — ` (hoje sai `2` com
  `modelo: forma anterior — plano na forma de orações`, medido 2026-09-20).

  ```
  python .claude/tools/modelo.py show --plano docs/plans/P-0743-modelo-de-dominio.md
  ```
  sai `0` e a saída traz as seções `## Objetos`, `## Fluxo` e o estado final. **É esta saída que o
  dono lê no Marco 3.**

  ```
  grep -c '^### 1.3 Estado inicial e estado final' docs/plans/P-0743-modelo-de-dominio.md
  ```
  imprime `1`. Na árvore, antes do ato do modelador: `0` (medido 2026-09-21). **A âncora `^###` é
  obrigatória**: sem ela o comando imprime `9` hoje — o heading aparece citado dentro dos blocos
  literais deste plano —, o aceite passaria antes de a tarefa começar e não discriminaria os dois
  mundos (`D-54`, `AE-23`). Com a âncora, só a seção real casa, e é exatamente este heading que o
  instrumento exige (`.claude/tools/modelo.py:158`).

  ```
  grep -c '^- \*\*Oração do modelo:\*\*' docs/plans/P-0743-modelo-de-dominio.md
  ```
  imprime `0` (hoje imprime `18`, medido 2026-09-21 — um por card). O padrão é ancorado em
  `^- ` de propósito: conta **campo**, não citação. Contado sem a âncora, `Oração do modelo`
  aparece 37 vezes no plano, e as excedentes são texto de card fechado — `DOM-T5` publica o
  literal que remove o campo dos agentes — que **não se toca** (`I-3`).

  ```
  grep -c '^- \*\*Operação do modelo:\*\*' docs/plans/P-0743-modelo-de-dominio.md
  ```
  imprime `18` (hoje imprime `0`, medido 2026-09-21) — um campo por card, que é o que a `V2`
  exige. O número se re-deriva no despacho (`I-5`): é a contagem de `^### DOM-T` do plano.

  ```
  python .claude/tools/backlog.py check
  ```
  imprime `check: OK — nenhuma violação.` e sai `0`.
- **Pronto quando:** `modelo.py check` sobre este plano sai `0`, `show` imprime a leitura do dono
  com estado final, `backlog.py check` sai `0`, **a linha de retorno traz a saída literal do estado
  de entrada do ato 2** — exit `1`, `18` violações, todas `V2` — e o **registro do loop** mostra o
  despacho do modelador entre os dois atos deste card. É essa dupla — saída de comando mais
  registro de quem despachou — que discrimina a mão certa, e **nenhuma das duas é frase do
  executor sobre a própria entrega** (`I-11`, `AE-12`, `D-50`, `D-52`). A seção `## 1` **não entra
  no aceite deste card**: ela é entrega do ato do modelador.
- **Fora do escopo desta tarefa:** o modelo de qualquer outro plano, e tudo que muda papel
  (Marco 4).


### DOM-T6 — A porta de entrada, e a revisão do README [Sonnet · esforço medium · classe implementacao]
- **Status:** `done` · 2026-09-21
- **Depende de:** `DOM-T10`
- **Objetivo:** a seção pública do README descrevendo o modelo de domínio, o estágio e o modelador,
  e o `README.md` inteiro revisado contra o estado da árvore ao fim do plano.
- **Fundamento:** `D-1`, `D-2`, `D-5`, `D-48`, `D-50`; fatos `F-7`, `F-13`; invariantes `I-4`,
  `I-9`, `I-15`, `I-16`, `I-17`. O bloco da §8.1 **afirma comportamento do instrumento** — que
  `show` abre pelo estágio atual e que plano em forma anterior não é bloqueado —, e afirmação de
  comportamento não fecha por `grep` (`I-17`, `AE-22`): a `Verificação` traz os dois comandos que
  as confrontam. É a tarefa de revisão de README que `G-README` dever 2 exige de toda sprint.
  **O literal da §8.1 foi reescrito no `ESC-6`**: o que estava aqui descrevia o modelo com *lista
  de mudanças*, a forma que o terceiro estágio substitui — publicá-lo seria fechar o plano com a
  porta de entrada pública na forma anterior. A `Depende de` passou de `DOM-T5` para `DOM-T10` pela
  mesma razão que moveu esta tarefa para o fim (`AE-16`): ela revisa o README **contra a árvore
  final**, e a árvore só fica final depois da `DOM-T10`.
- **Operação do modelo:** `OP-13`
  - OP-13: O mantenedor abre a porta de entrada pública ao modelo de domínio e confere a documentação pública contra o estado da árvore ao fim do plano.
  - precisa de: modelo deste plano — seção `## 1. Modelo conceitual` de `docs/plans/P-0743-modelo-de-dominio.md` e o campo `Operação do modelo` de cada card da §9; a seção é ato do modelador e o campo é ato do executor que converte os cards, e as duas mãos não se cruzam; doutrina publicada do kit — `GOVERNANCA.md`, as skills e os agentes do kit; cada ponteiro nomeia a seção vigente que governa a forma, e ponteiro órfão é defeito no caminho da entrega, não dívida a pagar depois; instrumento do modelo — `.claude/tools/modelo.py`, verbos `check` e `show`, exits `0`, `1` e `2` com literais fixos; lê as tarefas do plano por `backlog._parse_plano` e não reescreve `backlog.py`; cada regra nova nasce com fixture e teste pelo caminho do usuário
- **Camada e fronteira:** documentação pública, na raiz. Nenhum código, nenhum teste.
- **Arquivos-alvo:**
  - `README.md`
    - **arquivo inteiro**: o passo 3 varre o arquivo todo e o aceite é de coerência dele inteiro
      (`I-10`)
    - região de substituição literal 1: a `### 8.1 O modelo conceitual — o que o dono lê`, do
      heading até a linha anterior ao próximo heading — linha 644 em 2026-09-20
    - região de substituição literal 2: a frase que remete a §8.1 — linha 420 em 2026-09-20
    - os dois números se re-derivam no despacho (`I-5`), localizados por conteúdo
- **Texto novo, literal — substituição integral da §8.1 de `README.md`:**

  ```markdown
  ### 8.1 O modelo de domínio do plano — o que o dono lê

  Todo plano carrega, logo depois do pedido, a seção **Modelo conceitual**: uma tabela de **objetos**,
  cada um com as **propriedades** observadas e o contrato de quem implementa; um **fluxo de
  operações** encadeadas, que dizem quem age, o que faz, de que objetos precisa e que propriedades
  altera; o **estado inicial e o estado final** de cada propriedade; e o **registro de versões** do
  modelo. O texto da operação, com o contrato dos objetos, chega copiado ao card da tarefa, para que
  o executor saiba do que precisa sem abrir o plano.

  O **estado final é o desejo do dono**, e é por ele que o plano se aceita: o plano só é bem-sucedido
  se o estado final real for o especificado, e essa diferença é o que tem valor para quem pediu. O
  andamento, esse, **não é gravado em lugar nenhum**: é derivado do estado das tarefas. Uma operação
  está concluída quando todas as tarefas dela fecharam, em curso quando alguma está em execução ou em
  revisão, e prevista no resto. O **estágio atual** do plano é a primeira operação que ainda não
  concluiu. O dono lê uma linha — qual é o estágio — em vez de um estado por frase.

  O modelo **versiona, não se reescreve**: quando uma decisão muda o que o plano entrega, a versão
  nova nasce ao lado da vigente, marcada como pendente, e as duas coexistem até o marco seguinte, em
  que o dono aceita ou recusa. Quem escreve o modelo é um agente só, o `pantonic-model-designer`: ele
  escreve na autoria, emenda quando uma decisão muda o que o plano entrega e resolve conflito entre o
  texto e a entrega. Nenhum
  outro papel escreve ali; quem precisa de um ato de modelo devolve um dossiê fechado, e quem conduz
  a sessão o despacha. O instrumento `.claude/tools/modelo.py` confere a seção (`check`) e gera a
  leitura do dono (`show`), que abre pelo estágio atual. Planos escritos antes desta doutrina não são
  migrados: o instrumento os reconhece como forma anterior e não bloqueia nada.
  ```

- **Texto novo, literal — substituição da frase da linha 420 de `README.md`:**

  ```markdown
  **sinaliza** `blocked` com a razão tipada e escala — não improvisa uma alternativa própria. O plano nasce com o **modelo de domínio** (§8.1), e o dono dá go ou no-go lendo só ele — é o Marco 1 de todo plano.
  ```

- **Passos:**
  1. Substituir a §8.1 inteira pelo bloco literal acima, do heading (linha 644 em 2026-09-21) até
     a **última linha com texto** da seção (a 655), **preservando a linha em branco** que a separa
     do heading `## 9.` (a 656). O bloco entra com **25 linhas**: a primeira é o heading, a última
     termina em `não bloqueia nada.`. Os três números se re-derivam no despacho (`I-5`).
  2. Substituir a frase da linha 420 pelo literal acima.
  3. Percorrer o `README.md` inteiro com
     `grep -n -e 'orações' -e 'oração' -e 'modelo conceitual' -e 'Modelo conceitual' README.md`.
     **Medido no `ESC-3`, 2026-09-20:** todas as ocorrências que descrevem a forma do modelo
     estão **dentro** da §8.1 (linhas 644-655) e na linha 420 — isto é, dentro das duas regiões
     que os passos 1 e 2 já substituem por bloco literal. As duas que sobram **ficam como
     estão**: a 384 é a palavra `exploração` e a 393 fala do *modelo conceitual em clean
     architecture*, que é outro assunto. Depois dos passos 1 e 2 este passo não tem nada a
     fazer — **confirme e siga**.
     Se o grep encontrar, fora das duas regiões, alguma frase que descreva a forma do modelo do
     plano, **não redija texto novo**: pare e sinalize `blocked` razão `premissa`, com a linha
     encontrada. Este card não traz bloco literal para ela, e redigir doutrina em execução é o
     que o `AE-10` proíbe.
  4. Rodar `pwsh -NoProfile -File .claude/checks/check-readme.ps1`. **Medido no `ESC-4`,
     2026-09-20: sai `0`** com `10 agente(s), 11 skill(s), 20 guardrail(s), versão '0.0.0',
     14 seção(ões) com Fonte da verdade válida`, e as duas edições deste card são de uma
     subseção `###` e de uma frase — não mexem em contagem de agente, skill, guardrail nem em
     linha `Fonte da verdade`. Se ainda assim sair diferente de `0`, corrigir **só** o item que
     a saída nomear (contingência 1). Se o item nomeado exigir redigir texto normativo que
     nenhum bloco deste card fornece, **não redija**: pare e sinalize `blocked` razão
     `premissa`, com a saída literal (`I-13`, `D-20`).
  5. Devolver, na linha de retorno, a saída literal de `check-readme.ps1` — é o insumo do
     veredito do dono — e o **sinal** `fidelidade conferida: §8.1` e `fidelidade conferida:
     linha 420`, sem contagem de linhas (`I-11`).
  6. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - `README.md` (a raiz) e `.claude/README.md` são arquivos diferentes (`I-9`): esta tarefa toca
    **só** o da raiz, e não regenera nada.
  - A tabela **Agentes** e a frase de contagem da §11 já foram fechadas pela `DOM-T4`; esta tarefa
    não as toca, e o passo 3 as exclui explicitamente.
  - Frase que conta ou enumera se fecha no mesmo card que muda o conjunto (`I-4`).
  - Nenhuma contingência deste card cria arquivo. Se alguma só puder ser cumprida criando
    arquivo não declarado nos `Arquivos-alvo`, o card está incompleto: sinalizar `blocked` razão
    `premissa` (`I-10`).
  - Não commitar (`I-6`).
- **Não fazer:**
  - Não tocar `.claude/README.md`.
  - Não alterar a frase de contagem `O kit são dez agentes, …`.
  - Não abrir nem alterar plano nenhum de `docs/plans/`.
- **Contingências:**
  1. Se `check-readme.ps1` sair diferente de `0` por causa de item alheio a esta sprint → corrigir
     só o que a saída nomear e registrar na linha de retorno como
     `contingência 1 acionada: <item>`.
  2. Se o passo 3 encontrar ocorrência de `orações` ou de `modelo conceitual` que **não** descreva
     a forma do modelo do plano → deixar como está e registrar a linha na linha de retorno. As
     duas conhecidas em 2026-09-20 são a 384 e a 393.
  3. Se um literal de aceite imprimir número diferente do declarado **e** o bloco estiver
     transcrito verbatim → **parar** e devolver `blocked` razão `premissa` com o comando, a
     contagem obtida e a linha do bloco de onde o literal sai (`I-16`, `AE-19`). Não ajustar o
     texto publicado, não relaxar o comando e não atribuir a falha a causa não medida.
- **Testes:** nenhum teste automatizado. O guarda executável é `check-readme.ps1`, e o veredito do
  dono é gate de fechamento, não critério desta entrega.
- **Verificação:**

  ```
  pwsh -NoProfile -File .claude/checks/check-readme.ps1
  ```
  sai `0` e a saída começa por `check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s)`.

  ```
  grep -c '8.1 O modelo de domínio do plano' README.md
  ```
  imprime `1` (hoje imprime `0`).

  ```
  grep -c 'numeradas que afirmam o que o resultado faz' README.md
  ```
  imprime `0` (hoje imprime `1`, na linha 647, medido 2026-09-20).

  ```
  grep -c 'modelo de domínio' README.md
  ```
  imprime **o valor medido antes da primeira edição, mais `2`**. Hoje esse valor é `1` — a linha
  820, da tabela **Agentes**, que a `DOM-T4` entregou e este card não toca (medido 2026-09-21) —,
  logo o esperado hoje é `3`: o pré-existente, mais o heading da §8.1 e a frase da linha 420. O
  piso é **relação, não constante** (`D-54`): rode o comando **antes** da primeira edição, some
  `2`, e é esse o número de aceite (`I-5`). A linha de base declarada antes desta rodada era `0`,
  e era falsa.

  ```
  grep -cF -e 'o instrumento os reconhece como forma anterior e não bloqueia nada.' README.md
  ```
  imprime `1` (hoje imprime `0`, medido 2026-09-21) — **última** linha do bloco da §8.1: fecha a
  borda de baixo da substituição, que o grep do heading não alcança (`I-11` item 2).

  **Comportamento — as duas afirmações do bloco confrontadas com o instrumento** (`I-17`), pelo
  caminho do usuário:

  ```
  python .claude/tools/modelo.py check --plano docs/plans/P-0741-modelo-conceitual.md
  ```
  sai `2` e imprime `modelo: forma anterior — plano na forma de orações (sem '### 1.2 Fluxo de
  operações')` — medido 2026-09-21. É a prova da frase *"o instrumento os reconhece como forma
  anterior e não bloqueia nada"*: exit `2` não é falha.

  ```
  python .claude/tools/modelo.py show --plano tests/fixtures/modelo/fluxo-valido.md
  ```
  sai `0` e a **segunda** linha contém `estágio atual: OP-2 — ` — medido 2026-09-21. É a prova da
  frase *"gera a leitura do dono (`show`), que abre pelo estágio atual"*.

  **Censo do arquivo inteiro** (`D-50`), que é o que dá poder discriminante à última cláusula do
  `Pronto quando`:

  ```
  grep -c 'orações' README.md
  ```
  imprime `0` (hoje imprime `2`, nas linhas 646 e 648, medido 2026-09-20; as duas estão **dentro**
  da §8.1, que o passo 1 substitui inteira). O padrão é `orações`, no plural, de propósito: a forma
  singular casa dentro de `exploração`, na linha 384, que não fala de modelo nenhum.

  ```
  grep -cF -e 'propriedades** observadas' README.md
  ```
  imprime `1` (hoje imprime `0`, medido 2026-09-20) — a §8.1 na forma do terceiro estágio.

  ```
  grep -cF 'modelo de domínio** (§8.1)' README.md
  ```
  imprime `1` (hoje imprime `0`, medido 2026-09-20) — a frase da linha 420 entregue. `-F` é
  obrigatório: a frase tem `**`, que em expressão regular não é literal.

  ```
  grep -cF 'modelo conceitual** (§8.1)' README.md
  ```
  imprime `0` (hoje imprime `1`, na linha 420, medido 2026-09-20) — a frase que tem de sumir
  (`I-11` item 3).

  ```
  sed -n '/^### 8.1 O modelo de domínio do plano/,/não bloqueia nada\.$/p' README.md
  ```
  sai idêntico, linha a linha, ao bloco cercado da §8.1 deste card — **25 linhas**, da linha do
  heading à que termina em `não bloqueia nada.` (contagem do bloco medida em 2026-09-21). O fim do
  intervalo é a **última linha do bloco**, e não `^## 9\.`: terminado no heading seguinte, o
  comando imprime duas linhas a mais que o bloco — a linha em branco e o próprio `## 9.` —, e a
  igualdade declarada seria falsa por construção (`D-54`). **É este comando, e não a declaração do executor, que prova a fidelidade**
  (`I-11` item 1). A declaração `fidelidade conferida: <bloco>` vai na linha de retorno como
  **sinal**, em `Passos`, sem contagem de linhas: o número autodeclarado errou duas vezes em
  treze na `DOM-T5` (`AE-12`), com os treze blocos corretos byte a byte.
- **Pronto quando:** os comandos da `Verificação` devolvem os números declarados — inclusive as
  duas bordas da §8.1 e as duas formas da frase da linha 420 —, o `sed` da §8.1 sai idêntico ao
  bloco cercado, `check-readme.ps1` sai `0` anunciando dez agentes, e **o censo de `orações`
  imprime `0`** — é ele, e não juízo do executor, que afirma que nenhuma frase do `README.md`
  descreve o modelo como orações numeradas (`D-50`) — **e os dois comandos de comportamento saem
  como declarado** (`I-17`). **Nenhum item deste
  `Pronto quando` se apoia em frase escrita pelo executor sobre a própria entrega** (`I-11`,
  `D-22`, `AE-12`).
- **Fora do escopo desta tarefa:** o veredito do dono sobre o README, que é gate de fechamento
  registrado pela orquestração (`GOVERNANCA.md` §4.5) e não entrega desta tarefa.

---

## 10. Ordem de execução

Fila única, sequencial. Nada roda em paralelo: cada tarefa consome o artefato da anterior.

```
DOM-T1 (norma)
   └→ DOM-T2 (gramática)
        └→ DOM-T3 (instrumento)
             └→ DOM-T3a (o que o instrumento e a gramática dizem de si mesmos)
                  └→ DOM-T3b (a referência cruzada do docstring)
                       └→ DOM-T4 (modelador)
                            └→ DOM-T5 (papéis)
                                 └→ DOM-T5a (a costura do retorno do revisor)
                                      └→ DOM-T5b (a cadeia do retorno, do emissor ao consumidor)
                                           └→ DOM-T7 (a norma da forma nova)
                                                └→ DOM-T8 (a gramática da forma nova)
                                                     └→ DOM-T8a (os ponteiros que a forma nova deixou para trás)
                                                          └→ DOM-T9 (o instrumento)
                                                               └→ DOM-T9a (o modelador fala a forma nova)
                                                                    └→ DOM-T9b (o gate que o modelador consegue fechar)
                                                                         └→ DOM-T9c (a quarta família de violações)
                                                                              └→ DOM-T10 (o modelo deste plano)
                                                                                   └→ DOM-T6 (porta de entrada e revisão do README)
```

> O grafo acima ficou parado no estágio 2 até 2026-09-20 e foi estendido no `ESC-6`. A residência
> que manda na fila é a linha `**Ordem de execução:**` do cabeçalho (`backlog.py` lê dela); este
> grafo é a razão de cada aresta, e as duas concordam.

- `DOM-T2` depende de `DOM-T1` porque a gramática é a forma da norma; publicá-la antes abriria
  janela em que as duas divergem — o defeito que a `MC-T1` produziu no plano anterior.
- `DOM-T3` depende de `DOM-T2` porque implementa a gramática, não a inventa.
- `DOM-T3a` depende de `DOM-T3` porque repara o resíduo que a reescrita dela deixou, e vem
  **antes** da `DOM-T4` porque a `DOM-T4` e a `DOM-T5` leem o `--help` e a skill enquanto
  trabalham: deixar o resíduo vivo é deixar duas fontes divergentes do mesmo fato na mesa de
  quem executa (`D-16`).
- `DOM-T3b` depende de `DOM-T3a` porque corrige um token do bloco que a `DOM-T3a` publicou, e
  vem antes da `DOM-T4` pela mesma razão que a `DOM-T3a`: referência cruzada errada no
  instrumento é uma segunda fonte do mesmo fato na mesa de quem executa os cards seguintes
  (`D-18`).
- `DOM-T4` depende de `DOM-T3b` porque o agente novo se auto-confere com o instrumento, e o
  ensinamento que ele carrega não pode contradizer o que o instrumento diz de si mesmo.
- `DOM-T5` depende de `DOM-T4` porque as cláusulas dos papéis nomeiam o agente.
- `DOM-T5a` depende de `DOM-T5` porque repara o quinto ponto do arquivo que ela entregou, e vem
  antes da `DOM-T6` porque é conduta, não documentação pública: a `DOM-T6` revisa o README
  **contra a árvore final**, e a árvore só fica final quando a cadeia revisor → loop →
  modelador fecha (`D-21`).
- `DOM-T5b` depende de `DOM-T5a` porque fecha, no `scrum-master` e no domínio de saída do
  revisor, a mesma interface que ela abriu na definição do papel, e vem **antes** da `DOM-T6`
  pela razão de sempre: a `DOM-T6` revisa o README **contra a árvore final** (`D-23`).
- `DOM-T7` → `DOM-T8` → `DOM-T9` seguem a ordem norma → gramática → instrumento, a mesma dos
  estágios 1 e 2 e pela mesma razão: publicar a forma antes da norma abre a janela em que as duas
  divergem (`AE-4`).
- `DOM-T8a` depende da `DOM-T8` por duas razões, e as duas são de conteúdo: as linhas que ela
  repara passam a **apontar** para `### 1.4 Registro de versões`, que a gramática acabou de definir
  — repará-las antes seria apontar para residência inexistente —, e o bloco `R5` só é verdadeiro
  depois que a §15 está transcrita. Vem **antes** da `DOM-T9` porque quem executa a `DOM-T9` lê a
  norma **e a gramática** enquanto trabalha, e o ponteiro do preâmbulo manda, hoje, para a §5, que
  é a forma anterior: resíduo vivo é segunda fonte do mesmo fato na mesa de quem executa (`D-16`,
  `AE-18`).
- `DOM-T9a` depende da `DOM-T9` porque todo ato do modelador termina em `modelo.py check` exit `0`:
  publicar os deveres da forma nova antes de o instrumento os aceitar fabricaria um gate
  impossível. Vem **antes** da `DOM-T10` porque a `DOM-T10` **despacha o modelador** — é a única
  tarefa do plano que o faz —, e ele lê a própria definição antes de agir (`D-48`).
- `DOM-T9b` depende da `DOM-T9a` porque reescreve um bullet do arquivo que ela acabou de fechar, e
  vem **antes** da `DOM-T10` porque é ela que despacha o modelador: com o gate vigente, o ato dele
  não tem como terminar num plano em conversão (`D-53`).
- `DOM-T9c` depende da `DOM-T9b` porque reescreve o bullet que ela acabou de publicar, e vem
  **antes** da `DOM-T10` pela mesma razão que a `DOM-T9b`: a `DOM-T10` despacha a **primeira
  autoria** do modelador neste plano, e `V15` e `V17` — as violações órfãs — são as faltas mais
  prováveis desse ato (`AE-22`).
- `DOM-T10` depende da `DOM-T9c` e roda em **dois despachos**, com o ato do modelador entre eles:
  ato 1 pede e para em `blocked` razão `dependencia`; o loop despacha o `pantonic-model-designer`,
  que **grava** a seção; ato 2 confere o estado de entrada e converte os campos dos cards (`D-52`).
- `DOM-T6` é a última por `G-README` dever 2: a revisão do README se faz contra a árvore final.

---

## 11. Fora de escopo (explícito)

| o que fica de fora | por quê | onde mora |
|---|---|---|
| A especificação do agente de planejamento | assunto disjunto, com arquivos disjuntos (`D-13`) | `P-0744` |
| Migrar o `P-0741` para a forma nova | o plano está fechado e as orações dele são verdadeiras sobre o que entregou (`D-10`) | linha `MD-9` na lista de mudanças do próprio `P-0741` |
| A enumeração de agentes de `GOVERNANCA.md` §9, que cita três de nove | já está defasada antes deste plano; corrigi-la aqui seria varredura fora do tema | tíquete novo, a abrir no diário |
| As seis pendências abertas do `P-0741` (`docs/OPERACOES_AS_IS.md`) | nenhuma é bloqueante e nenhuma é do tema deste plano | as residências declaradas na tabela de pendências daquele documento |
| A `MC-T5` e o fechamento do `P-0741` | o `Pronto quando` dela exige veredito do dono, que é ato dele | `docs/DIARIO_DE_OBRAS.md`, no aceite do Marco 2 do `P-0741` |
| Qualquer edição em `backlog.py`, `review_evidence.py` e `card_check.py` | invariante `I-1` | — |
| O driver do `P-0742` | plano próprio, `blocked`; a edição da `DOM-T5` viaja para ele por transcrição literal (`F-15`) | `docs/plans/P-0742-loop-fora-do-llm.md` |

---

## 12. Riscos

| risco | resposta pré-decidida |
|---|---|
| O `P-0742` começa antes deste plano fechar e reescreve o roteamento do `scrum-master`, perdendo a edição da `DOM-T5` | o `P-0742` transcreve a skill **literalmente** (`DLF-6`, `F-15`); a ordem barata é este plano fechar primeiro. Se o `P-0742` for despachado antes, a `DOM-T5` fica `blocked` razão `dependencia` e volta à fila depois da `LF-T3` |
| A `DOM-T3` reescreve o instrumento e algum plano do acervo passa a sair `1` em vez de `2` | a `DOM-T3` verifica `modelo.py check` sobre o `P-0741` e exige exit `2` com o literal de forma anterior; qualquer plano do acervo que saia `1` é fixture faltando, e a contingência 2 da `DOM-T3` cobre |
| A fixture de quatorze violações esconde uma violação atrás de outra | contingência 2 da `DOM-T3`: partir em duas fixtures e somar as saídas |
| O numeral da frase de contagem do README fica por extenso errado e `check-readme.ps1` reprova | contingência 2 da `DOM-T4`: corrigir a frase, nunca a tabela |
| Um dos cards muda uma enumeração e deixa para trás a frase que a conta — a classe que apareceu cinco vezes no `P-0741` | invariante `I-4` em todos os cards, e a `Verificação` de cada card que mexe em enumeração publica **os dois** valores, antes e depois |
| Número de aceite deste plano caduca entre o planejamento e o despacho | invariante `I-5`: todo número é referência datada de 2026-09-20 e se re-deriva no despacho |

---

## 13. O terceiro estágio do modelo — diretiva do dono de 2026-09-20

> **Status desta seção:** insumo de **planejamento**, não de execução. Ela grava a diretiva, mapeia
> o alcance e enumera o que o desenho ainda não fecha. **Nenhum card do terceiro estágio foi
> escrito**, e a razão está em §13.4.

### 13.1 A diretiva, verbatim

> Gostei da divisão do modelo em objeto e fluxo de operações. Mudanças, na forma descrita, não deve ser parte do modelo, ele a descrição indica um evento, e eventos são ocorrências que alteram o estado do modelo. O estado do modelo é definido por duas variáveis: os objetos trabalhados, e o fluxo de operações nos quais esses objetos participam.
> No lugar de "mudanças", deve entrar "propriedades". Um modelo de modelo inicia com os objetos com certas propriedades, e, por meio do fluxo de operações, essas propriedades se alteram, sendo geralmente as propriedades finais o estado "desejável" do modelo. Assim, por meio das propriedades é possível modelar o "aceite" do plano: o plano somente será bem sucedido se o estado final for o especificado no modelo. Essa abordagem funcionaria neste plano em particular: nosso modelo seria o agente model designer e o modelo. Por meio da operação "construir o modelo", receberiamos o "modelo" no padrão esperado, facilmente testável e ajustável. As tarefas resultantes que não estejam abrangidas no modelo significam que não tem interesse para o usuário/gerente do projeto/domain expert, e devem ser realizadas, sim, mas devem ser mantidas de forma transparente. A validação da mecânica será evidente apenas pela confrontação do estado final do modelo real com o estado final modelo conceitual, e essa diferença é de valor para o cliente.
> Vamos começar por esse "modelo de um modelo", e se a necessidade requerer outra forma de modelo, veremos no futuro.
> Sobre o artefato 2, com base no mencionado acima, fica mecânico a elaboração do modelo: ele demandará uma entrada de dados: objetos, operações e estados inicial e final.
> Acrescente, porém, o versionamento. Se um agentes escrever uma emenda ao modelo original, o novo modelo deverá ser versionado. No final do plano, o "drift" será avaliado se adequado ou não. Modelos são seres vivos que podem se alterar com base na evolução do projeto, mas um "rewrite" não é adequado. O versionamento deve ser criado, apresentado no próximo marco, e, caso validado, aí pode ser feito um "merge" nas versões.
> Deixe a resolução de conflitos com o consultor. Se o agente model designer consegue versionar mudanças, ele pode guardar as informações recebidas, e deixar para o agente apropriado decidir. Não quero que o model designer seja mais um controle do processo. Sua função é ver o modelo, e não o projeto, por isso ele não tem o cenário completo para inferir se uma mudança é pertinente ou não.
> Gere novos cards no mesmo plano para continuar no próximo contexto o terceiro estágio do "modelo", e das responsabilidades revistas do "model designer"

### 13.2 O alcance, mapeado

Oito residências, e a comparação de tamanho é com os estágios 1 e 2 **deste plano**, que custaram
seis cards e quatro corretivos.

| residência | o que o terceiro estágio muda nela | decisões |
|---|---|---|
| `GOVERNANCA.md` §3.2 (norma) | sai `Mudanças`, entra `Propriedades`; estado do modelo definido por objetos e fluxo; aceite do plano modelável; versionamento; o ato de conflito muda de dono | `D-24`..`D-30` |
| skill `diario-de-obras` (gramática) | a tabela `### 1.1 Objetos` ganha propriedades; `### 1.3` deixa de ser lista de mudanças; entram estado inicial e estado final; entra a marca de versão | `D-24`, `D-25`, `D-28`, `D-29` |
| `.claude/tools/modelo.py` (instrumento) | `V13` muda de conteúdo; `V2` deixa de ser violação universal; nascem regras de propriedade e de estado; `show` passa a abrir pelo estado e a exibir drift; versão vira eixo. Testes e fixtures inteiros | `D-24`..`D-29` |
| `.claude/agents/pantonic-model-designer.md` | perde o ato `conflito` como decisão, ganha registro e versionamento; a entrada de dados vira declarada | `D-28`, `D-29`, `D-30` |
| `.claude/agents/pantonic-consultant.md` | ganha a resolução de conflito de modelo | `D-30` |
| `.claude/agents/pantonic-reviewer.md` e skill `scrum-master` | a cadeia do dossiê muda de destino, e com ela os elos que o `ESC-5` e o `AE-15` mapearam | `D-30`, `AE-15` |
| anatomia do card (`pantonic-planner.md`) e `Operação do modelo` | tarefa fora do modelo passa a ser legítima e marcada como transparente | `D-27` |
| marcos do plano | o drift é apresentado no marco seguinte e avaliado ali | `D-29` |

**Leitura de tamanho, honesta.** Isto não é um estágio dentro de uma janela: é da ordem de grandeza
do `DOM-T1`..`DOM-T5` somados, porque percorre as mesmas oito residências e refaz o instrumento.
Empacotar para caber numa janela seria o defeito que este plano já pagou quinze vezes.

### 13.3 O que o desenho ainda não fecha

Enumeradas, **não resolvidas** — resolvê-las é ato de planejamento com o dono, e nenhuma delas o
executor pode decidir (`G-NOASK`, Regra 8).

| id | questão aberta |
|---|---|
| `Q-1` | **Régua de granularidade de propriedade.** O que é uma propriedade e o que não é? O `docs/OPERACOES_AS_IS.md` já registra a ausência dessa régua como entrega pela metade; o desenho novo a torna bloqueante, porque é a propriedade que carrega o aceite |
| `Q-2` | **Forma do estado inicial e do estado final.** Por objeto, por propriedade, ou tabela única de duas colunas? O verbatim diz "objetos com certas propriedades" e "propriedades finais", sem fixar a forma |
| `Q-3` | **Teste do que é objeto.** A confrontação de estado final só é mecânica se "objeto" for decidível. O `OPERACOES_AS_IS` registra que esse teste não existe |
| `Q-4` | **Forma do versionamento.** Versão nova da seção no mesmo arquivo, arquivo próprio, sufixo? E o que `modelo.py show` mostra com duas versões vivas? |
| `Q-5` | **O que é "drift".** O verbatim usa o termo uma vez para a diferença entre versões do modelo e, em outro ponto, fala da "confrontação do estado final do modelo real com o estado final modelo conceitual". **Podem ser a mesma medida ou duas medidas diferentes**; o texto não decide |
| `Q-6` | **O que substitui a `V2`.** Tarefa sem operação deixa de ser violação, ou vira violação de outra classe? E qual é a **marca de transparência** no card de uma tarefa fora do modelo? |
| `Q-7` | **Onde o modelador "guarda" enquanto o versionamento não existe.** O verbatim condiciona: *"Se o agente model designer consegue versionar mudanças, ele pode guardar"* — a ordem entre as duas coisas não está fixada |
| `Q-8` | **O ato `conflito` do modelador é removido ou muda de natureza** (de decidir para registrar)? O verbatim diz que ele "guarda" e "deixa para o agente apropriado decidir" |
| `Q-9` | **Se o consultor resolve o conflito, ele escreve no modelo?** *"Deixe a resolução de conflitos com o consultor"* fixa quem **decide**; decidir não é escrever. Se o consultor escrever, cai `M-9` e `D-5` — um agente só é dono de todo ato sobre o modelo. Se não escrever, falta dizer como a decisão dele volta ao modelador |
> **Superadas.** As dez questões foram fechadas pelo dono em `D-33`..`D-44` no mesmo dia; a
> `Q-11` e a `Q-12` de §13.5 foram fechadas pela `D-47` e pela `D-46`. **Nenhuma questão deste
> plano está aberta** (`D-49`). Esta tabela fica como registro do que o desenho não fechava no ato
> da diretiva — não como trava vigente de card nenhum.

| `Q-10` | **O que os marcos passam a ser.** Se o estado final especificado é o aceite do plano, o Marco 1 passa a ser o dono validando o estado final? E o que resta do Marco 2 deste plano, cuja leitura é a saída de `show` na forma que o terceiro estágio substitui? |

### 13.4 Por que nenhum card foi escrito (superado em 2026-09-20)

Cada card do terceiro estágio depende de ao menos uma das dez questões acima. Um card escrito hoje
cairia numa destas duas formas, e as duas são proibidas por doutrina deste plano:

- **Card com ponto sem bloco literal** — `I-13`, nascido do `AE-10`: o executor para em `blocked`
  razão `premissa` em vez de redigir. Publicá-lo seria fabricar o bloqueio de antemão.
- **Card que empurra decisão de desenho para a execução** — Regra 8 e `G-NOASK`: *"se para começar
  o executor precisaria perguntar ou decidir algo, o plano está incompleto — devolve ao
  planejamento e não performa."*

O que **sobrevive ao próximo contexto** e é o insumo daquela sessão está gravado: as decisões
`D-24`..`D-32` na §3, este mapa de alcance e estas dez questões. O `docs/OPERACOES_AS_IS.md`
completa o quadro com o estado medido dos artefatos.

> **Superado.** O dono fechou as dez questoes em `D-33`..`D-44` no mesmo dia. Os cards do **Marco
> 3** — `DOM-T7`..`DOM-T10` — estao escritos na secao 9, e as residencias normativas deles sao as
> secoes 14, 15 e 16. Os Marcos 4 e 5 seguem sem cards, pela razao de 13.5.

### 13.5 Por que os Marcos 4 e 5 ainda nao tem cards

**Duas razoes, e a primeira e doutrinaria.** A regua de marco que o dono acabou de fixar (`D-43`)
diz que marco e **detector de desvio**: chegar a `-100` no meio do caminho diz que o processo ja
falhou, *"nao precisa chegar ao termino do plano para concluir o desvio"*. O Marco 3 mede se a
forma nova e reconhecivel pelo dono — se ele nao reconhecer o estado final como o desejo dele, tudo
que os Marcos 4 e 5 escreveriam esta errado. Escrever esses cards agora e gastar antes do detector.

**A segunda razao e que faltam duas respostas**, e as duas sao do dono. Ficam registradas aqui na
mesma forma das dez anteriores, **nao resolvidas**:

> **Superada em 2026-09-20, no mesmo dia.** A `Q-11` foi fechada pela `D-47` e a `Q-12` pela
> `D-46`. **A segunda razão caiu; a primeira, não** — e ela sozinha sustenta a ausência de cards
> dos Marcos 4 e 5: a régua da `D-43`. As duas linhas abaixo ficam como registro do que faltava
> (`D-49`).

| id | questao aberta | quem trava |
|---|---|---|
| `Q-11` | **Qual e o destino da divergencia que o revisor apura.** A `D-38` separa **medicao** (resultados contra o modelo) de **drift** (variacao do modelo); a divergencia que o revisor acha no passo `5a` e **medicao**, nao conflito. A `D-40` tira o ato `conflito` do modelador e a `D-41` define conflito como a existencia de um pos-drift e um vigente que nao e ele. **Resultado: a cadeia revisor -> loop -> modelador, que a `DOM-T5`, a `DOM-T5a` e a `DOM-T5b` construiram, fica sem destino** — o dossie `Ato de modelo` de `conflito` que o revisor devolve nao tem mais quem o receba. A divergencia de medicao vira proposta de drift? De quem e esse ato? Ou o revisor so abre achado e nada mais viaja? | `DOM-T11` (consultor e cadeia) e a parte de papeis da norma |
| `Q-12` | **Como uma tarefa tatica existe mecanicamente.** A glosa da `D-42` diz que a `V2` nao muda e que o que muda e o que sobe ao dono, *"nao o que se permite no plano"*. Mas a `V2` exige campo `Operacao do modelo` em **toda** tarefa do plano: com ela intacta, **tarefa sem lastro no modelo nao passa no `check`**, e a `D-42` diz que ela e legitima. O verbatim do dono **nao menciona a `V2`** — a tensao esta entre a decisao e a glosa, nao no que o dono disse. Ou a `V2` afrouxa, ou "tatica" descreve outra coisa | `DOM-T13` (tatica e estrategia) |

**O que isso nao trava.** Nada do Marco 3: a `DOM-T7` publica so a forma e tem, escrito no proprio
card, o `Nao fazer` que a impede de tocar a tabela de papeis; a `DOM-T8` nao toca a linha
`| campo do card |`; a `DOM-T9` preserva a `V2` como esta. **Nenhuma metade de mudanca de papel e
publicada** — que e o defeito `AE-11`, medido duas vezes neste plano.

**E o que isso não protegia, medido no `ESC-6`.** Não tocar a tabela de papéis protege o **papel**;
não protege a **forma do que o papel devolve**. Cinco pontos da árvore mandavam o modelador
devolver a linha `MD-<n>`, cuja última residência a `DOM-T8` remove, e nenhum card os re-declarava
(`AE-17`). A `DOM-T8a` e a `DOM-T9a` os reparam **sem tocar em papel nenhum** (`D-48`).

**Cards previstos dos Marcos 4 e 5, para dimensionamento — nao sao cards, sao escopo.**

| id previsto | marco | escopo | trava |
|---|---|---|---|
| `DOM-T11` | 4 | o modelador perde `conflito` (`D-47`) e ganha a entrada de dados declarada (`D-28`, `D-40`, `D-44`). **A forma do registro da versão sai daqui**: é forma, não papel, e foi para a `DOM-T9a` do Marco 3 (`D-48`) | régua do marco (`D-43`) |
| `DOM-T12` | 4 | o consultor ganha recusar e escalar drift; a cadeia inteira reencaminhada, **absorvendo o `AE-15`** (`D-41`, `D-47`, `I-14`) | régua do marco (`D-43`) |
| `DOM-T13` | 5 | tatica e estrategia no que sobe ao dono: relatorio de encerramento e apresentacao de marco (`D-42`, `D-46`) | régua do marco (`D-43`) |
| `DOM-T14` | 5 | a regua de marco publicada como doutrina (`D-43`) | nenhuma |
| `DOM-T6` | 5 | a porta de entrada publica, ja escrita, migrada do Marco 2 extinto | nenhuma |

---

---

## 14. Norma do terceiro estágio (texto literal para `GOVERNANCA.md` `### 3.2`)

Insumo literal da `DOM-T7`, que o transcreve verbatim (`I-3`); **residência depois da transcrição:
`GOVERNANCA.md` §3.2** (`D-51`). Supersede, nos três parágrafos que nomeia, o bloco da §4.
**Esta seção cobre só a forma do modelo.** O que muda nos **papéis** — o modelador perder o ato
`conflito` (`D-40`), a autoridade do consultor (`D-41`) e a cadeia do retorno — **não está aqui**:
está no Marco 4, e depende da `Q-11` (§13.3), que está aberta.

> **Bloco P1** — substitui integralmente o parágrafo `**O que é.**` de `GOVERNANCA.md` `### 3.2`,
> linhas 323-331 em 2026-09-20 (nove linhas, da que começa em `**O que é.** Todo plano carrega` à
> que termina em `"Modelo de domínio (seção do plano)"`).

```markdown
**O que é.** Todo plano carrega, logo depois de `## 0. O problema, verbatim`, a seção
`## 1. Modelo conceitual`: a descrição, em linguagem corrente, do que o plano entrega, escrita como
**objetos com propriedades** e **operações encadeadas** que alteram essas propriedades. São quatro
blocos, nesta ordem: a tabela de **objetos** (`### 1.1 Objetos`), cada um com as propriedades
observadas, o contrato e a operação que o produz; o **fluxo de operações**
(`### 1.2 Fluxo de operações`), numeradas `OP-<n>`, cada uma nomeando quem age, o que faz, de que
objetos precisa e que propriedades altera; o **estado inicial e o estado final**
(`### 1.3 Estado inicial e estado final`), uma linha por propriedade; e o **registro de versões**
(`### 1.4 Registro de versões`). A gramática que o instrumento lê mora na skill `diario-de-obras`
(*Gramática legível por máquina*, "Modelo de domínio (seção do plano)").
```

> **Bloco P2** — parágrafo **novo**, inserido imediatamente **antes** do parágrafo
> `**O contrato chega ao card.**` (linha 346 em 2026-09-20), separado dele por uma linha em branco.

```markdown
**Objeto, operação e propriedade.** **Propriedade** é a característica **observada** de um objeto:
a que o processo altera, ou a que o processo tem de manter e por isso precisa vigiar. Característica
que não interessa ao dono não é propriedade e não entra no modelo. **Objeto é o que possui
propriedade. Operação não possui propriedade** — operação é o que **altera** a propriedade de um
objeto. Propriedade que aparece numa operação é sinal de operação mal recortada, e a operação
**decompõe-se em um objeto mais uma operação nova**. É assim que objetos e operações se descobrem:
identificam-se as propriedades, e deles caem por decomposição — não por intuição.

**Estado inicial, estado final e o aceite do plano.** O **estado inicial** é o retrato do começo do
plano, antes de ele ser implementado, e serve para **calibrar as tarefas**: tarefa escrita sem
conhecer o que será trabalhado é adivinhação. O **estado final** é o **desejo do dono**, e pode ser
quantificável ou apenas qualificável — há plano cujo estado final é atender a requisitos, não
alcançar um valor. **O aceite do plano é a confrontação dos dois:** o plano só é bem-sucedido se o
estado final real for o estado final especificado, e essa diferença é o que tem valor para o dono.

**Versão vigente, pendente e obsoleta.** A seção `## 1. Modelo conceitual` carrega **sempre o modelo
vigente**, com o número de versão no cabeçalho, monotônico. Emenda ao modelo **versiona, não
reescreve**: a versão nova nasce como **bloco irmão**, declarada pendente de validação, e as duas
coexistem até o marco seguinte. No marco, a validação se busca em **duas instâncias, nesta ordem**:
primeiro o consultor; validando ele, o dono — porque mudar a versão do modelo é mudar a entrega.
Aceita, a pendente passa a vigente e a anterior passa a **obsoleta**; o conteúdo da obsoleta **não
fica no plano**, cuja residência de histórico é o versionador, e o plano guarda só a linha que
registra qual versão ficou obsoleta, quando e por aceite de qual versão. Recusada, a pendente é
**eliminada** e a vigente permanece, sem marca.

**Medição e drift não são a mesma coisa.** **Medição** é o confronto dos **resultados do processo**
contra o modelo; **drift** é a **variação do modelo** em si. À medida que o modelo varia, as
informações originais se perdem ou se modificam, e é por isso que o drift importa. A medição parte
**sempre do modelo vigente** e nunca do obsoleto.
```

> **Bloco P3** — substitui integralmente o parágrafo `**Retroatividade.**`, linhas 370-373 em
> 2026-09-20 (quatro linhas, da que começa em `**Retroatividade.** Plano sem a seção` à que termina
> em `2026-09-20 sobre o Marco 2 do P-0741.`).

```markdown
**Retroatividade.** Plano sem a seção `## 1. Modelo conceitual`, plano com a seção na **forma
anterior** — frases `M-<n>` com estado gravado — e plano com a seção sem
`### 1.3 Estado inicial e estado final` são forma anterior: `modelo.py check` sai `2` para eles e o
loop segue. Nenhum plano é migrado. Caso medido de origem: diretiva do dono de 2026-09-20 sobre o
Marco 2 do `P-0741`.
```

---

## 15. Gramática do terceiro estágio (texto literal para a skill `diario-de-obras`)

Insumo literal da `DOM-T8`, que a transcreve verbatim (`I-3`); **residência depois da transcrição:
`.claude/skills/diario-de-obras/SKILL.md`, subseção `### Modelo de domínio (seção do plano)`**
(`D-51`). Supersede, nas quatro linhas que reescreve, o bloco da §5 — e é a §15 que o preâmbulo
`## Gramática legível por máquina` da skill passa a nomear (`DOM-T8a`, bloco `R5`). Os cinco blocos
abaixo substituem cinco linhas da tabela, e um sexto acrescenta um parágrafo.

> **Bloco G1** — substitui integralmente a linha `| cabeçalho |` da tabela (linha 182 em
> 2026-09-20). **Uma linha só.**

```markdown
| cabeçalho | `**Estado do modelo:** versão <n> · AAAA-MM-DD · autor: <papel> · <k> operações · <p> propriedades · situação: <vigente \| pendente>` | linha única; obrigatória (`V13`); `<n>` monotônico e `situação` é `vigente` na seção `## 1` |
```

> **Bloco G2** — substitui integralmente a linha `| objetos |` da tabela (linha 183 em 2026-09-20).
> **Uma linha só.**

```markdown
| objetos | `### 1.1 Objetos` + tabela `\| objeto \| o que é \| propriedades \| contrato \| origem \|`; `<objeto>` é um nome em linguagem corrente, único na tabela; `<propriedades>` é uma lista separada por vírgula, em linguagem corrente, não vazia; `<origem>` é `externo` ou `OP-<n>` | obrigatória (`V13`); objeto sem propriedade é violação (`V15`); `<origem>` `OP-<n>` existe no fluxo (`V7`); objeto de origem `externo` é citado por alguma operação (`V6`) |
```

> **Bloco G3** — substitui integralmente a linha `| operações |` da tabela (linha 184 em
> 2026-09-20). **Uma linha só.**

```markdown
| operações | `### 1.2 Fluxo de operações`; cada operação é o par de linhas: `- **OP-<n>** — <texto>` e, na linha seguinte, `  - \`precisa de: <objeto>[, <objeto>]\` · \`altera: <objeto>.<propriedade>[, <objeto>.<propriedade>]\` · \`tarefas: <ID>[, <ID>]\`` | numeração `1..k` na ordem do encadeamento, sem salto (`V8`); `<n>` único (`V11`); `<texto>` sem crase e sem `/` (`V12`); todo `<objeto>` existe na tabela de objetos (`V5`); todo par `<objeto>.<propriedade>` de `altera:` existe na tabela de objetos (`V16`); toda `<ID>` existe como `### <ID> — …` no plano (`V3`); lista de tarefas não vazia (`V1`); operação com `<n>` maior que 1 cita ao menos um objeto de origem `OP-<m>` (`V9`), e esse `<m>` é menor que `<n>` (`V10`). Subtítulos `**A. …**` entre operações são livres e ignorados |
```

> **Bloco G4** — substitui integralmente a linha `| mudanças |` da tabela (linha 185 em
> 2026-09-20) por **duas** linhas: o estado e o registro de versões. **Duas linhas.**

```markdown
| estado | `### 1.3 Estado inicial e estado final` + tabela `\| propriedade \| estado inicial \| estado final \|`; a célula `propriedade` é `<objeto>.<propriedade>`; `estado inicial` é o retrato antes da implementação; `estado final` é o desejo do dono, quantificável ou qualificável | obrigatória (`V13`); toda propriedade da tabela de objetos tem exatamente uma linha aqui (`V17`) |
| versões | `### 1.4 Registro de versões` + tabela `\| versão \| data \| situação \| por \|`; `situação` é `vigente`, `pendente` ou `obsoleta`; a linha `obsoleta` registra por aceite de qual versão ela caiu, e o conteúdo dela não fica no plano | obrigatória (`V13`); exatamente uma linha `vigente` (`V19`) |
```

> **Bloco G5** — parágrafo **novo**, inserido imediatamente **antes** do parágrafo
> `**Andamento, nunca gravado.**` (linha 188 em 2026-09-20), separado dele por uma linha em branco.

```markdown
**Versão pendente, como bloco irmão.** Uma versão pós-drift não sobrescreve a vigente: nasce como a
seção `## 1A. Modelo conceitual — versão pendente de validação`, imediatamente depois da `## 1` e
delimitada pelo próximo heading de nível 2, com a mesma estrutura interna de `### 1.1` a `### 1.3` e
o cabeçalho em `situação: pendente`. As duas coexistem até o marco. `modelo.py show` mostra a
**vigente** por omissão, a pendente com `--pendente` e a diferença entre as duas com `--drift`.
Aceita a pendente, ela ocupa a `## 1` e a `## 1A` desaparece; recusada, a `## 1A` é eliminada e a
`## 1` permanece sem marca.
```

---

## 16. Superfície do instrumento no terceiro estágio (normativa; a `DOM-T9` a implementa)

> Insumo normativo da `DOM-T9`; **residência depois da implementação: `.claude/tools/modelo.py`**
> (`D-51`). Supersede a §6 no que reescreve, e é esta seção que o docstring do módulo passa a
> nomear.

**Chamadas** — as duas vigentes, mais dois modificadores de `show`:

```
python .claude/tools/modelo.py check --plano <caminho> [--root <raiz>]
python .claude/tools/modelo.py show  --plano <caminho> [--pendente | --drift] [--root <raiz>]
```

`--pendente` e `--drift` são mutuamente exclusivos; os dois exigem `## 1A` presente e saem `2` com
`modelo: sem versão pendente` quando ela não existe. Sem modificador, `show` imprime a **vigente**,
como hoje.

**Violações novas.** As catorze vigentes (`V1`..`V14`) permanecem com o mesmo código e o mesmo
literal, **inclusive a `V2`** — a `Q-12` (§13.3) está aberta e nada neste estágio a toca. Entram:

| código | condição | substring literal |
|---|---|---|
| `V15` | objeto com a célula `propriedades` vazia | `V15 objeto — objeto sem propriedade <nome>` |
| `V16` | `altera:` cita `<objeto>.<propriedade>` que não está na tabela de objetos | `V16 OP-<n> — propriedade inexistente <nome>` |
| `V17` | propriedade da tabela de objetos sem linha em `### 1.3` | `V17 objeto — propriedade sem estado <nome>` |
| `V18` | operação sem `altera:` ou com `altera:` vazio | `V18 OP-<n> — operação que não altera propriedade` |
| `V19` | `### 1.4 Registro de versões` sem exatamente uma linha `vigente` | `V19 secao — registro de versões sem vigente único` |
| `V20` | `## 1A` presente com versão diferente da vigente mais um | `V20 secao — versão pendente fora de sequência` |

**`V13` muda de literal**, porque a enumeração que ela conta mudou:

| código | condição | substring literal |
|---|---|---|
| `V13` | falta o cabeçalho `**Estado do modelo:**`, ou `### 1.1 Objetos`, ou `### 1.3 Estado inicial e estado final`, ou `### 1.4 Registro de versões` | `V13 secao — cabeçalho, objetos, estado ou registro de versões ausente` |

**Exit codes.** Os quatro vigentes, com um acréscimo na linha de forma anterior:

| condição | exit | stdout / stderr |
|---|---|---|
| seção `## 1. Modelo conceitual` ausente | `2` | `modelo: ausente — plano anterior à doutrina (sem '## 1. Modelo conceitual')` |
| seção presente, `### 1.2 Fluxo de operações` ausente | `2` | `modelo: forma anterior — plano na forma de orações (sem '### 1.2 Fluxo de operações')` |
| seção e fluxo presentes, `### 1.3 Estado inicial e estado final` ausente | `2` | `modelo: forma anterior — plano sem estado inicial e final` |
| zero violações | `0` | `modelo: OK — <k> operações, <o> objetos, <p> propriedades, <t> tarefas, versão <v>` |
| ≥ 1 violação | `1` | stderr: `modelo: FALHOU — <n> violação(ões)` e uma linha por violação |

**Ordem de emissão:** inalterada — `OP-<n>` e `secao` na ordem do arquivo, depois `objeto` na ordem
da tabela, depois `<ID>` na ordem das tarefas.

**Forma de saída de `show --drift`** (fixa):

```
# Drift do modelo — <P-NNNN> — <título do plano>
vigente: versão <a> · <data>   pendente: versão <b> · <data>

## Objetos
[+] <objeto> — <propriedades>
[-] <objeto> — <propriedades>
[~] <objeto> — <propriedades da vigente> => <propriedades da pendente>

## Fluxo
[+] OP-<n> — <texto>
[-] OP-<n> — <texto>
[~] OP-<n> — <texto da vigente> => <texto da pendente>

## Estado final
[~] <objeto>.<propriedade> — <estado final vigente> => <estado final pendente>
```

Os três marcadores têm **três** caracteres com os colchetes: `[+]`, `[-]` e `[~]`. Linha sem
diferença não é impressa. Nenhuma seção com diferença zero é impressa, e `show --drift` sem nenhuma
diferença imprime `sem drift` e sai `0`.

---

## 17. Os ponteiros que a forma nova deixou para trás (texto literal para a `DOM-T8a`)

Insumo literal dos **cinco** blocos que a `DOM-T8a` transcreve (`I-3`); a residência de cada um é o
arquivo que o bloco nomeia (`D-51`). **Esta seção supersede,
nos pontos que nomeia, os literais da §4 deste plano** (linha da matriz de responsabilidades e
tabela de papéis da `### 3.2`) e os blocos `D` e `E` da `DOM-T5`: são os mesmos pontos, escritos
para a forma nova. Nenhum ponto aqui muda **quem faz o quê** — só a forma do que o modelador
devolve (`D-48`).

> **Bloco R1** — substitui integralmente a linha `| **Modelagem** |` da matriz de responsabilidades
> de `GOVERNANCA.md` §3 (linha 95 em 2026-09-20). **Uma linha só.** Muda **um** trecho:
> `a linha de mudança que registra o ato` → `a linha do registro de versões que registra o ato`.
> Todo o resto da linha é byte a byte o que já está publicado — inclusive
> `resolver conflito entre o texto e a entrega`, que **permanece** (o ato `conflito` só sai no
> Marco 4, `D-47`).

```markdown
| **Modelagem** | O mais poderoso disponível (Opus) — escrever o modelo de domínio de um plano é julgamento de domínio, e a consistência entre planos é o que um agente único compra | **Todo** ato sobre o modelo de domínio do plano (§3.2): escrever a seção na autoria, emendá-la quando uma decisão muda o que o plano entrega, resolver conflito entre o texto e a entrega e explicar o contexto do modelo a quem pergunta; devolve a seção literal e a linha do registro de versões que registra o ato (`pantonic-model-designer`) | Não planeja, não executa, não julga entrega e não escreve nenhuma outra linha do plano; não é acionado por outro agente — recebe despacho de quem conduz a sessão |
```

> **Bloco R2** — substitui integralmente a linha `| modelador |` da tabela de papéis de
> `GOVERNANCA.md` `### 3.2` (linha 388 em 2026-09-20). **Uma linha só.**

```markdown
| modelador | escreve a seção inteira, em todo ato; devolve a seção literal e a linha do ato em `### 1.4 Registro de versões` |
```

> **Bloco R3** — substitui integralmente as **quatro** linhas do item `## 1. Modelo conceitual` do
> esqueleto do plano em `.claude/agents/pantonic-planner.md` (linhas 165-168 em 2026-09-20), dentro
> do bloco cercado da Fase 3. A indentação das linhas de continuação é de **34** espaços, como nas
> demais linhas do esqueleto.

```markdown
## 1. Modelo conceitual          (GOVERNANCA.md §3.2 — escrito pelo pantonic-model-designer ANTES
                                  de decompor: objetos com propriedades, fluxo de operações OP-<n>
                                  que as alteram, estado inicial e final, registro de versões;
                                  nada carrega andamento; é o que o dono lê no Marco 1 e dá go/no-go)
```

> **Bloco R4** — substitui integralmente o parágrafo `**O modelo antes das tarefas.**` de
> `.claude/agents/pantonic-planner.md` (linhas 180-191 em 2026-09-20, doze linhas: da que começa
> em `**O modelo antes das tarefas.**` à que termina em `antes da primeira tarefa.`).

```markdown
**O modelo antes das tarefas.** A §1 se escreve antes da §5, e **não é você quem a escreve**:
o dono de todo ato sobre o modelo é o `pantonic-model-designer` (`GOVERNANCA.md` §3.2). Você
devolve, na própria linha de retorno, o dossiê `Ato de modelo` de `autoria` — nenhum agente
aciona outro, e quem conduz a sessão despacha o modelador. A forma está na gramática da skill
`diario-de-obras` ("Modelo de domínio (seção do plano)"): tabela de objetos, cada um com as
propriedades observadas e o contrato que quem implementa precisa; fluxo de operações `OP-<n>`
encadeadas, cada uma nomeando quem age, o que faz, de que objetos precisa e que propriedades
altera; estado inicial e estado final, uma linha por propriedade; e o registro de versões.
**Nenhum elemento da seção carrega andamento** — o andamento é derivado das tarefas e o estágio
atual é a primeira operação não concluída. Só então decompor: cada operação vira ≥ 1 card, e cada
card cita ≥ 1 operação no campo `Operação do modelo`, com o texto copiado e o contrato dos objetos
de que ela precisa. O Marco 1 de todo plano é o dono lendo só a §1 — `go` aprova o plano, `no-go`
o cancela antes da primeira tarefa.
```

> **Bloco R5** — substitui integralmente as **duas** linhas do preâmbulo de
> `## Gramática legível por máquina`, em `.claude/skills/diario-de-obras/SKILL.md`, que nomeiam a
> seção de origem da subseção do modelo (linhas 135-136 em 2026-09-21: da que começa em
> `"Modelo de domínio (seção do plano)" transcreve` à que termina no nome do módulo
> `modelo.py`). **Duas linhas viram duas.** As quatro linhas anteriores do mesmo preâmbulo, que
> falam do `P-0739` e do `backlog.py`, **não se tocam**.

```markdown
"Modelo de domínio (seção do plano)" transcreve `docs/plans/P-0743-modelo-de-dominio.md` §5 e §15 —
onde as duas divergem, governa a §15 — e é lida por `.claude/tools/modelo.py`.
```

---

## 18. O modelador na forma nova (texto literal para a `DOM-T9a`)

Residência única dos seis literais que a `DOM-T9a` transcreve (`I-3`). Todos moram em
`.claude/agents/pantonic-model-designer.md`, entregue pela `DOM-T4`. **Nenhum bloco aqui remove
ato, cria ato ou move responsabilidade**: o ato `conflito` continua existindo e continua sendo do
modelador até o Marco 4 (`D-47`, `D-48`, `D-49`). O que muda é **o que ele devolve**, que a §14 e a
§15 já redefiniram.

> **Bloco S1** — substitui integralmente o bullet da norma em `## Fatos estáveis` (linhas 15-17 em
> 2026-09-20). **Três linhas.** Muda **uma** palavra: `três blocos` → `quatro blocos`, porque o
> bloco P1 da §14 enumera quatro (`I-4`).

```markdown
- A norma do modelo de domínio — o que a seção é, os quatro blocos que a compõem, o estágio derivado
  e nunca gravado, e quem escreve o quê — mora em `GOVERNANCA.md` §3.2. Leia-a antes de agir; este
  corpo não a recopia (`D-9`).
```

> **Bloco S2** — substitui integralmente o **item 1** de `## O ensinamento` (linhas 28-30 em
> 2026-09-20). **Três linhas viram seis.** Razão: o item vigente manda começar pelos objetos, e o
> bloco P2 da §14, já publicado pela `DOM-T7`, manda o contrário — *"identificam-se as
> propriedades, e deles caem por decomposição"*. São duas fontes do mesmo fato, e uma é falsa.

```markdown
1. Comece pelas **propriedades** — a característica **observada** de um objeto: a que o processo
   altera, ou a que ele tem de manter e por isso vigia. **Objeto é o que possui propriedade;
   operação é o que a altera e não possui nenhuma.** Das propriedades caem, por decomposição, os
   objetos da tabela `### 1.1 Objetos` e as operações do fluxo — não por intuição. Cada objeto
   recebe, além das propriedades, o **contrato** que quem implementa precisa: o suficiente para
   que um executor frio, lendo só o card, saiba o que tem nas mãos sem abrir o plano inteiro.
```

> **Bloco S3** — substitui integralmente o bullet **Autoria** de `## Os quatro atos` (linhas 42-44
> em 2026-09-20). **Três linhas.**

```markdown
- **Autoria** — recebe o plano gravado sem a seção do modelo, no dossiê do planejador (`Ato:
  autoria`). Devolve a seção `## 1. Modelo conceitual` inteira, escrita pela primeira vez, e a
  linha da **versão 1** em `### 1.4 Registro de versões`, com a situação `vigente`.
```

> **Bloco S4** — substitui integralmente o bullet **Emenda** (linhas 45-48 em 2026-09-20).
> **Quatro linhas viram sete.** O acréscimo é a mecânica do bloco irmão, que o parágrafo
> `**Versão vigente, pendente e obsoleta.**` da §14 já publicou em `GOVERNANCA.md` §3.2 e que o
> bloco `G5` da §15 grava na gramática: emenda **versiona, não reescreve**.

```markdown
- **Emenda** — recebe uma decisão que muda o que o plano entrega, no dossiê de quem a tomou (`Ato:
  emenda`, com o identificador da decisão em `Motivo`). **Versiona, não reescreve.** Devolve a
  versão nova como **bloco irmão** — a seção `## 1A. Modelo conceitual — versão pendente de
  validação`, com o trecho afetado reescrito, o cabeçalho em `situação: pendente` e as `OP-<n>`
  que a decisão toca — e a linha da versão nova em `### 1.4 Registro de versões`, com a situação
  `pendente` e, na célula `por`, o papel e o identificador da decisão. A `## 1` vigente **não se
  toca**: quem decide entre as duas é o marco, nunca você.
```

> **Bloco S5** — substitui integralmente os bullets **Conflito** e **Leitura** (linhas 49-55 em
> 2026-09-20). **Sete linhas.** O ato `conflito` **permanece**, com o mesmo dono e a mesma entrada;
> muda só a forma do que ele devolve, pela mesma razão do bloco S4 — toda mudança do modelo
> versiona.

```markdown
- **Conflito** — recebe um achado de divergência entre o texto de uma operação e o que a entrega
  materializou de fato, no dossiê de quem o encontrou (`Ato: conflito`, com o identificador do
  achado em `Motivo`). Devolve a correção **na mesma forma da emenda** — bloco irmão pendente e
  linha da versão nova, com a situação `pendente`, no registro de versões.
- **Leitura** — recebe um pedido de contexto sobre o modelo (`Ato: leitura`), sem que nada no
  repositório precise mudar. Devolve a explicação pedida a partir do estado real da seção; se
  nada no modelo muda, nenhuma linha de versão é gerada.
```

> **Bloco S6** — substitui integralmente a seção `## A forma da devolução` inteira, do heading à
> linha que começa em `Nenhuma prosa fora da seção` (linhas 69-77 em 2026-09-20). **Nove linhas
> viram onze.**

```markdown
## A forma da devolução

Todo ato devolve exatamente duas coisas, e nada além delas:

1. A seção **inteira e literal** — a `## 1. Modelo conceitual` na autoria; a
   `## 1A. Modelo conceitual — versão pendente de validação` em todo ato que versiona. Não um
   trecho, não um resumo do que mudou.
2. A linha da versão do ato, registrada em `### 1.4 Registro de versões` dentro da própria seção,
   com a situação que o ato produz.

Nenhuma prosa fora da seção, nenhum comentário sobre a qualidade do plano, nenhuma recomendação.
```

## 19. O gate do modelador, qualificado (texto literal para a `DOM-T9b`)

Insumo literal da `DOM-T9b`, que o transcreve verbatim (`I-3`); **residência depois da transcrição:
`.claude/agents/pantonic-model-designer.md`** (`D-51`). Supersede o quarto bullet de
`## Fatos estáveis`, que a `DOM-T4` publicou e a `DOM-T9a` não tocou.

> **Superada pela §20** (`ESC-10`, 2026-09-21, `AE-22`). O bloco abaixo **afirma uma fronteira que
> o instrumento não emite**: ele nomeia dois tokens de índice, e `modelo.py` emite **quatro** — o
> que falta é `objeto` (`V6`, `V7`, `V15`, `V17`), família da seção que o modelador escreve. O
> bloco **não se reescreve**: é o registro do que a `DOM-T9b` transcreveu, e o aceite dela se
> confere contra ele. Onde as duas divergem, **governa a §20** (`D-51`).

> **Bloco T1** — substitui integralmente o bullet do gate em `## Fatos estáveis` (linhas 22-24 em
> 2026-09-21: da que começa em `- Todo ato termina com` à que termina em
> `escreveu e rode de novo antes de devolver.`). **Três linhas viram oito.** Os três outros bullets
> da seção **não se tocam**.

```markdown
- Todo ato termina com `python .claude/tools/modelo.py check --plano <plano>`. Com exit `0`, você
  devolve. Exit `1` cujas violações sejam da **seção** — as que o instrumento indexa por `OP-<n>` ou
  por `secao` — é ato não concluído: corrija a seção que você mesmo escreveu e rode de novo antes de
  devolver. Violação indexada pelo **`<ID>` de uma tarefa** (`V2`, `V4`, `V14`) **não é sua**: ela
  mora no card, e card não é linha que você escreve. Nesse caso devolva o ato com a **saída literal**
  do `check`, nomeando as violações que ficaram — quem conduz a sessão as roteia para a tarefa que
  converte os cards. Exit `2` é plano ainda na forma anterior: se o seu ato é justamente trazê-lo
  para a forma nova, ele deixa de sair `2` no instante em que você grava a seção.
```

## 20. O gate do modelador, pela fronteira medida (texto literal para a `DOM-T9c`)

Insumo literal da `DOM-T9c`, que o transcreve verbatim (`I-3`); **residência depois da transcrição:
`.claude/agents/pantonic-model-designer.md`** (`D-51`). Supersede o bloco `T1` da §19.

**A fronteira, medida pelo caminho do usuário em 2026-09-21** — `modelo.py check --plano` sobre
`tests/fixtures/modelo/plano-invalido.md` e sobre uma cópia adulterada de `fluxo-valido.md` em
`%TEMP%`, nunca na árvore viva. Quatro tokens de índice, vinte violações:

| token | violações | onde mora |
|---|---|---|
| `secao` | `V13`, `V19`, `V20` | seção — **do modelador** |
| `OP-<n>` | `V1`, `V3`, `V5`, `V8`, `V9`, `V10`, `V11`, `V12`, `V16`, `V18` | seção — **do modelador** |
| `objeto` | `V6`, `V7`, `V15`, `V17` | seção (`### 1.1` e `### 1.3`) — **do modelador** |
| `<ID>` de tarefa | `V2`, `V4`, `V14` | card — **não é do modelador** |

Saídas literais medidas: `V6 objeto — objeto externo sem uso <nome>`,
`V7 objeto — origem inexistente <nome>`, `V15 objeto — objeto sem propriedade <nome>`,
`V17 objeto — propriedade sem estado <nome>`. **`V15` e `V17` são as faltas mais prováveis de uma
autoria**, que é exatamente o ato que a `DOM-T10` despacha.

**Por isso o bloco abaixo define o ramo por complemento, não por enumeração:** é o que sobrevive à
chegada de uma quinta família.

> **Bloco T2** — substitui integralmente o bullet do gate em `## Fatos estáveis` de
> `.claude/agents/pantonic-model-designer.md` — o bullet que a `DOM-T9b` publicou, hoje com **oito**
> linhas, da que começa em `- Todo ato termina com` à que termina em
> `no instante em que você grava a seção.` Os três outros bullets da seção **não se tocam**.

```markdown
- Todo ato termina com `python .claude/tools/modelo.py check --plano <plano>`. Com exit `0`, você
  devolve. Exit `1` é ato não concluído **sempre que ao menos uma violação for da seção** — e é da
  seção **toda** violação que o instrumento não indexa pelo `<ID>` de uma tarefa: as de `secao`, as
  de `OP-<n>` e as de `objeto`, estas últimas vindas de `### 1.1 Objetos` e de
  `### 1.3 Estado inicial e estado final` (`V6`, `V7`, `V15`, `V17`). Corrija a seção que você mesmo
  escreveu e rode de novo antes de devolver. Só três violações **não são suas**, e são as indexadas
  pelo `<ID>` de uma tarefa: `V2`, `V4` e `V14` — elas moram no card, e card não é linha que você
  escreve. Havendo **apenas** essas, devolva o ato com a **saída literal** do `check`, nomeando as
  violações que ficaram: quem conduz a sessão as roteia para a tarefa que converte os cards. Exit
  `2` é plano ainda na forma anterior: se o seu ato é justamente trazê-lo para a forma nova, ele
  deixa de sair `2` no instante em que você grava a seção.
```

---

## Achados da execução

### AE-1 — literal de aceite publicado quebrado no bloco cercado da §4 (`DOM-T1`, `B0`)

**Fato medido.** A `Verificação` 4 da `DOM-T1` exige o literal contíguo
`O reviewer não escreve fora do caminho do laudo` numa linha só, mas o bloco cercado da §4 deste
plano publica a frase **quebrada em duas** (linhas 321-322). Com a transcrição verbatim que a `I-3`
manda, o aceite era inalcançável: `grep -c` sem multiline nunca casaria. O executor reempacotou o
ponto de soft-wrap — sem alterar palavra, pontuação ou ordem — e o reviewer conferiu a fidelidade
palavra por palavra contra a §4 e marcou `criterio-de-pronto` e `escopo` como conformes
(`aprovado 100%`, bloqueante `nenhuma`).

**Atribuição (`B0`, medida por `review_evidence.py --atribuir`).** O defeito está em
`docs/plans/P-0743-modelo-de-dominio.md` §4 — arquivo **fora** dos `Arquivos-alvo` da `DOM-T1`.
Não é pendência da tarefa: a entrega não é rebaixada e o laudo não se refaz.

**Rota.** Item de replanejamento deste plano: republicar o bloco cercado da §4 já na quebra de
linha que o arquivo-alvo carrega, para que literal de aceite e texto normativo coincidam. O
reviewer varreu os demais literais de aceite do plano e **nenhum outro atravessa quebra de linha**,
então o achado não bloqueia `DOM-T2`..`DOM-T6`.

**Lição para quem planeja.** Literal que vai virar alvo de `grep` no card tem de ser publicado no
plano com a mesma quebra de linha do arquivo de destino; do contrário a restrição verbatim e a
verificação se contradizem, e a contradição cai no executor como decisão — que é o que o `G-NOASK`
proíbe.

### AE-2 — o renome da subseção deixou órfão o preâmbulo que a nomeia (`DOM-T2`, rota corrigida para a `DOM-T3a`)

**Fato medido.** A `DOM-T2` renomeou `### Modelo conceitual (seção do plano)` para
`### Modelo de domínio (seção do plano)` em `.claude/skills/diario-de-obras/SKILL.md`, e o card
**confinou** a edição a esse recorte. O preâmbulo da mesma seção `## Gramática legível por máquina`
(`SKILL.md:133-136`) continua dizendo que a subseção `Modelo conceitual (seção do plano)`
transcreve a §5 de `docs/plans/P-0741-modelo-conceitual.md` — **nome que não existe mais no arquivo
e plano de origem errado**: a residência passou a ser a §5 do `P-0743`.

**Atribuição.** Defeito de **autoria do card**, não da execução: o executor obedeceu o recorte e a
entrega não é rebaixada (rubrica §6, invariante 1; critério (viii) da §8). A `DOM-T2` fechou
`aprovado 100%`, bloqueante `nenhuma`.

**Rota — corrigida no `ESC-1` (consultor de plano, 2026-09-20).** A rota original dizia que a
`DOM-T6` alcançava o preâmbulo. **Não alcança, e a verificação é direta:** os `Arquivos-alvo` da
`DOM-T6` são só `README.md`, o `Não fazer` dela proíbe tocar `.claude/README.md` e planos, e
nenhum passo, nenhuma verificação e nenhuma linha do `Pronto quando` dela nomeia
`.claude/skills/diario-de-obras/SKILL.md`. A crença de que a skill estava "no raio da revisão da
porta de entrada" era leitura do título do card, não do card. Era, portanto, a **mesma classe**
do `AE-5`: resíduo sem card que o cubra. Rota nova: **`DOM-T3a`**, card corretivo criado neste
escalonamento (`D-16`), que tem `SKILL.md` inteiro nos `Arquivos-alvo`, publica o literal das
três linhas e fecha com os greps `P-0741` → `0` e `P-0743` → `1` ou mais no arquivo.

**Lição para quem planeja.** Renomear é sempre tarefa de **duas pontas**: card que renomeia um
objeto e confina a edição ao recorte do objeto deixa, por construção, toda referência externa
apontando para o vazio. O invariante `I-4` já obriga fechar as frases que **contam** um conjunto
alterado; falta a ele a contraparte para as frases que **nomeiam** o que foi renomeado — que é o
que o `I-10` passou a cobrir. E uma segunda, do próprio registro deste achado: **rota de achado
que aponta para um card existente só vale depois de conferir os `Arquivos-alvo` e o
`Pronto quando` daquele card**, nunca pelo título dele.

### AE-3 — o atribuidor fabrica autoria falsa com tarefa nunca despachada (`DOM-T2`, sai do plano)

**Fato medido.** `review_evidence.py --atribuir` rotulou **quatorze** arquivos como
`alvo-de-outra-tarefa (DOM-T3)`, `(DOM-T4)`, `(DOM-T5)` — tarefas **em `ready`, nunca despachadas**,
que não produziram nada. Os arquivos são entrega da janela paralela do `P-0741`. O atribuidor casa
caminho contra os `Arquivos-alvo` de **qualquer** tarefa do plano **sem olhar o status dela**, e
assim fabrica autoria exatamente no regime de **commit por marco** (diretiva do `P-0740`, item 3)
em que a atribuição é o que separa uma entrega da outra. Nas duas revisões desta janela a
**injeção manual do despacho teve de desmentir a própria evidência mecânica**.

**Rota.** Matéria de **instrumento**, cruza o tema deste plano e por isso fica fora dele (`DM-4` do
`P-0740`): tíquete `TK-66` no `docs/DIARIO_DE_OBRAS.md`. Candidatos de correção já nomeados pelo
laudo: filtrar a atribuição por tarefas em `in-progress`/`review`/`done`, ou criar a categoria
própria `alvo de tarefa não despachada`.

### AE-4 — contradição viva entre residências durante a janela de transição (`DOM-T2`, rota na `DOM-T5`)

**Fato medido.** Desde que a `DOM-T1` fechou, `GOVERNANCA.md` §3.2 e `docs/RUBRICA_DE_REVISAO.md`
§7 dizem que o revisor **não escreve** no modelo do plano, enquanto a **definição do papel**
(`.claude/agents/pantonic-reviewer.md`) ainda o instrui a *confirmar e emendar* a seção
`## 1. Modelo conceitual` como sua única escrita fora do laudo. As duas residências se contradizem
enquanto a `DOM-T5` não fecha.

**Como foi resolvido no ato.** O revisor da `DOM-T2` fez prevalecer a **norma do repositório** e
**nada escreveu** no modelo do `P-0743`. É a conduta correta e fica como precedente para as
revisões das tarefas `DOM-T3` e `DOM-T4`, que rodam dentro da mesma janela de contradição.

**Rota.** `DOM-T5` (*Os papéis diante do modelador*), já no plano. Sem card novo. Este é o custo
previsto da ordem de execução da §10 — a norma sai antes das definições de conduta —, e não um
defeito de rota.

### AE-5 — resíduo de forma anterior no que o módulo diz de si mesmo (`DOM-T3`, reparado pela `DOM-T3a`)

**Fato medido.** Os `Arquivos-alvo` da `DOM-T3` recortam `.claude/tools/modelo.py` em **quatro
faixas de linhas** (53, 74, 87, 268). As faixas **excluem** o docstring do módulo (linhas 1-14) e a
`description` do `argparse` em `main()` — **ambos texto da forma anterior**, que sobreviveu à
reescrita. O `Pronto quando` do card não traz aceite de **coerência do módulo** (rubrica §8,
critério (iv); `DM-3`) que os alcançasse. O executor corrigiu o docstring de `tests/test_modelo.py`
para a forma nova e deixou o de `.claude/tools/modelo.py` e o `--help` na anterior.

**Por que não bloqueou.** Dimensão `residuo` marcada `parcial`, bloqueante `nenhuma`, veredito
`ressalva 88%`, recomendação `seguir com ressalva`. O instrumento **funciona**: 249 testes verdes,
os quatro exits e os quatorze literais exatos.

**Por que não há onde cair.** **Nenhum card seguinte cobre isto**: a `DOM-T4` cria o agente, a
`DOM-T5` mexe nas definições de conduta e a `DOM-T6` tem no raio o `README.md` e a porta de
entrada — não o interior de `modelo.py`. Sem reparo, o plano fecha com o instrumento dizendo de si
mesmo o que ele deixou de ser.

**Rota — decidida no `ESC-1` (consultor de plano, 2026-09-20; `D-16`).** Card corretivo próprio,
a **`DOM-T3a`**, despachada logo depois da `DOM-T3` e **antes** da `DOM-T4`. Ampliar a `DOM-T6`
foi considerado e rejeitado: misturaria documentação pública com interior de instrumento e de
skill, quebraria o `Fora do escopo` dela e adiaria para o fim do plano um defeito que a `DOM-T4`
e a `DOM-T5` leem enquanto trabalham. A `DOM-T3a` absorve também o `AE-2`, que é a mesma classe
no outro arquivo.

**Lição para quem planeja.** Recorte por faixa de linhas dentro de um arquivo-alvo **orienta bem a
edição e cega a revisão de coerência do arquivo inteiro**. Card que reescreve a semântica de um
módulo precisa de um aceite que alcance o módulo todo — docstring, `--help`, mensagens —, não só as
faixas editadas.

### AE-6 — contingência que cria arquivo não o declara nos alvos nem exige declaração (`DOM-T3`)

**Fato medido.** A contingência 2 da `DOM-T3` autoriza criar
`tests/fixtures/modelo/plano-invalido-2.md`, mas **não o inclui nos `Arquivos-alvo`** e **não manda
declarar a ativação** na linha de retorno. Consequência medida: o executor acionou a contingência
(as quatorze violações não cabiam numa fixture só), **não declarou**, e o dossiê de evidência saiu
com veredito mecânico de escopo `aberto`, com o arquivo listado como fora dos alvos e
`sem-atribuicao`. O revisor teve de reconstruir a autoria à mão.

**Rota — aplicada no `ESC-1` (consultor de plano, 2026-09-20).** Virou a decisão `D-17` e a
primeira metade do invariante `I-10`: **toda contingência que cria arquivo declara esse arquivo
nos `Arquivos-alvo` e exige a declaração da ativação na linha de retorno**. Aplicado aos quatro
cards restantes (`DOM-T3a`, `DOM-T4`, `DOM-T5`, `DOM-T6`). **Medido na varredura do `ESC-1`:**
nenhuma das sete contingências restantes cria arquivo — a única criação declarada é
`.claude/agents/pantonic-model-designer.md`, que já está nos `Arquivos-alvo` da `DOM-T4`. Por
isso a aplicação tomou a forma de uma cláusula de parada em cada card: contingência que só possa
ser cumprida criando arquivo não declarado significa card incompleto, e o executor sinaliza
`blocked` razão `premissa` em vez de criar. Sobe como matéria de doutrina de autoria de card.

### AE-7 — a §6 conta dez onde os próprios literais dela têm nove (`DOM-T3`)

**Fato medido.** A §6 do plano afirma que os três rótulos de andamento têm *"largura fixa de dez
caracteres entre colchetes"*, mas os três literais normativos publicados na **mesma seção** —
`[concluída]`, `[em curso ]`, `[prevista ]` — têm **nove** caracteres entre colchetes e onze com
eles. E é o **nove** que casa com a indentação de doze espaços da linha `precisa de:`.

**Como foi resolvido.** A entrega seguiu **os literais**, que são a norma; a prosa é que está
falsa. O `show` está correto.

**Rota — executada no `ESC-1` (consultor de plano, 2026-09-20).** A §6 deste plano foi emendada:
a frase passou a dizer **nove** caracteres entre colchetes, onze com os colchetes, e a explicitar
que são os doze espaços da linha `precisa de:` que alinham o texto dela sob o texto da operação.
Os três literais normativos não mudaram — eram eles que estavam certos —, e a entrega da
`DOM-T3` não é tocada nem rebaixada. Nenhum card novo.

### ESC-1 — escalonamento ao consultor de plano (2026-09-20)

**O que motivou.** A revisão da `DOM-T3` (`ressalva 88%`, bloqueante `nenhuma`) produziu três
achados de **autoria de plano** — `AE-5`, `AE-6`, `AE-7` — dos quais um, o `AE-5`, não tinha card
que o cobrisse até o fim do plano. O loop não revisa plano; o reparo é do consultor.

**O que foi reparado.** §6 (emenda do `AE-7`); `## 1. Modelo conceitual` (cabeçalho do estado,
`tarefas:` de `M-1`, `M-5`, `M-6`, `M-7`, e a linha `MD-1`); §3 (decisões `D-16` e `D-17`); §8
(invariante `I-10`); card novo `DOM-T3a`; cards `DOM-T4`, `DOM-T5` e `DOM-T6` (cláusula do
`I-10`, aceites de coerência de arquivo inteiro, e a âncora defasada `README.md:816` → 819); §10
(fila e as duas razões de dependência); achados `AE-2`, `AE-5`, `AE-6` e `AE-7`.

**Classificação.** `tatico`: nenhum dos quatro achados muda escopo, rota ou contrato do plano, e
nenhum toca as decisões `D-1`..`D-15` nem o Marco 1. Nada foi ao dono.

**O que fica inconclusivo.** (i) O `AE-3` continua fora deste plano, no tíquete `TK-66`: enquanto
`review_evidence.py --atribuir` casar caminho contra tarefa nunca despachada, a evidência
mecânica da `DOM-T3a`, da `DOM-T4` e da `DOM-T5` seguirá exigindo injeção manual de despacho, e
isso não é defeito da entrega. (ii) A `DOM-T5` toca `.claude/agents/pantonic-consultant.md`, que
é a definição deste papel; a conferência de que a cláusula nova não contradiz a conduta em uso
cabe à revisão daquela tarefa, não a este ato. (iii) O `I-10` é invariante **deste** plano; a
promoção dele a doutrina de autoria de card (`GOVERNANCA.md` ou a definição do planejador) é
matéria do dono e não foi feita aqui.

### AE-8 — o aceite por grep de resíduo é cego à fidelidade do literal (`DOM-T3a`)

**Fato medido.** A `DOM-T3a` passou em **11/11** dos greps de aceite e ainda assim entregou o
docstring **divergente** do bloco literal do card: ele diz `(I-3 do P-0743)` onde o card manda
`(I-1 do P-0743)`. O valor é **herdado do docstring substituído**, que citava `I-3` do `P-0741` —
um token do texto antigo sobreviveu à troca do bloco inteiro.

**Por que nenhum grep viu.** Os onze comandos de aceite são todos **contagens de ocorrência de
resíduo da forma anterior**. O token sobrevivente não é resíduo de forma: é **referência cruzada
errada**, e nenhuma contagem de resíduo a alcança. Veredito `ressalva 94%`, dimensão `rota`
`parcial`, bloqueante `nenhuma`.

**Consequência.** O docstring publicado de `.claude/tools/modelo.py` aponta o leitor para o
invariante errado do plano — diz `I-3` (transcrição verbatim) onde queria dizer `I-1` (proibição de
editar `backlog.py`), que é justamente o invariante que a frase está explicando.

**Rota — decidida no `ESC-2` (consultor de plano, 2026-09-20; `D-18`).** Card corretivo próprio,
a **`DOM-T3b`**, `esforço low`, despachada logo depois da `DOM-T3a` e antes da `DOM-T4`. Ela
republica o docstring inteiro como bloco cercado, nomeia a única linha divergente e fecha por
**confronto do bloco entregue contra o bloco do card** (`I-11`), não por contagem de resíduo.
Pendurar a correção num card restante foi considerado e rejeitado: nenhum deles toca
`.claude/tools/modelo.py`, e pendurar assunto alheio num card é como o `AE-2` nasceu.

**Lição para quem planeja — vale para todo card de transcrição verbatim.** Aceite por grep de
resíduo **não discrimina fidelidade**. Card que manda transcrever verbatim precisa de uma linha de
`Verificação` que **confronte o bloco entregue contra o bloco cercado do card** — não contagens do
que deveria ter sumido. Matéria do critério (xii)(a) da `docs/RUBRICA_DE_REVISAO.md` §8.
**Aplicada no `ESC-2`** como invariante `I-11`, com linha de `Verificação` e declaração
`fidelidade conferida:` acrescentadas à `DOM-T3b`, à `DOM-T4`, à `DOM-T5` e à `DOM-T6` — os
quatro cards restantes que mandam transcrever.

### AE-9 — `review_evidence.py` lê prosa de `Arquivos-alvo` como caminho (`DOM-T3a`)

**Fato medido.** Os `Arquivos-alvo` deste plano trazem prosa e símbolo no meio dos caminhos (ex.:
`o argumento description=(...) do argparse.ArgumentParser dentro de main()`). O
`review_evidence.py` leu `argparse.ArgumentParser` **como caminho de arquivo** e emitiu
`sem diferença coletável — arquivo ausente na árvore de trabalho`, além de **6 literais** não
reconhecidos como caminho.

**Rota — duas pontas, decididas no `ESC-2` (consultor de plano, 2026-09-20).** (a) O conserto do
**instrumento** fica no `TK-66`, já aberto, junto do defeito do atribuidor (`AE-3`); não abre
tíquete novo. (b) O conserto da **forma do plano** é ato deste escalonamento e não espera o
tíquete: decisão `D-19` e invariante `I-12` — `Arquivos-alvo` passa a ser **um caminho puro por
bullet**, sem prosa nem símbolo na mesma linha, com a qualificação em sub-bullet. Reescritos
nessa forma os `Arquivos-alvo` da `DOM-T3b`, da `DOM-T4`, da `DOM-T5` e da `DOM-T6`. A `DOM-T3a`
fica como está: já fechou, e reescrever card fechado falsifica o registro do que foi despachado.

### ESC-2 — segundo escalonamento ao consultor de plano (2026-09-20)

**O que motivou.** O `AE-8`: a `DOM-T3a` fechou `ressalva 94%` com 11/11 greps verdes e um token
divergente do bloco literal do card. Um token não tem card que o abrigue — a mesma ausência que
produziu o `AE-5`.

**O que foi reparado.** Card novo `DOM-T3b`; decisões `D-18` e `D-19`; invariantes `I-11`
(fidelidade de transcrição) e `I-12` (forma dos `Arquivos-alvo`); `Arquivos-alvo` da `DOM-T4`,
`DOM-T5` e `DOM-T6` reescritos em caminho puro + sub-bullet; linha de fidelidade acrescentada à
`Verificação` dos quatro cards restantes; cabeçalho (8 tarefas, fila) e §10; achados `AE-8` e
`AE-9`.

**O que a varredura do item 3 encontrou, além do pedido.** A edição da `DOM-T5` no
`scrum-master` estava errada em três pontos, todos medidos: (i) o bloco literal mandava *"siga
para o passo 9"* estando ancorado no **passo 6**, saltando os passos 7 e 8 — referência cruzada
errada dentro do próprio literal, exatamente a classe do `AE-8`; (ii) a "frase da linha 113"
não cabe numa linha: vai de 111 a 116; (iii) `grep -n 'V6'` imprime **duas** linhas, 113 e
**188**, e a segunda está no passo 9, que a contingência 2 do card **excluía** — deixando viva
a fundamentação do gate do modelo que afirma que *"o reviewer acabou de gravar confirmação ou
emenda"* (linhas 184-185), afirmação que morre com `D-8`. A edição virou **três** blocos
literais ancorados por conteúdo — passo 6, passo 8 (onde o despacho do modelador de fato cabe,
porque a `Saída` do passo 8 é que leva ao passo 9) e passo 9 —, com a chamada e os três exits
do gate preservados byte a byte. A fundamentação do bloco C também corrigiu um fato: sob `D-2`,
`review` e `in-progress` deixam a operação **igualmente** `em curso`, então o texto anterior,
que justificava segurar a tarefa em `review` para não criar vermelho, deixou de ser verdadeiro.

**Classificação.** `tatico`: nada muda escopo, rota ou contrato do plano; `D-1`..`D-15` e o
Marco 1 seguem intocados. Nada foi ao dono.

**O que fica inconclusivo.** (i) `AE-3` e `AE-9` continuam no `TK-66`: a evidência mecânica dos
cards restantes vai seguir exigindo injeção manual de despacho, e isso não é defeito de entrega.
(ii) `I-11` e `I-12` são invariantes **deste** plano; a promoção deles à rubrica §8 e à doutrina
de autoria de card é matéria do dono. (iii) **`card_check.py` reprova o bloco `Verificação` de
todos os oito cards deste plano**, inclusive os quatro já aprovados: ele exige a forma numerada
da rubrica §8.1 e o plano inteiro usa blocos cercados soltos. Defeito pré-existente de forma,
não introduzido por nenhum escalonamento; escrevi `DOM-T3a` e `DOM-T3b` na forma prevalecente
em vez de divergir em dois cards. Se o dono quiser o `card_check` como gate deste plano, é
reescrita dos oito blocos e precisa de decisão dele. (iv) A `DOM-T5` toca
`.claude/agents/pantonic-consultant.md`, definição deste papel: a conferência cabe à revisão
daquela tarefa, não a este ato.

### AE-10 — a `Verificação` da `DOM-T5` alcança um ponto que os `Passos` dela não citam (`DOM-T5`, `A3b`)

**Fato medido.** A `Verificação` da `DOM-T5` exige
`grep -c 'Oração do modelo' .claude/agents/pantonic-planner.md` → `0`. Hoje o arquivo tem **duas**
ocorrências, nas linhas **184** e **363**. Os `Passos` do card nomeiam **três** pontos do planner —
o esqueleto do plano na Fase 3, o item `4a` (linha **229**) e a anatomia do card (linha **363**) —
e **nenhum deles é a linha 184**.

A 184 mora num **quarto trecho**, o parágrafo `**O modelo antes das tarefas.**` (linhas **179-186**),
que o card não cita em passo nenhum. E o parágrafo não é de correção mecânica: ele descreve a forma
antiga inteira — nomeia a subseção superada `Modelo conceitual (seção do plano)` e manda *"cada
oração com `estado: prevista`"*, que a §5 deste plano **proíbe** (`Andamento, nunca gravado. Nenhum
elemento da seção carrega estado`). Reescrevê-lo sem contradizer a §5 exige **redigir conteúdo
novo** — a gramática de `OP-<n>`, dos objetos e das mudanças — que **nenhum bloco literal do card
fornece**.

**Conduta do executor: correta.** Escrever esse conteúdo seria decidir redação de doutrina no meio
da execução, que é o que a Regra 8 e o `G-NOASK` proíbem. Ele parou, devolveu `blocked` razão
`premissa` e **deixou `pantonic-planner.md`, `pantonic-consultant.md` e
`.claude/skills/scrum-master/SKILL.md` intocados**. Os quatro blocos literais de
`.claude/agents/pantonic-reviewer.md` (linhas 5, 47, 100, 140) **já foram aplicados** e estão na
árvore.

**Erro de despacho, assumido pela orquestração.** O despacho re-derivou a linha 184 como *"o item
`4a` da Fase 4"*. Está errado: o `4a` é a linha **229**. O executor apanhou o erro em vez de
executar sobre ele.

**Rota — decidida no `ESC-3` (consultor de plano, 2026-09-20; `D-20`).** Sem card novo: a
`DOM-T5` ganhou **seis** blocos literais que não tinha — `D` (esqueleto da Fase 3, 165-167),
`E` (o parágrafo `O modelo antes das tarefas`, 179-186, que é o furo do `AE-10`), `F` (item
`4a`, 229), `G` (anatomia do card, 363), `H` (`description` do consultor, 3) e `I` (item 3 do
consultor, 38-40) — e os `Passos` deixaram de descrever mudanças em prosa: cada passo agora
aponta um bloco. Opção (b), recortar a `Verificação` para os três pontos, foi **rejeitada**: o
que sobraria é precisamente a contradição com a §5 que o executor apanhou, publicada e sem
dono. Rota original preservada abaixo para registro.

**Rota original (superada).** Escalonamento `ESC-3` ao consultor de plano: ou o card ganha um quarto bloco literal para
o parágrafo `O modelo antes das tarefas`, ou a `Verificação` recorta o alvo para os três pontos que
os `Passos` alcançam e o quarto vira card próprio. Decisão é dele.

**Lição para quem planeja.** `Verificação` que mede o **arquivo inteiro** (`I-10`) e `Passos` que
enumeram **pontos** só fecham quando alguém confere que os pontos cobrem o que a medida alcança.
Aqui o `I-10` e a lista de passos divergiram, e a divergência só apareceu na execução.

### ESC-3 — terceiro escalonamento ao consultor de plano (2026-09-20)

**O que motivou.** A `DOM-T5` voltou `blocked` razão `premissa`: o `AE-10`. A `Verificação`
media o arquivo inteiro (`I-10`) e os `Passos` enumeravam três pontos do planejador; o quarto —
o parágrafo `**O modelo antes das tarefas.**`, linhas 179-186 — não estava citado, prescrevia
`estado: prevista` (que a §5 deste plano **proíbe**) e não tinha bloco literal. O executor parou
em vez de redigir doutrina, e deixou planejador, consultor e `scrum-master` intocados.

**O que foi reparado.** `DOM-T5`: seis blocos literais novos (`D`..`I`), `Passos` reescritos de
prosa para transcrição (11 passos), `Arquivos-alvo` com os quatro pontos do planejador e os dois
do consultor medidos, `.claude/README.md` acrescentado com passo de regeneração por instrumento,
quatro aceites novos, contingências 3 e 4, e nota de `I-5` sobre o estado parcial na árvore.
Bloco C corrigido de 182-190 para **183-192**. `DOM-T6`: passo 3 deixou de mandar reescrever em
prosa e passou a trazer a medição. Decisão `D-20` e invariante `I-13`.

**O que a varredura encontrou, além do pedido.** (i) O planejador tem **quatro** pontos, não
três: as linhas 165-167 do esqueleto também prescrevem `orações M-<n> com estado`. (ii) O
consultor tem **dois**, não um: a linha 38 e a linha 3, que é a `description` do front matter —
e mudá-la **altera a região gerada de `.claude/README.md`**, porque ela deriva de `name`,
`model` e `description`. Sem regenerar por instrumento, o `check-drift` da própria
`Verificação` do card acusaria drift; com a `DOM-T4` fechada, o caminho é o `kit_check -Mode
generate`. (iii) As linhas 144-145 do planejador citam `orações` como **fato histórico
verdadeiro** sobre o `P-0741` (`D-10`) e ficam — entraram no `Não fazer`. (iv) A `DOM-T6`
**tinha** o mesmo vão do `AE-10` no passo 3, mas ele é **benigno**: medido, todas as ocorrências
que descrevem a forma do modelo estão dentro das duas regiões que os passos 1 e 2 já substituem
por literal; as duas restantes são `exploração` (384) e *clean architecture* (393). O passo
virou confirmação com cláusula de parada.

**Classificação.** `tatico`: nada muda escopo, rota ou contrato; `D-1`..`D-15` e o Marco 1
intocados; nenhum card novo, fila inalterada. Nada foi ao dono.

**O que fica inconclusivo.** (i) A anatomia do card no planejador (linha 367) ainda manda
`Arquivos-alvo` na forma `caminho:linha com o texto da âncora`, que contradiz o `I-12` deste
plano. **Não mexi**: promover `I-11`, `I-12` e `I-13` a doutrina do planejador é decisão do
dono, não reparo de plano — e é a terceira vez que anoto isto. (ii) `AE-3` e `AE-9` seguem no
`TK-66`. (iii) `card_check.py` segue reprovando os oito cards por forma do bloco `Verificação`;
sem decisão do dono, não reescrevo. (iv) O bloco H reescreve a `description` **deste papel**, e
o bloco I o item 3 da minha própria definição: a conferência de que a conduta nova não
contradiz a em uso cabe à revisão da `DOM-T5`, não a este ato — é a segunda vez que registro a
ressalva. (v) Três escalonamentos, três achados da mesma família (`AE-5` recorte, `AE-8`
fidelidade, `AE-10` ponto sem bloco): o padrão é card de texto normativo com aceite de arquivo
inteiro e passos que enumeram pontos. Os invariantes `I-10`, `I-11` e `I-13` cobrem os três,
mas só dentro deste plano.

### AE-11 — costura aberta: o passo 7 do reviewer contradiz o passo 5a que este plano entregou (`DOM-T5`, `A8a`/`B1`)

**Fato medido.** `.claude/agents/pantonic-reviewer.md` passo 7 (linha **127**) diz
`Retorno ao chamador — duas linhas, nada além`. Isso **contradiz** duas linhas que a própria
`DOM-T5` acabou de entregar verbatim: o passo `5a` (linha **107**) e o bullet de fronteira (linha
**150**), que mandam **anexar o dossiê `Ato de modelo` de `conflito` à linha de retorno** — forma
exigida por `GOVERNANCA.md` §3.2 e **consumida pelo bloco B do `scrum-master`**, que manda o loop
despachar o modelador quando esse dossiê aparecer.

O card nomeou **quatro** pontos em `pantonic-reviewer.md` e **não deu bloco literal para o quinto**.
A execução acertou em não redigir (`I-3`, `D-20`, `I-13`). **É a mesma classe do `AE-10`** — e é a
segunda vez que ela aparece.

**Consequência se ficar como está.** O plano fecha com a cadeia **revisor → loop → modelador**
interrompida: o revisor é instruído a não devolver o dossiê que o loop espera receber para
despachar o modelador. A `M-9` fica publicada e inexequível.

**Por que não rebaixou a entrega.** Veredito `aprovado 100%`, bloqueante `nenhuma`, todas as sete
dimensões conformes: a `DOM-T5` fez exatamente o que o card mandava. O defeito é de **autoria de
card**, não de execução — daí a recomendação `escalar` e a rota `A8a` → `B1`.

**Rota — decidida no `ESC-4` (consultor de plano, 2026-09-20; `D-21`).** Card corretivo próprio,
a **`DOM-T5a`**, `esforço low`, com o **bloco J**: substituição integral do item 7 (linhas
127-135), coerente com o passo `5a`, com o bullet 150 e com o bloco B do `scrum-master`.
Pendurar cláusula na `DOM-T6` foi considerado e **rejeitado**: a `DOM-T6` é `medium` e o tema
dela é a porta de entrada e o `README.md`, enquanto o passo 7 é definição de conduta — tema da
`DOM-T5`. Pendurar assunto alheio num card é como o `AE-2` nasceu, e a mesma opção já tinha sido
rejeitada no `ESC-1`.

### AE-12 — aceite de fidelidade morando em narrativa de executor (`DOM-T5`)

**Fato medido.** O `Pronto quando` da `DOM-T5` fecha em *"a linha de retorno traz a declaração de
fidelidade do `I-11` por bloco"* — aceite cujo **único suporte é a narrativa do executor**, que a
rubrica §3 e a fronteira do revisor proíbem usar como evidência.

E a medida mostra por quê: os treze blocos batem **byte a byte**, mas **duas das treze declarações
trazem contagem de linha errada** — `reviewer-5a` declarou `5` contra **7** reais, e o bloco `E`
declarou `9` contra **12**. O número autodeclarado erra enquanto o conteúdo está certo. Se o aceite
morasse só ali, ele teria reprovado uma entrega correta — ou aprovado uma errada.

**Rota — executada no `ESC-4` (consultor de plano, 2026-09-20; `D-22`).** O `I-11` foi **emendado**
e passou a exigir, por bloco, **três** itens de `Verificação` re-deriváveis: (1) o `sed` da região
entregue, para confronto linha a linha; (2) `grep -c` da **primeira** e da **última** linha do
bloco, que fecham as duas bordas da substituição — a borda de baixo era justamente a que nenhum
aceite alcançava; (3) `grep -c` da frase que tem de sumir, com chegada `0`. A declaração
`fidelidade conferida:` **saiu do `Pronto quando`**, desceu para `Passos` e **perdeu a contagem de
linhas**: continua como sinal para quem revisa, nunca como aceite. Aplicado à `DOM-T6` e à
`DOM-T5a`. Os cards já fechados não se reescrevem — reescrever card fechado falsifica o registro
do que foi despachado.

**Lição para quem planeja.** O `I-11` acertou ao exigir confronto bloco contra bloco; errou ao
deixar a **prova** do confronto na voz de quem executou. Declaração é útil como sinal; aceite tem
de ser comando.

### ESC-4 — quarto escalonamento ao consultor de plano (2026-09-20)

**O que motivou.** A `DOM-T5` fechou `aprovado 100%` com recomendação `escalar`: o `AE-11` (o
passo 7 do revisor proibindo o dossiê que o passo `5a`, o bullet 150 e o bloco B do
`scrum-master` exigem) e o `AE-12` (aceite de fidelidade morando em narrativa de executor).

**O que foi reparado.** Card novo `DOM-T5a` com o **bloco J**; decisões `D-21` e `D-22`; `I-11`
emendado; `DOM-T6` com os três itens do `I-11` novo — inclusive as **duas bordas** da §8.1, que
nenhum aceite alcançava — e passo 4 limitado por medição, com cláusula de parada; `Pronto
quando` da `DOM-T6` desancorado da narrativa; cabeçalho (9 tarefas), §10, modelo (`MD-3`,
`M-9` e `M-10` passam a citar `DOM-T5a`); achados `AE-11` e `AE-12`.

**O que a varredura do item 3 encontrou na `DOM-T6`.** Um ponto sem bloco, e é o passo 4:
*"rodar `check-readme.ps1` e fechar o que ele apontar"* — mandato aberto que, se o guarda
apontasse algo, exigiria redigir texto que nenhum bloco fornece. **Medido:** o guarda sai `0`
hoje, e as duas edições do card são de uma subseção `###` e de uma frase, que não tocam nenhuma
das contagens que ele confere. O passo foi limitado a isso, com parada explícita se o item
nomeado exigir redação. Os passos 1, 2 e 3 já estavam cobertos por literal e por medição do
`ESC-3`.

**Classificação.** `tatico`: nada muda escopo, rota ou contrato; `D-1`..`D-15` e o Marco 1
intocados. Nada foi ao dono por este ato — a decisão do item 4 abaixo é que sobe pelo relatório
de encerramento (`G-NOASK`).

**A decisão que o dono precisa tomar, formulada em uma linha.** *Promover `I-10`, `I-11` e
`I-13` — recorte não delimita aceite; fidelidade se prova por comando, não por declaração; um
bloco literal por ponto — de invariantes do `P-0743` a doutrina de autoria de card, gravando-os
na anatomia do card de `pantonic-planner.md` e na `docs/RUBRICA_DE_REVISAO.md` §8, ou mantê-los
locais a este plano.* **O custo medido de não promover:** quatro achados em três escalonamentos
(`AE-5` recorte, `AE-8` fidelidade, `AE-10` e `AE-11` ponto sem bloco), dois deles parando a
execução, todos em cards escritos **antes** de os invariantes existirem. **O custo de promover:**
editar a anatomia do card e a rubrica, e todo plano futuro passa a publicar mais `Verificação` —
e o `I-12` (caminho puro em `Arquivos-alvo`) entra junto ou fica de fora, porque contradiz a
forma `caminho:linha` que a anatomia do card prescreve hoje na linha 367 do planejador.

**O que fica inconclusivo.** (i) A linha 367 de `pantonic-planner.md` segue prescrevendo
`Arquivos-alvo` como `caminho:linha`, contra o `I-12` — **quarta** anotação; é parte da decisão
acima e não de reparo. (ii) `AE-3` e `AE-9` seguem no `TK-66`. (iii) `card_check.py` segue
reprovando os nove cards por forma do bloco `Verificação`. (iv) Os cards já fechados mantêm o
`I-11` na forma antiga; não se reescreve card fechado. (v) `DOM-T5a` toca o arquivo do revisor,
que julga as entregas deste plano: a revisão da própria `DOM-T5a` roda sob a definição **antiga**
do passo 7, e é a revisão seguinte — a da `DOM-T6` — a primeira a rodar sob a nova. Não é
defeito; é a janela de transição, igual à que o `AE-4` registrou, e fica declarada para quem
conduz.

### AE-13 — o bloco J repete o defeito que o `AE-1` documentou (`DOM-T5a`, `A3b`)

**Fato medido.** O bloco J da `DOM-T5a` publica o literal de aceite `devolve o dossiê e para.`
**atravessando uma quebra de linha** — `devolve o` no fim da linha **1734** do plano e
`dossiê e para.` no começo da **1735**. A `Verificação` do mesmo card exige
`grep -c 'devolve o dossiê e para.'` → `1`. Transcrevendo verbatim como a `I-3` manda, o `grep` sai
`0`: **os dois mandatos do card se contradizem na prática**.

**É o `AE-1`, de novo.** O primeiro achado desta janela, na `DOM-T1`, mediu exatamente isto e
deixou a lição escrita: *"literal que vai virar alvo de `grep` no card tem de ser publicado no plano
com a mesma quebra de linha do arquivo de destino"*. O bloco J, escrito **onze achados depois**,
repete o defeito — e desta vez num card cujo tema é justamente consertar uma contradição interna de
arquivo.

**Conduta do executor: correta, mas o dossiê é que falhou.** Ele parou e devolveu `blocked` razão
`premissa` em vez de decidir. O `AE-1` **já decidiu** este caso — reempacotar só o ponto de
soft-wrap, sem alterar palavra, pontuação ou ordem, e declarar na linha de retorno —, mas o
**despacho não carregou o precedente**. A falha é da orquestração, que tinha o precedente
registrado e não o colou no dossiê. Assumida aqui.

**Rota.** Redespacho com o precedente do `AE-1` nomeado. **Não abre escalonamento**: a decisão
existe, é do plano, e o executor não precisa tomá-la. O reparo durável do bloco J — republicar com
a quebra do destino — fica para o consultor no próximo ato de plano, se houver; se o plano fechar
antes, o `AE-1` e este achado sobem juntos ao dono como matéria de doutrina de autoria de card.

**Lição, agora medida duas vezes.** Registrar a lição no plano **não** a faz chegar a quem executa:
o `AE-1` estava escrito e o defeito voltou, porque nem o autor do bloco novo nem o despacho o
consultaram. Lição que precisa ser lembrada por quem lê é lição que vai falhar; a que funciona é a
que vira **regra verificável** — como o `I-10`, o `I-11` e o `I-13` viraram.

### AE-14 — a costura fecha no revisor e continua aberta entre o loop e o revisor (`DOM-T5a`, `A8a`/`B1`)

**Fato medido.** A `DOM-T5a` fechou a contradição **dentro** de
`.claude/agents/pantonic-reviewer.md`: o passo 7 agora admite o dossiê `Ato de modelo` abaixo das
duas linhas fixas, coerente com o passo `5a` (107) e o bullet de fronteira (150). Mas
`.claude/skills/scrum-master/SKILL.md` **reimpõe a proibição no ponto em que a instrução de fato
vincula o revisor** — o ato do despacho:

- linha **128**: `instrução de devolver só as duas linhas de veredito`
- linha **129**: `- **Saída:** duas linhas do `reviewer`.`
- linha **134**: `- **Entrada:** as duas linhas fixas:`

O **bloco B** (linha 150), escrito no `ESC-2` e aprovado na `DOM-T5`, pressupõe essa proibição
**levantada** — ele manda o loop despachar o modelador quando o dossiê aparecer na linha de
retorno. Um dossiê que o passo 6 acabou de proibir o revisor de produzir.

**Escopo do `ESC-4` ficou curto.** O card da `DOM-T5a` escopou o defeito ao passo 7 do reviewer e
deu o bloco B como *"já aprovado"*. O bloco B está correto; o que não foi tocado é o **passo 6**,
que é o emissor da instrução. O executor **acertou em não tocar o arquivo** — o `I-13` e o
`Não fazer` do card o proibiam.

**O defeito está vivo na conduta desta janela.** Todos os seis despachos de revisor feitos por esta
orquestração carregaram a frase *"devolva **somente** as duas linhas"*. A instrução que vincula o
revisor na prática é a do despacho, não a da definição dele — e é por isso que consertar só a
definição não fecha a cadeia.

**Rota — decidida no `ESC-5` (consultor de plano, 2026-09-20; `D-23`).** Card corretivo próprio,
a **`DOM-T5b`**, `esforço medium`, com **cinco** blocos literais — `K` e `L` no passo 6, `M` e
`N` no passo 7, `O` no domínio de saída do revisor — e a **tabela da cadeia** declarada e
exaustiva, que o aceite percorre elo a elo (`I-14`). Os elos de norma (`GOVERNANCA.md` §3.2 e
`docs/RUBRICA_DE_REVISAO.md` §6) foram conferidos no `ESC-5` e **estão corretos**: não entram no
card. Rota original preservada abaixo.

**Rota original (superada).** Escalonamento `ESC-5`: card corretivo irmão da `DOM-T5a`, sobre o **passo 6** do
`scrum-master` (e o que mais da cadeia estiver na mesma condição), antes do fechamento do plano.

**Lição para quem planeja — terceira ocorrência da mesma família.** `AE-11` e `AE-14` são o mesmo
defeito em dois pontos da mesma cadeia: o card corrigiu **um lado da interface** e deu o outro como
pronto. Quando um card altera um **contrato entre papéis**, o aceite tem de percorrer a cadeia
inteira — emissor, meio e consumidor —, não o arquivo onde o texto foi editado.

### ESC-5 — quinto escalonamento ao consultor de plano (2026-09-20)

**O que motivou.** A `DOM-T5a` fechou `aprovado 100%` com recomendacao `escalar`: o `AE-14`. A
costura fechou **dentro** de `pantonic-reviewer.md` e continuou aberta no `scrum-master`, que
reimpoe a proibicao no ato do **despacho** — que e onde a instrucao de fato vincula o revisor.
Somou-se o `AE-13`: o bloco J publicava um literal de aceite atravessando quebra de linha, que e
o `AE-1` repetido onze achados depois, num bloco de autoria do consultor.

**O que foi reparado.** Card novo `DOM-T5b`, com **cinco** blocos literais (`K`, `L`, `M`, `N`,
`O`) e a **tabela da cadeia** emissor -> meio -> consumidor, declarada e exaustiva; decisao
`D-23`; invariante `I-14`; cabecalho (10 tarefas), fila, secao 10, modelo (`MD-4`); achados
`AE-13` e `AE-14`.

**A varredura inteira, medida — doze elos.** Norma (`GOVERNANCA.md` 3.2, tabela de papeis e o
paragrafo "Nenhum agente aciona outro agente"): **correto**, nao se toca. Rubrica
(`docs/RUBRICA_DE_REVISAO.md` 6, alvo `modelo`): **correto**, nao se toca. Revisor: dominio de
saida (51-52) **defeituoso**, bloco `O`; passo `5a` (107), passo 7 (127) e fronteira (150)
corretos. `scrum-master`: passo 6 acao (127-128) e saida (129) **defeituosos**, blocos `K` e
`L`; passo 7 entrada (134-136) e saida (141) **defeituosos**, blocos `M` e `N`; passo 8 bloco B
(150) e passo 9 bloco C corretos. **Cinco pontos defeituosos, todos neste card.**

**A licao do `AE-13`, que e minha.** O `AE-1` ensinou que literal de aceite tem de ser publicado
na quebra de linha do destino, e eu o repeti no bloco J. O reparo nao e so o do bloco: a
`DOM-T5b` traz uma **nota de autoria** declarando que cada literal de aceite cabe inteiro numa
linha so, e que **todo** comando usa `grep -cF -e` — `-F` porque os literais tem `**`, que nao e
literal em regex, e `-e` porque cinco deles comecam por `-` e sem ele o `grep` aborta com
`unknown option`. Medi os dez comandos antes de publicar; cinco abortavam sem o `-e`.

**Classificacao: `tatico`, com tripwire.** A razao nao e inercia. O que mudou neste
escalonamento e que a superficie deixou de ser inferida e passou a ser **medida**: os doze elos
acima foram percorridos, cinco estao defeituosos e os sete restantes foram conferidos um a um,
inclusive os dois de norma, que nao entram no card porque estao certos. Enquanto a superficie
era inferida, cada card fechava um elo e descobria o proximo — dai `AE-11` e `AE-14`. O tripwire
`D-23` e o preco de eu estar errado: **um sexto ponto da mesma familia nao vira sexto card, vira
replanejamento**, e o executor para em `blocked premissa` em vez de corrigir.

**A causa-raiz, para o relatorio de encerramento.** O plano mudou um **protocolo entre papeis**
— a forma da linha de retorno do revisor — com cards escopados **por arquivo**. Nenhum card era
dono do protocolo inteiro, entao cada um corrigia o seu arquivo e dava o vizinho como pronto.
`I-10`, `I-11` e `I-13` cobrem a mecanica da autoria de card; **nenhum deles cobre isto**, e por
isso nasceu o `I-14`. E a quinta anotacao sobre promover estes invariantes a doutrina, e a
primeira que nomeia a causa em vez do sintoma.

**O que fica inconclusivo.** (i) A linha 367 de `pantonic-planner.md` segue contra o `I-12` —
quinta anotacao. (ii) `AE-3` e `AE-9` seguem no `TK-66`. (iii) `card_check.py` segue reprovando
os dez cards por forma do bloco `Verificacao`. (iv) A revisao da propria `DOM-T5b` roda sob a
instrucao de despacho **antiga** se o loop nao mudar a frase que usa ao invocar o revisor: o
bloco `K` corrige a skill, mas os seis despachos desta janela ja carregaram
"devolva somente as duas linhas" — a primeira revisao a rodar sob a forma nova e a da `DOM-T6`.
(v) Nenhum card deste plano exercita a rota completa com um dossie real; a primeira vez que o
dossie `Ato de modelo` de conflito atravessar a cadeia sera em execucao futura, e e la que a
costura se prova.

### AE-15 — o décimo terceiro elo, e o tripwire `D-23` disparando (`DOM-T5b`, encerra a janela)

**Fato medido.** A tabela da cadeia publicada na `DOM-T5b` se declara **exaustiva** (`D-23`) com
doze elos. Ela não inclui a linha `- **Entrada:**` do **passo 8** do `.claude/skills/scrum-master/SKILL.md`
(linha **151**, intocada desde `e0efcf6`), que enumera o que o roteamento recebe do passo 7 —
`status`, `veredito`, `bloqueante`, `recomendação`, contador de retentativas — e **omite o dossiê
`Ato de modelo`** que o bloco `N` (passo 7, saída) agora lhe entrega e que a `- **Saída:**` do
**mesmo passo 8** (bloco `B`, linha 154, entrega aprovada da `DOM-T5`) consome para despachar o
modelador.

**De onde veio o elo.** Ele foi **criado pela própria `DOM-T5`**, quando o bloco B acrescentou o
consumo do dossiê à saída do passo 8 sem tocar a entrada do mesmo passo. A varredura do `ESC-5`
mediu a cadeia procurando pontos que **proíbem, contam ou transportam** a linha de retorno e não o
alcançou, porque a `Entrada` do passo 8 não fala da linha de retorno do revisor: fala do que o
**passo 7** entrega ao **passo 8**.

**Consequência.** Não é defeito da `DOM-T5b`, que fechou `aprovado 100%` com as sete dimensões
conformes e entregou exatamente os cinco blocos. É a superfície que não estava delimitada — a mesma
condição que o `D-23` nomeou de antemão.

**Rota, decidida antes do fato (`D-23`).** Sexto ponto da mesma família **não vira sexto card
corretivo: vira replanejamento**. A janela de orquestração **encerra aqui** e a matéria sobe ao
dono. O consultor instruiu, no `ESC-5`, que neste caso não fosse acionado de novo.

**Rota final — absorvido pelo terceiro estágio (consultor de plano, 2026-09-20, §13).** O
replanejamento que o `D-23` exigia **chegou**, e é a diretiva do dono do terceiro estágio. O
`AE-15` **não vira card próprio**: a `D-30` tira do modelador a resolução de conflito e a passa
ao consultor, de modo que **o destino do dossiê muda** e a `- **Entrada:**` do passo 8 tem de
ser escrita já na forma nova — escrevê-la agora, na forma velha, seria refazê-la em seguida. O
elo entra no mapa de alcance da §13.2, linha do `pantonic-reviewer.md` e do `scrum-master`, e a
forma exata depende das questões `Q-8` e `Q-9`.

**O que fica vivo na árvore até lá, e por que não bloqueia.** A `- **Entrada:**` do passo 8
omite o dossiê que a `- **Saída:**` do mesmo passo consome. É inconsistência de **prosa numa
skill de orquestração**, não de instrumento: nenhum gate mecânico a lê, e a `Saída` do passo 8
já diz ao loop o que fazer quando o dossiê aparece. Fica declarada aqui para quem conduzir a
próxima janela.

**Lição, e é a que o plano custou mais caro para aprender.** Varredura de cadeia precisa **reincluir
os pontos que as entregas anteriores da mesma janela criaram**, não só os que existiam antes dela.
O `ESC-5` mediu a superfície contra o estado de `e0efcf6`; entre `e0efcf6` e a medição, a `DOM-T5`
havia criado um elo novo. Uma superfície medida contra a árvore de partida envelhece a cada entrega
que a janela faz sobre ela.

### AE-16 — a dependência declarada contradizia a §13.5 e prendia a fila no card errado (orquestração)

**Fato medido.** A `DOM-T7` declarava `Depende de: DOM-T6`. Dependência declarada em card é
vinculante para a fila (diretiva do `P-0740`, item 4), então `backlog.py next` devolvia a `DOM-T6`
mesmo depois de a ordem de execução ter sido reescrita — não era a linha de ordem que prendia, era
a dependência.

**A contradição.** A §13.5, escrita no mesmo ato que criou a `DOM-T7`, declara que a `DOM-T6`
pertence ao **Marco 5** e que **nada do terceiro estágio depende dela**. A dependência codificava a
**sequência** da fila no momento da autoria, não uma dependência de **conteúdo**, e a sequência
mudou depois.

**Por que não podia ficar.** A `DOM-T6` revisa o `README.md` contra a **árvore final**
(`G-README` dever 2). Rodá-la primeiro publicaria, na porta de entrada pública, a forma do modelo
que a `DOM-T7` substitui **na tarefa seguinte** — o defeito de publicar metade de uma mudança, que
esta janela mediu em `AE-2`, `AE-5`, `AE-11` e `AE-14`.

**Ato da orquestração.** `Depende de` da `DOM-T7` corrigido de `DOM-T6` para `DOM-T5b`, e a
`DOM-T6` movida para o fim da ordem de execução. A reordenação da fila é atribuição da orquestração
(diretiva do `P-0740`, item 4); a correção do campo é **edição de conteúdo de card**, e fica
declarada aqui para o dono revogar se discordar. Nenhum outro campo da `DOM-T7` foi tocado.

---

### AE-17 — o token `MD-<n>` fica órfão entre a norma e a gramática (`DOM-T7`, `A8a`/`B1`)

**Fato medido (2026-09-20, laudo da `DOM-T7`, veredito `aprovado 100%`, `bloqueante=nenhuma`,
`recomendacao=escalar`).** Duas linhas da árvore continuam **exigindo** `MD-<n>` depois que a
`DOM-T8` — já `ready`, próxima da fila — remove a residência do token: a linha da **tabela de
papéis** da `### 3.2` de `GOVERNANCA.md` (medida na linha 388), que manda o modelador devolver
*"a linha `MD-<n>` que registra o ato"*, e o **item (f)** do agente
`.claude/agents/pantonic-model-designer.md`, entregue pela `DOM-T4`. Os blocos `G1` e `G4` da §15
retiram `última mudança: <MD-<n>>` do cabeçalho e substituem a linha de mudanças da gramática;
depois disso **nenhuma residência define `MD-<n>`**, e nenhum card do plano re-declara as duas
linhas que o exigem.

**Por que não fecha sozinho.** A tabela de papéis é **Marco 4** e está fechada pelas `Restrições`
de todo card deste estágio: depende da `Q-11` (§13.3), aberta. O Marco 4 é exatamente o que
reescreve essa tabela — então a linha 388 não tem dono enquanto a `Q-11` não fechar, e a `DOM-T8`
não espera por ela. É a janela entre norma e gramática produzindo token órfão, a mesma família de
defeito que `AE-2`, `AE-5`, `AE-11` e `AE-14` mediram como "publicar metade de uma mudança".

**Achado irmão, do mesmo laudo.** A cláusula do `Pronto quando` da `DOM-T7` — *"nenhuma linha da
`### 3.2` descreve o modelo como tendo lista de mudanças"* — tem escopo de **seção inteira**, mas o
único instrumento que a operacionaliza é `grep -cF '### 1.3 Mudanças do modelo' = 0`, que **não
alcança** a linha 388. Na leitura ampla, a cláusula tinha alvo inalcançável dentro do escopo
declarado do card. Rota: operacionalizar a cláusula por literal que a execução possa fechar, ou
restringi-la ao parágrafo `**O que é.**`. A entrega da `DOM-T7` **não** é afetada — as três regiões
saíram verbatim e a conferência foi por diff, não por sinal do executor.

**Rota.** Matéria de plano, **antes do despacho da `DOM-T8`**: definir o dono das duas linhas sem
esperar a `Q-11`. Escalado ao consultor de plano pelo `B1`.

**Resolvido pelo `ESC-6`** (consultor de plano, 2026-09-20): `D-48`, `D-49` e `D-50`; cards
`DOM-T8a` e `DOM-T9a`; literais nas §17 e §18. A premissa do `AE-17` — *"a `Q-11` está aberta"* —
estava vencida desde a `D-47`, e o alcance era de **sete** linhas sem dono, não duas.
---

### ESC-6 — sexto escalonamento ao consultor de plano (2026-09-20)

**Entrada.** `AE-17` (`DOM-T7` fechou `aprovado 100%`, `bloqueante=nenhuma`, `recomendacao=escalar`;
`A8a` fechou pelo veredito, `B1` trouxe a pendência). Pergunta: quem é o dono das linhas que exigem
`MD-<n>` depois que a `DOM-T8` remove a residência do token, sem repetir o `AE-11`.

**Classificação: impedimento tático.** A janela segue com o reparo; nada sobe ao dono.

**O que a medição mudou na pergunta.** Três fatos, medidos antes de decidir:

1. **A premissa do `AE-17` estava vencida.** A `Q-11` está fechada desde a `D-47` e a `Q-12` desde a
   `D-46`, ambas do mesmo dia — as tabelas de §13.3 e §13.5 é que ficaram para trás. A tabela de
   papéis não está trancada por questão aberta; está trancada pela **régua do marco** (`D-43`), que
   é razão diferente e continua de pé (`D-49`).
2. **Não eram duas linhas, eram nove**, em três arquivos: `GOVERNANCA.md` 95 e 388;
   `pantonic-planner.md` 167 e 186 (mais o parágrafo e o esqueleto que as contêm);
   `pantonic-model-designer.md` 15, 44, 47, 51, 55 e 75. O censo `grep -c 'MD-'` fora de
   `docs/plans/` e `docs/RDO/` dá **10** linhas, das quais 2 são da skill que a `DOM-T8` reescreve e
   1 é de `modelo.py`, que a `DOM-T9` reescreve. **As 7 restantes não tinham dono.**
3. **Não é dívida doutrinária: é defeito no caminho da entrega do Marco 3.** A `DOM-T10` **despacha
   o modelador** — é a única tarefa do plano que o faz — e ele lê a própria definição antes de agir.
   Com a definição na forma anterior, ele devolve `### 1.3 Mudanças do modelo`, `modelo.py check`
   recusa e a contingência 1 da `DOM-T10` bloqueia. Deixar o token sobreviver até o Marco 4 era,
   medido, travar o marco que valida o desenho.

**Decisão (`D-48`) — o eixo do corte é forma × papel.** O que essas linhas descrevem é **a forma do
que o modelador devolve**, e forma é exatamente o que o terceiro estágio substitui. Vão para o
Marco 3, em dois cards corretivos: `DOM-T8a` (norma e planejador, depois da gramática) e `DOM-T9a`
(modelador, depois do instrumento e antes da `DOM-T10`). **Como isto não repete o `AE-11`:** o
`AE-11` é publicar metade de uma mudança de **papel**; aqui nenhuma atribuição de papel muda — o
ato `conflito` permanece, a tabela de papéis não ganha nem perde linha, e cada linha tocada conserva
verbatim quem faz o quê. Os dois cards publicam **guardas executáveis** disso
(`grep -cF 'resolver conflito entre o texto e a entrega'` = `1`, `## Os quatro atos` = `1`, tabela
de papéis = `9` linhas), de modo que o revisor mede a promessa em vez de acreditar nela.

**Decisão (`D-50`) — o achado irmão vira regra.** A cláusula com escopo de seção só entra num card
se a `Verificação` trouxer um **censo** que percorra a seção inteira. Os quatro cards abertos do
estágio receberam o seu: `MD-` na skill (`DOM-T8`), `Mudanças do modelo` e `MD-` no módulo
(`DOM-T9`), diff do revisor no lugar do *byte a byte* autodeclarado (`DOM-T10`) e `orações` no
`README.md` (`DOM-T6`).

**Quarto achado, encontrado no censo e reparado aqui:** o literal da §8.1 que a `DOM-T6` publicaria
descrevia o modelo com *"uma lista de mudanças"* — a forma anterior. Como a `DOM-T6` é a **última**
tarefa do plano, o plano fecharia com a porta de entrada pública na forma que ele mesmo substituiu.
O literal foi reescrito e a `Depende de` dela passou de `DOM-T5` para `DOM-T10`, que é o que
*"revisar contra a árvore final"* significa depois da reordenação do `AE-16`.

**Reparo, em ponteiros.** Cabeçalho (`Ordem de execução`, `Tarefas: 16`); `D-48`, `D-49` e `D-50` na
§3; cards `DOM-T8a` e `DOM-T9a` na §9; `DOM-T8`, `DOM-T9`, `DOM-T10` e `DOM-T6` emendados; §10
estendida (o grafo estava parado no estágio 2); notas de superação em §13.3 e §13.5; §17 e §18 como
residência única dos dez blocos literais (`R1`..`R4`, `S1`..`S6`).

**O que fica para quem conduz.** O consultor devolveu, na linha de retorno, o dossiê `Ato de modelo`
de **emenda**: as listas `tarefas:` das orações `M-1`, `M-8` e `M-11` precisam citar os dois cards
novos, e quem escreve ali é o `pantonic-model-designer` (`M-9`, `D-5`). Enquanto o modelador não
rodar, o plano tem duas tarefas que operação nenhuma cita.

**O que fica inconclusivo.** A citação `ESC-6` da `DOM-T10` foi escrita **antes** deste
escalonamento existir, apontando para um número medido no replanejamento; ela passa a ser verdadeira
por coincidência de numeração — a série de `ESC` deste plano ia até `ESC-5`. Fica registrado para
que ninguém a leia como prova de que o número veio daqui: os `14` cards eram do replanejamento, os
`16` são deste ato.


---

### AE-18 — a `§5` e a `§15` disputam a mesma residência, e a skill aponta para a superada (`DOM-T8`, `A8a`/`B1`)

**Fato medido (2026-09-20, laudo da `DOM-T8`, veredito `aprovado 100%`, `bloqueante=nenhuma`,
`recomendacao=escalar`).** O preâmbulo de `## Gramática legível por máquina`, em
`.claude/skills/diario-de-obras/SKILL.md`, diz que a subseção `### Modelo de domínio (seção do
plano)` transcreve a **§5** deste plano. A `DOM-T8` transcreveu a **§15**, que substitui **quatro
das seis** linhas da tabela — cabeçalho, objetos, operações, e a linha de mudanças virando duas
(estado e versões). A **§5 segue na árvore na forma anterior** (`última mudança: MD-<n>`, objetos
sem `propriedades`, linha de mudanças): duas seções do mesmo plano reivindicam ser **residência
única** (`I-3`) do mesmo texto, com conteúdo divergente, e a skill aponta para a superada.

**Por que não fecha sozinho.** A `Restrição` da própria `DOM-T8` fechou o ponteiro **por decisão**
— *"a §15 é continuação dela, não substituição"* —, e a medição do revisor mostra a premissa
**falsa**: é substituição em quatro das seis linhas. Nenhum card do plano reconcilia a §5 com a
§15 nem corrige o ponteiro do preâmbulo.

**Fora do alcance da `D-48`.** O `ESC-6` resolveu as **sete linhas do token `MD-<n>`** em
`GOVERNANCA.md`, `pantonic-planner.md` e `pantonic-model-designer.md`, pelos cards `DOM-T8a` e
`DOM-T9a`. Este achado é outro: é o **ponteiro de residência** do preâmbulo da skill e a
coexistência de duas residências divergentes dentro do plano.

**Rota.** Matéria de plano: card corretivo, ou emenda que declare qual das duas seções governa.
Escalado ao consultor de plano pelo `B1`.

**Resolvido pelo `ESC-7`** (consultor de plano, 2026-09-21): `D-51`; bloco `R5` na §17 e quinto
ponto na `DOM-T8a`; notas de superação nas §4, §5 e §6 e fórmula de preâmbulo unificada nas §14,
§15 e §16; referência cruzada do docstring nomeada na `DOM-T9`. **A §15 governa a gramática**, e a
§5 fica como registro do que a `DOM-T2` transcreveu — não se reescreve.

---

### ESC-7 — sétimo escalonamento ao consultor de plano (2026-09-21)

**Entrada.** `AE-18` (`DOM-T8` fechou `aprovado 100%`, `bloqueante=nenhuma`,
`recomendacao=escalar`). Pergunta: qual seção governa a gramática, e quem corrige o ponteiro do
preâmbulo da skill.

**Classificação: impedimento tático.** A janela segue com o reparo; nada sobe ao dono.

**A família, medida antes de decidir — e ela é menor do que parece.** Censo de ponteiros para este
plano fora de `docs/plans/` e `docs/RDO/`: **cinco**, em dois arquivos.

| ponteiro | aponta para | estado | dono |
|---|---|---|---|
| `SKILL.md` 135 | §5 | **defasado**: a §15 substituiu quatro das seis linhas | **ninguém** → `DOM-T8a`, bloco `R5` |
| `modelo.py` 2 | `### 6` | defasado a partir da `DOM-T9`, que implementa a §16 | `DOM-T9` (arquivo inteiro), agora **nomeado** no passo 5 |
| `modelo.py` 10 | `### 6` e `V1`..`V14` | idem | `DOM-T9`, idem |
| `modelo.py` 3 e 441 | o plano, sem seção | corretos: citam o plano, não uma seção dele | — |
| `GOVERNANCA.md` | — | **não existe**: a norma não cita seção deste plano | — |

Ou seja: a norma (§4 × §14) **não tem ponteiro na árvore** e nunca teve o defeito; o instrumento
(§6 × §16) tem dois, e já têm dono; só a gramática tinha um ponteiro **sem dono**. O defeito da
família inteira não é o ponteiro: é a **fórmula do preâmbulo**.

**A causa, e é de redação.** As §4, §5 e §6 dizem *"Residência única **depois** da transcrição:
`<arquivo>`"* — fórmula correta, que nomeia o arquivo da árvore como residência e a seção como
insumo. As §14, §15 e §16, escritas no replanejamento, dizem *"Residência única"* **sem o
complemento**. Lidas juntas, duas seções do mesmo plano reivindicam o mesmo texto. A `DOM-T8`
fechou o ponteiro por decisão — *"a §15 é continuação dela, não substituição"* — e a medição do
revisor mostrou a premissa falsa.

**Decisão (`D-51`).** Residência é sempre o **arquivo da árvore**; seção de plano é **insumo
literal de card**. Quando um estágio posterior substitui parte do texto transcrito: a seção antiga
leva **nota de superação** e o bloco cercado dela **fica intacto** — reescrevê-lo falsificaria o
diff de aceite do card fechado que o transcreveu —; a seção nova recebe a **mesma fórmula** de
preâmbulo; e **o ponteiro da árvore passa a nomear a seção vigente**, por card. A §15 governa a
gramática onde ela e a §5 divergem.

**Por que o ponteiro entrou na `DOM-T8a` e não num card novo.** Ele tem de valer **antes da
`DOM-T9`**: quem executa a `DOM-T9` lê a gramática enquanto trabalha, e o preâmbulo o manda hoje à
§5, que é a forma anterior — é o `D-16` outra vez, e foi por ele que a `DOM-T3a` e a `DOM-T3b`
vieram antes da `DOM-T4`. A `DOM-T8a` é a **única** tarefa entre a `DOM-T8` e a `DOM-T9`, está
`ready` e **nunca foi despachada** — não há RDO nem laudo a invalidar. O card mudou de nome, de
*"o token órfão, na norma e no planejador"* para **"os ponteiros que a forma nova deixou para
trás"**, que é o que ele sempre foi: cinco ponteiros defasados, nenhum deles mudando papel.

**Rota descartada, e por quê.** Reabrir a `DOM-T8` para reescrever a §5 na forma nova: o card
fechou `aprovado 100%`, o aceite dele está satisfeito, e o achado é de **ponteiro**, não de
entrega — card fechado não se reabre. Reescrever a §5 destruiria, ainda, a única evidência contra
a qual o aceite da `DOM-T2` se confere.

**Reparo, em ponteiros.** `D-51` na §3; preâmbulos das §4, §5, §6, §14, §15 e §16; bloco `R5` na
§17, que passa a ter **cinco** blocos e muda de título; `DOM-T8a` com o quinto ponto, o quinto
censo e o quarto guarda; `DOM-T9` com a referência cruzada do docstring nomeada no passo 5 e dois
censos novos (`### 6` = `0`, `### 16` ≥ `1`); §10 com o nome e a aresta da `DOM-T8a` refeitos.

**Nota sobre o `ESC-6`.** O registro dele fala em *"dez blocos literais"* e em *"residência
única"*: era verdade no ato. Hoje são **onze** blocos e a fórmula é a da `D-51`. O registro **não
se reescreve** — é o que ele decidiu, quando decidiu.

---

### AE-19 — linha de aceite inalcançável por construção: o literal quebra em duas linhas (`DOM-T8a`, `A8a`/`B1`)

**Fato medido (2026-09-21, laudo da `DOM-T8a`, veredito `aprovado 100%`, `bloqueante=nenhuma`,
`recomendacao=escalar`).** A `Verificação` da `DOM-T8a` exigia
`grep -cF -e '§5 e §15 — onde as duas divergem, governa a §15' = 1`. O literal **quebra em duas
linhas** dentro do próprio bloco `R5` da §17 (plano, linhas 3612-3613), e `grep -cF` só casa
**dentro** de uma linha: com o bloco transcrito verbatim, a contagem é `0` — e só seria `1` se a
árvore publicasse o texto **sem** a quebra, isto é, **divergindo** da residência. A linha de aceite
era, por construção, inalcançável junto com a `I-3`.

**Consequência medida na execução.** A entrega está **correta**: o diff byte a byte dos cinco
blocos contra a §17 deu zero divergência, os cinco censos saíram `0` e os quatro guardas saíram
`1`, `9`, `15` e `2` — nenhuma atribuição de papel se moveu. O vermelho não era de entrega. Mas o
executor, diante do aceite que não casava, **decidiu** manter o bloco verbatim e conferir por
bytes, e atribuiu a falha a *"artefato de transmissão de shell"* — diagnóstico **falso**: a causa é
a quebra de linha do literal. É decisão tomada por quem executa sobre ponto que o card não fechou
(`G-NOASK`), e a `Contingência 1` do card não prevê aceite que não casa com bloco verbatim.

**Por que não é só desta tarefa.** A **mesma autoria** produziu os blocos literais restantes deste
estágio, e os **seis literais da §18** alimentam a `DOM-T9a`, ainda não despachada. O defeito é de
**forma de aceite**, não de conteúdo: literal de aceite tem de estar contido em **uma** linha do
bloco de residência (`RUBRICA_DE_REVISAO.md` §8, critérios (xi) e (xii)(d)).

**Rota.** Matéria de plano, **antes do despacho da `DOM-T9a`**: re-derivar as linhas de aceite dos
cards restantes contra os blocos que eles transcrevem, e fechar a contingência para o caso de
aceite que não casa com bloco verbatim. Escalado ao consultor de plano pelo `B1`.

**Resolvido pelo `ESC-8`** (consultor de plano, 2026-09-21): `I-15` e `I-16` na §8; contingência
nova nos quatro cards abertos; auditoria mecânica de **todos** os literais de aceite restantes,
publicada no `ESC-8`. **A autoria da linha defeituosa é do consultor** (`ESC-7`), não do executor.

---

### ESC-8 — oitavo escalonamento ao consultor de plano (2026-09-21)

**Entrada.** `AE-19` (`DOM-T8a` fechou `aprovado 100%`, `bloqueante=nenhuma`,
`recomendacao=escalar`). Duas perguntas: o defeito alcança os cards restantes, e o que o executor
faz quando o aceite não casa com bloco verbatim.

**Classificação: impedimento tático.** A janela segue com o reparo; nada sobe ao dono.

**Antes de tudo, a autoria.** A linha de aceite inalcançável foi escrita **por mim**, no `ESC-7`,
ao derivar o literal da **frase** que eu tinha em mente em vez da **linha** do bloco `R5` que eu
mesmo acabara de escrever. O executor herdou um card impossível. O que lhe cabe é o que fez
**depois**: decidir, e vestir a decisão de diagnóstico não medido. As duas falhas são distintas e
as duas viram invariante — `I-15` para quem escreve o aceite, `I-16` para quem o executa.

**A auditoria, mecânica e completa.** Critério da `RUBRICA_DE_REVISAO.md` §8 (xi) e (xii)(d): todo
literal de `grep -cF` que **entra** tem de estar contido em **uma** linha do bloco que a residência
publica. Extraí por script todos os `grep -cF` dos cards abertos e testei cada literal contra as
linhas publicáveis do plano — blocos cercados ```` ```markdown ```` mais o texto normativo da §16.

| card | literais que entram | resultado |
|---|---|---|
| `DOM-T9a` (§18) | 6 (`S1`..`S6`) | **todos cabem em uma linha** do bloco: 3631, 3642, 3656, 3666, 3686, 3667/3699 |
| `DOM-T9` (§16) | 15 substrings normativas (`V15`..`V20`, `V13` novo, os cinco exits, drift) | **todas cabem em uma linha** da §16: 3485-3541 |
| `DOM-T10` | 1 (`### 1.3 Estado inicial e estado final`) | cabe |
| `DOM-T6` | 2 (`propriedades** observadas`, `modelo de domínio** (§8.1)`) | cabem, no bloco da §8.1 do próprio card |

**Os guardas e os censos não entram no critério, e é proposital:** literal que **sai** (esperado
`0`) e guarda de imutabilidade (esperado inalterado) casam contra a **árvore de hoje**, não contra
bloco nenhum — e todos foram medidos quando escritos. O único literal do plano que não cabia em
linha publicável era o do `R5`, e é o que o `AE-19` mediu.

**Conclusão dirimente para a fila: o defeito não alcança a `DOM-T9`.** A tarefa mais cara do plano
(`xhigh`, o instrumento) tem os quinze literais dela contidos, cada um, numa linha da §16. Não há
reparo a pagar antes do despacho dela — e isso é medição, não impressão.

**O substituto medido da linha defeituosa**, para quem precisar reconferir a entrega da `DOM-T8a`
(o card está `done` e **não se reescreve**): `grep -cF -e 'onde as duas divergem, governa a §15'`
imprime `1`, e `grep -cF -e 'de-dominio.md` §5 e §15 —'` imprime `1` — os dois medidos em
2026-09-21 contra `.claude/skills/diario-de-obras/SKILL.md`. São **dois** greps, um por linha,
que é exatamente a forma que a `I-15` passa a exigir.

**Onde a regra mora, para não repetir card a card.** Na §8, que é a residência dos invariantes
deste plano — `I-15` (autoria do aceite) e `I-16` (conduta do executor) —, e cada card aberto
repete só o pedaço que o vincula, como manda o preâmbulo da §8. Os quatro cards restantes ganharam
a **contingência** correspondente e a citação nos `Fundamento`. Fora deste plano a regra já existe
em forma geral (`G-NOASK`, Regra 8, e os critérios (xi)/(xii)(d) da rubrica): o que faltava era a
conduta **operacional** — `blocked` razão `premissa` com três dados medidos —, e promovê-la a
doutrina de árvore é matéria de tíquete, não desta janela.

**Reparo, em ponteiros.** `I-15` e `I-16` na §8; contingência nova em `DOM-T9a`, `DOM-T9`,
`DOM-T10` e `DOM-T6`, com `I-15`/`I-16` acrescentados aos `Fundamento`; a frase *"residência única
da superfície"* do `Fundamento` da `DOM-T9` corrigida para *"insumo normativo"* (`D-51`).

---

### AE-20 — as seis violações novas ficaram sem fixture: aferição por dentro, não pelo caminho do usuário (`DOM-T9`, `A8`)

**Fato medido (2026-09-21, laudo da `DOM-T9`, veredito `ressalva 91%`, `bloqueante=nenhuma`,
`recomendacao=seguir com ressalva`, dimensão `testes` em `parcial`).** Os `Arquivos-alvo` da
`DOM-T9` dão **duas** fixtures inválidas — `plano-invalido.md` e `plano-invalido-2.md` — e as duas
já estão **saturadas** por `V1`..`V14`, com um teste que afirma a **ordem de emissão** sobre elas.
Somar `V15`..`V20` a qualquer uma quebra esse teste, e a `Contingência 1` do card só autorizava
**redistribuir entre essas mesmas duas**. Resultado: as seis violações novas ficaram sem fixture
nenhuma, e a suíte **não exercita o caminho `parser → check`** para elas — foram aferidas por
chamada direta a `validar`/`montar_drift` com dados sintéticos.

**O que não é.** Não é defeito de comportamento: a revisão reconstruiu o caminho ponta a ponta
(`extrair_modelo` + `validar` sobre markdown sintético e sobre `fluxo-pendente.md` com a versão
pendente adulterada) e as seis violações **disparam corretamente pelo parser**. É furo de
**aferição**: a suíte não prova o que o instrumento faz.

**Causa no dossiê.** O card dimensionou as fixtures pela forma **antiga** do vocabulário de
violações, não pela forma nova que ele mesmo entrega.

**Rota (achado com rota, pela `A8`).** Matéria de replanejamento do `P-0743`: uma **terceira**
fixture inválida (`plano-invalido-3.md`) nos `Arquivos-alvo` de um card corretivo, com um teste
funcional por violação nova via `modelo.py check --plano`, exit `1` e a substring no stderr.
Registrado e **não escalado**: o laudo fechou `Pendência: nenhuma` e a recomendação é
`seguir com ressalva` — a janela segue, e a rota é nomeada no relatório de encerramento.

---

### AE-21 — duas mãos sobre a mesma região na `DOM-T10`, sem regra de precedência (`DOM-T9a`, `A8a`/`B1`)

**Fato medido (2026-09-21, laudo da `DOM-T9a`, veredito `aprovado 100%`, `bloqueante=nenhuma`,
`recomendacao=escalar`).** A `DOM-T9a` acabou de tornar vinculante, na definição do modelador, que
ele **só devolve** com `modelo.py check --plano` saindo `0` — o que exige que **ele mesmo já tenha
gravado** a seção `## 1. Modelo conceitual` no arquivo do plano. E o **passo 2 da `DOM-T10`** manda
o **executor** transcrever, no mesmo lugar, a seção que recebeu. São **duas mãos sobre a mesma
região**, e nenhum dos dois cards fixa precedência.

**Por que importa agora.** A `DOM-T10` é a próxima da fila e é a tarefa que converte **este** plano
para a forma nova — o único caminho pelo qual `modelo.py check --plano docs/plans/P-0743-*` deixa
de sair `2`. Se as duas mãos escreverem, a segunda sobrescreve a primeira sem que nenhum aceite
perceba: o `check` sai `0` nos dois casos.

**Fronteira com o que já tem dono.** Não é o `AE-17` (token `MD-<n>`, fechado no segundo
corretivo — o censo do kit inteiro saiu `0`), não é o `AE-18` (residência, `D-51`), não é o `AE-19`
(forma de aceite, `I-15`/`I-16`) e não é o `AE-20` (fixture das violações novas). É **ordem de
escrita entre papéis** sobre a mesma região de arquivo.

**Rota.** Matéria de plano, **antes do despacho da `DOM-T10`**: fixar quem grava a seção no arquivo
e o que o outro faz. Escalado ao consultor de plano pelo `B1`.

**Resolvido pelo `ESC-9`** (consultor de plano, 2026-09-21): `D-52` e `D-53`; card `DOM-T9b` com
literal na §19; `DOM-T10` reescrita em **dois atos** com estado de entrada discriminante. **Quem
grava é o modelador**, e a seção sai dos `Arquivos-alvo` da `DOM-T10`.

---

### ESC-9 — nono escalonamento ao consultor de plano (2026-09-21)

**Entrada.** `AE-21` (`DOM-T9a` fechou `aprovado 100%`, `bloqueante=nenhuma`,
`recomendacao=escalar`). Perguntas: quem grava a `## 1`, o que o outro faz, e como o aceite
discrimina.

**Classificação: impedimento tático.** A janela segue com o reparo; nada sobe ao dono.

**A precedência não era escolha — já estava decidida, em dois lugares.** A norma diz que nenhum
outro papel escreve na seção (`M-9`, `D-5`, `GOVERNANCA.md` §3.2), e o gate publicado pela
`DOM-T9a` **exige** que o modelador grave: não há como `modelo.py check --plano` sair `0` sobre
seção que não está no arquivo. O passo 2 da `DOM-T10` — *"transcrevê-la literal e inteira"* — era o
resíduo de um desenho anterior ao gate. Sai.

**O que a medição achou além da pergunta, e teria queimado o próximo despacho.** O gate vigente
diz *"você só devolve o ato com exit `0`"*. Medido: gravada a seção neste plano, o `check` acusa
`V2` em **toda** tarefa que ainda cita `Oração do modelo` — e a conversão desse campo é da
`DOM-T10`, em linhas que o modelador está **proibido** de tocar. O gate só se fecharia se ele
corrigisse o que não é dele: **deadlock**, e da mesma família do `AE-19` — aceite inalcançável por
construção. A fronteira que o desfaz **já existe no instrumento**: `violacoes_id` indexa `V2`, `V4`
e `V14` pelo `<ID>` da tarefa (moram no card); todas as demais são indexadas por `OP-<n>` ou
`secao` (moram na seção). O gate passa a ler por essa fronteira (`D-53`, card `DOM-T9b`).

**Como o aceite discrimina — três camadas, nenhuma delas frase do executor.**

1. **Escopo:** a `## 1` sai dos `Arquivos-alvo` da `DOM-T10`. Edição do executor ali é edição fora
   de alvo, e o laudo a trata como tal.
2. **Estado de entrada do ato 2**, medido antes de qualquer edição: `check` tem de sair `1`, com
   `17` violações, **todas** `V2`. Esse estado é **impossível** no caminho errado — antes do ato do
   modelador o mesmo comando sai `2` com `modelo: forma anterior` (medido hoje), e depois da
   conversão sai `0`. Sair `0` na entrada dispara `blocked` razão `premissa`: é a assinatura de
   duas mãos, que é o que o `AE-21` teme.
3. **Registro do loop:** quem despachou o modelador foi o loop, e isso consta do registro dele —
   **não é testemunho do executor**. Pós-morte, o diff do arquivo não distingue as duas mãos
   (nada é commitado entre os atos), e é por isso que a discriminação tem de acontecer **no gate**,
   não na auditoria.

**Sobre o `AE-20` — não vira card neste plano, e a razão é a `D-43`.** A ressalva é real: as seis
violações novas não têm fixture e o caminho `parser → check` não é exercitado para elas. Mas o
**Marco 3** ainda não teve veredito, e a régua do dono diz que marco é **detector de desvio**:
gastar um card de endurecimento de suíte **antes** do `go` é gastar antes do detector — se o dono
recusar a forma nova, o instrumento muda e a fixture nova vai junto. Fica como **matéria de
replanejamento**, com o escopo já fechado aqui para não repagar a análise: `plano-invalido-3.md`
nos `Arquivos-alvo`, um TF por violação nova via `modelo.py check --plano`, exit `1` e a substring
no stderr, **sem** tocar as duas fixtures saturadas nem o teste de ordem de emissão. Nasce como
card do Marco 5 se o Marco 3 der `go`.

**Reparo, em ponteiros.** Cabeçalho (`Ordem de execução`, `Tarefas: 17`); `D-52` e `D-53` na §3;
§19 com o bloco `T1`; card `DOM-T9b` na §9; `DOM-T10` com alvo reduzido, dois atos, quatro
contingências e `Pronto quando` discriminante; §10 com o nó e as duas arestas novas. A `DOM-T6`
foi conferida e **não herda o padrão**: os blocos que ela transcreve são literais do próprio card,
sem segunda mão.

---

### AE-22 — a fronteira do gate tem quatro famílias, e o texto publicado nomeia duas (`DOM-T9b`, `A8a`/`B1`)

**Fato medido (2026-09-21, laudo da `DOM-T9b`, veredito `aprovado 100%`, `bloqueante=nenhuma`,
`recomendacao=escalar`).** A fronteira publicada na §19 — e a medição que a fundou (`D-52`/`ESC-9`:
*"todas as demais são indexadas por `OP-<n>` ou `secao`"*) — **não cobre o que `modelo.py` emite**.
`validar()` devolve **quatro** famílias de índice, não duas: `violacoes_op` (`OP-<n>`), `secao`
(`V13`, `V19`, `V20`), **`violacoes_objeto`** (`V6`, `V7`, `V15`, `V17`, indexadas pelo literal
`objeto`) e `violacoes_id` (`V2`, `V4`, `V14`).

Resultado: **4 das 20** violações — todas da seção que o **modelador** escreve, `### 1.1 Objetos` e
`### 1.3 Estado` — não caem em nenhum dos dois ramos do texto publicado: não são `OP-<n>` nem
`secao` (o ramo do *ato não concluído* não as alcança) e não são `<ID>` de tarefa (o ramo do *que
não é seu* também não).

Medido pelo caminho real do usuário, não por leitura de código:
`python .claude/tools/modelo.py check --plano tests/fixtures/modelo/plano-invalido.md` imprime
`V6 objeto — objeto externo sem uso` e `V7 objeto — origem inexistente` **entre** o bloco `OP-<n>`
e o bloco `<ID>`, no mesmo stderr que o gate manda o modelador devolver literal.

**Por que importa agora.** A **`DOM-T10`** é a **primeira autoria** do modelador neste plano — o
ato em que `V15` (objeto sem propriedade) e `V17` (propriedade sem estado) são as faltas mais
prováveis. Sem emenda, o deadlock que o `ESC-9` fechou pelo ramo `<ID>` **reabre** por um ramo que
o texto não nomeia.

**A entrega não responde por isto.** O card mandou transcrever a §19 **verbatim** (`I-3`) e a
`Contingência 2` proibiu ajustar o texto publicado (`RUBRICA_DE_REVISAO.md` §6, invariante 1). O
mesmo defeito está no `Não fazer` do card, que declara a fronteira como `violacoes_id` ×
`violacoes_op` e omite `violacoes_objeto`. A premissa errada nasceu na medição do `ESC-9` e
atravessou **intacta** a `D-52`, a `D-53`, a §19 e o card — quatro residências repetindo a mesma
frase sem que nenhuma a re-medisse.

**Rota.** Matéria de plano, **antes do despacho da `DOM-T10`**: emendar a §19 e o bullet do gate
para nomear `objeto` como família da **seção**. Escalado ao consultor de plano pelo `B1`.

**Resolvido pelo `ESC-10`** (consultor de plano, 2026-09-21): §20 com o bloco `T2`, que define o
ramo **por complemento**; card `DOM-T9c` antes da `DOM-T10`; `I-17`; `D-52`, `D-53` e a
contingência 1 da `DOM-T10` corrigidas; nota de superação na §19. **A premissa errada era minha**
(`ESC-9`).

---

### ESC-10 — décimo escalonamento ao consultor de plano (2026-09-21)

**Entrada.** `AE-22` (`DOM-T9b` fechou `aprovado 100%`). Pergunta: a fronteira do gate.

**Classificação: impedimento tático.** A janela segue com o reparo; nada sobe ao dono.

**A autoria, primeiro.** A premissa *"todas as demais são indexadas por `OP-<n>` ou `secao`"* é
minha, do `ESC-9`, e nasceu de **ler o código** — os nomes das listas `violacoes_op` e
`violacoes_id` — em vez de **rodar o instrumento**. Eu nomeei a lista e chamei de família; a
família é o **token de índice**, e `violacoes_op` carrega dois (`OP-<n>` e `secao`) enquanto uma
terceira lista, `violacoes_objeto`, existe e eu não a vi. Escrevi a medição com a mesma confiança
com que escrevo as que rodei — e é exatamente contra isso que eu mesmo publiquei o `DM-12`.

**A re-medição, pelo caminho do usuário.** Duas execuções da CLI, nenhuma leitura de função por
dentro, e a segunda numa cópia adulterada em `%TEMP%`, nunca na árvore viva:

| comando | saída medida |
|---|---|
| `modelo.py check --plano tests/fixtures/modelo/plano-invalido.md` | 10 violações: `V13 secao`, quatro `OP-<n>`, **`V6 objeto`**, **`V7 objeto`**, três de `<ID>` |
| `modelo.py check` sobre cópia de `fluxo-valido.md` com objeto sem propriedade e propriedade sem estado | `V16 OP-3`, **`V17 objeto — propriedade sem estado`**, **`V15 objeto — objeto sem propriedade`** |

Quatro tokens, vinte violações, sem sobra: `secao` (3), `OP-<n>` (10), `objeto` (4), `<ID>` (3). A
tabela completa está na §20. **`V15` e `V17` são as faltas típicas de uma autoria**, que é o ato
que a `DOM-T10` despacha — o deadlock reabriria no primeiro despacho.

**A decisão, e por que ela é diferente da anterior.** O ramo passa a ser definido por
**complemento**: é da seção **toda** violação que o instrumento não indexa pelo `<ID>` de uma
tarefa. Enumerar famílias foi o erro; a enumeração agora é **glosa**, não regra, e uma quinta
família futura cai no lado certo sozinha. A fronteira em si **não mudou** — o que é do card
continua sendo `V2`, `V4` e `V14`.

**As quatro residências da premissa, e o que aconteceu com cada uma.**

| residência | disposição |
|---|---|
| §19, bloco `T1` | **não se reescreve** — é o registro do que a `DOM-T9b` transcreveu, e o aceite dela se confere contra ele (`D-51`). Ganhou **nota de superação** apontando a §20 |
| `.claude/agents/pantonic-model-designer.md` (árvore) | corrigido pelo card **`DOM-T9c`**, com o bloco `T2` |
| `D-52` e `D-53` | **emendadas no texto**, com a correção nomeada e datada: decisão não é registro histórico, é regra vigente, e regra vigente com fato falso dentro se corrige |
| `Não fazer` da `DOM-T9b` (card `done`) | **fica como está, e por quê:** card fechado é o que o executor leu, e reescrevê-lo desalinha o card do laudo e do RDO. O `AE-22` o nomeia explicitamente e esta linha o resolve |

**A lição, promovida a invariante (`I-17`).** Bloco literal que **descreve um instrumento** não
fecha só por `grep`: o `grep` prova que o texto chegou, nunca que ele é verdadeiro. A `DOM-T9b`
fechou `aprovado 100%` com sete literais batendo e a afirmação falsa. Daí em diante, card nessa
condição traz **ao menos um comando do próprio instrumento** cuja saída confirma a afirmação, pelo
caminho do usuário. Aplicado já: a `DOM-T9c` prova a família `objeto` rodando o `check`
(`grep -c ' objeto — '` sobre o stderr imprime `2`), e a **`DOM-T6`** ganhou os dois comandos que
confrontam as duas afirmações de comportamento do bloco da §8.1 — `check` sobre um plano em forma
anterior (exit `2`, não bloqueia) e `show` abrindo por `estágio atual:`. A `DOM-T10` já fechava por
comportamento e não precisou de item novo.

**Reparo, em ponteiros.** Cabeçalho (`Ordem de execução`, `Tarefas: 18`); `I-17` na §8; `D-52` e
`D-53` emendadas; §19 com nota de superação; §20 nova, com a tabela medida e o bloco `T2`; card
`DOM-T9c` na §9; `DOM-T10` com a contingência 1 corrigida e as contagens `17` → `18`; `DOM-T6` com
o aceite de comportamento; §10 com o nó e as arestas.

---

### AE-23 — o aceite insatisfazível voltou, no card escrito para corrigir o aceite insatisfazível (`DOM-T9c`, `A3b`/`G-REPLAN`)

**Fato medido (2026-09-21, retorno do executor da `DOM-T9c`, `blocked motivo=premissa`).** O
literal de entrada do bloco `T2`

```
as de `OP-<n>` e as de `objeto`, estas últimas vindas de `### 1.1 Objetos` e de
```

imprime **`0`**, e o card declara `1`. A causa é a mesma do `AE-19`: **o próprio bloco `T2` da §20
quebra esse trecho em duas linhas** (plano, 4087-4088 — o `as` fecha uma linha e o `de \`OP-<n>\``
abre a seguinte), e `grep -cF` só casa dentro de uma linha. Com a `I-3` em vigor, o aceite é
**insatisfazível por construção**.

**O que a execução fez, e é o comportamento certo.** O executor transcreveu o bloco verbatim,
mediu, achou a divergência e **parou**, devolvendo `blocked` razão `premissa` com os três dados
medidos — comando, contagem obtida e as linhas do bloco de onde o literal sai. É exatamente a
conduta que a `I-16` passou a exigir **nesta janela**, escrita para o `AE-19`. O invariante
funcionou no primeiro caso real: onde a `DOM-T8a` decidiu sozinha e inventou um diagnóstico, a
`DOM-T9c` parou e mediu.

**O que isso diz do `I-15`.** O `ESC-8` auditou os literais de **todos** os cards abertos e
declarou que nenhum outro era inalcançável. A auditoria estava certa para os cards que existiam
naquele momento: o `T2` e a §20 **nasceram depois**, no `ESC-10`, e a mesma autoria repetiu o mesmo
erro de derivar o literal da **frase** em vez da **linha** do bloco. O `I-15` existe desde o
`ESC-8`; o que faltou foi **aplicá-lo ao escrever o bloco novo**.

**Natureza do bloqueio: de aceite, não de rota** (`G-REPLAN`, saída (c), ramo `review`). A entrega
**está na árvore**, transcrita verbatim, e a verificação de comportamento (`I-17`) do próprio card
confirma o fato que o bloco afirma: `check` sobre `plano-invalido.md` emite as quatro famílias e
`grep -c ' objeto — '` imprime `2`. A rota está confirmada pelo fato medido; o que precisa mudar é
a **redação da `Verificação`**, não o plano.

**Entrada da rodada de replanejamento.** Este achado e a razão registrada no corpo da `DOM-T9c`.
A rodada corrige o literal de aceite do `T2` — pela forma que a `I-15` já prescreve, **dois greps,
um por linha** — e confere, pelo mesmo critério, os literais dos cards que restam (`DOM-T10`,
`DOM-T6`). Teto do `G-REPLAN`: este é o **primeiro** bloqueio `premissa` da `DOM-T9c`.

**Absorvido pela rodada `RP-1` (2026-09-21).** As linhas que este achado nomeia como 4087-4088
são, depois da rodada, **4164-4165** — a rodada acresceu texto acima do bloco `T2` e a numeração
andou; o conteúdo das duas linhas é o mesmo. Decisão nova `D-54`, na §3; `Verificação` da
`DOM-T9c` reescrita com **seis** literais de entrada, cada um contido em uma linha do bloco `T2` e
cada um publicado com o par de valores medido; auditoria dos cards abertos pelo mesmo critério, com
um literal corrigido na `DOM-T10` e três na `DOM-T6`. Tarefa de volta a `review`, plano de volta a
`in-progress`. Ver `### RP-1`, abaixo.

---

### RP-1 — a rodada que absorveu o `AE-23`: o literal que atravessava a quebra (2026-09-21)

**Classificação da mudança: técnica** (`G-REPLAN`, passo 2). Nada de objetivo, de prioridade, de
doutrina ou de escopo mudou, e nada sobe ao dono: a rota está confirmada pelo fato medido do
próprio card — o instrumento emite as quatro famílias e o contador de `objeto` imprime `2` —, a
entrega está na árvore transcrita verbatim, e o que se corrigiu foi a **redação da `Verificação`**.
Decisão nova: `D-54`, na §3. Nenhum card nasceu, nenhum morreu, a fila não mudou de ordem e os
Marcos 4 e 5 não foram antecipados (`D-43`).

**Causa-raiz, na autoria.** Fase 4 do protocolo do planejador, item 7 (*teste do parser frio*, que
manda citar a ocorrência real que cada literal casa) e item 12 (v) (*o literal do comando é o que
foi colado e rodado*). Quem escreveu o bloco `T2` no `ESC-10` derivou o literal de aceite da
**frase que tinha em mente** em vez da **linha** do bloco, e **não rodou o comando antes de
publicar** — com a `I-3` em vigor, o aceite ficou insatisfazível por construção. A `I-15` existe
desde o `ESC-8` justamente para isso; o `ESC-8` auditou os literais dos cards que existiam naquele
momento, e o `T2` nasceu depois. A fenda não é de regra ausente: é de regra não aplicada ao artefato
que nasceu depois dela.

**A verificação que teria evitado o bloqueio**, agora fechada na `D-54`: rodar cada literal de
aceite **antes** de publicá-lo e publicá-lo como **par medido** — o valor na árvore e o valor no
texto anterior —, porque o par é o que separa os dois mundos e um literal que atravessa quebra dá
`0` no par inteiro, denunciando-se na hora. E, na rodada corretiva, varrer os literais de **todos**
os cards abertos pelo mesmo critério, não só o do card que bloqueou: foi essa varredura que achou
os outros dois defeitos, ambos silenciosos — o `### 1.3` da `DOM-T10`, que sem âncora imprime `9`
hoje e passaria antes de a tarefa começar, e o censo `modelo de domínio` da `DOM-T6`, com linha de
base falsa, ao lado do `sed` de fidelidade que terminava no heading seguinte e imprimia duas linhas
a mais que o bloco.

**Veredito sobre a lição para o planejador (`G-REPLAN`, saída (e)): classe conhecida, falha de
aplicação — `.claude/agents/pantonic-planner.md` NÃO foi editado.** A família já está documentada
três vezes e em três residências: o `AE-19` deste plano (o caso que a mediu), a `I-15` da §8 (a
regra vinculante, com a prescrição literal *"dois greps, um por linha"*) e o critério (v) de
`docs/RUBRICA_DE_REVISAO.md`, espelhado na fase 4 item 12 do papel. O que faltou foi **execução da
régua**, não régua: uma quarta enunciação em prosa diluiria as três que já existem e não teria
impedido este caso, porque o autor do `T2` tinha a `I-15` no mesmo plano e citada no próprio card.
Registro para a próxima ocorrência: **terceira vez desta família é sinal de que a régua precisa de
instrumento, não de mais texto** — o candidato natural é extrair os literais de `Verificação` do
card e rodá-los, e isso nasce como tíquete do kit, não como parágrafo de agente.

**O que a rodada tocou, em ponteiros.** §3: `D-54`. `DOM-T9c`: nota de atribuição no `Fundamento`,
`Verificação` reescrita (dois literais de saída e seis de entrada, cada um com a linha de origem
nomeada e o par de valores medido), guardas com par medido, `Pronto quando` com a contagem dos
literais fechada no mesmo ato (`I-4`) e sem depender de sinal autodeclarado. `DOM-T10`: o literal do
heading `### 1.3` ancorado em `^###`. `DOM-T6`: censo `modelo de domínio` vira relação re-derivada,
`sed` de fidelidade termina na última linha do bloco, `-F` no literal da borda de baixo e o passo 1
preserva a linha em branco antes do `## 9.`. `AE-23` marcado como absorvido.

---

### AE-24 — as duas provas do `Pronto quando` de um card de dois atos não têm residência (`DOM-T10`, `B0`)

**Fato medido (2026-09-21, laudo da `DOM-T10`, veredito `aprovado 100%`, `bloqueante=nenhuma`,
`recomendacao=seguir`).** O `Pronto quando` da `DOM-T10` exige cinco provas. Três são comandos
re-rodáveis sobre a árvore. As outras duas — a **saída literal do estado de entrada do Ato 2** e o
**registro do loop** que despachou o modelador entre os dois atos — chegaram ao revisor apenas na
mensagem de quem conduziu a sessão, e nenhuma tem residência declarada no repositório: quando o
laudo é descartado (`DP-K` §14.4), as duas somem. O aceite do card foi satisfeito, e é justamente a
dupla que discrimina qual mão escreveu cada região (`D-52`, `AE-21`) que fica sem lastro depois do
fechamento.

**Atribuição (`B0`).** Não é defeito da entrega: nenhum dos `Arquivos-alvo` da `DOM-T10` é
residência de registro de execução. O alvo é o desenho do registro — `rdo.py` e a doutrina de
fechamento —, fora do escopo do card. **Nenhuma dimensão rebaixada**, e a entrega não se refaz.

**Rota:** matéria de replanejamento do `P-0743`, a fixar a **RDO da tarefa** como residência das
provas de proveniência de todo card desenhado em dois atos com ato de terceiro agente no meio.

---

### AE-25 — o card despachado em dois atos entra duas vezes na série de consumo (`DOM-T10`, `B0`)

**Fato medido (2026-09-21, laudo da `DOM-T10`).** O Ato 1 da `DOM-T10` foi registrado **duas vezes**
em `docs/telemetria.tsv`: uma linha gravada pelo hook `SubagentStop` com o rótulo `DOM-T10` (lido de
`.claude/estado/tarefa-corrente.json`, que carrega o id do card, não o do ato) e outra apensada pelo
loop com o rótulo `DOM-T10-ato1` — mesma medida, `7` tool uses e `52.8k`. A série passaria a contar
o mesmo ato duas vezes. **Defeito de procedência do registro, não de grandeza:** os números estão
certos, o que falta é regra de rótulo.

**Correção aplicada no ato, pelo loop:** a linha do hook foi removida à mão e ficou a do ato
(`DOM-T10-ato1`), conforme a cláusula da skill `scrum-master` que manda o loop corrigir linha de
hook divergente. O mesmo hook **não** gravou linha para o ato do modelador nem para o Ato 2, o que
é sinal irmão: o gatilho não é confiável e já tem tíquete (`TK-55`).

**Atribuição (`B0`).** Fora dos `Arquivos-alvo` da `DOM-T10`: o alvo é `GOVERNANCA.md` §4.2 e o hook
de telemetria. **Nenhuma dimensão rebaixada.**

**Rota:** matéria de replanejamento do `P-0743`, a emendar a §4.2 fixando o **rótulo por ato**
quando um card é despachado em mais de um — e a conferir o gatilho do hook contra o `TK-55`.
