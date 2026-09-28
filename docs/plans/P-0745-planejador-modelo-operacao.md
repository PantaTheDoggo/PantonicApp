# P-0745 — O planejador diante do modelo: uma operação, um card

**Data:** 2026-09-21 · **Origem:** pedido do dono em 2026-09-21 (transcrito na §0) ·
**Plano de origem:** `P-0744` (classe B — este plano o sucede e herda as três tarefas dele, tarefa
a tarefa; `docs/plans/P-0744-spec-do-planejador.md` passa a `superseded`) e `P-0743` (`done`,
aceito em 2026-09-21 — é a premissa: o modelo de domínio e o modelador existem) ·
**Status:** `done` · 2026-09-22 · **Marco 1 aceito pelo dono**, sobre a versão 3 do modelo: o
plano está publicado e a fila alcança as sete tarefas. O `no-go` de 2026-09-21, sobre a versão 1,
não cancelou o plano — o conceito de modelo se revisou no `P-0746` e se reaplicou aqui, e o dono
mediu de novo em 2026-09-22 ·
**Prefixo das tarefas no diário:** `PLN-T<n>` ·
**Prefixo das decisões:** `DPN-<n>` · **Checagem de versão do kit:** modo hub — congelada em
`0.0.0` (`GOVERNANCA.md` §10), nada a comparar · **Branch de trabalho:**
`plan/planner-modelo-escopo` (criada em 2026-09-21 a pedido do dono; a execução inteira corre nela e
o merge em `main` é ato do dono ao fim, com resolução de conflitos). A entrega aceita do `P-0741`+`P-0743`,
que estava solta na árvore, é o **primeiro commit desta branch** (`e4c1608`, 84 arquivos) — `main` a alcança
por `git merge --ff-only e4c1608` sem arrastar este plano.
**Ordem de execução:** PLN-T1 → PLN-T2 → PLN-T3 → PLN-T4 → PLN-T4a → PLN-T5 → PLN-T5a → PLN-T6 →
PLN-T7 → PLN-T7a.
**Modelo de planejamento:** Fable 5.1 (modelo ativo da sessão de 2026-09-21, escolhido pelo dono).

**Marcos de validação pelo dono:**

| marco | o que o dono lê | veredito |
|---|---|---|
| **Marco 1** — **fechado em 2026-09-22** | a `## 1. Modelo conceitual` deste plano, escrita pelo modelador — os três objetos que o pedido da `## 0` nomeia, com o tipo de cada um, as sete propriedades que convergem e, em especial, o estado final de *agente de planejamento.régua com que ele dimensiona um card*, que aposenta o percentual de ocupação e a tabela de tetos | exercido duas vezes: `no-go` na versão 1, em 2026-09-21, que reautorou o modelo sem cancelar o plano e sem efeito sobre o `P-0744` — o desfecho real que o gate de dois ramos não previa; **`go` na versão 3**, em 2026-09-22, depois de o `P-0746` instituir o lastro obrigatório e de o adendo de objeto de escopo, externo e de medição redecompor o modelo. O plano sai de `blocked` para `ready` e a fila o alcança |
| **Marco 2** — **fechado em 2026-09-22** | `python .claude/tools/modelo.py show --plano docs/plans/P-0745-planejador-modelo-operacao.md` depois da `PLN-T5`, mais a *Diretriz de dimensionamento de tarefa* de `GOVERNANCA.md` §3 e a Fase 3 de `.claude/agents/pantonic-planner.md` | **`go` em 2026-09-22.** O modelo e o drift foram apresentados ao dono com as quatro alterações da versão 4 isoladas por `diff` entre a `## 1` e a `## 1A`, e com a nota de que `--drift` expõe só uma delas — as outras três moram no `contrato` e no estado inicial, que o comando não compara. Veredito verbatim: *"Aceito o drift. Pode continuar o plano"*. A versão 4 passa a **vigente** e a 3 a **obsoleta** (merge das versões, Diretriz de desenho do `P-0743` item 7: drift validado funde). A `PLN-T6` sai da espera: o passo 0 dela lê este veredito |
| **Marco 3** — **fechado em 2026-09-22** | `docs/planner-spec.md` depois da `PLN-T6`, o `README.md` revisado (`PLN-T7` e `PLN-T7a`) e o documento de encerramento (`docs/OPERACOES_AS_IS_P-0745.md`) | **`go` em 2026-09-22.** O as-is foi apresentado ao dono com os ganhos medidos, os seis degraus do padrão que a execução revelou — cada um com estado 🟢/🟡/🔴 — e as sete pendências. O dono questionou o número de pendências; a destrinchada mostrou **duas** de dívida real deste plano (as emendas de régua do `TK-72`, com texto pronto, e a cópia global do dono sem guarda executável), **uma** anterior ao plano (`TK-66`/`TK-74`), **duas** que são lacunas declaradas de propósito na `## 10` da especificação, e **duas** linhas cosméticas. Veredito verbatim: *"Pode concluir o plano"*. O plano fecha `done` 10/10 |

**Tarefas:** 10 — as sete da autoria (`PLN-T1`..`PLN-T7`) mais três cards corretivos, todos de
2026-09-22: `PLN-T4a`, somado à `OP-3` (`AE-13`/`AE-14`); `PLN-T5a`, somado à `OP-4`
(`AE-19`/`AE-20`); e `PLN-T7a`, somado à `OP-6` (`AE-23`/`AE-24`). Fila única, sequencial.

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

> **Como ler esta seção (Marcos 1 e 2).** Versão 4, vigente desde o aceite do dono no Marco 2 de
> 2026-09-22; o que cada versão mudou, e por que a anterior caiu, está em `### 1.4 Registro de
> versões`. A doutrina que a versão 3 instituiu em 2026-09-22 sobre o adendo de doutrina
> que o dono ditou naquele dia e que `GOVERNANCA.md` §3.2 já publica: dentro de objeto há agora
> **objeto de escopo**, o que o plano transforma e que por isso limita a atuação dele; **objeto
> externo**, o que gera insumo sem ser transformado; e **objeto de medição**, o que porta a
> propriedade pela qual a transformação se prova. Externo e medição são **constantes** — nenhuma
> operação altera propriedade deles. A versão 2 media cinco das seis operações alterando objeto
> constante, e foi substituída no lugar porque nunca vigorou: o Marco 1 não deu `go`. Aqui o
> **agente de planejamento** é o objeto de escopo — o plano existe para levá-lo de um estado
> anterior a um estado atualizado, e todas as seis operações agem sobre ele —; o **agente model
> designer** é externo — gera o insumo que caracteriza a transformação e o plano não visa
> alterá-lo —; e a **tarefa** é a medição — antes ela nasce sob os padrões obsoletos, depois sob
> os vigentes, e é essa diferença que prova que quem planeja mudou. O pedido transcrito na `## 0`
> descreve uma mudança de estado do framework que **já ocorreu**; este plano não a produz, ele
> leva as instruções que governam o planejamento a alcançá-la. **Todo** elemento aqui tem lastro
> declarado num trecho daquele pedido; o que o plano ainda entrega sem lastro nele reside em
> `## Requisitos secundários`, logo abaixo. A leitura gerada por
> `python .claude/tools/modelo.py show --plano docs/plans/P-0745-planejador-modelo-operacao.md`
> é esta mesma seção com o estágio derivado do andamento das tarefas. Os cards da `## 8` precedem
> o modelo (`DPN-10`), e por isso a numeração não alinha um para um: a `OP-5` se materializa em
> dois cards.

**Estado do modelo:** versão 4 · 2026-09-22 · autor: modelador · 3 objetos · 6 operações · 7 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem | lastro na §0 | tipo |
|---|---|---|---|---|---|---|
| agente de planejamento | a figura que recebe um pedido, decide a rota e devolve um plano decomposto em cards — e o conjunto de instruções que a governam, que é onde ela de fato existe | aproveitamento do aparato de modelo, régua com que ele dimensiona um card, unidade de trabalho que ele recorta, responsabilidade pelo lastro das operações, descrição pública da figura | residências da conduta: `.claude/agents/pantonic-planner.md`, em **dez regiões — e esta enumeração é a lista inteira**: descrição, fatos estáveis, tese do papel, abertura do protocolo, Fases 3a e 3b, Fase 4, Fase 5, anatomia do card, rodada de replanejamento e o que ele nunca faz. Quem edita o arquivo confronta as dez antes de publicar; região de conduta que não esteja aqui é achado para o modelador, não licença de autoria. A outra residência da conduta é a região gerada `kit:agents` de `.claude/README.md` — produzida por `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` e nunca editada à mão. Residências da régua e da unidade: `GOVERNANCA.md` §3 (matriz de responsabilidades, *A unidade de trabalho é o módulo coeso*, *Diretriz de dimensionamento de tarefa*, tabela da §4, §4.1, §4.3, G-PLANREADY e G-MODULO), `.claude/global/CLAUDE.md` (Regras 2 e 7) e a cópia do dono (`DPN-12`), `docs/RESIDENCIA_DOUTRINA.md`, as skills `diario-de-obras` (*Formato de uma tarefa*), `modelo-por-fase` e `bootstrap-pantonic`, `.claude/agents/pantonic-fora-da-caixa.md` e `README.md`. A régua **numérica** não reside em `.claude/agents/pantonic-planner.md` — ela é interna a `GOVERNANCA.md` §3 —, mas o arquivo **remete** a ela, e remissão a régua aposentada conta como residência para efeito do estado final: enquanto a linha de `## Fatos estáveis` que invoca a tabela de classes como régua numérica do papel estiver viva, a propriedade da régua não alcançou o estado final, ainda que toda residência numérica tenha sido reescrita. Residência da responsabilidade pelo lastro: `GOVERNANCA.md` §3.2 e `.claude/agents/pantonic-model-designer.md`, nas duas pontas no mesmo card. Residência da descrição: `docs/planner-spec.md` (novo), uma seção por dimensão da §4, na ordem dela e aberta por `## 0. O que esta especificação não é`. O censo linha a linha, com destino, é a §7; a classe do cabeçalho do card permanece como natureza do trabalho, porque os parsers a leem; ocorrência de outro sentido — escrita atômica em disco, passo atômico de migração — fica intacta; as entradas `RP-1`..`RP-7` e os itens de verificação que não citam ocupação permanecem, são a memória medida do papel; o escopo do papel continua na matriz de `GOVERNANCA.md` §3 (G-SCOPE), e a especificação não é residência nem do escopo nem do protocolo de conduta | OP-1 | *“elabore o plano para melhoramento do agente de planejamento”*; *“Avalie o projeto atual”* | escopo |
| agente model designer | o papel único que escreve todo ato sobre o modelo conceitual de um plano — e, por isso, quem gera o insumo de que quem planeja passa a depender | autoria exclusiva do modelo | não se transforma neste plano: a seção `## 1. Modelo conceitual` escrita por ele e o vocabulário de violações `V1`..`V21` de `.claude/tools/modelo.py` são o insumo que quem planeja consome, e permanecem como estão. `.claude/tools/modelo.py`, `tests/test_modelo.py` e as fixtures **não se tocam**. O que os cards deste plano publicam em `GOVERNANCA.md` §3.2 e em `.claude/agents/pantonic-model-designer.md` é a responsabilidade de **quem planeja** pelo lastro das operações, e nada além disso: o portão com que o modelador aceita ou recusa escrever a seção sobre um plano ainda sem cards não é objeto deste plano — alterá-lo é colateral e se escala | externo | *“agora com o conceito de modelo e do agente model designer estabelecido”* | externo |
| tarefa | a unidade de trabalho do loop: o card que um contexto executa inteiro, de ponta a ponta | padrão sob o qual ela nasce | nenhum card deste plano altera uma tarefa. O que se observa nela, antes e depois, é o padrão sob o qual ela nasce: o nome da unidade no cabeçalho e na doutrina, a régua que definiu o recorte e a presença do campo `Operação do modelo` com o texto e os contratos copiados. Os sete cards deste plano, escritos sob o padrão antigo, são o retrato do antes; a aferição do depois é o primeiro plano decomposto depois da `PLN-T4`, lido por `python .claude/tools/modelo.py show` | externo | *“a mudança da orientação de granularidade de tarefa, que não mais serão atividades atomicas, mas ativiidades de escopo maior, mantendo a coesão e coerência do objeto trabalhado”* | medição |

### 1.2 Fluxo de operações

**A. A régua e a unidade mudam onde a doutrina as guarda**

- **OP-1** — O redator da norma troca a régua com que quem planeja dimensiona um card: aposenta o percentual de ocupação da janela e a tabela de tetos de turnos, e institui no lugar deles a materialização de uma operação inteira do modelo, coesa e coerente com o objeto trabalhado.
  - `precisa de: tarefa, agente model designer` · `altera: agente de planejamento.régua com que ele dimensiona um card, agente de planejamento.unidade de trabalho que ele recorta` · `tarefas: PLN-T2` · `lastro: a revisão dos limites de janela; a mudança da orientação de granularidade de tarefa, que não mais serão atividades atomicas, mas ativiidades de escopo maior`
- **OP-2** — O redator da gramática reescreve a forma do card que quem planeja emite: ele passa a nascer como a materialização de uma operação, com o texto dela copiado e o contrato dos objetos de que ela precisa, e as demais definições de conduta deixam de chamar a unidade pelo nome antigo.
  - `precisa de: agente de planejamento, tarefa` · `altera: agente de planejamento.unidade de trabalho que ele recorta` · `tarefas: PLN-T3` · `lastro: mantendo a coesão e coerência do objeto trabalhado; que não mais serão atividades atomicas, mas ativiidades de escopo maior`

**B. O vão entre o modelo e quem planeja se fecha**

- **OP-3** — O autor de papéis fecha o vão do protocolo de quem planeja: a sessão ganha uma terceira forma de terminar sem plano fechado, com o esqueleto gravado e o pedido de autoria do modelo devolvido na linha de retorno; a decomposição só começa depois de o modelo existir, um card por operação, e o recorte deixa de se medir por percentual.
  - `precisa de: agente de planejamento, agente model designer` · `altera: agente de planejamento.aproveitamento do aparato de modelo, agente de planejamento.régua com que ele dimensiona um card, agente de planejamento.descrição pública da figura` · `tarefas: PLN-T4, PLN-T4a` · `lastro: elabore o plano para melhoramento do agente de planejamento; agora com o conceito de modelo e do agente model designer estabelecido`
- **OP-4** — O autor de papéis devolve a quem planeja o lastro que é dele: a lista de tarefas de cada operação do modelo passa a ser responsabilidade de quem decompõe o plano, e o que o instrumento mede nela volta medido para ele, em vez de travar a devolução de quem escreve o modelo.
  - `precisa de: agente de planejamento, agente model designer` · `altera: agente de planejamento.responsabilidade pelo lastro das operações` · `tarefas: PLN-T5, PLN-T5a` · `lastro: elabore o plano para melhoramento do agente de planejamento; agora com o conceito de modelo e do agente model designer estabelecido`

**C. A figura nova se descreve e chega a quem entra pela porta da frente**

- **OP-5** — O redator da especificação descreve a figura de quem planeja depois de medir como ela se comportou até aqui: uma seção por dimensão, cada afirmação ancorada no retrato medido ou na decisão que instituiu o depois, e a última nomeando o que o corpus ainda não permite dizer.
  - `precisa de: agente de planejamento, agente model designer` · `altera: agente de planejamento.descrição pública da figura` · `tarefas: PLN-T1, PLN-T6` · `lastro: Avalie o projeto atual; elabore o plano para melhoramento do agente de planejamento`
- **OP-6** — O mantenedor leva a unidade nova à porta de entrada do repositório: o glossário e as seções que ainda chamam a unidade de trabalho pelo nome antigo passam a falar do card que materializa uma operação, o orçamento de turnos por classe sai de onde quem chega o lia, e a figura de quem planeja passa a se anunciar lá pela decomposição do modelo.
  - `precisa de: agente de planejamento, tarefa` · `altera: agente de planejamento.unidade de trabalho que ele recorta, agente de planejamento.régua com que ele dimensiona um card, agente de planejamento.descrição pública da figura` · `tarefas: PLN-T7, PLN-T7a` · `lastro: que não mais serão atividades atomicas, mas ativiidades de escopo maior; a revisão dos limites de janela`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final | lastro na §0 |
|---|---|---|---|
| agente de planejamento.aproveitamento do aparato de modelo | o protocolo manda o modelo preceder a decomposição, mas prevê uma única parada — o plano já gravado —, e por isso quem planeja escreve cards que citam operações antes de elas existirem (`F-3`); o lado do executor já mudou, o do planejador só pela metade (`F-7`) | a sessão tem três saídas antes do plano fechado, e a terceira é o esqueleto gravado com o dossiê de autoria devolvido na linha de retorno; a decomposição só começa com o modelo na árvore, um card por operação, na ordem delas e com o id derivado do número da operação | *“agora com o conceito de modelo e do agente model designer estabelecido”* |
| agente de planejamento.régua com que ele dimensiona um card | ele dimensiona por percentual de ocupação da janela — 50%, tolerância 60% — e por uma tabela de tetos de turnos por classe calibrada em 2026-08-01 sobre uma janela de 200 mil tokens; os números vivem em cinco residências (`F-5`), e a janela real medida em 2026-09-18 é de um milhão (`F-7`); além das cinco, uma sexta residência **remete** aos números sem os repetir e o censo da §7 não a apanhou — `## Fatos estáveis` de `.claude/agents/pantonic-planner.md` declara que a régua numérica é a tabela de classes de `GOVERNANCA.md` §3, interna ao papel | ele dimensiona por três critérios sem número — uma operação inteira do modelo, contexto coerente e coeso, autossuficiência em contexto —, com a tabela de tetos aposentada e a classe preservada como natureza do trabalho; o único limiar que fica é o da janela de orquestração, declarado fora do dimensionamento de tarefa. E **nenhuma residência da conduta remete à tabela aposentada**: a linha de `## Fatos estáveis` de `.claude/agents/pantonic-planner.md` que hoje invoca a tabela de classes como a régua numérica interna ao papel ou morre, ou passa a dizer o que `GOVERNANCA.md` §3 diz desde a `PLN-T2` — a classe é natureza do trabalho e não carrega teto. Aposentar a tabela e deixar viva a linha que a invoca é o defeito de `F-5` repetido do lado do ponteiro: a régua numérica sobrevivendo na residência que ninguém reescreveu | *“assim como a revisão dos limites de janela”*; *“mantendo a coesão e coerência do objeto trabalhado”* |
| agente de planejamento.unidade de trabalho que ele recorta | ele recorta tarefas atômicas: vinte e uma linhas de doutrina viva nomeiam a unidade assim — `GOVERNANCA.md`, `README.md`, as duas cópias das regras globais, três skills e dois agentes (`F-6`), com destino linha a linha no censo da §7 —, e o bloco de formato que ele preenche abre por *Formato de uma tarefa atômica*, com objetivo em uma frase e critério objetivo solto, sem nada que ligue o card ao objeto trabalhado nem o campo `Operação do modelo` | ele recorta a materialização de uma operação inteira do modelo: nenhuma dessas linhas nomeia a tarefa atômica como unidade, e o bloco de formato abre por *Formato de uma tarefa*, declara o card como essa materialização, traz o campo `Operação do modelo` com o texto e os contratos copiados e faz o `Pronto quando` derivar do estado final de cada propriedade que a operação altera; as ocorrências de outro sentido ficam intactas | *“a mudança da orientação de granularidade de tarefa, que não mais serão atividades atomicas, mas ativiidades de escopo maior”*; *“mantendo a coesão e coerência do objeto trabalhado”* |
| agente de planejamento.responsabilidade pelo lastro das operações | a lista de tarefas de cada operação e o id de tarefa que ela cita são tratados como defeito da seção do modelo, e quem planeja não responde por eles em residência nenhuma (`F-4`) | a lista de tarefas de cada operação é lastro declarado de quem planeja, e as duas violações que ela dispara voltam medidas para ele; a norma e as duas definições de conduta dizem o mesmo nas duas pontas | *“elabore o plano para melhoramento do agente de planejamento”*; *“agora com o conceito de modelo e do agente model designer estabelecido”* |
| agente de planejamento.descrição pública da figura | a figura existe só na definição de conduta: `docs/planner-spec.md` não existe, enquanto a consultoria já tem especificação e entrada no índice (`F-14`), e a `description` do agente e a linha do índice do kit anunciam decomposição em tarefas atômicas fechadas | a figura tem especificação própria — uma seção por dimensão da §4, cada afirmação ancorada no retrato medido ou na decisão que a instituiu, e o que o corpus não responde nomeado em vez de adivinhado —, e a `description` do agente, a linha regenerada do índice do kit e o `README.md` anunciam a decomposição do modelo em cards | *“Avalie o projeto atual, e elabore o plano para melhoramento do agente de planejamento”* |
| tarefa.padrão sob o qual ela nasce | ela nasce sob os padrões obsoletos: chamada de tarefa atômica, recortada por percentual de ocupação e teto de turnos, sem o campo `Operação do modelo` que a ligue ao objeto trabalhado — os sete cards da `## 8` deste plano são esse retrato | ela nasce sob os padrões vigentes: um card por operação do modelo, recortado por coesão e coerência do objeto trabalhado, com o campo `Operação do modelo` trazendo o texto e os contratos copiados e o `Pronto quando` derivado do estado final das propriedades que a operação altera. Nenhuma operação deste plano a altera: a diferença entre as duas colunas é o que **prova** que quem planeja foi transformado | *“a mudança da orientação de granularidade de tarefa, que não mais serão atividades atomicas, mas ativiidades de escopo maior”* |
| agente model designer.autoria exclusiva do modelo | todo ato sobre a seção `## 1. Modelo conceitual` de um plano é dele, e só dele; é ele quem gera o insumo — a seção escrita — de que quem planeja passa a depender | o mesmo, inalterado: este plano não o transforma. O que o alteraria — o portão com que ele aceita ou recusa escrever sobre um plano ainda sem cards — é colateral, e se escala em vez de virar operação | *“agora com o conceito de modelo e do agente model designer estabelecido”* |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 4 | 2026-09-22 | vigente | modelador — conflito apurado pelo revisor da `PLN-T4` entre o texto do modelo e o que a entrega materializou. Duas células, nenhuma operação tocada: o contrato do `agente de planejamento` enumerava oito regiões de `.claude/agents/pantonic-planner.md` como residências da conduta e omitia `## Fatos estáveis` e `## O que você NUNCA faz`, esta editada pela própria `PLN-T4`; e o estado final de `agente de planejamento.régua com que ele dimensiona um card`, que dá a tabela de tetos por aposentada, não alcançava o ponteiro vivo a ela em `.claude/agents/pantonic-planner.md:36-37`. Validada no Marco 2 de 2026-09-22, com o `go` do dono — *“Aceito o drift. Pode continuar o plano”* —, e promovida a vigente nessa data |
| 3 | 2026-09-22 | obsoleta | modelador — emenda sob o adendo de doutrina do dono de 2026-09-22, publicado em `GOVERNANCA.md` §3.2: objeto de escopo, objeto externo e objeto de medição, com a coluna `tipo` na tabela de objetos. O agente de planejamento passa a ser o único objeto de escopo e as seis operações agem só sobre ele; a tarefa passa a medição e o agente model designer a externo, constantes que nenhuma operação altera. Caiu pelo aceite da versão 4 no Marco 2 de 2026-09-22 |
| 2 | 2026-09-22 | obsoleta | substituída no lugar pela versão 3, sem nunca ter vigorado — o Marco 1 não deu `go` depois dela. Medição que a derrubou: cinco das seis operações alteravam propriedade de objeto constante — `OP-1`, `OP-2` e `OP-6` sobre a tarefa, `OP-4` sobre o agente model designer, `OP-3` mista |
| 1 | 2026-09-21 | obsoleta | caiu no `no-go` do Marco 1 de 2026-09-21 — onze objetos, quatro deles sem lastro no enunciado e quatro que eram propriedade promovida a objeto, e vinte e um estados finais para um enunciado que especificou poucos (`docs/DIARIO_DE_OBRAS.md` › `## TK-69` §3); substituída no lugar, sem nunca ter vigorado |

---

## Requisitos secundários

> Residência do elemento sem lastro no pedido da `## 0` (`GOVERNANCA.md` §3.2; skill
> `diario-de-obras`, *Modelo de domínio (seção do plano)*). Nada aqui é contrato: são entregas
> que o agente julga necessárias para que o modelo não seja prejudicado, e a responsabilidade
> por elas é inteira dele. O dono as lê para saber que existem — não para aprová-las. As quatro
> saíram da `### 1.1` da versão 1 na reautoria de 2026-09-22, e continuam a ser entregues pelos
> cards que já as previam.

| requisito | por que o agente o julga necessário | quem responde |
|---|---|---|
| a seção `## 12. Agregado medido` deste plano, e o corpus fechado de oito fontes de onde ela sai (`PLN-T1`) | a descrição pública da figura só pode afirmar o que foi medido; sem o retrato do antes, cada afirmação da especificação seria adivinhação. O enunciado pediu a figura melhorada, não o retrato — o retrato é meio | agente |
| `tests/test_doutrina_unidade.py`, a guarda executável da forma antiga (`DPN-9`) | é a aferição do critério de fracasso que o dono nomeou — instrumento que ainda usa o conceito obsoleto —, e texto de doutrina sem guarda regride no primeiro transporte do kit. É aceite, não coisa que o plano trabalha | agente |
| as duas entradas novas de `docs/DOC_MAP.md` — a da especificação e a deste plano (`PLN-T7`) | o índice de documentos é como um agente frio alcança o que o plano publica | agente |
| as citações históricas de medida, preservadas intactas (`F-16`, `I-7`) | medida do passado é registro, não regra; reescrevê-las apagaria a evidência que justifica a troca de régua | agente |

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
| `GOVERNANCA.md:78,80` | §3, parágrafo de abertura (hierarquia qualidade > rota > custo): "orçamento de turnos" como instrumento de sustentabilidade e "caber no orçamento" | `PLN-T7` reescreve — sítio acrescentado ao censo pelo consultor em 2026-09-22 (`AE-10`), passo 4a |
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
| `C:/Users/panta/.claude/CLAUDE.md:78` | Regra 2, *Consequências práticas*, "várias tarefas atômicas" — espelho de `.claude/global/CLAUDE.md:49`, idêntico byte a byte (`F-15`) | `PLN-T2` reescreve ("várias tarefas") — passo 14b, linha acrescentada ao censo pelo consultor em 2026-09-22 (`AE-7`) |
| `C:/Users/panta/.claude/CLAUDE.md:167-171` | Regra 7, bullet "Orçamento por tarefa atômica" — **idêntico byte a byte** ao do kit | `PLN-T2` reescreve (`DPN-12`) |
| `C:/Users/panta/.claude/CLAUDE.md`, Controles 1.1 e 1.2 | 28 linhas que a cópia do kit não tem | **fica** — matéria alheia ao tema, tíquete `TK-68` |
| `.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md:4,71-72` | auditoria de 2026-07-08 | **fica** (`I-7`) |
| `docs/RESIDENCIA_DOUTRINA.md:80` | item 2.1 "capacidade (~50% da janela)" | `PLN-T2` reescreve a célula |
| `docs/RESIDENCIA_DOUTRINA.md:142` | item 7.7 "Orçamento por tarefa atômica" | `PLN-T2` reescreve a linha |
| `.claude/agents/pantonic-planner.md:3` | `description`: "tarefas atômicas fechadas" | `PLN-T4` reescreve |
| `.claude/agents/pantonic-planner.md:36-37` | `## Fatos estáveis`: "a régua numérica é a **tabela de classes** de `GOVERNANCA.md` §3" — remissão à tabela que a `PLN-T2` aposentou | `PLN-T4a` reescreve a segunda metade da frase — sítio acrescentado ao censo pelo consultor em 2026-09-22 (`AE-13`/`AE-14`); a varredura de 2026-09-21 buscou `atômic\|atomic` e `50%\|60%\|~80 linhas\|fatias verticais`, e "tabela de classes" não casa nenhum |
| `.claude/agents/pantonic-planner.md:237-238` | Fase 4 item 5: "~50% (...) 60%", "~80 linhas" | `PLN-T4` reescreve |
| `.claude/agents/pantonic-planner.md:187` | "fatias verticais finas primeiro" | `PLN-T4` reescreve |
| `.claude/agents/pantonic-model-designer.md:24-27` | `## Fatos estáveis`, frase **antecedente** do bullet do `exit 1`: "é da seção **toda** violação que o instrumento não indexa pelo `<ID>` de uma tarefa: as de `secao`, as de `OP-<n>` e as de `objeto`" — governa, e contradiz, o que a `PLN-T5` publicou cinco linhas adiante sobre `V1` e `V3`; e a lista `(V6, V7, V15, V17)` está incompleta (medido: `V21 objeto` existe e não é citado) | `PLN-T5a` reescreve — sítio acrescentado ao censo pelo consultor em 2026-09-22 (`AE-19`/`AE-20`); fora dos `Arquivos-alvo` de todo card até aqui |
| `.claude/agents/pantonic-executor.md:140` | heading "Módulo coeso, não fragmento atômico" | **fica** — é a negação |
| `.claude/agents/pantonic-fora-da-caixa.md:54` | "cada passo virando tarefa atômica candidata" | `PLN-T3` reescreve |
| `.claude/agents/pantonic-fora-da-caixa.md:67` | "passos atômicos, cada um testável" (passo de migração) | **fica** — outro sentido |
| `.claude/skills/diario-de-obras/SKILL.md:206` | heading "Formato de uma tarefa atômica" | `PLN-T3` reescreve |
| `.claude/skills/modelo-por-fase/SKILL.md:24` | "Uma tarefa atômica do diário de obras, TDD" | `PLN-T3` reescreve |
| `.claude/skills/bootstrap-pantonic/SKILL.md:34` | "checklists de tarefas atômicas" | `PLN-T3` reescreve |
| `.claude/README.md:20` | região gerada, `description` do planejador | `PLN-T4` regenera |
| `README.md:94,305,350,382,405,432,478,825,826` | glossário, §3, §4, §5, §6, §11 — re-ancoradas em 2026-09-22: as duas linhas da §11 estavam como `824,825` e o arquivo andou uma linha; `:94` escreve `Tarefa atômica` com maiúscula e `:382` é a única linha com **duas** ocorrências | `PLN-T7` reescreve |
| `README.md:121-124`, `:209,211`, `:308-309`, `:311-322`, `:324-326`, `:941-942`, `:946-947`, `:1032` | **oito sítios de doutrina viva** que defendem, definem ou pressupõem o teto de turnos por classe que o `README.md:306` declara aposentado: a entrada de glossário `- **Orçamento de turnos**`; o parágrafo da hierarquia qualidade > rota > custo, **espelho de `GOVERNANCA.md:78,80`**; o parágrafo do `≤30`; o `**Por quê.**` que defende o teto graduado; a premissa de estouro em `**Onde o gerente intervém.**`; a calibração de tetos como finalidade da série, em dois pontos; e a linha da tabela de trade-offs. Nenhum estava no censo | `PLN-T7a` reescreve — sítios acrescentados ao censo pelo consultor em 2026-09-22 (`AE-23`/`AE-24`), por varredura do **conceito** aposentado |
| `README.md:1036` | §11, tabela de trade-offs: "71 turnos e ~189 mil tokens numa única tarefa atômica" — **a mesma** medida histórica de `README.md:366`, em segunda residência | **fica** (`I-7`) — sítio acrescentado ao censo pelo consultor em 2026-09-22 (`AE-17`); é por ele que a Verificação 3 da `PLN-T7` espera **2**, não `1` |
| `README.md:366` | "uma única tarefa atômica chega a 71 turnos" (medida) | **fica** (`I-7`) |
| `README.md:401`, `GOVERNANCA.md:724` | "fatias verticais finas antes de camadas horizontais" (G-SLICE, §7 item 1: ordem de entregáveis, não tamanho de card) | **fica** — outro sentido |
| `CHANGELOG.md:62,160` | histórico de versões | **fica** (`I-7`) |
| `.claude/tools/ocupacao.py:83,86,128`, `tests/test_ocupacao.py:3` | limiar 0,50 da janela de orquestração | **fica** — `DPN-3`, fora do dimensionamento de tarefa |
| `backlog.py`, `rdo.py`, `telemetria.py`, `review_evidence.py`, `ARQUITETURA_PANTONICA.md:205`, `tests/test_backlog.py:1004`, `tests/test_rdo.py:9` | "escrita atômica" | **fica** — outro sentido |

---

## 8. Tarefas

### PLN-T1 — O agregado medido da atuação do planejador [Sonnet · esforço high · classe investigacao]
- **Status:** `done` · 2026-09-22
- **Objetivo:** a seção `## 12. Agregado medido` deste plano preenchida com uma tabela por dimensão
  da §4, dentro de 120 linhas, sem nenhum dado bruto — o retrato do planejador **antes** deste plano.
- **Fundamento:** `DPN-1`, `DPN-8`; fatos `F-2`, `F-9`. Herda o método da `PLS-T1` do `P-0744`
  com o corpus ampliado; o corpus é fechado e não se amplia.
- **Operação do modelo:** `OP-5`
  - OP-5: O redator da especificação descreve a figura de quem planeja depois de medir como ela se comportou até aqui: uma seção por dimensão, cada afirmação ancorada no retrato medido ou na decisão que instituiu o depois, e a última nomeando o que o corpus ainda não permite dizer.
  - precisa de: agente de planejamento — residências da conduta: `.claude/agents/pantonic-planner.md` (descrição, tese do papel, abertura do protocolo, Fases 3a e 3b, Fase 4, Fase 5, anatomia do card e rodada de replanejamento) e a região gerada `kit:agents` de `.claude/README.md` — produzida por `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` e nunca editada à mão. Residências da régua e da unidade: `GOVERNANCA.md` §3 (matriz de responsabilidades, *A unidade de trabalho é o módulo coeso*, *Diretriz de dimensionamento de tarefa*, tabela da §4, §4.1, §4.3, G-PLANREADY e G-MODULO), `.claude/global/CLAUDE.md` (Regras 2 e 7) e a cópia do dono (`DPN-12`), `docs/RESIDENCIA_DOUTRINA.md`, as skills `diario-de-obras` (*Formato de uma tarefa*), `modelo-por-fase` e `bootstrap-pantonic`, `.claude/agents/pantonic-fora-da-caixa.md` e `README.md`. Residência da responsabilidade pelo lastro: `GOVERNANCA.md` §3.2 e `.claude/agents/pantonic-model-designer.md`, nas duas pontas no mesmo card. Residência da descrição: `docs/planner-spec.md` (novo), uma seção por dimensão da §4, na ordem dela e aberta por `## 0. O que esta especificação não é`. O censo linha a linha, com destino, é a §7; a classe do cabeçalho do card permanece como natureza do trabalho, porque os parsers a leem; ocorrência de outro sentido — escrita atômica em disco, passo atômico de migração — fica intacta; as entradas `RP-1`..`RP-7` e os itens de verificação que não citam ocupação permanecem, são a memória medida do papel; o escopo do papel continua na matriz de `GOVERNANCA.md` §3 (G-SCOPE), e a especificação não é residência nem do escopo nem do protocolo de conduta; agente model designer — não se transforma neste plano: a seção `## 1. Modelo conceitual` escrita por ele e o vocabulário de violações `V1`..`V21` de `.claude/tools/modelo.py` são o insumo que quem planeja consome, e permanecem como estão. `.claude/tools/modelo.py`, `tests/test_modelo.py` e as fixtures **não se tocam**. O que os cards deste plano publicam em `GOVERNANCA.md` §3.2 e em `.claude/agents/pantonic-model-designer.md` é a responsabilidade de **quem planeja** pelo lastro das operações, e nada além disso: o portão com que o modelador aceita ou recusa escrever a seção sobre um plano ainda sem cards não é objeto deste plano — alterá-lo é colateral e se escala
- **Camada e fronteira:** nenhuma camada de produto é tocada. A tarefa lê o corpus e escreve
  **só** neste arquivo de plano.
- **Arquivos-alvo:**
  - `docs/plans/P-0745-planejador-modelo-operacao.md` — só este arquivo, e nele só a seção nova
    `## 12. Agregado medido`, inserida entre `## 11. Riscos` e `## Achados da execução`. As oito
    fontes do corpus (`Método de sondagem`) são **lidas, nunca escritas**, e por isso não são
    arquivo-alvo.
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
     python -c "import re,pathlib;t=pathlib.Path('docs/plans/P-0745-planejador-modelo-operacao.md').read_text(encoding='utf-8');m=re.search(r'^## 12\. Agregado medido\n.*?(?=^## )', t, re.M|re.S);print(len(m.group(0).splitlines()) if m else 0)"
     ```
     → um número **maior que 0 e menor ou igual a 120** — a seção inteira, do heading até a linha
     anterior ao próximo `## `. **Medido antes: 0** — a seção não existe.
     > **Reparo do consultor, 2026-09-22, com a tarefa já em `review` (`AE-2`).** O comando
     > publicado originalmente partia o arquivo pelo literal `## 12. Agregado medido`, que ocorre
     > **primeiro dentro do próprio card** (`Objetivo` e `Formato do agregado`): media prosa do
     > card, nunca a seção. Medido: devolve **6** no arquivo entregue e **73** no arquivo de
     > `d75e7a6` — nunca o `IndexError` que o card deduzia, porque o literal já existia no card
     > antes da entrega. O **critério não mudou** (≤ 120); mudou só o instrumento que o afere,
     > agora ancorado no heading em início de linha. Medições deste reparo, rodadas: **106** no
     > arquivo entregue, **0** no arquivo de `d75e7a6`. O número que o executor reportou na linha
     > de retorno (6) é o da forma antiga.
  4. ```
     python .claude/tools/backlog.py check
     ```
     → `check: OK — nenhuma violação.`, exit **0**. **Medido antes: o mesmo** (`I-3`).
- **Pronto quando:** a seção `## 12. Agregado medido` existe com as dez subseções na ordem da §4,
  cada uma com a tabela ou com a linha `sem ocorrência no corpus medido`, e a seção inteira tem no
  máximo 120 linhas — o número que tem de existir ao final é, por dimensão, a contagem de
  ocorrências e a data da mais antiga e da mais recente.
  Por propriedade que a operação altera (`DPN-6`):
  - `agente de planejamento.descrição pública da figura` — a parcela desta tarefa: o retrato medido do antes, de que a descrição depende; a propriedade só alcança o estado final na `PLN-T6` — Verificação 1, 2 e 3.
  - As demais entregas desta tarefa são **requisito secundário** (`## Requisitos secundários`), não propriedade do modelo: a seção `## 12. Agregado medido` e o corpus fechado de onde ela sai.
- **Fora do escopo desta tarefa:** a redação da especificação (`PLN-T6`) e o índice de documentos
  (`PLN-T7`).

### PLN-T2 — A norma da unidade de trabalho e dos limites [Opus · esforço high · classe redacao]
- **Status:** `done` · 2026-09-22
- **Depende de:** `PLN-T1`
- **Objetivo:** `GOVERNANCA.md`, `.claude/global/CLAUDE.md` e `docs/RESIDENCIA_DOUTRINA.md` dizem
  que a unidade de trabalho é a materialização de uma operação do modelo e que nenhum percentual de
  ocupação nem teto de turnos dimensiona tarefa; uma guarda executável tranca a forma antiga.
- **Fundamento:** `DPN-2`, `DPN-3`, `DPN-9`; fatos `F-5`, `F-6`, `F-7`, `F-8`, `F-15`, `F-16`;
  censo da §7; invariantes `I-6`, `I-7`, `I-9`.
- **Operação do modelo:** `OP-1`
  - OP-1: O redator da norma troca a régua com que quem planeja dimensiona um card: aposenta o percentual de ocupação da janela e a tabela de tetos de turnos, e institui no lugar deles a materialização de uma operação inteira do modelo, coesa e coerente com o objeto trabalhado.
  - precisa de: tarefa — nenhum card deste plano altera uma tarefa. O que se observa nela, antes e depois, é o padrão sob o qual ela nasce: o nome da unidade no cabeçalho e na doutrina, a régua que definiu o recorte e a presença do campo `Operação do modelo` com o texto e os contratos copiados. Os sete cards deste plano, escritos sob o padrão antigo, são o retrato do antes; a aferição do depois é o primeiro plano decomposto depois da `PLN-T4`, lido por `python .claude/tools/modelo.py show`; agente model designer — não se transforma neste plano: a seção `## 1. Modelo conceitual` escrita por ele e o vocabulário de violações `V1`..`V21` de `.claude/tools/modelo.py` são o insumo que quem planeja consome, e permanecem como estão. `.claude/tools/modelo.py`, `tests/test_modelo.py` e as fixtures **não se tocam**. O que os cards deste plano publicam em `GOVERNANCA.md` §3.2 e em `.claude/agents/pantonic-model-designer.md` é a responsabilidade de **quem planeja** pelo lastro das operações, e nada além disso: o portão com que o modelador aceita ou recusa escrever a seção sobre um plano ainda sem cards não é objeto deste plano — alterá-lo é colateral e se escala
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
  - `C:/Users/panta/.claude/CLAUDE.md` — **fora do repositório** (`DPN-12`); só os blocos nomeados nos passos 14a e 14b, com o literal idêntico ao dos passos 10, 11 e 12
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
      literal é o mesmo e não se reescreve. **Nenhuma outra linha desse arquivo se toca além da do passo
      14b** — em especial, os Controles 1.1 e 1.2 da Regra 1, que são matéria do `TK-68`.
  14b. Ainda em `C:/Users/panta/.claude/CLAUDE.md`, na **Regra 2**, parágrafo `**Consequências
      práticas:**` (linha **78**, medida em 2026-09-22), substituir `o contexto atravessa várias
      tarefas atômicas` por `o contexto atravessa várias tarefas`. É a **mesma** substituição do
      passo 11, aplicada ao parágrafo espelho: fora dos Controles 1.1 e 1.2 as duas cópias são
      idênticas byte a byte (`F-15`), e depois deste passo o parágrafo volta a fechar com o do kit,
      quebra de linha inclusive. **Não é matéria nova** — é a terceira ocorrência da mesma forma
      antiga que os passos 10, 11 e 12 aposentam, omitida do censo da §7 na autoria e acrescentada
      a ele em 2026-09-22 (`AE-7`). Este passo é na **Regra 2**: os Controles 1.1 e 1.2 da Regra 1
      seguem intocados.
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
  - No arquivo do dono, **só** os blocos dos passos 14a e 14b. A guarda executável continua aferindo **apenas**
    arquivos do repositório — teste que leia caminho absoluto de usuário não roda em outra máquina —, e o
    arquivo do dono se afere pelas verificações 10 e 11 deste card.
  - Não commitar (`I-1`).
- **Não fazer:**
  - Não "aproveitar" para reescrever outras linhas de `GOVERNANCA.md` que citem tema, módulo ou
    ocupação além das listadas nos `Arquivos-alvo`: o censo da §7 é fechado.
  - Não tocar, no arquivo do dono, nada além dos blocos dos passos 14a e 14b — os Controles 1.1 e 1.2 são do
    `TK-68`, e o arquivo não é alvo de nenhum outro card deste plano.
  - Não alterar a *Gramática do card* nem o vocabulário de classes.
- **Contingências:**
  1. Se uma âncora de linha dos `Arquivos-alvo` não casar com o texto declarado → localizar pelo
     literal citado no passo (`grep -n`) e seguir; se o literal não existir no arquivo → parar e
     sinalizar `blocked` razão `premissa`, com o literal na linha de retorno.
  2. Se `python -m pytest tests -q` reprovar em teste que este card não criou → parar e sinalizar
     `blocked` razão `premissa`, colando a linha de falha.
  3. Se um dos blocos dos passos 14a e 14b não existir, literalmente, em `C:/Users/panta/.claude/CLAUDE.md`
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
      → **0**, depois dos passos 14a **e** 14b. **Medido antes de tudo: 2.** **Medido em 2026-09-22,
      com o 14a aplicado e o 14b ainda não: 1** — a única ocorrência remanescente é a da linha 78,
      que o passo 14b trata, e foi esse estado que devolveu o card `blocked` (`AE-6`, `AE-7`).
- **Pronto quando:** as onze verificações acima imprimem os valores declarados e nenhum arquivo fora
  dos `Arquivos-alvo` foi editado. As verificações 10 e 11 saem da contingência 3 se ela for acionada,
  e então a linha de retorno a nomeia.
  Por propriedade que a operação altera (`DPN-6`):
  - `agente de planejamento.régua com que ele dimensiona um card` — ele dimensiona por três critérios sem número — uma operação inteira do modelo, contexto coerente e coeso, autossuficiência em contexto —, com a tabela de tetos aposentada e a classe preservada como natureza do trabalho; o único limiar que fica é o da janela de orquestração, declarado fora do dimensionamento de tarefa — Verificação 2, 3, 4, 5 e 7.
  - `agente de planejamento.unidade de trabalho que ele recorta` — a parcela desta tarefa: nenhuma das linhas de doutrina editadas aqui nomeia a tarefa atômica como unidade; o módulo coeso ganha definição decidível — a materialização de uma operação do modelo — Verificação 1, 4 e 6.
  - As demais entregas desta tarefa são **requisito secundário** (`## Requisitos secundários`), não propriedade do modelo: a guarda executável `tests/test_doutrina_unidade.py`, aferida pela Verificação 8.
- **Fora do escopo desta tarefa:** a gramática do card e as skills (`PLN-T3`), o protocolo do
  planejador (`PLN-T4`), o gate do modelador e a tabela *Quem escreve* de §3.2 (`PLN-T5`), o
  `README.md` (`PLN-T7`).

### PLN-T3 — A gramática do card: a tarefa é a materialização de uma operação [Sonnet · esforço medium · classe redacao]
- **Status:** `done` · 2026-09-22
- **Depende de:** `PLN-T2`
- **Objetivo:** a skill `diario-de-obras` apresenta o formato de uma tarefa como a materialização
  de uma operação do modelo, com o campo `Operação do modelo` no bloco de formato; as skills
  `modelo-por-fase` e `bootstrap-pantonic` e o agente `pantonic-fora-da-caixa` deixam de nomear a
  tarefa atômica.
- **Fundamento:** `DPN-2`, `DPN-6`, `DPN-9`; fatos `F-6`; censo da §7 (linhas das skills e do
  `pantonic-fora-da-caixa`).
- **Operação do modelo:** `OP-2`
  - OP-2: O redator da gramática reescreve a forma do card que quem planeja emite: ele passa a nascer como a materialização de uma operação, com o texto dela copiado e o contrato dos objetos de que ela precisa, e as demais definições de conduta deixam de chamar a unidade pelo nome antigo.
  - precisa de: agente de planejamento — residências da conduta: `.claude/agents/pantonic-planner.md` (descrição, tese do papel, abertura do protocolo, Fases 3a e 3b, Fase 4, Fase 5, anatomia do card e rodada de replanejamento) e a região gerada `kit:agents` de `.claude/README.md` — produzida por `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` e nunca editada à mão. Residências da régua e da unidade: `GOVERNANCA.md` §3 (matriz de responsabilidades, *A unidade de trabalho é o módulo coeso*, *Diretriz de dimensionamento de tarefa*, tabela da §4, §4.1, §4.3, G-PLANREADY e G-MODULO), `.claude/global/CLAUDE.md` (Regras 2 e 7) e a cópia do dono (`DPN-12`), `docs/RESIDENCIA_DOUTRINA.md`, as skills `diario-de-obras` (*Formato de uma tarefa*), `modelo-por-fase` e `bootstrap-pantonic`, `.claude/agents/pantonic-fora-da-caixa.md` e `README.md`. Residência da responsabilidade pelo lastro: `GOVERNANCA.md` §3.2 e `.claude/agents/pantonic-model-designer.md`, nas duas pontas no mesmo card. Residência da descrição: `docs/planner-spec.md` (novo), uma seção por dimensão da §4, na ordem dela e aberta por `## 0. O que esta especificação não é`. O censo linha a linha, com destino, é a §7; a classe do cabeçalho do card permanece como natureza do trabalho, porque os parsers a leem; ocorrência de outro sentido — escrita atômica em disco, passo atômico de migração — fica intacta; as entradas `RP-1`..`RP-7` e os itens de verificação que não citam ocupação permanecem, são a memória medida do papel; o escopo do papel continua na matriz de `GOVERNANCA.md` §3 (G-SCOPE), e a especificação não é residência nem do escopo nem do protocolo de conduta; tarefa — nenhum card deste plano altera uma tarefa. O que se observa nela, antes e depois, é o padrão sob o qual ela nasce: o nome da unidade no cabeçalho e na doutrina, a régua que definiu o recorte e a presença do campo `Operação do modelo` com o texto e os contratos copiados. Os sete cards deste plano, escritos sob o padrão antigo, são o retrato do antes; a aferição do depois é o primeiro plano decomposto depois da `PLN-T4`, lido por `python .claude/tools/modelo.py show`
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
  - `agente de planejamento.unidade de trabalho que ele recorta` — a parcela desta tarefa: o bloco de formato que ele preenche abre por *Formato de uma tarefa*, declara o card como a materialização de uma operação, traz o campo `Operação do modelo` com o texto e os contratos copiados e faz o `Pronto quando` derivar do estado final de cada propriedade que a operação altera; e nenhuma das quatro definições de conduta nomeia a tarefa atômica como unidade, com as ocorrências de outro sentido, como passo atômico de migração, intactas — Verificação 1, 2, 3 e 4.
  - As demais entregas desta tarefa são **requisito secundário** (`## Requisitos secundários`), não propriedade do modelo: a extensão da guarda `tests/test_doutrina_unidade.py`, aferida pela Verificação 5.
- **Fora do escopo desta tarefa:** o protocolo do planejador (`PLN-T4`) e a `description` dele,
  que é o que a região gerada de `.claude/README.md` repete.

### PLN-T4 — O protocolo do planejador: modelo primeiro, um card por operação [Opus · esforço xhigh · classe redacao]
- **Status:** `done` · 2026-09-22
- **Depende de:** `PLN-T3`
- **Objetivo:** `.claude/agents/pantonic-planner.md` reescrito nas regiões que a `DPN-2`, a
  `DPN-3`, a `DPN-4`, a `DPN-5` e a `DPN-6` tocam — descrição, tese, protocolo com três saídas,
  Fase 3 partida em 3a e 3b, Fase 4 sem percentual, anatomia do card derivada do modelo, rodada de
  replanejamento com card corretivo somado à operação — e a região gerada de `.claude/README.md`
  regenerada.
- **Fundamento:** `DPN-2`..`DPN-6`, `DPN-9`; fatos `F-3`, `F-5`, `F-7`, `F-11`; censo da §7.
- **Operação do modelo:** `OP-3`
  - OP-3: O autor de papéis fecha o vão do protocolo de quem planeja: a sessão ganha uma terceira forma de terminar sem plano fechado, com o esqueleto gravado e o pedido de autoria do modelo devolvido na linha de retorno; a decomposição só começa depois de o modelo existir, um card por operação, e o recorte deixa de se medir por percentual.
  - precisa de: agente de planejamento — residências da conduta: `.claude/agents/pantonic-planner.md` (descrição, tese do papel, abertura do protocolo, Fases 3a e 3b, Fase 4, Fase 5, anatomia do card e rodada de replanejamento) e a região gerada `kit:agents` de `.claude/README.md` — produzida por `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` e nunca editada à mão. Residências da régua e da unidade: `GOVERNANCA.md` §3 (matriz de responsabilidades, *A unidade de trabalho é o módulo coeso*, *Diretriz de dimensionamento de tarefa*, tabela da §4, §4.1, §4.3, G-PLANREADY e G-MODULO), `.claude/global/CLAUDE.md` (Regras 2 e 7) e a cópia do dono (`DPN-12`), `docs/RESIDENCIA_DOUTRINA.md`, as skills `diario-de-obras` (*Formato de uma tarefa*), `modelo-por-fase` e `bootstrap-pantonic`, `.claude/agents/pantonic-fora-da-caixa.md` e `README.md`. Residência da responsabilidade pelo lastro: `GOVERNANCA.md` §3.2 e `.claude/agents/pantonic-model-designer.md`, nas duas pontas no mesmo card. Residência da descrição: `docs/planner-spec.md` (novo), uma seção por dimensão da §4, na ordem dela e aberta por `## 0. O que esta especificação não é`. O censo linha a linha, com destino, é a §7; a classe do cabeçalho do card permanece como natureza do trabalho, porque os parsers a leem; ocorrência de outro sentido — escrita atômica em disco, passo atômico de migração — fica intacta; as entradas `RP-1`..`RP-7` e os itens de verificação que não citam ocupação permanecem, são a memória medida do papel; o escopo do papel continua na matriz de `GOVERNANCA.md` §3 (G-SCOPE), e a especificação não é residência nem do escopo nem do protocolo de conduta; agente model designer — não se transforma neste plano: a seção `## 1. Modelo conceitual` escrita por ele e o vocabulário de violações `V1`..`V21` de `.claude/tools/modelo.py` são o insumo que quem planeja consome, e permanecem como estão. `.claude/tools/modelo.py`, `tests/test_modelo.py` e as fixtures **não se tocam**. O que os cards deste plano publicam em `GOVERNANCA.md` §3.2 e em `.claude/agents/pantonic-model-designer.md` é a responsabilidade de **quem planeja** pelo lastro das operações, e nada além disso: o portão com que o modelador aceita ou recusa escrever a seção sobre um plano ainda sem cards não é objeto deste plano — alterá-lo é colateral e se escala
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
  - `agente de planejamento.aproveitamento do aparato de modelo` — a sessão tem três saídas antes do plano fechado, e a terceira é o esqueleto gravado com o dossiê de autoria devolvido na linha de retorno; a decomposição só começa com o modelo na árvore, um card por operação, na ordem delas e com o id derivado do número da operação — Verificação 3 e 5.
  - `agente de planejamento.descrição pública da figura` — a parcela desta tarefa: a `description` do agente e a linha regenerada do índice do kit anunciam a decomposição do modelo em cards, um por operação, e a parada que devolve o dossiê de autoria; a linha do índice sai da regeneração, nunca de edição à mão — Verificação 4 e 6.
  - `agente de planejamento.régua com que ele dimensiona um card` — a parcela desta tarefa: nenhum percentual e nenhum sinal de volume sobrevivem no protocolo, a conferência dimensiona por operação inteira, coesão e autossuficiência em contexto, e operação que não cabe num card coeso volta ao modelador por dossiê em vez de ser partida — Verificação 1 e 2.
  - As demais entregas desta tarefa são **requisito secundário** (`## Requisitos secundários`), não propriedade do modelo: a extensão da guarda `tests/test_doutrina_unidade.py`, aferida pela Verificação 7.
- **Fora do escopo desta tarefa:** o gate do modelador (`PLN-T5`); a spec (`PLN-T6`); o
  `README.md` fora da região gerada de `.claude/README.md` (`PLN-T7`).

### PLN-T4a — O ponteiro sobrevivente da tabela aposentada, nos Fatos estáveis do planejador [Sonnet · esforço low · classe redacao]
- **Status:** `done` · 2026-09-22
- **Depende de:** `PLN-T4`
- **Objetivo:** `.claude/agents/pantonic-planner.md:36-37` deixa de remeter à *tabela de classes* de
  `GOVERNANCA.md` §3, aposentada pela `PLN-T2` (`DPN-3`), e passa a dizer o que a régua é hoje; a
  primeira metade da frase — `Nenhum teto se escreve no card` — sobrevive intacta, porque continua
  verdadeira. Uma guarda executável tranca o retorno da remissão.
- **Fundamento:** `DPN-3`; achado `AE-13`. **Card corretivo somado à `OP-3`**, na forma que a
  própria `PLN-T2` instituiu em `GOVERNANCA.md` §3 (*A unidade de trabalho é o módulo coeso*: card
  corretivo de replanejamento **somado à operação que repara**, nunca operação partida em dois).
  Resíduo de `OP-3` e não de `OP-1`: quem aposentou a tabela foi a `OP-1`, em `GOVERNANCA.md`, mas
  o ponteiro sobrevivente está em `.claude/agents/pantonic-planner.md` — residência da `OP-3`, a
  única operação que declara alterar a **régua** e agir naquele arquivo.
- **Operação do modelo:** `OP-3`
  - OP-3: O autor de papéis fecha o vão do protocolo de quem planeja: a sessão ganha uma terceira forma de terminar sem plano fechado, com o esqueleto gravado e o pedido de autoria do modelo devolvido na linha de retorno; a decomposição só começa depois de o modelo existir, um card por operação, e o recorte deixa de se medir por percentual.
  - precisa de: agente de planejamento — residências da conduta: `.claude/agents/pantonic-planner.md` (descrição, tese do papel, abertura do protocolo, Fases 3a e 3b, Fase 4, Fase 5, anatomia do card e rodada de replanejamento) e a região gerada `kit:agents` de `.claude/README.md` — produzida por `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` e nunca editada à mão. Residências da régua e da unidade: `GOVERNANCA.md` §3 (matriz de responsabilidades, *A unidade de trabalho é o módulo coeso*, *Diretriz de dimensionamento de tarefa*, tabela da §4, §4.1, §4.3, G-PLANREADY e G-MODULO), `.claude/global/CLAUDE.md` (Regras 2 e 7) e a cópia do dono (`DPN-12`), `docs/RESIDENCIA_DOUTRINA.md`, as skills `diario-de-obras` (*Formato de uma tarefa*), `modelo-por-fase` e `bootstrap-pantonic`, `.claude/agents/pantonic-fora-da-caixa.md` e `README.md`. Residência da responsabilidade pelo lastro: `GOVERNANCA.md` §3.2 e `.claude/agents/pantonic-model-designer.md`, nas duas pontas no mesmo card. Residência da descrição: `docs/planner-spec.md` (novo), uma seção por dimensão da §4, na ordem dela e aberta por `## 0. O que esta especificação não é`. O censo linha a linha, com destino, é a §7; a classe do cabeçalho do card permanece como natureza do trabalho, porque os parsers a leem; ocorrência de outro sentido — escrita atômica em disco, passo atômico de migração — fica intacta; as entradas `RP-1`..`RP-7` e os itens de verificação que não citam ocupação permanecem, são a memória medida do papel; o escopo do papel continua na matriz de `GOVERNANCA.md` §3 (G-SCOPE), e a especificação não é residência nem do escopo nem do protocolo de conduta; agente model designer — não se transforma neste plano: a seção `## 1. Modelo conceitual` escrita por ele e o vocabulário de violações `V1`..`V21` de `.claude/tools/modelo.py` são o insumo que quem planeja consome, e permanecem como estão. `.claude/tools/modelo.py`, `tests/test_modelo.py` e as fixtures **não se tocam**. O que os cards deste plano publicam em `GOVERNANCA.md` §3.2 e em `.claude/agents/pantonic-model-designer.md` é a responsabilidade de **quem planeja** pelo lastro das operações, e nada além disso: o portão com que o modelador aceita ou recusa escrever a seção sobre um plano ainda sem cards não é objeto deste plano — alterá-lo é colateral e se escala
  - **Contrato copiado da versão 3, vigente em 2026-09-22.** A versão 4 está **pendente** do
    veredito do dono no Marco 2 (`## 1A`), e a medição parte sempre do modelo **vigente**
    (`GOVERNANCA.md` §3.2). Este card executa antes do Marco 2, logo não há o que recopiar.
- **Camada e fronteira:** um agente do kit, uma frase, mais uma asserção na guarda executável que a
  `PLN-T2` criou. Nenhuma linha de `GOVERNANCA.md`, nenhuma skill, nenhum instrumento de
  `.claude/tools/`. A região gerada `kit:agents` de `.claude/README.md` **não** se regenera: o texto
  tocado está em `## Fatos estáveis`, não na `description` do frontmatter — a Verificação 5 afere
  que o drift continua ausente.
- **Domínio:** *tabela de classes* — a tabela de tetos de turnos por classe que vivia em
  `GOVERNANCA.md` §3 e foi aposentada em 2026-09-21 (`DPN-3`), substituída pelo bullet *Classe do
  card — natureza, não teto* (`GOVERNANCA.md:189`). *Fatos estáveis* — a região de
  `.claude/agents/pantonic-planner.md` que a versão 4 pendente do modelo acrescenta à enumeração
  fechada das residências da conduta.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md:36-37` (`## Fatos estáveis`, fim do bullet do cabeçalho de tarefa)
  - `tests/test_doutrina_unidade.py` (acréscimo de uma função de teste; as duas existentes não se tocam)
- **Passos:**
  1. Em `.claude/agents/pantonic-planner.md:37`, substituir o literal
     `card: a régua numérica é a tabela de classes de `GOVERNANCA.md` §3, interna a este papel.`
     pelo literal
     `card, e nenhum número o dimensiona: a classe é natureza do trabalho (`GOVERNANCA.md` §3, *Classe do card — natureza, não teto*) e a régua é a operação do modelo que o card materializa (`GOVERNANCA.md` §3.2).`
     O fim da linha 36 — `Nenhum teto se escreve no` — **não se toca**: é a metade verdadeira da
     frase, e a Verificação 2 afere que ela sobreviveu. Quebra de linha se reajusta a ~100 colunas;
     palavra não muda.
  2. Acrescentar a `tests/test_doutrina_unidade.py`, **depois** das duas funções existentes e sem
     alterar nenhuma delas, a função literal:
     ```python
     def test_conduta_do_planejador_nao_remete_a_tabela_aposentada():
         t = _texto(".claude/agents/pantonic-planner.md")
         assert "tabela de classes" not in t
         assert "tabela de tetos" not in t
         assert "Nenhum teto se escreve no" in t
     ```
  3. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - Só a segunda metade da frase muda. Nenhuma outra linha de `.claude/agents/pantonic-planner.md`
    se toca — em especial as entradas `RP-1`..`RP-7` e os itens da Fase 4, que são a memória medida
    do papel (`I-9`).
  - As duas funções já existentes de `tests/test_doutrina_unidade.py` não se alteram: são entrega
    aceita da `PLN-T2`.
  - Não regenerar região alguma de `.claude/README.md`.
  - Não commitar (`I-1`).
- **Não fazer:**
  - Não "aproveitar" para revisar outras remissões do agente: a varredura da família
    `tabela de classes|tabela de tetos|teto por classe` foi feita em 2026-09-22 e este é o **único**
    sítio vivo (`AE-14`). `CHANGELOG.md:196,215` e
    `.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md:71` são registro datado e **ficam** (`I-7`).
  - Não tocar `GOVERNANCA.md`: o sítio dele já é da `PLN-T7`, passo 4a.
- **Contingências:**
  1. Se o literal do passo 1 não casar byte a byte → localizar por
     `grep -n 'tabela de classes' .claude/agents/pantonic-planner.md` e aplicar sobre a linha
     devolvida; se o literal não existir no arquivo → parar e sinalizar `blocked` razão `premissa`.
  2. Se `python -m pytest tests -q` reprovar em teste que este card não criou → parar e sinalizar
     `blocked` razão `premissa`, colando a linha de falha.
- **Testes:** `TR-DU-3` (`test_conduta_do_planejador_nao_remete_a_tabela_aposentada`), em
  `tests/test_doutrina_unidade.py`; suíte: `python -m pytest tests -q`.
- **Verificação:**

  1. ```
     grep -c 'tabela de classes' .claude/agents/pantonic-planner.md
     ```
     → **0**. **Medido antes: 1** (2026-09-22).
  2. ```
     grep -c 'Nenhum teto se escreve no' .claude/agents/pantonic-planner.md
     ```
     → **1** — a metade verdadeira sobreviveu. **Medido antes: 1** (2026-09-22).
  3. ```
     grep -c 'Classe do card — natureza, não teto' .claude/agents/pantonic-planner.md
     ```
     → **1**. **Medido antes: 0** (2026-09-22). O alvo da remissão existe: o mesmo `grep -c` sobre
     `GOVERNANCA.md` devolve **1**, medido na mesma data.
  4. ```
     python -m pytest tests -q
     ```
     → termina em `<N> passed`, com `<N>` igual ao total re-medido no despacho **mais 1**.
     **Medido antes: `271 passed`** (2026-09-22).
  5. ```
     pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift
     ```
     → exit **0**, primeira linha `kit_check: check-drift OK - .claude/README.md == regenerado (10 agente(s), 11 skill(s)); materializacao do alvo 'projeto' == canonico.`
     **Medido antes: o mesmo** (2026-09-22).
  6. ```
     python .claude/tools/backlog.py check
     ```
     → `check: OK — nenhuma violação.`, exit **0**. **Medido antes: o mesmo**.
- **Pronto quando:** as seis verificações imprimem os valores declarados e nenhum arquivo fora dos
  `Arquivos-alvo` foi editado.
  Por propriedade que a operação altera (`DPN-6`):
  - `agente de planejamento.régua com que ele dimensiona um card` — a parcela desta tarefa: a última
    residência da conduta que remetia à tabela aposentada deixa de remeter, e passa a apontar para a
    régua vigente; é o estado final que a versão 4 pendente do modelo exige e que o dono valida no
    Marco 2 — Verificação 1, 2 e 3.
  - As demais entregas desta tarefa são **requisito secundário** (`## Requisitos secundários`), não
    propriedade do modelo: a asserção nova de `tests/test_doutrina_unidade.py`, aferida pela
    Verificação 4.
- **Fora do escopo desta tarefa:** o sítio de `GOVERNANCA.md` (`PLN-T7`, passo 4a); a recópia dos
  contratos da versão 4 nos cards abertos, que é condicionada ao veredito do dono no Marco 2 e mora
  na `PLN-T6` e na `PLN-T7`.

### PLN-T5 — O modelador diante do plano sem cards, e o lastro que é do planejador [Sonnet · esforço medium · classe redacao]
- **Status:** `done` · 2026-09-22
- **Depende de:** `PLN-T4`
- **Objetivo:** `GOVERNANCA.md` §3.2 e `.claude/agents/pantonic-model-designer.md` publicam, nas
  duas pontas, que o modelador escreve a §1 sobre um plano ainda sem cards, que `V1` e `V3` são
  violações do lastro do planejador e voltam como saída literal, e que antes do Marco 1 a §1 é
  rascunho substituível no lugar.
- **Fundamento:** `DPN-4`, `DPN-5`, `DPN-7`, `DPN-9`; fatos `F-3`, `F-4`. A mudança de papel se
  publica nas duas pontas no mesmo card — a classe de defeito "metade de mudança de papel
  publicada" está medida em `docs/Entregas Aceitas/Entregas - P-0743.md`.
- **Operação do modelo:** `OP-4`
  - OP-4: O autor de papéis devolve a quem planeja o lastro que é dele: a lista de tarefas de cada operação do modelo passa a ser responsabilidade de quem decompõe o plano, e o que o instrumento mede nela volta medido para ele, em vez de travar a devolução de quem escreve o modelo.
  - precisa de: agente de planejamento — residências da conduta: `.claude/agents/pantonic-planner.md` (descrição, tese do papel, abertura do protocolo, Fases 3a e 3b, Fase 4, Fase 5, anatomia do card e rodada de replanejamento) e a região gerada `kit:agents` de `.claude/README.md` — produzida por `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` e nunca editada à mão. Residências da régua e da unidade: `GOVERNANCA.md` §3 (matriz de responsabilidades, *A unidade de trabalho é o módulo coeso*, *Diretriz de dimensionamento de tarefa*, tabela da §4, §4.1, §4.3, G-PLANREADY e G-MODULO), `.claude/global/CLAUDE.md` (Regras 2 e 7) e a cópia do dono (`DPN-12`), `docs/RESIDENCIA_DOUTRINA.md`, as skills `diario-de-obras` (*Formato de uma tarefa*), `modelo-por-fase` e `bootstrap-pantonic`, `.claude/agents/pantonic-fora-da-caixa.md` e `README.md`. Residência da responsabilidade pelo lastro: `GOVERNANCA.md` §3.2 e `.claude/agents/pantonic-model-designer.md`, nas duas pontas no mesmo card. Residência da descrição: `docs/planner-spec.md` (novo), uma seção por dimensão da §4, na ordem dela e aberta por `## 0. O que esta especificação não é`. O censo linha a linha, com destino, é a §7; a classe do cabeçalho do card permanece como natureza do trabalho, porque os parsers a leem; ocorrência de outro sentido — escrita atômica em disco, passo atômico de migração — fica intacta; as entradas `RP-1`..`RP-7` e os itens de verificação que não citam ocupação permanecem, são a memória medida do papel; o escopo do papel continua na matriz de `GOVERNANCA.md` §3 (G-SCOPE), e a especificação não é residência nem do escopo nem do protocolo de conduta; agente model designer — não se transforma neste plano: a seção `## 1. Modelo conceitual` escrita por ele e o vocabulário de violações `V1`..`V21` de `.claude/tools/modelo.py` são o insumo que quem planeja consome, e permanecem como estão. `.claude/tools/modelo.py`, `tests/test_modelo.py` e as fixtures **não se tocam**. O que os cards deste plano publicam em `GOVERNANCA.md` §3.2 e em `.claude/agents/pantonic-model-designer.md` é a responsabilidade de **quem planeja** pelo lastro das operações, e nada além disso: o portão com que o modelador aceita ou recusa escrever a seção sobre um plano ainda sem cards não é objeto deste plano — alterá-lo é colateral e se escala
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
     grep -c 'e `V3`, que moram no' .claude/agents/pantonic-model-designer.md
     ```
     → **1** — a menção de `V3` como violação que mora no **lastro**. **Medido em 2026-09-22,
     contra a entrega na árvore: 1.**
  1a. ```
      grep -c '`V3` dispara por construção' .claude/agents/pantonic-model-designer.md
      ```
      → **1** — a menção de `V3` como violação que dispara sobre plano ainda sem cards. **Medido
      em 2026-09-22, contra a entrega na árvore: 1.**
      > **Reparo do consultor, 2026-09-22 (`AE-17`).** A forma anterior era
      > `grep -c 'V3' … → um número maior ou igual a 2`, e **`grep -c` conta linhas com match, não
      > ocorrências**: o literal do passo 3 é uma linha física única que carrega as **duas**
      > menções, então o comando devolvia `1` sobre uma entrega correta e a tarefa parou
      > `blocked premissa`. Medido: `grep -c 'V3' …` = **1**, `grep -o 'V3' … | wc -l` = **2**.
      > O aceite **não** foi afrouxado — ficou mais estrito: em vez de "duas ocorrências quaisquer
      > da sigla", afere-se que **cada uma das duas afirmações** existe, por literal próprio. O
      > literal entregue no passo 3 **não se toca**: quem estava errado era o aferidor, não a
      > entrega (`DM-12`), e reescrever a entrega para o número fechar seria inverter a regra.
  2. ```
     grep -c 'Só cinco violações' .claude/agents/pantonic-model-designer.md
     ```
     → **1**. **Medido em 2026-09-22: 0.**
  3. ```
     grep -c 'Só três violações' .claude/agents/pantonic-model-designer.md
     ```
     → **0**. **Medido em 2026-09-22: 1.**
  4. ```
     grep -c '^\*\*Lastro\.\*\*\|^\*\*Rascunho antes do Marco 1\.\*\*' GOVERNANCA.md
     ```
     → **2**. **Medido em 2026-09-22: 0.**
  5. ```
     python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md
     ```
     → a **mesma** saída re-medida no despacho, byte a byte, e exit **0** — este card não toca o
     `P-0743` (invariância, `I-4`). A forma é relação, não constante: o que se afere é que **este
     card** não moveu o `P-0743`, e não que o `P-0743` seja imóvel. **Medido em 2026-09-22:**
     `modelo: OK — 13 operações, 9 objetos, 21 propriedades, 18 tarefas, versão 1`.
  6. ```
     python -m pytest tests -q
     ```
     → `<N> passed`, com `<N>` igual ao total re-medido no despacho **mais 1**. **Medido em
     2026-09-22, depois da `PLN-T4a`: `274 passed`** — o valor publicado na autoria
     (`262 passed`, 2026-09-21) envelheceu doze testes em quatro tarefas, e a forma-relação
     absorveu sem dano. É por isso que ela fica (`AE-16`).
  7. ```
     python .claude/tools/backlog.py check
     ```
     → `check: OK — nenhuma violação.`, exit **0**. **Medido antes: o mesmo**.
- **Pronto quando:** as **oito** verificações — 1, 1a, 2, 3, 4, 5, 6 e 7 — imprimem os valores
  declarados. É o gate do **Marco 2**:
  a orquestração abre o marco com `modelo.py show` sobre este plano.
  Por propriedade que a operação altera (`DPN-6`):
  - `agente de planejamento.responsabilidade pelo lastro das operações` — a lista de tarefas de cada operação é lastro declarado de quem planeja e as duas violações que ela dispara voltam medidas para ele; a norma e as duas definições de conduta dizem o mesmo nas duas pontas — Verificação 1, 1a, 2, 3 e 4.
  - **Colateral, aprovado pelo dono em 2026-09-22 e entregue por este card, fora do modelo:** os passos 1, 2 e 4 também abrem o portão do modelador para plano ainda sem cards e declaram que, entre a autoria e o primeiro aceite do dono, a seção é rascunho que se substitui no lugar. As duas alteram o `agente model designer`, que é objeto **externo** do modelo (`GOVERNANCA.md` §3.2), e por isso não são operação nem propriedade daqui. **Não escale**: a decisão já foi tomada — entregue-as com o resto do card — aferidas pela metade `**Rascunho antes do Marco 1.**` da Verificação 4.
  - As demais entregas desta tarefa são **requisito secundário** (`## Requisitos secundários`), não propriedade do modelo: a extensão da guarda `tests/test_doutrina_unidade.py`, aferida pela Verificação 6.
- **Fora do escopo desta tarefa:** a spec (`PLN-T6`) e o `README.md` (`PLN-T7`).

### PLN-T5a — A frase que governa o gate do modelador, e a enumeração que envelheceu [Sonnet · esforço low · classe redacao]
- **Status:** `done` · 2026-09-22
- **Depende de:** `PLN-T5`
- **Objetivo:** a frase **antecedente** de `.claude/agents/pantonic-model-designer.md:24-27` deixa
  de classificar `V1` e `V3` como violações "da seção" — que travariam a devolução do ato pelo
  próprio critério que ela enuncia —, e a enumeração das violações de `objeto` deixa de ser lista
  fechada, porque a medição mostrou que ela já estava incompleta.
- **Fundamento:** `DPN-4`, `DPN-5`; achado `AE-19`. **Card corretivo somado à `OP-4`**, na forma
  que a `PLN-T2` instituiu em `GOVERNANCA.md` §3 (card corretivo de replanejamento **somado à
  operação que repara**). É resíduo da `OP-4` e de nenhuma outra: o texto da operação diz, literal,
  "em vez de **travar a devolução** de quem escreve o modelo", e a frase antecedente é exatamente o
  que ainda trava. Completa um **colateral que o dono já aprovou em 2026-09-22** e que a `PLN-T5`
  entregou pela metade — não é matéria nova e não se escala de novo.
- **Operação do modelo:** `OP-4`
  - OP-4: O autor de papéis devolve a quem planeja o lastro que é dele: a lista de tarefas de cada operação do modelo passa a ser responsabilidade de quem decompõe o plano, e o que o instrumento mede nela volta medido para ele, em vez de travar a devolução de quem escreve o modelo.
  - precisa de: agente de planejamento — residências da conduta: `.claude/agents/pantonic-planner.md` (descrição, tese do papel, abertura do protocolo, Fases 3a e 3b, Fase 4, Fase 5, anatomia do card e rodada de replanejamento) e a região gerada `kit:agents` de `.claude/README.md` — produzida por `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` e nunca editada à mão. Residências da régua e da unidade: `GOVERNANCA.md` §3 (matriz de responsabilidades, *A unidade de trabalho é o módulo coeso*, *Diretriz de dimensionamento de tarefa*, tabela da §4, §4.1, §4.3, G-PLANREADY e G-MODULO), `.claude/global/CLAUDE.md` (Regras 2 e 7) e a cópia do dono (`DPN-12`), `docs/RESIDENCIA_DOUTRINA.md`, as skills `diario-de-obras` (*Formato de uma tarefa*), `modelo-por-fase` e `bootstrap-pantonic`, `.claude/agents/pantonic-fora-da-caixa.md` e `README.md`. Residência da responsabilidade pelo lastro: `GOVERNANCA.md` §3.2 e `.claude/agents/pantonic-model-designer.md`, nas duas pontas no mesmo card. Residência da descrição: `docs/planner-spec.md` (novo), uma seção por dimensão da §4, na ordem dela e aberta por `## 0. O que esta especificação não é`. O censo linha a linha, com destino, é a §7; a classe do cabeçalho do card permanece como natureza do trabalho, porque os parsers a leem; ocorrência de outro sentido — escrita atômica em disco, passo atômico de migração — fica intacta; as entradas `RP-1`..`RP-7` e os itens de verificação que não citam ocupação permanecem, são a memória medida do papel; o escopo do papel continua na matriz de `GOVERNANCA.md` §3 (G-SCOPE), e a especificação não é residência nem do escopo nem do protocolo de conduta; agente model designer — não se transforma neste plano: a seção `## 1. Modelo conceitual` escrita por ele e o vocabulário de violações `V1`..`V21` de `.claude/tools/modelo.py` são o insumo que quem planeja consome, e permanecem como estão. `.claude/tools/modelo.py`, `tests/test_modelo.py` e as fixtures **não se tocam**. O que os cards deste plano publicam em `GOVERNANCA.md` §3.2 e em `.claude/agents/pantonic-model-designer.md` é a responsabilidade de **quem planeja** pelo lastro das operações, e nada além disso: o portão com que o modelador aceita ou recusa escrever a seção sobre um plano ainda sem cards não é objeto deste plano — alterá-lo é colateral e se escala
  - **Contrato copiado da versão 3, vigente em 2026-09-22.** A versão 4 está pendente do veredito
    do dono no Marco 2 (`## 1A`), e a medição parte sempre do modelo vigente (`GOVERNANCA.md`
    §3.2). Se o veredito for `go` na versão 4 antes do despacho deste card, o contrato se recopia
    do bloco vigente, na mesma regra do passo 0 da `PLN-T6` (`AE-14`).
- **Camada e fronteira:** um agente do kit, uma frase, mais uma asserção na guarda executável.
  Nenhuma linha de `GOVERNANCA.md` — a ponta da norma está correta e foi conferida concordante
  pelo reviewer da `PLN-T5` —, nenhum instrumento de `.claude/tools/`. A região gerada `kit:agents`
  de `.claude/README.md` **não** se regenera: o texto está em `## Fatos estáveis`, não na
  `description` do frontmatter, e a Verificação 5 afere que o drift continua ausente.
- **Domínio:** *violação da seção* — no gate do modelador, a violação que o impede de devolver o
  ato. O critério publicado é o **rótulo de indexação** que `.claude/tools/modelo.py` imprime:
  `secao`, `OP-<n>`, `objeto` ou o `<ID>` de uma tarefa. Medido em 2026-09-22 contra
  `tests/fixtures/modelo/plano-invalido.md`: `V1` e `V3` saem indexadas por `OP-<n>` — logo, pelo
  critério antecedente, seriam "da seção", contra o que a frase seguinte publica.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-model-designer.md:24-27` (`## Fatos estáveis`, a frase antecedente do
    bullet do `exit 1`, da palavra `seção` na linha 24 até `antes de devolver.` na linha 27)
  - `tests/test_doutrina_unidade.py` (acréscimo de uma função; as existentes não se tocam)
- **Passos:**
  1. Em `.claude/agents/pantonic-model-designer.md`, substituir o bloco literal que hoje ocupa as
     linhas 24 a 27 até `antes de devolver.` —
     ```
       seção **toda** violação que o instrumento não indexa pelo `<ID>` de uma tarefa: as de `secao`, as
       de `OP-<n>` e as de `objeto`, estas últimas vindas de `### 1.1 Objetos` e de
       `### 1.3 Estado inicial e estado final` (`V6`, `V7`, `V15`, `V17`). Corrija a seção que você mesmo
       escreveu e rode de novo antes de devolver.
     ```
     — pelo bloco literal:
     ```
       seção **toda** violação que o instrumento não indexa pelo `<ID>` de uma tarefa — as de
       `secao`, as de `OP-<n>` e as de `objeto`, estas últimas vindas de `### 1.1 Objetos` e de
       `### 1.3 Estado inicial e estado final` —, **exceto `V1` e `V3`**: o instrumento as indexa
       por `OP-<n>`, mas elas moram no lastro e não são suas, como a frase seguinte declara. A
       classe se lê pelo **rótulo com que o instrumento indexa** a violação, nunca por lista de
       códigos: o vocabulário `V1`..`V21` cresce, e lista fechada envelhece. Corrija a seção que
       você mesmo escreveu e rode de novo antes de devolver.
     ```
     **Ajuste de quebra de linha para caber em ~100 colunas é permitido e esperado; mudança de
     palavra não é.** A frase seguinte, que começa em `Só cinco violações **não são suas**:`,
     **não se toca** — é entrega aceita da `PLN-T5`.
  2. Acrescentar a `tests/test_doutrina_unidade.py`, **depois** das funções existentes e sem
     alterar nenhuma delas, a função literal:
     ```python
     def test_gate_do_modelador_nao_classifica_lastro_como_secao():
         t = _texto(".claude/agents/pantonic-model-designer.md")
         assert "exceto `V1` e `V3`" in t
         assert "(`V6`, `V7`, `V15`, `V17`)" not in t
         assert "Só cinco violações" in t
     ```
  3. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - A frase `Só cinco violações **não são suas**: ...` e tudo que a segue **não se tocam**: são
    entrega aceita da `PLN-T5`, conferida concordante pelo reviewer em 2026-09-22.
  - Nenhuma outra linha de `.claude/agents/pantonic-model-designer.md` se toca.
  - As funções já existentes de `tests/test_doutrina_unidade.py` não se alteram.
  - Não regenerar região alguma de `.claude/README.md`. Não commitar (`I-1`).
- **Não fazer:**
  - Não tocar `.claude/tools/modelo.py`, `tests/test_modelo.py` nem as fixtures: o vocabulário
    `V1`..`V21` é insumo e invariante deste plano.
  - Não "aproveitar" para revisar outras frases do agente: a varredura das 111 linhas foi feita em
    2026-09-22 e este é o **único** sítio que governa ou contradiz o que a `PLN-T5` publicou
    (`AE-20`). Em especial, `:55-57` (autoria preenche `tarefas:` por convenção) e `:107` (a lista
    é lastro do planejador depois da autoria) foram conferidos **concordantes** e ficam como estão.
  - Não tocar `GOVERNANCA.md` §3.2: a outra ponta está correta.
- **Contingências:**
  1. Se o bloco literal não casar byte a byte — quebra de linha diferente, por exemplo → localizar
     por `grep -n 'e as de .objeto., estas últimas vindas' .claude/agents/pantonic-model-designer.md`
     e aplicar sobre a frase que a linha devolver, preservando o sentido literal do texto novo. Se
     a frase não existir no arquivo → parar e sinalizar `blocked` razão `premissa`.
  2. Se `python -m pytest tests -q` reprovar em teste que este card não criou → parar e sinalizar
     `blocked` razão `premissa`, colando a linha de falha.
- **Testes:** `TR-DU-6` (`test_gate_do_modelador_nao_classifica_lastro_como_secao`), em
  `tests/test_doutrina_unidade.py`; suíte: `python -m pytest tests -q`.
- **Verificação:**

  1. ```
     grep -c 'exceto `V1` e `V3`' .claude/agents/pantonic-model-designer.md
     ```
     → **1**. **Medido em 2026-09-22: 0.**
  2. ```
     grep -c '(`V6`, `V7`, `V15`, `V17`)' .claude/agents/pantonic-model-designer.md
     ```
     → **0** — a lista fechada saiu. **Medido em 2026-09-22: 1.**
  3. ```
     grep -c 'Só cinco violações' .claude/agents/pantonic-model-designer.md
     ```
     → **1** — a entrega da `PLN-T5` sobreviveu intacta. **Medido em 2026-09-22: 1.**
  4. ```
     python -m pytest tests -q
     ```
     → `<N> passed`, com `<N>` igual ao total re-medido no despacho **mais 1**. **Medido em
     2026-09-22: `275 passed`.**
  5. ```
     pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift
     ```
     → exit **0**, com os **mesmos** números de agentes e skills re-medidos no despacho — este card
     não cria nem remove agente nem skill. **Medido em 2026-09-22:**
     `kit_check: check-drift OK - .claude/README.md == regenerado (10 agente(s), 11 skill(s)); materializacao do alvo 'projeto' == canonico.`
  6. ```
     python .claude/tools/backlog.py check
     ```
     → `check: OK — nenhuma violação.`, exit **0**. **Medido em 2026-09-22: o mesmo.**
  7. ```
     python .claude/tools/modelo.py check --plano docs/plans/P-0745-planejador-modelo-operacao.md
     ```
     → a **mesma** saída re-medida no despacho e exit **0**: este card não toca o modelo
     (invariância). **Medido em 2026-09-22:**
     `modelo: OK — 6 operações, 3 objetos, 7 propriedades, 8 tarefas, versão 3`.
- **Pronto quando:** as sete verificações imprimem os valores declarados e nenhum arquivo fora dos
  `Arquivos-alvo` foi editado.
  Por propriedade que a operação altera (`DPN-6`):
  - `agente de planejamento.responsabilidade pelo lastro das operações` — a parcela desta tarefa: o
    gate do modelador deixa de ter duas leituras sobre `V1` e `V3`, e a única que resta é a que a
    `PLN-T5` publicou — elas são lastro do planejador e voltam medidas para ele, em vez de travar a
    devolução de quem escreve o modelo — Verificação 1 e 3.
  - As demais entregas desta tarefa são **requisito secundário** (`## Requisitos secundários`), não
    propriedade do modelo: a asserção nova de `tests/test_doutrina_unidade.py` e a retirada da lista
    fechada de códigos, aferidas pelas Verificações 2 e 4.
- **Fora do escopo desta tarefa:** a ponta da norma em `GOVERNANCA.md` §3.2, correta e conferida; o
  vocabulário `V1`..`V21` do instrumento; e a divergência entre a tabela de transições da skill
  `diario-de-obras` e o `_TRANSICOES` de `backlog.py` (`AE-18`, rota `TK-66`).

### PLN-T6 — A especificação do agente de planejamento [Opus · esforço xhigh · classe redacao]
- **Status:** `done` · 2026-09-22
- **Depende de:** `PLN-T5`
- **Objetivo:** `docs/planner-spec.md` escrito, com uma seção por dimensão da §4, cada afirmação
  ancorada no agregado da `PLN-T1` (o antes) ou numa decisão `DPN-<n>` deste plano (o depois), e
  nenhuma afirmação sem uma das duas âncoras.
- **Fundamento:** `DPN-1`, `DPN-8`; fatos `F-9`, `F-14`. A lista de dimensões tem residência
  única na §4; este card a consome, não a reenuncia. Herda a `PLS-T2` do `P-0744`.
- **Operação do modelo:** `OP-5`
  - OP-5: O redator da especificação descreve a figura de quem planeja depois de medir como ela se comportou até aqui: uma seção por dimensão, cada afirmação ancorada no retrato medido ou na decisão que instituiu o depois, e a última nomeando o que o corpus ainda não permite dizer.
  - precisa de: agente de planejamento — residências da conduta: `.claude/agents/pantonic-planner.md`, em **dez regiões — e esta enumeração é a lista inteira**: descrição, fatos estáveis, tese do papel, abertura do protocolo, Fases 3a e 3b, Fase 4, Fase 5, anatomia do card, rodada de replanejamento e o que ele nunca faz. Quem edita o arquivo confronta as dez antes de publicar; região de conduta que não esteja aqui é achado para o modelador, não licença de autoria. A outra residência da conduta é a região gerada `kit:agents` de `.claude/README.md` — produzida por `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` e nunca editada à mão. Residências da régua e da unidade: `GOVERNANCA.md` §3 (matriz de responsabilidades, *A unidade de trabalho é o módulo coeso*, *Diretriz de dimensionamento de tarefa*, tabela da §4, §4.1, §4.3, G-PLANREADY e G-MODULO), `.claude/global/CLAUDE.md` (Regras 2 e 7) e a cópia do dono (`DPN-12`), `docs/RESIDENCIA_DOUTRINA.md`, as skills `diario-de-obras` (*Formato de uma tarefa*), `modelo-por-fase` e `bootstrap-pantonic`, `.claude/agents/pantonic-fora-da-caixa.md` e `README.md`. A régua **numérica** não reside em `.claude/agents/pantonic-planner.md` — ela é interna a `GOVERNANCA.md` §3 —, mas o arquivo **remete** a ela, e remissão a régua aposentada conta como residência para efeito do estado final: enquanto a linha de `## Fatos estáveis` que invoca a tabela de classes como régua numérica do papel estiver viva, a propriedade da régua não alcançou o estado final, ainda que toda residência numérica tenha sido reescrita. Residência da responsabilidade pelo lastro: `GOVERNANCA.md` §3.2 e `.claude/agents/pantonic-model-designer.md`, nas duas pontas no mesmo card. Residência da descrição: `docs/planner-spec.md` (novo), uma seção por dimensão da §4, na ordem dela e aberta por `## 0. O que esta especificação não é`. O censo linha a linha, com destino, é a §7; a classe do cabeçalho do card permanece como natureza do trabalho, porque os parsers a leem; ocorrência de outro sentido — escrita atômica em disco, passo atômico de migração — fica intacta; as entradas `RP-1`..`RP-7` e os itens de verificação que não citam ocupação permanecem, são a memória medida do papel; o escopo do papel continua na matriz de `GOVERNANCA.md` §3 (G-SCOPE), e a especificação não é residência nem do escopo nem do protocolo de conduta; agente model designer — não se transforma neste plano: a seção `## 1. Modelo conceitual` escrita por ele e o vocabulário de violações `V1`..`V21` de `.claude/tools/modelo.py` são o insumo que quem planeja consome, e permanecem como estão. `.claude/tools/modelo.py`, `tests/test_modelo.py` e as fixtures **não se tocam**. O que os cards deste plano publicam em `GOVERNANCA.md` §3.2 e em `.claude/agents/pantonic-model-designer.md` é a responsabilidade de **quem planeja** pelo lastro das operações, e nada além disso: o portão com que o modelador aceita ou recusa escrever a seção sobre um plano ainda sem cards não é objeto deste plano — alterá-lo é colateral e se escala
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
  0. **Sincronizar o contrato copiado com o modelo vigente, antes de qualquer outro passo.** Ler a
     linha do veredito do **Marco 2** na tabela de marcos deste plano — ela já está registrada
     quando este card é despachado, porque o Marco 2 precede a `PLN-T6`. Se o veredito for `go` na
     versão 4, recopiar para o campo `Operação do modelo` **deste card** o texto da operação e a
     linha `precisa de` a partir do bloco do modelo que estiver **vigente**, e fazer o mesmo na
     `PLN-T7` — que é o único outro card aberto com contrato copiado. Se for `no-go`, a versão 3
     permanece vigente e **nada se recopia**. Registrar na linha de retorno
     `passo 0: contrato <recopiado da versão 4 | mantido na versão 3>`. Não é decisão do executor:
     o veredito do dono já existe e este passo apenas o materializa (`GOVERNANCA.md` §3.2, *a
     medição parte sempre do modelo vigente*). Acrescentado pelo consultor em 2026-09-22 (`AE-14`).
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
     grep -o 'DPN-[0-9]*' docs/planner-spec.md | sort -u | wc -l
     ```
     → **um número maior ou igual a 5** — âncoras **distintas**, uma por decisão que a seção 4 e a
     5 citam. **Medido antes: o arquivo não existe.** A forma anterior (`grep -c 'DPN-'`) contava
     **linhas com match** e errava nos dois sentidos: cinco decisões citadas numa linha davam `1`,
     e a mesma decisão repetida em cinco linhas dava `5` — nenhum dos dois é "uma âncora por
     decisão" (`AE-17`). Forma nova exercitada em 2026-09-22 contra um arquivo que existe,
     `docs/plans/P-0745-planejador-modelo-operacao.md`: devolve **13** âncoras distintas, contra
     **74** linhas pela forma antiga.
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
  - `agente de planejamento.descrição pública da figura` — a figura tem especificação própria — uma seção por dimensão da §4, cada afirmação ancorada no retrato medido ou na decisão que a instituiu, e o que o corpus não responde nomeado em vez de adivinhado —, e a `description` do agente e a linha regenerada do índice do kit anunciam a decomposição do modelo em cards, na parcela que esta tarefa fecha: o documento existe, com uma seção por dimensão na ordem da §4 e uma seção de abertura que declara o que ele não é — Verificação 1, 2 e 3.
- **Fora do escopo desta tarefa:** o índice de documentos e a revisão do README (`PLN-T7`).

### PLN-T7 — O índice de documentos e a revisão do README [Sonnet · esforço medium · classe implementacao]
- **Status:** `done` · 2026-09-22
- **Depende de:** `PLN-T6`
- **Objetivo:** `docs/planner-spec.md` e este plano alcançáveis por `docs/DOC_MAP.md`; o `README.md`
  revisado contra o estado da árvore ao fim deste plano — reescritas **todas** as linhas de
  "tarefa atômica" da §7 **menos uma**, a `README.md:366`, medida histórica que não se edita
  (`I-7`), e a §3 sem a tabela de tetos — e `check-readme.ps1` verde; e o parágrafo de abertura de
  `GOVERNANCA.md` §3 sem o orçamento de turnos, que é o mesmo ato na residência espelho do hub.
- **Fundamento:** `DPN-1`, `DPN-2`, `DPN-3`; fatos `F-6`, `F-10`, `F-14`, `F-16`; invariantes
  `I-6`, `I-7`. É a tarefa de revisão de README que `G-README` dever 2 exige de toda sprint. Herda
  a `PLS-T3` do `P-0744`.
- **Operação do modelo:** `OP-6`
  - OP-6: O mantenedor leva a unidade nova à porta de entrada do repositório: o glossário e as seções que ainda chamam a unidade de trabalho pelo nome antigo passam a falar do card que materializa uma operação, o orçamento de turnos por classe sai de onde quem chega o lia, e a figura de quem planeja passa a se anunciar lá pela decomposição do modelo.
  - precisa de: agente de planejamento — residências da conduta: `.claude/agents/pantonic-planner.md`, em **dez regiões — e esta enumeração é a lista inteira**: descrição, fatos estáveis, tese do papel, abertura do protocolo, Fases 3a e 3b, Fase 4, Fase 5, anatomia do card, rodada de replanejamento e o que ele nunca faz. Quem edita o arquivo confronta as dez antes de publicar; região de conduta que não esteja aqui é achado para o modelador, não licença de autoria. A outra residência da conduta é a região gerada `kit:agents` de `.claude/README.md` — produzida por `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` e nunca editada à mão. Residências da régua e da unidade: `GOVERNANCA.md` §3 (matriz de responsabilidades, *A unidade de trabalho é o módulo coeso*, *Diretriz de dimensionamento de tarefa*, tabela da §4, §4.1, §4.3, G-PLANREADY e G-MODULO), `.claude/global/CLAUDE.md` (Regras 2 e 7) e a cópia do dono (`DPN-12`), `docs/RESIDENCIA_DOUTRINA.md`, as skills `diario-de-obras` (*Formato de uma tarefa*), `modelo-por-fase` e `bootstrap-pantonic`, `.claude/agents/pantonic-fora-da-caixa.md` e `README.md`. A régua **numérica** não reside em `.claude/agents/pantonic-planner.md` — ela é interna a `GOVERNANCA.md` §3 —, mas o arquivo **remete** a ela, e remissão a régua aposentada conta como residência para efeito do estado final: enquanto a linha de `## Fatos estáveis` que invoca a tabela de classes como régua numérica do papel estiver viva, a propriedade da régua não alcançou o estado final, ainda que toda residência numérica tenha sido reescrita. Residência da responsabilidade pelo lastro: `GOVERNANCA.md` §3.2 e `.claude/agents/pantonic-model-designer.md`, nas duas pontas no mesmo card. Residência da descrição: `docs/planner-spec.md` (novo), uma seção por dimensão da §4, na ordem dela e aberta por `## 0. O que esta especificação não é`. O censo linha a linha, com destino, é a §7; a classe do cabeçalho do card permanece como natureza do trabalho, porque os parsers a leem; ocorrência de outro sentido — escrita atômica em disco, passo atômico de migração — fica intacta; as entradas `RP-1`..`RP-7` e os itens de verificação que não citam ocupação permanecem, são a memória medida do papel; o escopo do papel continua na matriz de `GOVERNANCA.md` §3 (G-SCOPE), e a especificação não é residência nem do escopo nem do protocolo de conduta; tarefa — nenhum card deste plano altera uma tarefa. O que se observa nela, antes e depois, é o padrão sob o qual ela nasce: o nome da unidade no cabeçalho e na doutrina, a régua que definiu o recorte e a presença do campo `Operação do modelo` com o texto e os contratos copiados. Os sete cards deste plano, escritos sob o padrão antigo, são o retrato do antes; a aferição do depois é o primeiro plano decomposto depois da `PLN-T4`, lido por `python .claude/tools/modelo.py show`
- **Camada e fronteira:** documentação — a porta de entrada (`README.md`, `docs/DOC_MAP.md`) e o
  parágrafo de abertura de `GOVERNANCA.md` §3, residência espelho do mesmo texto. Nenhum código,
  nenhum arquivo de `.claude/`.
- **Arquivos-alvo:**
  - `GOVERNANCA.md:78,80` (§3, parágrafo de abertura: "orçamento de turnos", "caber no orçamento")
  - `docs/DOC_MAP.md:157` (entrada de `docs/consultant-spec.md`, modelo da entrada nova)
  - `README.md:94` (glossário, `- **Tarefa atômica** —`)
  - `README.md:305` (§3, parágrafo `**Orçamento de turnos por classe de tarefa.**`, até o fim do parágrafo e da tabela que o segue, se houver)
  - `README.md:350` (§4, linha `| Planejamento (intelectual) |`)
  - `README.md:382` (§5, `decompõe a iniciativa em **tarefas atômicas**`)
  - `README.md:405` (§5, `Uma tarefa atômica bem escrita carrega, no mínimo:`)
  - `README.md:432` (§5, `a tarefa atômica em contexto limpo`)
  - `README.md:478` (§6, `**Passo 3 — escolher uma única tarefa atômica.**`)
  - `README.md:825-826` (§11, linhas `| `pantonic-planner` |` e `| `pantonic-executor` |` — re-ancoradas em 2026-09-22; o card as citava como `824-825`)
- **Passos:**
  0. **Conferir o contrato copiado.** Se a `PLN-T6` registrou `passo 0: contrato recopiado da
     versão 4`, o campo `Operação do modelo` deste card já foi recopiado por ela; conferir que o
     texto de `OP-6` e a linha `precisa de` batem com o bloco vigente do modelo e, se não baterem,
     recopiar. Se a `PLN-T6` registrou `mantido na versão 3`, nada se faz. Registrar na linha de
     retorno `passo 0: contrato <conferido | recopiado>`. Acrescentado pelo consultor em 2026-09-22
     (`AE-14`).
  1. Acrescentar a `docs/DOC_MAP.md` uma entrada `## docs/planner-spec.md (~<n> linhas)` na mesma
     forma da entrada de `docs/consultant-spec.md` da linha 157: o resumo em uma linha, a lista de
     seções e a linha `**Acesso:**` com o `Grep` de heading; `<n>` é a contagem real obtida por
     `python -c "import pathlib;print(len(pathlib.Path('docs/planner-spec.md').read_text(encoding='utf-8').splitlines()))"`.
  2. Acrescentar a `docs/DOC_MAP.md` uma entrada `## docs/plans/P-0745-planejador-modelo-operacao.md (~<n> linhas)` na mesma forma, com as seções `## 3. Decisões`, `## 7. Censo das formas reais`, `## 8. Tarefas` e `## 12. Agregado medido` e a linha `**Acesso:**` por `Grep pattern:"^### PLN-T2 "`.
  3. Em `README.md:94`, substituir `- **Tarefa atômica** — a unidade de execução, definida por uma propriedade: executável por um agente` pelo início literal `- **Card** — a unidade de execução: a materialização de **uma operação do modelo** do plano, executável por um agente` e ajustar o restante da entrada do glossário para que a propriedade que a define seja *uma operação inteira, coesa e autossuficiente em contexto*, sem percentual e sem teto.
  4. Em `README.md:305`, substituir o parágrafo `**Orçamento de turnos por classe de tarefa.**` — e a tabela de tetos que o segue, se existir — por um parágrafo literal:
     `**Classe do card — natureza, não teto.** A classe do cabeçalho (`mecanica|implementacao|comportamental|investigacao|redacao`) declara a natureza do trabalho e calibra a profundidade de quem executa; nenhum número de turnos ou de ocupação dimensiona a tarefa. A tabela de tetos por classe, calibrada em 2026-08-01 sobre o recorte atômico numa janela de 200k, foi aposentada em 2026-09-21 junto com esse recorte (`GOVERNANCA.md` §3; `P-0745`). O consumo continua medido em `docs/telemetria.tsv` e se lê na série, nunca como aceite.`
  4a. Em `GOVERNANCA.md:78`, substituir `fase, orçamento de turnos e economia de contexto` por
     `fase, dimensionamento pela operação do modelo e economia de contexto`; e em
     `GOVERNANCA.md:80`, substituir `nenhuma rota se muda para caber no orçamento` por
     `nenhuma rota se muda para caber no custo`. É o **mesmo ato do passo 4**, na residência espelho:
     o parágrafo de abertura da §3 ainda vende o orçamento de turnos como instrumento de
     sustentabilidade, enquanto a própria §3 o aposentou como régua na `PLN-T2` (`DPN-3`), e `custo`
     é o termo que a mesma hierarquia já usa duas frases antes. Quebra de linha se reajusta a ~100
     colunas; palavra não muda. Sítio acrescentado ao censo da §7 pelo consultor em 2026-09-22
     (`AE-10`), e é o **único** órfão da forma antiga em `GOVERNANCA.md` — varredura medida na
     mesma data.
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
  - `README.md:366` **e** `README.md:1036` não se editam (`I-7`): são a mesma medida histórica de
    2026-07, em duas residências, e são exatamente as duas linhas que a Verificação 3 espera
    encontrar ao final (`AE-17`). `README.md:401` não se edita (outro sentido, §7).
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
     → **um número maior em 2 que o medido no despacho**. **Medido em 2026-09-22: 11** — o valor
     publicado na autoria (**9**, 2026-09-21) envelheceu duas entradas; a forma-relação absorveu
     (`AE-16`).
  3. ```
     grep -ic 'tarefa atômica\|tarefas atômicas' README.md
     ```
     → **2** — as **duas** medidas históricas que ficam (`I-7`): `README.md:366` e
     `README.md:1036`, as duas carregando a mesma aferição de 2026-07 ("71 turnos e ~189 mil
     tokens numa única tarefa atômica"). **Medido em 2026-09-22: 11 linhas e 12 ocorrências.**
     Três defeitos de aferidor corrigidos no mesmo ato (`AE-17`): **(i)** o `-i` é necessário —
     a entrada de glossário de `README.md:94` escreve **`Tarefa atômica`** com maiúscula, e a
     forma anterior, sem `-i`, **não a enxergava**; **(ii)** o esperado passa de `1` para `2`,
     porque a segunda medida histórica (`README.md:1036`) não estava no censo da §7 e foi
     acrescentada a ele como **fica**; **(iii)** a contagem é de **linhas** de propósito — a
     pergunta é "que linhas sobraram" —, e a conferência de que nenhuma ocorrência ficou escondida
     numa linha já reescrita é a Verificação 3a.
  3a. ```
      grep -oi 'tarefa atômica\|tarefas atômicas' README.md | wc -l
      ```
      → **2** — uma ocorrência em cada uma das duas linhas históricas. **Medido em 2026-09-22: 12
      ocorrências em 11 linhas**, sendo `README.md:382` a única linha com **duas** — e o passo 6
      cobre as duas no mesmo literal.
  4. ```
     grep -c 'Orçamento de turnos por classe de tarefa' README.md
     ```
     → **0**. **Medido antes: 1**.
  4a. ```
      grep -c 'orçamento de turnos\|caber no orçamento' GOVERNANCA.md
      ```
      → **0**. **Medido antes: 2** — as duas linhas do passo 4a (`GOVERNANCA.md:78` e `:80`),
      contadas em 2026-09-22.
  5. ```
     pwsh -NoProfile -File .claude/checks/check-readme.ps1
     ```
     → exit **0**, e a primeira linha começa por `check-readme: OK -` com **os mesmos números de
     agentes, skills e guardrails re-medidos no despacho** — este card não cria nem remove agente,
     skill ou guardrail, então a relação é de invariância, não de constante (`AE-16`). **Medido em
     2026-09-22:** `check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s), versão '0.0.0',
     14 seção(ões) com Fonte da verdade válida`.
  6. ```
     python .claude/tools/backlog.py check
     ```
     → `check: OK — nenhuma violação.`, exit **0**. **Medido antes: o mesmo**.
- **Pronto quando:** as **oito** verificações — 1, 2, 3, 3a, 4, 4a, 5 e 6 — imprimem os valores
  declarados e a saída literal de `check-readme.ps1` está na linha de retorno.
  Por propriedade que a operação altera (`DPN-6`):
  - `agente de planejamento.unidade de trabalho que ele recorta` — a parcela desta tarefa: o glossário abre por card, as demais linhas da porta de entrada falam do card que materializa uma operação, e `check-readme.ps1` continua saindo `0` — Verificação 3 e 5.
  - `agente de planejamento.régua com que ele dimensiona um card` — a parcela desta tarefa: o parágrafo do orçamento de turnos por classe sai da porta de entrada e vira a classe como natureza do trabalho, e o parágrafo de abertura de `GOVERNANCA.md` §3 deixa de vender o orçamento de turnos como instrumento de sustentabilidade — Verificação 4 e 4a.
  - `agente de planejamento.descrição pública da figura` — a parcela desta tarefa: as linhas do `README.md` que anunciavam decomposição em tarefas atômicas passam a anunciar a decomposição do modelo em cards, um por operação — Verificação 3.
  - As demais entregas desta tarefa são **requisito secundário** (`## Requisitos secundários`), não propriedade do modelo: as duas entradas novas de `docs/DOC_MAP.md`, aferidas pela Verificação 1 e 2.
- **Fora do escopo desta tarefa:** o veredito do dono sobre o README e sobre a especificação
  (Marco 3), registrado pela orquestração (`GOVERNANCA.md` §4.5); o documento de encerramento
  (skill `entrega-de-encerramento`), que a orquestração produz ao fechar o plano.
### PLN-T7a — O README deixa de defender a régua que ele mesmo aposenta [Sonnet · esforço medium · classe redacao]
- **Status:** `done` · 2026-09-22
- **Depende de:** `PLN-T7`
- **Objetivo:** nenhuma linha de doutrina **viva** do `README.md` defende, define ou pressupõe o
  teto de turnos por classe que o `README.md:306` declara aposentado. As duas **medidas históricas**
  (`README.md:354` e `README.md:1025`) permanecem intactas: medida datada não se falsifica (`I-7`).
- **Fundamento:** `DPN-3`; achado `AE-23`, varredura do `AE-24`. **Card corretivo somado à `OP-6`**,
  na forma que a `PLN-T2` instituiu em `GOVERNANCA.md` §3. É resíduo da `OP-6` e de nenhuma outra: a
  operação diz, literal, que o mantenedor leva a unidade nova **à porta de entrada do repositório** e
  que "o orçamento de turnos por classe sai de onde quem chega o lia" — e oito sítios da porta de
  entrada ficaram fora do censo. **Nenhum passo deste card autora doutrina nova:** cada substituição
  condensa texto **já publicado e aceito** em `GOVERNANCA.md` §3, cuja âncora vem nomeada no passo.
  O `README.md` é residência **derivada**; a autoridade é o hub.
- **Operação do modelo:** `OP-6`
  - OP-6: O mantenedor leva a unidade nova à porta de entrada do repositório: o glossário e as seções que ainda chamam a unidade de trabalho pelo nome antigo passam a falar do card que materializa uma operação, o orçamento de turnos por classe sai de onde quem chega o lia, e a figura de quem planeja passa a se anunciar lá pela decomposição do modelo.
  - precisa de: agente de planejamento — residências da conduta: `.claude/agents/pantonic-planner.md`, em **dez regiões — e esta enumeração é a lista inteira**: descrição, fatos estáveis, tese do papel, abertura do protocolo, Fases 3a e 3b, Fase 4, Fase 5, anatomia do card, rodada de replanejamento e o que ele nunca faz. Quem edita o arquivo confronta as dez antes de publicar; região de conduta que não esteja aqui é achado para o modelador, não licença de autoria. A outra residência da conduta é a região gerada `kit:agents` de `.claude/README.md` — produzida por `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` e nunca editada à mão. Residências da régua e da unidade: `GOVERNANCA.md` §3 (matriz de responsabilidades, *A unidade de trabalho é o módulo coeso*, *Diretriz de dimensionamento de tarefa*, tabela da §4, §4.1, §4.3, G-PLANREADY e G-MODULO), `.claude/global/CLAUDE.md` (Regras 2 e 7) e a cópia do dono (`DPN-12`), `docs/RESIDENCIA_DOUTRINA.md`, as skills `diario-de-obras` (*Formato de uma tarefa*), `modelo-por-fase` e `bootstrap-pantonic`, `.claude/agents/pantonic-fora-da-caixa.md` e `README.md`. A régua **numérica** não reside em `.claude/agents/pantonic-planner.md` — ela é interna a `GOVERNANCA.md` §3 —, mas o arquivo **remete** a ela, e remissão a régua aposentada conta como residência para efeito do estado final: enquanto a linha de `## Fatos estáveis` que invoca a tabela de classes como régua numérica do papel estiver viva, a propriedade da régua não alcançou o estado final, ainda que toda residência numérica tenha sido reescrita. Residência da responsabilidade pelo lastro: `GOVERNANCA.md` §3.2 e `.claude/agents/pantonic-model-designer.md`, nas duas pontas no mesmo card. Residência da descrição: `docs/planner-spec.md` (novo), uma seção por dimensão da §4, na ordem dela e aberta por `## 0. O que esta especificação não é`. O censo linha a linha, com destino, é a §7; a classe do cabeçalho do card permanece como natureza do trabalho, porque os parsers a leem; ocorrência de outro sentido — escrita atômica em disco, passo atômico de migração — fica intacta; as entradas `RP-1`..`RP-7` e os itens de verificação que não citam ocupação permanecem, são a memória medida do papel; o escopo do papel continua na matriz de `GOVERNANCA.md` §3 (G-SCOPE), e a especificação não é residência nem do escopo nem do protocolo de conduta; tarefa — nenhum card deste plano altera uma tarefa. O que se observa nela, antes e depois, é o padrão sob o qual ela nasce: o nome da unidade no cabeçalho e na doutrina, a régua que definiu o recorte e a presença do campo `Operação do modelo` com o texto e os contratos copiados. Os sete cards deste plano, escritos sob o padrão antigo, são o retrato do antes; a aferição do depois é o primeiro plano decomposto depois da `PLN-T4`, lido por `python .claude/tools/modelo.py show`
- **Camada e fronteira:** documentação, um arquivo. Nenhuma linha de `GOVERNANCA.md` — a autoridade
  está correta e é a fonte de cada literal deste card —, nenhum agente, nenhuma skill, nenhum
  instrumento. `docs/planner-spec.md` **não se toca**: é entrega aceita da `PLN-T6`.
- **Domínio:** *doutrina viva* × *medida histórica* — a distinção que governa este card. Doutrina
  viva é enunciado normativo em vigor: envelhece e se corrige. Medida histórica é observação datada:
  **não se falsifica**, permanece e é preservada por `I-7`. As duas medidas históricas do `README`
  são `:354` e `:1025`, ambas "71 turnos e ~189 mil tokens numa única tarefa atômica", de 2026-07.
- **Arquivos-alvo:**
  - `README.md:121-124` (glossário, entrada `- **Orçamento de turnos**`)
  - `README.md:209,211` (§ da hierarquia qualidade > rota > custo — espelho de `GOVERNANCA.md:78,80`)
  - `README.md:308-309` (parágrafo do `≤30` da rodada de replanejamento)
  - `README.md:311-322` (parágrafo `**Por quê.**`, que defende o teto graduado)
  - `README.md:324-326` (parágrafo `**Onde o gerente intervém.**`, premissa de estouro de teto)
  - `README.md:941-942` e `README.md:946-947` (calibração de tetos como finalidade da série)
  - `README.md:1032` (tabela de trade-offs, linha do teto graduado)
  - `tests/test_doutrina_unidade.py` (acréscimo de uma função; as existentes não se tocam)
- **Passos:**
  1. Em `README.md:121-124`, substituir a entrada inteira `- **Orçamento de turnos** — …` pela
     entrada literal, condensada de `GOVERNANCA.md:188-197` (*Classe do card — natureza, não teto*):
     ```
     - **Classe do card** — `mecanica|implementacao|comportamental|investigacao|redacao`: declara a
       **natureza** do trabalho e calibra a profundidade de quem executa. **Não carrega teto**:
       nenhum número de turnos ou de ocupação dimensiona uma tarefa — a unidade é a operação do
       modelo que o card materializa. O consumo segue medido em `docs/telemetria.tsv` e se lê **na
       série**, nunca como aceite. Onde a regra mora: `GOVERNANCA.md` §3 (§3 desta página).
     ```
  2. Em `README.md:209`, substituir `o
     orçamento de turnos, o modelo por fase e a disciplina de coleta existem` por
     `o dimensionamento pela operação do modelo, o modelo por fase e a disciplina de coleta existem`;
     e em `README.md:211`, substituir `nenhuma rota se muda para caber no orçamento` por
     `nenhuma rota se muda para caber no custo`. São **as mesmas duas substituições** já aplicadas em
     `GOVERNANCA.md:78,80` pelo passo 4a da `PLN-T7`: este é o parágrafo espelho, e o literal é o
     mesmo. Quebra de linha se reajusta a ~100 colunas; palavra não muda.
  3. Em `README.md:308-309`, **remover** o parágrafo inteiro
     `A rodada de replanejamento tem linha própria porque a série dessas rodadas não cabe em ≤30, e dividi-la entre contextos obrigaria a repagar a leitura da decisão em cada fatia.`
     — ele descreve uma linha de uma tabela que não existe mais.
  4. Em `README.md:311-322`, substituir o parágrafo `**Por quê.**` inteiro pelo literal, que
     **preserva o que continua verdadeiro** e descarta a defesa do teto — condensado de
     `GOVERNANCA.md:165-187` (*Diretriz de dimensionamento de tarefa*) e `:188-197`:
     ```
     **Por quê.** Custo e consumo são informativos e não têm valor em isolamento: só rendem insight
     analisados **em conjunto, na série**, e limite não conscientemente delimitado que afete o fluxo
     é vício, não critério. Foi por isso que o teto por classe saiu: ele dimensionava a tarefa por um
     número quando o que a dimensiona é a **operação do modelo** que ela materializa — coesa,
     autossuficiente em contexto. O controle real é **recortar o card pela operação**, e operação que
     não cabe num card coeso é defeito do modelo, não card grande. O registro qualitativo por tarefa,
     quando existe, mora no card "Lições aprendidas na tarefa" do laudo de revisão.
     ```
  5. Em `README.md:324-326`, substituir `escolher uma classe mais generosa *depois* do estouro é falsificar a`
     por `escolher uma classe mais generosa *depois* da entrega é falsificar a`, e
     `se um estouro se repete numa mesma classe, o sinal é de decomposição errada, e a resposta é replanejar`
     por `estouro de contexto numa tarefa é registrado no corpo dela e vira insumo de revisão do modelo — sinal de operação mal recortada`.
     Literal de `GOVERNANCA.md:185-187` e `:196-197`. O resto do parágrafo **não se toca**.
  6. Em `README.md:941-942`, substituir `a calibração dos tetos de que o modelo econômico` por
     `a leitura da série de que o modelo econômico`. O número medido (**11% a 44%**) **não se toca**:
     é medida histórica.
  7. Em `README.md:946`, substituir `É ele quem lê a série para calibrar tetos — e a regra é que`
     por `É ele quem lê a série — e a regra é que`; e em `README.md:947`, substituir
     `(estouro de teto,` por `(estouro de contexto,`.
  8. Em `README.md:1032`, substituir a célula-regra
     `**Teto de turnos graduado por classe, calibrado pela série medida**` e a célula de custo que a
     acompanha pelo literal, condensado de `GOVERNANCA.md:165-197`:
     ```
     | **Nenhum número dimensiona uma tarefa: a unidade é a operação do modelo** | Perde-se o alarme numérico por classe, que era barato de ler. Em troca, o recorte passa a ser por coesão da operação, e estouro deixa de ser sinal de card grande para ser insumo de revisão do modelo — operação mal recortada volta ao modelador. A série continua medida em `docs/telemetria.tsv`, lida em conjunto, nunca como aceite. |
     ```
  9. Acrescentar a `tests/test_doutrina_unidade.py`, **depois** das funções existentes e sem alterar
     nenhuma delas, a função literal:
     ```python
     def test_readme_nao_defende_a_regua_aposentada():
         t = _texto("README.md")
         assert "Orçamento de turnos" not in t
         assert "Um teto único para tudo" not in t
         assert "Teto de turnos graduado por classe" not in t
         assert "calibrar tetos" not in t
         assert "calibração dos tetos" not in t
         assert "não cabe em ≤30" not in t
         assert "71 turnos e ~189 mil tokens" in t
     ```
  10. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - `README.md:354` e `README.md:1025` **não se editam** (`I-7`): são a mesma medida datada de
    2026-07, em duas residências, e a Verificação 8 afere que sobreviveram.
  - Nenhum literal deste card é autoral: cada um condensa `GOVERNANCA.md` §3, cuja âncora está no
    passo. Divergindo o literal do card do texto do hub, **manda o hub** — e a divergência vai na
    linha de retorno como achado, sem edição de `GOVERNANCA.md`.
  - Ajuste de quebra de linha para ~100 colunas é permitido e esperado; mudança de palavra não é.
  - Não editar `docs/planner-spec.md`, `docs/DOC_MAP.md` nem `.claude/README.md`. Não commitar (`I-1`).
- **Não fazer:**
  - Não tocar os sítios de **outro sentido**, conferidos na varredura de 2026-09-22 e que **ficam**:
    `README.md:286-303` (economia de turnos como disciplina de **custo**, que o plano não aposenta),
    `:704`, `:707`, `:722`, `:727`, `:744` (teto de checkpoint e de dossiê, outro sentido).
  - Não "aproveitar" para revisar seção alheia: a varredura foi pelo **conceito aposentado** e por
    todos os nomes que o invocam, e os oito sítios acima são a lista inteira (`AE-24`).
- **Contingências:**
  1. Se uma âncora de linha não casar → localizar pelo literal citado no passo (`grep -n`) e seguir;
     literal ausente → parar e sinalizar `blocked` razão `premissa`, com o literal na linha de retorno.
  2. Se `python -m pytest tests -q` reprovar em teste que este card não criou → parar e sinalizar
     `blocked` razão `premissa`, colando a linha de falha.
- **Testes:** `TR-DU-7` (`test_readme_nao_defende_a_regua_aposentada`); suíte: `python -m pytest tests -q`.
- **Verificação:**

  1. ```
     grep -c 'Orçamento de turnos' README.md
     ```
     → **0**. **Medido em 2026-09-22: 1.**
  2. ```
     grep -c 'caber no orçamento' README.md
     ```
     → **0**. **Medido em 2026-09-22: 1.**
  3. ```
     grep -c 'não cabe em ≤30' README.md
     ```
     → **0**. **Medido em 2026-09-22: 1.**
  4. ```
     grep -c 'Um teto único para tudo' README.md
     ```
     → **0**. **Medido em 2026-09-22: 1.**
  5. ```
     grep -c 'calibração dos tetos\|calibrar tetos' README.md
     ```
     → **0**. **Medido em 2026-09-22: 2** (uma ocorrência de cada, em linhas distintas).
  6. ```
     grep -c 'Teto de turnos graduado por classe' README.md
     ```
     → **0**. **Medido em 2026-09-22: 1.**
  7. ```
     grep -c 'Classe do card — natureza, não teto' README.md
     ```
     → **1** — o parágrafo que a `PLN-T7` instalou sobrevive intacto. **Medido em 2026-09-22: 1.**
  8. ```
     grep -c '71 turnos e ~189 mil tokens' README.md
     ```
     → **2** — as duas medidas históricas preservadas (`I-7`). **Medido em 2026-09-22: 2.**
  9. ```
     pwsh -NoProfile -File .claude/checks/check-readme.ps1
     ```
     → exit **0**, com os **mesmos** números de agentes, skills e guardrails re-medidos no despacho.
     **Medido em 2026-09-22:** `check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s)`.
  10. ```
      python -m pytest tests -q
      ```
      → `<N> passed`, com `<N>` igual ao total re-medido no despacho **mais 1**. **Medido em
      2026-09-22: `276 passed`.**
  11. ```
      python .claude/tools/backlog.py check
      ```
      → `check: OK — nenhuma violação.`, exit **0**. **Medido em 2026-09-22: o mesmo.**
  12. ```
      python .claude/tools/modelo.py check --plano docs/plans/P-0745-planejador-modelo-operacao.md
      ```
      → a **mesma** saída re-medida no despacho e exit **0**: este card não toca o modelo
      (invariância). **Medido em 2026-09-22: exit 0, versão 4.**
- **Pronto quando:** as doze verificações imprimem os valores declarados e nenhum arquivo fora dos
  `Arquivos-alvo` foi editado.
  Por propriedade que a operação altera (`DPN-6`):
  - `agente de planejamento.régua com que ele dimensiona um card` — a parcela desta tarefa: a porta
    de entrada do repositório deixa de **defender** a régua que ela mesma declara aposentada, e a
    única régua que um leitor novo encontra é a operação do modelo — Verificação 1 a 7.
  - As demais entregas desta tarefa são **requisito secundário** (`## Requisitos secundários`), não
    propriedade do modelo: a asserção nova de `tests/test_doutrina_unidade.py`, aferida pela
    Verificação 10.
- **Fora do escopo desta tarefa:** as duas medidas históricas (`I-7`); os sítios de outro sentido
  nomeados no `Não fazer`; e as duas atribuições erradas do `review_evidence.py`, rota `TK-66`/`TK-74`.


---

## 9. Ordem de execução

Fila única, sequencial.

```
PLN-T1 (agregado medido — o antes)
   └→ PLN-T2 (a norma: unidade e limites)
        └→ PLN-T3 (a gramática do card e as skills)
             └→ PLN-T4 (o protocolo do planejador)
                  └→ PLN-T4a (o ponteiro sobrevivente da tabela aposentada — corretivo da OP-3)
                  └→ PLN-T5 (o modelador e o lastro)
                  └→ PLN-T5a (a frase que governa o gate — corretivo da OP-4)   ← Marco 2
                       └→ PLN-T6 (a especificação)
                            └→ PLN-T7 (índice e README)
                            └→ PLN-T7a (o README deixa de defender a régua aposentada —
                                        corretivo da OP-6)   ← Marco 3
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
| O dono dá `no-go` no Marco 1 porque não aceita aposentar o percentual e os tetos (`DPN-3`) | o modelo volta ao modelador para reautoria e o plano segue `blocked`; nada foi editado, porque nenhuma tarefa roda antes do Marco 1, e o `P-0744` continua `superseded` |
| `main` muda durante a execução (a outra janela) e o merge conflita em `GOVERNANCA.md`, no diário ou no `README.md` | é o desenho do dono (§0): a execução inteira corre em `plan/planner-modelo-escopo` e o merge é ato dele, com resolução de conflitos; nenhuma tarefa faz `merge` nem `rebase`. A superfície de conflito já foi **reduzida na origem**: a entrega solta do `P-0741`+`P-0743` virou o primeiro commit desta branch (`e4c1608`), que `main` alcança por `git merge --ff-only`, e a partir dali só este plano diverge |
| O dono veta, no Marco 1, editar o `CLAUDE.md` global dele (`DPN-12`) | a `PLN-T2` perde o passo 14a e as verificações 10 e 11, e nada mais muda — o card fecha só com a cópia do kit; a pendência volta a ser ato do dono, e a linha do `TK-68` a registra |
| A guarda de `tests/test_doutrina_unidade.py` quebra por reformulação legítima futura da doutrina | é o objetivo: quem reformular edita a guarda no mesmo card, como toda regra de conformance do kit |
| O agregado da `PLN-T1` não sustenta uma ou mais dimensões da spec | contingência 1 da `PLN-T1` e contingência 2 da `PLN-T6`: a dimensão existe, diz o que a decisão instituiu e o que faltaria medir |
| A revisão do `README.md` encontra frases fora do censo da §7 que ainda descrevem a forma antiga | contingência 1 da `PLN-T7` fecha só o que `check-readme.ps1` apontar; o resto vira `AE-<n>` para a fila pós-plano, nunca edição "de passagem" |

---

## 12. Agregado medido

### 1. A figura, em uma página

| métrica | valor |
|---|---|
| ocorrências | sem ocorrência no corpus medido |

### 2. Gatilho

| métrica | valor |
|---|---|
| ocorrências | 14 |
| mais antiga | `AE-1`→`RP-1` (`P-0739`), 2026-09-16 |
| mais recente | `AE-23`→`RP-1` (`P-0743`), 2026-09-21 |
| classe dominante | `blocked motivo=premissa` do executor/revisor |
| exemplo | `AE-1`→`RP-1` (`P-0739`), 2026-09-16 |

### 3. Domínio de decisão

| métrica | valor |
|---|---|
| ocorrências | 14 |
| mais antiga | `RP-1` (`P-0739`), 2026-09-16 |
| mais recente | `RP-1` (`P-0743`), 2026-09-21 |
| classe dominante | técnica/tática fechada no próprio contexto (`G-NOASK`) |
| exemplo | `RP-1` (`P-0741`), 2026-09-20 — fronteira com decisão do dono |

### 4. Operacionalização do plano em cards

| métrica | valor |
|---|---|
| ocorrências | 7 |
| mais antiga | `AE-1`/`RP-1` (`P-0739`), 2026-09-16 |
| mais recente | régua de granularidade, `Entregas - P-0743.md`, 2026-09-21 |
| classe dominante | gramática ou campo de card ambíguo |
| exemplo | `AE-1` (`P-0739`), 2026-09-16 |

### 5. Fronteira

| métrica | valor |
|---|---|
| ocorrências | 5 |
| mais antiga | `RP-3` (`P-0739`), 2026-09-16 |
| mais recente | papéis que escrevem no modelo (3→1), `Entregas - P-0743.md`, 2026-09-21 |
| classe dominante | quem escreve ou edita — papel vs ferramenta |
| exemplo | `AE-11` (`P-0740`), 2026-09-18 |

### 6. Instrumento

| métrica | valor |
|---|---|
| ocorrências | 3 |
| mais antiga | `RP-1` de `pantonic-planner.md` (sobre `P-0739`), 2026-09-16 |
| mais recente | `RP-2` de `pantonic-planner.md` (`AE-4`, `P-0740`), 2026-09-18 |
| classe dominante | comando citado em `Verificação` sem execução medida |
| exemplo | `RP-2` de `pantonic-planner.md` (`AE-4`, `P-0740`), 2026-09-18 |

### 7. Custo e teto

| métrica | valor |
|---|---|
| linhas de planejamento | 1 |
| consumo mediano | 183k tk |
| consumo máximo | 183k tk (mesma linha, `F-9`) |
| data primeira | 2026-08-15 |
| data última | 2026-08-15 |
| exemplo | `RPC-P0735-planejamento`, 2026-08-15 |

### 8. A rodada de replanejamento

| métrica | valor |
|---|---|
| ocorrências | 14 |
| replanejamento (planejador) | 13 |
| reparo (consultor, substituto) | 1 — `RP-5` (`P-0740`), 2026-09-18 |
| mais antiga | `RP-1` (`P-0739`), 2026-09-16 |
| mais recente | `RP-1` (`P-0743`), 2026-09-21 |
| classe dominante | técnica/tática sobre achado do executor ou revisor |
| exemplo | `RP-6` (`P-0739`), 2026-09-18 |

### 9. Estatística do próprio acionamento

| métrica | valor |
|---|---|
| rodadas totais | 14 |
| fecharam técnica/tática no contexto | 13 |
| subiram ao dono (como saída da rodada) | 0 |
| decisão do dono antecedente à rodada | 1 — `RP-1` (`P-0741`), 2026-09-20 |
| terminaram com plano `superseded` | 0 |
| mais antiga | `RP-1` (`P-0739`), 2026-09-16 |
| mais recente | `RP-1` (`P-0743`), 2026-09-21 |
| exemplo | `RP-2` (`P-0739`), 2026-09-16 |

### 10. O que esta especificação não fecha

| pergunta que o corpus não responde |
|---|
| se a rodada de reparo conduzida pelo consultor (`RP-5`, `P-0740`) conta como rodada de replanejamento da dimensão 8/9, ou é classe à parte |
| se escalonamento ao consultor (`ESC-*`) é ocorrência da dimensão 2 ou 3, já que não é rodada de replanejamento nem decisão do dono |
| custo de sessão de planejamento cuja `tarefa` na telemetria não contém `planej`/`planner` — a linha única da dimensão 7 pode subcontar |
| por que a dimensão 1 não tem ocorrência medida no corpus fechado |
| se "papéis que escrevem no modelo: 3→1" (`Entregas - P-0743.md`) é decisão retroativa sobre a dimensão 3 ou fato novo da dimensão 5 |

---

## Achados da execução

- **AE-1 — card publicado sem `Arquivos-alvo`, e o gerador de evidência para o loop no passo 6.**
  A `PLN-T1` foi o único dos sete cards deste plano sem o campo `Arquivos-alvo` nem `Entregável`:
  declarava o alvo três vezes em prosa (`Camada e fronteira`, `Restrições desta tarefa`, `Formato
  do agregado que volta`) e nenhuma no campo que o instrumento lê. Medido em 2026-09-22, com a
  tarefa já em `review`: `review_evidence.py --tarefa PLN-T1` sai exit 1 com
  `'PLN-T1' precisa de exatamente um entre 'Arquivos-alvo' e 'Entregável' (tem nenhum)`
  (`rdo.py:313-320`), e sem o dossiê o reviewer não julga. Reparado pelo consultor em
  `docs/plans/P-0745-planejador-modelo-operacao.md:399-403`, transcrevendo para o campo o alvo que
  a prosa do card já fixava — um arquivo só, a declaração mais estreita possível, que só aperta o
  crivo do reviewer. Gerador passa a sair exit 0. Reincidência medida da família `AE-19` do
  `TK-72` (`Arquivos-alvo` fecha o efeito colateral obrigatório). **Rota:** `TK-72`, não matéria nova.
- **AE-2 — verificação que não mede o que pretende, e `Medido antes` deduzido em vez de rodado.**
  A Verificação 3 da `PLN-T1` partia o plano pelo literal `## 12. Agregado medido`, que ocorre
  primeiro **dentro do próprio card** (`Objetivo` e `Formato do agregado`): media prosa do card,
  não a seção entregue. Medido em 2026-09-22: a forma original devolve **6** no arquivo entregue —
  número que satisfaz `≤ 120` pela letra e não afere nada — e **73** no arquivo em `d75e7a6`,
  quando a seção ainda não existia; logo o `Medido antes: o comando falha com IndexError` do card
  era **dedução, e falsa**, segundo defeito da mesma família no mesmo item. A seção real é
  `docs/plans/P-0745-planejador-modelo-operacao.md:1362-1467`, 106 linhas. Reparado pelo consultor
  em `:461-475`: comando ancorado em `^## 12\. Agregado medido` com `re.M`, rodado — **106** no
  arquivo entregue, **0** quando a seção não existe. O critério (`≤ 120`) não mudou; mudou o
  aferidor, e o reparo está declarado no próprio card para o reviewer ver a emenda. O achado é
  autoral do executor da `PLN-T1`, que o reportou na linha de retorno em vez de deixar passar.
  Reincidência medida da família `AE-20` do `TK-72` (`DM-12`: comando de aceite não se deduz, se
  roda). **Rota:** `TK-72`.
- **AE-3 — com trabalho de outro plano não commitado na árvore, nenhum recorte do gerador isola a
  entrega.** O dossiê da `PLN-T1` (`docs/RDO/evidencia/P-0745-PLN-T1.md`, gerado com
  `--desde d75e7a6`) lista 15 arquivos "fora dos alvos e sem atribuição" e 22 "alheios", **todos**
  do `P-0746` e **todos** já sujos no `git status` da abertura da janela, antes de a `PLN-T1` ser
  despachada. `--desde <ref>` só recorta rastreado alterado desde um commit; trabalho não
  commitado e arquivo `??` entram sempre, por construção (`review_evidence.py`,
  `coletar_arquivos_tocados`). Consequência medida: o reviewer recebe ruído maior que a entrega e
  tem material para um `rejeitado` falso, que só não ocorre porque o despacho carrega o aviso à
  mão. Família nova, distinta de `AE-19`/`AE-20` — é do instrumento e da cadência de commit, não
  da autoria do card. Não reparado aqui: `.claude/tools/*` está fora do escopo deste plano.
  **Rota:** `TK-66`/`TK-74`, com `AE-9` e `AE-21` — as três facetas do mesmo recorte.
- **AE-4 — âncora errada na dimensão 6 do agregado, apurada pelo reviewer da `PLN-T1`.**
  Laudo de 2026-09-22, veredito `ressalva` 88% `bloqueante=nenhuma`, recomendação `escalar`:
  a subseção `### 6. Instrumento` da seção `## 12. Agregado medido`
  (`docs/plans/P-0745-planejador-modelo-operacao.md:1419-1427`) cita um identificador que não
  corresponde à ocorrência medida no corpus. Não é defeito de contagem nem de método — é de
  citação, e por isso não bloqueou o veredito. **Tem de ser corrigida antes de a `PLN-T6`
  consumir o agregado como insumo**, senão a especificação herda a âncora quebrada: a `PLN-T6`
  escreve uma seção por dimensão da §4 a partir exatamente deste agregado. Roteado ao consultor
  de plano por `B1` na mesma janela.
  **REPARADO em 2026-09-22 pelo consultor:** a citação era `RP-3` onde o corpus ancora `RP-2` em
  quatro lugares (`pantonic-planner.md:112`, `:320`; `P-0740:6244`, `:6249`), e as três ocorrências
  de `RP-3` no corpus são todas de 2026-09-16 e do `P-0739`. Corrigido em
  `docs/plans/P-0745-planejador-modelo-operacao.md:1425` e `:1427`; a contagem `3` foi conferida e
  **não** alterada. `backlog.py check` e `modelo.py check` exit 0. Nada pendente neste achado; o
  que o reparo revelou de novo está no `AE-5`. **Rota:** fechado no ato pelo consultor nesta
  janela; nada pendente.
- **AE-5 — a tabela de métrica do agregado nomeia os extremos, mas a contagem não é
  re-derivável, e o identificador `RP-<n>` é por plano.** Reparada a `### 6. Instrumento`
  (`AE-4`), ficaram medidos dois defeitos de forma da tabela, não de número. **(i)** A linha
  `ocorrências | 3` declara três ocorrências e a tabela nomeia só duas — a mais antiga e a mais
  recente; a do meio não aparece. O corpus fechado tem **quatro** citações de instrumento
  candidatas (`.claude/agents/pantonic-planner.md:97`, `:103`, `:107`, `:112`/`:320`), logo o
  número `3` não é contradito, mas **qual** das quatro o executor excluiu não se re-deriva da
  tabela — e quem consumir o agregado não tem como reconstruir o conjunto. **(ii)** A dimensão 6 é
  a **única** das dez que cita no formato `RP-<n> de pantonic-planner.md`; as outras nove citam
  `RP-<n>` (`P-<plano>`). O identificador `RP-<n>` é **por plano** (cada plano tem o seu `RP-1`),
  e `pantonic-planner.md` só o hospeda por referência — citar o arquivo em vez do plano da rodada
  deixa o identificador ambíguo, e foi nessa ambiguidade que a âncora errada do `AE-4` sobreviveu
  à autoria. **Consequência para a `PLN-T6`:** ela escreve a seção 6 a partir desta tabela; sem a
  ocorrência do meio nomeada e com a citação no formato divergente, a especificação publica um
  número que não sustenta e uma âncora que não resolve. **Rota:** insumo da `PLN-T6` — ao redigir
  a dimensão 6, nomear as três ocorrências com `arquivo:linha` e uniformizar a citação para
  `RP-<n>` (`P-<plano>`), como nas outras nove dimensões. Não se corrige no agregado: a `PLN-T1`
  está fechada e a contagem medida não está errada.
- **AE-6 — a `PLN-T2` parou por premissa: o passo 14a e a Verificação 11 do card se contradizem
  na cópia do dono das regras globais.** Medido em 2026-09-22, com os passos 1-15 já aplicados na
  árvore. O passo 14a escopa a edição de `C:/Users/panta/.claude/CLAUDE.md` a **dois** blocos — o
  bullet `- **Capacidade**` da Regra 2 e o bullet `- **Orçamento por tarefa atômica**` da Regra 7 —,
  e o card reforça "nada além dos dois blocos nomeados" (`DPN-12`). A **Verificação 11** exige
  `grep -c 'tarefa atômica\|tarefas atômicas'` = **0** naquele arquivo **inteiro**. A **segunda** das
  duas ocorrências que o `Medido antes: 2` contava, e a única remanescente depois do passo 14a,
  está em `C:/Users/panta/.claude/CLAUDE.md:78`
  (`o contexto atravessa várias tarefas atômicas`), que é a **análoga** da que o passo 11 trata em
  `.claude/global/CLAUDE.md:49` — e o passo 11 foi escopado só à cópia do kit. Logo o card manda,
  ao mesmo tempo, não tocar aquela linha e entregar o arquivo com zero ocorrências: as duas coisas
  não coexistem. A **contingência 3** não cobre o caso — ela trata do bloco do passo 14a não existir
  literalmente, e os dois existiam byte a byte, como o `F-15` declara; ambos foram aplicados com o
  literal idêntico ao do kit. **Estado medido da entrega:** Verificações 1-7 e 10 conformes
  (`1, 0, 0, 3, 0, 0, 0, 0`), `.claude/global/CLAUDE.md` em **0** ocorrências, cópia do dono em
  **1**, `tests/test_doutrina_unidade.py` criado, `backlog.py check` e
  `modelo.py check` exit 0. Só a Verificação 11 fica em 1, e por isso o `Pronto quando` não fecha.
  **Rota:** `A3b` do `scrum-master` — a tarefa fica `blocked` razão `premissa`, sem RDO e sem
  laudo, e a matéria sobe ao **planejador** por `G-REPLAN` (`GOVERNANCA.md` §7 item 17). A decisão
  que falta é de uma linha: ou o passo 14a passa a nomear um terceiro bloco na cópia do dono
  (a linha 78, com o mesmo literal que o passo 11 aplica em `.claude/global/CLAUDE.md:49`), ou a
  Verificação 11 deixa de aferir o arquivo inteiro e passa a aferir só os dois blocos. Família do
  `AE-20`/`TK-72` (verificação cujo alvo é mais largo que o escopo que o card autoriza), agora
  medida do lado do **escopo**, não do comando.
  **RESOLVIDO em 2026-09-22 pelo consultor, não pelo planejador:** pelo ato do dono da mesma data
  (`DC-4`, `docs/consultant-spec.md` §3), a parada de executor é triada pela figura, e esta era
  tática. Nenhuma das duas saídas que este achado antecipou foi tomada isoladamente: o defeito
  estava a montante das duas, no censo da §7 (`AE-7`). A rota "sobe ao planejador por `G-REPLAN`"
  registrada acima é a que a `A3b` do `scrum-master` prescrevia e que o ato do dono substituiu.
- **AE-7 — o censo da §7 do arquivo do dono nasceu de um `diff` de dois bullets, e a Verificação 11
  foi escrita contra o arquivo inteiro.** Causa-raiz do `AE-6`, medida em 2026-09-22. O censo da §7
  enumera para `.claude/global/CLAUDE.md` **três** sítios de edição (`:31-36`, `:49`, `:139-143`) e
  para `C:/Users/panta/.claude/CLAUDE.md` apenas **dois** (`:31-36`, `:167-171`) mais a linha dos
  Controles 1.1/1.2 como `fica`. O sítio espelho de `.claude/global/CLAUDE.md:49` — o parágrafo
  *Consequências práticas* da Regra 2, `C:/Users/panta/.claude/CLAUDE.md:78` — **nunca entrou no
  censo**. O motivo está no `F-15`: a conferência entre as duas cópias foi feita por `diff` **sobre
  os dois bullets que o plano reescreve**, e concluiu, corretamente, que eles são idênticos byte a
  byte; o que ela não fez foi varrer o arquivo do dono pela **forma antiga** que o plano aposenta.
  O passo 14a herdou a enumeração do censo ("os dois blocos"), enquanto a Verificação 11 foi escrita
  contra o **arquivo inteiro** — e as duas coisas não fecham. **A restrição não era restrição:** o
  motivo declarado dela, verbatim no passo e no censo, é preservar os Controles 1.1 e 1.2 da Regra 1
  (`TK-68`), e a linha 78 está na Regra 2. **Reparado pelo consultor** (`DC-1`, `DC-3`, `DC-4`): o
  censo ganhou a linha `:78` (`docs/plans/P-0745-planejador-modelo-operacao.md:362`), o card ganhou
  o **passo 14b** (`:618-627`), `Arquivos-alvo` (`:525`), restrições (`:659`, `:666`), contingência 3
  (`:675`) e a cadeia de medição da Verificação 11 (`:728-730`) foram alinhados. Sem drift:
  `modelo.py check` segue exit 0 na versão 3, com as mesmas 6 operações, 3 objetos e 7 propriedades.
  **Regra de autoria que o caso mede:** quando um card edita **duas cópias** de um mesmo documento,
  o censo da cópia secundária se levanta pela **varredura da forma antiga naquela cópia**, nunca por
  `diff` dos trechos já enumerados na cópia primária — `diff` de dois blocos prova que os dois blocos
  são iguais, e não diz nada sobre o terceiro. Família do `AE-20`/`TK-72`, agora medida do lado do
  **censo**, não do comando nem do escopo da verificação. **Rota:** `TK-72`.
  **Conferido pelo reviewer da `PLN-T2` em 2026-09-22 — ponteiro, não achado novo:** a matéria é a
  deste `AE-7` (e do `AE-6`), e o que a revisão acrescenta é a aferição independente de que o
  reparo fechou. Medido por leitura direta do arquivo fora do repositório, que nenhum dossiê de
  evidência alcança: os **três** blocos de `C:/Users/panta/.claude/CLAUDE.md` tocados pelos passos
  14a e 14b — `- **Capacidade**`, `- **Classe do card é natureza, não teto**` e o parágrafo
  `**Consequências práticas:**` (linha 78) — são **byte a byte idênticos** aos de
  `.claude/global/CLAUDE.md`, comparados por leitura em `utf-8` dos três trechos, sem CRLF em
  nenhuma das duas cópias. O `diff` **inteiro** entre as duas cópias são hoje **29 linhas, todas o
  bloco dos Controles 1.1 e 1.2** que só o arquivo do dono tem (as 28 linhas que o censo declara
  como `fica`): os Controles estão intactos, nenhum dos três passos encostou neles, e não sobrou
  divergência em mais lugar nenhum. Verificações 10 e 11 re-rodadas em `0` e `0`. **Rota: sem
  ação** — o `AE-6` e este achado ficam fechados; a regra de autoria que o caso mede segue no
  `TK-72`, que é quem a incorpora à régua de criação de card.
- **AE-8 — o censo da §7 está fechado e incompleto, e os cards que faltam herdam o vão.**
  Apurado pelo reviewer da `PLN-T2` em 2026-09-22, laudo `aprovado` 100% `bloqueante=nenhuma`,
  recomendação `escalar`. `GOVERNANCA.md:78,80` ainda nomeia o **orçamento de turnos** como alavanca
  de qualidade (`Modelo por fase, orçamento de turnos e economia de contexto tornam a qualidade
  sustentável (...) nenhuma rota se muda para caber no orçamento`) — na **mesma §3** de que o
  passo 4 da `PLN-T2` removeu o bullet e a tabela de tetos. O sítio **não está no censo da §7** e
  não é alvo de card nenhum; o `Não fazer` do card proibia o executor de tocá-lo, e ele
  corretamente não tocou. Não rebaixou a entrega: a `PLN-T2` fez tudo que o card mandava.
  **É a mesma família do `AE-7`** — censo levantado por enumeração de sítios conhecidos em vez de
  varredura da forma antiga —, agora medida dentro do próprio `GOVERNANCA.md` e não na cópia
  secundária. **Consequência:** `PLN-T3`..`PLN-T7` herdam o censo fechado e o mesmo `Não fazer`,
  então o vão não se fecha sozinho em nenhum card seguinte. **Rota:** decidir qual card passa a
  possuir a linha **antes do próximo despacho** — roteado ao consultor de plano por `B1` na mesma
  janela, sob as diretivas `DC-1`/`DC-3`/`DC-4` (`docs/consultant-spec.md` §3).
- **AE-9 — arquivo-alvo compartilhado entre dois planos: a atribuição por arquivo não separa as
  entregas, e o `AE-3` era mais largo do que se mediu.** Apurado pelo reviewer da `PLN-T2` em
  2026-09-22. O `AE-3` mediu o fenômeno **por arquivo**: trabalho não commitado do `P-0746` entra
  sempre no recorte `--desde <ref>`, e o dossiê da `PLN-T2`
  (`docs/RDO/evidencia/P-0745-PLN-T2.md:91`) repete o retrato — 15 arquivos "fora dos alvos e sem
  atribuição" e 48 tocados no total, contra **quatro** que são da entrega (`GOVERNANCA.md`,
  `.claude/global/CLAUDE.md`, `docs/RESIDENCIA_DOUTRINA.md`, `tests/test_doutrina_unidade.py`).
  O que não se tinha medido é que a poluição **entra também dentro de um arquivo-alvo**:
  `git diff -U0 d75e7a6 -- GOVERNANCA.md` devolve onze hunks, dez deles nos nove sítios que a
  `PLN-T2` reescreve, e **um de `+51` linhas** no antigo `:354` (hoje `:337-389`), que abre em
  `**Lastro no enunciado, e as duas vias de leitura.**` — matéria do `P-0746`, não desta entrega.
  Como a atribuição do dossiê é **por arquivo** (`docs/RUBRICA_DE_REVISAO.md:48-60`),
  `GOVERNANCA.md` chega ao reviewer marcado `da entrega` **inteiro**, com 51 linhas de outro plano
  dentro. O que deveria haver: ou atribuição por **hunk** quando o arquivo-alvo está sujo com
  trabalho não commitado de outro plano, ou cadência de commit que isole a entrega antes do
  despacho da revisão. **Não rebaixou dimensão nenhuma:** reconciliado sob o passo 3a do protocolo
  de revisão, com os hunks confrontados um a um contra os `Arquivos-alvo`. **Rota:** família
  `TK-66`/`TK-74` (atribuição e recorte de `review_evidence.py`), a que este caso acrescenta a
  faceta **intra-arquivo** — `TK-66` mede atribuição a tarefa nunca despachada e `TK-74` mede alvo
  terminado em barra; nenhum dos dois cobre arquivo-alvo com hunk de outro plano.
  **Não subiu como pendência:** é matéria de instrumento e de cadência, já com tíquete vivo, não
  invalida a rota do `P-0745` e não exige decisão antes do próximo despacho.
- **AE-10 — a varredura que o `AE-7` exigiu, aplicada à residência primária: um sítio órfão, e a
  atribuição dele pela operação, não pela fila.** Executado em 2026-09-22 sobre o `AE-8`, sob
  `DC-1`/`DC-3`/`DC-4`. Varredura de `GOVERNANCA.md` **inteiro** pelas formas que este plano
  aposenta (`orçamento de turnos`, `teto de turnos`, `tabela de tetos`, `tarefa atômica`,
  `% de ocupação`), mais `turnos` e `atômic` soltos, estendida a `docs/RESIDENCIA_DOUTRINA.md` e
  `.claude/global/CLAUDE.md`. **Resultado: `GOVERNANCA.md:78,80` é o único órfão** — duas linhas de
  um mesmo parágrafo, não uma. Todos os demais achados se classificam e **ficam**: `:93` é a negação
  da forma antiga, gêmea do literal que a `PLN-T2` instalou em `:185`; `:123` é `I-7` e a Verificação
  1 da `PLN-T2` exige exatamente 1; `:180`, `:185`, `:192-193` são texto instalado pela `PLN-T2`;
  `:122`, `:135`, `:219`, `:221` são economia de turnos como disciplina de **custo**, que o plano não
  aposenta; `:98` é outro sentido; `:576`-`:615` e `:786` são a janela de orquestração, preservada
  por `DPN-3`. Em `docs/RESIDENCIA_DOUTRINA.md`, o `DR-C` (`:169`, `:183`) é registro datado de
  2026-08 que o próprio documento já supera em `:218` — mesma classe do `:123`, e reescrevê-lo seria
  falsificar histórico. `.claude/global/CLAUDE.md`: zero órfãos.
  **Atribuição:** o sítio passa a ser da **`PLN-T7`** (`OP-6`), e a razão é a operação, não a fila —
  a `OP-6` nomeia a matéria verbatim ("o orçamento de turnos por classe sai de onde quem chega o
  lia"), o campo `precisa de` dela já declara `GOVERNANCA.md` §3 como residência da régua, e o passo
  4 do mesmo card já remove o parágrafo gêmeo em `README.md:305`: é um ato só, em duas residências
  espelho. Censo da §7 (`:346`), `Arquivos-alvo`, passo **4a**, Verificação **4a** e a frase de
  contagem do `Pronto quando` (`I-6`) alinhados no mesmo ato.
  **Urgência reavaliada com medição:** nenhuma verificação de `PLN-T3`..`PLN-T7` faz grep de
  `GOVERNANCA.md` pela forma antiga, logo o sítio **não bloqueava a `PLN-T3`**. O risco real era o
  outro: o plano fechar com a §3 se contradizendo — e esse está fechado.
  **Regra de autoria que o caso soma ao `AE-7`:** sítio órfão se atribui ao card cuja **operação**
  já o cobre pelo texto e pelo contrato de objetos; se nenhuma operação o cobrir, o caminho é card
  corretivo somado à operação que repara — e aí a matéria é do planejador ou do modelador, porque a
  lista `tarefas:` mora dentro da `## 1. Modelo conceitual`. **Rota:** `TK-72`.
- **AE-11 — `modelo.py` confere lastro só numa direção: operação → tarefa, nunca tarefa → operação.**
  Medido em 2026-09-22 em `.claude/tools/modelo.py:350-354`: o instrumento emite `V1` (operação sem
  tarefa) e `V3` (tarefa inexistente citada por uma operação), mas **não** verifica que todo card de
  `## 8. Tarefas` seja citado por alguma operação. Consequência: um card acrescentado a um plano sem
  atualizar a lista `tarefas:` da operação que ele materializa sai **lastro órfão e invisível** —
  `modelo.py check` continua verde e a contagem de tarefas continua batendo com a lista, não com o
  plano. Foi o que impediu, neste caso, a rota "card corretivo `PLN-T2b` somado à `OP-1`", que a
  norma instalada pela `PLN-T2` prescreveria: sem poder tocar a `## 1. Modelo conceitual`, o card
  novo nasceria fora do alcance do instrumento. **Rota:** linhagem do `P-0746` (lastro do modelo) /
  `TK-66`. Sem ação nesta janela — `.claude/tools/*` não é objeto do `P-0745`.
- **AE-12 — âncora de linha sobre alvo compartilhado não é invariante, e a contingência de âncora
  não cobre descrição errada de tamanho.** Apurado pelo reviewer da `PLN-T3` em 2026-09-22, laudo
  `ressalva` 94% `bloqueante=nenhuma`, recomendação `seguir com ressalva`. O card declarava
  `Arquivos-alvo: .claude/skills/diario-de-obras/SKILL.md:206-225`; o heading real estava em **245**
  — desvio de **+39** produzido pelo trabalho não commitado do `P-0746` no mesmo arquivo. Pior que o
  deslocamento: o Passo 2 descreve o bloco cercado como *"linhas 209-226"*, **18 linhas**, e ele tem
  **14** (real: `253-268`). A **Contingência 1** do card cobre a âncora que não casa, mas **não**
  cobre a descrição errada do **tamanho** do bloco — e um executor que confiasse na contagem
  inseriria as duas linhas no lugar errado. O card só ficou executável porque a orquestração
  re-derivou as âncoras no despacho e mandou localizar os dois bullets **pelo literal**, não pela
  posição. É o critério (xviii)/`AE-49` aplicado à **âncora de linha** em vez da contagem de corpus:
  âncora sobre arquivo que outra entrega desloca **não é invariante** ao que o card possui.
  **Família `AE-2`/`AE-6`/`AE-7`**, agora medida na âncora e não na verificação nem no censo — é a
  quarta ocorrência da mesma raiz nesta janela: o card afirma sobre a árvore um número que envelhece
  entre a autoria e o despacho. **Rota:** `TK-72`, somada à régua de autoria de card.
  **Segundo achado do mesmo laudo, rota `sem ação`:** a Verificação 5 publicava
  `Medido antes: 262 passed` (2026-09-21, antes da `PLN-T2`), defasado em **+9** do total real no
  despacho (**271**). É o **único** dos seis `Medido antes` do card que estava errado — V1 (1),
  V2 (0), V3 (1), V4 (`:1,:1,:1`) e V6 conferem com o estado pré-entrega re-medido. A **forma** do
  item é a conforme (relação ao total re-medido **mais 1**, com o literal como referência datada),
  então o aceite se sustenta com o valor real: **272 = 271 + 1**, re-rodado na revisão. Por isso
  não entra na família acima.
- **AE-13 — a décima residência da régua ficou fora de todo card, e o censo da §7 não podia
  apanhá-la.** Apurado pelo reviewer da `PLN-T4` em 2026-09-22 (laudo `aprovado` 100%,
  `bloqueante=nenhuma`, recomendação `escalar`) e confirmado pelo modelador no mesmo dia.
  `.claude/agents/pantonic-planner.md:36-37`, em `## Fatos estáveis`, diz *"Nenhum teto se escreve
  no card: a régua numérica é a tabela de classes de `GOVERNANCA.md` §3, interna a este papel"* — e
  segue **byte-idêntica ao `HEAD`**. A tabela que ela invoca foi **aposentada pela `PLN-T2`** às
  07:23 de 2026-09-22, onze horas antes da entrega da `PLN-T4`: o ponteiro está quebrado. Nenhum
  card do `P-0745` tem essa linha nos `Arquivos-alvo`, e a `PLN-T4` **não podia** corrigi-la sem
  sair dos alvos declarados — a entrega dela está correta e fechou em 100%.
  **Por que o censo não a apanhou:** a varredura de 2026-09-21 buscou `atômic|atomic` e
  `50%|60%|~80 linhas|fatias verticais`; a linha diz *"tabela de classes"* e não casa nenhum dos
  dois padrões. É **meia mudança de papel publicada** — a classe de defeito que o `P-0743` mediu e
  que este plano existe para não repetir.
  **Ato de modelo executado:** o reviewer devolveu dossiê de `conflito` e o modelador o acatou,
  registrando a **versão 4 pendente** num bloco `## 1A` irmão (a `## 1` vigente não foi tocada fora
  da tabela de versões). Duas células, nenhuma operação alterada: o contrato do `agente de
  planejamento` passa a enumerar **dez** regiões de conduta — as oito anteriores mais
  `## Fatos estáveis` e `## O que você NUNCA faz`, esta editada pela própria `PLN-T4` — e declara a
  enumeração **fechada**; e o estado final de `régua com que ele dimensiona um card` passa a exigir
  que nenhuma residência da conduta **remeta** à tabela aposentada. A régua **numérica** continua
  não residindo no agente: ela é interna a `GOVERNANCA.md` §3, e o que o contrato acrescenta é que
  *remissão* a régua aposentada conta como residência para efeito do estado final. **O dono valida
  ou recusa a versão 4 no Marco 2**, que é `modelo.py show` depois da `PLN-T5`.
  **Aviso operacional para o Marco 2, medido pelo modelador:** `modelo.py show --drift` compara
  propriedades, operações e estado, mas **não compara a célula `contrato`** — rodando só `--drift`
  o dono vê uma das duas mudanças. O marco tem de rodar também `--pendente`, que renderiza o bloco
  inteiro com o contrato.
  **Rota:** card corretivo `PLN-T4a` somado à `OP-3`, roteado ao consultor por `B1` na mesma
  janela. A §7 ganha linha nova com destino, e o corpus se re-varre por
  `tabela de classes|tabela de tetos|teto por classe` antes da `PLN-T7` — se este ponteiro escapou,
  outros da mesma família podem ter escapado.
- **AE-14 — o primeiro card corretivo do plano, a varredura que o autorizou e dois vãos de
  instrumento que ele expôs.** Medido em 2026-09-22, em resposta ao `AE-13`, sob `DC-1`/`DC-3`/`DC-4`.
  **(i) Varredura, não enumeração** (regra do `AE-7`, terceira aplicação): varrido
  `tabela de classes|tabela de tetos|teto por classe|tetos por classe|régua numérica` em todo
  `*.md`/`*.py`/`*.ps1` do repositório, ampliado para `teto` e `turnos` em todo o `.claude/`.
  **`.claude/agents/pantonic-planner.md:36-37` é o único órfão vivo.** Ficam, classificados:
  `pantonic-reviewer.md:62,155` (negações verdadeiras, classe do `GOVERNANCA.md:93`);
  `pantonic-planner.md:97,264,412` (outro sentido); `pantonic-planner.md:258,260` e
  `pantonic-executor.md:74,78-80` (texto novo alinhado); `GOVERNANCA.md:192`,
  `RESIDENCIA_DOUTRINA.md:142`, `tests/test_doutrina_unidade.py:2` (texto que **registra** a
  aposentadoria); `README.md:305` (já é da `PLN-T7`); `CHANGELOG.md:196,215` e
  `RECOMENDACOES_CONSUMO_GLOBAL.md:71` (registro datado, `I-7`); e os tetos de outro sentido das
  cinco skills. **(ii) Card corretivo `PLN-T4a`**, somado à `OP-3` na forma que a própria `PLN-T2`
  instalou em `GOVERNANCA.md` §3 — resíduo de `OP-3` e não de `OP-1`, porque quem aposentou a
  tabela foi a `OP-1` em `GOVERNANCA.md`, mas o ponteiro sobrevivente está na residência da `OP-3`.
  Posicionado **antes** da `PLN-T5`: o estado final que a versão 4 pendente exige — nenhuma
  residência da conduta remetendo à tabela aposentada — é o que o dono valida no Marco 2, e validá-lo
  sobre corpus que ainda o contradiz mediria o modelo contra o mundo errado. **(iii) Vão de
  instrumento confirmado (`AE-11`), agora com prova:** com o `PLN-T4a` escrito e fora de toda lista
  `tarefas:`, `modelo.py check` sai **exit 0** e imprime `8 tarefas` — ele conta os cards de `## 8`
  e **nunca** confere card → operação. Lastro furado é silencioso, e por isso o `Ato de modelo`
  desta rodada é obrigatório, não opcional. **(iv) Vão de instrumento novo:** `V14` confere que os
  sub-bullets do campo `Operação do modelo` **existem**, nunca que a cópia está **corrente** — com
  a versão 4 pendente do Marco 2, `PLN-T6` e `PLN-T7` carregam contrato da versão 3 e nada acusa.
  Resolvido sem antecipar o dono: **passo 0 condicional** na `PLN-T6`, que lê o veredito já
  registrado do Marco 2 e recopia ou não, e passo 0 de conferência na `PLN-T7` — o executor
  materializa um veredito, não decide. **Rota:** (iii) e (iv) para a linhagem do `P-0746`/`TK-66`;
  (i) e (ii) para o `TK-72`, como terceira medição da família "censo por enumeração".
  **Regra de autoria que o caso soma:** varredura de censo se faz pelo **conceito aposentado** e
  por todos os nomes que o invocam, não pelos padrões que a rodada anterior usou — a de 2026-09-21
  buscou `atômic|atomic` e `50%|60%|~80 linhas|fatias verticais`, e "tabela de classes" não casa
  nenhum dos dois.
- **AE-15 — a raiz das seis ocorrências: a régua de autoria prende o número re-derivável à linha
  de aceite, e os seis defeitos moraram todos fora dela.** Apurado pelo reviewer da `PLN-T4a` em
  2026-09-22 (laudo `aprovado` 100%, `bloqueante=nenhuma`, recomendação `escalar`). O card da
  `PLN-T4a` afirmava, em `Arquivos-alvo` e em `Restrições desta tarefa`, *"as duas funções já
  existentes"* de `tests/test_doutrina_unidade.py`; no despacho havia **quatro** (a `PLN-T2` criou
  duas, a `PLN-T3` a terceira, a `PLN-T4` a quarta). **Agravante:** este card foi escrito **hoje,
  minutos antes do despacho**, pelo consultor — e ainda assim errou a contagem. Inócuo na entrega:
  o executor nomeou o erro na linha de retorno, não decidiu nada e não alterou nenhuma das quatro.
  **A raiz, e é o achado que importa:** a §8 da rubrica de revisão, critérios (v) e (xiii), prende
  o *"número re-derivável por comando, nunca copiado"* à **linha de aceite**. Os seis defeitos desta
  janela moraram em `Arquivos-alvo`, em `Restrições`, em descrição de tamanho de bloco e em censo —
  **todos fora do bloco `Verificação`**. A régua, como está escrita, **não alcança a classe**, e é
  por isso que seis ocorrências passaram por ela sem serem apanhadas: `AE-2` (verificação que mede
  a coisa errada), `AE-6` (escopo mais estreito que a verificação), `AE-7` (censo por `diff` de dois
  bullets), `AE-12` (âncora de linha e tamanho de bloco), `AE-13` (residência fora do censo) e esta.
  **Rota:** emenda à §8 de `docs/RUBRICA_DE_REVISAO.md`, estendendo o critério a **qualquer
  afirmação do card sobre o estado da árvore** — contagem de funções, de regiões, de sítios,
  descrição de tamanho —, não só às linhas de aceite. É matéria de **kit**, fora do escopo do
  `P-0745`: vai para o `TK-72`, que é a régua de autoria de card, como a medição que fecha a família.
  **Segundo achado do mesmo laudo, rota `sem ação`:** o literal `Medido antes: 271 passed` da
  Verificação 4 estava vencido no despacho (total re-medido: **273**), **sem dano**, porque a linha
  é **relação** (*"`<N>` igual ao total re-medido no despacho mais 1"*) e o literal é referência
  datada. Registrado como confirmação de que a **forma-relação absorve** o envelhecimento que a
  forma-constante não absorveria — é o contraexemplo que dá a solução da família acima.
- **AE-16 — a forma-relação aplicada aos três cards abertos, e o discriminante que a medição
  revelou: o número não envelhece por ser número, envelhece por ser de outro.** Feito em
  2026-09-22 em resposta ao `AE-15`, sob `DC-1`/`DC-3`/`DC-4`. Varridos os três cards abertos por
  toda afirmação numérica **sobre a árvore**, dentro e fora do bloco `Verificação` — que é onde
  cinco dos seis defeitos da família moraram. **Dez sítios, em dois cards; a `PLN-T6` estava
  limpa.** Reparados: `PLN-T5` V1-V4 re-datados, valores da autoria confirmados por re-medição;
  `PLN-T5` V5 de constante para **relação de invariância** ("a mesma saída re-medida no despacho,
  byte a byte") — o que se afere é que **este card** não moveu o `P-0743`, nunca que o `P-0743`
  seja imóvel; `PLN-T5` V6 com a constante de apoio corrigida de `262 passed` para `274 passed`;
  `PLN-T7` Objetivo, de "as **nove** linhas" para "todas menos uma, a `README.md:366`" — alvo que
  não envelhece; `PLN-T7` V2, **que já havia envelhecido**, de `9` para `11`; `PLN-T7` V3
  re-datado; e `PLN-T7` V5 de constante para relação de invariância nos números de agentes, skills
  e guardrails. **Medição que corrige a intuição:** das dez, **seis constantes continuavam exatas**
  e quatro estavam ou ficaram erradas. Logo o defeito **não é "ser constante"**. O discriminante é
  a **autoria do número**: número sobre o que o próprio card escreve é causado por ele e não
  envelhece — a `PLN-T6` inteira é desta classe, e por isso saiu limpa; número sobre o **resto da
  árvore** envelhece entre a autoria e o despacho, porque outros cards e outros planos o movem, e
  só sobrevive como **relação** ("igual ao re-medido no despacho ± n") ou **invariância** ("o mesmo
  re-medido no despacho"). **Caso que fecha a demonstração:** a V4 do `PLN-T4a` publicou
  `271 passed` e o real no despacho era `273` — dois testes de diferença em minutos, sem dano
  nenhum, porque a linha era relação. A `PLN-T7` V2 envelheceu duas entradas em um dia, também sem
  dano, pela mesma razão. **Rota:** a emenda da §8 de `docs/RUBRICA_DE_REVISAO.md` **não** foi
  feita — é régua de kit, fora do objeto do `P-0745`, e vai ao `TK-72` com o texto já redigido,
  para custo zero de redação na abertura do tíquete.
  **Texto proposto para a emenda, a aplicar fora desta janela:** *"O número que um card afirma é
  **medição**, e medição envelhece. O critério vale em **todo campo do card** — `Arquivos-alvo`,
  `Passos`, `Restrições`, `Não fazer`, `Objetivo` e `Pronto quando`, não só `Verificação`. Número
  sobre o que o próprio card escreve pode ser constante: o card é a causa dele. Número sobre
  qualquer outra parte da árvore se escreve como **relação** — `igual ao re-medido no despacho
  ± n`, `o mesmo re-medido no despacho`, `todos menos <o nomeado>` — ou vem acompanhado do comando
  que o re-deriva. Contagem de itens de um conjunto que o card não cria ('as duas funções', 'as
  nove linhas', 'os três blocos') é a forma proibida: nomeia-se o conjunto pela regra, nunca pela
  cardinalidade. Casos medidos: `AE-2`, `AE-6`, `AE-7`, `AE-12`, `AE-13`, `AE-15` e `AE-16` do
  `P-0745` — seis autores distintos, dois planejadores, três executores e o consultor."*
- **AE-17 — o aferidor mede a pergunta errada: `grep -c` conta linhas, e quatro verificações dos
  cards abertos perguntavam ocorrência, distinção ou caixa.** Sétima ocorrência da família do
  `AE-2`, e a primeira em que o defeito é **semântica de comando**, não número envelhecido.
  Disparo: a `PLN-T5` voltou `blocked premissa` em 2026-09-22 com a entrega **correta** na árvore —
  o literal do passo 3 é uma linha física única que carrega as duas menções de `V3`, e
  `grep -c 'V3'` devolveu **1** onde a V1 exigia **≥2**; `grep -o 'V3' … | wc -l` devolve **2**. O
  executor inseriu o literal verbatim, não reflowou e parou: conduta correta, porque reflow seria
  decidir ponto de quebra que o card não autoriza (`Regra 8`). **Varredura dos três cards abertos
  pela mesma semântica — quatro defeitos, não um:** **(i)** `PLN-T5` V1, reparada em duas
  verificações por literal próprio, forma **mais estrita** que a original — em vez de "duas
  ocorrências quaisquer da sigla", cada uma das duas afirmações tem de existir; a entrega **não se
  tocou**, porque reescrever entrega correta para o número fechar inverte o `DM-12`.
  **(ii)** `PLN-T6` V2, `grep -c 'DPN-' ≥5` para aferir "uma âncora por decisão": errava nos dois
  sentidos — cinco decisões numa linha dariam `1`, a mesma decisão em cinco linhas daria `5`.
  Trocada por `grep -o 'DPN-[0-9]*' | sort -u | wc -l`, exercitada contra um arquivo que existe:
  **13** distintas contra **74** linhas. **(iii)** `PLN-T7` V3, com **três** defeitos sobrepostos e
  que teria repetido este mesmo bloqueio **no card que fecha o plano**: sem `-i` não enxergava
  `**Tarefa atômica**` de `README.md:94` (10 linhas contra 11 com `-i`); esperava `1` quando o
  pós-estado correto é **2**, porque `README.md:1036` carrega a mesma medida histórica de
  `README.md:366` e **não estava no censo**; e contava linhas onde `README.md:382` tem **duas**
  ocorrências (12 ocorrências em 11 linhas). Reparada para `grep -ic … = 2`, mais a V3a de
  ocorrências. **(iv)** censo da §7: as âncoras da §11 andaram uma linha (`824,825` → `825,826`) e
  `README.md:1036` entrou como **fica** (`I-7`). **O que este achado acrescenta ao `AE-16`, sem
  contradizê-lo:** aquela régua pergunta *de quem é o número* e resolve o envelhecimento; esta
  pergunta *o comando responde à pergunta da linha?* e resolve a semântica. As duas são necessárias
  — a V1 da `PLN-T5` passou pela varredura do `AE-16` e foi classificada "exata", porque o
  `Medido antes` **estava** exato; o que estava errado era o aferidor. **Regra que o caso fixa:**
  toda linha de `Verificação` declara, além do valor esperado, **que pergunta o comando responde**
  — presença de literal, contagem de linhas, contagem de ocorrências ou contagem de identificadores
  distintos —, e o comando se escolhe pela pergunta: `grep -c` só quando a pergunta é sobre
  **linhas** e o alvo não pode repetir na mesma; `grep -o … | wc -l` para ocorrências;
  `grep -o … | sort -u | wc -l` para distinção; `-i` sempre que o corpus mistura caixa.
  **Rota:** `TK-72`, junto com a emenda da §8 da rubrica proposta no `AE-16` — os dois critérios
  entram no mesmo ato, porque são as duas metades da mesma régua.
- **AE-18 — a doutrina publica a transição `blocked` → `review` e o instrumento a recusa.**
  Medido em 2026-09-22, ao materializar o desbloqueio da `PLN-T5`.
  `.claude/skills/diario-de-obras/SKILL.md:102` publica a transição, com gatilho e condição:
  *"`blocked` → `review` — a rodada de replanejamento corrigiu o **aceite** de um `blocked premissa`
  cuja entrega material já está na árvore (`G-REPLAN`, saída (c)); nenhum retorno novo de executor é
  exigido — **gatilho 1**: o `scrum-master` invoca o `pantonic-reviewer`"*. O par
  `("blocked", "review")` **não existe** em `_TRANSICOES` de `.claude/tools/backlog.py:1166-1179`,
  que só admite `blocked` → `ready` e `blocked` → `cancelled`. Consequência medida: o caminho
  doutrinário é recusado pelo instrumento, e o loop alcança o mesmo estado por
  `blocked` → `ready` → `in-progress` → `review`, três chamadas em vez de uma, com o mesmo efeito e
  sem executor — o que a linha 102 autoriza explicitamente. É **meia mudança publicada** na direção
  inversa das outras desta janela: aqui a doutrina andou e o instrumento ficou. **Não reparado:**
  `.claude/tools/*` não é objeto do `P-0745`. **Rota:** linhagem do `P-0746`/`TK-66`, junto com o
  `AE-11` (o instrumento não confere card → operação) — as duas são defasagem do mesmo instrumento
  em relação à doutrina que ele deveria aferir.
- **AE-19 — o gate do modelador ficou meio aberto: a frase antecedente contradiz o literal novo.**
  Apurado pelo reviewer da `PLN-T5` em 2026-09-22, laudo `aprovado` 100% `bloqueante=nenhuma`,
  recomendação `escalar`. A `PLN-T5` devolveu ao **lastro do planejador** as violações `V1` e `V3`,
  publicando-o nas duas pontas (`GOVERNANCA.md` §3.2 e `.claude/agents/pantonic-model-designer.md`)
  — e as duas pontas foram conferidas concordantes. Mas a frase **antecedente** daquele agente,
  fora do recorte do passo 3 e **fora dos `Arquivos-alvo` do card**, continua dizendo: *"é da seção
  toda violação que o instrumento não indexa pelo `<ID>` de uma tarefa: as de `secao`, as de
  `OP-<n>` e as de `objeto`"*. Medido contra `tests/fixtures/modelo/plano-invalido.md`:
  `modelo.py` emite `V1 OP-2` e `V3 OP-3`, isto é, **indexadas por `OP-<n>`**. Pela regra
  antecedente elas são "da seção" e o ato do modelador não se conclui; pelo literal novo elas são
  do lastro do planejador e o ato se devolve. **As duas leituras coexistem no mesmo arquivo.**
  Defeito do **dossiê**, não da entrega: o executor não podia editar aquela região, e por isso
  `criterio-de-pronto` ficou `conforme`. **Urgência:** a recópia dos contratos prevista para depois
  do Marco 2 (`AE-14` item iv) **herda a ambiguidade** se nenhum card a fechar. **Rota:** roteado
  ao consultor por `B1` na mesma janela, sob `DC-1`/`DC-3`/`DC-4`. Oitava ocorrência da família do
  censo por enumeração (`AE-7`, `AE-10`, `AE-13`, `AE-17`): o recorte do passo alcançou a frase que
  se queria mudar e não a frase que a governa.
- **AE-20 — a varredura do gate do modelador: um sítio que governa, e uma enumeração de códigos
  que envelheceu dentro da mesma frase.** Medido em 2026-09-22 em resposta ao `AE-19`, sob
  `DC-1`/`DC-3`/`DC-4`; oitava ocorrência da família do censo por enumeração (`AE-7`, `AE-10`,
  `AE-13`, `AE-17`). **(i) A contradição, confirmada por mapeamento completo:** levantado em
  `.claude/tools/modelo.py` o rótulo de indexação de cada código `V1`..`V21` — `secao`: V13, V19,
  V20; `OP-<n>`: V1, V3, V5, V8, V9, V10, V11, V12, V16, V18; `objeto`: V6, V7, V15, V17, V21;
  `<ID>` de tarefa: V2, V4, V14. O critério antecedente de
  `.claude/agents/pantonic-model-designer.md:24-27` ("`OP-<n>` ⇒ da seção") está **correto para
  oito dos dez**; as duas exceções são exatamente `V1` e `V3`, que a `PLN-T5` publicou como lastro
  do planejador. O reparo não reescreve o critério — **nomeia a exceção onde o critério é
  enunciado**. **(ii) Defeito segundo, que o laudo não viu e a varredura viu:** a mesma frase
  enumera as violações de `objeto` como `(V6, V7, V15, V17)` — **quatro de cinco**. `V21 objeto —
  objeto sem lastro declarado`, criada pelo `P-0746`, **não aparece uma única vez** no arquivo do
  agente (`grep -c 'V21'` = 0). Corrigido pela régua do `AE-16`/`AE-17`: a lista sai e entra a
  regra — a classe se lê pelo **rótulo com que o instrumento indexa**, nunca por lista de códigos,
  porque o vocabulário cresce e lista fechada envelhece. **(iii) Varredura das 111 linhas:** este é
  o **único** sítio que governa ou contradiz o que a `PLN-T5` publicou. Conferidos concordantes e
  mantidos: `:55-57` (na autoria ele preenche `tarefas:` por convenção — é o que faz `V3` disparar
  por construção), `:107`, `:39-44`, `:3`, `:104`. **(iv) Rota:** card corretivo `PLN-T5a`,
  somado à `OP-4` porque o texto da operação diz literalmente "em vez de **travar a devolução** de
  quem escreve o modelo" e a frase antecedente é o que ainda trava; censo da §7 com o sítio;
  `Ato de modelo` de lastro devolvido para a lista `tarefas:` da `OP-4` nos dois blocos.
  **(v) Natureza do ato:** não é matéria nova — é a **conclusão de um colateral que o dono aprovou
  em 2026-09-22** e que a `PLN-T5` entregou pela metade por defeito de recorte, e por isso não se
  escala de novo. **(vi) Cadência, corrigida:** a recópia de contratos do `AE-14` (iv) **não**
  propaga esta ambiguidade — ela copia texto do modelo, não do arquivo do agente. Nada antes do
  Marco 2 depende deste reparo. Quem sofre a ambiguidade é o modelador frio na **próxima autoria
  de plano sem cards**, que é o cenário que a `PLN-T5` abriu. **(vii) Duas lições da janela
  embutidas no card corretivo:** cláusula explícita de reflow no passo — cuja ausência foi o que
  bloqueou a `PLN-T5` (`AE-17`) — e literais de verificação escolhidos para caber **numa linha
  física**, porque a frase-alvo se parte entre as linhas 24 e 25 e um `grep` de linha única sobre
  ela devolve `0`, medido antes de publicar. **Rota:** `TK-72`.
- **AE-21 — arquivo-alvo não rastreado entra colado inteiro no dossiê de evidência.** Apurado pelo
  reviewer da `PLN-T5a` em 2026-09-22 (laudo `aprovado` 100%, recomendação `seguir`; achado de alvo
  `dossiê`, não rebaixou dimensão). Terceira faceta da família do `AE-3`/`AE-9`, e a primeira sobre
  arquivo **não rastreado**: `tests/test_doutrina_unidade.py` está em `??` no `git status` — foi
  criado pela `PLN-T2` e nunca commitado —, e por isso `review_evidence.py` o entrega **inteiro**
  ao revisor, sem separar a função que esta tarefa acrescentou das seis que as entregas anteriores
  já haviam aceito. Somado aos 15 arquivos do `P-0746` que saem como "fora dos alvos e sem
  atribuição", a reconciliação exigiu **mtime** mais confronto com o dossiê de evidência da
  `PLN-T5`. **Recapitulando a família:** `AE-3` mediu o fenômeno por arquivo (trabalho não
  commitado de outro plano entra sempre no recorte `--desde <ref>`); `AE-9` mediu dentro de um
  arquivo-alvo rastreado (hunk de outro plano chega marcado `da entrega`); este mede o arquivo
  **não rastreado**, onde não há sequer hunk a separar. As três têm a mesma causa a montante —
  **a árvore carrega trabalho não commitado de dois planos** — e o mesmo par de remédios: atribuição
  por hunk no instrumento, ou cadência de commit que isole a entrega antes do despacho da revisão.
  **Rota:** `TK-66`/`TK-74`, com `AE-3` e `AE-9`. Sem ação nesta janela: `.claude/tools/*` não é
  objeto do `P-0745`.
- **AE-22 — três achados de ofício da revisão da `PLN-T6`, nenhum bloqueante, todos com rota.**
  Laudo `aprovado` 100% `bloqueante=nenhuma`, recomendação `seguir`, 2026-09-22.
  **(i) A rota do `AE-5` era indeterminável pela metade, e a recusa do executor foi correta.** O
  `AE-5` roteou à `PLN-T6` nomear as **três** ocorrências da dimensão 6 do agregado e uniformizar a
  citação. O executor entregou a metade que se deriva — os extremos, com `arquivo:linha` re-medido
  (`pantonic-planner.md:109` para `RP-1` (`P-0739`) e `:124`/`:342` para `RP-2` (`P-0740`)), no
  formato `RP-<n>` (`P-<plano>`) das outras nove, que é o item (ii) do `AE-5` — e **recusou nomear
  a terceira**, porque o agregado fixa os extremos e a contagem `3` sem dizer qual das duas
  candidatas (`:115` `RP-2` `P-0739`, `:119` `RP-3` `P-0739`) entrou. O reviewer confrontou as
  quatro linhas, confirmou que existem e que o **próprio corpo do `AE-5`** já dizia que a exclusão
  não se re-deriva. Escolher seria afirmação sem âncora, vedada pelo card. **O defeito é do
  roteamento, não da entrega:** rotear a um card a correção de um dado que o corpus não permite
  reconstruir produz tarefa parcialmente impossível. **Rota:** a pergunta ficou registrada na
  seção 10 de `docs/planner-spec.md`; fechá-la exige o critério de inclusão que a `PLN-T1` usou, e
  isso é matéria de quem tiver o corpus aberto, não deste plano.
  **(ii) Literal de corpus sem data, no próprio card.** A Verificação 2 da `PLN-T6` ilustrava com
  `74` linhas contendo `DPN-`; o real mede **79** hoje e **65** em `d75e7a6`. O número é
  ilustrativo e o critério vigente é a forma nova — `grep -o 'DPN-[0-9]*' | sort -u | wc -l` = **13**
  distintas, que confirmou —, então não houve dano. É a família `AE-16` na forma exata que ela
  prevê: constante sobre a árvore, sem data, num campo de `Verificação`. **Rota:** `TK-72`.
  **(iii) Duas imperfeições de redação em `docs/planner-spec.md`, sem custo de dimensão.**
  `:127` fecha a seção 6 com *"É a primeira vez que uma mudança de doutrina do papel nasce com
  aferição automática em vez de só com texto"* — **sem âncora** no agregado nem em `DPN`, e a razão
  da `DPN-9` cita aferição por invariância medida já no `P-0740`. É o **único floreio em 217 linhas**
  que ancoram todo número, data e identificador; reversível por deleção, sem claim dependendo dele.
  E a linha `Âncoras` da seção 5 é a única que aponta para a seção 10 omitindo a citação
  `agregado, dimensão 10, Nª linha` que as seções 2, 7, 8 e 9 trazem. **Rota:** passagem da
  `PLN-T7` ou card corretivo; **nenhuma bloqueia o Marco 3**.
- **AE-23 — o censo da §7 fechou incompleto e o `README` §3 saiu do plano contradizendo a si
  mesmo.** Apurado pelo reviewer da `PLN-T7` em 2026-09-22, laudo `ressalva` **83%**
  `bloqueante=nenhuma`, recomendação `escalar` — o menor percentual da janela, e no card que fecha
  o plano. O passo 6 da `PLN-T7` instalou em `README.md:306` o parágrafo que **aposenta** a tabela
  de tetos. Mas ficaram fora do censo, e hoje **contradizem esse parágrafo**, três sítios do mesmo
  documento: `README.md:308-309` (o parágrafo do `≤30` da rodada de replanejamento),
  `README.md:311-324` (o *"Por quê"* que defende o teto graduado, mais *"Onde o gerente intervém"*,
  premissado em estouro de teto) e `README.md:1032` (a linha da tabela de trade-offs
  *"Teto de turnos graduado por classe, calibrado pela série medida"*).
  **Por que nada apanhou:** o único aceite do passo 11 — *"percorrer o `README` contra o estado da
  árvore"* — é `check-readme.ps1` exit 0, que confere estrutura e contagens e **não discrimina
  órfão semântico**. A execução **não podia** editá-los: o `Não fazer` fecha o censo e a linha de
  risco do plano manda registrar como `AE-<n>`. A entrega está correta dentro do que o card
  autorizou; o defeito é de autoria de censo.
  **Nona ocorrência da família** (`AE-7`, `AE-10`, `AE-13`, `AE-17`, `AE-19`, `AE-20`), e a mais
  cara: **não resta card no plano**, e é o `README` que o dono lê no Marco 3. **Rota:** roteado ao
  consultor por `B1`, e **tem de fechar antes do Marco 3**.
  **Dois achados menores do mesmo laudo, ambos alvo `dossiê`, sem custo de dimensão:**
  **(i)** âncoras do card envelhecidas na **terceira** geração de re-ancoragem — os `Arquivos-alvo`
  diziam `README.md:825-826` enquanto o passo 10 e a árvore em `HEAD` dizem `824/825`, e a
  `Restrição` citava `README.md:1036` quando a segunda medida histórica está em `:1035`. Sem dano:
  a execução resolveu pelo literal, como a contingência 3 prescreve. **(ii)** `review_evidence.py`
  errou duas atribuições no dossiê desta tarefa — não reconheceu `GOVERNANCA.md:78,80` como caminho
  (lista de linhas separada por vírgula) e marcou `GOVERNANCA.md` como alheio quando ele é
  arquivo-alvo; e extraiu `docs/consultant-spec.md` de dentro de um parêntese numa linha de alvo,
  marcando-o `da entrega` quando é trabalho do consultor (provado por mtime). Reconciliado por hunk
  e mtime no passo 3a. **Rota:** `TK-66`/`TK-74`, com `AE-3`, `AE-9` e `AE-21`.
- **AE-24 — a varredura do `README` pelo conceito aposentado: oito sítios de doutrina viva, não
  três, e um deles é do consultor.** Medido em 2026-09-22 em resposta ao `AE-23`; nona ocorrência
  da família do censo por enumeração (`AE-7`, `AE-10`, `AE-13`, `AE-17`, `AE-19`, `AE-20`) e a
  primeira em que o defeito é **doutrina viva contradizendo doutrina viva** no documento de
  entrada, e não ponteiro quebrado ou contagem errada. **(i) Oito sítios**, contra os três do
  laudo: `:121-124` (entrada de glossário `- **Orçamento de turnos**`, gêmea da `- **Tarefa
  atômica**` de `:94` que o passo 3 reescreveu — o censo pegou uma e não a outra); `:209,211`;
  `:308-309`; `:311-322`; `:324-326`; `:941-942`; `:946-947`; `:1032`. Os três últimos e o
  glossário **não estavam** no laudo, e apareceram só porque a varredura foi pelo **conceito** e
  por todos os nomes que o invocam — `teto`, `tetos`, `orçamento`, `turnos`, `ocupação`,
  `tool uses` —, nunca pelos padrões da rodada anterior. **(ii) Erro próprio, declarado:**
  `README.md:209,211` é o **espelho exato** de `GOVERNANCA.md:78,80`, sítio que o consultor
  atribuiu à `PLN-T7` na rodada do `AE-10` tratando **só a residência do hub**, sem conferir a
  gêmea da porta de entrada — contra a régua que ele mesmo fixara no `AE-7` ("censo de cópia
  secundária se levanta por varredura, nunca por `diff` do já enumerado"). Segunda vez na janela em
  que a família tem a digital do consultor, depois do `AE-15`. **(iii) Distinção preservada:** os
  sítios de **outro sentido** ficam — `:286-303` (economia de turnos como disciplina de **custo**,
  que o plano não aposenta), `:704`, `:707`, `:722`, `:727`, `:744` (teto de checkpoint e de
  dossiê) —, e as **duas medidas históricas** `:354` e `:1025` são preservadas por `I-7`: medida
  datada não se falsifica, e a guarda `TR-DU-7` afere **presença** delas junto com a ausência da
  doutrina revogada, porque guarda que só afere ausência autoriza apagar demais. **(iv) Por que o
  passo 11 da `PLN-T7` não apanhou:** seu único aceite é `check-readme.ps1` exit 0, que confere
  estrutura e contagens e **não discrimina órfão semântico** — "percorrer o README contra o estado
  da árvore" é instrução sem aferidor, e instrução sem aferidor não fecha nada. **(v) Rota:** card
  corretivo `PLN-T7a`, somado à `OP-6` porque a operação diz literalmente que o mantenedor leva a
  unidade nova à porta de entrada e que "o orçamento de turnos por classe sai de onde quem chega o
  lia"; censo da §7 com os oito sítios; `Ato de modelo` de lastro para a `tarefas:` da `OP-6`.
  **(vi) Régua que o caso fixa, e que fecha a série da janela:** quando um card **aposenta um
  conceito**, o alvo não é o parágrafo que o instituía — é **todo enunciado que o define, o
  defende, o pressupõe ou o invoca por nome**, em toda residência, e a varredura se faz pelo
  conceito, jamais pelo literal do parágrafo revogado. Doutrina viva envelhece e se corrige; medida
  datada não se falsifica — e o card tem de aferir **as duas direções**. **Rota:** `TK-72`, com o
  `AE-16` e o `AE-17`, os três critérios no mesmo ato.
- **AE-25 — guarda que prende uma ponta de um invariante de duas.** Apurado pelo reviewer da
  `PLN-T7a` em 2026-09-22, laudo `aprovado` 100% `bloqueante=nenhuma`, recomendação `seguir`;
  achado de alvo `dossiê`, sem custo de dimensão. A `TR-DU-7` foi escrita para prender as **duas
  pontas** do `I-7`: ausência da doutrina revogada **e** presença da medida datada que não se
  falsifica. Exercitada por mutação em memória, ela cumpre a primeira em 6/6 — reinserir qualquer
  um dos seis literais obsoletos a derruba — e cumpre a segunda **pela metade**: a asserção é
  `assert "71 turnos e ~189 mil tokens" in t`, que prende **uma** residência, e o `I-7` protege
  **duas** (`README.md:349` e `:1020`). **Apagar apenas uma passa.** Medido: `grep -c` = 2, ambas
  intactas hoje, então não houve dano. O literal foi ditado verbatim pelo passo 9 e o card proibia
  mudar palavra — é defeito de **autoria do dossiê**, não da execução. **Régua que o caso fixa:**
  guarda de invariante com N residências afere **contagem**, não pertinência — `in t` prova que
  sobrou pelo menos uma, nunca que sobraram as N. **Rota:** `TK-72`, com `AE-16`, `AE-17` e
  `AE-24`. **Segundo achado do mesmo laudo, alvo `dossiê`:** âncoras do card divergiam do real na
  **quarta** geração de re-ancoragem do plano (`Por quê` era `311-320`, não `311-322`;
  `Onde o gerente intervém` em `322-325`, não `324-326`). Resolvido pelo literal via contingência 1,
  sem perda nem arrasto de vizinho — a cauda de "Onde o gerente intervém" sobreviveu como o card
  mandava. Mesma causa das três anteriores: âncora de linha contra arquivo que entregas do próprio
  marco deslocam. **Rota:** `TK-72`, família `AE-12`.
- **AE-26 — o loop duplicou nove linhas de telemetria: o gancho grava e o loop apensou de novo.**
  Medido em 2026-09-22 no fechamento do plano, durante a redação do documento de encerramento —
  que apurou pares repetidos ao somar o custo da janela. Defeito de **condução do loop**, não do
  instrumento. O gancho `SubagentStop` grava sozinho a linha de consumo ao fim de cada subagente; a
  norma do `scrum-master` manda **conferir** essa linha contra o bloco `<usage>` da notificação e
  **corrigi-la à mão quando divergir** (`AE-3` do `P-0739` mediu o caso do valor inflado). O loop
  leu a norma como se mandasse **apensar**, e apensou a segunda linha em **nove das dez** tarefas —
  nas duas primeiras (`PLN-T1`, `PLN-T2`) seguiu a norma corretamente, conferindo e corrigindo só a
  duração, e daí em diante não conferiu mais se o gancho já havia gravado.
  **Efeito medido:** 47 linhas brutas no recorte `2026-09-22` das tarefas `PLN-*`/`MARCO*` contra
  **38** distintas. Cada par diferia **exclusivamente na duração**, em frações de segundo —
  `tool_uses` e `tokens_k` idênticos. Logo **nenhuma medida por tarefa estava errada** e **todo
  total de janela publicado antes da limpeza estava inflado**: o número reportado ao dono durante a
  execução (`3.592,4k` no relatório de encerramento da primeira janela, e `5.472,2k` depois) é
  maior que o real. **Reparado no fechamento:** as nove duplicatas removidas, mantendo a linha de
  duração derivada do `<usage>`; `sort | uniq -d` sobre o recorte devolve vazio. Totais verdadeiros
  da execução inteira: **38 registros, 852 tool uses, 4.553,9k tokens** — 3.959,3k em 31 registros
  de Opus e 594,6k em 7 de Sonnet.
  **Régua que o caso fixa:** a linha de telemetria de subagente tem **um** autor por rodada. O loop
  confere se o gancho gravou **antes** de apensar, e só apensa quando ele não gravou — que é o caso
  do subagente retomado por `SendMessage`, em que o gancho não dispara. Apensar sem conferir
  transforma um registro de medida em soma dupla, e o consumo de janela é **medida, nunca
  auto-relato** (`GOVERNANCA.md` §4.2). **Rota:** `TK-72`, junto com as demais emendas de régua
  desta janela — é defeito de procedimento do loop, não de card, mas mora na mesma família: o
  executor da norma leu o que ela não diz.
