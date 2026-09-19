# RDO — P-0740 · LM-T9

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T9` — `consultant-spec`: a figura ad-hoc vira especificação
**Modelo:** Opus · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** converter os insumos de `## 9` — medidos durante a execução deste plano, não lembrados depois — em **um** documento, `docs/consultant-spec.md`, que descreva a figura do consultor de plano como ela **se comportou**: quando é acionada, o que decide sozinha, o que escala, qual é a fronteira com o `pantonic-planner` e qual é o custo dela. Um tema só: **a especificação da figura**. A `DM-28` é a régua: até este documento existir e ser aceito, o `pantonic-consultant` é ad-hoc e não se cita como fonte normativa.

**Arquivos-alvo:** - `docs/consultant-spec.md` — o documento (novo). - `docs/DOC_MAP.md` — a entrada de navegação do documento novo. - `CHANGELOG.md` — a linha do bloco não lançado.

**Verificação:** (os comandos foram extraídos deste card e rodados verbatim na autoria, 2026-09-19 — `DM-24`; reescrita na forma normativa da rubrica pelo `ESC-28`, com o literal `**Medido antes:**` que o `card_check` lê e **nenhuma** constante de corpus como aceite) 1. ``` pwsh -NoProfile -Command "[int](Test-Path docs/consultant-spec.md)" ``` → **1** depois. **Medido antes: 0**. 2. ``` pwsh -NoProfile -Command "(Select-String -Path docs/DOC_MAP.md -Pattern 'consultant-spec' -SimpleMatch | Measure-Object).Count" ``` → **≥ 1** depois. **Medido antes: 0**. 3. ``` pwsh -NoProfile -Command "if (Test-Path docs/consultant-spec.md) { [int]((Select-String -Path docs/consultant-spec.md -Pattern 'I-' -SimpleMatch | Measure-Object).Count) } else { 0 }" ``` → depois, **≥** a contagem de insumos `I-<n>` medida no despacho pelo comando de insumo abaixo. **Medido antes: 0** — o arquivo ainda não existe, e é isso que torna o valor **invariante**: ele mede o alvo do card, não o corpus que outras entregas movem (`ESC-28`). **Insumo do despacho, fora da lista e sem número de item** (não é aceite, é o número que o executor precisa ter à mão): ``` pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0740-loop-de-modulos.md -Pattern '^- \*\*.I-\d' | Measure-Object).Count" ``` mede quantos insumos `I-<n>` existem em `## 9` **no momento do despacho** — referência **datada**, nunca aceite: **8** na autoria (2026-09-19) e **10** em 2026-09-19 depois da `LM-T10`, que é a prova de que publicar essa contagem como constante envelheceria (`AE-49`). *Nota de autoria, `DM-24`:* a primeira forma deste comando usava `-SimpleMatch` com o padrão `- **I-` e devolveu **1** — casou a própria linha em que estava publicada e **nenhum** dos insumos, porque o identificador vem entre crases. Mesma classe do `AE-19`, pega antes do despacho por ter sido rodada. A forma acima é ancorada em início de linha, o que exclui a publicação.

**Pronto quando:** `docs/consultant-spec.md` existe, cobre as **oito** perguntas (a)..(h) — contagem fechada no mesmo ato que acrescentou (g) e (h), `DM-18` (i) —, cada uma com pelo menos um identificador de lastro, está indexado no `docs/DOC_MAP.md` e tem linha no `CHANGELOG.md`.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` · 2026-09-19
- **Esforço:** high
- **Depende de:** `LM-T6`. É penúltima por ordem do dono (2026-09-19, `DM-29`) — a spec se escreve depois que a figura tiver conduzido o plano inteiro, porque insumo de uma janela só não sustenta uma especificação. Na prática: despachar depois que a `LM-T6` fechar, com `## 9` já contendo os `I-<n>` das janelas posteriores a esta.
- **Produto do módulo:** `docs/consultant-spec.md` respondendo, com o insumo medido ao lado de cada resposta: (a) **gatilho** — o que aciona o consultor e o que não aciona; (b) **domínio de decisão** — o que ele fecha sozinho (técnico/tático) e o que sobe ao dono (estratégico, `G-NOASK`); (c) **fronteira com o `pantonic-planner`** — ele autorou cards novos nesta janela, e o documento tem de dizer se isso é da figura ou empréstimo; (d) **instrumento** — por que nasce com `Bash` (`DM-12`, `DM-24`); (e) **custo e teto** — 68,5% da janela num papel só é o número que a spec precisa endereçar, com a regra de quando **não** acionar. **Segunda medida, da janela de 2026-09-19:** **63%** (`3.802,2k` de `6.004,3k`), em **14** acionamentos — a spec tem **duas** janelas medidas e trata o número como **série**, não como constante (`DM-23`, `AE-21`); (f) **encerramento** — como a figura termina (decisão de janela × poluição, Regra 2); **(g) e (h), acrescentados por ato do dono em 2026-09-19 (`DM-45` (iii) e (iv)):** **(g) fim de vida por limite, e a sucessão** — o consultor **promove handover ao perceber que se aproxima do próprio limite** (estado do cenário, escalonamentos abertos, o que estava em curso), e o `scrum-master` **descomissiona a instância e provisiona outra**, repassando esse handover. A spec fixa **a forma de comunicação**, que nesta janela ficou **ad-hoc** por `DM-28` e por isso **não é fonte normativa** até ser projetada no plano próprio. Lastro medido: o `ESC-22`, em que a queda por *session limit* levou junto o contexto de 14 passagens e deixou o `AE-38` sem alocação e a `LM-T3b` sem varredura — o loop seguiu por medida própria no gate, mas o cenário acumulado **morreu**; **(h) estatística do próprio acionamento** — o consultor registra, a cada acionamento, **o que o motivou, que classe de impedimento era e o que ficou inconclusivo**, produzindo o **panorama dos pontos inconclusivos**. A spec diz **o que se coleta, onde mora e quem lê**. Destino declarado: **insumo da spec de robustez**. Lastro medido: 14 acionamentos e **63%** do consumo desta janela (`3.802,2k` de `6.004,3k`) sem **nenhum** registro estruturado de causa — `docs/telemetria.tsv` mede **custo**, não **motivo**; sem o panorama, a spec de robustez seria autorada sobre impressão.
- **Restrições desta tarefa (copiadas inline):** - **Descrever o medido, não o desejado.** Toda afirmação da spec sai de um `I-<n>` de `## 9` ou de um `AE-<n>`/`ESC-<n>` deste plano, citado pelo identificador. Afirmação sem lastro medido não entra — nem como recomendação. - **Não é doutrina ainda.** O documento é especificação de figura provisória: não altera `GOVERNANCA.md`, não cria guardrail `G-*`, não se declara fonte normativa. Promover a doutrina é ato posterior do dono (`DM-28`). - `redacao-doc`: sem narrativa de proveniência, sem citação de interlocutor, sem ID de processo no corpo — os identificadores entram como **lastro citado**, em nota ou tabela, não como historinha. - Não editar `.claude/agents/pantonic-consultant.md`. A definição do agente é outra superfície e outro tema; se a spec concluir que a definição diverge, o achado sai como `AE-<n>` com rota.
- **Não fazer:** não escrever a spec do `pantonic-planner` nem redesenhar o `scrum-master`; não absorver `TK-38`, `TK-54b` nem a matéria de confiabilidade (`DM-30`); não antecipar esta tarefa para antes da `LM-T6`.

## Execução

**Consumo:** 24 tool uses, 122.0 k tokens, 486.9 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: a divergencia definicao x pratica de (c) ja esta lastreada em I-5, entao nao abri AE novo nem toquei o plano
laudo: Artefato de validacao do marco 3 carrega tres afirmacoes falsificadas pelo proprio repositorio - decidir se corrige antes da leitura do dono: (1) 'a figura nao apensa linha de telemetria' contra 14 linhas ESC-23..ESC-36-consultor em docs/telemetria.tsv; (2) 3a instancia com consumo 'nao medido', quando ESC-27..ESC-36 tem tool_uses, tokens_k e duracao publicados; (3) censo 'tres instanciacoes / 33 acionamentos' omite a instancia ESC-23..ESC-26 e com ela a classe de gatilho do ESC-26.

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

Modulo mais barato da janela (122,0k tk / 24 tool uses / 486,9 s) para o maior artefato unico do plano (339 linhas). Observacao que o numero sozinho nao da: os tres defeitos encontrados nao sao de redacao - sao de conferencia contra a arvore (telemetria.tsv com 14 linhas ESC-*-consultor; censo de ESC-23..ESC-26), classe que nenhuma das tres linhas de Verificacao do card toca, porque todas medem presenca. Card de redacao cujo produto e 'descrever o medido' precisa de pelo menos uma linha de aceite que RE-MEDE a afirmacao central contra a fonte, e nao a presenca dela no texto.

## Fechamento

**Desdobramento:** aprovado com ressalva
