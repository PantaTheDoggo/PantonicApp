# P-0752 — Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção

**Data:** 2026-09-26 · **Origem:** pedido do dono na sessão de 2026-09-26 (§0) e a amostra de ~210 ocorrências classificadas nela (F-10) · **Status:** `done` · 2026-09-26 · **Prefixo das tarefas no diário:** `FPU-T<n>` · **Prefixo das decisões:** `DFP-<n>` · **Forma:** legado (arquivo único, id de 4 dígitos).
**Ordem de execução:** FPU-T1 → FPU-T3 → FPU-T5 → FPU-T2 → FPU-T5a → FPU-T1a → FPU-T5b → FPU-T4 → FPU-T6 → FPU-T5c → FPU-T4a → FPU-T7 → FPU-T8 → FPU-T9 → FPU-T8a → FPU-T9a → FPU-T10
**Checagem de versão do kit:** modo hub, congelada em `0.0.0`.

**Pronto quando:** os 17 cards estão `done`; o gate do card volta a ser evidência sobre o corpus vivo; o executor devolve medida em arquivo; o dossiê carrega os precedentes sozinho; a telemetria recusa a duplicata; e a tabela de acionamentos mede a causa raiz de cada parada.

## 0. O problema, verbatim

Pedido (dono, 2026-09-26): *"Um dos maiores pontos fraco do trabalho de agentes é o "esquecimento" e a "assunção". A medida que um trabalho progride, ele se lembra do momento atual, ele assume que a informação atual é verdadeira e passa a basear seu próximo passo com base na sua crença ao invés dos fatos reais. Assim, quero que você proponha uma forma de gerar mecanismos que reduzam essa ocorrência, seja por meio de funções programáticas, ou por meio de skills. Inicie por amostrando ocorrências onde o agente assumidamente reconheceu seu erro por esquecimento ou assunção, tente investigar causas básicas por princípio de pareto (focar nas causas que respondem pelas maiores ocorrências dessses erros) e proponha medidas para combater isso."*

Ordem de planejamento (dono, 2026-09-26): *"Transforme agora em plano, para inicio na próxima janela"*.

Proposta aceita pela ordem acima (agente, 2026-09-26; a amostra e a classificação estão em F-10):

- Pareto das causas: *"1. Valor ou ponteiro reutilizado do contexto em vez de medido no instante do uso (~35%). 2. Premissa sobre a árvore afirmada na autoria do card ou no despacho sem sondar (~30%). 3. Auto-relato aceito como medida (~10%). 4. Regra ou precedente já registrado e não aplicado conforme a janela avança (~10%). 5. Semântica de ferramenta suposta (~8%). 6. Contexto presumido compartilhado com o dono (~5%)."*
- Leitura transversal: *"Esquecimento puro é minoria. Dois terços dos casos são o agente reutilizando algo que já esteve no contexto no lugar de uma medida no ponto de uso."* · *"A doutrina já diz 'medido, nunca presumido' dezenas de vezes e isso não bastou. Prosa lida uma vez não sobrevive a uma janela longa."* · *"O kit já achou a direção certa, mas não a fechou: o instrumento existe em card_check.py, mas o gate ficou suspenso."*
- Medidas: *"1. Pré-voo obrigatório do card: religar o card_check como gate de despacho e como passo final da autoria. 2. Âncora por literal, nunca só por número de linha. 3. Número sem comando é crença: todo literal numérico de aceite carrega comando e data, e um hook avisa no ato de gravar. 4. Retorno do executor por arquivo de medida, não por prosa. 5. Toda regra 'conferir antes de X' vira guarda dentro de X: a telemetria deduplica no escritor; o show cola no dossiê os achados roteados ao card. 6. Skill 'fatos frescos': antes de escrever despacho, relatório ou encerramento, o agente tabula cada número com a origem; origem 'memória' é proibida. 7. Lista de armadilhas de ferramenta medidas, num arquivo só. 8. Comunicação: já coberta pela skill mensagem-ao-dono."*
- Métrica: *"Acrescentar uma coluna causa_raiz ao ACIONAMENTOS_CONSULTOR.tsv com o vocabulário fechado das seis classes. O indicador é a taxa de 'blocked premissa' por despacho. Hoje a linha de base é 25 de 40 acionamentos."*

## 1. Modelo conceitual

**Estado do modelo:** versão 2 · 2026-09-26 · autor: modelador · 10 operações · 12 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem | lastro na §0 | tipo |
|---|---|---|---|---|---|---|
| régua executável | o conjunto de conferências que rodam por comando no ponto de uso, em vez de serem lembradas por quem escreve | conferências | Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill. | OP-1 | *"mecanismos que reduzam essa ocorrência, seja por meio de funções programáticas"* | escopo |
| card | a tarefa de plano ou de tíquete, com as premissas, as âncoras e os números que ela afirma sobre a árvore | premissas conferidas, âncoras, números de aceite | Quem implementa faz o instrumento ler a forma que o corpus vivo usa; card vivo não se reescreve para caber no instrumento. | externo | *"ele assume que a informação atual é verdadeira"* | escopo |
| dossiê de despacho | o que o executor recebe: o card e o que quem despacha herda para ele | precedentes | Quem implementa deriva o precedente dos achados do plano, sem depender de quem despacha lembrar. | externo | *"A medida que um trabalho progride, ele se lembra do momento atual"* | escopo |
| retorno do executor | a linha e o artefato que o executor devolve ao loop | evidência de verificação | Quem implementa faz o loop e o revisor lerem o arquivo de medida; prosa não conta como verde. | externo | *"passa a basear seu próximo passo com base na sua crença ao invés dos fatos reais"* | escopo |
| série de telemetria | o arquivo de consumo por tarefa que o gancho e o fechamento escrevem | linhas por rodada | Quem implementa põe a recusa da duplicata no escritor, nunca em quem chama. | externo | *"a telemetria deduplica no escritor"* | escopo |
| mensagem ao dono | relatório de janela, encerramento, handover ou conversa que leva número ao dono | origem dos números | Quem implementa faz a origem de cada número ser declarada antes de enviar; memória não é origem. | externo | *"ou por meio de skills"* · *"o agente tabula cada número com a origem; origem 'memória' é proibida"* | escopo |
| armadilhas de ferramenta | a lista das semânticas de ferramenta que já enganaram um agente, com o caso medido e a forma segura | residência | Quem implementa escreve a lista num arquivo só e faz a doutrina apontar para ele. | OP-8 | *"5. Semântica de ferramenta suposta"* · *"7. Lista de armadilhas de ferramenta medidas, num arquivo só"* | escopo |
| tabela de acionamentos | o registro de cada parada triada pelo consultor | causa raiz por linha | Quem implementa acrescenta a coluna com vocabulário fechado; linha anterior recebe o valor vazio. | externo | *"Acrescentar uma coluna causa_raiz ao ACIONAMENTOS_CONSULTOR.tsv com o vocabulário fechado das seis classes"* | escopo |
| achado de execução | a entrada de achado que um laudo ou uma parada deixa no plano, com a rota | rota | Ninguém altera: o achado nasce do laudo e o dossiê o lê. | externo | *"o show cola no dossiê os achados roteados ao card"* | externo |
| ocorrência de erro por crença | a parada ou o achado em que um valor do contexto substituiu uma medida | parcela dos acionamentos | Ninguém altera: a coluna da tabela de acionamentos é o que a mede. | externo | *"amostrando ocorrências onde o agente assumidamente reconheceu seu erro por esquecimento ou assunção"* · *"Hoje a linha de base é 25 de 40 acionamentos"* | medição |

### 1.2 Fluxo de operações

- **OP-1** — O gate do card passa a ler a forma de Verificação que o corpus vivo usa, a rodar cada comando e a comparar o valor do mundo em que o card está.
  - `precisa de: card` · `altera: card.premissas conferidas, régua executável.conferências` · `tarefas: FPU-T1, FPU-T1a` · `lastro: religar o card_check como gate de despacho e como passo final da autoria`
- **OP-2** — O gate do card roda no ensaio do planejador e no despacho do loop, e card que não fecha não se despacha.
  - `precisa de: régua executável, card` · `altera: card.premissas conferidas` · `tarefas: FPU-T2` · `lastro: Pré-voo obrigatório do card`
- **OP-3** — O gate do card confere, nos arquivos que o card vai tocar e nos passos dele, enquanto o card não está concluído, que cada âncora de arquivo e linha traz o literal citado e que esse literal está contido numa das linhas da faixa ancorada hoje.
  - `precisa de: régua executável, card` · `altera: card.âncoras, régua executável.conferências` · `tarefas: FPU-T3` · `lastro: Âncora por literal, nunca só por número de linha`
- **OP-4** — Um gancho avisa, no ato de gravar plano ou diário, todo número de aceite que chega sem comando.
  - `precisa de: régua executável, card` · `altera: card.números de aceite, régua executável.conferências` · `tarefas: FPU-T4, FPU-T4a` · `lastro: Número sem comando é crença`
- **OP-5** — O executor devolve a verificação como arquivo de medida gerado por comando, e o revisor e o loop leem o arquivo.
  - `precisa de: régua executável, retorno do executor` · `altera: retorno do executor.evidência de verificação, régua executável.conferências` · `tarefas: FPU-T5, FPU-T5a, FPU-T5b, FPU-T5c` · `lastro: Retorno do executor por arquivo de medida, não por prosa`
- **OP-6** — O dossiê de despacho carrega os achados do plano roteados ao card, derivados das entradas de achado e não da memória de quem despacha.
  - `precisa de: régua executável, dossiê de despacho, achado de execução` · `altera: dossiê de despacho.precedentes, régua executável.conferências` · `tarefas: FPU-T6` · `lastro: o show cola no dossiê os achados roteados ao card`
- **OP-7** — O escritor da série de telemetria recusa a segunda linha da mesma rodada, e a conferência sai de quem chama.
  - `precisa de: régua executável, série de telemetria` · `altera: série de telemetria.linhas por rodada, régua executável.conferências` · `tarefas: FPU-T7` · `lastro: a telemetria deduplica no escritor`
- **OP-8** — As armadilhas de ferramenta medidas ganham um arquivo só, apontado pela doutrina e pela régua do card.
  - `precisa de: régua executável` · `altera: armadilhas de ferramenta.residência` · `tarefas: FPU-T8, FPU-T8a` · `lastro: Lista de armadilhas de ferramenta medidas, num arquivo só`
- **OP-9** — A skill de fatos frescos faz toda mensagem ao dono declarar a origem de cada número, e memória deixa de ser origem admitida.
  - `precisa de: régua executável, mensagem ao dono` · `altera: mensagem ao dono.origem dos números` · `tarefas: FPU-T9, FPU-T9a` · `lastro: Skill fatos frescos`
- **OP-10** — A tabela de acionamentos ganha a coluna de causa raiz com o vocabulário fechado de classes, cada uma nomeando o que a pega: a conferência da régua ou, onde a régua não tem, nenhuma conferência e o que a pega fora dela.
  - `precisa de: régua executável, tabela de acionamentos, ocorrência de erro por crença` · `altera: tabela de acionamentos.causa raiz por linha` · `tarefas: FPU-T10` · `lastro: Acrescentar uma coluna causa_raiz`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final | lastro na §0 |
|---|---|---|---|
| régua executável.conferências | uma conferência existe, a do card, e está suspensa; as demais são frases de skill | seis conferências rodam por comando: forma do card, âncora, número gravado, medida do executor, precedente no dossiê, duplicata na telemetria | *"mecanismos que reduzam essa ocorrência, seja por meio de funções programáticas"* |
| card.premissas conferidas | conferência manual por quem despacha; a conferência do card recusa os cards vivos pela forma deles | conferidas por comando no ensaio da autoria e em todo despacho; card que não fecha não se despacha | *"Pré-voo obrigatório do card"* |
| card.âncoras | número de linha sem literal é aceito e envelhece em silêncio | enquanto o card não está concluído, toda âncora nos arquivos que ele vai tocar e nos passos leva o literal, e o gate acusa a âncora sem literal e o literal que não está em nenhuma linha da faixa citada; objetivo, verificação e contratos ficam fora da conferência | *"Âncora por literal, nunca só por número de linha"* |
| card.números de aceite | número gravado sem comando passa em silêncio | número gravado sem comando recebe aviso no ato de gravar | *"Número sem comando é crença"* |
| dossiê de despacho.precedentes | colados por quem despacha, quando lembra | derivados das entradas de achado do plano roteadas ao card | *"o show cola no dossiê os achados roteados ao card"* |
| retorno do executor.evidência de verificação | prosa na linha de retorno | arquivo de medida gerado por comando, lido pelo revisor e pelo loop | *"Retorno do executor por arquivo de medida, não por prosa"* |
| série de telemetria.linhas por rodada | até duas, quando o loop apensa sem conferir o gancho | uma; o escritor recusa a segunda | *"a telemetria deduplica no escritor"* |
| mensagem ao dono.origem dos números | não declarada; total de janela já saiu inflado | declarada por número: rodado neste turno ou copiado de arquivo e linha | *"o agente tabula cada número com a origem; origem 'memória' é proibida"* |
| armadilhas de ferramenta.residência | espalhadas em memória, achados e lições | um arquivo, apontado pela doutrina e pela régua do card | *"Lista de armadilhas de ferramenta medidas, num arquivo só"* |
| tabela de acionamentos.causa raiz por linha | coluna ausente | coluna presente, vocabulário fechado de seis classes, preenchida a cada acionamento | *"Acrescentar uma coluna causa_raiz"* |
| achado de execução.rota | nomeia card ou tíquete | nomeia card ou tíquete | *"o show cola no dossiê os achados roteados ao card"* |
| ocorrência de erro por crença.parcela dos acionamentos | 25 de 40 acionamentos (2026-09-23 a 2026-09-26) | medida a cada plano fechado pela coluna nova, esperada em queda | *"Hoje a linha de base é 25 de 40 acionamentos"* |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 1 | 2026-09-26 | obsoleta | planejador — modelo derivado da proposta aceita pela ordem *"Transforme agora em plano"*, escrito na mesma sessão, sem o ciclo planejador–modelador, como no `P-0750` e no `P-0751`. Caiu pelo aceite da versão 2 no marco de 2026-09-26 (consultor `DFP-23`; dono *"Validar agora"*) |
| 2 | 2026-09-26 | vigente | modelador — ato de conflito sobre o achado de processo de alvo modelo do laudo da FPU-T3, causado pela DFP-16, que emendou a DFP-4 sem ato de modelo: a OP-3 e o estado final de card.âncoras passam ao alcance entregue — só os arquivos-alvo e os passos, só card não concluído, e o literal conferido por estar contido numa linha da faixa citada; emenda da DFP-22 (consultor, acionamento 10) na mesma versão pendente, que é única até o marco: a OP-10 deixa de prometer conferência da régua para as seis classes — cada classe nomeia o que a pega, a conferência da régua ou, onde a régua não tem, nenhuma conferência e o que a pega fora dela; e o estado inicial de régua executável.conferências e de card.premissas conferidas sai sem nome de instrumento e sem remissão a fato |

## 2. Fatos estabelecidos

- **F-1** Referência de 2026-09-26: `python -m pytest -q` → `397 passed`.
- **F-2** `.claude/tools/card_check.py` (299 linhas, 8 testes em `tests/test_card_check.py`, fixture `tests/fixtures/card_check/plano-exemplo.md` com `EX-T1`..`EX-T5`) lê só a forma `### 8.1` da rubrica (comando em bloco cercado logo após `N.`, linha `→`, literal `**Medido antes:**`). Rodado em 2026-09-26 sobre `EBK-T1` do `P-0751` (card `done`, conforme, aceito pelo dono): `FALHOU - 4 item(ns)`, todos `fora da forma da 8.1`. Corpus vivo: o `P-0751` tem 67 itens de Verificação na forma inline (`N. \`comando\` → esperado — antes \`a\`, depois \`b\``) e 0 `Medido antes:`; o diário tem 4 `Medido antes:`; o `P-0740` tem 177. O gate está suspenso desde 2026-09-19 (`docs/RUBRICA_DE_REVISAO.md:328-335`, `AE-33` do `P-0740`: item fantasma — o marcador `N.` casa qualquer `N.` do texto achatado, inclusive dentro de prosa).
- **F-3** `.claude/tools/encerrar.py` (`TK-88a`, em `review` em 2026-09-26) fecha tarefa e plano num comando cada e lê o consumo da série (`consumo_da_serie`, linha 175); apensa à série só quando o chamador traz `--tool-uses/--tokens-k/--duracao-s`. A recusa de duplicata não existe em `telemetria.py`: `append_row` (linha 116) apensa sem olhar o conteúdo.
- **F-4** `backlog.py show` (linha 1008) devolve só o texto do item (`_truncar(alvo.texto, …)`); `next` imprime o mesmo dossiê. Nenhum achado viaja nele. `encerrar.py` tem `achados_do_plano` (linha 208) que lê as entradas `- **\`AE-<n>\`**` da seção de achados; o rótulo de rota nas entradas recentes é `**Rota:**` (`P-0750` §8, cinco ocorrências).
- **F-5** `.claude/skills/scrum-master/SKILL.md` Passo 3 (linhas 57-75) tem três gates (`G-PLANREADY`, gate de delegação, `modelo.py check`); `card_check` não aparece nele, nem em `passagem-de-bastao/SKILL.md`, nem em `pantonic-planner.md` (0 ocorrências nos três). O planejador manda, no item 14 da Fase 4 (linha 409-413), ensaiar os cards em árvore temporária e rodar cada linha de Verificação antes e depois — sem instrumento nomeado.
- **F-6** `.claude/agents/pantonic-executor.md:127` — a última mensagem do executor é só a linha de retorno; nenhum artefato de medida. `pantonic-reviewer.md:34-45` — três entradas de julgamento: dossiê da tarefa, dossiê de evidência de `review_evidence.py` e diff; a evidência nasce em `docs/RDO/evidencia/<plano>-<ID>.md` (plano legado).
- **F-7** `.claude/agents/pantonic-consultant.md:38` — o consultor apensa uma linha por acionamento a `docs/ACIONAMENTOS_CONSULTOR.tsv` com nove campos: `data`, `plano`, `acionamento`, `tarefa`, `gatilho`, `motivo`, `classe_impedimento`, `rota`, `inconclusivo`. A tabela tem 40 linhas de dados em 2026-09-26.
- **F-8** `README.md:851` — *"O kit são dez agentes, doze skills, quatro verificadores executáveis e a declaração de projeções,"*; `.claude/checks/check-readme.ps1` confere a frase e a tabela de skills (caso medido: `AE-6` do `P-0750`, card `blocked` por frase de contagem não trocada).
- **F-9** Os ganchos do projeto vivem em `.claude/projecoes.json` (`alvos.projeto.chaves.hooks`) e são projetados no `settings.json` local por `python .claude/tools/materializar.py apply` (`settings.json` é gitignorado). Os dois `PreToolUse` atuais (`ocupacao.py`, `progresso_hook.py`) usam matcher `.*` e leem o payload em stdin; `progresso_hook.py` é falha aberta (sempre exit 0, nunca imprime).
- **F-10** Amostra de 2026-09-26 (arquivo bruto em `%TEMP%\claude\selfack.txt`, 156 trechos de transcritos de todos os projetos, só falas do assistente; mais 40 linhas da tabela de acionamentos, ~60 lições de RDO e 118 achados `AE-n` dos planos `P-0740`..`P-0751`). Classificação manual: valor reutilizado em vez de medido ~35%; premissa não sondada na autoria ~30%; auto-relato aceito ~10%; regra ou precedente esquecido ~10%; semântica de ferramenta ~8%; contexto presumido com o dono ~5%. Dos 40 acionamentos, 25 são `defeito de autoria do card` ou `blocked premissa`.
- **F-11** Armadilhas de ferramenta medidas na amostra: aspas duplas no PowerShell convertem `\t` em tabulação (`P-0740`, 2026-09-19); `Select-String` é case-insensitive por padrão (`LM-T5a`); `Measure-Object -Line` ignora linha vazia (memória `powershell-contagem-de-linhas`, 2026-08-08); `subprocess.run` sem `shell=True` trata `;` e `|` como texto (`card_check.py:146-165`); `git stash create` não carrega não rastreado (`AE-3` do `P-0750`); `description` de frontmatter com `: ` derruba `yaml.safe_load` (`AE-20` do `P-0747`); escape de markdown (`\*`) e soft-wrap vazando para literal de aceite (`AE-19`, `AE-23` do `P-0740`); console cp1252 estoura `UnicodeEncodeError` ao imprimir `→` (`TK-65b`, e de novo na autoria deste plano, 2026-09-26). Re-medido pela DFP-20: no PowerShell `\t` fica como está em aspas duplas (quem expande é `` `t `` e `$nome`); o `\t` vira tabulação no literal Python de `python -c`; o ponteiro da armadilha do `subprocess.run` derivou para a função `_rodar_comando`.
- **F-12** Nenhum plano em pasta existe no acervo em 2026-09-26 (`docs/plans/*/` vazio); `P-0750` e `P-0751` declararam `Forma: legado`.

## 3. Decisões

| id | decisão | razão |
|---|---|---|
| DFP-1 | Forma legado (arquivo único), como `P-0750` e `P-0751` | F-12; os instrumentos foram exercitados nessa forma |
| DFP-2 | O `card_check` lê duas formas: a `8.1` (já lida) e a forma inline do corpus, `N. \`<comando>\` → <esperado>[ — antes \`<a>\`, depois \`<b>\`]`; o mundo comparado deriva do status do card — `done` compara `depois` (ou o esperado, quando não há par), qualquer outro status compara `antes`; card não `done` cujo item não tem `antes` falha por `sem valor antes` | F-2: 67 itens vivos na forma inline; card vivo não se reescreve para caber no instrumento (contrato do objeto card) |
| DFP-3 | O marcador de item só vale no início de linha do markdown original; para isso o `DossieTarefa` passa a expor as linhas brutas de cada campo (`campos_linhas`), sem mudar `campos` | fecha o item fantasma do `AE-33` do `P-0740` na causa: o achatamento do campo apaga a fronteira de linha |
| DFP-4 | (emendada por DFP-16) Âncora é toda ocorrência `` `<caminho>:<linha>` `` nos campos `Arquivos-alvo`, `Passos` e nos rótulos `Texto atual <n>`; o literal é o texto entre crases logo depois da âncora na mesma linha, ou o primeiro bloco cercado (`~~~~` ou ```` ``` ````) que segue o rótulo; o gate acusa `âncora sem literal` e `literal fora da linha` (comparação com `strip()` da linha citada) | causa 1 da amostra: número de linha que envelhece (`AE-4` do `P-0750`, linha 184 do `P-0743`) |
| DFP-5 | O aviso de crença é gancho `PreToolUse`, matcher `Write|Edit`, só sobre `docs/plans/**` e `docs/DIARIO_DE_OBRAS.md`; avisa por `systemMessage`, nunca bloqueia; falha aberta como `progresso_hook.py` | número gravado é o ponto de uso; bloquear travaria a autoria por falso positivo |
| DFP-6 | A medida do executor é JSON gravado por `card_check.py --gravar <caminho>`, um registro por item (`indice`, `comando`, `exit`, `saida` truncada a 400 chars, `bate`), em `docs/RDO/evidencia/<plano>-<ID>-medida.json` para plano legado; `review_evidence.py` incorpora o arquivo como seção `## Medida do executor` quando ele existe, e escreve `ausente` quando não | causa 3 da amostra: verde afirmado e não medido (`MC-T2` do `P-0741`) |
| DFP-7 | Os achados roteados entram no `show` por parser próprio de `backlog.py` (duplicado de `encerrar.achados_do_plano`, sem import cruzado, padrão de `rdo.py:137`), lendo o rótulo `**Rota:**`; entra a entrada cujo texto de rota cita o id do card como palavra inteira | `encerrar.py` está em `review` (`TK-88a`) e `backlog.py` é o módulo base; import cruzado inverteria a dependência |
| DFP-8 | A recusa de duplicata compara a linha nova só com a última linha da mesma `tarefa` na série; chave `modelo`, `tool_uses`, `tokens_k` iguais → exit 3 e mensagem `linha repetida`; a série nunca é reescrita | `AE-26` do `P-0745`: os nove pares diferiam só na duração |
| DFP-9 | As 40 linhas anteriores da tabela de acionamentos recebem `-` na coluna nova; a linha de base é F-10 | classificar o passado é julgamento, não transcrição, e o executor não julga |
| DFP-10 | Ordem: instrumentos antes da doutrina que os cita (`FPU-T1`, `FPU-T3`, `FPU-T5` antes de `FPU-T2` e `FPU-T5a`) | card de redação que cita flag inexistente nasce com premissa falsa |
| DFP-11 | Os valores `antes` de toda Verificação foram medidos na autoria (2026-09-26) sobre a árvore real; o ensaio em cópia (valores `depois`) não foi rodado — o `depois` é o aceite que o revisor re-mede | declarado, não omitido; é o próprio defeito que o plano combate |
| DFP-12 | (emendada por DFP-21) A skill `fatos-frescos` é a única medida em prosa do plano; onde houver instrumento para o número (`encerrar.py plano` para totais de janela, `telemetria.py` para consumo), a skill manda usá-lo | a mensagem ao dono não tem instrumento; a skill é o mínimo que a cobre |
| DFP-13 | (invólucro revogado por DFP-15) `rdo._parsear_campos` mantém a assinatura de dois valores como invólucro; as linhas brutas saem de `_parsear_campos_com_linhas`, chamada por `extrair_dossie` | `tests/test_rdo.py:1017` e `:1040` chamam `_parsear_campos` direto (`AE-1`); o invólucro cumpre DFP-3 sem tocar teste vivo; prototipado em cópia: `60 passed` em `test_rdo.py`, `397 passed` na suíte |
| DFP-14 | (consultor, acionamento 2; emenda DFP-2) Forma inline é item cujo resto da linha do marcador, depois de `N.`, começa por crase simples (`` `<comando>` ``); `→ <esperado>` e o par ` — antes …, depois …` são opcionais, cada um. Esperado = texto entre `→` e ` — antes` (ou o fim do item). Valor do mundo: não `done` → `antes` (ausente: `sem valor antes`); `done` → `depois`, ou, sem par, o conteúdo da primeira crase do esperado (sem `→`: `sem valor esperado`; esperado sem crase: `esperado sem literal`) | `AE-2`: `EBK-T1` item 3 (`P-0751:151`) tem par sem `→`, e o item 1 tem `→` com prosa (`verde, com os testes acima.`); o card vivo não se reescreve (I-3). Protótipo sobre as linhas brutas do `EBK-T1`: 4 itens inline, item 2 literal `check: OK — nenhuma violação.` (bate com a saída medida), item 4 literal `passed`. Descartado: `→` obrigatório (o item 3 cairia em `fora da forma`, que é o fantasma que o plano fecha) |
| DFP-15 | (consultor, acionamento 3; revoga o invólucro da DFP-13) `rdo._parsear_campos` deixa de existir: o corpo mora só em `_parsear_campos_com_linhas` (três valores), chamada por `extrair_dossie`; `tests/test_rdo.py:1017` e `:1040` passam a `campos, _, _ = rdo._parsear_campos_com_linhas(linhas)`, mesma asserção | `AE-3`: o invólucro só tinha chamador em `tests/`, e o gate bloqueante `dead_code.py` (G-DEADCODE) acusa exatamente isso; exceção no `dead_code` seria allowlist de conveniência. Medido em cópia da árvore do 2º redespacho com o reparo: `dead_code` exit 0; Verificação 1 `73 passed`; Verificação 2 exit 1 com as duas falhas nomeadas; Verificação 3 exit 1 `fora da forma`; suíte `402 passed`; `kit_check` validate e check-drift, `check-readme`, `ratchet_piso` exit 0. Descartado: manter o invólucro (gate vermelho); `_parsear_campos(linhas, com_linhas=False)` com retorno variável pela flag |
| DFP-16 | (consultor, acionamento 4; emenda DFP-4) `conferir_ancoras` varre só as linhas brutas de `campos_linhas["arquivos-alvo"]` e o conteúdo achatado do extra `Passos` (rótulo por `rdo._normalizar_rotulo`); literal é só o span de crases logo depois da âncora, após ` — ` ou `: `, com `\`` desescapado e `strip()`, e confere quando está contido em alguma linha (`strip()`) da faixa; âncora sem literal passa se o mesmo texto de âncora tem literal noutra ocorrência do card; a conferência só roda com mundo `antes`. `Texto atual <n>` e bloco cercado saem da DFP-4 | `AE-4`: `passos` não é canônico em `rdo._CAMPOS_CANONICOS` (`.claude/tools/rdo.py:121-128`) e o extra é achatado, logo `campos_linhas["passos"]` e "bloco cercado depois do rótulo" não existiam; o rótulo do corpus `- **Texto atual 1** (…):` não casa `_CAMPO_RE` e nunca entra no dossiê, e nenhuma linha `Texto atual` do acervo tem âncora `caminho:linha` (grep: 0); o corpus escapa crase dentro do literal (`\``). Protótipo em cópia: `test_card_check.py` `16 passed`, V2 exit 1 `âncora sem literal`, suíte `406 passed`, `dead_code`/`ratchet_piso`/`kit_check` validate/`check-readme` exit 0; sobre `FPU-T5`..`FPU-T10` achou `pantonic-planner.md:409` velho (hoje 411), `rdo.py:137` e `pantonic-planner.md:447-448` sem literal — reparados. Descartado: estender `rdo.py` (fora dos alvos, muda o módulo base por um único leitor); ler o plano cru no `card_check` (duplica a localização do bloco) |
| DFP-17 | (consultor, acionamento 5; emenda DFP-6) `verificar_tarefa` devolve `(ok, falhas, medida)`, e `medida` é o JSON do `--gravar` menos `gerado_em` (plano, tarefa, mundo já resolvido, itens), com um registro por item de `_parsear_itens`: `exit`/`saida`/`bate` só quando o comando roda; `--gravar` grava ok ou não, sem mudar exit nem saída. O JSON mora em `<dir da evidência>/<plano>-<ID>-medida.json`: o dir é o pai do `--out` resolvido pelo `main` de `review_evidence` (o bloco de destino de plano em pasta sobe para antes de `montar_documento`), ou `<root>/docs/RDO/evidencia` em plano legado sem `--out`; `<plano>` = `_caminhos.id_do_plano(...) or stem`. A seção entra logo antes de `## Guardas`, por kwargs `dir_evidencia` (`montar_documento`) e `linhas_medida` (`_renderizar`) | `AE-5`: o JSON exige `mundo`, que só `verificar_tarefa` resolve (`card_check.py:344`), e a tupla de três do Passo 1 não o levava; `montar_documento` não conhece o `--out`; "depois da seção de diff" tinha dois candidatos; V3 usava `%TEMP%\` (sem expansão em PowerShell, Bash e no `shlex` do `card_check`) e V2/V4 não tinham par legível. Protótipo em cópia: V1 `71 passed`, V3 exit 0, V4 `True`, suíte `409 passed`, `dead_code`/`ratchet_piso`/`kit_check` validate/`check-readme` exit 0; `card_check` sobre o card reparado exit 0 em `antes` (árvore) e em `depois` (cópia). Descartado: `main` repetir a extração do dossiê (duplica `rdo.extrair_dossie`); registros como terceiro elemento sem o mundo |
| DFP-18 | (consultor, acionamento 6; triagem do `AE-39` e dos achados abertos) O gate de despacho é satisfeito reparando a forma da Verificação dos cards vivos **deste** plano, sem estender o regex do par: toda linha de Verificação de card não `done` do `P-0752` leva ` — antes \`<a>\`, depois \`<b>\``, com `exit N` **dentro** da crase (`antes \`exit 0\``); contagem "`N` ou mais" vira comando que imprime booleano (`>=N` → `True`/`False`); a suíte inteira compara `exit 0`, não `N passed` (a contagem muda a cada card da fila). `AE-34` → card corretivo `FPU-T1a` (`OP-1`); `AE-37` → `FPU-T5b` (`OP-5`); `AE-38`, `AE-40`, `AE-41` → tíquete `TK-89` no diário (`TK-89a` e `TK-89b`); `AE-35` → já coberto pelo `TK-84`; `AE-36` segue no marco | Medido sobre todo card não `done` de `docs/plans/` (17 cards, 29 itens): só os 7 do `P-0752` saem com `sem valor antes` (20 itens); nenhum card de outro plano usa as formas `antes:`, `antes exit \`0\`` ou `antes` sem `depois`, então estender o regex serviria só a cards que o próprio plano escreveu fora da `DFP-14` — e o `antes` sem `depois` deixaria o mundo `depois` sem valor. Com o reparo, os 9 cards restantes saem `card_check` exit 0 em `antes` na árvore. Descartado: estender `_ANTES_DEPOIS_RE` (sem caso no corpus; código fora de card nenhum); contagem fixa da suíte (`397 passed` já era `409`) |
| DFP-19 | (consultor, acionamento 7; emenda DFP-7; `FPU-T6` recusado no item 3 do gate de delegação, e triagem de `AE-42`..`AE-44`) `achados_roteados` recebe o texto do plano (`Plano.texto`), não o caminho, e lê as duas formas de entrada do §8 com a mesma leitura de `encerrar.achados_do_plano` (entrada = `- ` na coluna 0 + continuação; id `\bAE-(\d+)\b` na primeira linha; rota = depois do primeiro `**Rota:**`); o bloco sai em `show` (tarefa de plano) e em `renderizar_next` (pai plano), fora do teto DB-7; os testes montam a seção numa cópia da `verde`, que fica intocada em disco. `AE-42` → card corretivo `FPU-T5c` (`OP-5`); `AE-44` → card corretivo `FPU-T4a` (`OP-4`); `AE-43` → emenda da I-1, sem card | O contrato antigo só lia a forma com crase (`AE-1`..`AE-5`, as do consultor), mas a maioria das entradas vem do `encerrar.py` sem crase (`AE-34`..`AE-44`); `show` e `renderizar_next` não têm `repo` e `Item.arquivo` é relativo; a `verde` não tem tarefa `ready` e serve a 20 testes (vencedor do `next` = `TK-1a`); `## Achados da execução` não é fronteira de item, por isso a seção entra no texto do último card. Protótipo em cópia (apagada): `test_backlog.py` `112 passed` (três TF falham no código de hoje, o TR passa), `crenca_hook` `2` contra `4`, suíte `420 passed`, `dead_code`/`ratchet_piso`/`kit_check` validate/`check-readme` exit 0, `backlog.py check` OK. `AE-43`: nenhum card vivo do plano projeta gancho, e o teste de apply real é deliberado (o nome o diz). Descartado: `plano_path` com `repo` passado a `show`; seção na `verde` em disco; tíquete para o teste de apply real |
| DFP-20 | (consultor, acionamento 8; `FPU-T8` `blocked` premissa, 1ª parada) A coluna `forma segura` da tabela da `FPU-T8` vem no Passo 1 do card, uma por armadilha, cada uma medida; a armadilha 1 entra com o texto re-medido (F-11 emendado), o ponteiro da 4 vira `_rodar_comando`; a entrada no `docs/DOC_MAP.md` deixa de ser condicional (bloco na forma do `## docs/ACIONAMENTOS_CONSULTOR.tsv`, Passo 4); o fim do bullet de `GOVERNANCA.md` é ancorado; Verificações 5 e 6 novas | O modelo (`## 1`, objeto *armadilhas de ferramenta*) já exigia a forma segura, e F-11 não a trazia: defeito de autoria do card, não do modelo. Medido em 2026-09-26: pwsh `a`, crase-t, `b` mede 3 caracteres em aspas duplas e 4 em simples, `"a\tb".Length` 4, `python -c` `len('a\tb')` 3 e `len(r'a\tb')` 4; `Select-String -SimpleMatch` 1 sem e 0 com `-CaseSensitive`; `Measure-Object -Line` 2 contra `(Get-Content f).Count` 4; `subprocess.run` passa `'\|'` e `';'` como argv; `git stash create` vazio com não rastreado e `git ls-files --others --exclude-standard` o lista; `yaml.safe_load` recusa `description: a: b` e aceita ` - ` e aspas; `frontmatter_yaml.py` exit 1 no recusado e 0 no aceito; `\*enfase\*` conta 0 e `*enfase*` 1, frase através da quebra 0; `print('→')` em pipe cp1252 estoura e `-X utf8`/`reconfigure` emitem `e2 86 92`. Protótipo do card em cópia (apagada): `card_check --mundo depois` exit 0, tabela 10 linhas de 4 colunas, `kit_check` exit 0, `check-readme` exit 0, `check-drift` só com o artefato de caminho da cópia (árvore exit 0). Descartado: deixar o executor autorar as formas; transcrever a armadilha 1 de F-11 como estava |
| DFP-21 | (consultor, acionamento 9; emenda DFP-12; triagem de `AE-45`..`AE-48`) Onde houver instrumento de **leitura** para o número, a skill `fatos-frescos` manda usá-lo: tarefas fechadas na projeção `(<status>, <fechadas>/<total>)` do índice de `docs/DIARIO_DE_OBRAS.md`, que `backlog.py status` reescreve; consumo na série `docs/telemetria.tsv` (linha citada, ou soma por `python -c` rodado no turno). Instrumento que escreve (`encerrar.py plano`, `telemetria.py append`) não é origem. A skill é a medida em prosa da DFP-12, fora da régua executável: o estado final de `régua executável.conferências` lista seis conferências e a skill não é uma delas, e o item do checklist da `mensagem-ao-dono` §1 é o ponto de uso da skill, não conferência nova — defeito do card, sem drift do modelo. `AE-47` e `AE-48` → card corretivo `FPU-T9a` (`OP-9`); `AE-46` → card corretivo `FPU-T8a` (`OP-8`); `AE-45` → sem card | `AE-47`: `encerrar.py plano` fecha o plano (exige `--veredito`, recusa plano com tarefa aberta) e `telemetria.py` só registra o subcomando `append`; o exemplo da skill citava `docs/telemetria.tsv:212`, que é a linha do `TK-51`. `AE-46`: a `§8` da rubrica se nomeia "régua de **autoria** do card" e não apontava o arquivo. `AE-45`: crase cosmética, sentido intacto; nenhum card vivo toca `pantonic-executor.md:127`, e um despacho por uma crase custa mais que o defeito. Descartado: verbo de leitura novo em `encerrar.py` (I-4) ou em `telemetria.py` (código sem card; a `FPU-T7` é dona do arquivo); recolocar a skill como régua (contradiz o contrato do objeto); ponteiro na tabela de critérios da rubrica (muda critério numerado) |
| DFP-22 | (consultor, acionamento 10; ordem do dono de 2026-09-26, erro inequívoco não se adia) A subseção `### 3.3 Vocabulário de causa raiz` do `FPU-T10` diz, por token, o que o pega, com as seis linhas escritas no Passo 3: `valor-reutilizado`, `premissa-nao-sondada`, `auto-relato` e `regra-esquecida` nomeiam uma conferência da régua (âncora e número gravado, `card_check` no ensaio e no despacho, medida do executor, precedente no dossiê); `semantica-de-ferramenta` e `contexto-presumido` dizem `nenhuma conferência da régua` e nomeiam o que os pega fora dela (a lista de armadilhas; o checklist da `mensagem-ao-dono` com a skill `fatos-frescos`). O enunciado da `OP-10` ("cada classe nomeia a conferência da régua que a pega") promete conferência para as seis: vai ao modelador por dossiê de emenda | o estado final de `régua executável.conferências` lista seis conferências e nenhuma pega ferramenta nem contexto do dono; a lista de armadilhas é residência (`OP-8`) e a skill é medida em prosa (DFP-21); o card antigo listava seis mecanismos sem casá-los aos tokens, e deixava o casamento ao executor, que não julga (DFP-9). Classes por fundamento dos cards: causa 1 → `FPU-T3`/`FPU-T4`, 3 → `FPU-T5`, 4 → `FPU-T6`, 5 → `FPU-T8`. Descartado: chamar de conferência a lista de armadilhas ou o checklist (contradiz o contrato do objeto e a DFP-21); criar conferência nova para as duas classes (operação nova, rota do planejador, sem pedido) |
| DFP-23 | (consultor, acionamento 11, gatilho 4; validação da versão 2 pendente da `## 1`, primeira instância da `GOVERNANCA.md` §3.2) **Conforme.** A `OP-3` e o estado final de `card.âncoras` dizem o alcance que a `FPU-T3` entregou sob a `DFP-16`, medido no código: `conferir_ancoras` lê só `arquivos-alvo` e o extra `Passos`, roda só no mundo `antes` (card não `done`) e aceita o literal contido em qualquer linha da faixa. A `OP-10` diz o que a `DFP-22` fixou: duas das seis classes não têm conferência da régua, e o estado final da régua lista seis conferências, nenhuma para `semantica-de-ferramenta` nem `contexto-presumido`. Os dois estados iniciais sem nome de instrumento não mudam o que se mede. Objetos, contratos, as outras oito operações, os demais estados finais e o `Pronto quando` do plano ficam idênticos à versão 1; `modelo.py show --pendente` exit 0. O `precisa de: régua executável` da `OP-9` (inconclusivo do acionamento 9) não é drift e não segura a promoção. Aceita pelo dono no marco, 2026-09-26: *"Validar agora"*. A promoção é do modelador; depois dela, o condutor alinha as cópias do `FPU-T3` (sub-bullet `OP-3` e `Pronto quando`) e do `FPU-T10` (sub-bullet `OP-10`) ao texto da versão 2 (`AE-36`). O arquivo do modelador não descreve o desfecho do marco: `TK-91`. | a norma busca a validação primeiro no consultor; o drift é o alcance que a entrega já tem, e recusá-lo retroagiria a `FPU-T3` `done` a um alcance que a `DFP-16` descartou com razão medida |
| DFP-24 | (consultor, acionamento 12; emenda I-4; `FPU-T7` `blocked` premissa, 1ª parada) A recusa de duplicata mora em `telemetria.checar_repetida(path, row)`, que lê a `row` pelas colunas de `_COLUMNS`; `append_row(path, row)` e `build_row(args)` mantêm a assinatura e `append_row` chama `checar_repetida` antes de escrever — vale para todo escritor da série, inclusive o fechamento. `encerrar.fechar_tarefa` chama a mesma `checar_repetida` na fase de checagem, logo depois do `checar_close`, e traduz a recusa em `EncerramentoError` antes da primeira escrita (padrão do `TK-88d`); é a única edição de `encerrar.py`, com um teste TR em `tests/test_encerrar.py`. A I-4 perdeu a razão (`TK-88a`..`TK-88d` `done`) e fica emendada para essa edição | O objeto `série de telemetria` é o arquivo "que o gancho e o fechamento escrevem", e o estado inicial de `linhas por rodada` é o loop apensando sem conferir o gancho: o fechamento é o escritor que a `OP-7` corrige. Parâmetro opcional que pula a recusa deixaria o fechamento duplicar (a recusa voltaria a depender de quem chama); recusa só em `append_row`, sem a checagem prévia, estouraria em `encerrar.py:503` depois do `done` e do RDO, e perderia os achados. Medido em cópia: `test_telemetria.py` `12 passed`, `test_encerrar.py` `21 passed`, suíte `448 passed` |
| DFP-25 | (consultor, acionamento 13; `FPU-T10` `blocked` premissa, 1ª parada) Os Passos 2 e 3 do `FPU-T10` publicam o texto a transcrever em blocos cercados `~~~~` (RUBRICA §8 critério (xi); a forma inline com barra-crase é o defeito do `AE-49`): a linha 38 do consultor inteira mais seis sub-itens `   - <token> — <o que é>`, com o critério igual à coluna `o que é` da `### 3.3`; a tabela com os tokens entre crases e as células da DFP-22; a frase da medida com ponto final; a linha 92 ganha `; causa raiz pelo vocabulário da §3.3` logo depois de `docs/ACIONAMENTOS_CONSULTOR.tsv` (e não `### 3.3` no fim da linha). A citação à §3.3 no texto do consultor vai na forma "da §3.3 de `GOVERNANCA.md`", que o C-11 não colhe. O Passo 1 declara o terminador CRLF do TSV (medido: 62 de 62 linhas) e manda gravar LF. A Verificação 2 passa a travar as sete linhas; a V6 nova trava a tabela, a frase e a linha 92 | o card deixava a redação ao executor, que não decide (Regra 8): o Passo 2 pedia "a frase com os seis tokens e o critério", sem texto, e a V2 só contava `causa_raiz`; o Passo 3 publicava literal com crase escapada por barra invertida, e a linha 92 dizia "acrescentar" sem ponto de inserção; a citação com o arquivo antes da seção, dentro do plano, reprova o `backlog.py check` (C-11) no mundo `antes`, medido. Protótipo na árvore, revertido byte a byte: `card_check --mundo depois` exit 0 (V1-V6), `kit_check` validate/check-drift, `check-readme` e `ratchet_piso` exit 0, suíte `448 passed`; `card_check --mundo antes` exit 0. Descartado: reaproveitar a coluna `o que o pega` como critério (o critério de classificar é o que o erro é; o que o pega mora na §3.3) |

## 4. Invariantes de execução

- **I-1** (emendada por DFP-19, `AE-43`) Nenhum executor edita à mão `C:\Users\panta\.claude\` nem `.claude/settings.json`. A escrita em `.claude/settings.json` que a suíte faz ao rodar `tests/test_materializar.py::test_tr_drift_projeto_ok_no_repositorio_real_depois_do_apply` (`materializar apply` contra o repositório real) não viola esta invariante; por ela, o gancho da `FPU-T4` já está projetado e vivo, e o passo de projeção do condutor depois do `done` da `FPU-T4` ficou cumprido.
- **I-2** Nenhuma tarefa acrescenta card a este plano; achado com rota de tíquete abre tíquete no diário, já com card.
- **I-3** Nenhuma tarefa reescreve card vivo de outro plano ou do diário para caber no instrumento.
- **I-4** Nenhuma tarefa toca `.claude/tools/encerrar.py` nem `tests/test_encerrar.py` (`TK-88a` em `review`). Emendada pela DFP-24: a `FPU-T7` acrescenta em `encerrar.py` só a chamada a `checar_repetida` na fase de checagem e em `tests/test_encerrar.py` um teste TR.

## 5. Tarefas

### FPU-T1 — O gate do card lê a forma do corpus e deixa de produzir item fantasma [Sonnet · esforço high · classe implementacao]

- **Status:** `done` · 2026-09-26
- **Operação do modelo:** `OP-1`
  - OP-1: O gate do card passa a ler a forma de Verificação que o corpus vivo usa, a rodar cada comando e a comparar o valor do mundo em que o card está.
  - precisa de: card — Quem implementa faz o instrumento ler a forma que o corpus vivo usa; card vivo não se reescreve para caber no instrumento.
- **Objetivo:** `python .claude/tools/card_check.py --plano <plano> --tarefa <ID>` sai `0` sobre card conforme nas duas formas (DFP-2), compara o mundo derivado do status (`done` → `depois`; demais → `antes`), reconhece marcador de item só no início de linha do markdown original (DFP-3) e continua saindo `1` com falha nomeada nos casos da fixture atual.
- **Fundamento:** DFP-2 (emendada por DFP-14), DFP-3, DFP-14, F-2; `docs/RUBRICA_DE_REVISAO.md` `### 8.1`.
- **Arquivos-alvo:**
  - `.claude/tools/card_check.py` — `_ITEM_MARKER_RE` e `_parsear_itens` (linhas 73-135), `_bate_com_medido` (181), `verificar_tarefa` (191-256), `main` (259-296)
  - `.claude/tools/rdo.py` — `DossieTarefa.__init__` (linha 164-178: acrescentar `campos_linhas`) e `extrair_dossie` (263-330: preencher `campos_linhas` a partir de `_parsear_campos_com_linhas`, que substitui `_parsear_campos` e devolve também as linhas brutas por campo, sem mudar o dicionário `campos` — DFP-15)
  - `tests/test_card_check.py`, `tests/test_rdo.py`
  - `tests/fixtures/card_check/plano-corpus.md` (novo)
- **Contratos/classes:** `card_check.verificar_tarefa(plano: Path, tarefa_id: str, root: Path, mundo: str | None = None) -> tuple[bool, list[str]]` — `mundo` em `{"antes", "depois", None}`; `None` deriva do status do card. `ItemVerificacao` ganha `antes: str | None` e `depois: str | None`; `medido_antes` continua sendo o da forma 8.1. `DossieTarefa.campos_linhas: dict[str, list[str]]` — mesmas chaves de `campos`, valor é a lista de linhas brutas do campo.
- **Passos:**
  1. (DFP-13) Mover o corpo de `rdo._parsear_campos` para uma função nova `_parsear_campos_com_linhas(linhas) -> tuple[dict[str, str], list[list[str]], dict[str, list[str]]]`, que acumula também as linhas brutas de cada campo canônico (a linha do rótulo e cada linha indentada anexada a ele); (DFP-15) `_parsear_campos` é apagada — invólucro sem chamador de produção reprova o gate bloqueante `dead_code.py` —, e os dois chamadores diretos `tests/test_rdo.py:1017` e `:1040` passam a `campos, _, _ = rdo._parsear_campos_com_linhas(linhas)`, sem mudar asserção nenhuma. **A árvore já contém a entrega do 2º redespacho** (`rdo.py`, `card_check.py`, `test_rdo.py`, `test_card_check.py`, fixture `plano-corpus.md`, com 73/402 passed): ajustar só isto — apagar a função `_parsear_campos` (`rdo.py:273-277`), trocar as duas linhas de teste, e atualizar as menções em docstring a `_parsear_campos` em `card_check.py:9` e `rdo.py:386` para `_parsear_campos_com_linhas`; o resto da árvore não se refaz. `extrair_dossie` (linha 329) passa a chamar `_parsear_campos_com_linhas`; `DossieTarefa.__init__` ganha `campos_linhas=None` como último parâmetro (o único construtor é `rdo.py:344`). Os 60 testes de `tests/test_rdo.py` continuam verdes, com a troca das duas linhas de chamada como única alteração deles (medido em cópia pelo consultor, acionamento 3: `python .claude/checks/dead_code.py` exit 0 `0 achado(s)`; `73 passed` na Verificação 1; suíte `402 passed`).
  2. Em `card_check._parsear_itens`, receber as linhas brutas do campo `verificacao` em vez do texto achatado; marcador de item é `^\s*(\d+)\.` no início de uma linha bruta (DFP-3). O item vai da linha do marcador até a linha anterior ao próximo marcador (linhas juntadas com espaço). Item cujo resto da linha do marcador, depois de `N.`, abre bloco cercado (```` ``` ````, como `EX-T1`) é forma 8.1 (tratamento atual); item cujo resto começa por crase simples é forma inline (DFP-14: `→` e par opcionais); qualquer outro item (prosa depois de `N.`, como `EX-T4`) segue `item N: fora da forma da 8.1`, com a mensagem atual. Na forma inline: comando = conteúdo da primeira crase, esperado = texto entre `→` e ` — antes` (ou o fim do item), `antes`/`depois` = valores capturados por `antes\s+`?([^`,;]+)`?[,;]?\s*depois\s+`?([^`.\n]+)`?`, quando existirem (o valor pode estar entre crases ou não).
  3. Em `verificar_tarefa`, derivar `mundo` do bullet `- **Status:**` do card quando `mundo is None` (`done` → `depois`; qualquer outro → `antes`). Status: `rdo._status_atual(plano_path, dossie.tarefa_id, dossie, None)` (lê o bullet do plano legado). Forma inline, nesta ordem e uma falha por item, sem as checagens de `→`/`Medido antes` da 8.1: (a) valor do mundo (DFP-14) — card não `done` sem `antes` → `item N: sem valor antes`; card `done` sem par e sem `→` → `item N: sem valor esperado`; card `done` sem par com esperado sem crase → `item N: esperado sem literal`; (b) `_validar_comando` recusa → `item N: comando recusado - <motivo>` (mesma linha da 8.1); (c) rodar e comparar com `_bate_com_medido(valor_do_mundo, returncode, saida)` → `divergencia` como na 8.1. `**Aferição: manual**` num item inline segue a regra da 8.1. Forma 8.1: sem mudança de semântica (compara `Medido antes` em qualquer mundo, como hoje).
  4. Em `main`, acrescentar `--mundo {antes,depois}` opcional.
  5. Fixture nova `tests/fixtures/card_check/plano-corpus.md` com cabeçalho de plano legado mínimo e quatro cards na forma inline: `CX-T1` `ready` com `1. \`python -c "print('a')"\` → \`b\` — antes \`a\`, depois \`b\`` (fecha em `antes`); `CX-T2` `done` com o mesmo item (fecha em `depois` só se o comando imprimir `b` — usar `python -c "print('b')"`); `CX-T3` `ready` com item sem `antes` (falha `sem valor antes`); `CX-T4` `ready` cujo campo `Contingências` contém a prosa `acionamento 1. medido` (nenhum item fantasma: a Verificação dele tem um item só, e o gate reporta um só).
- **Testes (novos, em `tests/test_card_check.py`):** TF `test_tf_corpus_ready_compara_antes` (`CX-T1` → exit 0); TF `test_tf_corpus_done_compara_depois` (`CX-T2` → exit 0; com `--mundo antes` → exit 1 e `divergencia`); TF `test_tf_corpus_sem_antes_falha` (`CX-T3` → exit 1, `sem valor antes`); TF `test_tf_marcador_so_no_inicio_de_linha` (`CX-T4` → exatamente um item reconhecido, exit 0); TR: os 8 testes atuais sobre `plano-exemplo.md` inalterados e verdes; em `tests/test_rdo.py`, os dois testes de `_parsear_campos` (`:1017`, `:1040`) mudam só a linha de chamada (DFP-15). Em `tests/test_rdo.py`: TF `test_tf_campos_linhas_preserva_quebras` (`campos_linhas["verificacao"]` tem tantas linhas quanto o bloco bruto do card da fixture de `rdo`).
- **Verificação:**
  1. `python -m pytest tests/test_card_check.py tests/test_rdo.py -q` → verde, com os cinco testes novos — antes `68 passed`, depois `73 passed`.
  2. `python .claude/tools/card_check.py --plano docs/plans/P-0751-esgotar-backlog.md --tarefa EBK-T1` → exit 1 com exatamente duas falhas, `item 1: esperado sem literal` e `item 3: comando recusado - primeiro token fora da lista fechada ('python', 'pwsh')`, e nenhuma `fora da forma` — antes exit `1` com `4 item(ns)` `fora da forma da 8.1`, depois exit `1` com `2 item(ns)`. Roda a suíte inteira (item 4), cerca de 35 s. Medido pelo consultor (2026-09-26), com os comandos rodados como `_rodar_comando`: item 2 sai `0` com `check: OK — nenhuma violação.` na saída; item 4 sai `0` com `397 passed`; item 3 recusado com esse motivo exato.
  3. `python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-exemplo.md --tarefa EX-T4` → exit 1 com `fora da forma` — antes exit `1`, depois exit `1` (regressão da forma 8.1; a linha não discrimina e é declarada como trava, não como aceite).
  4. `python -m pytest -q` → nenhuma falha; `passed` ≥ 397 + 5 — antes `397 passed`.
- **Pronto quando:** card.premissas conferidas — conferidas por comando sobre card conforme nas duas formas (fixture) e lidas sem `fora da forma` sobre o corpus vivo — Verificações 1 e 2; régua executável.conferências — o `card_check` fecha sobre o corpus vivo e sobre a fixture antiga — Verificações 1 a 3.
- **Não fazer:** não tocar `_validar_comando` nem `_COMANDOS_PERMITIDOS`; não reescrever card nenhum de `docs/plans/` nem do diário (I-3); não tocar `encerrar.py` (I-4); não mudar o dicionário `campos` nem as chaves dele.
- **Contingências:**
  - (fato, DFP-14, não mais contingência) o item 3 do `EBK-T1` (`P-0751:151`) não tem `→` e é inline pelo par; o comando PowerShell nu é recusado, e o item 1 (`→ verde, com os testes acima.`) não tem literal: as duas falhas são o aceite da Verificação 2, não defeito da entrega — não pare por elas nem reescreva o `EBK-T1` (I-3).
  - chamadores de `_parsear_campos` medidos em 2026-09-26 (`grep -rn "_parsear_campos(" --include=*.py .claude tests`): `rdo.py:329`, `tests/test_rdo.py:1017`, `tests/test_rdo.py:1040` — `rdo.py:329` é o `extrair_dossie` e os dois de teste migram no Passo 1 (DFP-15); se o grep listar chamador fora desses → migre-o para `_parsear_campos_com_linhas` desempacotando três valores, sem parar.
  - (fato, DFP-15) `python .claude/checks/dead_code.py` é gate bloqueante da `guardrails-check` e roda no fechamento: símbolo de produção chamado só de `tests/` reprova; não crie invólucro, alias nem exceção no `dead_code.py` — exit 0 com `0 achado(s)` foi medido com o reparo do Passo 1.
  - se o bullet `- **Status:**` não existir no card (plano em pasta) → `mundo` = `antes`, com aviso na saída `status ausente: comparando antes`.
- **Handover:** 2026-09-26 · para `FPU-T3`, `FPU-T5`
  - **Entregue:** card_check le as duas formas de Verificacao: 8.1 (bloco cercado na linha do marcador) e inline (crase apos N., seta e par antes/depois opcionais, DFP-14) - .claude/tools/card_check.py:121 _parsear_itens sobre linhas brutas, :248 verificar_tarefa(plano, tarefa_id, root, mundo=None) deriva o mundo do Status (done->depois), :383 main com --mundo {antes,depois}; rdo._parsear_campos_com_linhas (.claude/tools/rdo.py:212) substitui _parsear_campos e devolve campos_linhas; DossieTarefa(..., campos_linhas=None) em rdo.py:171; fixture tests/fixtures/card_check/plano-corpus.md (CX-T1..CX-T4)
  - **Contrato:** card_check sai 0 sobre card conforme nas duas formas e 1 com falha nomeada por item (sem valor antes, sem valor esperado, esperado sem literal, comando recusado, divergencia, fora da forma da 8.1); marcador de item so no inicio de linha bruta; sobre EBK-T1 do P-0751 sai exit 1 com exatamente item 1 esperado sem literal e item 3 comando recusado; suite 402 passed, test_card_check+test_rdo 73 passed; dead_code 0 achados
  - **Não refazer:** parser inline e derivacao de mundo ja pagos; _parsear_campos nao existe mais (nao recriar invólucro: dead_code reprova)
  - **Pendente:** nenhum teste tranca o fantasma de prosa 'N.' na linha de continuacao do proprio item de Verificacao (o CX-T4 so cobre outro campo) - fixture absorvivel no FPU-T5; regex do par antes/depois nao casa com parentese entre antes e depois (item 1 do FPU-T3)
- **Notas de execução:**
  - 2026-09-26 `ready` — consultor ac.2: DFP-14 (seta e par opcionais na forma inline), Verificacao 2 re-medida
  - 2026-09-26 `ready` — consultor ac.3: DFP-15 (invólucro _parsear_campos apagado, 2 testes migram; dead_code medido exit 0); redespacho sobre a árvore atual, sem consumir retentativa
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T1-o-gate-do-card-le-a-forma-do-corpus-e-deixa-de-produzir-item.md`, veredito aprovado 100%

### FPU-T2 — O gate do card roda no ensaio do planejador e no despacho do loop [Sonnet · esforço medium · classe redacao]

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T1`, `FPU-T3`, `FPU-T5`
- **Operação do modelo:** `OP-2`
  - OP-2: O gate do card roda no ensaio do planejador e no despacho do loop, e card que não fecha não se despacha.
  - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; card — Quem implementa faz o instrumento ler a forma que o corpus vivo usa; card vivo não se reescreve para caber no instrumento.
- **Objetivo:** o `card_check` volta a ser gate obrigatório de despacho (scrum-master Passo 3 e gate de delegação) e passo final da autoria (planejador Fase 4 item 14 e Fase 5); a nota de suspensão da rubrica sai e a `### 8.1` publica as duas formas.
- **Fundamento:** DFP-2, DFP-10, F-5; `docs/RUBRICA_DE_REVISAO.md:326-335`.
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md:65` — `  Terceiro gate, mecânico: \`python .claude/tools/modelo.py check --plano <plano>\``
  - `.claude/skills/passagem-de-bastao/SKILL.md:133` — `Recusa de qualquer item do gate: **não delega**, e o que falta fechar volta ao planejamento.`
  - `.claude/agents/pantonic-planner.md:411` — `14. **Ensaio dos cards em árvore temporária** — antes de gravar, aplique os cards em sequência`
  - `docs/RUBRICA_DE_REVISAO.md:328` — `**Nota (2026-09-19):** o gate está **suspenso em efeito** desde 2026-09-19, por decisão do loop`
  - `.claude/README.md` (projeção regenerada, se o gerador do kit a reescrever)
- **Passos:**
  1. Scrum-master, Passo 3: depois do parágrafo do terceiro gate, inserir o quarto: `python .claude/tools/card_check.py --plano <plano> --tarefa <ID>` — exit `1`: **não delega**, o stderr vai à razão e a tarefa cai em `B3`, com a nota `gate do card`. Trocar `Aprovados os três` por `Aprovados os quatro`.
  2. Passagem-de-bastão, gate de delegação: acrescentar o item 8, `card_check` exit 0 sobre o card, antes da linha `Recusa de qualquer item do gate`.
  3. Planejador, Fase 4 item 14: nomear o instrumento — o ensaio roda `card_check.py --mundo antes` sobre cada card antes de gravar e `--mundo depois` sobre a cópia depois de aplicar o card; valor publicado é o medido. Fase 5: acrescentar `card_check` exit 0 para todo card como condição de registro, ao lado de `modelo.py check`.
  4. Rubrica `### 8.1`: apagar o parágrafo da nota de suspensão (linhas 328-335, dois parágrafos, do `**Nota (2026-09-19):**` até `item a item, por quem despacha.`) e publicar a **forma B** (inline) ao lado da forma A (bloco cercado), com o par `antes`/`depois` e a regra de mundo por status (DFP-2, emendada por DFP-14: `→` e par opcionais, esperado comparado pela primeira crase), e a âncora com literal (DFP-4, emendada por DFP-16).
  5. Regenerar `.claude/README.md` pelo gerador do kit se ele projetar as skills tocadas; rodar `pwsh .claude/checks/check-readme.ps1`.
- **Verificação:**
  1. `python -c "from pathlib import Path;print(Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8').count('card_check'))"` → `2` — antes `0`, depois `2`.
  2. `python -c "from pathlib import Path;print(Path('.claude/skills/passagem-de-bastao/SKILL.md').read_text(encoding='utf-8').count('card_check'))"` → `1` — antes `0`, depois `1`.
  3. `python -c "from pathlib import Path;print(Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8').count('card_check'))"` → `2` — antes `0`, depois `2`.
  4. `python -c "from pathlib import Path;print(Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8').count('suspenso em efeito'))"` → `0` — antes `1`, depois `0`.
  5. `pwsh .claude/checks/check-readme.ps1` → exit 0 — antes exit `0`, depois exit `0` (trava).
- **Pronto quando:** card.premissas conferidas — conferidas por comando no ensaio da autoria e em todo despacho; card que não fecha não se despacha — Verificações 1 a 4.
- **Não fazer:** não tocar o bloco A nem o bloco B do scrum-master; não tocar `GOVERNANCA.md`; não reescrever cards vivos (I-3).
- **Contingências:**
  - se `pantonic-planner.md` tiver frontmatter que `yaml.safe_load` recuse depois da edição → a edição não tocou o frontmatter: parar e sinalizar `blocked` razão `premissa`, colando o erro.
- **Handover:** 2026-09-26 · para `FPU-T5a`, `FPU-T4`
  - **Entregue:** card_check e gate de despacho: .claude/skills/scrum-master/SKILL.md Passo 3 (quarto gate, exit 1 -> B3 com nota 'gate do card'; 'Aprovados os quatro'); .claude/skills/passagem-de-bastao/SKILL.md gate de delegacao item 8; .claude/agents/pantonic-planner.md Fase 4 item 14 (--mundo antes/depois no ensaio) e Fase 5 (card_check exit 0 por card); docs/RUBRICA_DE_REVISAO.md 8.1 sem a nota de suspensao, com Forma A e Forma B (inline)
  - **Contrato:** todo despacho roda card_check --plano <plano> --tarefa <ID>; exit 1 nao delega. Os cards restantes do P-0752 hoje saem exit 1 (FPU-T5a, FPU-T4, FPU-T6) - o reparo passa pelo consultor
  - **Não refazer:** nada a declarar
  - **Pendente:** scrum-master:62 diz 'sete itens' (agora oito) e a linha B3 do bloco B nao cita card_check; rubrica 8.1 diz literal 'comparado por strip() contra a linha citada' mas o instrumento confere contido em alguma linha da faixa
- **Notas de execução:**
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T2-o-gate-do-card-roda-no-ensaio-do-planejador-e-no-despacho-do.md`, veredito ressalva 88%

### FPU-T3 — Toda âncora de arquivo e linha do card leva o literal, e o gate confere a linha hoje [Sonnet · esforço medium · classe implementacao]

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T1`
- **Operação do modelo:** `OP-3`
  - OP-3: O gate do card confere, nos arquivos que o card vai tocar e nos passos dele, enquanto o card não está concluído, que cada âncora de arquivo e linha traz o literal citado e que esse literal está contido numa das linhas da faixa ancorada hoje.
  - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; card — Quem implementa faz o instrumento ler a forma que o corpus vivo usa; card vivo não se reescreve para caber no instrumento.
- **Objetivo:** `card_check.py` acusa `âncora sem literal` para toda ocorrência `` `<caminho>:<linha>` `` sem literal (DFP-4) e `literal fora da linha` quando o literal não está na linha citada da árvore de `--root`; card sem âncora não é afetado.
- **Fundamento:** DFP-4, F-2, causa 1 de F-10.
- **Arquivos-alvo:**
  - `.claude/tools/card_check.py` — nova função `conferir_ancoras(dossie, root) -> list[str]` chamada em `verificar_tarefa` depois dos itens de Verificação
  - `tests/test_card_check.py`
  - `tests/fixtures/card_check/plano-ancoras.md` (novo) e `tests/fixtures/card_check/alvo.txt` (novo, três linhas: `um`, `dois`, `tres`)
- **Contratos/classes:** `conferir_ancoras(dossie: DossieTarefa, root: Path) -> list[str]` (DFP-16, emenda DFP-4) — varre dois textos: as linhas brutas de `dossie.campos_linhas.get("arquivos-alvo", [])` e o conteúdo (achatado) de cada par de `dossie.extras` cujo rótulo, por `rdo._normalizar_rotulo`, é `passos` — `passos` não é campo canônico e `rdo.py` não se toca; `Texto atual <n>` não se varre e bloco cercado não é literal. Âncora e literal, regex exatas (medidas pelo consultor em protótipo):
  ~~~~
  _ANCORA_RE = re.compile(r"`(?P<caminho>[^`:\s]+\.[A-Za-z0-9]+):(?P<linha>\d+)(?:-(?P<fim>\d+))?`")
  _LITERAL_APOS_ANCORA_RE = re.compile(r"\s*(?:—|:)\s*`(?P<lit>(?:\\`|[^`\\])+)`")
  ~~~~
  literal = `_LITERAL_APOS_ANCORA_RE.match(texto, m.end())`, com `\`` trocado por `` ` `` e `strip()` (forma do corpus: `P-0752` linhas do `FPU-T2`, `FPU-T5a`, `FPU-T8`, `FPU-T10`); confere quando está **contido** em alguma linha (`strip()`) da faixa `linha..fim` de `root / caminho`. Âncora sem literal passa quando o mesmo texto de âncora (`m.group(0)`) tem literal em outra ocorrência do card (Passo que remete a alvo já ancorado).
- **Passos:**
  1. Escrever `conferir_ancoras` com as três falhas nomeadas: `âncora sem literal`, `alvo inexistente`, `literal fora da linha` (mensagem traz o literal esperado e a linha real com `strip()`).
  2. Chamar em `verificar_tarefa` só quando o mundo comparado é `antes` (card não `done`: a entrega desloca as linhas que o card ancorou; DFP-16), apensando as falhas à lista; `main` não muda.
  3. Fixtures: `alvo.txt` com as linhas `um`, `dois`, ``tres `x` ``; `plano-ancoras.md` com quatro cards `ready` cuja Verificação é `` 1. `python -c "print('a')"` → `a` — antes `a`, depois `a` `` (fecha em `antes`). `AN-T1`: Arquivos-alvo `` `tests/fixtures/card_check/alvo.txt:2` — `dois` `` e `` `tests/fixtures/card_check/alvo.txt:3` — `tres \`x\`` ``, e Passo que repete a âncora da linha 2 sem literal (fecha); `AN-T2`: a âncora da linha 2 sem literal, só no Passo (falha `âncora sem literal`); `AN-T3`: Arquivos-alvo `` `tests/fixtures/card_check/alvo.txt:2` — `tres` `` (falha `literal fora da linha`); `AN-T4` sem âncora (fecha).
- **Testes (novos):** TF `test_tf_ancora_com_literal_fecha`, TF `test_tf_ancora_sem_literal_falha`, TF `test_tf_literal_fora_da_linha_falha`, TR `test_tr_card_sem_ancora_nao_muda` (`AN-T4` exit 0).
- **Verificação:**
  1. `python -m pytest tests/test_card_check.py -q` → verde — antes `12 passed` (após `FPU-T1`), depois `16 passed`.
  2. `python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-ancoras.md --tarefa AN-T2` → exit 1 com `âncora sem literal` — antes: arquivo inexistente, exit `1` por `plano inexistente`; depois exit `1` com `âncora sem literal`.
  3. `python -m pytest -q` → nenhuma falha; `passed` ≥ 402 + 4 — antes `402 passed`.
- **Pronto quando:** card.âncoras — enquanto o card não está concluído, toda âncora nos arquivos que ele vai tocar e nos passos leva o literal, e o gate acusa a âncora sem literal e o literal que não está em nenhuma linha da faixa citada; objetivo, verificação e contratos ficam fora da conferência — Verificações 1 e 2; régua executável.conferências — a conferência de âncora roda no `card_check` — Verificação 1.
- **Não fazer:** não varrer `Verificação`, `Objetivo` nem `Contratos` por âncora (só `Arquivos-alvo` e `Passos`, DFP-16); não tocar `rdo.py`; não reescrever card vivo (I-3).
- **Contingências:**
  - se `conferir_ancoras` acusar algo nos cards `ready` deste plano (`FPU-T5`..`FPU-T10`) → não é da entrega; medido no acionamento 4 do consultor, com o protótipo acima: zero falhas depois do reparo das âncoras de `FPU-T2`, `FPU-T6` e `FPU-T8`; registrar em `pendencia=`.
  - Medido em protótipo sobre cópia da árvore (acionamento 4): Verificação 1 `16 passed`; Verificação 2 exit 1 com `âncora sem literal`; suíte `406 passed`; `dead_code.py`, `ratchet_piso.py`, `kit_check.ps1 -Mode validate`, `check-readme.ps1` exit 0.
- **Handover:** 2026-09-26 · para `FPU-T5`, `FPU-T2`
  - **Entregue:** conferir_ancoras(dossie, root) em .claude/tools/card_check.py:256, com _ANCORA_RE (:252) e _LITERAL_APOS_ANCORA_RE (:253); chamada em verificar_tarefa (:449) so com mundo antes; varre linhas brutas de Arquivos-alvo e o extra Passos (DFP-16); falhas nomeadas: ancora sem literal, alvo inexistente, literal fora da linha; fixtures tests/fixtures/card_check/plano-ancoras.md (AN-T1..AN-T4) e alvo.txt
  - **Contrato:** card_check acusa ancora sem literal e literal fora da linha em card nao done; ancora repetida sem literal passa se o mesmo texto de ancora tem literal em outra ocorrencia do card; Objetivo, Verificacao e Contratos nao sao varridos; card done nao confere ancora; test_card_check 16 passed; suite >= 406
  - **Não refazer:** conferencia de ancora ja paga; rdo.py intocado de proposito (Passos lido do extra achatado)
  - **Pendente:** versao 2 do modelo (OP-3 e card.ancoras com o alcance da DFP-16) pendente de validacao do dono no marco; ancoras para arquivos que o proprio card cria saem alvo inexistente no mundo antes - FPU-T2 precisa isenta-las
- **Notas de execução:**
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T3-toda-ancora-de-arquivo-e-linha-do-card-leva-o-literal-e-o-ga.md`, veredito aprovado 100%

### FPU-T4 — O aviso de crença no ato de gravar plano ou diário [Sonnet · esforço medium · classe implementacao]

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T1`
- **Operação do modelo:** `OP-4`
  - OP-4: Um gancho avisa, no ato de gravar plano ou diário, todo número de aceite que chega sem comando.
  - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; card — Quem implementa faz o instrumento ler a forma que o corpus vivo usa; card vivo não se reescreve para caber no instrumento.
- **Objetivo:** `python .claude/tools/crenca_hook.py` (novo gancho `PreToolUse`, matcher `Write|Edit`) lê o payload em stdin e, quando o `file_path` está em `docs/plans/` ou é `docs/DIARIO_DE_OBRAS.md`, conta no conteúdo novo (`content` ou `new_string`) os literais numéricos de aceite sem comando e devolve `{"systemMessage": "<n> número(s) de aceite sem comando no texto novo: número sem comando é crença — medir antes de gravar"}`; zero → sem saída; qualquer exceção → exit 0 sem saída (DFP-5).
- **Fundamento:** DFP-5, F-9, causa 1 de F-10.
- **Arquivos-alvo:**
  - `.claude/tools/crenca_hook.py` (novo)
  - `tests/test_crenca_hook.py` (novo)
  - `.claude/projecoes.json` — `alvos.projeto.chaves.hooks.PreToolUse`: acrescentar `{"matcher": "Write|Edit", "hooks": [{"type": "command", "command": "python {KIT_ROOT}/tools/crenca_hook.py"}]}`
  - `tests/test_materializar.py` (se houver teste que conta os ganchos projetados)
- **Contratos/classes:** `contar_crencas(texto: str) -> int` — literal numérico de aceite é: `\b\d+ passed\b`, `antes \`?\d+\`?`, `depois \`?\d+\`?`, `Medido antes: \d+`, `` `[^`]+:\d+` `` (âncora de linha) — descontados os que estão na mesma linha de um comando (linha contém `` `python `` ou `` `pwsh `` ou está dentro de bloco cercado) ou de um literal logo após a âncora (DFP-4). `main(argv=None, entrada=None) -> int` no padrão de `progresso_hook.main`.
- **Passos:**
  1. Escrever o gancho com `_forcar_utf8`, leitura de stdin, filtro de caminho, `contar_crencas` e a saída JSON em stdout.
  2. Testes: TF `test_tf_numero_sem_comando_avisa` (conteúdo com `410 passed` em prosa → `systemMessage` com `1 número`); TF `test_tf_numero_na_linha_do_comando_nao_avisa` (`` 1. `python -m pytest -q` → verde — antes `397 passed` `` → sem saída); TF `test_tf_fora_de_docs_plans_nao_avisa` (`file_path` em `src/` → sem saída); TR `test_tr_payload_invalido_sai_zero` (stdin vazio → exit 0, sem saída).
  3. Acrescentar a projeção em `projecoes.json`; `python .claude/tools/materializar.py check` sai 0.
- **Verificação:**
  1. `python -m pytest tests/test_crenca_hook.py tests/test_materializar.py -q` → verde — antes `exit 4`, depois `exit 0` (antes o arquivo de teste não existe, erro de coleta; depois 24 testes, 4 novos sobre os 20 de `test_materializar.py`).
  2. `python -c "from pathlib import Path;print(Path('.claude/projecoes.json').read_text(encoding='utf-8').count('crenca_hook.py'))"` → `1` — antes `0`, depois `1`.
  3. `python .claude/tools/materializar.py check` → exit 0 — antes `exit 0`, depois `exit 0` (trava).
  4. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0` (a suíte ganha os 4 testes novos; `409 passed` no acionamento 6 do consultor).
- **Pronto quando:** card.números de aceite — número gravado sem comando recebe aviso no ato de gravar — Verificação 1; régua executável.conferências — o gancho está projetado — Verificações 2 e 3.
- **Não fazer:** não bloquear (`decision: block`) em caso nenhum; não escrever em `settings.json` (I-1); não tocar `progresso_hook.py` nem `ocupacao.py`.
- **Contingências:**
  - se `materializar.py check` recusar o matcher `Write|Edit` → usar matcher `.*` e filtrar por `tool_name` dentro do gancho; registrar em `pendencia=`.
  - se `tests/test_materializar.py` fixar o número de ganchos `PreToolUse` em `2` → o teste que fixa o número é alvo da tarefa (`DM-33` do `P-0740`): passa a `3`, com a asserção de que o terceiro é o `crenca_hook.py`.
- **Handover:** 2026-09-26 · para `FPU-T6`
  - **Entregue:** gancho PreToolUse .claude/tools/crenca_hook.py (contar_crencas :42, _elegivel :63, main :68), projetado em .claude/projecoes.json (matcher Write|Edit, 3o PreToolUse); tests/test_crenca_hook.py (4 testes)
  - **Contrato:** Write/Edit em docs/plans/ ou docs/DIARIO_DE_OBRAS.md com numero de aceite sem comando recebe systemMessage de aviso, nunca bloqueio; excecao sai 0 sem saida; o gancho ja esta vivo no .claude/settings.json do projeto (o teste de apply real de test_materializar.py o materializou)
  - **Não refazer:** gancho e projecao ja pagos
  - **Pendente:** contagem por casamento de padrao infla o numero exibido (um literal casa dois padroes); I-1 inalcancavel enquanto test_materializar roda apply real
- **Notas de execução:**
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T4-o-aviso-de-crenca-no-ato-de-gravar-plano-ou-diario.md`, veredito aprovado 100%

### FPU-T5 — O executor devolve a medida como arquivo, e a evidência a incorpora [Sonnet · esforço high · classe implementacao]

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T1`
- **Operação do modelo:** `OP-5`
  - OP-5: O executor devolve a verificação como arquivo de medida gerado por comando, e o revisor e o loop leem o arquivo.
  - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; retorno do executor — Quem implementa faz o loop e o revisor lerem o arquivo de medida; prosa não conta como verde.
- **Objetivo:** `card_check.py --gravar <caminho.json>` roda os itens no mundo pedido e grava um JSON com um registro por item (DFP-6), sem mudar o exit; `review_evidence.py` incorpora o JSON como seção `## Medida do executor` quando `<dir da evidência>/<plano>-<ID>-medida.json` existe (DFP-17; plano legado sem `--out`: `docs/RDO/evidencia/`), e escreve `## Medida do executor` com `ausente` quando não.
- **Fundamento:** DFP-6, DFP-17, F-6, causa 3 de F-10.
- **Arquivos-alvo:**
  - `.claude/tools/card_check.py` — `verificar_tarefa` (devolver também os registros) e `main` (`--gravar`)
  - `.claude/tools/review_evidence.py` — ponto onde o dossiê é montado antes de `--out` (função que escreve a saída; localizar por `--out` em `main`)
  - `tests/test_card_check.py`, `tests/test_review_evidence.py`
- **Contratos/classes:** JSON: `{"plano": str, "tarefa": str, "mundo": "antes"|"depois", "gerado_em": ISO-8601, "itens": [{"indice": int, "comando": str|null, "exit": int|null, "saida": str (≤400 chars), "bate": bool}]}`. `review_evidence` lê o arquivo por caminho derivado (`<dir da evidência>/<plano>-<ID>-medida.json`) e o transcreve como tabela `| item | comando | exit | bate |` sob `## Medida do executor`.
  `verificar_tarefa(plano, tarefa_id, root, mundo=None) -> tuple[bool, list[str], dict]` (DFP-17): o terceiro elemento é `medida = {"plano": plano_path.as_posix(), "tarefa": dossie.tarefa_id, "mundo": <mundo já resolvido>, "itens": registros}` — o JSON inteiro menos `gerado_em`, que `main` acrescenta ao gravar (`datetime.now(timezone.utc).isoformat(timespec="seconds")`). Registro: um por elemento de `itens` de `_parsear_itens` (item `fora da forma` não entra em `itens`, não tem registro e segue só como falha), criado no início da iteração com `exit: None`, `saida: ""`, `bate: False` e atualizado só no ramo que chama `_rodar_comando`: `exit` = returncode, `saida` = `saida.strip()[:400]`, `bate` = o `_bate_com_medido` daquele ramo; item manual, recusado ou sem valor fica com os valores iniciais.
  Caminho do JSON (DFP-17): `<dir da evidência>` = pai do `--out` depois da resolução que `main` já faz (plano em pasta sem `--out`: `<pasta>/evidencia`); plano legado sem `--out`: `<root>/docs/RDO/evidencia`. `<plano>` = `_caminhos.id_do_plano(plano_path) or plano_path.stem` (o `plano_id` que `montar_documento` já calcula); `<ID>` = `dossie.tarefa_id`.
  `secao_medida_do_executor(caminho_json: Path) -> list[str]`: primeira linha `## Medida do executor`; arquivo ausente → `- ausente: <caminho> não existe`; JSON ilegível ou sem as chaves (`ValueError`, `KeyError`, `TypeError`) → `- ilegível: <caminho> (<erro>)`, sem exceção; presente → `- Arquivo: <caminho>; mundo: <mundo>; gerado em: <gerado_em>`, linha vazia, `| item | comando | exit | bate |`, `|---|---|---|---|` e uma linha por item `| <indice> | <comando entre crases> | <exit> | <true ou false> |` (`comando` ou `exit` nulo → `-`; `|` dentro do comando sai escapado, `replace("|", "\\|")`).
- **Passos:**
  1. `card_check`, `verificar_tarefa`: devolve `(ok, falhas, medida)` (Contratos); o mundo resolvido em `.claude/tools/card_check.py:344` — `if mundo is None:` chega a `main` dentro de `medida`, sem repetir a extração do dossiê. Único chamador: `.claude/tools/card_check.py:484` — `ok, falhas = verificar_tarefa(args.plano, args.tarefa, args.root, mundo=args.mundo)`; nenhum teste chama `verificar_tarefa` direto (todos passam por `main`).
  2. `card_check`, `main`: `--gravar` (`type=Path`, default `None`). Quando vem, grava `medida` + `gerado_em` depois que `verificar_tarefa` retorna, **ok ou não**, com `json.dumps(..., ensure_ascii=False, indent=2)`, `parent.mkdir(parents=True, exist_ok=True)` e escrita atômica pelo padrão de `.claude/tools/review_evidence.py:837` — `fd, tmp_path = tempfile.mkstemp(` (temporário no mesmo diretório + `os.replace`); `CardCheckValidationError` sai exit 1 sem gravar. Exit, stdout e stderr ficam os de hoje.
  3. `review_evidence`: `secao_medida_do_executor` (Contratos). `_renderizar` ganha o kwarg `linhas_medida: list[str] | None = None`, estendido (seguido de linha vazia) logo antes da seção `## Guardas`, isto é, antes de `.claude/tools/review_evidence.py:682` — `linhas.extend(`; `montar_documento` ganha o kwarg `dir_evidencia: Path | None = None` e passa `linhas_medida=secao_medida_do_executor(<caminho do JSON>)`, com o `plano_id` de `.claude/tools/review_evidence.py:728` — `plano_id = _caminhos.id_do_plano(plano_path) or plano_path.stem`. Em `main`, o bloco de `.claude/tools/review_evidence.py:830` — `if args.out is None:` (resolução do destino de plano em pasta) sobe para antes da chamada de `montar_documento`, que recebe `dir_evidencia=args.out.parent if args.out is not None else None`.
  4. Testes (3; `68` → `71`): TF `test_tf_gravar_escreve_um_registro_por_item` em `tests/test_card_check.py` — `card_check.main(["--plano", str(_PLANO_CORPUS), "--tarefa", "CX-T1", "--root", str(_ROOT), "--gravar", str(tmp_path / "medida.json")])` → `0`; o JSON tem `mundo == "antes"`, `tarefa == "CX-T1"`, 1 item com `exit == 0` e `bate is True`. TF `test_tf_evidencia_incorpora_medida` em `tests/test_review_evidence.py` — padrão de `test_cli_main_ok_e_falhou` (`_init_repo_com_baseline`, `plano = tmp_path / "plano.md"` com `_escrever_plano`, `review_evidence.BATERIA_GUARDAS = _BATERIA_FAKE_VERDE`); JSON com o item `{"indice": 1, "comando": "python -c \"print('a')\"", "exit": 0, "saida": "a", "bate": true}` em `tmp_path / "ev" / "plano-T1-medida.json"` (plano sem id → stem `plano`); `main` com `--out tmp_path / "ev" / "plano-T1.md"` → `0`, e o arquivo gravado contém `## Medida do executor` e a linha ``| 1 | `python -c "print('a')"` | 0 | true |``. TR `test_tr_evidencia_sem_medida_diz_ausente` — `montar_documento(plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE)` sem JSON → a seção `## Medida do executor` diz `ausente`.
- **Verificação:**
  1. `python -m pytest tests/test_card_check.py tests/test_review_evidence.py -q` → verde — antes `68 passed`, depois `71 passed` (16 + 52 após `FPU-T1` e `FPU-T3`; medidos no acionamento 5).
  2. `python -c "from pathlib import Path;print(Path('.claude/tools/review_evidence.py').read_text(encoding='utf-8').count('Medida do executor')>=1)"` → `True` — antes `False`, depois `True`.
  3. `python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-corpus.md --tarefa CX-T1 --gravar scratchpad/medida-CX-T1.json` → exit 0 — antes `exit 2`, depois `exit 0` (flag inexistente antes; `scratchpad/` é ignorado pelo `.gitignore` e o `--gravar` cria a pasta).
  4. `python -c "import json;print(json.load(open('scratchpad/medida-CX-T1.json',encoding='utf-8'))['itens'][0]['bate'])"` → `True` — antes `exit 1`, depois `True` (roda depois do item 3).
  5. `python -m pytest -q` → nenhuma falha — antes `406 passed`, depois `409 passed`.
- **Pronto quando:** retorno do executor.evidência de verificação — arquivo de medida gerado por comando, lido pela evidência — Verificações 1 a 4; régua executável.conferências — a medida do executor é registro, não prosa — Verificações 3 e 4.
- **Não fazer:** não tocar `encerrar.py` (I-4); não mudar o exit do `card_check` por causa de `--gravar`; não mudar o nome nem o caminho do dossiê de evidência; não mudar a assinatura de `montar_documento` e `_renderizar` além dos dois kwargs com default `None`; não versionar o JSON de `scratchpad/`.
- **Contingências:**
  - a montagem da saída são três pontos, e o Passo 3 diz o que cada um recebe: `main` (resolve o destino), `montar_documento` (deriva o caminho do JSON), `_renderizar` (escreve a seção) — não é bifurcação (DFP-17).
  - se `dead_code.py` acusar `secao_medida_do_executor` ou um kwarg novo → ambos têm chamador de produção (`montar_documento`); a acusação significa que só os testes os chamam: corrigir a chamada, nunca isentar (DFP-15). Medido no acionamento 5, em cópia com o reparo: `dead_code`, `ratchet_piso`, `kit_check` validate e `check-readme` exit 0.
- **Handover:** 2026-09-26 · para `FPU-T5a`, `FPU-T2`
  - **Entregue:** card_check: verificar_tarefa (.claude/tools/card_check.py:320) devolve (ok, falhas, medida) com medida = {plano, tarefa, mundo resolvido, itens}; main --gravar <json> (:511) acrescenta gerado_em e grava atomico, sem mudar exit; review_evidence: secao_medida_do_executor(caminho_json) em .claude/tools/review_evidence.py:588, montar_documento(..., dir_evidencia=) (:737) e _renderizar(..., linhas_medida=) (:629) poem '## Medida do executor' antes de '## Guardas'
  - **Contrato:** JSON de medida em <dir da evidencia>/<id do plano>-<ID>-medida.json (legado sem --out: docs/RDO/evidencia); evidencia sem o arquivo escreve linha 'ausente', JSON ilegivel 'ilegivel', sem excecao; tabela | item | comando | exit | bate |; suite 409 passed
  - **Não refazer:** --gravar e a secao da evidencia ja pagos; main de review_evidence ja resolve --out antes de montar_documento
  - **Pendente:** saida no JSON guarda a cabeca (strip()[:400]); em item de pytest o sumario 'N passed' fica fora - achado com rota de replanejamento
- **Notas de execução:**
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T5-o-executor-devolve-a-medida-como-arquivo-e-a-evidencia-a-inc.md`, veredito aprovado 100%

### FPU-T5a — O executor, o revisor e o loop falam do arquivo de medida [Sonnet · esforço low · classe redacao]

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T5`
- **Operação do modelo:** `OP-5`
  - OP-5: O executor devolve a verificação como arquivo de medida gerado por comando, e o revisor e o loop leem o arquivo.
  - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; retorno do executor — Quem implementa faz o loop e o revisor lerem o arquivo de medida; prosa não conta como verde.
- **Objetivo:** o executor roda `card_check.py --mundo depois --gravar docs/RDO/evidencia/<plano>-<ID>-medida.json` como último passo antes da linha de retorno; o revisor lê a seção `## Medida do executor` como a terceira entrada de julgamento no lugar de qualquer afirmação de verde; o scrum-master Passo 5 nomeia o arquivo como parte do retorno.
- **Fundamento:** DFP-6, F-6.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-executor.md:127` — `6. **Encerramento**: sinalize \`review\` e encerre. A sua última mensagem é **só** a linha de retorno do despacho`
  - `.claude/agents/pantonic-reviewer.md:34` — `- Três entradas de julgamento, e só elas: o dossiê da tarefa no plano, o dossiê de evidência`
  - `.claude/skills/scrum-master/SKILL.md:109` — `### Passo 5 — Recepção do retorno do executor`
  - `.claude/README.md` (projeção regenerada, se o gerador do kit a reescrever)
- **Passos:**
  1. Executor: antes do item 6, item novo `5a. **Medida gravada**: rode \`python .claude/tools/card_check.py --plano <plano> --tarefa <ID> --mundo depois --gravar docs/RDO/evidencia/<plano>-<ID>-medida.json\`; exit 1 é entrega incompleta, não verde com ressalva.`
  2. Revisor: acrescentar à lista das entradas a frase `a seção \`## Medida do executor\` do dossiê de evidência é a única afirmação de verde admitida; \`ausente\` conta como verificação não feita`.
  3. Scrum-master Passo 5, Saída: acrescentar `e o arquivo de medida em docs/RDO/evidencia/<plano>-<ID>-medida.json, cuja ausência vai ao laudo como verificação não feita`.
  4. Regenerar `.claude/README.md` pelo gerador do kit se ele projetar os agentes tocados; rodar `python .claude/checks/frontmatter_yaml.py` se existir como verbo, senão `pwsh .claude/checks/kit_check.ps1`.
- **Verificação:**
  1. `python -c "from pathlib import Path;print(Path('.claude/agents/pantonic-executor.md').read_text(encoding='utf-8').count('--gravar'))"` → `1` — antes `0`, depois `1`.
  2. `python -c "from pathlib import Path;print(Path('.claude/agents/pantonic-reviewer.md').read_text(encoding='utf-8').count('Medida do executor'))"` → `1` — antes `0`, depois `1`.
  3. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print(t.count('Medida do executor')+t.count('-medida.json')>=1)"` → `True` — antes `False`, depois `True`.
  4. `pwsh .claude/checks/kit_check.ps1` → exit 0 — antes `exit 0`, depois `exit 0` (trava; inclui o frontmatter dos agentes).
- **Pronto quando:** retorno do executor.evidência de verificação — o executor gera o arquivo e o revisor o lê no lugar da prosa — Verificações 1 a 3.
- **Não fazer:** não tocar o frontmatter dos agentes; não tocar o bloco A do scrum-master.
- **Contingências:**
  - se `kit_check.ps1` acusar contagem no `README.md` por causa da regeneração → a frase de contagem não muda nesta tarefa (nenhum agente ou skill criado): parar e sinalizar `blocked` razão `premissa`, colando a saída.
- **Handover:** 2026-09-26 · para `FPU-T4`
  - **Entregue:** pantonic-executor.md item 5a 'Medida gravada' (card_check --mundo depois --gravar docs/RDO/evidencia/<plano>-<ID>-medida.json; exit 1 e entrega incompleta); pantonic-reviewer.md: '## Medida do executor' e a unica afirmacao de verde admitida, 'ausente' conta como verificacao nao feita; scrum-master/SKILL.md Passo 5 Saida nomeia o arquivo de medida
  - **Contrato:** todo executor grava a medida antes da linha de retorno; o revisor julga verde so pela secao Medida do executor; kit_check exit 0
  - **Não refazer:** texto de executor, revisor e Passo 5 ja pagos
  - **Pendente:** em plano em pasta o caminho literal docs/RDO/evidencia/... diverge do que review_evidence le (<pasta>/evidencia); <plano> ambiguo (caminho vs id) - achado com rota de replanejamento
- **Notas de execução:**
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T5a-o-executor-o-revisor-e-o-loop-falam-do-arquivo-de-medida.md`, veredito aprovado 100%

### FPU-T1a — Um teste tranca o marcador de item só no início de linha, com prosa `N.` na continuação do próprio item [Sonnet · esforço low · classe implementacao]

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T1`
- **Operação do modelo:** `OP-1`
  - OP-1: O gate do card passa a ler a forma de Verificação que o corpus vivo usa, a rodar cada comando e a comparar o valor do mundo em que o card está.
  - precisa de: card — Quem implementa faz o instrumento ler a forma que o corpus vivo usa; card vivo não se reescreve para caber no instrumento.
- **Objetivo:** a fixture `tests/fixtures/card_check/plano-corpus.md` ganha o card `CX-T5`, cuja Verificação tem dois itens e a linha de continuação do item 1 traz prosa com `1.` e `2.` fora do início de linha; um TF novo prova que `card_check.verificar_tarefa` reconhece exatamente dois itens e fecha. É o caso do fantasma do `AE-33` do `P-0740`, que o TF `test_tf_marcador_so_no_inicio_de_linha` (`CX-T4`, prosa noutro campo) não discrimina (`AE-34`). Só teste e fixture: o `card_check.py` já se comporta certo.
- **Fundamento:** DFP-3, DFP-18, `AE-34`.
- **Arquivos-alvo:**
  - `tests/fixtures/card_check/plano-corpus.md`
  - `tests/test_card_check.py`
- **Passos:**
  1. Fixture: depois do `CX-T4`, o card `CX-T5` no mesmo nível de cabeçalho dos vizinhos, título `CX-T5 — Card inline com prosa N. na continuação do item de Verificação [Sonnet · classe mecanica]`, com `Status` `ready`, `Objetivo`, `Entregável` (`nenhum — fixture sintética, não é card vivo de plano.`), `Pronto quando` e esta Verificação, três linhas, as duas primeiras sendo o item 1 e sua continuação (cinco espaços de recuo): `  1. \`python -c "print('a')"\` → \`b\` — antes \`a\`, depois \`b\`; medido no` / `     acionamento 1. e conferido na revisão 2. da mesma janela` / `  2. \`python -c "print('c')"\` → \`d\` — antes \`c\`, depois \`d\``. No parágrafo de abertura da fixture, `Quatro cards sintéticos` → `Cinco cards sintéticos` e uma frase sobre o `CX-T5`.
  2. Teste: TF `test_tf_prosa_na_continuacao_do_item_nao_vira_item` — `ok, falhas, medida = card_check.verificar_tarefa(str(_PLANO_CORPUS), "CX-T5", _ROOT)` → `ok is True`, `falhas == []`, `len(medida["itens"]) == 2`. Medido pelo consultor em protótipo (acionamento 6): o parser de hoje dá 2 itens e fecha; o texto achatado das mesmas linhas tem 4 marcadores `N.`.
- **Verificação:**
  1. `python -m pytest tests/test_card_check.py -q -k prosa_na_continuacao` → verde — antes `exit 5`, depois `exit 0` (antes nenhum teste selecionado).
  2. `python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-corpus.md --tarefa CX-T5` → `card_check: OK` — antes `exit 1`, depois `exit 0` (antes `CX-T5` não encontrada).
  3. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`.
- **Pronto quando:** régua executável.conferências — o marcador de item só no início de linha está trancado por teste que falharia sobre o texto achatado — Verificações 1 e 2.
- **Não fazer:** não tocar `.claude/tools/card_check.py` nem `rdo.py`; não mudar `CX-T1`..`CX-T4` nem os testes que os usam.
- **Contingências:**
  - se o TF novo falhar sobre o `card_check.py` de hoje → o comportamento regrediu depois do `FPU-T1`: parar e sinalizar `blocked` razão `premissa`, colando a falha.
- **Handover:** 2026-09-26 · para quem vier depois
  - **Entregue:** card CX-T5 em tests/fixtures/card_check/plano-corpus.md:50 (prosa 1./2. na continuacao do item 1 da Verificacao); TF test_tf_prosa_na_continuacao_do_item_nao_vira_item em tests/test_card_check.py:206
  - **Contrato:** verificar_tarefa sobre CX-T5 -> ok True, falhas [], 2 itens; suite 410 passed
  - **Não refazer:** o fantasma do AE-33/P-0740 esta trancado por teste
  - **Pendente:** nenhum
- **Notas de execução:**
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T1a-um-teste-tranca-o-marcador-de-item-so-no-inicio-de-linha-com.md`, veredito aprovado 100%

### FPU-T5b — A medida guarda a cauda da saída, onde está o sumário [Sonnet · esforço low · classe implementacao]

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T5`
- **Operação do modelo:** `OP-5`
  - OP-5: O executor devolve a verificação como arquivo de medida gerado por comando, e o revisor e o loop leem o arquivo.
  - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; retorno do executor — Quem implementa faz o loop e o revisor lerem o arquivo de medida; prosa não conta como verde.
- **Objetivo:** em `verificar_tarefa` de `.claude/tools/card_check.py`, o campo `saida` do registro de cada item passa de `saida.strip()[:400]` (cabeça) para `saida.strip()[-400:]` (cauda), nas duas formas (8.1 e inline): em item de pytest a cabeça é a barra de pontos e o sumário `N passed` fica fora do JSON (`AE-37`). O teto de 400 caracteres (DFP-6) não muda; a mensagem de `divergencia` (`[:200]`) não muda.
- **Fundamento:** DFP-6, DFP-17, DFP-18, `AE-37`.
- **Arquivos-alvo:**
  - `.claude/tools/card_check.py`
  - `tests/test_card_check.py`
- **Passos:**
  1. Trocar as duas atribuições `registro["saida"] = saida.strip()[:400]` por `saida.strip()[-400:]`.
  2. Teste: TF `test_tf_gravar_guarda_a_cauda_da_saida(tmp_path, capsys)` — grava em `tmp_path` um plano mínimo com um card `ready` cuja Verificação é o item inline `` 1. `python -c "print('x'*500+'FIM')"` → `FIM` — antes `FIM`, depois `FIM` ``; roda `card_check.main` com `--root` = `_ROOT` e `--gravar`; o JSON tem `itens[0]["saida"]` terminando em `FIM` e com 400 caracteres. Medido pelo consultor em protótipo (acionamento 6): com o código de hoje o card fecha, a `saida` tem 400 caracteres e não termina em `FIM`.
- **Verificação:**
  1. `python -m pytest tests/test_card_check.py -q -k cauda_da_saida` → verde — antes `exit 5`, depois `exit 0` (antes nenhum teste selecionado).
  2. `python -c "from pathlib import Path;print(Path('.claude/tools/card_check.py').read_text(encoding='utf-8').count('[:400]'))"` → `0` — antes `2`, depois `0`.
  3. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`.
- **Pronto quando:** retorno do executor.evidência de verificação — o JSON de medida guarda o sumário do comando — Verificação 1.
- **Não fazer:** não mudar o teto de 400 nem a forma do JSON; não tocar `review_evidence.py`.
- **Contingências:**
  - se um teste existente afirmar a cabeça da `saida` → o teste que fixa o comportamento antigo é alvo da tarefa (`DM-33` do `P-0740`): passa a afirmar a cauda; registrar em `pendencia=`.
- **Handover:** 2026-09-26 · para quem vier depois
  - **Entregue:** registro['saida'] = saida.strip()[-400:] nas duas formas (.claude/tools/card_check.py:408 e :462); TF test_tf_gravar_guarda_a_cauda_da_saida em tests/test_card_check.py:308
  - **Contrato:** o JSON de medida guarda os ultimos 400 caracteres da saida (sumario do pytest incluso); forma do JSON e teto inalterados
  - **Não refazer:** cauda da saida ja paga
  - **Pendente:** nenhum
- **Notas de execução:**
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T5b-a-medida-guarda-a-cauda-da-saida-onde-esta-o-sumario.md`, veredito aprovado 100%

### FPU-T6 — O dossiê de despacho carrega os achados roteados ao card [Sonnet · esforço medium · classe implementacao]

- **Status:** `done` · 2026-09-26
- **Operação do modelo:** `OP-6`
  - OP-6: O dossiê de despacho carrega os achados do plano roteados ao card, derivados das entradas de achado e não da memória de quem despacha.
  - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; dossiê de despacho — Quem implementa deriva o precedente dos achados do plano, sem depender de quem despacha lembrar.; achado de execução — Ninguém altera: o achado nasce do laudo e o dossiê o lê.
- **Objetivo:** `backlog.py show <ID>` e `backlog.py next` imprimem, depois do texto do card de plano, o bloco `**Achados roteados a este card:**` com cada entrada `AE-<n>` da seção de achados do plano cujo texto depois de `**Rota:**` cita `<ID>` como palavra inteira (DFP-7), nas duas formas de entrada do corpus (id entre crases, a do consultor, e id sem crase, a do `encerrar.py tarefa --achado`); card sem achado roteado imprime `**Achados roteados a este card:** nenhum`. Plano inteiro, tíquete e subtarefa de tíquete saem como hoje.
- **Fundamento:** DFP-7, DFP-19, F-4, causa 4 de F-10 (`AE-1` do `P-0743` registrado na `DOM-T1` e não colado no despacho da `DOM-T5`).
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py:1008` — `def show(modelo: Modelo, id_: str) -> str:`
  - `.claude/tools/backlog.py:1431` — `linhas_saida.append(_truncar(item.texto, item.arquivo, item.linha_header, item.linha_fim))`
  - `tests/test_backlog.py`
- **Contratos/classes:** (DFP-19)
  - `achados_roteados(texto_plano: str, tarefa_id: str) -> list[str]` em `backlog.py` — recebe `Plano.texto`, já carregado (`show` e `renderizar_next` não recebem `repo`, e `Item.arquivo` é relativo ao repo). Leitura duplicada de `encerrar.achados_do_plano`, sem import: seção = da linha que casa `^## .*Achados da execução` até a próxima que casa `^#{1,2} ` (exclusive) ou o fim; entrada = linha que começa com `- ` na coluna 0 mais as seguintes até a próxima `- ` na coluna 0 ou o fim da seção, sem as linhas em branco do fim; só vale entrada cuja primeira linha casa `\bAE-(\d+)\b` (as duas formas casam; numeração não contígua não importa). Rota = texto da entrada depois da primeira ocorrência de `**Rota:**`, até o fim da entrada (inclui linhas de continuação e anotações posteriores, como `**Destino (…)**`); entrada sem `**Rota:**` nunca é roteada. Filtro: `re.search(rf"(?<![\w-]){re.escape(tarefa_id)}(?![\w-])", rota)`. Devolve o texto verbatim de cada entrada (linhas unidas por `\n`), na ordem do arquivo.
  - `_bloco_achados(texto_plano: str, tarefa_id: str) -> str` — `**Achados roteados a este card:** nenhum` se a lista é vazia; senão a linha `**Achados roteados a este card:**` seguida das entradas, unidas por `\n`.
  - `show`: quando `alvo` é `Item` com `tipo == "tarefa"`, devolve `_truncar(...)` + `"\n\n"` + `_bloco_achados(plano.texto, alvo.id)`, com `plano` = o de `modelo.planos` cujo `id == alvo.pai`; qualquer outro alvo devolve exatamente o de hoje. O bloco fica fora do teto DB-7 (o teto é do texto do card).
  - `renderizar_next`: quando `tipo_pai == "plano"`, `linhas_saida.append(_bloco_achados(pai.texto, item.id))` logo depois da linha do dossiê truncado e antes de `--- pendências mecânicas ---` (o `next` não chama `show`).
- **Passos:**
  1. Escrever `_ACHADOS_HEADING_RE`, `_AE_ID_RE`, `achados_roteados` e `_bloco_achados` logo acima de `show`, com o comentário de duplicação (`sem import cruzado com encerrar.py`, padrão `.claude/tools/rdo.py:137` — `duplicado aqui — sem import cruzado`).
  2. Alterar `show` e `renderizar_next` como no Contratos.
  3. Testes em `tests/test_backlog.py`, **sem alterar a fixture `verde` em disco**: helper `_verde_com_achados(tmp_path)` copia a `verde` com `_copiar_fixture` e apensa ao fim de `docs/plans/P-0001-alfa.md` uma linha em branco, `## Achados da execução`, outra linha em branco e quatro entradas — `AE-1` na forma do consultor (id entre crases) com `**Rota:**` citando `ALF-T1`; `AE-7` na forma do `encerrar.py` (`- **AE-7** (` + crase + `ALF-T1` + crase + `, fechamento, 2026-01-02) — …`) com a `**Rota:**` numa linha de continuação indentada de dois espaços citando `ALF-T1`; `AE-8` que cita `ALF-T1` no texto e não tem `**Rota:**`; `AE-9` com `**Rota:**` citando só `ALF-T1a`. A seção entra no texto do card `ALF-T1` (o `## Achados da execução` não é fronteira de item no `_scan_items`), por isso os asserts olham só o bloco. TF `test_tf_show_lista_achado_roteado` (bloco = o que vem depois de `"\n\n**Achados roteados a este card:**\n"` em `show(modelo, "ALF-T1")`: contém `AE-1`, `AE-7` e a linha de continuação; não contém `AE-8` nem `AE-9`); TF `test_tf_show_sem_achado_diz_nenhum` (`verde` intacta: `show(modelo, "BET-T1")` termina em `"\n\n**Achados roteados a este card:** nenhum"`); TR `test_tr_show_de_tiquete_nao_muda` (`verde` intacta: `show(modelo, "TK-1a") == _localizar(modelo, "TK-1a").texto`, e `renderizar_next` do vencedor `TK-1a` não contém `Achados roteados`); TF `test_tf_next_de_tarefa_de_plano_traz_o_bloco(tmp_path, capsys)` (`main(["next", "--repo", str(_verde_com_handover(tmp_path))])`, vencedor `ALF-T2`: a saída contém `**Achados roteados a este card:** nenhum` depois de `--- dossiê` e antes de `--- pendências mecânicas ---`). Medido pelo consultor em protótipo (acionamento 7): com o `backlog.py` de hoje os três TF falham e o TR passa; com o contrato, os quatro passam.
- **Verificação:**
  1. `python -m pytest tests/test_backlog.py -q` → verde — antes `108 passed`, depois `112 passed`.
  2. `python -c "from pathlib import Path;print(Path('.claude/tools/backlog.py').read_text(encoding='utf-8').count('Achados roteados')>=1)"` → `True` — antes `False`, depois `True`.
  3. `python .claude/tools/backlog.py check` → `check: OK — nenhuma violação.` — antes `OK`, depois `OK` (trava: o `check` da árvore real segue OK com o `backlog.py` alterado).
  4. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`.
  5. `python -c "import subprocess,sys;o=subprocess.run([sys.executable,'.claude/tools/backlog.py','show','FPU-T1'],capture_output=True,text=True,encoding='utf-8').stdout;b=o.split(chr(10)+'**Achados roteados a este card:**'+chr(10));print(len(b)==2 and b[1].count('**Rota:**')>=3)"` → `True` — antes `False`, depois `True` (no corpus real, `AE-1`..`AE-3` do §8 são roteados à `FPU-T1`).
- **Pronto quando:** dossiê de despacho.precedentes — derivados das entradas de achado do plano roteadas ao card — Verificações 1, 2 e 5.
- **Não fazer:** não importar `encerrar.py` (DFP-7, I-4); não mudar o texto do card devolvido antes do bloco nem o `_truncar`; não alterar a fixture `verde` em disco (compartilhada por 20 testes; o vencedor do `next` nela é `TK-1a`); não mudar `_scan_items`; não tocar o índice do diário.
- **Contingências:**
  - se um teste existente de `show` ou `next` afirmar a saída inteira de tarefa de plano → o teste que fixa o comportamento antigo é alvo da tarefa (`DM-33` do `P-0740`): passa a admitir o bloco; registrar em `pendencia=`. Medido no protótipo do consultor: nenhum (suíte inteira verde).
- **Handover:** 2026-09-26 · para `FPU-T5c`
  - **Entregue:** achados_roteados(texto_plano, tarefa_id) em .claude/tools/backlog.py:1012 (le as duas formas de entrada AE, consultor e encerrar.py) e _bloco_achados (:1052); show (:1059) e renderizar_next (:1434) apensam o bloco '**Achados roteados a este card:**' a tarefa de plano; 4 testes novos em tests/test_backlog.py (helper _verde_com_achados)
  - **Contrato:** backlog.py show <ID> e next trazem, depois do dossie, cada AE do plano cuja Rota cita o ID como palavra inteira; sem achado: 'nenhum'; tiquete nao muda; test_backlog 112 passed; suite 419 passed
  - **Não refazer:** bloco de achados no dossie ja pago
  - **Pendente:** o show do ultimo card do plano traz as secoes 6 a 8 junto (_scan_items so corta em heading '## X — ...'), comportamento anterior fora do card
- **Notas de execução:**
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T6-o-dossie-de-despacho-carrega-os-achados-roteados-ao-card.md`, veredito aprovado 100%

### FPU-T5c — A medida do executor mora onde o revisor a procura, também no plano em pasta [Sonnet · esforço low · classe redacao]

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T5a`
- **Operação do modelo:** `OP-5`
  - OP-5: O executor devolve a verificação como arquivo de medida gerado por comando, e o revisor e o loop leem o arquivo.
  - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; retorno do executor — Quem implementa faz o loop e o revisor lerem o arquivo de medida; prosa não conta como verde.
- **Objetivo:** o item 5a do executor e a Saída do Passo 5 do scrum-master deixam de fixar `docs/RDO/evidencia/<plano>-<ID>-medida.json` e passam a derivar o destino como `review_evidence.py` o procura (`AE-42`): `<evidencia>/<P-n>-<ID>-medida.json`, com `<P-n>` o id do plano (`P-0752`, nunca o caminho do `--plano`) e `<evidencia>` = `docs/RDO/evidencia` no plano legado ou `<pasta>/evidencia` no plano em pasta. O `pantonic-reviewer.md` não cita o caminho (só nomeia a seção `## Medida do executor`) e não muda.
- **Fundamento:** DFP-6, DFP-17, DFP-19, `AE-42`.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-executor.md:127` — `5a. **Medida gravada**: rode`
  - `.claude/skills/scrum-master/SKILL.md:119` — `cuja ausência vai ao laudo como verificação não`
  - `.claude/README.md` (projeção regenerada, se o gerador do kit a reescrever)
- **Passos:**
  1. Executor, item 5a: o trecho `` --gravar docs/RDO/evidencia/<plano>-<ID>-medida.json`; exit 1 `` passa a `` --gravar <evidencia>/<P-n>-<ID>-medida.json`, com `<P-n>` o id do plano (`P-0752`, nunca o caminho) e `<evidencia>` = `docs/RDO/evidencia` no plano legado ou `<pasta>/evidencia` no plano em pasta — a pasta em que `review_evidence.py` procura a medida; exit 1 ``.
  2. Scrum-master, Passo 5, Saída: o trecho `` `docs/RDO/evidencia/<plano>-<ID>-medida.json`, cuja ausência `` passa a `` `<evidencia>/<P-n>-<ID>-medida.json` (`<P-n>` o id do plano; `<evidencia>` = `docs/RDO/evidencia` no legado, `<pasta>/evidencia` no plano em pasta), cuja ausência ``, inteiro na mesma linha, sem reflow do parágrafo.
  3. Regenerar `.claude/README.md` pelo gerador do kit se ele projetar os arquivos tocados; rodar `pwsh .claude/checks/kit_check.ps1`. Medido pelo consultor em protótipo (acionamento 7): com os dois textos acima, Verificações 1 a 3 no valor `depois`, `kit_check` validate e `check-readme.ps1` exit 0.
- **Verificação:**
  1. `python -c "from pathlib import Path;fs=['.claude/agents/pantonic-executor.md','.claude/skills/scrum-master/SKILL.md'];print(sum(Path(f).read_text(encoding='utf-8').count('<plano>-<ID>-medida.json') for f in fs))"` → `0` — antes `2`, depois `0`.
  2. `python -c "from pathlib import Path;fs=['.claude/agents/pantonic-executor.md','.claude/skills/scrum-master/SKILL.md'];print(all('<pasta>/evidencia' in Path(f).read_text(encoding='utf-8') and '<P-n>-<ID>-medida.json' in Path(f).read_text(encoding='utf-8') for f in fs))"` → `True` — antes `False`, depois `True`.
  3. `pwsh .claude/checks/kit_check.ps1` → exit 0 — antes `exit 0`, depois `exit 0` (trava; inclui o frontmatter dos agentes).
- **Pronto quando:** retorno do executor.evidência de verificação — o executor grava a medida onde o revisor a lê, no plano legado e no plano em pasta — Verificações 1 e 2.
- **Não fazer:** não tocar `review_evidence.py` nem `pantonic-reviewer.md`; não mexer nas linhas `--out docs/RDO/evidencia/<plano>-<ID>.md` (outra convenção, fora do `AE-42`); não acrescentar nem remover linha em `scrum-master/SKILL.md` (a âncora `SKILL.md:305` da `FPU-T9` conta linhas); não tocar o frontmatter dos agentes nem o bloco A do scrum-master.
- **Contingências:**
  - se `kit_check.ps1` acusar contagem no `README.md` por causa da regeneração → a frase de contagem não muda nesta tarefa (nenhum agente ou skill criado): parar e sinalizar `blocked` razão `premissa`, colando a saída.
- **Handover:** 2026-09-26 · para `FPU-T4a`
  - **Entregue:** .claude/agents/pantonic-executor.md:127 (item 5a) e .claude/skills/scrum-master/SKILL.md:119 (Passo 5, Saida) nomeiam <evidencia>/<P-n>-<ID>-medida.json, <P-n> = id do plano, <evidencia> = docs/RDO/evidencia (legado) ou <pasta>/evidencia (plano em pasta); contagem de linhas do scrum-master inalterada
  - **Contrato:** a medida do executor mora onde review_evidence a procura, nos dois layouts; kit_check exit 0
  - **Não refazer:** caminho da medida ja pago
  - **Pendente:** docs/RDO/evidencia sem crase em pantonic-executor.md:127 (cosmetico)
- **Notas de execução:**
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T5c-a-medida-do-executor-mora-onde-o-revisor-a-procura-tambem-no.md`, veredito aprovado 100%

### FPU-T4a — O aviso de crença conta uma vez o literal que casa dois padrões [Sonnet · esforço low · classe implementacao]

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T4`
- **Operação do modelo:** `OP-4`
  - OP-4: Um gancho avisa, no ato de gravar plano ou diário, todo número de aceite que chega sem comando.
  - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; card — Quem implementa faz o instrumento ler a forma que o corpus vivo usa; card vivo não se reescreve para caber no instrumento.
- **Objetivo:** em `contar_crencas` de `.claude/tools/crenca_hook.py`, os casamentos de todos os padrões numa linha viram trechos `(m.start(), m.end())`; trechos que se sobrepõem formam um grupo, e a linha soma um por grupo, não um por casamento (`AE-44`): o texto `antes`, crase, `397 passed`, crase, `, depois`, crase, `401 passed`, crase conta `2`, não `4`. Os descontos de hoje (linha de comando, bloco cercado, âncora com literal logo depois) não mudam; âncora descontada não entra nos trechos.
- **Fundamento:** DFP-5, DFP-19, `AE-44`.
- **Arquivos-alvo:**
  - `.claude/tools/crenca_hook.py:55` — `for padrao in _PADROES:`
  - `tests/test_crenca_hook.py`
- **Passos:**
  1. No laço de `contar_crencas`, trocar o `total += 1` por casamento por uma lista de trechos da linha; depois do laço dos padrões, ordenar os trechos e somar um a `total` sempre que o início do trecho for maior ou igual ao maior fim já visto na linha.
  2. Teste: TF `test_tf_literais_sobrepostos_contam_uma_vez` em `tests/test_crenca_hook.py` (via `_load_crenca_hook()`): `contar_crencas` do texto do Objetivo devolve `2`. Medido pelo consultor em protótipo (acionamento 7): hoje devolve `4`; com o Passo 1, `2`, os quatro testes existentes seguem verdes e `410 passed` em prosa segue contando `1`.
- **Verificação:**
  1. `python -m pytest tests/test_crenca_hook.py -q -k sobrepostos` → verde — antes `exit 5`, depois `exit 0` (antes nenhum teste selecionado).
  2. `python -c "import sys;sys.path.insert(0,'.claude/tools');import crenca_hook as c;q=chr(96);print(c.contar_crencas('antes '+q+'397 passed'+q+', depois '+q+'401 passed'+q))"` → `2` — antes `4`, depois `2`.
  3. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`.
- **Pronto quando:** card.números de aceite — cada literal sem comando conta uma vez no aviso — Verificações 1 e 2.
- **Não fazer:** não mudar os padrões nem os descontos; não bloquear (`decision: block`); não tocar `projecoes.json` nem `settings.json`.
- **Contingências:**
  - se um teste existente afirmar a contagem por casamento → o teste que fixa o comportamento antigo é alvo da tarefa (`DM-33` do `P-0740`): passa a afirmar a contagem por grupo; registrar em `pendencia=`.
- **Handover:** 2026-09-26 · para `FPU-T7`
  - **Entregue:** contar_crencas (.claude/tools/crenca_hook.py:42) conta uma vez cada grupo de trechos sobrepostos dos padroes (_PADROES, :37); TF test_tf_literais_sobrepostos_contam_uma_vez em tests/test_crenca_hook.py:85
  - **Contrato:** 'antes `397 passed`, depois `401 passed`' conta 2, nao 4; o aviso segue so avisando, nunca bloqueia
  - **Não refazer:** regra de contagem ja paga
  - **Pendente:** nenhum
- **Notas de execução:**
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T4a-o-aviso-de-crenca-conta-uma-vez-o-literal-que-casa-dois-padr.md`, veredito aprovado 100%

### FPU-T7 — O escritor da telemetria recusa a linha repetida da mesma rodada [Sonnet · esforço low · classe implementacao]

- **Status:** `done` · 2026-09-27
- **Depende de:** `TK-88a`
- **Operação do modelo:** `OP-7`
  - OP-7: O escritor da série de telemetria recusa a segunda linha da mesma rodada, e a conferência sai de quem chama.
  - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; série de telemetria — Quem implementa põe a recusa da duplicata no escritor, nunca em quem chama.
- **Objetivo:** `python .claude/tools/telemetria.py append …` sai `3` com `linha repetida: <tarefa> já tem linha com modelo, tool_uses e tokens_k iguais (data <d>)` e não escreve, quando a última linha da mesma `tarefa` na série tem `modelo`, `tool_uses` e `tokens_k` iguais aos da linha nova (DFP-8); qualquer outra diferença apensa como hoje.
- **Fundamento:** DFP-8, DFP-24, F-3, `AE-26` do `P-0745`.
- **Arquivos-alvo:**
  - `.claude/tools/telemetria.py` — `append_row` (linha 116) e `main` (141)
  - `tests/test_telemetria.py`
  - `.claude/tools/encerrar.py:435` — `destino_rdo = _rdo.checar_close(args_precheck, "review")` (a chamada nova entra logo depois do `try` que envolve esta linha; única edição do arquivo, DFP-24)
  - `tests/test_encerrar.py` — um teste novo, nenhum existente muda
- **Contratos/classes:** `ultima_linha_da_tarefa(path: Path, tarefa: str) -> dict[str, str] | None` — cabeçalho = primeira linha quando ela começa por `data	`; sem ela (arquivo criado pelo próprio `append_row`), as colunas de `_COLUMNS`; `eh_repetida(ultima: dict, nova: dict) -> bool` — `modelo`, `tool_uses` e `tokens_k` iguais como texto; `checar_repetida(path: Path, row: str) -> None` — lê a `row` pelas colunas de `_COLUMNS` e lança `TelemetriaRepetidaError(ValueError)` com a mensagem do Objetivo; `append_row(path, row)` e `build_row(args)` **mantêm a assinatura** e `append_row` chama `checar_repetida` antes de ler os bytes, e assim a recusa vale para todo escritor (DFP-24); `main` traduz em exit 3 e `telemetria: FALHOU - <mensagem>` em stderr; `encerrar.fechar_tarefa`, quando `linha_telemetria is not None`, chama `_telemetria.checar_repetida(tsv, linha_telemetria)` logo depois do bloco do `checar_close` e traduz `TelemetriaRepetidaError` em `EncerramentoError(f"telemetria: {exc}")` — recusa antes da primeira escrita (padrão do `TK-88d`).
- **Passos:**
  1. Implementar as duas funções e a exceção; `append_row` conserva a escrita atômica.
  2. Testes: TF `test_tf_append_repetido_recusa` (duas chamadas iguais em `tmp_path` → segunda exit 3, arquivo com uma linha); TF `test_tf_append_com_tokens_diferentes_apensa` (segunda chamada com `tokens_k` diferente → duas linhas); TR `test_tr_serie_existente_nao_reescrita` (bytes anteriores idênticos após a recusa).
  3. `encerrar.py`: acrescentar a chamada do Contratos entre o `try` do `checar_close` e o laço de `pendencia`/`resumo`. Teste TR `test_tr_tarefa_trio_repetido_recusa_sem_escrever` em `tests/test_encerrar.py`: `_montar_repo(tmp_path)` (a série já traz `ALF-T1` `sonnet` `21` `77.5`) e `encerrar.main(_argv_tarefa(repo, **{"--tool-uses": "21", "--tokens-k": "77.5", "--duracao-s": "999.0", "--modelo-agente": "sonnet"}))` → exit 1, `linha repetida` no stderr, `_rdos(repo) == []`, plano igual a `PLANO.format(status_t1="review")` e série igual a `TELEMETRIA`.
- **Verificação:**
  1. `python -m pytest tests/test_telemetria.py -q` → verde — antes `9 passed`, depois `12 passed`.
  2. `python -c "from pathlib import Path;print(Path('.claude/tools/telemetria.py').read_text(encoding='utf-8').count('repetida')>=1)"` → `True` — antes `False`, depois `True`.
  3. `python -m pytest tests/test_telemetria_hook.py tests/test_encerrar.py -q` → verde — antes `exit 0`, depois `exit 0` (trava: o gancho e os testes existentes do fechamento não mudam).
  4. `python -m pytest tests/test_encerrar.py -q -k trio_repetido` → `1 passed` — antes `exit 5`, depois `exit 0`.
  5. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`.
- **Pronto quando:** série de telemetria.linhas por rodada — uma; o escritor recusa a segunda — Verificação 1.
- **Não fazer:** não tocar `telemetria_hook.py` (ele chama o CLI com `check=False` e ignora o exit 3); em `encerrar.py`, nada além da chamada do Passo 3 (I-4 emendada pela DFP-24); não mudar a assinatura de `build_row` nem de `append_row`; não alterar teste existente de `tests/test_encerrar.py`; não reescrever, reordenar ou deduplicar linhas existentes de `docs/telemetria.tsv`.
- **Contingências:**
  - se algum teste existente de `tests/test_encerrar.py` ou `tests/test_telemetria_hook.py` falhar depois do Passo 3 por apensar duas vezes a mesma linha de propósito → parar e sinalizar `blocked` razão `premissa`, nomeando o teste (medido no protótipo da DFP-24: nenhum).
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** telemetria.checar_repetida (.claude/tools/telemetria.py:149) chamada por append_row e por encerrar.fechar_tarefa antes da primeira escrita; exit 3 na linha repetida
  - **Contrato:** a série não aceita segunda linha da mesma tarefa com modelo, tool_uses e tokens_k iguais aos da última
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum
- **Notas de execução:**
  - 2026-09-27 `ready` — consultor DFP-24: recusa em checar_repetida, append_row e build_row sem mudar assinatura; encerrar.py so ganha a chamada de checagem (I-4 emendada)
  - 2026-09-27 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T7-o-escritor-da-telemetria-recusa-a-linha-repetida-da-mesma-ro.md`, veredito aprovado 100%

### FPU-T8 — As armadilhas de ferramenta medidas ganham um arquivo só [Sonnet · esforço low · classe redacao]

- **Status:** `done` · 2026-09-26
- **Operação do modelo:** `OP-8`
  - OP-8: As armadilhas de ferramenta medidas ganham um arquivo só, apontado pela doutrina e pela régua do card.
  - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.
- **Objetivo:** `docs/ARMADILHAS_DE_FERRAMENTA.md` existe com a tabela `| ferramenta | armadilha | caso medido | forma segura |` e as oito linhas de F-11; `GOVERNANCA.md` §3 (bullet *Disciplina de coleta*, linha 214) e `pantonic-planner.md` (campo `Verificação`, linha 450) apontam para ele, e o planejador passa a preferir `python -c` a shell em linha de Verificação.
- **Fundamento:** F-11, causa 5 de F-10, DFP-20.
- **Arquivos-alvo:**
  - `docs/ARMADILHAS_DE_FERRAMENTA.md` (novo)
  - `GOVERNANCA.md:214` — `- **Disciplina de coleta** — \`git status --short\`/\`git log --oneline\` no lugar dos completos;`
  - `.claude/agents/pantonic-planner.md:450` — `- **Verificação:** comandos exatos, executáveis como estão; para tarefa sem artefato executável,`
  - `docs/DOC_MAP.md` (entrada do arquivo novo, logo depois do bloco `## docs/ACIONAMENTOS_CONSULTOR.tsv`; DFP-20)
- **Passos:**
  1. Escrever o arquivo: cabeçalho de uma frase (o que é, quem apensa: quem mede uma armadilha nova apensa uma linha), a tabela com as oito linhas de F-11 (uma por armadilha, com o caso medido e o ponteiro), e a regra `linha de Verificação prefere python -c a shell; PowerShell só com pwsh -Command e aspas simples`. Linhas na ordem de F-11; `caso medido` é o ponteiro entre parênteses de F-11, salvo na linha 4, cujo ponteiro vira `card_check.py`, função `_rodar_comando` (o de F-11 derivou); `armadilha` é o texto de F-11, salvo na linha 1; `ferramenta` e `forma segura` são os textos abaixo, transcritos (DFP-20: cada forma medida pelo consultor); barra vertical dentro de célula vai escapada, `\|`:
     - linha 1 — ferramenta `PowerShell`; armadilha (re-medida, DFP-20): em aspas duplas o PowerShell expande `` `t `` e `$nome`, e `\t` fica como está; quem converte `\t` em tabulação é o literal Python dentro de `python -c "…"` — forma segura: aspas simples no PowerShell, onde nada se expande; em `python -c`, o `\t` que é texto vai em literal cru `r'…'`.
     - linha 2 — ferramenta `PowerShell` — forma segura: `-CaseSensitive` explícito, ou a contagem em `python -c` com `str.count`, que distingue caixa.
     - linha 3 — ferramenta `PowerShell` — forma segura: `(Get-Content f).Count`, ou `len(Path(f).read_text(encoding='utf-8').splitlines())` em `python -c`.
     - linha 4 — ferramenta `Python` — forma segura: linha de Verificação é um processo só, sem `;`, `\|` nem `>`; o filtro e a contagem vão dentro do próprio `python -c`.
     - linha 5 — ferramenta `git` — forma segura: listar os não rastreados à parte, com `git ls-files --others --exclude-standard`.
     - linha 6 — ferramenta `YAML` — forma segura: valor de `description` sem dois-pontos-espaço (trocar por ` - `) ou entre aspas duplas; conferir com `python .claude/checks/frontmatter_yaml.py <arquivo>`.
     - linha 7 — ferramenta `markdown` — forma segura: o literal de aceite se copia da linha física do arquivo, nunca do texto renderizado nem através de quebra de linha, e se confirma antes de publicar com `python -c` que imprime a contagem dele no arquivo.
     - linha 8 — ferramenta `Python` — forma segura: `python -X utf8`, ou `sys.stdout.reconfigure(encoding='utf-8')` antes do primeiro `print`.
  2. `GOVERNANCA.md:214`: o bullet termina em `GOVERNANCA.md:217` — `não-teste redireciona a saída para arquivo e lê só o fim.`; trocar esse ponto final pela frase `; armadilhas de ferramenta medidas: \`docs/ARMADILHAS_DE_FERRAMENTA.md\` — consultar antes de escrever linha de Verificação` seguida de ponto final.
  3. `.claude/agents/pantonic-planner.md:450` (bullet de duas linhas, 450-451): depois do ponto final da linha 451, acrescentar a frase `Prefira \`python -c\` a shell; as armadilhas medidas estão em \`docs/ARMADILHAS_DE_FERRAMENTA.md\`.`
  4. `docs/DOC_MAP.md`: logo depois do bloco `## docs/ACIONAMENTOS_CONSULTOR.tsv` (quatro linhas, título e três campos), acrescentar uma linha vazia e o bloco `## docs/ARMADILHAS_DE_FERRAMENTA.md`, com as três linhas `**Propósito:** armadilhas de ferramenta medidas — a semântica que já enganou um agente, o caso medido e a forma segura, uma linha por armadilha; quem mede uma armadilha nova apensa uma linha.`, `**Quando consultar:** antes de escrever linha de Verificação ou comando de medida.` e `**Acesso:** Read integral.`
- **Verificação:**
  1. `python -c "from pathlib import Path;p=Path('docs/ARMADILHAS_DE_FERRAMENTA.md');print(p.exists() and p.read_text(encoding='utf-8').count('|')>=40)"` → `True` (oito linhas de quatro colunas mais cabeçalho) — antes `False`, depois `True`.
  2. `python -c "from pathlib import Path;print(Path('GOVERNANCA.md').read_text(encoding='utf-8').count('ARMADILHAS_DE_FERRAMENTA'))"` → `1` — antes `0`, depois `1`.
  3. `python -c "from pathlib import Path;print(Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8').count('ARMADILHAS_DE_FERRAMENTA'))"` → `1` — antes `0`, depois `1`.
  4. `pwsh .claude/checks/kit_check.ps1` → exit 0 — antes `exit 0`, depois `exit 0` (trava).
  5. `python -c "from pathlib import Path;p=Path('docs/ARMADILHAS_DE_FERRAMENTA.md');print(p.exists() and '| forma segura |' in p.read_text(encoding='utf-8') and 'git ls-files --others' in p.read_text(encoding='utf-8'))"` → `True` — antes `False`, depois `True`.
  6. `python -c "from pathlib import Path;print(Path('docs/DOC_MAP.md').read_text(encoding='utf-8').count('## docs/ARMADILHAS_DE_FERRAMENTA.md'))"` → `1` — antes `0`, depois `1`.
- **Pronto quando:** armadilhas de ferramenta.residência — um arquivo, apontado pela doutrina e pela régua do card — Verificações 1 a 3, 5 e 6.
- **Não fazer:** não apagar a memória `powershell-contagem-de-linhas` (fora do repositório, I-1); não reescrever linhas de Verificação de card vivo (I-3); não reescrever as formas seguras do Passo 1 (medidas na DFP-20).
- **Contingências:**
  - se o bloco `## docs/ACIONAMENTOS_CONSULTOR.tsv` não estiver mais em `docs/DOC_MAP.md` → acrescentar o bloco do Passo 4 no fim do arquivo.
- **Handover:** 2026-09-26 · para `FPU-T9`
  - **Entregue:** docs/ARMADILHAS_DE_FERRAMENTA.md (tabela | ferramenta | armadilha | caso medido | forma segura |, oito linhas de F-11 com a forma segura medida pela DFP-20); ponteiros em GOVERNANCA.md:217 (Disciplina de coleta), .claude/agents/pantonic-planner.md:450-451 (campo Verificacao) e docs/DOC_MAP.md
  - **Contrato:** quem mede armadilha nova apensa uma linha ao arquivo; linha de Verificacao prefere python -c a shell
  - **Não refazer:** arquivo de armadilhas e ponteiros ja pagos
  - **Pendente:** docs/RUBRICA_DE_REVISAO.md secao 8 (regua de autoria do card) sem ponteiro para o arquivo; armadilha do heredoc Bash (\ vira \) medida pelo consultor e fora da tabela
- **Notas de execução:**
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T8-as-armadilhas-de-ferramenta-medidas-ganham-um-arquivo-so.md`, veredito aprovado 100%

### FPU-T9 — A skill de fatos frescos [Sonnet · esforço medium · classe redacao]

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T8`
- **Operação do modelo:** `OP-9`
  - OP-9: A skill de fatos frescos faz toda mensagem ao dono declarar a origem de cada número, e memória deixa de ser origem admitida.
  - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; mensagem ao dono — Quem implementa faz a origem de cada número ser declarada antes de enviar; memória não é origem.
- **Objetivo:** `.claude/skills/fatos-frescos/SKILL.md` existe (gatilho: antes de escrever despacho, relatório de janela, encerramento, handover ou mensagem ao dono que leve número, caminho com linha, hash ou contagem); o corpo manda tabular cada valor com a origem em três classes — `rodado neste turno (comando)`, `copiado de <arquivo:linha>`, `memória` — e proíbe enviar valor de origem `memória`; onde há instrumento para o número (`encerrar.py plano`, `telemetria.py`, `card_check.py`), manda usá-lo (DFP-12). A skill é citada por `mensagem-ao-dono` §1, pelo `scrum-master` (seção *Relatório de encerramento*) e pela `passagem-de-bastao` (Parte 3); a frase de contagem do `README.md` passa de `doze skills` a `treze skills` e a tabela de skills ganha a linha.
- **Fundamento:** DFP-12, F-8, causas 1 e 3 de F-10 (total de janela inflado, `AE-26` do `P-0745`; hash copiado de registro antigo).
- **Arquivos-alvo:**
  - `.claude/skills/fatos-frescos/SKILL.md` (novo; frontmatter `name`, `description` sem `: ` no valor — F-11)
  - `.claude/skills/mensagem-ao-dono/SKILL.md:21` — `## 1. Checagem antes de enviar`
  - `.claude/skills/scrum-master/SKILL.md:305` — `## Relatório de encerramento`
  - `.claude/skills/passagem-de-bastao/SKILL.md` — Parte 3, item 2 (`**Materializar o status e registrar**`)
  - `README.md:851` — `O kit são dez agentes, doze skills, quatro verificadores executáveis e a declaração de projeções,` e a tabela de skills da mesma seção
  - `.claude/README.md` (projeção regenerada)
- **Passos:**
  1. Escrever a skill: gatilho, a tabela de origem (três classes), a proibição, a lista de instrumentos por tipo de número, e um exemplo antes/depois de duas linhas.
  2. `mensagem-ao-dono` §1: acrescentar o item `- [ ] Todo número, caminho com linha, hash ou contagem passou pela skill \`fatos-frescos\` (origem declarada; memória não é origem).`
  3. Scrum-master, *Relatório de encerramento*: acrescentar, depois de `Contadores finais`, a frase `— pela skill \`fatos-frescos\`: totais vêm de \`encerrar.py plano\` ou da série, nunca de soma à mão`.
  4. Passagem-de-bastão, Parte 3 item 2: acrescentar `handover passa pela skill \`fatos-frescos\` antes de gravar`.
  5. `README.md:851`: `doze skills` → `treze skills`; tabela de skills: linha nova na forma das vizinhas.
  6. Regenerar `.claude/README.md` pelo gerador do kit; `pwsh .claude/checks/check-readme.ps1` exit 0.
- **Verificação:**
  1. `python -c "from pathlib import Path;print(Path('.claude/skills/fatos-frescos/SKILL.md').exists())"` → `True` — antes `False`, depois `True`.
  2. `python -c "from pathlib import Path;print(sum(Path(p).read_text(encoding='utf-8').count('fatos-frescos') for p in ['.claude/skills/mensagem-ao-dono/SKILL.md','.claude/skills/scrum-master/SKILL.md','.claude/skills/passagem-de-bastao/SKILL.md'])>=3)"` → `True` — antes `False`, depois `True`.
  3. `python -c "from pathlib import Path;t=Path('README.md').read_text(encoding='utf-8');print(t.count('treze skills'),t.count('doze skills'))"` → `1 0` — antes `0 1`, depois `1 0`.
  4. `pwsh .claude/checks/check-readme.ps1` → exit 0 — antes `exit 0`, depois `exit 0` (a frase e a tabela batem com o disco: 13).
  5. `python .claude/checks/frontmatter_yaml.py` → exit 0 — antes `exit 0`, depois `exit 0`.
- **Pronto quando:** mensagem ao dono.origem dos números — declarada por número: rodado neste turno ou copiado de arquivo e linha — Verificações 1 e 2.
- **Não fazer:** não criar gancho nem instrumento nesta tarefa; não tocar o bloco A do scrum-master; não tocar `GOVERNANCA.md`.
- **Contingências:**
  - se `check-readme.ps1` acusar outra contagem por extenso além da linha 851 (`AE-6` do `P-0750`) → trocar também a ocorrência acusada, só ela, e registrar em `pendencia=` a linha.
- **Handover:** 2026-09-26 · para `FPU-T10`
  - **Entregue:** .claude/skills/fatos-frescos/SKILL.md (nova; origem por valor em tres classes, memoria proibida); citada em mensagem-ao-dono secao 1, scrum-master Relatorio de encerramento (Contadores finais) e passagem-de-bastao Parte 3 item 2; README.md 'treze skills' + linha na tabela; .claude/README.md regenerado por kit_check -Mode generate
  - **Contrato:** toda mensagem ao dono com numero, caminho:linha, hash ou contagem passa pela skill; check-readme e kit_check check-drift OK com 13 skills
  - **Não refazer:** nada a declarar
  - **Pendente:** a secao Instrumentos da skill manda rodar encerrar.py plano (que FECHA o plano) para totais de janela e telemetria.py (so tem append) para consumo; a skill se diz 'regua executavel' contra a OP-9 - card corretivo da OP-9 via consultor
- **Notas de execução:**
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T9-a-skill-de-fatos-frescos.md`, veredito ressalva 88%

### FPU-T8a — A régua de autoria do card aponta as armadilhas de ferramenta [Sonnet · esforço low · classe redacao]

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T8`
- **Operação do modelo:** `OP-8`
  - OP-8: As armadilhas de ferramenta medidas ganham um arquivo só, apontado pela doutrina e pela régua do card.
  - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.
- **Objetivo:** a `## 8` de `docs/RUBRICA_DE_REVISAO.md`, que se nomeia "régua de **autoria** do card", passa a apontar `docs/ARMADILHAS_DE_FERRAMENTA.md` (`AE-46`): a OP-8 manda o arquivo ser apontado pela doutrina e pela régua do card, e a `FPU-T8` só o apontou em `GOVERNANCA.md` e no campo `Verificação` do planejador.
- **Fundamento:** DFP-20, DFP-21, `AE-46`.
- **Arquivos-alvo:**
  - `docs/RUBRICA_DE_REVISAO.md:288` — `> Fonte da verdade: régua de **autoria** do card, aplicada **antes** do despacho`
- **Passos:**
  1. Na linha 288, depois do ponto final de `esta julga o dossiê que a pediu.`, acrescentar, na mesma linha, um espaço e a frase `Armadilhas de ferramenta medidas: \`docs/ARMADILHAS_DE_FERRAMENTA.md\` — consultar antes de escrever linha de Verificação.` Medido pelo consultor em protótipo (acionamento 9): Verificações 1 e 2 no valor `depois`.
- **Verificação:**
  1. `python -c "from pathlib import Path;print(Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8').count('ARMADILHAS_DE_FERRAMENTA'))"` → `1` — antes `0`, depois `1`.
  2. `python -c "from pathlib import Path;l=Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8').splitlines();print([x.startswith('> Fonte da verdade') for x in l if 'ARMADILHAS_DE_FERRAMENTA' in x]==[True])"` → `True` — antes `False`, depois `True`.
- **Pronto quando:** armadilhas de ferramenta.residência — um arquivo, apontado pela doutrina e pela régua do card — Verificações 1 e 2.
- **Não fazer:** não acrescentar nem remover linha em `docs/RUBRICA_DE_REVISAO.md` (a âncora das linhas 340-341 do `TK-89b` conta linhas); não tocar a `### 8.1` (matéria do `TK-89b`) nem a tabela de critérios; não tocar `docs/ARMADILHAS_DE_FERRAMENTA.md`.
- **Contingências:**
  - se a linha 288 não começar mais por `> Fonte da verdade` → acrescentar a frase ao fim da linha do blockquote que abre a `## 8`, onde ela estiver, e registrar a linha em `pendencia=`.
- **Handover:** 2026-09-26 · para `FPU-T9a`
  - **Entregue:** docs/RUBRICA_DE_REVISAO.md:288 (linha '> Fonte da verdade' da secao 8) ganhou o ponteiro para docs/ARMADILHAS_DE_FERRAMENTA.md na mesma linha; contagem do arquivo mantida em 373
  - **Contrato:** a regua de autoria do card aponta as armadilhas medidas
  - **Não refazer:** ponteiro na rubrica ja pago
  - **Pendente:** nenhum
- **Notas de execução:**
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T8a-a-regua-de-autoria-do-card-aponta-as-armadilhas-de-ferrament.md`, veredito aprovado 100%

### FPU-T9a — A skill de fatos frescos lê os totais em instrumento de leitura e se declara medida em prosa [Sonnet · esforço low · classe redacao]

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T9`
- **Operação do modelo:** `OP-9`
  - OP-9: A skill de fatos frescos faz toda mensagem ao dono declarar a origem de cada número, e memória deixa de ser origem admitida.
  - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; mensagem ao dono — Quem implementa faz a origem de cada número ser declarada antes de enviar; memória não é origem.
- **Objetivo:** a skill `fatos-frescos` deixa de mandar rodar `encerrar.py plano` (que fecha o plano) e `telemetria.py` (que só apensa) para obter números, e aponta os instrumentos de leitura da DFP-21 — tarefas fechadas na projeção do índice de `docs/DIARIO_DE_OBRAS.md`, consumo na série `docs/telemetria.tsv` (`AE-47`); o exemplo cita uma linha real da série; a skill se declara a medida em prosa da DFP-12, sem o rótulo "régua executável" (`AE-48`); o *Relatório de encerramento* do `scrum-master` troca `encerrar.py plano` pelo índice do diário e pela série.
- **Fundamento:** DFP-12, DFP-21, `AE-47`, `AE-48`.
- **Arquivos-alvo:**
  - `.claude/skills/fatos-frescos/SKILL.md:10` — `skill é a régua executável dessa medida — não substitui o instrumento onde ele existe (DFP-12).`
  - `.claude/skills/fatos-frescos/SKILL.md:35` — `Onde existe instrumento para o número, o instrumento é obrigatório — a tabela de origem cobre o`
  - `.claude/skills/fatos-frescos/SKILL.md:49` — `- antes: \`Fechamos 3 tarefas nesta janela, consumo de ~40k tokens.\``
  - `.claude/skills/scrum-master/SKILL.md:316` — `totais vêm de \`encerrar.py plano\` ou da série, nunca de soma à mão.`
- **Passos:**
  1. Skill, linha 10: o trecho `skill é a régua executável dessa medida — não substitui o instrumento onde ele existe (DFP-12).` passa a `skill é a medida em prosa da DFP-12, e não conferência executável — não substitui o instrumento onde ele existe (DFP-12, emendada pela DFP-21).`
  2. Skill, `Instrumentos por tipo de número`: o título fica; o corpo (linhas 35 a 45, do parágrafo `Onde existe instrumento…` ao fim do bullet **Evidência de card**) passa a ser o parágrafo e os três bullets abaixo, transcritos, com quebra de linha livre até 100 colunas:
     - parágrafo: `Onde existe instrumento de leitura para o número, ele é obrigatório — a tabela de origem cobre o que não tem um (DFP-12, emendada pela DFP-21). Instrumento que escreve não é origem: \`encerrar.py plano\` fecha o plano (exige o veredito do dono e recusa plano com tarefa aberta) e \`telemetria.py\` só apensa linha à série.`
     - bullet 1: `- **Tarefas fechadas do plano** → a projeção \`(<status>, <fechadas>/<total>)\` do plano no índice de \`docs/DIARIO_DE_OBRAS.md\`, que \`backlog.py status\` reescreve a cada transição, lida no turno e citada como \`copiado de docs/DIARIO_DE_OBRAS.md:<linha>\`; as fechadas na janela são as que o próprio relatório lista com o RDO; nunca contagem de cabeça.`
     - bullet 2: `- **Consumo** (tool_uses, tokens, duração) → a série \`docs/telemetria.tsv\`: de uma tarefa, a linha dela, citada como \`copiado de docs/telemetria.tsv:<linha>\`; acumulado da janela, a soma rodada no turno, \`python -c "import csv;r=[l for l in csv.DictReader(open('docs/telemetria.tsv',encoding='utf-8'),delimiter='\t') if l['tarefa'].startswith('<prefixo>')];print(len(r),round(sum(float(l['tokens_k']) for l in r),1))"\`; nunca soma à mão.` O comando foi rodado pelo consultor (acionamento 9) com o prefixo `FPU-T`: exit 0, dois números.
     - bullet 3: o bullet **Evidência de card** de hoje, sem mudança.
  3. Skill, `Exemplo`: as linhas de hoje (antes e depois, linhas 49 a 52) passam a duas, `- antes: A FPU-T9 custou uns 90k tokens.` e `- depois: A FPU-T9 custou 91.5k tokens e 31 tool_uses (copiado de \`docs/telemetria.tsv:894\`).` — a linha 894 da série é a da `FPU-T9`, medida pelo consultor.
  4. Scrum-master, linha 316: o trecho `totais vêm de \`encerrar.py plano\` ou da série, nunca de soma à mão.` passa a `totais vêm do índice do diário e da série \`docs/telemetria.tsv\`, nunca de soma à mão.`, na mesma linha, sem reflow. Medido pelo consultor em protótipo (acionamento 9): com os Passos 1 a 4, Verificações 1 a 3 no valor `depois`.
- **Verificação:**
  1. `python -c "from pathlib import Path;s=Path('.claude/skills/fatos-frescos/SKILL.md').read_text(encoding='utf-8');print('encerrar.py plano --plano' in s,'é a régua executável' in s,'medida em prosa' in s)"` → `False False True` — antes `True True False`, depois `False False True`.
  2. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');q=chr(96);print(t.count('totais vêm de '+q+'encerrar.py plano'),t.count('totais vêm do índice do diário e da série'))"` → `0 1` — antes `1 0`, depois `0 1`.
  3. `python -c "from pathlib import Path;s=Path('.claude/skills/fatos-frescos/SKILL.md').read_text(encoding='utf-8');c=Path('docs/telemetria.tsv').read_text(encoding='utf-8').splitlines()[893].split(chr(9));print('docs/telemetria.tsv:894' in s and '91.5k tokens e 31 tool_uses' in s and c[2]=='FPU-T9' and c[4]=='31' and c[5]=='91.5')"` → `True` — antes `False`, depois `True` (o exemplo confere com a linha que ele cita).
  4. `python .claude/checks/frontmatter_yaml.py` → exit 0 — antes `exit 0`, depois `exit 0` (trava).
  5. `pwsh .claude/checks/check-readme.ps1` → exit 0 — antes `exit 0`, depois `exit 0` (trava: a `description` não muda).
- **Pronto quando:** mensagem ao dono.origem dos números — declarada por número: rodado neste turno ou copiado de arquivo e linha — Verificações 1 a 3.
- **Não fazer:** não tocar o frontmatter da skill (a `description` alimenta `.claude/README.md`); não tocar `mensagem-ao-dono` nem `passagem-de-bastao` (o item do checklist é o ponto de uso da skill, não conferência da régua — DFP-21); não tocar `encerrar.py` (I-4) nem `telemetria.py` (`FPU-T7`); não tocar o bloco de fechamento do plano no `scrum-master` (`encerrar.py plano --plano`); não acrescentar nem remover linha em `scrum-master/SKILL.md`.
- **Contingências:**
  - se a linha 894 de `docs/telemetria.tsv` não for mais a da `FPU-T9` → parar e sinalizar `blocked` razão `premissa`, colando a linha (a série nunca se reescreve, DFP-8).
- **Handover:** 2026-09-26 · para `FPU-T10`
  - **Entregue:** .claude/skills/fatos-frescos/SKILL.md: linha 10 declara a skill 'medida em prosa da DFP-12'; secao Instrumentos le totais no indice do diario e consumo na serie docs/telemetria.tsv; exemplo cita docs/telemetria.tsv:894 (FPU-T9); .claude/skills/scrum-master/SKILL.md:316 idem
  - **Contrato:** nenhum instrumento de escrita (encerrar.py plano, telemetria.py) e origem de numero na skill; frontmatter e check-readme OK
  - **Não refazer:** instrumentos de leitura ja pagos
  - **Pendente:** fatos-frescos/SKILL.md:57 tem duas sequencias barra-crase (literal com crase fora de bloco cercado, contra o criterio xi da rubrica 8)
- **Notas de execução:**
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T9a-a-skill-de-fatos-frescos-le-os-totais-em-instrumento-de-leit.md`, veredito aprovado 100%

### FPU-T10 — A tabela de acionamentos ganha a coluna de causa raiz [Sonnet · esforço low · classe redacao]

- **Status:** `done` · 2026-09-27
- **Depende de:** `FPU-T2`, `FPU-T6`, `FPU-T7`
- **Operação do modelo:** `OP-10`
  - OP-10: A tabela de acionamentos ganha a coluna de causa raiz com o vocabulário fechado de classes, cada uma nomeando o que a pega: a conferência da régua ou, onde a régua não tem, nenhuma conferência e o que a pega fora dela.
  - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; tabela de acionamentos — Quem implementa acrescenta a coluna com vocabulário fechado; linha anterior recebe o valor vazio.; ocorrência de erro por crença — Ninguém altera: a coluna da tabela de acionamentos é o que a mede.
- **Objetivo:** `docs/ACIONAMENTOS_CONSULTOR.tsv` ganha a décima coluna `causa_raiz`; todas as linhas de dados existentes recebem `-` (DFP-9; eram 40 na autoria, 50 depois do acionamento 6 do consultor, e crescem uma por acionamento); o consultor (`pantonic-consultant.md:38`) preenche a coluna com um dos seis tokens `valor-reutilizado`, `premissa-nao-sondada`, `auto-relato`, `regra-esquecida`, `semantica-de-ferramenta`, `contexto-presumido` ou `-`; `GOVERNANCA.md` §3, na linha *Consultoria* da tabela de modelo por fase (linha 92), aponta a subseção nova `Vocabulário de causa raiz`, que diz, para cada token, o que o pega: nos quatro primeiros, uma conferência da régua executável; em `semantica-de-ferramenta` e `contexto-presumido`, nenhuma conferência da régua — a lista de armadilhas e o checklist da `mensagem-ao-dono` ficam fora dela (DFP-21, DFP-22).
- **Fundamento:** DFP-9, DFP-22, DFP-25, F-7, F-10; a métrica da §0.
- **Arquivos-alvo:**
  - `docs/ACIONAMENTOS_CONSULTOR.tsv` — linha 1 (cabeçalho de nove campos) e todas as linhas de dados
  - `.claude/agents/pantonic-consultant.md:38` — `5. **Apensa uma linha de estatística por acionamento** a \`docs/ACIONAMENTOS_CONSULTOR.tsv\``
  - `GOVERNANCA.md` — nova subseção `### 3.3 Vocabulário de causa raiz` depois da `### 3.2` (antes de `## 4`), e a linha 92 da tabela
  - `.claude/README.md` (projeção regenerada, se o gerador do kit a reescrever)
- **Passos:**
  1. TSV: apensar `\tcausa_raiz` ao cabeçalho e `\t-` a cada linha de dados, por script Python que lê e reescreve em UTF-8 com `\n`, sem tocar nenhum outro byte das linhas. O arquivo tem hoje terminador CRLF em todas as linhas (medido, DFP-25): o script separa as linhas com `splitlines()` e grava cada uma terminada em LF, o canônico do `.gitattributes`; o terminador é a única outra mudança de byte, e não é desvio.
  2. `.claude/agents/pantonic-consultant.md`: a linha 38 inteira (item 5) é substituída pelas sete linhas do bloco abaixo, nesta ordem, transcritas sem mudar nenhum caractere (DFP-25). A primeira é a linha 38 com `causa_raiz` depois de `inconclusivo` na lista de campos e uma frase nova no fim; as seis seguintes são os sub-itens do item 5 e, no arquivo, começam com três espaços, como os sub-itens do item 3; a linha em branco que precede `## O que você não faz` fica depois delas. O texto depois do travessão de cada sub-item é a coluna `o que é` do Passo 3.

     ~~~~
     5. **Apensa uma linha de estatística por acionamento** a `docs/ACIONAMENTOS_CONSULTOR.tsv`, com os campos separados por tabulação, na ordem `data`, `plano`, `acionamento`, `tarefa`, `gatilho`, `motivo`, `classe_impedimento`, `rota`, `inconclusivo`, `causa_raiz`. `gatilho` é a classe 1-4 da §2 de `docs/consultant-spec.md` (1 card `blocked`; 2 laudo com pendência substantiva; 3 impedimento de instrumento que nenhum card cobre; 4 ato do dono no marco); `acionamento` é o número de ordem no plano; `inconclusivo` é o que a decisão deliberadamente não fechou, ou `-`. O consumidor é o `TK-55`, acumulador da spec de robustez. `causa_raiz` é a classe do erro por crença que originou o acionamento, do vocabulário fechado da §3.3 de `GOVERNANCA.md`, onde está também o que pega cada classe, ou `-` quando nenhuma das seis o explica; o critério de cada classe:
        - `valor-reutilizado` — valor reutilizado em vez de medido;
        - `premissa-nao-sondada` — premissa não sondada na autoria;
        - `auto-relato` — auto-relato aceito;
        - `regra-esquecida` — regra ou precedente esquecido;
        - `semantica-de-ferramenta` — semântica de ferramenta;
        - `contexto-presumido` — contexto presumido com o dono.
     ~~~~

  3. `GOVERNANCA.md`, duas edições, com o texto literal dos blocos abaixo (células da DFP-22, tokens entre crases; DFP-25). (a) Subseção nova inserida antes de `GOVERNANCA.md:477` — `## 4. Fluxo de desenvolvimento`: o título `### 3.3 Vocabulário de causa raiz`, uma linha em branco, a tabela e a frase do bloco, e uma linha em branco antes do `## 4`; a linha em branco que hoje precede o `## 4` fica antes do título.

     ~~~~
     | token | o que é | o que o pega |
     |---|---|---|
     | `valor-reutilizado` | valor reutilizado em vez de medido | conferência da régua: o literal da âncora no card_check e o aviso de número gravado sem comando |
     | `premissa-nao-sondada` | premissa não sondada na autoria | conferência da régua: o card_check no ensaio da autoria e no despacho |
     | `auto-relato` | auto-relato aceito | conferência da régua: o arquivo de medida do executor, lido pela evidência |
     | `regra-esquecida` | regra ou precedente esquecido | conferência da régua: os achados roteados ao card, colados no dossiê de despacho |
     | `semantica-de-ferramenta` | semântica de ferramenta | nenhuma conferência da régua: a lista docs/ARMADILHAS_DE_FERRAMENTA.md, consultada no ponto de uso |
     | `contexto-presumido` | contexto presumido com o dono | nenhuma conferência da régua: o checklist da mensagem-ao-dono, que chama a skill fatos-frescos, medida em prosa |

     A parcela de linhas com causa fora de `-` por plano fechado é a medida deste vocabulário; linha de base: 25 de 40 acionamentos em 2026-09-26 (`P-0752` F-10).
     ~~~~

     (b) Na linha 92 (linha *Consultoria* da tabela de modelo por fase), o trecho da primeira linha do bloco (ocorrência única no arquivo) passa a ser o da segunda.

     ~~~~
     `docs/ACIONAMENTOS_CONSULTOR.tsv` | Não reabre
     `docs/ACIONAMENTOS_CONSULTOR.tsv`; causa raiz pelo vocabulário da §3.3 | Não reabre
     ~~~~
- **Verificação:**
  1. `python -c "import csv;from pathlib import Path;r=list(csv.reader(Path('docs/ACIONAMENTOS_CONSULTOR.tsv').open(encoding='utf-8',newline=''),delimiter='\t'));print(len(r[0]),r[0][-1],all(len(l)==len(r[0]) for l in r[1:]))"` → `10 causa_raiz True` — antes `9 inconclusivo True`, depois `10 causa_raiz True` (toda linha de dados com o número de campos do cabeçalho).
  2. `python -c "from pathlib import Path;c=chr(96);t=Path('.claude/agents/pantonic-consultant.md').read_text(encoding='utf-8').splitlines();p=[('valor-reutilizado','valor reutilizado em vez de medido;'),('premissa-nao-sondada','premissa não sondada na autoria;'),('auto-relato','auto-relato aceito;'),('regra-esquecida','regra ou precedente esquecido;'),('semantica-de-ferramenta','semântica de ferramenta;'),('contexto-presumido','contexto presumido com o dono.')];print(t[38:44]==['   - '+c+k+c+' — '+v for k,v in p],(c+'inconclusivo'+c+', '+c+'causa_raiz'+c+'.') in t[37] and t[37].endswith('o critério de cada classe:'),t[44]=='')"` → `True True True` — antes `False False False`, depois `True True True` (os seis sub-itens na ordem, a linha 38 com a lista e a frase nova, a linha em branco depois deles).
  3. `python -c "from pathlib import Path;print(Path('GOVERNANCA.md').read_text(encoding='utf-8').count('Vocabulário de causa raiz')>=1)"` → `True` — antes `False`, depois `True`.
  4. `python .claude/tools/backlog.py check` → `check: OK — nenhuma violação.` — antes `OK`, depois `OK` (trava: a subseção nova não cria citação órfã).
  5. `python -c "from pathlib import Path;print(Path('GOVERNANCA.md').read_text(encoding='utf-8').count('nenhuma conferência da régua'))"` → `2` (as duas classes que a régua não pega) — antes `0`, depois `2`.
  6. `python -c "from pathlib import Path;c=chr(96);t=Path('GOVERNANCA.md').read_text(encoding='utf-8');print(sum(t.count('| '+c+k+c+' | ')==1 for k in 'valor-reutilizado premissa-nao-sondada auto-relato regra-esquecida semantica-de-ferramenta contexto-presumido'.split()),t.count('por plano fechado é a medida deste vocabulário; linha de base: 25 de 40 acionamentos em 2026-09-26 ('+c+'P-0752'+c+' F-10).'),t.count(c+'docs/ACIONAMENTOS_CONSULTOR.tsv'+c+'; causa raiz pelo vocabulário da §3.3 | '))"` → `6 1 1` — antes `0 0 0`, depois `6 1 1` (as seis linhas da tabela, a frase da medida e a linha 92).
- **Pronto quando:** tabela de acionamentos.causa raiz por linha — coluna presente, vocabulário fechado de seis classes, preenchida a cada acionamento — Verificações 1 a 3, 5 e 6.
- **Não fazer:** não classificar as linhas anteriores (DFP-9); não mudar nenhum outro campo do TSV; não tocar `docs/consultant-spec.md`.
- **Contingências:**
  - se alguma linha de dados do TSV tiver número de campos diferente de nove antes da edição → parar e sinalizar `blocked` razão `premissa`, nomeando a linha.
- **Handover:** 2026-09-27 · para `pantonic-consultant`
  - **Entregue:** docs/ACIONAMENTOS_CONSULTOR.tsv com a 10ª coluna causa_raiz (linhas anteriores '-'), pantonic-consultant.md:38 com os seis tokens, GOVERNANCA.md ### 3.3 Vocabulário de causa raiz e linha 92 apontando para ela
  - **Contrato:** cada acionamento do consultor preenche causa_raiz com um dos seis tokens ou '-'
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum
- **Notas de execução:**
  - 2026-09-27 `ready` — DFP-25: Passos 1-3 com o literal em bloco cercado; V2 e V6 travam o texto
  - 2026-09-27 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T10-a-tabela-de-acionamentos-ganha-a-coluna-de-causa-raiz.md`, veredito aprovado 100%

## 6. Ordem de execução

`FPU-T1` → `FPU-T3` → `FPU-T5` → `FPU-T2` → `FPU-T5a` → `FPU-T1a` → `FPU-T5b` → `FPU-T4` → `FPU-T6` → `FPU-T5c` → `FPU-T4a` → `FPU-T7` → `FPU-T8` → `FPU-T9` → `FPU-T8a` → `FPU-T9a` → `FPU-T10` (DFP-10; `FPU-T1a` e `FPU-T5b` pela DFP-18; `FPU-T5c` e `FPU-T4a` pela DFP-19; `FPU-T8a` e `FPU-T9a` pela DFP-21). `FPU-T7` espera o `TK-88a` fechar (I-4; `done` em 2026-09-26).

## 7. Fora de escopo

- A comunicação com o dono além da origem dos números (`P-0750`, feito).
- Classificar as 40 linhas anteriores da tabela de acionamentos (DFP-9).
- Qualquer edição em `encerrar.py` (`TK-88a`, I-4), fora a chamada de checagem da `FPU-T7` (DFP-24), e em `settings.json` ou na pasta global do usuário (I-1).
- Ensaio em cópia dos valores `depois` (DFP-11): é o revisor quem re-mede.

## 8. Achados da execução

- **`AE-1`** (2026-09-26, `FPU-T1` `blocked` premissa) — o Passo 1 afirmava "único chamador" de `rdo._parsear_campos`, mas `tests/test_rdo.py:1017` e `:1040` o chamam direto desempacotando dois valores; mudar a assinatura contradizia a cláusula "test_rdo verde sem alteração". As contagens do card também estavam velhas (`53`/`61` contra `60`/`68` medidos), e a do `FPU-T5` (`46` testes de `test_review_evidence.py` contra `52` medidos). **Rota:** absorvido em DFP-13; cards `FPU-T1` e `FPU-T5` reparados.
- **`AE-2`** (2026-09-26, `FPU-T1` `blocked` premissa, 2ª parada) — o Passo 2 e o DFP-2 tinham `→` como obrigatório na forma inline, e a Contingência 1 esperava ler como inline o item 3 do `EBK-T1` (`P-0751:151`), que só tem o par; a Verificação 2 (`exit 0`) também não fechava sob leitura nenhuma: o item 1 do `EBK-T1` tem esperado em prosa, e o Passo 2 dizia "bloco cercado na linha seguinte", o que leria o `EX-T4` como 8.1. **Rota:** absorvido em DFP-14; Passos 2-3, Verificação 2, Pronto quando e Contingência 1 do `FPU-T1` e o passo 4 do `FPU-T2` reparados.
- **`AE-3`** (2026-09-26, `FPU-T1` `blocked` premissa, 3ª parada) — o invólucro `_parsear_campos` que a DFP-13 mandou manter só tinha chamador em `tests/test_rdo.py:1017` e `:1040`, e o gate bloqueante `dead_code.py` (G-DEADCODE) reprova símbolo vivo só por teste; o reparo do acionamento 1 mediu pytest, mas não os guardrails. **Rota:** absorvido em DFP-15; Arquivos-alvo, Passo 1, Testes e Contingências do `FPU-T1` reparados.
- **`AE-4`** (2026-09-26, `FPU-T3` recusado no item 3 do gate de delegação, antes do despacho) — o contrato de `conferir_ancoras` lia `campos_linhas["passos"]` e os extras `Texto atual` com "mesma linha" e "primeiro bloco cercado", mas `passos` não é campo canônico de `rdo` e os extras chegam achatados; `rdo.py` não é alvo. Três âncoras de cards vivos do plano também falhariam no gate novo (`FPU-T2`, `FPU-T6`, `FPU-T8`). **Rota:** absorvido em DFP-16; Contratos, Passos 1-3, Verificação 3 (antes `402`), Não fazer e Contingências do `FPU-T3` e as âncoras de `FPU-T2`, `FPU-T6`, `FPU-T8` reparados.
- **`AE-5`** (2026-09-26, `FPU-T5` `blocked` premissa, 1ª parada) — o JSON do `--gravar` exige `mundo` resolvido, que só existe dentro de `verificar_tarefa` (`card_check.py:344`), e o Passo 1 fixava a tupla `(ok, falhas, registros)` sem ele; o card também dizia que testes chamam `verificar_tarefa` (nenhum chama), deixava o caminho do JSON dependente de um `--out` que `montar_documento` não recebe, tinha dois candidatos para "depois da seção de diff" e publicava V3 com `%TEMP%\`. **Rota:** absorvido em DFP-17; card `FPU-T5` reparado.
- **AE-34** (`FPU-T1`, fechamento, 2026-09-26) — Revisor: o TF test_tf_marcador_so_no_inicio_de_linha (CX-T4, prosa 'acionamento 1. medido' no campo Contingencias) nao discrimina a DFP-3 - o parser antigo so lia o campo verificacao; o fantasma do AE-33 do P-0740 e prosa 'N.' na linha de continuacao do proprio item de Verificacao. Comportamento novo correto (exercitado em plano sintetico: codigo novo exit 0 com 2 itens, base 24648624 exit 1 com 3 fantasmas), mas nenhum teste o tranca. **Rota:** replanejamento do P-0752: fixture com prosa 'N.' na continuacao do item de Verificacao, absorvivel no FPU-T5 (que ja estende tests/test_card_check.py). **Destino (consultor, acionamento 6):** card corretivo `FPU-T1a` (DFP-18).
- **AE-35** (`FPU-T1`, fechamento, 2026-09-26) — Revisor: review_evidence.py --desde <ref de git stash create> nao carrega arquivo nao rastreado; lista ~260 '??' anteriores ao despacho como tocados e acusa 31 'fora dos alvos e sem atribuicao'. Reconciliado pelo revisor: git diff da base toca so os alvos + registro da orquestracao; a fixture nova e o unico '??' da entrega. **Rota:** tiquete no diario: review_evidence.py registrar os nao rastreados presentes na captura da base e exclui-los do confronto. **Destino (consultor, acionamento 6):** já coberto pelo `TK-84`/`TK-84a` (`ready`, aberto pelo consultor do `P-0751`: não rastreado com mtime anterior ao commit de `desde` sai dos tocados); sem tíquete novo.
- **AE-36** (`FPU-T3`, fechamento, 2026-09-26) — Revisor/modelador: a DFP-16 estreitou o alcance da conferencia de ancora (so Arquivos-alvo e Passos, so card nao done) sem ato de modelo; o modelador gravou a versao 2 do modelo como pendente (secao 1A, OP-3 e card.ancoras). Se aceita no marco, o card FPU-T3 (sub-bullet OP-3 do campo Operacao do modelo e o Pronto quando) fica copiando o texto antigo. **Rota:** marco do plano: validar ou recusar a versao 2 do modelo com o dono; aceita, o consultor alinha as copias no card FPU-T3. **Validada** pelo consultor (`DFP-23`, acionamento 11) e aceita pelo dono (*"Validar agora"*, 2026-09-26); promoção pelo modelador, e o alinhamento das cópias do `FPU-T3` e do `FPU-T10` logo depois, pelo condutor
- **AE-37** (`FPU-T5`, fechamento, 2026-09-26) — Revisor: o contrato DFP-6/DFP-17 guarda saida = saida.strip()[:400], a cabeca da saida; em item de pytest a cabeca e so a barra de pontos e o sumario 'N passed' (o valor medido) fica fora do JSON (medido: FPU-T5 --mundo depois, itens 1 e 5). O campo bate carrega o veredito e a tabela da evidencia nao mostra saida, sem dano ao julgamento hoje. **Rota:** replanejamento do P-0752 a triar pelo consultor: guardar a cauda (ou cabeca+cauda) da saida antes que ela vire leitura de alguem. **Destino (consultor, acionamento 6):** card corretivo `FPU-T5b` (cauda, DFP-18).
- **AE-38** (`FPU-T2`, fechamento, 2026-09-26) — Revisor: review_evidence.py nao reconhece a entrada de Arquivos-alvo na forma 'caminho:linha - <literal>' que a DFP-16 tornou norma; 3 dos 4 alvos da FPU-T2 sairam como fora dos alvos ou ato do dono. Reconciliado por git diff e mtime. **Rota:** tiquete no diario: parser de Arquivos-alvo do review_evidence aceitar a ancora com literal. **Destino (consultor, acionamento 6):** tíquete `TK-89`, card `TK-89a` (medido: a crase escapada do literal desalinha o par de crases; o corte do literal antes da varredura dá 5 alvos na `FPU-T2` e só muda cards do `P-0752` em 314 do acervo). Até ele fechar, as evidências de `FPU-T5a`, `FPU-T8`, `FPU-T9` e `FPU-T10` listam os alvos ancorados como fora dos alvos: reconciliar por `git diff`.
- **AE-39** (`FPU-T2`, fechamento, 2026-09-26) — Revisor: a Verificacao 5 do card FPU-T2 ('antes exit <crase>0<crase>, depois exit <crase>0<crase>') fica fora do regex do par - card_check sai exit 1 em antes e em depois; trava conferida a mao (check-readme.ps1 exit 0). **Rota:** a da pendencia: consultor de plano (B1). **Destino (consultor, acionamento 6):** DFP-18 — o mesmo defeito estava em 7 cards vivos do plano (20 itens `sem valor antes`) e em 3 âncoras velhas (`scrum-master/SKILL.md:105`→`109`, `:299`→`303`, `pantonic-planner.md:447`→`450`, deslocadas pela própria `FPU-T2`); Verificações de `FPU-T5a`, `FPU-T4`, `FPU-T6`..`FPU-T10` reescritas na forma da DFP-14, sem estender o regex.
- **AE-40** (`FPU-T2`, fechamento, 2026-09-26) — Revisor: scrum-master/SKILL.md:62 segue dizendo 'sete itens' do gate de delegacao (agora oito) e a linha B3 do bloco B lista so G-PLANREADY, gate de delegacao e modelo.py check como gatilho, enquanto o Passo 3 manda o exit 1 do card_check para B3. **Rota:** tiquete corretivo no diario: 'sete' por 'oito' e card_check no gatilho de B3. **Destino (consultor, acionamento 6):** tíquete `TK-89`, card `TK-89b`.
- **AE-41** (`FPU-T2`, fechamento, 2026-09-26) — Revisor: RUBRICA_DE_REVISAO.md 8.1 (linhas 339-343) diz que o literal da ancora e 'comparado por strip() contra a linha citada'; a DFP-16 e o instrumento (card_check.py:306-307) conferem o literal contido em alguma linha da faixa linha..fim. **Rota:** tiquete corretivo no diario, junto do anterior (doutrina do gate). **Destino (consultor, acionamento 6):** tíquete `TK-89`, card `TK-89b`.
- **AE-42** (`FPU-T5a`, fechamento, 2026-09-26) — Revisor: o card fixou o caminho literal docs/RDO/evidencia/<plano>-<ID>-medida.json para o executor gravar e o scrum-master nomear, mas review_evidence.py:777-781 le o JSON no pai do --out, que em plano em pasta e <pasta>/evidencia - plano em pasta sai 'ausente' mesmo com o executor cumprindo o texto; e <plano> vale caminho em --plano e id (P-0752) no nome do JSON. O P-0752 (legado) nao exercita o ramo. **Rota:** replanejamento do P-0752: card corretivo da OP-5 que troca o literal pelo destino derivado (legado: docs/RDO/evidencia; pasta: <pasta>/evidencia) e desambigua <plano> em executor, reviewer e scrum-master Passo 5 **Destino (consultor, acionamento 7):** card corretivo `FPU-T5c` (DFP-19; o `pantonic-reviewer.md` não cita o caminho e não muda).
- **AE-43** (`FPU-T4`, fechamento, 2026-09-26) — Revisor: a I-1 do P-0752 (nenhum executor escreve em .claude/settings.json) e inalcancavel por construcao - as Verificacoes 1 e 4 do FPU-T4 e a bateria de guardas executam tests/test_materializar.py::test_tr_drift_projeto_ok_no_repositorio_real_depois_do_apply (linhas 547-557), que roda materializar apply contra o repositorio real; medido: settings.json reescrito 6 s depois da edicao de projecoes.json, e o crenca_hook ja esta vivo nele. **Rota:** replanejamento do P-0752: emendar a I-1 e o passo de fechamento do FPU-T4 (gancho ja projetado e vivo) e confrontar o teste de apply real com a I-1 para todo card que projeta gancho **Destino (consultor, acionamento 7):** I-1 emendada (DFP-19); nenhum card vivo do plano projeta gancho; sem card nem tíquete.
- **AE-44** (`FPU-T4`, fechamento, 2026-09-26) — Revisor: os padroes de Contratos do FPU-T4 se sobrepoem (antes `397 passed` casa \d+ passed e antes `?\d+`?) e o card nao diz se a contagem e por literal ou por casamento; a entrega conta por casamento - medido: 'antes `397 passed`, depois `401 passed`' devolve '4 numero(s)' para dois literais. O aviso dispara certo; o numero exibido fica inflado. **Rota:** replanejamento do P-0752: card corretivo que fecha a regra de contagem (um literal por trecho sobreposto) com teste que discrimine casamento de literal **Destino (consultor, acionamento 7):** card corretivo `FPU-T4a` (DFP-19).
- **AE-45** (`FPU-T5c`, fechamento, 2026-09-26) — Revisor: a Verificacao 2 do FPU-T5c nao discrimina o literal do Passo 1 - a entrega grafou docs/RDO/evidencia sem crase em .claude/agents/pantonic-executor.md:127 (o card pede entre crases; o scrum-master:119 manteve); sentido intacto. **Rota:** replanejamento do P-0752: o proximo card que tocar pantonic-executor.md:127 repoe a crase; a regua (xii)(a) do paragrafo 8 cobre a licao para cards futuros **Destino (consultor, acionamento 9):** sem card (DFP-21): crase cosmética, sentido intacto, nenhum card vivo toca a linha; a rota do revisor segue para quem a tocar. **Destino revisto (dono, 2026-09-26):** corrigido no ato por ordem do dono — `docs/RDO/evidencia` entre crases em `.claude/agents/pantonic-executor.md:127`; erro inequívoco não se adia (regra acrescentada a `.claude/agents/pantonic-consultant.md` item 3 e à `A8` de `.claude/skills/scrum-master/SKILL.md`).
- **AE-46** (`FPU-T8`, fechamento, 2026-09-26) — Revisor: a OP-8 diz 'apontado pela doutrina e pela regua do card'; o card mapeou 'regua do card' para pantonic-planner.md:450 (campo Verificacao), e docs/RUBRICA_DE_REVISAO.md secao 8, que se nomeia 'regua de autoria do card', segue sem ponteiro para docs/ARMADILHAS_DE_FERRAMENTA.md; entrega fiel ao card. **Rota:** replanejamento do P-0752 a triagem do consultor: ponteiro na rubrica secao 8 (card corretivo da OP-8 ou tiquete) **Destino (consultor, acionamento 9):** card corretivo `FPU-T8a` (DFP-21).
- **AE-47** (`FPU-T9`, fechamento, 2026-09-26) — Revisor: DFP-12 e o card nomeiam encerrar.py plano como instrumento de totais de janela e telemetria.py como instrumento de consumo, mas encerrar.py plano FECHA o plano (exige --veredito do dono, recusa plano com tarefa aberta) e telemetria.py so tem append; a skill fatos-frescos (secao Instrumentos) e o exemplo dela (encerrar.py plano --plano P-0752, id onde --plano pede caminho) mandam rodar o fechamento do plano para contar tarefas no meio dele; scrum-master:313 salva-se pelo 'ou da serie'. **Rota:** triagem do consultor: card corretivo da OP-9 que troca o instrumento de totais de janela por um de leitura (serie docs/telemetria.tsv, ou backlog.py/estado do plano) e o de consumo pela leitura da serie **Destino (consultor, acionamento 9):** card corretivo `FPU-T9a` (DFP-21: índice do diário e série `docs/telemetria.tsv`; o exemplo passa a citar `docs/telemetria.tsv:894`).
- **AE-48** (`FPU-T9`, fechamento, 2026-09-26) — Revisor: a OP-9 declara 'nenhuma conferencia nova entra como frase de skill', e o card (Passo 2, DFP-12) acrescenta uma conferencia em prosa ao checklist da mensagem-ao-dono secao 1; a skill se chama 'a regua executavel dessa medida'; as Verificacoes 1-2 (arquivo existe; contagem >=3 do nome) nao discriminam o conteudo. **Rota:** triagem do consultor no mesmo card corretivo da OP-9: declarar a skill como a medida em prosa da DFP-12 (sem o rotulo regua executavel) e dar a Verificacao um item que confira o exemplo contra o arquivo citado **Destino (consultor, acionamento 9):** card corretivo `FPU-T9a` (DFP-21: defeito do card, sem drift do modelo; a Verificação 3 confere o exemplo contra a linha citada).
- **AE-49** (`FPU-T9a`, fechamento, 2026-09-26) — Revisor: o Passo 3 do FPU-T9a publicou a linha nova do Exemplo em crase simples com crases internas escapadas por barra invertida, contra o criterio (xi) da RUBRICA secao 8 (literal com crase vai em bloco cercado); .claude/skills/fatos-frescos/SKILL.md:57 ficou com duas sequencias barra-crase. **Rota:** replanejamento do P-0752 via consultor: card corretivo da OP-9 que reescreve a linha 57 com o literal em bloco cercado e Verificacao que conta chr(92)+chr(96) no arquivo (antes 2, depois 0) **Destino (dono, 2026-09-26):** corrigido por ordem direta do dono, sem card: o Exemplo de `.claude/skills/fatos-frescos/SKILL.md` foi para dois blocos cercados `~~~~`; `python -c "from pathlib import Path;print(Path('.claude/skills/fatos-frescos/SKILL.md').read_text(encoding='utf-8').count(chr(92)+chr(96)))"` → `0`; `card_check --tarefa FPU-T9a --mundo depois` segue OK (a Verificação 3 dele confere as substrings do exemplo).
- **AE-50** (`FPU-T7`, fechamento, 2026-09-27) — review_evidence: a ref de despacho (git stash create) não carrega arquivo não rastreado, e o trecho de encerrar.py/test_encerrar.py sai inteiro, sem diff **Rota:** auditoria final
- **AE-51** (`FPU-T10`, fechamento, 2026-09-27) — docs/ACIONAMENTOS_CONSULTOR.tsv fora do git: a evidência cola o arquivo inteiro sem baseline e 'não mudar outro campo' só se confere por estrutura (mesma causa do AE-50) **Rota:** auditoria final
