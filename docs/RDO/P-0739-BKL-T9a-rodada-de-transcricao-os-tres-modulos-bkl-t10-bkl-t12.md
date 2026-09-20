# RDO — P-0739 · BKL-T9a

**Plano:** `docs/plans/P-0739-backlog-instrumento.md`
**Tarefa:** `BKL-T9a` — Rodada de transcrição: os três módulos `BKL-T10`..`BKL-T12`
**Modelo:** Opus · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — **transcrever**, sem re-decidir nada, a partição já fechada no `AE-13`, deixando o plano com três cards de módulo despacháveis a frio (`BKL-T10`, `BKL-T11`, `BKL-T12`) e os cinco cards absorvidos fora da fila. Partição, ordem, mapa de herança, regra de re-derivação do número e o encerramento do `AE-10` **já estão decididos**: o que falta é forma de card. Decisão nova de rota, escopo ou arquitetura **não se abre aqui** — matéria que exija uma volta como `blocked` razão `premissa`, nomeando-a.

**Arquivos-alvo:** - `docs/plans/P-0739-backlog-instrumento.md`

**Verificação:** 1. ``` pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0739-backlog-instrumento.md -Pattern '^### BKL-T1[012] ' | Measure-Object).Count" ``` → **3**: os três módulos existem como heading. **Medido antes: 0**. 2. ``` python .claude/tools/review_evidence.py --plano docs/plans/P-0739-backlog-instrumento.md --tarefa BKL-T10 --desde HEAD ``` idem para `BKL-T11` e `BKL-T12` → **exit 0** nos três: o parser que consome o card no despacho aceita os três. **Medido antes: exit 1 para `BKL-T10`**, contra **exit 0** para `BKL-T5` na mesma árvore — o par discrimina card ausente de card presente, e não a saúde do extrator. 3. ``` pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0739-backlog-instrumento.md -Pattern '^- \*\*Status:\*\* `cancelled`' | Measure-Object).Count" ``` → **5**: um por card absorvido, nem mais nem menos. **Medido antes: 0** (medido no ato do `ESC-1`, com esta forma já escrita no arquivo). A âncora `^- ` conta **linha de campo `Status` de card** e nada mais: a própria linha de comando deste item não casa, e menção em prosa também não — a forma anterior (`-SimpleMatch` sem âncora) media **1** por contar a si mesma (`AE-15`, achado secundário). 4. ``` pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0739-backlog-instrumento.md -Pattern '^- \*\*Status:\*\* `ready`' | Measure-Object).Count" ``` → **3**: só os três módulos ficam `ready`. **Medido antes: 5** — os cinco absorvidos, medidos no ato do `ESC-1` com esta forma já escrita no arquivo (a forma anterior media **6**, contando a si mesma). O par com o item 3 prova a **troca**, e não só a chegada dos novos: 5 `ready` + 0 `cancelled` **antes**, 3 `ready` + 5 `cancelled` **depois**. 5. ``` pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0739-backlog-instrumento.md -Pattern '\.claude/skills/proximo-passo/SKILL\.md','\.claude/skills/handover/SKILL\.md' | Measure-Object).Count" ``` → **6**, **invariante**: as seis ocorrências do caminho completo vivem no `## Contexto`, no corpo preservado da `BKL-T8` (dois `Arquivos-alvo`), no bullet de superfície morta deste card e na prosa do `AE-13` (duas) — medidas no ato do `ESC-1`, com esta forma já escrita no arquivo. Número maior significa alvo morto transcrito para card novo, que é o defeito que esta rodada existe para não cometer. O padrão exige o caminho **inteiro** (`.claude/…/SKILL.md`), e por isso a própria linha de comando deste item não casa — a forma anterior (`'skills/proximo-passo'` solto) media **7**, contando a si mesma (`AE-15`, achado secundário). **Medido antes: 6**. 6. ``` git diff --unified=0 -- docs/plans/P-0739-backlog-instrumento.md ``` → **dentro do corpo dos cinco cards absorvidos** (do heading `### BKL-T5` ao fim do `### BKL-T9`), a **única** remoção é a linha `Status` de cada um. Conferência contra a fonte: prova que o corpo dos cinco foi preservado verbatim, que é a condição de os três módulos poderem citá-los. **O diff contra `HEAD` traz também o reparo do consultor** (`DB-43`, `ESC-1`) nas seções `## 1`, `## 2` e `## 3` e neste card `BKL-T9a`, porque a janela não commita fora dos marcos de validação: essas linhas **não** são da entrega e não entram neste item — o recorte é a faixa dos cinco cards.

**Pronto quando:** os seis itens de `Verificação` saem com o número esperado, e o `git diff` do item 6 mostra remoção **apenas** nas cinco linhas `Status` dos cards absorvidos, na linha `**Ordem de execução:**` do cabeçalho e na linha do `AE-10` que passa a encerrado — nenhuma outra remoção **autorada nesta rodada** no arquivo, e nenhum outro arquivo tocado. As linhas do reparo `DB-43` já presentes na árvore de trabalho não são remoção desta rodada e não contam aqui.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` (2026-09-19, **2º despacho**) — desbloqueada pelo `ESC-1`: o consultor decidiu a rota **(b) generalizada** (`DB-43`), classificou o impedimento como **técnico/tático** e aplicou as emendas de `## 1`..`## 3` e do próprio card; o `check` cai de **309** para **27** achados e o corpus de **20** planos para **1**. O 1º despacho não consumiu retentativa (`A3b` não gasta): a tarefa chega com **0** gastas. Estado anterior, para registro: `blocked` razão `premissa` — o aceite herdado da `BKL-T6` era insatisfazível no escopo declarado, achado integral no `AE-15`, nenhum arquivo tocado pelo planejador (`G-EXECREADY` cumprido). Card autorado pelo `scrum-master` no ato da retomada, sob o item 3 da *Diretiva de execução do `P-0739`* (dono, 2026-09-19). Lacuna medida: o primeiro ato da retomada estava **decidido** (`AE-13` desta série) e **nomeado** na `Fila corrente` do diário, e mesmo assim não tinha card despachável — `review_evidence.py --tarefa BKL-T10` saía **exit 1** onde `--tarefa BKL-T5` saía **exit 0**, na mesma árvore. Registrada como `AE-14`. **Esta rodada é um card, e não uma seção `RP-<n>` em prosa como as sete anteriores:** o `_ID_HEADER_RE` de `.claude/tools/rdo.py:85` só aceita identificador da forma `<PREFIXO>-T<n>`, e `RP-8` sai **exit 1** no extrator de dossiê. O sufixo de letra segue a convenção que o próprio plano já usa para card inserido por rodada (`BKL-T2a`, `BKL-T3a`, `BKL-T3b`): numera depois do card que antecede, e executa antes dos três módulos.
- **Esforço:** high
- **Depende de:** nada. `BKL-T10`, `BKL-T11` e `BKL-T12` dependem desta.
- **Produto do módulo:** - **(a) Três cards de módulo** em `## 4. Tarefas`, nesta ordem e imediatamente **antes** do `### BKL-T5`: `BKL-T10` (absorve `BKL-T5` + `BKL-T6` — `drain`, o reparo de corpus da `DB-43` e a migração dos documentos vivos até `check` verde), `BKL-T11` (absorve `BKL-T7` + `BKL-T8` — o hook, o ponto de carga e as skills que passam a invocar o instrumento), `BKL-T12` (absorve `BKL-T9` sozinha — aferição do pickup e revisão do `README.md`, com veredito do dono). Cada um com cabeçalho na gramática de `GOVERNANCA.md` §3, `Status: ready`, `Esforço`, `Objetivo` **único**, `Depende de`, `Arquivos-alvo` em caminhos vivos, `Restrições` e bloco `Verificação` conforme `RUBRICA_DE_REVISAO.md` §8.1. - **(b) Os cinco cards absorvidos passam a `cancelled`**, razão *absorvido por `<ID do módulo>`*, com o corpo preservado **verbatim** e o bullet `- **Absorvida por:**` mantido. Nada se apaga: o corpo dos cinco é a fonte que os três módulos citam. - **(c) O `AE-10` marcado como encerrado** onde ele mora, pelo reparo `AE-47` **do `P-0740`** (a guarda de `transacionar_status` dissolveu a dependência de ordem com os marcadores `<!-- fila:gerada -->`), com o qualificador de plano na citação, como o `AE-13` exige. - **(d) A linha `**Ordem de execução:**` do cabeçalho** reescrita para a ordem viva — `BKL-T10` → `BKL-T11` → `BKL-T12` —, com os cards terminais nomeados entre parênteses, como a linha já faz hoje.
- **Restrições desta tarefa:** um único arquivo é tocado — `docs/plans/P-0739-backlog-instrumento.md`. Nenhum código, nenhum teste, nenhuma skill, nenhum doc de kit, nenhuma linha do `docs/DIARIO_DE_OBRAS.md` (o kanban é do `scrum-master`). O corpo dos cinco cards absorvidos **não se reescreve**: muda a linha `Status` deles e nada mais. Nenhuma seção de `## 1` a `## 3` (decisões, gramática, superfície) é alterada — se a transcrição exigir mexer em qualquer uma delas, é decisão nova: devolver `blocked` razão `premissa`. As emendas que o `AE-15` exigia **já estão aplicadas** nessas seções pelo consultor (`DB-43`, `ESC-1`): a transcrição as **cita**, e não as reescreve.

## Execução

**Consumo:** 66 tool uses, 177.2 k tokens, 1262.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: BKL-T10 acima do teto <=40 da classe implementacao (20 passos, 6 arquivos-alvo, 12 testes, dois temas); P-0737 permanece nos Arquivos-alvo do BKL-T10 so pela linha Status do cabecalho (DB-43); o apenso que a BKL-T8 previa em P-0737 ## 9 foi declarado fora de escopo no BKL-T11 por ser corpo de plano fechado.
laudo: BKL-T10 nao passa na rubrica de criacao de tarefa (##8 (ii)) por cruzar mais de um tema, e a particao que o gerou foi imposta pelo AE-13/ESC-1 e vedada a re-decisao pela BKL-T9a: decidir no planejamento se o BKL-T10 se desdobra antes do despacho ou se segue inteiro.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
