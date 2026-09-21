# P-0745 — O planejador diante do modelo: uma operação, um card

**Data:** 2026-09-21 · **Origem:** pedido do dono em 2026-09-21 (transcrito na §0) ·
**Plano de origem:** `P-0744` (classe B — este plano o sucede e herda as três tarefas dele, tarefa
a tarefa; `docs/plans/P-0744-spec-do-planejador.md` passa a `superseded`) e `P-0743` (`done`,
aceito em 2026-09-21 — é a premissa: o modelo de domínio e o modelador existem) ·
**Status:** `ready` · 2026-09-21 · **Prefixo das tarefas no diário:** `PLN-T<n>` ·
**Prefixo das decisões:** `DPN-<n>` · **Checagem de versão do kit:** modo hub — congelada em
`0.0.0` (`GOVERNANCA.md` §10), nada a comparar · **Branch de trabalho:**
`plan/planner-modelo-escopo` (criada em 2026-09-21 a pedido do dono; a execução inteira corre nela e
o merge em `main` é ato do dono ao fim, com resolução de conflitos). A entrega aceita do `P-0741`+`P-0743`,
que estava solta na árvore, é o **primeiro commit desta branch** (`e4c1608`, 84 arquivos) — `main` a alcança
por `git merge --ff-only e4c1608` sem arrastar este plano.
**Ordem de execução:** PLN-T1 → PLN-T2 → PLN-T3 → PLN-T4 → PLN-T5 → PLN-T6 → PLN-T7.
**Modelo de planejamento:** Fable 5.1 (modelo ativo da sessão de 2026-09-21, escolhido pelo dono).

**Marcos de validação pelo dono:**

| marco | o que o dono lê | veredito |
|---|---|---|
| **Marco 1** | a `## 1. Modelo conceitual` deste plano, escrita pelo modelador — em especial o estado final da propriedade *régua de dimensionamento*, que aposenta o percentual de ocupação e a tabela de tetos | `go` = o plano segue `ready`; `no-go` = `cancelled`, e o `P-0744` volta de `superseded` a `blocked` |
| **Marco 2** | `python .claude/tools/modelo.py show --plano docs/plans/P-0745-planejador-modelo-operacao.md` depois da `PLN-T5`, mais a *Diretriz de dimensionamento de tarefa* de `GOVERNANCA.md` §3 e a Fase 3 de `.claude/agents/pantonic-planner.md` | aceite registrado no diário (`GOVERNANCA.md` §4.5); `no-go` abre rodada de replanejamento |
| **Marco 3** | `docs/planner-spec.md` depois da `PLN-T6`, o `README.md` revisado (`PLN-T7`) e o documento de encerramento (skill `entrega-de-encerramento`) | aceite registrado no diário; fecha o plano |

**Tarefas:** 7 (`PLN-T1`..`PLN-T7`), fila única, sequencial.

---

## 0. O problema, verbatim

Pedido do dono, 2026-09-21, nas palavras dele:

> Avalie o projeto atual, e elabore o plano para melhoramento do agente de planejamento, agora com o
> conceito de modelo e do agente model designer estabelecido, assim como a revisão dos limites de
> janela e a mudança da orientação de granularidade de tarefa, que não mais serão atividades
> atomicas, mas ativiidades de escopo maior, mantendo a coesão e coerência do objeto trabalhado.
> Antes, porém, crie uma branch e trabalhe nessa branch, pois pode ocorrer mudanças durante a
> execução do plano. Conflitos serão resolvidos no merge apos o final

Três eixos, e o plano cobre os três: **(1)** o planejador passa a planejar **a partir do modelo**
que o modelador escreve — hoje o protocolo dele manda escrever cards que citam operações antes de
as operações existirem; **(2)** os **limites de janela** saem do dimensionamento de tarefa — o
percentual de ocupação e a tabela de tetos por classe foram calibrados numa janela de 200k sobre
tarefas atômicas, e o dono já decidiu em 2026-09-19 que o critério é coesão, não custo; **(3)** a
**unidade de trabalho** deixa de ser a tarefa atômica em toda residência da doutrina que ainda a
nomeia, e passa a ser a materialização de **uma operação inteira do modelo** — o objeto trabalhado e
as propriedades que a operação altera são a fronteira do card, e o estado final dessas
propriedades é o aceite dele.

---

## 1. Modelo conceitual

> **Como ler esta seção (Marco 1).** Ela descreve, em linguagem corrente, o que este plano
> entrega: os objetos que ele trabalha, as propriedades observadas desses objetos, a ordem em que
> as operações as alteram e o estado final que o dono especificou. A leitura gerada por
> `python .claude/tools/modelo.py show --plano docs/plans/P-0745-planejador-modelo-operacao.md` é
> esta mesma seção com o estágio atual derivado do andamento das tarefas. Escrita sobre cards que
> já existiam, pelo modo registrado na `DPN-10` — é a última vez.

**Estado do modelo:** versão 1 · 2026-09-21 · autor: modelador · 7 operações · 21 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem |
|---|---|---|---|---|
| agregado medido do planejador | o retrato contado do que o planejamento fez até aqui: quantas vezes cada comportamento apareceu, quando começou e quando foi a última vez | retrato por dimensão, série de custo do planejamento, série das rodadas de replanejamento | seção `## 12. Agregado medido` deste plano, inserida entre `## 11. Riscos` e `## Achados da execução`; dez subseções `### <n>. <dimensão>` na ordem da §4, com tabela de no máximo oito linhas cada e teto de 120 linhas para a seção inteira; só contagem, data, identificador e classe — nenhuma citação literal, nenhum trecho de plano, nenhuma linha de telemetria copiada; dimensão sem ocorrência traz a linha `sem ocorrência no corpus medido` | OP-1 |
| norma da unidade de trabalho | o texto de governança que diz qual é a unidade de trabalho do loop e por que régua ela se dimensiona | régua de dimensionamento, unidade nomeada na doutrina | residência única em `GOVERNANCA.md` §3 (matriz de responsabilidades, *A unidade de trabalho é o módulo coeso*, *Diretriz de dimensionamento de tarefa*, tabela da §4, §4.1, §4.3, G-PLANREADY e G-MODULO), espelhada em `.claude/global/CLAUDE.md` (Regras 2 e 7) e indexada em `docs/RESIDENCIA_DOUTRINA.md`; substituição de bloco nomeado, pelo texto literal dos passos da `PLN-T2`; a classe do cabeçalho do card permanece como natureza do trabalho, porque os parsers a leem | OP-2 |
| guarda da forma antiga | o teste que afere, por literal, que o percentual de ocupação e a tabela de tetos não voltaram às residências editadas | cobertura das residências editadas | `tests/test_doutrina_unidade.py`, criado pela `PLN-T2` e estendido por `PLN-T3`, `PLN-T4` e `PLN-T5`; um teste por residência editada, com assertivas por literal sobre o texto do arquivo; piso de regressão como relação — o total de `python -m pytest tests -q` não reduz da referência datada `262 passed` (2026-09-21) | OP-2 |
| gramática do card | a forma publicada de um card e as definições de conduta que nomeiam a unidade que ele materializa | formato do card, unidade nomeada nas skills | `.claude/skills/diario-de-obras/SKILL.md`, seção *Formato de uma tarefa*, mais uma linha em `modelo-por-fase`, uma em `bootstrap-pantonic` e uma em `.claude/agents/pantonic-fora-da-caixa.md`; a subseção *Modelo de domínio (seção do plano)* da mesma skill **não se toca** (fronteira com o `P-0743`, §6); ocorrência de outro sentido — passo atômico de migração, escrita atômica em disco — fica intacta | OP-3 |
| protocolo do planejador | a definição de conduta do agente de planejamento: como ele abre uma sessão, como a encerra e como recorta um card | saídas do protocolo, momento da decomposição, régua no protocolo, descrição pública do papel | `.claude/agents/pantonic-planner.md` (descrição, tese do papel, abertura do protocolo, Fases 3a e 3b, Fase 4, Fase 5, anatomia do card e rodada de replanejamento) e a região gerada `kit:agents` de `.claude/README.md`, produzida por `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` e nunca editada à mão; as entradas `RP-1`..`RP-7` e os itens de verificação que não citam ocupação permanecem — são a memória medida do papel; o escopo do papel continua na matriz de `GOVERNANCA.md` §3 (G-SCOPE) | OP-4 |
| gate do modelador | a fronteira entre o que o modelador corrige antes de devolver e o que ele devolve medido, mais a regra que diz a partir de quando o modelo se versiona | responsabilidade pelo lastro, regra do rascunho antes do primeiro aceite | `GOVERNANCA.md` §3.2 (tabela *Quem escreve* e dois parágrafos novos imediatamente antes de *Retroatividade*) e `.claude/agents/pantonic-model-designer.md` (gate de devolução e ato de autoria), nas duas pontas no mesmo card; `.claude/tools/modelo.py`, `tests/test_modelo.py` e as fixtures **não se tocam** — o vocabulário `V1`..`V20` não muda, só quem responde por `V1` e `V3` | OP-5 |
| especificação do planejador | o documento que descreve a figura do planejamento para quem precisa decidir quando acioná-la e quanto ela custa | existência do documento, ancoragem das afirmações | `docs/planner-spec.md` (novo): uma seção por dimensão da §4 deste plano, na ordem dela, aberta por `## 0. O que esta especificação não é`; descreve a figura **depois** das `PLN-T2`..`PLN-T5` (`DPN-8`); não é residência do escopo do papel (matriz de `GOVERNANCA.md` §3) nem do protocolo de conduta (`.claude/agents/pantonic-planner.md`); a lista de dimensões tem residência única na §4 e não se reenuncia | OP-6 |
| documentação pública do kit | a porta de entrada por onde quem chega ao repositório entende o que o kit faz, e o índice por onde alcança cada documento | unidade nomeada na porta de entrada, alcance pelo índice de documentos | `README.md` (glossário, §3, §4, §5, §6 e §11) e `docs/DOC_MAP.md`, com as entradas novas na forma da entrada de `docs/consultant-spec.md`; `pwsh -NoProfile -File .claude/checks/check-readme.ps1` sai `0`; numeral por extenso confere com a contagem de arquivos na árvore | OP-7 |
| corpus medido da atuação do planejador | as fontes fechadas de onde sai o retrato do antes: os achados de execução dos planos recentes, a entrega aceita e a série de consumo | fechamento do corpus | as oito fontes nomeadas no método de sondagem da `PLN-T1`, nessa ordem e só elas; acesso barato pela busca do heading dos achados de execução seguida de leitura com `offset` e `limit` — nenhum plano lido inteiro; diário e histórico ficam de fora por tamanho; fonte ausente no caminho declarado leva a tarefa a `blocked` razão `premissa`, nunca à ampliação do corpus | externo |
| modelo de domínio e o papel que o escreve | a rota entregue pelo plano anterior: a norma do modelo, a gramática que a máquina lê, o instrumento e o agente dono de todo ato sobre o modelo | forma lida pelo instrumento | `GOVERNANCA.md` §3.2, a subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras`, `.claude/tools/modelo.py` (`check` e `show`, `V1`..`V20`) e `.claude/agents/pantonic-model-designer.md`; premissa deste plano (`F-1`) e invariante dele (`I-4`) — `python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md` continua saindo `0` | externo |
| citações históricas de medida | as frases já escritas que registram uma medida do passado, e não uma regra vigente | preservação das medidas registradas | `GOVERNANCA.md:123`, `README.md:366`, `.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md` e `CHANGELOG.md:62,160` (`F-16`); invariante `I-7` — não se reescrevem em nenhuma tarefa deste plano; o limiar da janela de orquestração em `.claude/tools/ocupacao.py` também fica, por `DPN-3`, porque não dimensiona tarefa | externo |

### 1.2 Fluxo de operações

**A. Primeiro se mede o antes, porque ele deixa de existir logo depois**

- **OP-1** — O investigador mede como o planejamento se comportou até aqui: conta, dimensão a dimensão, quantas vezes cada comportamento apareceu no corpus fechado, com a ocorrência mais antiga e a mais recente, o custo que a série registra e quantas rodadas de replanejamento houve, e fecha o retrato sem nenhum dado bruto.
  - `precisa de: corpus medido da atuação do planejador` · `altera: agregado medido do planejador.retrato por dimensão, agregado medido do planejador.série de custo do planejamento, agregado medido do planejador.série das rodadas de replanejamento` · `tarefas: PLN-T1`

**B. A régua muda na doutrina, e a forma antiga fica trancada**

- **OP-2** — O redator da norma troca a régua com que a doutrina dimensiona uma tarefa: aposenta o percentual de ocupação da janela e a tabela de tetos de turnos, institui a materialização de uma operação inteira do modelo como a unidade de trabalho, e levanta a guarda executável que impede a forma antiga de voltar às residências que ele acabou de editar.
  - `precisa de: agregado medido do planejador, modelo de domínio e o papel que o escreve, citações históricas de medida` · `altera: norma da unidade de trabalho.régua de dimensionamento, norma da unidade de trabalho.unidade nomeada na doutrina, guarda da forma antiga.cobertura das residências editadas` · `tarefas: PLN-T2`
- **OP-3** — O redator da gramática reescreve o formato publicado de um card para que ele nasça como a materialização de uma operação, com o campo que copia o texto da operação e o contrato dos objetos de que ela precisa, e tira o nome da unidade antiga das demais definições de conduta que ainda o repetiam.
  - `precisa de: norma da unidade de trabalho, guarda da forma antiga, modelo de domínio e o papel que o escreve` · `altera: gramática do card.formato do card, gramática do card.unidade nomeada nas skills, guarda da forma antiga.cobertura das residências editadas` · `tarefas: PLN-T3`

**C. O vão entre o modelo e os cards se fecha nas duas pontas**

- **OP-4** — O autor de papéis fecha o vão do protocolo de quem planeja: a sessão ganha uma terceira forma de terminar sem plano fechado, em que ele grava o esqueleto e devolve o pedido de autoria do modelo na própria linha de retorno, e a decomposição só começa depois de o modelo existir, com um card por operação, na ordem delas e sem nenhum percentual no recorte.
  - `precisa de: gramática do card, norma da unidade de trabalho, guarda da forma antiga, modelo de domínio e o papel que o escreve` · `altera: protocolo do planejador.saídas do protocolo, protocolo do planejador.momento da decomposição, protocolo do planejador.régua no protocolo, protocolo do planejador.descrição pública do papel, guarda da forma antiga.cobertura das residências editadas` · `tarefas: PLN-T4`
- **OP-5** — O autor de papéis abre o portão do modelador para o plano que ainda não tem cards: a lista de tarefas de cada operação passa a ser lastro de quem planeja, as duas violações que ela dispara voltam medidas em vez de travar a devolução, e o modelo segue rascunho substituível no lugar até o primeiro aceite do dono.
  - `precisa de: protocolo do planejador, norma da unidade de trabalho, guarda da forma antiga, modelo de domínio e o papel que o escreve` · `altera: gate do modelador.responsabilidade pelo lastro, gate do modelador.regra do rascunho antes do primeiro aceite, guarda da forma antiga.cobertura das residências editadas` · `tarefas: PLN-T5`

**D. A figura nova se descreve e se publica**

- **OP-6** — O redator da especificação escreve, pela primeira vez, o documento que descreve a figura de quem planeja: uma seção por dimensão, cada afirmação ancorada no retrato medido do antes ou na decisão deste plano que instituiu o depois, e a última seção nomeando o que o corpus ainda não permite dizer.
  - `precisa de: agregado medido do planejador, protocolo do planejador, gate do modelador, norma da unidade de trabalho` · `altera: especificação do planejador.existência do documento, especificação do planejador.ancoragem das afirmações` · `tarefas: PLN-T6`
- **OP-7** — O mantenedor acerta a documentação pública contra o estado da árvore ao fim da rota: a porta de entrada deixa de chamar a unidade de trabalho pelo nome antigo e perde o orçamento de turnos por classe, o índice de documentos passa a alcançar a especificação nova e este plano, e as frases que registram medida do passado ficam como estão.
  - `precisa de: especificação do planejador, gramática do card, norma da unidade de trabalho, citações históricas de medida` · `altera: documentação pública do kit.unidade nomeada na porta de entrada, documentação pública do kit.alcance pelo índice de documentos` · `tarefas: PLN-T7`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final |
|---|---|---|
| agregado medido do planejador.retrato por dimensão | não existe retrato do papel: o que se sabe dele está espalhado pelos achados de execução de quatro planos e pela entrega aceita do `P-0743`, sem nenhuma contagem | dez subseções, uma por dimensão da §4, cada uma com o número de ocorrências, a mais antiga e a mais recente com data, a classe de erro dominante e um exemplo citado por identificador — no máximo 120 linhas, nenhum dado bruto |
| agregado medido do planejador.série de custo do planejamento | a série de consumo tem **uma** linha de planejamento (`RPC-P0735-planejamento`, 2026-08-15, Opus, 64 usos de ferramenta, 183 mil tokens); mediana e máximo coincidem (`F-9`) | a dimensão de custo declara o número de linhas, a mediana, o máximo e as datas da primeira e da última, e diz explicitamente o que uma linha só não permite afirmar |
| agregado medido do planejador.série das rodadas de replanejamento | não há contagem de quantas rodadas houve, quantas fecharam como decisão técnica no próprio contexto, quantas subiram ao dono e quantas terminaram com o plano `superseded` | as quatro contagens existem na dimensão do acionamento, e dimensão sem ocorrência aparece como linha explícita, nunca como silêncio |
| norma da unidade de trabalho.régua de dimensionamento | a diretriz dimensiona tarefa por percentual de ocupação da janela (50%, tolerância 60%) e por uma tabela de tetos de turnos por classe calibrada em 2026-08-01 sobre janela de 200 mil; os números vivem em cinco residências (`F-5`) | três critérios sem número — uma operação inteira do modelo, contexto coerente e coeso, autossuficiência em contexto; a tabela de tetos aposentada e a classe preservada como natureza do trabalho; o único limiar que fica é o da janela de orquestração, declarado fora do dimensionamento de tarefa |
| norma da unidade de trabalho.unidade nomeada na doutrina | a doutrina nomeia a tarefa atômica como unidade em dez linhas vivas de `GOVERNANCA.md`, `.claude/global/CLAUDE.md` e `docs/RESIDENCIA_DOUTRINA.md`, com destino linha a linha no censo da §7 | nenhuma dessas linhas nomeia a tarefa atômica como unidade: o módulo coeso ganha definição decidível — a materialização de uma operação do modelo — e a guarda executável afere a ausência por literal |
| guarda da forma antiga.cobertura das residências editadas | nenhum teste afere a ausência do percentual de ocupação ou da tabela de tetos; texto de doutrina sem guarda regride no primeiro transporte do kit (`DPN-9`) | um arquivo de teste novo, nascido com a norma e estendido pelas três operações seguintes, cobre por literal cada residência editada, e o total da suíte não reduz da referência datada `262 passed` |
| gramática do card.formato do card | o bloco de formato da skill abre por *Formato de uma tarefa atômica*, tem `Objetivo` em uma frase e `Pronto quando` como critério objetivo solto; o campo `Operação do modelo` não aparece nele | o bloco abre por *Formato de uma tarefa*, declara a tarefa como materialização de uma operação, traz o campo `Operação do modelo` com texto e contratos copiados, e o `Pronto quando` deriva do estado final de cada propriedade que a operação altera |
| gramática do card.unidade nomeada nas skills | três skills e um agente nomeiam a tarefa atômica em uma linha cada, fora o título do bloco de formato (`F-6`) | nenhum dos quatro a nomeia como unidade: todos falam em card materializado por uma operação do modelo; as ocorrências de outro sentido, como passo atômico de migração, ficam intactas |
| protocolo do planejador.saídas do protocolo | o protocolo declara cinco fases e **duas** saídas antes do plano fechado: campanha de investigação e rodada de decisões | **três** saídas antes do plano fechado; a terceira é o esqueleto gravado mais o dossiê de autoria do modelo devolvido na linha de retorno, para quem conduz a sessão despachar o modelador |
| protocolo do planejador.momento da decomposição | vão medido (`F-3`): a fase de autoria manda escrever cards que citam `OP-<n>` antes de as operações existirem, e a única parada prevista é a do plano já gravado | a fase de autoria se parte em duas — esqueleto e dossiê, depois decomposição sobre o modelo já na árvore —, com um card por operação, na ordem das operações e com o id derivado do número dela |
| protocolo do planejador.régua no protocolo | a Fase 4 repete a ocupação estimada de ~50% (tolerância 60%) e o sinal de card acima de ~80 linhas, no mesmo item em que já convive a régua por tema (`F-7`) | a conferência dimensiona por operação inteira, coesão e autossuficiência em contexto; nenhum percentual e nenhum sinal de volume sobrevivem, e operação que não cabe num card coeso volta ao modelador por dossiê em vez de ser partida |
| protocolo do planejador.descrição pública do papel | a `description` do agente e a linha regenerada do índice do kit anunciam decomposição em *tarefas atômicas fechadas* | as duas anunciam decomposição do modelo em cards fechados, um por operação, e a parada que devolve o dossiê de autoria; a linha do índice sai da regeneração, nunca de edição à mão |
| gate do modelador.responsabilidade pelo lastro | das violações do instrumento, só `V2`, `V4` e `V14` são declaradas alheias ao modelador; `V1` e `V3` são tratadas como da seção, e sobre plano ainda sem cards ele não consegue fechar o gate (`F-4`) | `V1` e `V3` são violações do lastro de quem planeja, voltam como saída literal medida, e a norma e a definição do papel dizem o mesmo nas duas pontas, fechadas no mesmo card |
| gate do modelador.regra do rascunho antes do primeiro aceite | a norma trata toda emenda como versionamento; não há regra para o modelo ainda não validado, e um segundo ato de autoria antes do Marco 1 não tem forma declarada | entre a autoria e o primeiro `go` do dono a seção é rascunho e se substitui no lugar, sem bloco irmão e sem linha nova no registro de versões; versionar começa a partir do primeiro aceite |
| especificação do planejador.existência do documento | `docs/planner-spec.md` não existe: o planejamento é o papel descrito só pela definição de conduta, enquanto a consultoria já tem especificação e entrada no índice (`F-14`) | o documento existe, com uma seção por dimensão na ordem da §4 e uma seção de abertura que declara o que ele não é — nem residência do escopo do papel, nem do protocolo de conduta |
| especificação do planejador.ancoragem das afirmações | não aplicável: nada escrito, e a única afirmação de custo disponível vem de uma linha de série (`F-9`) | toda afirmação numérica ou factual aponta para a subseção do agregado que a mediu ou para a decisão `DPN-<n>` que a instituiu; afirmação sem uma das duas âncoras não entra, e o que o corpus não responde é nomeado em vez de adivinhado |
| documentação pública do kit.unidade nomeada na porta de entrada | o `README.md` nomeia a tarefa atômica em dez linhas, entre elas a entrada do glossário, e carrega o parágrafo do orçamento de turnos por classe na §3 (`F-6`) | o glossário abre por card, as demais linhas falam de card por operação, o parágrafo do orçamento vira a classe como natureza do trabalho, e `check-readme.ps1` continua saindo `0` |
| documentação pública do kit.alcance pelo índice de documentos | `docs/DOC_MAP.md` não alcança a especificação do planejador, que não existe, nem este plano | duas entradas novas, na forma da entrada de `docs/consultant-spec.md`, cada uma com o resumo em uma linha, a lista de seções e a linha `**Acesso:**`, com a contagem real de linhas |
| corpus medido da atuação do planejador.fechamento do corpus | oito fontes nomeadas e alcançáveis na árvore em 2026-09-21 | as mesmas oito: fonte fora da lista não entra, nenhum plano é lido inteiro, e fonte ausente no caminho declarado para a tarefa em vez de ampliar o corpus |
| modelo de domínio e o papel que o escreve.forma lida pelo instrumento | a norma, a gramática, o instrumento e o agente estão na árvore, e o `check` sobre o `P-0743` imprime `modelo: OK — 13 operações, 9 objetos, 21 propriedades, 18 tarefas, versão 1` e sai `0` (`F-1`) | inalterada: nenhuma tarefa deste plano toca o instrumento, os testes dele, as fixtures nem a subseção da gramática, e aquele `check` continua saindo `0` (`I-4`) |
| citações históricas de medida.preservação das medidas registradas | seis frases registram medida do passado — o executor em 71 turnos numa tarefa atômica, a auditoria de consumo de 2026-07-08 e as linhas do histórico de versões (`F-16`) | as mesmas seis, intactas: medida do passado é registro, não regra, e nenhuma tarefa deste plano a reescreve (`I-7`) |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 1 | 2026-09-21 | vigente | modelador — autoria sobre o pedido do dono de 2026-09-21 (§0) e as decisões `DPN-1`..`DPN-11` |

---

## 2. Fatos estabelecidos

Todos medidos em 2026-09-21, na branch `plan/planner-modelo-escopo`, sobre a árvore que então carregava
a entrega do `P-0741`+`P-0743` solta (76 entradas em `git status --porcelain`, último commit `e0efcf6`).
Essa entrega foi commitada no mesmo dia (`e4c1608`); os fatos abaixo não mudam com isso, porque medem
conteúdo de arquivo, não estado de índice do git.

- **F-1 — O `P-0743` fechou `done` 18/18 e foi aceito pelo dono em 2026-09-21.** A norma do
  modelo de domínio (`GOVERNANCA.md` §3.2), a gramática (skill `diario-de-obras`, "Modelo de domínio
  (seção do plano)"), o instrumento (`.claude/tools/modelo.py`, `check`/`show`, `V1`..`V20`) e o
  agente `pantonic-model-designer` estão na árvore. `python .claude/tools/modelo.py check --plano
  docs/plans/P-0743-modelo-de-dominio.md` imprime `modelo: OK — 13 operações, 9 objetos, 21
  propriedades, 18 tarefas, versão 1` e sai `0`.
- **F-2 — O `P-0744` está `blocked` 0/3 e a razão do bloqueio caducou.** O cabeçalho diz *"depende
  de `P-0743` `done`"*, o que se cumpriu; mas a `## 1` dele está na forma intermediária (sem
  `### 1.3 Estado inicial e estado final`, sem `### 1.4 Registro de versões`, assinada `autor:
  planejador`) — `modelo.py check` sobre ele imprime `modelo: forma anterior — plano sem estado
  inicial e final` e sai `2`. A §0 do `P-0744` condicionou a spec à **ausência de iniciativa de
  melhoramento do agente de planejamento**; este plano é essa iniciativa. As três tarefas dele
  (`PLS-T1` agregado medido, `PLS-T2` spec, `PLS-T3` índice e README) são herdadas aqui, tarefa a
  tarefa (§6).
- **F-3 — O protocolo do planejador tem um vão medido entre o modelo e os cards.**
  `.claude/agents/pantonic-planner.md` (440 linhas) manda, na Fase 3, que a §1 seja escrita pelo
  modelador **antes** de decompor e que cada card cite `OP-<n>` com texto copiado (`V2`, `V4`,
  `V14`); mas a única parada prevista é a Fase 5 (plano gravado + dossiê de autoria) — o planejador
  escreve os cards antes de as operações existirem. O `P-0744` foi escrito assim (§1 pelo próprio
  planejador). O `P-0743` resolveu pelo inverso (`DOM-T10`: modelador escreve a §1 sobre cards já
  existentes, executor converte os cards), e mediu o custo: `AE-21` (duas mãos sobre a mesma região,
  sem regra de precedência), `AE-24` e `AE-25` (card de dois atos).
- **F-4 — O gate do modelador impede o modelo antes dos cards.** `pantonic-model-designer.md`
  linha 27: *"Só três violações não são suas (...) `V2`, `V4` e `V14`"*. `V1` (lista de tarefas
  vazia) e `V3` (id de tarefa inexistente) são tratadas como violações da seção — sobre um plano
  ainda sem cards, o modelador não consegue fechar o gate. `grep -c 'V3'` sobre o arquivo imprime
  `0`.
- **F-5 — Os limites de janela vivem em cinco residências, e uma delas é o kit.**
  `GOVERNANCA.md:169` (*"50% de ocupação da janela, com tolerância até 60%"*, critério (c) da
  diretriz de dimensionamento), `GOVERNANCA.md:177-215` (tabela *Orçamento de turnos por tarefa
  atômica*, tetos ≤15/≤40/≤60/≤30/≤50 calibrados em 2026-08-01), `.claude/global/CLAUDE.md:34` e
  `:139` (Regra 2 e Regra 7), `.claude/agents/pantonic-planner.md:237-238` (*"ocupação estimada
  ~50% da janela (tolerância 60%)"* e *"card que passa de ~80 linhas (...) é sinal de tarefa
  grande"*), `docs/RESIDENCIA_DOUTRINA.md:80` e `:142`. O único número de ocupação que governa
  execução real é `LIMIAR = 0.50` sobre `JANELA_TOKENS_DEFAULT = 1_000_000` em
  `.claude/tools/ocupacao.py:58,83` — aviso informativo da **janela de orquestração** (`B2` do
  `scrum-master`), nunca critério de tarefa.
- **F-6 — A unidade "tarefa atômica" sobrevive em vinte e uma linhas de doutrina viva**, fora de
  planos, RDOs, diário e histórico — o censo com destino linha a linha é a §7. `GOVERNANCA.md`
  conta 7 linhas com `tarefa atômica`/`tarefas atômicas`; `README.md`, 10; `.claude/global/CLAUDE.md`,
  2; `.claude/agents/pantonic-planner.md`, 1 (a `description`); skills `diario-de-obras`,
  `modelo-por-fase`, `bootstrap-pantonic`, 1 cada; `.claude/agents/pantonic-fora-da-caixa.md`, 2;
  `docs/RESIDENCIA_DOUTRINA.md`, 1. "Escrita atômica" em `backlog.py`, `rdo.py`, `telemetria.py`,
  `review_evidence.py`, `ARQUITETURA_PANTONICA.md:205` e dois docstrings de teste é **outro sentido**
  (atomicidade de escrita em disco) e não entra.
- **F-7 — O lado do executor já mudou; o lado do planejador, pela metade.** `P-0740` (`done`
  35/35, `DM-2`..`DM-5`) trocou a tarefa atômica pelo módulo coeso no executor
  (`pantonic-executor.md`, seção *Módulo coeso, não fragmento atômico*, janela de 1M medida em
  2026-09-18), em `GOVERNANCA.md` §3 (*A unidade de trabalho é o módulo coeso*) e no `G-MODULO`
  (§7 item 19). No planejador só a Fase 4 item 5 recebeu a régua do tema — e ali ela convive, no
  mesmo item, com o percentual de ocupação e o sinal de "~80 linhas".
- **F-8 — A diretiva do dono de 2026-09-19 fixa o critério.** `docs/DIARIO_DE_OBRAS.md`, diretiva
  de execução do `P-0740`, item 7: *"já resolvemos a questão de custo. Com os limites expandidos,
  nossa preocupação agora é a coesão e coerência do contexto ao invés de uso"* (`DM-30`).
- **F-9 — A série medida do planejador em `docs/telemetria.tsv` tem uma linha.** `grep -c -i
  'planner\|planejador\|planejamento'` imprime `1` (`RPC-P0735-planejamento`, 2026-08-15, Opus, 64
  tool uses, 183k tokens). A dimensão de custo da spec (§4, dimensão 7) nasce quase vazia, e é
  honesto que nasça assim.
- **F-10 — Instrumentos e guardas, hoje.** `python .claude/tools/backlog.py check` imprime `check:
  OK — nenhuma violação.` e sai `0`; `python -m pytest tests -q` termina em `262 passed`; `pwsh
  -NoProfile -File .claude/checks/check-readme.ps1` sai `0` e começa por `check-readme: OK - 10
  agente(s), 11 skill(s), 20 guardrail(s)`. `backlog.py` aceita `superseded` como estado de plano
  (`_VOCAB_PLANO`, linha 58).
- **F-11 — A tabela de agentes de `.claude/README.md` é região gerada** (`<!-- kit:agents:begin -->`
  a `<!-- kit:agents:end -->`) a partir do frontmatter dos agentes, por `pwsh -NoProfile -File
  .claude/checks/kit_check.ps1 -Mode generate`. A linha 20 repete a `description` do planejador; muda
  regenerando, nunca à mão.
- **F-12 — A forma normativa do bloco `Verificação`** é a de `docs/RUBRICA_DE_REVISAO.md` §8.1:
  `N.` + comando em bloco cercado + `→ **esperado**. **Medido antes: <valor>**`. O gate
  `card_check.py` está suspenso em efeito desde 2026-09-19 (`AE-33` do `P-0740`); a conferência é
  manual, por quem despacha.
- **F-13 — Os consumidores da unidade de trabalho já falam "módulo coeso" e não precisam de
  edição:** `passagem-de-bastao/SKILL.md:114-119` (gate de delegação: decomposição por tema),
  `scrum-master/SKILL.md:254` (`B2`, ocupação da janela de orquestração), `pantonic-reviewer.md`
  (julga UM MÓDULO ponta a ponta). Nenhum deles cita percentual de tarefa nem tarefa atômica.
- **F-14 — `docs/consultant-spec.md` §4** declara a fronteira consultor↔planejador do lado do
  consultor, e `docs/DOC_MAP.md:157` tem a entrada dele (nove linhas `Acesso:` no índice hoje).
  `docs/planner-spec.md` não existe.
- **F-15 — As duas cópias das regras globais divergem, mas não nos trechos que este plano reescreve.**
  O `CLAUDE.md` global do dono (`C:/Users/panta/.claude/CLAUDE.md`, 12.752 bytes) e a cópia do kit
  (`.claude/global/CLAUDE.md`, 10.751 bytes) diferem em **uma** região: os Controles 1.1 e 1.2 da Regra 1
  (28 linhas) existem só no arquivo do dono. Os dois blocos que a `PLN-T2` substitui — o bullet
  *Capacidade* da Regra 2 e o bullet *Orçamento por tarefa atômica* da Regra 7 — são **idênticos byte a
  byte** nas duas cópias, conferidos por `diff` em 2026-09-21: o mesmo literal fecha as duas. A divergência
  dos Controles é matéria alheia a este plano e tem tíquete próprio (`TK-68`); `.claude/sync-kit.ps1` não
  projeta `.claude/global/` (nenhuma ocorrência de `global` no script).
- **F-16 — Citações históricas de medida não são residência de regra** e ficam intactas:
  `GOVERNANCA.md:123` e `README.md:366` (executor em Opus, 71 turnos numa tarefa atômica, 2026-07),
  `.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md` (auditoria de 2026-07-08), `CHANGELOG.md:62,160`.

---

## 3. Decisões (fechadas neste ato; o executor não as reabre)

| id | decisão | razão |
|---|---|---|
| `DPN-1` | **Este plano sucede o `P-0744` (classe B).** O `P-0744` vai a `superseded` com ponteiro para cá; as três tarefas dele entram aqui tarefa a tarefa (§6): `PLS-T1` → `PLN-T1`, `PLS-T2` → `PLN-T6`, `PLS-T3` → `PLN-T7`. A residência das dez dimensões da spec passa a ser a §4 deste plano | `F-2`: a premissa da §0 do `P-0744` caiu com este pedido; regra de convergência (skill `diario-de-obras`, "Planos derivados"): uma iniciativa, um plano vivo. Herdar fase a fase perde tarefa (`GOVERNANCA.md` §3, caso `P-0725`) |
| `DPN-2` | **A unidade de trabalho é a operação do modelo.** Na autoria, cada card materializa **exatamente uma** operação e cada operação tem **exatamente um** card, com o id derivado do número da operação (`<prefixo>-T<n>` ↔ `OP-<n>`). Card corretivo nascido em replanejamento (`T<n>a`, `T<n>b`) soma-se à operação do card que corrige. O planejador **nunca parte uma operação em dois cards**: operação que não cabe num card coeso é defeito do modelo (operação com propriedade embutida, `GOVERNANCA.md` §3.2, *Objeto, operação e propriedade*) e volta ao modelador por dossiê | `F-7`, `F-8`: "módulo coeso" ganha definição decidível — deixa de ser recorte por juízo e passa a ser consequência do modelo, como o dono pediu ("coesão e coerência do objeto trabalhado"). `P-0743` mediu a relação: 13 operações, 13 cards de autoria, 5 corretivos |
| `DPN-3` | **O percentual de ocupação e a tabela de tetos saem do dimensionamento de tarefa.** A *Diretriz de dimensionamento de tarefa* passa a três critérios sem número: (a) uma operação inteira do modelo; (b) contexto coerente e coeso; (c) autossuficiência em contexto para a execução. A tabela *Orçamento de turnos por tarefa atômica* é aposentada; a **classe** do cabeçalho permanece como natureza do trabalho (os parsers a leem), sem teto. O único número de ocupação que fica é o limiar da **janela de orquestração** (`ocupacao.py`, `B2`), que este plano **não toca** | `F-5`, `F-8`: os números foram calibrados sobre tarefas atômicas numa janela de 200k; a janela real é 1M e o dono decidiu que o critério é coesão. Manter número que não dimensiona mais nada é a "régua interna" que ninguém usa e todo agente lê |
| `DPN-4` | **O protocolo do planejador ganha uma terceira saída e a Fase 3 se parte em duas.** Fase 3a — *esqueleto e dossiê*: o planejador grava o plano sem a §1 e sem os cards (§0, fatos, decisões, invariantes, fora de escopo, riscos) e devolve, na linha de retorno, o dossiê `Ato de modelo` de `autoria` (**SAÍDA 3**); quem conduz a sessão despacha o modelador. Fase 3b — *decomposição*: com a §1 na árvore, o planejador escreve um card por operação, na ordem das operações, e só então roda a Fase 4 e a Fase 5 | `F-3`, `F-4`: é o vão medido. Nenhum agente aciona outro (`GOVERNANCA.md` §3.2), logo a parada é obrigatória; sem ela o planejador continua inventando `OP-<n>` ou assinando a §1 |
| `DPN-5` | **A lista `tarefas:` de cada operação é lastro, não modelo, e é do planejador.** Na autoria, o modelador a preenche pela convenção `<prefixo>-T<n>` para `OP-<n>`; depois da autoria, quem a mantém é o planejador (Fase 3b e rodada de replanejamento). No gate do modelador, `V1` e `V3` passam a ser violações **que não são dele**, ao lado de `V2`, `V4` e `V14`, e voltam como saída literal | `F-4`: sem isso a `DPN-4` é inexequível — o modelador não fecha o gate sobre plano sem cards. Um id de card corretivo não muda o que o plano entrega, e versionar o modelo (`## 1A`) por um id seria custo sem leitura para o dono |
| `DPN-6` | **O aceite do card deriva do estado final.** `Objetivo` é o texto da operação copiado; `Pronto quando` enumera, por propriedade que a operação `altera:`, o estado final da `### 1.3` e a linha de `Verificação` que o mede; `Camada e fronteira` transcreve o contrato dos objetos de `precisa de:`. Card cuja `Verificação` não mede alguma propriedade alterada é card incompleto | pedido do dono: "coesão e coerência do objeto trabalhado". `GOVERNANCA.md` §3.2: *o aceite do plano é a confrontação dos dois estados* — o card herda o mesmo critério, por propriedade |
| `DPN-7` | **A `## 1` só é rascunho antes do Marco 1.** Segundo ato de autoria antes do Marco 1 (o planejador devolveu achado de decomposição) substitui a versão 1 no lugar, sem versionar; versionar (`## 1A`) só faz sentido a partir do primeiro `go` | `GOVERNANCA.md` §3.2 governa a emenda de modelo **validado**; antes do Marco 1 não há versão validada a preservar |
| `DPN-8` | **A spec do planejador descreve a figura depois deste plano**, ancorada no agregado da `PLN-T1` (o antes) e nas decisões deste plano (o depois). A lista de dimensões é a §4 | `DPL-3` do `P-0744` (só afirmação medida) continua valendo; escrever a spec antes das mudanças seria descrever uma figura que este plano aposenta |
| `DPN-9` | **Uma guarda executável tranca a forma antiga:** `tests/test_doutrina_unidade.py`, nascido na `PLN-T2` e estendido por `PLN-T3`, `PLN-T4` e `PLN-T5`, afere por literal a ausência do percentual de ocupação e da tabela de tetos nas residências que este plano edita | forma de aceite *invariância* medida no `P-0740`; texto de doutrina sem guarda regride no primeiro `sync` |
| `DPN-10` | **O modelo deste plano é escrito sobre cards que já existem** (o modo do `DOM-T10`), porque a `DPN-5` ainda não está na árvore — o gate vigente recusaria a autoria sobre plano sem cards. É a última vez: a partir da `PLN-T5`, a Fase 3a precede os cards | `F-4`. Registrar o modo é o que permite ao `P-0746` em diante medir a diferença |
| `DPN-11` | **Nada é commitado por tarefa; o commit é no marco**, na branch `plan/planner-modelo-escopo`; o merge em `main` é ato do dono | diretiva do dono de 2026-09-18 (`P-0740`, item 3) e o pedido da §0 |
| `DPN-12` | **A `PLN-T2` edita as duas cópias das regras globais** — a do kit (`.claude/global/CLAUDE.md`) e a do dono (`C:/Users/panta/.claude/CLAUDE.md`, fora do repositório) —, aplicando a cada uma o **mesmo literal**, e nada além dos dois blocos nomeados. O dono veta no Marco 1 se não quiser o segundo alvo | `F-15`: os dois blocos são idênticos byte a byte, e a cópia do dono é a que carrega em toda sessão. Editar só a do kit publica **metade** da mudança — a classe de defeito medida em `docs/Entregas Aceitas/Entregas - P-0743.md` (*metade de mudança de papel publicada*) — e deixa a regra que todo agente lê contradizendo a doutrina do repositório |

---

## 4. As dez dimensões da especificação (normativa; a `PLN-T6` as escreve)

> Residência única da lista de dimensões — herdada da §4 do `P-0744` (`DPN-1`). A `PLN-T1` mede
> uma tabela por dimensão; a `PLN-T6` escreve uma seção por dimensão. Nenhuma outra seção deste
> plano reenuncia a lista.

| # | dimensão | a pergunta que a seção responde |
|---|---|---|
| 1 | A figura, em uma página | o que é o planejamento, em um parágrafo que quem nunca viu entende |
| 2 | Gatilho | o que aciona uma sessão de planejamento, e o que **não** aciona |
| 3 | Domínio de decisão | o que o planejador fecha por si, e o que sobe ao dono |
| 4 | Operacionalização do plano em cards | como um modelo vira cards: a operação como unidade, o que entra num card, o que fica fora, e por que a partição é do modelo e não do planejador |
| 5 | Fronteira | onde o planejamento termina e começam o modelador, o consultor, a orquestração e a revisão |
| 6 | Instrumento | que comandos o planejador roda, por que roda, e o que ele nunca mede por conta própria |
| 7 | Custo e teto | quanto custa uma sessão de planejamento, medido, e quando não abrir uma — e o que a série ainda não permite dizer |
| 8 | A rodada de replanejamento | entrada, saída e posição na fila, com a série das rodadas já ocorridas |
| 9 | Estatística do próprio acionamento | quantas rodadas houve, quantas fecharam como decisão técnica e quantas subiram ao dono |
| 10 | O que esta especificação não fecha | as perguntas que o corpus medido não responde, nomeadas em vez de respondidas por adivinhação |

---

## 5. Invariantes de execução

- **I-1** — Nenhuma tarefa commita (`DPN-11`). Toda edição fica na branch
  `plan/planner-modelo-escopo`; a orquestração commita no marco.
- **I-2** — Piso de regressão é relação: o total de `python -m pytest tests -q` re-medido no
  despacho não reduz; cada card soma os testes que declara. Referência datada: `262 passed`
  (2026-09-21).
- **I-3** — `python .claude/tools/backlog.py check` imprime `check: OK — nenhuma violação.` e sai
  `0` ao fim de toda tarefa.
- **I-4** — `python .claude/tools/modelo.py check --plano docs/plans/P-0745-planejador-modelo-operacao.md`
  sai `0` ao fim de toda tarefa; e sobre `docs/plans/P-0743-modelo-de-dominio.md` continua saindo
  `0` (invariância: nenhuma tarefa muda a gramática que o instrumento lê).
- **I-5** — Todo número de aceite deste plano é referência datada de 2026-09-21; quem despacha o
  re-deriva antes de delegar.
- **I-6** — Card que muda uma enumeração fecha, no mesmo card, as frases da mesma seção que contam
  ou qualificam o conjunto.
- **I-7** — As citações históricas da `F-16` **não se reescrevem**: são medida do passado, não
  regra.
- **I-8** — Nenhum card edita `.claude/tools/*`, `tests/test_ocupacao.py`,
  `.claude/skills/scrum-master/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`,
  `.claude/agents/pantonic-executor.md`, `.claude/agents/pantonic-reviewer.md`,
  `.claude/agents/pantonic-consultant.md`, `CHANGELOG.md`, nem qualquer arquivo de `docs/plans/`
  que não seja este.
- **I-9** — Toda linha de `Verificação` por efeito em arquivo publica os dois valores rodados,
  antes e depois; literal com crase, asterisco ou barra invertida vai em bloco cercado.

---

## 6. Herança do `P-0744` e fronteira

| tarefa do `P-0744` | destino aqui | o que muda |
|---|---|---|
| `PLS-T1` — agregado medido | `PLN-T1` | corpus ganha os achados do `P-0743` (`AE-1`..`AE-25`) e a entrega aceita; o agregado passa a ser a **§12** deste plano |
| `PLS-T2` — a especificação | `PLN-T6` | depende também das mudanças (`PLN-T2`..`PLN-T5`); a dimensão 4 descreve a operação como unidade (`DPN-8`) |
| `PLS-T3` — índice e README | `PLN-T7` | soma a revisão das dez linhas de `README.md` que dizem "tarefa atômica" (`F-6`) e a entrada de `docs/DOC_MAP.md` para este plano |

Fronteira com o `P-0743` (`done`): este plano **edita** três artefatos que aquele entregou —
`GOVERNANCA.md` §3.2 (dois parágrafos: lastro e rascunho antes do Marco 1), a tabela *Quem escreve*
e `.claude/agents/pantonic-model-designer.md` (gate e ato de autoria) — e **não toca** `modelo.py`,
`tests/test_modelo.py`, `tests/fixtures/modelo/` nem a gramática da skill `diario-de-obras` na
subseção "Modelo de domínio (seção do plano)". Retrabalho depois do `done` nasce como item novo: é
o que estas tarefas são.

---

## 7. Censo das formas reais — cada ocorrência com destino

> Inventário exigido pelo protocolo do planejador (Fase 1, *plano cujo produto lê ou escreve um
> corpus*), medido em 2026-09-21 por `grep -rn -i 'atômic\|atomic'` e `grep -rn -E '50%|60%|~80
> linhas|fatias verticais'` sobre `*.md`, `*.py`, `*.ps1`, excluídos `docs/plans/`, `docs/RDO/`, o
> diário, o histórico, `docs/Entregas Aceitas/`, `docs/audits/`, `docs/benchmark/`,
> `docs/CUSTO_DO_PICKUP.md`, `docs/consultant-spec.md` e `docs/telemetria.tsv` (registro, não regra).

| arquivo:linha | forma encontrada | destino |
|---|---|---|
| `GOVERNANCA.md:91` | matriz, linha Planejamento: "tarefas atômicas fechadas", "ocupação estimada", "dossiê de autoria junto com o plano gravado" | `PLN-T2` reescreve |
| `GOVERNANCA.md:123` | "numa única tarefa atômica, ~30% do limite de 5h" (medida de 2026-07) | **fica** (`I-7`) |
| `GOVERNANCA.md:137-147` | "A unidade de trabalho é o módulo coeso" | `PLN-T2` acrescenta a definição pela operação |
| `GOVERNANCA.md:165-176` | Diretriz de dimensionamento, critério (c) "50% de ocupação (...) 60%" | `PLN-T2` reescreve |
| `GOVERNANCA.md:177-215` | "Orçamento de turnos por tarefa atômica" + tabela de tetos + três parágrafos | `PLN-T2` substitui por um bullet |
| `GOVERNANCA.md:389` | tabela *Quem escreve*, linha `planejador` | `PLN-T5` reescreve |
| `GOVERNANCA.md:420` | tabela §4, "tarefa atômica — uma por contexto" | `PLN-T2` reescreve |
| `GOVERNANCA.md:434,438` | §4.1 "checklist de tarefas atômicas", "Uma tarefa atômica bem escrita" | `PLN-T2` reescreve |
| `GOVERNANCA.md:542` | §4.3 "várias tarefas atômicas" | `PLN-T2` reescreve ("várias tarefas") |
| `GOVERNANCA.md:663` | "quebra a atomicidade" (caso de uso de plugin) | **fica** — outro sentido |
| `GOVERNANCA.md:781` | G-PLANREADY condição 2 | `PLN-T2` reescreve |
| `GOVERNANCA.md:923-926` | G-MODULO, enunciado | `PLN-T2` acrescenta a definição pela operação |
| `.claude/global/CLAUDE.md:31-36` | Regra 2, bullet Capacidade: "50% de ocupação (...) 60%" | `PLN-T2` reescreve |
| `.claude/global/CLAUDE.md:49` | Regra 2, "várias tarefas atômicas" | `PLN-T2` reescreve |
| `.claude/global/CLAUDE.md:139-143` | Regra 7, bullet "Orçamento por tarefa atômica" | `PLN-T2` reescreve |
| `C:/Users/panta/.claude/CLAUDE.md:31-36` | Regra 2, bullet Capacidade — **idêntico byte a byte** ao do kit (`F-15`) | `PLN-T2` reescreve (`DPN-12`) |
| `C:/Users/panta/.claude/CLAUDE.md:167-171` | Regra 7, bullet "Orçamento por tarefa atômica" — **idêntico byte a byte** ao do kit | `PLN-T2` reescreve (`DPN-12`) |
| `C:/Users/panta/.claude/CLAUDE.md`, Controles 1.1 e 1.2 | 28 linhas que a cópia do kit não tem | **fica** — matéria alheia ao tema, tíquete `TK-68` |
| `.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md:4,71-72` | auditoria de 2026-07-08 | **fica** (`I-7`) |
| `docs/RESIDENCIA_DOUTRINA.md:80` | item 2.1 "capacidade (~50% da janela)" | `PLN-T2` reescreve a célula |
| `docs/RESIDENCIA_DOUTRINA.md:142` | item 7.7 "Orçamento por tarefa atômica" | `PLN-T2` reescreve a linha |
| `.claude/agents/pantonic-planner.md:3` | `description`: "tarefas atômicas fechadas" | `PLN-T4` reescreve |
| `.claude/agents/pantonic-planner.md:237-238` | Fase 4 item 5: "~50% (...) 60%", "~80 linhas" | `PLN-T4` reescreve |
| `.claude/agents/pantonic-planner.md:187` | "fatias verticais finas primeiro" | `PLN-T4` reescreve |
| `.claude/agents/pantonic-executor.md:140` | heading "Módulo coeso, não fragmento atômico" | **fica** — é a negação |
| `.claude/agents/pantonic-fora-da-caixa.md:54` | "cada passo virando tarefa atômica candidata" | `PLN-T3` reescreve |
| `.claude/agents/pantonic-fora-da-caixa.md:67` | "passos atômicos, cada um testável" (passo de migração) | **fica** — outro sentido |
| `.claude/skills/diario-de-obras/SKILL.md:206` | heading "Formato de uma tarefa atômica" | `PLN-T3` reescreve |
| `.claude/skills/modelo-por-fase/SKILL.md:24` | "Uma tarefa atômica do diário de obras, TDD" | `PLN-T3` reescreve |
| `.claude/skills/bootstrap-pantonic/SKILL.md:34` | "checklists de tarefas atômicas" | `PLN-T3` reescreve |
| `.claude/README.md:20` | região gerada, `description` do planejador | `PLN-T4` regenera |
| `README.md:94,305,350,382,405,432,478,824,825` | glossário, §3, §4, §5, §6, §11 | `PLN-T7` reescreve |
| `README.md:366` | "uma única tarefa atômica chega a 71 turnos" (medida) | **fica** (`I-7`) |
| `README.md:401`, `GOVERNANCA.md:724` | "fatias verticais finas antes de camadas horizontais" (G-SLICE, §7 item 1: ordem de entregáveis, não tamanho de card) | **fica** — outro sentido |
| `CHANGELOG.md:62,160` | histórico de versões | **fica** (`I-7`) |
| `.claude/tools/ocupacao.py:83,86,128`, `tests/test_ocupacao.py:3` | limiar 0,50 da janela de orquestração | **fica** — `DPN-3`, fora do dimensionamento de tarefa |
| `backlog.py`, `rdo.py`, `telemetria.py`, `review_evidence.py`, `ARQUITETURA_PANTONICA.md:205`, `tests/test_backlog.py:1004`, `tests/test_rdo.py:9` | "escrita atômica" | **fica** — outro sentido |

---

## 8. Tarefas

### PLN-T1 — O agregado medido da atuação do planejador [Sonnet · esforço high · classe investigacao]
- **Status:** `ready` · 2026-09-21
- **Objetivo:** a seção `## 12. Agregado medido` deste plano preenchida com uma tabela por dimensão
  da §4, dentro de 120 linhas, sem nenhum dado bruto — o retrato do planejador **antes** deste plano.
- **Fundamento:** `DPN-1`, `DPN-8`; fatos `F-2`, `F-9`. Herda o método da `PLS-T1` do `P-0744`
  com o corpus ampliado; o corpus é fechado e não se amplia.
- **Operação do modelo:** `OP-1`
  - OP-1: O investigador mede como o planejamento se comportou até aqui: conta, dimensão a dimensão, quantas vezes cada comportamento apareceu no corpus fechado, com a ocorrência mais antiga e a mais recente, o custo que a série registra e quantas rodadas de replanejamento houve, e fecha o retrato sem nenhum dado bruto.
  - precisa de: corpus medido da atuação do planejador — as oito fontes nomeadas no método de sondagem da `PLN-T1`, nessa ordem e só elas; acesso barato pela busca do heading dos achados de execução seguida de leitura com `offset` e `limit` — nenhum plano lido inteiro; diário e histórico ficam de fora por tamanho; fonte ausente no caminho declarado leva a tarefa a `blocked` razão `premissa`, nunca à ampliação do corpus
- **Camada e fronteira:** nenhuma camada de produto é tocada. A tarefa lê o corpus e escreve
  **só** neste arquivo de plano.
- **Método de sondagem:**
  - **Corpus fechado, nesta ordem e só ele:** (1) `.claude/agents/pantonic-planner.md`, as entradas
    `RP-1`..`RP-7` e os casos `AE-*` e `DM-*` que elas citam; (2)
    `docs/plans/P-0739-backlog-instrumento.md`, seção `## Achados da execução`; (3)
    `docs/plans/P-0740-loop-de-modulos.md`, seção `## Achados da execução`; (4)
    `docs/plans/P-0741-modelo-conceitual.md`, seção `## Achados da execução`; (5)
    `docs/plans/P-0743-modelo-de-dominio.md`, seção `## Achados da execução` (`AE-1`..`AE-25`);
    (6) `docs/Entregas Aceitas/Entregas - P-0743.md`, inteiro; (7) `docs/consultant-spec.md`, §1 e
    §4, para a fronteira; (8) `docs/telemetria.tsv`, filtrado pelas linhas cujo campo `tarefa`
    contenha `planej` ou `planner`.
  - **Acesso barato:** cada seção `## Achados da execução` se alcança por
    `grep -n '^## Achados da execução' <plano>` seguido de leitura com `offset` e `limit` a partir
    da linha devolvida. Nenhum plano é lido inteiro.
  - **Métricas, por dimensão da §4:** número de ocorrências encontradas; a ocorrência mais antiga e
    a mais recente, com data; a classe de erro dominante, quando houver; e **uma** ocorrência de
    exemplo, citada por identificador e data, nunca transcrita.
  - **Métricas de custo (dimensão 7):** de `docs/telemetria.tsv`, o número de linhas de
    planejamento, o consumo mediano e o máximo, e a data da primeira e da última — com uma linha só
    (`F-9`), mediana e máximo coincidem e a tabela diz isso.
  - **Métricas de acionamento (dimensão 9):** número de rodadas de replanejamento ocorridas;
    quantas fecharam como decisão técnica ou tática no próprio contexto; quantas subiram ao dono;
    quantas terminaram com o plano `superseded`.
  - **Formato do agregado que volta:** a seção `## 12. Agregado medido` deste arquivo, inserida
    imediatamente antes de `## Achados da execução` e depois de `## 11. Riscos`, com **dez**
    subseções `### <n>. <dimensão>` na ordem da §4, cada uma com uma tabela de no máximo oito
    linhas. **Teto: 120 linhas** para a seção inteira.
  - **Nenhum dado bruto entra no agregado:** nenhuma citação literal de achado, nenhum trecho de
    plano, nenhuma linha de telemetria copiada. Só contagem, data, identificador e classe.
- **Restrições desta tarefa:**
  - Não ampliar o corpus. Fonte fora da lista de oito itens acima não entra.
  - Não editar nenhum arquivo além de `docs/plans/P-0745-planejador-modelo-operacao.md`.
  - Não escrever prosa de recomendação: a tarefa mede, não conclui.
  - Não commitar (`I-1`).
- **Não fazer:**
  - Não abrir `docs/DIARIO_DE_OBRAS.md` nem `docs/DIARIO_HISTORICO.md`: estão fora do corpus por
    tamanho.
  - Não criar `docs/planner-spec.md`: é a `PLN-T6`.
  - Não tocar a `## 1. Modelo conceitual` nem nenhum card deste plano.
- **Contingências:**
  1. Se uma dimensão da §4 não tiver nenhuma ocorrência no corpus → a subseção dela existe com a
     tabela vazia e a linha literal `sem ocorrência no corpus medido`. Dimensão sem ocorrência é
     insumo da dimensão 10, não motivo de parada.
  2. Se o agregado passar de 120 linhas → cortar pela cauda das tabelas, mantendo a ocorrência
     mais antiga e a mais recente de cada dimensão, e registrar na linha de retorno
     `contingência 2 acionada: <dimensão> cortada de <n> para 8 linhas`.
  3. Se alguma das oito fontes do corpus não existir no caminho declarado → parar e sinalizar
     `blocked` razão `premissa`, com o caminho na linha de retorno.
- **Testes:** nenhum — a entrega é agregado em texto.
- **Verificação:**

  1. ```
     grep -c '^## 12. Agregado medido' docs/plans/P-0745-planejador-modelo-operacao.md
     ```
     → **1**. **Medido antes: 0**.
  2. ```
     grep -c '^### [0-9]*\. ' docs/plans/P-0745-planejador-modelo-operacao.md
     ```
     → **10** — as dez subseções do agregado, numeradas. **Medido antes: 0**.
  3. ```
     python -c "import pathlib;t=pathlib.Path('docs/plans/P-0745-planejador-modelo-operacao.md').read_text(encoding='utf-8');s=t.split('## 12. Agregado medido')[1].split('\n## ')[0];print(len(s.splitlines()))"
     ```
     → um número **menor ou igual a 120**. **Medido antes: o comando falha com `IndexError`,
     porque a seção não existe**.
  4. ```
     python .claude/tools/backlog.py check
     ```
     → `check: OK — nenhuma violação.`, exit **0**. **Medido antes: o mesmo** (`I-3`).
- **Pronto quando:** a seção `## 12. Agregado medido` existe com as dez subseções na ordem da §4,
  cada uma com a tabela ou com a linha `sem ocorrência no corpus medido`, e a seção inteira tem no
  máximo 120 linhas — o número que tem de existir ao final é, por dimensão, a contagem de
  ocorrências e a data da mais antiga e da mais recente.
  Por propriedade que a operação altera (`DPN-6`):
  - `agregado medido do planejador.retrato por dimensão` — dez subseções, uma por dimensão da §4, cada uma com o número de ocorrências, a mais antiga e a mais recente com data, a classe de erro dominante e um exemplo citado por identificador — no máximo 120 linhas, nenhum dado bruto — Verificação 1, 2 e 3.
  - `agregado medido do planejador.série de custo do planejamento` — a dimensão de custo declara o número de linhas, a mediana, o máximo e as datas da primeira e da última, e diz explicitamente o que uma linha só não permite afirmar — Verificação 2.
  - `agregado medido do planejador.série das rodadas de replanejamento` — as quatro contagens existem na dimensão do acionamento, e dimensão sem ocorrência aparece como linha explícita, nunca como silêncio — Verificação 2.
- **Fora do escopo desta tarefa:** a redação da especificação (`PLN-T6`) e o índice de documentos
  (`PLN-T7`).

### PLN-T2 — A norma da unidade de trabalho e dos limites [Opus · esforço high · classe redacao]
- **Status:** `ready` · 2026-09-21
- **Depende de:** `PLN-T1`
- **Objetivo:** `GOVERNANCA.md`, `.claude/global/CLAUDE.md` e `docs/RESIDENCIA_DOUTRINA.md` dizem
  que a unidade de trabalho é a materialização de uma operação do modelo e que nenhum percentual de
  ocupação nem teto de turnos dimensiona tarefa; uma guarda executável tranca a forma antiga.
- **Fundamento:** `DPN-2`, `DPN-3`, `DPN-9`; fatos `F-5`, `F-6`, `F-7`, `F-8`, `F-15`, `F-16`;
  censo da §7; invariantes `I-6`, `I-7`, `I-9`.
- **Operação do modelo:** `OP-2`
  - OP-2: O redator da norma troca a régua com que a doutrina dimensiona uma tarefa: aposenta o percentual de ocupação da janela e a tabela de tetos de turnos, institui a materialização de uma operação inteira do modelo como a unidade de trabalho, e levanta a guarda executável que impede a forma antiga de voltar às residências que ele acabou de editar.
  - precisa de: agregado medido do planejador — seção `## 12. Agregado medido` deste plano, inserida entre `## 11. Riscos` e `## Achados da execução`; dez subseções `### <n>. <dimensão>` na ordem da §4, com tabela de no máximo oito linhas cada e teto de 120 linhas para a seção inteira; só contagem, data, identificador e classe — nenhuma citação literal, nenhum trecho de plano, nenhuma linha de telemetria copiada; dimensão sem ocorrência traz a linha `sem ocorrência no corpus medido`; modelo de domínio e o papel que o escreve — `GOVERNANCA.md` §3.2, a subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras`, `.claude/tools/modelo.py` (`check` e `show`, `V1`..`V20`) e `.claude/agents/pantonic-model-designer.md`; premissa deste plano (`F-1`) e invariante dele (`I-4`) — `python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md` continua saindo `0`; citações históricas de medida — `GOVERNANCA.md:123`, `README.md:366`, `.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md` e `CHANGELOG.md:62,160` (`F-16`); invariante `I-7` — não se reescrevem em nenhuma tarefa deste plano; o limiar da janela de orquestração em `.claude/tools/ocupacao.py` também fica, por `DPN-3`, porque não dimensiona tarefa
- **Camada e fronteira:** doutrina (`GOVERNANCA.md`, cópia do kit das regras globais, mapa de
  residência) e um teste de invariância em `tests/`. Nenhum instrumento, nenhum agente, nenhuma
  skill.
- **Domínio:** *operação do modelo* — item `OP-<n>` da `### 1.2 Fluxo de operações` de um plano,
  que nomeia quem age, de que objetos precisa e que propriedades altera (`GOVERNANCA.md` §3.2).
  *Módulo coeso* — nome que o `P-0740` deu à unidade de trabalho; este card o define pela operação.
  *Classe* — o campo `classe <classe>` do cabeçalho do card, vocabulário
  `mecanica|implementacao|comportamental|investigacao|redacao`, lido por `rdo.py` e `backlog.py`.
- **Arquivos-alvo:**
  - `GOVERNANCA.md:91` (linha `| **Planejamento** |` da matriz de responsabilidades)
  - `GOVERNANCA.md:137` (bullet `- **A unidade de trabalho é o módulo coeso.**`)
  - `GOVERNANCA.md:165` (bullet `- **Diretriz de dimensionamento de tarefa (do planejador).**`)
  - `GOVERNANCA.md:177` (bullet `- **Orçamento de turnos por tarefa atômica — régua interna de quem dimensiona, nunca gate.**`, até a linha anterior ao bullet `- **Decisão que escolhe mecanismo de plataforma`)
  - `GOVERNANCA.md:420` (linha `| Item de backlog / história |` da tabela de §4)
  - `GOVERNANCA.md:433-439` (§4.1, os dois parágrafos)
  - `GOVERNANCA.md:542` (§4.3, "várias tarefas atômicas")
  - `GOVERNANCA.md:781` (G-PLANREADY, condição 2)
  - `GOVERNANCA.md:926` (G-MODULO, "(§3, *A unidade de trabalho é o módulo coeso*)")
  - `.claude/global/CLAUDE.md:31-36` (Regra 2, bullet `- **Capacidade**`)
  - `.claude/global/CLAUDE.md:49` (Regra 2, "várias tarefas atômicas")
  - `.claude/global/CLAUDE.md:139-143` (Regra 7, bullet `- **Orçamento por tarefa atômica**`)
  - `docs/RESIDENCIA_DOUTRINA.md:80` (linha `| 2.1 |`)
  - `docs/RESIDENCIA_DOUTRINA.md:142` (linha `| 7.7 |`)
  - `C:/Users/panta/.claude/CLAUDE.md` — **fora do repositório** (`DPN-12`); só os dois blocos nomeados no passo 14a, com o literal idêntico ao dos passos 10 e 12
  - `tests/test_doutrina_unidade.py` (novo)
- **Passos:**
  1. Em `GOVERNANCA.md:91`, substituir o trecho `decomposição em checklists de **tarefas atômicas fechadas** (G-PLANREADY, §7 item 11), cada uma com objetivo, arquivos-alvo, verificação e critério de pronto; **o dimensionamento de cada tarefa** sob a *Diretriz de dimensionamento de tarefa* desta seção — coesão, autossuficiência em contexto e ocupação estimada, exercidas no recorte, não publicadas no card;` pelo texto literal:
     `decomposição do modelo em **cards fechados, um por operação** (G-PLANREADY, §7 item 11; §3.2), cada um com objetivo copiado da operação, arquivos-alvo, verificação e critério de pronto derivado do estado final das propriedades que a operação altera; **o dimensionamento de cada tarefa** sob a *Diretriz de dimensionamento de tarefa* desta seção — uma operação inteira, coesão e autossuficiência em contexto, exercidas no recorte, não publicadas no card;`
     e, na mesma linha, substituir `o planejador não escreve a seção do modelo — devolve o dossiê de autoria junto com o plano gravado, e o de emenda em rodada de replanejamento` por
     `o planejador não escreve a seção do modelo — grava o esqueleto do plano sem a §1 e sem os cards, devolve o dossiê de autoria e só decompõe depois de a seção existir (Fase 3a e 3b do protocolo dele); em rodada de replanejamento devolve o de emenda. A lista `tarefas:` de cada operação é lastro, não modelo, e é ele quem a mantém depois da autoria`.
  2. Em `GOVERNANCA.md:137`, substituir a abertura `- **A unidade de trabalho é o módulo coeso.** O card despachado cobre uma **disciplina fechada** —` por
     `- **A unidade de trabalho é o módulo coeso, e módulo coeso é a materialização de uma operação do modelo** (§3.2). O card despachado cobre uma **disciplina fechada** —`
     e, no mesmo bullet, substituir `**(iii) divide-se por tema, nunca por volume** — o teto` por
     `**(iii) divide-se por tema, nunca por volume — e o tema é a operação:** um card por operação na autoria, card corretivo de replanejamento somado à operação que repara, e nunca uma operação partida em dois cards, porque operação que não cabe num card coeso é defeito do modelo (operação com propriedade embutida, §3.2) e volta ao modelador; o teto`.
  3. Em `GOVERNANCA.md:165-176`, substituir o bullet inteiro da diretriz pelo texto literal:
     ```
     - **Diretriz de dimensionamento de tarefa (do planejador).** Quem planeja delimita o escopo de
       cada tarefa, e a delimita para satisfazer três critérios: **(a)** materializar **uma operação
       inteira do modelo** (§3.2) — os objetos de que a operação precisa e as propriedades que ela
       altera são a fronteira do card, e o estado final dessas propriedades é o aceite dele;
       **(b)** caber num contexto **coerente e coeso** — o que não pertence à operação fica fora, e
       operação que não cabe num card coeso é defeito do modelo (operação com propriedade embutida),
       que volta ao modelador por dossiê, nunca partição do planejador; **(c)** ser
       **autossuficiente em contexto para a execução** — o dossiê entrega tudo de que a execução
       precisa, sem leitura ad hoc no meio dela. **Nenhum percentual de ocupação e nenhum número de
       turnos entram no dimensionamento:** a janela de 1M tokens deixou de limitar a granularidade
       (medido em 2026-09-18, `docs/CUSTO_DO_PICKUP.md` `## 13`) e o critério de admissão de matéria
       num card é coesão, não custo (diretiva do dono de 2026-09-19, `DM-30` do `P-0740`; aposentado
       o percentual em 2026-09-21, `DPN-3` do `P-0745`). O único número de ocupação que permanece
       governa a **janela de orquestração** (§4.3), nunca a tarefa. A diretriz é de quem dimensiona e
       só dele: quem executa não se ocupa de teto, de orçamento nem de ocupação — a responsabilidade
       do executor é executar a tarefa. Capacidade **nunca interrompe tarefa em curso** (§4.3);
       estouro de contexto numa tarefa é **registrado no corpo da tarefa** e vira insumo para revisão
       do modelo — sinal de operação mal recortada, não de card grande.
     ```
  4. Em `GOVERNANCA.md:177` até a linha anterior ao bullet `- **Decisão que escolhe mecanismo de plataforma`, substituir o bullet *Orçamento de turnos por tarefa atômica* inteiro — tabela e os três parágrafos que a seguem — pelo bullet literal:
     ```
     - **Classe do card — natureza, não teto.** A classe do cabeçalho
       (`mecanica|implementacao|comportamental|investigacao|redacao`, *Gramática do card* abaixo)
       declara a natureza do trabalho e calibra a profundidade de quem executa; **nenhum número de
       teto de turnos acompanha a classe**. A tabela de tetos por classe, calibrada em 2026-08-01
       sobre o recorte atômico numa janela de 200k, foi aposentada em 2026-09-21 junto com esse
       recorte (`docs/plans/P-0745-planejador-modelo-operacao.md`, `DPN-3`). O consumo continua
       medido em `docs/telemetria.tsv`, por tarefa, e se lê **em conjunto, na série**, nunca como
       aceite de uma entrega; o registro **qualitativo** — o que o número sozinho não diz — reside
       no card "Lições aprendidas na tarefa" do laudo de revisão. A classe é escolhida antes de
       delegar e fica registrada; trocá-la depois da entrega é falsificação da série.
     ```
  5. Em `GOVERNANCA.md:420`, substituir a linha pela literal:
     `| Item de backlog / história | **card** — a materialização de uma operação do modelo (§3.2), uma por contexto de execução (§4.3); quem a dimensiona é o **planejador**, sob a *Diretriz de dimensionamento de tarefa* (§3) |`
  6. Em `GOVERNANCA.md:433-439` (§4.1), substituir os dois parágrafos pelos literais:
     ```
     Todo procedimento mais complexo **invoca o agente de planejamento** para criar, a partir do
     modelo de domínio do plano (§3.2), um **checklist de cards — um por operação do modelo** —,
     descritivo o suficiente para que o agente de execução **não precise fazer buscas transversais**
     à tarefa (o custo de contexto da exploração é pago uma vez, no planejamento — com apoio do
     agente de coleta).

     Um card bem escrito contém: a operação que materializa (texto e contrato copiados do modelo),
     objetivo, arquivos-alvo (caminho exato), contratos/classes envolvidos, testes que devem passar
     ao final e critério de pronto derivado do estado final das propriedades que a operação altera.
     ```
  7. Em `GOVERNANCA.md:542`, substituir `várias tarefas atômicas` por `várias tarefas`.
  8. Em `GOVERNANCA.md:781`, substituir `**Tarefas `T1..Tn` sequenciais**, em ordem de dependência, cada uma com objetivo, "pronto quando" e modelo da fase. Uma tarefa por contexto.` por
     `**Tarefas `T1..Tn` sequenciais**, em ordem de dependência, **uma por operação do modelo** (§3.2), cada uma com objetivo copiado da operação, "pronto quando" derivado do estado final e modelo da fase. Uma tarefa por contexto.`
  9. Em `GOVERNANCA.md:926`, substituir `(§3, *A unidade de trabalho é o módulo coeso*)` por
     `(§3, *A unidade de trabalho é o módulo coeso* — e módulo coeso é a materialização de uma operação do modelo, §3.2)`.
  10. Em `.claude/global/CLAUDE.md:31-36`, substituir o bullet `- **Capacidade**` inteiro pelo literal:
      ```
      - **Capacidade** — mesmo coeso, o desempenho cai conforme o contexto enche. A capacidade não
        interrompe trabalho em curso: ela **dimensiona o trabalho antes de começar**. Quem planeja
        delimita cada tarefa como a **materialização de uma operação inteira do modelo do plano**,
        coesa e autossuficiente em contexto para a execução; **nenhum percentual de ocupação entra
        no dimensionamento** — a janela de 1M tokens deixou de limitar a granularidade, e o critério
        de admissão de matéria numa tarefa é coesão, não custo. A ocupação é aviso da janela de
        orquestração, entre tarefas, nunca critério de tarefa.
      ```
  11. Em `.claude/global/CLAUDE.md:49`, substituir `várias tarefas atômicas` por `várias tarefas`.
  12. Em `.claude/global/CLAUDE.md:139-143`, substituir o bullet `- **Orçamento por tarefa atômica**` inteiro pelo literal:
      ```
      - **Classe do card é natureza, não teto**: nenhum número de turnos ou de ocupação dimensiona a
        tarefa — a unidade é a operação do modelo do plano (`GOVERNANCA.md` §3, kit Pantonic).
        Estourar não é punição — é sinal de operação mal recortada (volta ao modelador) ou de método
        ruim (thrashing editar-testar-editar sem plano interno); reportar no handover, não
        simplesmente continuar.
      ```
  13. Em `docs/RESIDENCIA_DOUTRINA.md:80`, substituir `capacidade (~50% da janela)` por
      `capacidade (dimensionamento pela operação do modelo, sem percentual — `P-0745` `DPN-3`)`.
  14. Em `docs/RESIDENCIA_DOUTRINA.md:142`, substituir a linha inteira pela literal:
      `| 7.7 | **Orçamento por tarefa atômica: "~≤40 tool uses esperado"** | `Pantonic` — **aposentado** | **Prec-1 + Prec-2** — o teto único e a tabela de tetos por classe que o substituiu foram aposentados em 2026-09-21 (`GOVERNANCA.md` §3, *Classe do card — natureza, não teto*; `P-0745` `DPN-3`): a unidade de trabalho é a operação do modelo e nenhum número dimensiona tarefa | global e kit dizem o mesmo: classe é natureza, não teto; o número histórico fica só em `RECOMENDACOES_CONSUMO_GLOBAL.md` como medida de 2026-07 |`
  14a. No arquivo global do dono, `C:/Users/panta/.claude/CLAUDE.md`, aplicar as **mesmas duas**
      substituições já feitas na cópia do kit (`DPN-12`): o bullet `- **Capacidade**` da Regra 2 pelo
      literal do passo 10, e o bullet `- **Orçamento por tarefa atômica**` da Regra 7 pelo literal do
      passo 12. Os dois blocos de origem são idênticos byte a byte aos da cópia do kit (`F-15`), logo o
      literal é o mesmo e não se reescreve. **Nenhuma outra linha desse arquivo se toca** — em especial,
      os Controles 1.1 e 1.2 da Regra 1, que são matéria do `TK-68`.
  15. Criar `tests/test_doutrina_unidade.py` com o conteúdo literal:
      ```python
      """TR do P-0745 (PLN-T2..PLN-T5): a forma antiga da unidade de trabalho — percentual de
      ocupação, tabela de tetos, tarefa atômica — não volta às residências que o plano editou."""
      from pathlib import Path

      RAIZ = Path(__file__).resolve().parents[1]


      def _texto(rel: str) -> str:
          return (RAIZ / rel).read_text(encoding="utf-8")


      def test_governanca_dimensiona_pela_operacao_sem_percentual():
          t = _texto("GOVERNANCA.md")
          assert "50% de ocupação" not in t
          assert "Orçamento de turnos por tarefa atômica" not in t
          assert "materialização de uma operação do modelo" in t


      def test_global_claude_sem_percentual_nem_tarefa_atomica():
          t = _texto(".claude/global/CLAUDE.md")
          assert "50% de ocupação" not in t
          assert "tarefa atômica" not in t
          assert "tarefas atômicas" not in t
      ```
  16. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - Os literais dos passos 1-15 entram **como estão**; ajuste de quebra de linha para caber em
    ~100 colunas é permitido, mudança de palavra não é.
  - `GOVERNANCA.md:123` e `.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md` não se editam (`I-7`).
  - Não editar `.claude/tools/ocupacao.py`, `tests/test_ocupacao.py`, skills nem agentes (`I-8`).
  - No arquivo do dono, **só** os dois blocos do passo 14a. A guarda executável continua aferindo **apenas**
    arquivos do repositório — teste que leia caminho absoluto de usuário não roda em outra máquina —, e o
    arquivo do dono se afere pelas verificações 10 e 11 deste card.
  - Não commitar (`I-1`).
- **Não fazer:**
  - Não "aproveitar" para reescrever outras linhas de `GOVERNANCA.md` que citem tema, módulo ou
    ocupação além das listadas nos `Arquivos-alvo`: o censo da §7 é fechado.
  - Não tocar, no arquivo do dono, nada além dos dois blocos do passo 14a — os Controles 1.1 e 1.2 são do
    `TK-68`, e o arquivo não é alvo de nenhum outro card deste plano.
  - Não alterar a *Gramática do card* nem o vocabulário de classes.
- **Contingências:**
  1. Se uma âncora de linha dos `Arquivos-alvo` não casar com o texto declarado → localizar pelo
     literal citado no passo (`grep -n`) e seguir; se o literal não existir no arquivo → parar e
     sinalizar `blocked` razão `premissa`, com o literal na linha de retorno.
  2. Se `python -m pytest tests -q` reprovar em teste que este card não criou → parar e sinalizar
     `blocked` razão `premissa`, colando a linha de falha.
  3. Se um dos dois blocos do passo 14a não existir, literalmente, em `C:/Users/panta/.claude/CLAUDE.md`
     → **não parar**: deixar o arquivo como está, registrar na linha de retorno
     `contingência 3 acionada: literal ausente no CLAUDE.md global do dono — <qual bloco>` e seguir. O
     arquivo é do dono, está fora do repositório e pode ter mudado; a entrega do card não depende dele.
- **Testes:** `TR-DU-1` (`test_governanca_dimensiona_pela_operacao_sem_percentual`) e `TR-DU-2`
  (`test_global_claude_sem_percentual_nem_tarefa_atomica`), em `tests/test_doutrina_unidade.py`;
  suíte: `python -m pytest tests -q`.
- **Verificação:**

  1. ```
     grep -c 'tarefa atômica\|tarefas atômicas' GOVERNANCA.md
     ```
     → **1** (só a linha 123, medida histórica). **Medido antes: 7**.
  2. ```
     grep -c '50% de ocupação' GOVERNANCA.md
     ```
     → **0**. **Medido antes: 1**.
  3. ```
     grep -c 'Orçamento de turnos por tarefa atômica' GOVERNANCA.md
     ```
     → **0**. **Medido antes: 1**.
  4. ```
     grep -c 'materialização de uma operação do modelo' GOVERNANCA.md
     ```
     → **3** (bullet do módulo coeso, tabela de §4 e G-MODULO). **Medido antes: 0**.
  5. ```
     grep -c '50% de ocupação' .claude/global/CLAUDE.md
     ```
     → **0**. **Medido antes: 1**.
  6. ```
     grep -c 'tarefa atômica\|tarefas atômicas' .claude/global/CLAUDE.md
     ```
     → **0**. **Medido antes: 2**.
  7. ```
     grep -c '50% da janela' docs/RESIDENCIA_DOUTRINA.md
     ```
     → **0**. **Medido antes: 1**.
  8. ```
     python -m pytest tests -q
     ```
     → termina em `<N> passed`, com `<N>` igual ao total re-medido no despacho **mais 2**.
     **Medido antes: `262 passed`** (2026-09-21).
  9. ```
     python .claude/tools/backlog.py check
     ```
     → `check: OK — nenhuma violação.`, exit **0**. **Medido antes: o mesmo**.
  10. ```
      grep -c '50% de ocupação' 'C:/Users/panta/.claude/CLAUDE.md'
      ```
      → **0**. **Medido antes: 1**.
  11. ```
      grep -c 'tarefa atômica\|tarefas atômicas' 'C:/Users/panta/.claude/CLAUDE.md'
      ```
      → **0**. **Medido antes: 2**.
- **Pronto quando:** as onze verificações acima imprimem os valores declarados e nenhum arquivo fora
  dos `Arquivos-alvo` foi editado. As verificações 10 e 11 saem da contingência 3 se ela for acionada,
  e então a linha de retorno a nomeia.
  Por propriedade que a operação altera (`DPN-6`):
  - `norma da unidade de trabalho.régua de dimensionamento` — três critérios sem número — uma operação inteira do modelo, contexto coerente e coeso, autossuficiência em contexto; a tabela de tetos aposentada e a classe preservada como natureza do trabalho; o único limiar que fica é o da janela de orquestração, declarado fora do dimensionamento de tarefa — Verificação 2, 3, 4, 5 e 7.
  - `norma da unidade de trabalho.unidade nomeada na doutrina` — nenhuma dessas linhas nomeia a tarefa atômica como unidade: o módulo coeso ganha definição decidível — a materialização de uma operação do modelo — e a guarda executável afere a ausência por literal — Verificação 1, 4 e 6.
  - `guarda da forma antiga.cobertura das residências editadas` — um arquivo de teste novo, nascido com a norma e estendido pelas três operações seguintes, cobre por literal cada residência editada, e o total da suíte não reduz da referência datada `262 passed` — Verificação 8.
- **Fora do escopo desta tarefa:** a gramática do card e as skills (`PLN-T3`), o protocolo do
  planejador (`PLN-T4`), o gate do modelador e a tabela *Quem escreve* de §3.2 (`PLN-T5`), o
  `README.md` (`PLN-T7`).

### PLN-T3 — A gramática do card: a tarefa é a materialização de uma operação [Sonnet · esforço medium · classe redacao]
- **Status:** `ready` · 2026-09-21
- **Depende de:** `PLN-T2`
- **Objetivo:** a skill `diario-de-obras` apresenta o formato de uma tarefa como a materialização
  de uma operação do modelo, com o campo `Operação do modelo` no bloco de formato; as skills
  `modelo-por-fase` e `bootstrap-pantonic` e o agente `pantonic-fora-da-caixa` deixam de nomear a
  tarefa atômica.
- **Fundamento:** `DPN-2`, `DPN-6`, `DPN-9`; fatos `F-6`; censo da §7 (linhas das skills e do
  `pantonic-fora-da-caixa`).
- **Operação do modelo:** `OP-3`
  - OP-3: O redator da gramática reescreve o formato publicado de um card para que ele nasça como a materialização de uma operação, com o campo que copia o texto da operação e o contrato dos objetos de que ela precisa, e tira o nome da unidade antiga das demais definições de conduta que ainda o repetiam.
  - precisa de: norma da unidade de trabalho — residência única em `GOVERNANCA.md` §3 (matriz de responsabilidades, *A unidade de trabalho é o módulo coeso*, *Diretriz de dimensionamento de tarefa*, tabela da §4, §4.1, §4.3, G-PLANREADY e G-MODULO), espelhada em `.claude/global/CLAUDE.md` (Regras 2 e 7) e indexada em `docs/RESIDENCIA_DOUTRINA.md`; substituição de bloco nomeado, pelo texto literal dos passos da `PLN-T2`; a classe do cabeçalho do card permanece como natureza do trabalho, porque os parsers a leem; guarda da forma antiga — `tests/test_doutrina_unidade.py`, criado pela `PLN-T2` e estendido por `PLN-T3`, `PLN-T4` e `PLN-T5`; um teste por residência editada, com assertivas por literal sobre o texto do arquivo; piso de regressão como relação — o total de `python -m pytest tests -q` não reduz da referência datada `262 passed` (2026-09-21); modelo de domínio e o papel que o escreve — `GOVERNANCA.md` §3.2, a subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras`, `.claude/tools/modelo.py` (`check` e `show`, `V1`..`V20`) e `.claude/agents/pantonic-model-designer.md`; premissa deste plano (`F-1`) e invariante dele (`I-4`) — `python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md` continua saindo `0`
- **Camada e fronteira:** skills e um agente do kit; um teste somado ao arquivo criado pela
  `PLN-T2`. A subseção "Modelo de domínio (seção do plano)" da skill `diario-de-obras` **não se
  toca** (fronteira com o `P-0743`, §6).
- **Arquivos-alvo:**
  - `.claude/skills/diario-de-obras/SKILL.md:206-225` (heading `## Formato de uma tarefa atômica` e o bloco de formato)
  - `.claude/skills/modelo-por-fase/SKILL.md:24` (linha `| Execução (implementar/editar/testar/corrigir) |`)
  - `.claude/skills/bootstrap-pantonic/SKILL.md:34` (`checklists de tarefas atômicas`)
  - `.claude/agents/pantonic-fora-da-caixa.md:54` (`cada passo virando tarefa atômica candidata`)
  - `tests/test_doutrina_unidade.py` (criado pela `PLN-T2`; soma um teste)
- **Passos:**
  1. Em `.claude/skills/diario-de-obras/SKILL.md:206`, substituir o heading `## Formato de uma tarefa atômica` por `## Formato de uma tarefa` e inserir, logo abaixo dele e antes do bloco cercado, o parágrafo literal:
     `Uma tarefa é a **materialização de uma operação do modelo** (`GOVERNANCA.md` §3.2): o `Objetivo` copia o texto da operação, o campo `Operação do modelo` traz o texto e os contratos copiados (gramática em "Modelo de domínio (seção do plano)", acima), e o `Pronto quando` deriva do estado final das propriedades que a operação altera. Um card por operação; card corretivo (`T<n>a`) soma-se à operação do card que corrige.`
  2. No bloco cercado de formato (linhas 209-226), inserir, imediatamente depois da linha `- **Objetivo:** <uma frase>`, a linha literal:
     `- **Operação do modelo:** `OP-<n>` + os dois sub-bullets copiados (texto da operação; `precisa de:` com contrato)`
     e substituir a linha `- **Pronto quando:** <critério objetivo>` por
     `- **Pronto quando:** <por propriedade que a operação altera, o estado final da ### 1.3 e a verificação que o mede>`.
  3. Em `.claude/skills/modelo-por-fase/SKILL.md:24`, substituir `Uma tarefa atômica do diário de obras, TDD` por `Um card do diário de obras — a materialização de uma operação do modelo —, TDD`.
  4. Em `.claude/skills/bootstrap-pantonic/SKILL.md:34`, substituir `checklists de tarefas atômicas` por `checklists de cards, um por operação do modelo`.
  5. Em `.claude/agents/pantonic-fora-da-caixa.md:54`, substituir `cada passo virando tarefa atômica candidata` por `cada passo virando card candidato, a materializar por uma operação do modelo do plano que o adotar`.
  6. Apensar a `tests/test_doutrina_unidade.py` a função literal:
     ```python
     def test_skill_diario_formato_de_tarefa_pela_operacao():
         t = _texto(".claude/skills/diario-de-obras/SKILL.md")
         assert "## Formato de uma tarefa atômica" not in t
         assert "## Formato de uma tarefa\n" in t
         assert "materialização de uma operação do modelo" in t
     ```
  7. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - A subseção `### Modelo de domínio (seção do plano)` (linhas 175-204) não se edita.
  - Os literais dos passos 1-6 entram como estão.
  - Não commitar (`I-1`).
- **Não fazer:**
  - Não editar `.claude/agents/pantonic-fora-da-caixa.md:67` ("passos atômicos, cada um testável"):
    é passo de migração, outro sentido (§7).
  - Não editar `pantonic-executor.md:140`: o heading é a negação da forma antiga (§7).
  - Não regenerar `.claude/README.md`: nenhuma `description` muda neste card.
- **Contingências:**
  1. Se uma âncora de linha não casar com o texto declarado → localizar pelo literal (`grep -n`) e
     seguir; literal ausente → parar e sinalizar `blocked` razão `premissa`.
  2. Se `tests/test_doutrina_unidade.py` não existir → parar e sinalizar `blocked` razão
     `dependencia` (`PLN-T2`).
- **Testes:** `TR-DU-3` (`test_skill_diario_formato_de_tarefa_pela_operacao`); suíte:
  `python -m pytest tests -q`.
- **Verificação:**

  1. ```
     grep -c '^## Formato de uma tarefa atômica' .claude/skills/diario-de-obras/SKILL.md
     ```
     → **0**. **Medido antes: 1**.
  2. ```
     grep -c '^## Formato de uma tarefa$' .claude/skills/diario-de-obras/SKILL.md
     ```
     → **1**. **Medido antes: 0**.
  3. ```
     grep -c 'Operação do modelo' .claude/skills/diario-de-obras/SKILL.md
     ```
     → **um número maior em 2 que o medido no despacho** (o parágrafo novo e a linha do bloco de formato). **Medido antes: 1** (2026-09-21).
  4. ```
     grep -c 'tarefa atômica\|tarefas atômicas' .claude/skills/modelo-por-fase/SKILL.md .claude/skills/bootstrap-pantonic/SKILL.md .claude/agents/pantonic-fora-da-caixa.md
     ```
     → três linhas, todas terminando em `:0`. **Medido antes: `:1`, `:1`, `:1`**.
  5. ```
     python -m pytest tests -q
     ```
     → `<N> passed`, com `<N>` igual ao total re-medido no despacho **mais 1**. **Medido antes: `262 passed`** (2026-09-21, antes da `PLN-T2`).
  6. ```
     python .claude/tools/backlog.py check
     ```
     → `check: OK — nenhuma violação.`, exit **0**. **Medido antes: o mesmo**.
- **Pronto quando:** as seis verificações imprimem os valores declarados.
  Por propriedade que a operação altera (`DPN-6`):
  - `gramática do card.formato do card` — o bloco abre por *Formato de uma tarefa*, declara a tarefa como materialização de uma operação, traz o campo `Operação do modelo` com texto e contratos copiados, e o `Pronto quando` deriva do estado final de cada propriedade que a operação altera — Verificação 1, 2 e 3.
  - `gramática do card.unidade nomeada nas skills` — nenhum dos quatro a nomeia como unidade: todos falam em card materializado por uma operação do modelo; as ocorrências de outro sentido, como passo atômico de migração, ficam intactas — Verificação 4.
  - `guarda da forma antiga.cobertura das residências editadas` — um arquivo de teste novo, nascido com a norma e estendido pelas três operações seguintes, cobre por literal cada residência editada, e o total da suíte não reduz da referência datada `262 passed` — Verificação 5.
- **Fora do escopo desta tarefa:** o protocolo do planejador (`PLN-T4`) e a `description` dele,
  que é o que a região gerada de `.claude/README.md` repete.

### PLN-T4 — O protocolo do planejador: modelo primeiro, um card por operação [Opus · esforço xhigh · classe redacao]
- **Status:** `ready` · 2026-09-21
- **Depende de:** `PLN-T3`
- **Objetivo:** `.claude/agents/pantonic-planner.md` reescrito nas regiões que a `DPN-2`, a
  `DPN-3`, a `DPN-4`, a `DPN-5` e a `DPN-6` tocam — descrição, tese, protocolo com três saídas,
  Fase 3 partida em 3a e 3b, Fase 4 sem percentual, anatomia do card derivada do modelo, rodada de
  replanejamento com card corretivo somado à operação — e a região gerada de `.claude/README.md`
  regenerada.
- **Fundamento:** `DPN-2`..`DPN-6`, `DPN-9`; fatos `F-3`, `F-5`, `F-7`, `F-11`; censo da §7.
- **Operação do modelo:** `OP-4`
  - OP-4: O autor de papéis fecha o vão do protocolo de quem planeja: a sessão ganha uma terceira forma de terminar sem plano fechado, em que ele grava o esqueleto e devolve o pedido de autoria do modelo na própria linha de retorno, e a decomposição só começa depois de o modelo existir, com um card por operação, na ordem delas e sem nenhum percentual no recorte.
  - precisa de: gramática do card — `.claude/skills/diario-de-obras/SKILL.md`, seção *Formato de uma tarefa*, mais uma linha em `modelo-por-fase`, uma em `bootstrap-pantonic` e uma em `.claude/agents/pantonic-fora-da-caixa.md`; a subseção *Modelo de domínio (seção do plano)* da mesma skill **não se toca** (fronteira com o `P-0743`, §6); ocorrência de outro sentido — passo atômico de migração, escrita atômica em disco — fica intacta; norma da unidade de trabalho — residência única em `GOVERNANCA.md` §3 (matriz de responsabilidades, *A unidade de trabalho é o módulo coeso*, *Diretriz de dimensionamento de tarefa*, tabela da §4, §4.1, §4.3, G-PLANREADY e G-MODULO), espelhada em `.claude/global/CLAUDE.md` (Regras 2 e 7) e indexada em `docs/RESIDENCIA_DOUTRINA.md`; substituição de bloco nomeado, pelo texto literal dos passos da `PLN-T2`; a classe do cabeçalho do card permanece como natureza do trabalho, porque os parsers a leem; guarda da forma antiga — `tests/test_doutrina_unidade.py`, criado pela `PLN-T2` e estendido por `PLN-T3`, `PLN-T4` e `PLN-T5`; um teste por residência editada, com assertivas por literal sobre o texto do arquivo; piso de regressão como relação — o total de `python -m pytest tests -q` não reduz da referência datada `262 passed` (2026-09-21); modelo de domínio e o papel que o escreve — `GOVERNANCA.md` §3.2, a subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras`, `.claude/tools/modelo.py` (`check` e `show`, `V1`..`V20`) e `.claude/agents/pantonic-model-designer.md`; premissa deste plano (`F-1`) e invariante dele (`I-4`) — `python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md` continua saindo `0`
- **Camada e fronteira:** um agente do kit e a região gerada do índice do kit. O escopo do papel
  continua na matriz de `GOVERNANCA.md` §3 (`G-SCOPE`): este card muda o **como**, não amplia o
  papel. As entradas `RP-1`..`RP-7` e os doze itens de verificação da Fase 4 que não citam
  ocupação **permanecem** — são a memória medida do papel.
- **Domínio:** *SAÍDA* — uma das formas de encerrar uma sessão de planejamento sem plano fechado
  (hoje: campanha de investigação, rodada de decisões). *Lastro* — a lista `tarefas:` de uma
  operação (`DPN-5`).
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md:3` (`description`)
  - `.claude/agents/pantonic-planner.md:45-55` (seção `## Tese do papel`)
  - `.claude/agents/pantonic-planner.md:57-61` (abertura de `## Protocolo — cinco fases, com duas saídas antes do plano`)
  - `.claude/agents/pantonic-planner.md:158-200` (`### Fase 3 — Autoria`)
  - `.claude/agents/pantonic-planner.md:201-240` (`### Fase 4`, itens 1, 2 e 5)
  - `.claude/agents/pantonic-planner.md:354-360` (`### Fase 5`)
  - `.claude/agents/pantonic-planner.md:362-393` (`## Anatomia do card`)
  - `.claude/agents/pantonic-planner.md:395-424` (`## Rodada de replanejamento`)
  - `.claude/agents/pantonic-planner.md:426-440` (`## O que você NUNCA faz`)
  - `.claude/README.md` (região `<!-- kit:agents:begin -->`..`<!-- kit:agents:end -->`, regenerada)
  - `tests/test_doutrina_unidade.py` (soma um teste)
- **Passos:**
  1. Substituir a linha 3 (`description:`) pela literal:
     `description: Agente de planejamento Pantonic*. Usar para produzir PRD, Architecture, Spec e Sprint Plan, e para decompor o modelo de domínio de um plano em cards fechados — um por operação do modelo, autossuficientes para um executor frio. Grava o esqueleto do plano, devolve o dossiê de autoria do modelo e só decompõe depois de a seção do modelo existir. Não implementa código, não sonda codebase por conta própria, não escreve a seção do modelo e não publica plano com questão aberta.`
  2. Na seção `## Tese do papel`, acrescentar ao fim o parágrafo literal:
     `**O modelo é o contexto do planejador.** Você decompõe o que o modelador escreveu, e nada além: cada operação da `### 1.2` vira exatamente um card, na ordem das operações, com o id derivado do número dela (`<prefixo>-T<n>` para `OP-<n>`); o `Objetivo` é o texto da operação copiado; o `Pronto quando` é o estado final de cada propriedade que ela altera, com a verificação que o mede; a `Camada e fronteira` transcreve o contrato dos objetos de que ela precisa. Operação que não cabe num card coeso não se parte — é defeito do modelo (operação com propriedade embutida, `GOVERNANCA.md` §3.2) e volta ao modelador por dossiê. A lista `tarefas:` de cada operação é lastro, não modelo: você a mantém depois da autoria.`
  3. Substituir o heading `## Protocolo — cinco fases, com duas saídas antes do plano` por `## Protocolo — cinco fases, com três saídas antes do plano` e, no parágrafo seguinte, substituir `Uma sessão de planejamento termina de **três** formas, e só três: campanha de investigação (fase 1), rodada de decisões (fase 2) ou plano fechado registrado (fase 5).` por `Uma sessão de planejamento termina de **quatro** formas, e só quatro: campanha de investigação (fase 1), rodada de decisões (fase 2), dossiê de autoria do modelo (fase 3a) ou plano fechado registrado (fase 5).`
  4. Substituir `### Fase 3 — Autoria` inteira (do heading até a linha anterior a `### Fase 4`) pelo texto literal:
     ```
     ### Fase 3a — Esqueleto e dossiê (SAÍDA 3)

     Grave `docs/plans/P-NNNN-<slug>.md` **sem a §1 e sem a §5**, com o esqueleto fixo, nesta ordem:

     ```
     # P-NNNN — <título>            (cabeçalho: data de origem, iniciativa, plano de origem se derivado)
     ## 0. O problema, verbatim
     ## 1. Modelo conceitual          (VAZIA aqui: é do pantonic-model-designer, GOVERNANCA.md §3.2 —
                                       objetos com propriedades, fluxo de operações OP-<n>, estado inicial
                                       e final, registro de versões; nada carrega andamento; é o que o
                                       dono lê no Marco 1)
     ## 2. Fatos estabelecidos        (cada fato com a fonte: dossiê, doc §, decisão anterior)
     ## 3. Decisões                   (tabela id → valor → razão; toda decisão consumida por ≥ 1 card)
     ## 4. Invariantes de execução    (regras que valem para todos os cards — e que cada card repete
                                       na parte que o vincula: o executor não é obrigado a ler esta seção)
     ## 5. Tarefas                    (VAZIA aqui: a Fase 3b escreve um card por operação)
     ## 6. Ordem de execução          (grafo explícito: quem depende de quem; o que roda em paralelo)
     ## 7. Fora de escopo (explícito) (o que este plano não faz e onde isso mora, se mora)
     ## 8. Riscos                     (cada risco com resposta pré-decidida: o que o executor faz se ocorrer)
     ## 9. Achados da execução        (vazio; apensado por quem executa/orquestra)
     ```

     Então **pare** e devolva, na linha de retorno, o dossiê `Ato de modelo` de `autoria` — seis
     campos, fechados: `Plano` (o caminho gravado), `Ato: autoria`, `Motivo` (o pedido da §0),
     `Fato novo` (em uma frase, o que o plano entrega quando termina — a frase da Fase 0), `Restrição`
     (os invariantes da §4 que limitam o que o plano pode entregar; a convenção de lastro
     `tarefas: <prefixo>-T<n>` para `OP-<n>`) e `Devolver` (a §1 inteira e a linha da versão 1).
     **Nenhum agente aciona outro:** quem conduz a sessão despacha o modelador. Você não escreve uma
     linha da §1, nem "só para adiantar".

     ### Fase 3b — Decomposição (com a §1 na árvore)

     Retome — no mesmo contexto se ele conduz a sessão, em invocação nova se você foi chamado como
     subagente — lendo **só** a §1 gravada e o esqueleto. Escreva a §5: **um card por operação, na
     ordem das operações**, id `<prefixo>-T<n>` para `OP-<n>`. Por card: `Objetivo` = texto da
     operação copiado; campo `Operação do modelo` na gramática da skill `diario-de-obras` (texto
     copiado e `precisa de:` com contrato); `Camada e fronteira` = os contratos dos objetos de
     `precisa de:`; `Pronto quando` = uma linha por propriedade de `altera:`, com o estado final da
     `### 1.3` e o número da `Verificação` que o mede. Card cuja `Verificação` não mede alguma
     propriedade alterada está incompleto. Se ao decompor uma operação você concluir que ela não cabe
     num card coeso, **não a parta**: devolva o dossiê `Ato de modelo` de `autoria` de novo, com o
     achado em `Fato novo` — antes do Marco 1 a §1 é rascunho e o modelador a substitui no lugar
     (`GOVERNANCA.md` §3.2, *Rascunho antes do Marco 1*). Preencha a lista `tarefas:` de cada
     operação com o id do card, se a convenção não bastar.

     Regras de autoria que continuam valendo: cada card tem **exatamente um** entregável observável
     — a operação; toda sprint termina com a tarefa nomeada de **revisão do `README.md`** (G-README
     dever 2; dossiê inclui `pwsh .claude/checks/check-readme.ps1` e o veredito do dono como aceite),
     e essa tarefa materializa a operação do modelo que altera a documentação pública; decisão
     estruturante emite os cards de regularização da superfície inteira **no mesmo ato** (G-SURFACE);
     rebase que absorve fase de outro plano mapeia **tarefa a tarefa**, nunca fase a fase.
     ```
  5. Na Fase 4, item 1, substituir `id sequencial; `T1..Tn` em ordem de dependência com objetivo, "pronto quando" e modelo;` por `id sequencial; `T1..Tn` em ordem de dependência, um por operação, com objetivo copiado da operação, "pronto quando" derivado do estado final e modelo;`.
  6. Na Fase 4, item 5, substituir o item inteiro (de `5. **Dimensionamento**` até a linha anterior a `6. **Legibilidade para a revisão**`) pelo literal:
     ```
     5. **Dimensionamento** (diretriz de `GOVERNANCA.md` §3, exercida e não publicada): o card
        materializa **uma operação inteira do modelo**, é coeso e é autossuficiente em contexto.
        **Nenhum percentual de ocupação e nenhum número de turnos dimensionam o card** — a janela de
        1M deixou de limitar a granularidade, e o critério de admissão de matéria é coesão, não custo.
        A classe é natureza do trabalho e se escolhe antes de registrar; não carrega teto. Sinal de
        card errado não é tamanho: é **propriedade alterada que a operação não declara** (tema
        cruzado — volta ao modelador) ou **matéria que não altera propriedade nenhuma** ("aproveitando
        que estou aqui" — sai do card). Divide-se quando o card cruza **duas operações**, nunca quando
        cruza muitas regiões da mesma; o teto de regiões editadas do gate de delegação é limite de
        **tema**, e a contagem de regiões é medida informativa (`G-EXECREADY`, §7 item 12; `G-MODULO`,
        §7 item 19).
     ```
  7. Na Fase 5, substituir `Grave `docs/plans/P-NNNN-<slug>.md`, apense a linha ao `_INBOX.md`` por `Com a §1 e a §5 na árvore, rode `python .claude/tools/modelo.py check --plano <plano>` (exit `0`), apense a linha ao `_INBOX.md``.
  8. Na `## Anatomia do card`, substituir a linha `- **Objetivo:** uma frase; o entregável observável.` por `- **Objetivo:** o texto da operação que o card materializa, copiado da `### 1.2`; o entregável observável é a operação.` e a linha `- **Pronto quando:** critério binário, observável por quem revisa sem perguntar a quem executou.` por `- **Pronto quando:** uma linha por propriedade que a operação `altera:`, na forma `<objeto>.<propriedade> — <estado final copiado da ### 1.3> — Verificação <n>`; critério binário, observável por quem revisa sem perguntar a quem executou.`
  9. Na `## Rodada de replanejamento`, acrescentar ao passo 4 (`**Reescrever os cards**`) a frase literal: `Card corretivo novo (`T<n>a`, `T<n>b`) materializa a **mesma operação** do card que corrige, com o campo `Operação do modelo` copiado, e o id dele entra na lista `tarefas:` daquela operação — lastro que é seu (`GOVERNANCA.md` §3.2), não ato do modelador. Se a decisão nova muda o que o plano entrega, devolva também o dossiê `Ato de modelo` de `emenda`.`
  10. Em `## O que você NUNCA faz`, acrescentar dois bullets literais:
      `- Escrever uma linha da §1 — nem a tabela de objetos, nem uma operação, nem o estado final. É do modelador; o seu ato é o dossiê.`
      `- Partir uma operação em dois cards, ou fundir duas num card. Operação que não cabe é achado para o modelador; card que cruza duas operações é dois cards.`
  11. Rodar `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` para regenerar a região de agentes de `.claude/README.md`.
  12. Apensar a `tests/test_doutrina_unidade.py` a função literal:
      ```python
      def test_planner_decompoe_o_modelo_sem_percentual():
          t = _texto(".claude/agents/pantonic-planner.md")
          assert "atômic" not in t
          assert "50%" not in t
          assert "~80 linhas" not in t
          assert "SAÍDA 3" in t
          assert "Fase 3b" in t
      ```
  13. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - As entradas `RP-1`..`RP-7` e os itens 3, 4, 4a, 6, 7, 8, 9, 10, 11 e 12 da Fase 4 **não se
    editam**, salvo a renumeração que os passos exigirem (nenhuma).
  - Os literais dos passos 1-10 e 12 entram como estão; ajuste de quebra de linha para ~100 colunas
    é permitido.
  - A região gerada de `.claude/README.md` só muda pelo comando do passo 11.
  - Não commitar (`I-1`).
- **Não fazer:**
  - Não reescrever a Fase 0, a Fase 1 nem a Fase 2: o protocolo de intake, levantamento e decisões
    não muda.
  - Não encurtar o arquivo "para caber": nenhum número de linhas é critério deste card.
  - Não editar `pantonic-model-designer.md`: é a `PLN-T5`.
- **Contingências:**
  1. Se uma âncora de linha não casar → localizar pelo heading ou literal citado (`grep -n`) e
     seguir; literal ausente → parar e sinalizar `blocked` razão `premissa`.
  2. Se `kit_check.ps1 -Mode generate` sair diferente de `0` → colar a saída na linha de retorno e
     parar com `blocked` razão `premissa`.
  3. Se, depois do passo 12, algum teste de `tests/test_doutrina_unidade.py` criado pelas `PLN-T2` ou
     `PLN-T3` reprovar → parar e sinalizar `blocked` razão `premissa`, com a linha de falha.
- **Testes:** `TR-DU-4` (`test_planner_decompoe_o_modelo_sem_percentual`); suíte:
  `python -m pytest tests -q`.
- **Verificação:**

  1. ```
     grep -c 'atômic' .claude/agents/pantonic-planner.md
     ```
     → **0**. **Medido antes: 1**.
  2. ```
     grep -c '50%\|~80 linhas' .claude/agents/pantonic-planner.md
     ```
     → **0**. **Medido antes: 2**.
  3. ```
     grep -c 'SAÍDA 3\|Fase 3b' .claude/agents/pantonic-planner.md
     ```
     → **um número maior ou igual a 3**. **Medido antes: 0**.
  4. ```
     grep -c 'tarefas atômicas' .claude/README.md
     ```
     → **0**. **Medido antes: 1**.
  5. ```
     grep -c '^- \*\*Objetivo:\*\* o texto da operação' .claude/agents/pantonic-planner.md
     ```
     → **1**. **Medido antes: 0**.
  6. ```
     pwsh -NoProfile -File .claude/checks/check-readme.ps1
     ```
     → exit **0**, primeira linha começando por `check-readme: OK - 10 agente(s)`. **Medido antes: o mesmo**.
  7. ```
     python -m pytest tests -q
     ```
     → `<N> passed`, com `<N>` igual ao total re-medido no despacho **mais 1**. **Medido antes: `262 passed`** (2026-09-21, antes da `PLN-T2`).
  8. ```
     python .claude/tools/backlog.py check
     ```
     → `check: OK — nenhuma violação.`, exit **0**. **Medido antes: o mesmo**.
- **Pronto quando:** as oito verificações imprimem os valores declarados.
  Por propriedade que a operação altera (`DPN-6`):
  - `protocolo do planejador.saídas do protocolo` — **três** saídas antes do plano fechado; a terceira é o esqueleto gravado mais o dossiê de autoria do modelo devolvido na linha de retorno, para quem conduz a sessão despachar o modelador — Verificação 3.
  - `protocolo do planejador.momento da decomposição` — a fase de autoria se parte em duas — esqueleto e dossiê, depois decomposição sobre o modelo já na árvore —, com um card por operação, na ordem das operações e com o id derivado do número dela — Verificação 3 e 5.
  - `protocolo do planejador.régua no protocolo` — a conferência dimensiona por operação inteira, coesão e autossuficiência em contexto; nenhum percentual e nenhum sinal de volume sobrevivem, e operação que não cabe num card coeso volta ao modelador por dossiê em vez de ser partida — Verificação 1 e 2.
  - `protocolo do planejador.descrição pública do papel` — as duas anunciam decomposição do modelo em cards fechados, um por operação, e a parada que devolve o dossiê de autoria; a linha do índice sai da regeneração, nunca de edição à mão — Verificação 4 e 6.
  - `guarda da forma antiga.cobertura das residências editadas` — um arquivo de teste novo, nascido com a norma e estendido pelas três operações seguintes, cobre por literal cada residência editada, e o total da suíte não reduz da referência datada `262 passed` — Verificação 7.
- **Fora do escopo desta tarefa:** o gate do modelador (`PLN-T5`); a spec (`PLN-T6`); o
  `README.md` fora da região gerada de `.claude/README.md` (`PLN-T7`).

### PLN-T5 — O modelador diante do plano sem cards, e o lastro que é do planejador [Sonnet · esforço medium · classe redacao]
- **Status:** `ready` · 2026-09-21
- **Depende de:** `PLN-T4`
- **Objetivo:** `GOVERNANCA.md` §3.2 e `.claude/agents/pantonic-model-designer.md` publicam, nas
  duas pontas, que o modelador escreve a §1 sobre um plano ainda sem cards, que `V1` e `V3` são
  violações do lastro do planejador e voltam como saída literal, e que antes do Marco 1 a §1 é
  rascunho substituível no lugar.
- **Fundamento:** `DPN-4`, `DPN-5`, `DPN-7`, `DPN-9`; fatos `F-3`, `F-4`. A mudança de papel se
  publica nas duas pontas no mesmo card — a classe de defeito "metade de mudança de papel
  publicada" está medida em `docs/Entregas Aceitas/Entregas - P-0743.md`.
- **Operação do modelo:** `OP-5`
  - OP-5: O autor de papéis abre o portão do modelador para o plano que ainda não tem cards: a lista de tarefas de cada operação passa a ser lastro de quem planeja, as duas violações que ela dispara voltam medidas em vez de travar a devolução, e o modelo segue rascunho substituível no lugar até o primeiro aceite do dono.
  - precisa de: protocolo do planejador — `.claude/agents/pantonic-planner.md` (descrição, tese do papel, abertura do protocolo, Fases 3a e 3b, Fase 4, Fase 5, anatomia do card e rodada de replanejamento) e a região gerada `kit:agents` de `.claude/README.md`, produzida por `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` e nunca editada à mão; as entradas `RP-1`..`RP-7` e os itens de verificação que não citam ocupação permanecem — são a memória medida do papel; o escopo do papel continua na matriz de `GOVERNANCA.md` §3 (G-SCOPE); norma da unidade de trabalho — residência única em `GOVERNANCA.md` §3 (matriz de responsabilidades, *A unidade de trabalho é o módulo coeso*, *Diretriz de dimensionamento de tarefa*, tabela da §4, §4.1, §4.3, G-PLANREADY e G-MODULO), espelhada em `.claude/global/CLAUDE.md` (Regras 2 e 7) e indexada em `docs/RESIDENCIA_DOUTRINA.md`; substituição de bloco nomeado, pelo texto literal dos passos da `PLN-T2`; a classe do cabeçalho do card permanece como natureza do trabalho, porque os parsers a leem; guarda da forma antiga — `tests/test_doutrina_unidade.py`, criado pela `PLN-T2` e estendido por `PLN-T3`, `PLN-T4` e `PLN-T5`; um teste por residência editada, com assertivas por literal sobre o texto do arquivo; piso de regressão como relação — o total de `python -m pytest tests -q` não reduz da referência datada `262 passed` (2026-09-21); modelo de domínio e o papel que o escreve — `GOVERNANCA.md` §3.2, a subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras`, `.claude/tools/modelo.py` (`check` e `show`, `V1`..`V20`) e `.claude/agents/pantonic-model-designer.md`; premissa deste plano (`F-1`) e invariante dele (`I-4`) — `python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md` continua saindo `0`
- **Camada e fronteira:** doutrina (§3.2) e um agente do kit. `modelo.py`, `tests/test_modelo.py`
  e as fixtures **não se tocam**: o vocabulário `V1`..`V20` não muda, só quem responde por `V1` e
  `V3`.
- **Domínio:** *lastro* — a lista `tarefas:` de uma operação (`DPN-5`). *Rascunho* — a §1 entre a
  autoria e o Marco 1 (`DPN-7`).
- **Arquivos-alvo:**
  - `GOVERNANCA.md` §3.2, parágrafo `**Quem escreve.**` (âncora: linha que começa por `**Quem escreve.** Um agente único`) e as linhas `| modelador |` e `| planejador |` da tabela que o segue
  - `GOVERNANCA.md` §3.2, parágrafo `**Retroatividade.**` (o parágrafo novo entra imediatamente antes dele)
  - `.claude/agents/pantonic-model-designer.md:27-33` (o trecho do gate que começa em `Só três violações **não são suas**`)
  - `.claude/agents/pantonic-model-designer.md:52-55` (bullet `- **Autoria**`)
  - `.claude/agents/pantonic-model-designer.md:100` (bullet `- Não escreve fora da seção`)
  - `tests/test_doutrina_unidade.py` (soma um teste)
- **Passos:**
  1. Em `GOVERNANCA.md` §3.2, na tabela *Quem escreve*, substituir a célula da linha `| modelador |` por:
     `escreve a seção inteira, em todo ato, inclusive sobre plano que ainda não tem cards — na autoria preenche a lista `tarefas:` de cada operação pela convenção `<prefixo>-T<n>` para `OP-<n>`; devolve a seção literal e a linha do ato em `### 1.4 Registro de versões`; a lista `tarefas:` depois da autoria não é dele`
     e a célula da linha `| planejador |` por:
     `grava o esqueleto do plano sem a seção do modelo e sem os cards e devolve o dossiê `Ato de modelo` de autoria; com a seção na árvore, escreve um card por operação e **mantém a lista `tarefas:` de cada operação** — lastro, não modelo — na decomposição e em toda rodada de replanejamento; o plano não vai ao Marco 1 sem a seção escrita pelo modelador, sem os cards e sem `modelo.py check` exit `0``.
  2. Em `GOVERNANCA.md` §3.2, inserir imediatamente antes do parágrafo `**Retroatividade.**` os dois parágrafos literais:
     ```
     **Lastro.** A lista `tarefas:` de uma operação diz quais cards a materializam. É **lastro**, não
     modelo: não descreve o que o plano entrega, descreve quem o entrega. Por isso é a única linha
     da seção que não é do modelador depois da autoria — é do planejador, que a preenche na
     decomposição e a estende em rodada de replanejamento com o card corretivo. As violações `V1`
     (lista vazia) e `V3` (id que não existe) são do lastro: sobre plano ainda sem cards elas
     disparam por construção, o modelador as devolve como saída literal e quem conduz a sessão as
     roteia à decomposição.

     **Rascunho antes do Marco 1.** A regra de versão acima governa modelo **validado**. Entre a
     autoria e o primeiro `go`, a `## 1` é rascunho: o planejador que, ao decompor, encontra
     operação que não cabe num card coeso devolve novo dossiê de `autoria`, e o modelador substitui
     a versão 1 **no lugar**, sem bloco irmão e sem linha nova no registro. Versionar só começa no
     Marco 1.
     ```
  3. Em `.claude/agents/pantonic-model-designer.md:27-33`, substituir o trecho que começa em `Só três violações **não são suas**` e termina em `quem conduz a sessão as roteia para a tarefa que converte os cards.` pelo literal:
     `Só cinco violações **não são suas**: `V2`, `V4` e `V14`, que moram no card, e `V1` e `V3`, que moram no **lastro** — a lista `tarefas:` de cada operação, que é do planejador depois da autoria (`GOVERNANCA.md` §3.2, *Lastro*). Sobre um plano que ainda não tem cards, `V3` dispara por construção e não é defeito do seu ato. Havendo **apenas** essas, devolva o ato com a **saída literal** do `check`, nomeando as violações que ficaram: quem conduz a sessão as roteia à decomposição do planejador.`
  4. No bullet `- **Autoria**`, substituir `recebe o plano gravado sem a seção do modelo, no dossiê do planejador (`Ato: autoria`).` por `recebe o plano gravado sem a seção do modelo e, no fluxo normal, ainda sem os cards, no dossiê do planejador (`Ato: autoria`); preenche a lista `tarefas:` de cada `OP-<n>` pela convenção `<prefixo>-T<n>` que o dossiê declara. Segundo dossiê de autoria antes do Marco 1 substitui a versão 1 no lugar, sem versionar (`GOVERNANCA.md` §3.2, *Rascunho antes do Marco 1*).`
  5. Substituir o bullet `- Não escreve fora da seção `## 1. Modelo conceitual` — nenhuma outra linha do plano é sua.` por `- Não escreve fora da seção `## 1. Modelo conceitual` — nenhuma outra linha do plano é sua; e dentro dela a lista `tarefas:` de cada operação só é sua na autoria — depois é lastro do planejador.`
  6. Apensar a `tests/test_doutrina_unidade.py` a função literal:
     ```python
     def test_modelador_devolve_lastro_como_saida_literal():
         t = _texto(".claude/agents/pantonic-model-designer.md")
         assert "Só cinco violações" in t
         assert "`V1` e `V3`" in t
         g = _texto("GOVERNANCA.md")
         assert "**Lastro.**" in g
         assert "**Rascunho antes do Marco 1.**" in g
     ```
  7. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - `.claude/tools/modelo.py`, `tests/test_modelo.py` e `tests/fixtures/modelo/` não se editam.
  - A subseção "Modelo de domínio (seção do plano)" da skill `diario-de-obras` não se edita.
  - Os literais dos passos 1-6 entram como estão.
  - Não commitar (`I-1`).
- **Não fazer:**
  - Não mudar o número de violações do instrumento nem o texto de nenhuma `V<n>`.
  - Não regenerar `.claude/README.md`: a `description` do modelador não muda.
  - Não tocar `.claude/skills/scrum-master/SKILL.md`: o gate de despacho (`B3`) continua lendo
    `modelo.py check` exit `1` como bloqueio, e no despacho os cards já existem.
- **Contingências:**
  1. Se uma âncora não casar → localizar pelo literal (`grep -n`) e seguir; literal ausente → parar
     e sinalizar `blocked` razão `premissa`.
  2. Se `modelo.py check` sobre `docs/plans/P-0743-modelo-de-dominio.md` deixar de sair `0` depois
     das edições → parar e sinalizar `blocked` razão `premissa` (nenhum passo deste card deveria
     alcançar o instrumento).
- **Testes:** `TR-DU-5` (`test_modelador_devolve_lastro_como_saida_literal`); suíte:
  `python -m pytest tests -q`.
- **Verificação:**

  1. ```
     grep -c 'V3' .claude/agents/pantonic-model-designer.md
     ```
     → **um número maior ou igual a 2**. **Medido antes: 0**.
  2. ```
     grep -c 'Só cinco violações' .claude/agents/pantonic-model-designer.md
     ```
     → **1**. **Medido antes: 0**.
  3. ```
     grep -c 'Só três violações' .claude/agents/pantonic-model-designer.md
     ```
     → **0**. **Medido antes: 1**.
  4. ```
     grep -c '^\*\*Lastro\.\*\*\|^\*\*Rascunho antes do Marco 1\.\*\*' GOVERNANCA.md
     ```
     → **2**. **Medido antes: 0**.
  5. ```
     python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md
     ```
     → `modelo: OK — 13 operações, 9 objetos, 21 propriedades, 18 tarefas, versão 1`, exit **0**. **Medido antes: o mesmo** (invariância, `I-4`).
  6. ```
     python -m pytest tests -q
     ```
     → `<N> passed`, com `<N>` igual ao total re-medido no despacho **mais 1**. **Medido antes: `262 passed`** (2026-09-21, antes da `PLN-T2`).
  7. ```
     python .claude/tools/backlog.py check
     ```
     → `check: OK — nenhuma violação.`, exit **0**. **Medido antes: o mesmo**.
- **Pronto quando:** as sete verificações imprimem os valores declarados. É o gate do **Marco 2**:
  a orquestração abre o marco com `modelo.py show` sobre este plano.
  Por propriedade que a operação altera (`DPN-6`):
  - `gate do modelador.responsabilidade pelo lastro` — `V1` e `V3` são violações do lastro de quem planeja, voltam como saída literal medida, e a norma e a definição do papel dizem o mesmo nas duas pontas, fechadas no mesmo card — Verificação 1, 2, 3 e 4.
  - `gate do modelador.regra do rascunho antes do primeiro aceite` — entre a autoria e o primeiro `go` do dono a seção é rascunho e se substitui no lugar, sem bloco irmão e sem linha nova no registro de versões; versionar começa a partir do primeiro aceite — Verificação 4.
  - `guarda da forma antiga.cobertura das residências editadas` — um arquivo de teste novo, nascido com a norma e estendido pelas três operações seguintes, cobre por literal cada residência editada, e o total da suíte não reduz da referência datada `262 passed` — Verificação 6.
- **Fora do escopo desta tarefa:** a spec (`PLN-T6`) e o `README.md` (`PLN-T7`).

### PLN-T6 — A especificação do agente de planejamento [Opus · esforço xhigh · classe redacao]
- **Status:** `ready` · 2026-09-21
- **Depende de:** `PLN-T5`
- **Objetivo:** `docs/planner-spec.md` escrito, com uma seção por dimensão da §4, cada afirmação
  ancorada no agregado da `PLN-T1` (o antes) ou numa decisão `DPN-<n>` deste plano (o depois), e
  nenhuma afirmação sem uma das duas âncoras.
- **Fundamento:** `DPN-1`, `DPN-8`; fatos `F-9`, `F-14`. A lista de dimensões tem residência
  única na §4; este card a consome, não a reenuncia. Herda a `PLS-T2` do `P-0744`.
- **Operação do modelo:** `OP-6`
  - OP-6: O redator da especificação escreve, pela primeira vez, o documento que descreve a figura de quem planeja: uma seção por dimensão, cada afirmação ancorada no retrato medido do antes ou na decisão deste plano que instituiu o depois, e a última seção nomeando o que o corpus ainda não permite dizer.
  - precisa de: agregado medido do planejador — seção `## 12. Agregado medido` deste plano, inserida entre `## 11. Riscos` e `## Achados da execução`; dez subseções `### <n>. <dimensão>` na ordem da §4, com tabela de no máximo oito linhas cada e teto de 120 linhas para a seção inteira; só contagem, data, identificador e classe — nenhuma citação literal, nenhum trecho de plano, nenhuma linha de telemetria copiada; dimensão sem ocorrência traz a linha `sem ocorrência no corpus medido`; protocolo do planejador — `.claude/agents/pantonic-planner.md` (descrição, tese do papel, abertura do protocolo, Fases 3a e 3b, Fase 4, Fase 5, anatomia do card e rodada de replanejamento) e a região gerada `kit:agents` de `.claude/README.md`, produzida por `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` e nunca editada à mão; as entradas `RP-1`..`RP-7` e os itens de verificação que não citam ocupação permanecem — são a memória medida do papel; o escopo do papel continua na matriz de `GOVERNANCA.md` §3 (G-SCOPE); gate do modelador — `GOVERNANCA.md` §3.2 (tabela *Quem escreve* e dois parágrafos novos imediatamente antes de *Retroatividade*) e `.claude/agents/pantonic-model-designer.md` (gate de devolução e ato de autoria), nas duas pontas no mesmo card; `.claude/tools/modelo.py`, `tests/test_modelo.py` e as fixtures **não se tocam** — o vocabulário `V1`..`V20` não muda, só quem responde por `V1` e `V3`; norma da unidade de trabalho — residência única em `GOVERNANCA.md` §3 (matriz de responsabilidades, *A unidade de trabalho é o módulo coeso*, *Diretriz de dimensionamento de tarefa*, tabela da §4, §4.1, §4.3, G-PLANREADY e G-MODULO), espelhada em `.claude/global/CLAUDE.md` (Regras 2 e 7) e indexada em `docs/RESIDENCIA_DOUTRINA.md`; substituição de bloco nomeado, pelo texto literal dos passos da `PLN-T2`; a classe do cabeçalho do card permanece como natureza do trabalho, porque os parsers a leem
- **Camada e fronteira:** documentação em `docs/`. Nenhum código, nenhum teste, nenhum arquivo do
  kit.
- **Domínio:** *planejador* é o papel declarado na matriz de responsabilidades de `GOVERNANCA.md`
  §3 — quem produz os artefatos iniciais, decide rota e decompõe o modelo em cards, um por operação.
  *Rodada de replanejamento* é a forma da `G-REPLAN` (`GOVERNANCA.md` §7 item 17). Nenhum dos dois
  é redefinido por este documento: a especificação **descreve** a figura e **não** altera o escopo
  do papel nem o protocolo de conduta.
- **Arquivos-alvo:**
  - `docs/planner-spec.md` (novo)
- **Passos:**
  1. Criar `docs/planner-spec.md` com o título `# Especificação do agente de planejamento` e um
     cabeçalho de três linhas: a data; a frase que declara as duas fontes — a `## 12. Agregado
     medido` e a `## 3. Decisões` de `docs/plans/P-0745-planejador-modelo-operacao.md`; e a frase
     que declara que a figura descrita é a que existe **depois** das `PLN-T2`..`PLN-T5`.
  2. Abrir o documento com uma seção `## 0. O que esta especificação não é`, de três linhas: não é
     a residência do escopo do papel, que é a matriz de `GOVERNANCA.md` §3; não é a residência do
     protocolo de conduta, que é `.claude/agents/pantonic-planner.md`; é a descrição **medida** da
     figura, para quem precisa decidir quando acioná-la e quanto ela custa.
  3. Escrever, na ordem da §4 deste plano, uma seção `## <n>. <dimensão>` por dimensão, cada uma
     respondendo a pergunta que a §4 associa a ela.
  4. Em cada seção, ancorar toda afirmação numérica ou factual na subseção correspondente do
     agregado (citando a dimensão e o número) ou na decisão `DPN-<n>` que a instituiu (citando o
     id). Afirmação sem ancoragem não entra.
  5. Na seção 4 (operacionalização), descrever a operação como unidade nos termos da `DPN-2` e da
     `DPN-6`, e a parada da Fase 3a nos termos da `DPN-4`; onde o agregado tiver ocorrência de
     "duas mãos sobre a mesma região" ou "card de dois atos", citar como o antes.
  6. Na seção 5 (fronteira), escrever a fronteira com o consultor como o **espelho** da §4 de
     `docs/consultant-spec.md`, e a fronteira com o modelador como o espelho da tabela *Quem
     escreve* de `GOVERNANCA.md` §3.2; onde as duas divergirem, registrar a divergência na seção 10
     em vez de escolher um lado.
  7. Na seção 7 (custo), escrever o que a série de uma linha (`F-9`) permite — e só isso; o
     restante da seção nomeia o que seria preciso medir.
  8. Na seção 10, listar as perguntas que o corpus medido não responde, uma por linha, cada uma
     com o que seria preciso medir para respondê-la.
  9. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - Nenhuma afirmação sem ancoragem. Onde o agregado disser `sem ocorrência no corpus medido`, a
    seção correspondente diz isso e o que a `DPN-<n>` pertinente instituiu, e nada mais.
  - Não reabrir o escopo do papel nem o protocolo de conduta: as duas residências são citadas,
    nunca reenunciadas.
  - Não editar nenhum arquivo do kit nem de doutrina.
  - Não commitar (`I-1`).
- **Não fazer:**
  - Não editar `.claude/agents/pantonic-planner.md`, por mais que a redação sugira melhorias: o que
    a redação descobrir vira linha da seção 10.
  - Não copiar texto de `docs/consultant-spec.md`: o precedente dá o esqueleto, não o conteúdo.
  - Não inventar número: número que o agregado não tem não existe neste documento.
  - Não escrever a entrada do índice de documentos: é a `PLN-T7`.
- **Contingências:**
  1. Se a seção `## 12. Agregado medido` deste plano não existir ou estiver vazia → parar e
     sinalizar `blocked` razão `dependencia` (`PLN-T1`).
  2. Se uma dimensão tiver agregado vazio → a seção dela existe, com a frase
     `sem ocorrência no corpus medido em 2026-09-21`, o que a decisão pertinente instituiu e o
     ponteiro para a linha correspondente da seção 10. A seção não é omitida.
  3. Se a fronteira do passo 6 divergir do precedente → registrar a divergência na seção 10 e
     devolver, na linha de retorno, `contingência 3 acionada: divergência de fronteira com <papel>`.
- **Testes:** nenhum — a entrega é documento.
- **Verificação:**

  1. ```
     grep -c '^## ' docs/planner-spec.md
     ```
     → **11** — a seção `## 0` mais as dez dimensões. **Medido antes: o arquivo não existe**.
  2. ```
     grep -c 'DPN-' docs/planner-spec.md
     ```
     → **um número maior ou igual a 5** (uma âncora por decisão que a seção 4 e a 5 citam). **Medido antes: o arquivo não existe**.
  3. ```
     python -c "import pathlib;print(len(pathlib.Path('docs/planner-spec.md').read_text(encoding='utf-8').splitlines()))"
     ```
     → um número entre **150** e **500**. **Medido antes: o arquivo não existe**.
  4. ```
     python .claude/tools/backlog.py check
     ```
     → `check: OK — nenhuma violação.`, exit **0**. **Medido antes: o mesmo**.
- **Pronto quando:** `docs/planner-spec.md` existe com as onze seções, cada dimensão da §4 tem
  exatamente uma seção, e nenhuma seção carrega número que não esteja no agregado da `PLN-T1` nem
  regra que não esteja numa `DPN-<n>`.
  Por propriedade que a operação altera (`DPN-6`):
  - `especificação do planejador.existência do documento` — o documento existe, com uma seção por dimensão na ordem da §4 e uma seção de abertura que declara o que ele não é — nem residência do escopo do papel, nem do protocolo de conduta — Verificação 1 e 3.
  - `especificação do planejador.ancoragem das afirmações` — toda afirmação numérica ou factual aponta para a subseção do agregado que a mediu ou para a decisão `DPN-<n>` que a instituiu; afirmação sem uma das duas âncoras não entra, e o que o corpus não responde é nomeado em vez de adivinhado — Verificação 2.
- **Fora do escopo desta tarefa:** o índice de documentos e a revisão do README (`PLN-T7`).

### PLN-T7 — O índice de documentos e a revisão do README [Sonnet · esforço medium · classe implementacao]
- **Status:** `ready` · 2026-09-21
- **Depende de:** `PLN-T6`
- **Objetivo:** `docs/planner-spec.md` e este plano alcançáveis por `docs/DOC_MAP.md`; o `README.md`
  revisado contra o estado da árvore ao fim deste plano — as nove linhas de "tarefa atômica" da §7
  reescritas, a §3 sem a tabela de tetos — e `check-readme.ps1` verde.
- **Fundamento:** `DPN-1`, `DPN-2`, `DPN-3`; fatos `F-6`, `F-10`, `F-14`, `F-16`; invariantes
  `I-6`, `I-7`. É a tarefa de revisão de README que `G-README` dever 2 exige de toda sprint. Herda
  a `PLS-T3` do `P-0744`.
- **Operação do modelo:** `OP-7`
  - OP-7: O mantenedor acerta a documentação pública contra o estado da árvore ao fim da rota: a porta de entrada deixa de chamar a unidade de trabalho pelo nome antigo e perde o orçamento de turnos por classe, o índice de documentos passa a alcançar a especificação nova e este plano, e as frases que registram medida do passado ficam como estão.
  - precisa de: especificação do planejador — `docs/planner-spec.md` (novo): uma seção por dimensão da §4 deste plano, na ordem dela, aberta por `## 0. O que esta especificação não é`; descreve a figura **depois** das `PLN-T2`..`PLN-T5` (`DPN-8`); não é residência do escopo do papel (matriz de `GOVERNANCA.md` §3) nem do protocolo de conduta (`.claude/agents/pantonic-planner.md`); a lista de dimensões tem residência única na §4 e não se reenuncia; gramática do card — `.claude/skills/diario-de-obras/SKILL.md`, seção *Formato de uma tarefa*, mais uma linha em `modelo-por-fase`, uma em `bootstrap-pantonic` e uma em `.claude/agents/pantonic-fora-da-caixa.md`; a subseção *Modelo de domínio (seção do plano)* da mesma skill **não se toca** (fronteira com o `P-0743`, §6); ocorrência de outro sentido — passo atômico de migração, escrita atômica em disco — fica intacta; norma da unidade de trabalho — residência única em `GOVERNANCA.md` §3 (matriz de responsabilidades, *A unidade de trabalho é o módulo coeso*, *Diretriz de dimensionamento de tarefa*, tabela da §4, §4.1, §4.3, G-PLANREADY e G-MODULO), espelhada em `.claude/global/CLAUDE.md` (Regras 2 e 7) e indexada em `docs/RESIDENCIA_DOUTRINA.md`; substituição de bloco nomeado, pelo texto literal dos passos da `PLN-T2`; a classe do cabeçalho do card permanece como natureza do trabalho, porque os parsers a leem; citações históricas de medida — `GOVERNANCA.md:123`, `README.md:366`, `.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md` e `CHANGELOG.md:62,160` (`F-16`); invariante `I-7` — não se reescrevem em nenhuma tarefa deste plano; o limiar da janela de orquestração em `.claude/tools/ocupacao.py` também fica, por `DPN-3`, porque não dimensiona tarefa
- **Camada e fronteira:** documentação. Nenhum código, nenhum arquivo do kit.
- **Arquivos-alvo:**
  - `docs/DOC_MAP.md:157` (entrada de `docs/consultant-spec.md`, modelo da entrada nova)
  - `README.md:94` (glossário, `- **Tarefa atômica** —`)
  - `README.md:305` (§3, parágrafo `**Orçamento de turnos por classe de tarefa.**`, até o fim do parágrafo e da tabela que o segue, se houver)
  - `README.md:350` (§4, linha `| Planejamento (intelectual) |`)
  - `README.md:382` (§5, `decompõe a iniciativa em **tarefas atômicas**`)
  - `README.md:405` (§5, `Uma tarefa atômica bem escrita carrega, no mínimo:`)
  - `README.md:432` (§5, `a tarefa atômica em contexto limpo`)
  - `README.md:478` (§6, `**Passo 3 — escolher uma única tarefa atômica.**`)
  - `README.md:824-825` (§11, linhas `| `pantonic-planner` |` e `| `pantonic-executor` |`)
- **Passos:**
  1. Acrescentar a `docs/DOC_MAP.md` uma entrada `## docs/planner-spec.md (~<n> linhas)` na mesma
     forma da entrada de `docs/consultant-spec.md` da linha 157: o resumo em uma linha, a lista de
     seções e a linha `**Acesso:**` com o `Grep` de heading; `<n>` é a contagem real obtida por
     `python -c "import pathlib;print(len(pathlib.Path('docs/planner-spec.md').read_text(encoding='utf-8').splitlines()))"`.
  2. Acrescentar a `docs/DOC_MAP.md` uma entrada `## docs/plans/P-0745-planejador-modelo-operacao.md (~<n> linhas)` na mesma forma, com as seções `## 3. Decisões`, `## 7. Censo das formas reais`, `## 8. Tarefas` e `## 12. Agregado medido` e a linha `**Acesso:**` por `Grep pattern:"^### PLN-T2 "`.
  3. Em `README.md:94`, substituir `- **Tarefa atômica** — a unidade de execução, definida por uma propriedade: executável por um agente` pelo início literal `- **Card** — a unidade de execução: a materialização de **uma operação do modelo** do plano, executável por um agente` e ajustar o restante da entrada do glossário para que a propriedade que a define seja *uma operação inteira, coesa e autossuficiente em contexto*, sem percentual e sem teto.
  4. Em `README.md:305`, substituir o parágrafo `**Orçamento de turnos por classe de tarefa.**` — e a tabela de tetos que o segue, se existir — por um parágrafo literal:
     `**Classe do card — natureza, não teto.** A classe do cabeçalho (`mecanica|implementacao|comportamental|investigacao|redacao`) declara a natureza do trabalho e calibra a profundidade de quem executa; nenhum número de turnos ou de ocupação dimensiona a tarefa. A tabela de tetos por classe, calibrada em 2026-08-01 sobre o recorte atômico numa janela de 200k, foi aposentada em 2026-09-21 junto com esse recorte (`GOVERNANCA.md` §3; `P-0745`). O consumo continua medido em `docs/telemetria.tsv` e se lê na série, nunca como aceite.`
  5. Em `README.md:350`, substituir `decomposição em checklists de tarefas atômicas` por `decomposição do modelo em cards, um por operação`.
  6. Em `README.md:382`, substituir `decompõe a iniciativa em **tarefas atômicas**. Uma tarefa atômica é definida` por `decompõe o modelo em **cards, um por operação**. Um card é definido`.
  7. Em `README.md:405`, substituir `Uma tarefa atômica bem escrita carrega, no mínimo:` por `Um card bem escrito carrega, no mínimo:` e acrescentar à lista que o segue, como primeiro item, `a operação do modelo que materializa, com texto e contrato copiados`.
  8. Em `README.md:432`, substituir `a tarefa atômica em contexto limpo` por `o card em contexto limpo`.
  9. Em `README.md:478`, substituir `**Passo 3 — escolher uma única tarefa atômica.**` por `**Passo 3 — escolher um único card.**`.
  10. Em `README.md:824`, substituir `decompor um procedimento complexo em tarefas atômicas. Não implementa.` por `decompor o modelo de um plano em cards, um por operação; grava o esqueleto, devolve o dossiê de autoria do modelo e decompõe depois. Não implementa e não escreve o modelo.`; em `README.md:825`, substituir `Implementar **uma** tarefa atômica por contexto` por `Implementar **um** card — uma operação do modelo — por contexto`.
  11. Percorrer o `README.md` contra o estado da árvore ao fim deste plano, rodando
      `pwsh -NoProfile -File .claude/checks/check-readme.ps1` e fechando o que ele apontar.
  12. Devolver, na linha de retorno, a saída literal de `check-readme.ps1` — é o insumo do veredito
      do dono.
- **Restrições desta tarefa:**
  - `README.md:366` não se edita (`I-7`); `README.md:401` não se edita (outro sentido, §7).
  - Entrada do índice segue a forma da entrada vigente de `docs/consultant-spec.md`, incluindo a
    linha `**Acesso:**`. Não inventar forma nova.
  - Se `README.md` ou `docs/DOC_MAP.md` tiverem frase que conte itens de uma lista tocada, ela se
    fecha neste mesmo card (`I-6`).
  - Não editar `.claude/README.md` nem regenerar região alguma.
  - Não commitar (`I-1`).
- **Não fazer:**
  - Não alterar `docs/planner-spec.md`: está fechado pela `PLN-T6`.
  - Não alterar a frase de contagem de agentes de `README.md` §11: o número de agentes não muda.
  - Não reescrever seções do `README.md` além das linhas listadas: o censo da §7 é fechado.
- **Contingências:**
  1. Se `check-readme.ps1` sair diferente de `0` por item alheio a este plano → corrigir só o que
     a saída nomear e registrar na linha de retorno `contingência 1 acionada: <item>`.
  2. Se `docs/DOC_MAP.md` tiver frase que conta as entradas → atualizá-la no mesmo ato e registrar
     `contingência 2 acionada: frase de contagem do índice`.
  3. Se uma âncora de linha do `README.md` não casar → localizar pelo literal (`grep -n`) e seguir;
     literal ausente → parar e sinalizar `blocked` razão `premissa`.
- **Testes:** nenhum. O guarda executável é `check-readme.ps1`; o veredito do dono é gate de
  fechamento, não critério desta entrega.
- **Verificação:**

  1. ```
     grep -c '^## docs/planner-spec.md\|^## docs/plans/P-0745-planejador-modelo-operacao.md' docs/DOC_MAP.md
     ```
     → **2**. **Medido antes: 0**.
  2. ```
     grep -c 'Acesso:' docs/DOC_MAP.md
     ```
     → **um número maior em 2 que o medido no despacho**. **Medido antes: 9** (2026-09-21).
  3. ```
     grep -c 'tarefa atômica\|tarefas atômicas' README.md
     ```
     → **1** (só a linha 366, medida histórica). **Medido antes: 10**.
  4. ```
     grep -c 'Orçamento de turnos por classe de tarefa' README.md
     ```
     → **0**. **Medido antes: 1**.
  5. ```
     pwsh -NoProfile -File .claude/checks/check-readme.ps1
     ```
     → exit **0**, primeira linha começando por `check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s)`. **Medido antes: o mesmo**.
  6. ```
     python .claude/tools/backlog.py check
     ```
     → `check: OK — nenhuma violação.`, exit **0**. **Medido antes: o mesmo**.
- **Pronto quando:** as seis verificações imprimem os valores declarados e a saída literal de
  `check-readme.ps1` está na linha de retorno.
  Por propriedade que a operação altera (`DPN-6`):
  - `documentação pública do kit.unidade nomeada na porta de entrada` — o glossário abre por card, as demais linhas falam de card por operação, o parágrafo do orçamento vira a classe como natureza do trabalho, e `check-readme.ps1` continua saindo `0` — Verificação 3, 4 e 5.
  - `documentação pública do kit.alcance pelo índice de documentos` — duas entradas novas, na forma da entrada de `docs/consultant-spec.md`, cada uma com o resumo em uma linha, a lista de seções e a linha `**Acesso:**`, com a contagem real de linhas — Verificação 1 e 2.
- **Fora do escopo desta tarefa:** o veredito do dono sobre o README e sobre a especificação
  (Marco 3), registrado pela orquestração (`GOVERNANCA.md` §4.5); o documento de encerramento
  (skill `entrega-de-encerramento`), que a orquestração produz ao fechar o plano.

---

## 9. Ordem de execução

Fila única, sequencial.

```
PLN-T1 (agregado medido — o antes)
   └→ PLN-T2 (a norma: unidade e limites)
        └→ PLN-T3 (a gramática do card e as skills)
             └→ PLN-T4 (o protocolo do planejador)
                  └→ PLN-T5 (o modelador e o lastro)   ← Marco 2
                       └→ PLN-T6 (a especificação)
                            └→ PLN-T7 (índice e README)  ← Marco 3
```

`PLN-T1` vai primeiro porque mede o antes, e o antes deixa de existir na `PLN-T2`. `PLN-T2` precede
`PLN-T3` e `PLN-T4` porque a norma é a residência que as skills e o agente citam. `PLN-T5` fecha a
mudança de papel nas duas pontas e é o gate do Marco 2. `PLN-T6` depende de tudo que muda a figura.
`PLN-T7` carrega o tamanho real da spec e é a revisão de README que fecha toda sprint.

---

## 10. Fora de escopo (explícito)

| o que fica de fora | por quê | onde mora |
|---|---|---|
| A divergência entre o `CLAUDE.md` global do dono e a cópia do kit — os Controles 1.1 e 1.2 da Regra 1, 28 linhas que só o do dono tem | é matéria de sincronismo das duas cópias, alheia ao tema deste plano; os **dois blocos** que este plano reescreve são idênticos nas duas e entram na `PLN-T2` (`DPN-12`) | `TK-68` no diário |
| Fazer `.claude/sync-kit.ps1` projetar `.claude/global/` | mesma matéria: é a rota candidata 2 do tíquete, e decidir entre as três é ato próprio | `TK-68` no diário |
| A rodada de revisão de guardrails de `GOVERNANCA.md` §7.1, pendente desde 2026-08-08 | §7.1 é a porta de **saída** de guardrail e a revisão é tarefa nomeada com registro próprio; este plano **acrescenta** definição a `G-MODULO` e a `G-PLANREADY`, o que é matéria da autoria, não da revisão | `TK-67` no diário |
| O limiar da janela de orquestração (`.claude/tools/ocupacao.py`, `LIMIAR = 0.50` sobre 1M) | não é limite de tarefa; é o aviso `B2` do loop, e o dono não pediu que mudasse | `DPN-3`; `GOVERNANCA.md` §4.3 |
| Propagação do kit aos projetos derivados (`sync-kit.ps1`) | é iniciativa própria, com divergências de transporte a preservar por projeto | tíquete a abrir depois do Marco 3 |
| `pantonic-executor.md`, `pantonic-reviewer.md`, `pantonic-consultant.md`, `scrum-master`, `passagem-de-bastao` | já operam por módulo coeso e não citam percentual de tarefa (`F-13`) | — |
| As pendências `P-1`..`P-6` da entrega aceita do `P-0743` (fixtures `V15`..`V20`, premissa escrita no modelo, rótulo de telemetria por ato, atribuidor de autoria, provas de proveniência, fidelidade do conteúdo) | são do modelo e dos instrumentos, não do planejador; `P-2` (premissa escrita) é a mais próxima e continua sendo matéria do modelador | `docs/Entregas Aceitas/Entregas - P-0743.md`, *Pendências abertas* |
| A `MC-T5` do `P-0741` (veredito do dono sobre a entrega aceita) | é o gate de outro plano | `docs/plans/P-0741-modelo-conceitual.md` |
| Especificação dos demais agentes do kit | o dono nomeou um caso, o do planejamento | — |
| Migrar os planos do acervo para "um card por operação" | estão fechados; o que afirmam é verdadeiro sobre o que entregaram | — |

---

## 11. Riscos

| risco | resposta pré-decidida |
|---|---|
| O modelador devolve um número de operações diferente de sete, ou uma partição que não casa os sete cards da §8 | é o modelo que manda (`DPN-2`): quem conduz a sessão de autoria ajusta os cards ao modelo — funde ou parte cards **antes** de registrar, e a §8 sai com um card por operação. Depois do registro, é rodada de replanejamento |
| O dono dá `no-go` no Marco 1 porque não aceita aposentar o percentual e os tetos (`DPN-3`) | o plano vai a `cancelled`; o `P-0744` volta de `superseded` a `blocked`, com a razão original; nada foi editado, porque nenhuma tarefa roda antes do Marco 1 |
| `main` muda durante a execução (a outra janela) e o merge conflita em `GOVERNANCA.md`, no diário ou no `README.md` | é o desenho do dono (§0): a execução inteira corre em `plan/planner-modelo-escopo` e o merge é ato dele, com resolução de conflitos; nenhuma tarefa faz `merge` nem `rebase`. A superfície de conflito já foi **reduzida na origem**: a entrega solta do `P-0741`+`P-0743` virou o primeiro commit desta branch (`e4c1608`), que `main` alcança por `git merge --ff-only`, e a partir dali só este plano diverge |
| O dono veta, no Marco 1, editar o `CLAUDE.md` global dele (`DPN-12`) | a `PLN-T2` perde o passo 14a e as verificações 10 e 11, e nada mais muda — o card fecha só com a cópia do kit; a pendência volta a ser ato do dono, e a linha do `TK-68` a registra |
| A guarda de `tests/test_doutrina_unidade.py` quebra por reformulação legítima futura da doutrina | é o objetivo: quem reformular edita a guarda no mesmo card, como toda regra de conformance do kit |
| O agregado da `PLN-T1` não sustenta uma ou mais dimensões da spec | contingência 1 da `PLN-T1` e contingência 2 da `PLN-T6`: a dimensão existe, diz o que a decisão instituiu e o que faltaria medir |
| A revisão do `README.md` encontra frases fora do censo da §7 que ainda descrevem a forma antiga | contingência 1 da `PLN-T7` fecha só o que `check-readme.ps1` apontar; o resto vira `AE-<n>` para a fila pós-plano, nunca edição "de passagem" |

---

## Achados da execução

_(vazio; apensado por quem executa ou orquestra)_
