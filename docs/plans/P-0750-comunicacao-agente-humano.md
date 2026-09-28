# P-0750 — Comunicação agente↔humano: a mensagem ao dono se entende sozinha

**Data:** 2026-09-25 · **Origem:** tíquete `TK-38` (absorvido, `DCH-7`) e rodada de decisões do dono (§0) · **Status:** `done` · 2026-09-25 · **aceito pelo dono no fechamento**, verbatim: *"No que depender de
aceite, considerar aceito."* (6/6 tarefas `done`; validação em `docs/OPERACOES_AS_IS_P-0750.md`). Antes: Marco 1
com o aceite do plano pelo dono na sessão de planejamento · **Prefixo das tarefas no diário:** `CAH-T<n>` · **Prefixo das decisões:**
`DCH-<n>` · **Forma:** legado (arquivo único, id de 4 dígitos).
**Ordem de execução:** CAH-T1 → CAH-T2 → CAH-T3 → CAH-T4 → CAH-T5 → CAH-T4a
**Checagem de versão do kit:** modo hub, congelada em `0.0.0`.

**Pronto quando:** existe uma regra única da mensagem ao dono na doutrina, com eco no regulamento
global; o glossário diz o que cada família de sigla nomeia; existe a tabela de falhas de
comunicação com as falhas já medidas; existe a skill do procedimento; e nenhum texto do kit manda
mais citar identificador sozinho ao dono.

## 0. O problema, verbatim

Pedido (dono, 2026-09-25): *"faça a tarefa de cmunicação agente humano"*.

Regra de ouro do tíquete (dono, 2026-08-13): *"toda comunicação que demandar que o humano leia um
documento extra, ou crie um novo prompt, é comunicação ineficiente, e deve ser registrada como lição
aprendida para melhoria da skill de comunicação"*.

Ato do dono sobre o painel (2026-09-24): *"E uma agregação dessa função de stream out é fazer
replace do código da tarefa por uma descrição resumida dela. Só referenciando siglas não
efetivamente agrega para a comunicação homem máquina."* — e, no mesmo ato: *"minha única crítica é
o termo 'evidência mecânica', que é vago."*

Rodada de decisões (dono, 2026-09-25):
- Onde mora a regra: *"Doutrina + skill"*.
- Como a sigla aparece: *"Padronizar com o que já é feito quando o fluxo de informações é
  apresentado no powershell"*.
- Idioma: *"Regra, sem tradução"*.
- Registro das falhas: *"TSV próprio"*.

## 1. Modelo conceitual

**Estado do modelo:** versão 1 · 2026-09-25 · autor: planejador · 5 operações · 9 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem | lastro na §0 | tipo |
|---|---|---|---|---|---|---|
| kit | os textos que ensinam os agentes a falar com o dono — doutrina, regulamento global, porta de entrada, skills e agentes — e a tabela onde se anotam as falhas | regra da mensagem ao dono, nome das coisas na mensagem, glossário das siglas, registro de falha, procedimento da mensagem, textos que mandam citar sigla | Quem implementa recebe esses textos. O que esta entrega não toca continua valendo como hoje. | OP-1 | *"faça a tarefa de cmunicação agente humano"* | escopo |
| painel do gerente | as frases que o dono lê na tela durante a execução, geradas por função | forma do nome | Quem implementa não o toca. É o padrão copiado: o título entre aspas no lugar da sigla. | externo | *"Padronizar com o que já é feito quando o fluxo de informações é apresentado no powershell"* | medição |
| falhas medidas | as vezes em que o dono teve de perguntar o que uma sigla ou um termo queria dizer | onde constam | Quem implementa as transcreve, sem reinterpretar. | externo | *"deve ser registrada como lição aprendida"* | medição |
| próxima mensagem ao dono | o primeiro relatório ou resposta que um agente escrever ao dono depois desta entrega | como nomeia as coisas | Quem implementa não a escreve. Ela mostra se a regra pegou. | externo | *"Só referenciando siglas não efetivamente agrega para a comunicação homem máquina"* | medição |

### 1.2 Fluxo de operações

- **OP-1** — O redator da doutrina escreve, ao lado da regra do artefato de humano mínimo, a regra da mensagem ao dono: o dono decide sem abrir outro documento nem perguntar de volta, e nenhuma sigla chega sozinha, vai o título entre aspas como no painel; o regulamento global ganha o eco curto dessa regra.
  - `precisa de: painel do gerente` · `altera: kit.regra da mensagem ao dono, kit.nome das coisas na mensagem` · `tarefas: CAH-T1` · `lastro: Doutrina + skill; Padronizar com o que já é feito quando o fluxo de informações é apresentado no powershell`
- **OP-2** — O mantenedor da porta de entrada escreve no glossário o que cada família de sigla do kit nomeia, e diz com franqueza que as letras depois do D das decisões não abreviam palavra.
  - `precisa de: kit` · `altera: kit.glossário das siglas` · `tarefas: CAH-T2` · `lastro: Só referenciando siglas não efetivamente agrega para a comunicação homem máquina`
- **OP-3** — O mantenedor do registro cria a tabela de falhas de comunicação e nela transcreve as três falhas já medidas.
  - `precisa de: kit, falhas medidas` · `altera: kit.registro de falha` · `tarefas: CAH-T3` · `lastro: TSV próprio; deve ser registrada como lição aprendida`
- **OP-4** — O autor de skill cria a skill da mensagem ao dono: a checagem antes de enviar, onde achar o título de cada sigla, o formato do pedido de decisão e o registro da falha; e a inscreve na anatomia do kit.
  - `precisa de: kit` · `altera: kit.procedimento da mensagem` · `tarefas: CAH-T4, CAH-T4a` · `lastro: Doutrina + skill; melhoria da skill de comunicação`
- **OP-5** — O mantenedor das superfícies troca, nos textos que hoje mandam citar identificador ao dono, a sigla sozinha pelo título entre aspas, e marca a fronteira do documento publicado.
  - `precisa de: kit, próxima mensagem ao dono` · `altera: kit.textos que mandam citar sigla` · `tarefas: CAH-T5` · `lastro: fazer replace do código da tarefa por uma descrição resumida dela`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final | lastro na §0 |
|---|---|---|---|
| kit.regra da mensagem ao dono | não existe; a regra de ouro vive só na prosa de um tíquete | uma regra única na doutrina, ao lado da regra do texto mínimo, com eco curto no regulamento global | *"Doutrina + skill"* |
| kit.nome das coisas na mensagem | a sigla vai crua; só o painel troca a sigla pelo título | em toda mensagem ao dono o título entre aspas substitui a sigla; a sigla só acompanha quando o dono precisa digitá-la | *"Padronizar com o que já é feito quando o fluxo de informações é apresentado no powershell"* |
| kit.glossário das siglas | três famílias definidas; as letras das decisões nunca explicadas | todas as famílias do kit com o que nomeiam; as letras das decisões declaradas como sem expansão | *"Só referenciando siglas não efetivamente agrega"* |
| kit.registro de falha | não existe; o portador previsto foi cancelado | tabela de máquina de uma linha por falha, gravada por quem recebeu a pergunta | *"TSV próprio"* |
| kit.procedimento da mensagem | não existe | skill com checagem, busca do título, pedido de decisão e registro de falha | *"melhoria da skill de comunicação"* |
| kit.textos que mandam citar sigla | o relatório de janela manda citar a regra pelo identificador; a rodada de decisões não fala de sigla | os dois mandam o título entre aspas; o documento publicado aponta para a regra | *"fazer replace do código da tarefa por uma descrição resumida dela"* |
| painel do gerente.forma do nome | título entre aspas no lugar da sigla | o mesmo. Nenhuma operação o altera: é o padrão copiado | *"o que já é feito quando o fluxo de informações é apresentado no powershell"* |
| falhas medidas.onde constam | espalhadas em prosa no diário e num plano | as mesmas, agora também copiadas na tabela. Nenhuma operação as altera | *"deve ser registrada como lição aprendida"* |
| próxima mensagem ao dono.como nomeia as coisas | pela sigla crua | pelo título entre aspas. Nenhuma operação a escreve: a diferença prova que a regra pegou | *"Só referenciando siglas não efetivamente agrega"* |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 1 | 2026-09-25 | vigente | planejador — rota escolhida pelo dono: planejamento em sessão, sem o ciclo planejador–modelador |

## 2. Fatos estabelecidos

Fonte: levantamento da sessão de planejamento, 2026-09-25 (três varreduras somente-leitura).

- **F-1** O glossário (`README.md:36-181`) define só `P-NNNN`, `TK-<seq>` e `DR-`/`DP-`
  (`README.md:178-181`, "decision record"); as letras de `DR`/`DP` não se expandem em lugar
  nenhum. Há ~25 famílias de prefixo de decisão, locais a cada plano, com colisão (`DM-`, `DC-`,
  `D-`, `M-`, `C-` nomeiam coisas diferentes em planos diferentes). `RDO` nunca se expande.
- **F-2** O painel do gerente já troca a sigla pelo título entre aspas: skill `scrum-master`, seção
  *Repertório de mensagens ao gerente* (`.claude/skills/scrum-master/SKILL.md:314-323`), invariante
  `I-12` do `P-0748`.
- **F-3** O relatório de encerramento de janela manda citar a regra que encerrou a janela "pelo
  identificador" (`.claude/skills/scrum-master/SKILL.md:292`) e cada tarefa "com identificador"
  (`:293`) — causa direta da falha de 2026-09-19.
- **F-4** Regra que precisa valer sem ninguém invocar skill não mora em skill (`GOVERNANCA.md:257`).
- **F-5** O `P-0749`, card `SAN-T5` (`ready`, não executado), grava em `GOVERNANCA.md` §4.2, logo
  depois do bullet *Fechamento enxuto*, o bullet *Artefato de humano mínimo*, que termina na linha
  `  são aplicações desta regra.` — hoje sem ocorrência em nenhum `.md` fora do `P-0749`.
- **F-6** `.claude/checks/check-readme.ps1` exige paridade entre `.claude/skills/*/SKILL.md` e a
  tabela *Skills* da seção *Anatomia do kit* do `README.md` (tabela em `README.md:837-849`);
  `.claude/README.md` é gerado por `.claude/checks/kit_check.ps1 -Mode generate` e conferido por
  `-Mode check-drift`. Skills hoje: 11. O mesmo script confere o numeral por extenso da frase de
  contagem da seção (`O kit são dez agentes, onze skills, …`) contra o disco (`AE-6`).
- **F-7** O regulamento global tem residência em `.claude/global/CLAUDE.md` (8 regras, 166 linhas)
  e chega a `~/.claude/CLAUDE.md` por `materializar.py apply --alvo usuario`, ato do dono (`TK-68`).
- **F-8** Falhas medidas: (1) 2026-08-13, handover da `EXA-T25` citou `DP-F`, `DP-I`, `DP-J`,
  `DP-L` sem expansão, custou 1 prompt e o dono inferiu "Decisão Pendente", errado
  (`docs/DIARIO_DE_OBRAS.md`, `## TK-38`); (2) 2026-09-19, relatório de janela do `P-0740`, o dono
  pediu glossário e citou `A10` e `B6`, que não existem (mesma seção); (3) 2026-09-24, termo
  "evidência mecânica" vago no relatório de janela do `P-0748` (`DTG-29`,
  `docs/plans/P-0748-tela-do-gerente.md:493`).
- **F-9** Referência de 2026-09-24: `python -m pytest tests -q` → `313 passed` (`P-0749` F-12).

## 3. Decisões

| id | decisão | razão |
|---|---|---|
| DCH-1 | A regra mora em `GOVERNANCA.md` §4.2, bullet novo *Mensagem legível ao dono*, logo depois de *Artefato de humano mínimo*; `.claude/global/CLAUDE.md` ganha a Regra 9, eco curto e autossuficiente (projeto fora do kit não tem `GOVERNANCA.md`); a skill `mensagem-ao-dono` guarda o procedimento | dono, 2026-09-25 (*"Doutrina + skill"*); F-4 |
| DCH-2 | Na mensagem ao dono o objeto vai pelo título entre aspas duplas, como no painel; a sigla só acompanha, entre parênteses, quando o dono precisa digitá-la para agir; sigla sem título achado vai com uma frase que diga o que ela nomeia | dono, 2026-09-25 (*"Padronizar com o que já é feito…"*); F-2. A exceção dos parênteses é derivação do planejador: o dono comanda por id (*"execute TK-38"*) |
| DCH-3 | A glosa se escreve no idioma da conversa; nenhuma tabela traduzida | dono, 2026-09-25 (*"Regra, sem tradução"*) |
| DCH-4 | Falha de comunicação vira linha em `docs/FALHAS_COMUNICACAO.tsv`, append-only, gravada por quem recebeu a pergunta, antes de responder; colunas `data`, `superficie`, `o_que_faltou`, `custo_prompts`, `correcao`, `fonte` | dono, 2026-09-25 (*"TSV próprio"*); o portador anterior (`TK-32`) foi cancelado |
| DCH-5 | O item (c) do tíquete se cumpre no glossário do `README.md`, só com as famílias do kit; a resposta a "o que `DP-` significa" é o fato: as letras depois do `D` não abreviam palavra e o número vale só dentro do plano | F-1; com DCH-2 a expansão de letra deixa de ser o que o dono lê |
| DCH-6 | `RDO` se glosa como registro canônico da tarefa, e a sigla como vinda do *Relatório Diário de Obra* da construção civil, de onde o kit toma a metáfora do diário de obras | F-1; o dono corrige no aceite se a origem for outra |
| DCH-7 | O `TK-38` é absorvido por este plano: no registro, `backlog.py status TK-38 cancelled --nota "absorvido pelo P-0750"` | forma usada no `P-0746` (`docs/DIARIO_DE_OBRAS.md:3143`) |
| DCH-8 | `CAH-T1` depende de `SAN-T5`: a regra irmã tem de existir antes, e a âncora de inserção é a última linha dela (F-5). A prioridade relativa entre os dois planos é do dono | F-5 |
| DCH-9 | Superfícies alteradas: só as que mandam citar id ao dono (relatório de janela da `scrum-master`, rodada de decisões do `pantonic-planner`) e a fronteira da `redacao-doc`. A superfície agente↔agente (`passagem-de-bastao`, dossiê, laudo, retorno do executor) não muda | fronteira `TK-36` × `TK-38` (`P-0734` `:4379-4385`) |
| DCH-10 | Nenhum instrumento novo: o título se acha por `backlog.py show` e por busca de texto. Um resolvedor sigla→título por função fica **registrado e não agido** | custo; o painel já tem o seu (`localizar_card` em `.claude/tools/progresso_hook.py`) |

## 4. Invariantes de execução

- **I-1** Os artefatos continuam usando a sigla abreviada; só o texto dirigido ao dono muda.
- **I-2** O texto da regra entra uma vez, em `GOVERNANCA.md`; skill, agente e `README.md` recebem
  ponteiro. A Regra 9 do regulamento global é o único eco, e é curta.
- **I-3** Nenhuma superfície agente↔agente recebe requisito de comunicação humana (DCH-9).
- **I-4** Nenhuma tarefa aplica o regulamento global em `~/.claude/` — só a residência
  `.claude/global/CLAUDE.md` muda; o `apply` é ato do dono (F-7).

## 5. Tarefas

### CAH-T1 — A regra da mensagem legível ao dono, na doutrina e no regulamento global [Sonnet · esforço low · classe redacao]
- **Status:** `done` · 2026-09-25
- **Objetivo:** O redator da doutrina escreve, ao lado da regra do artefato de humano mínimo, a regra da mensagem ao dono: o dono decide sem abrir outro documento nem perguntar de volta, e nenhuma sigla chega sozinha, vai o título entre aspas como no painel; o regulamento global ganha o eco curto dessa regra.
- **Fundamento:** DCH-1, DCH-2, DCH-3, DCH-4, DCH-8; F-2, F-4, F-5, F-7; I-2, I-4.
- **Depende de:** `SAN-T5`
- **Operação do modelo:** `OP-1`
  - OP-1: O redator da doutrina escreve, ao lado da regra do artefato de humano mínimo, a regra da mensagem ao dono: o dono decide sem abrir outro documento nem perguntar de volta, e nenhuma sigla chega sozinha, vai o título entre aspas como no painel; o regulamento global ganha o eco curto dessa regra.
  - precisa de: painel do gerente — Quem implementa não o toca. É o padrão copiado: o título entre aspas no lugar da sigla.
- **Camada e fronteira:** doutrina do kit (`GOVERNANCA.md` §4.2) e residência do regulamento global; nenhum código.
- **Arquivos-alvo:**
  - `GOVERNANCA.md`
  - `.claude/global/CLAUDE.md`
- **Texto novo, literal** (antigo → novo; `↵` é quebra de linha):

  ```text
  [H1] GOVERNANCA.md
    são aplicações desta regra.
  →   são aplicações desta regra.↵
  - **Mensagem legível ao dono** — toda mensagem ao dono (conversa, handover, relatório de janela,↵
    rodada de decisões) se entende sozinha: (a) o que o dono precisa para decidir ou validar vem no↵
    corpo — caminho de arquivo é complemento, nunca substituto; (b) nenhuma sigla chega sozinha: o↵
    objeto vai pelo título entre aspas duplas, como no painel do gerente (skill `scrum-master`,↵
    *Repertório de mensagens ao gerente*), e a sigla só o acompanha, entre parênteses, quando o dono↵
    precisa digitá-la para agir; sem título achado, a sigla vai com uma frase que diga o que ela↵
    nomeia; (c) a glosa se escreve no idioma da conversa. Pergunta do dono sobre o que algo significa↵
    ou onde está é falha medida: quem a recebeu apensa uma linha a `docs/FALHAS_COMUNICACAO.tsv`↵
    antes de responder. Procedimento: skill `mensagem-ao-dono`. A superfície agente↔agente (dossiê,↵
    retorno do executor, laudo, `passagem-de-bastao`) fica fora: ali a sigla crua é o contrato.

  [H2] .claude/global/CLAUDE.md — apensar ao fim do arquivo, depois da última linha da Regra 8
    codar a alternativa.
  →   codar a alternativa.↵
  ↵
  ## Regra 9 — A mensagem ao dono se entende sozinha↵
  ↵
  **Motivo:** o dono não participou do ato que criou uma sigla. Mensagem que o obriga a abrir outro↵
  documento ou a gastar um prompt perguntando o que algo significa é falha medida — já custou↵
  prompts ao dono e o levou a inventar siglas que não existem.↵
  ↵
  **Como aplicar:**↵
  - O que o dono precisa para decidir ou validar vem no corpo da mensagem; caminho de arquivo é↵
    complemento, nunca substituto.↵
  - Nenhuma sigla chega sozinha: o objeto vai pelo título entre aspas duplas; a sigla só o acompanha,↵
    entre parênteses, quando o dono precisa digitá-la para agir.↵
  - A glosa se escreve no idioma da conversa.↵
  - Em projeto Pantonic*, a regra mora em `GOVERNANCA.md` §4.2 (*Mensagem legível ao dono*), o↵
    procedimento na skill `mensagem-ao-dono`, e a falha medida vira linha em↵
    `docs/FALHAS_COMUNICACAO.tsv`.
  ```
- **Passos:**
  1. Rodar a Verificação 1 e conferir os valores "antes".
  2. Aplicar `H1` e `H2` com `Edit`.
  3. Rodar a Verificação 1 a 3.
- **Restrições desta tarefa:** I-2 — o texto da regra entra uma vez em `GOVERNANCA.md`; I-4 — não rodar `materializar.py apply`.
- **Não fazer:** não criar item novo em `GOVERNANCA.md` §7; não tocar o bullet *Artefato de humano mínimo*; não renumerar as regras 1–8 do regulamento global.
- **Contingências:**
  1. se `  são aplicações desta regra.` não aparecer exatamente uma vez em `GOVERNANCA.md` (o `SAN-T5` não rodou ou mudou o texto) → parar e sinalizar `blocked` razão `dependencia`.
  2. se `  codar a alternativa.` não for a última linha não vazia de `.claude/global/CLAUDE.md` → parar e sinalizar `blocked` razão `premissa`.
- **Testes:** nenhum novo (redação); a suíte inteira roda como TR.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command '(@(foreach ($p in @(@("GOVERNANCA.md","Mensagem legível ao dono"),@(".claude/global/CLAUDE.md","## Regra 9 — ")))) { @(Select-String -LiteralPath $p[0] -SimpleMatch -Pattern $p[1]).Count })) -join " / "'
     ```
     → **1 / 1**. **Medido antes: 0 / 0**.
  2. ```
     pwsh -NoProfile -Command '"total=" + @(Select-String -Path "GOVERNANCA.md","README.md",".claude/agents/*.md",".claude/skills/*/SKILL.md" -SimpleMatch -Pattern "a sigla só o acompanha, entre parênteses").Count'
     ```
     → **total=1** (a linha da regra em `GOVERNANCA.md`). **Medido antes: total=0**.
  3. ```
     python -m pytest tests -q
     ```
     → **nenhuma falha**, total igual ao da véspera. **Medido antes: 313 passed** (F-9).
- **Pronto quando:**
  - kit.regra da mensagem ao dono — uma regra única na doutrina, ao lado da regra do texto mínimo, com eco curto no regulamento global — Verificação 1, 2
  - kit.nome das coisas na mensagem — em toda mensagem ao dono o título entre aspas substitui a sigla; a sigla só acompanha quando o dono precisa digitá-la — Verificação 1
- **Fora do escopo desta tarefa:** a skill (`CAH-T4`), a tabela de falhas (`CAH-T3`), o `apply` em `~/.claude/` (dono).

### CAH-T2 — O glossário diz o que cada família de sigla nomeia [Sonnet · esforço low · classe redacao]
- **Status:** `done` · 2026-09-25
- **Objetivo:** O mantenedor da porta de entrada escreve no glossário o que cada família de sigla do kit nomeia, e diz com franqueza que as letras depois do D das decisões não abreviam palavra.
- **Fundamento:** DCH-5, DCH-6; F-1; I-1, I-2.
- **Depende de:** `CAH-T1`
- **Operação do modelo:** `OP-2`
  - OP-2: O mantenedor da porta de entrada escreve no glossário o que cada família de sigla do kit nomeia, e diz com franqueza que as letras depois do D das decisões não abreviam palavra.
  - precisa de: kit — Quem implementa recebe esses textos. O que esta entrega não toca continua valendo como hoje.
- **Camada e fronteira:** porta de entrada (`README.md`, seção do glossário, parte *Metadados*); documento publicado — segue a skill `redacao-doc` (nenhum id de plano ou de processo no texto novo).
- **Arquivos-alvo:**
  - `README.md`
- **Texto novo, literal** (substitui o bullet inteiro das linhas 178–181; `↵` é quebra de linha):

  ```text
  [G1] README.md
  - **Decisão `DR-` / `DP-`** — um *decision record* datado, ratificado pelo dono, que registra uma↵
    mudança comportamental intencional e o motivo dela; bifurcar rota exige um aprovado **antes** de a↵
    alternativa ser codada. Onde a regra mora: `GOVERNANCA.md` §3 (papéis) e §4.2 (registro)↵
    (§9 e §14 desta página).
  → - **Decisão `DR-` / `DP-` / `D<letras>-`** — um *decision record* datado, ratificado pelo dono, que↵
    registra uma mudança comportamental intencional e o motivo dela; bifurcar rota exige um aprovado↵
    **antes** de a alternativa ser codada. As letras depois do `D` não abreviam palavra: `DR-` e `DP-`↵
    são as formas mais antigas, e cada plano mais novo usa `D` seguido de letras próprias. O número só↵
    vale dentro do plano que o define, e o mesmo prefixo pode nomear decisões diferentes em planos↵
    diferentes. Onde a regra mora: `GOVERNANCA.md` §3 (papéis) e §4.2 (registro) (§9 e §14 desta↵
    página).↵
  - **Identificadores de trabalho** — as siglas com que os artefatos apontam uns para os outros. Em↵
    mensagem ao dono nenhuma chega sozinha: vai o título entre aspas. Onde a regra mora:↵
    `GOVERNANCA.md` §4.2 (*Mensagem legível ao dono*).↵
    - `<PFX>-T<n>` — tarefa de plano; `<PFX>` são letras escolhidas pelo plano e declaradas no↵
      cabeçalho dele.↵
    - `OP-<n>` — operação do modelo conceitual do plano.↵
    - `F-<n>`, `I-<n>`, `Q-<n>`, `R-<n>` — fato estabelecido, invariante de execução, questão ao↵
      dono e risco, numerados dentro do plano.↵
    - `AE-<n>`, `ESC-<n>`, `RP-<n>` — achado da execução, escalonamento e rodada de replanejamento,↵
      numerados dentro do plano.↵
    - `RDO` — o registro canônico de uma tarefa fechada, um arquivo por tarefa em `docs/RDO/`; a↵
      sigla vem do *Relatório Diário de Obra* da construção civil, de onde o kit toma a metáfora do↵
      diário de obras.↵
    - `TF-*` e `TR-*` — teste funcional e teste de regressão.↵
    - `G-<NOME>` — guardrail, item da lista de `GOVERNANCA.md` §7.↵
    - `A<n>` e `B<n>` — regras de roteamento do loop de execução: o bloco A decide o que fazer com a↵
      tarefa devolvida; o bloco B, se a janela continua ou encerra (skill `scrum-master`).↵
    - `M-<n>` — forma de frase do painel do gerente.
  ```
- **Passos:**
  1. Rodar a Verificação 1 e conferir os valores "antes".
  2. Aplicar `G1` com `Edit` (o texto antigo são as quatro linhas do bullet, exatas).
  3. Rodar a Verificação 1 a 3.
- **Restrições desta tarefa:** I-2 — o bullet novo aponta para a regra, não a reescreve.
- **Não fazer:** não renumerar seção do `README.md`; não citar id de plano, de tarefa ou de decisão concreta no texto novo; não mexer nos demais bullets do glossário.
- **Contingências:**
  1. se o texto antigo de `G1` não aparecer exatamente uma vez → parar e sinalizar `blocked` razão `dependencia`, devolvendo o trecho encontrado.
- **Testes:** nenhum novo (redação); a suíte inteira roda como TR.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command '(@(foreach ($t in "**Identificadores de trabalho**","As letras depois do ``D`` não abreviam palavra","Relatório Diário de Obra") { @(Select-String -LiteralPath README.md -SimpleMatch -Pattern $t).Count })) -join " / "'
     ```
     → **1 / 1 / 1**. **Medido antes: 0 / 0 / 0**.
  2. ```
     pwsh -NoProfile -File .claude/checks/check-readme.ps1
     ```
     → **exit 0**.
  3. ```
     python -m pytest tests -q
     ```
     → **nenhuma falha**, total igual ao da véspera.
- **Pronto quando:**
  - kit.glossário das siglas — todas as famílias do kit com o que nomeiam; as letras das decisões declaradas como sem expansão — Verificação 1, 2
- **Fora do escopo desta tarefa:** a linha da skill nova na tabela *Skills* (`CAH-T4`).

### CAH-T3 — A tabela de falhas de comunicação, com as falhas já medidas [Sonnet · esforço low · classe mecanica]
- **Status:** `done` · 2026-09-25
- **Objetivo:** O mantenedor do registro cria a tabela de falhas de comunicação e nela transcreve as três falhas já medidas.
- **Fundamento:** DCH-4; F-8.
- **Depende de:** `CAH-T1`
- **Operação do modelo:** `OP-3`
  - OP-3: O mantenedor do registro cria a tabela de falhas de comunicação e nela transcreve as três falhas já medidas.
  - precisa de: kit — Quem implementa recebe esses textos. O que esta entrega não toca continua valendo como hoje.
  - precisa de: falhas medidas — Quem implementa as transcreve, sem reinterpretar.
- **Camada e fronteira:** artefato de máquina do projeto, em `docs/`, ao lado de `docs/telemetria.tsv`.
- **Arquivos-alvo:**
  - `docs/FALHAS_COMUNICACAO.tsv` (novo)
- **Conteúdo literal** (UTF-8, fim de linha LF, 4 linhas; `⇥` é **um caractere TAB**, U+0009 — nunca espaço):

  ```text
  data⇥superficie⇥o_que_faltou⇥custo_prompts⇥correcao⇥fonte
  2026-08-13⇥handover⇥siglas DP-F, DP-I, DP-J e DP-L sem expansão; o dono inferiu "Decisão Pendente", errado⇥1⇥regra Mensagem legível ao dono⇥docs/DIARIO_DE_OBRAS.md ## TK-38
  2026-09-19⇥relatório de janela⇥regras de roteamento citadas pelo identificador; o dono pediu glossário e citou A10 e B6, que não existem⇥1⇥relatório de janela passa a citar a regra pela condição (CAH-T5)⇥docs/DIARIO_DE_OBRAS.md ## TK-38
  2026-09-24⇥relatório de janela⇥termo "evidência mecânica" vago⇥0⇥-⇥docs/plans/P-0748-tela-do-gerente.md:493
  ```
- **Passos:**
  1. Confirmar que `docs/FALHAS_COMUNICACAO.tsv` não existe.
  2. Gravar o arquivo com `Write`, trocando cada `⇥` por TAB.
  3. Rodar a Verificação 1.
- **Restrições desta tarefa:** nenhuma célula contém TAB ou quebra de linha; o texto das falhas é transcrito, não reescrito.
- **Não fazer:** não criar instrumento de gravação; não tocar `docs/telemetria.tsv`.
- **Contingências:**
  1. se o arquivo já existir → parar e sinalizar `blocked` razão `premissa`.
- **Testes:** nenhum novo; a Verificação 1 confere a forma.
- **Verificação:**
  1. ```
     python -c "import csv;r=list(csv.reader(open('docs/FALHAS_COMUNICACAO.tsv',encoding='utf-8',newline=''),delimiter='\t'));print(len(r),sorted({len(x) for x in r}),r[0][0],r[3][0])"
     ```
     → **`4 [6] data 2026-09-24`**. **Medido antes: arquivo inexistente**.
- **Pronto quando:**
  - kit.registro de falha — tabela de máquina de uma linha por falha, gravada por quem recebeu a pergunta — Verificação 1
- **Fora do escopo desta tarefa:** o procedimento de quem grava a linha (`CAH-T4`, na skill).

### CAH-T4 — A skill da mensagem ao dono [Sonnet · esforço medium · classe redacao]
- **Status:** `done` · 2026-09-25
- **Objetivo:** O autor de skill cria a skill da mensagem ao dono: a checagem antes de enviar, onde achar o título de cada sigla, o formato do pedido de decisão e o registro da falha; e a inscreve na anatomia do kit.
- **Fundamento:** DCH-1, DCH-2, DCH-4, DCH-9, DCH-10; F-2, F-6; I-2, I-3.
- **Depende de:** `CAH-T1`, `CAH-T2`, `CAH-T3`
- **Operação do modelo:** `OP-4`
  - OP-4: O autor de skill cria a skill da mensagem ao dono: a checagem antes de enviar, onde achar o título de cada sigla, o formato do pedido de decisão e o registro da falha; e a inscreve na anatomia do kit.
  - precisa de: kit — Quem implementa recebe esses textos. O que esta entrega não toca continua valendo como hoje.
- **Camada e fronteira:** skill do kit (`.claude/skills/`), propagada a derivados pelo `sync-kit.ps1` fora deste plano; a regra não se copia, só se aponta (I-2).
- **Arquivos-alvo:**
  - `.claude/skills/mensagem-ao-dono/SKILL.md` (novo)
  - `README.md` (tabela *Skills* e frase de contagem da seção *Anatomia do kit* — `K1`, `K2`)
  - `.claude/README.md` (regenerado, não editado à mão)
- **Conteúdo literal de `.claude/skills/mensagem-ao-dono/SKILL.md`:**

  ````text
  ---
  name: mensagem-ao-dono
  description: Checagem de toda mensagem escrita para o dono humano — conversa, handover, relatório de janela, rodada de decisões. Troca a sigla sozinha pelo título entre aspas, traz para o corpo o que o dono precisa para decidir e registra a falha quando o dono teve de perguntar. Usar antes de enviar ao dono mensagem que cite sigla do kit ou aponte arquivo, e ao receber dele pergunta de esclarecimento.
  ---

  # mensagem-ao-dono — a mensagem se entende sozinha

  A regra mora em `GOVERNANCA.md` §4.2 (*Mensagem legível ao dono*); esta skill é o procedimento.

  ## Gatilho

  1. Antes de enviar ao dono mensagem que cite sigla do kit (tarefa, tíquete, plano, decisão,
     achado, regra de roteamento, guardrail) ou aponte arquivo.
  2. Ao receber do dono pergunta do tipo "o que é", "o que significa" ou "onde está" sobre algo que
     um agente escreveu — é falha medida (§4).

  Fora do alcance: a superfície agente↔agente (dossiê, retorno do executor, laudo,
  `passagem-de-bastao`), onde a sigla crua é o contrato; documento publicado (`redacao-doc`);
  documento de encerramento de plano (`entrega-de-encerramento`), que já define todo termo no texto.

  ## 1. Checagem antes de enviar

  - [ ] Toda sigla foi trocada pelo título entre aspas duplas (§2). A sigla só acompanha, entre
        parênteses, quando o dono precisa digitá-la para agir.
  - [ ] O dono decide ou valida sem abrir arquivo: o fato que sustenta cada pedido está no corpo, e
        o caminho é complemento.
  - [ ] Termo interno (laudo, evidência, janela, marco) tem glosa curta na primeira ocorrência.
  - [ ] Pedido de decisão no formato do §3.
  - [ ] Escrita no idioma em que o dono conversa.

  Exemplo — antes: `Próximo: TK-38.` · depois: `Próximo: o tíquete "Comunicação entre agente e
  humano — skill própria e requisitos mínimos" (TK-38).` (a sigla fica porque o dono a digita para
  mandar executar).

  ## 2. Onde achar o título

  | sigla | onde está o título | como buscar |
  |---|---|---|
  | tarefa `<PFX>-T<n>`, tíquete `TK-<n>`, plano `P-NNNN` | o cabeçalho do item | `python .claude/tools/backlog.py show <ID>` — o título é o texto depois de ` — ` na primeira linha |
  | decisão, fato, invariante, achado (`D…-<n>`, `F-<n>`, `I-<n>`, `AE-<n>`) | a linha que a define no plano de origem | busca de texto por `**<ID>**` ou `\| <ID> \|` no plano; o título é a primeira oração |
  | regra de roteamento `A<n>` ou `B<n>` | a coluna *condição* das tabelas dos blocos A e B da skill `scrum-master` | a condição, em palavras |
  | guardrail `G-<NOME>` | a lista de `GOVERNANCA.md` §7 | o nome da regra |
  | família de sigla | o glossário do `README.md`, bullet *Identificadores de trabalho* | — |

  Sem título achado, a sigla vai com uma frase que diga o que ela nomeia — nunca sozinha.

  ## 3. Pedido de decisão

  Uma mensagem, todas as questões juntas. Cada questão traz: o fato medido que a originou, as
  opções com o que cada uma implica, o que fica bloqueado sem resposta, a recomendação com o motivo
  e, quando existir, a opção "registrar e não agir". É o mesmo formato do relatório de encerramento
  da skill `scrum-master` e da rodada de decisões do `pantonic-planner`; esta seção não o redefine.

  ## 4. Registro de falha

  O dono perguntou o que algo significa, onde algo está, ou teve de abrir arquivo para decidir:
  quem recebeu a pergunta apensa **uma** linha a `docs/FALHAS_COMUNICACAO.tsv` antes de responder,
  sem reescrever linha anterior. Colunas separadas por TAB:

  | coluna | conteúdo |
  |---|---|
  | `data` | `AAAA-MM-DD` |
  | `superficie` | conversa, handover, relatório de janela, rodada de decisões, painel ou documento |
  | `o_que_faltou` | a sigla ou o termo sem glosa, ou o dado que só estava fora da mensagem |
  | `custo_prompts` | prompts do dono gastos no esclarecimento |
  | `correcao` | o que muda na regra ou nesta skill para não repetir, ou `-` |
  | `fonte` | caminho do registro do caso, ou `-` |

  A tabela se lê em conjunto na revisão da doutrina (`GOVERNANCA.md` §7.1); uma linha isolada não
  muda esta skill.
  ````
- **Texto novo, literal, no `README.md`** (`↵` é quebra de linha):

  ```text
  [K1] README.md — depois da linha da skill redacao-doc na tabela Skills
  | `redacao-doc` | Autoria, reescrita ou revisão de documento publicado: proíbe narrativa de proveniência, citação de interlocutor e ID de processo no corpo. |
  → | `redacao-doc` | Autoria, reescrita ou revisão de documento publicado: proíbe narrativa de proveniência, citação de interlocutor e ID de processo no corpo. |↵
  | `mensagem-ao-dono` | Antes de enviar ao dono mensagem que cite sigla do kit ou aponte arquivo, e ao receber dele pergunta de esclarecimento: título entre aspas no lugar da sigla, o necessário para decidir no corpo, e a falha registrada em `docs/FALHAS_COMUNICACAO.tsv`. |

  [K2] README.md — frase de contagem da seção Anatomia do kit (lida pelo check-readme.ps1; AE-6)
  O kit são dez agentes, onze skills, quatro verificadores executáveis e a declaração de projeções,
  → O kit são dez agentes, doze skills, quatro verificadores executáveis e a declaração de projeções,
  ```
- **Passos:**
  1. Rodar a Verificação 1 e conferir os valores "antes".
  2. Criar `.claude/skills/mensagem-ao-dono/SKILL.md` com `Write`, conteúdo literal acima.
  3. Aplicar `K1` e `K2` com `Edit`.
  4. Rodar `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` para regenerar `.claude/README.md`.
  5. Rodar a Verificação 1 a 4.
- **Restrições desta tarefa:** I-2 — a skill aponta para a regra, não a reescreve; I-3 — nada na skill impõe requisito à superfície agente↔agente.
- **Não fazer:** não editar `.claude/README.md` à mão; não tocar `passagem-de-bastao`, `scrum-master` nem `pantonic-planner` (`CAH-T5`); não criar script; não rodar `sync-kit.ps1`.
- **Contingências:**
  1. se o texto antigo de `K1` não aparecer exatamente uma vez → parar e sinalizar `blocked` razão `dependencia`.
  2. se `kit_check.ps1 -Mode generate` falhar → parar e sinalizar `blocked` razão `ferramenta`, devolvendo o stderr.
  3. **Redespacho de 2026-09-25 (AE-6):** a execução anterior deixou na árvore os passos 2, 3 (só `K1`) e 4 — medido pelo consultor: Verificação 1 dá `skills=12 linha=1`, Verificação 3 exit 0, Verificação 2 exit 1 só pela frase de contagem. Então: se `.claude/skills/mensagem-ao-dono/SKILL.md` já existe, conferir que é idêntico ao literal acima e, se diferir, sobrescrever com `Write`; se a linha `` | `mensagem-ao-dono` | `` já aparece uma vez no `README.md`, não reaplicar `K1` (a contingência 1 não vale para ela); aplicar `K2`, rodar o passo 4 e as Verificações 1 a 4. O "Medido antes" da Verificação 1 é, neste redespacho, `skills=12 linha=1`.
- **Testes:** nenhum novo (redação); a suíte inteira roda como TR — se algum teste contar skills e falhar pelo número 11 → 12, é `blocked` razão `premissa`, não edição de teste.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command '"skills=" + @(Get-ChildItem .claude/skills -Directory).Count + " linha=" + @(Select-String -LiteralPath README.md -SimpleMatch -Pattern "| ``mensagem-ao-dono`` |").Count'
     ```
     → **skills=12 linha=1**. **Medido antes: skills=11 linha=0**.
  2. ```
     pwsh -NoProfile -File .claude/checks/check-readme.ps1
     ```
     → **exit 0**. **Medido pelo consultor** numa cópia (`-Root`, apagada) com `K1` e `K2` aplicados: exit 0, `12 skill(s)`; sem `K2`, exit 1 (`declara 11 vs 12`).
  3. ```
     pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift
     ```
     → **exit 0**.
  4. ```
     python -m pytest tests -q
     ```
     → **nenhuma falha**, total igual ao da véspera.
- **Pronto quando:**
  - kit.procedimento da mensagem — skill com checagem, busca do título, pedido de decisão e registro de falha — Verificação 1, 2, 3
- **Fora do escopo desta tarefa:** propagação aos projetos derivados (`TK-81`); resolvedor sigla→título por função (DCH-10).
- **Notas de execução:**
  - 2026-09-25 `ready` — consultor: K2 (onze->doze skills) e contingencia 3 do redespacho, AE-6

### CAH-T5 — Os textos que mandavam citar sigla ao dono passam a mandar o título [Sonnet · esforço low · classe redacao]
- **Status:** `done` · 2026-09-25
- **Objetivo:** O mantenedor das superfícies troca, nos textos que hoje mandam citar identificador ao dono, a sigla sozinha pelo título entre aspas, e marca a fronteira do documento publicado.
- **Fundamento:** DCH-2, DCH-9; F-3; I-2, I-3.
- **Depende de:** `CAH-T1`, `CAH-T4`
- **Operação do modelo:** `OP-5`
  - OP-5: O mantenedor das superfícies troca, nos textos que hoje mandam citar identificador ao dono, a sigla sozinha pelo título entre aspas, e marca a fronteira do documento publicado.
  - precisa de: kit — Quem implementa recebe esses textos. O que esta entrega não toca continua valendo como hoje.
  - precisa de: próxima mensagem ao dono — Quem implementa não a escreve. Ela mostra se a regra pegou.
- **Camada e fronteira:** skills e agente do kit, só nos trechos dirigidos ao dono; a superfície agente↔agente fica intocada (I-3).
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
  - `.claude/agents/pantonic-planner.md`
  - `.claude/skills/redacao-doc/SKILL.md`
- **Texto novo, literal** (antigo → novo; `↵` é quebra de linha):

  ```text
  [S1] .claude/skills/scrum-master/SKILL.md
  - Plano conduzido e regra que encerrou a janela (`A1`..`A9`, inclusive `A3c`, `A6a` e `A8a`, ou `B0`..`B4`, pelo identificador).
  → - Plano conduzido, pelo título entre aspas, e a regra que encerrou a janela, pela condição dela em palavras (a coluna *condição* das tabelas dos blocos A e B), com o identificador entre parênteses (*Mensagem legível ao dono*, `GOVERNANCA.md` §4.2).

  [S2] .claude/skills/scrum-master/SKILL.md
  - Tarefas fechadas na janela, cada uma com identificador, desdobramento e caminho do RDO.
  → - Tarefas fechadas na janela, cada uma pelo título entre aspas, com desdobramento e caminho do RDO.

  [P1] .claude/agents/pantonic-planner.md
  opção sobre o plano. Toda questão de rota
  → opção sobre o plano; objeto citado vai pelo título entre aspas, nunca pela sigla sozinha (*Mensagem legível ao dono*, `GOVERNANCA.md` §4.2). Toda questão de rota

  [R1] .claude/skills/redacao-doc/SKILL.md
  **registro**), onde narrar é a função.
  → **registro**), onde narrar é a função. Mensagem de conversa ao dono não é documento publicado:↵
  segue *Mensagem legível ao dono* (`GOVERNANCA.md` §4.2) e a skill `mensagem-ao-dono`.
  ```
- **Passos:**
  1. Rodar a Verificação 1 e conferir os valores "antes".
  2. Aplicar `S1`, `S2`, `P1`, `R1` com `Edit`.
  3. Rodar a Verificação 1 a 3.
- **Restrições desta tarefa:** I-2 — só ponteiro para a regra; I-3 — nada muda nas tabelas dos blocos A e B nem no repertório do painel.
- **Não fazer:** não tocar `passagem-de-bastao`, a tabela `M-*`, os blocos A e B, nem o formato das pendências ao dono (`:295-296`); não reescrever outro trecho do `pantonic-planner`.
- **Contingências:**
  1. se algum texto antigo não aparecer exatamente uma vez no arquivo → parar e sinalizar `blocked` razão `dependencia`, devolvendo o código da troca.
- **Testes:** nenhum novo (redação); a suíte inteira roda como TR.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command '(@(foreach ($f in ".claude/skills/scrum-master/SKILL.md",".claude/agents/pantonic-planner.md",".claude/skills/redacao-doc/SKILL.md") { @(Select-String -LiteralPath $f -SimpleMatch -Pattern "Mensagem legível ao dono").Count })) -join " / "'
     ```
     → **1 / 1 / 1**. **Medido antes: 0 / 0 / 0**.
  2. ```
     pwsh -NoProfile -Command '"id=" + @(Select-String -LiteralPath .claude/skills/scrum-master/SKILL.md -SimpleMatch -Pattern "pelo identificador).").Count'
     ```
     → **id=0**. **Medido antes: id=1**.
  3. ```
     python -m pytest tests -q
     ```
     → **nenhuma falha**, total igual ao da véspera.
- **Pronto quando:**
  - kit.textos que mandam citar sigla — os dois mandam o título entre aspas; o documento publicado aponta para a regra — Verificação 1, 2
- **Fora do escopo desta tarefa:** a próxima mensagem ao dono (medição, não escrita); o painel (já conforme).

### CAH-T4a — O título de tarefa na skill da mensagem ao dono para antes da etiqueta [Sonnet · esforço low · classe redacao]
- **Status:** `done` · 2026-09-25
- **Objetivo:** Corretivo da `CAH-T4` (`AE-7`): a linha da §2 da skill `mensagem-ao-dono` que diz onde achar o título de tarefa, tíquete e plano passa a cortar a etiqueta `[modelo · esforço · classe]` que o cabeçalho de tarefa traz depois do título.
- **Fundamento:** DCH-4; AE-7. Medido pelo consultor (2026-09-25): `backlog.py show CAH-T4` → `### CAH-T4 — A skill da mensagem ao dono [Sonnet · esforço medium · classe redacao]`; `show TK-72` → `## TK-72 — A régua de autoria de card do kit`; `show P-0750` → `# P-0750 — Comunicação agente↔humano: …` — só a tarefa traz ` [`.
- **Depende de:** `CAH-T4`
- **Operação do modelo:** `OP-4`
  - OP-4: O autor de skill cria a skill da mensagem ao dono: a checagem antes de enviar, onde achar o título de cada sigla, o formato do pedido de decisão e o registro da falha; e a inscreve na anatomia do kit.
  - precisa de: kit — Quem implementa recebe esses textos. O que esta entrega não toca continua valendo como hoje.
- **Camada e fronteira:** corpo da skill; o frontmatter não muda, então `.claude/README.md` não muda (o gerador lê só `name` e `description`).
- **Arquivos-alvo:**
  - `.claude/skills/mensagem-ao-dono/SKILL.md` (uma célula da tabela da §2)
- **Texto novo, literal** (antigo → novo; recorte dentro da linha `| tarefa `<PFX>-T<n>`, tíquete …`):

  ```text
  [T1] .claude/skills/mensagem-ao-dono/SKILL.md
  — o título é o texto depois de ` — ` na primeira linha |
  → — o título é o texto da primeira linha entre ` — ` e ` [`; sem ` [` na linha, vai até o fim dela |
  ```
- **Passos:**
  1. Rodar a Verificação 1 e conferir o valor "antes".
  2. Aplicar `T1` com `Edit`.
  3. Rodar a Verificação 1 a 3.
- **Restrições desta tarefa:** I-2 — a skill segue só apontando para a regra.
- **Não fazer:** não tocar outra linha da skill nem o `README.md`; não rodar `kit_check.ps1 -Mode generate`; não editar o card da `CAH-T4`.
- **Contingências:**
  1. se o texto antigo de `T1` não aparecer exatamente uma vez → parar e sinalizar `blocked` razão `dependencia`.
- **Testes:** nenhum novo (redação); a suíte inteira roda como TR.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command '"novo=" + @(Select-String -LiteralPath .claude/skills/mensagem-ao-dono/SKILL.md -SimpleMatch -Pattern "entre `` — `` e `` [``").Count + " antigo=" + @(Select-String -LiteralPath .claude/skills/mensagem-ao-dono/SKILL.md -SimpleMatch -Pattern "o texto depois de").Count'
     ```
     → **novo=1 antigo=0**. **Medido antes: novo=0 antigo=1**; medido pelo consultor numa cópia com `T1` aplicado: `novo=1 antigo=0`.
  2. ```
     pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift
     ```
     → **exit 0**. Medido antes, na árvore: exit 0. Numa cópia de `.claude/` o comando falha só pela materialização (caminho absoluto do destino, 13 problemas) com e sem `T1` — a troca não acrescenta problema.
  3. ```
     python -m pytest tests -q
     ```
     → **nenhuma falha**, total igual ao da véspera.
- **Pronto quando:**
  - kit.procedimento da mensagem — a busca do título de tarefa corta a etiqueta — Verificação 1, 2
- **Fora do escopo desta tarefa:** resolvedor sigla→título por função (DCH-10); propagação aos derivados (`TK-81`).

## 6. Ordem de execução

`CAH-T1` (espera `SAN-T5` do `P-0749`) → `CAH-T2` → `CAH-T3` → `CAH-T4` → `CAH-T5` → `CAH-T4a`. `CAH-T2` e
`CAH-T3` não dependem uma da outra; a ordem é só sequencial. `CAH-T4a` (corretivo da `CAH-T4`, `AE-7`)
não depende da `CAH-T5` nem ela dele: vai depois só para não reordenar a fila já despachável.

## 7. Fora de escopo

- Resolvedor sigla→título por função (DCH-10) — **registrado e não agido**.
- Tradução de glossário ou skill (DCH-3).
- `apply` do regulamento global em `~/.claude/` (dono, F-7) e propagação aos derivados (`TK-81`).
- Unificação de prefixos colidentes (`DM-`, `DC-`, `D-`): os artefatos mantêm as siglas (I-1).
- A superfície agente↔agente (DCH-9).

## 8. Riscos

- **R-1** O `P-0749` não roda ou muda o texto do `SAN-T5` → `CAH-T1` fica `blocked` razão
  `dependencia` (contingência 1). Mitigação: a prioridade entre os planos é do dono (DCH-8).
- **R-2** A regra pega na doutrina mas não na conversa, porque o regulamento global só vale depois
  do `apply` do dono → a medição é a próxima mensagem ao dono e a tabela de falhas.
- **R-3** Teste que conta skills falha com 12 → `CAH-T4` para em `premissa`, sem editar teste.

## 9. Achados da execução

- **`AE-1`** (2026-09-25, laudo da `CAH-T1`, aprovado 100, bloqueante `nenhuma`, recomendação `seguir` — regra `A9`; RDO fechado como aprovado) — **Achado de processo (autoria):** o comando da Verificação 1 da `CAH-T1` tem um `)` a mais em `)))) {` — o `foreach` fica sem corpo e sai `ParserError`, exit 1, antes e depois da entrega; o *Medido antes* `0 / 0` não foi observado por ele. O revisor mediu com um `)` a menos: `1 / 1` depois, `0` e `0` na ref do despacho. **Rota:** sem corretivo — a tarefa fechou e a varredura do loop (`)))) {` no plano) só acha a linha 199, da própria `CAH-T1`; o caso vai à régua de autoria (`TK-72`: rodar o comando da Verificação uma vez no ato da autoria).
- **`AE-2`** (2026-09-25, mesmo laudo) — **Achado de processo (autoria):** a Verificação 3 da `CAH-T1` publica o total da suíte como literal de aceite (*Medido antes: 313 passed*, `F-9`), que envelheceu antes do despacho (353 passed, re-medido no despacho e na revisão), contra a RUBRICA §8 (x), (xiii) e (xviii). **Rota:** sem corretivo — o gate de delegação (item 3) já re-deriva o número a cada despacho, e a varredura (`Medido antes: <n> passed`) só acha a linha 209, da própria `CAH-T1`; recorrência do `AE-7` do `P-0749`, régua de autoria do `TK-72`.
- **`AE-3`** (2026-09-25, mesmo laudo) — **Achado de processo (instrumento):** o dossiê de evidência lista 20 não rastreados anteriores ao despacho como "fora dos alvos e sem atribuição" (`git stash create` não carrega não rastreados); reconciliado pelo revisor por mtime (todos até 16:42, despacho às 17:52:35). **Rota:** fora do plano, sem card — quarta recorrência do caso do `TK-55`/`TK-78c` (`AE-1` (c) e `AE-3` (c) do `P-0749`).
- **`AE-4`** (2026-09-25, laudo da `CAH-T2`, aprovado 100, bloqueante `nenhuma`, recomendação `seguir` — regra `A9`; RDO fechado como aprovado) — **Achado de processo (autoria):** o card da `CAH-T2` e o `F-1` ancoram o texto antigo por número de linha (`README.md` 178–181); entregas anteriores o deslocaram para 181–184. O despacho re-derivou a âncora e a execução casou pelo literal, sem efeito na entrega. **Rota:** sem corretivo — o gate de delegação (item 3) re-deriva por texto toda âncora de linha a cada despacho da `CAH-T3`..`CAH-T5`; candidato à régua de autoria (`TK-72`: âncora de edição é recorte literal, nunca número de linha). **Anexo:** quinta recorrência do `AE-3` (20 não rastreados anteriores ao despacho, reconciliados por mtime), mesma rota. O retorno do executor trouxe prosa depois da linha de retorno — caso do `TK-79`; a primeira linha estava na gramática e foi lida como o retorno.
- **`AE-5`** (2026-09-25, laudo da `CAH-T3`, aprovado 100, bloqueante `nenhuma`, recomendação `seguir` — regra `A9`; RDO fechado como aprovado) — **Achado de processo (instrumento):** sexta recorrência do `AE-3` (20 não rastreados anteriores ao despacho, reconciliados por mtime). **Rota:** a mesma do `AE-3`, caso novo no acumulador `TK-55`. **Lição anexa:** a Verificação 1 da `CAH-T3` (`csv.reader`) não discrimina BOM nem CRLF; o revisor conferiu os bytes à parte. Card futuro de TSV pede a checagem de bytes na própria Verificação (régua de autoria, `TK-72`).
- **`AE-6`** (2026-09-25, `CAH-T4` `blocked` razão `premissa`) — **Achado de processo (autoria):** o `F-6` descreveu só a paridade da tabela *Skills*; o `check-readme.ps1` também confere o numeral por extenso da frase de contagem da *Anatomia do kit* (`O kit são dez agentes, onze skills, …`), que o card não trocava — a Verificação 2 falhou (`declara 11 vs 12`). **Rota:** consultor, `rota=resolve` — troca literal `K2` (`onze` → `doze`) no card, medida numa cópia (`check-readme -Root`, exit 0), e contingência 3 do redespacho sobre a árvore deixada pela execução anterior. Régua de autoria (`TK-72`): card que cria ou apaga skill ou agente troca também o numeral da frase de contagem.
- **`AE-7`** (2026-09-25, laudo da `CAH-T4` no redespacho, aprovado 100, bloqueante `nenhuma`, recomendação `seguir` — regra `A9`; RDO fechado como aprovado) — **Achado de processo (autoria):** o literal da skill `mensagem-ao-dono` (§2, linha tarefa/tíquete/plano) diz que o título é "o texto depois de ` — ` na primeira linha" da saída de `backlog.py show`; para tarefa, esse texto inclui a etiqueta `[Sonnet · esforço medium · classe redacao]`, que não é título. A entrega copiou o literal fielmente. Rota do revisor: emenda literal da linha da §2 (título entre ` — ` e ` [`, quando houver), por card corretivo ou tíquete. **Rota:** consultor (acionamento 2), `rota=resolve` — corretivo `CAH-T4a` (troca literal `T1` de uma célula, medida numa cópia), depois da `CAH-T5`; sem mudança de objeto, operação nem estado final da `## 1`. Régua de autoria (`TK-72`): literal que descreve saída de instrumento se confere contra a saída medida de cada forma que ele cobre. **Anexo:** sétima recorrência do `AE-3`, mesma rota.
- **`AE-8`** (2026-09-25, laudo da `CAH-T5`, aprovado 100, bloqueante `nenhuma`, recomendação `seguir` — regra `A9`; RDO fechado como aprovado) — **Achado de processo (instrumento):** oitava recorrência do `AE-3` (20 não rastreados anteriores ao despacho, reconciliados pelo revisor). Rota do revisor: a captura do ref no passo 4 do `scrum-master` (stash com não rastreados, ou a lista deles passada ao `review_evidence.py`). **Rota:** a mesma do `AE-3`, acumulador `TK-55`, fora do plano; a proposta do revisor vai junto como caso.
- **`AE-9`** (2026-09-25, laudo da `CAH-T4a`, aprovado 100, bloqueante `nenhuma`, recomendação `seguir` — regra `A9`; RDO fechado como aprovado) — **Achado de processo (instrumento):** nona recorrência do `AE-3`; neste caso o próprio alvo, não rastreado, sai sem diff contra a ref, e o revisor conferiu o arquivo inteiro byte a byte contra o literal. **Rota:** a mesma do `AE-3`, acumulador `TK-55`, fora do plano.
