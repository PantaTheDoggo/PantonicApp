# RDO — P-0740 · LM-T5d

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T5d` — A rubrica posta em dia: a suspensão do gate e o critério do rótulo
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — a rubrica de autoria fica em dia com o que esta janela mediu: quem a ler sabe que o gate está **suspenso em efeito** e por quê, e encontra o critério do **rótulo de campo** que o `AE-34` custou.

**Arquivos-alvo:** - `docs/RUBRICA_DE_REVISAO.md`

**Verificação:** 1. ``` pwsh -NoProfile -Command "(Select-String -Path docs/RUBRICA_DE_REVISAO.md -Pattern 'suspenso em efeito' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. 2. ``` pwsh -NoProfile -Command "(Select-String -Path docs/RUBRICA_DE_REVISAO.md -Pattern 'AE-33' -SimpleMatch -CaseSensitive | Measure-Object).Count" ``` → **≥ 1** (o ponteiro do achado). **Medido antes: 0**. 3. ``` pwsh -NoProfile -Command "(Select-String -Path docs/RUBRICA_DE_REVISAO.md -Pattern 'AE-34' -SimpleMatch -CaseSensitive | Measure-Object).Count" ``` → **≥ 1** (o critério `(xvi)` e seu caso medido). **Medido antes: 0**. 4. ``` pwsh -NoProfile -Command "(Select-String -Path docs/RUBRICA_DE_REVISAO.md -Pattern 'AE-35' -SimpleMatch -CaseSensitive | Measure-Object).Count" ``` → **≥ 1** (o critério `(xvii)` e seu caso medido). **Medido antes: 0**. 5. ``` pwsh -NoProfile -Command "(Select-String -Path docs/RUBRICA_DE_REVISAO.md -Pattern 'AE-49' -SimpleMatch -CaseSensitive | Measure-Object).Count" ``` → **≥ 1** (o critério `(xviii)` e seu caso medido). **Medido antes: 0**. 6. ``` pwsh -NoProfile -Command "(Select-String -Path docs/RUBRICA_DE_REVISAO.md -Pattern 'enquanto o commit for por marco' -SimpleMatch | Measure-Object).Count" ``` → **1** (o parágrafo datado da `## 3`). **Medido antes: 0**.

**Pronto quando:** a `### 8.1` traz a nota datada; os critérios `(xvi)`, `(xvii)` e `(xviii)` estão na tabela com os casos `AE-34`, `AE-35` e `AE-49` nomeados e a contagem da seção fechada em **dezoito**; a `## 3` traz o parágrafo datado que delimita a frase do `AE-13`; as **seis** linhas de `Verificação` saem como escritas; e **nada além dessas duas seções** mudou no arquivo.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` · 2026-09-19 — card novo do `ESC-17` (2026-09-19). **Fora do caminho crítico**, e **explicitamente não antes do marco**: existe só para que a superfície publicada não prescreva um gate que hoje reprova card conforme.
- **Esforço:** medium — era `low` com três produtos; o `ESC-28` acrescentou o `(xviii)` e o `ESC-31` o produto (e), e esforço declarado que não acompanha o produto é a mesma prosa defasada que este plano vem fechando.
- **Depende de:** `LM-T5c` (fechada — é o estado dela que a nota descreve). Nada depende desta.
- **Produto do módulo:** um parágrafo datado na `### 8.1`, logo abaixo da frase do gate, com quatro fatos e nenhum juízo novo: (a) o gate está **suspenso em efeito desde 2026-09-19**, por decisão do loop endossada pelo consultor (`DM-39` (ii), `DM-40` (i)); (b) a conferência dos três elementos segue **manual**, como a própria seção já prescreve para o período sem instrumento; (c) **o vermelho do `card_check` não é evidência** enquanto o `AE-33` item 1 estiver aberto — ele produz **item fantasma** sobre card conforme; (d) o ponteiro: `AE-33` no `P-0740`, e a reativação do gate depende dele.
- **Produto (b), acrescentado pelo `ESC-18` (`DM-41`) — o critério `(xvi)` da rubrica:** **rótulo de campo termina na mesma linha em que começa.** Decoração no rótulo (data, `ESC-n`, `DM-n`, ressalva) é permitida **enquanto o `:**` couber na primeira linha**; o parser de campos do kit lê **linha a linha**, de modo que rótulo quebrado faz o campo **desaparecer**, não apenas ficar feio. Caso medido: `AE-34` — o `Pronto quando` da `LM-T4b` quebrou depois de `(iii) —` e `review_evidence.py` saiu **exit 1**, `campo obrigatório ausente em 'LM-T4b': 'pronto-quando'`, com a entrega **pronta e verde**. É o décimo terceiro caso da classe e o **primeiro a derrubar o instrumento de evidência**, não o comando de aceite; e é o mais barato de todos de aferir, porque quem gera o dossiê **já falha ruidosamente** — o critério só nomeia a causa para quem escreve.
- **Produto (c), acrescentado pelo `ESC-19` (`DM-42` (iii)) — o critério `(xvii)` da rubrica:** **o aceite cobre o mundo que o próprio produto cria.** Quando o módulo **emite** uma forma, a `Verificação` exercita **essa** forma, e não só a que ele consome: produto que escreve num formato e é aferido noutro deixa o ramo que ele mesmo produz sem nenhuma linha que o discrimine. Caso medido: `AE-35` item 2 — a `LM-T4b` aferiu **só** o ramo em prosa; o ramo canônico `· data · razão — cauda`, que é exatamente o que a escrita dela emite ao transitar para `blocked` com `--razao`, não tinha **nenhuma** linha de aceite, e é nele que a cauda se perde (`AE-35` item 1). É a variação nova do critério (xii): não é alvo inalcançável, é **ramo não coberto** — e o décimo quarto caso da série.
- **Produto (d), acrescentado pelo `ESC-28` — o critério `(xviii)` da rubrica:** **o valor publicado no literal `Medido antes` é invariante ao que outras entregas movem.** Ele mede o que **este** card possui — exit code do comando, veredito binário, recorte do arquivo-alvo —, nunca um total de corpus que qualquer outra entrega desloca (total de suíte, contagem de módulo compartilhado, contagem de cards ou de insumos do próprio plano). Quando a pergunta é sobre corpus, o comando publica o **veredito** (`exit 0`, `iguais`, `1`) e o número absoluto desce para a prosa como referência **datada**, fora do literal. É o (x)/(xiii) levado até onde o instrumento o lê: a norma já dizia *relação, nunca constante*, mas a forma normativa exige o literal `Medido antes` e o `card_check` o compara como **substring literal** — de modo que o card obediente ao (xiii) era **re-congelado pelo gate**. Caso medido: `AE-49` — a baseline de suíte da `LM-T11` envelheceu **três vezes na mesma janela** (187, 191, 197), duas delas custando escalonamento ao consultor, e a `LM-T5a`, que escrevia *"Medido no `ESC-6`"* justamente para obedecer ao (xiii), reprovava no gate por `elemento ausente - Medido antes`.
- **Produto (e), acrescentado pelo `ESC-31` — a `## 3` reconciliada com o que a janela mediu:** a última frase da `## 3. Autoridade da evidência` afirma hoje que o reviewer *"não depende de injeção manual de contexto do orquestrador (`AE-13`)"*. Medido nesta janela: **falso em seis de seis revisões** — o loop injetou contexto em todo despacho de reviewer, e sem isso a atribuição seria ambígua. A frase **não se apaga e não se inverte**: ela está certa sobre o que fala, que é a marcação `da entrega`/`alheio` **por arquivo**. O que entra é um parágrafo **datado**, logo abaixo dela, com três fatos e nenhum juízo novo: (a) a atribuição do dossiê é **por arquivo** e segue dispensando injeção manual para a pergunta de **escopo**; (b) **enquanto o commit for por marco** (diretiva de execução do dono, 2026-09-18, item 3), o recorte `--desde <commit>` acumula as entregas do marco e um mesmo arquivo-alvo carrega autoria de várias tarefas — neste regime a injeção manual de contexto **é obrigatória** e faz parte do despacho do reviewer, não é desvio de quem orquestra; (c) o que suspende essa obrigação é **capacidade**, não card: atribuição por **hunk**. Caso medido: a diretiva do dono previu a obrigação *"até a `LM-T3` fechar a atribuição"*, a `LM-T3` **fechou** e a obrigação permaneceu, porque ela resolveu atribuição por **arquivo** e a ambiguidade é por **hunk** (`AE-55`, `AE-56`).
- **Restrições desta tarefa:** a frase do gate **não se apaga** — suspende-se em efeito, com data, e quem a reativa é o card que fechar o `AE-33`. A `### 8.2` fica **intocada**. Nenhum critério **existente** é reescrito: o `(xvi)` **entra ao lado**, como item novo da mesma tabela, e a frase que conta os critérios da seção fecha no mesmo ato (`DM-18` (i)) — de **quinze** para **dezoito**, porque o `ESC-19` acrescentou o `(xvii)` e o `ESC-28` o `(xviii)` ao mesmo card. Na `## 3`, a frase do `AE-13` **não se apaga nem se inverte**: o parágrafo novo entra **abaixo** dela e a delimita. A diretiva do dono **não** é emendada por este card — o parágrafo a **cita** e a aplica.
- **Não fazer:** não tocar `.claude/tools/card_check.py` (o reparo é matéria do `AE-33`, pós-marco); não reautorar card nenhum; não commitar.
- **Contingências:** 1. se a frase do gate não estiver na `### 8.1` no despacho → parar e sinalizar `blocked` razão `premissa`, citando o que encontrou.

## Execução

**Consumo:** 11 tool uses, 75.3 k tokens, 222.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Entrega exemplar no que o card soletrou: a frase do AE-13 sobreviveu intacta, o paragrafo novo entrou abaixo dela, a 8.2 e o card_check.py ficaram intocados (mtime 07:27 contra 17:37 do alvo) e as seis linhas de Verificacao saem como escritas ao serem re-rodadas. O defeito que sobrou e invisivel a Verificacao por Select-String: nenhuma das seis linhas conta criterios, e a unica frase que os conta ficou internamente contraditoria depois da propria edicao da entrega. Aceite por ocorrencia de literal nao discrimina coerencia de prosa - enquanto a classe da contagem defasada nao tiver varredura mecanica, ela reincide por baixo de seis linhas verdes.

## Fechamento

**Desdobramento:** aprovado com ressalva
