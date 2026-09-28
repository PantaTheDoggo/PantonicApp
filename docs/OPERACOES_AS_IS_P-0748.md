# Operações as-is — o que o `P-0748` deixou no lugar

Documento de encerramento do plano `docs/plans/P-0748-tela-do-gerente.md`, redigido em
2026-09-24 na branch `plan/planner-modelo-escopo`, sem commit. Descreve **as operações que existem
hoje**. Todo número abaixo foi re-derivado por comando nesta data; o registro da execução mora no
plano (`## 9. Achados da execução`) e nos dezessete arquivos `docs/RDO/P-0748-TLG-*.md`.

Os exemplos de painel vêm de duas fontes, sempre nomeadas. A primeira é o arquivo de progresso real
desta execução, `.claude/estado/progresso.txt`, com 143 linhas, citado por número de linha. A
segunda são execuções do gancho numa pasta temporária, com os títulos reais do plano, feitas para
este documento pela mesma via dos testes (`main(entrada=..., estado=<pasta temporária>, raiz=<raiz
do repositório>)`); essas execuções não tocam o arquivo real.

---

## O problema

Enquanto um plano roda, o gerente do projeto acompanha a execução pela tela da extensão VS Code do
Claude Code. Antes do plano:

- A tela mostrava cada chamada de ferramenta: resultados de busca, avisos de leitura, saídas de
  comando. Numa janela de execução medida, apareceram no topo **cerca de 90 chamadas feitas dentro
  dos agentes despachados** e **cerca de 35 chamadas do próprio condutor**.
- Nenhum arranjo conhecido tirava essas linhas de lá. Uma sonda de quatro formas de saída, feita
  com o gerente olhando a tela, mediu:

  | forma | mecanismo | aparece no fluxo principal? | o que apareceu na tela |
  |---|---|---|---|
  | (a) | `Grep` feito pelo condutor no topo | sim | uma linha recolhida: `Grep "TLG-T1" (in docs/plans/P-0748-tela-do-gerente.md)` · `14 lines of output` |
  | (b) | 3 `Grep` + 1 `Read` dentro de um agente despachado | sim | as quatro chamadas no topo, cada uma em linha própria, e o relatório do agente de novo, como mensagem própria |
  | (c) | saída de um gancho `PostToolUse` | não | o texto de sonda não aparece |
  | (d) | linha de status do settings global | não | nenhuma linha de status |

  A linha (b) decide: as chamadas internas de um agente despachado sobem ao topo, e o condutor não
  tem como escondê-las. O veredito de viabilidade **dentro da extensão** é **não**.
- Não existia forma combinada de mensagem ao gerente: o condutor escrevia, quando escrevia, frases
  soltas. Não existia arquivo de progresso, e nenhum gancho gravava coisa alguma depois de uma
  ferramenta.

A tela pedida é uma linha em linguagem humana por transição do loop, no molde *"Tarefa X, passo
Y."* → *"Agente executor recebe o passo Y e vai executar Z."* → *"Agente consultor aceitou a
entrega."* → *"Scrum master concluiu a tarefa X e vai pegar a tarefa X2."*, sem saída de comando
entre duas delas.

## A solução, em uma frase

A tela sai da extensão para um painel no terminal que segue um arquivo, e cada linha desse arquivo
é **gerada por um gancho do kit** a partir do ato de ferramenta que marca a transição do loop, com
o título da tarefa no lugar da sigla e sem nenhuma palavra escrita pelo condutor.

## Vocabulário mínimo

| termo | o que é |
|---|---|
| **condutor**, **loop** e **janela** | o condutor é o agente da sessão principal que executa um plano pela skill `.claude/skills/scrum-master/SKILL.md` — o loop. Ele escolhe a tarefa (`backlog.py next`), muda o estado dela (`backlog.py status <ID> <estado>`), despacha os agentes (executor, revisor, consultor, modelador, planejador), coleta a evidência para o revisor (`review_evidence.py`) e fecha a tarefa. Uma janela é uma sessão de condução, do primeiro `next` ao relatório de encerramento |
| **gancho** | comando que o harness do Claude Code roda sozinho em eventos da sessão, declarado em `.claude/settings.json`: `PreToolUse` (antes de uma ferramenta), `PostToolUse` (depois dela), `UserPromptSubmit` (quando chega uma mensagem à sessão principal) e `Stop` (fim de turno). Recebe pela entrada padrão um JSON com o evento, a ferramenta, a entrada e a resposta dela |
| **arquivo de progresso** e **painel** | `.claude/estado/progresso.txt`, uma frase por linha, e o terminal integrado do VS Code que o segue em tempo real |
| **frase** (`M-0`..`M-17`) | cada uma das 24 formas de linha do repertório. O sufixo `b` marca a segunda forma do mesmo evento (`M-10b`). As lacunas entre `<…>` se preenchem pelo evento ou por leitura local do gancho |
| **estado do gancho** | `.claude/estado/progresso-estado.json`: o que o gancho lembra entre dois eventos da mesma sessão — a tarefa corrente e o título dela, se a janela está aberta, a tarefa recém-fechada, os agentes ainda sem volta |
| **hand-back** | a forma em que o relatório de um agente despachado chega ao condutor: a ferramenta `Agent` responde só com um ponteiro (`{"handback": "send", "agentId": "…"}`), e o texto vem depois como mensagem `<agent-message from="<agentId>">` na sessão principal |
| **linha de retorno** | a primeira linha que cada agente devolve, em gramática fixa: `TLG-T3g review`, `TLG-T3g aprovado 100 bloqueante=nenhuma`, `rota=resolve` |
| **laudo**, **card corretivo**, **marco** e **modelo** | laudo: o julgamento do revisor sobre uma entrega (veredito, percentual, recomendação). Card corretivo: card com sufixo de letra, aberto durante a execução para reparar a entrega de um irmão da mesma operação. Modelo: a seção `## 1` do plano, com objetos, operações e estados finais. Marco: o ponto em que o gerente valida o modelo e a entrega |

---

## O arco — os estratos

O modelo do plano tem **cinco operações**, e cada card materializa uma delas. O plano fechou com
**dezessete cards**: cinco de autoria (`TLG-T1` a `TLG-T5`), cinco de duas rodadas de
replanejamento (`TLG-T2a` da primeira; `TLG-T3a`, `TLG-T2b`, `TLG-T3b` e `TLG-T4a` da segunda) e
sete corretivos nascidos de laudo, de leitura do painel ou da redação deste documento (`TLG-T3c`,
`TLG-T3d`, `TLG-T3e`, `TLG-T3f`, `TLG-T5a`, `TLG-T3g` e `TLG-T3h`).

| estrato | operação | pergunta que responde | cards |
|---|---|---|---|
| **A — a medida** | `OP-1` | a tela da extensão pode ser limpa? | `TLG-T1` |
| **B — as frases** | `OP-2` | o que cada linha do painel diz, e em que evento? | `TLG-T2`, `TLG-T2a`, `TLG-T2b` |
| **C — o gerador** | `OP-3` | quem escreve a linha, e como ela fica confiável? | `TLG-T3`, `TLG-T3a`, `TLG-T3b`, `TLG-T3c`, `TLG-T3d`, `TLG-T3e`, `TLG-T3f`, `TLG-T3g`, `TLG-T3h` |
| **D — o loop** | `OP-4` | o que o condutor faz para a linha chegar ao painel? | `TLG-T4`, `TLG-T4a` |
| **E — a porta** | `OP-5` | como o leitor do repositório sabe abrir e ler o painel? | `TLG-T5`, `TLG-T5a` |

Cada estrato depende do anterior. A medida de A tira a tela da extensão e cria a necessidade de um
arquivo. As frases de B são o conteúdo que o gerador de C grava. O loop de D só se liga a um
gerador que existe. A porta de E descreve o painel que C e D deixaram funcionando, e a própria
tarefa de E roda com esse painel aberto, como corpus da validação final.

**Dois regimes do mesmo painel.** O plano atravessou dois regimes. No **regime narrado**
(`TLG-T2`, `TLG-T2a`, `TLG-T3`, `TLG-T4`), o condutor escrevia cada linha no próprio texto,
começando pelo marcador `[gerente] `, e o gancho copiava essa linha do transcript da sessão. No
**regime gerado** (`TLG-T3a`, `TLG-T2b`, `TLG-T3b`, `TLG-T4a` e os corretivos), o gancho monta a
linha a partir do evento, e o condutor escreve nada. O regime narrado foi substituído inteiro; o
que sobrevive dele está dito em cada seção. As linhas 1 a 27 do painel real são do regime narrado;
da linha 28 à 143, do regime gerado.

A fila executada foi `TLG-T1` → `TLG-T2` → `TLG-T3` → `TLG-T2a` → `TLG-T4` → `TLG-T3a` →
`TLG-T2b` → `TLG-T3b` → `TLG-T4a` → `TLG-T5` → `TLG-T3c` → `TLG-T3d` → `TLG-T3e` → `TLG-T3f` →
`TLG-T5a` → `TLG-T3g` → `TLG-T3h`. Nenhum card ficou fora de estrato, e nenhum foi `cancelled`.

---

## O modelo do plano no fechamento

A **versão 3** do modelo é a vigente. A **versão 4** está **pendente** na seção `## 1A` e muda só
o texto da `OP-2`: a versão 3 ainda diz que cada lacuna das frases se preenche *"pelo que o
condutor já tem em mãos"*, quando quem a preenche é o gancho. O comando que mostra a diferença:

```
$ python .claude/tools/modelo.py show --plano docs/plans/P-0748-tela-do-gerente.md --drift
# Drift do modelo — P-0748 — A tela do gerente: o fluxo da execução em linguagem humana
vigente: versão 3 · 2026-09-24   pendente: versão 4 · 2026-09-24

## Fluxo
[~] OP-2 — O redator do loop escreve o repertório fechado de mensagens: uma frase-modelo para cada transição do loop — tarefa e passo, agente despachado e o que vai fazer, veredito recebido, próxima tarefa —, no molde do exemplo do dono, com cada lacuna preenchida só pelo que o condutor já tem em mãos naquele passo. => O redator do loop escreve o repertório fechado de mensagens: uma frase-modelo para cada transição do loop — tarefa e passo, agente despachado e o que vai fazer, veredito recebido, próxima tarefa —, no molde do exemplo do dono, com cada lacuna preenchida pelo campo do evento, pelo que a sessão já guarda ou por uma leitura que a própria função faz no plano e no diário, e nunca pela mão do condutor: nenhuma lacuna pede ao condutor uma chamada nova nem gasto seu.
```

Nenhum objeto, propriedade ou estado final muda entre as duas versões. O instrumento confere a
versão vigente contra os cards:

```
$ python .claude/tools/modelo.py check --plano docs/plans/P-0748-tela-do-gerente.md
modelo: OK — 5 operações, 4 objetos, 9 propriedades, 17 tarefas, versão 3
```

**Estado da validação da versão 4:** o consultor a validou como conforme (decisão `DTG-41`); a
validação do dono está **pendente** (pendência nº 2).

**Estado do aceite do Marco 3:** a **forma** das frases está aceita. A **confiabilidade** — nenhuma
linha que se perde, nenhuma linha que afirma o que não aconteceu, todo desvio já mapeado corrigido
(`DTG-42`, `DTG-47`) — é o veredito que este documento instrui (pendência nº 1). Os corretivos
`TLG-T3c` a `TLG-T3h` e `TLG-T5a` são a resposta a esse critério.

---

## `TLG-T1` — A sonda: a tela da extensão pode ser limpa?

**Contexto que a motivou:** o primeiro desenho do plano supunha que a extensão recolhe o que um
agente despachado faz, e que bastava o condutor parar de chamar ferramentas no topo para a tela
ficar limpa. Nada disso tinha sido visto.

**O que é o artefato:** uma medida, sem código: a tabela `### 2.2 Agregado da sonda de viabilidade`
do plano, com quatro linhas e o veredito. Durante a sonda, um gancho temporário de teste ficou
gravado em `.claude/settings.json` e foi removido ao fim (a busca pelo texto dele no arquivo dá
`0`).

**Como funciona na prática:**

1. **O que dispara:** a tarefa roda no topo da sessão, pelo próprio condutor, com o gerente
   olhando a extensão. Ela nunca se delega, porque o despacho de um agente é uma das formas medidas.
2. **A entrada:** as quatro formas de uma saída chegar à tela — busca do condutor, buscas e leitura
   dentro de um agente, saída de gancho e linha de status.
3. **O processamento:** o gerente anota, forma a forma, se a saída aparece no fluxo principal.
4. **A saída:** a tabela reproduzida em *O problema*, acima, e a regra de veredito escrita no
   próprio plano: *"`sim` se e só se a linha (b) registra 'só a linha do despacho'"*. A linha (b)
   registrou as quatro chamadas no topo, e o veredito saiu **não**. Com ele, a tela sai da extensão
   para um painel à parte, alimentado por arquivo.

**Protege contra:** a escolha de mecanismo de plataforma feita por suposição. A tarefa recebeu
laudo `aprovado 100%` com recomendação `escalar`, porque o veredito `não` pedia decisão de escopo.

---

## `TLG-T2` — O repertório nasce na skill do loop

**Contexto que a motivou:** não havia forma combinada de mensagem ao gerente.

**O que é o artefato:** a seção `## Repertório de mensagens ao gerente` de
`.claude/skills/scrum-master/SKILL.md`, criada por inserção pura, sem mudar linha existente. Na
forma desta tarefa, a seção trazia **15 frases-modelo** que o condutor preenchia e escrevia. A
seção continua existindo; o conteúdo dela é o da `TLG-T2b`.

**Como funciona na prática:** no regime narrado, o condutor escrevia a frase do passo. O painel real
guarda essas linhas, com a tarefa citada pela sigla e o termo *"evidência mecânica"*:

```
progresso.txt:2   Tarefa TLG-T4: vou reunir a evidência mecânica da entrega para a revisão.
progresso.txt:4   Scrum master concluiu a tarefa TLG-T4 e vai pegar a tarefa TLG-T5 — A porta de entrada diz como o dono acompanha a execução no painel.
```

**Protege contra:** frases soltas, cada uma numa forma. Deixou a residência que as tarefas seguintes
reescreveram: a seção da skill onde o condutor lê o que o painel mostra.

---

## `TLG-T2a` — O repertório para de citar um comando que não existe

**Contexto que a motivou:** a primeira rodada de replanejamento retirou o instrumento `loop.py`,
previsto para enxugar as chamadas do condutor no topo (decisão `DTG-26`): com a tela fora da
extensão, essas chamadas deixam de chegar ao gerente. Sete linhas do repertório citavam
`loop.py` nas colunas de momento e de lacunas.

**O que é o artefato:** as colunas *momento* e *lacunas* das linhas `M-0`, `M-1`, `M-2`, `M-3`,
`M-10`, `M-11` e `M-12` da tabela da `TLG-T2`, reescritas sem `loop.py`. A frase de cada linha
ficou idêntica.

**Como funciona na prática:** a busca por `loop.py` na skill do loop dá `0` hoje. A tabela inteira
foi depois substituída pela da `TLG-T2b`, que também não cita o comando.

**Protege contra:** a skill mandando o condutor rodar um comando que não existe.

---

## `TLG-T3` — O gancho e o arquivo de progresso passam a existir

**Contexto que a motivou:** com a tela fora da extensão, as linhas precisavam de um arquivo, e
nenhum gancho gravava coisa alguma depois de uma ferramenta.

**O que é o artefato:** quatro peças. O script `.claude/tools/progresso_hook.py`; o teste
`tests/test_progresso_hook.py`, com 9 testes nesta tarefa; a declaração do gancho em
`.claude/projecoes.json`, alvo `projeto`, materializada em `.claude/settings.json` pelo comando
`python .claude/tools/materializar.py apply --alvo projeto` (o `settings.json` nunca se edita à
mão); e o arquivo `.claude/estado/progresso.txt`, ignorado pelo git pela regra `.claude/estado/*`
(`.gitignore:11`). Nesta versão o gancho lia o transcript da sessão principal e copiava para o
arquivo as linhas de texto do condutor que começavam por `[gerente] `.

O que sobrevive dela no código de hoje: o caminho do script e do arquivo, a declaração no
`projecoes.json`, a **trava** `progresso.lock` — que serializa leitura do estado, gravação da linha
e gravação do estado quando o harness dispara o gancho em processos simultâneos — e a **barreira
`agent_type`**: o payload de um gancho disparado dentro de um agente despachado traz a chave
`agent_type`, e o gancho sai sem ler nem gravar nada. A leitura do transcript, o marcador e o
cursor saíram na `TLG-T3b`.

**Como funciona na prática:** a barreira, exercida hoje numa pasta temporária com um payload de
dentro de um executor que roda `backlog.py status TLG-T3g done`:

```
rc 0 arquivo existe: False
```

O gancho sai `0` e o arquivo de progresso nem é criado.

**Protege contra:** as chamadas internas dos agentes chegando ao painel — as 90 da janela medida —
e duas gravações simultâneas corrompendo o arquivo ou o estado.

---

## `TLG-T4` — O condutor narrava cada passo

**Contexto que a motivou:** o gancho da `TLG-T3` gravava só a linha que o condutor escrevesse com o
marcador, e a skill do loop ainda não mandava escrevê-la.

**O que é o artefato:** um bullet `**Narra:**` por passo do loop, do 2 ao 10, na skill
`scrum-master`, mais um bullet em `## Guardrails` com o marcador, e uma frase da skill
`.claude/skills/passagem-de-bastao/SKILL.md` dizendo que o que chega ao dono chega também pelo
repertório. Os bullets `**Narra:**` saíram na `TLG-T4a` (a busca por `Narra` na skill dá `0`
hoje); a frase da `passagem-de-bastao` existe, na redação da `TLG-T4a`.

**Como funciona na prática:** no regime narrado, a linha chegava ao painel só se o condutor
lembrasse a forma. O painel real abre com as linhas desse regime, todas citando a tarefa e o plano
pela sigla:

```
progresso.txt:1   Agente executor devolveu a tarefa TLG-T4: review — sem pendência.
progresso.txt:5   Scrum master concluiu a tarefa TLG-T4; a próxima, TLG-T5, é o Marco 3 e precisa do dono diante do painel. Encerrando a janela com o relatório.
progresso.txt:6   Abrindo a janela do plano P-0748: vou selecionar a próxima tarefa e conferir o modelo.
```

As linhas escritas durante a `TLG-T3` e a `TLG-T2a` **não chegaram** ao arquivo: foram escritas sem
o marcador, antes de a regra entrar na skill (achado `AE-7`).

**Protege contra:** nada que dure. A tarefa expôs o defeito que o regime gerado remove: a linha do
painel dependia da memória do condutor.

---

## `TLG-T3a` — A captura do que o gancho recebe

**Contexto que a motivou:** para derivar a transição do evento, o gancho precisa saber o que o
payload de cada evento carrega. A forma da resposta da ferramenta `Agent` nunca tinha sido vista.

**O que é o artefato:** a função `capturar(payload, estado)` em `.claude/tools/progresso_hook.py`,
com três constantes, chamada uma vez em `main`, e três testes `TF-CAP` em
`tests/test_progresso_hook.py`. A captura só roda enquanto existe o arquivo-flag
`.claude/estado/progresso-captura.on`; grava uma linha JSON por disparo em
`.claude/estado/progresso-captura.jsonl`, com o evento, a ferramenta, as chaves da entrada, o
comando ou o tipo de agente, o tipo e as chaves da resposta e a resposta cortada em 2.000
caracteres; para de gravar quando o arquivo passa de 1 MB.

**Como funciona na prática:** com o flag ligado numa pasta temporária, o `PostToolUse` de um
despacho de executor grava:

```
{"evento": "PostToolUse", "tool": "Agent", "input_chaves": ["prompt", "subagent_type"], "command": "", "subagent_type": "pantonic-executor", "response_tipo": "dict", "response_chaves": ["agentId", "handback"], "response": "{\"handback\": \"send\", \"agentId\": \"a1\"}"}
```

Foi essa forma que a captura revelou: a resposta de `Agent` é o ponteiro do hand-back, e o texto do
agente chega depois, pelo `UserPromptSubmit`. O corte em 2.000 caracteres impediu ler a forma
inteira pela captura, e a confirmação veio do transcript (achado `AE-8`, decisão `DTG-39`). Hoje o
flag não existe na pasta de estado: a captura está desligada.

**Protege contra:** um gerador escrito sobre a forma suposta do payload. Com a forma suposta, as
frases de volta de agente (`M-4`, `M-7`, `M-9`) nunca sairiam.

---

## `TLG-T2b` — O repertório vira tabela de eventos

**Contexto que a motivou:** a tabela da `TLG-T2` dizia ao condutor que frase escrever. No regime
gerado, a skill precisa dizer que frase o gancho gera, em que evento, e de onde vem cada lacuna.

**O que é o artefato:** a seção `## Repertório de mensagens ao gerente` da skill `scrum-master`,
reescrita: um parágrafo que diz que o condutor não escreve nenhuma linha, e uma tabela de **24
linhas** com as colunas *id*, *evento (gancho · ferramenta · detecção)*, *frase gerada* e *lacunas
← campo do evento ou leitura local*. O repertório tem três residências com papéis distintos: o
dicionário `FRASES` do gancho é a **vigente** (é dele que a linha sai), a tabela da skill é a
**cópia legível** para o condutor, e a `### 4.1` do plano é a **normativa** (a que o gerente
valida).

**Como funciona na prática:** uma linha da tabela, e o que o gancho grava quando o evento dela
acontece:

```
| `M-5` | evidência coletada — `PreToolUse` · `Bash` · `command` contém `review_evidence.py` e `--tarefa <ID>`, e não contém `--atribuir` | `Tarefa "<título>": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.` | …

progresso.txt:128   Tarefa "O painel reconhece o retorno do agente com o `%` ou o colchete a mais": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
```

A frase da evidência diz o que se coleta — os três blocos que `review_evidence.py` produz —, no
lugar do termo *"evidência mecânica"* do regime narrado. Igualdade medida hoje: a coluna *frase
gerada* da skill é igual a `FRASES` em 24 de 24 formas, e igual à `### 4.1` em 24 de 24.

**Protege contra:** a skill descrevendo uma frase diferente da que o painel mostra. A igualdade
código × skill é barrada pelo teste `TF-GER-18`; a igualdade skill × plano é conferida só na
verificação dos cards.

---

## `TLG-T3b` — O gancho gera a linha a partir do evento

**Contexto que a motivou:** no regime narrado, a linha chegava ao painel só se o condutor lembrasse
o marcador, e citava a tarefa pela sigla. As linhas de duas tarefas se perderam assim.

**O que é o artefato:** `.claude/tools/progresso_hook.py` reescrito inteiro, com as funções
`evento` (a tabela de detecção), `de_volta` (a leitura da linha de retorno de um agente),
`localizar_card` (o título), `tarefa_corrente`, `texto_da_resposta` (normaliza a resposta da
ferramenta para texto) e `main` (trava, estado, gravação); o dicionário `FRASES`; o estado do
gancho `.claude/estado/progresso-estado.json`; e o gancho declarado em quatro eventos — hoje
`progresso_hook.py` aparece em `PreToolUse`, `PostToolUse`, `Stop` e `UserPromptSubmit` do
`.claude/settings.json`. O script usa só a biblioteca padrão, não chama ferramenta, nunca imprime e
sai sempre `0`: qualquer exceção é silenciada, para o gancho jamais alterar o comportamento do
harness.

**Como funciona na prática:**

1. **O que dispara:** cada um dos quatro eventos na sessão principal.
2. **A entrada:** o JSON do evento — nome, ferramenta, entrada e resposta — e o estado do gancho.
3. **O processamento:** a função `evento` casa o ato de ferramenta com a transição do loop:
   - `backlog.py next` depois de rodar → tarefa escolhida (`M-0` na primeira da janela, `M-11` se
     há tarefa recém-fechada, `M-1` sempre) ou fila vazia (`M-12`, `M-12b`);
   - `backlog.py status <ID> <estado>` antes de rodar → `M-2` (`in-progress`), `M-10` (`done`),
     `M-10b` (`blocked`, `cancelled`); `review_evidence.py --tarefa` → `M-5`, ou `M-13` com
     `--atribuir`;
   - `Agent` antes de rodar → agente despachado (`M-3`, `M-6`, `M-8`, `M-14`, `M-15`); a volta vem
     pelo hand-back, no `UserPromptSubmit` `<agent-message from="…">`, ou direto na resposta de
     `Agent`, e `de_volta` a lê → `M-4`, `M-4b`, `M-7`, `M-9`, `M-9b`, ou `M-16` quando a linha de
     retorno sai da gramática;
   - `Stop` → `M-17`, só nas condições da `TLG-T3e`.

   O título vem de `localizar_card`: a primeira linha `### <ID> — <título> [` em
   `docs/plans/P-*.md` e, depois, em `docs/DIARIO_DE_OBRAS.md`; o objetivo, cortado em 240
   caracteres; o título do plano, da primeira linha do arquivo. Toda outra ferramenta e todo outro
   comando não geram linha.
4. **A saída:** a frase anexada ao arquivo de progresso, sob a trava, e o estado regravado.

Um ciclo inteiro, gerado hoje numa pasta temporária — o gancho recebeu, nesta ordem, `next`,
`status in-progress`, despacho e volta do executor por hand-back, `status review` encadeado à coleta
de evidência, despacho e volta do revisor e do consultor, `status done`, `modelo.py show --drift`,
`Stop`, `modelo.py show`, dois `Stop`, uma busca `Grep` e o `next` com a fila vazia:

```
Abrindo a janela do plano "A tela do gerente: o fluxo da execução em linguagem humana".
Tarefa "O painel reconhece o retorno do agente com o `%` ou o colchete a mais". Passo: conferir os gates e preparar o despacho.
Tarefa "O painel reconhece o retorno do agente com o `%` ou o colchete a mais": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
Agente executor recebe a tarefa "O painel reconhece o retorno do agente com o `%` ou o colchete a mais" e vai executar: O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório…
Agente executor devolveu a tarefa "O painel reconhece o retorno do agente com o `%` ou o colchete a mais": review — nenhuma a registrar.
Tarefa "O painel reconhece o retorno do agente com o `%` ou o colchete a mais": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O painel reconhece o retorno do agente com o `%` ou o colchete a mais" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O painel reconhece o retorno do agente com o `%` ou o colchete a mais": aprovado 100%, bloqueante nenhuma.
Agente consultor recebe a tarefa "O painel reconhece o retorno do agente com o `%` ou o colchete a mais" e vai triar.
Agente consultor devolveu a tarefa "O painel reconhece o retorno do agente com o `%` ou o colchete a mais": rota resolve.
Scrum master vai fechar a tarefa "O painel reconhece o retorno do agente com o `%` ou o colchete a mais" como done: registrar estado, RDO e telemetria.
Scrum master mostrou o modelo do plano e aguarda; a resposta dele está na extensão.
Scrum master concluiu a tarefa "O painel reconhece o retorno do agente com o `%` ou o colchete a mais"; nada delegável na fila. Encerrando a janela com o relatório.
```

Dezoito eventos, treze linhas. A volta do executor passou pelo hand-back; a busca `Grep`, o
`show --drift` e os `Stop` sem modelo mostrado não geraram linha. As entradas desse ciclo exercem
também os corretivos, e as seções deles citam as linhas que lhes cabem.

**Protege contra:** linha perdida porque o condutor esqueceu a forma, sigla sem título no painel e
saída de ferramenta no arquivo. Foi a única entrega com laudo `ressalva` (94%): o laudo mapeou três
defeitos da própria entrega (`AE-9`, `AE-10`, `AE-12`), corrigidos na `TLG-T3c`, e um do gerador de
evidência (`AE-11`, pendência nº 3). O primeiro despacho parou na captura cortada (`AE-8`), e o
segundo entregou.

---

## `TLG-T4a` — A skill do loop para de narrar

**Contexto que a motivou:** com o gerador no lugar, os bullets `**Narra:**` mandavam o condutor
escrever uma linha que o gancho já gera — duas fontes para a mesma linha.

**O que é o artefato:** três regiões de conduta. A remoção dos nove bullets `**Narra:**` dos passos
2 a 10 da skill `scrum-master`; o último bullet de `## Guardrails` da mesma skill, reescrito; e uma
frase da `passagem-de-bastao`, reescrita.

**Como funciona na prática:** é regra lida pelo condutor. O bullet de guardrails, hoje:

> O gerente acompanha a execução num painel fora da extensão que mostra
> `.claude/estado/progresso.txt`; cada linha desse arquivo é **gerada** pelo gancho
> `.claude/tools/progresso_hook.py` (eventos `PreToolUse`, `PostToolUse`, `UserPromptSubmit` — a
> volta do agente que entrega em hand-back, `DTG-39` — e `Stop`) a partir do evento da transição
> […]. O condutor **não escreve** linha de repertório, não usa marcador e não escreve no arquivo;
> nenhuma saída de ferramenta chega a ele.

E a `passagem-de-bastao`: *"o que chega ao dono chega pelas linhas do **repertório de mensagens ao
gerente**, que o gancho do kit gera a partir dos eventos do loop e grava no arquivo de progresso, e
pelo **relatório de encerramento** do `scrum-master`, e só por eles."* A menção ao
`UserPromptSubmit` no bullet é da `TLG-T3h`.

**Protege contra:** o condutor gastando turno para escrever uma linha que o gancho gera, e duas
versões da mesma transição no painel.

---

## `TLG-T5` — A porta de entrada diz como abrir e ler o painel

**Contexto que a motivou:** o `README.md` apresentava o loop pelo que ele despacha e roteia, sem
dizer o que o gerente lê enquanto ele roda.

**O que é o artefato:** um trecho do parágrafo **O que é.** da seção `## 6. O loop de execução` do
`README.md`, e um trecho da célula da linha `scrum-master` na tabela de skills (ver `TLG-T5a`).

**Como funciona na prática:** o trecho do `README.md`, hoje:

> […] acompanha a execução num painel fora da extensão do editor, que mostra o arquivo de progresso
> `.claude/estado/progresso.txt` com uma linha em linguagem humana por transição — por exemplo
> `Tarefa "A porta de entrada diz como o dono acompanha a execução no painel". Passo: conferir os
> gates e preparar o despacho.` e `Agente revisor devolveu a tarefa "A porta de entrada diz como o
> dono acompanha a execução no painel": aprovado 100%, bloqueante nenhuma.` —, gerada por um gancho
> do kit (`.claude/tools/progresso_hook.py`) […]. Para abrir o painel, no terminal integrado do VS
> Code, na raiz do repositório: `Get-Content -Path .claude/estado/progresso.txt -Wait -Tail 30
> -Encoding utf8` (o arquivo nasce com a primeira linha gerada).

Os dois exemplos do `README.md` são linhas reais do painel desta tarefa, que rodou pelo loop já
modificado, com o painel aberto:

```
progresso.txt:46   Tarefa "A porta de entrada diz como o dono acompanha a execução no painel". Passo: conferir os gates e preparar o despacho.
progresso.txt:51   Agente revisor devolveu a tarefa "A porta de entrada diz como o dono acompanha a execução no painel": aprovado 100%, bloqueante nenhuma.
```

A guarda estrutural do `README.md` sai limpa: `check-readme: OK - 10 agente(s), 11 skill(s), 20
guardrail(s), […]`.

**Protege contra:** quem chega ao repositório sem saber que o painel existe nem como abri-lo.

---

## `TLG-T3c` — O painel não perde linha e não afirma o que não aconteceu

**Contexto que a motivou:** o painel real das janelas da `TLG-T3b` e da `TLG-T5` mostrou seis
defeitos do gerador:

- o título se perdia: `progresso.txt:28`, `:30` e `:31` dizem `"(tarefa não identificada)"`. O
  gancho buscava a tarefa corrente num arquivo que outro gancho do kit (`telemetria_hook.py`) apaga
  quando o executor termina (achado `AE-9`);
- a linha da coleta de evidência faltou quando o condutor encadeou `backlog.py status … review &&
  review_evidence.py …` num só comando: a regra do `status` casava primeiro e a da evidência nunca
  era avaliada (`AE-16`);
- `progresso.txt:54` termina em ``rota resolve; estratégico: `..`` — o relatório do consultor citava
  `estrategico=` no meio de uma frase de prosa, e o gancho o leu como classificação (`AE-18`);
- `progresso.txt:44` diz `Scrum master encerrou a janela`, e a linha 45 mostra a janela seguindo:
  a frase saía a cada fim de turno do condutor (`AE-17` (i));
- uma resposta com lista de blocos vazia virava JSON cru no painel (`AE-12`);
- a verificação do card rodava o gancho contra a pasta de estado viva e apagava o estado da janela
  em curso (`AE-10`).

**O que é o artefato:** trechos de `.claude/tools/progresso_hook.py` — a regra do `status` e a da
evidência avaliadas de forma independente; o estado aceitando `done;` colado ao separador
(`([a-z-]+)`); `M-2`, `M-5` e o fallback de `tarefa_corrente` gravando tarefa, título e objetivo no
estado do gancho; `rota=` e `estrategico=` contados só no início de linha; a chave `relatorio` no
estado, que limita a frase de fim de turno ao turno que mostrou o modelo; `texto_da_resposta`
devolvendo `""` para lista sem texto. Em `tests/test_progresso_hook.py`: `TF-GER-1` e `TF-GER-9`
estendidos, `TF-GER-12` reescrito, `TF-GER-20` a `TF-GER-24` novos. Na skill, as cópias legíveis
de `M-9`, `M-9b`, `M-10` e `M-17`.

**Como funciona na prática:** no ciclo da `TLG-T3b`, o comando encadeado `backlog.py status
TLG-T3g review && review_evidence.py … --tarefa TLG-T3g …` gera a linha da evidência, e o relatório
do consultor que diz, em prosa, *"Decisão: sem `estrategico=`, o impedimento é tático."* gera a
`M-9` simples:

```
Tarefa "O painel reconhece o retorno do agente com o `%` ou o colchete a mais": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente consultor devolveu a tarefa "O painel reconhece o retorno do agente com o `%` ou o colchete a mais": rota resolve.
```

A `M-9b` sai quando a classificação é real, numa linha própria — `progresso.txt:85`:
`… rota resolve; estratégico: um sinal de "janela encerrada" inferido de eventos compartilhados não
fica confiável, […]`. Os títulos seguem presentes da linha 33 em diante do painel real.

**Protege contra:** linha perdida por comando encadeado, título perdido por arquivo de outro gancho,
classificação estratégica inventada a partir de prosa e JSON cru no painel. Cada caso tem teste:
`TF-GER-20` e `TF-GER-21` (título), `TF-GER-22` (`&&` e `;`), `TF-GER-24` (prosa), `TF-GER-1`
(lista vazia).

---

## `TLG-T3d` — A frase de fim de janela só no relatório de encerramento

**Contexto que a motivou:** depois da `TLG-T3c`, qualquer `modelo.py show` com a janela aberta
armava a frase de encerramento; um `show` pedido no meio da janela, ou o `show --drift` de uma
pausa de marco, fazia o fim de turno seguinte gravar *"Scrum master encerrou a janela"* sem a
janela ter encerrado (`AE-19`).

**O que é o artefato:** três condições em `evento`: só o `modelo.py show` **sem** `--drift` nem
`--pendente` arma a chave `relatorio`; o despacho de agente seguinte e o `backlog.py next` a
desarmam; e, nesta versão, um `Stop` com agente ainda sem volta não gerava a frase. Testes
`TF-GER-25` e `TF-GER-26`, e a cópia legível de `M-17` na skill. A terceira condição saiu na
`TLG-T3e`; as duas primeiras seguem no código.

**Como funciona na prática:** no ciclo da `TLG-T3b`, o `modelo.py show --drift` seguido de `Stop`
não gera linha; o `modelo.py show` sem flag seguido de `Stop` gera uma, e o segundo `Stop` não
repete:

```
Scrum master mostrou o modelo do plano e aguarda; a resposta dele está na extensão.
```

(A frase é a da `TLG-T3e`; nesta tarefa ela ainda dizia *"encerrou a janela"*.)

**Protege contra:** a leitura de modelo no meio da janela lida como encerramento. O laudo
(`aprovado 100%`, recomendação `escalar`) mostrou dois caminhos que as condições não fechavam: um
`show` sem flag no meio da janela, sem agente em voo, ainda gravava o encerramento falso; e um
agente caído sem volta suprimia o encerramento real (`AE-20`). Os dois se fecham na `TLG-T3e`. O
primeiro despacho parou por uma premissa que a triagem julgou improcedente (decisão `DTG-45`), e o
segundo entregou.

---

## `TLG-T3e` — Cada frase diz só o que o gancho vê

**Contexto que a motivou:** três frases afirmavam mais do que o evento prova.

- A `M-17` afirmava uma intenção do condutor — *"encerrou a janela"* — que nenhum evento isola: a
  mesma sequência `show` → `Stop` acontece no encerramento e numa pausa no meio da janela. Cada
  heurística sobre eventos compartilhados fechou um caminho e abriu outro (`AE-17` (i), `AE-19`,
  `AE-20`).
- A `M-8` dizia *"recebe a parada da tarefa"* também quando o consultor era despachado por laudo,
  por instrumento ou no marco, sem parada nenhuma: `progresso.txt:42`, `:53`, `:67`, `:84`
  (`AE-17` (ii)).
- A `M-10` dizia *"registrar estado, RDO e telemetria, e selecionar a próxima"* também para
  `blocked`, que não gera RDO nem próxima (`progresso.txt:74`, seguida de consultor e redespacho da
  mesma tarefa nas linhas 75 a 77), e para `done` seguido de parada sem `next`
  (`progresso.txt:83` → `:86`). A tarefa `blocked` ainda virava *"concluiu"* nas frases seguintes
  (`AE-21`).

**O que é o artefato:** em `FRASES`, três frases trocadas e uma nova:

| id | frase de hoje |
|---|---|
| `M-8` | `Agente consultor recebe a tarefa "<título>" e vai triar.` |
| `M-10` | `Scrum master vai fechar a tarefa "<título>" como done: registrar estado, RDO e telemetria.` |
| `M-10b` | `Scrum master vai marcar a tarefa "<título>" como <estado>, sem RDO.` |
| `M-17` | `Scrum master mostrou o modelo do plano e aguarda; a resposta dele está na extensão.` |

Em `evento`: o `Stop` só tira a chave `relatorio` e deixa a janela aberta; a `M-10b` não grava
tarefa recém-fechada; saem a guarda de agentes sem volta no `Stop` e o esvaziamento dela no
`next`. Testes `TF-GER-27`, `TF-GER-28` e `TF-GER-29` novos, asserções de frase e de estado em
outros sete; as cópias legíveis na skill.

**Como funciona na prática:** a `M-8`, a `M-10` e a `M-17` estão no ciclo da `TLG-T3b`, acima. Uma
tarefa `blocked`, gerada hoje numa pasta temporária — `next` de `TLG-T3d`, `status TLG-T3d
blocked`, `next` de `TLG-T3e`:

```
Abrindo a janela do plano "A tela do gerente: o fluxo da execução em linguagem humana".
Tarefa "O painel só diz que a janela encerrou quando ela encerrou". Passo: conferir os gates e preparar o despacho.
Scrum master vai marcar a tarefa "O painel só diz que a janela encerrou quando ela encerrou" como blocked, sem RDO.
Tarefa "O painel diz só o que o gancho vê: o modelo mostrado e o consultor despachado". Passo: conferir os gates e preparar o despacho.
```

Nenhum *"concluiu"* depois do `blocked`. No painel real, as frases novas aparecem a partir da linha
100.

**Protege contra:** a linha que afirma o que não aconteceu. A regra que ela aplica: **a frase diz o
que o gancho vê — o evento e o campo lido —, e nunca a intenção de quem age.** A varredura das
frases contra o que o loop faz em cada evento achou só a `M-10`, a `M-11` e a `M-12` nessa classe
(decisão `DTG-49`), e as três estão corrigidas.

**O procedimento que ela instalou:** **a frase do painel descreve o evento, e nunca a intenção.** A
`M-17` é o caso-limite: o gancho vê o modelo mostrado e o turno acabado, e só isso a frase diz. A
regra mora na nota da `M-17` da tabela da skill e da `### 4.1`; não tem residência de doutrina.

---

## `TLG-T3f` — O estado do gancho não guarda chave que ninguém lê

**Contexto que a motivou:** depois da `TLG-T3e`, a chave `encerrada` do estado era gravada sempre
`False` e nenhum código do kit a lia; a linha `M-1` da skill a documentava como se tivesse função
(`AE-22`).

**O que é o artefato:** uma instrução a menos na regra do `next` de `evento`, uma asserção nova em
`TF-GER-2` (`"encerrada" not in estado_loop`) e a cópia legível de `M-1` na skill.

**Como funciona na prática:** as chaves do estado ao fim do ciclo da `TLG-T3b`:

```
ESTADO: ['aberta', 'objetivo', 'pendentes', 'sessao', 'tarefa', 'titulo', 'titulo_plano']
```

O arquivo de estado real ainda traz `encerrada`, gravada antes da correção: o gancho regrava as
chaves que encontra enquanto a sessão é a mesma, e reinicia o estado quando o `session_id` muda.
Nenhum código a lê.

**Protege contra:** estado que documenta função que não existe e engana quem lê o gancho.

---

## `TLG-T5a` — A célula da tabela de skills volta a dizer quando a janela encerra

**Contexto que a motivou:** o texto da `TLG-T5` entrou entre *"encerra a janela"* e *"pelo fim do
plano ou pela condição de contexto"*, e esse complemento regia *"lê no painel"*: a célula
da `scrum-master` na tabela de skills do `README.md` saiu com o sentido trocado (`AE-15`).

**O que é o artefato:** a célula da linha `scrum-master` na tabela de skills do `README.md`.

**Como funciona na prática:** a célula, hoje (`README.md:841`):

> Ponto de entrada da execução de backlog — plano nomeado ou "siga o backlog": despacha executor e
> reviewer por tarefa, roteia pelo veredito calculado e encerra a janela pelo fim do plano ou pela
> condição de contexto; a cada transição, um gancho do kit gera a linha em linguagem humana que o
> gerente lê no painel do arquivo de progresso.

A tarefa rodou com o gancho já corrigido pela `TLG-T3c` a `TLG-T3f`, e o painel dela
(`progresso.txt:112` a `:122`) é o corpus final dessa correção. Nele apareceu um defeito novo: a
linha 119 caiu na forma genérica, fechada pela `TLG-T3g`.

**Protege contra:** a porta de entrada dizendo que o gerente lê o painel *"pelo fim do plano"*.

---

## `TLG-T3g` — O painel reconhece o retorno com o `%` ou o colchete a mais

**Contexto que a motivou:** duas linhas do painel real caíram na forma genérica `M-16`, que mostra
a linha de retorno crua, com a sigla:

```
progresso.txt:38    Agente executor devolveu a tarefa "A skill deixa de narrar: a transição chega ao painel pela função": TLG-T4a review [pendencia=- **Ação:** antes=10 depois=10].
progresso.txt:119   Agente revisor devolveu a tarefa "A célula da scrum-master na tabela de skills volta a dizer quando a janela encerra": TLG-T5a aprovado 100% bloqueante=nenhuma.
```

O executor devolveu o campo `pendencia=` entre colchetes, e o revisor devolveu o percentual com
`%`; a gramática dos dois papéis não tem nenhum dos dois caracteres (`AE-14`, `AE-24`).

**O que é o artefato:** os dois padrões de `de_volta` em `.claude/tools/progresso_hook.py`:

```
executor:  ^(\S+) review(?:\s+\[?pendencia=(.*?)\]?)?$
revisor:   ^(\S+) (\S+) (\d+)%? bloqueante=(.*)$
```

Duas asserções novas, em `TF-GER-6` e `TF-GER-7`, e as cópias legíveis de `M-4` e `M-7` na skill.
A gramática que os agentes escrevem fica como está (`.claude/agents/pantonic-reviewer.md:131` e o
passo 4 da skill `scrum-master`).

**Como funciona na prática:** no ciclo da `TLG-T3b`, a volta do executor `TLG-T3g review
[pendencia=nenhuma a registrar]`, seguida de prosa, e a do revisor `TLG-T3g aprovado 100%
bloqueante=nenhuma` geram as frases próprias:

```
Agente executor devolveu a tarefa "O painel reconhece o retorno do agente com o `%` ou o colchete a mais": review — nenhuma a registrar.
Agente revisor devolveu a tarefa "O painel reconhece o retorno do agente com o `%` ou o colchete a mais": aprovado 100%, bloqueante nenhuma.
```

**Protege contra:** os dois desvios medidos de um caractere na linha de retorno. Outro desvio
qualquer cai de novo na `M-16`: a linha continua no painel, com o texto cru.

**O procedimento que ela instalou:** **quem lê tolera, quem escreve segue a forma exata.** O gancho
aceita os desvios medidos; a gramática publicada aos agentes não muda. A regra mora na decisão
`DTG-51` do plano e no código; não tem residência de doutrina.

---

## `TLG-T3h` — Cada `status` do mesmo comando dá a sua linha, e a skill cita o evento da volta em hand-back

**Contexto que a motivou:** dois desvios medidos na redação deste documento. Primeiro: a regra do
gancho que detecta `backlog.py status` casava só o **primeiro** `status` de um comando; o comando
`backlog.py status TLG-T3f done && backlog.py status TLG-T3g in-progress` gerava a linha do `done`
e perdia a do `in-progress` (`AE-25`) — a mesma classe da linha perdida do `AE-16`. Segundo: a
tabela de frases da skill `scrum-master`, a `### 4.1` e o bullet do painel em `## Guardrails`
diziam que a volta de agente vem do `PostToolUse` e não citavam o `UserPromptSubmit`, por onde a
volta em hand-back de fato chega (`AE-26`); a busca por `UserPromptSubmit` na skill dava `0`. O
código estava certo; o texto descrevia menos que ele.

**O que é o artefato:** em `.claude/tools/progresso_hook.py`, a regra do `status` percorre todas
as ocorrências do comando (`re.finditer(r"backlog\.py status (\S+) ([a-z-]+)", cmd)`), com o corpo
inalterado; em `tests/test_progresso_hook.py`, o teste novo `TF-GER-30`. Na skill `scrum-master`,
a coluna *evento* das linhas `M-4`, `M-7`, `M-9` e `M-16` e o bullet do painel em `## Guardrails`
citam o `UserPromptSubmit` (a busca dá `5` hoje). A regra da coleta de evidência segue casando só
o primeiro `--tarefa` do comando: nenhum caso de dois `--tarefa` no mesmo comando foi medido.

**Como funciona na prática:** o comando de dois `status`, gerado hoje numa pasta temporária:

```
Scrum master vai fechar a tarefa "O painel reconhece o retorno do agente com o `%` ou o colchete a mais" como done: registrar estado, RDO e telemetria.
Tarefa "O painel dá uma linha a cada `status` do mesmo comando, e a skill cita o evento da volta em hand-back": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
```

Uma linha por `status`, na ordem do comando. A coluna *evento* da `M-4` na skill, hoje: *"agente
de volta, executor — `PostToolUse` · `Agent` · `pantonic-executor`; se o agente entregou em
hand-back (`handback` = `send` na resposta, e o `PostToolUse` só grava `pendentes[agentId]`),
`UserPromptSubmit` com `prompt` começando por `<agent-mes…`"*. A igualdade da coluna *frase gerada*
segue 24 de 24 entre código, skill e `### 4.1`. A janela desta tarefa no painel real
(`progresso.txt:135` a `:143`) saiu sem defeito.

**Protege contra:** a linha perdida quando o condutor encadeia dois `status`, barrada pelo
`TF-GER-30`; e a cópia legível descrevendo um caminho de volta a menos que o gancho percorre. O
laudo saiu `ressalva 94%`: o `TF-GER-30` entrou entre `TF-CAP-2` e `TF-CAP-3`, partindo o grupo
dos testes de captura, sem efeito funcional (`AE-28`, pendência nº 10).

---

## O que vale além deste plano

| regra | o que resolve | residência |
|---|---|---|
| A linha do painel é gerada pelo gancho a partir do evento; o condutor não escreve linha, não usa marcador e não escreve no arquivo | a linha chega ao painel sem depender da memória nem do gasto do condutor | skill `scrum-master`, último bullet de `## Guardrails` e seção `## Repertório de mensagens ao gerente` |
| O repertório tem três residências: `FRASES` vigente, a skill como cópia legível, a `### 4.1` do plano como normativa | a frase que o condutor lê é a que o painel mostra | `.claude/tools/progresso_hook.py` (`FRASES`); igualdade código × skill barrada por `TF-GER-18` |
| A frase do painel descreve o evento e o campo lido, nunca a intenção de quem age | nenhuma linha afirma o que não aconteceu | notas da `M-8`, `M-10`, `M-10b` e `M-17` na tabela da skill; sem residência de doutrina |
| Quem lê tolera o desvio medido; quem escreve segue a forma exata | um caractere a mais do agente não degrada a linha | padrões de `de_volta`; gramática em `.claude/agents/pantonic-reviewer.md:131` e passo 4 da skill `scrum-master` |
| O gancho falha aberto: nunca imprime, sai sempre `0` | o painel nunca muda o comportamento do harness | docstring de `.claude/tools/progresso_hook.py`; `TF-GER-13` |
| Gancho disparado dentro de agente despachado sai sem ler nem gravar | as chamadas internas dos agentes ficam fora do painel | barreira `agent_type` em `main`; `TF-GER-13` e `TF-CAP-3` |
| O painel é o terminal integrado seguindo o arquivo de progresso | o gerente acompanha em tempo real, fora da extensão | `README.md`, `## 6. O loop de execução`, parágrafo **O que é.** |
| O gancho se declara em `.claude/projecoes.json` e se materializa por `materializar.py apply`; o estado dele vive em `.claude/estado/`, ignorado pelo git | o gancho é artefato do kit, e o painel é fato de uma sessão numa máquina | `.claude/projecoes.json`, alvo `projeto`; `.gitignore:11` |

---

## Os ganhos, medidos

Tudo re-derivado em 2026-09-24.

| medida | antes | depois |
|---|---|---|
| onde o gerente lê a execução | a tela da extensão, com cada chamada de ferramenta — numa janela, ~90 chamadas internas de agentes e ~35 do condutor | o painel do arquivo de progresso: 143 linhas nesta execução, nenhuma saída de ferramenta |
| linhas do painel que nomeiam a tarefa ou o plano pela sigla | 27 de 27 no regime narrado (linhas 1 a 27) | 0 de 116 no regime gerado (linhas 28 a 143): a tarefa sai pelo título entre aspas, ou como `(tarefa não identificada)`; a sigla aparece só dentro do texto cru que um agente devolveu (linhas 38, 73, 119) |
| linhas que o condutor escreve para o painel | todas, com marcador; as de duas tarefas se perderam por falta dele | nenhuma |
| formas de frase | 15, preenchidas pelo condutor | 24, geradas; iguais em código, skill e plano em 24 de 24 |
| linhas do painel real com frase ou forma corrigida depois | — | 3 com título perdido (28, 30, 31), 2 na forma genérica (38, 119), 3 com *"encerrou a janela"* (44, 55, 86), 1 com estratégico lido de prosa (54), 9 com *"e selecionar a próxima"*, 9 com *"recebe a parada"*; todas anteriores ao corretivo da própria classe |
| defeito nas linhas geradas depois da entrega da `TLG-T3e` | — | 1 de 44 (linhas 100 a 143): a linha 119, fechada pela `TLG-T3g` |
| testes do gancho | 9 (depois da `TLG-T3`) | 33 — 30 `TF-GER` e 3 `TF-CAP` |
| suíte de testes | `289 passed` (antes da `TLG-T3a`) | `313 passed` |
| instrumentos de fechamento | — | `modelo.py check` exit `0` (versão 3) · `backlog.py check` OK · `check-readme` OK |
| vereditos de revisão | — | 17 laudos: 15 `aprovado` 100%, 2 `ressalva` 94% (`TLG-T3b`, `TLG-T3h`); 2 com recomendação `escalar` (`TLG-T1`, `TLG-T3d`) |
| paradas de executor | — | 2: `TLG-T3b` (premissa procedente) e `TLG-T3d` (premissa improcedente); as duas redespachadas e entregues |
| acionamentos do consultor | — | 16, uma linha cada em `docs/ACIONAMENTOS_CONSULTOR.tsv` |
| versões do modelo | 1 | 4: a 3 vigente, a 4 pendente |

Nas duas últimas contagens, a frase antiga era verdadeira em parte das linhas — houve parada, houve
próxima —, e falsa nas outras; a correção vale pela parte falsa (seção da `TLG-T3e`).

**Custo da execução, medido.** `docs/telemetria.tsv` registra, para as tarefas `TLG-*`, `P-0748-*`
e `AE-*-consultor-*` de 2026-09-24, **59 linhas**, somando **1.522 tool uses** e **5.446,8k
tokens**, sem linha duplicada (`sort | uniq -d` devolve vazio). Nenhuma linha é de 2026-09-23.

| papel | modelo | linhas | tool uses | tokens |
|---|---|---|---|---|
| executor | Sonnet | 18 | 403 | 1.411,0k |
| revisor | Opus | 17 | 303 | 1.425,5k |
| consultor | Opus | 16 | 574 | 1.569,4k |
| quem escreve o modelo | Opus | 3 | 38 | 188,5k |
| quem escreve o modelo | Fable | 1 | 16 | 80,3k |
| quem planeja | Opus | 1 | 62 | 247,5k |
| quem planeja | Fable | 1 | 49 | 246,4k |
| sonda da `TLG-T1` (agente da forma (b)) | Opus | 1 | 5 | 15,1k |
| redação deste documento (`P-0748-encerramento-redacao`) | Opus | 1 | 72 | 263,1k |

O executor tem 18 linhas para 16 tarefas despachadas: a `TLG-T1` roda no topo, sem executor, e a
`TLG-T3b` e a `TLG-T3d` foram despachadas duas vezes. O condutor da sessão não tem linha: o consumo
dele é o do contexto principal, fora da telemetria por tarefa.

---

## O padrão que a execução revelou

Quinze laudos fecharam em 100% e dois em 94%. Os sete corretivos repararam defeitos que o card não
previa, e todos vieram de ler o painel real, de exercitar o gancho fora do caminho feliz ou de
confrontar a skill com o código. Os defeitos formam duas classes.

**A classe maior: a linha dependia de o agente escrever a forma exata.** No regime narrado, a linha
existia só se o condutor escrevesse o marcador (`AE-7`). No regime gerado, a mesma dependência
sobreviveu em escala menor, em cada ponto onde o gancho lê texto de agente ou de comando: o
colchete do executor e o `%` do revisor (`AE-14`, `AE-24`), a palavra `estrategico=` em prosa
(`AE-18`), o comando encadeado (`AE-16`, `AE-25`). O regime gerado removeu a dependência onde o gancho lê
**evento** — ferramenta, comando, tipo de agente —, e ela restou onde o gancho lê **texto livre**.

**A segunda classe: a frase afirmava uma intenção inferida de eventos compartilhados.** *"Encerrou
a janela"*, *"recebe a parada"*, *"e selecionar a próxima"*, *"concluiu"* — cada uma dizia algo que
o condutor pretendia, e o gancho só via um evento que também serve a outras leituras. Três rodadas
sobre a `M-17` mostraram que nenhuma heurística sobre esses eventos separa o encerramento da pausa.
O que fechou a classe foi mudar o conteúdo da frase para o que o evento prova.

Um terceiro grupo são casos isolados: estado que depende de arquivo de outro gancho (`AE-9`), chave
de estado sem leitor (`AE-22`), JSON cru (`AE-12`), verificação que destrói o estado vivo
(`AE-10`), texto de card que troca o sentido de uma frase do `README.md` (`AE-15`), cópia legível
que descreve um caminho a menos que o código (`AE-26`), cabeçalho do plano que envelhece a cada
fechamento (`AE-27`) e teste fora do grupo dele (`AE-28`).

### Os defeitos da execução, com estado

| # | o que se descobriu | casos | estado | o que fecha |
|---|---|---|---|---|
| 1 | A linha chegava ao painel só se o condutor escrevesse o marcador | `AE-7`; linhas de duas tarefas perdidas | 🟢 **Fechado com guarda** — o gancho gera a linha do evento e não lê texto do condutor; 29 testes `TF-GER` fixam evento → linha | — |
| 2 | Frase afirmando intenção inferida de eventos compartilhados | `M-17` (`AE-17` (i), `AE-19`, `AE-20`), `M-8` (`AE-17` (ii)), `M-10`/`M-11`/`M-12` (`AE-21`) | 🟢 para os cinco casos — `TF-GER-23`, `TF-GER-25` a `TF-GER-29` barram a volta · 🟡 para a classe — a varredura das 23 frases foi leitura única; nenhum teste recusa uma frase nova que afirme intenção | a regra mora nas notas da tabela da skill; nenhuma pendência aberta |
| 3 | Linha de retorno com um caractere fora da gramática cai na forma genérica | `AE-14` (colchete), `AE-24` (`%`) | 🟡 **Caso fechado, classe sem guarda** — os dois desvios medidos têm teste; outro desvio cai na `M-16`, com a linha preservada e crua | nenhuma rota; a `M-16` mantém a informação no painel |
| 4 | Detecção que para na primeira ocorrência perde a linha seguinte do mesmo comando | `AE-16` (`status` + evidência), `AE-25` (dois `status`) | 🟢 **Fechado com guarda** para os dois casos — `TF-GER-22`, `TF-GER-30` · 🟡 para a classe — a regra da evidência segue casando só o primeiro `--tarefa` do comando, sem caso medido | nenhuma rota |
| 5 | Classificação lida de prosa | `AE-18` | 🟢 **Fechado com guarda** — `rota=` e `estrategico=` só no início de linha; `TF-GER-24` | — |
| 6 | Estado do gancho dependente de arquivo que outro gancho apaga | `AE-9` | 🟢 **Fechado com guarda** — tarefa e título gravados no estado do próprio gancho; `TF-GER-20`, `TF-GER-21` | — |
| 7 | Chave de estado sem leitor, documentada como se tivesse função | `AE-22` | 🟢 **Fechado com guarda** — `TF-GER-2` recusa a chave | — |
| 8 | Resposta sem texto virando JSON cru | `AE-12` | 🟢 **Fechado com guarda** — `TF-GER-1` | — |
| 9 | Verificação de card rodando o gancho contra o estado vivo | `AE-10` | 🟡 **Caso fechado, classe sem guarda** — os cards corretivos usam pasta temporária; nada impede um card futuro de apontar para `.claude/estado/` | nenhuma rota |
| 10 | Texto literal de card que desloca um complemento e troca o sentido da frase | `AE-15` | 🟡 **Caso fechado, classe sem guarda** — `check-readme` confere estrutura, não sentido | nenhuma rota |
| 11 | Valor de aceite da verificação viajando no campo `pendencia=` da linha de retorno, o que dispara escalada espúria | `AE-13` | 🔴 **Regra escrita, aplicação pendente** — a regra (valor de aceite não viaja em `pendencia=`) está na decisão `DTG-40` e no achado; a régua de autoria de card não a tem | pendência nº 8 |
| 12 | O gerador de evidência do revisor lista não rastreados anteriores ao despacho e não mostra diff de alvo não rastreado | `AE-4`, `AE-5`, `AE-11`; presente em dez dos dezessete laudos | 🔴 **Regra escrita, aplicação pendente** — remédio conhecido, sem aplicação | pendência nº 3 |
| 13 | Executores devolvem a linha de retorno seguida de prosa, mesmo com a proibição escrita no despacho | `AE-23`, três despachos seguidos | 🔴 **Regra escrita, aplicação pendente** — o painel não é afetado, porque o gancho lê só a primeira linha; a disciplina de retorno não está tipificada | pendência nº 4 |
| 14 | A cópia legível do repertório descreve um caminho de volta a menos que o gancho percorre | `AE-26` (`UserPromptSubmit` ausente da skill e da `### 4.1`) | 🟡 **Caso fechado, classe sem guarda** — as cinco linhas citam o evento; o `TF-GER-18` confere só a coluna *frase gerada*, e a coluna *evento* pode divergir do código sem teste que acuse | nenhuma rota |
| 15 | O cabeçalho do plano envelhece a cada fechamento de tarefa | `AE-27` | 🟡 **Caso fechado, classe sem guarda** — reescrito à mão; o `backlog.py status` troca só o estado entre crases, e o cabeçalho de hoje já diz *"próxima `TLG-T3h`"*, com a `TLG-T3h` `done` | pendência nº 9 |
| 16 | Entrega que põe o teste novo fora do grupo dele | `AE-28` | 🔴 **Regra escrita, aplicação pendente** — a posição estava fechada no card; a recolocação é mecânica e ainda não foi feita | pendência nº 10 |

---

## Pendências abertas ao fim do plano

| # | pendência | por que ficou aberta | o que a fecha | bloqueia algo? | estado |
|---|---|---|---|---|---|
| **1** | Aceite de **confiabilidade** do painel no Marco 3 | a forma está aceita; a confiabilidade é o veredito que este documento instrui | ato do dono no marco, lendo este documento e o painel | **sim** — o plano fecha só com ele | aberta |
| **2** | Validação da **versão 4** do modelo (só o texto da `OP-2`) | a validação tem dois degraus; o consultor validou (`DTG-41`), e o segundo degrau é do dono, sem resposta | ato do dono no marco: promover a versão 4 a vigente, ou recusá-la | **sim** — o modelo do plano fecha só com ele | aberta |
| **3** | O gerador de evidência (`review_evidence.py`) lista como *"fora dos alvos e sem atribuição"* arquivos não rastreados anteriores ao despacho e não dá diff de alvo não rastreado; o trecho de diff trunca em 4.000 caracteres (`AE-4`, `AE-5`, `AE-11`) | instrumento fora do objeto do plano | o tíquete acumulador de confiabilidade de instrumento (`TK-55`), com ponteiro para os três achados | não bloqueou entrega; **efeito fora do plano** — encarece toda revisão | aberta; o ponteiro no `TK-55` está indicado pelo consultor e **ainda não foi posto** |
| **4** | Executores devolvem prosa depois da linha de retorno (`AE-23`) | disciplina do papel executor, fora das operações do plano | tíquete no diário | não — o gancho lê só a primeira linha; **efeito fora do plano** | aberta; tíquete indicado pelo consultor, **ainda não aberto** |
| **5** | Propagação do gancho, da skill e do `README.md` aos cinco kits derivados | fora do escopo por decisão (`DTG-8`, `## 7` do plano) | tíquete de sincronização do kit; `.claude/tools/progresso_hook.py` não existe em nenhum dos derivados (conferido hoje) | não bloqueia o plano; **efeito fora do projeto** — os derivados rodam sem painel | aberta; tíquete indicado pelo consultor, **ainda não aberto** |
| **6** | A skill e a `### 4.1` não citavam o `UserPromptSubmit` da volta em hand-back (`AE-26`) | — | `TLG-T3h` | — | **fechada** (🟡, defeito nº 14) |
| **7** | Dois `backlog.py status` no mesmo comando geravam só a linha do primeiro (`AE-25`) | — | `TLG-T3h`, `TF-GER-30` | — | **fechada** (🟢, defeito nº 4) |
| **8** | A régua de autoria de card não proíbe valor de aceite no campo `pendencia=` (`AE-13`), e a doutrina de card de investigação diverge do parser de `rdo.py` no rótulo de pronto (`AE-1`) | as rotas de régua desta execução não chegaram a residência aberta | tíquete de régua de autoria de card | não; **efeito fora do plano** — qualquer card futuro | aberta; tíquete indicado pelo consultor, **ainda não aberto** |
| **9** | O cabeçalho do plano dizia `Status: ready` e *"próxima `TLG-T3a`"* (`AE-27`) | — | cabeçalho reescrito | não | **fechada** para o caso (🟡, defeito nº 15): o cabeçalho de hoje diz *"próxima `TLG-T3h`"*, já `done` |
| **10** | O `TF-GER-30` está entre `TF-CAP-2` e `TF-CAP-3`, partindo o grupo dos testes de captura (`AE-28`) | a recolocação é ato mecânico, sem card | mover as 21 linhas do teste para o fim do arquivo | não — sem efeito funcional; `33 passed` | aberta |

---

## O estado, sem enfeite

O plano entregou **dezessete cards, todos `done`**, contra as cinco operações do seu modelo: cinco
de autoria, cinco de duas rodadas de replanejamento e sete corretivos. Nenhum card foi cancelado,
nenhuma entrega foi reprovada. Quinze laudos fecharam em 100% e dois com ressalva, 94%. Dois
executores pararam e foram redespachados. Os instrumentos saem limpos: `modelo.py check` exit `0`
na versão 3, `backlog.py check` OK, `check-readme` OK, `313 passed` na suíte e `33 passed` nos
testes do gancho.

O que o repositório ganhou de durável: o gerente acompanha a execução num painel fora da extensão,
aberto por um comando no terminal; cada linha do painel é gerada por um gancho do kit a partir do
ato de ferramenta que marca a transição, com o título da tarefa e do plano no lugar da sigla, sem
custo para o condutor e sem nenhuma saída de ferramenta entre duas linhas; cada frase diz só o que
o evento prova; e a skill descreve os quatro eventos que o gancho escuta. Das 44 linhas geradas
depois da entrega da `TLG-T3e`, uma tinha defeito, e ele está corrigido.

Das dez pendências, **três estão fechadas** (nº 6, 7 e 9) e **sete abertas**. Duas **bloqueiam o
veredito**: o aceite de confiabilidade e a validação da versão 4 do modelo, ambas atos do dono.
Quatro **têm efeito fora deste plano**, e as quatro esperam um registro no diário que o consultor
indicou e ainda não foi feito: o ponteiro no `TK-55` para o gerador de evidência, e três tíquetes
novos — a disciplina de retorno do executor, a régua de autoria de card e, **fora do projeto**, a
propagação aos cinco kits derivados, que rodam sem painel. A última é a recolocação de um teste,
sem efeito funcional.

A lição que esta execução deixa: onde o gancho lê evento, a linha é confiável por construção; onde
lê texto livre de agente, a confiabilidade depende de tolerar cada desvio medido, e a classe
continua aberta.
